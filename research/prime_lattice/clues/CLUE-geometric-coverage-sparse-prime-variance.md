---
id: CLUE-prime-lattice-geometric-coverage-sparse-prime-variance
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md
  - research/prime_lattice/findings/PL-476-trimmed-paired-prime-variance-retains-the-grh-obstruction.md
  - research/prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity.md
  - research/prior_art/incremental/PA-lipschitz-integration-recovery.md
---

# Can geometric coverage retain the prime-variance criterion on a vanishing fraction of starts?

## Observation

MC-533 replaces a count-only deletion bill by the geometry of retained starts. For any complex sequence indexed by `X` consecutive starts with jump bound `J`, any nonempty retained set `R`, nearest-sample assignment `pi`, cell sizes `w_r=|pi^(-1)(r)|`, and `D=sum_j |j-pi(j)|`, its elementary recovery argument gives

`sum_j |u_j| <= sqrt(X sum_(r in R) w_r |u_r|^2) + J D`.

It applies this to complete smooth mean-zero Möbius pairings without masking the analytic tests. On the fixed grid of spacing `floor(sqrt X)`, only order `sqrt X` starts remain, yet the paired sample-energy ceiling is RH-equivalent. The ceiling is not proved independently. This is classical Lipschitz recovery plus the separate reciprocal-pole theorem, not a new sampling principle.

PL-476 already supplies the destination's complete paired tests, noncancelling mod-5 pole formula, logarithmic jump bound and independent GRH converse, but assumes fewer than half the starts are deleted. PL-477 shows why a common mask and signed target alone do not remove the quadratic cost on clustered gaps. Its two positive control sources have identical retained vectors under a common mask of size `B` and target separation of order `B^2/X`; the controls lack prime-power support and an arithmetic pole formula. Sparse well-spaced samples have a different distance budget from those clustered gaps.

## Research question

For integer `X`, set `I_X={X,...,2X-1}`, `a_n=Lambda(n) 1_(n=1 mod 5)` and `S_L(j)=sum_(j<n<=j+L) a_n`. For integer `1<=H<=X/20`, let `L_1=H`, `L_2=floor(sqrt(2)H)`. For each channel choose any nonempty `R_i` in `I_X`, its nearest assignment (ties to the smaller sample), weights `w_(i,r)`, distance sum `D_i`, and one constant `c_i`. Put

`W_i(c_i)=sum_(r in R_i) w_(i,r) |S_(L_i)(r)-c_i|^2`.

Does a nontrivial zero of zeta or one of the three primitive nonprincipal Dirichlet functions modulo 5 with real part `beta>1/2` force

`sum_(i=1,2) [sqrt(X W_i(c_i)) + log(3X) D_i]/L_i >= C X^beta`

uniformly over these choices on every sufficiently large integer block, with no majority-retention requirement?

At `H=floor(X/20)`, fix the source-independent grid

`g_X=floor(sqrt X)`, `R_X={X+k g_X:0<=k<=floor((X-1)/g_X)}`, `q_X=|R_X|`.

For `Q_i(X)=min_c sum_(r in R_X)|S_(L_i)(r)-c|^2`, determine whether existence of one unbounded integer scale set, fixed before epsilon, satisfying **both** `Q_i(X)/q_X <<_epsilon X^(1+epsilon)` for every `epsilon>0` is equivalent to joint mod-5 GRH. This is a candidate destination criterion, not an arithmetic upper bound.

## Why it may matter

This would replace the requirement of a small exceptional-start count by adequate coverage and correctly weighted energy, exposing a distinct deterministic sampling target for the actual prime source. It would also prevent PL-477's clustered-mask obstruction from being misread as a universal lower bound on retained fraction. Success changes the observation interface, not the need for an independent arithmetic estimate or the meaning of GRH.

## Decisive test

1. Reconstruct MC-533's finite weighted recovery lemma with `u_j=S_L(j)-c`. Use PL-476's exact endpoint difference and `0<=a_n<=log(3X)` to retain the prime jump price. Keep its complete mean-zero pairings and `O(log X)` rounding bill. Do not insert a retained-set indicator into the Mellin test or import the reciprocal-pole multiplicity factor.
2. Check the fixed grid's endpoint cells, `D<=X g_X`, `max_r w_r<=2g_X`, and conversion from the ordinary sample-centered energy to the weighted energy using the same constant. Keep both channels on the same unbounded scale set, with separate empirical means and every-epsilon quantification after the grid and scale family are fixed. A small complete mean square does not by itself bound a deterministic sparse sample.
3. Establish any converse directly from the fixed-modulus prime-counting estimate already used in PL-476, with center `L_i/4`; do not import MC-520 or the Möbius pointwise bound. Distinguish the implication from an equivalence if that converse is not supplied.
4. Test irregular and clustered samples against their actual weights and distance sums. Reconstruct PL-477's common-mask example to check consistency, not to claim that its coefficients are primes or Möbius values. MC-533's lower bound `D>=(X^2/q-q)/4` and distance-envelope example constrain generic absolute-mass recovery, not the arithmetic information limit or signed-test optimality. Compare the elementary step with the registered Lipschitz recovery prior art before any novelty claim.

**Bounded source reading for Prime Lattice:** read exactly `research/mobius_cancellation/findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md`, Sections 1, 3 and 4, for the finite recovery proof, grid bookkeeping and its generic lower-bound boundary. Include its current adjacent `research/mobius_cancellation/findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.review.md` if present. Inspected revision: `61e8a8549dd55ae36cf20680d9bd7041db11806e`. Recheck current claim/review state and reconstruct the argument independently. This read-only grant permits no other Möbius files, recursive dependencies, Mind, graph or clue browsing. MC-533 contains the entire finite lemma; PL-476 supplies the destination's analytic pair and converse. The reciprocal-zeta argument in MC-533 is not a destination input.

## Evidence boundary

MC-533 proves the source-side sparse Möbius criterion; PL-476 proves the prime criterion with a small deletion count; PL-477 proves a generic clustered-mask obstruction. The displayed weighted prime floor and sparse-grid joint-GRH equivalence remain unvalidated destination transfers. No arithmetic sample-energy ceiling, improved prime-counting estimate, optimal sample exponent, effective zero-uniform test, covariance positivity, formal verification, independent adversarial approval or external novelty is asserted. The construction does not recover Farey's complete uncentered moment, identify prime and reciprocal zero sets, or prove RH/GRH.
