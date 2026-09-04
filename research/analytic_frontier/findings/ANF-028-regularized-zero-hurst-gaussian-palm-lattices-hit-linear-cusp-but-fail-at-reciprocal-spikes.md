# ANF-028 — regularized zero-Hurst Gaussian Palm lattices hit the linear cusp but fail at reciprocal spikes

**Status:** `LITERATURE+DERIVED + EXACT-ASYMPTOTIC + NEGATIVE/OBSTRUCTION + DIFFRACTION-DUAL`. `ANF-025`--`ANF-027` show that the ordinary fractional-Brownian Palm-lattice family cannot reach the Montgomery--Taylor order interval: every fixed `H>0` has the wrong infrared exponent, while the singular unregularized `H\downarrow0` boundary returns to a white/iid-shuffle diffraction profile. That does **not** exhaust Gaussian stationary-increment perturbations. There is a distinct classical zero-Hurst regularization whose increment variance grows logarithmically rather than tending to a constant.

For `c>0`, let `B^{(c)}` be a centered Gaussian process with stationary increments, `B^{(c)}_0=0`, and variogram

\[
\boxed{
v_c(t)=c\log(1+t^2).
}
\tag{1}
\]

Perturb the Palm lattice by

\[
\widehat\xi_c=\{n+B^{(c)}_n:n\in\mathbb Z\}.
\tag{2}
\]

This logarithmic-variogram family is important for the scalar frontier for two reasons. First, unlike fBm with any fixed positive Hurst index, its diffuse structure factor has the **exact linear cusp**

\[
\boxed{
S_c(q)=2\pi^2c\,|q|+O(q^2),
\qquad q\to0.
}
\tag{3}
\]

Thus general Gaussian stationary-increment regularization can hit the same infrared exponent as the Montgomery--Taylor budget. Second, every fixed intensity still fails the full support-one domination. The obstruction has moved from the origin to the first reciprocal frequency: the logarithmic spreading erases Bragg atoms but leaves an integrable reciprocal spike, and after scaling to intensity `rho<=a<1` that spike sits at the interior point `h=rho` where the target density is strictly below one.

There is a particularly clean calibration at

\[
c_*:=\frac1{4\pi^2}.
\tag{4}
\]

At unit intensity, (3) becomes `S_{c_*}(q)~|q|/2`. Scale the process to the Montgomery--Taylor intensity

\[
a:=a_{\rm MT}=C_{\rm MT}^{-1}=0.753296067856070\ldots .
\]

Its full per-particle diffraction then has forward atom exactly `a` and diffuse slope

\[
\frac{1}{2a}=0.663749648160294\ldots<a.
\tag{5}
\]

So this candidate **strictly passes both local origin tests**. Nevertheless its first reciprocal feature, now at `h=a`, is logarithmically divergent and therefore violates the target `a|h|dh` on every sufficiently small neighborhood of `a`. Local hyperuniform slope plus the forward-atom budget are therefore not sufficient for the scalar diffraction witness.

## 1. The logarithmic variogram is an honest mixing stationary-increment Gaussian field

The existence of (1) follows directly from the Lévy--Khintchine representation used for Gaussian stationary-increment fields. The elementary identity

\[
\int_0^\infty \frac{e^{-x}}x(1-\cos tx)\,dx
=\frac12\log(1+t^2)
\tag{6}
\]

is obtained by differentiating in `t` and integrating `t/(1+t^2)`. Hence

\[
v_c(t)
=
\int_{\mathbb R}|1-e^{-itx}|^2\,\mu_c(dx),
\qquad
\mu_c(dx)=\frac c2\frac{e^{-|x|}}{|x|}\,dx.
\tag{7}
\]

The measure in (7) is positive, symmetric, satisfies the Lévy integrability condition, and is absolutely continuous. Thus it defines a continuous centered Gaussian process with stationary increments. By the Maruyama criterion quoted in Thomassey--Lachièze-Rey--Shapira, the field is mixing (in particular ergodic), so their Palm-stationarization result applies: (2) is the Palm distribution of a stationary ergodic point process of intensity one.

