# WI-188 — count-saturating bows force a self-dual twisted-prime covariance problem

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-187 left one natural short-height escape deliberately open: reopen the unconditional Montgomery proof and use the special von-Mangoldt coefficients rather than the arbitrary-coefficient Montgomery--Vaughan mean-value theorem. The source expansion below identifies exactly what that escape requires. At a source-compatible count-saturating Maynard--Pratt bow, WI-184 forces the reciprocal frequency to

\[
\alpha_*=\frac12+o(1),
\qquad
x_*=T^{\alpha_*}=T^{1/2+o(1)},
\]

so the prime polynomial is self-dual only at exponent scale; no multiplicative normalization `x_*=sqrt(T)(1+o(1))` is assumed. A height-localized second moment at that length becomes a twisted shifted-von-Mangoldt covariance over shifts `h \lesssim x_*/H`.

Two weak ways of trying to control that covariance can be closed. First, prime sparsity used only through positive/absolute prime-pair bounds saves at most a logarithm relative to the arbitrary-coefficient mean-value theorem and still misses the bow scale by a polynomial factor `T^(1/2-epsilon+o(1))`. This remains true even if one grants Hardy--Littlewood-scale **untwisted** pair counts: triangle inequality still gives an off-diagonal scale `O(x_*)`, whereas the diagonal is only `asymp H log x_*`. Second, the height twist is not automatically nonstationary on the integer lattice. The correct derivative-sweep scale for a shift `h` is `(U/x_*^2)h`, not `Theta(h)` without an additional saturation rate. Nevertheless, at the top of the required shift range `K=x_*/H`, the sweep is

\[
\frac{U}{x_*^2}K=\frac{U}{Hx_*}
=T^{1/2-\epsilon+o(1)}\log T\to\infty,
\]

so a naive uniform first-derivative/Kusmin--Landau dismissal of the local off-diagonal still fails.

Thus the remaining arithmetic escape is much more specific than “exploit prime coefficients”: it must prove cancellation in a **chirped, growing-shift von-Mangoldt covariance at exponent-level self-dual length**, or use a genuinely different source coupling. No unconditional simple-critical-zero percentage changes here.

## 1. Reopen the current unconditional Montgomery square

The current primary source is Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*, arXiv:2501.14545v3 (revised 1 September 2026). Its corrected unconditional Montgomery theorem is the pointwise form-factor input used in WI-186. In the proof, the load-bearing prime Dirichlet polynomial is

\[
A_2(x,t)
=-\sum_{n\ge1} a_x(n)n^{-it},
\qquad
a_x(n):=
\frac{\Lambda(n)}{\sqrt n}\,q_x(n),
\qquad
q_x(n):=\min\!\left(\frac n x,\frac x n\right).
\tag{1}
\]

The global argument evaluates its second moment at scale `T`; the diagonal has

\[
\sum_n a_x(n)^2\asymp \log x
\tag{2}
\]

in the range relevant here, producing the `T log x` term of Montgomery's theorem. Only this established logarithmic diagonal scale is needed below.

Now localize around a height `U\asymp T`. Let `W` be a real even integrable localizer and use

\[
\widehat W(\xi)=\int_{\mathbb R}W(u)e^{iu\xi}\,du.
\tag{3}
\]

For `H>0`, direct expansion and `t=U+Hu` give the exact identity

\[
\boxed{
\begin{aligned}
\mathcal M_W(U,H;x)
&:=\int_{\mathbb R}W\!\left(\frac{t-U}{H}\right)|A_2(x,t)|^2\,dt\\
&=H\sum_{m,n\ge1}a_x(m)a_x(n)
 e^{\,iU\log(n/m)}
 \widehat W\!\left(H\log\frac n m\right).
\end{aligned}}
\tag{4}
\]

The diagonal is

\[
\mathcal D_W
=H\widehat W(0)\sum_n a_x(n)^2
\asymp H\log x.
\tag{5}
\]

For a localizer whose Fourier transform is supported, or effectively supported, on a fixed bounded interval, the central dyadic block `m,n\asymp x` only couples

\[
n=m+h,
\qquad
|h|\lesssim K:=\frac{x}{H},
\tag{6}
\]

because `H log(1+h/m)=O(1)` there. Pairing `h` and `-h`, the off-diagonal on this block has the normalization-exact scale

