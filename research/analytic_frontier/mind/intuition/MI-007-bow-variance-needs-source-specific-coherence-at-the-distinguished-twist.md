# MI-007 — Bow variance is controlled by a square-root-scale source completion problem

**Evidence level:** exact Fejer-minus-completion identity, carrier no-go, and prime-source local second-moment reduction through ANF-162

## Core intuition

The endpoint threat in the bow identity is no longer an unspecified low-frequency defect. For the actual prime-source residual, the available arithmetic second moment pins the dangerous cumulative mode to a physical wavelength of order `sqrt X`. A target-scale endpoint completion would therefore require coherent residual accumulation of size `Omega(sqrt(X log X))` across `Omega(sqrt X)` sites.

This is the source-specific quantity that must be controlled. The low positive spectrum and the distinguished cubic carrier are not scarce enough, or coherent enough at the endpoint scale, to supply the missing theorem by themselves.

## Strongest justified principle

ANF-157 writes the bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-158 translates a large completion into large twisted cumulative residual modes. ANF-159--ANF-161 then show that the most tempting parity-quantized carrier resonance cancels too strongly on the relevant endpoint windows to generate the required target-scale spike.

ANF-162 finally inserts the actual residual `r_X=\vartheta-Q_R`. Brun--Titchmarsh sparsity and the explicit counterterm give `sum_I |r_X|^2 << H log X` on intervals `H>=sqrt(X/log X)`. In the endpoint-completion argument this improves the cumulative rank bound to the `K/sqrt X` scale and makes the dangerous physical wavelength `asymp sqrt X`. Hence target-sized completion forces a twisted prefix or suffix of order `sqrt(X log X)` over a square-root-sized block.

## Program consequence

Attack the residual in exactly this currency: prove that its twisted cumulative sums on `sqrt X` windows are `o(sqrt(X log X))` in the bow normalization, or derive a source identity forcing the positive Fejer term to dominate completion. Do not spend further effort on spectral abundance or bare-carrier resonance unless a new argument changes the source coefficient law.

## Counterevidence / boundary

ANF-162 does not itself make endpoint completion small. Its square-root cutoff is also essentially sharp if one uses only the stated local `L^2` bound and pointwise control, so a better conclusion needs genuinely stronger arithmetic information. Cancellation between the Fejer and completion terms remains possible.

## Epistemic status

**Supported exact reduction of the remaining bow obstruction to square-root-scale twisted cumulative concentration of the actual prime residual; the required cancellation theorem is still open.**

## Falsification criterion

Construct admissible prime residual data satisfying the ANF-162 source bounds whose endpoint completion reaches the target scale without a square-root-window cumulative spike, or prove that the current local second-moment inputs alone already force the needed completion bound.