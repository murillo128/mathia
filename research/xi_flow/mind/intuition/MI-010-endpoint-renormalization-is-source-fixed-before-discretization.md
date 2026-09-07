# MI-010 — Endpoint renormalization is source-fixed before Xi discretization

**Evidence level:** exact singular-quadrature derivation and literature-backed positive-time reference reduction through XF-089

## Core intuition

The Xi source-to-grid bridge has a genuine endpoint renormalization, but its leading singular sector is no longer an unknown dynamic error. The exact endpoint carrier contains the pole `-1/(4 xi)`. XF-088 proves that a periodic trapezoid sampling of this pole requires the mesh counterterm `(1/4) log Delta delta_0`; without it the discrete Volterra vector field has a logarithmically growing defect, while with it the guarded weighted error is negligible at the declared scales.

XF-089 then shows that positive heat time does not change that pole residue. The Polymath15 high-line reference carries the full degree-`-1` endpoint sector with residue `-1/4` throughout `0<=t<=1/2`, and the actual/reference residual is one Fourier derivative better. The source-faithful interface should therefore **subtract/transport the deterministic endpoint reference before discretization**, rather than re-fit a singular counterterm independently at each heat time.

## Strongest justified principle

XF-087 identifies the periodic power-sum dynamics with composite-trapezoid discretization of the one-sided Volterra flow. XF-088 isolates the failure of applying a smooth quadrature estimate directly to the raw endpoint. For a datum `F(xi)=-c/xi+b(xi)`, the analytic-family finite part and the punctured lattice differ by a forced mesh term `c log Delta delta_0`. After adding it, the vector-field mismatch is `O(1/m+m Delta^2)` on the small endpoint block; for Xi, `c=1/4`, and the exact XF-086 sideband weighting makes the total guarded defect `o(1)`. Omitting the counterterm leaves a leading vector-field error `2 c^2 log(1/Delta)+O(1/m)`.

XF-089 supplies the dynamic normalization. On a fixed high horizontal line, Polymath15's explicit reference `M_t` gives an actual/reference logarithm that remains bounded. The corresponding carrier difference is

`Z_t-Z_t^M = -(xi/(2 pi)) e^(a xi) \widehat L_(t,a)(xi)`,

so the residual has an exact factor of `xi`. The reference endpoint has

`Z_t^M(xi) = -e^-xi/(4 xi) - (t/8)e^-xi(log xi + gamma + log(4 pi)) + O_t(1)`,

hence the degree-`-1` residue stays `-1/4` for the whole classical positive-time interval. Heat introduces a lower-order logarithmic cusp but no new pole.

The remaining source-to-grid theorem should therefore estimate the reference-subtracted residual in the guarded Fourier/moment resource and account for any lower-order endpoint terms. The leading pole and the coefficient of its lattice counterterm are fixed source data, not free discretization choices.

## Counterevidence / boundary

Boundedness of the Polymath quotient does not itself provide the shrinking-band Fourier norm needed by the guarded selector, and the exact `xi` factor does not justify pointwise sampling of an arbitrary residual distribution. XF-089 also does not rule out lower-order counterterms or prove positive-transition coercivity.

Different finite-part conventions can move a fixed constant multiple of `delta_0`, but they cannot remove the mesh-dependent `c log Delta` coefficient. A useful alternative formulation must therefore be exactly equivalent to the same source-fixed renormalization rather than silently choosing a smoother endpoint model.

## Epistemic status

**Proved leading endpoint renormalization and time-independent pole residue; lower-order reference-residual control and positive-transition coercivity remain open.** No statement about the sign of the de Bruijn--Newman constant follows.

## Falsification criterion

Show that the raw Xi pole admits the XF-087 trapezoid comparison without the logarithmic counterterm at the stated guarded scales, or that the positive-time carrier acquires a different `1/xi` residue despite the XF-089 bounded-reference identity. Conversely, a guarded norm estimate for the reference-subtracted residual that closes the remaining continuum-to-grid error would validate the intended bridge.