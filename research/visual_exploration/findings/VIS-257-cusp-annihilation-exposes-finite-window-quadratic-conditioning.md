# VIS-257 — exact cusp annihilation exposes an optimal quadratic conditioning floor

## Claim

Let `0<b<=1` and let `nu` be any finite real signed measure supported on `[-b,b]` satisfying

`int dnu(q)=0`

and the cusp-adapted cancellation condition

`int |q| dnu(q)=0`.

Write

`m_2(nu)=int q^2 dnu(q)`.

Then the sharp inequality

`|m_2(nu)| <= (b^2/8) ||nu||_TV`

holds. The constant `1/8` is optimal.

An extremizing symmetric packet is

`nu_b^* = delta_0 - 2 sigma_(b/2) + sigma_b`,

where `sigma_x=(delta_x+delta_(-x))/2`. It satisfies

`||nu_b^*||_TV=4`,

`int dnu_b^*=0`,

`int |q| dnu_b^*=0`,

and

`m_2(nu_b^*)=b^2/2`.

Consequently, among all cusp-annihilating packets normalized by `|m_2|=1`, the minimum possible total variation is exactly

`8/b^2`,

attained by `(2/b^2)nu_b^*` up to overall sign.

Because the limiting sine-kernel/CUE support-edge profile from `VIS-256` is `T(q)=min(|q|,1)=|q|` on `[-b,b]`, this packet kills the limiting cusp **exactly** while retaining a nonzero quadratic channel. The price is unavoidable: keeping that quadratic channel at order one requires `Theta(b^-2)` total variation.

For the actual finite-window CUE profile of `VIS-144`, cusp cancellation does not remove the ultra-low-frequency null. If

`Delta(q)=2*pi^2*mu_2 q^2 + R_4(q)`

with

`|R_4(q)| <= (2/3)pi^4 mu_4 q^4`,

then

`int Delta(q)dnu_b^*(q) = pi^2 mu_2 b^2 + E_b`

with

`|E_b| <= (3/4)pi^4 mu_4 b^4`.

Hence whenever `bM->0` in the finite-window regime of `VIS-144`, where `mu_4<=M^2 mu_2`,

`int Delta dnu_b^* = pi^2 mu_2 b^2 [1+o(1)]`.

So an exact cusp-adapted packet exists, but it exposes rather than removes the finite-window quadratic floor. Adding `m_2=0` to remove that floor returns to the universal smooth-kernel obstruction of `VIS-145`: the same condition also annihilates every source correction represented through the same quadratic centered-cosine channel.

**Evidence/status:** `EXACT-DERIVED + SHARP CONDITIONING BOUND + NEGATIVE/REDESIGN CONTROL + NO-NOVELTY-CLAIM`.

No zeta arithmetic residual, Rudnick--Sarnak uniformity theorem, cross-height covariance law, or RH implication is claimed.

## 1. The sharp `1/8` inequality is elementary

The two cancellation constraints allow subtraction of both a constant and the absolute-value cusp. For `|q|<=b`, put

`F_b(q)=q^2-b|q|+b^2/8`.

Writing `t=|q|/b` gives

`F_b(q)/b^2 = t^2-t+1/8 = (t-1/2)^2-1/8`.

For `0<=t<=1`, this lies in `[-1/8,1/8]`. Therefore

`||F_b||_infinity = b^2/8`.

Since `nu` annihilates both `1` and `|q|`,

`m_2(nu)`
` = int [q^2-b|q|+b^2/8] dnu(q)`
` = int F_b(q)dnu(q)`.

Total variation immediately yields

`|m_2(nu)| <= ||F_b||_infinity ||nu||_TV`
`             = (b^2/8)||nu||_TV`.

No symmetry, positivity, density, or atomicity assumption on `nu` is used.

This is the concrete degree-one Chebyshev/minimax geometry behind the bound: `b|q|-b^2/8` is a best uniform approximation to `q^2` from the span of `1` and `|q|` on `[-b,b]`. The proof above is self-contained, so no approximation-theory theorem is load-bearing.

## 2. A three-radius packet attains equality

For

`nu_b^*=delta_0-2sigma_(b/2)+sigma_b`,

the three support radii are exactly the alternation points of `F_b`: `0`, `b/2`, and `b`.

The mass is

`1-2+1=0`.

The cusp moment is

`0-2(b/2)+b=0`.

The second moment is

`0-2(b^2/4)+b^2=b^2/2`.

The total variation is

`1+2+1=4`.

Thus

`m_2(nu_b^*)/||nu_b^*||_TV = b^2/8`,

so the bound is sharp. Rescaling by `2/b^2` gives a packet with `m_2=1` and total variation `8/b^2`; the inequality proves that no other packet satisfying the same cusp and mass cancellations can do better.

This exact optimum matters because scalar normalization cannot hide conditioning. Any theorem remainder, transfer error, or stochastic error controlled only against packet total variation inherits at least the `b^-2` pressure if an order-one quadratic carrier is to survive exact cusp cancellation.

## 3. The limiting cusp is killed exactly

`VIS-256` isolates the limiting support-edge obstruction

`T(q)=min(|q|,1)`.

On the present support `|q|<=b<=1`, this is simply `|q|`. Therefore

`int T(q)dnu_b^*(q)=0`

for every `b`, not merely asymptotically.

This shows that the negative statement in `VIS-256` is sharp in the complementary direction. Finitely many ordinary polynomial moments do not *force* cusp cancellation, but one direct non-polynomial moment condition does. The issue is no longer existence of a cusp-adapted packet; it is whether the remaining source-sensitive channel survives the conditioning and the finite-window null.

For a generic even smooth response

`G(q)=G(0)+a_2 q^2+r(q)`

