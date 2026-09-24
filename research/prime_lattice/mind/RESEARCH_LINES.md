# Prime-lattice research lines

This file records the current mathematical questions that survive the Prime-Lattice evidence. It is not a roadmap, task queue, status page, or history.

## Control the source-adapted mod-5 Schur ellipse through the two signed residue-energy differences

PL-407--PL-428 reduce the local-factor gate to a finite covariance problem. At `p=5`, image admission is equivalent to the normalized residue correlation matrix satisfying the `1/4` Loewner threshold. Real same-shift character variances determine only `Re K`; imaginary coherences can change the cone verdict, so ordinary real scalar products in the character basis do not determine admission.

PL-429--PL-433 show that the missing orientation is representable without artificial complex source coefficients. Vertical modulation recovers complex coherence from real scalar responses; for the dyadic prime source a single quarter-turn shift `t_X=-pi/(2 log X)` together with `t=0` suffices, and Abel--Stieltjes transport controls the deformation using multiscale `L^2` norms. The vanishing physical shift is nevertheless a fixed microscopic displacement on the zero scale, so unshifted zero-side continuity is not enough when one works through the character/vertical-shift representation.

PL-434 identifies the unconditional theorem-strength gap: the directly matched MRSTT short-interval theorem already handles the quarter-turn twist and fixed mod-5 progression channels, but at density/first-moment scale rather than the covariance scale required to preserve the cone margin. Stronger logarithmic savings in the same norm do not close the polynomial transfer loss on polynomial short intervals.

PL-437 reduces the unresolved oriented sector to two coordinates. Reality and the residue diagonal determine the other imaginary combination, leaving

` s = Im(K_01+K_21) ` and ` f = Im K_13 `.

The residual Hermitian perturbation has operator norm `sqrt(s^2+f^2)`, giving a simple Weyl sufficient condition. PL-438 shows that this Euclidean disk is not the exact source-adapted gate. In an explicit residue-space `1+2+1` normal form, write the visible blocks as `gamma`, `A`, `b`, `a`, `w`; on the strict branch `gamma>0`, set

`E=A-bb^T/gamma`, `mu=(w/gamma)b`, `alpha=a-w^2/gamma`.

For `E` positive definite, the exact remaining cone condition is the ellipse

`(g-mu)^T E^(-1)(g-mu) <= alpha`,

with `g=2^(-1/2)(s-f,s+f)^T`. Its center, axes and radius budget are fixed by visible real-product data plus the residue diagonal. PL-438 gives an admissible positive covariance for which this ellipse certifies the cone while the PL-437 Weyl disk fails, so the strengthening is genuine. It does **not** prove that the actual prime covariance lies in the ellipse.

PL-439 sharpens the source side of this reduction. For the centered real residue signal `R=(R_0,R_1,R_2,R_3)` in the established order `(1,2,4,3)`, let `J(w)=int (w^T R)^2 dmu`. Then the entire oriented sector is recovered from two paired differences of four fixed real sign probes:

`Delta_s = J(1,-1,1,1)-J(1,1,1,-1) = 8s`,

`Delta_f = J(1,1,-1,-1)-J(1,-1,-1,1) = 8f`.

All four sign vectors have coordinate squares equal to one, so the full diagonal self-energy `D_0+D_1+D_2+D_3` cancels identically inside each difference, even when the four residue variances are unequal. Thus the unresolved vector can be written directly as

`g=(1/(8 sqrt(2)))(Delta_s-Delta_f, Delta_s+Delta_f)^T`.

This settles a representation question more strongly than the quarter-turn route on the real residue-source side: the two load-bearing oriented coordinates are ordinary real signed-residue Selberg-energy differences, and quarter-turn tomography is not intrinsically required to define or observe them there. It remains useful on the character/zero side, where the same orientation appears as complex coherence. PL-439 is not an arithmetic estimate; large individual positive energies may cancel delicately, and estimating them separately can be badly conditioned.

The live arithmetic question is therefore **whether the actual fixed-mod-5 prime source satisfies the PL-438 Schur budget through the signed variance-difference vector `(Delta_s,Delta_f)` at the required variance scale, by an unconditional estimate genuinely weaker than full complex lower-frame control**. In an asymmetric regime the target is not necessarily separate smallness of `Delta_s` and `Delta_f`: the correct theorem may need to show that the resulting `g` tracks the visible center `mu` in the anisotropic `E^(-1)` metric. The source-subtracted centering is load-bearing, because two of the sign probes have nonzero reduced-residue mean before centering. A theorem for individual residue variances, total trace or first-order progression sums still misses this target.

## Keep representation completeness, exact cone geometry and arithmetic theorem strength distinct

The representation problem is now sharply separated from the number-theoretic one. PL-429--PL-432 show how the oriented sector can be observed through character-side vertical modulation; PL-437 compresses it to two coordinates; PL-438 identifies the exact strict-branch feasible ellipse; and PL-439 shows that on the real residue source those same two coordinates are exactly two paired signed-energy differences with complete diagonal cancellation. None of these results supplies the required arithmetic estimate. Conversely, PL-434--PL-436 show that unconditional theorems may already match the twist, residue channels or scalar variance technology yet remain too weak in norm or orientation to control the destination at covariance scale.

Any proposed completion should therefore state the exact branch hypotheses (`gamma>0`, `E` positive definite where the inverse ellipse is used), the centering convention, how the two signed differences place `g` relative to `(mu,E,alpha)`, and the unconditional input. A scalar theorem that sees only unshifted real products in the character basis is information-theoretically incomplete; a full complex-matrix theorem is stronger than representation requires; and a Weyl-norm theorem should be treated as a sufficient fallback rather than the exact source-adapted cone condition. The new minimal arithmetic target is the fixed-mod-5 signed Selberg-variance difference itself, not the machinery used to expose it in a particular basis.
