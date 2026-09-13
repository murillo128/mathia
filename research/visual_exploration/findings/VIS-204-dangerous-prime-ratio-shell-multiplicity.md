# VIS-204 — fixed-scale dangerous prime-ratio shells have multiplicity at most four

## Claim

Keep the exact-difference-shell setting of `VIS-203`. Write the full signed prime-ratio frequency set as

`Lambda_y={log(a/b): a,b<=y prime, a!=b}`.

For an ordered pair

`lambda=log(a/b)`, `mu=log(c/d)`,

the exact difference shell is determined by

`exp(lambda-mu)=ad/(bc)`.

Reduce this positive rational to lowest terms. Unique factorization gives an exact trichotomy.

1. If there is no prime cancellation between the numerator multiset `{a,d}` and denominator multiset `{b,c}`, the reduced numerator and denominator each contain two prime factors counted with multiplicity. For a fixed shell there are at most two assignments of its numerator factors to `(a,d)` and at most two assignments of its denominator factors to `(b,c)`. Hence the shell multiplicity is at most `4`.

2. If exactly one prime cancels, the reduced shell is a ratio `u/v` of two distinct primes. Conversely, every representation of such a shell is obtained by choosing a common anchor prime `t` and one of the two nonzero orientations

`(lambda,mu)=(log(u/t),log(v/t))`

or

`(lambda,mu)=(log(t/v),log(t/u))`.

Thus the high-multiplicity nonzero shells are exactly the one-cancellation prime/prime shells.

3. If two prime factors cancel, the reduced ratio is `1`, hence the shell is `xi=0`; by uniqueness of reduced prime ratios this is the diagonal `lambda=mu` already separated in `VIS-203`.

Now use the fixed dangerous scale from `VIS-195` and `VIS-203`,

`b_y=log(1+2/y^2)`.

For every fixed `A>0`, all sufficiently large `y` satisfy

`A b_y < log(1+1/y)`.

But every nonzero prime/prime shell with primes at most `y` obeys

`|log(u/v)| >= log(1+1/y)`.

Therefore **no one-cancellation shell can occur in**

`0<|xi|<=A b_y`

once `y` is sufficiently large. Every exact shell in this dangerous window is noncancelling and has multiplicity at most `4`.

For the nonnegative amplitudes of `VIS-203`,

`B_xi=sum_(lambda-mu=xi) b_lambda b_mu`,

Cauchy--Schwarz consequently gives the exact structural bound

`sum_(0<|xi|<=A b_y) B_xi^2`

` <= 4 sum_(lambda!=mu, 0<|lambda-mu|<=A b_y) b_lambda^2 b_mu^2`.

So at the fixed normalized collision scale, **large exact-shell multiplicity is not the missing compactness mechanism**. The difficult mass can only come from having many distinct noncancelling shells in the tiny window, not from many prime-ratio representations reinforcing one shell.

**Evidence/status:** `EXACT-DERIVED + UNIQUE-FACTORIZATION CLASSIFICATION + NEGATIVE/CONTROL FRONTIER + NO-NOVELTY-CLAIM`.

No new multiplicative-Sidon theorem, prime-gap theorem, shell-energy decay estimate, or improvement of the `VIS-202` square-root-log threshold is claimed.

## 1. Representation dictionary

The source object is an ordered pair of signed prime-ratio frequencies `(lambda,mu)`. The target representation is the reduced positive rational

`R(lambda,mu)=exp(lambda-mu)=ad/(bc)`.

Equivalently, write a rational as its finitely supported prime-exponent vector. Then `lambda-mu` is the logarithmic image of the exponent vector

`e_a+e_d-e_b-e_c`.

The dictionary is exact because the logarithm is injective on positive rationals and prime factorization is unique. Reduction of `ad/(bc)` is the only information-losing step relevant here: it erases shared prime anchors. Precisely those erased anchors are what create large shell multiplicity.

This is why the cancellation classification is not cosmetic. In the noncancelling region the reduced rational remembers all four prime factors, while a prime/prime quotient forgets the common anchor `t` and can therefore collect many representations.

## 2. Noncancelling shells have at most four ordered representations

Assume

`gcd(ad,bc)=1`.

Fix the reduced rational `R=A0/B0=ad/(bc)`. Since `a,d` are prime, the multiset of prime factors of `A0` is exactly `{a,d}`. Likewise the prime factors of `B0` are exactly `{b,c}`.

Unique factorization therefore fixes both multisets. There are at most two ways to decide which numerator prime is `a` and which is `d`, and independently at most two ways to decide which denominator prime is `b` and which is `c`. This gives at most four ordered pairs `(lambda,mu)` in the shell.

Repeated numerator or denominator primes only reduce this count. Restrictions already present in the finite prime set can also remove assignments; they cannot create new ones.

## 3. One cancellation is exactly an anchored prime/prime shell

Suppose instead that the reduced quotient is nontrivial and a prime cancels. Since the unreduced numerator and denominator each contain exactly two prime factors, cancelling one common prime leaves

`R=u/v`

for distinct primes `u,v`.

