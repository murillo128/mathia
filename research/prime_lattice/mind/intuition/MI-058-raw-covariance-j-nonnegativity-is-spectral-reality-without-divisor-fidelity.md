# MI-058 — Raw covariance J-nonnegativity gives spectral reality without divisor fidelity

**Evidence level:** exact/literature-calibrated operator synthesis from [PL-418](../../findings/PL-418-mod5-covariance-j-nonnegative-vacuity.md), sharpening the block-fidelity and indefinite-metric obstructions of PL-416--PL-417.

The repaired mod-5 source statistic has signature `(1,3)`, so retaining it in an indefinite metric is necessary for the canonical block packaging. PL-417 shows that `J`-selfadjointness alone is too weak: nonreal conjugate eigenvalue pairs are compatible with that signature. PL-418 tests the natural stronger condition `JT>=0` on the raw channel covariance and finds the opposite failure: it is automatic.

Let

`C = sum_x A_x A_x^* >= 0`,

`D = diag(15,-1,-1,-1) = R J R`,

with `R=diag(sqrt(15),1,1,1)` and `J=diag(1,-1,-1,-1)`. Setting `B=R C R` and `T=J B` preserves the raw signed supertrace through `tr(T)`, but

`J T = B >= 0`

for every possible collection of channel vectors. The Hermitian representative `B^(1/2) J B^(1/2)` has the same characteristic polynomial, so `T` has real spectrum independently of primes, multiplicativity, an explicit formula or zero locations. Diagonal positive `B` can prescribe the real eigenvalue magnitudes arbitrarily subject only to the `(1,3)` inertia. Raw covariance reality is therefore arithmetic-blind and survives matched off-line controls.

The required source/model subtraction removes this automatic positivity. Writing the Hermitian residual as

`H = C - C_model`, `T_res = J R H R`,

one has the exact equivalence

`J T_res >= 0  <=>  H >= 0  <=>  C >= C_model`

in Loewner order. The missing spectral condition is therefore a **four-channel matrix coercivity theorem**, not something inherited from the raw Gram representation.

Crucially, the signed scalar target does not imply that matrix order. The explicit PL-418 witness

`H_0 = [[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]]`

has `tr(D H_0)=0`, yet the canonical residual lift has eigenvalues `+/- i sqrt(15),0,0`. Moreover `H_0` is itself a difference of two positive rank-one Gram matrices. More generally every Hermitian residual is a difference of positive covariances. Thus neither “covariance minus covariance” nor exact success on the one signed supertrace can supply residual `J`-nonnegativity.

The reusable distinction is now threefold: **preserve the block statistic, prove the analytic scalar estimate, and localize the divisor spectrally are separate gates**. Proving the PL-407-scale signed supertrace estimate would solve the current source-replacement problem, but it would not by itself produce a Hilbert--Pólya reality theorem. A viable operator route needs additional matrix-level coercivity or an explicit divisor attachment that excludes the zero-trace nonreal witness and fails under an off-line matched control.

**Boundary.** PL-418 classifies the canonical covariance and residual `J`-lifts; it does not prove that every operator preserving the four mod-5 blocks is spectrally vacuous. The explicit residual witness is a structural control, not a claim that the actual Hardy--Littlewood residual realizes every Hermitian matrix. If arithmetic imposes an extra matrix relation excluding that witness, proving and transporting that relation is precisely the additional mathematics required. No RH theorem follows from the representation alone.
