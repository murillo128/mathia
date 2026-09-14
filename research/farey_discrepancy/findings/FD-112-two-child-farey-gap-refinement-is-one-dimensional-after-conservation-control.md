# FD-112 — two-child Farey gap refinement is one-dimensional after conservation control

**Status:** `EXACT-DERIVED + FAREY-MEDIANT-REFINEMENT + CONSERVATION-QUOTIENT + ONE-DIMENSIONAL-SHAPE + ZERO-CONTROLLED-PLUCKER + NEGATIVE/ROUTE-RESTRICTION`.

`FD-111` leaves refinement observables with a genuinely nonzero exterior defect as one of the remaining ways to escape the fixed finite local physical-source algebra. `CLUE-ordered-plucker-refinement-transfer.md` proposes precisely such a controlled two-level Plücker carrier. Before introducing richer discrepancy, harmonic, or ancestry coordinates, there is a canonical minimal refinement vector to test: the two child gaps created when a Farey mediant splits one parent gap, with the parent total treated as the nuisance scale.

That minimal carrier is exactly one-dimensional after the conservation control. Let

\[
\frac ab<\frac cd
\]

be Farey neighbors, so `bc-ad=1`, and let

\[
q=b+d,
\qquad
m=\frac{a+c}{b+d}
\tag{1}
\]

be the mediant inserted when the order first reaches `q`. Write the parent gap as

\[
G:=\frac cd-\frac ab=\frac1{bd}
\tag{2}
\]

and the ordered child-gap vector as

\[
g:=\left(m-\frac ab,\frac cd-m\right).
\tag{3}
\]

Then exactly

\[
\boxed{
g=G\left(\frac dq,\frac bq\right).}
\tag{4}
\]

If

\[
s:=\frac{d-b}{b+d}=\frac{d-b}{q},
\qquad
e:=(1,1),
\qquad
f:=(1,-1),
\tag{5}
\]

then the scale-free child shape is

\[
\boxed{
\frac gG
=\frac12e+\frac{s}{2}f.}
\tag{6}
\]

Thus the affine shape space of every two-child Farey split is the single line `x_1+x_2=1`. Removing the conserved parent-total coordinate leaves the one-dimensional space `span(f)`. With the canonical centered control

\[
u:=\frac gG-\frac12e=\frac{s}{2}f,
\tag{7}
\]

we therefore have, for **every pair of refinement events** `i,j`, at the same or different Farey orders,

\[
\boxed{\det(u_i,u_j)=0.}
\tag{8}
\]

The raw two-child determinant can be nonzero only because the affine line does not pass through the origin. In fact it contains no irreducible two-form information:

\[
\boxed{
\det\!\left(\frac{g_i}{G_i},\frac{g_j}{G_j}\right)
=\frac{s_i-s_j}{2},}
\tag{9}
\]

and hence

\[
\boxed{
\det(g_i,g_j)
=\frac{G_iG_j}{2}(s_i-s_j).}
\tag{10}
\]

After the known parent scales `G_i,G_j` are removed, the full local exterior field is only a first difference of the single scalar split imbalance `s`. The numerators `a,c` disappear completely. Therefore a nonzero Plücker carrier at the current Farey frontier cannot be obtained merely by taking exterior minors of the two Euclidean child gaps of each mediant split, even after normalizing their parent size. It must retain at least one additional independent residual coordinate, or couple different ancestry/horizon data before the conservation quotient is taken.

## 1. Exact derivation

The Farey-neighbor identity gives

\[
bc-ad=1.
\tag{11}
\]

Using `q=b+d`, the left child gap is

\[
\begin{aligned}
m-\frac ab
&=\frac{a+c}{q}-\frac ab\\
&=\frac{b(a+c)-a(b+d)}{bq}\\
&=\frac{bc-ad}{bq}
=\frac1{bq},
\end{aligned}
\tag{12}
\]

while the right child gap is

\[
\begin{aligned}
\frac cd-m
&=\frac cd-\frac{a+c}{q}\\
&=\frac{c(b+d)-d(a+c)}{dq}\\
&=\frac{bc-ad}{dq}
=\frac1{dq}.
\end{aligned}
\tag{13}
\]

Their sum is

\[
\frac1{bq}+\frac1{dq}
=\frac{b+d}{bdq}
=\frac1{bd}=G,
\tag{14}
\]

so division by `G` proves (4). Since

\[
\frac dq=\frac{1+s}{2},
\qquad
\frac bq=\frac{1-s}{2},
\tag{15}
\]

we obtain (6)--(8). Finally, for normalized vectors

\[
x_i=\left(\frac{1+s_i}{2},\frac{1-s_i}{2}\right),
\]

a direct determinant gives

\[
\det(x_i,x_j)=\frac{s_i-s_j}{2},
\tag{16}
\]

which proves (9)--(10).

