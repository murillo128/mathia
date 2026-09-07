# VIS-086 — quadratic Gram-arc subtraction extends the deterministic-null corridor

## Claim

Let `g_n` be the Gram points, defined for all sufficiently large `n` by

`theta(g_n)=pi n`,

up to the harmless conventional integer shift. Put

`a_n=theta'(g_n)`,
`b_n=theta''(g_n)`,
`x_h=pi h`,
`Delta_(n,h)=g_(n+h)-g_n`.

For any integer sequence `H_n>=0`, any prime cutoff `P_n>=2`, and every `0<=h<=H_n`, define the prime-phase residual after subtracting the second-order inverse-theta Gram arc by

`Q_(n,h)(p)`
` = exp(-i log p [Delta_(n,h)-x_h/a_n+b_n x_h^2/(2 a_n^3)])`,

for primes `p<=P_n`.

Then, for all sufficiently large `n`, uniformly over the whole block and all admitted primes,

`max_(h<=H_n) max_(p<=P_n) |Q_(n,h)(p)-1|`
` << H_n^3 log P_n / [g_n^2 (log g_n)^4]`.

Consequently, whenever

`H_n^3 log P_n = o(g_n^2 (log g_n)^4)`,

the quadratically corrected prime-phase field collapses uniformly to the identity.

For fixed prime support this includes every

`H_n=o(g_n^(2/3) (log g_n)^(4/3))`,

while for polynomial support `P_n<=g_n^A` with fixed `A` it includes every

`H_n=o(g_n^(2/3) log g_n)`.

Thus the first corridor left open by the linear Gram-arc control in `VIS-085` is still deterministic sampling geometry: adding the exact quadratic inverse-theta correction pushes the coordinatewise null from square-root scale to two-thirds-power scale for polynomial prime support.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-RIEMANN-SIEGEL-ASYMPTOTICS COROLLARY + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No higher-order optimality statement, long-block equidistribution theorem, zeta-approximation theorem, prime/zero independence statement, or RH consequence is claimed.

## 1. Classical derivative scales

The standard Riemann-Siegel theta expansion gives, as `t->infinity`,

`theta'(t) = (1/2) log(t/(2 pi)) + O(t^(-2))`,
`theta''(t) = 1/(2t) + O(t^(-3))`,
`theta'''(t) = -1/(2t^2) + O(t^(-4))`.

Hence for all sufficiently large `g=g_n`, with `a=theta'(g)` and `b=theta''(g)`,

`a asymp log g`,
`0<b<<1/g`,
`sup_(t>=g) |theta'''(t)| << 1/g^2`.

The first two estimates are the inputs already used in `VIS-085`; the third derivative is the next classical term needed to control the quadratic inverse expansion.

## 2. Second-order inversion with a global one-sided gap bound

Fix `h>=0`, write `x=pi h`, and put `Delta=Delta_(n,h)`. Since `theta'` is eventually positive and increasing,

`0<=Delta<=x/a`.

Define the first-order inverse error

`d = x/a-Delta`.

The integral Taylor identity used in `VIS-085` gives

`x-a Delta = integral_0^Delta (Delta-u) theta''(g+u) du`,

and therefore

`0<=d<<Delta^2/(g a)<<x^2/(g a^3)`.

Now freeze the quadratic coefficient at the block origin. By the third-derivative bound,

`integral_0^Delta (Delta-u) theta''(g+u) du`
` = b Delta^2/2 + E_3`,

with

`|E_3| << Delta^3/g^2`.

Thus

`d = b Delta^2/(2a) + E_3/a`.

Let

`q = x/a - b x^2/(2a^3)`

be the second-order inverse-theta approximation. Then

`Delta-q`
` = b x^2/(2a^3)-d`
` = [b/(2a)] [(x/a)^2-Delta^2] - E_3/a`
` = [b/(2a)] d (x/a+Delta) - E_3/a`.

Using `Delta<=x/a`, the first-order bound for `d`, `b<<1/g`, and `|E_3|<<Delta^3/g^2` yields

`|Delta-q|`
` << x^3/(g^2 a^5) + x^3/(g^2 a^4)`
` << h^3/[g^2 (log g)^4]`.

This estimate, like the strengthened `VIS-085` bound, does not require an a priori local restriction such as `H_n=O(log g_n)`. It is a global deterministic upper bound whose usefulness is determined by the displayed scale ratio.

## 3. Prime support multiplies only the second-order clock remainder

For real `y`, `|e^(-iy)-1|<=|y|`. Therefore, for every prime `p<=P_n`,

