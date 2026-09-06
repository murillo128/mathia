# WP-172 — Finite Pontryagin defect cannot repair the exact archimedean Gamma phase

**Status:** `LITERATURE+DERIVED + GENERALIZED-SCHUR-NO-GO + KREIN-LANGER-FACTORIZATION + FINITE-NEGATIVE-INDEX + ARCHIMEDEAN-GAMMA + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-170` proves that the exact real-place phase exposed by `WP-169`,

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})},
\qquad |R_\infty(t)|=1\quad(t\in\mathbb R),
\tag{1}
\]

is not an ordinary scalar Schur/inner response. `WP-171` then closes the regular finite-channel Hilbert-passive lift and leaves indefinite `J`-inner/generalized-Schur geometry as one of the explicit surviving categories.

The first indefinite relaxation is also too small. In the classical generalized Schur class with **Hilbert input/output channels and finite negative index** `kappa`, Krein--Langer factorization writes every transfer function as an ordinary Schur numerator divided by a finite Blaschke or Blaschke--Potapov factor of degree `kappa`. That finite denominator can supply only a finite Pontryagin defect. The Gamma phase needs an infinite one.

More precisely, neither orientation

\[
R_\infty,
\qquad R_\infty^{-1}
\tag{2}
\]

belongs to `S_kappa` for any finite `kappa`. The obstruction is exact and stronger than the sign change used in the ordinary passive audit:

- `R_infty` is analytic in the upper half-plane but has the non-Blaschke zero sequence
  \[
  \tau_n=i\left(2n+\frac12\right),\qquad n\ge0,
  \tag{3}
  \]
  already isolated in `WP-170`;
- `R_infty^{-1}` has a pole at every point (3);
- multiplying by a finite Blaschke denominator can neither turn the non-Blaschke zero sequence of the first orientation into the zero set of a bounded analytic function nor cancel the infinitely many poles of the second.

Consequently a Pontryagin-space passive/conservative realization whose external channels are Hilbert and whose transfer has only finitely many negative squares cannot make the exact Gamma phase into its scalar characteristic response. The same obstruction survives finite matrix channel mixing: no fixed scalar matrix coefficient, and in particular no determinant, of a finite-index matrix generalized-Schur transfer can equal `R_infty^{+/-1}` globally.

This is a genuine narrowing beyond `WP-170`/`WP-171`. Finite negative index **does** remove the ordinary Schur sign theorem: inverse Blaschke factors contribute negative boundary delay, and an ordinary inner numerator minus finitely many such defects may have a sign-changing delay. Thus sign change alone no longer kills the category. What kills the exact Gamma phase is its infinite analytic divisor. A finite number of indefinite directions is not enough.

The result does **not** exclude a genuinely indefinite external-channel `J`-inner theory, a Krein-space realization with infinite negative index, a singular/domain-changing operator response, or a nonseparable finite--archimedean construction in which `R_infty` is no longer itself the transfer readout. Those are materially different categories and still require an independent final positivity theorem.

## 1. Finite-negative-square generalized Schur functions have only a finite denominator defect

Use the disk formulation first. For Hilbert input/output spaces, a generalized Schur function `s in S_kappa` is a meromorphic function for which the de Branges--Rovnyak kernel

\[
K_s(z,w)=\frac{1-s(z)s(w)^*}{1-z\bar w}
\tag{4}
\]

has `kappa` negative squares. The classical Krein--Langer theorem gives, in the scalar case,

\[
\boxed{
s(z)=b(z)^{-1}s_0(z),
}
\tag{5}
\]

where `s_0` is an ordinary Schur function and `b` is a finite Blaschke product whose degree is `kappa` (or at most `kappa` under the corresponding at-most convention), with the factors coprime in the exact-index formulation.

For finite-dimensional matrix channels the left factorization is

\[
\boxed{
S(z)=B(z)^{-1}S_0(z),
}
\tag{6}
\]

