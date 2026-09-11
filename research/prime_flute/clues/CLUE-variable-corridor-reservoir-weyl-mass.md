---
id: CLUE-prime-flute-variable-corridor-reservoir-weyl-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain.md
  - research/prime_flute/findings/PF-280-one-sided-frequency-decoupled-schur-transfer-is-reservoir-stable.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle.md
  - research/prime_flute/findings/PF-283-heavy-angle-counting-criterion-for-weak-trace-endpoint.md
  - research/prime_flute/findings/PF-284-two-sided-heavy-angle-counting-sandwich.md
  - research/prime_flute/findings/PF-285-complementary-weak-schatten-extension-strengths-close-the-weak-trace-endpoint-without-angle-decay.md
  - research/prime_flute/findings/PF-286-physical-extension-strengths-are-not-compact.md
  - research/prime_flute/findings/PF-287-heavy-extension-angle-is-exactly-a-product-of-heavy-range-projections.md
  - research/prime_flute/findings/PF-288-diverging-local-form-witnesses-force-heavy-angle-noncompactness.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does the physical heavy-sector extension angle close the weak-trace endpoint?

## Observation

PF-279 shows that a variable scalar reservoir can erase a favorable isolated cut scale, while PF-280/PF-281 separate that raw obstruction from the physically mixed low/high block. PF-282 gives the exact factorization

