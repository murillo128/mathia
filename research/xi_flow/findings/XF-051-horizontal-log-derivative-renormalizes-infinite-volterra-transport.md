# XF-051 — horizontal logarithmic derivative renormalizes the infinite Volterra transport

**Status:** `LITERATURE+DERIVED` + `EXACT-DERIVED` + `INFINITE-DISTRIBUTIONAL-TRANSPORT` + `SOURCE-SPECIFIC-BOUNDARY`. XF-050 removes the finite-dimensional reality/collision/localization obstruction but leaves the raw infinite zero sum and its divergent zero-frequency background as the apparent transport barrier. That barrier can be split more sharply.

For the actual de Bruijn--Newman family there is a canonical infinite positive-frequency carrier that never requires the raw sum

\[
\sum_\rho e^{-i\xi x_\rho}
\]

as an ordinary function. Fix any `a>1` and put

\[
q(z,t):=\frac{\partial_z H_t(z)}{H_t(z)},
\qquad
Q_a(x,t):=q(x+ia,t).
\tag{1}
\]

The classical de Bruijn strip theorem, started from the unconditional critical strip at `t=0`, keeps every zero of `H_t` below the horizontal line `Im z=a` for every `t>=0`. Thus `Q_a` is a smooth tempered boundary value of a holomorphic function in the upper half-plane. Since

\[
\partial_t H_t=-\partial_z^2H_t,
\]

its logarithmic derivative satisfies the exact complex Burgers equation

\[
\boxed{
\partial_t Q_a
=-\partial_x^2Q_a-\partial_x(Q_a^2).
}
\tag{2}
\]

With the Fourier convention

\[
\widehat F(\xi)=\int_{\mathbb R}F(x)e^{-i\xi x}\,dx,
\tag{3}
\]

the half-plane Paley--Wiener support theorem gives

\[
\boxed{
\operatorname{supp}\widehat Q_a(\cdot,t)\subset[0,\infty).
}
\tag{4}
\]

Consequently (2) has the exact tempered-distribution Fourier form

\[
\boxed{
\partial_t\widehat Q_a(\xi,t)
=
\xi^2\widehat Q_a(\xi,t)
-
\frac{i\xi}{2\pi}
(\widehat Q_a*\widehat Q_a)(\xi,t).
}
\tag{5}
\]

The convolution is well-defined because both factors are supported in the proper cone `[0,infinity)`. In particular, on positive frequencies the nonlinear term is Volterra-triangular: a test localized at frequency `xi>0` can receive nonlinear input only from frequencies between `0` and `xi`. This is an **exact infinite Xi-flow statement**, valid through complex zeros and collisions because it is an identity for the entire function rather than for labelled zero trajectories.

After removing the harmless vertical-line factor, (5) is exactly the XF-049/XF-050 finite zero-sum law. Define on the open positive half-line

\[
\boxed{
\mathcal Z_t(\xi)
:=
\frac{i}{2\pi}e^{a\xi}\widehat Q_a(\xi,t),
\qquad \xi>0.
}
\tag{6}
\]

This distribution is independent of the choice of `a>1`, agrees with `Z_N(\xi)=\sum_j e^{-i\xi x_j}` for finite polynomial controls, and obeys

\[
\boxed{
\partial_t\mathcal Z_t(\xi)
=
\xi^2\mathcal Z_t(\xi)
-
\xi\int_0^\xi
\mathcal Z_t(\eta)\mathcal Z_t(\xi-\eta)\,d\eta
}
\tag{7}
\]

in the distributional Volterra sense. Equation (7) does **not** make the singular endpoint `xi=0` innocuous and does not by itself propagate the XF-050 order-one margin. What it does remove is the structural infinite-volume question: the one-sided carrier and its nonlinear evolution exist canonically before any quantitative subtraction of the archimedean background.

## 1. A fixed zero-free horizontal line exists unconditionally for `t>=0`

At the endpoint, a nontrivial zeta zero `rho=beta+i gamma` corresponds in the XF-050 coordinate to

\[
x_\rho=-2i(\rho-\tfrac12)
=2\gamma-2i(\beta-\tfrac12).
\tag{8}
\]

The classical critical strip `0<beta<1` therefore gives

\[
|\operatorname{Im}x_\rho|<1.
\tag{9}
\]

De Bruijn's strip-shrinking theorem says that if the zeros at time `t_0` lie in `|Im z|<=y_0`, then at later time `t>t_0` they lie in

\[
|\operatorname{Im}z|
\le
\sqrt{\max\{y_0^2-2(t-t_0),0\}}.
\tag{10}
\]

Taking `t_0=0` and `y_0=1` shows that every zero of `H_t` lies below any fixed line `Im z=a>1` for all `t>=0`; for `t>=1/2` the same theorem gives real zeros. No RH assumption and no real-simple interval are used here.

The classical order-one Hadamard factorization of `H_t` also gives enough growth control for the boundary-value argument. Pairing zeros under `z -> -z`, one may write the logarithmic derivative as a locally normally convergent paired sum

