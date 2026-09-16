# WI-321 — Hilbert-valued channelization cannot contract a scalar Weil semibound

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-311, WI-317, WI-320.

WI-320 closes adaptive scalar feedback for the smooth **real** multiwindow localization class developed in WI-311: a single short nonnegative test has nonnegative source-exact localization defect for every admissible real localizer, so feeding the same scalar lower semibound into all localized copies cannot strictly improve that scalar constant. A natural apparent escape is to allow complex phases or finitely many auxiliary channels and hope that phase-sensitive autocorrelations carry information unavailable to real windows.

They do not, as long as the channels are only a representation of the same scalar source and every localized channel is estimated by the same scalar semibound. The exact sliding identity extends to finite-dimensional complex Hilbert-valued windows. Its defect is obtained by replacing the real factor `(1-R(a))H_f(a)` by

\[
\operatorname{Re}\!\left((1-R(a))h_f(a)\right),
\]

where `R` is now the complex Hilbert-valued autocorrelation and `h_f` is the full complex autocorrelation of the test. On the same short real nonnegative witness used in WI-320, `h_f(a)` is real and nonnegative. Cauchy--Schwarz gives `Re R(a) <= |R(a)| <= 1`, so the defect is again nonnegative for **every** complex channelization, even if the channelization is chosen after seeing the test.

Consequently complex phases, finite auxiliary channel dimension, and unitary mixing of those channels do not escape the scalar-bootstrap obstruction. A surviving vector/mode localization route must carry genuinely non-scalar information between scales -- for example a coupled matrix lower bound, prime-dependent state, or another invariant not reducible to applying the same scalar semibound componentwise.

## 1. Complex channelized localization and its exact source identity

Fix an outer aperture `L>0`. Let `K` be a finite-dimensional complex Hilbert space and let

\[
G\in C_c^\infty((-1/2,1/2);K),
\qquad
\int_{\mathbb R}\|G(u)\|_K^2\,du=1.
\tag{1}
\]

Choosing an orthonormal basis of `K` writes `G=(g_1,\ldots,g_J)` and recovers a finite complex multiwindow family. For `f\in C_c^\infty((-L,L);\mathbb C)` define the channelized translated localization

\[
F_y(u):=G(u)f(u+y)\in K.
\tag{2}
\]

Let `Q_K` denote the diagonal Hilbert-space amplification of the scalar Weil form,

\[
Q_K(F):=\sum_{j=1}^J Q(F_j).
\tag{3}
\]

This definition is independent of the chosen orthonormal basis by polarization, so a unitary change of channel coordinates cannot change any conclusion below.

The norm identity is exact:

\[
\int_{\mathbb R}\|F_y\|_{L^2(K)}^2\,dy
=\|f\|_2^2.
\tag{4}
\]

Write the full scalar autocorrelation

\[
h_f(a)=\int_{\mathbb R}f(v+a)\overline{f(v)}\,dv
\tag{5}
\]

and the channel autocorrelation

\[
R_G(a)=\int_{\mathbb R}
\langle G(u),G(u+a)\rangle_K\,du,
\tag{6}
\]

with the convention chosen so that the component formula is

\[
R_G(a)=\sum_j\int g_j(u+a)\overline{g_j(u)}\,du
\]

up to harmless complex conjugation. Only real parts will enter. Direct compact-support Fubini gives the basis-free identity

\[
\int_{\mathbb R}\sum_j h_{g_j(\cdot)f(\cdot+y)}(a)\,dy
=R_G(a)h_f(a).
\tag{7}
\]

The frozen Liu source used in WI-304 and WI-320 defines the classical Weil form on arbitrary complex smooth tests and expresses every translated source contribution through the real part of `h_f`. Therefore the same source calculation as WI-311, without imposing reality on the localizer, gives

\[
Q(f)=\int_{\mathbb R}Q_K(F_y)\,dy-\mathcal E_G(f),
\tag{8}
\]

where

\[
\begin{aligned}
\mathcal E_G(f)
={}&\int_0^{2L}K_0(a)
\operatorname{Re}\!\left((1-R_G(a))h_f(a)\right)\,da\\
&+\sum_{\log n<2L}
\frac{2\Lambda(n)}{\sqrt n}
\operatorname{Re}\!\left((1-R_G(\log n))h_f(\log n)\right),
\end{aligned}
\tag{9}
\]

