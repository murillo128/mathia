# VIS-277 — Wang's fixed-source remainder mean is the classical `-log(2*pi)` normalization constant

## Claim

Keep the notation and fixed-source regime of `VIS-276`: `H=T^theta` with fixed `0<theta<1`, `I=(T,T+H]`, and Wang's decomposition

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`,

with

`B_x(t)=log(t+2)/x`.

For every compact `K subset (1,infinity)`, uniformly for `x in K`, the signed mean isolated in `VIS-276`,

`M_T(x) := (x/H) Re integral_I E_x(t) dt`,

has the asymptotic

`M_T(x) = -log(2*pi) + O_K(H^-1 + T^-1)`.

In particular,

`M_T(x) -> -log(2*pi)`,

not `0`, on every fixed source window `x=e^(2*pi*q)` with `q` in a compact subset of `(0,infinity)`.

The constant is not a new arithmetic effect. It is the classical gamma-factor normalization already visible in `log(t/(2*pi))`. If one recenters Wang's decomposition by defining

`B_x^*(t) = [log(t+2)-log(2*pi)]/x`,

`E_x^*(t) = E_x(t)+log(2*pi)/x`,

then

`A(x,t)=-D_x(t)+B_x^*(t)+E_x^*(t)`

and the recentered mean satisfies

`M_T^*(x):=(x/H) Re integral_I E_x^*(t)dt = O_K(H^-1+T^-1)=o(1)`.

However, this recentering does **not** remove a normalization-invariant `1/log T` source correction. It merely moves the same constant from the `B,E` cross term into `|B^*|^2`, since with `L=log T` and `c=log(2*pi)`,

`H(L-c)^2/x^2 = H L^2/x^2 - 2c H L/x^2 + O(H/x^2)`.

Thus the open `M_T=o(1)` branch in `VIS-276` is resolved for Wang's original remainder convention: the mean remainder has a nonzero classical limit, while the recentered remainder has vanishing mean. Any further attempt to improve the fixed-source expansion must therefore be phrased in a normalization-invariant way, keeping the full source `B_x+E_x` (or equivalently accounting explicitly for the `log(2*pi)` shift).

**Evidence/status:** `LITERATURE+DERIVED + EXACT ASYMPTOTIC + CLASSICAL-NORMALIZATION + BOTTLENECK RESOLUTION + NO-NOVELTY-CLAIM`.

No secondary pair-correlation theorem, improved global error term, prime-power transfer, or RH implication is claimed.

## 1. Recover the signed remainder before Wang takes the pointwise envelope

Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh derive the explicit formula used by Wang from Landau's identity. At `sigma=3/2`, keeping the terms that are compressed into Wang's `E_x` gives

`A(x,t)+D_x(t)`
` = -x^-1 zeta'/zeta(-1/2+it) + P_x(t) + Q_x(t)`,

where the pole contribution can be written

`P_x(t)=x^(1/2-it) [1/(1/2+it)+1/(3/2-it)]`

and the trivial-zero contribution is

`Q_x(t)=sum_(m>=1) x^(-2m-1/2-it)`
`  * [1/(2m-1/2+it)-1/(2m+3/2+it)].`

For `x` in a fixed compact subset of `(1,infinity)`, the denominator cancellations give

`P_x(t)=O_K(t^-2)`, `Q_x(t)=O_K(t^-2)`.

Since Wang defines `B_x(t)=log(t+2)/x`, it follows that

`x E_x(t)`
` = -zeta'/zeta(-1/2+it) - log(t+2)`
`   + x P_x(t) + x Q_x(t).`

This is the signed structure hidden by the coarser pointwise statement `E_x(t)=O(1/x)` used in Proposition 2.6.

The formulas above are first obtained away from prime-power values of `x` in the usual Landau explicit formula. The resulting `A+D` expression extends to fixed `x>1` by the same continuous limiting interpretation used by the smoothed `min(n/x,x/n)` coefficient; the asymptotic claim here only needs compact fixed-source windows.

## 2. The functional equation exposes `-log(2*pi)`

The zeta functional equation gives, after logarithmic differentiation,

`-zeta'/zeta(s)`
` = -log(2*pi) - (pi/2) cot(pi s/2)`
`   + psi(1-s) + zeta'/zeta(1-s).`

At `s=-1/2+it`, the standard digamma asymptotic and the exponentially small real part of the cotangent term imply

`Re[-zeta'/zeta(-1/2+it)]`
` = log t - log(2*pi)`
`   + Re[zeta'/zeta(3/2-it)] + O(t^-2).`

Consequently,

`x Re E_x(t)`
` = -log(2*pi) + Re[zeta'/zeta(3/2-it)]`
`   + [log t-log(t+2)] + O_K(t^-2)`

and therefore

`x Re E_x(t)`
` = -log(2*pi) + Re[zeta'/zeta(3/2-it)] + O_K(t^-1).`

