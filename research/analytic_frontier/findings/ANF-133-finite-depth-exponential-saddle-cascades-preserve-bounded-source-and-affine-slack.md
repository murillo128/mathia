# ANF-133 — finite-depth exponential saddle cascades preserve bounded source and affine slack

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-OBSTRUCTION + POSITIVE-TRANSLATION-CASCADE + CRITICAL-RENORMALIZATION + FIXED-DEPTH`. `ANF-129` constructs a critical exponential positive translation cloud that evacuates the original `ANF-115` saddle without source blowup. `ANF-130` shows that every finite critical source skeleton has a finite positive translation annihilator, while `ANF-132` proves that repeating such an annihilator only `o(A)` times cannot suppress a genuinely exponential oversource. The remaining same-profile question is whether the required positive-rate repetition `m=Theta(A)` necessarily destroys the source-heavy normalization or consumes the affine/cardinality slack.

It does neither. A finite positive annihilator can be repeated at a uniquely selected first positive density until the modified exponential pressure returns exactly to zero. The old critical chambers are then superexponentially evacuated, a new finite nondegenerate critical skeleton appears elsewhere, the total source remains comparable to the original `ANF-115` source, and the logarithmic copy-count rate stays below the universal barrier `f_gamma/2`. The construction can therefore be iterated to **arbitrarily large but fixed finite depth**. At every fixed depth the source remains bounded/macroscopic, some fixed central notch remains exponentially dark, and the packet cardinality stays exponentially negligible relative to the source-heavy affine normalization.

The conclusion is deliberately not depth-uniform. It does not construct a fatal near-extremizer and does not settle a cascade with depth `d=d(A)->infinity`. The new frontier is precisely whether the successive critical skeletons, notch widths, translation spans, and chamber counts can be controlled uniformly enough to pass from arbitrary fixed depth to a depth growing with scale.

## 1. Critical positive translation landscapes have a universal half-`f_gamma` copy-rate ceiling

Fix `gamma>0` and the `ANF-115` base packet `P_A^(gamma)`. On the positive source half-band `0<=alpha<1`, write

\[
F_\gamma(\alpha)
=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2},
\qquad
f_\gamma=\max_{0\le\alpha<1}F_\gamma(\alpha)>0.
\tag{1}
\]

Recall the two endpoint facts

\[
F_\gamma(0)=0,
\qquad
F_\gamma'(0)=1.
\tag{2}
\]

Consider a fixed finite-depth positive translation cascade whose modulation is

\[
M_A(\alpha)
=\prod_{\ell=1}^s
P_\ell(\alpha)^{\lfloor r_\ell A\rfloor},
\tag{3}
\]

where every factor is a finite positive integer-coefficient translation polynomial

\[
P_\ell(\alpha)
=\sum_{\nu}a_{\ell,\nu}e^{-2\pi i\tau_{\ell,\nu}\alpha},
\qquad
a_{\ell,\nu}\in\mathbb N,
\tag{4}
\]

and

\[
V_\ell:=P_\ell(0)=\sum_\nu a_{\ell,\nu}>1.
\tag{5}
\]

Thus `(3)` is a genuine positive translation multiset: each repetition replaces every current copy by `V_ell` translated copies. Put

\[
R:=\sum_{\ell=1}^s r_\ell\log V_\ell
\tag{6}
\]

for its logarithmic copy-count rate. Relative to the base source exponential scale, the limiting positive-frequency exponent is

\[
G(\alpha)
:=F_\gamma(\alpha)-f_\gamma
+2\sum_{\ell=1}^s r_\ell\log|P_\ell(\alpha)|.
\tag{7}
\]

Assume the current block is source-critical,

\[
\boxed{\sup_{0\le\alpha<1}G(\alpha)=0,}
\tag{8}
\]

and that its maximizer set is finite, interior, and nondegenerate. This is exactly the regime produced by `ANF-129`; below we show that the property is preserved by the new renormalization step.

Positivity gives a useful invariant at the origin. Since `P_ell(0)>0` is real while

\[
P_\ell'(0)
=-2\pi i\sum_\nu a_{\ell,\nu}\tau_{\ell,\nu}
\]

is purely imaginary,

\[
\frac{d}{d\alpha}\log|P_\ell(\alpha)|\Big|_{\alpha=0}=0.
\tag{9}
\]

Consequently

\[
G(0)=-f_\gamma+2R,
\qquad
G'_+(0)=1.
\tag{10}
\]

If `G(0)=0`, the positive right derivative would force `G(alpha)>0` for all sufficiently small positive `alpha`, contradicting `(8)`. Since `(8)` also gives `G(0)<=0`, every source-critical positive cascade satisfies the strict universal ceiling

\[
\boxed{R<\frac{f_\gamma}{2}.}
\tag{11}
\]

This ceiling immediately controls the physical cardinality. The `ANF-115` base packet has

\[
|P_A^{(\gamma)}|
=\exp\!\left(\gamma\log2\,A+o(A)\right),
\tag{12}
\]

while its source satisfies

\[
E_A:=E_0(P_A^{(\gamma)})
=\exp\!\left((2\gamma\log2+f_\gamma)A+o(A)\right).
\tag{13}
\]

After the cascade, counting translation multiplicity,

\[
|X_A|
=\exp\!\left((\gamma\log2+R)A+o(A)\right).
\tag{14}
\]

Hence

\[
\boxed{
\limsup_{A\to\infty}
\frac1A\log\frac{|X_A|}{E_A}
=R-\gamma\log2-f_\gamma
<-\gamma\log2-\frac{f_\gamma}{2}<0.
}
\tag{15}
\]

Thus source criticality itself leaves a **uniform exponential cardinality margin**, independent of the finite cascade depth. A same-profile positive cascade cannot consume that margin while remaining source-critical.

## 2. A finite critical skeleton can be annihilated and retuned exactly back to criticality

Let the current source-critical landscape have finite nondegenerate maximizer set

\[
K=\{\xi_1,\ldots,\xi_J\}\subset(0,1).
\tag{16}
\]

Following `ANF-130`, define the positive binomial annihilator

\[
Q_K(\alpha)
:=\prod_{j=1}^J
\left(1+e^{-2\pi i\tau_j\alpha}\right),
\qquad
\tau_j:=\frac1{2\xi_j}.
\tag{17}
\]

Then

\[
Q_K(\xi_j)=0
\quad(1\le j\le J),
\qquad
Q_K(0)=2^J.
\tag{18}
\]

For a repetition density `theta>=0`, introduce the modified pressure landscape

\[
G_\theta(\alpha)
:=G(\alpha)+2\theta\log|Q_K(\alpha)|
\tag{19}
\]

and its pressure

\[
M(\theta)
:=\sup_{0\le\alpha<1}G_\theta(\alpha).
\tag{20}
\]

At `theta=0`, `M(0)=0`. For every sufficiently small positive `theta`, however,

\[
\boxed{M(\theta)<0.}
\tag{21}
\]

Indeed, near an old nondegenerate maximum `xi_j`, for some `c>0`,

\[
G(\xi_j+x)\le-cx^2.
\tag{22}
\]

If the zero of `Q_K` there has order `k_j>=1`, then locally

\[
\log|Q_K(\xi_j+x)|
\le C+k_j\log|x|.
\tag{23}
\]

The best value of the resulting local upper bound obeys

\[
\sup_x
\left[-cx^2+2\theta k_j\log|x|+O(\theta)\right]
=k_j\theta\log\theta+O(\theta)<0
\tag{24}
\]

for sufficiently small `theta`. Away from fixed neighborhoods of the old maxima, `G` already has a fixed negative gap, while `log|Q_K|<=J log 2`; hence `(21)` holds globally. This is the quantitative version of the finite-skeleton excision mechanism from `ANF-130`.

The pressure cannot remain negative forever. Define the origin-saturation density

\[
\theta_0
:=\frac{f_\gamma-2R}{2J\log2}>0,
\tag{25}
\]

where positivity follows from `(11)`. At that density,

\[
G_{\theta_0}(0)
=-f_\gamma+2R+2\theta_0J\log2
=0.
\tag{26}
\]

But every positive translation factor again has zero logarithmic-modulus derivative at the origin, so

\[
(G_{\theta_0})'_+(0)=1.
\tag{27}
\]

Therefore `G_{theta_0}(alpha)>0` for sufficiently small positive `alpha`, and

\[
M(\theta_0)>0.
\tag{28}
\]

The function `M` is convex as a supremum of affine functions of `theta`, and it is finite and continuous for `theta>0`. Combining `(21)` and `(28)`, define the first positive critical density

\[
\boxed{
\theta_*
:=\inf\{\theta>0:M(\theta)\ge0\}.
}
\tag{29}
\]

Then

\[
0<\theta_*<\theta_0,
\qquad
\boxed{M(\theta_*)=0.}
\tag{30}
\]

Thus a positive-rate annihilator layer can be tuned **exactly** back to source criticality after it has destroyed the previous critical skeleton.

Its new copy-count rate is

\[
R_*=R+\theta_*J\log2,
\tag{31}
\]

so `(25)` and `(30)` give

\[
\boxed{R_*<\frac{f_\gamma}{2}.}
\tag{32}
\]

The invariant `(11)` is therefore preserved by the renormalization step.

## 3. The old saddle chambers are superexponentially killed while a new finite skeleton carries the source

The critical density in `(29)` is implemented physically by

\[
m_A:=\lfloor\theta_*A\rfloor
\tag{33}
\]

repetitions of the finite positive translation cloud `(17)`. Its multiplicity factor is exactly

\[
2^{Jm_A}
=\exp\!\left(\theta_*J\log2\,A+O(1)\right).
\tag{34}
\]

At any old critical point `xi_j`, the new layer is much stronger than an ordinary exponential penalty. Let

\[
|\alpha-\xi_j|\le\frac{S_A}{\sqrt A},
\qquad
S_A\to\infty,
\qquad
S_A=A^{o(1)}.
\tag{35}
\]

Using the order-`k_j` zero of `Q_K`,

\[
|Q_K(\alpha)|^{2m_A}
\le
\exp\!\left[-\theta_*k_jA\log A+o(A\log A)\right].
\tag{36}
\]

Hence the entire Gaussian chamber that formerly carried the source is **superexponentially evacuated**. Any later fixed number of positive-rate finite layers can amplify a chamber by at most `exp(O(A))`; they cannot resurrect the `exp[-cA log A]` loss in `(36)`.

Where does the source go? The new critical landscape `G_{theta_*}` has supremum zero, while `(18)` excludes every old `xi_j` from its maximizer set. It also cannot maximize at the origin because `theta_*<theta_0` gives

\[
G_{\theta_*}(0)<0.
\tag{37}
\]

Nor can a maximum escape through `alpha=1`: the `ANF-115` factor `F_gamma(alpha)` tends to `-infinity` there, while every finite translation factor is bounded above. Thus the new maxima lie in the interior.

For the concrete cascade generated by `ANF-129` and the binomial layers `(17)`, the exponent is piecewise strictly concave between the finitely many zeros of its factors. The base curvature is

\[
F_\gamma''(\alpha)
=-\frac{\gamma\pi^2}{2}
\sec^2\frac{\pi\alpha}{2}<0.
\tag{38}
\]

The digit factors satisfy, on zero-free cells,

\[
\frac{d^2}{dx^2}\log|D_q(x)|
=-\pi^2q^2\csc^2(\pi qx)
+\pi^2\csc^2(\pi x)<0,
\tag{39}
\]

using `|sin(qy)|<q|sin y|` away from the common zero set. Each binomial annihilator factor has

\[
\log|1+e^{-2\pi i\tau\alpha}|
=\log2+\log|\cos(\pi\tau\alpha)|,
\tag{40}
\]

whose second derivative is strictly negative wherever finite. There is therefore at most one maximizer in each zero-free cell, and every maximizer is nondegenerate. The new critical skeleton is again finite.

Standard one-dimensional Laplace localization around those finitely many nondegenerate maxima gives, at fixed cascade depth,

\[
\boxed{E_0(X_A^*)\asymp E_A.}
\tag{41}
\]

The floor in `(33)` changes the multiplier at a new maximizer by only a bounded factor because `Q_K` is nonzero there, so it does not change `(41)`. Since `(37)` is strict and the exponent is continuous near zero, there also exist constants depending on the new layer,

\[
\eta_*>0,
\qquad c_*>0,
\tag{42}
\]

such that

\[
\boxed{
\sup_{0\le\alpha\le\eta_*}
G_{\theta_*}(\alpha)
\le-c_*.
}
\tag{43}
\]

Thus some fixed central notch remains exponentially dark after critical retuning. The width `eta_*` is not claimed to equal, or be uniformly comparable to, the notch from the preceding layer.

## 4. Arbitrarily deep fixed cascades remain physical, source-critical, and cardinality-negligible

Start from the source-critical `ANF-129` digit cloud. Its critical source skeleton is finite and nondegenerate, so the construction above applies. The output again has a finite nondegenerate critical skeleton, satisfies the copy-rate invariant `(32)`, and has a fixed dark central neighborhood `(43)`. It can therefore be fed back into exactly the same construction.

Inductively, for every integer depth `d>=1` fixed before taking `A->infinity`, one obtains a same-profile positive translation cascade `X_A^(d)` with the following simultaneous properties:

\[
E_0(X_A^{(d)})\asymp E_A,
\tag{44}
\]

\[
R_d<\frac{f_\gamma}{2},
\tag{45}
\]

and hence

\[
\limsup_{A\to\infty}
\frac1A\log\frac{|X_A^{(d)}|}{E_A}
<-\gamma\log2-\frac{f_\gamma}{2}<0.
\tag{46}
\]

Every critical skeleton from the earlier layers is superexponentially suppressed by the first later annihilator that targets it, while the current source is carried by a new finite set of nondegenerate chambers. For each fixed `d` there also exists a fixed `eta_d>0` for which the central notch `0<=|alpha|<=eta_d` carries exponentially negligible source mass.

The construction remains a genuine finite physical multiset. At fixed depth, the translations introduced in one repeated layer have total horizontal extent

\[
O_d(A),
\tag{47}
\]

because the finite shifts `tau_j` are independent of `A` within that layer and are repeated `Theta(A)` times. The constant in `(47)` is allowed to depend on depth. No distinctness assertion is needed: positive integer multiplicity is part of the multiset realization.

This gives the precise answer to the entropy barrier of `ANF-132`. The estimate there is sharp about the required scale: `m=o(A)` cannot beat an exponential source reservoir, but `m=Theta(A)` can. More importantly, the positive-rate layer need not leave an exponentially oversized remainder. Its density can be pressure-tuned so that the newly generated chambers have exactly the original source scale `(44)`. The cascade does not run out of cardinality slack either, because the half-`f_gamma` ceiling `(11)` survives every fixed renormalization step.

## 5. What this does not close, and the new gate

This is not yet a fatal near-extremizer construction. Every **finite-depth** output again has only finitely many critical source chambers, so `ANF-130` supplies another finite positive annihilator. The result shows that adding that annihilator at the positive density forced by `ANF-132` can regenerate a bounded critical source elsewhere; it does not show that the resulting block is non-excisable from a complete near-extremizer.

More importantly, all asymptotics above are fixed-depth statements. Nothing here controls a diagonal regime

\[
d=d(A)\longrightarrow\infty.
\tag{48}
\]

The number of critical chambers, the annihilator shifts

\[
\tau_j=\frac1{2\xi_j},
\tag{49}
\]

the constants in the Laplace estimates, and the fixed dark-notch widths `eta_d` may deteriorate rapidly with `d`. In particular, `(43)` proves only the existence of **some** positive fixed notch at each fixed depth. It does not preserve an arbitrary preassigned notch and does not provide a positive lower bound on `eta_d` as `d->infinity`.

Therefore `CLUE-near-extremizer-notch-exposure-envelope.md` remains open. The next same-profile gate is now depth-uniform: determine whether the renormalization can be controlled for `d(A)->infinity`, or whether chamber proliferation, collapse of `eta_d`, or growth of the translation span forces eventual exposure/excisability. A transverse/macroscopic source mechanism remains the other natural escape if the same-profile cascade cannot be made depth-uniform.

A directed prior-art audit found only the general analogies one would expect from Riesz-product constructions, repeated trigonometric-polynomial powers, and Laplace/pressure principles. None supplies the Mathia-specific combination used here: positive physical translation realization, saddle annihilation, source-critical pressure retuning, and the half-`f_gamma` copy-rate invariant. No external theorem is load-bearing for the argument, so this finding introduces no new `SOURCES.md` dependency.

**Bottom line.** The `ANF-132` Gaussian entropy barrier is a threshold, not a terminal obstruction. Once a positive-rate second layer is allowed, the same-profile construction can evacuate the current critical saddle set, regenerate source at a new finite skeleton, retain a dark central notch, and preserve exponential affine/cardinality slack. This can be repeated to every fixed finite depth. The unresolved question has moved from *whether* the exponential cascade can continue to whether it can be controlled **uniformly as the depth itself grows with `A`**.