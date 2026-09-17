# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price height adaptation by source-resolvable motion, repertoire and approximate linear complexity

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-049-fixed-prime-phase-rank-survives-density-one-acquisition-filters`.

NB-165--NB-167 isolate the capped Poisson transport metric actually seen by a compact signed sampler near `Re s=1`. NB-168 shows one fixed stationary template cannot produce logarithmic Euler rescue on positive density under the subcritical transport budget. NB-169--NB-171 then price ordered height adaptation by refresh count, total variation and finite `p`-variation measured at that same source resolution.

NB-172 removes temporal regularity entirely: rescue density is controlled by the internal covering number of the template range in capped Poisson transport. NB-173 gives a different compression when the range lies exactly in a stationary linear span. NB-174 unifies those unordered compressions at source resolution through approximate linear complexity `mathfrak L_T(epsilon)`.

NB-175 supplies a dual nuclear-response lower certificate. NB-176 makes one such witness source-native using actual Euler frequencies and amplitudes. NB-177 finds an intrinsic compactness ceiling for that jointly Hilbert-contracting witness. NB-178 shows a larger coordinatewise dual can escape through dense phase codes, but NB-179 constructs the same maximal response from bare Poisson-width packing. NB-180 shows that genuine Euler frequency support remains nonselective if weak frequency channels may be normalized independently: the true Euler amplitudes are the load-bearing source datum.

NB-181 closes the bounded-Hilbert repair. Retaining the true amplitudes inside the natural feature Hilbert space gives a nuclear bound forcing RMS Hilbert acquisition norm `Omega(sqrt N)` for an `N x N` Hadamard-scale response. The physical scalar Euler readout is not a counterexample because its phase vector is not `ell^2`; its convergence uses absolute Dirichlet summability.

NB-182 prices that exact non-Hilbert escape. After charging each Euler character by its capped-Poisson Lipschitz cost, the absolute Euler exposure

`W(a)=sum Lambda(n)n^(-1-a) max{2,a log n}`

satisfies `W(a) asymp 1/a`. Normalized scalar Euler translates are convex combinations of unit capped-transport characters, and Fourier--Stieltjes mixtures obey the same nuclear bound with RMS total-variation acquisition gain `G`. Dense rank-`N` phase coding still requires `G=Omega(sqrt N)`: the Wiener/Dirichlet topology changes the currency but does not make coherent phase acquisition free.

The uniform high-ordinate zeta bound supplies gain `kappa_T asymp 1/(a H_T)`, where `H_T=min{1/a,log T/log log T}`. NB-182 therefore left a square crossover `a H_T^2=O(1)` if one insists on that worst-case source norm.

NB-183 resolves the height-frequency side of that question by showing that the **actual** capped-Poisson Lipschitz seminorm `mathcal H_(a,B)(t)` has mean square

`T^(-1) integral_T^(2T) mathcal H_(a,B)(t)^2 dt << 1 + (T a^4)^(-1)`.

Its stated regime `T a^4 -> infinity` is a convenient sufficient condition, not the true acquisition threshold. NB-184 first notes that the `NB-183` estimate already gives `sqrt(a) mathcal H -> 0` in relative measure under `T a^3 -> infinity`. It then uses the zero-mass quotient by constants: anchor the Euler kernel before applying one-dimensional interpolation. The resulting bound implies

`sqrt(a_T) mathcal H_(a_T,B)(t) -> 0`

in relative measure whenever `a_T -> 0` and `T a_T^2 -> infinity`. Since `W(a) asymp 1/a` and the full generic packing dimension is `N asymp 1/a`, the charged scalar acquisition ratio satisfies `kappa/sqrt(N) -> infinity` on density-one heights throughout that quadratic-divergence regime. For power widths this covers every `a=T^(-alpha)` with fixed `alpha<1/2`.

NB-185 removes a purely algebraic finite-rank obstruction inside that same good-height set. Distinct prime logarithms generate an equidistributed finite torus, and deleting the `o(T)` acquisition-bad set cannot erase any fixed positive-measure phase box. Hence every fixed finite Hadamard prime-phase code can be realized by NB-184-good heights, with all raw phase-matrix singular values on the `sqrt N` scale. Finite prime-phase relations therefore do not cap coherent rank qualitatively.

NB-186 removes the high-dimensional phase-box bottleneck for the weaker but sufficient nuclear notion of growing raw rank. If `G subset [T,2T]` has relative complement `epsilon`, pairwise prime-phase correlations on `G` are bounded by `rho << epsilon+p_N/T`. A fourth-moment selection of `N` heights then gives a raw first-`N`-prime phase matrix with

`||P||_* >= N^(3/2) / sqrt(2+N rho^2)`.

Combining this with the quantitative `NB-184` exceptional-density bound and `N asymp 1/a` yields `||P||_* >> N^(3/2)` already at the cubic simultaneous-selection scale `T a^3 \gtrsim 1` for a fixed acquisition threshold. If `T a^3 -> infinity`, the threshold may tend to zero slowly while `||P||_* >= (1/sqrt(2)-o(1)) N^(3/2)`. Thus growing raw prime-phase coherence does not require quantitative high-dimensional Kronecker hitting; low pairwise moments suffice.

NB-187 identifies where that raw code sits inside the actual `NB-182` Wiener source. Under the normalized Euler-Wiener weights, the scaled logarithmic frequency `u=a log n` converges to density proportional to `e^(-u) max{2,u}`; in particular `a W(a) -> 2+e^(-2)`. The first `N asymp 1/a` primes used by NB-186 satisfy `a log p_N ->0` and carry only

`Theta_N(a) ~ [2/(2+e^(-2))] a log(1/a) -> 0`

of the full source budget. In fact any `O(1/a)` individual prime channels carry vanishing mass, while a fixed positive fraction of the Wiener budget requires exponentially many prime channels. Thus selecting or shell-flattening only Poisson-many favorable frequencies cannot be the amplitude-balanced bridge; direct isolation of the NB-186 block costs `Theta_N(a)^(-1) asymp 1/(a log(1/a))` in the Wiener coefficient currency.

The post-NB-187 target is therefore **mass-reusing aggregate acquisition**. A positive route must coherently compress an exponentially large population of true-amplitude Euler channels into only `O(1/a)` effective observables while preserving a positive fraction of the growing phase nuclear mass. A negative route should prove that every such overlapping compression loses the `NB-178` certificate once charged in the Wiener/capped-Poisson currency. Separately, the cubic scale remains only the boundary of the current simultaneous-selection argument, while the finite-height scalar acquisition boundary remains the genuine quadratic endpoint `T a^2=O(1)`.

## Keep target conditioning and arithmetic-source persistence separate

NB-168--NB-187 are source-side persistence/resource theorems. NB-177 shows one canonical square-summed witness can be too compact; NB-178--NB-180 show why enlarging and renormalizing the dual can manufacture nonselective generic codes; NB-181 prices true amplitudes in bounded Hilbert geometry; NB-182 prices the actual non-Hilbert Euler scalar family in Wiener/Fourier--Stieltjes geometry; NB-183 shows that its local charged acquisition cost is generically much smaller than the worst-case uniform high-ordinate bound; NB-184 puts that statement in the correct quotient-by-constants geometry and pushes the density-one acquisition regime to `T a^2 -> infinity`; NB-185 shows that fixed finite prime-phase coherence survives that density-one filter; NB-186 upgrades raw phase accessibility to growing nuclear rank `N asymp 1/a` at cubic simultaneous-selection scale without prescribed high-dimensional phase boxes; NB-187 shows that every Poisson-sized set of individual prime channels nevertheless carries vanishing Euler-Wiener mass, forcing any successful amplitude-balanced extraction to aggregate far more arithmetic channels than geometric output coordinates.

None of these results turns a density obstruction into pointwise exclusion at a selected sparse sequence, resolves the quadratic finite-height endpoint, constructs or rules out a mass-reusing aggregate acquisition, or by itself connects surviving source response back to global Nyman approximation. The next certificate must therefore couple growing arithmetic phase coherence to an overlapping amplitude-balanced source-faithful acquisition map and a matched-control comparison, rather than obtaining apparent complexity from independently normalized characters.