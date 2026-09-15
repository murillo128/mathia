# VIS-235 — lag-two Markov-type mean reduces to two-step deletion counts

## Claim

Let `A` be a finite alphabet, let `C=(C_(ij))_(i,j in A)` be a feasible first-order transition-count matrix, and fix initial and terminal states `s,t`. Write

`Omega(C;s,t)`

for the distinct state sequences with those endpoints and transition counts, and

`W(C;s,t)=|Omega(C;s,t)|`.

For

`T_2(x)=sum_(r=1)^(N-1) 1_{x_r=x_(r+2)}`,

there is an exact first-moment formula that does not require the full suffix dynamic program of `VIS-234`.

For `u,v in A`, let `D^(u,v)` remove the two transitions of a lag-two return:

- if `u!=v`, `D^(u,v)=E_(uv)+E_(vu)`;
- if `u=v`, `D^(u,u)=2E_(uu)`.

Put `C^(u,v)=C-D^(u,v)`, and interpret `W(C^(u,v);s,t)=0` whenever the reduced matrix is negative or infeasible. For a feasible reduced type define

`a_u(C^(u,v);t)=sum_j C^(u,v)_(uj)+1_(u=t)`,

the number of occurrences of state `u` in every sequence of `Omega(C^(u,v);s,t)`.

Then

`sum_(x in Omega(C;s,t)) T_2(x)`
` = sum_(u,v in A) a_u(C^(u,v);t) W(C^(u,v);s,t)`,

and therefore, when `W(C;s,t)>0`,

`E[T_2 | C,s,t]`
` = [sum_(u,v) a_u(C^(u,v);t) W(C^(u,v);s,t)] / W(C;s,t)`.

Since each `W` is a standard fixed-transition Markov-type cardinality, Whittle's classical determinant formula can evaluate every term. Thus the conditional center of `T_2` requires only the original type count plus at most one reduced-type count per ordered pair `(u,v)` that can support a two-step return, rather than the full state space `prod_(i,j)(C_(ij)+1)` of the exact law recursion.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-PATTERN-EXPECTATION SPECIALIZATION + COMPUTATIONAL SIMPLIFICATION + NO-NOVELTY-CLAIM`.

The identity does not replace the `VIS-234` recursion when support, variance, tails, or nonzero constant degeneracy are needed.

## 1. Mark a return and delete its two-step excursion

Fix `u,v`. Count pairs `(x,r)` with `x in Omega(C;s,t)` and

`x_r=u, x_(r+1)=v, x_(r+2)=u`.

Collapse the marked block `u,v,u` to the single state `u`. The resulting sequence has the same initial and terminal states and transition-count matrix `C^(u,v)`: the collapse removes exactly `u->v` and `v->u`, or two copies of `u->u` when `u=v`, and leaves the transitions immediately before and after the block unchanged.

Conversely, take `y in Omega(C^(u,v);s,t)` and choose an occurrence of state `u` in `y`. Replace that occurrence by `u,v,u`. This inserts exactly the two removed transitions and marks the newly inserted lag-two return. Collapse and insertion are inverse operations on marked objects, including endpoint occurrences and the self-loop case `u=v`.

Every sequence with transition counts `C'` contains a fixed number of occurrences of `u`: each occurrence except a possible terminal occurrence emits one outgoing transition, so

`# {k:y_k=u} = sum_j C'_(uj)+1_(u=t)`.

Hence the number of marked `u,v,u` occurrences over all sequences of the original type is exactly

`a_u(C^(u,v);t) W(C^(u,v);s,t)`.

Summing over all ordered pairs `(u,v)` counts every term in `T_2` once and proves the formula.

## 2. The VIS-233 binary witness is recovered immediately

For the witness type

`C_00=2, C_01=1, C_10=1, C_11=0, s=t=0`,

there are `W(C;0,0)=3` compatible sequences.

The loop return `(u,v)=(0,0)` removes the two `0->0` transitions. The reduced type has one compatible sequence and contains two occurrences of `0`, contributing `2` marked returns.

The excursion `(u,v)=(0,1)` removes `0->1` and `1->0`. The reduced type again has one compatible sequence and contains three occurrences of `0`, contributing `3` marked returns.

Thus the total lag-two count over the type class is `2+3=5`, so

`E[T_2]=5/3`,

matching the polynomial `Z(q)=q+2q^2` from `VIS-234`.

## 3. Cheap zero-degeneracy gate and computational role

All terms in the numerator are nonnegative integers. Therefore

`E[T_2 | C,s,t]=0`

if and only if every compatible sequence has `T_2=0`.

This gives a cheap exact rejection gate before building the full generating polynomial: if every two-step deletion produces an infeasible reduced type, then `T_2` is identically zero under the conditioned type. In particular, no sequence can contain a lag-two return unless the transition multiset contains either a reciprocal pair `u->v, v->u` or at least two copies of a self-loop.

When the mean is positive, this test alone does **not** establish nondegeneracy. `T_2` could be the same positive constant on every compatible sequence. The min/max or polynomial recursion of `VIS-234` is still required to distinguish that case and to obtain the exact conditional law.

The practical value is narrower: Whittle cardinalities provide an independent exact center for testing an implementation or conditional sampler and can cheaply kill zero-support types before the higher-dimensional dynamic program is attempted.

## 4. Prior art and novelty boundary

Whittle's 1955 work gives the classical exact cardinality/probability formula for sequences conditioned on transition totals. Richard Cowan's 1991 paper, *Expected frequencies of DNA patterns using Whittle's formula* (`Journal of Applied Probability` 28:4, 886–892, DOI `10.2307/3214691`), explicitly develops exact expected pattern frequencies over sequences with fixed transition counts, and his 1993 note (`Theory of Probability & Its Applications` 37:2, 320–322, DOI `10.1137/1137065`) states the same conditional-pattern problem in that general framework.

The displayed deletion identity is therefore **not claimed as a new general Markov-type theorem**. It is an elementary length-three specialization tailored to Mathia's active statistic `T_2`, with the useful consequence that its conditional center can be computed through a sparse family of Whittle type-cardinality ratios before invoking the complete `VIS-234` recursion.

The derivation above is independent of those sources; the sources determine the novelty boundary and provide the standard exact evaluation machinery for `W`.

## Boundaries and falsification

The formula assumes the uniform law on distinct compatible state sequences, exactly as in `VIS-234`. A different conditional weighting requires weighting both the original and reduced type classes consistently; unweighted Whittle cardinalities would then give the wrong center.

The insertion count is a count of **state occurrences**, not labelled parallel edges. Introducing a factor such as `C_(uv)` would change the sample space and overcount repeated transitions.

The endpoint correction `1_(u=t)` is necessary. Omitting it loses insertions at the final state and fails even on small endpoint-matched types.

Falsify the claim by exhibiting a feasible finite type for which direct enumeration of the distinct compatible state sequences gives a total `T_2` different from the deletion sum above.

## Research consequence

`VIS-234` made the full conditional `T_2` law exact but potentially expensive. This result separates the cheapest exact calibration from the full admission test: first evaluate the Whittle deletion center and the zero-degeneracy gate; only types that survive then need support/variance or full-law computation.

For the accepted critical prime-phase occupancy clue, this reduces the next computational burden without changing the scientific standard. A positive or unusual conditional center is not prime-specific evidence; the actual prime-phase type still needs a frozen support/variance calibration, confirmation comparison, representation-stability test, and a bridge back to the signed prime-phase kernel.