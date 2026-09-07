# ANF-089 — a cross-metric Gram ratio controls distance to the separable cone

**Status:** `EXACT-DERIVED + CONDITIONING-TO-GEOMETRY + CROSS-METRIC-GRAM-GATE + ALL-CARDINALITIES + ALL-MULTIPLICITIES + CENTRAL-NOTCH`. `ANF-086` shows that a configuration defeating the fixed central-notch certificate must stay a fixed positive distance `kappa_crit` from every compatible separable carrier in the destination norm. `ANF-088` shows that Montgomery--Taylor excess pays exactly for nonreal antisymmetric projection leakage, but leaves open whether small projection taxes force small destination distance. The missing implication can be made quantitative without a compactness assumption: for every finite configuration, the distance to the real-collapse separable carrier is bounded by the relative Montgomery--Taylor excess multiplied by one explicit cross-metric Gram-conditioning ratio.

Fix the central-notch data of `ANF-086`,

\[
J_s\ge0,
\qquad
\|q\|_s^2:=\int_{-1}^{1}J_s(\alpha)|q(\alpha)|^2\,d\alpha,
\qquad
q_s>0,
\tag{1}
\]

and retain the Montgomery--Taylor notation

\[
\Delta(W):=E_{\rm MT}(W)-L(W),
\qquad
L(W):=2|W|-\sigma(W).
\tag{2}
\]

Let `Z_+(W)` contain one representative `z=x_z+i y_z`, with `y_z>0`, from each distinct nonreal conjugate pair of a nonempty finite conjugation-invariant multiset `W`, and let `m_z` be the common multiplicity of `z` and `bar z`. Put

\[
M_{\rm nr}(W):=\sum_{z\in Z_+(W)}m_z.
\tag{3}
\]

For the exact Montgomery--Taylor factor `eta_MT` of `ANF-087`--`ANF-088`, define

\[
f_\lambda(u):=\eta_{\rm MT}(u)e^{-2\pi i u\lambda},
\qquad -\frac12\le u\le\frac12,
\tag{4}
\]

and let `Lambda(W)` be the set of **distinct** support points of `W`. Its source Gram matrix is

\[
G_{\rm MT}(W)
:=
\bigl(\langle f_\lambda,f_\mu\rangle\bigr)_{\lambda,\mu\in\Lambda(W)},
\qquad
a(W):=\lambda_{\min}(G_{\rm MT}(W)).
\tag{5}
\]

Since `eta_MT>0` on the open interval and finite exponentials with distinct complex frequencies are linearly independent there, `G_MT(W)` is positive definite and

\[
\boxed{a(W)>0.}
\tag{6}
\]

For each nonreal representative define the destination defect created by collapsing the pair to its real center,

\[
d_z(\alpha)
:=e^{-2\pi i\alpha z}
 +e^{-2\pi i\alpha\bar z}
 -2e^{-2\pi i\alpha x_z}.
\tag{7}
\]

Let `D_s(W)` be the weighted defect Gram matrix

\[
D_s(W)
:=
\bigl(
\sqrt{m_zm_w}\,\langle d_z,d_w\rangle_s
\bigr)_{z,w\in Z_+(W)},
\qquad
b_s(W):=\lambda_{\max}(D_s(W)),
\tag{8}
\]

with `b_s(W)=0` when `W` is real. Define the cross-metric conditioning ratio

\[
\boxed{
\chi_s(W):=
\begin{cases}
 b_s(W)/a(W),& Z_+(W)\ne\varnothing,\\
 0,& Z_+(W)=\varnothing.
\end{cases}}
\tag{9}
\]

Then every `W` satisfies

\[
\boxed{
 d_{\rm sep}(W)^2
 \le
 \frac{\chi_s(W)}{2q_s}
 \frac{\Delta(W)}{L(W)}.
}
\tag{10}
\]

