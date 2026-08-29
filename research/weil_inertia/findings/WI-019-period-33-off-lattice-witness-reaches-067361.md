# WI-019 — a period-33 off-lattice witness reaches density 0.67361 for the collapsed MT Gram interface

**Status:** `EXACT-DERIVED + COMPUTATIONAL-REPLAY + NEEDS-AUDIT + NEGATIVE/OBSTRUCTION` for the collapsed single-profile Montgomery--Taylor Gram-defect interface of WI-015--WI-018. The configuration, density, analytic tail estimate, and final self-consistency implication are exact. The load-bearing finite kernel sum has been independently reproduced in binary64 and x86 `long double`, but has **not** yet been replayed with directed interval arithmetic; until that one finite inequality is interval-certified, this finding must not be upgraded to the `COMPUTATIONAL-INTERVAL` tier of WI-018.

## 1. Precise candidate obstruction

Retain the collapsed stability interface

\[
S\ge HN+\mathcal D(M)-o(N),\qquad
H=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2},
\]

with

\[
\mathcal D(M)=\operatorname{tr}\Psi(M),\qquad
\Psi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2.\end{cases}
\]

As in WI-018, for every positive semidefinite Gram matrix,

\[
\mathcal D(M)\le \operatorname{tr}(M-I)^2,
\]

so a periodic configuration whose quadratic pair energy is small enough is already a countermodel to any downstream argument using only this collapsed single-profile interface and scalar span/count bookkeeping.

The candidate below has exact retained density

\[
\boxed{r=\frac{67361}{100000}=0.67361.}
\]

If the single finite numerical inequality isolated in Section 4 is confirmed with directed interval arithmetic, it follows that the collapsed interface alone cannot force

\[
\boxed{S/N>0.67361.}
\]

This would sharpen WI-018's interval-backed explicit obstruction `31/46=0.6739130434...` and independently approach the `0.6736` fixed-Montgomery--Taylor pure-Gram ceiling claimed in Michael Devine's public 2026 follow-up.

## 2. Exact rational period-33 configuration

Use `m=33` retained atoms per period and total normalized period length

\[
\boxed{L=\frac{33}{r}=\frac{3300000}{67361}.}
\]

Take the first 32 gaps to be the following terminating rationals (the displayed six-decimal values are exact):

\[
\begin{aligned}
(&1.958232,1.035260,1.962375,1.035749,1.962956,1.035863,1.963137,1.035908,\\
 &1.963215,1.035929,1.963254,1.035940,1.963273,1.035945,1.963282,1.035946,\\
 &1.963282,1.035945,1.963274,1.035940,1.963254,1.035930,1.963216,1.035908,\\
 &1.963138,1.035864,1.962958,1.035749,1.962378,1.035261,1.958239,1.026589).
\end{aligned}
\tag{1}
\]

Define the final gap by exact closure,

\[
\boxed{g_{33}=L-\sum_{j=1}^{32}g_j
=\frac{69151625771}{67361000000}
=1.0265825295200486\ldots.}
\tag{2}
\]

All gaps are positive. Let `x_1=0` and `x_{j+1}=x_j+g_j`; periodically extend by `x_{j+33}=x_j+L`.

The geometry is worth recording because it differs from the simpler two-gap witness in WI-018. Most of the period alternates between gaps near `1.036` and `1.963`, but one localized defect consists of two consecutive short gaps near `1.0266`, with neighboring gaps relaxing smoothly toward the bulk alternation. This is the continuous analogue of a phase-locked lattice gas with a localized soliton rather than an exact integer/mechanical word.

## 3. Exact quadratic-energy target

For the normalized Montgomery--Taylor overlap use the same kernel as WI-018,

\[
 k(x)=\frac{\cos(\pi x)-A x\sin(\pi x)}{1-2\pi^2x^2},
 \qquad
 A=\sqrt2\,\pi\cot(1/\sqrt2),
 \qquad w(x)=k(x)^2.
\tag{3}
\]

Define the periodic quadratic defect per retained atom

\[
 d=\frac1{33}\sum_{i,j=1}^{33}\sum_{q\in\mathbb Z}'
 w\!\left(|x_j-x_i+qL|\right),
\tag{4}
\]

where the prime omits only `(i,j,q)=(i,i,0)`. Then every long finite section of the periodic configuration satisfies

\[
\mathcal D(M)\le dS+o(S).
\tag{5}
\]

It is enough to establish

\[
\boxed{d<\frac{819}{500000}=0.001638.}
\tag{6}
\]

Indeed WI-016 already gives the exact rational upper bound

\[
H<\frac{672500704}{10^9}.
\tag{7}
\]

Using `r=67361/100000`, exact arithmetic gives

\[
\begin{aligned}
r\left(1-\frac{819}{500000}\right)
-\frac{672500704}{10^9}
&=\boxed{\frac{296141}{50000000000}}>0.
\end{aligned}
\tag{8}
\]

Hence (6) implies `H+rd<r`, which is exactly the self-consistency condition for the periodic countermodel.

## 4. The only numerical gate: a finite sum through 10,000 periods

Let

\[
 d_{10000}:=\frac1{33}\sum_{i,j=1}^{33}
 \sum_{q=-10000}^{10000}{}'
 w\!\left(|x_j-x_i+qL|\right).
\tag{9}
\]

Two independent direct evaluations of the exact rational configuration (1)--(2) and the literal kernel (3) gave

