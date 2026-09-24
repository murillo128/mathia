# VIS-416 — Wang balance radius admits a coefficient-free Bernstein normalization

## Claim

Keep a finite labelled family of real Wang shell functions from `VIS-413`--`VIS-415`,

`F_i(T)=sum_(lambda in Lambda_i) B_(i,lambda) exp(-i lambda T)`.

For each nonconstant shell define its frequency radius and real-axis sup norm

`Omega_i = max_(lambda in Lambda_i) |lambda|`,

`M_i = sup_(T in R) |F_i(T)|`.

Because `F_i` is a finite exponential sum with frequencies in `[-Omega_i,Omega_i]`, it extends to an entire function of exponential type at most `Omega_i` and is bounded on the real axis. The classical Bernstein inequality for entire functions of exponential type therefore gives

`sup_(T in R) |F_i'(T)| <= Omega_i M_i`.

Fix `T_0` with `F_i(T_0) != 0` for every selected shell and define

`beta_i(T_0) = |F_i(T_0)|/(Omega_i M_i)`

when `Omega_i>0`, with `beta_i(T_0)=+infinity` for a nonzero constant shell. Put

`beta_*(T_0)=min_i beta_i(T_0)`.

Then every centered interval of radius `r<beta_*(T_0)` is simultaneously sign-definite for all selected shells. Hence every nonzero weighted Bargmann cycle built from a nonnegative window supported in that interval is positive by `VIS-414`.

Conversely, if a nonzero cycle on a centered interval window of radius `r` is negative, then for some participating shell

`|F_i(T_0)|/M_i <= r Omega_i`.

Thus the local Wang balance obstruction has a coefficient-free certificate depending only on the shell function's normalized pointwise amplitude and spectral bandwidth. In particular, the dimensionless quantity

`a_i(T)=|F_i(T)|/M_i in [0,1]`

is the amplitude factor in the certified radius `beta_i=a_i/Omega_i`.

Combining this with the coefficient `l^1` derivative budget from `VIS-415`,

`L_i=sum_(lambda in Lambda_i) |lambda B_(i,lambda)|`,

one has the improved explicit derivative bound

`sup |F_i'| <= D_i := min(L_i, Omega_i M_i)`

and therefore the larger certified radius

`rho_i^(cert)(T_0)=|F_i(T_0)|/D_i`.

**Evidence/status:** `LITERATURE+DERIVED + EXACT SPECIALIZATION + NEGATIVE REPRESENTATION/SCALING CONTROL + NO-NOVELTY-CLAIM`.

The classical Bernstein inequality is not new. The Mathia-specific consequence is that the Wang balance-radius program from `VIS-415` must separate a generic reciprocal-bandwidth scale from source-specific normalized amplitude behavior before interpreting radius collapse as arithmetic structure.

## 1. Wang shells lie in a Bernstein class

Each fixed shell is a finite exponential sum. For complex `z=x+iy`,

`F_i(z)=sum_(lambda in Lambda_i) B_(i,lambda) exp(-i lambda z)`

satisfies

`|F_i(z)| <= (sum |B_(i,lambda)|) exp(Omega_i |y|)`.

Hence `F_i` is entire of exponential type at most `Omega_i`. On the real axis it is a bounded continuous trigonometric/exponential polynomial, so `M_i<infinity`.

Bernstein's inequality for an entire function of exponential type `Omega_i` bounded on the real axis yields

`|F_i'(T)| <= Omega_i M_i`

for every real `T`.

This is different from the coefficient-triangle estimate in `VIS-415`. The latter sees the particular coefficient expansion through `L_i`; the Bernstein bound depends only on the realized shell function through its bandwidth and sup norm.

## 2. Bandwidth-normalized local balance radius

For `|T-T_0|<=r`, the derivative bound gives

`|F_i(T)-F_i(T_0)| <= Omega_i M_i r`.

If

`r < |F_i(T_0)|/(Omega_i M_i)=beta_i(T_0)`,

then the right-hand side is strictly smaller than `|F_i(T_0)|`, so `F_i` cannot vanish and keeps the sign of `F_i(T_0)` throughout the interval.

Taking the minimum over a finite shell family gives simultaneous sign-definiteness for `r<beta_*`. `VIS-414` then switches the finite-window Gram matrix to an entrywise nonnegative matrix, so every nonzero cycle product is positive.

If a negative cycle occurs on a centered interval of radius `r`, `VIS-414` forces a zero of some participating shell inside the interval. Applying the same derivative bound from `T_0` to that zero gives

`|F_i(T_0)| <= r Omega_i M_i`,

or equivalently `a_i(T_0)<=r Omega_i`.

Thus negative-cycle incidence requires at least one shell to be small relative to its own sup norm at the bandwidth-rescaled observation scale.

## 3. The sharpest of the two explicit certificates

`VIS-415` proves

`sup |F_i'| <= L_i`.

The Bernstein argument proves independently

`sup |F_i'| <= Omega_i M_i`.

Therefore

`sup |F_i'| <= min(L_i,Omega_i M_i)=D_i`.

The same mean-value argument gives the certificate

`rho_i^(cert)=|F_i(T_0)|/D_i`.

