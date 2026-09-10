# PC-246 — prime-prime transfer spectrum is one signed modular residue

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `NEGATIVE/OBSTRUCTION` for the simplest simultaneous-growth escape left open by PC-245. For distinct primes \(p<q\), the finite polyphase packet \(K_{p,q}\) of the native transfer \(W_p^*W_q\) is exactly the overlap matrix of the \(p\)- and \(q\)-block partitions of a \(pq\)-point interval. Its Gram matrix is

\[
\boxed{
K_{p,q}^*K_{p,q}=pq\,I_p-L_{p,h},
\qquad h\equiv q\pmod p,
}
\]

where \(L_{p,h}\) is a weighted path Laplacian with edge weights
\[
w_k=(hk\bmod p)\bigl(p-(hk\bmod p)\bigr),
\qquad 1\le k<p.
\]
After removing the elementary scalar \(pqI_p\), the complete singular spectrum depends on \(q\) only through the signed residue class \(q\bmod p\) up to \(h\leftrightarrow p-h\); conversely its second spectral moment recovers exactly that signed residue. Thus the first canonical growing family of PC-245 packets does not produce an additional spectral variable: at fixed lower prime \(p\), its centered spectrum is equivalent to one modular remainder.

This is not a no-go for simultaneous growth of more complicated packet networks. It is a sharp boundary for **pairwise native prime-shell transfers**. A surviving all-scale packet mechanism must use a relation among several conductors, a nontrivial normalization/limit, nonlinear data, or another source-forced structure not already determined by pairwise Euclidean residue data.

## 1. Prime masks turn the PC-245 packet into a block-overlap matrix

Use the native Hardy weighted covers from PC-245,
\[
W_n=M_{\Phi_n}C_n,\qquad (C_nf)(z)=f(z^n).
\]
For distinct primes \(p<q\),
\[
\Phi_p(z)=\sum_{i=0}^{p-1}z^i,\qquad
\Phi_q(z)=\sum_{j=0}^{q-1}z^j.
\]
Since \((p,q)=1\), PC-245 gives a \(q\times p\) packet
\[
K_{p,q}(u,t)=\kappa_{pu-qt}^{p,q},
\qquad
0\le u<q,\quad 0\le t<p,
\tag{1}
\]
where
\[
\kappa_r^{p,q}
=\#\{(i,j):0\le i<p,\ 0\le j<q,\ j-i=r\}.
\tag{2}
\]

Partition the integer interval \(\{0,\ldots,pq-1\}\) in the two canonical ways
\[
I_u=\{pu,\ldots,p(u+1)-1\},\qquad 0\le u<q,
\tag{3}
\]
and
\[
J_t=\{qt,\ldots,q(t+1)-1\},\qquad 0\le t<p.
\tag{4}
\]
The equation contributing to (1),
\[
pu+i=qt+j,
\tag{5}
\]
identifies the coefficient pair \((i,j)\) with one point of \(I_u\cap J_t\). Hence

\[
\boxed{
K_{p,q}(u,t)=|I_u\cap J_t|.
}
\tag{6}
\]

No asymptotic or choice of coordinates is involved. The native prime cyclotomic masks are precisely the all-one short masks, and their adjoint transfer packet is the incidence/overlap matrix of two uniform interval partitions.

Every \(I_u\) has \(p\) points and every \(J_t\) has \(q\) points, so
\[
K_{p,q}\mathbf 1_p=p\mathbf 1_q,
\qquad
K_{p,q}^*\mathbf 1_q=q\mathbf 1_p.
\tag{7}
\]

## 2. The packet Gram matrix is exactly a modular weighted path

Because \(q>p\), a \(p\)-block \(I_u\) can cross at most one boundary between consecutive \(q\)-blocks. Therefore two different columns of \(K_{p,q}\) have common support only when they are adjacent, so
\[
G_{p,q}:=K_{p,q}^*K_{p,q}
\tag{8}
\]
is tridiagonal.

