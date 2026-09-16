# WI-319 — The scalar-localizer recurrence obstruction has a sharp `t^2/log t` complexity threshold

**Status:** `EXACT-DERIVED + CLASSICAL-HARMONIC + DECISIVE-BARRIER + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-311, WI-312, WI-317, WI-318.

WI-318 proves that a uniformly `H^1`-bounded adaptive family of source-exact unit-window localizers cannot contract a reused scalar Weil defect. Its proof only records a qualitative escape condition: the total derivative energy must become unbounded.

The same recurrence argument admits a quantitative sharpening. If the localizer is allowed to depend on the high carrier `t`, write

\[
M_t:=\sum_\nu\|(g_{\nu,t})'\|_2^2
\]

for its total derivative energy. Then the continuous localization error obeys the uniform estimate

\[
\boxed{
|\mathcal C_t(f_t)|
\le C_{L,\phi}
\left(
\frac{1+\sqrt{M_t}}{|t|}
+
\frac{M_t\log(2+|t|)}{t^2}
\right)
}
\tag{1}
\]

for the WI-318 test vectors `f_t(u)=e^{itu}\phi(u)` and every unit-window real multiwindow localizer. Consequently

\[
M_t=o\!\left(\frac{t^2}{\log |t|}\right)
\quad\Longrightarrow\quad
\mathcal C_t(f_t)=o(1).
\tag{2}
\]

Along the common prime-phase recurrence sequence of WI-318, the arithmetic part still has the same family-independent positive first-prime floor. Therefore an adaptive scalar-feedback scheme that contracts by a fixed amount must, on that sequence, choose localizers satisfying

\[
\boxed{
M_{t_k}\ge c\,\frac{t_k^2}{\log t_k}
}
\tag{3}
\]

for some `c>0` and all sufficiently large `k` whenever `log 2<2L`. In the prime-free regime `2L<=log 2`, the same conclusion holds with `c` depending on the claimed contraction size.

This order is not an artifact of the estimate. There is an explicit three-window resonant family with

\[
M_t=M_0+c\frac{t^2}{\log t}
\]

whose continuous localization error on the same carrier satisfies

\[
\boxed{
\mathcal C_t(f_t)\longrightarrow-\frac c2.
}
\tag{4}
\]

Thus the high-carrier recurrence falsifier behind WI-317--WI-318 is quantitatively exhausted at the `t^2/log t` scale. Spectral noncompactness is not merely required: the scalar architecture has to pay an almost-quadratic frequency-second-moment bill before this particular obstruction can even cease to force the wrong sign. Conversely, once that bill is paid, the recurrence test itself no longer rules out contraction. This does **not** prove that such a high-complexity family contracts the Weil defect on every test vector.

## 1. Exact setting and the quantity to control

Retain the source-exact WI-311 localization identity and all notation from WI-318. For one admissible finite real multiwindow family

\[
G=(g_1,\ldots,g_J),
\qquad
\sum_{\nu=1}^J\|g_\nu\|_2^2=1,
\qquad
\operatorname{supp}g_\nu\subset(-1/2,1/2),
\]

put

\[
R(a)=\langle T_aG,G\rangle,
\qquad
M=\|G'\|_2^2
=\sum_\nu\|g_\nu'\|_2^2.
\tag{5}
\]

Fix the same real nonnegative unit vector

\[
\phi\in C_c^\infty((-L,L)),
\qquad
h(a)=\int\phi(u+a)\phi(u)\,du,
\]

and `f_t(u)=e^{itu}\phi(u)`. The continuous part of the source defect is

\[
\mathcal C_G(f_t)
=
\int_0^{A}
(1-R(a))\kappa(a)h(a)\cos(ta)\,da,
\qquad A:=2L,
\tag{6}
\]

with

\[
\kappa(a)
=
\frac{2e^{-a/2}}{1-e^{-2a}}
-4\cosh(a/2).
\tag{7}
\]

The point of the present refinement is that the constant hidden in WI-318's `O(1/t)` estimate can be tracked as `M` grows with `t`.

## 2. Spectral representation of the localizer autocorrelation

Use the unitary Fourier convention. Since the windows are real, the aggregate power spectrum defines a symmetric probability measure

\[
d\mu(\xi)
:=
\sum_\nu|\widehat g_\nu(\xi)|^2\,d\xi,
\]

for which

\[
R(a)=\int_{\mathbb R}\cos(a\xi)\,d\mu(\xi),
\qquad
\int_{\mathbb R}\xi^2\,d\mu(\xi)=M.
\tag{8}
\]

Thus

\[
1-R(a)
=
\int_{\mathbb R}(1-\cos(a\xi))\,d\mu(\xi).
\tag{9}
\]

The singularity in (6) is exactly first order. Since `h(0)=1`, `h'(0)=0`, and `a\kappa(a)` extends smoothly through zero with value one,

