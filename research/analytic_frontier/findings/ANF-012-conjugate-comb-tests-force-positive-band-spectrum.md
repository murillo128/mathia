# ANF-012 — conjugate-comb tests force a nonnegative compact-band spectrum

**Status:** `EXACT-DERIVED + CLASSICAL-BRIDGE + DECISIVE-NEGATIVE + STRUCTURAL-BOUNDARY`. For a scalar affine counting certificate that is universal over finite conjugation-invariant complex multisets, the high-multiplicity tests of `ANF-005` are much stronger than real-axis copositivity once the pair kernel has a continuous compactly supported Fourier profile. An explicit family of conjugate binomial combs can concentrate the corresponding spectral energy at any prescribed frequency in the band. Consequently the Fourier profile must be nonnegative everywhere. Thus **every universal affine scalar support-one certificate is automatically positive-definite on the real line; a signed spectral density is impossible even before the Montgomery--Taylor functional is optimized.**

## 1. Universal affine counting makes every conjugation-invariant pair energy nonnegative

Use the universal affine setup of `ANF-005`. Let `F : C -> C` be even and of real type and suppose that, for every nonempty finite multiset `Z` invariant under complex conjugation,

\[
s(Z)\ge A|Z|-E_F(Z),
\qquad
E_F(Z):=\sum_{z,w\in Z}F(z-w),
\tag{1}
\]

where `s(Z)` counts simple real elements.

Fix any such finite multiset `Z`. For an integer `M>=2`, multiply every multiplicity in `Z` by `M`; call the result `MZ`. No point of `MZ` is simple, so `s(MZ)=0`, while

\[
|MZ|=M|Z|,
\qquad
E_F(MZ)=M^2E_F(Z).
\]

Equation (1) gives

\[
0\ge AM|Z|-M^2E_F(Z),
\]

hence

\[
E_F(Z)\ge \frac{A|Z|}{M}.
\]

Letting `M -> infinity` yields the exact necessary condition

\[
\boxed{E_F(Z)\ge0\quad\text{for every finite conjugation-invariant multiset }Z.}
\tag{2}
\]

`ANF-005` used the same scaling only on real multisets and therefore obtained real translation-Gram copositivity. Equation (2) keeps the full complex-conjugation geometry.

## 2. Compact-band kernels turn (2) into a nonnegative spectral-energy condition

Assume now that, for some `B>0`,

\[
F(z)=\widehat J(z)
:=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\tag{3}
\]

where `J` is continuous, real and even. This includes the continuous support-one BGSST profiles relevant to `ANF-005` when `B=1`.

For real `alpha` define

\[
S_Z(\alpha):=\sum_{z\in Z}e^{-2\pi i\alpha z},
\tag{4}
\]

with multiplicities. Conjugation invariance gives

\[
S_Z(-\alpha)=\overline{S_Z(\alpha)}.
\tag{5}
\]

Therefore Fourier inversion inside the finite pair sum gives

\[
\begin{aligned}
E_F(Z)
&=\int_{-B}^{B}J(\alpha)
   S_Z(\alpha)S_Z(-\alpha)\,d\alpha\\
&=\boxed{\int_{-B}^{B}J(\alpha)|S_Z(\alpha)|^2\,d\alpha}.
\end{aligned}
\tag{6}
\]

So (2) says that `J` integrates nonnegatively against every spectral weight realizable by a finite conjugation-invariant positive atomic configuration. The remaining question is whether those weights can resolve an arbitrary point of the band. They can.

## 3. Conjugate binomial combs localize at any prescribed interior frequency

Set

\[
a:=\frac1{2B}.
\tag{7}
\]

For integers `m>=1` and parameters `y>=0`, take the conjugation-invariant multiset `Z_{m,y}` that has multiplicity `binom(m,j)` at each

\[
z_j=ja+iy
\quad\text{and}\quad
\bar z_j=ja-iy,
\qquad 0\le j\le m.
\tag{8}
\]

