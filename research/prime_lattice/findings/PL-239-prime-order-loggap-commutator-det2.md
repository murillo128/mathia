# PL-239 — Prime-order log-gap commutator sits at the `S_{1+}` endpoint; its `det_2` real divisor is local-gap data

## Claim

The first canonical way to implement the post-`PL-237` requirement that **actual rational-prime order and labels enter before averaging** is to place the increasing primes

`p_1=2<p_2=3<p_3=5<...`

on `ell^2(N)`, use the logarithmic position operator

`Q e_n=(log p_n)e_n`,

and compare it with the source-order unilateral shift

`U e_n=e_(n+1)`.

On the finite-support core,

`C=[Q,U]`

extends to the weighted shift

`C e_n=delta_n e_(n+1)`,

where

`delta_n=log(p_(n+1)/p_n)>0`.

Thus the commutator records the **actual consecutive log-prime gaps**, not merely the abstract order type closed by `PL-237` and not a scalar projective cocycle factoring continuously through the completed log-energy line closed by `PL-238`.

This source-forced operator has an exact borderline trace-ideal structure:

`C in S_q  for every q>1`,

but

`C notin S_1`.

The non-trace-class statement is exact and telescopic,

`sum_(n<=N) delta_n=log p_(N+1)-log 2 -> infinity`,

while the `S_q`, `q>1`, side follows from any power-saving bound on relative consecutive-prime gaps, for example Baker--Harman--Pintz.

The canonical self-adjoint doubling

`D=[[0,C^*],[C,0]]`

therefore belongs to every `S_q`, `q>1`, but not `S_1`, and has nonzero eigenvalues

`{+delta_n,-delta_n : n>=1}`.

Its Hilbert--Schmidt regularized determinant is completely explicit:

`det_2(I-zD)=product_(n>=1) (1-z^2 delta_n^2)`.

Hence its nonzero determinant zeros are exactly

`z=+/- 1/delta_n`.

They are real **unconditionally**, and their exponent of convergence is exactly `1` because

`sum delta_n^q<infinity` for every `q>1`, while `sum delta_n=infinity`.

Using the Baker--Harman--Pintz exponent `0.525`, their counting function also satisfies the coarse bound

`N_D(R)=O(R log R)`.

This is superficially Hilbert--Polya-like — a self-adjoint, source-forced prime operator whose regularized determinant has a real order-one zero divisor at at most the same coarse `R log R` scale as the Riemann zero count — but the mechanism is **not** a localization theorem for zeta. The determinant divisor is tautologically the reciprocal local log-gap list. No functional equation, explicit-formula duality, analytic continuation, or Weil positivity has entered.

The result is therefore a precise negative boundary for the route

`actual prime order + actual log-prime labels + nearest-neighbor commutator + standard self-adjoint doubling/det_2`

