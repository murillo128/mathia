# VIS-289 — Wang's fixed-power residual is `o(H)` after the linear source baseline

## Claim

Let `H=T^theta`, `L=log T`, with fixed `0<theta<1`. Fix a compact exponent panel

`0 < beta_0 <= beta <= beta_1 < theta`,

and put `x=T^beta`. For Biao Wang's short-interval pair-correlation statistic `F_I(x)`, one has uniformly for `beta in [beta_0,beta_1]`

`F_I(T^beta) = (H/(2*pi))(L^2 T^(-2 beta) + beta L) + o(H)`.

Since `H L^2 T^(-2 beta)=o(H)` uniformly on the panel,

`F_I(T^beta) = (H beta L)/(2*pi) + o(H)`.

Thus the `O(H)` frontier isolated in `VIS-288` is not a genuine fixed-power obstruction. The load-bearing `O(H)` term in Wang's Proposition 2.6 comes from the coarse estimate

`sum_n a_n^2 = log x + O(1)`

inside the `D_x` mean square. A standard prime-number-theorem remainder sharpens this to

`sum_n a_n^2 = log x + o(1)`,

and every other displayed error in Wang's proof is already `o(H)` on a fixed compact power panel.

Consequently **there is no nonzero `H`-scale fixed-power residual profile left by this argument**. Any unresolved fixed-power effect is strictly smaller than `H`; the other genuinely open branch is a moving source regime not contained in one fixed compact exponent panel.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT-DERIVED + NEGATIVE SCALE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, quantitative rate for the final `o(H)`, moving-boundary estimate, off-critical-strip gain, or RH implication is claimed.

## 1. Locate the bare `O(H)` term in Wang's proof

Wang defines

`D_x(t)=sum_(n>=2) a_n n^(-it)`,

with

`a_n = Lambda(n)/sqrt(n) * min(n/x,x/n)`.

Lemma 2.5 records

`sum_n a_n^2 = log x + O(1)`

and

`sum_n n a_n^2 << x log^2(2x)`.

The mean-value step in the proof of Proposition 2.6 is therefore

`int_I |D_x(t)|^2 dt = H sum_n a_n^2 + O(sum_n n a_n^2)`

`                         = H log x + O(H + x log^2(2x))`.

The standalone `O(H)` in Proposition 2.6 is inherited from the `O(1)` remainder in `sum a_n^2`. The other displayed source-dependent errors are explicit and were already shown in `VIS-288` to be `o(H)` when `x=T^beta` with `beta` in a fixed compact subinterval of `(0,theta)`.

## 2. Sharpen the squared-von-Mangoldt input

Write

`A(u)=sum_(n<=u) Lambda(n)^2`.

The classical prime number theorem with a zero-free-region remainder, for example the standard DLMF estimate

`pi(u)-li(u) = O(u exp(-c sqrt(log u)))`,

implies by partial summation

`sum_(p<=u) (log p)^2 = u log u - u + o(u)`.

Prime powers `p^k<=u`, `k>=2`, contribute only `o(u)` to `A(u)`. Hence

`A(u)=u log u-u+o(u)`.

This is standard prime-number-theorem arithmetic; no novelty is claimed for this asymptotic.

Now split Wang's coefficient square exactly at `x`:

`S(x):=sum_n a_n^2`

` = x^(-2) sum_(n<=x) n Lambda(n)^2`
`   + x^2 sum_(n>x) Lambda(n)^2/n^3`.

Stieltjes partial summation with `A(t)=t log t-t+o(t)` gives

`x^(-2) sum_(n<=x) n Lambda(n)^2`
` = (1/2) log x - 1/4 + o(1)`,

while

`x^2 sum_(n>x) Lambda(n)^2/n^3`
` = (1/2) log x + 1/4 + o(1)`.

The constants cancel, so

`S(x)=log x+o(1)`.

The `o(1)` is uniform for all `x>=X` once `X` is large. Therefore it is uniform over `x=T^beta`, `beta in [beta_0,beta_1]`, because the smallest source `T^beta_0` tends to infinity.

## 3. Feed the sharpening back into the complete statistic

Wang's mean-value identity now becomes, uniformly on the fixed exponent panel,

`int_I |D_x(t)|^2 dt = H log x + o(H) + O(x log^2 x)`.

Since `beta_1<theta`,

`x log^2 x <= T^beta_1 L^2 = o(H)`.

Thus

`int_I |D_x(t)|^2 dt = H log x + o(H)`.

The remaining terms in Wang's proof are already below `H` uniformly on the same panel: the `B_x` square contributes its explicit main term `H L^2/x^2` plus `o(H)`, the `B_x-D_x`, `D_x-E_x`, and `B_x-E_x` crosses are `o(H)`, and Lemma 2.4's localization error `O(xL^3)` is `o(H)` because `beta_1<theta`.

Hence

`2*pi F_I(x) = H(log x + L^2/x^2) + o(H)`.

Substituting `x=T^beta` proves

`F_I(T^beta) = (H/(2*pi))(beta L + L^2 T^(-2 beta)) + o(H)`

uniformly for `beta in [beta_0,beta_1]`, and the second displayed main term is itself `o(H)`.

## 4. Prior art and evidence boundary

The pair-correlation formula and all decomposition/mean-value identities used here are from Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially Lemmas 2.4–2.5 and Proposition 2.6.

The only additional input is standard prime-number-theorem precision. NIST DLMF §27.12, equation 27.12.5, records the classical estimate `pi(x)-li(x)=O(x exp(-c sqrt(log x)))`, which is more than sufficient for `A(u)=u log u-u+o(u)`. The cancellation of the `-1/4` and `+1/4` constants above is an elementary specialization to Wang's symmetric coefficient profile.

This finding does not claim that Wang's published proposition should have stated an `o(H)` remainder, nor that the refinement is new in analytic number theory. Its durable role is to close a Mathia control question: the previously anonymous `O(H)` fixed-power floor does not survive once the standard two-term squared-von-Mangoldt asymptotic is inserted into the proof.

## Dependencies

- `VIS-287`: complete-statistic fixed-power linearization at the `HL` scale.
- `VIS-288`: extraction of the apparent `O(H)` fixed-power residual frontier.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose fixed-power `H`-scale branch is closed here.

## Research consequence

The fixed-power branch is now closed through the `H` scale: after subtracting the universal linear source law, the residual is `o(H)` uniformly on every compact exponent panel bounded away from `0` and `theta`.

Further work on this thread must either resolve a genuinely smaller-than-`H` fixed-power scale with a quantitative refinement, or leave the fixed-panel regime entirely — for example `beta(T)->0`, approach to the admissible source ceiling, or a singular packet family whose norm growth is controlled rather than hidden in the normalization.