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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has been reduced to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333` gives Wang's exact nonvanishing multiplier `m(xi)=4(1+i xi)/(4+xi^2)`, while `VIS-334` shows that exact pointwise inversion pays one derivative. `VIS-339` and `VIS-340` show that the surviving prime source and the prime square-log summatory source are exact differential/integral images of the same `G`; repackaging primes into packets is therefore not an independent information channel.

The generic scalar smoothing escapes have also been narrowed. `VIS-341` shows that every fixed finite polynomial smoothing order preserves the Korobov--Vinogradov power class. `VIS-342` shows that a fixed positive gain in that class would require polynomially growing effective order. `VIS-343` converts that order into a scale-count cost for pure Wang dilates, and `VIS-344` shows that fixed translated copies cannot pool asymptotic moment cancellation across distinct phase fibers.

`VIS-345` closes moving windows once their lengths resolve the translation gaps. `VIS-346` removes most of the remaining fixed-bank short-window loophole: Turán--Nazarov propagation shows that, for a fixed bank with `B` phase fibers, `O(X^-r)` cancellation on windows of length `ell_X` still forces the same fiber moments through order `r-1` whenever

`X min(ell_X,1)^(B-1) -> infinity`.

`VIS-347` prices the first genuinely scale-dependent escape. For an `X`-dependent bank, let `B_X` be the number of active first-moment phase fibers, `Delta_X` their minimum spacing, `ell_X` the window length, `S_X` the first inverse-scale moment vector, and `T_X=sum_j |c_(j,X)|/a_(j,X)^2`. Then order-`>=2` attenuation forces the Turán--Nazarov phase-entropy budget

`(B_X-1) log(A L_X/e_X)`
` >= log( X ||S_X||_2 / (sqrt(2) D_X) )`,

with `L_X=4(B_X-1)/Delta_X`, `e_X=min(ell_X,L_X)`, and `D_X=C_0/2+2T_X`.

If `D_X/||S_X||_2=X^(o(1))`, this budget must be `(1-o(1))log X`. Consequently, a bounded `B` with `ell_X=X^-alpha` and `Delta_X=X^-beta` needs `(B-1)(alpha+beta)>=1`, while well-separated phases on macroscopic windows need `B_X log B_X` at least of order `log X`, hence `B_X=Omega(log X/log log X)` up to constants.

`VIS-348` shows that the first-moment gate is not special. If the lower translated inverse-scale moment polynomials `P_1,...,P_(q-1)` vanish exactly and `P_q` is the first surviving one, then claiming one further local inverse-frequency order again forces the same one-power `X` Turán--Nazarov budget, now with the phase count, spacing and conditioning of the `q`th moment. Exact low-order Vandermonde cancellation therefore does not make the first surviving higher moment locally cheap.

`VIS-349` removes the algebraic ambiguity from simultaneous nonzero tail orders. Without assuming lower moments vanish, the first `q` interacting Wang orders are exactly

`E_(q,X)(xi)=sum_b exp(-i b xi) Q_(b,q,X)(xi)`,

with `deg Q_(b,q,X)<=q-1`. Exact cancellation forces all phase-fiber moments through order `q` to vanish separately, while one extra local Wang order forces `E_(q,X)=O(X^-1)` on the working window with the next-tail conditioning displayed explicitly.

`VIS-350` closes the missing **propagation** part of that confluent problem. Polynomially weighted exponentials are compact-uniform limits of ordinary exponential sums obtained by coalescing frequencies, so the measurable Turán--Nazarov inequality passes to the limit. If

`N_X=sum_b (deg Q_(b,q,X)+1)`

is the total confluent multiplicity, `J_X subset I_X`, `H_X=sup_(I_X)|E_(q,X)|`, and `D_(q,X)=2^q C_0+C_q T_(q+1,X)`, then one-extra-order attenuation implies

`X H_X/D_(q,X) <= (A |I_X|/|J_X|)^(N_X-1)`.

No phase-spacing penalty appears in this propagation step. Near-coalescing phases can help only by making the complete confluent tail already small on the reference interval relative to its natural coefficient/moment scale. The finite-bank loophole is therefore a norming/conditioning problem, not a missing special confluent Remez theorem.

## Research question

Does `G` possess a genuinely scale-dependent, adaptive, signed, or arithmetic localization that survives these moment, phase-entropy, total-multiplicity, conditioning and derivative-repayment gates and produces a pointwise smaller Wang output without reconstructing the larger source scale through `Q'` or equivalent unsmoothed information?

