# NB-139 — arbitrary polynomial crowding inherits the target-poor confluent barrier

**Status:** `DERIVED + GROWING-SIMPLE-CLUSTER + TARGET-AWARE-GRASSMANN-CONTROL + ARBITRARY-NODE-GEOMETRY + EXPLICIT-POLYNOMIAL-DIAMETER + MATCHED-ZERO-ENVELOPE-CONTROL + REPRESENTATION-INVARIANT + NEGATIVE/METHOD-BOUNDARY`.

`NB-138` shows that the target-poor confluent packet from `NB-111` is already inherited by an equally spaced simple packet at a fixed polynomial vertical spacing. Equal spacing is convenient for forward differences, but it is not intrinsic to the Nyman state geometry and leaves a possible escape: perhaps irregular simple zeros do not approach the same target-poor state space unless their individual gaps obey a special pattern.

That escape is absent. The relevant small parameter is the **diameter of the whole simple cluster**, not its internal spacing pattern or its minimum gap.

Fix

\[
r\ge 1,\qquad q\ge2,\qquad 0<a<\frac12,
\qquad 0<c<\frac18,
\tag{1}
\]

and put

\[
m_G=\lceil G\rceil,\qquad R_G=m_Gq,
\qquad d_G=\lfloor c\log G\rfloor.
\tag{2}
\]

Retain the analytic one-state family `w_G(h)`, the target `e_G`, and the confluent space

\[
\mathcal S_G^{\rm conf}
=
\operatorname{span}\{w_G^{(j)}(0):0\le j<d_G\}
\tag{3}
\]

from `NB-137`--`NB-138`. Let

\[
h_{0,G},\ldots,h_{d_G-1,G}\in\mathbb R
\tag{4}
\]

be **arbitrary pairwise distinct nodes** satisfying

\[
|h_{j,G}|\le \Delta_G,
\qquad
\Delta_G\longrightarrow0,
\tag{5}
\]

and define the corresponding simple-state space

\[
\mathcal S_G^{\rm split}
:=
\operatorname{span}\{w_G(h_{j,G}):0\le j<d_G\}.
\tag{6}
\]

As in `NB-138`, set

\[
D_a:=1+\frac{4(1-a)}a=\frac4a-3.
\tag{7}
\]

Then the sufficient condition

\[
\boxed{
\Delta_G\,
G^{c\log D_a}
(\log G)^{25/2}
\longrightarrow0
}
\tag{8}
\]

implies

\[
\boxed{
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\longrightarrow0.
}
\tag{9}
\]

In particular, for every fixed

\[
\boxed{B>c\log D_a,}
\tag{10}
\]

**every** pairwise-distinct simple packet contained in the polynomial vertical cell

\[
\boxed{|h_{j,G}|\le G^{-B}}
\tag{11}
\]

inherits the target-poor confluent barrier. No lower bound, regularity, arithmetic progression, or comparability assumption on the internal gaps is used.

If also `c<0.10076`, the formal points

\[
\rho_{j,G}=\frac12+a+i(G+h_{j,G})
\tag{12}
\]

remain compatible with the same coarse right-half zero-count and Vinogradov--Korobov envelopes used in `NB-133`--`NB-138`: those source laws do not exclude a packet of `(c+o(1))\log G` simple right-half points inside a cell of height `O(G^{-B})`. Thus replacing the equally spaced matched control by arbitrary local zero geometry does not rescue target coercivity.

The conclusion is deliberately target-aware. It does **not** assert that the ordinary evaluation matrix must have the same condition number for every internal node pattern. Instead it says something representation-invariant: the whole simple-state span itself remains asymptotically unable to capture the normalized Nyman target.

## 1. Newton divided differences remove all dependence on the minimum gap

For a fixed `G`, abbreviate `d=d_G`, `h_j=h_{j,G}`, and write `[h_0,\ldots,h_j]w_G` for the vector-valued divided difference of the analytic map `h\mapsto w_G(h)`. Define the normalized Newton columns

\[
u_{j,G}
:=
j!\,[h_0,\ldots,h_j]w_G,
\qquad 0\le j<d.
\tag{13}
\]

Because the nodes are pairwise distinct, `u_{j,G}` is a linear combination of

\[
w_G(h_0),\ldots,w_G(h_j)
\]

whose coefficient at `w_G(h_j)` is

\[
\frac{j!}{\prod_{\ell<j}(h_j-h_\ell)}\ne0.
\tag{14}
\]

Hence the Newton transformation is triangular and invertible, regardless of how small the pairwise gaps are. Therefore

\[
\boxed{
\operatorname{span}\{u_{j,G}:0\le j<d\}
=
\mathcal S_G^{\rm split}.
}
\tag{15}
\]

The coefficients in `(14)` may be enormous when nodes nearly collide. That is irrelevant here: `(15)` is an exact identity of subspaces, and the argument below estimates the normalized divided-difference columns directly rather than the inverse Newton matrix.

The Hermite--Genocchi identity follows by repeated use of the fundamental theorem of calculus. With `\nu_j` the probability measure obtained by normalizing Lebesgue measure on the simplex

