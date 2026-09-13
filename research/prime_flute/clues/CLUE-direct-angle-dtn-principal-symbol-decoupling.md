---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-001-exact-cuff-coordinate.md
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law.md
  - research/prime_flute/findings/PF-235-hypercycle-boundary-compactification-has-only-quadratic-prime-dependent-defect.md
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-299-prime-seam-scale-has-critical-ell-one-accumulation.md
  - research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect.md
  - research/prime_flute/findings/PF-316-direct-channel-payment-makes-the-conditional-angle-endpoint-visible.md
  - research/prime_flute/findings/PF-317-positive-diagonal-completion-reduces-the-direct-angle-to-local-pant-crossing.md
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-319-corridor-form-smallness-alone-does-not-control-the-seam-normalized-direct-angle.md
  - research/prime_flute/findings/PF-320-form-smallness-controls-the-direct-angle-even-when-raw-seam-blocks-amplify.md
  - research/prime_flute/findings/PF-321-superlinear-seam-scale-local-angle-decay-is-trace-class.md
  - research/prime_flute/findings/PF-322-physical-low-packets-retain-critical-compactified-transverse-energy.md
---

# Can the shear-deleted local pant angle gain any fixed superlinear power of the seam scale?

## Observation

PF-315--PF-316 reduce the full physical `P/H` endpoint to two genuine angle channels: the conditional post-low angle `T_H` and the direct angle. PF-317 localizes the direct channel to finitely many positive local pant crossings; PF-318 shows that a local squared Hilbert--Schmidt budget `O((1+\log P_n)/P_n^2)` already gives the required global weak-`S_1` count. PF-320 then moves the actual geometric problem to the **shear-deleted intrinsic local pant angle**, because the PF-232 shear changes that angle only at the already-affordable reciprocal-prime scale.

PF-321 weakens the positive target substantially. Since the exact pant seam distances

\[
s_n=\frac{h_n+h_{n+1}}2
\]

satisfy `\sum_n(1+\log P_n)s_n^q<\infty` for every fixed `q>1`, any bound

\[
\boxed{\|T_{0,n}^{(r)}\|=O(s_n^{1+\varepsilon})}
\]

with one fixed `\varepsilon>0` makes the shear-deleted reference direct channel trace class. A quadratic bound is more than enough. PF-233's exact scaling `T_{a_n}=s_n^2\widetilde T_n` and the even expansion of `F(x)=x/\sinh x` therefore remain a natural source of cancellation to test.

PF-322 now closes the preliminary adversarial check against using that expansion uniformly too early. It constructs explicit **zero-mean** physical-low Fourier packets, entirely inside the fixed PF-212 band, whose mass remains concentrated in an `O(1)` window at a cuff-cell seam. Under the fixed PF-235 compactification their cellwise Pöschl--Teller energy obeys

\[
\liminf_n s_n^2\mathfrak a_{n,\mathrm{cell}}[Uf_n]>0.
\]

The scale collision is exact: PF-001 gives `\cosh(\ell_n/2)=\coth(h_n/2)` and PF-299 gives `s_n\ge h_n/2`, so `s_n\cosh(\ell_n/2)>1`. Thus the whole retained physical-low sector is **not** a uniform small-argument sector for `s_n\widetilde T_n^{1/2}` at the unprojected compactified-form stage. The missing positive mechanism, if it exists, must occur after the actual physical `L/H` projection, seam-energy normalization, and common finite-pant completion.

PF-215 remains only a negative control for the cuff-constant channel; PF-322's witness has zero mean. PF-319 remains the separate warning that corridor-form smallness does not by itself control a seam-normalized raw mixed block.

## Research question

For one canonical one-cusp pant contribution, delete only the PF-232 hypercycle-straightening shear while retaining the actual PF-205 seam energy, the variable-width diagonal corridor, the full common finite-pant/cusp-side completion, and the fixed physical low/high cutoff from PF-212. After distributing the positive identity share as in PF-320, let `T_{0,n}^{(r)}` be the intrinsic local low/high angle for one neighboring offset `r`.

Does this **completed projected angle** satisfy either

\[
\boxed{\|T_{0,n}^{(r)}\|\le Cs_n^{1+\varepsilon}}
\]

