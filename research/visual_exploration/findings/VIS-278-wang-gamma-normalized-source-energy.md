# VIS-278 — the gamma-normalized fixed-source energy has a classical prime-power variance floor

## Claim

Keep the fixed-source regime and notation of `VIS-276`–`VIS-277`: `H=T^theta` with fixed `0<theta<1`, `I=(T,T+H]`, and Wang's decomposition

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`.

For `x` in any fixed compact `K subset (1,infinity)`, define the normalization-invariant combined-source residual

`R_x(t) := x(B_x(t)+E_x(t)) - log(t/(2*pi)).`

Then uniformly for `x in K` and `t in I`,

`R_x(t) = zeta'/zeta(3/2-it) + O_K(t^-1).`

Consequently,

`(1/H) integral_I R_x(t) dt = O_K(H^-1+T^-1)`,

while its mean square has the nonzero limit

`(1/H) integral_I |R_x(t)|^2 dt = C_Lambda + o_K(1)`,

where

`C_Lambda := sum_(n>=2) Lambda(n)^2/n^3`
`          = sum_p (log p)^2/(p^3-1) > 0.`

The residual is therefore centered in mean but not small in energy. Equivalently,

`(x^2/H) integral_I |B_x(t)+E_x(t)|^2 dt`
` = [log(T/(2*pi))]^2 + C_Lambda + o_K(1).`

Thus, once the classical gamma baseline `log(t/(2*pi))` is removed consistently from the **combined** source, the first normalization-invariant source-energy correction is the classical prime-power constant `C_Lambda`. It is not a new arithmetic invariant and it is not removed by recentering Wang's `B,E` split.

Under the fixed-`q` packet scaling of `VIS-274`–`VIS-277`, this pure source-energy correction enters at order `1/(log T)^2`, not at the larger `1/(log T)^(3/2)` scale still present in the full theorem-level remainder. Hence any genuine `L^(-3/2)` frontier must come from another sector of the full decomposition or from a bound coupling the source to that sector; it cannot be the standalone gamma-normalized `|B+E|^2` energy.

**Evidence/status:** `LITERATURE+DERIVED + EXACT ASYMPTOTIC + CLASSICAL DIRICHLET-MEAN-SQUARE + BOTTLENECK LOCALIZATION + NO-NOVELTY-CLAIM`.

No new mean-value theorem for Dirichlet series, improved pair-correlation theorem, prime-power transfer theorem, or RH implication is claimed.

## 1. The combined source removes the decomposition convention

`VIS-277` reconstructs the signed terms hidden inside Wang's pointwise remainder and obtains, on fixed compact source windows,

`x(B_x(t)+E_x(t))`
` = -zeta'/zeta(-1/2+it) + x P_x(t) + x Q_x(t),`

with

`x P_x(t)+x Q_x(t)=O_K(t^-2).`

The logarithmically differentiated functional equation gives

`-zeta'/zeta(-1/2+it)`
` = log(t/(2*pi)) + zeta'/zeta(3/2-it) + O(t^-1)`

as a complex identity after the standard Stirling expansion of the digamma term; the imaginary constants from the cotangent and digamma pieces cancel, leaving only an `O(t^-1)` complex remainder.

Therefore

`R_x(t)=zeta'/zeta(3/2-it)+O_K(t^-1).`

Unlike Wang's separate `B_x` and `E_x`, this residual is defined from their sum and is invariant under moving an `x^-1` constant from one piece to the other. This is the source interface required by the normalization warning in `VIS-277`.

## 2. The residual mean vanishes on every power-short interval

For `Re(s)=3/2`, absolute convergence gives

`zeta'/zeta(3/2-it)`
` = -sum_(n>=2) Lambda(n) n^(-3/2) exp(it log n).`

For each `n>=2`,

`|integral_T^(T+H) exp(it log n) dt| <= 2/log n.`

Since

`sum_(n>=2) Lambda(n)/(n^(3/2) log n) < infinity,`

termwise integration yields

`(1/H) integral_I zeta'/zeta(3/2-it) dt = O(H^-1).`

The `O_K(t^-1)` reconstruction error contributes `O_K(T^-1)` in mean. Hence

`(1/H) integral_I R_x(t)dt = O_K(H^-1+T^-1)=o(1)`

uniformly on `K`.

This recovers the vanishing mean that `VIS-277` obtained only after its convention-dependent recentering, but now for a convention-independent residual.

## 3. The mean-square limit is a prime-power constant

Put

`a_n = Lambda(n)n^(-3/2)`

and

`Z(t)=zeta'/zeta(3/2-it)=-sum_(n>=2) a_n exp(it log n).`

Because `sum |a_n|<infinity`, the double expansion of `|Z(t)|^2` is absolutely and uniformly summable. Averaging over `I` gives

`(1/H) integral_I |Z(t)|^2 dt`
` = sum_(m,n>=2) a_m a_n exp(i T log(n/m)) K_H(log(n/m)),`

where

`K_H(u)=(exp(i H u)-1)/(i H u)` for `u != 0`, and `K_H(0)=1`.

