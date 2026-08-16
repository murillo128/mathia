"""Exact materialization of the accepted PANEL_V2 contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any

from .canonical import stable_id

PANEL_VERSION = "intuition_fertility_panel_v2"

INTUITION_REQUEST = (
    "Propose one compact mathematical strategy for why the result should hold and how a proof "
    "might be organized. Identify the main mechanism or representation and a small number of "
    "useful intermediate mathematical goals if needed. Mention an obstruction or essential "
    "assumption only if it materially guides the route. Do not write the proof."
)

GENERIC_STRATEGY_CONTROL = (
    "Search for a structural viewpoint that makes the conclusion natural. Identify one useful "
    "representation, decomposition, invariant, or intermediate object and a small number of "
    "subgoals suggested by it. Prefer a viewpoint that removes irrelevant detail. Do not write "
    "the proof."
)


class Presentation(str, Enum):
    STANDARD = "standard"
    GENERICITY = "genericity"


@dataclass(frozen=True)
class PublicTarget:
    theorem_id: str
    role: str
    statement: str
    genericity_variant: str


@dataclass(frozen=True)
class TargetControl:
    theorem_id: str
    factual_control: str


@dataclass(frozen=True)
class TargetIdentity:
    theorem_id: str
    role: str
    canonical_target: str
    reported_artifact_target: str
    record_id: str
    source_path: str
    source_revision: str
    phase2_status: str
    audit_mechanism_note: str


_PUBLIC_TARGETS = {
    "A": PublicTarget(
        "A",
        "primary",
        "Let `𝕜` be a nontrivially normed field, and let `E` and `F` be normed spaces over the same field `𝕜`, with `F` complete. Let `U` be a preconnected subset of `E` and let `f : E → F` be analytic in a neighborhood of every point of `U`. Assume there is a point of `U` near which `f` agrees with the constant zero function. Show that `f` agrees with the constant zero function throughout `U`.",
        "Let `K` be a nontrivially normed field and let `X` and `Y` be normed spaces over `K`, with `Y` complete. Let `V` be preconnected and let `g : X → Y` be analytic near every point of `V`. Suppose some point of `V` has a neighborhood on which `g` is the constant zero function. Show that `g` is the constant zero function on all of `V`.",
    ),
    "B": PublicTarget(
        "B",
        "primary",
        "Let `T` be an endomorphism of a torsion-free module over a domain, and let `λ` and `μ` be distinct scalars. For any generalized-eigenspace depths `k` and `l` in the extended natural numbers `ℕ∞` — including the unbounded depth — show that the generalized eigenspace of `T` for `λ` at depth `k` and the generalized eigenspace for `μ` at depth `l` have trivial intersection.",
        "Let `S` be an endomorphism of a torsion-free module over a domain and let `α` and `β` be distinct scalars. Fix any depths `p` and `q` in `ℕ∞`, allowing the unbounded case. Consider the corresponding generalized eigenspaces for `α` and `β`. Show that they have trivial intersection.",
    ),
    "C": PublicTarget(
        "C",
        "primary",
        "Let `v` be a family of vectors indexed by the disjoint sum of two index types. Show that the whole family is linearly independent if and only if the restriction to each side is linearly independent and the submodules spanned by the ranges of the two restrictions are disjoint.",
        "Let `(a_i)` and `(b_j)` be two tagged families of vectors whose index sets are disjoint. Form the combined tagged family. Show that it is linearly independent exactly when each original family is linearly independent and the spans of the two families have trivial intersection.",
    ),
    "D": PublicTarget(
        "D",
        "primary",
        "Let `G` and `F` be graphs, with the vertex type of `F` finite. Assume that every subgraph of `G` having finitely many vertices admits a graph homomorphism into `F`. Show that there exists a graph homomorphism from all of `G` into `F`.",
        "Let `H` be a source graph and `K` a graph with finite vertex type. Suppose every finite-vertex subgraph of `H` admits a homomorphism into `K`. Show that the entire graph `H` admits a homomorphism into `K`.",
    ),
    "E": PublicTarget(
        "E",
        "primary",
        "Let `r` be a reduction relation. Assume that whenever one object makes two direct `r`-steps to two successors, the branches can be joined so that one successor needs at most one further `r`-step and the other needs only finitely many `r`-steps. Show that whenever two objects are each reachable from a common start by finitely many `r`-steps, the two endpoints have a common descendant reachable from each by finitely many `r`-steps. Zero-step reachability is allowed.",
        "Let `→` be a relation. Suppose every pair of one-step paths from the same source can be joined, with one branch requiring no more than one additional step and the other a finite path. If `y` and `z` are reached from `x` by finite paths, allowing empty paths, show that `y` and `z` can each reach a common object by finite paths.",
    ),
    "F": PublicTarget(
        "F",
        "primary",
        "Let a family of measurable spaces be indexed by an arbitrary type, and let `s` be a measurable subset of their product. Show that there is a countable set of coordinates `I` and a subset `t` of the product restricted to `I` such that `s` is exactly the preimage of `t` under the coordinate-restriction map. Thus membership in `s` depends only on the coordinates in `I`.",
        "Let `(Y_j)` be measurable spaces indexed by a type `J`, and let `A` be a measurable subset of their product. Show that there is a countable subset `K` of `J` and a subset `B` of the product over `K` such that `A` is the inverse image of `B` under restriction to `K`. Equivalently, changing coordinates outside `K` cannot change membership in `A`.",
    ),
    "G": PublicTarget(
        "G",
        "calibration",
        "Let a finite group `G` act on a set and let `x` be a point. Show that the cardinality of the orbit of `x` multiplied by the cardinality of the stabilizer of `x` equals the cardinality of `G`.",
        "Let a finite group `H` act on a set and choose a point `y`. Show that the size of the set of positions reachable from `y`, multiplied by the size of the subgroup fixing `y`, is the size of `H`.",
    ),
}

_TARGET_CONTROLS = {
    "A": TargetControl(
        "A",
        "`E` and `F` are normed over the same nontrivially normed field, `F` is complete, `U` is preconnected, `f` is analytic near every point of `U`, and near one point of `U` it agrees with the constant zero function. The target is equality with that function on all of `U`.",
    ),
    "B": TargetControl(
        "B",
        "The same endomorphism `T` determines generalized eigenspaces for two distinct scalars `λ` and `μ`, at arbitrary depths in `ℕ∞`, possibly unbounded. The module is torsion-free over a domain. The target is that the two submodules have only the trivial intersection.",
    ),
    "C": TargetControl(
        "C",
        "The family has one restriction to each side of a disjoint index sum. The target is an equivalence between independence of the combined family and independence of both restrictions together with disjointness of their spans.",
    ),
    "D": TargetControl(
        "D",
        "`F` has finitely many vertices. Every finite-vertex subgraph of `G` has at least one graph homomorphism into `F`. The target is existence of a graph homomorphism from `G` itself into `F`.",
    ),
    "E": TargetControl(
        "E",
        "The premise gives a joinability condition for every direct fork of `r`. The target gives a joinability condition for endpoints of arbitrary finite reduction sequences from the same source, with empty paths allowed.",
    ),
    "F": TargetControl(
        "F",
        "`s` is measurable in a product measurable space. The target is existence of a countable coordinate set and a restricted-product subset whose inverse image under coordinate restriction is exactly `s`.",
    ),
    "G": TargetControl(
        "G",
        "The orbit contains the points reachable from `x` under the action, and the stabilizer contains the group elements that leave `x` fixed. The target relates their finite cardinalities to the cardinality of `G`.",
    ),
}

ADJACENT_DONORS = {"A": "E", "E": "A", "B": "C", "C": "B", "D": "F", "F": "D"}
DISTANT_DONORS = {"A": "C", "B": "D", "C": "E", "D": "B", "E": "C", "F": "B"}


def get_public_target(theorem_id: str) -> PublicTarget:
    try:
        return _PUBLIC_TARGETS[theorem_id]
    except KeyError as error:
        raise ValueError(f"unknown theorem id: {theorem_id}") from error


def get_control(theorem_id: str) -> TargetControl:
    try:
        return _TARGET_CONTROLS[theorem_id]
    except KeyError as error:
        raise ValueError(f"unknown theorem id: {theorem_id}") from error


def get_target_identity(theorem_id: str) -> TargetIdentity:
    # Kept behind a separate accessor so generator code never needs the private module.
    from ._private_panel import PRIVATE_TARGETS

    public = get_public_target(theorem_id)
    return TargetIdentity(
        theorem_id=theorem_id, role=public.role, **PRIVATE_TARGETS[theorem_id]
    )


def generator_payload(
    theorem_id: str, presentation: Presentation | str
) -> dict[str, str]:
    """Return the only normal payload accepted by an intuition generator."""

    public = get_public_target(theorem_id)
    try:
        selected = Presentation(presentation)
    except ValueError as error:
        raise ValueError(f"unknown presentation: {presentation}") from error
    statement = (
        public.statement
        if selected is Presentation.STANDARD
        else public.genericity_variant
    )
    return {"theorem_statement": statement, "intuition_request": INTUITION_REQUEST}


def panel_snapshot(*, include_private: bool = False) -> dict[str, Any]:
    """Return deterministic transport data, with private material opt-in only."""

    targets: list[dict[str, Any]] = []
    for theorem_id in sorted(_PUBLIC_TARGETS):
        row: dict[str, Any] = {
            "public": asdict(_PUBLIC_TARGETS[theorem_id]),
            "formal_control": asdict(_TARGET_CONTROLS[theorem_id]),
        }
        if include_private:
            row["private"] = asdict(get_target_identity(theorem_id))
        targets.append(row)
    return {
        "schema_version": PANEL_VERSION,
        "intuition_request": INTUITION_REQUEST,
        "generic_strategy_control": GENERIC_STRATEGY_CONTROL,
        "adjacent_donors": ADJACENT_DONORS,
        "distant_donors": DISTANT_DONORS,
        "targets": targets,
    }


PANEL_ID = stable_id("panel", panel_snapshot(include_private=True))
