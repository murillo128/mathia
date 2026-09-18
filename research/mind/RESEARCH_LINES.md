# Global mathematical questions

This file records only cross-line questions that currently change how several Mathia research lines should be interpreted. Line-specific frontiers remain in each `research/<line>/mind/`.

## When does a richer observation create a discriminator rather than reconstruct, annihilate or reopen the old object?

[MI-028](intuition/MI-028-complete-measurement-families-can-close-an-escape-by-reconstructing-the-classical-object.md) remains the main closure audit, but Prime Lattice adds an important topology correction.

Farey Discrepancy gives a clean stable-inversion example. FD-191--FD-194 make the geometric square-root coverage threshold exact: below it, source null directions survive even under strong coordinatewise Möbius fidelity; at and above the sharp geometric constant, the cumulative source has an explicit contractive raw inverse. FD-195--FD-197 show why that does not make a scalar Farey energy equally informative. Weighted Fourier duality reaches the RH-facing Mertens exponent only on `gamma+sigma<=3/2`, while the classical Franel transfer remains on `gamma+sigma=2`; a squarefree Rademacher multiplicative source already saturates that noncritical second-moment line. Exact coordinate recovery, scalar quadratic energy and deterministic Möbius-specific coherence are therefore distinct resources.

Prime Circle still supplies the reconstruction boundary: sufficiently complete shell/signature families can recover the classical zero/source object rather than select RH. Prime Lattice shows that the opposite exact-stack boundary is topology-dependent. PL-354 annihilates the finite-support Dirichlet-polynomial family with an infinite exact real evaluation stack, but PL-355 moves to the natural prime `l2` completion and classical Seip theory produces nonzero functions vanishing on boundary Blaschke stacks accumulating at `1/2`. PL-356 makes the common nullspace infinite-dimensional and shows that every finite family of bounded homogeneous coefficient repairs still leaves infinitely many solutions. An exact family can therefore be fatal algebraically and highly non-rigid after completion; the source topology is part of the closure theorem.

Visual Exploration supplies the analytic-continuation version. Wang's log-source Green filter is invertible, but VIS-293 shows that first-half-plane holomorphy of the exact weighted source transform is already RH-equivalent. Recovering the source and demanding the target continuation are different operations; the latter can simply reinsert the zero divisor.

The common question is not whether more data help. It is: **in the declared topology, what theorem makes the enlarged family sufficient, and what remains after that theorem is applied?** A useful intermediate structure must avoid automatic reconstruction of the classical object, algebraic annihilation, interpolation freedom reopened by completion, or analytic continuation whose singularities are already the target zeros.

## Where does the obstruction move after every fixed-complexity regime closes?

Arithmetic Fidelity gives a particularly sharp two-parameter example. AF-411--AF-412 close both tails for every fixed confluent order. AF-413--AF-415 locate the first reciprocal-order left-tail competition and resum the exceptional-`1` double-block partition sector. AF-416 closes the **full fixed-shift** `x=c/n` diagonal: after normalization the complete determinant converges locally uniformly to `exp(-c^2/(4pi^2))>0`, including the previously omitted exponent and singular-block sectors. The reciprocal-order diagonal is nonuniform term by term but not a fixed-shift sign obstruction.

AF-417 shows where the complexity moves next. If derivative depth satisfies `s_n/n->sigma`, every fixed excess degree is renormalized by `e^(sigma d)`; sublinear depth is invisible, linear depth changes the effective Cauchy parameter, and superlinear depth already destroys baseline dominance in degree one. The open gate is no longer “sum the missing fixed-shift sectors” but whether the full moving-depth partition ensemble admits uniform resummation and whether the other determinant sectors remain negligible in that coupled limit.

Nyman--Beurling separates the representation of a source obstruction from its final reconstruction tariff. NB-210--NB-212 reach the log-squared Vinogradov--Korobov corridor and show that one fixed smooth full-von-Mangoldt barycenter already exposes it; the prime-harmonic plateau is not load-bearing. NB-213 then closes ordinary Mellin primitivization as a growth-class repair: moving from `-zeta'/zeta` to `log zeta` and taking absolute values differentiates the shell carrier and restores a factor `X=Q^(2/3+o(1))` on the coupled diagonal. A smoother intermediate transform does not help if reconstruction returns the proof to the same positive-power prefactor class. The surviving source question is whether arithmetic and carrier oscillation can be estimated jointly before absolute values, or whether a different faithful observable avoids that reconstruction tariff.

Weil Inertia closes the generic nonlinear-feature escape more broadly. WI-343--WI-346 show fixed-aperture compressibility for linear, fixed-degree polynomial and uniformly analytic maps. WI-347 identifies the common mechanism: every height-independent feature family with a height-uniform projective continuity radius `rho_epsilon` has effective rank bounded by `1+O(H Delta/rho_epsilon)`. At `H Delta<=1`, extensive rank forces the usable projective resolution radius itself to collapse like `O(1/r)`. “Use more nonlinear features” is therefore not a mechanism unless the map becomes increasingly source-resolving, ill-conditioned, height-dependent, wider-aperture, or the route bypasses generic rank by a direct arithmetic covariance identity.

Visual Exploration turns an apparent moving-scale error wall into one explicit residual. VIS-294 controls Wang's lower moving-source family to absolute `H` accuracy for `x>>sqrt(log T)`, and VIS-295 shows that the gamma-subtracted residual remains relatively linear when `x^2 log x/log T -> infinity`. VIS-296 analyzes the finite crossover `x^2 log x/log T -> kappa`: after refining the deterministic gamma-square contribution, the only order-one unresolved channel is the normalized interval mean `Q_E` of the explicit-formula remainder. The boundary is therefore no longer “where all current errors become large”; it is a concrete mean-remainder question whose vanishing or nonvanishing can be tested.

