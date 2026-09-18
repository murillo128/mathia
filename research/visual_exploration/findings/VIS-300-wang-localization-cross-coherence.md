# VIS-300 — Wang's `H/log^3 T` localization boundary is an inside--outside cross-coherence problem

## Claim

Let

`I=(T,T+H]`, `H=T^theta`, `L=log T`,

with fixed `0<theta<1`, and let `A(x,t)` and `A_I(x,t)` be Biao Wang's full-zero and interval-restricted fields. Put

`R_I(x,t)=A(x,t)-A_I(x,t)`

for `t in I`, and

`J_I(x)=integral_I |A(x,t)|^2 dt`.

Then Wang's exact Lemma 2.3 identity admits the decomposition

`2*pi F_I(x)-J_I(x)`
` = integral_(R\I) |A_I(x,t)|^2 dt`
`   - 2 Re integral_I A_I(x,t) overline(R_I(x,t)) dt`
`   - integral_I |R_I(x,t)|^2 dt`.

Moreover, the two **pure leakage energies** satisfy

`integral_I |R_I(x,t)|^2 dt << x L^2`,

`integral_(R\I) |A_I(x,t)|^2 dt << x L^2`.

Hence

`2*pi F_I(x)`
` = J_I(x) - 2 Re integral_I A_I overline(R_I) dt + O(xL^2)`.

In particular, if `x->infinity` and `x=O(H/L^3)`, then `xL^2=o(H)` and the interior expansion already established in `VIS-298`--`VIS-299` gives

`2*pi F_I(x)`
` = H log x + H(L-log(2*pi))^2/x^2`
`   - 2 Re integral_I A_I overline(R_I) dt + o(H)`.

Therefore at the moving boundary `x asymp H/L^3`, the unresolved `H`-scale localization problem is **entirely the inside--outside cross-coherence term**. The masses of the omitted tail and of the interval field's exterior leakage are already `o(H)` there.

Equivalently, within this regime the `o(H)` extension of the `VIS-299` pointwise asymptotic is reduced to

