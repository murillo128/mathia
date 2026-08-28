# WI-005 — critical-lattice aggregation can screen the negative mass of off-line pairs

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `NEGATIVE/OBSTRUCTION`. The single-pair spectrum and the critical-lattice cancellation below are exact consequences of Alpöge--Furman's test family and Poisson--Gabor identity. The diagonal/painless Gabor-frame mechanism is classical, so no novelty is claimed for that harmonic-analysis identity. The research consequence is negative: horizontal depth by itself cannot be charged additively to `tr(Q_- )`; vertical arrangement can screen the negative mass of a positive-density family of off-line pairs. Any zeta-specific lower bound of the type proposed in WI-004 therefore needs additional vertical/arithmetic information.

## 1. The question left by WI-004

WI-004 retains the nonnegative remainder in the Alpöge--Furman rank--trace inequality and shows that a near-extremizer must satisfy

\[
\operatorname{tr}(Q'_-)=o(N).
\]

It therefore proposed testing a bridge of the form

\[
\operatorname{tr}(Q'_-)
\stackrel{?}{\ge}
c(\eta)\,\#\{\rho:\ |\beta-\tfrac12|\log T\ge\eta\}-o(N),
\qquad c(\eta)>0.
\]

A first instinct is that each off-line functional-equation pair has one negative direction, and that the magnitude of that negative eigenvalue should grow with horizontal depth. The first statement is correct for an isolated pair. The second does **not** survive aggregation: at the critical vertical spacing used by the compressed Weil matrix, an entire lattice of equally deep pairs has a positive-semidefinite aggregate independent of the depth.

This is a cancellation/screening mechanism inside the exact Alpöge--Furman Gabor geometry, not a generic matrix counterexample.

## 2. Exact spectrum of one off-line pair on the full sample grid

Use Alpöge--Furman's notation

\[
L=\log(T/2\pi),\qquad h=\frac{2\pi}{L},\qquad
\alpha_k=T+kh,
\qquad a=\frac{\|\phi\|_2^2}{L}.
\]

Let

\[
\rho=\frac12+\delta+it,
\qquad z:=\gamma_\rho=t-i\delta,
\]

and on the full grid `k in Z` put

\[
w=(\widehat\phi(z-\alpha_k))_{k\in\mathbb Z}=A+iB,
\qquad A,B\in\ell^2(\mathbb Z;\mathbb R).
\]

Alpöge--Furman Lemma 2.1 gives, first with `z'=z`,

\[
w^{\mathsf T}w=aL^2.
\]

Hence

\[
A\cdot B=0,
\qquad
\|A\|^2-\|B\|^2=aL^2.
\]

With `z'=\bar z`, reality of `phi` gives

\[
\|w\|^2
=L\,\widehat{\phi^2}(z-\bar z)
=L\int_{-L/2}^{L/2}\phi(u)^2e^{-2\delta u}\,du.
\]

Because `phi^2` is even, define

\[
r_L(\delta)
:=\frac{\int\phi(u)^2\cosh(2\delta u)\,du}{\|\phi\|_2^2}\ge1.
\]

Then

\[
\|A\|^2=\frac{aL^2}{2}(r_L+1),
\qquad
\|B\|^2=\frac{aL^2}{2}(r_L-1).
\]

The normalized contribution of the simple off-line pair `rho,1-bar(rho)` is

\[
R_\rho
=\frac{1}{aL^2}
\left(ww^{\mathsf T}+\bar w\bar w^{\mathsf T}\right)
=\frac{2}{aL^2}(AA^{\mathsf T}-BB^{\mathsf T}).
\]

Since `A` and `B` are orthogonal, the two nonzero eigenvalues are exactly

\[
\boxed{
\lambda_+(R_\rho)=1+r_L(\delta),
\qquad
\lambda_-(R_\rho)=-(r_L(\delta)-1).
}
\]

Thus one isolated pair really does carry a depth-dependent negative charge.

At the natural scale `y=delta L` fixed as `L -> infinity`, the smoothing in (2.7) gives

\[
r_L(y/L)\longrightarrow
r_\psi(y)
:=\frac{\int_{-1/2}^{1/2}\psi(s)\cosh(2ys)\,ds}
{\int_{-1/2}^{1/2}\psi(s)\,ds}.
\]

For small `y`,

\[
r_\psi(y)-1
=2\mu_2(\psi)y^2+O(y^4),
\qquad
\mu_2(\psi)=\frac{\int s^2\psi(s)\,ds}{\int\psi(s)\,ds}.
\]

For the ideal flat window `psi_0=1`,

\[
\boxed{r_{\psi_0}(y)=\frac{\sinh y}{y}},
\]

so the isolated negative magnitude is `sinh(y)/y-1` (about `0.1752` at `y=1` and `0.8134` at `y=2`).

This makes the failure below nontrivial: aggregation can erase a negative eigenvalue that is order one at fixed nonzero normalized depth.

## 3. Exact critical-lattice screening

Now place off-line pair centers at the same vertical spacing as the test-family grid:

\[
t_j=t_0+jh,
\qquad j\in\mathbb Z,
\]

all at the same horizontal displacement `delta`. Let `R_j` denote their normalized pair matrices on the full coefficient space `ell^2(Z)`.

For a finitely supported real vector `x=(x_k)`, set

\[
X(u):=\sum_k x_ke^{i\alpha_k u}.
\]

Writing

\[
c_j(x):=\sum_kx_k\widehat\phi(t_j-i\delta-\alpha_k)
=\int\phi(u)X(u)e^{-it_ju}e^{-\delta u}\,du,
\]

one has

\[
x^{\mathsf T}R_jx
=\frac{2}{aL^2}\operatorname{Re}c_j(x)^2.
\]

Sum over the full vertical lattice. Poisson summation at `h=2pi/L` gives

\[
\sum_{j\in\mathbb Z}e^{-ijh(u+v)}
=L\sum_{m\in\mathbb Z}\delta(u+v-mL).
\]

Since `u,v` lie in `[-L/2,L/2]`, compact support leaves only `m=0` (the endpoint cases vanish for the smoothed compactly supported window). On `v=-u`, three things happen simultaneously:

\[
e^{-\delta(u+v)}=1,
\qquad
\phi(v)=\phi(u),
\qquad
X(-u)=\overline{X(u)}
\]

for real `x`. Therefore

\[
\boxed{
\sum_{j\in\mathbb Z}x^{\mathsf T}R_jx
=\frac{2}{aL}\int_{-L/2}^{L/2}\phi(u)^2|X(u)|^2\,du
\ge0.
}
\]

The horizontal depth has disappeared **exactly**.

Under the Fourier-series identification of `ell^2(Z)` with `L^2([-L/2,L/2])`, the full aggregate is simply the multiplication operator

\[
\boxed{
F_\delta:=\sum_{j\in\mathbb Z}R_j
\ \simeq\ M_{\,2\phi^2/a},
}
\]

which is positive semidefinite and independent of `delta`.

For the ideal flat window `phi=1` on the interval, `a=1` and

\[
\boxed{F_\delta=2I}
\]

for **every** horizontal depth. This is exactly the residual equality shape `Q=2Pi` from the rank--trace lemma, obtained here by aggregating individually indefinite off-line pair blocks.

## 4. The screening survives finite macroscopic clusters

The preceding identity is infinite-lattice, but the obstruction is not an artifact of taking infinitely many pairs.

Align a finite block of pair centers with sample positions and take fixed normalized depth `y=delta L`. Write

\[
u_j(k):=\frac{\widehat\phi((j-k)h-i y/L)}{\sqrt a\,L}.
\]

The decay estimate (2.8) implies uniformly for fixed `y`

\[
|u_j(k)|\ll_y
\min\left(1,\frac{1}{1+|j-k|},\frac{L}{(1+|j-k|)^2}\right).
\]

Consequently, if `P_J` projects onto the coordinate interval `J` and a center `j in J` is distance `r` from its boundary,

\[
\|(1-P_J)u_j\|_2\ll_y(1+r)^{-1/2}
\]

until the stronger quadratic tail takes over. For a real rank-one form,

\[
\|uu^{\mathsf T}-(Pu)(Pu)^{\mathsf T}\|_1
\le2\|u\|\|(1-P)u\|+\|(1-P)u\|^2.
\]

Applying this separately to the real and imaginary parts of the pair vectors gives, for `Q_J=sum_{j in J} R_j` and the positive compression `B_J=P_JF_\delta P_J`,

\[
\boxed{
\|Q_J-B_J\|_1
\ll_y \sqrt{|J|}+\log L.
}
\]

The `sqrt(|J|)` term is the sum of the internal boundary tails; the `log L` term is the contribution of lattice centers outside `J` entering the compression. Since `B_J` is positive semidefinite,

\[
\boxed{
\operatorname{tr}(Q_J)_-
\le\|Q_J-B_J\|_1
\ll_y\sqrt{|J|}+\log L.
}
\]

In particular, for the natural blocks `|J|asymp L`, which occupy a fixed `O(1)` vertical interval,

\[
\boxed{
\operatorname{tr}(Q_J)_-=o(|J|)
}
\]

although every pair has fixed nonzero normalized depth `|beta-1/2|L=|y|` and, in isolation, an order-one negative eigenvalue.

This finite-section estimate is the decisive point for WI-004: the negative charge is not additive even at density scale.

## 5. Coarse zero counts do not by themselves forbid the screening pattern

This is an adversarial zero-side configuration, not a claim about the actual zeta zeros. It is nevertheless compatible with the coarse counting scale available in the Alpöge--Furman setup.

A block of `cL` lattice centers has vertical length

\[
(cL)\frac{2\pi}{L}=2\pi c=O(1)
\]

and contributes `O(L)` zeros. The standard local bound `N(t,t+1) \ll L`, and even the Riemann--von Mangoldt formula differenced over bounded intervals with its `O(L)` error, do not exclude such a fixed-density burst by themselves.

One can repeat separated `O(1)` blocks, leaving compensating gaps so that the average zero count has the correct `L/(2pi)` scale. Comparing each block to its positive compression gives total boundary cost `O(T sqrt(L))=o(TL)=o(N)` over `[T,2T]` for fixed normalized depth.

Therefore a universal inequality that charges every deep pair by a fixed amount of negative spectral mass cannot be obtained solely from:

- the individual `(1,1)` off-line block signature;
- the horizontal depth `|beta-1/2|L`;
- the Gabor localization estimate (2.8);
- the standard coarse zero-count bounds.

A theorem for the **actual** zeta zeros could still force such a charge, but it would have to use extra information that rules out the vertically coherent screening pattern: pair/higher correlations, a prime-side observable, spacing/anti-clustering information, or another arithmetic constraint.

## 6. Flat and Montgomery--Taylor windows react differently after screening

The screening kills negative mass for every admissible window, but it does not make every aggregate equal to `2I`. The residual positive spectral shape remembers `phi` through the multiplier `2phi^2/a`.

For long finite lattice blocks the second spectral moment per pair tends to

\[
D_\psi
:=4\frac{\int_{-1/2}^{1/2}\psi(s)^2\,ds}
{\left(\int_{-1/2}^{1/2}\psi(s)\,ds\right)^2}.
\]

For the flat window,

\[
D_{\psi_0}=4,
\]

so the screened block also asymptotically realizes the `Q=2Pi` equality spectrum. Thus the flat first-two-moment model cannot distinguish a cluster of fixed-normalized-depth off-line pairs from the residual projection model merely through `tr`, `tr(Q_- )`, or the second moment.

For the Montgomery--Taylor window `psi_MT(s)=cos(sqrt(2)s)`,

\[
\int\psi_{\mathrm{MT}}
=\sqrt2\sin(1/\sqrt2),
\qquad
\int\psi_{\mathrm{MT}}^2
=\frac12+\frac{\sin\sqrt2}{2\sqrt2},
\]

and hence

\[
\boxed{D_{\psi_{\mathrm{MT}}}=4.024508763\ldots>4.}
\]

So the full WI-004 remainder still sees a screened Montgomery--Taylor lattice through the positive-eigenvalue variance term `sum(q_j-2)^2`, even though `tr(Q_-)=o(N)`. This does **not** yet improve the theorem: on-line double zeros can still realize the flat residual charge, and other vertical arrangements may alter the screened spectrum. It does show that negative mass is only one component of the stability problem.

## 7. Prior art and novelty audit

Alpöge--Furman already prove the exact Poisson--Gabor identity used above and explicitly note that their critical-density system has a translation-invariant frame kernel with no aliasing error. The general phenomenon that compact support plus sufficiently dense modulation makes a Gabor frame operator diagonal is classical; a standard source is Daubechies--Grossmann--Meyer, *Painless nonorthogonal expansions* (1986), and later nonstationary-Gabor work states the multiplication-operator formula explicitly.

Accordingly, no novelty is claimed for Poisson summation, Gabor-frame diagonality, or the multiplier `2phi^2/a` in isolation.

The durable consequence for this research line is the interaction with the **indefinite off-line pair blocks**: each pair has a depth-dependent negative eigenvalue, but a critical vertical lattice cancels the depth factors exactly at `u+v=0`, leaving a positive aggregate. This directly falsifies the naive additivity premise behind a depth-only implementation of the WI-004 bridge.

## 8. Consequence for `weil_inertia`

WI-004's proposed target must be refined. The relevant missing observable is not horizontal depth alone but a joint depth/vertical-geometry quantity.

A viable strengthening now needs to distinguish, for example,

\[
\boxed{
\text{deep off-line mass}
\quad+\quad
\text{vertical deviation from a screening configuration}
}
\]

or exploit a remainder term that survives screening, such as positive-spectrum variance for a nonflat window.

The most discriminating next questions are therefore:

1. can the actual zeta pair-correlation/prime-side information rule out positive-density near-critical-lattice clusters of off-line pairs at fixed normalized depth?;
2. can the Montgomery--Taylor positive-spectrum variance be converted into a zero-side charge that separates off-line screened pairs from on-line doubles?;
3. is there a joint inequality involving `tr(Q_- )` and `sum(q_j-2)^2` whose near-equality configurations are incompatible with established zero statistics?

Until one of these supplies genuinely new information, **pairwise horizontal depth cannot be summed into the missing negative-mass lower bound**.