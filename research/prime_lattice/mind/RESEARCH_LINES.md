# Prime-lattice research lines

This file records the current mathematical questions that survive the Prime-Lattice evidence. It is not a roadmap, task queue, status page, or history.

## Control the source-adapted mod-5 Schur ellipse through its reflection-anisotropy and quadratic-lag channels

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

All four sign vectors have coordinate squares equal to one, so the full diagonal self-energy cancels identically inside each difference, even when the four residue variances are unequal. Thus the unresolved vector can be written directly as

`g=(1/(8 sqrt(2)))(Delta_s-Delta_f, Delta_s+Delta_f)^T`.

PL-440 then identifies the source symmetry carried by these two differences. After extending the four probes by zero at residue `0 mod 5`, the pair defining `Delta_s` has identical circular lag autocorrelation, while the pair defining `Delta_f` differs by exactly `4 chi_5(h)`. Therefore every residue-translation-stationary lag kernel contributes **zero** to `Delta_s`, whereas its contribution to `Delta_f` is exactly one quadratic-character lag projection. In source terms, `s` is a reflection/start-residue anisotropy channel, while `f` contains a single `chi_5` lag channel plus any nonstationary anisotropic remainder. This split is exact but does not assert that the actual moving prime covariance is stationary or that either surviving term is small.

The live arithmetic question is therefore narrower than controlling a generic complex covariance or even two arbitrary signed energies. Decompose the canonical centered fixed-mod-5 prime pair covariance into its translation-stationary lag component and its start-residue/boundary anisotropic remainder, then prove variance-scale control strong enough to place the resulting `g` inside the PL-438 Schur ellipse. The `s` coordinate asks specifically for control of reflection/start-residue anisotropy; the stationary part of `f` asks for one explicit quadratic-character lag twist, with the anisotropic remainder charged separately. In an asymmetric regime the target is still the full source-adapted metric `(g-mu)^T E^(-1)(g-mu)`, not separate smallness of `s` and `f`.

The adversarial boundary is load-bearing. Translation stationarity is a decomposition of the source covariance, not a theorem about the whole source; centering and interval endpoints can create precisely the anisotropy measured by `Delta_s`; and identifying a nonprincipal character projection does not by itself supply a variance-scale saving. Existing first-moment or almost-all progression technology cannot be substituted for the required second-order fixed-source estimate.

## Keep representation completeness, exact cone geometry and arithmetic theorem strength distinct

The representation problem is now sharply separated from the number-theoretic one. PL-429--PL-432 show how the oriented sector can be observed through character-side vertical modulation; PL-437 compresses it to two coordinates; PL-438 identifies the exact strict-branch feasible ellipse; PL-439 realizes those coordinates as real signed-residue energy differences; and PL-440 resolves their symmetry types into reflection anisotropy and a quadratic lag character. None of these results supplies the required arithmetic estimate.

Any proposed completion should therefore state the exact branch hypotheses (`gamma>0`, `E` positive definite where the inverse ellipse is used), the centering convention, the stationary/anisotropic covariance decomposition, how its two surviving modes place `g` relative to `(mu,E,alpha)`, and the unconditional input. A scalar theorem that sees only unshifted real products in the character basis is information-theoretically incomplete; a full complex-matrix theorem is stronger than representation requires; a Weyl-norm theorem is only a sufficient fallback; and a generic stationarity heuristic erases the exact boundary/start-residue channel that PL-440 isolates.
