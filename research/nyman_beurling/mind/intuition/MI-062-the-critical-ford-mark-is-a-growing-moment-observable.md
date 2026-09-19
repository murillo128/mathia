# MI-062 — The critical Ford mark is a growing-resolution observable whose classical form is a microlocal Landau–Gonek remainder

**Evidence level:** exact positive reduction plus matched-control and classical-explicit-formula boundary from [NB-234](../../findings/NB-234-growing-depth-moment-hierarchy-reconstructs-critical-ford-mark.md) and [NB-235](../../findings/NB-235-critical-ford-transition-reduces-to-microlocal-landau-gonek-remainder.md), building on NB-230--NB-233.

NB-234 shows that on every fixed critical layer the residue can be reconstructed from profiled depth--phase moments with an order `K(Q)` that grows slowly with source capacity, while every predetermined fixed `K` remains blind in a matched spectral control. The nonlinear exponential depth mark is therefore not a fixed-moment statistic.

NB-235 identifies what that growing hierarchy is approximating in classical zeta language. With `x=e^X` and `s_X=sigma_X+it`, the exact carrier satisfies `e^(iXv_rho)=x^(rho-s_X)`, and the critical residue is, up to `o(1)`,

`x^(-s_X) sum_{|X(1-beta)-log J|<=C} m(rho) x^rho F(H(gamma-t))`.

This is a microscopic Landau zero sum with an additional horizontal-depth cutoff. The shell profile has zero total integral, so the ordinary Landau--Gonek prime-power diagonal disappears up to a negligible endpoint tail. What survives is a microlocal remainder coefficient, not a missing main term.

The nearest classical global theorem does not yet control it. Stieltjes smoothing of the cumulative Landau--Gonek formula pays the total variation of `F(H(.-t))`, which is independent of `H`; the generic cumulative remainder therefore gives only an `O(Q)` normalized guarantee at the Ford scale. Narrowing the window does not automatically buy the `o(1)` needed by the destination.

The reusable lesson is that **growing-resolution source information and microlocal explicit-formula cancellation are two representations of the same missing object here**. The moment hierarchy is a sufficient surrogate, but the sharper theorem target is direct control of the horizontally marked local remainder or an equivalent zeta-specific identity that couples depth to ordinate phase before absolute-value estimates erase cancellation.

**Boundary.** NB-234 does not prove that zeta supplies the growing moments, and NB-235 does not prove the microlocal remainder is large or small. Its `O(Q)` statement is only the guarantee inherited from global cumulative control after black-box smoothing, and the ordinary Landau--Gonek formula does not include the horizontal cutoff. No Nyman--Beurling distance bound or RH consequence follows without a separate source theorem and destination bridge.