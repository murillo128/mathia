# WI-166 — the arbitrary-weight four-point positive-cover relaxation is already sharp

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + BARRIER`. The surviving pre-collapse branch of `CLUE-four-point-weighted-cover-assembly` has an exact obstruction in the arbitrary-nonnegative-pair-weight/gap relaxation used by the finite WI-011 statements. The unique third-neighbor chord in each four-point certificate gives a window-by-window capacity constraint, and an exact abstract saturation witness shows that no positive weighted cover can improve the scalar `E+P` constant in this relaxation. This is upstream of WI-165 and does not assume that the witness is realizable by the Montgomery--Taylor kernel or by zeta zeros.

No unconditional zero proportion changes in this finding.

## 1. Exact relaxation and local input

Fix `m >= 4` ordered points and let

\[
q=m-3
\]

be the number of consecutive four-point windows. For each window start `s=0,...,q-1`, write the non-pressure part of the certified four-point inequality as

\[
C_s(w)
=
\frac23\bigl(w_{s,s+1}+w_{s+1,s+2}+w_{s+2,s+3}\bigr)
+\bigl(w_{s,s+2}+w_{s+1,s+3}\bigr)
+2w_{s,s+3}.
\tag{1}
\]

The WI-011 finite formalization treats the pair weights as arbitrary nonnegative numbers and the local pressure as an arbitrary nonnegative term, with the local certificate supplied as a hypothesis. For the zeta application the constants are

\[
\varepsilon=\frac{231}{100000},
\qquad
p=\frac1{2500},
\tag{2}
\]

and the pressure in window `s` is `p` times its three-gap span. Abstractly write it as `P_s >= 0`. The local constraints are

\[
\boxed{\varepsilon\le C_s(w)+P_s.}
\tag{3}
\]

The global pair-energy and pressure resources are

\[
E=2\sum_{0\le i<j<m}w_{ij},
\qquad
P=\sum_{s=0}^{q-1}P_s.
\tag{4}
\]

The uniform WI-011 sum uses every local inequality once. The coefficient accounting formalized in `WI011FourPointAssembly.lean` proves

\[
\sum_s C_s(w)\le E,
\tag{5}
\]

hence

\[
\boxed{q\varepsilon\le E+P.}
\tag{6}
\]

The question left open by WI-165 was whether a positive cover assembled before scalar collapse could do strictly better while still dominating arbitrary nonnegative pair weights and gaps.

## 2. The unique third-neighbor chord gives an atomic capacity ceiling

Consider any positive weighted cover built from the same consecutive four-point inequalities. Expand all chosen blocks, lengths, shifts, and placements into their underlying local windows, and let

\[
\beta_s\ge0
\]

be the total multiplicity assigned to local window `s`. If the aggregate pair spend must be dominated coefficientwise by the same global pair-energy `E` for arbitrary nonnegative `w`, inspect the pair

\[
(s,s+3).
\]

It occurs in exactly one consecutive four-point functional, namely `C_s`, where its coefficient is `2`. Therefore the aggregate local coefficient of this pair is `2 beta_s`, while its coefficient in `E` is exactly `2`. Coefficientwise domination forces

\[
2\beta_s\le2,
\qquad\text{so}\qquad
\boxed{\beta_s\le1}
\tag{7}
\]

for every window separately.

Consequently every such positive cover satisfies

\[
\boxed{
\varepsilon\sum_{s=0}^{q-1}\beta_s
\le q\varepsilon.
}
\tag{8}
\]

Because `P_s>=0`, the same `beta_s<=1` also prevents over-spending the available pressure sum. The uniform cover `beta_s=1` for every `s` is feasible by (5), so the ceiling (8) is attained. In linear-programming language, the third-neighbor coordinates alone provide a diagonal dual witness: every atomic local certificate already has its own private pair-energy capacity fully priced at coefficient `2`.

This argument is insensitive to how many block lengths are used. A local window that lies inside several selected blocks merely receives the sum of their positive weights as `beta_s`, and its private third-neighbor chord still imposes (7).

## 3. An exact primal witness closes even adaptive scalar improvements

The coefficientwise argument above assumes the proposed proof exposes a positive cover whose pair domination is checked coefficient by coefficient. A more adaptive rule might instead choose weights after seeing the abstract pair weights or gaps, so that a pointwise statement `beta_s<=1` need not describe every intermediate choice. The relaxation nevertheless has an exact primal saturation witness that blocks any stronger universal scalar conclusion from the same local constraints.

Set all gaps to zero, hence all span pressures to zero, and choose arbitrary nonnegative pair weights by

\[
w_{s,s+3}=\frac{\varepsilon}{2}
\qquad (s=0,\ldots,q-1),
\tag{9}
\]

with every other pair weight equal to zero. The third-neighbor pairs are distinct. For every local window,

\[
C_s(w)+P_s
=2\frac{\varepsilon}{2}
=\varepsilon,
\tag{10}
\]

so every local certificate is saturated exactly. At the same time,

\[
E
=2\sum_s\frac{\varepsilon}{2}
=q\varepsilon,
\qquad
P=0.
\tag{11}
\]

Thus the feasible abstract data attain equality in (6). It follows that the exact minimum of the scalar resource `E+P` over the arbitrary-nonnegative-weight/gap relaxation subject only to the local four-point certificates is

\[
\boxed{
\inf(E+P)=q\varepsilon.
}
\tag{12}
\]

Therefore no positive weighted cover, finite multi-length family, geometry-dependent selection rule, or other argument using only these abstract local constraints can prove a universal scalar lower bound `E+P > q epsilon`. Any such theorem would be false on (9)--(11).

The witness is deliberately **not** asserted to satisfy the Montgomery--Taylor kernel relation `w_{ij}=w(y_j-y_i)`, to arise from a positive-semidefinite Gram matrix, or to be realizable by zeta zeros. Those couplings were explicitly discarded by the arbitrary-weight finite relaxation and remain possible sources of additional information.

## 4. Relation to WI-165

WI-165 is a downstream convex-mixture barrier. Once each block construction has already become a scalar inequality `a_j S >= b_j N-o(N)`, any fixed nonnegative mixture is a convex combination of the constituent ratios and cannot beat the best one. It explicitly left open a geometry-aware positive assembly before scalar collapse.

WI-166 closes that surviving branch only in the arbitrary-weight/gap relaxation demanded by the clue's first decisive test. It acts before the scalar zeta ratio is formed: the private third-neighbor chord caps the multiplicity of each atomic four-point inequality, and the saturation witness proves that the resulting `q epsilon` scalar resource is exact. Hence changing block lengths, overlap patterns, or positive cover weights cannot create a larger universal `E+P` budget unless the proof retains structure absent from this relaxation.

The two barriers are therefore complementary rather than duplicate. WI-165 says positive mixing cannot help **after** independent scalarization; WI-166 says positive cover bookkeeping cannot help **before** scalarization once the pair data have already been relaxed to arbitrary nonnegative weights and the target is only a stronger scalar `E+P` lower bound.

## 5. Prior-art and novelty audit

The capacity argument is elementary linear-programming/packing algebra, not a new external theorem. No priority claim is made. The relevant zeta-specific inputs and their provenance were already audited in WI-009 and WI-011, while `WI011FourPointAssembly.lean` records exactly the arbitrary-nonnegative-weight coefficient pattern used here. The present finding adds only the exact obstruction obtained by reading the unique third-neighbor coefficient as a private capacity and by exhibiting the saturation point (9).

A current-repository audit found no earlier `weil_inertia` finding that closes this pre-collapse arbitrary-weight cover class. WI-165 intentionally stopped short of it. The accepted clue is therefore resolved by a strictly stronger, upstream barrier rather than by rephrasing the weighted-mediant result.

## 6. Consequence and escape test

Within this relaxation, further optimization over positive multi-length block covers is exhausted. An attempted improvement escapes WI-166 only if it keeps or adds information that invalidates the abstract saturation witness. Concrete possibilities include the actual Montgomery--Taylor relation among all pair weights, positive-semidefinite/Gram consistency retained jointly with the local geometry, another spectral invariant before reduction to `E+P`, a rigorously dominated sign-indefinite combination, multiple independent test-function channels, or genuinely new arithmetic/support information.

In particular, a numerical improvement obtained solely by rearranging positive copies of the same four-point inequality must be checked against (7) and (12) before any zeta asymptotics are considered. If its proof remains valid for arbitrary nonnegative pair weights and gaps and still concludes only a stronger scalar `E+P` budget, the witness above rules it out exactly.