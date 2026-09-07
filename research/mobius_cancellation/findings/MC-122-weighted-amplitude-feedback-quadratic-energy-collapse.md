# MC-122 — Deterministically weighted amplitude feedback collapses to quadratic path energy

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `NO-NOVELTY-CLAIM`.

## Claim

Write

\[
M_n=M(n),\qquad \mu_n=\mu(n)=M_n-M_{n-1},\qquad M_0=0.
\]

`MC-013` records the unweighted quadratic chain rule

\[
2\mu_nM_{n-1}=M_n^2-M_{n-1}^2-\mu_n^2.
\tag{1}
\]

The same identity closes a larger candidate class than was isolated there. For **arbitrary real weights** `w_1,...,w_N`, define

\[
C_w(N)=\sum_{n=1}^N w_n\mu_nM_{n-1},
\qquad
Q_w(N)=\sum_{n=1}^N w_n\mu_n^2.
\tag{2}
\]

Finite summation by parts gives the exact identity

\[
\boxed{
2C_w(N)+Q_w(N)
=
w_NM_N^2+
\sum_{n=1}^{N-1}(w_n-w_{n+1})M_n^2.
}
\tag{3}
\]

Thus deterministic weighting does not by itself turn the amplitude feedback `mu(n)M(n-1)` into an independent source statistic. Once the explicitly known square-free term `Q_w` is retained, every such weighted correlation is exactly a weighted quadratic energy of the Mertens path.

In particular, if

\[
w_1\ge w_2\ge\cdots\ge w_N\ge0,
\tag{4}
\]

then the right-hand side of `(3)` is nonnegative. Positive decreasing weights therefore produce a positive `L^2`-type path-energy transform, not a new signed cancellation carrier.

This materially sharpens one boundary in `MC-013`: an unweighted amplitude correlation collapses by the square chain rule, but **nontrivial deterministic weighting alone does not escape that collapse**. New arithmetic information would have to enter through how the weighted energy is independently controlled, through a genuinely different observable such as the Tanaka sign feedback, through conditioning/coupling not reducible to `(3)`, or through other source-specific structure.

## 1. General weighted identity

Multiply `(1)` by `w_n` and sum:

\[
2C_w(N)+Q_w(N)
=
\sum_{n=1}^Nw_n(M_n^2-M_{n-1}^2).
\tag{5}
\]

The finite right-hand side telescopes after Abel summation:

\[
\sum_{n=1}^Nw_n(M_n^2-M_{n-1}^2)
=
w_NM_N^2-w_1M_0^2
+
\sum_{n=1}^{N-1}(w_n-w_{n+1})M_n^2.
\tag{6}
\]

Since `M_0=0`, `(6)` is exactly `(3)`. No asymptotic estimate, zero-free region, analytic continuation, or probabilistic model enters.

For decreasing nonnegative weights, every coefficient on the right of `(3)` is nonnegative. Consequently

\[
2C_w(N)+Q_w(N)\ge0,
\tag{7}
\]

and the weighted amplitude feedback can be negative only to the extent allowed by the explicit square-free mass `Q_w`.

The identity is algebraic and remains true for any prescribed finite weight vector. What it rules out is a claim that weighting **by itself** creates a new information carrier. A theorem that estimates `C_w` from independent arithmetic structure may still be difficult and useful, but its mathematical consequence is exactly control of the weighted quadratic path energy in `(3)`.

## 2. The triangular weight is exactly the full quadratic path energy

Take

\[
w_n=N-n\quad(1\le n\le N-1),
\qquad w_N=0.
\tag{8}
\]

Then every first difference is one, so `(3)` becomes

\[
\boxed{
2\sum_{n=1}^{N-1}(N-n)\mu_nM_{n-1}
+
\sum_{n=1}^{N-1}(N-n)\mu_n^2
=
\sum_{n=1}^{N-1}M_n^2.
}
\tag{9}
\]

This is the `L^2` analogue of the triangular Tanaka identity in `MC-013`, which represents the first absolute mean using `sgn(M_{n-1})` plus zero-departure local time. The distinction is now exact: replacing the sign of the excursion by its amplitude turns the triangular carrier into quadratic energy.

For integer `N`,

\[
D_M(N)=\frac1N\int_1^N|M(x)|\,dx
=\frac1N\sum_{n=1}^{N-1}|M_n|.
\tag{10}
\]

Cauchy-Schwarz gives

\[
D_M(N)^2
\le
\frac1N\sum_{n=1}^{N-1}M_n^2.
\tag{11}
\]

Therefore an estimate

\[
\sum_{n=1}^{N-1}M_n^2
\ll_\varepsilon N^{2+2\varepsilon}
\tag{12}
\]

implies the RH-scale mean-absolute estimate

\[
D_M(N)\ll_\varepsilon N^{1/2+\varepsilon}.
\tag{13}
\]

By `MC-121`, `(13)` on **any unbounded sequence of integer checkpoints** already implies RH. Conversely RH gives the classical pointwise bound `M_n=O_epsilon(n^(1/2+epsilon))`, hence `(12)` at every scale. Thus the triangular weighted amplitude route is RH-complete at arbitrary unbounded checkpoints precisely because it is the quadratic path-energy route in disguise.

