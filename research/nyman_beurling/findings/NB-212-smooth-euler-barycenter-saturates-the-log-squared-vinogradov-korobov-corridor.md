# NB-212 — A smooth full-Euler barycenter already saturates the log-squared Vinogradov--Korobov corridor

**Date:** 2026-09-18  
**Status:** `DERIVED + REFINEMENT + REPRESENTATION-AUDIT + SOURCE-ACQUISITION + POSITIVE-EULER + VINOGRADOV-KOROBOV + METHOD-BOUNDARY + NB-194/NB-211-REFINEMENT`.

`NB-210`--`NB-211` reach an order-one positive-return gap by first transferring a small Euler defect to a plateau of nearly maximal prime Dirichlet values and then applying a prime-supported Halasz inequality. The proof-level refinement in `NB-211`, however, exposes more information than that route uses: its Vinogradov--Korobov contour already gives a pointwise smoothed von-Mangoldt correlation estimate. Applying that estimate directly to a fixed nonnegative smooth window inside the actual Euler shell yields the same log-squared diagonal corridor with **one source-faithful scalar barycenter**, without prime-only reduction, harmonic amplification, or a large-value theorem.

Keep

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\]

and the normalized positive Euler defect

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\tag{1}
\]

Fix once and for all a nonzero function

\[
0\le f\le1,
\qquad
f\in C_c^\infty((1,e^\Delta)).
\tag{2}
\]

Define the smooth full-source barycenter

\[
M_{a,f}(t)
:=
\sum_n \Lambda(n)n^{-1-a-it}f(n/x_a).
\tag{3}
\]

Then there are constants `kappa_f,eta_f>0`, depending only on the fixed shell and `f`, such that for all sufficiently small `a`,

\[
\boxed{
1\le |t|\le
\exp\!\left(
\kappa_f\frac{X_a^{3/2}}{(\log X_a)^2}
\right)
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge\eta_f.
}
\tag{4}
\]

Thus the quantitative corridor of `NB-211` is already visible in a **single smooth full-von-Mangoldt observable**. The harmonic plateau remains a valid independent derivation, but it is not what creates the `X_a^(3/2)/(log X_a)^2` scale once the full Vinogradov--Korobov contour estimate has been exposed.

The same calculation also isolates a sharp method tariff. If a contour argument has normalized error

\[
L(Q)
\exp\!\left[
-c\frac{X}{Q^{2/3}(\log Q)^{1/3}}
\right],
\qquad Q=\log(10+|t|),
\tag{5}
\]

then **any positive power prefactor** `L(Q)=Q^{A+o(1)}`, `A>0`, forces the same log-squared threshold. Replacing the prefactor by a polylogarithm would move the method arbitrarily close to the Ford scale, while reaching the exact Ford scale by this contour mechanism requires a bounded prefactor (up to constants). This identifies the remaining quantitative target more precisely than “exploit more harmonics.”

## 1. A positive return forces one smooth full-source barycenter to stay near its mass

Put

\[
m_{a,f}:=M_{a,f}(0)
=
\sum_n\Lambda(n)n^{-1-a}f(n/x_a).
\tag{6}
\]

Since `f` is nonnegative and supported inside the same shell as (1),

\[
\begin{aligned}
m_{a,f}-\Re M_{a,f}(t)
&=
\sum_n\Lambda(n)n^{-1-a}f(n/x_a)
\bigl(1-\cos(t\log n)\bigr)\\
&\le
\sum_{x_a\le n<y_a}
\Lambda(n)n^{-1-a}|e^{-it\log n}-1|\\
&=D_a\mathcal A_a(t).
\end{aligned}
\tag{7}
\]

The prime number theorem on a fixed multiplicative shell gives

\[
D_a=e^{-r_0}\Delta+o(1),
\tag{8}
\]

and, uniformly as `a->0`,

