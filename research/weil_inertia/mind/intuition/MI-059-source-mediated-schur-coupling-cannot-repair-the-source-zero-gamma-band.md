# MI-059 — Source-mediated Schur coupling cannot repair the source-zero gamma band

**Evidence level:** exact source-conditioned block-operator synthesis from [WI-378](../../findings/WI-378-pure-schur-coupling-cannot-repair-source-zero-gamma-band.md), combining the corrected gamma negative-index profile WI-377 with elementary Hermitian principal-subspace and Schur-complement geometry. The linear algebra is classical; the line-specific content is the zero-credit statement on the actual source-zero sector.

Let `V_(eta,k)` be the WI-377 source-zero subspace on which the corrected archimedean block satisfies

`A_k[F] <= -eta ||F||^2`

with `dim V_(eta,k) >= (q_eta/pi+o(1)) log(k+1)`. Consider an enlarged form with a direct old-space term `P_k`, off-diagonal old--new coupling `B_k`, and new-variable block `D_k`. Because the exact domain contains `V_(eta,k) x {0}`, positivity of the full form already forces

`P_k[F] >= eta ||F||^2` on `V_(eta,k)`.

No off-diagonal coupling can contribute when the new variable is set to zero. If the coupling is source-mediated, `B_k=C_k R_k`, then on the exact source-zero space `Z_k=ker R_k` it vanishes identically. With a positive pivot, Schur elimination only subtracts `B_k^*D_k^(-1)B_k`, so the shortened form is exactly `A_k+P_k` on `Z_k`.

Thus the WI-377 spectral tariff cannot be paid by strengthening the source pivot or its coupling. A successful repaired proof must place extensive positive coercivity directly into the old source-zero sector **before** elimination, with at least the fixed-depth profile `q_eta/pi`, or alter the admissible domain/category so that the certified vectors no longer appear as `(F,0)`.

The durable accounting rule is that coupling capacity and direct old-sector coercivity are different resources. A later Schur identity cannot retroactively create positivity on a principal subspace on which the coupling is absent.

**Boundary.** WI-378 does not classify the full rooted network. An inherited parent form, polar channel or another global term may contribute directly to the old--old block, and a genuinely different admissibility relation may remove the source-zero vectors. The result rules out the coupling-only positive-pivot repair, not every nonadditive construction and not RH.