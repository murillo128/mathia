# NB-303 — Farey-separated shell frequencies force quadratic moving-cutoff source compression

**Date:** 2026-09-23

**Status:** `EXACT-DERIVED` + `SOURCE-SIDE` + `MOVING-CUTOFF` + `LARGE-SIEVE` + `NONOPTIMAL-SUFFICIENT-RATE`.

NB-302 reduced the moving-cutoff projected-dilation source-compression threshold from cubic to the five-halves scale by expanding the reciprocal-shell tail pairwise. Its remaining `N^5/m^2` phase term came from taking absolute values of the individual pairwise periodic remainders. That term is not intrinsic.

The reciprocal-shell sequence is itself a finite trigonometric polynomial whose distinct frequencies are reduced rationals with denominator at most `N`. Hence its frequency set is `N^{-2}`-separated on the circle. Applying the classical Montgomery--Vaughan separated-frequency large-sieve inequality directly to the *whole shell sequence*, rather than pairwise to its Gram expansion, yields a uniform interval-energy bound. Combining that bound with one exact full-period identity gives

\[
\boxed{
Q_N(u)\le (4N^2+2)\|u\|_2^2\le 5N^2\|u\|_2^2,
}
\]

where `Q_N(u)` is the Cesàro shell energy from NB-302. A dyadic decomposition of the weighted reciprocal-shell tail then gives

\[
\boxed{
\left\|1_{(0,1/m]}u\right\|_2^2
\le
\left(
\frac{10N^2}{m}
+
\frac{20N^4}{3m^2}
\right)\|u\|_2^2.
}
\]

Therefore, with `N=n-1`,

\[
\boxed{
\beta_n(m)^2
\le
\min\left\{
1,
\frac{10N^2}{m}
+
\frac{20N^4}{3m^2}
\right\},
}
\]

and in particular

\[
\boxed{
\frac{m}{(n-1)^2}\to\infty
\quad\Longrightarrow\quad
\beta_n(m)\to0.
}
\]

This removes both the logarithmic Cesàro loss and the five-halves phase barrier of NB-302. The result remains a sufficient source-compression estimate, not an optimality theorem and not a target-aware Ford estimate.

## 1. Reciprocal shells have a Farey-separated spectrum

Use the notation of NB-301--NB-302. Let

\[
U=V_{n-1},
\qquad
N=n-1,
\]

and write

\[
u=\sum_{j=2}^N a_jg_j.
\]

On the reciprocal shell `t in [k,k+1)`, with `t=1/x`, one has

\[
u(1/t)=u_k:=\sum_{j=2}^Na_jr_j(k),
\qquad
r_j(k)=\frac{k\bmod j}{j}.
\tag{1}
\]

The exact source norm and tail are

\[
\|u\|_2^2
=
\sum_{k\ge1}\frac{|u_k|^2}{k(k+1)},
\tag{2}
\]

and

\[
\left\|1_{(0,1/m]}u\right\|_2^2
=
\sum_{k\ge m}\frac{|u_k|^2}{k(k+1)}.
\tag{3}
\]

Each `r_j` is `j`-periodic, so its finite Fourier expansion has frequencies `h/j`, `0<=h<j`. After combining equal characters, there is a finite set `F_N subset R/Z` and coefficients `c_alpha` such that

\[
\boxed{u_k=\sum_{\alpha\in F_N}c_\alpha e^{2\pi i\alpha k}.}
\tag{4}
\]

Every `alpha in F_N` is a reduced rational whose denominator is at most `N`. Hence for distinct `alpha,beta in F_N`, represented by reduced fractions `a/q` and `b/r`,

\[
\|\alpha-\beta\|_{\mathbb R/\mathbb Z}
\ge
\frac1{qr}
\ge
\frac1{N^2}.
\tag{5}
\]

Thus the shell spectrum is uniformly separated by

\[
\boxed{\delta_N\ge N^{-2}.}
\tag{6}
\]

This is the structural input that NB-302 did not use: pairwise periods `<=N^2` are the time-domain shadow of an `N^{-2}` Farey separation in frequency space.

## 2. The dual large sieve controls every shell interval

For a finite set of frequencies on `R/Z` with circular separation at least `delta`, the classical separated-frequency large sieve, equivalently the dual Montgomery--Vaughan generalized Hilbert inequality, gives for every interval `I` of `L` consecutive integers

\[
\sum_{k\in I}
\left|
\sum_\alpha c_\alpha e^{2\pi i\alpha k}
\right|^2
\le
(L-1+\delta^{-1})
\sum_\alpha|c_\alpha|^2.
\tag{7}
\]

Using the harmless weaker constant `L+delta^{-1}` and (6), define

\[
Q_N(u):=\sum_{\alpha\in F_N}|c_\alpha|^2.
\tag{8}
\]

Then every interval of `L` consecutive reciprocal shells satisfies

\[
\boxed{
\sum_{k\in I}|u_k|^2
\le
(L+N^2)Q_N(u).
}
\tag{9}
\]

This `Q_N` is exactly the Cesàro shell energy used in NB-302. Indeed, if

