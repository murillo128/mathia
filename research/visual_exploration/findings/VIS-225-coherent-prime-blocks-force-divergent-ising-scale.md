# VIS-225 — coherent prime blocks force divergent symmetric-taper Ising scale

## Claim

Keep the strictly subcritical prime-phase setup of `VIS-190`--`VIS-192`, the midpoint-symmetric real taper reduction of `VIS-223`, and the Ising objective of `VIS-224`. Thus

`0 <= alpha < 1/2`,

`H=H(y)->infinity`, `H log y / y -> 0`,

and for a fixed midpoint-symmetric real taper with normalized centered transform `r_v(0)=1`,

`B_(p,q)=Q_y^(-1) p^(-alpha)q^(-alpha) r_v(H log(q/p))`, `p<q<=y`,

with zero diagonal and

`Q_y=sum_(p<=y) p^(-2alpha)`.

Define

`I_abs(B)=max_(epsilon_p in {+1,-1}) |epsilon^T B epsilon|`.

Then there is a constant `c_(alpha,v)>0` such that, for all sufficiently large `y`,

`I_abs(B_(y,H)) >= c_(alpha,v) y/(H log y)`.

Consequently, throughout the whole strictly subcritical regime,

`I_abs(B_(y,H)) -> infinity`.

Moreover `VIS-192` gives

`R_v(y,H) asymp_(alpha,v) 1/H`,

so

`I_abs(B_(y,H))/sqrt(R_v(y,H))`
` >>_(alpha,v) y/(sqrt(H) log y)`
` -> infinity`.

By `VIS-224`, the exact continuous-phase torus optimum and the full real correlation SDP have the same bounded-versus-divergent normalized scale up to a universal constant. Therefore the exact symmetric-taper worst-start objective also diverges relative to Haar RMS throughout the strictly subcritical regime.

**Evidence/status:** `EXACT-DERIVED + PNT/FOURIER-LOCALIZATION SPECIALIZATION + PROBABILISTIC-METHOD SIGN CERTIFICATE + NO-NOVELTY-CLAIM`.

No new prime-gap theorem, general Ising theorem, Dirichlet-polynomial large-value theorem, Grothendieck theorem, or RH consequence is claimed.

## 1. Near-diagonal ratio cells have a fixed positive coupling sign

Midpoint symmetry gives a real even centered taper response `r_v`; normalization gives `r_v(0)=1`. By continuity there are fixed constants `eta_v,c_v>0` such that

`r_v(u)>=c_v`

whenever `|u|<=eta_v`.

As in the same-cell argument of `VIS-218`, partition `(y/2,y]` into intervals of length

`ell=eta_v y/(8H)`.

Let their prime occupancies be `n_1,...,n_J`. Then `J<<_v H`. If `p<q` lie in the same cell, `p>=y/2` and `q-p<=ell`, hence

`H log(q/p) <= 2H(q-p)/y <= eta_v/4`.

Therefore every such edge has positive coupling and

`B_(p,q) >= c_v Q_y^(-1) y^(-2alpha)`.

The PNT/partial-summation normalization already used in `VIS-192` and `VIS-218` gives

`Q_y asymp_alpha y^(1-2alpha)/log y`,

so each same-cell edge contributes

`B_(p,q) >>_(alpha,v) log y/y`.

This is a signed statement, stronger for the present purpose than the absolute-value edge estimate in `VIS-218`: the unresolved local ratio shell around `u=0` is uniformly ferromagnetic after the midpoint gauge.

## 2. Strict subcriticality forces many coherent same-cell pairs

Put

`m=pi(y)-pi(y/2)=(1/2+o(1))y/log y`.

Cauchy gives

`sum_j binom(n_j,2)`
` = (sum_j n_j^2-m)/2`
` >= (m^2/J-m)/2`.

Because

`m/J >>_v y/(H log y) -> infinity`,

the total number of same-cell prime pairs is

`>>_v y^2/(H (log y)^2)`.

Multiplying by the preceding lower edge weight shows that the total positive coupling mass internal to these cells satisfies

`sum_j sum_(p<q in C_j) B_(p,q)`
` >>_(alpha,v) y/(H log y)`.

This is the same population mechanism that underlies the `VIS-218` effective-edge lower bound, but here its common sign is used rather than discarded by absolute values.

## 3. Block Rademacher signs isolate the positive local mass

