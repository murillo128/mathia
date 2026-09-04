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

Thus no pointwise upper or lower gap bound is needed to control the aggregate far exterior. To make that leakage `o(1)`, however, one needs `D/S\to\infty`. Combining this exact block reduction with XF-007 and Rodgers--Tao's source-valid zero-counting scale exposes a sharper obstruction: a fixed-heat-time Xi core already has `S\asymp\log T`, while the unconditional real-simple counting input used in the contradiction regime controls windows only of physical size `O(\log T)` with bounded scale factor. The present source package therefore supplies a **scale-matched buffer, not a super-mesoscopic one**.

This replaces the pointwise large-gap concern in XF-018 by a more global and more precise requirement. The remaining far-tail problem is not that one must bound every gap individually; it is that a localization argument which wants vanishing aggregate exterior mass needs trustworthy zero geometry beyond the `\log T` fixed-time memory window by a diverging physical scale factor.

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

The integral is elementary. Writing

\[
A_0=x_a,\quad B_0=x_{b+1},\quad C_0=x_c,\quad D_0=x_{d+1},
\]

with `A_0<B_0<C_0<D_0`,

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

The right side is itself the logarithm of the cross-ratio of the **four block endpoints**. Thus the cellwise projective kernel of XF-018 is stable under contiguous aggregation: microscopic gap ratios disappear from the upper bound and only the geometry of the two macroscopic intervals remains.

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

Then (5) becomes the scale-free formula

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

The resulting condition is also sharp in scale. If `D_+=R S` with fixed `R`, the right side of (7) is the nonzero constant `log(1+1/R)`. To force the aggregate far-tail mass to vanish uniformly by this mechanism alone one needs

\[
\boxed{D_+/S\to\infty}
\tag{12}
\]

and similarly on the left. A fixed-ratio buffer cannot supply a small parameter.

On an arithmetic lattice this requirement is visible directly: `w_{ik}=1/(i-k)^2`, and the interaction of a block of `N` sites with a tail beginning `RN` sites away approaches the same scale-free logarithmic profile. Thus the conclusion is not an artifact of irregular gaps.

## 4. Comparison with the source-valid Xi scales

XF-007 identified the fixed-heat-time memory scale near local equilibrium as

\[
N_T\asymp \log^2 T
\]

gaps, corresponding to physical core length

\[
S_T\asymp \log T.
\tag{13}
\]

Rodgers--Tao's Theorem 3.2 and Corollary 3.3 give, in the hypothetical real-simple regime `\Lambda<t\le0`, the source-valid mesoscopic counting law

\[
N_t([T,T+\alpha\log T])
=
\frac{\alpha\log^2T}{4\pi}+o(\log^2T)
\tag{14}
\]

for bounded `\alpha`, uniformly in bounded `\alpha`, and equivalently

\[
x_k(t)-x_j(t)
=
\frac{4\pi(k-j)}{\log \xi_j}+o(\log \xi_j)
\tag{15}
\]

for `k-j\le \log^2\xi_j` in their stated normalization.

This is exactly enough to resolve physical spans of order `\log T` with a **bounded** scale factor. It is not, as stated, a theorem uniform for `\alpha=\alpha(T)\to\infty`, nor does Corollary 3.3 extend (15) to `\omega(\log^2T)` index windows.

Consequently the known counting input can provide a buffer comparable to the fixed-time core, but the purely geometric far-tail estimate (10) needs a buffer whose physical span is asymptotically larger than the core if its contribution is to become `o(1)`:

\[
\boxed{
\text{fixed-time core }\asymp\log T
\quad + \quad
\text{vanishing block tail}
\quad\Longrightarrow\quad
\text{controlled buffer }=\omega(\log T).
}
\tag{16}
\]

This is a source-boundary statement, not a theorem that such larger-scale control is impossible. It says only that the currently imported Rodgers--Tao counting theorem does not by itself supply the diverging scale ratio required by (10).

## 5. Interaction with XF-017 and cutoff localization

