# PC-307 — polylog oriented prime packets require near-qlogq conditioning

**Status:** `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the stable-conditioning escape left open by PC-306.

PC-306 separates exact cyclotomic injectivity from stable analytic information. For the canonical prime source and its one-step translate it gives the general packet bound `O(K/q)` for the first `K` Fourier modes, hence a conditioning lower bound of order `q/K`. That estimate uses only `|F_q(k)|<=1`; it does not use the actual distribution of the prime source.

The prime-number-theorem hierarchy from PC-275--PC-276 makes the instability substantially stronger. For every fixed `A>0`, all nonzero Fourier modes up to polylogarithmic bandwidth `K<=(log q)^A` are themselves only logarithmic-integral fluctuations around the flat source. Consequently the disjoint prime source and its one-step translate have oriented Fourier packets separated by at most

\[
\boxed{
\frac{C_A\,[1+\log(2+K)]}{q\log q}
}
\tag{1}
\]

in sup norm. Any downstream map that turns those packets into outputs a fixed positive distance apart must therefore have Lipschitz constant at least

\[
\boxed{
\operatorname{Lip}(G_q)
\gg_A
\frac{q\log q}{1+\log(2+K)}.
}
\tag{2}
\]

In particular, for every fixed power `K<=(log q)^A`, the required conditioning is at least `Omega_A(q log q / log log q)`; for fixed `K>=1` it is exactly of order `q log q`. Thus adding any polylogarithmic number of ordinary oriented Fourier coordinates does not stabilize the exact cyclotomic source encoding exposed by PC-306.

## 1. Prime-source Fourier packet and matched translation control

Let `q` be prime and define

\[
P_q:=\{p:2<p<q,\ p\text{ prime}\},
\qquad
M_q:=|P_q|=\pi(q)-2,
\tag{3}
\]

with normalized source measure

\[
\nu_q:=\frac1{M_q}\sum_{p\in P_q}\delta_{p/q}.
\tag{4}
\]

Its oriented Fourier coefficients are

\[
F_q(k)
:=
\int_0^1 e^{2\pi i k t}\,d\nu_q(t)
=
\frac1{M_q}\sum_{p\in P_q}e^{2\pi i kp/q}.
\tag{5}
\]

PC-306 uses the translated support

\[
P_q^+:=P_q+1\pmod q.
\tag{6}
\]

Because every element of `P_q` is odd whereas every element of `P_q^+` is even, the two supports are disjoint for `q>3`; their normalized counting measures have total-variation distance one. Translation acts diagonally on the Fourier packet:

\[
F_q^+(k)=\zeta_q^k F_q(k),
\qquad
F_q^+(k)-F_q(k)
=(\zeta_q^k-1)F_q(k).
\tag{7}
\]

The new point is to estimate the actual factor `F_q(k)` rather than replace it by its trivial bound one.

## 2. Uniform polylogarithmic Fourier bound

Put `L=log q`. Introduce the exact normalized logarithmic-integral source from PC-276,

\[
d\lambda_q(t)
:=
\frac{q}{\operatorname{Li}(q)-\operatorname{Li}(2)}
\frac{\mathbf 1_{[2/q,1]}(t)}{L+\log t}\,dt.
\tag{8}
\]

The classical quantitative prime number theorem

\[
\pi(x)=\operatorname{Li}(x)
+O\!\left(xe^{-c\sqrt{\log x}}\right)
\tag{9}
\]

and Stieltjes partial summation imply, after splitting the range below `sqrt(q)` from the bulk, that for an integer mode `k`

\[
\boxed{
F_q(k)-\widehat\lambda_q(k)
=
O\!\left((1+|k|)L e^{-c'\sqrt L}\right)
+O(L/q)
}
\tag{10}
\]

for some `c'>0`. The endpoint convention at `q` and omission of the prime `2` contribute only to the displayed `O(L/q)` term.

PC-276 expands the normalized `Li` source using the logarithmic polynomials `P_m` determined by

\[
P_0(u)=1,
\qquad
P_m(u)=(-u)^m-\sum_{j=1}^m j!P_{m-j}(u).
\tag{11}
\]

For every fixed truncation order `N`, the same derivation is uniform over test functions of sup norm at most one. Hence, for every nonzero integer `k`,

\[
\widehat\lambda_q(k)
=
\sum_{m=1}^{N}\frac{a_m(k)}{L^m}
+O_N(L^{-N-1})
+O_N(q^{-1/2}),
\tag{12}
\]

where

\[
a_m(k)
:=
\int_0^1 e^{2\pi i kt}P_m(\log t)\,dt.
\tag{13}
\]

There is no `m=0` term because

