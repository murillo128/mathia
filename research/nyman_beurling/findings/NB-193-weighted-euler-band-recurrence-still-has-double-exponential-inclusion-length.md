# NB-193 — Weighted Euler-band recurrence still has double-exponential inclusion length

**Date:** 2026-09-17  
**Status:** `DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + WEIGHTED-RECURRENCE + EFFECTIVE-DIMENSION + METRIC-ENTROPY + NB-192-STRENGTHENING`.

`NB-192` shows that the coordinatewise common-return mechanism used by `NB-191` is violently nonuniform when `a -> 0`: requiring every active prime phase in one Euler band to return close to one gives a syndetic inclusion length whose logarithm is already `>> a exp(r_0/a)`. Its main positive escape is explicit: perhaps one need not recur exponentially many phases coordinatewise; perhaps it is enough to preserve the true-amplitude band mask **on average** in the `ell^1` coefficient topology of `NB-190`.

That direct aggregate escape does not improve the worst-gap scale. The reason is not coordinatewise rigidity but concentration of Haar measure. For a rationally independent phase family with positive weights `w_j`, an aggregate return

\[
\sum_j w_j |e^{-it\lambda_j}-1|\le \eta
\]

occupies exponentially small Haar volume whenever `eta` is below the Haar mean chord length `4/pi`, with exponent governed by the effective dimension

\[
D_{\rm eff}(w):=\frac1{\sum_j w_j^2}.
\]

If such aggregate returns are syndetic with inclusion length `L`, then a length-`L` orbit segment must cover the whole torus after multiplication by that small target set. A one-dimensional orbit can do so only after paying the reciprocal target volume. More precisely, for every `0<eta<4/pi` and every `0<delta<4/pi-eta`,

\[
\boxed{
L
\ge
\frac{\delta}{\lambda_{\max}}
\left[
\exp\!\left(
\frac{(4/\pi-\eta-\delta)^2}
{2\sum_j w_j^2}
\right)-1
\right].
}
\tag{1}
\]

For the normalized true-amplitude prime weights in the first `NB-189` Euler band, `D_eff(w) asymp m_a`, where

\[
m_a\asymp a e^{r_0/a}
\]

is the number of prime channels in that fixed log-width band. Higher prime powers carry a vanishing fraction of the band mass. Consequently, if

\[
\mathcal A_a(t)
:=
\frac1{\theta_{0,a}}
\sum_{n\in S_{0,a}}
\alpha_{n,a}
|e^{-it\log n}-1|
\]

and `L_a^avg(eta)` is any syndetic inclusion length for the aggregate-return set `{t: A_a(t)<=eta}`, then for every fixed `0<eta<1`,

\[
\boxed{
\log L_a^{\rm avg}(\eta)
\gg_{r_0,\Delta,\eta}
 a e^{r_0/a}.
}
\tag{2}
\]

Thus replacing the `NB-191` max-phase return by the most direct **true-source-weighted `ell^1` band average** still leaves the same double-exponential worst-gap scale as `NB-192`. The corresponding guaranteed-block condition again has the log-log floor

\[
\boxed{
a
\ge
\frac{r_0}
{\log\log T+\log\log\log T+O_{r_0,\Delta,\eta}(1)}.
}
\tag{3}
\]

This remains a theorem about a recurrence/transplant architecture, not about arbitrary high-block Fourier--Stieltjes synthesis. In particular, signed cancellation after coefficient aggregation, a different response topology, or an exceptionally early return in the specific block `[T,2T]` remain outside the claim.

## 1. A general weighted-return filling bound

Let `lambda_1,...,lambda_m>0` be linearly independent over `Q`, let

\[
w_j>0,
\qquad
\sum_{j=1}^m w_j=1,
\tag{4}
\]

and define the dense phase flow

\[
\Phi(t)
:=
(e^{-it\lambda_1},\ldots,e^{-it\lambda_m})
\in\mathbb T^m.
\tag{5}
\]

For `z=(z_1,...,z_m)`, put

\[
F_w(z)
:=
\sum_{j=1}^m w_j|z_j-1|,
\qquad
G_w(\eta)
:=
\{z\in\mathbb T^m:F_w(z)\le\eta\}.
\tag{6}
\]

The weighted return set is

\[
\mathcal R_w(\eta)
:=
\{t\in\mathbb R:\Phi(t)\in G_w(\eta)\}.
\tag{7}
\]

Assume every real interval of length `L` meets `R_w(eta)`. Then

