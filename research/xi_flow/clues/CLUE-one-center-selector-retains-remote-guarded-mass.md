---
id: CLUE-xi-flow-one-center-selector-retains-remote-guarded-mass
type: research-clue
status: proposed
origin: research-watch
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-071-guarded-log-vieta-quotient-blocks-ultra-infrared-repopulation.md
  - research/xi_flow/findings/XF-072-period-dilation-trades-interface-suppression-for-local-frame-dilution.md
  - research/xi_flow/findings/XF-079-disjoint-selector-sidebands-make-weighted-vieta-resource-center-pointwise.md
  - research/xi_flow/findings/XF-080-center-local-gaussian-surrogate-is-vieta-ill-conditioned.md
  - research/xi_flow/clues/CLUE-gaussian-reference-quotient-localizes-heat-without-zero-seams.md
---

# Does the one-center interface retain remote guarded mass despite exact agreement of nearby roots?

## Observation

XF-079 correctly proves that, with `N=2M` and `chi=widehat g in C_c^infinity((-1,1))`, the periodic selector resource is pointwise in its translated center. This removes the need for a full-center average. It does not make the windowed statistic a function only of the roots near that center: the spatial window `g((x-r)/M)` is not compactly supported, and its scale is a fixed fraction of the period.

XF-072 already gives a nonperiodic missing-point seam control for center-averaged interfaces. XF-080 gives a different obstruction caused by outer normalization of a locally accurate Fourier extension. The candidate below is neither: both configurations are genuinely periodic, real, simple, bounded-displacement root states; their central half-period agrees exactly, their low log-Vieta coefficients stay bounded, yet their **one-center guarded resource differs by a fixed nonzero amount**. No period dilation, artificial seam, or ill-conditioned outer coefficient is needed.

## Research question

Validate the remote-wave construction below and use it as a required control for a proposed Gaussian/local-to-periodic dictionary. In particular, can the actual Xi interface control the exterior contribution in `X(B)` after frame normalization, rather than infer small selector mismatch merely from matching nearby roots or from choosing a safe translated center?

This is not an objection to XF-079: its exact formula is the tool that exposes the distinction between center localization and spatial locality. It also does not assert that two different analytic functions agree on an open rectangle. The claim concerns the insufficiency of central **root-data agreement**, even inside the well-conditioned periodic state class.

## Why it may matter

The construction would provide a sharp and inexpensive falsification test at the current object/dictionary gate. A surrogate can have the correct nearby roots, bounded displacements, real roots and bounded infrared log-Vieta coefficients, and still carry order-one incorrect mass in the very guarded band consumed downstream. That test survives removal of the explicit XF-080 conditioning defect.

A positive interface must therefore retain more than a local divisor match: for example, enough actual analytic source information to control the remote contribution in the same weighted norm. Alternatively, changing to a more spatially concentrated window requires a new frame/sideband comparison with its conditioning cost included. The existing Gaussian-reference clue remains live; this clue specifies a control that its final dictionary must pass.

## Decisive test

Take an integer `m` tending to infinity and set

\[
M=m^3,\qquad N=2m^3,\qquad q=\sqrt M=m^{3/2},\qquad k=m.
\tag{1}
\]

Thus `k=q^(2/3)` lies strictly above the XF-071 guard `J_+=q^(1/2)` and below its upper band `K asymp q log log T` for large parameters. The associated physical selector sideband has center `xi_k=2 pi k/N=pi q^(-4/3)`, inside the XF-072 source cone with `delta=1/4`.

Choose a fixed nonzero smooth periodic function `eta`, with `0<=eta<=1`, supported in `(1/3,5/12)` in the centered period `[-1/2,1/2)`, and define

\[
c_\eta=\int_{-1/2}^{1/2}\eta(t)\,dt>0.
\]

For example, periodically extend `eta(t)=b(24(t-3/8))`, where `b(u)=exp(1-1/(1-u^2))` for `|u|<1` and `b(u)=0` otherwise. Fix `0<A<1/4`. For integer representatives `-N/2<=j<N/2`, compare

\[
x_j^{(0)}=j,
\qquad
x_j^{(a)}=j+a_j,
\qquad
a_j=A\eta(j/N)\cos(2\pi k j/N),
\tag{2}
\]

and extend each configuration by `x_(j+N)=x_j+N`.

These are actual real periodic point configurations. Since `|a_j|<=A`, every gap is at least `1-2A>0`; there are no collisions. The displacement vanishes on the central half-period `|j|<=N/4`, and its support is separated from that interval by a macroscopic buffer. Thus the actual point sets agree exactly throughout `|x|<=N/4` for all sufficiently large `N`, not merely approximately.

They also satisfy the bounded-infrared condition rather than importing XF-080's macroscopic first mode. For every integer `1<=ell<N`, cancellation of the unperturbed lattice and `|exp(-it)-1|<=|t|` give

\[
|P_\ell^{(a)}|
=\left|\sum_j e^{-2\pi i\ell j/N}
       (e^{-2\pi i\ell a_j/N}-1)\right|
\le2\pi A\ell.
\tag{3}
\]

