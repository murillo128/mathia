# VIS-107 — exact order-three Markov types leave only one area-area chronology direction

## Claim

Consider a finite scalar word after a fixed numerical embedding of its alphabet, and its ordinary three-delay polygonal path

`w_i=(x_i,x_(i+1),x_(i+2)) in R^3`.

Fix the initial three-symbol context and the complete length-four-block count table, so the admissible words form one exact order-three Markov type in the sense of `VIS-099`/`VIS-100`. Let

`P_AA ell_4 = q_1 B_1 + q_2 B_2 + q_3 B_3`

be the canonical degree-four area-area projection from `VIS-104`, with

`B_1=[u_12,u_13]`, `B_2=[u_12,u_23]`, `B_3=[u_13,u_23]`.

Then throughout the entire exact type class:

- `q_2` is constant;
- `q_1+q_3` is constant.

Equivalently, the centered area-area support is contained in the one-dimensional affine direction

`span(B_1-B_3)`.

Thus the nominally three-dimensional `P_AA` channel has only **one assembly-sensitive degree of freedom** after conditioning on the exact order-three Markov type. The only possible centered area-area chronology coordinate is proportional to `q_1-q_3`.

This bound is sharp in principle. The explicit equal-local-inventory collision in `VIS-097` changes the area-area coefficient by

`(1/4,0,-1/4)`,

which lies exactly in the surviving `B_1-B_3` direction.

**Evidence/status:** `EXACT-DERIVED + INFORMATION-BOUNDARY + SHARPNESS + CLASSICAL-EULER-TOUR-CONNECTIVITY + NO-NOVELTY-CLAIM`.

The repeated affine-line collapse observed empirically in the five complete type classes of `VIS-105`--`VIS-106` is therefore structural for this quotient, not an accident of those finite source words.

## 1. Every closed scalar three-delay excursion has equal `12` and `23` areas

Take any closed piece of a scalar three-delay path. Write its scalar coordinates as

`z_0,z_1,...,z_(L+2)`

with delay vertices

`W_i=(z_i,z_(i+1),z_(i+2))`, `0<=i<=L`,

and closure

`W_L=W_0`.

Hence

`z_L=z_0`, `z_(L+1)=z_1`, `z_(L+2)=z_2`.

For a closed polygonal path, the coefficient of `u_12` in its second signature level is the signed polygon area

`a_12=(1/2) sum_(i=0)^(L-1) [z_i z_(i+2)-z_(i+1)^2]`.

The coefficient of `u_23` is

`a_23=(1/2) sum_(i=0)^(L-1) [z_(i+1) z_(i+3)-z_(i+2)^2]`.

Shift the second sum by one index. All interior terms coincide with the first sum, while the endpoint difference is

`(1/2)[z_L z_(L+2)-z_(L+1)^2-z_0 z_2+z_1^2]=0`.

Therefore every closed scalar three-delay excursion has second-level area vector of the form

`S^2(C)=a u_12+b u_13+a u_23`.

The equality of the first and third area coordinates is forced purely by the one-step shift geometry of the delay embedding.

## 2. Swapping two closed excursions changes only `B_1-B_3`

Let two closed three-delay excursions have area vectors

`S^2(C) = a u_12+b u_13+a u_23`,

`S^2(D) = c u_12+d u_13+c u_23`.

`VIS-104` gives the exact degree-four change under swapping closed pieces:

`S^4(C*D)-S^4(D*C)=[S^2(C),S^2(D)]`.

Its `B_1,B_2,B_3` coefficient vector is

`(a d-b c, a c-a c, b c-a d)`

`=(kappa,0,-kappa)`.

So a closed-excursion swap preserves both `q_2` and `q_1+q_3` exactly. It may change `q_1-q_3`, and `VIS-097` shows that this remaining direction can genuinely be nonzero.

## 3. The same invariance holds for a directed Euler-tour T-transformation

The exact Markov type from `VIS-099` is an Eulerian reassembly problem on the directed three-context multigraph: each length-four block is one directed edge from its initial triple to its shifted terminal triple.

The standard directed Euler-tour T-transformation exchanges two directed subtrails with the same ordered endpoints. Locally write the affected portion of one tour as

`M=A*Q*B`

and the transformed portion as

`M'=B*Q*A`,

where `A` and `B` run from the same state `u` to the same state `v`, while the intervening `Q` runs from `v` back to `u`.

Both `M` and `M'` have the same oriented-edge multiset and the same endpoints. By `VIS-096`, their signatures agree through degree three. Append the same path `Q` to both. Then

`M*Q=(A*Q)*(B*Q)`,

`M'*Q=(B*Q)*(A*Q)`.

The two factors are closed three-delay excursions, so Section 2 shows that their degree-four area-area difference is `(kappa,0,-kappa)`. Because `M` and `M'` already agree through degree three, Chen multiplication by the common appended `Q` does not alter their degree-four difference. The same is true after restoring any common prefix and suffix of the full tour.

Hence **every directed Euler-tour T-transformation preserves `q_2` and `q_1+q_3`** for the scalar three-delay path.

## 4. Connectivity promotes the local swap invariant to the whole Markov type

The Markov type may be an open Euler trail rather than a circuit, but its initial context and transition-count table fix the terminal context. Convert every admissible trail to a rooted closed three-delay tour in a common way.

