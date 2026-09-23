# NB-302 — Pairwise shell periodicity lowers moving-cutoff source compression to the five-halves scale

**Date:** 2026-09-23

**Status:** `EXACT-DERIVED` + `SOURCE-SIDE` + `MOVING-CUTOFF` + `NONOPTIMAL-SUFFICIENT-RATE`.

NB-300 replaced the exponential `lcm(2,...,n-1)` source-overlap scale by an explicit periodicity bound, and NB-301 then used early-shell Möbius inversion to obtain the polynomial criterion

\[
\frac{m}{(n-1)^3}\to\infty
\quad\Longrightarrow\quad
\beta_n(m)\to0.
\]

The cubic exponent in NB-301 came from bounding every reciprocal-shell value of a section vector by an `\ell^1` coefficient envelope and then inserting that pointwise bound into the tail. That loses the fact that the tail norm is quadratic and that every *pair* of sawtooth shell sequences already has period at most `ij`, hence at most `N^2`, even though the whole vector can have exponentially large global period.

This note exploits that pairwise periodicity before summing coefficients. The result is an explicit bound

\[
\boxed{
\beta_n(m)^2
\le
\min\left\{
1,
\frac{N^2\left(9+\frac12 H_N^3\right)}{m}
+
\frac{6N^5}{m(m+1)}
\right\},
\qquad N=n-1,
}
\]

where `H_N` is the `N`-th harmonic number. Consequently,

\[
\boxed{
\frac{m}{N^{5/2}}\to\infty
\quad\Longrightarrow\quad
\beta_n(m)\to0.
}
\]

Thus the projected-dilation source-compression obstruction is excluded throughout a strictly larger moving-cutoff region than NB-301, without using the global lcm scale and without any source Gram condition number. The exponent `5/2` is a sufficient exponent from the present proof; no optimality is claimed.

## 1. Reciprocal-shell model

Let

\[
U=V_{n-1},
\qquad
N=n-1,
\]

and write the canonical Nyman generators as

\[
g_j(x)
=
\left\{\frac1{jx}\right\}
-
\frac1j\left\{\frac1x\right\},
\qquad
2\le j\le N.
\]

For

\[
u=\sum_{j=2}^N a_jg_j,
\]

put `t=1/x`. On the reciprocal shell `t in [k,k+1)`, NB-301 gives

\[
g_j(1/t)=r_j(k),
\qquad
r_j(k):=\frac{k\bmod j}{j},
\]

so

\[
u(1/t)=u_k:=\sum_{j=2}^Na_jr_j(k).
\]

The source norm and the tail near zero are exactly

\[
\|u\|_2^2
=
\sum_{k\ge1}\frac{|u_k|^2}{k(k+1)},
\]

and

\[
\left\|1_{(0,1/m]}u\right\|_2^2
=
\sum_{k\ge m}\frac{|u_k|^2}{k(k+1)}.
\tag{1}
\]

NB-301 also introduced the shell-difference data `b_d` and proved the coefficient bounds

\[
\sum_{d=1}^N\frac{|b_d|^2}{d^2}
\le
6\|u\|_2^2,
\tag{2}
\]

and

\[
\sum_{j=2}^N|a_j|
\le
\sqrt6\,N^{3/2}\|u\|_2.
\tag{3}
\]

The new point is to use (2) together with the exact *pairwise* Cesàro Gram of the shell sawteeth, rather than inserting (3) pointwise into (1).

## 2. Exact pairwise Cesàro Gram

For `2<=i,j<=N`, let

\[
q_{ij}
:=
\lim_{K\to\infty}
\frac1K\sum_{k=1}^Kr_i(k)r_j(k).
\]

Write

\[
g=(i,j),
\qquad
i=ga,
\qquad
j=gb,
\qquad
(a,b)=1.
\]

Over one joint period `lcm(i,j)=gab`, the residues modulo `i` and `j` have a common residue modulo `g`. Conditioning on that common residue makes the remaining base-`g` digits independent. Since

\[
\mu_j
:=
\frac1j\sum_{r=0}^{j-1}\frac rj
=
\frac{j-1}{2j},
\]

and the common residue has variance `(g^2-1)/12`, one obtains

\[
\boxed{
q_{ij}
=
\mu_i\mu_j
+
\frac{g^2-1}{12ij}.
}
\tag{4}
\]

