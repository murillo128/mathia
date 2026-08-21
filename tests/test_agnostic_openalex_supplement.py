import tempfile
import unittest
from pathlib import Path

from experiments import execution_provenance
from experiments.agnostic_mathia_corpus.openalex_supplement_v1 import pipeline
from experiments.riemann_corpus import full_corpus_v2 as issue42


def _write_synthetic_bundle(artifact_root: Path) -> dict:
    handoff_id = pipeline.HANDOFF_ID
    bundle = artifact_root / "openalex_handoffs" / handoff_id
    (bundle / "raw").mkdir(parents=True)
    (bundle / "normalized").mkdir()
    raw = bundle / "raw" / "w700.pdf"
    normalized = bundle / "normalized" / "w700.txt"
    raw.write_bytes(b"%PDF synthetic agnostic supplement\n")
    normalized.write_text(
        "Let X carry a structural relation.\n"
        "A representation preserves that relation.\n"
        "This line supplies bounded context.\n"
        "References.\n",
        encoding="utf-8",
    )
    manifest_row = {
        "access_boundary": "publicly accessible; redistribution rights not inferred",
        "acquisition_route": "synthetic-test",
        "authors": ["Test Author"],
        "candidate_public_locations": [],
        "doi": "10.0000/agnostic-700",
        "duplicate_relationships": [],
        "effective_url": "https://example.test/agnostic-700.pdf",
        "handoff_version": handoff_id,
        "ids": {"openalex": "https://openalex.org/W700"},
        "license": None,
        "normalization": {
            "media_type": "application/pdf",
            "warnings": ["synthetic fixture"],
        },
        "normalized_bytes": normalized.stat().st_size,
        "normalized_lines": 4,
        "normalized_path": str(normalized),
        "normalized_sha256": pipeline.sha256_file(normalized),
        "open_access": {"is_oa": True},
        "openalex_id": "https://openalex.org/W700",
        "priority": 1.0,
        "raw_bytes": raw.stat().st_size,
        "raw_path": str(raw),
        "raw_sha256": pipeline.sha256_file(raw),
        "relevance": {
            "ecosystem_lens_ids": ["representation_change"],
            "candidate_family_ids": [],
            "novelty_boundary": "metadata is not mathematical validation",
        },
        "snapshot": {"date": "2026-08-20"},
        "source_id": "openalex_agnostic_mathia_w700",
        "source_version": "publishedVersion",
        "title": "Synthetic agnostic source",
        "type": "article",
        "year": 2026,
    }
    manifest = bundle / "manifest.jsonl"
    pipeline.write_jsonl(manifest, [manifest_row])
    files = []
    for path in (manifest, normalized, raw):
        files.append(
            {
                "path": path.relative_to(bundle).as_posix(),
                "sha256": pipeline.sha256_file(path),
                "bytes": path.stat().st_size,
            }
        )
    pipeline.write_json(
        bundle / "freeze.json",
        {
            "consumer_contract": "synthetic offline consumer contract",
            "files": files,
            "freeze_id": issue42.OPENALEX_HANDOFF_SPECS[handoff_id]["freeze_id"],
            "frozen_at": "2026-08-20T00:00:00+00:00",
            "handoff_version": handoff_id,
            "immutable": True,
            "manifest_sha256": pipeline.sha256_file(manifest),
            "pipeline_version": "openalex-offline-discovery-v1",
            "source_count": 1,
            "stream": pipeline.HANDOFF_STREAM,
        },
    )
    return issue42._validate_openalex_handoff_bundle(
        bundle, handoff_id, pipeline.HANDOFF_STREAM
    )


def _setup_intake(root: Path) -> tuple[pipeline.SupplementLayout, Path]:
    layout = pipeline.SupplementLayout(root / "supplement")
    layout.root.mkdir(parents=True)
    layout.parent.write_text(pipeline.HERE.joinpath("parent.json").read_text(encoding="utf-8"), encoding="utf-8")
    artifact_root = root / "external-artifacts"
    bundle = _write_synthetic_bundle(artifact_root)
    classification = {
        "canonical_source_id": "openalex_w700",
        "handoff_source_id": "openalex_agnostic_mathia_w700",
        "disposition": "accepted_for_agnostic_supplement_analysis",
        "reason": "synthetic exact-identity miss",
        "identity_keys": [
            "doi:10.0000/agnostic-700",
            "openalex:openalex_w700",
        ],
        "matched_source_ids": [],
    }
    pipeline.write_jsonl(
        layout.intake,
        [
            issue42._handoff_source_ledger_record(
                bundle, bundle["rows"][0], classification
            )
        ],
    )
    return layout, artifact_root


