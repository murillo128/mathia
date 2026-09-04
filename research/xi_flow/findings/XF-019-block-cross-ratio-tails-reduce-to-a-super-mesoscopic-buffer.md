# XF-019 — block cross-ratio tails reduce to a super-mesoscopic buffer requirement

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `STRUCTURAL/BOUNDARY`. XF-018 replaced the singular centered leakage coefficient by the collision-safe weight

\[
w_{ik}=c_{ik}g_i g_k=1-e^{-\ell_{ik}}\le \ell_{ik},
\]

where for nonadjacent gap intervals `I_i=(x_i,x_{i+1})`, `I_k=(x_k,x_{k+1})`,

\[
\ell_{ik}=\int_{I_i}\int_{I_k}\frac{dy\,dx}{(y-x)^2}
\]

is the logarithm of their cross-ratio. Its row-wise tail bound still contained the endpoint gap `g_i`, so a single abnormally large gap could prevent decay. Summing **over a whole contiguous core** removes that pointwise dependence completely: the entire far-tail mass is bounded by one cross-ratio of the core and buffer endpoints.

For a core of physical span `S` separated from the exterior by a physical buffer of width `D`, the right-tail weight is at most

\[
\boxed{\log(1+S/D)}.
\]

Thus no pointwise upper or lower gap bound is needed to control the aggregate far exterior. To make that leakage `o(1)` uniformly by this mechanism one needs `D/S\to\infty`. XF-020 corrects the source comparison in the original version of this finding: Rodgers--Tao's global zero-counting formula already supplies such super-mesoscopic buffers after subtraction. The exact geometric reduction here remains valid, but **availability of a diverging physical scale ratio is not itself the remaining Xi obstruction**.

The surviving problem is more local. The block estimate controls only interactions with the exterior beyond the buffer; it does not control the near-buffer part of the localized dynamics, nor the neutral mean/span mode exposed in XF-018. Those are now the source-facing obligations.

## 1. Exact aggregation over two contiguous blocks

Work on any ordered real-simple slice of the Xi flow for which XF-014 and XF-018 apply. Let

\[
A=[a,b],\qquad K=[c,d],\qquad c\ge b+2,
\]

be two finite contiguous blocks of gap indices. Their physical unions are

\[
U_A=(x_a,x_{b+1}),\qquad U_K=(x_c,x_{d+1}).
\]

Every pair `(i,k)\in A\times K` is nonadjacent, so XF-018 gives

\[
w_{ik}\le \ell_{ik}
=\int_{I_i}\int_{I_k}\frac{dy\,dx}{(y-x)^2}.
\tag{1}
\]

Because the gap intervals tile their block unions up to endpoints of measure zero,

\[
\sum_{i=a}^b\sum_{k=c}^d \ell_{ik}
=
\int_{x_a}^{x_{b+1}}
\int_{x_c}^{x_{d+1}}
\frac{dy\,dx}{(y-x)^2}.
\tag{2}
\]

Writing

\[
A_0=x_a,\quad B_0=x_{b+1},\quad C_0=x_c,\quad D_0=x_{d+1},
\]

with `A_0<B_0<C_0<D_0`, direct integration gives

\[
\begin{aligned}
\int_{A_0}^{B_0}\int_{C_0}^{D_0}\frac{dy\,dx}{(y-x)^2}
&=
\int_{A_0}^{B_0}
\left(\frac1{C_0-x}-\frac1{D_0-x}\right)dx\\
&=\log\frac{(C_0-A_0)(D_0-B_0)}{(C_0-B_0)(D_0-A_0)}.
\end{aligned}
\tag{3}
\]

Hence

\[
\boxed{
\sum_{i=a}^b\sum_{k=c}^d w_{ik}
\le
\log\frac{(x_c-x_a)(x_{d+1}-x_{b+1})}
{(x_c-x_{b+1})(x_{d+1}-x_a)}.
}
\tag{4}
\]

The right side is the logarithm of the cross-ratio of the four block endpoints. Thus the cellwise projective kernel of XF-018 is stable under contiguous aggregation: microscopic gap ratios disappear from the upper bound and only the geometry of the two macroscopic intervals remains.

Equation (4) is an inequality rather than an equality only because `w_{ik}=1-e^{-\ell_{ik}}\le\ell_{ik}` was used before summing. The logarithmic kernel itself aggregates exactly.

## 2. Half-line tails depend only on core span and buffer width

Let the right block extend to infinity. Since the positive zeros are unbounded, letting `d\to\infty` in (4) gives

