# RE-213 — Adaptive Kaiser tests close the separated vertical endpoint at unit rate

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + ADAPTIVE-KAISER-WINDOW + WEIGHTED-PRIMITIVE-LOWER-BOUND + ORDINARY-PRIME-SOURCE + CHEBYSHEV-PREFIX-COERCIVITY + KV-BARRIER + ENDPOINT-CLOSURE + POSITIVE-TEST-METHOD-BOUNDARY`.

**Parent findings:** RE-209, RE-212.

`RE-212` proved that every fixed exponent below one is available in the positive compact-test coercion: after fixing `eta>0`, one fixes a Kaiser--Bessel parameter `beta=beta(eta)` and obtains

\[
\log R\ge ((1-\eta)+o(1))HT.
\]

That was enough to exclude `T_Q=c\log Q` for every fixed `c>1/(2H)`, but it deliberately left the endpoint `c=1/(2H)` open because no uniformity was claimed when `beta` grows with `Q`.

The missing uniformity can be made explicit. The Kaiser tail integrals used in `RE-212` admit bounds with constants independent of `beta`; this permits `beta` to grow slowly with `A:=HT`. Choosing

\[
\beta=\sqrt{A\log A},
\qquad
n=\left\lfloor\frac{A}{\beta}\right\rfloor,
\]

gives the quantitative generic bound

\[
\boxed{
\log R\ge A-O\!\left(\sqrt{A\log A}\right).
}
\tag{1}
\]

For the ordinary-prime separated Euler repair of `RE-209`, with `T_Q=O(\log Q)`, the loss in (1) is

\[
O\!\left(\sqrt{\log Q\,\log\log Q}\right)
=o(V(Q)),
\qquad
V(Q)=\frac{(\log Q)^{3/5}}{(\log\log Q)^{1/5}}.
\]

Hence preserving **every fixed Korobov--Vinogradov envelope** requires the sharp near-endpoint necessary condition

\[
\boxed{
\frac{\frac12\log Q-H T_Q}{V(Q)}\longrightarrow+\infty.
}
\tag{2}
\]

In particular, if `T_Q=c\log Q` with fixed `c`, then

\[
\boxed{
c<\frac1{2H}}
\tag{3}
\]

is necessary. Equality is now excluded. For the current corridor `H=\log 8`, the separated ordinary-prime `{0,1,2}` architecture therefore cannot hide a selector-scale packet at

\[
\boxed{
c\ge \frac1{2\log8}=0.2404491734\ldots .}
\tag{4}
\]

There is also a matching generic method boundary. If `w` is any nonnegative probability density supported on `[-1,1]` and

\[
F(x)=\int_{-1}^{1}e^{-ixt}w(t)\,dt,
\qquad
M(a):=\sup_{|x|\ge a}|F(x)|,
\]

then a Chebyshev/Remez limiting argument gives

\[
\boxed{M(a)\ge \operatorname{sech}a.}
\tag{5}
\]

Consequently the window functional introduced after `RE-211`,

\[
\Gamma(w)=
\sup_{a>0}
\frac{-\log M(a)}{a},
\]

satisfies `Gamma(w)<=1`; together with the Kaiser lower construction from `RE-212`,

\[
\boxed{
\sup_w\Gamma(w)=1.
}
\tag{6}
\]

Thus one is the exact supremal exponential coefficient for the positive compact-window tail functional. This does **not** say that every coercive argument for the separated source is limited to one, but it closes the explicit window-extremal subproblem left by `RE-212` and shows that the endpoint improvement above uses the full exponential coefficient available to this representation.

## 1. The Kaiser tail estimates are uniform in the growing parameter

Use the normalized continuous Kaiser--Bessel density and transform from `RE-212`:

\[
w_\beta(t)=
\frac{\beta}{2\sinh\beta}
I_0\!\left(\beta\sqrt{1-t^2}\right),
\qquad |t|\le1,
\]

and, for `x>=beta`,

\[
\Phi_\beta(x)
=C_\beta\frac{\sin y}{y},
\qquad
y:=\sqrt{x^2-\beta^2},
\qquad
C_\beta:=\frac{\beta}{\sinh\beta}.
\tag{7}
\]

The point omitted in `RE-212` is that the tail norms can be bounded **uniformly in `beta`**. Since

\[
\frac{dx}{dy}=\frac{y}{\sqrt{y^2+\beta^2}}\le1,
\]

for every integer `n>=2`,

\[
\begin{aligned}
\int_\beta^\infty |\Phi_\beta(x)|^n\,dx
&\le
C_\beta^n
\int_0^\infty |\operatorname{sinc}y|^n\,dy
\\
&\le 2C_\beta^n.
\end{aligned}
\tag{8}
\]

For the derivative, monotonicity of the change of variables removes the Jacobian exactly from total variation:

\[
\int_\beta^\infty
\left|\frac{d}{dx}\Phi_\beta(x)^n\right|dx
=
 nC_\beta^n
\int_0^\infty
|\operatorname{sinc}y|^{n-1}
|\operatorname{sinc}'y|\,dy.
\tag{9}
\]

On `[0,1]`, `sinc'` is uniformly bounded. For `y>=1`,

