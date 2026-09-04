# WI-144 — coherent Hilbert multi-window lifts remain Fourier-positive and cannot realize the CGdL tail sign

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-143 rules out positive convex mixtures and Hilbert direct sums of scalar Lamzouri windows as a route to the Chirre--Gonçalves--de Laat (CGdL) RH gain: their squared real-gap kernels stay in a Fourier-positive autocorrelation cone, whereas the CGdL improvement uses a dual profile with a genuinely favorable non-positive tail outside the range where Montgomery's pair-correlation asymptotic is available. A natural remaining escape is to put several windows coherently into one vector- or matrix-valued Hilbert feature and hope that cross-channel interference creates the missing tail sign.

That escape also fails for two broad positive-Hilbert subclasses. First, an arbitrary vector-valued translation feature inside a **single positive Hilbert inner product collapses exactly to one scalar Lamzouri window**: only its pointwise squared norm survives in the Gram kernel. Second, even if one retains a positive-semidefinite operator-valued spectral density and only scalarizes after forming the translation Gram, its natural Hilbert--Schmidt/Frobenius energy has a pointwise nonnegative Fourier transform. Thus coherent common-Hilbert recombination and Frobenius matrix-channel lifts do not enlarge the tail-sign class relevant to the CGdL transplant.

The boundary is essential. This finding does **not** prove that every joint multi-profile certificate is Fourier-positive. A more general sign-indefinite scalarization of matrix entries can have a signed Fourier profile, and genuinely nonlinear joint constraints need not reduce to either subclass below. The surviving route therefore has to leave the positive single-feature/Frobenius architecture in a mathematically substantive way and prove a new finite zero-side inequality that remains valid for the off-critical blocks.

## 1. A coherent vector-valued single feature collapses exactly to a scalar window

Let `E` be a finite-dimensional complex Hilbert space and let

\[
\psi:\mathbb R\longrightarrow E
\]

be compactly supported and square-integrable. Normalize

\[
\int_{\mathbb R}\|\psi(u)\|_E^2\,du=1,
\tag{1}
\]

and impose the same parity/support restrictions needed in the Lamzouri proposition through the scalar norm profile. Form the translation/modulation features

\[
f_z(u):=\psi(u)e^{-2\pi i z u}\in L^2(\mathbb R;E).
\tag{2}
\]

With the usual Hilbert inner product, their kernel is

\[
\langle f_z,f_s\rangle
 =\int_{\mathbb R}\|\psi(u)\|_E^2
 e^{-2\pi i(z-\overline s)u}\,du.
\tag{3}
\]

Lamzouri's conjugation-adapted relabeling converts the same kernel into the displayed square-kernel statistic in Proposition 2.1; the distinction between `z-s` and `z-\bar s` is only the standard conjugation bookkeeping and is immaterial for the collapse below.

Set

\[
q(u):=\|\psi(u)\|_E^2\ge0,
\qquad
\eta_{\rm eff}(u):=\sqrt{q(u)}.
\tag{4}
\]

Then

\[
\eta_{\rm eff}(u)^2=q(u),
\qquad
K_\psi(\xi)=\widehat q(\xi)
             =K_{\eta_{\rm eff}}(\xi).
\tag{5}
\]

Equation (5) is an identity of the **entire complex kernel**, not just of its restriction to real gaps. Support, normalization, and evenness of the norm profile pass directly from `psi` to `eta_eff`. Consequently every finite Hilbert inequality obtained by inserting the coherent vector-valued feature (2) into the same positive projection/Bessel argument is literally the scalar Lamzouri inequality for `eta_eff`.

This closes a stronger class than WI-143. Arbitrary channel phases, rotations, and coherent mixing inside `psi(u)` disappear because a positive Hilbert inner product contracts the channel index pointwise to `||psi(u)||^2`. To make the spectral density signed at this stage one would have to replace (4) by a signed quantity, which cannot be a squared Hilbert norm and therefore is no longer a consequence of the same positive-Hilbert proof.

## 2. Retaining matrix channels still leaves Frobenius energy Fourier-positive

One can avoid the scalar collapse (5) by retaining channel information in an operator-valued translation kernel. Let

\[
W(u)\succeq0
\tag{6}
\]

be an integrable compactly supported Hermitian matrix-valued density and define

\[
K(x):=\int_{\mathbb R}W(u)e^{-2\pi i xu}\,du.
\tag{7}
\]

For real gaps `x`, consider the natural quadratic Hilbert energy

\[
G(x):=\|K(x)\|_{\rm HS}^2
     =\operatorname{Tr}(K(x)K(x)^*).
\tag{8}
\]

Expanding (8) gives

