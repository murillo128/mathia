# VIS-110 — bounded-lag higher-order correlation remains a finite-block statistic

## Claim

Let `x=(x_0,...,x_(N-1))` be a finite sequence, let

`0=t_0<=t_1<=...<=t_(q-1)=r<N`,

and let `f` be any fixed function of the selected coordinates. Define the bounded-lag cylinder sum

`M_x(f;t_0,...,t_(q-1)) = sum_(j=0)^(N-1-r) f(x_(j+t_0),...,x_(j+t_(q-1))).`

Then `M_x` is determined exactly by the unordered multiset of length-`(r+1)` blocks of `x`. If `N_x(u)` denotes the number of occurrences of the block

`u=(u_0,...,u_r)`,

then

`M_x = sum_u N_x(u) f(u_(t_0),...,u_(t_(q-1))).`

Consequently every finite collection of higher-order correlation coordinates whose maximum lag is bounded by a fixed `R` factors through the empirical length-`(R+1)` block inventory. Any deterministic scalar, vector, visualization, classifier, or decision rule that consumes only that finite collection also factors through the same finite local quotient.

For the third-order correlation of `VIS-109`,

`C_x(k,l)=sum_(j=0)^(N-1-max(k,l)) x_j x_(j+k) x_(j+l)`,

`C_x(k,l)` is therefore exactly a length-`(max(k,l)+1)` block statistic. In particular, the new span-four coefficient from `VIS-109` is not global chronology: it is a linear functional of the length-five block inventory. Relative to the exact order-three Markov-type quotient of `VIS-099`, span four is the **first unforced local layer**, not an escape from the finite-block hierarchy.

The explicit homometric pair from `VIS-108` makes this boundary concrete. Its length-four block multisets agree, but its length-five block multisets differ. With the notation of `VIS-109`, the only excess five-blocks are

`a-b: 01000, 00111, 11001`,

`b-a: 01001, 10111, 11000`,

one occurrence each. Correspondingly,

`(C_a(1,4),C_a(2,4),C_a(3,4))=(1,0,0)`,

`(C_b(1,4),C_b(2,4),C_b(3,4))=(0,1,1)`.

