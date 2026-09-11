# PC-267 — reflection parity sectors interlace on the central collision component

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the reflection/projective and fine-spectrum channel left after PC-260 and PC-266.

Fix distinct odd primes

\[
2<p<r<q,
\]

and let the PC-251 shared-upper collision reduction be

\[
M_q=W G_r W G_p\in M_k(\mathbb R),
\tag{1}
\]

with positive diagonal `W`, binary path Gram factors `G_p,G_r`, and `k` even. PC-260 proves the exact reflection symmetry

\[
J_kM_qJ_k=M_q,
\tag{2}
\]

while PC-266 proves that cutting at every **double-gap seam**

\[
\varepsilon_a=\eta_a=0
\tag{3}
\]

splits `M_q` into maximal collision components whose common checkerboard gauge is oscillatory.

Combining those two exact structures gives a stronger classification of the reflection sectors. The double-gap decomposition is itself reflection symmetric. Every noncentral component is paired with a reflected isospectral component. There is at most one reflection-fixed component, and if it exists it has even size. On that central component the `J=-1` and `J=+1` eigenvalues are forced to **strictly alternate** in descending order:

\[
\boxed{
\lambda^-_1>\lambda^+_1>
\lambda^-_2>\lambda^+_2>
\cdots>
\lambda^-_m>\lambda^+_m>0.
}
\tag{4}
\]

Equivalently, if the central component has size `2m` and its eigenvalues are ordered

\[
\lambda_1>\lambda_2>\cdots>\lambda_{2m}>0,
\tag{5}
\]

then the corresponding `M_q` eigenvector has reflection parity

\[
\boxed{Jx_j=(-1)^j x_j.}
\tag{6}
\]

Thus the largest central eigenvalue is reflection-odd, the next is reflection-even, and so on. The reflection label is not an independent arithmetic quantum number: once the ordered simple spectrum of the central component is known, its parity sequence is fixed.

More globally, let

\[
P_q^{\pm}(\lambda)
=\det(\lambda I-M_q^{(\pm)})
\tag{7}
\]

be the two parity characteristic polynomials of PC-260. If `Q_q` is the product of the characteristic polynomials of one representative from every reflected noncentral component pair, then

\[
\boxed{
P_q^+(\lambda)=Q_q(\lambda)C_q^+(\lambda),
\qquad
P_q^-(\lambda)=Q_q(\lambda)C_q^-(\lambda),
}
\tag{8}
\]

where `C_q^\pm` are the parity polynomials of the unique central component when one exists, and are both `1` otherwise. Hence if the central seam is a double gap, there is no central component and

\[
\boxed{P_q^+=P_q^- .}
\tag{9}
\]

If the central component exists, the zeros of `C_q^-` and `C_q^+` strictly interlace as in (4). Any additional common zero between the two full parity polynomials beyond the forced factor `Q_q` can only come from an accidental spectral coincidence between distinct disconnected components, exactly the type of cross-component coincidence left open by PC-266.

This is a classical oscillation consequence rather than a new zeta mechanism. It closes the possibility that the exact reflection of PC-260 supplies an independent parity ordering, an internal parity-sector crossing, or a new finite-volume projective label. Quantitative gaps between the alternating levels, near-spectrum scaling, subleading fluctuations, top Lyapunov data, and genuinely long resonance itineraries remain outside the result.

## 1. Reflection pairs the double-gap components

PC-260 gives the exact palindromes

\[
w_{k+1-a}=w_a,
\qquad
\varepsilon_{k-a}=\varepsilon_a,
\qquad
\eta_{k-a}=\eta_a.
\tag{10}
\]

Therefore seam `a` is a double gap exactly when seam `k-a` is. Cutting the collision coordinate line at all double gaps produces a reflection-invariant partition into contiguous components.

Every component not meeting the central seam between coordinates `k/2` and `k/2+1` is exchanged with a distinct reflected component. If the central seam itself is a double gap, all components occur in such pairs. If it is not a double gap, exactly one component crosses that seam and is fixed by reflection.

Because `k` is even, a reflection-fixed contiguous component contains coordinates in mirrored pairs and therefore has even size, say `2m`. This proves the purely combinatorial part of the decomposition behind (8)--(9).

## 2. Reflected component pairs contribute the same polynomial to both parity sectors

Let `C` be one noncentral component and `C^\vee` its reflection. In the component decomposition, the restriction of `M_q` to their direct sum has the form