for some fixed `\varepsilon>0`, or, failing that,

\[
\boxed{
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\le C\frac{1+\log P_n}{P_n^2}?
}
\]

The first closes the shear-deleted reference in trace class by PF-321; the second closes it at the weak-trace endpoint by PF-318. PF-320 then adds the actual shear. The independent conditional channel `T_H` remains outside this clue.

## Why it may matter

The open calculation is now sharply localized. There is no need to force reciprocal-prime decay if any fixed superlinear seam power survives, but PF-322 proves that this gain cannot come from a blanket claim that `s_n^2\widetilde T_n` is small on every retained low vector. Any successful proof must expose a **projected off-diagonal cancellation** or a singular-value effect created by the physical quotient/normalization/completion.

That distinction matters because PF-233 still gives strong structural information: the principal identity part cannot itself mix `L/H` once represented in a split-respecting space, and the variable-width transfer has an even small-scale expansion. PF-322 says only that the unbounded compactified transverse operator reaches the critical scale on endpoint packets. It therefore tells the next calculation exactly what must be shown: the critical packet must disappear from the intrinsic mixed angle, not from the full local energy.

## Decisive test

Use the explicit seam-centered zero-mean physical-low packets from PF-322 as the adversarial family. Do **not** repeat the already-settled unprojected graph-smallness test.

Propagate those packets through the actual shear-deleted one-cusp-pant construction in the following mathematical sense: retain the finite-pant quotient, transport into the PF-205 physical cuff representation, apply the true seam-energy diagonal normalization, keep the common positive completion used by PF-320, and then form the physical `L/H` mixed corner and its intrinsic angle.

The decisive quantity is the projected normalized response of the PF-322 packet. There are three materially different outcomes:

1. the compactification-critical component cancels in the mixed corner and one obtains `O(s_n^{1+\varepsilon})` for some fixed `\varepsilon>0`; then PF-321 closes the reference direct channel strongly;
2. operator-norm superlinear decay fails, but the critical packet spreads into sufficiently few/small singular directions that the local squared Hilbert--Schmidt leakage remains `O((1+\log P_n)/P_n^2)`; then PF-318 still closes the endpoint;
3. a nonconstant PF-322-type packet survives the full quotient/normalization/completion with angle mass incompatible with both criteria; then this direct-angle route is genuinely obstructed and the failure is no longer attributable merely to an unprojected graph norm.

A negative conclusion must be expressed at the **intrinsic angle** level. Large `A`-form energy, raw seam-block amplification, or the PF-215 constant mode are not sufficient witnesses.

PF-247's parity-Jacobi structure and PF-235's quadratically small hypercycle-coordinate defect should be reintroduced only if they control the specific representation step at which the PF-322 packet either cancels or leaks. PF-233's exact transfer law remains the local corridor input; PF-318 is the fallback if operator norm is too strong.

## Evidence boundary

PF-321 is an implication theorem, not a local PDE estimate. PF-233 supplies exact transfer structure but does not make its unbounded transverse operator uniformly small on the growing physical-low space. PF-322 proves that such uniform smallness is false already at the cell-energy level, using a zero-mean fixed-band packet.

PF-322 does **not** prove that the completed shear-deleted local angle is large. The finite-pant quotient, seam normalization, `L/H` projection, and common completion may erase the critical component. Conversely, none of the current findings proves that they do. The superlinear angle estimate and the PF-318 Hilbert--Schmidt fallback therefore remain open.

PF-320 controls only the difference between the actual sheared and shear-deleted local angles at the established reciprocal-prime cost. It does not transfer PF-233's formal quadratic cancellation through the reference problem. The fixed-domain DtN and band-concentration literature remain prior-art guidance rather than a theorem for this degenerating canonical pant family.

The clue remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-322 has completed the first adversarial packet calculation and rules out the unprojected uniform-Taylor shortcut. The surviving target is now strictly downstream: determine what the **physical projected intrinsic angle** does to that explicit critical packet. Any fixed superlinear seam gain closes the reference channel by PF-321; otherwise measure singular-value/Hilbert--Schmidt leakage against PF-318.