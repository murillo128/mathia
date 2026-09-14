# VIS-226 — strictly subcritical symmetric-taper worst-start energy has exact `y/(H log y)` scale

## Claim

Keep the midpoint-symmetric real-taper setup of `VIS-190`, `VIS-192`, `VIS-223`, `VIS-224`, and `VIS-225`. Fix `0 <= alpha < 1/2` and a fixed midpoint-symmetric real taper in the class used there, with centered transform `r_v` normalized by `r_v(0)=1`. Let

`H=H(y)->infinity`, `H log y / y -> 0`,

and define the real symmetric zero-diagonal prime matrix

`B_(p,q)=Q_y^(-1) p^(-alpha)q^(-alpha) r_v(H log(q/p))`, `p<q<=y`,

with `Q_y=sum_(p<=y) p^(-2alpha)`.

Then

`I_abs(B_(y,H))`
` = max_(epsilon_p in {+1,-1}) |epsilon^T B_(y,H) epsilon|`
` asymp_(alpha,v) y/(H log y)`.

Consequently the exact unit-modulus prime-torus worst-start objective and the real correlation SDP satisfy the same two-sided scale:

`M_abs(A_(y,H)) asymp_(alpha,v) y/(H log y)`,

`U_abs^R(B_(y,H)) asymp_(alpha,v) y/(H log y)`.

Equivalently, using `VIS-192`'s Haar scale `R_v(y,H) asymp_(alpha,v) 1/H`,

`I_abs(B_(y,H))/sqrt(R_v(y,H))`
` asymp_(alpha,v) y/(sqrt(H) log y)`,

and the same asymptotic order holds for `M_abs/sqrt(R_v)` and `U_abs^R/sqrt(R_v)`.

Thus `VIS-225`'s coherent prime-block certificate is not merely a divergent lower bound: throughout the complete strictly subcritical regime it already has the correct order of magnitude, up to constants depending only on the fixed exponent and taper.

**Evidence/status:** `EXACT-DERIVED + EXISTING-BOUND SYNTHESIS + TWO-SIDED SCALE + NO-NOVELTY-CLAIM`.

No sharp constant, exact optimizer, critical-scale theorem, supercritical theorem, access-time theorem, new Dirichlet-polynomial mean-value theorem, new Grothendieck theorem, or RH consequence is claimed.

## 1. The absolute tapered envelope gives the matching upper bound

For a midpoint-symmetric real taper, `VIS-223` gives

`kappa_v(u)=exp(iu/2) r_v(u)`

with `r_v(u)` real. Hence

`|r_v(u)|=|kappa_v(u)|`.

For any sign vector `epsilon`, symmetry and the zero diagonal give

`|epsilon^T B epsilon|`
` = |2 sum_(p<q<=y) epsilon_p epsilon_q B_(p,q)|`
` <= 2 sum_(p<q<=y) |B_(p,q)|`
` = 2 Q_y^(-1) sum_(p<q<=y) p^(-alpha)q^(-alpha)`
`     |kappa_v(H log(q/p))|`.

The final normalized sum is exactly the absolute off-diagonal envelope `O_v(y;H,T)` of `VIS-190`; its modulus is independent of `T`. Therefore

`I_abs(B_(y,H)) <= 2 O_v(y;H,T)`.

In the present regime `H log y/y ->0`, one has `H<y` for all sufficiently large `y`. The first branch of `VIS-190` then yields

`O_v(y;H,T) <<_(alpha,v) y/(H log y)`,

so

`I_abs(B_(y,H)) <<_(alpha,v) y/(H log y)`.

No new prime-pair estimate is needed. The upper bound is the already-audited absolute-envelope estimate, now applied to the real switched Hamiltonian.

## 2. Coherent prime blocks give the matching lower bound

`VIS-225` proves in exactly the same strictly subcritical regime that the near-diagonal ratio shell contains enough same-sign prime couplings to construct a block-constant sign certificate with

`I_abs(B_(y,H)) >>_(alpha,v) y/(H log y)`.

The proof partitions top-half primes into cells of width `asymp y/H`, uses continuity of `r_v` near zero to make every within-cell coupling positive, and averages one Rademacher sign per cell so that cross-cell contributions vanish in expectation while the positive within-cell mass survives.

Combining this lower bound with the `VIS-190` upper envelope gives the claimed two-sided estimate