def _write_screening(layout: pipeline.SupplementLayout) -> None:
    assignment = pipeline.load_json(next(layout.screening_assignments.glob("*.json")))
    source = assignment["source"]
    pipeline.write_jsonl(
        Path(assignment["output_path"]),
        [
            {
                "source_id": source["source_id"],
                "handoff_source_id": source["handoff_source_id"],
                "decision": "useful",
                "mathematical_scope": "Structural relations and representation change.",
                "usefulness_reason": "The source exposes a bounded representation mechanism.",
                "duplicate_or_version_note": "No exact #44 identity match is asserted.",
                "extraction_risk": "Synthetic plain text has no material extraction risk.",
                "proposed_lens_ids": ["representation_change"],
                "proposed_new_family_ids": [],
                "reviewer_provenance": {
                    "kind": "fresh-source-screening",
                    "model": "synthetic-test",
                    "context_id": "screening-test",
                },
            }
        ],
    )
    pipeline.combine_source_screening(layout)


def _write_depth_plan(layout: pipeline.SupplementLayout) -> None:
    assignment = pipeline.load_json(next(layout.depth_assignments.glob("*.json")))
    source = assignment["source"]
    pipeline.write_jsonl(
        Path(assignment["output_path"]),
        [
            {
                "source_id": source["source_id"],
                "normalized_sha256": source["normalized_sha256"],
                "inspection_summary": "All four synthetic logical lines inspected.",
                "coverage_segments": [
                    {
                        "line_start": 1,
                        "line_end": 2,
                        "disposition": "unit-bearing",
                        "reason": "The two lines jointly state the mechanism.",
                    },
                    {
                        "line_start": 3,
                        "line_end": 3,
                        "disposition": "supporting-context",
                        "reason": "Bounded context only.",
                    },
                    {
                        "line_start": 4,
                        "line_end": 4,
                        "disposition": "bibliography-or-front-matter",
                        "reason": "Reference marker.",
                    },
                ],
                "accepted_units": [
                    {
                        "local_unit_id": "agnostic_oa_representation_relation",
                        "unit_type": "conceptual-mechanism",
                        "title": "Representation preserves a structural relation",
                        "line_start": 1,
                        "line_end": 2,
                        "why_material": "It states what the representation preserves.",
                        "context_note": "The claim is deliberately generic.",
                        "representation_dependency": "Depends on the unspecified structural relation.",
                    }
                ],
                "ecosystem_findings": [
                    {
                        "kind": "reinforced_44_lens",
                        "identifier": "representation_change",
                        "evidence_unit_ids": ["agnostic_oa_representation_relation"],
                        "summary": "The unit reinforces preservation under representation change.",
                    }
                ],
                "remaining_meaningful_material": [],
                "stop_reason": "Every line has an explicit disposition.",
                "reviewer_provenance": {
                    "kind": "fresh-whole-source-depth-plan",
                    "model": "synthetic-test",
                    "context_id": "depth-test",
                },
            }
        ],
    )


