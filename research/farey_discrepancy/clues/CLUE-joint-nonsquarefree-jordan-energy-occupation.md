---
id: CLUE-joint-nonsquarefree-jordan-energy-occupation
type: research-clue
status: accepted
origin: master-researcher
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/findings/FD-034-square-divisor-modes-force-four-adic-linear-prefix-saturation-gaps.md
  - research/farey_discrepancy/findings/FD-035-square-divisor-renormalization-alone-does-not-force-a-pointwise-linear-prefix-gap.md
  - research/farey_discrepancy/clues/CLUE-coherent-dyadic-staircases-cannot-jointly-saturate-gcd-duality.md
  - research/farey_discrepancy/clues/CLUE-joint-squarefree-sign-and-divisor-compatibility.md
---

# Does the full nonsquarefree Jordan-row union retain a positive fraction of the physical Schur energy?

## Observation

FD-034 identifies every nonsquarefree Jordan row as exactly transverse to the Schur equality direction. It uses one prime-square row family at a time to obtain a smaller-horizon energy lower bound and a four-adic average defect. FD-035 proves that even all the separate prime-square inequalities, together with monotone superlinear-to-quadratic abstract energy growth, do not forbid a cofinal vanishing-defect subsequence.

That control is an abstract energy profile, not the quotient-shell transform of the actual Mertens source. Before replacing every square family by a separate lower-horizon bound, the full union has an exact same-horizon energy. Its rows overlap arithmetically but are orthogonal coordinates in the Jordan norm. This suggests testing the union once, without double-counting, against the physical source rather than taking more separate recurrence inequalities.

## Research question

Fix the Schur-head dimension D. Use exactly the FD-034 quantities

\[
w(r)=J_2(r)/r^2,\qquad
\mathcal H(k)=\sum_{s\le k}\frac{\mathbf M(\lfloor k/s\rfloor)}s,
\qquad
E_{H,D}=\sum_{D<r\le H}w(r)\mathcal H(\lfloor H/r\rfloor)^2,
\]

where bold M is the actual Mertens summatory function. Define the joint nonsquarefree contribution

\[
U_{H,D}:=\sum_{\substack{D<r\le H\\\mu(r)=0}}
 w(r)\mathcal H(\lfloor H/r\rfloor)^2.
\]

Does there exist, for each fixed D, a constant c_D>0 such that U_{H,D}>=c_D E_{H,D} for every sufficiently large H? This is an unproved sufficient-channel question, not a conjecture that follows from the density of nonsquarefree integers. A weaker explicitly quantified restriction on the horizons where U/E is small is useful only if it improves on the already-known four-adic average control.

FD-034's vanishing equality coordinates suggest U_{H,D}<=rho_{H,D}^2, with rho its full transverse Schur residual. Thus a positive answer would imply a normalized projective gap. A negative answer for U/E would not refute such a gap: transverse contributions within the squarefree rows may still survive.

## Why it may matter

The test retains information discarded by the separate inequalities in FD-035: which square-divisor families receive energy at the same horizon, their overlap, and their coupling through one exact quotient-shell function. It asks for a fraction of the full energy, not an absolute nonsquarefree distance that can be diluted when E/H diverges.

This is distinct from the resolved squarefree-sign/divisor clue, which optimized synthetic increment signs under one divisor identity. Here the source is the actual Mertens transform and squarefreeness classifies Jordan rows, not freely chosen increments. It is also distinct from the accepted coherent-horizon clue: its immediate observable is a same-horizon energy fraction, not another averaged chain of scalar dual ratios.

## Decisive test

First verify the bound U<=rho^2 in the unchanged Schur/Jordan normalization, including the removal of the first D rows. Compute the union directly or by exact inclusion-exclusion. Summing the separate energies over primes is invalid without controlling multiplicity, since a row divisible by several prime squares must be counted only once.

Then group by the exact quotient-shell blocks

\[
\Gamma_{H,D}(k)=\{r:D<r\le H,\ \lfloor H/r\rfloor=k\},
\]

and set

\[
a_k=\sum_{r\in\Gamma_{H,D}(k)}w(r),\qquad
\nu_k=\sum_{\substack{r\in\Gamma_{H,D}(k)\\\mu(r)=0}}w(r).
\]

Check the finite identities E=sum_k a_k Hcal(k)^2 and U=sum_k u_k Hcal(k)^2, where Hcal denotes the displayed mathcal H. For nonempty blocks put theta_k=u_k/a_k. This converts the question into whether the physical energy can concentrate on blocks with small theta_k. Short or singleton blocks may have theta_k=0; a uniform lower bound on every block must not be assumed.