\[
G(x)=\iint_{\mathbb R^2}
 \operatorname{Tr}(W(u)W(v))
 e^{-2\pi i x(u-v)}\,du\,dv.
\tag{9}
\]

With the Fourier convention

\[
\widehat G(\alpha)=\int_{\mathbb R}G(x)e^{-2\pi i\alpha x}\,dx,
\]

Fourier inversion/Fubini in (9) yields

\[
\boxed{
\widehat G(\alpha)
 =\int_{\mathbb R}
   \operatorname{Tr}(W(u)W(u+\alpha))\,du
 \ge0.
}
\tag{10}
\]

The inequality is pointwise: for positive-semidefinite matrices `A,B`,

\[
\operatorname{Tr}(AB)
 =\operatorname{Tr}(A^{1/2}BA^{1/2})\ge0.
\tag{11}
\]

In the rank-one case `W(u)=a(u)a(u)^*`, (10) becomes the especially transparent identity

\[
\widehat G(\alpha)
 =\int_{\mathbb R}
   |\langle a(u),a(u+\alpha)\rangle|^2\,du
 \ge0.
\tag{12}
\]

The same obstruction holds for every positive scalar compression. For a fixed vector `v`,

\[
q_v(u):=v^*W(u)v\ge0,
\qquad
v^*K(x)v=\widehat{q_v}(x),
\]

so the Fourier transform of `|v^*K(x)v|^2` is the autocorrelation of the nonnegative density `q_v` and is pointwise nonnegative. Positive sums or integrals of these energies remain pointwise nonnegative on the Fourier side.

There is also a representation-theoretic proof of (10). Any translation-covariant positive operator-valued Gram can be written abstractly as

\[
K(t)=V^*U_tV
\tag{13}
\]

for a unitary representation `U_t`. Put `T=VV^*`. Then the Frobenius energy is a matrix coefficient of the conjugation representation on Hilbert--Schmidt operators,

\[
G(t)
 =\operatorname{Tr}(T U_t T U_t^*)
 =\langle T,\operatorname{Ad}(U_t)T\rangle_{\rm HS}.
\tag{14}
\]

Hence `G` is positive-definite and Bochner's theorem gives a positive Fourier measure. Equation (10) is the concrete density version. Operator-valued Bochner theorems are classical; for a modern Fourier-feature formulation see H.Q. Minh, *Operator-valued Bochner theorem, Fourier feature maps for operator-valued kernels*, arXiv:1608.05639. No novelty is claimed for this functional-analytic identity.

## 3. Exact clash with the CGdL transplant target

WI-143 reconstructed the relevant sign mechanism in Chirre--Gonçalves--de Laat's RH pair-correlation SDP. Their improvement is not obtained by another Fourier-positive autocorrelation kernel of Montgomery--Taylor type. It uses the nonnegativity of the form factor to tolerate, and then discard in the favorable direction, a genuinely non-positive dual tail outside the interval on which the pair-correlation asymptotic is known.

The two coherent Hilbert extensions above cannot manufacture that sign pattern:

\[
\psi\hbox{ coherent single feature}
\quad\Longrightarrow\quad
q=\|\psi\|^2\ge0
\quad\Longrightarrow\quad
\text{ordinary scalar Lamzouri kernel},
\tag{15}
\]

while

\[
W\succeq0,\quad
G=\|\widehat W\|_{\rm HS}^2
\quad\Longrightarrow\quad
\widehat G(\alpha)
 =\int\operatorname{Tr}(W(u)W(u+\alpha))du
 \ge0.
\tag{16}
\]

A positive Fourier profile can agree with the required non-positive tail only by vanishing there. That reverts to the compact-support/support-limited situation rather than importing the CGdL tail gain. Therefore simply replacing Lamzouri's scalar window by a coherent vector window, a common positive Hilbert feature, or a PSD matrix channel measured by its Frobenius/Hilbert energy cannot transfer the CGdL `67.92%` mechanism to the unconditional proof.

This is a structural obstruction, not a numerical optimization failure. No choice of the number of channels, channel phases, pointwise unitary mixing, or PSD matrix weight changes (5) or the sign in (10).

## 4. Falsification boundary: not every joint quadratic scalarization is covered

It would be incorrect to infer from (10) that **every** nonnegative quadratic statistic built from matrix entries has a pointwise nonnegative Fourier transform. Let

\[
r(u)=\sum_{i,j}c_{ij}W_{ij}(u)
\tag{17}
\]

for coefficients `c_ij` that do not define a positive scalar compression. Then

\[
\left|\sum_{i,j}c_{ij}K_{ij}(x)\right|^2
 =|\widehat r(x)|^2\ge0,
\tag{18}
\]

