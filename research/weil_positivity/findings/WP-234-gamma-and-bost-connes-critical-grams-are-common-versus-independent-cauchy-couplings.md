# WP-234 — Gamma and Bost–Connes critical Grams are common-versus-independent Cauchy couplings

**Status:** `EXACT-DERIVED + BOCHNER-POSITIVE + CAUCHY-COUPLING-NONUNIQUENESS + MATCHED-PRIME-RAY-CONTROLS + MIXED-PRIME-SOURCE-SELECTION-OBSTRUCTION + FREE-MONOID-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-233` identifies two independently selected positive kernels that agree exactly on every one-prime ray but differ on mixed-prime incomparable states. The mismatch has a sharper structural interpretation: the two kernels are the characteristic kernels of **the same Cauchy one-coordinate law with two different cross-prime dependence structures**. The critical Bost–Connes Gram corresponds to independent Cauchy coordinates, while the one-dimensional Gamma/log kernel corresponds to one common latent Cauchy coordinate shared by every prime.

This yields a continuum of positive matched controls with exactly the same critical half-density on every prime ray. Therefore prime-local half-density together with positive-definiteness cannot select the global mixed-prime geometry. Any surviving Mathia route must derive the cross-prime coupling itself from the source algebra/geometry before the final sign is read out; otherwise the global completion remains underdetermined even before the Weil defect and archimedean/polar terms are addressed.

## 1. The two kernels are two Cauchy dependence structures

For a finite set of primes `P`, write the logarithmic valuation vector

\[
x_P(n):=(v_p(n)\log p)_{p\in P}\in\mathbb R^P,
\]

and suppose `m,n` have no prime factors outside `P`. Put

\[
\Delta_p:=x_p(m)-x_p(n)
=(v_p(m)-v_p(n))\log p.
\tag{1}
\]

The critical Bost–Connes Gram from `WP-216` is

\[
\boxed{
G_{\rm BC}(m,n)
=\frac{\gcd(m,n)}{\sqrt{mn}}
=\exp\!\left(-\frac12\sum_{p\in P}|\Delta_p|\right).
}
\tag{2}
\]

The one-dimensional archimedean/log kernel isolated in `WP-233` is

\[
\boxed{
K_\infty(m,n)
=\exp\!\left(-\frac12|\log m-\log n|\right)
=\exp\!\left(-\frac12\left|\sum_{p\in P}\Delta_p\right|\right).
}
\tag{3}
\]

Let `C` denote a centered Cauchy random variable of scale `1/2`, so its characteristic function is

\[
\mathbb E[e^{itC}]=e^{-|t|/2}.
\tag{4}
\]

If `(C_p)_{p\in P}` are independent copies of `C`, then independence and (4) give

\[
\begin{aligned}
\mathbb E\exp\!\left(i\sum_{p\in P}C_p\Delta_p\right)
&=\prod_{p\in P}e^{-|\Delta_p|/2}\\
&=G_{\rm BC}(m,n).
\end{aligned}
\tag{5}
\]

If instead the same variable `C` is used in every coordinate, then

\[
\mathbb E\exp\!\left(iC\sum_{p\in P}\Delta_p\right)
=e^{-|\sum_p\Delta_p|/2}
=K_\infty(m,n).
\tag{6}
\]

Thus the metric mismatch in `WP-233` is equivalently a dependence mismatch:

\[
\boxed{
G_{\rm BC}=\text{independent Cauchy prime coordinates},
\qquad
K_\infty=\text{one common Cauchy coordinate}.
}
\tag{7}
\]

Both are positive definite for the same elementary reason: they are expectations of rank-one character kernels. No RH assumption, zero data, or target-fitted sign enters this positivity.

## 2. Prime-ray data fix only the marginals, not the coupling

The interpretation above immediately produces a much larger matched-control class. Let `\pi` be any probability law on `\mathbb R^P` whose coordinate marginals are centered Cauchy laws of scale `1/2`. Define

