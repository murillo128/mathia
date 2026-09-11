# VIS-165 — prime-log collision controls admit a polynomial discrepancy regime

## Claim

Keep the notation of `VIS-164`. Let

`P={p_0,p_1,...,p_d}`

be a finite retained set of distinct rational primes with `d>=1`, let `r` be a prime not in `P`, and write

`theta=(alpha_1,...,alpha_d,beta)`

with

`alpha_j=log p_j/log p_0`, `beta=log r/log p_0`.

For the anchored collision scores

`C_q = |sin(pi q beta)| / sqrt(sum_(j=1)^d sin^2(pi q alpha_j))`,

put

`F_Q(L)=Q^(-1) #{1<=q<=Q : C_q>L}`

and let `mu_d(L)` be the Haar exceedance law from `VIS-164`.

Then there exists an exponent `delta=delta(P,r)>0` such that the star discrepancy `D_Q^*` of the Kronecker sequence `q theta mod 1` satisfies

`D_Q^* = O_(P,r)(Q^(-delta))`.

Consequently, uniformly for `L>=1`,

`|F_Q(L)-mu_d(L)|`
` <= C_(P,r,d) Q^(-delta/(2d+3)) (1+L)^((2d+2)/(2d+3))`.

In particular, if `L(Q)=Q^gamma` with

`0 < gamma < delta/(2d^2+5d+2)`,

then

`F_Q(L(Q)) ~ c_d Q^(-d gamma)`,

where `c_d` is the explicit Haar-tail constant in `VIS-164`. Hence for every such `gamma`, eventually

`max_(1<=q<=Q) C_q > Q^gamma`.

Equivalently, the finite-window held-out-prime Lipschitz control from `VIS-163` has a genuine positive-power lower bound along the anchored windows: with `T_Q=pi Q/log p_0`,

`Lambda_P(A_r;[-T_Q,T_Q]) >= Q^gamma`

for all sufficiently large `Q` and every fixed `gamma` below the displayed threshold.

**Evidence/status:** `LITERATURE+DERIVED + QUANTITATIVE-MATCHED-NULL + NO-NOVELTY-CLAIM`.

The exponent `delta(P,r)` supplied here is only an existence/effectivity consequence of classical lower bounds for linear forms in logarithms plus discrepancy theory. No useful numerical value is claimed, and this is not an extreme-value law, a Poisson law, a zeta theorem, or an RH consequence.

## 1. Prime-log vectors are of finite Diophantine type

Let `m=d+1`, and let the coordinates of `theta` correspond to the primes

`a_1,...,a_m = p_1,...,p_d,r`.

For any nonzero integer vector `h=(h_1,...,h_m)`, choose `n in Z` nearest to `h dot theta`. Then

`Lambda = (h dot theta - n) log p_0`
`       = sum_(j=1)^m h_j log a_j - n log p_0`.

This linear form is nonzero. Otherwise exponentiation would give a multiplicative relation among distinct rational primes, contradicting unique factorization.

Moreover `|n|=O_(P,r)(||h||_infinity)`, so the largest integer coefficient in `Lambda` is `O_(P,r)(||h||_infinity)`. Matveev's explicit lower-bound theorem for nonzero homogeneous rational linear forms in logarithms of algebraic numbers therefore gives constants `A,c>0`, depending only on the fixed prime set, such that

`|Lambda| >= c ||h||_infinity^(-A)`.

Dividing by `log p_0` yields

`||h dot theta|| >= c' ||h||_infinity^(-A)`.

Thus the anchored prime-log rotation vector is of finite Diophantine type. This is stronger than the qualitative rational independence used in `VIS-164`.

The external input is classical. A suitable explicit source is E. M. Matveev, **An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II**, *Izvestiya: Mathematics* 64:6 (2000), 1217--1269, DOI `10.1070/IM2000v064n06ABEH000314`. No new linear-forms theorem is claimed here.

## 2. Erdős--Turán--Koksma gives polynomial star discrepancy

For the Kronecker points

`x_q = q theta mod 1`, `1<=q<=Q`,

