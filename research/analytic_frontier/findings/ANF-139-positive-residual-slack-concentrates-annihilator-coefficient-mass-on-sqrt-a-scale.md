# ANF-139 — positive residual slack concentrates annihilator coefficient mass on sqrt-A scale

**Status:** `EXACT-DERIVED + POSITIVE-TRANSLATION-CASCADE + BERNOULLI-CLOUD + SLACK-MOMENT-BUDGET + SUBGAUSSIAN-COEFFICIENT-MASS + DEPTH-UNIFORM-UNDER-RESIDUAL-SLACK + SOURCE-ENERGY-GATE`. `ANF-134` shows that the residual copy-rate slack `delta_d` controls the hard support geometry of the positive saddle-annihilator cascade, while `ANF-138` shows that every finite-depth conditioning loss can be absorbed by a sufficiently slow diagonal. There is a stronger probabilistic structure hidden in the same positive expansion: after normalizing its coefficients, the complete annihilator multiplier is exactly the characteristic function of a sum of independent Bernoulli translations.

This turns slack spend into a hierarchy of moment budgets. If `delta_D>0` is the residual slack after depth `D`, then the continuum second-moment budget of all annihilator shifts telescopes as

\[
\boxed{
\sum_{d=1}^{D}\theta_d
\sum_{j=1}^{J_{d-1}}\tau_{j,d-1}^{\,2}
\le
\frac{1}{8\log2}
\left(\frac1{\delta_D}-\frac1{\delta_0}\right).
}
\tag{1}
\]

At physical scale `A`, the integer powers are `m_{d,A}=floor(theta_d A)`. Since the floor only **removes** Bernoulli increments, the same estimate immediately gives the exact finite-scale variance proxy

\[
\boxed{
\Sigma_{D,A}
:=
\sum_{d=1}^{D}m_{d,A}
\sum_{j=1}^{J_{d-1}}\tau_{j,d-1}^{\,2}
\le
\frac{A}{8\log2}
\left(\frac1{\delta_D}-\frac1{\delta_0}\right).
}
\tag{2}
\]

If `X_{D,A}` denotes a translation drawn according to normalized expansion coefficients and `Y_{D,A}=X_{D,A}-E X_{D,A}`, then

\[
\boxed{
P(|Y_{D,A}|\ge t)
\le
2\exp\!\left(-\frac{2t^2}{\Sigma_{D,A}}\right).
}
\tag{3}
\]

Consequently, whenever

\[
\delta_D\ge\delta_*>0,
\tag{4}
\]

there is a constant `c_{gamma,delta_*}>0`, independent of `D`, such that

\[
\boxed{
P\left(|Y_{D,A}|\ge u\sqrt A\right)
\le2e^{-c_{\gamma,\delta_*}u^2}.
}
\tag{5}
\]

In particular every window `r_A` with

\[
\frac{r_A}{\sqrt A}\to\infty,
\qquad
r_A=o(A),
\tag{6}
\]

contains asymptotically all normalized coefficient mass after recentering at the barycenter, while every fixed macroscopic displacement satisfies

\[
\boxed{
P\left(|Y_{D,A}|\ge\varepsilon A\right)
\le2e^{-c_{\gamma,\delta_*}\varepsilon^2A}.
}
\tag{7}
\]

Thus positive residual slack controls considerably more than the `O(A)` hard span in `ANF-134`: **the bulk coefficient geometry is only `sqrt(A)` wide modulo a common translation, uniformly in cascade depth**. Any fatal effect that still relies on translations a positive fraction of `A` away from the barycenter must therefore be carried by an exponentially thin coefficient tail. The remaining difficulty is that coefficient mass is not source energy; exponentially thin positive tails may still be amplified coherently by the source kernel. This finding isolates that weighted large-deviation question without assuming it away.

## 1. The annihilator expansion is exactly a Bernoulli translation cloud

Use the `ANF-133`--`ANF-134` notation. At stage `d-1` the positive critical skeleton is

\[
\mathcal K_{d-1}
=\{\xi_{1,d-1},\ldots,\xi_{J_{d-1},d-1}\},
\]