Thus the qualitative frontier of `ANF-088` becomes an exact quantitative dichotomy. If `W_j` is Montgomery--Taylor near-extremal in the relative sense

\[
\frac{\Delta(W_j)}{L(W_j)}\longrightarrow0
\tag{11}
\]

while remaining a fixed positive distance from the separable cone, then necessarily

\[
\boxed{\chi_s(W_j)\longrightarrow\infty.}
\tag{12}
\]

Conversely, on every class with a uniform bound `chi_s(W)<=C`,

\[
\boxed{
 d_{\rm sep}(W)
 \le
 \sqrt{\frac{C}{2q_s}}
 \sqrt{\frac{\Delta(W)}{L(W)}}.
}
\tag{13}
\]

So the near-extremizer-to-separable-cone implication is already closed for every uniformly cross-conditioned subclass. A surviving all-cardinality obstruction must make the source exponential system increasingly singular relative to the destination pair-collapse geometry.

## 1. The Montgomery--Taylor projection tax controls total nonreal multiplicity through `a(W)`

Use the notation of `ANF-088`. For `z in Z_+(W)`,

\[
g_z=\frac{f_z+f_{\bar z}}2,
\qquad
h_z=\frac{f_z-f_{\bar z}}{2i},
\tag{14}
\]

and `U` is spanned by the repeated-real `f_x` together with every symmetric nonreal vector `g_w`.

Take arbitrary `u in U`. Because the full family `{f_lambda}_{lambda in Lambda(W)}` is linearly independent, `u` has a unique coefficient vector in that family. If the coefficient of `g_z` in `u` is `c`, then the coefficients of `u` at the two frequencies `z,bar z` are both `c/2`. The corresponding coefficients of `h_z-u` are

\[
\frac1{2i}-\frac c2,
\qquad
-\frac1{2i}-\frac c2.
\tag{15}
\]

Their squared Euclidean mass is exactly

\[
\left|\frac1{2i}-\frac c2\right|^2
+
\left|-\frac1{2i}-\frac c2\right|^2
=
\frac12+\frac{|c|^2}{2}
\ge\frac12.
\tag{16}
\]

All other coefficients only increase the coefficient norm. By the definition of the smallest source-Gram eigenvalue,

\[
\|h_z-u\|_2^2
\ge
 a(W)\,\|\operatorname{coeff}(h_z-u)\|_{\ell^2}^2
\ge\frac{a(W)}2.
\tag{17}
\]

Taking the infimum over `u in U` gives

\[
\boxed{
\operatorname{dist}(h_z,U)^2\ge\frac{a(W)}2.
}
\tag{18}
\]

The exact projection tax in `ANF-088` contains

\[
4\sum_{z\in Z_+(W)}m_z\,\operatorname{dist}(h_z,U)^2.
\tag{19}
\]

Discarding all other nonnegative taxes and using (18),

\[
\boxed{
\Delta(W)
\ge
2a(W)M_{\rm nr}(W).
}
\tag{20}
\]

No restriction on real multiplicities, nonreal multiplicities, pair count, heights, horizontal collisions of real centers, or total cardinality is used. The only quantity allowed to deteriorate is the actual smallest Gram eigenvalue of the distinct source frequencies.

## 2. Real-part collapse turns the destination error into one finite defect Gram form

Construct the real-collapse multiset `P(W)` by leaving every real point of `W` unchanged and replacing each pair

\[
\{z^{(m_z)},\bar z^{(m_z)}\},
\qquad z=x_z+i y_z,
\tag{21}
\]

by `2m_z` copies of the real center `x_z`. Collisions between different centers or with pre-existing real sites are simply aggregated as multiplicities.

This preserves cardinality. It can only remove simple-real sites, never create a new simple site from a nonreal pair, so

\[
|P(W)|=|W|,
\qquad
\sigma(P(W))\le\sigma(W),
\qquad
L(P(W))\ge L(W).
\tag{22}
\]

