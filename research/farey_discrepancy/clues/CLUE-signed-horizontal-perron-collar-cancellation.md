---
id: CLUE-farey-signed-horizontal-perron-collar-cancellation
type: research-clue
status: accepted
origin: mind
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/findings/FD-281-classical-perron-error-pushes-repair-control-above-cluster-pruning-regime.md
  - research/farey_discrepancy/findings/FD-282-absolute-grouped-perron-contours-retain-a-self-divisor-depth-plateau.md
---

# Can signed horizontal Perron integration beat the self-divisor collar plateau?

## Observation

`FD-281` shows that pointwise truncated-Perron error becomes small in the physical Farey repair norm only after the spectral height has already left the useful cluster-pruning regime. `FD-282` then moves consecutive differencing and divisor replication inside the contour and still finds a genuine low-height obstruction once pointwise absolute values are taken on the horizontal edge: prime physical coordinates retain a self-divisor contribution, forcing an absolute right-collar cost of order `Nx` up to logarithms for `T<<x`.

The same finding deliberately leaves one structured channel untouched. The lower bound is for the **absolute collar functional**, not for the signed horizontal contour integral. The complex phase varies with `sigma`, and the upper and lower horizontal edges are related by conjugation for the real Mertens source. A power saving could therefore exist only after integrating a sufficiently large signed object before taking the destination norm.

## Research question

For the exact grouped physical kernel `K_s(d)` of `FD-282`, can the signed upper/lower horizontal contributions at a cluster-prunable cutoff `T=x^(tau+o(1))`, `tau<1`, be estimated directly in the physical repair norm strongly enough to beat `N^theta x^(2-beta)` at the live depths, without first replacing either the `sigma` integral or the physical-coordinate sum by its pointwise absolute envelope?

Equivalently, is there a source-derived oscillatory mechanism along the horizontal contour that cancels the prime self-divisor plateau after integration, or does a second obstruction survive even at this later sign-preserving interface?

## Why it may matter

This is the narrowest surviving hard-Perron escape after `FD-281` and `FD-282`. A positive estimate would preserve the low spectral heights where the complete-cluster population ledger is still informative while avoiding the exact proof interface that creates the `Nx` collar tariff. A negative estimate would close the main sign-preserving continuation of the current hard-contour architecture and redirect attention toward smoothing or a genuinely modified Perron representation.

The question is materially different from merely grouping divisors before triangle inequality: `FD-282` has already done that and shown that the right collar remains too expensive. The possible gain must come from cancellation **along or between contour pieces after physical grouping**.

## Decisive test

Write the exact grouped upper and lower horizontal contributions after the Farey consecutive-difference/divisor-replication map, keeping the `sigma` integral complex until the end. At the first-row calibration and, more generally, polynomial depth `x=N^(lambda+o(1))`, derive a bound in the same physical `l^1` repair norm used by `FD-261` and `FD-281`.

A positive result must exhibit a power saving beyond the `Nx` absolute-collar scale that crosses the target `N^theta x^(2-beta)` while `T` remains below the relevant `FD-278` cluster-population threshold. A negative result must identify a sign-stable component, dual witness or integrated lower-bound mechanism that survives the `sigma` integration or upper/lower-edge combination. Failure of the existing pointwise estimate to exploit cancellation is not a negative result.

## Evidence boundary

`FD-281` and `FD-282` are certificate obstructions, not lower bounds for the true Perron remainder. No signed horizontal cancellation estimate, integrated lower bound, smoothing theorem or RH consequence is established here. The clue concerns the present hard-contour/grouped-repair architecture only; a smooth Mellin cutoff, modified Perron formula or different repair map may have a different collar law.

## Research disposition

Accepted. `FD-283` shows that on every strict right subcollar `1+eta/log(2Nx) <= sigma <= c`, preserving signs through the `sigma` integral does not itself produce a new oscillatory mechanism. After exact physical grouping and the absolutely convergent expansion of `1/zeta(s)`, the `sigma` integration is a positive radial weight multiplying the Möbius Mellin character `exp(iT log(Nu/n))`, while the conjugate edge pair merely extracts one sine quadrature.

The unresolved question is therefore narrower: can this coefficient-space Mellin cancellation, or cancellation between the strict right collar and the portion with `Re(s) <= 1+eta/log(2Nx)`, beat `N^theta x^(2-beta)` at cluster-prunable `T`? No such power saving is established. The clue remains worth pursuing because the exact reduction preserves both a genuinely signed Möbius channel and a cross-collar channel, while ruling out a separate `sigma`-phase explanation.