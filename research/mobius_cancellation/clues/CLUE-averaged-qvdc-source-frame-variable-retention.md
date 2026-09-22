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

`MC-467` prices the remaining apparent freedom in the threshold `M`. The exact normalized parametrization advances the original integer `n` by `[r,r']s_0` when the source index advances by one. Hence on a dyadic reduced-divisor shell `X<=s_0<2X`, one fixed anchor has at most `1+X/T` source points while each source interval has length at most `1+N/([r,r']X)`. In the only regime where the fixed-anchor moment can give a nontrivial gain, their product is bounded by

\[
A_XH_X\le 4\frac{N}{[r,r']T}.
\]

Away from the near-complete endpoint `L_X\approx p`, the shell threshold obeys

\[
M_X<\frac{2N}{\eta p[r,r']}
\qquad
\text{when }L_X\le(1-\eta)p,
\]

so a nonvanishing favorable Fejér fraction at large `r'` requires, at exponent scale,

\[
r'\lesssim_\eta (N/p)^{2/3}.
\]

`MC-468` removes a further shortcut in pricing that surviving region. Abstract `k`-fold well-factorability is completely nonrestrictive on arbitrary `1`-bounded coefficient sequences supported below `Q^{1/k}`: for every factor split, the whole sequence may sit in one geometric-mean-sized factor while all other factors are `delta_1`. More generally, a chosen factorization `lambda=alpha*beta` gives bounded factors and support ranges but no anti-concentration law for either factor. Therefore the required small-cell mass saving cannot be credited to “well-factorability” as a generic regularity property. It must come from the concrete Rosser--Iwaniec/beta-sieve coefficient construction or from a later oscillatory estimate.

## Research question

Inside the cells that survive `MC-467`, can the exact staged family

\[
\sum_{s_0}\widetilde\beta(s_0)
\sum_{j\in J_{s_0}}
\chi(j+U_{s_0})
\overline{\chi(j+U_{s_0}-D_{s_0})}
\overline{B_\beta(C_{s_0}+r_1s_0j)}
\]

be estimated before the second residual expansion and before componentwise positive closure with a strict conductor-power gain that survives the **construction-specific coefficient mass** of the small outer cells, the near-complete endpoint, weighted participation of `\widetilde\beta`, and the aligned residual amplitude?

The bulk support/interval geometry is no longer a live degree of freedom, and generic factorability supplies no coefficient-spreading theorem. A positive factor-specific result must now use either extra structure of the actual sieve coefficients in the small-outer-scale region, a legitimate endpoint mechanism, or cancellation that depends essentially on the retained residual coefficient/amplitude. A source-only conductor-reduction branch remains logically separate and must still pay the full product-level summation cost.

## Why it may matter

The staged route has reached a much sharper bottleneck than generic “use factorability before Cauchy.” The outer source-frame tariff can no longer be beaten by internal-factor multiplicity, large gcds, Fejér short-shift bias, arbitrary shift-independent outer coefficient concentration, treating support size and interval length as independent tunable parameters, or assuming that well-factorability itself spreads coefficient mass. What remains is an arithmetic question about the **specific coefficient construction** and whether the unexpanded aligned amplitude supplies information that the bare source-frame model cannot see.

A negative result showing that the concrete upper-sieve coefficients put insufficient total mass on the surviving small-`r'`/small-lcm and endpoint cells would close the most plausible bare outer/support escape. A positive result would have to exhibit either a construction-specific coefficient concentration law in the favorable direction or a quantitative weighted dispersion mechanism inside those cells rather than recover one of the already-neutralized resources.

## Decisive test

Start from the exact `MC-463` aggregated variable `s_0` and split it dyadically. For every fixed outer pair and original Fejér shift, set

\[
R=[r,r'],
\qquad
T=\frac{r'}{(h,r')}.
\]

Use `MC-467` immediately. Discard as non-gainful the one-point anchor regime `X<T` and the one-point interval regime `RX>N`. In every nonendpoint bulk shell impose

\[
A_XH_X\le 4\frac{N}{RT},
\qquad
M_X<\frac{2N}{\eta pR}.
\]

Then choose the **actual** upper-sieve coefficient family used by the branch, including the finite well-factorable decomposition and one admissible split `lambda=alpha*beta`. Record the sieve level and factor-support parameters explicitly and check where the surviving `r'`/`R` range sits relative to the root-scale vacuity boundary of `MC-468`. No anti-concentration estimate may be inferred from factorability alone.

With those concrete coefficients, sum the true outer coefficient envelope—componentwise if the upper-sieve weight is a finite linear combination—with the standard Fejér shift weight still present, only over cells for which

\[
\min\!\left(1,\frac{M_X(M_X+1)}{r'}\right)
\]

is not negligible. The first decisive question is whether **construction-specific** support/sign/normalization information makes the total mass of those small-`r'`/small-`R` cells too small to support a conductor-power gain. Treat `L_X>(1-\eta)p` as a separate endpoint family rather than hiding it in the bulk threshold.

If a significant family survives, aggregate `\widetilde\beta(s_0)` by exact `(U,D)` collisions, compute its weighted participation rather than support cardinality, and keep

\[
B_\beta(C_{s_0}+r_1s_0j)
\]

inside the estimate. The branch advances only if a fixed-anchor/dispersion or completion estimate retains a strict conductor-power gain after coefficient mass, variable lengths, endpoint cells, aligned amplitude, outer summation, exceptional terms, and source depth are all charged.

Do not reopen large-gcd coefficient concentration, a global `S\times L` threshold, or generic well-factorability as independent resources; `MC-466`--`MC-468` close those mechanisms for the standard staged/Fejér architecture. If a different positive finite-band filter is proposed, its favorable-set concentration must be priced together with its diagonal/DC cost against `MC-416`--`MC-417`.

## Evidence boundary

`MC-467` is an exact shellwise obstruction, not an estimate of the full staged kernel. `MC-468` is an exact class-level no-go for deriving anti-concentration from well-factorability alone; it does **not** determine the coefficient mass of the specific Rosser--Iwaniec/beta-sieve weight, show that every surviving outer cell lies in the root-scale vacuity range, or control the endpoint `L_X\approx p`.

Neither result establishes useful weighted participation of `\widetilde\beta` or estimates the joint character/divisor-sum amplitude. The literature-backed `MC-456` comparison still shows that factor-specific dispersion can genuinely work in other arithmetic geometries; the present obstructions are specific to the exact fixed-character staged source frame and to what can be inferred from the bare factorability definition. No local gain has yet been propagated to a Möbius bound or an RH-relevant global estimate.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-468`**. `MC-467` closes the bulk pair-dependent-threshold loophole by coupling residual support to interval length. `MC-468` then shows that the next coefficient-mass step cannot be solved by a generic “well-factorable weights spread out” principle: below the root-scale support threshold the class is arbitrary, and individual convolution factors need not be anti-concentrated anywhere in their supports.

The live factor-specific work is therefore restricted to: (i) pricing the surviving small-cell mass from the concrete upper-sieve coefficient construction and an explicit admissible factorization; (ii) a separately isolated near-complete endpoint; and, only if enough outer mass survives, (iii) weighted participation and joint oscillation with the aligned unexpanded residual amplitude. The clue is not resolved because none of those three construction-specific quantitative steps has yet been established.