The multiset `P(W)` is real and hence is a degenerate separable carrier in the comparison class of `ANF-086`. Its structure factor differs from that of `W` by exactly

\[
S_W-S_{P(W)}
=
\sum_{z\in Z_+(W)}m_zd_z.
\tag{23}
\]

Write `v_z:=sqrt(m_z)d_z`. Then (23) is the synthesis of the vectors `v_z` with coefficient vector `(sqrt(m_z))_z`. By the definition of the maximal defect-Gram eigenvalue,

\[
\begin{aligned}
\|S_W-S_{P(W)}\|_s^2
&\le
b_s(W)\sum_zm_z\\
&=b_s(W)M_{\rm nr}(W).
\end{aligned}
\tag{24}
\]

On the other hand the all-real certificate underlying `ANF-086` gives

\[
\|S_{P(W)}\|_s^2
=E_{F_s}(P(W))
\ge q_sL(P(W))
\ge q_sL(W).
\tag{25}
\]

Therefore the particular admissible comparator `P(W)` satisfies

\[
\delta_s(W\mid P(W))^2
\le
\frac{b_s(W)M_{\rm nr}(W)}{q_sL(W)}.
\tag{26}
\]

Combining (20) and (26), and then taking the infimum defining `d_sep`, proves (10):

\[
 d_{\rm sep}(W)^2
\le
\delta_s(W\mid P(W))^2
\le
\frac{b_s(W)}{2a(W)q_s}
\frac{\Delta(W)}{L(W)}.
\tag{27}
\]

The weights `sqrt(m_z)` in (8) are essential. Without them, repeated nonreal pairs would produce a quadratic coefficient loss in (23), while the projection tax (19) is naturally weighted linearly by multiplicity. The weighted defect Gram absorbs exactly that mismatch and makes (27) valid for arbitrary multiplicities.

## 3. Fatal central-notch configurations require explicit conditioning blow-up

Retain from `ANF-086`

\[
\rho_s:=\frac{C(J_s)}{C_{\rm MT}},
\qquad
\kappa_{\rm crit}:=1-\sqrt{\rho_s/q_s}>0.
\tag{28}
\]

Any configuration capable of defeating the fixed central-notch certificate must satisfy

\[
d_{\rm sep}(W)\ge\kappa_{\rm crit}.
\tag{29}
\]

If it is nonreal, then `Delta(W)>0` by `ANF-087`, and (10) forces

\[
\boxed{
\chi_s(W)
\ge
2q_s\kappa_{\rm crit}^2
\frac{L(W)}{\Delta(W)}.
}
\tag{30}
\]

This is the quantitative version of the “ill-conditioned exponential system” escape left by `ANF-088`. A sequence cannot simultaneously have relative Montgomery--Taylor excess tending to zero, a fixed positive separable-cone distance, and bounded cross-metric conditioning.

`ANF-086` also gives, for any fatal configuration,

\[
\frac{E_{\rm MT}(W)}{L(W)}
\le
\frac{\rho_s}{1-s}.
\tag{31}
\]

When

\[
\varepsilon_s
:=
\frac{\rho_s}{1-s}-1
\ge0,
\tag{32}
\]

this means `Delta(W)/L(W)<=varepsilon_s`. Hence every fatal configuration must obey the fixed conditioning threshold

\[
\boxed{
\chi_s(W)
\ge
\frac{2q_s\kappa_{\rm crit}^2}{\varepsilon_s}.
}
\tag{33}
\]

If `varepsilon_s<0`, `ANF-086` already rules out fatal configurations before this argument is needed. More generally, any subclass satisfying `chi_s(W)<=C` is completely screened whenever

\[
\boxed{
\frac{C\varepsilon_s}{2q_s}<\kappa_{\rm crit}^2.
}
\tag{34}
\]

Thus a proposed separated/Riesz subclass no longer needs a new bespoke energy proof. It is enough to control the explicit ratio `b_s/a` sharply enough to pass (34).

