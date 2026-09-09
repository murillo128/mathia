# XF-149 — root-scale derivative sensors trade missing jet depth for antipodal reach

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/DISTRIBUTIONAL-REAL-SENSOR-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-OBSERVATION` + `FULL-FUTURE` + `DERIVATIVE-DEPTH/ANTIPODAL-REACH-TRADEOFF`. XF-148 proves that polynomially normalized finite-measure sensors remain exponentially transition-blind unless their support reaches the antipodal visibility layer, but deliberately excludes derivative evaluations and other distributional functionals. For the same maximal-contact pair, root-spacing-normalized spatial derivatives admit an all-future envelope with a simple effective-degree law: each derivative can consume at most one power of the packet's spatial suppression. Thus derivative sensing does not remove the aperture obstruction unless the derivative depth itself approaches the full polynomial degree, or the support approaches the antipode according to a joint depth/reach tradeoff.

## Claim

Use the maximal-contact matched pair of XF-141--XF-148,

\[
R_1(x,s),\qquad R_{\lambda_\rho}(x,s),
\tag{1}
\]

with even degree `N>=4`,

\[
n:=N-2,
\tag{2}
\]

fixed `rho>0`, and

\[
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_\rho})=-\rho.
\tag{3}
\]

Normalize spatial differentiation at the Fourier/root-spacing scale by

\[
\boxed{
\mathscr D_N
:=\frac{L}{2\pi N}\,\partial_x.
}
\tag{4}
\]

For every integer `0<=j<=n`, every real `x`, and every future heat time `s>=0`,

\[
\boxed{
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4e^{-(N-1)as}
B(x)^{\,n-j},
}
\tag{5}
\]

where

\[
B(x)
:=
\max\!\left\{
\frac12,
\left|\sin\frac{\pi x}{L}\right|
\right\}
\le1.
\tag{6}
\]

Thus a normalized derivative of order `j` can remove at most `j` powers from the exact spatial blindness exponent. In particular, any derivative depth `j=o(N)` preserves the same exponential rate as the raw trace on every fixed proper aperture.

More generally, let

\[
\Omega_N\subset\mathbb T_L\times[0,\infty)
\tag{7}
\]

be any nonempty predetermined observation set and define, as in XF-148,

\[
d_N:=
\inf_{(x,s)\in\Omega_N}
\operatorname{dist}_{\mathbb T_L}(x,x_{\rm anti}),
\qquad
x_{\rm anti}=L/2\pmod L,
\tag{8}
\]

and

\[
B_N:=
\max\!\left\{
\frac12,
\cos\frac{\pi d_N}{L}
\right\}.
\tag{9}
\]

Then for every `0<=J_N<=n`,

\[
\boxed{
\max_{0\le j\le J_N}
\sup_{(x,s)\in\Omega_N}
\left|
\mathscr D_N^j
(R_1-R_{\lambda_\rho})(x,s)
\right|
\le
4B_N^{\,n-J_N}.
}
\tag{10}
\]

This extends to polynomially normalized finite-order distributional sensing. Let `mu_{k,N}`, `1<=k<=m_N`, be finite complex Borel measures supported on `Omega_N`, choose derivative orders

\[
0\le j_{k,N}\le J_N,
\tag{11}
\]

and define

\[
\mathcal O_N(R)
:=
\left(
\int_{\Omega_N}
\mathscr D_N^{j_{k,N}}R\,d\mu_{k,N}
\right)_{k=1}^{m_N}.
\tag{12}
\]

If

\[
W_N:=\max_k\|\mu_{k,N}\|_{\rm TV},
\tag{13}
\]

then

\[
\boxed{
\|\mathcal O_N(R_1)-\mathcal O_N(R_{\lambda_\rho})\|_{\ell^2}
\le
4\sqrt{m_N}\,W_N B_N^{\,n-J_N}.
}
\tag{14}
\]

Equivalently, `(12)` covers distributions obtained by applying up to `J_N` normalized spatial derivatives to finite measures, after the usual integration-by-parts identification on the real circle.

Every decoder that recovers `Lambda_per` on both matched controls and is Lipschitz in this observation norm therefore has condition number `K_N` satisfying

\[
\boxed{
K_N
\ge
\frac{\rho}
{4\sqrt{m_N}\,W_N B_N^{\,n-J_N}}.
}
\tag{15}
\]

If `m_N` and `W_N` grow at most polynomially, this gives two useful phase boundaries.

First, if the observation geometry stays a fixed relative distance from the antipode,

\[
\frac{d_N}{L}\ge\delta>0,
\tag{16}
\]

put

\[
\kappa_\delta
:=
-\log\max\!\left\{
\frac12,
\cos(\pi\delta)
\right\}>0.
\tag{17}
\]

Then

\[
\boxed{
\log K_N
\ge
\kappa_\delta\,(N-2-J_N)-O(\log N).
}
\tag{18}
\]

Hence every fixed fractional derivative depth

\[
J_N\le(1-\eta)N
\qquad(\eta>0)
\tag{19}
\]

still leaves exponential transition conditioning. If `J_N=o(N)`, the exponential rate is the same as in XF-148. To make this matched family stop forcing even superpolynomial conditioning on a fixed proper aperture, one must at least enter the near-full-degree regime

\[
\boxed{
N-J_N=O(\log N).
}
\tag{20}
\]

Second, if the support itself approaches the antipode and `d_N/L->0`, then

\[
\boxed{
\log K_N
\ge
\left(\frac{\pi^2}{2}+o(1)\right)
\frac{(N-2-J_N)d_N^2}{L^2}
-O(\log N).
}
\tag{21}
\]

Therefore

\[
\boxed{
\frac{(N-J_N)d_N^2}{L^2\log N}
\longrightarrow\infty
}
\tag{22}
\]

forces superpolynomial transition conditioning. The XF-148 visibility layer is exactly the `J_N=0` instance of this formula. With derivatives available, the present adversary only ceases to certify superpolynomial blindness when

\[
\boxed{
d_N
=O\!\left(
L\sqrt{\frac{\log N}{N-J_N}}
\right)
}
\tag{23}
\]

or when the residual derivative deficit `N-J_N` itself has fallen to logarithmic size.

Equations `(20)` and `(23)` are **necessary escape conditions for this certificate, not sufficiency statements**. The bound becomes deliberately nonsharp when `J_N` is extremely close to `N`; the actual matched pair may remain much more poorly conditioned there.

## 1. Differentiate the exact Gaussian packet before taking absolute values

XF-145--XF-148 use the exact maximal-contact representation

\[
t_*\Delta Q(y,s)
=-2\sigma\,
 e^{Ny/2-M^2u}
\mathbb E\,
\sinh^n\!\left(
\frac y2+qZ
\right),
\tag{24}
\]

where

\[
N=2M,
\qquad
n=N-2=2(M-1),
\qquad
u:=as,
\qquad
q:=\sqrt{u/2},
\tag{25}
\]

`Z` is standard Gaussian and `|sigma|=1`. On the physical real circle,

\[
y=-\frac{2\pi i x}{L}.
\tag{26}
\]

Since

\[
\mathscr D_N
=-\frac{i}{N}\partial_y
\tag{27}
\]

on this parametrization, only the modulus of `N^{-j}\partial_y^j` matters.

Fix the Gaussian variable and write

\[
t=qZ\in\mathbb R,
\qquad
z=t+y/2,
\qquad
A:=|\sinh z|.
\tag{28}
\]

The key derivative estimate is elementary. Regard `sinh^n z` as a product of `n` identical factors. After `ell` differentiations, every term in the iterated product rule is a product of `sinh z` and `cosh z`, and at least `n-ell` factors were never differentiated. There are at most `n^ell` ordered differentiation histories. Therefore, for `0<=ell<=n`,

\[
|\partial_z^\ell\sinh^n z|
\le
n^\ell A^{n-\ell}C^\ell,
\tag{29}
\]

where

\[
C:=\max\{|\sinh z|,|\cosh z|\}.
\tag{30}
\]

For `y` purely imaginary,

\[
|\sinh(t+i\theta)|^2
=\sinh^2t+\sin^2\theta,
\tag{31}
\]

\[
|\cosh(t+i\theta)|^2
=\sinh^2t+\cos^2\theta,
\tag{32}
\]

so

\[
A\le C\le\cosh|t|\le e^{|t|}.
\tag{33}
\]

Now differentiate the complete integrand

\[
g(y):=e^{Ny/2}\sinh^n(t+y/2).
\tag{34}
\]

Leibniz gives

\[
N^{-j}\partial_y^j g
=
2^{-j}e^{Ny/2}
\sum_{\ell=0}^j
\binom j\ell
N^{-\ell}
\partial_z^\ell\sinh^n z.
\tag{35}
\]

Because `n/N<1`, equations `(29)`--`(33)` imply

\[
\begin{aligned}
\left|N^{-j}\partial_y^j g\right|
&\le
2^{-j}
\sum_{\ell=0}^j
\binom j\ell
A^{n-\ell}e^{\ell|t|}\\
&=
2^{-j}A^{n-j}(A+e^{|t|})^j\\
&\le
A^{n-j}e^{j|t|}.
\end{aligned}
\tag{36}
\]

This is the structural reason for the effective degree `n-j`: every normalized spatial derivative can replace at most one of the `n` small `sinh` factors by a nonsmall `cosh` factor.

## 2. The XF-147 aperture envelope survives with degree `n-j`

Set

\[
b:=\left|\sin\frac{\pi x}{L}\right|.
\tag{37}
\]

The elementary XF-147 inequality says, for every real `t`,

\[
A
=
\sqrt{\sinh^2t+b^2}
\le
\frac12e^{|t|}
\max\{1,2b\}.
\tag{38}
\]

Combining `(36)` and `(38)` gives

\[
\left|N^{-j}\partial_y^j g\right|
\le
2^{-(n-j)}
\max\{1,2b\}^{n-j}
e^{n|t|}.
\tag{39}
\]

Taking the Gaussian expectation in `(24)` and using the same elementary estimate as XF-146--XF-147,

\[
\mathbb E e^{nq|Z|}
\le
2e^{n^2u/4},
\tag{40}
\]

we obtain

\[
\left|
\mathscr D_N^j(t_*\Delta Q)(x,s)
\right|
\le
4
\left(
\max\left\{\frac12,b\right\}
\right)^{n-j}
 e^{-(M^2-n^2/4)u}.
\tag{41}
\]

For maximal contact,

\[
M^2-\frac{n^2}{4}=N-1,
\tag{42}
\]

which proves

\[
\left|
\mathscr D_N^j(t_*\Delta Q)(x,s)
\right|
\le
4e^{-(N-1)as}B(x)^{n-j}.
\tag{43}
\]

Finally,

\[
R_1-R_{\lambda_\rho}
=(1-\lambda_\rho)t_*\Delta Q,
\qquad
0<1-\lambda_\rho<1,
\tag{44}
\]

so `(43)` proves `(5)`.

The heat factor in `(43)` is dissipative for every derivative order in the theorem. Thus waiting arbitrarily long does not create a derivative-sensor escape from this envelope; the only changes are spatial reach and derivative depth.

## 3. Arbitrary derivative-measure geometry reduces to one depth and one distance

For every real `x`,

\[
\left|\sin\frac{\pi x}{L}\right|
=
\cos\!\left(
\frac{\pi}{L}
\operatorname{dist}_{\mathbb T_L}(x,x_{\rm anti})
\right).
\tag{45}
\]

Hence `B(x)<=B_N` throughout `Omega_N`. Since `B_N<=1`, for every `j<=J_N`,

\[
B_N^{n-j}\le B_N^{n-J_N}.
\tag{46}
\]

Dropping the dissipative heat factor proves `(10)`.

For each sensor in `(12)`, total variation then gives

\[
\left|
\int_{\Omega_N}
\mathscr D_N^{j_{k,N}}
(R_1-R_{\lambda_\rho})\,d\mu_{k,N}
\right|
\le
4W_NB_N^{n-J_N}.
\tag{47}
\]

Taking the `ell^2` norm proves `(14)`, and the fixed transition separation `rho` proves `(15)`.

This is a genuine extension of XF-148's observation class. Point evaluations of derivatives are obtained by Dirac measures, finite weighted derivative samples by atomic measures, and normalized finite-order distributional sensors of the form `partial_x^j mu` are the dual version of the same estimate. No positive-measure or connected-support assumption appears.

## 4. Depth/reach phase law and stress tests

Assume `m_N` and `W_N` are polynomial. Their contribution to `log K_N` is `O(log N)`. If `d_N/L>=delta`, then `B_N<=exp(-kappa_delta)`, and `(18)` follows immediately. Therefore a derivative bank whose maximum normalized order is any fixed fraction below the degree remains exponentially blind. In particular,

\[
J_N=o(N)
\tag{48}
\]

changes the exponent only by `o(N)` and does not improve the XF-148 exponential rate.

When `d_N/L->0`, eventually `B_N=cos(pi d_N/L)`, and

\[
-\log B_N
=
\frac{\pi^2}{2}\frac{d_N^2}{L^2}
+O\!\left(\frac{d_N^4}{L^4}\right).
\tag{49}
\]

Substitution into `(15)` gives `(21)`--`(23)`.

Several boundary checks are useful.

At `J_N=0`, equations `(10)`, `(15)`, and `(21)` reduce exactly to the XF-148 finite-measure bound and its `L sqrt(log N/N)` visibility layer. Thus the new theorem is a strict extension rather than a competing normalization.

At fixed proper aperture and `J_N=(1-eta)N+O(1)`, `(18)` still gives an exponential condition number with exponent at least `eta kappa_delta N+O(1)`. So even a linearly deep derivative bank is not enough unless its depth approaches the full degree.

At `J_N=n`, the bound becomes only `O(1)` and intentionally says nothing about conditioning. This loss is not evidence of stable recovery. For example, at the initial center the exact packet has an `n`-fold zero, and its root-normalized `n`-th derivative still contains the factorial ratio `n!/(2N)^n`, which is exponentially small by Stirling. Thus the envelope `(5)` is designed as a robust all-geometry upper bound, not as a sharp high-jet asymptotic.

The normalization `(4)` is essential to a meaningful conditioning statement. Bernstein's classical inequality for degree-`N` trigonometric polynomials scales one derivative by a factor of order `N`; multiplying an observed derivative by an exponentially large external weight would merely hide the inverse instability inside the sensor. Root-spacing normalization removes that trivial degree gain before the observation norm is assessed.

## 5. Prior-art boundary and research implication

Bernstein and Markov derivative inequalities are the classical neighboring framework for controlling derivatives of polynomial and trigonometric-polynomial data. Modern surveys include H. Queffélec and R. Zarouf, *On Bernstein's inequality for polynomials*, Analysis and Mathematical Physics 9 (2019), 1181--1207, DOI `10.1007/s13324-019-00294-x`, and S. Kalmykov, B. Nagy and V. Totik, *Bernstein- and Markov-type inequalities*, Surveys in Approximation Theory 9 (2021), 1--17. Higher-order local derivative inequalities on compact arcs are likewise classical approximation theory. Those results justify the normalization context but are not load-bearing here.

The present estimate is packet-specific and stronger in a different direction: instead of bounding derivatives by a global polynomial norm, `(36)` keeps track of the number of undifferentiated `sinh` factors, and `(43)` couples that residual contact order to the exact all-future antipodal envelope. The proof is self-contained once the canonical XF-145 Gaussian representation and XF-147 scalar inequality are imported. No external theorem is used to prove `(5)`--`(23)`, so this finding creates no new `SOURCES.md` dependency.

XF-140 already shows that even a full degree-order **complex exterior logarithmic jet** can remain transition-blind at a fixed macroscopic height. XF-149 addresses the orthogonal boundary left explicit by XF-148: **real-axis derivative/distributional sensors on arbitrary nonlocal supports through the complete future**. The resulting phase law says that spatial reach and derivative depth are interchangeable only through the residual degree `N-J_N` in this certificate.

This still does not construct a source-faithful Xi observable. It narrows what such an observable must accomplish. A target-side route that remains away from the antipodal visibility layer cannot be rescued by a modest derivative bank: for fixed proper reach, the maximal-contact pair survives every normalized jet that leaves more than logarithmically many degrees unresolved. Conversely, if an Xi-derived observable genuinely provides near-full-degree distributional information, that is a materially different source interface and must carry its own normalization/stability proof.

The other live escape remains source-side: prove that the actual Xi heat flow excludes the maximal-contact direction or any transition-sharp family with the same high-contact geometry.

## Scope and falsification

The theorem concerns the raw real periodic heat trace and predetermined observation geometry. It does not cover data-adaptive policies whose future support depends discontinuously on the observed input, exponentially normalized distributions, or nonlinear sensors without a controlled Lipschitz modulus. It also does not assert that the actual Xi source realizes the matched pair.

A direct falsifier is any `0<=j<=N-2`, real `x`, and `s>=0` for which `(5)` fails. The only substantive inequalities in the derivation are the iterated-product bound `(29)`, the elementary real-axis identities `(31)`--`(33)`, and the already established XF-147 envelope `(38)`. At low order `(29)` is immediate from the ordinary product rule; at the extreme `j=n`, it deliberately overcounts repeated differentiation histories and therefore remains an upper bound rather than a sharp formula.

A stronger continuation could optimize the occupancy combinatorics in `(29)` and determine the true high-derivative phase boundary. Such a refinement would matter only near `J_N=N-O(log N)`, where the present certificate intentionally stops deciding polynomial versus superpolynomial conditioning.