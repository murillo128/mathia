# ANF-207 — Shrinking notches force a sharp cardinality scale below the cusp threshold

**Status:** EXACT-DERIVED + REAL-LATTICE-WITNESS + COMPLEX-CARDINALITY-LOWER-BOUND + SINGULAR-WIDTH-LIMIT. A triangular notch whose removed height is proportional to its width admits an energy drop of order `eta^(4/3)` with `Theta(eta^(-2/3))` real points. Every conjugation-invariant complex multiset reaching this same certified drop needs at least that order of cardinality. This holds below, at, and above the distant-copy cusp threshold. A related comparison bounds the initial real two-site attainment interval by `O(eta^3)` in amplitude. Neither finite nonattainment at a fixed subcritical width nor a matching lower bound on the unrestricted energy floor is asserted.

## Object and quantitative statement

Use the Fourier convention `f_hat(x)=int f(u) exp(-2 pi i u x) du` and
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,
\]
\[
K(x)=\frac{\cos(\pi x)-\sqrt2\pi\cot(1/\sqrt2)x\sin(\pi x)}
{1-2\pi^2x^2},\qquad K(0)=1,
\tag{1}
\]
with the removable values continued. For `0<eta<=1/2`, put
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\qquad
J_{\eta,a}=J_0-a\tau_\eta,\qquad
\widehat{a\tau_\eta}(x)=a\eta\operatorname{sinc}^2(\eta x).
\tag{2}
\]
Here `sinc(x)=sin(pi x)/(pi x)`, with its continuous value at zero.
Here `a` is the **removed spectral height**, not the relative amplitude
`t` of ANF-200--ANF-206. Fix `b=1/10`; then
`phi_eta=b tau_eta<=J_0` and `a=bt`. Indeed `g>=3/4` on its support,
so `J_0(u)>=(9/16)(1-|u|)`, which exceeds `b` on `[-eta,eta]`.
We restrict to `0<a<=b/2`, so `0<t<=1/2` and
\[
J_{\eta,a}\ge(1-t)J_0\ge\tfrac12J_0.
\tag{3}
\]

For a nonempty finite conjugation-invariant multiset `W`, let
\[
N=|W|,\quad L(W)=2N-\sigma(W),\quad
S_W(u)=\sum_{z\in W}e^{-2\pi iuz},\quad
Q_{\eta,a}(W)=\frac{\int J_{\eta,a}|S_W|^2}{L(W)}.
\tag{4}
\]
All entries include positive integer multiplicities; `sigma` counts
distinct simple real sites. In particular `N<=L<=2N`. The source
inequality is `E_0(W):=int J_0|S_W|^2>=L(W)`.

Fix any `lambda>0` and set `a=lambda eta` before sending `eta` to zero.
With
\[
c_0=\frac1{2\pi^2},\qquad c_\lambda=c_0\lambda^{4/3},
\tag{5}
\]
the following assertions hold for all sufficiently small `eta`, with
the onset allowed to depend on `lambda`:

1. An explicit distinct real lattice segment `X_eta` satisfies
   \[
   Q_{\eta,\lambda\eta}(X_\eta)
   \le1-c_\lambda\eta^{4/3},\qquad
   |X_\eta|\sim\frac{\lambda^{1/3}}2\eta^{-2/3}.
   \tag{6}
   \]
2. Every conjugation-invariant complex multiset satisfying the energy
   inequality in (6) has
   \[
   \boxed{|W|>\frac{c_0\lambda^{1/3}}4\eta^{-2/3}.}
   \tag{7}
   \]

Thus the least cardinality needed to reach this **specified energy
benchmark** is `Theta_lambda(eta^(-2/3))`, even when arbitrary complex
heights, multiplicities and horizontal spans are allowed. The exponent
is sharp for this benchmark, not asserted to describe actual global
minimizers or the exact floor.

Writing `q_infty` for the unrestricted infimum and `q_m` for the same
infimum with `N<=m`, (6)--(7) give `q_infty<q_m` for every fixed `m`
once `eta` is small enough; a direct gap estimate appears below.
Any attained unrestricted minimizer must obey (7). Configurations
within `(c_lambda/2) eta^(4/3)` of the unrestricted infimum obey the
same order of lower bound, with its constant halved.

## Integer spacing balances fourth-power source cost against notch gain

