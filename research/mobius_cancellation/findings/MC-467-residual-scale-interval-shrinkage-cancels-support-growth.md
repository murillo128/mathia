# MC-467 — Residual-scale interval shrinkage cancels source-support growth

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The remaining large-threshold escape after `MC-466` is more constrained than the formal parameter

\[
M=\left\lceil\frac{S L}{p-L}\right\rceil-1
\]

suggests. In the exact `MC-463` staged geometry, residual support size and source-interval length are **not independent resources**: increasing the reduced residual divisor `s_0` creates more possible source points in a dyadic shell but shortens each source interval by the reciprocal factor.

Fix a contributing outer pair `(r,r')`, an original compatible shift `h`, and write

\[
R=[r,r'],
\qquad
T=\frac{r'}{(h,r')}.
\tag{1}
\]

The equality for `T` is `MC-466` equation (3). After the exact `MC-463` gcd-sector aggregation, the admissible integers in the reduced residual variable `s_0` satisfy

\[
n+h
=
 g r_1 G s_0\bigl(\ell_{s_0}+Tj\bigr),
\tag{2}
\]

with `r'=g r_2`, `G=(h_0,r_2)`, `T=r_2/G`, and therefore increasing `j` by one increases `n` by exactly

\[
 g r_1 G s_0 T
=
 g r_1 r_2 s_0
=
R s_0.
\tag{3}
\]

Hence, if `J_{s_0}` is the actual `j`-interval coming from `1<=n<=N-h`, then

\[
\boxed{
|J_{s_0}|
\le
1+\frac{N}{R s_0}.
}
\tag{4}
\]

Now restrict the reduced divisors to one dyadic shell

\[
X\le s_0<2X.
\tag{5}
\]

For a fixed source anchor, `MC-463` gives one residue class modulo `T`; coprimality restrictions can only reduce the count. Therefore the number `A_X` of represented reduced divisors in that anchor satisfies

\[
A_X\le 1+\frac XT.
\tag{6}
\]

Let

\[
H_X:=\max_{X\le s_0<2X}|J_{s_0}|.
\]

Equations `(4)` and `(6)` give the exact scale envelope

\[
\boxed{
A_X H_X
\le
\left(1+\frac XT\right)
\left(1+\frac{N}{RX}\right).
}
\tag{7}
\]

There are two boundary regimes and one genuine bulk regime.

If `X<T`, a fixed anchor contains at most one integer of the dyadic shell, so the fixed-anchor second moment from `MC-461` cannot beat its pointwise bound for an interval of length at most `p`: its effective participation is at most one while the gain condition requires more than `p/L>=1`.

If `RX>N`, equation `(4)` gives `|J_{s_0}|<=1` for every integer `s_0` in the shell. After equal source shifts are aggregated modulo `p`, effective participation is at most `p`, while the `MC-461` gain condition at length one requires strictly more than `p`; again no strict source-frame gain is possible.

Thus any shell capable of a nontrivial fixed-anchor source-moment gain lies in the interior regime

\[
T\le X\le \frac NR.
\tag{8}
\]

There `(7)` collapses to

\[
\boxed{
A_X H_X\le 4\frac{N}{RT}.
}
\tag{9}
\]

For arbitrary aggregated coefficients in this shell, the effective participation ratio satisfies `R_eff<=A_X`. Any legitimate common interval length `L_X` is at most `H_X`. The `MC-461` slice-Cauchy estimate can improve on the pointwise bound only if

\[
R_{\rm eff}>\frac p{L_X},
\]

so `(9)` gives the necessary condition

\[
\boxed{
T<4\frac{N}{pR}.
}
\tag{10}
\]

The reduced quotient therefore cannot become favorable merely by moving to a larger residual-divisor scale: the increased shell occupancy is canceled, at exponent scale, by the shorter arithmetic progression available to each residual divisor.

There is a matching consequence for the `MC-464`--`MC-466` favorable-shift threshold. Suppose a common-length reduction is made inside the shell and stays away from the complete-length endpoint,

\[
L_X\le(1-\eta)p
\qquad(0<\eta\le1).
\tag{11}
\]

Define the shell threshold

\[
M_X
:=
\left\lceil\frac{X L_X}{p-L_X}\right\rceil-1.
\tag{12}
\]

In the only potentially gainful regime `(8)`, equations `(4)` and `(11)` imply

\[
X L_X
\le
X H_X
\le
X+\frac NR
\le
2\frac NR,
\]

and therefore

\[
\boxed{
M_X
<
\frac{2N}{\eta pR}.
}
\tag{13}
\]

Applying the original-shift Fejér envelope of `MC-466` to this shell gives

