---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-413-additive-differencing-complete-block-ramanujan-collapse.md
  - research/mobius_cancellation/findings/MC-415-vdc-diagonal-resquares-linear-sieve.md
  - research/mobius_cancellation/findings/MC-416-weighted-vdc-filters-cannot-remove-diagonal.md
  - research/mobius_cancellation/findings/MC-417-fejer-riesz-closes-positive-finite-band-kernels.md
  - research/mobius_cancellation/findings/MC-446-source-frame-box-mean-square-has-quadratic-occupancy-threshold.md
  - research/mobius_cancellation/findings/MC-447-crt-source-frame-fibers-collapse-to-shift-common-primes.md
  - research/mobius_cancellation/findings/MC-448-fixed-lcm-fourier-weil-averaging-still-pays-polynomial-occupancy.md
  - research/mobius_cancellation/findings/MC-449-centered-complement-duality-closes-near-complete-fixed-lcm-escape.md
  - research/mobius_cancellation/findings/MC-450-lcm-frequency-synchronization-recombines-to-centered-autocorrelation.md
  - research/mobius_cancellation/findings/MC-451-beta-sieve-fixed-lcm-signs-are-maximally-coherent.md
  - research/mobius_cancellation/findings/MC-452-truncated-mobius-is-not-well-factorable.md
  - research/mobius_cancellation/findings/MC-453-bounded-factorable-splitting-cannot-dilute-quadratic-diagonal.md
  - research/mobius_cancellation/findings/MC-454-internal-factorization-does-not-increase-source-frame-occupancy.md
  - research/mobius_cancellation/findings/MC-455-standard-qvdc-conductor-reduction-preserves-product-quotient.md
  - research/mobius_cancellation/findings/MC-456-triply-well-factorable-dispersion-provides-a-factor-specific-quotient-breaking-template.md
  - research/mobius_cancellation/findings/MC-457-coprime-factor-residue-completion-tensorizes-from-fixed-source-conductor.md
  - research/mobius_cancellation/findings/MC-458-staged-factor-conditioning-exposes-residual-divisor-sum-kernel.md
  - research/mobius_cancellation/findings/MC-459-staged-residual-energy-is-controlled-by-the-normalized-shift.md
  - research/mobius_cancellation/findings/MC-460-one-sided-residual-conditioning-promotes-reduced-divisor-to-reciprocal-source-shift.md
  - research/mobius_cancellation/findings/MC-461-residual-source-starts-decompose-into-bounded-anchor-slices.md
  - research/mobius_cancellation/findings/MC-462-anchor-fibre-support-ceiling-forces-a-residual-range-gate.md
  - research/mobius_cancellation/findings/MC-463-gcd-sector-normalization-collapses-to-common-anchor-quotient.md
  - research/mobius_cancellation/findings/MC-464-normalized-gcd-gate-makes-favorable-shifts-totient-sparse.md
  - research/mobius_cancellation/findings/MC-465-fejer-weighted-favorable-gcd-classes-remain-sparse.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The direct source-frame repairs are tightly classified. `MC-446`--`MC-450` show that ambient box averaging, hidden CRT multiplicity, one-lcm Fourier/Weil control, near-complete intervals, and bare cross-lcm frequency synchronization do not pay the conductor-power occupancy tariff. `MC-451`--`MC-455` then show that fixed-lcm sieve signs, raw truncated Möbius, bounded factorable component counts, internal factor multiplicity, and source-only conductor splitting do not become exponent-saving resources merely by changing representation.

`MC-456` supplies the positive neighboring template: Pascadi/Yang-type dispersion succeeds when factor blocks occupy genuinely different arithmetic roles before positive closure and survive into reciprocal/Kloosterman phases. `MC-457` tests the most direct transfer into the present fixed-conductor frame and finds exact CRT tensorization: an internal factor retained only as an independent coprime residue modulus disappears from complete mixed blocks, leaving factor dependence only in incomplete tails.

`MC-458` identifies a different legal ordering. For one genuine factorable component `lambda=alpha*beta`, write

\[
B_\beta(y)=\sum_{s\mid y}\beta_s,
\qquad
w(m)=\sum_{r\mid m}\alpha_r B_\beta(m/r).
\]

