# MI-003 — Fixed-time Xi memory is mesoscopic and fractional; local observables face a precision-versus-nonlocality tradeoff

**Evidence level:** supported; finite-jet obstruction is proved under the simple double-collision hypothesis, while the mesoscopic and Sobolev statements are exact for the linearized lattice model

## Core intuition

Order-one heat-time memory at high Xi height lives on a growing mesoscopic field, not in a finite collision jet or a bounded gap stencil. The universal linearized boundary model is a Cauchy/half-Laplacian flow. New results show that this is also an **observation-scale problem**: fixed-radius translation averages lose mesoscopic ordering at leading order, smooth ones see phase only at an even smaller `h^4` scale with the wrong local `k^2` symbol, while nonsmooth adjacent-gap Sobolev seminorms recover the fractional driver only by paying an endpoint tradeoff.

The first viable carrier must therefore match simultaneously the `log^2 T` spatial scale, the vanishing amplitude, and the nonlocal `|D|` geometry.

## Strongest justified principle

XF-006 rules out every robust finite collision jet as Xi-specific: polynomial real-rooted controls can approximate any fixed jet while placing their transition at an independently chosen time.

XF-007--XF-008 determine the universal fixed-time scale. With mean gap `h ~ 1/log T`, order-one memory requires `N ~ h^-2 ~ log^2 T` gaps over physical length `~log T`. On the coordinate `X=h^2 j`, the linearized symbol converges to `-2 pi |kappa|`, so the limit is the Cauchy semigroup with algebraic tails. An order-one relative profile is driven by an equilibrium defect `R-2=O(h^2)`.

XF-009 shows that every fixed-radius translation-averaged Lipschitz gap functional freezes to a pointwise value-distribution statistic up to `O(h^2)`. Equimeasurable cosine profiles are indistinguishable at leading order although their Cauchy decay rates differ. A limiting local constant therefore discards the mesoscopic phase that controls fixed-time evolution.

XF-010 sharpens smooth observables. The entire `O(h^2)` correction is a periodic coboundary and cancels under translation averaging; generic phase sensitivity first appears at `O(h^4)` and responds as `h^4 k^2`. At Xi height this is `log^-4 T`, while the dynamical driver is `log^-2 T |k|`. Smooth finite-stencil averaging is both too weak in amplitude and local in the wrong derivative order.

XF-011 identifies a real nonlinear local escape and its sharp endpoint. Adjacent-gap `W^{1,p}` seminorms are exact Lyapunov quantities for the discrete linearized Markov semigroup. After division by `h^2`, for every `1<p<infinity` they converge to `||U'||_p`, which is equivalent by the M. Riesz theorem to `|| |D|U||_p`. Thus local nonlinear differences can control the nonlocal generator after renormalization. But their raw `p`-moment scale is `h^{2p}`; the endpoint `p=1` is visible already at `h^2` yet no uniform `L^1` bound of the Cauchy driver by total variation exists because the Hilbert transform is not strongly `L^1` bounded.

## Evidence synthesis and boundaries

All of these mechanisms are universal matched controls near arithmetic equilibrium, not Xi-specific theorems. They do not classify nonlinear collision cascades, rare large defects, higher multiplicity, or global non-equilibrium zeros.

The live source input must therefore do more than control a fixed local statistic. It must supply a quantitative mesoscopic inequality in a norm/space compatible with the fractional generator, or exploit endpoint weak-type/cancellation structure strongly enough to cross the `p=1` barrier. Any import from `analytic_frontier` must be checked for block growth and error precision, not only for a better limiting constant.

## Status / novelty

Laguerre--Pólya approximation, zero ODE linearization, Cauchy semigroups, local Taylor expansion, Markov contraction, Hilbert transforms, and Sobolev norms are classical. The synthesis is the Xi scale-matching gate: **fixed-time memory requires nonlocal mesoscopic information, and local access to that information trades raw signal size against fractional-generator control**.

## Falsification criterion

Produce a fixed finite smooth stencil with leading order `h^2 |k|` phase response, or a uniform strong `L^1` estimate `|| |D|U||_1 <= C||U'||_1`, or a finite-jet Xi selector defeating XF-006 controls. A source-specific mesoscopic coercive law would evade these universal obstructions.

## Lean-formalizable core

- Fixed-radius frozen-stencil asymptotics.
- Cancellation of the smooth `h^2` term and `h^4` Hessian correction.
- Linearized Cauchy scaling.
- Adjacent-difference `W^{1,p}` contraction.
- `L^p`, `1<p<infinity`, Hilbert-transform equivalence and `p=1` endpoint failure.
