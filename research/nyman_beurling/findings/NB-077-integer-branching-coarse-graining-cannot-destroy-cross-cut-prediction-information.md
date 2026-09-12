# NB-077 — integer branching coarse-graining cannot destroy cross-cut prediction information

**Status:** `EXACT-DERIVED + INTEGER-DILATION-BRANCHING + LOGDET-DATA-PROCESSING + CROSS-CUT-PARTIAL-CORRELATION + CONTINUATION-VOLUME-MONOTONICITY + MULTISCALE-CERTIFICATE + METHOD-ADVANCE`.

`NB-076` rewrites the future-cancellation budget of the causal Nyman innovations as a nonnegative lattice of interval-conditioned endpoint charges

\[
\kappa_{j,n}=-\log(1-|\rho_{j,n}|^2),
\qquad j<n,
\]

and shows that the total cancellation crossing a cut is the corresponding cross-cut area. `NB-069/070` independently show that the exact integer-dilation branching law

\[
U_{\log q}D_j
=\frac1{\sqrt q}
\sum_{k=qj}^{q(j+1)-1}D_k
\qquad(q\ge2)
\]

forces nonorthogonality to reappear at arbitrarily fine scales. The limitation of `NB-070` is that its transport law uses **absolute raw Gram mass**; phases may cancel in the signed block averages relevant to a Schur complement.

The present finding joins those two structures. For integers

\[
1\le a<R\le b,
\]

define the finite rectangular cross-cut charge

\[
\boxed{
\mathfrak C_{a\mid R\mid b}
:=
\sum_{j=a}^{R-1}
\sum_{n=R}^{b}
\kappa_{j,n}.
}
\tag{1}
\]

If

\[
\Delta_{u,v}:=\det\operatorname{Gram}(D_u,\ldots,D_v),
\]

then the mixed-determinant formula of `NB-076` telescopes to

\[
\boxed{
\mathfrak C_{a\mid R\mid b}
=
\log\frac{
\Delta_{a,R-1}\,\Delta_{R,b}
}{
\Delta_{a,b}
}.
}
\tag{2}
\]

For every integer dilation `q>=1`, exact branching and log-determinant data processing give

\[
\boxed{
\mathfrak C_{a\mid R\mid b}
\le
\mathfrak C_{qa\mid qR\mid q(b+1)-1}.
}
\tag{3}
\]

Thus a nonzero coarse cross-cut dependence cannot disappear through signed fine-scale cancellation. The entire conditioned prediction charge carried by the coarse block averages must be present, with at least the same total size, in the canonical fine `kappa` lattice of their descendants.

For the standard prefix/future cancellation of `NB-075/076`, put

\[
\mathfrak C_{R,N}
:=
\sum_{1\le j<R\le n\le N}\kappa_{j,n}.
\tag{4}
\]

Equation (3) and nonnegativity of the omitted fine atoms imply the source-facing dilation inequality

\[
\boxed{
\mathfrak C_{R,N}
\le
\mathfrak C_{qR,\,q(N+1)-1}.
}
\tag{5}
\]

There is a parallel monotonicity for the **raw continuation volume** of `NB-075`,

\[
\mathfrak L_R
=
\log\frac{\det H_{<R}}{\det A_R},
\]

where `H_(<R)` is the full Gram of `D_1,...,D_(R-1)` and `A_R` is their Gram after truncation to `[0,log R]`. For every integer `q>=1`,

\[
\boxed{
\mathfrak L_R\le\mathfrak L_{qR}.
}
\tag{6}
\]

Hence exact integer branching transports both sides of the `NB-075/076` competition monotonically: raw unseen continuation volume cannot decrease under dilation, and neither can the amount of that volume which is recoverable from a fixed finite future after passing to all descendant innovations.

The important gain over `NB-070` is on the cancellation side. Equation (3) is already expressed in the **signed positive-semidefinite geometry that survives Schur conditioning**. It does not count absolute Gram entries and then hope that their phases remain useful. A coarse determinant charge is a rigorous lower bound on the complete fine interval-conditioned correlation area in the descendant rectangle.