`|Q_(n,h)(p)-1|`
` <= log p |Delta_(n,h)-x_h/a_n+b_n x_h^2/(2a_n^3)|`
` << h^3 log P_n/[g_n^2 (log g_n)^4]`.

Taking maxima over `h<=H_n` and the admitted prime support proves the claim.

Equivalently, the empirical block of second-order-corrected prime-phase vectors converges to a point mass in the sup chord metric whenever

`H_n^3 log P_n=o(g_n^2(log g_n)^4)`.

For polynomial support, `log P_n=O(log g_n)`, so the condition reduces to

`H_n^3=o(g_n^2(log g_n)^3)`,

or `H_n=o(g_n^(2/3) log g_n)`.

## 4. What this closes and what it does not

`VIS-084` identifies the first visible local Gram motion; `VIS-085` shows that subtracting the linear inverse-theta arc removes the sampling-clock residual throughout

`H_n^2 log P_n=o(g_n(log g_n)^3)`.

The present result shows that the boundary of that estimate is not a natural positive transition. A deterministic quadratic correction extends the collapse corridor to

`H_n^3 log P_n=o(g_n^2(log g_n)^4)`.

For polynomial support this moves the admissible block scale from `o(sqrt(g_n) log g_n)` to `o(g_n^(2/3) log g_n)`. Any apparent Gram/prime-phase geometry inside the larger corridor that disappears under this correction is therefore sampling-clock curvature, not a new arithmetic channel.

The result does **not** prove that the quadratic corridor is sharp. Higher inverse-theta terms may extend the deterministic null further, and the asymptotic inversion itself strongly suggests that finite-order corrections form a hierarchy. Establishing a general `k`-th order corridor is a separate question and is not folded into this finding.

Nor does coordinatewise phase collapse imply growing-dimensional Haar behavior, control arbitrary scalar observables with dimension-dependent Lipschitz constants, approximate zeta by the admitted prime support, or remove information in `Z(g_n)`, zero locations, Gram occupancy, derivatives, or another independently supplied analytic coordinate.

## Prior art and novelty assessment

The Riemann-Siegel theta asymptotic expansion and controlled remainder theory are classical. Richard P. Brent, **On the Accuracy of Asymptotic Approximations to the Log-Gamma and Riemann-Siegel Theta Functions**, *Journal of the Australian Mathematical Society* 107:3 (2019), 319-337, DOI `10.1017/S1446788718000393`, gives rigorous error bounds for theta asymptotics. R. B. Paris, **Refined asymptotics of the Riemann-Siegel theta function**, *Bulletin of Kerala Mathematics Association* 16:2 (2020), 17-27, develops the refined large-`t` expansion.

Gram points themselves are classically obtained by inverting `theta(g_n)=pi n`, and coarse Lambert-`W` inversion is standard. The second-order inverse coefficient used here is the ordinary Taylor/inverse-function coefficient specialized to the Gram clock.

A targeted search around Gram-point spacing, theta inversion, and higher-order asymptotics found no basis for presenting the displayed estimate as a new general theorem. **No novelty is claimed for the analytic inversion bound.** The durable Mathia contribution is its use as a stronger null boundary: a visually plausible residual just beyond the linear-arc corridor is still explained by deterministic Gram-clock geometry.

## Boundary and falsification

The collapse conclusion requires

`H_n^3 log P_n=o(g_n^2(log g_n)^4)`.

Outside this corridor the bound merely stops forcing convergence; it gives no lower bound and no evidence that a residual survives. A higher-order inverse-theta control may push the boundary farther.

Falsify the claim by breaking the classical derivative asymptotics, eventual monotonicity used for `Delta<=x/a`, the integral Taylor remainder estimate, the algebraic second-order inversion step, or the elementary phase chord inequality.

A proposed positive Gram/prime-phase separator inside the displayed corridor must demonstrate information not removed by the quadratic sampling null. Beyond the corridor it must first establish the correct higher-order or nonlocal Gram-sampling control before interpreting residual visual structure.

## Visual consequence

No canonical PNG is retained. The exact uniform second-order remainder bound is a stronger control than a finite-height rendering, and plotting the small residual without its scale normalization could create precisely the false positive this finding rules out.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should be narrowed again. Merely moving beyond the linear `VIS-085` corridor does not create a candidate separator: for polynomial prime support, deterministic Gram-clock geometry remains removable through every block with `H_n=o(g_n^(2/3) log g_n)` after quadratic inverse-theta correction.

A surviving Gram/prime-phase route must either operate beyond the quadratic corridor and derive the appropriate higher-order/nonlocal null, or add an observable/source coordinate whose information is not determined by the prime phases and the Gram sampling clock.