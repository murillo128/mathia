# PL-130 — Finite critical-line phase jets and samples are locally non-identifying for real Grosswald–Schnitzer deformations

## Claim

`PL-127` showed that the first critical-line reflection-phase derivative is a positive discriminator for one-sided Grosswald–Schnitzer deformations, while `PL-129` showed that this single scalar has exact aliases even in the integer endpoint subclass. A natural surviving idea is to retain finitely many additional phase derivatives or phase samples and hope that the resulting finite vector recovers a prescribed low prime-generator pattern.

For the original Grosswald–Schnitzer class with **real** generators this cannot work, no matter how many such finite observables are kept.

Let

`phi_q(s)=Z_q(s)/zeta(s)=prod_n (1-p_n^(-s))/(1-q_n^(-s))`

and, on the critical line, choose the continuous reflection phase

`R_q(1/2+it)=phi_q(1/2+it)/phi_q(1/2-it)=exp(i theta_q(t))`,

with `theta_q(0)=0`. Fix any finite family consisting of finitely many odd derivatives `theta_q^(m)(0)` and finitely many samples `theta_q(t_r)` at distinct positive heights. Fix also any prime index `j`.

Then there exist two admissible real Grosswald–Schnitzer sequences `q` and `q'` such that

- `p_n <= q_n,q'_n <= p_(n+1)` for every `n`;
- both sequences differ from the rational-prime sequence at only finitely many indices;
- `q_j != q'_j`;
- every chosen phase derivative and every chosen phase sample is **exactly equal** for `q` and `q'`.

The construction is local and uses only finitely many compensating tail coordinates. The proof is an inverse-function-theorem argument: the response functions of any finite collection of these natural phase observables are linearly independent on every sufficiently far real tail, so one can choose as many tail generator variables as observables with an invertible Jacobian and use them to compensate an arbitrary sufficiently small change in the prescribed low generator.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` for finite phase-fingerprint reconstruction in the **real** Grosswald–Schnitzer class.

This does not resolve `CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint`, whose narrowed research question deliberately restricts to **integer** generators. It instead proves that this integrality restriction is load-bearing: without discrete generator positions, every finite jet/sample fingerprint has exact local aliases. A positive integer reconstruction theorem must therefore use arithmetic discreteness rather than only analytic richness of the critical-line phase.

## Analytic setup without any critical-strip Euler-product extrapolation

Write `q_n=exp(x_n)` and define, for `x>0`,

`H_x(s)=log(1-exp(-x s))`.

For `Re(s)>0` the argument of the logarithm is nonzero. In the collision constructed below only finitely many `q_n` differ from `p_n`, so

`log phi_q(s)=sum_n [H_(log p_n)(s)-H_(x_n)(s)]`

is actually a **finite sum**. Consequently it is analytic throughout `Re(s)>0`, and the phase data at `Re(s)=1/2` are obtained from an honest nonvanishing analytic quotient, not by continuing a divergent Euler product term by term.

In `Re(s)>1`, this finite quotient is exactly `Z_q/zeta`. Multiplication by the same finite nonvanishing factor therefore supplies the continuation to `Re(s)>0` and preserves the zeta zero divisor there. This is the finite-support subfamily of the Grosswald–Schnitzer deformation class, so the same-zero statement needed here is analytically elementary once the quotient is written down.

Schwarz symmetry gives

`log R_q(1/2+it)=2i Im log phi_q(1/2+it)`,

so the continuous phase may be taken as

`theta_q(t)=2 Im log phi_q(1/2+it)`.

It is odd in `t`; all even derivatives at `0` vanish identically and carry no information.

## Response functions for odd central derivatives

For odd `m>=1`, expansion of a **single** Euler factor is valid at `Re(s)>0` and gives

`d^m/ds^m H_x(s)|_(s=1/2)
 = x^m sum_(k>=1) k^(m-1) exp(-k x/2)
 =: A_m(x)`.

The corresponding odd phase derivative differs from the sum of the `A_m(log p_n)-A_m(x_n)` only by the nonzero constant `2 i^(m-1)`. Thus the derivative of this observable with respect to one logarithmic generator coordinate is, up to a nonzero constant,

`u_m(x)=-A_m'(x)`.

