# PC-259 — common integer dilation is exact direct sum for the shared-upper defect

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the remaining long-cocycle escape after PC-257/PC-258.

Let `a<b` be positive integers and let the overlap packet be the interval matrix used in PC-251,

\[
K_{a,b}(u,t)
=
a\left|[u,u+1)\cap\left[\frac{bt}{a},\frac{b(t+1)}a\right)\right|,
\qquad 0\le u<b,\ 0\le t<a.
\tag{1}
\]

For every integer `m>=1`, the simultaneous dilation `(a,b) -> (ma,mb)` does not create a new overlap packet. After grouping rows and columns into the natural `m` consecutive scale blocks,

\[
\boxed{
K_{ma,mb}=m\,(I_m\otimes K_{a,b}).
}
\tag{2}
\]

Consequently, for the shared-upper defect

\[
D_{p,r;q}:=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T},
\tag{3}
\]

one has the exact all-depth identity

\[
\boxed{
D_{mp,mr;mq}=m^2\,(I_m\otimes D_{p,r;q}).
}
\tag{4}
\]

With the native normalization of PC-251,

\[
\Delta_{p,r;q}:=\frac{D_{p,r;q}}{q\sqrt{pr}},
\tag{5}
\]

the scalar factor cancels completely:

\[
\boxed{
\Delta_{mp,mr;mq}=I_m\otimes\Delta_{p,r;q}.
}
\tag{6}
\]

Thus common refinement does not lengthen the surviving PC-257/PC-258 cocycle in a genuinely new way. It repeats it as `m` independent copies. The complete normalized singular spectrum, characteristic polynomial per block, transfer dynamics per block, and every length-normalized Lyapunov/log-volume quantity are unchanged. Any Prime-Circle mechanism based on the long shared-upper transfer chain must therefore distinguish the primitive quotient rather than count common-refinement repetitions as new long-range information.

## 1. Exact block identity for the overlap packet

Write a column index of `K_{ma,mb}` uniquely as

\[
t=ah+t_0,
\qquad 0\le h<m,
\qquad 0\le t_0<a,
\tag{7}
\]

and a row index as

\[
u=bh'+u_0,
\qquad 0\le h'<m,
\qquad 0\le u_0<b.
\tag{8}
\]

The lower interval attached to column `t` is

\[
\left[\frac{mb(ah+t_0)}{ma},\frac{mb(ah+t_0+1)}{ma}\right)
=
\left[bh+\frac{bt_0}{a},\,bh+\frac{b(t_0+1)}a\right).
\tag{9}
\]

It is contained in the `h`th block `[bh,b(h+1))`. Hence it has zero intersection with every unit row cell belonging to a different block `h'!=h`. For `h'=h`, translation by `bh` reduces the intersection exactly to that of (1), while the prefactor is `ma` instead of `a`. Therefore

\[
K_{ma,mb}(bh+u_0,ah+t_0)
=mK_{a,b}(u_0,t_0),
\tag{10}
\]

with all off-block entries zero. This proves (2) without asymptotics, coprimality, or primality assumptions.

## 2. The complete shared-upper defect repeats blockwise

Apply (2) to the three overlap packets in (3):

\[
K_{mp,mq}=m(I_m\otimes K_{p,q}),
\quad
K_{mr,mq}=m(I_m\otimes K_{r,q}),
\quad
K_{mp,mr}=m(I_m\otimes K_{p,r}).
\tag{11}
\]

Then

\[
\begin{aligned}
D_{mp,mr;mq}
&=K_{mp,mq}^{*}K_{mr,mq}-(mq)K_{mp,mr}^{T}\\
&=m^2 I_m\otimes K_{p,q}^{*}K_{r,q}
   -m^2 q I_m\otimes K_{p,r}^{T}\\
&=m^2(I_m\otimes D_{p,r;q}),
\end{aligned}
\tag{12}
\]

which is (4). Since

\[
(mq)\sqrt{(mp)(mr)}=m^2q\sqrt{pr},
\tag{13}
\]

dividing (4) by the native normalization proves (6).

The result is stronger than a moment or determinant identity: it identifies the entire normalized operator up to the explicit block ordering.

## 3. Spectral and transfer consequences

Let

\[
\mathscr H_{p,r;q}
=
\begin{pmatrix}
0&\Delta_{p,r;q}\\
\Delta_{p,r;q}^{T}&0
\end{pmatrix}
\tag{14}
\]

be the normalized symmetric dilation used to expose the complete singular spectrum in PC-257. Equation (6) gives, after the corresponding block permutation,

\[
\boxed{
\mathscr H_{mp,mr;mq}
\simeq I_m\otimes\mathscr H_{p,r;q}.
}
\tag{15}
\]

