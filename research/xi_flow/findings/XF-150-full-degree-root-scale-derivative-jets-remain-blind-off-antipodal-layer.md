# XF-150 — full-degree root-scale derivative jets remain blind off the antipodal layer

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/DISTRIBUTIONAL-REAL-SENSOR-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-OBSERVATION` + `FULL-FUTURE` + `FULL-DEGREE-JET` + `BINOMIAL-FREQUENCY-MOMENT`. XF-149 proves that root-spacing-normalized derivatives preserve the antipodal aperture obstruction while a macroscopic residual degree remains, but its product-rule envelope becomes noninformative at near-full derivative depth. For the same maximal-contact pair, the exact heat/Fourier expansion gives a complementary high-derivative envelope: the packet has a reflected binomial frequency profile, so large normalized derivative orders are themselves exponentially small. Combining the two envelopes closes the high-jet loophole. Even the complete normalized real spatial jet through degree `N-2`, observed through the entire future, remains exponentially transition-blind on every fixed proper aperture and superpolynomially blind until the support enters the same `L sqrt(log N/N)` antipodal layer forced for the raw trace.

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

For `0<=j<=n`, define

\[
\boxed{
A_{N,j}
:=
2^{-n}\sum_{k=0}^{n}
\binom nk
\left(\frac{N-1-k}{N}\right)^j.
}
\tag{5}
\]

Equivalently, for `K_N~Bin(n,1/2)`,

\[
A_{N,j}
=
\mathbb E\left(1-\frac{K_N+1}{N}\right)^j.
\tag{6}
\]

Then for every real `x`, every `s>=0`, and every `0<=j<=n`,

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

XF-149 independently gives

\[
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4e^{-(N-1)as}B(x)^{n-j},
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

Hence

\[
\boxed{
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4e^{-(N-1)as}
\min\!\left\{B(x)^{n-j},A_{N,j}\right\}.
}
\tag{10}
\]

The moments `A_{N,j}` decrease with `j`. Therefore, for every integer `0<=J<=n`, low derivative orders can use the aperture envelope while high derivative orders use the frequency envelope:

\[
\boxed{
\max_{0\le j\le n}
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4e^{-(N-1)as}
\max\!\left\{B(x)^{n-J},A_{N,J}\right\}.
}
\tag{11}
\]

The binomial moment obeys the elementary bound

\[
\boxed{
A_{N,J}
\le
 e^{-J/N}
\left(\frac{1+e^{-J/N}}2\right)^n
\le
\exp\!\left(-\frac{3nJ}{8N}\right)
}
\tag{12}
\]

for `0<=J<=n`.

Now let `Omega_N` be any predetermined real space-time observation set. Define

\[
d_N
:=
\inf_{(x,s)\in\Omega_N}
\operatorname{dist}_{\mathbb T_L}(x,x_{\rm anti}),
\qquad
x_{\rm anti}=L/2\pmod L,
\tag{13}
\]

and

\[
B_N
:=
\max\!\left\{
\frac12,
\cos\frac{\pi d_N}{L}
\right\},
\qquad
\kappa_N:=-\log B_N.
\tag{14}
\]

If `N>=8` and `N kappa_N>=4`, choose

\[
J_N
:=
\left\lfloor\frac{\kappa_NN}{2}\right\rfloor.
\tag{15}
\]

Then

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
\tag{16}
\]

Thus the complete degree-order normalized real derivative jet is uniformly small through the entire future.

For a polynomially normalized linear sensor bank, let

\[
\mathcal S_{r,N}(R)
:=
\sum_{j=0}^{n}
\int_{\Omega_N}
\mathscr D_N^jR\,d\mu_{r,j,N},
\qquad
1\le r\le m_N,
\tag{17}
\]

and define

\[
W_N
:=
\max_{1\le r\le m_N}
\sum_{j=0}^{n}
\|\mu_{r,j,N}\|_{\rm TV}.
\tag{18}
\]

If `m_N` and `W_N` are polynomial in `N`, then

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
\tag{19}
\]

Any Lipschitz transition-time decoder on a class containing this pair has condition number at least

\[
\boxed{
K_N
\ge
\frac{\rho}{4\sqrt{m_N}W_N}
\exp\!\left(\frac{3}{32}(N-2)\kappa_N\right).
}
\tag{20}
\]

On every fixed proper aperture, `kappa_N` is bounded below and `(20)` is exponential in `N`, even with every derivative order `0,...,N-2` available. If `d_N/L->0`, then

\[
\kappa_N
=
\frac{\pi^2}{2}\frac{d_N^2}{L^2}
+O\!\left(\frac{d_N^4}{L^4}\right),
\tag{21}
\]

so

\[
\boxed{
\frac{Nd_N^2}{L^2\log N}
\longrightarrow\infty
}
\tag{22}
\]

still forces superpolynomial transition conditioning. Consequently this matched pair stops certifying superpolynomial blindness only after one reaches, up to constants, the same antipodal layer

\[
\boxed{
d_N
=O\!\left(
L\sqrt{\frac{\log N}{N}}
\right)
}
\tag{23}
\]

already found for the raw trace in XF-147--XF-148. Equation `(23)` is a necessary escape condition for this certificate, not a sufficiency theorem for recovery.

## 1. Exact heat evolution exposes a binomial Fourier-frequency law

XF-145--XF-149 give the exact maximal-contact packet

\[
t_*\Delta Q(y,s)
=-2\sigma
 e^{Ny/2-M^2u}
\mathbb E
\sinh^n\!\left(\frac y2+qZ\right),
\tag{24}
\]

with

\[
N=2M,
\qquad
n=N-2,
\qquad
u=as,
\qquad
q=\sqrt{u/2},
\qquad
|\sigma|=1.
\tag{25}
\]

Here the scalar heat variable is `u=as`; the displayed `u` in `(24)`--`(25)` is not an additional parameter.

Expand before taking absolute values:

\[
\sinh^n w
=
2^{-n}\sum_{k=0}^{n}
(-1)^k\binom nk e^{(n-2k)w}.
\tag{26}
\]

The Gaussian moment gives

\[
\mathbb E e^{(n-2k)qZ}
=
\exp\!\left(\frac{(n-2k)^2u}{4}\right).
\tag{27}
\]

Set

\[
m:=N-1-k.
\tag{28}
\]

Because `n=N-2`,

\[
\frac{N+n-2k}{2}=m,
\tag{29}
\]

and

\[
-M^2u
+\frac{(n-2k)^2u}{4}
=-m(N-m)u.
\tag{30}
\]

Therefore

\[
\boxed{
t_*\Delta Q(y,s)
=-2\sigma\,2^{-n}
\sum_{k=0}^{n}
(-1)^k\binom nk
 e^{(N-1-k)y}
 e^{-(N-1-k)(k+1)u}.
}
\tag{31}
\]

The frequencies are exactly `1,...,N-1`, with absolute coefficient profile equal to a reflected `Bin(n,1/2)` law. Every mode has heat eigenvalue at least `N-1` because

\[
(N-1-k)(k+1)=m(N-m)\ge N-1.
\tag{32}
\]

This exact diagonal form is the structure hidden by the iterated product-rule estimate in XF-149.

## 2. High normalized derivatives are binomial frequency moments

On the physical real circle,

\[
y=-\frac{2\pi ix}{L},
\qquad
|e^{my}|=1,
\tag{33}
\]

and XF-149 gives, up to a unit phase,

\[
\mathscr D_N
=-\frac{i}{N}\partial_y.
\tag{34}
\]

Applying `j` normalized derivatives to `(31)` multiplies the frequency `m` by `(m/N)^j` in modulus. Taking the triangle inequality only after this exact diagonalization yields

\[
\left|
\mathscr D_N^j(t_*\Delta Q)(x,s)
\right|
\le
2e^{-(N-1)u}
2^{-n}\sum_{k=0}^{n}
\binom nk
\left(\frac{N-1-k}{N}\right)^j.
\tag{35}
\]

XF-149 also gives the exact relation

\[
R_1-R_{\lambda_\rho}
=(1-\lambda_\rho)t_*\Delta Q,
\qquad
0<1-\lambda_\rho<1,
\tag{36}
\]

so `(35)` proves `(7)`.

The distinction from a generic Bernstein derivative bound is essential. A worst-case degree-`N` trigonometric polynomial may concentrate near frequency `N`, so root-spacing normalization need not suppress its highest derivatives. The maximal-contact packet has a binomial frequency profile concentrated near `N/2`; every large normalized derivative therefore pays a moment of a number strictly below one.

Because every base in `(5)` belongs to `(0,1)`,

\[
A_{N,j+1}\le A_{N,j}.
\tag{37}
\]

For `j<=J`, `(8)` is at most `4e^{-(N-1)as}B(x)^{n-J}`. For `j>=J`, `(7)` and `(37)` are at most `2e^{-(N-1)as}A_{N,J}`. This proves the split estimate `(11)`: low and high derivative orders are suppressed by different mechanisms.

## 3. The binomial MGF closes the near-full-degree loophole

Since

\[
0<1-\frac{K_N+1}{N}<1,
\tag{38}
\]

we have

\[
\left(1-\frac{K_N+1}{N}\right)^J
\le
\exp\!\left(-\frac{J(K_N+1)}{N}\right).
\tag{39}
\]

Taking expectations gives

\[
A_{N,J}
\le
 e^{-J/N}
\mathbb E e^{-(J/N)K_N}
=
 e^{-J/N}
\left(\frac{1+e^{-J/N}}2\right)^n.
\tag{40}
\]

Put `t=J/N`. For `0<=t<=1`,

\[
-\log\frac{1+e^{-t}}2
=
\frac t2-\log\cosh\frac t2.
\tag{41}
\]

Using the elementary inequality

\[
\log\cosh z\le\frac{z^2}{2},
\tag{42}
\]

we obtain

\[
-\log\frac{1+e^{-t}}2
\ge
\frac t2-\frac{t^2}{8}
\ge
\frac{3t}{8},
\tag{43}
\]

which proves `(12)`.

Now write `B_N=e^{-\kappa_N}` and choose `(15)`. Since `B_N>=1/2`,

\[
0\le\kappa_N\le\log2<1.
\tag{44}
\]

For `N>=8`, this choice obeys

\[
n-J_N\ge\frac n2.
\tag{45}
\]

Hence

\[
B_N^{n-J_N}
\le e^{-\kappa_Nn/2}.
\tag{46}
\]

If `N\kappa_N>=4`, flooring gives

\[
J_N\ge\frac{\kappa_NN}{4}.
\tag{47}
\]

Therefore `(12)` yields

\[
A_{N,J_N}
\le
\exp\!\left(-\frac{3}{32}n\kappa_N\right).
\tag{48}
\]

Combining `(46)` and `(48)` in `(11)` proves `(16)`. The constant `3/32` is deliberately unoptimized; the exact moment `(5)` has a sharper large-deviation rate, but that refinement is unnecessary for the phase boundary.

The key point is conceptual: **one does not need a single estimate sharp at every derivative order**. Spatial contact controls the low part of the jet; frequency concentration controls the high part. Their overlap prevents any root-normalized derivative from becoming large away from the antipode.

## 4. The antipodal visibility scale survives the full jet

The sensor class `(17)` contains pointwise derivative jets, arbitrary polynomially weighted derivative grids, distributed derivative measurements, and polynomially normalized mixtures across all derivative orders. Total variation plus `(16)` gives `(19)`, while the fixed transition separation `rho` gives `(20)`.

On a fixed proper aperture this is an exponential obstruction, closing the case `N-J_N=O(log N)` that XF-149 left undecided. Near the antipode, substituting `(21)` into `(20)` gives a logarithmic condition-number exponent of order

\[
\frac{Nd_N^2}{L^2}.
\tag{49}
\]

Polynomially many sensors and polynomial total variation cost only `O(log N)`; hence `(22)` forces superpolynomial inverse conditioning. The depth/reach law of XF-149 remains a valid sufficient blindness certificate at bounded derivative depth, but its apparent enlargement of the escape layer near full degree was an artifact of using only the spatial-contact envelope.

Several checks delimit the result. At `j=0`, `A_{N,0}=1`, so all spatial suppression comes from the aperture factor, as in XF-148. At `j=n`, the XF-149 factor becomes `B^0=1`, while `(12)` makes the frequency moment exponentially small. At the exact antipode, `\kappa_N=0` and `(16)` correctly becomes vacuous. At positive heat time, every exact Fourier mode in `(31)` decays by at least `e^{-(N-1)as}`, so waiting never amplifies the matched difference.

## 5. Prior-art boundary and research implication

The neighboring classical frameworks are Bernstein/Markov derivative inequalities for trigonometric polynomials, binomial or Krawtchouk frequency profiles, and elementary large-deviation/Laplace estimates for binomial moments. None is load-bearing here. Equations `(31)`, `(35)`, and `(40)` are exact consequences of the canonical Mathia packet, the Gaussian moment generating function, and the binomial MGF. The prior-art audit therefore creates no new `SOURCES.md` dependency and no external novelty claim is made for the generic binomial estimates themselves.

The Mathia-specific conclusion is that the transition-sharp maximal-contact pair has exactly the frequency law needed to close XF-149's high-derivative loophole. **Adding more real root-scale derivatives, even all the way to the algebraic degree, is not a distinct target-side escape.** For this adversary, polynomially stable transition visibility still requires reaching the antipodal layer, using more than polynomial sensor normalization, accessing genuinely different complex/off-circle information, or excluding the matched family through source-specific Xi structure.

No existing xi-flow clue changes status from this finding. In particular, the Gaussian-reference and source-selector routes concern different interfaces; this result only removes the idea that a sufficiently deep raw real derivative jet can by itself repair the aperture obstruction.

## Scope and falsification

The theorem concerns the raw real periodic heat trace, root-spacing-normalized spatial derivatives, predetermined observation geometry, and polynomially normalized linear combinations. It does not cover exponentially weighted sensors, nonlinear functionals without a controlled Lipschitz modulus, discontinuously data-adaptive support, complex off-circle information, or external inverse-heat normalization. It also does not assert that the Xi source realizes the matched pair, and `(23)` is not a sufficiency theorem near the antipode.

A direct falsifier is any `N`, `0<=j<=N-2`, real `x`, and `s>=0` for which the exact expansion `(31)` or moment bound `(7)` fails. Algebraically, `(31)` uses only

\[
-\frac{N^2}{4}
+\frac{(N-2-2k)^2}{4}
=-(N-1-k)(k+1),
\tag{50}
\]

while `(12)` follows from `(39)`, the exact binomial MGF, and `(42)`. No unproved asymptotic enters the full-degree conclusion.

The next useful target-side test is therefore no longer “add more local derivatives.” A genuinely new route must touch the antipodal visibility layer, use complex/off-circle data, exploit a stably normalized nonlinear quantity not controlled by `(17)`, or derive source-specific Xi restrictions that forbid the maximal-contact packet.