For the refinement `F_(q-1) -> F_q`, every newly inserted reduced fraction of denominator `q` is the mediant of the two neighbors that bracketed it before insertion, with their denominators summing to `q`. Thus the calculation applies event-by-event to the entire exact Farey refinement, not merely to an isolated Stern--Brocot example.

## 2. Representation kill test and matched controls

The representation issue is more important than the determinant identity itself. The observable `g/G` has two displayed coordinates, but conservation fixes their sum. Its genuine shape dimension is therefore one. A linear control that removes parent total must land in `ker(x_1+x_2)`, which is one-dimensional, so **every alternating bilinear form on the controlled local shape vanishes identically**. Equation (8) is coordinate-free content, not a consequence of choosing the symmetric center `(1/2,1/2)` in a lucky basis.

Equation (9) explains a possible false positive. If the affine vectors `g/G` are wedged without centering, a nonzero determinant can appear. But that value is exactly a difference of the scalar imbalance `s`; no second local degree of freedom has been discovered. Likewise, a nonlinear feature map such as `s -> (s,s^2)` can manufacture nonzero determinants, but the resulting vector remains reconstructible from `s` and therefore does not constitute an independent information carrier. A future refinement-Plücker proposal has to show where a second independent residual coordinate enters before interpreting nonzero minors geometrically.

A finite exact sanity check gives the expected extremes. The unique `q=2` insertion has `b=d=1`, hence `s=0` and equal children. At `q=6`, the insertions `1/6` and `5/6` have denominator pairs `(1,5)` and `(5,1)`, so `s=2/3` and `s=-2/3`; their centered vectors are opposite and still have zero determinant. Their raw normalized determinant is nonzero, but (9) shows it is only the scalar difference `2/3-(-2/3)` divided by two.

## 3. Relation to the existing Plücker frontier

This is distinct from `FD-011`. There the vectors are raw homogeneous numerator-denominator increments along one Farey order; their fixed-lag minors collapse to the Hall--Shiu/Haynes Farey-index algebra. Here the vectors are the **two child interval lengths of an actual mediant refinement event**, and the obstruction is even earlier: after quotienting the conserved parent length there is only one local shape degree of freedom on which an exterior two-form could act.

It is also distinct from `FD-109`, where the prime-direction cube of the physical harmonic source coefficients has tensor rank one, and from `FD-111`, which classifies finite local polynomial nonlinearities of those source coefficients. The present rank-one statement is geometric and Farey-specific; no physical-source coefficient law is used.

The finding does **not** resolve `CLUE-ordered-plucker-refinement-transfer.md`. That clue deliberately allows controlled refinement vectors containing denominator bands, discrepancy modes, harmonic features, or ancestry information. What is closed is its minimal two-child-gap instantiation. Any surviving version must retain at least two independent coordinates *after* all predeclared nuisance controls. In practical terms, merely adding more notation around left/right child gaps cannot satisfy that requirement; the extra coordinate has to come from genuinely different information such as cross-level ancestry, a source/discrepancy residual, or a multi-cell packet.

This also sharpens the matched-control requirement. Since `s=(d-b)/(d+b)` is already a complete coordinate for the normalized local split, preserving its ordered sequence preserves every statistic of the two-child geometry. A claimed local two-gap Plücker effect that survives only because a control changes `s` has not isolated an exterior phenomenon; it has changed the underlying scalar split process.

## 4. Prior-art audit and evidence boundary

The ingredients `bc-ad=1`, mediant insertion `(a+c)/(b+d)`, and the child-gap formulas are classical Farey/Stern--Brocot geometry. A target-specific literature search located the standard mediant/refinement description and neighboring Farey-map formulations; for example, Singerman--Strudwick's *The Farey Maps Modulo N* (arXiv:1803.08851) uses the classical triangle with vertices `a/c`, `(a+b)/(c+d)`, `b/d`, while standard continued-fraction references record the mediant gap `1/(Q_n(Q_n+Q_(n+1)))`. No novelty is claimed for any of those identities.

The local Mathia audit found no earlier finding that states the present conservation-quotient classification. `FD-011` kills homogeneous-increment Plücker minors by reduction to Farey-index algebra, `FD-013` shows first-order gap-order data are not coercive for cumulative discrepancy, and `FD-109` kills raw prime-source Plücker curvature. None says that the normalized two-child mediant split has only one residual shape degree and that its raw wedge is exactly the first difference (9). No external theorem is load-bearing for the proof, so `SOURCES.md` requires no change.

The conclusion is deliberately negative and local. It gives no estimate for Franel--Landau discrepancy, Möbius cancellation, spectral allocation, or RH. It does not say that the scalar imbalance sequence `s` is information-free, nor that a richer ancestry/refinement vector cannot have nonzero exterior curvature. It says only that **two child-gap coordinates, once their conserved parent size is removed, cannot by themselves support the genuinely two-dimensional controlled Plücker carrier sought at the current frontier.**