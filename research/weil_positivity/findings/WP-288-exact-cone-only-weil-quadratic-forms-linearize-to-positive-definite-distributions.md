---
id: WP-288
title: Exact cone-only Weil quadratic forms linearize to positive-definite distributions
branch: weil_positivity
status: supported
kind: cone-only-polarization-and-bochner-boundary
claim_strength: exact polarization and kernel-factorization theorem showing that a continuous translation-invariant cone functional matching Weil convolution squares is already the quadratic form of a unique positive-definite distribution; nonlinearity on the square cone is not a separate target category
created: 2026-09-13
related: [WP-005, WP-039, WP-269, WP-287]
prior_art:
  - André Weil, Sur les formules explicites de la théorie des nombres premiers (1952)
  - Bombieri's Weil quadratic-functional formulation
  - Schwartz kernel theorem and Bochner--Schwartz theorem
  - Jacques Dixmier and Paul Malliavin, Factorisations de fonctions et de vecteurs indéfiniment différentiables (1978)
  - Masatoshi Suzuki, screw-function realizations of the Weil quadratic form
---

# WP-288 — Exact cone-only Weil quadratic forms linearize to positive-definite distributions

## Claim

`WP-287` closes arbitrary nonlinear post-processing of the **scalar Arthur-height profile** whenever the result is still required to be a linear distribution in the test function. It deliberately leaves one apparent escape untouched: perhaps geometry should never produce a linear distribution at all. It could instead assign a nonnegative scalar directly to the Weil cone of convolution squares,

\[
q(f)\quad\text{for}\quad f\in C_c^\infty(\mathbb R),
\]

and try to identify only that scalar with

\[
q_W(f):=W(f*\widetilde f),
\qquad
\widetilde f(x):=\overline{f(-x)},
\tag{1}
\]

where `W` is the Weil explicit-formula distribution. Since Weil positivity is stated precisely on these squares, this seems at first to permit nonlinear geometric operations such as minima, determinants, nonlinear norms, entropies, or operator-level optimizations without ever recovering `W` as a linear object.

For an **exact** match on the full Weil test class, that apparent extra freedom disappears. Let

\[
V=C_c^\infty(\mathbb R).
\]

Suppose a scalar functional `q:V->R` is continuous and satisfies the identities forced by any Hermitian distributional square:

\[
q(\lambda f)=|\lambda|^2q(f),
\tag{2}
\]

\[
q(f+h)+q(f-h)=2q(f)+2q(h),
\tag{3}
\]

and logarithmic-translation invariance

\[
q(\tau_a f)=q(f),
\qquad
(\tau_a f)(x)=f(x-a).
\tag{4}
\]

Then complex polarization produces a continuous Hermitian sesquilinear form `B` on `V`. Translation invariance forces the Schwartz kernel of `B` to depend only on the difference variable. Consequently there is a **unique distribution** `T` on `R` such that

\[
\boxed{
B(f,h)=T(f*\widetilde h),
\qquad
q(f)=T(f*\widetilde f).
}
\tag{5}
\]

If in addition

\[
q(f)\ge0\qquad(f\in V),
\tag{6}
\]

then `T` is a positive-definite distribution. By Bochner--Schwartz, `T` is automatically tempered and its Fourier transform is a positive tempered measure `mu`; up to Fourier-normalization convention,

\[
\boxed{
q(f)=\int_{\mathbb R}|\widehat f(\xi)|^2\,d\mu(\xi).
}
\tag{7}
\]

Finally, if the proposed geometry claims the exact Weil identity

\[
q(f)=W(f*\widetilde f)
\qquad\text{for every }f\in V,
\tag{8}
\]

then polarization gives equality with `W` on every mixed convolution `f*\widetilde h`. The Dixmier--Malliavin factorization theorem says every element of `C_c^\infty(R)` is a finite sum of convolutions of two compactly supported smooth functions. Hence those mixed convolutions algebraically span the full test space, and therefore

\[
\boxed{T=W.}
\tag{9}
\]

So an exact cone-only route does **not** define a genuinely larger target category than the Weil distribution. Either its scalar output fails one of the Hilbertian identities (2)--(4), in which case it cannot equal the Weil quadratic form on the full test class, or it satisfies them and automatically linearizes to a unique translation-invariant positive-definite distribution. If it also matches the Weil squares, that distribution is exactly `W`.

This is not a proof that `W` is positive. If `q>=0` and (8) were established independently, (9) would simply be a proof of Weil positivity and hence of the corresponding RH criterion. The result is instead a **category closure**: the escape left open by `WP-287` cannot obtain its novelty merely from being nonlinear before evaluation on convolution squares.

