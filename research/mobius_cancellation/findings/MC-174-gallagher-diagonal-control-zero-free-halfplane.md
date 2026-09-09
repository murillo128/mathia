# MC-174 — Gallagher diagonal control at `tau >= 1/8` forces a fixed zeta zero-free half-plane

**Status:** `EXACT-DERIVED`, `FRONTIER-RESTRICTION`, `ZERO-FREE-CONSEQUENCE`, `CLASSICAL-TOOLS`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The live Gallagher-energy target in `MC-172` is substantially stronger than a generic local second-moment estimate. In the phase-transport regime

\[
\frac18\le \tau<\frac38,
\qquad
T_\beta=e^{\tau/\beta},
\tag{1}
\]

assume the true Möbius phase satisfies

\[
\boxed{
\limsup_{\beta\downarrow0}
\beta\log \mathcal G_\mu(\beta,T_\beta)
\le \frac18.
}
\tag{2}
\]

Then three consequences follow without assuming analytic continuation of `1/zeta` in the argument that produces `(2)`.

First, `(2)` automatically transfers to every fixed vertical modulation of Möbius. If

\[
\mathcal G_{\mu,t_0}(\beta,T)
:=
T\int_0^\infty
\left|
\sum_{y<n\le ye^{1/T}}
\mu(n)n^{-it_0}e^{-\beta(\log n)^2}
\right|^2\frac{dy}{y},
\tag{3}
\]

then for every fixed real `t_0`,

\[
\boxed{
\limsup_{\beta\downarrow0}
\beta\log \mathcal G_{\mu,t_0}(\beta,T_\beta)
\le \frac18.
}
\tag{4}
\]

Second, the heat-semigroup identity plus Gallagher localization converts `(4)` into a pointwise bound for the full time orbit from `MC-169`:

\[
\Theta_\mu(\beta,t)
=
\sum_{n\ge1}\mu(n)n^{-it}e^{-\beta(\log n)^2}.
\]

For every fixed real `t`,

\[
\boxed{
\limsup_{\beta\downarrow0}
\beta\log^+|\Theta_\mu(\beta,t)|
\le
c_\tau
:=
\frac1{16}+\frac\tau2.
}
\tag{5}
\]

Third, the Poisson/heat subordination argument already audited in `MC-169` turns `(5)` into a fixed zero-free half-plane:

\[
\boxed{
\zeta(s)\ne0
\qquad
\text{whenever}
\qquad
\operatorname{Re}s>
\alpha_\tau
:=
\sqrt{\frac14+2\tau}.
}
\tag{6}
\]

Thus the `MC-172` target is not merely an innocuous intermediate variance statement. For every `tau<3/8` covered by this transfer, `(6)` gives `alpha_tau<1`, hence exclusion of **all** zeta zeros from a fixed half-plane strictly wider than the classical asymptotic zero-free region near `Re(s)=1`. At the first robust endpoint `tau=1/8`,

\[
\alpha_{1/8}=\frac1{\sqrt2}\approx0.7071.
\tag{7}
\]

As `tau` approaches `3/8` from below, `alpha_tau` approaches `1`, matching the fact that the finite-time statistic becomes phase-blind at the `3/8` washout horizon of `MC-171`.

The result does **not** say that `(2)` is equivalent to RH. A fixed positive `tau` gives a zero-free boundary strictly to the right of `1/2`. It instead quantifies the analytic price of the proposed local-energy estimate: proving diagonal exponential type in the robust sub-washout regime would already be a major fixed-power zero-exclusion theorem.

## 1. Vertical twists are locally almost constant

Write

\[
w_\beta(n)=e^{-\beta(\log n)^2}
\]

and, for a fixed multiplicative interval,

\[
S_{t_0}(y)
=
\sum_{y<n\le ye^{1/T}}
\mu(n)n^{-it_0}w_\beta(n),
\qquad
S_0(y)
=
\sum_{y<n\le ye^{1/T}}
\mu(n)w_\beta(n).
\tag{8}
\]

Factor out the unit-modulus phase `y^{-it_0}`. Since