where `S_0` is an ordinary matrix Schur function and `B` is a finite Blaschke--Potapov product. In particular `det B` is a finite scalar Blaschke product, and

\[
(\det B)S=\operatorname{adj}(B)S_0
\tag{7}
\]

has bounded analytic matrix entries up to an irrelevant finite-dimensional norm constant.

The Cayley map between the disk and the upper half-plane preserves the finite-negative-square class up to the standard positive kernel multiplier and sends finite Blaschke products to finite upper-half-plane Blaschke products. Therefore (5)--(7) may be used directly for the phase (1).

A useful equivalent statement from realization theory is that, with Hilbert external spaces, an `S_kappa` transfer has only `kappa` poles counting multiplicity. This is the finite Pontryagin defect carried by the denominator. The factorization form is preferable here because it also treats the analytic orientation `R_infty`, whose obstruction is a zero-set rather than a pole count.

## 2. The analytic orientation cannot have a finite Krein--Langer denominator

Assume for contradiction that

\[
R_\infty=b^{-1}s_0
\tag{8}
\]

with `b` a finite upper-half-plane Blaschke product and `s_0` ordinary Schur. Then

\[
s_0=bR_\infty.
\tag{9}
\]

The finite product `b` can add only finitely many zeros. It cannot remove any of the infinitely many zeros (3) of `R_infty`. Hence the zero set of the nonzero bounded analytic function `s_0` contains (3).

But (3) violates the upper-half-plane Blaschke condition:

\[
\sum_{n\ge0}
\frac{\operatorname{Im}\tau_n}{1+|\tau_n|^2}
=
\sum_{n\ge0}
\frac{2n+\tfrac12}{1+(2n+\tfrac12)^2}
=\infty.
\tag{10}
\]

No nonzero bounded analytic function can have such a zero set. Equation (9) is impossible. Thus

\[
\boxed{R_\infty\notin S_\kappa\quad\text{for every finite }\kappa.}
\tag{11}
\]

This makes precise the "infinite compensation" statement in `WP-170`: the compensation cannot be merely a finite Pontryagin defect.

## 3. The inverse orientation has infinitely many forbidden poles

For the inverse orientation,

\[
R_\infty^{-1}(\tau)
=\pi^{-i\tau}
\frac{\Gamma(\tfrac14+\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14-\tfrac{i\tau}{2})},
\tag{12}
\]

every point (3) is a simple pole. If

\[
R_\infty^{-1}=b^{-1}s_0,
\tag{13}
\]

then

\[
s_0=bR_\infty^{-1}.
\tag{14}
\]

A finite Blaschke product has only finitely many zeros, so it can cancel at most finitely many of the poles (3). The right side of (14) therefore still has infinitely many upper-half-plane poles and cannot be the analytic Schur numerator `s_0`. Hence

\[
\boxed{R_\infty^{-1}\notin S_\kappa\quad\text{for every finite }\kappa.}
\tag{15}
\]

The two orientations fail for complementary reasons: one needs a bounded numerator with a non-Blaschke zero sequence, while the other needs a finite denominator to absorb infinitely many poles.

## 4. Finite matrix mixing does not hide the divisor

Let `S in S_kappa^{d x d}` have Hilbert external channels and a left Krein--Langer factorization (6). For fixed vectors `u,v in C^d`, (7) implies

\[
(\det B)\,u^*S(z)v
=
u^*\operatorname{adj}(B(z))S_0(z)v,
\tag{16}
\]

which is bounded analytic up to a finite constant depending only on `d`. Therefore any fixed scalar matrix coefficient of `S` becomes an ordinary bounded analytic function after multiplication by the finite scalar Blaschke factor `det B`.

If such a coefficient were exactly `R_infty`, the bounded analytic function in (16) would retain every zero (3), contradicting (10). If it were `R_infty^{-1}`, finitely many zeros of `det B` could cancel only finitely many of its poles. Thus neither orientation can be hidden as a fixed finite-channel coefficient.