\[
|\operatorname{sinc}y|\le y^{-1},
\qquad
|\operatorname{sinc}'y|\le y^{-1}+y^{-2}\le2y^{-1}.
\]

Therefore the last integral in (9) is bounded by an absolute constant for all `n>=2`, and

\[
\boxed{
\int_\beta^\infty |(\Phi_\beta^n)'(x)|dx
\ll nC_\beta^n
}
\tag{10}
\]

with no hidden dependence on `beta`.

Now return to the generic separated spectral-gap setup. Let `nu` be supported on `[H,\infty)` and suppose

\[
\sup_{|t|\le T}|1-\widehat\nu(t)|\le\epsilon,
\qquad \epsilon<1.
\tag{11}
\]

Set

\[
G(L)=\int_{[H,L]}e^u\,d\nu(u),
\qquad
R=\sup_{L\ge H}e^{-L}|G(L)|,
\qquad
A:=HT.
\tag{12}
\]

For a parameter `beta>=1`, choose

\[
n=\left\lfloor\frac{A}{\beta}\right\rfloor,
\tag{13}
\]

and assume `n>=2`. As in `RE-212`, scale `w_beta` to support `[-T/n,T/n]` and take its `n`-fold convolution. Its transform is

\[
\phi_n(L)=\Phi_\beta(LT/n)^n.
\tag{14}
\]

Because `n<=A/beta`, every `L>=H` has `LT/n>=beta`, so (8)--(10) apply over the full repair support. Scaling back from `x=LT/n` gives

\[
\int_H^\infty |\phi_n'(L)|dL
\ll nC_\beta^n,
\tag{15}
\]

and

\[
\int_H^\infty |\phi_n(L)|dL
\ll \frac nT C_\beta^n.
\tag{16}
\]

For fixed `H` and `beta>=1`, `n/T<=H/beta<=H`, so

