# Visual-exploration source anchors

This file records durable external literature dependencies used to support or delimit canonical findings in `research/visual_exploration/`. It is an anchor list, not search history.

## Invariant-subspace perturbation geometry

- Chandler Davis and W. M. Kahan, **The Rotation of Eigenvectors by a Perturbation. III**, *SIAM Journal on Numerical Analysis* 7:1 (1970), 1–46. DOI: `10.1137/0707001`. Role: classical reference for principal angles and perturbation of invariant subspaces; prior-art boundary for the projector-angle language used in `VIS-005`. The commutator lower bound in that finding is elementary and is not claimed as a new general perturbation theorem.

## Reciprocal-prime asymptotics

- Franz Mertens, **Ein Beitrag zur analytischen Zahlentheorie**, *Journal für die reine und angewandte Mathematik* 78 (1874), 46–62. DOI: `10.1515/crll.1874.78.46`. Role: classical reciprocal-prime asymptotic underlying the shifted sieve product `prod_{7<=p<=x}(1-1/(p-2)) = Theta(1/log x)` in `VIS-005`; the shift from `p` to `p-2` changes the logarithm only by an absolutely convergent `O(sum_p p^-2)` correction.

## Local analytic-zero normal form

- NIST Digital Library of Mathematical Functions, **§1.10(i) Taylor's Theorem for Complex Variables — Zeros**, https://dlmf.nist.gov/1.10. Role: authoritative standard reference for the definition of zero multiplicity by the first nonzero Taylor coefficient; prior-art boundary for the local factorization and universal rescaled zero portrait in `VIS-008`.

## Riemann-xi reflection symmetry

- NIST Digital Library of Mathematical Functions, **§25.4 Reflection Formulas**, https://dlmf.nist.gov/25.4. Role: authoritative definition of Riemann's `xi` function and its reflection functional equation; together with ordinary conjugation symmetry, this is the classical input for the reflection-fixed Taylor-coefficient constraints in `VIS-009` and `VIS-011`.

## Riemann-zeta zero geometry

- NIST Digital Library of Mathematical Functions, **§25.10(i) Riemann Zeta Function — Zeros — Distribution**, https://dlmf.nist.gov/25.10. Role: authoritative reference for the critical strip, zero symmetries, critical line, and statement of RH used as contextual boundaries in `VIS-008`, `VIS-009`, `VIS-011`, `VIS-012`, `VIS-013`, and `VIS-014`; none of those local identities assumes RH unless explicitly stated as a conditional specialization.

## Hadamard zero moments and Lehmer pairs

- George Csordas, Wayne Smith, and Richard S. Varga, **Lehmer pairs of zeros, the de Bruijn-Newman constant Lambda, and the Riemann Hypothesis**, *Constructive Approximation* 10:1 (1994), 107–129. DOI: `10.1007/BF01205170`. Role: canonical-product and inverse-square zero-interaction prior art for `VIS-012`. Their equation (1.7) gives the relevant even canonical product, equation (1.12) defines the inverse-square interaction `g_k(0)`, and equation (1.11) gives the Lehmer-pair threshold. `VIS-012` uses these to show that the gap-normalized average second log-residual curvature is an affine re-expression of the classical Lehmer quantity rather than a new visual invariant.

## Poisson harmonic extension

- **Encyclopedia of Mathematics**, *Poisson integral*, https://encyclopediaofmath.org/wiki/Poisson_integral. Role: standard reference for harmonic reconstruction in a disk from boundary data; prior-art boundary for `VIS-013`, which applies this classical Poisson-semigroup relation to zero-normalized `xi` log-modulus shells.
- **Encyclopedia of Mathematics**, *Abel–Poisson summation method*, https://encyclopediaofmath.org/wiki/Abel%E2%80%93Poisson_summation_method. Role: standard Fourier-series form of Poisson extension, with radial multiplier `r^k` on angular mode `k`; supports the exact Fourier-mode scaling used in `VIS-013`.

## Jensen zero-counting formula

- Elias M. Stein and Rami Shakarchi, **Complex Analysis**, Princeton Lectures in Analysis II, Princeton University Press (2003), Chapter 5 §1, pp. 135–137. Role: standard Jensen formula relating the logarithmic circular mean of a holomorphic function to the moduli of the zeros inside the disk; prior-art boundary for `VIS-014`, which uses the formula to show that the circular-mean zero-entry profile is exactly a transform of centered radial zero distances.

## Poisson–Jensen zero-potential decomposition

- Thomas Ransford, **Potential Theory in the Complex Plane**, London Mathematical Society Student Texts 28, Cambridge University Press (1995), §4.5 “The Poisson–Jensen Formula”. Role: classical Green-function/harmonic-measure decomposition of `log|F|` into boundary harmonic data plus zero/pole sources; prior-art boundary for `VIS-015`, which rewrites the disk zero-source term in angular Fourier/log-radius coordinates and uses it as a negative control for circular-shell multiscale geometry.

## Hybrid prime/zero decompositions

- S. M. Gonek, C. P. Hughes, and J. P. Keating, **A hybrid Euler-Hadamard product for the Riemann zeta function**, *Duke Mathematical Journal* 136:3 (2007), 507–549. DOI: `10.1215/S0012-7094-07-13634-2`. Role: establishes the unconditional smoothed representation `zeta(s) = P_X(s) Z_X(s) (1 + explicit error)` with a finite von-Mangoldt prime factor and a smoothed zero factor; canonical prior-art baseline for the critical-strip scale decomposition and quotient-control obstruction in `VIS-010` and the accepted prime-phase recursive-geometry clue.

