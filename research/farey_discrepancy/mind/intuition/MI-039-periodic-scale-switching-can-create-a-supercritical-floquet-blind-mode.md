# MI-039 — Switched-block blindness persists to Vinogradov–Korobov-scale horizons below literal Euler coverage

**Evidence level:** exact/literature-backed synthesis from [FD-212](../../findings/FD-212-period-three-diagonal-root-depth-creates-a-source-realizable-supercritical-floquet-blind-ray.md) through [FD-223](../../findings/FD-223-vinogradov-korobov-scale-switched-blocks-remain-blind-below-literal-euler-coverage.md), interpreted against the fixed-family dichotomy of FD-210--FD-211.

The periodic schedule `q_j=(0,3,3)` has a physical super-square-root Floquet blind mode even though each instantaneous annihilator has only the harmless root `1`. FD-212--FD-221 show that exact Möbius Euler laws, bounded scheduled observations and a macroscopic earlier-prefix defect can coexist across arbitrarily long fixed blocks until a later Euler window literally covers every prime coordinate affecting the original prefix.

FD-222 proves that the obstruction survives every `J<=C log log N`. FD-223 shows that log-log growth was only the consequence of deliberately weak analytic input. Put `Phi(N)=(log N)^(3/5)/(log log N)^(1/5)`. For every fixed `0<beta<1`, there is `kappa_beta>0` such that every `J<=kappa_beta Phi(N)` admits one deterministic squarefree comparison source satisfying all Euler relations for `p<=beta N`, all switched observations bounded by `O_beta(D)` with `D asymp 2^J`, and

`X_N(N) asymp_beta N/(D log N)`.

Since `exp(O(Phi(N)))=N^(o(1))`, the entire stretched-logarithmic observation block stays subpower-small while the earlier defect remains `N^(1-o(1))`. The same positive null cycle and divisor reservoirs survive; Vinogradov--Korobov prime and Möbius estimates are strong enough to absorb the exponential reservoir and triangular-repair losses throughout this range.

The reusable distinction is now four-way: fixed panels, slowly growing panels, VK-scale growing panels, and one cofinal source are different quantifiers. Increasing observation count is not coercive while the source can be reconstructed scale by scale and the repair cost remains below the available source-cancellation budget. A successful positive theorem must identify which source freedom actually disappears rather than infer coercivity from the failure of one countermodel estimate.

**Boundary.** FD-223 still uses a comparison source depending on `N` and `J`, keeps `beta<1`, and does not prove blindness beyond a fixed multiple of `Phi(N)` or for approximate Euler laws. Exhausting the present VK estimate would be only a method boundary unless an independent theorem shows that repair is structurally impossible there. No counterexample to Möbius cancellation or RH is produced.