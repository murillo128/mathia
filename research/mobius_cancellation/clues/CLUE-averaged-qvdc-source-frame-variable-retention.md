---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-413-additive-differencing-complete-block-ramanujan-collapse.md
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

`MC-461` now removes the main dimensional ambiguity in that source map. In a fixed gcd sector set `h_0=d h_1`, `g_0=(h_1,t)`, and `t_0=t/g_0`. The congruence defining `m_s` implies

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

Consequently a bare source-frame aggregate supported on `R_U` anchors has the slice-Cauchy tariff `R_U p/H`, and the full `p^2/H` ambient tariff reappears only if anchor diversity itself reaches conductor scale. The variable `U_s` therefore does **not** by itself kill the staged route. What remains unresolved is whether the actual residual weights populate enough reciprocal shifts per anchor and whether the unexpanded aligned `B_beta` amplitude can survive the same dispersion step.

## Research question

Can the one-sided staged family isolated by `MC-460`, schematically

\[
\sum_s \beta_s
\sum_{j\in J_s}
\chi(j+U_s)\overline{\chi(j+U_s-\delta s_0^{-1})}
\overline{B_\beta(C_s+r_1s_0j)},
\]

be estimated before the second residual expansion and before componentwise positive closure with a strict conductor-power gain that survives off-diagonal dispersion/completion, outer-factor multiplicity, exceptional source ranges, and later source-depth bookkeeping?

The source-pair multiplicity question is now partly resolved by `MC-461`: in a fixed gcd sector the starts factor through `s_0 mod t_0`, so the decisive quantity is no longer ambient two-dimensional occupancy but **effective reciprocal-shift occupancy inside each represented anchor fibre**. Does the actual well-factorable residual-divisor range supply more than `p/H` effective `D_s` values per anchor often enough to gain, and can that gain be retained when the aligned amplitude `B_beta(C_s+r_1s_0j)` and variable lengths `J_s` are kept rather than majorized away?

A second branch remains legitimate but separate: source-only conductor reduction could still win without factor-specific staging if the reduced-conductor estimate beats the full product-level occupancy cost after every later summation.

## Why it may matter

The earlier structural ambiguity in the factor-specific branch is gone. `MC-458` gives an exact pre-positive carrier, `MC-459` removes positive-energy inflation as the immediate obstruction, `MC-460` promotes a residual factor into a reciprocal translated-character shift, and `MC-461` proves that the accompanying start variation is arithmetically compressed rather than automatically free.

This puts the branch at a genuinely quantitative threshold. A favourable range with small `phi(t_0)` and many reciprocal shifts per anchor could lower the source-frame cost before product collapse. An unfavourable theorem showing that the actual factorable coefficients never supply the required `p/H` effective fibre occupancy, or that preserving the second residual amplitude necessarily destroys fixed-anchor orthogonality, would close the most plausible remaining well-factorable escape.

## Decisive test

Take a balanced well-factorable component `lambda=alpha*beta` in the source form underlying `MC-409`/`MC-413`. Keep the `MC-458` staging, condition on exactly one complementary divisor as in `MC-460`, and preserve the second `B_\beta` block through the first nontrivial Cauchy/dispersion/completion step.

For each fixed outer pair and gcd sector, write

\[
t_0=\frac{t}{(h_1,t)},
\qquad
U_s\text{ determined by }s_0\pmod{t_0},
\qquad
D_s=\delta s_0^{-1}\pmod p.
\]

Group the residual divisors by their exact anchor class before applying positivity. Compute the effective weighted occupancy of reciprocal shifts inside each `U` fibre, including collisions modulo `p`, the actual `beta_s` magnitudes, and the admissible `s_0` range. The bare source-frame gate from `MC-461` is crossed only when the fibre participation ratio is larger than `p/H` after the relevant common-length or legitimate variable-length reduction.

Then repeat the estimate **with the second residual amplitude still present**. Use the alignment

\[
C_s\equiv r_1s_0(U_s-D_s)\pmod p
\]

rather than replacing `B_\beta(C_s+r_1s_0j)` by an unrelated pointwise norm. The next substantive gate is passed only if a weighted fixed-anchor dispersion or completion estimate retains a strict conductor-power gain after the amplitude, variable lengths, gcd sectors, outer `(r,r')` summation, exceptional terms, and `MC-415`/`MC-448` source-depth bookkeeping are all charged.

A bound that averages over the full `(U,D)` box, expands the surviving divisor sum first, or proves only the bare `MC-461` slice moment without controlling the aligned amplitude has not passed this gate.

For the independent source-only branch, propagate the best admissible reduced-conductor estimate through the existing product-level summation and require an actual net conductor-power gain; an improved individual character sum consumed by occupancy does not qualify.

## Evidence boundary

`MC-456` is a literature-backed transfer classification, not a theorem about the Möbius kernel. Reciprocal/Kloosterman and bilinear character-sum methods in the neighboring literature show that reciprocal factor variables can be analytically meaningful, but they do not estimate the coupled family derived here.

`MC-457` exactly closes full completion of an independent coprime factor-residue mask. `MC-458` exactly constructs the staged carrier. `MC-459` proves that its positive diagonal is affordable. `MC-460` exactly derives the reciprocal source shift and modular alignment of the surviving amplitude. `MC-461` exactly classifies the start fibres and the bare prime-conductor fixed-anchor shift moment.

None of these findings controls the full weighted family with `B_beta(C_s+r_1s_0j)` intact, proves that enough effective reciprocal shifts occur in the actual well-factorable range, or propagates a gain to the final Möbius source budget. The clue therefore remains `accepted`.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-461`**. The question “does variable `U_s` automatically restore a two-dimensional conductor box?” is closed negatively: in each gcd sector `U_s` factors through `s_0 mod t_0`, and prime-conductor shift averaging has only a `p/H` tariff per represented anchor.

The live well-factorable branch is now the weighted fibre problem: determine the actual effective `D_s` occupancy inside those anchor classes and carry the aligned unexpanded residual amplitude through the first oscillatory estimate. Generic internal-factor multiplicity, bounded component splitting, source-only q-vdC after product collapse, complete factor-residue completion, polynomial progression-energy inflation, absence of factor-specific source oscillation, and automatically free two-dimensional start/shift variation are now closed or neutralized by `MC-454`--`MC-461`. The independent source-only conductor-reduction branch remains open only as a separate quantitative question.