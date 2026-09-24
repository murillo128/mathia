# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Require an explicit source-to-response theorem before testing qutrit decoder capacity

VIS-367--VIS-407 reduce the intrinsic centered source-subspace problem to a scale-free qutrit observable and identify exact capacity tests for pre-fixed decoder classes. A fixed Lipschitz budget is equivalent to a uniform mass floor, while finite-basis or polynomial budgets imply explicit floors. VIS-407 also shows that regularity imposed in a singular invariant chart can be a coordinate artifact even when the intrinsic source path is regular.

VIS-408 closes the direct Wang-packet handoff. The actual final Wang packet class is infinite-dimensional and has no packet-uniform derivative, finite-basis, polynomial-degree or Lipschitz budget; its variational cosine optimizer is a scalar zero-pair kernel with no proved source-to-qutrit response dictionary. The missing theorem remains an intrinsic map from the Wang arithmetic source decomposition to the qutrit tangent/response object together with a target-independent complexity bound. Without that map, decoder capacity is an externally chosen representation restriction rather than arithmetic evidence.

## Test Wang small values and persistence only after the exact Gram/Haar tariffs

VIS-409--VIS-418 separate faithful representation from source selectivity. Pairwise phase portraits can be gauge-dependent, fixed shell sign patterns can be trivialized, raw balance radii contain a generic bandwidth factor, frequency-gap geometry can manufacture long quiet windows, and global translation can move those windows onto or away from a distinguished height without changing coarse spectral summaries. A selector and a shell observable must therefore be calibrated against the actual arithmetic phase law rather than against independent random phases or generic spectral intuition.

VIS-419 identifies that exact fixed-shell null: every canonical finite Wang shell is a Laurent character polynomial on the torus of its base-prime phases, and long translation is the Haar pushforward of those phases. VIS-420 prices finite-window replacement by the actual prime-log small divisors. VIS-421 removes an implicit anchoring shortcut: Wang's short-interval theorem does not itself select a canonical sparse family of heights. VIS-422 then eliminates ordinary Gram points as a fixed-shell anomaly source because every fixed finite prime-phase vector at Gram points is asymptotically Haar.

VIS-423--VIS-424 extend that comparison to growing Laurent polynomials and normalized **pointwise** amplitude. On dyadic Gram blocks, a changing observable is controlled by its Fourier/Wiener mass, frequency-weighted mass and reciprocal-frequency mass. For `X_N=|F_N|^2/M_N^2`, every fixed moment pays the explicit tariff

`W_N^(2r) [1/N + r Omega_N/log N + (log N)/(N delta_(N,r))]`.

If these tariffs vanish for every fixed `r` and the Haar law has no persistent boundary mass at the chosen threshold, every fixed continuous normalized-amplitude test, and then every fixed-threshold low-tail frequency, converges to the shell's own Haar self-null.

VIS-425 closes the ordinary fixed-radius **path persistence** loophole under the corresponding mixed-moment tariffs. For a uniformly bounded outer frequency radius `Omega_N<=Omega_*`, offsets merely rephase the same Laurent characters. Bernstein's inequality makes `u -> |F_N(z tau(u))|/S_N` uniformly Lipschitz, so `sup_(|u|<=rho)` over a fixed radius can be approximated, at any fixed accuracy, by a mesh whose size is independent of `N`. Finite collections of offsets obey the same character tariff, with the pre-cancellation structural divisor `delta^*_(N,R)`. Hence if

`W_N^(2R) [1/N + R Omega_*/log N + (log N)/(N delta^*_(N,R))] -> 0`

for every fixed `R`, every continuous fixed-radius persistence observable has the same Gram-block and Haar asymptotic. For strict near-band Wang shells `Omega_*<log 2`, and the product-ratio structure gives the explicit floor `delta^*_(N,R)>=(2Y_N)^(-2R)`. Fixed-radius persistence is therefore not an independent escape once those strengthened tariffs and Haar anti-concentration pass.

VIS-427 treats growing-window **normalized path averages** directly from the same surviving character machinery. For any radius `rho_N`, including `rho_N -> infinity`, the normalized path-power average

`J_(N,q)=(1/(2rho_N)) int_(-rho_N)^(rho_N) X_(N,u)^q du`

pays no additional radius tariff at fixed moment order: Fubini expands its moments into the same shifted Laurent characters as VIS-423--VIS-425, and the offset-box volume cancels exactly against the normalization. Its Gram/Haar discrepancy is controlled by the same `W_N`, `Omega_N` and structural-small-divisor budget. Growing path length by itself therefore cannot create an anomaly for normalized fixed-power path averages.

VIS-427 does not close growing-window suprema. A fixed-height spike can occupy a vanishing fraction of a long window when `rho_N Omega_N` grows, so every fixed-power normalized average may miss it. Approximating the supremum by taking moment order `q=q_N -> infinity` is outside the fixed-order theorem. The surviving distinction is therefore **averaged path mass versus concentration on a vanishing relative subset**, not merely fixed versus growing radius.

The live Wang question is now sharply split. For ordinary Gram points, first compute the normalized Wiener masses, mixed structural small divisors and Haar boundary concentration. If the VIS-425 tariffs pass, pointwise amplitude and fixed-radius persistence are self-null; if the corresponding fixed-order tariffs pass, VIS-427 extends the same conclusion to normalized path averages of arbitrary growing radius. A genuine escape must come from quantified tariff failure, a selector with non-Haar finite-prime phase law, localized/supremum path concentration invisible to normalized averages, growing moment order, or another destination observable not reduced by the current character machinery. None of those possibilities is established merely by growing dimension, shell complexity or visually persistent patterns.
