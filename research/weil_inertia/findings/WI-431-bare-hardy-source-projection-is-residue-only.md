# WI-431 — bare Hardy source projection is residue-only; localization is an essential arithmetic gate

Status: `CLASSICAL-IDENTITY + EXACT-DERIVED + DECISIVE-BARRIER + PRIOR-ART-REDIRECT + NO-NOVELTY-CLAIM`

Parents: `WI-429`, `WI-430`

## Claim

`WI-429` identifies the positive-frequency Hardy projection of Kunik's interior Blaschke logarithmic derivative as an exact detector for zeros deeper than the probe line, and `WI-430` turns its positive energy into a quantitative defect counter. The remaining source-side problem has an important obstruction which can be made exact: **the bare global positive-frequency projection contains no independent prime-side component at all.** On a safe line the prime source is purely negative-frequency; after continuation toward the critical line, the positive-frequency component is precisely the inner/Blaschke residue data one is trying to bound.

Define the pole-cancelled logarithmic derivative

\[
F(s):=\frac{\zeta'(s)}{\zeta(s)}+\frac1{s-1}.
\tag{1}
\]

The addition removes the pole of \(\zeta'/\zeta\) at \(s=1\). Under the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
\tag{2}
\]

let \(P_+\) be the multiplier \(1_{\xi>0}\).

For every \(\sigma_0>1\), absolute convergence of the Euler/Dirichlet series gives

\[
F(\sigma_0+it)
=-\sum_{n\ge2}\Lambda(n)n^{-\sigma_0}e^{-it\log n}
+\frac1{\sigma_0-1+it}.
\tag{3}
\]

Every prime atom in (3) has frequency \(-\log n<0\), and the Cauchy term with positive real part also has Fourier support in \(\xi<0\). Hence, as an ordinary tempered distribution on every safe line,

\[
\boxed{P_+F(\sigma_0+i\,\cdot)=0,\qquad \sigma_0>1.}
\tag{4}
\]

Now put \(\sigma=1/2+a\) with \(0<a<1/2\). Kunik's exact logarithmic-derivative factorization is

\[
\frac{\zeta'(s)}{\zeta(s)}
=
\frac1s-\frac1{s-1}
-\frac1\pi\int_{-\infty}^{\infty}
\frac{\log|\zeta(\frac12+iu)|}{(s-\frac12-iu)^2}\,du
+\frac{B'(s)}{B(s)},
\qquad \Re s>\frac12.
\tag{5}
\]

After adding \(1/(s-1)\), both non-Blaschke terms on the right of

\[
F(s)=
\frac1s
-\frac1\pi\int_{-\infty}^{\infty}
\frac{\log|\zeta(\frac12+iu)|}{(s-\frac12-iu)^2}\,du
+\frac{B'(s)}{B(s)}
\tag{6}
\]

have negative-frequency Hardy orientation on the line \(\Re s=1/2+a\). Therefore the positive-frequency component is entirely the inner factor:

\[
\boxed{
P_+F(\tfrac12+a+i\,\cdot)
=
P_+\frac{B'}B(\tfrac12+a+i\,\cdot),
}
\tag{7}
\]

with the same localization/distributional qualification already recorded in `WI-429` for the full zeta object. For every finite Blaschke subproduct this is an ordinary \(L^2\) identity, and `WI-429` gives explicitly

\[
P_+\frac{B_F'}{B_F}(\tfrac12+a+it)
=
\sum_{d_j>a}\frac{m_j}{a-d_j+i(t-\gamma_j)}.
\tag{8}
\]

Equations (4) and (7)--(8) identify the source-side bottleneck sharply. Moving from \(\sigma_0>1\) to \(1/2+a\) does not uncover a hidden positive-frequency prime spectrum: the prime Dirichlet series starts entirely in the opposite Hardy half-space. The positive component that appears after continuation is exactly the zero/inner-factor residue content. Thus a proof which tries to upper-bound the `WI-429`/`WI-430` projected energy by simply projecting the unlocalized prime Dirichlet series has no arithmetic signal to use: before continuation that projection is identically zero, and after continuation the surviving component is the defect itself.

This does **not** rule out a source-side theorem. It rules out the bare translation-invariant projection shortcut. A non-oracular argument must introduce an operation which mixes the two Hardy half-spaces—most naturally height localization—or use genuinely additional arithmetic/analytic information. Once a window \(\chi\) is introduced, the exact identity

\[
\boxed{
P_+(\chi F)
=
\chi P_+F+[P_+,\chi]F
}
\tag{9}
\]

shows where the independent source information can enter. On a safe line, where \(P_+F=0\),

\[
\boxed{
P_+(\chi F)=[P_+,\chi]F.
}
\tag{10}
\]

All positive-frequency prime-side leakage is therefore created by the localization commutator. On an interior line, combining (7) and (9) gives

\[
\boxed{
\chi P_+\frac{B'}B
=
P_+(\chi F)-[P_+,\chi]F.
}
\tag{11}
\]

Consequently the localization/boundary term is not a technical nuisance that can be discarded after proving the global projection identity. It is the **essential arithmetic gate**: any viable upper bound for the localized defect energy must quantitatively control the commutator or an equivalent frequency-mixing term from data fixed independently of the off-line zeros.

## 1. Safe-line support is one-sided

For \(\sigma_0>1\), the classical identity

\[
\frac{\zeta'(s)}{\zeta(s)}
=-\sum_{n\ge2}\Lambda(n)n^{-s}
\tag{12}
\]

converges absolutely and locally uniformly. On the vertical line,

\[
n^{-(\sigma_0+it)}=n^{-\sigma_0}e^{-it\log n},
\]

so every von Mangoldt term is a Fourier atom at \(\xi=-\log n\). There are no positive-frequency prime atoms.

For \(c>0\), the Cauchy kernel used throughout `WI-429` satisfies

\[
\widehat{\frac1{c+i t}}(\xi)
=2\pi e^{c\xi}1_{\xi<0}.
\tag{13}
\]

Taking \(c=\sigma_0-1\) proves that the pole-cancelling elementary term in (3) is also negative-frequency. Equation (4) follows termwise without analytic continuation, zero-density input, or any hypothesis on zeros.

The cancellation at \(s=1\) in the definition of \(F\) is important. If one projects \(\zeta'/\zeta\) and \(1/(s-1)\) separately after moving to \(\sigma<1\), the Fourier orientation of the elementary Cauchy term changes. But the meromorphic pole at \(s=1\) cancels exactly in \(F\); it must not be mistaken for a zero-defect signal.

## 2. Kunik factorization assigns the opposite Hardy component to the inner factor

Equation (5) is Kunik's equation (2.39). On \(s=1/2+a+it\), the term \(1/s\) has a positive real-part Cauchy denominator and therefore lies in the negative Hardy half-space. The differentiated Poisson--Schwarz term is a superposition of squared kernels

\[
\frac1{(a+i(t-u))^2},
\]

which have the same negative-frequency support. Applying \(P_+\) to (6) therefore removes the entire outer/critical-line contribution and leaves (7).

For a finite Blaschke subproduct, the one-zero identity from `WI-429` is

\[
\frac{B_\rho'(s)}{B_\rho(s)}
=
\frac1{s-\rho}
-
\frac1{s-(1-\bar\rho)}.
\tag{14}
\]

If \(\rho=1/2+d+i\gamma\), then on the line \(1/2+a+it\) the reflected denominator always has positive real part, while the first denominator has negative real part precisely when \(d>a\). The Riesz projection therefore yields (8). In this finite setting no convergence issue is hidden in the argument.

For the full zeta Blaschke factor, (7) is best read as the same Hardy/distributional interface already isolated by `WI-429`, not as a new assertion that \(\zeta'/\zeta\) or \(B'/B\) belongs globally to ordinary \(L^2\). The present barrier does not need that stronger statement: its source-side half, (4), is exact on \(\sigma_0>1\), while Kunik's factorization identifies which factor can carry the opposite Hardy orientation after continuation.

## 3. Localization is mathematically essential, not merely regularization

Multiplication by a height window \(\chi(t)\) is non-translation-invariant. In frequency it convolves the one-sided spectrum with \(\widehat\chi\), so negative prime frequencies can leak into \(\xi>0\). Algebraically this is exactly the commutator in (9).

On \(\sigma_0>1\), equation (10) says that **all** positive-frequency content of the localized source is window-generated. In particular, any estimate of \(P_+(\chi F_{\sigma_0})\) is really an estimate of the Hardy commutator acting on an explicitly prime-generated negative-frequency source. That is a legitimate arithmetic object, but it is different from a global `P_+` norm.

On \(\sigma=1/2+a\), equation (11) shows what must be transported through analytic continuation or an explicit formula. The left side contains the deeper-zero signal from `WI-429`; the two terms on the right are accessible only if one can control both the localized source and the commutator/boundary correction without using those same zeros as input.

This identifies a concrete next target for the current program: choose a predetermined family of height windows \(\chi_T\) and probe depths \(a_n\downarrow0\), derive an exact localized version of (11), and prove a quantitative bound for the commutator/leakage term whose dependence on \(a_n,T\) is strong enough to compare with `WI-430`'s defect quantum. A source theorem that omits this term cannot be correct at the required level of independence.

## 4. Scope of the barrier

The no-go statement is deliberately narrow.

It closes the route

\[
\text{prime Dirichlet series}
\;\xrightarrow{\text{bare linear Hardy projection}}\;
\text{upper bound for deeper-defect energy},
\]

because the first arrow gives zero on every absolutely convergent safe line. It also explains why simply invoking analytic continuation does not create independent positive-frequency arithmetic data: Kunik's factorization assigns that component to the Blaschke inner factor.

It does **not** exclude:

- localized/windowed estimates, where frequency convolution and the commutator in (9) are the mechanism rather than an error to ignore;
- nonlinear source functionals or mixed-frequency moments;
- explicit-formula identities which keep both half-spaces and expose additional arithmetic terms;
- independent zero-density, mollifier, or correlation information that bounds the defect by a route not reducible to the bare projection;
- a direct complex-analytic source theorem strong enough to control (7), provided its hypotheses are independently verified rather than equivalent to the desired zero exclusion.

Thus `WI-430`'s global subquantum criterion remains diagnostically correct, but the immediate research priority changes. The next viable object is a **localized Hardy/commutator inequality**, not a global prime-side `P_+` energy.

## Prior art and novelty audit

No novelty or priority claim is made for the Hardy-space or factorization identities.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829v2 (2009), https://arxiv.org/abs/0804.4829. Equations (1.2)--(1.4) give the outer/Blaschke factorization in \(\Re s>1/2\), and equation (2.39) gives the logarithmic-derivative identity used in (5). Kunik explicitly places the construction in the Hardy/Poisson--Schwarz framework.
- Jean-François Burnol, *An adelic causality problem related to abelian L-functions*, Journal of Number Theory 87 (2001), 253--269; arXiv:math/0001013, https://arxiv.org/abs/math/0001013. Burnol's causality formulation is conceptually important prior art: bad zeros appear as poles of the scattering operator, and causality is equivalent to RH. This reinforces that an opposite-Hardy-space component created by continuation can itself encode the zero defect rather than supply independent source data.
- The Fourier support of Cauchy kernels, Paley--Wiener/Hardy decomposition, Riesz projections, and the commutator identity (9) are classical.
- `WI-429` already records the projected Blaschke identity and formally notes (7). `WI-430` records the resulting defect quantum. The repository-local advance here is the **barrier implication** obtained by combining that interface with the safe-line prime spectrum: the bare source projection is identically zero before continuation, so localization/frequency mixing is an essential source-side gate rather than optional regularization.

A targeted prior-art search around Kunik's factorization, Burnol's causality formulation, Hardy/Riesz projections of logarithmic derivatives, and zeta logarithmic-derivative bounds did not locate a source packaging this exact no-go statement for the current projected Kunik-energy program. Absence from that search is not used as evidence of priority.

## Stress tests and falsification

1. **The result is not an impossibility theorem for all source-side estimates.** A theorem bounding the interior projected term by independent arithmetic data could exist. The claim is that it cannot arise by taking the bare positive-frequency projection of the absolutely convergent prime Dirichlet series and carrying that unchanged across the strip.

2. **Localization is an escape, not a contradiction.** Multiplication by \(\chi\) does not commute with \(P_+\); the commutator in (9) is exactly why localized prime data can have positive frequencies even though the global source does not.

3. **No global \(L^2\) claim is imported.** Equations (4) and (12)--(13) are rigorous on \(\sigma_0>1\). Equations (7)--(8) use Kunik's factorization and the finite-product theorem of `WI-429`; any full-zeta norm statement still requires the localization/distributional convergence gate already recorded there.

4. **The pole at one is cancelled before the comparison.** This prevents the change of Hardy orientation of \(1/(s-1)\) across \(\sigma=1\) from being falsely interpreted as off-line-zero information.

5. **The barrier is falsified by an independent positive-frequency source term.** If an exact source decomposition in the relevant interior strip produces a positive-frequency arithmetic term not reducible to Blaschke residues or window/mixing corrections, then the conclusion must be revised. No such term appears in Kunik's canonical factorization.

## Consequence for the research line

The `WI-429`/`WI-430` detector remains useful, but its next proof obligation is now sharper. The source-side task is not to estimate a global positive-frequency prime norm—it is identically absent on the safe line. The task is to build and control a localized frequency-mixing bridge, with all commutator and boundary terms explicit, and then compare that genuinely independent arithmetic quantity against the finite-height defect coercivity of `WI-430`.
