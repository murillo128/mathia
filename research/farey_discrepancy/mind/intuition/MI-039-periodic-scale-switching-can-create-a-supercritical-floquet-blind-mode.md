# MI-039 — Periodic scale switching creates a supercritical blind mode that survives almost-full one-horizon Euler coherence

**Evidence level:** exact synthesis from [FD-212](../../findings/FD-212-period-three-diagonal-root-depth-creates-a-source-realizable-supercritical-floquet-blind-ray.md) through [FD-217](../../findings/FD-217-linear-prime-cutoff-euler-coherence-remains-one-horizon-blind.md), interpreted against the fixed-family dichotomy of FD-210--FD-211.

Let `Delta_A(n)=A(2n)-A(n)` and observe one dyadic root filter at each scale. FD-212 takes the periodic depth schedule `q_j=(0,3,3)`. Each instantaneous annihilator has only the harmless root `1`, and the fixed family has gcd `1`, yet the ordered period-three transfer has multiplier `lambda=-(7+3sqrt(5))/2=-phi^4`. Its per-step modulus lies strictly between `sqrt(2)` and `2`, so the nonautonomous recurrence supports a physical super-square-root Floquet mode at bounded filter depth.

FD-213 lifts that mode from one dyadic ray to every integer because dyadic dilation preserves mantissa. FD-214--FD-215 then show that exact squarefree support, unit amplitudes and every fixed finite set of Möbius Euler sign laws can coexist with the blind mechanism. FD-216 makes the first growing-coherence statement: a horizon-indexed family can satisfy exact Euler laws at `Theta(log N)` primes while remaining blind on a target window.

FD-217 shows that the one-horizon source class is vastly more permissive than that logarithmic count suggests. For every fixed `0<theta<1`, one may impose

`xi_(pn)=-xi_n   (p<=theta N, p not| n)`

for **all** primes below the linear cutoff, preserve the squarefree ternary source, keep the selected switched observation bounded at the single target `N`, and still have `X_N(N) asymp_theta N/log N`. The construction uses the remaining macroscopic prime reservoir above `theta N` to cancel the finite response at that horizon.

There is a sharp qualitative endpoint. If the same relations are imposed for every prime `p<=N`, then every squarefree `n<=N` is generated from constrained primes and the source is forced to equal Möbius on the whole target prefix. Thus a fixed fractional cutoff remains relaxable, while full target-prefix coverage removes the one-horizon freedom.

The decisive currency is therefore **persistence across horizons**, not local prime count. A target-dependent source can absorb nearly all prime constraints below the horizon because the unconstrained reservoir can be reselected at each `N`. That does not produce one globally compatible source. To defeat the switched blind mode without assuming Möbius outright, a physical Farey observable must couple enough neighboring scales that those reservoir choices cannot be independently retuned, or prove another same-source compatibility law of comparable force.

The reusable mechanism is a quantifier audit. Local source fidelity can be arbitrarily rich while still failing to constrain a target if the admissible source is allowed to change with the target. Before treating a growing family of exact relations as coercive, ask whether they are enforced on one persistent object and whether their overlap across scales has a quantitative cost.

**Boundary.** FD-217 is a one-horizon statement; FD-216 retains stronger target-window uniformity. Neither is a Möbius counterexample. The fixed-ratio theorem does not classify a shrinking cutoff `theta_N->1`, and the exact endpoint `theta=1` should not be interpolated without additional prime-distribution and compatibility arguments. No RH consequence is claimed.