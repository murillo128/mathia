# MC-170 — Stationary scalar heat-orbit statistics erase the Möbius prime phase

**Status:** `EXACT-DERIVED`, `CLASSICAL-HARMONIC-ANALYSIS`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue from the square-free heat orbit of `MC-169`, but replace the fixed Möbius sign at each prime by an arbitrary unimodular prime phase. For

\[
z=(z_p)_{p\in\mathcal P}\in\mathbb T^{\mathcal P},
\qquad
\chi_z(n):=\prod_p z_p^{v_p(n)},
\]

put

\[
\Theta_z(\beta,t)
:=
\sum_{n\ge1}\mu(n)^2\chi_z(n)
 e^{-\beta(\log n)^2}n^{-it},
\qquad \beta>0.
\tag{1}
\]

The Möbius orbit is the special point `z_p=-1` for every prime, because

\[
\mu(n)=\mu(n)^2(-1)^{\omega(n)},
\]

while `z_p=1` gives the all-plus square-free control from `MC-169`.

For every fixed `\beta>0`, the scalar orbit `(1)` has the following exact phase-blindness property:

\[
\boxed{
\text{every continuous stationary long-time statistic built from finitely many }
\Theta_z(\beta_j,t+\tau_j)
\text{ is independent of }z.
}
\tag{2}
\]

More precisely, fix `k`, numbers `\beta_j>0`, shifts `\tau_j\in\mathbb R`, and a continuous function `\Phi:\mathbb C^k\to\mathbb C`. Then

\[
\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}
\Phi\!\left(
\Theta_z(\beta_1,t+\tau_1),\ldots,
\Theta_z(\beta_k,t+\tau_k)
\right)dt
\tag{3}
\]

exists and has the same value for every prime-phase vector `z`.

The same orbit-density mechanism also gives the exact worst-time identity

\[
\boxed{
\sup_{t\in\mathbb R}|\Theta_z(\beta,t)|
=
\sum_{n\ge1}\mu(n)^2e^{-\beta(\log n)^2},
}
\tag{4}
\]

again for every `z`. Thus the two most obvious ways to aggregate the time orbit destroy the distinction needed by the pointwise criterion in `MC-169`:

- stationary long-time averages forget the starting prime phase;
- the all-time supremum allows the Kronecker flow to approach complete phase alignment and therefore recovers the phase-free worst case.

A particularly sharp quantitative consequence is that the Besicovitch mean-square norm has the **same numerical small-`\beta` exponent `1/16`** that appears as the RH-critical pointwise exponent in `MC-169`, but here it is unconditional and phase-blind:

\[
\boxed{
\lim_{\beta\downarrow0}
\beta\log
\left(
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^{T}|\Theta_z(\beta,t)|^2dt
\right)^{1/2}
=
\frac1{16}
}
\tag{5}
\]

for every `z`. By contrast, `(4)` has unconditional type `1/4`:

\[
\boxed{
\lim_{\beta\downarrow0}
\beta\log\sup_t|\Theta_z(\beta,t)|
=
\frac14.
}
\tag{6}
\]

Hence the constant `1/16` by itself is not a Möbius/RH discriminator. In `MC-169` its significance comes from the **quantifier topology**: first fix `t`, then take `\beta\downarrow0`, for every fixed `t`. Replacing that family of anchored pointwise conditions by a stationary time mean makes the same exponent arise from ordinary square-free support and Hilbert-space squaring.

## 1. Bohr lift of the prime-phase heat orbit

For fixed `\beta>0`, define on the infinite prime torus

\[
F_\beta(w)
:=
\sum_{n\ge1}\mu(n)^2\chi_w(n)e^{-\beta(\log n)^2},
\qquad
w\in\mathbb T^{\mathcal P}.
\tag{7}
\]

Because

\[
\sum_{n\ge1}e^{-\beta(\log n)^2}<\infty,
\tag{8}
\]

`(7)` converges uniformly and absolutely in `w`; therefore `F_\beta` is continuous.

Let

\[
R_t(w)_p:=w_p p^{-it}.
\tag{9}
\]

Complete multiplicativity gives the exact identity

\[
\Theta_z(\beta,t)=F_\beta(R_tz).
\tag{10}
\]

This is the standard Bohr/vertical-limit representation of a Dirichlet series, here applied to the absolutely convergent Gaussian heat coefficients.

## 2. The prime-log flow is dense and uniquely averaging

For distinct primes `p_1,\ldots,p_r`, any integer relation

\[
\sum_{j=1}^r m_j\log p_j=0
\]

would imply

\[
\prod_{j=1}^r p_j^{m_j}=1,
\]

so unique factorization forces every `m_j=0`. Thus every finite set of prime logarithms is rationally independent.

Kronecker's theorem therefore makes the finite projection

\[
t\longmapsto(p_1^{-it},\ldots,p_r^{-it})
\]

