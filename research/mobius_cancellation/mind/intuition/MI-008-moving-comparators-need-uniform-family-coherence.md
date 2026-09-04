# MI-008 — Moving quadratic comparators are squeezed by fidelity, signed feedback, conductor distribution, and turnover

**Evidence level:** supported by MC-053--MC-067; exact for the stated convolution/feedback identities and literature-backed for Burgess/Munsch, reciprocity, and Siegel--Walfisz inputs

## Core intuition

Allowing the comparator to move with scale escapes fixed-comparator transfer theorems, but it does not remove the resource accounting. Absolute coefficient transfer, signed convolution feedback, conductor size, and inter-scale turnover impose different constraints, and improving one can expose another.

The newest boundary is especially sharp for quadratic characters. Signed feedback genuinely removes the internal-conductor `L^1` penalty that produced the `11/19` absolute-transfer floor, but it replaces that penalty by a positive `p^{-theta}` budget over split primes. Uniform prime distribution then kills every polylogarithmic conductor for any fixed exponent below one, while the classical squarefree-character certificate near exponent `1/2` simultaneously forbids polynomially large conductors. The surviving classical corridor is super-polylogarithmic but subpolynomial, and existence of a coherent family there is completely open.

## Strongest justified principle

MC-053--MC-063 establish the family gate: fixed comparator classes transfer exponents; good character fits force conductor growth and twisted-uniformity costs; distinct subquadratic good fits cannot turn over freely and are power-separated across observation scales.

MC-064--MC-065 calibrate absolute transfer. The direct squarefree-character route gives a Burgess/Munsch term together with weighted coefficient defect. Allowing `q<=X` lowers the absolute method floor from `11/16` to `11/19`, but the character zero at its own conductor creates a coefficientwise cost of size `X/q`. This is a method-specific floor, not a theorem about Mertens itself.

MC-066 identifies the signed escape exactly. With `f_chi=mu^2 chi` and `h_chi=1*f_chi`, one has `f_chi=mu*h_chi` and

`h_chi(p^a)=0,2,1`

according as `chi(p)=-1,+1,0`. The bootstrap budget is

`R_theta(X;chi)=sum_{2<=d<=X} h_chi(d)d^{-theta}`.

The conductor zero contributes only a small prime-power factor, but every split prime contributes `2p^{-theta}`. Triangle-inequality contraction therefore demands a much stronger power-weighted sparsity of quadratic residues than ordinary prime-harmonic agreement.

MC-067 closes slow conductor motion. Siegel--Walfisz implies `R_theta(X;chi) >> X^(1-theta)/log X` uniformly for every `q<=(log X)^B` and fixed `theta<=1-eta`, so no fixed polylogarithmic conductor can close the positive feedback bootstrap. Near the critical exponent, the displayed Munsch certificate requires `q=X^{o(1)}`. The method-specific search corridor is consequently `(log X)^{omega(1)} < q < X^{o(1)}`.

## What remains possible

A positive character route must derive a source-forced family in that intermediate conductor regime with three properties simultaneously: a near-critical squarefree-character estimate, a contractive signed feedback budget, and enough cross-scale coherence to cover the Mertens range despite the turnover repulsion of MC-062--MC-063. A signed analysis of the feedback remainder could evade the positive-kernel triangle budget, but it would need a new cancellation theorem rather than an accounting improvement.

A different comparator class may evade the character-specific exponents, but it must expose its own complexity, uniformity, and turnover resources explicitly.

## Status / novelty

The analytic inputs are classical. The synthesis is the four-way gate: **moving comparator fidelity, transfer strength, signed feedback, and conductor turnover cannot be optimized independently; the current quadratic architecture is squeezed into a narrow unproved intermediate regime**.

## Falsification criterion

Construct a polylogarithmic-conductor family satisfying the MC-066 positive-feedback contraction at a fixed `theta<1`, contradicting MC-067, or produce a coherent family in the surviving corridor whose total hypotheses are provably cheaper than the Mertens exponent it transfers.

## Lean-formalizable core

- Character-prefix conductor/turnover bounds.
- Absolute-transfer `11/19` balance.
- Exact signed convolution feedback identity.
- Split-prime lower bound for `R_theta`.
- Polylogarithmic-conductor exclusion.
