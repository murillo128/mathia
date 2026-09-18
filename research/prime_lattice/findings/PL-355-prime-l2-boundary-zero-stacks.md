# PL-355 — ℓ² prime completion admits boundary Blaschke zero stacks; the critical kernel is classical Dirichlet/Brownian geometry

**Status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

**Parent finding:** `PL-354`.

`PL-354` proves that an infinite stack of distinct exact real evaluations kills every finite-support prime coefficient vector. The most canonical escape is to complete the degree-one prime sector from finite support to `ℓ²(P)`. That escape is real, but it is not new and it does not by itself produce RH rigidity.

Let

\[
\mathcal P^2_0
:=
\left\{F_c(s)=\sum_p c_p p^{-s}: c=(c_p)_p\in\ell^2(\mathcal P)\right\},
\qquad
\|F_c\|=\|c\|_2.
\tag{1}
\]

This is the zero-constant part of Seip's space `\mathscr D_\infty`, i.e. the first homogeneous/prime-supported sector of the Hardy space of Dirichlet series. Point evaluation is continuous exactly for `Re s>1/2`; nevertheless there are nonzero functions in (1) with infinitely many prescribed real zeros accumulating at `1/2`. In particular, the sequence

\[
\sigma_j=\frac12+2^{-j}
\tag{2}
\]

is the zero set of a nontrivial prime-supported `ℓ²` Dirichlet series. More generally, every bounded real sequence in `Re s>1/2` satisfying the half-plane Blaschke condition is admitted by Seip's `\alpha=\infty` construction. Thus the finite-support rigidity of `PL-354` disappears abruptly under the natural Hilbert completion.

The same completion has reproducing kernel

\[
K(s,w)=\sum_p p^{-s-\bar w}=P(s+\bar w),
\tag{3}
\]

where `P` is the prime zeta function. On real points approaching the critical boundary on the logarithmic scale

\[
\sigma_u=\frac12+e^{-u},
\qquad
\sigma_v=\frac12+e^{-v},
\tag{4}
\]

one has

\[
K(\sigma_u,\sigma_v)
=
\min(u,v)+O(1).
\tag{5}
\]

The leading kernel is therefore the Brownian covariance kernel. This boundary geometry is also prior art in zeta probability: Vassaux's Brownian limit for horizontal approaches to the critical line is driven by the same prime covariance. Consequently neither the existence of boundary zero stacks nor the Brownian `min` kernel can be promoted as a new prime-lattice mechanism for RH.

## 1. The completed degree-one prime sector and its evaluation boundary

For `s=\sigma+it` with `\sigma>1/2`, Cauchy–Schwarz gives

\[
|F_c(s)|
\le
\|c\|_2
\left(\sum_p p^{-2\sigma}\right)^{1/2}.
\tag{6}
\]

Hence evaluation is represented by

\[
k_s=(p^{-\bar s})_p\in\ell^2(\mathcal P),
\qquad
K(s,w)=\langle k_w,k_s\rangle=P(s+\bar w).
\tag{7}
\]

The threshold is exact:

\[
\|k_\sigma\|^2=P(2\sigma)<\infty
\iff
\sigma>\frac12.
\tag{8}
\]

So `1/2` is already the natural evaluation boundary of the completed prime first chaos. This is standard Hardy/Dirichlet-series geometry; it is not evidence for RH by itself.

The completion does retain one elementary rigidity from `PL-354`. Suppose `c\ne0` and `F_c` has infinitely many distinct real zeros `\sigma_j>1/2`. Interior accumulation is impossible by holomorphy. Unbounded real zeros are also impossible: let `p_0` be the least prime with `c_{p_0}\ne0`. Then

\[
p_0^\sigma F_c(\sigma)
=
c_{p_0}
+
\sum_{p>p_0}c_p\left(\frac{p_0}{p}\right)^\sigma.
\tag{9}
\]

Fix `\sigma_0>1/2`. For `\sigma\ge\sigma_0`, the tail is bounded by

\[
\|c_{>p_0}\|_2
\left(
\sum_{p>p_0}
\left(\frac{p_0}{p}\right)^{2\sigma}
\right)^{1/2}.
\tag{10}
\]

The summand is dominated by the summable sequence `(p_0/p)^{2\sigma_0}` and tends pointwise to zero, so dominated convergence makes (10) tend to zero. Therefore (9) tends to `c_{p_0}\ne0`, and `F_c(\sigma)` cannot vanish for arbitrarily large real `\sigma`.

