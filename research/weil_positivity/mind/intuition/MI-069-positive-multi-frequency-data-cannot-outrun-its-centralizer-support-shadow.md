# MI-069 — Positive multi-frequency data cannot outrun its centralizer support shadow

**Evidence level:** exact operator-algebraic synthesis from [WP-397](../../findings/WP-397-multi-frequency-positivity-is-support-dominated-by-critical-centralizer-shadow.md), extending the one-frequency positivity projection of MI-068 and the diffuse critical-centralizer boundary of WP-395.

Multi-frequency positivity does retain noncentral cross terms, but those terms cannot be used to cancel away the zero-frequency support required by positivity. Let `E` be the compact gauge expectation from the critical Bost--Connes factor onto its centralizer and let `a>=0`. Faithfulness gives `E(a)=0` only when `a=0`.

More strongly, if `d=E(a)` and `p=s(d)`, every gauge Fourier coefficient `a_r` satisfies

`a_r = p a_r p`.

This follows from positivity of the operator-valued Fourier coefficient matrix: the `2 x 2` block with diagonal `d` and off-diagonal `a_r` is positive, so the off-diagonal source and range supports cannot extend outside the support of `d`. The centralizer component is therefore not merely nonzero; it is a support floor for every retained frequency.

For a finite sum `y=sum_r x_r` of homogeneous modes, the mechanism is transparent:

`E(y^*y)=sum_r x_r^*x_r`.

Cross-frequency terms may survive in `y^*y`, but the gauge average removes them and leaves a sum of positive self-pairings that cannot destructively interfere. Multi-frequency mixing therefore escapes the one-mode scalarization of MI-068 without escaping the centralizer support tariff.

At the critical Bost--Connes measure class this matters because the standard countable prime-power orbit is Haar-null. Requiring the canonical diagonal support of a bounded positive element to lie exactly on that orbit forces the support projection to vanish, hence the entire positive element to vanish. Off-diagonal frequencies cannot remain nonzero over a region where the centralizer shadow is zero.

The reusable lesson is that **cross terms can preserve information without preserving independent support**. When positivity is formed under a faithful compact-group action, the fixed-point component controls where every Fourier coefficient can live. A proposed multi-frequency selector must therefore use arithmetic phase/correlation information inside a nonzero diffuse support, rather than expect interference to erase the diffuse component while retaining an atomic selector.

**Boundary.** WP-397 concerns bounded positive elements and the canonical critical gauge expectation. It does not show that nonzero-frequency correlations inside diffuse support are arithmetically useless, and it does not classify continuous cores, one-sided correspondences, unbounded nonhomogeneous affiliated forms or finite--archimedean assemblies. The support-domination theorem is universal compact-group positivity machinery; it supplies a structural no-go, not a Weil sign theorem.