A particularly strong sufficient condition illustrates the scale. If along an unbounded checkpoint sequence

\[
\sum_{n<N}(N-n)\mu_nM_{n-1}\le0,
\tag{14}
\]

then `(9)` and `mu_n^2<=1` give

\[
\sum_{n<N}M_n^2
\le
\sum_{n<N}(N-n)\mu_n^2
\le \frac{N(N-1)}2,
\tag{15}
\]

so `D_M(N)=O(sqrt(N))` on those checkpoints and `MC-121` yields RH. No such sign theorem is asserted. Equation `(15)` only quantifies how strong a genuinely independent anticorrelation statement would be.

## 3. Positive logarithmic weights do not evade the collapse

A direct recent prior-art neighbor is Chavez (`MC-S22`), who studies logarithmically weighted correlations between `mu(n)` and `M(n-1)` and, under RH plus simplicity of the nontrivial zeta zeros, obtains asymptotic formulas related to negative moments of `zeta'(rho)`.

For the basic decreasing weight appearing in that setting,

\[
w_n=n^{-1-\delta},\qquad \delta>0,
\tag{16}
\]

`(3)` gives at every finite cutoff `N`

\[
\begin{aligned}
2\sum_{n\le N}\frac{\mu_nM_{n-1}}{n^{1+\delta}}
+
\sum_{n\le N}\frac{\mu_n^2}{n^{1+\delta}}
={}&
\frac{M_N^2}{N^{1+\delta}}\\
&+
\sum_{n<N}
\left(
\frac1{n^{1+\delta}}-
\frac1{(n+1)^{1+\delta}}
\right)M_n^2.
\end{aligned}
\tag{17}
\]

The right-hand side is again a positive weighted quadratic energy. This does **not** trivialize Chavez's conditional spectral asymptotics: his normalization, moving parameters, zero information, and connection to negative zeta-derivative moments are additional analytic content. It does establish a precise boundary for this line: the raw deterministic amplitude-weighted correlation itself cannot be treated as a new signed source observable distinct from a weighted `M^2` energy.

The same warning applies to any proposed family of positive monotone deterministic weights. Changing the kernel changes which portions of the path energy are emphasized and may change analytic tractability, but it does not by itself recover the `L^1` excursion information that the current mean-absolute frontier needs.

## Prior art and novelty assessment

The algebra behind `(3)` is ordinary finite Abel/summation-by-parts applied to the elementary square chain rule. No novelty is claimed for that mechanism or for weighted quadratic-energy identities in general.

The closest line-local arithmetic prior art is Gordon Vincent Chavez, *Correlations of the Möbius and Liouville functions with their partial sums*, International Journal of Number Theory 22(8) (2026), 1875–1899, DOI `10.1142/S1793042126500934`, published 13 May 2026. It is already recorded as `MC-S22`. Chavez studies logarithmically weighted amplitude correlations and derives conditional formulas under RH and simple zeros. That paper validates this weighted correlation as a genuine contemporary arithmetic object, while `(3)` supplies the exact path-energy reduction relevant to Mathia's source-statistic search.

A targeted search around weighted Möbius/partial-sum correlations, Abel summation, and `M(n)^2` did not reveal a separately named theorem packaging `(3)` as a Mertens obstruction. Absence of such packaging is not novelty evidence; the identity is an elementary specialization and is stored here because it closes a live candidate class.

## Boundaries and falsification tests

- This finding gives no new unconditional upper bound for `M`, `D_M`, or the quadratic energy.
- It does not show that weighted correlations are useless. An independently proved arithmetic estimate for one side of `(3)` may still be a viable route; the point is that its consequence is exactly a weighted quadratic-energy estimate.
- The square-free term `Q_w` must not be discarded. For positive weights it supplies the explicit diagonal mass against which negative amplitude feedback is measured.
- Positivity requires the monotonicity/nonnegativity condition `(4)`. Oscillatory or sign-changing weights still satisfy `(3)` but no longer define a positive energy; their possible usefulness must be audited separately.
- A data-dependent or arithmetically structured choice of weights can itself carry information. Equation `(3)` still holds pointwise, but this finding does not claim that the rule producing such weights is informationally empty.
- Passing from finite `(17)` to an infinite Dirichlet-series identity requires a justified boundary limit. In particular one must not suppress `N^(-1-delta)M_N^2` in a range where doing so would already require strong Mertens control.
- The triangular criterion is not a proof strategy by itself. Bounding its exact right-hand side at the RH exponent is already an RH-complete task by `MC-121`.

## Consequence for the line

The current search for a source-natural transfer to first absolute mean should not treat **deterministically weighted amplitude feedback** as an independent information carrier merely because the unweighted correlation in `MC-013` was degenerate. The entire weighted family has the exact collapse `(3)`.

This moves attention back to observables that retain information lost by quadratic energy: the Tanaka sign feedback and zero-departure term, genuinely conditional or cross-scale structure, Möbius-specific bilinear laws not algebraically reducible to one-path energy, or another source statistic whose polynomial control forbids rare coherent excursions. Any future amplitude-correlation proposal should first be tested against `(3)` before receiving a novelty or transfer interpretation.
