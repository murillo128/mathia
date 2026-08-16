from __future__ import annotations

import copy
import json
import re
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from experiments.intuition_fertility.canonical import canonical_json, stable_id
from experiments.intuition_fertility.conditions import (
    CALIBRATION_CONDITIONS,
    PRIMARY_CONDITIONS,
    Condition,
    ConditionCell,
    build_donor_condition,
    build_fixed_condition,
    build_relevant_condition,
    relevant_distant_length_eligibility,
)
from experiments.intuition_fertility.interchange import (
    ExperimentBundle,
    read_bundle,
    write_bundle,
)
from experiments.intuition_fertility.metrics import compute_metrics
from experiments.intuition_fertility.panel import (
    ADJACENT_DONORS,
    DISTANT_DONORS,
    INTUITION_REQUEST,
    PANEL_ID,
    Presentation,
    generator_payload,
    get_control,
    get_public_target,
    get_target_identity,
    panel_snapshot,
)
from experiments.intuition_fertility.prompts import (
    COMMENT_CLOSE,
    COMMENT_OPEN,
    PromptTemplate,
    import_rendered_prompt,
    inspect_prompt_parity,
    render_prompt,
)
from experiments.intuition_fertility.records import (
    FrozenIntuitionStore,
    GeneratorRole,
    IntuitionSample,
    LeakageDecision,
    LeakageDecisionStore,
    LeakageLabel,
    WhitespaceTokenCounter,
    deterministic_leakage_flags,
    sample_eligibility,
)
from experiments.intuition_fertility.results import (
    CandidateResult,
    CandidateResultStore,
    FormalWorkerRun,
    VerificationCategory,
    VerificationEvidence,
    VerifierStatus,
)

TOKENIZER = WhitespaceTokenCounter()
GENERATOR_CONFIG = {
    "provider": "fixture-provider",
    "model": "fixture-model",
    "revision": "fixture-revision",
    "parameters": {"temperature": 0},
}


def make_sample(
    theorem_id: str = "A",
    *,
    role: GeneratorRole = GeneratorRole.QWEN_BASE,
    text: str = "Use a propagation invariant and isolate the obstruction.",
    capture: str | None = None,
    config: dict | None = None,
    presentation: Presentation = Presentation.STANDARD,
    index: int = 0,
) -> IntuitionSample:
    return IntuitionSample.capture(
        theorem_id=theorem_id,
        presentation=presentation,
        generator_role=role,
        generator_config=config or GENERATOR_CONFIG,
        capture_identity=capture or f"fixture:{theorem_id}:{role.value}",
        sample_index=index,
        raw_text=text,
        token_counter=TOKENIZER,
    )


def make_decision(
    sample: IntuitionSample,
    label: LeakageLabel = LeakageLabel.STRATEGIC,
    *,
    uncertain: bool = False,
    disputed: bool = False,
) -> LeakageDecision:
    return LeakageDecision.create(
        sample=sample,
        classifier_identity={"kind": "fixture", "revision": "v1"},
        requested_label=label,
        uncertain=uncertain,
        disputed=disputed,
    )


def make_run(candidate_budget: int = 3) -> FormalWorkerRun:
    return FormalWorkerRun.create(
        qwen_lean_identity={
            "repository": "example/qwen-lean",
            "checkpoint": "supplied",
        },
        base_model_identity={"repository": "example/base", "revision": "supplied"},
        tokenizer_identity=TOKENIZER.identity,
        formal_environment_identity={"image": "fixture@sha256:123"},
        mathlib_revision="fixture-mathlib-revision",
        lean_version="fixture-lean-version",
        generation_settings={"temperature": 0.25, "top_p": 0.9},
        candidate_budget=candidate_budget,
        seeds=list(range(candidate_budget)),
    )


def make_template(theorem_id: str = "A") -> PromptTemplate:
    identity = get_target_identity(theorem_id)
    return PromptTemplate(
        prefix=b"import Mathlib\n\n",
        declaration=f"theorem {identity.canonical_target} : True := by\n".encode(),
    )


