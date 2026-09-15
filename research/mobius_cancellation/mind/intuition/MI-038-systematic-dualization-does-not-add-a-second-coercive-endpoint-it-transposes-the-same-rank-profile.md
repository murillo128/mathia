# MI-038 — Systematic dualization does not add a second coercive endpoint; it transposes the same rank profile

**Evidence level:** exact binary-code equivalence from [MC-316](../../findings/MC-316-systematic-submatrix-rank-wei-dual-reflection.md), refining the diagonal generalized-cap frontier [MC-315](../../findings/MC-315-diagonal-projective-generalized-cap-frontier.md).

Put a full `[2R,R]` binary code in systematic form `G=[I_R | P]`. MC-316 converts the near-maximal generalized-weight requirement into an exact family of rectangular submatrix-rank tests on `P`: for the relevant defect parameters, every `(g+a+1) x g` submatrix must retain rank at least `g-t+1` throughout the prescribed range of `g`.

The apparent dual escape is not independent. The dual code has systematic generator `[P^T | I_R]`, and Wei duality turns the same endpoint requirement into the reflected generalized-weight condition on `C^perp`. After systematic reduction this is the transpose of the same submatrix-rank family. The primal hierarchy, the dual hierarchy, and the corresponding erasure/rank formulation are therefore equivalent views of one combinatorial constraint, not separate sources of coercivity that can be combined for extra force.

At the live scale `t_R=ceil(2 log_2(R+1))` and constant defect, the matched-control question remains the existence of binary matrices `P_R` whose **entire required submatrix profile** survives. Standard duality, a second Griesmer calculation, or mirrored erasure language cannot close the frontier because they do not impose information beyond that profile.

This sharpens the generic-versus-arithmetic split. If the required matrices exist generically, the arithmetic source must contribute a realizability restriction not expressible as the same systematic rank tests. If they do not, the obstruction is already finite-geometric. Either way, re-encoding the endpoint through the dual code does not create the missing arithmetic theorem.

**Boundary.** The equivalence is for the systematic binary `[2R,R]` endpoint studied in MC-316. It does not decide whether the required matrix family exists, and it does not rule out genuinely arithmetic constraints on the particular matrices realized by Legendre/source incidence. A theorem using extra arithmetic structure of `P_R` would not be a mere dual reformulation.