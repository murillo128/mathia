# MC-017 — Mertens path energy is a boundary-cancelled inverse-frequency Fourier energy

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `CANDIDATE-NEW-STRUCTURE`.

## Claim

The amplitude-sensitive carrier isolated in `MC-016`,

\[
V_a(N)=\sum_{k=1}^{N-1}|A(k)|^2,
\qquad
A(k)=\sum_{n\le k}a(n),
\]

has an exact Fourier representation that exposes where its information lives. Define

\[
F_N(t)=\sum_{n=1}^{N-1}a(n)e^{2\pi i nt},
\qquad
B_N=A(N-1),
\]

and the **boundary-cancelled Fourier polynomial**

\[
H_N(t)=F_N(t)-B_Ne^{2\pi iNt}.
\]

Then

\[
\boxed{
V_a(N)
=
\int_0^1
\frac{|H_N(t)|^2}{|1-e^{2\pi it}|^2}\,dt
=
\int_0^1
\frac{|F_N(t)-B_Ne^{2\pi iNt}|^2}{4\sin^2(\pi t)}\,dt .}
\tag{1}
\]

The apparent singularity at `t=0` is removable because `H_N(0)=0`. Thus the all-prefix quadratic path energy is exactly a low-frequency-amplified `L^2` norm: the summation operator contributes the multiplier `(1-e^{2 pi i t})^{-1}`, while the endpoint subtraction is forced by the finite boundary.

This gives a decisive matched-support negative result for ordinary Fourier `L^2` information. Let

\[
q(n)=\mu(n)^2,
\qquad
Q(x)=\sum_{n\le x}q(n)=\frac{6}{\pi^2}x+O(\sqrt x).
\]

For **every** sign assignment `a(n) in {-1,0,1}` with `|a(n)|=q(n)`, Parseval gives the identical unweighted mass

\[
\int_0^1|F_N(t)|^2dt=Q(N-1).
\tag{2}
\]

Yet two exact-support controls have different path-energy exponents:

- for the all-positive sequence `a(n)=q(n)`,
  \[
  V_q(N)=\sum_{k<N}Q(k)^2
  =\frac{12}{\pi^4}N^3+O(N^{5/2});
  \tag{3}
  \]
- for the support-matched independent-sign sequence `a(n)=q(n)\varepsilon_n` of `MC-016`,
  \[
  \mathbb E V_a(N)=\sum_{k<N}Q(k)
  =\frac{3}{\pi^2}N^2+O(N^{3/2}).
  \tag{4}
  \]

Therefore the ordinary global Fourier `L^2` norm is **structurally blind to the cancellation distinction relevant to `V_a`**, even after exact square-free support is fixed. The missing information is not total Fourier energy; it is how phase coherence is distributed near the zero frequency after the endpoint mode is removed and the inverse-square summation weight is restored.

For Möbius itself, (1) gives

\[
V_M(N)=\sum_{k<N}M(k)^2
=\int_0^1
\frac{|S_{N-1}(t)-M(N-1)e^{2\pi iNt}|^2}{4\sin^2(\pi t)}dt,
\tag{5}
\]

where `S_{N-1}(t)=sum_{n<N} mu(n)e^{2 pi i n t}`. Combined with the already exact transfer from `MC-016`,

\[
D_M(N)^2\le \frac{V_M(N)}{N},
\tag{6}
\]

a bound `V_M(N) <<_epsilon N^(2+epsilon)` is an amplitude-sensitive `L^2` route to the RH-scale mean-absolute target without requiring pointwise control of every `M(k)`.

The new information here is not that partial summation has a Fourier multiplier; that is classical harmonic analysis. The line-specific result is the exact finite-boundary identity (1), the exact-support `L^2` blindness control (2)–(4), and the resulting localization of the unresolved arithmetic burden in a boundary-cancelled inverse-frequency energy.

## 1. Exact derivation of the Fourier identity

Let

\[
G_N(t)=\sum_{k=1}^{N-1}A(k)e^{2\pi i kt}.
\]

A finite telescoping calculation gives

\[
\begin{aligned}
(1-e^{2\pi it})G_N(t)
&=\sum_{k=1}^{N-1}A(k)e^{2\pi i kt}
 -\sum_{k=1}^{N-1}A(k)e^{2\pi i(k+1)t}\\
&=\sum_{n=1}^{N-1}a(n)e^{2\pi i nt}
 -A(N-1)e^{2\pi iNt}\\
&=H_N(t).
\end{aligned}
\tag{7}
\]

