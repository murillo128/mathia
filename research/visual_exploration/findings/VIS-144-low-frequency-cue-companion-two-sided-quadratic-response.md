# VIS-144 — finite-window CUE companions have a two-sided quadratic response and a cancellable second moment

## Claim

Use the exact bounded-arc finite-CUE null and notation of `VIS-142`--`VIS-143`:

`K_(N,L,M)(x)=A_M(x)W_L(x)D_N(x)^2`,

`Delta(q)=integral_(-M)^M K_(N,L,M)(x)[1-cos(2*pi*q*x)]dx`,

with `0<M<=alpha N`, fixed `0<alpha<1`, and

`kappa_alpha=(pi alpha)/sin(pi alpha)`.

Define the finite kernel moments

`mu_2=integral_(-M)^M x^2 K_(N,L,M)(x) dx`,

`mu_4=integral_(-M)^M x^4 K_(N,L,M)(x) dx`.

Then for every real `q`,

`2*pi^2*mu_2*q^2 - (2/3)*pi^4*mu_4*q^4 <= Delta(q) <= 2*pi^2*mu_2*q^2`.

Since `mu_4<=M^2 mu_2`,

`2*pi^2*mu_2*q^2 [1-(pi^2/3)M^2q^2] <= Delta(q) <= 2*pi^2*mu_2*q^2`.

In particular, whenever

`|q|M <= sqrt(3/2)/pi`,

one has the explicit two-sided bound

`pi^2*mu_2*q^2 <= Delta(q) <= 2*pi^2*mu_2*q^2`.

The coefficient `mu_2` is itself nondegenerate. Put

`w_(M,L)=1/[1+(pi*M/(2L))^2]`

and retain `J(u)=u-sin(2*pi*u)/(2*pi)` from `VIS-143`. Then

`[w_(M,L)/(4*pi^2)] J(M/2) <= mu_2 <= [kappa_alpha^2/pi^2] J(M)`.

Consequently, along any family with fixed capacity margin `M/N<=alpha<1`, bounded aspect ratio `M/L<=beta`, and `M->infinity`,

`mu_2=Theta(M)`.

If additionally `|q|M->0`, then

`Delta(q)=Theta(M q^2)`.

Thus the ultra-low-frequency finite-window regime found in `VIS-143` is not merely bounded above by a quadratic scale: each nonzero centered cosine mode has a genuinely quadratic response there, with a coefficient of order `M` under the natural bounded-aspect-ratio regime.

There is also a new exact packet-level distinction. For any finite signed measure `nu_b` supported in `|q|<=b`, put

`B(nu_b)=integral Delta(q) dnu_b(q)`

and `m_2(nu_b)=integral q^2 dnu_b(q)`. Then

`|B(nu_b)-2*pi^2*mu_2*m_2(nu_b)|`
` <= (2/3)*pi^4*mu_4*integral q^4 d|nu_b|(q)`.

Hence a signed companion packet satisfying the exact moment condition

`m_2(nu_b)=0`

cancels the entire universal quadratic CUE-centered mean term. Its remaining null mean is at most

`|B(nu_b)| <= (2/3)*pi^4*mu_4*b^4 ||nu_b||_TV`.

