# WI-401 — Widder fixed-height sampling has exact horizontal resolution

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SHARP-STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.

**Parent finding:** [WI-400](./WI-400-widder-root-profile-exactly-recovers-horizontal-defect-width.md).

## Claim

Conditional on the fixed-height prime/zero root-rate interface imported and audited in WI-399--WI-400, the scalar Widder criterion has an exact sampling resolution. An off-critical zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad d:=|\delta|>0,
\]

is visible at threshold `1` precisely on an open interval of fixed heights of radius `d`, independent of its ordinate. More explicitly, if

\[
w_\rho=(\gamma-id)^2
\]

and

\[
r_\rho(T)
:=
4T^2\frac{|w_\rho|}{|T^2+w_\rho|^2},
\]

then

\[
\boxed{
r_\rho(T)>1
\iff
T\in I_\rho
:=
\left(
\sqrt{\gamma^2+2d^2}-d,
\sqrt{\gamma^2+2d^2}+d
\right).
}
\tag{1}
\]

Thus the interval center and radius are

\[
c_\rho=\sqrt{\gamma^2+2d^2},
\qquad
\operatorname{rad}(I_\rho)=d,
\qquad
|I_\rho|=2d.
\tag{2}
\]

Let

\[
L_{\mathcal P}(T)
:=
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}
\]

be the prime-side root rate from WI-399, and let `S` be any set of admissible fixed heights. If one proves

\[
L_{\mathcal P}(T)\le1
\qquad(T\in S),
\tag{3}
\]

then every off-critical zero must satisfy

\[
\boxed{
d\le \operatorname{dist}(c_\rho,S).
}
\tag{4}
\]

Consequently, if `S` is an `h`-net for the possible centers, so that every such center lies within distance `h` of `S`, then

\[
\boxed{
|\Re\rho-1/2|\le h
\quad\text{for every nontrivial zero }\rho.
}
\tag{5}
\]

A uniform lattice of spacing `q` therefore has scalar horizontal resolution exactly `q/2`: threshold-`1` control at all lattice points forces the strip `|Re rho-1/2|<=q/2`. A dense sample set has zero covering radius and hence yields RH, conditional on the same source interface.

The resolution is sharp at the level of this scalar fixed-height geometry. Any sampling set with a positive open gap can hide a hypothetical sufficiently shallow off-line functional-equation/conjugation-symmetric block whose whole visibility interval lies in that gap. Hence a fixed positive mesh cannot exclude arbitrarily shallow off-critical defects by the scalar threshold `L_P(T)<=1` alone.

No existence of such zeta zeros is asserted, and no proof of RH or improved simple-critical-zero proportion is claimed.

## 1. Source interface and exact zero-side geometry

The primary source remains Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026:

https://www.preprints.org/manuscript/202609.1018/v2

It is a recent non-peer-reviewed preprint and is not treated as established peer-reviewed evidence. Proposition A1 and Lemma A1 give the fixed-height zero-side root radius and its prime-side transport; WI-400 packages them as

\[
\boxed{
\max\{1,L_{\mathcal P}(T)\}
=
\max\{1,\mathcal R(T)\}
}
\qquad(T\ge2),
\tag{6}
\]

where

\[
\mathcal R(T)
=
\max_\rho r_\rho(T).
\tag{7}
\]

Therefore, at the endpoint threshold,

\[
L_{\mathcal P}(T)\le1
\iff
\mathcal R(T)\le1.
\tag{8}
\]

The source also records the exact factorization underlying its fixed-height RH criterion. For a zero of depth `d=|delta|`, direct expansion gives

\[
|T^2+w_\rho|^2-4T^2|w_\rho|
=
(-T^2-2Td+d^2+\gamma^2)
(-T^2+2Td+d^2+\gamma^2).
\tag{9}
\]

The two positive roots in `T` are

\[
T_- = \sqrt{\gamma^2+2d^2}-d,
\qquad
T_+ = \sqrt{\gamma^2+2d^2}+d.
\tag{10}
\]

For `T` between these roots the product in (9) is negative, and outside their closed span it is positive. Since the denominator defining `r_rho(T)` is positive,

