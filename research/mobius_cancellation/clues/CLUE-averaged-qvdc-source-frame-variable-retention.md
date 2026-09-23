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
  - research/mobius_cancellation/findings/MC-471-empty-vector-base-is-two-sided-sifted-translated-ratio-sum.md
  - research/mobius_cancellation/findings/MC-472-pair-sieve-complete-period-factorizes.md
  - research/mobius_cancellation/findings/MC-473-termwise-pair-sieve-completion-pays-exponential-branch-multiplicity.md
  - research/mobius_cancellation/findings/MC-474-pair-sieve-fourier-spectral-norm-is-exponential.md
  - research/mobius_cancellation/findings/MC-475-pair-sieve-parseval-coupling-pays-full-frequency-dimension.md
  - research/mobius_cancellation/findings/MC-476-sifted-restriction-is-coefficient-blind-at-zero-frequency.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The factor-specific route has been reduced to a small number of genuinely different channels. `MC-459`--`MC-467` price the generic staged source geometry: normalized gcd sectors collapse to one anchor quotient, favorable gcd classes remain sparse under Fejér weighting, increasing residual support shortens the corresponding source interval, and nonendpoint gain is forced onto small outer scales. `MC-468` shows that generic well-factorability alone supplies no missing anti-concentration theorem.

The concrete modified linear-sieve decomposition then forces an `r=0` empty-vector component (`MC-469`) with outer geometry `R=T=1`. Its residual is the nonnegative upper-sieve boundary count

\[
B(y)=R_z(y)+E(y),
\qquad
R_z(y)=\mathbf 1_{(y,P(z))=1},
\qquad E(y)\ge0,
\]

so internal coefficient signs do not provide oscillation (`MC-470`). In this base cell, staging also creates no independent reciprocal phase: recombination gives exactly

\[
C_h^{(0)}(I)=\sum_{n\in I}K_h(n)B(n+h)B(n),
\qquad
K_h(n)=\chi(n+h)\overline{\chi(n)}
=\chi\!\left(\frac{n+h}{n}\right)
\]

on nonzero character support (`MC-471`). The amplitude splits into rough×rough, two mixed rough/boundary terms, and boundary×boundary.

For rough×rough, let

\[
W_z=\prod_{\substack{q<z\\q\ne p}}q,
\qquad
A_{W_z,h}(n)=\mathbf 1_{(n(n+h),W_z)=1}.
\]

`MC-472` proves that the complete joint period contains no hidden sieve/phase resonance:

\[
\sum_{n\bmod pW_z}K_h(n)A_{W_z,h}(n)
=-W_z\delta_{W_z}(h),
\]

with normalized mean `-delta_W(h)/p`. Odd shifts vanish exactly when `z>2`, and the uniform shift-average of `delta_W(h)` is the independent reduced-residue baseline. Thus the live rough×rough object is the centered incomplete discrepancy

\[
\mathcal D_{W,h}(I)
=
\sum_{n\in I}K_h(n)A_{W,h}(n)
+\frac{|I|}{p}\delta_W(h).
\]

`MC-473` closes the most direct incomplete repair. Exact Möbius expansion of both roughness constraints followed by a separate Fourier/Weil completion of every congruence branch gives

\[
|\mathcal D_{W,h}(I)|
\ll
\sqrt p\log p\,
\mathcal B_W(h),
\qquad
\mathcal B_W(h)=\prod_{q\mid W}(1+\nu_q(h)),
\]

up to the smaller finite-interval centering term. For a primorial sieve,

\[
2^{\omega(W)}\le\mathcal B_W(h)\le3^{\omega(W)}.
\]

So the individual progression character sums are easy, but full inclusion-exclusion plus branchwise absolute values is exponentially expensive in the number of sieve primes. This is a method obstruction, not a lower bound for the true discrepancy: any surviving sieve route must keep cancellation or approximation structure across divisor levels before absolute closure.

`MC-474` and `MC-475` classify the two most immediate Fourier repairs. Exact additive Fourier expansion followed by separate modewise completion still pays an exponentially large Fourier `ell^1` norm. Replacing `ell^1` scalarization by plain Cauchy--Schwarz/Parseval does not help either: if

\[
S_r(I)=\sum_{n\in I}K_h(n)e_W(rn),
\]

