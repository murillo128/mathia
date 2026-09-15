# PC-302 — oriented cross-frame repair is mode-reversal gauge or sine-Fourier covariance

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the simplest oriented-frame escape left open by PC-301.

PC-301 shows that the centered same-source carrier `G_s=Z_s^*X_s` satisfies `G_{-s}=G_s`, so arbitrary source correlations cannot recover orientation after that contraction. It leaves a natural earlier intervention open: retain the oriented Fourier frames themselves and compare two distinct source frames before forming a same-source Gram matrix.

That repair has a sharp split. At the level of **unlabelled frame/subspace geometry or positive cross-frame spectral data**, source reflection is still an exact gauge: it merely reverses the latent Fourier-mode labels `m<->-m`. The first labelled component that genuinely changes under an individual source reflection is nonzero, but it is exactly a finite sine cross-Gram. Under the canonical same-law source average it becomes a positive Gram matrix of the imaginary parts of the ordinary additive Fourier transform of the source law. For the prime source this is therefore classical additive exponential-sum data over primes, not a new zeta spectral variable.

Thus retaining the frames before `G_s` is mathematically richer than PC-301's sign quotient, but the **simplest quadratic repair** does not yet escape the classical Fourier packet. A further mechanism must use a geometrically justified chirality/mode label, higher joint information, or a different cross-level carrier before positive compression.

Let `q` be an odd prime,

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and retain the symmetric low-frequency packet

\[
S_M=\{\pm1,\ldots,\pm M\},\qquad 2M<q.
\]

As in PC-296, define

\[
x_{m,s}(h)=N^{-1/2}e^{2\pi i msh/q},
\qquad h\in H_B,
\]

and let `X_s` be the `N x 2M` matrix with columns `x_{m,s}`, `m in S_M`. Let

\[
c_d:=\frac1N\sum_{h=-B}^{B}e^{2\pi i dh/q}.
\tag{1}
\]

The centered window gives

\[
c_{-d}=c_d\in\mathbb R.
\tag{2}
\]

For two source residues define the oriented cross-frame overlap

\[
H_{p,r}:=X_p^*X_r,
\qquad
\boxed{(H_{p,r})_{n,m}=c_{mr-np}.}
\tag{3}
\]

The same conclusions hold for the `Z` frames. To include the actual boundary-log low-mode weights, let

\[
W=-D=\operatorname{diag}_{m\in S_M}w_m,
\qquad w_m:=-a_q(m)>0,
\]

so `w_{-m}=w_m`, and put

\[
R_{p,r}:=W^{1/2}H_{p,r}W^{1/2}.
\tag{4}
\]

## 1. Reflection is exactly latent mode reversal

Let `J` be the unitary involution on the latent mode space defined by

\[
Je_m=e_{-m}.
\tag{5}
\]

Then directly from the definition of the frame,

\[
\boxed{X_{-s}=X_sJ.}
\tag{6}
\]

In particular,

\[
\boxed{\operatorname{Ran}X_{-s}=\operatorname{Ran}X_s.}
\tag{7}
\]

Thus merely retaining the source-dilated frame as an **unlabelled subspace** does not recover the orientation erased by PC-301: reflection does not even change that subspace.

For the labelled cross-frame matrix,

\[
\boxed{
H_{-p,r}=JH_{p,r},
\qquad
H_{p,-r}=H_{p,r}J,
\qquad
H_{-p,-r}=JH_{p,r}J.
}
\tag{8}
\]

Because `WJ=JW`, the same identities hold with `H` replaced by `R`.

Consequently every singular value satisfies

\[
\boxed{
s_j(R_{-p,r})=s_j(R_{p,r})=s_j(R_{p,-r})
}
\tag{9}
\]

for every `j`. The same is true for every Schatten norm, `R^*R` spectrum, determinant magnitude, and any principal-angle statistic after frame whitening. Simultaneous reflection is even stronger: `R_{-p,-r}=JR_{p,r}J` is an exact unitary similarity, so the complete eigenvalue spectrum is unchanged as well.

This is a pointwise statement at finite `q,B,M`. It does not use averaging, asymptotics, a prime-number theorem, or any distributional assumption on the sources.

Individual-reflection **nonnormal eigenvalues** of a labelled square overlap are not covered by (9), because left multiplication by `J` is not a similarity. But such a use identifies two independently labelled latent mode spaces before taking eigenvalues, exactly the sort of noncanonical row/column identification already isolated in PC-278. The present result does not declare it impossible; it says that orientation is absent from the basis-invariant positive geometry of the frames themselves.

## 2. The first labelled orientation-odd carrier is exactly a sine cross-Gram

The labelled matrix does contain information that the unlabelled subspace forgets. Extract the component odd under reflection of the first source:

\[
O_{p,r}:=\frac12\left(R_{p,r}-R_{-p,r}\right)
=\frac12(I-J)R_{p,r}.
\tag{10}
\]

Using (1)--(3) and

\[
\cos(a-b)-\cos(a+b)=2\sin a\sin b,
\]

one obtains the exact entry formula