\[
\kappa(a)h(a)=\frac1a+s(a),
\qquad
s\in C^1([0,A]).
\tag{10}
\]

The support of `\phi` strictly inside `(-L,L)` makes this decomposition harmless at `A`; near the right endpoint `\kappa h=0` and hence `s=-1/a`.

By Tonelli/Fubini, justified near zero by `1-R(a)<=Ma^2/2`, write

\[
\mathcal C_G(f_t)
=
\int_{\mathbb R}
\bigl[J_0(t,\xi)+J_s(t,\xi)\bigr]
\,d\mu(\xi),
\tag{11}
\]

where

\[
J_0(t,\xi)
:=
\int_0^A
\frac{(1-\cos(\xi a))\cos(ta)}a\,da
\tag{12}
\]

and

\[
J_s(t,\xi)
:=
\int_0^A
(1-\cos(\xi a))s(a)\cos(ta)\,da.
\tag{13}
\]

The logarithmic threshold comes entirely from the singular term `J_0`.

## 3. Low spectral frequencies give a second-difference gain

Assume `t>0`; the estimate is even in `t`. For `|\xi|<=t/2`, the elementary cosine-integral identity gives

\[
\begin{aligned}
J_0(t,\xi)
={}&
\operatorname{Ci}(tA)
-rac12\operatorname{Ci}((t+\xi)A)
-rac12\operatorname{Ci}((t-\xi)A)
\\
&+\frac12\log\!\left(1-\frac{\xi^2}{t^2}\right).
\end{aligned}
\tag{14}
\]

For `tA` large, integration by parts in the defining tail integral for `Ci` yields `|Ci(x)|<=C/x`; and for `|\xi|<=t/2`,

\[
\left|
\log\!\left(1-\frac{\xi^2}{t^2}\right)
\right|
\le C\frac{\xi^2}{t^2}.
\]

Hence

\[
|J_0(t,\xi)|
\le C_A\left(\frac1t+\frac{\xi^2}{t^2}\right),
\qquad |\xi|\le t/2.
\tag{15}
\]

Integrating (15) over the low-frequency part of `\mu` gives

\[
\int_{|\xi|\le t/2}|J_0(t,\xi)|\,d\mu(\xi)
\le C_A\left(\frac1t+\frac M{t^2}\right).
\tag{16}
\]

This is the gain hidden by the one-integration-by-parts proof of WI-318: below resonance, the singular kernel sees a **second frequency difference**, so the second moment `M` enters divided by `t^2`.

## 4. The resonant tail costs exactly one logarithm

For arbitrary `\xi`, use `1-\cos x<=\min(2,x^2/2)` in (12):

\[
|J_0(t,\xi)|
\le
C_A\bigl(1+\log(1+A|\xi|)\bigr).
\tag{17}
\]

On `|\xi|>t/2` and `t>=2`, an elementary comparison gives

\[
1+\log(1+A|\xi|)
\le
C_A\frac{\xi^2}{t^2}\log(2+t).
\tag{18}
\]

Therefore

