# PF-199 — two-sided finite-color localization has no weak-trace counting loss

**Status:** `EXACT-DERIVED + CONDITIONAL-APPLICATION + ENDPOINT-REASSEMBLY + POSITIVE/BOUNDARY`. PF-197 puts every compactly localized principal gradient piece of the PF-175 first-relative-resolvent form into the critical weak ideal `S_{1,\infty}` once its matrix coefficient is in `L log L`. PF-198 then proves that splitting one long Lambert body into `O(a)` fixed-width windows preserves the prime-summable critical coefficient budget. A remaining concern was whether **weak-`S_1` singular-value counting itself** necessarily reintroduces a factor depending on that number of windows. It does not, provided the local principal pieces are localized on **both their input and output sides** before they are summed. Fixed enlargement of the PF-198 translated windows admits a fixed finite coloring by pairwise disjoint supports. Inside each color the localized operators are an orthogonal block sum, so their singular-value counting functions add exactly. Summing the finitely many colors costs only one fixed constant independent of Lambert depth, window count, or prime index.

Consequently, if the local Ponge constants for the two-sided principal pieces grow at most polynomially in Lambert depth as allowed by PF-196/PF-197, then the **entire family of such two-sided localized principal pieces is already in `S_{1,\infty}`** with a prime-summable counting budget. The unresolved endpoint operator burden is therefore narrower: construct the actual global resolvent/parametrix decomposition with those quantitative local constants and control the off-diagonal tails, cutoff/commutator terms, physical cuff/interface pieces, and endpoint conservative splice. PF-199 does not prove that those remainders are weak trace class and does not prove the full first relative resolvent is in `S_{1,\infty}`.

## Claim

For a compact operator `T:H->K` between Hilbert spaces define

\[
N_T(\sigma):=\#\{j:s_j(T)>\sigma\},
\qquad
q(T):=\sup_{\sigma>0}\sigma N_T(\sigma).
\tag{1}
\]

Thus `q(T)` is the counting quasi-norm used in PF-189 and is equivalent to the usual `S_{1,\infty}` quasi-norm.

### A. Orthogonal two-sided families add without loss

Let `A_i:H->K` be compact operators. Suppose there are orthogonal projections `Q_i` on `H` and `P_i` on `K` such that

\[
A_i=P_iA_iQ_i,
\tag{2}
\]

and, for `i\ne j`,

\[
Q_iQ_j=0,
\qquad
P_iP_j=0.
\tag{3}
\]

If

\[
\sum_i q(A_i)<\infty,
\tag{4}
\]

then the sum `A=\sum_iA_i` converges in operator norm, is compact, and satisfies

\[
\boxed{
N_A(\sigma)=\sum_iN_{A_i}(\sigma)
\quad(\sigma>0),
\qquad
q(A)\le\sum_iq(A_i).
}
\tag{5}
\]

### B. A fixed number of colors costs only a fixed constant

Suppose a family is partitioned into `K` colors and (2)--(3) hold within each color. Write

\[
A^{(c)}=\sum_{i\in I_c}A_i,
\qquad
A=\sum_{c=1}^K A^{(c)}.
\tag{6}
\]

Then

\[
\boxed{
q(A)
\le
K\sum_{c=1}^K q(A^{(c)})
\le
K\sum_iq(A_i).
}
\tag{7}
\]

In particular, a coloring number `K=O(1)` cannot create a Lambert-depth factor, a factor equal to the number of windows, or a logarithmic singular-value loss.

### C. Application to the PF-198 Lambert localization

On the exact-area prime/shift module of Lambert depth `a_n`, let

\[
C_n=\sum_jC_{n,j}
\tag{8}
\]

be PF-198's fixed-width coefficient partition. It can be chosen so that

\[
N_n=O(1+a_n),
\qquad
\sum_j\|C_{n,j}\|_{L\log L}
\le
C\frac{d_n(1+a_n)}{\cosh a_n},
\tag{9}
\]