This cancellation is algebraic and support-preserving. Whether a zeta-specific arithmetic term survives the same signed packet is not established and becomes a separate research question.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL TAYLOR/FOURIER BOUND + NEGATIVE/REDESIGN CONTROL + NO-NOVELTY-CLAIM`.

No zeta arithmetic residual, four-level theorem, covariance law, finite-height transfer estimate, or stochastic-noise improvement is claimed.

## 1. Two-sided Taylor control is exact at finite window

For every real `u`,

`u^2/2-u^4/24 <= 1-cos(u) <= u^2/2`.

The upper inequality is standard. For the lower inequality, equivalently

`1-u^2/2+u^4/24-cos(u) >= 0`;

its fourth derivative is `1-cos(u)>=0`, while the function and its first three derivatives vanish at zero, so repeated integration proves the inequality for `u>=0`, and evenness gives all real `u`.

Substitute `u=2*pi*q*x` and integrate against the nonnegative kernel `K_(N,L,M)`. This gives

`Delta(q)`
` <= 2*pi^2 q^2 integral x^2K(x)dx`
` = 2*pi^2 mu_2 q^2`,

and

`Delta(q)`
` >= 2*pi^2 mu_2 q^2-(2/3)pi^4 mu_4 q^4`.

Because `|x|<=M` on the support,

`mu_4<=M^2 mu_2`,

which yields the relative-error form in the claim. If `(pi^2/3)M^2q^2<=1/2`, the lower bound is at least half the quadratic leading term.

This upgrades the one-sided finite-window estimate of `VIS-143` without using an asymptotic sine-kernel replacement.

## 2. The quadratic coefficient is of order the source-window width

The upper bound follows from the capacity-margin domination already proved in `VIS-142`:

`D_N(x)^2 <= kappa_alpha^2 sinc(x)^2`,

while `0<=A_M,W_L<=1`. Therefore

`mu_2`
` <= (kappa_alpha^2/pi^2) integral_(-M)^M sin(pi*x)^2 dx`
` = (kappa_alpha^2/pi^2) J(M)`.

For the lower bound, restrict to `|x|<=M/2`. The explicit cubic tent overlap from `VIS-130` is decreasing on `0<=|x|/M<=1/2` and satisfies

`A_M(x)>=A(1/2)=1/4`.

On the same interval,

`W_L(x)>=w_(M,L)`.

Also, because `|x|<N` under the fixed capacity margin,

`D_N(x)=sinc(x) [(pi*x/N)/sin(pi*x/N)]`

and `|u/sin u|>=1` for `|u|<pi`, so

`D_N(x)^2>=sinc(x)^2`.

Hence

`mu_2`
` >= [w_(M,L)/4] integral_(-M/2)^(M/2) x^2 sinc(x)^2 dx`
` = [w_(M,L)/(4*pi^2)] J(M/2)`.

If `M/L<=beta`, then `w_(M,L)` is bounded below by a positive constant depending only on `beta`. Since `J(M)=M+O(1)` and `J(M/2)=M/2+O(1)`, the coefficient satisfies `mu_2=Theta(M)` uniformly under fixed `alpha,beta`.

Therefore the local response is genuinely `Theta(Mq^2)` whenever the Taylor scale `qM` tends to zero.

## 3. The scalar normalization pressure of VIS-143 is sharp for one mode

Take a single companion mode with `q=b`, `bM->0`, under fixed `alpha` and bounded `M/L`. Then

`Delta(b)=Theta(Mb^2)`.

Accordingly, if a scalar multiplier `lambda_b` is used solely to keep this finite-CUE centered mean contribution of order one, the necessary scale from `VIS-143`,

`lambda_b = Omega(1/(Mb^2))`,

is also sufficient at the level of this one-mode null mean up to constants:

`lambda_b=Theta(1/(Mb^2))` gives an order-one centered CUE response.

This is not a statement about detectability. The same multiplier acts on finite-height transfer error, stochastic fluctuations, covariance, theorem remainder, and any arithmetic term. It only fixes the deterministic null-mean normalization scale.

## 4. Signed packets expose a second-moment cancellation channel

For a finite signed packet `nu_b`, integrate the two-sided Taylor decomposition before taking absolute values:

`B(nu_b)=2*pi^2*mu_2 m_2(nu_b)+R_4`,

with

`|R_4|`
` <= (2/3)pi^4 mu_4 integral q^4 d|nu_b|(q)`.

This separates packet normalization from packet shape. A positive packet cannot cancel its nonnegative second moment unless it is concentrated at zero. A signed packet can.

If `m_2(nu_b)=0`, the quadratic universal CUE term disappears exactly and

`|B(nu_b)| <= (2/3)pi^4 mu_4 b^4 ||nu_b||_TV`.

Using `mu_4<=M^2mu_2=O(M^3)` under the bounded-aspect-ratio regime gives the coarse support-level control

`|B(nu_b)|=O(M^3 b^4 ||nu_b||_TV)`.

This is a **null-side cancellation mechanism**, not evidence of arithmetic sensitivity. The same signed weights may also cancel the desired zeta correction or amplify variance. The only justified conclusion is that the support-safe companion design space is richer than scalar amplification of one positive low-frequency mode: one can impose a moment-null condition that removes the leading finite-window CUE mean while leaving the Fourier support unchanged.

## 5. Stress tests and boundaries

The result is representation-independent once the finite-window kernel from `VIS-130` is fixed. No plotted slope or fitted crossover is used.

The lower coefficient bound retains the exact tent geometry and Montgomery weight. If `M/L` is allowed to diverge, the displayed lower bound can degenerate, so `Theta(M)` is not claimed without an aspect-ratio condition. If `M/N->1`, the upper constant `kappa_alpha` again loses uniformity, exactly as in `VIS-142`--`VIS-143`.

The packet cancellation statement is exact for the deterministic centered mean. It gives no variance reduction. In particular, a signed packet with large positive and negative weights may have small `m_2` but large total variation, so noise and theorem errors can worsen even while the universal mean cancels.

The result also does not show that the arithmetic lower-order term has a different low-frequency moment expansion from CUE. If zeta and the finite-CUE null share the same quadratic coefficient through the relevant accuracy, imposing `m_2=0` could erase both. That is the decisive unresolved question.

## 6. Prior-art and novelty audit

The finite-CUE kernel, tent overlap, capacity-margin comparison, and linear/quadratic upper bounds are already anchored in `VIS-130`, `VIS-142`, and `VIS-143`. The new derivation uses only classical Taylor inequalities for cosine and elementary moment bounds for compactly supported nonnegative kernels.

The fact that a compactly supported even kernel has a quadratic centered Fourier response determined by its second moment, and that signed filters can annihilate prescribed low-order moments, is standard harmonic-analysis/filter-design structure. No general novelty is claimed. No additional source anchor is needed for the elementary theorem recorded here.

The Mathia-specific value is the exact composition with the frozen support-edge finite-CUE null: it turns the `VIS-143` one-sided normalization pressure into a two-sided local scale and identifies an explicit signed-moment cancellation channel that can now be tested for arithmetic selectivity rather than guessed from low-frequency plots.

## Research consequence

The asymmetric restricted-support branch now has two mathematically distinct companion designs.

A one-sign or single-mode ultra-low-frequency companion has deterministic finite-CUE centered mean `Theta(Mb^2)` when `Mb->0`, so keeping that mean macroscopic fixes the scalar normalization scale at `Theta(1/(Mb^2))` before any stochastic or zeta-side accounting.

A signed packet may instead impose `integral q^2 dnu_b(q)=0`, cancelling the universal quadratic CUE mean without changing the support budget. This is worth testing only if the zeta-specific lower-order contribution can be shown to have a nonzero component outside that same quadratic moment functional and if the packet's total variation, variance, transfer error, and four-level/cross-window obligations remain controlled.

No untouched confirmation-zero data are needed for that next test.