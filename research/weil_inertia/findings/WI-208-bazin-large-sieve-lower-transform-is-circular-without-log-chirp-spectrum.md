# WI-208 — Bazin's large-sieve lower transform is circular without new log-chirp spectrum

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

A recent lower-bound theorem of Péa Bazin gives a genuinely relevant new lens on the source-fixed Gallagher problem left by WI-195--WI-207, but it does not black-box close that problem. Bazin's general Theorem 8 applies to an arbitrary finitely supported coefficient sequence and lower-bounds a sliding short-interval `L^2` norm by samples of the global additive Fourier transform at Farey points. Applied to the distinguished logarithmically chirped von-Mangoldt coefficients, it converts the bow variance into a **rational log-chirp spectral-energy problem**.

There is, however, an exact obstruction to obtaining the required bow lower bound from the large-sieve transform alone. Because the target short sum is unchanged by an arbitrary linear demodulation, average Bazin's Farey-sample inequality over that demodulation parameter. Parseval then identifies the averaged spectral term **exactly with the original short-interval variance**. The resulting inequality is only

\[
V\ge \frac{M_Q}{N+K+Q^2}\,V,
\qquad
M_Q:=\sum_{q\le Q}\varphi(q),
\qquad Q\le \sqrt N,
\]

up to the harmless integer-floor convention in Bazin's displayed denominator. Since `M_Q/(N+K+Q^2)<1` (indeed at most `1/2` by an elementary bound), this is circular and gives no positive diagonal-scale information.

Bazin obtains arithmetic content for the unchirped prime sequence by adding a separate Bombieri--Vinogradov-type major-arc theorem of Liu--Zhan. That input estimates `sum Lambda(n)e((a/q+lambda)n)` by its classical rational major-arc main term. For the bow coefficient `Lambda(n)n^{-iU}` (and still more for `(Lambda-Lambda^sharp)(n)n^{-iU}`), the corresponding Farey samples are instead

\[
B_U(\beta)=\sum_{n\le N} b_U(n)e(\beta n),
\qquad
b_U(n)=(\Lambda(n)-\Lambda^\sharp(n))n^{-iU}
\]

or the analogous weighted source coefficient. No theorem located in the bounded prior-art audit supplies the required pointwise/lower-energy control of this rationally shifted logarithmic chirp at the self-dual bow scale. Thus Bazin materially redirects the live source problem, but the missing module remains genuinely arithmetic rather than large-sieve/Parseval formalism.

No unconditional zeta-zero proportion changes here.

## 1. Exact Bazin input

The current primary source is Péa (Pierre-Alexandre) Bazin, *Exponential sums over primes are unbounded*, arXiv:2508.18394v3 (5 August 2026). For an arithmetic function `f` supported on `[1,x]`, write

\[
F(x;\alpha)=\sum_{n\le x}f(n)e(\alpha n),
\qquad
F(n,n+y;\alpha)=\sum_{n<m\le n+y} f(m)e(\alpha m),
\]

and

\[
E_y(\beta)=\sum_{1\le h\le y}e(\beta h).
\]

Bazin's Theorem 8 states, for `y<=x` and `Q<=x^{1/2}`,

\[
\sum_{-y<n\le x}|F(n,n+y;\alpha)|^2
\gg
\frac1x
\sum_{q\le Q}\sum_{(a,q)=1}
|F(x;a/q)|^2
\left|E_y\!\left(\alpha-\frac aq\right)\right|^2.
\tag{1}
\]

The proof is explicit: the Fourier transform of the sliding-window sequence is

\[
F(x;\alpha+\beta)E_y(-\beta),
\tag{2}
\]

and the Montgomery--Vaughan large sieve is applied at the points `a/q-alpha`, whose spacing is at least `Q^{-2}`. Before replacing the denominator by `asymp x`, the proof gives the more precise scale

\[
\sum_{-y<n\le x}|F(n,n+y;\alpha)|^2
\ge
\frac{1}{\lfloor x\rfloor+\lfloor y\rfloor+Q^2}
\sum_{q\le Q}\sum_{(a,q)=1}
|F(x;a/q)|^2
\left|E_y\!\left(\alpha-\frac aq\right)\right|^2.
\tag{3}
\]

