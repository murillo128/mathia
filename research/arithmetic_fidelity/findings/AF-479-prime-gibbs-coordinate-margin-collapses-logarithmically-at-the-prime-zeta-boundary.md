# AF-479 — Prime Gibbs coordinate margin collapses logarithmically at the prime-zeta boundary

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INPUT`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `BOUNDARY-CONDITIONING`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-478 proves that every anchored prime Gibbs half-line `sigma>=sigma_0>1` has a positive scale-free `ell^1`-to-Hilbert margin under the canonical coordinate embedding. The anchor is genuinely load-bearing: the same embedding has **no uniform lower Lipschitz constant on the full family `sigma>1`**, and its infinitesimal margin has an exact logarithmic collapse rate as the prime-zeta convergence boundary is approached.

Let

\[
P(\sigma)=\sum_p p^{-\sigma},
\qquad
\mu_\sigma(p)=\frac{p^{-\sigma}}{P(\sigma)},
\qquad \sigma>1,
\tag{1}
\]

and use the AF-478 coordinate Hilbert embedding

\[
H(\mu)=\sqrt2\,\mu\in\ell^2(\mathbb P).
\tag{2}
\]

Define its local lower-margin ratio along the prime Gibbs curve by

\[
\rho(\sigma)
:=
\frac{\sqrt2\,\|\mu_\sigma'\|_2}
     {\|\mu_\sigma'\|_1}.
\tag{3}
\]

If `epsilon=sigma-1` and

\[
L=\log\frac1\epsilon,
\tag{4}
\]

then, as `epsilon downarrow 0`,

\[
\boxed{
\rho(1+\epsilon)
\sim
\frac{\sqrt{P(2)/2}}{\log(1/\epsilon)}.
}
\tag{5}
\]

Consequently

\[
\inf_{\sigma\ne\tau>1}
\frac{\|H(\mu_\sigma)-H(\mu_\tau)\|_2}
     {\|\mu_\sigma-\mu_\tau\|_1}
=0.
\tag{6}
\]

Thus the AF-478 positive theorem cannot be extended uniformly to the open boundary `sigma>1` for this canonical embedding. At the same time, `(5)` shows that the actual local deterioration is only logarithmic. The finite-positive-support estimate used in AF-478 is therefore a robust sufficient bound, not a sharp description of prime-Gibbs conditioning near the boundary.

The reusable Arithmetic Fidelity distinction is

\[
\boxed{
\text{exact injectivity and half-line scale-free fidelity may coexist with a vanishing boundary conditioning margin.}
}
\tag{7}
\]

This is a concrete example where the surviving discriminator is not lost at any fixed interior parameter, but becomes progressively harder to resolve under a fixed compression geometry as the source approaches a singular normalization boundary.

## Exact derivation

Write

\[
m(\sigma)
:=
\mathbb E_{\mu_\sigma}[\log p]
=
-\frac{P'(\sigma)}{P(\sigma)}.
\tag{8}
\]

Termwise differentiation is valid for every fixed `sigma>1`, and gives the exact score identity

\[
\mu_\sigma'(p)
=
\mu_\sigma(p)\bigl(m(\sigma)-\log p\bigr).
\tag{9}
\]

### Prime-zeta boundary scale

The classical Möbius inversion formula

\[
P(s)=\sum_{k\ge1}\frac{\mu(k)}k\log\zeta(ks)
\tag{10}
\]

shows that, near `s=1` from the right, only the `k=1` term is singular. Hence

\[
P(1+\epsilon)=L+O(1),
\qquad
-P'(1+\epsilon)=\frac1\epsilon+O(1),
\tag{11}
\]

and therefore

\[
m(1+\epsilon)
\sim
\frac1{\epsilon L}.
\tag{12}
\]

In particular `m->infinity` but

\[
\epsilon m\sim\frac1L\to0.
\tag{13}
\]

### The `ell^1` speed is asymptotic to `2m`

Let `X=log p` under `mu_sigma`. Because `E(X-m)=0`, the positive and negative Jordan masses of the centered score agree:

\[
\mathbb E|X-m|
=
2\,\mathbb E[(m-X)_+].
\tag{14}
\]

The low-energy probability is

\[
\mu_\sigma(X<m)
=
\frac1{P(\sigma)}
\sum_{p<e^m}p^{-1-\epsilon}.
\tag{15}
\]

For `p<e^m`, `(13)` gives

\[
e^{-\epsilon m}\le p^{-\epsilon}\le1,
\qquad e^{-\epsilon m}=1-o(1).
\tag{16}
\]

Mertens' prime reciprocal theorem gives

\[
\sum_{p<e^m}\frac1p
=
\log m+B_1+o(1).
\tag{17}
\]

From `(12)`,

\[
\log m=L-\log L+o(L),
\tag{18}
\]

so `(11)`, `(15)`--`(18)` imply

\[
\mu_\sigma(X<m)\to1.
\tag{19}
\]

For the truncated first moment, the classical weighted Mertens estimate

\[
\sum_{p\le x}\frac{\log p}{p}
=
\log x+O(1)
\tag{20}
\]

gives

\[
\mathbb E[X;X<m]
\le
\frac{m+O(1)}{P(\sigma)}
=
O\!\left(\frac mL\right)
=o(m).
\tag{21}
\]

Therefore

\[
\mathbb E[(m-X)_+]
=
m\,\mu_\sigma(X<m)-\mathbb E[X;X<m]
\sim m,
\tag{22}
\]

and from `(9)` and `(14)`,

\[
\boxed{
\|\mu_\sigma'\|_1
=\mathbb E|X-m|
\sim2m.
}
\tag{23}
\]

### The `ell^2` speed loses one factor of `P(s)`

Using `(9)` directly,

\[
\|\mu_\sigma'\|_2^2
=
\frac1{P(\sigma)^2}
\sum_p p^{-2\sigma}(m-\log p)^2.
\tag{24}
\]

Expanding the square in terms of the prime zeta function gives the exact identity

\[
\|\mu_\sigma'\|_2^2
=
\frac{
P''(2\sigma)+2mP'(2\sigma)+m^2P(2\sigma)
}{P(\sigma)^2}.
\tag{25}
\]

As `sigma downarrow 1`, the quantities `P(2sigma)`, `P'(2sigma)`, and `P''(2sigma)` converge to finite values while `m->infinity`. Thus the quadratic term dominates:

