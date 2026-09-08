# XF-110 — q-scale source Toeplitz bad spectrum is thin while bad eigenvectors are broad

**Status:** `EXACT-DERIVED` + `SOURCE-L2-DILUTION` + `SPECTRAL-THINNESS` + `EIGENVECTOR-DELOCALIZATION`. XF-106--XF-109 progressively force any failure of the q-scale source Toeplitz gate to be collective, long-range, and macroscopically rough in coefficient-Fourier space. There is an additional orthogonal restriction. At the same fixed q-scale cutoff, the entire off-diagonal source has vanishing normalized `ell^2` mass. Consequently the Toeplitz matrix may still be indefinite, but only on a vanishing fraction of its spectrum, while every actual nonpositive eigenvector must be spread over almost `q` coefficient coordinates.

Keep the mass-preserving source interface of XF-108--XF-109,

\[
N=2q^2,\qquad
\Delta^2\asymp q^{-3},\qquad
a:=N\Delta\asymp q^{1/2},
\qquad \Delta\asymp a^{-3},
\tag{1}
\]

with fixed

\[
L=\log a+c,\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor,
\qquad c\in\mathbf R,
\tag{2}
\]

and moments

\[
\widehat\mu_0=1,
\qquad
\widehat\mu_m
=
\frac{1}{N}
\left[
B(m\Delta)
-
\frac1{2\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\omega_\psi\!\left(m,\frac{\lambda_n}{\Delta}\right)
\right],
\qquad
\lambda_n=\frac12\log n,
\tag{3}
\]

where `omega_psi` is the bounded, compactly supported, mass-preserving deposition of XF-108. Let

\[
\widehat T_K=(\widehat\mu_{i-j})_{0\le i,j\le K}
\tag{4}
\]

and write its eigenvalues as `lambda_0,...,lambda_K`. Then

\[
\boxed{
S_2(a):=\sum_{m=1}^K|\widehat\mu_m|^2
\ll_{\psi,c}
\frac{(\log a)^2}{a^2}.
}
\tag{5}
\]

This gives the normalized spectral second-moment bound

\[
\boxed{
\frac1{K+1}
\sum_{j=0}^K(\lambda_j-1)^2
\le 2S_2(a)
\ll_{\psi,c}
\frac{(\log a)^2}{a^2}.
}
\tag{6}
\]

Hence, for every fixed `eta>0`,

\[
\boxed{
\frac{
\#\{j:|\lambda_j-1|\ge\eta\}
}{K+1}
\ll_{\psi,c,\eta}
\frac{(\log a)^2}{a^2}.
}
\tag{7}
\]

In particular, if `n_-(\widehat T_K)` denotes the number of nonpositive eigenvalues, counted with multiplicity, then

\[
\boxed{
\frac{n_-(\widehat T_K)}{K+1}
\ll_{\psi,c}
\frac{(\log a)^2}{a^2}
\asymp
\frac{(\log q)^2}{q},
}
\tag{8}
\]

and, since `K+1\asymp a^3\log a`, also

\[
\boxed{
n_-(\widehat T_K)
\ll_{\psi,c}
a(\log a)^3
\asymp
q^{1/2}(\log q)^3.
}
\tag{9}
\]

At the same time, every real unit eigenvector `v` with eigenvalue `lambda<=0` obeys

\[
\boxed{
\|v\|_\infty
\ll_{\psi,c}
\frac{\log a}{a},
}
\tag{10}
\]

and therefore

\[
\boxed{
|\operatorname{supp}v|
\gg_{\psi,c}
\frac{a^2}{(\log a)^2}
\asymp
\frac{q}{(\log q)^2}.
}
\tag{11}
\]

Thus a surviving source obstruction has a characteristic **thin-but-broad** geometry: the bad eigenspace can occupy only a vanishing spectral fraction, but an individual bad eigenvector cannot be sparse. This strengthens the `Omega(q^{1/2})` support obstruction of XF-106 by almost a square-root factor for the canonical eigenvector certificate of indefiniteness.

## 1. The q-scale source has vanishing quadratic moment mass

Split `(3)` as

\[
\widehat\mu_m
=\mu_m^{\rm ar}+\mu_m^{\rm pp},
\tag{12}
\]

where

\[
\mu_m^{\rm ar}=\frac{\Delta}{a}B(m\Delta)
\tag{13}
\]

and

\[
\mu_m^{\rm pp}
=-\frac1{2a}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\omega_\psi\!\left(m,\frac{\lambda_n}{\Delta}\right).
\tag{14}
\]

For the archimedean part, XF-052 gives

\[
B(\xi)
=e^\xi-
\frac{e^{-5\xi}}{1-e^{-4\xi}}.
\tag{15}
\]

Hence `|B(xi)|<<xi^{-1}` for `0<xi<=1`, while `|B(xi)|<<e^xi` for `xi>=1`. On the singular range `m Delta<=1`,

\[
|\mu_m^{\rm ar}|
\ll \frac1{am},
\tag{16}
\]

so

\[
\sum_{m\Delta\le1}|\mu_m^{\rm ar}|^2
\ll
\frac1{a^2}\sum_{m\ge1}\frac1{m^2}
\ll a^{-2}.
\tag{17}
\]

On `1<=m Delta<=L`, geometric summation instead gives

\[
\begin{aligned}
\sum |\mu_m^{\rm ar}|^2
&\ll
\frac{\Delta^2}{a^2}
\sum_{m\Delta\le L}e^{2m\Delta}\\
&\ll
\frac{\Delta e^{2L}}{a^2}
\ll_c \Delta
\asymp a^{-3}.
\end{aligned}
\tag{18}
\]

Thus

\[
\sum_{m=1}^K|\mu_m^{\rm ar}|^2
\ll_c a^{-2}.
\tag{19}
\]

The prime-power part is larger only by logarithms. At the fixed cutoff `(2)`, the one-atom-per-cell geometry of XF-106 applies. Indeed a mesh coordinate can receive an atom only from an integer in an interval of length

\[
\ll \Delta e^{2L}
\asymp_c a^{-1},
\tag{20}
\]

which is smaller than one for all sufficiently large `a`. Hence each coordinate receives at most one prime-power atom. Conversely, compact support of the fixed deposition bump makes each atom touch only `O_psi(1)` coordinates, and the mass-preserving weights are uniformly bounded because the denominator `p_psi` of XF-108 is bounded below.

It follows from `(14)` that, with `X=e^{2L+O(\Delta)}\asymp_c a^2`,

\[
\sum_{m=1}^K|\mu_m^{\rm pp}|^2
\ll_\psi
\frac1{a^2}
\sum_{n\le X}\frac{\Lambda(n)^2}{n}.
\tag{21}
\]

No PNT is needed to bound the last sum. Since `0<=Lambda(n)<=log X` for `n<=X`,

\[
\sum_{n\le X}\frac{\Lambda(n)^2}{n}
\le
(\log X)
\sum_{n\le X}\frac{\Lambda(n)}n.
\tag{22}
\]

XF-104 derives the elementary Chebyshev bound `Psi(x)=sum_{n<=x}Lambda(n)<<x`. Partial summation therefore gives

\[
\sum_{n\le X}\frac{\Lambda(n)}n
=
\frac{\Psi(X)}X
+
\int_2^X\frac{\Psi(t)}{t^2}\,dt
+O(1)
\ll \log X.
\tag{23}
\]

Combining `(21)`--`(23)` and `X\asymp_c a^2`,

\[
\boxed{
\sum_{m=1}^K|\mu_m^{\rm pp}|^2
\ll_{\psi,c}
\frac{(\log a)^2}{a^2}.
}
\tag{24}
\]

Finally `|x+y|^2<=2|x|^2+2|y|^2`, together with `(19)` and `(24)`, proves `(5)`. The contrast with XF-105 is useful: the normalized raw `ell^1` mass is already order one at this cutoff, while the normalized `ell^2` mass still tends to zero quadratically in `a` up to logarithms.

## 2. Hilbert--Schmidt mass makes the exceptional spectrum sparse

Put

\[
A_K:=\widehat T_K-I_{K+1}.
\tag{25}
\]

Because `A_K` is Hermitian Toeplitz with zero diagonal,

\[
\begin{aligned}
\|A_K\|_{\rm HS}^2
&=
\sum_{\substack{0\le i,j\le K\\i\ne j}}
|\widehat\mu_{i-j}|^2\\
&=
2\sum_{m=1}^K(K+1-m)|\widehat\mu_m|^2\\
&\le
2(K+1)S_2(a).
\end{aligned}
\tag{26}
\]

The eigenvalues of `A_K` are exactly `lambda_j-1`, so the spectral theorem turns `(26)` into the exact identity and bound

\[
\sum_{j=0}^K(\lambda_j-1)^2
=
\|A_K\|_{\rm HS}^2
\le
2(K+1)S_2(a).
\tag{27}
\]

Equations `(5)` and `(27)` prove `(6)`. Markov's inequality on this finite spectral measure gives `(7)`. Every nonpositive eigenvalue satisfies `|lambda_j-1|>=1`, so `(8)` follows by taking `eta=1`; `(9)` then follows from

\[
K+1\asymp\frac{\log a}{\Delta}\asymp a^3\log a.
\tag{28}
\]

This conclusion is deliberately weaker than positivity. The Hilbert--Schmidt norm itself is not small: `(26)` allows it to grow because the matrix dimension grows like `a^3 log a`. What vanishes is the **mean squared spectral displacement from one**. A small exceptional set of very nontrivial eigenvalues remains fully compatible with `(6)`.

## 3. A nonpositive eigenvector is almost q-scale in coefficient support

The same `ell^2` coefficient bound has a different consequence at the eigenvector level. Let `v` be a real unit eigenvector,

\[
\widehat T_Kv=\lambda v,
\qquad \lambda\le0.
\tag{29}
\]

For each coordinate `i`, the eigenvalue equation gives

\[
(1-\lambda)v_i
=-
\sum_{\substack{0\le j\le K\\j\ne i}}
\widehat\mu_{i-j}v_j.
\tag{30}
\]

Each positive lag occurs at most twice in one row, hence

\[
\sum_{j\ne i}|\widehat\mu_{i-j}|^2
\le 2S_2(a).
\tag{31}
\]

Cauchy--Schwarz, `||v||_2=1`, and `1-lambda>=1` therefore yield

\[
|v_i|
\le \sqrt{2S_2(a)}.
\tag{32}
\]

Taking the maximum and inserting `(5)` proves `(10)`. If `s=|supp v|`, then

\[
1=\|v\|_2^2
\le s\|v\|_\infty^2,
\tag{33}
\]

which proves `(11)`.

The quantifier matters. Equation `(10)` is proved for an **eigenvector with nonpositive eigenvalue**, not for every arbitrary vector whose Rayleigh quotient happens to be nonpositive. This is enough for the feasibility obstruction: if `widehat T_K` is indefinite, the spectral theorem supplies such an eigenvector canonically. It also avoids a false strengthening in which a mixture of positive and negative spectral directions would be claimed to inherit the same coordinatewise bound.

## 4. The surviving obstruction is thin in dimension but broad in every canonical direction

XF-107 applies to the support of the eigenvector in `(29)`: restricting to that principal coordinate set retains a nonpositive Rayleigh direction. Hence its physical lag diameter must satisfy

\[
\Delta\,\operatorname{diam}(\operatorname{supp}v)
\ge \log a-O(1).
\tag{34}
\]

XF-109 applies to the same unit vector and forces a fixed fraction of its coefficient-Fourier energy outside the PNT-flat arc

\[
|\theta|
\le
\Delta\exp\!\bigl(c_2\sqrt{\log a}\bigr).
\tag{35}
\]

The q-scale source-side obstruction must therefore satisfy four simultaneous constraints. Its nonpositive spectral subspace has relative dimension at most `O((log q)^2/q)` by `(8)`; any nonpositive eigenvector uses at least `Omega(q/(log q)^2)` coefficient coordinates by `(11)`; its lag support spans the natural q-scale frequency range by `(34)`; and it carries fixed coefficient-Fourier mass in the arithmetically rough sector by XF-109.

These constraints are compatible rather than contradictory. A low-dimensional subspace can be generated by vectors that are individually very broad. What is excluded is a large family of independent local failures, or a negative eigenvector concentrated on the `Omega(q^{1/2})` support threshold that remained possible after XF-106 alone.

## 5. Stress tests and exact boundary

The fixed offset `c` in `(2)` is load-bearing for the stated powers. It keeps the arithmetic endpoint at `X\asymp a^2` and ensures the one-atom-per-cell estimate `(20)`. The same argument can be tracked for slowly moving cutoffs, but the constants and powers must then be recomputed rather than imported from `(5)`.

Mass-preserving deposition is not needed merely to prove a crude `ell^2` upper bound; bounded fixed-width deposition would suffice for `(21)`. It remains part of the canonical q-scale source because XF-108--XF-109 show that without mass preservation a mesh-phase artifact can contaminate the PNT-scale Toeplitz interpretation. The present finding therefore stays on that corrected source interface rather than reopening the older unnormalized model.

Equation `(8)` does not imply that the negative spectrum is empty, and `(10)` does not control an arbitrary nonpositive test vector. Nor does Toeplitz positivity, even if eventually proved, automatically produce the exact equal-weight real-divisor carrier required by XF-085; it remains the weighted-measure relaxation isolated in XF-084. Finally, nothing here supplies the separate destination theorem needed to convert source realizability or nonrealizability into an upper bound on the de Bruijn--Newman constant.

No RH input enters. The arithmetic estimate uses only the Chebyshev bound already derived in XF-104. In particular, the stronger PNT cancellation used by XF-108--XF-109 is not required for `(5)`--`(11)`.

## 6. Prior-art and novelty boundary

The passage from Hilbert--Schmidt control to the second moment of matrix eigenvalues is finite-dimensional spectral theory, and asymptotic spectral distribution for Toeplitz matrices belongs to the classical Szego/Toeplitz literature. No novelty is claimed for those generic principles or for Chebyshev's bound. The closest current RH-facing Toeplitz works found in the line's prior-art audit remain Alain Connes and Walter D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, **Communications in Mathematical Physics** 406 (2025), article 312, and Wojciech Michalowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients*, arXiv:2607.16795 (2026). They study different Toeplitz/convolution objects and do not supply the source estimate `(5)` or the exceptional-spectrum and eigenvector-support scales `(8)`--`(11)` for the Guinand--Weil/Vieta moment matrix `(4)`.

The line-specific mathematical delta is the q-scale source estimate `(5)` and what it does to the still-open Toeplitz feasibility gate. After XF-109, the surviving negative sector had to be macroscopically rough but could in principle have been spectrally extensive. It cannot: **almost all eigenvalues of the source Toeplitz matrix converge to one in density, while any eigenvector that actually reaches the nonpositive sector must be spread over at least `q/(log q)^2` coefficients.** The next sign problem is therefore an exceptional-sector problem, not a bulk instability problem.

No new external theorem is load-bearing beyond sources already anchored for the current line, so `SOURCES.md` requires no change.