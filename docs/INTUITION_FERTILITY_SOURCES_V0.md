# Intuition-fertility theorem documentation sources v0

## Purpose

The first intuition pre-test uses familiar theorems because the immediate question is whether a model can produce a compact strategy that changes a formal worker's verified proof yield, not whether the theorem itself is novel.

For #30, each theorem should therefore have human-readable mathematical documentation in addition to the private Lean proof. These sources are for **scoping, audit, and later interpretation**. They are not supplied to Qwen/Codex/Mathia during primary intuition generation, and their text is not automatically authorized as training data.

Before any source material is copied into a future training corpus, its exact license and permitted use must be checked separately. Linking or consulting a source for internal research does not establish redistribution/training rights.

## Subgroup cardinality / Lagrange

- UCL course notes, *Cosets and Lagrange's Theorem*: https://www.homepages.ucl.ac.uk/~ucahmto/0007/_book/4-6-cosets-and-lagranges-theorem.html
- Stanford notes, *Group Theory — Lagrange's Theorem*: https://crypto.stanford.edu/pbc/notes/group/lagrange.html
- Private formal target: `Subgroup.card_subgroup_dvd_card` in qwen-lean's pinned mathlib.

These references document the coset-partition viewpoint rather than only the divisibility conclusion.

## Rank-nullity

- UCL course notes, *The rank-nullity theorem*: https://www.homepages.ucl.ac.uk/~ucahmto/0005_2023/Ch4.S15.html
- Private formal target: `LinearMap.rank_range_add_rank_ker` in qwen-lean's pinned mathlib.

The Mathia audit reference additionally uses the quotient-by-kernel / surviving-information viewpoint already explicit in the mathlib theorem neighborhood. External source text is not shown to the intuition generator.

## Orbit-stabilizer

- University of Michigan notes, *The Orbit Stabilizer Theorem*: https://sites.lsa.umich.edu/kesmith/wp-content/uploads/sites/1309/2024/07/GroupActionsStabilizersANSWERS.pdf
- Harvard Algebra I course page/remarks on group actions and orbit-stabilizer: https://abel.math.harvard.edu/~elkies/M122.23/index.html
- Private formal target: `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` in qwen-lean's pinned mathlib.

The relevant conceptual relation is the quotient/coset representation of orbit positions by stabilizer redundancy.

## Schröder-Bernstein

- Whitman College online text, *The Schröder-Bernstein Theorem*: https://www.whitman.edu/mathematics/higher_math_online/section04.09.html
- Cornell CS notes, *A careful proof of the Cantor-Schroder-Bernstein Theorem*: https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec14-cantor.html
- Private formal target: `Function.Embedding.schroeder_bernstein_of_rel` in qwen-lean's pinned mathlib.

The private target is a relation-preserving strengthening used by mathlib, so the audit must distinguish the standard theorem's chain/partition intuition from the extra pointwise relation obligation.

## Hall's marriage theorem

- MIT OpenCourseWare, 18.315 Combinatorial Theory lecture notes containing Hall's Marriage Theorem: https://ocw.mit.edu/courses/18-315-combinatorial-theory-introduction-to-graph-theory-extremal-and-enumerative-combinatorics-spring-2005/resources/lec24/
- Yale CS notes, matching and Hall's theorem: https://www.cs.yale.edu/homes/aspnes/pinewiki/CS202%282f%292008%282f%29Notes%282f%29Combined.html
- Private formal target: `HallMarriageTheorem.hall_hard_inductive` in qwen-lean's pinned mathlib.

The mathlib proof uses the tight-subfamily versus strict-slack dichotomy. Human sources may use different proof routes; that diversity is useful for audit and is a reason not to define one historical proof as the only valid intuition.

## Continuous image of a compact set

- Harvard topology course notes: https://people.math.harvard.edu/~ctm/home/text/class/harvard/131/13/html/home/course/course.pdf
- Manchester topology notes, compactness chapter: https://personalpages.manchester.ac.uk/staff/yuri.bazlov/topology/notes/ch7.pdf
- Private formal target: `IsCompact.image_of_continuousOn` in qwen-lean's pinned mathlib.

The standard open-cover argument and mathlib's filter/cluster-point implementation give different formal surfaces for the same transport-under-continuity mechanism. This makes the item useful for checking whether an intuition has to mimic the library proof in order to be fertile.

## Source-use rule for #32

The primary intuition generators see **none** of the sources above. They receive only the frozen name-free theorem presentation.

After intuitions and qwen-lean outcomes are frozen, these sources may be used for interpretation questions such as:

- did the generated strategy recover a documented mechanism?;
- did it find a different strategy that nevertheless improved verified proof yield?;
- did Codex merely reproduce a canonical exposition?;
- did qwen-lean benefit from a strategy that is mathematically sound but formally different from mathlib's original proof?

Similarity to these references remains auxiliary evidence. Verified downstream effect is the intended hard signal.