with translated cutoffs having uniformly bounded derivatives and overlap.

Choose for every coefficient window a slightly larger cutoff `eta_{n,j}` that equals one on a neighborhood of `supp C_{n,j}`. The enlargement width is fixed, independent of `n`, `j`, and `a_n`. For the compactly localized **principal parametrix piece** write schematically

\[
B_{n,j}
=
M_{\eta_{n,j}}\,Q_{n,j}
M_{C_{n,j}}P_{n,j}\,M_{\eta_{n,j}},
\tag{10}
\]

where `P_{n,j},Q_{n,j}` are the order-`-1` source/target gradient-resolvent parametrix factors from PF-197, with the harmless zero-order metric/bundle identifications absorbed into them. Ponge's critical theorem then gives

\[
q(B_{n,j})
\le
K_{n,j}\|C_{n,j}\|_{L\log L}.
\tag{11}
\]

Assume the quantitative family bound already isolated as the live PF-197 gate:

\[
K_{n,j}\le C(1+a_n)^m
\tag{12}
\]

for one fixed `m`, uniformly over the windows in module `n`. Then PF-196 and PF-198 imply

\[
\boxed{
\sum_{n,j}q(B_{n,j})
\le
C\sum_n
\frac{d_n(1+a_n)^{m+1}}{\cosh a_n}
<\infty.
}
\tag{13}
\]

Because the PF-198 windows are translates of one fixed bounded family, their fixed enlargements can be colored by a fixed number `K` of residue classes so that enlarged supports are pairwise disjoint within each color. If adjacent module-end pieces are included in the same localization, enlarging `K` by another fixed factor handles the one-dimensional module adjacency; alternatively the finitely many end/corner pieces per module may be left with the interface remainder. In either version `K` is independent of `a_n`, `N_n`, and `n`.

For each smooth outer cutoff let `E_{n,j}=supp eta_{n,j}` and use the characteristic support projections `M_{1_{E_{n,j}}}` on the source and target `L^2` spaces. Equation (10) is unchanged by inserting these projections outside it. Disjoint enlarged supports therefore give the orthogonal source and target projections required in (2)--(3), even though the smooth multipliers `M_{eta_{n,j}}` themselves are not projections. Applying (5)--(7) and (13) yields

\[
\boxed{
B_{\rm loc}:=\sum_{n,j}B_{n,j}
\in\mathcal S_{1,\infty},
\qquad
q(B_{\rm loc})
\le
C_K\sum_n
\frac{d_n(1+a_n)^{m+1}}{\cosh a_n}.
}
\tag{14}
\]

Equation (14) is the precise finite-color conclusion. It concerns the **two-sided compactly localized principal pieces**. It is not an identity between `B_loc` and the full PF-175 relative resolvent.

## 1. Orthogonal support makes the singular values a literal multiset union

From (2)--(3), for `i\ne j`,

\[
A_i^*A_j
=Q_iA_i^*P_iP_jA_jQ_j=0,
\qquad
A_iA_j^*=0.
\tag{15}
\]

Moreover `q(A_i)>=||A_i||`: let `sigma` increase to the largest singular value from below in (1). Thus (4) implies

\[
\sum_i\|A_i\|<\infty,
\tag{16}
\]

so `A=\sum_iA_i` converges in operator norm. Equations (15)--(16) make `A` block diagonal with respect to the mutually orthogonal source and target support subspaces. Hence `A^*A` is the orthogonal direct sum of the `A_i^*A_i`, plus a zero block on the unused source space. The nonzero singular values of `A` are therefore exactly the multiset union of those of the `A_i`. This proves the equality in (5); the quasi-norm bound follows immediately:

\[
\sigma N_A(\sigma)
=
\sum_i\sigma N_{A_i}(\sigma)
\le
\sum_iq(A_i).
\tag{17}
\]

