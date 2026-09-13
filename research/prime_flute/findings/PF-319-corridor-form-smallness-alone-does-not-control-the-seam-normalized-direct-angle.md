# PF-319 — corridor form-smallness alone does not control the seam-normalized direct angle

**Status:** `EXACT-DERIVED + TWO-METRIC-COUNTERMODEL + DECISIVE-NEGATIVE/PROOF-STRATEGY-OBSTRUCTION + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-232-hypercycle-straightening-shear-is-reciprocal-prime-form-small|PF-232]] proves that the straightened hypercycle corridor is a reciprocal-prime relative perturbation of its variable-width diagonal comparison in the **corridor energy metric**. [[research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace|PF-318]] asks for a reciprocal-prime mean-square bound after a different normalization: the PF-205 seam energy used in the direct physical low/high angle.

Those two statements cannot be connected by Loewner comparison alone. A relative form error that is `O(P_n^{-1})` after normalization by the diagonal corridor form can become order one, or arbitrarily larger, after normalization by a second positive form unless the change of energy metric is controlled on the relevant source/target sectors. The obstruction is already exact in dimension two.

This sharply limits how PF-232 may be used in the current direct-angle program. Its `O(P_n^{-1})` form sandwich removes the apparent order-one graph-straightening coefficient as a geometric obstruction, but it does **not** by itself establish the PF-318 local Hilbert--Schmidt leakage bound. A positive proof must additionally use structure of the actual hypercycle/shear map in the seam-normalized physical-frequency representation — for example the mode locality developed in PF-239/PF-242/PF-255 — or prove the required mixed corner directly.

## Claim

Let `A,B,Q>0` be positive definite operators on a finite-dimensional Hilbert space, and suppose

\[
(1-\varepsilon)B\le A\le(1+\delta)B,
\qquad 0\le\varepsilon<1,\quad \delta\ge0.
\tag{1}
\]

Define the corridor-relative perturbation

\[
E:=B^{-1/2}(A-B)B^{-1/2}.
\tag{2}
\]

Then

\[
-\varepsilon I\le E\le\delta I,
\qquad
\boxed{\|E\|\le\eta:=\max\{\varepsilon,\delta\}.}
\tag{3}
\]

Consequently, if `L` is an orthogonal projection of rank `r` and `H` any orthogonal projection, then in the **`B`-normalized metric**

\[
\boxed{
\|LEH\|_{\mathcal S_2}^2\le r\eta^2.
}
\tag{4}
\]

However the same perturbation in the `Q`-normalized metric is

\[
D_Q:=Q^{-1/2}(A-B)Q^{-1/2}
=C^*EC,
\qquad
C:=B^{1/2}Q^{-1/2}.
\tag{5}
\]

Thus the relative form bound controls `D_Q` only after controlling the change-of-metric factors carried by `C` on the relevant source and target sectors.

There is no bound on a mixed `L/H` corner of `D_Q` in terms of `\eta` and `r` alone. Indeed, on `\mathbb C^2=\operatorname{span}\{e_L,e_H\}` choose

\[
B=\begin{pmatrix}b_L&0\\0&b_H\end{pmatrix},
\qquad
Q=\begin{pmatrix}q_L&0\\0&q_H\end{pmatrix},
\qquad
E=\eta
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\tag{6}
\]

with `0<\eta<1` and all four diagonal parameters positive, and put

\[
A:=B^{1/2}(I+E)B^{1/2}.
\tag{7}
\]

Then `A>0` and exactly

\[
(1-\eta)B\le A\le(1+\eta)B,
\tag{8}
\]

while the seam-normalized mixed matrix element is

\[
\boxed{
\left|\langle e_L,D_Qe_H\rangle\right|
=\eta\sqrt{\frac{b_L}{q_L}}\sqrt{\frac{b_H}{q_H}}.
}
\tag{9}
\]

The right-hand side can be made arbitrarily large while the relative form error `\eta` is fixed. Hence a small Loewner-relative perturbation in one energy metric does not imply a small mixed block after an unrelated positive normalization.

For PF-232 one may take `A` to be the straightened hypercycle energy DtN form and `B` its variable-width diagonal comparison. PF-232 gives

\[
(1-\beta_n)B\le A\le(1+\beta_n+\beta_n^2)B,
\qquad
\beta_n=O(P_n^{-1}),
\tag{10}
\]

so (3)--(4) show that **in the diagonal-corridor metric itself** a logarithmic-rank mixed corner would automatically have the PF-318 mean-square scale

\[
O\!\left(\frac{1+\log P_n}{P_n^2}\right).
\tag{11}
\]

But the actual direct-angle normalization is the PF-205 seam form `Q=\Lambda_Q^0` (up to the controlled PF-234 comparison), not `B`. Equation (5) is therefore the missing conversion. No estimate of the PF-318 corner follows from (10) until the relevant parts of `B^{1/2}Q^{-1/2}` are controlled or the special structure of the actual perturbation prevents the worst-case alignment in (9).

## Why the metric mismatch is real at thin-corridor scale

The flat matched control already shows that the two natural energies need not be uniformly comparable. PF-228 gives, on tangential frequency `\mu=\sqrt{1+\xi^2}`, the corridor DtN matrix

\[
\Lambda_E(\mu)
=\mu
\begin{pmatrix}
\coth(\mu s)&-\operatorname{csch}(\mu s)\\
-\operatorname{csch}(\mu s)&\coth(\mu s)
\end{pmatrix},
\tag{12}
\]

whereas the symmetric seam branch is

\[
q_w(\mu)=\mu\tanh(\mu w).
\tag{13}
\]

For bounded physical frequency with `\mu s\ll1` and `\mu w\ll1`, the hard corridor branch is of scale `s^{-1}` while the symmetric seam energy is of scale `w\mu^2`. Their ratio therefore contains the large thin-geometry factor `(sw)^{-1}`. This is precisely why a congruence from the corridor metric to the seam metric is not a harmless bounded change of norm at the endpoint.

This observation is only a scale calibration. The two-dimensional countermodel does **not** assert that the canonical hypercycle shear actually aligns with the worst-conditioned directions. PF-239, PF-242 and PF-255 record additional locality of the real geometric transport that is absent from the countermodel and may prevent such alignment.

## Prior art and novelty audit

The order-theoretic step in (1)--(5) is elementary classical positive-operator algebra: Loewner order is preserved under congruence, and the Hilbert--Schmidt estimate (4) is the standard finite-rank consequence of an operator-norm bound. The two-dimensional construction (6)--(9) is likewise an elementary counterexample. No general matrix/operator theorem is claimed as new.

The project-specific delta is the identification of the **two-metric amplification** at the exact PF-318 frontier. PF-232 already warns that its form comparison does not compare the seam-normalized off-diagonal block; PF-319 makes that warning quantitative and proves that no argument using only the PF-232 relative Loewner sandwich can close the direct-angle endpoint. The surviving proof obligation is therefore structural rather than order-theoretic.

## Boundary and consequences

PF-319 does not refute the PF-318 Hilbert--Schmidt target, does not show that the real hypercycle shear violates weak trace class, and does not estimate the finite one-cusp pant completion. It also says nothing about the independent conditional channel `T_H` from PF-315--PF-316.

It does rule out one tempting shortcut: `\beta_n=O(P_n^{-1})` in PF-232 cannot simply be multiplied by the `O(\log P_n)` low rank and declared endpoint-complete after seam normalization. To close the shear part of the accepted direct-angle clue, one must instead prove at least one of the following for the actual canonical geometry:

1. a seam-normalized rowwise/Hilbert--Schmidt estimate directly at the PF-318 scale;
2. a source/target-restricted bound on the metric conversion `B^{1/2}Q^{-1/2}` strong enough to preserve reciprocal-prime leakage;
3. a locality/almost-diagonal statement for the actual shear perturbation in the physical-frequency/seam basis that prevents the cross-metric amplification exhibited by (9).

PF-239/PF-242/PF-255 make the third route plausible, but none of them by itself supplies the complete local `L/H` Hilbert--Schmidt estimate demanded by PF-318.