\[
\int_0^1e^{2\pi i kt}\,dt=0
\qquad(k\in\mathbb Z\setminus\{0\}).
\tag{14}
\]

For every fixed `m>=1`, elementary oscillatory integration gives

\[
\boxed{
|a_m(k)|
\ll_m
\frac{[1+\log(2+|k|)]^m}{|k|}.
}
\tag{15}
\]

Indeed, each `P_m(log t)` is a polynomial in `log t`. For a monomial `(log t)^j`, split the integral at `t=1/|k|`. The lower piece has size `O_j((1+log|k|)^j/|k|)`. On `[1/|k|,1]`, one integration by parts gives the same bound because the derivative is `j(log t)^{j-1}/t` and its absolute integral is `O_j((log|k|)^j)`. Constant terms integrate to zero at nonzero integer frequency.

Fix `A>0` and choose an integer `N>A+2`. If

\[
1\le |k|\le L^A,
\tag{16}
\]

then `log(2+|k|)=O_A(log L)=o(L)`. Equations (12)--(15) therefore give

\[
\widehat\lambda_q(k)
\ll_A
\frac{1+\log(2+|k|)}{|k|L},
\tag{17}
\]

because the higher logarithmic orders form a finite geometric-sized correction and the remainder `L^{-N-1}` is smaller than the right side uniformly throughout (16). The PNT error (10) is beyond every fixed negative power of `L` on this polylogarithmic range. Thus

\[
\boxed{
|F_q(k)|
\ll_A
\frac{1+\log(2+|k|)}{|k|\log q}
\qquad
(1\le|k|\le(\log q)^A).
}
\tag{18}
\]

This is a source statement, not a new exponential-sum estimate: it is precisely the normalized `Li` hierarchy of PC-276 viewed in the additive Fourier basis.

## 3. Translation packets are closer by an extra logarithmic factor

For `|k|<=q/2`,

\[
|\zeta_q^k-1|
\le \frac{2\pi|k|}{q}.
\tag{19}
\]

Combining (7), (18), and (19) yields, uniformly for `1<=|k|<=K<=(log q)^A`,

\[
|F_q^+(k)-F_q(k)|
\ll_A
\frac{1+\log(2+|k|)}{q\log q}.
\tag{20}
\]

Therefore the positive-frequency packet

\[
\mathcal F_{q,K}:=(F_q(1),\ldots,F_q(K))
\tag{21}
\]

and its translated control satisfy

\[
\boxed{
\|\mathcal F_{q,K}^+-\mathcal F_{q,K}\|_\infty
\ll_A
\frac{1+\log(2+K)}{q\log q}.
}
\tag{22}
\]

The same conclusion holds for the symmetric packet `|k|<=K` because negative modes are complex conjugates.

This sharpens the topology statement of PC-306 in the entire polylogarithmic regime. The previous source-free estimate was `O(K/q)`. Equation (22) shows that the canonical prime source is much more translation-flat than an arbitrary vertex subset: the low and polylogarithmic modes are already almost uniform because the only finite logarithmic corrections come from the smooth `Li` density.

## 4. Fixed modes have an explicit universal limit

For a fixed nonzero integer `k`, only the first coefficient of (12) is needed. Since

\[
P_1(u)=-(1+u),
\tag{23}
\]

and the constant Fourier mode vanishes,

\[
F_q(k)
=
\frac{C_k}{\log q}
+O_k((\log q)^{-2}),
\qquad
C_k:=-\int_0^1 e^{2\pi i kt}\log t\,dt.
\tag{24}
\]

For `k>0`, elementary sine/cosine integration gives

\[
\boxed{
C_k
=
\frac{
\operatorname{Si}(2\pi k)
+i\,[\gamma+\log(2\pi k)-\operatorname{Ci}(2\pi k)]
}{2\pi k}.
}
\tag{25}
\]

In particular `C_1!=0`. From (7),

\[
\boxed{
q\log q\,[F_q^+(k)-F_q(k)]
\longrightarrow
2\pi i k C_k.
}
\tag{26}
\]

Thus for every fixed `K>=1`,

\[
\|\mathcal F_{q,K}^+-\mathcal F_{q,K}\|_\infty
=\Theta_K((q\log q)^{-1}).
\tag{27}
\]

A direct scalar audit is available at `k=1`:

\[
2\pi|C_1|
\approx 2.82016098079,
\tag{28}
\]

so

\[
q\log q\,|F_q^+(1)-F_q(1)|
\to 2.82016098079\ldots.
\tag{29}
\]

The convergence is slow because the next `Li` corrections are only logarithmically smaller, but the limiting constant is explicit and source-independent once the normalized prime intensity has been fixed.

## 5. Conditioning consequence