\[
\int_{|\xi|>t/2}|J_0(t,\xi)|\,d\mu(\xi)
\le
C_A\frac{M\log(2+t)}{t^2}.
\tag{19}
\]

This logarithm cannot be removed under second-moment control alone; Section 7 gives the matching resonant family.

## 5. The regular kernel remainder is cheaper

For `|\xi|<=t/2`, integrate (13) once by parts. Since `s,s'` are bounded and integrable on the fixed interval,

\[
|J_s(t,\xi)|
\le
\frac{C_s(1+|\xi|)}t.
\tag{20}
\]

Cauchy--Schwarz and (8) give

\[
\int|\xi|\,d\mu(\xi)\le\sqrt M.
\tag{21}
\]

For the high-frequency part use the crude bound `|J_s|<=2\|s\|_1` together with Chebyshev,

\[
\mu\{|\xi|>t/2\}\le\frac{4M}{t^2}.
\tag{22}
\]

Thus

\[
\int_{\mathbb R}|J_s(t,\xi)|\,d\mu(\xi)
\le
C_{L,\phi}
\left(
\frac{1+\sqrt M}{t}
+
\frac M{t^2}
\right).
\tag{23}
\]

Combining (16), (19), and (23) proves (1).

In particular, for a `t`-dependent localizer sequence,

\[
M_t=o\!\left(\frac{t^2}{\log t}\right)
\]

implies `\mathcal C_t(f_t)=o(1)`. The `\sqrt{M_t}/t` term is then `o(1/\sqrt{\log t})` and the logarithmic second-moment term is `o(1)`.

## 6. The WI-318 recurrence now forces almost-quadratic complexity

Suppose first that `\log2<2L`. WI-318 supplies an unbounded recurrence sequence `t_k`, independent of the localizer, such that every active prime-power phase is eventually nonnegative and

\[
\cos(t_k\log2)\ge\frac12.
\]

The unit-support square-zero translation estimate is also independent of `M`:

\[
R(\log2)\le\frac12.
\]

Consequently every admissible localizer satisfies, for all sufficiently large `k`,

\[
\mathcal P_G(f_{t_k})
\ge
\delta_{L,\phi}
:=
\frac{\log2}{2\sqrt2}h(\log2)
>0.
\tag{24}
\]

Let a scalar-feedback architecture claim a fixed contraction `\kappa>0`, so after seeing `f_{t_k}` it must choose some localizer `G_k` with

\[
\mathcal E_{G_k}(f_{t_k})
=
\mathcal C_{G_k}(f_{t_k})
+
\mathcal P_{G_k}(f_{t_k})
\le-\kappa.
\tag{25}
\]

If instead

\[
M_k\le\varepsilon\frac{t_k^2}{\log t_k},
\]

then (1) gives

\[
|\mathcal C_{G_k}(f_{t_k})|
\le
C_{L,\phi}
\left(
\frac1{t_k}
+
\frac{\sqrt\varepsilon}{\sqrt{\log t_k}}
+O(\varepsilon)
\right).
\tag{26}
\]

Choose `\varepsilon>0` sufficiently small in terms of `L,\phi`, then take `k` large. The right side is `<\delta_{L,\phi}/2`, contradicting (24)--(25). Hence there is a constant `c=c(L,\phi)>0` such that every contracting selector must satisfy

\[
\boxed{
M_k\ge c\frac{t_k^2}{\log t_k}
}
\tag{27}
\]

for all sufficiently large recurrence indices.

If `2L<=\log2`, there is no arithmetic part. A claimed contraction still requires `\mathcal C_{G_k}(f_{t_k})<=-\kappa`. The same estimate gives (27) with a positive constant depending additionally on `\kappa`.

Thus WI-318's qualitative conclusion `M_k\to\infty` understates the escape cost by almost two powers of the carrier.

## 7. Matching resonant localizers show the order is sharp for this obstruction

Fix any real

\[
g\in C_c^\infty((-1/2,1/2)),
\qquad \|g\|_2=1,
\]

