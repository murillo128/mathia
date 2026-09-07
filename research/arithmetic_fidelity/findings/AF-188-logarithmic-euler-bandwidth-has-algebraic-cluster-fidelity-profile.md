# AF-188 — Logarithmic Euler bandwidth has an algebraic parity-cluster fidelity profile

**Status:** `EXACT-DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-184 proves that adaptive positive parity clusters can be super-algebraically invisible to bounded-band Euler-log observations when

\[
\delta T(\delta)\log(1/\delta)\to0,
\tag{1}
\]

while AF-187 proves that the same mechanism becomes order-one visible once `\delta T(\delta)` stays bounded below by a positive constant. The intermediate logarithmic Rayleigh scale can be calibrated more sharply for the same controls.

Fix

\[
x>0,
\qquad
\sigma>0,
\qquad
r=e^{-\sigma x}\in(0,1).
\tag{2}
\]

Let `\delta\downarrow0`, and let `q=q_\delta` and `m=m_\delta` be positive integers satisfying

\[
\boxed{
q_\delta\to\infty,
\qquad
\frac{m_\delta}{q_\delta^2}\to\infty,
\qquad
m_\delta q_\delta\delta\to0.
}
\tag{3}
\]

Use the normalized parity-split controls of AF-182,

\[
\nu_\delta
:=
\mu_{+,\delta}-\mu_{-,\delta}
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta}.
\tag{4}
\]

They are differences of positive probability measures and satisfy

\[
\boxed{
W_1(\mu_{+,\delta},\mu_{-,\delta})=\delta,
}
\tag{5}
\]

while their full support diameter tends to zero because `(3)` implies `m_\delta\delta\to0`.

For

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+it,
\tag{6}
\]

define the bandwidth

\[
\boxed{
T_\delta=\frac{\pi}{q_\delta\delta}
}
\tag{7}
\]

and discrepancy

\[
D_\delta
=
\sup_{|t|\le T_\delta}
\left|
\int F_{\sigma+it}(u)\,d\nu_\delta(u)
\right|.
\tag{8}
\]

Then

\[
\boxed{
(2+o(1))\frac{r^{q_\delta}}{q_\delta}
\le
D_\delta
\le
\left(\frac{2}{1-r}+o(1)\right)
\frac{r^{q_\delta}}{q_\delta}.
}
\tag{9}
\]

In particular,

\[
\boxed{
\log D_\delta
=-\sigma x\,q_\delta-\log q_\delta+O(1).
}
\tag{10}
\]

The lower bound is not obtained by the base-point phase alignment used in AF-187. It is witnessed directly at the band edge `t=T_\delta`, where the `q_\delta`-th Euler harmonic is exactly resonant with the parity finite-difference filter. The condition `m_\delta/q_\delta^2\to\infty` makes that resonance narrow enough to suppress every lower harmonic despite its larger Euler coefficient, while `m_\delta q_\delta\delta\to0` prevents the real damping from attenuating the resonant term.

The two growth requirements in `(3)` are jointly feasible exactly when

\[
\boxed{q_\delta^3\delta\to0.}
\tag{11}
\]

Thus the logarithmic choice

\[
L_\delta=\log(1/\delta),
\qquad
q_\delta=\lfloor cL_\delta\rfloor,
\qquad c>0,
\tag{12}
\]

is admissible. For example `m_\delta=\lceil q_\delta^2L_\delta\rceil` satisfies `(3)`. Then

\[
T_\delta
\sim
\frac{\pi}{c\,\delta L_\delta}
\tag{13}
\]

and `(9)` becomes the algebraic profile

\[
\boxed{
D_\delta
=\Theta\!\left(
\frac{\delta^{c\sigma x}}{\log(1/\delta)}
\right).
}
\tag{14}
\]

Equivalently, if the critical scaled bandwidth tends to a fixed value

\[
\delta T_\delta\log(1/\delta)\to\lambda\in(0,\infty),
\tag{15}
\]

then choosing `c=\pi/\lambda` gives

\[
\boxed{
\frac{\log D_\delta}{\log\delta}
\longrightarrow
\frac{\pi\sigma x}{\lambda}.
}
\tag{16}
\]

So the logarithmic window is not merely an unresolved binary transition between invisible and visible. For this matched-control family it carries a continuum of algebraic fidelity exponents.

A direct consequence for inverse regularity is also exact at the exponent level. Put

\[
\beta=\frac{\pi\sigma x}{\lambda}.
\tag{17}
\]

Since the source distance is exactly `\delta` while `D_\delta=\Theta(\delta^\beta/L_\delta)`, no uniform inverse-Hölder estimate

\[
W_1(\mu,\nu)
\le C D(\mu,\nu)^\alpha
\tag{18}
\]

can hold on any source class containing these controls when

\[
\boxed{
\alpha\ge\frac1\beta
=\frac{\lambda}{\pi\sigma x}.
}
\tag{19}
\]

At equality the extra factor `L_\delta^{-\alpha}` still makes the right-hand side `o(\delta)`. For smaller `\alpha`, this particular pair does not obstruct such an estimate; no recovery theorem is claimed.

## Exact harmonic response

The Euler local logarithm has the absolutely convergent harmonic expansion

\[
F_s(u)
=
\sum_{k\ge1}\frac{e^{-ksu}}{k},
\qquad \Re(s)>0.
\tag{20}
\]

As in AF-182 and AF-187, the parity finite difference gives

\[
R_\delta(t)
:=
\int F_{\sigma+it}(u)\,d\nu_\delta(u)
=
2^{1-m}
\sum_{k\ge1}
\frac{r^k e^{-iktx}}{k}
\left(e^{-k(\sigma+it)\delta}-1\right)^m,
\tag{21}
\]

where `m=m_\delta`. Write

\[
\theta=t\delta,
\qquad
b_{k,\delta}(\theta)
=
\frac{|1-e^{-k\sigma\delta}e^{-ik\theta}|}{2}.
\tag{22}
\]

Then

\[
|R_\delta(t)|
\le
2\sum_{k\ge1}
\frac{r^k}{k}
 b_{k,\delta}(\theta)^m,
\tag{23}
\]

with `b_{k,\delta}(\theta)\le1` for all `k` and `\theta`.

The exact identity

\[
b_{k,\delta}(\theta)^2
=
e^{-k\sigma\delta}
\sin^2\!\frac{k\theta}{2}
+
\frac{(1-e^{-k\sigma\delta})^2}{4}
\tag{24}
\]

is the quantitative bridge between the parity cancellation order and harmonic resolution.

## Uniform suppression of every harmonic below `q`

Inside the whole declared band,

\[
|\theta|\le\frac\pi q.
\tag{25}
\]

For `k=q-j`, `1\le j\le q-1`, equation `(25)` gives

\[
\sin^2\!\frac{k\theta}{2}
\le
\cos^2\!\frac{\pi j}{2q}.
\tag{26}
\]

Using `\sin u\ge2u/\pi` on `[0,\pi/2]`,

\[
\cos^2\!\frac{\pi j}{2q}
\le
1-\frac{j^2}{q^2}.
\tag{27}
\]

Condition `(3)` implies `q^3\delta\to0`, hence in particular `q^2\delta\to0`. Therefore, uniformly for `j\ge1`, the damping remainder in `(24)` is eventually at most half the deficit in `(27)`, and

\[
b_{q-j,\delta}(\theta)^2
\le
1-\frac{j^2}{2q^2}.
\tag{28}
\]

Consequently

\[
\boxed{
b_{q-j,\delta}(\theta)^m
\le
\exp\!\left(-\frac{m j^2}{4q^2}\right).}
\tag{29}
\]

Put `a=\sigma x` and `\eta_\delta=m/q^2\to\infty`. Relative to the scale `r^q/q`, the complete contribution of `k<q` is bounded by

\[
\sum_{j=1}^{q-1}
\frac{q}{q-j}
 e^{aj}
 e^{-\eta_\delta j^2/4}.
\tag{30}
\]

For `j\le q/2`, the prefactor `q/(q-j)` is at most `2`, and the Gaussian exponent in `(30)` dominates the fixed linear exponent `aj` because `\eta_\delta\to\infty`. For `j>q/2`, the whole sum is bounded by

\[
q^2\exp\!\left(aq-\frac{m}{16}\right)
\longrightarrow0,
\tag{31}
\]

because `m/q^2\to\infty`. Hence, uniformly over the full band,

\[
\boxed{
2\sum_{k<q}
\frac{r^k}{k}b_{k,\delta}(\theta)^m
=o\!\left(\frac{r^q}{q}\right).
}
\tag{32}
\]

This is the key distinction from a fixed-order analysis: a growing parity order builds a harmonic filter narrow enough that no lower Euler harmonic can leak into a band whose edge first reaches the `q`-th reciprocal resonance.

## Band upper bound

For `k\ge q`, use only `b_{k,\delta}(\theta)\le1`. Then

\[
2\sum_{k\ge q}\frac{r^k}{k}b_{k,\delta}(\theta)^m
\le
2\sum_{k\ge q}\frac{r^k}{k}
\le
\frac{2r^q}{q(1-r)}.
\tag{33}
\]

Combining `(32)` and `(33)` gives, uniformly for `|t|\le T_\delta`,

\[
D_\delta
\le
\left(\frac{2}{1-r}+o(1)\right)
\frac{r^q}{q},
\tag{34}
\]

which is the upper half of `(9)`.

The constant `2/(1-r)` is not asserted to be sharp. The theorem needs only a uniform upper bound at the same exponential scale as the edge witness below; that is enough to determine the logarithmic fidelity exponent exactly.

## Exact edge resonance and the lower bound

At the positive band edge,

\[
t=T_\delta,
\qquad
\theta=\frac\pi q.
\tag{35}
\]

the `k=q` factor is exactly antipodal:

\[
e^{-q(\sigma+iT_\delta)\delta}
=-e^{-q\sigma\delta}.
\tag{36}
\]

Its contribution to `(21)` is therefore

\[
2(-1)^m
\frac{r^q e^{-iqT_\delta x}}{q}
\left(\frac{1+e^{-q\sigma\delta}}2\right)^m.
\tag{37}
\]

Since

\[
1-\frac{1+e^{-q\sigma\delta}}2
\le
\frac{q\sigma\delta}{2}
\tag{38}
\]

and `mq\delta\to0`,

\[
\left(\frac{1+e^{-q\sigma\delta}}2\right)^m
\longrightarrow1.
\tag{39}
\]

Thus the resonant harmonic alone has magnitude `(2+o(1))r^q/q`.

It remains to show that the other harmonics cannot cancel it at this frequency. The terms `k<q` are already `o(r^q/q)` by `(32)`. For `q<k<2q`, write `k=q+j`. At `\theta=\pi/q`,

\[
\sin^2\!\frac{k\theta}{2}
=
\cos^2\!\frac{\pi j}{2q},
\tag{40}
\]

and the same argument as `(28)`--`(29)` gives

\[
b_{q+j,\delta}(\pi/q)^m
\le
\exp\!\left(-c\frac{m j^2}{q^2}\right)
\tag{41}
\]

for one fixed `c>0` and all sufficiently small `\delta`. Since the Euler coefficient now also decreases by the factor `r^j`, the sum over `1\le j<q` is `o(r^q/q)`.

Finally,

\[
2\sum_{k\ge2q}\frac{r^k}{k}
=O\!\left(\frac{r^{2q}}q\right)
=o\!\left(\frac{r^q}q\right).
\tag{42}
\]

Therefore

\[
\boxed{
R_\delta(T_\delta)
=
2(-1)^m
\frac{r^q e^{-iqT_\delta x}}q
\bigl(1+o(1)\bigr),
}
\tag{43}
\]

and hence

\[
D_\delta
\ge
|R_\delta(T_\delta)|
=(2+o(1))\frac{r^q}{q}.
\tag{44}
\]

Together with `(34)`, this proves `(9)` and `(10)`.

## Feasibility of the isolating order

Conditions `(3)` expose a real source-complexity cost. Writing

\[
h_\delta=\frac{m_\delta}{q_\delta^2},
\tag{45}
\]

they are

\[
h_\delta\to\infty,
\qquad
h_\delta q_\delta^3\delta\to0.
\tag{46}
\]

Thus they imply `(11)`. Conversely, if `q_\delta^3\delta\to0`, choose for example

\[
h_\delta=(q_\delta^3\delta)^{-1/2}
\tag{47}
\]

and take `m_\delta` to be an integer asymptotic to `q_\delta^2h_\delta`. Then `h_\delta\to\infty` while `h_\delta q_\delta^3\delta\to0`, proving the converse.

The condition has a transparent interpretation. Resolving neighboring harmonics around index `q` requires filter order much larger than `q^2`; preserving the resonant Euler factor against real damping requires order much smaller than `1/(q\delta)`. Those two demands are compatible exactly when `q^3\delta\to0`.

## Prior art and novelty assessment

Every ingredient used here has strong classical or modern prior art.

- NIST Digital Library of Mathematical Functions, §25.2(iv), especially Eq. 25.2.11, records the Euler product for `\zeta(s)` in `\Re(s)>1`; the local logarithmic expansion `(20)` is the elementary logarithm of one geometric Euler factor.
- David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309–1331, DOI `10.1137/0523074`, is foundational prior art for the reciprocal relation between Fourier bandwidth, source spacing, and stable sparse recovery.
- Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199–220, DOI `10.1137/18M1212197`, prove sharp clustered-Fourier conditioning bounds whose super-resolution exponent is controlled by the maximal cluster size.
- Dmitry Batenkov and Gil Goldman, **“Single-exponential bounds for the smallest singular value of Vandermonde matrices in the sub-Rayleigh regime,”** *Applied and Computational Harmonic Analysis* 55 (2021), 426–439, DOI `10.1016/j.acha.2021.07.003`, explicitly analyze exponential deterioration with growing cluster size.
- Dmitry Batenkov, Gil Goldman, and Yosef Yomdin, **“Super-resolution of near-colliding point sources,”** *Information and Inference: A Journal of the IMA* 10(2) (2021), 515–572, DOI `10.1093/imaiai/iaaa005`, gives neighboring minimax recovery laws in terms of the super-resolution factor and cluster size.
- Ping Liu and Habib Ammari, **“Super-resolution of positive near-colliding point sources,”** *Information and Inference: A Journal of the IMA* 12(4) (2023), 3087–3111, DOI `10.1093/imaiai/iaad048`, shows that positivity does not remove cluster-size-dependent super-resolution ill-conditioning.

The high-order finite-difference Fourier multiplier and the concentration of its `\sin^m` profile are standard Fourier/finite-difference mathematics. A targeted literature audit found strong prior art for the source-separation/bandwidth/cluster-size mechanism, but did not identify an authoritative source whose theorem is the exact variable-residue Euler-log specialization `(9)`--`(16)`. No novelty claim is made from that absence. The durable value of this finding is the explicit arithmetic calibration of the control family already developed in AF-182--AF-187.

## Boundaries and failure modes

1. **This is a matched-control theorem, not a full inverse theorem.** It determines the discrepancy scale of one increasingly complex positive parity-cluster family. Other generalized-prime controls may be harder to distinguish, and the result gives no uniform recovery bound for the whole source class.

2. **The algebraic exponent is exact; the multiplicative constant for the band supremum is not.** The edge response has the sharp leading constant `2`, while the uniform upper bound in `(9)` is intentionally coarse. Both bounds have the same `r^q/q` scale, which is sufficient for `(10)` and `(16)`.

3. **Growing source complexity is essential.** The cluster has `m+1` distinct nodes and unnormalized multiplicity mass `2^{m-1}`. Fixed support size, multiplicity, entropy, or another source-complexity cap can evade this family.

4. **The observation band is continuous.** Unlike AF-187, no base-point phase alignment is needed for the lower bound because the exact edge `t=\pi/(q\delta)` is observed. A discrete frequency grid must be analyzed separately.

5. **The theorem concerns the Euler local-factor repetition mechanism, not rational-prime uniqueness.** The harmonic ladder exists for generalized Euler factors as well. The result quantifies survival of a declared generalized-prime source contrast through Euler-log compression; it does not distinguish the ordinary rational primes from all generalized-prime systems.

6. **The source metric is normalized `W_1`.** Different source metrics or unnormalized multiplicity conventions change the numerical conditioning comparison even though the harmonic response identity remains valid.

7. **The scale `q^3\delta\to0` belongs to this resonance-isolation proof.** It is the exact feasibility condition for simultaneously imposing `m/q^2\to\infty` and `mq\delta\to0`; it is not claimed to be an information-theoretic threshold for every possible control family or reconstruction method.

8. **No RH consequence is asserted.** The theorem is a fidelity audit for a compression used in arithmetic analysis, not evidence for the location of zeta zeros.

## Consequences for Arithmetic Fidelity

AF-184 and AF-187 left a deliberately explicit gap between logarithmically sub-Rayleigh super-algebraic invisibility and fixed-fraction reciprocal-band visibility. AF-188 resolves the critical `T\asymp1/(\delta\log(1/\delta))` behavior for the same parity controls: **their discrepancy is algebraic, with an exponent set continuously by the scaled bandwidth `\lambda=\delta T\log(1/\delta)`.**

This gives a more precise recovery taxonomy than a binary faithful/non-faithful label. At one fixed compression family, the same source contrast passes through three quantitative regimes as observation bandwidth grows: below the logarithmic Rayleigh scale it can be flatter than every source power; at the logarithmic scale it has a finite algebraic fidelity exponent; at a fixed fraction of reciprocal separation AF-187 supplies order-one visibility.

The reusable audit lesson is that a compression should be specified together with **source separation, source complexity, observation bandwidth, and desired inverse regularity**. Exact distinguishability alone misses the transition, while a single condition number misses the way the admissible Hölder exponent changes with scale. The next unresolved question is no longer the behavior of this parity family at the logarithmic boundary; it is whether structurally different positive generalized-prime controls can beat the algebraic profile `(16)`, or whether an independent lower-bound mechanism for the full Euler observation class forces a comparable recovery exponent.