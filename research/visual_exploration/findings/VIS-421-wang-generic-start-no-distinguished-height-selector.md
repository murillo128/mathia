# VIS-421 — Wang's generic interval start supplies no canonical distinguished-height selector

## Claim

The Wang short-interval interface used by the current shell program does **not** itself select a sparse or otherwise distinguished set of observation heights.

In Biao Wang's source, the asymptotic parameter is the generic interval start `T`, with

`H=T^theta`, `L=log T`, `I=(T,T+H]`,

for fixed `0<lambda<theta<1`. The main theorem is stated through a `liminf_(T->infinity)`, and the explicit-formula input is valid for ordinary real `t in I` and `1<=x<=T^lambda`. The Dirichlet polynomial

`D_x(t)=sum_(n>=2) a_n n^(-it)`,

with

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`,

therefore carries a continuously varying time coordinate. Nothing in this imported interface defines a selector

`S={T_1,T_2,...}`

of Gram points, zero ordinates, extrema, special congruence heights, or any other discrete arithmetic panel.

Consequently the fixed-shell Haar law from `VIS-419` and its finite-window calibration from `VIS-420` answer a **conditional self-null** question: after freezing one shell, how atypical is a chosen phase point relative to translations of that same shell? They do not by themselves make the chosen height source-selected.

A multi-height test therefore needs two additional pieces of data before values are inspected:

1. an independently justified deterministic height selector `S`;
2. when the panel spans changing asymptotic scale, a pre-specified shell-family rule that tells how `H`, `x`, the dyadic shell, bandwidth normalization, and persistence radius vary with the selected height.

Without the first item, there is no distinguished-height hypothesis to test. Without the second, a cross-height comparison can mix phase alignment with changes in the shell itself.

If `S` comes from another zeta structure, such as a Gram-type or zero-defined rule, a low Haar-tail value can still be mathematically interesting, but its correct interpretation is **cross-structure alignment between that external selector and the Wang shell family**, not phase anchoring supplied by Wang's short-interval source alone.

**Evidence/status:** `SOURCE-INTERFACE AUDIT + EXACT REPRESENTATION/CONTROL BOUNDARY + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No assertion is made that no useful external arithmetic selector exists. The result only identifies what the Wang interface currently imported by this line does and does not provide.

## 1. The source height is a generic asymptotic coordinate

Wang fixes

`0<lambda<theta<1`, `H=T^theta`, `L=log T`, `I=(T,T+H]`.

Theorem 1.1 concerns the limiting proportions of simple critical and distinct zeros in `(T,T+T^theta]` as `T->infinity`. The short-interval pair-correlation theorem is likewise written for this generic `I`.