and the positive annihilator is

\[
Q_{d-1}(\alpha)
=
\prod_{j=1}^{J_{d-1}}
\left(1+e^{-2\pi i\tau_{j,d-1}\alpha}\right),
\qquad
\tau_{j,d-1}=\frac1{2\xi_{j,d-1}}.
\tag{8}
\]

At scale `A`, layer `d` is implemented with

\[
m_{d,A}:=\lfloor\theta_dA\rfloor
\tag{9}
\]

copies of this annihilator. The complete annihilator multiplier through depth `D` is therefore

\[
\mathcal P_{D,A}(\alpha)
=
\prod_{d=1}^{D}
\prod_{j=1}^{J_{d-1}}
\left(1+e^{-2\pi i\tau_{j,d-1}\alpha}\right)^{m_{d,A}}.
\tag{10}
\]

Expand it with multiplicity,

\[
\mathcal P_{D,A}(\alpha)
=
\sum_{\omega}c_{\omega,D,A}e^{-2\pi i\omega\alpha},
\qquad
c_{\omega,D,A}\ge0.
\tag{11}
\]

Different subsets may produce the same physical translation `omega`; their multiplicities simply add in `c_omega`. The total coefficient mass is

\[
V_{D,A}
:=\sum_\omega c_{\omega,D,A}
=\mathcal P_{D,A}(0)
=2^{\sum_d m_{d,A}J_{d-1}}.
\tag{12}
\]

Normalize

\[
\mu_{D,A}
:=
\frac1{V_{D,A}}
\sum_\omega c_{\omega,D,A}\,\delta_\omega.
\tag{13}
\]

If `X_{D,A}` has law `mu_{D,A}`, then the product expansion gives the exact distributional identity

\[
\boxed{
X_{D,A}
\overset{d}=\
\sum_{d=1}^{D}
\sum_{j=1}^{J_{d-1}}
\sum_{\ell=1}^{m_{d,A}}
\tau_{j,d-1}B_{d,j,\ell},
}
\tag{14}
\]

where all `B_{d,j,ell}` are independent Bernoulli variables with parameter `1/2`. No distinctness assumption on the resulting physical translations is needed.

In particular,

\[
\bar\omega_{D,A}:=E X_{D,A}
=
\frac12
\sum_{d,j}m_{d,A}\tau_{j,d-1},
\tag{15}
\]

and

\[
\boxed{
\operatorname{Var}(X_{D,A})
=
\frac14\Sigma_{D,A}.
}
\tag{16}
\]

There is also an exact Fourier identity. Since

\[
\frac{1+e^{-2\pi i\tau\alpha}}2
=e^{-\pi i\tau\alpha}\cos(\pi\tau\alpha),
\]

one has

\[
\boxed{
e^{2\pi i\alpha\bar\omega_{D,A}}
\frac{\mathcal P_{D,A}(\alpha)}{\mathcal P_{D,A}(0)}
=
\prod_{d,j}
\cos(\pi\tau_{j,d-1}\alpha)^{m_{d,A}}
=
E e^{-2\pi i\alpha(X_{D,A}-\bar\omega_{D,A})}.
}
\tag{17}
\]

So the cosine penalties that shape the cascade pressure are literally the centered characteristic function of its positive coefficient cloud.

## 2. Slack spend controls every shift moment

Write

\[
s_d:=\delta_{d-1}-\delta_d
=2\theta_dJ_{d-1}\log2
\tag{18}
\]

for the exact continuum slack spend of layer `d`. `ANF-134` gives every historical annihilator shift the bound

\[
\tau_{j,d-1}
\le\frac1{2\delta_{d-1}}.
\tag{19}
\]

For `p>1`, equations (18)--(19) imply

\[
\begin{aligned}
\theta_d
\sum_{j=1}^{J_{d-1}}\tau_{j,d-1}^{\,p}
&\le
\frac{s_d}{2^{p+1}\log2}\,\delta_{d-1}^{-p}\\
&\le
\frac{1}{2^{p+1}(p-1)\log2}
\left(
\delta_d^{1-p}-\delta_{d-1}^{1-p}
\right).
\end{aligned}
\tag{20}
\]