This identity can also be checked directly by summing over the `lcm(i,j)` residue classes. It is the crucial place where global lcm synchronization disappears: each quadratic cross-term has period only

\[
\operatorname{lcm}(i,j)\le ij\le N^2.
\tag{5}
\]

Define the Cesàro shell energy

\[
Q_N(u)
:=
\lim_{K\to\infty}
\frac1K\sum_{k=1}^K|u_k|^2.
\]

Using (4),

\[
Q_N(u)
=
\left|\sum_{j=2}^Na_j\mu_j\right|^2
+
\frac1{12}
\sum_{i,j=2}^N
 a_i\overline{a_j}
\frac{(i,j)^2-1}{ij}.
\tag{6}
\]

We bound the two terms separately.

## 3. Möbius inversion controls the centered Cesàro energy

Set

\[
x_j:=\frac{a_j}{j},
\qquad
y_d:=\frac{b_d}{d}.
\]

The early-shell Möbius inversion of NB-301 gives

\[
x_j
=
-\sum_{q\mid j}\frac{\mu(q)}q\,y_{j/q},
\qquad j\ge2.
\tag{7}
\]

By Minkowski for divisor convolution,

\[
\|x\|_{\ell^2([2,N])}
\le
\left(\sum_{q\le N}\frac1q\right)\|y\|_2
=
H_N\|y\|_2.
\]

Combining with (2),

\[
\boxed{
\|x\|_2
\le
\sqrt6\,H_N\|u\|_2.
}
\tag{8}
\]

For the centered term in (6), use the Jordan-totient identity

\[
(i,j)^2-1
=
\sum_{\substack{d\mid i\\d\mid j\\d\ge2}}J_2(d).
\]

Then

\[
Q_N^{\mathrm{cen}}(u)
=
\frac1{12}
\sum_{d=2}^N
J_2(d)
\left|
\sum_{\substack{j\le N\\d\mid j}}x_j
\right|^2.
\tag{9}
\]

Since `J_2(d)<=d^2`, Cauchy gives

\[
\left|
\sum_{d\mid j}x_j
\right|^2
\le
\frac Nd
\sum_{d\mid j}|x_j|^2.
\]

Substituting into (9) and reversing the sums yields

\[
Q_N^{\mathrm{cen}}(u)
\le
\frac N{12}
\sum_{j=2}^N|x_j|^2
\sum_{d\mid j}d.
\]

Using

\[
\sigma_1(j)
\le
jH_j
\le
NH_N,
\]

and (8),

\[
\boxed{
Q_N^{\mathrm{cen}}(u)
\le
\frac12N^2H_N^3\|u\|_2^2.
}
\tag{10}
\]

The logarithmic loss here is harmless for the polynomial threshold; importantly, no source Gram inverse appears.

## 4. The mean term is only quadratic in the cutoff

It remains to bound

\[
\mu(u):=\sum_{j=2}^Na_j\mu_j.
\]

Take `L=N^2` and define the finite shell average

\[
\overline u_L
:=
\frac1L\sum_{k=1}^Lu_k.
\]

From the exact weighted source norm,

\[
\sum_{k=1}^L|u_k|^2
\le
L(L+1)\|u\|_2^2,
\]

and hence by Cauchy

\[
|\overline u_L|^2
\le
(L+1)\|u\|_2^2
=
(N^2+1)\|u\|_2^2.
\tag{11}
\]

For one sawtooth, an incomplete period contributes at most `j` samples of size at most one, so

\[
\left|
\frac1L\sum_{k=1}^Lr_j(k)-\mu_j
\right|
\le
\frac jL.
\]

Therefore, by (3),

\[
|\mu(u)-\overline u_L|
\le
\frac1L\sum_{j=2}^Nj|a_j|
\le
\frac N{N^2}
\sqrt6\,N^{3/2}\|u\|_2
=
\sqrt6\,N^{1/2}\|u\|_2.
\tag{12}
\]

Combining (11) and (12), and using `N>=2`, gives the convenient bound

\[
\boxed{
|\mu(u)|^2
\le
9N^2\|u\|_2^2.
}
\tag{13}
\]

Together with (10), equation (6) yields

\[
\boxed{
Q_N(u)
\le
N^2
\left(9+\frac12H_N^3\right)
\|u\|_2^2.
}
\tag{14}
\]

Thus the long-run quadratic shell energy is only `N^2 polylog(N)` relative to the true source norm, even though the full shell vector can have exponential global period.

## 5. Pairwise periodicity controls the weighted tail

