# XF-119 — Poisson deconvolution converts q-scale Toeplitz coercivity into exact Xi-budget equal-weight realization

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `POISSON-DECONVOLUTION` + `EXACT-EQUAL-WEIGHT-REALIZATION` + `STATIC-SOURCE-TO-REAL-DIVISOR-BRIDGE`. XF-084 isolates the real-divisor selector bridge as an equal-weight trigonometric moment problem, and XF-085 solves that problem when the target moments already admit a representing density bounded above and below by fixed constants. XF-118 supplies something different and stronger at the actual mass-preserving Xi source: on the full natural q-scale prefix,

\[
\|\widehat T_K-I\|_{\rm op}=o(1).
\tag{1}
\]

The missing step is to turn this **Toeplitz near-isometry** into the regular positive density required by XF-085 without assuming an `ell^1` coefficient margin. That step can be done exactly. Inflate the first `K` moments by a backward Poisson factor `r_K^{-m}` with `r_K=e^{-\gamma/K}`. The inflation is a uniformly bounded Schur multiplier on the finite Toeplitz section, so positivity survives. Represent the inflated moments by an arbitrary positive measure, then convolve that measure forward with the Poisson kernel at radius `r_K`. The forward convolution restores the original first `K` moments exactly. Toeplitz near-isometry forces the intermediate measure to put mass `Theta(K^{-1})` in every arc of length `Theta(K^{-1})`; consequently the Poisson-smoothed density has a uniform positive floor and ceiling. Gilboa--Peled then gives an equal-weight trigonometric quadrature for **every** sufficiently large node count `N>=C K`.

At the XF-118 scale

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\tag{2}
\]

\[
L=\log a+c,
\qquad
K=\left\lfloor\frac L\Delta\right\rfloor
\asymp a^3\log a,
\qquad
N\asymp a^4,
\tag{3}
\]

so

\[
\boxed{
\frac NK\asymp\frac{a}{\log a}\longrightarrow\infty.
}
\tag{4}
\]

Therefore the **prescribed Xi degree `N=2q^2` itself** eventually lies above the exact equal-weight quadrature threshold. The full XF-118 source prefix is not merely inside the weighted Toeplitz moment cone: it has an exact degree-`N` real-divisor moment realization at the Xi node budget. No RH assumption is used.

## 1. Backward Poisson inflation preserves Toeplitz near-isometry

Write the XF-118 normalized moments as

\[
c_0=1,
\qquad
c_m=\widehat\mu_m,
\qquad
c_{-m}=\overline{c_m},
\tag{5}
\]

and

\[
T_K(c):=(c_{i-j})_{0\le i,j\le K}.
\tag{6}
\]

Set

\[
\varepsilon_K:=\|T_K(c)-I\|_{\rm op}=o(1).
\tag{7}
\]

Fix once and for all `gamma>0`, put

\[
r_K:=e^{-\gamma/K},
\tag{8}
\]

and define the backward-Poisson-inflated truncated moments

\[
\widetilde c_0:=1,
\qquad
\widetilde c_m:=r_K^{-m}c_m
=e^{\gamma m/K}c_m,
\qquad 1\le m\le K,
\tag{9}
\]

with `\widetilde c_{-m}=\overline{\widetilde c_m}`.

At first sight `(9)` is dangerous: multiplying moments outward can destroy positive definiteness. The relevant multiplier is nevertheless uniformly bounded at this `1/K` inflation rate. Let

\[
E_K:=T_K(c)-I
\tag{10}
\]

and

\[
A^{(K)}_{ij}:=e^{\gamma|i-j|/K}.
\tag{11}
\]

Because the diagonal of `E_K` is zero,

\[
T_K(\widetilde c)-I=A^{(K)}\circ E_K,
\tag{12}
\]

where `circ` denotes the Schur product.

To bound this multiplier, take

\[
f_\gamma(x):=e^{\gamma|x|},
\qquad -1\le x\le1,
\tag{13}
\]

and extend it `2`-periodically. This periodic function is continuous, piecewise smooth, and has derivative of bounded variation, hence its Fourier coefficients satisfy

\[
|a_n|\ll_\gamma (1+n^2)^{-1},
\qquad
\sum_{n\in\mathbb Z}|a_n|=:C_\gamma<\infty.
\tag{14}
\]

Thus

\[
e^{\gamma|i-j|/K}
=
\sum_{n\in\mathbb Z}
a_n e^{i\pi n i/K}e^{-i\pi n j/K}.
\tag{15}
\]

For each `n`, Schur multiplication by the rank-one phase matrix in `(15)` is just conjugation by a diagonal unitary, so its operator norm is `1`. Therefore

