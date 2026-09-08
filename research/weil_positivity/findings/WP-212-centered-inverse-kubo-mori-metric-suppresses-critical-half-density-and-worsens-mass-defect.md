# WP-212 — Centered inverse Kubo–Mori metric suppresses the critical half-density and worsens the mass defect

**Status:** `DERIVED + EXACT + BOST-CONNES-KMS + INVERSE-KUBO-MORI + RECIPROCAL-LOGARITHMIC-MEAN + SOURCE-FORCED-CRITICAL-TEMPERATURE + SUPPORT-PRESERVING + BOUNDED-MASS-OBSTRUCTION + PRIOR-ART-AUDITED + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-211` leaves one canonical thermodynamic escape explicitly open: replace the Duhamel/Bogoliubov canonical correlation by its dual/inverse Kubo–Mori geometry. That repair does not recover the Weil carrier in the bounded KMS category.

Relative to the KMS midpoint, the Duhamel multiplier on a rational-log grade `q=e^E` is

\[
s_\beta(E)=\frac{2\sinh(\beta E/2)}{\beta E}.
\]

The centered inverse Kubo–Mori operator therefore has the positive even multiplier

\[
\boxed{
r_\beta(E)=\frac{\beta E}{2\sinh(\beta E/2)}.
}
\]

It satisfies `0<r_beta(E)<=1`, is strictly positive for every finite grade, and decays as

\[
r_\beta(E)\sim \beta |E|e^{-\beta |E|/2}.
\]

Thus the inverse metric preserves support exactly and, at high energy, damps the midpoint spectrum by an *additional* half-density rather than amplifying it.

For a bounded self-adjoint KMS observable with positive unsymmetrized weights `c_q` and detailed balance

\[
c_{q^{-1}}=q^{-\beta}c_q,
\qquad
\sum_q c_q<\infty,
\]

the midpoint weights are `q^{-beta/2}c_q`. Applying the centered inverse multiplier gives, at the source-selected Bost–Connes critical value `beta=1`,

\[
q^{-1/2}c_q\,r_1(\log q)
=
\boxed{c_q\frac{\log q}{q-1}}.
\]

Exact matching to the positive-frequency finite Weil coefficient

\[
\frac{\Lambda(p^k)}{p^{k/2}}
=\frac{\log p}{p^{k/2}}
\]

would therefore require

\[
\boxed{
c_{p^k}
=\frac{p^k-1}{k\,p^{k/2}}
=\frac{p^{k/2}-p^{-k/2}}{k}.
}
\]

Already for `k=1`, `c_p=\sqrt p-1/\sqrt p`, so the required underlying positive GNS mass is not merely non-summable: its individual prime weights grow without bound. Hence no bounded KMS vector can realize the Weil carrier through the inverse Kubo–Mori repair.

This result is stronger than the bounded-mass obstruction in `WP-211` for the forward Duhamel correlation. The forward logarithmic mean erases the midpoint half-density asymptotically; its centered inverse does the opposite operation on the canonical-correlation geometry but, when expressed against the symmetric midpoint measure required by Weil, it introduces an extra high-energy suppression and forces an even larger underlying source mass.

The result does **not** rule out an affiliated observable, distributional tangent, or genuinely unbounded/closable state-space form. It shows that such an escape cannot be justified merely by saying that the inverse BKM metric has the right dual positivity: the exact Weil coefficients force it outside the bounded GNS tangent category, and the inverse multiplier itself cannot manufacture prime-power support or the archimedean/polar terms.

## 1. Center the Duhamel multiplier at the KMS midpoint

`WP-211` derives the normalized strip-average multiplier

\[
m_\beta(q)=\frac{1-q^{-\beta}}{\beta\log q}.
\tag{1}
\]

Writing `E=log q`, factor (1) around the KMS midpoint:

\[
\boxed{
m_\beta(e^E)
=e^{-\beta E/2}
\frac{2\sinh(\beta E/2)}{\beta E}.
}
\tag{2}
\]

The first factor is exactly the KMS midpoint half-density. The second factor

\[
s_\beta(E):=\frac{2\sinh(\beta E/2)}{\beta E}
\tag{3}
\]

is positive, even, and at least one. This is the symmetric spectral multiplier of the Duhamel/Bogoliubov form after the detailed-balance asymmetry has been removed by midpoint conjugation.

The inverse on this centered spectral representation is therefore

\[
\boxed{
r_\beta(E):=s_\beta(E)^{-1}
=\frac{\beta E}{2\sinh(\beta E/2)}.
}
\tag{4}
\]

Equation (4) is positive and even, with continuous value `r_beta(0)=1`. Since `sinh x >= x` for `x>=0`,

\[
0<r_\beta(E)\le1.
\tag{5}
\]

For large `|E|`,

\[
r_\beta(E)
\sim \beta |E|e^{-\beta |E|/2}.
\tag{6}
\]

Thus inverse Kubo–Mori geometry is perfectly sign-compatible on each centered grade, but its high-energy behavior is fixed and strongly suppressive.

## 2. Exact critical coefficient after the inverse metric

Let `c_q>=0` denote the unsymmetrized KMS spectral weights used in `WP-209`--`WP-211`. Detailed balance gives

\[
c_{q^{-1}}=q^{-\beta}c_q.
\tag{7}
\]

Hence the symmetric midpoint mass on the pair `q,q^{-1}` is

\[
a_q^{(\beta)}=q^{-\beta/2}c_q.
\tag{8}
\]

Applying (4) gives the inverse-metric coefficient

