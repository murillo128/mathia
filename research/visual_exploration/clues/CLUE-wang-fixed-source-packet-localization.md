---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-333-wang-summatory-log-frequency-transfer.md
  - research/visual_exploration/findings/VIS-334-wang-summatory-pointwise-inverse-derivative-tax.md
  - research/visual_exploration/findings/VIS-339-wang-prime-source-chebyshev-theta-differential-image.md
  - research/visual_exploration/findings/VIS-340-wang-prime-squarelog-partial-summation-invertible.md
  - research/visual_exploration/findings/VIS-341-vk-scale-stable-under-finite-spectral-smoothing.md
  - research/visual_exploration/findings/VIS-342-vk-power-gain-requires-growing-truncation-order.md
  - research/visual_exploration/findings/VIS-343-wang-dilate-mixture-cancellation-order.md
  - research/visual_exploration/findings/VIS-344-wang-translated-dilate-cancellation-fibers.md
  - research/visual_exploration/findings/VIS-345-long-window-phase-resolution.md
  - research/visual_exploration/findings/VIS-346-turan-nazarov-short-window-obstruction.md
  - research/visual_exploration/findings/VIS-347-variable-wang-phase-entropy-budget.md
  - research/visual_exploration/findings/VIS-348-higher-wang-moments-inherit-phase-entropy-gate.md
  - research/visual_exploration/findings/VIS-349-wang-cross-order-confluent-exponential-polynomial.md
  - research/visual_exploration/findings/VIS-350-confluent-turan-total-multiplicity.md
  - research/visual_exploration/findings/VIS-351-divided-difference-cluster-conditioning.md
  - research/visual_exploration/findings/VIS-352-hermite-collision-scale-budget.md
  - research/visual_exploration/findings/VIS-353-separated-cluster-block-riesz-floor.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has been reduced to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333` gives Wang's exact nonvanishing multiplier `m(xi)=4(1+i xi)/(4+xi^2)`, while `VIS-334` shows that exact pointwise inversion pays one derivative. `VIS-339` and `VIS-340` show that the surviving prime source and the prime square-log summatory source are exact differential/integral images of the same `G`; repackaging primes into packets is therefore not an independent information channel.

The generic scalar smoothing escapes have also been narrowed. `VIS-341` shows that every fixed finite polynomial smoothing order preserves the Korobov--Vinogradov power class. `VIS-342` shows that a fixed positive gain in that class would require polynomially growing effective order. `VIS-343` converts that order into a scale-count cost for pure Wang dilates, and `VIS-344` shows that fixed translated copies cannot pool asymptotic moment cancellation across distinct phase fibers.

`VIS-345` closes moving windows once their lengths resolve the translation gaps. `VIS-346` removes most of the remaining fixed-bank short-window loophole: Turan--Nazarov propagation shows that, for a fixed bank with `B` phase fibers, `O(X^-r)` cancellation on windows of length `ell_X` still forces the same fiber moments through order `r-1` whenever

`X min(ell_X,1)^(B-1) -> infinity`.

`VIS-347` prices the first genuinely scale-dependent escape. For an `X`-dependent bank, let `B_X` be the number of active first-moment phase fibers, `Delta_X` their minimum spacing, `ell_X` the window length, `S_X` the first inverse-scale moment vector, and `T_X=sum_j |c_(j,X)|/a_(j,X)^2`. Then order-`>=2` attenuation forces the Turan--Nazarov phase-entropy budget

`(B_X-1) log(A L_X/e_X)`
` >= log( X ||S_X||_2 / (sqrt(2) D_X) )`,

with `L_X=4(B_X-1)/Delta_X`, `e_X=min(ell_X,L_X)`, and `D_X=C_0/2+2T_X`.

If `D_X/||S_X||_2=X^(o(1))`, this budget must be `(1-o(1))log X`. Consequently, a bounded `B` with `ell_X=X^-alpha` and `Delta_X=X^-beta` needs `(B-1)(alpha+beta)>=1`, while well-separated phases on macroscopic windows need `B_X log B_X` at least of order `log X`, hence `B_X=Omega(log X/log log X)` up to constants.

`VIS-348` shows that the first-moment gate is not special. If the lower translated inverse-scale moment polynomials `P_1,...,P_(q-1)` vanish exactly and `P_q` is the first surviving one, then claiming one further local inverse-frequency order again forces the same one-power `X` Turan--Nazarov budget, now with the phase count, spacing and conditioning of the `q`th moment. Exact low-order Vandermonde cancellation therefore does not make the first surviving higher moment locally cheap.

`VIS-349` removes the algebraic ambiguity from simultaneous nonzero tail orders. Without assuming lower moments vanish, the first `q` interacting Wang orders are exactly

`E_(q,X)(xi)=sum_b exp(-i b xi) Q_(b,q,X)(xi)`,

with `deg Q_(b,q,X)<=q-1`. Exact cancellation forces all phase-fiber moments through order `q` to vanish separately, while one extra local Wang order forces `E_(q,X)=O(X^-1)` on the working window with the next-tail conditioning displayed explicitly.

`VIS-350` closes the missing propagation part of that confluent problem. Polynomially weighted exponentials are compact-uniform limits of ordinary exponential sums obtained by coalescing frequencies, so the measurable Turan--Nazarov inequality passes to the limit. If

`N_X=sum_b (deg Q_(b,q,X)+1)`

is the total confluent multiplicity, `J_X subset I_X`, `H_X=sup_(I_X)|E_(q,X)|`, and `D_(q,X)=2^q C_0+C_q T_(q+1,X)`, then one-extra-order attenuation implies

`X H_X/D_(q,X) <= (A |I_X|/|J_X|)^(N_X-1)`.

`VIS-351` removes a coordinate artifact from the remaining conditioning question. Generalized divided differences of colliding exponentials form uniformly normed coordinates for every fixed cluster multiplicity on a fixed reference interval. Raw Vandermonde coefficient explosion is therefore not itself a resource.

`VIS-352` then prices the genuine geometric loss that remains after that quotient. For a bounded cluster with `B` phase fibers, polynomial degree `<q`, total confluent multiplicity `N=Bq`, and physical diameter `delta_X` with a uniformly separated normalized shape,

`H_X >= C delta_X^(N-1) ||c_X||_2`.

Thus if `D_(q,X)/||c_X||_2=X^(o(1))`, a collision-only explanation of the required `H_X<=D_(q,X)/X` needs

`delta_X <= X^(-1/(N-1)+o(1))`.

Near-coalescence is therefore no longer an unpriced conditioning loophole: bounded confluent geometry can buy the missing power only through an explicitly polynomially microscopic translation scale. Hierarchical subcollisions must be separated into their own scales rather than hidden in one cluster constant.

`VIS-353` removes the corresponding bounded **inter-cluster** loophole. For a fixed number of cluster-local divided-difference blocks with bounded total spectral span and uniform separation between distinct cluster spectra, the union has a uniform lower Riesz bound on a fixed interval:

`||F||_2 >= kappa (sum_a ||u_a||_2^2)^(1/2)`.

Combining this with the `VIS-352` local collision ledger gives

`||F||_2 >= C (sum_a delta_a^(2(N_a-1)) ||c_a||_2^2)^(1/2)`.

So a bounded separated family cannot obtain a second asymptotic power from cancellation between already-priced cluster subspaces. If inter-cluster separation collapses, the clusters must be merged into a new collision hierarchy; if count or total span grows, that growth is itself a new complexity resource.

## Research question

Does `G` possess a genuinely scale-dependent, adaptive, signed, or arithmetic localization that survives these moment, phase-entropy, total-multiplicity, collision-scale, block-Riesz, and derivative-repayment gates and produces a pointwise smaller Wang output without reconstructing the larger source scale through `Q'` or equivalent unsmoothed information?

