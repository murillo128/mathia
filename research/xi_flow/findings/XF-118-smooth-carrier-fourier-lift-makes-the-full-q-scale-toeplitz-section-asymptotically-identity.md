# XF-118 — smooth-carrier Fourier lift makes the full q-scale Toeplitz section asymptotically identity

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `FULL-Q-SCALE-TOEPLITZ-COERCIVITY` + `POSITIVE-DENSITY-LIFT`. XF-115 proves that every order-`K` plane-wave/Fejer test of the mass-preserving Xi source is asymptotically positive on the full mesh-angle circle. XF-116 and XF-117 then force any hypothetical nonpositive witness to become increasingly non-plane-wave, broad, and multiscale. The remaining escape can in fact be removed for the actual Xi source. The cardinal deposition of XF-108 lets the autocorrelation of an **arbitrary** coefficient vector be interpolated by one fixed Schwartz multiplier, while the autocorrelation Fourier series is the positive density `|P_v|^2`. A smooth carrier version of the XF-114/XF-115 Vinogradov--Korobov argument is uniformly flat at every polynomial physical frequency. These two facts lift scalar source flatness to the full finite Toeplitz cone:

\[
\boxed{
\|\widehat T_K-I\|_{\rm op}\longrightarrow0.
}
\tag{1}
\]

Consequently

\[
\boxed{
\lambda_{\min}(\widehat T_K)=1-o(1)>0
}
\tag{2}
\]

for all sufficiently large q-scale prefixes. In particular, the nonpositive witnesses constrained in XF-106--XF-117 do not merely have to become more complicated: **they do not exist for the actual mass-preserving Xi q-scale Toeplitz section.**

Keep the normalization of XF-108--XF-117,

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\qquad
\Delta\asymp a^{-3},
\tag{3}
\]

\[
L=\log a+c,
\qquad
K=\left\lfloor\frac L\Delta\right\rfloor,
\qquad
\ell:=(K+1)\Delta=L+O(\Delta),
\tag{4}
\]

and

\[
\widehat T_K=(\widehat\mu_{i-j})_{0\le i,j\le K},
\qquad
\widehat\mu_0=1.
\tag{5}
\]

No RH assumption is used.

## 1. A shrinking smooth carrier has uniformly small Xi source transform at every polynomial frequency

Use the regular logarithmic source measure introduced in XF-115,

\[
dS(\xi)
=
e^\xi\,d\xi
-\frac12\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,\delta_{\lambda_n},
\qquad
\lambda_n=\frac12\log n.
\tag{6}
\]

Set

\[
w_a:=\frac1{\log a}.
\tag{7}
\]

Choose a real smooth cutoff `chi_a` on the positive half-line such that

\[
\chi_a(\xi)=1\quad(0\le\xi\le\ell),
\qquad
\operatorname{supp}\chi_a\subset[0,\ell+w_a],
\tag{8}
\]

with `chi_a` constant near zero and

\[
\|\chi_a^{(j)}\|_\infty\ll_j w_a^{-j}.
\tag{9}
\]

Define the normalized smooth-carrier transform

\[
\mathfrak H_a(y)
:=
\frac1a
\int_0^\infty
\chi_a(\xi)e^{iy\xi}\,dS(\xi).
\tag{10}
\]

The first new lemma is that, for every fixed `C>0`,

\[
\boxed{
\sup_{|y|\le a^C}|\mathfrak H_a(y)|=o(1).
}
\tag{11}
\]

There is also the crude global bound

\[
\boxed{
\sup_{y\in\mathbb R}|\mathfrak H_a(y)|=O_c(1).
}
\tag{12}
\]

The latter follows directly from total variation. The archimedean mass in `(8)` is `O(e^{\ell+w_a})=O_c(a)`, while Chebyshev gives

\[
\sum_{\lambda_n\le\ell+w_a}
\frac{\Lambda(n)}{\sqrt n}
\ll e^{\ell+w_a}=O_c(a).
\tag{13}
\]

The content is `(11)`. It is the smooth compact-carrier analogue of the triangular transform estimate in XF-115, and the same unconditional Vinogradov--Korobov zero-free region is sufficient.

Let

\[
I_a(z)
:=
\int_0^\infty
\chi_a(\xi)e^{iz\xi}\,d\xi.
\tag{14}
\]

Because `chi_a=1` near zero, repeated integration by parts isolates the only lower-end boundary term. For every fixed integer `M>=2` and `|z|>=1`,

