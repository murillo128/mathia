# MI-006 — Critical weak-trace transport reduces locally to stability of a sharp `R<5/2` half-line Jacobi window

**Evidence level:** exact weak-ideal architecture and exact free/variable parity-Jacobi reductions through PF-249

## Core intuition

The Prime-Flute endpoint is controlled by the singular-value envelope of the fully normalized off-diagonal transfer, not by raw channel count or qualitative seam regularity. Earlier work isolated the infinite-rank high-high shear block as the only local piece still needing genuine smoothing.

PF-247--PF-249 now identify the fixed compactification problem sharply. The actual relative geometry is a mode-local half-line Jacobi operator with an inverse-square, first-moment-critical tail. Its free limit has a boundary cancellation strong enough that **full separated output retains exactly the smoothing window `R<5/2`**. Since the endpoint only needs some `R>1`, criticality and output accumulation are no longer generic reasons for failure; the remaining question is stability of that margin under the specific variable Jacobi and geometric perturbations.

## Strongest justified principle

PF-196--PF-243 establish the critical weak-`S_1` architecture, exact channel multiplicity, dressed corridor envelope, actual-seam one-sided control, and reduction of the high-high block to separated Robin-Poisson smoothing of order `R>1`. PF-244 proves that generic form domination permits arbitrary high-to-low conversion; PF-245 rules out a uniform supercritical strip for the bare seam; PF-246 shows that exact commutation would smooth to all orders.

PF-247 supplies the missing intermediate structure. In the Gegenbauer corridor basis the fixed compactified axis generator is exactly parity tridiagonal. The relative operator is two half-line Jacobi chains with coefficients tending to the constant free chain and essential spectrum `[0,1]`.

PF-248 proves coefficient deviations `O(j^{-2})`: trace class but with divergent first weighted moment, so standard first-moment Jost theory cannot simply transfer free edge behavior. In the constant half-line model, the Dirichlet image cancels the bilateral `n^{-2}` square-root tail in fixed output rows, producing `n^{-3}` decay and a toy threshold `R<5/2`.

PF-249 upgrades that calibration to the norm actually relevant after positive separation. For every `d>0`, `E_dJ_0^{1/2}N^R` is Hilbert--Schmidt iff `R<5/2` and has no bounded extension for `R>=5/2`. Thus full-output summation plus separated propagation preserves the same sharp boundary; the free model leaves a robust supercritical interval `1<R<5/2`.

## Program consequence

The theorem surface is now a weighted functional-calculus / threshold-scattering estimate for the **specific first-moment-critical `O(j^{-2})` parity-Jacobi tail**, or for the exact normalized Robin scalar factor if it differs from `J^{1/2}`. It need only retain one fixed exponent `R>1`, not reproduce all-order smoothing.

After that fixed-axis transfer succeeds, charge the `T_a` replacement and width-dependent hypercycle reparameterization against the remaining exponent margin. Do not reopen the already-positive free full-output calculation.

## Counterevidence / boundary

Trace-class perturbation alone does not preserve weighted square-root decay at a zero-energy threshold, and PF-248's formal `j^{-1/2}` subordinate branch is only a diagnostic. PF-249 concerns the constant proxy `J_0^{1/2}` after idealized positive separation; the scalar operator entering the actual normalized Robin map has not yet been proved identical to it. The actual variable-width seam remains a later perturbative step.

## Epistemic status

**Exact mode-local Jacobi reduction and sharp positive free full-output window `R<5/2`; stability on the actual first-moment-critical chain and global reassembly remain open.**

## Falsification criterion

Show that the PF-247 variable Jacobi/actual normalized scalar factor necessarily loses every separated weighted exponent above `R=1`, or invalidate PF-249's sharp free threshold. A positive continuation should transfer some `1<R<5/2` margin through the variable chain and then through the canonical geometric perturbations.