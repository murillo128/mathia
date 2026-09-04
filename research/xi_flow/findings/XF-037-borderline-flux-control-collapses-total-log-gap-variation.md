# XF-037 — borderline flux control collapses total log-gap variation

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `SOURCE-SPECIFIC` + `STRUCTURAL/STABILITY`. XF-036 proves that the source-side borderline hypothesis

\[
M V_M=O(1),
\qquad
V_M:=\sum_{k=0}^{2M-3}|\phi_{k+1}-\phi_k|,
\]

combined with translated super-mesoscopic Xi counting forces every gap in the active `2M`-gap block to be uniformly asymptotic to the mean spacing. The same hypotheses force a stronger first-order conclusion that was not extracted there: the **entire logarithmic gap profile has vanishing total variation**.

Let

\[
M=R(T)\log^2T,
\qquad
R(T)\to\infty,
\qquad
R(T)=o(T/\log T),
\]

work in the real-simple regime `Lambda<t<=0`, and write

\[
g_k=x_{j+k+1}(t)-x_{j+k}(t)>0,
\qquad
h_T=\frac{4\pi}{\log T},
\qquad
z_k=\log\frac{g_k}{h_T},
\]

for `0<=k<2M`. Set

\[
d_k=z_{k+1}-z_k=\log\frac{g_{k+1}}{g_k},
\qquad
\phi_k=F'(d_k),
\qquad
0\le k\le2M-2,
\]

where `F` is the normalized triple-discriminant shape function of XF-030/031. If

\[
\boxed{M V_M=O(1),}
\tag{1}
\]

then

\[
\boxed{
D_M:=\sum_{k=0}^{2M-2}|d_k|=o(1).
}
\tag{2}
\]

Equivalently, the discrete total variation of `k -> log(g_k/h_T)` across the whole super-mesoscopic block tends to zero. In particular, for every fixed `epsilon>0`,

\[
\boxed{
\#\{k:M|d_k|\ge\epsilon\}=o(M),
}
\tag{3}
\]

so the `O(1/M)` microscopic contrasts left open by XF-036 can occupy only a vanishing fraction of the block at any fixed rescaled amplitude.

Several useful corollaries follow at the same scale:

\[
\sum_k|\phi_k|=o(1),
\tag{4}
\]

\[
\sum_k\bigl(F(0)-F(d_k)\bigr)=o(1/M),
\tag{5}
\]

and, for the mean-normalized reciprocal gaps `u_k:=h_T/g_k=e^{-z_k}`,

\[
\boxed{
\sum_k|u_{k+1}-u_k|=o(1).
}
\tag{6}
\]

Thus bounded inverse-buffer variation of the triple flux does more than remove macroscopic folds: once the translated Xi count has flattened the zeroth-order gap field, the same flux hypothesis collapses the total first-order shape budget. The surviving obstruction is necessarily sparse or concentrated on sub-super-mesoscopic index sets.

This still does **not** prove `max_k M|d_k|=o(1)`, does not prove the sign of the tapered triple-discriminant derivative, and does not derive (1) from the Xi dynamics. Those remain separate obligations.

## 1. XF-036 supplies the two inputs needed for an interpolation step

Under (1), XF-036 proves

\[
\boxed{
A_M:=\max_{0\le k<2M}|z_k|=o(1)
}
\tag{7}
\]

from translated fixed-fraction Xi counting. Its proof also gives

\[
\boxed{
\max_k|d_k|=O(1/M).
}
\tag{8}
\]

The second ingredient is control of the variation of the contrast sequence itself. Since XF-030 gives

\[
\phi(d)=F'(d),
\qquad
\phi(0)=0,
\qquad
\phi'(0)=F''(0)=-\frac32,
\tag{9}
\]

equation (8) places every `d_k` in an arbitrarily small fixed neighborhood of zero for large `T`. Hence there is a constant `c_0>0`, independent of `M`, such that

\[
|\phi'(d)|\ge c_0
\]

throughout the realized contrast range. The mean-value theorem therefore gives

\[
|d_{k+1}-d_k|
\le c_0^{-1}|\phi_{k+1}-\phi_k|.
\tag{10}
\]

Consequently

\[
\boxed{
B_M:=\sum_{k=0}^{2M-3}|d_{k+1}-d_k|
=O(1/M).
}
\tag{11}
\]

