# WP-180 — Dissipative Schur passivity does not control boundary-phase sign

**Status:** `EXACT-SCALAR-COUNTEREXAMPLE + POSITIVE-REAL-PASSIVE-REALIZATION + MATCHED-LOSSLESS-CONTROL + TUNABLE-SIGN-REVERSAL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION`.

`WP-179` classifies the lossless modified-determinant route: ordinary determinant and `det_2` inherit a one-sided boundary-phase law from positive passive delay, while higher `det_m` do not. It deliberately leaves **dissipative/nonunitary lifts** open. The first question for that escape is therefore more primitive than any determinant regularization:

> if a Mathia boundary object is passive but genuinely dissipative, does Schur/bounded-real contractivity itself still force a one-sided boundary phase?

The answer is **no**, already for the simplest scalar rational passive one-port. Let

\[
S_{a,b}(s)=\frac{s+a}{s+b},
\qquad 0<a<b.
\tag{1}
\]

For `Re s>0`,

\[
|s+b|^2-|s+a|^2
=
2(b-a)\operatorname{Re}s+b^2-a^2>0,
\tag{2}
\]

hence

\[
|S_{a,b}(s)|<1.
\tag{3}
\]

Thus `S_{a,b}` is a strict scalar Schur/bounded-real transfer on the right half-plane. More strongly, it is not merely an abstract contractive function: under the normalized impedance/scattering Cayley transform

\[
S=\frac{Z-1}{Z+1},
\tag{4}
\]

it comes from

\[
Z_{a,b}(s)
=
\frac{1+S_{a,b}(s)}{1-S_{a,b}(s)}
=
\frac{2s+a+b}{b-a}
=
\frac{a+b}{b-a}+
\frac{2}{b-a}s.
\tag{5}
\]

This is positive real for `Re s>0` and is exactly the impedance of a positive resistor plus positive inductive term after normalization. Therefore (1) sits inside the elementary physical passive-scattering class, with strict dissipation on every finite boundary frequency:

\[
|S_{a,b}(i\omega)|^2
=
\frac{a^2+\omega^2}{b^2+\omega^2}<1.
\tag{6}
\]

Nevertheless its unwrapped boundary phase

\[
\theta_{a,b}(\omega)
:=
\arg S_{a,b}(i\omega)
=
\arctan\frac{\omega}{a}
-
\arctan\frac{\omega}{b}
\tag{7}
\]

has derivative

\[
\boxed{
\theta'_{a,b}(\omega)
=
\frac{a}{a^2+\omega^2}
-
\frac{b}{b^2+\omega^2}
=
\frac{(b-a)(ab-\omega^2)}
{(a^2+\omega^2)(b^2+\omega^2)}.
}
\tag{8}
\]

Hence

\[
\theta'_{a,b}(\omega)
\begin{cases}
>0,& |\omega|<\sqrt{ab},\\
=0,& |\omega|=\sqrt{ab},\\
<0,& |\omega|>\sqrt{ab}.
\end{cases}
\tag{9}
\]

The sign reversal is invariant under the global phase-orientation convention: reversing the convention multiplies (8) by `-1` but cannot make it one-sided. Therefore

\[
\boxed{
\text{passive Schur contractivity}
\;\not\Longrightarrow\;
\text{one-sided boundary-phase derivative}
}
\tag{10}
\]

in the genuinely dissipative/nonunitary class.

This is a decisive narrowing for the open escape left by `WP-179`. Dissipation can remove the lossless phase-sign obstruction, but it removes it by making phase orientation **less constrained**, not by providing a new positive theorem. A dissipative construction that reproduces the sign change of the real-place Gamma phase therefore does not acquire Weil-type positivity merely because it is passive. It needs an additional Mathia-native coercive/order theorem stronger than Schur contractivity.

## 1. The counterexample is an exact passive one-port, not a hand-picked analytic transfer

The branch contract excludes arbitrary analytic fitting, so it matters that (1) has an intrinsic passive realization independent of the zeta/Gamma target.

For the positive-real impedance (5), write

\[
Z_{a,b}(s)=R+Ls,
\qquad
R=\frac{a+b}{b-a}>0,
\qquad
L=\frac{2}{b-a}>0.
\tag{11}
\]

For `s=x+iy` with `x>0`,