\[
\boxed{
\|\mu_\sigma'\|_2
\sim
\frac{m\sqrt{P(2)}}{P(\sigma)}
\sim
\frac{m\sqrt{P(2)}}L.
}
\tag{26}
\]

Combining `(23)` and `(26)` proves `(5)`.

For every fixed `sigma>1`, the map `sigma mapsto mu_sigma` is differentiable in both `ell^1` and `ell^2` on a small neighborhood of `sigma`. Therefore

\[
\lim_{\tau\to\sigma}
\frac{\|H(\mu_\tau)-H(\mu_\sigma)\|_2}
     {\|\mu_\tau-\mu_\sigma\|_1}
=
\rho(\sigma).
\tag{27}
\]

Sending `sigma downarrow 1` in `(27)` proves `(6)`.

## Relation to AF-478 and the source-complexity frontier

AF-478 gives, on every fixed half-line `sigma>=sigma_0>1`, a global lower bound based on the number of prime coordinates below

\[
m(\sigma_0)=-P'(\sigma_0)/P(\sigma_0).
\tag{28}
\]

AF-479 shows two things that the support-count argument alone does not reveal.

First, no lower constant can remain bounded away from zero as `sigma_0 downarrow 1`: taking a local pair at the left endpoint already forces the best possible half-line constant to satisfy

\[
c(\sigma_0)
:=
\inf_{\sigma\ne\tau\ge\sigma_0}
\frac{\|H(\mu_\sigma)-H(\mu_\tau)\|_2}
     {\|\mu_\sigma-\mu_\tau\|_1}
\le
\rho(\sigma_0)
\sim
\frac{\sqrt{P(2)/2}}
     {\log(1/(\sigma_0-1))}.
\tag{29}
\]