\[
\begin{array}{ll}
\text{NumPy / binary64:}&
 d_{10000}=0.0016368318535888034,\\[1mm]
\text{C / x86 long double:}&
 d_{10000}=0.00163683185358877553923.
\end{array}
\tag{10}
\]

The two implementations agree to about `2.8e-17`. The deliberately loose finite target needed below is only

\[
\boxed{d_{10000}<\frac{1637}{10^6}=0.001637.}
\tag{11}
\]

Thus the observed numerical margin to the finite target is about `1.68e-7`, many orders of magnitude larger than the discrepancy between the two floating implementations. Nevertheless, ordinary floating-point agreement is not a proof of (11); this is why the finding remains `NEEDS-AUDIT` rather than `COMPUTATIONAL-INTERVAL`.

A decisive replay is small in logical scope: evaluate the `21,781,056` nonzero summands in (9) with directed Arb/MPFR intervals, or equivalently group equal rational distances first, and prove the single rational comparison (11). No optimization is part of the replay.

## 5. Exact analytic tail: less than `7e-7`

WI-018 derives, using only `A<7` and `pi>3`, the pointwise estimate

\[
|k(x)|\le\frac8{17x},\qquad
w(x)\le\frac{64}{289x^2}
\qquad(x\ge1).
\tag{12}
\]

For every omitted `|q|>=10001` and every pair of points in one period,

\[
|x_j-x_i+qL|\ge L(|q|-1).
\]

There are `33^2` directed pairs per sign and the energy is divided by `33`. Therefore

\[
\begin{aligned}
d-d_{10000}
&\le
2\cdot33\,\frac{64}{289L^2}
\sum_{n\ge10000}\frac1{n^2}\\
&\le
2\cdot33\,\frac{64}{289L^2}
\left(\frac1{10000^2}+\frac1{10000}\right)\\
&=
\frac{45379580714321}{74507812500000000000}\\
&<\boxed{\frac7{10^7}}.
\end{aligned}
\tag{13}
\]

This part is exact rational arithmetic after substituting `L=3300000/67361`.

Consequently, once (11) is interval-verified,

\[
d<0.001637+0.0000007=0.0016377<0.001638,
\]

and the exact self-consistency margin (8) completes the obstruction at density `0.67361`.

## 6. Prior art and novelty audit

The broad ceiling is **not claimed as new**. Michael Devine's public August 2026 work explicitly states that the fixed optimal Montgomery--Taylor kernel plus pure Gram/rank machinery cannot force a bound above `0.6736`; his later `0.673399` headline uses several independent bandlimited profiles and therefore lies outside the single-profile interface capped here. `SOURCES.md` already records that claim as `NEEDS-AUDIT` rather than established evidence.

Targeted searches for the exact rational density `67361/100000`, a period-33 witness of the form above, or the displayed localized-defect gap pattern did not locate matching public prior art. That absence does not establish priority. The useful role of this finding is narrower: it gives Mathia an explicit, reproducible near-`0.6736` adversary and reduces independent verification of the claimed fixed-profile ceiling to a concrete finite interval calculation.

The unit-lattice optimization in WI-017 does not apply: the continuous MT kernel is oscillatory and the witness deliberately relaxes away from integer sites. WI-018 already showed that exact integer phase locking is not optimal; the present candidate quantifies how much further a structured continuous relaxation can go.

## 7. Boundaries and falsification tests

This is an information-loss obstruction, not a zeta-zero construction and not an upper bound on the full uncollapsed Weil/inertia method.

- **Finite replay gate.** If directed interval arithmetic fails to prove (11), the claimed `0.67361` obstruction is withdrawn or weakened to the strongest density whose finite sum can be certified. This is the immediate falsification test.
- **Single-profile only.** Multiple genuinely independent admissible profiles retain information absent from one MT Gram matrix. Devine's claimed `0.673399` construction explicitly uses this escape route and remains separately `NEEDS-AUDIT`.
- **Collapsed exceptional block.** WI-004 retains positive remainder information involving the exceptional block `Q'`; any successful coupling of simple and exceptional blocks lies outside (5).
- **Zeta-specific correlations.** A spacing/correlation theorem excluding this periodic geometry by positive density would add information discarded by the collapsed interface.
- **Support greater than one.** The support-one screening threshold of WI-007 remains another independent escape through genuinely new arithmetic information.

No optimality is claimed for period 33 or for density `0.67361`. The numerical search that produced (1) also indicates that feasibility becomes tight very near `0.6736`, in agreement with the public Devine ceiling, but such an optimization statement is not part of the durable claim.

## 8. Consequence for `weil_inertia`

WI-015--WI-017 showed that exact global optimization of the collapsed single-profile Gram defect encounters adversarial periodic configurations, and WI-018 moved the obstruction off the unit lattice to `31/46`. The present candidate pushes that barrier essentially to the independently claimed `0.6736` wall with a compact explicit witness.

If the interval replay succeeds, further effort to improve the theorem materially past `0.6736` should not be spent on better optimization of the **same** collapsed MT Gram functional. The live routes are exactly the ones that retain additional information:

\[
\boxed{\text{multiple genuinely independent profiles}}
\]

or

\[
\boxed{\text{uncollapsed simple/exceptional spectral coupling}}
\]

or

\[
\boxed{\text{new zeta-specific spacing/correlation or support}>1\text{ input}.}
\]

The most immediate audit task, however, is intentionally much smaller: replay (11) with directed intervals and either promote the witness to an exact computational obstruction or discard it.