As `x->infinity`,

`A_m(x)=x^m exp(-x/2)(1+O_m(exp(-x/2)))`,

and therefore

`u_m(x)=exp(-x/2)[(1/2)x^m-m x^(m-1)+O_m(x^m exp(-x/2))]`.

Hence, after multiplication by the common factor `exp(x/2)`, different odd derivative orders have different polynomial leading degrees. In particular, for any distinct odd orders `m_1<...<m_a`, the functions `u_(m_1),...,u_(m_a)` are linearly independent on every tail `(X,infinity)`. A linear relation would, after multiplying by `exp(x/2)`, have a highest nonzero polynomial degree that cannot be cancelled by lower degrees or the exponentially small remainder.

For the consecutive jet `m=1,3,...,2a-1`, this tail rank can also be seen directly from the asymptotic Jacobian. At tail points `x_i=c_i T` with distinct positive `c_i`, column and row rescaling sends the matrix to

`[c_i^(2r-1)]_(r,i)`,

whose determinant is

`(product_i c_i) product_(i<k) (c_k^2-c_i^2) != 0`.

Thus arbitrarily deep prime-gap coordinates can supply a full-rank compensating Jacobian for every finite central phase jet.

## Response functions for finitely many phase samples

Fix a positive height `t` and put `s_t=1/2+it`. The contribution of a logarithmic generator coordinate `x` to `theta_q(t)` is `-2 Im H_x(s_t)`, so its coordinate response is

`w_t(x)=-2 Im [s_t/(exp(s_t x)-1)]`.

For large `x`,

`exp(x/2) w_t(x)
 = -2[t cos(t x)-(1/2) sin(t x)] + O_t(exp(-x/2)).`

If `t_1,...,t_b` are distinct positive heights, the functions `w_(t_r)` are linearly independent on every tail. Indeed, an exact real linear relation would imply that the finite trigonometric polynomial

`sum_r c_r [t_r cos(t_r x)-(1/2)sin(t_r x)]`

tends to zero as `x->infinity`. A nonzero trigonometric polynomial with distinct positive frequencies cannot do that: its long-interval mean square has a strictly positive limit. Hence all coefficients must vanish.

The same argument also shows independence for a **mixed** finite family of odd central derivatives and positive phase samples. After multiplication by `exp(x/2)`, the derivative responses have distinct polynomial leading terms while the sample responses remain bounded trigonometric terms. The highest polynomial degree is forced to vanish first; after all polynomial coefficients vanish, trigonometric independence forces the sample coefficients to vanish.

Therefore any finite natural fingerprint of the form considered here has `d` linearly independent one-coordinate response functions on every far tail, where `d` is the number of nonredundant observables.

## Exact collision from the inverse function theorem

Fix the low index `j` that is supposed to be reconstructed. Choose an interior base value

`x_j^0 in (log p_j, log p_(j+1))`.

Let the finite fingerprint contain `d` nonredundant observables. Choose `d` distinct tail indices `n_1,...,n_d>j`. Because the response functions are real analytic and linearly independent on every tail, their evaluation determinant is not the zero analytic function. Hence the tail indices and interior base points

`x_(n_r)^0 in (log p_(n_r),log p_(n_r+1))`

may be chosen so that the `d x d` Jacobian with respect to these tail coordinates is invertible. All remaining generator coordinates are fixed at the rational primes.

Let

`F(x_j,x_(n_1),...,x_(n_d)) in R^d`

be the selected phase fingerprint. At the chosen base point, the partial derivative of `F` with respect to the `d` tail variables is invertible. The inverse function theorem therefore gives a neighborhood of `x_j^0` and smooth functions