\[
\boxed{
m_{a,f}
=
e^{-r_0}I_f+o(1),
\qquad
I_f:=\int_1^{e^\Delta}f(u)\frac{du}{u}>0.
}
\tag{9}
\]

Consequently a sufficiently small constant value of `mathcal A_a(t)` forces

\[
|M_{a,f}(t)|
\ge \Re M_{a,f}(t)
\ge e^{-r_0}I_f-O(\mathcal A_a(t))-o(1).
\tag{10}
\]

No prime selection or harmonic lifting appears here. This is the actual positive von-Mangoldt source restricted by a fixed nonnegative window.

## 2. The `NB-211` contour estimate applies directly to this barycenter

Write

\[
g_a(u):=u^{-1-a}f(u).
\tag{11}
\]

The family `g_a` stays in a bounded subset of `C_c^infty((1,e^Delta))` for small `a`, and

\[
M_{a,f}(t)
=x_a^{-1-a}
\sum_n\Lambda(n)g_a(n/x_a)n^{-it}.
\tag{12}
\]

The smoothed prime-power kernel estimate derived in `NB-211` is not tied to the particular cutoff used there. Repeating the same Mellin inversion with the uniformly smooth family `g_a`, shifting to a fixed safe fraction of the Vinogradov--Korobov zero-free width, gives

\[
\boxed{
M_{a,f}(t)
=
x_a^{-a-it}F_a(t)
+O_f\!\left(
x_a^{-a}E_{\rm VK}(X_a,t)
\right),
}
\tag{13}
\]

where

\[
F_a(t):=
\int_1^{e^\Delta}f(u)u^{-1-a-it}\,du,
\tag{14}
\]

and, with

\[
Q_t:=\log(10+|t|),
\qquad
R_t:=Q_t^{2/3}(\log Q_t)^{1/3},
\tag{15}
\]

one may take

\[
\boxed{
E_{\rm VK}(X,t)
:=
Q_t^2
\exp\!\left[-c\frac{X}{R_t}\right]
}
\tag{16}
\]

for some fixed `c>0`. As in `NB-211`, bounded-height pieces and Mellin tails are absorbed into the constants. Prime powers are included automatically because the Dirichlet series is `-zeta'/zeta`; there is no prime-only approximation in (13).

For completeness, the residue producing the first term in (13) is the pole of `-zeta'/zeta` at `1`. The shifted vertical integral contributes `x_a^{-a}E_VK`: the horizontal displacement supplies `exp(-cX_a/R_t)`, while the local logarithmic-derivative bound on the safe contour supplies the retained polynomial factor in `Q_t`. This is exactly the source of the error already isolated in `NB-211`.

## 3. A fixed smooth window has a uniform nonzero-frequency contraction

At `a=0`, change variables `u=e^v` in (14):

\[
F_0(t)
=
\int_0^\Delta f(e^v)e^{-itv}\,dv.
\tag{17}
\]

This is the Fourier transform of a nonzero nonnegative smooth density supported on an interval. Therefore

\[
|F_0(t)|<F_0(0)=I_f
\qquad(t\ne0),
\tag{18}
\]

by the strict triangle inequality. Since `F_0(t)->0` as `|t|->infty` and `F_0` is continuous, there exists a fixed `delta_f>0` such that

\[
\boxed{
\sup_{|t|\ge1}|F_0(t)|
\le(1-\delta_f)I_f.
}
\tag{19}
\]

Moreover

\[
\sup_t|F_a(t)-F_0(t)|
\le
\int_1^{e^\Delta}
f(u)u^{-1}|u^{-a}-1|\,du
=O_f(a),
\tag{20}
\]

so for all sufficiently small `a`,

\[
\sup_{|t|\ge1}|F_a(t)|
\le
\left(1-\frac{\delta_f}{2}\right)I_f.
\tag{21}
\]

Combining (13), `x_a^{-a}=e^{-r_0}`, and (21), whenever `E_VK(X_a,t)=o(1)` uniformly we have

