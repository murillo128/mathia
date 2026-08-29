# MI-003 — Absolute Selberg theory fails, and relative theory must beat asymptotically affine composite clones

**Evidence level:** proved for the stated obstructions; supported for the surviving relative-program constraint

## Core intuition

The prime flute is structurally outside the standard absolute Selberg/Ruelle/Fredholm regime, but this no longer leaves “some relative theory” as a sufficiently discriminating target. The strongest exact controls now preserve the projective gap process and approximate the **entire sampled exact tail** by an all-composite flute with summable endpoint displacement. Any future relative invariant must therefore survive both the universal noncompact background and this much tighter arithmetic control.

## Strongest justified impossibility principle

For the ordinary `L^2` Laplacian, the absolute obstruction remains decisive: primitive lengths accumulate at zero and on positive compact intervals, recurrent finite tangents implant sub-quarter essential spectrum, and the pencil

\[
\Delta-s(1-s)
\]

is non-Fredholm at infinitely many points tending to `s=1`. Standard absolute Selberg/Ruelle products and near-one meromorphic-Fredholm theory are therefore the wrong category for this surface.

The relative branch is constrained at several additional levels.

- PF-088 and PF-102 show that the selected `Re s=1/4` boundaries can be produced by one-dimensional propagation and even by a single compact endpoint defect.
- PF-103 shows that completing the selected primitive-orbit sector to include arbitrary cusp windings restores the universal parabolic threshold `Re s=1/2`.
- PF-104 shows that differential or analytic information of the continuous interpolation `x -> cot(pi/x)` away from the sampled endpoints is not intrinsic surface data.
- PF-105 gives an all-composite dilation clone with uniformly vanishing full-tail cross-ratio/separator distortion.
- PF-106 strengthens this to the affine clone `q_n=p_n+1`: after the canonical Möbius translation, its sampled endpoint displacement from the exact prime flute is `ell^1`, every all-span tail cross-ratio distortion is `O(P^-3)`, and the natural piecewise-affine boundary matching has `L^1` derivative defect with tail mass tending to zero.

Thus a candidate that depends continuously only on projective tangents, finite endpoint jets, off-prime interpolation, or an asymptotically affine/summable marked deformation cannot claim prime specificity.

## The surviving operator question

PF-106 deliberately stops before the decisive analytic bridge. The piecewise-affine boundary matching is not yet a group-equivariant quasiconformal comparison of the quotient surfaces, and no theorem has been proved that the corresponding resolvent, heat, or scattering difference is compact or lies in a Schatten class.

This is now the sharp boundary. If the all-composite affine clone is operator-theoretically perturbative relative to the prime flute, then any surviving global spectral distinction is confined to an even smaller relative spectral-shift/scattering sector and cannot be read from the tail geometry alone. If it is **not** perturbative despite `ell^1` endpoint closeness, the obstruction itself would identify a genuinely nonlocal amplification mechanism worth understanding.

## Evidence against overgeneralization

The composite-clone estimates do not imply isometry, isospectrality, compact resolvent difference, or equality of scattering data. Nor do they erase the finite resolved multi-gap memory of MI-001: that mechanism is a local marked statement before the prime/composite global comparison is imposed.

Likewise, relative constructions remain legitimate when their reference is forced by the geometry and shares the same essential/orbit pathology. What is no longer legitimate is treating a convenient analytic threshold, a cotangent jet, or a weakly matched smooth background as arithmetic evidence.

## Status / novelty

The absolute spectral obstructions and the endpoint-control estimates are rigorous findings. The conclusion that future relative theory must be tested against the affine all-composite clone is a supported synthesis, not a theorem that all such relative objects coincide.

## Falsification criterion

Refute the synthesis by producing an intrinsic prime-flute spectral invariant that is continuous under the PF-106 marked asymptotically affine comparison yet distinguishes the prime and all-composite flutes for a reason not supplied by external labels; or by disproving one of the exact endpoint/cross-ratio estimates used by the control.

## Lean-formalizable core

- Essential-spectrum implies non-Fredholmness of `Delta-lambda`.
- `p`-series thresholds underlying the universal `1/4` and cusp-winding `1/2` examples.
- Summability of the normalized endpoint displacement for `p -> p+1`.
- Uniform propagation of secant-ratio bounds to cross-ratios and separating lengths.
