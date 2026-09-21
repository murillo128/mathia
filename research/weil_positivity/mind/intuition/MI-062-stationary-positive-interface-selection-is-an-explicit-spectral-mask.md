# MI-062 — Stationary positive interface selection is an explicit spectral mask

**Evidence level:** exact algebraic synthesis from [WP-390](../../findings/WP-390-shift-invariant-positive-interface-forms-are-rational-spectral-masks.md), extending the Ramanujan interface reduction in WP-389. Character diagonalization under the unit shift is classical; the line-specific content is the selector classification for the Weil boundary currents.

On the periodic-character span, every shift-invariant positive sesquilinear form diagonalizes in rational-frequency characters:

`B(sum a_r chi_r, sum b_r chi_r) = sum w(r) a_r conjugate(b_r)`

with arbitrary nonnegative weights `w(r)`. The WP-389 shell current `j_m=c_m/sqrt(m)` uses exactly the primitive rational frequencies of reduced denominator `m`, so distinct shell indices are automatically orthogonal.

Exact mixed-prime shell nullity then forces `w(r)=0` at every rational frequency whose reduced denominator has at least two distinct prime factors. Conversely any nonnegative mask supported on denominator `1` and prime powers gives that nullity. Thus stationary positivity does not derive the finite-place selector; it merely provides a coordinate system in which the selector can be programmed explicitly.

Even denominatorwise/Galois symmetry leaves arbitrary shell weights. Bounded Hilbert completion also permits the discontinuous prime-power mask. If the weights instead extend continuously to the ordinary circle, mixed-prime rational frequencies are dense and exact nullity forces the whole form to vanish.

**Boundary.** The classification is stationary. Nonstationary off-diagonal forms, finite-`q` prelimit structure and finite--archimedean coupling remain open categories. A surviving positive mechanism must force its arithmetic spectral support from additional source geometry rather than choose the mask after the Ramanujan decomposition is visible.