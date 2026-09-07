# AF-189 — First reachable Euler resonance gives the sharp parity-cluster band discrepancy

**Status:** `EXACT-DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-188 determines the logarithmic fidelity exponent of the adaptive parity controls but leaves a constant-factor gap in the full vertical-band discrepancy. Under exactly the same asymptotic hypotheses, that gap closes: the first harmonic resonance accessible to the band is asymptotically the whole supremum.

Fix

\[
x>0,
\qquad
\sigma>0,
\qquad
r=e^{-\sigma x}\in(0,1),
\tag{1}
\]

let `\delta\downarrow0`, and let positive integers `q=q_\delta` and `m=m_\delta` satisfy

\[
q_\delta\to\infty,
\qquad
\frac{m_\delta}{q_\delta^2}\to\infty,
\qquad
m_\delta q_\delta\delta\to0.
\tag{2}
\]

For the normalized parity-split controls

\[
\nu_\delta
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta},
\tag{3}
\]

and the Euler local logarithm

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+it,
\tag{4}
\]

put

\[
T_\delta=\frac{\pi}{q_\delta\delta},
\qquad
D_\delta=
\sup_{|t|\le T_\delta}
\left|
\int F_{\sigma+it}(u)\,d\nu_\delta(u)
\right|.
\tag{5}
\]

Then

\[
\boxed{
D_\delta
=(2+o(1))\frac{r^{q_\delta}}{q_\delta}.
}
\tag{6}
\]

Thus AF-188's band-edge lower bound is asymptotically sharp, including its leading constant. The supremum cannot gain a fixed factor by combining many nearby harmonics: the high-order parity filter resolves the individual reciprocal resonances faster than their spacing closes, and the strictly decreasing Euler weight `r^k/k` makes the first reachable one, `k=q_\delta`, dominant.

For the integer logarithmic schedule

\[
q_\delta=\lfloor c\log(1/\delta)\rfloor,
\qquad c>0,
\tag{7}
\]

the sharp statement remains naturally discrete:

\[
\boxed{
D_\delta
=(2+o(1))
\frac{e^{-\sigma x\lfloor c\log(1/\delta)\rfloor}}
{\lfloor c\log(1/\delta)\rfloor}.
}
\tag{8}
\]

Consequently

\[
D_\delta
=\Theta\!\left(
\frac{\delta^{c\sigma x}}{\log(1/\delta)}
\right),
\tag{9}
\]

recovering AF-188's algebraic profile while identifying the exact leading asymptotic before integer-rounding effects. One should not replace `(8)` by an asymptotic equivalent with `\delta^{c\sigma x}` alone: the bounded fractional part of `c\log(1/\delta)` produces a bounded multiplicative lattice oscillation.

The theorem is specific to this matched-control family and this Euler harmonic weight. It is not a full inverse theorem for generalized-prime systems and does not establish rational-prime specificity.

## Exact response and the remaining upper-bound problem

Write `q=q_\delta`, `m=m_\delta`, and

\[
R_\delta(t)
=
\int F_{\sigma+it}(u)\,d\nu_\delta(u).
\tag{10}
\]

The exact expansion used in AF-188 is

\[
R_\delta(t)
=
2^{1-m}
\sum_{k\ge1}
\frac{r^k e^{-iktx}}{k}
\left(e^{-k(\sigma+it)\delta}-1\right)^m.
\tag{11}
\]

Set

\[
\theta=t\delta,
\qquad
b_{k,\delta}(\theta)
=
\frac{|1-e^{-k\sigma\delta}e^{-ik\theta}|}{2}.
\tag{12}
\]

Then

\[
|R_\delta(t)|
\le
2\sum_{k\ge1}\frac{r^k}{k}b_{k,\delta}(\theta)^m,
\tag{13}
\]

and

\[
b_{k,\delta}(\theta)^2
=
e^{-k\sigma\delta}\sin^2\frac{k\theta}{2}
+
\frac{(1-e^{-k\sigma\delta})^2}{4}.
\tag{14}
\]

AF-188 already proves uniformly for `|\theta|\le\pi/q` that

\[
2\sum_{k<q}\frac{r^k}{k}b_{k,\delta}(\theta)^m
=o\!\left(\frac{r^q}{q}\right).
\tag{15}
\]

Its upper bound treated every `k\ge q` only with `b_{k,\delta}\le1`, producing the non-sharp factor `1/(1-r)`. The missing fact is that, in the relevant part of the band, the peaks `k\theta\approx\pi` are asymptotically disjoint.

## Gaussian localization of the first resonance comb

Because `(2)` implies `q\delta\to0`, for all sufficiently small `\delta` and

\[
q\le k\le\frac{3q}{2}
\tag{16}
\]

we have `\rho_k:=e^{-k\sigma\delta}\ge1/2`. By symmetry it is enough to take `0\le\theta\le\pi/q`. Put `\phi=k\theta-\pi`; then `|\phi|\le\pi` on `(16)`. Rewriting `(14)` around the antipodal point gives

\[
b_{k,\delta}(\theta)^2
=
\frac{(1+\rho_k)^2}{4}
-
\rho_k\sin^2\frac{\phi}{2}
\le
1-\rho_k\sin^2\frac{\phi}{2}.
\tag{17}
\]

Since `|\sin(\phi/2)|\ge |\phi|/\pi` for `|\phi|\le\pi`, there is an absolute `c>0` such that

\[
\boxed{
b_{k,\delta}(\theta)^m
\le
\exp[-c m(k\theta-\pi)^2]}
\tag{18}
\]

uniformly on `(16)` and the whole band.

If `0\le\theta\le\pi/(2q)`, then `k\theta\le3\pi/4` throughout `(16)`, so the sum of the terms in `(18)` is `O(qe^{-c'm})=o(1)`. If instead `\pi/(2q)\le\theta\le\pi/q`, put

\[
y=\frac{\pi}{\theta},
\qquad
a=c m\theta^2.
\tag{19}
\]

Then

\[
\exp[-c m(k\theta-\pi)^2]
=
\exp[-a(k-y)^2],
\qquad
a\ge\frac{c\pi^2}{4}\frac{m}{q^2}\to\infty.
\tag{20}
\]

For every real `y`, choosing a nearest integer shows

\[
\sum_{k\in\mathbb Z}e^{-a(k-y)^2}
\le
1+2\sum_{j\ge1}e^{-a(j-1/2)^2}
=1+o(1)
\tag{21}
\]

uniformly in `y`. Therefore

\[
\boxed{
\sup_{|\theta|\le\pi/q}
\sum_{q\le k\le3q/2}
b_{k,\delta}(\theta)^m
\le1+o(1).
}
\tag{22}
\]

This is the new localization step: asymptotically, at most one of the first reachable harmonic peaks can contribute with order-one filter amplitude at any vertical phase.

## Sharp band upper bound

For `k\ge q`, the Euler weights decrease:

\[
\frac{r^k}{k}\le\frac{r^q}{q}.
\tag{23}
\]

Hence `(22)` implies

\[
2\sum_{q\le k\le3q/2}
\frac{r^k}{k}b_{k,\delta}(\theta)^m
\le
(2+o(1))\frac{r^q}{q}
\tag{24}
\]

uniformly on the band. The remaining tail needs no localization:

\[
2\sum_{k>3q/2}
\frac{r^k}{k}b_{k,\delta}(\theta)^m
\le
2\sum_{k>3q/2}\frac{r^k}{k}
=o\!\left(\frac{r^q}{q}\right),
\tag{25}
\]

because the relative geometric factor is `O(r^{q/2})`. Combining `(15)`, `(24)`, and `(25)` gives

\[
D_\delta
\le
(2+o(1))\frac{r^q}{q}.
\tag{26}
\]

AF-188 already proves at the band edge `t=T_\delta` that

\[
|R_\delta(T_\delta)|
=(2+o(1))\frac{r^q}{q}.
\tag{27}
\]

Equations `(26)` and `(27)` prove `(6)`.

## Structural interpretation

Near `k\asymp q`, neighboring reciprocal resonances are separated in phase by order `q^{-2}`. Equation `(18)` gives a peak width of order `m^{-1/2}` in `k\theta-\pi`, hence order `(q\sqrt m)^{-1}` in `\theta`. The hypothesis

\[
\frac{m}{q^2}\to\infty
\tag{28}
\]

is exactly the scale separation making those peaks asymptotically disjoint.

Once peak overlap disappears, the destination observable is not controlled merely by a derivative envelope. Its discrete harmonic architecture orders the surviving channels. For the Euler logarithm the weights `r^k/k` strictly decrease, so the first harmonic admitted by the bandwidth controls the supremum. This sharpens the lesson of AF-187--AF-188: source complexity, resolution, and regularity do not determine fidelity without the kernel's internal harmonic structure.

## Falsification and boundaries

The theorem uses all of the following features.

- The source pair is the specific positive parity-split finite-difference family of AF-182. Other source classes may have different cancellation mechanisms.
- The Euler logarithm supplies monotonically decreasing magnitudes `r^k/k`. A general Laplace series can have non-monotone weights or coefficient cancellation, so its maximizing resonance need not be the first accessible one.
- The observation is a continuous vertical band. A discrete frequency set may miss the reciprocal resonance and requires a separate aliasing/Diophantine analysis.
- The argument requires `m/q^2\to\infty`; without it, neighboring resonance peaks may overlap.
- The real-damping condition `mq\delta\to0` remains necessary for the AF-188 edge lower bound used here.
- The result distinguishes this matched pair after Euler-log compression, not the rational primes from generalized Euler-product systems. The prime-power harmonic ladder is shared by that wider category.

Equation `(6)` is therefore a sharp forward discrepancy theorem, not a stable inverse theorem. It supplies one exact obstruction profile that any proposed uniform recovery modulus must dominate.

## Prior art and novelty assessment

The ingredients have strong classical and modern prior art. NIST Digital Library of Mathematical Functions, §25.2(iv), Eq. 25.2.11, records the Euler product for `\zeta(s)` in `\Re(s)>1`; the local series used here is the elementary logarithm of one Euler factor. David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, is foundational prior art for the inverse relation between bandwidth and source spacing. Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, proves sharp clustered partial-Fourier conditioning bounds whose exponent depends on cluster size.

The finite-difference Fourier multiplier and Gaussian localization estimate `(18)` are elementary. A targeted literature search did not identify an authoritative source stating the exact specialized asymptotic `(6)` for the Euler logarithm and the AF-182 positive parity controls. That search is not evidence of priority, and no novelty claim is made. The durable content is the exact sharpening of the already-defined Arithmetic Fidelity control problem.

## Dependencies and evidence boundary

The proof depends on AF-188's exact response formula, its uniform `k<q` suppression `(15)`, and its band-edge asymptotic `(27)`. The new step is the uniform one-resonance estimate `(22)` and the resulting sharp upper constant.

No numerical experiment is used as evidence. No RH consequence, rational-prime uniqueness statement, or full generalized-prime reconstruction theorem follows from this finding.