\[
0<\log(n/y)\le\frac1T
\]

throughout the interval and `|e^{-iv}-1|<=|v|`,

\[
\begin{aligned}
|S_{t_0}(y)-y^{-it_0}S_0(y)|
&\le
\sum_{y<n\le ye^{1/T}}
\mu(n)^2w_\beta(n)
\left|e^{-it_0\log(n/y)}-1\right|\\
&\le
\frac{|t_0|}{T}
\sum_{y<n\le ye^{1/T}}
\mu(n)^2w_\beta(n).
\end{aligned}
\tag{9}
\]

Let `mathcal G_+(beta,T)` denote the all-plus square-free Gallagher energy from `MC-172`. Taking the `L^2(T\,dy/y)` norm and using the reverse triangle inequality gives the exact stability estimate

\[
\boxed{
\left|
\mathcal G_{\mu,t_0}(\beta,T)^{1/2}
-
\mathcal G_\mu(\beta,T)^{1/2}
\right|
\le
\frac{|t_0|}{T}
\mathcal G_+(\beta,T)^{1/2}.
}
\tag{10}
\]

For `T=T_beta` and `tau<3/8`, `MC-172` proves

\[
\lim_{\beta\downarrow0}
\beta\log \mathcal G_+(\beta,T_\beta)
=
\frac12-\tau.
\tag{11}
\]

Therefore the squared error term in `(10)` has exponential type

\[
\left(\frac12-\tau\right)-2\tau
=
\frac12-3\tau.
\tag{12}
\]

Exactly at

\[
\tau=\frac18,
\]

this equals the diagonal type `1/8`; for every larger `tau` it is smaller. Hence `(2)` and `(10)` imply `(4)` for every fixed `t_0` whenever `(1)` holds. The multiplicative phase `n^{-it_0}` is too slowly varying across these windows to destroy a diagonal-type estimate once `tau>=1/8`.

This `1/8` threshold is a **stability threshold for the present proof**, not a claim that twist transport is impossible below it. Below `1/8`, the phase-free envelope in `(10)` can have type larger than the target after the `T^{-2}` gain, so an additional signed estimate would be needed.

## 2. Heat smoothing converts finite-time `L^2` control into pointwise orbit control

The Gaussian weights satisfy an exact heat-semigroup relation in the spectral variable `t`. For `delta>0`, let

\[
K_\delta(u)
=
\frac1{\sqrt{4\pi\delta}}
\exp\!\left(-\frac{u^2}{4\delta}\right).
\tag{13}
\]

Its Fourier transform is `e^{-delta xi^2}`. Absolute convergence of the theta sums therefore gives

\[
\boxed{
\Theta_\mu(\beta+\delta,t_0)
=
\int_{\mathbb R}
K_\delta(u)\Theta_\mu(\beta,t_0+u)\,du.
}
\tag{14}
\]

Fix `eta>0` and put `delta=eta beta`. Split `(14)` at `|u|=T_beta`. On the central interval, Cauchy--Schwarz gives

\[
\begin{aligned}
\left|
\int_{-T_\beta}^{T_\beta}
K_{\eta\beta}(u)\Theta_\mu(\beta,t_0+u)\,du
\right|
&\le
\|K_{\eta\beta}\|_2
\left(
\int_{-T_\beta}^{T_\beta}
|\Theta_\mu(\beta,t_0+u)|^2du
\right)^{1/2}\\
&\ll_\eta
\beta^{-1/4}
\left(
T_\beta V_{\mu,t_0}(\beta,T_\beta)
\right)^{1/2},
\end{aligned}
\tag{15}
\]

where

\[
V_{\mu,t_0}(\beta,T)
=
\frac1{2T}
\int_{-T}^{T}
|\Theta_\mu(\beta,t_0+u)|^2du.
\tag{16}
\]

Applying Gallagher's inequality to the vertically twisted coefficients gives

\[
V_{\mu,t_0}(\beta,T)
\ll
\mathcal G_{\mu,t_0}(\beta,T).
\tag{17}
\]

The tail `|u|>T_beta` in `(14)` is negligible on every `exp(C/beta)` scale. Indeed,

