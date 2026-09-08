# XF-113 — Fejer-well controls pass current q-scale gates yet retain Toeplitz negativity

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `FEJER-SCALE-OBSTRUCTION` + `TOEPLITZ-FEASIBILITY-BOUNDARY`. XF-112 showed that every nonpositive q-scale Xi source-Toeplitz witness must concentrate fixed Fourier mass on a source-determined low-symbol set of normalized measure `O((log a)^2/a^2)`. That set is small in ordinary angular measure, but it is still huge at the resolution of a `(K+1)`-dimensional Toeplitz section: with `K asymp a^3 log a`, its allowed time-bandwidth product is `K (log a)^2/a^2 asymp a (log a)^3 -> infinity`. This gap is genuine rather than an artifact of the trace estimate. An explicit real Fejer-well control can satisfy simultaneously the fixed `ell^1` source budget, the XF-110/XF-112 `ell^2` dilution scale, central symbol flatness, vanishing low-symbol measure, broad coefficient support, macroscopic spectral concentration away from the PNT-flat arc, and extreme lag roughness, while its finite Toeplitz section still has a uniformly negative Rayleigh direction.

This is a matched-control obstruction, not a claim that the actual Xi source has such a well. It shows that the coarse source estimates proved through XF-112 cannot by themselves establish q-scale Toeplitz positivity. The next source-side gate is naturally **Fejer-scale geometry and depth**: one must control negative wells after averaging at angular scale `1/K`, not merely show that their total measure tends to zero.

Keep the q-scale regime

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\qquad
\Delta\asymp a^{-3},
\tag{1}
\]

and

\[
L=\log a+c,
\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor
\asymp a^3\log a,
\qquad c\in\mathbf R
\tag{2}
\]

fixed. Put

\[
\varepsilon_a:=\frac{(\log a)^2}{a^2}
\tag{3}
\]

and choose an even integer `n=n(a)` with

\[
n\asymp \varepsilon_a^{-1}
\asymp \frac{a^2}{(\log a)^2}.
\tag{4}
\]

Then

\[
\boxed{
\frac{K}{n}\asymp a(\log a)^3\longrightarrow\infty.
}
\tag{5}
\]

Equation `(5)` is the scale mismatch left unresolved by XF-112.

## 1. A normalized Fejer well has exactly the XF-112 `ell^2` scale

Define

\[
H_n(x)
:=
\frac1{n^2}
\left|\sum_{j=0}^{n-1}e^{ijx}\right|^2
=
\frac1n
+\frac2n\sum_{m=1}^{n-1}
\left(1-\frac mn\right)\cos(mx).
\tag{6}
\]

Thus `0<=H_n<=1`, `H_n(0)=1`, and its mass is `1/n`. For even `n`, `H_n(pi)=0`. Consider the real even trigonometric polynomial

\[
\boxed{
G_n(\theta)
=
1+\frac4n
-2H_n\!\left(\theta-\frac\pi2\right)
-2H_n\!\left(\theta+\frac\pi2\right).
}
\tag{7}
\]

The `4/n` term restores mean one exactly. Writing

\[
G_n(\theta)=1+2\sum_{m=1}^K\nu_m\cos(m\theta),
\tag{8}
\]

with `nu_m=0` for `m>=n`, one gets explicitly

\[
\boxed{
\nu_m
=-\frac4n
\left(1-\frac mn\right)
\cos\!\left(\frac{m\pi}{2}\right),
\qquad 1\le m<n.
}
\tag{9}
\]

Consequently

\[
\sum_{m=1}^K|\nu_m|=O(1)
\tag{10}
\]

and

\[
\boxed{
\sum_{m=1}^K|\nu_m|^2
\le \frac{C}{n}
\asymp
\frac{(\log a)^2}{a^2}.
}
\tag{11}
\]

Thus `(10)` matches the fixed raw `ell^1` budget used in XF-109, while `(11)` sits exactly at the source `ell^2` dilution scale of XF-110--XF-112. Also `|G_n|=O(1)` uniformly.

The control is PNT-flat around the central angle in the only sense used after XF-109. Indeed, for `|theta|<=theta_a`, with

\[
\theta_a
=\Delta\exp\!\bigl(c_2\sqrt{\log a}\bigr)=o(1),
\tag{12}
\]

the two shifted kernels in `(7)` stay a fixed angular distance from their centers. The elementary bound