After conditioning the shifted correlation on the `alpha`-block divisors `r,r'`, the incomplete source kernel becomes a translated primitive-character correlation multiplied by two residual divisor-sum weights along affine quotient progressions. Those residual weights vary with the same integer source variable, so they are not the independent coprime residue masks classified by `MC-457`. Expanding them immediately restores the old product variables, but before that expansion there is a genuine staged factor-weighted kernel on which an analytic estimate can act.

`MC-459` settles the first quantitative objection to this carrier. Writing `r=g r_1`, `r'=g r_2`, `h=g h_0`, the two quotient forms satisfy `r_1y_1-r_2y_2=h_0`; their product therefore has discriminant `h_0^2`. The exact coupled divisor densities are controlled by the normalized shift, and the true positive residual-weight diagonal is only subpower. Progression concentration does **not** force a polynomial loss merely because the quotient slopes are large.

`MC-460` then answers the next structural question positively. If only one residual block is expanded and `s|y_1` is conditioned before the second block is opened, write `d=(s,r_2)`, `s=d s_0`, and `r_2=d t`. After the forced congruence is solved and the remaining progression is rescaled to unit step, the source phase has the exact form

\[
\chi(j+U_s)\overline{\chi(j+U_s-D_s)},
\qquad
D_s=\delta s_0^{-1}\pmod q,
\]

while the second residual amplitude remains unexpanded on `C_s+r_1s_0j`, with

\[
C_s\equiv r_1s_0(U_s-D_s)\pmod q.
\]

Thus a surviving factor variable enters the oscillatory source coordinate itself and the remaining amplitude is aligned with the conjugate-character leg.

`MC-461` removes the main dimensional ambiguity in that source map. In a fixed gcd sector set `h_0=d h_1`, `g_0=(h_1,t)`, and `t_0=t/g_0`. The congruence defining `m_s` implies