Thus an infinite distinct real zero stack for a nonzero element of `\mathcal P^2_0` can accumulate only at

\[
\boxed{\sigma=\frac12.}
\tag{11}
\]

This is the precise way in which completion changes `PL-354`: finite support makes every infinite exact real stack fatal, whereas `ℓ²` support permits one escape channel, accumulation at the evaluation boundary.

## 2. Seip already classifies the relevant completed zero-set problem

Seip defines

\[
\mathscr D_\infty
=
\left\{
\sum_n a_n n^{-s}\in\mathscr H^2:
 a_n=0\ \text{unless }n=1\text{ or }n\text{ is prime}
\right\}.
\tag{12}
\]

For bounded sequences `S` in `Re s>1/2`, his Theorem 2 gives, at `\alpha=\infty`,

\[
S\text{ is a zero set for a nontrivial }\mathscr D_\infty\text{ function}
\iff
S\in Z\bigl(D_1(\mathbb C^+_{1/2})\bigr),
\tag{13}
\]

where `D_1` is the classical Dirichlet space of the half-plane. In particular, for sequences contained in a non-tangential cone

\[
|t-t_0|\le c(\sigma-1/2),
\tag{14}
\]

Carleson's zero-set result implies that the ordinary half-plane Blaschke condition is sufficient for membership in `Z(D_1)`. Every real sequence approaching `1/2` lies in such a cone with `t_0=0`.

There is a small but important support issue: (12) allows a constant coefficient, while the coefficient problem in `PL-354` is homogeneous and prime-supported. Seip's proof removes that issue. His Lemma 5 constructs the approximating Dirichlet series in the tail form

\[
F(s)=\sum_{n=N}^{\infty}a_n n^{-s}
\tag{15}
\]

for arbitrary sufficiently large `N`, and the final iteration proving Theorem 2 uses these tail approximants. Taking `\alpha=\infty` and `N\ge2`, membership in `\mathscr D_\infty` forces every surviving index in (15) to be a prime. Hence the resulting nontrivial zero-set function has the form

\[
F(s)=\sum_{p\ge N}c_p p^{-s},
\qquad
(c_p)_p\in\ell^2,
\tag{16}
\]

with no constant term.

For a bounded real sequence, the half-plane Blaschke condition is simply

\[
\sum_j(\sigma_j-1/2)<\infty.
\tag{17}
\]

Therefore the explicit sequence (2) satisfies the condition, and Seip's construction yields a nonzero `F\in\mathcal P^2_0` with

\[
F\left(\frac12+2^{-j}\right)=0
\qquad(j\ge1).
\tag{18}
\]

This is a decisive control on the live escape left by `PL-354`: an infinite exact real evaluation stack does **not** remain rigid after the natural `ℓ²` completion. The only possible accumulation point identified in (11) is not merely a logical loophole; classical zero-set theory actually fills it with nontrivial prime-supported functions.

## 3. The boundary Gram kernel is asymptotically Brownian

The prime zeta identity in its legitimate half-plane is

\[
\log\zeta(s)
=
\sum_{m\ge1}\frac{P(ms)}m,
\qquad \Re s>1.
\tag{19}
\]

As `s=1+\varepsilon\downarrow1`, the terms with `m\ge2` remain uniformly bounded, while

\[
\log\zeta(1+\varepsilon)
=
\log(1/\varepsilon)+O(1).
\tag{20}
\]

Hence

\[
P(1+\varepsilon)
=
\log(1/\varepsilon)+O(1).
\tag{21}
\]

No continuation through `Re s=1` is being used here: every identity above is evaluated from the right of the Euler-product boundary.

Applying (21) to (3)--(4),

\[
\begin{aligned}
K(\sigma_u,\sigma_v)
&=P(1+e^{-u}+e^{-v})\\
&=\log\frac1{e^{-u}+e^{-v}}+O(1)\\
&=\min(u,v)-\log(1+e^{-|u-v|})+O(1)\\
&=\boxed{\min(u,v)+O(1)}.
\end{aligned}
\tag{22}
\]

The leading radial Gram kernel is therefore exactly the covariance kernel of one-dimensional Brownian motion after the logarithmic boundary-time change `u=-\log(\sigma-1/2)`.

This does not make `\mathcal P^2_0` a stochastic process. It says that its deterministic reproducing-kernel geometry has Brownian leading order at the critical boundary. The same prime covariance is already visible in modern probabilistic zeta theory. Vassaux considers