\[
\boxed{
I_a(z)
=-\frac1{iz}
+O_M\!\left(
\frac{w_a^{1-M}e^{(\ell+w_a)|\operatorname{Im}z|}}
{|z|^M}
\right).
}
\tag{15}
\]

For `|z|<1`, the trivial integral bound gives

\[
|I_a(z)|
\ll
(\ell+w_a)e^{(\ell+w_a)|\operatorname{Im}z|}.
\tag{16}
\]

Now use the paired Hadamard/positive-frequency zero-field bridge already established in XF-051 and used quantitatively in XF-114/XF-115. For

\[
\rho=\beta+i\gamma,
\qquad
x_\rho=2\gamma+i(1-2\beta),
\tag{17}
\]

one obtains, after choosing one representative from each `x<->-x` pair,

\[
\left\langle
\mathcal Z_0,
\chi_a(\xi)e^{iy\xi}
\right\rangle_{\rm can}
=
\sum_x
\left[I_a(y-x)+I_a(y+x)\right].
\tag{18}
\]

The canonical endpoint correction from the regular source `(6)` to `(18)` is still only

\[
O\!\left(\log(1/\Delta)\right)
\tag{19}
\]

uniformly in real `y`: the extra endpoint term is supported at zero, and the singular regularization `B(\xi)-e^\xi=-1/(4\xi)+O(1)` has absolute mass `O(log(1/Delta))` on a bounded cutoff. After division by `a` this is `o(1)`, exactly as in XF-114/XF-115.

Fix `C` and split `(18)` at

\[
R:=a^{C+2}.
\tag{20}
\]

For the zeros with `|gamma|<=R`, the Vinogradov--Korobov region already anchored in `SOURCES.md` gives

\[
1-|\operatorname{Im}x_\rho|
\gg_C
\frac1{(\log a)^{2/3}(\log\log a)^{1/3}}
=:d_a.
\tag{21}
\]

The exponentially amplified remainder in `(15)` therefore pays

\[
\frac{e^{(\ell+w_a)|\operatorname{Im}x|}}a
\ll_c
\exp(-d_a\ell+O(1))
=o((\log a)^{-A})
\tag{22}
\]

for every fixed `A`. Partitioning the real zero coordinates into unit intervals and using the Riemann--von Mangoldt local count makes the contribution of the remainder in `(15)`

\[
O_{C,M}\!\left(
(\log a)^{O_M(1)}e^{-d_a\ell}
\right)=o(1).
\tag{23}
\]

The non-amplified boundary term in `(15)` is also harmless, but here the `+-` pairing is essential. Away from the `O(1)`-neighborhoods of the two resonances `x=+-y`,

\[
\frac1{y-x}+\frac1{y+x}
=
\frac{2y}{y^2-x^2}.
\tag{24}
\]

Unit-interval zero counting then gives only a polylogarithmic total contribution. The resonant intervals contain `O(log(2+R))` zeros and are controlled by `(16)`; after `(21)` their off-critical amplification satisfies `(22)`, while critical-line or centrally located zeros contribute only `O(ell log R)=o(a)`. Hence the whole local-zero block is `o(a)` uniformly for `|y|<=a^C`.

For `|gamma|>R`, equation `(24)` gives a paired boundary tail

\[
\ll
|y|\sum_{|\gamma|>R}\frac1{\gamma^2}
\ll
\frac{|y|\log R}{R},
\tag{25}
\]

while the critical strip `|Im x|<1` and `(15)` give

\[
\ll_M
a\,w_a^{1-M}
\sum_{|\gamma|>R}\frac1{|\gamma|^M}
\ll_M
a\,w_a^{1-M}
\frac{\log R}{R^{M-1}}.
\tag{26}
\]

After division by `a`, `(20)`, `(25)`, and `(26)` are `o(1)`. This proves `(11)`.

The use of a shrinking transition width `w_a=1/log a` is deliberate. The auxiliary carrier reaches only a `1+o(1)` multiplicative arithmetic layer beyond the q-scale endpoint. Its derivative losses are merely polylogarithmic and are swallowed by `(22)`. Thus `(11)` is not obtaining coercivity from a hidden fixed-width prime band.

## 2. Every arbitrary coefficient autocorrelation becomes one positive Fourier density

Let

\[
v=(v_0,\ldots,v_K),
\qquad
\|v\|_2=1,
\tag{27}
\]

be an arbitrary complex unit vector. For `m>=0` define

\[
r_m
:=
\sum_{j=0}^{K-m}
\overline{v_{j+m}}v_j,
\qquad
r_{-m}:=\overline{r_m},
\tag{28}
\]

and put `r_m=0` for `|m|>K`. With