The appearance of `2*pi` is exactly the familiar normalization from the zeta functional equation and the Riemann-von Mangoldt main term. It is not evidence of a new source-side arithmetic invariant.

## 3. The remaining Dirichlet-series term averages away

On `Re(s)=3/2`, the logarithmic derivative has the absolutely convergent Dirichlet series

`zeta'/zeta(3/2-it)`
` = -sum_(n>=2) Lambda(n) n^(-3/2+it).`

Termwise integration is therefore legitimate. For every `n>=2`,

`|(1/H) integral_T^(T+H) exp(it log n) dt| <= 2/(H log n)`.

Hence

`|(1/H) integral_I zeta'/zeta(3/2-it) dt|`
` <= (2/H) sum_(n>=2) Lambda(n)/(n^(3/2) log n)`
` = O(H^-1).`

Averaging the `O_K(t^-1)` remainder over `I` contributes `O_K(T^-1)`. Combining the two estimates gives

`M_T(x)`
` = (1/H) integral_I x Re E_x(t) dt`
` = -log(2*pi) + O_K(H^-1+T^-1).`

Because `H=T^theta`, both error terms tend to zero for every fixed `theta>0`. This proves the claimed compact fixed-source asymptotic.

## 4. Recentring resolves the remainder mean but not the full source correction

Set `c=log(2*pi)` and move the constant from the remainder into the explicit source term:

`B_x^*=B_x-c/x`, `E_x^*=E_x+c/x`.

Then the decomposition of `A` is unchanged, while

`M_T^*(x)=M_T(x)+c=O_K(H^-1+T^-1)`.

So `VIS-276` did identify a signed quantity that can be sharpened far below its pointwise `O(1)` envelope, but its literal target `M_T=o(1)` is not the property of Wang's original convention. It becomes true only after the classical gamma-factor normalization is placed in `B_x^*`.

This distinction matters because `B` and `E` are not separately invariant. Expanding the recentered explicit term gives

`integral_I |B_x^*(t)|^2 dt`
` = H(L-c)^2/x^2 + O_K(L H^2/T + H^3/T^2)`
` = H L^2/x^2 - 2c H L/x^2 + O_K(H/x^2 + L H^2/(T x^2)).`

The `-2c H L/x^2` term is exactly at the source scale that becomes `1/L` after the fixed-source normalization. Under Wang's original split, the same constant appears through the `B,E` cross term. Moving it between the two pieces cannot improve the full statistic.

Therefore the meaningful next object is not the mean of an arbitrarily normalized `E_x` in isolation. It is the first correction of the combined source `B_x+E_x`, with the classical `log(t/(2*pi))` normalization removed once and consistently.

## 5. Stress tests and boundaries

The statement is uniform only on compact fixed-source windows `K subset (1,infinity)`, exactly the regime corresponding to compact `q` support away from `q=0`. It does not analyze moving source windows where `x` grows with `T`.

Only the real mean of `E_x` is evaluated because that is the quantity entering the `B,E` cross term isolated in `VIS-276`. No claim is made that `E_x` itself converges pointwise or in complex mean to a real constant.

The result also does not by itself give the complete secondary expansion of Wang's Proposition 2.6. The `D_x,E_x` interaction and the other already exposed source terms remain separate, and the normalization of the final pair-correlation statistic must be made consistent with the same `log(T/(2*pi))` scale before any coefficient is interpreted as new arithmetic structure.

Most importantly, the constant is convention-sensitive while the full source is not. A future finding must not report disappearance of the `1/L` correction merely because `M_T^*=o(1)` after recentering.

## 6. Prior-art and novelty boundary

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), equations (2.7)–(2.9) and Proposition 2.6. Wang records `B_x(t)=log(t+2)/x` and uses only the pointwise envelope for `E_x` at the stage relevant here.

The signed reconstruction uses the Landau explicit formula in Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), Lemma 1 and its proof. The zeta reflection formula and the digamma asymptotic are classical; authoritative standard forms are DLMF §25.4 and §5.11.

The constant `log(2*pi)`, the `log(t/(2*pi))` normalization, logarithmic differentiation of the functional equation, and averaging an absolutely convergent Dirichlet series are all classical. No novelty is claimed for any of them. The durable Mathia result is the exact resolution of the specific open source quantity created by `VIS-276` and the accompanying control against mistaking a decomposition-dependent recentering for an improvement of the full fixed-source statistic.

## Research consequence

The `VIS-276` source-side question is no longer to prove cancellation of Wang's original `M_T(x)` to zero: its fixed-source limit is the classical constant `-log(2*pi)`.

The next coherent step is to rewrite the fixed-source source contribution with `log(t/(2*pi))` treated as the explicit baseline and determine the first **normalization-invariant** unresolved correction after that deterministic `1/L` term has been accounted for. Only then is it meaningful to ask whether the next exposed scale, including the `L^-3/2` terms already visible in `VIS-275`, contains cancellable or arithmetic structure.

No untouched confirmation-zero data are used.