but its Fourier transform is the autocorrelation

\[
(r*\widetilde r)(\alpha),
\tag{19}
\]

which need not be pointwise nonnegative when `r` is signed or complex. Thus positivity of a real-gap cost by itself is **not** enough to force the tail-sign obstruction. What matters in (10) is the stronger PSD-channel/Frobenius structure, or in (5) the fact that the density is literally a squared Hilbert norm.

Accordingly this finding does not close:

- genuinely nonlinear joint constraints retaining several profile statistics rather than collapsing them to one Hilbert norm;
- sign-indefinite cross-window scalarizations for which a new finite zero-side inequality can nevertheless be proved;
- matrix-valued statistics outside positive scalar compressions and Frobenius/Hilbert--Schmidt energy;
- source-specific arithmetic restrictions on the zeta zero configuration;
- wider Fourier support when independently justified by established arithmetic input.

In particular, the live `CLUE-higher-zero-correlations-horizontal-rigidity` is not resolved. The result only removes another superficially attractive positive-Hilbert implementation of its remaining `joint profile` direction.

## 5. Prior-art and novelty audit

The load-bearing finite zero-side input is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882, Proposition 2.1. Its scalar feature kernel is exactly the object from which (5) is abstracted. The comparison target is Emanuel Carneiro/Chirre--Gonçalves--de Laat's pair-correlation SDP architecture as reconstructed from Chirre--Gonçalves--de Laat, *Pair correlation estimates for the zeros of the Riemann zeta-function*, Math. Comp. (2018), especially the test-function step used in the simple-zero application. WI-143 records the exact scalar sign mismatch and should be read as the immediate predecessor.

The operator-valued positive-definite framework is classical Bochner theory. H.Q. Minh, arXiv:1608.05639, is an explicit modern operator-valued Bochner/Fourier-feature reference; it supports the classification of (13)--(14) as classical rather than new mathematics.

A public `teal-sea/zeta-lab` frontier-math audit already records the broader scalar obstruction: Gram/autocorrelation feature families do not reproduce the oscillatory CGdL dual tail, and positive sums do not repair the sign. Therefore no priority is claimed here for the scalar observation, for the CGdL transplant bottleneck, or for operator-valued Bochner theory. The Mathia contribution is the exact closure of two natural proposed escapes left open by WI-143: **arbitrary coherent vector mixing inside one positive Hilbert feature collapses to a scalar window, and the natural PSD operator-valued/Frobenius lift remains Fourier-positive.**

A search over the current `weil_inertia` corpus found no earlier finding proving these two closures. WI-143 treats positive scalar mixtures/direct sums but explicitly leaves genuinely joint profiles open. The present result narrows that surviving class while preserving the falsification boundary in Section 4.

## 6. Research consequence

The following routes should now be treated as closed unless some additional non-Hilbert or arithmetic ingredient is introduced:

1. package many scalar Lamzouri windows as channels of one coherent vector-valued translation feature and feed the result through the same positive projection/Bessel inequality;
2. retain PSD matrix-valued translation channels but collapse them through Frobenius/Hilbert--Schmidt energy or positive scalar compressions in an attempt to obtain the CGdL negative Fourier tail;
3. increase the number of such positive channels and optimize their mixing while expecting a qualitative change of tail sign.

A viable joint-profile escape must instead do something that (5) and (10) deliberately exclude: keep several observables coupled nonlinearly, use a sign-indefinite cross-window form backed by a new finite zero-side inequality that controls the off-critical conjugation blocks, or import genuinely new arithmetic information. This is a decisive barrier for the positive-Hilbert version of the multi-profile program, but it neither improves the present certified proportion nor bounds the uncertified complement by itself.

## Classification

- **Classical identity:** positive Hilbert Gram kernels and operator-valued translation kernels admit Bochner/Fourier-feature representations; Hilbert--Schmidt coefficients have positive Fourier measure.
- **Literature-backed input:** Lamzouri Proposition 2.1 and the CGdL RH SDP/simple-zero mechanism, with the scalar transplant obstruction already present in public `zeta-lab` prior art.
- **Exact deduction:** coherent vector-valued single-feature lifts collapse identically to `eta_eff=sqrt(||psi||^2)`, and PSD operator-valued Frobenius energies satisfy the pointwise nonnegative Fourier identity (10).
- **Decisive barrier:** those two broad positive-Hilbert multi-window architectures cannot synthesize the CGdL favorable non-positive tail.
- **Not claimed:** impossibility of every joint/matrix-valued certificate, any new numerical simple-zero proportion, or any restriction on sign-indefinite cross-channel statistics beyond the finite inequalities actually proved here.
