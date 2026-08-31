# WP-071 — rotation-invariant Hilbert completions cannot both contain a cyclotomic shell and bound the Mangoldt boundary anchor

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + MATHIA-SHELL-SPECIALIZATION`. This finding closes a concrete scalar-positive escape left by WP-067--WP-070. The functional-analysis ingredients are elementary and standard; no theorem-level historical novelty is claimed. The Mathia-specific content is that the canonical Prime-Circle cyclotomic logarithms and their exact Mangoldt readout at `z=1` are incompatible with *every* positive rotation-invariant Hilbert completion in which that boundary readout is represented by a bounded finite-energy anchor.

WP-067 identified the exact shell functional

\[
L(\Gamma_n)=\Lambda(n),
\]

while WP-068/WP-069 showed that `L` is unbounded in the base Hardy geometry and that a successful positive repair must genuinely change the finite topology. A natural remaining possibility is therefore to replace the Hardy norm by another positive weighted-Hardy/Fourier-multiplier Hilbert norm while preserving the rotational symmetry of the disk and making the arithmetic anchor at `z=1` continuous.

That entire class is impossible. Let `\mathcal H` be a Hilbert completion of analytic polynomials such that

1. rotations
   \[
   (U_\theta f)(z)=f(e^{i\theta}z)
   \]
   act unitarily;
2. every monomial `z^m` has nonzero norm;
3. polynomial evaluation at the canonical boundary point,
   \[
   \operatorname{ev}_1(p)=p(1),
   \]
   extends to a bounded functional on `\mathcal H`.

Then **no nontrivial Mathia cyclotomic shell function**

\[
F_n(z)=\operatorname{Log}\Phi_n(z),\qquad n>1,
\]

belongs to `\mathcal H`.

Equivalently: merely changing the radial/rotation-invariant positive Fourier weights cannot turn the exact Mangoldt boundary readout into a finite-energy vector while retaining even one canonical cyclotomic logarithm. Any scalar-positive completion that keeps the shell functions and makes their Mangoldt anchor continuous must break rotation symmetry in the *metric/topology itself*, restrict to a non-ambient shell quotient/subspace, or leave this Hilbert/RKHS architecture.

## 1. Exact Mathia bridge: Mangoldt is boundary evaluation of the shell logarithm

Prime Circle gives, for every `n>1`, the analytic disk function

\[
F_n(z)=\operatorname{Log}\Phi_n(z)
=-\sum_{m\ge1}\frac{c_n(m)}m z^m,
\tag{1}
\]

where `c_n(m)` is the Ramanujan sum. The corresponding Hankel shell is `\Gamma_n`; PC-075 and WP-067 identify the same coefficients on the operator side.

At the distinguished boundary point `z=1`, the elementary cyclotomic identity is

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\\
1,&n>1\text{ is not a prime power},
\end{cases}
\]

so

\[
\boxed{F_n(1)=\log\Phi_n(1)=\Lambda(n).}
\tag{2}
\]

Thus the exact arithmetic functional of WP-067 is not an arbitrary coefficient insertion: on the analytic shell model it is literally the canonical boundary evaluation at `1`.

The question is whether a different positive rotation-invariant Hilbert geometry can make this evaluation bounded while keeping the same shell functions as finite-energy states.

## 2. Rotation invariance forces a diagonal monomial geometry

Because the rotations are unitary,

\[
\langle z^m,z^k\rangle
=\langle U_\theta z^m,U_\theta z^k\rangle
=e^{i(m-k)\theta}\langle z^m,z^k\rangle
\]

for every `\theta`. Hence

\[
\boxed{\langle z^m,z^k\rangle=0\qquad(m\ne k).}
\tag{3}
\]

Write

\[
w_m:=\|z^m\|_{\mathcal H}^2>0.
\]

Then every polynomial satisfies

\[
\left\|\sum_{m=0}^M a_m z^m\right\|_{\mathcal H}^2
=\sum_{m=0}^M w_m|a_m|^2.
\tag{4}
\]

Therefore every positive rotation-invariant Hilbert repair of this scalar analytic type is, after notation, a weighted coefficient space. No assumption about a power law, Sobolev order, or monotonicity of the weights is needed below.

## 3. A bounded boundary anchor forces reciprocal weights to be summable

Assume `ev_1` is bounded with norm at most `C`. For each `M`, use the polynomial

\[
p_M(z)=\sum_{m=0}^M\frac{1}{w_m}z^m.
\]

Let

\[
S_M:=\sum_{m=0}^M\frac1{w_m}.
\]

By (4),

\[
\|p_M\|_{\mathcal H}^2=S_M,
\qquad
p_M(1)=S_M.
\]

Boundedness of `ev_1` gives

\[
S_M^2\le C^2S_M,
\]

hence `S_M\le C^2` for every `M`. Therefore

\[
\boxed{\sum_{m\ge0}\frac1{w_m}<\infty.}
\tag{5}
\]

This is the finite-energy requirement for the Riesz vector representing boundary evaluation at `1`.

## 4. Every cyclotomic logarithm forces the opposite summability on an arithmetic progression

Fix any `n>1`. On the subsequence `m=n\ell`, the Ramanujan sum in (1) is

\[
c_n(n\ell)=\varphi(n),
\]

so the shell coefficients satisfy

\[
\left|[z^{n\ell}]F_n\right|
=\frac{\varphi(n)}{n\ell}.
\tag{6}
\]

If `F_n\in\mathcal H`, equations (4) and (6) force

\[
\sum_{\ell\ge1}w_{n\ell}\frac{\varphi(n)^2}{n^2\ell^2}<\infty,
\]

or equivalently

\[
\boxed{\sum_{\ell\ge1}\frac{w_{n\ell}}{\ell^2}<\infty.}
\tag{7}
\]

But (5) also implies

\[
\sum_{\ell\ge1}\frac1{w_{n\ell}}<\infty.
\tag{8}
\]

Applying Cauchy--Schwarz to the harmonic series gives

\[
\sum_{\ell=1}^M\frac1\ell
=\sum_{\ell=1}^M
\frac{\sqrt{w_{n\ell}}}{\ell}\,
\frac1{\sqrt{w_{n\ell}}}
\]

and therefore

\[
\sum_{\ell=1}^M\frac1\ell
\le
\left(\sum_{\ell\ge1}\frac{w_{n\ell}}{\ell^2}\right)^{1/2}
\left(\sum_{\ell\ge1}\frac1{w_{n\ell}}\right)^{1/2}.
\tag{9}
\]

The right-hand side is finite and independent of `M` by (7)--(8), while the left-hand side diverges. Contradiction.

Hence

\[
\boxed{
\operatorname{ev}_1\text{ bounded on }\mathcal H
\quad\Longrightarrow\quad
F_n\notin\mathcal H\ \text{for every }n>1.
}
\tag{10}
\]

This is stronger than the null-sequence obstruction of WP-068 for this symmetry class: one does not need a carefully assembled full-root control. A **single** cyclotomic logarithm already conflicts with a bounded boundary anchor once positivity and full rotation invariance fix the ambient Hilbert geometry.

## 5. Geometric reading: pointing the functional is not enough; the metric must be pointed

Equation (10) has a simple boundary interpretation. If `ev_1` is bounded and rotations are unitary, then for every `\zeta=e^{i\theta}` the functional

\[
\operatorname{ev}_\zeta(f)=\operatorname{ev}_1(U_\theta f)
\]

is bounded with the same norm. Thus a rotation-invariant positive boundary-RKHS topology cannot make only the arithmetic point `1` regular: it makes the entire boundary orbit equally regular.

But `F_n=\operatorname{Log}\Phi_n` has logarithmic singularities precisely at the primitive `n`-th roots of unity. The coefficient proof above is the rigorous form of this geometric mismatch. The arithmetic selector is obtained by **pointing the readout at `1`**, whereas the shell itself stores cyclotomic root data all around the unit circle. If the positive topology remains rotationally homogeneous, making the pointed readout finite-energy regularizes every rotated copy and expels the shell.

This sharpens the survivor left by PC-037. Breaking rotation only in the *functional* does not suffice. A successful scalar-positive route must break it already in the metric, domain, quotient, or coupling.

## 6. Matched power-weight control shows the critical gap transparently

For the familiar one-parameter family

\[
w_m\asymp m^\alpha,
\]

a cyclotomic shell has, on the subsequence `m=n\ell`, energy bounded below by a constant multiple of

\[
\sum_{\ell\ge1}\ell^{\alpha-2},
\]

so shell membership requires

\[
\alpha<1.
\]

In contrast, bounded boundary evaluation requires

\[
\sum_m m^{-\alpha}<\infty,
\]

hence

\[
\alpha>1.
\]

At `\alpha=1` both conditions fail logarithmically. The arbitrary-weight proof above shows that this is not an artifact of choosing a Sobolev/power scale: no irregular redistribution of positive rotation-invariant Fourier weights can bridge the gap.

The full-root controls of WP-068 give the same qualitative diagnosis from the opposite direction. Their generating function

\[
F_N(z)=\log\frac{1-z^N}{1-z}
\]

has `F_N(1)=\log N`; normalizing by `\log N` keeps the boundary anchor order one while the Hardy energy tends to zero. WP-071 shows that strengthening the entire rotation-invariant positive coefficient topology enough to bound that boundary anchor necessarily makes the individual primitive shell logarithms infinite-energy.

## 7. Adversarial and prior-art audit

This finding does **not** claim that weighted Hardy/RKHS evaluation criteria are new. Orthogonality of Fourier modes under unitary rotations, the Riesz criterion for evaluation, and the cyclotomic/Ramanujan coefficient identities are classical. The substantive result for this research line is the exact specialization and no-go:

\[
\text{Mathia cyclotomic shell}
+\text{rotation-invariant positive Hilbert metric}
+\text{finite-energy }z=1\text{ anchor}
\quad\text{are mutually incompatible.}
\]

It is not a reformulation of Weil positivity, Hilbert--Polya, Connes trace formulas, Sonin localization, or a zero-defined spectral criterion: no zeta zero data enter. It also differs from WP-039, which rules out translation-invariant **Markov/Dirichlet** symbols with Mangoldt support. Here the obstruction applies to arbitrary positive rotation-invariant scalar Hilbert weights and uses the cyclotomic shell singularity plus the exact boundary anchor.

The result survives a matched non-arithmetic control: any analytic function with coefficients bounded below by `c/m` on an infinite arithmetic progression obeys the same incompatibility. Thus the obstruction is geometric/functional-analytic, not an RH-specific arithmetic miracle. That is a feature of the negative result: it precisely identifies which natural positive completion is too symmetric to carry the arithmetic distinction.

## 8. Boundaries and surviving routes

The theorem deliberately does **not** rule out the following.

- A bounded functional on the **closed shell span only** that agrees with `\Lambda(n)` on the generators but is not the restriction of ambient point evaluation. WP-067 already isolates this as a separate Riesz-representer question.
- A positive Hilbert metric that is genuinely **non-rotation-invariant** and privileges the arithmetic point or a Mathia-native finite/archimedean coupling.
- Matrix-valued, internal, graded, Krein-to-positive-after-reduction, cohomological, or intersection-theoretic structures in which scalar boundary evaluation is not the primitive operation.
- Semidefinite quotient constructions that collapse part of the monomial ambient space, provided the quotient is canonical and the Mangoldt readout remains well-defined.
- Singular anchor nets, test-dependent auxiliary sectors, or nonlinear selectors, subject to the main README requirement that the eventual Weil form and its sign be intrinsic rather than fitted.
- A construction that couples finite and archimedean sectors **before** taking the Hilbert completion, so that neither the isolated shell norm nor isolated `ev_1` exists as assumed here.

These boundaries are important: WP-071 closes the rotation-invariant scalar ambient repair, not every possible changed finite geometry.

## 9. Consequence for the Weil-positivity search

WP-067--WP-070 showed that the canonical Hardy metric and its direct `q=2` positive partner leave the exact Mangoldt anchor unbounded. WP-071 now rules out the broadest obvious repair that preserves scalar positivity and rotational homogeneity while merely reweighting Fourier modes.

The remaining scalar-positive route has therefore become more specific:

\[
\boxed{
\text{if the arithmetic anchor is point-like at }1,
\text{ the positive geometry itself must also be pointed/non-homogeneous.}
}
\]

That symmetry breaking must be Mathia-native, survive the non-arithmetic controls in the README, keep the exact cyclotomic/Mangoldt selector continuous, and still supply the archimedean and polar counterterms before a global independent sign theorem is invoked. Merely selecting `z=1` after constructing a rotation-invariant positive energy cannot do it.

## 10. Falsification criterion

WP-071 is falsified by an explicit Hilbert completion `\mathcal H` of analytic polynomials satisfying all three assumptions above -- unitary full-circle rotations, nonzero monomials, and bounded ambient `ev_1` -- for which some `F_n=\operatorname{Log}\Phi_n`, `n>1`, has finite norm. Such an example would have to invalidate one of (3), (5), (6), or the Cauchy--Schwarz implication (9).

A non-rotation-invariant space, a shell-only quotient, or a functional that agrees with `\Lambda(n)` on shell generators without being ambient evaluation at `1` is **not** a counterexample; those are explicitly outside the claim and remain candidates for further research.

## Dependencies

- `research/prime_circle/findings/PC-075-cyclotomic-log-hankel-core-is-universal-hilbert-channels.md` — exact `\operatorname{Log}\Phi_n` / Ramanujan-coefficient shell representation.
- `research/prime_circle/findings/PC-037-rotation-invariant-harmonic-forms-collapse-to-divisor-tails.md` — prior symmetry-collapse boundary and motivation to distinguish a pointed functional from a pointed metric.
- `research/weil_positivity/findings/WP-067-base-shell-hardy-canonical-zero-finite-part-is-indefinite.md` — exact Hardy shell Gram and `L(\Gamma_n)=\Lambda(n)`.
- `research/weil_positivity/findings/WP-068-full-root-hardy-differences-make-mangoldt-anchor-functional-unbounded.md` — canonical full-root null controls.
- `research/weil_positivity/findings/WP-069-positive-hardy-extensions-cannot-carry-unbounded-mangoldt-anchor-at-finite-energy.md` — finite-energy-anchor obstruction and changed-topology escape.
- `research/weil_positivity/findings/WP-070-q2-antipodal-hardy-correction-is-blind-to-odd-full-root-controls.md` — failure of the most canonical positive reflection correction.
- `research/weil_positivity/README.md` — canonical research mandate and control requirements.