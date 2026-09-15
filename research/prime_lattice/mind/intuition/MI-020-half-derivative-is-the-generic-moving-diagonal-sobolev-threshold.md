# MI-020 — Half a derivative is the generic moving-diagonal Sobolev threshold

**Evidence level:** exact negative/sufficient boundary from [PL-316](../../findings/PL-316-critical-half-derivative-still-misses-moving-diagonal.md) and [PL-317](../../findings/PL-317-supercritical-zero-extension-forces-moving-tail-decay.md), on top of the moving Green observation isolated in [PL-314](../../findings/PL-314-moving-green-atoms-require-tail-anti-concentration.md).

The finite-`s` Green problem samples the physical logarithmic tail at a moving point `Q=r/s`. This turns ordinary global regularity into the wrong currency unless it controls the boundary trace strongly enough to suppress `m(r/s)/s`.

PL-316 shows that the zero-extension endpoint `H^{1/2}(R)` is still too weak. Sparse packets can have arbitrarily small critical norm and still satisfy `Q_n m(Q_n)=r` at selected `Q_n=r/s_n`, so the normalized moving Green transfer remains order one. The critical norm is scale-invariant under compression and proportional to packet amplitude; the moving observer multiplies that tiny amplitude by the reciprocal scale and recovers an order-one signal.

PL-317 shows that **any** positive Sobolev gain changes the mechanism. If the zero extension belongs to `H^{1/2+eta}(R)`, then for every `0<beta<min(eta,1/2)` the one-dimensional fractional Morrey embedding gives a Hölder representative that vanishes at the boundary. In logarithmic endpoint coordinates this becomes

`|m(Q)| <= C_beta exp(-beta Q)`.

Hence `Qm(Q)->0` and, more sharply, `m(r/s)/s->0` exponentially fast. The sufficient PL-314 rank-one Green limit follows automatically.

The reusable distinction is therefore **critical norm control versus boundary-trace control**. At exactly half a derivative the zero extension can carry arbitrarily small norm while hiding sparse packets at the moving observation scale. Any fixed gain beyond half a derivative forces a true zero trace and converts the exponentially compressed physical distance `1-x=2e^-Q` into exponential decay in `Q`.

For this route, searching for successively stronger unnamed Sobolev conditions at or below `1/2` is no longer useful. The live source question is whether the completed-Weil eigen-equation supplies a positive supercritical gain, or a structurally different condition that directly controls the moving samples: `m(Q)=o(1/Q)`, a critical Besov/Dini refinement, monotone or one-sided tails, an asymptotic expansion, or another source-specific anti-concentration law.

**Boundary.** The threshold is sharp only for the generic **zero-extension Sobolev sufficient-condition strategy**. PL-317 does not make `H^{1/2+eta}` necessary for Green convergence, and PL-316 does not say the actual completed-Weil mismatch realizes the sparse counterexample. Interior Sobolev regularity without the zero-extension boundary condition is also insufficient for the PL-317 argument. The arithmetic sign and rational-prime selection problem remains separate after the moving-tail gate is crossed.