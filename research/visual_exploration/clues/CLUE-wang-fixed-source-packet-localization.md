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

`VIS-351` removes a further coordinate artifact from the remaining conditioning question. Generalized divided differences of colliding exponentials form uniformly normed coordinates for every fixed cluster multiplicity on a fixed reference interval. In the two-phase model, raw coefficients can blow like `1/h` as a gap `h->0` while the stable coefficient is the finite derivative coordinate `h c_1`; the represented function does not become small. More generally, a bounded collision cluster has a uniformly positive Gram lower bound in divided-difference coordinates.

Therefore near-coalescing phases can no longer be credited merely because a raw Vandermonde coefficient vector becomes ill-conditioned. The finite-bank loophole is now the conditioning of the **Wang moment data into stable cluster coordinates**, together with cancellation between distinct clusters, growing effective multiplicity, window shrinkage, or genuinely source-dependent structure.

## Research question

Does `G` possess a genuinely scale-dependent, adaptive, signed, or arithmetic localization that survives these moment, phase-entropy, total-multiplicity, cluster-coordinate conditioning and derivative-repayment gates and produces a pointwise smaller Wang output without reconstructing the larger source scale through `Q'` or equivalent unsmoothed information?

For a finite translated/dilated packet mechanism with frequency-independent coefficients, after grouping near-colliding phases and rewriting each bounded-multiplicity cluster in generalized divided-difference coordinates, can the resulting cluster-adapted coefficient vector or the interaction among distinct cluster subspaces collapse strongly enough to meet the required local attenuation **without** paying the same gain through growing multiplicity, cluster radius, inter-cluster packing, scale degeneration, or a singular moment-to-cluster coordinate map? Alternatively, can frequency- or source-dependent coefficients, an infinite expansion, or direct signed structure of `G` produce a gain that is not equivalent to making a finite scalar multiplier unusually small?

## Why it may matter

The fixed and slowly varying scalar-bank routes are now substantially classified. Neither bounded/subpolynomial scalar order, a small pure-dilation bank, fixed translations, phase-resolving moving windows, ordinary mildly shrinking windows, exact cancellation of several low tail moments, interaction among finitely many nonzero tail orders, failure of Turan propagation under phase coalescence, nor raw Vandermonde blow-up inside a fixed collision cluster provides a free smoothing gain.

For finite frequency-independent banks the remaining question is more intrinsic than before. The correct coefficient norm is not the raw exponential-coordinate norm when phases collide; generalized divided differences quotient that singular representation. A useful construction must now exhibit a real loss in the map from Wang scale/translation moments to those stable cluster coordinates, a growing cluster/inter-cluster complexity, or source information absent from the finite scalar model.

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

Then partition phases into collision clusters at the scale relevant to `I_X`. Within every cluster whose multiplicity and diameter stay in a fixed compact regime, rewrite the exponential family in the generalized divided-difference basis of `VIS-351`. Do **not** debit raw Vandermonde coefficient explosion as a resource. Record instead the cluster-adapted coefficient vector and the map from the original Wang moment data to that vector.

A finite-bank proposal must identify where the required power of `X` is paid after this reparameterization. Legitimate possibilities include growing total/cluster multiplicity, a shrinking measure ratio, growing cluster radius or inter-cluster density that destroys a uniform Riesz bound, a quantitatively singular moment-to-divided-difference map, or cancellation among distinct cluster subspaces. Each must be priced in the actual stable coordinates.

A construction satisfying this finite-dimensional budget is still not a positive source result. Propagate it through Wang's full destination: identify every occurrence of `Q`, `Q'`, or equivalent unsmoothed information and show that the final bound retains the smaller scale rather than reconstructing the source through the derivative channel.

If coefficients depend on frequency or directly on `G`, or if the mechanism is infinite rather than finite-dimensional, state that dependence explicitly and prove the resulting estimate as a signed source statement rather than rebranding it as fixed-filter smoothing.

Kill the route if it reduces to the already-classified scalar truncation order, violates the total-multiplicity/window budget, appears to win only through raw collision-coordinate blow-up removed by divided differences, restates a stronger theta/PNT remainder, or loses the gain in a destination derivative term.

## Evidence boundary

`VIS-333`--`VIS-351` are obstruction, representation, transfer, classicalization and conditioning results. They do not prove a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, or a destination-level avoidance of derivative repayment.

`VIS-350` proves that measurable Turan--Nazarov propagation survives confluent phase collision with total multiplicity replacing ordinary term count. `VIS-351` proves that a fixed bounded collision cluster is uniformly conditioned after generalized divided-difference reparameterization. Neither result supplies a global lower bound for a growing collection of moving clusters or a quantitative lower bound from the **raw Wang moment data** to the cluster-adapted coefficients. That intrinsic map and inter-cluster interaction remain open, as do frequency/source-dependent coefficients, infinite expansions, and arithmetic sign cancellation coupled directly to `G`.

The clue therefore remains `accepted`: the finite scalar packet hierarchy is narrower, but a genuinely source-coupled localization mechanism remains unclassified.

## Research disposition

Outcome: **narrowed**.

Future finite-bank work should first quotient phase-collision coordinate singularities with generalized divided differences, then price the remaining moment-to-cluster and inter-cluster norming map. Raw exponential-coefficient blow-up is no longer an admissible explanation for a small reference norm at fixed collision multiplicity. The qualitatively distinct branches remain growing effective complexity, source/frequency dependence, infinite representation, or direct signed arithmetic structure of `G`, followed by the unchanged downstream derivative audit.