# MC-180 — A logarithmic prime split removes the Möbius smooth-support barrier and isolates a rough parity block

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-178` and `MC-179` show that the Chinis-style architecture cannot reach a fixed-power polynomial-window variance gain by repeatedly removing individual large prime factors and then paying for the terminal smooth sector by support cardinality. The obstruction is real for that method class, but Möbius has a more rigid support feature that changes the decomposition problem: on its nonzero support every prime occurs at most once.

Fix

\[
0<\theta<1,
\qquad H=X^\theta,
\tag{1}
\]

and choose a fixed constant

\[
0<c<\min(\theta,1-\theta),
\qquad y=c\log X.
\tag{2}
\]

Put

\[
Q_y=\prod_{p\le y}p,
\tag{3}
\]

and define two multiplicative functions

\[
f_y(n)=\mu(n)\mathbf 1_{P^+(n)\le y},
\qquad
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y},
\tag{4}
\]

with the conventions `P^+(1)=1` and `P^-(1)=infinity`. At every prime, `f_y` owns the Euler factor `1-z` when `p<=y` and `g_y` owns it when `p>y`. Hence

\[
\boxed{f_y*g_y=\mu}
\tag{5}
\]

exactly.

The small-prime factor has finite square-free support:

\[
\boxed{f_y(a)\ne0\iff a\mid Q_y.}
\tag{6}
\]

The prime number theorem gives

\[
\log Q_y=\vartheta(y)=y+o(y),
\qquad
2^{\pi(y)}=X^{o(1)},
\tag{7}
\]

so `(2)` yields

\[
\boxed{Q_y=X^{c+o(1)}<\min(H,X/H)}
\tag{8}
\]

for all sufficiently large `X`. In particular, a square-free integer all of whose prime factors are at most `y` is at most `Q_y<X`. Thus **the pure `y`-smooth Möbius sector contributes nothing at all on `[X,2X]`**. The positive-density smooth-number remainder from `MC-178` is therefore not an intrinsic Möbius obstruction once the cutoff is lowered to logarithmic size and all primes above the cutoff are extracted as one composite block.

The price is equally exact. Define the rough Möbius interval sum

\[
R_y(u,L)
:=
\sum_{u<m\le u+L}g_y(m)
=
\sum_{\substack{u<m\le u+L\\P^-(m)>y}}\mu(m).
\tag{9}
\]

Then `(5)` gives, for every real `x`,

\[
\boxed{
\sum_{x<n\le x+H}\mu(n)
=
\sum_{a\mid Q_y}\mu(a)
R_y\!\left(\frac xa,\frac Ha\right).
}
\tag{10}
\]

So the growing one-prime-at-a-time extraction depth of `MC-179` can indeed be bypassed: all primes larger than `y` are carried by the single structured rough factor `g_y`, while the complementary small-prime factor `a` has only `X^{o(1)}` possible values and is uniformly shorter than both `H` and `X/H`.

More importantly, this split preserves the fixed-power local-variance currency with only subpower loss. Write

\[
V_y(U,L)
:=
\int_U^{2U}|R_y(u,L)|^2\,du.
\tag{11}
\]

Cauchy--Schwarz in `(10)` followed by `u=x/a` gives the exact transfer inequality

\[
\boxed{
V_\mu(X,H)
\le
2^{\pi(y)}
\sum_{a\mid Q_y}a\,
V_y\!\left(\frac Xa,\frac Ha\right),
}
\tag{12}
\]

where

\[
V_\mu(X,H)
=
\int_X^{2X}
\left|\sum_{x<n\le x+H}\mu(n)\right|^2dx.
\tag{13}
\]

Consequently, if for some fixed `0<eta<=1` one can prove uniformly for every `a|Q_y` that

\[
V_y\!\left(\frac Xa,\frac Ha\right)
\le
X^{o(1)}\frac Xa
\left(\frac Ha\right)^{2-\eta},
\tag{14}
\]

then

\[
\boxed{
V_\mu(X,H)
\le
X^{1+o(1)}H^{2-\eta}.
}
\tag{15}
\]

Indeed,

\[
2^{\pi(y)}=X^{o(1)}
\tag{16}
\]

and

\[
\sum_{a\mid Q_y}a^{\eta-2}
=
\prod_{p\le y}(1+p^{\eta-2})
=
\begin{cases}
O_\eta(1),&0<\eta<1,\\
X^{o(1)},&\eta=1.
\end{cases}
\tag{17}
\]

For `eta=1`, the last product is only `O(log y)` by the prime harmonic sum. Thus a fixed-power variance theorem for the **rough parity block at the scaled windows in `(14)`** transfers to the full Möbius variance without losing the fixed exponent. By `MC-177`, it would then imply the global Mertens power bound

\[
M(x)
\ll
x^{\max(1-\theta\eta/2,\theta)+o(1)}.
\tag{18}
\]

This identifies a sharper surviving source-side target after `MC-178`--`MC-179`: not another bounded number of large-prime extractions, and not support sparsity of a terminal smooth set, but phase-sensitive short-interval control of a logarithmically sifted **rough Möbius sum**.

## 1. Why the smooth Möbius remainder collapses at logarithmic cutoff

For a generic `y`-smooth integer, arbitrarily high prime powers allow the integer to be much larger than the primorial `Q_y`. That is why ordinary smooth-number counting remains a nontrivial problem even when the allowed prime set is finite.

Möbius removes exactly this freedom. If `f_y(a)` is nonzero, then `a` is square-free and every prime divisor of `a` is at most `y`; therefore each such prime appears at most once and `a|Q_y`. Conversely every divisor of `Q_y` is square-free and has all prime factors at most `y`, proving `(6)`.

With `y=c log X`, the prime number theorem in Chebyshev form gives

\[
\log Q_y=\sum_{p\le y}\log p=y+o(y),
\]

so `Q_y=X^(c+o(1))`. The inequalities in `(2)` provide fixed power room on both sides of `(8)`. They also ensure `H/a` tends to infinity uniformly for `a|Q_y`, so `(14)` does not hide intervals of vanishing length.

The number of possible small-prime factors is

\[
d(Q_y)=2^{\pi(y)}
=
\exp\!\left((\log2+o(1))\frac{c\log X}{\log\log X}\right)
=X^{o(1)}.
\tag{19}
\]

This is the essential rate difference from the individual-prime extraction counted in `MC-179`. A worst-case integer can contain order `log X/log log X` primes near a logarithmic threshold, but **their entire large-prime part can be kept as one coefficient object** while the complementary product of all small primes ranges over only a subpower family.

## 2. Exact variance transfer to the rough block

Equation `(10)` follows by summing the convolution `(5)` over the interval. Because `f_y` is supported exactly on divisors of `Q_y`, no other `a` occurs.

For each `x`, Cauchy--Schwarz gives

\[
\left|\sum_{x<n\le x+H}\mu(n)\right|^2
\le
2^{\pi(y)}
\sum_{a\mid Q_y}
\left|R_y\!\left(\frac xa,\frac Ha\right)\right|^2.
\tag{20}
\]

Integrating over `X<=x<=2X` and substituting `u=x/a` in each term proves `(12)`.

Under `(14)`, the `a`-th term after the change of variables is

\[
a\,V_y(X/a,H/a)
\le
X^{o(1)}XH^{2-\eta}a^{\eta-2}.
\tag{21}
\]

Summing `(21)` and using `(16)`--`(17)` proves `(15)`. Nothing in this step uses analytic continuation, `1/zeta(s)`, a zero-free region, or a random-walk model.

The reduction is one-way: it says that sufficiently strong rough-block variance is enough to control Möbius. It does **not** assert that the rough-block estimate is currently accessible, nor that passing to rough numbers makes the sign problem easy.

## 3. The rough factor is not a sparse error; it is the parity carrier

The remaining factor

\[
g_y(n)=\mu(n)\mathbf1_{P^-(n)>y}
\tag{22}
\]

is not power-sparse. Every prime `p>y` belongs to its support with value `-1`, so already

\[
\#\{n\le X:g_y(n)\ne0\}
\ge
\pi(X)-\pi(y)
=X^{1-o(1)}.
\tag{23}
\]

Thus replacing the old smooth-remainder cardinality estimate by a cardinality estimate for the rough factor merely moves the problem; it cannot supply the fixed-power saving in `(14)`.

More structurally, on its support

\[
g_y(n)=(-1)^{\omega(n)}.
\tag{24}
\]

So the sign that `(14)` must exploit is exactly parity of the number of rough prime factors. This meets the sieve-parity obstruction already isolated in `MC-082`: local divisor densities or unsigned sieve remainders can be extremely accurate while forgetting the parity signal. The classical Friedlander--Iwaniec parity-sensitive sieve (`MC-S40`) shows that this is not an impossibility theorem for every sieve-flavored method; it says that a viable proof of `(14)` must retain additional signed bilinear, Type-II, harmonic, or comparably parity-sensitive coupling.

The decomposition therefore sharpens rather than removes the obstacle. `MC-179` left three escapes: signed cancellation in the smooth sector, composite-block extraction, or a genuinely growing-depth multiscale scheme. The present result makes the composite-block escape precise and shows where its difficulty lands: **rough prime-factor parity at logarithmic sifting level**.

## 4. Standalone rough power cancellation is not a cheap substitute

Let

\[
G_y(t)=\sum_{m\le t}g_y(m).
\tag{25}
\]

Summing `(5)` gives

\[
\boxed{
M(X)=\sum_{a\mid Q_y}\mu(a)G_y(X/a).
}
\tag{26}
\]

Suppose, for some fixed `alpha>0`, that one first proves the standalone bound

\[
G_y(t)\ll X^{o(1)}t^\alpha
\tag{27}
\]

uniformly for `X/Q_y<=t<=X`. Then `(26)` yields

\[
|M(X)|
\le
X^{\alpha+o(1)}
\prod_{p\le y}(1+p^{-\alpha})
=
X^{\alpha+o(1)}.
\tag{28}
\]

The last equality follows because for every fixed `alpha>0`,

\[
\sum_{p\le c\log X}p^{-\alpha}=o(\log X).
\tag{29}
\]

Hence a fixed global power bound for the moving rough sum already transfers, up to subpower loss, to the same global power bound for `M`. That route does not create an independently cheap source estimate. The genuinely different target is the local second-moment statement `(14)`, whose arithmetic proof could in principle use cancellation available only after averaging interval locations while still feeding the Gallagher currency of `MC-177`.

## 5. Prior art and novelty assessment

The prime partition in `(4)`--`(5)` is classical Euler-factor algebra. It is also a scale-dependent instance of the prime-partition normal form proved in `MC-079`; no novelty is claimed for splitting the rational primes at a cutoff or for the convolution identity itself.

The rough Möbius factor is established prior art, not a newly invented Mathia object. Krishnaswami Alladi, *Asymptotic estimates of sums involving the Moebius function*, Journal of Number Theory 14 (1982), 86--98, DOI `10.1016/0022-314X(82)90060-9`, studies precisely

\[
M(x,y)=\sum_{\substack{n\le x\\P^-(n)>y}}\mu(n),
\tag{30}
\]

with the smallest-prime-factor cutoff. His companion paper, *Asymptotic estimates of sums involving the Moebius function. II*, Transactions of the American Mathematical Society 272 (1982), 87--105, DOI `10.1090/S0002-9947-1982-0656482-7`, studies the complementary largest-prime-factor/smooth Möbius sum. Donald G. Hazlewood, *Sums over numbers with restricted prime factors*, Journal of Number Theory 17 (1983), 350--365, DOI `10.1016/0022-314X(83)90053-7`, treats a broader restricted-prime-factor framework including `g(n)=mu(n)`.

Recent work confirms that the rough side remains an active analytic object. Yazan Alamoudi, *On subradically sifted sums related to Alladi's higher order duality between prime factors*, arXiv:2601.10636 (2026), studies quantitative estimates for higher-order rough Möbius sums and includes `k=1` as the Alladi-type base case. This is a recent preprint and is used here only as a prior-art boundary; no theorem from it is promoted to independently verified evidence for `(14)`.

The classical sieve parity phenomenon is already anchored in `MC-S39`, and `MC-S40` records a setting where additional harmonic structure breaks it. None of these sources supplies the polynomial-window rough Möbius variance estimate `(14)` required here.

The durable Mathia contribution is therefore the **rate-preserving reduction `(12)`--`(17)` at logarithmic cutoff**. It connects three previously separate boundaries in the line: the square-free support specificity excluded from the generic smooth-number argument of `MC-178`, the composite-block escape explicitly left open by `MC-179`, and the parity-information obstruction of `MC-082`. The resulting target is narrower and source-facing: prove or rule out fixed-power short-interval variance for logarithmically rough Möbius coefficients at the scaled family of windows in `(14)`.

## 6. Boundaries and falsification tests

- The support collapse `(6)` is Möbius-specific. It uses square-free support; it is false for Liouville and for generic smooth integers because prime powers are then allowed.
- The cutoff must satisfy `c<min(theta,1-theta)` for the uniform shortening statement `(8)`. Taking `c` near or above either boundary changes the scaled-window geometry and is outside this claim.
- Equation `(15)` is conditional on the uniform rough-block variance input `(14)`. The finding does not prove such an estimate.
- A global bound for the rough partial sum is not counted as a cheaper route: `(26)`--`(29)` show why a fixed-power bound transfers almost directly back to `M`.
- The rough support is dense at power scale, so support cardinality alone is not the missing gain. The required information is signed.
- Ordinary parity-blind sieve data are not enough by `MC-082`, but parity-sensitive bilinear or harmonic methods are not ruled out; `MC-S40` is the explicit classical warning against overextending the parity barrier.
- Alladi's, Hazlewood's, and Alamoudi's rough/sifted sums are prior art. The claim of this finding is not that the rough Möbius function is new, but that the logarithmic prime split gives an exact subpower-cost transfer from its local variance to the current Gallagher/Mertens frontier.

The exact derivation is falsified if the local Euler factors do not give `(5)`, if a nonzero `f_y(a)` need not divide `Q_y`, if the prime number theorem fails to imply `(7)`--`(8)`, or if the Cauchy/change-of-variables calculation does not yield `(12)`. The frontier interpretation is falsified if existing literature already proves `(14)` with some fixed `eta>0` uniformly over the required scaled windows, in which case `MC-177` would immediately convert that theorem into a new global Mertens power bound and the line should record the resulting consequence instead.

## Consequence for the live frontier

The next factorization attack should no longer ask how many individual primes must be peeled before the smooth remainder becomes sparse. At logarithmic cutoff, square-free support lets Möbius package the entire large-prime part into one classical rough block while the complementary small-prime factor has only `X^{o(1)}` states and lies below `X/H`.

The decisive question is now concrete: **can the logarithmically rough Möbius coefficients satisfy a fixed-power short-interval second-moment estimate of the form `(14)` by genuinely parity-sensitive source arithmetic?** A positive answer at any fixed `eta>0` would survive the reduction to full Möbius variance and enter `MC-177`; a proof that all currently accessible rough-sum machinery remains only logarithmic/subpower would close this composite-block escape as cleanly as `MC-179` closed bounded-depth support-only extraction.