XF-017 showed that for the **centered** Cauchy leakage one can beat the fixed-ratio `H^{1/2}` barrier using a logarithmic taper over a diverging buffer ratio, with pure geometric cost `O(1/\log R)`. Its nonlinear application was blocked because absolute-value control of `c_{ik}(g_i-h)(g_k-h)` needs pair-level amplitude/conductance information across that broad buffer.

XF-019 shows that the uncentered carrier of XF-018 has a complementary advantage. Once interactions are summed over contiguous physical blocks, the far exterior is already collision-safe and obeys the stronger scale estimate `O(1/R)` from (10), with **no pairwise gap envelope at all**. The remaining price is still a diverging buffer ratio and, separately, the neutral mean/span mode identified in XF-018.

Thus two previously entangled requirements should be kept separate:

1. **far-tail geometry:** after uncentered renormalization and block aggregation, this needs only a super-core physical buffer, not pointwise gap control;
2. **mean removal / near-buffer dynamics:** this is where endpoint span information, tapering, or an additional signed cancellation must still enter.

The exact block estimate therefore removes one candidate obstruction rather than closing the localization argument.

## 6. Stress tests and failure modes

The result is restricted to the real-simple regime because `w_{ik}` comes from the gap ODE of XF-014. The bound itself remains nonsingular as gaps approach zero, but it is not asserted across an actual collision where the ordered real-simple parametrization ceases to apply.

The separation condition matters. Adjacent gap pairs have `w_{i,i+1}=1`; they are not represented by the finite nonadjacent cell integral because two touching intervals produce the endpoint singularity of the continuum kernel. Equations (4)--(10) therefore require at least one complete gap between the core and the far block. This is harmless for a genuine buffer but prevents misusing the estimate as a hard-cutoff boundary bound with zero buffer.

The estimate controls the **sum of kernel weights**, not a signed dynamical term with arbitrary additional amplitudes. It is directly suited to the uncentered localization carrier because `g_i g_k` has already been absorbed into `w_{ik}`. Reintroducing centered amplitudes would undo this renormalization and return to the conductance issue of XF-016--XF-017.

Finally, the need for `D/S\to\infty` is a uniform geometric requirement. A particular Xi configuration may have additional cancellation or arithmetic structure allowing a smaller buffer. No such cancellation is supplied by the present argument.

## 7. Prior art and novelty boundary

The logarithmic cross-ratio identity for two separated intervals and its Möbius invariance are classical. The double-integral representation used here was already made explicit in XF-018. A targeted search around interval cross-ratios, fractional/Cauchy energies, log gases, and projective interval interactions found the underlying ingredients to be standard and did not identify a Xi-flow theorem packaging the cellwise leakage weights into the block estimate (4)--(10). Absence from that search is not treated as novelty evidence.

Rodgers--Tao's Theorem 3.2 and Corollary 3.3 are established prior art and are already anchored in `SOURCES.md`; no new literature dependency is introduced here. The Mathia-specific contribution is the exact combination of the XF-018 carrier with contiguous aggregation and the fixed-time scale from XF-007, which turns the vague large-gap concern into the explicit source requirement `controlled buffer = omega(log T)` if one wants uniform vanishing of the uncentered far tail.

## 8. Consequence for `xi_flow`

The next localization question should no longer be phrased as “can every gap in a broad buffer be bounded away from zero and infinity?” That is stronger than the uncentered carrier needs for its far exterior. **Aggregate cross-ratio leakage only asks for enough trustworthy physical span between the `log T` core and the uncontrolled exterior.**

The sharp source-level test is now whether one can obtain, in the hypothetical real-simple regime and without circular RH input, either:

- zero-counting/span control on windows `omega(log T)` while retaining errors strong enough for the energy argument; or
- a multiscale/signed organization that cancels the residual fixed-ratio exterior contribution without requiring such a super-mesoscopic window.

If neither is available, the remaining obstruction is not collision singularity and not pointwise gap irregularity. It is the absence of a **diverging spatial scale ratio beyond the fixed-time mesoscopic core**.