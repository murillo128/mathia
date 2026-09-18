# Global mathematical questions

This file records only cross-line questions that currently change how several Mathia research lines should be interpreted. Line-specific frontiers remain in each `research/<line>/mind/`.

## When does a richer observation create a discriminator rather than reconstruct the old object?

[MI-028](intuition/MI-028-complete-measurement-families-can-close-an-escape-by-reconstructing-the-classical-object.md) remains the main warning. Several lines now have exact closure theorems showing that adding enough coordinates can eliminate an observation nullspace without creating a new RH mechanism.

Farey Discrepancy gives the cleanest stable-inversion example. FD-191--FD-194 make the geometric square-root threshold exact: below the threshold there are source null directions even under strong coordinatewise Möbius fidelity, while at and above the sharp geometric constant the cumulative source has an explicit contractive inverse. The remaining problem is therefore relation-sensitive observation below complete coordinate recovery, not better conditioning of an already complete band.

Prime Circle reaches two different completeness limits. Full-shell finite-measure Mellin data collapses to zeta-zero jets with a sharp Gamma-strip threshold, and finite linear Hilbert lifts inherit that boundary. The full radial Chen signature goes further and is faithful to the radial shell path, with Mangoldt data in its abelianization. Both are strong representation theorems; neither selects the Riemann divisor. The useful frontier is an intermediate nonlinear quotient whose arithmetic sufficiency can be proved without reconstructing the complete source.

Prime Lattice now quantifies the same intermediate problem by Beurling--Malliavin density. One endpoint state gives the classical logarithmic Riesz criterion; a complete modulation family is the localized Weil form itself. Prime-log modulations already form a form core, while finite prime-axis families have only a finite completeness budget. Multiplicative closure, and even one free prime coordinate in the audited family, can collapse that sparse budget. The missing theorem is not “more modulations” but a constrained source-forced family that becomes destination-sufficient before it becomes complete.

Visual Exploration supplies a continuous analogue. Wang's symmetric source smoothing is exactly a log-scale Green resolvent with nonvanishing Fourier/Mellin multiplier, so the exact profile retains the weighted prime-power source. Yet stable inversion is costly and the complete fixed-power statistic reduces, after its linear baseline, to a Korobov--Vinogradov-scale residual. Exact source recoverability and useful asymptotic discrimination are therefore again different questions.

## Where does the obstruction move after every fixed-complexity regime closes?

Arithmetic Fidelity now has a genuine diagonal-complexity frontier. AF-411--AF-412 prove eventual positivity in both tails for **every fixed confluent order**. Any escaping-tail failure must therefore have order tending to infinity. AF-413 identifies the first left-tail balance `m e^t=Theta(1)` but does not provide a uniform diagonal theorem. The unresolved object has moved from one fixed determinant to a coupled large-order/small-source limit.

Nyman--Beurling shows the same methodological issue in exponential-sum form. Fixed-complexity improvements are not enough when the derivative or moment parameter grows: NB-206 shows that a fixed VMVT loss can erase the nominal gain on the diagonal. After Fejér smoothing removes an avoidable harmonic loss, NB-208--NB-209 show that a positive Euler return forces a correlated prime-harmonic plateau and that generic large-value estimates miss it by one logarithmic dimension. The next theorem must use the geometry of the whole plateau, not a better one-point bound.

Weil Inertia gives a negative control for another growing hierarchy. Ordinary Gowers norms fail at their natural diagonal threshold; deleting cube diagonals, deleting any sparse geometric family, deterministic scalar reweighting and linear mixing across orders all remain inside a Walsh-character quotient that matched-energy Rademacher sources can reproduce. Increasing generic hierarchy complexity is therefore exhausted unless the statistic changes information carrier and retains source-specific signed covariance.

Across these lines, “take the complexity parameter larger” is not a research mechanism. The load-bearing question is whether the estimate is uniform in the moving parameter and whether the limiting statistic preserves information absent from the matched control.

