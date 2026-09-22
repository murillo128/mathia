# PL-427 — The Kandhil–Languasco–Moree proof polarizes to the full fixed-modulus mixed-zero matrix, but only under GRH

**Evidence/status:** `LITERATURE + EXACT-DERIVED + FRONTIER-REFINEMENT + CIRCULARITY-OBSTRUCTION`.

**Parent findings:** `PL-421`, `PL-425`, `PL-426`.

## Claim

`PL-426` correctly identifies an information loss in the **published observable** of Yıldırım and Kandhil--Languasco--Moree: for fixed `q=5`, knowing their four residue quantities

\[
F_5(x,T;a)
=\sum_{\chi,\psi\bmod5}
\overline{\chi(a)}\psi(a)G_{\chi,\psi}(x,T)
\]

recovers only the diagonal of a Fourier conjugate of the full mixed-character matrix

\[
G(x,T)=\bigl(G_{\chi,\psi}(x,T)\bigr)_{\chi,\psi\bmod5}.
\]

A closer audit of the **proof** of Kandhil--Languasco--Moree Theorem 3 sharpens that conclusion. At fixed modulus `q=5`, their explicit-formula/mean-square argument can be repeated with an arbitrary fixed character coefficient vector `c=(c_\chi)`. Under the same GRH hypothesis and in the same high-`T` range, it yields

\[
\boxed{
 c^*G(x,T)c
 =\frac{T\log x}{\pi}\,\|c\|_2^2
 +o_c(T\log x).
}
\tag{1}
\]

Because the character space has fixed dimension four, polarization of (1) gives the full matrix asymptotic

\[
\boxed{
G(x,T)
=\frac{T\log x}{\pi}I_4
+o(T\log x)
\quad\text{in operator norm}.
}
\tag{2}
\]

Equivalently,

\[
G_{\chi,\chi}(x,T)
\sim\frac{T\log x}{\pi},
\qquad
G_{\chi,\psi}(x,T)=o(T\log x)
\quad(\chi\ne\psi).
\tag{3}
\]

Thus the stronger mixed-matrix estimate left as a possible escape in `PL-426` is not absent at the level of the KLM proof: at fixed modulus it is latent after replacing the single residue-character vector by arbitrary coefficients and polarizing.

This does **not** close the `PL-425` transfer target or provide an RH mechanism. KLM's argument assumes GRH for the Dirichlet `L`-functions modulo `5`; for the principal character,

\[
L(s,\chi_0)=\zeta(s)(1-5^{-s}),
\]

so that hypothesis already contains RH for `zeta`. The useful redirect is therefore negative and precise: the missing issue is not a GRH-conditional mixed-character covariance theorem. It is an **unconditional, or genuinely weaker-than-RH, matrix-valued source/zero transfer** in a range compatible with the `PL-421` positivity gate.

## 1. The KLM mixed matrix and arbitrary coefficient vectors

Kandhil--Languasco--Moree define, under GRH,

\[
G_{\chi,\psi}(x,T)
=
\sum_{\substack{|\gamma_\chi|\le T\\|\gamma_\psi|\le T}}
 x^{i(\gamma_\chi-\gamma_\psi)}
 \frac{4}{4+(\gamma_\chi-\gamma_\psi)^2}.
\tag{4}
\]

The kernel has the positive Fourier representation

\[
\frac4{4+u^2}
=
\int_{-\infty}^{\infty}e^{ivu}e^{-2|v|}\,dv.
\tag{5}
\]

Writing

\[
Z_\chi(v)
:=\sum_{|\gamma_\chi|\le T}x^{i\gamma_\chi}e^{iv\gamma_\chi},
\]

we have

\[
G_{\chi,\psi}(x,T)
=
\int Z_\chi(v)\overline{Z_\psi(v)}e^{-2|v|}\,dv.
\tag{6}
\]

Hence `G` is a positive-semidefinite Gram matrix. For any fixed `c in C^4`, define

