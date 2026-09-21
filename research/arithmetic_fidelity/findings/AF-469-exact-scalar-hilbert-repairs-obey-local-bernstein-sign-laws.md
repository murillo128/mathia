# AF-469 — Exact scalar Hilbert repairs obey local Bernstein sign laws

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-THEOREM+LINE-SPECIFIC-TRANSFER`, `ARITHMETIC-FIDELITY`, `SOURCE-METRIC-REPAIR`, `HILBERT-METRIC-TRANSFORM`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-468 showed that a scalar transform supporting complexity-independent Hilbert fidelity on the unrestricted probability simplex must amplify sufficiently small TV distances at least at square-root scale, and recorded Bernstein functions as a broad sufficient class for exact Hilbert repair. A stronger constraint follows from the exact metric-transform classification of Alman, Chu, Miller, Narayanan, Sellke, and Song: **on the lower half of the simplex diameter, exact scalar Hilbert repair forces the full Bernstein alternating-sign hierarchy, not merely the square-root asymptotic.**

Use the line's normalization

\[
\Delta(A)=\left\{\mu\in\ell^1(A):\mu(a)\ge0,\ \sum_a\mu(a)=1\right\},
\qquad d(\mu,\nu)=\|\mu-\nu\|_1\in[0,2].
\]

Let `g:[0,2] -> [0,infinity)` be continuous with `g(0)=0`. Assume that for every finite subset of `Delta(A)`, the kernel

\[
K_g(\mu,\nu)=g(d(\mu,\nu))
\]

is a squared Hilbert distance; equivalently, `K_g` is conditionally negative definite. Write the forward difference as

\[
\Delta_h g(x)=g(x+h)-g(x).
\]

Then for every integer `k>=1`, every `0<x<1`, and every positive `epsilon_1,...,epsilon_k` satisfying

\[
2x+\sum_{i=1}^k\epsilon_i<2,
\tag{1}
\]

one has

\[
\boxed{
(-1)^{k-1}
\Delta_{\epsilon_1}\cdots\Delta_{\epsilon_k}g(x)
\ge0.
}
\tag{2}
\]

Consequently, if `g` is `C^infinity` on `(0,2)`, then for every `0<x<1` and every `k>=1`,

\[
\boxed{
(-1)^{k-1}g^{(k)}(x)\ge0.
}
\tag{3}
\]

Thus `g'` is completely monotone on `(0,1)`: `g` is increasing and concave there, with all higher derivatives alternating exactly as for a Bernstein function. The conclusion is deliberately local. It does **not** prove that `g` is a Bernstein function on all of `[0,2]`.

For an exact scalar Hilbert repair written in AF-468's form

\[
\|\Psi(\mu)-\Psi(\nu)\|_H=\phi(d(\mu,\nu)),
\]

apply the statement to `g=phi^2`. Hence any sufficiently smooth exact radial repair must satisfy the Bernstein sign hierarchy for `phi^2` throughout `0<d<1`. This is a much narrower class than transforms that merely satisfy the necessary lower-scale bound `phi(t) \gtrsim sqrt(t)` from AF-468.

## Probability-simplex hyperrectangles

The line-specific bridge is elementary but load-bearing: every weighted Hamming cube whose total side length is at most the simplex diameter occurs **isometrically** inside a probability simplex.

Take side lengths `a_1,...,a_d>=0` with

\[
A_0=\sum_{i=1}^d a_i\le2.
\]

Use one base atom `*` and two atoms `(i,0),(i,1)` for each coordinate. For a corner `b in {0,1}^d`, define

\[
\mu_b(*)=1-\frac{A_0}{2},
\qquad
\mu_b(i,b_i)=\frac{a_i}{2},
\qquad
\mu_b(i,1-b_i)=0.
\tag{4}
\]

Every `mu_b` is a probability measure. If corners `b,c` differ on the coordinate set `D(b,c)`, then each changed coordinate moves mass `a_i/2` between two atoms, so

\[
\boxed{
\|\mu_b-\mu_c\|_1
=
\sum_{i\in D(b,c)}a_i.
}
\tag{5}
\]

Thus the corner metric of the real hyperrectangle with side lengths `(a_i)` embeds isometrically into `Delta(A)` whenever the total side length is at most `2`.

This matters because the converse direction in Alman et al.'s Manhattan-to-squared-Euclidean theorem is proved precisely by testing transformed distance matrices on weighted real hyperrectangles and reading their Walsh-character eigenvalues as alternating finite differences of the scalar transform.

## Transfer of the hyperrectangle argument

Fix `k`, `x`, and positive `epsilon_1,...,epsilon_k` satisfying `(1)`. For sufficiently large `d>k`, choose a `d`-dimensional hyperrectangle with

\[
a_i=\epsilon_i\quad(1\le i\le k),
\qquad
a_i=\frac{2x}{d}\quad(k<i\le d).
\tag{6}
\]

Its total side length is

\[
\sum_{i=1}^k\epsilon_i
+
\frac{2x(d-k)}{d}
<
\sum_{i=1}^k\epsilon_i+2x
<2,
\]

so `(4)` embeds every corner into the probability simplex without changing any pairwise Manhattan distance.

