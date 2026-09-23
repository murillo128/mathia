# WI-411 — Vertical translations obey an exact height-area budget

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent:** [WI-410](./WI-410-carleman-summation-removes-bsy-height-decay-only-by-giving-up-finite-source-budget.md).

## Claim

WI-410 left vertically translated Burnol--Kunik/Blaschke probes as an explicit escape from the real-axis scale barrier. That escape can be priced exactly inside the same finite-total-variation mixture model.

For a right-half zero

\[
\rho=\frac12+d+i\gamma,
\qquad 0<d<\frac12,
\]

and a half-plane probe

\[
s=\frac12+a+ib,
\qquad a>0,
\]

the single-zero Blaschke charge is

\[
q_{a,b}(\gamma,d)
:=\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2}
\ge0.
\tag{1}
\]

Its total mass in the vertical target variable is exactly

\[
\boxed{
\int_{\mathbb R}q_{a,b}(\gamma,d)\,d\gamma
=2\pi\min(a,d)
\le 2\pi d.
}
\tag{2}
\]

The identity is independent of the vertical center `b`. Therefore, if `nu` is any finite signed or complex Borel measure on probe parameters `(a,b) in (0,infinity) x R`, with total variation

\[
M:=\|\nu\|_{\rm TV}<\infty,
\]

and

\[
Q_\nu(\gamma,d)
:=\int q_{a,b}(\gamma,d)\,d\nu(a,b),
\]

then `Q_nu(.,d)` is defined almost everywhere and

\[
\boxed{
\int_{\mathbb R}|Q_\nu(\gamma,d)|\,d\gamma
\le 2\pi d\,M.
}
\tag{3}
\]

Consequently, if a source-independent translated mixture is required to have a height-uniform linear defect response

\[
|Q_\nu(\gamma,d)|\ge c d
\]

for almost every `gamma` in an interval `I` of length `L`, then necessarily

\[
\boxed{
M\ge \frac{cL}{2\pi}.
}
\tag{4}
\]

In particular, uniform `Omega(d)` sensitivity throughout `[T,2T]` costs `Omega(T)` coefficient total variation. Vertical translation can remove the **pointwise** `d/gamma` attenuation seen by a fixed real-axis probe by moving the probe near the target height, but it cannot turn that localization into a fixed finite-budget detector across an expanding height range.

The order is sharp inside this mixture model. A single real-axis probe with `a=T`, multiplied by weight `T`, already gives for `T>=1`, `0<d<=1/2`, and `T<=gamma<=2T`,

\[
Tq_{T,0}(\gamma,d)
\ge
\frac{2T^2d}{\gamma^2+T^2+d^2}
\ge
\frac{8}{21}d.
\tag{5}
\]

Thus the minimum coefficient mass needed for a fixed positive linear-depth response across a dyadic height window is `Theta(T)`, not merely `Omega(T)`. Allowing vertical translations changes where the budget is spent; it does not improve its asymptotic order.

No improved simple-critical-zero proportion and no RH conclusion are claimed.

## 1. Exact translated Blaschke charge

The half-plane Blaschke factor used in WI-410 compares a zero `rho=1/2+d+i gamma` with its reflection `1-bar(rho)=1/2-d+i gamma` across the critical line. At

\[
s=\frac12+a+ib,
\]

its modulus ratio is

\[
|b_\rho(s)|^2
=
\frac{(\gamma-b)^2+(a-d)^2}
     {(\gamma-b)^2+(a+d)^2}.
\]

Hence `-log |b_rho(s)|` is exactly (1). The numerator in (1) exceeds the denominator by `4ad`, so the charge is nonnegative. At `a=d` and `b=gamma` it has the expected logarithmic singularity; that singularity is locally integrable and does not affect the area identity.

Put

\[
A=a+d,
\qquad
B=|a-d|,
\qquad
u=\gamma-b.
\]

Then `A>=B>=0` and

\[
q_{a,b}
=\frac12\log\frac{\nu^2+A^2}{\nu^2+B^2}.
\]

For `B>0`, write the logarithmic ratio as an integral in the scale parameter:

\[
\frac12\log\frac{\nu^2+A^2}{\nu^2+B^2}
=
\int_B^A\frac{t}{\nu^2+t^2}\,dt.
\]

