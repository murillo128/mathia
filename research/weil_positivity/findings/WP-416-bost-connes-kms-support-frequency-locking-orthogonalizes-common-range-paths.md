---
id: WP-416
title: Bost-Connes KMS support-frequency locking orthogonalizes common-range varying-support paths
branch: weil_positivity
status: supported
kind: bost-connes-kms-support-frequency-locking-obstruction
claim_strength: exact RH-independent obstruction for homogeneous common-generalized-range Hilbert-correspondence paths with canonical Bost-Connes divisibility source projections; KMS forces source mass ratios to equal path frequency ratios and annihilates every scalar Gram entry between distinct divisibility supports
created: 2026-09-23
related: [WP-216, WP-412, WP-415]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
  - O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics II, 2nd ed., Springer, 1997
  - E. C. Lance, Hilbert C*-Modules: A Toolkit for Operator Algebraists, London Mathematical Society Lecture Note Series 210, Cambridge University Press, 1995
  - M. Laca, S. Neshveyev and M. Trifkovic, Bost-Connes systems, Hecke algebras, and induction, J. Noncommut. Geom. 7 (2013), 525-546; arXiv:1010.4766
---

# WP-416 — Bost-Connes KMS support-frequency locking orthogonalizes common-range varying-support paths

## Claim

`WP-415` leaves source-forced varying support/incidence as a genuine escape from the common-support correspondence obstruction. For the most direct Bost--Connes varying-support realization, however, the KMS relation locks support variation to time frequency so rigidly that the scalar path Gram loses every cross-support entry.

Let `(A_BC,sigma)` be the rational Bost--Connes system, let `phi_beta` be any `KMS_beta` state with `beta>0`, and let `X` be a right Hilbert `A_BC`-module with a compatible strongly continuous dynamics `U_t`. Suppose finitely many path vectors `xi_a` are homogeneous,

\[
U_t\xi_a=e^{itd_a}\xi_a,
\tag{1}
\]

have canonical divisibility source projections

\[
p_a:=\langle\xi_a,\xi_a\rangle=E_{n_a}:=\mu_{n_a}\mu_{n_a}^*,
\tag{2}
\]

and share one generalized rank-one range projection

\[
q:=\theta_{\xi_a,\xi_a}\in\mathcal K(X).
\tag{3}
\]

Fix a reference path `0`. Then common range gives the coefficient partial isometries

\[
r_a:=\langle\xi_0,\xi_a\rangle,
\qquad
r_a^*r_a=E_{n_a},
\qquad
r_ar_a^*=E_{n_0},
\qquad
\xi_a=\xi_0r_a.
\tag{4}
\]

Compatibility with the dynamics makes `r_a` homogeneous of frequency `d_a-d_0`. The KMS boundary relation and the exact Bost--Connes masses `phi_beta(E_n)=n^{-beta}` then force

\[
\boxed{
d_a-d_0=\log\frac{n_0}{n_a}.}
\tag{5}
\]

Consequently

\[
\langle\xi_a,\xi_b\rangle=r_a^*r_b
\tag{6}
\]

has frequency

\[
(d_b-d_0)-(d_a-d_0)
=\log\frac{n_a}{n_b}.
\tag{7}
\]

Every KMS state is invariant under the time evolution, so a homogeneous element of nonzero frequency has zero expectation. Therefore

\[
\boxed{
n_a\ne n_b
\Longrightarrow
\phi_\beta(\langle\xi_a,\xi_b\rangle)=0.}
\tag{8}
\]

Thus the ordinary scalarized correspondence Gram is **block diagonal by the exact divisibility support `E_n`**. After scalar normalization of each diagonal block, distinct supports are orthogonal. Within one fixed `n`, the surviving degree-zero coefficients are corner-unitary correlations of the type already classified in `WP-415`.

There is a completely native realization showing that the theorem is not a formal empty case. Take the standard right module `X=A_BC` and

\[
\xi_n:=\mu_n^*.
\tag{9}
\]

Then

\[
\langle\xi_n,\xi_n\rangle=E_n,
\qquad
\theta_{\xi_n,\xi_n}=1
\tag{10}
\]

for every `n`, while `xi_n` has frequency `-log n`. Hence

\[
\phi_\beta(\langle\xi_m,\xi_n\rangle)
=\phi_\beta(\mu_m\mu_n^*)
=\delta_{mn}n^{-\beta}.
\tag{11}
\]

