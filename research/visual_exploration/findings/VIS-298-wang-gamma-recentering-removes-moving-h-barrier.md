# VIS-298 — exact gamma recentering removes Wang's moving square-root-log H barrier

## Claim

Let

`I=(T,T+H]`, `H=T^theta`, `L=log T`,

with fixed `0<theta<1`, and fix `lambda<theta`. Let the source scale satisfy

`x=x(T) -> infinity`, `1<=x<=T^lambda`.

Then Biao Wang's short-interval pair-correlation statistic satisfies

`F_I(x) = (H/(2*pi)) [log x + (L-log(2*pi))^2/x^2] + o(H)`.

Thus the `x~sqrt(L)` absolute-`H` boundary recorded in `VIS-294` is not a genuine boundary of the exact decomposition. It is created by two coarse steps in Wang's Proposition 2.6 proof: keeping the gamma factor inside an undifferentiated `E_x=O(1/x)` remainder and then using Cauchy--Schwarz against the uniform estimate `||D_x||_2 << sqrt(HL)`.

After the exact gamma contribution is recentered and the remaining right-half-plane zeta term is treated with its actual Dirichlet frequencies, **every moving source `x->infinity` below one fixed theorem ceiling is resolved to absolute `o(H)` accuracy**. In particular there is no separate moving lower-source transition at `sqrt(log T)`.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT-DERIVED ERROR RECOMBINATION + MOVING-BOUNDARY NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new zero-free region, prime-number-theorem remainder, pair-correlation theorem beyond this specialization, RH implication, bounded-source asymptotic, or moving upper-ceiling theorem is claimed.

## 1. Recenter Wang's exact decomposition before estimating cross terms

