# PL-328 — A new source-exact certificate pushes localized Weil positivity to `a=17/16` and isolates a tail-dropping obstruction

**Evidence:** `LITERATURE (NON-PEER-REVIEWED, COMPUTER-ASSISTED, NOT INDEPENDENTLY REPRODUCED) + EXACT-DERIVED + NEGATIVE/OBSTRUCTION`

**Status:** `BOUNDED-SUPPORT POSITIVITY FRONTIER + SOURCE-EXACT CERTIFICATION + LOCALIZATION-OBSTRUCTION + NO RH CONSEQUENCE`

## Claim

A manuscript by Vincent Liu dated 14 September 2026 and submitted to *Mathematics of Computation* reports a computer-assisted coercivity theorem for the classical Weil quadratic form on the full complex test space

\[
\mathcal D_{17/16}=C_c^\infty((-17/16,17/16);\mathbb C):
\qquad
\boxed{Q(f)\ge 2^{-49162}\|f\|_2^2.}
\]

The source keeps the pole term, every active prime-power source, the infinite-dimensional complement, and the compression/complement cross block. Its public frozen package records a 448-mode Legendre compression split into two parity matrices of order 224, a quantitative Fourier-band complement, a retained positive rank-two tail term, and exact integer residual certificates. The public wrapper explicitly states that external independent reproduction has **not** yet been completed and that journal acceptance is not claimed. This Research Watch inspected the theorem statement, normalization, proof architecture, exact source list, obstruction theorem, and frozen repository provenance, but did **not** execute the roughly 635 MB reproduction package. The numerical lower bound is therefore stored as a recent non-peer-reviewed computer-assisted literature claim, not as independently reproduced Mathia evidence.

Combining that theorem with the already-audited common-form dictionary of `PL-265`/`PL-283` gives the canonical Suzuki/Friedrichs operator bound

\[
\boxed{A_{17/16}\ge 2^{-49162}I>0.}
\]

Indeed the external inequality holds on the smooth compactly supported class, hence on Suzuki's form core, and a uniform lower form bound survives Friedrichs closure. By the nested-domain min--max monotonicity of `PL-280`, conditional only on correctness of the reported certificate,

\[
\boxed{A_a>0\qquad(0<a\le17/16).}
\]

Thus the current canonical fixed-window frontier jumps from the `a=0.8` certificate in `PL-283` to

\[
\boxed{a_-=\inf\{a:\lambda_1(a)<0\}>17/16=1.0625}
\]

if a strict-negative aperture exists at all.

The same manuscript proves an independent structural obstruction: a particular localization that replaces the high-frequency tail by the unit-window lower comparison has a strictly negative high-frequency defect once

\[
L>\frac{\log8}{2}.
\]

For explicitly modulated compactly supported tests it obtains

\[
\lim_{k\to\infty}
\frac{\mathcal D_\chi(f_k)}{\|f_k\|^2}
=
\frac1{16}-\frac{\log2}{2\sqrt2}
< -\frac18,
\]

and proves that no fixed bounded compact self-adjoint correction can make that **comparison** nonnegative for every test. This is not a negative value of the full Weil form. Rather, it shows that beyond the `8` threshold a source-exact proof cannot simply discard the positive high-frequency remainder and hope to repair the resulting comparison by a fixed compact term. The positive `17/16` theorem succeeds precisely by retaining quantitative tail information.

## 1. Exact arithmetic content of the `17/16` window

At half-width

\[
L=\frac{17}{16},
\qquad
2L=\frac{17}{8}=2.125,
\]

the support condition in the explicit formula is

\[
\log n<2L.
\]

Since

\[
\log 8<2L<\log9,
\]

the complete von-Mangoldt support is exactly

\[
n=2,3,4,5,7,8.
\]

In prime-exponent coordinates these are the axis points

\[
e_2,\ e_3,\ 2e_2,\ e_5,\ e_7,\ 3e_2.
\]

This is a genuine source-frontier advance over `PL-283`: the `0.8` certificate had only `2,3,4` active. The new result crosses the `5`, `7`, and `8` activation thresholds and remains below the next source event `9=3^2` at `a=(\log9)/2`.

The manuscript writes, on the legal smooth domain,

\[
Q(f)=\langle f,(M+K)f\rangle+T_{\rm tail}(f),
\]

where `M` contains the six compressed prime-power shifts and `K` is a compact integral operator. It proves the explicit order bound

\[
\frac{9617}{10400}I\preceq M\preceq\frac{63183}{10400}I
\]

