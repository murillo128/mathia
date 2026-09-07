# VIS-077 — neighboring-prime modes force growth of the signed Euler-product resonance norm

## Claim

Let `B_(X,sigma)` be the coefficient-weighted reciprocal-frequency norm from `VIS-076`,

`B_(X,sigma)=sum_(k!=0) [prod_(p<=X) p^(-sigma |k_p|)] / |sum_(p<=X) k_p log p|`,

with `sigma>0`. Put

`m_X = pi(X)-pi(X/2)`,

the number of primes in `(X/2,X]`. Whenever `m_X>=2`, the nearest-neighbor prime modes alone give the exact finite lower bound

`B_(X,sigma) >= X^(-2 sigma) (m_X-1)^2`.

Consequently the prime number theorem implies

`B_(X,sigma) >= (1/4+o(1)) X^(2-2 sigma)/(log X)^2`.

In particular, on the critical-line parameter `sigma=1/2`,

`B_(X,1/2) >= (1/4+o(1)) X/(log X)^2`.

Thus the fixed-support `O(1/L)` proof from `VIS-076` cannot have a dimension-uniform coefficient. More sharply, if

`C_X = 2 P_X(1,0) B_(X,1/2)`

is the exact `l^1` certificate constant appearing in that critical-line bound, then Mertens' product theorem gives

`C_X >= (e^gamma/2+o(1)) X/log X`.

Therefore any joint-limit proof that tries to establish uniform moving-window collapse solely by forcing the `VIS-076` triangle-inequality certificate `C_X/L` to zero must at least have

`L >> X/log X`.

This is a **lower bound on the proof certificate, not on the actual moving-window deviation**. It does not show that `|P_X(1/2,t)|^2` retains a macroscopic window signal when `L` is smaller. It shows that the coefficientwise `l^1` small-divisor route from `VIS-076` is intrinsically too expensive there; any stronger result must exploit cancellation, an `l^2`/mean-square structure, or a more precise growing-cutoff theorem.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PNT/MERTENS INPUT + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No sharp asymptotic for `B_(X,sigma)`, lower bound for the true window discrepancy, optimal cutoff/window threshold, zeta approximation result, or RH consequence is claimed.

## 1. Restrict to neighboring-prime signed characters

Let

`X/2 < p_1 < p_2 < ... < p_m <= X`

be all primes in `(X/2,X]`, so `m=m_X`. For each adjacent pair `p_j<p_(j+1)`, take the signed exponent vector having `-1` at `p_j`, `+1` at `p_(j+1)`, and zero elsewhere. Its coefficient and frequency are

`w_j=(p_j p_(j+1))^(-sigma)`,

`lambda_j=log(p_(j+1)/p_j)`.

Because both primes are at most `X`,

`w_j >= X^(-2 sigma)`.

Writing `g_j=p_(j+1)-p_j` and using `log(1+u)<=u`,

`lambda_j = log(1+g_j/p_j) <= g_j/p_j <= 2 g_j/X`,

so

`1/lambda_j >= X/(2 g_j)`.

Every one of these modes is a legitimate term in the positive sum defining `B_(X,sigma)`. Hence

`B_(X,sigma) >= (X^(1-2 sigma)/2) sum_(j=1)^(m-1) 1/g_j`.

No Baker estimate is used in this direction.

## 2. Cauchy turns prime density into resonance mass

The adjacent gaps telescope:

`sum_(j=1)^(m-1) g_j = p_m-p_1 <= X/2`.

Cauchy-Schwarz therefore gives

`sum_(j=1)^(m-1) 1/g_j`
` >= (m-1)^2 / sum_j g_j`
` >= 2(m-1)^2/X`.

Substitution yields the exact finite inequality

`B_(X,sigma) >= X^(-2 sigma)(m_X-1)^2`.

The point is structural: the growing resonance norm is already forced by the most elementary signed characters `e_q-e_p`. It does not require large exponent vectors or exceptionally delicate Diophantine approximations among many prime logarithms.

## 3. Prime-number-theorem scale

The prime number theorem gives

