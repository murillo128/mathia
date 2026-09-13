# MI-003 — Projective occupation-defect quality removes the spurious superexponential composition loss

**Evidence level:** exact through [FD-094](../../findings/FD-094-normalized-schur-energy-records-upgrade-frontier-carriers-to-fixed-occupation.md), [FD-095](../../findings/FD-095-bounded-record-defect-turns-the-source-head-into-an-amplitude-scale-predecessor.md), [FD-096](../../findings/FD-096-source-record-doubling-slowdown-forces-sharp-occupied-bounded-defect-horizons.md), and [FD-097](../../findings/FD-097-projective-occupation-defect-quality-reduces-growing-depth-loss-to-exponential.md). A false-RH contradiction still requires an effective relation between descent depth and physical scale plus control of accumulated transport errors.

For fixed `1/2<sigma<Theta`, write

`F_sigma(H)=E_(H,1)/H^(2 sigma)`, `R_sigma(H)=P_sigma(H)/F_sigma(H)`,

and suppose a state has occupation `U_(H,1)/E_(H,1)>=eta` and defect `R_sigma(H)<=K`. The useful certificate is not the pair `(eta,K)` separately but its projective quality

`q=eta/K = U_(H,1)/(H^(2 sigma) P_sigma(H))`.

At every repairable predecessor step the occupation lower bound and inherited defect upper bound are multiplied by the **same** unknown destination factor `x=F_sigma(H)/F_sigma(C)`. If the branch coefficient is `a>0`, then

`eta_C >= a eta x`, `K_C <= K x`, hence `q_C >= a q`.

The destination scale cancels exactly. Bounding `eta_C` and `K_C` independently had allowed mutually incompatible worst cases and made the iteration look quadratic/superexponential. FD-097 shows that all current predecessor branches have fixed positive projective coefficients, so along an `m`-step chain

`q_m >= q_0 b_sigma^m`

for a fixed `b_sigma>0`. Occupation need decay and defect grow only exponentially in depth. Combined with the sharp bounded-defect entry states of FD-096, a diagonal choice of farther and farther source records yields chains of depth tending to infinity while these losses remain subpower at every visited scale.

This closes **constant blow-up as the main multistep obstruction**. What remains is physical descent versus depth. The current theorem is existential and gives no effective lower bound on achievable depth in terms of the starting horizon; an all-head scalar control can satisfy the projective inequalities while guaranteeing only `O(H^Theta)` additive progress from scale `H`. Transport error terms must also remain negligible along whatever growing-depth chain is ultimately used.

**Boundary.** The projective certificate does not prove infinite descent or contradict false RH. It says the correct multistep currency keeps the common scale correlation instead of paying occupation and defect losses independently. The next theorem must quantify how many genuinely lower physical scales are reached before the exponentially degrading projective budget becomes ineffective.