We use a simple periodic weighted-tail lemma.

**Lemma.** Let `f_k` be `p`-periodic, `|f_k|<=1`, with Cesàro mean `\bar f`. Then for every `m>=1`,

\[
\boxed{
\left|
\sum_{k=m}^\infty\frac{f_k}{k(k+1)}
-
\frac{\bar f}{m}
\right|
\le
\frac{p}{m(m+1)}.
}
\tag{15}
\]

Indeed, `h_k=f_k-\bar f` is mean-zero and `p`-periodic, so every shifted partial sum of `h_k` has modulus at most `p`. Abel summation against the decreasing weight `w_k=1/[k(k+1)]` gives

\[
\left|\sum_{k=m}^\infty h_kw_k\right|
\le
p\,w_m,
\]

which is (15).

Apply this lemma to

\[
f_k=r_i(k)r_j(k).
\]

Its period is `p_{ij}=lcm(i,j)<=ij`, its mean is `q_{ij}`, and therefore

\[
\sum_{k=m}^\infty
\frac{r_i(k)r_j(k)}{k(k+1)}
=
\frac{q_{ij}}m+E_{ij}(m),
\]

with

\[
|E_{ij}(m)|
\le
\frac{ij}{m(m+1)}.
\tag{16}
\]

Insert this expansion into (1). The Cesàro part is exactly `Q_N(u)/m`, while the phase error is bounded by

\[
\frac1{m(m+1)}
\left(\sum_{j=2}^Nj|a_j|\right)^2.
\]

From (3),

\[
\sum_{j=2}^Nj|a_j|
\le
N\sum_{j=2}^N|a_j|
\le
\sqrt6\,N^{5/2}\|u\|_2.
\tag{17}
\]

Using (14) and (17),

\[
\boxed{
\left\|1_{(0,1/m]}u\right\|_2^2
\le
B_{N,m}\|u\|_2^2,
}
\tag{18}
\]

where

\[
\boxed{
B_{N,m}
:=
\frac{N^2\left(9+\frac12H_N^3\right)}m
+
\frac{6N^5}{m(m+1)}.
}
\tag{19}
\]

This is the advertised source-tail estimate.

## 6. Projected dilation and the five-halves threshold

Let `S_m` be the normalized multiplicative dilation and let

\[
T_m=P_U S_m|_U,
\qquad
\beta_n(m):=\|T_m\|.
\]

As in NB-299--NB-301, `S_mv` is supported in `(0,1/m]`. Hence for unit vectors `u,v in U`,

\[
|\langle u,S_mv\rangle|
\le
\|1_{(0,1/m]}u\|_2.
\]

Taking suprema and using (18),

\[
\boxed{
\beta_n(m)^2
\le
\min\{1,B_{n-1,m}\}.
}
\tag{20}
\]

Now suppose `N=N_X` and `m=m_X` move with

\[
\frac{m_X}{N_X^{5/2}}\to\infty.
\tag{21}
\]

The second term in (19) tends to zero because

\[
\frac{N_X^5}{m_X^2}\to0.
\]

For the first term,

\[
\frac{N_X^2H_{N_X}^3}{m_X}
=
\frac{H_{N_X}^3}{\sqrt{N_X}}
\frac{N_X^{5/2}}{m_X}
\to0.
\]

Therefore

\[
\boxed{
\frac{m_X}{(n_X-1)^{5/2}}\to\infty
\quad\Longrightarrow\quad
\beta_{n_X}(m_X)\to0.
}
\tag{22}
\]

The global lcm scale plays no role in this argument. The only periodicities used are the pairwise periods `lcm(i,j)<=N^2` inside the quadratic tail form.

## 7. Consequence for first-free projected-dilation compression

Let `Z` be a finite off-critical packet and

\[
\delta_Z
:=
\min_{\rho\in Z}
\left(\Re\rho-\frac12\right)>0.
\]

Let `K_{n-1,Z}` be the first-free sample Gram from NB-293--NB-300, and let `\Xi_{m,n,Z}` denote the projected-dilation first-free compression matrix of NB-299/300.

Define

\[
\varepsilon_{m,n}
:=
\min\{1,\sqrt{B_{n-1,m}}\}.
\]

The NB-299 projected-dilation estimate, now with the explicit source-side bound (20), gives whenever `\varepsilon_{m,n}<1`,

