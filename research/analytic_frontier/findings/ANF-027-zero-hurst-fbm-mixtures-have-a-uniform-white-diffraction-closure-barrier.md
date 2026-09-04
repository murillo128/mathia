# ANF-027 — zero-Hurst fBm mixtures have a uniform white-diffraction closure barrier

**Status:** `LITERATURE+DERIVED + EXACT-WEAK-CLOSURE + NEGATIVE/OBSTRUCTION + DIFFRACTION-DUAL`. `ANF-025` excludes every fixed fractional-Brownian Palm-lattice regularization from the Montgomery--Taylor order interval, while `ANF-026` identifies the fixed-scale `H\downarrow0` boundary and excludes arbitrary scale mixtures **after** that boundary is taken. The remaining nonuniform loophole was to let the Hurst index and the scale distribution move simultaneously before taking a weak-* limit.

That loophole is also closed. Let

\[
a:=a_{\rm MT}=C_{\rm MT}^{-1}=0.753296067856070\ldots,
\qquad
\nu_a=a\,\delta_0+a|h|\,dh
\]

on `(-1,1)`. For `0<H<1` and intensity `rho>0`, let `mu_{H,rho}` denote the normalized full diffraction measure of the one-dimensional Palm lattice regularized by fBm of Hurst index `H`, after spatial dilation to intensity `rho`. Let `pi_j` be arbitrary probability laws on pairs `(H,rho)` and set

\[
\overline\mu_j
:=
\int \mu_{H,\rho}\,d\pi_j(H,\rho).
\]

Assume only that the Hurst coordinate collapses to zero in probability,

\[
H\longrightarrow0
\qquad\text{under }\pi_j.
\tag{1}
\]

Then **no vague subsequential limit** of `overline mu_j` on `(-1,1)` can satisfy

\[
\boxed{\overline\mu\le\nu_a.}
\tag{2}
\]

No relation between `H` and `rho` is required. In particular this excludes deterministic double scalings `H_j\downarrow0`, `rho_j\downarrow0`, mixtures whose scale law itself collapses to zero, and mixtures in which positive, vanishing and moderately large scales coexist while `H\to0`.

The mechanism has two exact pieces. First, **dilution is uniformly Poissonian at the diffraction level**: for every `0\le H\le1/2`,

\[
\boxed{
\rho\downarrow0
\quad\Longrightarrow\quad
\mu_{H,\rho}\longrightarrow dh
}
\tag{3}
\]

in tempered distributions, uniformly in `H`. Thus taking the scale to zero does not create a new hyperuniform boundary; it destroys the correlations and leaves the unit self-scattering background. Second, on scales bounded away from zero the `H\downarrow0` convergence from `ANF-026` is uniform on compact scale intervals. Together these facts make the extended zero-Hurst family compact enough to pass through arbitrary moving mixtures. The same one-frequency budget used in `ANF-026` then gives a uniform contradiction with a robust margin.

## 1. Exact fBm structure factor and scaled autocorrelation

Thomassey--Lachièze-Rey--Shapira prove that the Palm lattice regularized by one-dimensional fBm has an absolutely continuous Bartlett spectrum away from the origin and give the exact lattice specialization of their structure-factor formula. In the Mathia Fourier convention `e^{-2 pi i h x}`, the unit-intensity density is

\[
S_H(q)
=
\sum_{n\in\mathbb Z}
\exp\!\left(-2\pi^2q^2|n|^{2H}\right)
 e^{-2\pi i qn},
\qquad q\ne0.
\tag{4}
\]

After dilation to intensity `rho`, the full normalized diffraction is

\[
\boxed{
\mu_{H,\rho}
=
\rho\,\delta_0
+
S_H(h/\rho)\,dh.
}
\tag{5}
\]

The corresponding normalized Palm autocorrelation is more useful for limits. If

\[
g_v(x)=\frac1{\sqrt{2\pi v}}e^{-x^2/(2v)},
\]