When `y=0`, the coincident conjugate copies are simply counted with doubled multiplicity. By the binomial theorem,

\[
S_{m,y}(\alpha)
=2\cosh(2\pi\alpha y)
  \left(1+e^{-2\pi i a\alpha}\right)^m.
\tag{9}
\]

Hence

\[
|S_{m,y}(\alpha)|^2
=4\cosh^2(2\pi\alpha y)
 \left[4\cos^2\!\left(\frac{\pi\alpha}{2B}\right)\right]^m.
\tag{10}
\]

Fix a target `alpha_0` with `0<alpha_0<B`, and put

\[
y_m=\tau m,
\qquad
\tau:=\frac1{4B}\tan\!\left(\frac{\pi\alpha_0}{2B}\right).
\tag{11}
\]

On `[0,B)` define

\[
\phi(\alpha)
:=4\pi\tau\alpha
 +\log\!\left[4\cos^2\!\left(\frac{\pi\alpha}{2B}\right)\right].
\tag{12}
\]

For `x>=0`, `(1/2)e^x <= cosh x <= e^x`. Thus the weight in (10) is trapped, up to constants independent of `m` and `alpha`, between positive multiples of `e^{m\phi(\alpha)}`. Moreover

\[
\phi'(\alpha)
=4\pi\tau-\frac{\pi}{B}
 \tan\!\left(\frac{\pi\alpha}{2B}\right),
\tag{13}
\]

and

\[
\phi''(\alpha)
=-\frac{\pi^2}{2B^2}
 \sec^2\!\left(\frac{\pi\alpha}{2B}\right)<0.
\tag{14}
\]

By (11), `phi'(alpha_0)=0`. Strict concavity makes `alpha_0` the unique maximum of `phi` on `[0,B)`. The even weight therefore has exactly two dominant points, `+/-alpha_0`.

This is a genuine concentration statement, not only a stationary-phase analogy. For every sufficiently small neighborhood `U` of `{+/-alpha_0}`, strict concavity gives an `eta>0` such that

\[
\sup_{[-B,B]\setminus U}\phi
\le \phi(\alpha_0)-\eta.
\tag{15}
\]

The uniform exponential bounds following (12) then show that the mass of (10) outside `U` is exponentially negligible compared with its mass in `U`.

If `J(alpha_0)<0`, continuity and evenness give a neighborhood `U` on which `J<=-epsilon<0`. Equation (15) then makes

\[
\int_{-B}^{B}J(\alpha)|S_{m,y_m}(\alpha)|^2\,d\alpha<0
\]

for all sufficiently large `m`, contradicting (2) and (6). Therefore

\[
J(\alpha_0)\ge0
\qquad(0<\alpha_0<B).
\tag{16}
\]

For `alpha_0=0`, take `tau=0`. Then the factor `[4 cos^2(pi alpha/(2B))]^m` has its unique maximum at zero, and the same concentration argument gives `J(0)>=0`. Continuity then supplies the endpoints. Consequently

\[
\boxed{J(\alpha)\ge0\qquad(-B\le\alpha\le B).}
\tag{17}
\]

## 4. The support-one affine branch is automatically positive-definite

For `B=1`, (17) applies directly to every continuous support-one profile in the global affine branch of `ANF-005`. By Bochner's theorem, the restriction `F|_R=\widehat J` is then a positive-definite translation-invariant kernel. Thus

\[
\boxed{
\text{universal affine complex counting}
+\text{continuous compact Fourier support}
\Longrightarrow
\text{nonnegative spectral profile / real-line PSD kernel}.
}
\tag{18}
\]

This is stronger than the real copositivity condition recorded in `ANF-005`. There, copositivity was correctly noted to be weaker than positive semidefiniteness for arbitrary real translation matrices. The missing information was the family of **complex conjugate** positive configurations. The vertical displacement in (8) supplies an exponential spectral tilt, while the binomial real comb supplies a narrow frequency window; together they recover every pointwise sign of `J`.

