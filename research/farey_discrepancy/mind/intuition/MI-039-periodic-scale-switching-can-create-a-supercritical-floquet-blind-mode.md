# MI-039 — Periodic scale switching creates a supercritical blind mode until cross-horizon prime coverage reaches the earlier prefix

**Evidence level:** exact synthesis from [FD-212](../../findings/FD-212-period-three-diagonal-root-depth-creates-a-source-realizable-supercritical-floquet-blind-ray.md) through [FD-220](../../findings/FD-220-four-horizon-wraparound-remains-blind-below-eighth-scale-euler-coverage.md), interpreted against the fixed-family dichotomy of FD-210--FD-211.

Let `Delta_A(n)=A(2n)-A(n)` and observe one dyadic root filter at each scale. FD-212 takes the periodic depth schedule `q_j=(0,3,3)`. Each instantaneous annihilator has only the harmless root `1`, yet the ordered period-three transfer has multiplier `lambda=-(7+3sqrt(5))/2=-phi^4`, giving a physical super-square-root Floquet mode at bounded filter depth. FD-213--FD-216 lift the mode to all integers and show that squarefree ternary amplitudes plus growing families of exact Möbius Euler sign laws can coexist with blindness.

FD-217 shows that one isolated horizon remains extremely permissive: for every fixed `0<theta<1`, a target-dependent source can obey the exact Euler law for every prime `p<=theta N`, keep the switched observation bounded at `N`, and still have `X_N(N) asymp_theta N/log N`. Full coverage `theta=1` instead identifies Möbius on the target prefix.

FD-218 turns persistence into a geometric overlap threshold. One **same deterministic source** can simultaneously serve horizons `N` and `2N`, satisfy all exact Euler laws through `p<=theta H` at each horizon, and retain a macroscopic summatory defect at the earlier horizon for every fixed `theta<1/2`. At `theta>=1/2`, the later cutoff reaches every prime `p<=N` and forces the earlier squarefree prefix to equal Möbius.

FD-219 shows that this survives an entire `(0,3,3)` switching period. For every fixed `theta<1/4`, one common source can serve `N,2N,4N`, obey all required Euler laws, keep the three scheduled observations bounded, and still satisfy `X_N(N) asymp_theta N/log N`. At `theta>=1/4`, the `4N` Euler window covers all primes up to `N` and forces the earlier squarefree prefix.

FD-220 crosses the first schedule wrap. At horizons `N,2N,4N,8N`, the depths are `(0,3,3,0)`, so the observation support is no longer the monotone three-horizon geometry used in FD-219. Nevertheless, for every fixed `theta<1/8`, five prime reservoirs give exact response vectors whose four high directions form a matrix of determinant `112`, and the low-prefix response satisfies

`-v_L = V (1, 3/7, 10/7, 11/7)^T`.

The positive coefficients are load-bearing: they permit simultaneous repair of all four switched observations using actual counts of high-reservoir prime flips while the low reservoir leaves an `N/log N` defect at the first horizon. At `theta>=1/8`, the `8N` Euler window reaches every prime up to `N` and again identifies the earlier Möbius prefix.

The reusable mechanism is therefore an **overlap-and-reachable-cone audit**. Relation count, local cutoff fraction, source persistence, observation support, response rank and positivity are distinct currencies. A persistent source remains blind while uncovered prime coordinates generate a positive repair cone containing the observation defect; rigidity appears when coverage closes that reservoir, unless a finite-block response cone loses the required direction earlier for an independent geometric reason.

The next problem is not to extrapolate the observed `1/2,1/4,1/8` thresholds by pattern. It is to determine whether every fixed block of the periodic schedule admits a uniform positive-reservoir construction until literal prefix coverage, or whether some later response matrix/cone fails before then.

**Boundary.** FD-220 proves the explicit four-horizon `N,2N,4N,8N` construction and its sharp eighth-scale prefix-identification threshold. It does not classify arbitrary longer schedules, prove a general reciprocal-largest-horizon threshold, or prove a Möbius theorem from approximate Euler relations. The source constructions are comparison objects, not counterexamples to Möbius cancellation or RH.