\[
M_C\oplus M_{C^\vee},
\qquad
M_{C^\vee}=J_C M_C J_C,
\tag{11}
\]

where `J_C` identifies the two reflected coordinate intervals.

For every vector `v` on `C`, the two vectors

\[
(v,J_Cv),
\qquad
(v,-J_Cv)
\tag{12}
\]

have reflection parity `+1` and `-1`, respectively. Equation (11) shows that the action induced on either parity subspace is exactly `M_C`. Therefore the pair contributes

\[
\det(\lambda I-M_C)
\tag{13}
\]

to **both** `P_q^+` and `P_q^-`.

Multiplying (13) over one representative of every reflected pair gives the common factor `Q_q` in (8). If no central component exists, these paired subspaces exhaust the collision coordinates, proving (9) exactly.

This factor is symmetry-forced. Distinct component pairs can still have accidental common eigenvalues, and a paired component can accidentally share an eigenvalue with the central component; PC-267 does not relabel such coincidences as reflection information.

## 3. Checkerboard oscillation forces parity alternation on the central component

Assume now that a central component `C_0` of size `2m` exists. Let

\[
S=\operatorname{diag}(1,-1,1,-1,\ldots)
\tag{14}
\]

be the global checkerboard gauge restricted to `C_0`, and put

\[
B=S M_{C_0} S.
\tag{15}
\]

PC-266 proves that `B` is an oscillatory matrix. Hence its eigenvalues are real, positive and simple. Order them as in (5). The classical Gantmacher--Krein oscillation theorem says that a right eigenvector `y_j` for the `j`th largest eigenvalue has exactly `j-1` sign changes, with zeros handled by the standard sign-variation convention.

The reflection symmetry survives the gauge. On an even reflection-fixed component the alternating checkerboard signs reverse under coordinate reflection, so

\[
JS=-SJ.
\tag{16}
\]

Using (2),

\[
JBJ
=JS M_{C_0} S J
=(-SJ)M_{C_0}(-JS)
=S M_{C_0} S
=B.
\tag{17}
\]

Because every eigenvalue of `B` is simple, its eigenvector `y_j` has definite reflection parity,

\[
Jy_j=\tau_j y_j,
\qquad
\tau_j\in\{+1,-1\}.
\tag{18}
\]

For a nonzero vector of even length, reflection parity determines the parity of its number of sign changes. After deleting zero coordinates, a reflection-even vector has its sign transitions in mirrored pairs, so their number is even. A reflection-odd vector has those mirrored pairs plus one unavoidable central sign reversal, so their number is odd. Since `y_j` has exactly `j-1` sign changes,

\[
\boxed{\tau_j=(-1)^{j-1}.}
\tag{19}
\]

The corresponding eigenvector of the original collision matrix is

\[
x_j=Sy_j.
\tag{20}
\]

Equations (16) and (19) give

\[
Jx_j
=JSy_j
=-SJy_j
=-\tau_j x_j
=(-1)^j x_j,
\tag{21}
\]

which is (6). Since the spectrum is simple, the odd and even parity roots must alternate strictly, proving (4).

The checkerboard anticommutation in (16) is important. The oscillatory gauged matrix `B` has a reflection-even Perron eigenvector, but transforming back to `M_q` flips the reflection sector; this is why the largest squared singular eigenvalue in (4) lies in the `J=-1` sector.

## 4. Exact controls from the existing collision examples

For `(p,r,q)=(7,11,13)`, PC-260 gives one connected six-site collision component and the exact parity polynomials

\[
P_q^+(\lambda)
=(\lambda-16)(\lambda^2-592\lambda+2304),
\tag{22}
\]

\[
P_q^-(\lambda)
=\lambda^3-736\lambda^2+78336\lambda-774144.
\tag{23}
\]

Their roots are approximately

\[
P_q^-:\quad
609.57395,\ 115.42328,\ 11.00277,
\]

\[
P_q^+:\quad
588.08218,\ 16,\ 3.91782,
\]

and therefore

\[
609.57395>588.08218>
115.42328>16>
11.00277>3.91782,
\tag{24}
\]

exactly as (4) predicts. The proof above does not depend on these numerical approximations; they are only a finite audit against the independently persisted PC-260 polynomials.

For `(p,r,q)=(7,13,17)`, PC-266 gives collision weights `(15,4,4,15)` and double gaps after coordinates `1` and `3`. The two reflected singleton components each contribute the eigenvalue `900`, while the central two-site component contributes `144` and `16`. The parity factorization is therefore

