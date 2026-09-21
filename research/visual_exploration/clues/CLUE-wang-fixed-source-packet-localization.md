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

## Research question

Does `G` possess a genuinely scale-dependent, adaptive, signed, or arithmetic localization that survives these moment, phase-entropy, total-multiplicity, collision-scale, cluster-coordinate conditioning and derivative-repayment gates and produces a pointwise smaller Wang output without reconstructing the larger source scale through `Q'` or equivalent unsmoothed information?

For a finite translated/dilated packet mechanism with frequency-independent coefficients, after grouping near-colliding phases and pricing every bounded cluster by the `VIS-352` Hermite collision scale, can the interaction among distinct cluster subspaces or the map from Wang source moments to the raw polynomial coefficient vector collapse strongly enough to meet the required local attenuation without paying the same gain through growing multiplicity, hierarchical microscopic clustering, inter-cluster packing, scale degeneration, or source-side strengthening? Alternatively, can frequency- or source-dependent coefficients, an infinite expansion, or direct signed structure of `G` produce a gain that is not equivalent to making a finite scalar multiplier unusually small?

## Why it may matter

The fixed and slowly varying scalar-bank routes are now substantially classified. Neither bounded/subpolynomial scalar order, a small pure-dilation bank, fixed translations, phase-resolving moving windows, ordinary mildly shrinking windows, exact cancellation of several low tail moments, interaction among finitely many nonzero tail orders, failure of Turan propagation under phase coalescence, raw Vandermonde blow-up, nor an unpriced bounded cluster collision provides a free smoothing gain.

For finite frequency-independent banks the remaining issue is now global rather than intra-cluster. A bounded cluster has stable divided-difference coordinates, and its possible coefficient-to-function loss is explicitly charged by `delta_X^(N-1)`. A useful construction must therefore exploit a genuinely singular source-to-polynomial-coefficient map, cancellation among several cluster subspaces, growing/hierarchical cluster complexity, or information absent from the finite scalar model.

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

After all intra-cluster collision powers are charged, quantify the map from the original Wang scale/translation moments to the raw polynomial coefficient vectors and the interaction among distinct cluster subspaces. A surviving finite-bank proposal must identify where the required power of `X` is paid. Legitimate possibilities now include growing total/cluster multiplicity, a shrinking measure ratio, a hierarchy of polynomially microscopic collision scales, inter-cluster density/cancellation, or a quantitatively singular source-to-coefficient map.

A construction satisfying this finite-dimensional budget is still not a positive source result. Propagate it through Wang's full destination: identify every occurrence of `Q`, `Q'`, or equivalent unsmoothed information and show that the final bound retains the smaller scale rather than reconstructing the source through the derivative channel.

If coefficients depend on frequency or directly on `G`, or if the mechanism is infinite rather than finite-dimensional, state that dependence explicitly and prove the resulting estimate as a signed source statement rather than rebranding it as fixed-filter smoothing.

Kill the route if it reduces to the already-classified scalar truncation order, violates the total-multiplicity/window budget, appears to win only through raw collision-coordinate blow-up, hides the needed power in an unrecorded microscopic collision hierarchy, restates a stronger theta/PNT remainder, or loses the gain in a destination derivative term.

## Evidence boundary

`VIS-333`--`VIS-352` are obstruction, representation, transfer, classicalization and conditioning results. They do not prove a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, or a destination-level avoidance of derivative repayment.

`VIS-350` proves that measurable Turan--Nazarov propagation survives confluent phase collision with total multiplicity replacing ordinary term count. `VIS-351` supplies stable divided-difference coordinates for bounded collision multiplicity. `VIS-352` adds a uniform worst-case lower bound that charges a bounded cluster by `delta_X^(N-1)` relative to its raw polynomial coefficient scale. None of these gives a global lower frame bound for a growing hierarchy of clusters, controls cancellation among distinct cluster subspaces, or proves that the map from `G`/Wang moments into the polynomial coefficient vector is non-singular at the required scale.

The clue therefore remains `accepted`: the finite scalar packet hierarchy is narrower, but genuinely source-coupled localization, hierarchical/growing cluster structure, and inter-cluster cancellation remain unclassified.

## Research disposition

Outcome: **narrowed**.

Future finite-bank work should treat every bounded collision cluster as a priced Hermite finite-difference resource: record its total multiplicity and physical diameter, charge the factor `delta_X^(N-1)`, and recurse when the normalized shape has a finer subcollision. The remaining finite-dimensional question is then the source-to-polynomial-coefficient map and interaction between the resulting cluster subspaces. Qualitatively different branches remain source/frequency dependence, infinite representation, or direct signed arithmetic structure of `G`, followed by the unchanged downstream derivative audit.