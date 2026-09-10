# VIS-149 — the moment-null packet reduces common source-transfer error to a fourth-moment gate

## Claim

Let `E` be an integrable signed source-coordinate error supported on `[-M,M]` with finite sixth absolute moment, and define the same centered-cosine transfer used by `VIS-145`--`VIS-148`,

`Delta_E(q)=integral E(x)[1-cos(2*pi*q*x)]dx`.

Let `nu_b` be a finite signed packet supported on `[-b,b]` with

`m_2(nu_b)=integral q^2 dnu_b(q)=0`,

and `m_4(nu_b) != 0`. Then Taylor's theorem gives the exact packet-level decomposition

`integral Delta_E(q)dnu_b(q)`
` = -(2/3) pi^4 mu_4(E) m_4(nu_b) + R_6(E,nu_b)`,

where

`mu_4(E)=integral x^4 E(x)dx`,
`M_6(E)=integral |x|^6 |E(x)|dx`,

and

`|R_6(E,nu_b)| <= (4/45) pi^6 M_6(E) b^6 ||nu_b||_TV`.

Consequently, when the retained main source carrier `H^main` has

`A_4=-(2/3)pi^4 mu_4(H^main)`,

the common source-transfer error can be compared to the quartic packet signal through the dimensionless packet condition number

`kappa_b = b^4 ||nu_b||_TV / |m_4(nu_b)| >= 1`.

Indeed,

`|integral Delta_E dnu_b| / |A_4 m_4(nu_b)|`
` <= |mu_4(E)|/|mu_4(H^main)|`
`    + (2*pi^2/15) kappa_b [M_6(E)b^2/|mu_4(H^main)|]`.

Thus, for a bounded-condition packet family (`kappa_b=O(1)`), a sufficient deterministic source-transfer gate is

`|mu_4(E_L)|/|mu_4(H_L^main)| -> 0`

and

`M_6(E_L)b_L^2/|mu_4(H_L^main)| -> 0`.

This is strictly more representation-adapted than demanding four or five raw vanishing moments of `E_L`. In this observable, the zeroth source moment cancels inside `1-cos`, odd source moments never appear because the kernel is even, and the packet condition `m_2(nu_b)=0` cancels the complete quadratic source response. The first source-error moment that survives the **already frozen packet architecture** is therefore `mu_4(E)`.