def make_result(
    *,
    run: FormalWorkerRun,
    cell: ConditionCell,
    prompt,
    index: int,
    verified: bool,
    generated_tokens: int | None = 10,
    runtime: float | None = 0.5,
) -> CandidateResult:
    identity = get_target_identity(cell.theorem_id)
    status = VerifierStatus.ACCEPTED if verified else VerifierStatus.REJECTED
    category = (
        VerificationCategory.VERIFIED_PROOF
        if verified
        else VerificationCategory.LEAN_REJECTION
    )
    evidence = VerificationEvidence.create(
        status=status,
        formal_environment_identity_id=run.formal_environment_identity_id,
        evidence={"returncode": 0 if verified else 1, "log_hash": f"log-{index}"},
    )
    return CandidateResult.capture(
        run=run,
        cell=cell,
        prompt=prompt,
        canonical_target=identity.canonical_target,
        theorem_record_id=identity.record_id,
        candidate_index=index,
        candidate_order=index + 1,
        raw_continuation="exact trivial" if verified else "invalid",
        finish_reason="stop",
        generation_metadata={"seed": index},
        verification_category=category,
        verification_evidence=evidence,
        generated_token_count=generated_tokens,
        runtime_seconds=runtime,
        runtime_comparability_id="fixture-runtime" if runtime is not None else None,
    )


class PanelTests(unittest.TestCase):
    def test_exact_panel_membership_and_roles(self) -> None:
        snapshot = panel_snapshot(include_private=True)
        self.assertEqual(
            [row["public"]["theorem_id"] for row in snapshot["targets"]],
            list("ABCDEFG"),
        )
        self.assertTrue(
            all(get_public_target(item).role == "primary" for item in "ABCDEF")
        )
        self.assertEqual(get_public_target("G").role, "calibration")
        self.assertEqual(
            PANEL_ID,
            "panel_d7c8fb558f3f5d1a4973864491f5fdf794e12e8bb0cb0b526361d77e72fc9f1c",
        )

    def test_corrected_de_names_and_legacy_provenance(self) -> None:
        d = get_target_identity("D")
        e = get_target_identity("E")
        self.assertEqual(
            d.canonical_target,
            "SimpleGraph.nonempty_hom_of_forall_finite_subgraph_hom",
        )
        self.assertEqual(e.canonical_target, "Relation.church_rosser")
        self.assertNotEqual(d.canonical_target, d.reported_artifact_target)
        self.assertNotEqual(e.canonical_target, e.reported_artifact_target)

    def test_generator_payload_is_only_public_statement_and_request(self) -> None:
        for theorem_id in "ABCDEFG":
            for presentation in Presentation:
                payload = generator_payload(theorem_id, presentation)
                self.assertEqual(
                    set(payload), {"theorem_statement", "intuition_request"}
                )
                self.assertEqual(payload["intuition_request"], INTUITION_REQUEST)
                serialized = canonical_json(payload)
                private = get_target_identity(theorem_id)
                for forbidden in (
                    private.canonical_target,
                    private.record_id,
                    private.source_path,
                    private.source_revision,
                    private.audit_mechanism_note,
                ):
                    self.assertNotIn(forbidden, serialized)

    def test_public_snapshot_is_private_by_default(self) -> None:
        public = canonical_json(panel_snapshot())
        private = canonical_json(panel_snapshot(include_private=True))
        self.assertNotIn("canonical_target", public)
        self.assertNotIn("record_id", public)
        self.assertNotIn("source_path", public)
        self.assertIn("canonical_target", private)

    def test_model_visible_primary_math_has_no_concrete_numerals(self) -> None:
        for theorem_id in "ABCDEF":
            public = get_public_target(theorem_id)
            text = " ".join(
                [
                    public.statement,
                    public.genericity_variant,
                    get_control(theorem_id).factual_control,
                ]
            )
            self.assertIsNone(re.search(r"[0-9]", text))

    def test_condition_contract_has_no_shuffled_condition(self) -> None:
        values = {condition.value for condition in PRIMARY_CONDITIONS}
        self.assertNotIn("shuffled_intuition", values)
        self.assertNotIn(
            Condition.ADJACENT_CROSS_THEOREM_STRATEGY, CALIBRATION_CONDITIONS
        )
        self.assertNotIn(Condition.DISTANT_MISMATCHED_STRATEGY, CALIBRATION_CONDITIONS)


