---
id: WP-266
title: Hamiltonian diagonal centering removes regulator ambiguity but critical rescaling is nonclosable
branch: weil_positivity
status: supported
kind: negative
claim_strength: exact regulator-covariant centering theorem with critical-scale nonclosability obstruction
created: 2026-09-12
refined: 2026-09-12
related: [WP-032, WP-263, WP-264, WP-265]
prior_art:
  - spectral conditional expectation onto a simple-spectrum Hamiltonian diagonal
  - connected/covariance subtraction of one-body diagonal terms
  - Sylvester inertia for complete-graph forms
  - closability of rank-one quadratic forms
---

# WP-266 — Hamiltonian diagonal centering removes regulator ambiguity but critical rescaling is nonclosable

## Claim

The regulator ambiguity exposed by `WP-265` can be removed **intrinsically inside the complete-incidence construction**, without choosing a finite subtraction constant, by using the source Hamiltonian itself to define the diagonal conditional expectation.

On the prime layer let

\[
H e_p=(\log p)e_p,
\qquad
P_p=|e_p\rangle\langle e_p|,
\]

and define

\[
\mathbb E_H(A):=\sum_p P_pAP_p.
\tag{1}
\]

Because the prime energies `log p` are simple, `E_H` is the spectral-diagonal expectation determined by `H`; it does not require an independently chosen coordinate basis. Applying the connected projection `I-E_H` to either the hard-cutoff or Gibbs complete-incidence Gram removes the divergent one-body term and its regulator-dependent finite remainder **exactly before taking any limit**.

For the hard cutoff,

\[
M_X=H_XD_{W,X}+a_Xa_X^*-2D_X,
\qquad
H_X=\sum_{q\le X}\frac1q,
\]

one has

\[
\boxed{
M_X-\mathbb E_H(M_X)=a_Xa_X^*-D_X.
}
\tag{2}
\]

For the Gibbs/Abel regulator of `WP-265`,

\[
M_\varepsilon=P(1+\varepsilon)D_W
+a_\varepsilon a_\varepsilon^*-2D_\varepsilon,
\]

one has identically

\[
\boxed{
M_\varepsilon-\mathbb E_H(M_\varepsilon)
=a_\varepsilon a_\varepsilon^*-D_\varepsilon.
}
\tag{3}
\]

Both centered families converge in trace norm to the same operator

\[
\boxed{K=aa^*-D,}
\qquad
d_p=\frac{\log p}{p^{3/2}},\quad a_p=\sqrt{d_p}.
\tag{4}
\]

Thus the `B_1` versus `B_1-gamma` finite-part mismatch of `WP-265` is not unavoidable: a source-native connected prescription cancels it algebraically rather than selecting one regulator's constant.

The gain is real but insufficient for Weil positivity. Every finite compression of `K` to at least two primes has exactly one positive direction and is strictly negative on the primitive hyperplane `ker a^*`; globally `K` is trace class with exactly one positive direction and infinite negative index. However this canonical connected form lives one factor `p^{-1}` below the critical Weil half-density. The source-canonical rescaling by `e^{H/2}` restores the critical prime amplitudes only at finite cutoff. In the infinite system it becomes a nonclosable rank-one form because

\[
\sum_p\frac{\log p}{\sqrt p}=\infty.
\]

So the complete-incidence geometry exhibits a sharp tradeoff: **Hamiltonian centering gives regulator independence and a genuine index-one sign theorem, while Hamiltonian rescaling back to the Weil critical scale destroys global closability.** No archimedean Gamma/polar term is generated, so this does not produce the sought global Weil-positive form.

**Classification:** `DERIVED`, `NEGATIVE/OBSTRUCTION WITH POSITIVE STRUCTURAL SUBRESULT`.

## Source-native diagonal expectation

Retain the notation of `WP-264` and `WP-265`,