So the problem has become a deterministic discrete interpolation statement: a sequence `z` has uniformly vanishing amplitude, while its first difference `d` has total variation of order at most the inverse interval length. This is enough to make the `ell^1` norm of `d` vanish.

## 2. A block interpolation inequality forces `D_M=o(1)`

The needed estimate is elementary and keeps the scale transparent. Let

\[
N:=2M-1
\]

be the number of contrasts `d_0,...,d_{N-1}`. Fix an integer block length `1<=L<=N` and partition the contrast indices into consecutive blocks of lengths at most `L`.

Consider one such block

\[
d_a,\ldots,d_{a+\ell-1},
\qquad 1\le\ell\le L,
\]

and let its arithmetic mean be

\[
\bar d
=\frac1\ell\sum_{k=a}^{a+\ell-1}d_k
=\frac{z_{a+\ell}-z_a}{\ell}.
\tag{12}
\]

By (7),

\[
\ell|\bar d|
=|z_{a+\ell}-z_a|
\le2A_M.
\tag{13}
\]

Because `bar d` lies between the minimum and maximum of the `d_k` in the block,

\[
\sum_{k=a}^{a+\ell-1}|d_k-\bar d|
\le
\ell\left(\max d_k-\min d_k\right)
\le
L\,\operatorname{TV}_{\rm block}(d).
\tag{14}
\]

Combining (13)--(14),

\[
\sum_{k=a}^{a+\ell-1}|d_k|
\le2A_M+L\,\operatorname{TV}_{\rm block}(d).
\tag{15}
\]

Summing over the blocks yields the deterministic inequality

\[
\boxed{
D_M
\le
2A_M\left\lceil\frac{2M-1}{L}\right\rceil
+L B_M.
}
\tag{16}
\]

Now fix any `delta in (0,1)` and take

\[
L=\lfloor\delta M\rfloor.
\]

For large `M`, the number of blocks is bounded by a constant depending only on `delta`. Equations (7), (11), and (16) give

\[
\limsup_{T\to\infty}D_M
\le C\delta
\tag{17}
\]

for a constant `C` depending only on the bound in (1). Since `delta>0` is arbitrary,

\[
D_M\to0,
\]

which proves (2).

The proof deliberately uses two scales. On each fixed-fraction block, small amplitude of the primitive `z` controls the mean contrast, while the inverse-buffer bound on `TV(d)` controls departures from that mean. Taking the block fraction to zero only after the high-zero limit removes both contributions.

## 3. Rescaled nonlattice contrasts have vanishing density

Equation (3) is immediate from (2). If

\[
E_{M,\epsilon}:=\{k:M|d_k|\ge\epsilon\},
\]

then

\[
D_M
\ge\frac{\epsilon}{M}|E_{M,\epsilon}|,
\]

so

\[
\frac{|E_{M,\epsilon}|}{M}
\le\frac{D_M}{\epsilon}
=o(1).
\tag{18}
\]

This improves the qualitative reading of XF-036. That finding allowed `O(1/M)` contrast oscillations after all gaps had become uniformly lattice-like. Such contrasts may still occur at fixed rescaled amplitude, but they cannot fill a positive fraction of the super-mesoscopic buffer under the same `M V_M=O(1)` hypothesis.

The distinction matters for the XF-031 product rule. A prospective finite-gap obstruction after the source flattening step cannot be a positive-density sea of order-`1/M` slope. It must concentrate its shape mismatch on a sparse set, exploit the long-range `L_w` coupling despite vanishing total contrast, or violate the borderline flux-variation bound itself.

## 4. Flux, shape-deficit, and reciprocal-gap corollaries

By (8), all `d_k` tend uniformly to zero. Hence the Taylor behavior from XF-030 gives constants `C_1,C_2` such that for all realized contrasts at sufficiently large `T`,

\[
|\phi(d_k)|\le C_1|d_k|,
\qquad
0\le F(0)-F(d_k)\le C_2 d_k^2.
\tag{19}
\]

Summing the first inequality and using (2) gives (4). For the second,

\[
\sum_k d_k^2
\le
\left(\max_k|d_k|\right)\sum_k|d_k|
=O(1/M)\,o(1)
=o(1/M),
\tag{20}
\]

