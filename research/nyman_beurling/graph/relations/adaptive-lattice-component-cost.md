---
id: RG-nyman-adaptive-lattice-component-cost
type: research-graph-relation
scope: nyman_beurling
derived: true
---

# Adaptive lattice selection and physical component cost

[[research/nyman_beurling/graph/nyman-beurling|Nyman–Beurling graph]]

This mechanism separates finite-energy target assembly, contiguous retention and adaptive retention in the same closed real-dilation orbit spaces. It does not identify lattice-slot count with finite Nyman-generator count.

## Source-backed chain

- [[research/nyman_beurling/findings/NB-356-finite-orbit-target-assembly-is-equivalent-to-a-reciprocal-phase-series|NB-356]], §§2–3 and §5, gives the bounded lattice sampler, bounded right inverse and reciprocal-phase summability criterion, including the real-seed extension. The target is the projection \(t=P_{\mathcal N}e\); the common zeta inner factor \(B\) remains in the physical vectors.
- [[research/nyman_beurling/findings/NB-368-cubic-logarithmic-seeds-give-deterministic-finite-energy-target-completion|NB-368]], §§1–3, proves the all-integer simultaneous lower bound \(\max(\|n\alpha\|,\|n\beta\|)\ge\gamma n^{-1/2}\) for the specified cubic pair and uses it for finite-energy completion and a logarithmic interpolation-tail upper bound.
- [[research/nyman_beurling/findings/NB-369-critical-return-energy-makes-three-orbit-lattice-truncation-logarithmically-sharp|NB-369]], §§1–3, proves the matching contiguous-cutoff squared cost \(\asymp\log M/M\), even after optimizing over every exact component split. Its scope expressly leaves selected high-index retention open.
- [[research/nyman_beurling/findings/NB-370-adaptive-lattice-selection-removes-the-three-orbit-cutoff-logarithm|NB-370]], §§1–3, settles that adaptive-retention question under the same simultaneous lower bound. For \(w_n=[n^2(\|n\alpha\|^2+\|n\beta\|^2)]^{-1}\), first-return counting gives \(w_j^*\asymp j^{-2}\). The optimal omitted weight is \(\asymp1/M\), and the sampler/lift inequalities transport this order to the sum of squared physical component distances for all exact splits. One fixed lifted split attains the upper order for every retained set.

The [[research/prior_art/incremental/PA-best-term-hilbert-approximation-weak-sequence|classical best-term rearrangement theorem]] resolves NB-370's named approximation dependency. It does not prove the phase counting or turn the Hardy lift into an orthonormal identification. The contiguous lower bound is not refuted: the admitted approximation family changed.

## Retention, search and realization remain different resources

NB-370 places every globally largest retained weight within \(O_\gamma(M^2)\) indices. [[research/nyman_beurling/mind/intuition/MI-087-adaptive-lattice-retention-removes-the-component-cost-logarithm|MI-087]] separately synthesizes NB-369/NB-370 into the two-budget comparison

\[
F_{M,K}\asymp_\gamma M^{-1}+\frac{\log K}{K},\qquad K\ge M\ge64,
\]

for retaining at most \(M\) indices within a searched prefix of length \(K\). Its \(M\log M\) order-optimal horizon is explicitly a synthesis deduction, not an additional canonical finding or independently reviewed result. It need not find the globally largest weights or the exact physical optimizer. No precision or arithmetic-operation bound follows from either index horizon.

## Actual dilation coefficients after lattice selection

[[research/nyman_beurling/findings/NB-371-critical-line-zeros-force-unbounded-finite-dilation-synthesis-cost|NB-371]], §§1–3 and its finite-generator consequence, settles the fixed absolute-coefficient budget question left by NB-370. For the normalized columns \(A_ag_v\), arbitrary real seeds \(v>1\) and arbitrary dilation ranges, put \(Q=\sum|c_\nu|(v_\nu^{-1}+v_\nu^{-1/2})\le2S\), where \(S=\sum|c_\nu|\). The [[research/prior_art/incremental/PA-burnol-nyman-projection-factorization|classical Burnol projection]] retains target modulus \(b/|s|\), while the synthesized modulus is at most \(Q|\zeta(s)|/|s|\) on \(\Re s=1/2\). Integration near one fixed critical-line zero of multiplicity \(m\) gives

