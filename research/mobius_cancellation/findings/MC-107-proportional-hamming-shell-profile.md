# MC-107 — Proportional Hamming shells stay positive and force radial cancellation into the `2 log log N` scale

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the exact source-forced Hamming deformation from `MC-092`, `MC-095`, `MC-105`, and `MC-106`:

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
C_{k,N}=\sum_{\substack{a\ \mathrm{squarefree}\\\omega(a)=k}}W_N(a),
\tag{1}
\]

and its pair representation

\[
\mathcal Q_N(t)
=\sum_{m,n\le N}\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right),
\qquad
z(x)=\lfloor x\rfloor+\frac12-x.
\tag{2}
\]

Write

\[
L:=\log\log N,
\qquad
J:=\int_0^1\!\int_0^1 z\!\left(\frac1{uv}\right)du\,dv
=\gamma+\gamma_1-\frac12>0.
\tag{3}
\]

`MC-106` proved positivity and a Landau profile only for moving degrees `k=o(L)`. The same source kernel can be carried through the full proportional Sathe–Selberg regime.

Let `k=k_N` satisfy

\[
\beta_N:=\frac{k-2}{2L}\longrightarrow\beta\in(0,\infty).
\tag{4}
\]

Then

\[
\boxed{
C_{k,N}
\sim
J\,\mathcal A(\beta)
\frac{N^2}{(\log N)^2}
\frac{(2L)^{k-2}}{(k-2)!},
}
\tag{5}
\]

where

\[
\boxed{
\mathcal A(\beta)
:=
\frac1{\Gamma(1+\beta)^2}
\prod_p
\left(1+\frac{2\beta}{p}+\frac1{p^2}\right)
\left(1-\frac1p\right)^{2\beta}.
}
\tag{6}
\]

The Euler product in `(6)` converges locally uniformly for positive `beta`, and every local factor is positive. Hence

\[
\boxed{C_{k,N}>0}
\tag{7}
\]

eventually for every proportional degree `k~2 beta log log N`. There is therefore **no sign transition of the radial shell coefficients anywhere at fixed positive Sathe–Selberg scale**.

Moreover, uniformly when `beta_N` stays in a compact subinterval of `(0,infinity)`, consecutive shells satisfy

\[
\boxed{
\frac{C_{k+1,N}}{C_{k,N}}
=\left(1+o(1)\right)\frac{2L}{k-1}.
}
\tag{8}
\]

Thus the positive shell magnitudes increase while `k<(2-o(1))L`, turn at the scale

\[
k\sim2\log\log N,
\tag{9}
\]

and decrease after that scale. At the turning parameter `beta=1`, the arithmetic factor simplifies exactly to

\[
\mathcal A(1)
=\prod_p(1-p^{-2})^2
=\frac1{\zeta(2)^2}
=\frac{36}{\pi^4}.
\tag{10}
\]

Consequently any sequence with `k-2=2L+O(1)` has a positive shell of order

\[
\boxed{
C_{k,N}
\sim
\frac{36J}{\pi^4\sqrt{4\pi L}}\,N^2.
}
\tag{11}
\]

The shell cascade therefore reaches an `N^2/sqrt(log log N)` peak even though the hard endpoint remains, by the unconditional Korobov–Vinogradov input already used in `MC-098`, `MC-105`, and `MC-106`,

\[
\mathcal Q_N(1)
=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\qquad\text{for every fixed }A>0.
\tag{12}
\]

There is a stronger radial-truncation consequence below the peak. Fix `0<beta<1` and let `K=K_N` satisfy `(K-2)/(2L)->beta`. Then

\[
\boxed{
\sum_{k=2}^{K}(-1)^k C_{k,N}
\sim
(-1)^K\frac{C_{K,N}}{1+\beta}.
}
\tag{13}
\]

Since `C_{0,N}=O(N)`, `C_{1,N}=O(N log log N)`, and `(12)` is negligible compared with `(5)`, the omitted radial tail must satisfy