\[
b_q^{(\beta)}
=q^{-\beta/2}c_q
\frac{\beta\log q}{2\sinh((\beta/2)\log q)}.
\tag{9}
\]

At `beta=1`, use

\[
2\sinh\!\left(\frac12\log q\right)
=q^{1/2}-q^{-1/2}
\tag{10}
\]

to obtain

\[
\boxed{
b_q^{(1)}=c_q\frac{\log q}{q-1}.}
\tag{11}
\]

No asymptotic approximation is involved.

For `q=p^k`, exact equality with the finite Weil coefficient requires

\[
c_{p^k}\frac{k\log p}{p^k-1}
=\frac{\log p}{p^{k/2}},
\tag{12}
\]

so

\[
\boxed{
c_{p^k}
=\frac{p^k-1}{k p^{k/2}}
=\frac{p^{k/2}-p^{-k/2}}{k}.}
\tag{13}
\]

For primes,

\[
c_p=\sqrt p-\frac1{\sqrt p}\longrightarrow\infty.
\tag{14}
\]

Therefore

\[
\sum_pc_p=\infty,
\tag{15}
\]

contradicting the bounded-vector identity `sum_q c_q=phi(X*X)<infinity` even more strongly than the earlier finite-mass tests.

## 3. The uncentered reciprocal mean does not provide a different symmetric escape

One may instead write the reciprocal of (1) directly:

\[
m_\beta(q)^{-1}
=\frac{\beta\log q}{1-q^{-\beta}}.
\tag{16}
\]

But (16) is not even under `q<->q^{-1}`. The asymmetry is exactly the KMS detailed-balance factor already separated in (2). A Weil-type real/even carrier must first pass to the symmetric midpoint representation; conjugating (16) by that midpoint normalization gives precisely (4).

Thus choosing the uncentered reciprocal mean does not evade (13). It merely hides the same KMS asymmetry in the coordinates.

## 4. Support is preserved, so the arithmetic selector is still external

For every finite `E`,

\[
r_\beta(E)>0.
\tag{17}
\]

Therefore

\[
b_q^{(\beta)}=0
\quad\Longleftrightarrow\quad
c_q=0.
\tag{18}
\]

The inverse Kubo–Mori transform cannot eliminate mixed rational grades or create prime-power support. Exact Mangoldt support must already be present in the source tangent/vector or be produced by a different quotient, cohomological boundary, or global incidence before this metric is applied.

This is the same support rigidity exposed for the forward Duhamel transform in `WP-211`; dualizing the thermodynamic geometry changes the spectral weights but not the selector problem.

## 5. Aggressive falsification and surviving category

**Could the inverse metric rescue the half-density because its uncentered multiplier grows like `log q`?** No. That growth is measured against the unsymmetrized KMS norm. Once the detailed-balance asymmetry is removed, the canonical centered inverse multiplier is (4), which decays like `|log q|q^{-beta/2}`. Equation (11) is the exact critical coefficient.

**Could a bounded observable with different mixed grades compensate?** No. All spectral masses are nonnegative and (17) is diagonal/support-preserving. Additional grades cannot cancel the required prime weights.

**Could one use an unbounded affiliated observable?** Logically yes. Equation (13) then states the precise required source growth. Such a construction must independently prove that the corresponding vector/form has a dense domain and is closable and positive. Finite-cutoff positivity does not establish the infinite limit.

**Could a state-space tangent rather than an observable vector evade this calculation?** Only by leaving the centered GNS implementation classified here. The BKM state-space metric is the dual geometry induced by the same canonical correlation; a genuinely type-III/distributional tangent must specify its operator-algebraic domain and cannot claim the exact Weil match merely from formal inversion of the logarithmic mean.

**Could this supply the archimedean sector?** No. The multiplier depends only on the KMS modular grade and supplies neither the Euler-Gamma divisor nor the polar/global counterterms. Those remain a separate source obligation.

## 6. Prior-art and novelty boundary

No novelty is claimed for the Bogoliubov/Kubo–Mori canonical correlation, its induced state-space geometry, or inversion of the logarithmic-mean operator. Petz and Toth, *The Bogoliubov inner product in quantum statistics*, Letters in Mathematical Physics 27 (1993), 205–216, DOI `10.1007/BF00739578`, and Petz, *Geometry of canonical correlation on the state space of a quantum system*, Journal of Mathematical Physics 35 (1994), 780–795, DOI `10.1063/1.530611`, are the relevant classical anchors already used by `WP-211`.

The line-specific contribution is the exact Bost–Connes critical-grade calculation (11)--(15): after KMS midpoint symmetrization, the canonical inverse metric forces the source weights needed for a Weil match to grow like `sqrt(p)` already on primes. This closes the explicit inverse-BKM repair left open by `WP-211`; it is not a new positivity theorem.

## Consequence for the research line

The canonical thermodynamic fork is now narrower:

\[
\text{KMS midpoint}
\;\xrightarrow{\text{forward Duhamel}}\;
\text{logarithmic-mean carrier (`WP-211`)},
\]

while

\[
\text{KMS midpoint}
\;\xrightarrow{\text{inverse centered BKM}}\;
\text{reciprocal-mean carrier (`WP-212`)}.
\]

Both are independently positive canonical geometries and both fail exact bounded Weil matching; the inverse route is quantitatively worse, and neither supplies the prime-power selector. A surviving KMS construction must therefore be genuinely unbounded/distributional or must acquire its arithmetic support and global finite--archimedean assembly from additional source geometry before the thermodynamic sign theorem is invoked.