The word "signed" in the remaining support-one problem must therefore be interpreted carefully. The spatial kernel `F(x)` may still take negative values, and the normalization slack `delta` from `ANF-005` still pays for those dips. But the compact-band spectral profile `J` itself cannot change sign.

Accordingly, the unresolved extremal problem is now strictly narrower:

\[
J\ge0,\quad \operatorname{supp}J\subset[-1,1],\quad F=\widehat J,
\quad F(x)\ge-\delta,\quad F(iy)\ge1-\delta,
\tag{19}
\]

together with the remaining universal constraints, and the improvement target

\[
M(F)+\delta<m_{\rm MT}.
\tag{20}
\]

Equation (17) alone does **not** imply `F(x)>=0`; therefore it does not by itself invoke the Carneiro--Chandee--Littmann--Milinovich nonnegative-spatial-kernel extremal theorem or close (20).

## 5. Relation to the out-of-band obstruction

`ANF-010` showed that a scalar PSD Gram construction cannot combine with a Cohn--Elkies negative spectral tail, because PSD already demands a nonnegative spectral measure. `ANF-011` then removed PSD from that particular out-of-band argument: any nontrivial negative tail beyond the known band drives `F(iy)` to `-infinity` and violates the isolated conjugate-pair floor.

The present result closes a different loophole. Even **inside a compact band**, one cannot evade scalar PSD structure by choosing an indefinite spectral profile and hoping that the full universal affine inequality survives. The universal complex-configuration inequality itself forces spectral positivity through (2)--(17).

`ANF-011` remains genuinely necessary for noncompact Fourier--Laplace profiles. The binomial comb in (10) localizes within a fixed compact band; it is not a replacement for the outer-tail dominance argument when arbitrarily large frequencies remain present.

Together the two results sharpen the routing:

- compact-band universal affine scalar certificates are automatically spectrally positive;
- useful negative out-of-band tails are incompatible with the universal affine scalar template;
- any escape based on a genuinely signed spectrum must therefore leave universal affine scalar pair counting, for example through pre-compression matrix/inertia information, local ordered configurations, higher-order observables, or a zeta-specific inequality that does not quantify over arbitrary conjugation-invariant multisets.

## 6. Prior art and novelty boundary

Bochner's theorem and the Fourier characterization of translation-invariant positive-definite functions are classical. A directly relevant complex extension is Jorge Buescu, A. C. Paixão and A. Symeonides, **Complex Positive Definite Functions on Strips**, *Complex Analysis and Operator Theory* 11:3 (2017), 627--649, DOI `10.1007/s11785-015-0527-y`, which characterizes holomorphic positive-definite strip functions as Fourier--Laplace transforms of positive exponentially finite measures and places Bochner and Widder in one framework.

Those theorems start from positive definiteness and characterize its representing measure. They do not supply the step needed here: deriving spectral positivity from the much more asymmetric hypothesis (1), which only tests positive multiplicities and only on conjugation-invariant multisets. The binomial-comb argument is the explicit bridge from that counting hypothesis to (17).

A targeted search of positive-definite/Fourier--Laplace and copositive-kernel literature did not locate this exact universal-affine counting reduction. No publication-level novelty claim is made. The durable Mathia contribution is the structural boundary (18) and the resulting narrowing of the live support-one extremal problem.

## 7. Decisive audit boundary

The theorem is conditional only on explicit structural hypotheses: universality of (1), conjugation invariance of the admissible finite multisets, and a continuous real-even compactly supported profile `J` giving (3). A counterexample would have to break one of the exact steps above: either produce a conjugation-invariant multiset with negative energy despite (1) and multiplicity scaling, violate the spectral identity (6), or find `J(alpha_0)<0` while all binomial-comb energies remain nonnegative despite the concentration in (10)--(15).

The result does not cover discontinuous/singular spectral measures without an approximation argument, noncompact spectra, a certificate valid only for actual zeta-zero configurations, or any genuinely non-affine/configuration-level functional. Those are precise exits rather than hidden gaps in (17).