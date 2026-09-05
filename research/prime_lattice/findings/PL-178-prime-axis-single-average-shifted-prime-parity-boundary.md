# PL-178 — Canonical single-prime-axis affine averaging is the classical shifted-prime Liouville parity problem

## Claim

The most canonical **single-axis** residual left open by `PL-177` does not define a new prime-lattice invariant. Fix a prime `r` and, for a prime `q` and any base integer `n>=1`, consider the source-forced additive parallelogram

\[
n,\qquad rn,\qquad qn,\qquad (r+q-1)n.
\]

Its Liouville parity collapses exactly to

\[
\boxed{
\lambda(n)\lambda(rn)\lambda(qn)\lambda((r+q-1)n)
=\lambda(q+r-1).
}
\]

Consequently the normalized average over the unfrozen prime axis is exactly

\[
\boxed{
A_r(X)=\frac1{\pi(X)}\sum_{q\le X}\lambda(q+r-1),
}
\]

where the sum is over primes `q`. Thus, with the fixed shift `h=r-1`, the canonical one-axis escape is precisely the classical problem of Liouville cancellation on shifted primes.

Peer-reviewed prior art treats

\[
\sum_{q\le X}\mu(q+h)=o(\pi(X))
\]

for each prescribed fixed `h>0` as a folklore conjecture and proves it only **on average over the shift** in a broad range; the same averaged results hold for Liouville. Therefore freezing one prime axis does evade the double-source Davenport/Parseval estimate of `PL-177`, but only by landing on an established parity-problem frontier. The prime-exponent lattice and the base point have disappeared before the hard step.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION`. The exact reduction is elementary. The prior-art classification is anchored by Hildebrand's shifted-prime work and Lichtman's peer-reviewed averaged-shift theorem. This finding is decisive only for the canonical four-point closure with one fixed prime source and broad averaging over the other prime source. It does not solve the fixed-shift parity problem, rule out other single-axis observables, or exclude completed/target-relative couplings.

## Exact reduction from the exponent lattice

In exponent coordinates,

\[
\lambda(m)=(-1)^{\langle v(m),\mathbf 1\rangle}.
\]

Multiplication by `r` and `q` translates `v(n)` along the prime basis directions `e_r` and `e_q`. Ordinary additive closure chooses the fourth vertex `(r+q-1)n` because

\[
rn+qn=n+(r+q-1)n.
\]

Complete multiplicativity then gives

\[
\begin{aligned}
&\lambda(n)\lambda(rn)\lambda(qn)\lambda((r+q-1)n)\\
&\qquad=\lambda(n)^4\lambda(r)\lambda(q)\lambda(r+q-1)\\
&\qquad=\lambda(r)\lambda(q)\lambda(r+q-1).
\end{aligned}
\]

Since `r` and `q` are prime, `lambda(r)=lambda(q)=-1`, proving the displayed identity. This is pointwise in `n`; no limiting argument, convergence issue, or analytic continuation is involved. In particular, averaging or weighting the base variable cannot restore information: the base coordinate has already cancelled identically.

For fixed `r`, averaging over `q` therefore yields exactly the shifted-prime sum at the fixed additive shift

\[
h=r-1.
\]

The same statement holds on a dyadic prime interval by replacing the full sum with the corresponding difference of partial sums. There is no residual operator, torus phase, or exponent-lattice geometry hidden in this scalar after the reduction.

## Prior-art boundary: fixed shift versus averaged shift

Adolf Hildebrand's 1989 paper, *Additive and Multiplicative Functions on Shifted Primes*, established foundational mean-value results for arithmetic functions on sequences such as `p+1`, including a partial analogue of Halasz theory for multiplicative functions. This is classical prior art for treating multiplicative signs on shifted primes as a sieve/parity problem rather than a new lattice phenomenon.

Jared Duker Lichtman's peer-reviewed paper, *Averages of the Möbius Function on Shifted Primes*, states explicitly that for every fixed `h>0`

\[
\sum_{p\le X}\mu(p+h)=o(\pi(X))
\]

is a folklore conjecture appearing in print at least since Hildebrand. Lichtman proves instead that, when `H<X` and

\[
\frac{\log H}{\log\log X}\to\infty,
\]

one has

\[
\sum_{h\le H}\left|\sum_{p\le X}\mu(p+h)\right|=o(H\pi(X)),
\]

with quantitative logarithmic savings when `H=X^theta`. The paper emphasizes that averaging over the input shift is essential to the theorem, and its Remark 1.7 states that the results hold equally for the completely multiplicative Liouville function `lambda`.

This distinction is exactly the distinction exposed by the prime-lattice calculation. `PL-177` averages both source axes and obtains unconditional Fourier flattening. Freezing `r` removes one averaging variable, but the remaining scalar is not a new uncontrolled lattice statistic: it is the specified-shift case that the shifted-prime literature isolates as the hard parity frontier.

## Novelty and conflicting-claim audit

This is a classicalization/redirect, not a novelty claim. The exact identification of the particular four-point lattice closure with `lambda(q+r-1)` is immediate from complete multiplicativity once the configuration is written down.

Primary anchors:

- A. Hildebrand, “Additive and Multiplicative Functions on Shifted Primes,” *Proceedings of the London Mathematical Society* (3) **59**(2) (1989), 209–232. DOI `10.1112/plms/s3-59.2.209`.
- Jared Duker Lichtman, “Averages of the Möbius Function on Shifted Primes,” *The Quarterly Journal of Mathematics* **73**(2) (2022), 729–757. DOI `10.1093/qmath/haab054`.

A targeted audit also surfaced N. A. Carella's 2022 arXiv `math.GM` preprint `2206.12956`, which asserts much stronger fixed-shift Möbius and Liouville estimates. I found no peer-reviewed journal record or authoritative subsequent validation establishing those claims as a solution of the folklore conjecture. Because they conflict with the established peer-reviewed status boundary and have not cleared the Research Watch authority bar, they are **not** used as evidence that the fixed-shift problem is solved. This finding needs revision if a validated theorem settling the prescribed-shift Liouville average is identified later.

Recent 2026 work continues to develop Chowla-type statements **on average**, including along primes, rather than supplying a validated fixed-shift theorem. This is consistent with, but not needed for, the classification above.

## Adversarial checks and limitations

- **Not a proof of cancellation.** The exact lattice reduction says what the one-axis statistic is; it does not prove `A_r(X)->0` for a prescribed `r`.
- **Not covered by the shift-average theorem.** An estimate averaged over all `h<=H` cannot be specialized to the particular value `h=r-1` without an additional uniform argument.
- **Fixed source means fixed shift.** If `r=r(X)` grows with `X`, the displayed reduction is still exact, but the classical fixed-`h` formulation no longer by itself describes the required uniformity. Such growing/conditioned regimes need a separate theorem.
- **No implication toward RH is supplied.** Even conjectural cancellation of `lambda(p+h)` is a parity/pseudorandomness statement; this calculation does not connect its rate to the zero-free half-plane `Re(s)>1/2`, the functional equation, or a Weil/Nyman positivity criterion.
- **No general single-axis no-go.** Another observable could prevent the complete-multiplicative collapse, retain a target vector before averaging, impose a non-product phase condition, or use completion data. Only this canonical four-point parity closure is classicalized here.
- **No rescue from base averaging.** For this observable the base `n` disappears pointwise, so logarithmic/Cesaro/weighted averaging in `n` is irrelevant unless the observable is changed before the parity product is formed.

## Consequence for the research line

The accepted affine non-Haar clue should no longer treat the raw canonical one-prime-axis closure as an unexplored geometric escape. Its hard step is already the classical fixed-shift shifted-prime Liouville problem.

The surviving single-axis branch must therefore add a mathematically independent ingredient **before** the multiplicative collapse: for example a target-relative/completed coupling, a jointly constrained or phase-conditioned source readout, or a quantitative bridge whose required strength is explicitly RH-relevant. Merely packaging

\[
\sum_{q\le X}\lambda(q+r-1)
\]

as a trace, spectrum, or prime-lattice observable does not create new structure.