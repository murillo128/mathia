# WI-402 — Widder sampled root bounds have an exact mesh--margin resolution law

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SHARP-STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.

**Parent finding:** [WI-401](./WI-401-widder-sampling-mesh-has-exact-horizontal-resolution.md).

## Claim

Conditional on the fixed-height prime/zero root-rate interface imported and audited in WI-399--WI-401, the endpoint sampling law of WI-401 extends exactly to any uniform root-rate margin above one. The resulting geometry separates the two burdens that WI-401 identified qualitatively: height sampling and arithmetic amplitude control.

Let

\[
\rho=\frac12+\delta+i\gamma,
\qquad d:=|\delta|>0,
\]

and retain the one-zero Widder factor

\[
r_\rho(T)
:=4T^2\frac{|w_\rho|}{|T^2+w_\rho|^2},
\qquad
w_\rho=(\gamma-id)^2.
\]

Fix `epsilon>=0` and put

\[
K:=1+\varepsilon.
\]

Then the superlevel set `r_rho(T)>K` is empty precisely when

\[
\boxed{d^2\le \varepsilon\gamma^2.}
\tag{1}
\]

When `d^2>epsilon gamma^2`, it is exactly the open interval

\[
\boxed{
I_{\rho,\varepsilon}
=
\left(C_{\rho,\varepsilon}-H_{\rho,\varepsilon},
      C_{\rho,\varepsilon}+H_{\rho,\varepsilon}\right)
}
\tag{2}
\]

with

\[
\boxed{
C_{\rho,\varepsilon}
=
\frac{\sqrt{\gamma^2+(2+\varepsilon)d^2}}{\sqrt{1+\varepsilon}},
\qquad
H_{\rho,\varepsilon}
=
\frac{\sqrt{d^2-\varepsilon\gamma^2}}{\sqrt{1+\varepsilon}}.
}
\tag{3}
\]

Thus a positive arithmetic slack above the neutral threshold does not merely shrink WI-401's visibility interval by an unspecified amount. It consumes **horizontal depth squared** at the exact rate `epsilon gamma^2`.

Let

\[
L_{\mathcal P}(T)
:=\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}
\]

be the prime-side root rate from WI-399. Suppose a sample set `S` satisfies

\[
L_{\mathcal P}(T)\le1+\varepsilon
\qquad(T\in S).
\tag{4}
\]

If `S` has covering radius at most `h` for all possible centers `C_{rho,epsilon}` in (3), then every off-critical zero satisfies the exact consequence

\[
\boxed{
d^2\le \varepsilon\gamma^2+(1+\varepsilon)h^2.}
\tag{5}
\]

For a uniform lattice of spacing `q`, `h=q/2`, so

\[
\boxed{
|\Re\rho-1/2|^2
\le
\varepsilon\gamma^2
+(1+\varepsilon)\frac{q^2}{4}.
}
\tag{6}
\]

Equation (5) is sharp at the level of the scalar fixed-height geometry: placing the center (3) at the midpoint of a largest sampling gap and taking `H_{rho,epsilon}=h` puts the neighboring sample points exactly at threshold `K`.

The structural consequence is a no-go for approximate endpoint certification with height-independent slack. Even with continuous sampling (`h=0`), (5) reduces to

\[
\boxed{d\le\sqrt\varepsilon\,\gamma.}
\tag{7}
\]

Hence every fixed `epsilon>0` becomes completely vacuous against the ordinary critical-strip bound `d<1/2` once `gamma` is sufficiently large. To force a fixed horizontal target scale `d<=a` near ordinate `gamma`, the admissible root-rate excess must be of order at most `a^2/gamma^2`, in addition to a mesh whose covering radius is below that same horizontal scale. The `1/gamma^2` amplitude scale is not a numerical artifact: it is already exact in the one-zero factor.

No proof of RH and no improved simple-critical-zero proportion is claimed.

## 1. Source interface

The load-bearing external source is Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026. The source is explicitly non-peer-reviewed. Its Appendix A supplies the fixed-height zero-side spectral radius and the prime-side transport used in WI-399--WI-401.

WI-400 packages that interface as the threshold equivalence

\[
\boxed{
L_{\mathcal P}(T)\le K
\iff
\mathcal R(T)\le K
}
\qquad(K\ge1),
\tag{8}
\]

where

\[
\mathcal R(T)=\max_\rho r_\rho(T).
\]