and

\[
K_0(a)=
\frac{2e^{-a/2}}{1-e^{-2a}}-4\cosh(a/2).
\tag{10}
\]

For real windows, `R_G` is real and (9) reduces exactly to WI-320 equation (8). Thus (9) is not a new source model; it is the complex polarization of the already audited source-exact localization identity.

## 2. The same short witness kills all complex phases and channels

Let `rho>1` be the real root of

\[
\rho^3-\rho-1=0,
\]

and put

\[
h_0=\log\rho.
\]

WI-320 derives exactly

\[
K_0(a)>0\quad(0<a<h_0),
\qquad
h_0<\log2.
\tag{11}
\]

Choose

\[
0<d<\min\{2L,h_0\}
\tag{12}
\]

and a nonzero real nonnegative

\[
f\in C_c^\infty((-L,L))
\]

supported in an interval of diameter strictly smaller than `d`. Then

\[
h_f(a)=\int f(v+a)f(v)\,dv\ge0
\tag{13}
\]

and

\[
h_f(a)=0\qquad(a\ge d).
\tag{14}
\]

Since `d<h_0<log 2`, equation (14) annihilates every prime-power term in (9) exactly.

Bundle the channels in the single unit vector `G\in L^2(\mathbb R;K)`. Translation is unitary, so Cauchy--Schwarz and (1) imply

\[
|R_G(a)|\le1,
\qquad
\operatorname{Re}R_G(a)\le1.
\tag{15}
\]

On the chosen real witness, (13) gives

\[
\operatorname{Re}\!\left((1-R_G(a))h_f(a)\right)
=(1-\operatorname{Re}R_G(a))h_f(a)\ge0.
\tag{16}
\]

Using (11), (14) and the exact vanishing of the arithmetic sum, (9) becomes

\[
\boxed{
\mathcal E_G(f)
=\int_0^d
K_0(a)(1-\operatorname{Re}R_G(a))h_f(a)\,da
\ge0.
}
\tag{17}
\]

The same fixed `f` works for every finite-dimensional `K` and every normalized smooth complex `G`. No phase choice can make the defect negative on this witness.

## 3. Scalar feedback still cannot contract

Assume the only lower estimate supplied to the localized channels is the same scalar semibound

\[
Q(h)\ge-c\|h\|_2^2
\tag{18}
\]

for every scalar complex test `h`. Applying (18) componentwise in any orthonormal basis of `K` and using (4) yields

\[
\int Q_K(F_y)\,dy
\ge-c\|f\|_2^2.
\tag{19}
\]

Combining (8) and (19),

\[
Q(f)\ge-c\|f\|_2^2-\mathcal E_G(f).
\tag{20}
\]

Even if the auxiliary dimension and `G` are chosen adaptively after observing `f`, a strict uniform contraction to `c-kappa` with `kappa>0` would require, for every nonzero `f`, some admissible channelization satisfying

\[
\mathcal E_G(f)\le-\kappa\|f\|_2^2.
\tag{21}
\]

But the single short nonnegative witness above satisfies (17) for every admissible `G`. Hence (21) fails for every `kappa>0`:

\[
\boxed{
\text{finite complex Hilbert-valued channelization cannot strictly improve a scalar Weil semibound by reusing that semibound componentwise.}
}
\tag{22}
\]

This includes arbitrary finite complex multiwindow families, arbitrary complex phases, arbitrary finite channel number, carrier-frequency modulation, and any unitary rotation of the channel coordinates. The obstruction is pointwise in the chosen localizer, so no compactness, frequency budget, derivative bound or finite portfolio is needed.

## 4. Why this is stronger than the real-window no-go but not a no-go for non-scalar state

WI-320 was deliberately stated for the exact admissible class established in WI-311: finite smooth **real** multiwindow families. Equation (22) removes the two most immediate representational escapes. First, multiplying windows by complex phases does not help, because on the falsifying test only `Re R_G` survives and it is still at most one. Second, introducing an auxiliary channel space does not help if `Q` is merely amplified diagonally and the same scalar lower bound is applied in each channel.