\[
\boxed{
\sum_{k>K}(-1)^k C_{k,N}
\sim
-(-1)^K\frac{C_{K,N}}{1+\beta}.
}
\tag{14}
\]

In particular, for every fixed `epsilon>0`, a radial cutoff at

\[
K=(2-\epsilon)\log\log N+O(1)
\tag{15}
\]

still misses a tail of the same asymptotic size as its last retained shell. `MC-106`'s `o(log log N)` barrier is therefore not the true radial scale: **any endpoint mechanism based on direct radial truncation must enter the `(2-o(1)) log log N` regime**. The first unresolved radial cancellation region is the turning zone around `2 log log N`, where adjacent positive shells become comparable and the external signs `(-1)^k`, rather than signs of the `C_{k,N}` themselves, can cancel across many degrees.

This result does not estimate `M(N)` or `M(N^2)`, does not prove that the endpoint cancellation is concentrated in a `sqrt(log log N)` central window, and does not provide a source-specific recurrence capable of transporting the endpoint.

## 1. Pairwise-coprime exact-degree counts have a two-variable Sathe–Selberg factor

As in `MC-105` and `MC-106`, write every square-free pair uniquely as

\[
b=(m,n),\qquad m=bd,\qquad n=be,
\tag{16}
\]

where `b,d,e` are pairwise coprime and square-free. With `x=N/b`,

\[
d_\triangle(m,n)=\omega(d)+\omega(e),
\qquad
z\!\left(\frac{N^2}{mn}\right)=z\!\left(\frac{x^2}{de}\right).
\tag{17}
\]

For fixed square-free `b`, introduce the two-variable Dirichlet series

\[
F_b(s,t;u,v)
:=
\sum_{\substack{d,e\ge1\\d,e\ \mathrm{squarefree}\\(d,e)=1\\(de,b)=1}}
\frac{u^{\omega(d)}v^{\omega(e)}}{d^s e^t}
=
\prod_{p\nmid b}\left(1+\frac{u}{p^s}+\frac{v}{p^t}\right).
\tag{18}
\]

Factor the two independent zeta singularities:

\[
F_b(s,t;u,v)=\zeta(s)^u\zeta(t)^v H_b(s,t;u,v),
\tag{19}
\]

where

\[
\begin{aligned}
H_b(s,t;u,v)
={}&\prod_{p\nmid b}
\left(1+\frac{u}{p^s}+\frac{v}{p^t}\right)
(1-p^{-s})^u(1-p^{-t})^v\\
&\times
\prod_{p\mid b}(1-p^{-s})^u(1-p^{-t})^v.
\end{aligned}
\tag{20}
\]

For `u,v` in a fixed compact set, the `p^{-s}` and `p^{-t}` terms cancel in the local logarithm, so `H_b` is represented by a normally convergent Euler product in a fixed product half-plane to the left of `(1,1)`. At the singular point,

\[
H_b(1,1;u,v)
=
H_0(u,v)
\prod_{p\mid b}\left(1+\frac{u+v}{p}\right)^{-1},
\tag{21}
\]

with

\[
H_0(u,v)
:=
\prod_p\left(1+\frac{u+v}{p}\right)
\left(1-\frac1p\right)^{u+v}.
\tag{22}
\]

This is the exact local correction that was invisible in `MC-106`: when the degrees are `o(L)`, the saddle parameters tend to zero and common-prime defects are `o(1)`; at proportional degree they contribute a nontrivial Euler factor and must not be discarded.

## 2. Coprimality inversion reduces the rectangle law to one-variable Sathe–Selberg

Let

\[
P_{j,l}^{(b)}(x;r,s)
:=
\#\left\{
\begin{array}{l}
d\le rx,\ e\le sx:\ d,e\text{ square-free},\\
(d,e)=1,\ (de,b)=1,\ \omega(d)=j,\ \omega(e)=l
\end{array}
\right\}.
\tag{23}
\]

