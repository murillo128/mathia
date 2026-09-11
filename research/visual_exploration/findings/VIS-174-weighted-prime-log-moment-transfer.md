# VIS-174 — weighted prime-log moments transfer at an effective-dimension cost

## Claim

Let `P_y` be any finite set of primes with `p<=y`, let `w_p>0`, and write

`W_y = sum_(p in P_y) w_p`,

`Q_y = sum_(p in P_y) w_p^2`,

`D_2(y) = W_y^2/Q_y`.

Define the centered weighted prime-phase observable

`S_y(t) = Q_y^(-1/2) sum_(p in P_y) w_p [sin^2(t log p/2)-1/2]`.

Let `Theta_p` be independent Haar-uniform angles on `[0,2pi)` and define the matched weighted Haar variable

`S_y^Haar = Q_y^(-1/2) sum_(p in P_y) w_p [sin^2(Theta_p/2)-1/2]`.

Then for every fixed integer `k>=1`, every interval start `T`, and every length `H>0`,

`| H^(-1) int_T^(T+H) S_y(t)^k dt - E[(S_y^Haar)^k] |`
` <= 2^(2-k) y^k D_2(y)^(k/2) / H`.

In particular, along any growing family for which

`y^k D_2(y)^(k/2) / H -> 0`,

the deterministic vertical prime-log orbit inherits the `k`th moment of the representation-matched weighted Haar null.

For the critical-line amplitude-squared taper

`w_p = 1/p`, `p<=y`,

one has

`D_2(y) ~ (log log y)^2/P(2)`,

where `P(s)=sum_p p^(-s)` is the prime zeta function. Hence any polylogarithmic support cap

`y=(log H)^A`, `A>0`,

transfers every preassigned fixed moment as `H->infinity`.

At the same time `VIS-173` gives

`D_4(y) -> P(2)^2/P(4) < infinity`,

so the weighted Haar fluctuation keeps a non-Gaussian low-prime fingerprint. In particular its limiting fourth cumulant is

`-3 P(4)/(128 P(2)^2)`,

and therefore the deterministic fourth moment over polylogarithmically growing support converges to the same non-Gaussian weighted-null value.

Thus **persistent non-Gaussian low-prime shape can survive deterministic prime-log averaging under a genuinely growing cutoff without carrying source-specific information**. `D_2` controls the elementary finite-window transfer cost, while `D_4` independently controls whether the matched Haar shape Gaussianizes.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL KRONECKER/FOURIER SPECIALIZATION + QUANTITATIVE WEIGHTED NULL + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not a discrepancy theorem for arbitrary observables, an optimal growing-support rate, a Gram-point theorem, a zeta-versus-control separation, or an RH consequence.

## 1. Every nonresonant prime-log character has an elementary finite-window gap

Expand a product of `k` cosine factors arising from the prime phases. Every Fourier character has frequency

`lambda = sum_(j=1)^k epsilon_j log p_j`, `epsilon_j in {+1,-1}`.

After collecting repeated primes,

`lambda = sum_p m_p log p = log(a/b)`,

where `m_p` are integers, `a` and `b` are distinct positive integers when `lambda!=0`, and both satisfy

`a,b <= y^k`.

Unique factorization gives `lambda=0` exactly when every net exponent `m_p` vanishes. For a nonzero frequency, assume `a>b`. Then

`|lambda| = log(a/b)`
` >= log(1+1/b)`
` >= 1/(b+1)`
` >= 1/(2y^k)`.

For every interval `[T,T+H]`,

`| H^(-1) int_T^(T+H) exp(i lambda t) dt |`
` <= min(1, 2/(H|lambda|))`
` <= 4 y^k/H`.

The bound is uniform in the starting height `T`. It is crude but completely explicit and uses only unique factorization plus the elementary oscillatory integral.

## 2. Haar and time averages agree exactly on resonant modes

Since

`sin^2(t log p/2)-1/2 = -(1/2) cos(t log p)`,

write

`S_y(t) = -(2 sqrt(Q_y))^(-1) sum_p w_p cos(t log p)`.

Expanding the `k`th power gives ordered prime tuples weighted by `prod_j w_(p_j)`. Each product of cosines is the average of its `2^k` exponential characters.

Under independent Haar phases, a character has expectation one exactly when the net exponent of every prime is zero, and expectation zero otherwise. The deterministic time average has the same value one on every resonant character. Therefore only the nonresonant characters contribute to the difference, and Section 1 bounds each cosine-product discrepancy by `4y^k/H`.

Summing absolute coefficients yields

`| time_k - Haar_k |`
` <= [4 y^k/H] [W_y^k/(2^k Q_y^(k/2))]`
` = 2^(2-k) y^k D_2(y)^(k/2)/H`.

No independence assumption is made for the deterministic orbit. Independence appears only in the matched Haar comparator, and unique factorization identifies exactly the same resonant Fourier modes on both sides.

## 3. Effective dimension is the transfer burden

The normalized weighted observable has Haar variance `1/8`, independent of the weight profile, but the finite-window transfer bound depends on

`W_y/sqrt(Q_y) = sqrt(D_2(y))`.