For the determinant the conclusion is even more direct:

\[
\det S=\frac{\det S_0}{\det B},
\tag{17}
\]

and `det S_0` is scalar Schur because every singular value of `S_0(z)` is at most one. Hence

\[
\boxed{
\det S\neq cR_\infty^{\pm1}
}
\tag{18}
\]

for every unimodular constant `c` and every finite-index generalized-Schur matrix transfer with Hilbert external channels.

This closes the most direct indefinite extension of the determinant/total-phase strategy left after `WP-171`. It does not classify arbitrary nonlinear or state-dependent scalarizations of a matrix response.

## 5. Matched control: finite negative index really can create negative delay

The obstruction is not a disguised reuse of ordinary Schur positivity. Take a single upper-half-plane Blaschke factor

\[
b_a(z)=\frac{z-a}{z-\bar a},
\qquad \operatorname{Im}a>0.
\tag{19}
\]

Its inverse `b_a^{-1}` is a generalized inner function of index one. On the real line its boundary phase derivative has the opposite sign from the ordinary inner factor:

\[
-i\overline{b_a(t)^{-1}}\frac{d}{dt}b_a(t)^{-1}
=-\frac{2\operatorname{Im}a}{|t-a|^2}<0.
\tag{20}
\]

More generally, if a scalar generalized inner function has finite-index factorization `s=b^{-1}s_0`, then distributionally its boundary delay is

\[
q_s=q_{s_0}-q_b,
\tag{21}
\]

where `q_{s_0}` is the nonnegative inner phase measure and `q_b` is a finite sum of positive Poisson kernels. Finite negative index therefore genuinely permits negative delay and even sign changes. The Hilbert-passive cone obstruction of `WP-170`/`WP-171` has been relaxed.

But the negative defect in (21) is only finite. In particular it decays like `O(t^{-2})` away from the finite pole locations, whereas the Gamma orientation associated with `R_infty` has

\[
\frac{d}{dt}\arg R_\infty(t)
=-A_\infty(t)
=-\log\frac{t}{2\pi}+O(t^{-2})
\longrightarrow-\infty.
\tag{22}
\]

So the boundary behavior independently reflects the same mismatch: a finite sum of inverse-Blaschke defects cannot supply the unbounded negative Gamma tail on top of a nonnegative inner contribution. The divisor proof (11) is stronger and avoids boundary-regularity assumptions, while (22) shows geometrically why a finite Pontryagin defect is the wrong scale.

## 6. Aggressive falsification and exact scope

**Infinite zero sets are not themselves an obstruction.** An ordinary inner numerator may have infinitely many Blaschke zeros. What is decisive is the logarithmically divergent non-Blaschke sequence (3). Adding or deleting finitely many zeros does not change divergence of (10).

**Finite negative index is not the same as finite-dimensional state space.** The positive part of a Pontryagin realization may be infinite-dimensional and `s_0` may be a genuinely nonrational Schur function. The result still holds because only the negative index -- equivalently the Krein--Langer denominator degree -- is finite. This is stronger than the trivial observation that a finite-state rational transfer cannot equal a Gamma ratio.

**A finite compensator cannot repair the divisor.** Multiplying by delays, ordinary inner factors, or finite generalized-Schur all-pass factors changes the divisor by at most an admissible Blaschke zero set plus finitely many poles. It cannot remove the non-Blaschke tail (3) or absorb the inverse orientation's infinitely many poles.

**Indefinite external channels are not covered.** The clean finite-pole Krein--Langer statement used above assumes Hilbert input/output spaces. For genuinely Pontryagin input/output channel spaces of nonzero negative index, generalized Schur--Nevanlinna theory is more complicated and finite kernel index need not imply only finitely many poles. This is an explicit remaining escape, not a technical omission. Any Mathia use of it would also have to explain why the external indefinite metric is source-forced and how a final Hilbert-positive Weil form emerges from it.