\[
q(z,t)
=
\sum_j\frac{2z}{z^2-x_j(t)^2},
\tag{11}
\]

with the usual multiplicities and symmetric interpretation. The fixed distance `a-1` from the zero strip and the standard zero count `N_t(R)=O(R\log R)` give the coarse bound

\[
Q_a(x,t)=O_{a,I}\!\bigl((1+|x|)\log(2+|x|)\bigr)
\tag{12}
\]

uniformly for `t` in a compact interval `I subset [0,infinity)`. Indeed, roots of modulus at most `2|x|+O(1)` contribute at most their count times the fixed inverse distance, while the paired tail is bounded using `2z/(z^2-x_j^2)=O(|z|/|x_j|^2)` and `sum |x_j|^{-2}<infinity`. Thus `Q_a` and its needed derivatives are tempered distributions in `x`.

## 2. Burgers evolution is regular even when the zero coordinates are not

From `partial_t H_t=-H_{zz}` and

\[
\frac{H_{zz}}H=q_z+q^2,
\tag{13}
\]

we obtain

\[
q_t
=\partial_z\!\left(-\frac{H_{zz}}H\right)
=-q_{zz}-2qq_z
=-q_{zz}-(q^2)_z.
\tag{14}
\]

Restricting to `z=x+ia` gives (2). Unlike the particle equation, this identity has no collision denominator: `q` is holomorphic everywhere away from the zeros, and the entire horizontal half-plane `Im z>a` stays zero-free. A collision below the line changes neither the domain nor the regularity of (14).

Fourier transforming (14) gives (5), since

\[
\widehat{-Q_{a,xx}}=\xi^2\widehat Q_a,
\qquad
\widehat{Q_a^2}
=\frac1{2\pi}(\widehat Q_a*\widehat Q_a).
\tag{15}
\]

The only delicate point is that these are distributional identities rather than ordinary `L^1` Fourier integrals. The polynomial bound (12) supplies temperedness, while the one-sided support below makes the convolution canonical.

## 3. Upper-half-plane analyticity forces exact positive-frequency support

For fixed `t>=0`, the map

\[
w\longmapsto q(w+ia,t)
\tag{16}
\]

is holomorphic for `Im w>0` and has polynomial boundary growth. The classical Fourier--Laplace/Paley--Wiener theorem for distributional boundary values of half-plane holomorphic functions therefore places its boundary Fourier transform on one half-axis. With convention (3) the correct half-axis is `[0,infinity)`.

The sign can be checked without convention ambiguity on the elementary pole kernel. If `z_0` lies below the horizontal line, then

\[
\int_{\mathbb R}
\frac{e^{-i\xi x}}{x+ia-z_0}\,dx
=
-2\pi i\,e^{-a\xi}e^{-i\xi z_0},
\qquad \xi>0,
\tag{17}
\]

and the transform is zero for `xi<0`. The paired Hadamard logarithmic derivative is the infinite analogue of the same Cauchy kernels. Hence (4) is not a reality statement about the roots; it is a half-plane analyticity statement about a zero-free line above the whole zero strip.

Because the closed half-line is a proper convolution cone, addition

\[
(\eta,\zeta)\mapsto\eta+\zeta
\tag{18}
\]

is proper on its intersection with the preimage of a compact frequency set. Thus the convolution of two distributions supported in `[0,infinity)` is defined. Its restriction at positive target frequency uses only the compact simplex

\[
0\le\eta\le\xi.
\tag{19}
\]

This proves the infinite one-sided transport statement without truncating the zero set.

## 4. The horizontal carrier is the canonical renormalized positive-frequency zero field

For a finite polynomial whose roots all lie below `Im z=a`, the logarithmic derivative is

\[
Q_{a,N}(x)
=
\sum_{j=1}^N\frac1{x+ia-x_j},
\tag{20}
\]

so (17) gives exactly

\[
\widehat Q_{a,N}(\xi)
=-2\pi i\,e^{-a\xi}Z_N(\xi),
\qquad
Z_N(\xi)=\sum_j e^{-i\xi x_j},
\quad \xi>0.
\tag{21}
\]

Therefore (6) agrees exactly with the finite field used in XF-049 and XF-050. Substituting (21) into (5) reproduces

\[
\partial_t Z_N
=\xi^2Z_N
-\xi\int_0^\xi Z_N(\eta)Z_N(\xi-\eta)\,d\eta,
\tag{22}
\]

including the sign and coefficient. This finite consistency check rules out a Fourier-convention artifact.

For the infinite Xi family, (6) can instead be taken as the **definition** of the renormalized positive-frequency zero field. It does not depend on the chosen height. If `a_2>a_1>1`, vertical translation in the common zero-free half-plane gives

\[
\widehat Q_{a_2}(\xi,t)
=e^{-(a_2-a_1)\xi}\widehat Q_{a_1}(\xi,t),
\qquad \xi>0,
\tag{23}
\]

