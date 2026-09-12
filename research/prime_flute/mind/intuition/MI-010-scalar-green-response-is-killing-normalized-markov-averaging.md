# MI-010 — Source-weighted Green strength is defect-scale avoidance, and internal energy-normalized sources satisfy it automatically

**Evidence level:** proved for finite positive sections of the canonical prime-flute boundary response through PF-314; no final physical `P/H` weak/Schatten estimate, canonical source-identification theorem, or arithmetic discrimination theorem is claimed.

PF-303--PF-312 normalize the assembled constant chain, separate low screening from residual high conversion, and show that inversion does not create a second normalized angle. With `T=S^(-1/2)ER^(-1/2)` for the post-low constant/high block, the diagonal-normalized mixed Green block has exactly the singular values of `T`; raw amplification splits into the unchanged angle and diagonal Green strengths.

PF-313 characterizes the left diagonal strength without inversion. Writing `F_C=S-ER^(-1)E*`, bounded source-weighted Green norm `||F_C^(-1/2)J_C||<=K` is equivalent to

`J_C J_C* <= K^2 F_C`.

After whitening this becomes `Jhat_C Jhat_C*<=K^2(I-TT*)`, so on a singular direction of value `sigma` the physical source must vanish at least like `sqrt(1-sigma^2)`. The right/reassembly side has the symmetric criterion.

PF-314 identifies when this source condition is automatic. Put the source sector `U`, constant sector `C`, and residual high sector `H` inside one positive three-block form. After shorting `H`, the residual source coupling is `J_H=J-ER^(-1)K`, the source energy is `A_H=A-K*R^(-1)K`, and positivity gives

`J_H A_H^(-1) J_H* < F_C`.

Since `A_H<=A`, any coefficient map `W` with uniformly bounded source energy `||A^(1/2)W||<=K_0` induces `J_C=J_HW` satisfying `J_CJ_C*<=K_0^2F_C`. Thus **an internal source normalized in the energy of the same positive form cannot independently violate the PF-313 defect gate**.

This changes the live diagnostic. Before proving another return-potential estimate, derive the actual physical forcing through the same elimination used for the `C/H` block. If it is an internal energy-bounded residual coupling, diagonal source amplification is already controlled and attention should move to normalized angle, multiplicity/ideal counting, the reassembly side, and signed composition. If it is a direct external injection—PF-308's killing source is the canonical counterexample—or its source-energy norm grows, then that external map is precisely where a new quantitative estimate is required.

The reusable distinction is stronger than “positivity helps.” Positivity constrains the source only when **source coordinates and destination energy belong to one joint positive form and the source is normalized in its own energy**. An arbitrary positive/external normalization does not inherit the Schur defect.

**Boundary.** PF-314 does not identify the canonical physical forcing automatically, prove compactness or weak trace class, control `T`, or show that a divergent external diagonal strength survives final signed reassembly. It classifies one source representation for which PF-313 is free and leaves the representation check itself as a mathematical gate.