\[
\Sigma_j
=
\{(t_0,\ldots,t_j):t_\ell\ge0,\ \sum t_\ell=1\},
\tag{16}
\]

one has the Banach-valued formula

\[
\boxed{
u_{j,G}
=
\int_{\Sigma_j}
 w_G^{(j)}\!\left(\sum_{\ell=0}^j t_\ell h_\ell\right)
 d\nu_j(t).
}
\tag{17}
\]

For `j=0`, this simply reads `u_{0,G}=w_G(h_0)`. Formula `(17)` is the arbitrary-node analogue of the cube integral used for the forward differences in `NB-138`.

Every convex combination in `(17)` lies in `[-\Delta_G,\Delta_G]`. The fixed-tube Cauchy estimate already proved in `NB-138` gives, uniformly for real `|h|\le1`,

\[
\|w_G^{(k)}(h)\|_2
\le
C_{a,q,r}\,k!\left(\frac2a\right)^k.
\tag{18}
\]

Applying the fundamental theorem of calculus once more to `w_G^{(j)}` and using `(18)` with `k=j+1` yields

\[
\boxed{
\|u_{j,G}-w_G^{(j)}(0)\|_2
\le
C_{a,q,r}\,
\Delta_G\,(j+1)!
\left(\frac2a\right)^{j+1}.
}
\tag{19}
\]

There is no factor involving the reciprocal of a pairwise node gap. Near-collision is absorbed by divided differences before the subspace is compared.

## 2. Laguerre normalization transfers the whole arbitrary-node span

Use the same Laguerre-normalized confluent columns as `NB-138`:

\[
g_{k,G}
=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 w_G^{(j)}(0),
\qquad 0\le k<d.
\tag{20}
\]

Define their arbitrary-node split analogues by

\[
\widetilde g_{k,G}
:=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 u_{j,G}.
\tag{21}
\]

The transformation from the Newton columns `u_j` to `\widetilde g_k` is triangular with nonzero diagonal. Combining this with `(15)` gives

\[
\boxed{
\operatorname{span}\{\widetilde g_{k,G}:0\le k<d\}
=
\mathcal S_G^{\rm split}.
}
\tag{22}
\]

From `(19)`,

\[
\begin{aligned}
\|\widetilde g_{k,G}-g_{k,G}\|_2
&\le
C_{a,q,r}\Delta_G
\sum_{j=0}^{k}
\binom kj
\frac{(2(1-a))^j}{j!}
(j+1)!
\left(\frac2a\right)^{j+1}\\
&\le
C_{a,q,r}\Delta_G
\sum_{j=0}^{k}
\binom kj
(j+1)
\left(\frac{4(1-a)}a\right)^j.
\end{aligned}
\tag{23}
\]

Writing `X=4(1-a)/a`, the binomial identity

\[
\sum_{j=0}^{k}\binom kj(j+1)X^j
=(1+X)^{k-1}(1+(k+1)X)
\tag{24}
\]

therefore gives

\[
\boxed{
\|\widetilde g_{k,G}-g_{k,G}\|_2
\le
C_{a,q,r}\Delta_G(k+1)D_a^k.
}
\tag{25}
\]

Let

\[
A_G\alpha=\sum_{k<d}\alpha_k g_{k,G},
\qquad
B_G\alpha=\sum_{k<d}\alpha_k\widetilde g_{k,G}.
\tag{26}
\]

A Frobenius estimate from `(25)` gives the operator bound

\[
\boxed{
\|B_G-A_G\|
\le
C_{a,q,r}\Delta_G d^{3/2}D_a^d.
}
\tag{27}
\]

The exponent of `d` is not important. In particular, the slightly stronger hypothesis `(8)` safely absorbs `(27)` and keeps the same polynomial threshold `B>c\log D_a` as `NB-138`.

## 3. Confluent coercivity converts arbitrary-node closeness into a target-angle bound

The Laguerre coercivity theorem of `NB-111`, used in exactly the same coordinates in `NB-138`, gives for `d_G=\lfloor c\log G\rfloor` and `c<1/8`

\[
\boxed{
\sigma_{\min}(A_G)
\gg_{a,q,r,c}
(\log G)^{-10}.
}
\tag{28}
\]

Set

\[
\vartheta_G
:=
C_{a,q,r,c}
\Delta_G d_G^{3/2}D_a^{d_G}(\log G)^{10}.
\tag{29}
\]

Condition `(8)` implies `\vartheta_G\to0`. For every unit vector `y` in `Ran(B_G)`, write `y=B_G\alpha/\|B_G\alpha\|`. Then

\[
\operatorname{dist}(y,\operatorname{Ran}(A_G))
\le
\frac{\|B_G-A_G\|}
{\sigma_{\min}(A_G)-\|B_G-A_G\|}
\le
\frac{\vartheta_G}{1-\vartheta_G}
\tag{30}
\]

for all sufficiently large `G`. Consequently,

\[
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\le
\frac{\|P_{\mathcal S_G^{\rm conf}}e_G\|}
     {\|e_G\|}
+
\frac{\vartheta_G}{1-\vartheta_G}.
\tag{31}
\]

