# VIS-131 — bounded-tent CUE support-edge rounding is a Poisson-sampled profile with regular effective-size sensitivity

## Claim

Continue the exact bounded-source finite-CUE statistic from `VIS-130`,

`C_(N,L,M)(q)`
` = 1 - integral_(-M)^M A_M(x) W_L(x) D_N(x)^2 exp(2*pi*i*q*x) dx`,

with

`D_N(x)=sin(pi*x)/(N sin(pi*x/N))`,

`W_L(x)=1/(1+(pi*x/L)^2)`,

and the normalized tent overlap `A_M(x)=A(|x|/M)` from `VIS-130`.

Put

`rho_L=N/L`,  `kappa_L=M/L`,  `q=1+v/L`,

and assume a fixed non-wrapping capacity margin

`0 < kappa_L <= kappa_+ < rho_- <= rho_L`

while `v` stays in a fixed compact set. Define the compactly supported even function

`g_kappa(u)`
` = A(|u|/kappa)/(1+(pi*u)^2)` for `|u|<=kappa`,
` = 0` otherwise,

and use the Fourier convention

`hat g_kappa(t)=integral_R g_kappa(u) exp(2*pi*i*t*u) du`.

Then the support-edge deficit has the exact finite-`N` representation

`1-C_(N,L,M)(1+v/L)`
` = [1/(rho_L^2 L)]`
`   { sum_(j=1)^N j hat g_(kappa_L)(v+j/rho_L)`
`     + sum_(j=N+1)^(2N-1) (2N-j) hat g_(kappa_L)(v+j/rho_L) }`.

Because the tent overlap is compactly supported and `C^2` with piecewise-smooth third derivative, `hat g_kappa(t)=O((1+|t|)^-4)` uniformly under the fixed capacity margin. Hence

`C_(N,L,M)(1+v/L)`
` = 1 - Phi_(rho_L,kappa_L)(v)/L + O(L^-3)`,

where

`Phi_(rho,kappa)(v)`
` = rho^-2 sum_(j>=1) j hat g_kappa(v+j/rho)`.

The leading profile satisfies the exact alias-free identity

`Phi_(rho,kappa)(-v) - Phi_(rho,kappa)(v) = v`

whenever `kappa<rho`. Therefore, relative to the ideal infinite-CUE ramp/plateau edge,

`R_infty(1+v/L)=1+min(v,0)/L`,

the bounded-tent finite-CUE rounding is symmetric:

`C_(N,L,M)(1+v/L)`
` = R_infty(1+v/L) - Phi_(rho_L,kappa_L)(|v|)/L + O(L^-3)`.

Most importantly for the accepted support-edge clue, `Phi_(rho,kappa)(v)` is a regular `C^1` function of `rho` as long as the capacity margin remains nonzero. A perturbation `delta rho` of the effective-size ratio therefore moves this bounded-source mean null by only

`O(delta rho/L)`.

Thus an unresolved `delta rho=O(1/log L)` transfer error produces `O(1/(L log L))`, not a generic `O(1/L)` displacement. Integerization `delta N=O(1)` contributes only `O(L^-2)` at the mean level. The logarithmically enhanced `rho`-sensitivity found in the full-circle real-time statistic `VIS-123`/`VIS-129` is therefore **not inherited by the correctly replaced bounded-tent source window**.

**Evidence/status:** `EXACT-DERIVED + ASYMPTOTIC CONTROL + NEGATIVE NUISANCE RESULT + CLASSICAL FOURIER/CUE INGREDIENTS + NO-NOVELTY-CLAIM`.

No covariance formula, arithmetic residual, effective-size transfer theorem, new CUE theorem, or implication toward RH is claimed.

## 1. Fejer expansion converts the bounded arc into an exact sampled Fourier sum

The normalized CUE kernel has the finite Fourier expansion

`D_N(x)^2`
` = (1/N) sum_(m=-(N-1))^(N-1) (1-|m|/N) exp(2*pi*i*m*x/N)`.

This is the ordinary Fejer-kernel identity in mean-spacing coordinates. Since

`A_M(Lu) W_L(Lu)=g_(kappa_L)(u)`,

substitution into the exact `VIS-130` integral and the change of variable `x=Lu` give

`1-C`
` = (L/N) sum_(|m|<N) (1-|m|/N)`
`     hat g_(kappa_L)(L(1+v/L+m/N))`.

Write `m=-N+j`. Then

`L(1+v/L+m/N)=v+j/rho_L`.

For `1<=j<=N`, the Fejer coefficient is `j/N`; for `N<j<2N`, it is `(2N-j)/N`. This yields the exact finite sum in the claim.

The representation makes the edge mechanism transparent. Near `q=1`, only Fourier modes lying a bounded number of lattice steps from the terminal CUE mode `m=-N` contribute at order `1/L`. The bounded source taper turns those edge modes into samples of one fixed smooth Fourier transform rather than the slowly decaying full-circle coordinate-overlap transform.

## 2. The far-side circle contribution is lower order

The compact cubic tent overlap satisfies `A(1)=A'(1)=A''(1)=0`, its two polynomial pieces match through second derivative, and its even extension has zero first derivative at the origin. Multiplication by the smooth Montgomery factor preserves this regularity. Consequently `g_kappa` is compactly supported, globally `C^2`, piecewise smooth, and has a third derivative of bounded variation. Repeated integration by parts gives

`hat g_kappa(t)=O((1+|t|)^-4)`.

In the second finite sum, `j>N`, so `v+j/rho_L=Theta(L)` uniformly. Its total contribution is `O(L^-3)`. Extending the first sum from `j<=N` to `j<infinity` also costs only `O(L^-3)`, because

`sum_(j>N) j |hat g(v+j/rho_L)| = O(N^-2)`.

