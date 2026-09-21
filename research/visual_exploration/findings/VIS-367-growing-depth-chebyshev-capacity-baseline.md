# VIS-367 — growing positive compact depth has a universal Chebyshev-capacity collapse baseline

## Claim

Let `mu` be any positive probability measure supported on a compact interval `K=[a,b]` of length `L=b-a>0`. For each depth `q>=1`, let

`T_(mu,q) : R^q -> L^2(mu)`

be the monomial sampling operator

`(T_(mu,q)c)(x)=sum_(d=0)^(q-1) c_d x^d`,

and let

`s_1(q)>=...>=s_q(q)>=0`

be its singular values. Let `Z_q(mu)` be the Vandermonde partition sum from `VIS-366`, so exactly

`Z_q(mu)=det(T_(mu,q)^* T_(mu,q))=prod_(j=1)^q s_j(q)^2`.

Then growing depth already carries a universal source-free compact-capacity collapse.

For every `q>=1`,

`Z_q(mu) <= 4^(q-1) (L/4)^(q(q-1))`.

In particular, after the standard affine normalization `K=[-1,1]`,

`Z_q(mu) <= 2^(-(q-1)(q-2))`.

Moreover, for every `q>=2`,

`s_q(q) <= 2 (L/4)^(q-1)`.

Hence on `[-1,1]`,

`s_q(q) <= 2^(2-q)`

and, because `s_1(q)>=1`,

`kappa(T_(mu,q)) >= 2^(q-2)`

whenever `T_(mu,q)` has full rank; if it does not, the condition number is infinite.

Thus **a rapidly shrinking Vandermonde determinant or raw monomial smallest singular value is generic source-free compact polynomial geometry once the cancellation depth grows**. It cannot by itself be credited as arithmetic localization or stronger cancellation. Any growing-depth Wang proposal must first quotient this Chebyshev/capacity baseline and then repay the coefficient-coordinate and destination costs of using the high-degree near-null direction.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CHEBYSHEV MINIMAX/ORTHOGONAL-POLYNOMIAL SPECIALIZATION + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not close growing cancellation depth as a route, does not give a lower bound on the usable Wang gain, and proves no stronger estimate for the Chebyshev-theta remainder, zeta zeros, or RH.

## 1. Gram determinants factor through monic orthogonal-polynomial norms

Let

`G_q=T_(mu,q)^*T_(mu,q)`

be the `q x q` moment Gram matrix in the monomial basis. Apply Gram-Schmidt to

`1,x,...,x^(q-1)`

without rescaling the leading coefficient. This produces monic orthogonal polynomials

`p_0,p_1,...,p_(q-1)`

with squared `L^2(mu)` norms

`h_n=integral_K |p_n(x)|^2 dmu(x)`.

The change from monomials to these monic polynomials is unit triangular, hence has determinant one. Therefore

`Z_q(mu)=det G_q=prod_(n=0)^(q-1) h_n`.

Equivalently, `h_n` is the minimum `L^2(mu)` norm squared among all monic degree-`n` polynomials. This is the growing-depth form of the same moment-Gram geometry isolated in `VIS-366`.

## 2. Chebyshev gives a measure-independent capacity ceiling

For `n>=1`, the monic polynomial of least uniform norm on `K=[a,b]` is the affine Chebyshev polynomial. Its uniform norm is

`M_n(K)=2 (L/4)^n`.

Because `mu` is a probability measure,

`||f||_(L^2(mu)) <= ||f||_(L^infinity(K))`.

Since `p_n` minimizes the monic `L^2(mu)` norm,

`h_n <= M_n(K)^2 = 4 (L/4)^(2n)`.

Also `h_0=1`. Multiplying for `n=1,...,q-1` gives

`Z_q(mu)`
` = prod_(n=0)^(q-1) h_n`
` <= prod_(n=1)^(q-1) 4 (L/4)^(2n)`
` = 4^(q-1) (L/4)^(q(q-1))`.

For `K=[-1,1]`, `L=2`, so

`Z_q(mu) <= 2^(2(q-1)-q(q-1)) = 2^(-(q-1)(q-2))`.

The determinant therefore has a universal `exp(-Theta(q^2))` compact-capacity ceiling in normalized coordinates even before any support clustering, special weighting, or arithmetic source information is introduced.

## 3. The raw monomial smallest singular value collapses exponentially

Take the degree `n=q-1` affine Chebyshev polynomial normalized to have uniform norm one on `K`. Its leading coefficient is

`1/M_n(K)`.

Let `c` be its monomial coefficient vector. Then

`||c||_2 >= 1/M_n(K)`.

Normalize the coefficient vector by setting `u=c/||c||_2`. Since `||u||_2=1`, the variational definition of the smallest singular value gives

