---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-416-weighted-vdc-filters-cannot-remove-diagonal.md
  - research/mobius_cancellation/findings/MC-417-fejer-riesz-closes-positive-finite-band-kernels.md
  - research/mobius_cancellation/findings/MC-456-triply-well-factorable-dispersion-provides-a-factor-specific-quotient-breaking-template.md
  - research/mobius_cancellation/findings/MC-458-staged-factor-conditioning-exposes-residual-divisor-sum-kernel.md
  - research/mobius_cancellation/findings/MC-459-staged-residual-energy-is-controlled-by-the-normalized-shift.md
  - research/mobius_cancellation/findings/MC-460-one-sided-residual-conditioning-promotes-reduced-divisor-to-reciprocal-source-shift.md
  - research/mobius_cancellation/findings/MC-461-residual-source-starts-decompose-into-bounded-anchor-slices.md
  - research/mobius_cancellation/findings/MC-463-gcd-sector-normalization-collapses-to-common-anchor-quotient.md
  - research/mobius_cancellation/findings/MC-464-normalized-gcd-gate-makes-favorable-shifts-totient-sparse.md
  - research/mobius_cancellation/findings/MC-465-fejer-weighted-favorable-gcd-classes-remain-sparse.md
  - research/mobius_cancellation/findings/MC-466-original-shift-fejer-envelope-cancels-outer-gcd-advantage.md
  - research/mobius_cancellation/findings/MC-467-residual-scale-interval-shrinkage-cancels-support-growth.md
  - research/mobius_cancellation/findings/MC-468-root-scale-support-makes-well-factorability-vacuous.md
  - research/mobius_cancellation/findings/MC-469-empty-vector-sieve-component-survives-small-outer-cell-pruning.md
  - research/mobius_cancellation/findings/MC-470-empty-vector-residual-is-a-nonnegative-sieve-boundary-count.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The surviving factor-specific route starts from the exact staging

\[
w(m)=\sum_{r\mid m}\alpha_r B_\beta(m/r),
\qquad
B_\beta(y)=\sum_{s\mid y}\beta_s,
\]

which keeps one factor block in the source progression while the complementary block remains as an unexpanded divisor-sum amplitude. `MC-459`--`MC-467` progressively remove apparent free resources from this representation: the true residual diagonal is only subpower; compatible gcd sectors collapse to one normalized anchor modulus; favorable normalized-gcd classes are sparse even under Fejér weighting; large outer gcd gives no net advantage; and support growth is coupled to shrinking source-interval length. In the nonendpoint bulk, the dyadic shell geometry obeys

\[
A_XH_X\le 4\frac{N}{RT},
\qquad
M_X<\frac{2N}{\eta pR},
\]

with `R=[r,r']` and `T=r'/(h,r')`.

`MC-468` shows that generic well-factorability supplies no missing anti-concentration theorem. `MC-469` then opens a concrete modified linear-sieve decomposition. Its empty-vector component has

\[
\alpha=\delta_1,
\qquad
\beta=\lambda^{(0)},
\qquad
R=T=1,
\]

so no growing outer-support suppression applies. Nonempty rough-block components still have a genuine product-of-bins support filter and should be pruned before any expensive dispersion estimate.

`MC-470` now identifies the base residual exactly. If `Q=D^\varepsilon`, `z=Q^\varepsilon`, and

\[
m_z(y)=\prod_{\substack{q<z\\q\mid y}}q,
\]

then

\[
B_{\lambda^{(0)}}(y)
=\sum_{\substack{d\mid m_z(y)\\d\in\mathcal D^+(Q)}}\mu(d)
\in\mathbf Z_{\ge0}.
\]

It is a nonnegative upper-sieve boundary count, not a hidden signed oscillatory amplitude. It equals `1` on genuinely `z`-rough values and its non-rough positive part is supported only on high-rank small-prime configurations: if `m_z(y)>1` and `\varepsilon(\omega(m_z(y))+2)\le1`, then the amplitude vanishes exactly. This rank gate is structural, not a density or power-saving estimate.

The live coefficient problem is therefore sharper. The empty-vector branch cannot gain from sign cancellation internal to `B_{\lambda^{(0)}}`; the nonempty branch can still gain only after exact support pruning; and a cross-component route must retain the signed finite decomposition before triangle inequalities or positive closure.

## Research question

Can the staged decomposition produce a strict conductor-power gain through one of the mechanisms that survives `MC-470`?

For the **empty-vector base component**, the target is now the joint estimate

