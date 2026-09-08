# XF-112 — nonpositive q-scale Toeplitz witnesses concentrate on a vanishing symbol sublevel set

**Status:** `EXACT-DERIVED` + `SYMBOL-SUBLEVEL-CONCENTRATION` + `PHASE-SPACE-BOTTLENECK` + `TOEPLITZ-FEASIBILITY-BOUNDARY`. XF-109 showed that every nonpositive q-scale source-Toeplitz witness must place fixed coefficient-Fourier mass outside the PNT-flat central arc. XF-110 and XF-111 separately showed that the nonpositive spectrum is thin and that every nonpositive Rayleigh witness needs almost `q` coefficient coordinates. These restrictions can be unified and sharpened: **all** nonpositive witnesses must place a fixed amount of Fourier energy on the same source-determined low-symbol set, while that set itself has normalized angular measure `O((log q)^2/q)` and is disjoint from the PNT-flat arc. Thus the surviving obstruction is not merely a dense rough witness; it is a finite-dimensional concentration phenomenon on a vanishing set of arithmetic symbol angles.

Keep the fixed-q-scale mass-preserving source interface of XF-108--XF-111,

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

with

\[
L=\log a+c,
\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor,
\qquad c\in\mathbf R
\tag{2}
\]

fixed independently of `a`. Let

\[
\widehat T_K=(\widehat\mu_{i-j})_{0\le i,j\le K},
\qquad
F_a(\theta)
=
1+2\sum_{m=1}^K\widehat\mu_m\cos(m\theta),
\tag{3}
\]

and write normalized Haar measure on the circle as

\[
dm(\theta)=\frac{d\theta}{2\pi}.
\]

The source estimates already established in XF-109--XF-111 give

\[
S_2(a):=\sum_{m=1}^K|\widehat\mu_m|^2
\ll_{\psi,c}\frac{(\log a)^2}{a^2},
\tag{4}
\]

and a fixed constant `M=M(\psi,c)<\infty` such that

\[
F_a(\theta)\ge -M
\qquad(-\pi\le\theta\le\pi).
\tag{5}
\]

Moreover, for some `c_2>0`, if

\[
\theta_a
=
\Delta\exp\!\bigl(c_2\sqrt{\log a}\bigr),
\tag{6}
\]

then XF-109 gives, for all sufficiently large `a`,

\[
F_a(\theta)\ge\frac12
\qquad (|\theta|\le\theta_a).
\tag{7}
\]

Define the fixed low-symbol set

\[
\boxed{
\mathcal B_a
=
\{\theta\in[-\pi,\pi]:F_a(\theta)\le\tfrac14\}.
}
\tag{8}
\]

Then

\[
\boxed{
m(\mathcal B_a)
\le
\frac{32}{9}S_2(a)
\ll_{\psi,c}
\frac{(\log a)^2}{a^2}
\asymp
\frac{(\log q)^2}{q}.
}
\tag{9}
\]

For a unit vector `v in C^{K+1}`, put

\[
P_v(e^{i\theta})
=
\sum_{j=0}^K v_j e^{ij\theta}.
\tag{10}
\]

Every nonpositive Rayleigh witness satisfies the common concentration bound

\[
\boxed{
v^*\widehat T_Kv\le0
\quad\Longrightarrow\quad
\int_{\mathcal B_a}|P_v(e^{i\theta})|^2\,dm(\theta)
\ge
\delta_*:=\frac1{4M+1}.
}
\tag{11}
\]

At the same time `(7)` implies

\[
\boxed{
\mathcal B_a\cap\{|\theta|\le\theta_a\}=\varnothing.
}
\tag{12}
\]

Thus a fixed fraction of every nonpositive witness must fit inside a set whose relative angular measure tends to zero like at most `(log q)^2/q`, and that set lies entirely beyond the PNT-flat physical-frequency window.

## 1. Source `ell^2` dilution makes low-symbol angles rare

Parseval applied directly to the trigonometric symbol `(3)` gives the exact identity

\[
\int_{-\pi}^{\pi}|F_a(\theta)-1|^2\,dm(\theta)
=
2\sum_{m=1}^K|\widehat\mu_m|^2
=
2S_2(a).
\tag{13}
\]