Since `D_i<=L_i` and `D_i<=Omega_i M_i`, this radius is at least as large as either certificate used separately. No comparison between `L_i` and `Omega_i M_i` is asserted in general; either can be the active bound depending on coefficient cancellation and shell geometry.

The exact derivative norm `||F_i'||_infinity` would give the strongest certificate of this form. The value of `D_i` is useful because both constituent bounds are explicit from already-defined shell data and do not require locating every derivative extremum.

## 4. Scaling consequence for the growing-family question

The research consequence of `VIS-415` asks how the lower envelope of local balance radii behaves as Wang shell families grow. The Bernstein form exposes a generic scale that must be removed from any arithmetic interpretation:

`beta_i(T)=a_i(T)/Omega_i`, where `a_i(T)=|F_i(T)|/M_i`.

Thus a decrease of a certified physical radius can come from two mathematically distinct mechanisms:

1. increasing shell bandwidth `Omega_i`, which shortens the fastest available variation scale even for a source-free band-limited function;
2. decreasing normalized amplitude `a_i(T)`, which places the observation height unusually close to a shell zero relative to the shell's own amplitude scale.

Only the second component is a plausible carrier of source-specific small-value geometry after bandwidth is matched. Consequently, a matched-control comparison for growing Wang families should preserve the shell bandwidths `Omega_i` and compare the distribution/lower envelope of `a_i(T)` or, equivalently, the bandwidth-rescaled certificates `Omega_i beta_i(T)`.

This is a **control requirement**, not evidence that the normalized amplitudes are arithmetic-specific. A random or surrogate exponential-sum ensemble with the same bandwidths may reproduce the same lower-envelope behavior.

## 5. Representation consequence

The coefficient budget in `VIS-415` is tied to one exponential-sum representation. The Bernstein certificate shows that the same local-balance logic survives after quotienting away coefficient bookkeeping: once the actual shell function and its frequency support are fixed, `M_i`, `Omega_i`, and `a_i(T)` are invariant under reordering or regrouping identical frequencies.

Amplitude rescaling `F_i -> c_i F_i` with `c_i != 0` leaves `a_i`, `beta_i`, and `rho_i^(cert)` unchanged because numerator and sup norm/derivative budgets scale together. Sign flips are included in this invariance.

A genuinely different packetization can still change the function, bandwidth, or both. The present result therefore removes coefficient-coordinate dependence inside a fixed shell representation; it does not make the Wang packetization itself canonical.

## 6. Prior art and novelty boundary

The derivative inequality used here is classical Bernstein theory. A standard statement is: if an entire function has exponential type `tau` and is bounded on the real axis, then

`sup_R |f'| <= tau sup_R |f|`.

Clément Frappier, **Inequalities for Entire Functions of Exponential Type**, *Canadian Mathematical Bulletin* 27:4 (1984), 463--471, DOI `10.4153/CMB-1984-073-4`, states this classical Bernstein inequality explicitly and studies refinements. The Encyclopedia of Mathematics entry **Bernstein inequality** records the corresponding derivative bound for trigonometric polynomials and its entire-function extension.

No novelty is claimed for Bernstein's inequality, exponential type of finite band-limited sums, sup-norm derivative bounds, or zero exclusion by the mean-value theorem. The only Mathia-specific content is their insertion into the Wang shell balance framework of `VIS-413`--`VIS-415` and the resulting bandwidth-normalization control for the proposed growing-family statistic.

## 7. Boundaries and falsification

The result still concerns a finite selected shell family at a fixed stage. It does not supply a positive lower bound uniform over an infinite growing family.

`M_i` is the global real-axis sup norm. Replacing it by a finite-window empirical maximum without proof would destroy the rigorous Bernstein certificate; a visual experiment may estimate `M_i`, but a canonical use of the bound must justify the replacement or keep it explicitly approximate.

The frequency radius must bound the actual Fourier support of the chosen shell function. If a packetization introduces additional frequencies, its `Omega_i` must change accordingly.

The theorem does not assert that raw `rho_i=|F_i|/L_i` and `beta_i=|F_i|/(Omega_i M_i)` are ordered. The combined denominator `D_i=min(L_i,Omega_i M_i)` is the justified improvement because both are independent upper bounds for the same derivative norm.

Falsify the specialization by exhibiting one canonical finite Wang shell for which the stated frequency support gives exponential type greater than `Omega_i`, or a real height at which `|F_i'(T)|>Omega_i M_i`. Either would contradict the classical Bernstein hypothesis/conclusion as applied here.

## Dependencies

- `VIS-413`: canonical Wang near-band shell functions are finite real exponential sums on the real axis.
- `VIS-414`: simultaneous shell sign-definiteness forces all nonzero finite-window cycle products positive.
- `VIS-415`: coefficient-based derivative budget and local balance radius.

## Research consequence

The next visual/control experiment should not compare raw balance radii across shell scales without normalization. A sharper test is to compare the lower envelope and empirical distribution of

`a_i(T)=|F_i(T)|/||F_i||_infinity`

for the arithmetic Wang shells against controls matched in `Omega_i`, shell count, and a pre-specified coarse energy statistic. The physical window scale can then be reconstructed through `a_i/Omega_i`. If the normalized-amplitude law is reproduced by the controls, the apparent balance-radius scaling is a generic band-limited small-value effect rather than an arithmetic signal.
