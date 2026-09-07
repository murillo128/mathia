# VIS-078 — signed Euler-product l2 energy separates resonance-certificate growth from actual window mass

## Claim

Fix `sigma>0` and a finite prime cutoff `X`. Let

`P_X(sigma,t)=prod_(p<=X) (1-p^(-sigma-it))^(-1)`

and let

`M_(X,L)(h)=(1/L) integral_h^(h+L) |P_X(sigma,t)|^2 dt`.

Using the notation of `VIS-076`,

`lambda_k=sum_(p<=X) k_p log p`,

`w_k=prod_(p<=X) p^(-sigma |k_p|)`,

and

`A_X=P_X(2 sigma,0)`,

the long-height mean-square fluctuation of the moving-window mean has the exact cancellation-sensitive formula

`V_(X,sigma)(L)`
` = lim_(T->infinity) (1/T) integral_0^T |M_(X,L)(h)-A_X|^2 dh`
` = A_X^2 sum_(k!=0) w_k^2 sinc^2(L lambda_k/2)`.

Thus the natural `l^2` object is the **actual sinc-filtered spectral energy**, not the absolute reciprocal-frequency norm from `VIS-076`.

For fixed `X`, put

`Q_(X,sigma)=sum_(k!=0) w_k^2/lambda_k^2`.

The same fixed-set Baker input as in `VIS-076` gives `Q_(X,sigma)<infinity`, and hence

`V_(X,sigma)(L) <= [4 A_X^2 Q_(X,sigma)]/L^2`.

On the critical-line parameter `sigma=1/2`, neighboring primes in `(X/2,X]` force this **secondary `l^2` reciprocal-frequency certificate** to grow. If

`m_X=pi(X)-pi(X/2)`,

then

`Q_(X,1/2) >= 2 (m_X-1)^3/X^2`
` = (1/4+o(1)) X/(log X)^3`.

Since Mertens' product theorem gives

`A_X=P_X(1,0)~e^gamma log X`,

the coefficient in the displayed `L^-2` bound satisfies

`4 A_X^2 Q_(X,1/2) >= (e^(2 gamma)+o(1)) X/log X`.

Therefore any proof that tries to establish growing-support mean-square collapse solely by forcing this reciprocal-frequency `l^2` certificate to zero must at least have

`L >> sqrt(X/log X)`.

However, the **actual sinc-filtered energy carried by the very neighboring-prime modes that force the certificate growth vanishes**. Let `V_neigh(X,L)` be the contribution to `V_(X,1/2)(L)` from the two signed characters

`+e_(p_(j+1))-e_(p_j)` and `-e_(p_(j+1))+e_(p_j)`

for consecutive primes `p_j<p_(j+1)` in `(X/2,X]`. Then uniformly for every `L>0`,

`V_neigh(X,L)`
` <= 8 A_X^2 (m_X-1)/X^2`
` = (4 e^(2 gamma)+o(1)) (log X)/X`
` -> 0`.

So the elementary near-resonances responsible for the growth of both the `VIS-077` `l^1` certificate and the present reciprocal-frequency `l^2` certificate are **certificate-heavy but energy-light**. Their small denominators do not by themselves produce a persistent moving-window signal.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PARSEVAL/PNT/MERTENS SPECIALIZATION + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No sharp asymptotic for the full sinc-filtered energy, optimal joint cutoff/window threshold, lower bound for the true growing-support fluctuation, zeta approximation theorem, or RH consequence is claimed.

## 1. Exact long-height Parseval formula

`VIS-076` gives the absolutely and uniformly convergent Fourier expansion

`|P_X(sigma,t)|^2`
` = A_X sum_(k in Z^(pi(X))) w_k exp(-it lambda_k)`.

After averaging over a length-`L` window,

`M_(X,L)(h)-A_X`
` = A_X sum_(k!=0) w_k`
`   exp(-i(h+L/2)lambda_k) sinc(L lambda_k/2)`.

Because the prime logarithms are rationally independent over the integers, unique factorization gives

