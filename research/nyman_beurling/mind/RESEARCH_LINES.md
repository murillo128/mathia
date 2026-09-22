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

where `z_(m,n,Z)` is the sample-null component of the same quotient band. Thus the previously scalar retention loss now has a canonical decomposition into a first-free visible repair charge and a first-free sample-null charge, tied by the actual dilation geometry.

The decisive moving-packet question is no longer whether such a vector-valued carrier exists, but whether it is **coercive in the target-relevant direction**. NB-292 gives no lower bound forcing either charge to be large and does not yet control the target-aware future-null Parseval tail of NB-287. A useful next theorem must connect the matrix cocycle `Gamma_(m,n,Z)`, the defect vectors `d_(m,n,Z)` or the null-band components `z_(m,n,Z)` to the moving minimum-norm source/target coefficients strongly enough to force a rate. Another inequality depending only on `sigma_n`, `sqrt(n)sigma_n`, `c_(m,n)` or the raw zero-sample table remains inside the NB-291 matched-control class.