and, rather than discarding the exterior Fourier band, retains

\[
T_{\rm tail}(f)
\ge
2^{-49162}\|f\|^2+\langle f,Uf\rangle,
\]

where `U` is a positive rank-two operator built from the first two Legendre modes after applying the band-complement operator. The finite compression uses Legendre orders `0,...,447`; reflection symmetry produces two real symmetric blocks of order 224. The final sign test is reduced by positive congruence to exact integer matrices satisfying a Gram-plus-margin decomposition whose residual row sums are strictly smaller than the retained diagonal margin.

These details matter because the theorem is not a statement that a floating-point Galerkin matrix happened to be positive. The source separately pays for the finite block, the full orthogonal complement, and their first-order coupling. Nevertheless, without an independent replay of the frozen artifact Mathia does not promote the stated numerical constant above literature status.

## 2. Transfer to the canonical localized Suzuki operator

`PL-265` and `PL-283` already audit the normalization dictionary between the classical compact-support Weil form and Suzuki's localized closed form. Let `A_a` denote the corresponding Friedrichs representative. The external theorem states its lower bound for every smooth complex test supported in `(-17/16,17/16)`, so in particular it holds on Suzuki's smooth form core. Therefore

\[
Q^{17/16}_W(v)
\ge2^{-49162}\|v\|_2^2
\]

on that core, and closure yields

\[
A_{17/16}\ge2^{-49162}I.
\]

No finite-dimensional-to-infinite-dimensional inference is being introduced by Mathia here: that burden belongs to the external theorem. The Mathia step is only restriction to the already-identified form core followed by closure.

`PL-280` then supplies the exact monotonic implication. Since the form domains are nested with aperture and the ordered eigenvalues are nonincreasing,

\[
\lambda_1(a)\ge\lambda_1(17/16)>0
\qquad(0<a\le17/16).
\]

This supersedes the **finite certified frontier** in `PL-283`. It does not supersede the analytic mechanism program of `PL-313`--`PL-327`: those findings ask why source activation preserves positivity and what signed local structure could scale, whereas the present theorem is a very large fixed-window certificate.

## 3. The `8`-channel obstruction is to a proof strategy, not to Weil positivity

The manuscript also analyzes a localization obtained by averaging unit-window pieces and replacing their exact high-frequency remainder with a bounded lower comparison. For any

\[
L>\frac{\log8}{2},
\]

it chooses a two-bump real function whose autocorrelation meets the arithmetic comb only at `log 8`, and modulates it by

\[
T_k=\frac{2\pi k}{\log8}.
\]

The continuous defect then vanishes by Riemann--Lebesgue while the `8` source remains phase-locked. The surviving discrete contribution is

\[
\frac{c_8}{2}=\frac{\log2}{2\sqrt2},
\]

whereas the retained scalar floor is only `1/16`. This gives the exact negative limit

\[
\frac1{16}-\frac{\log2}{2\sqrt2}.
\]

Because high-frequency modulations converge weakly to zero, every fixed compact correction contributes asymptotically zero; hence no such compact repair can restore nonnegativity of that tail-dropped comparison.

This is a useful falsification result for the current line. It rules out a broad-looking but actually too-weak strategy: prove a source-local inequality after dropping difficult positive tail directions, then compensate all arithmetic losses by a fixed compact operator. The obstruction is **phase-specific to the rational-prime source** through `log 8`, but it is still only an obstruction to that localization scheme. The complete Weil form retains additional positive tail energy, and Theorem B claims positivity at `17/16`, which is already strictly above `log8/2`.

The right lesson is therefore not that the `8` channel causes negativity. It is that any scalable source-side proof must retain enough frequency-dependent positive information to balance phase-locked prime-power losses. The rank-two tail retention in the source is one finite-window realization of this principle; no aperture-uniform version is supplied.

## 4. Prior-art and novelty audit

The closest prior certified bound in this line is Zhu's arXiv:`2608.24827v2`, recorded as source 58 and transferred to Suzuki's operator in `PL-283`, at half-width `0.8` with lower constant `8.9e-18`. Liu's manuscript explicitly identifies that as the closest verified quantitative comparison and states that an earlier `1.19` certificate in that version chain was withdrawn. Yoshida's classical work supplies much smaller-window strict positivity and finite-to-infinite precedents; Connes--Consani and Suzuki supply the operator/form framework. The block-Schur, interval-matrix, Legendre, and residual-verification machinery is therefore not claimed as new in itself.