\[
P_q^-(\lambda)=(\lambda-900)(\lambda-144),
\qquad
P_q^+(\lambda)=(\lambda-900)(\lambda-16).
\tag{25}
\]

The common factor is precisely the reflected component pair; the remaining central odd root `144` lies strictly above the central even root `16`.

## 5. Matched controls and RH-facing consequence

The argument uses only structures already shown to be prime-blind at this stage of the shared-upper reduction: the palindromic rational-partition collision word of PC-260, positive collision weights, binary path Gram factors, the double-gap decomposition, and the oscillatory checkerboard gauge of PC-266. The same reasoning therefore applies to the admissible odd pairwise-coprime rational-partition controls whenever they realize the same collision construction.

Consequently, none of the following can by itself provide a new Prime-Circle/RH discriminator:

- the sequence of reflection parities of the connected-component eigenvalues;
- the number of odd versus even central levels;
- an exact crossing between the two central parity sectors;
- equality of the two parity spectra when the central seam is a double gap; or
- the symmetry-forced common factors contributed by reflected disconnected components.

The exact reflection of PC-260 is therefore more rigid than a generic `Z_2` label. Inside the only reflection-fixed connected component, **the parity is already encoded by eigenvalue order through classical oscillation theory**.

What remains genuinely outside this result is quantitative rather than combinatorial: the sizes and scaling laws of the alternating parity gaps, fine spacing, mesoscopic/near-spectrum characteristic statistics, subleading edge fluctuations, top Lyapunov or other subadditive transfer data, and resonant itineraries whose complexity grows with the source. PC-267 does not claim those quantities are classical.

## 6. Prior-art and novelty audit

The mathematical ingredients are classical. F. Gantmacher and M. Krein, **Sur les matrices completement non negatives et oscillatoires**, *Compositio Mathematica* 4 (1937), 445--476, is the original oscillatory-matrix source; the sign-variation theorem is also standard in their later monograph *Oscillation Matrices and Kernels and Small Vibrations of Mechanical Systems*. S. M. Fallat and C. R. Johnson, *Totally Nonnegative Matrices*, Princeton University Press (2011), gives a modern account of the same spectral structure.

Reflection parity for centrosymmetric matrices is likewise classical. A. Cantoni and P. Butler, **Eigenvalues and eigenvectors of symmetric centrosymmetric matrices**, *Linear Algebra and its Applications* 13:3 (1976), 275--288, DOI `10.1016/0024-3795(76)90101-4`, proves the symmetric/skew-symmetric eigenvector decomposition and, for the symmetric centrosymmetric tridiagonal case with distinct spectrum, alternating reflection parity in eigenvalue order. That paper does not contain the Prime-Circle collision matrix, which is generally nonsymmetric and not tridiagonal in collision coordinates, but it is direct prior art for the parity-interlacing phenomenon.

No novelty is claimed for oscillatory sign variation, centrosymmetric parity decomposition, or interlacing as an abstract matrix phenomenon. The project-local content is the exact combination forced by the Prime-Circle carrier: PC-260 supplies a palindromic reflection, PC-266 supplies an oscillatory gauge on every double-gap component, the even checkerboard gauge anticommutes with reflection, and together these facts yield the explicit factorization (8) and parity law (6) for the native collision operator.

A targeted novelty check against oscillatory matrices, centrosymmetric spectra, total nonnegativity, and parity interlacing found established neighboring theory rather than an independent zeta-spectral mechanism. The result is therefore stored as a classicalization/boundary theorem, not as `CANDIDATE-NEW-STRUCTURE`.

## 7. Falsification and boundary audit

The claim has direct exact failure modes.

1. **Component symmetry:** find a PC-260 collision word whose double-gap set is not preserved by reflection.
2. **Paired-block action:** find a reflected component pair for which the two parity restrictions are not both similar to the same component matrix.
3. **Central parity:** find a reflection-fixed component of odd size, contrary to even total collision count and central contiguity.
4. **Oscillation:** violate PC-266 by producing a central component whose checkerboard gauge is not oscillatory.
5. **Parity law:** for a central oscillatory component, find an eigenvector whose sign-variation parity disagrees with its reflection parity, or for which (16) fails.
6. **Finite controls:** violate the exact parity allocations in (22)--(25).

The theorem is intentionally narrow. It applies to the PC-251/PC-257 shared-upper collision operator with the exact PC-260 reflection and PC-266 oscillatory component structure. It does not transfer automatically to another Prime-Circle operator, and it says nothing about hyperbolic prime-flute constructions.