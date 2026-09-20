# AF-460 — Finite-rank source laws have zero cube-completion defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `COMPLETED-SECANT`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-459 reduces one important stable-fidelity question to the source-side profile

\[
D_k(C)=\inf_B\mathbb E_\varepsilon\operatorname{dist}_1(q^B_\varepsilon,C),
\]

where `C` is a normalized completed-secant carrier and `q^B_\varepsilon` runs over paired sign cubes. A natural possible escape is that finitely many source-law constraints might keep those cubes a positive distance from the physical carrier. They do not, at the level of the normalized kernel carrier.

Let `A` be an infinite alphabet and let

\[
\ell^1_0(A)
=
\left\{h\in\ell^1(A):\sum_{a\in A}h(a)=0\right\}.
\tag{1}
\]

Let

\[
L:\ell^1_0(A)\to E
\tag{2}
\]

be a bounded linear operator with finite-dimensional range `E_0=L(\ell^1_0(A))`. Define the normalized kernel carrier

\[
C_L
=
\{h\in\ker L:\|h\|_1=1\}.
\tag{3}
\]

For a paired block of `2k` distinct atoms

\[
B=((a_1,b_1),\ldots,(a_k,b_k)),
\]

use the AF-459 sign cube

\[
q^B_\varepsilon
=
\frac1{2k}\sum_{j=1}^k
\varepsilon_j(\delta_{a_j}-\delta_{b_j}),
\qquad
\varepsilon\in\{-1,+1\}^k,
\tag{4}
\]

so that `\|q^B_\varepsilon\|_1=1`. Then, for every fixed `k>=1`,

\[
\boxed{D_k(C_L)=0.}
\tag{5}
\]

More strongly, for every `epsilon>0` there is one paired block `B` of `2k` distinct atoms such that

\[
\boxed{
\sup_{\varepsilon\in\{-1,+1\}^k}
\operatorname{dist}_1(q^B_\varepsilon,C_L)
<\epsilon.
}
\tag{6}
\]

Thus finite-rank linear source information cannot make an infinite atomic normalized kernel carrier quantitatively cube-poor. The obstruction is not merely that some kernel secants survive: arbitrarily accurate full paired sign cubes survive at every finite scale.

Combining `(5)` with AF-459 gives the immediate target-geometry consequence. If `Y` has Rademacher type `p>1`, `phi:A->Y` is bounded by

\[
\sup_{a\in A}\|\phi(a)\|_Y\le M,
\]

and the bounded affine observation acts on a physical normalized secant carrier `C` containing `C_L`, then

\[
\kappa_C(F_\phi)
\le
M T_p(Y)k^{1/p-1}
\qquad(k\ge1),
\tag{7}
\]

hence

\[
\boxed{\kappa_C(F_\phi)=0.}
\tag{8}
\]

The reusable Arithmetic Fidelity conclusion is:

\[
\boxed{
\text{finitely many bounded linear source constraints cannot by themselves protect uniform TV fidelity against bounded affine compression into a target of nontrivial type.}
}
\tag{9}
\]

Any genuine escape must come from structure not represented by the full normalized kernel of a finite-rank source map: completion restrictions, positivity/boundary geometry, nonlinear or infinite-dimensional source laws, unbounded marks, a different physical metric, or another mechanism that keeps the actual carrier away from large paired cubes.

## Exact derivation

Fix `k>=1` and choose a base atom `a_0 in A`. For every `a != a_0`, put

\[
x_a=L(\delta_a-\delta_{a_0})\in E_0.
\tag{10}
\]

Because `L` is bounded and

\[
\|\delta_a-\delta_{a_0}\|_1=2,
\]

the family `{x_a}` is bounded in the finite-dimensional space `E_0`. Hence its closure is compact. Since `A` is infinite, there is a point `x_* in E_0` such that for every `eta>0` the ball `B(x_*,eta)` contains arbitrarily many distinct `x_a` after passing to an infinite subfamily or, equivalently, one can find `2k` distinct atoms

\[
a_1,b_1,\ldots,a_k,b_k
\tag{11}
\]

with

\[
\|x_{a_j}-x_*\|_E<\eta,
\qquad
\|x_{b_j}-x_*\|_E<\eta.
\tag{12}
\]

Therefore

