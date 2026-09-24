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

VIS-426 supplies a complementary representation-level tariff for radial motion. For the normalized coefficient representative `u_r`, its exact speed is the Fisher/covariance density,

`||u_r'||_2^2 = Upsilon_N(r)/4`.

An `L^1` bound on Fisher mass over a shell therefore controls the **average** squared displacement `||u_(r+h)-u_r||_2^2` and the measure of exceptional starting radii. At relative step `h=eta Delta_s`, the Wang-shell source bound used in VIS-426 yields mean squared displacement `O(eta^2)` in the borderline scaling. This is not a uniform pointwise persistence theorem: a small exceptional radial set can still carry large local motion.

The live Wang question is now sharply split. For ordinary Gram points and fixed-radius, uniformly band-limited shells, first compute the normalized Wiener masses, mixed structural small divisors and Haar boundary concentration; if the VIS-425 tariffs pass, pointwise amplitude and fixed-radius persistence are analytically certified self-null and need no numerical anomaly hunt. A genuine escape must come from a quantified tariff failure, a selector with non-Haar finite-prime phase law, growing persistence radius or bandwidth, or a destination theorem that can exploit the average/exceptional-set radial control of VIS-426 where uniform control is unavailable. None of those possibilities is established merely by growing dimension, shell complexity or visually persistent patterns.
