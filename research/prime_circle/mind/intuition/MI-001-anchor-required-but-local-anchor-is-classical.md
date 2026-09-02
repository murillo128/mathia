# MI-001 — Finite canonical circle compressions and standard spectralizations repeatedly classicalize

**Evidence level:** supported by exact structural reductions, Fourier identities, and classical cyclotomic/Farey/Toeplitz/OPUC controls

## Core intuition

Breaking rotational symmetry by naming vertices or retaining old/new structure is necessary to avoid the coarsest Prime-Circle quotients, but neither finite combinatorial complexity, fixed translation-invariant nonlocality, nor standard finite-section spectral machinery is enough to create a new arithmetic channel. The current evidence closes three large classes: finite cotangent networks reduce to endpoint/cyclotomic algebra, cumulative primitive-root kernel statistics reduce to classical Farey/Mertens Fourier data, and natural Toeplitz/CMV/resultant spectralizations of finitely many cyclotomic shells reduce to finite-period, finite-state, or tautological cyclotomic data.

## Strongest justified principle

PC-090--PC-097 close the finite cotangent sector. Reflection parity, Galois-rational complete-shell contractions, arbitrary diagonal shell weights, cycles, parallel edges, repeated shells, and collision strata all reduce by exact confluent elimination to one-body endpoint Cauchy/cyclotomic data. PC-098 then shows that fixed finite shell support with arbitrary composition depth is finite-state by Cayley--Hamilton, and PC-099 shows that canonical complete-preimage growth has universal affine-band limits determined by the base spectrum.

PC-105 supplies a distinct nonlocal control. The cumulative primitive-root cloud is exactly the Farey cloud, and its Fourier coefficients are finite divisor transforms of the Mertens function. In particular `nu_N^(1)=M(N)/A_N`, so the familiar RH-sensitive rate is already the classical Mertens criterion. Every fixed translation-invariant positive kernel on the circle packages the same summatory Ramanujan/Mertens modes in a weighted `l^2` norm.

PC-121--PC-125 now close the most natural finite-shell spectralization escape. For the scalar symbol `|Phi_n|^2`, the Toeplitz determinant is an exact quasipolynomial in section size with period dividing `n`; its ordinary generating function is rational and its leading term is the cyclotomic discriminant. The coherent multi-shell matrix symbol `p p^*` is overcomplete: its block determinant becomes identically zero beyond a finite dimension threshold and the last two-shell nonsingular section is a cyclotomic resultant. Passing to the canonical pseudodeterminant removes the off-diagonal shell coherence and leaves a fixed-band scalar recurrence with rational generating function.

The alternative OPUC/CMV spectralization is equally rigid. Equal mass on primitive roots has normalized Ramanujan moments; the finite CMV spectrum is exactly the primitive roots supplied as input and its characteristic polynomial is `Phi_n`. Finally, promoting a pairwise shell resultant to a relative complex scale does create a divisor, but every zero is a root-of-unity ratio and the whole divisor factors into ordinary cyclotomic polynomials with Ramanujan-correlation multiplicities.

These results are complementary. Finite topology, convolutional nonlocality, and standard finite-shell spectral machinery can all look richer while remaining functions of the same finite cyclotomic/Fourier information layer.

## What remains possible

A surviving Prime-Circle mechanism must use structure not already determined by endpoint/cyclotomic elimination, cumulative Fourier data, or finite polynomial spectralization. Possibilities include a genuinely cross-level operator retaining provenance before finite-shell compression, an independently forced incomplete growing family, a singular/domain-changing completion, or a global coupling whose operator ideal and spectral data are not fixed by finite-state polynomial algebra.

Any candidate should first prove nonfactorization through the closed classes above. Rewriting Mertens discrepancy in a positive kernel norm, replacing a finite shell by its CMV matrix, increasing Toeplitz section size at fixed conductor, taking a pseudodeterminant of the one-channel coherent lift, or promoting a resultant by a single relative scale no longer qualifies.

## Status / novelty

The reductions use persisted exact findings and classical cotangent, Ramanujan, Farey, Mertens, Toeplitz, resultant, and OPUC/CMV theory. The synthesis is a closure statement for the audited canonical finite/convolutional/spectralized Prime-Circle sectors, not a theorem about every possible circle operator.

## Falsification criterion

Exhibit a canonical object covered by PC-090--PC-125 whose invariant is not determined by the stated endpoint/Fourier/cyclotomic finite-state data, or derive a new cross-level spectral variable before those reductions apply and prove that it survives matched non-arithmetic controls.

## Lean-formalizable core

- Confluent partial-fraction elimination of finite cotangent networks.
- Fixed-state Cayley--Hamilton recurrence.
- Exact cumulative Ramanujan/Mertens Fourier identity.
- Toeplitz finite-section quasipolynomial/rank reductions.
- Gram pseudodeterminant reduction to an output frame operator.
- Primitive-root moment/CMV characteristic-polynomial identity.
- Cyclotomic factorization of the relative-scale resultant.
