# AF-324 — Bounded prime height quantifies fixed-time phase filling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-CONSEQUENCE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SUPPORT-HEIGHT`, `QUANTITATIVE-DENSITY`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-323 proves a qualitative support-uniform obstruction: at every fixed nonzero time, varying rational-prime supports are tail-dense in every finite phase torus. The missing resource variable is the **height of the allowed prime support**. Classical prime-gap technology gives a direct quantitative law for it.

Fix `tau != 0` and an integer `m >= 1`. Equip `S^1` with angular distance

\[
d_{\mathbb T}(e^{i\alpha},e^{i\beta})
=\min_{k\in\mathbb Z}|\alpha-\beta+2\pi k|
\]

and `(S^1)^m` with the corresponding sup metric. For `H >= 2`, let

\[
\mathcal Q_{m,\tau}(H)
=
\left\{
(p_1^{-i\tau},\ldots,p_m^{-i\tau}):
 p_j\le H\ \text{distinct rational primes}
\right\},
\tag{1}
\]

and define its covering radius

\[
\rho_{m,\tau}(H)
=
\sup_{z\in(S^1)^m}
\inf_{q\in\mathcal Q_{m,\tau}(H)}d_\infty(z,q).
\tag{2}
\]

Then, for fixed `m` and `tau`,

\[
\boxed{
\frac{\pi}{\pi(H)}
\le
\rho_{m,\tau}(H)
\ll_{m,\tau}
H^{-19/40}
}
\qquad(H\to\infty),
\tag{3}
\]

where `pi(H)` is the prime-counting function. In particular the prime number theorem turns the lower bound into

\[
\rho_{m,\tau}(H)
\ge
(\pi+o(1))\frac{\log H}{H}.
\tag{4}
\]

The exponent `19/40=0.475` in the upper bound is not intrinsic to Arithmetic Fidelity. It is exactly the complement of the peer-reviewed Baker--Harman--Pintz short-interval exponent `21/40=0.525`: every sufficiently large interval

\[
[x,x+x^{21/40}]
\]

contains a prime. More generally, any theorem asserting a prime in `[x,x+x^theta]` for all sufficiently large `x`, with `theta<1`, gives

\[
\boxed{
\rho_{m,\tau}(H)
\ll_{m,\tau}
H^{-(1-\theta)}.
}
\tag{5}
\]

Thus AF-323's topological density has an explicit finite-support version: **a maximum-prime-height budget `H` still allows every fixed finite phase configuration to be reproduced to polynomial accuracy**. The support-height mark prevents literal unrestricted collapse, but it buys only a shrinking phase-space margin unless the downstream theorem consumes that mark quantitatively.

For the eight-point singular problem of AF-320--AF-323, let

\[
\mathcal D
=
\{Z\in(S^1)^8:s_1(Z)=e_4(Z)=s_3(Z)=0\}.
\tag{6}
\]

A rotated regular octagon belongs to `mathcal D`. Applying `(3)` to that one target gives distinct primes `p_1,...,p_8 <= H` such that, for every fixed `tau != 0`,

\[
\boxed{
\operatorname{dist}
\bigl((p_1^{-i\tau},\ldots,p_8^{-i\tau}),\mathcal D\bigr)
\ll_\tau H^{-19/40}.
}
\tag{7}
\]

Since `s_1`, `e_4`, and `s_3` are Lipschitz on the compact eight-torus, the same supports satisfy simultaneously

\[
|s_1|+|e_4|+|s_3|
\ll_\tau H^{-19/40}.
\tag{8}
\]

This is a quantitative **near-incidence** theorem, not an exact-incidence theorem. It sharpens the warning from AF-323: arbitrarily good numerical proximity to the deeper singular geometry is forced by ordinary prime distribution as support height grows and therefore cannot by itself decide whether an exact prime hit `s_1=e_4=0` exists.

## 1. One logarithmic period already covers the whole phase circle

Put

\[
L=\frac{2\pi}{|\tau|}.
\tag{9}
\]

The map

\[
x\longmapsto x^{-i\tau}
\tag{10}
\]

traverses the full unit circle once whenever `log x` traverses an interval of length `L`.

To approximate an arbitrary target tuple

\[
z=(z_1,\ldots,z_m)\in(S^1)^m,
\]

reserve `m` disjoint logarithmic periods below `H`, for example

\[
I_j(H)
=
[H e^{-2jL},\ H e^{-(2j-1)L}],
\qquad 1\le j\le m.
\tag{11}
\]

Each interval has logarithmic length `L`. Therefore for every `j` there is an `x_j in I_j(H)` with