This is stronger than bounded geometric overlap. It is why the outer cutoffs on **both** sides of (10) matter. Disjoint coefficient supports alone do not imply (15) for the original nonlocal pseudodifferential/resolvent pieces.

## 2. Finite colors use only the elementary singular-value counting inequality

For a compact operator `T`, `N_T(alpha)` is the least rank needed to approximate `T` in operator norm to error at most `alpha`: truncate the singular-value decomposition above `alpha`. Therefore, for compact `S,T` and positive `alpha,beta`, choose finite-rank approximants of ranks `N_S(alpha)` and `N_T(beta)` with errors at most `alpha` and `beta`. Their sum has rank at most the sum of the ranks and approximates `S+T` to error at most `alpha+beta`. Hence

\[
\boxed{
N_{S+T}(\alpha+\beta)
\le
N_S(\alpha)+N_T(\beta).
}
\tag{18}
\]

This is the counting form of the classical Fan singular-value inequality. Iterating (18) over the fixed number of colors with `alpha_c=sigma/K` gives

\[
N_A(\sigma)
\le
\sum_{c=1}^K
N_{A^{(c)}}(\sigma/K)
\le
\frac K\sigma
\sum_{c=1}^Kq(A^{(c)}),
\tag{19}
\]

which is exactly (7).

The proof is included because no subtle weak-ideal quasi-triangle theorem is needed. The only price is the fixed coloring number. Classical singular-value inequalities go back to Ky Fan, including *Maximum Properties and Inequalities for the Eigenvalues of Completely Continuous Operators*, Proc. Natl. Acad. Sci. USA **37** (1951), 760--766, DOI `10.1073/pnas.37.11.760`, and *On the Singular Values of Compact Operators*, J. London Math. Soc. (2) **3** (1971), 187--189, DOI `10.1112/jlms/s2-3.1.187`. No novelty is claimed for (18)--(19).

## 3. Why the PF-198 cover has a fixed coloring number

PF-198 deliberately uses fixed-width Fermi windows and notes that the cutoff family may be chosen from translates of one bounded template. Enlarge every support by one fixed buffer needed to define the two-sided parametrix cutoffs. If the translated window spacing is `h>0` and the enlarged support diameter in the longitudinal coordinate is at most `D`, choose an integer

\[
K> D/h+1.
\tag{20}
\]

Windows whose indices agree modulo `K` then have disjoint enlarged supports. Neither `D` nor `h` depends on the Lambert depth. Thus the fact that a deep Lambert body needs `N_n=O(a_n)` windows is irrelevant to the color count.

The same observation is stable under the fixed number of corner/end charts in PF-198 and under the chain adjacency of the flute: one may either increase `K` by a fixed finite factor to keep enlarged supports disjoint across neighboring module ends, or exclude those boundary pieces from `B_loc` and put them into the still-open interface remainder. The result needed here is only that **bulk chart multiplicity does not force `K` to grow with `a_n`**.

## 4. What PF-199 closes and what it does not

PF-197 left three analytically distinct questions entangled under the phrase “localization and reassembly”:

1. whether the local matrix-valued critical theorem exists;
2. whether coefficient fragmentation across `O(a)` charts destroys the critical budget;
3. whether summing the resulting weak-`S_1` pieces necessarily loses another factor at the singular-value counting level.

PF-197 closes the first, PF-198 closes the second, and PF-199 closes the third **for the genuinely two-sided localized principal pieces**. Once (12) is available, their weak-trace budget sums with only a fixed coloring constant.

The unresolved difference between the full principal form

\[
(dR_h)^*M_CdR_g
\tag{21}
\]

and the two-sided local family (10) contains exactly the nonlocal terms that PF-197/PF-198 refused to hide: when outer cutoffs are inserted, at least one gradient-resolvent factor may connect the coefficient support to the complement of the enlarged window. A full global decomposition also generates cutoff commutators, smoothing/parametrix remainders, physical cuff/body transmission terms, and the geometric identification/splice terms. None of these terms is controlled by the orthogonal-support lemma unless it is separately two-sided localized with a summable bound.