Therefore any sampled prime bound (4) forces

\[
r_\rho(T)\le1+\varepsilon
\]

for every zero and every sampled height. The new content below is the exact geometry of that non-endpoint superlevel set and the resulting mesh--margin law.

The primary-source page was checked again on 22 September 2026: version 2 remains the latest posted version, dated 17 September 2026, and is still marked as not peer-reviewed.

## 2. Exact non-endpoint visibility interval

Write

\[
x=T^2,
\qquad
s:=\gamma^2+d^2=|w_\rho|,
\qquad
a:=\gamma^2-d^2=\Re w_\rho.
\]

Then

\[
|T^2+w_\rho|^2=x^2+2ax+s^2,
\]

and `r_rho(T)>K` is equivalent to

\[
Q_K(x)
:=K(x^2+2ax+s^2)-4xs<0.
\tag{9}
\]

Set `K=1+epsilon`. The discriminant of this quadratic is

\[
\boxed{
\operatorname{disc}Q_K
=16\bigl(\gamma^2+(2+\varepsilon)d^2\bigr)
      \bigl(d^2-\varepsilon\gamma^2\bigr).
}
\tag{10}
\]

Since the leading coefficient is positive, a strict superlevel interval exists exactly when the second factor is positive, proving (1). This agrees independently with the exact peak value from WI-401,

\[
\max_T r_\rho(T)=1+\frac{d^2}{\gamma^2}:
\]

that peak exceeds `1+epsilon` exactly when `d^2>epsilon gamma^2`.

Assume now `d^2>epsilon gamma^2`. Define

\[
A:=\sqrt{\gamma^2+(2+\varepsilon)d^2},
\qquad
B:=\sqrt{d^2-\varepsilon\gamma^2}.
\]

The two positive roots of (9) are

\[
x_\pm=\frac{(A\pm B)^2}{1+\varepsilon}.
\tag{11}
\]

Indeed their sum and product agree exactly with the Vieta data of (9); equivalently direct substitution reduces to (10). Since

\[
A^2-B^2=(1+\varepsilon)(\gamma^2+d^2)>0,
\]

we have `A>B>0`, so taking positive square roots gives

\[
T_\pm=\frac{A\pm B}{\sqrt{1+\varepsilon}}.
\tag{12}
\]

The quadratic is negative precisely between these roots. Their midpoint and half-width are exactly (3), proving (2)--(3).

At `epsilon=0`, equations (2)--(3) reduce to WI-401:

\[
C_{\rho,0}=\sqrt{\gamma^2+2d^2},
\qquad
H_{\rho,0}=d.
\]

Thus the endpoint sampling theorem is the zero-margin member of a complete one-parameter family, not a separate phenomenon.

## 3. Exact mesh--margin tradeoff

Assume (4) and suppose first that `d^2<=epsilon gamma^2`. Then (5) is immediate.

Otherwise the nonempty interval (2) is precisely where this zero would force

\[
r_\rho(T)>1+\varepsilon.
\]

By (8), no point of `S` may lie in that interval. If every center (3) is within distance `h` of `S`, the interval can avoid `S` only if

\[
H_{\rho,\varepsilon}\le h.
\]

Squaring (3) gives

\[
\frac{d^2-\varepsilon\gamma^2}{1+\varepsilon}
\le h^2,
\]

which is exactly (5). Equation (6) follows from the lattice covering radius `h=q/2`.

The two error sources therefore add in **squared horizontal depth**:

\[
\text{unresolved depth}^2
\le
\underbrace{\varepsilon\gamma^2}_{\text{amplitude slack}}
+
\underbrace{(1+\varepsilon)h^2}_{\text{sampling slack}}.
\tag{13}
\]

This is stronger than treating mesh resolution and endpoint precision as two qualitative requirements. It gives the exact exchange rate between them in the scalar model.

## 4. Sharpness

The bound is geometrically sharp in the same sense as WI-401's `q/2` endpoint law. Suppose the sample set has an open gap of length `2h`, centered at some admissible value `C`. Choose `gamma,d` so that

\[
C_{\rho,\varepsilon}=C,
\qquad
H_{\rho,\varepsilon}=h.
\]

The second equation is exactly

\[
d^2=\varepsilon\gamma^2+(1+\varepsilon)h^2.
\tag{14}
\]

Together with the first it gives a two-equation algebraic placement problem; whenever the resulting `gamma>0` and `0<d<1/2` lie in the zeta geometric range, the superlevel interval is exactly that gap. At its two endpoints

