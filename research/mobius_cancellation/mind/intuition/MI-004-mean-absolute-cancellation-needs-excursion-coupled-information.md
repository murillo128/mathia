# MI-004 — Mean-absolute Mertens control is RH-complete; the hard part is producing it from weaker arithmetic input

**Evidence level:** exact Mellin equivalence through MC-115, exact checkpoint interpolation through MC-116, with stronger Pintz profile still `NEEDS-AUDIT`

## Core intuition

The mean-absolute endpoint is no longer merely a plausible dynamical proxy. MC-115 proves directly that square-root-scale mean absolute Mertens control is equivalent to RH: absolute convergence of the Mellin integral for `M(x)` continues `1/zeta(s)` into the corresponding half-plane and excludes zeros there. The research problem is therefore not to justify the endpoint, but to find a **source-faithful mechanism that proves it without already solving the same zero-free problem in disguise**.

MC-116 simultaneously lowers the scale-coverage burden. It is enough to prove the required exponent on a deterministic subpower-dense sequence of checkpoints; monotonicity of the cumulative absolute mass fills the gaps without exponent loss. This isolates cancellation strength, rather than continuum-in-scale control, as the genuine difficulty.

## Strongest justified principle

Let `A(X)=integral_1^X |M(x)| dx`. MC-115 shows that `A(X)/X=O(X^alpha)` implies absolute convergence of `s integral_1^infinity M(x)x^{-s-1}dx` for `Re s>alpha`, where it agrees with `1/zeta(s)` in the initial half-plane. Hence zeros with real part greater than `alpha` are impossible. Applying this at every `alpha>1/2` gives the exact RH equivalence.

MC-116 uses only monotonicity of `A`. If `log X_(j+1)/log X_j ->1`, an RH-scale bound at the checkpoints propagates to all intermediate `X` with the same exponent. More generally a limiting logarithmic ratio `q>1` gives an explicit exponent penalty rather than an all-or-nothing loss.

Earlier matched controls remain decisive. Diffusive or positive-norm carriers can reproduce coarse mean-absolute behavior without retaining Möbius-specific signed information, while several natural transforms expose an RH-equivalent reciprocal-zeta mode directly. The live mechanism must therefore generate the checkpoint bound from information independently weaker than the Mellin conclusion.

## Counterevidence / boundary

MC-115 does not provide a new proof of the square-root bound; it identifies exactly how strong such a bound is. MC-116 does not reduce the cancellation exponent, only the density of scales on which it must be established. The stronger Pintz asymptotic in MC-009 remains useful only conditionally on its audit and must not be treated as established evidence.

## Epistemic status

**Proved endpoint equivalence and interpolation; open source mechanism.** The Mellin bridge is classical in character, while its role as the exact downstream target is durable line synthesis.

## Falsification criterion

Find an error in the MC-115 Mellin continuation under its stated mean-absolute hypothesis, or a subpower-dense checkpoint sequence satisfying MC-116's hypotheses whose bound fails to interpolate with the claimed exponent. Otherwise any proposed route should be judged by whether it produces the checkpoint estimate from genuinely weaker arithmetic information.