For equal weights, `D_2=|P_y|`, so the sufficient `k`th-moment condition becomes

`H >> y^k |P_y|^(k/2)`.

This is the natural weighted extension of the fixed-finite vertical-flow identity in `VIS-071`: as support grows, the combinatorial coefficient mass of the moment expansion is paid through `D_2^(k/2)`, while the smallest possible nonzero `k`-character frequency is paid through `y^k`.

The estimate is intentionally one-sided and conservative. It does not assert that either factor is necessary, or that the true equidistribution threshold is this large.

## 4. The `1/p` taper transfers a persistent non-Gaussian shape

Take `P_y={p:p<=y}` and `w_p=1/p`. Classical reciprocal-prime asymptotics give

`W_y ~ log log y`,

while

`Q_y -> P(2)`.

Hence

`D_2(y) ~ (log log y)^2/P(2)`.

If `y=(log H)^A` with fixed `A>0`, then for every fixed `k`,

`y^k D_2(y)^(k/2)/H`
` = O((log H)^(Ak) (log log log H)^k/H)`
` -> 0`.

So every preassigned fixed moment transfers from the deterministic vertical orbit to the weighted Haar law along this genuinely growing prime cutoff.

But `VIS-173` shows that the same weight family has finite shape dimension

`D_4(y) -> P(2)^2/P(4)`.

For the Haar-normalized centered sum, the fourth cumulant therefore tends

`-3/(128 D_4)`
` = -3 P(4)/(128 P(2)^2) != 0`.

The weighted Haar limit is not Gaussian. The transfer estimate above shows that this non-Gaussian fourth-moment signature is also inherited by the deterministic prime-log orbit for polylogarithmic support growth. A visual or statistical experiment that sees this persistent low-prime shape has therefore not yet escaped the representation-matched null.

## 5. Prior art and novelty boundary

No new external theorem is introduced. `VIS-071` already audits the classical Kronecker--Weyl/Bohr fact that a fixed finite prime-phase vertical flow has the shared-phase Haar law. The present finite-window estimate is the direct Fourier-character proof with an explicit elementary lower bound for the nonzero frequencies that can occur in a fixed `k`th moment.

`VIS-173` already audits the classical weighted-array/Lindeberg boundary and derives the separate effective dimensions `D_2` and `D_4`. The reciprocal-prime asymptotic used for `w_p=1/p` is classical Mertens material already anchored in `SOURCES.md`.

No novelty is claimed for quantitative equidistribution of trigonometric polynomials, moment comparison by Fourier expansion, or weighted central-limit theory. The Mathia-specific content is the exact coupling of the existing weighted collision representation to a deterministic growing-cutoff control: the same `D_2` that describes weighted concentration also bounds the elementary moment-transfer burden, while `D_4` can remain finite and preserve non-Gaussian shape.

## Representation consequence

The result separates two representation effects that a visual comparison can otherwise conflate.

Changing prime weights changes the deterministic transfer problem through `D_2=W^2/Q`, because that quantity measures the total coefficient mass relative to the quadratic normalization. The same change can independently preserve or erase non-Gaussian Haar shape through `D_4=Q^2/R`.

The `1/p` taper is the clean counterexample to treating persistent deterministic non-Gaussianity as source evidence: its `D_2` grows slowly enough that fixed moments transfer under a broad polylogarithmic cutoff, while its `D_4` remains finite and forces a permanent low-prime shape fingerprint.

A source-sensitive representation must therefore beat the **weighted deterministic/Haar pair**, not merely differ from the equal-weight Gaussian picture.

## Boundaries and falsification

The theorem concerns continuous vertical averaging. It does not automatically transfer to Gram-point sampling, sparse selectors, short discrete blocks, or an observable containing the zero/hybrid factor.

The moment order `k` is fixed before the limit. The estimate is not uniform in `k`, and it gives no total-variation, Kolmogorov, rare-tail, shrinking-target, or full-distribution bound when support grows.

The `y^k` frequency-separation factor is deliberately elementary and can be far from sharp. A stronger lower bound for the actual character family, cancellation among Fourier coefficients, or a better discrepancy argument could substantially enlarge the admitted cutoff.

The weight family is frozen before source inspection. Post-selecting a taper to manufacture a favorable residual remains outside the control.

Falsify the finding by producing an error in the character-resonance identification, the bound `|log(a/b)|>=1/(2y^k)`, the coefficient-mass calculation, or the imported `D_2`/`D_4` asymptotics.

## Research consequence

The accepted prime-phase clue should no longer treat persistent weighted non-Gaussianity under a slowly growing deterministic prime cutoff as a candidate source signal by itself. For the natural `1/p` taper, that behavior is already forced by the representation-matched Haar law and can be transferred to the actual continuous prime-log orbit over polylogarithmically growing support.

The useful frontier is narrower: a zeta-facing statistic must show a predeclared separation from the **same weighted prime-log control** after matching support growth, normalization, and low-prime participation. A remaining route can still attack sharper growing-dimensional discrepancy, source-sensitive hybrid residuals, Gram/discrete sampling, or a statistic whose contrast survives the `D_2` transfer and `D_4` shape gates.