# VIS-256 — finite moment cancellation does not beat the sine-kernel cusp

## Claim

Let

`T(q)=min(|q|,1)`

be the classical centered sine-kernel/CUE form-factor increment appearing in the `sinc^2 <-> triangle` identity used in `VIS-142`.

For every integer `n>=1` there is a finite real signed measure `mu_n` supported on `[-1,1]` such that

- `||mu_n||_TV = 2^n`;
- `int x^k dmu_n(x)=0` for every integer `0<=k<=2n-1`;
- `int |x| dmu_n(x)=c_n != 0`.

Consequently, for every `0<b<=1`, the dilation `mu_(n,b)` supported on `[-b,b]` has the same bounded total variation, annihilates the same finite set of ordinary moments, yet

`int T(q) dmu_(n,b)(q) = c_n b`.

Thus **no fixed finite collection of ordinary moment-cancellation constraints, even together with symmetry and zero total mass, can by itself improve the universal low-frequency sine-kernel scale from `O(b)` to `o(b)`**. For every prescribed finite moment order there are bounded-normalization shrinking packets satisfying those cancellations whose response to the cusp remains exactly linear in bandwidth.

This is a negative design control for the asymmetric support-safe route in `CLUE-zeta-montgomery-support-edge-arithmetic-residual.md`. A stronger shrinking-channel suppression must control the non-polynomial cusp itself — for example through a weighted `|q|` condition or another structure not reducible to finitely many polynomial moments — rather than merely adding finitely many vanishing moments to the companion packet.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL SINE-KERNEL IDENTITY + NEGATIVE DESIGN CONTROL + NO-NOVELTY-CLAIM`.

No new CUE theorem, zeta correlation theorem, finite-height transfer theorem, or arithmetic residual is claimed.

## 1. An explicit moment-annihilating packet

Fix `n>=1`. Put

`x_j=sqrt(j/n)`,

`w_j=(-1)^(n-j) binom(n,j)`,

for `j=0,...,n`, and let

`sigma_x = (delta_x+delta_(-x))/2`

for `x>0`, with `sigma_0=delta_0`. Define

`mu_n = sum_(j=0)^n w_j sigma_(x_j)`.

The support points are distinct except for the deliberate `+0=-0` identification, so

`||mu_n||_TV = sum_(j=0)^n |w_j| = 2^n`.

Symmetry gives every odd moment exactly zero. For an even moment of order `2k`,

`int x^(2k) dmu_n(x)`
` = sum_(j=0)^n w_j (j/n)^k`
` = n^(-k) sum_(j=0)^n (-1)^(n-j) binom(n,j) j^k`.

The final sum is the `n`-th forward finite difference of the polynomial `j^k`. It vanishes whenever `k<n`. Hence every even moment through degree `2n-2` vanishes, while symmetry kills every odd moment. Therefore

`int x^m dmu_n(x)=0`, `0<=m<=2n-1`.

In particular the packet has zero total mass and, for arbitrarily large but fixed `n`, arbitrarily many exact polynomial moment cancellations.

## 2. The cusp survives every fixed finite cancellation order

It remains to show that the same packet does not annihilate `|x|`. Define

`c_n = int |x| dmu_n(x)`
`    = sum_(j=0)^n (-1)^(n-j) binom(n,j) sqrt(j/n)`.

The elementary Laplace representation

`sqrt(y) = (1/(2 sqrt(pi))) int_0^infinity (1-exp(-y t)) t^(-3/2) dt`

follows by the change of variables `u=yt` and one integration by parts, using `Gamma(1/2)=sqrt(pi)`.

Substituting this representation into the finite binomial sum and using

`sum_(j=0)^n (-1)^(n-j) binom(n,j) = 0`,

`sum_(j=0)^n (-1)^(n-j) binom(n,j) exp(-j t/n)`
` = (exp(-t/n)-1)^n`
` = (-1)^n (1-exp(-t/n))^n`,

gives

`c_n = ((-1)^(n+1)/(2 sqrt(pi)))`
`      * int_0^infinity (1-exp(-t/n))^n t^(-3/2) dt`.

The integral is finite and strictly positive: near zero its integrand is `O(t^(n-3/2))`, which is integrable for `n>=1`, and at infinity it is `O(t^(-3/2))`. Therefore `c_n` is nonzero for every `n`.

Now let `mu_(n,b)` be the pushforward of `mu_n` by `x -> b x`. Its support is contained in `[-b,b]`, its total variation remains `2^n`, and all moments through degree `2n-1` still vanish. For `0<b<=1`, `T(q)=|q|` throughout that support, so

`int T(q) dmu_(n,b)(q)`
` = b int |x| dmu_n(x)`
` = c_n b`.

This is an exact linear response, not merely a lower-order asymptotic.

For any prescribed finite cancellation degree `d`, choose `n` with `2n-1>=d`. The resulting family has `O_d(1)` total variation as `b->0`, annihilates every ordinary moment through degree `d`, and still has a nonzero `Theta_d(b)` cusp response.

## 3. What this closes in the support-edge redesign

`VIS-142` proved the uniform finite-CUE upper bound

`0 <= Delta_(N,L,M)(q) <= kappa_alpha^2 min(|q|,1)`

under a fixed source-capacity margin, and therefore bounded-normalization companion packets supported in `|q|<=b` have at most `O(b)` centered null amplitude.

A natural attempted escape is to impose zero mass, symmetry, or several vanishing moments on the signed companion packet and hope that those cancellations force an additional power of `b`. The construction above shows that **no such conclusion follows from any fixed finite number of polynomial moment constraints alone**. The classical limiting sine-kernel profile already contains the nonanalytic `|q|` cusp, and bounded-TV packets can annihilate arbitrarily many fixed polynomial moments while retaining a linear cusp pairing.

The obstruction is representation-specific rather than a generic statement about smooth kernels. If the centered null profile were uniformly smooth enough at zero, vanishing moments could remove successive Taylor coefficients. Here the uniform support-edge control inherited from the sine-kernel limit is only Lipschitz at the origin. Polynomial moments do not annihilate the absolute-value singularity.

Accordingly, a claimed `o(b)` or `O(b^r)` improvement for the support-safe companion must use additional information. Examples include a direct bound on `int |q| dnu_b(q)`, a packet architecture tailored to the actual cusp rather than to polynomial moments, a finite-window regime with a quantitatively uniform smoothness scale that remains relevant as the source window grows, or a source-specific arithmetic identity that changes the target quantity being controlled.

## 4. Prior-art and novelty audit

The load-bearing harmonic identity is already audited in `VIS-142`: with the repository Fourier convention,

`int_R sinc(x)^2 exp(2*pi*i*q*x) dx = (1-|q|)_+`,

so the centered sine-kernel increment is `T(q)=min(|q|,1)`. This is the classical Fejer/Bartlett triangle identity and is not novel.

The remaining argument is an elementary finite-difference construction. Binomial finite differences annihilate polynomials below their order, symmetry annihilates odd moments, and the displayed Laplace/Gamma representation proves directly that the same finite difference of `sqrt(y)` is nonzero. No novelty is claimed for these classical ingredients or for the general fact that polynomial moment cancellation need not annihilate a nonsmooth function.

The durable contribution here is only the Mathia-specific design boundary: in the exact support-edge thread, adding any **fixed finite** number of ordinary vanishing moments to a shrinking low-frequency packet is not enough to improve the universal linear cusp scale. No new external theorem is load-bearing, so `SOURCES.md` needs no additional anchor.

## 5. Boundaries and falsification

This finding is a sharpness obstruction for deductions based only on bounded total variation plus finitely many ordinary moments. It does **not** say that every moment-balanced packet has a linear response; special packets can annihilate the cusp as well. It says the listed moment constraints do not force that stronger cancellation.

It also does not give a finite-`N` lower bound for every bounded-source CUE profile in `VIS-142`. At any fixed finite source window the centered profile is smoother at sufficiently tiny `q`. The point is instead uniform: the sine-kernel/CUE limit that supplies the robust `O(b)` envelope already admits bounded-normalization, arbitrarily high fixed-order moment cancellation with a linear cusp response. Therefore a stronger bound uniform across the support-edge scaling regime cannot be justified from those finite moment constraints alone.

The construction keeps `n` fixed while `b->0`; its total variation is `2^n`. If the cancellation order itself grows with the asymptotic parameter, conditioning becomes a separate question. This finding makes no claim about the optimal tradeoff between growing moment order, total variation, support width, and target visibility.

Nothing here controls the zeta-specific arithmetic correction, cross-height covariance, Rudnick-Sarnak remainder for an `L`-dependent test family, or finite-height transfer. Those remain the decisive obstacles of the accepted support-edge clue.

## Research consequence

For the asymmetric near-edge × low-frequency route, do not treat zero total mass, symmetry, or any fixed finite list of vanishing ordinary moments as sufficient evidence that the CUE-centered companion has improved from the `O(b_L)` scale in `VIS-142`.

Any proposed stronger null suppression must state the extra mechanism that kills or bypasses the `|q|` cusp and propagate that mechanism through the same normalization, theorem-error, transfer, noise, and covariance accounting already required by the clue. The original edge-edge dependence problem remains untouched.