\[
K_\pi(m,n)
:=\int_{\mathbb R^P}
\exp\!\left(i\sum_{p\in P}\xi_p\Delta_p\right)
\,d\pi(\xi).
\tag{8}
\]

For any finitely supported complex coefficients `a_j` and integers `n_j`,

\[
\begin{aligned}
\sum_{j,k}\overline{a_j}a_kK_\pi(n_j,n_k)
&=\int
\left|\sum_j a_j
 e^{i\langle\xi,x_P(n_j)\rangle}\right|^2
 d\pi(\xi)\\
&\ge0.
\end{aligned}
\tag{9}
\]

Hence every `K_\pi` is a normalized positive-definite Gram kernel.

Now restrict to a single prime ray, say `m=p^a`, `n=p^b`. All coordinates except `p` disappear from (8), so only the `p` marginal of `\pi` remains:

\[
\boxed{
K_\pi(p^a,p^b)
=e^{-\frac12|a-b|\log p}
=p^{-|a-b|/2}.
}
\tag{10}
\]

Therefore **every coupling with the same Cauchy marginals has exactly the same critical Bost–Connes/Gamma half-density on every prime ray**. The local source data see the marginals; mixed-prime matrix elements see the dependence law.

This is not merely an existence statement. Let `\pi_{\rm ind}` be the independent product law and `\pi_{\rm diag}` the law of `(C,C,\ldots,C)`. For `0\le\theta\le1`,

\[
\pi_\theta=(1-\theta)\pi_{\rm ind}+\theta\pi_{\rm diag}
\tag{11}
\]

has the same Cauchy marginals, and its kernel is

\[
\boxed{
K_\theta
=(1-\theta)G_{\rm BC}+\theta K_\infty.
}
\tag{12}
\]

Thus there is already an explicit continuum of normalized positive kernels that are indistinguishable by all one-prime restrictions and by the critical `p^{-k/2}` profile.

## 3. Mixed-prime states are exactly where the source-selection problem lives

For incomparable integers, (2) and (3) differ because opposite valuation changes can cancel in the scalar logarithm but not in the divisor `ell^1` norm. For distinct primes `p<q`,

\[
G_{\rm BC}(p,q)=\frac1{\sqrt{pq}},
\qquad
K_\infty(p,q)=\sqrt{\frac pq}.
\tag{13}
\]

The entire family (12) therefore has

\[
K_\theta(p,q)
=(1-\theta)\frac1{\sqrt{pq}}
+\theta\sqrt{\frac pq},
\tag{14}
\]

while its restrictions to the `p` and `q` rays remain exactly fixed. This is a clean matched control: local critical behavior and positivity are held constant while only the cross-prime dependence is changed.

The conclusion is stronger than the metric mismatch of `WP-233`. A derivation that knows only

1. the source energies `k\log p`,
2. the critical half-density `p^{-k/2}`, and
3. that the global object should be a normalized positive Gram kernel,

cannot determine whether mixed-prime directions should be independent, perfectly correlated through one real coordinate, or any of the other admissible dependence structures in (8). A global positivity mechanism based only on these ingredients is therefore underdetermined before any Weil-form comparison is made.

The Bost–Connes algebra itself *does* select the product/divisor geometry appearing in (2). The point is not that `G_BC` is arbitrary. The point is that **prime-ray positivity is not what selects it**. Any proposed Mathia bridge must use the genuinely global source structure that enforces that product law, and must then show why the same global structure also produces the archimedean and polar terms with the required sign.

## 4. Entrywise domination is not a positive correction

Triangle inequality gives

\[
\left|\sum_p\Delta_p\right|
\le\sum_p|\Delta_p|,
\]

so

\[
K_\infty(m,n)\ge G_{\rm BC}(m,n)
\tag{15}
\]

entrywise. It is tempting to interpret `K_infty-G_BC` as a positive archimedean correction. That is false.

Both kernels have diagonal exactly one. If `K_\infty-G_{\rm BC}` were positive semidefinite, it would be a positive semidefinite kernel with zero diagonal. Cauchy–Schwarz for positive semidefinite matrices would then force every off-diagonal entry to vanish. But (13) gives a nonzero off-diagonal difference. Hence

