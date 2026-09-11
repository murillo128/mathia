# MI-008 — Inverse separation, cadence, acquisition horizon and operator order are different quantitative losses

**Evidence level:** supported by the specified inverse, sampling and propagation models; no common universal condition number is claimed.

For a finite Blaschke product `B` of fixed degree with simple zeros `a_j`, put `delta(B)=min_j product_(k!=j) rho(a_j,a_k)`, where `rho` is pseudohyperbolic distance. With output distance `Delta(B,C)=inf_(|lambda|=1)||B-lambda C||_Hinf` and bottleneck pseudohyperbolic zero matching, [AF-178](../../arithmetic_fidelity/findings/AF-178-simple-blaschke-local-condition-number-is-exactly-reciprocal-double-separation.md) gives

\[
\kappa_{\rm loc}(B)=\frac1{2\delta(B)}.
\]

Exact zero recovery survives throughout the simple stratum, while its local inverse cost diverges when this separation product tends to zero. The result is local at fixed degree and metrics; neither another metric nor an unrestricted growing-degree family inherits a uniform bound.

Dirichlet recovery has two different acquisition losses. For `F(s)=sum_n a_n n^-s`, `B_c=sum_n |a_n|n^-c<infinity`, continuous vertical averaging on `c+it`, `|t|<=T`, yields, for `N>=2`,

\[
|\widehat a_N^{\eta}(T)-a_N|
\le N^c\left(\frac{B_c}{T\log(1+1/N)}+\varepsilon_T\right).
\]

This replaces unbounded real-depth coefficient peeling by fixed-real-part observation at the cost of time breadth and noise amplification ([AF-278](../../arithmetic_fidelity/findings/AF-278-vertical-bohr-means-trade-real-depth-for-phase-time-breadth.md)). Exact recovery at each fixed `N` does not give uniform finite-`T` recovery over all `N`.

Regular vertical sampling adds a different loss before finite-horizon conditioning. [AF-279](../../arithmetic_fidelity/findings/AF-279-discrete-vertical-sampling-is-phase-pushforward-fidelity.md) shows that all bilateral samples `F(c+ikh)` determine only the pushed measure under `lambda -> e^{-ih lambda}`. A resonant cadence can therefore create exact aliases even with infinitely many samples. For ordinary Dirichlet frequencies, a nonresonant cadence makes the infinite map injective, yet every fixed window `|k|<=K` still lacks a uniform inverse modulus on the unrestricted weighted `ell^1` source ball because remote logarithmic frequencies recur arbitrarily close in wrapped phase. Exact injectivity, cadence aliasing, and finite-horizon stability are three separate statements.

Operator composition can change which estimate is needed rather than merely multiply old losses. With exponential far propagation `e^-dK`, [PF-271](../../prime_flute/findings/PF-271-separated-propagation-only-needs-sublinear-low-output-leakage.md) reduces `PBK^R` boundedness to leakage from input `[Lambda,2Lambda)` into output `[kappa,A log Lambda]`, with `A>R/d` and decay `Lambda^(-R-epsilon)`. The normalized fixed-axis source actually fails the supercritical fixed-row bound by [PF-278](../../prime_flute/findings/PF-278-mass-one-branch-forces-critical-normalized-fixed-row-leakage.md).

Keep the relevant separation, cadence fibers, observation horizon, source norm and composed frequency window explicit. None is supplied merely by exact uniqueness at an earlier stage, and there is no established theorem identifying their condition numbers across these models.
