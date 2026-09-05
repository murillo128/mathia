# XF-054 — moving high line makes endpoint memory selector uniform

**Status:** `EXACT-DERIVED` + `UNIFORM-MATCHED-STATISTIC` + `SOURCE-SPECIFIC-TRANSPORT` + `CLASSICAL-HEAT/EULER-INPUT`. XF-053 shows that every fixed heat-time jet of the XF-050 memory-band statistic is `o(1)` but leaves open a genuinely nonuniform infinite-order replenishment from the singular endpoint. For the actual Xi family, that remaining escape can be removed at the level of the **matched compact statistic** without proving pointwise endpoint analyticity.

Let `f_T` be the compact one-sided XF-050 probe

\[
f_T(x)=g\!\left(\frac{x-T}{W}\right)e^{-i(\omega(x-T)+\varphi_T)},
\qquad
\widehat g=\chi\in C_c^\infty((-1,1)),
\tag{1}
\]

with

\[
\omega\asymp(\log T)^{-1},
\qquad
W\asymp\log^3T,
\qquad
W\omega\asymp\log^2T.
\tag{2}
\]

Its Fourier support is the negative interval of width `2/W` centered at `-omega`. With the canonical positive-frequency carrier `mathcal Z_t` of XF-051, define

\[
\mathcal S_T(t)
:=\frac1{2\pi}
\left\langle\mathcal Z_t(\xi),\widehat f_T(-\xi)\right\rangle.
\tag{3}
\]

For every fixed `t_0>0`, there is a fixed `A=A(t_0)>0` such that, if the auxiliary zero-free height is chosen as

\[
a_T=A\log T,
\tag{4}
\]

then

\[
\boxed{
\sup_{0\le t\le t_0}|\mathcal S_T(t)|=o(1)
\qquad(T\to\infty).
}
\tag{5}
\]

No RH assumption, real-root hypothesis, or finite-root truncation is used. The carrier is exactly independent of the horizontal height. Since `a_T omega=O_A(1)`, moving the line to height `A log T` costs only a bounded carrier renormalization. The Xi functional equation reflects that line into `Re s asy A log T`, where the Euler product makes the arithmetic factor polynomially small in `T`, uniformly through any fixed heat interval. The remaining deterministic heat-evolved gamma/polar background varies on the physical `T` scale, while the XF-050 probe makes `W omega asy log^2 T` oscillations across its envelope; repeated integration by parts kills that background.

Thus the infinite-order endpoint phenomenon left by XF-053 may still exist pointwise or distributionally near `xi=0`, but it cannot rebuild an order-one coefficient in the specific memory statistic that detects the XF-047 coherent slow mode. This resolves the accepted endpoint-selector transport clue at its matched-statistic level. It does not by itself bound `Lambda`; the remaining task is to connect this uniform source selector to the transition-side Cauchy rigidity/coercivity mechanism.

## 1. Exact heat representation on the reflected line

Normalize by one fixed nonzero scalar and put

\[
F_t(s):=H_t\!\left(-2i(s-\tfrac12)\right),
\qquad F_0(s)=\xi(s).
\tag{6}
\]

The scalar normalization is irrelevant to logarithmic derivatives. From `partial_t H_t=-partial_z^2 H_t` and `z=-2i(s-1/2)`,

\[
\boxed{\partial_tF_t=\frac14\partial_s^2F_t.}
\tag{7}
\]

Evenness of `H_t` gives

\[
F_t(s)=F_t(1-s).
\tag{8}
\]

For `t>0`, Gaussian heat propagation is exact:

\[
\boxed{
F_t(s)=\frac1{\sqrt{\pi t}}
\int_{\mathbb R}e^{-r^2/t}\xi(s+r)\,dr.
}
\tag{9}
\]

This also follows directly from the defining `H_t` integral: averaging in the real `s` direction multiplies each exponential component by `e^{t u^2}`. The Gaussian dominates the order-one growth of `xi`, so (9) and its `s` derivatives are legitimate on the moving lines below. The `t=0` case is the limiting identity.

