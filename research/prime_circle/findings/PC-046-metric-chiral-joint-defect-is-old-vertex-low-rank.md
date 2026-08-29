# PC-046 — joint metric/chiral primitive coupling is an old-vertex low-rank defect

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NEGATIVE/OBSTRUCTION` for the natural same-level repair that combines the canonical unoriented inverse-square chord operator of PC-044 with the canonical oriented cotangent/Cauchy operator of PC-045 and hopes that their noncommutativity supplies a new bulk spectral mechanism. The full-polygon spectra are classical; the prime-circle-specific consequence is the exact compression identity showing that every failure of the two primitive blocks to satisfy the full polynomial relation is carried by the deleted old vertices, plus the constant mode. This does **not** rule out cross-level constructions, nonlinear invariants sensitive to low-rank defects, shell-dependent kernels, or global uniformization/monodromy.

PC-044 and PC-045 left a natural residual question. Each canonical single-level operator separately classicalizes in multiplicative-character coordinates, but perhaps the **joint pair** retains information that disappears when either matrix is studied alone. In particular, two individually classical Hermitian matrices can generate nontrivial noncommutative algebra after compression to the primitive shell.

For the two most intrinsic metric/chiral kernels, that escape is sharply restricted: on the complete regular polygon the inverse-square Laplacian is exactly a quadratic polynomial in the cotangent operator, and after primitive compression the only defect from that relation factors through the old-vertex space.

## 1. The two canonical full-polygon operators

Let

\[
z_a=e^{2\pi ia/n},\qquad a\in\mathbb Z/n\mathbb Z.
\]

Use the inverse-square chord Laplacian from PC-032/044,

\[
(\mathcal L_nf)_a
=
\sum_{b\ne a}
\frac{f_a-f_b}{|z_a-z_b|^2},
\]

and the oriented cotangent operator from PC-045,

\[
H_n^{\rm full}(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}n\right),&a\ne b,\\[2mm]0,&a=b.
\end{cases}
\]

Both are Hermitian circulants. On the normalized additive Fourier modes

\[
f_k(a)=n^{-1/2}e^{2\pi ika/n}
\]

their eigenvalues are

\[
\lambda_0=0,
\qquad
\lambda_k=\frac{k(n-k)}2
\quad(1\le k<n),
\]

and

\[
h_0=0,
\qquad
h_k=n-2k
\quad(1\le k<n).
\]

Let

\[
\Pi_0=\frac1n\mathbf 1\mathbf 1^*
\]

be the projection onto the constant Fourier mode. For every nonconstant mode,

\[
n^2-h_k^2
=n^2-(n-2k)^2
=4k(n-k)
=8\lambda_k,
\]

while both sides vanish on the constant mode. Hence the **exact matrix identity**

\[
\boxed{
8\mathcal L_n+(H_n^{\rm full})^2
=n^2(I-\Pi_0)
=n^2I-nJ_n,
}
\]

where `J_n=11*` is the all-ones matrix.

Thus on the full polygon the canonical metric and chiral operators are not independent at all: modulo the constant mode, the chord Laplacian is the quadratic spectral complement of the finite cotangent/Hilbert operator.

## 2. Primitive compression exposes exactly one defect: coupling through old vertices

Let

\[
U(n)=(\mathbb Z/n\mathbb Z)^\times
\]

index the primitive/new vertices and let `O(n)` be its complement. Geometrically, `O(n)` is precisely the union of the older birth shells embedded in `P_n`:

\[
P_n\setminus P_n^*
=
\bigsqcup_{\substack{d\mid n\\d<n}}P_d^*.
\]

Write the full cotangent operator in primitive/old block form

\[
H_n^{\rm full}
=
\begin{pmatrix}
K_n&B_n\\
B_n^*&C_n
\end{pmatrix},
\]

where

\[
K_n=H_n^{\rm full}[U(n),U(n)]
\]

is exactly the primitive cotangent block of PC-045, and `B_n` contains all chiral couplings from primitive vertices to old vertices. Likewise set

\[
A_n=\mathcal L_n[U(n),U(n)],
\]

the grounded primitive inverse-square block of PC-044.

Taking the primitive principal block of the full polynomial identity gives

\[
P(H_n^{\rm full})^2P
=K_n^2+B_nB_n^*.
\]

Therefore

\[
\boxed{
8A_n+K_n^2+B_nB_n^*
=n^2I_{\varphi(n)}-nJ_{\varphi(n)}.
}
\]

Equivalently,

\[
\boxed{
A_n
=\frac18\left(
 n^2I-nJ-K_n^2-B_nB_n^*
\right).
}
\]

The term

\[
\boxed{D_n:=B_nB_n^*\succeq0}
\]

is the entire failure of primitive compression to preserve the full-polygon quadratic relation. It factors through the old-vertex coordinate space, so

\[
\boxed{
\operatorname{rank}D_n
\le n-\varphi(n).
}
\]

This gives the residual joint structure a direct geometric meaning: it is not an unexplained interaction created inside the primitive shell. It is exactly the virtual excursion

\[
\boxed{
\text{primitive}\to\text{old vertices}\to\text{primitive}
}
\]

that is lost when the full polynomial identity is compressed.

## 3. The commutator is supported by the same boundary defect

The strongest candidate for genuinely new same-level information is not the two spectra separately but their failure to commute. Commuting the compression identity with `K_n` yields

\[
\boxed{
8[A_n,K_n]
=-n[J,K_n]-[D_n,K_n].
}
\]

Since `J` has rank one and `D_n` has rank at most `n-phi(n)`, the elementary bound `rank([X,K]) <= 2 rank(X)` gives

\[
\boxed{
\operatorname{rank}[A_n,K_n]
\le
\min\!\left(
\varphi(n),
2\bigl(n-\varphi(n)+1\bigr)
\right).
}
\]

Thus **all same-level metric/chiral noncommutativity is generated by the constant direction and the deleted old-vertex sector**. There is no independent full-rank noncommutative bulk term hidden in the two canonical kernels.

For a squarefree semiprime `n=pq`,

\[
n-\varphi(n)=p+q-1,
\]

so

\[
\boxed{
\frac{\operatorname{rank}[A_{pq},K_{pq}]}{\varphi(pq)}
\le
\min\!\left(
1,
\frac{2(p+q)}{(p-1)(q-1)}
\right).
}
\]

Along semiprimes with `p,q -> infinity`, this upper bound tends to zero. The first multi-prime primitive blocks can certainly fail to commute, but in normalized rank their noncommutativity is an asymptotically thin old-shell defect rather than an extensive new bulk algebra.

This is a rank statement, not an operator-norm statement. A low-rank defect can still move special eigenvalues, determinants, or resolvents substantially, so those possibilities are not being silently discarded.

## 4. Prime levels collapse even further

For prime `p`, the old-vertex space contains only the common anchor `0`, corresponding to the root `1`. Hence `B_p` is a single column `b`.

The full cotangent operator annihilates constants,

\[
H_p^{\rm full}\mathbf 1=0.
\]

Restricting this identity to primitive rows gives

\[
b=-K_p\mathbf 1.
\]

Therefore

\[
\boxed{
B_pB_p^*=K_pJ K_p,
}
\]

and the joint relation becomes

\[
\boxed{
8A_p+K_p^2+K_pJK_p
=p^2I-pJ.
}
\]

So at a prime level the complete inverse-square primitive block is algebraically reconstructed from the cotangent primitive block together with the universally distinguished constant vector. There is no second independent same-level operator hiding behind the metric/chiral split.

This is consistent with PC-038: removing or pointing one vertex of a circulant can produce nontrivial local response, but that response is derivative/rank-one data of the original cyclic spectrum rather than a new spectral degree of freedom.

## 5. What this closes and what remains genuinely open

PC-044 showed that the squarefree primitive inverse-square block is finite `L(-1)` / generalized-Bernoulli mixing. PC-045 showed that its canonical oriented counterpart is finite `L(0)` / Bernoulli mixing. It remained possible that **combining** those two matrices before diagonalizing might create a qualitatively new noncommutative carrier.

The identity above rules out that interpretation in its naive extensive form. The full operators commute because one is a quadratic function of the other; after primitive compression, every failure of that relation factors through old vertices. Thus the natural route

\[
\boxed{
\text{primitive metric block }A_n
+\text{ primitive chiral block }K_n
\to
\text{new same-level bulk noncommutative spectrum}
\to
\text{RH}
}
\]

is obstructed: the noncommutative part is exactly a deletion/boundary defect of controlled rank.

The result deliberately does **not** close several stronger possibilities:

- nonlinear invariants specifically designed to amplify the low-rank old-shell defect `D_n`;
- cross-level operators that retain the old shells as active states rather than compressing them away;
- simultaneous couplings of several birth levels before forming any principal block;
- shell-dependent kernels not obtained by compressing one universal circulant;
- continuous parameters forced by the geometry rather than inserted into a functional calculus;
- the global primitive-only uniformization/monodromy sector of PC-017.

Indeed the formula identifies where any viable continuation of this specific idea must live: **in the old/new coupling itself**, not in treating `A_n` and `K_n` as two independent primitive-shell observables.

## 6. Prior-art and novelty audit

The full-polygon ingredients are classical. Calogero and Perelomov compute the spectra of the finite cotangent and `csc^2` circulant matrices and the corresponding trigonometric Fourier sums; those formulas are already anchored in `research/prime_circle/SOURCES.md` for the inverse-square branch and are the spectral input used by PC-032 and PC-045. From those two classical spectra, the full identity

\[
8\mathcal L_n+(H_n^{\rm full})^2=n^2(I-\Pi_0)
\]

is immediate by simultaneous Fourier diagonalization.

Targeted literature searches for a principal-compression identity joining these two particular root-of-unity operators did not locate the displayed `B_nB_n^*` defect formula. That absence is not evidence of historical priority. The block identity itself is elementary linear algebra once the full polynomial relation is known, and no general theorem novelty is claimed.

The durable project-specific content is the **information-loss classification** relevant to the prime-circle program: compressing both canonical kernels to the primitive shell cannot generate independent bulk noncommutativity; the exact discrepancy is a positive semidefinite factor through the already-existing lower-order vertices.

## 7. Exact audit and falsification tests

The obstruction is finite-dimensional and admits direct exact or high-precision checks:

1. diagonalize both full circulants and verify `8 lambda_k+h_k^2=n^2` for every nonconstant Fourier mode and zero on the constant mode;
2. block `H_n^{full}` by primitive versus nonprimitive vertices and verify `P H^2 P=K_n^2+B_nB_n^*`;
3. compare the resulting primitive identity entry by entry with the direct principal block of `mathcal L_n`;
4. verify `D_n=B_nB_n^*` is positive semidefinite and has rank at most `n-phi(n)`;
5. compute the commutator and check the displayed rank bound;
6. at prime `p`, verify `b=-K_p 1` and hence `D_p=K_pJK_p`.

Direct numerical constructions at `n=5,8,15,21` reproduce the full and compressed identities to floating-point precision; the prime `n=5` case also reproduces `D_p=K_pJK_p`. These computations are checks only—the claim rests on the exact Fourier and block derivation above.

Failure of the full polynomial identity or of the block factorization would invalidate the result. No claim is made that low-rank defects are spectrally negligible in norm, that every joint nonlinear invariant is classical, or that this obstruction settles any part of RH.