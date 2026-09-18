---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
  - research/arithmetic_fidelity/findings/AF-418-full-height-rectangles-expose-sigma-2-absolute-tail-transition.md
  - research/arithmetic_fidelity/findings/AF-419-subcritical-linear-shifts-admit-uniform-full-tail-resummation.md
  - research/arithmetic_fidelity/findings/AF-420-critical-derivative-window-has-sharp-subthreshold-absolute-resummation-domain.md
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

which is invisible to every fixed partition.

AF-419 closes the strictly subcritical branch. If `limsup s_n/n<2`, a column-height split plus Pieri's rule gives a shape-uniform absolute majorant and the complete exceptional-`1` sector converges to the fixed-degree candidate.

AF-420 penetrates the critical window itself. With

\[
a=\frac{c^2}{4\pi^2},
\qquad
b_n(a)=a\,n^{s_n/n-2},
\]

if `s_n/n -> 2` and `limsup b_n(A)<1`, the full sector converges uniformly on `0<=a<=A` to `exp(-a e^{s_n/n})`. If

\[
\tau_n=\left(\frac{s_n}{n}-2\right)\log n\to\tau,
\]

this gives the exact subthreshold domain `a<e^{-tau}`. Conversely, for `a e^tau>1` the single full-height column grows exponentially. On the exact critical sequence `s_n=2n`, the boundary is `a=1` (`c=2pi`): the candidate limit is proved for every compact `a<1`, while the `lambda=(1^n)` term already grows linearly at `a=1`.

The signed complete sum could still exhibit global cancellations on the boundary and in the superthreshold region, so the growing-column obstruction does not by itself refute the candidate exponential there.

## Decisive test

The strictly subcritical branch is resolved by AF-419. The finite-`tau` critical window is also resolved throughout the absolute subthreshold region `a e^tau<1` by AF-420.

The remaining critical problem starts at the effective boundary

\[
a e^\tau\ge1.
\]

There, derive an exact signed resummation/cancellation mechanism for the exponentially or polynomially large full-height sectors, or derive a signed asymptotic/counterexample showing that the complete sum depends on additional scaling data and differs from the fixed-degree candidate.

For genuinely supercritical ratios `sigma>2`, absolute control is impossible already from AF-418. The same signed alternative remains: either identify a global cancellation mechanism or prove a different/nonexistent complete limit.

The critical analysis should retain the effective coordinate `b_n(a)=a n^{s_n/n-2}` rather than only `s_n/n`, because AF-420 proves that this finer coordinate governs the absolute phase boundary.

## Downstream gate

Only after the exceptional-`1` signed sector is controlled in the boundary/superthreshold derivative-depth regime should AF-416's omitted-`1` and one-/zero-singular-block estimates be revisited for growing `s_n`. Their fixed-shift negligibility cannot be assumed.

## Research disposition

Accepted. AF-419 resolves all strictly subcritical derivative ratios. AF-420 further resolves the critical `n/log n` window below the sharp effective threshold `b=a e^tau=1` and shows that the full-height column blocks absolute control on the other side; for `s_n=2n` even the boundary term grows linearly. The live question is now genuinely signed: boundary/superthreshold cancellation or failure in the critical window, followed by the `sigma>2` regime.
