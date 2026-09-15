# VIS-233 — lag-two returns escape endpoint-matched first-order Markov type

## Claim

Let `x_1,...,x_m` be a finite sequence over a finite alphabet `A`. Fix its endpoints `(x_1,x_m)` and its first-order transition counts

`C_(ij) = #{1<=t<m : (x_t,x_(t+1))=(i,j)}`.

Then every translation-invariant additive observable of range at most one,

`F(x)=h(x_1,x_m)+sum_(t=1)^m f(x_t)+sum_(t=1)^(m-1) g(x_t,x_(t+1))`,

is determined exactly by the endpoint-matched transition type. Indeed, `VIS-232` gives the occupancy counts `N_i` from `C` and the endpoint, so

`F(x)=h(x_1,x_m)+sum_i N_i f(i)+sum_(i,j) C_(ij) g(i,j)`.

By contrast the lag-two same-cell return statistic

`T_2(x)=sum_(t=1)^(m-2) 1_{x_t=x_(t+2)}`

is not determined in general by the same first-order type. Writing

`D_(ijk)=#{1<=t<=m-2 : (x_t,x_(t+1),x_(t+2))=(i,j,k)}`,

one has

`T_2(x)=sum_(i,j) D_(iji)`,

so `T_2` depends on length-three block information rather than only the one- and two-block counts fixed by the control.

The nondegeneracy is already exact in the smallest useful binary example. The three sequences

`00010`, `00100`, `01000`

all start and end at `0` and all have

`C_00=2`, `C_01=1`, `C_10=1`, `C_11=0`,

but their `T_2` values are respectively `2,1,2`. Under the uniform conditional distribution on these three endpoint-matched realizations,

`E[T_2]=5/3`, `Var(T_2)=2/9`.

Thus an exact first-order transition-count-preserving control can be nondegenerate for a range-two/order-sensitive observable even though `VIS-232` proves that it is degenerate for the occupancy collision statistic `S` and, more generally, for every observable in the range-one additive class above.

**Evidence/status:** `EXACT-DERIVED + CONDITIONAL-NONDEGENERACY BOUNDARY + CLASSICAL MARKOV-TYPE/BLOCK-COUNT SPECIALIZATION + NO-NOVELTY-CLAIM`.

No claim is made that `T_2` is prime-specific, that it is nondegenerate for every realized transition type, that it is the best statistic for the critical prime-phase problem, or that it yields any RH consequence.

## 1. First-order type fixes the whole range-one additive class

For each state `i`, let `N_i=#{t:x_t=i}`. By `VIS-232`, with row sums `R_i=sum_j C_(ij)`,

`N_i=R_i+1_{x_m=i}`.

Therefore the endpoint and transition table determine every state count. The state contribution of `F` is exactly `sum_i N_i f(i)`, and the adjacent-pair contribution is exactly `sum_(i,j) C_(ij)g(i,j)`. Both are fixed inside an endpoint-matched first-order Markov type.

This gives a model-admission rule stronger than the special collision identity in `VIS-232`: if the confirmation null preserves exact first-order transition counts and endpoints, then no translation-invariant additive statistic built only from individual states and adjacent pairs can test residual variation inside that conditional class. Reweighting the same one- or two-block counts cannot rescue the test.

The restriction to translation-invariant additive local statistics is essential. Position-dependent weights or genuinely global functionals can vary even when the same counts are fixed; the claim is not that first-order transition counts determine the whole sequence.

## 2. Lag-two return depends on triple coupling

The statistic `T_2` counts length-three blocks whose first and third symbols agree. Its exact block-count form is

`T_2=sum_(i,j)D_(iji)`.

The first-order table constrains pair marginals of the triple counts, with endpoint corrections, but it does not in general fix how an incoming transition through a middle state is coupled to the outgoing transition that follows it. That coupling is precisely length-three information.

Consequently the natural hierarchy is conditional rather than cosmetic: preserving one-block counts kills occupancy-only statistics; preserving first-order transition counts kills the entire translation-invariant additive range-one class; but a length-three statistic can still fluctuate. If a later control also conditions on all triple counts, `T_2` becomes fixed and the same logic pushes the observable to information outside that stronger sigma-field.