\[
r_\rho(T)>1
\iff
T_-<T<T_+,
\]

which proves (1)--(2).

This interval statement is stronger and more geometric than merely knowing that an off-line zero produces `R(T)>1` somewhere. Its width is exactly `2d`, regardless of how high the zero lies.

The maximum height of the one-zero factor is not the center of the visibility interval. Differentiating the rational function in `x=T^2` shows that its maximum occurs at

\[
T_{\rm peak}=\sqrt{\gamma^2+d^2},
\tag{11}
\]

where

\[
\boxed{
r_\rho(T_{\rm peak})
=1+\frac{d^2}{\gamma^2}.
}
\tag{12}
\]

Thus two complementary scales coexist. The width of the threshold-`1` visibility interval is height-independent, while the peak excess above `1` decays like `d^2/gamma^2` for a high zero. This distinction matters for arithmetic certification: locating the violation does not become harder geometrically with height, but resolving its amplitude numerically can.

## 2. Sampling theorem

Let `S` be a subset of the admissible fixed heights and assume the prime-side endpoint estimate (3) at every point of `S`. By (8),

\[
\mathcal R(T)\le1
\qquad(T\in S).
\tag{13}
\]

If an off-critical zero had `d>dist(c_rho,S)`, some sample point would satisfy

\[
|T-c_\rho|<d.
\]

By (1), that point lies in `I_rho`, hence

\[
\mathcal R(T)\ge r_\rho(T)>1,
\]

contradicting (13). This proves (4).

Now suppose every possible center is within distance `h` of `S`. Equation (4) immediately gives (5). In particular, for a uniform grid of spacing `q`, the covering radius is `q/2`, so

\[
|\Re\rho-1/2|\le q/2.
\tag{14}
\]

For `q>=1` this is no better than the ordinary critical-strip bound `d<1/2`; a mesh strictly finer than `1` is required for a nontrivial strip improvement. If the sample set is dense, every nonempty open interval `I_rho` contains a sample point, so no `d>0` can occur. This recovers the qualitative rational-height criterion in the source from the exact visibility geometry.

The theorem is deliberately stated in terms of covering radius rather than a particular lattice. Nonuniform meshes can allocate finer resolution only where arithmetic control is available; the horizontal conclusion at a zero is then exactly the distance from its center to the nearest certified height.

## 3. Sharpness and falsification

The `h`-net conclusion cannot be strengthened using only the scalar sampled threshold information.

Suppose `S` misses an open interval `(a,b)` of length `ell=b-a>0`. Set

\[
c=\frac{a+b}{2}
\]

and choose any

\[
0<d<\frac{\ell}{2}
\]

small enough that `c^2>2d^2`. Define

\[
\gamma=\sqrt{c^2-2d^2}.
\tag{15}
\]

Then a hypothetical off-line zero of depth `d` and ordinate `gamma` has

\[
c_\rho=\sqrt{\gamma^2+2d^2}=c
\]

and therefore

\[
I_\rho=(c-d,c+d)\subset(a,b).
\tag{16}
\]

Its one-zero factor satisfies `r_rho(T)<=1` at every sample point in `S`. Completing it to the usual functional-equation/conjugation-symmetric quadruple does not alter this scalar visibility conclusion; critical-line zeros themselves have one-zero factors at most `1`.

This is a falsification model, not a claim that the Riemann zeta function possesses such a zero configuration. It shows that the scalar sampled root-profile geometry alone cannot rule it out. Any theorem excluding shallow defects while leaving positive sampling gaps must use information beyond the pointwise threshold `R(T)<=1` at those samples.

For a uniform grid of spacing `q`, the bound `d<=q/2` is sharp in the same geometric sense. Put a center at a grid-cell midpoint and take `d=q/2`. The open visibility interval has the two neighboring grid points as endpoints, where (9) gives exactly

\[
r_\rho(T)=1.
\]

Hence the sampled endpoint inequalities do not distinguish this boundary model from an on-line configuration.

## 4. Relation to WI-400