then

\[
\boxed{
\gamma_{H,\rho}
=
\delta_0
+
\sum_{n\in\mathbb Z\setminus\{0\}}
\rho\,
 g_{|n|^{2H}}(\rho x-n)\,dx.
}
\tag{6}
\]

Indeed the Palm displacement of label `n` is `(n+B_n^H)/rho`, and `B_n^H` is centered Gaussian with variance `|n|^{2H}`. Fourier transformation of (6) gives (5), including the forward atom of mass `rho`.

A useful uniform sanity check already follows from (4). At the half-cell frequency `q=1/2`,

\[
S_H(1/2)
=1+2\sum_{n\ge1}(-1)^n
 e^{-(\pi^2/2)n^{2H}}.
\]

The summands decrease in modulus, so the alternating-series bound gives

\[
\boxed{
S_H(1/2)
\ge
1-2e^{-\pi^2/2}
=0.985616233288347\ldots
}
\tag{7}
\]

uniformly for every `H>0`. Thus an individual profile satisfying the necessary forward-atom condition `rho<=a` already violates the diffuse target at `h=rho/2`. This does **not** by itself settle weak limits, because that violating frequency moves to zero when `rho\to0`; Sections 2--4 show why the violation cannot disappear through a singular mixture.

## 2. Dilution sends the whole small-Hurst family to white diffraction

Extend the notation in (6) to `H=0` by setting `|n|^{2H}=1` for `n\ne0`. This is exactly the zero-Hurst autocorrelation derived in `ANF-026` before Fourier transformation.

Let `psi` be a Schwartz test function. For `n>=1`, the absolute contribution of the `n`th term of (6) is

\[
I_{n,H,\rho}
:=
\int_{\mathbb R}
|\psi(x)|
\frac{\rho}{\sqrt{2\pi}\,n^H}
\exp\!\left(
-\frac{(\rho x-n)^2}{2n^{2H}}
\right)dx.
\tag{8}
\]

Put `z=rho x`. Split the integral into `|z|>=n/2` and `|z|<n/2`. For any fixed `M>2`, Schwartz decay gives on the first region

\[
|\psi(z/\rho)|
\le C_{\psi,M}\left(\frac{2\rho}{n}\right)^M,
\]

hence

\[
I^{(1)}_{n,H,\rho}
\le C_{\psi,M}\rho^M n^{-M}.
\tag{9}
\]

On the second region, `|z-n|>=n/2`. For `0\le H\le1/2`,

\[
\frac1{n^H}
\exp\!\left(-\frac{(z-n)^2}{2n^{2H}}\right)
\le
\exp(-n/8).
\]

Since

\[
\int_{|z|<n/2}|\psi(z/\rho)|\,dz
\le\rho\|\psi\|_{L^1},
\]

we obtain

\[
I^{(2)}_{n,H,\rho}
\le C_\psi\rho e^{-n/8}.
\tag{10}
\]

The negative labels obey the same estimate. Summing (9)--(10) yields, uniformly for `0\le H\le1/2` and `0<rho<=1`,

\[
\boxed{
\left|
\langle\gamma_{H,\rho}-\delta_0,\psi\rangle
\right|
\le C_\psi\rho.
}
\tag{11}
\]

After Fourier transformation,

\[
\boxed{
\sup_{0\le H\le1/2}
\left|
\langle\mu_{H,\rho}-dh,\varphi\rangle
\right|
\le C_\varphi\rho
}
\tag{12}
\]

for every Schwartz frequency test `varphi`. This proves the uniform dilute limit (3).

The interpretation is simple but important for the open boundary of `ANF-026`: if `rho_H\to0`, the typical pair separations and the fBm displacement scale both escape every fixed spatial window. The normalized autocorrelation retains only its self atom `delta_0`, whose Fourier transform is **Lebesgue measure**, not another linear-cusp hyperuniform profile.

## 3. The `H=0` boundary is jointly continuous on bounded scale sets