Fix `0<delta<1` and compact positive saddle ranges for

\[
a=\frac{j-1}{\log\log x},
\qquad
c=\frac{l-1}{\log\log x}.
\tag{24}
\]

For square-free `c_0`, define

\[
A_m^{(c_0)}(X)
:=\#\{n\le X:n\text{ square-free},\ (n,c_0)=1,\ \omega(n)=m\}.
\]

Möbius inversion of `1_{(d,e)=1}` gives the exact identity, with `X=rx`, `Y=sx`, and `h=\omega(q)`,

\[
P_{j,l}^{(b)}(x;r,s)
=\sum_{\substack{q\ge1\\q\text{ square-free}\\(q,b)=1}}
\mu(q)
A_{j-h}^{(bq)}(X/q)
A_{l-h}^{(bq)}(Y/q),
\tag{R1}
\]

where a term is zero when one of the displayed indices is negative. Indeed, for square-free `d,e`, writing `d=qd'`, `e=qe'` after selecting `q|(d,e)` leaves the two residual variables independently square-free and coprime to `bq`; the remaining coupling is entirely in the `q`-sum.

The one-variable square-free Sathe–Selberg theorem gives, for each fixed square-free `c_0`,

\[
A_m^{(c_0)}(X)
\sim
\frac{X}{\log X}\frac{(\log\log X)^{m-1}}{(m-1)!}
\frac{G_{c_0}(\alpha)}{\Gamma(1+\alpha)},
\qquad
\alpha=\frac{m-1}{\log\log X},
\tag{R2}
\]

uniformly when `alpha` ranges in a compact subset of `(0,infinity)`, where

\[
G_{c_0}(z)=G(z)\prod_{p\mid c_0}(1+z/p)^{-1},
\qquad
G(z)=\prod_p(1+z/p)(1-1/p)^z.
\tag{R3}
\]

The finite-prime exclusion factor in `(R3)` follows directly from the square-free Euler product. For every fixed `q`, `log log(X/q)=log log x+o(1)` uniformly for `r in [delta,1]`, and if `h=\omega(q)` then

\[
\frac{L^{j-h-1}/(j-h-1)!}{L^{j-1}/(j-1)!}
=\frac{(j-1)_h}{L^h}\longrightarrow a^h,
\tag{R4}
\]

with the analogous limit `c^h` in the second coordinate. After normalizing `(R1)` by

\[
rs\frac{x^2}{(\log x)^2}
\frac{L^{j+l-2}}{(j-1)!(l-1)!},
\]

the fixed-`q` summand therefore tends to

\[
\frac{\mu(q)(ac)^{\omega(q)}}{q^2}
\frac{G_{bq}(a)G_{bq}(c)}{\Gamma(1+a)\Gamma(1+c)}.
\tag{R5}
\]

No uniform-in-`q` Sathe–Selberg asymptotic is needed. Split the `q`-sum at `q=x^{1/2}`. For `q\le x^{1/2}`, the standard uniform Sathe–Selberg/Hardy–Ramanujan upper bound, `A_m^{(bq)}\le A_m^{(1)}`, and `(j-1)_h/L^h,(l-1)_h/L^h=O_K(C_K^h)` on compact saddle ranges give the summable normalized majorant

\[
\ll_K \frac{C_K^{\omega(q)}}{q^2},
\qquad
\sum_{q\ \mathrm{squarefree}}\frac{C_K^{\omega(q)}}{q^2}
=\prod_p\left(1+\frac{C_K}{p^2}\right)<\infty.
\tag{R6}
\]

For `q>x^{1/2}`, the crude pair count is

\[
\sum_{q>x^{1/2}}\frac{XY}{q^2}=O(x^{3/2}),
\tag{R7}
\]

which is negligible against every fixed proportional Sathe–Selberg scale `x^2` times a fixed power of `log x`. The estimates are uniform for `r,s in [delta,1]`, so dominated convergence applies to `(R1)`.