class CanonicalAndIntuitionTests(unittest.TestCase):
    def test_object_key_order_does_not_change_identity(self) -> None:
        first = stable_id("fixture", {"b": 2, "a": {"y": 1, "x": 0}})
        second = stable_id("fixture", {"a": {"x": 0, "y": 1}, "b": 2})
        self.assertEqual(first, second)

    def test_provider_neutral_roles_and_round_trip(self) -> None:
        for role in GeneratorRole:
            sample = make_sample(role=role, capture=f"capture:{role.value}")
            self.assertEqual(IntuitionSample.from_dict(sample.to_dict()), sample)
            self.assertEqual(sample.generator_role, role.value)

    def test_same_input_same_identity_changed_text_changes_identity(self) -> None:
        first = make_sample(capture="stable")
        same = make_sample(
            capture="stable", config=dict(reversed(GENERATOR_CONFIG.items()))
        )
        changed = make_sample(capture="stable", text=first.raw_text + " More.")
        self.assertEqual(first, same)
        self.assertNotEqual(first.text_hash, changed.text_hash)
        self.assertNotEqual(first.sample_id, changed.sample_id)

    def test_frozen_record_and_store_conflicts(self) -> None:
        sample = make_sample(capture="frozen")
        with self.assertRaises(FrozenInstanceError):
            sample.raw_text = "mutated"  # type: ignore[misc]
        store = FrozenIntuitionStore()
        store.add(sample)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            store.add(sample)
        with self.assertRaisesRegex(ValueError, "already frozen"):
            store.add(make_sample(capture="frozen", text="Changed content."))

    def test_strict_tamper_and_unknown_field_rejection(self) -> None:
        sample = make_sample()
        tampered = sample.to_dict()
        tampered["raw_text"] += " altered"
        with self.assertRaisesRegex(ValueError, "does not match"):
            IntuitionSample.from_dict(tampered)
        malformed = sample.to_dict()
        malformed["quality_score"] = 1
        with self.assertRaisesRegex(ValueError, "unknown fields"):
            IntuitionSample.from_dict(malformed)

    def test_96_token_contract_preserves_raw_over_budget_sample(self) -> None:
        at_limit = make_sample(text=" ".join(["word"] * 96), capture="limit")
        over = make_sample(text=" ".join(["word"] * 97), capture="over")
        decision = make_decision(over)
        self.assertFalse(at_limit.over_budget)
        self.assertTrue(over.over_budget)
        self.assertEqual(over.token_count, 97)
        self.assertEqual(over.raw_text, " ".join(["word"] * 97))
        self.assertEqual(
            sample_eligibility(over, decision)[1], ("over_96_token_budget",)
        )


class LeakageTests(unittest.TestCase):
    def test_classifier_payload_is_blind(self) -> None:
        sample = make_sample()
        decision = make_decision(sample)
        payload = decision.classifier_payload()
        self.assertEqual(set(payload), {"theorem_statement", "candidate_guidance"})
        self.assertEqual(payload["candidate_guidance"], sample.raw_text)
        serialized = canonical_json(payload)
        self.assertNotIn(sample.generator_config_id, serialized)
        self.assertNotIn(get_target_identity("A").canonical_target, serialized)

    def test_all_labels_persist_and_uncertainty_is_borderline(self) -> None:
        samples = [
            make_sample(capture=f"sample:{label.value}") for label in LeakageLabel
        ]
        decisions = [
            make_decision(sample, label) for sample, label in zip(samples, LeakageLabel)
        ]
        self.assertEqual(
            {decision.label for decision in decisions},
            {label.value for label in LeakageLabel},
        )
        uncertain = make_decision(make_sample(capture="uncertain"), uncertain=True)
        disputed = make_decision(
            make_sample(capture="disputed"), LeakageLabel.PROOF_LIKE, disputed=True
        )
        self.assertEqual(uncertain.label, LeakageLabel.BORDERLINE.value)
        self.assertEqual(disputed.label, LeakageLabel.BORDERLINE.value)
        self.assertFalse(uncertain.primary_eligible)

    def test_external_decision_round_trip_and_conflict(self) -> None:
        sample = make_sample()
        decision = make_decision(sample)
        self.assertEqual(
            LeakageDecision.from_dict(decision.to_dict(), sample=sample), decision
        )
        store = LeakageDecisionStore()
        store.add(decision)
        with self.assertRaisesRegex(ValueError, "already"):
            store.add(decision)

    def test_rule_checks_only_overt_lean_markers(self) -> None:
        payload = {
            "theorem_statement": "Show the result.",
            "candidate_guidance": "theorem leaked : True := by\n  exact trivial",
        }
        self.assertIn("Lean declaration", deterministic_leakage_flags(payload))
        self.assertIn("Lean tactic", deterministic_leakage_flags(payload))
        with self.assertRaisesRegex(ValueError, "only"):
            deterministic_leakage_flags({**payload, "generator": "hidden"})