\[
\|L(\delta_{a_j}-\delta_{b_j})\|_E
=
\|x_{a_j}-x_{b_j}\|_E
<2\eta.
\tag{13}
\]

For every sign orientation in `(4)`,

\[
\|Lq^B_\varepsilon\|_E
\le
\frac1{2k}\sum_{j=1}^k
\|L(\delta_{a_j}-\delta_{b_j})\|_E
<\eta.
\tag{14}
\]

Because `E_0` is finite-dimensional, choose a bounded linear right inverse

\[
R:E_0\to\ell^1_0(A),
\qquad
LR=I_{E_0}.
\tag{15}
\]

It may be chosen with finite-support range: the vectors `L(\delta_a-\delta_{a_0})` span `E_0`, so choose a finite basis from them and send that basis to the corresponding finitely supported preimages.

Correct each cube orientation by

\[
u_\varepsilon=R Lq^B_\varepsilon,
\qquad
v_\varepsilon=q^B_\varepsilon-u_\varepsilon.
\tag{16}
\]

Then

\[
Lv_\varepsilon=0,
\qquad
\|v_\varepsilon-q^B_\varepsilon\|_1
\le
\|R\|\eta.
\tag{17}
\]

Set `d=\|R\|\eta` and take `eta` small enough that `d<1`. Since `\|q^B_\varepsilon\|_1=1`, equation `(17)` gives

\[
\big|\|v_\varepsilon\|_1-1\big|\le d,
\tag{18}
\]

so `v_\varepsilon !=0`. Normalize inside the kernel:

\[
c_\varepsilon
=
\frac{v_\varepsilon}{\|v_\varepsilon\|_1}
\in C_L.
\tag{19}
\]

Using `(17)` and `(18)`,

\[
\begin{aligned}
\|c_\varepsilon-q^B_\varepsilon\|_1
&\le
\|c_\varepsilon-v_\varepsilon\|_1
+
\|v_\varepsilon-q^B_\varepsilon\|_1\\
&=
\big|1-\|v_\varepsilon\|_1\big|+d\\
&\le2d
=2\|R\|\eta.
\end{aligned}
\tag{20}
\]

The same block `B` works simultaneously for every one of the `2^k` sign orientations. Since `eta>0` is arbitrary, `(6)` follows, and averaging `(20)` gives `(5)`.

No probabilistic selection and no target-space cancellation are used in this step. The collapse is entirely source-side: a bounded finite-dimensional image of infinitely many atoms necessarily contains arbitrarily tight finite clusters, and a finite-dimensional splitting corrects the resulting approximate cube back into the exact kernel at arbitrarily small `ell^1` cost.

## Consequence for type-p targets

AF-459 proves, for a normalized completed-secant carrier `C`,

\[
\kappa_C(F_\phi)
\le
M\left[T_p(Y)k^{1/p-1}+D_k(C)\right].
\tag{21}
\]

If the physical carrier contains `C_L`, then

\[
D_k(C)
\le D_k(C_L)=0,
\tag{22}
\]

so `(21)` becomes `(7)`. For `p>1`,

\[
k^{1/p-1}\to0,
\]

which proves `(8)`.

This cleanly separates the two resources required for stable bounded affine fidelity:

- target geometry must not cancel large balanced mixtures too efficiently; and
- the physical source carrier must itself forbid or quantitatively repel the paired-cube directions that target type can cancel.

Finite-rank linear source information supplies neither protection once its full normalized kernel is physically admissible.

## What this adds to AF-459

AF-459 leaves `D_k(C)` as the live source-side quantity. AF-460 computes it exactly for a broad control class:

\[
\boxed{
C=C_L\text{ for a bounded finite-rank linear source map on an infinite alphabet}
\quad\Longrightarrow\quad
D_k(C)=0\text{ for every }k.
}
\tag{23}
\]

This eliminates one natural explanation for positive cube defect. A finite list of bounded linear moments, conservation laws, coarse coordinates, or other finite-dimensional linear source marks cannot by itself create the asymptotic source rigidity needed to escape AF-459.

The conclusion is stronger than an asymptotic statement `D_k->0`: every fixed cube dimension already has infimum defect zero. What grows with `k` is only how many atoms must be found inside a sufficiently tight cluster of the finite-dimensional source image.

## Prior art and novelty audit

