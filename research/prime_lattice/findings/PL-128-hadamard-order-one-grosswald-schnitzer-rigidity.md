# PL-128 — Order-one Hadamard rigidity defeats all Grosswald–Schnitzer deformations without using the integer prime lattice

## Claim

`PL-125` uses Grosswald–Schnitzer deformations as a matched control: for arbitrary real generators

`p_n <= q_n <= p_(n+1)`,

the modified Euler product

`Z_q(s)=product_n (1-q_n^(-s))^(-1)`

extends meromorphically to `Re(s)>0` and has exactly the same zeros, with multiplicity, as `zeta` there. `PL-126` showed that for **integer** `q_n`, adding Hamburger's ordinary-Dirichlet-series hypotheses and the exact Riemann functional equation forces `Z_q=zeta`.

There is a different rigidity mechanism that removes the integrality hypothesis entirely, but at the price of assuming the full zeta-style global analytic type. Define the completed function

`Xi_q(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) Z_q(s)`.

Assume that `Xi_q` extends to an entire function of order at most one and satisfies the exact Riemann symmetry

`Xi_q(s)=Xi_q(1-s)`.

Then necessarily

`Xi_q(s)=xi(s)`,

hence `Z_q(s)=zeta(s)` and therefore `q_n=p_n` for every `n`.

The proof is purely classical Hadamard rigidity. Grosswald–Schnitzer already supplies the same zero divisor in `Re(s)>0`; the functional equation reflects that equality to the whole plane, and two entire functions of order at most one with the same zeros differ only by `exp(as+b)`. Reflection symmetry forces `a=0`, and the Euler-product normalization as `Re(s)->+infinity` forces the remaining constant to be one.

**Evidence/status:** `LITERATURE+DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION` for interpreting successful rejection of the Grosswald–Schnitzer control as evidence that a proposed mechanism has used the exact rational-prime lattice.

The result is not an RH mechanism. In fact it sharpens the opposite warning: once a candidate already assumes the Grosswald–Schnitzer zero divisor together with a zeta-style order-one completion, the deformation collapses by generic entire-function rigidity **without using the exponent lattice, unique factorization, or integrality of the generators at all**. Thus a future construction must derive the completion/positivity from arithmetic structure rather than count the abstract uniqueness of the completed function as prime-specific evidence.

## Step 1: Grosswald–Schnitzer already fixes the right-half-plane divisor

Grosswald and Schnitzer prove that

`Z_q(s)=phi_q(s) zeta(s)`

in `Re(s)>0`, where `phi_q` is analytic and nonvanishing there. Consequently `Z_q` and `zeta` have exactly the same zeros, with the same multiplicities, in the open half-plane `Re(s)>0`. The modified function has a simple pole at `s=1` with positive residue, and the defining Euler product is zero-free in `Re(s)>1`.

This is a theorem about the meromorphic continuations, not a formal continuation of the Euler product. It is precisely the matched same-zero control used in `PL-125` and `PL-127`.

Now impose the additional global hypothesis that

`Xi_q(s)=(1/2)s(s-1)pi^(-s/2)Gamma(s/2)Z_q(s)`

is entire and satisfies `Xi_q(s)=Xi_q(1-s)`. At `s=1`, the factor `s-1` cancels the simple pole of `Z_q`, so `Xi_q(1)` is nonzero; symmetry then gives `Xi_q(0)=Xi_q(1) != 0`.

Every zero of `Xi_q` in `Re(s)>0` is therefore one of the ordinary nontrivial zeta zeros, with the same multiplicity. Conversely, an extra zero `rho` with `Re(rho)<=0` would reflect to a zero `1-rho` with `Re(1-rho)>=1`. There are no such zeros: for `Re(s)>1` this follows from the absolutely convergent zero-free Euler product, while on `Re(s)=1` Grosswald–Schnitzer's same-zero theorem and the classical zero-free line for `zeta` exclude them; `s=1` itself is nonzero after completion. Hence `Xi_q` and `xi` have exactly the same zero divisor on the whole plane.

## Step 2: order one plus the same divisor leaves only an exponential gauge

The Riemann `xi` function is entire of order one. Classical Hadamard factorization says that an entire function of finite order at most one is determined by its zero divisor up to an exponential factor of degree at most one. Since `Xi_q` and `xi` have the same zeros with multiplicity, there exist constants `a,b in C` such that

`Xi_q(s)=exp(a s+b) xi(s)`.

This is the only analytic freedom left. It is not arithmetic: no coefficient or prime information enters this step.

Both completed functions obey the same reflection law, so

`exp(a s+b) xi(s)=Xi_q(s)=Xi_q(1-s)=exp(a(1-s)+b) xi(1-s)`.

Using `xi(1-s)=xi(s)` and analytic continuation across the isolated zeros gives

`exp(a(2s-1))=1`

for every `s`. Differentiating, or simply using nonconstancy of the exponential unless `a=0`, yields

`a=0`.

Thus `Xi_q=c xi` for a nonzero constant `c`.

Finally, on the real axis `sigma->+infinity`, both Euler products tend to one:

`Z_q(sigma)->1`,    `zeta(sigma)->1`,

because `q_n>=p_n` and `sum_p p^(-sigma)->0`. Since the completion factors cancel in the quotient,

`c = Xi_q(sigma)/xi(sigma) = Z_q(sigma)/zeta(sigma) -> 1`.

Therefore `c=1`, proving

`Xi_q=xi` and `Z_q=zeta`.

## Step 3: equality of the functions forces the real generators themselves to be the primes

No ordinary integer Dirichlet expansion is needed to recover the generator sequence. Suppose the two sequences differ and let `j` be the first changed index. Then