\[
\boxed{
(O_{p,r})_{n,m}
=\frac{2\sqrt{w_nw_m}}{N}
\sum_{h=1}^{B}
\sin\!\left(\frac{2\pi nph}{q}\right)
\sin\!\left(\frac{2\pi mrh}{q}\right).
}
\tag{11}
\]

Hence `O_{p,r}` changes sign if either source is reflected. It is not zero in general: retaining labelled positive/negative Fourier modes before same-source Gram formation really does recover a relative orientation channel.

But (11) also identifies that channel completely. It is just the cross-Gram matrix of two finite sine-feature families. No new operator symbol has appeared.

For completeness, the reflection-even companion is

\[
\frac12(R_{p,r}+R_{-p,r}),
\]

whose entries are the corresponding cosine-cosine overlaps plus the constant `h=0` term. Thus the full labelled quadratic cross-frame carrier splits exactly into cosine and sine Fourier sectors.

## 3. Independent same-law averaging gives a positive odd-Fourier Gram

Let `mu` be any probability law on `Z/qZ`, and define its additive Fourier transform by

\[
\widehat\mu(t)
:=\sum_{x\bmod q}\mu(x)e^{2\pi i tx/q}.
\tag{12}
\]

Choose `p,r` independently with law `mu`. Define the `B x 2M` real matrix

\[
S_\mu(h,m)
:=\sqrt{w_m}\,\operatorname{Im}\widehat\mu(mh),
\qquad 1\le h\le B,\ m\in S_M.
\tag{13}
\]

Independence in (11) gives immediately

\[
\boxed{
\mathbb E_{p,r\sim\mu}O_{p,r}
=\frac{2}{N}S_\mu^{T}S_\mu.
}
\tag{14}
\]

So the first averaged orientation-sensitive quadratic carrier is positive semidefinite and depends only on the **odd/sine Fourier feature Gram** of the source law. In particular it is unchanged under reflection of the entire source law,

\[
\mu^\vee(x)=\mu(-x),
\qquad
S_{\mu^\vee}=-S_\mu,
\]

and therefore

\[
\boxed{
\mathbb E_{\mu^\vee}O
=\mathbb E_\mu O.
}
\tag{15}
\]

The complete iid mean cross-frame matrix has the equally explicit decomposition

\[
\boxed{
\mathbb E H_{p,r}
=\frac1N\mathbf 1\mathbf 1^T
+\frac{2}{N}\left(C_\mu^TC_\mu+S_\mu^{(0)T}S_\mu^{(0)}\right),
}
\tag{16}
\]

where `C_mu(h,m)=Re widehat mu(mh)` and `S_mu^(0)(h,m)=Im widehat mu(mh)` without the `sqrt(w_m)` weights. Equivalently,

\[
(\mathbb EH)_{n,m}
=\frac1N\sum_{h=-B}^{B}
\overline{\widehat\mu(nh)}\widehat\mu(mh).
\tag{17}
\]

Thus the entire first-moment oriented-frame overlap is a second-order additive-Fourier covariance kernel. PC-299's positive Fejer defect retained only an additive power packet after squaring; (14)--(17) retain more, including cross-frequency odd information, but they still stop at ordinary quadratic Fourier data.

## 4. Distinct-source conditioning remains in the same classical packet

The canonical Prime-Circle source often uses distinct lower primes. The iid formula is not hiding a new effect at that conditioning step.

Let `P subset Z/qZ` be any finite source set of size `L`, let `mu` be its uniform law, and average over ordered pairs `p!=r` from `P`. Write `E_!=` for this expectation. Since

\[
\sum_{p\ne r}O_{p,r}
=\sum_{p,r}O_{p,r}-\sum_pO_{p,p},
\]

we have exactly

\[
\mathbb E_{\ne}O
=\frac{L}{L-1}\mathbb E_{\rm iid}O
-\frac1{L-1}\mathbb E_{p\sim\mu}O_{p,p}.
\tag{18}
\]

The diagonal term is again an ordinary Fourier packet. From (11) and `2 sin a sin b=cos(a-b)-cos(a+b)`,

\[
\boxed{
(\mathbb E_{p\sim\mu}O_{p,p})_{n,m}
=\frac{\sqrt{w_nw_m}}{N}
\sum_{h=1}^{B}
\left[
\operatorname{Re}\widehat\mu((n-m)h)
-\operatorname{Re}\widehat\mu((n+m)h)
\right].
}
\tag{19}
\]

Combining (14), (18), and (19) proves that without-replacement conditioning introduces no new carrier: it only mixes products of imaginary Fourier coefficients with real Fourier coefficients of the same source law.

For an unordered source pair, `O_{r,p}=O_{p,r}^T`. Hence every swap-invariant symmetric/Hermitian aggregate over `p<r` is controlled by the same ordered-distinct formula. An explicitly order-sensitive antisymmetric statistic is a different carrier and is not claimed to be closed here.

## 5. Prime source: the recovered orientation is ordinary prime exponential-sum data

Let