The construction works more generally whenever
\[
0<a\le b/2,\qquad 0<\eta\le\min(1/2,a^{1/3}/4).
\tag{8}
\]
Choose
\[
\ell=\lceil a^{-1/3}\rceil\in\mathbb N,\qquad
M=\left\lfloor\frac1{2\eta\ell}\right\rfloor+1,\qquad
X=\{0,\ell,\ldots,(M-1)\ell\}.
\tag{9}
\]
Then `M>=2`, `L(X)=M`, `ell<=2a^(-1/3)`, and the span is at most
`1/(2eta)`. At nonzero integer arguments (1) gives exactly
\[
F(k\ell)=\frac1{(1-2\pi^2k^2\ell^2)^2}.
\tag{10}
\]
This is the integer-lattice calibration of ANF-114. Retaining the
finite boundary factors,
\[
\frac{E_0(X)}M-1
=2\sum_{k=1}^{M-1}\left(1-\frac kM\right)F(k\ell)
\le C_*\ell^{-4}\le C_*a^{4/3},
\quad C_*:=\frac8{3(2\pi^2-1)^2}<\frac1{2\pi^2}.
\tag{11}
\]
Here `sum k^(-4)<=4/3` suffices. The displayed constant inequality
also follows from `3<pi<4`.

For `|v|<=1/2`, concavity of sine gives `sinc^2(v)>=4/pi^2`.
Every ordered pair difference in (9) is in that range after
multiplication by `eta`. Consequently
\[
\frac{E_{a\tau_\eta}(X)}M
=\frac{a\eta}M\sum_{x,y\in X}\operatorname{sinc}^2(\eta(x-y))
\ge\frac4{\pi^2}a\eta M
\ge\frac{2a}{\pi^2\ell}
\ge\frac1{\pi^2}a^{4/3}.
\tag{12}
\]
Subtracting (12) from (11) proves the finite, explicit bound
\[
\boxed{Q_{\eta,a}(X)\le1-c_0a^{4/3}.}
\tag{13}
\]
No thermodynamic limit or interchange of an infinite lattice sum with
the notch limit is used. For `a=lambda eta`, (8) holds for small
`eta`, and the ceiling and floor in (9) give the cardinality asymptotic
in (6). The scales are `ell~a^(-1/3)` and `M~a^(1/3)/(2eta)`:
the retained source cost `ell^(-4)` balances the removable energy
`a/ell`.

## Complex height cannot replace the required cardinality

Suppose `Q_{eta,a}(W)<=1`. By (3),
\[
E_0(W)\le\frac{L(W)}{1-t}\le4N.
\tag{14}
\]
ANF-201's source-energy height estimate therefore gives
\[
H(W):=\max_{z\in W}|\Im z|
\le h(N):=\frac{2N}{\pi}
\log\left[2\left(1+4N\sqrt{\mathfrak h_N/j_*}\right)\right]
=O(N\log(2+N)),
\tag{15}
\]
where `mathfrak h_N=sum_(k=1)^N 1/k` and
`j_*=(1/4)cot^2(1/sqrt(2))>0`. This bound includes repetitions
and is independent of all horizontal separations.

The mechanism behind (15) is worth retaining because it permits a
growing cap here. Since `J_0>=j_*` on `[-1/2,1/2]`, averaging
`sum_(k=1)^N |S_W(kd)|^2` over
`1/(4N)<=d<=1/(2N)` produces one common spacing with every sampled
power sum bounded by `sqrt(4N mathfrak h_N E_0/j_*)`.
Newton's identities for the `N` roots `exp(-2 pi i d z)` then bound
their moduli by twice one plus this bound. Conjugation supplies a
root with modulus `exp(2 pi d H)`. This gives (15); no inverse
Vandermonde matrix or site separation assumption enters.

For `|u|<=eta`, the triangle inequality gives
`|S_W(u)|<=N exp(2 pi eta H(W))`. Since `int tau_eta=eta`,
\[
\frac{E_{a\tau_\eta}(W)}{L(W)}
\le a\eta N\exp(4\pi\eta h(N)).
\]
Together with `E_0/L>=1`, this yields
\[
\boxed{Q_{\eta,a}(W)\ge
1-a\eta N\exp(4\pi\eta h(N))\qquad(Q_{\eta,a}(W)\le1).}
\tag{16}
\]
This uses the whole nonnegative source, not signs of individual
complex pair terms.

Now set `a=lambda eta` and
`k_lambda=c_lambda/(4lambda)=c_0 lambda^(1/3)/4`.
Uniformly for integers `1<=N<=k_lambda eta^(-2/3)`, (15) implies
\[
\eta h(N)=O_\lambda(\eta^{1/3}\log(1/\eta))\longrightarrow0.
\tag{17}
\]
For sufficiently small `eta` the exponential in (16) is at most two.
Such configurations then satisfy
\[
Q_{\eta,\lambda\eta}(W)
\ge1-2\lambda\eta^2N
\ge1-\tfrac12c_\lambda\eta^{4/3},
\tag{18}
\]
which excludes the benchmark in (6) and proves (7). Configurations
with `Q>1` already fail the benchmark. The same argument with
`c_lambda/2` proves the approximate-minimizer assertion.

