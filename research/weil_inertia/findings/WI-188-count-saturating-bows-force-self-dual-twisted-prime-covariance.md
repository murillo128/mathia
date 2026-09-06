# WI-188 — count-saturating bows force a self-dual twisted-prime covariance problem

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-187 left one natural short-height escape deliberately open: reopen the unconditional Montgomery proof and use the special von-Mangoldt coefficients rather than the arbitrary-coefficient Montgomery--Vaughan mean-value theorem. The source expansion below identifies exactly what that escape requires. At the source-compatible count-saturating Maynard--Pratt bow, WI-184 forces the reciprocal frequency to `alpha=1/2`, hence the prime-side Dirichlet length is `x=sqrt(T)`. A height-localized second moment at that length becomes a twisted shifted-von-Mangoldt covariance over shifts `h \lesssim x/H`.

Two weak ways of trying to control that covariance can be closed. First, prime sparsity used only through positive/absolute prime-pair bounds saves at most a logarithm relative to the arbitrary-coefficient mean-value theorem and still misses the bow scale by the polynomial factor `T^(1/2-epsilon)`. This remains true even if one grants Hardy--Littlewood-scale **untwisted** pair counts: triangle inequality still gives an off-diagonal scale `O(x)`, whereas the diagonal is only `asymp H log x`. Second, the height twist is not automatically nonstationary on the integer lattice. At `x=sqrt(T)` its phase derivative sweeps an interval containing `Theta(h)` integers for shift `h`, so a naive first-derivative/Kusmin--Landau argument has `Theta(h)` lattice aliases to cross.

Thus the remaining arithmetic escape is much more specific than “exploit prime coefficients”: it must prove cancellation in a **self-dual, chirped, growing-shift von-Mangoldt covariance**, or use a genuinely different source coupling. No unconditional simple-critical-zero percentage changes here.

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

in the range relevant here, producing the `T log x` term of Montgomery's theorem. The exact constants are not needed for the resolution argument below; only the established logarithmic diagonal scale is used.

Now localize around a height `U\asymp T`. Let `W` be a real even integrable localizer and use the Fourier convention

\[
\widehat W(\xi)=\int_{\mathbb R}W(u)e^{iu\xi}\,du.
\tag{3}
\]

For `H>0`, direct expansion and the change of variables `t=U+Hu` give the exact identity

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

because `H log(1+h/m)=O(1)` there. Pairing `h` and `-h`, the off-diagonal on this block has the schematic but normalization-exact scale

\[
\mathcal O_W
=\frac{2H}{x}\operatorname{Re}
\sum_{1\le h\lesssim K}
\sum_{m\asymp x}
\Lambda(m)\Lambda(m+h)\,w_{x,H}(m,h)
 e^{\,iU\log(1+h/m)},
\tag{7}
\]

where `w_{x,H}` is a bounded smooth weight containing the two `q_x` factors, the `sqrt{x^2/(m(m+h))}` normalization, the dyadic cutoff, and `\widehat W(H log(1+h/m))`. Formula (7), rather than an arbitrary-coefficient mean-value theorem, is the arithmetic object that a prime-specific local bow argument has to control.

## 2. Positive prime-pair information still misses the required scale

Suppose one refuses to use the oscillation in (7) and estimates each shifted correlation by absolute values. On `m\asymp x`, the standard dimension-two Selberg upper-bound sieve gives, uniformly for `1\le h=o(x)`, the prime-pair scale

\[
\sum_{m\asymp x}\Lambda(m)\Lambda(m+h)
\ll x\,\mathfrak S_2(h)+O(\sqrt x\log^2x),
\tag{8}
\]

where the local factor may be taken, up to an absolute constant and the parity convention, as

\[
\mathfrak S_2(h)
\ll
\prod_{\substack{p\mid h\\p>2}}
\frac{p-1}{p-2}.
\tag{9}
\]

The prime-power remainder in (8) is harmless for the conclusion. No conjectural asymptotic is being used.

The average local factor costs no growing power or logarithm. Indeed