## 3. Exact nondegenerate first-order type

Consider binary sequences of length five with start and end state `0` and transition table

`C_00=2`, `C_01=1`, `C_10=1`, `C_11=0`.

The endpoint-matched realizations are exactly

`00010`, `00100`, `01000`.

Each consists of two `00` transitions and one excursion `0->1->0`, with only the excursion position changing. Direct evaluation gives

`T_2(00010)=2`,
`T_2(00100)=1`,
`T_2(01000)=2`.

Hence the conditional support is not a point mass. Under the uniform distribution on the three realizations,

`E[T_2]=(2+1+2)/3=5/3`,

and

`Var(T_2)=[(2-5/3)^2+(1-5/3)^2+(2-5/3)^2]/3=2/9`.

This example is only a witness of nondegeneracy. A particular large prime-phase transition type can still make `T_2` constant or nearly constant, so its conditional support and variance must be checked before `T_2` is used as a confirmation statistic.

## 4. Prior-art and novelty boundary

Fixed-transition-count Markov-chain realizations and their enumeration are classical. P. Whittle, **Some Distribution and Moment Formulae for the Markov Chain**, *Journal of the Royal Statistical Society: Series B* 17:2 (1955), 235–242, gives the foundational combinatorial treatment of observed transition totals.

R. Cowan, **Expected Pattern Frequency in Markov Chain Realizations Conditional Upon Transition Counts: Application of Whittle’s Combinatoric Formula to Problems in DNA Sequences**, *Theory of Probability & Its Applications* 37:2 (1993), 320–322, DOI `10.1137/1137065`, explicitly studies pattern frequencies conditional on fixed transition counts. Philippe Jacquet, Charles Knessl, and Wojciech Szpankowski, **Counting Markov Types**, DMTCS, AofA 2010, DOI `10.46298/dmtcs.2768`, treats first-order Markov types through pair-frequency matrices. Sara Kropf, **Variance and Covariance of Several Simultaneous Outputs of a Markov Chain**, *Discrete Mathematics & Theoretical Computer Science* 18:3 (2016), DOI `10.46298/dmtcs.1341`, includes counts of specific blocks as Markov-source outputs.

The present finding claims no new theorem about Markov types, conditional pattern frequencies, or block-count statistics. Its contribution is the exact specialization needed by the active Mathia control problem: it identifies the whole range-one additive class that an endpoint-matched first-order type conditions away, and exhibits a minimal local range at which a concrete replacement statistic can escape that degeneracy.

## Boundaries and falsification

The phrase “minimal local range” refers only to translation-invariant additive observables formed from fixed-radius local blocks. It does not cover position-weighted adjacent-pair statistics, nonlinear global path functionals, or other observables that may vary inside the same first-order type for unrelated reasons.

`T_2` is only a candidate information carrier. It may be generic under the exact conditional Markov-type ensemble, unstable under phase-cell origin changes, or unrelated to the signed prime-phase kernel. Any of those outcomes would kill it as a useful prime-specific discriminator without affecting the exact combinatorial boundary proved here.

If the admitted null preserves all length-three block counts, `T_2` is measurable from the preserved summary and therefore invalid for the same reason that `S` is invalid under occupancy conditioning. The statistic and the conditioning sigma-field must always be audited together.

Falsify the exact claim by producing two endpoint-matched sequences with the same first-order transition table but different values of some `F` in the stated range-one additive class, or by finding an error in the displayed binary transition table or `T_2` values.

## Research consequence

The accepted `CLUE-prime-phase-critical-logarithmic-occupancy` no longer needs to ask abstractly whether any order-sensitive observable survives an exact first-order transition control. `T_2` supplies a concrete predeclared first candidate and the binary example proves that such conditional variation can exist.

The next gate is statistical and arithmetic rather than combinatorial existence: for the actual critical prime-phase transition type, verify that `T_2` has a nondegenerate conditional distribution, calibrate that distribution without using confirmation outcomes to choose the statistic, test stability across the predeclared phase-cell representation choices, and only then ask whether any residual couples to the signed prime-phase energy. If `T_2` fails, a successor statistic must carry information outside the same preserved first-order sigma-field rather than merely reweighting the fixed counts.