def _write_analysis_and_audit(
    layout: pipeline.SupplementLayout, artifact_root: Path, critic_decision: str = "accept_as_is"
) -> None:
    pipeline.prepare_analysis_stage("generation", layout, artifact_root)
    generation_assignment = pipeline.load_json(
        next(layout.analysis_assignments("generation").glob("*.json"))
    )
    unit_id = generation_assignment["units"][0]["unit_id"]
    pipeline.write_jsonl(
        Path(generation_assignment["output_path"]),
        [
            {
                "analysis_id": generation_assignment["expected_analysis_ids"][unit_id],
                "unit_id": unit_id,
                "interpretation": "The representation is useful because it preserves the named relation while changing presentation.",
                "source_support": "The exact two-line unit states the relation and its preservation.",
                "nonparaphrase_operation": "Separates the preserved structure from the chosen representation.",
                "boundary_or_failure": "No preservation claim follows for an unrelated structure.",
                "uncertainty": "The source excerpt leaves the relation abstract.",
                "teacher_provenance": {
                    "kind": "source-grounded-generation",
                    "model_family": "synthetic-test",
                    "exact_service_checkpoint": "synthetic-test-v1",
                    "agent_task_path": "/root/synthetic-generation",
                    "review_scope": "Exact synthetic unit and generated assignment only.",
                },
            }
        ],
    )
    pipeline.prepare_analysis_stage("critic", layout, artifact_root)
    critic_assignment = pipeline.load_json(
        next(layout.analysis_assignments("critic").glob("*.json"))
    )
    pipeline.write_jsonl(
        Path(critic_assignment["output_path"]),
        [
            {
                "analysis_id": critic_assignment["expected_analysis_ids"][unit_id],
                "unit_id": unit_id,
                "decision": critic_decision,
                "faithfulness": "The interpretation remains within the two-line source claim.",
                "unsupported_or_imported": "None identified.",
                "paraphrase_risk": "Low because the response separates structure from representation.",
                "context_risk": "The abstract relation limits specificity.",
                "missed_mechanism": "No material mechanism omitted.",
                "revision_instructions": "Preserve the boundary if revision is requested.",
                "critic_provenance": {
                    "kind": "fresh-isolated-critic",
                    "model_family": "synthetic-test",
                    "exact_service_checkpoint": "synthetic-test-v1",
                    "agent_task_path": "/root/synthetic-critic",
                    "review_scope": "Exact synthetic unit and compact candidate only.",
                },
            }
        ],
    )
    pipeline.prepare_analysis_stage("revision", layout, artifact_root)
    if critic_decision == "revise":
        revision_assignment = pipeline.load_json(
            next(layout.analysis_assignments("revision").glob("*.json"))
        )
        pipeline.write_jsonl(
            Path(revision_assignment["output_path"]),
            [
                {
                    "analysis_id": revision_assignment["expected_analysis_ids"][unit_id],
                    "unit_id": unit_id,
                    "decision": "accepted",
                    "interpretation": "A change of representation is controlled here only by preservation of the specified relation.",
                    "source_support": "Both source lines are used and no external theorem is imported.",
                    "nonparaphrase_operation": "Makes the preservation condition the test for a legitimate change of presentation.",
                    "boundary_or_failure": "The statement does not cover structures other than the specified relation.",
                    "uncertainty": "The exact kind of relation remains abstract.",
                    "quality_reason": "The bounded repair makes the preservation criterion explicit.",
                    "teacher_provenance": {
                        "kind": "bounded-source-grounded-revision",
                        "model_family": "synthetic-test",
                        "exact_service_checkpoint": "synthetic-test-v1",
                        "agent_task_path": "/root/synthetic-revision",
                        "review_scope": "Exact synthetic unit, candidate, and critic only.",
                    },
                }
            ],
        )
    pipeline.finalize_analysis(layout)
    pipeline.prepare_independent_audit(layout, artifact_root)
    audit_assignment = pipeline.load_json(next(layout.audit_assignments.glob("*.json")))
    pipeline.write_jsonl(
        Path(audit_assignment["output_path"]),
        [
            {
                "unit_id": unit_id,
                "decision": "accept",
                "faithfulness": "The interpretation is supported by the exact source unit.",
                "context_sufficiency": "The unit is self-contained for this generic claim.",
                "nonparaphrase_value": "It identifies preservation as the selection test.",
                "specificity": "Specific to a relation-preserving representation.",
                "representation_sensitivity": "Changing what is preserved would change the conclusion.",
                "uncertainty_discipline": "The abstract relation is explicitly retained as a limit.",
                "ecosystem_contribution": "refinement_or_relation",
                "notes": "No material audit defect.",
                "reviewer_provenance": {
                    "kind": "fresh-independent-audit",
                    "model_family": "synthetic-test",
                    "exact_service_checkpoint": "synthetic-test-v1",
                    "agent_task_path": "/synthetic/audit-test",
                    "review_scope": "synthetic exact unit and candidate only",
                },
            }
        ],
    )
    pipeline.combine_independent_audit(layout)