\[
x_j^{-i\tau}=z_j.
\tag{12}
\]

The unused logarithmic period between consecutive `I_j` is deliberate: it leaves a gap of order `H` between the corresponding ordinary intervals, so the nearby primes chosen below remain distinct.

## 2. Short-interval primes convert support height into phase resolution

Let `theta<1` be any exponent for which every sufficiently large `[x,x+x^theta]` contains a prime. Choose

\[
p_j\in[x_j,x_j+x_j^\theta].
\tag{13}
\]

For fixed `m,tau`, every `x_j` is a fixed positive multiple of `H`. Since `x_j^theta=o(H)`, for sufficiently large `H` the primes in `(13)` stay below `H` and the `m` chosen intervals remain disjoint. Hence the `p_j` are distinct.

The angular phase error obeys

\[
\begin{aligned}
d_{\mathbb T}(p_j^{-i\tau},z_j)
&\le |\tau|\,|\log(p_j/x_j)|\\
&\le |\tau|\log(1+x_j^{\theta-1})\\
&\le |\tau|x_j^{\theta-1}\\
&\ll_{m,\tau}H^{\theta-1}.
\end{aligned}
\tag{14}
\]

Taking the maximum over coordinates and then the supremum over the target tuple proves `(5)`. Baker--Harman--Pintz give `theta=21/40`, yielding the right-hand inequality in `(3)`.

This proof uses the short-interval theorem only as a worst-case local prime-existence statement. It does not assert that the phases `tau log p mod 2pi` are equidistributed when primes are ordered by size. Indeed logarithmic prime phases have their own non-uniform distribution issues; the present object is the much weaker but decision-relevant **covering radius**.

## 3. Cardinality gives an unavoidable information lower bound

Suppose `mathcal Q_{m,tau}(H)` is a `rho`-net of `(S^1)^m`. Fix arbitrary target values in coordinates `2,...,m` and vary only the first target coordinate. Projecting the approximating tuples to coordinate one shows that

\[
\{p^{-i\tau}:p\le H\}
\tag{15}
\]

must itself be a `rho`-net of `S^1`.

A set of at most `N` points on a circle of circumference `2pi` has angular covering radius at least `pi/N`: one complementary gap has length at least `2pi/N`, and its midpoint is at distance at least `pi/N` from the set. The phase set `(15)` has at most `pi(H)` distinct points. Therefore

\[
\rho_{m,\tau}(H)
\ge\frac{\pi}{\pi(H)},
\tag{16}
\]

which proves the left side of `(3)`. The prime number theorem gives `(4)`.

The gap between `(4)` and the unconditional upper exponent is real. Closing it uniformly would require substantially stronger worst-case information on primes in short intervals; Arithmetic Fidelity does not supply such number theory for free.

## 4. Continuous compressions inherit the same finite-height filling law

Let

\[
C:(S^1)^m\to Y
\]

be continuous into a metric space, and let `omega_C` be any modulus of continuity on the compact torus. Because `mathcal Q_{m,tau}(H)` is a `rho_{m,tau}(H)`-net,

\[
d_H\left(
C(\mathcal Q_{m,\tau}(H)),
C((S^1)^m)
\right)
\le
\omega_C(\rho_{m,\tau}(H)),
\tag{17}
\]

where `d_H` is Hausdorff distance in `Y`. Thus every continuous finite-phase compression approaches its **full ambient image** at a rate controlled directly by the support-height covering radius.

For a Lipschitz compression this becomes

\[
d_H\left(
C(\mathcal Q_{m,\tau}(H)),
C((S^1)^m)
\right)
\ll_{C,m,\tau}H^{-19/40}.
\tag{18}
\]

This is the quantitative form of AF-323's support-varying collapse. If a proposed discriminator relies on an open phase-space gap from some ambient collision stratum, then retaining only the information `p_j<=H` cannot support a larger gap than the prime-height filling scale without using additional arithmetic structure beyond the phase tuple.

## 5. Application to the eight-point deeper singular geometry

Take as target a rotated regular octagon

\[
R=(a,a\zeta_8,\ldots,a\zeta_8^7),
\qquad |a|=1.
\tag{19}
\]

Its root polynomial is

\[
w^8-a^8,
\tag{20}
\]

so all intermediate elementary symmetric coefficients vanish. In particular

\[
s_1(R)=e_4(R)=s_3(R)=0,
\]

and `R in mathcal D`.

Equation `(3)` supplies an eight-prime support whose fixed-time phase tuple lies `O_tau(H^{-19/40})` from `R`, proving `(7)`. On the unit torus each power sum is globally Lipschitz, and `e_4` is a finite multilinear polynomial with bounded derivative. Hence `(8)` follows.

