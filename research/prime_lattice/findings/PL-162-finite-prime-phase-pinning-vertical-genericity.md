# PL-162 — Finite prime-phase pinning is vertically generic for zeta zeros

## Claim

The phase condition left by `PL-161` is not, by itself, an arithmetic anti-aliasing obstruction. Fix any finite set of distinct rational primes

`P={p_1,...,p_r}`

and let `gamma` run over the positive imaginary parts of the nontrivial zeros of the Riemann zeta function, counted with multiplicity. Then the prime-phase vectors

`x_gamma=(gamma log p_1/(2 pi),...,gamma log p_r/(2 pi)) mod 1`

are uniformly distributed in the finite torus `T^r`. Consequently, for every neighborhood `U` of the identity in `T^r`, a positive asymptotic proportion of zeta zero ordinates have `x_gamma in U`; in particular there is a sequence of distinct ordinates `gamma_j -> infinity` such that

`p^(i gamma_j) -> 1`

simultaneously for every `p in P`.

This is an unconditional specialization of the simultaneous fractional-part theorem of Ford--Meng--Zaharescu. For prime-log coordinates one takes

`alpha_j=log p_j/(2 pi)`.

Their arithmetic relation matrix may be chosen `M=I_r`, with `a_j=q_j=1`; this is the full-rank `r=n` case, where their required Diophantine condition follows from Baker's theorem. Their asymptotic for sufficiently smooth torus test functions has the form

`sum_(0<gamma<=T) h(x_gamma)`
` = N(T) integral_(T^r) h(x) dx`
`   + T integral_(T^r) h(x) g_P(x) dx + o(T)`,

where

`g_P(x)`
` = -(1/pi) sum_(p in P) (log p)`
`     Re sum_(k>=1) p^(-k/2) exp(-2 pi i k x_p)`.

Since `N(T)~(T/(2 pi)) log T`, division by `N(T)` gives Haar equidistribution. At the identity,

`g_P(0)=-(1/pi) sum_(p in P) log p/(sqrt(p)-1) < 0`.

Thus rational-prime phases do leave a genuine first-order arithmetic fingerprint: a sufficiently localized smooth bump around the identity has a negative `T`-scale correction. But this correction is smaller by a factor of order `1/log T` than the Haar-leading `N(T)` population. It depletes the identity phase statistically; it does not forbid it, and it cannot prevent sparse sequences approaching the identity.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE/STRUCTURAL-BOUNDARY`. The simultaneous phase theorem and its explicit secondary density are peer-reviewed prior art. The specialization to distinct prime logarithms and the diagonal extraction of a sequence converging to the torus identity are direct consequences. No novelty claim is made. The decisive-negative scope is limited to attempts to kill the surviving `PL-161` loophole using only unconditioned vertical prime-phase distribution for one or finitely many primes.

## Prime-log coordinates fall exactly inside the known simultaneous-distribution theorem

Ford--Meng--Zaharescu study

`({alpha_1 gamma},...,{alpha_n gamma})`

for fixed distinct positive `alpha_j`. Their arithmetic case is described by an integer matrix `M` satisfying

`M alpha^T`
` = (a_1 log p_1/(2 pi q_1),...,a_r log p_r/(2 pi q_r))^T`

for distinct primes `p_j`. When the chosen frequencies themselves are the prime logarithms,

`alpha_j=log p_j/(2 pi)`,

we may take `M=I_r` and `a_j=q_j=1`. Hence the rank is maximal, `r=n`, and their Corollary 1.1 applies. The Baker-theorem input in their proof supplies the quantitative lower bound for nonzero integer linear forms in the `alpha_j` needed to control Fourier modes.

The resulting secondary density is especially transparent because the rows of `M` are the coordinate vectors. Substituting the prime-log data into their general formula yields

`g_P(x)`
` = -(1/pi) sum_(j=1)^r (log p_j)`
`     Re sum_(k>=1) p_j^(-k/2) exp(-2 pi i k x_j)`.

The secondary term is therefore additive across the finite prime coordinates. This is not the independent-Haar model exactly: the actual zeta zero ordinates remember prime powers through a deterministic `T`-scale discrepancy. Nevertheless the leading term is still Haar measure because the zero count is of order `T log T`.

For a continuity set `U subset T^r`, smooth approximation of its indicator gives

`#{0<gamma<=T : x_gamma in U}/N(T) -> Haar(U)`.