\[
|M_{a,f}(t)|
\le
e^{-r_0}
\left(1-\frac{\delta_f}{2}ight)I_f
+o(1).
\tag{22}
\]

On the other hand, (8)--(10) show that if `mathcal A_a(t)<=eta_f`, with `eta_f>0` chosen sufficiently small once and for all, then

\[
|M_{a,f}(t)|
\ge
e^{-r_0}
\left(1-\frac{\delta_f}{4}ight)I_f
+o(1),
\tag{23}
\]

which contradicts (22). Thus a constant positive-return gap follows from one smooth barycenter as soon as the contour error is uniformly small.

## 4. Solving the same contour error reproduces the log-squared corridor

Let

\[
Q_a
:=
\kappa\frac{X_a^{3/2}}{(\log X_a)^2}
\tag{24}
\]

with fixed `kappa>0`. Uniformly for `Q_t<=Q_a+O(1)`,

\[
Q_t^{2/3}(\log Q_t)^{1/3}
\le
\left(
\kappa^{2/3}
\left(\frac32\right)^{1/3}
+o(1)
\right)
\frac{X_a}{\log X_a}.
\tag{25}
\]

Hence

\[
\frac{cX_a}{R_t}
\ge
\left(C\kappa^{-2/3}+o(1)\right)\log X_a
\tag{26}
\]

for some fixed `C>0`, whereas

\[
2\log Q_t
\le
3\log X_a-4\log\log X_a+O(1).
\tag{27}
\]

Choosing `kappa=kappa_f` small enough makes (16) tend to zero uniformly throughout

\[
1\le|t|\le\exp(Q_a).
\tag{28}
\]

Equations (22)--(23) then prove (4).

The quantitative range therefore agrees with `NB-211`, but the logical route is shorter:

\[
\text{small positive Euler defect}
\Longrightarrow
\text{one large smooth full-source barycenter}
\Longrightarrow
\text{Vinogradov--Korobov contour contradiction}.
\tag{29}
\]

The prime harmonic plateau and prime Halasz inequality remain mathematically correct, but they are not load-bearing for this particular diagonal range after the contour estimate has been sharpened to its natural zero-free width.

## 5. Any polynomial `Q`-prefactor forces the same log-squared threshold

The preceding calculation is more general than the exponent `2` in (16). Suppose a source-faithful contour estimate has error

\[
\mathcal E(X,Q)
=
L(Q)
\exp\!\left[-c
\frac{X}{Q^{2/3}(\log Q)^{1/3}}
\right].
\tag{30}
\]

Test the scale

\[
Q
=
\kappa\frac{X^{3/2}}{(\log X)^\gamma}.
\tag{31}
\]

Then

\[
\boxed{
\frac{X}{Q^{2/3}(\log Q)^{1/3}}
=
\left(C\kappa^{-2/3}+o(1)\right)
(\log X)^{(2\gamma-1)/3}
}
\tag{32}
\]

for a fixed `C>0`.

If

\[
L(Q)=Q^{A+o(1)},
\qquad A>0,
\tag{33}
\]

then

\[
\log L(Q)
=
\left(\frac{3A}{2}+o(1)\right)\log X.
\tag{34}
\]

For `gamma<2`, the saving exponent in (32) is `o(log X)`, so it cannot absorb (34). At `gamma=2` the two are both order `log X`, and a sufficiently small fixed `kappa` makes the saving win. Therefore

\[
\boxed{
L(Q)=Q^{A+o(1)},\ A>0
\quad\Longrightarrow\quad
\gamma=2
\text{ is the universal VK contour threshold up to constants.}
}
\tag{35}
\]

The conclusion is independent of the positive power `A`: improving `Q^2` to `Q`, `Q^(1/100)`, or any other fixed positive power changes constants but not the log-squared exponent.

The situation changes qualitatively if

\[
L(Q)=(\log Q)^{B+o(1)}.
\tag{36}
\]

Then `log L(Q)=O(log log X)`, so every fixed

