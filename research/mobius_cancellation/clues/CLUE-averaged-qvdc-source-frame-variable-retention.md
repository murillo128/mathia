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
  - research/mobius_cancellation/findings/MC-462-anchor-fibre-support-ceiling-forces-a-residual-range-gate.md
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

`MC-462` now prices the other side of the same quotient. If the residual block is supported on `s<=S` and `t<p`, one fixed anchor can contain at most

\[
1+\frac{S}{dt_0}
=1+\frac{S(h_1,t)}{r_2}
\]

residual divisors. Since participation ratio never exceeds support cardinality, the `MC-461` moment cannot beat the pointwise bound at all in a sector satisfying

\[
1+\frac{S(h_1,t)}{r_2}\le \frac pH.
\]

Thus small anchor diversity is useful only when it is accompanied by enough **per-anchor residual support**. In power-scale form the bare route needs `S H (h_1,t) \gtrsim p r_2`. This eliminates every short-fibre sector before coefficient phases or the surviving amplitude are examined.

## Research question

Can the one-sided staged family isolated by `MC-460`, schematically

\[
\sum_s \beta_s
\sum_{j\in J_s}
\chi(j+U_s)\overline{\chi(j+U_s-\delta s_0^{-1})}
\overline{B_\beta(C_s+r_1s_0j)},
\]

be estimated before the second residual expansion and before componentwise positive closure with a strict conductor-power gain that survives off-diagonal dispersion/completion, outer-factor multiplicity, exceptional source ranges, and later source-depth bookkeeping?

The geometric admissibility part is now explicit. In the `t<p` regime, only gcd sectors satisfying

\[
1+\frac{S(h_1,t)}{r_2}>\frac pH
\]

can possibly exploit the bare fixed-anchor second moment. The live question is therefore whether those favourable sectors carry enough outer weight and whether their **actual** factorable coefficients have participation comparable to the available support. Only after that should the aligned amplitude `B_beta(C_s+r_1s_0j)` and variable lengths `J_s` be passed through a joint dispersion/completion estimate.

A second branch remains legitimate but separate: source-only conductor reduction could still win without factor-specific staging if the reduced-conductor estimate beats the full product-level occupancy cost after every later summation.

## Why it may matter

The factor-specific branch has moved from a qualitative representation question to a sequence of quantitative gates. `MC-458` gives an exact pre-positive carrier, `MC-459` removes positive-energy inflation as the immediate obstruction, `MC-460` promotes a residual factor into a reciprocal translated-character shift, `MC-461` compresses the accompanying start variation, and `MC-462` proves that the same compression yields a necessary residual-range threshold.

A positive route must therefore find genuine mass in sectors where normalized-shift gcd compression is strong enough, residual support is long enough, and coefficient participation survives aggregation. A negative estimate showing that such sectors are too sparse after the outer sums, or that the surviving amplitude destroys the fixed-anchor gain, would close the most plausible remaining well-factorable escape without claiming factorability is useless in other arithmetic geometries.

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

First apply the exact `MC-462` support gate. Sectors with

\[
1+\frac{S(h_1,t)}{r_2}\le\frac pH
\]

cannot gain from bare anchor slicing and should be charged directly rather than sent into a finer occupancy argument. For the complementary sectors, sum the actual outer/gcd weights and determine whether their total mass is polynomially large enough to matter after the `MC-415`/`MC-448` source-depth budget.

Inside those surviving sectors, group residual divisors by exact anchor class and compute the **weighted** participation of reciprocal shifts after collisions modulo `p`, using the actual `beta_s` rather than the support ceiling. Passing the support gate is only admission: the required quantity is still larger than `p/H` per represented anchor at the relevant common-length or legitimate variable-length scale.

Then repeat the estimate with the second residual amplitude still present. Use

\[
C_s\equiv r_1s_0(U_s-D_s)\pmod p
\]

rather than replacing `B_\beta(C_s+r_1s_0j)` by an unrelated pointwise norm. The next substantive gate is passed only if a weighted fixed-anchor dispersion or completion estimate retains a strict conductor-power gain after amplitude variation, variable lengths, gcd sectors, outer `(r,r')` summation, exceptional terms, and source depth are all charged.

A bound that averages over the full `(U,D)` box, expands the surviving divisor sum first, ignores the `MC-462` range condition, or proves only the bare `MC-461` slice moment without controlling the aligned amplitude has not passed this gate.

For the independent source-only branch, propagate the best admissible reduced-conductor estimate through the existing product-level summation and require an actual net conductor-power gain; an improved individual character sum consumed by occupancy does not qualify.

## Evidence boundary

`MC-456` is a literature-backed transfer classification, not a theorem about the Möbius kernel. Reciprocal/Kloosterman and bilinear character-sum methods in the neighboring literature show that reciprocal factor variables can be analytically meaningful, but they do not estimate the coupled family derived here.

`MC-457` exactly closes full completion of an independent coprime factor-residue mask. `MC-458` exactly constructs the staged carrier. `MC-459` proves that its positive diagonal is affordable. `MC-460` exactly derives the reciprocal source shift and modular alignment of the surviving amplitude. `MC-461` exactly classifies the start fibres and the bare prime-conductor fixed-anchor shift moment. `MC-462` adds a coefficient-independent support ceiling and excludes every `t<p` sector whose residual range cannot even meet the `p/H` participation threshold.

None of these findings proves that the favourable sectors have enough total mass, that the actual `beta_s` attain the available participation, that the full weighted family with `B_beta(C_s+r_1s_0j)` intact satisfies a useful joint moment, or that any local gain propagates to the final Möbius source budget. The clue therefore remains `accepted`.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-462`**. The questions “does variable `U_s` automatically restore a two-dimensional conductor box?” and “can every compressed anchor sector exploit the fixed-anchor moment?” are both closed negatively. The first is ruled out by the quotient `s_0 mod t_0`; the second by the support ceiling `1+S(h_1,t)/r_2`.

The live well-factorable branch is now restricted to favourable gcd/range sectors that pass the exact `MC-462` gate. Within them, determine the weighted `D_s` participation, price the total sector mass, and carry the aligned unexpanded residual amplitude through the first oscillatory estimate. Generic internal-factor multiplicity, bounded component splitting, source-only q-vdC after product collapse, complete factor-residue completion, polynomial progression-energy inflation, absence of factor-specific source oscillation, automatically free two-dimensional start/shift variation, and short anchor fibres are now closed or neutralized by `MC-454`--`MC-462`. The independent source-only conductor-reduction branch remains open only as a separate quantitative question.