\[
\|t-w\|^2\ge c_{\rho,b}(1+Q)^{-1/m}.
\]

This is a shrinking-neighborhood estimate, not bounded point evaluation on the Hardy boundary. Hence error \(O(M^{-1/2})\) for the final projected target requires \(S_M=\Omega(M^m)\), at least \(\Omega(M)\) without a simplicity assumption. If the coefficient Euclidean norm is bounded by \(C_M\), then \(J_MC_M^2=\Omega(M^{2m})\); no generator-count bound follows without coefficient control.

For each fixed nonzero finite lattice lift, NB-356's explicit right inverse has a rational numerator with finitely many critical-line zeros. Hardy's infinitude theorem leaves a critical-line zeta zero at which that lift is nonzero. NB-371 therefore also excludes each selected component from every fixed same-seed absolute-coefficient closure, including finite-total-variation dilation mixtures. The selected zero and constant may depend on the component. This is not a uniform lower bound as the selected set grows.

The fixed-target estimate permits all seed choices and bounds excess above the Burnol floor. It supplies no matching upper synthesis law, maximal-dilation bound or positive distance from the unrestricted closed orbit. NB-353's weighted one-line lattice cost, NB-020's index-weighted integer-section cost and NB-083's stationary polynomial prediction depth remain different resources, as NB-371 expressly records. The classical multiplier-vanishing mechanism is not claimed as novel.

## Effective range remains a separate obstruction

[[research/nyman_beurling/findings/NB-372-bounded-effective-dilation-range-retains-a-strict-projected-target-gap|NB-372]], §§1–3, retains the same projected target but removes the coefficient-budget hypothesis. For every finite \(R>1\), the closed span \(\mathcal W_R\) of columns with \(av\le R\) has \(\Delta_R=\operatorname{dist}(t,\mathcal W_R)>0\), even with unbounded coefficient sums and column counts. Its distance from the original target is exactly \(1-b^2+\Delta_R^2\) after squaring.

In logarithmic time, the causal inverse source is \(\mathscr I h=M*(D+1/2)h\), with \(M=\sum_{n\ge1}\mu(n)n^{-1/2}\delta_{\log n}\). It is locally continuous from \(L^2\) to distributions. Each column has inverse source \(v^{-1}\delta_{\log a}-v^{-1/2}\delta_{\log(av)}\); fixed support therefore survives Hilbert closure without assuming a finite measure limit. A compact inverse source for \(t\) would give an entire transform \(E=bB/\zeta\). The continuous boundary product would have modulus \(b>0\) everywhere, contradicting a critical-line zero. No boundary evaluation of a generic Hardy function is used.

NB-372 also constructs bounded Hilbert duals from compact tests outside \([0,\log R]\). Their nonzero target responses are existential, so no effective rate for \(\Delta_R\) follows. Increasing range gives \(\Delta_R\to0\). Convergent finite syntheses must therefore have both divergent coefficients (NB-371) and divergent effective range (NB-372); only for fixed seeds does the latter force dilation \(a\) itself to diverge. Neither condition prices column count without additional assumptions.

The source's comparison with [Burnol's cutoff theorem, Theorem 1.3](https://arxiv.org/pdf/math/0103058), preserves the distinction between distance to the original indicator and strict excess above its possibly positive projection floor. The displayed classical lower rate becomes trivial when the limiting distance is positive; subtracting the floor does not yield a rate for \(\Delta_R\). No improved cutoff rate or bibliographic priority is inferred.

## Evidence boundary

The budget counts positive lattice-index pairs shared by two non-anchor components. The approximation spaces contain an unrestricted infinite-dimensional sampler kernel, and the anchor remains unrestricted. Squared component-distance lower bounds do not lower-bound the residual of the sum, whose errors may cancel. Constructing the vectors still uses \(B\) and \(b=B(1)\), even though the selector uses only phases. Mere summability does not replace the all-integer bad-approximation hypothesis, and the specified integer seeds \(2,3,5\) are not covered. The Burnol floor and RH closure question remain unchanged. NB-371 adds a necessary coefficient cost; the finite-generator upper approximation problem remains open. The sources report analytic derivations with independent adversarial review pending; graph curation supplies no approval or novelty upgrade.