The integrand is nonnegative, so Tonelli gives

\[
\begin{aligned}
\int_{\mathbb R}q_{a,b}(\gamma,d)\,d\gamma
&=
\int_B^A
\left(
\int_{\mathbb R}\frac{t}{\nu^2+t^2}\,d\nu
\right)dt\\
&=
\int_B^A\pi\,dt\\
&=\pi(A-B).
\end{aligned}
\]

The case `B=0` follows by monotone convergence, or by the same nonnegative integral with the endpoint `t=0` omitted. Since

\[
A-B
=(a+d)-|a-d|
=2\min(a,d),
\]

this proves (2).

Two features are worth separating. Translation in `b` merely translates the nonnegative profile and therefore leaves its `L^1` mass unchanged. Changing the horizontal scale `a` changes the mass only until `a=d`; once the probe lies at least as far from the critical line as the zero depth, the available area saturates at exactly `2 pi d`.

## 2. Finite-total-variation mixtures

Let `|nu|` denote the total-variation measure of the finite signed/complex probe measure. Positivity of every single-probe profile gives, wherever the mixture is defined,

\[
|Q_\nu(\gamma,d)|
\le
\int q_{a,b}(\gamma,d)\,d|\nu|(a,b).
\]

Integrating in `gamma` and applying Tonelli to the nonnegative right side,

\[
\begin{aligned}
\int_{\mathbb R}|Q_\nu(\gamma,d)|\,d\gamma
&\le
\int
\left(
\int_{\mathbb R}q_{a,b}(\gamma,d)\,d\gamma
\right)d|\nu|(a,b)\\
&=
2\pi\int\min(a,d)\,d|\nu|(a,b)\\
&\le
2\pi d\,\|\nu\|_{\rm TV},
\end{aligned}
\]

which is (3). The same computation also shows that the mixture is finite for almost every target height.

If `|Q_nu|>=cd` almost everywhere on an interval `I`, then

\[
cd|I|
\le
\int_I|Q_\nu(\gamma,d)|\,d\gamma
\le
2\pi d M,
\]

and cancellation of `d>0` gives (4). More generally, Chebyshev immediately yields

\[
\left|
\{\gamma:|Q_\nu(\gamma,d)|\ge cd\}
\right|
\le
\frac{2\pi M}{c}.
\tag{6}
\]

Thus a fixed finite-TV mixture can have `Omega(d)` response only on a target-height set of uniformly bounded Lebesgue measure. It cannot cover height intervals whose length tends to infinity without its coefficient mass tending to infinity at least linearly in the covered length.

## 3. The linear budget is sharp in order

The lower bound is not an artifact of estimating signed mixtures by absolute values. The real-axis family from WI-410 already achieves the same asymptotic order.

Take one probe with horizontal scale `a=T`, center `b=0`, and coefficient `T`. Using `artanh x >= x` for `0<=x<1`,

\[
Tq_{T,0}(\gamma,d)
\ge
T\frac{2Td}{\gamma^2+T^2+d^2}.
\]

For `T<=gamma<=2T`, `T>=1`, and `d<=1/2`, the denominator is at most

\[
4T^2+T^2+\frac14
\le \frac{21}{4}T^2,
\]

so (5) follows. The probe has coefficient total variation exactly `T`.

Therefore, for any fixed target response constant bounded away from zero, the least TV order needed to cover a dyadic window is

\[
\boxed{M_T=\Theta(T).}
\tag{7}
\]

Vertical translations may improve constants or permit localized targeting, but they cannot improve the order of the uniform-window budget within this linear mixture architecture. This closes the specific vertical-translation loophole left open in WI-410 for **source-independent uniform height coverage**.

## 4. What this does not close

The scope of the barrier is deliberately narrow.

First, (3) is an `L^1(d gamma)` statement. It does **not** bound the value of a translated mixture on an arbitrary discrete measure-zero set. A construction that somehow knew the ordinates of the exceptional zeros in advance could center narrow probes on those ordinates and is not ruled out by the uniform-coverage corollary. Such adaptive targeting would need its own source-side, non-circular justification before it could serve as a defect-to-zero mechanism.

