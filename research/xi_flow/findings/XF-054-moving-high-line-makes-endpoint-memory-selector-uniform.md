# XF-054 — moving high line makes endpoint memory selector uniform

**Status:** `EXACT-DERIVED` + `UNIFORM-MATCHED-STATISTIC` + `SOURCE-SPECIFIC-TRANSPORT` + `CLASSICAL-HEAT/EULER-INPUT`. XF-053 shows that every fixed heat-time jet of the XF-050 memory-band statistic is `o(1)` but leaves open a genuinely nonuniform infinite-order replenishment from the singular endpoint. For the actual Xi family, that remaining escape can be removed at the level of the **matched compact statistic** without proving pointwise endpoint analyticity.

Let `f_T` be the compact one-sided XF-050 probe,

\[
f_T(x)
=
g\!\left(\frac{x-T}{W}\right)
 e^{-i(\omega(x-T)+\varphi_T)},
\qquad
\widehat g=\chi\in C_c^\infty((-1,1)),
\tag{1}
\]

with

\[
\omega\asymp\frac1{\log T},
\qquad
W\asymp\log^3T,
\qquad
W\omega\asymp\log^2T.
\tag{2}
\]

Its Fourier support is the negative interval of width `2/W` centered at `-omega`, hence the canonical positive-frequency carrier of XF-051 defines

\[
\mathcal S_T(t)
:=
\frac1{2\pi}
\left\langle
\mathcal Z_t(\xi),
\widehat f_T(-\xi)
\right\rangle.
\tag{3}
\]

For every fixed `t_0>0`, there is a fixed `A=A(t_0)>0` such that, with the auxiliary zero-free height chosen **after** `T` as

\[
a_T=A\log T,
\tag{4}
\]

one has the uniform estimate

\[
\boxed{
\sup_{0\le t\le t_0}
|\mathcal S_T(t)|
=o(1),
\qquad T\to\infty.
}
\tag{5}
\]

No RH assumption, real-root hypothesis, or finite-root truncation is used. The point is that the carrier is exactly independent of the horizontal height. At the memory frequency, `a_T omega=O_A(1)`, so moving the line to height `A log T` costs only a bounded carrier renormalization. After the Xi functional equation reflects that line into `Re s \asymp A log T`, the Euler product makes the arithmetic factor polynomially small in `T`, uniformly through every fixed heat interval. What remains is a deterministic heat-evolved gamma/polar background varying on the physical `T` scale, while the XF-050 probe has `W omega \asymp log^2 T` oscillations across its envelope; repeated integration by parts kills that background.

Thus the infinite-order endpoint effect left by XF-053 may still exist as a pointwise/distributional phenomenon near `xi=0`, but it cannot rebuild an order-one coefficient in the **specific memory statistic that detects the XF-047 coherent slow mode**. This resolves the accepted endpoint-selector transport clue at its stated matched-statistic level. It does not by itself bound `Lambda`: the remaining task is to connect this uniform source selector to the transition-side Cauchy rigidity/coercivity mechanism.

## 1. The Xi heat flow becomes ordinary heat flow in the `s` variable

Normalize by one fixed nonzero scalar and define

\[
F_t(s)
:=
H_t\!\left(-2i(s-\tfrac12)\right)
\quad\text{so that}\quad
F_0(s)=\xi(s).
\tag{6}
\]

The scalar normalization is irrelevant to logarithmic derivatives. Since

\[
\partial_tH_t=-\partial_z^2H_t,
\]

and `z=-2i(s-1/2)`, one has the exact forward heat equation

\[
\boxed{
\partial_tF_t=\frac14\partial_s^2F_t.
}
\tag{7}
\]

Evenness of `H_t` gives the functional equation

\[
F_t(s)=F_t(1-s)
\tag{8}
\]

for every `t>=0`. For `t>0`, the heat equation has the exact Gaussian representation

\[
\boxed{
F_t(s)
=
\frac1{\sqrt{\pi t}}
\int_{\mathbb R}
 e^{-r^2/t}\,\xi(s+r)\,dr.
}
\tag{9}
\]

It can also be checked directly from the defining `H_t` integral: Gaussian averaging in the real `s` direction multiplies each exponential component by `e^{t u^2}`. The Gaussian dominates the order-one growth of `xi`, so (9) and its `s` derivatives are legitimate on the moving lines used below. At `t=0`, all statements are interpreted by the obvious limiting identity.

For `z=x+i a`, put