Every fixed open neighborhood of `0 in T^r` has positive Haar measure and therefore contains infinitely many such phase vectors. Taking a nested sequence of identity neighborhoods with radii tending to zero and choosing one new zero ordinate from each sufficiently high range gives distinct `gamma_j -> infinity` with

`max_(p in P) |p^(i gamma_j)-1| -> 0`.

No Riemann-hypothesis assumption enters this argument.

## The identity phase is arithmetically depleted, not excluded

The one-dimensional predecessor of Ford--Meng--Zaharescu is Ford--Zaharescu's refinement of the classical Hlawka equidistribution theorem. For special frequencies

`alpha=a log p/(2 pi q)`,

the discrepancy has an explicit prime-power density. In the basic prime-axis case `a=q=1`, the limiting correction is most negative at the identity phase. The simultaneous theorem retains exactly this phenomenon coordinatewise.

At `x=0`, summing the geometric series gives

`sum_(k>=1) p^(-k/2)=1/(sqrt(p)-1)`,

hence

`g_P(0)=-(1/pi) sum_(p in P) log p/(sqrt(p)-1)`.

Because `g_P` is continuous, a sufficiently small nonnegative smooth bump concentrated at the identity has a negative first-order correction. This is a genuine arithmetic feature generated by the prime-power terms in the Landau explicit formula. It is also the strongest immediately relevant control found in the literature audit against the identity-pinning condition of `PL-161`.

But its scale is decisive. For a fixed test function,

`N(T) integral h ~ (T log T/(2 pi)) integral h`,

whereas the arithmetic correction is only of order `T`. Thus the correction changes the local count by a relative amount of order `1/log T`; it cannot make the leading positive mass of a fixed identity neighborhood disappear. In particular it gives no positive lower bound on

`dist(gamma log p_j/(2 pi), Z)`

for all large zero ordinates, separately or simultaneously across finitely many primes.

## Consequence for the PL-161 phase-pinned frontier

`PL-161` shows that if a fixed-step Suzuki sample is bounded on one side under failure of RH, then near-rightmost zeros must satisfy a coupled condition

`beta_j -> Theta`,
`exp(i T_j h) -> 1`.

For the prime ray `h=log p`, the angular condition is `p^(i T_j)->1`. A natural next attack was therefore to ask whether rational-prime arithmetic makes such phase recurrence impossible. The present prior-art audit shows that this cannot work at the level of the ordinates alone: among the complete zeta zero sequence, recurrence to the identity occurs not merely for one prime but simultaneously for **every prescribed finite family of primes**.

Accordingly, the surviving information in `PL-161` is the coupling between the horizontal and vertical coordinates of the zeros. Any useful theorem must discriminate zeros with real part approaching the extremal abscissa from the overwhelming bulk used in the unconditional equidistribution theorem. A statement about all ordinates, or about a finite prime-torus projection without conditioning on `beta`, cannot contradict the phase-pinned frontier.

This also shows why simply adding more fixed prime axes does not repair the issue. If `P` is any fixed finite set, actual zeta ordinates already approach the common identity in the corresponding finite prime torus. The obstruction is not finite-dimensional simultaneous Diophantine approximation of the ordinates; it is whether an **off-critical near-frontier subsequence** can do so.

## Relation to the two-prime positivity reduction

This finding does not conflict with `PL-155`. There the joint two-prime exponent face is RH-equivalent because positivity of Suzuki's translation-invariant screw kernel on the positive semigroup extends to the dense signed group

`Z log p + Z log q`.

That argument uses all pairwise kernel differences and continuity; it is not an assertion that zeta zero phases avoid simultaneous recurrence. The present result concerns only the distribution of the scalar ordinate phases

`(p^(i gamma),q^(i gamma))`.

Thus two-prime **kernel positivity** can be complete even though two-prime **vertical phase anti-aliasing** is impossible. These are different information channels.

## Prior art and novelty audit