then grouping by residues modulo `W` gives exactly

\[
\sum_{r\bmod W}|S_r(I)|^2
=W\sum_{a\bmod W}\left|
\sum_{\substack{n\in I\\n\equiv a\pmod W}}K_h(n)
\right|^2.
\]

In the live `|I|<W`, `|I|\le p` regime this is essentially `W|I|`. Thus the centered mask has cheap Fourier `ell^2` energy, but the matching full-grid response carries the entire primorial frequency dimension. Ordinary full-grid additive large-sieve averaging therefore reproduces the same `W` cost rather than yielding a conductor-power saving.

`MC-476` now audits the natural next suggestion against the current general restriction theory for sifted sets. Bera--Viswanadham's 2026 restriction theorem applies directly to the shifted pair sieve for surviving even shifts when `z<=|I|^(1/4)`: each small prime forbids one or two residues and the corresponding sieve dimension is two. But the theorem is uniform in the coefficient sequence and sees `K_h` only through its `ell^2` mass. At the zero additive frequency it therefore gives essentially the same norm bound for `K_h` as for constant positive coefficients on the same sifted support. Since its sieve quantity is at most polylogarithmic for this dimension-two sieve, the black-box restriction inequality cannot itself supply a fixed power of the character conductor.

Crucially, this does not exhaust the new prior art. Bera--Viswanadham's proof uses an enveloping-sieve majorant whose Fourier representation is supported on rational frequencies with denominators at most `z^2`, far smaller as a representation than the full primorial `W` grid. That compressed representation remains potentially useful only if it is coupled to `K_h`-specific cancellation **before** coefficient phase is discarded. Positivity of the majorant alone does not authorize its substitution inside the signed character sum.

There is also a one-sided prior-art boundary from Gong--Jia--Korolev: above the square-root conductor scale, `sum R_z(n)K_h(n)` and its translated analogue receive logarithmic cancellation because one rough leg can be absorbed into a bounded multiplicative coefficient. That theorem neither handles the joint pair-sieve coefficient nor supplies the required conductor-power gain.

## Research question

Can the concrete staged-sieve decomposition still produce a strict conductor-power gain through a mechanism that survives `MC-473`--`MC-476`?

For the **empty-vector rough×rough component**, the target is no longer generic incomplete completion, exact hard-mask Fourier expansion, ordinary full-grid Hilbert-space averaging, or a black-box application of a coefficient-uniform sifted restriction theorem. The sharp restriction-style question is now: can the **low-denominator enveloping-sieve representation** be combined with a conductor-sensitive estimate for the translated-ratio phase before positive majorization or norm closure destroys that phase? Equivalent alternatives are a truncated/factorable beta-sieve weight, a Buchstab/bilinear decomposition, or dispersion performed before the full `W`-frequency frame is formed. Any approximation to the exact pair-sieve indicator must price its signed error on the actual source interval; positivity or a standard density asymptotic alone is insufficient.

The three positive boundary variants obtained by replacing one or both rough indicators by `E` remain separate targets. Their first-exit structure is not covered by the complete-period factorization, branch-multiplicity calculation, hard-mask Fourier barriers, or the rough-pair restriction audit.

For **nonempty rough-block components**, after discarding every bin tuple whose product cannot enter the `MC-467` small-outer region, does the surviving normalized signed mass remain large and structured enough for factor-specific dispersion to matter?

A third channel is **cross-component interference**. It is admissible only if the complete signed finite decomposition is carried through an oscillatory transform before componentwise absolute values or positive quadratic closure.

## Why it may matter

The route has progressively removed fake resources: large gcd, extra factor labels, Fejér concentration, independent support/interval tuning, generic well-factorability, blanket support pruning, internal signs of the empty-vector upper-sieve residual, the reciprocal divisor coordinate, complete-period sieve/phase resonance, full exact pair-sieve inclusion-exclusion followed by independent completion, exact Fourier `ell^1` recombination, plain full-grid `ell^2`/ordinary-large-sieve averaging, and now coefficient-uniform restriction at the target zero mode.

