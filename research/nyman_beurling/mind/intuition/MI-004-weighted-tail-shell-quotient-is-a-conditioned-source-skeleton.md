# MI-004 — A conditioned source-faithful skeleton can still hide the full target oracle cost

**Evidence level:** proved

## Core intuition

A useful Nyman compression can quotient a large moving-tail nuisance sector while preserving source coordinates and quantitative conditioning. But those certificates do not imply either that the target loss is arbitrarily reducible or that the compressed target geometry is cheap to evaluate. The weighted tail-shell skeleton makes both distinctions exact.

Its target loss has an intrinsic inverse-cutoff floor, and its upper-section correction carries the original Burnol distance in an explicit source direction. Compression quality, target-loss scale, and **oracle cost** are separate mathematical gates.

## Strongest justified claim

NB-031--NB-034 construct the weighted tail-shell quotient. It preserves the low canonical coefficients, compresses the ordinary tail to one weighted scalar, loses at most `1/M` target energy, and has polynomial conditioning uniformly in the original section size `N`. NB-035--NB-036 give exact Vasyunin/Möbius dual readouts for the retained coordinates.

NB-037--NB-038 show that the upper-section correction cannot be ignored at the final scale. The relative Gram and target-correlation defects are forced at order `d_N^2`, and for the explicit direction `a=B_M^(1/2)u_M`,

`a* S_(M,N) a = (1+o(1)) d_N^2`

in the stated regime. The missing correction therefore contains a multiplicatively accurate copy of the original distance in a direction fixed by the retained arithmetic data.

NB-039 then proves that the `1/M` target loss is itself sharp rather than a crude upper estimate. The weighted nuisance tail contains the dilation `A_M V_floor(N/M)`, giving

`(1-d_floor(N/M)^2)/M <= kappa_hat_(M,N)^2-d_N^2 <= 1/M`.

For `N>=2M`, the loss is uniformly between `log 2/M` and `1/M`. Hence multiplicative target preservation for this quotient is equivalent to

`M d_N^2 -> infinity`.

The same dilation argument also sharpens the explicit-direction approximation: seeing the Burnol/source defect only requires the adaptive condition `M d_N^2/d_floor(N/M)^2 -> infinity`, which can be much weaker than superlogarithmic compression away from the closure-scale alternative.

## Synthesis of evidence

The weighted skeleton succeeds as a representation theorem and exposes why it cannot be a free compression theorem. The discarded weighted tail recursively contains a smaller copy of the original Nyman problem, so the `1/M` loss has a structural source. Meanwhile the target/Gram correction re-enters exactly through a known source direction at the original distance scale.

The next question is therefore a source-cost question: can that explicit directional correction be computed or bounded from arithmetic information strictly cheaper than controlling `d_N` itself? Improving the same quotient's conditioning cannot change the exact inverse-distance threshold.

## Counterevidence / boundary cases

NB-039 is specific to this weighted quotient. A materially different nuisance subspace may have a different target-loss floor. It also does not prove circularity of every theorem controlling the explicit Burnol-scale defect; a new arithmetic identity may still estimate that direction cheaply.

The order-necessity of the familiar superlogarithmic cutoff uses the expected `d_N^2 asymp 1/log N`; the exact unconditional criterion is `M d_N^2 -> infinity`.

## Epistemic status

**Exact representation and compression boundary:** the weighted quotient is source-faithful and conditioned, its target loss is sharply `Theta(1/M)` and multiplicative preservation occurs exactly above the inverse-distance scale, while its upper-section correction carries `d_N^2` in an explicit source direction.

## Novelty/prior-art status

No broad novelty claim is made beyond the finding-level audits. Vasyunin, Burnol, and Bagchi dilation ingredients are prior art; this note records their exact role in the persisted weighted-skeleton construction.

## Falsification criterion

Invalidate the dilation inclusion or the two-sided target-loss identity of NB-039, derive an admitted sequence violating the criterion `kappa_hat/d_N ->1 iff M d_N^2->infinity`, or construct a source estimate for the explicit directional correction that is demonstrably cheaper than the Nyman distance. Any of these would materially revise the present boundary.