def _write_synthetic_execution_ledger(layout: pipeline.SupplementLayout) -> None:
    rows = []
    assignment_paths = [
        path
        for stage in ("generation", "critic", "revision")
        for path in sorted(layout.analysis_assignments(stage).glob("*.json"))
    ] + sorted(layout.audit_assignments.glob("*.json"))
    for index, assignment_path in enumerate(assignment_paths):
        assignment = pipeline.load_json(assignment_path)
        output_path = Path(assignment["output_path"])
        row = execution_provenance.base_execution_row()
        row.update(
            {
                "schema_version": 1,
                "ledger_kind": "synthetic-test-execution",
                "ledger_id": f"synthetic_{index:04d}",
                "release_id": pipeline.RELEASE_ID,
                "stage": assignment.get("stage"),
                "status": "authoritative",
                "requires_rerun": False,
                "rerun_reason": None,
                "assignment_relpath": pipeline._ledger_relpath(layout, assignment_path),
                "assignment_sha256": pipeline.sha256_file(assignment_path),
                "prompt_recovery_status": "encrypted-local-only",
                "agent_task_path": f"/root/synthetic-{assignment.get('stage')}-{index}",
                "output_relpath": pipeline._ledger_relpath(layout, output_path),
                "output_sha256": pipeline.sha256_file(output_path),
                "output_records": len(pipeline.load_jsonl(output_path)),
                "recovery_quality": "synthetic-exact",
            }
        )
        rows.append(row)
    execution_provenance.validate_execution_rows(rows)
    pipeline.write_jsonl(layout.root / "execution" / "ai_execution_ledger.jsonl", rows)


def _build_ready_supplement(
    root: Path, critic_decision: str = "accept_as_is"
) -> tuple[pipeline.SupplementLayout, Path]:
    layout, artifact_root = _setup_intake(root)
    pipeline.prepare_source_screening(layout, artifact_root)
    _write_screening(layout)
    pipeline.prepare_depth_plans(layout, artifact_root)
    _write_depth_plan(layout)
    if pipeline.validate_depth_plans(layout, True):
        raise AssertionError(pipeline.validate_depth_plans(layout, True))
    pipeline.materialize_units(layout, artifact_root)
    _write_analysis_and_audit(layout, artifact_root, critic_decision)
    pipeline.build_objects(layout, artifact_root)
    pipeline.write_trainable_manifest(layout, artifact_root)
    pipeline.write_processing_metrics(layout)
    _write_synthetic_execution_ledger(layout)
    return layout, artifact_root


