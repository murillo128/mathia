# MC-260 — Sparse BDH diagonal scale starts only beyond the live shell barrier

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the exact logarithmic-shell source isolated in `MC-258`--`MC-259`. Write

\[
y=c\log X,
\qquad
R=\prod_{y<r\le 2y\atop r\ {m prime}}r,
\qquad
T=X-P=X^{1+o(1)},
\]

so that the prime number theorem gives

\[
R=X^{c+o(1)},
\qquad
R^2=X^{2c+o(1)}.
\tag{1}
\]

The exact descended blind-source projector of `MC-258` is

\[
B_S^{(A)}(X)
=
\frac1{R|H|}
\sum_{\substack{n\le T\\-n\bmod R\in H}}g_y(n),
\qquad
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y},
\tag{2}
\]

and direct support reaches the square-root target only at

\[
c\ge \frac14.
\tag{3}
\]

A natural response to `MC-259` is to seek a variance theorem whose error is scaled by the thin support of `g_y`, rather than by the full progression occupancy `T/R`. Adam Harper's 2025 sparse Barban--Davenport--Halberstam theorem is a particularly close piece of prior art: for a general complex sequence satisfying his progression, concentration, and hereditary-sparsity hypotheses, Theorem 1 gives a variance with diagonal main term

\[
\frac Q2\sum_{n\le x}|a_n|^2
\tag{4}
\]

rather than a dense `Qx` scale. However, the theorem is stated only in the large-modulus range

\[
\boxed{\sqrt{2x}<Q\le x.}
\tag{5}
\]

For the Mathia shell, this range restriction has an exact exponent consequence independent of every other hypothesis of Harper's theorem:

- on the descended squarefree modulus `R`, `(5)` would require `c>1/2+o(1)`, so it never reaches the canonical shell range `0<c<1/2`;
- on the original square modulus `R^2`, `(5)` would require

\[
2c>\frac12+o(1),
\qquad\text{i.e.}\qquad
\boxed{c>\frac14+o(1).}
\tag{6}
\]

But `(6)` is precisely the side of the phase boundary on which the elementary rough-support estimate from `MC-258` already gives

\[
|B_S^{(A)}(X)|
\ll
\frac{X^{1-2c+o(1)}}{\log\log X}
\le X^{1/2+o(1)}.
\tag{7}
\]

Therefore **the currently available general sparse-BDH diagonal regime turns on only after the live fixed-power shell problem has already disappeared by support**. In the strict hard range

\[
0<c<\frac14,
\tag{8}
\]

both `R=X^{c+o(1)}` and `R^2=X^{2c+o(1)}` lie below the square-root modulus threshold in `(5)`.

This is a theorem-range obstruction, not a claim that sparse variance is irrelevant. In fact it identifies a sharp missing input: a fixed-modulus or sub-square-root-modulus analogue with variance scaled by the actual rough support would contain information absent from `MC-237` and `MC-259`. Harper's theorem shows that such support-sensitive diagonal behavior is mathematically natural in an adjacent regime, but its present modulus range cannot be transplanted to the live shell by parameter optimization.

No new BDH theorem, no variance estimate for `g_y` at `R` or `R^2`, and no improvement for `M(X)` is proved here.

## 1. The live support threshold is exactly `c=1/4`

`MC-258` proves that conductor descent from the prime-square modulus to the squarefree shell radical does not remove the exterior normalization inherited from the original projector. In the full-shell specialization this gives the support bound

\[
|B_S^{(A)}(X)|
\ll
\frac{T}{R^2}\frac{\varphi(P)}P+X^{o(1)}.
\tag{9}
\]

Mertens' product theorem at `y=c\log X` gives

\[
\frac{\varphi(P)}P\asymp\frac1{\log y}
\asymp\frac1{\log\log X},
\tag{10}
\]

while `(1)` gives `T/R^2=X^{1-2c+o(1)}`. Hence `(9)` has power exponent `1-2c`. It reaches the RH-facing square-root scale exactly when

\[
1-2c\le\frac12,
\]

which is `(3)`.

The unresolved shell regime is consequently not an arbitrary parameter choice: it is exactly `c<1/4`.

## 2. Harper's sparse variance theorem lives on the opposite side

Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences*, Journal of the London Mathematical Society (2025), DOI `10.1112/jlms.70293`, arXiv `2412.19644`, studies the dyadic-modulus variance `V(\mathcal A,x,Q)` for a general complex sequence. Theorem 1 assumes

\[
\sqrt{2x}<Q\le x
\tag{11}
\]

and, under progression, non-concentration-on-multiples, and hereditary-sparsity conditions, obtains the diagonal term `(4)` plus explicit errors. The point relevant here is structural: the leading variance sees `\sum |a_n|^2`, so genuinely sparse support can lower the natural variance scale.

For the shell source, take only the exponent-level substitution `x=T=X^{1+o(1)}`. No claim that `g_y` satisfies Harper's other hypotheses is needed for the obstruction below.

If one tries to use the descended modulus as the dyadic modulus scale, `Q\asymp R`, then `(1)` and `(11)` require