- S. M. Gonek, **Finite Euler products and the Riemann hypothesis**, *Transactions of the American Mathematical Society* 364:4 (2012), 2157–2191. DOI: `10.1090/S0002-9947-2011-05546-7`. Role: studies approximation of zeta by short finite Euler products in the critical strip and delineates the additional hypotheses/regimes under which prime truncations can approximate zeta; boundary against treating arbitrary raw partial Euler products as a convergent critical-strip recursion.

## Boundary modulus, maximum modulus, and harmonic conjugacy

- John B. Conway, **Functions of One Complex Variable I**, 2nd ed., Graduate Texts in Mathematics 11, Springer (1978). DOI: `10.1007/978-1-4612-6313-5`. Role: Chapters 7 and 11 provide the classical maximum-modulus, identity/uniqueness, and harmonic-function/harmonic-conjugate machinery used in `VIS-016` and `VIS-017`. `VIS-016` uses the regular-disk consequence that equal interior zeros plus equal full boundary modulus determine a holomorphic function up to a unimodular constant. `VIS-017` then glues those local constants across nonempty disk overlaps; no novelty is claimed for either classical complex-analysis ingredient.

## Finite-size random-matrix baselines for zeta-zero spacings

- Peter J. Forrester and Anthony Mays, **Finite-size corrections in random matrix theory and Odlyzko’s dataset for the Riemann zeros**, *Proceedings of the Royal Society A* 471:2182 (2015), 20150436. DOI: `10.1098/rspa.2015.0436`. Role: established finite-size CUE corrections for nearest-neighbor spacing statistics and accurate agreement with Odlyzko high-zero data; prior-art boundary against treating finite-height deviations from the sine-kernel limit as automatically arithmetic-specific visual structure.

- Folkmar Bornemann, Peter J. Forrester, and Anthony Mays, **Finite Size Effects for Spacing Distributions in Random Matrix Theory: Circular Ensembles and Riemann Zeros**, *Studies in Applied Mathematics* 138:4 (2017), 401–437. DOI: `10.1111/sapm.12160`. Role: further finite-size spacing-distribution analysis for circular ensembles and Riemann zeros; background for the effective finite-matrix comparison used in later consecutive-spacing work.

- Shinsuke M. Nishigaki, **Distributions of Consecutive Level Spacings of Circular Unitary Ensemble and Their Ratio: Finite-Size Corrections and Riemann ζ Zeros**, *Progress of Theoretical and Experimental Physics* 2026:2 (2026), 023A02. DOI: `10.1093/ptep/ptag006`. Role: canonical prior-art boundary for `VIS-019`. The paper derives the joint law of two consecutive CUE spacings and its finite-`N` correction, shows the `O(N^-2)` term cancels in the CUE gap-ratio distribution so its first correction is `O(N^-4)`, and compares very-high Riemann-zero data with an effective finite CUE model. The two-gap joint density agrees with the effective-CUE prediction through the displayed `O(N_e^-2)` correction, while the zeta gap-ratio deviation exposes an arithmetic `O(N_e^-3)` correction. Raw adjacent-gap return maps and ratio histograms are therefore baseline spectral-statistics views, not by themselves new visual invariants.

## Conditional-dependence and higher-order-spacing baselines

- Thomas M. Cover and Joy A. Thomas, **Elements of Information Theory**, 2nd ed., Wiley (2006). DOI: `10.1002/047174882X`. Role: canonical textbook anchor for entropy, relative entropy, conditional mutual information, chain rules, conditioning inequalities, and maximum-entropy reasoning used in `VIS-020`. The identity `D(P||Q)=I(X;Z|Y)=H(Q)-H(P)` for the adjacent-pair-preserving Markov completion is an elementary specialization of this standard machinery and is not claimed as a new information-theory theorem.

- D. Herman, T. T. Ong, G. Usaj, H. Mathur, and H. U. Baranger, **Level spacings in random matrix theory and Coulomb blockade peaks in quantum dots**, *Physical Review B* 76 (2007), 195448. DOI: `10.1103/PhysRevB.76.195448`. Role: explicit random-matrix treatment of correlations involving two and three consecutive level spacings; prior-art boundary against treating raw three-gap structure as automatically new. Together with the finite-size zeta/CUE sources above, this motivates the lower-order-preserving conditional-residual test rather than a raw three-gap visualization.

## Correspondence-analysis interaction geometry

- Michael Greenacre, **Correspondence analysis**, *WIREs Computational Statistics* 2:5 (2010), 613–619. DOI: `10.1002/wics.114`. Role: canonical overview of correspondence analysis as an SVD-based visualization of contingency tables in the chi-square metric; prior-art boundary for identifying the `VIS-024` Pearson-whitened conditional residual with classical correspondence-analysis geometry in `VIS-025`.

- Marco Riani, Anthony C. Atkinson, Francesca Torti, and Aldo Corbellini, **Robust correspondence analysis**, *Journal of the Royal Statistical Society: Series C (Applied Statistics)* 71:5 (2022), 1381–1401. DOI: `10.1111/rssc.12580`. Role: explicit standard formulation `S=D_r^(-1/2)(P-r c^T)D_c^(-1/2)` and its ordinary SVD; supports the exact fiberwise identification and singular-value representation controls in `VIS-025`.

- André Carlier and Pieter M. Kroonenberg, **Decompositions and Biplots in Three-Way Correspondence Analysis**, *Psychometrika* 61:2 (1996), 355–373. DOI: `10.1007/BF02294344`. Role: established prior art for correspondence-analysis decompositions of deviations from independence in three-way contingency tables; boundary against treating the conditional-fiber SVD organization in `VIS-025` as a new general multiway correspondence-analysis method.