This proves the stated leading profile without a fitted correction coefficient and without inspecting zeta zeros.

## 3. Capacity makes the edge rounding alias-free

The identity

`Phi(-v)-Phi(v)=v`

is not a numerical symmetry. It follows from Poisson summation and the same strict single-arc capacity condition required by `VIS-129`--`VIS-130`.

Since `supp(g_kappa) subset [-kappa,kappa]` and `kappa<rho`, periodization on the lattice `rho Z` sees only the central copy. Poisson summation therefore gives

`sum_(j in Z) hat g_kappa(v+j/rho) = rho g_kappa(0)=rho`.

Applying the same formula to the derivative, or equivalently to `t hat g_kappa(t)`, gives

`sum_(j in Z) (v+j/rho) hat g_kappa(v+j/rho)=0`,

because `g_kappa` is even and `g_kappa'(0)=0`. Hence

`sum_(j in Z) j hat g_kappa(v+j/rho) = -rho^2 v`.

Pairing positive and negative `j` and using evenness of `hat g_kappa` yields exactly

`rho^2[Phi(v)-Phi(-v)] = -rho^2 v`.

Thus the finite source does not shift the ramp discontinuity asymmetrically: it rounds the two sides by the same leading profile after the deterministic ideal-ramp term is removed.

This also supplies a strong implementation check. A numerical quadrature or Monte Carlo mean for the frozen bounded-tent CUE null that violates the reflected edge relation beyond finite-`L` error is not evaluating the same source-window statistic.

## 4. Effective-size uncertainty loses the full-circle logarithmic amplification

Under a fixed capacity margin, the `O(t^-4)` decay is also sufficient to differentiate the defining series for `Phi` with respect to `rho`. Explicitly,

`partial_rho Phi_(rho,kappa)(v)`
` = -2 rho^-3 sum_(j>=1) j hat g_kappa(v+j/rho)`
`   - rho^-4 sum_(j>=1) j^2 hat g_kappa'(v+j/rho)`,

with absolute convergence on compact parameter sets away from `rho=kappa`.

Therefore the mean null responds Lipschitz-continuously to the effective-size ratio. If `rho` is replaced by `rho+delta rho` while the physical taper is frozen,

`Delta C = O(delta rho/L)`.

This materially changes the calibration picture from `VIS-129`. For the full-circle noninteger-time statistic, the rectangular coordinate overlap produces a log-enhanced support-edge term and a `delta rho=Theta(1/log L)` ambiguity can contaminate the `1/L` scale. The bounded tent removes that slow rectangular tail. In the correctly windowed statistic, the same ratio uncertainty is one logarithm smaller than `1/L` at the mean level.

This does not prove that the classical pair-correlation effective-size rule is exact for the bounded observable. It shows only that **asymptotically vanishing ratio uncertainty is no longer, by itself, a first-order mean-identifiability obstruction** for a fixed compact source taper.

## Prior-art and novelty assessment

The Fejer-kernel expansion, Poisson summation, Fourier scaling, and decay of Fourier transforms of compact piecewise-smooth functions are classical harmonic analysis. NIST DLMF §1.8(iv), “Poisson's Summation Formula”, is an authoritative reference for the summation identity used above: `https://dlmf.nist.gov/1.8.iv`.

The finite-`N` CUE determinantal kernel and its mean-spacing scaling are standard random-matrix theory; `VIS-130` already anchors them to Peter J. Forrester and Bo-Jian Shen, **Finite size corrections in the bulk for circular beta ensembles**, *Forum of Mathematics, Sigma* 14 (2026), e105, DOI `10.1017/fms.2026.10240`.

Sohail, Youyi Huang, and Lu Wei, **Higher-order spectral form factors of circular unitary ensemble**, *Journal of Statistical Physics* 193 (2026), article 20, DOI `10.1007/s10955-026-03572-8`, derive exact all-real-time full-circle CUE spectral form factors and the logarithmic finite-size behavior that supplied the prior full-circle control in `VIS-123`.

No novelty is claimed for any of those ingredients or for Poisson summation applied abstractly. The Mathia-specific contribution is the control calculation for the exact bounded source statistic already selected by the active visual thread: the Fejer/Poisson representation exposes its leading support-edge profile, proves the reflected rounding identity under the single-arc capacity condition, and shows that the earlier full-circle logarithmic effective-size sensitivity does not survive source-window replacement.

## Boundary and falsification

The result is a **mean-null statement**. It does not derive the joint covariance of several edge coordinates, stochastic finite-height unfolding error, the exact zeta-to-CUE effective-size transfer, or any arithmetic lower-order amplitude. Those remain necessary before source confirmation.

The fixed capacity margin is load-bearing. If `kappa` approaches `rho`, additional Poisson aliases can enter and the simple reflected identity need not survive unchanged. Likewise, a hard or insufficiently smooth source window can restore slower Fourier tails and different sensitivity scaling.

The `O(L^-3)` remainder is for the exact ratio parameters `rho_L=N/L`, `kappa_L=M/L` in the displayed profile, with `v` in a compact set and a uniform positive capacity margin. Replacing those finite-`L` ratios by limiting constants introduces the ordinary error implied by their convergence rate.

## Research consequence

The accepted Montgomery support-edge clue no longer needs to treat `delta rho=Theta(1/log L)` as a same-order **mean** nuisance for the bounded tent. The next unresolved gate is the joint covariance and finite-height transfer for a frozen collection of edge coordinates under this exact statistic.

Before any untouched zeta confirmation, derive that covariance and propagate the remaining source-side uncertainties through it. Only then should an independently predicted arithmetic lower-order amplitude be compared with a residual. The current result narrows the control stack; it does not establish that such a residual exists.
