# MI-072 — History is a fidelity resource only after nuisance quotient and noise coupling

**Evidence level:** exact deterministic minimax synthesis from [AF-489](../../findings/AF-489-global-lp-relative-noise-has-sharp-horizon-sample-accumulation-law.md) and [AF-490](../../findings/AF-490-nuisance-quotients-replace-depth-by-transverse-spread.md), refining the pointwise-noise horizon obstruction of MI-071.

For the linearized observation model

`z = v - theta s + u`, with `v in V` and `||u||_p <= rho`,

AF-490 identifies the exact deterministic minimax radius as

`R_p = rho / d_p(s,V)`, where `d_p(s,V)=inf_(v in V)||s-v||_p`.

The relevant sensitivity is therefore not the raw sampling vector but its class in the quotient by nuisance directions. Equivalently, an optimal dual witness annihilates `V` and measures only the component of `s` that survives nuisance elimination. If `d_p(s,V)=0`, the target is non-identifiable because its displacement can be absorbed entirely by the nuisance.

AF-489 is the zero-nuisance special case `V={0}`. For one known-amplitude Dirichlet atom, a fixed global relative-error budget gives `R=Theta(epsilon/||s||_p)`, so on a fixed-step expanding lattice the radius is `Theta(H^(-1-1/p))` for finite `p` and `Theta(H^-1)` for `p=infinity`. Sample accumulation helps only because the growing observation family shares one non-growing coupled budget.

Unknown positive amplitude changes the resource before the noise geometry is even priced. After logarithms the nuisance is `V=span{1}`, so the sharp additive sensitivity is

`d_p(s,span{1}) = inf_c ||s-c 1||_p`.

A common translation `s -> s+t1` leaves this quantity unchanged, and in the original multiplicative model the shift is absorbed exactly by reparametrizing the amplitude. Thus moving a fixed-width window to larger absolute depth creates no information when amplitude is unrestricted. On an expanding fixed-step prefix the AF-489 powers survive for a different reason: the centered span of the sample locations grows, and for finite `p` the number of samples enlarges that centered `ell_p` spread.

The reusable resource test therefore has two ordered gates. First quotient target sensitivity by every nuisance symmetry of the actual observation model; only the surviving transverse discriminator can count as information. Then compare that quotient sensitivity with the admissible cross-sample noise budget. Raw depth, sample count, or horizon are fidelity resources only insofar as they enlarge `d_p(s,V)` faster than the adversary's budget.

**Boundary.** The identity `rho/d_p(s,V)` is exact for the finite-dimensional additive norm-bounded channel. AF-490 transfers it to the stated multiplicative relative-noise model only up to constants after logarithms, although common-shift equivalence with unrestricted positive amplitude is exact. Bounds or priors on the nuisance, signed/complex source classes, stochastic or correlated noise, growing-depth Dirichlet inversion, and rational-prime provenance require separate evidence.