# MI-041 — One Riesz order crosses the critical conditioning threshold without moving the zero discriminator

**Evidence level:** exact/literature-derived boundary statement from [AF-351](../../findings/AF-351-one-riesz-order-is-the-critical-boundary-conditioning-threshold.md), building on the singularity-fidelity calibration in [AF-350](../../findings/AF-350-riesz-error-exponents-preserve-right-half-plane-dirichlet-singularities.md)

For the Riesz profile

`R_r[Lambda-1](X)=sum_(n<=X)(Lambda(n)-1)(1-n/X)^r`,

AF-351 isolates an exact transition at the sharp `sqrt(X)` boundary. For every fixed integer `r>=1`,

`RH <=> R_r[Lambda-1](X)=O_r(sqrt(X))`,

whereas the unsmoothed case `r=0` cannot satisfy the same bound: the classical Hardy--Littlewood oscillation of `psi(X)-X` exceeds `sqrt(X)` by an unbounded `log log log X` factor along suitable sequences.

The mechanism is quantitative rather than semantic. On RH the critical zero at height `gamma` enters the order-`r` explicit formula with beta-factor amplitude `B(rho,r+1)=O_r(|gamma|^(-r-1))`. The zero count is `O(T log T)`, so `r=1` is the first integer order for which the critical zero amplitudes are absolutely summable. The frequencies `gamma` themselves are unchanged.

This gives a concrete counterexample to the idea that stronger conditioning must cost the target signal. **A transform can suppress the nuisance accumulation that makes the endpoint norm ill-conditioned while preserving the singularity locations that define the discriminator.** AF-350 guarantees the complementary direction: an `O(X^theta)` Riesz error still excludes singularities strictly to the right of `Re s=theta`.

The design rule is therefore not “preserve as much source information as possible.” It is to compare how a transformation attenuates nuisance directions with how it attenuates the exact endpoint discriminator. Here one Riesz factor changes the high-zero tail from the non-absolutely-summable `1/|gamma|` scale to `1/|gamma|^2` while leaving the off-critical singularity obstruction intact.

**Boundary.** This is a sharp statement for the fixed finite-order Riesz kernel and the critical `C^0` boundary norm. It does not recover prime support or coefficients, does not say `r=0` loses zero information, and does not make the `O(sqrt(X))` estimate easier: for every fixed `r>=1` that estimate is already RH-equivalent.