For `m=n`, the contribution is exactly `sum a_n^2`. For each fixed `m!=n`, `K_H(log(n/m))->0` as `H->infinity`, while `|K_H|<=1`. The dominating double series

`sum_(m,n) |a_m a_n| = (sum_n |a_n|)^2`

is finite. Dominated convergence therefore gives

`(1/H) integral_I |Z(t)|^2 dt -> sum_(n>=2) Lambda(n)^2/n^3.`

The `O_K(t^-1)` error in `R_x-Z` changes this mean square by `O_K(T^-1)+O_K(T^-2)`, because `Z` is uniformly bounded on `Re(s)=3/2`. Thus

`(1/H) integral_I |R_x(t)|^2 dt = C_Lambda+o_K(1).`

Finally, `Lambda(n)` is supported on prime powers, so

`C_Lambda`
` = sum_p sum_(k>=1) (log p)^2 p^(-3k)`
` = sum_p (log p)^2/(p^3-1).`

The constant is finite and strictly positive.

## 4. The gamma baseline is asymptotically orthogonal to the residual

Let

`ell(t)=log(t/(2*pi))`, `ell_T=log(T/(2*pi)).`

From the previous mean estimate,

`ell_T * (1/H) integral_I overline(R_x(t))dt`
` = O_K((log T)/H + (log T)/T).`

Also

`sup_(t in I) |ell(t)-ell_T| = O(H/T)`,

while the absolute convergence above gives a uniform bound for the average absolute size of `R_x`. Hence

`(1/H) integral_I [ell(t)-ell_T] overline(R_x(t))dt = O_K(H/T).`

Because `H=T^theta` with `0<theta<1`, both terms are `o(1)`. Therefore

`(1/H) Re integral_I ell(t) overline(R_x(t))dt = o_K(1).`

Moreover,

`(1/H) integral_I ell(t)^2 dt`
` = ell_T^2 + O((log T)H/T + H^2/T^2)`
` = ell_T^2+o(1).`

Since

`x(B_x+E_x)=ell+R_x`, 

expanding the square proves

`(x^2/H) integral_I |B_x+E_x|^2 dt`
` = ell_T^2 + C_Lambda + o_K(1).`

The `-2 log(2*pi) log T` correction found in `VIS-277` is therefore entirely part of the classical gamma baseline; after that baseline is kept intact, the next source-energy term is the constant `C_Lambda`.

## 5. Fixed-`q` consequence

In the fixed-source coordinate of `VIS-274`, `x=e^(2*pi*q)` with `q` in a compact subset of `(0,infinity)`. A source-energy term

`H C_Lambda/x^2`

is therefore weighted by `e^(-4*pi q)`. Under the same even-test change of variables `d alpha=(2*pi/log T)dq` and the normalization `2*pi/(H log T)`, its contribution is of order

`(log T)^(-2) integral h(q)e^(-4*pi q)dq`

for a fixed smooth packet `h`.

This is one power of `log T` below the deterministic leading source term and below the theorem-level `L^(-3/2)` error scale isolated earlier. The pure combined-source energy is therefore no longer the location of that larger frontier once the gamma baseline has been handled exactly.

This does **not** prove that the full pair-correlation statistic has a universal `C_Lambda/L^2` secondary coefficient. Other pieces of `|A|^2`, their cross terms, and Wang's remaining error estimates can contribute at equal or larger scales. The result only closes the standalone `|B+E|^2` source sector.

## 6. Prior art, stress tests, and novelty boundary

The explicit-formula reconstruction and gamma normalization are the same source bridge already audited in `VIS-277`: Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), together with the Landau explicit-formula reconstruction used there from Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh and the classical zeta functional equation/digamma asymptotic.

The mean-square identity for an absolutely convergent Dirichlet series is classical Parseval/mean-value theory. No general theorem is claimed here: the needed case is proved directly above by absolute convergence and dominated convergence. The equality

`sum Lambda(n)^2/n^3 = sum_p (log p)^2/(p^3-1)`

is the immediate prime-power expansion of the von Mangoldt support.

The compact fixed-source restriction is essential for the stated uniform `O_K(t^-1)` reconstruction. Moving `x=x(T)` may make the explicit pole/trivial-zero terms non-negligible and requires a separate audit.

The residual mean tending to zero must not be confused with its energy tending to zero. In fact the positive constant `C_Lambda` proves the opposite at the mean-square level. Likewise, the positive variance does not imply a lower bound for every signed packet statistic: a packet can still cancel an integrated coefficient after the source-energy kernel has been placed in the full formula.

No untouched confirmation-zero data are used.

## Research consequence

The normalization issue raised by `VIS-277` now has a convention-independent closure for the pure source sector. After subtracting the exact classical gamma baseline, the residual has zero mean but classical prime-power variance `C_Lambda`; its standalone fixed-`q` energy appears only at `L^-2`.

The next coherent frontier is therefore not another recentering or a finer estimate of `|B+E|^2`. It is to identify which non-source interaction produces the still larger `L^-3/2` theorem-level term and determine whether that interaction retains signed structure before Wang's absolute-value majorization. That is a separate mathematical question and should be handled in a later invocation.