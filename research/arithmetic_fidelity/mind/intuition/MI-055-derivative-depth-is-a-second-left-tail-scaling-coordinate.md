# MI-055 — Derivative depth, source selection, transport provenance, and probe amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-435](../../findings/AF-435-coefficient-root-neutrality-selects-source-radius.md).

AF-416--AF-424 show that the reciprocal-order left-tail determinant has more than one scaling coordinate. A fixed derivative shift closes to a positive Cauchy limit, but moving depth enters through `s_n/n`; the complete partition family detects the critical value `2`, and in the critical window probe amplitude and depth combine as

`b_n(a)=a n^(s_n/n-2)`.

Near square values `b=m^2`, full-column rectangles can tie at leading exponential order while exact rectangle ratios, complete-packet drift and the discrete derivative offset remain visible at finer scales. AF-425--AF-428 show that continuous saddle tuning is therefore not enough: the physical depth variable is integral, exact-square fibres miss the required second-order cancellation, and moving amplitudes lead to exceptional sets that can be residual while still Lebesgue-null and Hausdorff-thin. AF-429--AF-432 expose the analogous supercritical hierarchy: for fixed rational density the source mesh automatically reaches the first `R_n/n` saddle aperture infinitely often, while the packet-corrected `R_n/n^2` target is a genuinely finer pointwise condition.

AF-433--AF-434 then separate two provenance questions that the target geometry alone cannot answer. The reciprocal-order family `x_n(c)=c/n` permits every `c>0`, while the source itself has singularity shells `r_m=2pi m`, so the square amplitudes satisfy `a=m^2 <=> c=r_m`. But the present determinant sums shell labels into zeta factors before partition packets form. Source realization of the same numerical values therefore does not mean that shell identity is transported into packet identity.

AF-435 closes one natural version of the missing selection gate. For an analytic germ `f(z)=sum a_j z^j` with finite nonzero Taylor radius `R(f)`, the source-only coefficient-root response obeys

`Gamma_f(c)=limsup |a_j c^j|^(1/j)=c/R(f)`.

Hence the unique coefficient-root-neutral scale is `c=R(f)`. For the Bernoulli source, `R(h)=2pi`, so this criterion selects `c=2pi` and therefore `a=1` without inspecting determinant packets, exceptional-set membership, primes or zeros. The selection is genuine source provenance. It is also only one admissible selector class, not a theorem that every canonical source rule must choose the radius.

The selected point immediately separates selection from downstream success. AF-434 still says that the existing determinant does not transport shell index, and AF-426 says that the exact-square fibre `a=1` cannot achieve complete adjacent-packet cancellation. Thus the root-neutral selector is a **provenance-positive but mechanism-negative control**: fixing the free amplitude canonically does not make the current target cancellation work.

The reusable order is now four-stage. **First establish source selection. Second establish transport of the selected datum into the destination representation. Third compare the physical source mesh with the target aperture. Fourth test the selected point rather than an optimized surrogate.** The current branch passes the first stage for coefficient-root neutrality, fails shell-index transport in the present determinant, and fails adjacent-packet cancellation at the selected amplitude.

**Boundary.** AF-435 does not classify all possible source-side admissibility notions or nonlinear reparameterizations. AF-434 does not rule out a different shell-resolved representation. AF-426 closes only the present adjacent-packet cancellation mechanism at the selected square fibre, not every full-determinant mechanism. Nothing in this synthesis selects rational primes or zeta zeros or implies RH.