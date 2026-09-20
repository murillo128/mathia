# MI-059 — Common-anchor chord weighting is a universal QMF shift

**Evidence level:** exact operator/dynamical synthesis from [PC-380](../../findings/PC-380-common-anchor-chord-weighted-refinement-is-a-universal-qmf-shift.md), following the Chebyshev/tent reductions of PC-372--PC-379. The underlying filter/isometry mechanism is classical; this classifies the source-forced common-anchor chord at the Prime-Circle frontier rather than claiming a new QMF theorem.

For the circle power map `w -> w^m`, attach the most immediate non-unimodular geometric amplitude: the Euclidean chord from the common anchor,

`d(w)=|1-w|`.

Every power-map fiber has exactly constant chord energy:

`(1/m) sum_(w^m=z) d(w)^2 = 2`.

Therefore the normalized weighted composition operator

`W_m = 2^(-1/2) M_d V_m`

is an isometry for every `m>=2`. It is proper, so its adjoint has the universal closed-unit-disk spectrum; before normalization the chord transfer has spectrum `sqrt(2) * closed_disk`. Keeping the full complex chord `1-w` changes nothing because the isometry condition depends on the same squared modulus.

The identity survives the real-cyclotomic/Chebyshev quotient and is independent of whether `m` is prime or composite and of which point of the circle is chosen as anchor. Thus **the canonical branch chord is not the missing source decoration: its exact fiber energy puts it directly on the classical quadrature-mirror-filter/isometry surface**.

This complements the flatness result of PC-379. Resolving branch labels creates only common-refinement relabeling; multiplying those branches by the direct anchor chord creates only a normalized proper isometry. Neither operation retains prime-specific curvature after the relevant quotient.

**Boundary.** PC-380 does not classify singular inverse-chord weights, higher or nonlinear chord functions whose squared fiber mean is not constant, conductor/primitive-shell-dependent amplitudes, source-dependent domains, or matrix/nonlinear interactions before common-refinement identification. Any such candidate must show that its surviving structure is source-forced and not another generic covering/filter identity.