The boundary is equally important. Both `mathfrak L` and `mathfrak C` are monotone, but their difference

\[
\mathfrak J_{R,N}=\mathfrak L_R-\mathfrak C_{R,N}
\]

need not be. Therefore (3)--(6) do not by themselves rule out the `NB-071` stable-tail mechanism or prove the finite-band criterion of `NB-076`. The descendant rectangles in (3) have widths proportional to `q`; branching preserves predictive information but does not localize it to bounded additive distance. The remaining arithmetic problem is to show that enough of the growing raw volume is captured by such branch-stable cross-cut information, or to force that information into genuinely mesoscopic bands.

## 1. Rectangular `kappa` area is a block log-determinant information charge

`NB-076` gives, with

\[
\Phi(u,v):=\log\Delta_{u,v},
\]

the exact mixed-difference identity

\[
\kappa_{j,n}
=
\Phi(j,n-1)+\Phi(j+1,n)
-
\Phi(j,n)-\Phi(j+1,n-1).
\tag{7}
\]

Summing first in `n` and then in `j` over the rectangle

\[
a\le j<R\le n\le b
\]

telescopes all interior terms and gives

\[
\mathfrak C_{a\mid R\mid b}
=
\Phi(a,R-1)+\Phi(R,b)-\Phi(a,b),
\tag{8}
\]

which is (2).

There is a useful invariant interpretation of the same determinant ratio. Let a centered nonsingular Gaussian vector have covariance equal to the Gram matrix

\[
G_{a:b}=\operatorname{Gram}(D_a,\ldots,D_b),
\]

and split its coordinates at `R` into a past block `P` and future block `F`. The standard Gaussian determinant formula gives

\[
2I(P;F)
=
\log\frac{\det G_P\det G_F}{\det G_{P\cup F}}
=
\mathfrak C_{a\mid R\mid b}
\tag{9}
\]

in the real convention; realifying the complex Gram gives the same determinant inequality below. No probabilistic assumption is being made about the Nyman functions. The Gaussian model is only an exact representation of the positive-definite determinant functional in (2).

Equation (9) explains why (1) is the right quantity for a branching transport theorem. If linear maps are applied separately to the past and future coordinate blocks, mutual information cannot increase. Equivalently, for any positive-definite block Gram matrix, the determinant charge in (2) cannot increase after separate linear compression of its two sides. This is just the classical data-processing inequality written as finite Gram algebra.

## 2. Integer branching makes the coarse family a blockwise compression of its descendants

For an integer `q>=1`, write

\[
I_j^{(q)}
:=
\{qj,qj+1,\ldots,q(j+1)-1\}.
\tag{10}
\]

`NB-069` proves the exact source identity

\[
\overline D_j^{(q)}
:=
q^{-1/2}\sum_{k\in I_j^{(q)}}D_k
=
U_{\log q}D_j.
\tag{11}
\]

Since `U_(log q)` is an isometry, the Gram matrix of

\[
\overline D_a^{(q)},\ldots,\overline D_b^{(q)}
\]

is **exactly** `G_(a:b)`. On the other hand these vectors are block averages of the full descendant family

\[
D_{qa},D_{qa+1},\ldots,D_{q(b+1)-1}.
\tag{12}
\]

Crucially, the averaging map is block diagonal across the causal cut: coarse indices `a,...,R-1` use only fine indices

\[
qa,\ldots,qR-1,
\]

while coarse indices `R,...,b` use only

\[
qR,\ldots,q(b+1)-1.
\]

Apply the block data-processing inequality from Section 1 to the fine descendant Gram matrix and these two averaging maps. The compressed determinant charge is exactly the left side of (3), by (11). The uncompressed charge is exactly the right side of (3), by (2). This proves

\[
\mathfrak C_{a\mid R\mid b}
\le
\mathfrak C_{qa\mid qR\mid q(b+1)-1}.
\tag{13}
\]