as an RH mechanism. It does **not** say that prime-gap data are information-theoretically insufficient: the full ordered prime-gap sequence determines the primes. It says that the canonical local commutator and its standard regularized determinant do not themselves create the missing global relation that could identify their real divisor with the zeta-zero divisor.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`, decisive only for the bare nearest-neighbor log-prime commutator and its standard self-adjoint `det_2` spectralization.

## Exact source-order commutator

Let

`H=ell^2(N)`

with basis `{e_n}` indexed by primes in increasing order. Define the self-adjoint diagonal operator

`Q e_n=(log p_n)e_n`

on its maximal domain, and the bounded unilateral shift

`Ue_n=e_(n+1)`.

On finitely supported vectors,

`QUe_n=(log p_(n+1))e_(n+1)`,

`UQe_n=(log p_n)e_(n+1)`,

so

`[Q,U]e_n=delta_n e_(n+1)`,

`delta_n:=log(p_(n+1)/p_n)`.

Classical prime-gap estimates give `delta_n->0`; in particular Baker--Harman--Pintz prove

`p_(n+1)-p_n << p_n^0.525`,

so

`delta_n <= (p_(n+1)-p_n)/p_n << p_n^-0.475`.

Thus the core commutator extends uniquely to a compact weighted shift `C`.

Because

`C^* C e_n=delta_n^2 e_n`,

the singular-value multiset of `C` is exactly `{delta_n}`. No spectral approximation is involved: the trace-ideal problem is exactly the summability problem for consecutive logarithmic prime gaps.

## Exact failure of trace class

For every `N`, consecutive ratios telescope:

`sum_(n=1)^N delta_n`

` = sum_(n=1)^N log(p_(n+1)/p_n)`

` = log(p_(N+1)/2)`.

Since `p_N->infinity`,

`sum_n delta_n=infinity`.

Therefore

`||C||_1=sum_n delta_n=infinity`,

and

`C notin S_1`.

The prime number theorem sharpens only the source-order growth:

`log p_(N+1)=log N+log log N+o(1)`,

so

`(1/log N) sum_(n<=N) delta_n ->1`.

This last formula is **not** asserted to be a Dixmier trace. The trace ideals use decreasing singular-value rearrangement, whereas the displayed sum is in the canonical prime order. It is retained only to show that the endpoint divergence is already PNT-scale in the source ordering.

## Every higher Schatten power is summable

Put

`theta=0.525`, `a=1-theta=0.475`.

Group indices by dyadic prime scale

`B_k={n: 2^k <= p_n < 2^(k+1)}`.

For all sufficiently large `k`, Baker--Harman--Pintz gives

`max_(n in B_k) delta_n << 2^(-a k)`.

The total logarithmic increment across one such block is uniformly bounded. Indeed, if `n_0` and `n_1` are the first and last indices in `B_k`, then telescoping gives

`sum_(n in B_k) delta_n`

` <= log(p_(n_1+1)/p_(n_0))`.

The next prime after the block endpoint is

`p_(n_1+1) <= 2^(k+1)+O(2^(theta(k+1)))`,

so the displayed ratio is at most `2+o(1)` and the block sum is `O(1)`.

For any fixed `q>1`,

`sum_(n in B_k) delta_n^q`

` <= (max_(n in B_k) delta_n)^(q-1) sum_(n in B_k) delta_n`

` << 2^(-a(q-1)k)`.

The geometric series over `k` converges. Hence

`boxed: C in intersection_(q>1) S_q,  but C notin S_1.`

The exact value `0.525` is not structural. Any unconditional consecutive-gap theorem

`p_(n+1)-p_n << p_n^theta`

with some fixed `theta<1` gives the same conclusion. Thus the `S_{1+}` endpoint is not a delicate consequence of the best known prime-gap exponent.

## Canonical self-adjoint doubling and the regularized determinant

Set

`D = [[0,C^*],[C,0]]`

on `H direct_sum H`. This is compact and self-adjoint. Since `C^*C` has eigenvalues `delta_n^2`, the nonzero spectrum of `D` is

`spec(D)\{0}={+delta_n,-delta_n:n>=1}`,

with the usual multiplicities. There is also the harmless zero mode coming from the one-dimensional cokernel of the unilateral weighted shift.

Because `D in S_2`, the standard Hilbert--Schmidt determinant `det_2` is defined. Pairing the `+delta_n` and `-delta_n` eigenvalues in the canonical product gives

`det_2(I-zD)`

` = product_n [(1-z delta_n)e^(z delta_n)]`

`             [(1+z delta_n)e^(-z delta_n)]`

` = product_n (1-z^2 delta_n^2)`.

The product converges locally uniformly because

`sum_n delta_n^2<infinity`.

Therefore the entire determinant has the exact nonzero divisor

`Z_D={+/- delta_n^(-1):n>=1}`.

In particular, every determinant zero is real without any RH assumption. This reality comes from the self-adjoint doubling and contains no independent arithmetic localization statement.

The exponent of convergence of this divisor is exactly `1`:

`inf {q>0 : sum_(zeta in Z_D\{0}) |zeta|^-q < infinity}`

` = inf {q>0 : sum_n delta_n^q < infinity}`

` =1`.

Thus even the order-one nature of the divisor is automatic from the trace-ideal endpoint proved above; it is not evidence for the Riemann critical line.

## Coarse determinant-zero counting ceiling

Let

`A_R={n: delta_n>=1/R}`.

Up to the factor two from the symmetric signs,

`N_D(R)=# {z in Z_D: |z|<=R}=2 #A_R`.