This variogram is not an invented special function. Fyodorov--Khoruzhenko--Simm, *Fractional Brownian motion with Hurst index H=0 and the Gaussian Unitary Ensemble*, *Annals of Probability* 44 (2016), 2980--3031, DOI `10.1214/15-AOP1039`, introduced an `eta`-regularized zero-Hurst fractional Brownian motion: a centered Gaussian stationary-increment process with logarithmic increment structure. Up to harmless amplitude and spatial rescalings, (1) is exactly that regularized `H=0` functional form. This is a different limiting object from the unregularized `H\downarrow0` field in `ANF-026`--`ANF-027`.

## 2. The Palm two-point measure gives an exact Fourier series

For each nonzero integer `n`, the marginal displacement `B^{(c)}_n` is Gaussian with variance

\[
v_c(n)=c\log(1+n^2).
\]

Therefore the expected Palm measure is

\[
\mathbb E\widehat\xi_c
=
\delta_0+
\sum_{n\ne0}g_{v_c(n)}(x-n)\,dx,
\tag{8}
\]

where `g_v` is the centered Gaussian density of variance `v`. Local second moments are finite: for a fixed compact interval, the probability that the label `n` enters it decays like `exp(-\Omega(n^2/\log|n|))`, and the corresponding double sums are summable by Cauchy--Schwarz. Thus the stationary process has a well-defined Bartlett spectrum.

In the Mathia Fourier convention `e^{-2\pi iqx}`, Fourier transformation of the correlation distribution gives, away from the forward frequency,

\[
\boxed{
S_c(q)
=1+2\sum_{n\ge1}
(1+n^2)^{-2\pi^2c q^2}
\cos(2\pi qn).
}
\tag{9}
\]

For every noninteger `q`, the coefficients in (9) decrease to zero, so Dirichlet convergence is immediate. Near a nonzero integer the same series is represented by a locally integrable power or logarithmic singularity derived below. Consequently the Bartlett spectrum is absolutely continuous on `\mathbb R\setminus\{0\}`; the logarithmic growth has erased nonzero Bragg **atoms**, even though it has not erased reciprocal-frequency structure.

The normalized full diffraction at unit intensity is therefore

\[
\mu_c=\delta_0+S_c(q)\,dq.
\tag{10}
\]

After spatial dilation to intensity `rho>0`, the same normalization used in `ANF-025`--`ANF-027` gives

\[
\boxed{
\mu_{c,\rho}
=\rho\,\delta_0+S_c(h/\rho)\,dh.
}
\tag{11}
\]

## 3. Logarithmic variance growth produces the missing linear cusp

Set

\[
p:=4\pi^2c q^2,
\qquad
\theta:=2\pi q.
\tag{12}
\]

The exact coefficient in (9) differs from `n^{-p}` by an absolutely summable error:

\[
\begin{aligned}
0&\le n^{-p}-(1+n^2)^{-p/2}\\
&=n^{-p}\left(1-(1+n^{-2})^{-p/2}\right)\\
&\le \frac p2\,n^{-p}\log(1+n^{-2}).
\end{aligned}
\tag{13}
\]

Uniformly for small `q`, summing (13) shows that

\[
S_c(q)
=1+2\operatorname{Re}\operatorname{Li}_{p}(e^{i\theta})
+O(p).
\tag{14}
\]

Now use the classical Jonquière expansion, recorded as NIST DLMF 25.12.12,

\[
\operatorname{Li}_s(z)
=
\Gamma(1-s)\left(\log\frac1z\right)^{s-1}
+
\sum_{k\ge0}\zeta(s-k)\frac{(\log z)^k}{k!},
\tag{15}
\]

valid here for small nonzero `p` and `|theta|<2pi`. For `q>0`, the real part of the singular term is

\[
\Gamma(1-p)\theta^{p-1}\sin\frac{\pi p}{2}.
\tag{16}
\]

