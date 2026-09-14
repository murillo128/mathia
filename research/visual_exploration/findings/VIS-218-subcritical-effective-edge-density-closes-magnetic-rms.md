# VIS-218 — subcritical prime graphs have too many effective edges for the normalized magnetic RMS route

## Claim

Keep the prime-phase coefficient matrix `A_(y,H)` from `VIS-213` and the fixed taper/exponent hypotheses of `VIS-190`--`VIS-192`:

`0 <= alpha < 1/2`,

`v in C^2([0,1])` real with `v(0)=v(1)=0` and `V=int_0^1 v != 0`,

and

`H=H(y)->infinity`, `H log y / y -> 0`.

For each support edge `e={p,q}`, `p<q<=y`, write

`w_e=|A_(p,q)|`
`   = Q_y^(-1) p^(-alpha) q^(-alpha) |kappa_v(H log(q/p))|`,

where

`Q_y=sum_(p<=y) p^(-2alpha)`.

Put

`W_1=sum_e w_e`,

`W_2=sum_e w_e^2`,

and

`N_eff=W_1^2/W_2`.

Then throughout the strictly subcritical regime,

`W_1 asymp_(alpha,v) y/(H log y)`,

`W_2 asymp_(alpha,v) 1/H`,

and consequently

`N_eff asymp_(alpha,v) y^2/(H (log y)^2)`.

Let `n(y,H)` be the number of nonisolated vertices in the support graph of `A_(y,H)`. Since `n(y,H)<=pi(y)`,

`N_eff/n(y,H) >>_(alpha,v) y/(H log y) -> infinity`.

Therefore the normalized magnetic spectral relaxation of `VIS-216`--`VIS-217` is parametrically too weak to certify Haar-RMS-scale worst-start suppression anywhere in this strictly subcritical regime. If

`U_spec=B(A)-min(S_+,S_-)`

is its spectral upper certificate and

`R(A)=2 sum_e w_e^2=R_v(y,H)`,

then

`U_spec/sqrt(R_v(y,H))`
` >= sqrt(2 N_eff/(n(y,H)-1))`
` >>_(alpha,v) sqrt(y/(H log y))`
` -> infinity`.

Thus no choice of prime-edge phases, cycle holonomies, or magnetic ground states can make **this normalized spectral relaxation** prove

`max_(|z_p|=1)|z^*A_(y,H)z|=O(sqrt(R_v(y,H)))`

in the strictly subcritical regime. This does not lower-bound the exact torus optimum beyond the generic RMS floor and does not close the stronger fixed-modulus or cycle-packing routes.

**Evidence/status:** `EXACT-DERIVED + PNT/FOURIER-LOCALIZATION SPECIALIZATION + NEGATIVE RELAXATION CLOSURE + NO-NOVELTY-CLAIM`.

No new prime-pair theorem, magnetic-Laplacian theorem, effective-dimension theorem, or RH consequence is claimed.

## 1. The coefficient `L1` mass is exactly the absolute envelope

For `p<q`, `VIS-213` defines

`A_(p,q)=Q_y^(-1) p^(-alpha) q^(-alpha) kappa_v(H log(q/p))`.

Hence

`W_1`
` = Q_y^(-1) sum_(p<q<=y) p^(-alpha)q^(-alpha)|kappa_v(H log(q/p))|`.

After the change of variables in `VIS-190`--`VIS-191`, this is exactly their start-independent absolute envelope:

`W_1=O_v(y;H,T)`.

`VIS-190` already supplies the upper bound, valid eventually because strict subcriticality implies `H<=y`,

`W_1 <<_(alpha,v) y/(H log y)`.

The matching lower scale is stronger than the consecutive-prime floor recorded in `VIS-191`; it is already latent in the same-bin population used to prove the `VIS-192` variance lower bound.

## 2. Fourier-unresolved top-half cells force the matching `L1` lower bound

Because `kappa_v(0)=1`, choose constants `eta_v,c_v>0` such that

`|kappa_v(theta)|>=c_v`

for `|theta|<=eta_v`.

As in `VIS-192`, partition `(y/2,y]` into intervals of length

`ell=eta_v y/(8H)`.

The prime number theorem gives

`m=pi(y)-pi(y/2)=(1/2+o(1))y/log y`

primes in the top half, while the number of cells satisfies `J<<_v H`. If their occupancies are `n_1,...,n_J`, then

`sum_j binom(n_j,2)`
` = (sum_j n_j^2-m)/2`
` >= (m^2/J-m)/2`.

Since

`m/J >>_v y/(H log y) -> infinity`,

the number of same-cell prime pairs is

`>>_v y^2/(H (log y)^2)`.

For each such pair,

`H log(q/p)<=eta_v/4`,

so its taper factor is bounded below by `c_v`. Also `p,q<=y`, hence

`p^(-alpha)q^(-alpha)>=y^(-2alpha)`.

Finally the PNT/partial-summation normalization used throughout this branch gives, with `beta=1-2alpha`,

`Q_y asymp_alpha y^beta/log y`.

Thus every selected pair contributes

`>>_(alpha,v) log y/y`

to `W_1`, and therefore

`W_1 >>_(alpha,v) [y^2/(H(log y)^2)] [log y/y]`
`     = y/(H log y)`.

Combined with `VIS-190`, this proves

`W_1 asymp_(alpha,v) y/(H log y)`.

