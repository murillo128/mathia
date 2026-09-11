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

PF-287 now removes one additional abstraction from that question. For arbitrary positive thresholds define the isometric unit-energy extension maps

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

The live theorem is therefore a quantitative essential-orthogonality theorem for the **unit-energy physical low/high extension ranges**, not a problem of estimating polar maps or strength populations separately.

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

Because PF-286 shows that both physical sides contain infinite heavy populations, mere rank truncation can no longer help. The relevant theorem must establish actual transversality/compactness of the low-fed and high-fed pant extension ranges.

## Why it may matter

PF-281 proves that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. PF-286 removes a potentially cheaper but misleading direction: there is no finite global strength exponent to estimate on either side, so further work on polynomial population counts cannot close the canonical endpoint.

PF-287 makes the surviving geometry directly testable. Fixed-threshold compactness is equivalent to compactness of the product of the two heavy-range projections. This is the classical essential-orthogonality condition for those physical extension ranges, while the weak-trace endpoint asks for a quantitative thresholded refinement. The project no longer needs to infer the angle indirectly from the polar decomposition: it can estimate the unshifted energy-normalized cross form itself.

A positive heavy-range theorem would show that the actual pant extension separates physical low and high directions strongly enough to overcome infinite saturated strength on both sides. A negative theorem can now be cheaper than a full endpoint asymptotic: one fixed pair of thresholds supporting arbitrarily large uniformly correlated unit-energy low/high families already makes the heavy projection product noncompact and, by PF-284, makes `T` noncompact.

## Decisive test

Work with the actual simultaneous pant-extension form and keep the physical PF-212 `P/H` projectors fixed before any simplifying coordinate change. Do **not** begin by constructing the polar maps `V_P,V_H`. For chosen fixed thresholds `\alpha,\beta`, use PF-287 to pass directly to unit-energy heavy inputs:

\[
u=|R_P|^{-1}x,
\qquad
v=|R_H|^{-1}y,
\]

with `x\in\operatorname{Ran}Q_P^\alpha`, `y\in\operatorname{Ran}Q_H^\beta`. Estimate the physical cross energy `k[u,v]` and therefore the product `\Pi_P^\alpha\Pi_H^\beta`.

The cheapest decisive negative test comes first. Try to construct, at one fixed positive pair `\alpha,\beta`, arbitrarily large orthonormal heavy families `x_1,\ldots,x_m` and `y_1,\ldots,y_m` such that the cross-energy matrices

\[
G_m(i,j)
=
k\!\left[|R_P|^{-1}x_i,\ |R_H|^{-1}y_j\right]
\]

have smallest singular value bounded below independently of `m`. PF-287 then gives a noncompact heavy projection product, and PF-284 gives noncompact `T`; the endpoint is genuinely dead.

If every fixed-threshold obstruction of this kind can be excluded, prove compactness by the orthonormal-sequence criterion from PF-287: every unit-energy orthonormal high-heavy extension family must have correlation with the entire low-heavy extension range tending to zero. Only after fixed-threshold compactness survives should effort move to the finer small-threshold count needed for weak trace class, preferably the PF-283 `O(\tau^{-1})` sufficient law or an asymmetric PF-284-compatible replacement.

PF-231's exactly separable untrimmed corridor may be used as a calibration, but it does not settle the physical projection product. Its hypercycle trim, physical projectors, neighboring-cell inhomogeneity, and global Schur completion remain possible sources of low/high range overlap.

Do not replace the physical angle by scalar same-mode reservoirs, raw high/high multiplicity alone, or a coordinate-mode angle that changes the fixed `P/H` split. PF-286 already uses those raw low/high estimates only to establish that the outer factors are heavy; the remaining question concerns their **common unit-energy range geometry**.

## Evidence boundary

PF-282 establishes the exact strength-angle factorization and fixed-heavy-sector ideal equivalence. PF-283 establishes one sufficient symmetric heavy-angle count. PF-284 establishes the reverse comparison and the corresponding necessary weighted budget. PF-285 establishes an abstract population-only sufficient route, while PF-286 proves that this route does not apply to the canonical physical strength factors because both are noncompact with infinite heavy populations.

PF-287 establishes that each thresholded heavy angle has exactly the same nonzero singular-value distribution as the product of the corresponding heavy extension-range projections, and gives the direct unshifted energy-normalized cross-form formula. The underlying two-subspace/projection geometry is classical; PF-287's contribution is the exact identification with the physical Prime-Flute endpoint object.

None of PF-286/PF-287 shows that the physical projection product is compact or noncompact, or that `T` does or does not belong to weak trace class. No physical principal-angle counting law has yet been proved, and no wave-operator, trace-formula, prime/clone separation, zeta-zero, or RH consequence follows.

## Research disposition

The clue remains `accepted`. The strength-population route is closed by PF-286, while PF-287 converts the surviving angular target into an explicit physical object: the product of the unit-energy heavy extension-range projections, equivalently the unshifted diagonal-energy-normalized low/high cross form. Test fixed-threshold essential orthogonality first using PF-287's finite-witness/orthonormal-sequence criteria; if it survives, measure the thresholded projection-product count using PF-283 as a clean sufficient endpoint and PF-284 as the genuine necessary boundary.