On `\mathcal B_a`, one has `F_a<=1/4`, hence

\[
|F_a-1|\ge\frac34.
\tag{14}
\]

Chebyshev's inequality in `(13)` therefore yields

\[
\frac9{16}m(\mathcal B_a)
\le
2S_2(a),
\tag{15}
\]

which is exactly `(9)`. This step uses no Toeplitz eigenvalue asymptotics: it is a finite-scale statement about the actual q-scale Xi source symbol.

The threshold `1/4` is not canonical. Any fixed level strictly below the positive central-arc floor in `(7)` gives the same `O(S_2)` measure conclusion with different constants. The choice `1/4` leaves a uniform positive floor on the complement and makes the next step transparent.

## 2. Nonpositive Rayleigh quotients must concentrate on the same rare set

Parseval also gives

\[
\int_{-\pi}^{\pi}|P_v(e^{i\theta})|^2\,dm(\theta)=1,
\tag{16}
\]

and the exact Toeplitz-symbol identity is

\[
\boxed{
v^*\widehat T_Kv
=
\int_{-\pi}^{\pi}
F_a(\theta)|P_v(e^{i\theta})|^2\,dm(\theta).
}
\tag{17}
\]

Write

\[
p_a(v)
=
\int_{\mathcal B_a}|P_v|^2\,dm.
\tag{18}
\]

On `\mathcal B_a^c`, definition `(8)` gives `F_a>1/4`; globally `(5)` gives `F_a>=-M`. Hence `(16)`--`(18)` imply

\[
\begin{aligned}
v^*\widehat T_Kv
&\ge
\frac14\bigl(1-p_a(v)\bigr)-Mp_a(v)\\
&=
\frac14-\left(M+\frac14\right)p_a(v).
\end{aligned}
\tag{19}
\]

If the Rayleigh quotient is nonpositive, `(19)` forces

\[
p_a(v)
\ge
\frac1{4M+1},
\tag{20}
\]

proving `(11)`. In particular, if `\mathcal B_a` were empty then `\widehat T_K` would already be positive definite. More generally, negativity cannot be produced by a witness that merely has some unspecified high-frequency roughness: the witness must concentrate a uniform amount of energy on the **same** low-symbol set fixed by the Xi source.

Combining `(9)` and `(11)` also forces a Fourier spike. Since

\[
p_a(v)
\le
m(\mathcal B_a)\|P_v\|_{L^\infty(\mathbb T)}^2,
\tag{21}
\]

any nonpositive witness obeys

\[
\boxed{
\|P_v\|_{L^\infty(\mathbb T)}^2
\gg_{\psi,c}
\frac1{S_2(a)}
\gg_{\psi,c}
\frac{a^2}{(\log a)^2}.
}
\tag{22}
\]

Because the mass in `(11)` lies on `\mathcal B_a`, `(12)` shows that such a spike must occur outside the PNT-flat central arc. In q-variables its amplitude is at least of order `q^{1/2}/log q`, up to fixed source constants.

## 3. The XF-110 and XF-111 restrictions become phase-space consequences

If `s=|supp v|`, then Cauchy--Schwarz gives

\[
\|P_v\|_\infty
\le
\|v\|_1
\le
\sqrt{s}\|v\|_2
=
\sqrt{s}.
\tag{23}
\]

Thus `(22)` immediately recovers the almost-q support obstruction

\[
\boxed{
v^*\widehat T_Kv\le0
\quad\Longrightarrow\quad
|supp v|
\gg_{\psi,c}
\frac{a^2}{(\log a)^2}
\asymp
\frac{q}{(\log q)^2},
}
\tag{24}
\]

now as a consequence of concentration on `\mathcal B_a`. XF-111 obtained the same scale directly from restricted Hilbert--Schmidt control; the two proofs expose different geometry.

There is also a common-subspace version. Let `C_{\mathcal B_a}` be the finite Fourier concentration operator on coefficient space, defined by

\[
\langle v,C_{\mathcal B_a}v\rangle
=
\int_{\mathcal B_a}|P_v|^2\,dm.
\tag{25}
\]