\[
w_p=\frac{\log p}{\sqrt p},
\qquad
D_W=\operatorname{diag}(w_p),
\qquad
d_p=\frac{w_p}{p}=\frac{\log p}{p^{3/2}},
\qquad
a_p=\sqrt{d_p},
\qquad
D=\operatorname{diag}(d_p).
\tag{5}
\]

The logarithmic source Hamiltonian has distinct prime eigenvalues. Hence its spectral projections `P_p` are canonical and equation (1) is invariant under phase changes of the eigenvectors. On any finite prime compression it is the unique expectation that deletes off-diagonal matrix elements while preserving every spectral block of `H`.

This matters because the ambiguity in `WP-265` sits entirely in a diagonal one-body term proportional to `D_W`. Instead of subtracting an asymptotic scalar multiple of `D_W`, one can ask for the connected part of the full positive Gram relative to the source Hamiltonian.

This operation is not itself positivity preserving: `I-E_H` is a centering map, not a positive projection on operators. Any sign theorem for the centered object must therefore be proved independently rather than inherited from the original Gram positivity.

## Exact cancellation for the hard cutoff

Let `P_X` project onto primes `p<=X`, and abbreviate the compressed diagonal operators by `D_{W,X}` and `D_X`. `WP-264` gives

\[
M_X=H_XD_{W,X}+a_Xa_X^*-2D_X,
\qquad
H_X=\sum_{q\le X}\frac1q.
\tag{6}
\]

Since the diagonal of the rank-one operator is

\[
\mathbb E_H(a_Xa_X^*)=D_X,
\tag{7}
\]

we obtain

\[
\mathbb E_H(M_X)=H_XD_{W,X}-D_X.
\tag{8}
\]

Subtracting (8) from (6) proves the exact identity

\[
K_X^{\rm sharp}:=(I-\mathbb E_H)M_X
=a_Xa_X^*-D_X.
\tag{9}
\]

No Mertens asymptotic and no finite-part constant enters equation (9). In particular the `B_1D_W` remainder produced by leading-only sharp subtraction in `WP-265` has disappeared before `X` tends to infinity.

## Exact cancellation for the Gibbs regulator

For the Gibbs family of `WP-265`, set

\[
d_p^{(\varepsilon)}=w_pp^{-1-\varepsilon},
\qquad
a_p^{(\varepsilon)}=\sqrt{d_p^{(\varepsilon)}},
\qquad
D_\varepsilon=\operatorname{diag}(d_p^{(\varepsilon)}).
\tag{10}
\]

The exact Gram identity is

\[
M_\varepsilon=P(1+\varepsilon)D_W
+a_\varepsilon a_\varepsilon^*-2D_\varepsilon.
\tag{11}
\]

Again

\[
\mathbb E_H(a_\varepsilon a_\varepsilon^*)=D_\varepsilon,
\]

and hence

\[
\mathbb E_H(M_\varepsilon)
=P(1+\varepsilon)D_W-D_\varepsilon.
\tag{12}
\]

Therefore

\[
K_\varepsilon^{\rm Gibbs}:=(I-\mathbb E_H)M_\varepsilon
=a_\varepsilon a_\varepsilon^*-D_\varepsilon.
\tag{13}
\]

Equations (9) and (13) are the matched-regulator statement. Sharp and Gibbs regularization no longer differ by `gamma`; after source-Hamiltonian diagonal centering they are two approximations to the same connected operator.

## Common trace-norm limit

The critical connected weights are summable:

\[
\sum_p d_p
=\sum_p\frac{\log p}{p^{3/2}}<\infty.
\tag{14}
\]

Thus `a` lies in `ell^2` and `D` is trace class. For the hard cutoff,

\[
\|D_X-D\|_1\to0,
\qquad
\|a_X-a\|_2\to0.
\]

Using

\[
\|uu^*-vv^*\|_1
\le(\|u\|_2+\|v\|_2)\|u-v\|_2,
\tag{15}
\]

we get

\[
\|K_X^{\rm sharp}-K\|_1\to0.
\tag{16}
\]

