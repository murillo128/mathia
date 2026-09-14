# MI-018 — Fixed algebraic CA-height corrections are controlled by weighted spectral mass at the finite zero edge

**Evidence level:** exact in the attained finite-edge branch through [RE-120](../../findings/RE-120-isolated-finite-zero-edges-determine-every-algebraic-ca-height-correction.md) and [RE-121](../../findings/RE-121-spectral-boundary-mass-flatness-replaces-horizontal-isolation-in-ca-height-closure.md), building on RE-112--RE-119. The new boundary-mass flatness condition is not known for the zeta zeros; no claim is made for a non-attained edge or the `Theta=1` branch.

RE-119 shows that regular CA states sample the leading edge profile `J` with phase mesh finer than every inverse power of `nu=log log C`. RE-120 then proves under a fixed horizontal gap below an attained edge `Theta>1/2` that every fixed algebraic correction is already a deterministic stable-filter descendant of that same profile:

`B_Theta(C)=J_0(nu)+sum_(k=1)^K (-1)^k k! J_k(nu)/nu^k+O(nu^(-K-1))`.

RE-121 identifies exactly what the horizontal gap was buying. Retaining the complete high strip gives, at every fixed order `K`,

`B_Theta(C)=E_K(nu)+S_K(nu)+O(nu^(-K-1))`,

where `E_K` is the RE-120 edge hierarchy and `S_K` is the damped contribution of subedge zeros. If

`W(t)=sum_{0<Theta-Re(rho)<=t} [1/(|rho||1-rho|)+1/|1-rho|^2]`,

then `|S_K(u)|` is dominated by its positive Laplace--Stieltjes envelope

`L(u)=int e^(-ut) dW(t)`,

and for every fixed `A>0`,

`W(t)=O(t^A)  <=>  L(u)=O(u^-A)`.

Thus a fixed horizontal gap is only an extreme sufficient case. The complete RE-120 algebraic closure still holds if the weighted zero mass approaching the edge is **superpolynomially flat**, even when real parts accumulate at `Theta` with no gap at all.

The converse direction gives the useful source diagnostic. If the edge-only expansion fails at algebraic size `nu^-A`, then a definite amount of weighted zero mass must occur in a shrinking layer of width about `(A+1)log(nu)/nu`. This is a necessity statement only: phases inside that mass can still cancel, so non-flat boundary mass does not by itself create a Robin-height anomaly.

The reusable point is sharper than “near-edge zeros matter.” The endpoint sees the nonisolated spectrum through a **rate-valued boundary measure**. Spectral accumulation can be present and still be invisible to every fixed algebraic CA correction if its weighted mass is flat enough; algebraic visibility requires polynomially detectable boundary mass at the matching shrinking scale.

The remaining finite-edge question is therefore not whether horizontal isolation holds. It is whether the actual zeta spectrum satisfies enough boundary-mass flatness to close the fixed-order hierarchy, or, if it does not, whether the signed phases of the non-flat boundary layer can be controlled strongly enough to affect the Robin/CA destination rather than merely its absolute envelope.

**Boundary.** The equivalence is for the positive envelope `W/L`; it does not provide a lower bound for the signed oscillatory correction. Everything remains fixed-order in the Poincare sense. RE-121 weakens the isolation hypothesis but does not prove its replacement for zeta, sum the all-orders series, handle a non-attained edge, or resolve `Theta=1`.