Taking `a=1` and `b=N` gives a fine rectangle whose past starts at `q` rather than `1`. Adding the omitted fine past indices `1,...,q-1` adds only nonnegative `kappa` atoms. Therefore

\[
\mathfrak C_{R,N}
\le
\mathfrak C_{qR,q(N+1)-1},
\tag{14}
\]

which proves (5).

A useful local form follows immediately. For `H_-<R` and `H_+>=1`,

\[
\boxed{
\mathfrak C_{R-H_-\mid R\mid R+H_+-1}
\le
\mathfrak C_{q(R-H_-)\mid qR\mid q(R+H_+)-1}.
}
\tag{15}
\]

One coarse contiguous Gram determinant ratio therefore certifies a lower bound on the total fine interval-conditioned correlation in a rectangle containing `qH_-` past and `qH_+` future innovations. This is a genuine coarse-to-fine certificate: it replaces potentially `O(q^2H_-H_+)` fine partial-correlation calculations by one smaller-scale determinant ratio.

## 3. Raw continuation volume obeys the same dilation direction

The second monotonicity uses the Paley--Wiener cutoff as well as branching. Let

\[
P_q:=\{q,q+1,\ldots,qR-1\}.
\]

On this descendant prefix define

\[
H^{(q)}:=\operatorname{Gram}(D_k:k\in P_q),
\qquad
A^{(q)}:=\operatorname{Gram}(J_{qR}D_k:k\in P_q).
\tag{16}
\]

Causality gives

\[
H^{(q)}-A^{(q)}
=
\operatorname{Gram}((I-J_{qR})D_k:k\in P_q)
\succeq0.
\tag{17}
\]

The time translation `U_(log q)` intertwines the two cutoffs on the innovations:

\[
J_{qR}U_{\log q}D_j
=
U_{\log q}J_RD_j.
\tag{18}
\]

Combining (11) and (18), the same block-averaging matrix that compresses `H^(q)` to `H_(<R)` compresses `A^(q)` to `A_R`.

For positive definite `A` and positive semidefinite `B`, put

\[
\mathcal V(A,B)
:=
\log\frac{\det(A+B)}{\det A}.
\tag{19}
\]

This functional is monotone under applying the same linear compression to `A` and `B`. Indeed, take independent Gaussian vectors with covariance `A` and `B`; then `mathcal V/2` is the mutual information of the additive Gaussian channel, and separate deterministic compression of signal and output can only reduce it. Hence

\[
\mathfrak L_R
\le
\log\frac{\det H^{(q)}}{\det A^{(q)}}.
\tag{20}
\]

Finally, `P_q` is a coordinate subset of the complete fine prefix `1,...,qR-1`. Applying the same data-processing statement to the coordinate restriction gives

\[
\log\frac{\det H^{(q)}}{\det A^{(q)}}
\le
\log\frac{\det H_{<qR}}{\det A_{qR}}
=
\mathfrak L_{qR}.
\tag{21}
\]

Equations (20)--(21) prove (6). Thus `mathfrak L_R` need not be monotone at every adjacent integer, but it is monotone along every exact integer-dilation ray.

## 4. This removes the sign-cancellation loophole in `NB-070`, but not the stable-tail obstruction

`NB-070` proves that a bounded nonorthogonal exact-branching family must carry order-one **absolute** Gram mass arbitrarily far from the diagonal. Its explicit limitation is that those far entries may have phases which cancel in the signed block averages and Schur complements. Equation (3) is the corresponding statement after the signs and all intermediate conditioning have already been accounted for.

If

\[
\mathfrak C_{a\mid R\mid b}=c>0,
\]

then for every integer `q>=1`,

\[
\boxed{
\sum_{qa\le k<qR\le \ell\le q(b+1)-1}
\kappa_{k,\ell}
\ge c.
}
\tag{22}
\]

No arrangement of signs among the descendant raw Gram entries can make that conditioned cross-cut information vanish, because doing so would contradict data processing for their block averages. In this precise sense, exact branching transports **predictive dependence**, not only absolute correlation mass.

