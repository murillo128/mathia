# AF-282 — Two-prime joint phase separation is inverse breadth

**Status:** `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `FINITE-BREADTH`, `STABILITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-281 proves that the mixed two-cadence channel

\[
h_2=\frac{2\pi}{\log 2},
\qquad
h_3=\frac{2\pi}{\log 3}
\]

is exactly coefficient-faithful for ordinary Dirichlet series because the two rational resonance groups have trivial intersection. Exact injectivity, however, does not price how accurately a finite source prefix must resolve the resulting joint phase labels.

For `n>=1`, define

\[
z_n=
\left(
 e^{-2\pi i\log n/\log2},
 e^{-2\pi i\log n/\log3}
\right)\in\mathbb T^2
\]

and, for `N>=2`, let

\[
\delta_N=
\min_{1\le m<n\le N}
\max\bigl(|z_{n,1}-z_{m,1}|,|z_{n,2}-z_{m,2}|\bigr).
\]

Then the finite-prefix joint phase map has the sharp order

\[
\boxed{\delta_N=\Theta(N^{-1}).}
\]

More explicitly,

\[
\boxed{
\frac{4}{3^{1/4}\log 6}\,\frac1N
\le \delta_N
\le
\frac{2\pi}{\log2}\,\frac1{N-1}.
}
\]

Thus the exact two-prime coupling repair from AF-281 does not hide an exponentially fine **phase-label** separation problem on the prefix `1,...,N`: the worst pairwise joint-node spacing is of inverse-breadth order. Resolving the source label from a directly observed noisy joint phase therefore needs phase accuracy `O(1/N)`, equivalently only `O(log N)` bits of absolute resolution.

This is not a coefficient-recovery condition number. Recovering an unknown coefficient measure from mixed Fourier moments still incurs the separate mixed-mode-degree and interpolation-conditioning bills identified by AF-281. The theorem prices only the geometry of the finite source labels themselves.

## Lower bound

Fix `1<=m<n<=N` and write

\[
r=\frac nm>1,
\qquad
\delta=
\max\left(
\left|e^{-2\pi i\log r/\log2}-1\right|,
\left|e^{-2\pi i\log r/\log3}-1\right|
\right).
\]

If `delta>=1`, then the asserted lower bound already follows because

\[
\frac{4}{3^{1/4}\log6}\frac1N<1
\]

for every `N>=2`.

Assume therefore `delta<1`. For a real `x`,

\[
|e^{2\pi i x}-1|=2|\sin(\pi\|x\|)|,
\]

where `||x||` denotes distance to the nearest integer. On the range forced by `delta<1`, the elementary inverse-sine estimate gives

\[
\left\|\frac{\log r}{\log2}\right\|\le\frac\delta4,
\qquad
\left\|\frac{\log r}{\log3}\right\|\le\frac\delta4.
\]

Choose nearest integers `a,b>=0`. Then

\[
|\log r-a\log2|\le\frac\delta4\log2,
\qquad
|\log r-b\log3|\le\frac\delta4\log3.
\]

If `a=b=0`, then

\[
\log r\ge\log\left(1+\frac1{N-1}\right)\ge\frac1N,
\]

while the second approximation gives `log r<=delta log3/4`. Hence

\[
\delta\ge\frac4{N\log3},
\]

which is stronger than the claimed constant.

The case in which exactly one of `a,b` is zero is impossible: the nonzero quantity `|a log2-b log3|` is then at least `log2`, whereas the two approximation errors give

\[
|a\log2-b\log3|
\le\frac\delta4(\log2+\log3)
<\frac14\log6<\log2.
\]

It remains that `a,b>=1`. Put

\[
A=2^a,
\qquad
B=3^b.
\]

They are distinct integers. The approximation bounds and `delta<1` imply

\[
A\le r\,2^{1/4}\le 2^{1/4}N,
\qquad
B\le r\,3^{1/4}\le 3^{1/4}N.
\]

For distinct positive integers,

\[
|\log(A/B)|\ge\frac1{\max(A,B)}.
\]

Indeed, if `A>B`, then

\[
\log(A/B)=\log\left(1+\frac{A-B}{B}\right)
\ge\frac{A-B}{A}\ge\frac1A,
\]

and the other ordering is symmetric. Therefore

\[
\frac1{3^{1/4}N}
\le |a\log2-b\log3|
\le\frac\delta4\log6,
\]

so

