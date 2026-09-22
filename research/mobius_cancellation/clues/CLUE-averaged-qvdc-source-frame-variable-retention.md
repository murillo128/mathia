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

The source geometry is tightly classified. `MC-461` decomposes starts into arithmetic anchor slices; `MC-463` removes the artificial residual gcd-sector multiplicity. For a fixed outer pair and compatible original shift,

\[
T=\frac{r'}{(h,r')}
\]

is the common normalized anchor modulus, and all compatible residual sectors aggregate into one reduced variable `s_0` with coefficient `\widetilde\beta(s_0)`.

`MC-464`--`MC-466` price the outer shift supply. Favorable normalized-gcd classes are totient-sparse, remain sparse under standard Fejér weights, and the apparent benefit of concentrating outer coefficients on large `(r,r')` cancels in the original shift envelope. `MC-467` then couples residual support to interval length. On a dyadic shell `X<=s_0<2X`, with

\[
R=[r,r'],
\qquad
T=\frac{r'}{(h,r')},
\]

one has in the nonendpoint bulk

\[
A_XH_X\le 4\frac{N}{RT},
\qquad
M_X<\frac{2N}{\eta pR},
\]

and a nonvanishing favorable Fejér fraction at large `r'` requires, at exponent scale,

\[
r'\lesssim_\eta (N/p)^{2/3}.
\]

`MC-468` shows that this surviving coefficient-mass problem cannot be solved from generic well-factorability: below the root-scale vacuity radius the class permits arbitrary bounded concentration, and a chosen factorization `lambda=alpha*beta` carries no anti-concentration law for its factors.

`MC-469` now opens one concrete upper-linear-sieve decomposition rather than reasoning from the abstract class. In Lichtman's finite rough-block decomposition, the `r=0` empty-vector term is an actual component. Its rough-block factor is exactly `delta_1`, while the residual factor is the parity-even upper beta-sieve weight. Under the `MC-458` staging this gives

\[
\alpha=\delta_1,
\qquad
\beta=\lambda^{(0)},
\]

so the outer source-frame parameters are exactly

\[
R=T=1.
\]

Therefore construction-specific support pruning cannot make **all** small outer cells disappear componentwise: the empty-vector base component sits at the minimal outer cell. For nonempty rough-block components, however, the same published construction gives a genuine support filter: if their block bins are `(D_1,\ldots,D_r)`, their outer product exceeds `D_1\cdots D_r`, so an outer cutoff `a<=Y` eliminates every component with `D_1\cdots D_r>=Y`.

The coefficient problem has therefore bifurcated. The nonempty pieces can still be priced by exact bin-product support. The empty-vector piece bypasses that pruning entirely and must be attacked through its residual beta-sieve amplitude, a separately justified endpoint mechanism, or cancellation with other signed components retained before positive closure.

## Research question

For the concrete staged decomposition after `MC-469`, can either of the two surviving channels produce a strict conductor-power gain?

First, for the **empty-vector base component**, can the exact family

\[
\sum_{s_0}\widetilde\beta(s_0)
\sum_{j\in J_{s_0}}
\chi(j+U_{s_0})
\overline{\chi(j+U_{s_0}-D_{s_0})}
\overline{B_{\lambda^{(0)}}(C_{s_0}+s_0j)}
\]

be estimated before the second residual expansion and before positive closure with a power gain that survives the near-complete endpoint and weighted participation of the residual coefficient?

Second, after discarding nonempty rough-block components whose bin product cannot enter the `MC-467` small-outer region, does the **remaining nonempty family** carry enough signed/componentwise mass for factor-specific dispersion to matter, or is it too sparse/expensive once Fejér shifts, source lengths, and residual amplitudes are charged?

A third possibility remains logically distinct: retain the complete signed finite decomposition through an oscillatory transform and exploit cross-component interference. `MC-453` and `MC-469` do not rule that out, but any such proposal must keep the interference explicitly; it cannot first apply triangle inequalities or separate positive energies and later appeal to cancellation.

## Why it may matter

The route is no longer a vague instruction to “use factorability before Cauchy.” The outer source-frame tariff cannot be beaten by internal-factor multiplicity, large gcds, Fejér short-shift bias, arbitrary shift-independent coefficient concentration, independent tuning of support and interval length, generic well-factorability, or a blanket claim that concrete rough-block support removes every favorable small cell.