## 4. What the two Gram factors mean

The denominator `a(W)` measures source-side independence of the distinct Montgomery--Taylor exponential modes. It becomes small when those modes become nearly linearly dependent in `L^2(eta_MT^2 du)`. This includes the familiar nonharmonic-Fourier loss of conditioning as frequencies approach collisions, but the definition itself requires no separation hypothesis and remains exact for complex frequencies.

The numerator `b_s(W)` measures a different phenomenon: how coherently the pair-to-real-center defects can add in the **actual central-notch destination norm**. It therefore records vertical amplification, repeated-center coherence, and other effects that a source-only condition number would miss. The ratio in (9) is deliberately cross-metric. A small source Gram eigenvalue is harmless if the corresponding destination collapse defect shrinks even faster; conversely, a well-conditioned source family can still be unusable if destination defects amplify coherently.

This distinction prevents a false conclusion from generic Riesz theory. Classical Ingham inequalities give two-sided frame bounds for suitably separated real-frequency exponential families, while the nonharmonic-Fourier literature on clustered frequencies and divided differences describes how ordinary exponential bases lose conditioning as gaps collapse. Those are the correct neighboring tools for bounding `a(W)` or related synthesis constants in structured subclasses, but they do not by themselves control `b_s(W)` in the central-notch Fourier--Laplace norm. No external frame theorem is used in (10)--(34).

## 5. Adversarial checks and boundaries

The proof is finite-dimensional and has no hidden compactness passage. The positivity of `a(W)` uses only the exact interior positivity of `eta_MT` and linear independence of finitely many distinct exponentials, already used in `ANF-088`. The destination Gram `D_s(W)` is positive semidefinite because `J_s>=0`. Real-center collisions are allowed: they are handled inside the defect vectors before the Gram operator norm is taken. Arbitrary pair multiplicities are also allowed because the `sqrt(m_z)` weighting matches the exact multiplicity factor in the projection tax.

The bound is intentionally one-sided. A large `chi_s(W)` does **not** imply that `W` is a counterexample, near extremal, or far from the separable cone. It is only a necessary escape channel. Likewise, a tiny ordinary source Gram eigenvalue does not by itself signal danger: if `b_s` vanishes proportionally faster, the cross-metric ratio can remain small. This is particularly relevant near the real locus, where pair-collapse defects are second-order in the vertical displacement while conjugate exponentials themselves coalesce at first order.

Equation (10) does not prove a global uniform bound on `chi_s`, and therefore does not yet close the unrestricted all-cardinality complex branch. It also does not improve the zeta zero proportion or prove RH. What it does remove is the ambiguity in the phrase “conditioning-to-geometry”: the exact quantity that must blow up is now an explicit ratio of two finite Gram spectra, and every candidate obstruction can be tested against (30) or the stronger fixed-notch criterion (34).

## 6. Prior art and research consequence

The spectral estimates used here are elementary finite Gram-matrix inequalities. Classical Ingham/Riesz-sequence theory and the literature on divided differences of clustered exponentials are mature prior art for obtaining uniform frame constants under additional gap/density hypotheses; a targeted check found no theorem that identifies the Mathia-specific ratio `b_s/a`, relates Lamzouri's projection tax to the real-collapse defect in the central-notch norm, or supplies the fixed threshold (30). No external theorem is load-bearing, so `SOURCES.md` is unchanged.

The next gate is therefore sharply testable. Either prove that `chi_s(W)` stays below the threshold (33) on a sufficiently broad geometric class, using nonharmonic-Fourier/Riesz estimates for the source factor together with a destination defect-Bessel bound, or construct a growing family for which `chi_s` diverges at least as fast as `L/Delta` while the exact Montgomery--Taylor taxes remain small. Higher-order carriers remain unnecessary until such a genuinely cross-metric ill-conditioned family survives the separable-distance test.