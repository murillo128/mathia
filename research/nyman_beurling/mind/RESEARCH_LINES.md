# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Force branch-stable cross-cut prediction information into a mesoscopic band

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-066--NB-073 reduce a persistent late quotient to a global continuation mode and show that exact branching, the full finite-window local flag, zero one-cell memory, ordinary global conditioning, and stationary matched controls do not determine whether a stable tail survives.

NB-074 introduces the nonstationary continuation charge `J_(R,N)`. NB-075 writes it as raw continuation volume `L_R` minus future-conditioned multiple-correlation charges. NB-076 resolves those charges into the nonnegative interval lattice `kappa_(j,n)=-log(1-|rho_(j,n)|^2)`, giving the exact cross-cut area

`J_(R,N)=L_R-sum_(j<R<=n<=N) kappa_(j,n)`.

NB-077 now reconnects that **signed/conditioned** cancellation geometry to exact integer branching. For a finite rectangle across a cut,

`C_(a|R|b)=sum_(a<=j<R<=n<=b) kappa_(j,n)=log(Delta_(a,R-1) Delta_(R,b)/Delta_(a,b))`,

and integer dilation satisfies

`C_(a|R|b) <= C_(qa|qR|q(b+1)-1)`.

Likewise the raw continuation volume obeys `L_R<=L_(qR)`. Thus coarse cross-cut prediction information cannot be destroyed by signed fine-scale cancellation: exact branching transports it monotonically into the descendant `kappa` lattice. This closes the phase-cancellation weakness of the earlier absolute-Gram branching argument.

The remaining gap is localization. The descendant rectangles widen proportionally with `q`, so branching preserves total predictive information without forcing it into bounded additive distance from the cut. The live arithmetic theorem is to show that enough branch-stable charge accumulates in a genuinely finite/mesoscopic band to recover `L_R-O(1)`, or otherwise compare the growth of raw volume and transported cross-cut charge strongly enough to make the uncancelled continuation `J` bounded along an unbounded sequence.

## Treat raw continuation volume, total cross-cut information, band localization and uncancelled continuation separately

NB-077 makes both `L_R` and the complete finite cross-cut charge monotone under integer branching, but their difference need not be monotone. Branching preservation is therefore not yet a stable-tail contradiction. The missing currency is **where** the preserved conditioned information lands relative to the cut, not whether it survives at all.