Second, an `Omega(T)` coefficient budget is not automatically too large for every zeta application. Since a dyadic zero count has order `T log T`, linear coefficient mass is still smaller than the total number of zeros. Equation (7) therefore closes the **fixed finite-budget** escape, not every possible averaged source estimate with a growing budget. Any proposed use must price the actual source-side norm rather than silently identify coefficient TV with an unrelated arithmetic cost.

Third, every profile still scales linearly with horizontal depth. Even a height-uniform translated detector has no fixed positive quantum per off-line zero as `d->0`. The shallow-defect obstruction from WI-409--WI-410 remains: displacement-sensitive information does not become a count of off-line zeros without an independent depth lower bound, quantization law, or nonlinear coercivity.

Finally, infinite-total-variation or distributional combinations, Abel/Carleman limits, nonlinear functionals of translated probes, and genuinely different explicit-formula observables lie outside the theorem. Kondratyuk's Carleman endpoint remains the classical example showing that leaving the finite-budget regime can remove height decay altogether.

## 5. Prior-art and novelty audit

The Blaschke factorization and its zeta interpretation are inherited from the primary sources already audited in WI-410:

- M. Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:`0804.4829v2` (2009), for symmetric Poisson--Schwarz/Blaschke factorizations in `Re s>1/2`;
- J.-F. Burnol, *A note on Nyman's equivalent formulation of the Riemann hypothesis*, Contemp. Math. **287** (2001), 23--26; arXiv:`math/9910055`, for the quantitative zero-product/Nyman connection;
- A. A. Kondratyuk, *A Carleman-Nevanlinna Theorem and Summation of the Riemann Zeta-Function Logarithm*, Computational Methods and Function Theory **4**(2), 391--403, DOI `10.1007/BF03321076`, for the height-unweighted Carleman endpoint.

The prior-art audit also found a neighboring harmonic-analysis literature on translates of the Poisson kernel and on integral logarithmic means of half-plane Blaschke products. In particular, Bruna--Melnikov (Bull. London Math. Soc. 39 (2007), 317--326, DOI `10.1112/blms/bdl039`) study completeness of Poisson-kernel translates, while Mikayelyan--Hayrapetyan (Proceedings of the YSU A 52:3 (2018), 166--171, DOI `10.46991/PYSU:A/2018.52.3.166`) study integral logarithmic means of half-plane Blaschke products. Those are neighboring classical contexts, not evidence for a new zeta theorem here.

No priority claim is made for the one-factor integral identity (2), which is elementary harmonic analysis and may well be implicit or explicit in the Blaschke integral-mean literature. The Mathia contribution recorded here is the exact **budget consequence at the current frontier**: combining that conserved height-area with total variation shows that the vertical-translation escape left by WI-410 costs `Theta(T)` coefficient mass for uniform linear-depth sensitivity on a dyadic height window.

The evidence labels mean:

- `CLASSICAL-IDENTITY`: the half-plane Blaschke factor and the underlying Poisson/logarithmic integral geometry are classical;
- `LITERATURE+DERIVED`: the interpretation as a continuation of the WI-409--WI-410 zeta-defect program uses the audited Burnol--Kunik/Kondratyuk framework;
- `EXACT-DERIVED`: equations (2)--(7), including the `2 pi min(a,d)` area law, finite-TV inequality, and matching `Theta(T)` order, are proved directly above;
- `DECISIVE-NEGATIVE`: vertical translation does not yield a source-independent height-uniform `Omega(d)` detector with fixed finite coefficient budget.

## Consequence for `weil_inertia`

The classical half-plane route now has a sharper ledger. A fixed real-axis probe loses sensitivity with height; scale optimization can improve that loss to `d/gamma`; translating a probe vertically can restore `O(d)` local sensitivity, but covering an expanding height range then requires coefficient mass proportional to the range length. These are different manifestations of the same conserved amount of single-defect Blaschke charge.

Accordingly, further work should not treat vertical translation by itself as a free escape from WI-410. A viable continuation must supply at least one additional ingredient: a source norm for which the required `Theta(T)` translated family is cheap enough to exploit, a non-circular way to target a sparse discrete exceptional set without uniform coverage, a collective identity that aggregates many defects more efficiently than linear TV mixing, or a mechanism whose response is coercive in **count** rather than only in horizontal displacement.