\[
|\Theta_\mu(\beta,t)|
\le
A(\beta)
:=
\sum_{n\ge1}\mu(n)^2e^{-\beta(\log n)^2},
\tag{18}
\]

and `A(beta)` has exponential type `1/4`, while the Gaussian tail of `K_{eta beta}` beyond `T_beta=e^{tau/beta}` decays like

\[
\exp\!\left(-\frac{T_\beta^2}{O(\beta)}\right),
\]

which is super-exponentially smaller.

Combining `(4)`, `(15)` and `(17)` yields

\[
\limsup_{\beta\downarrow0}
\beta\log^+
|\Theta_\mu((1+\eta)\beta,t_0)|
\le
\frac\tau2+\frac1{16}.
\tag{19}
\]

Rescale `beta'=(1+eta)beta`. Since `(19)` holds for every fixed positive `eta`,

\[
\limsup_{\beta'\downarrow0}
\beta'\log^+|\Theta_\mu(\beta',t_0)|
\le
(1+\eta)
\left(\frac\tau2+\frac1{16}\right).
\]

Letting `eta` decrease to zero proves `(5)`.

The direction is important. This argument uses Gallagher only in its valid direction `V << mathcal G`. No reverse Gallagher inequality or point-evaluation estimate is assumed. The pointwise information comes instead from the exact heat-semigroup smoothing `(14)`.

## 3. Subordination gives the zero-free boundary

`MC-169` already audits the classical Poisson/heat subordination identity

\[
e^{-\sigma u}
=
\frac{\sigma}{2\sqrt\pi}
\int_0^\infty
\beta^{-3/2}
\exp\!\left(-\frac{\sigma^2}{4\beta}\right)
 e^{-\beta u^2}\,d\beta,
\qquad \sigma>0.
\tag{20}
\]

For `sigma>1`, termwise insertion into the absolutely convergent Möbius Dirichlet series gives

\[
\frac1{\zeta(\sigma+it_0)}
=
\frac{\sigma}{2\sqrt\pi}
\int_0^\infty
\beta^{-3/2}
 e^{-\sigma^2/(4\beta)}
\Theta_\mu(\beta,t_0)\,d\beta.
\tag{21}
\]

Now assume `(5)`. For any real

\[
\sigma_0>2\sqrt{c_\tau},
\]

choose `epsilon>0` such that

\[
c_\tau+\epsilon<\frac{\sigma_0^2}{4}.
\]

Then `(5)` makes the right side of `(21)` absolutely convergent at small `beta` with a positive exponential margin. Exactly as in `MC-169`, the same integral defines a holomorphic continuation in the right-hand connected component of the corresponding region `Re(z^2)>4(c_tau+epsilon)`. It agrees with `1/zeta(z+it_0)` for real `z>1`, so uniqueness of meromorphic continuation forbids a pole at the real point `z=sigma_0`. Therefore

\[
\zeta(\sigma_0+it_0)\ne0.
\]

Since `t_0` and `sigma_0` were arbitrary,

\[
\zeta(s)\ne0
\qquad
\text{for }
\operatorname{Re}s>2\sqrt{c_\tau}.
\]

Using

\[
2\sqrt{c_\tau}
=
2\sqrt{\frac1{16}+\frac\tau2}
=
\sqrt{\frac14+2\tau}
\]

proves `(6)`.

This generalizes only the **quantitative boundary** of the already-classicalized subordination mechanism in `MC-169`. At `c=1/16` the boundary becomes `Re(s)>1/2` and hence RH; the present fixed `tau>0` yields `c_tau>1/16` and therefore a strictly weaker zero-exclusion statement.

## 4. Why this materially restricts the `MC-172` frontier

The numerical map

\[
\tau
\longmapsto
\alpha_\tau=\sqrt{\frac14+2\tau}
\tag{22}
\]

prices the local-energy target directly in zero-free-region strength. For example, the first phase-transport point `tau=1/8` already forces `Re(s)>1/sqrt(2)` to be zero-free, while any `tau<3/8` forces some fixed half-plane `Re(s)>alpha_tau` with `alpha_tau<1`.

