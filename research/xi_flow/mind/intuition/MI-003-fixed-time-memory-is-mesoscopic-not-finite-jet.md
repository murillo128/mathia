# MI-003 — Fixed-time Xi memory is mesoscopic and fractional; the endpoint carrier survives finite-amplitude bulk deformation

**Evidence level:** supported; finite-jet obstruction is proved under the simple double-collision hypothesis, mesoscopic scaling is exact for the linearized lattice model, and the endpoint/nonlinear coercivity statements are exact in their stated regimes

## Core intuition

Order-one heat-time memory at high Xi height lives on a growing mesoscopic field, not in a finite collision jet or bounded gap stencil. The universal linearized boundary model is a Cauchy/half-Laplacian flow. The endpoint carrier is now sharper than a pure `L^1` limit: `L log L` adjacent-gap data retain the `h^2` amplitude and control the fractional driver without a diverging Hilbert-transform constant.

The nonlinear results show that this scale is not an artifact of infinitesimal perturbation. Exact gap conductances remain Cauchy-coercive under finite-amplitude upper gap bounds. The downstream target is therefore an Xi-specific theorem preventing large-gap/flux escape on the required mesoscopic block.

## Strongest justified principle

XF-006 rules out every robust finite collision jet as Xi-specific. XF-007--XF-010 identify the fixed-time scale: `Theta(log^2 T)` gaps, physical length `Theta(log T)`, Cauchy `|D|` dynamics, and failure of fixed-radius smooth stencils to retain the required phase at the `h^2` scale.

XF-011 gives exact adjacent-gap `W^{1,p}` Lyapunovs for the linearized Markov semigroup. XF-012 shows that choosing `p_h=1+c/log(1/h)` preserves a fixed fraction of the `h^2` raw moment with only a logarithmic Hilbert-transform loss, optimal within the pure near-endpoint `L^p` route.

XF-013 changes the endpoint category. The Young function `Phi(s)=s log(e+s)` gives an exact adjacent-gap Luxemburg Lyapunov, raw scale `Theta(h^2)`, and the Zygmund endpoint bound `H:L log L->L^1` controls the Cauchy driver with an `h`-independent constant. The price is concentration sensitivity in the derivative distribution, not a diverging operator norm.

XF-014 makes positive diffusion exact for the full real-simple gap field: convex entropy dissipates in the bulk, with the only sign-indefinite term coming from interactions outside a finite block.

XF-015 then proves nonperturbative fractional coercivity. Under only `g_r<=Mh`, the exact conductances dominate `1/[M^2h^2(k-i)^2]`; small gaps cannot soften the bulk. For a mesoscopic block `N~h^-2`, the finite-block bulk variance decay rate stays order one. With two-sided envelopes the full inverse-square/Cauchy tail is quantitatively preserved.

## Evidence synthesis and boundaries

All these sign/coercivity mechanisms remain universal matched controls. They do not constrain the de Bruijn--Newman constant without source information ensuring that the relevant Xi blocks have controlled upper gaps and that external boundary flux does not overwhelm the internal dissipation.

A useful cross-line input must therefore control a `Theta(log^2 T)` block at the `h^2` scale in a norm strong enough for the Orlicz/fractional carrier **and** prevent the envelope constant from escaping through rare large gaps. Better simple-zero percentages or fixed local gap laws are insufficient unless such a transfer is proved.

## Status / novelty

Laguerre--Polya approximation, Cauchy semigroups, Pichorides/Zygmund bounds, Orlicz norms, Markov contraction, positive conductance diffusion, and fractional Poincare estimates are classical. The synthesis is the current scale-matching gate: **the endpoint carrier and finite-amplitude bulk coercivity exist; source-specific envelope and boundary control do not**.

## Falsification criterion

Produce a bounded-envelope configuration in the XF-015 regime whose bulk fractional coercivity degenerates with height, or derive an unconditional Xi-specific mesoscopic envelope/flux theorem strong enough to yield a fixed backward interval.

## Lean-formalizable core

- Fixed-time `log^2 T` gap scaling.
- `L log L` Markov contraction and Zygmund endpoint transfer.
- Exact nonlinear positive-conductance gap diffusion.
- Bounded-envelope inverse-square coercivity and mesoscopic variance rate.