\[
\boxed{
\sum_{i=a}^b\sum_{k\ge c} w_{ik}
\le
\log\frac{x_c-x_a}{x_c-x_{b+1}}.
}
\tag{5}
\]

Set

\[
S:=x_{b+1}-x_a,
\qquad
D_+:=x_c-x_{b+1}>0.
\tag{6}
\]

Then

\[
\boxed{
\sum_{i=a}^b\sum_{k\ge c} w_{ik}
\le
\log\left(1+\frac{S}{D_+}\right).
}
\tag{7}
\]

The left tail is identical. If `e\le a-2` and

\[
D_-:=x_a-x_{e+1},
\]

then

\[
\boxed{
\sum_{i=a}^b\sum_{k\le e} w_{ki}
\le
\log\left(1+\frac{S}{D_-}\right).
}
\tag{8}
\]

Therefore, if a core of span `S` has been insulated on both sides by physical buffers satisfying

\[
D_\pm\ge R S,
\tag{9}
\]

its total interaction with the exterior beyond those buffers obeys

\[
\boxed{
\sum_{i\in A}\sum_{k\in \mathrm{far\ exterior}} w_{ik}
\le
2\log(1+R^{-1})
\le \frac{2}{R}.
}
\tag{10}
\]

This is uniform over every ordered positive gap configuration. No lower-gap envelope, upper-gap envelope, lattice approximation, or control of individual ratios `g_i/g_{i\pm1}` enters.

## 3. Why this is stronger than the row-wise tail in XF-018

XF-018 obtained, for one fixed gap,

\[
\sum_{k\ge i+L}w_{ik}
\le
\log\left(1+\frac{g_i}{x_{i+L}-x_{i+1}}\right).
\tag{11}
\]

A large endpoint gap can make (11) order one even when many indices separate the two regions. Summing (11) crudely over `i` would retain precisely the pointwise large-gap problem highlighted there.

Equations (7)--(8) do something different. They sum the logarithmic cell interactions **before** estimating them. Contiguous gap intervals then tile one physical interval, so all interior endpoints cancel at the integral level. The numerator becomes the total core span `S`, not a sum of uncontrolled pointwise ratios.

The resulting geometric condition is sharp in scale. If `D_+=R S` with fixed `R`, the right side of (7) is the nonzero constant `log(1+1/R)`. To force the aggregate far-tail mass to vanish uniformly by this mechanism alone one needs

\[
\boxed{D_+/S\to\infty}
\tag{12}
\]

and similarly on the left. A fixed-ratio buffer cannot supply a small parameter.

On an arithmetic lattice this requirement is visible directly: `w_{ik}=1/(i-k)^2`, and the interaction of a block of `N` sites with a tail beginning `RN` sites away approaches the same scale-free logarithmic profile. Thus the conclusion is not an artifact of irregular gaps.

## 4. The source-valid Xi scale is broader than the local corollary suggests

XF-007 identified the fixed-heat-time memory scale near local equilibrium as

\[
N_T\asymp \log^2 T
\]

gaps, corresponding to physical core length

\[
S_T\asymp \log T.
\tag{13}
\]

Rodgers--Tao also prove a precise local counting theorem on intervals `[T,T+\alpha\log T]` uniformly for bounded `\alpha`, together with the corresponding `O(\log^2T)`-gap spacing corollary. Read in isolation, that local statement does not permit `\alpha=\alpha(T)\to\infty`.

However, their **global** counting estimate is stronger for the present super-mesoscopic purpose. In their notation,

\[
N_t([0,T])=\Psi(T)+O(\log^2T),
\qquad
\Psi(T)=\frac{T}{4\pi}\log\frac{T}{4\pi}-\frac{T}{4\pi},
\tag{14}
\]

throughout the hypothetical real-simple regime. Subtracting (14) at `T+D` and `T` gives, for `0<D\le T/2`,

\[
N_t([T,T+D])
=
\frac{D}{4\pi}\log\frac{T}{4\pi}
+O\left(\log^2T+\frac{D^2}{T}\right).
\tag{15}
\]

XF-020 records the derivation and source audit in full. In particular, for

\[
D=R(T)\log T,
\qquad
R(T)\to\infty,
\qquad
R(T)=o(T/\log T),
\tag{16}
\]

one has

\[
\boxed{
N_t([T,T+R(T)\log T])
=
\frac{R(T)\log^2T}{4\pi}(1+o(1)).
}
\tag{17}
\]

This reverses the earlier source diagnosis. The local theorem is needed when `D\asymp\log T`, because the `O(\log^2T)` global error is then as large as the main term. Once `D/\log T\to\infty`, the same global error becomes relatively negligible. The source therefore supplies exactly the diverging buffer ratio demanded by (12), provided the buffer remains `o(T)`.

