# MI-008 — Moving quadratic comparators are squeezed to an exceptional-character frontier or a genuinely signed remainder

**Evidence level:** supported by MC-053--MC-069; exact for the convolution/feedback identities and literature-backed for Burgess/Munsch, Siegel--Walfisz, large-sieve, and Landau--Page inputs

## Core intuition

Allowing the comparator to move with scale escapes fixed-comparator transfer theorems, but the current positive quadratic-feedback architecture is now far narrower than a generic super-polylogarithmic/subpolynomial search corridor. The feedback condition forces an extreme negative terminal-prime twist; classical family and exceptional-character theory then says that ordinary nonexceptional quadratic characters are overwhelmingly unavailable.

The surviving issue is no longer “find many good moving characters.” It is either the possible moving Landau--Siegel exceptional character itself, a conductor range beyond the present pointwise uniform theorem, or a new argument that preserves signs inside the feedback sum instead of paying the positive triangle budget.

## Strongest justified principle

MC-053--MC-063 establish the family gate: good subquadratic fits require conductor growth and cannot turn over freely across scales. MC-064--MC-065 calibrate absolute transfer and its method-specific conductor penalty.

MC-066 gives the exact signed escape. For `f_chi=mu^2 chi` and `h_chi=1*f_chi`, positive triangle closure is controlled by

`R_theta(X;chi)=sum_{2<=d<=X} h_chi(d)d^{-theta}`,

where split primes contribute `2p^{-theta}`. MC-067 proves that every fixed polylogarithmic conductor, and in fact a fixed stretched-exponential range, fails this contraction uniformly for `theta` bounded away from one.

MC-068 turns the same condition into a family theorem. `R_theta<1` forces a linear-size negative character correlation with primes in `(X/2,X]`; the multiplicative large sieve therefore permits only `O(log X)` prime quadratic conductors below square-root scale to pass the necessary feedback test.

MC-069 sharpens the pointwise quasi-subpower range. Up to `Q<=exp(kappa log X/log log X)`, every nonexceptional primitive character has too much cancellation to support the required terminal bias. At most one prime conductor can survive, and it must be the unique Landau--Page exceptional primitive character at that level if such a character exists at all. Thus the positive-feedback corridor is stratified into an excluded low range, a singleton exceptional-character range, and only later a sparse family bound.

## What remains possible

A positive continuation of this exact architecture must control the possible moving exceptional character coherently across scales, push pointwise arithmetic beyond the current quasi-subpower threshold, or prove cancellation in the signed feedback remainder itself. Merely searching a broad family of ordinary quadratic comparators below the pointwise threshold is closed.

A different comparator class can evade the character-specific theorem, but it must expose its own transfer, feedback, complexity, and turnover resources explicitly.

## Status / novelty

The character-sum, large-sieve, and exceptional-zero inputs are classical. The synthesis is the frontier reduction: **positive quadratic feedback turns moving-comparator freedom into an extreme prime-bias condition that is empty for ordinary low conductors, singleton-exceptional through a quasi-subpower range, and sparse farther out**.

## Falsification criterion

Exhibit two distinct nonexceptional prime quadratic conductors in the MC-069 range satisfying `R_theta(X;q)<1` for a fixed gap from `theta=1`, or derive a source-forced signed feedback theorem that closes the recurrence without the positive budget `R_theta<1`.

## Lean-formalizable core

- Exact signed convolution feedback identity.
- Split-prime lower bound for `R_theta`.
- Terminal-prime bias from contraction.
- Large-sieve family sparsity.
- Landau--Page singleton reduction in the quasi-subpower range.
