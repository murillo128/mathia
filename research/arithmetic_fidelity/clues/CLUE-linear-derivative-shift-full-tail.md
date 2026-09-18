---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: proposed
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
---

# Linear derivative-shift full-tail resummation

## Question

AF-417 proves that if `s_n/n -> sigma` and `x=c/n`, every fixed excess degree in the exceptional-`1` Cauchy--Binet sector is renormalized by `e^{sigma d}`. The resulting degree-by-degree coefficients are exactly those of

\[
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right).
\]

Does the **complete** exceptional-`1` partition sector satisfy the locally uniform limit

\[
\frac{D_{n+1,\,1\in A}^{(s_n)}(c/n)}{E_n^{(s_n)}(c/n)}
\longrightarrow
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right)
\]

for every finite `sigma>=0`, uniformly for `c` in compact subsets of `(0,\infty)`?

## Why this is nontrivial

AF-415 proves the corresponding full resummation only for a fixed derivative shift. Its absolute Schur domination uses an excess-degree bound whose constant depends on `s`. When `s_n` grows linearly with `n`, the factor

\[
\prod_i(k_i/i)^{s_n-1}
\]

cannot be replaced over the whole partition range by an `n`-independent constant to `|lambda|` using the fixed-shift argument. AF-417 therefore establishes the candidate limit only degree by degree; exchanging the large-`n` limit with the unbounded partition sum remains open.

## Decisive test

Derive a uniform-in-partition majorant on `x=c/n`, `s_n/n` in a fixed compact interval, strong enough to justify the partition-tail interchange and recover the proposed exponential limit; or construct a growing family of partitions whose normalized contribution survives outside that proposed resummation and falsifies it.

A successful proof should explicitly control partitions whose length and size grow with `n`, not only fixed shapes. A counterexample should identify the scale of `|lambda|`, length, and shifted indices responsible for the failure.

## Downstream gate

If the exceptional-`1` resummation survives, the next gate is to revisit AF-416's omitted-`1` and one-/zero-singular-block estimates with `s_n~sigma n`. Fixed-shift negligibility cannot be assumed at growing derivative depth.