The explicit formula then introduces, for real `t`,

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`

with

`D_x(t)=sum a_n n^(-it)`

and states the approximation for `t in I`, uniformly over `1<=x<=T^lambda` in the subsequent estimates. Thus `T` locates an arbitrary large interval and `t` moves continuously through it. The source theorem does not attach a special combinatorial or arithmetic label to particular starting heights inside the asymptotic variable.

This is enough for the present boundary. The claim is not an absence statement about every conceivable zeta construction; it is an audit of the exact Wang interface from which the Mathia shells were derived.

## 2. Freezing a shell changes the question in a controlled way

The visual line groups Wang's prime-power Dirichlet-polynomial terms into finite real exponential sums of the form

`F_i(T)=sum_(lambda in Lambda_i) B_(i,lambda) exp(-i lambda T)`.

For a **fixed** shell, `VIS-419` proves that translation in `T` is the Kronecker flow on the finite base-prime torus and that long translation converges to the exact Haar pushforward of the corresponding character polynomial. `VIS-420` quantifies finite-window error for finite character-polynomial observables through the active small divisors.

That calibration is deliberately conditional on freezing the shell data. It asks whether a particular phase point of a particular finite trigonometric polynomial is unusual relative to the same polynomial's translation orbit.

Wang's source family, however, also carries scale dependence through at least `H=T^theta`, `L=log T`, and the admissible range `x<=T^lambda`. A source-faithful test at several widely separated heights cannot silently identify all those source instances with one frozen shell. It must state which shell parameters are frozen and which are transported with the selected height.

This does not invalidate the fixed-shell Haar null. It identifies its exact role: **within-shell phase calibration**, not a complete across-height source model.

## 3. Selector provenance is a separate information channel

Suppose a deterministic panel `S={T_j}` is chosen by a rule independent of the shell values. For each selected height, a shell-family rule produces `F_j`, and the observed statistic is compared with the exact Haar self-null of that frozen `F_j`.

Then each resulting tail rank answers a valid conditional question. But any systematic excess across the panel depends on information in two objects:

- the Wang-derived shell family;
- the rule that selected the heights.

If the selector is not part of Wang's source interface, the residual cannot be attributed to Wang alone. This is analogous to an alignment test between two deterministic arithmetic structures: the potential signal lies in their coupling.

The distinction matters because `VIS-418` already showed that translation can place or remove quiet regions without changing frequency geometry, while `VIS-419` identified the exact translation self-null. Once translation is calibrated, the only way a deterministic panel can be special is through how its selector samples the shell phases. Selector provenance is therefore not bookkeeping; it specifies the second structure whose coupling is being tested.

## 4. Pre-registration consequence

The accepted clue `CLUE-wang-phase-anchored-small-values` correctly requires the arithmetic height panel, shell family, statistic, and numerical rule to be fixed before inspecting comparison values. The present audit sharpens what that pre-registration must contain.

A valid test specification must state:

- the deterministic rule defining the height panel and why that rule is mathematically prior to the observed shell values;
- whether the selector is claimed to come from Wang's construction or from an explicitly external zeta/arithmetic structure;
- the shell-family transport rule across heights, including the choices of `theta`, `lambda`/`x`, dyadic shell identity or scaling rule, and bandwidth normalization;
- the persistence radius or its scale law when a quiet-region statistic is used;
- the panel-level aggregation rule if more than one conditional Haar tail rank is to support one claim.

The first two items cannot be recovered after seeing the data without reintroducing selection bias. The third is needed because changing `T` changes the source asymptotic scales even before phase is considered.

Therefore the next substantive step is **not yet numerical evaluation of an unspecified distinguished-height panel**. It is to freeze a selector with explicit provenance and a covariant shell-family rule. Once those are fixed, `VIS-419` and `VIS-420` already provide the correct fixed-shell null/calibration machinery.

## 5. Prior art and novelty boundary

The source-side facts are directly from Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals*, arXiv:2609.07918v1 (2026): Theorem 1.1 uses `liminf_(T->infinity)` for intervals `(T,T+T^theta]`; the notation section fixes `H=T^theta`, `L=log T`, `I=(T,T+H]`; equations (2.7)--(2.9) give the explicit formula and `D_x(t)` for real `t in I`; the subsequent estimates are uniform for `1<=x<=T^lambda` where stated.

No novelty is claimed for those facts, for pre-registration as statistical discipline, or for the general observation that an externally selected sample introduces information through the selector. The durable Mathia contribution is the interface audit against the exact `VIS-416`--`VIS-420` program: it prevents the fixed-shell Haar self-null from being over-interpreted as though Wang's source had already supplied the panel on which phase anchoring is to be tested.

## 6. Boundaries and falsification

This finding does **not** reject the possibility that a natural external selector is valuable. A Gram-point rule, a zero-derived rule, or another canonical zeta construction could define a legitimate panel if it is fixed independently of the shell observations. Such an experiment would test a cross-structure relation.

It also does not require all heights in a panel to use identical shells. A varying shell family is allowed; the point is that its transport/scaling rule must be specified before inspecting the anomaly.

The finding would be falsified if the Wang source interface actually used by the canonical shell derivation contains a deterministic distinguished-height selector that was omitted here and that survives as part of the shell construction, rather than merely treating `T` as the generic interval start. In that case the selector should be identified explicitly and the clue can revert to a genuinely source-internal anchoring test.

## Dependencies

- `VIS-416`: bandwidth-normalized amplitude isolates the candidate small-value factor.
- `VIS-418`: fixed-height quiet-region incidence depends on phase/time-origin alignment even with frequency geometry fixed.
- `VIS-419`: the exact fixed-shell self-null is the base-prime Haar pushforward.
- `VIS-420`: finite translation calibration pays explicit small divisors and does not replace direct Haar for nonlinear tails.
- Biao Wang, arXiv:2609.07918v1: source definition of the short-interval height/scale interface.

## Research consequence

The accepted phase-anchoring clue remains potentially fertile but must be narrowed. Before any distinguished-height computation, freeze the selector provenance and the shell-family transport rule. If the selector is external to Wang, interpret any surviving anomaly as a coupling between that selector and the Wang shell family. Only a selector derived from the same source interface would justify the stronger phrase "Wang-source-selected height".