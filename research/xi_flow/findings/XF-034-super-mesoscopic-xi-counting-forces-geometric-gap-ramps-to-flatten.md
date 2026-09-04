# XF-034 — super-mesoscopic Xi counting forces geometric gap ramps to flatten

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `SOURCE-SPECIFIC` + `STRUCTURAL/BOUNDARY`. XF-032 and XF-033 identify geometric gap progressions as exact bulk null modes for the current normalized-discriminant route and, more generally, for every finite-range translation-invariant assembly of scale-invariant local shape observables. That null family is universal at the level of the local variational algebra. It is **not** source-admissible at nontrivial slope on the super-mesoscopic Xi buffers supplied by XF-020.

Let `t` lie in the real-simple regime `Lambda < t <= 0`, let `x_j(t) \asymp T`, and let

\[
M=M(T)=R(T)\log^2 T,
\qquad
R(T)\to\infty,
\qquad
R(T)=o(T/\log T).
\tag{1}
\]

Suppose that `2M` consecutive gaps form an exact geometric progression

\[
\boxed{
 g_{j+k}=C_T r_T^k,
 \qquad 0\le k\le 2M-1,
}
\tag{2}
\]
with `C_T>0` and `r_T>0`. Then the XF-020 spacing law at lengths `M` and `2M` forces

\[
\boxed{r_T^M=1+o(1),}
\tag{3}
\]
so in particular

\[
\boxed{M\log r_T=o(1).}
\tag{4}
\]

Thus the endpoint gap ratio across one super-mesoscopic half-block satisfies

\[
\frac{g_{j+M}}{g_j}=1+o(1),
\tag{5}
\]

and the whole geometric ramp is asymptotically flat. The nontrivial affine-log-gap null mode of XF-032/033 collapses to the arithmetic-lattice member when it persists across the source-valid Xi buffer scale.

The same conclusion is stable under a uniformly vanishing multiplicative perturbation. If instead

\[
 g_{j+k}=C_T r_T^k e^{\varepsilon_{k,T}},
 \qquad
 \max_{0\le k<2M}|\varepsilon_{k,T}|=o(1),
\tag{6}
\]

then again `r_T^M=1+o(1)`. Hence an `o(1)`-multiplicative neighborhood of the exact geometric null family is also forced to have vanishing total logarithmic slope on the Xi super-mesoscopic scale.

This is a genuine positive source restriction, but it is not yet a Lyapunov theorem. Arbitrary gap profiles can satisfy the same two span asymptotics without being close to a geometric ramp, so XF-020 does not by itself control the mean logarithmic contrast of a general configuration. The remaining problem is now more specific: combine the bulk near-null information of XF-031/033 with source counting strongly enough to show that a configuration with small interior shape force is close to the geometric family, at which point the present counting rigidity would force that family to be nearly arithmetic.

## 1. The source supplies two compatible super-mesoscopic span laws

XF-020 derives from the Rodgers--Tao global zero count that whenever

\[
L=Q(T)\log^2T,
\qquad
Q(T)\to\infty,
\qquad
Q(T)=o(T/\log T),
\]

one has, uniformly in the stated real-simple regime,

\[
 x_{j+L}(t)-x_j(t)
 =\frac{4\pi L}{\log T}(1+o(1))
\tag{7}
\]

for zero blocks based at height comparable to `T`. Apply this once with `L=M` and once with `L=2M`. The hypotheses remain valid because both `R(T)` and `2R(T)` diverge and remain `o(T/log T)`. Therefore

\[
\Delta_M:=x_{j+M}-x_j
=\frac{4\pi M}{\log T}(1+o(1)),
\tag{8}
\]

and

\[
\Delta_{2M}:=x_{j+2M}-x_j
=\frac{8\pi M}{\log T}(1+o(1)).
\tag{9}
\]

Dividing gives the scale-free source constraint

\[
\boxed{
\frac{\Delta_{2M}}{\Delta_M}=2+o(1).
}
\tag{10}
\]

This is stronger for the present purpose than merely fixing the total span of one block. It compares the same gap profile at two nested source-valid scales.

## 2. A geometric ramp has an exact nested-span ratio

Under (2),

\[
\Delta_M
=C_T\sum_{k=0}^{M-1}r_T^k,
\tag{11}
\]

while

\[
\Delta_{2M}
=C_T\sum_{k=0}^{2M-1}r_T^k.
\tag{12}
\]

The second geometric sum splits exactly into two copies of the first, with the second multiplied by `r_T^M`:

\[
\sum_{k=0}^{2M-1}r_T^k
=
\left(1+r_T^M\right)
\sum_{k=0}^{M-1}r_T^k.
\tag{13}
\]

Hence

\[
\boxed{
\frac{\Delta_{2M}}{\Delta_M}=1+r_T^M.
}
\tag{14}
\]

Comparing (10) and (14) yields (3). Positivity then permits taking logarithms:

\[
M\log r_T=\log(r_T^M)=o(1),
\]

which is (4). No Taylor expansion in the individual gaps is used.

The same argument works for `r_T=1` without a separate limiting convention: both sides of (13) are ordinary finite sums and the ratio is exactly two.

## 3. The full dynamic range also collapses

Equation (3) immediately gives

\[
r_T^{2M}=(r_T^M)^2=1+o(1).
\tag{15}
\]

Therefore every gap on the `2M`-gap ramp differs from the first by only a vanishing multiplicative factor:

\[
\sup_{0\le k<2M}
\left|\log\frac{g_{j+k}}{g_j}\right|
\le 2M|\log r_T|
=o(1).
\tag{16}
\]

In the XF-032 notation `d=log r_T`, this says

\[
\boxed{d=o(1/M).}
\tag{17}
\]

For the normalized triple discriminant,

