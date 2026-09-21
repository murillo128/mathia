# VIS-350 — measurable Turán–Nazarov extends to confluent Wang tails by total multiplicity

## Claim

Let

`F(x)=sum_(b in B) Q_b(x) exp(-i b x)`

be a nonzero confluent exponential polynomial on the real line, where the phases `b` are distinct real numbers and each nonzero polynomial `Q_b` has degree `d_b`. Define the total multiplicity

`N = sum_(b in B) (d_b+1)`.

Then the classical measurable Turán–Nazarov inequality for ordinary exponential sums extends to `F` with the same algebraic exponent `N-1`: there is an absolute constant `A` such that for every finite interval `I` and measurable `E subset I` with positive measure,

`sup_I |F| <= (A |I|/|E|)^(N-1) sup_E |F|`.

No minimum phase spacing enters this propagation inequality. In particular, arbitrarily close distinct phases do not create a separate local-concentration escape; near-coalescence can matter only through how small the reference norm `sup_I|F|` is relative to the underlying polynomial/phase coefficients.

Applied to the Wang interacting tail from `VIS-349`,

`E_(q,X)(xi)=sum_b exp(-i b xi) Q_(b,q,X)(xi)`,

let

`N_X=sum_b (deg Q_(b,q,X)+1) <= q B_X`

with zero coefficient polynomials omitted. If on an interval `J_X subset [X,2X]`

`sup_(J_X)|M_X| <= C_0 X^(-(q+1))`,

put

`D_(q,X)=2^q C_0 + C_q T_(q+1,X)`.

Then `VIS-349` gives

`sup_(J_X)|E_(q,X)| <= D_(q,X)/X`.

For every finite interval `I_X` containing `J_X`, with

`H_X=sup_(I_X)|E_(q,X)|`,

one therefore has either `H_X=0` (hence all first `q` phase-fiber moments vanish exactly by `VIS-349`) or the necessary budget

`X H_X / D_(q,X)`
` <= (A |I_X|/|J_X|)^(N_X-1)`.

Equivalently, whenever `X H_X>D_(q,X)`,

`(N_X-1) log(A |I_X|/|J_X|)`
` >= log(X H_X/D_(q,X))`.

Thus if the reference tail is nondegenerate in the sense

`D_(q,X)/H_X = X^(o(1))`,

one extra local inverse-frequency order forces

`(N_X-1) log(A |I_X|/|J_X|) >= (1-o(1)) log X`.

The unresolved finite-bank issue is therefore no longer a missing confluent propagation theorem. It is the **norming/conditioning problem** of proving that `H_X` cannot itself collapse relative to the Wang moment data unless the coefficients, phase geometry, or effective dimension pay for that collapse.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL TURAN-NAZAROV LIMIT ARGUMENT + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does not supply a uniform lower bound for `H_X` in terms of the raw Wang moment coefficients when phases approach one another or the polynomial coefficient system becomes ill-conditioned. It does not improve the Korobov–Vinogradov remainder or produce a source-coupled cancellation estimate for `G`.

## 1. Confluent exponentials are uniform limits of ordinary exponential sums

For one phase `b`,

`partial_b^r exp(-i b x)=(-i x)^r exp(-i b x)`,

so

`x^r exp(-i b x)=i^r partial_b^r exp(-i b x)`.

The forward finite difference gives, uniformly for `x` in every fixed compact interval,

`epsilon^(-r) sum_(s=0)^r (-1)^(r-s) C(r,s) exp(-i (b+s epsilon) x)`
` -> (-i x)^r exp(-i b x)`

as `epsilon->0`.

Hence each polynomially weighted term

`Q_b(x) exp(-i b x)`

with `deg Q_b=d_b` is a uniform compact-limit of an ordinary exponential sum using the `d_b+1` nearby pure-imaginary frequencies

`b, b+epsilon, ..., b+d_b epsilon`.

Summing over the finitely many distinct phases and choosing `epsilon` small enough that the clusters remain disjoint produces ordinary exponential sums `F_epsilon` with exactly `N` terms and

`F_epsilon -> F`

uniformly on `I`.

The coefficients in `F_epsilon` may diverge as powers of `epsilon^-1`, but this is harmless here because the measurable Turán–Nazarov constant depends on the number of terms and the real parts of the exponents, not on coefficient size or frequency separation. All approximating exponents are purely imaginary.

## 2. Pass the measurable Turán–Nazarov inequality through the confluent limit

For every `epsilon>0`, the ordinary `N`-term pure-imaginary exponential sum satisfies

`sup_I |F_epsilon|`
` <= (A |I|/|E|)^(N-1) sup_E |F_epsilon|`.

Uniform convergence on `I` implies convergence of both suprema. Passing to the limit gives

`sup_I |F|`
` <= (A |I|/|E|)^(N-1) sup_E |F|`.

This argument works pointwise in any external parameter. Therefore the phases, polynomial coefficients, and even their near-collisions may vary with `X`: for each fixed `X`, apply the finite-difference approximation to that finite confluent system and use the same absolute constant `A`.

