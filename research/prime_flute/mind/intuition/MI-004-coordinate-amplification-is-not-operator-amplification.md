# MI-004 — Coordinate amplification is not operator amplification, and the first operator ideal is now excluded

**Evidence level:** supported by exact geometric and microlocal comparison results; compact/`S_p`, `p>1`, and scattering conclusions remain open

## Core intuition

For the exact all-composite shift clone `p_n -> p_n+1`, different coordinates and operator topologies see genuinely different defects. Raw additive cuff and seam coordinates can carry nonsummable common-scale modes even while endpoint, collar, pant-local marked-length, and canonical gluing data are summable or uniformly vanishing. The new evidence also closes one tempting operator route: a first resolvent difference for two nonisometric smooth metrics is locally pseudodifferential of order `-2` in dimension two and is therefore not trace class. The surviving question is no longer whether the clone is “small” in one coordinate, but **which operator category is geometrically justified and still sees arithmetic information**.

## Strongest justified principle

PF-107--PF-120 now separate four effects that had been conflated.

- PF-107--PF-111 show that endpoint and several pant-local/geodesic defects are small despite the non-`ell^1` additive cuff coordinate. Collar widths/areas, seam/spine additive defects, explicit collar distortion, all-span separator ratios, and pant-local marked-length distortions are summable or uniformly vanishing in the relevant normalization.
- PF-114 and PF-118 isolate a nonsummable `~1/p_n` **relative seam/common-scale mode**. PF-119 then shows that the canonical cusp-split gluing offset differentiates this mode between neighboring pants and has summable clone defect. PF-120 shows that cusp Busemann rescalings must be synchronized, but the raw sidewise mismatch can be redistributed with arbitrarily small additional one-dimensional Lipschitz cost. Thus the nonsummable coordinate mode is not by itself a proved global metric obstruction.
- PF-113 proves that raw relative generator right limits in a fixed endpoint frame are parabolic gauge data caused by escaping centers; the intrinsic elliptic mismatch is summable. PF-115--PF-116 also close the coarse-hyperbolic escape: prime and clone lie in the same Gromov-hyperbolicity class, and in fact neither surface is Gromov hyperbolic.
- PF-112 gives the first genuine operator-ideal no-go. Under any smooth nonisometric marked identification, the first relative resolvent has the local `Psi^{-2}` singular-value law in dimension two, so it cannot be `S_1`. This obstruction is local and does not diagnose the prime tail.

The remaining operator gate is therefore narrower: compactness or `S_p` for `p>1`, higher resolvent powers, heat/wave comparison, or a relative scattering object after a synchronized global pants/cusp identification.

## What remains possible

A direct common-surface construction may still produce a metric perturbation that tends to the identity strongly enough through the thin end to preserve essential spectrum or give compact/`S_p`, `p>1`, relative objects. Conversely, collapsing collars may amplify the summable pant/gluing defects in exactly one of those weaker operator categories.

Any surviving arithmetic signal must be separated from three backgrounds already identified here: local pseudodifferential non-trace-class behavior, gauge-dependent escaping-center matrices, and coarse non-Gromov geometry.

## Status / novelty

The summability estimates, pant/arc comparisons, gluing/Busemann identities, gauge and coarse controls, and first-resolvent trace-class obstruction are persisted findings. No compactness, `S_p` for `p>1`, wave-operator completeness, or relative-scattering conclusion is promoted here.

## Falsification criterion

Prove a synchronized common-surface comparison and show that an operator-native relative object is compact or belongs to a specific `S_p`, `p>1`, class, or construct a weakly null sequence showing noncompactness despite the summable intrinsic controls. A purported `S_1` theorem for the first relative resolvent under a nonisometric smooth identification would contradict PF-112.

## Lean-formalizable core

- Series classifications for endpoint, cuff, collar, seam, pant-length, and gluing defects.
- Telescoping/differencing identity turning the common seam scale into a summable gluing offset.
- Gauge comparison for relative generators.
- Abstract separation of local `Psi^{-2}` trace-class obstruction from tail compactness questions.
