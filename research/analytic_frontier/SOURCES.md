# Analytic-frontier source anchors

This file records durable literature dependencies for `research/analytic_frontier/`. It is an anchor list, not a search history and not a claim that the frontier is bibliographically complete.

## Large values and zero density

- Larry Guth and James Maynard, **New large value estimates for Dirichlet polynomials**, *Annals of Mathematics* 203:2 (2026), 623–675, DOI `10.4007/annals.2026.203.2.6`. Role: current primary anchor for new large-value estimates, the bound `N(sigma,T) <= T^{30(1-sigma)/13+o(1)}`, and the associated short-interval prime consequences.
- Terence Tao, Tim Trudgian and Andrew Yang, **New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach**, arXiv:2501.16779, current manuscript dated 24 August 2026. Role: systematic implication network among exponent pairs, large-value exponents, zero-density exponents and zero-additive-energy exponents; source for the post-Guth--Maynard optimized frontier and the new `A^*(sigma)` estimates.
- [Analytic Number Theory Exponent Database (ANTEDB)](https://teorth.github.io/expdb/). Role: living human-readable and executable source for the current optimized zero-density and zero-energy tables and their theorem dependencies; use the underlying cited theorem/paper when a durable claim depends on one entry.
- [`research/prior_art/zero-density-method.md`](../prior_art/zero-density-method.md). Role: Mathia prior-art anchor for the classical zero-detecting/zero-density mechanism and its evidence boundary.

## Zero additive energy

- D. R. Heath-Brown, **Zero Density Estimates for the Riemann Zeta-Function and Dirichlet L-Functions**, *Journal of the London Mathematical Society* (2) 19:2 (1979), 221–232. Role: classical near-critical fixed-`sigma` additive-energy bound retained as the current best ANTEDB entry on `1/2 <= sigma <= 2/3`; load-bearing input for `ANF-001`.
- Tao--Trudgian--Yang / ANTEDB above. Role: current improved additive-energy bounds beginning at `sigma=7/10`, and the exact fixed-`sigma` definition of `A^*(sigma)` used to distinguish deep-strip improvements from microscopic near-line uniformity.

## Critical-line proportions and mollifiers

- [`research/prior_art/levinson-conrey-mollifier-method.md`](../prior_art/levinson-conrey-mollifier-method.md). Role: retained primary-source-backed anchor for the Levinson–Conrey method, longer mollifiers, mean-value asymptotics, Kloosterman control, and variational optimization.

## Unconditional pair correlation and horizontal information

- Youness Lamzouri, **A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line**, arXiv:2609.02882v1, 2 September 2026. Role: primary source for `ANF-002`; gives the conjugation-invariant Hilbert-space inequality, direct unconditional pair-correlation proof of the `0.6725007...` simple-critical proportion, derivative removal of the BGSST weight, and the explicit statement that the Montgomery--Taylor constant is optimal for the one-factor squared-kernel method.
- Siegfred A. C. Baluyot, Daniel A. Goldston, Ade Irma Suriajaya and Caroline L. Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357–376, DOI `10.4064/aa230612-20-3`; arXiv:2306.04799. Role: unconditional complex-zero pair-correlation formula used by Lamzouri and the current support-one analytic evaluation boundary.
- Siegfred A. C. Baluyot, Daniel A. Goldston, Ade Irma Suriajaya and Caroline L. Turnage-Butterbaugh, **Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros**, arXiv:2501.14545, current revision 1 September 2026. Role: predecessor horizontal pair-correlation mechanism under a narrow-box hypothesis and comparison point for Lamzouri's removal of termwise strip positivity.
- Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, **Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function**, *Journal für die reine und angewandte Mathematik* 725 (2017), 143–182. Role: extremal Hilbert-space result giving the Montgomery--Taylor lower bound on the one-factor quadratic constant; exact ceiling used in `ANF-002`.
- Andrés Chirre, Felipe Gonçalves and David de Laat, **Pair correlation estimates for the zeros of the zeta function via semidefinite programming**, *Advances in Mathematics* 361 (2020), 106926. Role: RH-conditional enlargement from compact Fourier support to a Cohn--Elkies/semidefinite sign class, yielding the `1.3208` multiplicity constant and `0.6792` simple-zero proportion; closest established comparison for a possible richer unconditional quadratic certificate beyond the Montgomery--Taylor class.
- [`research/prior_art/montgomery-pair-correlation.md`](../prior_art/montgomery-pair-correlation.md). Role: retained anchor separating proved restricted pair-correlation information from conjectural full correlation and random-matrix extrapolation.

## Positive-definite Fourier--Laplace structure

- Jorge Buescu, A. C. Paixão and A. Symeonides, **Complex Positive Definite Functions on Strips**, *Complex Analysis and Operator Theory* 11:3 (2017), 627–649, DOI `10.1007/s11785-015-0527-y`. Role: classical characterization of holomorphic positive-definite strip functions as Fourier--Laplace transforms of positive exponentially finite measures, unifying the Bochner and Widder sections; prior-art boundary for `ANF-012`, which derives the needed spectral positivity from universal affine conjugation-invariant counting rather than assuming positive definiteness.

## Translation-invariant vector kernels

- C. Carmeli, E. De Vito, A. Toigo and V. Umanità, **Vector valued reproducing kernel Hilbert spaces and universality**, *Analysis and Applications* 8 (2010), 19–61, DOI `10.1142/S0219530510001503`. Role: classical feature-map and operator-valued Bochner description of translation-invariant vector-valued kernels; prior-art boundary for `ANF-003`, clarifying that common-translation vectorization followed by scalar Gram compression is redundant while genuinely operator-valued spectral data can remain richer.

## Local ordered-gap and block certificates

- `anthropics/zeta-23-lean`, Lean 4 companion development for arXiv:2608.13637. Role: formal source of the unconditional baseline `H = 3/2 - (1/sqrt(2)) cot(1/sqrt(2)) = 0.672500703679...` and the analytic/stability infrastructure consumed by later local-gap refinements.
- Thomas Lince / `teal-sea/zeta-lab`, `lean/bridge` development, frozen Palomar source commit `84312e4477dfeb7e0d8a91c38897f225f5a52f19`, registered as `PALOMAR-2026-08-25-000005` on 25 August 2026. Role: primary formal-artifact anchor for `ANF-006`--`ANF-009`; proves the parametric `n_point_bound` bridge, fixes its exact `F` and `Phi_n` definitions and block cap, discharges the three- and four-point finite gap certificates inside Lean, and yields the unconditional four-point proportion `0.6728470197666887...`; the eight-point theorem explicitly retains its finite-certificate hypothesis.
- `teal-sea/zeta-lab`, `lean/bridge/AXIOM-AUDIT.md`, current audit record dated through 31 August 2026. Role: pinned evidence boundary for the advertised bridge surface: no `sorryAx` in the proved declarations and only standard choice/propositional-extensionality/quotient axioms; explicitly notes that this does not make the conditional eight-point certificate unconditional.
- Thomas Lince / `teal-sea/zeta-lab`, `hunts/family_wall/FAMILY-LIMIT.md`, inspected at repository commit `c140868c2780d19187134e0f8f9f5f00d8b72cb9` (2 September 2026). Role: public research-artifact prior art for `ANF-009`; independently studies the same `n_point_bound` pressure family, records its asymptotic return to `H`, and derives a stronger finite all-`n` numerical envelope after an adversarial repair. It is neither a Palomar theorem nor peer review and is used only to classify prior art and compare boundaries, not as proof of `ANF-009`.
- Ainta, `ainta/zeta-simple-zeros`, seven-point local-gap refinement as audited and generalized by the `zeta-lab` bridge. Role: prior-art origin of the consecutive-gap/block-defect mechanism; its larger numerical certificate remains an external finite inequality rather than an unconditional Lean theorem in the bridge.

## Expansion rule

Add a source here only when it becomes a durable dependency for a canonical finding or a repeated falsification boundary. Recent preprints should be anchored only after the line has identified the exact load-bearing theorem or estimate being used.