At `t=0`, both sides vanish; away from zero,

\[
G_N(t)=\frac{H_N(t)}{1-e^{2\pi it}}.
\tag{8}
\]

Since `G_N` is a finite trigonometric polynomial, Parseval gives

\[
\int_0^1|G_N(t)|^2dt=\sum_{k=1}^{N-1}|A(k)|^2=V_a(N).
\tag{9}
\]

Substituting (8) into (9) proves (1). The quotient extends continuously across `t=0` because it is identically the polynomial `G_N` there; no principal value or regularization is involved.

Expanding the right side of (9) in the coefficient variables reproduces the signed all-shift/all-prefix identity recorded in `MC-016`. Thus the correlation aggregate and the inverse-frequency Fourier energy are not two assumptions: they are two exact coordinate descriptions of the same carrier.

## 2. Ordinary global Fourier L2 loses all sign information

For any coefficient sequence,

\[
\int_0^1|F_N(t)|^2dt=\sum_{n<N}|a(n)|^2.
\tag{10}
\]

If `|a(n)|=q(n)=mu(n)^2`, the right side is `Q(N-1)` independently of every sign. In particular, actual Möbius, the all-positive square-free indicator, and every support-matched random-sign realization have exactly the same value in (10).

The path energy is radically different. For the all-positive control, `A(k)=Q(k)`, so using `Q(k)=c k+O(sqrt(k))` with `c=6/pi^2`,

\[
\sum_{k<N}Q(k)^2
=c^2\sum_{k<N}k^2+O\left(\sum_{k<N}k^{3/2}\right)
=\frac{c^2}{3}N^3+O(N^{5/2}),
\]

which is (3). For the independent-sign exact-support model, independence and centering give

\[
\mathbb E|A(k)|^2=Q(k),
\]

and summing in `k` gives (4), in agreement with `MC-016`.

This is a stronger obstruction than saying that Parseval is a coarse statistic in the abstract. It exhibits **matched objects with the exact Möbius support and exactly equal global `L^2` Fourier mass whose cumulative path energies differ by a full factor of order `N`**. Any route using only the scalar norm in (10) has already erased the target discriminator.

## 3. The inverse-square weight identifies a multiscale boundary layer

Write `||t||` for distance from `t` to the nearest integer. For `||t||<=1/2`,

\[
4\,||t||\le |1-e^{2\pi it}|\le2\pi\,||t||.
\tag{11}
\]

Hence away from the removable zero, the weight in (1) is comparable to `||t||^(-2)`. On a dyadic annulus

\[
I_j=\left\{t:\frac{2^j}{N}\le ||t||<\frac{2^{j+1}}{N}\right\},
\tag{12}
\]

as long as the upper endpoint is at most `1/2`, its contribution satisfies

\[
\int_{I_j}\frac{|H_N(t)|^2}{4\sin^2(\pi t)}dt
\asymp
\frac{N^2}{4^j}\int_{I_j}|H_N(t)|^2dt,
\tag{13}
\]

with absolute comparison constants.

This gives a concrete polynomial information budget. A diffusive-scale annular estimate

\[
\int_{I_j}|H_N(t)|^2dt
\ll_\varepsilon N^\varepsilon 2^j
\tag{14}
\]

for every nonempty dyadic annulus contributes at most

\[
\ll_\varepsilon \frac{N^{2+\varepsilon}}{2^j}
\]

to `V_a(N)`, so the annular contributions sum geometrically at the desired `N^(2+epsilon)` scale. One must additionally control the innermost core `||t||<1/N` in the naturally weighted norm from (1); the zero `H_N(0)=0` removes the literal singularity but does not make that core automatic.

Thus the residual question from `MC-016` can be stated without taking absolute values over shifts: **can Möbius arithmetic force diffusive `L^2` mass for the boundary-cancelled polynomial across the low-frequency dyadic hierarchy, including the critical core?** This is more specific than generic Fourier uniformity and exactly preserves the signed cancellations lost in the `MC-006` `l^1` correlation majorant.

## 4. Relation to recent Möbius Fourier-moment prior art

