# VIS-408 — Wang's final test-packet admissibility does not supply a qutrit decoder budget

## Claim

In Biao Wang's short-interval pair-correlation argument, the final weight-removal/test-packet layer does impose a genuine target-independent structure, but it is **not** a finite-dimensional or uniformly regular source-to-response decoder of the kind required by `VIS-405`--`VIS-407`.

Fix `0<lambda<theta<1` and write

`J=(-lambda/2,lambda/2)`.

Wang chooses any fixed real even

`eta in C_c^infinity(J)`, `int_R eta(u)^2 du=1`,

and defines

`f=eta^2`, `K=hat(f)`, `Q=f*f`.

The pair statistic is then tested by the scalar kernel `K`, and for each fixed admissible `f` the asymptotic cost is the quadratic functional

`C(f)=int_R f(u)^2 du + int_R int_R |u-v| f(u)f(v) du dv`.

The admissible class before optimization is infinite-dimensional and carries **no packet-uniform derivative, Lipschitz, finite-basis, or polynomial-degree budget**. In particular, for any fixed even normalized bump `psi in C_c^infinity((-1,1))`, the family

`eta_b(u)=b^(-1/2) psi(u/b)`

is admissible whenever `0<b<lambda/2`, while its derivative norms diverge as `b->0`. Thus support and `L^2` normalization alone do not furnish the numerical decoder complexity needed by `VIS-405`--`VIS-406`.

Wang subsequently minimizes `C` in the larger class of real `L^2(J)` functions of integral one. The unique minimizer is

`f_lambda(u)=cos(sqrt(2)u)/(sqrt(2) sin(lambda/sqrt(2))) * 1_[-lambda/2,lambda/2](u)`.

The same infimum is approached in Wang's original smooth-square class by cutoff approximants `f_epsilon=eta_epsilon^2`; the optimizer itself is not promoted to a finite-dimensional source-response law. It is a **fixed scalar zero-pair test kernel selected by a variational problem**.

Therefore the actual Wang packet layer gives two distinct facts:

1. before optimization, the admissible smooth packet family is too flexible to imply a universal numerical decoder-capacity bound;
2. after optimization, one obtains an explicit target-independent scalar test profile, but Wang supplies no mathematical dictionary identifying that profile with a qutrit source tangent, a qutrit residual decoder, or the intrinsic source-to-response map sought in the current clue.

Consequently the missing qutrit decoder budget cannot be credited to Wang's final packet/test-function admissibility itself. Any such budget would require an additional theorem linking Wang's arithmetic source `A(x,t)` (or its reconstructed source component) to the qutrit tangent/response model in an intrinsic metric.

**Evidence/status:** `LITERATURE+DERIVED + EXACT-INTERFACE-AUDIT + NEGATIVE/BOUNDARY + NO-NOVELTY-CLAIM`.

No claim is made that Wang's packet optimization is defective, that the pair-correlation theorem permits moving tests outside its proved regime, or that no future source-to-qutrit construction can exist.

## 1. What Wang actually fixes

Wang's Theorem 2.2 first proves a short-interval pair-correlation asymptotic for every **fixed** real even smooth test `g` supported in `[-lambda,lambda]`. In Section 3, to remove the rational weight, Wang chooses a fixed real even `eta` supported strictly inside `J` with `int eta^2=1`, then sets `f=eta^2`, `K=hat(f)`, and `Q=f*f`.

The algebraic identity involving `Q`, `Q''`, and the rational weight allows the weighted pair-correlation theorem to control

`S_K(I)=sum_(gamma,gamma' in I) K(i(rho-rho')L/(2pi))^2`.

For fixed `f`, the leading coefficient is exactly `C(f)`. This is an honest target-independent packet interface: the test function is chosen before taking the zero statistic, not fitted to the observed zero sample.

But the interface is a scalar test kernel on zero differences. It does not define a finite-dimensional latent state, source-tangent law, or qutrit decoder.

## 2. The admissible smooth class has no uniform regularity budget

The conditions

`eta in C_c^infinity(J)`, `eta real/even`, `int eta^2=1`

fix support, parity, smoothness, and normalization, but not a numerical smoothness constant.

Choose any real even `psi in C_c^infinity((-1,1))` with `int psi^2=1`. For every `0<b<lambda/2`, set

`eta_b(u)=b^(-1/2) psi(u/b)`.

Then `eta_b` remains real, even, smooth, compactly supported in `J`, and normalized in `L^2`. However

`||eta_b'||_infinity = b^(-3/2) ||psi'||_infinity`,

and for `f_b=eta_b^2`,

`||f_b'||_infinity = b^(-2) ||(psi^2)'||_infinity`.

Higher derivative norms grow by still higher inverse powers of `b`. The class also contains infinitely many linearly independent packet shapes. Hence no constant `L(lambda)`, fixed polynomial degree, fixed basis dimension, or coefficient budget follows from Wang's admissibility conditions alone.