\[
H_n(x)
\le
\min\left\{1,\frac{C}{n^2 d(x,2\pi\mathbf Z)^2}\right\}
\tag{13}
\]

therefore gives

\[
\boxed{
\sup_{|\theta|\le\theta_a}|G_n(\theta)-1|=O(1/n)=o(1).
}
\tag{14}
\]

In particular `G_n>=1/2` on the whole XF-109 central arc for large `a`.

Now define the analogue of the XF-112 low-symbol set,

\[
\mathcal C_n
:=
\{\theta:G_n(\theta)\le1/4\}.
\tag{15}
\]

If `theta in C_n`, equation `(7)` implies that at least one of the two shifted `H_n` values is bounded below by a fixed positive constant. By `(13)`, `theta` must then lie within `O(1/n)` of `pi/2` or `-pi/2`. Hence

\[
\boxed{
m(\mathcal C_n)=O(1/n)=O(\varepsilon_a),
}
\tag{16}
\]

exactly matching the vanishing-measure conclusion of XF-112. Conversely, since

\[
H_n(y/n)\longrightarrow
\left(\frac{\sin(y/2)}{y/2}\right)^2
\tag{17}
\]

locally uniformly in fixed `y`, there is a fixed `c_0>0` such that, for all sufficiently large even `n`,

\[
\boxed{
G_n(\theta)\le-\frac12
\quad\text{whenever}\quad
\left|\theta\mp\frac\pi2\right|\le\frac{c_0}{n}.
}
\tag{18}
\]

So a set can be as rare as XF-112 requires while still containing fixed-depth wells much wider than the finite-section resolution `1/K`.

## 2. A real broad witness sees the wells and has negative Rayleigh quotient

Let

\[
E_K
:=
\#\{0\le j\le K:j\ \text{is even}\}
\asymp K
\tag{19}
\]

and define the real unit vector

\[
\boxed{
v_j
=E_K^{-1/2}\cos\!\left(\frac{\pi j}{2}\right),
\qquad 0\le j\le K.
}
\tag{20}
\]

Thus `v_j` vanishes on odd indices and alternates sign on even indices. Its Toeplitz autocorrelations are exact:

\[
r_{2s}
=(-1)^s\left(1-\frac{s}{E_K}\right),
\qquad
r_{2s+1}=0
\tag{21}
\]

whenever the corresponding lag is available. Let `T_K(G_n)` be the real symmetric Toeplitz matrix with diagonal one and off-diagonal moments `(9)`. Since only even lags survive, `(9)` and `(21)` give

\[
\begin{aligned}
v^\top T_K(G_n)v
&=1+2\sum_{m=1}^{n-1}\nu_m r_m\\
&=1-\frac8n
\sum_{s=1}^{n/2-1}
\left(1-\frac{2s}{n}\right)
\left(1-\frac{s}{E_K}\right).
\end{aligned}
\tag{22}
\]

The first factor alone sums to `n/4+O(1)`, while `n/E_K=O(n/K)=o(1)` by `(5)`. Therefore

\[
\boxed{
v^\top T_K(G_n)v
=-1+O\!\left(\frac1n+\frac nK\right)<0
}
\tag{23}
\]

for all sufficiently large `a`.

The witness also passes the geometric restrictions accumulated before XF-112. Its coefficient support has cardinality `E_K asymp K`, much larger than the XF-111 lower scale `a^2/(log a)^2`; its occupied indices span the full q-scale section; and `(21)` has adjacent-lag jumps of order one, so its physical lag roughness is `asymp Delta^{-1} asymp a^3`, far beyond the subexponential lower threshold obtained in XF-108. Its Fourier polynomial is the sum of two normalized Dirichlet packets centered at `+-pi/2`, precisely outside the PNT-flat arc.

Moreover, the standard Dirichlet-kernel tail bound gives, for any fixed `c>0`,

\[
\int_{d(\theta,\{\pm\pi/2\})>c/n}
|P_v(e^{i\theta})|^2\,dm(\theta)
\ll_c \frac nK=o(1).
\tag{24}
\]

Thus this one explicit real vector does not merely put the fixed positive mass required by XF-112 into the rare wells: asymptotically all of its Fourier mass fits inside intervals of total width `O(1/n)=O(\varepsilon_a)`.

Equations `(10)`--`(16)` and `(19)`--`(24)` form the matched-control obstruction. Every current coarse q-scale gate is compatible with a genuinely negative Toeplitz direction.