\[
c>\frac12+o(1).
\tag{12}
\]

This lies outside the canonical `c<1/2` shell even before imposing the harder `c<1/4` frontier.

If instead one retains the original prime-square modulus, `Q\asymp R^2`, then `(11)` requires

\[
2c>\frac12+o(1),
\]

which is `(6)`. Thus the square-modulus version first enters Harper's large-modulus regime at the same exponent where `(9)` already becomes square-root-small.

This matching is not an artefact of constants. Replacing `\sqrt{2x}` by `x^{1/2+o(1)}` leaves the phase boundary unchanged.

## 3. Why this differs from the KMT obstruction

`MC-237` and `MC-259` use Klurman--Mangerel--Teräväinen's individual smooth-modulus theorem. That result *does* apply to the exact logarithmically smooth source moduli in the hard region, but its residual scale is tied to dense progression occupancy and gains only a subpower relative factor after the smoothness parameter is priced. `MC-259` further shows that source-coset aggregation leaves at most one blind pretender as a rank-one obstruction, while the KMT residual remains weaker than direct rough support.

Harper's theorem attacks the complementary weakness: its diagonal main term is support-sensitive. For a sparse sequence with roughly `T/\log y` nonzero coefficients, a diagonal variance of the form `(4)` is of order `QT/\log y`, not `QT`. This is qualitatively the kind of source-scaled information that `MC-259` says could matter.

The obstruction here is therefore different from `MC-237`: **the right variance normalization exists in prior art, but only for moduli above the square-root barrier; the exact Mathia hard shell sits below that barrier.** The two theorems currently miss the target in complementary ways:

\[
\text{KMT: correct modulus regime, dense residual scale;}
\]

\[
\text{Harper: sparse diagonal scale, wrong modulus regime.}
\tag{13}
\]

This isolates a more precise theorem surface than the vague request for "better dispersion".

## 4. Enlarging the averaging window does not automatically include the source modulus

Harper's variance is dyadic in the modulus variable: it sums over moduli in a range comparable to `Q`. A source modulus `R` or `R^2` below `X^{1/2}` is therefore not a nonnegative summand of a theorem applied with some unrelated `Q>X^{1/2}`. One cannot invoke `(11)` at a larger modulus scale and then discard terms to obtain a bound for the smaller source modulus.

Likewise, multiplying `R` by auxiliary factors until the resulting modulus crosses `X^{1/2}` changes the residue problem. Such a lift would need an exact identity transporting `(2)` to the enlarged modulus while preserving the normalization and signed source; no such identity follows from sparse BDH itself.

The obstruction is thus not repaired by a bookkeeping choice of `Q`.

## 5. Prior-art and novelty audit

The sparse/general-sequence BDH theorem is established prior art. Harper's paper proves two elementary general variance estimates and applies them to smooth numbers; Theorem 1 is explicitly designed for sparse sequences and explicitly assumes `\sqrt{2x}<Q\le x`. The diagonal term `(4)` and range `(5)` are taken directly from that theorem.

Classical Möbius BDH is already audited in `MC-227`, and the individual smooth-modulus multiplicative-function variance theorem is already audited in `MC-237` and `MC-259`. A bounded literature check around sparse BDH, rough/smooth-number progression variance, and smooth moduli found no theorem in those sources that simultaneously provides Harper-type support-scaled diagonal control for the exact fixed shell modulus in the sub-square-root range `(8)`. This is only a bounded frontier audit, not a claim of bibliographic nonexistence.

No novelty is claimed for BDH, Harper's diagonal formula, Mertens' product, or the prime-number-theorem estimate for `R`. The durable line-specific result is the **phase alignment** obtained by substituting the exact Mathia shell scales into the closest support-sensitive variance theorem: its lower modulus threshold coincides with the point at which direct support already closes the original square-modulus source.

## 6. Boundaries and decisive escape route

- The finding does not prove that `g_y` satisfies Harper's progression, concentration, or hereditary-sparsity hypotheses. The no-go uses only the theorem's necessary modulus range, so failure to verify those additional hypotheses can only make direct application harder.
- The theorem is an average over a dyadic family of moduli. Even above the threshold, an asymptotic for that family is not automatically a sharp fixed-modulus estimate for the distinguished shell modulus.
- A different sparse-variance theorem valid for fixed smooth moduli or for `Q<X^{1/2}` is not ruled out. That is precisely the missing theorem surface identified here.
- A source-coupled bilinear argument may bypass residue-class variance entirely. Nothing here obstructs cancellation before the coset projection or across the smooth-dilation fibers.
- The endpoint `c=1/4` carries logarithmic factors and is not treated as a sharp constant-level transition; all statements are at fixed-power exponent resolution.

A genuinely new input would therefore have to combine the two currently separated advantages in `(13)`: **support-sensitive variance at the actual sub-square-root smooth source modulus**, or an exact source transformation reducing the hard coset sum to a regime where such a theorem already applies. Merely importing a large-modulus sparse BDH theorem cannot change the current frontier.