`lambda_k=lambda_l  <=>  k=l`.

The displayed Fourier series is absolutely convergent, so its square may be averaged termwise. Long-height averaging in `h` annihilates every cross term with `k!=l`, while the diagonal terms survive. Hence

`V_(X,sigma)(L)`
` = A_X^2 sum_(k!=0) w_k^2 sinc^2(L lambda_k/2)`.

Equivalently, this is ordinary Parseval on the finite prime torus for the windowed observable. It is the exact matched prime-phase null energy: no random-phase approximation is being introduced.

This formula is cancellation-sensitive in the relevant sense. The phases have already been orthogonalized before the coefficients are aggregated, so one does not replace the spectrum by the termwise absolute-value sum used for the uniform `l^1` bound in `VIS-076`.

## 2. The fixed-support l2 reciprocal certificate

For fixed `X`, the same Baker lower bound used in `VIS-076` gives constants `c_X,A_X'>0` such that

`|lambda_k| >= c_X (1+||k||_infinity)^(-A_X')`

for every `k!=0`.

Since `w_k^2` decays exponentially in `||k||_1`, it follows exactly as before that

`Q_(X,sigma)=sum_(k!=0) w_k^2/lambda_k^2 < infinity`.

Using

`|sinc y| <= min(1,1/|y|)`

gives

`sinc^2(L lambda_k/2) <= 4/(L^2 lambda_k^2)`,

and therefore

`V_(X,sigma)(L) <= 4 A_X^2 Q_(X,sigma)/L^2`.

At fixed support this is a legitimate strengthening from an `l^1` uniform-in-`h` estimate to an `l^2` long-height estimate. The key question is again what happens when the support grows.

## 3. Neighboring primes force growth of Q

Let

`X/2 < p_1 < p_2 < ... < p_m <= X`

be all primes in the upper dyadic half, and write

`g_j=p_(j+1)-p_j`.

For the signed vector `k=e_(p_(j+1))-e_(p_j)` at `sigma=1/2`,

`w_k^2=(p_j p_(j+1))^(-1) >= X^(-2)`.

Also

`lambda_k=log(p_(j+1)/p_j)`
` <= g_j/p_j`
` <= 2g_j/X`,

so

`w_k^2/lambda_k^2 >= 1/(4 g_j^2)`.

The opposite signed vector contributes the same amount. Hence the neighboring modes alone give

`Q_(X,1/2) >= (1/2) sum_(j=1)^(m-1) 1/g_j^2`.

Now

`sum_j g_j=p_m-p_1 <= X/2`.

Cauchy twice, or equivalently the power-mean inequality, gives

`sum_j 1/g_j^2`
` >= (m-1)^3/(sum_j g_j)^2`
` >= 4(m-1)^3/X^2`.

Therefore

`Q_(X,1/2) >= 2(m-1)^3/X^2`.

The prime number theorem yields

`m=pi(X)-pi(X/2)=(1/2+o(1)) X/log X`,

so

`Q_(X,1/2) >= (1/4+o(1)) X/(log X)^3`.

Multiplying by `4 A_X^2` and using `A_X~e^gamma log X` gives the stated certificate lower bound

`4 A_X^2 Q_(X,1/2) >= (e^(2 gamma)+o(1)) X/log X`.

This means only that the simple reciprocal-frequency `l^2` upper bound cannot become a useful joint-limit certificate unless `L^2 log X/X -> infinity`. It is not a lower bound on `V_(X,1/2)(L)`.

## 4. The certificate-heavy modes have vanishing actual energy

The exact Parseval formula makes the distinction explicit. The total actual contribution of the two neighboring signed modes for each adjacent pair is

`V_neigh(X,L)`
` = 2 A_X^2 sum_(j=1)^(m-1)`
`   (p_j p_(j+1))^(-1)`
`   sinc^2((L/2) log(p_(j+1)/p_j))`.

Since `p_j,p_(j+1)>X/2`,

`(p_j p_(j+1))^(-1) <= 4/X^2`,