For a finite translated/dilated packet mechanism with frequency-independent coefficients, can the reference norm of its confluent tail collapse relative to the underlying Wang moment data strongly enough to meet the required local attenuation **without** paying the same gain through phase collision, coefficient explosion, scale degeneration, growing effective dimension, or window collapse? Alternatively, can frequency- or source-dependent coefficients, an infinite expansion, or direct signed structure of `G` produce a gain that is not equivalent to making a finite scalar multiplier unusually small?

## Why it may matter

The fixed and slowly varying scalar-bank routes are now substantially classified. Neither bounded/subpolynomial scalar order, a small pure-dilation bank, fixed translations, phase-resolving moving windows, ordinary mildly shrinking windows, exact cancellation of several low tail moments, interaction among finitely many nonzero tail orders, nor a supposed failure of Turán propagation under phase coalescence provides a free smoothing gain.

For finite frequency-independent banks the remaining issue is sharply localized: the coefficient-to-function map for the confluent tail may become ill-conditioned as phases coalesce or polynomial coefficients cancel. A useful construction must quantify that conditioning and show that the resulting reference-norm loss is not simply the resource paying for the apparent local gain. A genuinely different positive mechanism would instead use information that the finite scalar model discards, such as source/frequency-dependent coefficients, an infinite representation, or arithmetic sign structure of `G`.

## Decisive test

Start from the exact source quotients in `VIS-339` and `VIS-340` and state the candidate directly as a quantitative property of `G`.

For any finite translated-dilate bank with frequency-independent coefficients, choose the finite asymptotic depth `q` needed by the claimed gain and form

`E_(q,X)(xi)=sum_(k=1)^q beta_k xi^(q-k) P_(k,X)(xi)`
`             =sum_b exp(-i b xi) Q_(b,q,X)(xi)`.

Record the distinct phases, the degree and coefficients of each `Q_b`, the scale count, the working window `J_X`, the next-tail term, and a mathematically natural containing reference interval `I_X`. Set

`N_X=sum_b(deg Q_b+1)`,
`H_X=sup_(I_X)|E_(q,X)|`,
`D_(q,X)=2^q C_0+C_q T_(q+1,X)`.

Apply the exact `VIS-350` budget

`X H_X/D_(q,X) <= (A |I_X|/|J_X|)^(N_X-1)`.

A finite-bank proposal must then identify where the required power of `X` is paid. If it comes from growing `N_X` or a shrinking measure ratio, debit that explicit propagation complexity. If it comes from small `H_X` relative to the natural moment/coefficient data, prove a quantitative norming or condition-number statement and show that phase coalescence, polynomial cancellation, coefficient explosion, or scale degeneration has not merely paid for the gain in another coordinate system.

A construction satisfying this finite-dimensional budget is still not a positive source result. Propagate it through Wang's full destination: identify every occurrence of `Q`, `Q'`, or equivalent unsmoothed information and show that the final bound retains the smaller scale rather than reconstructing the source through the derivative channel.

If coefficients depend on frequency or directly on `G`, or if the mechanism is infinite rather than finite-dimensional, state that dependence explicitly and prove the resulting estimate as a signed source statement rather than rebranding it as fixed-filter smoothing.

Kill the route if it reduces to the already-classified scalar truncation order, violates the total-multiplicity/window budget, meets it only by polynomial collapse of the reference norm through ill-conditioning, restates a stronger theta/PNT remainder, or loses the gain in a destination derivative term.

## Evidence boundary

`VIS-333`--`VIS-350` are obstruction, representation, transfer, and classicalization results. They do not prove a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, or a destination-level avoidance of derivative repayment.

`VIS-350` proves that measurable Turán--Nazarov propagation itself survives confluent phase collision with total multiplicity replacing ordinary term count. It does **not** prove a uniform lower bound for the reference norm `H_X` in terms of raw Wang phase-fiber moments when the coefficient-to-function map becomes ill-conditioned. That norming problem remains open, as do frequency/source-dependent coefficients, infinite expansions, and arithmetic sign cancellation coupled directly to `G`.

The clue therefore remains `accepted`: the finite scalar packet hierarchy is narrower, but a genuinely source-coupled localization mechanism remains unclassified.

## Research disposition

Outcome: **narrowed**.

Future finite-bank work should target the reference-norm/conditioning map rather than search for a separate confluent Turán propagation theorem. Growing total multiplicity and shrinking windows have an explicit cost; phase collision or polynomial cancellation matters only through the amount by which it collapses the complete tail relative to its natural moment scale. The remaining qualitatively distinct branch is source/frequency dependence, infinite representation, or direct signed arithmetic structure of `G`, followed by the unchanged downstream derivative audit.