Hence every singular value of `Delta_{p,r;q}` occurs exactly `m` times at the dilated level. The normalized empirical spectral measure is identical. If `P(z)` denotes the characteristic polynomial of one normalized block, the dilated characteristic polynomial is `P(z)^m`, apart from the same direct-sum bookkeeping for null spaces.

PC-257 represents the nonzero spectrum by a constant-width transfer recursion along the ordered collision chain. Equation (15) shows what simultaneous common refinement does to that supposedly longer chain: it inserts exact block seams and yields `m` disconnected copies of the original transfer problem. A monodromy over the complete repeated object is consequently a product of identical block monodromies, and any Lyapunov exponent or log-determinant normalized by total length is exactly the base value.

This closes a natural but misleading long-range escape: growth of the raw conductor triple caused only by a common integer dilation is not growth of the intrinsic cocycle complexity.

## 4. Mechanical-word interpretation of the seams

The same conclusion is visible in the PC-258 torus/mechanical-word coding. Replacing `(p,r,q)` by `(mp,mr,mq)` leaves the ratios

\[
\alpha=\frac pq,
\qquad
\beta=\frac rq
\tag{16}
\]

unchanged. The lower partition indicators therefore repeat with the base period `q` in each consecutive upper block. At a block seam both scaled lower partitions have an integer boundary simultaneously. In the collision-coordinate description this is a degenerate endpoint event, and the Dirichlet Green factor

\[
G(x,y)=\min(x,y)-xy
\tag{17}
\]

vanishes at the common endpoint. Thus there is no nonzero collision edge connecting adjacent copies. The torus word may be written `m` times in the raw coordinate, but the source-forced weighted transfer object is the direct sum (15), not one irreducible word of `m` times the dynamical depth.

This gives an exact finite counterpart to PC-258's asymptotic warning that local torus statistics are classical. Here even the complete all-depth object is classicalized under a specific scale-growth operation.

## 5. Prior-art and novelty audit

No novelty is claimed for Kronecker products, direct sums, periodic repetition, or transfer matrices of repeated cells. These are standard constructions in matrix analysis, multirate/polyphase signal processing, and Floquet/periodic transfer theory. PC-245 already records the broader classical multirate/polyphase boundary for the native weighted-cover operators, while PC-257 records the standard bounded-width transfer-matrix setting.

The project-local content is narrower and exact: the particular uniform-overlap packet underlying PC-251 has the scaling law (2), and therefore the **entire surviving normalized PC-251--PC-258 shared-upper spectral/cocycle carrier** obeys the direct-sum identity (6), not merely a low-order moment or local-window limit. This consequence is not an absence-of-literature claim; it follows directly from the interval geometry.

A matched-control warning is essential. The dilated triple `(mp,mr,mq)` has common gcd `m`, so this theorem does not by itself prove that every pairwise-coprime composite control reproduces a prime triple. It proves something different: any invariant of this carrier that is stable under direct-sum repetition cannot regard common refinement depth as prime-specific arithmetic information.

## 6. Boundaries and falsification

The theorem does **not** erase all arithmetic information in the primitive triple. Raw dimensions and spectral multiplicities reveal the repetition factor `m`, and a construction may explicitly quotient by or otherwise use the gcd before forming its observable. Nor does (6) classify couplings between two distinct primitive triples, nonlinear cross-scale operations that connect the blocks, or a mechanism that uses the primitiveness of `(p,r,q)` as an additional source-forced hypothesis.

What it rules out is more precise: no proposed RH mechanism may obtain new information merely because the PC-257 transfer chain becomes longer under the simultaneous replacement

\[
(p,r,q)\mapsto(mp,mr,mq).
\tag{18}
\]

After native normalization the operator has not become more complicated; it has only acquired multiplicity.

The falsification test is finite and exact. Construct the interval-overlap matrices from (1), permute rows and columns into the block coordinates (7)--(8), and check (2). Then build the three-packet defect and verify (4), followed by (6). A single nonzero off-block overlap or a failure of the scalar factors in (10)--(13) falsifies the claim.

## 7. Consequence for the current Prime-Circle frontier

PC-258 left open genuinely long-range transfer information whose observation depth grows with collision rank. PC-259 separates **intrinsic depth growth** from trivial common-refinement growth. The latter is now closed exactly: it produces direct-sum copies and cannot generate a new normalized Lyapunov exponent, spectral shape, or monodromy law.

The live question therefore becomes sharper. A surviving long-cocycle mechanism must vary the primitive rational data themselves, or couple distinct primitive scales in a way not conjugate to direct-sum repetition, and it must still distinguish the cyclotomic source from the classical rational-partition controls already identified in PC-251/PC-258. Common dilation alone cannot supply that distinction.