and write

\[
R_g(a)=\int g(u+a)g(u)\,du,
\qquad
M_0=\|g'\|_2^2.
\]

For a fixed `c>0` and large `t`, put

\[
p_t:=\frac c{\log t}<1
\]

and use the three real windows

\[
\begin{aligned}
g_{0,t}(u)&=\sqrt{1-p_t}\,g(u),\\
g_{1,t}(u)&=\sqrt{p_t}\,g(u)\cos(tu),\\
g_{2,t}(u)&=\sqrt{p_t}\,g(u)\sin(tu).
\end{aligned}
\tag{28}
\]

They remain supported in the unit window and satisfy the exact normalization

\[
\sum_{j=0}^2\|g_{j,t}\|_2^2=1.
\tag{29}
\]

The sine/cosine cross terms cancel pointwise in the derivative energy, giving

\[
\boxed{
M_t
=
\sum_{j=0}^2\|g_{j,t}'\|_2^2
=
M_0+p_t t^2
=
M_0+c\frac{t^2}{\log t}.
}
\tag{30}
\]

Their aggregate autocorrelation is also exact:

\[
R_t(a)
=R_g(a)\bigl(1-p_t+p_t\cos(ta)\bigr).
\tag{31}
\]

Hence

\[
1-R_t(a)
=
(1-R_g(a))
+p_tR_g(a)(1-\cos(ta)).
\tag{32}
\]

The first term in (32) contributes `o(1)` to `\mathcal C_t(f_t)` by ordinary Riemann--Lebesgue. For the second term define

\[
W(a):=aR_g(a)\kappa(a)h(a).
\]

Then `W` is smooth at zero, compactly supported in the integration interval, and `W(0)=1`. Therefore

\[
\begin{aligned}
I_t
&:=
\int_0^A
R_g(a)(1-\cos(ta))\kappa(a)h(a)\cos(ta)\,da\\
&=
\int_0^A
W(a)\frac{(1-\cos(ta))\cos(ta)}a\,da.
\end{aligned}
\tag{33}
\]

Since

\[
(1-\cos x)\cos x
=-\frac12+\cos x-\frac12\cos(2x),
\tag{34}
\]

with the combination vanishing quadratically at zero, the standard logarithmic oscillatory integral estimate gives

\[
\boxed{
I_t=-\frac12\log t+O(1).
}
\tag{35}
\]

One direct proof splits at `a=1/t`: the inner interval is `O(1)`; on `[1/t,A]` the constant term in (34) contributes `-(1/2)\log t+O(1)`, while the two cosine terms are uniformly bounded by Dirichlet integration because `W` is smooth and compactly supported.

Multiplying (35) by `p_t=c/\log t` yields

\[
\boxed{
\mathcal C_t(f_t)
=-\frac c2+o(1).
}
\tag{36}
\]

This proves that the scale in (27) is order-sharp for the continuous part of the WI-318 falsifier.

There is an even sharper interpretation along the recurrence sequence itself. For every active prime power `n`,

\[
R_{t_k}(\log n)
=R_g(\log n)
\bigl(1-p_{t_k}+p_{t_k}\cos(t_k\log n)\bigr)
\longrightarrow R_g(\log n),
\]

and `\cos(t_k\log n)\to1`. Thus the finite arithmetic defect converges to the fixed positive value

\[
P_g
:=
\sum_{\log n<A}
\frac{2\Lambda(n)}{\sqrt n}
\bigl(1-R_g(\log n)\bigr)
 h(\log n).
\tag{37}
\]

Equations (36)--(37) give

\[
\boxed{
\mathcal E_{G_{t_k}}(f_{t_k})
\longrightarrow P_g-\frac c2.
}
\tag{38}
\]

Choosing `c>2P_g` makes the very sequence that defeated every bounded-`H^1` portfolio acquire **negative** source defect. Choosing `c>2(P_g+\kappa)` makes its limiting defect `<-\kappa`.