Wang writes

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`,

with `B_x(t)=log(t+2)/x`. `VIS-297`, returning to the exact Landau-form decomposition inherited from Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, rewrites the remainder as

`E_x(t)`
` = x^(-1)[-chi'/chi(-1/2+it)`
`           + zeta'/zeta(3/2-it) - log(t+2)]`
`   + P_x(t)+T_x(t)`.

Therefore the artificial split between `B_x` and the leading gamma part of `E_x` can be removed exactly. Put

`G(t)=-chi'/chi(-1/2+it)`,

`Z(t)=zeta'/zeta(3/2-it)`,

and `R_x(t)=P_x(t)+T_x(t)`. Then

`A(x,t) = -D_x(t) + x^(-1)[G(t)+Z(t)] + R_x(t)`.

This identity is the load-bearing change. The terms that produced `H sqrt(L)/x` and `H L/x^2` in the coarse Proposition 2.6 error budget should now be re-estimated separately rather than charged through `||E_x||_2`.

## 2. The diagonal and gamma squares have explicit absolute-H asymptotics

`VIS-291` gives, before any fixed-power specialization,

`int_I |D_x(t)|^2 dt`
` = H log x`
`   + O(H exp(-c V(log x)) + x log^2(2x))`,

where `V(y)=y^(3/5)(log y)^(-1/5)` for sufficiently large `y`. Since `x->infinity` and `x<=T^lambda` with `lambda<theta`, both error terms are `o(H)`. Hence

`int_I |D_x(t)|^2 dt = H log x + o(H)`.

For the gamma factor, the standard digamma asymptotic on a fixed vertical line gives the full complex estimate

`G(t)=log(t/(2*pi))+O(1/t)`,

and `G'(t)=O(1/t)`. Uniformly on `I`, because `H=o(T)`,

`G(t)=L-log(2*pi)+O(H/T+1/T)`.

Consequently

`x^(-2) int_I |G(t)|^2 dt`
` = H (L-log(2*pi))^2/x^2 + o(H)`.

The error is `o(H)` even without using `x->infinity`, since `L H/T ->0`.

## 3. The right-half-plane zeta square is negligible once x moves

On `Re(s)=3/2`,

`Z(t)=-sum_(m>=2) Lambda(m)m^(-3/2) exp(it log m)`

converges absolutely, so `Z(t)=O(1)` uniformly. Hence

`x^(-2) int_I |Z(t)|^2 dt = O(H/x^2)=o(H)`

for every `x->infinity`.

The pole and trivial-zero remainder from `VIS-297` satisfies

`R_x(t)=O(x^(1/2)/T^2 + x^(-5/2)/T)`.

Its square and all of its cross terms with `D_x`, `G/x`, and `Z/x` are `o(H)` under `x<=T^lambda`, `lambda<theta<1`; ordinary Cauchy--Schwarz is already more than sufficient at this much smaller scale.

## 4. The apparent sqrt(L) cross-term barrier disappears under frequency-aware bounds

The `D_x,G` cross term can be estimated exactly as Wang estimates the `D_x,B_x` cross. Since

`D_x(t)=sum_n a_n n^(-it)`

and Wang's coefficients satisfy

`sum_n a_n/log n << sqrt(x)`,

integration by parts with `G(t)=O(L)` and `G'(t)=O(1/T)` yields

`int_I G(t) n^(-it) dt << L/log n`.

After the prefactor `1/x`,

`x^(-1) |int_I D_x(t) overline(G(t)) dt| << L/sqrt(x)=o(H)`.

The `D_x,Z` cross term is even smaller, and here the frequency orientation matters. Because

`overline(Z(t))=-sum_(m>=2) Lambda(m)m^(-3/2) exp(-it log m)`,

the product `D_x(t) overline(Z(t))` contains frequencies `log(nm)`, never a diagonal frequency `log(n/m)`. Therefore

`x^(-1) |int_I D_x(t) overline(Z(t)) dt|`
` << x^(-1) sum_n a_n sum_(m>=2) [Lambda(m)m^(-3/2)/log(nm)]`
` << x^(-1) sum_n a_n/log n`
` << x^(-1/2)`.

This is `o(H)` with no square-root-log restriction.

Likewise, integrating the absolutely convergent series for `Z` termwise against the slowly varying gamma factor gives

`x^(-2) |int_I G(t) overline(Z(t)) dt| << L/x^2 = o(H)`.

Thus neither mixed channel produces the `H sqrt(L)/x` or `H L/x^2` barrier seen after the coarse `E_x` norm bound.

## 5. Reassemble the complete statistic

Wang's short-interval localization identity is

`2*pi F_I(x)=int_I |A(x,t)|^2 dt + O(x L^3)`.

Combining the preceding square and cross estimates gives

`int_I |A(x,t)|^2 dt`
` = H log x + H(L-log(2*pi))^2/x^2 + o(H)`.

The localization remainder is also `o(H)` because

`x L^3/H <= T^(lambda-theta)L^3 ->0`.

Division by `2*pi` proves the claim.

The conclusion is uniform along any chosen moving family satisfying only `x->infinity` and one fixed upper ceiling `x<=T^lambda`, `lambda<theta`. No lower growth rate such as `x>>sqrt(L)` or `x^2 log x>>L` is required after the exact decomposition is used.

## 6. What this closes and what it does not

`VIS-294` correctly identified where the **coarse Proposition 2.6 majorants** first cease to be `o(H)`: `H sqrt(L)/x` and `H L/x^2` become order `H` near `x~sqrt(L)`. The present recombination shows that those majorants are not load-bearing for the exact statistic. Their apparent crossover comes from treating explicit gamma and absolutely convergent zeta pieces as one generic `O(1/x)` remainder.

Accordingly, the accepted `CLUE-wang-fixed-source-packet-localization` no longer has a live **moving lower-source** branch. Every source with `x->infinity` is already controlled at absolute `H` resolution after natural gamma recentering. A genuinely bounded source `x=O(1)` is a different regime: the `Z/x` square need not be `o(H)`, so this finding does not claim a bounded-source formula.

The fixed-power real-axis arithmetic question also remains separate. This proof uses the same Korobov--Vinogradov PNT envelope as `VIS-291`; it does not improve that arithmetic input. The upper source ceiling remains separate as well: `lambda<theta` is still fixed, and nothing here allows `lambda` or `log x/L` to approach `theta` without a new uniformity argument.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the short-interval pair-correlation decomposition, Proposition 2.6 error budget, coefficient bounds, and localization identity used here.

S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, and C. L. Turnage-Butterbaugh, **An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function**, *Acta Arithmetica* 214 (2024), 357--376, arXiv:2306.04799, supply the exact Landau-form source identity inherited by Wang and unpacked in `VIS-297`.

The gamma/digamma asymptotics are classical; NIST DLMF §5.11 is an authoritative reference. No novelty is claimed for those ingredients. The Mathia-specific result is the exact recombination and scale accounting showing that the previously stored square-root-log absolute-`H` frontier is not intrinsic once the pieces are estimated according to their actual analytic structure.

The finding does not control bounded `x`, improve the PNT scale, establish a new secondary arithmetic term, permit a moving theorem ceiling, or change any RH-equivalent analytic-continuation boundary from `VIS-293`.

## Dependencies

- `VIS-291`: `H log x+o(H)` diagonal square for every moving source under a fixed ceiling.
- `VIS-293`: RH-equivalent half-plane pole boundary for the squared-von-Mangoldt source transform.
- `VIS-294`: the coarse absolute-`H` square-root-log boundary now shown to be non-load-bearing.
- `VIS-295`--`VIS-297`: normalization analysis culminating in the exact gamma/zeta decomposition used here.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose lower moving-source branch is closed by this finding.

## Research consequence

Do not spend further visual-research effort searching for a moving lower-source transition at `x~sqrt(log T)` or `x~sqrt(log T/log log T)` within Wang's present fixed-ceiling theorem. After exact gamma recentering, the complete statistic already has an absolute-`H` asymptotic for every `x->infinity`.

The surviving source questions are now cleaner: either improve the genuinely arithmetic fixed-power residual beyond the generic PNT envelope, or prove new uniformity as the source approaches Wang's upper theorem ceiling. The bounded-source regime is separate and should be investigated only if it exposes information not already exhausted by the fixed-source analysis.