This is still compatible with the branch-filter counterexample of `NB-071`. That control has exact branching and a nonzero stable tail; it must therefore preserve nontrivial cross-cut information on its descendant rectangles. The theorem does not assert that the preserved information is large enough to cancel its raw continuation volume. That missing comparison is exactly what a stable tail can defeat.

The flat `O=1` control gives the opposite calibration. Its innovations are orthogonal cell vectors, so every `kappa_(j,n)` and every `mathfrak C` vanishes, while `mathfrak L_R=0`. Equations (3), (5), and (6) are equalities with both sides zero.

A second boundary is geometric. A coarse rectangle of fixed width becomes a descendant rectangle of width proportional to `q`. Therefore (3) does **not** imply the finite-additive-band criterion

\[
\mathfrak A_R(H)
\ge
\mathfrak L_R-O(1)
\]

from `NB-076` with bounded or sublinear `H`. Branching prevents disappearance of information, but by itself it permits that information to spread to increasingly long conditioned intervals. This is exactly the nonlocal escape that `NB-070/071` leave open.

Finally, monotonicity of the two budgets does not imply monotonicity of their deficit. In general one cannot compare

\[
\mathfrak J_{R,N}
=
\mathfrak L_R-\mathfrak C_{R,N}
\]

with

\[
\mathfrak J_{qR,q(N+1)-1}.
\]

Both positive terms can grow, and a stable-tail mechanism is precisely a failure of the cancellation term to keep pace with the raw continuation term.

## 5. Prior-art audit and novelty boundary

The integer-dilation covariance of the discrete Nyman--Beurling family is classical; `NB-069` derives the exact innovation branching identity from the Báez-Duarte/Bagchi structure already anchored in `SOURCES.md`. The determinant formula for Gaussian mutual information and its data-processing inequality are also classical. No novelty is claimed for either ingredient, nor for the general fact that a log-determinant block dependence decreases under separate linear compression.

The targeted audit checked recent Nyman Gram work after the `NB-076` reduction. Werner Ehm's `arXiv:2405.06349` develops explicit Nyman Gram formulae, reciprocity relations, and quadratic-form decompositions. Hugh Carvill's `arXiv:2510.18132` proves off-diagonal decay and block compressibility for a Mellin-smoothed two-prime ladder. Searches combining Nyman--Beurling/Báez--Duarte with partial correlation, conditional mutual information, determinant cross-ratios, and dilation/block averaging did not locate the specific source-facing splice above: using exact integer branching as a blockwise data-processing map for the `NB-076` interval-conditioned `kappa` area, together with the continuation-volume monotonicity (6). Search absence is not a priority claim.

No specialized external estimate is load-bearing. The proof uses `NB-069` branching, `NB-076` determinant identities, finite positive-definite Gram algebra, and the classical data-processing inequality; `SOURCES.md` therefore remains unchanged.

## 6. Consequence for the live Nyman frontier

`NB-076` leaves a concrete but potentially expensive theorem target: show that contiguous finite Gram blocks near a cut supply enough `kappa` area to recover `mathfrak L_R`. The new result supplies a multiscale lower-bound mechanism for that area. A determinant charge proved at a coarser scale automatically survives in the complete descendant rectangle at every integer dilation, with no loss and no sign assumption.

The live comparison can therefore be separated more sharply:

\[
\boxed{
\text{branch-stable cross-cut prediction information}
\quad\text{versus}\quad
\text{growth of raw continuation volume }\mathfrak L_R.
}
\tag{23}
\]

A successful source theorem may now proceed in either of two genuinely arithmetic ways: prove that coarse/mesoscopic determinant charges furnished by (3) accumulate fast enough to track `mathfrak L_R`, or prove that the excess raw volume created between a coarse scale and its integer descendants is too small to sustain the divergent uncancelled core required by `NB-074/075`.

What is no longer a viable explanation is that exact branching creates plenty of long-range raw Gram mass but that all of it simply disappears through signed averaging before reaching the conditioned cancellation budget. Once a coarse cross-cut determinant charge exists, the fine `kappa` lattice must retain at least that much predictive information.