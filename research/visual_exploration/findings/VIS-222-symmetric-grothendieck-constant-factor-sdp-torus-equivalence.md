# VIS-222 — symmetric Grothendieck makes the correlation SDP a constant-factor torus surrogate

## Claim

Keep the finite complex Hermitian matrix setup of `VIS-213`--`VIS-221`. For

`M_abs(A)=max_(|z_i|=1) |z^*Az|`

and the correlation semidefinite relaxation

`U_abs(A)=max_(X>=0, diag(X)=1) |Tr(A X)|`,

one has the dimension-free two-sided comparison

`M_abs(A) <= U_abs(A) <= K_gamma^C M_abs(A)`,

where `K_gamma^C` is the complex symmetric Grothendieck constant of Friedland--Lim and their explicit bound gives

`K_gamma^C <= 8/pi - 1 < 1.547`.

Thus the correlation SDP of `VIS-221` is not merely an upper relaxation of unknown asymptotic quality. For arbitrary finite Hermitian coefficient matrices it approximates the exact unit-modulus quadratic optimum within a universal constant factor.

For the canonical prime matrices `A_(y,H)` of `VIS-213`, whose exact fixed-parameter worst-start statistic satisfies

`sup_T |M_v(y;H,T)-1| = M_abs(A_(y,H))`,

this yields

`U_abs(y,H)/K_gamma^C <= sup_T |M_v(y;H,T)-1| <= U_abs(y,H)`.

Consequently, after normalization by the exact Haar scale `sqrt(R_v(y,H))`, the SDP and exact torus problem have the same asymptotic scale up to a universal constant. In particular,

`U_abs/sqrt(R_v)=O(1)` if and only if `M_abs/sqrt(R_v)=O(1)`,

and

`U_abs/sqrt(R_v) -> infinity` if and only if `M_abs/sqrt(R_v) -> infinity`.