For \(1\le k<p\), let
\[
r_k\equiv qk\pmod p,\qquad 1\le r_k<p.
\tag{9}
\]
The unique \(p\)-block containing the boundary \(qk\) is split by that boundary into pieces of lengths \(r_k\) and \(p-r_k\). Consequently
\[
(G_{p,q})_{k-1,k}
=(G_{p,q})_{k,k-1}
=r_k(p-r_k)=:w_k.
\tag{10}
\]

Equation (7) gives
\[
G_{p,q}\mathbf 1_p=pq\,\mathbf 1_p.
\tag{11}
\]
Thus the diagonal is forced by the adjacent off-diagonal entries. With \(w_0=w_p=0\), define the weighted path Laplacian
\[
(L_{p,h})_{kk}=w_k+w_{k+1},
\qquad
(L_{p,h})_{k-1,k}=(L_{p,h})_{k,k-1}=-w_k,
\tag{12}
\]
where
\[
h\equiv q\pmod p,\qquad
w_k=(hk\bmod p)\bigl(p-(hk\bmod p)\bigr).
\tag{13}
\]
Then

\[
\boxed{
G_{p,q}=pq\,I_p-L_{p,h}.
}
\tag{14}
\]

In particular \(L_{p,h}\ge0\), \(L_{p,h}\mathbf 1=0\), and the top singular value of \(K_{p,q}\) is exactly \(\sqrt{pq}\). All remaining squared singular values are \(pq-\lambda_j(L_{p,h})\).