## Which physical cost survives exact-real coding, remote repair and conductor minimization?

[MI-023](intuition/MI-023-source-information-is-priced-by-inverse-distinguishability-not-forward-smoothness.md) remains the broad synthesis, but the new evidence makes the relevant physical currencies more specific.

Möbius Cancellation now distinguishes finite-resolution shell stability from minimum primitive source conductor. Exact-real subset-sum access can encode an entire endpoint sign vector even near balance; `l1` shell quotienting and `l2` average stability remove different parts of that leakage. MC-371--MC-375 then show that a quartic-efficient endpoint is forced toward quadratic primitive conductors on almost the whole Fourier cube while its source mass is both Hamming-central and delocalized across incidence signatures. The cheap-representative escape is therefore closed: further progress must work at the near-quadratic conductor boundary or change invariant.

Robin Extremal has reached a two-sided continuum source-cost theorem. Finite vertical panels remain aliasable, but hiding a whole interval separated by a logarithmic support gap has exponential spectral cost. Ordinary-prime constructions can nevertheless hide selector-scale data through `T=c log Q` for a positive explicit range while preserving every fixed KV envelope. RE-209 supplies the converse: any separated repair that hides the continuum forces a Chebyshev-prefix excursion growing like `exp(H T/e)`, giving a much larger explicit logarithmic-height ceiling. The live object is the quantitative gap between constructive ordinary-prime repair and prefix coercivity, not exact analytic injectivity.

Farey Discrepancy contributes the complementary observation-side lesson: the square-root band threshold is an exact coverage threshold with a stable inverse, while critical prime-extension energy can still hide in the nullspace below it. Source relation cost matters only when the observation actually exposes the relation.

## Can positivity preserve the critical amplitude before scalar closure squares or imports it?

Weil Positivity now gives a detailed negative classification of the direct level-one Hecke/Eisenstein route. Nonconstant Fourier modes retain genuine divisibility projections, but positive cusp-boundary squares scalarize them at `1/p` rather than the critical `p^(-1/2)` amplitude. Smooth height cutoffs add only `p^2`-orbit coherence and retain the same scalar density. An all-prime strong completion exists only for `l2` coefficients, excluding the critical amplitudes.

Passing to the globally correlated Eisenstein line does not fix the issue: finite Hecke Grams are rank-one test pullbacks, while the unrenormalized critical prime multiplier diverges. The canonical Euler completion is exactly `zeta(s+ir)zeta(s-ir)`; at the center it gives a modulus square containing finite and archimedean data but no zero-selective orientation. Its logarithmic derivative recovers the desired Mangoldt half-density only by importing the zeta divisor as poles and abandoning inherited positivity.

This sharpens a global design rule also visible in Möbius Cancellation and Prime Lattice: **the critical carrier must survive before the final quotient or positive square**. If the source-specific amplitude appears only after taking a square root of a scalarized projection, differentiating a completed scalar `L`-function, or reconstructing the full classical form, the proposed positivity mechanism has not generated an independent sign theorem.

## Global discriminator

For every proposed route, identify the admissible source class, observation family and nullspace, destination quotient, physical source-coordinate map, acquisition budget, requested precision, normalization gauge, analytic domain/class, moving-complexity regime, source support domain and granularity, sign/covariance structure and matched control. Then ask two opposite-direction questions in the same currency: **what does the destination force, and what can the physical source mechanism actually supply?**

The newest results sharpen four recurring failure modes. A complete family may merely reconstruct the classical object; a fixed-complexity theorem may become irrelevant on the diagonal where complexity must grow; exact-real or remote-source freedom may move the cost into resolution, conductor or prefix discrepancy; and positivity may square the critical amplitude or recover it only after the target divisor has already been inserted. Progress requires a source-forced intermediate structure that survives all four audits and has an independent destination theorem.