This corrects the one-sided interpretation left open in `VIS-221`: a divergent high-rank SDP value cannot be dismissed as an arbitrarily large relaxation gap. It already forces a comparably large exact torus optimum, up to the universal symmetric-Grothendieck factor. Rank-one tightness remains important only when the exact finite optimum or optimizer is wanted, not for deciding bounded-versus-divergent RMS-normalized scale.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL SYMMETRIC-GROTHENDIECK SPECIALIZATION + EXACT CONSTANT-FACTOR SCALE EQUIVALENCE + NO-NOVELTY-CLAIM`.

No new Grothendieck inequality, bound on the symmetric Grothendieck constant, prime-specific SDP estimate, access-time theorem, or RH consequence is claimed.

## 1. The two Mathia optimization problems are exactly the two symmetric Grothendieck seminorms

Friedland and Lim define, for a complex Hermitian matrix `A=(a_ij)`,

`||A||_gamma = max_(||x_i||=1) |sum_(i,j) a_ij <x_i,x_j>|`

and

`||A||_theta = max_(|delta_i|=1) |sum_(i,j) a_ij conjugate(delta_i) delta_j|`.

Their symmetric Grothendieck inequality states

`||A||_theta <= ||A||_gamma <= K_gamma^C ||A||_theta`

with a universal constant independent of matrix dimension and, in the complex case,

`K_gamma^C <= 8/pi - 1`.

The `theta` seminorm is exactly Mathia's fixed-modulus objective:

`||A||_theta=M_abs(A)`.

For the `gamma` seminorm, a family of unit vectors has a Hermitian Gram matrix `X>=0` with `X_ii=1`, and every such correlation matrix is realized by unit vectors in dimension at most the matrix size. Up to the harmless transpose/conjugation convention for complex Gram matrices,

`sum_(i,j) a_ij <x_i,x_j> = Tr(A X)`.

Because `A` and `X` are Hermitian, `Tr(A X)` is real. Therefore

`||A||_gamma=max_(X>=0,diag(X)=1)|Tr(A X)|`
`              =max(U_+(A),U_+(-A))`
`              =U_abs(A)`.

So the abstract inequality applies to exactly the pair of objects already present in `VIS-221`; no approximation or change of matrix is needed.

## 2. High-rank relaxation values still control the exact torus optimum

`VIS-221` correctly proves the easy side

`M_abs(A)<=U_abs(A)`

by dropping the rank-one condition `X=zz^*`. It then treated a large high-rank SDP optimum as potentially only a relaxation failure.

The symmetric Grothendieck inequality supplies the missing converse estimate:

`M_abs(A)>=U_abs(A)/K_gamma^C`.

Hence high rank can obstruct recovery of the exact optimizer, but it cannot create an unbounded multiplicative gap in the objective value. The entire correlation body may enlarge the feasible set dramatically in geometric terms while the Hermitian quadratic objective remains universally comparable to its restriction to rank-one unit-circle correlations.

This distinction is important for the current research branch. PSD stress from `VIS-221` is still an exact certificate when a particular torus phase assignment is globally optimal and the SDP is rank-one tight. But if the only question is whether the prime-phase worst-start amplitude is at Haar-RMS scale or parametrically above it, exact rank-one recovery is unnecessary.

## 3. Specialization to the prime-phase worst-start problem

`VIS-213` proves for every fixed finite `(y,H)` that the prime-log orbit is dense in the full prime torus and therefore

`sup_T |M_v(y;H,T)-1|=M_abs(A_(y,H))`.

Combining this identity with the symmetric Grothendieck comparison gives

`U_abs(A_(y,H))/K_gamma^C`
` <= sup_T |M_v(y;H,T)-1|`
` <= U_abs(A_(y,H))`.

The comparison is pointwise in `(y,H)` and its constant does not depend on the number of primes. Therefore it survives every growing-parameter regime without any uniformity loss.

Let `R_v(y,H)` be the exact Haar second moment from `VIS-192` and `VIS-213`. Dividing by `sqrt(R_v)` gives

`(1/K_gamma^C) U_abs/sqrt(R_v)`
` <= M_abs/sqrt(R_v)`
` <= U_abs/sqrt(R_v)`.

Thus the SDP/RMS ratio and the true worst-start/RMS ratio are asymptotically equivalent at the coarse scale relevant to the current clue. A bounded SDP ratio proves an RMS-scale pointwise upper bound; a divergent SDP ratio proves that the exact worst-start amplitude exceeds RMS by a divergent factor. There is no third possibility in which only the SDP diverges because of an unbounded relaxation gap.

## 4. Relation to the earlier magnetic and cycle certificates

The result does not reopen the certificate families closed in `VIS-218` and `VIS-220`. Those findings show that two particular upper-bound mechanisms — the normalized magnetic dual ansatz and simple-cycle packing — cannot reach the required RMS scale in the stated regimes.

`VIS-221` embeds the magnetic certificate as one restricted dual choice inside the full correlation SDP. `VIS-222` adds a different fact: however the full SDP value is obtained, it remains within the universal factor `K_gamma^C` of the exact torus optimum. Therefore a large magnetic upper certificate says little about the true optimum, but a large **optimal correlation SDP value** does.

This sharpens the live decision tree. The remaining task is no longer to determine whether the SDP relaxation gap itself can invalidate scale conclusions. It is to determine the actual asymptotic scale of `U_abs(A_(y,H))`, analytically or through exact finite certificates that motivate an analytic bound.

## 5. Prior art and novelty boundary

The decisive theorem is Shmuel Friedland and Lek-Heng Lim, **Symmetric Grothendieck inequality**, arXiv:2003.07345 (2020). Their equations defining the complex `gamma` and `theta` seminorms and their symmetric Grothendieck inequality give

`||A||_theta <= ||A||_gamma <= K_gamma^C ||A||_theta`

for arbitrary complex Hermitian matrices, without a positive-semidefinite assumption on `A`, and they prove the explicit bound

`K_gamma^C <= 8/pi - 1`.

No novelty is claimed for this theorem, its proof, the constant, Gram-matrix parametrization of correlation SDPs, or constant-factor approximation of Hermitian unit-modulus quadratic optimization. The Mathia-specific content is the exact dictionary

`||A_(y,H)||_theta = M_abs(A_(y,H))`

and

`||A_(y,H)||_gamma = U_abs(A_(y,H))`,

combined with `VIS-213`'s exact prime-log-orbit supremum identity. That dictionary changes the interpretation of the live prime-phase SDP question from a potentially loose certificate problem into a constant-factor surrogate for the exact static worst-start problem.

## Boundaries and falsification

The universal comparison is multiplicative, not an exact equality. It does not identify the maximizing torus phase, the SDP rank, or the finite relaxation gap. A PSD stationary stress as in `VIS-221` is still needed for the particular rank-one exactness certificate used there.

The comparison also says nothing about the **time required** for the one-parameter prime-log orbit to approach a near-maximizing torus phase. `VIS-213` identifies equality of suprema by density, but quantitative access time remains a separate simultaneous-Diophantine problem.

Nor does the theorem determine whether `U_abs/sqrt(R_v)` is bounded or divergent for the canonical prime matrices. It only proves that whichever asymptotic scale the SDP has, the exact torus optimum has the same scale up to a fixed constant.

Falsify this finding by locating a mismatch between the feasible correlation matrices in `VIS-221` and the Gram matrices in Friedland--Lim's `gamma` seminorm, a mismatch between `M_abs` and their `theta` seminorm, a failure of the complex symmetric Grothendieck theorem for arbitrary Hermitian matrices, or an error in applying `VIS-213`'s fixed-parameter torus-supremum identity.

## Research consequence

The local clue `CLUE-prime-phase-sdp-rms-tightness` remains genuinely open, but its interpretation becomes stronger. Determining the scale of the full correlation SDP now determines the scale of the exact finite torus worst-start problem within a universal factor.

The next coherent investigation should therefore estimate `U_abs(A_(y,H))/sqrt(R_v(y,H))` on the canonical prime matrices. If it stays bounded in a growing regime, the exact worst-start amplitude is at RMS scale. If it diverges, the exact worst-start amplitude also diverges relative to RMS. SDP rank and stress remain valuable diagnostics for exact finite optimization, but they are no longer prerequisites for asymptotic scale transfer.