\[
\operatorname{Re}Z_{a,b}(s)=R+Lx>0.
\tag{12}
\]

Thus it is the elementary resistor--inductor positive-real impedance. Applying the standard Cayley conversion from impedance to normalized reflection coefficient gives exactly (1):

\[
\frac{Z_{a,b}-1}{Z_{a,b}+1}
=
\frac{s+a}{s+b}.
\tag{13}
\]

Equation (6) makes the lost energy visible directly. The deficit is

\[
1-|S_{a,b}(i\omega)|^2
=
\frac{b^2-a^2}{b^2+\omega^2}>0.
\tag{14}
\]

No zero data, prime data, Gamma factor, regularization polynomial, spectral placement, or chosen kernel enters this construction. It is therefore an appropriate arithmetic-free matched control for any proposal claiming that **dissipative passivity itself** explains a signed archimedean phase.

## 2. Dissipation permits a tunable phase hump

For positive frequency, (7) satisfies

\[
\theta_{a,b}(0)=0,
\qquad
\theta_{a,b}(\omega)>0\quad(\omega>0),
\qquad
\lim_{\omega\to\infty}\theta_{a,b}(\omega)=0.
\tag{15}
\]

So the phase rises, reaches its maximum exactly at

\[
\omega_*=\sqrt{ab},
\tag{16}
\]

and then falls back to zero. The sign change in (8) is therefore structural, not a numerical accident.

Moreover the transition can be placed at **any prescribed positive frequency** without leaving the same passive class. Given `Omega>0` and any `c>1`, choose

\[
a=\frac{\Omega}{c},
\qquad
b=c\Omega.
\tag{17}
\]

Then `0<a<b` and

\[
\sqrt{ab}=\Omega.
\tag{18}
\]

Thus the location of a positive-to-negative phase-slope transition is freely tunable inside a two-parameter family of elementary passive dissipative systems. Qualitative agreement with a target sign transition is consequently extremely weak evidence: passivity does not select where that transition occurs.

For the concrete control `a=1`, `b=4`,

\[
\theta'(0)=\frac34>0,
\qquad
\theta'(2)=0,
\qquad
\theta'(3)=\frac1{10}-\frac4{25}=-\frac3{50}<0.
\tag{19}
\]

These values provide a direct exact check of (8), with no numerical fitting.

## 3. Matched lossless control isolates what was lost

The distinction from `WP-171`--`WP-179` is precisely **inner versus non-inner** boundary behavior. In the lossless scalar class, boundary values are unimodular and the inner/all-pass phase derivative has a fixed orientation after choosing the half-plane convention. This is the classical phase-monotonicity mechanism behind positive Wigner--Smith/delay forms and the order-one/order-two results already used by the branch.

Equation (6) shows that `S_{a,b}` leaves that inner boundary immediately: finite-frequency modulus is strictly below one. The outer/dissipative part now carries amplitude information, and its phase need not inherit the inner orientation. Equation (8) proves this in the smallest possible rational example.

This matched comparison matters because it rules out a misleading inference:

\[
\text{lossless passive phase is one-sided}
\quad\not\Rightarrow\quad
\text{dissipative passive phase is one-sided}.
\tag{20}
\]

The positivity of the underlying energy balance survives as contractivity, but the scalar boundary phase is no longer an order-preserving readout of that positivity.

## 4. Consequence for the source-derived Gamma phase

`WP-169`--`WP-179` use the exact real-place phase

\[
R_\infty(t)
=
\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})}
=e^{i\phi_\infty(t)},
\tag{21}
\]

whose derivative is

\[
\phi_\infty'(t)
=
\log\pi-
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right).
\tag{22}
\]

That derivative is positive near the origin and negative for sufficiently large positive `t`. Lossless inner/passive phase monotonicity therefore obstructs a direct realization. A dissipative Schur lift removes that particular contradiction because (8) can have the same qualitative sign pattern.

But (17)--(18) show why this is **not** positive evidence for the research mandate. The crossover can be moved arbitrarily using an arithmetic-free resistor--inductor control. Therefore a proposed dissipative realization that merely reproduces the Gamma sign change has explained no global Weil positivity. It has only entered a category flexible enough to mimic the sign pattern.