For `f=Lambda`, Bazin then supplies the arithmetic major-arc module from Jianya Liu and Tao Zhan, *The ternary Goldbach problem in arithmetic progressions*, Acta Arith. 82 (1997), 197--227, Theorem 3. In Bazin's normalization this is his Theorem 9:

\[
\sum_{q\le Q}
\max_{(a,q)=1}
\max_{|\lambda|<\delta}
\left|
\psi(x;a/q+\lambda)
-\frac{\mu(q)}{\varphi(q)}E_x(\lambda)
\right|
\ll_A x(\log x)^{-A}
\tag{4}
\]

when

\[
Q\le x^{1/3}(\log x)^{-E(A)},
\qquad
\delta\le Q^{-3}(\log x)^{-E(A)}.
\tag{5}
\]

This is the extra arithmetic input behind Bazin's unconditional Theorem 2,

\[
\inf_{\alpha\in\mathbb R}
\frac1x\sum_{-y<n\le x}
\left|\sum_{n<m\le n+y}\Lambda(m)e(\alpha m)\right|^2
\gg y\log x,
\qquad y\le x^{1/3-\varepsilon}.
\tag{6}
\]

Equation (1) is general harmonic analysis; equations (4)--(6) are where the special prime arithmetic enters.

## 2. Exact specialization to the distinguished bow coefficient

Let `N,K` be positive integers and let `b(1),...,b(N)` be an arbitrary complex sequence. Define

\[
S_b(n;K):=
\sum_{\substack{n<m\le n+K\\1\le m\le N}}b(m),
\qquad
V_b(K):=\sum_{-K<n\le N}|S_b(n;K)|^2,
\tag{7}
\]

and its additive Fourier polynomial

\[
B(\beta):=\sum_{m=1}^{N}b(m)e(\beta m).
\tag{8}
\]

For an arbitrary demodulation parameter `xi in R/Z`, put

\[
f_\xi(m):=b(m)e(-\xi m).
\tag{9}
\]

Apply Bazin's Theorem 8 to `f_xi` at additive twist `alpha=xi`. The short sum is then exactly independent of `xi`:

\[
\sum_{n<m\le n+K}f_\xi(m)e(\xi m)
=S_b(n;K).
\tag{10}
\]

At a Farey point `r=a/q`, however,

\[
F_\xi(N;r)
=\sum_{m\le N}b(m)e((r-\xi)m)
=B(r-\xi).
\tag{11}
\]

Thus (3) becomes the exact proof interface

\[
\boxed{
V_b(K)
\ge
\frac{1}{N+K+Q^2}
\sum_{q\le Q}\sum_{(a,q)=1}
|B(a/q-\xi)|^2
|E_K(\xi-a/q)|^2
}
\tag{12}
\]

with the same harmless endpoint convention as Bazin's finite support.

For the WI-195 source problem one may take, schematically,

\[
b_U(m)=(\Lambda(m)-\Lambda^\sharp(m))m^{-iU}
\tag{13}
\]

or retain the exact smooth/source weight before the final normalization. Equation (12) is then a rational-additive sampling theorem for the **logarithmically chirped** source coefficient. It does not discard the sign-sensitive `Lambda-Lambda^sharp` coupling.

## 3. Averaging the free demodulation is exactly circular

A tempting use of (12) is to exploit that `xi` is free and average it, hoping that some translate of the Farey cloud must capture generic Fourier energy. This gives no new information.

For every fixed `r in R/Z`, periodicity and the change of variable `beta=r-xi` give

\[
\int_0^1
|B(r-\xi)|^2|E_K(\xi-r)|^2\,d\xi
=
\int_0^1|B(\beta)|^2|E_K(\beta)|^2\,d\beta.
\tag{14}
\]

But the exact Fourier identity used in Bazin's own proof, followed by Parseval, gives

\[
\boxed{
\int_0^1|B(\beta)|^2|E_K(\beta)|^2\,d\beta
=V_b(K).
}
\tag{15}
\]

Therefore, if