\[
T=F_P\Gamma_{PF}F_H,
\qquad
F_P=f(K_P^{1/2}),\quad F_H=f(K_H^{1/2}),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

where the outer factors record extension strength and `\Gamma_{PF}` records the relative angle of the low-fed and high-fed extension ranges.

PF-283 supplies a convenient sufficient endpoint criterion. With

\[
Q_P^\tau=\mathbf1_{[\tau,1]}(F_P),
\qquad
Q_H^\tau=\mathbf1_{[\tau,1]}(F_H),
\qquad
\Gamma_{PF,\tau}=Q_P^\tau\Gamma_{PF}Q_H^\tau,
\]

it is enough that

\[
\sup_{0<\tau<\tau_0}
\tau\,N_{\Gamma_{PF,\tau}}(2\tau)<\infty.
\]

PF-284 shows that this particular `O(\tau^{-1})` count is not necessary: weak trace class itself only forces the weaker symmetric envelope `N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-3})`. PF-285 then identifies a second sufficient mechanism: if `F_P,F_H` have complementary finite weak-Schatten population exponents, the two strength factors alone can pay the weak-trace budget.

PF-286 performs that strength census for the **canonical physical split** and closes the population-only route negatively. PF-216 forces the low diagonal energy to be unbounded on the tangentially constant physical-low module tail, so

\[
\operatorname{rank}Q_P^\tau=\infty
\qquad(0<\tau<1).
\]

PF-227 forces the physical high strength to be noncompact, so there is `\tau_H>0` with

\[
\operatorname{rank}Q_H^\tau=\infty
\qquad(0<\tau\le\tau_H).
\]

Thus no finite `p_P,p_H` exist for PF-285's population-only criterion. The surviving endpoint question is genuinely angular: can `\Gamma_{PF}` turn two infinite-dimensional heavy sectors into a compact/weak-trace cross operator with the required thresholded singular-value decay?

PF-287 removes one abstraction from that question. For arbitrary positive thresholds define the isometric unit-energy extension maps

\[
W_P^\alpha=V_PQ_P^\alpha,
\qquad
W_H^\beta=V_HQ_H^\beta
\]

and let `\Pi_P^\alpha,\Pi_H^\beta` be the orthogonal projections onto their closed ranges in the common energy space. Then

\[
\Gamma_{PF,\alpha,\beta}=(W_P^\alpha)^*W_H^\beta
\]

and, exactly,

\[
N_{\Gamma_{PF,\alpha,\beta}}(a)
=
N_{\Pi_P^\alpha\Pi_H^\beta}(a).
\]

Moreover the same operator can be computed directly from the physical precision form. With `\rho(\alpha)=\alpha/\sqrt{1-\alpha^2}`, the heavy threshold is `Q_P^\alpha=\mathbf1_{[\rho(\alpha),\infty)}(|R_P|)`, and for heavy `x,y`,

\[
\langle x,\Gamma_{PF,\alpha,\beta}y\rangle
=
k\!\left[|R_P|^{-1}x,\ |R_H|^{-1}y\right].
\]

PF-288 now makes the cheapest **negative** test local. Because the simultaneous PF precision is block-Jacobi, pairwise separated local low/high form vectors are exactly energy-orthogonal across different windows. If both diagonal Rayleigh quotients diverge and their same-window normalized mixed correlation stays bounded below, their unit-energy images asymptotically enter every fixed heavy spectral sector. A sparse-subsequence argument then gives an infinite-dimensional heavy cross-Gram operator bounded below, so `T` is noncompact. No explicit construction of global heavy spectral vectors is needed.

PF-216 already provides the diverging local physical-low Rayleigh sequence. Therefore the current local falsifier has only two genuinely new geometric obligations: construct a pairwise separated **physical-high** local family with diverging diagonal Rayleigh quotient, and decide whether its normalized mixed form correlation with the PF-216 low channel vanishes.

## Research question

For the actual simultaneous one-cusp-pant extension, what is the singular-value distribution of

\[
\Pi_P^\alpha\Pi_H^\beta,
\]

or equivalently

\[
\Gamma_{PF,\alpha,\beta}
=Q_P^\alpha\Gamma_{PF}Q_H^\beta,
\]

on the physical heavy-strength sectors?

The strongest simple target remains the PF-283 symmetric law

\[
N_{\Pi_P^\tau\Pi_H^\tau}(2\tau)=O(\tau^{-1}),
\]

which is sufficient for `T\in\mathcal S_{1,\infty}`. Failure of that law is not endpoint failure. PF-284/PF-287 leave an intermediate regime, so the more flexible target is an asymmetric threshold budget: find physically adapted `\alpha_k,\beta_k,a_k` for which

\[
\alpha_k\beta_k a_k\,
N_{\Pi_P^{\alpha_k}\Pi_H^{\beta_k}}(a_k)
\]

stays uniformly bounded, or prove that the corresponding necessary budget diverges along a canonical sequence.

Because PF-286 shows that both physical sides contain infinite heavy populations, mere rank truncation can no longer help. The relevant positive theorem must establish actual transversality/compactness of the low-fed and high-fed pant extension ranges. For a negative theorem, PF-288 says to test the local form first rather than diagonalizing the heavy spectral projections.

## Why it may matter

PF-281 proves that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. PF-286 removes a potentially cheaper but misleading direction: there is no finite global strength exponent to estimate on either side, so further work on polynomial population counts cannot close the canonical endpoint.

PF-287 makes the surviving geometry directly testable. Fixed-threshold compactness is equivalent to compactness of the product of the two heavy-range projections. This is the classical essential-orthogonality condition for those physical extension ranges, while the weak-trace endpoint asks for a quantitative thresholded refinement. The project no longer needs to infer the angle indirectly from the polar decomposition: it can estimate the unshifted energy-normalized cross form itself.

PF-288 makes the fixed-threshold **falsification** side substantially cheaper. The spectral projection may remain global; one can work on repeated local pant windows. Diverging diagonal form energy automatically pushes the corresponding unit-energy vectors into each fixed heavy sector, and block-Jacobi locality keeps distinct windows orthogonal. Thus a persistent local normalized low/high correlation would already kill compactness before any small-threshold counting asymptotic is attempted.

A positive heavy-range theorem would show that the actual pant extension separates physical low and high directions strongly enough to overcome infinite saturated strength on both sides. A negative theorem can now be obtained from one local channel pattern repeated sparsely at infinity if it carries the PF-288 high-energy correlation.

## Decisive test

Start with the PF-288 local falsifier, because it avoids global spectral-vector construction. Take a sparse sequence of pant/module windows so different windows are separated by more than the block-Jacobi interaction range. On the low side use the explicit PF-216 tangentially constant module vector `\ell_n`, for which

\[
\frac{k[\ell_n]}{\|\ell_n\|^2}
\gtrsim\frac{P_n}{\log P_n}\to\infty.
\]

On the same windows construct a physical-high vector `h_n` (or uniformly finite-dimensional physical-high family) and test the two quantities

\[
\frac{k[h_n]}{\|h_n\|^2},
\qquad
\frac{|k[\ell_n,h_n]|}
{\sqrt{k[\ell_n]k[h_n]}}.
\]

If the first tends to infinity while the second stays bounded below along a subsequence, PF-288 implies that every fixed positive heavy-angle compression is noncompact, hence `T` is noncompact and the weak-trace endpoint fails. This is now the cheapest decisive negative test.

A large raw high/high pant crossing is not enough. PF-227 supplies many raw physical-high channels but does not establish either the local high-Rayleigh divergence needed by PF-288 or a persistent **low/high** normalized cross correlation. Those must be computed for the actual fixed physical `P/H` split.

If the PF-288 local obstruction is absent, return to PF-287's positive compactness criterion: every unit-energy orthonormal high-heavy extension family must have correlation with the entire low-heavy extension range tending to zero. Only after fixed-threshold compactness survives should effort move to the finer small-threshold count needed for weak trace class, preferably the PF-283 `O(\tau^{-1})` sufficient law or an asymmetric PF-284-compatible replacement.

PF-231's exactly separable untrimmed corridor may be used as a calibration, but it does not settle the physical projection product. Its hypercycle trim, physical projectors, neighboring-cell inhomogeneity, and global Schur completion remain possible sources of low/high range overlap. In particular, separability may make the leading local model low/high orthogonal, so any persistent PF-288 correlation has to be derived rather than inferred from raw corridor multiplicity.

Do not replace the physical angle by scalar same-mode reservoirs, raw high/high multiplicity alone, or a coordinate-mode angle that changes the fixed `P/H` split. PF-286 already uses those raw low/high estimates only to establish that the outer factors are heavy; the remaining question concerns their **common unit-energy range geometry**.

## Evidence boundary

PF-282 establishes the exact strength-angle factorization and fixed-heavy-sector ideal equivalence. PF-283 establishes one sufficient symmetric heavy-angle count. PF-284 establishes the reverse comparison and the corresponding necessary weighted budget. PF-285 establishes an abstract population-only sufficient route, while PF-286 proves that this route does not apply to the canonical physical strength factors because both are noncompact with infinite heavy populations.

PF-287 establishes that each thresholded heavy angle has exactly the same nonzero singular-value distribution as the product of the corresponding heavy extension-range projections, and gives the direct unshifted energy-normalized cross-form formula. PF-288 establishes a sufficient **local-form noncompactness certificate**: pairwise separated local low/high vectors with divergent diagonal Rayleigh quotients and persistent normalized mixed correlation force noncompactness at every fixed heavy threshold. The underlying compactness, spectral-projection, and two-subspace geometry is classical; PF-288's useful specialization is the bridge from exact PF block-Jacobi locality and local Rayleigh growth to the PF-287 heavy witness.

PF-216 supplies only the low-side divergent local Rayleigh channel. Neither PF-227 nor PF-286 proves the remaining high-side local divergence plus mixed low/high correlation. Therefore PF-288 does not yet decide whether the physical projection product is compact or noncompact, or whether `T` does or does not belong to weak trace class. No physical principal-angle counting law has yet been proved, and no wave-operator, trace-formula, prime/clone separation, zeta-zero, or RH consequence follows.

## Research disposition

The clue remains `accepted`. The strength-population route is closed by PF-286, PF-287 identifies the surviving object as the product of unit-energy heavy extension-range projections, and PF-288 localizes the cheapest noncompactness test. First test whether the PF-216 low channel can be paired with a separated physical-high local family having diverging diagonal energy and nonvanishing normalized mixed correlation. If that obstruction fails, attack fixed-threshold essential orthogonality via PF-287; only after compactness survives should the research spend effort on the PF-283/PF-284 quantitative threshold counts.