For a finite translated/dilated packet mechanism with frequency-independent coefficients, after pricing all bounded collision scales and quotienting all bounded separated cluster blocks by `VIS-353`, can the map from Wang source moments into the raw polynomial coefficient vectors collapse strongly enough to meet the required local attenuation without restating stronger source cancellation? Alternatively, can a genuinely growing/global geometry — increasing multiplicity or cluster count, collapsing inter-cluster scales, expanding spectral span/density, shrinking windows — or frequency/source-dependent coefficients, an infinite expansion, or direct signed structure of `G` supply a gain that is not equivalent to making a finite scalar multiplier unusually small?

## Why it may matter

The bounded finite-bank routes are now substantially classified. Neither bounded/subpolynomial scalar order, a small pure-dilation bank, fixed translations, phase-resolving moving windows, ordinary mildly shrinking windows, exact cancellation of several low tail moments, interaction among finitely many nonzero tail orders, failure of Turan propagation under phase coalescence, raw Vandermonde blow-up, an unpriced bounded collision, nor cancellation among a fixed bounded separated family of stable cluster blocks provides a free smoothing gain.

For finite frequency-independent banks the remaining bounded-dimensional issue is now mostly upstream of the block geometry: whether the exact Wang scale/translation moments map into an anomalously small polynomial coefficient vector relative to the source normalization. Global geometry becomes a distinct resource only when one of the compactness parameters genuinely escapes with `X`.

