# ANF-016 — a cubic positive spectrum beats the thermodynamic Montgomery--Taylor lattice ratio

**Status:** `EXACT-DERIVED + EXPLICIT-PRIMAL-WITNESS + DUAL-SEPARATION + STRUCTURAL-BOUNDARY`. The thermodynamic lattice obstruction isolated in `ANF-013`--`ANF-015` does **not** by itself recover the Montgomery--Taylor ceiling. There is an explicit continuous real-even spectral profile `J>=0`, supported in `[-1,1]`, for which every long simple/duplicated lattice periodization remains at least its normalized floor while the BGSST pair cost is strictly below `C_MT`.

For `0<=x<=1`, define

\[
J_*(x)
=1-\frac38x-\frac74x^2+\frac98x^3
=(1-x)\left(1+\frac58x\left(1-\frac95x\right)\right),
\]

extend by evenness, and put `J_*(x)=0` for `|x|>1`. Then

\[
\boxed{p(J_*):=\inf_{h>0}\frac1h\sum_{k\in\mathbb Z}J_*(k/h)=1}
\]

but

\[
\boxed{C(J_*)=J_*(0)+2\int_0^1xJ_*(x)\,dx=\frac{53}{40}=1.325
<C_{\rm MT}=1.3274992963\ldots .}
\]

Thus the all-scale thermodynamic lattice survival test is genuinely weaker than Montgomery--Taylor. By weak duality, the multiplicative packing dual of `ANF-015` has optimum at most `53/40`, so it cannot reach `C_MT`. The next scalar obstruction must use finite-volume corrections, non-lattice real configurations, vertically displaced conjugate configurations, or another universal constraint not captured by the limiting periodization floor.

## 1. A one-parameter perturbation of the triangular spectrum

Start from the triangular profile

\[
J_0(x)=1-x,\qquad 0\le x\le1,
\]

and perturb it by

\[
\phi(x)=x(1-x)\left(1-\frac95x\right).
\]

Set

\[
J_\varepsilon(x)=J_0(x)+\varepsilon\phi(x)
=(1-x)\left(1+\varepsilon x\left(1-\frac95x\right)\right).
\tag{1}
\]

For `0<=epsilon<=5/8`, this is nonnegative on `[0,1]`: the concave quadratic `x(1-9x/5)` has minimum `-4/5` on the interval, so the second factor in (1) is at least `1-epsilon*4/5>=1/2`. Extend `J_epsilon` evenly and by zero outside `[-1,1]`.

The BGSST cost from `ANF-013` is elementary:

\[
\begin{aligned}
C(J_\varepsilon)
&=1+2\int_0^1xJ_\varepsilon(x)\,dx\\
&=\frac43-\frac{\varepsilon}{75}.
\end{aligned}
\tag{2}
\]

Hence increasing `epsilon` along this direction decreases the analytic cost.

## 2. Exact all-scale periodization at the endpoint

Write

\[
P_\varepsilon(h)
:=\frac1h\sum_{k\in\mathbb Z}J_\varepsilon(k/h).
\tag{3}
\]

For `0<h<1`, every nonzero sample lies outside the support, so

\[
P_\varepsilon(h)=\frac1h>1.
\tag{4}
\]

It remains to control `h>=1`. Write

\[
h=N+r,\qquad N=\lfloor h\rfloor\ge1,\qquad 0\le r<1.
\]

At `epsilon=0`, summing the linear profile gives

\[
\boxed{
P_0(h)-1=\frac{r(1-r)}{(N+r)^2}\ge0.
}
\tag{5}
\]

At the endpoint `epsilon=5/8`, direct summation of the cubic gives

\[
\boxed{
P_*(h)-1=\frac{Q_N(r)}{48(N+r)^4},
}
\tag{6}
\]

where

