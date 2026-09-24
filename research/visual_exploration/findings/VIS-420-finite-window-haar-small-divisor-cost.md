# VIS-420 — finite translation-to-Haar calibration carries an explicit small-divisor cost

## Claim

Fix one finite Wang shell in the prime-torus form established by `VIS-419`,

`F_M(T)=Phi_M(z(T))`,

where `z_p(T)=p^(-iT)` for the finite set of base primes `P_M`. Let

`G(z)=sum_(m in S) c_m z^m`

be any finite trigonometric/Laurent polynomial on that torus, with `m=(m_p)_(p in P_M)` and

`nu_m=sum_p m_p log p`.

For every starting height `T_0` and translation length `V>0`,

`(1/V) integral_0^V G(z(T_0-s)) ds - c_0`

is exactly

`sum_(m in S, m!=0) c_m z(T_0)^m exp(i V nu_m/2) sinc(V nu_m/2)`,

with `sinc(x)=sin(x)/x`. Unique factorization gives `nu_m!=0` for every nonzero character, so

`| (1/V) integral_0^V G(z(T_0-s)) ds - c_0 |`
` <= sum_(m!=0) |c_m| min(1, 2/(V |nu_m|))`
` <= (2/V) sum_(m!=0) |c_m|/|nu_m|`.

Thus `VIS-419`'s asymptotic translation/Haar equivalence has an explicit finite-window calibration for every character-polynomial observable, but the rate necessarily sees the active **small divisors** `|m dot (log p)|`. Mode count, outer bandwidth, coefficient norm, or shell support size alone do not supply this rate.

For a shell written with distinct real frequencies

`F_M(T)=sum_j B_j exp(-i lambda_j T)`,

its finite-window mean obeys

`| (1/V) integral_0^V F_M(T_0-s) ds - E_Haar[F_M] |`
` <= (2/V) sum_(lambda_j!=0) |B_j|/|lambda_j|`,

and its mean energy has the exact bound

`| (1/V) integral_0^V |F_M(T_0-s)|^2 ds - sum_j |B_j|^2 |`
` <= (2/V) sum_(j!=k) |B_j B_k|/|lambda_j-lambda_k|`,

after equal frequencies have been combined. The second bound makes the beat-gap obstruction from `VIS-417` the general finite-shell small-divisor cost for quadratic translation averages.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL QUANTITATIVE KRONECKER/FOURIER SPECIALIZATION + CONTROL CALIBRATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No uniform growing-shell rate, nonlinear tail bound, distinguished-height anomaly, or RH consequence is claimed.

## 1. Exact finite-window character average

From `VIS-419`, translation of the base-prime phase point is

`z_p(T_0-s)=z_p(T_0) p^(is)`.

Therefore one torus character satisfies

`z(T_0-s)^m = z(T_0)^m exp(i s nu_m)`.

If `m=0`, its translation average is the constant coefficient `c_0`, which is exactly its Haar average. If `m!=0`, unique factorization gives

`nu_m=sum_p m_p log p = log(prod_p p^(m_p)) != 0`.

Direct integration yields

`(1/V) integral_0^V exp(i s nu_m) ds`
` = exp(i V nu_m/2) sin(V nu_m/2)/(V nu_m/2)`.

Summing the finitely many characters proves the exact identity in the claim. The pointwise estimate

`|sinc x| <= min(1,1/|x|)`

gives the two displayed bounds immediately.

The convergence in `VIS-419` therefore has no mystery at the finite-polynomial level: every nonconstant Fourier character dies at a rate set by its own orbit frequency, and characters with very small `|nu_m|` can remain coherent over a long translation window.

## 2. Shell mean and energy are explicit specializations

Write the combined distinct-frequency shell as

`F_M(T)=sum_j B_j exp(-i lambda_j T)`.

For the mean, each shell mode is one prime-torus character with orbit frequency `-lambda_j`; the general bound gives the first specialization in the claim. Canonical strict ratio modes have no constant character, so the Haar mean is zero unless the shell definition explicitly retains a zero-frequency term.

For energy,

`|F_M(T)|^2 = sum_(j,k) B_j conjugate(B_k) exp(-i(lambda_j-lambda_k)T)`.

The diagonal `j=k` terms are constant and give the Haar mean `sum_j |B_j|^2`. Each off-diagonal term has orbit frequency `lambda_j-lambda_k`, hence direct integration gives the second displayed bound.