For fixed positive `rho`, `ANF-026` proved

\[
\mu_{H,\rho}\longrightarrow\mu_{0,\rho}
\qquad(H\downarrow0),
\tag{13}
\]

where

\[
\boxed{
\mu_{0,\rho}
=
\rho\sum_{k\in\mathbb Z}e^{-2\pi^2k^2}\delta_{k\rho}
+
\left(1-e^{-2\pi^2(h/\rho)^2}\right)dh.
}
\tag{14}
\]

Define also

\[
\boxed{\mu_{0,0}:=dh.}
\tag{15}
\]

The convergence is in fact joint at the corner needed for moving mixtures. For every `M<infinity` and every Schwartz test `varphi`,

\[
\boxed{
\sup_{0<\rho\le M}
\left|
\langle\mu_{H,\rho}-\mu_{0,\rho},\varphi\rangle
\right|
\longrightarrow0
\qquad(H\downarrow0).
}
\tag{16}
\]

To see this, fix a small `delta>0`. On `0<rho<=delta`, both `mu_{H,rho}` and `mu_{0,rho}` are within `O_varphi(delta)` of `dh` by (12), uniformly for `H<=1/2`. On the compact scale interval `delta<=rho<=M`, use (6). For each fixed label `n`, the Gaussian term converges continuously as `H\to0`, uniformly in `rho` on that compact interval. The same Gaussian-tail split used in `ANF-026` supplies a summable majorant independent of small `H` and `rho in [delta,M]` (for instance, once `H<=1/4`, the near-origin tail has `exp(-c n^{3/2})` decay while Schwartz decay controls the translated bulk). Dominated convergence is therefore uniform on the compact scale interval. Letting `delta\downarrow0` proves (16).

Equation (16) is the missing interchange statement. Fixed-scale convergence from `ANF-026` plus the dilute estimate (12) means that taking `H\to0`, taking `rho\to0`, mixing bounded scales, and then testing on a compact frequency window cannot generate an extra boundary profile between (14) and white diffraction.

## 4. Arbitrary zero-Hurst moving mixtures still overshoot the Montgomery--Taylor band

Assume for contradiction that a subsequence of `overline mu_j` converges vaguely to a measure `overline mu` satisfying (2). Let

\[
m_j:=\int\rho\,d\pi_j(H,\rho).
\tag{17}
\]

Every component in (5) has an atom of mass `rho` at zero, so the barycenter has a forward atom of mass `m_j`. Take a continuous cutoff `chi_delta` supported in `(-delta,delta)`, with `0<=chi_delta<=1` and `chi_delta(0)=1`. Positivity gives

\[
m_j\le\langle\overline\mu_j,\chi_\delta\rangle.
\]

Passing to the vague limit and using `overline mu<=nu_a`,

\[
\limsup_jm_j
\le
 a+a\delta^2.
\]

Therefore

\[
\boxed{\limsup_jm_j\le a.}
\tag{18}
\]

Use the explicit slack `eta=0.01`. For all large `j`,

\[
m_j\le a+\eta.
\]

With

\[
M:=2(a+\eta)
=1.526592135712141\ldots,
\tag{19}
\]

Markov's inequality gives

\[
\pi_j\{\rho\le M\}\ge\frac12.
\tag{20}
\]

Condition (1) says that, after intersecting with the small-Hurst region where (16) applies, this still leaves mass `1/2-o(1)`.

Now choose any nonnegative smooth test `varphi` with

\[
\operatorname{supp}\varphi\subset(0.49,0.51),
\qquad
\int\varphi(h)dh=1.
\tag{21}
\]

For the extended zero-Hurst profiles (14)--(15), the nonzero Bragg atoms are positive and may be discarded in a lower bound. On the support of `varphi` and for every `0<=rho<=M`, the diffuse density is at least