## 5. Interaction with XF-017 and cutoff localization

XF-017 showed that for the **centered** Cauchy leakage one can beat the fixed-ratio `H^{1/2}` barrier using a logarithmic taper over a diverging buffer ratio, with pure geometric cost `O(1/\log R)`. Its nonlinear application was blocked because absolute-value control of `c_{ik}(g_i-h)(g_k-h)` needs pair-level amplitude/conductance information across that broad buffer.

The uncentered carrier of XF-018 has a complementary advantage. Once interactions are summed over contiguous physical blocks, the far exterior is collision-safe and obeys the stronger scale estimate `O(1/R)` from (10), with **no pairwise gap envelope at all**. By (17), a source-valid buffer with `R(T)\to\infty` is available. Consequently the far-exterior piece can be made `o(1)` without postulating new pointwise gap bounds.

What is not controlled by this argument is the interaction with the buffer itself and the removal of the neutral mean. XF-018 writes the block variance as an uncentered square minus a span term; differentiating that span imports endpoint velocities and therefore exterior flux. A complete localization still needs a way to organize those near-buffer and endpoint terms without recreating the singular centered leakage.

Thus two requirements should be kept separate:

1. **far-tail geometry:** after uncentered renormalization and block aggregation, this is now compatible with existing source-valid super-mesoscopic counting;
2. **mean removal / near-buffer dynamics:** this remains open and is where endpoint span information, overlapping blocks, tapering, or signed cancellation must enter.

The exact block estimate removes one candidate obstruction rather than closing the localization argument.

## 6. Stress tests and failure modes

The result is restricted to the real-simple regime because `w_{ik}` comes from the gap ODE of XF-014. The bound itself remains nonsingular as gaps approach zero, but it is not asserted across an actual collision where the ordered real-simple parametrization ceases to apply.

The separation condition matters. Adjacent gap pairs have `w_{i,i+1}=1`; they are not represented by the finite nonadjacent cell integral because two touching intervals produce the endpoint singularity of the continuum kernel. Equations (4)--(10) therefore require at least one complete gap between the core and the far block. This is harmless for a genuine buffer but prevents misusing the estimate as a hard-cutoff boundary bound with zero buffer.

The estimate controls the **sum of kernel weights**, not a signed dynamical term with arbitrary additional amplitudes. It is directly suited to the uncentered localization carrier because `g_i g_k` has already been absorbed into `w_{ik}`. Reintroducing centered amplitudes would undo this renormalization and return to the conductance issue of XF-016--XF-017.

Finally, the source-valid long-window count from XF-020 does not itself control the near-buffer dynamical amplitudes or endpoint velocities. It establishes the spatial room required by (10), not the remaining flux estimate.

## 7. Prior art and novelty boundary

The logarithmic cross-ratio identity for two separated intervals and its Möbius invariance are classical. The double-integral representation used here was already made explicit in XF-018. A targeted search around interval cross-ratios, fractional/Cauchy energies, log gases, and projective interval interactions found the underlying ingredients to be standard and did not identify a Xi-flow theorem packaging the cellwise leakage weights into the block estimate (4)--(10). Absence from that search is not treated as novelty evidence.

Rodgers--Tao's zero-counting estimates are established prior art and are already anchored in `SOURCES.md`. XF-020 corrects how those estimates interact with the present scale: the bounded-`\alpha` local theorem is not the only available source input; subtraction of the global `O(\log^2T)` formula supplies the required super-mesoscopic window. No new external dependency is introduced here.

The Mathia-specific contribution remains the exact combination of the XF-018 carrier with contiguous aggregation: a vague pointwise large-gap concern becomes the scale-free criterion `D/S\to\infty`. The new source audit shows that this criterion is satisfiable at the counting level, so it should no longer be reported as an obstruction.

## 8. Consequence for `xi_flow`

The next localization question should no longer be phrased as whether unconditional Xi information reaches beyond the `\log T` fixed-time core by a diverging factor. XF-020 shows that the existing global count already reaches that scale with vanishing relative error.

The sharper frontier is now **inside the buffer**. One should ask whether the collision-safe uncentered identity can be combined with its span subtraction so that the near-buffer and endpoint-flux terms are either coercive, cancel across overlapping blocks, or are controlled by source-valid aggregate information. If such an organization exists, the far exterior can already be made negligible by choosing `D=R(T)\log T` with `R(T)\to\infty`; if it fails, the obstruction lies in mean removal and local flux, not in the availability of a super-mesoscopic spatial scale.