After replacing `xi_n` by `n^{beta/2}xi_n`, this canonical common-range varying-support family is exactly orthonormal in the KMS scalar product.

**Classification:** `EXACT-DERIVED + BOST-CONNES-KMS + NONFULL-CORRESPONDENCE + COMMON-RANGE-VARYING-SOURCE-SUPPORT + SUPPORT-FREQUENCY-LOCKING + DISTINCT-SUPPORT-KMS-ORTHOGONALITY + SOURCE-NATIVE-CONTROL + DECISIVE-NARROWING + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Common generalized range converts support variation into a homogeneous partial isometry

The common-range factorization is the exact `WP-415` identity. Because each `p_a=E_{n_a}` is a projection and `theta_{xi_a,xi_a}=q` is common,

\[
r_a^*r_a=E_{n_a},
\qquad
r_ar_a^*=E_{n_0}.
\tag{12}
\]

No fullness assumption is needed. The only extra input here is the equivariant structure. Compatibility of `U` with the coefficient dynamics says

\[
\langle U_tx,U_ty\rangle
=\sigma_t(\langle x,y\rangle).
\tag{13}
\]

Using (1),

\[
\begin{aligned}
\sigma_t(r_a)
&=\langle U_t\xi_0,U_t\xi_a\rangle\\
&=e^{it(d_a-d_0)}r_a.
\end{aligned}
\tag{14}
\]

So the same coefficient that implements Murray--von Neumann equivalence between the two source projections also carries a definite thermodynamic frequency. This is the point where support geometry and KMS dynamics cease to be independent choices.

## 2. KMS fixes that frequency from the source masses

For an analytic homogeneous element `r` of frequency `omega`,

\[
\sigma_{i\beta}(r)=e^{-\beta\omega}r.
\tag{15}
\]

The KMS relation gives

\[
\phi_\beta(rr^*)
=\phi_\beta(r^*\sigma_{i\beta}(r))
=e^{-\beta\omega}\phi_\beta(r^*r).
\tag{16}
\]

Apply this to `r_a`. Bost--Connes KMS states satisfy, independently of phase,

\[
\phi_\beta(E_n)=n^{-\beta}.
\tag{17}
\]

Therefore

\[
n_0^{-\beta}
=e^{-\beta(d_a-d_0)}n_a^{-\beta}.
\tag{18}
\]

Since `beta>0`, taking logarithms proves (5):

\[
d_a-d_0=\log(n_0/n_a).
\tag{19}
\]

This is an exact support-frequency law. Equal degree is now especially rigid: if `d_a=d_0`, then `n_a=n_0`. Thus the equal-degree/common-range regime of `WP-415` cannot simultaneously carry genuinely different canonical Bost--Connes divisibility supports.

The converse interpretation is also useful. Distinct divisibility supports are possible under common range, but they are forced into different time degrees. Support variation cannot be hidden inside a balanced coefficient sector.

## 3. Distinct supports become KMS-orthogonal

From `xi_a=xi_0r_a`,

\[
\langle\xi_a,\xi_b\rangle=r_a^*r_b.
\tag{20}
\]

Equation (14) shows that its frequency is

\[
\omega_{ab}
=(d_b-d_0)-(d_a-d_0)
=\log(n_a/n_b).
\tag{21}
\]

KMS invariance alone now supplies the second gate. If `sigma_t(x)=e^{it\omega}x` and `omega\ne0`, then

\[
\phi_\beta(x)
=e^{it\omega}\phi_\beta(x)
\quad\text{for every }t,
\tag{22}
\]

hence `phi_beta(x)=0`. Combining (21) and (22) proves (8).

If `n_a=n_b=n`, then `r_a^*r_b` has degree zero. Moreover it is a unitary of the corner `E_nA_BCE_n`:

\[
(r_a^*r_b)^*(r_a^*r_b)=E_n
=(r_a^*r_b)(r_a^*r_b)^*.
\tag{23}
\]

The KMS state restricts to a trace on the fixed-point algebra, so each equal-support block is exactly a tracial corner-unitary correlation Gram. Thus there are only two possibilities inside this class: distinct canonical supports are orthogonal, while equal supports fall back to the universal positive correlation geometry already exposed in `WP-415`.

This is stronger than applying `WP-412` in isolation. `WP-412` says a nonzero-frequency observable vanishes thermally; it does not say that changing a correspondence source support necessarily creates nonzero frequency. Equation (19) is the missing bridge: the Bost--Connes projection masses force precisely that implication.

## 4. The native adjoint-isometry family makes the collapse explicit

The standard module `A_BC` over itself already contains the required geometry. With `xi_n=mu_n^*`,

\[
\langle\xi_n,\xi_n\rangle
=\mu_n\mu_n^*=E_n.
\tag{24}
\]

For the standard module, `theta_{x,x}` is left multiplication by `xx^*`; therefore

\[
\theta_{\mu_n^*,\mu_n^*}
=L_{\mu_n^*\mu_n}
=L_1
\tag{25}
\]

for every `n`. All paths have the same generalized range even though their source projections run through the full divisibility family.

Their relative inner products are

\[
\langle\xi_m,\xi_n\rangle
=\mu_m\mu_n^*,
\tag{26}
\]

of frequency `log(m/n)`. KMS invariance kills (26) for `m\ne n`; for `m=n` it equals `E_n` and (17) gives the diagonal. This proves (11).

The comparison with `WP-216` is important. The critical GCD/Poisson Gram there comes from **conditioning the KMS GNS vector by the commuting projections `E_n` themselves**. Those projection vectors overlap through `E_mE_n=E_lcm(m,n)`. The present common-range path family uses the adjoint isometries `mu_n^*`; their common range forces support change to be carried by thermodynamic degree, and KMS scalarization makes distinct degrees orthogonal. Replacing projection conditioning by common-range partial-isometry paths therefore does not preserve the useful GCD overlaps; it erases them.

## 5. Matched control and prior-art boundary

The support-frequency identity is thermodynamic rather than uniquely arithmetic. In a finite-dimensional Gibbs system `B=M_d(C)` with dynamics `Ad(e^{itK})`, a matrix unit joining two energy eigenspaces is a homogeneous partial isometry. The KMS Gibbs weights of its source and range projections differ by exactly the Boltzmann factor of its frequency, reproducing (16). Thus one must not count KMS support-frequency locking itself as a new arithmetic sign mechanism.

What is Bost--Connes-specific is the exact source mass law (17). It converts the generic Boltzmann relation into the arithmetic logarithmic ratio (19), and hence converts distinct canonical divisibility labels into distinct time frequencies. The resulting orthogonalization is therefore an exact local obstruction for this Mathia route, not a new theorem about KMS systems in general.

All functional-analytic ingredients are standard. The KMS boundary relation and invariance are classical C-star dynamical-system theory; Lance supplies the Hilbert-module framework used in `WP-415`; Bost--Connes supplies the isometries, time evolution and KMS projection masses. Equivariant correspondences between Bost--Connes systems and induction of KMS states are also established in the literature, for example by Laca--Neshveyev--Trifkovic. A targeted literature audit found these ingredients and broader correspondence machinery, but no reason to treat the elementary support-frequency identity as novel operator algebra. The durable delta is only its application to the exact common-range varying-support escape left open by `WP-415`.

## 6. Boundary of the obstruction and consequence for `weil_positivity`

The hypotheses are load-bearing. The theorem requires `beta>0`, homogeneous path vectors, canonical source projections `E_n`, a common generalized range projection, and ordinary KMS scalarization of the module inner product. At `beta=0`, equation (18) no longer determines the frequency. A nonhomogeneous vector can mix several time degrees. If generalized ranges vary as well as sources, the partial-isometry factorization (4) need not hold. Operator-valued or non-KMS readouts can retain information that the scalar equilibrium state annihilates. Twisted/projective multiplication and genuinely non-Gram orientation-sensitive functionals are also outside the theorem.

Within the declared class, however, the varying-support escape is closed exactly. It cannot produce a nontrivial all-scale Gram by taking common-range homogeneous correspondence paths with source supports `E_n`: different `n` blocks are KMS-orthogonal, and each same-`n` block is again a universal tracial corner-unitary correlation Gram.

The surviving correspondence route is therefore narrower than the final boundary in `WP-415`. To use **source-forced varying support/incidence** nontrivially, a candidate must also vary generalized range/incidence, mix time degrees in a source-forced way, change the scalarization, or leave ordinary Gram geometry. It must still recover the finite prime-power coefficients, the Gamma and polar sectors, and a global sign theorem independently of RH or target-coded spectral data. Nothing here proves Weil positivity or RH; it removes one concrete native way in which varying support might otherwise have appeared to evade the existing passive path-Gram obstructions.