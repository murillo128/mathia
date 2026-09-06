---
id: CLUE-analytic-frontier-positive-cone-domination-uniform-complex-tube
type: research-clue
status: proposed
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-030-montgomery-taylor-extremizer-forces-palm-zero-set-rigidity.md
  - research/analytic_frontier/findings/ANF-034-central-notch-perturbation-gives-an-explicit-finite-real-separator-ray.md
  - research/analytic_frontier/findings/ANF-081-two-level-clipping-closes-the-full-real-multiplicity-gate.md
  - research/analytic_frontier/findings/ANF-082-central-notch-real-certificate-opens-a-p-minus-quarter-complex-tube.md
---

# Can positive-cone domination remove the pair-count loss from the complex tube?

## Observation

ANF-082 bounds the absolute structure-factor perturbation by an expression of order `p h^2`, then compares it with an affine norm floor of order `sqrt(p)`. This produces a protected height of order `p^(-1/4)`. Its stated next test is to remove that loss without restricting multiplicity or horizontal geometry.

The central-notch construction has stronger structure than an arbitrary nonnegative spectrum. By ANF-030 and ANF-034, with `J_0=J_MT` and `R_0=widehat J_0`,

\[
R_0(t)\ge0\quad(t\in\mathbb R),\qquad
0\le\phi_\eta\le J_0,\qquad
(1-s)J_0\le J_s=J_0-s\phi_\eta\le J_0.
\]

Thus the unperturbed Gram matrix is entrywise nonnegative as well as positive semidefinite, and the two spectral norms are uniformly comparable. The candidate below uses both facts before applying the final triangle inequality. It does not assume that `widehat J_s` is pointwise nonnegative.

## Research question

For every nonempty finite conjugation-invariant multiset `W`, let `X` be its real-part collapse, preserving all multiplicities, and put `h=max |Im z|`. Define

\[
S_Z(\alpha)=\sum_{z\in Z}e^{-2\pi i\alpha z},\qquad
\|f\|_s^2=\int_{-1}^1J_s(\alpha)|f(\alpha)|^2\,d\alpha.
\]

Can the following relative estimate be established with no dependence on cardinality, pair count, separation, or occupancy?

\[
\boxed{
\|S_W-S_X\|_s\le
\frac{\cosh(2\pi h)-1}{\sqrt{1-s}}\,\|S_X\|_s.
}
\tag{A}
\]

The proposed derivation is supplied below for independent audit. If it survives, splice (A) into ANF-081 to replace the shrinking ANF-082 tube by one fixed positive-width tube for the same fixed notch and a strictly improving affine normalization.

## Why it may matter

This would remove the entire apparent escape through an increasing number of pairs approaching the real axis. Unlike a separated-frequency or bounded-occupancy repair, it would cover coincident centers, arbitrarily close horizontal sites, arbitrary real occupancies, and repeated nonreal pairs. It is an enlargement of the auxiliary complex certificate, not a zero-free strip for zeta and not a complete complex certificate.

## Decisive test

Group the entries of `W` by their distinct real parts `x_i`. Let `r_i` be the number of real entries at `x_i`, and let the nonreal pairs at that center have heights `y_ij>0` and positive integer multiplicities `n_ij`. The collapsed multiplicity is

\[
m_i=r_i+2\sum_jn_{ij}.
\]

For each integer `k>=1`, set

\[
a_{i,k}=2\sum_jn_{ij}y_{ij}^{2k},\qquad
T_k(\alpha)=\sum_i a_{i,k}e^{-2\pi i\alpha x_i}.
\]

Then `0<=a_{i,k}<=h^(2k)m_i`. In the unperturbed norm, entrywise nonnegativity gives the candidate's key comparison directly:

\[
\begin{aligned}
\|T_k\|_0^2
&=\sum_{i,l}a_{i,k}a_{l,k}R_0(x_i-x_l)\\
&\le h^{4k}\sum_{i,l}m_im_lR_0(x_i-x_l)
=h^{4k}\|S_X\|_0^2.
\end{aligned}
\tag{B}
\]

This compares positive coefficient vectors in a fixed Gram form. It does not compare the pointwise absolute values of exponential sums, and it does not discard phases by replacing the norm of `S_X` with its coefficient sum.

The exact conjugate-pair expansion is