\[
\gamma>\frac12
\tag{37}
\]

makes the saving in (32) dominate the prefactor. Thus a merely polylogarithmic prefactor would push the same contour mechanism to

\[
Q
=
\frac{X^{3/2}}{(\log X)^{1/2+\epsilon}}
\tag{38}
\]

for every fixed `epsilon>0`.

At the exact Ford scale `gamma=1/2`, the exponential saving in (32) is only a fixed constant depending on `kappa`. Any prefactor tending to infinity therefore defeats this absolute contour bound. A bounded prefactor, by contrast, would in principle permit a constant-gap statement at

\[
Q
\asymp
\kappa\frac{X^{3/2}}{\sqrt{\log X}}
\tag{39}
\]

for sufficiently small `kappa`, because the constant exponential saving can then be made smaller than the fixed Fourier-contraction margin from (19).

This gives a precise hierarchy for the remaining analytic target:

\[
\boxed{
\begin{array}{ccl}
Q^{A} &\Rightarrow& X^{3/2}/(\log X)^2,\\[2mm]
(\log Q)^B &\Rightarrow& X^{3/2}/(\log X)^{1/2+\epsilon},\\[2mm]
O(1) &\Rightarrow& \text{Ford-scale access in principle.}
\end{array}
}
\tag{40}
\]

Equation (40) is a method phase diagram, not a claim that the stronger correlation estimates currently exist.

## 6. Toeplitz/AP structure alone cannot remove a pointwise correlation prefactor

`NB-211` left phase-pinned arithmetic-progression structure as a possible way to improve the prime-correlation step. There is a useful representation boundary on that idea. Suppose an argument opens correlations on the sample set

\[
t,2t,\ldots,Ht
\]

and retains only that the normalized correlation matrix is Hermitian positive semidefinite, Toeplitz, has diagonal `1`, and satisfies a uniform off-diagonal envelope

\[
|G_{hk}|\le\rho
\qquad(h\ne k).
\tag{41}
\]

Those data alone cannot force any cancellation in the coherent direction. Indeed, for every `0<=rho<=1`,

\[
\boxed{
G^{(\rho)}
:=(1-\rho)I_H+\rho\mathbf 1\mathbf 1^*
}
\tag{42}
\]

is Hermitian, positive semidefinite and Toeplitz, has diagonal `1`, and has every off-diagonal entry equal to `rho`. Its coherent eigenvalue is

\[
\boxed{
\lambda_{\rm coh}
=1+(H-1)\rho.
}
\tag{43}
\]

Thus the row-sum accumulation permitted by a pointwise envelope is exactly realizable by a positive semidefinite Toeplitz control. Increasing `H`, changing deterministic weights, or invoking Toeplitz structure cannot by itself turn a bound `|G_r|<=rho` into cancellation of the lags. A genuine AP improvement must retain additional arithmetic information such as signed/oscillatory dependence on the lag `r`, a mean-square bound over the lags, or another estimate that beats

\[
\sum_r |w_r|\,|G_r|
\le
\rho\sum_r|w_r|.
\tag{44}
\]

This is a generic matrix obstruction, not an arithmetic theorem. Its role here is diagnostic: the remaining suggestion “exploit the arithmetic progression” becomes mathematically meaningful only if the proposed estimate uses **more than** positivity, Toeplitzness and the same uniform Vinogradov--Korobov envelope.

## 7. Representation and prior-art audit

**Representation audit.** The implication (7) is source-faithful: it uses the actual positive von-Mangoldt weights of the Euler shell. Equation (13) is also source-faithful because `-zeta'/zeta` contains the same prime-power coefficients. The only localization is multiplication by one fixed nonnegative smooth function inside the shell; no coordinates are individually renormalized and no sparse prime code is substituted for the source.