In particular, a one-sided expression such as

\[
Q_{n,j}M_{C_{n,j}}P_{n,j}
\tag{22}
\]

with globally supported input or output is **not** an orthogonal block merely because the `C_{n,j}` are disjoint. Applying (5) directly to (22) would repeat exactly the mistake warned against in PF-198.

## Prior art and novelty assessment

The direct-sum singular-value union, approximation-number characterization, Fan inequality, finite coloring of translated intervals, and weak-Schatten counting formalism are classical. Ponge's matrix-valued critical Cwikel estimate is prior art already audited as S20 in `research/prime_flute/SOURCES.md`. No new operator-ideal theorem is claimed.

A targeted search for weak-Schatten direct sums, singular-value counting, disjoint-support Cwikel localization, and finite-color pseudodifferential assembly found the expected classical singular-value/weak-ideal background but no theorem that performs the **prime-flute-specific** decomposition of the actual two-metric global relative resolvent. Search absence is not evidence of novelty.

The project-specific deduction is the boundary (13)--(14): **PF-198's `O(a)` local chart family does not itself cause a weak-`S_1` reassembly loss once the principal pieces are made two-sided local.** The only depth dependence left in that principal family is the local Ponge/parametrix constant already isolated in PF-197; any further endpoint loss must enter through those constants or through the omitted nonlocal/interface/geometric remainder, not through weak-ideal counting of a fixed-color local family.

## Falsification and boundary checks

A later adversary can test PF-199 by:

1. checking (2)--(5) directly and verifying that both source and target support projections are needed for block orthogonality;
2. deriving (18) from finite-rank singular-value truncations and then (19) with thresholds `sigma/K`;
3. checking PF-198's translated fixed-width cover and verifying that a fixed buffer still admits a color number independent of `a_n`;
4. verifying that the local PF-197/Ponge piece can be written with compact **outer** cutoffs on both sides as in (10), rather than silently treating the global resolvent factors as local;
5. retaining (12) as an explicit conditional family estimate and using PF-196/PF-198 to derive the summability in (13);
6. separating any module-end/corner pieces whose enlarged supports are not covered by the chosen coloring and charging them to a fixed-color boundary family or to the still-open interface remainder;
7. rejecting any upgrade from (14) to the full relative resolvent unless every off-diagonal, commutator, smoothing, density/interface, and geometric splice term is separately controlled in a summable endpoint ideal.

PF-199 would be overclaimed if read as proving any of the following, none of which is asserted:

- the family constants (12) for the actual global PF resolvent localization;
- trace or weak-trace bounds for the off-diagonal resolvent tails;
- endpoint control of every cutoff/IMS/parametrix remainder;
- the canonical conservative short-collar splice;
- the full prime/shift first relative resolvent belongs to `S_{1,\infty}`;
- PF-190's global `log^2(n)/n` envelope has already been improved;
- wave/scattering equivalence, prime/clone spectral separation, or any RH implication.

## Consequences for the research line

The weak-endpoint analytic frontier should no longer list **finite-color singular-value counting of the compactly localized principal pieces** as an independent obstacle. PF-196 supplies prime-summable critical currency, PF-197 supplies the correct local matrix theorem, PF-198 shows that `O(a)` coefficient windows preserve that currency, and PF-199 shows that a two-sided fixed-color sum preserves weak-`S_1` counting up to a constant independent of `a`.

The next operator question is correspondingly sharper: build the actual global cutoff/parametrix identity and decide whether the nonlocal tails, commutators, module-end/cuff transmission, and identification terms obey the same prime-summable endpoint budget while the local Ponge constants remain within a fixed-polynomial Lambert-depth envelope. Separately, the geometric endpoint conservative splice remains necessary. A failure beyond PF-199 must now be located in one of those genuine nonlocal/geometric mechanisms, not in the mere number of Lambert windows.