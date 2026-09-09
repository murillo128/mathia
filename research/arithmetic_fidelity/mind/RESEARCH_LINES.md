# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Separate positive Peano-cone transfer from signed-source conditioning

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-195--AF-205 identify the exact fixed-order transfer geometry. Minimal-support moment-flat controls are Peano B-spline/divided-difference carriers, and for every fixed cancellation order `m` the minimal `m+1`-node Euler transfer is two-sided comparable to the product of the scale-free source shape factor and the profile-weighted localization functional. The quartic five-node calibration is therefore an instance of an all-order mechanism rather than a special accident.

AF-206 supplies the positive boundary: higher convex order is equivalent to nonnegative order-`m` Peano kernel, and inside that cone the fixed-band transfer is an exact positive Peano expectation. AF-207--AF-208 show why this does not extend to unrestricted signed carriers. Signed Peano mass admits fixed-band approximate nulls even with compact support, so source localization and exact injectivity alone do not give uniform coercivity.

AF-209--AF-210 isolate the correct recovery resource. Every positive-width Euler band is injective on the unrestricted density class modulo the anchor atom, but quantitative recovery is restored only after a compactness/complexity restriction such as bounded variation; on a precompact normalized source class, finitely many frequencies already form an approximate norming set. Thus infinite observation bandwidth is not the missing ingredient once the source category is compact.

AF-211--AF-212 then quantify how severe the conditioning loss is as source complexity grows. The optimal BV lower modulus decays faster than every algebraic power, and Gevrey controls sharpen this to stretched-exponential decay `exp(-c M^alpha)` for every fixed `alpha<1`. Exact injectivity can therefore coexist with almost-exponential instability along a natural source exhaustion.

The live question is no longer to generalize the quartic calculation. It is to identify **source-forced arithmetic complexity or positivity constraints** under which the exact Peano transfer law yields a useful quantitative modulus, and to state how that modulus scales with the actual source class. A recovery theorem should declare cancellation order, positivity/sign category, localization/profile scale, complexity budget, and observation band together.

## Solve extremals only inside the declared transfer category

The homogeneous Peano shape functional remains useful for classifying minimal-support source geometry, but AF-200 and the later fixed-band results show that shape optimization without the observation/localization gate can optimize the wrong problem. Positive Peano carriers, signed BV classes, and other source categories have fundamentally different conditioning laws.

Future extremal statements should therefore optimize the actual transfer resource inside a declared source class. A sharp `Q_m` constant, a transport-distance bound, or an exact finite-dimensional sufficiency statement is not by itself a stable-recovery theorem unless it controls the observation-specific lower modulus.

## Keep provenance and endpoint sufficiency separate from conditioning

A representation can be exactly sufficient yet lose source identity after quotienting, or preserve provenance while becoming arbitrarily ill-conditioned on an expanding source class. Recovery claims should state separately what is reconstructible, which equivalences are harmless, which source carrier remains localized, and at what quantitative cost the inverse stays stable.