`x_(n_r)=x_(n_r)(x_j)`

such that

`F(x_j,x_(n_1)(x_j),...,x_(n_d)(x_j))`

is exactly constant. Shrinking the neighborhood keeps every compensating coordinate inside its own Grosswald–Schnitzer interval.

Choose two distinct values of `x_j` in that neighborhood. They produce two admissible sequences whose selected critical-line phase data agree **exactly**, while the prescribed low generator differs. Only `j,n_1,...,n_d` need differ from the ordinary prime sequence.

This is stronger than a conditioning or finite-precision objection. It is genuine local non-injectivity, and it does not require an infinite tail, a limiting subsum, or approximate Diophantine cancellation.

## Why this does not contradict the positive scalar rigidity of PL-127

`PL-127` proves that the central slope `D(q)` is nonnegative for every one-sided deformation and that `D(q)=0` only for the undeformed prime sequence. The present collision does not challenge that statement.

The undeformed sequence sits at the **boundary** `q_n=p_n` of every Grosswald–Schnitzer interval, where the positive scalar has its global minimum. The inverse-function construction instead starts at interior generator values. Increasing one low coordinate can then be compensated by decreasing or increasing interior tail coordinates while all of them remain above their corresponding primes. Thus two already-deformed systems may share the same finite phase fingerprint even though neither can share the zero slope of the undeformed system.

Likewise, `PL-129` is complementary rather than redundant. `PL-129` constructs exact aliases for a single scalar while retaining **integer endpoint** generators; the present result handles arbitrarily many finite phase observables but uses the **continuous real** deformation freedom. Together they identify the precise unresolved corner: finite-dimensional reconstruction, if it exists at all, must exploit integer discreteness strongly enough to defeat both scalar subsum aliasing and continuum Jacobian compensation.

## Prior-art and novelty audit

Primary deformation source:

- **Emil Grosswald, F. J. Schnitzer**, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357. Their theorem permits arbitrary real `q_n` with `p_n<=q_n<=p_(n+1)` and constructs the nonvanishing quotient in `Re(s)>0` that preserves the zeta zero divisor.

The inverse function theorem, linear independence of distinct polynomial degrees, and linear independence of finite trigonometric/exponential polynomials are classical analysis and are not claimed as new. A targeted literature search around Grosswald–Schnitzer phase data, Taylor/critical-line fingerprints, and inverse reconstruction found the original deformation theorem and later uses of the same-zero class, but no source treating this finite-phase inverse problem or the local compensating-tail argument above.

No broad novelty claim is made. The durable contribution is the exact **matched-control theorem for this research line**: once the Grosswald–Schnitzer generators are allowed to move continuously inside their permitted prime gaps, finite critical-line phase data cannot identify a prescribed generator because finitely many tail directions can always absorb the same number of constraints.

## Consequence for the research line

The active phase-fingerprint route now has a sharp arithmetic boundary.

For real Grosswald–Schnitzer generators, every finite collection of the most natural critical-line phase observables considered so far — odd Taylor data at the self-dual point, finitely many nonzero phase samples, or any finite mixture of the two — is exactly locally non-injective. Increasing the number of observables does not fix the problem: the deformation class supplies the same number of independent tail coordinates.

For integer generators, the inverse-function mechanism is unavailable. That is precisely why the narrowed `CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint` remains open after this finding. A positive result must derive a discrete tail-uniform separation theorem; a negative result must obtain an exact integer collision by subsum/Diophantine or other arithmetic structure. Dimension counting or smooth identifiability arguments are no longer enough.

For RH itself, the conclusion remains diagnostic rather than a localization mechanism. All members of the control class retain the same zeta zero divisor in `Re(s)>0`. The finding says that finitely sampled reflection phase is not, by itself, a finite arithmetic coordinate chart for that class. Any future prime-lattice spectral construction that uses only finitely many such phase constraints must explain where genuinely discrete rational-prime rigidity enters.