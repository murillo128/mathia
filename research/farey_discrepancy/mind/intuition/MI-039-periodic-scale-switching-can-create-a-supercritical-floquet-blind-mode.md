# MI-039 — Periodic scale switching creates an all-integer supercritical blind mode from individually harmless filters

**Evidence level:** exact synthesis from [FD-212](../../findings/FD-212-period-three-diagonal-root-depth-creates-a-source-realizable-supercritical-floquet-blind-ray.md) and [FD-213](../../findings/FD-213-dyadic-band-profile-lifting-preserves-all-integer-switched-blindness.md), interpreted against the fixed-family dichotomy of FD-210--FD-211.

Let `Delta_A(n)=A(2n)-A(n)` and observe one dyadic root filter at each scale. FD-212 takes the periodic depth schedule `q_j=(0,3,3)` on powers of two. Each instantaneous annihilator has only the harmless root `1`, and the fixed family has gcd `1`, yet the ordered period-three transfer has multiplier

`lambda=-(7+3sqrt(5))/2=-phi^4`,

whose per-step modulus `rho=phi^(4/3)` satisfies `sqrt(2)<rho<2`. The nonautonomous recurrence therefore supports a physical super-square-root Floquet mode at bounded filter depth and critical random cost.

FD-213 shows that this is not merely a sparse-ray artifact. Dyadic dilation preserves the mantissa

`t(n)=n/2^floor(log_2 n)`.

If `(a_j)` is the scale-index Floquet mode and `h:[1,2]->R` is Lipschitz with `h(1)=h(2)=0`, then

`A(n)=epsilon a_(floor(log_2 n)) h(t(n))`

inherits the switched recurrence on every integer because dilation changes only the scale index. The endpoint zeros of `h` make adjacent-band increments uniformly bounded when `rho<2`. Hence FD-213 constructs a real bounded source for which the selected switched filter vanishes **for every integer** while `|A(N_m)| asymp N_m^alpha` on explicit interior band points, with `alpha≈0.9256558848>1/2`.

The durable mechanism is a fibre decomposition. An all-integer diagonal criterion need not add cross-ray information when its dilation operator preserves an auxiliary coordinate exactly. Here the mantissa fibres carry independent copies of the same scale recurrence, and a vanishing boundary profile stitches them into one bounded-increment source without destroying the blind mode.

The remaining arithmetic discriminator must therefore couple those fibres or forbid the lifted source for a reason absent from bounded-increment geometry—for example squarefree support, multiplicativity, or another exact Möbius relation. Another argument based only on all-integer sampling, bounded source increments, fixed-family gcds or instantaneous filter spectra cannot eliminate the FD-213 mode.

**Boundary.** FD-213 is a bounded-source representation countermodel, not a Möbius counterexample. It does not show that a multiplicative or squarefree-supported source can realize the profile-lifted mode, nor classify arbitrary switched schedules. Its exact content is that additive/summatory coherence plus all-integer diagonal observation still does not restore square-root completeness for this nonautonomous sensor.