\[
\boxed{
\int_H^\infty
(|\phi_n'|+|\phi_n|)dL
\ll_H nC_\beta^n.
}
\tag{17}
\]

The implied constant is independent of both `beta` and `n`.

Pairing (11) against the nonnegative probability test and integrating by parts exactly as in `RE-209` yields

\[
1-\epsilon
\le
R\int_H^\infty(|\phi_n'|+|\phi_n|)dL.
\]

Hence

\[
\boxed{
\log R
\ge
n\log\frac{\sinh\beta}{\beta}
-\log n-O_H(1).
}
\tag{18}
\]

This is the uniform form that permits `beta` to move with the asymptotic scale.

## 2. An adaptive parameter reaches unit rate with sub-KV loss

For large `beta`,

\[
\log\frac{\sinh\beta}{\beta}
=
\beta-\log(2\beta)+O(e^{-2\beta}).
\tag{19}
\]

Since `n>=A/beta-1`, (18) and (19) imply

\[
\log R
\ge
A
-O\!\left(
\frac{A\log(2\beta)}{\beta}
+\beta+\log A
\right).
\tag{20}
\]

Take

\[
\boxed{
\beta=\sqrt{A\log A}.
}
\tag{21}
\]

Then `beta=o(A)`, so `n->infinity`, and (20) becomes

\[
\boxed{
\log R
\ge
A-O\!\left(\sqrt{A\log A}\right).
}
\tag{22}
\]

This proves (1). The precise choice in (21) is not claimed optimal; it is chosen because the resulting loss is already far below the arithmetic KV scale relevant downstream.

For `A=HT_Q=O(\log Q)`,

\[
\sqrt{A\log A}
=O\!\left(\sqrt{\log Q\log\log Q}\right).
\tag{23}
\]

Comparing with

\[
V(Q)=\frac{(\log Q)^{3/5}}{(\log\log Q)^{1/5}},
\]

we have

\[
\frac{\sqrt{\log Q\log\log Q}}{V(Q)}
=
(\log Q)^{-1/10}(\log\log Q)^{7/10}
\longrightarrow0.
\tag{24}
\]

Thus the adaptive-window loss is `o(V(Q))`.

## 3. Ordinary-prime pullback closes the endpoint

Use the same arithmetic architecture and normalization as `RE-209`--`RE-212`: a selector-scale local packet near `X_0=2Q`, followed only after the fixed logarithmic gap `H` by ordinary-prime edits with coefficients in `{-1,+1}`, exact Euler discrepancy `o(d_Q)` uniformly on `|t|<=T_Q`, and

\[
d_Q=\frac1{\sqrt Q\log Q}.
\]

Nothing in the reduction from exact Euler atoms to the first-harmonic measure depends on the test parameter. The local packet collapses to the unit atom uniformly on the observed interval, and the total normalized prime-power error remains `o(1)` over all remote shells. Because the test in Section 1 is always a nonnegative probability density supported on `[-T_Q,T_Q]`, the same uniform spectral discrepancy may be paired against the `Q`-dependent adaptive test without additional loss.

The weighted primitive remains exactly the scaled signed prime-count prefix. Repeating the `RE-209` partial-summation pullback with (22) gives, for `H T_Q->infinity`,

\[
\boxed{
\sup_{x\ge X_0e^H}
\frac{|\Delta\vartheta_Q(x)|}{x}
\ge
Q^{-1/2}
\exp\!\left(
H T_Q
-O\!\left(\sqrt{H T_Q\log(H T_Q)}\right)
\right).
}
\tag{25}
\]

Assume now `T_Q=O(\log Q)` and fidelity to every fixed KV envelope,

\[
|\Delta\vartheta_Q(x)|
=o\!\left(xe^{-bV(x)}\right)
\qquad
\text{for every fixed }b>0
\tag{26}
\]

through every affected scale. Since `V` is eventually increasing, the scale supplied by (25) also satisfies the upper bound `o(e^{-bV(Q)})` after division by `x`. By (23)--(24), (25) is

\[
\frac{|\Delta\vartheta_Q(x)|}{x}
\ge
\exp\!\left(
-\frac12\log Q+H T_Q-o(V(Q))
\right).
\tag{27}
\]

If

\[
D_Q:=\frac12\log Q-H T_Q
\]

did not satisfy `D_Q/V(Q)->infinity`, then along a subsequence `D_Q<=CV(Q)` for some fixed `C`. Choosing any fixed `b>C+1` in (26) would contradict (27). Therefore (2) is necessary.

At the formerly open endpoint

\[
T_Q=\frac{\log Q}{2H},
\]

we have `D_Q=0`, so (2) fails maximally. The endpoint is excluded. More generally, the continuum window must remain below `\frac{1}{2H}\log Q` by an amount `\omega(V(Q))`, not merely by an unspecified `o(\log Q)` margin.

The constructive range of `RE-208`, `c<1/(24H\log2)`, is unchanged. Thus the result closes the coercive endpoint but does not close the large remaining constructive/coercive constant gap.

## 4. A Chebyshev/Remez limit pins the compact-window tail exponent at one

The coefficient one in (22) is not an accident of Kaiser--Bessel. There is a generic upper bound for the uniform tail attenuation of any positive compact window.

Let `w` be a nonnegative probability density on `[-1,1]` and

\[
F(z)=\int_{-1}^{1}e^{-izt}w(t)dt.
\tag{28}
\]

Then `F(0)=1`, `|F(x)|<=1` on the real axis, and

\[
|F(x+iy)|\le e^{|y|}.
\tag{29}
\]

Fix `a>0` and write

\[
M(a)=\sup_{|x|\ge a}|F(x)|.
\tag{30}
\]

We prove (5) by reducing to the classical exterior Chebyshev extremal problem.

Fix `delta>0`. For large `R>a`, set

\[
g_R(z)=F(Rz).
\]

On the Bernstein ellipse with parameter `e^s`, the largest imaginary part is `sinh s`; hence (29) gives

\[
\max_{E_s}|g_R|\le e^{R\sinh s}.
\tag{31}
\]

Choose a fixed small `s>0` such that

\[
\sinh s<(1+\delta)s.
\]

The standard Chebyshev-coefficient estimate on `E_s` shows that the degree

\[
N_R=\lceil(1+\delta)R\rceil
\]

Chebyshev truncation `P_R` of `g_R` satisfies

\[
\|g_R-P_R\|_{[-1,1]}
\le
C_s\exp\!\left(
R\sinh s-N_Rs
\right)
=:\varepsilon_R,
\tag{32}
\]

with `epsilon_R->0` exponentially. Define

\[
p_R(x)=P_R(x/R).
\]

Then `p_R` has degree at most `N_R` and approximates `F` uniformly on `[-R,R]` within `epsilon_R`.

Evenize:

\[
e_R(x)=\frac{p_R(x)+p_R(-x)}2=q_R(x^2),
\]

where `deg q_R=m_R<=N_R/2`. At the origin,

\[
|q_R(0)|=|p_R(0)|\ge1-\varepsilon_R.
\tag{33}
\]

For `a<=|x|<=R`, both `x` and `-x` lie in the tail, so

\[
|e_R(x)|\le M(a)+\varepsilon_R.
\tag{34}
\]

Thus `q_R` is bounded by `M(a)+epsilon_R` on `[a^2,R^2]`. The classical exterior Chebyshev inequality for a degree-`m_R` polynomial, applied at the point `0` outside that interval, gives

\[
1-\varepsilon_R
\le
(M(a)+\varepsilon_R)
T_{m_R}\!\left(
\frac{R^2+a^2}{R^2-a^2}
\right).
\tag{35}
\]

For complex coefficients, rotate `q_R(0)` to be positive real and apply the real Chebyshev inequality to the real part; (35) is unchanged. Since

\[
\operatorname{arccosh}\!\left(
\frac{R^2+a^2}{R^2-a^2}
\right)
=2\operatorname{artanh}(a/R),
\tag{36}
\]

and `2m_R<=N_R`, the Chebyshev factor in (35) is at most

\[
\cosh\!\left(N_R\operatorname{artanh}(a/R)\right).
\]

Letting `R->infinity` gives

\[
1\le M(a)\cosh((1+\delta)a).
\]

Finally `delta->0`, proving

\[
\boxed{
M(a)\ge\frac1{\cosh a}.
}
\tag{37}
\]

Therefore

\[
\frac{-\log M(a)}a
\le
\frac{\log\cosh a}{a}<1,
\]

and taking the supremum over `a` gives `Gamma(w)<=1`. `RE-212` supplies windows with `Gamma` arbitrarily close to one, so (6) follows.

There is also a direct connection to the actual integration-by-parts norm used by `RE-209`. For any admissible density whose transform tends to zero and whose derivative tail has finite variation,

\[
\int_a^\infty |F'(x)|dx
\ge
\sup_{x\ge a}|F(x)|
=M(a)
\ge
\operatorname{sech}a.
\tag{38}
\]

(The equality of positive- and two-sided tail suprema follows from `F(-x)=\overline{F(x)}`.) If the derivative variation is infinite, the test is unusable for obtaining a stronger integration-by-parts estimate anyway. Hence the denominator in the positive compact-test argument cannot have an exponential coefficient better than one. Adaptive Kaiser reaches that coefficient up to a sublinear loss.

## 5. Representation audit, prior-art boundary, and falsification checks

The source-side invariant is unchanged from `RE-209`: continuum hiding after a fixed logarithmic gap forces a weighted signed primitive, which for ordinary-prime Euler edits is exactly a scaled signed prime-count prefix and therefore a Chebyshev-prefix excursion. The Kaiser parameter is only a coordinate in the positive compact spectral test. Allowing it to grow does not alter the source model, multiplicity constraint, selector debt, or KV target.

The harmonic ingredients are generic. Kaiser--Bessel windows are classical; polynomial approximation of Bernstein-space entire functions and Chebyshev/Remez exterior extremality are classical approximation theory. Broad prior-art search found the expected literature on pointwise Remez inequalities and Bernstein spaces, but no source-specific statement coupling the unit tail exponent to the ordinary-prime Euler/KV repair problem. No external theorem beyond these standard, explicitly reproduced ingredients is load-bearing here, so `SOURCES.md` needs no new anchor.

Several possible failure modes were checked explicitly.

First, `RE-212` hid constants depending on fixed `beta`; equations (8)--(10) remove that dependence and are the essential new uniformity. Second, the floor in `n=floor(A/beta)` costs `O(beta)`, which is included in (20) and remains `o(V(Q))` under (21). Third, `beta` grows while `n` also tends to infinity, so convolution restores the Fourier-tail integrability needed for integration by parts despite the endpoint jump of the base Kaiser density. Fourth, the arithmetic spectral error is uniform on the full interval, so pairing against a `Q`-dependent probability test does not magnify it. Fifth, (37) is a generic method boundary only for positive compact-window tail attenuation; it does not rule out a fundamentally different coercive representation, a signed test with independently controlled norm, or an argument not based on the `RE-209` integration-by-parts architecture.

Finally, (2)--(4) remain statements about the **separated repair architecture**. They do not prove Robin's inequality, do not exclude repairs without a fixed pre-repair gap, and do not show that a hypothetical Robin counterexample must expose the required continuum vertical Euler data.

## Research consequence

The obstruction-side window problem left by `RE-212` is now closed at the exponential-coefficient level. The unit rate is both achievable up to `o(V(Q))` loss by an adaptive Kaiser family and unbeatable for the positive compact-window tail functional. As a result, the separated KV architecture has the sharp near-endpoint necessary condition (2), and the previously unresolved fixed endpoint `c=1/(2H)` is impossible.

For `H=\log8`, the current two-sided range is therefore

\[
0<c<0.0289079\ldots
\quad\text{constructed},
\qquad
c\ge0.2404491734\ldots
\quad\text{excluded within the separated KV architecture}.
\]

Further obstruction progress cannot come from another ordinary positive compact window merely having better uniform sidelobes: the exponential coefficient one is already optimal. The meaningful remaining directions are to improve the subexponential loss or, more importantly, to leave this positive-test representation altogether. On the constructive side the same dual target remains: control the signed weighted prime-count prefix directly rather than paying with absolute coefficient variation.