with `|r(q)|<=Cq^4` on `[-b,b]`, the same packet gives

`int G dnu_b^* = (a_2/2)b^2 + O(Cb^4)`.

After the optimal normalization `(2/b^2)nu_b^*`, the quadratic coefficient is retained at order one while the remainder is `O(Cb^2)`, but the packet total variation is exactly `8/b^2`.

## 4. Finite-window CUE reappears at quadratic order

The exact finite-window null does not have the limiting cusp at sufficiently small frequency. `VIS-144` gives

`Delta(q)=2*pi^2 mu_2 q^2+R_4(q)`,

`|R_4(q)| <= (2/3)pi^4 mu_4 q^4`.

For the extremal cusp-annihilating packet,

`m_2(nu_b^*)=b^2/2`.

Also

`int q^4 d|nu_b^*|(q)`
` = 2(b/2)^4+b^4`
` = (9/8)b^4`.

Therefore

`int Delta dnu_b^*`
` = pi^2 mu_2 b^2 + E_b`,

with

`|E_b|`
` <= (2/3)pi^4 mu_4 (9/8)b^4`
` = (3/4)pi^4 mu_4 b^4`.

Since `VIS-144` also gives `mu_4<=M^2mu_2`, the relative remainder is at most

`(3/4)pi^2 M^2b^2`.

Thus in the ultra-low-frequency regime `Mb->0`,

`int Delta dnu_b^* ~ pi^2 mu_2 b^2`.

The limiting `|q|` cusp has disappeared exactly, but the finite-window CUE quadratic mode survives with a sharp nonzero packet moment. This is not a contradiction: the cusp arises only after a nonuniform growing-window limit, whereas every fixed finite source window has an analytic centered Fourier response near zero.

## 5. Consequence for the support-edge redesign

The asymmetric support-safe branch now has a three-way design boundary.

If the packet does not cancel `|q|`, the robust limiting `O(b)` cusp envelope of `VIS-142`--`VIS-256` remains.

If the packet cancels `|q|` but retains a quadratic channel, the cusp can be removed exactly, but an order-one quadratic carrier requires at least `8/b^2` total variation, and the finite-window CUE null itself survives at quadratic order. Any claimed arithmetic gain must therefore calibrate/subtract that finite-window coefficient with error `o(b^2)` before optimal quadratic normalization, or otherwise prove a source-specific quadratic contrast not already absorbed by the null calibration.

If the packet additionally imposes `m_2=0` to remove the finite-window quadratic CUE term, `VIS-145` shows that every smooth source correction entering through the same centered finite-window cosine transform loses its quadratic term as well. The search then moves to quartic-or-higher structure and the stronger conditioning/error gates already developed in `VIS-146`--`VIS-149`.

So cusp adaptation is a real mathematical escape from the specific `VIS-256` obstruction, but **not a free support-edge escape**. It trades the limiting linear cusp for a sharp quadratic conditioning floor and exposes the finite-window calibration problem that was hidden by the limiting picture.

## 6. Prior-art and novelty audit

The approximation geometry behind the sharp constant is classical. A bounded search of standard approximation-theory terminology identifies the result as the elementary degree-one Chebyshev/minimax approximation of `x^2` on `[0,1]`, whose alternating error has magnitude `1/8`. The signed extremizer is the corresponding three-point annihilating measure. These are standard ingredients, and no general approximation-theory novelty is claimed.

The proof here does not rely on an external theorem: the exact residual `q^2-b|q|+b^2/8` and the extremizing packet verify the bound and sharpness directly. `VIS-142`, `VIS-144`, `VIS-145`, and `VIS-256` already contain the line-specific sine-kernel and finite-window Fourier context, so no new external source is load-bearing and `SOURCES.md` does not need an additional anchor.

The durable Mathia-specific contribution is the composed design law: **exactly killing the limiting support-edge cusp while retaining a quadratic source channel has optimal total-variation cost `8/b^2`, and the same packet leaves the actual finite-window CUE quadratic response asymptotically nonzero when `Mb->0`**.

## 7. Boundaries and falsification

The sharp total-variation bound concerns only packets satisfying zero mass and exact cusp cancellation. A different observable may avoid this packet architecture entirely.

The result does not say that every cusp-annihilating packet has nonzero `m_2`; some also satisfy `m_2=0`. It says that retaining a prescribed quadratic moment under cusp cancellation has the stated optimal conditioning cost.

The finite-window conclusion uses the `VIS-144` Taylor regime. If `Mb` is not small, its relative quadratic approximation need not be accurate and the robust support-edge bounds should be used instead.

The `8/b^2` lower bound is a total-variation statement. A stronger norm, variance functional, structured theorem remainder, orthogonality relation, or source-specific cancellation can impose additional costs or occasionally control errors more efficiently than raw total variation. Such structure must be proved in the exact destination observable; it is not supplied here.

Nothing here derives a zeta-specific arithmetic coefficient, controls the four-level cross-height functional, proves a uniform Rudnick--Sarnak remainder for an `L`-dependent family, or permits inspection of untouched confirmation-zero data.

## Research consequence

The accepted support-edge clue should no longer treat cusp adaptation as an unspecified possibility. There is an explicit sharp packet that annihilates the limiting cusp, and its cost is exactly understood at quadratic order.

A viable cusp-adapted redesign must now decide which side of the finite-window fork it uses: retain `m_2` and prove a source-specific quadratic contribution that survives an `o(b^2)` null/transfer calibration under the unavoidable `b^-2` conditioning, or impose `m_2=0` and accept the quartic-or-higher source gate of `VIS-145`--`VIS-149`. The original edge-edge four-level dependence problem remains unchanged.