A concrete sufficient test is to choose fixed eta,delta>0 independently of the source values and establish

\[
\sum_{\substack{k:a_k>0\\\theta_k<\eta}}
 a_k\mathcal H(k)^2
\le(1-\delta)E_{H,D}.
\]

It would give U/E>=eta delta. The elementary implication is not the proposed mathematical contribution: the missing theorem is the source-specific weighted concentration bound. Derive the block weights exactly before invoking density estimates, and identify what controls energy on the thin exceptional blocks. Positivity, ambient nonsquarefree density, E/H tending to infinity, or the separate square recurrences do not by themselves establish this concentration estimate.

A finite diagnostic may evaluate these rational sums from the true Mobius prefix on predeclared horizons, reporting U/E and the distribution of energy across theta_k, including horizons with large energy increments. Preserve the full source prefix and all rows; do not select favorable horizons after inspecting the ratios. Finite positive fractions are not asymptotic evidence. An abstract spike profile may refute an intermediate implication but cannot refute the physical-source statement unless it also satisfies the exact quotient-shell relation.

If a bound survives, translate it into the precise normalized linear-prefix dual gap and state its actual consequence. A fixed scalar gap alone is not an improved Mertens exponent or an RH proof. If the union loses almost all energy in an admissible physical regime, identify the concentration mechanism and leave the squarefree transverse/longitudinal channels open rather than declaring the full projective route impossible.

## Evidence boundary

The cited current findings and the two relevant local clue dispositions were inspected at 7797f89e198f582ef44b54596d2d379b8ee540fb. Check current source and adjacent review state before adoption. No weighted occupation theorem, physical vanishing subsequence, numerical experiment, or formal verification is supplied here. Grouping finite sums and Jordan orthogonality are baseline tools; the proposed contribution is a source-sensitive concentration test that is not implied by FD-035's abstract recurrence inputs. If already covered by an existing joint-row result, link that result and close this clue rather than creating another finding from the same decomposition.

## Research disposition

Accepted. `FD-036` supplies a pointwise projective bound of order `H^(-1/2)` but does not answer whether the nonsquarefree rows themselves retain a fixed fraction of the physical Schur energy. The direction therefore remains mathematically distinct and worth pursuing.

[[research/farey_discrepancy/findings/FD-037-bounded-increments-localize-nonsquarefree-occupation-failure-to-a-cube-root-jordan-core.md]] proves the first source-specific reduction: if `U_(H,D)/E_(H,D)` tends to zero along an unbounded sequence, then asymptotically all of `E_(H,D)` must concentrate on Jordan rows `r=O(H^(1/3))`, equivalently quotient arguments of size at least order `H^(2/3)`. Outside that core, the exact one-Lipschitz law for `mathcal H` pairs every squarefree row with a bounded-distance nonsquarefree witness at total cost `O(H)`, which is negligible because `FD-033` gives `E_(H,D)/H -> infinity`.

[[research/farey_discrepancy/findings/FD-038-terminal-quotient-blocks-have-universal-nonsquarefree-jordan-occupation.md]] proves a complementary source-independent bulk law. For every fixed `alpha<1/3`, the terminal quotient range `k<=H^alpha` has nonsquarefree Jordan-energy fraction tending to the explicit weighted-density constant `delta_ns=0.3558...`, uniformly over the nonnegative shell values. For the physical source this terminal region alone has energy `~H Q(H^alpha)/zeta(3)` and is superlinear. Consequently any sequence with `U/E->0` must satisfy `E/(H Q(H^alpha))->infinity` for every `alpha<1/3`, while `FD-037` simultaneously forces almost all energy into `r=O(H^(1/3))`.

The precise unresolved question is therefore sharper than cube-root-core concentration alone: can the sparse hyperbola samples `mathcal H(floor(H/r))` with `r<=H^(1/3)` overwhelm by an unbounded factor every growing terminal critical-square prefix `H Q(H^alpha)`, `alpha<1/3`? Excluding that hyperbola-sampling amplification for one fixed `alpha<1/3` would yield `U/E>=c_D>0` and hence a fixed projective linear-prefix gap. Ambient nonsquarefree density is now known to be fully effective in the long terminal quotient blocks; the unresolved arithmetic lies in the thin low-row sample geometry.
