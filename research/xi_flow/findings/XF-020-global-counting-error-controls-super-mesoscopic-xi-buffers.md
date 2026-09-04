# XF-020 — global counting error controls super-mesoscopic Xi buffers

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `STRUCTURAL/BOUNDARY`. XF-019 identified an exact geometric requirement for the collision-safe uncentered localization: if a mesoscopic core has physical span `S`, then making its aggregate cross-ratio interaction with the far exterior `o(1)` requires a buffer `D` with `D/S\to\infty`. The first version of XF-019 treated Rodgers--Tao's bounded-`\alpha` local counting theorem as the available source scale and therefore diagnosed the required super-mesoscopic buffer as missing.

That diagnosis was too pessimistic. Rodgers--Tao's **global** Riemann--von Mangoldt estimate for `H_t` has absolute error `O(\log^2 T)`. Subtracting it over a window of length `D` gives

\[
\boxed{
N_t([T,T+D])
=
\frac{D}{4\pi}\log\frac{T}{4\pi}
+O\!\left(\log^2T+\frac{D^2}{T}\right)
}
\]

for `0<D\le T/2` in the hypothetical real-simple regime `\Lambda<t\le0`. Therefore any

\[
D=R(T)\log T,
\qquad R(T)\to\infty,
\qquad R(T)=o(T/\log T),
\]

has the asymptotic count

\[
\boxed{
N_t([T,T+R(T)\log T])
=
\frac{R(T)\log^2T}{4\pi}(1+o(1)).
}
\]

Thus the source package already provides buffers whose physical width exceeds the fixed-time Xi core `S\asymp\log T` by a diverging factor. Combined with XF-019, this makes the aggregate far-exterior cross-ratio leakage `o(1)`. The remaining localization obstruction is **not** lack of source-valid spatial room; it is the near-buffer/mean-removal flux left by XF-018.

## 1. Source input: the global count

Rodgers--Tao define

\[
\Psi(T)
:=
\frac{T}{4\pi}\log\frac{T}{4\pi}
-
\frac{T}{4\pi},
\tag{1}
\]

so that

\[
\Psi'(T)=\frac1{4\pi}\log\frac{T}{4\pi},
\qquad
\Psi''(T)=\frac1{4\pi T}.
\tag{2}
\]

Their global zero-counting theorem in the regime `\Lambda<t\le0` gives

\[
\boxed{
N_t([0,T])=\Psi(T)+O(\log_+^2 T).
}
\tag{3}
\]

The same theorem also supplies the sharper local law on `[T,T+\alpha\log T]` for bounded `\alpha`. That local result is indispensable at the scale `D\asymp\log T`: the error in (3) is itself `O(\log^2T)`, the same size as the main term on such a window.

For the present problem the scale is deliberately larger. Once `D/\log T\to\infty`, the global error in (3) becomes lower order after subtraction. This is the key source distinction missed in the earlier XF-019 diagnosis.

Rodgers--Tao's notation convention states that their un-subscripted implied constants are absolute except for permitted dependence on `\Lambda`. Thus no additional dependence on the particular `t` is introduced into (3) within the stated real-simple regime. The finding needs only that source-level uniformity; it does not extrapolate the ordered zero dynamics beyond `t>\Lambda`.

## 2. Subtracting the global formula

For `0<D\le T/2`, subtract (3) at the two endpoints:

\[
N_t([T,T+D])
=
\Psi(T+D)-\Psi(T)+O(\log^2T).
\tag{4}
\]

Any endpoint-counting convention changes the left side by at most a bounded amount, which is absorbed by the displayed error.

Taylor's theorem and (2) give

\[
\Psi(T+D)-\Psi(T)
=
D\Psi'(T)+O\left(D^2\sup_{u\in[T,T+D]}|\Psi''(u)|\right),
\]

hence

