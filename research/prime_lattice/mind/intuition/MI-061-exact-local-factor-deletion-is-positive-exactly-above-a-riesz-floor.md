# MI-061 — Exact local-factor deletion is positive exactly above a Riesz floor

**Evidence level:** exact finite-dimensional range characterization from [PL-421](../../findings/PL-421-local-factor-dephasing-image-cone.md), sharpening the ambient nonpositivity obstruction of MI-060/PL-420.

The favorable restricted cone left open by PL-420 is now explicit. After removing a harmless positive scalar, insertion of the odd-prime local factor is the dephasing map

`Psi_p(R)=((p-2)/(p-1))R + (1/(p-1))Diag(R)`.

Its inverse is positive on a target covariance `S` exactly when

`S - (1/(p-1))Diag(S) >= 0`.

On the positive diagonal support, normalize `S` to the correlation matrix `C=Diag(S)^(-1/2) S Diag(S)^(-1/2)`. Then exact local-factor deletion preserves positivity if and only if

`lambda_min(C) >= 1/(p-1)`.

At the live prime `p=5`, the threshold is exactly `1/4`. In Gram language, the four normalized residue vectors must form a Riesz sequence with lower bound `1/4`. Generic positive semidefiniteness supplies only the floor `0`, so this is a genuinely stronger arithmetic matrix theorem rather than a reformulation of PSD.

This converts the vague “actual arithmetic image may lie in a good cone” escape into a falsifiable source requirement. One may attack it through a direct lower-frame estimate, an operator-norm decorrelation bound such as `||C-I||_op<=3/4`, or stronger pairwise coherence control. But the theorem must apply to the actual full residue/character covariance at the stage where de-aliasing is performed and must not import the desired critical-line conclusion circularly.

The geometry also explains the sign loss in PL-420. Local-factor insertion adds a private orthogonal component of squared weight `1/(p-1)` to every residue direction while attenuating shared coherence. Exact deletion is positive precisely when that private floor can be removed without collapsing some linear combination below zero.

The durable audit is therefore sharper than “retain the full matrix.” A positive source transfer must both retain off-diagonal coherence, as PL-419 requires, and prove membership in this quantitative lower-Riesz cone before exact local deletion. If that floor cannot be established, the route needs a different divisor-faithful representation rather than an appeal to ambient PSD.

**Boundary.** PL-421 characterizes the image cone but does not prove that actual prime or zero correlation matrices belong to it. It concerns the raw local-factor deletion gate only; source/model subtraction can still destroy positivity as PL-418 shows. The result is finite-dimensional local-factor algebra and neither assumes nor proves RH or auxiliary GRH.