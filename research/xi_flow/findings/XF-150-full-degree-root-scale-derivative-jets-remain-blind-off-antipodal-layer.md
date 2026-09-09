# XF-150 — full-degree root-scale derivative jets remain blind off the antipodal layer

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/DISTRIBUTIONAL-REAL-SENSOR-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-OBSERVATION` + `FULL-FUTURE` + `FULL-DEGREE-JET` + `BINOMIAL-FREQUENCY-MOMENT`. XF-149 proves that root-spacing-normalized derivatives of order `J_N` preserve the antipodal aperture obstruction whenever a macroscopic residual degree `N-J_N` remains, but deliberately leaves the near-full-degree regime unresolved because its product-rule envelope becomes `O(1)` at `J_N=N-2`. For the same maximal-contact matched pair, the exact heat/Fourier expansion supplies a second envelope: high normalized derivative orders are exponentially small because the packet's Fourier frequencies themselves have a binomial profile concentrated away from the top frequency. Combining the low-derivative spatial-contact envelope with this high-derivative frequency-moment envelope closes the gap. Even the complete normalized real spatial jet through degree `N-2`, observed through the entire future, remains exponentially transition-blind on every fixed proper aperture and superpolynomially blind until the support enters the same `L sqrt(log N/N)` antipodal layer already forced for the raw trace.

## Claim

Use the maximal-contact matched pair of XF-141--XF-149,

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

Keep the XF-149 root-spacing normalization

\[
\mathscr D_N
:=\frac{L}{2\pi N}\,\partial_x.
\tag{4}
\]

For `0<=j<=n`, define the binomial frequency moment

\[
\boxed{
A_{N,j}
:=
2^{-n}
\sum_{k=0}^{n}
\binom nk
\left(\frac{N-1-k}{N}\right)^j.
}
\tag{5}
\]

Equivalently, if `K_N~Bin(n,1/2)`,

\[
A_{N,j}
=
\mathbb E
\left(1-\frac{K_N+1}{N}\right)^j.
\tag{6}
\]

Then for every real `x`, every future heat time `s>=0`, and every `0<=j<=n`,

\[
\boxed{
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
2e^{-(N-1)as}A_{N,j}.
}
\tag{7}
\]

Combining `(7)` with XF-149's spatial-contact estimate gives the sharper two-sided certificate

\[
\boxed{
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4e^{-(N-1)as}
\min\!\left\{
B(x)^{n-j},
A_{N,j}
\right\},
}
\tag{8}
\]

where

\[
B(x)
:=
\max\!\left\{
\frac12,
\left|\sin\frac{\pi x}{L}\right|
\right\}.
\tag{9}
\]

The new envelope is useful precisely where XF-149 loses power. `A_{N,j}` is nonincreasing in `j`, and for every integer `0<=J<=n`,

\[
\boxed{
\max_{0\le j\le n}
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4e^{-(N-1)as}
\max\!\left\{
B(x)^{n-J},
A_{N,J}
\right\}.
}
\tag{10}
\]

Thus one may use spatial contact for all derivative orders `j<=J` and binomial frequency suppression for all `j>=J`. No derivative order has to satisfy both mechanisms simultaneously.

The moment in `(5)` has the elementary bound

\[
\boxed{
A_{N,J}
\le
 e^{-J/N}
\left(
\frac{1+e^{-J/N}}2
\right)^n
\le
\exp\!\left(-\frac{3nJ}{8N}\right)
}
\tag{11}
\]

for `0<=J<=n`. Consequently, let `Omega_N` be any predetermined real space-time observation set and define

\[
d_N
:=
\inf_{(x,s)\in\Omega_N}
\operatorname{dist}_{\mathbb T_L}(x,x_{\rm anti}),
\qquad
x_{\rm anti}=L/2\pmod L,
\tag{12}
\]

\[
B_N
:=
\max\!\left\{
\frac12,
\cos\frac{\pi d_N}{L}
\right\},
\qquad
\kappa_N:=-\log B_N.
\tag{13}
\]

If `N>=8` and `N kappa_N>=4`, choosing

\[
J_N
:=
\left\lfloor\frac{\kappa_NN}{2}\right\rfloor
\tag{14}
\]

in `(10)` gives the uniform full-jet estimate

\[
\boxed{
\max_{0\le j\le N-2}
\sup_{(x,s)\in\Omega_N}
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4\exp\!\left(-\frac{3}{32}(N-2)\kappa_N\right).
}
\tag{15}
\]

The heat factor was dropped only because it is at most one. Equation `(15)` is therefore an **all-future, full-degree normalized derivative-jet barrier**.

For a polynomially normalized linear sensor bank, the same conclusion survives arbitrary mixing of derivative orders. Let

\[
\mathcal S_{r,N}(R)
:=
\sum_{j=0}^{n}
\int_{\Omega_N}
\mathscr D_N^jR\,d\mu_{r,j,N},
\qquad
1\le r\le m_N,
\tag{16}
\]

where the signed/complex finite measures are predetermined and

\[
W_N
:=
\max_{1\le r\le m_N}
\sum_{j=0}^{n}
\|\mu_{r,j,N}\|_{\rm TV}.
\tag{17}
\]

If `m_N` and `W_N` grow at most polynomially, then the two controls in `(1)` satisfy

\[
\boxed{
\left\|
\mathcal S_N(R_1)-
\mathcal S_N(R_{\lambda_\rho})
\right\|_{\ell^2}
\le
4\sqrt{m_N}W_N
\exp\!\left(-\frac{3}{32}(N-2)\kappa_N\right).
}
\tag{18}
\]

Any Lipschitz decoder of the transition time on a class containing this pair must therefore have condition number

\[
\boxed{
K_N
\ge
\frac{\rho}{4\sqrt{m_N}W_N}
\exp\!\left(\frac{3}{32}(N-2)\kappa_N\right).
}
\tag{19}
\]

Two consequences are immediate. On every fixed proper aperture `d_N/L>=delta>0`, `kappa_N>=kappa_delta>0`, so **even the complete degree-order real derivative jet remains exponentially transition-blind**. If instead `d_N/L->0`, then

\[
\kappa_N
=
\frac{\pi^2}{2}\frac{d_N^2}{L^2}
+O\!\left(\frac{d_N^4}{L^4}\right),
\tag{20}
\]

and therefore

\[
\boxed{
\frac{Nd_N^2}{L^2\log N}
\longrightarrow\infty
}
\tag{21}
\]

still forces superpolynomial transition conditioning **even when every normalized derivative order `0,...,N-2` is available**. Thus the maximal-contact pair does not merely trade derivative depth against spatial reach as in XF-149. Once the high-derivative frequency profile is used, its necessary antipodal escape scale returns, up to constants, to

\[
\boxed{
d_N
=O\!\left(
L\sqrt{\frac{\log N}{N}}
\right),}
\tag{22}
\]

the same visibility layer already found for the raw trace in XF-147--XF-148.

Equation `(22)` is again only a necessary escape condition for this matched-control certificate. It does not say that observing the antipodal layer is sufficient for stable recovery, and it does not assert that Xi realizes the maximal-contact pair.

## 1. Exact heat evolution exposes a binomial Fourier-frequency law

Start from the exact XF-145--XF-149 Gaussian packet

\[
t_*\Delta Q(y,s)
=-2\sigma
 e^{Ny/2-M^2u}
\mathbb E
\sinh^n\!\left(
\frac y2+qZ
\right),
\tag{23}
\]

where

\[
N=2M,
\qquad
n=N-2,
\qquad
u:=as,
\qquad
q:=\sqrt{u/2},
\qquad
|\sigma|=1.
\tag{24}
\]

Expand the power before taking absolute values:

\[
\sinh^n w
=
2^{-n}
\sum_{k=0}^{n}
(-1)^k\binom nk
 e^{(n-2k)w}.
\tag{25}
\]

The Gaussian moment is exact,

\[
\mathbb E e^{(n-2k)qZ}
=
\exp\!\left(
\frac{(n-2k)^2u}{4}
\right).
\tag{26}
\]

Set

\[
m:=N-1-k.
\tag{27}
\]

Because `n=N-2`, the spatial exponent simplifies to

\[
\frac{N+n-2k}{2}=m,
\tag{28}
\]

while the heat exponent satisfies

\[
-M^2u+rac{(n-2k)^2u}{4}
=-m(N-m)u.
\tag{29}
\]

Hence the complete packet has the finite exact expansion

\[
\boxed{
t_*\Delta Q(y,s)
=-2\sigma\,2^{-n}
\sum_{k=0}^{n}
(-1)^k\binom nk
 e^{(N-1-k)y}
 e^{-(N-1-k)(k+1)u}.
}
\tag{30}
\]

Equivalently, its frequencies are exactly the integers

\[
1,2,\ldots,N-1,
\tag{31}
\]

with absolute coefficient profile equal to a reflected `Bin(n,1/2)` law. This is the structure hidden by the iterated product-rule estimate in XF-149.

Every frequency in `(30)` has heat eigenvalue at least `N-1`:

\[
(N-1-k)(k+1)
=m(N-m)
\ge N-1.
\tag{32}
\]

Thus all of the high-derivative estimates below are automatically uniform over the complete future.

## 2. High normalized derivatives are frequency moments, not worst-case Bernstein growth

On the physical real circle,

\[
y=-\frac{2\pi ix}{L},
\qquad
|e^{my}|=1,
\tag{33}
\]

and XF-149 gives

\[
\mathscr D_N
=-\frac{i}{N}\partial_y
\tag{34}
\]

up to an irrelevant unit phase. Applying `j` normalized derivatives to `(30)` therefore multiplies its `m`-th frequency by exactly `(m/N)^j` in modulus. Taking the triangle inequality only after this exact diagonalization gives

\[
\left|
\mathscr D_N^j(t_*\Delta Q)(x,s)
\right|
\le
2e^{-(N-1)u}
2^{-n}
\sum_{k=0}^{n}
\binom nk
\left(\frac{N-1-k}{N}\right)^j.
\tag{35}
\]

This is `(7)` for `t_*Delta Q`. Since XF-149 has the exact relation

\[
R_1-R_{\lambda_\rho}
=(1-\lambda_\rho)t_*\Delta Q,
\qquad
0<1-\lambda_\rho<1,
\tag{36}
\]

`(7)` follows.

The contrast with a generic degree-`N` Bernstein inequality is important. A worst-case polynomial could place essentially all of its mass at frequency `N`, in which case root-spacing normalization would leave its high derivatives unsuppressed. The maximal-contact packet does not do that. Its frequency mass is binomial, centered near `N/2`, and every high normalized derivative pays a moment of the factor `m/N<1`. This is why the near-full-degree loophole in XF-149 is a proof artifact rather than a real escape for this matched family.

The moments are monotone:

\[
A_{N,j+1}\le A_{N,j},
\tag{37}
\]

because every base `(N-1-k)/N` lies in `(0,1)`. XF-149 independently gives

\[
\left|
\mathscr D_N^j
(R_1-R_{\lambda_\rho})(x,s)
\right|
\le
4e^{-(N-1)as}B(x)^{n-j}.
\tag{38}
\]

For `j<=J`, the right side of `(38)` is at most

\[
4e^{-(N-1)as}B(x)^{n-J},
\tag{39}
\]

whereas for `j>=J`, `(7)` and `(37)` give at most

\[
2e^{-(N-1)as}A_{N,J}.
\tag{40}
\]

This proves `(10)`. The full jet is controlled by **splitting derivative order**, not by forcing one envelope to remain sharp at every order.

## 3. An elementary binomial MGF is enough to close the full-degree gap

Let `K_N~Bin(n,1/2)`. Since `0<1-(K_N+1)/N<1`,

\[
\left(1-\frac{K_N+1}{N}\right)^J
\le
\exp\!\left(
-\frac{J(K_N+1)}{N}
\right).
\tag{41}
\]

Taking expectations gives the first inequality in `(11)`:

\[
A_{N,J}
\le
 e^{-J/N}
\mathbb E e^{-(J/N)K_N}
=
 e^{-J/N}
\left(
\frac{1+e^{-J/N}}2
\right)^n.
\tag{42}
\]

Put `t=J/N`. For `0<=t<=1`,

\[
-\log\frac{1+e^{-t}}2
=
\frac t2-\log\cosh\frac t2.
\tag{43}
\]

The elementary subgaussian inequality

\[
\log\cosh z\le\frac{z^2}{2}
\tag{44}
\]

therefore gives

\[
-\log\frac{1+e^{-t}}2
\ge
\frac t2-rac{t^2}{8}
\ge
\frac{3t}{8}.
\tag{45}
\]

Dropping the additional favorable factor `e^{-t}` yields the second inequality in `(11)`.

Now write `B_N=e^{-kappa_N}` and choose `(14)`. Since `B_N>=1/2`,

\[
0\le\kappa_N\le\log2<1.
\tag{46}
\]

When `N>=8`,

\[
J_N\le\frac{\log2}{2}N
\quad\Longrightarrow\quad
n-J_N\ge\frac n2.
\tag{47}
\]

Therefore the low-order branch of `(10)` obeys

\[
B_N^{n-J_N}
\le
 e^{-\kappa_Nn/2}.
\tag{48}
\]

If `N kappa_N>=4`, flooring loses at most a factor two in the chosen split depth:

\[
J_N
\ge
\frac{\kappa_NN}{4}.
\tag{49}
\]

Equation `(11)` then gives

\[
A_{N,J_N}
\le
\exp\!\left(
-\frac{3}{32}n\kappa_N
\right).
\tag{50}
\]

The high-order branch `(50)` is weaker than `(48)` and therefore controls the maximum in `(10)`, proving `(15)`.

The constant `3/32` is deliberately not optimized. The exact moment `(5)` admits a sharper Laplace-principle rate for `j` proportional to `N`, but no such refinement is needed for the phase boundary: `(50)` already retains a fixed positive fraction of the full spatial exponent `n kappa_N` uniformly through derivative order `n`.

## 4. Full-degree linear sensors still see the same antipodal visibility layer

The measure formulation `(16)` includes much more than a pointwise jet. Dirac measures give derivative samples at arbitrary predetermined points; atomic measures give arbitrary polynomially weighted derivative grids; absolutely continuous measures give distributed derivative observations; and allowing every `j=0,...,n` in the same sensor permits polynomially normalized mixing across the complete jet.

Equation `(15)` and total variation give, for each `r`,

\[
\left|
\mathcal S_{r,N}(R_1)
-
\mathcal S_{r,N}(R_{\lambda_\rho})
\right|
\le
4W_N
 e^{-3n\kappa_N/32}.
\tag{51}
\]

Taking the `ell^2` norm proves `(18)`, and the fixed transition-time separation `rho` proves `(19)`.

For a fixed proper aperture, `kappa_N` is bounded below, so `(19)` is exponential in `N` regardless of whether the sensor uses one derivative, a linearly deep jet, or every derivative through degree `N-2`. This strictly strengthens XF-149's fixed-aperture conclusion, which stopped deciding the case `N-J_N=O(log N)`.

Near the antipode, `(20)` turns the exponent into

\[
\frac{3\pi^2+o(1)}{64}
\frac{Nd_N^2}{L^2}.
\tag{52}
\]

Polynomially many sensors and polynomial total variation cost only `O(log N)` in the logarithm of the observation gap. Hence `(21)` makes the inverse condition number superpolynomial. The derivative bank has **not** enlarged the escape layer from `L sqrt(log N/N)` to the `L sqrt(log N/(N-J_N))` scale suggested by the one-envelope certificate of XF-149. That earlier depth/reach tradeoff was valid as a sufficient blindness certificate, but it was not the true high-jet boundary of the maximal-contact pair.

The mechanism is transparent. Low derivative orders preserve many of the packet's `n` spatial zeros and are suppressed by distance from the antipode. High derivative orders can consume those zeros, but doing so weights a binomial Fourier profile by `(m/N)^j`, which is itself exponentially costly. The two losses overlap enough that **no normalized derivative order is large on a proper aperture**.

## 5. Boundary checks, prior-art audit, and research implication

Several stress tests prevent the new envelope from being misread.

At `j=0`, `A_{N,0}=1`, so `(7)` has no spatial information. The entire aperture suppression comes from XF-149's factor `B(x)^n`, exactly as it should.

At `j=n`, XF-149's local bound becomes `O(1)` and was intentionally silent. Equation `(7)` instead gives

\[
\left|
\mathscr D_N^n(R_1-R_{\lambda_\rho})
\right|
\le
2A_{N,n},
\tag{53}
\]

and `(11)` with `J=n` makes this exponentially small. This agrees with XF-149's center check based on the factorial ratio `n!/(2N)^n`, but now holds uniformly on the whole real circle and through all future heat times.

At the exact antipode, `B_N=1` and `kappa_N=0`; `(15)` correctly becomes vacuous. The packet is designed to become visible there, so no proper-aperture argument should suppress that point.

At positive heat time, every exact Fourier mode in `(30)` carries at least `e^{-(N-1)as}`. Waiting cannot amplify any normalized spatial derivative of this matched difference; it only decreases the envelope.

The neighboring classical frameworks are Bernstein/Markov derivative inequalities for trigonometric polynomials, binomial/Krawtchouk frequency profiles, and elementary large-deviation or Laplace estimates for binomial moments. The exact series `(30)` and the MGF bound `(42)` are derived directly here and no external theorem is load-bearing. The prior-art audit therefore does not create a new `SOURCES.md` dependency. The claim is not that binomial moment estimates are new; the Mathia-specific content is that the canonical maximal-contact transition-sharp control has exactly this binomial heat-frequency law, and that combining it with the previously derived aperture envelope closes the full-degree real-jet escape.

This result materially narrows the target-side frontier. Increasing a real root-scale derivative bank all the way to the algebraic degree is **not** a distinct route out of XF-147--XF-149. For this adversary, stable polynomial transition visibility still requires reaching the antipodal layer, using a sensor with more than polynomial normalization, using genuinely different nonlocal information not controlled by the full real spatial jet on the prescribed support, or leaving the matched-control class through source-specific Xi structure.

The source-side escape remains unchanged: prove that the actual Xi heat flow excludes the maximal-contact direction, or prove a source-faithful observable whose normalization carries information that the periodic full-jet data above does not.

## Scope and falsification

The theorem concerns the raw real periodic heat trace, root-spacing-normalized spatial derivatives, predetermined observation geometry, and polynomially normalized linear combinations of those derivatives. It does not cover exponentially weighted sensors, nonlinear functionals without a controlled Lipschitz modulus, adaptive observation policies that move support discontinuously in response to the data, complex off-circle information, or a positive-time interval encoded with an external inverse-heat normalization.

It also does not assert that the Xi source realizes the matched pair, and `(22)` is not a sufficiency theorem for recovery near the antipode.

A direct falsifier is any `N`, `0<=j<=N-2`, real `x`, and `s>=0` for which the exact expansion `(30)` or the moment bound `(7)` fails. Algebraically, `(30)` follows only from the binomial expansion of `sinh^n`, the Gaussian moment generating function, and the identity

\[
-\frac{N^2}{4}
+rac{(N-2-2k)^2}{4}
=-(N-1-k)(k+1).
\tag{54}
\]

A second falsifier is any counterexample to `(11)`; its proof is the one-line comparison `(41)` followed by the exact binomial MGF and `(44)`. Thus the new full-degree conclusion does not depend on unproved asymptotics or a literature estimate.

The next useful target-side test is no longer “add more local derivatives.” A genuinely new route must either touch the antipodal visibility layer, use complex/off-circle data, exploit a nonlinear quantity with a justified stable modulus that is not controlled by `(16)`, or derive source-specific Xi restrictions that forbid the maximal-contact packet entirely.