For Gibbs damping, `0<=d_p^(epsilon)<=d_p`; dominated convergence gives `a_epsilon -> a` in `ell^2` and `D_epsilon -> D` in trace norm, so the same estimate yields

\[
\|K_\varepsilon^{\rm Gibbs}-K\|_1\to0.
\tag{17}
\]

The equality of the limits is therefore stronger than equality of asymptotic finite parts: the two source regulators converge to the same trace-class connected operator without evaluating either `B_1` or `gamma`.

## Exact index-one theorem for the connected form

For a finite set `F` of `m>=2` primes, let

\[
T_F=\operatorname{diag}(a_p)_{p\in F}.
\]

Because `D_F=T_F^2` and `a_Fa_F^*=T_FJ_mT_F`, where `J_m` is the all-ones matrix,

\[
K_F=T_F(J_m-I_m)T_F.
\tag{18}
\]

`T_F` is invertible. The complete-graph matrix `J_m-I_m` has one positive eigenvalue `m-1` and `m-1` negative eigenvalues `-1`. Sylvester inertia therefore gives

\[
\boxed{\operatorname{inertia}(K_F)=(1,m-1,0).}
\tag{19}
\]

There is also a canonical primitive sign statement. If `a^*x=0`, then

\[
\langle x,Kx\rangle
=-\langle x,Dx\rangle
=-\sum_p d_p|x_p|^2<0
\tag{20}
\]

for every nonzero `x` in `ker a^*`. Globally, `K=-D+aa^*` is a rank-one perturbation of a strictly negative compact operator, so it has at most one positive direction; any two-prime compression supplies one, hence it has exactly one. Equation (20) gives infinite negative index. Finally,

\[
\operatorname{tr}K=\|a\|_2^2-\operatorname{tr}D=0.
\tag{21}
\]

This is a genuine Hodge-like index theorem for the connected incidence remainder, but it occurs at the summable density `d_p`, not at the target critical scale.

## The critical rescaling obstruction

The source Hamiltonian itself provides the natural finite-dimensional map back toward the critical prime amplitudes:

\[
S=e^{H/2},
\qquad
Se_p=\sqrt p\,e_p.
\tag{22}
\]

On a finite prime set,

\[
\widetilde K_F:=S_FK_FS_F
=b_Fb_F^*-D_{W,F},
\qquad
b_p=\sqrt{w_p}
=\sqrt{\frac{\log p}{\sqrt p}}.
\tag{23}
\]

Because this is a congruence by an invertible positive diagonal matrix, every finite `\widetilde K_F` still has inertia `(1,m-1,0)`. Thus the sign theorem survives every finite critical rescaling.

The infinite limit fails for a different reason. The critical amplitude vector is not square summable:

\[
\|b\|_2^2
=\sum_p w_p
=\sum_p\frac{\log p}{\sqrt p}
=\infty.
\tag{24}
\]

On the finite-support core `c_00`, the rank-one part is the quadratic form

\[
q_b(x)=\left|\sum_p b_px_p\right|^2.
\tag{25}
\]

A rank-one form of this type is closable on `ell^2` exactly when its coefficient vector defines a continuous functional, equivalently when `b` belongs to `ell^2`. Equation (24) therefore makes `q_b` nonclosable. The diagonal form from `D_W` is bounded because `w_p` is bounded and tends to zero. Consequently, if

\[
\widetilde q(x)=q_b(x)-\langle x,D_Wx\rangle
\tag{26}
\]

were closable, adding the bounded diagonal form would make `q_b` closable, a contradiction. Hence the source-canonical critical rescaling is nonclosable globally.

This is the same analytic mechanism isolated abstractly for critical rank-one Gram forms in corrected `WP-032`, now arising as the precise cost of restoring the Weil half-density after the regulator-independent connected centering.

## Aggressive falsification and controls

