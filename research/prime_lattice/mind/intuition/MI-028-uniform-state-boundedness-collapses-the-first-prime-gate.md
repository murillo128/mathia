# MI-028 — Uniform state boundedness turns every finite prime-power birth into a trace gate

**Evidence level:** exact synthesis from [PL-329](../../findings/PL-329-source-amplitude-gate-for-first-prime-reflection.md) through [PL-338](../../findings/PL-338-all-prime-activation-flatness.md). Uniform state boundedness is proved on compact aperture/eigenvalue ranges; later global branch ordering remains open.

The first-prime problem originally separated source amplitude, endpoint remainder and the critical half-log coefficient. PL-337 collapses those quantities through one state-space fact: normalized eigenstates remain uniformly bounded in `L^infty` across compact aperture ranges and bounded eigenvalue windows because active prime translations decompose into positive atomic jump Dirichlet forms plus bounded scalar shifts.

PL-338 shows that the same architecture persists at **every finite prime-power activation**. At the threshold for `q=p^k`, the newly born arithmetic channel is first-order flat:

`P_q = O(delta/L_delta) = o(delta)`.

If the transported simple branch has nonzero limiting boundary trace `C_0`, the leading reflected correlation is

`P_q ~ 4 Lambda(q)/sqrt(q) C_0^2 delta/L_delta > 0`.

Thus a finite prime-power channel is born with favorable sign precisely when the relevant boundary coefficient does not collapse. The smallness is universal at birth; the sign is encoded by the squared source-selected trace rather than by a generic semigroup positivity statement.

The reusable lesson is that **activation geometry and branch state geometry separate cleanly**. Uniform jump-form boundedness controls the moving source and endpoint error across activations, while each new channel reduces locally to a boundary-trace noncollapse question. This extends the first-prime mechanism without pretending that all later arithmetic dynamics are solved.

**Boundary.** PL-338 is local to each finite activation threshold. It does not prove that one simple branch survives and stays correctly ordered through arbitrarily many activations, that all relevant traces remain uniformly nonzero, or that the accumulated multi-channel tail has a favorable global sign. The next frontier is therefore branch transport/noncollapse and scalable tail geometry across many activation events, not the original first-prime concentration gate.