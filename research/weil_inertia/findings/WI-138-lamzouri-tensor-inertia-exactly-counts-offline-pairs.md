# WI-138 — Lamzouri's finite tensor inertia exactly counts distinct off-line pairs

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-INTERFACE + PRIOR-ART-REDIRECT`. WI-137 packages the full finite slack in Lamzouri's Hilbert argument as the Hilbert--Schmidt distance of a canonical self-adjoint tensor operator `A_F` from the quantized target `P_U+P_V`, and observes that the squared negative spectral mass is bounded by the slack. There is an additional exact invariant which was not used there: on Lamzouri's finite space `W`, the inertia of `A_F` is determined **completely** by the zero-type populations. If `k` is the number of distinct non-real conjugate pairs in the finite multiset, `n` the number of simple real points, and `r` the number of distinct repeated real points, then

\[
\boxed{
\operatorname{In}\!\left(\mathcal A_F\big|_W\right)
=(n+r+k,\ k,\ 0).
}
\tag{A}
\]

In particular,

\[
\boxed{
 n_-(\mathcal A_F)=k,
 \qquad
 \operatorname{rank}(\mathcal A_F)=n+r+2k,
 \qquad
 \operatorname{sig}(\mathcal A_F)=n+r.
}
\tag{B}
\]

Thus the negative index of the Lamzouri tensor counts **exactly one negative direction per distinct off-line conjugate pair**, independently of multiplicity and independently of how strongly the pair is screened. Critical-line doubles and higher critical-line multiplicities do not create negative directions. The eigenvalue magnitudes can nevertheless collapse to zero, so this identity does not by itself improve the unconditional zeta percentage. Coupled to WI-137, it sharpens the near-extremizer picture: positive-density off-line mass near saturation cannot make the negative sector disappear; it must instead create a positive-density cloud of negative eigenvalues whose root-mean-square magnitude tends to zero.

## 1. Primary-source interface

The source remains Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1 and its proof. With Lamzouri's notation, list the distinct real elements and the distinct non-real elements of the conjugation-invariant finite multiset as

\[
R_1=\{x_1,\ldots,x_n\},
\qquad
R_2=\{x_{n+1},\ldots,x_{n+r}\},
\]

\[
S=\{z_1,\bar z_1,\ldots,z_k,\bar z_k\},
\]

and define

\[
f_z(u)=\eta(u)e^{-2\pi iuz},
\qquad
g_z=\frac{f_z+f_{\bar z}}2,
\qquad h_z=\frac{f_z-f_{\bar z}}{2i}.
\tag{1}
\]

Lamzouri's exact pair grouping is

\[
F
=\sum_{\ell=1}^{n+r}m_{x_\ell}f_{x_\ell}\otimes f_{x_\ell}
+2\sum_{j=1}^{k}m_{z_j}
 \bigl(g_{z_j}\otimes g_{z_j}-h_{z_j}\otimes h_{z_j}\bigr).
\tag{2}
\]

WI-126 proves, using analyticity of finite exponential polynomials, that the family

\[
\mathcal B=
\bigl(
 f_{x_1},\ldots,f_{x_{n+r}},
 g_{z_1},\ldots,g_{z_k},
 h_{z_1},\ldots,h_{z_k}
\bigr)
\tag{3}
\]

is linearly independent and spans `W`. Hence

\[
\dim W=n+r+2k,
\qquad
\dim V=n+r+k.
\tag{4}
\]

All vectors in (3) satisfy Lamzouri's real symmetry `conj(Phi(u))=Phi(-u)`, and their mutual inner products are real. WI-137 therefore identifies (2) with a self-adjoint operator on the resulting finite real Hilbert space,

\[
\mathcal A_F
=\sum_{\ell=1}^{n+r}m_{x_\ell}
   f_{x_\ell}\otimes f_{x_\ell}
+2\sum_{j=1}^{k}m_{z_j}
   \bigl(g_{z_j}\otimes g_{z_j}-h_{z_j}\otimes h_{z_j}\bigr).
\tag{5}
\]

No asymptotic approximation is present in (5).

## 2. Exact congruence normal form

Let

\[
B:\mathbb R^{n+r+2k}\longrightarrow W
\]

be the synthesis map whose ordered columns are the vectors in (3). By WI-126, `B` is an isomorphism. Define the diagonal matrix

\[
J:=\operatorname{diag}\!\left(
 m_{x_1},\ldots,m_{x_{n+r}},
 2m_{z_1},\ldots,2m_{z_k},
 -2m_{z_1},\ldots,-2m_{z_k}
\right).
\tag{6}
\]

Equation (5) is exactly

\[
\boxed{\mathcal A_F=BJB^*.}
\tag{7}
\]

Every multiplicity is a positive integer. Therefore `J` has `n+r+k` positive entries, `k` negative entries, and no zero entries. Since `B` is invertible, Sylvester's law of inertia for congruences gives

\[
\operatorname{In}(\mathcal A_F)
=\operatorname{In}(J)
=(n+r+k,k,0),
\]

which proves (A). This also proves that `A_F|_W` is nonsingular for every finite Lamzouri configuration, even when the odd directions are extremely strongly screened.

The counting identities (B) are immediate. In particular, if

\[
D_{\mathbb R}:=n+r,
\qquad
D_{\rm all}:=n+r+2k
\]

are respectively the numbers of distinct real elements and all distinct elements of the finite multiset, then

\[
\boxed{
D_{\mathbb R}=\operatorname{sig}(\mathcal A_F),
\qquad
D_{\rm all}=\operatorname{rank}(\mathcal A_F),
\qquad
2k=2n_-(\mathcal A_F).
}
\tag{8}
\]

So the finite Lamzouri tensor itself separates distinct real points from distinct non-real pairs exactly. Multiplicity affects the spectral magnitudes through the diagonal weights in `J`, but not the inertia.

## 3. Zeta interpretation

In Lamzouri's application,

\[
\mathcal Z_T=
\left\{
 i\left(\rho-\frac12\right)\frac{\log T}{2\pi}:
 0<\operatorname{Im}\rho\le T
\right\}.
\tag{9}
\]

The functional equation makes this multiset invariant under complex conjugation, and an element of `Z_T` is real exactly when the corresponding zeta zero lies on `Re rho=1/2`. Consequently, each distinct functional-equation pair of off-critical zeros gives one non-real conjugate pair in Lamzouri coordinates and therefore one negative eigenvalue of `A_F`.

Thus, for the exact finite operator attached to `Z_T`,

\[
\boxed{
 n_-(\mathcal A_{F,T})
 =\#\{\text{distinct off-critical functional-equation pairs in }\mathcal Z_T\}.
}
\tag{10}
\]

This is a count of **distinct pairs**, not a multiplicity-weighted count. A critical-line zero of multiplicity two contributes one positive direction with weight `2`; an off-line pair of multiplicity `m` still contributes one positive and one negative direction, with signed weights `+2m` and `-2m` before congruence.

The result therefore supplies an exact finite invariant that distinguishes the two main exceptional mechanisms which pair-level screening can make look similar: a real double has no negative direction, while an off-line pair always has one. What screening can erase is the **magnitude** of that negative eigenvalue, not its sign or existence.

## 4. Coupling to the WI-137 slack identity

WI-137 proves the exact identity

\[
\Delta
=\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
 +2B+4H_V,
\qquad
\Delta:=n-(2N-Q),
\tag{11}
\]

and hence

\[
\sum_{\lambda_i(\mathcal A_F)<0}\lambda_i^2\le\Delta.
\tag{12}
\]

WI-137 deliberately noted that (12) alone cannot convert negative square mass into a count, because an arbitrary matrix may have many tiny negative eigenvalues. Equation (A) now identifies exactly when that happens here: the number of negative eigenvalues is not arbitrary but is precisely `k`.

If a sequence of Lamzouri configurations is near-sharp,

\[
\Delta=o(N),
\tag{13}
\]

and has a positive density of distinct off-line pairs,

\[
k\ge\delta N
\qquad(\delta>0),
\tag{14}
\]

then (12) and (A) imply

\[
\boxed{
\frac1k\sum_{\lambda_i<0}\lambda_i^2
\le\frac{\Delta}{k}=o(1).
}
\tag{15}
\]

Thus a positive-density off-line population is compatible with near saturation only through a **macroscopic near-zero negative spectral cloud**. This is stronger than merely saying that the total negative square mass is small: the cardinality of that cloud is fixed by the off-line population.

For every `epsilon>0`, (12) also gives

\[
\#\{\lambda_i< -\epsilon\}
\le\frac{\Delta}{\epsilon^2}.
\tag{16}
\]

Combined with `n_-(A_F)=k`, a near-sharp configuration with `k` extensive must therefore place all but `o(N)` of its negative directions inside `(-epsilon,0)` for every fixed `epsilon`.

## 5. Exact determinant and the Schur-screening interface

The congruence form (7) also gives a determinant identity. Let `G_B=B^*B` be the ordinary positive-definite Gram matrix of the basis (3). Then

\[
\boxed{
\det_W(\mathcal A_F)
=(-1)^k\det(G_B)
\left(\prod_{x\in R}m_x\right)
\left(\prod_{j=1}^k(2m_{z_j})^2\right).
}
\tag{17}
\]

In particular `sign det(A_F)=(-1)^k` and the determinant never vanishes at finite `T`.

This factors through the odd Schur complement studied in WI-132. Write the basis as `[B_V,H]`, where `B_V` contains the real and `g` columns and `H` contains the `h` columns. Standard Gram determinant factorization gives

\[
\det G_B
=\det G_V\,
 \det\!\bigl(H^*(I-P_V)H\bigr).
\tag{18}
\]

If `z_j=x_j+iy_j`, `y_j>0`, and `u_j=h_{z_j}/y_j` are the normalized odd divided differences of WI-132, with

\[
S=U^*(I-P_V)U,
\]

then

\[
H^*(I-P_V)H=Y S Y,
\qquad Y=\operatorname{diag}(y_1,\ldots,y_k),
\]

so

\[
\boxed{
|\det_W(\mathcal A_F)|
=\det G_V\,\det S
\left(\prod_{j=1}^k y_j^2\right)
\left(\prod_{x\in R}m_x\right)
\left(\prod_{j=1}^k4m_{z_j}^2\right).
}
\tag{19}
\]

Equation (19) does not provide a lower bound by itself: the horizontal depths can approach zero, the normalized odd Schur determinant can collapse through screening, and the retained Gram determinant can collapse through clustering. It does, however, isolate the exact mechanisms by which the nonzero finite determinant can become asymptotically tiny. This is a useful determinant-level companion to the minimum-eigenvalue interface in WI-132--WI-136.

## 6. Controls and limits

Three elementary controls agree with the claim. A single simple real point has inertia `(1,0,0)`. A single real double also has inertia `(1,0,0)` despite multiplicity two. A single simple non-real conjugate pair has basis `(g,h)` and congruence target `diag(2,-2)`, hence inertia `(1,1,0)` regardless of the angle between `g` and `h`.

The last control also explains why (A) does not contradict the screening constructions of WI-005--WI-007 or the Schur collapse mechanisms in WI-132--WI-136. As the pair approaches a screened or confluent configuration, the synthesis map `B` can become badly conditioned and the unique negative eigenvalue can approach zero while remaining strictly negative at every finite stage. Sylvester inertia is topological/sign information; it supplies no uniform spectral gap.

Consequently this finding does **not** yield an unconditional improvement to the current simple-critical-zero proportion, and it does not identify the entire uncertified complement with off-line zeros. Real doubles remain a zero-negative-index exceptional population, higher multiplicity and pure proof slack remain separately charged by WI-126/WI-137, and an extensive off-line population can still evade a quantitative improvement if its negative eigenvalues collapse sufficiently fast.

## 7. Prior-art and novelty audit

The linear-algebra mechanism is classical Sylvester inertia under congruence; no novelty is claimed for it, for signed Gram representations, or for Gram/Schur determinant identities. There is also direct zeta-function prior art. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I* (2000), showed for sufficiently large finite truncations of Weil's quadratic form, under a finite-off-line-zero hypothesis, that the number of negative eigenvalues is one half of the number of zeros off the critical line. Alpöge--Furman explicitly credit this negative-index observation to Bombieri and use Sylvester inertia in their 2026 matrix-compression proof.

A targeted audit of Lamzouri's preprint found no inertia, eigenvalue, or Sylvester formulation of Proposition 2.1. The public `AxiomMath/ZetaZeros` formalization likewise contains no inertia/eigenvalue layer in the current tree. Therefore (A) should be viewed as a **classical-principle specialization and bridge**, not as a new matrix theorem: once WI-126 supplies exact linear independence and WI-137 identifies the tensor with a self-adjoint operator, Lamzouri's `g/h` decomposition is itself a square invertible congruence of a signed diagonal form.

The durable Mathia content is the exact application to the Lamzouri tensor, the count/signature identities (8), and their coupling to the WI-137 quantitative slack and WI-132 Schur determinant. This restores, inside the newer Hilbert-space proof, the same fundamental distinction that Bombieri's and Alpöge--Furman's inertia viewpoints expose: off-line pairs carry unavoidable negative **index**, even when their negative **mass** is screened almost to zero.

## 8. Research implication

The defect-to-zero target is now sharper. For a near-extremizing sequence with positive-density off-line pairs, one no longer needs to prove the existence of negative directions; there are exactly as many as the pair count. What remains is to rule out their simultaneous collapse toward zero.

A successful bootstrap can therefore attack any one of the exact factors or consequences above: a lower bound on a positive-density set of negative eigenvalue magnitudes; a lower bound on the normalized odd Schur determinant or an extensive portion of its spectrum; a cluster-aware lower bound on the retained Gram determinant; or a zeta-accessible mixed moment/principal-minor identity incompatible with `k` extensive eigenvalues accumulating at zero while WI-137 simultaneously forces the positive spectrum toward the `2/1` target. Conversely, an explicit zeta-count-compatible family with `k\asymp N`, `Delta=o(N)`, and the required macroscopic near-zero negative cloud would be a decisive no-go for this inertia-to-zero bootstrap architecture.