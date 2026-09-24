# VIS-427 — normalized growing-window path averages pay no radius tariff

## Claim

Continue the Laurent-polynomial notation of `VIS-423`--`VIS-425`. Let

`F_N(z)=sum_(a in S_N) b_(N,a) z^a`,

`S_N=||F_N||_infinity`,

`W_N=(sum_a |b_(N,a)|)/S_N`,

`Omega_N=max_a |lambda_a|`,

and

`X_(N,u)(z)=|F_N(z tau(u))|^2/S_N^2 in [0,1]`.

For an arbitrary positive path radius `rho_N>0` and a fixed integer `q>=1`, define the normalized path-power average

`J_(N,q)(z)=(1/(2 rho_N)) integral_(-rho_N)^(rho_N) X_(N,u)(z)^q du in [0,1]`.

For each fixed integer `m>=1`, let `delta^*_(N,qm)` be the structural mixed divisor from `VIS-425`: the smallest nonzero magnitude of a sum of `qm` frequency differences `lambda_a-lambda_c`, with `+infinity` if no nonzero value occurs.

Then the dyadic Gram-block moment discrepancy satisfies

`| (1/N) sum_(N<k<=2N) J_(N,q)(z(g_k))^m - int J_(N,q)(z)^m dm_H(z) |`

`<= C W_N^(2qm) [ 1/N + 2qm Omega_N/log N + (log N)/(N delta^*_(N,qm)) ]`,

with the same absolute constant type as `VIS-423`.

In particular, **the path radius `rho_N` contributes no additional tariff at all** to normalized path averages, even when `rho_N->infinity`. If for every fixed `m`

`W_N^(2qm) [ 1/N + qm Omega_N/log N + (log N)/(N delta^*_(N,qm)) ] -> 0`,

then for every fixed continuous `phi:[0,1]->C`,

`(1/N) sum_(N<k<=2N) phi(J_(N,q)(z(g_k))) - int phi(J_(N,q)(z)) dm_H(z) -> 0`.

For a fixed threshold `t in (0,1)`, the corresponding Gram and Haar tail probabilities also agree when the Haar pushforwards of `J_(N,q)` satisfy the usual uniform boundary-mass condition at `t`.