It is positive semidefinite and has

\[
\operatorname{tr}C_{\mathcal B_a}
=(K+1)m(\mathcal B_a).
\tag{26}
\]

Let `P_-` denote the spectral projector of `\widehat T_K` onto its nonpositive eigenspace and `n_-=\operatorname{rank}P_-`. Every unit vector in `ran P_-` has nonpositive Rayleigh quotient, so `(11)` is equivalent to the operator inequality

\[
P_-C_{\mathcal B_a}P_-
\succeq
\delta_*P_-.
\tag{27}
\]

Taking traces and using `0<=P_-<=I` gives

\[
\delta_*n_-
\le
\operatorname{tr}(C_{\mathcal B_a}P_-)
\le
\operatorname{tr}C_{\mathcal B_a}.
\tag{28}
\]

Therefore

\[
\boxed{
n_-
\le
\delta_*^{-1}(K+1)m(\mathcal B_a)
\ll_{\psi,c}
(K+1)S_2(a)
\ll_{\psi,c}
a(\log a)^3,
}
\tag{29}
\]

since `K+1\asymp a^3\log a`. This recovers the XF-110 bad-rank scale from the phase-space capacity of the same rare set that forces `(24)`. The rank thinness and coefficient broadness are therefore not independent accidents: both are compatible with a single concentration bottleneck.

## 4. Stress tests and exact boundary

The result is only a necessary condition for source-Toeplitz indefiniteness. A nonempty `\mathcal B_a`, or even a region where `F_a<0`, does not by itself guarantee that the finite section `\widehat T_K` has a nonpositive eigenvalue. Conversely, if `\mathcal B_a` is empty then `(19)` gives an immediate uniform positive lower bound. No asymptotic Szego theorem is being used to replace this finite-section distinction.

The fixed offset `c` in `L=log a+c` is load-bearing through the global lower bound `(5)`. If one moves to `L=log a+c(a)` with `c(a)->+infinity`, XF-109's raw `ell^1` source budget can grow, `M` need not stay fixed, and the concentration fraction `delta_*=1/(4M+1)` may collapse. The sublevel-measure estimate `(9)` still follows from whatever `S_2` bound is available, but `(11)` must then be recomputed with the actual lower bound for the symbol.

The argument also remains at the weighted Toeplitz/Caratheodory relaxation isolated in XF-084. It does not prove exact equal-weight realization, and it does not convert source feasibility into an upper bound for the de Bruijn--Newman constant. No RH assumption enters.

## 5. Prior-art audit and consequence for the live frontier

The broad operator language is classical. Szego-type theory relates the spectral distribution of large selfadjoint Toeplitz sections to the distribution of their real symbol; refinements for band Toeplitz matrices explicitly count eigenvalues through symbol preimages. Separately, the Slepian--Landau--Pollak concentration theory and its discrete prolate version study how much Fourier energy a finite coefficient vector can place inside a prescribed small frequency set. No novelty is claimed for Parseval, Chebyshev, the finite Fourier concentration operator, its trace, or the general phase-space interpretation.

Those classical theories do not supply the statement above for the present source without the Xi-specific estimates already proved in XF-108--XF-111. Here the symbol itself varies with the q-scale, the explicit-formula source gives the quantitative dilution `S_2(a)<< (log a)^2/a^2`, PNT creates the disjoint central positive arc, and the fixed raw source budget supplies the uniform floor `-M`. The durable delta is the resulting common-set theorem `(9)`--`(12)` at the Xi arithmetic scale. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The source-side frontier is therefore narrower than the generic "dense rough sector" left after XF-111. A surviving nonpositive certificate must simultaneously use almost `q` coefficient coordinates and place a fixed fraction of its Fourier energy on a **source-determined set of relative measure at most `O((log q)^2/q)`**, entirely outside the growing PNT-flat window. The next useful source-side attack is no longer to search arbitrary dense witnesses. It is to control the geometry and depth of `\mathcal B_a`, or to prove an Xi-specific anti-concentration statement showing that the destination-relevant witness class cannot put fixed mass on such a vanishing arithmetic set.
