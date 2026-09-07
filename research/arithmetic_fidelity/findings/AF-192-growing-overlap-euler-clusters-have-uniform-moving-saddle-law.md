# AF-192 — Growing-overlap Euler clusters have a uniform moving-saddle law

**Status:** `EXACT-DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-191 proves a sharp Euler-band discrepancy law when the parity-cluster order is linear in the reciprocal-band index, `m/q` staying in a fixed compact subset of `(0,infinity)`. Its proof leaves two apparently different growing-overlap boundaries open: `m/q -> 0`, where the saddle moves toward the low-harmonic endpoint, and `m/q -> infinity` with `m/q^2 -> 0`, where it moves toward the band edge.

Both boundaries are governed by the same saddle law. The correct uniform condition is not that `m/q` stay fixed, but that the dominant saddle remain many lattice spacings and many Gaussian widths away from both endpoints. For the Euler logarithm this is exactly ensured by

\[
m\to\infty,
\qquad
\frac{m}{q^2}\to0.
\]

Fix

\[
x>0,
\qquad
\sigma>0,
\qquad
a=\sigma x>0,
\qquad
r=e^{-a}.
\tag{1}
\]

Let `delta -> 0`, and let positive integers `q=q_delta`, `m=m_delta` satisfy

\[
q\to\infty,
\qquad
m\to\infty,
\qquad
\frac{m}{q^2}\to0,
\qquad
mq\delta\to0.
\tag{2}
\]

Use the normalized parity-split controls

\[
\nu_\delta
=
2^{1-m}
\sum_{j=0}^{m}
(-1)^{m-j}
\binom mj
\delta_{x+j\delta},
\tag{3}
\]

the Euler local logarithm

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+it,
\tag{4}
\]

and the reciprocal band

\[
T_\delta=\frac{\pi}{q\delta},
\qquad
D_\delta
=
\sup_{|t|\le T_\delta}
\left|
\int F_{\sigma+it}(u)\,d\nu_\delta(u)
\right|.
\tag{5}
\]

Put

\[
\kappa=\frac mq,
\tag{6}
\]

and retain the AF-191 functions

\[
f_{a,\kappa}(\alpha)
=-a\alpha
+\kappa\log\sin\frac{\pi\alpha}{2},
\qquad 0<\alpha\le1,
\tag{7}
\]

\[
\alpha_*(a,\kappa)
=
\frac2\pi
\arctan\frac{\pi\kappa}{2a},
\tag{8}
\]

\[
\Psi(a,\kappa)
=
-\frac{2a}{\pi}
\arctan\frac{\pi\kappa}{2a}
+
\kappa\log
\frac{\pi\kappa}
{\sqrt{4a^2+\pi^2\kappa^2}},
\tag{9}
\]

\[
H(a,\kappa)
=
\frac{a^2}{\kappa}
+
\frac{\pi^2\kappa}{4},
\tag{10}
\]

and

\[
C(a,\kappa)
=
\frac{2}{\alpha_*(a,\kappa)}
\sqrt{\frac{2\pi}{H(a,\kappa)}}.
\tag{11}
\]

Then throughout the full regime `(2)`, with no lower or upper compactness assumption on `m/q`,

\[
\boxed{
D_\delta
=
\bigl(1+o(1)\bigr)
C(a,\kappa)
q^{-1/2}
\exp\!\left[q\Psi(a,\kappa)\right].
}
\tag{12}
\]

The dominant harmonic still satisfies

\[
k_*=q\alpha_*(a,\kappa)+O\!\left(\sqrt{q/H(a,\kappa)}\right),
\tag{13}
\]

but `(12)` is now uniform along sequences for which `\kappa -> 0`, `\kappa -> \kappa_0 in (0,infinity)`, or `\kappa -> infinity` subject to `\kappa=o(q)`.

Thus the two open AF-191 boundaries are not new fidelity phases. They are endpoint motions of one triangular-array saddle. The genuine changes of mechanism occur when the saddle width ceases to contain asymptotically many harmonics (`m` bounded), or when the band-edge distance is no longer asymptotically large in saddle-width units (`m/q^2` order one), the latter being the theta-profile regime of AF-190.

## Exact Euler response and reduction to one positive edge sum

As in AF-187--AF-191, write `theta=t delta`. The exact response is

\[
R_\delta(t)
=
2^{1-m}
\sum_{k\ge1}
\frac{r^k e^{-iktx}}{k}
\left(e^{-k(\sigma+it)\delta}-1\right)^m.
\tag{14}
\]

For `1<=k<q` and `|theta|<=pi/q`, define

\[
b_{k,\delta}(\theta)
=
\frac{|1-e^{-k\sigma\delta}e^{-ik\theta}|}{2}.
\tag{15}
\]

The AF-191 estimate remains uniform over the whole sub-band range:

\[
b_{k,\delta}(\theta)
\le
\left(1+\frac{\sigma q\delta}{2}\right)
\sin\frac{\pi k}{2q}.
\tag{16}
\]

Because `mq delta -> 0`, raising the prefactor in `(16)` to the `m`-th power changes it by `1+o(1)`. Hence the full sub-band response is bounded by `1+o(1)` times

\[
S_{q,m}
=
2\sum_{k=1}^{q-1}
\frac{e^{-ak}}{k}
\sin^m\frac{\pi k}{2q}.
\tag{17}
\]

For `k>=q`, simply `b_{k,delta}<=1`, so

\[
2\sum_{k\ge q}\frac{r^k}{k}b_{k,\delta}(\theta)^m
\le
\frac{2e^{-aq}}{q(1-e^{-a})}.
\tag{18}
\]

It therefore suffices to derive a moving-saddle asymptotic for `(17)`, prove that `(18)` is negligible on that scale, and then show that one frequency in the continuous band asymptotically aligns the phases of all relevant sub-band harmonics.

## The moving saddle remains interior in its own scale

Write

\[
\phi_{q,m}(k)
=-ak
+m\log\sin\frac{\pi k}{2q}
=
q f_{a,\kappa}(k/q).
\tag{19}
\]

The continuous maximizer is

\[
k_0=q\alpha_*(a,\kappa),
\tag{20}
\]

and its inverse curvature scale in the integer variable is

\[
s^2
=
\frac{q}{H(a,\kappa)}.
\tag{21}
\]

Introduce

\[
z=\frac{\pi\kappa}{2a}.
\tag{22}
\]

Then `(10)` gives the exact identity

\[
s^2
=
\frac{m}{a^2(1+z^2)}.
\tag{23}
\]

The standardized distance from the saddle to the lower endpoint is

\[
\frac{k_0}{s}
=
\sqrt m\,
\frac{\sqrt{1+z^2}}{z}\arctan z.
\tag{24}
\]

The factor multiplying `sqrt(m)` stays bounded below by a positive constant for all `z>0`, so `(2)` implies

\[
\frac{k_0}{s}\to\infty.
\tag{25}
\]

Likewise

\[
\frac{q-k_0}{s}
=
\sqrt m\,
\frac{\pi\sqrt{1+z^2}}{2z}
\left(1-\frac2\pi\arctan z\right).
\tag{26}
\]

For bounded `z` this diverges because `m->infinity`. As `z->infinity`, the factor after `sqrt(m)` is asymptotic to `1/z`, so `(26)` is asymptotic to

\[
\frac{2a}{\pi}\frac{q}{\sqrt m},
\tag{27}
\]

which tends to infinity exactly because `m/q^2 -> 0`. Thus

\[
\boxed{
\frac{k_0}{s}\to\infty,
\qquad
\frac{q-k_0}{s}\to\infty.
}
\tag{28}
\]

This is the geometric reason compactness of `m/q` was unnecessary: even when the normalized saddle `alpha_*` approaches `0` or `1`, it remains asymptotically interior after rescaling by its own Gaussian width.

The lattice also becomes fine on that scale. From `(21)`,

\[
\frac1{s^2}
=
\frac{H}{q}
=
\frac{a^2}{m}
+
\frac{\pi^2m}{4q^2}
\longrightarrow0,
\tag{29}
\]

so `s->infinity`.

## Uniform discrete Laplace asymptotic

The derivatives at the saddle are explicit:

\[
f''(\alpha_*)=-H,
\tag{30}
\]

\[
f'''(\alpha_*)
=
\frac{a(4a^2+\pi^2\kappa^2)}{2\kappa^2}
=
\frac{2aH}{\kappa},
\tag{31}
\]

and

\[
f^{(4)}(\alpha_*)
=-
\frac{(4a^2+\pi^2\kappa^2)(12a^2+\pi^2\kappa^2)}{8\kappa^3}.
\tag{32}
\]

On the standardized scale `k=k_0+s y`, the cubic Taylor coefficient is bounded in magnitude by a constant times

\[
\frac{|f'''(\alpha_*)|}{\sqrt q\,H^{3/2}},
\tag{33}
\]

which is `O(m^{-1/2})` when `kappa` is small and `O((q kappa^3)^{-1/2})` when it is large. Both tend to zero under `(2)`. The standardized quartic coefficient is similarly `O(1/m)` at either endpoint regime. On every fixed `|y|<=L`, therefore,

\[
\phi_{q,m}(k_0+s y)-\phi_{q,m}(k_0)
=
-\frac{y^2}{2}+o(1)
\tag{34}
\]

uniformly along every sequence satisfying `(2)`.

Moreover `f` is strictly concave on `(0,1)`. Equations `(28)`--`(29)` put both endpoints outside every fixed standardized window, and concavity supplies a Gaussian/exponential majorant away from the central window. Letting first `q,m` tend along `(2)` and then `L->infinity` gives the triangular-array discrete Laplace law

\[
\sum_{k=1}^{q-1}e^{\phi_{q,m}(k)}
=
\bigl(1+o(1)\bigr)
\sqrt{\frac{2\pi q}{H}}
\,e^{q\Psi(a,\kappa)}.
\tag{35}
\]

The amplitude `2/k` is also constant to relative `o(1)` across the saddle window because

\[
\frac{s}{k_0}	o0
\tag{36}
\]

by `(25)`. Consequently

\[
\boxed{
S_{q,m}
=
\bigl(1+o(1)\bigr)
C(a,\kappa)q^{-1/2}e^{q\Psi(a,\kappa)}.
}
\tag{37}
\]

The asymptotic method itself is classical discrete Laplace/saddle-point analysis. The new point relative to AF-191 is the verified moving-saddle uniformity at both degenerating values of `kappa`.

## The above-band tail is uniformly negligible

For every fixed `kappa>0`, strict interior maximality gives `Psi(a,kappa)>-a`. What is needed here is that the advantage over the endpoint still diverge when `kappa` itself varies.

If `kappa` remains bounded, continuity together with the small-`kappa` limit `Psi(a,kappa)->0` gives

\[
q\bigl(\Psi(a,\kappa)+a\bigr)\to\infty.
\tag{38}
\]

If `kappa->infinity`, the AF-191 expansion gives

\[
\Psi(a,\kappa)+a
=
\frac{2a^2}{\pi^2\kappa}
+O(\kappa^{-3}),
\tag{39}
\]

hence

\[
q\bigl(\Psi(a,\kappa)+a\bigr)
\sim
\frac{2a^2q^2}{\pi^2m}
\to\infty
\tag{40}
\]

by `(2)`. Thus the tail `(18)` is `o(S_{q,m})` in every allowed regime.

## Continuous-band phase alignment is uniform over the moving saddle

The zero-damping identity

\[
e^{-ik\theta}-1
=-2i e^{-ik\theta/2}\sin\frac{k\theta}{2}
\tag{41}
\]

shows that, apart from the common factor `(-i)^m`, the `k`-th harmonic phase is

\[
\exp\!\left[
-ik\theta
\left(\frac{x}{\delta}+\frac m2\right)
\right].
\tag{42}
\]

Set

\[
A_\delta=\frac{x}{\delta}+\frac m2
\tag{43}
\]

and choose the largest mesh point

\[
\theta_*
=
\frac{2\pi\ell_\delta}{A_\delta}
\le
\frac{\pi}{q}.
\tag{44}
\]

Since `m delta -> 0`,

\[
0\le\frac\pi q-\theta_*=O(\delta).
\tag{45}
\]

Every zero-damping phase in `(42)` is then exactly equal. More importantly, the magnitude comparison is uniform for the entire range `1<=k<q`. Concavity of sine on `[0,pi/2]` gives

\[
\frac{\sin(k\theta_*/2)}
{\sin(\pi k/(2q))}
\ge
\frac{q\theta_*}{\pi}
=
1-O(q\delta).
\tag{46}
\]

Thus taking the `m`-th power changes every sub-band edge magnitude by `1+o(1)` because `mq delta ->0`.

Restoring `e^{-k sigma delta}` changes each factor relative to `1-e^{-ik\theta_*}` by at most `O(q delta)` uniformly for `1<=k<q`; after the `m`-th power both its magnitude and phase perturbations are `o(1)`. Therefore all sub-band terms add at `theta_*` with a common phase up to a uniform `o(1)` error and with total magnitude

\[
|R_\delta(\theta_*/\delta)|
=
\bigl(1+o(1)\bigr)S_{q,m}
+o(S_{q,m}).
\tag{47}
\]

The frequency lies in the declared band, so `(37)` and `(47)` give the lower bound matching the upper bound from `(16)`--`(18)`. This proves `(12)`.

## Endpoint regimes and matching with the neighboring laws

The exact formula `(12)` should normally be used with the current value `kappa=m/q`; endpoint expansions can be misleading if their remainder is multiplied by the large parameter `q`.

When `m/q -> 0` while `m->infinity`,

\[
\alpha_*
=\frac{\kappa}{a}+O(\kappa^3),
\qquad
\Psi
=
\kappa\left(\log\frac{\pi\kappa}{2a}-1\right)
+O(\kappa^3).
\tag{48}
\]

Hence the dominant harmonic is of order `m/a`, far below the nominal band edge. If additionally

\[
\frac{m^3}{q^2}\to0,
\tag{49}
\]

then the accumulated exponent error in `(48)` is `o(1)` and `(12)` simplifies to

\[
D_\delta
\sim
2\sqrt{\frac{2\pi}{m}}
\left(\frac{\pi m}{2aeq}\right)^m.
\tag{50}
\]

When `m/q -> infinity` but `m/q^2 ->0`,

\[
\alpha_*
=1-\frac{4a}{\pi^2\kappa}+O(\kappa^{-3}),
\qquad
\Psi
=-a+\frac{2a^2}{\pi^2\kappa}+O(\kappa^{-3}).
\tag{51}
\]

The dominant harmonic approaches the band edge but its distance from that edge is still many saddle widths by `(27)`. If additionally

\[
\frac{q^4}{m^3}\to0,
\tag{52}
\]

then the accumulated exponent error is again `o(1)` and

\[
D_\delta
\sim
4\sqrt{\frac{2}{\pi m}}
\exp\!\left[
-aq+
\frac{2a^2q^2}{\pi^2m}
\right].
\tag{53}
\]

The large-`kappa` formula also matches the small-`tau` saddle of AF-190. Formally setting `tau=m/q^2`, the AF-190 theta profile has its dominant offset near `4a/(pi^2 tau)` and Gaussian width of order `tau^{-1/2}`; discrete Laplace evaluation of that theta sum gives the same exponential correction and prefactor as `(53)`. Thus AF-190 and AF-192 meet at the boundary `tau->0`, while AF-190 is required once `tau` stays order one because the distance to the band edge is then only order one in the local resonance scale.

## Falsification and boundaries

The theorem is deliberately tied to the declared source, kernel, and observation model.

- The source is the positive parity-split finite-difference family. Other clustered controls can have different cancellation geometry.
- The destination is the Euler local logarithm with coefficient ladder `e^{-ak}/k`; the saddle equation is kernel-specific.
- The observation set is a continuous vertical band. A sparse grid can miss the `O(delta)` phase-alignment mesh and needs a separate aliasing analysis.
- The assumption `m->infinity` is essential to this Gaussian lattice law. If `m` stays bounded while `m/q->0`, the saddle contains only order-one many harmonics and a different fixed-order limit is required.
- The assumption `m/q^2->0` is the interior-in-saddle-width gate. At `m/q^2 -> tau in (0,infinity)`, AF-190's discrete theta profile replaces the continuum Gaussian saddle; at `m/q^2->infinity`, AF-189's isolated first-reachable resonance takes over.
- The assumption `mq delta->0` keeps real damping and the phase-alignment displacement negligible after the `m`-th power. A nonzero damping scale changes the profile.
- `(12)` is a sharp forward discrepancy law for one generalized Euler-product control family. It is not a stable inverse theorem for arbitrary source systems and does not distinguish rational primes from Beurling/generalized-prime systems.

The reusable fidelity conclusion is exact: **the correct compression audit is controlled by source complexity measured in the destination kernel's intrinsic resolution units, not by bandwidth alone**. Here the same nominal reciprocal band supports three different internal mechanisms—moving continuum saddle, finite theta overlap, and isolated resonance—depending on how `m` compares with `q^2`.

## Prior art and novelty assessment

Richard B. Paris, **“The discrete analogue of Laplace's method,”** *Computers & Mathematics with Applications* 61(10) (2011), 3024--3034, DOI `10.1016/j.camwa.2011.03.092`, gives a rigorous classical framework for asymptotic estimation of positive sums by their maximal term and local quadratic profile. The moving-saddle argument above uses that classical mechanism but verifies separately the triangular-array endpoint and lattice-width conditions needed when `m/q` is not compact.

Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, proves sharp Fourier conditioning bounds whose exponent depends on cluster size. David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, is foundational prior art for the interaction between bandwidth, source separation/complexity, and stable recovery.

A targeted search over discrete Laplace methods with moving maxima, weighted sine-power sums, clustered Fourier recovery, and source-complexity/bandwidth asymptotics did not identify an authoritative source stating `(12)` for the Euler logarithm and the AF parity controls. That search is not evidence of priority, and no novelty claim is made. The durable contribution is the exact closure of both endpoint regimes explicitly left open by AF-191 and the resulting phase diagram boundary with AF-189 and AF-190.

## Dependencies and evidence boundary

The exact harmonic formula and parity controls are inherited from AF-182 and AF-187--AF-191. AF-191 supplies the fixed-`kappa` saddle functions `(7)`--`(11)`; AF-192's new mathematical step is proving their uniform validity when `kappa` tends to either endpoint under the single growing-overlap condition `m->infinity`, `m/q^2->0`, and then making the phase-alignment estimate uniform over the full sub-band.

No numerical experiment is used as evidence. The endpoint asymptotics `(50)` and `(53)` include the additional scale assumptions needed to turn the local expansions of `Psi` into relative asymptotics after multiplication by `q`; without those assumptions the exact formula `(12)` remains the asserted result. No RH consequence, rational-prime uniqueness statement, or general inverse theorem follows.