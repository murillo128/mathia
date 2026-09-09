---
id: CLUE-weil-inertia-two-harmonic-screen-continuum-residual
type: research-clue
status: resolved
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-211-two-offline-pairs-screen-the-full-two-harmonic-packet.md
  - research/weil_inertia/findings/WI-212-finite-harmonic-packets-admit-sparse-deep-offline-screens.md
---

# Does the exact two-pair screen leave a full-scale residual across the natural reciprocal-peak width?

## Observation

WI-211 cancels both reciprocal samples available for `2<d<3` with two additional deep off-line pairs, and WI-212 extends finite-sample screening to every fixed reciprocal-harmonic packet. The unresolved test was whether WI-211's exact two-pair screen also flattens the coherent peak on its natural `1/M` frequency width once integer phase lifts are allowed, and whether that width survives honest conversion to the source-fixed Gallagher observable.

For odd `M`, the centered bow is

\[
D_M(t)=\frac{\sin(\pi Mt)}{\sin(\pi t)},
\qquad
B_M(t)=2\cosh(ht)D_M(t),
\]

and the central WI-211 screen uses its exact larger quadratic root `y_M`, with

\[
a_M=\operatorname{arcosh}\sqrt{y_M},
\qquad
\phi_M=\arccos(-A_M/\sqrt{y_M}),
\]

so that

\[
S_M(t)=4\cosh(a_Mt)\cos(\phi_Mt),
\qquad
(B_M+S_M)(1)=(B_M+S_M)(2)=0.
\]

The clue proposed the natural-scale profile at `t=2+u/M`, required a uniform Taylor proof rather than numerical fitting, explicitly retained the freedom to lift either screen ordinate by an integer grid step, and required the continuum window to be priced in the native source norm before drawing any zeta conclusion.

## Resolution

WI-213 proves the central profile and then classifies every admissible integer-lift family with bounded normalized continuum energy. After a subsequence, such a family has an integer relative lift `q` and a limiting common lift `kappa`, with exact local profile

\[
F_{h,\kappa,q}(u)
=2\cosh(2h)\frac{\sin(\pi u)}{\pi u}
+e^{2\pi i\kappa u}
\left[-2\cosh(2h)+\pi(3+4q)\cosh^2(h)u\right].
\]

At the cancelled harmonic,

\[
F'_{h,\kappa,q}(0)
=\pi(3+4q)\cosh^2h-4\pi i\kappa\cosh(2h),
\]

hence

\[
|F'_{h,\kappa,q}(0)|\ge\pi\cosh^2h>0.
\]

Thus no bounded-energy integer lift flattens the natural-scale peak. The central representatives `(q,kappa)=(0,0)` have slope `3 pi cosh^2 h`, while the best relative lift `q=-1`, `kappa=0` reduces the leading small-window energy coefficient by a factor `9` but cannot make it vanish. Relative lifts growing with `M` have divergent normalized continuum energy and therefore do not provide a low-energy escape.

WI-213 also supplies the required source dictionary. With `L=log T` and

\[
X=T^{2/d},
\qquad
x_M(u)=T^{(2+u/M)/d},
\]

the synthetic profile is exactly the `x^{1/2}`-normalized selected zero-residue integrand of the twisted explicit formula. A fixed `u`-window has physical relative width `asymp L/(dM)`, precisely the bow/Gallagher scale. Integrating over a fixed short `u`-interval converts the nonzero profile into selected residue energy of order

\[
\frac{X^2L^3}{d^3M},
\]

while the raw-prime Gallagher diagonal at the matching short length is of order

\[
\frac{X^2L^2}{d^2M}.
\]

The residual is therefore `Omega(log T)` superdiagonal in energy. The continuum channel is not being added for free.

This still does not exclude an actual zeta bow. The full explicit formula retains remote/complementary zeros and the structured source terms, and WI-195 records that the needed diagonal-scale upper bound for the full source-fixed error is not currently established. WI-213 therefore resolves the clue by ruling out phase-lift flattening of the explicit two-pair screen and locating the exact source-scale burden, not by claiming RH or a density improvement. More general unequal-depth or multi-pair continuum screens remain a separate research problem.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/weil_inertia/findings/WI-213-natural-scale-residual-survives-two-pair-phase-lifts]]