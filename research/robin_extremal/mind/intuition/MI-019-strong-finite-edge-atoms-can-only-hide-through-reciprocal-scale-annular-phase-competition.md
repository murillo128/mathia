# MI-019 — Strong finite-edge atoms can only hide through a logarithmically comparable cancelling-phase companion

**Evidence level:** exact consequence of [RE-125](../../findings/RE-125-invisible-algebraic-subedge-atoms-require-a-reciprocal-scale-ordinate-annulus.md)--[RE-127](../../findings/RE-127-hiding-a-strong-subedge-atom-forces-a-logarithmically-comparable-cancelling-phase-companion.md), building on the full-packet phase transfer of RE-123 and matched-filter localization of RE-124. No theorem excludes the required zeta-zero pairs, controls the diffuse branch, the nonattained edge or `Theta=1`.

RE-124 shows that an algebraically strong subedge atom can remain invisible only if comparable coefficient mass is spectrally localized within `U^(-1+eta)` of its ordinate. RE-125 identifies a source-specific lower edge for that cancellation window. The leading Robin/CA coefficients for positive-ordinate finite-edge zeros lie in a fixed angular sector strictly inside the right half-plane, and fixed-order corrections preserve it. After demodulation at `gamma_0`, every neighbor with

`|gamma-gamma_0|<=c_*/U`

has uniformly positive real projection. Exact multiplicity and tighter micro-clusters reinforce the target; they cannot cancel it.

RE-126 adds the local zero-count budget. If a target of size at least `U^-A` remains hidden, the annular mass cannot be spread over arbitrarily many tiny modes. At least one distinct-ordinate companion satisfies

`|a_(rho_1,K)(U)| >= c |a_(rho_0,K)(U)|/log U`,

lies in the same `O(log U/U)` horizontal edge layer at polynomial height, and obeys

`c_*/U < |gamma_1-gamma_0| <= U^(-1+eta)`.

Along an unbounded hidden-target sequence this gives `|gamma_1-gamma_0| log(2+gamma_0)->0`.

RE-127 preserves the sign discarded in the absolute-mass pigeonhole. The matched Fourier cutoff has real nonnegative frequency weights. The target and all sub-reciprocal neighbors contribute positive real projection after demodulation, while hiding the target forces the filtered total to be small. Therefore the annulus must supply **negative projected mass**, and the same `O(log U)` local zero count yields a companion with

`-Re(a_(rho_1,K)(U)e^(i(gamma_1-gamma_0)U)) >= c_1 |a_(rho_0,K)(U)|/log U`.

So the strong-atom escape is not merely close-pair geometry. At least one logarithmically comparable companion must already lie in the opposite half-plane in the target-demodulated coordinate.

Writing `vartheta_1(U)=arg a_(rho_1,K)(U)`, the source coefficient sector gives

`-C_K/U <= vartheta_1(U) <= omega_*+C_K/U`, `omega_*<pi/2`.

Hence the scaled signed gap is constrained to a fixed cancellation arc:

`(gamma_1-gamma_0)U in [pi/2-omega_*-o(1), 3pi/2+o(1)] mod 2pi`.

The arc is intentionally broad. The theorem forces one negative real projection, not an almost-antipodal two-mode pair; if the companion amplitude is much larger than its guaranteed lower bound, its cosine may approach zero. Nor does the theorem claim that this one companion cancels the target over the full observation window.

The live strong-atom problem is therefore now two-dimensional but explicit: an attained off-critical edge must support infinitely many algebraically strong near-edge pairs with both vanishing normalized ordinate separation and the required target-demodulated cancellation sector. A useful exclusion theorem can attack either geometry or phase, but it must apply to potentially nonconsecutive off-line zeros in the exact horizontal layer forced here. The other escape is genuinely different: a diffuse packet with no algebraically strong atom.

**Boundary.** RE-127 gives a necessary companion and sign projection, not a sufficient cancellation mechanism and not a zeta zero-gap theorem. It does not force a fixed angular margin inside the left half-plane, prove pair consecutiveness, or control the diffuse branch. The durable refinement is that strong-atom hiding requires a concrete phase-carrying companion, not an unspecified annular cloud.