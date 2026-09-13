# MI-034 — A sub-boundary profile cap makes quartic Euler minimization equicoercive

**Evidence level:** exact on the five-node quartic source class through [AF-319](../../findings/AF-319-profile-capped-quartic-euler-minimizers-converge-to-the-certified-homogeneous-optimizer.md), using the certified AF-198 optimizer/boundary input. The cap is an extra source restriction; unrestricted full-Euler sublevels can still escape as in AF-200.

Let `Q=M_4/W_1^4` be the scale-free quartic profile. The certified homogeneous problem has a unique projective minimizer

`q_*=[1:t_*:t_*:1]`, with `9 t_*^3-5 t_*^2-7 t_*-1=0`,

and every normalized shape approaching a collision face has `Q>=3`, while `Q_*<2.891`. Therefore any fixed cap `Q_*<C<3` defines a compact projective class `K_C={Q<=C}`.

That compactness is exactly the missing non-escape needed to transfer the homogeneous optimizer to the physical fixed-band Euler problem. If `J_delta(q)` is the Euler objective normalized by `delta^4` after scaling to `W_1=delta`, then on `K_C`

`sup_q |J_delta(q)-c_(x,sigma,T) Q(q)| <= (L_5/8) C^2 delta`.

Hence every minimizer `q_delta` of `J_delta` on `K_C` converges projectively to `q_*`; moreover `Q(q_delta)-Q_*=O(delta)` and local projective coordinates converge at `O(sqrt(delta))` from the positive-definite Hessian.

The reusable point is not merely that one optimizer converges. **A profile bound below the certified boundary level simultaneously buys projective compactness and physical localization**, so uniform asymptotic expansion becomes strong enough to transfer minimizers. Without such a source-side non-escape resource, pointwise asymptotics do not prevent shapes from escaping into regions where the homogeneous model no longer controls the physical objective.

**Boundary.** AF-319 does not show that the arithmetic source naturally satisfies `Q<C<3`. The remaining conceptual question is whether an independently motivated source constraint yields such a profile cap, or an alternative equicoercive condition, rather than imposing it solely to recover the homogeneous optimizer.