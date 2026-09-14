# MI-018 — Fixed algebraic CA-height corrections are governed by near-edge zero geometry; a strong hidden atom requires reciprocal-scale clustering

**Evidence level:** exact in the attained finite-edge branch through [RE-120](../../findings/RE-120-isolated-finite-zero-edges-determine-every-algebraic-ca-height-correction.md), [RE-121](../../findings/RE-121-spectral-boundary-mass-flatness-replaces-horizontal-isolation-in-ca-height-closure.md), [RE-122](../../findings/RE-122-algebraic-ca-anomalies-require-polynomial-height-zero-edge-approach.md), [RE-123](../../findings/RE-123-regular-ca-phases-resolve-the-full-subedge-packet-superalgebraically.md), and [RE-124](../../findings/RE-124-invisible-algebraic-subedge-atoms-require-near-reciprocal-ordinate-clustering.md). The required height-approach, strong-atom/diffuse-mass alternative and signed-cancellation laws are not known for zeta zeros; no claim is made for a non-attained edge or the `Theta=1` branch.

RE-119 shows that regular CA states sample the leading edge profile with phase mesh finer than every inverse power of `nu=log log C`. RE-120 then proves under a fixed horizontal gap below an attained edge that every fixed algebraic correction is already a deterministic stable-filter descendant of that same profile.

RE-121 identifies what the horizontal gap was buying. Retaining the complete high strip gives an edge hierarchy plus a damped subedge correction. If `W(t)` is the weighted mass of subedge zeros within horizontal distance `t`, its positive Laplace--Stieltjes envelope satisfies, for every fixed `A>0`,

`W(t)=O(t^A)  <=>  L(u)=O(u^-A)`.

Thus superpolynomial boundary-mass flatness preserves every fixed algebraic edge-only correction even when real parts accumulate at the edge.

RE-122 makes that condition geometric. An actual residual of size at least `c nu^-A` forces a subedge zero within horizontal distance `O(log nu/nu)` at ordinate `O(nu^A log nu)`. A finite-edge anomaly therefore needs polynomial-height spectral approach, not merely accumulation at the edge.

RE-123 shows that arithmetic placement of regular CA states does not add another fixed-order obstruction. The complete signed subedge packet has reciprocal-square zero weights. After a polynomial ordinate cutoff its phase speed is only polylogarithmic and the omitted tail is algebraically negligible, while the regular-CA phase mesh is exponentially finer. Any continuum signed excursion of fixed algebraic size is therefore sampled by actual regular CA states at the same scale.

RE-124 localizes what internal cancellation must look like when one zero is individually strong. For a target atom `rho_0` with coefficient `|a_(rho_0,K)(U)| >= cU^-A` and any fixed `eta>0`, define the neighboring ordinate cluster by

`|Im rho - Im rho_0| <= U^(-1+eta)`.

Then the target coefficient is bounded, up to `o(U^-A)`, by the maximum packet size in a window `|u-U|<=U^(1-eta/2)` plus the total coefficient mass inside that cluster. Consequently, if the nearby competing mass is `o(|a_(rho_0,K)(U)|)`, the full signed packet has an excursion comparable to the target atom; when `A<K+1`, RE-123 transfers that excursion to an actual regular CA state.

So **distant frequencies cannot hide an individually algebraically visible subedge zero**. Along an unbounded sequence, suppressing such a strong atom requires comparable coefficient mass inside ordinate windows of width `U^(-1+eta)` for every fixed `eta>0`: effectively `U^(-1+o(1))` reciprocal-scale clustering. The separate escape is genuinely diffuse algebraic mass, where no individual atom reaches the target scale and cancellation is collective rather than a local repair of one strong mode.

The reusable resource separation is now fourfold. Positive boundary mass determines whether subedge information can be algebraically visible; polynomial-height approach prices access to it; strong-atom versus diffuse allocation determines whether a local spectral witness exists; and signed correlation inside near-reciprocal clusters determines whether that witness survives. Regular CA placement is already superalgebraically fine and ordinary distant-frequency interference is no longer an independent escape.

**Boundary.** RE-124 is a localization necessity, not a zero-spacing theorem. It does not prove the required clusters exist or cannot exist, and it does not control a diffuse packet made of individually subcritical atoms. Its transfer remains fixed-order. The nonattained-edge and `Theta=1` branches remain outside this synthesis.