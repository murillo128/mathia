# MI-003 — Projective occupation-defect quality removes the spurious composition loss; source regularity still leaves submacroscopic descent

**Evidence level:** exact through [FD-094](../../findings/FD-094-normalized-schur-energy-records-upgrade-frontier-carriers-to-fixed-occupation.md), [FD-095](../../findings/FD-095-bounded-record-defect-turns-the-source-head-into-an-amplitude-scale-predecessor.md), [FD-096](../../findings/FD-096-source-record-doubling-slowdown-forces-sharp-occupied-bounded-defect-horizons.md), [FD-097](../../findings/FD-097-projective-occupation-defect-quality-reduces-growing-depth-loss-to-exponential.md), and the uniform-short-interval refinement [FD-098](../../findings/FD-098-uniform-short-interval-cancellation-thickens-source-head-descent-by-a-logarithmic-corridor.md). A false-RH contradiction still requires an effective physical scale theorem and transport-error control.

For fixed `1/2<sigma<Theta`, write

`F_sigma(H)=E_(H,1)/H^(2 sigma)`, `R_sigma(H)=P_sigma(H)/F_sigma(H)`,

and suppose a state has occupation `U_(H,1)/E_(H,1)>=eta` and defect `R_sigma(H)<=K`. The useful certificate is not the pair `(eta,K)` separately but its projective quality

`q=eta/K = U_(H,1)/(H^(2 sigma) P_sigma(H))`.

At every repairable predecessor step the occupation lower bound and inherited defect upper bound are multiplied by the **same** unknown destination factor `x=F_sigma(H)/F_sigma(C)`. If the branch coefficient is `a>0`, then

`eta_C >= a eta x`, `K_C <= K x`, hence `q_C >= a q`.

The destination scale cancels exactly. Bounding `eta_C` and `K_C` independently had allowed mutually incompatible worst cases and made the iteration look quadratic/superexponential. FD-097 shows that all current predecessor branches have fixed positive projective coefficients, so along an `m`-step chain

`q_m >= q_0 b_sigma^m`

for a fixed `b_sigma>0`. Combined with the sharp bounded-defect entry states of FD-096, a diagonal choice of farther and farther source records yields chains of depth tending to infinity while these losses remain subpower at every visited scale.

FD-098 then tests the remaining all-head obstruction with the strongest currently anchored **uniform** local Möbius regularity. When the false-RH frontier exponent satisfies `11/20<Theta<1`, a source record of amplitude `A=X^(Theta+o(1))` is protected backwards not merely for distance `O(A)` but for

`L_X asymp A (log X)^kappa`, for every fixed `kappa<1/3`.

Every four-adic reembedding across this corridor remains frontier-sharp, has fixed nonsquarefree occupation and bounded normalized-energy record defect. Thus the worst head repair gains a genuine logarithmic factor without paying a new projective penalty. But `L_X/X -> 0`: even this strengthened arithmetic regularity certifies only submacroscopic additive descent. A matched triangular control shows that the endpoint regularity estimate itself cannot force a longer scale.

So two previously plausible obstructions are now separated and largely closed. **Composition constants are not the problem**, because projective quality keeps the common destination factor. **Known uniform endpoint smoothing is not the missing scale theorem**, because it only thickens the protected head corridor logarithmically. The residual must couple physical descent to branch type, prove source refueling before the additive corridor is exhausted, or exploit the exact signed/divisibility coefficient law beyond an aggregate short-interval norm bound.

The threshold is real. For `1/2<Theta<=11/20`, FD-098 cannot improve the one-Lipschitz `O(A)` corridor with the current all-interval theorem. For `11/20<Theta<1`, the logarithmically thickened corridor is still `o(X)`. Neither regime supplies a fixed-factor contraction by itself.

**Boundary.** Projective quality and the short-interval corridor do not prove infinite descent or contradict false RH. They identify the scale ledger that remains after artificial composition loss and currently available source regularity have both been priced sharply. Any final argument must still control accumulated asymptotic errors along the physically descending chain.
