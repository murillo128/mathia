# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. Target pairings change the projection defect and anchor mismatch but do not secretly strengthen the source-source Gram. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Price first-free boundary data through vector-valued metric arithmetic coupling

NB-276--NB-283 move the source-native divisor route away from universal zero sampling. The Ford current is a singular Mellin derivative of the canonical Möbius Nyman source, but finite differentiated sources are entire and cannot carry the interior divisor current across a zero. Moving the pole into a legal dual functional reduces all source-independent point and multiplicity-jet data to the finite Burnol/Blaschke defect. The first source-dependent jet can be interpolated with sparse finite support, so support rank alone is not an obstruction.

NB-284--NB-287 isolate the genuine finite-section penalty. For a fixed zero packet the first-free synthesis cost converges to the full-space cost; any persistent obstruction must be a **moving-packet** phenomenon. After the first surjective section, each genuinely new source direction has a canonical neutralized innovation in the exact sampling nullspace, and the finite-section excess is exactly the Parseval tail of the current minimum-norm interpolant on the future sample-null innovations.

NB-288 closes generic Hilbert conditioning as the source of a rate: arbitrary decreasing excess profiles coexist with uniformly positive, almost perfectly conditioned sampling Grams, bounded optimal right inverses and sample-visible enrichments. NB-289 closes the stronger sample-algebra shortcut. By a unit-triangular change of generators one can impose the exact future Dirichlet zero-sample vectors `n^(-rho_j)-n^(-1)` and their exact multiplicative semigroup identities while leaving every section, projector, sampling Gram, null innovation and prescribed lethargy profile unchanged.

NB-290 supplies a genuine canonical source-metric identity that those controls do not automatically contain. The Nyman dilation isometry satisfies

`P_(V_(mn-1)^perp) A_m w_n = sqrt(m) w_(mn)`,

so the raw Gram--Schmidt pivots obey `sigma_(mn)<=sigma_n/sqrt(m)` and `sqrt(n) sigma_n` is monotone down divisibility chains. NB-291 then shows that **all scalar consequences of that pivot profile are still insufficient**: an old-section triangular graft can match the exact Dirichlet sample table and prescribe the canonical pivot `sigma_n` at every future index while preserving the same sections, sampling Grams, normalized null innovations and arbitrary finite-section lethargy. It therefore also matches the scalar divisibility contraction, retention coefficients, cocycle and one-step determinant ratios.

NB-292 identifies the first exact vector/matrix structure that this scalar graft does not encode. For a finite zero packet `Z`, let `V_(r,Z)` be the Blaschke-deflated quotient sections, `L_Z` the first-free sampling map and `D_Z(m)` the diagonal action of the canonical dilation. The orthogonal multiplicative band

`W_(m,n,Z)=V_(mn-1,Z) \ominus S_m V_(n-1,Z)`

has positive sampling Gram

`Gamma_(m,n,Z)=K_(mn-1,Z)-D_Z(m)K_(n-1,Z)D_Z(m)^* >= 0`,

and these Grams obey the exact cocycle

`Gamma_(km,n,Z)=Gamma_(k,mn,Z)+D_Z(k)Gamma_(m,n,Z)D_Z(k)^*`.

For the normalized innovation, the old-section defect `b_(m,n,Z)=S_m psi_(n,Z)-c_(m,n)psi_(mn,Z)` lies in this band, with sample defect `d_(m,n,Z)=D_Z(m)v_(n,Z)-c_(m,n)v_(mn,Z)`, and the scalar dilation loss splits exactly as

`1-c_(m,n)^2 = d_(m,n,Z)^* Gamma_(m,n,Z)^+ d_(m,n,Z) + ||z_(m,n,Z)||^2`,

where `z_(m,n,Z)` is the sample-null component of the same quotient band. Thus the previously scalar retention loss has a canonical visible/null decomposition tied by the actual dilation geometry.

NB-293 now gives the exact destination map for that carrier once the lower quotient section is first-free-surjective. Neutralizing each `w` in `W_(m,n,Z)` by its minimum-norm old-section sample repair produces a bijection onto the new null block

`Q_(m,n,Z)=D_(mn-1,Z) \ominus S_m D_(n-1,Z)`.

For first-free datum `y`, if `g_(m,n)(y)` is its minimum-norm realization in the dilated old section, the entire multiplicative-section improvement is

`Delta_(m,n,Z)(y)=||P_(Q_(m,n,Z)) g_(m,n)(y)||^2`.

Equivalently, with `A=D_Z(m)K_(n-1,Z)D_Z(m)^*`, `M=A^(-1/2) Gamma_(m,n,Z) A^(-1/2)` and `x=A^(-1/2)y`,

`Delta_(m,n,Z)(y)=x^* M(I+M)^(-1)x`.

Thus trace, determinant, operator norm, band dimension and scalar dilation loss count only through spectral occupation by the **actual transformed datum**. The canonical defect gives the explicit certificate

`Delta_(m,n,Z)(y) >= |d_(m,n,Z)^* A^(-1)y|^2 / (1-c_(m,n)^2+d_(m,n,Z)^*A^(-1)d_(m,n,Z))`,

while an already sample-null component of the band is target-silent for this direct enrichment. Multiplicative gains also obey an exact chain rule only after transporting the datum contravariantly: a fixed-datum telescoping argument is invalid.

The decisive moving-packet question is therefore no longer whether a vector carrier exists or how it reaches the target. Both are exact. The missing theorem is **arithmetic target occupation**: force enough mass of the moving transformed Ford datum into the positive spectrum of the whitened cocycle, or lower-bound a canonical pairing such as `d^*A^(-1)y`, strongly enough to control the target-aware future-null tail. NB-293 itself supplies no such lower bound and no approximation rate. Another inequality depending only on `sigma_n`, `sqrt(n)sigma_n`, `c_(m,n)`, raw matrix size or the zero-sample table remains outside the needed target-aware currency.