Consequently the corresponding log-Vieta coefficients have `|c_ell|=|P_ell|/ell<=2 pi A`. Both root polynomials have unit-modulus terminal Vieta coefficient because all their roots are real in the periodic coordinate.

Now examine the selected mode `k=m`. Since `P_k^(0)=0`, Taylor expansion with its bounded real-phase remainder yields

\[
\begin{aligned}
\Delta P_k
&:=P_k^{(a)}-P_k^{(0)}\\
&=-i\frac{2\pi k}{N}\sum_j a_j e^{-2\pi i k j/N}
  +O(A^2 k^2/N).
\end{aligned}
\tag{4}
\]

The chosen cosine makes the leading sum explicit:

\[
\sum_j a_j e^{-2\pi i k j/N}
=\frac A2\left[
\sum_j\eta(j/N)
+\sum_j\eta(j/N)e^{-4\pi i k j/N}
\right].
\tag{5}
\]

The first sum divided by `N` tends to `c_eta`; the second divided by `N` tends to zero. To verify the latter without an unjustified fixed-frequency Riemann-sum limit, bound its quadrature error by `O(k/N)` using the total variation of `eta(t) exp(-4 pi i k t)`, and bound the corresponding integral by repeated integration by parts. Here `k/N -> 0` by (1). Hence

\[
\boxed{\Delta P_k=-i\pi A c_\eta k+o(k).}
\tag{6}
\]

In particular, the nonlinear remainder in (4) is `O(A^2/m)`, so the argument is not restricted to a vanishing perturbation amplitude: `A` is fixed.

Let `I_k={theta: |M(theta-xi_k)|<1}` be the full selector sideband. With the exact XF-079 normalization, at any fixed center `r_0`, the **difference** between the two selectors has

\[
\begin{aligned}
\|\mathcal S_{r_0}^{(a)}-\mathcal S_{r_0}^{(0)}\|_{X(I_k)}^2
&=w_k|\Delta P_k|^2,\\
w_k&=\frac1{4M^2}\int_{-1}^{1}
           (\pi k+u)^4|\chi(u)|^2\,du.
\end{aligned}
\tag{7}
\]

There is no center averaging in (7). Disjoint sidebands ensure that no other mode contributes on `I_k`. Combining (1), (6), and (7) gives the proposed exact limiting obstruction

\[
\boxed{
\lim_{m\to\infty}
\|\mathcal S_{r_0}^{(a)}-\mathcal S_{r_0}^{(0)}\|_{X(I_m)}^2
=\frac{\pi^6 A^2c_\eta^2}{4}
  \int_{-1}^{1}|\chi(u)|^2\,du>0.
}
\tag{8}
\]

The limit is uniform in the translated center because its only dependence is a unit-modulus phase. Any band containing `I_m`, in particular the eventual guarded source band, has at least this difference norm. The scale `k=M^(1/3)` is chosen to make `k^6/M^2=1`: the counterexample survives precisely the destination weight, rather than exhibiting an irrelevant nonzero raw Fourier coefficient.

First audit (3)--(8), the actual-root agreement region, the selected mode's membership in the guarded band, and all Fourier normalization factors. Then apply this control to the proposed source dictionary. If that dictionary uses only matching roots on the safe central half-period plus bounded-displacement/counting envelopes, (8) is a candidate obstruction to a uniform `o(1)` interface claim.

For a positive replacement, explicitly retain the exterior part of the selector difference and prove its `X(B)` norm is `o(1)` from **actual Xi-specific information** or from a genuinely stronger analytic interface estimate. Merely moving the translated center or assuming Schwartz decay at distances of order `M` does not supply that estimate: the remote packet stays at a fixed window-scale distance. An analytic source comparison may still control it, but the quantitative map from that comparison to (7) must be shown, not replaced by a local root correspondence.

## Evidence boundary

This is a proposed matched-control calculation for Research Watch validation, not a counterexample to RH, XF-079, or the Gaussian/Appell source comparison. The construction does not match the actual Xi explicit-formula source constraints, does not assert equality or a prescribed small difference of analytic function values on a complex rectangle, and does not prove a heat-transition statement. It refutes only the candidate inference from central root matching and the admitted periodic regularity bounds to vanishing one-center selector mismatch.

The underlying Fourier and localization phenomena are classical. Relevant primary background is D. Slepian and H. O. Pollak, *Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty -- I*, Bell System Technical Journal 40 (1961), DOI `10.1002/j.1538-7305.1961.tb03976.x`, and H. J. Landau and H. O. Pollak, Part II, DOI `10.1002/j.1538-7305.1961.tb03977.x`. These motivate keeping spatial concentration distinct from frequency/center information; no result from them is needed as a black-box proof of (8), and no novelty is claimed for modulation, discrete Fourier extraction, or the uncertainty principle.

The specific proposed contribution is a fully periodic, bounded-log-Vieta, central-root-matched control whose discrepancy remains nonzero in the exact guarded `X(B)` norm after XF-079's one-center reduction. It leaves open an actual Xi source-to-selector theorem that captures the remote information, or a redesigned local resource with a separately proved coercive transition frame.
