# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Find a selector-sensitive source invariant between one boundary charge and coefficient-by-coefficient Euler recovery

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-042-subcritical-euler-jet-depth-does-not-change-the-leading-kv-sign-complexity-exponent`.

RE-153--RE-168 identify the Pareto-weighted Chebyshev-deficit destination and quantify how much post-selector Robin motion remains possible under quantitative Korobov--Vinogradov source fidelity. The intrinsic decay length `ell_KV(T)=log T/V(T)` gives the spatial capacity scale: a bounded-multiplicative or subpower region can still carry order-one normalized displacement while enough future capacity remains.

RE-169 identifies Mertens normalization as an exact conservation law for the same Robin kernel. RE-170--RE-171 show that exact global charge does not localize it over flexible generalized sources. RE-172 adds finite ordinary-prime rigidity, but RE-173 proves that this is compactness rigidity: an infinite `{0,1,2}` delete/duplicate tail on ordinary prime labels can match `Gamma=gamma` exactly, stay below every fixed KV envelope and still create an order-one transient Robin excursion.

RE-174 closes the opposite extreme. For any bounded multiplicity perturbation on ordinary primes, an unbounded exact high-temperature Euler profile identifies every multiplicity, because the first changed prime dominates `D_Q(sigma)` as `sigma->infinity`. That source fingerprint is exact but exponentially ill-conditioned at the Robin scale.

RE-175 finds a cheaper intermediate diagnostic. The right boundary jets of the Euler discrepancy at `s=1` are weighted log-prime moments with kernels `J_j(q)~(-1)^j(log q)^j/q`. Matching the Mertens value and the first `K` derivatives forces at least `K+1` sign changes in any sufficiently far-out nonzero multiplicity perturbation. For the RE-173 control, the first slope already detects the delayed compensator at exactly the Robin normalization.

RE-176 turns that qualitative extra sign change into a quantitative placement cost for the minimal `- + -` escape. RE-177 removes the terminal one-sign restriction: if the residual tail begins at `Y` and has `M` maximal sign-constant phases, exact Mertens plus first-slope matching forces

`sqrt(p) log(p) (M + ell_KV(Y)) e^(-b V(Y)) >> 1`.

Thus subpolynomial `M` does not move the leading `bV(Y)=(1/2)log p` horizon, while delaying the repair beyond `(1/2+delta)log p` costs at least polynomially many sign phases.

RE-178 now closes the simplest higher-jet upgrade. For jet order `j=o(V(Y))`, scalar tail capacity satisfies

`sum_(q>=Y)|c_q||J_j(q)| << (log Y)^(j-1)(M+ell_KV(Y))e^(-bV(Y))`.

Higher derivatives increase the logarithmic location weight but leave sign-phase dependence linear. At the RE-177 horizon, after selector normalization by `(log p)^(j-1)`, every fixed jet family and even every `j=o(log p/log log p)` contributes only `p^(o(1))` additional leverage. The same scalar Abel/KV method therefore cannot improve the leading polynomial distance-versus-sign-complexity exponent below the crossover

`j_cap(p) asymp log p/log log p`.

The live matched-control escape is still high/infinite oscillatory complexity, but the next useful theorem can no longer be “add a few more scalar Euler derivatives.” A real strengthening must exploit **joint moment geometry across jets**, reach a genuinely growing derivative family near/above the crossover with independently justified debts, use ordinary-prime/integer-multiplicity structure that scalar capacity ignores, or derive a selector-native source invariant rather than impose more matched moments.

This still does **not** make any Euler boundary jet a free invariant of the original Robin problem. RE-175--RE-178 state what additional source coordinates would force and where the scalar-capacity method saturates. Any closure must explain why such information follows from genuine arithmetic input rather than being an extra hypothesis.

## Control one-sided vertical reciprocal escape without overstating the symmetric obstruction

RE-144--RE-152 put the zero-side packet into reciprocal-scale language and show that one-sided vertical phase geometry can hide a scale-maximal target at lacunary stages while fixed-order global local-correlation statistics remain unchanged. A closure theorem on this branch still needs target-conditioned exceptional geometry rather than typical-center averages.

## Keep source capacity, exact identification, jet depth and usable conditioning distinct

Quantitative PNT/KV fidelity, exact Mertens normalization, ordinary-prime support, integer multiplicity, finite/growing Euler boundary jets, the full high-temperature Euler germ and the zero-side packet obstruction answer different questions. RE-173 shows strong coarse fidelity plus one exact boundary charge is non-rigid; RE-174 shows an unbounded exact Euler hierarchy is fully rigid but exponentially ill-conditioned; RE-175--RE-177 show that one extra slope detects and spatially prices the known compensation by sign complexity; RE-178 shows that subcritical scalar jet depth does not improve the leading exponent because each additional derivative only supplies logarithmic leverage while each sign phase still contributes linearly.

Future matched controls must therefore state **what source ambiguity survives, how many sign alternations it uses, how many genuinely joint source moments are available, and at what selector-normalized precision/placement cost** before source rigidity is credited as Robin leverage.