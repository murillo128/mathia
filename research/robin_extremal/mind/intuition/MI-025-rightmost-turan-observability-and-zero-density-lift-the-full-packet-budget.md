# MI-025 — Rightmost Turán observability removes horizontal spread; zero density lifts the full-packet tail budget

**Evidence level:** exact/literature-derived finite-packet observability from [RE-139](../../findings/RE-139-turan-power-sums-remove-the-horizontal-spread-tax-from-rightmost-robin-packets.md), full-core/tail splice from [RE-140](../../findings/RE-140-full-packet-turan-closure-has-a-rightmost-gain-complexity-budget.md), and zero-density tail improvement from [RE-141](../../findings/RE-141-zero-density-lifts-the-full-packet-tail-budget.md)

RE-137--RE-138 used Turán--Nazarov propagation from an external anchor. For actual zeta zeros that route showed that superalgebraic hiding of a selected leading packet requires large scaled horizontal spread and/or unbounded absolute vertical span.

RE-139 removes the horizontal-spread alternative for finite packets. Normalize at a rightmost horizontal atom `rho_*`. Every sampled power-sum root then lies in the closed unit disk, while the Robin coefficients have uniformly positive real part. Turán's Second Main Theorem searches directly inside the observation window and gives, for a packet of `N` positive-ordinate modes,

`sup |S_(C,0)| >= c_(Theta,kappa) exp(-C_kappa N) |a_(rho_*,0)(U)|`,

with no horizontal-spread or vertical-diameter penalty. For actual zeta zeros, Riemann--von Mangoldt converts `N` into absolute vertical span. Hence superalgebraic finite-packet hiding forces the absolute vertical span to diverge; horizontal drift to the left of a rightmost atom is not an independent hiding resource.

RE-140 performs the exact finite-core/full-tail splice. Truncate at height `T`, let `N_T` be the core size, compare the rightmost core amplitude with a strong reference atom by `G(U,T)`, and put `Lambda_kappa=2 log(16e/kappa)`. The finite witness contributes at scale

`G(U,T) exp(-Lambda_kappa N_T) M_0(U)`.

With only the global absolute zero tail, this had to beat `log T/T`.

RE-141 uses the defining off-critical strip information in the correct place. Ingham zero density plus the Robin `gamma^-2` coefficient and horizontal damping gives, for every `epsilon>0`,

`||S_0-S_(0,T)||_infty << T^(-2+nu_I(Theta)+epsilon)(log T)^C + exp(-c_epsilon U) log T/T`,

where `nu_I(Theta)=3(1-Theta)/(2-Theta)<1`. Thus for a polynomial cutoff `T=U^B`, strong-atom exponent `A`, amplitude loss `G>=T^-eta` and effective mode count `N_T<=alpha log T`, the sufficient budget becomes

`A/B + eta + Lambda_kappa alpha < 2-nu_I(Theta) = (1+Theta)/(2-Theta)`.

This is a strict improvement over the former right-hand side `1` for every attained edge `Theta>1/2`. The gain comes from using zero density to suppress the **exterior tail**, not by inserting a polynomial zero-count directly into an exponential Turán cardinality penalty.

The improvement still does not close the full packet. The geometry-free rightmost comparison has `eta=2`, while `2-nu_I(Theta)<2` for every `Theta<1`; even with negligible strong-atom and mode-count costs, that crude transfer misses the budget. Effective finite-core complexity is also still open. The remaining source theorem must therefore improve rightmost amplitude/height transfer, reduce the effective Turán mode count, sharpen the signed tail further, or bypass truncation with an infinite-packet observability theorem.

The reusable distinction is now three-way: **finite observability, source-weighted exterior suppression, and retained-core complexity/amplitude transfer**. A source theorem may be useless when charged as raw mode count yet decisive when inserted into a coefficient-weighted tail. Conversely, a much smaller tail does not repair a core lower bound whose rightmost anchor loses too much amplitude.

**Boundary.** RE-139--RE-141 concern the leading attained-edge Robin packet and provide sufficient certificates. They do not prove actual exterior cancellation, a useful effective-mode theorem, or RH. The tail estimate remains absolute; better signed cancellation or a source-specific rightmost theorem could improve the budget further.