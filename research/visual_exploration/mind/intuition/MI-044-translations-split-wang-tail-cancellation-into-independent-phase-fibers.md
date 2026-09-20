# MI-044 — Translations split Wang tail cancellation into independent phase fibers

**Evidence level:** exact harmonic-analysis synthesis from [VIS-333](../../findings/VIS-333-wang-summatory-log-frequency-transfer.md), [VIS-342](../../findings/VIS-342-vk-power-gain-requires-growing-truncation-order.md), [VIS-343](../../findings/VIS-343-wang-dilate-mixture-cancellation-order.md), and [VIS-344](../../findings/VIS-344-wang-translated-dilate-cancellation-fibers.md). The conclusion is for uniform real-frequency polynomial tail decay of finite translated-dilate banks with frequency-independent coefficients; it does not classify moving windows or adaptive coefficients.

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

The genuine remaining escape is qualitative rather than another constant-weight asymptotic bank: a moving or finite frequency window where different phases can interfere locally, coefficients depending on frequency or source data, or a signed arithmetic estimate for the theta remainder `G` that is not equivalent to uniform multiplier-tail cancellation. Such an escape must state the window and admissible coefficient dependence before inspecting the data and then survive the exact source and derivative-repayment quotients.

**Boundary.** Cross-phase interference can be substantial on finite intervals, so VIS-344 does not imply fiberwise cancellation there. Nor does it cover infinite banks, frequency-dependent coefficients, adaptive/nonlinear packet selection or source-specific arithmetic correlations. The result isolates only the uniform polynomial tail mechanism; no new bound for `G`, `Q` or the prime-number-theorem remainder follows.