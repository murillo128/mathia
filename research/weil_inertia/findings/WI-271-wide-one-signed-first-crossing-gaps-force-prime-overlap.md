# WI-271 — wide one-signed first-crossing gaps force prime-power overlap

## Status

- **Evidence:** `EXACT-DERIVED + SOURCE-SPECIFIC-RIGIDITY + LITERATURE+DERIVED + PRIOR-ART-AUDITED`.
- **Scope:** a quantitative source-specific constraint on the one-signed branch of a hypothetical first unrestricted Suzuki null mode. An internal support gap at least as long as the unique positive-source range cannot be screened purely by the archimedean part: firstness forces positive von-Mangoldt overlap across the gap.
- **What it does not claim:** this is not RH, does not show that an arbitrary first null mode is one-signed, and does not force prime overlap when every internal gap is shorter than the archimedean sign-change length. The sign-changing branch still requires the nodal/signed-Laplacian analysis of `WI-269`.

## Claim

Assume RH is false and let

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\}
\]

be the first unrestricted crossing of Suzuki's localized Weil ground-state energy. Let `v` be a normalized real null mode

\[
\|v\|_2=1,
\qquad
A_av=0,
\qquad
q_a\ge0,
\tag{1}
\]

and assume the one-signed branch; after changing sign if necessary,

\[
v\ge0\quad\text{a.e.}
\tag{2}
\]

Use the exact archimedean source weight from `WI-269`,

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\tag{3}
\]

and let

\[
h_0=\log\rho,
\qquad
\rho^3-\rho-1=0.
\tag{4}
\]

Then

\[
w(h)>0\quad(0<h<h_0),
\qquad
w(h_0)=0,
\qquad
w(h)<0\quad(h>h_0).
\tag{5}
\]

Suppose there is an internal essential-support gap

\[
(\alpha,\beta)\subset(-a,a),
\qquad
v=0\ \text{a.e. on }(\alpha,\beta),
\tag{6}
\]

with positive `L^2` mass on both sides,

\[
M_L:=\int_{-a}^{\alpha}v(x)^2\,dx>0,
\qquad
M_R:=\int_{\beta}^{a}v(x)^2\,dx>0.
\tag{7}
\]

Write

\[
L:=\beta-\alpha,
\qquad
r_L:=\frac{a+\alpha}{2},
\qquad
r_R:=\frac{a-\beta}{2},
\tag{8}
\]

and define the cross-gap overlap at separation `h>0` by

\[
J_{\alpha,\beta}(h)
:=
\int_{\mathbb R}
\mathbf 1_{\{x\le\alpha,\ x+h\ge\beta\}}
 v(x+h)v(x)\,dx.
\tag{9}
\]

If

\[
\boxed{L\ge h_0,}
\tag{10}
\]

then the prime-power cross-gap mass obeys

\[
\boxed{
P_{\alpha,\beta}
:=
\sum_{\substack{L\le\log n<2a\\ \Lambda(n)>0}}
\frac{\Lambda(n)}{\sqrt n}
J_{\alpha,\beta}(\log n)
\ge
\max\!\left\{
\lambda_{r_L}M_L,
\lambda_{r_R}M_R
\right\}
>0.
}
\tag{11}
\]

Consequently at least one active prime power satisfies

\[
L\le\log n<2a,
\qquad
\boxed{C_v(\log n)>0,}
\tag{12}
\]

where

\[
C_v(h):=\int_{\mathbb R}v(x+h)v(x)\,dx.
\tag{13}
\]

More quantitatively, put

\[
W_a(L)
:=
\sum_{\substack{L\le\log n<2a\\ \Lambda(n)>0}}
\frac{\Lambda(n)}{\sqrt n}.
\tag{14}
\]

Equation (11) forces `W_a(L)>0`, and

\[
\boxed{
\max_{\substack{L\le\log n<2a\\ \Lambda(n)>0}}
C_v(\log n)
\ge
\frac{
\max\{\lambda_{r_L}M_L,\lambda_{r_R}M_R\}
}{W_a(L)}.
}
\tag{15}
\]

Thus complete prime-lag screening on the one-signed first-crossing branch implies the sharper geometric consequence

\[
\boxed{
\text{there is no internal essential-support gap of length }\ge h_0
\text{ separating positive mass.}
}
\tag{16}
\]

This improves the `2h_0` support-gap corollary of `WI-270` to the exact source sign-change scale `h_0`, and it proves more than gap exclusion: a gap at or beyond that scale forces an explicitly positive arithmetic autocorrelation.

## 1. A smooth cut through the gap exactly isolates the two side modes

Choose a bounded Lipschitz function `chi` satisfying

\[
\chi(x)=0\quad(x\le\alpha),
\qquad
\chi(x)=1\quad(x\ge\beta),
\tag{17}
\]

