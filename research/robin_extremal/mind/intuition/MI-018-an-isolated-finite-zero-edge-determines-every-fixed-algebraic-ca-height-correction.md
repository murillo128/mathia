# MI-018 — An isolated finite zero edge determines every fixed algebraic CA-height correction

**Evidence level:** exact under the additional horizontal-isolation hypothesis in [RE-120](../../findings/RE-120-isolated-finite-zero-edges-determine-every-algebraic-ca-height-correction.md), building on RE-113--RE-119. The isolation hypothesis is not known; the non-isolated near-edge boundary layer remains open.

Assume a finite attained edge `Theta>1/2` and a fixed horizontal gap `delta>0` below it. RE-119 already shows that regular CA states sample the leading edge profile `J` with phase mesh finer than every inverse power of `nu=log log C`.

RE-120 asks whether the first algebraic corrections in `1/nu` restore an independent CA selector. They do not. For every fixed `K`, the edge-normalized Robin height has the uniform expansion

`B_Theta(C)=J_0(nu)+sum_(k=1)^K (-1)^k k! J_k(nu)/nu^k+O(nu^(-K-1))`,

with `J_0=J` and

`J_k=L^k G`,

where `L f(u)=int_0^infinity e^(-(1-Theta)s)f(u+s) ds` and `G=J'+Theta J`. Thus every fixed algebraic coefficient is a deterministic stable-filter descendant of the same leading edge profile.

The mechanism is structural. Horizontal isolation makes every non-edge zero exponentially smaller in the logarithmic phase variable, while the CA selector correction beyond first order is also exponentially small. The only inverse-`nu` hierarchy comes from the reciprocal-Mertens kernel, and its coefficients are repeated applications of the same stable resolvent to `J`.

Hence **no finite algebraic order in `1/log log C` supplies a new arithmetic-placement coordinate in the isolated-edge branch**. Refining RE-119 from `o(1)` to `1/nu`, `1/nu^2`, or any fixed order cannot separate the discrete CA staircase from the continuous edge profile.

The complementary non-isolated branch is sharply localized. A zero with real part `beta=Theta-Delta` enters the edge normalization with factor `e^(-Delta nu)`, so influence at order `nu^-K` can only come from a shrinking boundary layer

`Theta-beta <=~ K log(nu)/nu`.

That near-edge zero population, rather than finite-order CA asymptotics, is the first unresolved source capable of altering the algebraic correction hierarchy.

**Boundary.** RE-120 is conditional on a fixed horizontal gap below the attained edge and gives a Poincare expansion only at each fixed order. It does not prove convergence of the full asymptotic series, handle a non-attained edge, control zeros entering the shrinking boundary layer, or resolve the `Theta=1` branch.