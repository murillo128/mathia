# AF-267 — Count-preserving near-critical zero surgery defeats uniform vertical robustness

**Status:** `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `MATCHED-CONTROL`, `ZERO-SURGERY`, `STABILITY-OBSTRUCTION`, `HEIGHT-UNIFORM`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-266 shows that a **purely inserted** off-critical zero quartet cannot hide from the full vertical logarithmic-derivative channel on any fixed line `Re(s)=sigma>1`: at the moving quartet height it leaves a positive signal bounded below independently of the zero height. That separation disappears once the matched-control class is enlarged from one-sided insertion to **count-preserving signed replacement**.

Fix

\[
\sigma>1,
\qquad
 a:=\sigma-\frac12>\frac12.
\tag{1}
\]

There is a sequence of entire order-one Riemann-symmetric controls `F_n` such that:

1. each `F_n` is obtained from `xi` by removing two simple critical-line zero pairs and inserting one off-critical symmetric quartet;
2. `F_n(1-s)=F_n(s)` and `F_n(\overline s)=\overline{F_n(s)}`;
3. `F_n(0)=xi(0)` and `F_n(1)=xi(1)`;
4. the upper-half-plane zero count is eventually unchanged exactly, not merely to leading order;
5. every `F_n` has zeros off the critical line; but
6. the renormalized logarithmic derivatives converge to the Riemann one in the **full vertical supremum norm**:

\[
\boxed{
\sup_{t\in\mathbb R}
\left|
\mathcal R_{F_n}(\sigma+it)-\mathcal R_{\xi}(\sigma+it)
\right|
\longrightarrow0,
}
\tag{2}
\]

where, with the same completion normalization as AF-266,

\[
\mathcal R_f(s)
:=\frac{f'}{f}(s)-A(s),
\qquad
A(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi\!\left(\frac s2\right).
\tag{3}
\]

Thus the positive height-uniform margin from AF-266 is a property of the **pure-insertion fiber**, not of the full count-preserving Riemann-symmetric replacement fiber. Exact right-half-plane logarithmic-derivative data remain faithful, but their inverse is not uniformly separated from RH-violating matched controls in this vertical sup metric.

More explicitly, choose distinct simple critical-line zeros

\[
\tau_{1,n}
=\frac12+i(\gamma_n-d_n),
\qquad
\tau_{2,n}
=\frac12+i(\gamma_n+d_n),
\tag{4}
\]

with

\[
\gamma_n\to+\infty,
\qquad
d_n\to0.
\tag{5}
\]

Choose any sequence

\[
0<x_n<a,
\qquad
x_n\to0,
\tag{6}
\]

and put

\[
\rho_n=\frac12+x_n+i\gamma_n.
\tag{7}
\]

Let `P_n` be the polynomial with zero set

\[
\left\{
\rho_n,\overline{\rho_n},1-\rho_n,1-\overline{\rho_n}
\right\},
\tag{8}
\]

and let

\[
Q_{j,n}(s)
=(s-\tau_{j,n})(s-\overline{\tau_{j,n}}),
\qquad j=1,2.
\tag{9}
\]

Define

\[
C_n
:=\frac{Q_{1,n}(0)Q_{2,n}(0)}{P_n(0)},
\qquad
F_n(s)
:=C_n\,P_n(s)\,
\frac{\xi(s)}{Q_{1,n}(s)Q_{2,n}(s)}.
\tag{10}
\]

Then `(2)` obeys the quantitative bound

\[
\boxed{
\left\|\mathcal R_{F_n}-\mathcal R_\xi\right\|_{\sigma,\infty}
\le
\frac{4x_n^2}{a(a^2-x_n^2)}
+
\frac{4d_n^2}{a^3}.
}
\tag{11}
\]

In particular, if eventually `x_n<=a/2`,

\[
\left\|\mathcal R_{F_n}-\mathcal R_\xi\right\|_{\sigma,\infty}
\le
\frac{16}{3}\frac{x_n^2}{a^3}
+
4\frac{d_n^2}{a^3}
\longrightarrow0.
\tag{12}
\]

The conclusion persists when the genuine Riemann channel is referenced to any **fixed finite prime-power prefix** from AF-266. If

\[
R_X(s)=-\sum_{2\le m\le X}\frac{\Lambda(m)}{m^s},
\tag{13}
\]

then for every fixed `X`,

\[
\left|
\|\mathcal R_{F_n}-R_X\|_{\sigma,\infty}
-
\|\mathcal R_\xi-R_X\|_{\sigma,\infty}
\right|
\le
\|\mathcal R_{F_n}-\mathcal R_\xi\|_{\sigma,\infty}
\longrightarrow0.
\tag{14}
\]

So a fixed arithmetic prefix plus unbounded vertical observation has no positive robustness gap against this larger signed replacement class.

## Exact derivation

### 1. Arbitrarily close simple critical-line zero pairs exist at arbitrarily large height

Alpöge--Furman prove unconditionally that, in every sufficiently large dyadic interval,

\[
N_0^{\mathrm s}(T,2T)
\ge
\left(\frac23-o(1)\right)N(T,2T),
\tag{15}
\]

where `N_0^s` counts simple zeros on the critical line and

\[
N(T,2T)\asymp T\log T.
\tag{16}
\]

Hence the interval `[T,2T]`, of length `T`, contains `\gg T\log T` distinct simple critical-line ordinates. Ordering them and applying the pigeonhole principle gives two consecutive such ordinates with gap

\[
O\!\left(\frac1{\log T}\right).
\tag{17}
\]

Choosing a sequence `T_n->infinity`, let their midpoint be `gamma_n` and half-gap be `d_n`. Then `(4)`--`(5)` hold.

No small-gap conjecture, pair-correlation hypothesis, or RH assumption is used. Only the unconditional abundance of simple critical-line zeros and a finite-interval packing argument are needed.

### 2. The zero surgery is entire, symmetric, normalized, and count-preserving

Because `tau_{1,n}` and `tau_{2,n}` are simple zeros of `xi`, division by `Q_{1,n}Q_{2,n}` removes exactly one copy of each conjugate critical-line pair and leaves an entire function. Multiplication by the fixed-degree polynomial `P_n` does not change order one.

The root set of `P_n` is invariant under conjugation and under `z->1-z`, so

\[
P_n(\overline s)=\overline{P_n(s)},
\qquad
P_n(1-s)=P_n(s).
\tag{18}
\]

The same identities hold for each `Q_{j,n}` because `1-\tau_{j,n}=\overline{\tau_{j,n}}`. Therefore `(10)` inherits the Riemann reflection and conjugation symmetries.

Also

\[
P_n(1)=P_n(0),
\qquad
Q_{j,n}(1)=Q_{j,n}(0),
\tag{19}
\]

so the choice of `C_n` gives

\[
F_n(0)=\xi(0),
\qquad
F_n(1)=\xi(1).
\tag{20}
\]

In the upper half-plane, the denominator removes exactly the two zeros at ordinates `gamma_n-d_n` and `gamma_n+d_n`, while `P_n` inserts exactly the two off-critical zeros

\[
\frac12+x_n+i\gamma_n,
\qquad
\frac12-x_n+i\gamma_n.
\tag{21}
\]

Thus once the counting height lies above all three surgery ordinates,

\[
N_{F_n}(Y)=N_\xi(Y)
\tag{22}
\]

counting multiplicity in the upper half-plane. In particular the surgery preserves not only the Riemann--von Mangoldt leading term but the eventual counting function exactly. Since `x_n>0`, each `F_n` has an off-critical conjugate-reflection quartet.

### 3. The upper-half-plane logarithmic-derivative defect is quadratic in the replacement displacement

The scalar `C_n` disappears under logarithmic differentiation. Hence

\[
\mathcal R_{F_n}(s)-\mathcal R_\xi(s)
=
\frac{P_n'}{P_n}(s)
-
\frac{Q_{1,n}'}{Q_{1,n}}(s)
-
\frac{Q_{2,n}'}{Q_{2,n}}(s).
\tag{23}
\]

Fix a real observation height `t` and center first on the upper surgery height. Write

\[
u=t-\gamma_n,
\qquad
z=a+iu.
\tag{24}
\]

The two inserted upper-half-plane roots contribute

\[
I_{x_n}(u)
:=
\frac1{z-x_n}+
\frac1{z+x_n}
=
\frac{2z}{z^2-x_n^2}.
\tag{25}
\]

The two removed critical-line roots contribute

\[
C_{d_n}(u)
:=
\frac1{z-id_n}+
\frac1{z+id_n}
=
\frac{2z}{z^2+d_n^2}.
\tag{26}
\]

Insert the common reference `2/z`. Exactly,

\[
I_x(u)-\frac2z
=
\frac{2x^2}{z(z^2-x^2)},
\tag{27}
\]

while

\[
\frac2z-C_d(u)
=
\frac{2d^2}{z(z^2+d^2)}.
\tag{28}
\]

Because `Re(z)=a` and `0<x<a`,

\[
|z|\ge a,
\qquad
|z-x|\ge a-x,
\qquad
|z+x|\ge a+x,
\tag{29}
\]

and therefore

\[
|z^2-x^2|
=|z-x||z+x|
\ge a^2-x^2.
\tag{30}
\]

Similarly

\[
|z-id|\ge a,
\qquad
|z+id|\ge a,
\qquad
|z^2+d^2|\ge a^2.
\tag{31}
\]

Equations `(27)`--`(31)` give, uniformly in `u`,

\[
|I_x(u)-C_d(u)|
\le
\frac{2x^2}{a(a^2-x^2)}
+
\frac{2d^2}{a^3}.
\tag{32}
\]

### 4. The lower conjugate surgery obeys the same bound

The lower inserted pair is centered at `-gamma_n`, as are the two removed conjugate critical-line zeros. Repeating the same calculation with

\[
u=t+\gamma_n
\tag{33}
\]

gives exactly the bound `(32)` for the lower-half-plane contribution.

Summing upper and lower defects yields `(11)`. Since `x_n->0` and `d_n->0`, equation `(2)` follows. If `x_n<=a/2`, then

\[
a^2-x_n^2\ge\frac34a^2,
\tag{34}
\]

which gives the simplified estimate `(12)`.

The cancellation mechanism is transparent. AF-266's pure insertion has unmatched positive Cauchy/Poisson mass at the moving height. Here the inserted upper pair converges simultaneously in horizontal displacement `x_n` and vertical splitting `d_n` to the same double critical-line location represented by the removed pair. The leading `2/z` contribution cancels exactly; the residual is second order in `x_n` and `d_n`.

### 5. Fixed finite source prefixes cannot restore a positive metric margin

For every fixed `X`, the reverse triangle inequality for norms gives

\[
\left|
\|\mathcal R_{F_n}-R_X\|_{\sigma,\infty}
-
\|\mathcal R_\xi-R_X\|_{\sigma,\infty}
\right|
\le
\|\mathcal R_{F_n}-\mathcal R_\xi\|_{\sigma,\infty}.
\tag{35}
\]

Equation `(2)` proves `(14)`. Thus even if `X` was chosen using AF-266 so that the true Riemann residual is uniformly approximated to a small fixed tolerance, the same tolerance cannot separate all count-preserving signed controls: the RH-violating `F_n` eventually lie arbitrarily close in exactly the full vertical metric that produced AF-266's insertion-only lower bound.

This does **not** say that a finite prime prefix determines the controls or that `F_n` has an Euler product. It says only that metric proximity to the genuine prime-side residual in this observation norm is not a robust discriminator on the enlarged control fiber.

## What this changes in the Arithmetic Fidelity audit

AF-265 showed that compact-open control is too weak because dangerous zeros can escape every bounded observation window. AF-266 repaired that specific defect for pure insertion by letting the observer follow the zero to arbitrary height. AF-267 shows that **height reach and vertical uniformity alone still do not solve the stability problem** once the control may replace nearby critical-line mass rather than only add mass.

The hierarchy is therefore sharper:

- fixed compact or fixed vertical bands lose high divisor components by escape to infinity;
- a full vertical logarithmic-derivative channel detects any unmatched inserted quartet with a fixed margin;
- the same full vertical channel has zero separation radius from count-preserving off-critical replacements that coalesce with nearby removed critical-line zeros.

The remaining zeta-specific question cannot be phrased merely as “retain the whole vertical line.” A robust obstruction must either restrict the admissible source class strongly enough to forbid this signed replacement fiber, retain a metric that prices the horizontal/vertical divisor displacement at the scale being collapsed here, or use an additional arithmetic/global relation that is not continuous under these synthetic replacements.

This is a stability obstruction for **off-criticality itself**, but not yet the phase-specific obstruction in MI-024. The construction does not prove that the inserted quartet has a prescribed positive `K_pc` or any particular dangerous Keiper approximation exponent. Its ordinate is selected by a close pair of actual critical-line zeros, and no source-specific Diophantine property of the resulting phase is asserted. Consequently AF-267 narrows the admissible notion of a robust source witness without resolving the open task of controlling the actual Keiper phase.

## Prior art and novelty assessment

The ingredients are deliberately classical or externally supplied rather than claimed as new in isolation.

The abundance input is Levent Alpöge and Ralph Furman, **“More than two thirds of the zeta zeros are simple and on the critical line,”** arXiv:`2608.13637` (2026). Their theorem gives `(15)` together with the standard Riemann--von Mangoldt scale `(16)`; the existence of a pair with gap `O(1/log T)` then follows immediately by pigeonhole. The broader study of gaps between zeta zeros is classical; no new zero-gap theorem is claimed here.

The rational-function estimate `(27)`--`(32)` is elementary resolvent/Cauchy-transform stability. No novelty is claimed for the fact that two nearby signed atomic configurations have close Cauchy transforms on a line a fixed positive distance away.

The Arithmetic Fidelity contribution is the **specific matched-control comparison against AF-266**: the exact height-uniform positive margin established for pure quartet insertion collapses to zero on a natural Riemann-symmetric, count-preserving replacement fiber while endpoint normalization and eventual zero counts are retained. This is a derived boundary on the robustness of that proposed information channel, not a broad theorem of complex analysis or a new result about the actual Riemann zeros.

## Boundaries and failure modes

- **The controls are synthetic, not L-functions.** No Euler product, Dirichlet-series coefficients, Selberg-class axioms, or arithmetic origin is asserted for `F_n`. A sufficiently strong source category may forbid this surgery; identifying the weakest such restriction is exactly the remaining fidelity problem.
- **Exact equality is not claimed.** AF-019's exact logarithmic-derivative faithfulness is untouched. For every finite `n`, `\mathcal R_{F_n}\ne\mathcal R_\xi`; the result concerns the absence of a positive stability margin.
- **AF-266 remains correct.** Its lower bound applies to one-sided quartet insertion. AF-267 changes the control family by removing nearby existing zeros, which cancels the leading moving-height signature.
- **No RH counterexample is produced.** `F_n` is not `xi`, and nothing here implies that the actual zeta function has an off-critical zero.
- **No dangerous Keiper phase is certified.** The inserted quartet is off critical, but its `K_pc` value is uncontrolled. The finding therefore constrains source-observation stability rather than resolving MI-024's phase-specific arithmetic question.
- **The metric is fixed.** The theorem concerns the full vertical supremum norm on one fixed line `Re(s)=sigma>1`. A stronger norm involving derivatives, multiple lines, height-dependent weights, or direct divisor transport may separate the controls.
- **Simplicity matters only to make the written quotient clean.** The Alpöge--Furman theorem supplies abundant simple critical-line zeros unconditionally. A version using multiplicities could be formulated more generally, but no such extension is needed here.

## Evidence classification

`EXACT-DERIVED` for the surgery construction and vertical norm estimate, conditional only on the cited unconditional Alpöge--Furman theorem as literature input. `LITERATURE+DERIVED` for the existence of the close simple critical-line pairs. The finding is an Arithmetic Fidelity stability obstruction with **no broad novelty claim** for its classical analytic ingredients.