\[
\boxed{
\|A^{(K)}\circ E\|_{\rm op}
\le C_\gamma\|E\|_{\rm op}
}
\tag{16}
\]

for every `(K+1)`-square matrix `E`, uniformly in `K`. Equations `(7)`, `(12)`, and `(16)` give

\[
\boxed{
\|T_K(\widetilde c)-I\|_{\rm op}
\le C_\gamma\varepsilon_K=o(1).
}
\tag{17}
\]

In particular `T_K(\widetilde c)` is positive definite for all sufficiently large `K`.

This `r_K=e^{-\gamma/K}` scale is load-bearing. A fixed backward radius would require factors growing exponentially across the prefix and is not protected by `(16)`. The construction uses only a bounded amount of deconvolution across the entire degree-`K` window.

## 2. The inflated representing measure is locally regular at scale `1/K`

By the finite trigonometric moment theorem used in XF-084, positivity of `T_K(\widetilde c)` supplies a probability measure `sigma_K` on the unit circle with Fourier moments

\[
\widehat\sigma_K(m)=\widetilde c_m,
\qquad |m|\le K.
\tag{18}
\]

No regularity of this representing measure is assumed; it may initially be atomic. Equation `(17)` nevertheless gives a uniform sampling identity. If

\[
P(z)=\sum_{j=0}^{K}v_jz^j,
\tag{19}
\]

then, with normalized Haar measure `dm=dtheta/(2pi)`,

\[
\boxed{
(1-\delta_K)\int|P|^2dm
\le
\int|P|^2d\sigma_K
\le
(1+\delta_K)\int|P|^2dm,
\qquad
\delta_K=o(1).
}
\tag{20}
\]

This forces `sigma_K` to have neither holes nor macroscopic atoms at the resolution relevant to degree `K` polynomials.

For the upper bound, use the normalized Fejer kernel

\[
F_K(t)
:=
\frac1{K+1}
\left|\sum_{j=0}^{K}e^{ijt}\right|^2,
\qquad
\int F_K\,dm=1.
\tag{21}
\]

It is the square modulus of a degree-`K` analytic polynomial, so `(20)` implies uniformly in `x`

\[
\int F_K(x-\theta)\,d\sigma_K(\theta)
=1+o(1).
\tag{22}
\]

For a fixed sufficiently small `rho>0`,

\[
F_K(t)\ge c_\rho K
\qquad
(d_{\mathbb T}(t,0)\le\rho/K),
\tag{23}
\]

hence

\[
\boxed{
\sup_x\sigma_K\!\left(
\left\{\theta:d_{\mathbb T}(\theta,x)\le\rho/K\right\}
\right)
\le\frac{C}{K}.
}
\tag{24}
\]

Covering by finitely many such arcs gives the same `O(K^{-1})` upper bound for every arc of length `O(K^{-1})`, with the constant depending only on the fixed length multiple.

A lower bound requires a more localized positive test. Let

\[
m:=\lfloor K/2\rfloor
\tag{25}
\]

and define

\[
G_K(t)
:=
\frac{F_m(t)^2}{\int F_m^2dm}.
\tag{26}
\]

Because `F_m^2` is the square modulus of the analytic polynomial `D_m^2/(m+1)` of degree `2m<=K`, `(20)` again applies, giving

\[
\int G_K(x-\theta)\,d\sigma_K(\theta)=1+o(1).
\tag{27}
\]

The standard elementary Dirichlet-kernel estimates imply

\[
G_K(t)\le C K,
\qquad
G_K(t)\le
\frac{CK}{1+(K d_{\mathbb T}(t,0))^4}.
\tag{28}
\]

Partition the circle outside a radius `R/K` into arcs of length comparable to `1/K`. Equation `(24)` bounds the `sigma_K` mass of each such arc by `C/K`, while `(28)` makes the contribution of the `j`th arc `O(j^{-4})`. Choosing one fixed large `R` makes the total contribution outside `R/K` smaller than, say, `1/2`. Equation `(27)` then forces a fixed amount of `G_K` mass inside that radius; the first bound in `(28)` yields

\[
\boxed{
\inf_x\sigma_K\!\left(
\left\{\theta:d_{\mathbb T}(\theta,x)\le R/K\right\}
\right)
\ge\frac{c}{K}.
}
\tag{29}
\]

Thus an arbitrary representing measure of the inflated moments is already quantitatively Ahlfors-regular at the only scale needed below:

\[
\boxed{
\sigma_K(I)\asymp K^{-1}
\quad
\text{for every circle arc }I
\text{ of fixed-multiple length }K^{-1}.
}
\tag{30}
\]

