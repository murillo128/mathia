---
id: CLUE-prime-lattice-density-one-dyadic-variance-arithmetic-recovery
type: research-clue
status: resolved
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-523-density-one-dyadic-window-control-permits-near-linear-prefixes.md
  - research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md
  - research/prime_lattice/findings/PL-467-relative-frame-admits-sparse-common-off-critical-poles.md
---

# Can arithmetic pole constraints recover zero exclusion when sparse dyadic blocks are missing?

## Observation

PL-466 assumes complete empirical variance at every sufficiently large dyadic block. Its seam-weighted Mellin decomposition has a vertically periodic mean factor and an error holomorphic for `Re s>1-theta/2`. Arithmetic sublinear pole counts remove poles of the periodic factor; a finite-difference recurrence then recovers the unfiltered logarithmic derivative. Neither the unknown means nor dyadic sampling alone lose the zero information.

MC-523 defeats a different, generic coverage repair. It constructs one nonmultiplicative sequence `a` with `|a(n)|=mu(n)^2` and all qualitative fixed-shift Chowla correlations. On the predetermined set

`G = {1,2,...} \ {3^k-1,3^k : k>=2}`,

every sufficiently large retained block `X=2^j` has `|sum_(y<n<=y+H) a(n)|<=4 sqrt(H log X)` for every integer `1<=H<=X` and real `X<=y<=2X`. Thus the complete uncentered moment is at most `16 X H log X`, and its empirical variance is no larger. Only `O(log J)` indices up to `J` are omitted, with no run longer than two omissions. Yet some prefixes have size `>>T/log T`. The construction overwrites sparse intervals that none of the retained windows meets. It supplies no multiplicativity, reciprocal-zeta continuation or sparse pole law.

PL-467 supplies a complementary control with positive integer-supported coefficients and finitely many noncancelling off-critical poles, but its absolute centered variance exceeds the ceiling at every sufficiently large scale whenever its pole frontier is beyond `1-theta/2`. It therefore does not answer whether sparse omissions can coexist with those analytic constraints and the retained absolute ceiling.

## Research question

Fix `0<theta<1`, finite `A>=0`, the explicit set `G` above, and PL-466's actual source

`P_j(y)=sum_(y<n<=y+H_j, n=1 mod 5) Lambda(n)`,
`X_j=2^j`, `H_j=floor X_j^theta`, `mu_j=X_j^(-1) int_(X_j)^(2X_j) P_j(y) dy`.

If `V_j=int_(X_j)^(2X_j)|P_j-mu_j|^2 << X_j H_j (log X_j)^A` holds only for all sufficiently large `j in G`, does the same zero-free conclusion for all four mod-5 Dirichlet factors in `Re s>1-theta/2` follow? No bound on omitted-block variances or means, other window lengths, or non-dyadic scales is supplied.

The first unsupported implication is control of the omitted-block Mellin remainder, before PL-466's pole recurrence can be invoked. The density-one and bounded-gap properties of `G` do not give such control by themselves. Start with this explicit mesh; a theorem for arbitrary density-one or source-selected scales would be a separate extension.

## Why it may matter

The complete-dyadic transfer currently makes its near-one fixed-exponent family a strong sufficient zero-free input. A valid transfer from this weaker coverage would weaken the sufficient coverage premise; a precise analytic obstruction would identify what must be added to selected-shell estimates. The explicit mesh is a test of coverage, not a claim that Farey's carrying scales contain it. No outcome here supplies an independent arithmetic variance bound.

## Decisive test

Retain PL-466's finite seam weight, local inversion and empirical means. With its notation `W_j=b_j J_m+R_j`, sum the identity separately over `j in G` and `j notin G`. The good-block remainder has the existing holomorphy bound. Keep the missing series `sum_(j notin G) 2^(-js) R_j(s)` explicit rather than treating index density zero as a convergence estimate. Determine whether the actual logarithmic-derivative structure, noncancelling negative residues and sublinear off-critical pole counts force a usable continuation or compatibility law for that series. Do not assume the all-block decomposition's holomorphic error before justifying this step.

For a negative test of sufficiency of the **abstract analytic inputs**, seek a single integer-supported coefficient source `0<=b_n<<log(2n)`, vanishing at multiples of 5, with the same residue-channel bookkeeping, leading mass `x/4+o(x)` in each nonzero residue, meromorphic continuation in the relevant strip, simple noncancelling negative real off-critical residues and pole count `o(T)` in every fixed half-plane `Re s>=sigma>1/2`, while satisfying the retained absolute variance ceiling and possessing a pole beyond `1-theta/2`. Preserve every hypothesis claimed in the proposed inference. MC-523's arbitrary overwrite does not establish continuation or pole sparsity; PL-466's dyadic density has a linear-density pole progression; PL-467's finite-pole control fails the retained ceiling. None already supplies this counterexample. A control lacking the actual Euler product or functional equation could delimit the abstract method but could not refute a stronger actual-prime implication. Failure to construct one is not a proof.

If recovery requires an additional bound on the omitted remainder, state that bound as an explicit extra hypothesis and check whether it is weaker than reinstating the missing variances. Separate a proved conditional transfer, a matched-control obstruction and an unfinished method audit. Perform the ordinary prior-art audit for lacunary Mellin series and sparse-scale variance converses before claiming a new result.

**Bounded source reading for Prime Lattice:** inspect exactly `research/mobius_cancellation/findings/MC-523-density-one-dyadic-window-control-permits-near-linear-prefixes.md` for the retained-window geometry, the density-zero overwrite, and the missing arithmetic assumptions. Include its adjacent `research/mobius_cancellation/findings/MC-523-density-one-dyadic-window-control-permits-near-linear-prefixes.review.md` if present. The inspected source revision is `43eb7906bbf746e9d31a1ab8af68ca526fe97831`. Recheck current source and review state. This read-only grant permits no other Möbius files or recursive dependency traversal; MC-523 gives its construction in full. PL-466 and PL-467 are destination-local sources.

## Evidence boundary

The actual-prime implication is now proved conditionally in PL-471: the complete empirical variance ceiling on the specified retained mesh excludes mod-5 zeros in `Re s>1-theta/2`. The ceiling itself remains unproved. The result uses the actual logarithmic-derivative explicit formula and a power-saving zero-density estimate; it is not a recovery theorem for arbitrary meromorphic sources with merely `o(T)` poles. No RH/GRH result or effective sampling guarantee is asserted.

## Research disposition

Outcome: supported

Resolved by:
- [[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block]]

PL-471 resolves the original actual-source question by a different test from the omitted-block Mellin decomposition. A compactly supported test annihilates every unwanted off-critical zero in a fixed right half-plane. The arithmetic explicit formula, followed by finite-order additive-window inversion, forces `V_1(X,floor X^theta)>=c H^2 X^(2beta-1)` on every sufficiently large real block if a zero with real part `beta>1/2` exists. Hence any unbounded set carrying the full ceiling suffices; the original retained dyadic mesh is an immediate instance, and no estimate on omitted blocks or their means is supplied or needed.

This is an explicit extension beyond the initial fixed mesh. It does not establish that any source-selected or Farey-selected scale set carries the required variance estimate. The constants depend on the full zero set and are non-effective. PL-468's fixed-profile natural-boundary obstruction and PL-469's positive meromorphic control remain valid; the latter fails the quantitative strip-growth input identified in PL-470. The broader meromorphic-control question from the negative test is not conflated with the now-resolved actual-prime implication.
