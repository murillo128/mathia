---
id: CLUE-prime-lattice-dyadic-variance-smooth-endpoint-recovery
type: research-clue
status: resolved
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md
  - research/prime_lattice/findings/PL-464-dyadic-empirical-variance-residue-rigidity.md
  - research/prime_lattice/findings/PL-465-relative-frame-transfers-dirichlet-zero-bounds.md
  - research/prior_art/incremental/PA-van-cittert-approximate-deconvolution.md
---

# Can smooth recovery remove the dyadic variance endpoint loss without estimating block means?

## Observation

MC-521 separates smooth analytic recovery from sharp endpoint reconstruction. For fixed `0<theta<1`, `0<eta<=1`, and `H=X^theta`, a complete uncentered Möbius moment bounded by `O_epsilon(X^(1+epsilon) H^(2-eta))` for every `epsilon>0` and every sufficiently large real scale implies nonvanishing in `Re s>1-theta eta/2`. With `B_h w(z)=h^(-1) int_0^h w(z-u) du` and smooth `w` compactly supported in `(1,2)`, its finite correction uses

`B_h sum_(j<K)(I-B_h)^j w = w-(I-B_h)^K w`,

with `h=H/X` and remainder `O_w(h^K)`. Choosing fixed `K(1-theta)>theta eta/2` removes the endpoint exponent from that analytic implication. The arithmetic variance premise remains unproved.

PL-465 already has the corresponding local mean-zero smooth recovery for prime windows at all real scales. Repeating that interior calculation is therefore not the missing test. PL-464 instead assumes empirical variance only at `X_j=2^j`, with `H_j=floor(X_j^theta)`. It obtains the half-plane `Re s>max(1-theta/2,theta)`: its sharp-block reconstruction leaves `O(H_j log X_j)` at the block endpoints. Unknown block masses are retained in a vertically periodic meromorphic factor, and the real residues of the identity-residue logarithmic derivative rule out surviving zero poles. PL-464 expressly does not establish optimality of the endpoint loss.

## Research question

For fixed `2/3<theta<1` and finite `A>=0`, retain exactly PL-464's hypothesis at every sufficiently large integer `j`:

`int_(X_j)^(2X_j) |P_j(y)-bar P_j|^2 dy << X_j H_j (log X_j)^A`,

where `P_j(y)=sum_(y<n<=y+H_j, n=1 mod 5) Lambda(n)` and `bar P_j` is its empirical mean. Does this imply that all four mod-5 Dirichlet factors are zero-free in `Re s>1-theta/2`, without bounds on the means, non-dyadic scales, or additional window lengths?

The proposed route is finite smooth recovery combined with compatibility across adjacent dyadic blocks. The unsupported step is to remove the seam error while retaining enough information about the arbitrary means to use the arithmetic pole residues. Smooth interior estimates alone do not supply this step.

## Why it may matter

A positive answer would decide whether the current best dyadic boundary `2/3` is a sharp-block proof limitation. Applied separately to fixed exponents approaching one, the stronger implication would make that family of unproved dyadic variance bounds sufficient for joint GRH modulo 5. It would not establish the bounds. A precise seam obstruction would instead distinguish sparse-scale information from the all-real-scale recovery in MC-521 and PL-465, preventing an unjustified transfer between them.

## Decisive test

First analyze two consecutive blocks `[X,2X]` and `[2X,4X]`, with their actual, different window lengths. Apply finite box correction to interior mean-zero tests and explicitly retain every boundary-supported term and every unknown mean. Determine whether the two stated variance bounds control the seam correction at the smooth scale `X^(1-theta/2)` up to logarithmic or arbitrarily small power losses. Do not add variance information at neighboring lengths or estimate either mean by its expected density.

For a successful global proof, provide an exact replacement for PL-464's decomposition of

`D_1(s)=(1/4) sum_(chi mod 5) -L'(s,chi)/L(s,chi)`.

Its error must be locally uniformly holomorphic for `Re s>1-theta/2`. Any surviving mean factor must have an explicit law sufficient to exclude a single pole with the actual negative real residue `-(1/4) sum_chi m_chi(rho)`. Simply smoothing each disjoint block can leave gaps at every dyadic seam or destroy the periodic factor; neither can be suppressed as negligible without an estimate. The existing factorization with multiplier `I(s)=(2^(1-s)-1)/(1-s)` is one possible template, not a required form of the answer.

Use PL-464's positive blockwise-constant density as a negative control at its stated `theta=1/2`: it has small dyadic empirical variance and a forbidden-looking Mellin pole, but its translated residues have nonreal ratios. Any argument that also excludes this control without using arithmetic residue information has lost a hypothesis. An adaptation to `theta>2/3` must recompute its variance at that exponent. Failure of a particular smoothing construction is only a method obstruction; a counterexample to a stronger analytic implication must preserve the residue assumptions it purports to test. No fabricated prime or Dirichlet-zero counterexample is admissible.

**Bounded source reading for the Prime Lattice watch:** read only `research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md`, especially equations (4)–(9), to reconstruct the finite box correction, its support bound and its fixed-depth quantifiers; include its current adjacent `.review.md` sidecar if present. The inspected source revision is `1653e7dd22661fe26c3fedb07518817c097ab692`. Recheck the current source and review state before use. This read-only grant permits no traversal of other Möbius findings or its Mind/clues. PL-464 and PL-465 are destination-local evidence. The prior-art node in `based_on` records the classical inversion mechanism, not an extra cross-line reading grant.

## Evidence boundary

No improved dyadic half-plane, seam estimate, new variance bound, or GRH implication beyond the stated conditional proposal is established here. MC-521 uses complete uncentered moments at all sufficiently large real scales; PL-464 uses empirical centering and only dyadic scales. Their norms and quantifiers are not interchangeable. PL-465 already resolves smooth recovery under its all-real-scale assumption, and neither its frame theorem nor a frame at one exponent supplies this clue's hypothesis. The finite deconvolution polynomial and Mellin method are classical; the unresolved object is their compatibility with the dyadic seam and unknown-mean structure. Research Watch must perform the mathematical and prior-art audit before accepting the proposed transfer.

## Research disposition

Outcome: supported

Resolved by:
- [[research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss]]

PL-466 proves the proposed half-plane under exactly the stated dyadic variance hypothesis. It uses a weight `(1-cos(2 pi log(u)/log(2)))^m` whose finite-order zeros remove the seam error while preserving a finite Fourier representation. The empirical means remain in a vertically periodic meromorphic factor. Classical sublinear off-critical zero density rules out poles of that factor, and a finite-difference recurrence then recovers the unweighted logarithmic derivative's pole information. Thus no adjacent-mean estimate or extra window length is needed. The positive dyadic density control remains admissible for the variance bound but fails the arithmetic sublinear-pole-density input. The result establishes the conditional implication, not the actual-prime variance bound or GRH.