\[
\Psi(T+D)-\Psi(T)
=
\frac{D}{4\pi}\log\frac{T}{4\pi}
+O\left(\frac{D^2}{T}\right).
\tag{5}
\]

Combining (4) and (5) yields the long-window estimate

\[
\boxed{
N_t([T,T+D])
=
\frac{D}{4\pi}\log\frac{T}{4\pi}
+O\!\left(\log^2T+\frac{D^2}{T}\right).
}
\tag{6}
\]

No new analytic number theory enters (6): it is an elementary consequence of the source theorem. Its value for this line is that it exposes a second useful resolution regime that is easy to miss when reading only the local corollary.

## 3. The super-mesoscopic regime has vanishing relative error

Set

\[
D=R(T)\log T
\tag{7}
\]

with

\[
R(T)\to\infty,
\qquad
R(T)=o(T/\log T).
\tag{8}
\]

Then `D=o(T)`, so the restriction `D\le T/2` holds eventually. The main term in (6) is of order `R(T)\log^2T`. Relative to it, the three harmless discrepancies have sizes

\[
O\left(\frac1{R(T)}\right),
\qquad
O\left(\frac1{\log T}\right),
\qquad
O\left(\frac{R(T)}{T}\right),
\tag{9}
\]

coming respectively from the global `O(\log^2T)` remainder, replacing `\log(T/4\pi)` by `\log T`, and the curvature term `D^2/T`. All tend to zero. Therefore

\[
\boxed{
N_t([T,T+R(T)\log T])
=
\frac{R(T)\log^2T}{4\pi}(1+o(1)).
}
\tag{10}
\]

The important point is conceptual: **the coarse global theorem improves relative to the signal as the window gets larger**. At bounded multiples of `\log T` it is too imprecise, which is why Rodgers--Tao prove the finer local theorem. At a diverging multiple of `\log T`, the same absolute error is exactly what makes the required buffer source-valid.

No diagonal compactness argument in the bounded-`\alpha` local theorem is needed. In particular, this finding does not claim that the local theorem itself is uniform for an arbitrary prescribed `\alpha(T)\to\infty`; it uses the separate global formula (3).

## 4. Equivalent super-mesoscopic index spacing

The same estimate can be inverted on a zero block. Suppose `x_j(t)\asymp T` and let

\[
M=M(T)=R(T)\log^2T,
\qquad
R(T)\to\infty,
\qquad
R(T)=o(T/\log T).
\tag{11}
\]

For any fixed `\varepsilon>0`, apply (10) to the two window lengths

\[
D_\pm
=(4\pi\pm\varepsilon)\frac{M}{\log T}.
\tag{12}
\]

Their counts are respectively `(1\pm\varepsilon/(4\pi)+o(1))M`. For large `T`, monotonicity of the counting function therefore squeezes the `M`-gap span between `D_-` and `D_+`, up to harmless endpoint indexing. Letting `\varepsilon\downarrow0` gives

\[
\boxed{
x_{j+M}(t)-x_j(t)
=
\frac{4\pi M}{\log T}(1+o(1)).
}
\tag{13}
\]

This is not a replacement for the finer Rodgers--Tao local spacing theorem. It covers a complementary range: once the number of gaps is a diverging multiple of `\log^2T`, the global counting remainder is already small relative to the block size.

## 5. The XF-019 far exterior is therefore source-compatible

XF-007 fixes the perturbative order-one heat-memory core at

\[
N_T\asymp\log^2T
\]

gaps, hence physical span

\[
S_T\asymp\log T.
\tag{14}
\]

XF-019 proves that if a buffer of width `D` separates this core from the uncontrolled far exterior, then the total uncentered cross-ratio weight across both tails is at most

\[
2\log\left(1+\frac{S_T}{D}\right).
\tag{15}
\]

Choose

\[
D=R(T)\log T
\]

with `R(T)` satisfying (8). Then (10) certifies that this buffer contains the expected `\asymp R(T)\log^2T` real zeros in the allowed regime, while (15) gives