Exact phase equality should first be grouped into one polynomial coefficient `Q_b`; near equality does not alter the inequality. The only combinatorial quantity charged by measurable propagation is the total confluent dimension `N`.

## 3. Wang local smallness now has an explicit total-multiplicity budget

`VIS-349` proves, for fixed finite truncation depth `q`,

`xi^q M_X(xi)=E_(q,X)(xi)+R~_(q,X)(xi)`

and on `J_X subset [X,2X]`, under one-extra-order attenuation,

`sup_(J_X)|E_(q,X)| <= D_(q,X)/X`.

Apply the confluent Turán–Nazarov inequality with `F=E_(q,X)`, `E=J_X`, and any containing reference interval `I_X`. Then

`H_X <= (A |I_X|/|J_X|)^(N_X-1) D_(q,X)/X`.

This separates two costs that were mixed together in the previous formulation.

The **propagation cost** is completely explicit: total multiplicity `N_X` and the measure ratio `|I_X|/|J_X|`. Phase spacing does not appear.

The **conditioning cost** is hidden only in the ratio `H_X/D_(q,X)`. Near-coalescing phases, polynomial coefficient cancellation, or a nearly singular confluent Vandermonde can help only by making the whole tail small already on the reference interval. That is no longer a local-concentration phenomenon; it is a norming statement about the coefficient-to-function map.

For example, if `N_X=N` is bounded, `D_(q,X)/H_X=X^(o(1))`, and `|I_X|/|J_X|=X^(alpha+o(1))`, then necessarily

`alpha (N-1) >= 1-o(1)`.

If `J_X` occupies a fixed positive proportion of `I_X`, bounded total multiplicity cannot manufacture the extra order under the nondegeneracy hypothesis.

## 4. What remains genuinely open

The remaining finite-dimensional loophole is now sharper: prove or disprove a useful lower bound of the form

`H_X >= kappa_X * ||moment-data_X||`

for a natural Wang moment norm, and quantify exactly how `kappa_X` can deteriorate under phase collision, polynomial multiplicity, scale geometry, or coefficient growth.

A construction that makes `kappa_X` polynomially small has paid for its local gain through global conditioning before any arithmetic property of the source `G` is used. Conversely, a source-coupled mechanism that beats the Wang output while `E_(q,X)` remains well-conditioned would have to leave the finite frequency-independent scalar-bank model rather than exploit an unpriced confluent Remez loophole.

This does not settle frequency-dependent/source-dependent coefficients, infinite expansions, or direct signed arithmetic cancellation in `G`; those remain qualitatively different branches of the accepted clue.

## Prior-art audit

F. L. Nazarov, **Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type**, *Algebra i Analiz* 5:4 (1993), 3–66; English translation *St. Petersburg Mathematical Journal* 5:4 (1994), 663–717, is the classical measurable propagation theorem used in `VIS-346`.

A. J. van der Poorten, **Generalisations of Turán's main theorems on lower bounds for sums of powers**, *Bulletin of the Australian Mathematical Society* 2:1 (1970), 15–37, DOI `10.1017/S0004972700041575`, is direct classical prior art for Turán-type lower bounds with polynomial coefficients, already recorded in `VIS-349`.

Omer Friedland and Yosef Yomdin, **An observation on the Turán–Nazarov inequality**, *Studia Mathematica* 218:1 (2013), 27–39, DOI `10.4064/sm218-1-2`, is a modern reference for the measurable Turán–Nazarov framework and its metric-entropy extension.

No new general Turán theorem is claimed. The Mathia-specific contribution is the elementary confluence limit combined with the exact Wang reduction of `VIS-349`, which identifies the correct budget for the currently active finite-bank question and moves the unresolved difficulty from propagation to coefficient/function conditioning.

## Dependencies

- `VIS-346`: measurable Turán–Nazarov propagation for ordinary Wang moment exponential polynomials.
- `VIS-347`: scale-dependent first-moment phase-entropy budget.
- `VIS-348`: higher first-surviving-moment budget after exact lower cancellations.
- `VIS-349`: exact reduction of all first `q` interacting Wang tail orders to one confluent exponential polynomial and the `O(X^-1)` local-smallness obligation.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed here.

## Research consequence

A special scale-dependent Turán theorem for confluent Wang tails is **not** the next missing step. Measurable propagation already follows from the classical ordinary Turán–Nazarov inequality by coalescing frequencies, with total multiplicity replacing term count and no spacing penalty.

Future finite-bank work should therefore target the reference-norm/conditioning map from Wang phase-fiber moments to `E_(q,X)`. Growing total multiplicity and shrinking windows have an explicit propagation cost; phase collision and coefficient cancellation matter only insofar as they make the entire confluent tail globally small relative to its natural moment scale. A genuinely different escape must use source/frequency dependence, infinite representation, or direct signed information in `G`.