The latest prior art also gives a more concrete positive target than the vague phrase “try restriction theory.” A general sifted restriction theorem already exists and is not enough by itself; what remains is its **representation layer**. If the `q<=z^2` enveloping frequencies can be coupled to the special rational character phase with a conductor-power estimate while the signed replacement cost stays below the gain, that would evade the full-primorial complexity exposed by `MC-473`--`MC-475`. Conversely, if this compressed majorant necessarily loses the needed phase through positive domination or its signed replacement error recreates the source tariff, the main restriction-style escape closes cleanly.

## Decisive test

For the **base rough×rough term**, set `R=T=1` and work in the recombined `n` representation. Remove odd `h` exactly when `z>2` and subtract the complete mean `-delta_W(h)/p` from the outset.

Do **not** re-expand the exact pair sieve completely and estimate every divisor/residue branch independently: `MC-473` proves that this pays `B_W(h)=prod(1+nu_q(h))`. Do **not** replace that by exact hard-mask Fourier modes and estimate them independently: `MC-474` proves exponential `ell^1` cost. Do **not** rely only on Cauchy--Schwarz/Parseval or the ordinary additive large sieve over all `W` modes: `MC-475` proves that the dual response energy pays the full primorial frequency dimension. Do **not** invoke the Bera--Viswanadham restriction inequality at zero frequency as the missing character estimate: `MC-476` proves that this step is coefficient-blind and contains no conductor-sensitive power gain.

The immediate restriction-style test is instead to take the **enveloping-sieve majorant/decomposition itself**, with its rational Fourier support at denominators `q<=z^2`, and derive both sides of the actual signed tradeoff:

1. a conductor-sensitive estimate for the resulting `K_h`-twisted rational-frequency family, with the total coefficient/norm cost over `q<=z^2` explicit; and
2. a valid treatment of the difference between the exact pair-sieve indicator and the enveloping object on the actual source interval. Pointwise majorization is not enough because `K_h` changes phase; either the replacement must occur inside a legitimate positive quadratic form that retains useful character information or the signed replacement error must be bounded directly.

Accept the route only if these two bounds together produce a strict conductor-power saving after source length, shell summation, Fejér weights, endpoint separation, coefficient normalization, and source depth are charged. Kill the route if the low-denominator representation still accumulates enough coefficient/spectral mass to erase the character saving, or if making the majorant accurate enough forces a signed replacement error of trivial scale.

For the mixed and boundary terms, use the exact first-exit formula from `MC-470`; high rank or nonnegativity alone is not sparsity. For nonempty components, apply the exact lower support `a>D_1...D_r` before estimating surviving tuples. For cross-component interference, retain the signed finite sum through the proposed transform and exhibit a concrete cross term whose cancellation survives normalization; separate positive energies followed by a later appeal to cancellation do not qualify.

Keep exact `(U,D)` collision aggregation wherever a staged form is genuinely needed, and isolate the near-complete endpoint instead of hiding it in a bulk estimate.

## Evidence boundary

`MC-472` proves only complete-period factorization and local density identities. `MC-473` proves only that full exact inclusion-exclusion plus independent branchwise completion is too expensive. `MC-474` proves only that exact hard-mask Fourier expansion plus modewise absolute values has exponential Fourier `ell^1` cost. `MC-475` proves only that plain full-grid `ell^2` coupling restores the full `W`-dimensional response energy. `MC-476` proves only that the current general coefficient-uniform sifted restriction theorem does not expose translated-ratio character cancellation at zero frequency; it explicitly leaves the enveloping representation plus a coefficient-specific estimate open.

None of these results bounds the actual incomplete discrepancy or rules out a successful low-denominator enveloping-sieve/character coupling, truncated structured weights, Buchstab identities, bilinear forms, or dispersion before scalarization. Likewise, none proves a power saving for the boundary terms, the surviving nonempty components, or cross-component interference. No conductor-power gain, Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted` and is materially narrowed through `MC-476`. The immediate rough×rough restriction test is now **representation-level rather than theorem-level**: the general restriction inequality already exists but quotients away the needed coefficient phase, while its low-denominator enveloping sieve may still compress the exact pair-sieve complexity enough to permit a separate `K_h`-specific estimate. Full inclusion-exclusion plus termwise completion, exact hard-mask Fourier `ell^1` recombination, ordinary full-grid `ell^2` averaging, and black-box zero-mode sifted restriction are closed as standalone routes. The low-denominator mixed sieve/character coupling, boundary terms, nonempty components, and pre-positive cross-component interference remain distinct surviving channels.