the multidimensional Erdős--Turán--Koksma inequality bounds star discrepancy by

`D_Q^* <= C_m [ H^(-1) + sum_(0<||h||_infinity<=H) r(h)^(-1) |Q^(-1) sum_(q<=Q) exp(2 pi i q h dot theta)| ]`,

where `r(h)=prod_j max(1,|h_j|)`.

The normalized geometric sum obeys

`|Q^(-1) sum_(q<=Q) exp(2 pi i q h dot theta)|`
` <= min(1, C/(Q ||h dot theta||))`
` <= C Q^(-1) ||h||_infinity^A`.

Also

`sum_(0<||h||_infinity<=H) r(h)^(-1) = O_m((log H)^m)`.

Therefore

`D_Q^* <= C [ H^(-1) + Q^(-1) H^A (log H)^m ]`.

Choosing `H` as a small power of `Q` gives

`D_Q^* = O_(P,r)(Q^(-delta))`

for some `delta>0`. For example, the displayed estimate gives every exponent strictly below `1/(A+1)` after absorbing the logarithmic factor.

This is standard discrepancy theory rather than a new property of Mathia's construction. Harald Niederreiter's **Further discrepancy bounds and an Erdős--Turán--Koksma inequality for hybrid sequences**, *Monatshefte für Mathematik* 161 (2010), 193--222, DOI `10.1007/s00605-009-0150-y`, is a modern reference for the Erdős--Turán--Koksma machinery and Kronecker-sequence discrepancy context.

## 3. A grid transfer turns star discrepancy into collision-tail discrepancy

The exceedance set in `T^(d+1)` is

`E_L = {(x,y): |sin(pi y)| > L sqrt(sum_(j=1)^d sin^2(pi x_j))}`.

Write

`g_L(x,y)=sin^2(pi y)-L^2 sum_j sin^2(pi x_j)`.

Then `E_L={g_L>0}`. Partition the unit cube into axis-aligned cubes of side `h`. Let `U_-` be the union of cells wholly contained in `E_L` and `U_+` the union of cells that meet `E_L`. Then

`U_- subset E_L subset U_+`.

A general axis-aligned box has discrepancy at most `2^(d+1) D_Q^*` by inclusion-exclusion from anchored boxes. Since either grid union contains at most `h^(-(d+1))` cells, the empirical/Haar discrepancy of each of `U_-` and `U_+` is at most

`C_d D_Q^* h^(-(d+1))`.

It remains to control cells crossing the boundary. The derivative of `sin^2(pi u)` is bounded by `pi`, hence in the sup metric

`|g_L(z)-g_L(z')| <= pi(1+dL^2) ||z-z'||_infinity`.

Every crossing cell is therefore contained in

`{|g_L| <= pi(1+dL^2)h}`.

For fixed `x`, the random variable `sin^2(pi y)` with uniform `y` has the arcsine law on `[0,1]`. Uniformly in the center `a`, an interval of width `2 eta` has mass `O(sqrt(eta))`; equivalently,

`Leb{y: |sin^2(pi y)-a|<=eta} <= C sqrt(eta)`.

Integrating over `x` gives

`Leb(U_+ \ U_-) <= C_d (1+L) h^(1/2)`.

The sandwich `U_- subset E_L subset U_+` now yields

`|F_Q(L)-mu_d(L)|`
` <= C_d [ D_Q^* h^(-(d+1)) + (1+L) h^(1/2) ]`.

Optimizing at

`h asymp (D_Q^*/(1+L))^(2/(2d+3))`

produces

`|F_Q(L)-mu_d(L)|`
` <= C_d (D_Q^*)^(1/(2d+3)) (1+L)^((2d+2)/(2d+3))`.

Combining with the polynomial star-discrepancy estimate proves the stated finite-`Q` bound.

## 4. A first rigorous jointly growing threshold regime

`VIS-164` proves

`mu_d(L) ~ c_d L^(-d)`

as `L->infinity`. Put `L(Q)=Q^gamma`. The absolute error above is

`O(Q^(-delta/(2d+3) + gamma(2d+2)/(2d+3)))`.

