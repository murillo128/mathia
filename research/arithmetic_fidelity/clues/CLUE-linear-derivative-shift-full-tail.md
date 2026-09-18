---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
  - research/arithmetic_fidelity/findings/AF-418-full-height-rectangles-expose-sigma-2-absolute-tail-transition.md
---

# Linear derivative-shift full-tail resummation

## Question

AF-417 proves that if `s_n/n -> sigma` and `x=c/n`, every fixed excess degree in the exceptional-`1` Cauchy--Binet sector is renormalized by `e^{sigma d}`. The resulting degree-by-degree coefficients are exactly those of

\[
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right).
\]

Does the **complete signed** exceptional-`1` partition sector satisfy the locally uniform limit

\[
\frac{D_{n+1,\,1\in A}^{(s_n)}(c/n)}{E_n^{(s_n)}(c/n)}
\longrightarrow
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right)
\]

for finite `sigma>=0`, uniformly for `c` in compact subsets of `(0,\infty)`? If not, what additional large-partition scaling data control the limit?

## Why this is nontrivial

AF-415 proves the corresponding full resummation only for a fixed derivative shift. Its absolute Schur domination uses an excess-degree bound whose constant depends on `s`. When `s_n` grows linearly with `n`, the factor

\[
\prod_i(k_i/i)^{s_n-1}
\]

cannot be replaced over the whole partition range by an `n`-independent constant to `|lambda|` using the fixed-shift argument. AF-417 therefore establishes the candidate limit only degree by degree.

AF-418 shows that this is a genuine large-partition obstruction rather than only a missing estimate. For every fixed `r>=1`, the full-height rectangle `lambda=(r^n)` has an exact normalized magnitude whose leading exponent is

\[
\frac1n\log C_{n,r}
=
r\left(\frac{s_n}{n}-2\right)\log n
+r\log\!\left(\frac{c^2}{4\pi^2}\right)
-\frac{s_n}{n}\log(r!)+o(1).
\]

Hence AF-415-style absolute domination is impossible for `sigma>2`. At `sigma=2`, the growing rectangle retains the finer scale

\[
\left(\frac{s_n}{n}-2\right)\log n,
\]

which is invisible to every fixed partition. For `s_n=2n`, even the single column `(1^n)` grows exponentially in normalized magnitude when `c>2pi`.

The signed complete sum could still exhibit global cancellations, so AF-418 does not by itself refute the proposed exponential limit.

## Decisive test

Treat the regimes separately.

For `sigma<2`, derive a shape-uniform absolute majorant strong enough to justify the complete partition-tail interchange, including partitions whose length and size grow with `n`.

For `sigma>=2`, an AF-415-style absolute argument is ruled out. Either derive an exact signed resummation/cancellation mechanism that controls the exponentially large growing-partition sectors, or construct a signed asymptotic/counterexample showing that the complete sector depends on additional scaling data and does not have the fixed-degree candidate limit.

The critical regime must track at least the window

\[
s_n=2n+\Theta(n/\log n),
\]

because AF-418 proves that the coarser datum `s_n/n -> 2` does not control individual full-height sectors.

## Downstream gate

Only after the exceptional-`1` signed sector is controlled in the relevant derivative-depth regime should AF-416's omitted-`1` and one-/zero-singular-block estimates be revisited for growing `s_n`. Their fixed-shift negligibility cannot be assumed.

## Research disposition

Accepted. AF-418 proves that the original all-`sigma` absolute-majorant route is impossible and identifies a new critical large-partition scale. The unresolved research question is now sharply regime-dependent: subcritical shape-uniform absolute resummation versus critical/supercritical signed cancellation or failure. A future resolution should not infer complete-tail behavior from fixed-degree coefficients alone.