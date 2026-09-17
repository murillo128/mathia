# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Find a selector-sensitive source invariant between one boundary charge and coefficient-by-coefficient Euler recovery

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-041-remote-two-jet-repair-trades-kv-distance-for-sign-phase-complexity`.

RE-153--RE-168 identify the Pareto-weighted Chebyshev-deficit destination and quantify how much post-selector Robin motion remains possible under quantitative Korobov--Vinogradov source fidelity. The intrinsic decay length `ell_KV(T)=log T/V(T)` gives the spatial capacity scale: a bounded-multiplicative or subpower region can still carry order-one normalized displacement while enough future capacity remains.

RE-169 identifies Mertens normalization as an exact conservation law for the same Robin kernel. RE-170--RE-171 show that exact global charge does not localize it over flexible generalized sources. RE-172 adds finite ordinary-prime rigidity, but RE-173 proves that this is compactness rigidity: an infinite `{0,1,2}` delete/duplicate tail on ordinary prime labels can match `Gamma=gamma` exactly, stay below every fixed KV envelope and still create an order-one transient Robin excursion.

RE-174 closes the opposite extreme. For any bounded multiplicity perturbation on ordinary primes, an unbounded exact high-temperature Euler profile identifies every multiplicity, because the first changed prime dominates `D_Q(sigma)` as `sigma->infinity`. That source fingerprint is exact but exponentially ill-conditioned at the Robin scale.

RE-175 finds a materially cheaper intermediate diagnostic. The right boundary jets of the Euler discrepancy at `s=1` are weighted log-prime moments with kernels `J_j(q)~(-1)^j(log q)^j/q`. Matching the Mertens value and the first `K` derivatives forces at least `K+1` sign changes in any sufficiently far-out nonzero multiplicity perturbation. For the specific one-sign-change RE-173 control, the first slope already satisfies

`|D_Q'(1+)| >= (log(16/3)-o(1)) d_p ~ 1/(sqrt(p) log p)`,

exactly the normalization of its order-one Robin excursion. The delayed compensator is therefore visible without coefficient-by-coefficient high-temperature recovery.

RE-176 turns that qualitative extra sign change into a quantitative placement cost for the minimal `- + -` escape. If the original RE-173 deletion packet lies near `p`, the positive compensating phase begins at a fixed multiple beyond it, the terminal negative phase begins at `Y`, the Mertens charge and first boundary slope both match exactly, and the source discrepancy obeys the same KV envelope, then the terminal one-sign tail must carry a fixed first-slope debt. Its available capacity beyond `Y` is only

`ell_KV(Y) e^(-b V(Y))`,

so necessarily

`sqrt(p) log(p) ell_KV(Y) e^(-b V(Y)) >>_b 1`,

and hence `b V(Y) <= (1/2+o(1)) log p`. The second sign change cannot be exiled arbitrarily far while retaining two-jet matching and KV fidelity. Distance can reduce the required Mertens mass, but it cannot erase the first-slope workload.

RE-177 removes the terminal one-sign restriction for tails of finite sign complexity. If the first positive compensating phase is completed before `Y` and the residual tail has `M` maximal sign-constant phases, exact Mertens plus first-slope matching leaves a centered Euler debt of order `d_p`, while the KV envelope gives only

`(M + ell_KV(Y)) e^(-b V(Y))`

of absolute first-slope capacity. Therefore

`sqrt(p) log(p) (M + ell_KV(Y)) e^(-b V(Y)) >> 1`.

In particular, `M=p^(o(1))` does not move the leading `bV(Y)=(1/2)log p` horizon, while delaying the repair to `bV(Y)>=(1/2+delta)log p` forces `M>=p^(delta-o(1))`. The live matched-control escape is now **high sign complexity**: polynomially many or infinitely many alternating phases, or an architecture that starts interlacing signs before a separated first positive phase can be isolated. A useful next test is whether higher boundary jets or ordinary-prime integer granularity impose a superlinear complexity tariff on such oscillatory repairs.

This still does **not** make the first slope a free invariant of the original Robin problem. RE-175--RE-177 state what one additional source coordinate would force. Any closure must also explain why the required boundary-jet information follows from genuine arithmetic input rather than being imposed as an extra hypothesis.

## Control one-sided vertical reciprocal escape without overstating the symmetric obstruction

RE-144--RE-152 put the zero-side packet into reciprocal-scale language and show that one-sided vertical phase geometry can hide a scale-maximal target at lacunary stages while fixed-order global local-correlation statistics remain unchanged. A closure theorem on this branch still needs target-conditioned exceptional geometry rather than typical-center averages.

## Keep source capacity, exact identification and usable conditioning distinct

Quantitative PNT/KV fidelity, exact Mertens normalization, ordinary-prime support, integer multiplicity, finite Euler boundary jets, the full high-temperature Euler germ and the zero-side packet obstruction answer different questions. RE-173 shows strong coarse fidelity plus one exact boundary charge is non-rigid; RE-174 shows an unbounded exact Euler hierarchy is fully rigid but exponentially ill-conditioned; RE-175 shows that an intermediate finite boundary observable can detect the known delayed-compensation control at the Robin scale; RE-176 prices the remote placement of the minimal two-sign-change repair; and RE-177 shows that bounded or subpolynomial later sign complexity cannot improve that leading placement horizon. Future matched controls must state both **what source ambiguity survives, how many sign alternations it uses, and at what selector-normalized precision/placement cost** before source rigidity is credited as Robin leverage.