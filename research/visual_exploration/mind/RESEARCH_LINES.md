# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Require an explicit source-to-response theorem before testing qutrit decoder capacity

VIS-367--VIS-407 reduce the intrinsic centered source-subspace problem to a scale-free qutrit observable and identify exact capacity tests for pre-fixed decoder classes. In particular, a fixed Lipschitz budget is equivalent to a uniform mass floor, while finite-basis or polynomial budgets imply explicit floors. VIS-407 also shows that regularity imposed in a singular invariant chart can be a coordinate artifact even when the intrinsic source path is regular.

VIS-408 closes the direct Wang-packet handoff. The actual final Wang packet class is infinite-dimensional and has no packet-uniform derivative, finite-basis, polynomial-degree or Lipschitz budget; its variational cosine optimizer is a scalar zero-pair kernel with no proved source-to-qutrit response dictionary. The missing theorem is therefore an intrinsic map from the Wang arithmetic source decomposition to the qutrit tangent/response object together with a target-independent complexity bound on that map. Without that map, decoder capacity is an externally chosen representation restriction rather than arithmetic evidence.

## Test bandwidth-normalized Wang small values only against selectors and growing observables that survive the Gram/Haar tariff

VIS-409--VIS-411 separate faithful representation from new source structure. A one-shell Wigner portrait is equivalent to the same rank-one state; a full cross-Wigner matrix for genuinely separate shells retains already-present labelled coherence; and for projective shell data the representative phases quotient to Bargmann cycle holonomies. Pairwise interference phases are therefore not intrinsic unless the source fixes representatives, while closed-cycle products are the first phase-sensitive gauge invariants.

The subsequent Wang analysis removes the simplest way such cycle structure could become selective. Constant finite-shell sign patterns can be gauge-trivialized, so their apparent frustration does not by itself define source-rigid arithmetic holonomy. VIS-415 supplies a local sign-change certificate from the shell margin and coefficient derivative budget.

VIS-416 separates the generic spectral scale from the candidate source-dependent part. For a finite Wang shell `F_i` with frequency radius `Omega_i` and real-axis sup norm `M_i`, Bernstein's inequality gives `||F_i'||_infinity<=Omega_i M_i`. Thus the coefficient-free certified balance radius is `beta_i(T)=a_i(T)/Omega_i`, where `a_i(T)=|F_i(T)|/M_i`. A shrinking raw balance radius can therefore be caused solely by increasing bandwidth.

VIS-417 shows that bandwidth normalization is still not a complete matched control: fixed outer bandwidth, mode count, coefficient magnitudes, long-time energy and global supremum can coexist with arbitrarily long quiet windows when a frequency gap shrinks. VIS-418 closes the next loophole: even when the complete frequency set and its gap are fixed, global translation moves a quiet interval onto or away from any prescribed height without changing those spectral summaries. Existence of quiet windows and alignment with a distinguished arithmetic height are therefore different observables.

VIS-419 resolves the fixed-shell calibration problem exactly. Every canonical finite Wang shell is a Laurent character polynomial on the torus of its **base-prime phases**, and long translation of that same realized shell is exactly the Haar pushforward of those prime phases for bounded continuous fixed-shell observables. Ratio-mode phases retain their induced character dependencies; independently randomizing every ratio frequency is generally an invalid null.

VIS-420 supplies the quantitative finite-window gate. If `G(z)=sum_m c_m z^m` and `nu_m=sum_p m_p log p`, translation averaging differs from Haar by the exact sinc-weighted nonzero-character sum, with error controlled by the active small divisors `|nu_m|`. Fixed-window calibration is therefore governed by the actual prime-log character lattice, not just mode count, outer bandwidth or coefficient norm.

VIS-421 removes the implicit source-anchoring shortcut. Wang's short-interval setup treats `T` as a generic asymptotic interval start and does not itself select a canonical sparse family of heights. Any anomaly panel must therefore use a selector justified independently of the observed shell values and a pre-specified rule transporting shell scale, normalization and persistence radius across heights. If the selector comes from another zeta structure, the claim is cross-structure alignment rather than intrinsic Wang anchoring.

VIS-422 disposes of ordinary Gram points in the **fixed-shell** regime. Existing discrete-universality prior art gives Haar equidistribution of every fixed finite prime-phase vector at Gram points. Combined with VIS-419, every frozen finite Wang shell sampled at Gram points has the same asymptotic normalized-amplitude law as its exact prime-torus Haar self-null, as does every fixed-radius continuous persistence statistic. Arithmetic sparsity of the selector alone therefore gives no fixed-shell anomaly.

VIS-423 closes a nontrivial part of the growing-shell escape. On a dyadic Gram block, a character `exp(i alpha g_k)` obeys the explicit tariff

`|E_N(alpha)| <= C(1/N + |alpha|/log N + (log N)/(N|alpha|))`.

For a changing Laurent polynomial with nonzero character frequencies `nu_m=sum_p m_p log p`, the Gram-block deviation from its own Haar mean is controlled by three Fourier budgets: total coefficient mass `A_0`, frequency-weighted mass `A_1`, and reciprocal-frequency mass `A_(-1)`. In particular `A_0=o(N)`, `A_1=o(log N)` and `A_(-1)=o(N/log N)` force convergence to the Haar mean even while the prime support and character set grow. Thus a growing shell does not escape the Gram/Haar null merely by increasing dimension; it must carry excessive Fourier mass, high-frequency mass, a genuine prime-log small-divisor burden, or an observable not controlled by this tariff.

VIS-424 removes normalized pointwise amplitude as an unspecified nonlinear escape. For `X_N=|F_N|^2/M_N^2`, every fixed moment `X_N^r` remains in the same Laurent algebra with Wiener mass at most `W_N^(2r)`, frequency radius at most `2r Omega_N`, and smallest surviving nonzero frequency `delta_(N,r)`. Applying VIS-423 moment by moment gives the sufficient tariff

`W_N^(2r) [1/N + r Omega_N/log N + (log N)/(N delta_(N,r))] -> 0`

for each fixed `r`. Under these bounds, every fixed continuous function of normalized amplitude has the same asymptotic Gram and Haar averages. Fixed-threshold low-tail frequencies follow as well once the Haar self-null has uniform boundary anti-concentration at the threshold. The real costs are therefore the normalized Wiener mass, outer character scale, fixed-order prime-log small divisors and threshold anti-concentration; the absolute value or modulus alone is not a new source resource.

The live source question is now more specific. For a proposed Gram-point **pointwise normalized-amplitude** anomaly, compute `W_N`, `Omega_N`, the fixed-order `delta_(N,r)`, and the Haar boundary mass. If the VIS-424 tariffs vanish and the threshold is uniformly non-concentrated, both continuous amplitude tests and fixed-threshold low-tail frequencies are analytically certified Haar and the route closes without numerical testing. A failure of one of those gates is only a candidate source resource and must itself be derived from the Wang shell rather than inferred from growing dimension.

The path-valued persistence statistic `sup_(|u|<=rho)|F_N(T+u)|/M_N` remains outside VIS-424: it is not a scalar function of `X_N(T)` and still requires a uniform path approximation or stability theorem. More generally, the remaining open categories are a selector whose finite-prime phase law is genuinely non-Haar, a quantified failure of the VIS-424 moment/anti-concentration conditions, or a persistence/path observable whose growing-family Gram/Haar comparison cannot be reduced to those scalar moments. Any positive result would establish only a source-sensitive or cross-structure phase-alignment channel, not an RH mechanism.