\[
P_v(s):=\sum_{j=0}^K v_j e^{ijs},
\tag{29}
\]

the complete autocorrelation Fourier series is the exact positive identity

\[
\boxed{
\sum_{m\in\mathbb Z}r_m e^{-ims}
=|P_v(s)|^2.
}
\tag{30}
\]

In particular,

\[
\frac1{2\pi}
\int_{-\pi}^{\pi}|P_v(s)|^2\,ds=1.
\tag{31}
\]

Let `varphi_psi` be the translation-invariant cardinal kernel extracted in XF-115 from the mass-preserving XF-108 deposition,

\[
\omega_\psi(m,u)=\varphi_\psi(m-u),
\qquad
\varphi_\psi\in C_c^\infty([-1,1]).
\tag{32}
\]

Interpolate the **full** autocorrelation by

\[
R_v(\xi)
:=
\sum_{m\in\mathbb Z}
r_m\,
\varphi_\psi\!\left(m-\frac\xi\Delta\right).
\tag{33}
\]

Its ordinary Fourier transform is exact:

\[
\boxed{
\widehat R_v(y)
=
\Delta\,
\widehat\varphi_\psi(-\Delta y)
|P_v(\Delta y)|^2.
}
\tag{34}
\]

This is the step that is unavailable if one treats the deposition phase atom-by-atom. No smoothness, packet structure, support density, or plane-wave approximation is imposed on `v`; all of its complexity is absorbed into the positive periodic density `|P_v|^2`.

For `xi>=0`, the negative-lag summands in `(33)` vanish because `varphi_psi` is supported in `[-1,1]` and vanishes at the endpoints. Moreover `R_v(xi)=0` for `xi>=ell`. Hence the cutoff `(8)` is exactly invisible to the desired source pairing:

\[
\int R_v\,dS
=
\int \chi_a R_v\,dS.
\tag{35}
\]

## 3. Polynomial source flatness plus Schwartz cardinal decay is uniform over the entire Toeplitz cone

Fourier inversion in `(35)` and `(34)` gives

\[
\boxed{
\frac1a\int R_v(\xi)\,dS(\xi)
=
\frac1{2\pi}
\int_{\mathbb R}
\widehat\varphi_\psi(-s)
|P_v(s)|^2
\mathfrak H_a(s/\Delta)
\,ds.
}
\tag{36}
\]

The interchange is absolutely legitimate uniformly in `v`. Indeed, since `widehat varphi_psi` is Schwartz,

\[
C_\psi
:=
\sum_{k\in\mathbb Z}
\sup_{s\in[2\pi k-\pi,2\pi k+\pi]}
|\widehat\varphi_\psi(s)|
<\infty,
\tag{37}
\]

and `(31)` gives

\[
\int_{\mathbb R}
|\widehat\varphi_\psi(s)|
|P_v(s)|^2\,ds
\le
2\pi C_\psi.
\tag{38}
\]

Split `(36)` at `|s|=a`. Since `Delta asymp a^{-3}`, the central part only asks for

\[
|s/\Delta|\ll a^4.
\tag{39}
\]

Equation `(11)` with `C=4`, together with `(38)`, therefore gives

\[
\sup_{\|v\|_2=1}
\left|
\int_{|s|\le a}
\widehat\varphi_\psi(-s)|P_v(s)|^2
\mathfrak H_a(s/\Delta)\,ds
\right|
=o(1).
\tag{40}
\]

For the tail, `(12)` and Schwartz decay imply, for every fixed `M>2`,

\[
\sup_{\|v\|_2=1}
\int_{|s|>a}
|\widehat\varphi_\psi(s)|\,|P_v(s)|^2
|\mathfrak H_a(s/\Delta)|\,ds
\ll_{\psi,M}a^{1-M}
=o(1).
\tag{41}
\]

Thus

\[
\boxed{
\sup_{\|v\|_2=1}
\left|
\frac1a\int R_v\,dS
\right|=o(1).
}
\tag{42}
\]

The important feature is that the dimension `K+1 asymp a^3 log a` never appears in the loss. The periodic `L^1` mass of `|P_v|^2` is exactly fixed by `(31)`, while the nonperiodic cardinal multiplier is summable over all aliases by `(37)`.

## 4. Return to the actual Xi Toeplitz moments

Define the deposited regular-source coefficients for every integer `m` by

\[
\nu_m
:=
\frac1a
\int_0^\infty
\varphi_\psi\!\left(m-\frac\xi\Delta\right)dS(\xi).
\tag{43}
\]

XF-115 already proves on the visible positive lags

