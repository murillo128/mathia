# VIS-071 — finite prime vertical flow has the shared-phase Haar law

## Claim

Fix finitely many primes `P`, finitely many harmonics at each prime, and finitely many predeclared coordinates `alpha=1,...,d`. Let

`A_alpha(t) = Re sum_(p in P) sum_k c_(alpha,p,k) exp(-i k t log p)`,

with fixed complex coefficients `c_(alpha,p,k)`. Let `Theta_p` be independent uniform phases on `[0,2 pi)` and define

`A_alpha^null(Theta) = Re sum_(p in P) sum_k c_(alpha,p,k) exp(i k Theta_p)`.

Then for every bounded continuous `F : R^d -> C`,

`lim_(T->infinity) (1/T) integral_0^T F(A_1(t),...,A_d(t)) dt`
` = E F(A_1^null(Theta),...,A_d^null(Theta))`.

Thus the complete fixed-finite-coordinate shared-prime-phase law from `VIS-070` is not merely a convenient randomized comparator. It is exactly the vertical Cesaro limiting law of the deterministic finite prime-phase field itself.

The same statement covers any fixed collection of height offsets or scale coordinates: factors such as `exp(-i k h_alpha log p)` are absorbed into the coefficients `c_(alpha,p,k)`. In particular, every fixed finite prime-factor increment field built from finitely many prime powers has the same long-height finite-dimensional law as its shared-phase Haar control.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL KRONECKER/BOHR SPECIALIZATION + DECISIVE-NEGATIVE + NO-NOVELTY-CLAIM`.

No quantitative finite-window equidistribution rate, growing-cutoff theorem, infinite random Euler-product limit, hybrid prime/zero independence statement, or RH consequence is claimed.

## 1. Prime logarithms have no nontrivial integer resonance

Let `m=(m_p)_(p in P)` be an integer vector and suppose

`sum_(p in P) m_p log p = 0`.

Exponentiating gives

`prod_(p in P) p^(m_p) = 1`.

Move the negative exponents to the other side. Unique factorization then forces every `m_p=0`. Therefore the finite frequency vector `(log p)_(p in P)` has no nonzero integer relation.

This is the exact arithmetic input. Prime powers do not add independent frequencies: the `k`th harmonic at prime `p` is an integer multiple of the same prime frequency, exactly matching the shared-phase convention of `VIS-067`--`VIS-070`.

## 2. The continuous prime-phase orbit equidistributes on the torus

Consider the torus orbit

`theta(t) = (-t log p mod 2 pi)_(p in P)`.

For any nonzero integer character `m`, put

`lambda_m = sum_p m_p log p`.

The previous section gives `lambda_m != 0`, and hence

`(1/T) integral_0^T exp(i m dot theta(t)) dt`
` = (1/T) integral_0^T exp(-i t lambda_m) dt`
` -> 0`.

The zero character averages to `1`. By the continuous Weyl criterion, `theta(t)` is therefore uniformly distributed with respect to Haar measure on the finite torus.

Equivalently, the vertical prime phases form a uniquely ergodic Kronecker flow at this finite level. The argument is elementary because the only possible character obstruction would be an integer relation among the prime logarithms, and unique factorization removes it.

## 3. Pushforward gives exactly the `VIS-070` law

Define the continuous map `G : T^|P| -> R^d` by

`G_alpha(theta) = Re sum_(p in P) sum_k c_(alpha,p,k) exp(i k theta_p)`.

Then `A(t)=G(theta(t))`, while `A^null(Theta)=G(Theta)` with `Theta` Haar-distributed. For bounded continuous `F`, the composite `F o G` is continuous on the compact torus, so equidistribution gives

`lim_(T->infinity) (1/T) integral_0^T F(G(theta(t))) dt`
` = integral_(T^|P|) F(G(theta)) dtheta`
` = E F(A^null(Theta))`.

The right-hand side is precisely the pushforward law whose characteristic function was factorized prime by prime in `VIS-070`. Thus `VIS-070` and the deterministic vertical prime field describe the same fixed-finite limiting probability law from two directions: one by independent Haar phases, the other by long vertical translation.

For a lagged field `A(t+h_alpha)` or several fixed scale increments, absorb the deterministic factors `exp(-i k h_alpha log p)` and the scale weights into `c_(alpha,p,k)`. The same one-parameter torus orbit then controls the whole finite coordinate vector, so the conclusion is unchanged.

## 4. Consequence for arithmetic-versus-null visual tests

At fixed finite prime/harmonic support, a long-height population test cannot separate the deterministic prime-factor field from the shared-phase Haar null by any bounded continuous statistic of a fixed finite coordinate vector. Covariance, cumulants, nonlinear norms, finite-grid geometric summaries, and other continuous finite-dimensional witnesses all converge to their null expectations because the underlying empirical measure converges to the same torus pushforward.

This sharpens the interpretation of the accepted prime-phase recursive-geometry clue. A persistent asymptotic population discrepancy at fixed finite support is not an admissible target: under the stated hypotheses it is exactly zero in the limit.

Finite-height differences are a different question. They measure discrepancy of a particular finite segment of the Kronecker orbit from Haar measure, not a different limiting law. A matched finite-window control should therefore preserve the deterministic frequency vector and phase sharing — for example by randomizing the initial torus phase and evolving it with the same `log p` frequencies — rather than independently resampling a new phase field at every sampled height and then attributing the resulting serial mismatch to arithmetic structure.

Likewise, a regime in which the prime cutoff, harmonic support, coordinate dimension, or window geometry grows with `T` is outside this theorem. Such a route needs quantitative equidistribution uniform in the growing family before a residual can be interpreted.

## 5. Prior art and novelty boundary

The mathematics is classical. Kronecker--Weyl theory identifies rationally independent torus flows with dense/equidistributed phase motion, and the direct character average above is the standard Weyl-criterion proof in this finite setting.

The Dirichlet-series interpretation is also classical Bohr theory. Håkan Hedenmalm, Peter Lindqvist, and Kristian Seip, **A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)**, *Duke Mathematical Journal* 86:1 (1997), 1--37, DOI `10.1215/S0012-7094-97-08601-4`, identify vertical limit functions with multiplicative-character twists and explicitly invoke Kronecker's theorem for the converse direction. The present finding only specializes that character/vertical-limit viewpoint to the finite shared-prime-phase control already defined by Mathia.

For the torus theorem itself, the **Encyclopedia of Mathematics**, *Kronecker theorem*, records the classical density/uniform-distribution consequence for rationally independent torus rotations. No novelty is claimed for the equidistribution theorem or for Bohr vertical limits.

The Mathia contribution here is only the control diagnosis: once `VIS-070` has made the finite shared-phase null explicit, classical vertical equidistribution shows that this null is already the asymptotic law of the deterministic finite prime field being compared against it.

## 6. Boundary and falsification

The theorem is fixed-finite in every structural direction: finitely many primes, finitely many harmonics, finitely many coordinates, and a fixed coefficient array. It gives weak convergence tested by bounded continuous functions through long continuous vertical averaging.

It does not give a useful convergence rate. Near-resonances among linear combinations of `log p` can make finite windows converge slowly, and controlling that discrepancy uniformly as the support grows is a separate Diophantine problem.

It does not apply to the zero factor or hybrid residual, whose dependence on zeta zeros and approximation error is not a deterministic function of the fixed prime torus alone. It also does not equate a null that independently resamples phases at each height with the shared-phase process; those are different stochastic objects.

Falsify the claim by producing a finite prime set, finite coefficient field, and bounded continuous `F` for which the displayed vertical average exists but differs from the Haar expectation. Such an example would contradict the character calculation above and therefore would require a nontrivial integer relation among distinct prime logarithms.

## Research consequence

The simplest proposed within-prime population experiment is closed at fixed finite cutoff. The deterministic vertical prime-factor field and the exact shared-phase null have the same long-height finite-dimensional law.

Any remaining within-prime visual route must therefore live in a boundary excluded here: quantitatively controlled finite-window discrepancy with a frequency-preserving null, a cutoff/support growing with height together with uniform equidistribution control, or an independently defined variable not reducible to the fixed prime torus. The factor/residual joint route remains open because the hybrid residual is not determined by this prime-phase equidistribution argument.