and `sinc^2<=1`. Therefore, uniformly in the window length,

`V_neigh(X,L) <= 8 A_X^2 (m-1)/X^2`.

Using PNT and Mertens again,

`8 A_X^2 (m-1)/X^2`
` = (4e^(2 gamma)+o(1)) log X/X`
` -> 0`.

The relative contribution after dividing by the squared Haar mean is even smaller:

`V_neigh(X,L)/A_X^2 = O(1/(X log X))`.

Thus the neighboring-prime family has exactly the asymmetry a raw small-divisor visualization can hide: it creates large reciprocal-frequency norms because a few frequencies are tiny, while its squared Fourier coefficient mass tends to zero.

This is the decisive control. Neither divergence of `B_(X,1/2)` from `VIS-077` nor divergence of `Q_(X,1/2)` establishes persistent finite-window energy.

## 5. Prior art and novelty boundary

The harmonic-analysis mechanism is classical. The exact formula above is Parseval for the Bohr/prime-torus Fourier representation already used throughout `VIS-067`--`VIS-076`; no new general Parseval or mean-value theorem is claimed.

S. M. Gonek and J. P. Keating, **Mean values of finite Euler products**, *Journal of the London Mathematical Society* 82:3 (2010), 763--786, DOI `10.1112/jlms/jdq049`, studies mean values of the modulus squared of finite Euler products and the regimes in which the Euler factors behave independently. It is the nearest direct analytic-number-theory boundary for treating mean-square finite-Euler-product behavior as established territory.

The prime number theorem and Mertens' product theorem are used only for the displayed asymptotic scales. The finite neighboring-prime inequalities themselves are elementary and require no unproved prime-gap hypothesis.

The Mathia-specific contribution is therefore only the control diagnosis at the present visual frontier: **the elementary near-resonances that make coefficientwise reciprocal-frequency certificates grow can simultaneously carry vanishing actual `l^2` window energy.** A positive visual claim must measure the sinc-filtered spectral mass itself, or use a direct mean-value theorem for the exact growing observable, rather than promote certificate failure into evidence.

## Boundary and falsification

The exact Parseval identity is for the linear moving-window average of `|P_X(sigma,t)|^2` at finite prime support. The growing-support asymptotic comparison is specialized to `sigma=1/2`.

The vanishing statement concerns only the adjacent-prime difference characters in `(X/2,X]`. It does not show that the full signed spectrum has vanishing energy, nor that other families of near-resonant smooth ratios are negligible.

The `sqrt(X/log X)` scale is a necessary condition only for the displayed reciprocal-frequency `l^2` **certificate** to vanish. It is not asserted to be a true transition scale for the moving-window observable.

Falsify the exact part by producing a failure of the Poisson-product Fourier coefficients, two distinct exponent vectors with the same prime-log frequency, or a mismatch between the long-height mean square and the displayed squared-coefficient sinc sum. Falsify the neighboring-mode estimates by an adjacent prime pair in `(X/2,X]` violating the elementary coefficient/frequency inequalities or by failure of the stated PNT/Mertens asymptotics.

## Research consequence

`VIS-077` showed that the coefficientwise `l^1` resonance certificate becomes expensive at growing support. The present result shows that simply moving to a reciprocal-frequency `l^2` certificate does not fully solve the problem: its coefficient also necessarily grows, although at a softer square-root window scale.

More importantly, the neighboring-prime modes used to prove that growth contribute vanishing actual spectral energy. This closes the tempting route of reading a growing small-divisor norm, or a visually dramatic nearest-neighbor beat family, as evidence of a persistent signed Euler-product window signal.

For `CLUE-zeta-prime-phase-recursive-geometry`, the next admissible signed-support test must control the **full exact sinc-filtered energy**

`A_X^2 sum_(k!=0) w_k^2 sinc^2(L lambda_k/2)`

under a frozen joint law `X=X(L)`, or import a direct growing-cutoff mean-value theorem for the same observable. Anything weaker remains only a proof-certificate statement about the prime-torus null.