\[
m_s=m_{s'}\pmod t
\quad\Longleftrightarrow\quad
s_0=s'_0\pmod{t_0}.
\]

Hence `U_s=m_st^{-1}` occupies at most `phi(t_0)` anchor slices, rather than an automatically conductor-sized independent start coordinate. For prime conductor `p`, each fixed anchor has the exact complete-shift second moment

\[
\sum_{D\bmod p}
\left|\sum_{j\in J}\chi(j+U)\overline{\chi(j+U-D)}\right|^2
\le p|J|.
\]

Consequently a bare source-frame aggregate supported on `R_U` anchors has the slice-Cauchy tariff `R_U p/H`; variable `U_s` does not by itself kill the staged route.

`MC-462` prices the other side of that quotient inside one fixed residual gcd sector. If the residual block is supported on `s<=S` and `t<p`, one fixed anchor contains at most `1+S(h_1,t)/r_2` residual divisors, so a short fibre cannot meet the `p/H` participation threshold.

`MC-463` shows that the sector decomposition itself contains a redundancy. For the fixed outer pair define

\[
G=(h_0,r_2),
\qquad
T=\frac{r_2}{G},
\qquad
H_0=\frac{h_0}{G}.
\]

Every compatible `d=(s,r_2)` has the same reduced quotient `t_0=T`; after normalization the interval, source pair, anchor modulus, and surviving amplitude depend only on `s_0=s/d`, while the original coefficients aggregate exactly into

\[
\widetilde\beta(s_0)
=
\sum_{\substack{d\mid G\\(s_0,r_2/d)=1\\d s_0\le S}}
\beta_{d s_0}.
\]

In the clean regime `T<p`, one anchor contains at most `1+S/T` reduced source points, so the natural full-family support gate is

\[
1+\frac{S(h_0,r_2)}{r_2}>\frac pH.
\]

The internal `d`-sector is therefore not a source-frame resource or cost. The relevant compression parameter is the outer gcd `G=(h_0,r_2)`.

`MC-464` then counts the shifts that can pass this gate. Writing

\[
T(h_0)=\frac{r_2}{(h_0,r_2)},
\]

and expressing the support condition as `T(h_0)<=M`, the favorable residue classes modulo `r_2` have exact cardinality

\[
\sum_{\substack{T\mid r_2\\T\le M}}\varphi(T).
\]

Thus they have vanishing density whenever `M=o(sqrt(r_2))`; merely allowing many shifts does not make the large-gcd sector generic.

`MC-465` propagates the **actual standard Fejér/van-der-Corput outer weights** into those same gcd classes. If `Q` is the Fejér bandwidth, `X=floor((Q-1)/g)>=2`, and `F_Q` is the total nonzero compatible Fejér mass on `T(h_0)<=M`, while `D_Q` is the total compatible positive nonzero Fejér mass, then

\[
\frac{F_Q}{D_Q}
\le
\min\!\left(1,2\frac{M(M+1)}{r_2}\right).
\]

So the triangular preference for short shifts does not rescue the sparse favorable classes: `M=o(sqrt(r_2))` still gives vanishing favorable mass. The first outer-weight loophole is closed for the canonical positive q-vdC kernel. `MC-415`--`MC-417` also show that abandoning Fejér inside the scalar positive finite-band framework is not a free optimization, because the Fejér window already minimizes the normalized diagonal/DC burden, although those findings do not by themselves give a sharp favorable-set concentration inequality for every alternative kernel.

## Research question

Can the one-sided staged family, after the exact `MC-463` aggregation,

\[
\sum_{s_0}\widetilde\beta(s_0)
\sum_{j\in J_{s_0}}
\chi(j+U_{s_0})
\overline{\chi(j+U_{s_0}-D_{s_0})}
\overline{B_\beta(C_{s_0}+r_1s_0j)},
\]

be estimated before the second residual expansion and before componentwise positive closure with a strict conductor-power gain that survives outer coefficient weights, aggregated coefficient participation, amplitude variation, off-diagonal dispersion/completion, exceptional source ranges, and later source-depth bookkeeping?

For a fixed outer pair set

\[
G=(h_0,r_2),
\qquad
T=r_2/G.
\]

`MC-464`--`MC-465` now show that, for the standard Fejér outer average, configurations with sufficiently small `T` are not only support-sparse but carry vanishing relative nonzero shift mass below the square-root normalized-quotient threshold. The live arithmetic question is therefore sharper: **can the actual well-factorable outer coefficients and the aggregated residual coefficients concentrate enough useful signed mass on those sparse favorable classes to overcome that baseline, and does the aligned unexpanded amplitude preserve a conductor-power gain once they do?**

A second branch remains legitimate but separate: source-only conductor reduction could still win without factor-specific staging if the reduced-conductor estimate beats the full product-level occupancy cost after every later summation.

## Why it may matter

The factor-specific branch has moved from a qualitative representation question to a narrow quantitative bottleneck. `MC-458` gives an exact pre-positive carrier, `MC-459` removes positive-energy inflation as the immediate obstruction, `MC-460` promotes a residual factor into a reciprocal translated-character shift, `MC-461` compresses the accompanying start variation, `MC-462` supplies the first support gate, and `MC-463` removes the artificial gcd-sector coordinate. `MC-464`--`MC-465` then show that the outer gcd configurations admitted by that gate are sparse in both counting measure and the standard Fejér shift measure below the same square-root threshold.

A positive route must therefore exhibit **arithmetic coefficient concentration or joint oscillatory structure**, not merely choose the standard shift average and hope that its short-shift bias favors large gcds. A negative result showing that well-factorable coefficient mass cannot concentrate sufficiently on those classes, or that the surviving amplitude destroys the fixed-anchor gain, would close the most plausible remaining factor-specific escape without claiming factorability is useless in other arithmetic geometries.

## Decisive test

Take a balanced well-factorable component `lambda=alpha*beta` in the source form underlying `MC-409`/`MC-413`. Keep the `MC-458` staging and condition on exactly one complementary divisor as in `MC-460`, but **before any Cauchy or sectorwise absolute value**, apply `MC-463`: replace all compatible residual gcd sectors by the single reduced variable `s_0` and coefficient `\widetilde\beta(s_0)`.

For each fixed outer pair compute

\[
G=(h_0,r_2),
\qquad
T=\frac{r_2}{G},
\qquad
U_{s_0}\text{ determined by }s_0\pmod T,
\qquad
D_{s_0}=H_0(r_1Ts_0)^{-1}\pmod p.
\]

In the regime `T<p`, apply the exact full-family support gate first. `MC-464`--`MC-465` already price the **bare standard-Fejér outer mass** of the surviving normalized-gcd classes, so do not repeat that counting argument. Instead restore the actual outer sieve coefficients and determine whether their signed or quadratic weight can concentrate on the classes `T(h_0)<=M` at a rate that beats the Fejér baseline without merely moving the cost into the positive diagonal. If a modified positive finite-band shift filter is proposed, its favorable-set concentration and its diagonal/DC cost must be priced together against `MC-416`--`MC-417`.

Inside the surviving outer classes, group the aggregated coefficients `\widetilde\beta(s_0)` by exact anchor class and reciprocal-shift collision and compute their **weighted participation**, not just support cardinality. Effective participation must exceed the `p/H` slice threshold at the relevant common-length or legitimate variable-length scale.

Then repeat the estimate with the second residual amplitude still present, using its exact aligned trajectory

\[
B_\beta(C_{s_0}+r_1s_0j)
\]

rather than replacing it by an unrelated pointwise norm. The next substantive gate is passed only if a weighted fixed-anchor dispersion or completion estimate retains a strict conductor-power gain after coefficient concentration, amplitude variation, variable lengths, outer summation, exceptional terms, and source depth are all charged.

A bound that treats different `d=(s,r_2)` sectors as independent source families, averages over the full `(U,D)` box, expands the surviving divisor sum first, ignores the normalized-gcd support/mass condition, or merely rederives the bare Fejér sparsity of `MC-465` has not passed this gate.

For the independent source-only branch, propagate the best admissible reduced-conductor estimate through the existing product-level summation and require an actual net conductor-power gain; an improved individual character sum consumed by occupancy does not qualify.

## Evidence boundary

`MC-456` is a literature-backed transfer classification, not a theorem about the Möbius kernel. Reciprocal/Kloosterman and bilinear character-sum methods in the neighboring literature show that reciprocal factor variables can be analytically meaningful, but they do not estimate the coupled family derived here.

`MC-457` exactly closes full completion of an independent coprime factor-residue mask. `MC-458` exactly constructs the staged carrier. `MC-459` proves that its positive diagonal is affordable. `MC-460` exactly derives the reciprocal source shift and modular alignment of the surviving amplitude. `MC-461` exactly classifies the start fibres and the bare prime-conductor fixed-anchor shift moment. `MC-462` adds a sectorwise coefficient-independent support ceiling. `MC-463` proves the common normalized quotient and exact coefficient aggregation. `MC-464` proves totient/gcd sparsity of the favorable outer shifts, and `MC-465` proves that this sparsity survives the standard triangular Fejér weighting with relative favorable mass `O(M^2/r_2)`.

None of these findings proves that the **actual well-factorable coefficient weight** cannot concentrate on the favorable normalized-gcd classes, that `\widetilde\beta` attains the available participation, that the full weighted family with `B_\beta(C_{s_0}+r_1s_0j)` intact satisfies a useful joint moment, or that any local gain propagates to the final Möbius source budget. Nor do `MC-416`--`MC-417` classify every possible arithmetic, signed, or nonstationary reweighting. The clue therefore remains `accepted`.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-465`**. Standard Fejér/q-vdC weighting is no longer a live escape from the normalized-gcd support sparsity: below the square-root quotient scale, the favorable classes carry vanishing relative nonzero shift mass even after the exact triangular weight is applied.

The live well-factorable branch is now restricted to two genuinely arithmetic questions: whether the actual outer sieve coefficients can concentrate useful mass on the sparse favorable gcd classes without an offsetting positive-energy cost, and whether the aggregated `\widetilde\beta` plus the aligned unexpanded residual amplitude then yield a strict conductor-power gain. Generic internal-factor multiplicity, bounded component splitting, source-only q-vdC after product collapse, complete factor-residue completion, polynomial progression-energy inflation, automatically free start/shift variation, short anchor fibres, residual-gcd-sector multiplicity, unweighted favorable-shift abundance, and ordinary Fejér short-shift bias are now closed or neutralized by `MC-454`--`MC-465`. The independent source-only conductor-reduction branch remains open only as a separate quantitative question.