A fourth-primitive certificate from `VIS-148` remains a valid sufficient route, but it imposes cancellations that the packeted centered-cosine observable does not itself need. Likewise, a fifth primitive is sufficient to annihilate `mu_4(E)`, but direct control or cancellation of `mu_4(E)` plus the sixth absolute moment can provide the same packet-level order without proving all lower raw moments vanish.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL TAYLOR/MOMENT CALCULUS + REPRESENTATION-QUOTIENT + SOURCE-TRANSFER GATE + NO-NOVELTY-CLAIM`.

No claim is made that the actual finite-height zeta transfer error satisfies either displayed asymptotic gate, that `mu_4(H_L^main)` is nonzero, that `M_6(E_L)` has favorable growth on the `M_L=Theta(L)` source window, or that a Rudnick--Sarnak-safe packet family has yet passed the remaining theorem and covariance requirements.

## 1. The packet itself already performs part of the source cancellation

For real `u`, Taylor's theorem gives

`1-cos u = u^2/2 - u^4/24 + r_6(u)`

with

`|r_6(u)| <= |u|^6/720`.

Substituting `u=2*pi*q*x` and integrating against `E` gives

`Delta_E(q)`
` = 2*pi^2 mu_2(E) q^2`
`   -(2/3)pi^4 mu_4(E) q^4`
`   + r_E(q)`,

where

`|r_E(q)| <= (4/45)pi^6 M_6(E)|q|^6`.

Now integrate over `nu_b`. The complete quadratic term vanishes because `m_2(nu_b)=0`, regardless of `mu_2(E)`. This is exactly the same universal quadratic cancellation already established for ordinary source corrections in `VIS-145` and quantified in `VIS-146`; it applies equally to an error represented in the same source-coordinate channel.

The remaining quartic term is proportional only to `mu_4(E)m_4(nu_b)`. The remainder bound follows from `|q|<=b` and total variation.

This distinguishes two different error representations that should not be conflated. A generic already-transformed per-mode error `e_b(q)` known only through `||e_b||_infinity` still faces the minimax gate of `VIS-146` and gains nothing from unproved source structure. But when the error is genuinely represented **before the cosine transform** by a signed source kernel `E(x)`, the frozen packet algebra supplies additional exact cancellation that must be used before asking for stronger source hypotheses.

## 2. The packet condition number isolates the real sixth-moment cost

The quartic signal contributed by `H^main` after packet integration is

`A_4 m_4(nu_b)`
` = -(2/3)pi^4 mu_4(H^main)m_4(nu_b)`.

The quartic part of the error has the same packet factor `m_4(nu_b)`, so its relative size is exactly

`|mu_4(E)|/|mu_4(H^main)|`.

For the sixth-order remainder, divide the Taylor bound by the quartic signal. Since

`kappa_b=b^4||nu_b||_TV/|m_4(nu_b)|`,

one obtains

`|R_6|/|A_4m_4|`
` <= (2*pi^2/15) kappa_b M_6(E)b^2/|mu_4(H^main)|`.

`VIS-146` proves `kappa_b>=1`, and its fixed two-scale construction shows that `kappa_b=O(1)` is attainable for a bounded-complexity quartic packet. Therefore the `b^2` gain in the sixth-order remainder is genuine for such a packet family; it is not erased merely by the unavoidable `b^-4` total-variation normalization.

This does not make the growing source window harmless. If `M_6(E_L)` grows too quickly with `L`, the second gate can still fail. The result only identifies the correct weighted quantity after all algebraic cancellations already present in the observable have been applied.

## 3. Observable-side cancellation is weaker than a repeated-primitive certificate

`VIS-148` gives an important general-purpose sufficient condition: a `k`-fold primitive with zero endpoint traces implies the low-frequency bound `Delta_E(q)=O(q^k||G_k||_1)` and is equivalent, on compact support, to the vanishing of all raw moments below degree `k`.

For the present packeted centered-cosine observable, that hierarchy is stronger than necessary.

First, `1-cos(2*pi*q*x)` is even in `x`, so the odd part of `E` is annihilated exactly. Second, the zeroth Taylor coefficient is absent because `1-cos(0)=0`. Third, the remaining quadratic coefficient is annihilated after packet integration by `m_2(nu_b)=0`. Hence a four-primitive certificate, which also requires zeroth and odd-moment cancellations, should not be treated as the minimal admission condition for the current clue.

At quartic order the adapted requirement is instead quantitative: the transfer-error fourth moment must be negligible relative to the main-carrier fourth moment. If one can establish `mu_4(E)=0` exactly, then the source error begins at sixth order after packet integration and the remaining deterministic question is the weighted sixth-moment gate above. No vanishing `mu_0`, `mu_1`, `mu_2`, or `mu_3` is needed for that packet-level conclusion.

Primitive bounds remain valuable when they are what the finite-height source naturally supplies, when they give stronger control than absolute sixth moments on the growing window, or when one needs a pointwise-in-`q` transfer estimate before packet integration. The correction here is only to avoid making them a necessary condition when the observable has already quotiented several directions itself.

## 4. Stress tests and boundaries

No symmetry of `E` is assumed. The cosine kernel automatically replaces `E` by its even part, so odd source structure cannot rescue or spoil the displayed packet mean.

The result also does not infer smallness from formal moment cancellation. The absolute sixth moment can scale badly on `M_L=Theta(L)`, and `VIS-147` already shows why fixed-spacing asymptotics do not control growing-window weighted moments. A source theorem must still provide the required weighted uniformity, cancellation, or an alternative exact oscillatory estimate.

The packet condition `m_2=0` must be exact in the same frozen coordinate. A calibration or numerical construction that only approximately cancels `m_2` leaves a residual quadratic term and must propagate that error explicitly. Likewise, if the theorem/transfer uncertainty is supplied only after the source transform as a generic `L^infinity` envelope, it cannot be retroactively assigned a source kernel merely to claim the cancellations above.

Nothing here addresses stochastic variance or four-level covariance. It is a deterministic mean/error reduction only.

## 5. Prior-art and novelty audit

The cosine Taylor expansion, the fact that an even kernel annihilates odd source components, moment cancellation by a signed measure, and Taylor remainder bounds by absolute moments are classical harmonic-analysis/filter-calculus facts. No general theorem novelty is claimed.

`VIS-145` and `VIS-146` already establish the packet-side universal quadratic cancellation and quartic Taylor channel for finite-window source corrections. `VIS-148` establishes a different sufficient source-transfer mechanism through repeated primitives. The additional Mathia-specific point here is the representation audit obtained by composing those two pieces: an error that lives in the **same pre-transform source coordinate** as the main carrier must first be passed through the already frozen `m_2=0` packet before deciding which source cancellations are actually required. That composition reduces the deterministic source test to the fourth-moment ratio plus a weighted sixth-moment remainder, rather than a blanket requirement for four or more vanishing raw moments.

## Research consequence

Revise the accepted moment-cancelled companion clue so that the next finite-height source audit tests the weakest representation-faithful gate first.

After effective-CUE size/scale calibration, decompose the bounded-window source as `H_L=H_L^main+E_L`. If the source representation is justified strongly enough to pass `E_L` through the same centered-cosine transform, measure or bound `mu_4(E_L)` and `M_6(E_L)` directly. For a bounded-condition quartic packet, compare

`|mu_4(E_L)|/|mu_4(H_L^main)|`

and

`M_6(E_L)b_L^2/|mu_4(H_L^main)|`

to zero. Only if those weighted moment controls are unavailable or too weak should the route escalate to repeated primitives or another stronger oscillatory certificate.

If even this weaker transform-adapted gate cannot be obtained from the actual finite-height source on the growing window, the quartic support-edge companion remains blocked at the source-information boundary.