This is consistent with, but distinct from, `VIS-267`. That finding priced **moving signed probes** against the seminorms exposed by Wang's proof. The present statement concerns the final nonnegative `f=eta^2` weight-removal packet class itself: even when every packet is fixed with respect to `T`, the class as a whole has no universal numerical decoder regularity.

## 3. Optimization selects a scalar kernel, not a decoder family

Wang's Section 4 solves the variational problem for `C(f)` on the larger affine space of real `L^2(J)` functions with integral one. The unique minimizer is the explicit cosine profile `f_lambda` above, and the minimum is

`C_lambda = lambda/2 + (1/sqrt(2)) cot(lambda/sqrt(2))`.

Wang then proves that the same infimum is attained as a limit inside the original smooth-square class. He chooses smooth cutoffs `chi_epsilon` equal to one away from the endpoints and defines

`eta_epsilon(u)=chi_epsilon(u) sqrt(f_lambda(u))/sqrt(b_epsilon)`,

`f_epsilon=eta_epsilon^2`,

so that `f_epsilon -> f_lambda` in `L^1` and `L^2` and `C(f_epsilon)->C_lambda`.

This is a strong target-independent restriction **after the variational objective has been chosen**: asymptotically optimal packets converge to one explicit profile for each `lambda`. But the restriction lives at the zero-pair test-kernel level. The source does not identify `f_lambda`, `K_lambda=hat(f_lambda)`, or their cutoff approximants with the qutrit residual coordinate `u`, with the source-subspace commutator Laplacian `Delta_S`, or with a decoder from source conjugacy data to tangent spectral shape.

That missing dictionary matters. A fixed scalar test profile cannot be re-labelled as a fixed decoder-complexity budget without proving how the arithmetic source enters that decoder and which intrinsic metric controls the response.

## 4. Consequence for the qutrit decoder-capacity branch

`VIS-405` and `VIS-406` show that an independently frozen numerical decoder budget would have an exact observable consequence: for example a monotone Lipschitz budget forces a uniform mass floor in the target residual law. `VIS-407` then rules out obtaining that budget merely from the singular algebraic invariant chart of rank-one qutrit source conjugacy.

The Wang audit closes the next obvious escape. The paper's packet admissibility does not supply a uniform numerical smoothness/finite-complexity budget, while the optimized profile is a scalar kernel for a different mathematical interface. Thus neither the general admissible class nor the variational optimizer, by themselves, justify the qutrit decoder restriction.

A future source-response route would have to add real mathematics: an explicit map from the Wang source decomposition to the intrinsic qutrit tangent/response object, followed by a target-independent estimate on that map. Only then could `VIS-405`--`VIS-406` be invoked without circularly importing a representation budget.

## 5. Prior art and novelty boundary

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026). The load-bearing statements are Theorem 2.2, equations (3.1)--(3.5), and Proposition 4.1 with its approximation of the minimizing profile by `eta_epsilon^2` packets.

Wang explicitly supplies the fixed-test admissibility, the functional `C(f)`, the unique cosine minimizer in the larger `L^2` class, and the fact that the same infimum is approached inside the smooth-square class. The dilation family `eta_b` and the conclusion that these hypotheses impose no packet-uniform derivative bound are elementary consequences of those admissibility conditions.

No novelty is claimed for bump dilation, Fourier test kernels, variational minimization, or the cosine optimizer. The durable Mathia contribution is the interface audit: it prevents the current qutrit branch from treating Wang's packet language as evidence for a source-to-response capacity restriction that the source does not actually provide.

## Dependencies

- `VIS-267`: moving smooth test packets and Wang-seminorm bandwidth costs.
- `VIS-339`: Wang prime-source/Chebyshev-theta differential image.
- `VIS-384`--`VIS-390`: intrinsic qutrit source-subspace and residual reduction.
- `VIS-393`: source-stabilizer symmetry alone leaves the qutrit residual law free.
- `VIS-403`--`VIS-406`: decoder-capacity identification and exact observable consequences.
- `VIS-407`: the scalar qutrit invariant chart is boundary-singular and cannot supply an intrinsic regularity budget.

## Research consequence

The accepted Wang packet-localization clue has reached a clean boundary. The actual final Wang packet interface is either an infinite-dimensional fixed smooth class with no universal numerical decoder complexity, or—after variational optimization—an explicit scalar zero-pair kernel with no proved dictionary to the qutrit source-response model.

Accordingly the present **decoder-capacity route is closed as a consequence of Wang packet admissibility alone**. Reviving it requires a new, explicit source-to-qutrit response theorem in an intrinsic metric; choosing another latent, chart, basis, or regularity budget is not a continuation of the established Wang mechanism.