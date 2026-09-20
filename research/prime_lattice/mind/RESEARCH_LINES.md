# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Retain the analytic continuation tail in a zero-sensitive category rather than quotienting it away

**Linked intuition:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`.

The native bounded almost-periodic zeta symbol leaves its algebra at `Re(s)=1`, while Besicovitch `B^2` carries the Dirichlet series through `Re(s)>1/2` but forgets isolated point values. PL-391 adds a prior-art boundary: finite Dirichlet-polynomial Jessen zero densities can concentrate on the half-line for an `L^2` coefficient-energy reason, yet that normalized density is too coarse to track a fixed zero of the analytically continued zeta function.

PL-392 makes the loss exact. The one-term Euler--Maclaurin correction `N^(1-s)/(s-1)` turns the raw partial sum into a function converging locally uniformly to zeta on `Re(s)>0` away from the pole, so Rouché can recover each fixed zero. On every fixed vertical strip inside the critical strip, however, that correction is `C_0` in the height variable and therefore has zero Besicovitch `B^2` seminorm. The zero-faithful continuation and the raw cutoff represent the same `B^2` class.

The next object must therefore be single-zero-sensitive **and** distinguish the source-forced analytic continuation tail from its `B^2` quotient. A nonlinear Jessen/logarithmic quantity, an `AP+C_0` extension, or a target-relative Fredholm/Toeplitz construction remains viable only if it retains the actual continuation representative rather than depending solely on the native mean-square class.

## Keep density concentration, analytic continuation and divisor fidelity separate

A limiting zero density on `Re(s)=1/2` is not an RH statement unless it controls the actual analytic divisor. Conversely, local-uniform Euler--Maclaurin continuation is zero-faithful but can be invisible to a mean-square almost-periodic quotient. Every proposed prime-lattice bridge should state which representative is retained, which topology gives continuation, and what mechanism sees an individual zero rather than only an averaged density.
