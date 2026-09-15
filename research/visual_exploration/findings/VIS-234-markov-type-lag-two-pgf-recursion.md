# VIS-234 — fixed-transition lag-two law has an exact finite generating recursion

## Claim

Let `A` be a finite alphabet and let `C=(C_(ij))_(i,j in A)` be a feasible first-order transition-count matrix with fixed initial state `s` and terminal state `t`. Let `Omega(C;s,t)` be the set of distinct state sequences

`x_1,...,x_(N+1)`, `N=sum_(i,j) C_(ij)`,

with `x_1=s`, `x_(N+1)=t`, and exactly `C_(ij)` occurrences of transition `i->j`. For

`T_2(x)=sum_(r=1)^(N-1) 1_{x_r=x_(r+2)}`,

the complete conditional distribution of `T_2` under the uniform law on `Omega(C;s,t)` is determined by an exact finite recursion on the remaining transition counts.

For a nonnegative remaining matrix `R` and a current two-state suffix `(u,v)`, define the polynomial `F_(R;u,v)(q)` to be the generating polynomial of all valid completions that use exactly the transitions in `R` and finish at `t`, weighted by the additional lag-two returns created after the current prefix. Then

`F_(0;u,v)(q)=1_{v=t}`

and, for `|R|>0`,

`F_(R;u,v)(q)=sum_(w:R_(vw)>0) q^(1_{u=w}) F_(R-E_(vw);v,w)(q)`.

If `N>=1`, the full type polynomial is

`Z_(C;s,t)(q)=sum_(v:C_(sv)>0) F_(C-E_(sv);s,v)(q)`.

Therefore

`[q^k] Z_(C;s,t)(q) = #{x in Omega(C;s,t): T_2(x)=k}`,

`Z_(C;s,t)(1)=|Omega(C;s,t)|`,

and, whenever the type is nonempty,

`P(T_2=k | C,s,t)=[q^k]Z/Z(1)`.

In particular the exact admission gate for the candidate statistic is algebraic: `T_2` is nondegenerate inside the endpoint-matched first-order type if and only if `Z_(C;s,t)` is not a monomial.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CONDITIONAL-PATTERN ENUMERATION SPECIALIZATION + COMPUTATIONAL ADMISSION GATE + NO-NOVELTY-CLAIM`.

No claim is made that this recursion is a new general enumeration algorithm, that the actual prime-phase type has nonzero variance, that uniform conditioning on a Markov type is the uniquely correct scientific null, or that any resulting residual has an RH consequence.

## 1. Why the recursion is exact

Suppose a partially constructed state sequence ends in `(u,v)` and the unused transition multiset is `R`. Any next state `w` must satisfy `R_(vw)>0`. Appending `w` consumes one `v->w` transition and contributes exactly one new term to `T_2`, namely `1_{u=w}`. After that step the only information needed for future lag-two returns is the new suffix `(v,w)` together with the remaining transition counts.

This gives the displayed recurrence by partitioning the valid completions according to their next state. The partition is disjoint and exhaustive.

There is deliberately **no factor `R_(vw)`** in the recurrence. The conditional sample space here consists of distinct state sequences, not Euler trails with separately labelled copies of repeated edges. Choosing the next state `w` determines the next symbol of the state sequence; indistinguishable occurrences of the same transition do not create distinct realizations. This is the same sequence-level conditional object used in the fixed-transition-count Markov-type literature cited in `VIS-233`.

The terminal condition is also essential. A remaining matrix can admit a path from the current state only for some endpoint; `F_(0;u,v)=1_{v=t}` removes completions with the wrong final state automatically.

## 2. Exact support, moments, and nondegeneracy

The polynomial itself gives the full conditional support. If only the admission question is needed, one can propagate the minimum and maximum attainable lag-two counts with the same state recursion:

`L(0;u,v)=U(0;u,v)=0` when `v=t`, with infeasible terminal states excluded, and

`L(R;u,v)=min_(w:R_vw>0) {1_{u=w}+L(R-E_vw;v,w)}`,

`U(R;u,v)=max_(w:R_vw>0) {1_{u=w}+U(R-E_vw;v,w)}`.

Thus `T_2` is nondegenerate exactly when the full initial recursion has `L<U`. The polynomial is still needed when the shape of the conditional law matters.

Exact moments follow without enumerating individual realizations once `Z` is known:

`E[T_2]=Z'(1)/Z(1)`,

`Var(T_2)=Z''(1)/Z(1)+E[T_2]-E[T_2]^2`.

Equivalently, a memoized implementation can propagate the triple `(count, first moment sum, second raw moment sum)` instead of full polynomials when only mean and variance are required. The state space is finite: for fixed alphabet it is bounded by the current suffix choices times `prod_(i,j)(C_(ij)+1)`. This may still be large for a high-resolution phase partition, but it is an exact finite benchmark rather than a Monte Carlo assumption.

## 3. Recovery of the VIS-233 witness

For the binary endpoint-matched type

`C_00=2`, `C_01=1`, `C_10=1`, `C_11=0`, `s=t=0`,

the recursion gives

`Z(q)=q+2q^2`.

Hence there are three distinct realizations, the support is `{1,2}`, and

`E[T_2]=5/3`, `Var(T_2)=2/9`,

exactly reproducing the direct enumeration in `VIS-233`. This is a self-check of both the no-edge-multiplicity convention and the endpoint handling.

## 4. Prior-art and novelty boundary

Whittle's classical transition-total formulas count Markov-chain realizations conditional on observed transition totals. Cowan's 1991 and 1993 work explicitly studies expected pattern frequencies over realizations with fixed transition counts, including the fact that the relevant realizations are equiprobable under the conditioned Markov-chain model. Those sources already place conditional higher-block pattern counts inside established Markov-type combinatorics.

The recursion above is therefore not claimed as a new theorem in that literature. It is an elementary dynamic-programming specialization to the exact Mathia admission question left by `VIS-233`: before treating `T_2` as a critical prime-phase confirmation statistic, determine its endpoint-matched conditional support and law for the realized first-order type rather than assuming that a generic nondegeneracy witness transfers to that type.

## Boundaries and falsification

The uniform law on `Omega(C;s,t)` is one explicit conditional null. If the scientifically justified null weights compatible sequences nonuniformly, the recursion must carry those weights and the displayed uniform probabilities are not the correct calibration.

The exact recursion does not solve model selection. A nondegenerate conditional law only proves that `T_2` survives the chosen first-order conditioning sigma-field. It does not make the statistic prime-specific, independent of phase-cell representation, or relevant to the signed prime-phase kernel.

For large transition tables the exact state space can be computationally prohibitive. Approximate samplers remain possible, but then they should be validated against the exact recursion on reduced or coarsened types before their tails are trusted for confirmation.

Falsify the exact claim by exhibiting a feasible endpoint-matched transition type for which the recurrence miscounts a compatible state sequence, assigns an incorrect lag-two exponent, or fails to reproduce direct enumeration.

## Research consequence

`VIS-233` supplied a concrete statistic outside the endpoint-matched range-one sigma-field. This finding supplies the exact next admission test: construct the actual critical prime-phase transition table for a predeclared representation, evaluate `Z_(C;s,t)` (or at minimum its exact support/moments), and kill `T_2` immediately if that conditional law is degenerate or nearly degenerate.

If exact evaluation is too large, the recursion remains a reference object for validating a conditional sampler on tractable reductions. Only after this type-level calibration is frozen should the observed prime-phase value be compared with the conditional law and then tested for stability and signed-kernel relevance.