The first term tends to zero by `NB-111`; the second tends to zero by `(8)`. This proves `(9)`.

For the polynomial cell `(11)`,

\[
D_a^{d_G}
=G^{c\log D_a+o(1)},
\tag{32}
\]

so `(29)` gives

\[
\vartheta_G
\ll
G^{-(B-c\log D_a)+o(1)}
(\log G)^{23/2},
\tag{33}
\]

which vanishes whenever `(10)` holds. The displayed hypothesis `(8)` deliberately keeps the slightly looser logarithmic budget of `NB-138`; the power threshold is the substantive feature.

## 4. Matched zero-envelope control survives arbitrary node geometry

Take the formal points `(12)` with `\Delta_G=G^{-B}`. Their total vertical diameter is at most `2G^{-B}=o(1)`. The explicit zero-count estimate already anchored for this line has endpoint error

\[
0.10076\log T+0.24460\log\log T+O(1).
\tag{34}
\]

Applied at the two ends of an `O(G^{-B})` window near `G`, the main-term variation is `o(\log G)` while the two endpoint errors permit

\[
(0.20152+o(1))\log G
\tag{35}
\]

zeros in the whole strip. Functional-equation symmetry pairs every right-half off-critical zero with a left-half one at the same ordinate, so the corresponding right-half allowance is

\[
(0.10076+o(1))\log G.
\tag{36}
\]

Thus every fixed `c<0.10076` remains below what this **coarse source law alone** can exclude. The fixed horizontal location `1/2+a` is also eventually far to the left of the Vinogradov--Korobov zero-free boundary near `1`, so that law does not forbid `(12)` either.

This is only a matched-control statement. It does not claim that zeta actually has such packets. It says that the source information currently imported into this route cannot distinguish them from admissible zero geometry.

The distinction from `NB-138` is material. There the control was an arithmetic progression and one could wonder whether the obstruction was created by the special phase relation needed for forward differences. Here the internal gaps may be wildly nonuniform and arbitrarily smaller than the cell diameter. The target-poor conclusion is controlled by the enclosing cell alone.

## 5. Prior art, information audit, and boundaries

Newton/Hermite divided differences, the Hermite--Genocchi integral representation, and convergence from simple to confluent interpolation are classical. No novelty is claimed for that interpolation machinery. The line-local contribution is the quantitative splice with the exact Nyman state map and the `NB-111` target-angle coercivity: a growing `Theta(log G)` packet of arbitrary simple nodes inside a fixed polynomial cell inherits the same target-poor state geometry.

A literature audit of zeta-zero spacing does not provide the missing source law. Classical and modern gap results control existence or statistics of small/large normalized gaps, often under RH; recent work on simple/distinct zeros in short intervals supplies lower-count information rather than a deterministic lower bound forbidding `Theta(log G)` right-half points in a polynomially shrinking window. None of that is used as an input to the proof above. The only external quantitative source input remains the zero-count and zero-free-region material already anchored in `SOURCES.md`, so no new source anchor is required.

Several boundaries are essential:

- The nodes in `(4)` are simple and pairwise distinct. Repeated nodes lead directly to Hermite/confluent states and therefore do not offer an escape from `NB-111`; the present statement avoids introducing multiplicity notation unnecessarily.
- The theorem concerns a vertically clustered packet at fixed horizontal displacement `a`. It does not prove an analogous result for a packet whose real parts spread with `G`.
- The threshold `B>c\log D_a` is sufficient, not asserted sharp. The constants and logarithmic powers were not optimized.
- Small target projection of this packet does not prove the full Nyman distance is large; other zero packets or other state sectors may remain target-bearing.
- Conversely, terrible conditioning of a chosen power basis is no longer needed for the obstruction. Even if an alternative coordinate system is numerically stable, it spans the same target-poor space.
- The matched formal points are not asserted to be zeta zeros. A genuine source theorem excluding such local occupancy would invalidate the control and would be substantive new arithmetic information.

## 6. Consequence for the live source question

`NB-137` separated ordinary conditioning from target relevance; `NB-138` showed that this separation already occurs at polynomial equal spacing. The present result removes the remaining internal-geometry artifact:

\[
\boxed{
\text{logarithmic-rank simple packet}
+
\text{polynomially shrinking total diameter}
\Longrightarrow
\text{target-poor confluent geometry},
}
\tag{37}
\]

under `(8)`, independently of the pairwise gap pattern.

Therefore a source-side repair cannot consist merely of proving that the zeros are not exactly equally spaced, nor of controlling one particular adjacent gap, nor of stabilizing a preferred Vandermonde chart. What is needed is information that prevents **logarithmic occupancy of a polynomial confluence cell** in the relevant right-half zero packet, or information that directly forces nonvanishing target occupation despite such crowding.

This sharpens the live discriminator from generic `spacing` to **target-bearing local occupancy geometry**. A minimum-spacing theorem strong enough to force at most `o(\log G)` relevant zeros in every cell `(11)` would certainly suffice to break this matched control, but average-gap information or the existence of occasional large gaps does not address the quantified packet in `(9)`.