Let `t` be the cancelled prime. Before reduction the numerator and denominator multisets must be

`{u,t}` and `{v,t}`.

Of the four formal assignments of these factors to `(a,d)` and `(b,c)`, two put the common `t` into the same prime ratio and create a zero frequency, which is excluded from `Lambda_y`. The two valid assignments are exactly

`(log(u/t),log(v/t))`

and

`(log(t/v),log(t/u))`.

For the full prime set up to `y`, each admissible anchor `t<=y`, `t!=u,v`, therefore supplies these two representations. This explains the potentially growing multiplicity: reduction forgets which anchor was used.

For the symmetric amplitudes of `VIS-203`, `b_(-lambda)=b_lambda`, the two anchor contributions even have the same weight. The amplification is real at prime/prime shells; it is simply too far from zero to enter the fixed `b_y` collision window.

## 4. Prime/prime shells are separated from the `y^-2` window

For distinct positive integers `u,v<=y`, after swapping if necessary let `u>v`. Then

`u/v >= 1+1/v >= 1+1/y`,

so

`|log(u/v)| >= log(1+1/y)`.

On the other hand,

`A b_y = A log(1+2/y^2) <= 2A/y^2`,

while

`log(1+1/y) >= 1/(y+1)`.

For fixed `A`, eventually `2A/y^2 < 1/(y+1)`. Hence every nonzero shell satisfying

`|xi|<=A b_y`

must be noncancelling.

The zero shell is different and remains highly populated, but it is exactly the diagonal contribution already removed when `VIS-203` writes the finite-start error as a sum over `xi!=0`.

## 5. Consequence for shell energy

Inside the dangerous window let `m_xi` be the number of ordered representations of `xi`. The previous sections give `m_xi<=4` for all sufficiently large `y` at fixed `A`.

For each shell, Cauchy--Schwarz yields

`B_xi^2`
` = (sum_(lambda-mu=xi) b_lambda b_mu)^2`
` <= m_xi sum_(lambda-mu=xi) b_lambda^2 b_mu^2`
` <= 4 sum_(lambda-mu=xi) b_lambda^2 b_mu^2`.

Distinct shells partition the ordered pairs, so summing gives the displayed bound in the claim.

This does **not** make the shell energy small by itself. It removes a different possible obstruction: the fourth-moment quantity cannot blow up at the fixed normalized scale because a single exact difference has a growing number of representations. Any failure of square-summability there must instead be caused by the aggregate weighted mass distributed over many distinct four-prime shells.

## Prior-art audit

The load-bearing mathematics is classical unique factorization and the familiar multiplicative-Sidon behavior of primes. In the standard terminology, a multiplicative Sidon set has unique pair products up to permutation; primes are the canonical elementary example. See Y. Jing and A. Mudgal, **Finding large additive and multiplicative Sidon sets in sets of integers**, *Mathematische Annalen* 391 (2025), 685--715, DOI `10.1007/s00208-024-02932-7`, for the standard multiplicative-Sidon definition and the prime example.

Related arithmetic-combinatorial work studies multiplicative energy of prime sets and the repulsion induced by logarithms; see I. D. Shkredov, **On some applications of GCD sums to Arithmetic Combinatorics**, arXiv:`2010.03020` (2020). These references bound novelty rather than supply the present proof.

No novelty is claimed for unique factorization, multiplicative Sidon terminology, or product-representation counting. The Mathia-specific content is the exact application to the `VIS-203` difference-shell representation and the observation that its only high-multiplicity fibers are separated by order `1/y` from the order `1/y^2` collision window.

## Boundaries and falsification

The multiplicity cap is tied to exact shells built from ratios of two primes. It does not automatically extend to approximate shell bins, products with more prime factors, generalized-prime systems, or a representation in which the reduced rational no longer retains the same factor data.

The fixed-`A` assumption matters. If the shell window widens from order `y^-2` toward order `y^-1`, prime/prime cancellation shells can enter and their anchor multiplicity must be treated explicitly.

The energy inequality is a reduction, not a decay theorem. It does not prove that the right-hand pair mass is `o(R_v(y,H)^2)` in the boundary regime left open by `VIS-202`.

Falsify the finding by producing a nonzero shell with `0<|xi|<=A b_y` for arbitrarily large `y` that has a cancelled prime anchor, or a noncancelling exact shell with more than four ordered prime-ratio representations.

## Research consequence

`VIS-203` left shell packing as the next compactness question after exact-shell sign cancellation was removed. The present result eliminates one natural concern: **dangerous exact shells cannot accumulate unbounded representation multiplicity**. The only shells that forget an arbitrary anchor are prime/prime quotients, and those sit parametrically outside the fixed normalized collision window.

The next coherent question is therefore not how to control one enormous exact fiber. It is whether the weighted mass of the many distinct noncancelling four-prime shells can be shown to spread thinly enough for

`sum_(0<|xi|<=A b_y) B_xi^2=o(R_v(y,H)^2)`

at or below the `VIS-202` square-root-log frontier, or whether a lower-bound construction shows that even bounded shell multiplicity leaves order-one energy. That is a new question and should be handled in a later invocation.