\[
\mathcal O_W
=\frac{2H}{x}\operatorname{Re}
\sum_{1\le h\lesssim K}
\sum_{m\asymp x}
\Lambda(m)\Lambda(m+h)\,w_{x,H}(m,h)
 e^{\,iU\log(1+h/m)},
\tag{7}
\]

where `w_{x,H}` is a bounded smooth weight containing the two `q_x` factors, the `sqrt{x^2/(m(m+h))}` normalization, the dyadic cutoff, and `\widehat W(H log(1+h/m))`. Formula (7), rather than an arbitrary-coefficient mean-value theorem, is the arithmetic object that a prime-specific local bow argument must control.

## 2. Positive prime-pair information still misses the required scale

Suppose one refuses to use the oscillation in (7) and estimates shifted correlations by absolute values. On `m\asymp x`, the standard dimension-two Selberg upper-bound sieve gives, uniformly for `1\le h=o(x)`,

\[
\sum_{m\asymp x}\Lambda(m)\Lambda(m+h)
\ll x\,\mathfrak S_2(h)+O(\sqrt x\log^2x),
\tag{8}
\]

with, up to an absolute constant and parity convention,

\[
\mathfrak S_2(h)
\ll
\prod_{\substack{p\mid h\\p>2}}
\frac{p-1}{p-2}.
\tag{9}
\]

The prime-power remainder is harmless here. The average local factor costs no growing power or logarithm. Indeed

\[
\prod_{\substack{p\mid h\\p>2}}
\left(1+\frac1{p-2}\right)
=
\sum_{d\mid h}g(d),
\qquad
g(d):=\mathbf1_{d\ {\rm odd\ squarefree}}
\prod_{p\mid d}\frac1{p-2},
\tag{10}
\]

so

\[
\sum_{h\le K}\mathfrak S_2(h)
\ll
K\sum_{d\ge1}\frac{g(d)}d
=
K\prod_{p>2}\left(1+\frac1{p(p-2)}\right)
\ll K.
\tag{11}
\]

Therefore triangle inequality in (7), followed only by positive prime-pair information, gives

\[
\boxed{|\mathcal O_W|\ll x,}
\tag{12}
\]

while the desired diagonal is `asymp H log x`. Such an argument can certify diagonal dominance only in the regime

\[
\boxed{x=o(H\log x).}
\tag{13}
\]

This improves WI-187's arbitrary-coefficient Montgomery--Vaughan condition `x=o(H)` by one logarithm, but not in exponent. Even granting a Hardy--Littlewood-sized untwisted correlation

\[
\sum_{m\asymp x}\Lambda(m)\Lambda(m+h)
\sim x\mathfrak S_2(h)
\tag{14}
\]

leaves the same `O(x)` result after absolute summation over `h\lesssim x/H`. Thus **better positive pair counting alone cannot solve the localized bow problem**. One must exploit cancellation in the complex phase, cancellation between shifts/localizer weights, or a different source identity before absolute values are taken.

## 3. Count saturation gives square-root length only at exponent scale

WI-184 proves that a source-compatible mirror-closed bow with ordinate step `c/log T` must satisfy

\[
c\ge4\pi-o(1),
\tag{15}
\]

and its first reciprocal frequency is

\[
\alpha_*=\frac{2\pi}{c}.
\tag{16}
\]

At count saturation, `c=4pi+o(1)`, hence

\[
\boxed{
\alpha_*=\frac12+o(1),
\qquad
x_*=T^{\alpha_*}=T^{1/2+o(1)}.
}
\tag{17}
\]

This does **not** imply `x_*=sqrt(T)(1+o(1))`; that stronger normalization would require `(alpha_*-1/2)log T -> 0`, a rate unavailable from WI-184.

For the Maynard--Pratt scale `m=T^epsilon` with fixed `0<epsilon<1/2`, the bow height is

\[
H_{\rm bow}\asymp\frac{T^\epsilon}{\log T}.
\tag{18}
\]

Consequently

\[
K=\frac{x_*}{H_{\rm bow}}
=T^{1/2-\epsilon+o(1)}\log T
\tag{19}
\]

and the ratio between the absolute prime-pair scale (12) and the diagonal (5) is

\[
\boxed{
\frac{x_*}{H_{\rm bow}\log x_*}
=T^{1/2-\epsilon+o(1)}\to\infty.
}
\tag{20}
\]

