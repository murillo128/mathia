# XF-028 — overlapping normalized discriminants make covered collisions positive

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE` + `STRUCTURAL/BOUNDARY`. XF-027 found a scale-free block discriminant whose internal logarithmic-repulsion production is a square and whose far exterior field is affine-cancelled, but a root colliding immediately across a hard block boundary can still drive the block derivative to `-infinity` at order `1/epsilon`. That hard-boundary spike is not the leading singularity once normalized discriminants are overlapped.

Fix a block length `n>=3`. For the consecutive block

\[
I_j=\{j,j+1,\ldots,j+n-1\},
\]

let `\mathcal J_j` be the normalized block discriminant of XF-027,

\[
\mathcal J_j
=
\log\prod_{r<s\in I_j}(x_r-x_s)^2
-
N\log V_j,
\qquad
N=\binom n2,
\]

where `V_j` is the centered quadratic span of the block. For any finitely supported real coefficients `a_j`, define

\[
\mathcal K_{n,a}:=\sum_j a_j\mathcal J_j.
\]

Suppose one adjacent gap

\[
\epsilon=x_{k+1}-x_k\downarrow0
\]

undergoes an isolated two-root collision while all other gaps meeting the finitely many active blocks stay bounded away from zero. Put

\[
\boxed{
W_k:=\sum_{j=k-n+2}^{k}a_j,
}
\]

the total weight of blocks containing **both** colliding roots. Then along the logarithmic zero-motion law,

\[
\boxed{
\mathcal K_{n,a}'
=
\frac{8W_k}{\epsilon^2}
+O\!\left(\frac1\epsilon\right).
}
\]

Thus the sign of the strongest collision singularity is controlled only by pair coverage. In particular, if `W_k>0`, then

\[
\boxed{
\mathcal K_{n,a}'\longrightarrow +\infty
\qquad(\epsilon\downarrow0).
}
\]

For a nonnegative localization taper this requires only that the target collision wall lie inside at least one positively weighted block. With uniform weights, every interior adjacent pair belongs to `n-1` translated `n`-blocks, so the leading term is

\[
\boxed{
\frac{8(n-1)}{\epsilon^2}.
}
\]

The negative `1/epsilon` spike of a block that contains exactly one member of the colliding pair is still present, but it is one order weaker and therefore cannot overturn a positively covered collision. This is a qualitative difference from the smooth quadratic/variance localizations of XF-021--XF-025, whose first non-removable boundary term itself occurs at order `1/epsilon`.

The result does **not** prove that `\mathcal K_{n,a}` is globally monotone, bounded in the direction needed to exclude a collision, or Xi-specific. It removes a narrower obstruction: hard membership boundaries do not force a collision-negative singularity for an overlapped normalized-discriminant localization. The live problem becomes the finite-gap sign of the aggregate flux and the support-edge region where pair coverage vanishes.

## 1. The adjacent gap itself has a universal `4/epsilon` opening law

Work first in a finite real-rooted logarithmic particle system,

\[
x_i'=2\sum_{\ell\ne i}\frac1{x_i-x_\ell},
\tag{1}
\]

and isolate the adjacent pair `x_k<x_{k+1}` with

\[
\epsilon=x_{k+1}-x_k.
\tag{2}
\]

Subtracting the two velocities gives

\[
\begin{aligned}
\epsilon'
&=
\frac4\epsilon
+2\sum_{\ell\ne k,k+1}
\left(
\frac1{x_{k+1}-x_\ell}
-
\frac1{x_k-x_\ell}
\right)\\
&=
\frac4\epsilon
-2\epsilon
\sum_{\ell\ne k,k+1}
\frac1{(x_{k+1}-x_\ell)(x_k-x_\ell)}.
\end{aligned}
\tag{3}
\]

Under the isolated-collision hypothesis the second line is `4/epsilon+O(epsilon)`. Hence

\[
\boxed{
\frac{2\epsilon'}\epsilon
=
\frac8{\epsilon^2}+O(1).
}
\tag{4}
\]

For the Xi zero system the same local coefficient is valid on a real-simple slice with the Rodgers--Tao principal-value convention used in XF-014. The difference in (3) is an inverse-square tail, so the local subtraction is absolutely summable at the Xi zero-location scale. No extension of the ordered zero law through the collision is being assumed.

## 2. A block containing both roots has a positive `8/epsilon^2` singularity

Take one active block `I_j` containing both indices `k` and `k+1`. Because `n>=3` and the collision is isolated, at least one other root in the block remains separated from the pair. Therefore its centered span has a positive limit,

\[
V_j\longrightarrow V_j^*>0.
\tag{5}
\]

The discriminant factors as

\[
\prod_{r<s\in I_j}(x_r-x_s)^2
=
\epsilon^2 D_j,
\tag{6}
\]

where `D_j` extends to a positive smooth function at `epsilon=0`. Consequently

\[
\mathcal J_j
=
2\log\epsilon+R_j,
\tag{7}
\]

where `R_j=\log D_j-N\log V_j` extends smoothly across the collision wall and is symmetric under exchanging `x_k` and `x_{k+1}`.

XF-026 applies exactly to this regular remainder: the singular pair action on `R_j` is removable. All other local denominators stay nonzero, so

\[
R_j'=O(1)
\tag{8}
\]

as `epsilon` tends to zero. Combining (4), (7), and (8),

\[
\boxed{
\mathcal J_j'
=
\frac8{\epsilon^2}+O(1)
}
\tag{9}
\]

for every translated block containing both colliding roots.

This is the mechanism absent from a smooth centered variance. The normalized discriminant deliberately retains the internal logarithmic collision barrier, and its scale normalization does not cancel that barrier once `n>=3` because the rest of the block keeps `V_j` nonzero.

## 3. A block containing only one colliding root is at worst `1/epsilon`

Now take a translated block containing `x_k` but not `x_{k+1}`, or vice versa. There is no internal collision inside that block, so `\mathcal J_j` and its gradient remain finite as `epsilon` tends to zero. The only singularity comes from the velocity of the included root, which contains the omitted partner with size `2/epsilon`.

Using the XF-027 shape gradient

\[
\frac12\nabla\mathcal J_j=q^{(j)},
\tag{10}
\]

the two possible one-sided blocks have the sharper expansions

\[
\mathcal J_{k-n+1}'
=-\frac{4q^{L}_k}{\epsilon}+O(1),
\qquad
\mathcal J_{k+1}'
=\frac{4q^{R}_{k+1}}\epsilon+O(1),
\tag{11}
\]

when those blocks are present. Here `q^L_k` and `q^R_{k+1}` denote the limiting boundary components of the corresponding block shape gradients. Every block containing neither colliding root contributes only `O(1)` to this local singular expansion.

Thus a hard membership edge can still have either sign at order `1/epsilon`, exactly as XF-027 exhibited. The point is not cancellation of that term. The point is that any block containing both roots contributes the stronger positive `8/epsilon^2` term.

## 4. Overlap gives an exact pair-coverage coefficient

Summing (9)--(11) with the coefficients `a_j`, the blocks containing both `k` and `k+1` are precisely

\[
j=k-n+2,\ldots,k.
\tag{12}
\]

Therefore

\[
\begin{aligned}
\mathcal K_{n,a}'
&=
\frac8{\epsilon^2}
\sum_{j=k-n+2}^{k}a_j
+O\!\left(\frac1\epsilon\right)\\
&=
\boxed{
\frac{8W_k}{\epsilon^2}
+O\!\left(\frac1\epsilon\right)}.
\end{aligned}
\tag{13}
\]

This coefficient also appears directly in the static energy. The summed unnormalized discriminants satisfy the exact finite-range pair decomposition

\[
\sum_j a_j\log\Delta_{I_j}^2
=
\sum_{r=1}^{n-1}
\sum_i
w_{i,r}\log(x_{i+r}-x_i)^2,
\tag{14}
\]

where

\[
\boxed{
w_{i,r}:=
\sum_{j=i+r-n+1}^{i}a_j.}
\tag{15}
\]

For the adjacent pair `r=1`, `w_{k,1}=W_k`. Hence `W_k` is not an artifact of differentiating the block formula: it is exactly the multiplicity with which the collapsing Vandermonde factor is covered by the overlapped energy.

The normalized variance terms

\[
-N\sum_j a_j\log V_j
\tag{16}
\]

cannot produce a competing `1/epsilon^2` term in an isolated two-root collision for `n>=3`, because every `V_j` of a block containing both roots has a positive collision limit and is exchange-symmetric there. Their pair singularity is therefore removable in the sense of XF-026.

## 5. Uniform overlap and localized tapers

For the formal translation-invariant choice `a_j=1`, each adjacent pair lies in exactly `n-1` consecutive blocks. Thus

\[
W_k=n-1
\tag{17}
\]

and

\[
\boxed{
\mathcal K_n'
=
\frac{8(n-1)}{\epsilon^2}
+O\!\left(\frac1\epsilon\right).
}
\tag{18}
\]

An infinite unweighted sum of the block energies is not itself the intended Xi observable: local block shapes approach a nonzero background, so the raw sum need not converge. The useful statement is local. Choose a finitely supported or summable **nonnegative** taper `a_j` and place the target core inside a region where

\[
W_k\ge w_*>0.
\tag{19}
\]

Then every isolated adjacent collision in that covered core satisfies

\[
\mathcal K_{n,a}'>0
\tag{20}
\]

once the gap is sufficiently small. Support-edge collisions for which `W_k=0` are not protected by this theorem; there the one-sided `1/epsilon` terms of XF-027 may again dominate.

This separates two localization questions which the hard single block conflated:

- **collision-wall coverage:** solved locally by positive overlap, because an internal log barrier is order `1/epsilon^2`;
- **finite-gap/support-edge flux:** still open and must be controlled by taper design, buffer geometry, or Xi-specific information.

## 6. The case `n=2` is a sharp degeneracy

The restriction `n>=3` is essential. For two roots `x_1,x_2`,

\[
V=\frac{(x_2-x_1)^2}{2},
\qquad
N=1,
\]

so

\[
\mathcal J
=
\log(x_2-x_1)^2
-
\log\frac{(x_2-x_1)^2}{2}
=
\log2.
\tag{21}
\]

The normalized two-root discriminant is identically constant: scale removal cancels the entire collision logarithm. Thus there is no `1/epsilon^2` production to dominate a membership spike. Three roots are the smallest block size that retains nontrivial shape and therefore the smallest block size for which overlap can supply the positive leading collision barrier.

## 7. Relation to the recent Xi-flow obstruction sequence

XF-021--XF-025 showed that smooth mean-removing functionals on fixed ordered-gap windows repeatedly inherit collision-positive or collision-negative `1/epsilon` boundary terms. XF-026 identified those terms as reflection-wall gradient mismatch. XF-027 then escaped the smooth class by using a symmetric logarithmic collision barrier, but a single hard block still had a negative exterior `1/epsilon` spike.

Equation (13) shows that this last spike is **not stable under overlap**. Once the same collision wall is internal to a positively weighted neighboring block, the deliberately singular Vandermonde factor contributes at order `1/epsilon^2`, while the membership defect remains only order `1/epsilon`. In that precise sense, overlapping normalized discriminants cure the leading hard-boundary collision sign without requiring a smooth root-exchange extension of each individual block.

The result is compatible with the other gain of XF-027. Each individual block still annihilates the affine part of its exterior field and sees distant roots only through a cubic multipole tail. A finite weighted aggregate therefore preserves that far-field cancellation blockwise. Combining positive pair coverage in a core with the super-mesoscopic physical buffers of XF-020 leaves a more focused proof obligation: control the finite-gap non-affine flux before the taper reaches a region where `W_k` degenerates.

## 8. Prior-art and novelty boundary

The logarithmic Vandermonde energy, Stieltjes equilibrium, Hermite extremizers, and general one-dimensional log-gas gradient mechanisms are classical and already delimited in `SOURCES.md` and XF-027. A targeted audit of finite-range/local logarithmic interactions and discriminant heat-flow literature did not supply a theorem matching the specific sliding-block coefficient (13).

No external theorem is load-bearing here. Equations (3)--(18) are finite algebra from the Rodgers--Tao root law and the normalized-discriminant identity already persisted in XF-027. Accordingly this finding does not claim a new general log-gas theorem. Its durable content is the exact Mathia-localization statement that **pair coverage, not hard-block membership by itself, determines the leading collision sign of an overlapped normalized-discriminant functional**.

## 9. Consequence for `xi_flow`

The immediate candidate is no longer a single block `\mathcal J_I`, but a nonnegative family of overlapping blocks whose target core has a strict pair-coverage floor `W_k>=w_*>0`. Such a family simultaneously has three properties already established by XF-027 and the present calculation: scale-free shape normalization, blockwise affine cancellation of the far exterior field, and a positive leading singularity at every covered isolated two-root collision.

What remains is substantial. Equation (13) is only a near-collision asymptotic and gives no global sign for `\mathcal K_{n,a}'`; the aggregate itself is not shown coercive in the direction needed for an upper bound on `Lambda`; support-edge walls remain unprotected; and no Xi-specific estimate yet bounds the finite-gap non-affine exterior residual by the internal square production. The next useful step is therefore not another collision-wall patch. It is an exact finite-gap estimate for an overlapped taper, or a counterexample showing that the `O(1/epsilon)` and regular flux can still defeat the summed square production away from the collision asymptotic.