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

- NIST Digital Library of Mathematical Functions, **§25.10(i) Riemann Zeta Function — Zeros — Distribution**, https://dlmf.nist.gov/25.10. Role: authoritative reference for the critical strip, zero symmetries, critical line, and statement of RH used as contextual boundaries in `VIS-008`, `VIS-009`, `VIS-011`, and `VIS-012`; none of those local identities assumes RH unless explicitly stated as a conditional specialization.

## Hadamard zero moments and Lehmer pairs

- George Csordas, Wayne Smith, and Richard S. Varga, **Lehmer pairs of zeros, the de Bruijn-Newman constant Lambda, and the Riemann Hypothesis**, *Constructive Approximation* 10:1 (1994), 107–129. DOI: `10.1007/BF01205170`. Role: canonical-product and inverse-square zero-interaction prior art for `VIS-012`. Their equation (1.7) gives the relevant even canonical product, equation (1.12) defines the inverse-square interaction `g_k(0)`, and equation (1.11) gives the Lehmer-pair threshold. `VIS-012` uses these to show that the gap-normalized average second log-residual curvature is an affine re-expression of the classical Lehmer quantity rather than a new visual invariant.

## Hybrid prime/zero decompositions

- S. M. Gonek, C. P. Hughes, and J. P. Keating, **A hybrid Euler-Hadamard product for the Riemann zeta function**, *Duke Mathematical Journal* 136:3 (2007), 507–549. DOI: `10.1215/S0012-7094-07-13634-2`. Role: establishes the unconditional smoothed representation `zeta(s) = P_X(s) Z_X(s) (1 + explicit error)` with a finite von-Mangoldt prime factor and a smoothed zero factor; canonical prior-art baseline for the critical-strip scale decomposition and quotient-control obstruction in `VIS-010` and the accepted prime-phase recursive-geometry clue.

- S. M. Gonek, **Finite Euler products and the Riemann hypothesis**, *Transactions of the American Mathematical Society* 364:4 (2012), 2157–2191. DOI: `10.1090/S0002-9947-2011-05546-7`. Role: studies approximation of zeta by short finite Euler products in the critical strip and delineates the additional hypotheses/regimes under which prime truncations can approximate zeta; boundary against treating arbitrary raw partial Euler products as a convergent critical-strip recursion.