The functional-analytic ingredients are classical, and this finding makes **no novelty claim** for them.

- Felix Cabello Sanchez and Jesus M. F. Castillo, **“Complemented Subspaces of Banach Spaces,”** Chapter 1 of *Homological Methods in Banach Space Theory*, Cambridge University Press (2023), pp. 9--45, DOI `10.1017/9781108778312.003`. This is a modern reference for classical complementability and splitting language in Banach spaces. AF-460 uses only the elementary special case that a bounded operator onto a finite-dimensional range admits a bounded linear right inverse.
- Finite-dimensional normed spaces have compact closed bounded sets, so every infinite bounded family has finite subsets of arbitrary prescribed cardinality at arbitrarily small diameter around an accumulation point. This is standard finite-dimensional compactness rather than a new geometric theorem.
- AF-459 already supplies the Rademacher-type / discrete-cube prior-art bridge and the quantitative inequality `(21)`. AF-460 does not strengthen Banach-space type theory; it computes the source-side cube defect for one classical finite-rank control class.

A fresh prior-art search found the classical complementability framework above but no established result stated in the line-specific `D_k(C_L)=0` language. That absence is not a novelty claim: `(5)` is presented as an exact specialization assembled from standard finite-dimensional compactness, bounded splitting, and the AF-459 definition.

## Boundary and falsification audit

- **The physical-carrier inclusion is essential.** A finite-rank source law does not automatically imply that one prescribed positive source-law fiber contains every normalized kernel direction as a completable secant. Equation `(8)` requires `C_L subset C`, or an independently proved approximation of those kernel cubes by the actual AF-452 completed carrier.
- **Positivity and boundary effects can block completion.** A signed kernel direction may exist algebraically while no sufficiently small common-background completion reaches the prescribed fiber because the source value lies on a boundary or because support/positivity constraints forbid the needed background. Such failure is precisely a possible nonzero source resource; AF-460 does not erase it.
- **Support budgets matter.** The correction operator `R` has finite-support range, but its fixed support is added to the `2k` cube atoms. A hard atom budget can therefore exclude the corrected secants. The theorem concerns the unrestricted normalized kernel carrier unless a separate completion argument preserves the declared budget.
- **Infinite alphabet is substantive.** A finite alphabet admits paired cubes only up to its cardinality and has no infinite clustering argument.
- **Finite rank is substantive.** For infinite-dimensional `L`, the bounded atomic image need not be precompact and a bounded right inverse need not exist. Either failure can keep `D_k` positive.
- **Boundedness is substantive.** Unbounded source marks can separate far-out atoms strongly enough that the cluster step `(12)` fails.
- **TV / `ell^1` normalization is substantive.** The normalization estimate `(20)` and AF-459's defect are in total variation geometry. A different physical source metric needs its own correction modulus.
- **No converse is claimed.** Infinite-dimensional, nonlinear, boundary-restricted, or non-precompact source structure may still have `D_k=0`; escaping this theorem is necessary, not sufficient, for positive bounded affine fidelity.

## Arithmetic specialization

Suppose an arithmetic source is represented on an infinite atomic alphabet by finitely many bounded linear statistics

\[
Lh
=
\left(
\sum_a h(a)\psi_1(a),\ldots,
\sum_a h(a)\psi_q(a)
\right),
\tag{24}
\]

with each `psi_j` bounded. If the actual arithmetic source-law carrier contains the normalized kernel directions of these statistics, then AF-460 gives

\[
D_k=0
\qquad\text{for every fixed }k.
\tag{25}
\]

Therefore no finite collection of such bounded moments or coarse marks can be the mechanism that protects a complexity-independent arithmetic discriminator after bounded affine compression into Hilbert space or, more generally, a target of Rademacher type `p>1`.

For rational-prime applications this sharpens the AF-459 frontier. The next source-side question is not merely whether the prime system obeys finitely many extra constraints. It is whether the **actual physical completed-secant carrier** has a genuinely stronger exclusion mechanism: for example an infinite-dimensional/non-precompact arithmetic law, an unbounded norm map, a positivity or support boundary that blocks common-background completion, or another intrinsic relation that keeps large paired prime cubes a positive TV distance away.

That is now the falsifiable boundary: if the claimed prime discriminator is protected only by finitely many bounded linear source statistics and their full kernel remains physically completable, the protection is illusory.