# Prime-lattice research lines

This file records the current mathematical questions that survive the Prime-Lattice evidence. It is not a roadmap, task queue, status page, or history.

## Control the two genuinely oriented mod-5 covariance coordinates at variance scale

PL-407--PL-428 reduce the local-factor gate to a finite covariance problem. At `p=5`, image admission is equivalent to the normalized residue correlation matrix satisfying the `1/4` Loewner threshold. Real same-shift character variances determine only `Re K`; three imaginary coherences can change the cone verdict, so ordinary real scalar products do not determine admission.

PL-429--PL-433 show that the missing orientation is representable without artificial complex coefficients. Vertical modulation recovers complex coherence from real scalar responses; for the dyadic prime source a single quarter-turn shift `t_X=-pi/(2 log X)` together with `t=0` suffices, and Abel--Stieltjes transport controls the deformation using multiscale `L^2` norms. The vanishing physical shift is nevertheless a fixed microscopic displacement on the zero scale, so unshifted zero-side continuity is not enough.

PL-434 identifies the unconditional theorem-strength gap: the directly matched MRSTT short-interval theorem already handles the quarter-turn twist and fixed mod-5 progression channels, but at density/first-moment scale rather than the covariance scale required to preserve the cone margin. Stronger logarithmic savings in the same norm do not close the polynomial transfer loss on polynomial short intervals.

PL-437 now reduces the finite-dimensional target itself. Reality forces the imaginary covariance perturbation to have rank at most two. Once `A=Re K` and the residue diagonal already required by the cone test are known, the combination `r=d-b` is algebraically determined, leaving only

` s = Im(K_01+K_21) ` and ` f = Im K_13 `

as genuinely unresolved oriented coordinates. The remaining Hermitian perturbation has operator norm `sqrt(s^2+f^2)`. Thus a theorem for the entire complex `4 x 4` covariance matrix is stronger than necessary: a visible real-sector margin plus sufficiently strong control of these two oriented coordinates is enough to certify the cone by the PL-437 perturbation bound.

The live arithmetic question is therefore **whether the actual prime source admits a noncircular variance-scale estimate for `(s,f)` at the required quarter-turn geometry, strong enough relative to the visible spectral margin**. Direct prime-side control is preferable; an equivalent shifted scalar theorem is also sufficient if its hypotheses do not contain RH/GRH and its normalization reaches the source-subtracted covariance. Rank two is not smallness: PL-428 still supplies positive-semidefinite matched controls in the fixed-visible-data fibre for which the cone verdict changes.

## Keep representation completeness, conditioning and arithmetic theorem strength distinct

The representation problem is now sharply separated from the number-theoretic one. PL-429--PL-432 show how to observe the oriented sector and control the quarter-turn deformation; PL-437 compresses that sector to two coordinates after using the gate's own residue diagonal. Neither result supplies the required arithmetic estimate. Conversely, PL-434 shows that an unconditional theorem may already match the twist and residue channels yet remain too weak in norm to control those coordinates at covariance scale.

Any proposed completion should therefore state which of `s` and `f` it controls, the visible margin against which `sqrt(s^2+f^2)` is compared, the source/model normalization, and the exact unconditional hypotheses. A scalar theorem that still sees only real-product data is information-theoretically incomplete; a full-matrix theorem is unnecessary if the two-coordinate defect is controlled directly.
