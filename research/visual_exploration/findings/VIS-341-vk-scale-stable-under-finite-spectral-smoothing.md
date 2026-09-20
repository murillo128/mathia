# VIS-341 — finite-order truncation gains preserve the Korobov–Vinogradov exponent class

## Claim

Let `A>0` and, for sufficiently large `t`, define a Korobov–Vinogradov zero-free width

`nu(t)=A (log t)^(-2/3) (log log t)^(-1/3)`.

For fixed `r>0`, put `u=log x` and define the weighted zero-free/truncation balance

`Omega_r(u)=inf_(t>=t_0) {u nu(t)+r log t}`.

Then, as `u->infinity`,

`Omega_r(u)`
` ~ C_A r^(2/5) u^(3/5) (log u)^(-1/5)`,

where

`C_A=(5^6 A^3/(2^2 3^4))^(1/5)`.

Equivalently,

`Omega_r(u)/Omega_1(u) -> r^(2/5)`.

Thus any argument that keeps the same Korobov–Vinogradov zero-free width and changes only a **fixed polynomial truncation penalty** from `t^(-1)` to `t^(-r)` can improve the constant in the exponential saving, but cannot change the characteristic

`u^(3/5)(log u)^(-1/5)`

exponent class.

Applied as a control to the accepted Wang source-localization clue, this rules out a specific false mechanism: Wang's one-order high-log-frequency attenuation cannot produce a new subpower envelope class merely by being interpreted as one additional fixed inverse-frequency power in the standard zero-free-region/truncation optimization. A source-specific cancellation or nonstationary mechanism would have to do more than alter that fixed polynomial tail cost.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-ANCHORED + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does **not** prove an improved pointwise bound for Wang's `Q`, does not identify the actual log-frequency distribution of the Chebyshev-theta remainder, and does not assert that Wang's Fourier multiplier may automatically be inserted into a zeta-zero truncation argument as `r=2`. It classifies only the fixed-`r` optimization once such a polynomial tail gain is the admitted mechanism.

## 1. Reduction to one regularly varying minimization

Write

`y=log t`.

Then

`Omega_r(u)=inf_(y>=y_0) {A u y^(-2/3)(log y)^(-1/3)+r y}`.

Let

`V(u)=u^(3/5)(log u)^(-1/5)`

and set `y=c V(u)` with fixed `c>0`. Since

`log(c V(u))=(3/5)log u-(1/5)log log u+O(1)`,

one has, uniformly for `c` in any fixed compact subset of `(0,infinity)`,

`A u y^(-2/3)(log y)^(-1/3)`
` = A (5/3)^(1/3)c^(-2/3) V(u)(1+o(1))`.

Therefore

`[A u y^(-2/3)(log y)^(-1/3)+r y]/V(u)`
` = a c^(-2/3)+r c+o(1)`,

where

`a=A(5/3)^(1/3)`.

The minimizer cannot escape to `c=0` or `c=infinity`: evaluating at any fixed positive `c` gives an `O(V(u))` upper bound; if `y/V(u)->infinity`, the term `r y` alone is supercritical, while if `y/V(u)->0` the zero-free-width term is supercritical (and bounded `y` gives order `u`). Hence the asymptotic minimization reduces to the fixed positive function

`f_r(c)=a c^(-2/3)+r c`.

## 2. The fixed tail order changes only the constant

The unique critical point satisfies

`r=(2/3)a c^(-5/3)`,

so

`c_r=(2a/(3r))^(3/5)`.

At this point,

`r c_r=(2/3)a c_r^(-2/3)`,

and therefore

`min_(c>0) f_r(c)`
` =(5/3)a c_r^(-2/3)`
` =(5^6 A^3 r^2/(2^2 3^4))^(1/5)`.

This yields

`Omega_r(u)`
` ~ (5^6 A^3 r^2/(2^2 3^4))^(1/5)`
`    u^(3/5)(log u)^(-1/5)`.

In particular, every fixed `r` leaves the powers `3/5` and `-1/5` unchanged. Relative to the baseline `r=1`, a fixed extra inverse-frequency order changes only the leading exponential constant by `r^(2/5)`. For example, replacing a `t^(-1)` truncation penalty by `t^(-2)` would multiply this optimized constant by `2^(2/5)`, not produce a new asymptotic envelope shape.

## 3. Relation to the optimal PNT balance

Bellotti's current optimal PNT error formulation uses exactly

`omega(x)=min_(t>=1) {nu(t) log x+log t}`,

with Korobov–Vinogradov width

`nu(t)=A_0(log t)^(-2/3)(log log t)^(-1/3)`.

