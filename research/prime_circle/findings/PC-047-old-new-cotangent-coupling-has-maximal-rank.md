# PC-047 — old/new cotangent coupling has maximal possible rank

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CORRECTION`. For the canonical same-level pairing of the primitive/new shell with the inherited old vertices through the intrinsic cotangent/Cauchy kernel, the old/new coupling has the **largest rank allowed by its rectangular dimensions**, except for the balanced power-of-two case where there is exactly one dependency. Consequently the compression defect in the joint metric/chiral identity is often full rank on the primitive shell. The exact factorization through old vertices remains valid and is an information-provenance statement, but it is not a general low-rank obstruction.

PC-044 and PC-045 classify separately the primitive inverse-square and oriented cotangent blocks. On the full regular polygon those two operators satisfy an elementary polynomial relation. Compressing to the primitive shell leaves a defect that factors through the deleted old vertices. The key question is whether this factorization forces that defect to be small.

It does not. The cotangent block is a Cauchy-type matrix whose rectangular rank can be evaluated exactly.

## 1. Full-polygon relation and the old/new defect

Let

\[
z_a=e^{2\pi ia/n},\qquad a\in\mathbb Z/n\mathbb Z,
\]

and retain the two canonical Hermitian circulants

\[
(\mathcal L_nf)_a
=
\sum_{b\ne a}
\frac{f_a-f_b}{|z_a-z_b|^2}
\]

and

\[
H_n^{\rm full}(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}n\right),&a\ne b,\\[2mm]
0,&a=b.
\end{cases}
\]

Their additive Fourier eigenvalues are

\[
\lambda_0=0,\qquad
\lambda_k=\frac{k(n-k)}2
\]

and

\[
h_0=0,\qquad h_k=n-2k\quad(1\le k<n).
\]

Hence, with \(\Pi_0=n^{-1}\mathbf 1\mathbf 1^*\),

\[
\boxed{
8\mathcal L_n+(H_n^{\rm full})^2
=n^2(I-\Pi_0)
=n^2I-nJ_n.
}
\]

Let

\[
U=U(n)=(\mathbb Z/n\mathbb Z)^\times,
\qquad
O=(\mathbb Z/n\mathbb Z)\setminus U,
\]

so that \(U\) indexes the primitive/new vertices and \(O\) the inherited old vertices. Put

\[
A_n=\mathcal L_n[U,U],
\qquad
K_n=H_n^{\rm full}[U,U],
\qquad
B_n=H_n^{\rm full}[U,O].
\]

Taking the \(U\times U\) block of the full identity gives

\[
\boxed{
8A_n+K_n^2+B_nB_n^*
=n^2I_{\varphi(n)}-nJ_{\varphi(n)}.
}
\]

Thus

\[
\boxed{D_n:=B_nB_n^*\succeq0}
\]

is exactly the defect produced by virtual excursions

\[
\text{primitive}\longrightarrow\text{old}\longrightarrow\text{primitive}.
\]

This factorization is exact. What requires separate analysis is its rank.

## 2. Every square old/new minor is a Cauchy double alternant times one product factor

For a primitive row \(a\in U\) and an old column \(b\in O\), write

\[
x=\zeta_n^a,\qquad y=\zeta_n^b.
\]

Then

\[
\boxed{
B_n(a,b)
=i\cot\frac{\pi(a-b)}n
=
\frac{x+y}{y-x}.
}
\]

Choose any \(k\) primitive roots \(x_1,\ldots,x_k\) and any \(k\) old roots
\(y_1,\ldots,y_k\), and let \(M\) be the corresponding square minor. Put

\[
X=\prod_{i=1}^k x_i,
\qquad
Y=\prod_{j=1}^k y_j,
\qquad
C_{ij}=\frac1{x_i-y_j}.
\]

A direct rank-one reduction of the classical Cauchy matrix gives

\[
\boxed{
\det M
=
(-1)^k\,2^{k-1}(X+Y)\det C.
}
\]

Since the two root sets are disjoint and contain no repetitions, the Cauchy double alternant satisfies

\[
\det C\ne0.
\]

Therefore the exact vanishing criterion for every square old/new minor is simply

\[
\boxed{
\det M=0
\iff
\prod_i x_i=-\prod_j y_j.
}
\]

For completeness, one short derivation is as follows. With
\(D_x=\operatorname{diag}(x_i)\),

\[
-M=2D_xC-J.
\]

The matrix determinant lemma reduces the extra factor to a scalar involving
\(C^{-1}(x_i^{-1})\). If

\[
R(t)=\sum_j\frac{u_j}{t-y_j}
\]

interpolates \(1/t\) at the \(x_i\), comparison of the numerator polynomial at
\(t=0\) gives

\[
\sum_j u_j=1-\frac{Y}{X}.
\]

Substitution yields the displayed determinant formula. The only external
ingredient is the classical Cauchy determinant; see, for example, Samuel
Schechter, *On the Inversion of Certain Matrices*, Mathematical Tables and
Other Aids to Computation **13** (1959), 73–77.

## 3. Exact rank of the old/new cotangent coupling

Set

\[
r=\varphi(n),
\qquad
s=n-\varphi(n).
\]

If \(r<s\), fix all \(r\) primitive rows. Among the \(r\)-element subsets of
the \(s\) old roots, not all products can equal the same value: two subsets
differing in one root would otherwise force two distinct roots to coincide.
Hence one \(r\times r\) minor has \(X+Y\ne0\), so

\[
\operatorname{rank}B_n=r.
\]

The same argument with rows and columns exchanged gives rank \(s\) when
\(s<r\).

When \(r=s\), the full square determinant vanishes. Indeed
\(\varphi(n)=n/2\) holds exactly for powers of \(2\). For \(n>2\), the product
of all primitive \(n\)-th roots is \(1\), whereas the product of all \(n\)-th
roots is \(-1\); hence the product of all old roots is \(-1\). The determinant
criterion gives \(X+Y=0\). A minor of order \(r-1\) is nonzero by the same
subset-product argument. The case \(n=2\) also has rank \(0=r-1\).

Thus, for every \(n>1\),

\[
\boxed{
\operatorname{rank}B_n=
\begin{cases}
\min\!\bigl(\varphi(n),\,n-\varphi(n)\bigr),
&\varphi(n)\ne n/2,\\[2mm]
\varphi(n)-1,
&\varphi(n)=n/2.
\end{cases}
}
\]

Equivalently, the exceptional second line is exactly \(n=2^m\).

Because \(D_n=B_nB_n^*\),

\[
\boxed{\operatorname{rank}D_n=\operatorname{rank}B_n.}
\]

So the old/new defect is not merely capable of being full rank: its rank is
**maximal possible** for the rectangular coupling.

## 4. Squarefree consequence: the defect is frequently full rank

For every even \(n\) having an odd prime divisor,

\[
\frac{\varphi(n)}n
=
\frac12\prod_{\substack{p\mid n\\p\ {\rm odd}}}
\left(1-\frac1p\right)
<\frac12.
\]

Therefore

\[
\boxed{
\operatorname{rank}D_n=\varphi(n)
}
\]

and \(D_n\) is positive definite on the entire primitive coordinate space.

In particular, for **every even squarefree composite level \(n>2\)**, the
old/new defect is full rank. The first example is \(n=6\), and the example
\(n=30\) is not a marginal case: its \(8\times8\) defect has rank exactly \(8\).

Odd squarefree levels split according to the same dimension comparison:

\[
\boxed{
\operatorname{rank}D_n
=
\min\!\bigl(\varphi(n),\,n-\varphi(n)\bigr).
}
\]

Thus large odd semiprimes remain a genuinely thin-deletion regime:
for \(n=pq\),

\[
n-\varphi(n)=p+q-1,
\]

which is \(o(\varphi(n))\) when \(p,q\to\infty\). But once enough prime factors
are present, \(\varphi(n)/n\) can fall below \(1/2\) and the defect becomes full
rank again; for example \(n=105\) has \(\varphi(105)=48<57\).

The correct structural statement is therefore not “old vertices imply low
rank.” It is

\[
\boxed{
\text{old vertices determine the provenance of the defect, while their
number determines whether the defect is thin or full rank.}
}
\]

## 5. The commutator can also be full rank

Commuting the compression identity with \(K_n\) still gives

\[
\boxed{
8[A_n,K_n]
=-n[J,K_n]-[D_n,K_n].
}
\]

The general upper bound

\[
\operatorname{rank}[A_n,K_n]
\le
\min\!\left(
\varphi(n),
2\bigl(n-\varphi(n)+1\bigr)
\right)
\]

remains correct, but it is informative only when the old sector is small.

There is an exact squarefree counterexample to any global rank-deficiency
interpretation already at \(n=6\). With primitive indices \(1,5\),

\[
A_6=
\begin{pmatrix}
35/12&-1/3\\
-1/3&35/12
\end{pmatrix},
\qquad
K_6=
\begin{pmatrix}
0&i/\sqrt3\\
-i/\sqrt3&0
\end{pmatrix},
\]

and hence

\[
\boxed{
[A_6,K_6]
=
\begin{pmatrix}
2\sqrt3\,i/9&0\\
0&-2\sqrt3\,i/9
\end{pmatrix},
\qquad
\det[A_6,K_6]=\frac4{27}\ne0.
}
\]

So same-level metric/chiral noncommutativity can occupy the full primitive
space even though it is generated entirely by the old/new compression
defect.

## 6. What remains valid and what the exact rank changes

Several useful conclusions survive unchanged:

- on the complete polygon, \(\mathcal L_n\) is a quadratic polynomial in the
  cotangent operator modulo the constant mode;
- after primitive compression, the entire discrepancy is exactly
  \(B_nB_n^*\), so the extra same-level information is localized
  conceptually in old/new coupling rather than in two independent universal
  bulk kernels;
- at a prime level the old sector is only the common anchor, and the defect is
  rank one; using \(H_p^{\rm full}\mathbf1=0\) gives
  \(B_pB_p^*=K_pJK_p\), so \(A_p\) is reconstructed from \(K_p\) and the
  distinguished constant vector;
- along large semiprimes, the normalized rank bound really does tend to zero.

What does **not** survive is a global no-go based on low rank. At squarefree
levels such as \(6,30,42,105,\ldots\), the old/new defect can be full rank, and
at \(n=6\) the metric/chiral commutator is already full rank.

Therefore the joint same-level route cannot be dismissed merely by saying
that compression introduces a low-dimensional boundary correction. A viable
continuation would have to study the structured matrix \(B_nB_n^*\) itself,
or a cross-level/nonlinear invariant built from it, and then pass the same
novelty gate already used for the separate `L(-1)` and `L(0)` blocks.

No RH mechanism follows from maximal rank. Rank alone supplies neither a
complex spectral parameter nor a critical-line symmetry. The correction is
instead an information-preservation result: **the old/new coupling is large
enough to remain a legitimate carrier and must be analyzed rather than
discarded on dimensional grounds.**

## 7. Prior-art and novelty audit

The analytic ingredients are classical:

- the full cotangent and inverse-square regular-polygon spectra are the
  Calogero–Perelomov trigonometric matrix identities already used in
  PC-032/PC-045;
- the square-minor evaluation above is a rank-one variant of Cauchy's double
  alternant, with the standard Cauchy determinant and inverse/interpolation
  formulas available in Schechter (1959);
- \(\varphi(n)=n/2\) exactly for powers of \(2\) is elementary arithmetic.

No novelty claim is made for those ingredients. Directed searches around
Cauchy/cotangent determinants confirm that this determinant technology is
classical. The durable prime-circle contribution is the consequence for the
specific primitive/old partition forced by the roots-of-unity birth geometry:

\[
\boxed{
\text{the canonical chiral old/new coupling has maximal rectangular rank.}
}
\]

This changes the research boundary materially. The factorization through old
vertices remains exact, but it should be read as a structural localization
of information, not as a general low-rank or no-bulk theorem.

## 8. Exact falsification tests

The result can be checked without fitting:

1. verify the full Fourier identity
   \(8\mathcal L_n+(H_n^{\rm full})^2=n^2(I-\Pi_0)\);
2. block by primitive versus old vertices and recover
   \(8A_n+K_n^2+B_nB_n^*=n^2I-nJ\);
3. for arbitrary equal-size row/column subsets, substitute
   \(B(a,b)=(x+y)/(y-x)\) and verify the Cauchy-minor determinant;
4. use distinctness of the roots to prove existence of a nonzero maximal
   minor whenever the rectangle is unbalanced;
5. in the balanced case use the products of primitive and old roots to show
   the full determinant vanishes, then exhibit a nonzero minor of order one
   less;
6. verify directly that
   \(\operatorname{rank}D_n=\operatorname{rank}B_n\);
7. at \(n=6\), compute the displayed matrices and the nonzero commutator
   determinant \(4/27\).

A failure of the square-minor determinant formula or of the maximal-rank
argument would invalidate the correction. No claim is made that a full-rank
defect yields new zeta information, that its spectrum is nonclassical, or
that cross-level combinations evade the existing prime-circle no-go results.