The construction would be noncanonical if the diagonal expectation depended on an arbitrary basis. Here it does not: the source Hamiltonian has simple prime spectrum, so its spectral projections determine `E_H`. A degeneracy or an additional internal multiplicity would weaken that conclusion and would require a further canonical blockwise rule.

The regulator claim would fail if sharp and Gibbs centering left different scalar remainders. Equations (9) and (13) show instead that both divergent bath scalars are removed identically at finite regulator. The common limit would fail if `sum d_p` diverged; equation (14) is precisely what makes the connected remainder trace class.

The critical obstruction would fail if `b` were square summable. It is not. Conversely, the obstruction is only to this source-canonical linear rescaling of the connected form; it does **not** prove that every nonlinear quotient, boundary completion, or genuinely global finite-archimedean construction must fail.

Nor can the missing critical one-body information simply be restored by declaring a finite multiple `lambda D_W` after centering. That is exactly a new diagonal datum. Unless a separate geometric theorem fixes `lambda` before comparison with Weil, the scheme parameter rejected in `WP-264` and `WP-265` has merely been reintroduced in another notation.

Most importantly, `I-E_H` is not a positive map on forms. The nonnegativity/negativity information in (19)-(20) comes from the complete-graph congruence and primitive restriction, not from the positivity of the original Gram. This prevents the connected subtraction itself from being mistaken for the desired independent Weil positivity theorem.

## Prior-art and novelty audit

Conditional expectations onto the diagonal algebra of a simple-spectrum self-adjoint operator are standard operator theory. Connected/covariance subtraction is likewise standard, as are the spectrum of `J_m-I_m`, Sylvester inertia, and the criterion that a rank-one functional on `ell^2` is continuous/closable only when its coefficient vector lies in `ell^2`. No novelty is claimed for any of those ingredients.

The branch-specific result is their exact interaction with the Mathia critical complete-incidence Gram: the Hamiltonian spectral expectation cancels **both** the sharp `B_1` and Gibbs `B_1-gamma` finite parts before asymptotics, the resulting source-defined connected operator has an exact index-one primitive theorem, and the Hamiltonian rescaling that restores the critical prime amplitudes is then globally nonclosable. A focused prior-art search found classical instances of each ingredient but no result identifying this regulator-removal/critical-closability tradeoff for the present prime-incidence construction.

This does not bypass classical Weil positivity, Hilbert-Polya, Connes/trace, Frobenius/cohomology, or intersection-form approaches. It is instead a branch-local structural diagnosis of why the most canonical connected version of the current Mathia incidence mechanism becomes well defined only below the critical scale.

## Falsification target

The obstruction is defeated by a Mathia-native completion that retains the regulator-independent connected cancellation while supplying the critical one-body and archimedean/polar data through a **closable global object**, with its normalization fixed by geometry rather than by comparison to the Weil formula. A boundary or cohomological sector would have to do more than add a scalar diagonal counterterm: it must explain why the critical rescaling is globally admissible or replace it by a different canonical local-to-global mechanism.

A particularly sharp test is whether such a completion can reproduce the finite-compression index-one theorem of (19), survive both hard and Gibbs regulators without a scheme constant, and generate the Gamma/polar contribution from the same structural law. Failure of any one of those tests returns the route to the earlier regulator or critical-closability obstructions.

## Consequence

`WP-265` left open the possibility that the finite-part ambiguity was an artifact of asking each regulator to perform its own scalar subtraction. The source Hamiltonian does provide a stronger answer: take the connected part relative to its spectral diagonal, and the ambiguity disappears exactly.

But this does not move the construction across the critical barrier. The resulting canonical form is trace class and has the desired one-positive-direction/primitive-negative geometry only at `d_p=(log p)/p^{3/2}`. The canonical Hamiltonian congruence that moves it to the critical `w_p=(log p)/sqrt p` scale preserves every finite-dimensional inertia statement while destroying global closability. The missing structure is therefore no longer merely a regulator constant; it is a genuinely global mechanism capable of reconciling **regulator invariance, critical scaling, closability, and the archimedean completion in one theorem**.