The primary sources are:

- **Kevin Ford, Alexandru Zaharescu**, “On the distribution of imaginary parts of zeros of the Riemann zeta function,” *Journal für die reine und angewandte Mathematik* **579** (2005), 145--158. DOI `10.1515/crll.2005.2005.579.145`; arXiv `math/0405459`. This paper refines Hlawka's unconditional uniform distribution of `{alpha gamma}` and gives the explicit prime-log discrepancy density, including the shortage near the identity phase.
- **Kevin Ford, Xianchang Meng, Alexandru Zaharescu**, “Simultaneous distribution of the fractional parts of Riemann zeta zeros,” *Bulletin of the London Mathematical Society* **49**(1) (2017), 1--9. DOI `10.1112/blms.12001`; arXiv `1511.06814`. Theorem 1 and Corollary 1.1 give the simultaneous asymptotic and its explicit density; the full-rank prime-log specialization used here satisfies their Diophantine hypothesis by Baker's theorem.

A current targeted audit also checked later work on fractional parts of zeta-zero ordinates and zero-density based extensions. Those sources refine vertical distribution or treat special subsequences under additional hypotheses, but the bounded search did not locate a theorem controlling the prime phases **conditioned on hypothetical zeros whose real parts approach an off-critical extremal abscissa**. That absence is not evidence of novelty and is not used as a claim. The durable content here is the opposite: existing prior art already kills the unconditioned finite-prime anti-aliasing route.

## Adversarial boundaries

1. **This does not construct the `PL-161` near-frontier sequence.** Uniform distribution is over all nontrivial zeros and discards the real parts `beta`. It gives no reason that zeros with `beta` close to a hypothetical `Theta>1/2` inherit the same phase law.

2. **This does not weaken the necessary condition in `PL-161`.** `PL-161` couples radial approach `beta_j->Theta` with angular pinning. The present result says only that the angular half, even simultaneously in finitely many prime coordinates, is common among the full vertical zero population.

3. **The first-order negative identity bias is not a zero-free phase gap.** It is an `O(T)` correction against a main count of order `T log T`. It can reduce counts in fixed identity neighborhoods but cannot force them to vanish asymptotically.

4. **Only fixed finite prime sets are covered.** No claim is made about approaching the identity simultaneously in infinitely many prime coordinates, about a topology on the full infinite torus, or about allowing the number of observed primes to grow with `T`.

5. **No shrinking-target rate is claimed.** Equidistribution for every fixed neighborhood permits a diagonal sequence with neighborhoods shrinking after the height threshold is chosen. It does not give an effective relation between the phase error and the height of the selected zero.

6. **The theorem concerns ordinates counted with multiplicity.** Multiple zeros do not affect the conclusion; the diagonal sequence can be chosen with distinct ordinates because every fixed positive-measure neighborhood contains an asymptotically growing number of zeros.

7. **No Euler product is continued into the critical strip.** The underlying proofs use Landau-type explicit formulas, zero-density estimates, Fourier analysis, and Diophantine bounds. The prime-log phase statement is a theorem about the actual completed zeta zero set, not a formal continuation of the Euler product.

A falsification of the derived part would require that the prime-log vector fail the full-rank hypotheses of Ford--Meng--Zaharescu, that their normalized simultaneous distribution not imply positive asymptotic mass in every fixed identity neighborhood, or that the standard diagonal extraction from nested neighborhoods fail.

## Consequence for the research line

Do not pursue a theorem of the form “zeta zero ordinates cannot approach `2 pi Z/log p`” as the missing arithmetic anti-aliasing input for `PL-161`, nor its analogue for any fixed finite family of rational primes. Those statements are false for the full zero sequence.

The live fixed-ray question must instead retain horizontal information. A meaningful next target is a **conditioned or weighted prime-phase theorem for near-frontier zeros**: for example, control of the phase distribution among zeros with `beta>Theta-epsilon`, or an explicit-formula weight that magnifies large `beta` while resolving `exp(i gamma log p)`. Such a theorem would address the actual coupled loophole left by `PL-161`; ordinary vertical equidistribution, discrepancy, or finite-prime Kronecker geometry cannot.