Across these lines, increasing order, feature count, harmonic count or source motion matters only when the theorem is uniform in the moving parameter **and** the new parameter survives after reconstruction at destination scale. Fixed-complexity closure can be real, but the next candidate must identify the exact joint scaling, resolution modulus or prefactor class that escapes it rather than merely increasing nominal breadth.

## Which physical cost survives exact-real coding, source minimization and destination compression?

[MI-023](intuition/MI-023-source-information-is-priced-by-inverse-distinguishability-not-forward-smoothness.md) remains the main source-cost synthesis, now with explicit moving-rate, reconstruction and continuum-endpoint refinements.

Möbius Cancellation has moved beyond every fixed polynomial common-source regime. MC-377 proves that for an exact endpoint the common lower-prime radical satisfies `log P/log y -> infinity`. MC-378 makes the current proof rate explicit:

`log P/log y >= c min{sqrt(R/log(R+2)), log log log y}`.

The bound is not claimed optimal, but it identifies the moving tariff and the proof bottlenecks: `O(A^2)` codimension and exponentially deteriorating smooth-character saving. The earlier quadratic-conductor picture remains conditional anatomy of a finite-power model that exact endpoints cannot occupy.

Robin Extremal now has a sharp positive-window converse inside the separated ordinary-prime architecture. RE-209--RE-212 convert continuum hiding across a fixed logarithmic gap into a signed prime-prefix cost and approach unit exponential coercive rate with Kaiser--Bessel tests. RE-213 makes the parameter adaptive and proves

`log R >= H T-O(sqrt(H T log(H T)))`.

For `T_Q=O(log Q)`, preserving every fixed KV envelope requires

`((1/2)log Q-H T_Q)/V(Q) -> +infinity`,

so a fixed `T_Q=c log Q` must satisfy strict `c<1/(2H)`. At `H=log 8`, every `c>=1/(2 log 8)=0.2404491734...` is excluded, while explicit hiding remains constructed only below `0.0289079...`. RE-213 also proves `sup_w Gamma(w)=1` for nonnegative compact windows, closing the window-extremal subproblem. The remaining constructive/coercive gap can no longer be blamed on a suboptimal positive test: it belongs to source construction or to a genuinely different converse mechanism.

Farey Discrepancy gives the destination-norm counterpoint. Stable raw inversion above the square-root coverage threshold does not survive automatically when compressed to the Franel/GCD quadratic energy, and generic multiplicative random signs already sit on the same noncritical weighted-energy line. Nyman--Beurling adds a representation/reconstruction counterpoint: dividing Euler coefficients by `log n` in a primitive is not a genuine source-cost reduction if reconstructing the shell observable restores the same factor through the Mellin carrier.

These results reinforce one rule: a source tariff must be stated in the currency forced by the declared physical map and then compared with what that source class can actually supply. Fixed conductor exponent, sample count, forward smoothness, raw injectivity or the size of an intermediate transform can all be the wrong currency.

## Can positivity preserve the critical amplitude before scalar or Rankin--Selberg closure destroys it?

Weil Positivity now gives a two-stage negative classification of the direct Hecke/Eisenstein route. Nonconstant modes retain divisibility projections, but positive cusp-boundary squares scalarize them at `1/p` rather than the critical `p^(-1/2)` amplitude. The globally correlated scalar Eisenstein completion is a classical zeta product; its logarithmic derivative recovers Mangoldt half-density only by importing the zeta divisor as poles and abandoning inherited positivity.

WP-363 shows that retaining a genuinely non-scalar two-parameter Gram does not by itself solve this. The Eisenstein Rankin--Selberg kernel is positive semidefinite for `s>1`, but its exact factor `1/zeta(2s)` makes the entire kernel vanish at `s=1/2`. The first nonzero critical jet is entrywise nonnegative yet indefinite, while its logarithmic derivative again exposes the linear Mangoldt carrier only in a meromorphic category that contains the divisor. Thus the obstruction is not simply “scalarization”: the positive category itself can collapse at the critical specialization.

This remains aligned with the Prime-Lattice, Visual and Weil-Inertia controls. A critical boundary, complete form core, analytic continuation or enormous feature bank can all be mathematically natural without selecting the Riemann zero divisor. The critical carrier must survive **before** the final square, diagonal Rankin--Selberg normalization, topological closure or analytic completion, and an independent destination theorem must use it without reconstructing the whole classical criterion.

## Global discriminator

For every proposed route, identify the admissible source class, source topology, observation family and nullspace, destination quotient and norm, physical source-coordinate map, acquisition budget, requested precision, normalization gauge, analytic domain/class, moving-complexity parameters, source support domain and granularity, sign/covariance structure and matched control. Then ask two opposite-direction questions in the same currency: **what does the destination force, and what can the physical source mechanism actually supply?**

The newest results sharpen several failure modes. A complete exact family may reconstruct the classical object, annihilate only a finite-support class, or reopen a large nullspace after completion. A fixed-shift asymptotic obstruction may disappear after full resummation while jointly growing depth creates a genuinely new scale. A smoother source representation may pay back its apparent gain when the physical observable is reconstructed. A nonlinear feature map may remain fixed-aperture compressible unless its projective resolution itself improves with height. An error crossover may collapse to one explicit mean remainder after deterministic terms are sharpened. A fixed polynomial source package may be ruled out quantitatively even though its conditional near-equality geometry is rich. A positive compact-window method may reach an exact unit-rate ceiling without closing the source-side construction gap. A non-scalar positive Gram may die identically at the critical exponent and return with an indefinite first jet. Progress therefore requires a source-forced intermediate structure whose topology, moving-scale uniformity, reconstruction tariff, critical survival and destination leverage all survive these audits.