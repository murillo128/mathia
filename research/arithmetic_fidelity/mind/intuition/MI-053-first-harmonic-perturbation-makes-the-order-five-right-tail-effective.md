# MI-053 — First-harmonic perturbation makes the order-five right tail effective

**Evidence level:** exact synthesis from [AF-408](../../findings/AF-408-order-five-euler-failure-is-confined-to-compact-log-scale.md) and [AF-409](../../findings/AF-409-order-five-euler-gate-explicit-right-tail.md). The Toda/Hankel reduction is classical; the Mathia content is the explicit Euler-log perturbation bound.

For the Euler-log profile `f(t)=-log(1-exp(-e^t))`, order five is controlled by the scalar Toda gate `A_4(t)=-(log H_4(t))''`. AF-408 proved only eventual positivity in the right tail. AF-409 makes that half effective:

`A_4(t) > 4e^t-3 > 0` whenever `e^t>=50`, hence `A_4(t)>0` for every `t>=log 50` and in particular for `t>=4`.

The mechanism is useful beyond the numerical cutoff. Writing `x=e^t` and expanding the Euler-log profile by harmonics, the `n=1` harmonic gives an exactly invertible `4 x 4` Hankel reference matrix with determinant `12x^6`. All `n>=2` harmonics form an exponentially small matrix perturbation for large `x`. Controlling the second logarithmic derivative of its determinant converts spectral perturbation size directly into a strict lower bound for the next Toda curvature gate.

Thus the order-five problem is no longer symmetric between the two tails. The right semi-infinite interval is rigorously closed at an explicit source scale; the unresolved quantitative tail bridge is on the left. The compact-interior sign question remains separate, and AF-408 still supplies only eventual left-tail positivity until a comparable effective estimate is proved.

**Boundary.** This does not prove global `H_5>0`, does not supply an effective left cutoff, and does not move the RH discriminator. It is a finite-order translation-positivity certificate for the Euler-log profile, not a rational-prime zero selector.