The Fourier-contraction step (19) is generic harmonic analysis, and the phase diagram (35)--(40) is generic once a Vinogradov--Korobov-shaped contour error is given. The Toeplitz matched control (42) is entirely generic linear algebra. These generic pieces are retained because they distinguish which part of the present frontier is genuinely arithmetic: obtaining a better **actual von-Mangoldt correlation estimate** than the polynomial-prefactor contour bound.

**Prior-art audit.** Smoothed explicit formulas obtained from Mellin inversion of `-zeta'/zeta`, Vinogradov--Korobov zero-free contours, and the elementary equicorrelation matrix (42) are classical technology. No novelty is claimed for any of them. The load-bearing literature dependencies are already recorded in `SOURCES.md`: Bellotti's Vinogradov--Korobov zero-free region and the Matomaki--Radziwill proof whose prime-power contour kernel was unpacked in `NB-211`. A targeted search found the standard equicorrelation/Toeplitz matrix literature and near-one logarithmic-derivative estimates, but no additional theorem is required here, so `SOURCES.md` does not need another anchor.

The project-local delta is the coupling and the causal correction: the `NB-211` contour estimate, applied directly to a positive smooth window of the **full Euler source**, already gives its log-squared constant-gap corridor. The harmonic plateau is therefore not yet evidence that arithmetic-progression structure has bought extra height.

## 8. Adversarial checks and boundaries

**The window has fixed positive source mass.** Equation (9) prevents the contradiction from being manufactured by a vanishing subwindow. Any fixed nonzero nonnegative smooth `f` supported in the shell has a positive limiting mass.

**The fixed-frequency main term is not discarded.** For bounded nonzero `t`, the pole contribution in (13) need not be small. The proof uses the strict uniform Fourier contraction (19), not a false claim that the main term vanishes for every `|t|>=1`. Riemann--Lebesgue decay is used only to make the supremum on the unbounded region compactly controllable.

**Uniformity in `a` is explicit.** The smooth family `g_a(u)=u^(-1-a)f(u)` has uniformly bounded seminorms and converges uniformly with all needed derivatives on the fixed compact support. Equation (20) makes the main-term contraction uniform.

**The contour result is not stronger than its input.** The method inherits the same Vinogradov--Korobov width and polynomial logarithmic-derivative prefactor as `NB-211`. Equation (4) matches that range; it does not claim to reach the farther Ford corridor.

**The phase diagram concerns this contour architecture.** Equation (35) does not say that every analytic method with a polynomial factor must stop at log-squared height. It says that any estimate of the explicit form (30), with the Vinogradov--Korobov width fixed and a positive-power prefactor in `Q`, has that threshold when one asks the error itself to be uniformly small.

**Positivity remains load-bearing.** Equation (7) fails as a coercive statement for signed or complex source combinations because cancellation can occur before individual phases approach one. This finding does not advance the signed/complex branch.

**The destination bridge remains missing.** As in `NB-194`--`NB-211`, nothing here proves that a near-optimal Nyman--Beurling approximant must make `mathcal A_a(t)` small. Equation (4) is a source-acquisition obstruction, not a lower bound for the optimal Nyman distance.

## 9. Consequence for the research frontier

The positive-source frontier should be read differently after this audit. The best current order-one diagonal gap does **not** require a growing or even fixed harmonic plateau once the `NB-211` contour estimate is available; one smooth full-Euler barycenter already sees it. Therefore a future AP-based improvement is only substantive if it produces new cancellation across the actual lagged prime correlations that is absent from the one-frequency contour estimate.

Quantitatively, the remaining gap to `NB-205` is now a prefactor problem with a clear scale. A reduction from `Q^A` to a polylogarithmic prefactor would move the contour mechanism from `(log X)^2` to `(log X)^(1/2+epsilon)` for every fixed `epsilon>0`; exact Ford-scale access requires a bounded prefactor, or a different mechanism that does not estimate every lag by one absolute contour envelope. The larger structural frontiers are unchanged: signed/complex synthesis and the destination-coupled theorem remain necessary before any source-side return obstruction can become a quantitative Nyman--Beurling distance theorem.