## 3. The exact finite-section resolution is Fejer scale `1/K`

The previous construction is a concrete falsifier of a proof from measure rarity alone. There is also an exact identity that isolates the right replacement target for the actual Xi symbol.

For any real even symbol

\[
F(\theta)=1+2\sum_{m=1}^K\mu_m\cos(m\theta)
\tag{25}
\]

and any angle `theta_0`, define the complex plane-wave vector

\[
u^{(\theta_0)}_j
=(K+1)^{-1/2}e^{-ij\theta_0}.
\tag{26}
\]

Its Rayleigh quotient is exactly the Fejer mean of the symbol:

\[
\boxed{
(u^{(\theta_0)})^*T_K(F)u^{(\theta_0)}
=
\int_{\mathbb T}
F(\theta)\Phi_K(\theta-\theta_0)\,dm(\theta),
}
\tag{27}
\]

where

\[
\Phi_K(x)
=
\frac1{K+1}
\left|\sum_{j=0}^K e^{ijx}\right|^2
\tag{28}
\]

is the Fejer kernel. The elementary tail estimate

\[
\boxed{
\int_{d(x,0)>w}\Phi_K(x)\,dm(x)
\ll\frac1{Kw}
}
\tag{29}
\]

holds whenever `K^{-1}<<w<=1`.

Suppose, therefore, that the actual Xi symbol `F_a` has a fixed-depth negative well

\[
F_a(\theta)\le-\eta
\qquad
(|\theta-\theta_0|\le w)
\tag{30}
\]

for some fixed `eta>0`, while `|F_a|<=M` globally as in XF-109. Equations `(27)`--`(29)` imply

\[
(u^{(\theta_0)})^*\widehat T_Ku^{(\theta_0)}
\le
-\eta
+O\!\left(\frac{M+\eta}{Kw}\right).
\tag{31}
\]

Hence

\[
\boxed{
Kw\longrightarrow\infty
\quad\Longrightarrow\quad
\widehat T_K\ \text{is nonpositive whenever such a fixed-depth well exists}.
}
\tag{32}
\]

This is only a sufficient condition for failure of positivity; Toeplitz negativity can occur without a single interval well. But `(27)` identifies the finite-section quantity that pointwise or measure-only symbol bounds miss: **the symbol averaged at angular scale `1/K`**.

For the q-scale Xi section,

\[
\frac1K
\asymp
\frac1{a^3\log a},
\tag{33}
\]

whereas XF-112 currently controls the total low-symbol measure only at

\[
\varepsilon_a
\asymp
\frac{(\log a)^2}{a^2}.
\tag{34}
\]

Their ratio is

\[
\boxed{
K\varepsilon_a
\asymp a(\log a)^3\to\infty.
}
\tag{35}
\]

Thus `m(B_a)->0` is far from an uncertainty-scale contradiction. In fact the concentration-operator trace from XF-112 is precisely of order `(K+1)m(B_a)`, and the current bound permits that phase-space capacity to diverge like `a(log a)^3`.

## 4. What this closes and what remains open

The result closes a tempting but invalid continuation of XF-112: one cannot obtain q-scale Toeplitz positivity merely by strengthening the prose interpretation of `m(B_a)=o(1)`, nor by combining that fact with the already-proved broad-support, spike, span, and roughness requirements. The Fejer-well family `(7)`--`(24)` satisfies all of those coarse restrictions at the same asymptotic scales and still has a uniformly negative finite section.

The actual Xi source is much more structured than the control `(7)`, so this does **not** show that `\widehat T_K` is indefinite. It changes the next gate. A useful source-side theorem must now exploit arithmetic structure to prove something such as: fixed-depth negative components have width `O(1/K)` or smaller; the Fejer averages `(27)` stay nonnegative despite pointwise oscillation; or destination-relevant witnesses obey an additional regularity constraint that prevents concentration on Fejer-scale wells. Merely improving the total-measure estimate for `\mathcal B_a` by a constant or logarithm cannot bridge the factor `(35)`.

The classical ingredients used above are the Fejer approximate identity and finite Fourier concentration; a prior-art audit found the expected Toeplitz/Fejer and Slepian concentration literature. No external theorem is load-bearing here: `(6)`--`(35)` are elementary finite-dimensional derivations, and the durable delta is the q-scale matched-control obstruction and the explicit resolution mismatch with XF-112. No `SOURCES.md` update is therefore required.
