# RE-196 — Fixed jet matching collapses the entire real Euler ray by log powers

**Status:** `EXACT-DERIVED + FULL-REAL-EULER-RAY + LOG-POWER-SUPPRESSION + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + ARBITRARY-RECIPROCAL-VARIATION + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + STABLE-NONRIGIDITY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-182, RE-190, RE-195.

`RE-195` leaves a natural scalar escape route open: its large-variation padding is negligible on every fixed real Euler window, but it does not rule out using an expanding or even complete real temperature family `s>=1` as a stable source discriminator. The existing matched repair has much more structure than arbitrary finite-Laplace data: after exact boundary matching, its absolute Euler mass has only bounded logarithmic transport away from the selector scale.

That is enough to collapse the **entire positive real Euler ray**, not just a fixed window.

Let

\[
d_p\asymp \frac1{\sqrt p\log p}
\]

be the canonical selector debt. Fix an integer `K>=1`. For every sufficiently large selector scale `p` and every prescribed finite `Lambda_p>0`, the `RE-195` ordinary-prime `{0,1,2}` matched control can be chosen so that, in addition to all conclusions of `RE-195`, its exact Euler discrepancy

\[
D_Q(s)=\sum_q (m_Q(q)-1)[-\log(1-q^{-s})]
\]

satisfies

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\ll_K
\frac{d_p}{(\log p)^{K+1}}
+
\frac1{p^2}
\ll_K
\frac{d_p}{(\log p)^{K+1}}.
}
\tag{1}
\]

At the same time,

\[
D_Q^{(j)}(1+)=0\qquad(0\le j\le K),
\tag{2}
\]

`Q` obeys every fixed Korobov--Vinogradov source envelope, the selector-normalized Robin coordinate still has an order-one transient at `8p`, and

\[
\sum_q\frac{|m_Q(q)-1|}{q}\ge\Lambda_p.
\tag{3}
\]

Consequently, for every fixed `A>0`, one may choose a fixed integer `K>A` and obtain an honest bounded-multiplicity matched control with

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
=o\!\left(\frac{d_p}{(\log p)^A}\right)
}
\tag{4}
\]

while the normalized Robin transient remains order one and reciprocal variation remains arbitrarily large.

Thus enlarging a scalar Euler panel from a fixed interval to **all real temperatures `s>=1`** does not restore Robin-scale stable rigidity. Exact identification and stable discrimination separate sharply: the exact continuum remains injective in the sense of `RE-174`, but its inverse has no selector-scale modulus on the present matched-control class.

## 1. A log-transport lemma for a boundary-matched Euler source

Put

\[
H_s(q):=-\log(1-q^{-s}),
\qquad H(q):=H_1(q).
\]

Let `c_q` be any signed prime packet supported on `q>=p`, finite or absolutely `H`-summable, and define

\[
M_0:=\sum_q|c_q|H(q),
\qquad
M_r:=\sum_q|c_q|H(q)\left|\log\frac qp\right|^r.
\tag{5}
\]

For `u>=0`, normalize away the common selector decay:

\[
F(u):=p^u\sum_q c_qH_{1+u}(q).
\tag{6}
\]

The exact Euler series gives

\[
p^uH_{1+u}(q)
=
\sum_{n\ge1}\frac{q^{-n}}n
\exp\!\left[-u\left(n\log q-\log p\right)\right].
\tag{7}
\]

Since `q>=p`, every exponent rate in (7) is nonnegative. Therefore, for each fixed integer `r>=0`,

\[
\left|
\frac{d^r}{du^r}
\bigl[p^uH_{1+u}(q)\bigr]
\right|
\le
\frac1q\left|\log\frac qp\right|^r
+
C_r\frac{(\log q)^r}{q^2}.
\tag{8}
\]

The first term is the genuine centered logarithmic transport. The second is only the prime-power correction.

Suppose now that `F^(j)(0)=0` for `0<=j<=K` and that the right-hand side of (8), summed against `|c_q|` with `r=K+1`, is at most `L_{K+1}`. Taylor's theorem gives

\[
|F(u)|
\le
\frac{L_{K+1}}{(K+1)!}u^{K+1}.
\tag{9}
\]

Since the original discrepancy is `p^{-u}F(u)` and

\[
\sup_{u\ge0}u^{K+1}p^{-u}
=
\left(\frac{K+1}{e\log p}\right)^{K+1},
\tag{10}
\]

we obtain the general bound

\[
\boxed{
\sup_{s\ge1}
\left|\sum_qc_qH_s(q)\right|
\ll_K
\frac{L_{K+1}}{(\log p)^{K+1}}.
}
\tag{11}
\]

The important point is that spectral width has disappeared. Once the boundary jets vanish, the common factor `p^{-(s-1)}` suppresses the Taylor remainder before large real temperatures can amplify it.

## 2. The RE-182 repair has bounded centered logarithmic transport

Separate the `RE-195` source into

\[
Q-P=S_p+G_p,
\tag{12}
\]

where `G_p` is the finite odd-index padding packet beginning at `X=p^2`, and `S_p` is the canonical selector deletion plus the infinite even-index exact repair.

The selector part of `S_p` lies in `[2p,3p]`, has absolute `H`-mass `d_p`, and therefore contributes `O_K(d_p)` to every fixed centered moment `M_r`.

For the repair, recall the quantitative iteration from `RE-182`. At generation `n`, the support is at

\[
x_n\asymp_K R_K^np,
\]

its total absolute `H`-mass is

\[
T_n\ll_K M_n+x_n^{-1},
\]

and

\[
M_n\ll_K \theta_K^nd_p+x_{n-1}^{-1}
\qquad(0<\theta_K<1).
\tag{13}
\]

On that generation,

\[
\left|\log\frac qp\right|\ll_K n+1.
\]

Hence for every fixed `r`,

\[
\sum_{n\ge0}(n+1)^rT_n
\ll_{K,r}
 d_p\sum_{n\ge0}(n+1)^r\theta_K^n
+
\frac1p\sum_{n\ge0}\frac{(n+1)^r}{R_K^n}
\ll_{K,r}d_p.
\tag{14}
\]

The same estimate survives the `RE-195` padding splice because its contribution to every fixed repair target is `o_K(d_p)`. Thus

\[
\boxed{
\sum_{q\in S_p}|c_q|H(q)
\left|\log\frac qp\right|^r
\ll_{K,r}d_p
\qquad(r\ \text{fixed}).
}
\tag{15}
\]

The prime-power term in (8) is smaller. On the selector shell it is `O_K(d_p(\log p)^r/p)`, and on the repair generations the extra factor `q^{-1}` makes the geometric sum still smaller. Consequently the absolute `(K+1)`st derivative of the normalized structured profile

\[
F_S(u):=p^uD_{S_p}(1+u)
\]

obeys

\[
\boxed{
\sup_{u\ge0}|F_S^{(K+1)}(u)|\ll_K d_p.
}
\tag{16}
\]

This is the source-specific input that is absent from a generic finite-Laplace inverse problem: the exact repair can run to infinity, but its signed correction mass moves outward with geometrically summable `H`-weight, so every fixed centered log-transport moment remains selector-scale.

## 3. The arbitrary-variation padding is uniformly small on the whole ray

`RE-195` proved the padding estimate only on each fixed interval `1<=s<=1+U`. The same Abel argument is actually uniform for all real `s>=1`.

Let

\[
A_G(t)=\sum_{\substack{q\in G_p\\q\le t}}c_q\log q,
\qquad |A_G(t)|\le\log t,
\tag{17}
\]

with `G_p` supported on `[X,Y]`, `X=p^2`. For the first harmonic

\[
F_G^{(1)}(s):=\sum_{q\in G_p}c_qq^{-s},
\]

Abel summation with `f_s(t)=t^{-s}/\log t` gives

\[
F_G^{(1)}(s)
=A_G(Y)f_s(Y)-\int_X^YA_G(t)f_s'(t)\,dt.
\tag{18}
\]

For every real `s>=1`,

\[
\log t\,|f_s'(t)|
=t^{-s-1}\left(s+\frac1{\log t}\right),
\]

so

\[
\left|F_G^{(1)}(s)\right|
\le
Y^{-s}
+
\int_X^\infty t^{-s-1}
\left(s+\frac1{\log t}\right)dt
\ll X^{-s}
\le X^{-1}.
\tag{19}
\]

The exact Euler prime-power tail is also uniform:

\[
\sum_{q\in G_p}\sum_{n\ge2}\frac{q^{-ns}}n
\ll
\sum_{m\ge X}m^{-2}
\ll X^{-1}.
\tag{20}
\]

Therefore

\[
\boxed{
\sup_{s\ge1}|D_{G_p}(s)|\ll X^{-1}=p^{-2},
}
\tag{21}
\]

with a constant independent of `Lambda_p`, the terminal point `Y`, and the spectral span. Arbitrarily large reciprocal variation can therefore be placed in a direction that is uniformly invisible on the **complete positive real Euler axis**.

For later use, `RE-195` also gives, for every fixed `j`,

\[
|D_{G_p}^{(j)}(1+)|
\ll_j\frac{(\log p)^j}{p^2}.
\tag{22}
\]

## 4. Exact finite jets convert into full-ray log-power suppression

The complete source `Q` matches all boundary derivatives through `K` exactly. Therefore, with

\[
F_Q(u):=p^uD_Q(1+u),
\]

we have

\[
F_Q^{(m)}(0)=0
\qquad(0\le m\le K).
\tag{23}
\]

Since `F_Q=F_S+F_G`, equation (22) and the Leibniz rule imply

\[
|F_S^{(m)}(0)|
=|F_G^{(m)}(0)|
\ll_K\frac{(\log p)^m}{p^2}
\qquad(0\le m\le K).
\tag{24}
\]

Apply Taylor's theorem to `F_S` using (16):

\[
|F_S(u)|
\ll_K
\sum_{m=0}^K
\frac{(\log p)^m}{p^2}u^m
+
 d_pu^{K+1}.
\tag{25}
\]

Multiplying by `p^{-u}` and optimizing each monomial gives

\[
\sup_{u\ge0}|D_{S_p}(1+u)|
\ll_K
\frac1{p^2}
+
\frac{d_p}{(\log p)^{K+1}}.
\tag{26}
\]

Finally add the uniform padding estimate (21). This proves (1).

The proof also shows why the result is stronger than taking a larger fixed window in `RE-191` or increasing `R` in `RE-192`--`RE-193`. The source is not merely compressed by the real Euler channel. It lies in a concrete near-null direction of the **entire** one-sided channel, with a quantitative null depth set by the number of exact boundary jets and the centered log-transport moment of the repair.

## Representation audit

The decisive representation is not raw temperature width. Write `s=1+u` and factor the common selector decay `p^{-u}`. The remaining kernel is an exponential in the centered coordinate

\[
n\log q-\log p.
\]

Exact boundary jets kill the first Taylor coordinates of this normalized profile. The `RE-182` repair pays only bounded selector-scale moments in `log(q/p)`, so the first surviving Taylor remainder is `O_K(d_pu^{K+1})`. The factor `p^{-u}` then turns this into the global maximum `O_K(d_p/(\log p)^{K+1})`.

This is a stable-information statement, not an exact-identification theorem. `RE-174` remains untouched: exact values at an unbounded temperature set can identify the infinite prime source. Here `D_Q` is not identically zero. The result says instead that the whole real profile can approach zero much faster than the physical selector debt while the Robin destination remains macroscopically different. Any use of exact analytic continuation is therefore using precision far below the selector scale.

The arbitrary-variation padding plays a second, logically independent role. Its huge unsigned reciprocal mass need not satisfy bounded centered moments, but greedy Chebyshev balancing makes its complete real transform `O(p^-2)` directly. Thus neither raw reciprocal variation nor real spectral span supplies a coercive stable complexity on this source class.

## Adversarial self-review

**Does observing every real `s>=1` exactly still identify the source?** Yes. There is no contradiction with `RE-174` or standard uniqueness of Laplace/Dirichlet transforms. The profile in (1) is small, not zero. The finding is about stability at Robin-relevant precision.

**Is the bound uniform as `s` tends to infinity?** Yes. For the structured repair, the optimization in (10) is over the whole half-line `u>=0`; for the padding, (19)--(21) have constants independent of the upper temperature endpoint.

**Could enormous `Lambda_p` destroy the estimate through a huge terminal `Y`?** No. The padding is handled through its signed Chebyshev primitive rather than its unsigned mass. Equation (19) depends only on the lower support edge `X` and the bound `|A_G(t)|<=log t`; the absolutely convergent prime-power tail in (20) is bounded by the full integer tail beyond `X`, independently of how many padding primes are used.

**Does the structured repair really have all centered moments bounded by `d_p`?** For each fixed moment order, yes, because the generation mass is geometrically summable while `log(q/p)` grows only linearly with generation index. This is exactly the combination in (13)--(15). No statement uniform in growing `K` is made.

**Does this close the growing-jet region between `RE-188` and `RE-189`?** No. `K` is fixed before `p` tends to infinity. The constants in the interpolation, the centered moments, and the Taylor remainder may grow rapidly with `K`. The result rules out every fixed log-power stable precision on the full real axis, not an arbitrarily shrinking precision or a growing-depth exact germ.

**Does the argument cover complex temperatures `s=1+u+it`?** No. The positivity of the rates in (7) controls the real ray. Vertical phases probe `log q` rather than merely damping it and can behave differently. A genuinely complex/nonlocal observable is therefore not ruled out by this finding.

## Prior-art audit

The generic warning is classical. Inversion of the Laplace transform is a paradigmatic severely ill-posed problem; for example, Epstein and Schotland, *The Bad Truth about Laplace's Transform*, SIAM Review **50** (2008), 504--520, analyze its spectral ill-conditioning and regularized inversion. Greedy signed harmonic balancing and Abel summation are also classical mechanisms. Targeted searches found no external theorem needed for (1): the log-power estimate is an elementary Taylor/transport consequence once the exact `RE-182` source geometry is inserted.

No novelty is claimed for Laplace ill-posedness, Taylor remainder bounds, or greedy sign balancing in isolation. The line-specific content is the quantitative splice: the ordinary-prime `{0,1,2}` repair has selector-scale centered log moments, exact finite Euler jets annihilate the corresponding normalized Taylor coordinates, and the disjoint arbitrary-variation padding is uniformly `O(p^-2)` on the complete real Euler ray. No new load-bearing external dependency is introduced, so `SOURCES.md` is unchanged.

## What this changes

The scalar frontier narrows again. **Real spectral span is no longer a plausible stable-rigidity resource by itself.** Even the complete one-sided real Euler profile can be smaller than the selector debt by any prescribed fixed power of `log p`, while a bounded-multiplicity source preserves KV fidelity and an order-one transient Robin displacement.

What remains genuinely distinct is: precision shrinking faster than every fixed log power; boundary depth growing with `p` in the unresolved region between `RE-188` and `RE-189`; or observables that introduce vertical/complex phase or otherwise leave the one-sided real scalar Euler channel. Exact analytic identification remains mathematically true but, on this matched-control class, is not a selector-scale stability mechanism.

## Sources

- `RE-182`, exact fixed-depth ordinary-prime Euler-jet repair and its geometric generation-mass bounds.
- `RE-190`--`RE-193`, shrinking/fixed/large real-temperature compression of the scalar Euler channel.
- `RE-195`, arbitrary-variation Chebyshev-balanced padding and the disjoint repair channel.
