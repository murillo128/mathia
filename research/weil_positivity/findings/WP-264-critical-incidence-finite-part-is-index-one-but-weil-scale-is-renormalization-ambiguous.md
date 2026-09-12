---
id: WP-264
title: Critical incidence finite part is index one but the Weil scale is renormalization-ambiguous
branch: weil_positivity
status: supported
kind: negative
claim_strength: exact theorem for the renormalized critical complete-incidence family
created: 2026-09-12
refined: 2026-09-12
related: [WP-035, WP-262, WP-263]
prior_art:
  - weighted complete-graph incidence Grams and signless Laplacians
  - rank-one perturbation and Sylvester-inertia arguments
  - Hodge-index signature as a comparison mechanism only
  - finite-part subtraction and counterterm ambiguity
---

# WP-264 — Critical incidence finite part is index one but the Weil scale is renormalization-ambiguous

## Claim

The critical complete Gibbs incidence that collapses after unit-diagonal normalization in `WP-263` has a different, nontrivial limit if its divergent diagonal is subtracted before normalization. On the prime layer, the unnormalized finite-cutoff Gram splits exactly into a divergent positive diagonal plus a trace-class mixed-prime remainder. Subtracting only the divergent coefficient leaves

\[
R=aa^*-2D,
\qquad
D=\operatorname{diag}\!\left(\frac{\log p}{p^{3/2}}\right),
\qquad
a_p=\frac{\sqrt{\log p}}{p^{3/4}}.
\]

This remainder is a compact trace-class self-adjoint operator with **exactly one positive direction**, and it is strictly negative on the canonical codimension-one hyperplane `ker(a^*)`. Thus the complete-incidence route really can create a global Hodge-index-like signature that evades the unbounded-index obstruction of `WP-035`.

However, this does not produce a canonical Weil-positive geometry. The source fixes the divergent subtraction only up to a finite constant. Every admissible scalar finite-part choice has the form

\[
R_C=aa^*-2D+C D_W,
\qquad
D_W=\operatorname{diag}\!\left(\frac{\log p}{\sqrt p}\right).
\]

The unfixed counterterm direction `D_W` is exactly the critical Mangoldt half-density scale carried by the Fock construction. For `C<=0` the index-one sign theorem survives, so the sign does not select the finite constant; for `C>0` the positive index becomes infinite. The algebraically minimal choice `C=0` leaves the primitive positive metric at the smaller scale `(log p)/p^{3/2}`, with an extra factor `1/p` relative to the critical Weil carrier. Hence the apparent Hodge mechanism is real but its connection to the Weil coefficient is renormalization-programmable rather than source-forced.

## Derivation or evidence

Retain the symmetric-Fock prime layer and the exact critical source weight from `WP-262`,

\[
w_p:=\frac{\log p}{\sqrt p}.
\]

For a finite prime cutoff `P_X={p:p<=X}`, let

\[
H_X:=\sum_{q\le X}\frac1q
\]

and use the **unnormalized** complete Gibbs incidence

\[
U_X e_p
:=
\sqrt{w_p}\sum_{\substack{q\le X\\q\ne p}}
q^{-1/2}e_{pq},
\qquad p\le X.
\]

Unique factorization gives, for distinct `p,r<=X`,

\[
\langle U_Xe_p,U_Xe_r\rangle
=
\frac{\sqrt{w_pw_r}}{\sqrt{pr}},
\]

while

\[
\|U_Xe_p\|^2
=w_p\left(H_X-\frac1p\right).
\]

Set

\[
d_p:=\frac{w_p}{p}=\frac{\log p}{p^{3/2}},
\qquad
a_p:=\sqrt{d_p},
\qquad
D_W=\operatorname{diag}(w_p),
\qquad
D=\operatorname{diag}(d_p).
\]

The cutoff Gram `M_X=U_X^*U_X` therefore has the exact matrix decomposition

\[
\boxed{
M_X=H_XD_W+a_Xa_X^*-2D_X.
}
\tag{1}
\]

Indeed the rank-one term supplies every off-diagonal entry and contributes `d_p` on the diagonal, while `-2D_X` changes that contribution to `-d_p`, giving the required diagonal `w_p(H_X-1/p)`.

Because

\[
\sum_p d_p
=
\sum_p\frac{\log p}{p^{3/2}}<\infty,
\]

we have `a in ell^2`, `D` trace class, and

\[
R_X:=M_X-H_XD_W=a_Xa_X^*-2D_X
\longrightarrow
R:=aa^*-2D
\]

in trace norm after extending the cutoff operators by zero. Thus the divergent complete incidence contains a well-defined trace-class mixed-prime finite part once one chooses the subtraction in (1).

The inertia is exact. On any finite set `F` of `m>=3` primes, let `T_F=diag(a_p)_{p in F}`. Then

\[
R_F=T_F(J_m-2I_m)T_F,
\tag{2}
\]

where `J_m` is the all-ones matrix. Since `J_m-2I_m` has eigenvalues `m-2` once and `-2` with multiplicity `m-1`, Sylvester inertia gives

