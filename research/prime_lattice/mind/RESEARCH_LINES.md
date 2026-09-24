# Prime-lattice research lines

This file records the current mathematical questions that survive the Prime-Lattice evidence. It is not a roadmap, task queue, status page, or history.

## Control the source-adapted mod-5 Schur ellipse at variance scale

PL-407--PL-428 reduce the local-factor gate to a finite covariance problem. At `p=5`, image admission is equivalent to the normalized residue correlation matrix satisfying the `1/4` Loewner threshold. Real same-shift character variances determine only `Re K`; imaginary coherences can change the cone verdict, so ordinary real scalar products do not determine admission.

PL-429--PL-433 show that the missing orientation is representable without artificial complex coefficients. Vertical modulation recovers complex coherence from real scalar responses; for the dyadic prime source a single quarter-turn shift `t_X=-pi/(2 log X)` together with `t=0` suffices, and Abel--Stieltjes transport controls the deformation using multiscale `L^2` norms. The vanishing physical shift is nevertheless a fixed microscopic displacement on the zero scale, so unshifted zero-side continuity is not enough.

PL-434 identifies the unconditional theorem-strength gap: the directly matched MRSTT short-interval theorem already handles the quarter-turn twist and fixed mod-5 progression channels, but at density/first-moment scale rather than the covariance scale required to preserve the cone margin. Stronger logarithmic savings in the same norm do not close the polynomial transfer loss on polynomial short intervals.

PL-437 reduces the unresolved oriented sector to two coordinates. Reality and the residue diagonal determine the other imaginary combination, leaving

` s = Im(K_01+K_21) ` and ` f = Im K_13 `.

The residual Hermitian perturbation has operator norm `sqrt(s^2+f^2)`, giving a simple Weyl sufficient condition. PL-438 shows that this Euclidean disk is not the exact source-adapted gate. In an explicit residue-space `1+2+1` normal form, write the visible blocks as `gamma`, `A`, `b`, `a`, `w`; on the strict branch `gamma>0`, set

`E=A-bb^T/gamma`, `mu=(w/gamma)b`, `alpha=a-w^2/gamma`.

For `E` positive definite, the exact remaining cone condition is the ellipse

`(g-mu)^T E^(-1)(g-mu) <= alpha`,

with `g=2^(-1/2)(s-f,s+f)^T`. Its center, axes and radius budget are fixed by visible real-product data plus the residue diagonal. PL-438 gives an admissible positive covariance for which this ellipse certifies the cone while the PL-437 Weyl disk fails, so the strengthening is genuine. It does **not** prove that the actual prime covariance lies in the ellipse.

The live arithmetic question is therefore **whether the actual fixed-mod-5 prime source satisfies this scalar Schur budget at variance scale by an unconditional estimate genuinely weaker than full complex lower-frame control**. Bounding `sqrt(s^2+f^2)` remains sufficient but is no longer the canonical target. A useful theorem may exploit anisotropic visible margins and the nonzero center `mu`; it must still control the two oriented combinations at the quarter-turn geometry with the source-subtracted covariance normalization and without RH/GRH hidden in the hypotheses.

## Keep representation completeness, exact cone geometry and arithmetic theorem strength distinct

The representation problem is now sharply separated from the number-theoretic one. PL-429--PL-432 show how to observe the oriented sector and control the quarter-turn deformation; PL-437 compresses it to two coordinates; PL-438 then identifies the exact strict-branch feasible ellipse and proves that the earlier Euclidean margin can be unnecessarily strong. None of these results supplies the required arithmetic estimate. Conversely, PL-434 shows that an unconditional theorem may already match the twist and residue channels yet remain too weak in norm to control the destination at covariance scale.

Any proposed completion should therefore state the exact branch hypotheses (`gamma>0`, `E` positive definite where the inverse ellipse is used), which combination of `(s,f)` it controls relative to `(mu,E,alpha)`, the source/model normalization, and the unconditional input. A scalar theorem that still sees only unshifted real-product data is information-theoretically incomplete; a full-matrix theorem is stronger than necessary; and a Weyl-norm theorem should be treated as a sufficient fallback rather than the exact source-adapted cone condition.