This does not establish the global contraction condition for all test vectors. It proves something narrower and decisive for the no-go architecture: the WI-317/WI-318 high-carrier recurrence witness cannot be pushed to rule out adaptive localizers once they are allowed derivative energy at the `t^2/log t` scale.

## 8. What this closes and what remains open

The scalar localization route now has a quantitative resource boundary:

\[
\boxed{
M_t=o(t^2/\log t)
\ \Longrightarrow\ 
\text{the common recurrence obstruction survives},
}
\]

while an explicit family with

\[
M_t\asymp t^2/\log t
\]

already defeats that obstruction on its own adversarial sequence.

Therefore merely replacing the bounded-`H^1` hypothesis of WI-318 by a slowly diverging frequency budget is not a meaningful escape. Any autonomous scalar-feedback proposal that still recycles only the same semibound must explain where an almost-quadratic localizer frequency moment comes from and how the resulting resonances are controlled on **all** test vectors, not only on the recurrence witness.

This also sharpens the interpretation of WI-311--WI-312. High localizer carrier is not just one optional way to leave compactness: near resonance with the adversarial carrier it is precisely how a `t^2/log t` budget can turn the archimedean localization error back into an order-one term. Paying that complexity bill does not create new arithmetic information; it only prevents the old recurrence witness from washing the continuous defect away.

The clean RH-facing alternatives remain those already isolated in WI-318: a genuinely stronger localized source estimate, mode- or prime-dependent information, vector/matrix rather than scalar feedback, different support geometry, or a direct sign/coercivity mechanism for the exact comparison form.

## 9. Prior-art and novelty audit

The analytic ingredients are classical. Equation (8) is the standard Wiener--Khinchin/Plancherel power-spectrum representation of an autocorrelation. The low-frequency estimate is an elementary second-difference calculation for the cosine integral; the high-frequency tail uses only a second-moment Markov bound. The `O(1/t)` decay of Fourier transforms of bounded-variation/absolutely-continuous amplitudes and compactness of bounded Sobolev families are standard harmonic-analysis facts. The simultaneous prime-phase recurrence and the Haagerup--de la Harpe nilpotent numerical-radius bound were already source-audited in WI-317--WI-318.

A targeted literature search around quantitative Riemann--Lebesgue bounds for Sobolev/BV families, autocorrelation moment bounds, IMS/localization semibounds, nilpotent translation estimates, and Weil-form localization found those ingredients individually but no source stating the `t^2/log t` adaptive-complexity threshold (27), the matching resonant construction (28)--(36), or their application to the source-exact scalar Weil-feedback obstruction. This is recorded as a novelty audit, **not** a claim of priority.

No external numerical certificate, conjectural zero statistic, RH assumption, wider Fourier support, or cross-line input is used. The result is an exact consequence of the WI-311 source identity plus classical harmonic analysis.

## 10. Evidence boundary and falsification controls

The theorem concerns exactly the source-exact **unit-window** localization architecture at fixed outer aperture and the same scalar-feedback premise as WI-317--WI-318. It does not constrain non-unit support families, a stronger theorem fed into localized pieces, matrix/vector state retained between pieces, or a different explicit-formula decomposition.

The lower bound (27) is a necessary complexity cost along the particular common recurrence sequence, not a sufficient condition for contraction and not a lower bound on every localizer used by an arbitrary successful proof. The matching family proves sharpness of this **recurrence obstruction** and of the continuous-error scale; it does not prove existence of a scalar bootstrap.

The logarithm in the threshold is load-bearing. A proof claiming a quadratic `M\gtrsim t^2` barrier from second-moment control alone would be false for the present argument: the resonant family (28) has only `M\asymp t^2/\log t` yet produces the order-one limit (36).

Likewise, the construction cannot be interpreted as new arithmetic information. At recurrent prime phases its arithmetic term simply returns to the fixed `g`-profile value (37); all new leverage comes from deliberately resonating the localizer spectrum with the test carrier in the singular archimedean kernel.