\[
P_N=\operatorname{lcm}(2,\ldots,N),
\]

then every frequency in `F_N` has denominator dividing `P_N`. Orthogonality of distinct characters over one full period gives the exact identity

\[
\boxed{
\sum_{k=1}^{P_N}|u_k|^2
=P_NQ_N(u).
}
\tag{10}
\]

No estimate of the Fourier coefficients in terms of the original `a_j` is needed.

## 3. Exact periodicity plus the large sieve gives `Q_N=O(N^2)||u||^2`

The key step is to reverse the usual use of the large sieve: instead of only upper-bounding a finite shell block, use it to show that a positive fraction of one exact period must already occur among the first `O(N^2)` shells.

Set

\[
L:=2N^2.
\tag{11}
\]

First suppose `P_N>=L`. If `P_N=L`, (10) immediately gives all period energy in the first `L` shells. If `P_N>L`, apply (9) to the complementary consecutive block

\[
I=\{L+1,\ldots,P_N\},
\]

whose length is `P_N-L`. Then

\[
\sum_{k=L+1}^{P_N}|u_k|^2
\le
(P_N-L+N^2)Q_N(u).
\]

Subtracting from (10),

\[
\boxed{
\sum_{k=1}^{L}|u_k|^2
\ge
(L-N^2)Q_N(u)
=N^2Q_N(u).
}
\tag{12}
\]

Since the weights in (2) decrease,

\[
\|u\|_2^2
\ge
\frac1{L(L+1)}
\sum_{k=1}^{L}|u_k|^2
\ge
\frac{N^2}{L(L+1)}Q_N(u).
\]

With `L=2N^2`, this yields

\[
\boxed{
Q_N(u)
\le
(4N^2+2)\|u\|_2^2.
}
\tag{13}
\]

Now suppose instead that `P_N<L`. Using the complete first period in (2),

\[
\|u\|_2^2
\ge
\frac1{P_N(P_N+1)}
\sum_{k=1}^{P_N}|u_k|^2
=
\frac{Q_N(u)}{P_N+1}.
\]

Hence

\[
Q_N(u)
\le
(P_N+1)\|u\|_2^2
<
(2N^2+1)\|u\|_2^2.
\tag{14}
\]

Combining the two cases, for every `N>=2`,

\[
\boxed{
Q_N(u)
\le
(4N^2+2)\|u\|_2^2
\le
5N^2\|u\|_2^2.
}
\tag{15}
\]

This sharpens the `N^2(9+H_N^3/2)` bound of NB-302 and, more importantly, obtains it without Möbius inversion or coefficient `ell^1` control.

## 4. Dyadic interval control removes the pairwise phase remainder

Partition the tail `k>=m` into dyadic shell blocks

\[
I_r
=
\{2^rm,\ldots,2^{r+1}m-1\},
\qquad r\ge0.
\tag{16}
\]

The block length is `2^rm`. By (9),

\[
\sum_{k\in I_r}|u_k|^2
\le
(2^rm+N^2)Q_N(u).
\tag{17}
\]

For `k in I_r`,

\[
\frac1{k(k+1)}
\le
\frac1{(2^rm)^2}.
\]

Therefore (3) and (17) give

\[
\begin{aligned}
\left\|1_{(0,1/m]}u\right\|_2^2
&\le
Q_N(u)
\sum_{r\ge0}
\left(
\frac1{2^rm}
+
\frac{N^2}{4^rm^2}
\right)\\
&=
Q_N(u)
\left(
\frac2m
+
\frac{4N^2}{3m^2}
\right).
\end{aligned}
\tag{18}
\]

Inserting (15),

\[
\boxed{
\left\|1_{(0,1/m]}u\right\|_2^2
\le
\left(
\frac{10N^2}{m}
+
\frac{20N^4}{3m^2}
\right)
\|u\|_2^2.
}
\tag{19}
\]

The `N^5/m^2` remainder from NB-302 has disappeared because the incomplete phases are never separated pair by pair. The large sieve controls their collective interference on every dyadic interval before any absolute-value expansion of the Gram occurs.

## 5. Quadratic moving-cutoff source compression

Let `S_m` be the normalized multiplicative dilation and, as in NB-299--NB-302,

\[
T_m=P_U S_m|_U,
\qquad
\beta_n(m):=\|T_m\|.
\tag{20}
\]

The dilated vector `S_mv` is supported in `(0,1/m]`. Hence for unit `u,v in U`,

\[
|\langle u,S_mv\rangle|
\le
\left\|1_{(0,1/m]}u\right\|_2.
\]

Taking suprema and using (19), with `N=n-1`, gives

\[
\boxed{
\beta_n(m)^2
\le
\min\left\{
1,
\frac{10(n-1)^2}{m}
+
\frac{20(n-1)^4}{3m^2}
\right\}.
}
\tag{21}
\]

Consequently, for a moving family `n=n_X`, `m=m_X`,

\[
\boxed{
\frac{m_X}{(n_X-1)^2}\to\infty
\quad\Longrightarrow\quad
\beta_{n_X}(m_X)\to0.
}
\tag{22}
\]