which proves (5).

For reciprocal gaps, `u_k=e^{-z_k}` and (7) gives `max|z_k|=o(1)`. The mean-value theorem therefore yields

\[
|u_{k+1}-u_k|
\le e^{A_M}|z_{k+1}-z_k|
=e^{A_M}|d_k|.
\tag{21}
\]

Summing and using (2) proves (6).

These are source-conditioned conclusions, not new monotonicity laws. In particular, (4) does not let one bound the taper term in XF-031 by absolute values through a collision, because the factor `y_i'` can still be singular. XF-028 remains the correct collision-wall input.

## 5. The pointwise `1/M` scale can still survive on a sparse patch

The conclusion cannot in general be strengthened from the present data to

\[
\max_k M|d_k|=o(1).
\tag{22}
\]

Fix `c>0` and choose integers `m=m(M)` with

\[
m\to\infty,
\qquad
m=o(M).
\]

As a deterministic matched control, take a contrast sequence equal to `c/M` on `m` consecutive indices and zero elsewhere. Its primitive `z` changes by only

\[
\frac{cm}{M}=o(1),
\]

so after an `o(1)` common normalization all gaps satisfy the zeroth-order source flattening and every fixed-fraction translated average differs from the common mean by `o(1)`. The contrast variation has only the two edge jumps,

\[
B_M=O(1/M),
\qquad
V_M=O(1/M),
\]

while

\[
M\max_k|d_k|=c.
\tag{23}
\]

At the same time

\[
D_M=\frac{cm}{M}=o(1),
\]

exactly as (2) requires. Thus the new theorem rules out macroscopic or positive-density borderline slopes but deliberately leaves **sub-super-mesoscopic microfolds**. This example is not claimed to be an actual Xi zero block or a trajectory of the logarithmic-particle flow; it is a sharpness control for what translated relative-error-zero counting plus (1) can force statically.

The same example also shows why `D_M=o(1)` is not merely a restatement of uniform gap flattening. A uniformly `o(1)` profile can oscillate with large total variation if no control like (11) is present; the borderline flux variation is what prevents repeated small-amplitude oscillation from accumulating order-one or larger total shape.

## 6. Prior-art and novelty boundary

Interpolation inequalities relating a sequence, its first differences, and higher differences are classical; the discrete Landau--Kolmogorov/difference-inequality literature is a broad neighboring framework for (16). A targeted literature check found that general class but no external theorem is needed here: (12)--(17) are a direct finite-block proof, and no claim of novelty is made for the abstract interpolation principle.

The only external load-bearing input is still the Rodgers--Tao zero-counting law already anchored in `research/xi_flow/SOURCES.md` and specialized to translated super-mesoscopic windows in XF-020/036. The flux law and its local invertibility come from the exact internal algebra of XF-030/031/035. No `SOURCES.md` change is required.

The durable line-specific content is the scale coupling: **translated Xi counting converts the borderline bound `M V_M=O(1)` into vanishing `ell^1` logarithmic contrast and hence a vanishing-density theorem for order-`1/M` nonlattice slopes.** This is stronger than the zeroth-order uniform flattening in XF-036 while respecting its stated pointwise boundary.

## 7. Consequence for `xi_flow`

The constructive gate remains the one isolated by XF-036: derive `V_M=O(1/M)` (or a comparable compactness estimate) from the exact XF-031 interaction between `L_lambda` and the long-range cross-ratio operator `L_w`, while retaining XF-028 collision coverage. The present result says what becomes available once that gate is crossed: not only are all gaps uniformly close to `h_T`, but the entire shape profile has vanishing total logarithmic variation, the triple flux has vanishing `ell^1` mass, and order-`1/M` contrasts have zero asymptotic density.

Therefore a negative continuation should no longer use a macroscopic fold or a positive-density near-lattice wave once (1) is assumed. A genuine residual obstruction must be sparse/sub-super-mesoscopic, exploit the nonlocality of `L_w`, concentrate near transition/collision structures in a way compatible with XF-028, or show that the dynamics cannot supply the borderline variation bound in the first place. This narrows the accepted overlap-discriminant taper clue without resolving it: the decisive signed/coercive comparison between `L_lambda h` and `L_w h` is still missing.