Thus reopening the source and inserting prime sparsity buys a logarithm compared with WI-187, but the count-saturating bow still misses the resulting resolution gate by a polynomial factor for every fixed `epsilon<1/2`.

## 4. The height chirp has a rate-free lattice-alias obstruction

Equation (7) contains potentially useful oscillation. It is important not to treat the height translation as automatically nonstationary. Write the phase in cycles as

\[
f_h(m):=\frac{U}{2\pi}\log\left(1+\frac hm\right),
\tag{21}
\]

so

\[
\boxed{
f_h'(m)=-\frac{Uh}{2\pi m(m+h)}.}
\tag{22}
\]

Take `U=theta T` with `theta` bounded above and below by positive constants and retain the actual count-saturating length `x_*=T^{1/2+o(1)}`. Define

\[
\rho_T:=\frac{U}{x_*^2}.
\tag{23}
\]

Then `rho_T=T^{o(1)}` up to bounded factors, but it need not converge to a nonzero constant. Since every relevant shift satisfies `h=o(x_*)`, uniformly on `m\in[x_*,2x_*]`,

\[
|f_h'(x_*)|
=\frac{\rho_T h}{2\pi}(1+o(1)),
\qquad
|f_h'(2x_*)|
=\frac{\rho_T h}{8\pi}(1+o(1)).
\tag{24}
\]

Hence the monotone derivative sweeps an interval of length

\[
\boxed{
\left(\frac{3}{8\pi}+o(1)\right)\rho_T h.
}
\tag{25}
\]

The number of integer derivative levels crossed is therefore `O(1+rho_T h)` in general and is asymptotic to a positive constant multiple of `rho_T h` once `rho_T h->infinity`. For every integer `k` in the derivative image there is a unique stationary point `m_k\in[x_*,2x_*]` satisfying

\[
f_h'(m_k)=-k.
\tag{26}
\]

These are the lattice resonances encountered after Poisson summation / a van-der-Corput `B` process.

The missing saturation rate does not restore a uniform first-derivative argument, because the required shift family extends to `K=x_*/H_bow`. At that upper scale,

\[
\boxed{
\rho_T K
=\frac{U}{H_{\rm bow}x_*}
=T^{1/2-\epsilon+o(1)}\log T\to\infty.
}
\tag{27}
\]

Thus for shifts `h\asymp K` the derivative interval crosses `T^{1/2-epsilon+o(1)}` integer levels. Even if `rho_T->0`, the top part of the required growing-shift range contains arbitrarily many lattice resonances. A uniform first-derivative/Kusmin--Landau dismissal of the entire off-diagonal is therefore unavailable.

This does **not** prove that the twisted prime correlation is large. A refined Poisson, exponent-pair, Vaughan/Heath-Brown identity, bilinear argument, or cancellation across stationary frequencies may exploit the structure. The exact conclusion is narrower: the height chirp is genuinely an arithmetic oscillation problem, not a free consequence of translating the local mean square to height `U\asymp T`.

## 5. Exact cancellation target for a viable prime-specific escape

Define the raw twisted shifted-prime sum on the central block by

\[
S_h(U;x)
:=\sum_{m\asymp x}
\Lambda(m)\Lambda(m+h)\,\widetilde w_x(m,h)
 e^{\,iU\log(1+h/m)},
\tag{28}
\]

where `\widetilde w_x` contains only bounded source/dyadic weights. With the localizer factor retained, (7) shows that a sufficient source-level replacement for the black-box mean-value step is a bound of the shape

\[
\boxed{
\sum_{h\lesssim x/H}
\widehat W\!\left(H\log(1+h/m)\right)S_h(U;x)
=o(x\log x),
}
\tag{29}
\]

with the `m`-dependence of the Fourier weight understood inside the double sum. Equivalently, the normalized off-diagonal in (7) must be `o(H log x)`.

At the count-saturating bow this means controlling a family of shifts out to

\[
h\lesssim T^{1/2-\epsilon+o(1)}\log T
\tag{30}
\]

at length `x_*=T^{1/2+o(1)}`, with the nonlinear height chirp (21). A theorem only about untwisted positive correlations `sum Lambda(m)Lambda(m+h)` does not meet (29); neither does a generic short-interval mean-value theorem whose error is propagated absolutely.

WI-189 strengthens the corrected alias bookkeeping: after summing the full localized shift family, the aggregate number of `B`-process derivative aliases has main scale `U/H^2`, independent of the uncertain reciprocal length. That later result is consistent with, but not required for, the present reduction.

## 6. Prior art and evidence boundary

The local expansion (4) is elementary Fourier algebra applied to the prime polynomial in the current BGSTB proof; equations (20), (25), and (27) are exact deductions inside this research line. The arithmetic ingredients and the depth of the remaining target have substantial prior art:

- H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *J. London Math. Soc.* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, gives the arbitrary-coefficient Dirichlet-polynomial mean-value theorem used in WI-187. The present finding reopens the coefficients instead of invoking that theorem as a black box.
- The classical dimension-two Selberg upper-bound sieve gives the prime-pair bound used in (8). Modern Selberg-sieve treatments, including DHJ Polymath, **Variants of the Selberg sieve, and bounded intervals containing many primes**, *Research in the Mathematical Sciences* 1 (2014), 12, DOI `10.1186/s40687-014-0012-7`, explicitly use Selberg upper-bound sieves for prime-tuple correlations. Equation (11) supplies the only average-in-`h` fact needed here directly.
- D. A. Goldston and H. L. Montgomery, **Pair correlation of zeros and primes in short intervals**, in *Analytic Number Theory and Diophantine Problems*, Progress in Mathematics 70 (1987), 183--203, establishes under RH the classical equivalence between strong pair correlation and prime variance in short intervals. The current BGSTB paper itself cites this source for its load-bearing `A_2` mean square.
- Alessandro Languasco and Alberto Perelli, **Pair Correlation of Zeros, Primes in Short Intervals and Exponential Sums over Primes**, *Journal of Number Theory* 84 (2000), 292--304, DOI `10.1006/jnth.2000.2511`, proves under RH an equivalence, in a substantial range, between pair correlation and a truncated mean-square asymptotic for exponential sums over primes. This is direct prior art that prime exponential mean squares in this regime encode pair-correlation-level information rather than being a cosmetic refinement of Montgomery--Vaughan.
- Brian Conrey and Jonathan Keating's series **Moments of zeta and correlations of divisor-sums**, in particular parts IV--V (2016--2019), develops the general shifted-convolution/Poisson architecture for long Dirichlet-polynomial mean squares with divisor coefficients. It reinforces that the stationary aliases in Section 4 are a standard doorway to a nontrivial shifted-convolution problem, not an automatic cancellation estimate.
- Larry Guth and James Maynard, **New large value estimates for Dirichlet polynomials**, *Annals of Mathematics* 203 (2026), 623--675, gives major new global large-value estimates for Dirichlet polynomials and consequences for primes in short intervals. A targeted audit found no theorem there, or in the other sources checked in this pass, that gives the deterministic height-localized, twisted `Lambda(m)Lambda(m+h)` covariance (29) at `H=T^epsilon/log T` for arbitrary fixed `epsilon<1/2`.

No priority claim is made from this bounded search. In particular, (29) may be approachable by existing exponential-sum technology after a more delicate decomposition. The established result here is the exact reduction and two closed weak routes: positive/absolute prime-pair information has the wrong exponent, and simple nonstationary-phase reasoning fails uniformly because the required shift range reaches arbitrarily large lattice-alias counts even without a multiplicative `sqrt(T)` normalization.

## 7. Research consequence

WI-187's broad escape “exploit the specific prime coefficients” can now be split sharply. **Prime sparsity without phase cancellation is closed**: even Hardy--Littlewood-scale positive pair information plus triangle inequality leaves an `O(x)` off-diagonal, polynomially larger than the bow-local diagonal. **Naive height oscillation is also closed**: count saturation forces `alpha=1/2+o(1)`, and although the exact per-shift alias scale is `(U/x^2)h` rather than `Theta(h)`, the top of the required local shift family has polynomially many stationary lattice frequencies.

The next source-level attempt should therefore target (29) explicitly, most plausibly by a Poisson/`B`-process followed by arithmetic control of the dual stationary sums, a Vaughan/Heath-Brown decomposition that can average the chirped growing shifts, or a bow--reservoir observable whose cross terms carry a sign/inertia charge and avoid isolating this local prime square. A result of that kind would be genuinely new arithmetic information relative to WI-187 and could legitimately reopen the bow route. Merely replacing Montgomery--Vaughan by a sieve count, or citing rapid phase variation without resolving its lattice aliases, is a closed weak route.