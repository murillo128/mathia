# Nyman--Beurling research lines

This file records current mathematical questions for the Nyman--Beurling line. It is a mutable synthesis, not a task queue or history.

## Control the bounded-mass Ford edge pairing with the local zeta potential

**Linked intuition:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`.

NB-230--NB-233 show that population-only control, global pair statistics and unweighted local phase equidistribution do not determine the carrier-width Ford transition. NB-234 identifies the exact nonlinear depth mark and shows that a slowly growing hierarchy of profiled depth--phase moments reconstructs it with factorial accuracy, while every fixed finite hierarchy remains blind in a matched Bellotti-compatible packet.

NB-235 changes representation from abstract growing moments to a classical zeta object. On the critical layer, the unresolved coefficient is a horizontally marked microlocal Landau--Gonek remainder; the shell profile kills the ordinary prime-power diagonal, while black-box smoothing of the global cumulative formula loses the microscopic scale and gives no useful shrinking remainder.

NB-236 removes the horizontal-localization tariff itself. Insert a smooth Ford-depth cutoff directly into the holomorphic carrier and apply Poincare--Lelong to `log|zeta|`. Because the carrier is holomorphic, the Laplacian of the test function lives only on the two transition strips of the depth cutoff. At the Ford scaling its total `L^1` mass is `O(Y+J_0^-1)`, hence `O(1)` on the critical diagonal, and it annihilates harmonic backgrounds. Thus the depth cutoff does not inherently cost a growing power of `X`, `H` or the source capacity.

The load-bearing object is now the signed potential pairing

`int log|zeta(s)| Delta Psi(s) dA(s)`

against this bounded-mass two-edge kernel. Taking absolute values is still useless: bounded kernel mass gives at best a bounded local average, not the `o(1)` required by the destination, and the zeta potential is singular at zeros. The next source theorem must instead give local harmonic approximation or a cancellation-sensitive signed mean for `log|zeta|` across the paired Ford transition strips.

## Keep growing source resolution, horizontal localization cost and potential cancellation distinct

The sequence NB-234--NB-236 now separates three currencies that previously appeared entangled. Growing depth--phase moments are one sufficient representation of the missing source information. The exact zeta representation is a horizontally marked local zero sum. Poincare--Lelong then shows that imposing that horizontal mark smoothly is itself affordable: the kernel has bounded total mass and zero total integral.

What remains is genuinely arithmetic/analytic cancellation in the **local non-harmonic part of the zeta potential**. A theorem that controls only zero population, a global cumulative explicit formula, or the absolute size of `log|zeta|` has not used the cancellation encoded by the edge kernel. Conversely, a microlocal harmonic-approximation theorem for these two strips would attack the exact coefficient directly without first reconstructing an entire growing moment hierarchy.

Future work should preserve the coupled Ford geometry explicitly: the horizontal depth layer, microscopic ordinate scale, carrier normalization, signed two-edge kernel and final `o(1)` target. A result that drops the horizontal mark or replaces the signed pairing by its absolute mass has changed the problem.