# MI-011 — Exact heat-trace identification can be arbitrarily local while transition transport remains superexponentially unstable

**Evidence level:** exact state-identification and transition-conditioning boundaries through XF-145

## Core intuition

The periodic polynomial state is algebraically easy to identify compared with the de Bruijn--Newman transition parameter. One off-circle trace, two nearby real traces, or even one arbitrarily short moving real scan can determine every coefficient exactly at fixed degree. This does not imply stable transport to `Lambda_per`.

The decisive distinction is now quantitative: **state identifiability has essentially zero geometric threshold, while transition conditioning has a source-dependent time/scale threshold**. Central matched packets can hide an order-one transition shift superexponentially even from the complete root-spacing real observation tube over short heat windows.

## Strongest justified principle

XF-130 gives exact one-channel periodic reconstruction. XF-131--XF-140 progressively show that zero-delay exterior data and even full degree-order spatial jets can be exponentially transition-blind. XF-141 constructs maximal central packets with exact transition-time separation, and XF-142 proves that instantaneous time derivatives add no independent axis because the gauged local trace satisfies the ordinary heat equation.

XF-143 shows that two real heat histories separated by only half a mean root spacing recover every Vieta coefficient for an arbitrary degree-`N` state; the reflected-pair inverse costs `O(N)`. XF-144 lowers the exact interface further: a single real probe moving at any nonzero speed makes all heat exponents distinct, so arbitrarily small total travel is injective. The elementary reflected-pair condition number is at least `Omega(L/D)` for travel `D`.

XF-145 then restores the target distinction. For the transition-sharp central packet, the complete real tube `|x|<=CL/N`, `0<=s<=S_N` remains `e^{-omega(N)}`-close whenever `NaS_N->0`, despite an order-one difference in `Lambda_per`. For `S_N<=A/(aN^{1+epsilon})`, the inverse transition condition number is at least `exp(gamma_epsilon N log N-O(N))`. Restricting to any moving scan cannot improve this because it sees less than the whole tube.

## Program consequence

Do not optimize exact coefficient recovery further unless it changes the transition modulus. The next useful observation must use an independent heat-time scale, a transition-adapted quotient, a nonlocal geometry, or a source theorem that rules out the matched central packets. State dimension and injectivity are no longer informative proxies.

A proposed decoder should state its norm, observation window, source restriction, and quantitative inverse modulus for `Lambda_per` itself.

## Counterevidence / boundary

XF-145 treats root-spacing spatial tubes and sub-inverse-degree heat windows. It does not rule out windows at scale `1/N` or larger, global/nonlocal observations, or source-specific constraints excluding the matched controls. Exact identification by moving probes remains true and may become useful if combined with such additional structure.

## Epistemic status

**Exact algebraic identifiability together with exact superexponential short-time transition blindness; a stable source-to-transition observable remains open.**

## Falsification criterion

Produce a uniformly stable `Lambda_per` decoder on the XF-145 matched family from the stated short-time root-spacing tube, or invalidate its central-packet bound. A positive continuation should cross the time/geometry/source boundary rather than merely add another injective state representation.