The second line is just the integral comparison

\[
(\delta_{d-1}-\delta_d)\delta_{d-1}^{-p}
\le
\int_{\delta_d}^{\delta_{d-1}}x^{-p}\,dx.
\tag{21}
\]

Summing telescopes:

\[
\boxed{
\sum_{d=1}^{D}\theta_d
\sum_j\tau_{j,d-1}^{\,p}
\le
\frac{
\delta_D^{1-p}-\delta_0^{1-p}
}{2^{p+1}(p-1)\log2},
\qquad p>1.
}
\tag{22}
\]

For `p=1` the corresponding logarithmic limit is

\[
\boxed{
\sum_{d=1}^{D}\theta_d
\sum_j\tau_{j,d-1}
\le
\frac1{4\log2}
\log\frac{\delta_0}{\delta_D}.
}
\tag{23}
\]

Equation (23) is the coefficient-moment analogue of the hard-span law in `ANF-134`; equation (22) is new information because support diameter alone gives no concentration. Taking `p=2` gives exactly (1).

At finite scale there is no floor penalty in the upper bound. From

\[
m_{d,A}=\lfloor\theta_dA\rfloor\le\theta_dA
\tag{24}
\]

and (1),

\[
\Sigma_{D,A}
\le
A\sum_d\theta_d\sum_j\tau_{j,d-1}^2
\le
\frac{A}{8\log2}
\left(\frac1{\delta_D}-\frac1{\delta_0}\right),
\tag{25}
\]

which is (2). This is depth-uniform as soon as the residual slack is: chamber proliferation and fixed-depth conditioning constants do not appear at all.

The first moment satisfies an analogous centered-geometry law. Combining (15), (23), and the floor inequality gives

\[
\frac{\bar\omega_{D,A}}A
\le
\frac1{8\log2}\log\frac{\delta_0}{\delta_D}.
\tag{26}
\]

Thus positive slack controls both the barycentric displacement and the fluctuation scale, but in different currencies: logarithmic slack ratio for the mean and inverse-slack difference for the variance proxy.

## 3. The coefficient cloud is subgaussian on the square-root scale

Set

\[
Y_{D,A}:=X_{D,A}-\bar\omega_{D,A}.
\]

Each centered Bernoulli increment has the form

\[
Z=\tau(B-1/2),
\]

and its moment-generating function is exactly

\[
E e^{\lambda Z}
=\cosh\frac{\lambda\tau}{2}.
\tag{27}
\]

The elementary inequality

\[
\cosh u\le e^{u^2/2}
\tag{28}
\]

gives, by independence,

\[
E e^{\lambda Y_{D,A}}
\le
\exp\left(\frac{\lambda^2}{8}\Sigma_{D,A}\right).
\tag{29}
\]

Markov's inequality and optimization at `lambda=4t/Sigma_{D,A}` give

\[
P(Y_{D,A}\ge t)
\le
\exp\left(-\frac{2t^2}{\Sigma_{D,A}}\right).
\tag{30}
\]

Apply the same estimate to `-Y_{D,A}` to obtain (3).

If `delta_D>=delta_*>0`, equation (2) gives

\[
\Sigma_{D,A}
\le
\frac{A}{8\log2}
\left(\frac1{\delta_*}-\frac1{\delta_0}\right)
=:C_{\gamma,\delta_*}A,
\tag{31}
\]

with a constant independent of `D`. Equations (3) and (31) prove (5)--(7). Thus the normalized coefficient distribution has a Gaussian-width bulk even though its hard positive support can still have linear diameter.

A common translation of every physical copy changes the Fourier sum only by a unit-modulus phase and hence does not change the source energy. Therefore the relevant statement is naturally centered: modulo a source-invisible common translation, almost all coefficient mass sits in a `sqrt(A)`-scale cloud.

## 4. Positive limiting slack makes the coefficient law genuinely arbitrary-depth

Suppose the infinite nested cascade of `ANF-138` has

\[
\delta_\infty:=\inf_d\delta_d>0.
\tag{32}
\]