`MC-469` is especially diagnostic because it prevents a false negative closure. A calculation showing that all **nonempty** rough-block bins miss the favorable region would not by itself kill the branch: the base upper-beta-sieve component would still remain at `R=T=1`. Conversely, if the base component is shown to obey the same source-frame barrier after its residual amplitude is used optimally, and the nonempty pieces are either support-pruned or individually too costly, then the current componentwise architecture would be close to a genuine closure.

## Decisive test

Start from the exact `MC-463` aggregated variable `s_0`, retain the standard Fejér shift weight, and split dyadically. Use `MC-467` immediately in every nonendpoint bulk shell:

\[
A_XH_X\le 4\frac{N}{RT},
\qquad
M_X<\frac{2N}{\eta pR}.
\]

Then use one concrete published upper-sieve decomposition rather than the abstract factorability class.

**Base component.** Isolate the `r=0` empty-vector term before summing any other component. For the Lichtman decomposition, use `alpha=delta_1`, `beta=lambda^(0)`, hence `R=T=1`. Do not credit any outer-support saving to this term. Aggregate `\widetilde\beta(s_0)` by exact `(U,D)` collisions, measure its weighted participation rather than support cardinality, keep

\[
B_{\lambda^{(0)}}(C_{s_0}+s_0j)
\]

inside the estimate, and isolate `L_X>(1-\eta)p` rather than hiding it in the bulk bound. The base branch advances only if the residual amplitude/character interaction yields a strict conductor-power gain after all shell, Fejér, endpoint, and outer costs.

**Nonempty components.** For each rough-block vector `(D_1,\ldots,D_r)`, use the exact support lower bound

\[
a>D_1\cdots D_r.
\]

Given the surviving outer cutoff from `MC-467`, discard every bin tuple whose product already exceeds that cutoff. On the surviving tuples, retain the actual scalar normalization/sign from the finite decomposition, choose an admissible factor split, and price the true outer coefficient envelope with the Fejér factor

\[
\min\!\left(1,\frac{M_X(M_X+1)}{r'}\right).
\]

Only if a quantitatively significant nonempty family survives should the calculation proceed to exact `(U,D)` collisions and the aligned residual amplitude.

**Cross-component channel.** If the base and nonempty pieces are to cancel each other, do not estimate them separately first. Carry the signed finite combination through the proposed oscillatory transform and exhibit an explicit cross-component term whose cancellation survives normalization, source lengths, and the old `MC-453` component-energy floor.

The branch advances only on a conductor-power gain after coefficient normalization, surviving-bin mass, variable lengths, endpoint cells, aligned amplitude, outer summation, exceptional terms, and source depth are all charged. Do not reopen large-gcd concentration, a global `S\times L` threshold, generic well-factorability, or “all small cells are support-pruned” as independent resources.

## Evidence boundary

`MC-467` is an exact shellwise obstruction, not an estimate of the complete staged kernel. `MC-468` is a class-level no-go for deriving anti-concentration from well-factorability alone. `MC-469` adds a construction-specific fact for one published modified linear-sieve decomposition: its empty-vector component survives at the minimal outer cell, while nonempty rough-block components obey explicit bin-product support constraints.

`MC-469` does **not** provide a lower bound on the fully recombined sieve weight, because the finite decomposition is signed; it does not show that the empty-vector residual amplitude is large; and it does not claim that every Rosser--Iwaniec or beta-sieve representation has the identical component organization. Cross-component interference and residual-amplitude cancellation remain open mechanisms.

The literature-backed `MC-456` comparison still shows that factor-specific dispersion can genuinely work in other arithmetic geometries. No local gain from the present fixed-character source frame has yet been propagated to a Möbius bound or an RH-relevant global estimate.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-469`**. The coefficient-mass stage is no longer one aggregate question. It splits into: (i) the unavoidable empty-vector base component, which must be attacked through the residual beta-sieve amplitude/endpoint or through retained cross-component interference; and (ii) nonempty rough-block components, which should first be pruned by the exact product of their prime bins and only then priced quantitatively.

The next useful work is therefore to price the base component's weighted residual participation and source-frame estimate at `R=T=1`, while separately summing only the nonempty bin tuples that can actually enter the `MC-467` favorable outer region. The clue is not resolved because neither quantitative calculation has yet been carried through.