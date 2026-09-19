# AF-429 — Supercritical full-column saddle has a shrinking integer window

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `SUPERCRITICAL` · `MOVING-SADDLE` · `SIGNED-RESUMMATION` · `SHRINKING-TARGET` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-418 in the genuinely supercritical regime. Fix `a>0`, let `s_n` be nonnegative integers, and write

\[
q_n=\frac{s_n}{n}\longrightarrow\sigma>2.
\]

For the full-height rectangular partition `lambda=(r^n)`, AF-418 gives the exact normalized magnitude

\[
\boxed{
C_{n,r}^{(s_n)}(a)
=
\left(\frac{a}{n^2}\right)^{rn}
\binom{n+r}{r}^{s_n-1}
\frac{\prod_{j=n+1}^{n+r}\zeta(2j)}{\prod_{j=1}^{r}\zeta(2j)}
\left[
\frac{\prod_{j=n+1}^{n+r}(2j-1)}{\prod_{j=1}^{r}(2j-1)}
\right]^2.
}
\tag{1}
\]

Define the moving scale

\[
\boxed{
R_n=a^{1/q_n}n^{1-2/q_n}.
}
\tag{2}
\]

Then `R_n -> infinity` and `R_n/n -> 0`. For every integer sequence `r_n` with

\[
\frac{r_n}{R_n}\longrightarrow t\in(0,\infty),
\]

one has the exact logarithmic saddle profile

\[
\boxed{
\frac{1}{nR_n}\log C_{n,r_n}^{(s_n)}(a)
\longrightarrow
\sigma t(1-\log t).
}
\tag{3}
\]

The profile has its unique maximum at `t=1`. Hence the fixed-width divergence found in AF-418 is only the left edge of the supercritical picture: the full-height rectangular family develops a moving saddle at width

\[
r\asymp R_n
=a^{1/q_n}n^{1-2/q_n},
\]

with peak logarithmic size

\[
\log C_{n,r}^{(s_n)}(a)
=\sigma nR_n(1+o(1))
\]

for any integer `r/R_n -> 1`.

The discrete saddle is sharper than `(3)` alone shows. The exact adjacent-rectangle ratio is

\[
\boxed{
F_{n,r}:=
\frac{C_{n,r}^{(s_n)}(a)}{C_{n,r-1}^{(s_n)}(a)}
=
\left(\frac{a}{n^2}\right)^n
\left(\frac{n+r}{r}\right)^{s_n-1}
\frac{\zeta(2(n+r))}{\zeta(2r)}
\left(\frac{2(n+r)-1}{2r-1}\right)^2.
}
\tag{4}
\]

Use the right-hand side of `(4)` to define a smooth positive interpolation for real `r>1/2`, and let

\[
\Phi_n(r)=\log F_{n,r}.
\]

Set

\[
\boxed{
\rho_n=\frac{nR_n}{n-R_n}.
}
\tag{5}
\]

For all sufficiently large `n`, `\Phi_n` is strictly decreasing on a neighborhood containing the relevant crossing inside `[R_n/2,2R_n]`, and it has a unique zero `tau_n` there. More precisely,

\[
\boxed{
\tau_n
=
\rho_n
+
\frac{R_n}{q_n n}\log\!\left(\frac{n}{R_n}\right)(1+o(1)).
}
\tag{6}
\]

In particular `tau_n/R_n -> 1` and `tau_n-rho_n -> 0`. Uniformly for real `r` with `|r-tau_n|<=1`,

\[
\boxed{
\Phi_n(r)
=
-\frac{q_n n}{R_n}(r-\tau_n)(1+o(1)).
}
\tag{7}
\]

Therefore adjacent **integer** rectangles near the moving saddle have comparable magnitudes only inside the shrinking window

\[
\boxed{
|r-\tau_n|=O\!\left(\frac{R_n}{n}\right).
}
\tag{8}
\]

Equivalently, an integer rectangle pair can sit at order-one adjacent ratio only if

\[
\boxed{
\operatorname{dist}(\tau_n,\mathbb Z)
=O\!\left(\frac{R_n}{n}\right)
=O\!\left(n^{-2/\sigma+o(1)}\right).
}
\tag{9}
\]

To have `F_{n,r_n}->1` from the rectangle amplitudes themselves, the stronger condition

\[
\operatorname{dist}(\tau_n,\mathbb Z)
=o\!\left(\frac{R_n}{n}\right)
\tag{10}
\]

is necessary along the chosen subsequence, with the nearest integer taken on the appropriate side of the real crossing.

When `n` is odd, the normalized rectangular Cauchy--Binet terms have sign `(-1)^{rn}=(-1)^r`, so adjacent rectangles alternate. Thus `(9)` is a necessary **discrete saddle-lattice gate** for cancellation between the two adjacent full-height rectangles at the supercritical peak. If

\[
\frac{\operatorname{dist}(\tau_n,\mathbb Z)}{R_n/n}\longrightarrow\infty,
\]

then even the nearest adjacent rectangular magnitudes separate without bound, and the rectangular saddle cannot cancel by pairing its two nearest integer widths.