This is an `L1` statement about the coefficient envelope, not signed cancellation.

## 3. The coefficient `L2` mass is the long-start variance

`VIS-192` proves the exact identity

`R_v(y,H)=2 Q_y^(-2) sum_(p<q<=y) p^(-2alpha)q^(-2alpha)|kappa_v(H log(q/p))|^2`.

The right-hand side is exactly

`2 W_2`.

In the same strictly subcritical regime, `VIS-192` proves

`R_v(y,H) asymp_(alpha,v) 1/H`.

Hence

`W_2=R_v/2 asymp_(alpha,v) 1/H`.

The effective edge count is therefore forced to be

`N_eff=W_1^2/W_2`
` asymp_(alpha,v) [y^2/(H^2(log y)^2)]/(1/H)`
` = y^2/(H(log y)^2)`.

So the prime coefficient mass is spread over an effectively much larger edge family than the number of available prime vertices in this regime.

## 4. Effective edge density diverges relative to every possible support-vertex count

Let `n=n(y,H)` count the nonisolated prime vertices after zero-weight edges are discarded. No lower estimate for `n` is needed. Trivially

`n<=pi(y) asymp y/log y`.

Therefore

`N_eff/n`
` >= N_eff/pi(y)`
` >>_(alpha,v) y/(H log y)`.

Strict subcriticality is exactly

`H log y/y ->0`,

so

`N_eff/n -> infinity`.

If some taper zeros remove edges or even vertices, this conclusion only becomes stronger because the denominator `n` decreases while `N_eff` is already determined by the full nonzero coefficient masses above.

## 5. The `VIS-217` dimension floor now closes the spectral RMS route

For several connected support components, `VIS-217` gives

`U_spec >= sum_K B_K/sqrt(n_K-1)`.

If `n` is the total number of nonisolated vertices, then `n_K-1<=n-1`, so

`U_spec >= B(A)/sqrt(n-1)`.

Using the exact `VIS-216` normalization

`B(A)/sqrt(R(A))=sqrt(2N_eff)`

and `R(A)=R_v(y,H)`, one gets

`U_spec/sqrt(R_v)`
` >= sqrt(2N_eff/(n-1))`
` >>_(alpha,v) sqrt(y/(H log y))`
` -> infinity`.

This is stronger than the conditional diagnostic in `VIS-217`: the prime-phase graph actually lies on the forbidden side of the effective-edge/vertex ratio throughout the whole strictly subcritical regime.

The conclusion concerns the **quality of the relaxation**. Since `U_spec` is an upper bound on the exact torus optimum, proving that `U_spec` is large does not prove that the true optimum is large. The fixed-modulus torus may exploit structure that the variable-amplitude spectral relaxation discards.

## 6. Prior-art and novelty boundary

All load-bearing ingredients are already source-audited in the immediately preceding canonical findings. `VIS-190`--`VIS-192` use classical Fourier localization, the prime number theorem, elementary occupancy/Cauchy arguments, and standard Dirichlet-polynomial orthogonality. `VIS-216` anchors the connection/magnetic-Laplacian relaxation to the classical synchronization and magnetic-frustration literature, including Bandeira--Singer--Spielman and Lange--Liu--Peyerimhoff--Post. `VIS-217` derives the phase-independent normalized-adjacency dimension floor by elementary linear algebra.

The effective count `N_eff=W_1^2/W_2` is the standard inverse-concentration/participation-ratio scale already introduced and novelty-bounded in `VIS-216`. No new general effective-dimension or graph-spectral statement is asserted here.

The Mathia-specific content is the exact scale matching across those already-audited objects: the same unresolved top-half prime pairs that force `R_v asymp H^-1` also force `W_1 asymp y/(H log y)`, which makes the prime graph's effective edge count superlinear relative to its available vertices and activates the `VIS-217` obstruction automatically.

## Boundaries and falsification

The exponent `alpha` and taper `v` are fixed. Constants are not uniform as `alpha->1/2` or over varying taper families.

The scale statement requires `H->infinity` and `H log y/y->0`. It makes no claim at the constant critical transition `H asymp y/log y`, where the cell occupancy per Fourier-resolution window is only order one and the lower argument above no longer has growing multiplicity.

The result does not close the exact torus optimization of `VIS-213`, the cycle-holonomy characterization of `VIS-214`, or the fractional cycle-packing certificate of `VIS-215`. It also says nothing about the quantitative access time of the one-parameter prime-log flow to near-extremal torus regions.

Falsify the finding by locating an error in the identity `W_1=O_v`, the same-cell pair count, the single-edge lower weight, the exact relation `2W_2=R_v`, the resulting `N_eff` scale, or the application of the `VIS-217` componentwise dimension floor.

## Research consequence

The immediate arithmetic question left by `VIS-217` is now answered in the strictly subcritical regime: the normalized magnetic ground-state relaxation is not merely difficult to sharpen; its own dimension floor forces its certificate to exceed the Haar RMS scale by a diverging factor.

Further work on this worst-start branch should therefore not spend effort trying to improve magnetic extreme-eigenvalue estimates within the same normalized relaxation in this regime. The remaining static possibilities are the stronger cycle-packing/frustration route of `VIS-215` or the exact fixed-modulus torus problem of `VIS-213`; the access-time problem remains separate. Testing either is a new coherent research question for a later invocation.