A directly adjacent preprint is Alberto Verjovsky, *Local Moments of Möbius Fourier Polynomials and the Riemann Hypothesis*, arXiv:2607.25002v1 (27 July 2026), https://arxiv.org/abs/2607.25002. It studies

\[
P_N(t)=N^{-1/2}S_N(t)
\]

on the single critical arc `[-c/N,c/N]`. Its Theorem 1.3 proves that RH is equivalent to subpolynomial growth of arbitrarily high finite local moments. More quantitatively, Corollary 3.3 and Remark 3.4 show that one fixed local moment exponent `q` with subpolynomial growth yields only

\[
M(N)=O_\varepsilon\left(N^{1/2+1/(2(q+1))+\varepsilon}\right),
\tag{15}
\]

so fixed `q=2` gives the generic pointwise exponent `2/3+epsilon`; arbitrarily large finite moments are required to recover the `1/2` pointwise boundary through that local moment-to-value argument.

The present carrier is different rather than stronger. It keeps exponent `2` but changes the observable: `H_N`, not `S_N`; inverse-square frequency weighting, not an unweighted local mean; and all dyadic scales, not one critical arc. It also targets the weaker mean-square path quantity `V_M`, from which `D_M` follows by Cauchy–Schwarz, instead of directly reconstructing the single endpoint `M(N)`.

Earlier global Fourier-norm work includes el Houcein el Abdalaoui, *Exponential sums of the Möbius function and flat polynomials*, arXiv:1910.10569, which uses `L^alpha` semi-flatness for `alpha>2` as an RH-relevant condition. The matched-support identity (10) explains why exponent `2` without localization or weighting cannot play the same role: at `L^2`, the norm is fixed solely by the coefficient support.

No novelty is claimed for Parseval, the summation multiplier `(1-e^{2 pi i t})^{-1}`, discrete Hardy/summation-operator language, or the existence of Fourier reformulations of Mertens cancellation. A targeted search found the recent local-moment and global semi-flatness programs above, but the purpose of this finding is narrower: preserve the exact `MC-016` path-energy target and identify the Fourier information layer that distinguishes it from norm data already known to be support-only.

## 5. Boundaries and falsification tests

Equation (1) is an identity for every finite coefficient sequence; by itself it gives no new bound for Möbius and does not make an RH claim. A spectral route is circular if it simply assumes `H_N` has the weighted `L^2` size required to conclude `V_M(N)<<N^(2+epsilon)` without deriving that estimate from independently controlled arithmetic input.

The finding also does not say that low frequency alone in one fixed window is sufficient. The inverse-square norm is multiscale, and the critical core must be controlled in the weighted boundary-cancelled quantity. Replacing it by the ordinary local `L^2` norm of `S_N` loses both the endpoint cancellation and the scale weights.

The all-positive and independent-sign controls falsify any claim that exact square-free support plus global Fourier `L^2` mass explains Mertens cancellation. They do **not** falsify higher moments, localized moments, signed phase information, or multiplicativity-sensitive Fourier estimates.

The decisive continuation test is therefore quantitative: derive (14), or an equivalent summable weighted estimate, for actual Möbius from a source-natural signed/multiplicative theorem whose strength is not already RH-equivalent; alternatively construct a multiplicative exact-support comparator satisfying the proposed Fourier-local inputs while its weighted energy in (1) is superquadratic. The latter would kill this spectralized path-energy interface in the same way `MC-015` and `MC-016` killed overstrong excursion statistics.

## Consequences for the active clue

`MC-016` left the signed all-shift/all-prefix aggregate as the unresolved part of `V_M`. Equation (1) gives that aggregate an exact spectral form. The useful target is no longer vague "Fourier randomness": it is **boundary-cancelled low-frequency `L^2` control with the inverse summation multiplier retained**.

This also sharpens the information hierarchy exposed across the line:

- global unweighted `L^2` is support-only and decisively insufficient;
- one fixed unweighted local `L^2` moment does not reach the pointwise square-root boundary through the known generic local-moment transfer;
- the weighted multiscale `L^2` energy (1) is exactly the amplitude-aware path carrier needed for the mean-absolute route.

The remaining mathematical burden is to find genuinely arithmetic control of that weighted energy, not to invent another Fourier norm around the Möbius coefficients.