## Decisive test

Start from the exact source quotients in `VIS-339` and `VIS-340` and state the candidate directly as a quantitative property of `G`.

For any finite translated-dilate bank with frequency-independent coefficients, choose the finite asymptotic depth `q` needed by the claimed gain and form

`E_(q,X)(xi)=sum_(k=1)^q beta_k xi^(q-k) P_(k,X)(xi)`
`             =sum_b exp(-i b xi) Q_(b,q,X)(xi)`.

Record the distinct phases, polynomial coefficient data, scale count, working window `J_X`, next-tail term, and a mathematically natural containing reference interval `I_X`. Set

`N_X=sum_b(deg Q_b+1)`,
`H_X=sup_(I_X)|E_(q,X)|`,
`D_(q,X)=2^q C_0+C_q T_(q+1,X)`.

Apply the exact `VIS-350` budget

`X H_X/D_(q,X) <= (A |I_X|/|J_X|)^(N_X-1)`.

Partition phases into collision clusters at the scale relevant to `I_X`. Within every cluster of bounded multiplicity, choose its physical diameter `delta_X` and normalized shape. If the normalized centers remain uniformly separated, apply `VIS-352`: any claimed intra-cluster loss must appear in the explicit factor `delta_X^(N_cluster-1)` or in a small raw Wang polynomial coefficient vector. If the normalized shape itself degenerates, recurse on the finer subcluster scale rather than burying it in a condition number.

After the local collision scales are priced, apply `VIS-353` whenever the number of blocks is fixed, their total spectral span is uniformly bounded, and distinct block spectra remain uniformly separated. In that regime, do not debit an additional power to inter-block cancellation: the global norm is bounded below by the quadrature norm of the stable local block coordinates. If cross-block separation collapses, merge the affected blocks and price the new collision scale; if block count or spectral span grows, record that growth explicitly as the candidate resource.

What remains in the bounded regime is the exact map from Wang source/scale moments to the raw polynomial coefficient vectors. A surviving proposal must prove a genuine polynomial loss there without simply assuming a stronger bound for `G`, `theta`, or an equivalent source quantity.

A construction satisfying this finite-dimensional budget is still not a positive source result. Propagate it through Wang's full destination: identify every occurrence of `Q`, `Q'`, or equivalent unsmoothed information and show that the final bound retains the smaller scale rather than reconstructing the source through the derivative channel.

If coefficients depend on frequency or directly on `G`, or if the mechanism is infinite rather than finite-dimensional, state that dependence explicitly and prove the resulting estimate as a signed source statement rather than rebranding it as fixed-filter smoothing.

Kill the route if it reduces to the already-classified scalar truncation order, violates the total-multiplicity/window budget, appears to win only through raw collision-coordinate blow-up, hides the needed power in an unrecorded collision hierarchy or bounded separated-block cancellation, restates a stronger theta/PNT remainder, or loses the gain in a destination derivative term.

## Evidence boundary

`VIS-333`--`VIS-353` are obstruction, representation, transfer, classicalization, conditioning, and finite-dimensional block-norming results. They do not prove a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, or a destination-level avoidance of derivative repayment.

`VIS-350` proves measurable Turan--Nazarov propagation with total confluent multiplicity. `VIS-351` supplies stable divided-difference coordinates through bounded collisions. `VIS-352` charges each bounded cluster by its explicit Hermite collision scale relative to raw polynomial coefficients. `VIS-353` shows that a fixed separated family of such cluster blocks with bounded total spectral span has a uniform global Riesz floor, so bounded inter-cluster cancellation contributes no additional asymptotic power.

None of these proves that the exact map from `G`/Wang source moments into the raw polynomial coefficient vectors is non-singular at the required scale. They also do not cover growing cluster count/multiplicity, unbounded spectral span/density, collapsing inter-cluster separation, shrinking reference windows, source/frequency-dependent coefficients, infinite expansions, or direct arithmetic sign cancellation.

The clue therefore remains `accepted`: the bounded finite-bank geometry is narrower again, while source-coupled coefficient loss and genuinely growing/global localization mechanisms remain unclassified.

## Research disposition

Outcome: **narrowed**.

Future bounded finite-bank work should stop treating inter-cluster cancellation as an independent escape once local collision scales are priced and the blocks stay in a compact separated regime. The next bounded-dimensional target is the Wang source-moment-to-polynomial-coefficient map itself. Qualitatively different branches require an explicit escaping parameter — growing multiplicity/count/span/density, a new collision hierarchy or shrinking window — or source/frequency dependence, infinite representation, or direct signed arithmetic structure of `G`, followed by the unchanged downstream derivative audit.