\[
Z_c(v):=\sum_{\chi\bmod5}\overline{c_\chi}Z_\chi(v).
\tag{7}
\]

Then exactly

\[
\boxed{
\int |Z_c(v)|^2e^{-2|v|}\,dv
=c^*G(x,T)c.
}
\tag{8}
\]

For the special vector

\[
c^{(a)}_\chi:=\chi(a),
\qquad a\in U_5,
\tag{9}
\]

(8) is precisely the KLM residue observable `F_5(x,T;a)`. The published theorem tests `G` on the four vectors `c^(a)`; nothing in the positive-kernel identity itself restricts us to those vectors.

## 2. The explicit-formula proof survives arbitrary fixed character weights

The key step in KLM is to multiply the explicit formula for each character by `overline{chi(a)}` and sum over characters. Character orthogonality then turns the prime-side Dirichlet series into a single residue class.

For arbitrary fixed `c`, make the same linear combination with coefficient `overline{c_chi}`. The corresponding prime-side residue weight is

\[
b_c(n)
:=
\sum_{\chi\bmod5}\overline{c_\chi}\chi(n).
\tag{10}
\]

For `c=c^(a)`, character orthogonality gives

\[
b_{c^{(a)}}(n)=4\,1_{n\equiv a\ (5)}
\]

for `(n,5)=1`, exactly recovering the arithmetic term in the published proof.

The main mean-square calculation depends only on the squared coefficients of this prime-side Dirichlet polynomial. Replacing the residue indicator by `b_c(n)` therefore replaces KLM's scalar weighted prime sum by

\[
S_c(x)
=
\frac1{x^2}\sum_{n\le x}n\Lambda(n)^2|b_c(n)|^2
+x^2\sum_{n>x}\frac{\Lambda(n)^2|b_c(n)|^2}{n^3},
\tag{11}
\]

up to the same harmless normalization convention used in the paper. KLM state the auxiliary mean-square lemma for real coefficients, but the required complex-coefficient form follows from the same kernel expansion (or, equivalently, by separating real and imaginary parts); no number-theoretic input changes.

For fixed modulus `5`, GRH gives the weighted prime-number theorem in each reduced residue class with the error used by KLM. Splitting (11) over `a in U_5` therefore gives

\[
S_c(x)
=
\frac{\log x}{4}
\sum_{a\in U_5}|b_c(a)|^2
+O_c\!\left(\frac{\log^3x}{\sqrt x}\right).
\tag{12}
\]

Finite character orthogonality now supplies the decisive identity

\[
\sum_{a\in U_5}|b_c(a)|^2
=4\sum_{\chi\bmod5}|c_\chi|^2.
\tag{13}
\]

Consequently

\[
\boxed{
S_c(x)
=\|c\|_2^2\log x
+O_c\!\left(\frac{\log^3x}{\sqrt x}\right).
}
\tag{14}
\]

This is exactly the scalar main term required for (1). It is also a useful conceptual point: once arbitrary character weights are allowed, the prime-side residue decomposition itself supplies the Euclidean norm on character space. There is no remaining leading-order mixed coherence under the GRH input used by the proof.

## 3. The imprimitive principal-character correction does not spoil the fixed-5 extension

One step that is invisible for the special residue vectors needs checking before (1) can be claimed. KLM pass from imprimitive characters to their inducing primitive characters. In the published residue sum, the resulting correction `R_4` vanishes after character orthogonality. For arbitrary `c`, it need not vanish.

At prime modulus `5` this correction is nevertheless negligible for a simpler reason. The only imprimitive character modulo `5` is the principal character `chi_0`, induced by the trivial character of conductor `1`. The two characters differ only on integers divisible by `5`. Since the explicit formula is weighted by `Lambda(n)`, the correction is therefore supported only on

\[
n=5^k,\qquad k\ge1.
\tag{15}
\]

