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
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The surviving factor-specific route starts from the exact `MC-458` staging

\[
w(m)=\sum_{r\mid m}\alpha_r B_\beta(m/r),
\qquad
B_\beta(y)=\sum_{s\mid y}\beta_s,
\]

which keeps one well-factorable block inside an unexpanded divisor-sum amplitude while the other block determines the source progression. `MC-459` shows that the true positive residual diagonal is only subpower, and `MC-460` shows that one-sided residual conditioning promotes the reduced divisor into a reciprocal source shift while retaining the second residual amplitude on an aligned affine trajectory.

The source geometry is now tightly classified. `MC-461` decomposes the starts into arithmetic anchor slices and gives the exact prime-conductor fixed-anchor shift second moment; `MC-463` then removes the artificial residual gcd-sector multiplicity. For a fixed outer pair and compatible original shift,

\[
T=\frac{r'}{(h,r')}
\]

is the common normalized anchor modulus, and all compatible residual sectors aggregate into one reduced variable `s_0` with coefficient `\widetilde\beta(s_0)`.

`MC-464`--`MC-466` price the outer shift supply. Favorable normalized-gcd classes are totient-sparse, remain sparse under the standard Fejér weights, and the apparent benefit of concentrating outer coefficients on large `(r,r')` cancels when measured in the original shift envelope. For any shift-independent nonnegative outer coefficient mass, the favorable Fejér fraction is controlled by the scale `M^2/r'`; large pair gcd alone is not a resource.

`MC-467` now prices the remaining apparent freedom in the threshold `M`. The exact normalized parametrization advances the original integer `n` by

\[
[r,r']s_0
\]

when the source index advances by one. Hence on a dyadic reduced-divisor shell `X<=s_0<2X`, one fixed anchor has at most `1+X/T` source points while each source interval has length at most `1+N/([r,r']X)`. In the only regime where the fixed-anchor moment can give a nontrivial gain, their product is bounded by

\[
A_XH_X\le 4\frac{N}{[r,r']T}.
\]

Thus residual support and interval length are not independent. Away from the near-complete endpoint `L_X\approx p`, the shell threshold obeys

\[
M_X<\frac{2N}{\eta p[r,r']}
\qquad
\text{when }L_X\le(1-\eta)p.
\]

Combining this with `MC-466`, a nonvanishing favorable Fejér fraction at large `r'` requires, at exponent scale,

\[
N\gtrsim_\eta p[r,r']\sqrt{r'},
\]

and therefore necessarily

\[
r'\lesssim_\eta (N/p)^{2/3}.
\]

So the generic large-threshold escape is closed in the bulk: one cannot combine the large residual support belonging to one scale with the long interval belonging to another. The live outer region has been compressed to genuinely small `r'`/small lcm cells and the near-complete endpoint.

## Research question

Inside the cells that survive `MC-467`, can the exact staged family

\[
\sum_{s_0}\widetilde\beta(s_0)
\sum_{j\in J_{s_0}}
\chi(j+U_{s_0})
\overline{\chi(j+U_{s_0}-D_{s_0})}
\overline{B_\beta(C_{s_0}+r_1s_0j)}
\]

be estimated before the second residual expansion and before componentwise positive closure with a strict conductor-power gain that survives the **actual well-factorable coefficient mass of the small outer cells**, the near-complete endpoint, weighted participation of `\widetilde\beta`, and the aligned residual amplitude?

The bulk support/interval geometry is no longer a live degree of freedom. A positive factor-specific result must now use either arithmetic concentration in the small-outer-scale region, a legitimate endpoint mechanism, or cancellation that depends essentially on the retained residual coefficient/amplitude. A source-only conductor-reduction branch remains logically separate and must still pay the full product-level summation cost.

## Why it may matter

The staged route has reached a much sharper bottleneck than generic “use factorability before Cauchy.” The outer source-frame tariff can no longer be beaten by internal-factor multiplicity, large gcds, Fejér short-shift bias, arbitrary shift-independent outer coefficient concentration, or by treating support size and interval length as independent tunable parameters. What remains is an arithmetic question about where the **actual coefficient mass** sits and whether the unexpanded aligned amplitude supplies information that the bare source-frame model cannot see.

A negative result showing that the surviving small-`r'`/small-lcm and endpoint cells have insufficient total coefficient mass would close the most plausible bare outer/support escape. A positive result would have to exhibit a quantitative weighted dispersion mechanism inside those cells rather than recover one of the already-neutralized resources.

## Decisive test

Start from the exact `MC-463` aggregated variable `s_0` and split it dyadically. For every fixed outer pair and original Fejér shift, set

\[
R=[r,r'],
\qquad
T=\frac{r'}{(h,r')}.
\]

Use `MC-467` immediately. Discard as non-gainful the one-point anchor regime `X<T` and the one-point interval regime `RX>N`. In every nonendpoint bulk shell impose the coefficient-independent resource bounds

\[
A_XH_X\le 4\frac{N}{RT},
\qquad
M_X<\frac{2N}{\eta pR}.
\]

Then sum the **actual outer well-factorable coefficient envelope**, with the standard Fejér shift weight still present, only over cells for which the resulting `MC-466` factor

\[
\min\!\left(1,\frac{M_X(M_X+1)}{r'}\right)
\]

is not negligible. The first decisive question is whether the total mass of those small-`r'`/small-`R` cells is already too small to support a conductor-power gain. Treat `L_X>(1-\eta)p` as a separate endpoint family rather than hiding it in the bulk threshold.

If a significant family survives, aggregate `\widetilde\beta(s_0)` by exact `(U,D)` collisions, compute its weighted participation rather than support cardinality, and keep

\[
B_\beta(C_{s_0}+r_1s_0j)
\]

inside the estimate. The branch advances only if a fixed-anchor/dispersion or completion estimate retains a strict conductor-power gain after coefficient mass, variable lengths, endpoint cells, aligned amplitude, outer summation, exceptional terms, and source depth are all charged.

Do not reopen large-gcd coefficient concentration or a global `S\times L` threshold as independent resources; `MC-466` and `MC-467` close those mechanisms for the standard Fejér architecture. If a different positive finite-band filter is proposed, its favorable-set concentration must be priced together with its diagonal/DC cost against `MC-416`--`MC-417`.

## Evidence boundary

`MC-467` is an exact shellwise obstruction, not an estimate of the full staged kernel. It does **not** prove that the small-`r'`/small-lcm outer cells have negligible well-factorable coefficient mass, control the endpoint `L_X\approx p`, establish useful weighted participation of `\widetilde\beta`, or estimate the joint character/divisor-sum amplitude. It also does not show that every non-Fejér or shift-adaptive architecture obeys the same favorable-set envelope.

The literature-backed `MC-456` comparison shows that factor-specific dispersion can genuinely work in other arithmetic geometries; the present obstruction is specific to the exact fixed-character staged source frame and standard Fejér outer architecture derived here. No local gain has yet been propagated to a Möbius bound or an RH-relevant global estimate.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-467`**. The bulk pair-dependent-threshold loophole is closed after the true residual interval geometry is retained: source support grows like `X/T` while interval length shrinks like `N/(RX)`, leaving the scale-invariant resource `N/(RT)`.

The live factor-specific work is now restricted to: (i) pricing the actual well-factorable coefficient mass on the small-`r'`/small-lcm cells allowed by `MC-467`; (ii) a separately isolated near-complete endpoint; and, only if enough outer mass survives, (iii) weighted participation and joint oscillation with the aligned unexpanded residual amplitude. The clue is not resolved because none of those three quantitative steps has yet been established.