\[
\boxed{K_\infty-G_{\rm BC}\not\succeq0.}
\tag{16}
\]

The reverse difference is also not positive semidefinite. On the two-point set `{p,q}`, either nonzero difference has a matrix with zero diagonal and eigenvalues of opposite sign.

This is consistent with the branch's earlier equal-diagonal/passive-positive rigidity results; it is not claimed as a separate general theorem. Here it serves as an exact control showing that passing from independent to common Cauchy coupling is **not** a passive positive finite–archimedean completion, despite the pointwise ordering (15).

## 5. The ambiguity survives generalized-prime/free-monoid controls

Nothing in the coupling argument depends on unique arithmetic properties of the rational primes. Let a free commutative monoid have generators `g_j` with arbitrary positive weights `w_j`, and write

\[
x_j(\alpha)=\alpha_jw_j.
\tag{17}
\]

Independent Cauchy coordinates produce

\[
K_{\rm ind}(\alpha,\beta)
=\exp\!\left(-\frac12\sum_j
|\alpha_j-\beta_j|w_j\right),
\tag{18}
\]

while one common Cauchy coordinate produces

\[
K_{\rm common}(\alpha,\beta)
=\exp\!\left(-\frac12\left|
\sum_j(\alpha_j-\beta_j)w_j\right|\right).
\tag{19}
\]

Both have identical generator-ray restrictions `exp[-|a-b|w_j/2]`, and convex mixtures again give a continuum of positive matched controls. Therefore the nonuniqueness mechanism is universal to a weighted free-monoid valuation geometry. It cannot by itself distinguish `\mathbb Q` or encode the Riemann Gamma/polar completion.

This generalized control is decisive for scope: the new structure is useful as a **falsifier/source-selection test**, not as a candidate proof of RH.

## 6. Aggressive falsification and exact scope

**Does the Cauchy representation itself yield the Weil form?** No. It represents positive Gram kernels. `WP-216` and `WP-232` already show that the exact finite Weil ray is an indefinite defect of the positive Bost–Connes/Poisson Gram. The Cauchy representation does not alter that sign.

**Does choosing the common latent variable solve the archimedean completion?** No. `WP-233` already proves that `K_infty` disagrees with the Bost–Connes Gram on incomparable mixed-prime states, and (16) shows that the discrepancy is not a passive positive correction.

**Could positivity choose the independent coupling uniquely?** No. Equations (8)--(12) give explicit positive counterexamples with identical one-prime data. Additional source structure is necessary.

**Could one choose a coupling because it makes the final Weil form positive?** That would reverse the required logic. The research mandate requires positivity to follow independently from geometry, not a dependence law selected by the target RH-equivalent sign. A target-selected copula/coupling would be another hand-picked kernel.

**Do arbitrary Cauchy-marginal couplings define one consistent infinite-prime process?** This finding does not need that claim. Equation (8) is stated for each finite prime set, which is enough for finite matched controls; the explicit independent, common-latent, and convex-mixture families are themselves consistent for all finite restrictions and hence supply global counterexamples to uniqueness.

**Does this prove that no source-forced cross-prime coupling can work?** No. It identifies exactly what such a mechanism must add. A source algebra, cohomological incidence, noncommuting correspondence, boundary condition, or other intrinsic construction could canonically select a particular dependence structure. The finding only rules out treating prime-local critical positivity as sufficient evidence that the global completion has been forced.

## 7. Prior art and novelty boundary

No historical novelty is claimed for characteristic functions, Bochner's theorem, the centered Cauchy characteristic function `exp(-gamma |t|)`, multivariate characteristic functions, coupling probability measures with fixed marginals, Laplacian kernels, or positivity of GCD matrices. These are classical ingredients.