Baker--Harman--Pintz gives

`delta_n << p_n^-a`, `a=0.475`.

Therefore `n in A_R` implies

`p_n << R^(1/a)`.

Put `X=C R^(1/a)` with a sufficiently large constant. Then

`#A_R / R <= sum_(n in A_R) delta_n`

`            <= sum_(p_n<=X) delta_n`.

The last sum telescopes to the logarithm of the prime immediately after `X`, divided by `2`. Bertrand's postulate already gives that this is `O(log X)=O(log R)`. Hence

`boxed: N_D(R)=O(R log R).`

The Riemann--von Mangoldt formula has the same **coarse growth class** `T log T` for the number of nontrivial zeta zeros up to height `T`. This observation is only an adversarial check: an `S_{1+}` source-order determinant is not immediately ruled out by a crude exponent/counting comparison. No asymptotic equality, scaling constant, or relation between the two divisors is established here.

## Relation to the prime-exponent lattice

The construction lives on the set of prime coordinate directions themselves. In exponent coordinates the prime `p_n` is the basis ray `e_(p_n)`, and

`Q e_(p_n)=(log p_n)e_(p_n)`.

The new ingredient is the **rational-prime successor relation**

`p_n -> p_(n+1)`.

That relation is not present in the abstract free commutative monoid `N_0^(P)` if the coordinates are treated as anonymous. This is precisely why it survives the exchangeability/spreadability collapses of `PL-232`--`PL-237`. It also does not factor merely through a jointly continuous scalar projective cocycle on the dense group `log Q_(>0)` studied in `PL-238`: it takes a discrete derivative after imposing the actual rational-prime ordering.

The price is equally precise. The nearest-neighbor commutator sees only

`delta_n=log p_(n+1)-log p_n`.

Its self-adjoint determinant therefore spectralizes **local source increments**, not the multiplicative Euler product, the prime-power von-Mangoldt measure, or the completed explicit formula. Mixed-support exponent vectors do not appear.

The full ordered gap sequence still determines the primes recursively from `p_1=2`, so this is not an information-loss theorem. Rather, it identifies the missing step: any RH use of this source-order geometry would need a mathematically forced transform that turns the local gap spectrum into the global completed zeta divisor. The standard commutator and `det_2` do not supply that transform.

## Prior-art and novelty audit

The ingredients are classical and the claim is intentionally not presented as new operator theory.