The substantive current-literature delta is the reported full-complex-test coercivity at `17/16`, with all active source terms through `8`, plus the explicit high-frequency obstruction to the specified tail-dropping localization. Targeted searches by the exact title, author, constants, and `17/16` window found the 15 September 2026 public dissemination and the frozen GitHub submission package, but no journal acceptance, citation-based independent verification, or external reproduction. Absence of such hits is not evidence of novelty; it determines only the evidence label used here.

The frozen public repository identifies source commit

`b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`

and a `634,659,625`-byte reproduction archive with SHA-256

`7f8e47d265326cbfa4da95197c98bc226fe6cbfd8a22e6896955c18d8cdb376d`.

Its README explicitly says `EXTERNAL_REPRODUCTION = NOT_YET_COMPLETED`. Historical internal labels inside the package are not treated as external validation.

## 5. Adversarial checks and boundaries

- **No independent replay.** The decisive computer-assisted inequalities and exact integer certificates were inspected as published source claims but not recomputed in this watch. A failed clean reproduction would require correction or withdrawal of the numerical frontier.
- **No peer-review upgrade.** Submission to *Mathematics of Computation* and public frozen artifacts are provenance, not acceptance or independent mathematical validation.
- **No RH consequence.** Fixed-window positivity, even beyond several prime-power thresholds, does not establish the universal support quantifier in Weil's criterion.
- **No monotonic forward extrapolation.** `PL-280` propagates positivity to *smaller* apertures only. Nothing here proves positivity past `17/16`, even though the next source event is `9`.
- **No claim that `8` is harmful to the full form.** The obstruction concerns a specified tail-dropping comparison. The full form retains the positive tail that the comparison removed.
- **No aperture-uniform certificate.** The reported constant is extraordinarily small and the proof uses a fixed 448-dimensional compression plus a fixed-band argument. It gives no uniform positive margin or bounded complexity as `a` grows.
- **No replacement for the current analytic gate.** `PL-324`--`PL-327` seek a structural sign mechanism near source activation. The new certificate shows that positivity in fact survives far beyond the first source, but it does not explain that survival in a way that scales to all apertures.

## 6. Decisive audit tests

The literature claim is directly falsifiable by replaying the frozen release in the documented CPython environment and checking the complete chain for Theorem B: source reconstruction, the exact active list `2,3,4,5,7,8`, the band-complement estimate, the retained rank-two tail bound, the projection/complement/cross-block error allowances, the two parity congruence compilers, and the final exact Gram residual inequalities. The reproduced lower bound must dominate `2^-49162` on the full complex test space, not merely on the 448-mode compression.

The obstruction theorem can be audited independently of the large certificate: reconstruct the two-bump test with autocorrelation supported only near `0` and `±log8`, verify that only the `8` source survives, apply Riemann--Lebesgue to the continuous term, and use weak convergence of the modulations against a fixed compact operator. Failure of any of those exact steps would invalidate the strategy obstruction while leaving the computer-assisted theorem logically separate.

## Consequence for the line

Conditional on successful independent validation of the new computer-assisted source, the finite-window question is now settled substantially deeper than `PL-283` recorded: the canonical completed Weil operator is strictly positive through `a=17/16`, after six prime-power axis atoms have activated. This makes further isolated first-prime positivity certificates even less valuable as an RH mechanism; the useful target remains an **aperture-uniform source-side argument** explaining why the positive archimedean/tail structure continues to dominate the growing von-Mangoldt comb.

The obstruction theorem sharpens that target. A scalable argument cannot indiscriminately replace the high-frequency tail by a scalar floor plus fixed compact repair once phase-locked prime-power channels are active. It must retain frequency-dependent positive information, or find a different exact identity whose arithmetic sign survives source growth.

## Sources

- Vincent Liu, *Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function*, manuscript dated 14 September 2026, submitted to *Mathematics of Computation*; public dissemination 15 September 2026. Frozen source/reproduction repository: https://github.com/luciferyu666/certified-weil-positivity , source commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`. Non-peer-reviewed; public wrapper states external reproduction is not yet completed.
- Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law*, arXiv:`2608.24827v2`, source 58: previous certified `a=0.8` comparison and finite-to-infinite precedent.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2`, source 56: canonical localized Weil form/Friedrichs operator used in the transfer.
- `PL-265`: common-form and support-radius normalization dictionary.
- `PL-280`: nested-domain eigenvalue monotonicity.
- `PL-283`: previous canonical finite-window frontier at `a=0.8` and the already-audited supported-test-to-Suzuki closure bridge.