Let `G_q` be any map from the first `K` oriented Fourier coordinates, equipped with sup norm, into a metric space `(Y,d_Y)`. Suppose the prime source and its translated control are required to remain a fixed distance apart:

\[
d_Y\bigl(G_q(\mathcal F_{q,K}),G_q(\mathcal F_{q,K}^+)\bigr)
\ge \delta>0.
\tag{30}
\]

Then (22) forces

\[
\boxed{
\operatorname{Lip}(G_q)
\gg_{A,\delta}
\frac{q\log q}{1+\log(2+K)}
\qquad
(K\le(\log q)^A).
}
\tag{31}
\]

For fixed `K`, (27) shows that the order `q log q` is sharp for this matched pair. If `K` is allowed to be any fixed power of `log q`, then

\[
1+\log(2+K)=O_A(\log\log q),
\tag{32}
\]

so every fixed-margin discriminator still consumes at least

\[
\Omega_A\!\left(
\frac{q\log q}{\log\log q}
\right)
\tag{33}
\]

conditioning. A polylogarithmic increase in ordinary Fourier bandwidth therefore does not convert the exact cyclotomic encoding of PC-306 into a uniformly stable carrier.

## 6. Prior-art and novelty audit

The analytic-number-theory input is classical. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge University Press (2006), Chapter 6, develops the prime number theorem and logarithmic-integral approximation used in PC-273--PC-276. The quantitative form (9), partial summation, and the finite `1/log q` expansion are not new claims here. The Fourier estimate (15) is an elementary integration-by-parts bound for logarithmic-polynomial densities.

A targeted literature check for fixed-frequency Fourier coefficients of the scaled prime empirical measure found no independent nonclassical ingredient needed for (18): the result is an immediate harmonic readout of the normalized `Li` source already classified in PC-276. Accordingly no novelty is claimed for the PNT, weighted prime sums, Fourier decay, sine/cosine integrals, or logarithmic-integral asymptotics, and no new `SOURCES.md` dependency is introduced.

The durable project-local content is the conditioning consequence. PC-306 supplied a matched **disjoint** source pair whose Fourier packets become close, but its `O(K/q)` bound was agnostic to prime distribution. Combining that exact translation control with the all-orders `Li` classicalization shows that the same pair is much closer throughout every fixed polylogarithmic bandwidth. This sharply restricts the live proposal that adding a modestly growing collection of oriented modes might stabilize the exact source information before an RH-sensitive downstream operation acts.

## 7. Boundaries, controls and falsification

The theorem is intentionally limited to ordinary additive Fourier coordinates and bandwidth

\[
K\le(\log q)^A
\tag{34}
\]

for fixed `A`. It does not control super-polylogarithmic bandwidth, shrinking singular windows, unbounded mode-dependent weights, exact `Li`-centered residuals, cross-level operators, or nonlinear constructions that couple levels before this packet is formed. Those remain legitimate escape directions under the canonical research mandate.

Nor does (31) say that an exploding amplifier cannot be defined. It says that any such amplifier must pay an explicit conditioning cost on a matched, maximally separated source pair. If one deliberately subtracts the exact normalized `Li` source and amplifies the residual until the classical explicit-formula oscillations become visible, that is a different channel; zero sensitivity inherited solely from the prime-counting remainder remains classical explicit-formula data unless the Prime-Circle geometry contributes an independent mechanism.

The result has three direct audit tests:

1. For fixed `k`, numerical prime sums must satisfy (26); at `k=1` the normalized translation difference must tend to the constant in (28).
2. For every fixed `A`, a sequence `k_q<=(log q)^A` with `|F_q(k_q)|` asymptotically larger than `(1+log(2+k_q))/(k_q log q)` by an unbounded factor would falsify the uniform estimate (18).
3. A fixed-margin downstream discriminator with Lipschitz constants `o(q log q/log log q)` on a polylogarithmic packet would contradict (22).

## 8. Consequence for the research line

The current boundary is stronger than “exact reconstruction is ill-conditioned.” At the canonical prime source, **every fixed-power polylogarithmic packet of ordinary oriented Fourier modes remains almost invariant under a one-vertex rotation of a completely disjoint support**, at scale at most `log log q/(q log q)`. This closeness is forced by the smooth logarithmic-integral source hierarchy rather than by zeta zeros.

Therefore a viable pre-decoding carrier cannot rely on merely adding polylogarithmically many standard Fourier coordinates and then applying a well-conditioned downstream map. To escape this obstruction it must change the observation regime in a mathematically source-forced way: substantially larger bandwidth, singular or nonlocal weighting with its conditioning accounted for, exact `Li` subtraction followed by a genuinely new geometric coupling, or cross-level/mixed-conductor structure that is not reproducible by unstable per-level source decoding followed by post-processing.