`pi(X)-pi(X/2) = (1/2+o(1)) X/log X`.

Therefore

`(m_X-1)^2 = (1/4+o(1)) X^2/(log X)^2`,

and the finite inequality becomes

`B_(X,sigma) >= (1/4+o(1)) X^(2-2 sigma)/(log X)^2`.

For every fixed `sigma<1`, this already forces polynomial growth of the `VIS-076` reciprocal-frequency norm. At `sigma=1/2`, the lower scale is `X/(log X)^2`.

This does not assert that neighboring-prime modes dominate `B_(X,sigma)`. More complicated smooth-ratio resonances may make the true norm much larger.

## 4. Critical-line consequence for the VIS-076 certificate

At `sigma=1/2`, `VIS-076` proves

`sup_h |M_(X,L)(h)-P_X(1,0)| <= C_X/L`,

where

`C_X=2 P_X(1,0) B_(X,1/2)`.

Mertens' product theorem gives

`P_X(1,0)=prod_(p<=X)(1-1/p)^(-1)=(e^gamma+o(1)) log X`.

Combining with the lower bound above,

`C_X >= (e^gamma/2+o(1)) X/log X`.

Thus a proof that uses this exact coefficientwise absolute-value certificate and asks its right-hand side to vanish must satisfy

`X/(L log X) -> 0`.

Equivalently, the `l^1` resonance certificate cannot by itself establish critical-line uniform collapse in regimes with `L=O(X/log X)`.

This conclusion is deliberately about the **method**. The actual signed Fourier modes can cancel, and a mean-square or directly integrated argument can be much sharper than the sum of absolute coefficient contributions.

## 5. Prior art and novelty boundary

All ingredients used in the lower bound are classical. NIST DLMF §27.2 records the prime number theorem `pi(x)~x/log x`; the Mertens product asymptotic is classical and already anchored in this line's sources. Gonek and Keating, **Mean values of finite Euler products**, *Journal of the London Mathematical Society* 82:3 (2010), 763–786, DOI `10.1112/jlms/jdq049`, study mean values of squared finite Euler products in growing-cutoff regimes and remain the direct analytic-number-theory boundary around this observable.

The present finding does not claim a new prime-gap theorem, mean-value theorem, or finite-Euler-product theorem. Its Mathia-specific role is narrower: it audits the exact coefficient-weighted norm introduced in `VIS-076` and shows that the fixed-support Baker/triangle-inequality proof mechanism necessarily develops a large growing-support constant even before high-dimensional Diophantine resonances are considered.

## Boundary and falsification

The exact finite lower bound uses only the signed nearest-neighbor characters associated with primes in `(X/2,X]`. It is valid for every `sigma>0` once that interval contains at least two primes.

The PNT asymptotic is useful only as `X->infinity`. For `sigma>=1` the displayed asymptotic lower bound need not be informative about growth, and no monotonic asymptotic for the full `B_(X,sigma)` is asserted here.

Most importantly, failure of the `l^1` certificate is not evidence of a surviving arithmetic signal. A cancellation-sensitive estimate may still prove moving-window collapse for much shorter windows. Falsify the finite inequality by finding an error in the neighboring-prime coefficient, the logarithmic bound, the telescoping gap sum, or the Cauchy step; falsify the asymptotic consequence by violating the stated PNT/Mertens inputs.

## Research consequence

The growing-support frontier should no longer be phrased merely as "make the Baker constant uniform" or "estimate `B_(X,sigma)` better." On the critical line, the exact `l^1` resonance norm is already forced to be at least of order `X/(log X)^2`, and its `VIS-076` window certificate carries at least order `X/log X` after the Euler-product mean factor is restored.

The next useful signed-support test should therefore be **cancellation-sensitive**: for example, the exact sinc-weighted `l^2` spectral energy of the moving-window observable, a direct mean-square theorem for the growing finite Euler product, or another statistic whose proof does not discard all phase cancellation term by term. This narrows `CLUE-zeta-prime-phase-recursive-geometry` without claiming that the growing-support route itself is closed.