\[
\begin{aligned}
Q_N(r)={}&N^4+4N^3r-18N^2r^2+24N^2r-N^2\\
&-96Nr^3+126Nr^2-28Nr-48r^4+48r^3.
\end{aligned}
\tag{7}
\]

This polynomial is nonnegative for every integer `N>=1` and `0<=r<=1`.

For `N=1`,

\[
Q_1(r)=-12r^2(4r^2+4r-9)\ge0,
\tag{8}
\]

because `4r^2+4r-9<=-1` on `[0,1]`. For `N=2`,

\[
Q_2(r)=-12(4r^4+12r^3-15r^2-6r-1)>0.
\tag{9}
\]

Indeed `4r^4+12r^3<=16r^2`, so the parenthesis in (9) is at most `r^2-6r-1<0`.

Finally,

\[
\begin{aligned}
\frac{\partial Q_N(r)}{\partial N}
={}&4N^3+12N^2r-36Nr^2+48Nr-2N\\
&-96r^3+126r^2-28r.
\end{aligned}
\tag{10}
\]

For `N>=2` and `0<=r<=1`,

\[
Nr(48-36r)\ge24r,\qquad
12N^2r\ge48r,
\]

and `-96r^3+126r^2>=0`. Therefore

\[
\frac{\partial Q_N(r)}{\partial N}
\ge4N^3-2N+44r>0.
\tag{11}
\]

Thus the `N=2` case controls every `N>=2`, while (8) controls `N=1`. Equations (4)--(11) prove

\[
P_*(h)\ge1\qquad(h>0).
\tag{12}
\]

Since `P_*(1)=J_*(0)=1`, the floor is exact:

\[
\boxed{p(J_*)=1.}
\tag{13}
\]

Because `P_epsilon(h)` is affine in `epsilon`, (5) and (12) also show `P_epsilon(h)>=1` for the whole segment `0<=epsilon<=5/8`.

## 3. The endpoint is exact along this perturbation direction

The value `5/8` is not an arbitrary convenient cutoff. For `h=1+r`, the exact periodization has the expansion

\[
P_\varepsilon(1+r)-1
=
r\left(1-\frac85\varepsilon\right)
+r^2\left(\frac{42}{5}\varepsilon-3\right)
+O(r^3).
\tag{14}
\]

If `epsilon>5/8`, the linear coefficient is negative, so `P_epsilon(1+r)<1` for all sufficiently small positive `r`. Therefore

\[
\boxed{\varepsilon=\frac58}
\]

is the largest point in this perturbation family that can retain the normalized thermodynamic floor `p>=1`.

Substituting it in (2) gives

\[
\boxed{
C(J_*)=\frac43-\frac1{120}=\frac{53}{40}=1.325.
}
\tag{15}
\]

The Montgomery--Taylor cost is

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=1.3274992963\ldots ,
\tag{16}
\]

so the exact cubic witness lies below it by about `0.0024992963`.

## 4. The escape is genuinely spatial sign change

Let

\[
F_*(u)=\widehat J_*(u)
=\int_{-1}^{1}J_*(x)e^{-2\pi iux}\,dx.
\tag{17}
\]

For real nonzero `u`, direct integration gives

\[
F_*(u)=
\frac{
2\pi^2u^2(3-4\cos 2\pi u)
-26\pi u\sin 2\pi u
-27\cos 2\pi u+27
}{
32\pi^4u^4
}.
\tag{18}
\]

At the origin,

\[
F_*(0)=\int_{-1}^{1}J_*(x)\,dx=\frac{49}{48}.
\tag{19}
\]

At every nonzero integer,

\[
\boxed{
F_*(m)=-\frac1{16\pi^2m^2}<0.
}
\tag{20}
\]

Thus the witness uses exactly the residual freedom left by `ANF-012`: the spectral density remains nonnegative, but its spatial Fourier kernel changes sign. In particular, this is not a disguised member of the nonnegative-spatial Montgomery--Taylor class.