`q_i=p_i` for `i<j`,

while the Grosswald–Schnitzer interval condition gives

`q_j>p_j`.

For large positive real `sigma`, use the absolutely convergent logarithm

`log(Z_q(sigma)/zeta(sigma))
 = sum_n [log(1-p_n^(-sigma))-log(1-q_n^(-sigma))]`.

All terms before `j` vanish. The `j`th contribution has asymptotic

`-p_j^(-sigma)+q_j^(-sigma)+O(p_j^(-2sigma))
 = -p_j^(-sigma)(1+o(1))`,

because `q_j>p_j`. The complete tail `n>j` is also `o(p_j^(-sigma))`: every later `p_n` and `q_n` is bounded below by `p_(j+1)>p_j`, and the corresponding absolutely convergent Dirichlet tail decays faster than the first missing scale. Hence

`log(Z_q(sigma)/zeta(sigma)) = -p_j^(-sigma)(1+o(1))`,

which cannot vanish identically. This contradicts `Z_q=zeta`. Therefore no first changed index exists and

`q_n=p_n` for all `n`.

This also shows why integrality is unnecessary here. The recovery uses only the ordered positive frequency scales and their asymptotic separation at `+infinity`.

## Relation to PL-126

`PL-126` remains correct and useful. Hamburger rigidity proves a stronger kind of converse statement from an ordinary Dirichlet-series coefficient structure plus global continuation/growth and the Riemann functional equation; it does **not** assume in advance that the zero divisor agrees with zeta. That is why the integer coefficient lattice matters there.

The present result starts from the much more specialized Grosswald–Schnitzer matched-control class, where equality of the right-half-plane zero divisor is already a theorem. Inside that class, if one additionally promotes the modified function all the way to a Riemann-symmetric **order-one entire completion**, Hadamard factorization makes the integer coefficient hypothesis unnecessary.

The two rigidity mechanisms should therefore not be conflated:

- Hamburger: coefficient/Dirichlet structure + functional equation + growth => identify `zeta`, without assuming its zero divisor.
- Hadamard in the Grosswald–Schnitzer class: same divisor + order-one entire completion + reflection => identify `xi`, without using the integer lattice.

This distinction materially changes the interpretation of the Grosswald–Schnitzer falsification test. A candidate that rejects the deformation merely because its completed entire function is required to have the same divisor, order, and reflection symmetry has not demonstrated that exact rational-prime arithmetic supplied the rigidity; generic entire-function theory supplied it.

## Adversarial boundary

The order hypothesis is load-bearing. Reflection symmetry and a common zero divisor alone do not force equality. For example, multiplying `xi(s)` by

`exp(c (s-1/2)^2)`

preserves the zero divisor and the symmetry `s<->1-s`, but raises the entire order to two. More general nonvanishing symmetric factors exist if zeta-like growth is not imposed. Thus the theorem does not say that the functional equation by itself kills arbitrary zero-preserving deformations.

Conversely, the same-zero hypothesis is also load-bearing. Hadamard factorization cannot locate the zeros. If ordinary zeta has an off-critical zero, every Grosswald–Schnitzer function in the original half-plane class has that same off-critical zero, and the argument above contains no positivity principle capable of moving it onto `Re(s)=1/2`.

The theorem therefore does **not** weaken the README's Beurling/generalized-prime control. It says only that one particular control can become vacuous if the proposed mechanism assumes enough global analytic data to determine an order-one entire function from an already-supplied divisor. A genuine RH mechanism must derive a localization/positivity statement that survives this distinction.

## Prior art and novelty audit

Primary deformation source:

- **Emil Grosswald, F. J. Schnitzer**, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357. Their Theorem 1 gives the meromorphic continuation to `Re(s)>0` and equality of the zero divisor there; the nonvanishing quotient `phi_q` is the starting point above.

Classical entire-function source:

- **H. M. Edwards**, *Riemann's Zeta Function*, Academic Press, 1974; Dover reprint, 2001. Chapter 1, especially the sections on `xi`, its zeros, and its product representation, gives the order-one/Hadamard framework for the Riemann `xi` function.
- **R. P. Boas, Jr.**, *Entire Functions*, Academic Press, New York, 1954. Classical reference for Hadamard factorization of finite-order entire functions.

No novelty is claimed for Grosswald–Schnitzer, Hadamard factorization, or uniqueness of an order-one entire function up to an exponential factor once its divisor is fixed. A targeted search around modified zeta functional equations, same-zero entire functions, and Hadamard uniqueness found these ingredients as classical analysis rather than a new theorem family. The durable contribution here is the **matched-control synthesis**: it exposes that the strongest natural global completion of a Grosswald–Schnitzer control collapses before exact prime-lattice arithmetic is used.

## Consequence for the research line

`PL-125` established that the zero divisor plus a square-free/self-adjoint prime-lattice realization does not identify the rational primes. `PL-126` then showed that ordinary integer Dirichlet structure plus the exact Riemann functional equation does identify zeta. The present finding separates a third effect:

`same zero divisor + order-one global completion + Riemann reflection`

already identifies `xi` by generic Hadamard rigidity.

Accordingly, future prime-lattice mechanisms should not treat “the Grosswald–Schnitzer deformation fails my completed functional equation/order-one test” as sufficient evidence of arithmetic specificity. The decisive question is **where the completion, growth, and especially the missing positivity/localization law came from**. To advance RH rather than merely identify the already-known completed function, that law must be derived from exact rational-prime/global arithmetic structure and must fail matched generalized-prime or freely programmable entire-function controls for a reason stronger than zero-divisor uniqueness.