\[
r_\rho(T)=1+\varepsilon,
\]

and outside the gap this one-zero factor is at most the certified threshold. A uniform lattice permits such midpoint placement after choosing the ordinate continuously in this scalar falsification model.

As in WI-401, this does **not** construct a compatible zeta zero set or satisfy the full explicit formula. It proves only that scalar sampled threshold data cannot improve (5) without extra arithmetic or cross-height structure.

## 5. Consequences for arithmetic precision

Equation (7) shows that dense height sampling by itself is insufficient once the certified prime bound has a positive excess above one. A height-independent `epsilon>0` cannot produce any nontrivial restriction on all high zeros: for

\[
\gamma\ge\frac{1}{2\sqrt\varepsilon},
\]

the right side of (7) is at least `1/2`, no better than the classical critical strip.

Conversely, if one aims only at a fixed strip `d<=a` in a height range where the sample covering radius is `h<a`, equation (5) shows the necessary resolution scale suggested by the sharp scalar model:

\[
\varepsilon\gamma^2+(1+\varepsilon)h^2\lesssim a^2.
\tag{15}
\]

With negligible mesh error this means `epsilon=O(a^2/gamma^2)`. This recovers quantitatively the peak-excess observation in WI-401, where a defect has maximum violation

\[
r_\rho(T_{\rm peak})-1=\frac{d^2}{\gamma^2}.
\]

The present finding shows that this amplitude scale and the mesh scale combine by the exact law (13).

This does not itself yield a defect-to-zero bootstrap. An asymptotic statement forcing `d=o(1)` as `gamma->infinity` still permits a zero-density family of off-line zeros with depths tending to zero. To prove RH from sampled bounds, one needs either exact endpoint control on a dense set, arbitrarily refinable local bounds whose mesh and amplitude terms both tend to zero around every possible zero height, or an additional invariant that converts small nonzero depth into a contradiction.

## 6. Prior art and novelty boundary

Rafik's preprint is direct prior art for the fixed-height factor, its peak behavior, the prime/zero root-growth interface, and the qualitative statement that an off-line zero creates a fixed-height violation. WI-400 derives the exact full-profile width recovery; WI-401 derives the endpoint visibility interval and its `q/2` sampling law.

A targeted search for Widder root-growth sampling with non-endpoint thresholds, covering-radius/margin tradeoffs, and quantitative horizontal-defect resolution located the Rafik source and classical neighboring Widder/Stieltjes material, but no separate statement of (2)--(6) or the squared-depth law (13). This search absence is recorded only as a novelty audit and is not a priority claim.

The new Mathia deduction is elementary once the one-zero factor and threshold transport are granted: factor the general `K=1+epsilon` superlevel quadratic, identify the exact interval, and combine its half-width with sampling covering radius. The result should therefore be read as an exact structural consequence of the recent source interface, not as independent validation of that interface.

## 7. Failure modes and decisive audit

The finding has four load-bearing checks:

1. verify WI-400's threshold transfer (8) for every fixed `K>=1` from the bounded explicit-formula remainder;
2. verify the discriminant factorization (10) and the positive roots (11)--(12);
3. verify that the sample covering-radius hypothesis is taken over the **shifted centers** `C_{rho,epsilon}`, not the endpoint centers of WI-401;
4. keep the source-evidence boundary explicit: Rafik's Appendix A is recent and non-peer-reviewed, so every prime-side consequence remains conditional on that fixed-height interface until independently rederived or otherwise validated.

No floating-point computation, numerical certificate, density hypothesis, or conjectural zero correlation enters (1)--(15).

## Research consequence

WI-401 separated sampling width from violation amplitude qualitatively. WI-402 makes their coupling exact. In the scalar Widder route, a root-rate slack `epsilon` at height `gamma` costs the same defect-resolution budget as horizontal depth `sqrt(epsilon) gamma`, while mesh covering radius contributes orthogonally through `(1+epsilon)h^2`.

This closes a tempting implementation shortcut: one cannot replace the exact endpoint theorem by a fixed-accuracy numerical or analytic estimate `L_P<=1+epsilon` and compensate merely by sampling heights more densely. At high ordinate that amplitude slack dominates regardless of mesh density. Any viable RH-facing implementation of the Widder detector must therefore control both resources at the correct scales, or introduce genuinely new cross-height/phase/arithmetic information.