class ConditionTests(unittest.TestCase):
    def test_exact_mappings_and_roles(self) -> None:
        self.assertEqual(
            ADJACENT_DONORS,
            {"A": "E", "E": "A", "B": "C", "C": "B", "D": "F", "F": "D"},
        )
        self.assertEqual(
            DISTANT_DONORS, {"A": "C", "B": "D", "C": "E", "D": "B", "E": "C", "F": "B"}
        )
        anchor = make_sample("A", capture="anchor")
        donor = make_sample("E", capture="donor")
        cell = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=anchor,
            donor_kind="adjacent",
            donor_sample=donor,
            donor_decision=make_decision(donor),
        )
        self.assertEqual(cell.experimental_role, "transfer_probe")
        self.assertNotEqual(cell.experimental_role, "negative_control")

    def test_donor_binding_requires_frozen_mapping_and_same_config(self) -> None:
        anchor = make_sample("A", capture="anchor")
        wrong_target = make_sample("B", capture="wrong-target")
        with self.assertRaisesRegex(ValueError, "must be theorem C"):
            build_donor_condition(
                receiver_theorem_id="A",
                anchor_sample=anchor,
                donor_kind="distant",
                donor_sample=wrong_target,
                donor_decision=make_decision(wrong_target),
            )
        other_config = make_sample(
            "C", capture="other-config", config={"provider": "other", "model": "x"}
        )
        with self.assertRaisesRegex(ValueError, "same frozen generator"):
            build_donor_condition(
                receiver_theorem_id="A",
                anchor_sample=anchor,
                donor_kind="distant",
                donor_sample=other_config,
                donor_decision=make_decision(other_config),
            )

    def test_missing_or_invalid_donor_is_explicitly_ineligible(self) -> None:
        anchor = make_sample("A", capture="anchor")
        missing = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=anchor,
            donor_kind="distant",
            donor_sample=None,
            donor_decision=None,
        )
        self.assertFalse(missing.eligible)
        self.assertEqual(missing.ineligibility_reasons, ("missing_donor_sample",))
        donor = make_sample("C", capture="bad-donor")
        invalid = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=anchor,
            donor_kind="distant",
            donor_sample=donor,
            donor_decision=make_decision(donor, LeakageLabel.BORDERLINE),
        )
        self.assertFalse(invalid.eligible)
        self.assertIn("leakage_label_borderline", invalid.ineligibility_reasons)

    def test_length_criterion_is_exact(self) -> None:
        relevant_80 = make_sample("A", text=" ".join(["r"] * 80), capture="r80")
        distant_100 = make_sample("C", text=" ".join(["d"] * 100), capture="d100")
        relevant_cell = build_relevant_condition(
            sample=relevant_80, decision=make_decision(relevant_80)
        )
        distant_cell = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=relevant_80,
            donor_kind="distant",
            donor_sample=distant_100,
            donor_decision=make_decision(distant_100),
        )
        self.assertTrue(
            relevant_distant_length_eligibility(relevant_cell, distant_cell).eligible
        )

        relevant_79 = make_sample("A", text=" ".join(["r"] * 79), capture="r79")
        relevant_79_cell = build_relevant_condition(
            sample=relevant_79, decision=make_decision(relevant_79)
        )
        distant_79_anchor = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=relevant_79,
            donor_kind="distant",
            donor_sample=distant_100,
            donor_decision=make_decision(distant_100),
        )
        self.assertFalse(
            relevant_distant_length_eligibility(
                relevant_79_cell, distant_79_anchor
            ).eligible
        )

    def test_calibration_rejects_cross_and_primary_accepts_all_conditions(self) -> None:
        g = make_sample("G", capture="g")
        with self.assertRaisesRegex(ValueError, "no adjacent or distant"):
            build_donor_condition(
                receiver_theorem_id="G",
                anchor_sample=g,
                donor_kind="distant",
                donor_sample=None,
                donor_decision=None,
            )
        relevant = build_relevant_condition(sample=g, decision=make_decision(g))
        self.assertTrue(relevant.eligible)

    def test_condition_interchange_revalidates_donor_binding(self) -> None:
        anchor = make_sample("A", capture="anchor")
        donor = make_sample("C", capture="donor")
        decisions = {
            anchor.sample_id: make_decision(anchor),
            donor.sample_id: make_decision(donor),
        }
        cell = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=anchor,
            donor_kind="distant",
            donor_sample=donor,
            donor_decision=decisions[donor.sample_id],
        )
        rebuilt = ConditionCell.from_dict(
            cell.to_dict(),
            samples={anchor.sample_id: anchor, donor.sample_id: donor},
            decisions=decisions,
        )
        self.assertEqual(rebuilt, cell)