Assign one independent Rademacher variable `sigma_j` to every top-half cell and set

`epsilon_p=sigma_j` for `p in C_j`.

For primes `p<=y/2`, assign independent Rademacher signs individually, independent also of all `sigma_j`.

For distinct primes, the sign product has expectation

`E[epsilon_p epsilon_q]=1`

when `p,q` lie in the same top-half cell, and `0` otherwise. Since `B` has zero diagonal,

`E[epsilon^T B epsilon]`
` = 2 sum_j sum_(p<q in C_j) B_(p,q)`
` >>_(alpha,v) y/(H log y)`.

Hence at least one deterministic sign assignment realizes at least this expectation. Therefore

`I_abs(B) >= max_epsilon epsilon^T B epsilon`
` >>_(alpha,v) y/(H log y)`.

No optimization algorithm or independence assumption about the prime couplings is used. Randomization is only an averaging device that cancels unwanted cross-cell terms while keeping every coherent near-diagonal pair.

## 4. The Haar-RMS-normalized Ising scale diverges

`VIS-192` proves in the same regime

`R_v(y,H) asymp_(alpha,v) 1/H`.

Combining with the block-sign certificate gives

`I_abs(B)/sqrt(R_v)`
` >>_(alpha,v) y/(sqrt(H) log y)`.

Write

`delta_y=H log y/y`.

Strict subcriticality is `delta_y->0`, and

`y/(sqrt(H) log y)`
` = sqrt(y/log y)/sqrt(delta_y)`
` -> infinity`.

Thus the accepted question in `CLUE-prime-phase-sdp-rms-tightness` has a decisive answer on its stated regime: the binary sign Hamiltonian cannot stay at Haar-RMS scale.

By the pointwise comparison in `VIS-224`,

`I_abs(B) <= M_abs(A) <= U_abs^R(B) <= K_gamma^R I_abs(B)`.

Therefore `M_abs(A)/sqrt(R_v)` and `U_abs^R(B)/sqrt(R_v)` diverge as well. Continuous phases and higher-rank SDP correlations are not responsible for the divergence; a coarse block-constant binary assignment already forces it.

## 5. Prior-art and novelty boundary

The analytic inputs are classical and already source-audited in the preceding branch. `VIS-192` supplies the long-start variance scale through standard Dirichlet-polynomial orthogonality and Fourier localization. `VIS-218` supplies the top-half cell population and PNT normalization. Classical mean- and large-value theory for Dirichlet polynomials, including Montgomery's 1969 work and the Montgomery--Vaughan Hilbert-inequality framework, is broad prior-art background for phase coherence and quadratic mean estimates; no new general theorem in that literature is asserted here.

The additional step is elementary: group nearby prime frequencies into cells on which the centered taper kernel has one positive sign, then average independent signs across cells so only the positive within-cell mass survives in expectation. The Mathia-specific consequence is that the already-established prime-cell population turns this elementary certificate into a divergent lower bound for the exact `VIS-224` Ising/worst-start scale.

No novelty claim is made for block randomization, the probabilistic method, PNT partial summation, or the underlying Dirichlet-polynomial machinery.

## Boundaries and falsification

The exponent and taper are fixed; constants are not uniform as `alpha->1/2` or over varying taper families. Midpoint symmetry is used to make the switched kernel real, and continuity plus `r_v(0)=1` supplies the positive local shell. The proof applies in the same strict subcritical regime as `VIS-192` and `VIS-218`; it does not address the critical transition `H asymp y/log y` or supercritical windows.

The argument does not identify an exact maximizing sign pattern. It proves existence through averaging over block-constant signs. It also does not solve the separate one-parameter access-time problem of whether the physical prime-log orbit reaches a near-maximizing torus point within a prescribed start range.

Falsify the finding by locating an error in the positive-shell reduction, same-cell pair count, lower coupling weight, block-sign expectation, the imported `R_v asymp 1/H` scale, or the `VIS-224` constant-factor transfer.

## Research consequence

The strictly subcritical static worst-start question is closed at the bounded-versus-divergent level: symmetric-taper prime Hamiltonians have a binary sign certificate whose energy already exceeds Haar RMS by a diverging factor.

Any continuation of this branch should therefore move to a genuinely different question: the critical/supercritical transition, quantitative optimizer structure, representation-matched controls for the size of the divergence, or one-parameter prime-log access time. Extending the same strictly subcritical boundedness test would be redundant.