\[
\sum_{s_0}\widetilde\beta(s_0)
\sum_{j\in J_{s_0}}
\chi(j+U_{s_0})
\overline{\chi(j+U_{s_0}-D_{s_0})}
B_{\lambda^{(0)}}(C_{s_0}+s_0j),
\]

where the residual factor is a positive `z`-rough-plus-boundary weight. Can the translated-character phase cancel against this weight on the exact affine trajectories strongly enough to give a conductor-power saving after the near-complete endpoint and weighted outer participation are charged? Alternatively, can cancellation in the signed outer coefficients `\widetilde\beta(s_0)` survive long enough to supply the missing gain?

For **nonempty rough-block components**, after discarding every bin tuple whose product cannot enter the `MC-467` small-outer region, does the surviving normalized signed mass remain large and structured enough for factor-specific dispersion to matter?

A third channel is **cross-component interference**. It is admissible only if the complete signed finite decomposition is carried through an oscillatory transform before componentwise absolute values or positive quadratic closure.

## Why it may matter

The route has moved from a generic appeal to factorability to a narrowly defined arithmetic interaction. Large gcd, extra factor labels, Fejér concentration, independent support/interval tuning, generic well-factorability, and blanket support pruning have all been priced or ruled out as standalone resources. `MC-470` also removes internal residual coefficient signs from the base component.

This makes the next estimate discriminating. If the positive upper-sieve boundary weight can be shown to obey the same source-frame tariff even after its exact affine arithmetic is retained, while the nonempty components are support-pruned or individually too expensive, the componentwise architecture is close to closure. A positive result would instead have to exhibit a genuine character-versus-sieve interaction, outer signed cancellation, or explicit cross-component interference that is absent from the already-classified positive source-frame model.

## Decisive test

Keep the exact `MC-463` variable `s_0`, the standard Fejér shift weight, and the `MC-467` shell geometry. Do not expand the residual into the old product variables before the decisive estimate.

For the **base component**, set `R=T=1` from the outset. Split

\[
B_{\lambda^{(0)}}(y)
=
\mathbf 1_{(y,P(z))=1}+E(y),
\qquad E(y)\ge0,
\]

where `E(y)` is the high-rank first-exit boundary count supplied by `MC-470`. Estimate the rough part and boundary part separately on the actual affine values `y=C_{s_0}+s_0j`. The rank condition on `E` may be used only after proving a quantitative count or weighted estimate for those affine high-rank values; it is not itself a sparsity saving. Keep exact `(U,D)` collision aggregation and isolate `L_X>(1-\eta)p` instead of absorbing the near-complete endpoint into a bulk estimate.

The base channel advances only if the character-weight interaction or the retained outer signs yield a strict conductor-power gain after shell summation, Fejér weights, endpoints, coefficient normalization, and source depth. A proof based on alternating signs inside `\lambda^{(0)}` is killed by `MC-470`, because those signs have already recombined pointwise into a nonnegative count.

For **nonempty components**, use the exact lower support `a>D_1\cdots D_r` to remove impossible bin tuples before estimating anything else. Price only the surviving tuples with their actual scalar normalization/sign and the Fejér participation factor. Continue to residual collisions only if their total contribution is quantitatively non-negligible.

For **cross-component interference**, retain the signed finite sum through the proposed transform and exhibit an explicit cross term whose cancellation remains after normalization and source-length costs. Separate positive energies followed by a later appeal to cancellation do not qualify.

## Evidence boundary

`MC-467` is a shellwise geometric restriction, not a bound for the full staged kernel. `MC-468` rules out generic anti-concentration from well-factorability. `MC-469` shows that one concrete upper-sieve decomposition contains an unavoidable base component at `R=T=1`. `MC-470` further proves that this base residual is a nonnegative boundary count and gives an exact low-rank vanishing criterion.

None of these findings proves that the high-rank boundary correction is sparse on the relevant affine trajectories, that the positive rough part has a favorable character correlation, that the outer coefficients cancel sufficiently, or that cross-component interference survives. No conductor-power gain, Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-470`**. The empty-vector residual is no longer an unspecified signed divisor amplitude: its internal coefficient signs cannot be the missing oscillatory resource. The immediate base test is now character cancellation against a positive `z`-rough plus high-rank boundary weight on the exact affine trajectories, with outer `s_0` signs and the near-complete endpoint accounted for separately. Nonempty rough-block pruning and pre-positive cross-component interference remain distinct surviving channels.