This does not settle the complete signed partition sum. It identifies the exact moving scale and shows that continuous saddle balance does not automatically survive discretization: the required integer resolution is `R_n/n`, which tends to zero.

## 1. Derivation of the moving profile

Because `q_n->sigma>2`, the scale `(2)` satisfies

\[
R_n\to\infty,
\qquad
\frac{R_n}{n}\to0,
\qquad
R_n^{q_n}=a n^{q_n-2}.
\tag{11}
\]

Take `r=r_n~tR_n`. Since `r=o(n)`,

\[
\log\binom{n+r}{r}
=r\log n-\log(r!)+O\!\left(\frac{r^2}{n}\right).
\tag{12}
\]

The zeta block in `(1)` has logarithm `O(1)`: the denominator product converges to a finite nonzero limit because `sum_j log zeta(2j)<infinity`, while the numerator tends uniformly to one on this sublinear window. The odd-distance block contributes

\[
O\!\left(r\log\frac{n}{r}+r\right),
\tag{13}
\]

which is `o(nR_n)`.

Using `(12)` in `(1)`, replacing `s_n-1` by `nq_n` costs only `o(nR_n)`, and the leading logarithm becomes

\[
\begin{aligned}
\log C_{n,r}^{(s_n)}(a)
&=
rn(\log a-2\log n)
+nq_n\bigl(r\log n-\log(r!)\bigr)
+o(nR_n)\\
&=
nq_n\bigl(r\log R_n-\log(r!)\bigr)
+o(nR_n).
\end{aligned}
\tag{14}
\]

Stirling's formula gives

\[
\log(r!)=r\log r-r+O(\log r),
\]

so

\[
\frac{1}{nR_n}\log C_{n,r}^{(s_n)}(a)
=
q_n\frac{r}{R_n}
\left(1+\log\frac{R_n}{r}\right)+o(1),
\]

which proves `(3)`.

The limiting profile

\[
f_\sigma(t)=\sigma t(1-\log t)
\]

has derivative `f'_sigma(t)=-sigma log t`, hence its unique maximum is at `t=1`. This saddle location is a direct consequence of the factorial entropy in the growing rectangle width; no fixed-`r` asymptotic can see it.

## 2. Exact adjacent ratio and the real crossing

Taking the ratio of `(1)` at widths `r` and `r-1` gives `(4)` exactly. The definition `(2)` rewrites its logarithm as

\[
\Phi_n(r)
=
nq_n\log\!\left(\frac{R_n(n+r)}{nr}\right)
+E_n(r),
\tag{15}
\]

where

\[
E_n(r)
=
-\log\!\left(\frac{n+r}{r}\right)
+
\log\!\left(\frac{\zeta(2(n+r))}{\zeta(2r)}\right)
+
2\log\!\left(\frac{2(n+r)-1}{2r-1}\right).
\tag{16}
\]

The point `rho_n` in `(5)` is chosen so that the large term in `(15)` vanishes exactly:

\[
\frac{R_n(n+\rho_n)}{n\rho_n}=1.
\tag{17}
\]

Since `rho_n~R_n`, direct substitution in `(16)` gives

\[
\boxed{
\Phi_n(\rho_n)
=
\log\!\left(\frac{n}{R_n}\right)
+O(R_n^{-1}).
}
\tag{18}
\]

Indeed `(n+rho_n)/rho_n=n/R_n` exactly, the odd-distance ratio equals `(n/R_n)(1+O(R_n^{-1}))`, and the zeta logarithm is exponentially small because `rho_n->infinity`.

Differentiating `(15)` on the real interpolation gives

\[
\Phi_n'(r)
=
-\frac{n^2q_n}{r(n+r)}+O(R_n^{-1})
\tag{19}
\]

uniformly for `r` in a fixed multiplicative neighborhood of `R_n`; the zeta derivative is exponentially small there and the remaining elementary derivatives are `O(R_n^{-1})`. Thus the main term is negative of order `n/R_n`, and in the `o(R_n)` neighborhood of `rho_n`,

\[
\Phi_n'(r)
=-\frac{q_n n}{R_n}(1+o(1)).
\tag{20}
\]

Because `(18)` is positive and

\[
\frac{R_n}{q_n n}\log\frac{n}{R_n}\to0,
\]

the intermediate value theorem and `(20)` give a unique nearby zero. Solving by the mean-value theorem yields `(6)`. Applying the same derivative estimate between that zero and any `r` with `|r-tau_n|<=1` gives `(7)`.

## 3. The integer cancellation window

Equation `(7)` converts a smooth saddle into an exact discretization test. If an integer `r_n` satisfies `|Phi_n(r_n)|=O(1)`, then necessarily

\[
|r_n-\tau_n|=O(R_n/n).
\]

Conversely, any integer in that window has `Phi_n(r_n)=O(1)`. This proves `(8)`--`(9)`.

The window is much narrower than one lattice spacing:

\[
\frac{R_n}{n}
=a^{1/q_n}n^{-2/q_n}
=n^{-2/\sigma+o(1)}\to0.
\tag{21}
\]

Hence the continuous optimizer is not enough: whether two adjacent integer widths are even comparable is an inhomogeneous shrinking-target problem for the fractional part of `tau_n`.

For odd `n`, AF-417's sign `(-1)^{|lambda|}` becomes `(-1)^{rn}=(-1)^r` on `lambda=(r^n)`. Therefore neighboring rectangles can cancel only if their magnitudes first pass `(9)`. Condition `(9)` is not sufficient for cancellation in the **complete** packet: residual partitions, nonrectangular shapes, and other determinant sectors can change both amplitude and phase/sign balance.

There is also a second scale transition hidden by the leading saddle `R_n`. From `(5)`,

\[
\boxed{
\rho_n-R_n
=
\frac{R_n^2}{n-R_n}.
}
\tag{22}
\]

Therefore:

- if `sigma<4`, then `rho_n-R_n->0`;
- if `sigma>4`, then `rho_n-R_n->infinity` although `(rho_n-R_n)/R_n->0`;
- if `sigma=4`, the absolute correction depends on the finer approach of `q_n` to `4`; for the exact sequence `q_n=4`, one has `rho_n-R_n->sqrt(a)`.

Thus `R_n` is always the correct multiplicative saddle scale, but for `sigma>=4` its finite-`n` correction is already larger than the integer resolution relevant to adjacent cancellation. The exact center `rho_n`, and then the logarithmic correction `tau_n-rho_n`, are load-bearing for lattice-level statements.

## Prior-art and novelty audit

Factorial-power saddle asymptotics are classical. Wright's work on generalized hypergeometric asymptotics develops the exponential large-variable behavior underlying many series with factorial/Gamma denominators; see E. M. Wright, *The Asymptotic Expansion of the Generalized Hypergeometric Function*, Proceedings of the London Mathematical Society 46 (1940), 389--408, DOI `10.1112/plms/s2-46.1.389`, https://doi.org/10.1112/plms/s2-46.1.389 . NIST DLMF §16.11 records the modern generalized-hypergeometric large-variable expansions and explicitly points to Wright's analysis: https://dlmf.nist.gov/16.11 . Related Le Roy-type functions continue to be studied through Gamma/factorial-power asymptotics; for a modern example see J. Paneva-Konovska, *Prabhakar Functions of Le Roy Type: Inequalities and Asymptotic Formulae*, Mathematics 11 (2023), 3768, DOI `10.3390/math11173768`, https://doi.org/10.3390/math11173768 .

Accordingly, no novelty is claimed for Stirling/Laplace saddle localization, factorial-power profiles, or the general principle that a discrete saddle can require lattice-resolution analysis. A targeted search did not locate the exact AF-418 zeta/odd-distance adjacent ratio `(4)` or its derivative-Hankel specialization. The durable result here is the direct Mathia specialization: AF-418's supercritical rectangle explosion localizes at the explicit moving width `(2)`, while the exact adjacent ratio forces the shrinking integer window `(9)` before odd-`n` rectangular cancellation is even possible.

## Boundaries and falsification checks

- The result concerns only the full-height rectangular family `lambda=(r^n)` inside the exceptional-`1` Cauchy--Binet sector. It does not control the complete partition packet, nonrectangular/tall-column shapes, the omitted-`1` sector, one-/zero-singular-block contributions, or the full determinant.
- `C_{n,r}` is a magnitude. The alternating-sign cancellation statement uses odd `n`; for even `n`, adjacent rectangles have the same `(-1)^{rn}` sign and cannot be paired in the same way.
- The hypothesis is `q_n=s_n/n->sigma` with finite `sigma>2`. The argument does not cover `q_n->infinity`.
- The definition of `R_n` uses the actual `q_n`, not only its limit. This is essential: no hidden assumption such as `(q_n-sigma)log n->0` is made.
- The shrinking-target condition `(9)` is necessary for adjacent rectangular comparability, not sufficient for complete signed-tail cancellation. Even `(10)` does not control residual packet corrections.
- The profile `(3)` identifies the moving rectangular scale but is not a claim that no other partition family can dominate the complete Cauchy--Binet sum.
- No conclusion here establishes rational-prime discrimination, zero recovery, or RH.

## Consequence for the research line

AF-418 showed that every fixed-width rectangle blows up once `sigma>2`, leaving the signed supercritical regime open. The present result replaces that qualitative obstruction by a precise moving-saddle problem. Within the rectangular family, the dominant width grows like `R_n`, the peak magnitude is `exp(sigma nR_n(1+o(1)))`, and adjacent odd-`n` cancellation requires hitting an integer lattice at the vanishing scale `R_n/n`.

So supercritical derivative depth does not remove the discretization problem; it moves it. The next useful step is no longer to guess a fixed packet index. It is to determine whether the **complete nonrectangular packet around `r~R_n`** inherits the same saddle and shrinking window, and then whether any source-forced arithmetic structure controls `dist(tau_n,Z)` at the required precision.