That is far stronger than what one should expect from merely combining existing almost-all short-interval cancellation or qualitative Chowla information. `MC-172` already showed those inputs miss the diagonal local-variance scale; the present result explains why closing that gap would be so consequential. A proof of `(2)` in this regime would not just improve a technical heat estimate: it would solve a genuine fixed zero-exclusion problem for zeta.

This also sharpens the interpretation of `MC-173`. Doyle's new `k`-free `ell^2` technology enters the current Möbius application only after an additive autocorrelation has removed prime orientation. The missing phase-sensitive estimate cannot be a modest refinement if it reaches `(2)` for `tau>=1/8`, because the resulting theorem would already imply `(6)`.

## Prior art and novelty audit

The ingredients are established. Gallagher's localization is classical (`MC-S42`) and its Dirichlet-series/Selberg-integral form is explicitly recorded by Coppola--Laporta (`MC-S43`). The Gaussian heat-semigroup identity `(14)` is the standard one-dimensional heat kernel acting on the time-frequency variable. Poisson/heat subordination and its reciprocal-zeta continuation consequence were already audited in `MC-169`. The all-plus exponential type used in `(11)` is the exact control derived in `MC-172` from classical square-free counting.

A targeted literature search around Gallagher localization, Möbius short-interval mean squares, Gaussian-smoothed Möbius sums, and heat/subordination zero-free arguments located the standard Gallagher/Coppola--Laporta machinery and general Dirichlet-polynomial mean-value literature, but did not locate this particular coupled `tau -> alpha_tau` statement. **No novelty claim is made**: the mathematical contribution here is an exact Mathia-specific composition of already established tools that calibrates the difficulty of the live `MC-172` target.

No new bibliographic anchor is required: all load-bearing external tools are already recorded in `SOURCES.md` through `MC-S42`--`MC-S44` or in the source audit of `MC-169`.

## Boundaries and falsification controls

- The implication is proved only for `1/8 <= tau < 3/8`. The lower endpoint comes from the support-based twist-stability estimate `(10)` and is not asserted to be optimal for Möbius.
- Below `tau=1/8`, `(12)` is larger than diagonal type. A stronger **signed** twist-stability theorem could still extend the zero-free consequence closer to the critical line; this finding does not rule that out.
- The upper endpoint `3/8` is the phase-washout boundary from `MC-171`. At and above that scale diagonal mean-square behavior no longer discriminates Möbius orientation at leading exponential type.
- A fixed `tau>0` does not imply RH through this argument. The resulting zero-free boundary is `alpha_tau>1/2`.
- No uniform constant in `t_0` is used. Each hypothetical zero ordinate is fixed before taking `beta -> 0`; the factor `|t_0|` in `(10)` is subexponential and therefore irrelevant to the type.
- The proof does not assume a reverse Gallagher inequality. If `(17)` were used backwards, the conclusion would be invalid.
- The proof does not infer deterministic arithmetic from the random-prime-phase control. The all-plus energy enters only as an exact envelope for the local variation of a fixed Archimedean twist.
- The conclusion would be falsified by an error in the heat-semigroup identity, the `T^{-2}` twist budget, or the subordination domain. Each of those steps is explicit above and independently checkable.

## Consequence for the research line

`MC-172` remains a mathematically valid intermediate object, but its proposed diagonal target is now quantitatively priced. In the robust regime `tau>=1/8`, proving that target would already force a fixed zero-free half-plane for zeta, with boundary `(22)`. This explains why current local-cancellation inputs can reach the geometric window scale yet remain dramatically short of the required second-moment strength.

A sharper next question is therefore not simply whether existing short-interval machinery can prove `(2)`. It is whether one can identify a **signed mechanism that either** (a) proves a weaker, genuinely cheaper local-energy exponent with a still-useful transfer, or (b) transports vertical twists below the `tau=1/8` support-envelope threshold without paying the all-plus coherence budget. Either outcome would expose where the zero-free information actually enters rather than hiding it inside a seemingly local variance estimate.