Because `p=O(q^2)`, one has `p\log\theta=o(1)`, and hence

\[
2\Gamma(1-p)\theta^{p-1}\sin\frac{\pi p}{2}
=
\frac{\pi p}{\theta}+o(q)
=
2\pi^2c\,q+o(q).
\tag{17}
\]

The regular part contributes only `O(q^2)`: indeed `1+2\zeta(p)=O(p)`, the `k=1` term is purely imaginary, and the remaining real terms begin at order `theta^2`. Combining (13)--(17), and using evenness, proves (3).

This identifies the missing asymptotic class behind the failure of fixed-H fBm. A power variogram `|n|^{2H}` produces the fractional cusp `|q|^{1-2H}`; a logarithmic variogram produces an exactly linear cusp. Therefore the fBm no-go in `ANF-025` is **not** a no-go for Gaussian stationary-increment perturbations as a whole.

## 4. Reciprocal frequencies survive as soft singularities rather than Bragg atoms

The same representation shows what replaces the erased lattice peaks. Near the first reciprocal frequency write

\[
q=1+\varepsilon,
\qquad
p(q)=4\pi^2c q^2.
\tag{18}
\]

Replacing `(1+n^2)^{-p(q)/2}` by `n^{-p(q)}` again changes the series by a uniformly absolutely convergent term. Thus the local behavior is governed by

\[
1+2\operatorname{Re}
\operatorname{Li}_{p(q)}(e^{2\pi i\varepsilon}).
\tag{19}
\]

Let

\[
p_1:=4\pi^2c.
\]

If `0<p_1<1`, (15) gives a positive integrable divergence of order

\[
|\varepsilon|^{p_1-1}.
\tag{20}
\]

If `p_1=1`, the pole of `Gamma(1-p)` cancels the pole of `zeta(p)` and the surviving singularity is logarithmic,

\[
\boxed{
S_c(1+\varepsilon)
=-2\log|2\pi\varepsilon|+O(1).
}
\tag{21}
\]

If `p_1>1`, the series converges absolutely at `q=1` and

\[
S_c(1)
=1+2\sum_{n\ge1}(1+n^2)^{-2\pi^2c}
>1.
\tag{22}
\]

All three regimes are locally integrable because `p_1>0`; hence there is no nonzero reciprocal atom. But in every regime there is a neighborhood of `q=1` on which the diffuse density exceeds `1` somewhere, and for `p_1\le1` it becomes arbitrarily large.

The special choice (4) sits exactly at the transition `p_1=1`, giving the clean logarithmic spike (21).

## 5. Every fixed intensity fails the Montgomery--Taylor order interval

Let

\[
\nu_a=a\,\delta_0+a|h|\,dh,
\qquad 0<a<1.
\tag{23}
\]

Assume for contradiction that some fixed pair `(c,rho)` satisfies

\[
\mu_{c,\rho}\le\nu_a
\qquad\text{on }(-1,1).
\tag{24}
\]

The forward atom in (11) forces

\[
\rho\le a<1.
\tag{25}
\]

Therefore the first reciprocal location `h=rho` lies strictly inside the tested band. At that point the target diffuse density is

\[
a\rho\le a^2<1.
\tag{26}
\]

But Sections 2--4 show that the source has no compensating signed term: its Bartlett spectrum is a positive absolutely continuous measure, and near `h=rho` its density is `S_c(h/rho)`. If `4pi^2 c<=1`, that density diverges positively as `h->rho`; if `4pi^2c>1`, it is continuous at `rho` with value strictly larger than one. Either way (24) fails on an interval of positive Lebesgue measure. Hence

\[
\boxed{
\mu_{c,\rho}\not\le\nu_a
\quad
\text{for every }c>0,\ \rho>0,\ 0<a<1.
}
\tag{27}
\]

This is not the iid cloaking tax of `ANF-023`: there is no Bragg atom at `h=rho` that must be forced to zero. The obstruction is a **soft reciprocal spike created by only logarithmic loss of lattice coherence**.

## 6. A calibrated profile passes the entire local origin gate before failing globally