\[
\delta\ge
\frac{4}{3^{1/4}\log6}\frac1N.
\]

Since this holds for every pair in the prefix, it proves the lower bound for `delta_N`.

## Upper bound

Take the adjacent pair `m=N-1`, `n=N`. For either `q in {2,3}`,

\[
\left|
 e^{-2\pi i\log(N/(N-1))/\log q}-1
\right|
\le
\frac{2\pi}{\log q}\log\frac N{N-1}.
\]

The larger right-hand side is the `q=2` one, and

\[
\log\frac N{N-1}
=\log\left(1+\frac1{N-1}\right)
\le\frac1{N-1}.
\]

Hence

\[
\delta_N\le
\frac{2\pi}{\log2}\frac1{N-1}.
\]

Together with the lower bound this gives `delta_N=Theta(1/N)`.

## What this adds to AF-281

AF-281 separates three resources: exact joint aliasing, mixed-mode budget, and finite-window inverse stability on an unrestricted infinite source. The present result inserts a fourth quantitative layer for a **known finite ordinary-Dirichlet prefix**.

The joint phase labels themselves have a polynomial, not exponentially collapsing, separation scale. In particular, if a phase-label observation is perturbed by less than

\[
\frac{2}{3^{1/4}\log6}\frac1N
\]

in the coordinatewise chord metric, nearest-node identification inside the prefix is unambiguous. Conversely, the adjacent pair shows that no prefix-uniform identification rule can tolerate a fixed positive phase error as `N` grows.

This prevents two different conditioning questions from being conflated. The arithmetic label map `n -> z_n` costs inverse breadth in precision, while reconstructing arbitrary amplitudes from a bounded set of mixed moments can be much worse because it also pays interpolation degree, node geometry collectively, and coefficient conditioning.

## Prior art and novelty assessment

No general sampling or Diophantine-approximation novelty is claimed. AF-281 already places the joint phase representation in classical compact-abelian Fourier analysis and Bohr theory for Dirichlet series, with Walter Rudin's *Fourier Analysis on Groups* and Ingo Schoolmann's work on general Dirichlet series as the surrounding literature.

The estimate here is an elementary finite-prefix specialization. Its lower bound uses only the exact multiplicative independence of `2` and `3`, the fact that distinct positive integers have logarithmic separation at least the reciprocal of their size, and the circle chord formula. A targeted literature search found the expected general Dirichlet-polynomial, Bohr-equivalence, and torus-frequency frameworks but no reason to treat this explicit `Theta(1/N)` bound as a new theorem of those subjects. It is retained because it prices a resource left qualitative in AF-281.

## Boundaries and failure modes

- The result concerns the declared finite source labels `1,...,N`. It does not estimate recovery of unknown frequencies outside that prefix.
- `delta_N` is pairwise node separation in the two-torus chord metric. It is not a lower singular value of a multivariate Vandermonde matrix and does not by itself control coefficient-recovery conditioning.
- The upper bound is order-sharp, not constant-sharp. No claim is made that adjacent integers always realize the exact minimum.
- The lower bound exploits the integer bases `2` and `3`. Analogous arguments extend to fixed multiplicatively independent integer bases with base-dependent constants, but that generalization is not needed for the arithmetic instance here.
- Infinite-source exact fidelity still requires the complete mixed channel of AF-281, and every fixed mixed-index box still lacks a source-breadth-independent inverse modulus on the unrestricted weighted `ell^1` class.
- No analytic continuation, zero-location statement, functional equation, or RH implication follows from this finite-prefix phase-separation estimate.

## Decisive audit test

When a finite-prefix mixed-cadence proposal claims that exact joint alias removal is unusable because the source labels themselves become arbitrarily close too quickly, compute the minimum joint phase spacing on the declared prefix. For the `log2/log3` arithmetic channel, the spacing is trapped between explicit constant multiples of `1/N`; any stronger instability must therefore enter through the observation map, the mixed-mode budget, coefficient inversion, noise model, or a broader source category rather than through exponential collapse of the phase labels themselves.

## Consequence for the research line

The live acquisition question can now be stated more sharply. Exact coupling solves aliasing, and finite-prefix phase labels require only inverse-breadth resolution, but AF-281 still leaves the aggregate moment inverse problem without a breadth-uniform modulus. The next useful theorem should therefore price the **joint** growth of mixed-mode degree, observation precision, and coefficient stability for an arithmetic source class actually consumed downstream, rather than attributing all finite-budget failure to phase-node collisions.