The smoothed coefficients used in the KLM explicit formula decay geometrically away from `n approximately x`. The square-sum of the prime-power correction is correspondingly bounded by a fixed-`c` geometric tail, and the same mean-square estimate used for the other remainder terms makes its contribution `o_c(T log x)` in the Theorem 3 range. Thus the principal-character imprimitive correction survives algebraically but cannot alter the leading matrix term at fixed `q=5`.

This fixed-prime argument is deliberately narrower than a variable-`q` statement. No uniform matrix theorem in growing modulus is claimed here.

## 4. Recovering the whole matrix by finite polarization

KLM's Theorem 3, specialized to `q=5`, is in the range

\[
\frac{x}{4}\le T\le \exp(x^{3/4})
\tag{16}
\]

for sufficiently large `x` (the paper states the corresponding general `q` range). Repeating the proof with fixed `c`, equations (8)--(14), together with the same estimates for the remaining explicit-formula terms and the zero-counting boundary contribution, give

\[
c^*G(x,T)c
=
\frac{T\log x}{\pi}\|c\|_2^2
+o_c(T\log x).
\tag{17}
\]

The constant calibrates against the published theorem: for `c=c^(a)`,

\[
\|c^{(a)}\|_2^2=4,
\]

so (17) becomes

\[
F_5(x,T;a)
\sim \frac4\pi T\log x,
\tag{18}
\]

which is exactly the `q=5` specialization of KLM's `phi(q)/pi` main term.

Now take only the finite collection of vectors

\[
e_j,\qquad e_j+e_k,\qquad e_j+i e_k
\quad(0\le j<k\le3).
\tag{19}
\]

Applying (17) to this finite set and using the complex polarization identity yields

\[
G_{jj}(x,T)
=\frac{T\log x}{\pi}+o(T\log x)
\tag{20}
\]

and

\[
G_{jk}(x,T)=o(T\log x)
\qquad(j\ne k).
\tag{21}
\]

Because the dimension is fixed,

\[
\left\|G(x,T)-\frac{T\log x}{\pi}I_4\right\|_{\rm op}
\le 4\max_{j,k}
\left|G_{jk}(x,T)-\frac{T\log x}{\pi}\delta_{jk}\right|
=o(T\log x),
\tag{22}
\]

which proves (2).

This also clarifies the relation to `PL-426`. The map

\[
G\mapsto (F_5(a))_{a\in U_5}
\]

is genuinely non-injective, exactly as `PL-426` proves. The refinement is that the **proof architecture** used to estimate those four compressed observables is tomographically extensible: one can feed it the additional coefficient vectors in (19), not reconstruct the missing entries from the four published numbers.

## 5. Why this does not close the `PL-425` source-transfer gate

There are two independent limitations.

First, the result is conditional on GRH for all Dirichlet `L`-functions modulo `5`. In particular the principal character satisfies

\[
L(s,\chi_0)=\zeta(s)(1-5^{-s}),
\tag{23}
\]

so GRH for `L(s,chi_0)` contains the Riemann hypothesis itself. Therefore (2) cannot be inserted into a purported proof of RH without circularity. It is useful as a structural calibration and as a redirect for the literature search, not as the missing positivity input.

Second, (2) is a high-`T` statement about the zero-correlation matrix `G(x,T)`. `PL-425` requires a matrix-valued transfer to the actual deterministically source-subtracted short-prime covariance in the scale relation needed by the `PL-421` local dephasing floor. The KLM proof does not by itself identify that covariance matrix with `G`, nor does the fixed-`q` argument above establish the required uniform source-replacement error in a different scaling regime.

Thus the surviving target is narrower than the one stated after `PL-426`:

\[
\boxed{
\text{obtain the needed mixed matrix control without assuming RH/GRH,
 or from an input strictly weaker than the target RH statement.}
}
\tag{24}
\]

A theorem that merely reproves (2) under GRH would add no mechanism to the line.

## 6. Prior-art and novelty audit