For a fixed cap `m`, the exponential is at most two for small `eta`,
so the sharper elementary comparison is
\[
q_m\ge1-2\lambda m\eta^2,
\qquad q_\infty\le1-c_\lambda\eta^{4/3}<q_m.
\tag{19}
\]
This does not need attainment of `q_m`. In the real class `H=0`,
and (16) holds without any restriction on energy or any exponential
factor.

## The initial real two-site interval must shrink at least cubically

For an arbitrary real multiset supported on at most two distinct
sites, write its positive integer multiplicities as `m_i` and put
`D=sum_i m_i^2`. The real source interactions are nonnegative,
`D>=L`, and `N^2<=2D`. Therefore, whenever `2a eta<1`,
\[
Q_{\eta,a}(W)\ge\frac{D-a\eta N^2}{L}
\ge1-2a\eta.
\tag{20}
\]
This covers unequal and arbitrarily large multiplicities, not only
simple pairs. Combining (13) and (20), no such configuration can
attain the unrestricted real floor when (8) holds and
\[
a^{1/3}>4\pi^2\eta.
\tag{21}
\]
For example take `a=(8 pi^2 eta)^3`; for all sufficiently small
`eta` it is admissible and (13) is at most `1-4a eta`, strictly
below (20). In the relative amplitude `t=a/b`, any initial interval
on which the ANF-200 two-site formula is valid throughout consequently
has endpoint at most
\[
\boxed{\frac{(8\pi^2)^3}{b}\eta^3.}
\tag{22}
\]
The constant is deliberately crude. No matching lower bound on that
interval is proved. ANF-200 still guarantees a positive interval
for every fixed width; (22) quantifies its possible deterioration
as the profile changes.

## Relation to the cusp, prior art and evidence boundary

Put `d=(1/2)cot^2(1/sqrt(2))`. ANF-205--ANF-206 place the exact
distant-copy threshold at removed height `a_c=d eta`. Thus
`a=lambda eta` with `0<lambda<d` is strictly subcritical, and
`lambda=d` is critical. Equations (6)--(7) still apply in both
regimes. Finite configurations passing every sufficiently distant
duplicate test therefore coexist with a requirement for growing
cardinality to reach the displayed energy benchmark as width shrinks.
Equation (22) lies at a still smaller amplitude scale than `a_c`.

The lattice identity and fourth-power cost are already ANF-114;
the height estimate is ANF-201. ANF-075 supplies a different
finite-support affine certificate and objective comparison, not the
energy separation (19). ANF-200 fixes the profile before shrinking
amplitude. The additional result here is the simultaneous
width/amplitude limit, its explicit finite lattice witness, the
matching complex cardinality lower bound for that witness's energy
scale, and the resulting upper bound (22) on the real two-site window.

The source inequality is [Lamzouri, Proposition 2.1](https://arxiv.org/html/2609.02882v2#S2).
Only its auxiliary Hilbert-space statement is used. The kernel is the
classical [Carneiro--Chandee--Littmann--Milinovich extremizer](https://arxiv.org/abs/1406.5462).
[Suto's compact-Fourier ground-state theory](https://arxiv.org/pdf/math-ph/0508004)
and [Procacci's stability constant, equation (1.3)](https://arxiv.org/pdf/2005.10362)
provide the neighboring classical frameworks. Their fixed-density
infinite-volume results and gas expansions are not imported as
finite attainment or this width-dependent cardinality theorem.
Targeted searches on these frameworks, weak attraction and the
Montgomery--Taylor lattice kernel did not supply this exact
amplitude/width statement. No general crystallization theorem,
new power-sum theorem or exhaustive novelty claim is made; the
existing source anchors suffice.

The decisive controls are the **integer** spacing in (10), the finite
span condition in (12), the distinction between removed height `a`
and relative amplitude `t`, and the uniform estimate (17) at the
actual growing cap. For arbitrary noninteger spacing the source
tail is generally only inverse-square. Applying bounded-cardinality
compactness without its quantitative height bound would not justify
(17). Signed weights or non-conjugation-invariant sources do not
have the asserted height and baseline interfaces.

As a noncertifying arithmetic check, direct finite pair sums tested
(11)--(13) for `lambda=d/2,d,2d` and
`eta=10^(-2),10^(-3),10^(-4)`, and tested (20)--(22) at
`eta=10^(-4),10^(-5),10^(-6)`. All twelve double-precision checks
satisfied the displayed bounds. These samples do not certify a
limit, a complex lower bound or optimality; the inequalities above
are the proof, and the scratch calculation is not a repository
dependency.

This is a changing-profile limit. It proves neither nonattainment at
one fixed subcritical or critical profile, nor an exact
`Theta(eta^(4/3))` law for `1-q_infty`: a larger drop from other
configurations remains possible. It leaves the fixed-profile
unrestricted exposure envelope open. No improved critical-line
proportion, zero-density bound, RH consequence or Lean verification
is claimed.