Choose any `0<delta_*<delta_infinity`. Then (4) holds at **every finite depth**, so (5)--(7) are uniform in `D` before any diagonal argument is chosen. Consequently they remain valid for every finite-valued depth law `D=D(A)`, however quickly it grows, as a statement about the annihilator coefficient multiplier itself.

The slow diagonal of `ANF-138` is still needed for a different reason: it is what turns those finite-depth multipliers into a physical family whose Montgomery--Taylor source asymptotics and near-extremizer properties survive while `D(A)->infinity`. But once such a physical diagonal is selected, no additional chamber-count or conditioning hypothesis is needed for coefficient concentration. Positive residual slack alone supplies it.

This is stronger than merely saying that the physical span remains `O(A)`. A support interval of linear width could carry order-one coefficient mass at both ends. Equations (5)--(7) exclude that geometry: at positive residual slack, macroscopic excursions from the barycenter have exponentially small normalized positive mass.

If instead `delta_d->0`, the variance budget (1) is allowed to diverge like `1/delta_D`. Slow diagonalization can make that divergence arbitrarily slow in `A`, exactly as `ANF-138` can slow the notch collapse, but it cannot manufacture a depth-uniform `sqrt(A)` constant from a vanishing slack. Thus the same scalar dichotomy remains visible in coefficient geometry.

## 5. Adversarial boundary: coefficient concentration is not source concentration

The conclusion must not be promoted to source-negligible trimming. The normalized law `mu_{D,A}` measures the **positive expansion coefficients** of the translation multiplier. The Montgomery--Taylor source is a quadratic spectral functional of the coherent sum of all translated packets. A set carrying exponentially small normalized coefficient mass can still have exponentially many absolute copies because the total unsigned mass itself is exponential in `A`; coherent spectral alignment may then make that tail source-relevant.

Accordingly, (7) does not contradict `ANF-100`, which requires linear physical diameter for actual near-extremizers, and it does not subsume the source-negligible trimming statements around `ANF-103`. The full support can remain linear even when almost all coefficient mass is concentrated around its barycenter, and the rare support extremes are exactly where a coherence-amplified escape could hide.

The finding also does not prove `delta_infinity>0`. It is conditional on the positive-residual-slack branch already isolated by `ANF-138`. Its role is to sharpen what that branch would mean geometrically: not only a fixed dark notch and bounded normalized span, but a square-root-scale bulk law for the entire positive annihilator coefficient cloud.

This leaves a concrete next gate. One should either prove a **source-weighted** analogue of (7), strong enough to show that coefficient tails outside `o(A)` cannot carry macroscopic source, or construct an explicit coherence mechanism where an exponentially thin coefficient tail nevertheless carries order-one source energy. Either outcome would materially advance the residual-slack branch.

## 6. Prior-art boundary

The probabilistic ingredients are classical. Products of cosine factors are standard characteristic functions of Bernoulli sums and sit next to the classical Riesz-product viewpoint; subgaussian concentration for sums of bounded independent variables is the content of the classical Hoeffding/Chernoff theory. A directed prior-art audit found no need to import those theorems: equations (27)--(30) give the complete concentration proof from the elementary inequality `cosh u<=exp(u^2/2)`.

The research-specific content is instead the coupling to the analytic-frontier cascade: the exact identification (14), the slack-spend moment hierarchy (22)--(23), and especially the telescoping second-moment law (1), which converts the scalar residual copy-rate budget into a depth-uniform `sqrt(A)` coefficient geometry. No external theorem is load-bearing, so `SOURCES.md` is unchanged and no novelty claim is made for the classical Bernoulli concentration mechanism itself.

**Consequence for `analytic_frontier`.** In the `delta_infinity>0` branch, the positive annihilator cascade cannot place a macroscopic fraction of its coefficient mass throughout its full `O(A)` support. After an irrelevant common translation, its bulk lives on the mesoscopic `sqrt(A)` scale. A fatal near-extremizer in this branch must therefore exploit **source amplification of exponentially thin coefficient tails**, not merely broad positive coefficient geometry. The scalar slack problem and the weighted-tail problem are now cleanly separated.