\[
\boxed{
\|\Xi_{m,n,Z}\|
\le
\|K_{n-1,Z}\|
\frac{
\left(m^{-\delta_Z}+\varepsilon_{m,n}\right)^2
}{
1-\varepsilon_{m,n}^2
}.
}
\tag{23}
\]

Consequently, for a moving family `(Z_X,n_X,m_X)`, if

\[
\frac{m_X}{(n_X-1)^{5/2}}\to\infty
\]

and

\[
\delta_{Z_X}\log m_X\to\infty,
\]

then

\[
\boxed{
\frac{
\|\Xi_{m_X,n_X,Z_X}\|
}{
\|K_{n_X-1,Z_X}\|
}
\to0.
}
\tag{24}
\]

Thus the source-overlap escape hatch left by NB-299 is impossible throughout this larger polynomial region.

## 8. What this rules out, and what it does not

NB-300 showed that source overlap vanishes once the dilation outruns the exponential common-period scale. NB-301 reduced this to the cubic scale by recovering coefficients from early reciprocal shells. Equation (22) improves the sufficient scale again:

\[
\text{lcm scale}
\quad\rightsquigarrow\quad
N^3
\quad\rightsquigarrow\quad
N^{5/2}.
\]

The improvement is genuinely arithmetic: it uses exact residue correlations and the fact that the *quadratic* tail sees only pairwise common periods.

Several limitations remain essential.

1. This is still a **source-side** estimate. It does not imply `d_N->0`, the Nyman--Beurling criterion, or RH.
2. It does not compare `\Xi` to the unresolved tail Gram `E`; that quantity may shrink simultaneously.
3. It does not remove sample conditioning or target-occupation issues in the remaining first-free interpolation problem.
4. The exponent `5/2` is **not claimed optimal**. The term `6N^5/m^2` comes from taking absolute values of all pairwise periodic phase errors. Cancellation among those errors, or a target-aware estimate, could lower the threshold further.
5. No RH-type assumption enters the argument. The only off-critical hypothesis in (23)--(24) is the explicit positive displacement `\delta_Z`, exactly as in NB-294--NB-300.

The next discriminating target is therefore the phase-error term in (19). A useful further advance would either prove cancellation in the matrix of pairwise periodic remainders and beat `N^5/m^2`, or show that the actual first-free target sees substantially less than the operator-norm worst case. Merely refining the global lcm argument would no longer address the active bottleneck.

## 9. Prior-art and source policy

A fresh audit was made against Nyman--Beurling Gram literature, gcd/Jordan-totient matrix identities, fractional-part covariance formulas, and recent work on Gram decay/compressibility. The ingredients used above -- periodic residue averages, Möbius inversion, the Jordan-totient identity, Abel summation, and elementary divisor bounds -- are classical. The audit did not locate this exact moving-cutoff estimate obtained by combining the reciprocal-shell model with pairwise-period quadratic tail control.

No external theorem is load-bearing: every identity and inequality needed for (19)--(24) is derived above or inherited from the already-reviewed internal chain NB-299--NB-301. Therefore `SOURCES.md` is unchanged, and no novelty claim is made for the classical arithmetic identities themselves.

## 10. Adversarial review

The main failure modes were checked explicitly.

- **Complex coefficients.** Equation (6) uses `a_i conjugate(a_j)`; the covariance matrix and Jordan-totient decomposition remain Hermitian positive semidefinite. No real-coefficient restriction is used.
- **Period mistake.** The sequence `r_i(k)r_j(k)` has period `lcm(i,j)`, which is at most `ij`; the argument never substitutes a period for the full vector `u_k`.
- **Weighted-tail phase.** The error in (15) is uniform in the starting index `m`; it follows from shifted partial sums of a mean-zero periodic sequence and Abel summation.
- **Mean term.** The Cesàro mean is not silently assumed small. It is controlled separately by a finite average over `N^2` early shells plus the explicit incomplete-period error (12).
- **Quantifiers.** Equation (22) is a sufficient moving-family statement. It does not assert decay when `m` is merely comparable to `N^{5/2}`.
- **Optimality.** The proof loses cancellation in the phase-error matrix. The exponent `5/2` is therefore recorded only as the current rigorous sufficient scale.
- **Target relevance.** Passing from (20) to (23) uses the established NB-299/300 projected-dilation comparison. No direct conclusion about the original Nyman distance is inferred.

The result survives these checks and gives a strict quantitative improvement of the source-compression frontier established by NB-301.