\[
P_q=\{\ell:\ell\text{ prime},\ 2<\ell<q\},
\qquad L_q=|P_q|,
\]

and define

\[
S_q(a):=\sum_{\ell\in P_q}e^{2\pi i a\ell/q}.
\tag{20}
\]

For the uniform prime law `nu_q`,

\[
\widehat\nu_q(a)=\frac{S_q(a)}{L_q}.
\tag{21}
\]

Therefore (14) becomes

\[
\boxed{
(\mathbb E O)_{n,m}
=\frac{2\sqrt{w_nw_m}}{NL_q^2}
\sum_{h=1}^{B}
\operatorname{Im}S_q(nh)
\operatorname{Im}S_q(mh),
}
\tag{22}
\]

and the distinct-prime correction (19) adds only real parts of `S_q((n-m)h)` and `S_q((n+m)h)`.

This is a genuine recovery relative to PC-301: the imaginary/odd part of the prime source Fourier transform, which `G_s` erased pointwise, is now visible. But the arithmetic endpoint is completely classical. `S_q(a)` is an ordinary additive exponential sum over primes. The Vinogradov/Vaughan/circle-method literature studies precisely such sums, and current work continues to sharpen them; for example James Maynard, Mayank Pandey and Maksym Radziwill, **Exponential sums over primes**, arXiv:2608.14777 (14 August 2026), improves the classical Vinogradov minor-arc exponent for the von-Mangoldt-weighted analogue.

PC-299 already records the neighboring zero-sensitive literature in which mean squares of prime exponential sums interface with primes in short intervals and zero pair correlation. Equations (20)--(22) do not produce a new spectral parameter, gamma factor, functional-equation symmetry, or critical-line constraint. Any RH sensitivity extracted solely by estimating these entries is inherited from the classical additive-prime Fourier package.

## 6. Prior-art and novelty audit

Every abstract ingredient is standard. Reflection of a symmetric harmonic frame acts by the mode-reversal permutation; cross-Gram singular data is invariant under left/right unitary changes of frame coordinates; and the odd/even decomposition of a finite Fourier sum is exactly its sine/cosine decomposition. Harmonic-frame symmetry and projective frame invariants are a mature subject; a representative reference is T.-Y. Chien and S. Waldron, **The Projective Symmetry Group of a Finite Frame**, *New Zealand Journal of Mathematics* 48 (2018), 55--81.

The prime-specific quantities in (20)--(22) are likewise standard additive exponential sums over primes. Targeted searches against harmonic-frame cross-Grams, Fourier phase retrieval, sine/cosine source covariance, and modern prime exponential-sum estimates found the expected classical frameworks and no independent reason to treat (14) as a new zeta operator. Absence of an exact match is not used as evidence of novelty.

The project-local delta is narrower and exact: the first route explicitly left open by PC-301—**retain the oriented low-mode frames before the centered same-source Gram**—splits into an exact mode-reversal gauge for positive/unlabelled geometry and an orientation-odd labelled sector that is precisely a sine-Fourier covariance. The proof is finite and self-contained; the literature anchors above are neighboring prior art rather than load-bearing dependencies, so no new `SOURCES.md` entry is required.

## 7. Falsification controls

The claims have direct finite tests.

For arbitrary admissible `q,B,M,p,r`, construct `X_p` explicitly. Equation (6) must hold exactly up to column ordering, and the singular values of `R_{p,r}`, `R_{-p,r}`, and `R_{p,-r}` must agree. Failure would refute the mode-reversal claim.

Entrywise, direct evaluation of `(R_{p,r}-R_{-p,r})/2` must equal the sine sum (11). Reflecting either source must negate that labelled odd component.

For any probability vector `mu` on `Z/qZ`, brute-force averaging over all source pairs must agree with the Gram identity (14). The matrix on the right is automatically positive semidefinite. Replacing `mu` by its reflected law must leave it unchanged.

For any finite source set, direct averaging over `p!=r` must agree with (18)--(19). These identities were stress-tested numerically on small prime moduli for nonuniform probability laws; the stored result depends only on the exact derivation.

## 8. Consequence for the research frontier

PC-301's instruction to preserve orientation **before** same-source contraction remains correct, but PC-302 narrows what that can mean. Simply retaining the symmetric `+m/-m` frame and then passing to subspaces, principal angles, singular values, or other positive basis-invariant geometry does not recover source orientation at all: reflection is only mode relabelling.

If the mode labels themselves are retained, the first reflection-odd quadratic observable is real and nontrivial, but after the natural same-law source average it is exactly the Gram matrix of sine Fourier coefficients. For primes, that is classical additive prime exponential-sum covariance.

A surviving mechanism therefore has to do more than say "keep the frames." It must use a **geometrically forced chirality** that distinguishes `+m` from `-m` before positive compression, a higher-order joint observable not determined by second-order source Fourier covariance, an intrinsically order-sensitive source relation, or a cross-level carrier whose information is not equivalent to these harmonic-frame overlaps. Such a mechanism must still pass the mandate's matched-control and prior-art gates; inserting an arbitrary sign-of-mode operator by hand would not do so.