Dividing by the Haar main term `c_d Q^(-d gamma)` shows that the relative error tends to zero whenever

`-delta/(2d+3) + gamma[d+(2d+2)/(2d+3)] < 0`,

which is exactly

`gamma < delta/(2d^2+5d+2)`.

Thus the order-of-limits obstruction in `VIS-164` can be crossed in at least one rigorous, if very conservative, regime: the collision threshold may grow as a sufficiently small positive power of the anchor count while the empirical exceedance frequency still tracks the shrinking Haar tail.

Since the predicted number of exceedances is then asymptotic to

`c_d Q^(1-d gamma)`,

and the admissible `gamma` is smaller than `1/d`, there are eventually many exceedances. In particular `max_(q<=Q) C_q>Q^gamma` for all sufficiently large `Q`.

## 5. Consequence for the active visual-exploration clue

The matched omitted-prime baseline now has three levels:

- `VIS-163`: qualitative continuous/Lipschitz decoder failure;
- `VIS-164`: fixed-threshold Haar collision law and dimension-coded tail;
- `VIS-165`: a finite-`Q` discrepancy transfer and a nontrivial jointly growing threshold regime.

This closes one explicit boundary left by `VIS-164`: a growing collision threshold is not automatically beyond proof merely because ordinary equidistribution is qualitative. Classical transcendence plus discrepancy theory already forces some quantitative growth for the omitted-prime null.

The result also makes the positive test stricter. A zeta-facing observable cannot claim source-sensitive instability merely from polynomially growing anchored collisions unless its growth is compared with this matched omitted-prime control under the same support and normalization. The meaningful target remains a predeclared relative separation, not absolute growth.

## 6. Prior art and novelty boundary

Both deep ingredients are established mathematics. Matveev supplies polynomial lower bounds for nonzero linear forms in logarithms of fixed algebraic numbers as the integer coefficients grow. Erdős--Turán--Koksma converts the resulting finite Diophantine type into polynomial discrepancy for the associated fixed-dimensional Kronecker sequence.

The grid approximation of the particular collision exceedance set is elementary and deliberately conservative; it is not claimed to be an optimal discrepancy theorem for smooth or semialgebraic sets. Sharper boundary-discrepancy machinery could improve the exponent without changing the conceptual conclusion.

No novelty is claimed for linear forms in logarithms, Kronecker discrepancy, arcsine anti-concentration, or shrinking-target theory. The Mathia-specific contribution is the composition of these classical tools with the anchored held-out-prime collision observable from `VIS-164`, yielding an explicit proof that the matched null already supports a jointly growing quantitative instability regime.

## 7. Boundaries and falsification

All prime sets are fixed. The constants and the exponent `delta(P,r)` may be extremely poor and deteriorate rapidly with support dimension or prime size. Nothing here is uniform in growing support.

The finite-`Q` bound is not sharp. It uses a box grid and only star discrepancy, paying the exponent `1/(2d+3)` because the boundary is controlled by the worst-case square-root anti-concentration of `sin^2(pi y)`. A more tailored discrepancy theorem may substantially improve it.

The theorem does not identify the true order of `max_(q<=Q) C_q`, does not give a limiting extreme-value distribution, and does not imply the heuristic `Q^(1/d)` scale. It proves only that some positive power `Q^gamma` is eventually exceeded, with an exponent limited by the Diophantine discrepancy input and the conservative set-transfer bound.

Falsify the argument by exhibiting a nonzero integer frequency for which the prime-log linear form violates the stated finite-type bound, an error in the Erdős--Turán--Koksma specialization, or a failure of the grid/arcsine boundary estimate. Any such failure would invalidate the quantitative conclusion.

## Research consequence

The held-out-prime null already has a rigorous jointly growing regime. Future visual or numerical collision experiments should therefore normalize against matched omitted-prime controls at the same support and should not treat positive-power growth of anchored collision scores as zeta-specific evidence.

A genuinely source-sensitive next step must prove a relative separation in exponent, normalized tail, approximation error, or another predeclared regularity functional that survives this strengthened quantitative control.