\[
F(d)=-\log2-\frac34d^2+O(d^4),
\tag{18}
\]

so an exact geometric null ramp satisfying the Xi count has vanishing total shape deficit across `O(M)` translated triples:

\[
M\,|F(d)+\log2|=o(1/M).
\tag{19}
\]

The local variational null mode therefore survives algebraically but becomes asymptotically indistinguishable from equal spacing on the source-valid super-mesoscopic block.

## 4. Uniformly near-geometric ramps obey the same rigidity

Assume (6) and write

\[
\eta_T:=\max_{0\le k<2M}|\varepsilon_{k,T}|=o(1).
\]

Let

\[
A_L(r):=\sum_{k=0}^{L-1}r^k.
\]

Then positivity gives

\[
e^{-\eta_T}C_TA_M(r_T)
\le \Delta_M
\le e^{\eta_T}C_TA_M(r_T),
\tag{20}
\]

and likewise

\[
e^{-\eta_T}C_TA_{2M}(r_T)
\le \Delta_{2M}
\le e^{\eta_T}C_TA_{2M}(r_T).
\tag{21}
\]

Consequently

\[
e^{-2\eta_T}\frac{A_{2M}(r_T)}{A_M(r_T)}
\le
\frac{\Delta_{2M}}{\Delta_M}
\le
e^{2\eta_T}\frac{A_{2M}(r_T)}{A_M(r_T)}.
\tag{22}
\]

Since `eta_T=o(1)` and the middle ratio is `2+o(1)` by (10),

\[
\frac{A_{2M}(r_T)}{A_M(r_T)}=2+o(1).
\tag{23}
\]

But the exact geometric identity (13) says this ratio is `1+r_T^M`. Hence again `r_T^M=1+o(1)`.

This is the useful stability form: one does not need an exactly constant contrast field. It is enough to show independently that the log-gap profile is uniformly `o(1)` away from an affine profile across the buffer.

## 5. What this does and does not repair in XF-033

XF-033 proves that finite-range scale-invariant local shape assemblies cannot themselves see the affine slope of `y_i=log g_i`: on an exact geometric ramp their interior Euler coefficient vanishes and the derivative is boundary-supported. The present result supplies a source-specific complement. At the scale where XF-020 gives relative-error-zero nested span information, an exact or uniformly near-geometric profile cannot carry a nonzero macroscopic log slope.

Thus the geometric-ramp obstruction should no longer be read as saying that Xi counting has no leverage on the missing mode. **One total-span constraint is insufficient, but nested super-mesoscopic span constraints kill the exact null family.** The count does not create local bulk coercivity; it removes the dangerous homogeneous state once the bulk dynamics has already forced the profile close enough to that state.

What remains open is the stability bridge from the nonlinear bulk force to geometricity. XF-031 identifies

\[
(L_\lambda h)_i=\phi_{i-1}-\phi_i,
\tag{24}
\]

with `phi=F'` strictly decreasing. Therefore small variation of `phi_i` is the natural finite-gap notion of proximity to the geometric null family. A successful continuation would prove, in a source-admissible collision-safe norm, that small aggregate bulk production or small `L_lambda h` forces an `o(1)`-uniform affine approximation to `log g` on the active buffer. Equation (6) would then trigger the present counting rigidity and force the affine slope to zero.

The finding does **not** prove such a stability estimate. In particular, two nested span constraints do not determine arbitrary individual gaps, endpoint velocities, cross-ratio conductances, or the sign of the full tapered derivative.

## 6. Stress tests and boundaries

The requirement `M/log^2 T -> infinity` is substantive. It is exactly what makes the global Rodgers--Tao counting remainder lower order in XF-020. The argument does not claim the same nested-span rigidity at a fixed multiple of `log^2 T` using only that global count.

The result also needs the ramp to persist across both nested blocks. A short geometric patch embedded inside an arbitrary larger buffer is not constrained by comparing `Delta_M` and `Delta_2M` unless the larger block inherits the same approximate affine-log-gap profile.

The conclusion is not an Xi-specific dynamical selector in isolation. Any matched real-zero flow with the same nested counting law would obey the same flattening theorem. Its role is source restriction: it combines an exact universal null-mode classification with a genuine property of the zero density available for `H_t`.

Finally, the theorem does not cross `t=Lambda` and does not assume RH at `t=0`. It uses only the real-simple regime and the source-valid global count already isolated in XF-020.

## 7. Prior-art and novelty boundary

The Rodgers--Tao zero-counting theorem is the only external load-bearing input and is already anchored in `SOURCES.md` through XF-020. Geometric-series identities and the nested-span comparison are elementary. A targeted literature check did not identify a separate theorem needed for this rigidity step, and no claim of general novelty is made.

The durable line-specific content is the interaction between two previously separate pieces of the Xi-flow program: the geometric-ramp null family of XF-032/033 and the super-mesoscopic nested spacing law of XF-020. Their combination shows that the exact local-shape null mode is **source-forced to flatten** on the available Xi buffer scale.

No `SOURCES.md` change is required.

## 8. Consequence for `xi_flow`

The next target should not be another local scale-free block observable aimed at penalizing the affine log-gap slope; XF-033 already rules out that design class. Nor should the program treat the geometric null family as an unconstrained source scenario; XF-034 shows that nested Xi counting removes every nontrivial exact or uniformly `o(1)`-near geometric ramp across a super-mesoscopic buffer.

The remaining constructive question is a **stability theorem**: can the collision-safe triple-discriminant bulk, together with overlap and tapering, force the active log-gap profile close enough to affine that the nested counting law makes its slope negligible? A negative result would need to exhibit source-compatible profiles whose bulk force is small without being uniformly near-geometric. That is now a sharper obstruction than the exact null mode itself.