\[
M_Q:=\#\{a/q\pmod1:q\le Q,(a,q)=1\}
=\sum_{q\le Q}\varphi(q),
\tag{16}
\]

then averaging (12) over `xi` yields only

\[
\boxed{
V_b(K)
\ge
\frac{M_Q}{N+K+Q^2}V_b(K).
}
\tag{17}
\]

This is a tautological self-bound, not a lower estimate for `V_b(K)`. Indeed

\[
M_Q\le \sum_{q\le Q}q=\frac{Q(Q+1)}2
\tag{18}
\]

and `N>=Q^2`, so

\[
\frac{M_Q}{N+K+Q^2}
\le
\frac{Q(Q+1)}{4Q^2}
\le \frac12.
\tag{19}
\]

No choice of the admissible `Q<=sqrt(N)` turns the averaged transform into coercivity. Any useful application of (12) to the distinguished bow must therefore insert **non-averaged arithmetic information about the sampled values `B(a/q-xi)`**.

This closes one natural route exposed by Bazin's new theorem: `general lower-sieve transform + free demodulation + Parseval/average` cannot create the missing diagonal-scale bound.

## 4. Why Bazin's prime theorem does not transfer as a fixed-additive black box

Bazin's Theorem 2 concerns a fixed linear phase `e(alpha m)` and is uniform in that fixed `alpha`. The distinguished bow phase is instead

\[
e\!\left(-\frac{U}{2\pi}\log m\right)=m^{-iU}.
\tag{20}
\]

At the count-saturating source scale of WI-188--WI-195,

\[
N=T^{1/2+o(1)},
\qquad U\asymp T,
\qquad
\frac{U}{N^2}=N^{o(1)}.
\tag{21}
\]

If the bow height is `T^vartheta` up to logarithms, its multiplicative Gallagher interval has

\[
K=\frac{N}{T^\vartheta}\,T^{o(1)}
=N^{1-2\vartheta+o(1)}.
\tag{22}
\]

For every fixed `vartheta<1/2`, this is a positive power of `N`. Linearizing the logarithmic phase over an interval of length `K` leaves a quadratic Taylor scale

\[
\frac{U}{N^2}K^2
=N^{2(1-2\vartheta)+o(1)}\to\infty.
\tag{23}
\]

Equivalently, its instantaneous additive frequency changes across the interval by

\[
\asymp \frac{U}{N^2}K
=N^{1-2\vartheta+o(1)}\to\infty.
\tag{24}
\]

Thus the self-dual logarithmic chirp cannot be frozen to one additive frequency on a power-length bow interval. This is the one-dimensional local manifestation of the phase self-duality already isolated in WI-194.

There is also a direct range mismatch at the current count-saturating frontier. WI-202 leaves only fixed `vartheta<=3943/12011`, so

\[
K\ge N^{1-2(3943/12011)+o(1)}
=N^{4125/12011+o(1)},
\tag{25}
\]

and `4125/12011 > 1/3`. Bazin's unconditional Theorem 2 is proved for `y<=x^{1/3-epsilon}`, not for this longer target scale. A lower bound on shorter subintervals does not prevent cancellation when those subintervals are assembled into a longer chirped sum.

The general Theorem 8 avoids this range restriction, but precisely at the price of requiring the new global spectral input in (12).

## 5. The missing arithmetic theorem is now explicit

For `b=b_U` from (13), the non-averaged Bazin route would need a lower-energy statement of the schematic form

\[
\sum_{q\le Q}\sum_{(a,q)=1}
|B_U(a/q-\xi)|^2
|E_K(\xi-a/q)|^2
\gg N^2K\log N
\tag{26}
\]

at some source-compatible `Q,xi`, with the exact normalization adjusted to the WI-195 weight. Equivalently, after restricting to `|xi-a/q|<=c/K`, one seeks enough rational spectral mass to force

\[
V_{b_U}(K)\gg NK\log N.
\tag{27}
\]

For the unchirped coefficient `Lambda`, Bazin manufactures this mass from the rational major-arc asymptotic (4). With the factor `n^{-iU}`, even the formal prime-density main term is oscillatory:

\[
\int_1^N t^{-iU}\,dt
=\frac{N^{1-iU}-1}{1-iU},
\tag{28}
\]

whose magnitude is `O(N/U)=N^{-1+o(1)}` at the self-dual scale. Hence the deterministic major-arc main term used for the unchirped prime sequence is not the required source of (26); any large rational spectral energy must come from the genuinely oscillatory arithmetic remainder/zero structure. For `Lambda-Lambda^sharp`, the same issue must be handled before taking absolute values so that the structured subtraction is not lost.

This does not prove that (26) is false. It identifies it as a new arithmetic theorem surface. Character decompositions at rational points, dispersion across the Farey family, source-specific bilinear structure, or an explicit-formula argument could in principle attack it. What is ruled out is obtaining (27) from Bazin's general lower-sieve identity plus harmonic-analysis averaging alone.

## 6. Prior art and novelty audit

- **Bazin, arXiv:2508.18394v3 (5 Aug 2026):** Theorem 8 is the general large-sieve lower transform (1); Theorem 2 is the unconditional prime lower bound at additive twists and lengths `y<=x^(1/3-epsilon)`. These are literature results, not Mathia claims.
- **Liu--Zhan, Acta Arith. 82 (1997), Theorem 3:** the Bombieri--Vinogradov-type additive rational-twist estimate is the arithmetic module Bazin uses for primes. Bazin restates it as Theorem 9 with the ranges in (5).
- **Matomäki--Shao, *Discorrelation Between Primes in Short Intervals and Polynomial Phases*, IMRN 2021, 12330--12355:** neighboring short-interval prime-phase prior art gives pointwise *upper/discorrelation* results for polynomial phases only for interval exponent `>2/3`; its proof also identifies multiplicative `n^{it}` twists as a separate Dirichlet-polynomial regime. It does not supply the lower spectral-energy statement (26).
- The local Mathia corpus already rules out phase-only two-dimensional compression (WI-194), twist-averaged de-exceptionalization, positive single-window optimization, and PSD multiwindow amplification (WI-195--WI-207). No local finding or source anchor located before publication contained Bazin's 2026 lower-transform theorem or the exact demodulation/Parseval circularity (14)--(19).

The new durable content here is therefore not Bazin's theorem itself. It is the exact specialization to the source-fixed logarithmic chirp, the proof that free-demodulation averaging collapses to a self-inequality, and the resulting identification of rational log-chirp spectral energy as the additional arithmetic information a Bazin-style attack would have to provide. No priority claim is made beyond this bounded audit.

## 7. Boundary and falsification conditions

This finding would be materially superseded by any theorem that supplies the missing non-averaged spectral mass in (26), or by a different specialization of Bazin's transform that uses additional source arithmetic before the Farey samples are averaged. In particular, (17) does **not** say that every choice of `xi` is useless; it says only that existence of a good `xi` cannot be obtained from averaging/Parseval without further information.

Likewise, the failure of local linearization in (23) does not rule out a higher-order stationary, bilinear, spectral, or character-theoretic treatment of the logarithmic phase. It rules out importing Bazin's fixed-additive Theorem 2 merely by freezing the chirp over the physical bow interval.

Finally, a theorem for `Lambda(n)n^{-iU}` alone would not automatically settle the exact WI-195 norm, because the structured `Lambda^sharp` term may interfere at the distinguished source twist. The decisive input must either control the full `Lambda-Lambda^sharp` coefficient in the same norm or prove a separate sign-safe bridge.

## Consequence for the research line

The newest unconditional lower-bound technology for additive prime twists does not remove the source-fixed bow obstruction as a black box. It does, however, give a sharper equivalent research interface:

\[
\boxed{
\text{distinguished multiplicative Gallagher coercivity}
\quad\Longleftarrow\quad
\text{non-averaged Farey energy for the rational log-chirp spectrum}.
}
\]

The generic large-sieve transform is already exhausted by Parseval under free demodulation. Progress must enter through special arithmetic of the sampled logarithmic-chirp prime spectrum, through the full signed source covariance, or through an observable outside the positive sliding-window framework already closed by WI-206--WI-207.