\[
\prod_{\substack{p\mid h\\p>2}}
\left(1+\frac1{p-2}\right)
=
\sum_{d\mid h}g(d),
\qquad
g(d):=\mathbf1_{d\ {m odd\ squarefree}}
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

The Euler product converges absolutely. Therefore applying triangle inequality to (7) and then only positive prime-pair information gives

\[
\boxed{
|\mathcal O_W|\ll x
}
\tag{12}
\]

(up to harmless localizer constants), while the desired diagonal is only `asymp H log x`. Such an argument can certify diagonal dominance only in the regime

\[
\boxed{x=o(H\log x).}
\tag{13}
\]

This is already stronger by one logarithm than WI-187's arbitrary-coefficient Montgomery--Vaughan resolution condition `x=o(H)`: prime sparsity is real information. But it does not change the exponent barrier.

The point is not an artifact of a loose Selberg-sieve constant. Even granting the Hardy--Littlewood-sized untwisted correlation

\[
\sum_{m\asymp x}\Lambda(m)\Lambda(m+h)
\sim x\mathfrak S_2(h)
\tag{14}
\]

would leave the same `O(x)` result after absolute summation over `h\lesssim x/H`. Thus **better positive pair counting alone cannot solve the localized bow problem**. One must exploit cancellation in the complex phase, cancellation between shifts/localizer weights, or a different source identity before absolute values are taken.

## 3. The count-saturating bow lands exactly at square-root length

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

## 4. The height chirp has linearly many lattice aliases per shift

Equation (7) contains potentially useful oscillation. It is important, however, not to treat the height translation as automatically nonstationary. Write the phase in cycles as

\[
f_h(m):=\frac{U}{2\pi}\log\left(1+\frac hm\right).
\tag{21}
\]

Then

\[
\boxed{
f_h'(m)=-\frac{Uh}{2\pi m(m+h)}.}
\tag{22}
\]

Take `U=theta T` with `theta` bounded above and below by positive constants, and take the count-saturating `x=sqrt(T)(1+o(1))`. Since every relevant shift in (19) satisfies `h=o(x)`, on `m\in[x,2x]`

\[
|f_h'(x)|
=\frac{\theta}{2\pi}h\,(1+o(1)),
\qquad
|f_h'(2x)|
=\frac{\theta}{8\pi}h\,(1+o(1)).
\tag{23}
\]

Hence the monotone derivative sweeps an interval of length

\[
\boxed{
\left(\frac{3\theta}{8\pi}+o(1)\right)h.
}
\tag{24}
\]

For large `h`, that interval contains `Theta(h)` integers. For every integer `k` in the interior there is a unique point `m_k\in[x,2x]` with

\[
f_h'(m_k)=-k.
\tag{25}
\]

These are precisely the lattice resonances encountered after Poisson summation / a van-der-Corput `B` process. Therefore the simple first-derivative principle “the phase changes rapidly, so the sum cancels” is unavailable uniformly: the square-root length forced by the zero-side count is also a self-dual arithmetic scale with linearly many stationary aliases for a shift of size `h`.

This does **not** prove that the twisted prime correlation is large. A refined Poisson, exponent-pair, Vaughan/Heath-Brown identity, or bilinear argument may exploit the stationary structure. The exact conclusion is narrower: the height chirp is genuinely an arithmetic oscillation problem, not a free consequence of translating the local mean square to height `U\asymp T`.

## 5. Exact cancellation target for a viable prime-specific escape

Define the raw twisted shifted-prime sum on the central block by

\[
S_h(U;x)
:=\sum_{m\asymp x}
\Lambda(m)\Lambda(m+h)\,\widetilde w_x(m,h)
 e^{\,iU\log(1+h/m)},
\tag{26}
\]

where `\widetilde w_x` contains only bounded source/dyadic weights. With the localizer factor retained, (7) shows that a sufficient source-level replacement for the black-box mean-value step is a bound of the shape

\[
\boxed{
\sum_{h\lesssim x/H}
\widehat W\!\left(H\log(1+h/m)\right)S_h(U;x)
=o(x\log x),
}
\tag{27}
\]

with the `m`-dependence of the Fourier weight understood inside the double sum. Equivalently, the normalized off-diagonal in (7) must be `o(H log x)`.

At the count-saturating bow this means controlling a family of shifts out to

\[
h\lesssim T^{1/2-\epsilon+o(1)}
\tag{28}
\]

at the self-dual length `x=sqrt(T)`, with the nonlinear height chirp (21). This is the concrete arithmetic target left open by WI-187. A theorem only about untwisted positive correlations `sum Lambda(m)Lambda(m+h)` does not meet (27); neither does a generic short-interval mean-value theorem whose error is propagated absolutely.

## 6. Prior art and evidence boundary

The local expansion (4) is elementary Fourier algebra applied to the prime polynomial in the current BGSTB proof; equations (20) and (24) are new exact deductions inside this research line. The arithmetic ingredients and the depth of the remaining target have substantial prior art:

- H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *J. London Math. Soc.* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, gives the arbitrary-coefficient Dirichlet-polynomial mean-value theorem used in WI-187. The present finding reopens the coefficients instead of invoking that theorem as a black box.
- The classical dimension-two Selberg upper-bound sieve gives the prime-pair bound used in (8). Modern Selberg-sieve treatments, including DHJ Polymath, **Variants of the Selberg sieve, and bounded intervals containing many primes**, *Research in the Mathematical Sciences* 1 (2014), 12, DOI `10.1186/s40687-014-0012-7`, explicitly use Selberg upper-bound sieves for prime-tuple correlations. Equation (11) supplies the only average-in-`h` fact needed here directly.
- D. A. Goldston and H. L. Montgomery, **Pair correlation of zeros and primes in short intervals**, in *Analytic Number Theory and Diophantine Problems*, Progress in Mathematics 70 (1987), 183--203, establishes under RH the classical equivalence between strong pair correlation and prime variance in short intervals. The current BGSTB paper itself cites this source for its load-bearing `A_2` mean square.
- Alessandro Languasco and Alberto Perelli, **Pair Correlation of Zeros, Primes in Short Intervals and Exponential Sums over Primes**, *Journal of Number Theory* 84 (2000), 292--304, DOI `10.1006/jnth.2000.2511`, proves under RH an equivalence, in a substantial range, between pair correlation and a truncated mean-square asymptotic for exponential sums over primes. This is direct prior art that prime exponential mean squares in this regime encode pair-correlation-level information rather than being a cosmetic refinement of Montgomery--Vaughan.
- Brian Conrey and Jonathan Keating's series **Moments of zeta and correlations of divisor-sums**, in particular parts IV--V (2016--2019), develops the general shifted-convolution/Poisson architecture for long Dirichlet-polynomial mean squares with divisor coefficients. It reinforces that the stationary aliases in Section 4 are a standard doorway to a nontrivial shifted-convolution problem, not an automatic cancellation estimate.
- Larry Guth and James Maynard, **New large value estimates for Dirichlet polynomials**, *Annals of Mathematics* 203 (2026), 623--675, gives major new global large-value estimates for Dirichlet polynomials and consequences for primes in short intervals. A targeted audit found no theorem there, or in the other sources checked in this pass, that gives the deterministic height-localized, twisted `Lambda(m)Lambda(m+h)` covariance (27) at `H=T^epsilon/log T` for arbitrary fixed `epsilon<1/2`.

No priority claim is made from this bounded search. In particular, (27) may be approachable by existing exponential-sum technology after a more delicate decomposition. The established result here is the exact reduction and the two closed weak routes: positive/absolute prime-pair information has the wrong exponent, and simple nonstationary-phase reasoning is invalidated by `Theta(h)` lattice aliases.

## 7. Research consequence

WI-187's broad escape “exploit the specific prime coefficients” can now be split sharply. **Prime sparsity without phase cancellation is closed**: even Hardy--Littlewood-scale positive pair information plus triangle inequality leaves an `O(x)` off-diagonal, polynomially larger than the bow-local diagonal. **Naive height oscillation is also closed**: the zero-side count forces `alpha=1/2`, putting the prime polynomial at square-root length where each growing shift crosses linearly many discrete stationary frequencies.

The next source-level attempt should therefore target (27) explicitly, most plausibly by a Poisson/`B`-process followed by arithmetic control of the dual stationary sums, a Vaughan/Heath-Brown decomposition that can average the chirped growing shifts, or a bow--reservoir observable whose cross terms carry a sign/inertia charge and avoid isolating this local prime square. A result of that kind would be genuinely new arithmetic information relative to WI-187 and could legitimately reopen the bow route. Merely replacing Montgomery--Vaughan by a sieve count, or citing rapid phase variation without resolving its lattice aliases, is now a closed weak route.