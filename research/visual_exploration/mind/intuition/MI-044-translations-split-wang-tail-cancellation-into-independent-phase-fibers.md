# MI-044 — Translations split Wang tail cancellation into independent phase fibers

**Evidence level:** exact harmonic-analysis synthesis from [VIS-333](../../findings/VIS-333-wang-summatory-log-frequency-transfer.md), [VIS-342](../../findings/VIS-342-vk-power-gain-requires-growing-truncation-order.md), [VIS-343](../../findings/VIS-343-wang-dilate-mixture-cancellation-order.md), [VIS-344](../../findings/VIS-344-wang-translated-dilate-cancellation-fibers.md), and the finite-window refinement [VIS-345](../../findings/VIS-345-long-window-phase-resolution.md). The core conclusion below is the uniform-tail theorem; VIS-345 additionally shows that sufficiently long moving windows recover the same fiberwise moment budget.

Wang's exact log-frequency multiplier is

`m(xi)=4(1+i xi)/(4+xi^2)`.

For a finite translated-dilate bank

`M(xi)=sum_j c_j exp(-i b_j xi)m(a_j xi)`,

group components with the same translation `b`. Expanding `m(a_j xi)` in inverse powers of `xi` turns the coefficient of each order `xi^(-k)` into a finite exponential polynomial

`P_k(xi)=sum_b S_(b,k) exp(-i b xi)`,

where `S_(b,k)=sum_(j in J_b)c_j a_j^(-k)`.

If `M(xi)=O(|xi|^(-r))` uniformly as real `|xi|->infinity`, then successive multiplication by `xi^k` shows that `P_k(xi)->0` for every `k<r`. A finite exponential polynomial that decays at infinity is identically zero, so every translation fiber must independently satisfy

`S_(b,k)=0`, `k=1,...,r-1`.

The within-fiber Vandermonde argument of VIS-343 then applies without help from the other phases. If fiber `b` contains `n_b` distinct active scales, its order satisfies `r<=n_b`. With `B` active translation fibers and `N=sum_b n_b` total components,

`N>=B r`.

Thus translation diversity is not an extra uniform asymptotic smoothing currency. It partitions the moment-cancellation budget into phase fibers, each of which must pay the full order separately. Combined with VIS-342, any fixed Korobov--Vinogradov power-class gain realized through this scalar uniform-tail mechanism still demands polynomially growing scale count in every active phase fiber.

VIS-345 narrows the finite-window escape. For a fixed bank whose distinct translations have minimum spacing `Delta`, any interval of length `L` with `L Delta >= 4(B-1)` has a uniform lower frame bound for each moment polynomial. Consequently a sequence of moving windows that is long enough to resolve the translation phases and supports order-`r` decay still forces the same fiberwise moments `S_(b,k)=0` for `k<r`. Merely moving the window center is therefore not a new asymptotic resource.

The remaining finite-window mechanism must fail that phase-resolution hypothesis in a controlled way: windows can stay too short relative to the phase spacing, translations can coalesce with scale, bank size or conditioning can vary, coefficients can become frequency/source dependent, or the target can be a signed estimate for the theta remainder `G` rather than a small multiplier norm. `MI-045` records the quantitative resolution gate.

**Boundary.** VIS-344 and VIS-345 concern finite translated-dilate banks with frequency-independent coefficients. VIS-345 does not exclude short unresolved windows, shrinking translation gaps, changing poorly conditioned banks, infinite banks, adaptive/nonlinear selection or source-specific arithmetic correlations. No new bound for `G`, `Q` or the prime-number-theorem remainder follows.