class PromptTests(unittest.TestCase):
    def test_no_guidance_is_exact_baseline(self) -> None:
        cell = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.NO_GUIDANCE,
            token_counter=TOKENIZER,
        )
        template = make_template()
        prompt = render_prompt(template, cell)
        self.assertEqual(prompt.prompt_bytes, template.baseline)
        self.assertTrue(
            inspect_prompt_parity(template, prompt)["non_intervention_bytes_identical"]
        )

    def test_guidance_is_one_inspectable_comment_before_exact_declaration(self) -> None:
        cell = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.FACTUAL_CONTROL,
            token_counter=TOKENIZER,
        )
        template = make_template()
        prompt = render_prompt(template, cell)
        parity = inspect_prompt_parity(template, prompt)
        self.assertTrue(parity["non_intervention_bytes_identical"])
        self.assertTrue(
            prompt.prompt_bytes[parity["insertion_start"] :].startswith(COMMENT_OPEN)
        )
        self.assertIn(COMMENT_CLOSE + template.declaration, prompt.prompt_bytes)
        self.assertTrue(prompt.prompt_bytes.endswith(b":= by\n"))

    def test_comment_breakers_are_deterministically_escaped_without_mutating_raw(
        self,
    ) -> None:
        raw = "Use /- nested-looking -/ structure."
        sample = make_sample(text=raw, capture="comment-breaker")
        cell = build_relevant_condition(sample=sample, decision=make_decision(sample))
        prompt = render_prompt(make_template(), cell)
        insertion = inspect_prompt_parity(make_template(), prompt)["inserted_utf8"]
        self.assertNotIn("/- nested-looking -/", insertion)
        self.assertIn("/ - nested-looking - /", insertion)
        self.assertEqual(sample.raw_text, raw)
        self.assertEqual(cell.guidance_hash, sample.text_hash)

    def test_prompt_import_rejects_nonintervention_tampering(self) -> None:
        cell = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.GENERIC_STRATEGY_CONTROL,
            token_counter=TOKENIZER,
        )
        prompt = render_prompt(make_template(), cell)
        self.assertEqual(import_rendered_prompt(prompt.to_dict(), cell=cell), prompt)
        tampered = prompt.to_dict()
        tampered["baseline_prompt_utf8"] = tampered["baseline_prompt_utf8"].replace(
            "Mathlib", "Other"
        )
        with self.assertRaisesRegex(ValueError, "hash"):
            import_rendered_prompt(tampered, cell=cell)