The statement is deliberately only at fixed multiples of `1/K`; no pointwise density of `sigma_K` is claimed.

## 3. Forward Poisson smoothing restores the Xi moments exactly and creates a uniform density

Let `P_r` be the Poisson kernel normalized by

\[
\int_{\mathbb T}P_r\,dm=1,
\qquad
\widehat{P_r}(m)=r^{|m|},
\tag{31}
\]

and define the density

\[
W_K(\theta)
:=
\int_{\mathbb T}
P_{r_K}(\theta-\phi)\,d\sigma_K(\phi).
\tag{32}
\]

Then `W_K` is positive, real analytic, and has total mass one. More importantly, `(9)`, `(18)`, and `(31)` give, for every `1<=m<=K`,

\[
\boxed{
\widehat W_K(m)
=r_K^m\widehat\sigma_K(m)
=r_K^m\widetilde c_m
=c_m.
}
\tag{33}
\]

So the forward smoothing has introduced **no moment approximation whatsoever**. The backward inflation and forward Poisson multiplier cancel exactly on the complete XF-118 prefix.

At `r_K=e^{-\gamma/K}`, the Poisson kernel obeys uniformly on the circle

\[
P_{r_K}(t)
\asymp_\gamma
\frac{K}{1+(K d_{\mathbb T}(t,0))^2}.
\tag{34}
\]

The lower mass estimate `(29)` and the lower half of `(34)` on the arc `d_{\mathbb T}(t,0)<=R/K` give

\[
W_K(\theta)
\ge
c_0>0
\tag{35}
\]

uniformly in `theta` and sufficiently large `K`.

For the upper bound, partition the circle into consecutive `1/K`-scale arcs about `theta`. Equation `(24)` puts at most `C/K` mass in each arc, while `(34)` bounds the Poisson kernel on the `j`th pair of arcs by `C_\gamma K/(1+j^2)`. Summing gives

\[
W_K(\theta)
\le
C_0
\sum_{j\ge0}(1+j^2)^{-1}
\le C_1.
\tag{36}
\]

Consequently

\[
\boxed{
0<c_0\le W_K(\theta)\le C_1<\infty
\qquad
\text{for all }\theta,
}
\tag{37}
\]

where `c_0,C_1` depend only on the fixed `gamma` and not on `K`, `q`, or the particular Xi prefix.

This is the regularity bridge that plain Toeplitz positivity does not provide. The output density has the exact desired moments through degree `K` and belongs to one fixed doubling class.

## 4. Uniform doubling regularity gives exactly the prescribed Xi node count

Equation `(37)` makes `W_K` a periodic doubling weight with a doubling constant bounded uniformly in `K`. It also gives

\[
R_{W_K}^{\rm trig}(K)
:=
\frac{\int_{-\pi}^{\pi}W_K(\theta)\,d\theta}
{\inf_x\int_{x-1/K}^{x+1/K}W_K(\theta)\,d\theta}
=O(K).
\tag{38}
\]

Gilboa--Peled's doubling-weight Chebyshev quadrature theorem, already anchored in `SOURCES.md` and used in XF-085, therefore gives one uniform constant `C` such that **every integer**

\[
M\ge CK
\tag{39}
\]

admits `M` equal-weight nodes `theta_1,...,theta_M` satisfying

\[
\frac1M\sum_{j=1}^{M}p(\theta_j)
=
\int_{\mathbb T}p(\theta)W_K(\theta)\,dm(\theta)
\tag{40}
\]

for every trigonometric polynomial of degree at most `K`.

Now take the node count to be the actual Xi degree

\[
M=N=2q^2.
\tag{41}
\]

From `(2)`--`(4)`, `N/K->infinity`, so `(39)` holds for all sufficiently large `q`. Taking `p(theta)=e^{-imtheta}` in `(40)` and using `(33)` gives

\[
\boxed{
\frac1N\sum_{j=1}^{N}e^{-im\theta_j}
=c_m=\widehat\mu_m,
\qquad
1\le m\le K.
}
\tag{42}
\]

Up to the harmless reflection `theta_j -> -theta_j` if the carrier power-sum convention uses `e^{+imtheta}`, `(42)` is exactly the equal-weight unit-circle moment condition of XF-084. Setting `nu_j=e^{i\theta_j}` therefore produces a degree-`N` periodic carrier all of whose roots are real modulo the period and whose normalized power sums match the **entire** mass-preserving XF-118 q-scale source prefix exactly.

Thus the weighted-measure relaxation and the equal-weight degree constraint close together:

\[
\boxed{
\|\widehat T_K-I\|_{\rm op}=o(1),\quad N/K\to\infty
\Longrightarrow
\text{exact degree-}N\text{ real-divisor realization of }\widehat\mu_1,\ldots,\widehat\mu_K.
}
\tag{43}
\]

