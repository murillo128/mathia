# PL-311 — The stretched Volterra defect has an endpoint range obstruction that localizes source matching to an `r=O(s)` corner

**Evidence:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-SELECTION-REFINEMENT`

**Status:** `EXACT-RANGE-CONDITION + EXACT-COMPRESSED-BULK-GEOMETRY + FINITE-S-MATCHING-CONDITIONAL`

## Question

`PL-310` identified the universal fixed profile of the small-order stretched Green operator

\[
(Tf)(r)=e^{-2r}f(r)+e^{-r}\int_0^r e^{-q}f(q)\,dq,
\qquad r>0,
\tag{PL311-1}
\]

but left its amplitude undetermined and observed that the completed-Weil source is lower order at every fixed stretched coordinate `r>0`. The remaining issue is whether that lower-order source can be incorporated by an ordinary endpoint-integrable perturbation of the fixed profile, or whether the singular endpoint `r=0` imposes an additional compatibility condition.

There is an exact obstruction: **the range of `I-T` on corrections integrable at the stretched endpoint can contain only forcings whose continuous endpoint value vanishes.** In particular,

\[
e^{-r}\notin \operatorname{Ran}(I-T)
\tag{PL311-2}
\]

on that class. Since a source with a nonzero limiting boundary value produces precisely an `e^{-r}` forcing after application of `T`, a regular fixed-`r` first-order expansion cannot absorb it unless some other finite-`s` term cancels its endpoint value. The geometry also identifies where the missing compensation can live: every fixed physical bulk point is compressed into an `r=O(s)` neighborhood of the stretched endpoint.

## Method

Let `f` be endpoint-integrable, meaning `f in L^1(0,R)` for every finite `R>0`, and suppose

\[
(I-T)f=h,
\tag{PL311-3}
\]

where `h` extends continuously to `r=0`. Define

\[
V(r)=\int_0^r e^{-q}f(q)\,dq.
\tag{PL311-4}
\]

Then `V(r)->0` as `r downarrow 0` and `V'=e^{-r}f` almost everywhere. Equation (PL311-3) becomes

\[
(1-e^{-2r})f(r)-e^{-r}V(r)=h(r),
\]

hence

\[
V'(r)-\frac{V(r)}{e^{2r}-1}
=\frac{e^{-r}h(r)}{1-e^{-2r}}.
\tag{PL311-5}
\]

The homogeneous integrating factor is encoded by

\[
\frac{d}{dr}\log\sqrt{1-e^{-2r}}
=\frac{1}{e^{2r}-1},
\]

so

\[
\boxed{
\frac{d}{dr}
\left(
\frac{V(r)}{\sqrt{1-e^{-2r}}}
\right)
=
\frac{e^{-r}h(r)}{(1-e^{-2r})^{3/2}}.
}
\tag{PL311-6}
\]

If `h(0)=h_0 != 0`, the right-hand side is

\[
\frac{h_0+o(1)}{(2r)^{3/2}}
\qquad (r\downarrow0).
\]

Integrating (PL311-6) therefore gives

\[
\frac{V(r)}{\sqrt{1-e^{-2r}}}
=-\frac{h_0+o(1)}{\sqrt{2r}},
\]

and hence

\[
V(r)\longrightarrow -h_0,
\qquad r\downarrow0,
\tag{PL311-7}
\]

contradicting (PL311-4). Consequently

\[
\boxed{
(I-T)f=h,\ f\text{ endpoint-integrable},\ h\in C([0,R])
\quad\Longrightarrow\quad h(0)=0.
}
\tag{PL311-8}
\]

This is only a necessary range condition; no surjectivity claim is made for the subspace `h(0)=0`.

## Evidence

The obstruction is internally exact. As a concrete test,

\[
T1
=e^{-2r}+e^{-r}\int_0^r e^{-q}\,dq
=e^{-r},
\tag{PL311-9}
\]

so `e^{-r}` has endpoint value one and (PL311-8) proves (PL311-2). This is not a statement about an abstract closure of the range in a weaker topology: it is a pointwise endpoint obstruction for an actual endpoint-integrable correction solving the Volterra equation.

The second exact ingredient comes from the stretched coordinate of `PL-310`,

\[
x_s(r)=1-2e^{-r/s}.
\]

If `r=sL`, then

\[
\boxed{x_s(sL)=1-2e^{-L},}
\tag{PL311-10}
\]

which is independent of `s`. Equivalently, every fixed physical point `x in (-1,1)` corresponds to

\[
L(x)=-\log\frac{1-x}{2},
\qquad
r_s(x)=sL(x)=O(s).
\tag{PL311-11}
\]

Thus the whole macroscopic physical interval collapses into an `r=O(s)` corner of the stretched coordinate. The fixed-`r>0` limit in `PL-310` necessarily discards exactly the region in which bulk information remains spatially resolved.

For the completed-Weil equation of `PL-310`, write schematically

\[
U_s=T_s\bigl[\alpha_s U_s-2\sqrt{s}\,a^{2s}g_s\bigr],
\qquad
 g_s(q)=(B_aw_s)(x_s(q)),
\tag{PL311-12}
\]

with `alpha_s=1+O(s)`. If, at fixed `q>0`, `g_s(q)->g_+`, then the source part of a formal `sqrt(s)` equation is