- **R. C. Baker, G. Harman, J. Pintz**, “The Difference Between Consecutive Primes, II,” *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`. Their theorem that `[x,x+x^0.525]` contains a prime for large `x` supplies the convenient power-saving mesh bound. The same source is already used in `PL-150`.
- **Thomas Britz, Alan Carey, Fritz Gesztesy, Roger Nichols, Fedor Sukochev, Dmitriy Zanin**, “The product formula for regularized Fredholm determinants,” *Proceedings of the American Mathematical Society, Series B* **8** (2021), 42--51, DOI `10.1090/bproc/70`, arXiv:`2007.12834`. This is the standard `det_2` framework already anchored in `SOURCES.md` and `PL-009`.
- **Rowan Killip, Barry Simon**, “Sum rules for Jacobi matrices and their applications to spectral theory,” *Annals of Mathematics* **158**(1) (2003), 253--321, DOI `10.4007/annals.2003.158.253`. This is broad classical prior art for Hilbert--Schmidt versus trace-class Jacobi perturbations and is already used as a spectral-theory control in `PL-037`.
- **Douglas F. Watson**, “Spectral Geometry of the Primes,” *Mathematics* **13**(21) (2025), 3554, DOI `10.3390/math13213554`. This recent work constructs other self-adjoint prime-indexed kernel/Laplacian geometries and derives a `1/2` spectral-dimension effect independently of RH. It is close thematic prior art and an important warning that a prime-built self-adjoint spectrum or a numerical `1/2` by itself is not an RH mechanism. Its operators are not the consecutive-log-gap commutator analyzed here.

Targeted searches for combinations of `log(p_(n+1)/p_n)`, weighted shifts, Schatten classes, Jacobi matrices, canonical products, and Fredholm determinants did not locate this exact commutator/doubling calculation. That absence is not used to claim novelty. The stored value is the exact line-specific reduction against the current `prime_lattice` frontier.

## Generic matched control

The trace-ideal phenomenon is not specific to rational primes. Let

`0<x_1<x_2<... -> infinity`

be any increasing event sequence with a power-saving relative mesh

`x_(n+1)-x_n << x_n^theta`

for some fixed `theta<1`, and define

`eta_n=log(x_(n+1)/x_n)`.

Exactly the same dyadic argument gives

`{eta_n} in ell^q  for every q>1`,

while telescoping gives

`sum_n eta_n=log(x_N/x_1)->infinity`.

Therefore the associated source-order commutator has the same

`intersection_(q>1) S_q \ S_1`

endpoint, and its self-adjoint doubling has an unconditional real determinant divisor `+/-1/eta_n` of exponent of convergence `1`.

So the coarse package

`source order + shrinking relative mesh + log position`

already produces the main spectral features above in matched non-prime systems. Rational-prime specificity can survive only in finer relations among the exact `{delta_n}` and in a global arithmetic transform coupling them to multiplication/prime powers/completion.

## Adversarial boundaries

1. **No RH criterion is claimed.** There is no theorem relating `det_2(I-zD)` to `xi(1/2+iz)` or to any completed zeta determinant.

2. **Reality is tautological here.** The determinant zeros are real because `D` is self-adjoint. This is exactly the kind of construction in which “all spectral zeros are real” is built in and therefore cannot by itself prove that a separately defined zeta divisor is real.

3. **The gap sequence contains the primes.** It would be wrong to call the operator information-free or zero-blind in an absolute sense. Starting with `p_1=2`, the exact ratios recover every `p_n`. The negative result concerns the absence of a forced **global zeta bridge** in the standard commutator/determinant machinery.

4. **`S_{1+}` is not a critical-line `1/2` law.** The endpoint `q=1` is a trace-ideal threshold caused by telescoping logarithmic length. It should not be rebranded as the RH half-axis.

5. **The `O(R log R)` count is only an upper bound.** Its resemblance to Riemann--von Mangoldt counting is too coarse to identify spectra. No matching main term is proved.

6. **No illicit continuation occurs.** Every calculation is on the real prime sequence plus standard compact-operator theory. The construction does not cross `Re(s)=1`; consequently it cannot claim to have solved the continuation barrier emphasized by the line mandate.

7. **Nearest-neighbor locality is the tested hypothesis.** Longer-range kernels, multiplicatively defined relations among several prime coordinates, prime-power coupling, or a target-relative transform could contain additional information. They are not ruled out by this finding.

## Consequence for the research line

`PL-237` showed that abstract prime order plus spreadability collapses back to exchangeability; `PL-238` showed that continuous scalar projective curvature through the one-dimensional log-energy completion collapses to a coboundary. The present calculation tests the most immediate remaining repair: keep the **actual numerical log-prime spacings** and differentiate them along the actual prime successor relation.

That repair is mathematically nontrivial — it yields a canonical compact `S_{1+}` commutator and a self-adjoint regularized determinant with a real order-one divisor — but its first spectralization remains local-gap geometry. The generic matched control shows that these coarse signatures arise for any power-saving ordered mesh.

Do not spend further passes treating self-adjointness, real determinant zeros, the `S_{1+}` endpoint, or an `O(R log R)` counting ceiling of this nearest-neighbor operator as evidence for RH. A surviving order-sensitive mechanism must add a **source-forced global relation** among several prime coordinates or prime powers that is not reducible to local successor increments, and then derive a bridge to analytic continuation/completion or Weil-type positivity rather than assuming that bridge from the spectral packaging.