`I_abs(B_(y,H)) asymp_(alpha,v) y/(H log y)`.

This identifies the coarse energy scale without solving the finite Ising optimization problem or identifying a maximizing sign pattern.

## 3. Torus and SDP scales follow without further arithmetic input

`VIS-224` proves pointwise for every finite midpoint-symmetric instance that

`I_abs(B) <= M_abs(A) <= U_abs^R(B) <= K_gamma^R I_abs(B)`,

where `K_gamma^R` is a universal real symmetric-Grothendieck constant. Therefore the two-sided Ising estimate transfers immediately:

`M_abs(A_(y,H)) asymp_(alpha,v) y/(H log y)`,

`U_abs^R(B_(y,H)) asymp_(alpha,v) y/(H log y)`.

Since `VIS-213` identifies `M_abs(A_(y,H))` with the exact worst-start supremum of the normalized tapered quadratic off-diagonal, the physical worst-start objective has the same order even though a one-parameter prime-log orbit need not reach a near-optimizer on any prescribed finite access time.

The conclusion concerns the supremum value, not quantitative recurrence time.

## 4. Haar normalization fixes the exact divergence rate up to constants

`VIS-192` gives

`R_v(y,H) asymp_(alpha,v) 1/H`.

Taking square roots and dividing the preceding two-sided bounds yields

`I_abs/sqrt(R_v)`
` asymp_(alpha,v) y/(sqrt(H) log y)`.

The `VIS-224` comparison gives the same order for the torus and SDP ratios. Writing

`delta_y=H log y/y ->0`,

the normalized scale is

`y/(sqrt(H) log y)=sqrt(y/log y)/sqrt(delta_y)`,

so it diverges. Unlike `VIS-225`, the present result also shows that no larger asymptotic order can be hidden in the remaining signed-shell interactions: the absolute Fourier-resolution envelope already caps the full optimization at the same scale.

## 5. Prior art and novelty boundary

No new external theorem is introduced here. The upper bound is exactly the smooth tapered Dirichlet-polynomial absolute-envelope estimate already source-audited in `VIS-190`, whose ingredients are classical Fourier localization, prime-pair sieve control, prime-number-theorem normalization, and standard Dirichlet-polynomial mean-value context. The lower bound is the Mathia block-sign certificate of `VIS-225`. The transfer from signs to the torus and real elliptope is the already-audited real symmetric Grothendieck specialization of `VIS-224`.

A targeted literature check against the classical Montgomery--Vaughan Dirichlet-polynomial/Hilbert-inequality framework and Friedland--Lim symmetric Grothendieck inequality exposes no separate novelty claim that should be attached to this squeeze. The mathematical delta is internal and specific: two previously established one-sided controls on the same prime-phase Hamiltonian match exactly in order, closing the coarse strictly subcritical energy-scale question.

Accordingly this finding claims no new general analytic-number-theory, spin-glass, semidefinite-optimization, or Grothendieck result.

## Boundaries and falsification

The exponent and taper are fixed as `y` grows. Midpoint symmetry is essential for the real switched matrix and the direct `VIS-224` Ising comparison. The strict subcritical assumptions are exactly

`H->infinity`, `H log y/y ->0`.

The result does not cover the transition `H asymp y/log y` or supercritical windows. It gives only order up to constants, not an asymptotic constant or optimizer structure. It also does not bound the time needed for the physical one-parameter prime-log orbit to approach a torus maximizer.

Falsify the finding by locating a mismatch between `|r_v|` and the `VIS-190` absolute kernel, an incorrect factor-of-two conversion from the symmetric quadratic form to the `p<q` envelope, a regime mismatch between `VIS-190` and `VIS-225`, an error in either imported bound, or an invalid use of the `VIS-224` constant-factor comparison.

## Research consequence

The strictly subcritical static energy scale is now closed more sharply than in `VIS-225`: binary signs, the exact continuous-phase torus objective, and the real correlation SDP all have order

`y/(H log y)`

and Haar-normalized order

`y/(sqrt(H) log y)`.

Further work on this exact regime should not seek another coarse bounded-versus-divergent estimate or a different relaxation merely to determine scale. Genuinely different questions are the critical/supercritical transition, sharp constants or optimizer geometry, representation-matched controls that distinguish arithmetic organization within this known scale, and quantitative one-parameter access time.