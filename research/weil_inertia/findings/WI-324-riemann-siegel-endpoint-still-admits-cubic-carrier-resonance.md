# WI-324 — Riemann--Siegel endpoint still admits cubic carrier resonance

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`.

WI-322 strengthens the source-compatible bow normalization to

\[
\rho_T:=\frac{U}{X_*^2}\ge 2\pi(1-o(1)),
\]

and WI-323 then shows that the direct logarithmic dual has length at least the source length. A remaining tempting escape is to hope that this sharper Riemann--Siegel normalization also forces the bare logarithmic carrier `n^{iU}` away from short coherent resonances, so that ordinary oscillatory estimates could de-exceptionalize the distinguished bow twist.

That implication is false at the level of the exact scale information carried by WI-322--WI-323. There is an explicit cofinal family with

\[
\frac{U_M}{X_M^2}
=2\pi\left(1+\frac1{2M}\right)
\longrightarrow 2\pi
\]

from the allowed side, whose direct dual is only one half-lattice step longer than the source, yet for which the first two lattice Taylor jets of the carrier cancel modulo integers and a block of length `\asymp M^{1/3}` remains coherent. Thus even asymptotic saturation of the exact Riemann--Siegel lower endpoint does not by itself supply carrier cancellation.

This is an information barrier, not a zeta counterexample. The family satisfies the reciprocal-length and zero-count scale constraints used in WI-322, but it is not asserted to be realized by an actual zeta bow. It therefore does not prove that the distinguished von-Mangoldt covariance is large or small. It closes only the strategy that tries to deduce nonresonance from the sharpened ratio `rho_T\ge2\pi(1-o(1))` plus smooth logarithmic phase geometry, without using the arithmetic location of the distinguished height or the prime coefficients.

## 1. A cofinal family at the exact lower endpoint

Let `M` be a positive integer and put

\[
A_M:=M\left(M+\frac12\right),
\qquad
U_M:=2\pi A_M,
\qquad
X_M:=M.
\tag{1}
\]

Then

\[
\boxed{
\frac{U_M}{X_M^2}
=2\pi\left(1+\frac1{2M}\right)
=2\pi+\frac{\pi}{M}.
}
\tag{2}
\]

Thus this family approaches the WI-322 endpoint `2\pi` from above at the much stronger additive rate `O(M^{-1})`.

In the notation of WI-323, the logarithmic phase parameter is `A=U/(2\pi)`. The direct reciprocal dual length at the central source scale is therefore

\[
\boxed{
Y_M:=\frac{A_M}{X_M}=M+\frac12.
}
\tag{3}
\]

Hence

\[
\frac{Y_M}{X_M}=1+\frac1{2M}\to1.
\tag{4}
\]

The family asymptotically saturates not only the WI-322 lower endpoint but also the noncontraction inequality of WI-323: the direct dual is longer by only one half lattice unit.

The same parameters can be made exactly compatible with the reciprocal-length definition used in WI-322. Set `T_M:=U_M` and

\[
c_M:=\frac{2\pi\log T_M}{\log M}.
\tag{5}
\]

Then, with `\alpha_M=2\pi/c_M`,

\[
T_M^{\alpha_M}=M=X_M
\tag{6}
\]

exactly, while

\[
c_M=4\pi+\frac{2\pi\log(2\pi)}{\log M}+o\!\left(\frac1{\log M}\right),
\tag{7}
\]

so `c_M` is bounded and tends to the count-saturating spacing `4\pi` from above. Moreover, writing `L_M=\log T_M` and `L_{0,M}=\log(T_M/(2\pi))=\log A_M`,

\[
\frac{c_M}{4\pi L_M/L_{0,M}}
=\frac{L_{0,M}}{2\log M}
=1+\frac{\log(1+1/(2M))}{2\log M}>1.
\tag{8}
\]

So the family satisfies even the unweakened leading zero-count threshold behind WI-322, and therefore also its stated asymptotic lower inequality. This establishes the intended information boundary: the exact count/reciprocal constraints themselves do not exclude the family.

## 2. Parity aliases the linear and quadratic jets

Use the standard notation `e(z)=\exp(2\pi i z)`. Consider the normalized bare carrier on the integer block beginning at `M`,

\[
C_M(j)
:=e\!\left(A_M\log\frac{M+j}{M}\right),
\qquad j\ge0.
\tag{9}
\]

For `0\le x\le1`, the alternating logarithm expansion gives

\[
\log(1+x)=x-\frac{x^2}{2}+R_3(x),
\qquad
0\le R_3(x)\le\frac{x^3}{3}.
\tag{10}
\]

Substituting `x=j/M` and `A_M=M(M+1/2)` yields

\[
\begin{aligned}
A_M\log\left(1+\frac jM\right)
&=\left(M+\frac12\right)j
-\left(\frac12+\frac1{4M}\right)j^2
+A_MR_3(j/M)\\
&=Mj-\frac{j(j-1)}2
+\theta_{M,j},
\end{aligned}
\tag{11}
\]

where

\[
\boxed{
\theta_{M,j}
=-\frac{j^2}{4M}+A_MR_3(j/M).
}
\tag{12}
\]

The first two terms in the last line of (11) are integers for every integer `j`. Thus the large linear phase and the half-integral quadratic phase do not merely become small: they **alias exactly on the integer lattice**. The visible phase is only the residual (12).

From (10), for `0\le j\le M`,

\[
|\theta_{M,j}|
\le
\frac{j^2}{4M}
+\left(1+\frac1{2M}\right)\frac{j^3}{3M}.
\tag{13}
\]

This is the precise source of the cubic coherence scale.

## 3. An explicit `M^(1/3)` coherent block

Take

\[
L_M:=\left\lfloor\frac14M^{1/3}\right\rfloor.
\tag{14}
\]

For `0\le j<L_M`, equation (13) gives, once `M\ge1`,

\[
|\theta_{M,j}|
\le
\frac{1}{64M^{1/3}}+\frac1{128}
\le\frac3{128}
<\frac16.
\tag{15}
\]

Therefore every rotated summand `e(\theta_{M,j})` lies in the open sector of angular width less than `\pi/3` around the positive real axis. In particular,

\[
\Re e(\theta_{M,j})>\frac12,
\]

and hence, whenever `L_M\ge1`,

\[
\boxed{
\left|
\sum_{j=0}^{L_M-1}
C_M(j)
\right|
\ge \frac{L_M}{2}
\asymp M^{1/3}.
}
\tag{16}
\]

So the carrier has a genuinely coherent cubic-scale block along a family for which `rho_T` approaches the exact WI-322 endpoint and the WI-323 direct dual approaches exact self-duality.

The sign of the twist is immaterial for this obstruction: replacing `n^{iU_M}` by `n^{-iU_M}` conjugates the sum and leaves (16) unchanged.

## 4. What this closes and what it does not

Equations (2)--(16) rule out the implication

\[
\boxed{
\rho_T\ge2\pi(1-o(1))
\; + \;
X_*\le\sqrt{U/(2\pi)}(1+o(1))
\; + \;
\text{smooth logarithmic carrier}
\Longrightarrow
\text{uniform short-block carrier cancellation}.
}
\tag{17}
\]

The failure occurs arbitrarily close to the exact Riemann--Siegel boundary, not only at a coarse `U\asymp X^2` scale. The extra normalization recovered in WI-322 therefore cannot be reused as a generic Diophantine nonresonance hypothesis. WI-323's noncontracting direct duality and the present parity alias are compatible: at (1) the dual scale is `M+1/2`, while the source lattice itself aliases the first two Taylor jets.

This finding does **not** resolve `CLUE-bow-distinguished-twist-offdiagonal-cancellation`. In particular:

- it does not assert that an actual zeta bow chooses the heights (1);
- it does not control `\Lambda(n)`, `\Lambda^\sharp(n)`, or their signed covariance;
- it does not produce the macroscopic negative off-diagonal cancellation required for a bow dip;
- and it does not show that the true distinguished height is resonant.

Its durable consequence is negative but sharp: any de-exceptionalization theorem at the current bow frontier must consume information absent from the scalar ratio `U/X_*^2` and the bare logarithmic phase geometry. That information could be a quantitative Diophantine statement about the actual distinguished height, signed cancellation in the von-Mangoldt coefficients, a norm-matched dispersion estimate, or another source-fixed observable. Merely pinning the reciprocal source to the Riemann--Siegel side does not supply it.

## 5. Prior-art and novelty audit

The surrounding exponential-sum phenomenon is classical. Van der Corput theory treats sums `\sum e(f(n))` through derivatives and lattice resonances; Huxley and Kolesnik, *Exponential Sums and the Riemann Zeta Function III*, Proc. London Math. Soc. 62 (1991), 449--468, specifically study the difficult regime where the Dirichlet length is close to the square root of the height. Ghaith Hiary, *Fast methods to compute the Riemann zeta function*, Ann. of Math. 174 (2011), 891--946, develops algorithms for quadratic and cubic exponential sums arising from Taylor reduction of Riemann-zeta Dirichlet sums, including cubic sums with a small cubic coefficient.

Those sources are prior art for the general use of Taylor-polynomial exponential sums at Riemann--Siegel scale; they are not load-bearing for (1)--(16), which are elementary exact algebra plus the alternating-series remainder. A bounded external audit did not locate a theorem surface asserting the specific line-local statement needed here: a count-compatible family approaching `U/X^2=2\pi` from above whose integer-lattice linear/quadratic jets alias and leave an `M^{1/3}` coherent block. No priority claim is made from that negative search.

The internal novelty audit checked the current WI-322--WI-323 frontier and the accepted distinguished-twist clue. WI-322 fixes the one-sided ratio and alias density; WI-323 proves direct-dual noncontraction and exact normalized self-duality. Neither supplies an explicit near-endpoint lattice carrier resonance or proves that the Riemann--Siegel normalization itself fails to de-exceptionalize the distinguished twist. The present result is therefore a new route-closing refinement rather than a restatement of either finding.
