# MI-057 — Source-slot conditioning does not remove the gamma bulk floor

**Evidence level:** exact source-conditioned variational synthesis from [WI-376](../../findings/WI-376-true-source-slots-do-not-remove-gamma-bulk-floor.md), using the corrected archimedean decomposition of WI-369 and the dependency audit WI-375. This concerns the corrected archimedean block and its ordinary source-complement short, not the full rooted Weil form.

The true source slots feeding one target cell in the current Desogus geometry are too sparse in physical logarithmic measure to eliminate the inherited gamma bulk modes. For target cell `C_k`, every active prime-power source slot has logarithmic width `log(1+1/k)`, and the number of such slots is `O(k/log k)`. Their total logarithmic measure is therefore `O(1/log k)->0` while the physical log interval has length `~log k`.

Perforating a bulk quasimode to vanish on all of those source slots costs only `O(1)` in the positive screened remainder of the corrected archimedean form. Its norm still grows like the interval length, so the constrained Rayleigh quotient tends to the same sharp bulk floor

`-C_Gamma`.

For large `k` there is consequently a nonzero source-zero direction with negative corrected archimedean energy. Scaling that direction shows that the ordinary variational short of the **archimedean block alone** at zero source data is `-infinity`. Retaining the gamma channel and then applying the printed gamma-free source-complement short is therefore not a neutral repair.

The reusable dependency rule is stronger than WI-375: **source conditioning cannot create coercivity if the conditioned complement still contains macroscopic negative bulk directions**. A corrected common-cut theorem must bring an inherited/global/arithmetic positive channel into the form before elimination, prove a coupling that charges those bulk modes, or change the elimination object so that the problematic complement is no longer admissible.

**Boundary.** WI-376 does not prove that the full rooted Weil form has an unbounded short, does not rule out a coupled old-core/arithmetic repair, and has no direct RH conclusion. The obstruction is specifically to using true source-slot deletion by itself to cure the corrected archimedean gamma debt before the pivot.