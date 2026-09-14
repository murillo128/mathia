# MI-018 — Fixed algebraic CA-height corrections are governed by the height law of near-edge zero mass

**Evidence level:** exact in the attained finite-edge branch through [RE-120](../../findings/RE-120-isolated-finite-zero-edges-determine-every-algebraic-ca-height-correction.md), [RE-121](../../findings/RE-121-spectral-boundary-mass-flatness-replaces-horizontal-isolation-in-ca-height-closure.md), and [RE-122](../../findings/RE-122-algebraic-ca-anomalies-require-polynomial-height-zero-edge-approach.md). The resulting boundary-mass/height conditions are not known for the zeta zeros; no claim is made for a non-attained edge or the `Theta=1` branch.

RE-119 shows that regular CA states sample the leading edge profile `J` with phase mesh finer than every inverse power of `nu=log log C`. RE-120 then proves under a fixed horizontal gap below an attained edge that every fixed algebraic correction is already a deterministic stable-filter descendant of that same profile.

RE-121 identifies exactly what the horizontal gap was buying. Retaining the complete high strip gives an edge hierarchy plus a damped subedge correction. If `W(t)` is the weighted mass of subedge zeros within horizontal distance `t`, its positive Laplace--Stieltjes envelope satisfies, for every fixed `A>0`,

`W(t)=O(t^A)  <=>  L(u)=O(u^-A)`.

Thus superpolynomial boundary-mass flatness preserves every fixed algebraic edge-only correction even when real parts accumulate at the edge. Conversely, an algebraic discrepancy of size `nu^-A` requires polynomially detectable positive mass in a layer of width `O(log nu/nu)`.

RE-122 makes that condition geometric. Let `H(t)` be the least ordinate of a subedge zero within horizontal distance `t` of the attained edge. Riemann--von Mangoldt gives

`W(t) << log(e H(t))/H(t)`.

Define `kappa_H=liminf log H(t)/log(1/t)`. Then the order-`K` residual is `o(nu^-A)` for every `A<min(kappa_H,K+1)`. If `kappa_H>K+1`, the edge-only expansion through order `K` survives with its intrinsic remainder; if `kappa_H=infinity`, every fixed algebraic correction is edge-determined despite nonisolation.

The converse is the useful source diagnostic. An actual residual `>=c nu^-A` forces a subedge zero within horizontal distance `O(log nu/nu)` at ordinate `O(nu^A log nu)`, so algebraic visibility requires `kappa_H<=A`. **A finite-edge anomaly therefore needs polynomial-height spectral approach, not merely accumulation at the edge.**

This remains only an absolute-envelope gate. Polynomial-height approach creates enough positive boundary mass to be visible, but the signed oscillatory phases of those zeros can still cancel. The remaining finite-edge problem is therefore a two-resource theorem: establish or rule out the necessary height-approach regime, and if it occurs, control the signed phase packet strongly enough to affect the Robin/CA observable.

**Boundary.** The height estimate is one-way through the positive mass envelope; it does not provide a lower bound for the signed correction. Everything remains fixed-order in the Poincare sense. RE-122 does not prove a height-approach law for zeta, handle a non-attained edge, or resolve `Theta=1`.