**Classification:** `EXACT-DERIVED + CONE-ONLY-CATEGORY-CLOSURE + POLARIZATION + TRANSLATION-INVARIANT-KERNEL + DIXMIER-MALLIAVIN-FACTORISATION + BOCHNER-SCHWARTZ + ARITHMETIC-BLIND-STRUCTURE-THEOREM + DECISIVE-NARROWING + NO-NOVELTY-CLAIM-FOR-FUNCTIONAL-ANALYSIS + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The Weil square already forces quadratic identities before any positivity theorem

Let `L` be any Hermitian linear distribution on `V` and define

\[
q_L(f):=L(f*\widetilde f).
\tag{10}
\]

Then (2) is immediate. The parallelogram law follows from bilinearity of convolution:

\[
\begin{aligned}
&(f+h)*\widetilde{(f+h)}
+(f-h)*\widetilde{(f-h)}\\
&\qquad=2f*\widetilde f+2h*\widetilde h.
\end{aligned}
\tag{11}
\]

Translation invariance of the square is even more rigid. Since

\[
\widetilde{\tau_a f}=\tau_{-a}\widetilde f,
\]

one has

\[
(\tau_a f)*\widetilde{\tau_a f}
=f*\widetilde f.
\tag{12}
\]

Thus every exact realization of the Weil square satisfies (2)--(4) **regardless of how it was constructed**. These are target identities, not optional regularity assumptions suggested by a particular model.

This immediately rejects a broad family of superficially positive nonlinear statistics. For example, a determinant, entropy, `min`/`max`, or generic nonlinear norm of source data may be nonnegative and geometrically natural, but unless its dependence on `f` obeys both degree-two homogeneity and the exact parallelogram law, it is not the Weil quadratic form. A shift-sensitive functional likewise cannot equal (1), because simultaneous translation of the input leaves the convolution square unchanged before `W` is applied.

Continuity is not an independent escape when exact equality (8) is claimed: the Weil distribution is continuous on `C_c^\infty`, convolution is continuous on the test-function topology, and therefore `q_W` has the corresponding continuous quadratic-form dependence. A discontinuous proposed readout can only match `q_W` pointwise by hiding the target; continuity of the resulting scalar map is already inherited from (8).

## 2. Polarization removes the apparent nonlinear freedom on the square cone

Assume (2)--(3). The complex polarization identity defines

\[
\begin{aligned}
B(f,h)
:=\frac14\bigl(&q(f+h)-q(f-h)\\
&+i\,q(f+ih)-i\,q(f-ih)\bigr).
\end{aligned}
\tag{13}
\]

With the convention used here, `B` is linear in the first variable and conjugate-linear in the second. The standard Jordan--von Neumann polarization argument gives

\[
B(f,f)=q(f).
\tag{14}
\]

No positivity is required for this algebraic reconstruction; positivity only turns `B` into a positive semidefinite form. If `q` is continuous, the four evaluations in (13) show that `B` is continuous as a sesquilinear form.

Equation (4), combined with polarization, yields simultaneous-translation invariance:

\[
B(\tau_a f,\tau_a h)=B(f,h)
\qquad(a\in\mathbb R).
\tag{15}
\]

Thus a cone-only candidate satisfying the identities of the Weil square has already generated a conventional continuous Hermitian two-point pairing. Its apparent nonlinearity survives, at most, in an upstream geometric parametrization; it is gone at the scalar quadratic-form level.

An instructive allowed case is

\[
q(f)=\|\Phi(f)\|_{\mathcal H}^2
\tag{16}
\]

for some potentially nonlinear feature map `Phi`. If (2)--(3) hold for the scalar output, then `q` itself has the linear polarization (13), whether or not the chosen coordinates `Phi` are linear. One may therefore replace the scalar metric data by its canonical Hilbert/GNS realization. Nonlinearity of a feature parametrization is not, by itself, a new positivity mechanism.

## 3. Translation invariance forces the polarized kernel to be a convolution distribution

By the Schwartz kernel theorem, the continuous sesquilinear form `B` is represented by a distributional kernel on `R x R`. Simultaneous translation invariance (15) says that this kernel is invariant along the diagonal action

\[
(x,y)\mapsto(x+a,y+a).
\tag{17}
\]

The quotient coordinate for that action is the difference `x-y`. Equivalently, every such invariant kernel is the pullback of a unique distribution `T` on the difference line. In pairing form this is exactly

\[
B(f,h)=T(f*\widetilde h).
\tag{18}
\]

For an ordinary kernel `k(x-y)`, (18) is visible directly:

\[
\iint k(x-y)f(x)\overline{h(y)}\,dx\,dy
=\int k(t)(f*\widetilde h)(t)\,dt,
\tag{19}
\]

and the distributional statement is its standard kernel-theorem extension.

Setting `h=f` gives the second part of (5). Hence the three elementary square identities force the cone functional back into the same convolution-distribution category that the proposed cone-only escape was meant to avoid.

The translation condition is essential to this exact conclusion. Without it, polarization still produces a positive kernel on `R x R`, but that kernel need not descend to a one-variable convolution distribution. Such a shift-dependent kernel cannot equal the global Weil form (1) on the full test space, because (12) is an exact identity of the target.

## 4. Positivity brings the construction directly into Bochner--Schwartz form

Assume now (6). From (5),

\[
T(f*\widetilde f)\ge0
\qquad(f\in C_c^\infty(\mathbb R)).
\tag{20}
\]

This is precisely positive definiteness of the distribution `T`. The Bochner--Schwartz theorem then applies: every positive-definite distribution is tempered and is the Fourier transform of a positive tempered measure. Therefore there is a positive `mu` for which (7) holds.

The theorem is useful here because it separates **positivity as a scalar fact** from **arithmetic specificity**. Once a cone-only proposal passes (2)--(6), its sign has a completely classical Hilbertian spectral representation. That representation by itself knows nothing about rational primes, the Gamma factor, the polar terms, or the zeta functional equation. The hard Mathia question has merely moved to determining which `mu`, or equivalently which distribution `T`, is forced by the source geometry.

This also supplies a strong matched control. Replace zeta by any system producing a continuous translation-invariant Hilbertian quadratic functional on the same test group. The identical polarization and Bochner--Schwartz reduction applies. Therefore the reduction cannot count as evidence that the Riemann finite-prime and archimedean pieces have been assembled correctly; it is an arithmetic-blind structure theorem.

`WP-269` encountered Bochner--Schwartz from the opposite direction: a source-native critical Mangoldt time spectrum was too large to be the positive spectral measure of an ordinary positive-definite distribution. The present result does not reuse that growth obstruction. It says that **if** an exact cone-only Weil candidate lives continuously on the ordinary compact-test space and is positive, then positive-definite-distribution structure is unavoidable before any spectral-growth question is asked.

## 5. Equality on convolution squares already determines the full Weil distribution

The strongest possible cone-only objection is that perhaps one need not care about `T` away from the square cone. Equation (8) only compares scalar values on `f*widetilde f`; why should this identify a linear distribution on every test function?

First polarization removes the diagonal restriction. If both `q` and `q_W` agree on every diagonal square, then (13) gives

\[
B(f,h)=W(f*\widetilde h)
\qquad(f,h\in V).
\tag{21}
\]

By (18), this means

\[
T(f*\widetilde h)=W(f*\widetilde h)
\qquad(f,h\in V).
\tag{22}
\]

Now use the classical Dixmier--Malliavin factorization theorem for the Lie group `(R,+)`: every

\[
\varphi\in C_c^\infty(\mathbb R)
\]

can be written as a finite sum

\[
\varphi=\sum_{j=1}^N a_j*b_j,
\qquad a_j,b_j\in C_c^\infty(\mathbb R).
\tag{23}
\]

For each `b_j`, put `h_j=\widetilde{b_j}`. Then

\[
a_j*b_j=a_j*\widetilde{h_j}.
\tag{24}
\]

Applying (22) termwise to (23) proves

\[
T(\varphi)=W(\varphi)
\qquad(\varphi\in C_c^\infty(\mathbb R)),
\tag{25}
\]

which is (9).

This is the exact sense in which the square cone is not information-poor for a Hermitian distribution. Diagonal values determine mixed correlations by polarization, and mixed convolutions algebraically generate the test algebra. A purported alternative positive object that agrees with Weil on **all** convolution squares has therefore not avoided the Weil distribution; it has reconstructed it.

No novelty is claimed for either ingredient. Polarization is elementary functional analysis and Dixmier--Malliavin is the classical factorization theorem for smooth compactly supported functions on Lie groups. Their role here is adversarial: they close a specific logical gap explicitly left open in `WP-287`.

## 6. Aggressive falsification and exact boundary

**Can a positive nonlinear statistic evade the theorem by failing the parallelogram law?** Yes, mathematically, but then it does not equal the Weil quadratic form. Positivity of a different scalar statistic has no implication for Weil positivity without an additional comparison theorem strong enough to transfer sign.

**Can a construction be defined only on convolution squares rather than on all `f`?** A scalar rule indexed by `f` still has to be independent of irrelevant presentations and satisfy the identities inherited from (1) if exact equality is claimed. If it is defined only on a proper restricted family of tests, it proves only restricted positivity unless a separate density/extension theorem upgrades that family to the full Weil criterion.

**Can discontinuity evade Bochner--Schwartz?** Not for an exact realization of `q_W` on the ordinary test space, because exact equality imports the target continuity. A genuinely discontinuous positive form is a different generalized-function category and needs a new bridge showing that it recovers the canonical Weil criterion.

**Can a translation-noninvariant geometry still be useful?** Potentially as an upstream construction, but its final scalar form must shed that dependence if it is to equal (1). Equation (12) is exact and leaves no room for a residual base-point or time-origin dependence at the target level.

**Can a nonlinear operator construction before scalarization survive?** Yes. This is the important surviving boundary. An operator-level nonlinear operation may be the mechanism that source-forces a particular `T`; the theorem does not linearize the internal operators or prove that such a construction is impossible. It says only that once its exact scalar output is a Weil square, the output possesses the canonical linear distributional representation (5). The novelty must therefore lie in why the geometry forces that `T` and its sign, not in the claim that the output is “nonlinear on the cone.”

**Can a cone functional merely bound or dominate the Weil form?** The theorem does not rule this out. A source-positive `q` together with an independently proved inequality such as `q_W(f)>=F(q(f))` of the correct sign could be useful. But the sign-transfer inequality then becomes the substantive bridge and must survive the same source-forcing and matched-control audit. A numerical lower bound of the Maaß--Selberg type is not automatically a Weil-positive form; `WP-237` is the existing warning.

**Can the source impose extra linear constraints on tests?** The polarization argument works on any complex linear test subspace on which the identities and continuity hold. The stronger identification `T=W` on the full distribution requires enough mixed convolutions to generate the full target test algebra. If the construction lives only on a constrained subspace, it has established a restricted criterion unless an extension theorem closes that gap.

## 7. Prior-art and novelty audit

The target itself is classical. Weil's explicit-formula criterion is a positivity statement on convolution squares, and Bombieri's treatment makes the quadratic-functional viewpoint explicit. Suzuki's screw-function work provides a modern operator/distributional presentation of the same Weil quadratic form; the 2026 operator realization again treats the localized Weil form as the canonical object rather than introducing an unrelated nonlinear cone statistic.

The functional-analysis ingredients are also classical. The Schwartz kernel theorem identifies continuous bilinear/sesquilinear pairings with distribution kernels. Diagonal translation invariance descends such a kernel to the difference coordinate. Bochner--Schwartz characterizes positive-definite distributions as Fourier transforms of positive tempered measures. Dixmier and Malliavin, *Factorisations de fonctions et de vecteurs indéfiniment différentiables*, Bulletin des Sciences Mathématiques 102 (1978), 307--330, prove that every compactly supported smooth function on a Lie group is a finite sum of convolutions of two compactly supported smooth functions.

A bounded literature audit around Weil convolution-square positivity, Bochner--Schwartz, and Dixmier--Malliavin factorization found these classical components but no reason to regard their combination as a new theorem in harmonic analysis. No such novelty is claimed. The Mathia-specific delta is the **closure of the exact cone-only escape left explicit in `WP-287`**: once one asks a nonlinear geometric scalar to equal the Weil quadratic form on the full test cone, the target's own algebraic identities reconstruct a unique linear positive-definite distribution, and exact square agreement reconstructs `W` itself.

This result therefore does not compete with classical Weil positivity, Hilbert--Pólya, Connes/trace, Sonin localization, cohomological/intersection mechanisms, or screw-function realizations. It is a routing theorem for the current search: any successful nonlinear geometry must act upstream and explain the source-selected distribution or kernel; it cannot claim a distinct positivity mechanism merely because its last scalarization was written only on squares.

## Consequence for `weil_positivity`

The scalar escape map is now narrower than after `WP-287`.

- Nonlinear post-processing of the scalar Arthur-height profile that still returns a distribution collapses to a linear profile functional (`WP-287`).
- A supposedly more radical exact functional defined only through the Weil convolution-square cone must satisfy degree-two homogeneity, the parallelogram law, continuity, and translation invariance. Those identities polarize and descend to a unique convolution distribution (`WP-288`).
- If that cone functional is nonnegative, Bochner--Schwartz puts it in the ordinary positive-definite/Hilbert spectral category. If it matches the Weil squares exactly, Dixmier--Malliavin factorization forces the resulting distribution to be `W` itself.

Therefore the remaining nonlinear route is **not** “avoid linearity by reporting only positive scalars.” It is to find a Mathia-native finite--archimedean, operator, boundary, or cohomological construction whose own independent theorem forces a positive form and whose polarized convolution kernel can then be proved to equal the global Weil distribution without importing RH, zero locations, or a hand-picked regularizer. In that scenario the upstream geometry would be genuinely new even though its final quadratic form necessarily admits the classical linear representation established here.