\[
\boxed{
\sum_{m=1}^K
|\widehat\mu_m-\nu_m|
\ll_{\psi,c}
\Delta+
\frac{\log(1/\Delta)}a
=o(1).
}
\tag{44}
\]

Because `dS` is supported on `xi>=0`, compact support of `varphi_psi` gives

\[
\nu_m=0\qquad(m<0).
\tag{45}
\]

At `m=0`, there are no prime atoms for large `a` in the one-cell interval `0<=xi<=Delta`, so

\[
\nu_0=O(\Delta/a)=o(1).
\tag{46}
\]

Equations `(33)`, `(43)`, `(45)`, and `(46)` yield

\[
\frac1a\int R_v\,dS
=
\nu_0+
\sum_{m=1}^K\nu_m r_m.
\tag{47}
\]

On the other hand, from `(5)` and `(28)`,

\[
v^*\widehat T_Kv-1
=
2\operatorname{Re}
\sum_{m=1}^K\widehat\mu_m r_m.
\tag{48}
\]

Since `|r_m|<=1`, equations `(42)`, `(44)`, `(46)`, and `(47)` give uniformly over all unit vectors

\[
\boxed{
\sup_{\|v\|_2=1}
|v^*(\widehat T_K-I)v|
=o(1).
}
\tag{49}
\]

The matrix is Hermitian, so `(49)` is exactly the operator-norm statement `(1)`. Equation `(2)` follows.

## 5. Stress tests and what this closes

The terminal-band abstract control used in XF-116/XF-117 does not contradict `(1)`. It was designed to saturate absolute lag-window bounds while retaining a negative corner mode. Such a control is **not** the Xi source and does not satisfy the new smooth-carrier transform `(11)`: its coherent terminal strip leaves an order-one polynomial-frequency carrier. This identifies the extra arithmetic input used here rather than hiding it inside the block estimate.

No symmetry of the deposition bump is used. The cardinal kernel may be asymmetric; `(34)` retains its complex Fourier multiplier and only uses its Schwartz decay. Likewise, the proof treats arbitrary complex `v`, so positivity is not obtained by restricting to real eigenvectors or to one angular packet.

The shrinking auxiliary cutoff is also a falsification control. Its transition width is `1/log a`, while the autocorrelation interpolation is already zero at `xi=ell`. Therefore changing the cutoff outside the q-scale support cannot alter the left-hand side of `(35)`. The extra source interval exists only to make the Hadamard kernel rapidly summable, and its multiplicative arithmetic depth tends to one.

The durable consequence is that the specific source-side obstruction pursued since XF-105 is now closed at the natural q-scale: **the mass-preserving Xi moments through `L=log a+O(1)` form an asymptotically coercive Toeplitz section, not merely a sequence whose simple tests happen to be positive.** XF-108's smooth-witness cancellation, XF-110/XF-112's thin bad-spectrum picture, XF-115's full-circle Fejer flatness, and XF-116/XF-117's packet gates are all strict shadows of `(1)`.

This does **not** prove `Lambda<=0` or RH. It proves a source-admission/coercivity theorem for the q-scale moment section. The research line still needs a separate bridge from this source-faithful moment positivity to the equal-weight real-divisor/heat-transition mechanism, or else it must move to the distinct first-prime-band route. In particular, no conclusion about finite-node realization at a prescribed node budget is asserted here merely from Toeplitz positivity.

## 6. Prior-art boundary

The generic ingredients are classical. Autocorrelation Fourier series of finite vectors are nonnegative trigonometric polynomials; Toeplitz quadratic forms and Fejer--Riesz/Wiener--Khinchin positivity are standard. Poisson/cardinal sampling and Schwartz alias decay are also classical. The Guinand--Weil/Hadamard explicit formula and the Vinogradov--Korobov zero-free region are already anchored in `SOURCES.md`; the latter is the only external arithmetic theorem load-bearing in `(11)`. No new source entry is therefore required.

A directed prior-art check included the standard Toeplitz/positive-trigonometric-polynomial literature, the Fourier-interpolation neighborhood already audited in XF-115 (including Bondarenko--Radchenko--Seip), and modern Vinogradov--Korobov zero-free-region references. That search did not locate the q-dependent statement `(1)` for the mass-preserving Xi deposition. No novelty is claimed for any classical component. The Mathia-specific delta is the combination: **a smooth polynomial-frequency Xi carrier estimate, inserted through the exact cardinal interpolation of arbitrary Toeplitz autocorrelations, removes the dimension loss because every witness contributes only one period-normalized positive Fourier density.**