By assumption, applying `g` to those distances gives a squared Euclidean distance matrix. The Schoenberg conditional-negative-type sign condition therefore applies to every Walsh character orthogonal to constants. Choose the character supported on the first `k` distinguished coordinates. The real-hyperrectangle eigenvalue formula used by Alman et al. expresses the corresponding eigenvalue, up to the fixed sign convention and positive normalization, as a binomial average of the `k`-fold alternating difference of `g` at the background distance

\[
\frac{2xS_d}{d},
\qquad
S_d\sim\operatorname{Binomial}(d-k,1/2).
\tag{7}
\]

As `d -> infinity`, `(7)` converges in probability to `x`. Continuity of `g` on the compact interval containing all terms lets the binomial average converge to the alternating difference at `x`. The conditional-negative-type eigenvalue sign therefore yields exactly `(2)`.

Finally, when `g` is smooth, divide `(2)` by `epsilon_1...epsilon_k` and let all increments tend to zero. This gives `(3)`.

The argument is the converse mechanism of Alman et al. restricted to those hyperrectangles that fit inside the probability simplex. The restriction is why the conclusion above is asserted only for `x<1`: the proof needs roughly `2x` of total background side length plus the distinguished increments, while the simplex has `l1` diameter `2`.

## Prior art and novelty audit

The global classification is classical prior art relative to this line, not a new theorem here. Josh Alman, Timothy Chu, Gary Miller, Shyam Narayanan, Mark Sellke, and Zhao Song, **“Metric Transforms and Low Rank Matrices via Representation Theory of the Real Hyperrectangle,”** arXiv:2011.11503v2 (2021), Theorem 1.9 and Appendix C, prove that for a function `f:R_{>=0}->R_{>=0}` the following are equivalent: `f` is Bernstein; `f` transforms Manhattan distances to Manhattan distances; and `f` transforms Manhattan distances to squared Euclidean distances. Their Appendix C derives necessity from real-hyperrectangle/Walsh eigenvalues and higher finite differences. Primary source: https://arxiv.org/abs/2011.11503 .

AF-469 makes **no novelty claim** for that classification, for Schoenberg negative type, or for Bernstein functions. The line-specific mathematical delta is the explicit embedding `(4)`--`(5)` of every diameter-compatible weighted hyperrectangle into the probability-law source and the resulting inherited local necessity `(2)`--`(3)`. AF-468 previously used Bernstein functions only as a sufficient exact-repair family; this finding shows that their complete-alternation signature is also forced locally by exact radial Hilbert repair of the full simplex.

## Boundary and falsification audit

- **Exact repair is essential.** The argument assumes `g(d)` itself is a squared Hilbert distance, equivalently a conditionally negative-definite kernel. AF-468's broader bounded-distortion hypothesis does not imply the Walsh eigenvalue signs used here.
- **The conclusion is local below half the diameter.** The embedded-box argument directly forces `(2)` only under `2x+sum epsilon_i<2`, and therefore `(3)` only for `x<1`. No global Bernstein characterization on `[0,2]` is claimed.
- **Continuity is used in the concentration limit.** The statement does not infer continuity from exact embeddability; it assumes it. Alman et al. derive regularity in their unrestricted-Manhattan theorem, but that derivation is not silently imported to the bounded simplex.
- **Smoothness is needed only for the derivative form.** The finite-difference law `(2)` is the more primitive conclusion and requires only continuity plus the exact Hilbert-distance assumption.
- **The transform remains scalar and radial.** State-dependent, marked, anisotropic, relational, or non-radial lifts remain outside this obstruction.
- **This is not a compression theorem by itself.** An exact Hilbert embedding may retain all pairwise information while changing metric geometry. Later quotient, trace, averaging, positivity, or spectral operations require separate fidelity audits.
- **No prime specificity is generated.** The hyperrectangle obstruction works on arbitrary labels. It constrains admissible transport geometry; it does not distinguish rational primes from matched controls.

## Arithmetic specialization

If prime-indexed finite-support probability laws are allowed with unrestricted mixture complexity, an exact scalar Hilbert reparameterization cannot be chosen merely by matching the square-root lower scale from AF-468. Its squared radial transform must also satisfy complete alternation at every scale below half the source diameter. In smooth form,

\[
(phi^2)'\ge0,
\qquad
(phi^2)''\le0,
\qquad
(phi^2)'''\ge0,
\qquad\ldots
\quad\text{on }(0,1).
\]

Therefore many ad hoc nonlinear metric repairs that look acceptable from first-order conditioning alone are already excluded before any zeta- or RH-facing operator is introduced. A rational-prime application still needs a separate theorem showing either that its admissible source family avoids these weighted-hyperrectangle tests or that the downstream analytic mechanism legitimately consumes an exact transform with the required Bernstein-type geometry.

## Consequence for the line

AF-468 left open whether its Bernstein positive family was merely one convenient source of exact scalar repairs among a much larger uncontrolled class. AF-469 sharply reduces that ambiguity near the small-distance regime relevant to conditioning: **exact radial Hilbert repair forces the same complete-alternation laws that characterize Bernstein transforms in unrestricted Manhattan geometry.**

The remaining gap is now precise. Either strengthen the bounded-simplex transfer enough to classify the whole interval `[0,2]`, or move beyond exact scalar/radial transforms and identify what additional marked or source-restricted structure can preserve the intended arithmetic discriminator without paying the unrestricted-mixture obstruction.