## 5. The `ANF-015` packing dual cannot reach Montgomery--Taylor

Normalize the primal lattice problem as in `ANF-015`, so `p(J)=1`. Every admissible multiplicative packing weight satisfies the weak-duality bound

\[
D(w)
=1+\int_1^\infty w(t)\left(1-\frac1t\right)\,dt
\le C(J)
\tag{21}
\]

for every normalized lattice-feasible `J`.

Applying (21) to the explicit `J_*` gives

\[
\boxed{
D(w)\le\frac{53}{40}<C_{\rm MT}
}
\tag{22}
\]

for **every** admissible packing-dual witness. No strong-duality theorem is needed. Consequently the program proposed at the end of `ANF-015` cannot close the scalar branch by optimizing the thermodynamic packing dual all the way to Montgomery--Taylor: a primal feasible point already separates the two values.

Equivalently, the long-lattice amplitude cap of `ANF-013` for this shape is

\[
2-\frac{C(J_*)}{p(J_*)}
=2-\frac{53}{40}
=\frac{27}{40}
=0.675,
\tag{23}
\]

which is above the Montgomery--Taylor benchmark `2-C_MT=0.6725007036...`. Equation (23) is only a **necessary-test cap**; it is not a proved zeta-zero proportion.

## 6. Falsification boundary

This finding resolves only the thermodynamic stage. It does **not** prove the universal affine inequality

\[
s(Z)\ge A|Z|-\sum_{z,w\in Z}F_*(z-w)
\tag{24}
\]

at `A=2`, or at any other intercept large enough to improve the zeta-zero bound. The periodization constraints arise after taking long equally spaced configurations. They discard finite-size boundary terms and say nothing by themselves about non-lattice real configurations or vertically displaced conjugate configurations.

This distinction is load-bearing. A finite arithmetic progression with `n` sites has normalized energy

\[
L_n(h)
=
F_*(0)+2\sum_{k=1}^{n-1}
\left(1-\frac{k}{n}\right)F_*(kh),
\tag{25}
\]

and the corresponding simple/duplicated tests constrain the intercept before the limit `n->infinity` replaces `L_n(h)` by `P_*(h)`. Those finite-volume inequalities are therefore the cheapest next falsification layer for the cubic survivor.

The result also does not contradict `ANF-015`: that finding proved only a strict improvement above the first Mellin dual witness, not that the optimized dual reaches `C_MT`. The explicit primal witness here supplies the missing upper separation.

## 7. Prior-art and novelty boundary

Polynomial summation, Fourier inversion, Fejér/Poisson periodization and weak duality are classical. The triangular spectrum is a standard positive-definite compact-band profile, and spatially signed Fourier transforms of nonnegative compactly supported spectra are not new in themselves.

A targeted search across the Montgomery--Taylor pair-correlation extremal problem, compactly supported positive spectra, lattice periodization constraints and low-degree polynomial perturbations did not locate this exact cubic witness or the conclusion (22) in the universal simple-critical-zero affine-certificate setting. No publication-level novelty claim is made. The durable contribution is the explicit **separation of stages**: thermodynamic lattice periodization is provably too weak to recover the Montgomery--Taylor ceiling, even inside the positive-spectral support-one class forced by `ANF-012`.

## 8. Decisive next test

The scalar frontier should now move from the infinite-lattice floor to the finite-volume universal configuration problem. The first exact target is to optimize the constraints obtained from (25), especially duplicated finite arithmetic progressions, over `n` and `h` for `J_*` and nearby positive-spectral perturbations.

If finite lattices alone force

\[
A-C(J_*)\le2-C_{\rm MT},
\]

then the cubic escape is killed without invoking complex configurations, and the resulting finite-size correction becomes the next scalar no-go mechanism. If it survives, the search should progress to non-lattice real configurations and then conjugation-invariant complex multisets. The configuration-level escape established in `ANF-006` remains outside all of these affine scalar obstructions.