Indeed both terms in (21) vanish under that hypothesis. This improves the sufficient scale `m/N^(5/2)->infinity` from NB-302 to the quadratic scale `m/N^2->infinity` and removes the logarithmic factor in the leading tail-energy control as well.

The exponent `2` is not claimed to be necessary or optimal. The proof only says that generic source overlap cannot sustain the projected-dilation mechanism above the quadratic window.

## 6. Consequence for first-free projected-dilation compression

Let `Z` be a finite off-critical packet and

\[
\delta_Z
:=
\min_{\rho\in Z}
\left(\Re\rho-\frac12\right)>0.
\]

Let `K_{n-1,Z}` be the first-free sample Gram and `Xi_{m,n,Z}` the projected-dilation compression matrix of NB-299--NB-302. Define

\[
\varepsilon_{\mathrm{LS}}(m,n)^2
:=
\min\left\{
1,
\frac{10(n-1)^2}{m}
+
\frac{20(n-1)^4}{3m^2}
\right\}.
\tag{23}
\]

Whenever `epsilon_LS(m,n)<1`, the exact NB-299 factorization and (21) imply

\[
\boxed{
\|\Xi_{m,n,Z}\|
\le
\|K_{n-1,Z}\|
\frac{
\left(m^{-\delta_Z}+\varepsilon_{\mathrm{LS}}(m,n)\right)^2
}{
1-\varepsilon_{\mathrm{LS}}(m,n)^2
}.
}
\tag{24}
\]

Thus for a moving family `(Z_X,n_X,m_X)`, the joint conditions

\[
\frac{m_X}{(n_X-1)^2}\to\infty
\qquad\text{and}\qquad
\delta_{Z_X}\log m_X\to\infty
\tag{25}
\]

force

\[
\boxed{
\frac{\|\Xi_{m_X,n_X,Z_X}\|}
{\|K_{n_X-1,Z_X}\|}
\to0.
}
\tag{26}
\]

So the generic source-overlap escape hatch is now excluded throughout the super-quadratic dilation regime, provided the off-critical damping also accumulates.

## 7. Adversarial checks

Several possible shortcuts were rejected before recording the result.

First, the argument does **not** assume that the original generator frequencies are distinct. Equal rational characters arising from different `r_j` are combined before the large sieve is applied. Separation is asserted only for the resulting distinct reduced frequencies.

Second, the circular separation estimate is uniform at the claimed scale. If `a/q` and `b/r` are distinct reduced fractions modulo one with `q,r<=N`, then their circular distance is at least `1/(qr)>=N^{-2}`. The frequency `0` causes no exception.

Third, equation (10) is exact, not asymptotic: every reduced denominator divides `P_N`, so the finite character family is orthogonal over a complete `P_N`-period. This exact identity is what permits the large-sieve upper bound on the *complement* of the first `2N^2` shells to become a lower bound on early-shell energy.

Fourth, the two `P_N` cases in Section 3 avoid any hidden assumption that `P_N` is already large compared with `N^2`. If `P_N<2N^2`, the full period itself gives the stronger estimate (14).

Fifth, the dyadic decomposition uses only interval energy and the monotone weight `1/[k(k+1)]`; there is no pairwise phase remainder left to estimate. The constants follow from `sum 2^{-r}=2` and `sum 4^{-r}=4/3`.

Finally, none of (21)--(26) compares `Xi` with the unresolved future-tail Gram, bounds the original Nyman distance, controls the condition number of the moving first-free sample Gram, or proves that the Ford target occupies a favorable destination direction. Those remain separate bottlenecks.

## 8. Prior-art boundary and research disposition

The load-bearing external inequality is classical. Montgomery and Vaughan's generalized Hilbert inequality supplies the standard separated-frequency large-sieve estimate used in (7); that source is already registered in `SOURCES.md` for NB-012. The fresh prior-art search for combinations of Nyman--Beurling, large sieve, Farey-separated reciprocal-shell frequencies, and this moving-cutoff compression mechanism did not locate the present application.

No novelty is claimed for the large sieve, Farey separation, or Fourier expansion of periodic sequences. The research delta is the combination specific to the canonical Nyman reciprocal-shell model: identify the complete shell sequence as an `N^{-2}`-separated rational-frequency polynomial, use exact-period orthogonality plus a large-sieve bound on the complementary shells to obtain `Q_N(u)=O(N^2)||u||^2`, and then apply the same interval estimate dyadically to force the quadratic moving-cutoff gate (22).

This result supersedes the `N^(5/2)` *sufficient source-compression frontier* of NB-302 but does not invalidate that historical finding. It also does not settle whether the quadratic scale is sharp. The next discriminating source-side regime is now the near/sub-quadratic window `m=O(N^2)`. Beyond source compression, the durable open issue remains coupling any such estimate to the moving off-critical packet, sample conditioning, and the target-aware Ford quantity rather than only to generic source overlap.

**Clue disposition:** no active clue is resolved by this theorem. In particular, the target-aware finite-section and inverse-repair clues remain open because the argument is source-side and target-independent.
