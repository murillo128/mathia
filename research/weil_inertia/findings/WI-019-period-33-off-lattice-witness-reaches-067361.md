# WI-019 — a period-33 off-lattice witness reaches density 0.67361 for the collapsed MT Gram interface

**Status:** `EXACT-DERIVED + COMPUTATIONAL-INTERVAL + DECISIVE-NEGATIVE` for the collapsed single-profile Montgomery--Taylor Gram-defect interface of WI-015--WI-018. The configuration, density, analytic tail estimate, and final self-consistency implication are exact. The load-bearing finite kernel sum has now been replayed with 160-bit MPFR directed interval arithmetic, closing the numerical gate left open in the first version of this finding.

## 1. Precise obstruction

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

The witness below has exact retained density

\[
\boxed{r=\frac{67361}{100000}=0.67361.}
\]

The directed interval replay in Section 4 proves the remaining finite inequality, so the collapsed interface alone cannot force

\[
\boxed{S/N>0.67361.}
\]

This sharpens WI-018's interval-backed explicit obstruction `31/46=0.6739130434...` and independently approaches the `0.6736` fixed-Montgomery--Taylor pure-Gram ceiling claimed in Michael Devine's public 2026 follow-up.

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

## 4. Directed interval replay of the finite sum

Let

\[
 d_{10000}:=\frac1{33}\sum_{i,j=1}^{33}
 \sum_{q=-10000}^{10000}{}'
 w\!\left(|x_j-x_i+qL|\right).
\tag{9}
\]

The original ordinary floating-point replays gave

\[
\begin{array}{ll}
\text{NumPy / binary64:}&
 d_{10000}=0.0016368318535888034,\\[1mm]
\text{C / x86 long double:}&
 d_{10000}=0.00163683185358877553923.
\end{array}
\tag{10}
\]

The finite sum has now also been evaluated with outward-rounded MPFR intervals at 160-bit precision directly from the exact rational gap data. The replay used `mpfr_const_pi` with downward/upward rounding, directed interval arithmetic for every algebraic operation, and rigorous sine/cosine enclosures. For a narrow argument interval `[a,b]`, the trigonometric enclosure was obtained from correctly rounded `sin(a)` or `cos(a)` and the global Lipschitz bounds

\[
|\sin x-\sin a|\le |x-a|,
\qquad
|\cos x-\cos a|\le |x-a|.
\]

To reduce transcendental calls without weakening rigor, successive lattice translates were advanced by the exact angle-addition formulas in interval arithmetic, with direct MPFR trigonometric recomputation every 96 translates. The rational position interval itself was advanced by the exact rational period `L`, always with directed rounding. Unordered-pair symmetry reduced the finite accumulation to `10,570,528` nonnegative interval terms; the final sum was accumulated upward.

The resulting upper endpoint was approximately

\[
0.0016368318535887754531\ldots,
\]

and, crucially, the directed comparison was made against a downward-rounded enclosure of the exact rational target. It proved

\[
\boxed{d_{10000}<\frac{1637}{10^6}=0.001637.}
\tag{11}
\]

The proof margin is about `1.68e-7`, while the outward-rounding width is far below that scale. Equation (11), not the printed decimal endpoint, is the durable computational claim.

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

Combining (11) and (13),

\[
d<0.001637+0.0000007=0.0016377<0.001638,
\]

so (6) holds and the exact self-consistency margin (8) completes the obstruction at density `0.67361`.

## 6. Prior art and novelty audit

The broad ceiling is **not claimed as new**. Michael Devine's public August 2026 work explicitly states that the fixed optimal Montgomery--Taylor kernel plus pure Gram/rank machinery cannot force a bound above `0.6736`; his later `0.673399` headline uses several independent bandlimited profiles and therefore lies outside the single-profile interface capped here. `SOURCES.md` already records that claim as `NEEDS-AUDIT` rather than established evidence.

Targeted searches for the exact rational density `67361/100000`, a period-33 witness of the form above, or the displayed localized-defect gap pattern did not locate matching public prior art. That absence does not establish priority. The useful role of this finding is narrower: it gives Mathia an explicit, interval-certified near-`0.6736` adversary for the collapsed single-profile interface.

The unit-lattice optimization in WI-017 does not apply: the continuous MT kernel is oscillatory and the witness deliberately relaxes away from integer sites. WI-018 already showed that exact integer phase locking is not optimal; the present witness quantifies how much further a structured continuous relaxation can go.

## 7. Boundaries and falsification tests

This is an information-loss obstruction, not a zeta-zero construction and not an upper bound on the full uncollapsed Weil/inertia method.

- **Independent replay remains useful.** The finite comparison (11) is now internally interval-certified, but an independently implemented directed-interval replay would still raise the verification tier further and is the cleanest falsification test for the computational step.
- **Single-profile only.** Multiple genuinely independent admissible profiles retain information absent from one MT Gram matrix. Devine's claimed `0.673399` construction explicitly uses this escape route and remains separately `NEEDS-AUDIT`.
- **Collapsed exceptional block.** WI-004 retains positive remainder information involving the exceptional block `Q'`; any successful coupling of simple and exceptional blocks lies outside (5).
- **Zeta-specific correlations.** A spacing/correlation theorem excluding this periodic geometry by positive density would add information discarded by the collapsed interface.
- **Support greater than one.** The support-one screening threshold of WI-007 remains another independent escape through genuinely new arithmetic information.

No optimality is claimed for period 33 or for density `0.67361`. The numerical search that produced (1) also indicates that feasibility becomes tight very near `0.6736`, in agreement with the public Devine ceiling, but such an optimization statement is not part of the durable claim.

## 8. Consequence for `weil_inertia`

WI-015--WI-017 showed that exact global optimization of the collapsed single-profile Gram defect encounters adversarial periodic configurations, and WI-018 moved the obstruction off the unit lattice to `31/46`. The present interval-certified witness pushes that barrier essentially to the independently claimed `0.6736` wall.

Accordingly, further effort to improve the theorem materially past `0.67361` should not be spent on better optimization of the **same collapsed single-profile MT Gram functional**. The live routes are exactly the ones that retain additional information:

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

The interval replay therefore converts WI-019 from a candidate near-ceiling into a certified information-loss obstruction for the collapsed single-profile architecture.