WI-400 classifies the information in the **complete** fixed-height root profile. It proves that, after clipping at `1`, the full family `C(T)=max{1,L_P(T)}` exactly recovers the worst horizontal defect and that the width-only feedback map is the identity. The present result asks a different question: how much horizontal information survives when only a subset of heights is certified at the exact endpoint threshold.

The answer is a metric sampling law. Each zero produces an interval whose radius is exactly its horizontal displacement, and the certified sample set can exclude that zero if and only if it intersects that interval. Thus full-profile control and sampled-profile control fit together as

\[
\text{horizontal defect depth}
\longleftrightarrow
\text{visibility radius in }T
\longleftrightarrow
\text{sampling resolution}.
\tag{17}
\]

This is not a contraction mechanism. It is instead a sharp statement of what arithmetic fixed-height information would be sufficient. To force defect `<=a`, threshold-`1` estimates on a sample set of covering radius `a` suffice. To force zero defect by this scalar route, the mesh gaps themselves must tend to zero, or an independent invariant must bridge the unsampled intervals.

## 5. Prior-art audit

The Rafik preprint explicitly supplies the load-bearing zero-radius formula, the prime/zero fixed-height root-rate relation, and an RH criterion that can be checked on every rational `T>14`. It also shows qualitatively that an off-line zero creates a nonempty open interval of heights with root radius above `1`. Those statements are literature input here, conditional on the correctness of the unreviewed source.

The new exact deductions in this finding are the factorized interval interpretation (1)--(2), the covering-radius theorem (4)--(5), the exact lattice resolution `q/2`, and the positive-gap sharpness model. A targeted search around Widder root growth, fixed-height sampling, rational-height RH criteria, and horizontal zero displacement found the Rafik source and classical neighboring Widder/Stieltjes material, but no separate source stating this quantitative sampling law. This is only a novelty audit and is not a priority claim.

The dense-rational qualitative endpoint is not claimed as new: the source already states that rational heights above its fixed lower cutoff suffice for its RH criterion. The substantive addition is the quantitative finite-mesh geometry and its exact obstruction.

## 6. Research implication

This finding narrows the live Widder arithmetic problem. WI-400 showed that a previously known strip width cannot bootstrap itself through the same scalar root envelope. WI-401 now shows that one does not necessarily need the full continuous profile to improve a strip: it would be enough to prove the exact endpoint bound

\[
L_{\mathcal P}(T)\le1
\]

on a sufficiently fine set of fixed heights. A mesh of spacing `2a` would already force the horizontal defect to at most `a`, conditional on the source interface.

At the same time, the sharpness construction closes the tempting sparse-sampling shortcut. A fixed mesh with a positive maximum gap has a matching unresolved defect scale. Reaching RH through this scalar threshold mechanism requires sampling gaps tending to zero, or genuinely new arithmetic/zero-side information capable of coupling neighboring heights. Candidate enrichments remain height-dependent depth constraints, signed prime cancellation with quantitative continuity in `T`, phase information, or population/correlation information not represented by `R(T)` alone.

This also separates geometric resolution from amplitude. High zeros do not shrink the interval that must be hit, but by (12) their violation above `1` becomes shallow. Any rigorous computational or analytic implementation therefore has two independent burdens: a sufficiently fine height mesh and enough arithmetic precision or margin to certify the endpoint inequality.

## 7. Evidence status and failure modes

Equations (1)--(5), (10)--(16) are exact elementary deductions from the one-zero rational factor and the clipped prime/zero identity already isolated in WI-400. No numerical experiment is used.

The dependency on Rafik's September 2026 preprint is nevertheless load-bearing. Until its Proposition A1/Lemma A1 fixed-height interface is independently rederived or otherwise validated, statements transferring `L_P(T)<=1` to the zeta-zero spectral radius should be read as conditional on that source. The geometric calculation on the zero side is independent once the rational factor is granted.

The positive-gap construction is only a sharpness model for the scalar interface. It does not construct a zeta function with the hypothetical zero block, does not show compatibility with the full explicit formula or prime arithmetic, and does not rule out stronger theorems that couple several heights at once. Its conclusion is narrower and exact: **sampled scalar threshold data with positive covering radius cannot, by itself, resolve horizontal defects below that radius.**