Take `a=a_MT`, `c=c_*` from (4), and `rho=a`. Equation (11) has forward atom exactly `a delta_0`. From (3),

\[
S_{c_*}(h/a)
=
\frac{|h|}{2a}+O(h^2).
\tag{28}
\]

Numerically,

\[
\frac1{2a}=0.663749648160294\ldots,
\qquad
 a=0.753296067856070\ldots,
\tag{29}
\]

so there is strict local slack

\[
a-\frac1{2a}=0.089546419695775\ldots .
\tag{30}
\]

Thus neither the forward atom nor the linear hyperuniform coefficient excludes this profile. The failure occurs only at finite frequency: (21) is transported to the interior point `h=a`, where the target density is finite and at most

\[
a^2=0.567454965847416\ldots .
\tag{31}
\]

This is the first candidate in the `ANF-020` diffraction search developed here that simultaneously has a tunable linear cusp, no nonzero Bragg atoms, and enough origin slack to pass the Montgomery--Taylor local budget, yet still fails by an explicit support-one finite-frequency obstruction.

## 7. Prior-art and novelty boundary

Three ingredients are prior art. Fyodorov--Khoruzhenko--Simm introduced regularized zero-Hurst fBm and its logarithmic stationary-increment structure. Thomassey--Lachièze-Rey--Shapira prove the Palm-stationarization result for ergodic Gaussian stationary-increment perturbations and explicitly note that obtaining structure factors for general slowly growing variograms is open; their exact structure-factor theorem itself is restricted to fBm. The polylogarithm expansion (15) is classical and recorded in NIST DLMF 25.12.12.

What is derived here is the specialization of the Palm-lattice correlation distribution to the logarithmic variogram (1), the exact linear coefficient (3), the classification of the softened first reciprocal feature (20)--(22), and the fixed-intensity Montgomery--Taylor obstruction (27), including the calibrated profile (28)--(31) that passes the local origin gate. A targeted search across regularized `H=0` fBm, logarithmic variograms, correlated perturbed lattices, hyperuniform structure factors and Palm-lattice diffraction did not locate this exact structure-factor calculation or its Montgomery--Taylor application. No publication-level novelty claim is made.

No `SOURCES.md` edit is required for the load-bearing point-process input: Thomassey--Lachièze-Rey--Shapira is already anchored there. Fyodorov--Khoruzhenko--Simm and DLMF serve here to classify the logarithmic process and the standard special-function expansion; the existence identity (6)--(7), the Fourier series (9), and all Montgomery--Taylor consequences are rederived explicitly.

## 8. Evidence boundary and next filter

Equation (27) excludes **fixed-scale** logarithmic-variogram Gaussian Palm lattices. It does not exclude convex mixtures over the intensity `rho`, the amplitude `c`, or both. That distinction is load-bearing: a continuous scale mixture can smear the reciprocal singularities across the band, just as scale mixing removes lattice atoms in `ANF-022`, while the local slope constraint now remains feasible because (3) is exactly linear.

The next useful test is therefore no longer another Hurst limit. It is the two-parameter mixture problem

\[
\int\left[\rho\delta_0+S_c(h/\rho)dh\right]d\Pi(c,\rho)
\stackrel{?}{\le}
 a_{\rm MT}\delta_0+a_{\rm MT}|h|dh.
\tag{32}
\]

The origin imposes the moment constraints

\[
\mathbb E_\Pi\rho\le a_{\rm MT},
\qquad
2\pi^2\mathbb E_\Pi\frac c\rho\le a_{\rm MT},
\tag{33}
\]

but, unlike the fBm family in `ANF-025`--`ANF-027`, these constraints are mutually compatible. Any further no-go must therefore use finite-frequency mass conservation or a quantitative integral cost of smearing the reciprocal spikes. Conversely, a mixture satisfying (32) would be the first genuine Gaussian stationary-increment candidate to survive all current diffraction-side filters. The configuration-level escape in `ANF-006` remains separate and unaffected.