\[
s_-(x,a)=\frac{1-a}{2}+\frac{i x}{2},
\qquad
u(x,a)=1-s_-(x,a)
=rac{1+a}{2}-\frac{i x}{2}.
\tag{10}
\]

Differentiating (8) gives the exact reflected logarithmic derivative

\[
\boxed{
Q_a(x,t)
:=
\frac{H_t'(x+i a)}{H_t(x+i a)}
=
-\frac{i}{2}
\frac{F_t'(\nu(x,a))}{F_t(\nu(x,a))}.
}
\tag{11}
\]

For every `a>1` the line is zero-free by the strip control already used in XF-051. Hence (11) is valid in particular for the moving choice (4).

## 2. A moving height turns the exact carrier into a right-half-plane problem

Set

\[
\sigma_T:=\frac{1+a_T}{2},
\qquad
u_T(x)=\sigma_T-\frac{i x}{2}.
\tag{12}
\]

On the central physical region `|x-T|<=T/2`,

\[
|\nu_T(x)|\asymp T,
\qquad
\operatorname{Re}\nu_T(x)
=\frac{A}{2}\log T+O(1).
\tag{13}
\]

Write the completed zeta function in the usual form

\[
\xi(s)=G(s)\zeta(s),
\qquad
G(s)
:=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\tag{14}
\]

Define the deterministic heat background on this line by

\[
G_t(\nu)
:=
\frac1{\sqrt{\pi t}}
\int_{\mathbb R}
 e^{-r^2/t}G(\nu+r)\,dr,
\qquad t>0,
\tag{15}
\]

with `G_0=G`. The integration path has fixed imaginary part `-x/2`, so it does not meet the real poles of the separate gamma factor.

Let

\[
L(\nu):=\frac{G'(\nu)}{G(\nu)}.
\]

Uniform Stirling expansion in (13) gives

\[
L(\nu_T(x))
=
\frac12\Log\!\left(\frac{\nu_T(x)}{2\pi}\right)
+O(T^{-1}),
\tag{16}
\]

and, for every fixed `k>=1`,

\[
L^{(k)}(\nu_T(x))=O_k(T^{-k}).
\tag{17}
\]

In particular `Re L=O(log T)` while `Im L=O(1)`. The Gaussian in (15) is therefore effectively tilted by only `O(log T)` in the real `r` direction. Expanding `log G(\nu+r)` through the tilted Gaussian window and using (17) yields, uniformly for `0<=t<=t_0` and `|x-T|<=T/2`,

\[
\boxed{
G_t(\nu)
=
G(\nu)
\exp\!\left(\frac{t}{4}L(\nu)^2\right)
\left(1+O_{t_0}\!\left(\frac{\log^2T}{T}\right)\right).
}
\tag{18}
\]

The same expansion may be differentiated a fixed number of times. In particular `G_t` is nonzero there for large `T` and

\[
\frac{G_t'}{G_t}=O_{t_0}(\log T),
\qquad
\partial_x^k\!\left(\frac{G_t'}{G_t}(\nu_T(x))\right)
=
O_{k,t_0}\!\left(\frac{(\log T)^{C_k}}{T^k}\right)
\quad(k\ge1).
\tag{19}
\]

Only the scale separation in (19) is needed below; no sharp Stirling coefficient is used.

## 3. The arithmetic part is uniformly negligible on the moving line

The heat representation (9) makes the source-specific gain explicit. Split the `r` integral at

\[
r=-\frac{\sigma_T}{2}.
\]

On the main portion `r>=-sigma_T/2`,

\[
\operatorname{Re}(\nu_T+r)
\ge
\frac{\sigma_T}{2}
=
\frac{A}{4}\log T+O(1).
\tag{20}
\]

The absolutely convergent Euler product therefore gives, uniformly there,

\[
|\zeta(\nu_T+r)-1|
+|\zeta'(\nu_T+r)|
\ll
2^{-\operatorname{Re}(\nu_T+r)}
\ll
T^{-A\log2/4+o(1)}.
\tag{21}
\]

The complex Gaussian saddle does not destroy this gain. By (16), the ratio between the absolute-value Gaussian integral of the leading approximation `G(\nu)e^{rL(\nu)}` and the modulus of its complex Gaussian integral is

\[
\exp\!\left(\frac{t}{4}(\operatorname{Im}L(\nu))^2\right)=O_{t_0}(1).
\tag{22}
\]

The errors in replacing `G(\nu+r)` by that saddle model are the same `O(log^2T/T)` terms already controlled in (18).

On the complementary negative tail `r<-sigma_T/2`, the Gaussian factor contributes

\[
\exp\!\left(-c\,A^2(\log T)^2/t_0\right).
\tag{23}
\]

Uniform Stirling bounds, and the functional equation when the real part crosses leftward, show that the growth of `xi(\nu+r)` on that tail is at most exponential in `O(|r|\log(T+|r|))`; choosing `A` sufficiently large relative to the fixed `t_0` leaves (23) super-polynomially small compared with (18). The same argument survives one `s` derivative.

Consequently there exists `kappa_A>0`, which can be made arbitrarily large by increasing the fixed `A`, such that

\[
\boxed{
\frac{F_t(\nu_T(x))}{G_t(\nu_T(x))}
=1+O_{t_0}\!\left(T^{-\kappa_A}(\log T)^C\right),
}
\tag{24}
\]

and

\[
\boxed{
\frac{F_t'}{F_t}(\nu_T(x))
-
\frac{G_t'}{G_t}(\nu_T(x))
=
O_{t_0}\!\left(T^{-\kappa_A}(\log T)^C\right)
}
\tag{25}
\]

uniformly for `0<=t<=t_0` and `|x-T|<=T/2`. The constants may depend on `t_0` and `A`, but not on `T` or `t`.

Define

\[
Q^{\rm bg}_{a_T}(x,t)
:=-\frac{i}{2}
\frac{G_t'}{G_t}(\nu_T(x)).
\tag{26}
\]

Then (11), (19), and (25) give on the central region

\[
Q_{a_T}-Q^{\rm bg}_{a_T}
=
O\!\left(T^{-\kappa_A}(\log T)^C\right),
\tag{27}
\]

while `Q^{bg}` varies only on the `T` scale.

This is the step unavailable to a generic matched heat flow. It uses both the Xi functional equation, which reflects the high horizontal line into the right half-plane, and the Euler product, which forces `zeta(s)->1` there.

## 4. Height independence gives an exact physical-space pairing

The crucial point is that choosing `a_T` does not change the observable. XF-051 proves

\[
\mathcal Z_t(\xi)
=
\frac{i}{2\pi}e^{a\xi}\widehat Q_a(\xi,t),
\qquad \xi>0,
\tag{28}
\]

independently of every `a>1`. If

\[
h_{T,a}(x):=f_T(x+i a),
\]

then Fourier translation gives

\[
\widehat h_{T,a}(-\xi)
=e^{a\xi}\widehat f_T(-\xi).
\tag{29}
\]

Parseval therefore turns (3) into the exact identity

\[
\boxed{
\mathcal S_T(t)
=
\frac{i}{2\pi}
\int_{\mathbb R}
 Q_a(x,t)f_T(x+i a)\,dx
}
\tag{30}
\]

for any `a>1`, in particular `a=a_T`.

For the XF-050 probe,

\[
f_T(x+i a_T)
=
e^{a_T\omega-i\varphi_T}
 g\!\left(\frac{x-T}{W}+i\frac{a_T}{W}\right)
 e^{-i\omega(x-T)}.
\tag{31}
\]

The moving height is exactly matched to the shrinking frequency:

\[
a_T\omega=O_A(1),
\qquad
\frac{a_T}{W}=O_A((\log T)^{-2}).
\tag{32}
\]

Hence the exponential factor in (31) stays bounded and the shifted `g` remains uniformly Schwartz. There is no hidden large renormalization penalty.

## 5. The deterministic background is invisible to the memory probe

Insert (26) into (30). On `|x-T|<=T/2`, the arithmetic error (27) has total contribution

\[
\ll
W\,T^{-\kappa_A}(\log T)^C
=o(1)
\tag{33}
\]

after choosing `A` so that `kappa_A>0`; any positive power of `T` dominates `W\asymp log^3T`.

For the background term, use (31) and integrate by parts three times against `e^{-i omega(x-T)}`. The term in which all three derivatives hit the envelope is bounded by

\[
O\!\left(
(\log T)\,W\,(W\omega)^{-3}
\right)
=
O((\log T)^{-2}),
\tag{34}
\]

because `Q^{bg}=O(log T)`, `W\asymp log^3T`, and `W omega\asymp log^2T`. Terms in which at least one derivative hits `Q^{bg}` acquire an additional factor `W/T` (up to powers of `log T`) by (19), and are smaller. Thus

\[
\int_{|x-T|\le T/2}
 Q^{\rm bg}_{a_T}(x,t)f_T(x+i a_T)\,dx
=o(1)
\tag{35}
\]

uniformly in `0<=t<=t_0`.

Finally, outside `|x-T|<=T/2`, the uniformly Schwartz factor in (31) is evaluated at real distance at least `T/(2W)`. The paired-zero/Hadamard estimate already used in XF-051 gives polynomial growth for `Q_{a_T}`; in fact the increasing distance of the line from the zero strip only helps. Taking sufficiently many Schwartz powers makes the entire tail `o(1)` uniformly on the fixed heat interval. Combining the central arithmetic error, the background estimate, and the physical tails proves (5).

## 6. Falsification controls and the matched-model boundary

The first control is that the moving line cannot erase a genuine memory coefficient by fiat. For a finite zero system, or for any carrier to which the XF-051 identity applies,

\[
e^{a\xi}\widehat Q_a(\xi)
=-2\pi i\,\mathcal Z(\xi)
\tag{36}
\]

is exactly independent of `a`. A mode at `xi\asymp1/log T` therefore survives the move to `a_T`; its raw horizontal-line damping is exactly undone by the factor `e^{a_T xi}`. In particular, the coherent XF-050 control still has

\[
\mathcal S_T=-\frac\kappa2+o(1),
\tag{37}
\]

while the actual Xi statistic obeys (5). The proof is source-discriminating, not a coordinate trick.

Second, the scale `a_T\asymp log T` is structurally matched to the problem. It is high enough that the reflected Euler product produces a power of `T`, but low enough that `e^{a_T omega}` remains bounded. Choosing a much larger height would lose this balance; choosing `a_T=o(log T)` need not produce enough arithmetic suppression to beat the physical envelope.

Third, at `t=0`, (5) agrees with the exact Guinand--Weil prime-free estimate of XF-050. The present proof is a different route: it uses the height-invariant carrier and right-half-plane Euler-product rigidity rather than evaluating the endpoint explicit formula term by term.

The conclusion is deliberately statistic-specific. It does not prove a literal positive-time prime-free support gap, does not prove that `mathcal Z_t` has a regular germ at `xi=0`, and does not justify uniform convergence of the Taylor series considered in XF-053. It shows instead that any such nonperturbative endpoint structure has `o(1)` projection onto the source-discriminating memory probe.

## 7. Prior-art and novelty boundary

Every analytic ingredient used above is classical: the Xi functional equation and Euler product, Gaussian heat propagation, uniform Stirling expansion, and the height-independence of the horizontal logarithmic-derivative carrier already established in XF-051. The Polymath15 high-zero analysis recorded in `SOURCES.md` also exhibits right-half-plane/freezing behavior for positive heat time in a different asymptotic regime, but its stated Riemann--Siegel approximation uses bounded imaginary displacement and does not directly provide the moving-height `a_T=A log T` carrier estimate (5).

A targeted literature audit did not locate a theorem stated as this moving-height transport of the XF-050 shrinking one-sided statistic. No novelty is claimed for the classical components or for generic heat-kernel saddle estimates. The durable Mathia delta is the exact scale match: **height independence permits `a_T\asymp log T`; Xi symmetry then converts the shrinking-frequency endpoint problem into a right-half-plane Euler-product estimate while the carrier normalization stays bounded.**

No additional external theorem is load-bearing beyond sources already anchored in `research/xi_flow/SOURCES.md`, so no source-file update is required.

## 8. Consequence for `xi_flow`

XF-048 finds a source-specific memory selector, XF-050 makes it compact and collision-safe, XF-051 supplies the exact infinite carrier, XF-052 identifies the endpoint background, and XF-053 excludes every finite-order replenishment. Equation (5) closes the remaining fixed-interval replenishment question for the actual matched statistic:

\[
\boxed{
\text{actual Xi endpoint selector}
\xrightarrow[\text{any fixed }0\le t\le t_0]{\text{exact carrier}}
o(1).
}
\tag{38}
\]

The endpoint-transport clue is therefore resolved in the positive direction. Further fixed heat jets or finer local expansions of the singular `xi=0` background are no longer the load-bearing gate for this selector. What remains is downstream: show that a hypothetical positive-`Lambda` transition necessarily produces, at some fixed heat time and source-relevant scale, the order-one memory coefficient already ruled out by (5), or identify a different transition geometry that evades that implication. No such transition-to-memory theorem, upper bound on `Lambda`, or RH conclusion is claimed here.
