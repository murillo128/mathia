# WP-215 — Bost–Connes state-Hamiltonian filters can encode prime powers, but critical Weil weights force a sharp half-Hölder threshold

**Status:** `DERIVED + EXACT + BOST-CONNES-HAMILTONIAN + DISCRETE-SPECTRUM + POSITIVE-SMOOTH-INTERPOLATION + TARGET-CODING-CONTROL + CRITICAL-HALF-DENSITY + SHARP-HOLDER-ONE-HALF-THRESHOLD + UNBOUNDED-DERIVATIVE + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

The correction in `WP-214` separates the dense Liouville/time-grade generator from the standard Bost–Connes state Hamiltonian. On the canonical `ell^2(N)` representation,

\[
H\varepsilon_n=(\log n)\varepsilon_n,
\qquad
\operatorname{Spec}(H)=\{\log n:n\ge1\},
\]

and this spectrum is discrete in every bounded energy interval. Consequently there is **no continuity obstruction at all** to selecting prime powers by scalar functional calculus of `H`: any prescribed nonnegative sequence `a_n` can be interpolated by a nonnegative `C^infinity` function `F` with

\[
F(\log n)=a_n.
\]

In particular, smooth positive `F(H)` can encode the prime-power indicator, `Lambda(n)`, or the critical finite-Weil amplitude

\[
a_n=\frac{\Lambda(n)}{\sqrt n}.
\]

This apparent escape is a matched control, not a Mathia-native positivity mechanism. The interpolation works just as well for an arbitrary subset of the integers with arbitrary prescribed nonnegative weights; the arithmetic content is put into `F` by hand.

The critical amplitude nevertheless has an exact regularity signature. For every odd prime `p>3`, at least one of `p+1` and `p+3` is **not** a prime power. Choose such an integer `m_p`. Then

\[
1\le m_p-p\le3,
\qquad
\Lambda(m_p)=0,
\]

and

\[
0<\log m_p-\log p
\le \log(1+3/p)
\le \frac3p.
\]

An exact state-Hamiltonian Weil selector must therefore change from

\[
F(\log p)=\frac{\log p}{\sqrt p}
\]

to `F(log m_p)=0` across an energy interval of length at most `3/p`. It follows that

\[
\boxed{
F\text{ cannot be globally Holder-}\alpha
\text{ for any }\alpha\ge\frac12.
}
\]

Conversely, for every fixed `0<alpha<1/2`, an explicit disjoint-bump construction gives a nonnegative bounded `C^infinity` interpolant with the exact critical values that **is** globally Holder-`alpha`. Thus `1/2` is a genuine sharp regularity threshold for target-coded scalar interpolation on the integer-log spectrum, not merely a one-sided obstruction.

If `F` is `C^1`, the mean-value theorem gives points `xi_p` between `log p` and `log m_p` with

\[
\boxed{
|F'(\xi_p)|
\ge
\frac{\sqrt p\log p}{3}.
}
\]

Every smooth exact interpolation of the critical Weil amplitudes therefore develops increasingly steep, increasingly narrow spectral transitions. Smoothness by itself does not make the selector regular in any global scale that controls the accumulating high-energy gaps.

This is the opposite failure mode from `WP-214`: on the Liouville grading continuity is too rigid to select prime powers; on the state Hamiltonian continuity is so permissive that it can encode arbitrary arithmetic data. The only nontrivial constraint visible at the critical half-density is the exact half-Hölder threshold, and even that does not make the selector canonical.

## 1. The standard Hamiltonian has a discrete integer-log spectrum

Bost and Connes' standard representation uses the orthonormal basis `epsilon_n`, `n>=1`, with

\[
H\varepsilon_n=(\log n)\varepsilon_n.
\tag{1}
\]

For any bounded interval `[A,B]`, the condition `log n in [A,B]` implies `e^A<=n<=e^B`, so only finitely many eigenvalues occur. Hence

\[
\Sigma_H:=\{\log n:n\in\mathbb N\}
\tag{2}
\]

is a closed discrete subset of `R`.

This differs fundamentally from the Liouvillean

\[
L=H\otimes I-I\otimes H,
\]

whose rational-log point spectrum contains `log(a/b)` and is dense. The density theorem in `WP-214` therefore cannot be transferred from `L` to `H`.

## 2. Every nonnegative sequence admits a smooth positive state-Hamiltonian interpolant

Let `a_n>=0` be arbitrary. Because every point `log n` is isolated, choose radii `r_n>0` so that the intervals

\[
I_n=(\log n-r_n,\log n+r_n)
\tag{3}
\]

are pairwise disjoint. Choose nonnegative `C^infinity` bumps `phi_n` supported in `I_n` and normalized by

\[
\phi_n(\log n)=1.
\tag{4}
\]

Then

\[
F(E):=\sum_{n\ge1}a_n\phi_n(E)
\tag{5}
\]

is well defined and `C^infinity`: the supports are disjoint, hence the sum is locally finite. Moreover

\[
F(E)\ge0,
\qquad
F(\log n)=a_n.
\tag{6}
\]

Consequently the spectral theorem gives

\[
F(H)\varepsilon_n=a_n\varepsilon_n.
\tag{7}
\]

There is nothing specifically arithmetic in this construction. If `S subset N` is random, composite-only, squarefree-only, or chosen after seeing the desired answer, setting `a_n=1_S(n)b_n` with arbitrary `b_n>=0` produces the corresponding positive smooth spectral selector just as easily.

Three controls are immediate:

\[
a_n=\mathbf1_{\{n\text{ prime power}\}},
\tag{8}
\]

\[
a_n=\Lambda(n),
\tag{9}
\]

and

\[
a_n=\frac{\Lambda(n)}{\sqrt n}.
\tag{10}
\]

All have smooth nonnegative interpolants. The last sequence is bounded and tends to zero, so (5) can also be chosen bounded.

This proves that **positivity, self-adjointness, boundedness, and even `C^infinity` scalar functional calculus are not a canonicity test on the discrete state spectrum**.

## 3. A uniformly nearby non-prime-power exists beside every large prime

The quantitative obstruction requires no prime-gap theorem.

Let `p>3` be an odd prime. Then `p+1` and `p+3` are both even. If an even integer is a prime power, its prime base must be `2`, so it is a power of two. But two powers of two greater than `4` cannot differ by `2`: if `2^a<2^b` with `a>=3`, then

\[
2^b-2^a\ge2^a\ge8.
\]

Since `(p+3)-(p+1)=2`, the two integers cannot both be prime powers. Therefore at least one choice

\[
m_p\in\{p+1,p+3\}
\tag{11}
\]

satisfies

\[
\Lambda(m_p)=0.
\tag{12}
\]

Its energy distance from the prime eigenvalue obeys

\[
0<\Delta_p
:=\log m_p-\log p
=\log\!\left(1+\frac{m_p-p}{p}\right)
\le\frac3p.
\tag{13}
\]

Thus the desired arithmetic support alternates between a prime eigenvalue and a guaranteed zero-weight eigenvalue at an exponentially shrinking energy separation `O(e^{-E})` when `E=log p`.

## 4. Raw support and Mangoldt weight already destroy uniform continuity

For the indicator selector (8), exact interpolation gives

\[
|F(\log p)-F(\log m_p)|=1
\tag{14}
\]

while `Delta_p->0`. Therefore no exact continuous interpolant of the prime-power indicator can be uniformly continuous on `R`.

For the raw Mangoldt selector (9),

\[
|F(\log p)-F(\log m_p)|=\log p,
\tag{15}
\]

so uniform continuity fails even more strongly. If `F` is differentiable, the mean-value theorem and (13) force

\[
\sup_{\xi\in(\log p,\log m_p)}|F'(\xi)|
\ge \frac{p\log p}{3}.
\tag{16}
\]

Hence a smooth state-energy function can encode these sequences only by becoming arbitrarily steep at high energy.

## 5. Critical half-density forbids every Holder exponent at or above one-half

The finite Weil amplitude is different because its prime value decays:

\[
a_p=\frac{\log p}{\sqrt p}\longrightarrow0.
\tag{17}
\]

Suppose `F` is globally Holder-`alpha` with finite constant `C`:

\[
|F(x)-F(y)|\le C|x-y|^\alpha.
\tag{18}
\]

Exact matching of (10), together with (12)--(13), gives

\[
\frac{\log p}{\sqrt p}
=|F(\log p)-F(\log m_p)|
\le C\left(\frac3p\right)^\alpha.
\tag{19}
\]

Equivalently,

\[
p^{\alpha-1/2}\log p
\le C3^\alpha.
\tag{20}
\]

For `alpha>1/2`, the left side diverges polynomially; for `alpha=1/2`, it diverges logarithmically. Thus

\[
\boxed{
F\notin C^{0,\alpha}_{\rm global}(\mathbb R)
\qquad\text{for every }\alpha\ge\frac12.
}
\tag{21}
\]

In particular no globally Lipschitz selector exists.

If `F` is `C^1`, applying the mean-value theorem directly to (19) yields some `xi_p` with

\[
|F'(\xi_p)|
\ge
\frac{(\log p)/\sqrt p}{3/p}
=
\boxed{\frac{\sqrt p\log p}{3}}.
\tag{22}
\]

Writing `E_p=log p`, the forced derivative scale is

\[
|F'(\xi_p)|\gtrsim E_p e^{E_p/2}.
\tag{23}
\]

The exponent `1/2` is source-relevant: the target amplitude `p^{-1/2}` is being compared with an adjacent integer-log gap of order `p^{-1}`, and the extra `log p` makes the endpoint itself impossible.

## 6. Below one-half the target-coded Holder interpolation exists

The threshold in (21) is exact for scalar interpolation. Fix

\[
0<\alpha<\frac12.
\tag{24}
\]

Choose, for example,

\[
r_n:=\frac1{10n}.
\tag{25}
\]

The intervals `I_n=(log n-r_n,log n+r_n)` are pairwise disjoint. Indeed

\[
\log(n+1)-\log n
=\log(1+1/n)
\ge\frac1{n+1},
\tag{26}
\]

while

\[
r_n+r_{n+1}
=\frac1{10}\left(\frac1n+\frac1{n+1}\right)
<\frac1{n+1}.
\tag{27}
\]

Take one fixed nonnegative `C^infinity` bump `phi`, supported in `(-1,1)`, with `0<=phi<=1` and `phi(0)=1`, and set

\[
F_\alpha(E)
:=\sum_{n\ge1}
\frac{\Lambda(n)}{\sqrt n}
\phi\!\left(\frac{E-\log n}{r_n}\right).
\tag{28}
\]

The sum is locally finite and nonnegative, and

\[
F_\alpha(\log n)=\frac{\Lambda(n)}{\sqrt n}.
\tag{29}
\]

A fixed smooth compactly supported bump is globally Holder-`alpha`; under the rescaling in (28), the Holder seminorm of the `n`th term is bounded by a constant times

\[
\frac{\Lambda(n)}{\sqrt n}\,r_n^{-\alpha}
\ll
\Lambda(n)n^{\alpha-1/2}.
\tag{30}
\]

Since `Lambda(n)<=log n` and `alpha-1/2<0`,

\[
\sup_{n\ge2}
\Lambda(n)n^{\alpha-1/2}
<\infty.
\tag{31}
\]

The disjoint supports and their uniformly comparable gap scale then give a global Holder-`alpha` bound for the sum. Concretely, points in the same support use (30); points crossing a support boundary compare to the zero boundary value; points in distinct supports are controlled by the sum of those two boundary estimates and the intervening distance.

Therefore

\[
\boxed{
\forall\,0<\alpha<\frac12
\quad\exists\quad
F_\alpha\ge0,
\quad
F_\alpha\in C^\infty\cap L^\infty\cap C^{0,\alpha}_{\rm global},
}
\tag{32}
\]

with the exact critical values (29).

Together (21) and (32) give the exact threshold

\[
\boxed{
\alpha_{\rm critical}=\frac12,
\quad\text{with the endpoint excluded by the factor }\log p.
}
\tag{33}
\]

In particular the critical selector can be smooth, bounded, and uniformly continuous; every `F_alpha` with `alpha>0` already has those properties. What it cannot have is global Holder regularity of order `1/2` or better. Its smooth derivatives must become unbounded as quantified by (22).

This is a matched control, not a new positive mechanism. The construction explicitly uses `Lambda(n)` in (28), and the same bump scheme realizes arbitrary bounded target sequences with corresponding gap-compatible regularity.

## 7. Why this is not a Weil-positive geometry

The operator `F_alpha(H)` from (28) is positive and bounded, but its positivity is tautological: `F_alpha` was prescribed to be nonnegative after the Mangoldt data were supplied. Nothing in the state Hamiltonian distinguishes (28) from an arbitrary control sequence.

It also produces only a diagonal positive state-energy weight. It does not generate the conventional finite Weil translation/autocorrelation orientation, the Euler-Gamma archimedean term, the polar/global counterterms, or a global sign theorem. Feeding (29) into a later construction must still survive the same support, orientation, mixed-prime, and finite--archimedean audits as any other inserted coefficient list.

The result therefore rejects a tempting but invalid inference:

\[
\text{canonical }H
+\text{ positive smooth }F(H)
+\text{ exact Weil coefficients}
\not\Rightarrow
\text{Mathia-native positivity}.
\tag{34}
\]

The exact coefficients can be achieved because the discrete spectrum permits arbitrary interpolation, not because the geometry forced them.

## 8. Aggressive falsification and exact scope

**Does continuity alone forbid a state-Hamiltonian prime-power selector?** No. Section 2 constructs smooth nonnegative selectors explicitly. This is the correction complementary to `WP-214`.

**Does uniform continuity forbid the critical half-density selector?** No. Section 6 constructs globally Holder selectors for every exponent below `1/2`.

**Is the half-Hölder barrier merely one-sided?** No. Equations (21) and (32) show that `1/2` is the exact threshold for this target-coded interpolation problem.

**Does `C^infinity` regularity rescue canonicity?** No. Smooth bumps can be arbitrarily narrow. Equation (22) shows that exact critical interpolation forces unbounded derivatives despite smoothness.

**Could a source-defined function with less than half-Hölder regularity nevertheless be canonical?** Logically yes. The theorem does not rule out an independently forced rough function. It says that matching the critical arithmetic sequence then requires precisely this regularity regime, which must be derived rather than hand-designed.

**Could non-scalar coupling evade this diagnosis?** Yes. The theorem classifies only scalar functional calculus of the standard state Hamiltonian. A matrix-valued, cohomological, boundary, or finite--archimedean coupling may use `H` before scalarization and remains subject to separate tests.

**Does this prove or assume RH?** No. It uses only the standard Bost–Connes Hamiltonian, the elementary support of `Lambda`, and the adjacent-integer estimate (13).

## 9. Prior-art and novelty boundary

No novelty is claimed for the Bost–Connes Hamiltonian, its logarithmic spectrum, smooth bump interpolation on a closed discrete subset, Holder regularity, or the mean-value theorem. Bost and Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica 1 (1995), 411–457, DOI `10.1007/BF01589495`, is already recorded in `SOURCES.md` as the classical system anchor.

A directed audit of the Bost–Connes Hamiltonian/time-evolution literature confirms the standard representation (1) and the distinction between state energies `log n` and operator time grades generated by energy differences. No novelty claim depends on absence of prior literature discussing prime-power interpolation.

The durable Mathia-specific delta is the exact matched-control classification produced by applying those standard facts to the current Weil-positivity problem: scalar state-Hamiltonian calculus can encode arbitrary prime-power data smoothly and positively, while the exact critical Weil amplitude has the sharp global Holder threshold `alpha=1/2` and forces derivative spikes at least of size `sqrt(p) log p/3`. This separates target-coded spectral interpolation from a source-forced geometric selector.

This is not a new spectral realization of zeta, not a positivity proof, and not evidence for RH.

## Consequence for the research frontier

Together `WP-214` and `WP-215` close a semantic ambiguity in the Bost–Connes escape. On the dense Liouville grading, regular scalar calculus cannot select prime powers. On the discrete state Hamiltonian, scalar calculus can select essentially anything, so positivity and smoothness carry no arithmetic content; exact critical weights merely impose the sharp half-Hölder roughness threshold.

A surviving construction must therefore obtain the Mangoldt support from structure **before** arbitrary scalar interpolation is available, or derive a particular rough/singular selector from an independent theorem. It must also couple that finite information to the real place and the global defect terms before invoking a sign theorem. Merely choosing a positive function of the canonical Hamiltonian is now a matched control, not a bridge.