with its transition contained in `(\alpha,\beta)`. Because `v=0` almost everywhere on the transition region,

\[
\chi v=v_R:=v\,\mathbf 1_{[\beta,a]},
\qquad
(1-\chi)v=v_L:=v\,\mathbf 1_{[-a,\alpha]}.
\tag{18}
\]

This avoids the sharp-cut domain issue entirely. `WI-269` proves that bounded Lipschitz multipliers preserve the first-crossing form domain and gives the exact ground-state transform

\[
q_a(\chi v)
=
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
D_\chi(v;\log n)
+
\int_0^{2a}w(h)D_\chi(v;h)\,dh,
\tag{19}
\]

where

\[
D_\chi(v;h)
=
\int_{\mathbb R}
(\chi(x+h)-\chi(x))^2v(x+h)v(x)\,dx.
\tag{20}
\]

For the present cut, every nonzero product in (20) has both points outside the gap. If both lie on the same side, the multiplier difference is zero; if they lie on opposite sides, the squared difference is one. Therefore

\[
\boxed{
D_\chi(v;h)=J_{\alpha,\beta}(h).
}
\tag{21}
\]

The same identity holds for `1-chi`, because its squared multiplier difference is identical. Hence the two side modes have the same energy

\[
q_a(v_L)=q_a(v_R)=:Q_{\alpha,\beta},
\tag{22}
\]

with

\[
Q_{\alpha,\beta}
=
P_{\alpha,\beta}
+
\int_L^{2a}w(h)J_{\alpha,\beta}(h)\,dh.
\tag{23}
\]

The lower integration limit is exact: a pair crossing the gap has one point at or to the left of `alpha` and the other at or to the right of `beta`, so its separation is at least `L`.

## 2. Firstness makes the cross-gap energy strictly positive

The left mode is supported in an interval of length `a+alpha`, and the right mode in one of length `a-beta`. Translation invariance of the global Weil form and the definition of the first crossing therefore give

\[
q_a(v_L)
\ge
\lambda_{r_L}M_L,
\qquad
q_a(v_R)
\ge
\lambda_{r_R}M_R.
\tag{24}
\]

Because the gap is internal and both side masses are positive,

\[
0<r_L<a,
\qquad
0<r_R<a.
\tag{25}
\]

By the definition of `a_*`, every proper radius has strictly positive ground-state energy:

\[
\lambda_{r_L}>0,
\qquad
\lambda_{r_R}>0.
\tag{26}
\]

Combining (22)--(26),

\[
\boxed{
Q_{\alpha,\beta}
\ge
\max\!\left\{
\lambda_{r_L}M_L,
\lambda_{r_R}M_R
\right\}
>0.
}
\tag{27}
\]

This is the same firstness mechanism underlying the half-cut lower bound in `WI-270`, but the genuine support gap lets the cut be implemented by a smooth multiplier and lets the actual side support radii `r_L,r_R` be used directly.

## 3. At the sign-change scale the archimedean source can only lower the cut energy

Since `v>=0`,

\[
J_{\alpha,\beta}(h)\ge0.
\tag{28}
\]

Under the width hypothesis `L>=h_0`, equations (5) and (23) imply

\[
\int_L^{2a}w(h)J_{\alpha,\beta}(h)\,dh\le0.
\tag{29}
\]

Therefore

\[
P_{\alpha,\beta}
\ge
Q_{\alpha,\beta}.
\tag{30}
\]

Together with (27), this proves (11). No Carleman estimate is used: once the whole cross-gap geometry lies beyond `h_0`, the positive short-range archimedean currency from `WI-270` disappears completely, while the long-range archimedean contribution has the wrong sign to pay the positive firstness cost. The only remaining positive currency is the von-Mangoldt source.

Because every term in `P_{\alpha,\beta}` is nonnegative, (11) forces some active prime-power term to be positive. For such a lag,

\[
C_v(\log n)
\ge
J_{\alpha,\beta}(\log n)>0,
\tag{31}
\]

which proves (12). Finally,

\[
P_{\alpha,\beta}
\le
W_a(L)
\max_{\substack{L\le\log n<2a\\\Lambda(n)>0}}
C_v(\log n),
\tag{32}
\]

and (15) follows from (11).

## 4. Relation to the current screening program

`WI-267` proves that an arbitrary Suzuki null mode cannot have a support gap on which every active prime translation is absent, but translated activity alone does not imply nonzero autocorrelation. `WI-269` upgrades firstness to an exact PSD signed-source Laplacian, and `WI-270` shows on the one-signed branch that a cut must be paid either by prime overlap or by bilateral short-range mass. Under complete prime screening, the generic Carleman estimate in `WI-270` ruled out internal gaps of length at least `2h_0`.