This is the finite-shell version of the same mechanism isolated visually and then exactly in `VIS-417`: close frequencies create a long beat scale because the corresponding quadratic character has a small orbit frequency.

## 3. What the bound does and does not calibrate

The accepted clue `CLUE-wang-phase-anchored-small-values` asks about normalized amplitude and fixed-radius quiet-region statistics at pre-specified distinguished heights. Those observables are continuous on the fixed shell's prime torus, but absolute value, supremum, and threshold/tail operations are not themselves finite character polynomials in general.

The present result therefore does **not** turn an arbitrary nonlinear finite-window statistic into a certified Haar sample merely by choosing a large-looking `V`. There are two safe routes:

1. evaluate or sample the exact base-prime Haar pushforward directly, as permitted by `VIS-419`; or
2. approximate the chosen continuous torus observable by a controlled finite Fourier polynomial and pay both the approximation error and the explicit small-divisor sum above.

For threshold probabilities, the continuity-point qualification already recorded in `VIS-419` remains necessary. For a family whose shell support or statistic changes with height, a uniform translation-window theorem additionally needs uniform control of the Fourier approximation and its active small divisors. The fixed-shell asymptotic theorem alone does not provide that.

## 4. Consequence for the phase-anchored Wang test

This closes one operational ambiguity in the accepted clue. If the comparison uses direct prime-torus Haar integration or Haar phase sampling, no translation-window convergence assumption is needed. If it instead approximates the self-null by translating the actual shell over a finite interval, the interval length must be justified against the chosen observable's active character frequencies rather than only against bandwidth, mode count, or an informal notion of a "long" window.

For polynomial diagnostics such as the shell mean or energy, the displayed sums give an immediate auditable tolerance rule. For the intended amplitude/persistence tail test, direct Haar evaluation is cleaner unless a quantitative Fourier approximation is supplied.

The source question remains unchanged: even after the null is calibrated exactly, a distinguished arithmetic height might or might not occupy an atypical part of that fixed shell's Haar distribution. This finding calibrates the null; it supplies no positive evidence for the anomaly.

## Prior art and novelty audit

The underlying quantitative mechanism is classical Fourier analysis of Kronecker motion, not a new equidistribution theorem. Leonardo Colzani, **Speed of convergence of Weyl sums over Kronecker sequences**, *Monatshefte für Mathematik* 200 (2023), 209–228, DOI `10.1007/s00605-022-01785-z`, explicitly records the continuous-rotation analogue

`(1/T) integral_0^T f(x+t alpha) dt - integral f`

as a Fourier sum with the same sinc factor `sin(pi T m dot alpha)/(pi T m dot alpha)` and discusses how convergence rates depend on Fourier support and Diophantine properties. The fixed prime-torus/Bohr correspondence itself is already bounded as prior art in `VIS-419` by Hedenmalm–Lindqvist–Seip and Defant–García–Maestre–Sevilla-Peris.

No novelty is claimed for the sinc integral, small divisors in torus rotations, quantitative Kronecker theory, or the energy expansion. The durable Mathia content is the explicit specialization that converts the qualitative boundary left by `VIS-419` into an auditable finite-window control for the current Wang self-null and shows exactly why a growing-shell test cannot inherit a shell-independent translation length for free.

## Boundaries and falsification

The bound is finite-shell and finite-Fourier. It may be numerically loose because the triangle inequality discards cancellation between characters; looseness does not invalidate it as a sufficient calibration bound.

It does not prove that the canonical Wang shell family actually develops arbitrarily small relevant divisors at any specified rate. Such a family-level statement would require analysis of the shell's changing prime-power character support.

It does not bound a discontinuous threshold statistic without additional boundary regularity, nor a continuous nonlinear statistic without either direct Haar evaluation or a quantitative Fourier approximation.

Falsify the exact formulas by exhibiting a nonzero prime-torus character with `nu_m=0`, a failure of the displayed character integral, or a shell energy expansion whose off-diagonal orbit frequency is not `lambda_j-lambda_k`. Any of these would contradict the derivation directly.

## Dependencies

- `VIS-417`: beat-scale obstruction for finite-window low-amplitude persistence.
- `VIS-418`: phase/time-origin alignment as a separate fixed-height control.
- `VIS-419`: exact fixed-shell prime-torus Haar calibration in the infinite-translation limit.