The resulting constant is exactly the `H_b` factor from `(21)`. Factoring out the primes dividing `b`,

\[
\sum_{\substack{q\text{ square-free}\\(q,b)=1}}
\frac{\mu(q)(ac)^{\omega(q)}}{q^2}G_{bq}(a)G_{bq}(c)
=G_b(a)G_b(c)
\prod_{p\nmid b}
\left(1-\frac{ac}{p^2(1+a/p)(1+c/p)}\right).
\tag{R8}
\]

For `p\nmid b`, multiplying the local factors gives

\[
(1+a/p)(1+c/p)-ac/p^2=1+(a+c)/p,
\]

while for `p\mid b` only `(1-1/p)^{a+c}` remains. Hence `(R8)=H_b(1,1;a,c)`, and therefore, uniformly for `r,s in [delta,1]`,

\[
\boxed{
P_{j,l}^{(b)}(x;r,s)
=
\left(rs+o(1)\right)
\frac{x^2}{(\log x)^2}
\frac{(\log\log x)^{j+l-2}}
{(j-1)!(l-1)!}
\frac{H_b(1,1;a,c)}{\Gamma(1+a)\Gamma(1+c)}.
}
\tag{25}
\]

Thus the load-bearing rectangle law needs only one-variable square-free Sathe–Selberg plus exact coprimality inversion; no unproved two-variable Cauchy extension is required.

## 3. The source sawtooth kernel retains the same positive integral `J`

Equation `(25)` says that, after normalization, the exact-degree pair measure on `[0,1]^2` converges to Lebesgue measure, uniformly for saddle parameters in compact positive ranges. The kernel

\[
f(u,v)=z\!\left(\frac1{uv}\right)
\tag{26}
\]

is bounded by `1/2`. On every `[delta,1]^2` its discontinuities lie on finitely many hyperbolas `uv=1/q`, each of area zero. The mass near either coordinate axis is `O(delta)` by `(25)`. Therefore, exactly as in `MC-105` and `MC-106`, first sending `x->infinity` and then `delta->0` gives

\[
\begin{aligned}
&\sum_{\substack{d,e\le x\\d,e\ \mathrm{squarefree}\\(d,e)=1\\(de,b)=1\\\omega(d)=j\\\omega(e)=l}}
 z\!\left(\frac{x^2}{de}\right)\\
&\qquad\sim
J
\frac{x^2}{(\log x)^2}
\frac{(\log\log x)^{j+l-2}}
{(j-1)!(l-1)!}
\frac{H_b(1,1;a,c)}{\Gamma(1+a)\Gamma(1+c)}.
\end{aligned}
\tag{27}
\]

Thus the proportional-degree arithmetic correction changes the **mass** of the pair shell but not the source-kernel average `J`. Since `J>0`, any sign change would have to come from the arithmetic correction. Equation `(21)` shows that no such sign is available on positive saddles.

## 4. Summing the degree split concentrates at the symmetric saddle

For total degree `k`, write `j-1=q` and `l-1=k-2-q`. Ignoring for one line the slowly varying correction in `(27)`, the exact factorial weights satisfy

\[
\sum_{q=0}^{k-2}
\frac1{q!(k-2-q)!}
=
\frac{2^{k-2}}{(k-2)!}.
\tag{28}
\]

Normalized by `(28)`, the split variable `q` is exactly `Binomial(k-2,1/2)`. When `(k-2)/(2L)->beta>0`, it is concentrated in a window `O(sqrt(L))` around `(k-2)/2`. Hence

\[
a,c\longrightarrow\beta
\tag{29}
\]

throughout the mass-carrying splits. The factor in `(27)` is continuous there. Standard Sathe–Selberg upper bounds make the exponentially small binomial tails negligible, including the edge splits with one degree sublinear in `L`.

For each fixed `b`, summing `(27)` therefore yields

\[
\sim
J\frac{(N/b)^2}{(\log N)^2}
\frac{(2L)^{k-2}}{(k-2)!}
\frac{H_b(1,1;\beta,\beta)}{\Gamma(1+\beta)^2}.
\tag{30}
\]