For `z=x+i a`, set

\[
s_-(x,a):=(1-a)/2+i x/2,
\qquad
v(x,a):=1-s_-(x,a)=(1+a)/2-i x/2.
\tag{10}
\]

Differentiating (8) yields the exact reflected logarithmic derivative

\[
\boxed{
Q_a(x,t):=\frac{H_t'(x+i a)}{H_t(x+i a)}
=-\frac{i}{2}\frac{F_t'(v(x,a))}{F_t(v(x,a))}.
}
\tag{11}
\]

For every `a>1` the line is zero-free by the strip control already used in XF-051, so (11) applies to the moving choice (4).

## 2. Right-half-plane dominance at height `A log T`

Write

\[
\sigma_T:=(1+a_T)/2,
\qquad
v_T(x):=\sigma_T-i x/2.
\tag{12}
\]

On `|x-T|<=T/2`, one has `|v_T(x)| asy T` and

\[
\operatorname{Re}v_T(x)=\frac{A}{2}\log T+O(1).
\tag{13}
\]

Use the usual factorization

\[
\xi(s)=G(s)\zeta(s),
\qquad
G(s):=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\tag{14}
\]

Define the deterministic heat background on this line by

\[
G_t(v):=\frac1{\sqrt{\pi t}}
\int_{\mathbb R}e^{-r^2/t}G(v+r)\,dr,
\qquad G_0=G.
\tag{15}
\]

The path has fixed imaginary part `-x/2`, so it does not meet the real poles of the separate gamma factor. Let `L=G'/G`. Uniform Stirling expansion in the region (13) gives

\[
L(v_T(x))=\frac12\Log\!\left(\frac{v_T(x)}{2\pi}\right)+O(T^{-1}),
\qquad
L^{(k)}(v_T(x))=O_k(T^{-k})\ (k\ge1).
\tag{16}
\]

Hence `Re L=O(log T)` and `Im L=O(1)`. The Gaussian in (15) is tilted only by `O(log T)` in the real `r` direction. Expanding `log G(v+r)` through that tilted window gives, uniformly for `0<=t<=t_0` and `|x-T|<=T/2`,

\[
G_t(v)=G(v)\exp\!\left(\frac{t}{4}L(v)^2\right)
\left(1+O_{t_0}\!\left(\frac{\log^2T}{T}\right)\right).
\tag{17}
\]

The expansion can be differentiated a fixed number of times. In particular, for large `T`, `G_t` is nonzero in the region and

\[
\frac{G_t'}{G_t}=O_{t_0}(\log T),
\qquad
\partial_x^k\!\left(\frac{G_t'}{G_t}(v_T(x))\right)
=O_{k,t_0}\!\left(\frac{(\log T)^{C_k}}{T^k}\right)
\quad(k\ge1).
\tag{18}
\]

Only this scale separation is needed; no sharp Stirling coefficient enters the conclusion.

## 3. Uniform suppression of the arithmetic factor

Split (9) at `r=-sigma_T/2`. On the main portion,

\[
\operatorname{Re}(v_T+r)\ge\sigma_T/2
=\frac{A}{4}\log T+O(1).
\tag{19}
\]

The absolutely convergent Euler product gives

\[
|\zeta(v_T+r)-1|+|\zeta'(v_T+r)|
\ll 2^{-\operatorname{Re}(v_T+r)}
\ll T^{-A\log2/4+o(1)}.
\tag{20}
\]

The complex Gaussian saddle does not erase this power gain. For the leading approximation `G(v)e^{rL(v)}`, the ratio of the absolute Gaussian integral to the modulus of the complex Gaussian integral is

\[
\exp\!\left(\frac{t}{4}(\operatorname{Im}L(v))^2\right)=O_{t_0}(1),
\tag{21}
\]

because `Im L=O(1)`. The errors are the same `O(log^2T/T)` terms already controlled in (17).

On the complementary negative tail, the Gaussian contributes

\[
\exp\!\left(-cA^2(\log T)^2/t_0\right).
\tag{22}
\]

Uniform Stirling bounds, together with the Xi functional equation after the real part crosses leftward, bound the remaining growth by `exp(O(|r| log(T+|r|)))`. Taking `A` sufficiently large relative to the fixed `t_0` leaves this tail super-polynomially small compared with (17). The same estimates survive one `s` derivative.

Therefore there is `kappa_A>0`, made arbitrarily large by increasing the fixed `A`, for which

\[
\frac{F_t(v_T(x))}{G_t(v_T(x))}
=1+O_{t_0}(T^{-\kappa_A}(\log T)^C)
\tag{23}
\]

and

\[
\frac{F_t'}{F_t}(v_T(x))-
\frac{G_t'}{G_t}(v_T(x))
=O_{t_0}(T^{-\kappa_A}(\log T)^C)
\tag{24}
\]

uniformly for `0<=t<=t_0` and `|x-T|<=T/2`.

Define

\[
Q^{\rm bg}_{a_T}(x,t):=-\frac{i}{2}
\frac{G_t'}{G_t}(v_T(x)).
\tag{25}
\]

Then

\[
Q_{a_T}(x,t)-Q^{\rm bg}_{a_T}(x,t)
=O(T^{-\kappa_A}(\log T)^C)
\tag{26}
\]

on the central region, while (18) shows that the background varies only on the physical `T` scale. This is the source-specific step: it uses both Xi symmetry and the Euler product. A generic matched heat flow need not satisfy it.

## 4. Height independence converts the carrier pairing exactly

XF-051 gives, for every `a>1`,

\[
\mathcal Z_t(\xi)=\frac{i}{2\pi}e^{a\xi}\widehat Q_a(\xi,t),
\qquad \xi>0,
\tag{27}
\]

and the left side is independent of `a`. Fourier translation of `h_{T,a}(x):=f_T(x+i a)` gives

\[
\widehat h_{T,a}(-\xi)=e^{a\xi}\widehat f_T(-\xi).
\tag{28}
\]

Parseval therefore yields the exact identity

\[
\boxed{
\mathcal S_T(t)=\frac{i}{2\pi}
\int_{\mathbb R}Q_a(x,t)f_T(x+i a)\,dx,
}
\tag{29}
\]

valid for any `a>1`, in particular `a=a_T`.

For the XF-050 probe,

\[
f_T(x+i a_T)
=e^{a_T\omega-i\varphi_T}
 g\!\left(\frac{x-T}{W}+i\frac{a_T}{W}\right)
 e^{-i\omega(x-T)}.
\tag{30}
\]

The scale match is exact in the only sense needed here:

\[
a_T\omega=O_A(1),
\qquad
a_T/W=O_A((\log T)^{-2}).
\tag{31}
\]

Thus the exponential factor stays bounded and the vertically shifted `g` is uniformly Schwartz. Moving the line has not changed or attenuated the canonical statistic.

## 5. Oscillatory cancellation of the deterministic background

On `|x-T|<=T/2`, the arithmetic error (26) contributes at most

\[
O(WT^{-\kappa_A}(\log T)^C)=o(1).
\tag{32}
\]

For the background term, substitute (30) into (29) and integrate by parts three times against `e^{-i omega(x-T)}`. The term in which all three derivatives hit the envelope is

\[
O\!\left((\log T)W(W\omega)^{-3}\right)
=O((\log T)^{-2}),
\tag{33}
\]

using `Q^{bg}=O(log T)`, `W asy log^3T`, and `W omega asy log^2T`. Every term in which at least one derivative hits `Q^{bg}` gains an additional `W/T`, up to powers of `log T`, by (18), so it is smaller. Hence the central background integral is `o(1)` uniformly in `0<=t<=t_0`.

Outside `|x-T|<=T/2`, the uniformly Schwartz factor in (30) is evaluated at real distance at least `T/(2W)`. The paired-zero/Hadamard estimate already used in XF-051 gives polynomial growth for `Q_{a_T}`; the increasing distance of the line from the zero strip only helps. Taking sufficiently many Schwartz powers makes this tail `o(1)` uniformly on the fixed heat interval. Combining the central arithmetic estimate, the background cancellation, and the physical tails proves (5).

## 6. Falsification controls and scale boundary

The moving line cannot erase a genuine memory coefficient by fiat. The exact identity (27) implies

\[
e^{a\xi}\widehat Q_a(\xi,t)=-2\pi i\,\mathcal Z_t(\xi),
\tag{34}
\]

so a mode at `xi asy 1/log T` is invariant under changing `a`. In particular the coherent XF-050 control still has

\[
\mathcal S_T=-\kappa/2+o(1),
\tag{35}
\]

while the actual Xi statistic satisfies (5). The proof discriminates the Xi source; it is not a coordinate trick.

The height `a_T asy log T` is matched to the memory scale. It is large enough to turn Euler-product decay into a power of `T`, but small enough that `e^{a_T omega}` stays bounded. Taking `a_T` much larger would lose that balance, while `a_T=o(log T)` need not give enough arithmetic suppression to beat the envelope.

At `t=0`, (5) agrees with the exact Guinand--Weil prime-free estimate of XF-050. The present proof reaches the same endpoint statistic by a different route: height invariance plus right-half-plane Euler-product rigidity.

The conclusion is intentionally statistic-specific. It does not prove a literal positive-time prime-free support gap, does not prove a regular germ for `mathcal Z_t` at `xi=0`, and does not justify uniform convergence of the Taylor series considered in XF-053. It proves that any such infinite-order endpoint structure has only `o(1)` projection onto the matched source-discriminating memory probe.

## 7. Prior-art and novelty boundary

The analytic ingredients are classical: the Xi functional equation and Euler product, Gaussian heat propagation, uniform Stirling expansion, and the height-independent horizontal logarithmic-derivative carrier already established in XF-051. The Polymath15 high-zero analysis anchored in `SOURCES.md` also exhibits right-half-plane/freezing behavior for positive heat time in a different asymptotic regime, but its stated Riemann--Siegel approximation uses bounded imaginary displacement and does not directly provide the moving-height `a_T=A log T` carrier estimate (5).

A targeted literature audit did not locate a theorem stated as this moving-height transport of the XF-050 shrinking one-sided statistic. No novelty is claimed for the classical components or for generic heat-kernel saddle estimates. The durable Mathia delta is the scale match: **height independence permits `a_T asy log T`; Xi symmetry converts the shrinking-frequency endpoint problem into a right-half-plane Euler-product estimate while the carrier normalization remains bounded.**

No additional external theorem is load-bearing beyond sources already anchored in `research/xi_flow/SOURCES.md`, so no source-file update is required.

## 8. Consequence for `xi_flow`

XF-048 finds a source-specific memory selector, XF-050 makes it compact and collision-safe, XF-051 supplies the exact infinite carrier, XF-052 identifies the endpoint background, and XF-053 excludes every finite-order replenishment. Equation (5) closes the remaining fixed-interval replenishment question for the actual matched statistic:

\[
\boxed{
\text{actual Xi matched endpoint statistic}=o(1)
\quad\text{uniformly for every fixed }0\le t\le t_0.
}
\tag{36}
\]

The endpoint-transport clue is therefore resolved in the positive direction. Further fixed heat jets or finer local expansions of the singular `xi=0` background are no longer the load-bearing gate for this selector. What remains is downstream: show that a hypothetical positive-`Lambda` transition necessarily produces, at some fixed heat time and source-relevant scale, the order-one memory coefficient already ruled out by (5), or identify a different transition geometry that evades that implication. No such transition-to-memory theorem, upper bound on `Lambda`, or RH conclusion is claimed here.