The bispectral distinction in `VIS-109` is therefore real, but at its minimal lag span it is exactly the next local-block layer that the order-three type omitted.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE INFORMATION-BOUNDARY + CLASSICAL HIGHER-ORDER-SPECTRAL/BLOCK SPECIALIZATION + NO-NOVELTY-CLAIM`.

This does not say that the full bispectrum, a fixed frequency-domain bispectral functional, or higher-order spectra in general are local finite-memory objects. A frequency-domain functional may mix correlations over lag ranges growing with the observation length. The theorem concerns bounded lag-domain coordinates and constructions that factor through a uniformly bounded lag set.

## 1. Every bounded-lag cylinder sum is a block-count functional

Fix the maximum lag `r`. For every start `j` in the defining sum, let

`u_j=(x_j,...,x_(j+r))`

be the length-`(r+1)` block beginning at `j`. The summand is the cylinder function

`F(u_j)=f((u_j)_(t_0),...,(u_j)_(t_(q-1))).`

Grouping starts by their complete block value gives immediately

`M_x=sum_u N_x(u)F(u)`.

No stationarity, probability model, Fourier transform, asymptotic limit, or quantization is needed. For a real-valued sequence the statement uses the exact multiset of real blocks; after a finite quantization it becomes an ordinary finite-alphabet block-count identity.

For product moments, take

`f(y_0,...,y_(q-1))=product_h y_h`.

For finite-alphabet indicators, take `f` to be the indicator of any selected symbol pattern. Centered moments and empirical cumulants constructed algebraically from a finite collection of such bounded-lag moments remain functions of the same sufficiently large finite block inventory.

Thus increasing moment order does not by itself create nonlocal memory. What matters for this information audit is the **lag span**, not merely whether a statistic is second-, third-, or higher-order.

## 2. Exact Markov types freeze the matching lag block

`VIS-099` identifies an exact order-`m` Markov type with a fixed initial `m`-context and the complete length-`(m+1)` transition-count table. Therefore every bounded-lag cylinder sum with maximum lag exactly `m` is constant on that type class by the identity above.

The same conclusion holds for smaller maximum lag after marginalizing the `(m+1)`-block inventory and using the type-determined terminal context for the finite boundary terms, exactly as in `VIS-109` for spans below three.

Conversely, moving from an order-`m` type to one coefficient at maximum lag `m+1` does not jump to global chronology. It merely accesses a function of the next length-`(m+2)` block inventory. In de Bruijn/Eulerian language, `VIS-094` already showed that the order-`m` transition graph stores `(m+1)`-blocks while forgetting the distinguished Eulerian assembly. A lag-`m+1` cylinder sum inspects adjacent transition pairings, equivalently one more local block order; it still does not retain the full trail.

This gives a hierarchy:

`fixed lag span r  ->  length-(r+1) block inventory`.

The hierarchy is exact for the statistic class above. A fixed but numerically large lag remains finite-memory if it does not grow with the observation scale.

## 3. Reinterpreting the `VIS-108` / `VIS-109` witness

`VIS-108` proves that

`a=01000111001011`,

`b=01001011100011`

have the same exact order-three Markov type and the same complete aperiodic two-point autocorrelation, while their degree-four delay signatures differ.

`VIS-109` then proves that their third-order correlations agree throughout the forced lag block `max(k,l)<=3` and differ at `C(1,4)`.

Direct length-five inventory comparison shows exactly where the new information enters. Every five-block count agrees except for the six one-occurrence differences listed in the claim. Since

`C_x(k,4)=sum_u N_x(u) u_0 u_k u_4`,

for binary five-blocks `u`, the displayed length-five differences yield

`C_a(1,4)-C_b(1,4)=1`,

`C_a(2,4)-C_b(2,4)=-1`,

`C_a(3,4)-C_b(3,4)=-1`.

The witness therefore establishes a useful but narrower fact than a global-order escape: two-point Fourier magnitude forgets information already present in the next local block layer, while third-order correlation can recover that layer.

This is still a legitimate information-admission result. It simply changes what a source-positive span-four statistic would mean. Such a result would establish dependence beyond the conditioned order-three block table, but not dependence beyond all finite local-memory descriptions.

## 4. Prior art and novelty assessment

The ingredients are classical. Higher-order moments/cumulants and their Fourier-domain polyspectra are standard signal-processing objects; C. L. Nikias and M. R. Raghuveer, **Bispectrum estimation: A digital signal processing framework**, *Proceedings of the IEEE* 75:7 (1987), 869–891, DOI `10.1109/PROC.1987.13824`, and Jerry M. Mendel, **Tutorial on higher-order statistics (spectra) in signal processing and system theory: theoretical results and some applications**, *Proceedings of the IEEE* 79:3 (1991), 278–305, DOI `10.1109/5.75086`, are standard references already used by `VIS-109` for the moment/cumulant–polyspectrum correspondence.

The finite-block/Eulerian side is likewise classical. `VIS-094` records the de Bruijn-style equivalence between an `(m+1)`-block inventory and the static transition multigraph, with Pevzner, Tang, and Waterman, **An Eulerian path approach to DNA fragment assembly**, *PNAS* 98:17 (2001), 9748–9753, DOI `10.1073/pnas.171285098`, as an established reconstruction reference. `VIS-099` records classical Markov-type conditioning through Whittle and later counting literature.

A targeted prior-art check under fixed-lag third-order moments, higher-order spectra, and Markov/block formulations found these classical ingredients rather than a distinct theorem whose novelty would need to be claimed here. No novelty is claimed for the cylinder-sum identity, higher-order correlations, bispectra, block frequencies, Markov types, or Eulerian sequence reconstruction.

The Mathia-specific value is the information audit at the current frontier: the phrase “beyond the order-three quotient” must not be conflated with “genuinely nonlocal.” The minimal bispectral witness of `VIS-109` advances exactly one local block layer.

## Boundary and falsification

The theorem covers finite collections of lag-domain statistics with maximum lag bounded independently of observation length and any deterministic construction that factors only through those statistics.

It does **not** classify:

- the complete third-order correlation surface with lag range growing to the full signal length;
- the full bispectrum or a frequency-domain functional that mixes an unbounded/growing set of lags;
- statistics whose lag span `R=R(N)` grows materially with sample size;
- path signatures, time-indexed filtrations, or other ordered carriers that do not factor through a fixed local-block inventory;
- independent analytic marks added to the gap sequence;
- source-specific finite-memory effects, which may still be scientifically real even though they are local.

A growing-lag or frequency-domain escape does not receive credit automatically. Its information content must still be audited, and source statistics must still be frozen before confirmation data are inspected.

Falsify the main claim by finding one bounded-lag cylinder sum whose value changes while the complete length-`(r+1)` block multiset at its maximum lag `r` remains fixed. The displayed grouping identity rules this out directly.

## Visual consequence

No canonical PNG is retained. This is an exact pre-render control. A bispectral heatmap can look globally structured even when the inspected coefficients occupy a bounded lag window and therefore contain only finite-block information. Rendering such a heatmap before deciding the lag scale would add selection freedom without changing this information bound.

## Research consequence

The accepted critical-strip multiscale clue should narrow again. A predeclared span-four or any other **fixed bounded-lag** third-order statistic may validly test zeta beyond an order-three Markov null, but it cannot by itself support a claim of genuinely nonlocal or multiscale chronology.

A continuation seeking a nonlocal channel must now do one of two things before source inspection: either specify a lag scale `R(N)` that grows with the observation window and state the corresponding lower-information control, or choose a genuinely frequency-domain/global higher-order functional and prove that it does not factor through a fixed finite-block inventory. A continuation interested only in finite-order source dependence may still use fixed lags, but must state that narrower target honestly and compare it against the matched finite-size CUE or other non-arithmetic source control.