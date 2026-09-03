# MI-003 — Fixed-time Xi memory is mesoscopic and fractional, while ordinary self-similar localization is scale critical

**Evidence level:** supported; finite-jet obstruction is proved under the simple double-collision hypothesis, mesoscopic scaling is exact for the linearized lattice model, nonlinear coercivity is used only through accepted findings in their stated regimes, and the self-similar localization obstruction is exact for the XF-016 cutoff class

## Core intuition

Order-one heat-time memory at high Xi height lives on a growing mesoscopic field, not in a finite collision jet or bounded gap stencil. The universal linearized boundary model is a Cauchy/half-Laplacian flow, and `L log L` adjacent-gap data supply an endpoint carrier at the correct `h^2` amplitude without a diverging Hilbert-transform constant.

The accepted nonlinear evidence shows that Cauchy-strength bulk coercivity can survive finite-amplitude gap deformation under an upper-gap envelope. But this does **not** make ordinary finite-window localization asymptotically exact. At the one-dimensional `H^{1/2}` endpoint, a fixed-shape self-similar cutoff has order-one boundary leakage on the same scale as the useful bulk term. The live problem is therefore source-specific control or cancellation of the exterior flux, or a genuinely non-self-similar localization architecture.

## Strongest justified principle

XF-006 rules out every robust finite collision jet as Xi-specific. XF-007--XF-010 identify the fixed-time scale: `Theta(log^2 T)` gaps, physical length `Theta(log T)`, Cauchy `|D|` dynamics, and failure of fixed-radius smooth stencils to retain the required phase at the `h^2` scale.

XF-011--XF-013 identify an endpoint carrier. Adjacent-gap `W^{1,p}` Lyapunovs approach the critical exponent with a logarithmic operator loss, while the Young function `Phi(s)=s log(e+s)` gives an exact Markov Lyapunov with raw `Theta(h^2)` scale and the Zygmund endpoint bound `H:L log L->L^1` controls the Cauchy driver with an `h`-independent constant.

XF-015 proves the accepted finite-amplitude bulk comparison in its stated envelope regime. Under `g_r<=Mh`, the relevant conductances dominate the inverse-square Cauchy conductances; small gaps cannot soften the controlled bulk. With two-sided envelopes the full inverse-square tail is quantitatively preserved.

XF-016 closes the conventional cutoff escape and supplies the localization statement needed here directly. For a finitely supported weight `psi`, its exact localized gap identity splits into a positive quadratic bulk term plus the signed leakage

`2 sum_{i<k} c_{ik}(psi_i-psi_k)^2 v_i v_k`.

At the arithmetic-lattice linearization, sampling a fixed cutoff profile on an `N`-gap block sends both the useful quadratic term and this leakage to nonzero continuum `H^{1/2}` forms. There is no decaying power of `N`; weighted-mean centering still leaves nonzero leakage, and bounded gap envelopes give only an `O(1)` estimate rather than `o(1)`. At the fixed-time scale `N~log^2 T`, smooth self-similar tapering therefore cannot make the boundary lower order.

The open adversarial sidecar on XF-014 is deliberately not used as accepted evidence here. Its challenged absolute-convergence justification remains outside this synthesis until that review is closed.

## Evidence synthesis and boundaries

The available bulk sign/coercivity mechanisms are universal matched controls. They do not constrain the de Bruijn--Newman constant without source information ensuring that the relevant Xi blocks have controlled large-gap excursions and that external interactions cancel or are quantitatively dominated.

A viable localization may use a non-self-similar multiscale/capacitary taper with a diverging inner/outer scale ratio, source-specific signed correlation in the leakage term, overlapping windows with an exact cancellation identity, or a convergent renormalized global entropy. None is established by the current evidence.

## Status / novelty

Laguerre--Polya approximation, Cauchy semigroups, Zygmund endpoint bounds, Orlicz norms, fractional Poincare estimates, IMS-type localization, and `H^{1/2}` scale invariance are classical. The synthesis is the current scale-matching gate: **the endpoint carrier and accepted finite-amplitude bulk comparison exist, but fixed-shape localization cannot separate them from boundary leakage; source-specific or multiscale structure is still required**.

## Falsification criterion

Produce a fixed-shape self-similar cutoff in the XF-016 class whose boundary leakage is uniformly `o(1)` relative to the mesoscopic Cauchy scale under only the stated envelope/centering hypotheses, or derive an unconditional Xi-specific mesoscopic envelope/flux theorem strong enough to yield a fixed backward interval.

## Lean-formalizable core

- Fixed-time `log^2 T` gap scaling.
- `L log L` Markov contraction and endpoint Hilbert-transform transfer.
- Bounded-envelope inverse-square bulk comparison in the accepted regime.
- Exact XF-016 weighted localization identity.
- `H^{1/2}` scale-critical cutoff cost.