This already shows the basic loss of pairwise arithmetic. At fixed \(p\), changing \(q\) while preserving \(q\bmod p\) changes the Gram spectrum only by the elementary scalar shift \(p(q'-q)\). The centered matrix itself is identical.

## 3. The complete centered spectrum is equivalent to \(q\bmod p\) up to sign

Multiplication by the nonzero residue \(h\) permutes \(\{1,\ldots,p-1\}\), so the unordered edge weights have universal first and second power sums:
\[
\sum_{k=1}^{p-1}w_k
=\sum_{r=1}^{p-1}r(p-r)
=\frac{p(p^2-1)}6,
\tag{15}
\]
and
\[
S_2:=\sum_{k=1}^{p-1}w_k^2
=\sum_{r=1}^{p-1}r^2(p-r)^2
=\frac{p(p^4-1)}{30}.
\tag{16}
\]
Hence
\[
\operatorname{tr}L_{p,h}
=2\sum_kw_k
=\frac{p(p^2-1)}3
\tag{17}
\]
is independent of \(h\). The first centered spectral moment therefore contains no residue information.

The second moment does. Put
\[
x=h(p-h),\qquad 1\le h<p.
\tag{18}
\]
The adjacent-edge correlation
\[
C_p(h):=\sum_{k=1}^{p-2}w_kw_{k+1}
\tag{19}
\]
can be evaluated exactly. Since the zero residue contributes nothing, it is the cyclic correlation of
\[
f(r)=r(p-r),\qquad r=0,\ldots,p-1,
\]
at shift \(h\):
\[
C_p(h)=\sum_{r\bmod p}f(r)f(r+h).
\tag{20}
\]
Splitting at the wrap point gives
\[
\begin{aligned}
C_p(h)
={}&\sum_{r=0}^{p-h-1}
r(p-r)(r+h)(p-r-h)\\
&+\sum_{r=p-h}^{p-1}
r(p-r)(r+h-p)(2p-r-h).
\end{aligned}
\tag{21}
\]
Using the standard finite sums through degree four yields

\[
\boxed{
C_p(h)
=\frac{p(p^4-1)}{30}
-\frac p6\,x(x+2).
}
\tag{22}
\]

For a weighted path,
\[
\operatorname{tr}L_{p,h}^2
=4S_2+2C_p(h),
\]
so (16) and (22) give

\[
\boxed{
\operatorname{tr}L_{p,h}^2
=
\frac{p(p^4-1)}5
-\frac p3\,x(x+2).
}
\tag{23}
\]

The map \(h\mapsto h(p-h)\) is strictly increasing on
\(1\le h\le(p-1)/2\), and \(h\) and \(p-h\) produce the same edge
weights pointwise. Therefore, for fixed \(p\),

\[
\boxed{
\operatorname{Spec}(L_{p,h})
\quad\Longleftrightarrow\quad
h=q\bmod p\ \text{up to }h\leftrightarrow p-h.
}
\tag{24}
\]

The reverse implication is immediate from (13). For the forward implication, the spectrum gives (23), hence \(x(x+2)\), hence \(x\ge0\), and finally \(h\) up to the only symmetry \(h\leftrightarrow p-h\).

Thus **the entire centered singular spectrum contains exactly one signed modular residue and no finer dependence on the upper prime**. Higher spectral moments cannot restore information already absent from the matrix.

A second invariant emphasizes the same rigidity. The weighted matrix-tree theorem for a path gives
\[
\operatorname{pdet}L_{p,h}
=p\prod_{k=1}^{p-1}w_k.
\tag{25}
\]
Again multiplication by \(h\) permutes the nonzero residues, so
\[
\boxed{
\operatorname{pdet}L_{p,h}
=p\bigl((p-1)!\bigr)^2,
}
\tag{26}
\]
independent of \(q\).

## 4. The residue \(q\equiv\pm1\pmod p\) is an exactly solvable classical difference operator

When \(h=\pm1\),
\[
w_k=k(p-k),
\tag{27}
\]
because the sign change sends \(k\) to \(p-k\) and leaves the product
unchanged. On vertices \(t=0,\ldots,p-1\),
\[
\begin{aligned}
(L_{p,1}f)(t)
={}&t(p-t)\bigl(f(t)-f(t-1)\bigr)\\
&+(t+1)(p-1-t)\bigl(f(t)-f(t+1)\bigr),
\end{aligned}
\tag{28}
\]
with the vanishing boundary coefficients supplying the endpoint convention.

This operator preserves the space of polynomials of each degree. Acting on
\(t^j\), the coefficient of \(t^j\) is \(j(j+1)\), while all remaining
terms have lower degree. Since \(L_{p,1}\) is real symmetric, its
eigenvalues are therefore

\[
\boxed{
\operatorname{Spec}(L_{p,\pm1})
=\{j(j+1):0\le j<p\}.
}
\tag{29}
\]
Consequently
\[
\boxed{
\operatorname{Spec}(K_{p,q}^*K_{p,q})
=
\{pq-j(j+1):0\le j<p\}
\quad\text{if }q\equiv\pm1\pmod p.
}
\tag{30}
\]

This is the standard Hahn/discrete-Chebyshev difference operator
(\(\alpha=\beta=0\), \(N=p-1\)). The NIST Digital Library of
Mathematical Functions, §§18.19 and 18.22, records the Hahn family and
its difference equation with spectral parameter
\(j(j+\alpha+\beta+1)\):
https://dlmf.nist.gov/18.19 and https://dlmf.nist.gov/18.22.
Thus even the most explicitly solvable residue sector is classical
finite orthogonal-polynomial structure, not a new zeta spectral law.

For example, \(p=5,q=11\) gives
\[
\operatorname{Spec}(K^*K)=\{55,53,49,43,35\},
\tag{31}
\]
and \(p=7,q=13\) gives
\[
\{91,89,85,79,71,61,49\}.
\tag{32}
\]

## 5. Matched controls

The overlap identity (6) and the weighted-path reduction (14) do not use
primality after the two masks have been chosen to be all ones. For any
coprime integers \(a<b\), use the short masks
\[
P_a(z)=1+z+\cdots+z^{a-1},\qquad
P_b(z)=1+z+\cdots+z^{b-1}
\tag{33}
\]
with cover factors \(a,b\), even when those factors are composite and
the masks are not the native exact-order cyclotomic polynomials
\(\Phi_a,\Phi_b\). The resulting PC-245 packet is again the overlap
matrix of the \(a\)- and \(b\)-block partitions and satisfies the same
modular weighted-path formula. Thus the path/overlap mechanism does not
detect that the conductors are prime.

The stronger nonarithmetic control from PC-245 also remains relevant:
arbitrary short FIR masks have the same polyphase/affine transfer
architecture. Their coefficient weights need not satisfy the special
residue-only formula (13), so the exact modular collapse here uses the
all-one mask shape that prime cyclotomy supplies. What is generic is the
finite polyphase carrier and its interval-overlap support; what is
Prime-Circle-specific in this subfamily is only the distinguished
all-one choice and the resulting elementary residue weights. This
separation prevents attributing the ambient spectral architecture to
prime arithmetic.

## 6. Prior-art and novelty audit

PC-245 already places finite adjoint transfers inside classical
polyphase/filter-bank and affine \(ax+b\) operator architecture, with
Cuntz and Brownlowe--an Huef--Laca--Raeburn as the durable operator
algebra anchors in `research/prime_circle/SOURCES.md`. The present
calculation does not claim novelty for polyphase decomposition,
partition-overlap matrices, weighted path Laplacians, the matrix-tree
theorem, finite power sums, or Hahn polynomials.

A structure-based literature check also finds the \(h=\pm1\) operator
inside the standard Hahn class: DLMF §18.22 gives the second-order Hahn
difference equation and the eigenvalue \(j(j+\alpha+\beta+1)\), which
specializes to (29). Generic polyphase matrices are standard filter-bank
machinery as already recorded by PC-245. No prior-art search result is
being used as an absence proof.

The project-local delta is narrower and exact: **the source-forced
prime--prime packet singled out by PC-245's open simultaneous-growth
boundary admits the explicit reduction (14), and its centered singular
spectrum is neither a new continuous parameter nor a hidden global
prime invariant; it is precisely \(q\bmod p\) up to sign.** That
consequence follows from the Prime-Circle packet formula and the exact
second-moment inversion (23), irrespective of terminology.

This does not make modular prime residues irrelevant. An aggregate over
many pairs could encode prime distribution in residue classes. Such an
aggregate would, however, be a genuinely new many-conductor object and
would have to be audited against classical Dirichlet/Farey/cyclotomic
dynamics rather than credited to the pairwise spectrum itself.

## 7. Consequence for the Prime-Circle frontier

PC-245 left open a source-forced **growing family** of finite coefficient
packets as the nearest way to escape finite-depth affine
classicalization. PC-246 tests the first canonical such family instead
of adding another fixed packet: let two prime conductors grow and retain
the full singular spectrum of their transfer.

For one pair, the answer is rigid. Once the elementary \(pqI\) bulk is
removed, all spectral dependence on the second prime collapses to one
signed Euclidean remainder. In particular, whenever two primes \(q,q'>p\)
satisfy
\[
q'\equiv\pm q\pmod p,
\]
their centered prime--prime transfer spectra are exactly identical.

Accordingly, a serious next packet mechanism cannot rely on pairwise
singular spectra alone. It must derive a nontrivial law from **jointly
coupled triples or larger conductor families**, from a source-forced
many-scale normalization/limit, or from structure outside the native
finite weighted-cover packet algebra. Any such construction must still
survive the nonarithmetic all-one-mask control and must show where its
information exceeds the collection of classical modular residues.

## Falsification and audit checks

The result is exactly auditable from PC-245. For distinct primes \(p<q\):

1. compute \(K_{p,q}\) from PC-245 equation (7) and verify the overlap
   identity (6);
2. check that only adjacent columns overlap and that their inner product
   at the \(qk\) boundary is \(r_k(p-r_k)\);
3. verify \(K^*K\mathbf1=pq\mathbf1\), which forces (14);
4. evaluate the finite sums (21) and verify (22)--(23);
5. recover \(h\) up to sign from the second spectral moment;
6. verify (26) from the weighted path cofactor;
7. in the \(h=\pm1\) case, check directly that (28) preserves polynomial
   degree with leading eigenvalue \(j(j+1)\);
8. repeat the construction with the same all-one masks at coprime
   composite cover lengths, where they are not the native exact-order
   masks \(\Phi_a,\Phi_b\), and separately compare with PC-245's
   arbitrary-short-mask control.

Any failure of (6), (14), or (23) invalidates the main classification.
The result makes no numerical-fit, asymptotic, or RH claim.