Choose three fresh numerical sentinel symbols not used by the embedded alphabet and a fresh root triple `R`. Prefix every admissible word by the same three-delay path from `R` to the fixed initial context, and suffix it by the same three-delay path from the fixed terminal context back to `R`. The sentinel-containing intermediate states occur only in these fixed chains, so `R` has a unique incoming/outgoing placement and supplies a common root. The added directed context edges balance the original start/end defect, producing one directed Eulerian multigraph shared by all admissible words.

The original trails agree through degree three by `VIS-096`; the prefix and suffix are fixed. Therefore the degree-four difference between two augmented rooted tours is exactly the degree-four difference between their original paths.

Directed Euler-tour T-transformation graphs are classically connected. Xueliang Li, **A lower bound for the connectivity of directed Euler tour transformation graphs**, *Discrete Mathematics* 163 (1997), 101--108, DOI `10.1016/0012-365X(95)00313-L`, explicitly records Xia's connectedness theorem for the T-transformation graph. Fuji Zhang and Xiaofeng Guo, **Hamilton cycles in directed Euler tour graphs**, *Discrete Mathematics* 64 (1987), 289--298, DOI `10.1016/0012-365X(87)90198-1`, study the same directed transformation graph; Torsten Mütze's 2023 Gray-code survey describes the flip as exchanging two directed subtrails between the same pair of vertices.

Consequently any two augmented rooted Euler tours are joined by a finite sequence of the transformations handled in Section 3. Since `q_2` and `q_1+q_3` survive each transformation, they are constant on the entire augmented tour class and therefore on the original exact Markov type.

A self-loop in the three-context graph can only be an edge `aaa -> aaa`, whose geometric delay increment is zero. Such zero edges may be removed for the transformation argument and reinserted arbitrarily without changing any path-signature level, so they do not create an exception.

## 5. Signature and log-signature give the same centered boundary

`VIS-096` proves that the exact type class fixes signature levels one through three. `VIS-103` then gives, pointwise on that type class,

`ell_4=s_4+C`

for one fixed degree-four tensor `C`.

Therefore all pairwise degree-four differences, and in particular the two invariants just proved for the `P_AA` projection, are identical for signature and log-signature after centering. The theorem applies directly to the `P_AA ell_4` statistic used in `VIS-104`--`VIS-106`.

## 6. Prior art and novelty assessment

The ingredients are classical or already canonical in this line. Markov types and their Eulerian context-graph representation are classical (`VIS-099`--`VIS-100`; Whittle and later Markov-type counting literature). Connectivity of directed Euler tours under T-transformations is classical graph theory (Xia as recorded by Li; Zhang--Guo). Chen multiplicativity, path signatures, tensor logarithms, and the free-Lie area-area bracket are classical signature theory and are already bounded by the prior-art audits in `VIS-096`, `VIS-103`, and `VIS-104`.

A targeted literature search found the standard Markov-type/Euler-tour and path-signature ingredients, but no basis for claiming novelty for their combination. This finding therefore makes **no novelty claim**. Its value is the exact Mathia information audit: the scalar shift structure forces every closed delay excursion into the plane `a_12=a_23`, and classical Euler-tour connectivity propagates that local bracket restriction across the complete exact conditional null.

## Boundary and falsification

This finding concerns only:

- the ordinary scalar three-delay path;
- fixed numerical symbol embedding;
- fixed initial triple and complete length-four-block count table;
- the degree-four area-area subspace `C_AA`;
- exact conditional reassembly within one order-three Markov type.

It does **not** show that the full fourth signature/log-signature is one-dimensional, that higher signature levels collapse, that a different nonlocal carrier is local-block determined, that continuous information discarded by quantization is absent, or that zeta zeros agree with CUE. It gives no RH criterion.

The claim is falsified by any admissible pair in one exact type class with different `q_2` or different `q_1+q_3`; equivalently, by a valid T-transformation whose area-area change has a nonzero `B_2` component or nonzero sum of the `B_1,B_3` components. The local geometric lemma is falsified by a closed scalar three-delay excursion with unequal `u_12` and `u_23` second-level coefficients.

## Visual consequence

No canonical PNG is retained. The decisive geometry is exact and low-dimensional: the scalar shift forces all closed-excursion area vectors into the plane `(a,b,a)`, whose pairwise bracket lies on the single line `(kappa,0,-kappa)`. Rendering that line would add presentation but no evidence beyond the algebraic statement.

## Research consequence

The structural subquestion left open by `VIS-106` is resolved: the affine-line behavior seen in five finite type classes is universal for the exact order-three Markov-type quotient used by this branch.

The `P_AA` source experiment should therefore no longer be described as a three-direction chronology carrier after conditioning. It has one surviving centered direction, `B_1-B_3`, and the already predeclared adjacent-block panel in `VIS-106` was negative for the basis-independent norm built from that support.

Further adjacent-window search on the same carrier remains scientifically spent. A future source-specific test should either supply an independently justified new source/height-scale hypothesis for this single surviving direction, fixed before inspecting new material, or move to a materially different nonlocal information carrier with its own exact lower-information null. Any positive source residual still requires the appropriate finite-size CUE or other non-arithmetic control before arithmetic interpretation.