\[
n_+(R_F)=1,
\qquad
n_-(R_F)=m-1.
\]

Globally, `R` is a rank-one perturbation of the strictly negative operator `-2D`, so it has at most one positive direction. Equation (2) on any three primes supplies a positive vector, hence

\[
\boxed{n_+(R)=1.}
\tag{3}
\]

Moreover, on the source-defined hyperplane

\[
\mathcal P:=\ker a^*,
\]

one has exactly

\[
\boxed{
\langle x,Rx\rangle
=-2\sum_p\frac{\log p}{p^{3/2}}|x_p|^2<0
\quad(x\in\mathcal P\setminus\{0\}).
}
\tag{4}
\]

So `-R` is genuinely positive on a codimension-one primitive space. Unlike the separable Prime-Circle globalization excluded by `WP-035`, the complete mixed-prime rank-one term enters **before** the sign theorem and collapses the global positive index to one.

The canonicity test is nevertheless fatal for the present route. Replace the subtraction `H_XD_W` by `c_XD_W`. A finite operator-norm limit requires, along the chosen exhaustion,

\[
H_X-c_X\longrightarrow C
\]

for some finite constant, and the resulting family is

\[
\boxed{
R_C=aa^*-2D+CD_W.
}
\tag{5}
\]

This is not a cosmetic freedom. On `ker a^*`,

\[
\langle x,R_Cx\rangle
=
\sum_p w_p\left(C-\frac2p\right)|x_p|^2.
\tag{6}
\]

For every `C<=0`, the diagonal part in (6) is strictly negative and the rank-one perturbation permits at most one positive direction. A positive direction nevertheless exists: after the change of variables `y_p=a_px_p`, positivity on a finite set is equivalent to the rank-one criterion

\[
\sum_{p\in F}\frac1{2-Cp}>1,
\]

which holds for some finite `F` because it is immediate for `C=0` with three primes, while for `C<0` the prime harmonic divergence makes the partial sums unbounded. Therefore

\[
\boxed{n_+(R_C)=1\quad\text{for every }C\le0.}
\tag{7}
\]

For `C>0`, the diagonal operator `CD_W-2D` is positive on all sufficiently large prime coordinates, so `R_C` has infinite positive index. Thus the Hodge-like sign condition constrains the finite part only to the half-line `C<=0`; it does **not** choose one normalization.

At the simplest subtraction `C=0`, the primitive positive metric from (4) is weighted by `(log p)/p^{3/2}` rather than the critical carrier `(log p)/sqrt p`. Choosing `C<0` inserts an arbitrary positive multiple `(-C)D_W` into `-R_C` on top of the smaller `2D` correction. Consequently the exact scale one hopes to explain is itself an unfixed finite counterterm direction.

## Prior-art and novelty audit

None of the ingredients is a new general theorem. Complete-graph incidence Grams, rank-one perturbations, Sylvester inertia, Hodge-index signature comparisons, and finite-part/counterterm ambiguities are classical mechanisms. The Bost--Connes and statistical-mechanical literature already makes the logarithmic Hamiltonian and critical zeta boundary natural, but it does not by itself turn this particular Fock complete-incidence finite part into a Weil sign theorem.

The branch-specific result is the exact conjunction of those mechanisms in the `WP-262`--`WP-263` carrier: the same source-forced critical complete incidence that becomes pairwise diagonal after probabilistic normalization has an index-one trace-class remainder after diagonal subtraction, and the complete family of scalar finite parts exposes the critical Weil carrier itself as the unfixed counterterm direction. This is therefore a narrowing/canonicity result, not a claim of a new Hodge theorem or a new renormalization theory.

## Falsification target

This finding would cease to block the route if an independently defined Mathia/global construction fixed the finite subtraction constant (or replaced scalar subtraction by a source-forced non-scalar boundary operation), retained the index-one or stronger positivity theorem, and simultaneously produced the correct finite Weil orientation together with the archimedean Gamma and polar terms. The fixing rule must be determined before comparison with the Weil target; choosing `C` because it improves the desired coefficient does not count.

A second genuine escape would derive a different pre-normalization all-prime incidence whose divergent part and finite remainder are both fixed by one global boundary/cohomological theorem, leaving no free `D_W` counterterm. Neither escape is supplied by the present Fock/Gibbs construction.

## Consequence

`WP-263` should not be read as saying that critical complete incidence contains no nontrivial global geometry. It contains a surprisingly sharp one: after finite-part subtraction its mixed-prime remainder has exactly the Hodge-like signature `(1, infinity)` and a canonical primitive hyperplane. But **the sign theorem is less selective than the arithmetic target**. The whole half-line of finite parts `C<=0` has the same one-positive-direction property, while the coefficient scale needed for the Weil carrier lies precisely in the unfixed diagonal counterterm.

The viable frontier is therefore narrower. A future construction must not merely rescue cross-prime coherence from the divergent prime layer; it must also fix its finite renormalization intrinsically and couple that choice to the archimedean/polar completion. Without such a theorem, the index-one remainder is a genuine geometric intermediate result but not an independent global Weil-positivity mechanism.
