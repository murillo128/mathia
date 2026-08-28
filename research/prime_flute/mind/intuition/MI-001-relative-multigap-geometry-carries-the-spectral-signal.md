# MI-001 — Relative multi-gap geometry survives in resolved spectral memory

**Evidence level:** proved

## Core intuition

A distinguished cuff by itself is only a standard hyperbolic cylinder parameter.  Arithmetic structure becomes spectrally nontrivial when **several neighboring cuff contrasts interact and the spectrum is kept resolved mode by mode**.  The first-order small eigenvalue at a weak neck sees the current relative gap scale; its first resolvable correction can remember the immediately stronger upstream neck.  Scalar products of the same eigenvalues can erase exactly that memory.

## Strongest justified claim

For a fixed chain of `N` pairs of pants with hierarchical separating lengths

\[
w_1>w_2>\cdots>w_{N-1}\to0,
\qquad r_j:=w_j/w_{j-1},
\]

assume, for `j=2,...,N-1`,

\[
r_j\to0,
\qquad \sqrt{w_1}=o(r_j),
\qquad r_{j+1}=o(r_j)\quad(j<N-1).
\]

Then Burger's quantitative surface-to-graph estimate resolves the first Feshbach correction on the **true hyperbolic surface**:

\[
\lambda^{(j)}
=\frac{j+1}{2\pi^2j}w_j
-\frac{(j+1)(j-1)^2}{2\pi^2j^3}
 \frac{w_j^2}{w_{j-1}}
+o\!\left(\frac{w_j^2}{w_{j-1}}\right).
\]

For exact prime-derived tangents in the hierarchical regime,

\[
w_j=4\sqrt{d_j/d_{j+1}}(1+o(1)),
\]

so the leading term depends on the current adjacent gap ratio while the correction depends on three consecutive gaps:

\[
\frac{w_j^2}{w_{j-1}}
=4\frac{d_j^{3/2}}{d_{j+1}\sqrt{d_{j-1}}}(1+o(1)).
\]

Equivalently, with cuff contrasts `C_j=ell_j-ell_{j+1}`,

\[
\lambda^{(j)}
=\frac{2(j+1)}{\pi^2j}e^{-C_j/4}
-\frac{2(j+1)(j-1)^2}{\pi^2j^3}
 e^{-(2C_j-C_{j-1})/4}
+o\!\left(e^{-(2C_j-C_{j-1})/4}\right).
\]

Thus the resolved low spectrum has a finite **upstream-memory ladder**: the first term sees the present scale, while the first nontrivial correction sees an ordered relation between present and previous scales.

## Synthesis of evidence

PF-032/PF-037 prove that a single cuff germ contributes only universal cylinder data.  PF-029/PF-034/PF-047/PF-054 show how relative gap patterns become finite punctured-sphere tangents and weighted-path small spectra.  PF-080/PF-081 identify effective resistance/Feshbach as the mechanism by which a weak mode remembers stronger upstream modes.  PF-090 proves the `b^2/a` coefficient for the actual `S_{0,5}` Laplacian in the moderate window `a^(3/2)<<b<<a`; PF-091 extends this to an arbitrary fixed-length graded ladder.

PF-089 supplies the complementary negative: for a weighted path,

\[
\operatorname{pdet}G=N\prod_j w_j,
\]

and in the strong hierarchy the product telescopes to the endpoint gap contrast.  In the two-neck case the `b^2/a` shifts of the two positive eigenvalues cancel exactly in `mu_+mu_-=3ab`.  The memory is therefore **spectrally resolved but determinant-invisible** at this singular order.

## Evidence against overgeneralization / boundary cases

The graded surface theorem is rigorous for any fixed hyperbolic chain satisfying the displayed scale conditions.  What is **not** proved is that the current Maynard/Pintz isolation machinery recurrently realizes those moderate upper bounds for consecutive prime gaps.  PF-046/PF-054 force very strong hierarchical prime patterns, but the sieve-selected subset is not controlled finely enough to guarantee `sqrt(w_1)<<r_j`.

Nor is every relative observable informative: PF-031 identifies a sojourn difference with a standard shear coordinate, PF-048 shows unmarked path eigenvalues are not generally inverse-unique, and PF-088 shows that some apparent critical exponents are one-dimensional propagation effects already present for integers.

## Status / novelty

The exact cross-ratio/cuff formulas and the finite-tangent spectral expansions under the graded hypotheses are proved.  The recurrence of those specific moderate hierarchies in the actual prime flute is open.  Burger's theorem, weighted graph limits, Feshbach reduction and effective resistance are classical; the potentially new content is the resolved multiscale coefficient and its exact prime-cuff interpretation.

## Falsification criterion

The precise surface intuition fails if the displayed `w_j^2/w_{j-1}` coefficient is not present in a chain satisfying the graded Burger window.  The arithmetic extension fails if prime isolation can never realize such a window and no sharper surface estimate reaches the stronger hierarchies that are known to recur.

## Lean-formalizable core

- Exact weighted-path eigenvalues for the two-neck case and `mu_+mu_-=3ab`.
- Effective-resistance formula for a path and the coefficient of `w_j^2/w_{j-1}`.
- Algebraic conversion from neck ratios to three-gap and two-cuff-contrast expressions.
- Matrix-tree telescoping of the low-energy pseudodeterminant.