\[
\boxed{
2\log\left(1+\frac{S_T}{D}\right)
=O\left(\frac1{R(T)}\right)
=o(1).
}
\tag{16}
\]

So the far-tail problem identified in XF-019 is geometrically and source-scale compatible: no new pointwise gap envelope and no stronger zero-counting theorem is required merely to push the **far exterior** below the leading scale.

## 6. What remains open

Equation (16) does not close a localized Xi-flow Lyapunov. XF-018's collision-safe carrier is the uncentered gap square, and the neutral constant-gap mode is removed only after subtracting a block-span term. Differentiating that span introduces endpoint velocities. Meanwhile XF-019's cross-ratio estimate begins only beyond the buffer; it does not dispose of interactions between the core and the buffer itself.

The remaining source-facing task is therefore to control or reorganize the **near-buffer and endpoint flux** without reverting to the singular centered coefficient `c_{ik}(g_i-h)(g_k-h)`. Plausible mathematical organizations include overlapping-block cancellation or a signed flux identity, but no such mechanism is asserted here. The matched-control requirement also remains: any eventual monotonicity must distinguish Xi from synthetic log-repulsion systems with the same local diffusion.

This is a meaningful narrowing. The obstruction has moved from “we do not have enough spatial scale” to “we have enough spatial scale, but not yet the right flux organization.”

## 7. Stress tests and boundaries

The argument uses Rodgers--Tao only in the regime where their zero counting and the ordered real-simple zero picture are available. It does not cross `t=\Lambda`, and it does not assume RH at `t=0` to label a hypothetical configuration below the real-rootedness threshold.

The condition `D=o(T)` is substantive for the Taylor form (6). The stated `R(T)=o(T/\log T)` is a convenient sufficient condition and leaves an enormous range of slowly or moderately diverging buffer factors. Nothing here claims useful control for windows comparable to the height itself.

The count controls aggregate density and physical span. It does not bound individual gaps, the conductances `c_{ik}`, endpoint velocities, or signed localized fluxes. Those would be materially stronger statements and are not smuggled in through (10).

Finally, the scale mechanism is not Xi-specific. Any matched real-zero heat flow with the same global density estimate could inherit the same buffer availability. The result removes an obstruction; it is not a selector and does not by itself upper-bound `\Lambda`.

## 8. Prior art and novelty boundary

Rodgers and Tao, **The de Bruijn--Newman constant is non-negative**, *Forum of Mathematics, Pi* 8 (2020), e6, are the primary source for (3), for the function `\Psi`, and for the neighboring bounded-`\alpha` local count. Their paper is already anchored in `research/xi_flow/SOURCES.md`.

No novelty is claimed for subtracting two Riemann--von Mangoldt estimates, Taylor expanding `\Psi`, or converting a count asymptotic into a spacing asymptotic. Those are elementary consequences of established source material.

The durable Mathia contribution is the **scale diagnosis inside the Xi-flow localization program**: the `O(\log^2T)` global error that is too coarse on the fixed-time core becomes relatively negligible on precisely the diverging `R(T)\log T` buffer required by XF-019. This corrects the previous source-boundary statement and removes super-mesoscopic buffer availability from the list of outstanding obstructions.

## 9. Consequence for `xi_flow`

The broad-buffer branch should not spend further effort trying to extend the bounded-`\alpha` local zero-counting theorem merely to obtain `D/\log T\to\infty`. That scale is already available from the global count.

The next sharp test is whether the uncentered identity of XF-018 admits a block or multiblock renormalization in which the neutral span term and the core-to-buffer interaction reduce to signed boundary fluxes that cancel or can be bounded using existing aggregate zero information. A positive result there would combine with (16) to remove the far exterior automatically; a negative result would identify the remaining barrier at the correct level, namely **mean removal and near-buffer flux rather than zero-counting scale**.