For the Xi normalization of XF-118, both hypotheses hold unconditionally.

## 5. Adversarial controls: why the extra construction is necessary

Several apparently simpler routes fail or lose the Xi budget.

First, `T_K(c)\succ0` alone only supplies a positive representing measure with arbitrary weights. XF-084 already explains why rounding those weights is not an exact equal-weight theorem. Generic design theorems on path-connected spaces provide existence for sufficiently many equal nodes, but their general quantitative bounds need not be linear in `K`; the Xi budget has `N/K->infinity` but not `N/K^2->infinity`, since

\[
K\asymp a^3\log a,
\qquad
N\asymp a^4.
\tag{44}
\]

The uniform doubling density is therefore doing real work.

Second, directly Poisson-smoothing a representing measure for the original moments would replace `c_m` by `r_K^m c_m` and lose exactness. Equation `(9)` performs the precise backward deconvolution needed to repair that loss. Conversely, taking a fixed `r<1` would require an exponentially growing backward multiplier across `m<=K` and can destroy positivity. The scale `1-r_K\asymp1/K` is the window in which smoothing regularizes the measure while the inverse multiplier remains uniformly bounded on the Toeplitz section.

Third, the representing measure in `(18)` may be highly singular. The floor in `(37)` does not come from assuming a nice Herglotz measure; it is forced by the near-isometry `(20)`. Fejer tests rule out excessive local mass, and the squared-Fejer test plus that upper bound rule out `1/K`-scale holes. This is why the argument needs the full operator statement of XF-118 rather than merely positive definiteness or a lower eigenvalue bounded away from zero with no upper control.

Finally, the argument is stable under complex target moments. Hermitian Toeplitz symmetry gives `c_{-m}=conj(c_m)`, the representing measure is positive, and Poisson convolution produces a real positive density. Equal-weight quadrature then realizes the complex Fourier moments simultaneously. No separate phase-alignment hypothesis is inserted.

These checks identify the precise hypothesis being consumed: **full near-isometry of the q-scale Toeplitz form**, not coefficientwise smallness and not the earlier Gershgorin `ell^1` cone.

## 6. What this closes, and what remains open

XF-118 ended with a static gap: q-scale Toeplitz coercivity did not itself give a finite equal-weight real-divisor carrier at the prescribed Xi degree. Equation `(43)` closes that gap. At every sufficiently large q-scale source slice, the complete moment prefix used by the XF-118 Toeplitz section has an exact `N=2q^2` equal-weight unit-circle realization. At the finite selector interface of XF-079/XF-084, no approximation or weight rounding is needed.

This is **not** a heat-flow existence theorem. The quadrature nodes are constructed independently at one fixed source slice. Nothing here proves that these node multisets can be chosen coherently as functions of heat time, that their zeros obey the required backward/forward heat dynamics, that simplicity is preserved, or that the resulting family carries the positive-transition mass needed at the destination. Those remain downstream dynamical obligations. The finding therefore closes the static source-to-real-divisor moment gate created by XF-084 and sharpened by XF-118; it does not close the Xi-flow program.

A useful next test is now more specific. Since static q-scale realization is no longer the obstruction, one should ask whether the exact quadratures can be selected with enough **inter-scale or heat-time coherence** to feed the guarded selector/endpoint transport machinery. Any future no-go result must exploit that dynamical compatibility rather than static finite Toeplitz feasibility.

## 7. Prior-art and novelty boundary

The finite trigonometric moment theorem, Fejer and Poisson kernels, Fourier-series Schur multipliers, and Chebyshev-type quadrature are classical. Gilboa--Peled prove sharp-order node bounds for Chebyshev-type quadratures of doubling weights; that external theorem is already recorded in `research/xi_flow/SOURCES.md` and was used canonically in XF-085. General equal-weight design existence results, such as Kane's work on path-connected spaces, do not by themselves supply the linear-in-`K` prescribed-node threshold needed here.

A targeted prior-art search for Toeplitz-near-identity moment data, Poisson regularization/deconvolution, and equal-weight trigonometric quadrature found the classical ingredients separately, but not this specific chain applied to the XF-118 source: **backward `1/K` Poisson inflation -> positive truncated moment representation -> Fejer-forced `1/K` local regularity -> forward Poisson smoothing with exact moment restoration -> uniform doubling class -> exact prescribed Xi-budget quadrature**. No claim of absolute novelty is made beyond that line-local synthesis.

Because every external load-bearing theorem used here is already anchored in `SOURCES.md`, no bibliography update is required in this pass.