The `b`-tail is handled without any uniform-in-`b` asymptotic: first sum over fixed `b\le B`, then use the unrestricted proportional Sathe–Selberg upper bound to dominate the normalized remainder by a convergent tail `\sum_{b>B} C_K^{\omega(b)}/b^2`; the crude contribution from `b>\sqrt N` is `O(N^{3/2+o(1)})`. Sending `B\to\infty` justifies the passage from `(30)` to the Euler product below.

## 5. The common-factor sum collapses to one positive Euler product

Using `(21)` at `u=v=beta`, the common-factor sum is

\[
\begin{aligned}
&\sum_{\substack{b\ge1\\b\ \mathrm{squarefree}}}
\frac1{b^2}H_b(1,1;\beta,\beta)\\
&\quad=
H_0(\beta,\beta)
\prod_p\left(1+\frac1{p^2(1+2\beta/p)}\right).
\end{aligned}
\tag{31}
\]

Prime by prime,

\[
\left(1+\frac{2\beta}{p}\right)
\left(1+\frac1{p^2(1+2\beta/p)}\right)
=
1+\frac{2\beta}{p}+\frac1{p^2}.
\tag{32}
\]

Combining `(22)`, `(31)`, and `(32)` gives exactly the Euler product in `(6)`. Its logarithm has no `1/p` term, so it converges locally uniformly; positivity is termwise for every real `beta>0`. This proves `(5)`--`(7)`.

At `beta->0`,

\[
\mathcal A(\beta)\longrightarrow
\prod_p(1+p^{-2})
=\frac{15}{\pi^2},
\tag{33}
\]

so `(5)` recovers the coefficient of `MC-105`/`MC-106`. At `beta=1`, `(32)` becomes

\[
(1+2/p+1/p^2)(1-1/p)^2=(1-p^{-2})^2,
\tag{34}
\]

which proves `(10)`.

## 6. The `2 log log N` turning scale and the last-shell prefix law

The correction `mathcal A(beta)` is smooth and nonzero on compact positive intervals. Dividing `(5)` at consecutive degrees therefore gives `(8)`. On the exponential scale, Stirling's formula gives, for `k~2 beta L`,

\[
C_{k,N}
=
N^2(\log N)^{-2+2\beta(1-\log\beta)+o(1)}.
\tag{35}
\]

The exponent `2 beta(1-log beta)` has its unique maximum at `beta=1`; this is the turning scale `(9)`. At `beta=1`, Stirling together with `(10)` gives `(11)`.

Now fix `0<beta<1` and `K` as in `(13)`. For every fixed `r>=0`, repeated use of `(8)` gives

\[
\frac{C_{K-r,N}}{C_{K,N}}\longrightarrow\beta^r.
\tag{36}
\]

Uniformly on any compact range ending at this `beta`, the backward ratios are eventually bounded by some number strictly below `1`. The earlier proportional degrees are therefore a geometric tail relative to `C_K`; the sub-proportional range is smaller still by `MC-106` and the large-deviation profile. Taking first finitely many backward shells and then letting their number tend to infinity yields

\[
\frac{(-1)^K}{C_{K,N}}
\sum_{k=2}^{K}(-1)^kC_{k,N}
\longrightarrow
\sum_{r=0}^{\infty}(-\beta)^r
=\frac1{1+\beta},
\tag{37}
\]

which is `(13)`. Equation `(14)` follows by subtracting this prefix, together with `C_0-C_1`, from the exact endpoint `(12)`.

The argument deliberately stops at `beta=1`. At the turning scale the ratio tends to one, so no single shell dominates the alternating prefix; cancellation can spread over a growing central band. That is a different problem from the positive-shell asymptotic itself.

## 7. Prior art and novelty boundary