Thus `omega(x)=Omega_1(log x)` in the notation above. Johnston's earlier generic zero-free-region analysis gives the corresponding explicit Korobov–Vinogradov exponent constant; after identifying `A=1/c`, its constant is exactly the `r=1` specialization of the formula derived here. The present `r`-dependence is only the elementary fixed-weight extension of that classical optimization, not a new PNT theorem.

This also clarifies what a finite-order smoother can and cannot buy under an **absolute truncation** interpretation. If the same zero-free width is retained and the only new input is a fixed additional polynomial decay in the spectral/height tail, then the optimization remains in the same regular-variation class. To change the powers in the exponent one needs a genuinely different zero-free width, a non-polynomial tail mechanism whose order itself grows, or source-specific cancellation that is not captured by the absolute balance `u nu(t)+r log t`.

## 4. Consequence for the Wang frequency-migration branch

`VIS-333` shows that Wang's exact summatory-remainder transfer has multiplier

`m(xi)=4(1+i xi)/(4+xi^2)`,

so `|m(xi)|~4/|xi|` at high log-frequency and no finite real frequency is annihilated. `VIS-334`--`VIS-340` then show that generic high-frequency attenuation is accompanied by derivative repayment and that the actual prime and square-log source descriptions quotient back to the same normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

The accepted clue still allows genuine source-envelope-scale frequency migration in `G`. The present result removes a weaker interpretation of that phrase. If the proposed migration does nothing more than push the standard Korobov–Vinogradov cutoff to higher frequencies while Wang contributes a fixed finite number of inverse-frequency powers, then the best optimized exponent remains

`Theta(u^(3/5)(log u)^(-1/5))`.

That mechanism can at most improve an exponential constant. It cannot by itself explain a new subpower class for `Q`, let alone a power saving or an RH-strength consequence.

A surviving source mechanism must therefore be visible after quotienting through `VIS-339` and `VIS-340` **and** must exploit more than the classical zero-free-width versus polynomial-tail balance: for example a genuinely arithmetic signed cancellation, a nonstationary concentration statement with stronger information than the known PNT envelope, or another effect whose gain is not equivalent to replacing fixed `r` by another fixed constant.

## 5. Prior art and evidence boundary

The zero-free-region/PNT optimization is prior art. Chiara Bellotti, **A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem**, arXiv:2508.02041 (2025), gives the optimal form

`psi(x)-x << x exp(-omega(x))`,

with

`omega(x)=min_(t>=1){nu(t)log x+log t}`

for the Korobov–Vinogradov zero-free width above. Daniel R. Johnston, **Zero-density estimates and the optimality of the error term in the prime number theorem**, arXiv:2411.13791 (2024), gives the corresponding explicit `3/5,1/5` exponent and constant for a generic Korobov–Vinogradov region. These sources establish the `r=1` analytic-number-theory boundary.

The extension to arbitrary fixed `r>0` here is an elementary one-variable asymptotic minimization included only to test the Wang clue's proposed frequency-migration escape. No novelty is claimed for regular-variation optimization, smoothed explicit-formula methods, or the general fact that zero-free regions control PNT errors.

Crucially, this finding does not establish that Wang's actual multiplier changes Bellotti's truncation factor from `t^(-1)` to `t^(-2)`, nor that the constant `2^(2/5)` is attained in Wang's statistic. Such a claim would require an exact zero-side representation and complete destination error audit. The proved statement is narrower: **any fixed polynomial change of truncation order leaves the Korobov–Vinogradov exponent class unchanged.**

## Dependencies

- `VIS-291`: records the Korobov–Vinogradov PNT envelope propagated through Wang's compact fixed-power statistic.
- `VIS-333`: gives Wang's exact nonvanishing one-order log-frequency multiplier.
- `VIS-334`--`VIS-336`: establish generic derivative repayment for high and migrating frequencies.
- `VIS-339`--`VIS-340`: quotient the surviving prime and squared-log summatory sources back to the Chebyshev-theta remainder.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose remaining source branch asks whether genuine theta-remainder nonstationarity can beat the generic controls.

## Research consequence

The accepted Wang clue narrows again. **Generic Korobov–Vinogradov frequency migration plus any fixed finite amount of polynomial spectral smoothing cannot change the unconditional subpower exponent class.** It may improve constants, but the `3/5,-1/5` shape survives exactly.

The next useful test should therefore not ask merely whether the theta remainder's effective frequency drifts upward. It must identify a quantitative property of `G` whose gain is not reducible to the standard zero-free-region/truncation balance with another fixed tail exponent, and then verify that Wang's complete destination does not repay that gain through `Q'` or equivalent unsmoothed information. That is a separate research question and is not pursued further in this invocation.
