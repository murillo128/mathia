# MI-015 — Symmetric-taper worst starts have the same coarse scale as a binary Ising problem

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy/certificate hierarchy through VIS-221, classical symmetric-Grothendieck comparison in [VIS-222](../../findings/VIS-222-symmetric-grothendieck-constant-factor-sdp-torus-equivalence.md), exact midpoint-gauge/real-elliptope reduction in [VIS-223](../../findings/VIS-223-midpoint-symmetric-taper-real-elliptope.md), and the real symmetric-Grothendieck specialization in [VIS-224](../../findings/VIS-224-midpoint-symmetric-taper-ising-constant-factor-equivalence.md). No prime-specific asymptotic estimate, exact Ising optimizer, recurrence-time theorem or RH consequence is claimed.

For fixed `y,H`, VIS-213 identifies the worst start exactly with the unit-modulus quadratic optimum

`M_abs(A_(y,H)) = max_(|z_p|=1) |z* A_(y,H) z|`.

VIS-222 proves that the full correlation SDP has the same objective scale up to a universal complex symmetric Grothendieck factor. VIS-223 then uses midpoint symmetry to gauge the canonical matrix to a real symmetric signed ratio-shell matrix

`A = D_H* B D_H`

and collapses the complex SDP exactly to the real elliptope.

VIS-224 shows that even the continuous torus is unnecessary for deciding boundedness versus divergence of the normalized objective. Define

`I_abs(B)=max_(epsilon_i in {+1,-1}) |epsilon^T B epsilon|`.

The real symmetric Grothendieck inequality gives pointwise

`I_abs(B) <= M_abs(A) <= U_abs^R(B) <= K_gamma^R I_abs(B)`,

with `K_gamma^R <= sqrt(2)(8/pi-1) < 2.188`.

Hence the binary Ising optimum, exact continuous-phase worst-start optimum and full real correlation SDP are universally constant-factor equivalent. After division by the Haar scale `sqrt(R_v)`, one is bounded exactly when the others are bounded, and one diverges exactly when the others diverge.

For the quadratic taper the centered couplings are explicit real signed ratio shells. The binary proxy therefore preserves the canonical coupling magnitudes and shell signs rather than inserting artificial continuous edge phases. Continuous vertex phases can improve a finite optimum, but only by a universal factor; high SDP rank can obstruct exact optimizer recovery, but cannot create a different asymptotic objective scale.

The live static theorem is now purely arithmetic/combinatorial: estimate

`I_abs(B_(y,H))/sqrt(R_v(y,H))`

in a growing prime regime. A bounded ratio gives Haar-RMS-scale exact worst starts immediately; a divergent ratio forces divergent exact worst starts. The already accepted local clue `CLUE-prime-phase-sdp-rms-tightness` records this unresolved test.

**Boundary.** The reduction requires a midpoint-symmetric real taper. It does not solve the Ising optimization, recover exact torus maximizers, or control the time needed for the one-parameter prime-log orbit to approach them. The durable gain is representational: coarse static scale is already visible on the sign hypercube.