\[
\boxed{
\mathbb T^m
=
\Phi([0,L])G_w(\eta).
}
\tag{8}
\]

Indeed, fix `y in T^m`. Density of the full flow supplies a sequence `x_n` with `Phi(-x_n)->y`. Choose

\[
\tau_n\in[x_n,x_n+L]
\quad\text{with}\quad
\Phi(\tau_n)\in G_w(\eta),
\]

and put `s_n=tau_n-x_n in [0,L]`. Passing to a subsequence, `s_n->s` and `Phi(tau_n)->g in G_w(eta)`. Since

\[
\Phi(s_n)=\Phi(\tau_n)\Phi(-x_n),
\]

we obtain `Phi(s)=gy`, hence `y in Phi(s)G_w(eta)` because `G_w(eta)` is invariant under coordinatewise inversion. This proves (8).

Let

\[
\lambda_{\max}:=\max_j\lambda_j.
\tag{9}
\]

The flow is `lambda_max`-Lipschitz for the product chord metric

\[
d_\infty(z,z'):=\max_j|z_j-z'_j|.
\]

Sample `[0,L]` at mesh at most `delta/lambda_max`. At most

\[
J
\le
1+\frac{L\lambda_{\max}}{\delta}
\tag{10}
\]

sample points suffice. If `d_infty(Phi(s),Phi(s_r))<=delta`, then multiplication by `Phi(s_r)^(-1)Phi(s)` can increase `F_w` by at most `delta`. Therefore (8) implies that `J` translates of `G_w(eta+delta)` cover the torus. Writing `m_T` for normalized Haar measure,

\[
1
\le
J\,m_T(G_w(\eta+\delta)).
\tag{11}
\]

The problem is therefore reduced to the Haar volume of a weighted chord-average sublevel set.

## 2. The aggregate target has exponentially small Haar volume

Under Haar measure on `T^m`, the coordinates `Z_j` are independent and uniform on the circle. Put

\[
X_j:=|Z_j-1|.
\]

Then `0<=X_j<=2` and

\[
\mathbb E X_j
=
\frac1{2\pi}
\int_0^{2\pi}|e^{i\vartheta}-1|\,d\vartheta
=
\frac4\pi.
\tag{12}
\]

The standard bounded-sum exponential estimate gives, for every `rho<4/pi`,

\[
\boxed{
m_T(G_w(\rho))
\le
\exp\!\left(
-\frac{(4/\pi-\rho)^2}
{2\sum_j w_j^2}
\right).
}
\tag{13}
\]

For completeness, this is just the elementary Hoeffding calculation applied to the independent variables `w_j X_j in [0,2w_j]`: centering at their common weighted mean `4/pi`, the bounded-mgf inequality for an interval of length `2w_j` gives

\[
\mathbb P\!\left(
\sum_j w_jX_j-\frac4\pi\le-d
\right)
\le
\exp\!\left(
-\frac{d^2}{2\sum_jw_j^2}
\right).
\tag{14}
\]

No dynamical equidistribution rate enters (13); it is a static product-Haar volume estimate.

Combining (11) with (13), with `rho=eta+delta<4/pi`, yields

\[
1+\frac{L\lambda_{\max}}{\delta}
\ge
\exp\!\left(
\frac{(4/\pi-\eta-\delta)^2}
{2\sum_jw_j^2}
\right),
\]

which is exactly (1).

A convenient fixed choice is

\[
\delta=\frac12\left(\frac4\pi-\eta\right).
\tag{15}
\]

Then

\[
\log L
\ge
\frac{(4/\pi-\eta)^2}{8}
D_{\rm eff}(w)
-
\log\lambda_{\max}
+O_\eta(1).
\tag{16}
\]

So the relevant dimension for **weighted** recurrence is not the raw number of frequencies by itself but the participation ratio `D_eff`. Concentrating the weights can genuinely reduce the entropy tariff; diffuse positive source weights cannot.

## 3. One true Euler band has exponential effective dimension

Return to the first balanced band from `NB-189`--`NB-192`,

\[
S_{0,a}
=
\left\{
n:\frac{r_0}{a}
\le\log n<
\frac{r_0}{a}+\Delta
\right\},
\tag{17}
\]

where `0<r_0<r_1<2` and `Delta>0` are fixed. Throughout this band `M_a(log n)=2` for small `a`, so the normalized Euler--Wiener weights are proportional to

\[
\Lambda(n)n^{-1-a}.
\tag{18}
\]

Let

\[
\mathcal Q_a
:=
\{p\text{ prime}:p\in S_{0,a}\},
\qquad
m_a:=|\mathcal Q_a|.
\tag{19}
\]

As in `NB-192`, unique factorization makes the frequencies `{log p:p in Q_a}` rationally independent, and the PNT gives

\[
\boxed{
m_a
=
\left(
\frac{e^\Delta-1}{r_0}+o(1)
\right)
 a e^{r_0/a}.
}
\tag{20}
\]

Normalize the prime weights within `Q_a`:

\[
w_{p,a}
:=
\frac{(\log p)p^{-1-a}}
{\sum_{q\in\mathcal Q_a}(\log q)q^{-1-a}}.
\tag{21}
\]

All these weights are comparable. If `p,q in Q_a`, then

\[
\frac{(\log p)p^{-1-a}}
{(\log q)q^{-1-a}}
\le
\frac{r_0/a+\Delta}{r_0/a}
 e^{(1+a)\Delta}
\le C_{r_0,\Delta}
\tag{22}
\]

for small `a`. Hence

\[
\max_{p\in\mathcal Q_a}w_{p,a}
\ll_{r_0,\Delta}\frac1{m_a},
\]

and therefore

\[
\boxed{
D_{\rm eff}(w_a)
=
\frac1{\sum_{p\in\mathcal Q_a}w_{p,a}^2}
\gg_{r_0,\Delta}m_a.
}
\tag{23}
\]

Thus positive true-amplitude weighting does **not** collapse the phase dimension of a fixed log-width prime band. Its effective dimension is still exponential in `1/a`.

## 4. Higher prime powers do not dilute the obstruction

Let

\[
\theta_{0,a}
:=
\sum_{n\in S_{0,a}}\alpha_{n,a},
\qquad
q_a
:=
\frac{
\sum_{p\in\mathcal Q_a}\alpha_{p,a}
}{\theta_{0,a}}.
\tag{24}
\]

Then

\[
\boxed{q_a\to1.}
\tag{25}
\]

A direct estimate suffices. Put `x=exp(r_0/a)` and `y=e^Delta x`. The prime contribution to the unnormalized band mass is bounded below, by the PNT, by a positive constant multiple of

\[
x^{-1-a}\sum_{x\le p<y}\log p
\asymp
x^{-a}
\asymp 1.
\tag{26}
\]

For prime powers of exponent at least two,

\[
\sum_{\substack{x\le p^k<y\\k\ge2}}
\frac{\log p}{p^{k(1+a)}}
\le
x^{-1-a}
\sum_{\substack{p^k<y\\k\ge2}}\log p
\ll
x^{-1/2-a}(\log x)^2
=o(1).
\tag{27}
\]

The common factor `M_a=2` and the global normalization `W(a)` cancel in the ratio, proving (25).

Now define the full true-source weighted phase defect

\[
\mathcal A_a(t)
:=
\frac1{\theta_{0,a}}
\sum_{n\in S_{0,a}}
\alpha_{n,a}|e^{-it\log n}-1|.
\tag{28}
\]

If `A_a(t)<=eta`, then its prime subaverage satisfies

\[
\sum_{p\in\mathcal Q_a}
w_{p,a}|e^{-it\log p}-1|
\le
\frac{\eta}{q_a}.
\tag{29}
\]

Fix `0<eta<1`. Since `q_a->1` and `1<4/pi`, the right side of (29) stays a fixed positive distance below `4/pi` for all sufficiently small `a`. Therefore any inclusion length for the full-band aggregate-return set is also an inclusion length for a prime weighted-return set to which (16), (20), and (23) apply. Since

\[
\lambda_{\max}
<\frac{r_0}{a}+\Delta,
\tag{30}
\]

we obtain

\[
\log L_a^{\rm avg}(\eta)
\gg_{r_0,\Delta,\eta}
m_a
\asymp
 a e^{r_0/a},
\tag{31}
\]

which proves (2).

The same inversion as in `NB-192` then gives (3): if this aggregate-recurrence mechanism is to be guaranteed inside a block of available length `T`, its inclusion length must satisfy `L_a^avg(eta) lesssim T`, forcing

\[
a e^{r_0/a}\lesssim\log T
\]

and hence

\[
\frac{r_0}{a}
\le
\log\log T+
\log\log\log T+O(1).
\]

## 5. Relation to the NB-190 coefficient topology

The aggregate defect (28) is not an invented metric. The normalized target row for the first band is

\[
\frac{\alpha_{n,a}}{\theta_{0,a}}
\mathbf 1_{S_{0,a}}(n).
\]

If that exact row is translated in height by `tau`, its in-band `ell^1` coefficient mismatch is **exactly**

\[
\frac1{\theta_{0,a}}
\sum_{n\in S_{0,a}}
\alpha_{n,a}|e^{-i\tau\log n}-1|
=
\mathcal A_a(\tau).
\tag{32}
\]

This is precisely the source-weighted coefficient currency used by `NB-190`. Therefore the most direct proposed relaxation of `NB-191`—replace uniform phase recurrence by small **average true-amplitude phase error**—does not lower the syndetic transport scale. The target set is larger than the coordinatewise Bohr box, but its Haar volume remains exponentially small because the positive source mass is spread over exponentially many comparable prime coordinates.

Equation (32) also explains why the threshold `eta<1` is the relevant one here. `NB-190` works at fixed coefficient errors below one in order to retain a nontrivial normalized band, and the whole interval `(0,1)` lies strictly below the Haar mean chord `4/pi` needed for the concentration bound.

## Generality audit

**Generality audited.** Claims (1) and (13) are generic facts about a dense one-parameter flow in a product torus and a positive weighted `ell^1` chord target. Their controlling quantity `D_eff=(sum w_j^2)^(-1)` is a generic participation ratio. They do not use primes, zeta, or Nyman--Beurling geometry.

The source-specific step is (20)--(25): the actual Euler acquisition band contains `m_a asymp a exp(r_0/a)` rationally independent prime-log coordinates, its true positive amplitudes are diffuse enough that `D_eff asymp m_a`, and higher prime powers are negligible in that band. Those facts convert the generic reciprocal-target-volume tariff into the same double-exponential `a`-scale that `NB-192` found for coordinatewise recurrence.

## Prior-art audit

The ingredients surrounding the proof are classical. Quantitative filling times for linear torus flows and Bohr recurrence are standard, as already audited in `NB-192`. The exponential estimate (13) is the usual bounded-independent-sum concentration inequality; equivalently it is the classical Hoeffding bound applied under product Haar measure. A focused search for weighted Bohr-return sets, weighted torus almost periods, linear-flow shrinking targets, and concentration estimates for aggregate phase defects found neighboring literature on Bohr sets, torus filling times, and toral large deviations, but no result needed beyond these standard ingredients and no source stating the line-specific Euler-band consequence (2).

The proof above derives the exact bound used here from the product-Haar model, while the only arithmetic asymptotic input is the PNT already anchored in `research/nyman_beurling/SOURCES.md`. No new external theorem is load-bearing, so `SOURCES.md` remains unchanged. The absence of a paper with the same Euler-band formulation is not used as evidence of novelty.

## Self-adversarial audit

The strongest tempting overclaim would be that (2) lower-bounds **all** high-block scalar acquisition. It does not. The theorem prices only recurrence/transplant mechanisms in which the normalized band mask is preserved through positive `ell^1` phase closeness of a translated seed. An arbitrary Fourier--Stieltjes measure supported directly in `[T,2T]` need not be a translate of the low-height seed, and its coefficient errors need not factor through (28).

Likewise, (13) relies on positive weights and absolute coefficient mismatch. If an architecture first aggregates channels with complex signs and only then measures response error, phase cancellation can enlarge the admissible target set dramatically. Such a construction would leave the `NB-190` coefficient topology and must be charged in a different source-safe currency before it can count as an escape.

Finally, this is still a **worst-gap** statement. A large inclusion length does not prove that the particular block `[T,2T]` contains no aggregate return; it proves that no theorem based only on syndetic recurrence of the full source-weighted band can guarantee one below the scale in (2). Arithmetic information about the specific block could still produce anomalously early returns.

## Research consequence

`NB-192` left two natural recurrence escapes: abandon coordinatewise phase matching in favor of weighted/band-averaged matching, or exploit a special early return in the actual dyadic block. The first escape is now closed in the exact positive `ell^1` coefficient topology of `NB-190`: diffuse true Euler weights retain exponential effective dimension, so average phase matching has the same double-exponential syndetic threshold.

The live acquisition frontier is therefore narrower. A continuation must either exploit **signed/complex aggregate cancellation in a demonstrably source-safe response topology**, prove or disprove genuinely exceptional early returns for the specific prime-log block `[T,2T]`, or bypass recurrence entirely with a direct high-block synthesis. None of those alternatives is supplied by generic Bohr almost periodicity.