\[
-2g_+T1=-2g_+e^{-r}.
\tag{PL311-13}
\]

For `g_+ != 0`, (PL311-8) says that this forcing cannot be absorbed by an endpoint-integrable regular correction. Therefore any valid first-order asymptotic description must either contain another term whose endpoint forcing cancels (PL311-13), or cease to be a regular fixed-`r` perturbation and resolve an additional corner/endpoint scale. Identity (PL311-11) gives the canonical candidate location of that missing matching region.

This source interpretation is structurally compatible with `PL-305`. Its finite prime-shift part is a sum of compressed translations `C_h+C_{-h}`. As `x->1^-`, the positive shift leaves the interval while the negative shift samples the interior value near `x=1-h`; the completion operator has a smooth integral kernel and therefore also admits a boundary functional under the corresponding bulk convergence. Hence a source-sensitive scalar `g_+` is a natural possible output of global matching rather than an arbitrary added parameter. This paragraph does **not** assert that the actual small-`s` branch has a nonzero `g_+`.

## Analysis

The new point is not another boundary profile. `PL-310` already proved that the principal fixed-`r` shape is universal and source-blind. The exact range calculation above shows why the next source-sensitive correction is singularly constrained: `I-T` loses the endpoint direction represented by a nonzero constant value of the forcing. Since constant boundary data are sent by `T` to `e^{-r}`, the first lower-order source naturally hits precisely that forbidden direction.

This sharpens the source-selection problem. The amplitude `C` in

\[
U_0(r)=\frac{C}{\sqrt{e^{2r}-1}}
\]

cannot in general be selected by simply solving an ordinary first-order inhomogeneous Volterra equation on the same fixed-`r` scale. The global information removed by the principal limit is geometrically concentrated at `r=O(s)`, where fixed physical bulk points remain distinguishable. Any mechanism by which the rational-prime/completion source selects `C` must therefore survive through that matching region or through an equivalent endpoint compensation.

The result is also a negative control against an apparently natural shortcut: knowing the universal kernel `T`, the fixed profile, and a bounded boundary value of the source is not enough to build a regular perturbation series on the outer stretched scale. The singular endpoint compatibility has to be addressed explicitly.

## Prior-art and novelty audit

Local duplicate checks against the `prime_lattice` findings and commit history found no previous statement of the range condition (PL311-8), the forbidden direction (PL311-2), or their combination with the exact compressed-bulk identity (PL311-11). The older Volterra/torsion negative result in this line concerns a different operator-level shortcut and does not imply this endpoint range obstruction.

A structural literature search around small-order fractional-Laplacian boundary layers, logarithmic-Laplacian asymptotics, and Volterra range conditions found broad surrounding theory but no direct match for this particular stretched Green operator and endpoint compatibility calculation. That search is **not** evidence of global novelty. The claim here is classified only as an exact new-to-line derivation and source-selection refinement; the elementary first-order ODE method itself is standard.

## Limits

The exact part of this finding stops at (PL311-8), (PL311-9), and (PL311-11). It does **not** yet prove a matched asymptotic expansion for the finite-`s` Green operator. In particular, `PL-310` proves convergence of `T_s` to `T` at fixed stretched coordinates but does not supply an error estimate of the form `T_s-T=o(sqrt(s))`. A finite-`s` kernel correction of order `sqrt(s)` could in principle contribute its own nonzero endpoint forcing and cancel (PL311-13).

Likewise, boundedness or convergence of `g_s(q)` at fixed `q` does not by itself identify the limiting boundary functional on the actual normalized small-order branch. Establishing `g_+`, proving it is nonzero when needed, and connecting it to the amplitude `C` require a genuine overlap theorem between the `r=O(s)` corner, the fixed physical bulk, and the outer stretched profile. No RH consequence follows from the range obstruction alone.

The endpoint-integrability hypothesis is deliberate. The principal profile behaves as `r^{-1/2}` and belongs to `L^1(0,R)`, so this is the natural class for a regular correction around `PL-310`. More singular corrections may evade (PL311-8); if they occur, that is itself evidence that the ordinary outer expansion has broken down and that an additional layer is required.

## Verdict

**Exact obstruction / positive localization of the next problem.** The limiting Volterra defect has a codimension-like endpoint compatibility condition: any continuous forcing in its endpoint-integrable range must vanish at `r=0`, and the canonical constant source direction produces the forbidden forcing `e^{-r}`. Independently, the stretched map sends every fixed physical bulk point into `r=O(s)`. Together these facts give a precise reason that the source/amplitude information missing from `PL-310` cannot be recovered by a naive regular perturbation at fixed `r>0`; it must be supplied by an endpoint cancellation or by matching through the compressed `r=O(s)` corner.

This materially narrows the completed-Weil source-selection frontier but does not yet select the critical line or determine the amplitude. A useful next theorem would quantify `T_s-T` uniformly across the `r=O(s)`/fixed-`r` overlap and identify the resulting solvability condition for `C`. The isolated Volterra range lemma is not being delegated for formalization at this stage: its elementary proof is exact, while the load-bearing unresolved mathematics is the finite-`s` overlap interface rather than the lemma itself.