Second, the mechanism of this collapse is **not** an explosion of independently switchable tail coordinates of the AF-473/AF-476 kind. Pairwise prime-Gibbs secants remain single-crossing. The deterioration instead comes from how the centered score spreads across the normalized prime tail: its `ell^1` speed is order `m`, while its `ell^2` speed is smaller by the diverging factor `P(s)~L`.

So raw Jordan-support cardinality is too coarse to measure conditioning near this boundary. The next useful source-complexity invariant should distinguish at least:

- combinatorial sign/support breadth, which AF-478 controls uniformly on anchored half-lines; and
- **effective norm breadth**, which can diverge even when the sign pattern remains rigid.

Equation `(5)` supplies a concrete prime-derived calibration for that second notion.

## Prior art and novelty audit

All analytic-number-theory inputs are classical.

- C.-E. Fröberg, **“On the Prime Zeta Function,”** *BIT* 8, 187--202 (1968), DOI `10.1007/BF01933420`, is the standard classical reference for the prime zeta function and its relation to the Riemann zeta function.
- Mertens' classical prime-sum theorems give `(17)` and `(20)`; modern standard treatments include Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*.
- The score identity `(9)` is the standard derivative formula for a one-parameter exponential family.

A targeted prior-art search found the prime-zeta boundary asymptotics, Mertens estimates, and exponential-family score mechanism as standard ingredients. It did not justify a novelty claim for the assembled ratio `(5)`. This finding therefore makes **no literature novelty claim**: its durable contribution is the Arithmetic Fidelity consequence that the canonical prime-Gibbs Hilbert margin has a quantified boundary collapse, sharpening the load-bearing-anchor warning in AF-478.

## Boundaries and falsification audit

- **This is a conditioning result, not a loss of injectivity.** For every fixed `sigma>1`, the prime Gibbs law remains exactly defined and the coordinate map is injective on the curve. What vanishes is a uniform inverse-Lipschitz margin over the full open half-line.
- **The result is embedding-specific.** Equation `(6)` rules out a global positive lower constant for the canonical linear coordinate Hilbert embedding `H(mu)=sqrt(2)mu`. It does not prove that every nonlinear Hilbert representation of the prime Gibbs curve must have the same boundary collapse.
- **It does not contradict AF-478.** Every anchored family `sigma>=sigma_0>1` still has the positive AF-478 constant. AF-479 shows that those constants cannot be uniform as the anchor approaches `1`.
- **The logarithmic rate in `(5)` is local.** Equation `(29)` is an upper bound on the best global half-line lower constant, not a matching asymptotic formula for that global constant.
- **The arithmetic input is not prime-selective.** Analogous Gibbs/Dirichlet families can exhibit normalization-boundary conditioning loss. This theorem does not distinguish rational primes from matched generalized-prime controls and is not evidence for RH.
- **The Mertens scale is load-bearing.** The exact `1/L` rate uses rational-prime reciprocal and weighted reciprocal asymptotics. A generalized-prime control with different boundary density can have a different conditioning law even if it preserves the single-crossing mechanism.
- **No finite-dimensional shortcut is being used.** The calculation audits the actual source secant/tangent norm geometry, consistent with AF-461 and AF-478's warning that parametric dimension alone does not determine fidelity.

## Research consequence

AF-478 showed that realizable secant sign complexity can defeat the generic soft-tail Hamming obstruction. AF-479 now separates that combinatorial success from metric robustness: **single crossing is enough for positive scale-free fidelity on every anchored half-line, but not enough for a boundary-uniform margin.**

For arithmetic source classes approaching a singular normalization or continuation boundary, a useful next gate is therefore to measure both the sign structure and the norm distribution of the admissible secants. In the prime Gibbs case the exact diagnostic is the local ratio `(3)`, and the prime-zeta/Mertens asymptotics force its logarithmic decay `(5)`.