`s_q(q) <= ||T_(mu,q)u||_(L^2(mu))`.

But the corresponding polynomial has uniform norm at most `1/||c||_2`, so

`s_q(q) <= 1/||c||_2 <= M_n(K)=2(L/4)^(q-1)`.

On `[-1,1]`, this becomes

`s_q(q) <= 2^(2-q)`.

The constant coefficient vector `e_0` maps to the constant function `1`, whose `L^2(mu)` norm is one. Hence `s_1(q)>=1`, and on the normalized interval

`kappa(T_(mu,q))=s_1(q)/s_q(q) >= 2^(q-2)`

whenever the map has full rank.

This is not an arithmetic instability. It is present for every positive probability measure on the interval and arises from expressing high-degree polynomial directions in raw monomial coordinates.

## 4. What this does and does not quotient in the Wang branch

`VIS-342` showed that, inside the scalar Vinogradov--Korobov optimization model, changing the power class by a fixed amount requires polynomial growth of the effective truncation order. `VIS-366` then showed that at fixed depth every positive compact coefficient bank is already priced by its moment Gram and Vandermonde partition sums.

The present result connects those two boundaries. Once `q` itself grows, the positive compact moment geometry develops a large source-free effect automatically:

- the full partition determinant can decay like an `exp(-Theta(q^2))` capacity scale;
- the raw monomial coefficient map always admits an exponentially small singular direction in normalized compact coordinates.

Therefore a growing-depth construction cannot use the mere appearance of very small `Z_q`, a rapidly increasing monomial condition number, or a tiny raw coefficient singular value as evidence that arithmetic information has been localized. Those effects exist before the source is consulted.

A serious growing-depth proposal must instead specify a coefficient topology/normalization that survives change of polynomial coordinates, or explicitly include the change-of-basis norm and the Wang destination repayment. If it uses the raw monomial coordinates because those coordinates are physically tied to tail coefficients, then the Chebyshev near-null direction is a baseline filter-design effect whose coefficient cost must be charged rather than counted as arithmetic gain.

## 5. The remaining growing-depth question

This finding does **not** show that growing `q` is useless. The scalar order itself can alter the zero-free/truncation balance, and a source-dependent or non-Hilbert construction may use high degree in a way not captured by passive positive compact conditioning.

The sharper test is now:

1. affine-normalize the compact node coordinate and identify the actual coefficient norm used by the Wang destination;
2. quotient the universal Chebyshev/capacity collapse of the positive polynomial space;
3. include the norm of any coordinate change used to expose a better-conditioned basis;
4. combine that cost with the growing-order/truncation balance from `VIS-342` and the remaining Wang destination terms;
5. credit arithmetic structure only to a residual gain that survives these source-free costs.

So growing depth remains open only as a **net destination mechanism**, not as raw high-degree Vandermonde ill-conditioning.

## Prior-art audit

The approximation-theory input is classical. NIST DLMF §18.38(i), “Approximation Theory,” records that the monic Chebyshev polynomial `2^(1-n) T_n(x)` has the minimax property on `[-1,1]`. The equivalent affine-interval formula gives the least uniform norm `2((b-a)/4)^n` for a monic degree-`n` polynomial on `[a,b]`.

The Gram-determinant/orthogonal-polynomial factorization is standard and is already within the prior-art boundary recorded for `VIS-366` through classical Andreief/Cauchy--Binet and orthogonal-polynomial ensemble machinery. No novelty is claimed for Chebyshev minimax, monic orthogonal-polynomial extremality, moment determinants, or polynomial-basis conditioning.

The Mathia-specific contribution is the audit consequence for the current Wang frontier: **the first growing-depth effect visible in positive compact monomial geometry is itself a universal source-free capacity/coordinate collapse**, so it must be removed before high-order conditioning can be interpreted as localization of the arithmetic source.

## Dependencies

- `VIS-342`: a fixed improvement of the scalar Vinogradov--Korobov power class requires polynomially growing effective order.
- `VIS-354`: Wang tail coefficients are raw truncated power moments of the bank weights.
- `VIS-361`: positive coefficient weights reduce to a positive moment Gram after pooled normalization.
- `VIS-366`: fixed-depth positive compact geometry is exactly priced by Vandermonde partition sums.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose growing-depth frontier this result narrows.

## Research consequence

Growing depth is not automatically a new arithmetic resource. In normalized compact coordinates, positive polynomial sampling acquires universal Chebyshev-capacity collapse before any source dependence appears: `Z_q` has a super-exponential determinant ceiling and the raw monomial smallest singular value has an exponential ceiling.

Future Wang work may still exploit growing cancellation depth, but only after quotienting this baseline and showing a **net** improvement once coefficient normalization, basis-change cost, truncation/order growth, and the complete destination repayment are included.