The present argument uses the same exact source transform but a stronger geometric hypothesis at the cut: a genuine gap of width at least `h_0`. That geometry removes **all** positive-range archimedean cross edges, not merely the mass in two `h_0` collars. The result is therefore an arithmetic rather than merely topological conclusion: such a gap forces a positive prime-power autocorrelation, quantitatively through (15).

This settles a nontrivial subcase of the accepted first-crossing screening clue. Any completely prime-screened one-signed first null mode must now have support that is `h_0`-gap-connected in the one-dimensional sense. The unresolved case is correspondingly sharper: either the support has no gap of length `h_0`, allowing the positive short-range archimedean network to percolate across every cut, or the first null mode changes sign and the nonnegative-overlap argument fails.

## 5. Boundary conditions and failure modes

The one-signed hypothesis is load-bearing twice. It makes every `J_{alpha,beta}(h)` nonnegative, so the long-range archimedean source has a definite unfavorable sign, and it makes positive prime cut mass imply positive global autocorrelation. For a sign-changing null mode neither implication survives; `WI-269`'s nodal compensation law remains the correct interface.

The threshold `h_0` is exact for this sign-only argument because it is the unique zero of the continuous source `w`. When `L<h_0`, cross-gap pairs can lie in the interval where `w>0`; that positive archimedean contribution may pay some or all of the firstness cost. `WI-270` quantifies that regime with the Hilbert--Carleman bound. Nothing here asserts that gaps below `h_0` are actually realizable or that `h_0` is the optimal threshold after using more source-specific information.

The argument also requires positive mass on both sides. A terminal empty interval adjacent to an endpoint is not an internal separating gap and does not produce two nonzero proper-aperture modes. The conclusion concerns arithmetic overlap of the hypothetical first-crossing mode, not the zero set of zeta directly; an additional argument is still required to exclude the remaining first-crossing geometries and thereby contradict RH failure.

## 6. Prior-art and novelty audit

Masatoshi Suzuki's **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), supplies the localized Weil form/operator and the exact source decomposition. The first-crossing construction, multiplier ground-state transform, and source sign analysis used here are the already-persisted consequences `WI-253`, `WI-269`, and `WI-270`; those ingredients are not claimed as new in this finding.

Ground-state representations for nonlocal quadratic forms and cut tests for signed Laplacians are classical mechanisms. In particular, the general ground-state-transform background audited in `WI-269` and the Hilbert--Carleman literature audited in `WI-270` remain the appropriate neighboring prior art. A targeted search of Suzuki's 2026 operator paper and neighboring localized-Weil, nonlocal ground-state, signed-Laplacian, support-gap, and cut literature found no statement converting the zeta-specific source sign-change length into the prime-overlap conclusion (11)--(15). Search absence is audit context only and is not a priority claim.

The Mathia deduction is the exact combination of three source-specific facts: strict positivity of every proper-aperture ground-state energy at the first crossing, the unique sign change of Suzuki's continuous source at `h_0`, and positivity of the von-Mangoldt coefficients. Once a support gap removes all cross edges below `h_0`, these three facts force the arithmetic source to carry the cut.

## Falsification and audit test

The finding is exact and uses no numerical certificate. A falsification must locate an error in at least one load-bearing step:

1. a Lipschitz transition inside a zero gap satisfies `chi v=v_R` and converts the `WI-269` multiplier identity exactly into the cross-gap overlap (21);
2. every pair contributing across `(alpha,beta)` has separation at least `L`, giving the lower limit in (23);
3. firstness and translation invariance give the proper-aperture lower bounds (24), with strictly positive `lambda_r` for `r<a_*`;
4. `w(h)<=0` for every `h>=h_0`;
5. one-signedness gives `J_{alpha,beta}(h)>=0` and hence (29)--(30);
6. positive weighted cross-gap prime mass forces at least one positive global prime-power autocorrelation, and (32) yields the quantitative bound.

Failure of any of these implications would invalidate the claim. Improvements below `h_0`, by contrast, would strengthen rather than falsify it.

## Consequence for the research line

The one-signed screening branch has acquired a direct defect-to-arithmetic bridge on a geometrically explicit regime. A support gap at the continuous-source sign-change scale cannot be financed by archimedean interactions and therefore exposes a positive prime-power autocorrelation. Complete screening must keep the support `h_0`-gap-connected everywhere.

The next live gate is no longer the `2h_0` topological gap from the generic Carleman estimate. It is whether source-specific firstness can force an `h_0`-scale bottleneck somewhere in a one-signed mode, or whether a completely screened mode can maintain short-range archimedean connectivity across every cut. The sign-changing branch remains separate and must be attacked through the PSD signed-source/nodal constraints rather than by importing this nonnegative-overlap argument.