**Infinite negative index is not excluded.** A Krein rather than Pontryagin state space can carry infinitely many negative directions. Such a category might accommodate the required infinite divisor, but ordinary finite-negative-square realization theory then no longer supplies a finite-defect positivity mechanism. An independent coercive quotient/compression theorem would be required.

**Nonseparable assembly remains open.** The finding tests the exact `R_infty` phase, its inverse, and fixed finite-channel readouts as characteristic responses. It does not exclude a construction in which finite-prime incidence and the real-place phase are coupled before a generalized transfer or positive form is defined, so that neither sector separately equals (1).

These boundaries matter because the branch mandate asks for positivity inherited from geometry, not merely for enough indefinite freedom to interpolate a desired phase.

## 7. Prior-art and novelty audit

The generalized Schur theorem used here is classical. The primary source is M. G. Krein and H. Langer, *Über einige Fortsetzungsprobleme, die eng mit der Theorie hermitescher Operatoren im Raume Pi_kappa zusammenhängen. I. Einige Funktionenklassen und ihre Darstellungen*, Mathematische Nachrichten 77 (1977), 187--236, DOI `10.1002/mana.19770770116`. A systematic realization-theoretic reference is Daniel Alpay, Aad Dijksma, James Rovnyak, and Hendrik S. V. de Snoo, *Schur Functions, Operator Colligations, and Reproducing Kernel Pontryagin Spaces*, Operator Theory: Advances and Applications 96, Birkhauser (1997), DOI `10.1007/978-3-0348-8908-7`.

For the exact system-theoretic formulation used in the audit, Lassi Lilleberg, *Passive Discrete-Time Systems with a Pontryagin State Space*, Complex Analysis and Operator Theory 13 (2019), 3767--3793, DOI `10.1007/s11785-019-00930-1`, states the left/right Krein--Langer factorization for Hilbert external channels and the resulting finite pole multiplicity. Lilleberg's later *Generalized Schur--Nevanlinna functions and their realizations*, Integral Equations and Operator Theory 92 (2020), DOI `10.1007/s00020-020-02600-w`, is also the relevant warning that genuinely Pontryagin external channel spaces are a broader category in which countably many poles can occur.

No novelty is claimed for negative squares, Krein--Langer factorization, Blaschke--Potapov products, or Pontryagin passive realizations. The Mathia-specific substantive delta is the application of that classical finite-defect classification to the exact Gamma phase divisor proved in `WP-170`. A bounded literature search found the generalized-Schur machinery and its indefinite-channel extensions, but no independent positivity theorem turning this particular Gamma ratio into a finite-index Pontryagin passive response. The result should therefore be read as a branch-specific no-go, not as a new theorem in generalized Schur theory.

## 8. Consequence for the Weil-positivity search

`WP-171` showed that ordinary Hilbert-passive finite-channel mixing cannot reproduce the signed Gamma delay by a positive boundary-delay observable. The obvious next relaxation was to permit a finite Pontryagin defect so that negative delay directions become legal. `WP-172` shows that this relaxation is still analytically too small:

\[
\boxed{
\text{ordinary Schur}
\;\longrightarrow\;
\text{finite-index generalized Schur}
\quad\text{still cannot carry }R_\infty^{\pm1}.
}
\tag{23}
\]

The required compensation is not merely indefinite; it is **infinite-defect or structurally different**. A viable continuation must therefore justify at least one of the following from Mathia's own geometry: genuinely indefinite external channels, infinite negative index with a later independent positive quotient, a singular/domain-changing operator category, or a nonseparable finite--archimedean object formed before the Gamma phase becomes a scalar transfer response.

This sharpening is useful because it prevents a cheap escape from the passive no-go. Adding finitely many negative directions can change the sign, but it cannot change the analytic divisor enough to host the exact real-place phase.