dense in `\mathbb T^r`. Since the product topology on `\mathbb T^{\mathcal P}` is determined by finite coordinate projections, the full one-parameter subgroup `R_t1` is dense in the infinite torus. Multiplication by a fixed `z` shows that every orbit `R_tz` is dense as well.

The required averaging statement can be proved directly, without importing any arithmetic estimate. A character of the infinite torus has finite support:

\[
\Xi_m(w)=\prod_p w_p^{m_p},
\qquad m_p\in\mathbb Z,
\quad m_p=0\text{ for all but finitely many }p.
\]

Along the flow,

\[
\Xi_m(R_tz)
=
\Xi_m(z)
 e^{-it\sum_p m_p\log p}.
\]

If `m\ne0`, rational independence gives a nonzero frequency, hence

\[
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^{T}\Xi_m(R_tz)dt=0.
\tag{11}
\]

The trivial character averages to `1`. Finite-coordinate trigonometric polynomials are uniformly dense in the continuous functions on the compact infinite torus, so `(11)` extends to every continuous `G`:

\[
\boxed{
\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}G(R_tz)dt
=
\int_{\mathbb T^{\mathcal P}}G(w)\,dm_\infty(w),
}
\tag{12}
\]

where `m_\infty` is Haar measure. In particular the limit is independent of `z`.

For `(3)`, simply take

\[
G(w)=
\Phi\!\left(
F_{\beta_1}(R_{\tau_1}w),\ldots,
F_{\beta_k}(R_{\tau_k}w)
\right),
\]

which is continuous. This proves `(2)`.

## 3. Closed orbit ranges and the worst-time phase alignment

Density also determines the closure of the scalar orbit:

\[
\overline{\{\Theta_z(\beta,t):t\in\mathbb R\}}
=
F_\beta(\mathbb T^{\mathcal P}),
\tag{13}
\]

independently of `z`. Hence any continuous extremal statistic of the closed orbit range is phase-blind as well.

The triangle inequality gives

\[
|F_\beta(w)|
\le
\sum_n\mu(n)^2e^{-\beta(\log n)^2},
\]

and equality is attained at the all-plus torus point `w_p=1`. Since every orbit is dense, `(4)` follows. Notice the quantifiers: the aligning time may depend on `\beta`; no single fixed `t` is asserted to align the phases as `\beta\downarrow0`.

Using the square-free counting law

\[
Q(x)=\sum_{n\le x}\mu(n)^2
=\frac6{\pi^2}x+O(\sqrt x),
\tag{14}
\]

Abel summation reduces the exponential scale of the right side of `(4)` to

\[
\int_1^\infty e^{-\beta(\log x)^2}\,dx
=
\int_0^\infty e^{u-\beta u^2}\,du.
\tag{15}
\]

The saddle is at `u=1/(2\beta)` and has exponent `1/(4\beta)`. The `O(\sqrt x)` error in `(14)` has strictly smaller exponential type. This proves `(6)`.

## 4. Every stationary mixed moment loses the prime phase

The general Haar argument already proves phase blindness, but polynomial moments make the arithmetic cancellation mechanism explicit. Absolute convergence permits termwise expansion. For example, a mixed monomial contains a time phase

\[
\exp\!\left(
-it\left[
\sum_{j=1}^r\log n_j-
\sum_{\ell=1}^s\log m_\ell
\right]
\right).
\]

Its long-time average is zero unless

\[
\prod_{j=1}^r n_j
=
\prod_{\ell=1}^s m_\ell.
\tag{16}
\]

On every surviving resonance, complete multiplicativity gives

\[
\frac{\prod_j\chi_z(n_j)}{\prod_\ell\chi_z(m_\ell)}=1.
\tag{17}
\]

Thus the prime phase cancels exactly on the resonant set selected by time averaging.

The two-point correlation therefore has the concrete phase-free form

\[
\boxed{
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^{T}
\Theta_z(\beta,t+\tau)
\overline{\Theta_z(\gamma,t)}dt
=
\sum_{n\ge1}\mu(n)^2
 e^{-(\beta+\gamma)(\log n)^2}n^{-i\tau}.
}
\tag{18}
\]

At `\gamma=\beta` and `\tau=0`, this is Parseval's mean-square identity

\[
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^{T}|\Theta_z(\beta,t)|^2dt
=
\sum_n\mu(n)^2e^{-2\beta(\log n)^2}.
\tag{19}
\]

Equation `(19)` contains no Möbius orientation at all.

## 5. Why the phase-blind mean has critical-looking type `1/16`

Apply `(14)` again to the right side of `(19)`. Its main exponential scale is

\[
\int_0^\infty e^{u-2\beta u^2}\,du,
\]

whose saddle is `u=1/(4\beta)` with exponent `1/(8\beta)`. Therefore