To become relevant, a dissipative Mathia construction must supply at least one stronger source-derived statement, for example a canonical positive kernel, storage inequality, Herglotz measure, de Branges-type norm, or finite--archimedean coupled form whose sign follows independently from geometry and whose scalarization yields the exact finite-prime plus Gamma/polar terms. The theorem must restrict the admissible dissipative class before seeing the target, not select `a,b`-like parameters because they match (22).

## 5. Aggressive falsification and exact scope

This finding **does not** prove that dissipative/nonunitary lifts are impossible. It proves the narrower and more useful no-go:

\[
\boxed{
\text{Schur/bounded-real passivity alone cannot be the missing positivity theorem.}
}
\tag{23}
\]

Several stronger possibilities remain open. A source-derived dissipative realization may carry a matrix-valued positive-real measure whose relevant quadratic form has a sign even though `arg det S` does not. A nonseparable finite--archimedean assembly may become positive only after quotient/compression. A canonical outer factor could be constrained by arithmetic geometry rather than chosen freely. Singular/domain-changing limits and indefinite or infinite-index structures are also outside the scalar control above.

Conversely, adding only ordinary passivity, stability, minimum-phase location, rationality, or finite-dimensional realizability does **not** evade the counterexample. `S_{a,b}` is stable, rational, minimum phase, strictly Schur, physically passive, and one-dimensional, yet its phase slope changes sign. Any proposed theorem using only those hypotheses is therefore false.

The result also does not depend on determinant regularization. The sign loss occurs in the raw scalar transfer before `det_m`, spectral shift, or trace regularization is introduced. Thus it is logically independent of the higher-counterterm mechanism classified in `WP-179` and closes a genuinely different attempted escape.

## 6. Prior-art and novelty audit

The systems theory used here is classical. The Schur class is the standard contractive transfer-function class for passive system realizations. A modern operator-theoretic reference is Lassi Lilleberg, *Minimal Passive Realizations of Generalized Schur Functions in Pontryagin Spaces*, Complex Analysis and Operator Theory 14 (2020), DOI `10.1007/s11785-020-00993-5`; in the Hilbert-space case it recalls the standard equivalence between passive transfer functions and ordinary Schur functions. Transfer-function realizations of Schur functions via contractive/isometric colligations are also standard in realization theory.

The inner/all-pass versus outer/minimum-phase phase distinction is likewise prior art. Pei Dang and Tao Qian, *Analytic Phase Derivatives, All-Pass Filters and Signals of Minimum Phase*, IEEE Transactions on Signal Processing 59(10), 4708--4718 (2011), DOI `10.1109/TSP.2011.2160260`, develops the fixed-orientation phase-derivative property for inner/all-pass functions and its relation to minimum-phase factorization. Positive-real impedance and the Cayley transformation between impedance and scattering descriptions are classical network theory.

No novelty is claimed for the rational function (1), the derivative (8), positive-real/passive realization, or the general fact that dissipative filters can have non-monotone phase. The Mathia-specific delta is the **adversarial use of this elementary passive control to close the live branch inference left by `WP-179`**:

\[
\text{allowing dissipation removes the lossless Gamma-phase obstruction,}
\]

but

\[
\boxed{
\text{it simultaneously removes any phase-sign conclusion obtainable from passivity alone.}
}
\tag{24}
\]

Therefore the dissipative escape is not a positivity mechanism until an additional source-native order theorem is exhibited. This is a decisive branch narrowing, not a new theorem in passive-system theory and not a proof of Weil positivity.

## 7. Research consequence

After `WP-179` and the present control, the useful boundary is sharper. Ordinary lossless passivity is too rigid to reproduce the signed real-place phase in the direct determinant channels already tested. Ordinary dissipative passivity is flexible enough to reproduce a sign change, but **too weak to certify its sign geometrically**.

The next viable dissipative question is therefore not “can a passive nonunitary transfer match Gamma?” The answer is generically yes at the level of qualitative phase flexibility and is not informative. The meaningful question is:

> Does a Mathia-native finite--archimedean construction force a *strictly smaller* dissipative class carrying an independent positive form whose scalar boundary response is the Weil explicit-formula functional?

That formulation preserves the branch mandate. It demands that positivity come first from the geometry and that the arithmetic/Gamma decomposition emerge from the same object, rather than using dissipation as a flexible phase-fitting device.