For external checks, the bounded audit used the Encyclopedia of Mathematics entries on characteristic functions/Bochner's theorem and Fourier–Stieltjes transforms, which state that characteristic functions are positive definite and characterize normalized continuous positive-definite functions. MathWorld's Cauchy-distribution entry records the characteristic function `exp(i m t-Gamma |t|/2)`, giving (4) at the stated normalization. Guillot and Wu, *Total nonnegativity of GCD matrices and kernels*, arXiv:1901.01947, explicitly recalls the classical positive-definiteness of GCD matrices and studies stronger total-nonnegativity properties. Searches combining Bost–Connes, normalized GCD kernels, Cauchy characteristic representations, and common-versus-independent dependence did not surface a source asserting the Mathia-specific identification below; absence from a bounded search is not a novelty proof.

The internal novelty boundary is narrower. `WP-216` already derives the normalized critical Bost–Connes GCD Gram. `WP-233` already proves that this Gram equals the exponential of divisor `ell^1` distance while the Gamma/log kernel is the exponential of scalar logarithmic distance, and that the two coincide on divisibility chains but not on mixed-prime incomparable states.

The durable new delta is the exact probabilistic/Bochner classification of that mismatch: **the two canonical kernels are independent-versus-common Cauchy dependence structures with identical prime-coordinate marginals, and varying only the dependence law produces a continuum of normalized positive matched controls with every prime-ray restriction fixed.** This turns the pairwise mismatch from `WP-233` into a source-selection obstruction for the entire active global-completion strategy.

Useful external references:

- Encyclopedia of Mathematics, “Characteristic function”: https://encyclopediaofmath.org/wiki/Characteristic_function
- Encyclopedia of Mathematics, “Fourier-Stieltjes transform”: https://encyclopediaofmath.org/wiki/Fourier-Stieltjes_transform
- Wolfram MathWorld, “Cauchy Distribution”: https://mathworld.wolfram.com/CauchyDistribution.html
- D. Guillot and J. Wu, “Total nonnegativity of GCD matrices and kernels”, arXiv:1901.01947: https://arxiv.org/abs/1901.01947

## 8. Consequence for the live research frontier

`WP-233` showed that the Riemann-Gamma adjacent jump density and the Bost–Connes critical ray share the same exact half-density. `WP-234` now shows why that match cannot be promoted to a global positive geometry by locality plus positivity alone.

The one-prime data determine the Cauchy marginals. They do **not** determine the joint law. Independent coordinates recover the Bost–Connes divisor geometry; one common coordinate recovers the scalar archimedean log geometry; and the convex family (12) supplies infinitely many positive intermediate controls without changing a single prime ray.

Therefore a viable continuation of the accepted Bost–Connes/global-completion clue must satisfy a stricter gate:

\[
\boxed{
\text{derive the cross-prime dependence from the source}
\quad\textit{before}\quad
\text{using positivity or matching the Weil sign}.
}
\tag{20}
\]

Only after that source-selection step is forced does it make sense to ask whether the same construction intrinsically creates the Gamma/polar counterterms and whether an independent geometric theorem makes the final Weil quadratic form nonnegative. A construction that merely chooses among the admissible couplings because one has favorable target behavior is not evidence for the research mandate.

## Dependencies

- `research/weil_positivity/findings/WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md`
- `research/weil_positivity/findings/WP-232-bost-connes-poisson-whitening-is-an-indefinite-jacobi-normal-form.md`
- `research/weil_positivity/findings/WP-233-adjacent-gamma-jump-density-samples-bost-connes-weil-ray-but-positive-completion-is-divergent.md`
- `research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md`
- `research/weil_positivity/SOURCES.md`

## Bottom line

The exact prime-ray agreement found in `WP-233` fixes only a one-dimensional Cauchy marginal. The Bost–Connes critical Gram and the Gamma/log Gram arise from two different source-globalizations of that marginal — independent prime coordinates versus one shared coordinate — and a continuum of other positive couplings has the same local data. Consequently, **critical half-density plus positivity cannot force the global mixed-prime geometry**. The surviving problem is not to find another positive kernel with the right prime rays, but to derive a unique cross-prime coupling from Mathia's intrinsic global structure and then obtain the full Weil finite/archimedean/polar decomposition and its sign from that same construction.