**Evidence/status:** `EXACT-DERIVED + QUANTITATIVE CONTROL + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

This result concerns normalized path averages, not path suprema. It gives no RH consequence and does not prove that the actual Wang family satisfies the displayed tariffs.

## 1. The window volume cancels exactly

For fixed `m`, Fubini gives

`J_(N,q)(z)^m`

`= (2 rho_N)^(-m) integral_([-rho_N,rho_N]^m) product_(j=1)^m X_(N,u_j)(z)^q du_1...du_m`.

For every fixed offset tuple `(u_1,...,u_m)`, the integrand is a mixed shifted monomial of total degree `qm`. As in `VIS-425`, the shifts only rephase coefficients; they do not change the character support. Therefore its Wiener norm is at most

`W_N^(2qm)`,

its character frequencies have magnitude at most

`2qm Omega_N`,

and every nonzero structural frequency has magnitude at least

`delta^*_(N,qm)`.

Applying `VIS-423` to this integrand gives, uniformly over the entire offset box,

`|G_N(P_u)-H(P_u)|`

`<= C W_N^(2qm) [ 1/N + 2qm Omega_N/log N + (log N)/(N delta^*_(N,qm)) ]`,

where `G_N` is the dyadic Gram-block average and `H` is Haar average on the relevant prime torus.

Integrate this uniform inequality over the offset box and multiply by `(2 rho_N)^(-m)`. The volume `(2 rho_N)^m` cancels exactly. No mesh, covering number, or fixed-radius assumption appears.

The cancellation is the substantive point: a larger path window supplies proportionally more offset tuples, but `J_(N,q)` averages rather than maximizes over them.

## 2. Scalar moment closure survives a growing window

The variable `J_(N,q)` always lies in `[0,1]`, regardless of `rho_N`. Under the fixed-`m` tariffs in the claim, every fixed moment of its Gram empirical law converges to the corresponding moment of its own Haar pushforward law.

For a fixed polynomial `p(x)=sum_(m=0)^M c_m x^m`, the difference of Gram and Haar expectations is therefore `o(1)`. Ordinary Weierstrass approximation on the fixed scalar interval `[0,1]` then gives the same conclusion for every fixed continuous `phi`.

As in `VIS-424`, a discontinuous threshold indicator needs one extra condition: the Haar laws must not accumulate increasing mass in shrinking neighborhoods of the chosen threshold. No new high-dimensional torus approximation is needed.

This remains true when `rho_N` grows arbitrarily fast. The only changing-family costs visible to the argument are still the normalized Wiener mass, outer frequency scale, and fixed-order structural small divisors.

## 3. Why this does not close growing-radius persistence

Let

`A_N(z,u)=|F_N(z tau(u))|/S_N`,

and

`Q_(N,rho_N)(z)=sup_(|u|<=rho_N) A_N(z,u)`.

Bernstein's inequality gives the pointwise Lipschitz bound

`|partial_u A_N(z,u)| <= Omega_N`

whenever `Omega_N>0`; the zero-bandwidth case is constant in `u`.

If `Q_(N,rho_N)(z)>=t>0`, choose a maximizing point `u_0`. On at least one side inside the path interval, `A_N` remains at least `t/2` for a length

`ell >= min(t/(2 Omega_N), 2 rho_N)`.

Hence

`J_(N,q)(z)`

`>= (t/2)^(2q) min(t/(2 Omega_N),2 rho_N)/(2 rho_N)`.

When `rho_N Omega_N->infinity`, this deterministic lower bound shrinks like `1/(rho_N Omega_N)`. A fixed-height supremum spike can therefore occupy a vanishing fraction of a long path window and disappear from every fixed positive threshold on the normalized average.

So the present result removes **growing path length by itself** as an escape for normalized path-average diagnostics, but it does not remove genuinely localized persistence/supremum effects. The remaining distinction is no longer simply `fixed radius` versus `growing radius`; it is **averaged path mass versus concentration on a vanishing relative subset of the path**.

## 4. Prior art and novelty audit

For a fixed finite exponential or Laurent polynomial, translation averages and their torus interpretation lie in classical Bohr almost-periodic/Kronecker-flow theory. `VIS-423` already records the Gram-point equidistribution prior art and supplies the quantitative triangular-array character estimate used here; `VIS-425` already records the Bernstein inequality used for the final localization boundary.

No new external theorem is needed in this finding. The moment identity is Fubini plus the uniform mixed-character tariff from `VIS-423`, and the continuous-test step is the same scalar polynomial approximation used in `VIS-424`. A targeted literature orientation found the surrounding fixed-function averaging picture to be classical, so no novelty is claimed for path averaging, almost-periodicity, Fubini, moment methods, or Bernstein localization.

The Mathia-specific delta is only the exact observation that **normalizing by path length cancels the entire growing-window volume inside the current Gram/Wang tariff**, thereby separating long-window averaging from long-window supremum persistence.

## 5. Boundaries and falsification

The theorem is sufficient, not necessary. Failure of one displayed tariff does not imply a Gram anomaly.

The path-power exponent `q` is fixed. Allowing `q=q_N->infinity` in order to approximate a supremum would make the required moment order grow and is not covered by the fixed-order argument.

The normalization by `2 rho_N` is essential. For the unnormalized path integral, the offset-box volume no longer cancels in its moments; powers of `rho_N` reappear.

The result does not establish a fixed-threshold low-tail statement without uniform Haar boundary control. It also does not turn a normalized path average into a substitute for a supremum when `rho_N Omega_N` grows.

Falsify the derivation by exhibiting an offset tuple for which the shifted mixed monomial has Wiener mass above `W_N^(2qm)`, a frequency outside the `2qm Omega_N` envelope, a nonzero structural frequency below `delta^*_(N,qm)`, a failure of the normalized Fubini identity, or a continuous scalar test on `[0,1]` not controlled by the fixed moments under the stated tariffs.

## Dependencies

- `VIS-423`: quantitative dyadic Gram-block character tariff.
- `VIS-424`: scalar moment closure for normalized amplitude.
- `VIS-425`: uniform shifted-character bookkeeping and Bernstein path control.

## Research consequence

For the accepted Wang phase-anchored small-value question, a path statistic based on a **normalized average of any fixed power of amplitude cannot escape the Gram/Haar self-null merely by letting the observation radius grow**. It pays exactly the same fixed-order Wiener/frequency/small-divisor resources as the corresponding mixed amplitude moments.

A genuinely new growing-path escape must therefore exploit something the normalized average can miss: concentration into a vanishing relative part of the path, a supremum or threshold functional sensitive to such localization, a moment order that itself grows, or a quantified failure of the existing Wang character tariffs. This sharpens the remaining persistence question without assuming any unsupported cross-line source bound.