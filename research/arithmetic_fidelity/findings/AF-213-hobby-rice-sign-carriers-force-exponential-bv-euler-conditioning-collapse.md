# AF-213 — Hobby–Rice sign carriers force exponential BV Euler conditioning collapse

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-FIDELITY`, `SOURCE-COMPLEXITY-GATE`, `SEVERE-ILL-POSEDNESS`, `NO-NOVELTY-CLAIM`

## Claim

AF-209 proves that every finite bounded-variation complexity budget gives a positive lower recovery modulus for a positive-width Euler observation band. AF-211 shows that this modulus decays faster than every algebraic power as the permitted BV complexity grows, and AF-212 sharpens that to every stretched-exponential rate `exp(-c M^alpha)` with fixed `alpha<1` by modulating one compact Gevrey bump. AF-212 deliberately leaves the exponent-one endpoint open because no nonzero compactly supported real-analytic bump exists.

That endpoint is nevertheless reachable by changing the source construction. Keep the AF-209 parameters

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad 0<T<\infty,\qquad L>x,
\]

and write

\[
D_T(b)
:=
\sup_{|\tau|\le T}
\left|
\int_x^L \phi_\tau(t)b(t)\,dt
\right|,
\qquad
V_h(b):=\int_x^L h(t)|b(t)|\,dt,
\]

with the same anchored Euler kernels `phi_tau` and positive weight `h` as AF-209. Let

\[
\gamma(M)
:=
\inf\left\{
\frac{D_T(b)}{V_h(b)}:
0\ne b\in BV([x,L]),\
\operatorname{Var}(b)\le M V_h(b)
\right\}.
\]

Then there are constants `c,C,M_0>0`, depending only on the fixed Euler band parameters, such that

\[
\boxed{
0<\gamma(M)\le C e^{-cM}
\qquad(M\ge M_0).
}
\tag{1}
\]

The strict positivity for finite `M` is AF-209. The new statement is the exponential upper bound.

More generally, the mechanism does not depend on the detailed Euler formula. Any compact family of observation functions on a fixed interval that extends holomorphically and uniformly boundedly to one common complex neighborhood admits signed `BV` directions whose observation norm is exponentially small in their variation budget while a fixed positive weighted `L^1` norm stays constant.

Thus the AF-212 exponent-one gap is not an uncertainty barrier for the full signed BV source cone. It is a limitation of the **fixed-profile modulation construction**. Allowing the sign pattern itself to depend on the complexity budget gives exact cancellation of the first `n` polynomial moments at only `O(n)` variation cost; uniform analytic polynomial approximation then converts that algebraic annihilation into `O(rho^{-n})` invisibility for the whole Euler band.

## Derivation

### 1. Hobby–Rice produces low-variation signs annihilating all low polynomial moments

Fix an integer `n>=1`. Apply the Hobby–Rice theorem on `[x,L]` to the `n` real functions

\[
1,t,t^2,\ldots,t^{n-1}.
\]

There is a sign function

\[
\varepsilon_n:[x,L]\to\{-1,+1\}
\]

which is constant on the intervals of a partition with at most `n` interior sign changes and satisfies

\[
\boxed{
\int_x^L t^j\varepsilon_n(t)\,dt=0,
\qquad 0\le j\le n-1.
}
\tag{2}
\]

After merging adjacent equal-sign intervals if necessary, every interior jump has size `2`, hence

\[
\operatorname{Var}(\varepsilon_n)\le 2n.
\tag{3}
\]

Because `|\varepsilon_n|=1` almost everywhere, its weighted source size is independent of `n`:

\[
V_h(\varepsilon_n)
=
H,
\qquad
H:=\int_x^L h(t)\,dt>0.
\tag{4}
\]

The constant moment in `(2)` also gives

\[
\int_x^L\varepsilon_n(t)\,dt=0,
\tag{5}
\]

so these are zero-mass signed directions, as in the AF-211/AF-212 conditioning tests.

Normalize if desired by `b_n=\varepsilon_n/H`. Then

\[
V_h(b_n)=1,
\qquad
\operatorname{Var}(b_n)\le\frac{2n}{H}.
\tag{6}
\]

### 2. The entire fixed Euler band has one common analytic neighborhood in the source variable

For `s=\sigma+i\tau`, `|\tau|\le T`, recall

\[
g_{m,\tau}(t)
=s^m\sum_{k\ge1}k^{m-1}e^{-kst},
\qquad
\phi_\tau(t)=g_{m,\tau}(t)-g_{m,\tau}(x).
\]

The interval `[x,L]` lies strictly inside the positive real axis. Choose a sufficiently thin complex neighborhood `U` of `[x,L]` such that

\[
\operatorname{Re}(sz)\ge\kappa>0
\tag{7}
\]

for every `z\in U` and every `s=\sigma+i\tau` with `|\tau|\le T`. This is possible by compactness: on the real interval `\operatorname{Re}(st)=\sigma t\ge\sigma x`, and the perturbation caused by a sufficiently small complex displacement is uniform over the compact `tau`-band.

On `U`, the defining Euler series and all source-variable derivatives converge locally uniformly, because

\[
|s|^m\sum_{k\ge1}k^{m-1}e^{-k\operatorname{Re}(sz)}
\le
(\sigma^2+T^2)^{m/2}
\sum_{k\ge1}k^{m-1}e^{-k\kappa}<\infty.
\tag{8}
\]

Consequently the family

\[
\{\phi_\tau:|\tau|\le T\}
\]

extends holomorphically to one common neighborhood of `[x,L]` and is uniformly bounded there.

Map `[x,L]` affinely to `[-1,1]`. Since Bernstein ellipses shrink to `[-1,1]` as their parameter tends to `1`, there exists some fixed `\rho>1` whose closed ellipse maps inside `U`. Classical Bernstein/Chebyshev approximation for analytic functions therefore gives a constant `A<\infty` such that, for every `n>=1` and every `|\tau|\le T`, there is a complex polynomial `p_{n-1,\tau}` of degree at most `n-1` satisfying

\[
\boxed{
\|\phi_\tau-p_{n-1,\tau}\|_{L^\infty([x,L])}
\le A\rho^{-n}.
}
\tag{9}
\]

The same `A` and `rho` work uniformly over the whole observation band.

### 3. Polynomial annihilation converts analytic approximation into exponential invisibility

Equation `(2)` annihilates every real polynomial of degree at most `n-1`, and therefore every complex polynomial of that degree. Hence, for every `|\tau|\le T`,

\[
\int_x^L p_{n-1,\tau}(t)\varepsilon_n(t)\,dt=0.
\tag{10}
\]

Using `(9)`, `(10)`, and `|\varepsilon_n|=1`,

\[
\begin{aligned}
\left|
\int_x^L\phi_\tau(t)\varepsilon_n(t)\,dt
\right|
&=
\left|
\int_x^L
(\phi_\tau(t)-p_{n-1,\tau}(t))
\varepsilon_n(t)\,dt
\right|\\
&\le
(L-x)A\rho^{-n}.
\end{aligned}
\tag{11}
\]

Taking the supremum over the whole band gives

\[
D_T(\varepsilon_n)
\le
(L-x)A\rho^{-n}.
\tag{12}
\]

Together with `(4)`,

\[
\frac{D_T(\varepsilon_n)}{V_h(\varepsilon_n)}
\le
\frac{(L-x)A}{H}\rho^{-n}.
\tag{13}
\]

Thus a source direction that spends only `O(n)` BV complexity can be exponentially invisible to the entire positive-width Euler band.

### 4. Convert the moment order into the AF-209 BV budget

For sufficiently large `M`, choose

\[
n(M)=\left\lfloor\frac{HM}{2}\right\rfloor.
\tag{14}
\]

Then `(3)` and `(4)` imply

\[
\operatorname{Var}(\varepsilon_{n(M)})
\le 2n(M)
\le MH
=MV_h(\varepsilon_{n(M)}),
\tag{15}
\]

so this sign carrier is admissible in the definition of `\gamma(M)`. For large `M`,

\[
n(M)\ge\frac{HM}{2}-1.
\]

Equation `(13)` therefore yields

\[
\gamma(M)
\le
\frac{(L-x)A\rho}{H}
\exp\left(-\frac{H\log\rho}{2}M\right).
\tag{16}
\]

This proves `(1)` with, for example,

\[
c=\frac{H\log\rho}{2}>0.
\]

No optimization of the constants is intended.

## General analytic-observation form

The proof exposes a reusable compression principle. Let `w>0` almost everywhere on a compact interval `I`, let `Theta` be compact, and let

\[
\{f_\theta\}_{\theta\in\Theta}
\]

extend holomorphically and uniformly boundedly to one common complex neighborhood of `I`. Define

\[
D(b)=\sup_{\theta\in\Theta}
\left|\int_I f_\theta(t)b(t)dt\right|,
\qquad
V_w(b)=\int_Iw(t)|b(t)|dt.
\]

If `H_w=\int_Iw>0`, the same Hobby–Rice signs give

\[
V_w(\varepsilon_n)=H_w,
\qquad
\operatorname{Var}(\varepsilon_n)\le2n,
\qquad
D(\varepsilon_n)\le C\rho^{-n}.
\tag{17}
\]

Hence any coercivity constant defined on the exhaustion

\[
\operatorname{Var}(b)\le M V_w(b)
\]

has an exponential upper bound in `M`.

The source of the obstruction is therefore more structural than the Fourier-tail construction of AF-211/AF-212: **finite variation can buy linearly many exact polynomial annihilation constraints, while a uniformly analytic observation family is exponentially approximable by those same finite-dimensional polynomial spaces.**

## Exact controls and boundaries

### AF-209 remains correct at every finite budget

The sign functions do not create a nonzero kernel element. Their variation tends to infinity with `n`, so they leave every fixed AF-209 compactified source slice. Exact injectivity and fixed-budget coercivity remain untouched:

\[
\gamma(M)>0
\qquad\text{for every finite }M.
\]

AF-213 concerns only how the best positive constant degenerates as the source class expands.

### AF-212's uncertainty boundary applies to its construction, not to the BV infimum

AF-212 correctly notes that a fixed nonzero compactly supported real-analytic bump cannot exist and that Paley–Wiener/Ingham uncertainty blocks the naive attempt to obtain an exponential Fourier tail from one fixed compact profile. The Hobby–Rice construction does something different: the source itself changes combinatorially with `n`, and its first `n` polynomial moments vanish exactly.

Thus there is no conflict with the AF-212 uncertainty discussion. The new result resolves the precise possibility AF-212 left open: a **different admissible BV construction** does give an exponential upper bound for the same `gamma(M)`.

### No exponential lower bound or sharp exponent is proved

Equation `(1)` is an upper bound on the optimal coercivity constant. It does not show

\[
\gamma(M)\asymp e^{-cM},
\]

nor does it rule out super-exponential deterioration from another source family. Establishing a matching lower scale would require a quantitative inverse theorem for the analytic Euler transform under a BV budget, not merely analyticity of the forward kernels.

### The obstruction remains signed

The Hobby–Rice carriers take both signs. They do not establish the same exponential collapse for the positive Peano cone of AF-206, for probability measures, for mass-one source-realizable Peano carriers, or for a rational-prime/generalized-prime control class. Positivity can destroy exactly the cancellation resource exploited here.

### The full interval is used only through a common analytic neighborhood

The proof is not tied to a particular polynomial basis or to Chebyshev projection. Any degree-`n` approximation theorem with geometric error on the common analytic neighborhood gives the same conclusion. Conversely, if the observation family is only finitely smooth, Gevrey, or loses a common complex neighborhood as the parameter range changes, the decay law must be recomputed from the corresponding approximation widths.

### No RH consequence follows

The result identifies a severe conditioning obstruction for an unrestricted signed source class. It does not show that the actual rational-prime discriminator occupies these sign-changing moment-null directions. An arithmetic application still needs a source-side theorem describing which cancellation patterns, variation scales, positivity constraints, or complexity budgets are intrinsically available to the prime-derived object.

## Prior art and novelty assessment

Both ingredients of the proof are classical, and no novelty is claimed for either the moment-annihilating signs or geometric polynomial approximation of analytic functions.

- C. R. Hobby and J. R. Rice, **“A moment problem in L1 approximation,”** *Proceedings of the American Mathematical Society* 16(4) (1965), 665–670, DOI `10.2307/2033900`, prove the sign-partition theorem used in `(2)`: `n` integrable real functions can be simultaneously annihilated by an alternating sign function with at most `n` cuts.
- Allan Pinkus, **“A simple proof of the Hobby-Rice theorem,”** *Proceedings of the American Mathematical Society* 60 (1976), 82–84, DOI `10.2307/2041117`, gives the standard concise form for finite nonatomic measures and makes the bounded-cut structure explicit.
- Lloyd N. Trefethen, ***Approximation Theory and Approximation Practice, Extended Edition***, SIAM (2019), Chapter 8, DOI `10.1137/1.9781611975949.ch8`, gives standard Bernstein-ellipse bounds: a function uniformly bounded and analytic on a Bernstein ellipse has polynomial/Chebyshev approximation error decaying geometrically in the degree.
- Darko Volkov, **“Optimal decay rates in Sobolev norms for singular values of integral operators,”** *Journal of Mathematical Analysis and Applications* 537(2) (2024), 128403, DOI `10.1016/j.jmaa.2024.128403`, places rapid and analytic-kernel singular-value decay in the modern inverse-problem literature and reinforces that analytic smoothing can entail severe inverse conditioning.

The literature audit found the two proof ingredients and the broader analytic-kernel ill-posedness mechanism as established theory. It did not justify a novelty claim for their combination, and none is made. The durable Arithmetic Fidelity result is the exact specialization to the AF-209 modulus: **the previously open exponent-one endpoint is attainable on the same unrestricted signed BV cone, by a source family whose complexity is the number of exact polynomial moments it can annihilate.**

## Consequence for the Arithmetic Fidelity frontier

AF-209 through AF-213 now separate four logically distinct gates for this Euler compression:

\[
\text{exact injectivity}
\quad\not\Rightarrow\quad
\text{fixed-class coercivity without compactification}
\quad\not\Rightarrow\quad
\text{complexity-uniform conditioning}
\quad\not\Rightarrow\quad
\text{arithmetic usefulness}.
\]

A fixed finite BV budget restores stability, but along the natural BV exhaustion the best stability constant is at most exponentially small. Therefore a future arithmetic use cannot justify stable discriminator survival merely by placing the source in `BV` or by proving finite variation. It needs a **source-forced complexity law or sign/positivity restriction** strong enough to exclude these linearly growing moment-annihilating sign patterns, together with a conditioning estimate at the actual arithmetic scale.

This closes AF-212's exponent-one endpoint as an open upper-bound question. The remaining quantitative problem is no longer whether exponential deterioration can occur, but whether the arithmetic source category supplies enough positivity, combinatorial rigidity, localization, or complexity control to avoid it, and whether any sharper lower conditioning law survives on that intrinsically admissible class.