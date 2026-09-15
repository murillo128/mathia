# MI-025 — Interior Schur stripping is admissible but contaminates the Gamma scale

**Evidence level:** exact asymptotic obstruction for the canonical fixed-interior scalar Schur reduction and finite end-normalized chains from [WP-311](../../findings/WP-311-finite-interior-schur-stripping-introduces-log-over-linear-gamma-contamination.md)

WP-310 shows that the critical logarithmic Mangoldt Herglotz source is outside the finite-moment asymptotic class required by the classical Schur transform at infinity. WP-311 tests the natural finite-reference escape, where admissibility is no longer the problem: the canonical one-point interior Schur reduction is a valid positivity-preserving Herglotz operation.

Its high-energy asymptotics nevertheless fail at an earlier scale. For a logarithmic Herglotz end with limiting imaginary height `q>0`, stripping at a fixed interior point `a=u+iv`, then applying the unique positive affine normalization that restores unit logarithmic growth, shifts the `log(y)/y` coefficient by

`A -> A + 2qv/eta`,

where `eta=Im f(a)>0`. Every nonempty finite chain adds such positive increments.

For the reflected critical Mangoldt response, `q=pi/2` and the incoming `log(y)/y` coefficient is zero. One interior step therefore creates the strictly positive term

`(pi v/eta) log(y)/y`,

while the Riemann Gamma comparison has no term at that order and first exposes the relevant curvature at `y^-2`. The Schur transform is thus **admissible but asymptotically non-neutral**: it inserts a larger nuisance term before the target Gamma coefficient is reached.

This separates two gates that are easy to conflate. A positivity-preserving transform must first be defined on the source class, but admissibility alone is insufficient. It must also preserve the asymptotic hierarchy in which the desired source/archimedean discriminator lives. A transform that generates a larger source-forced term can destroy the comparison even while remaining perfectly Herglotz.

The surviving route must therefore justify a mechanism that cancels or avoids this contamination without inserting the target by hand: boundary-reference or moving-reference geometry, an independently motivated renormalization, operator/matrix-valued structure, a noninvertible operation with new meaning, or a genuinely nonseparable finite--archimedean coupling.

**Boundary.** WP-311 covers the canonical scalar fixed-interior one-point reduction and finite chains returned after each step to the same unit-log Herglotz coordinate. It does not rule out boundary-node Schur reductions, moving interpolation points, operator-valued Schur complements, generalized resolvents, or an independently justified added archimedean channel.