so the factor `e^{a xi}` in (6) cancels the auxiliary line exactly.

The paired Hadamard product also shows what this renormalization means. On every compact positive-frequency interval bounded away from zero, pairing `mathcal Z_t` with a smooth compactly supported test agrees with the absolutely convergent pairing against the zero divisor obtained from the corresponding entire Schwartz test in physical space. Any canonical-product normalization terms are supported only at `xi=0` and disappear from such a test. Thus XF-050's compact one-sided band

\[
I_T=
[\omega-W^{-1},\omega+W^{-1}]
\subset(0,\log2/2)
\tag{24}
\]

has an exact infinite meaning for every fixed `T`: its endpoint statistic can be expressed as a compact pairing with `mathcal Z_0`, while its time derivative is governed by (7).

This is the point at which the raw divergent sum in XF-050 ceases to be the right object. The divergence at zero frequency is real, but it is an endpoint singularity of a well-defined half-line distribution rather than a failure of the positive-frequency field to exist.

## 5. What remains is a shrinking-band endpoint estimate, not structural renormalization

Equation (7) is not yet the desired upper-bound transport inequality. The XF-050 memory center satisfies

\[
\omega=\Theta(1/\log T),
\qquad
W^{-1}=\Theta(1/\log^3T),
\tag{25}
\]

so the compact band (24) approaches the singular endpoint `xi=0` as `T -> infinity`. The Volterra law allows the memory coefficient at `xi~omega` to receive input from the **entire lower-positive band** `0<=eta<=xi`. One-sidedness forbids high-positive/high-negative down-conversion, but it does not bound low-to-low transfer or the large archimedean background accumulated near zero.

Accordingly, the remaining quantitative theorem is now narrower. One needs a source-faithful decomposition of `mathcal Z_t` near `xi=0` into its deterministic archimedean/background part and a fluctuation for which the quadratic Volterra pairing against the XF-050 moving band is uniformly controlled over the relevant positive heat interval. A sufficient estimate would show that the contribution not already encoded by the transported endpoint fluctuation is `o(1)` in the matched statistic. A decisive negative would exhibit an order-one contribution generated from frequencies **below the memory band** or from the zero-frequency singularity itself.

A mechanism involving frequencies larger than the target, opposite-frequency mixing, loss of root reality, collision singularities, or a physical-space taper commutator no longer answers the current gate: (4)--(7) exclude those as structural sources in this carrier.

## 6. Prior-art and novelty boundary

The ingredients used here are classical separately. De Bruijn's 1950 theorem supplies strip shrinking under the heat deformation. The order-one Hadamard product and logarithmic-derivative zero representation are standard in the de Bruijn--Newman/Lehmer-pair literature. Cole--Hopf/logarithmic-derivative conversion of a linear heat equation to complex Burgers is classical. The half-line support statement for polynomial-growth holomorphic boundary values is a Paley--Wiener--Schwartz/Fourier--Laplace theorem; a modern precise reference is Marcus Carlsson and Jens Wittsten, *A Note on Holomorphic Functions and the Fourier--Laplace Transform*, Math. Scand. 120 (2017), 225--248, DOI `10.7146/math.scand.a-25612`.

A targeted search did not locate a source that states the particular Xi-flow conclusion (6)--(7) as the collision-safe infinite continuation of the finite XF-050 memory-band field. No claim is made that the classical components are new. The durable Mathia delta is the reduction: **infinite-volume existence and one-sidedness can be made exact by moving from a raw zero characteristic sum to the horizontal logarithmic derivative; the only remaining obstruction for the XF-050 selector is quantitative control as the positive band collapses toward zero frequency.**

The 2025 Schatz preprint already uses a logarithmic derivative in a different backward-positivity argument; it is not evidence for this result, and XF-001's audit of that argument remains untouched. Nothing here imports its root-labelling or collision-bridging claims.

## 7. Falsification controls and consequences

Three controls are immediate. First, finite polynomial substitution must recover XF-050 exactly; equations (21)--(22) do. Second, changing the auxiliary height `a>1` must not change `mathcal Z_t`; equation (23) gives exact cancellation. Third, the degree-two collision model from XF-050 remains regular because the horizontal logarithmic derivative has no pole on `Im z=a` as the roots merge and leave the real axis.

The strongest failure mode left is also explicit: if `mathcal Z_t` has an endpoint singular component whose Volterra self-interaction contributes order one to the XF-050 band after the archimedean part is subtracted, the endpoint prime-free selector need not propagate with the required margin. This finding supplies no estimate excluding that possibility.

Thus XF-051 does **not** prove `Lambda<=0`, does not assert an `o(1)` transport error, and does not turn a single endpoint scalar into a closed dynamical variable. It does remove the qualitative infinite-renormalization and localization uncertainty from the accepted endpoint-selector direction. The next gate is the quantitative `xi downarrow 0` analysis of the exact half-line distribution (6), especially the background/fluctuation decomposition inside `0<=xi<=Theta(1/log T)`.