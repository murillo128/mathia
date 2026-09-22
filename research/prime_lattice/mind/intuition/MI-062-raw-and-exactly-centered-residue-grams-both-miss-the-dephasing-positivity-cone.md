# MI-062 — Raw and exactly centered residue Grams both miss the dephasing positivity cone

**Evidence level:** literature-backed and exact source-side synthesis from [PL-418](../../findings/PL-418-j-nonnegative-lift-is-arithmetic-blind-before-subtraction.md), [PL-421](../../findings/PL-421-local-factor-dephasing-image-cone.md), [PL-422](../../findings/PL-422-raw-residue-gram-collapses-below-dephasing-floor.md), and [PL-423](../../findings/PL-423-exact-principal-channel-centering-breaks-dephasing-floor.md), closing two direct covariance repairs left by MI-061.

PL-421 turns exact positive deletion of the local `p=5` factor into a sharp image-cone condition: after normalizing the four reduced-residue covariance vectors, their correlation matrix `C` must satisfy

`lambda_min(C) >= 1/4`.

The canonical uncentered source Gram fails this asymptotically. PL-422 uses short-AP equidistribution to show, for every fixed polynomial window `h=X^theta` with `1/6<theta<=1/2`, that

`P_a(y;h)=h/4+o_(L^2)(h sqrt(X))`

uniformly over the four reduced residues. The common deterministic mean dominates, the normalized residue vectors become parallel, and therefore `C_X -> 11*` with `lambda_min(C_X)->0`. Retaining the full raw covariance is thus not enough: its common rank-one mode puts it outside the positive dephasing image cone.

PL-423 then closes the most literal repair. Exact data-dependent common-mode centering `q_a=x_a-(1/(p-1))sum_b x_b` forces `sum_a q_a=0`, so the centered Gram has an exact principal-direction zero mode. But every nonzero covariance in the positive image of the local dephasing map must satisfy a strictly positive normalized floor `1/(p-1)`. Hence every nontrivial exactly common-mode-centered residue Gram is also outside that image cone; at `p=5` its smallest normalized eigenvalue is exactly `0`, not merely asymptotically below `1/4`.

The source-transfer fork is therefore narrower than “center the raw matrix.” Raw covariance fails because the principal mode is too large, while exact principal-channel deletion fails because it removes that mode completely and creates a forbidden linear dependence. The remaining direct possibility is **deterministic model subtraction**, for example `P_a-h/(p-1)`, which removes the leading mean without forcing the principal fluctuation channel to vanish identically. Its residual covariance must then satisfy the dephasing image criterion non-circularly and still survive the separate source/model subtraction order gate of PL-418. Otherwise the route needs a genuinely different divisor-faithful positive representation.

This clarifies what matrix information is actually required. Full coherence must be retained, but neither an overwhelmingly common mode nor an exact projection away from the principal channel is compatible with positive local-factor deletion. A viable covariance must preserve enough principal fluctuation to avoid singularity while simultaneously maintaining the quantitative lower-Riesz floor after the declared model subtraction.

**Boundary.** PL-422 concerns the canonical uncentered covariance in the stated short-window range; PL-423 is an exact finite-dimensional obstruction to data-dependent common-mode centering. Neither determines the covariance after deterministic Hardy--Littlewood/PNT main-term subtraction, zero-side matrices, sub-threshold windows, or alternative positive lifts. These findings close two concrete representations, not the signed mod-5 supertrace problem or RH.