class AgnosticOpenAlexSupplementTests(unittest.TestCase):
    def test_parent_requires_exact_concrete_44_46_binding(self) -> None:
        self.assertEqual(pipeline._parent_errors(pipeline.SupplementLayout()), [])
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout = pipeline.SupplementLayout(Path(temporary_directory))
            parent = pipeline.load_json(pipeline.HERE / "parent.json")
            parent.pop("concrete_artifact_binding")
            pipeline.write_json(layout.parent, parent)
            self.assertIn(
                "agnostic supplement parent identity mismatch",
                pipeline._parent_errors(layout),
            )

    def test_committed_generation_ledger_exposes_two_reused_task_paths(self) -> None:
        reused = pipeline.discover_reused_generation_contexts()
        self.assertEqual(len(reused), 2)
        self.assertEqual(
            sorted(row["assignment_count"] for row in reused), [12, 15]
        )
        self.assertEqual(
            sorted(row["source_count"] for row in reused), [12, 12]
        )

    def test_source_isolation_archive_is_hash_verified_and_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout = pipeline.SupplementLayout(Path(temporary_directory) / "supplement")
            ledger_rows = []
            for index, source_id in enumerate(("source_a", "source_b")):
                assignment_path = (
                    layout.analysis_assignments("generation") / f"source_{index}.json"
                )
                output_path = layout.analysis_batches("generation") / f"source_{index}.jsonl"
                assignment = pipeline._bind_model_visible_packet(
                    {
                        "stage": "generation",
                        "source_id": source_id,
                        "units": [{"unit_id": f"unit_{index}", "source_id": source_id}],
                        "output_path": str(output_path),
                    }
                )
                pipeline.write_json(assignment_path, assignment)
                pipeline.write_jsonl(output_path, [{"unit_id": f"unit_{index}"}])
                row = execution_provenance.base_execution_row()
                row.update(
                    {
                        "schema_version": 1,
                        "ledger_kind": "synthetic-test-execution",
                        "ledger_id": f"synthetic_reuse_{index}",
                        "release_id": pipeline.RELEASE_ID,
                        "stage": "generation",
                        "status": "isolation-invalid",
                        "requires_rerun": True,
                        "rerun_reason": "reused-multi-source-context",
                        "assignment_relpath": pipeline._ledger_relpath(layout, assignment_path),
                        "assignment_sha256": pipeline.sha256_file(assignment_path),
                        "prompt_recovery_status": "encrypted-local-only",
                        "agent_task_path": "/root/reused-synthetic-generation",
                        "output_relpath": pipeline._ledger_relpath(layout, output_path),
                        "output_sha256": pipeline.sha256_file(output_path),
                        "output_records": 1,
                        "recovery_quality": "synthetic-exact",
                    }
                )
                ledger_rows.append(row)
            ledger_path = layout.root / "execution" / "ai_execution_ledger.jsonl"
            pipeline.write_jsonl(ledger_path, ledger_rows)
            pipeline.write_json(layout.freeze, {"candidate": "old"})
            (layout.root / "depth").mkdir(parents=True, exist_ok=True)
            pipeline.write_jsonl(layout.units, [{"unit_id": "retained"}])

            first = pipeline.prepare_source_isolation_rerun(layout)
            interrupted = dict(first)
            interrupted["status"] = "in_progress"
            pipeline.write_json(layout.isolation_summary, interrupted)
            resumed = pipeline.prepare_source_isolation_rerun(layout)
            second = pipeline.prepare_source_isolation_rerun(layout)
            self.assertEqual(resumed, second)
            self.assertEqual(first, second)
            self.assertEqual(first["status"], "complete")
            self.assertFalse(layout.freeze.exists())
            self.assertTrue(layout.units.is_file())
            self.assertEqual(
                issue42.validate_source_isolation_archive(
                    layout.root, layout.isolation_archive
                ),
                [],
            )
            manifest = pipeline.load_jsonl(layout.isolation_manifest)
            self.assertTrue(manifest)
            self.assertTrue(
                all(row["authoritative"] is False and row["trainable"] is False for row in manifest)
            )
            archived_path = layout.isolation_archive / manifest[0]["archive_relpath"]
            archived_path.write_bytes(archived_path.read_bytes() + b"drift")
            self.assertTrue(
                issue42.validate_source_isolation_archive(
                    layout.root, layout.isolation_archive
                )
            )

    def test_audit_carry_requires_exact_canonical_sample_packet(self) -> None:
        review = {"unit_id": "u", "decision": "accept"}
        prior = [{"unit_id": "u", "candidate": "old"}]
        self.assertEqual(pipeline.exact_audit_carry(prior, prior, [review]), [review])
        self.assertEqual(
            pipeline.exact_audit_carry(
                [{"unit_id": "u", "candidate": "changed"}], prior, [review]
            ),
            [],
        )

    def test_prepare_analysis_rejects_a_stale_same_named_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout, artifact_root = _setup_intake(Path(temporary_directory))
            pipeline.prepare_source_screening(layout, artifact_root)
            _write_screening(layout)
            pipeline.prepare_depth_plans(layout, artifact_root)
            _write_depth_plan(layout)
            pipeline.materialize_units(layout, artifact_root)
            pipeline.prepare_analysis_stage("generation", layout, artifact_root)
            assignment = pipeline.load_json(
                next(layout.analysis_assignments("generation").glob("*.json"))
            )
            pipeline.write_jsonl(Path(assignment["output_path"]), [{"stale": True}])
            with self.assertRaisesRegex(ValueError, "outputs already exist"):
                pipeline.prepare_analysis_stage("generation", layout, artifact_root)

    def test_route_corrected_license_and_handoff_reach_affected_source_objects(self) -> None:
        layout = pipeline.SupplementLayout()
        objects_path = layout.objects
        if not objects_path.is_file():
            objects_path = (
                layout.isolation_archive
                / "non_authoritative"
                / "artifacts"
                / "objects.jsonl"
            )
        records = [
            row
            for row in pipeline.load_jsonl(objects_path)
            if row.get("object_role") == "source"
            and row.get("source_ids") == ["openalex_w3098455240"]
        ]
        self.assertEqual(len(records), 7)
        self.assertTrue(
            all("reported license=None" in row["licensing_boundary"] for row in records)
        )
        self.assertEqual(
            {row["corpus_local_audit"]["handoff_id"] for row in records},
            {"agnostic_mathia_fulltext_v2"},
        )

    def test_analysis_provenance_must_be_structured_and_complete(self) -> None:
        self.assertFalse(pipeline._valid_analysis_provenance("opaque provenance text"))
        self.assertFalse(
            pipeline._valid_analysis_provenance(
                {"kind": "source-grounded-generation", "model_family": "GPT-5"}
            )
        )
        self.assertTrue(
            pipeline._valid_analysis_provenance(
                {
                    "kind": "source-grounded-generation",
                    "model_family": "GPT-5",
                    "exact_service_checkpoint": "unavailable",
                    "agent_task_path": "/root/synthetic-generation",
                    "review_scope": "Exact bound source unit only.",
                }
            )
        )

    def test_independent_audit_sampling_is_stratified_and_not_exhaustive(self) -> None:
        units = [
            {
                "unit_id": f"source_u{index:02d}",
                "source_id": "one_source",
                "unit_type": "one_type",
            }
            for index in range(40)
        ]
        analyses = [
            {
                "unit_id": unit["unit_id"],
                "decision": "quarantined" if index == 39 else "accepted",
            }
            for index, unit in enumerate(units)
        ]
        selected = pipeline._independent_audit_sample_ids(units, analyses)
        self.assertIn("source_u39", selected)
        self.assertGreaterEqual(len(selected), 2)
        self.assertLess(len(selected), len(units))
        self.assertEqual(
            selected, pipeline._independent_audit_sample_ids(units, analyses)
        )

    def test_end_to_end_synthetic_release_is_separate_and_frozen(self) -> None:
        parent_freeze = pipeline.PARENT_RELEASE_ROOT / "freeze.json"
        before = pipeline.sha256_file(parent_freeze)
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout, artifact_root = _build_ready_supplement(Path(temporary_directory))
            self.assertEqual(pipeline.validate_release_ready(layout, artifact_root), [])
            records = pipeline.load_jsonl(layout.objects)
            self.assertEqual(len(records), 2)
            self.assertTrue(
                all(
                    row["corpus_release_id"] == pipeline.RELEASE_ID
                    and row["corpus_origin"] == "agnostic"
                    and all("riemann" not in value for value in row["source_ids"])
                    for row in records
                )
            )
            source = next(row for row in records if row["object_role"] == "source")
            self.assertTrue(source["content_ref"].startswith(f"artifact://{pipeline.RELEASE_ID}/"))
            metrics = pipeline.load_json(layout.metrics)["processing_metrics"]
            self.assertEqual(metrics["sources_received"], 1)
            self.assertEqual(metrics["sources_useful"], 1)
            self.assertEqual(metrics["semantic_units"], 1)
            self.assertEqual(metrics["derivatives_accepted"], 1)
            self.assertEqual(metrics["reinforced_44_lenses"], ["representation_change"])
            self.assertFalse(
                metrics["agent_efficiency"]["exact_token_telemetry_available"]
            )
            proxies = metrics["agent_efficiency"]["observable_byte_proxies_by_stage"]
            self.assertEqual(proxies["screening"]["completed_agent_contexts"], 1)
            self.assertEqual(proxies["depth"]["analyzed_items"], 1)
            self.assertEqual(proxies["generation"]["analyzed_items"], 1)
            self.assertGreater(proxies["generation"]["observable_input_bytes_proxy"], 0)
            freeze_id = pipeline.freeze_release(layout, artifact_root)
            self.assertTrue(freeze_id.startswith("agnostic_openalex_supplement_"))
            self.assertEqual(pipeline.validate_freeze(layout, artifact_root), [])
        self.assertEqual(pipeline.sha256_file(parent_freeze), before)

    def test_depth_validation_rejects_a_gap(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout, artifact_root = _setup_intake(Path(temporary_directory))
            pipeline.prepare_source_screening(layout, artifact_root)
            _write_screening(layout)
            pipeline.prepare_depth_plans(layout, artifact_root)
            _write_depth_plan(layout)
            assignment = pipeline.load_json(next(layout.depth_assignments.glob("*.json")))
            plan = pipeline.load_jsonl(Path(assignment["output_path"]))[0]
            plan["coverage_segments"][1]["line_start"] = 4
            pipeline.write_jsonl(Path(assignment["output_path"]), [plan])
            errors = pipeline.validate_depth_plans(layout, True)
            self.assertIn("openalex_w700: coverage is not exact/gap-free", errors)

    def test_revision_is_exactly_required_for_revise(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout, artifact_root = _build_ready_supplement(
                Path(temporary_directory), critic_decision="revise"
            )
            final = pipeline.load_jsonl(layout.analysis_final)
            self.assertEqual(final[0]["decision"], "accepted")
            self.assertEqual(len(final[0]["derivation_ids"]), 3)
            self.assertEqual(pipeline.validate_release_ready(layout, artifact_root), [])

    def test_intake_rejects_a_riemann_namespace(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout, artifact_root = _setup_intake(Path(temporary_directory))
            row = pipeline.load_jsonl(layout.intake)[0]
            row["canonical_source_id"] = "riemann_forbidden_source"
            pipeline.write_jsonl(layout.intake, [row])
            errors = pipeline.validate_intake(layout, artifact_root)
            self.assertTrue(any("cross-stream" in error for error in errors))

    def test_completed_supplement_updates_only_agnostic_handoff_state(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            layout, artifact_root = _build_ready_supplement(root)
            pipeline.freeze_release(layout, artifact_root)
            state = issue42.load_json(issue42.OPENALEX_HANDOFF_STATE_PATH)
            state["streams"]["agnostic_mathia"]["consumed"] = [
                {
                    "handoff_id": pipeline.HANDOFF_ID,
                    "processing_status": "copied_pending_analysis",
                }
            ]
            state_path = root / "handoff-state.json"
            pipeline.write_json(state_path, state)
            riemann_before = state["streams"]["riemann"]
            pipeline.update_handoff_state(state_path, layout, artifact_root)
            updated = pipeline.load_json(state_path)
            consumed = updated["streams"]["agnostic_mathia"]["consumed"][0]
            self.assertEqual(consumed["processing_status"], "complete")
            self.assertEqual(consumed["supplement_release_id"], pipeline.RELEASE_ID)
            self.assertEqual(updated["streams"]["riemann"], riemann_before)
            self.assertEqual(
                updated["streams"]["agnostic_mathia"]["processing_metrics"],
                pipeline.derived_processing_metrics(layout),
            )

    def test_all_rejected_sources_can_close_without_forcing_trainable_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            layout, artifact_root = _setup_intake(Path(temporary_directory))
            pipeline.prepare_source_screening(layout, artifact_root)
            _write_screening(layout)
            screening = pipeline.load_jsonl(layout.screening_final)
            screening[0]["decision"] = "reject"
            screening[0]["usefulness_reason"] = (
                "The exact source review found no suitable generic semantic unit."
            )
            pipeline.write_jsonl(layout.screening_final, screening)
            pipeline.prepare_depth_plans(layout, artifact_root)
            pipeline.materialize_units(layout, artifact_root)
            for stage in ("generation", "critic", "revision"):
                pipeline.prepare_analysis_stage(stage, layout, artifact_root)
            pipeline.finalize_analysis(layout)
            pipeline.prepare_independent_audit(layout, artifact_root)
            pipeline.combine_independent_audit(layout)
            pipeline.build_objects(layout, artifact_root)
            pipeline.write_trainable_manifest(layout, artifact_root)
            pipeline.write_processing_metrics(layout)
            _write_synthetic_execution_ledger(layout)
            self.assertEqual(pipeline.validate_release_ready(layout, artifact_root), [])
            self.assertEqual(pipeline.load_jsonl(layout.objects), [])
            freeze_id = pipeline.freeze_release(layout, artifact_root)
            freeze = pipeline.load_json(layout.freeze)
            self.assertTrue(freeze_id.startswith("agnostic_openalex_supplement_"))
            self.assertEqual(
                freeze["final_decision"], "NO_USEFUL_AGNOSTIC_OPENALEX_SOURCES"
            )

    def test_artifact_root_inside_repository_is_forbidden(self) -> None:
        with self.assertRaisesRegex(ValueError, "outside Git"):
            pipeline._external_artifact_root(pipeline.REPO_ROOT / "forbidden-artifacts")


if __name__ == "__main__":
    unittest.main()