The arithmetic interpretation is deliberately asymmetric with AF-322. For a **fixed** support, Baker-type logarithmic lower bounds prevent the time orbit from approaching four-antipodal geometry faster than a support-dependent inverse power of time. For a **varying** support at fixed time, short-interval prime existence constructs supports approaching the same bad geometry at a support-height-controlled power rate. These are different resource directions and neither estimate implies the other.

Most importantly, `(7)`--`(8)` do not produce an exact point of `mathcal D`, or even an exact point of the middle-singular set `s_1=e_4=0`. The exact rational-prime incidence problem isolated by AF-322 and AF-323 remains untouched.

## Prior art and novelty assessment

No novelty is claimed for primes in short intervals, logarithmic prime phases, covering-radius cardinality bounds, or continuity transfer.

- R. C. Baker, G. Harman, and J. Pintz, **“The Difference Between Consecutive Primes, II,”** *Proceedings of the London Mathematical Society* 83(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`, prove that `[x,x+x^0.525]` contains primes for all sufficiently large `x`. This is the sole deep input behind the unconditional exponent in `(3)`.
- Olivier Ramaré, **“On the behaviour of gamma Log p modulo 1,”** arXiv:`1203.1759` (2012), studies lower bounds for sums of nonnegative periodic functions evaluated at `gamma log p`. It is direct prior art for treating logarithmic prime phases quantitatively. AF-324 asks a different worst-case question: how fine a net is formed when prime size is capped by `H`.
- The prime number theorem supplies only the elementary cardinality asymptotic in `(4)` here.

A newer preprint by Runbo Li, **“The number of primes in short intervals and numerical calculations for Harman's sieve,”** arXiv:`2308.04458` (latest version 2025), claims the stronger interval exponent `0.52`. If that result is used, the same argument mechanically improves `19/40=0.475` in `(3)`, `(7)`, and `(8)` to `0.48`. The peer-reviewed Baker--Harman--Pintz exponent is retained as the unconditional literature anchor for the canonical claim; no part of AF-324 depends on the newer preprint.

The durable Arithmetic Fidelity contribution is therefore not a new prime-gap theorem or a new distribution theorem. It is the **resource translation**: a support-height budget converts directly into a finite-phase covering modulus, which in turn quantifies how quickly actual rational-prime supports can reproduce ambient compression collisions.

## Boundaries and failure modes

- `m` and `tau != 0` are fixed while `H -> infinity`. The constants can deteriorate rapidly as `|tau| -> 0` or `m` grows, because the construction reserves finitely many complete logarithmic periods.
- The upper exponent is only as strong as the imported worst-case short-interval prime theorem. It is not claimed sharp.
- The lower bound `(4)` is information-theoretic and much smaller than the available unconditional upper bound. No matching asymptotic for `rho_{m,tau}(H)` is claimed.
- The theorem varies the **prime support** while holding time fixed. It does not estimate recurrence in time on one fixed support; AF-322 addresses that different direction.
- The chosen primes are distinct but otherwise unconstrained. Ordered supports, prescribed prime gaps, arithmetic progressions, or other extra source restrictions require new input.
- Quantitative density is still not exact incidence. In particular `(7)` and `(8)` cannot decide whether any eight distinct rational primes at a common nonzero time satisfy `s_1=e_4=0` exactly.
- A discontinuous discriminator need not inherit `(17)`. Any use against a downstream theorem must audit the topology actually consumed by that theorem.
- A compression may retain the prime labels, their heights, or another provenance mark in addition to the phase tuple. AF-324 obstructs phase-only support-uniform separation; it does not say that every marked representation collapses.
- No Riemann zero, critical-line statement, zero-density estimate, or RH implication follows.

## Consequence for the research line

AF-323 said that unrestricted support variation destroys every open phase-space separation at fixed nonzero time. AF-324 now prices the first natural restriction: capping the largest prime by `H` restores only a finite-resolution phase net, with unconditional covering radius between order `log H/H` and `H^{-19/40}` up to constants.

This makes the support/provenance warning operational. A downstream argument that needs a stable rational-prime discriminator across growing supports must state the scale at which support height enters its modulus; simply declaring the support finite does not restore a support-independent gap. For the current eight-point frontier, near-singular prime configurations are guaranteed at a polynomial rate in support height, so the remaining exact question stays sharply separated from numerical near-incidence: **does the rational-prime orbit ever hit `s_1=e_4=0` exactly?**