\[
D:=S_W-S_X
=\sum_{k\ge1}\frac{(2\pi)^{2k}}{(2k)!}\alpha^{2k}T_k(\alpha).
\tag{C}
\]

For finite `W` and finite `h`, the series converges uniformly on `[-1,1]`. Multiplication by `alpha^(2k)` is a contraction there. Applying (B), `J_s<=J_0`, and then `(1-s)J_0<=J_s` should give

\[
\begin{aligned}
\|D\|_s
&\le\sum_{k\ge1}\frac{(2\pi)^{2k}}{(2k)!}
       \|\alpha^{2k}T_k\|_s\\
&\le\sum_{k\ge1}\frac{(2\pi)^{2k}}{(2k)!}\|T_k\|_0\\
&\le[\cosh(2\pi h)-1]\|S_X\|_0\\
&\le\frac{\cosh(2\pi h)-1}{\sqrt{1-s}}\|S_X\|_s.
\end{aligned}
\tag{D}
\]

Next preserve the exact affine objective. Write `q=q_s` for ANF-081's fixed real-certificate constant, `rho=C(J_s)/C_MT<q`, and choose any fixed `q_*` with `rho<q_*<q`. Define

\[
\kappa_*=1-\sqrt{q_*/q},\qquad
\boxed{
h_*:=\frac{1}{2\pi}\operatorname{arcosh}
\left(1+\sqrt{1-s}\,\kappa_*\right)>0.
}
\tag{E}
\]

Here `sigma(W)` counts simple real sites, as in ANF-082, not all simple complex sites. Real-part collapse gives `sigma(X)<=sigma(W)` and preserves `N`. Consequently, for `h<=h_*`, the proposed splice is

\[
\begin{aligned}
E_{F_s}(W)
&\ge(1-\kappa_*)^2E_{F_s}(X)\\
&\ge q_*\bigl(2N-\sigma(W)\bigr),\qquad
\frac{C(J_s)}{q_*}<C_{\rm MT}.
\end{aligned}
\tag{F}
\]

The sign gate `kappa_*<1` must be retained before squaring the reverse triangle bound. Unlike ANF-082's `h_p`, (E) contains no `p` or `N`.

Audit (B)--(F), especially the coefficientwise comparison in the **unperturbed** Gram form, the factor of two per pair in (C), the direction of norm comparison, and the simple-real-site convention. Accept this route only after checking those steps and the unchanged ANF-081 hypotheses; otherwise give a counterexample under those exact hypotheses rather than under a weaker spectral class.

A useful negative control prevents a false generalization of (B). For `J_0=1/2` on `[-1,1]`, its transform is `sinc(2t)` and is negative at `t=3/4`. At sites `0,3/4`, coefficient vectors `a=(10,0)<=m=(10,1)` have energies `E(a)=100` and `E(m)=101-40/(3pi)<100`. Spectral nonnegativity/positive definiteness alone therefore does not justify the monotone-coefficient step. The actual Montgomery--Taylor kernel avoids this failure because ANF-030 gives its spatial transform as an explicit square.

## Evidence boundary

This is a proposed analytical handoff, not a canonical finding or an independently accepted proof. The relative lemma is elementary and the preceding derivation is intended to make validation or refutation inexpensive. Its application inherits ANF-081's all-real certificate and strict objective gap; neither that dependency chain nor a numerical value for a certified `h_*` is established anew here. Finite numerical checks cannot replace the all-configuration argument.

No theorem-level novelty is claimed for entrywise-nonnegative Gram forms, coefficient domination, or Hilbert-norm perturbation. Primary background is Carneiro--Chandee--Littmann--Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, arXiv:1406.5462, and Buescu--Paixao, *Positive-definiteness and integral representations for special functions*, arXiv:1801.09537. These anchor the kernel/Fourier-Laplace framework, not the specific uniform affine splice (B)--(F); no RH-conditional zero statistic from those works is imported.

The construction retains `s<1`, compact spectral support, positive multiplicities, and conjugation symmetry. It does not prove monotonicity of energy under arbitrary vertical motion, cover heights above `h_*`, eliminate a genuinely positive-height obstruction, improve an unconditional zero proportion, or resolve RH. Success would specifically show that the `p^(-1/4)` loss was unnecessary for this fixed comparable-notch family.