class ResultTests(unittest.TestCase):
    def setUp(self) -> None:
        self.run = make_run(candidate_budget=5)
        self.cell = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.NO_GUIDANCE,
            token_counter=TOKENIZER,
        )
        self.prompt = render_prompt(make_template(), self.cell)
        self.identity = get_target_identity("A")

    def capture_category(
        self,
        category: VerificationCategory,
        evidence_status: VerifierStatus | None,
        *,
        continuation: str = "candidate",
    ) -> CandidateResult:
        evidence = None
        if evidence_status is not None:
            evidence = VerificationEvidence.create(
                status=evidence_status,
                formal_environment_identity_id=self.run.formal_environment_identity_id,
                evidence={"category": category.value},
            )
        return CandidateResult.capture(
            run=self.run,
            cell=self.cell,
            prompt=self.prompt,
            canonical_target=self.identity.canonical_target,
            theorem_record_id=self.identity.record_id,
            candidate_index=0,
            candidate_order=1,
            raw_continuation=continuation,
            finish_reason="fixture",
            generation_metadata={},
            verification_category=category,
            verification_evidence=evidence,
        )

    def test_five_verification_states_stay_distinct(self) -> None:
        cases = [
            (VerificationCategory.VERIFIED_PROOF, VerifierStatus.ACCEPTED, "proof"),
            (VerificationCategory.LEAN_REJECTION, VerifierStatus.REJECTED, "bad proof"),
            (VerificationCategory.EMPTY_GENERATION_FAILURE, None, ""),
            (VerificationCategory.VERIFIER_TIMEOUT, VerifierStatus.TIMEOUT, "partial"),
            (
                VerificationCategory.VERIFIER_INFRASTRUCTURE_ERROR,
                VerifierStatus.ERROR,
                "partial",
            ),
        ]
        observed = {
            self.capture_category(
                category, status, continuation=text
            ).verification_category
            for category, status, text in cases
        }
        self.assertEqual(
            observed, {category.value for category in VerificationCategory}
        )

    def test_verified_requires_accepted_formal_evidence(self) -> None:
        with self.assertRaisesRegex(ValueError, "requires verifier status accepted"):
            self.capture_category(
                VerificationCategory.VERIFIED_PROOF,
                VerifierStatus.REJECTED,
                continuation="fluent but unverified",
            )
        with self.assertRaisesRegex(ValueError, "non-empty"):
            self.capture_category(
                VerificationCategory.VERIFIED_PROOF,
                VerifierStatus.ACCEPTED,
                continuation="",
            )

    def test_result_cannot_be_rebound_to_target_prompt_or_condition(self) -> None:
        with self.assertRaisesRegex(ValueError, "target identity"):
            CandidateResult.capture(
                run=self.run,
                cell=self.cell,
                prompt=self.prompt,
                canonical_target="Relation.church_rosser",
                theorem_record_id=self.identity.record_id,
                candidate_index=0,
                candidate_order=1,
                raw_continuation="candidate",
                finish_reason="stop",
                generation_metadata={},
                verification_category=VerificationCategory.EMPTY_GENERATION_FAILURE,
                verification_evidence=None,
            )
        other_cell = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.FACTUAL_CONTROL,
            token_counter=TOKENIZER,
        )
        with self.assertRaisesRegex(ValueError, "not bound"):
            CandidateResult.capture(
                run=self.run,
                cell=other_cell,
                prompt=self.prompt,
                canonical_target=self.identity.canonical_target,
                theorem_record_id=self.identity.record_id,
                candidate_index=0,
                candidate_order=1,
                raw_continuation="candidate",
                finish_reason="stop",
                generation_metadata={},
                verification_category=VerificationCategory.EMPTY_GENERATION_FAILURE,
                verification_evidence=None,
            )

    def test_run_and_result_round_trip_without_frozen_scientific_choices(self) -> None:
        self.assertEqual(FormalWorkerRun.from_dict(self.run.to_dict()), self.run)
        result = self.capture_category(
            VerificationCategory.LEAN_REJECTION, VerifierStatus.REJECTED
        )
        self.assertEqual(
            CandidateResult.from_dict(
                result.to_dict(), run=self.run, cell=self.cell, prompt=self.prompt
            ),
            result,
        )
        self.assertEqual(self.run.candidate_budget, 5)
        self.assertEqual(self.run.mathlib_revision, "fixture-mathlib-revision")

    def test_duplicate_candidate_slots_are_rejected(self) -> None:
        result = self.capture_category(
            VerificationCategory.LEAN_REJECTION, VerifierStatus.REJECTED
        )
        store = CandidateResultStore()
        store.add(result)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            store.add(result)