The analytic engine is classical. Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics 203, AMS (2019), Theorem 16.2, proves Sathe–Selberg uniformly for `1<=k<=C log log x`; the square-free finite-prime-exclusion specialization used in `(R2)`--`(R3)` follows from the corresponding square-free Euler product. The author-approved preliminary version is available at `https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf`; the theorem appears in Chapter 16 and cites Sathe (1953) and Selberg (1954).

Régis de la Bretèche, *Estimation de sommes multiples de fonctions arithmétiques*, Compositio Mathematica 128 (2001), 261–298, DOI `10.1023/A:1011803816545`, remains relevant adjacent multivariable prior art, but it is **not** load-bearing for `(25)`: exact coprimality inversion reduces the needed rectangle asymptotic to a summable superposition of one-variable counts.

A targeted search for Sathe–Selberg formulas on coprime pairs, square-free pair counts, sawtooth-weighted exact-prime-factor sums, Möbius Hamming shells, and symmetric-difference prime-factor distance did not identify `(5)`--`(14)` as a standard named theorem. **No novelty claim is made.** The durable content is the source-specific specialization: the exact pair kernel from the Möbius Hamming deformation has a positive proportional-degree profile with the explicit correction `(6)`, and this moves the already-established radial obstruction from `o(log log N)` to the turning scale `2 log log N`.

## 8. Boundaries and falsification tests

- The load-bearing uniformity in `(25)` is now reduced to the one-variable square-free Sathe–Selberg estimate plus the dominated `q`-sum `(R1)`--`(R7)`. A future audit should attack the compact-parameter one-variable upper bound, the `q>x^{1/2}` normalization, or the fixed-truncation `b` tail rather than relying on a generic two-variable Cauchy analogy.
- The coprimality constraint is **not negligible** at proportional degree. It is retained exactly in `(R1)` and is responsible, together with the common factor `b`, for the Euler correction `(6)`. Dropping it would give the wrong constant.
- The source kernel is bounded but discontinuous. The rectangle law `(25)`, the zero-area hyperbola discontinuities, and the `O(delta)` axis mass are the required justification for replacing it by the integral `J`; pointwise equidistribution language alone is insufficient.
- Formula `(5)` is a fixed-proportional-scale statement. It does not by itself give the fine local profile when `k-2L=o(L)`, although it identifies the unique turning scale and the positive arithmetic factor there.
- Equation `(13)` requires `beta<1`. At `beta=1`, last-shell domination fails and no conclusion about the precise width or mechanism of the central alternating cancellation is made.
- Positivity of every fixed-proportional shell does not imply positivity for degrees growing faster than `log log N`, nor does it imply a Poisson law for the exact source coefficients.
- The endpoint estimate `(12)` is only the existing unconditional bound. No zero-free region stronger than the known input, no RH-equivalent continuation of `1/zeta`, and no estimate for `M(x)` is imported.

The decisive radial continuation is now finer than the one stated in `MC-106`: resolve the **central parity-cancellation window around `k=2 log log N`**. A useful next result would determine the profile on a moving `o(L)` window around the turning point and test whether the exact arithmetic factor plus the external parity `(-1)^k` yields only a fixed power of `log N` cancellation or contains an additional source-specific relation capable of matching the super-logarithmic endpoint saving. A generic unsigned Poisson approximation is not enough, because the issue is precisely the parity-sensitive cancellation of the actual source coefficients.

## Consequence for the research line

The radial Hamming branch is now sharply localized. Fixed-degree, sub-log-logarithmic, and every fixed proportional degree below the turning point are not plausible endpoint approximations: their positive shell mass survives and must be cancelled by omitted higher degrees. The first radial regime that can genuinely host the endpoint cancellation is no longer an unspecified `Theta(log log N)` range but the turning zone at `2 log log N`, where shell ratios approach one.

This does not solve the surviving Mind requirement for a source-specific signed relation. It does, however, remove a large ambiguity in where such a relation could live: any purely radial relation that explains the endpoint must couple the central `2 log log N` scale (or use non-radial information that bypasses shell truncation altogether).