\[
\begin{aligned}
d_*
&:=1-\exp\!\left(
-2\pi^2\left(\frac{0.49}{M}\right)^2
\right)\\
&=0.869142764335815\ldots .
\end{aligned}
\tag{22}
\]

Thus

\[
\langle\mu_{0,\rho},\varphi\rangle\ge d_*
\qquad(0\le\rho\le M).
\tag{23}
\]

Uniform convergence (16), positivity of all discarded mixture components, and (20) give

\[
\liminf_j
\langle\overline\mu_j,\varphi\rangle
\ge
\frac{d_*}{2}
=0.434571382167907\ldots .
\tag{24}
\]

But domination by the Montgomery--Taylor budget would give

\[
\begin{aligned}
\langle\overline\mu,\varphi\rangle
&\le
 a\int h\varphi(h)dh\\
&\le0.51a\\
&=0.384180994606596\ldots .
\end{aligned}
\tag{25}
\]

The strict margin is

\[
0.434571382167907\ldots
-0.384180994606596\ldots
=0.050390387561311\ldots,
\]

so the `o(1)` in the uniform Hurst convergence cannot affect the sign. Equations (24)--(25) contradict vague convergence to a dominated limit and prove (2).

Notice that this proof does not assume the scale laws converge, remain bounded away from zero, or are chosen independently of `H`. The only scale information used is forced by the target itself: the forward atom bounds the mean intensity, and Markov then leaves at least half of every candidate mixture in a fixed compact scale interval. The small-scale endpoint of that interval is controlled by the new white-diffraction estimate (12).

## 5. Prior-art and novelty boundary

The external input is the exact stationary-increment regularization theorem and fBm lattice structure factor of Thomassey--Lachièze-Rey--Shapira, *Regularization of a stationary point process by a stationary increments perturbation*, arXiv:2602.19773v1 (23 February 2026). Their Theorem 1.1 gives the absolutely continuous structure factor and, for the lattice, the exact series underlying (4); Proposition 1.3 gives the fixed-`H` small-frequency law used in `ANF-025`. The fixed-dimensional `H=0` Gaussian limit and its fixed-scale diffraction consequence were already separated in `ANF-026`.

A targeted search across fBm-regularized lattices, Palm perturbations, low-Hurst limits, scale/dilution limits, hyperuniform structure factors and diffraction weak limits did not locate the uniform dilute estimate (11)--(12), the joint boundary statement (16), or their Montgomery--Taylor moving-mixture consequence (18)--(25). No publication-level novelty claim is made. These steps are direct consequences of the exact Gaussian Palm autocorrelation once the nonuniform corner is isolated.

No new `SOURCES.md` entry is needed: the only load-bearing paper is already anchored there for `ANF-025`, and `ANF-026` records the known finite-dimensional zero-Hurst prior art separately.

## 6. Evidence boundary and consequence for the scalar frontier

This finding closes the **entire singular zero-Hurst escape inside the fBm Palm-lattice family** under convexification: fixed positive `H` is excluded by `ANF-025`; the fixed-scale `H=0` boundary and post-limit scale mixtures are excluded by `ANF-026`; and pre-limit H-dependent scale mixtures with `H\to0` are excluded here. There is no remaining order-of-limits loophole based on sending the fBm Hurst index to zero.

The proof is specific to this fBm-generated family. It does not classify arbitrary stationary-increment Gaussian perturbations: Thomassey--Lachièze-Rey--Shapira explicitly note that the spectral cancellation formula is special to fractional Brownian fields. Nor does it exclude other genuinely correlated point processes, Gibbsian spacings, direct finite-cluster convexifications, or the configuration-level branch of `ANF-006`.

The useful reusable filter is the dilute endpoint: **a normalized correlated family whose Palm pair mass escapes every fixed spatial window as intensity tends to zero converges to white self diffraction, not to the required contracted linear cusp.** For future stochastic scalar candidates, a vanishing-density escape must therefore be checked at the autocorrelation level before treating dilution as extra spectral freedom.