`Re integral_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt = o(H)`.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-SPECIALIZATION + PROOF-STRUCTURE REDUCTION + NO-NOVELTY-CLAIM`.

This does not prove that the cross term is `o(H)`, does not show that `H/L^3` is an intrinsic transition of `F_I`, and does not assume RH or pair correlation beyond the inputs already used in the preceding Wang-source findings.

## 1. Exact localization-energy decomposition

Wang's Lemma 2.3 gives

`2*pi F_I(x)=integral_R |A_I(x,t)|^2 dt`.

On `I`, write `A=A_I+R_I`. Then pointwise

`|A_I|^2-|A|^2 = -2 Re(A_I overline(R_I))-|R_I|^2`.

Splitting the exact Lemma 2.3 integral into `I` and `R\I` therefore gives

`2*pi F_I(x)-integral_I |A|^2`
` = integral_(R\I)|A_I|^2`
`   -2 Re integral_I A_I overline(R_I)`
`   -integral_I |R_I|^2`.

No estimate has entered yet. This identity separates three mathematically different effects that are combined in the single `O(xL^3)` term of Lemma 2.4: exterior energy of the interval field, interior energy of the omitted-zero tail, and their coherent cross interaction.

## 2. Both pure leakage energies are only `O(xL^2)`

For `t=T+a in I`, put `b=H-a`. Wang's equation (2.15) gives

`|R_I(x,t)|`
` << sqrt(x)L[(1+a)^(-1)+(1+b)^(-1)]`.

Squaring and integrating over `0<=a<=H` yields

`integral_I |R_I|^2 dt`
` << xL^2 integral_0^H [(1+a)^(-1)+(1+H-a)^(-1)]^2 da`.

The two square terms have bounded integrals, while

`integral_0^H da/[(1+a)(1+H-a)]`
` = 2 log(1+H)/(H+2)`.

Thus the whole integral is `O(1)` and

`integral_I |R_I|^2 dt << xL^2`.

Wang's equation (2.16) already gives

`|A_I(x,t)| << sqrt(x)L/(1+dist(t,I))`

for `t notin I`; squaring and integrating the two exterior half-lines gives

`integral_(R\I)|A_I(x,t)|^2 dt << xL^2`.

So neither pure leakage term carries the additional factor `log H`.

## 3. The extra logarithm in Lemma 2.4 enters only through the cross term

Wang bounds the energy difference on `I` by combining the pointwise estimate

`|A|+|A_I| << sqrt(x)L`

with the endpoint tail bound for `R_I`. At the level of the exact decomposition above, that step is precisely an absolute-value estimate on

`C_I(x)=integral_I A_I(x,t) overline(R_I(x,t)) dt`.

Indeed,

`|C_I(x)|`
` << xL^2 integral_0^H [(1+a)^(-1)+(1+H-a)^(-1)] da`
` << xL^2 log(2+H)`
` << xL^3`.

This is the unique place where the logarithmic endpoint integral occurs. The `O(xL^3)` localization ceiling is therefore a bound on **coherence between the inside field and the outside-zero tail**, not a statement that the tail itself has `xL^3` energy.

This distinction matters because an improvement of the tail-energy estimates alone cannot move the `H/L^3` boundary: those energies are already smaller by one factor of `L` at that scale. Any proof-level gain must instead exploit cancellation, phase structure, a deterministic leading correction, or another structural property of `C_I(x)`.

## 4. At `x=O(H/L^3)` the cross term is the complete `H`-scale obstruction

Assume now `x->infinity` and `x=O(H/L^3)`. Then

`xL^2 = O(H/L)=o(H)`.

The analysis in `VIS-291`, `VIS-298`, and `VIS-299` is independent of Lemma 2.4 up to the final localization step and gives in this range

`J_I(x)`
` = H log x + H(L-log(2*pi))^2/x^2 + o(H)`.

The coefficient-square mean-value error satisfies `x log^2(2x)=o(H)` here, the Korobov--Vinogradov remainder is `o(H)` because `x->infinity`, and the exact gamma/right-half-plane zeta pieces remain within their previously established bounds.

Substituting this interior expansion and the two `O(xL^2)` leakage bounds into the exact identity proves

`2*pi F_I(x)`
` = H log x + H(L-log(2*pi))^2/x^2 -2 Re C_I(x)+o(H)`.

At `x asymp H/L^3`, therefore, proving the same pointwise asymptotic as below the boundary is equivalent to proving `Re C_I(x)=o(H)`. If instead `Re C_I(x)` has a deterministic `H`-scale limit or oscillatory correction, that correction is the quantity that must be evaluated. The current estimates do not decide between those possibilities.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies all external ingredients used here. Lemma 2.3 is the exact full-line energy identity; equations (2.14)--(2.16) give the full-field, omitted-tail, and exterior-decay bounds; Lemma 2.4 combines them into `O(xL^3)`. The present finding only reorganizes those displayed estimates and combines them with the already-persisted interior expansion from `VIS-298`--`VIS-299`.

No new general localization theorem, zero-correlation estimate, or literature novelty is claimed. The algebraic energy decomposition itself is elementary. Its research value is diagnostic: it identifies the single bilinear quantity that remains load-bearing at the first unresolved moving source scale.

## Dependencies

- `VIS-298`: exact gamma recentering and frequency-aware interior-field decomposition.
- `VIS-299`: extension of the pointwise source asymptotic through `x=o(H/L^3)` and identification of the localization boundary.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose upper branch asks for the actual localization-tail mechanism.

## Research consequence

Do not spend the next upper-boundary step trying merely to lower the `L^2` mass of `A-A_I` or the exterior mass of `A_I`; both are already negligible at absolute `H` resolution when `x=O(H/L^3)`.

The next decisive object is the bilinear coherence

`C_I(x)=integral_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt`.

A successful continuation must show cancellation in `Re C_I`, compute a deterministic leading correction, or exhibit an admissible control in which an `H`-scale cross term survives. Without such information, the `H/L^3` layer remains a proof boundary rather than an established transition of the pair-correlation statistic.