The primary source is already registered as source 107 in `research/prime_lattice/SOURCES.md`:

- Neelam Kandhil, Alessandro Languasco, Pieter Moree, “Pair correlation of zeros of Dirichlet L-functions: a possible path towards the conjectures of Chowla, Elliott-Halberstam and Montgomery,” *Mathematische Annalen* **394** (2026), Article 43, DOI `10.1007/s00208-026-03383-y`.

Their paper supplies the mixed matrix entries, the positive kernel, the summed explicit formula, the weighted mean-square argument, the GRH arithmetic-progression input, and Theorem 3. Yıldırım's earlier pair-correlation work and the Bui--Keating--Smith variance/pair-correlation transfer remain sources 105--106.

No novelty is claimed for the KLM theorem, the explicit formula, PNT in arithmetic progressions under GRH, finite character orthogonality, complex polarization, or the standard extension of a quadratic mean-square calculation from real to complex coefficients. Targeted searches around mixed/joint Dirichlet-`L` pair correlation and matrix-valued formulations did not locate the fixed-modulus arbitrary-coefficient statement (17) or the operator-norm corollary (22) stated explicitly in the literature.

The durable contribution is the line-specific proof audit: the information-theoretic compression of the **published** all-residue observables in `PL-426` should not be mistaken for a limitation of the KLM analytic machinery under its hypotheses. At fixed `q=5`, the machinery can be polarized to recover asymptotic orthogonality of the entire mixed-character zero matrix; the obstruction relevant to this line is instead the strength and circularity of the GRH hypothesis and the remaining source-transfer/range problem.

## 7. Adversarial audit

1. **No reconstruction from four residue observables is claimed.** `PL-426` remains valid: four diagonal Fourier quadratic forms cannot determine a `4 x 4` Hermitian matrix. Equation (22) comes from rerunning the proof on additional coefficient vectors.

2. **The coefficient-vector extension is fixed-dimensional.** Constants may depend on `c`; polarization uses only finitely many fixed vectors. No uniform statement in arbitrary vector dimension or growing modulus is inferred.

3. **The imprimitive correction has been retained.** The arbitrary-coefficient combination no longer enjoys KLM's exact residue-orthogonality cancellation of `R_4`. At `q=5`, its support is only the prime powers `5^k`, making it lower order in the same high-`T` range. A variable-modulus analogue would require a separate uniform treatment.

4. **The conclusion is conditional on GRH, hence target-circular.** It is not evidence that the required matrix floor can be proved unconditionally, and it cannot be used as an RH premise.

5. **Zero-side orthogonality is not yet prime-side source replacement.** Even a full operator-norm estimate for `G` does not automatically identify the deterministic short-prime covariance or preserve the exact normalization required by `PL-421`.

6. **No claim is made below the analytic-continuation barrier by Euler-product manipulation.** The extension operates inside the explicit-formula framework already used by KLM; continuation and zero information enter through their GRH-based `L`-function argument, not by formally extending a convergent Euler product.

## Consequence for the research line

The next pass should not search for a merely **GRH-conditional** theorem controlling the individual fixed-modulus mixed entries `G_{chi,psi}`: the KLM proof already contains enough machinery to obtain that after arbitrary character weighting and polarization.

The meaningful frontier is whether the source-side matrix needed by `PL-421` can be controlled by arithmetic input that does not already assume the desired zero localization. Concretely, a viable continuation must either

- derive an unconditional or target-weaker mixed-character covariance estimate strong enough to preserve the `1/4` mod-5 spectral floor in the relevant source-transfer range, or
- replace the current dephasing/source-transfer route by a source-faithful signed statistic whose cancellation can be controlled without such a matrix theorem.

This is a refinement of `PL-426`, not a reversal: **statement-level Fourier compression is real, but proof-level tomographic extensibility under GRH means the decisive obstruction is hypothesis strength and source transfer, not missing conditional matrix information.**