\[
\boxed{
\frac{F_Q(r,r';M_X)}{E_Q}
\le
\min\!\left(
1,
\frac{A(A+1)}{r'}
\right),
\qquad
A:=\frac{2N}{\eta pR}.
}
\tag{14}
\]

Thus the previously open large-`M` escape is forced onto a small outer scale unless the interval is near the endpoint `p`. At exponent scale, a nonvanishing favorable Fejér fraction in the nonendpoint regime requires

\[
\frac{N}{pR}
\not=o(\sqrt{r'}).
\tag{15}
\]

Since `R=[r,r']>=r'`, a necessary coarse consequence is

\[
\boxed{
r'\ \lesssim_\eta\ (N/p)^{2/3}}
\tag{16}
\]

for cells on which the shell threshold can be of square-root size. Equation `(16)` is only a necessary scale restriction; it does not show that the remaining small-`r'` cells have negligible coefficient mass.

The result closes one specific loophole left by `MC-466`: **the pair-dependent threshold cannot be made large in the bulk by combining a large residual support scale with the long interval belonging to a smaller residual scale.** Those two quantities are tied by the exact arithmetic step `R s_0`.

What remains genuinely open is narrower: near-complete source intervals `L_X\approx p`; the total well-factorable coefficient mass carried by the small-`r'`/small-`R` cells allowed by `(15)`--`(16)`; and whether the retained coefficient `\widetilde\beta(s_0)` together with the aligned amplitude `B_\beta(C_{s_0}+r_1s_0j)` yields additional cancellation inside those surviving cells.

No conductor-power saving for the full staged kernel, no bound for `M(x)`, and no RH consequence follows.

## 1. Exact interval geometry

Equation `(2)` is the normalized `MC-463` parametrization. Its `j`-coefficient is

\[
g r_1 G s_0 T
=g r_1 r_2s_0
=[r,r']s_0,
\]

which proves `(3)`. Any arithmetic progression with step `R s_0` contained in an interval of width at most `N` contains at most `1+N/(R s_0)` points, proving `(4)` independently of the start residue.

This is the missing dependence suppressed by a common symbol `L_{r,r'}` in the coarse support gate. The interval is naturally a function of the residual scale as well as of the outer pair.

## 2. Anchor occupancy and interval length consume the same dyadic scale

Inside `[X,2X)`, one residue class modulo `T` contains at most `1+X/T` integers. Combining this with `(4)` proves `(7)`.

When `X>=T`,

\[
1+\frac XT\le2\frac XT.
\]

When `X<=N/R`,

\[
1+\frac{N}{RX}\le2\frac{N}{RX}.
\]

Multiplication gives `(9)`. The reduced-divisor scale cancels exactly:

\[
\frac XT\cdot\frac{N}{RX}
=
\frac{N}{RT}.
\tag{17}
\]

This is not cancellation of oscillatory phases; it is a resource accounting identity. It says the same scale `X` that supplies more residual source points also makes each source sum shorter.

For weighted source points, replacing cardinality by the participation ratio cannot improve the envelope because `R_eff<=A_X`. Hence `(10)` is coefficient-independent at the support level.

## 3. The nonendpoint Fejér threshold loses the residual scale as well

For any positive real `y`, `ceil(y)-1<y`. Applying this to `(12)` and using `p-L_X>=eta p` gives

\[
M_X
<
\frac{X L_X}{\eta p}.
\tag{18}
\]

In the interior regime, equation `(4)` yields

\[
XH_X\le X+\frac NR\le2\frac NR,
\tag{19}
\]

so `(13)` follows. Substitution into `MC-466` equation (7) yields `(14)`.

If the favorable Fejér fraction is bounded below by a fixed positive constant along a family with `r'->infinity`, `(14)` forces `A` to be of order at least `sqrt(r')`, which is `(15)` at exponent scale. Using `R>=r'` then gives `(16)`.

The endpoint exclusion `(11)` is essential. When `L_X` approaches `p`, the denominator `p-L_X` in the support threshold becomes small and `(13)` no longer follows. That regime must be priced separately rather than hidden in a uniform `M`.

## 4. Prior art and novelty boundary

Dyadic decomposition, hyperbola-style length/support bookkeeping, van der Corput differencing, dispersion, and well-factorable weights are classical analytic-number-theory techniques. Recent primary examples checked for the present audit include Alexandru Pascadi, *On the exponents of distribution of primes and smooth numbers* (arXiv:2505.00653), which uses triply well-factorable weights and modern dispersion/large-sieve input, and Zhiyuan Yang, *Convolution-type Bombieri-Vinogradov theorem with well-factorable Weights, and its applications* (arXiv:2608.13299), which explicitly builds on Pascadi's triply-well-factorable convolution and incomplete-Kloosterman estimates.

Those papers establish that factor-specific scale management inside dispersion is active prior art; they do not supply equations `(3)`--`(16)` for the present fixed-character staged Möbius kernel. A targeted literature audit on 22 September 2026 found no basis for claiming the branch-specific resource identity `(17)` as an external theorem. No novelty claim is made: the durable result is an exact consequence of the already-derived `MC-463` parametrization combined with the classical fixed-anchor energy gate of `MC-461` and the Fejér envelope of `MC-466`.

## Boundaries and falsification tests

- **This is a shellwise statement.** Summing dyadic shells may introduce logarithmic factors and coefficient interactions. Equations `(9)` and `(13)` prevent a single shell from manufacturing an exponent gain by mixing support and interval scales; they do not bound the full weighted sum by themselves.
- **The near-complete endpoint is open.** If `L_X/p->1`, the denominator in `(12)` can dominate the scale accounting. Such cells require a separate endpoint argument.
- **Small outer scales remain live.** Equation `(16)` identifies rather than eliminates them. Their actual well-factorable coefficient mass and later summation cost must still be computed.
- **The residual amplitude remains live.** The bound concerns the bare source-frame occupancy/interval resource. It neither controls nor discards `\widetilde\beta(s_0)` or `B_\beta(C_{s_0}+r_1s_0j)`.
- **No independence assumption is used.** The result is deterministic and survives arbitrary coefficient concentration inside the shell because `R_eff<=A_X`.
- **The interval step must be audited after every reparametrization.** Any alternative staging that changes the exact `j`-step may evade `(4)`; reusing `(13)` without re-deriving that step would be invalid.

## Consequence for the live branch

The next outer-stage test should no longer treat `M_{r,r'}` as a free pair parameter obtained from a global residual cutoff and an unrelated long interval. Split the actual reduced residual variable dyadically, use `(13)` in every nonendpoint shell, and sum the outer coefficient envelope only over the surviving small-`R`/small-`r'` cells. If that total is negligible, the bare outer/support route closes except for the endpoint. If it is not negligible, the remaining work is genuinely inside those cells: weighted participation of `\widetilde\beta` and joint control of the aligned unexpanded amplitude.