\[
\lim_{\beta\downarrow0}
\beta\log
\left(
\sum_n\mu(n)^2e^{-2\beta(\log n)^2}
\right)
=
\frac18.
\tag{20}
\]

Taking the square root gives `(5)`.

This creates a useful matched-control warning for `MC-169`. There, the fixed-`t` pointwise demand

\[
\limsup_{\beta\downarrow0}
\beta\log^+|\Theta_\mu(\beta,t)|\le\frac1{16}
\qquad\text{for every fixed }t
\]

is RH-equivalent. Here the long-time `L^2` norm also has type exactly `1/16`, but it does so for **every** prime-phase deformation, including the all-plus square-free control. The equality of constants comes from two unrelated operations: Gaussian saddle conversion of a `1/2` Mertens exponent in the first case, and square-rooting a support-density mean square in the second.

Therefore a future heat argument cannot treat the appearance of `1/16` in a stationary Hilbert norm as latent RH information. It must preserve the anchored prime orientation through the relevant order of limits.

## Prior art and novelty audit

The ambient harmonic-analysis mechanism is classical. Bohr's correspondence identifies Dirichlet series with power series on the prime polytorus, and modern Hardy-space treatments identify `\mathbb T^\infty` with the character group of the positive rationals using unique prime factorization. For a recent explicit formulation, see Nikolaos Kouroupis, *Composition operators on weighted Hilbert spaces of Dirichlet series*, **Journal of the London Mathematical Society** 107 (2023), DOI `10.1112/jlms.12771`, §2.1.

The vertical-line/Kronecker-flow interpretation of mean values of Dirichlet series is likewise standard. Meredith Sargent, *Carlson's theorem for different measures*, **Journal of Mathematical Analysis and Applications** 466 (2018), 1410–1425, DOI `10.1016/j.jmaa.2018.06.054`, explicitly presents vertical translation as an ergodic flow on the infinite polytorus and interprets Carlson-type mean identities through that correspondence.

The Bost–Connes/Riemann-gas heat object itself is the source construction already audited in `MC-169`: Greenfield, Marcolli and Teh establish the relevant `\theta`-summable spectral-triple framework. The square-free counting law and Parseval/Carlson mean-square mechanism are classical.

The statements above are therefore recorded as an **exact specialization and obstruction for the current Mathia heat route**, not as a new theorem of harmonic analysis. A targeted search did not locate a primary source packaging this particular Möbius prime-phase family together with the contrast `(5)` versus the pointwise `MC-169` threshold, but search absence is not evidence of novelty and no novelty claim is made.

## Boundaries and falsification tests

- The order of limits is essential. Statements `(2)`, `(5)` and `(18)` first keep every `\beta_j>0` fixed and send `T\to\infty`. They do **not** control a coupled horizon `T=T(\beta)` as `\beta\downarrow0`. Quantitative failure of equidistribution on a moving, increasingly complex scale is a genuine possible escape.
- Finite-`T` averages need not be phase-blind: off-diagonal frequency terms survive before the long-time limit.
- Anchored or explicitly nonstationary functionals of time are outside `(2)` when their time weight prevents reduction to Haar averaging of one orbit translate.
- Operator-valued or crossed-product observables that do not factor through finitely many scalar heat traces are not classified here.
- The control family is **multiplicative prime-phase deformation**. For arbitrary unrelated phases assigned independently to each integer, a product resonance `(16)` need not cancel the phase as in `(17)`.
- Equation `(4)` does not produce one universal aligning time. It says only that the supremum over the dense orbit equals the torus maximum for each fixed `\beta`.
- The unconditional `1/16` in `(5)` is not a contradiction with the RH equivalence in `MC-169`; the two statements use different functionals and different quantifier order.
- Nothing here excludes a quantitative moving-window statistic, a nonstationary cross-scale coupling, or a source-forced operator relation that preserves orientation before the Haar/resonance quotient. Such a candidate must state explicitly which step above it avoids.

## Consequence for the line

`MC-169` left open whether averaging over the time orbit might turn the convergent heat family into a cheaper quantitative object. The exact Bohr/Kronecker reduction closes the fully stationary scalar version of that escape.

The heat route now has a three-way classification:

1. **fixed time, small heat scale:** critical type `1/16` is RH-equivalent (`MC-169`);
2. **stationary long-time Hilbert mean:** type `1/16` is unconditional and prime-phase blind (`MC-170`);
3. **worst time at each heat scale:** type `1/4` is unconditional because the dense orbit approaches phase alignment (`MC-170`).

A surviving time-dependent Bost–Connes mechanism must therefore retain information in the missing middle: a quantitative finite/moving time scale, an anchored nonstationary relation, or a genuinely non-scalar source operation. Merely replacing the pointwise orbit by a stationary average or a time supremum cannot supply a cheaper Mertens transfer.