class MetricAndBundleTests(unittest.TestCase):
    def build_metric_fixture(self):
        run = make_run(3)
        template_a = make_template("A")
        baseline = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.NO_GUIDANCE,
            token_counter=TOKENIZER,
        )
        factual = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.FACTUAL_CONTROL,
            token_counter=TOKENIZER,
        )
        generic = build_fixed_condition(
            theorem_id="A",
            presentation=Presentation.STANDARD,
            condition=Condition.GENERIC_STRATEGY_CONTROL,
            token_counter=TOKENIZER,
        )
        relevant_sample = make_sample(
            "A", text=" ".join(["relevant"] * 10), capture="metric-relevant"
        )
        distant_sample = make_sample(
            "C", text=" ".join(["distant"] * 5), capture="metric-distant"
        )
        relevant_decision = make_decision(relevant_sample)
        distant_decision = make_decision(distant_sample)
        relevant = build_relevant_condition(
            sample=relevant_sample, decision=relevant_decision
        )
        distant = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=relevant_sample,
            donor_kind="distant",
            donor_sample=distant_sample,
            donor_decision=distant_decision,
        )
        cells = [baseline, factual, generic, relevant, distant]
        prompts = {cell.cell_id: render_prompt(template_a, cell) for cell in cells}
        patterns = {
            baseline.cell_id: [False, True, False],
            factual.cell_id: [False, False, False],
            generic.cell_id: [False, True, False],
            relevant.cell_id: [False, True, True],
            distant.cell_id: [False, False, False],
        }
        results = []
        for cell in cells:
            for index, verified in enumerate(patterns[cell.cell_id]):
                results.append(
                    make_result(
                        run=run,
                        cell=cell,
                        prompt=prompts[cell.cell_id],
                        index=index,
                        verified=verified,
                        generated_tokens=10 + index,
                    )
                )
        return {
            "run": run,
            "cells": cells,
            "prompts": list(prompts.values()),
            "samples": [relevant_sample, distant_sample],
            "decisions": [relevant_decision, distant_decision],
            "results": results,
            "relevant": relevant,
            "distant": distant,
        }

    def test_yield_pass_rank_tokens_runtime_and_matched_deltas(self) -> None:
        fixture = self.build_metric_fixture()
        report = compute_metrics(
            runs=[fixture["run"]],
            cells=fixture["cells"],
            results=fixture["results"],
            samples=fixture["samples"],
            decisions=fixture["decisions"],
        )
        relevant = next(
            item
            for item in report.cell_metrics
            if item.condition_cell_id == fixture["relevant"].cell_id
        )
        self.assertEqual(relevant.verified_count, 2)
        self.assertEqual(relevant.verified_rate, 2 / 3)
        self.assertTrue(relevant.pass_at_k)
        self.assertEqual(relevant.first_verified_rank, 2)
        self.assertEqual(relevant.generated_tokens_to_first_verified, 21)
        self.assertTrue(relevant.runtime_comparable)
        controls = {
            item.control_condition: item
            for item in report.matched_comparisons
            if item.condition_cell_id == fixture["relevant"].cell_id
        }
        self.assertAlmostEqual(controls["no_guidance"].raw_verified_rate_delta, 1 / 3)
        self.assertAlmostEqual(
            controls["factual_control"].raw_verified_rate_delta, 2 / 3
        )
        self.assertIn("distant_mismatched_strategy", controls)

    def test_length_ineligible_raw_result_remains_visible_but_cannot_support_claim(
        self,
    ) -> None:
        fixture = self.build_metric_fixture()
        report = compute_metrics(
            runs=[fixture["run"]],
            cells=fixture["cells"],
            results=fixture["results"],
        )
        comparison = next(
            item
            for item in report.matched_comparisons
            if item.condition_cell_id == fixture["relevant"].cell_id
            and item.control_condition == "distant_mismatched_strategy"
        )
        self.assertAlmostEqual(comparison.raw_verified_rate_delta, 2 / 3)
        self.assertFalse(comparison.content_claim_eligible)
        self.assertIn("length_difference", comparison.exclusion_reasons[0])

    def test_missing_donor_cell_remains_visible_as_ineligible(self) -> None:
        sample = make_sample("A", capture="missing-donor-anchor")
        missing = build_donor_condition(
            receiver_theorem_id="A",
            anchor_sample=sample,
            donor_kind="distant",
            donor_sample=None,
            donor_decision=None,
        )
        report = compute_metrics(
            runs=[make_run(1)],
            cells=[missing],
            results=[],
            samples=[sample],
            decisions=[make_decision(sample)],
        )
        self.assertEqual(report.ineligible_cells[0].condition_cell_id, missing.cell_id)
        self.assertEqual(
            report.ineligible_cells[0].ineligibility_reasons,
            ("missing_donor_sample",),
        )

    def test_presentations_are_not_merged_in_matched_metrics(self) -> None:
        run = make_run(1)
        cells = []
        results = []
        for presentation in Presentation:
            cell = build_fixed_condition(
                theorem_id="A",
                presentation=presentation,
                condition=Condition.NO_GUIDANCE,
                token_counter=TOKENIZER,
            )
            prompt = render_prompt(make_template("A"), cell)
            cells.append(cell)
            results.append(
                make_result(
                    run=run,
                    cell=cell,
                    prompt=prompt,
                    index=0,
                    verified=presentation is Presentation.STANDARD,
                )
            )
        report = compute_metrics(runs=[run], cells=cells, results=results)
        self.assertEqual(
            {aggregate.presentation for aggregate in report.primary_aggregates},
            {presentation.value for presentation in Presentation},
        )

    def test_leakage_rates_include_excluded_samples(self) -> None:
        samples = [
            make_sample(capture="strategic"),
            make_sample(capture="borderline", index=1),
            make_sample(capture="proof-like", index=2),
        ]
        decisions = [
            make_decision(samples[0], LeakageLabel.STRATEGIC),
            make_decision(samples[1], LeakageLabel.BORDERLINE),
            make_decision(samples[2], LeakageLabel.PROOF_LIKE),
        ]
        report = compute_metrics(
            runs=[], cells=[], results=[], samples=samples, decisions=decisions
        )
        summary = report.leakage_summaries[0]
        self.assertEqual(summary.total_samples, 3)
        self.assertEqual(summary.strategic_count, 1)
        self.assertEqual(summary.borderline_count, 1)
        self.assertEqual(summary.proof_like_count, 1)
        self.assertEqual(summary.proof_like_rate, 1 / 3)

    def test_g_is_visible_but_excluded_from_primary_aggregate(self) -> None:
        fixture = self.build_metric_fixture()
        run = fixture["run"]
        g_cell = build_fixed_condition(
            theorem_id="G",
            presentation=Presentation.STANDARD,
            condition=Condition.NO_GUIDANCE,
            token_counter=TOKENIZER,
        )
        g_prompt = render_prompt(make_template("G"), g_cell)
        g_results = [
            make_result(
                run=run,
                cell=g_cell,
                prompt=g_prompt,
                index=index,
                verified=True,
            )
            for index in range(3)
        ]
        report = compute_metrics(
            runs=[run],
            cells=[*fixture["cells"], g_cell],
            results=[*fixture["results"], *g_results],
        )
        self.assertTrue(any(item.theorem_id == "G" for item in report.cell_metrics))
        self.assertTrue(
            all(
                "G" not in aggregate.theorem_ids
                for aggregate in report.primary_aggregates
            )
        )

    def test_bundle_is_order_independent_strict_and_round_trippable(self) -> None:
        fixture = self.build_metric_fixture()
        bundle = ExperimentBundle.create(
            samples=fixture["samples"],
            decisions=fixture["decisions"],
            cells=fixture["cells"],
            prompts=fixture["prompts"],
            runs=[fixture["run"]],
            results=fixture["results"],
        )
        reversed_bundle = ExperimentBundle.create(
            samples=reversed(fixture["samples"]),
            decisions=reversed(fixture["decisions"]),
            cells=reversed(fixture["cells"]),
            prompts=reversed(fixture["prompts"]),
            runs=[fixture["run"]],
            results=reversed(fixture["results"]),
        )
        self.assertEqual(bundle.bundle_id, reversed_bundle.bundle_id)
        self.assertEqual(ExperimentBundle.from_dict(bundle.to_dict()), bundle)
        malformed = copy.deepcopy(bundle.to_dict())
        malformed["unexpected"] = True
        with self.assertRaisesRegex(ValueError, "unknown fields"):
            ExperimentBundle.from_dict(malformed)
        with self.assertRaisesRegex(ValueError, "unknown leakage decision"):
            ExperimentBundle.create(
                samples=fixture["samples"],
                decisions=[],
                cells=fixture["cells"],
                prompts=fixture["prompts"],
                runs=[fixture["run"]],
                results=fixture["results"],
            )

    def test_bundle_file_transport_and_metric_identity(self) -> None:
        fixture = self.build_metric_fixture()
        bundle = ExperimentBundle.create(
            samples=fixture["samples"],
            decisions=fixture["decisions"],
            cells=fixture["cells"],
            prompts=fixture["prompts"],
            runs=[fixture["run"]],
            results=fixture["results"],
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bundle.json"
            write_bundle(path, bundle)
            loaded = read_bundle(path)
        self.assertEqual(loaded.bundle_id, bundle.bundle_id)
        self.assertEqual(loaded.metrics().report_id, bundle.metrics().report_id)
        self.assertEqual(json.loads(canonical_json(loaded.to_dict())), loaded.to_dict())


if __name__ == "__main__":
    unittest.main()