This sharpens what the live `vector/matrix/mode-dependent state` route has to mean. Merely storing the same scalar copy in several channels is not additional mathematical information. A genuine escape must use something not reducible to (18)--(19), for example a matrix-valued lower bound with nontrivial cross-channel terms, a prime- or mode-dependent state whose admissible region is smaller than the product of scalar semibounds, a source estimate that distinguishes channels arithmetically, or a different decomposition whose correction is not governed by (9).

The result therefore separates **representation dimension** from **information content**. Increasing the former alone does not evade the scalar localization barrier.

## 5. Stress tests and boundary of the theorem

**Complex tests are legal.** Liu's frozen manuscript defines `D_L=C_c^infty((-L,L);C)` and states the classical Weil form for arbitrary complex smooth tests. The extension above does not apply a real-only positivity theorem to complex localized pieces.

**The imaginary autocorrelation is retained until the decisive witness.** For a general complex `f`, the defect is (9), not `(1-Re R_G)H_f`; the imaginary parts of `R_G` and `h_f` can interact. The simplification occurs only after choosing the real nonnegative short witness, where `h_f(a)` is real and nonnegative. Thus no phase-sensitive term has been silently discarded.

**The pole/archimedean contribution is not omitted.** It is already part of the audited source kernel `K_0` in WI-304/WI-320. The proof uses the exact positive interval of that full continuous localization defect, not a prime-only surrogate.

**Every arithmetic atom vanishes exactly.** The witness diameter is below `h_0<log 2`, while every prime-power lag is at least `log 2`. No density, asymptotic or truncation estimate is used.

**Adaptive channelization is allowed.** The same witness works after the localizer is chosen, because (17) holds pointwise for every normalized `G`. The auxiliary dimension may vary with the localizer, provided it is finite and the source identity remains the diagonal Hilbert-space amplification above.

**Genuinely coupled vector estimates are outside the theorem.** If the localized state carries a matrix inequality, cross-channel covariance, prime labels, or another constraint stronger than applying (18) separately to each component, equation (19) is no longer the complete information being propagated. Such mechanisms remain open and are precisely the kind of additional information demanded by the research mandate.

**More general source-breaking localizations are outside the theorem.** A rule whose windows depend on the translation parameter in a way that destroys (7), or whose localized form is not the diagonal amplification of the original source, requires a new exact source identity and is not covered by (22).

## 6. Prior-art and novelty audit

The load-bearing source identity is literature-backed by Vincent Liu, **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, frozen source commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`. That manuscript explicitly works on arbitrary complex smooth tests and supplies the source normalization used in WI-304 and WI-320. WI-311 derives the real multiwindow source-exact localization identity, and WI-320 supplies the short-support sign witness and the exact plastic-constant interval.

The passage from scalar windows to a finite auxiliary Hilbert space is standard Hilbert-space packaging; the only analytic estimate needed is the ordinary Cauchy--Schwarz bound for translation autocorrelations. Generic IMS/localization literature likewise treats channel decompositions and partitions of unity as standard localization machinery. A targeted audit around complex IMS localization, Hilbert/vector-valued localization, source-exact Weil autocorrelation defects, and adaptive scalar-semibound bootstraps found the generic localization framework and Liu's scalar source identity, but no source stating the Weil-specific complex-channel obstruction (17)--(22). Search absence is not a priority claim.

The Mathia contribution here is therefore narrow and exact: it identifies the correct complex defect `Re((1-R_G)h_f)` and shows that the WI-320 prime-free positive bump annihilates every phase/channel escape that still propagates only the same scalar semibound.

## 7. Consequence for the Weil-inertia program

The scalar-localization no-go is not an artifact of insisting on real windows. It survives finite complex channelization exactly. This removes a cheap interpretation of the current `vector/matrix/mode` escape hatch: a useful non-scalar state must change the information propagated, not merely the representation in which the same scalar inequality is written.

The surviving RH-facing question is correspondingly sharper. One needs a source-justified invariant whose localized admissible set is strictly smaller than the Cartesian product of scalar semibounds, or a genuinely different coercivity/inertia mechanism. Complex phase freedom and finite channel multiplicity alone cannot supply the missing defect-to-zero bootstrap.