\[
\sigma_i=\frac12+(\log T)^{-\alpha_i}
\tag{23}
\]

and reduces the finite-dimensional Brownian limit of horizontal samples of `\log\zeta` to the prime covariance

\[
\sum_{p\le T}p^{-(\sigma_i+\sigma_j)}
\sim
(1\wedge\alpha_i\wedge\alpha_j)\log\log T.
\tag{24}
\]

Thus (22) is the untruncated RKHS counterpart of an already-known Brownian prime-sum mechanism, not a new route from exponent-lattice geometry to the zeta zero divisor.

## 4. Adversarial controls and boundaries

The finding does **not** say that every sequence accumulating at `1/2` is a zero set of a pure-prime `ℓ²` series. For general `D_1` zero sets the classification is subtler. The exact positive statement used here is the cone/real Blaschke class, which already supplies a large explicit family and is enough to falsify any blanket extension of `PL-354` from finite support to `ℓ²` support.

The finding also does not identify the zeros of a particular canonical prime-supported Dirichlet series with the Riemann zeros. Seip's theorem is an existence/interpolation theorem: coefficients are free variables chosen to realize the prescribed zero set. This flexibility is therefore a negative control under the line mandate. It shows that the ambient completed first-chaos geometry can manufacture critical-boundary zero stacks without importing the Euler product, functional equation, Möbius signs, or the exact Riemann zero divisor.

Likewise, the Brownian kernel (22) is driven only by the universal first-order singularity of the prime zeta function at `1`. It does not survive as a discriminator for the exact rational-prime zeta problem: the probabilistic literature already sees the same covariance before any RH-sensitive localization mechanism is supplied.

Finally, (11) concerns **real** evaluation points. Complex zero patterns of general prime-supported Hardy-Dirichlet functions have additional almost-periodic structure and are not classified here. The purpose of (11) is only to identify exactly where the real-stack escape from `PL-354` can live and then compare that escape with the classical zero-set theorem.

## 5. Prior art and novelty assessment

The load-bearing prior art is:

- Kristian Seip, *Zeros of functions in Hilbert spaces of Dirichlet series*, Math. Z. 274 (2013), 1327--1339; arXiv:1206.2815v2. Definition of `\mathscr D_\infty`, Theorem 2 (`\alpha=\infty`), Lemma 5 tail-supported approximation, and the cone/Dirichlet-space zero-set discussion provide (12)--(18).
- Louis Vassaux, *Brownian behaviour of the Riemann zeta function around the critical line*, arXiv:2505.07352v2 (1 June 2026). Theorem 1.1 and the prime-covariance reduction (2.8) provide the direct prior-art comparison for (22)--(24).
- Classical prime-zeta/Euler-product theory supplies (19)--(21).

What is derived here is the exact bridge back to the `PL-354` coefficient-stack problem: the least-prime argument localizes any infinite real zero stack to the `1/2` boundary; Seip's tail-supported `\alpha=\infty` construction then shows that this boundary escape genuinely exists even after imposing zero constant term; and the corresponding prime reproducing kernel is identified with the same Brownian covariance already present in current zeta probability. The organization is useful for this line, but none of the underlying zero-set or Brownian phenomena is claimed as new mathematics.

## Research consequence

The canonical Hilbert completion of the finite prime-axis coefficient problem is now classified far enough to rule it out as an RH mechanism by itself. The transition is

\[
\text{finite prime support}
\quad\xrightarrow{\text{completion}}\quad
\ell^2(\mathcal P),
\tag{25}
\]

and the qualitative behavior changes from `PL-354`'s exact infinite-stack rigidity to classical boundary zero-set flexibility. In particular, no argument of the form

\[
\text{infinitely many exact real evaluations}
\Longrightarrow
c=0
\tag{26}
\]

can survive on the full `\ell^2` prime first chaos when the evaluations approach `1/2`.

A live RH-facing mechanism must therefore add structure that Seip's interpolation freedom does not preserve: a canonical arithmetic source, higher/mixed exponent degrees, Möbius or Euler-product compatibility, a target-relative Nyman/Weil constraint, the global functional equation, or another exact coupling that prevents arbitrary `D_1`-type boundary zero interpolation. Merely completing the prime-axis coefficients, or exploiting the Brownian critical-boundary kernel of that completion, is insufficient.