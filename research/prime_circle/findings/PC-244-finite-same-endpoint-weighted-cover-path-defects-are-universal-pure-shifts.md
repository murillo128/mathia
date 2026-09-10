# PC-244 — finite same-endpoint weighted-cover path defects are universal pure shifts

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the finite scalar path-interference escape left open by PC-210 and still visible at the boundary of PC-243. If several intrinsic cyclotomic-weighted refinement paths have the same total covering degree and are compared by a scalar linear combination that cancels their common endpoint baseline, the resulting relational defect is either exactly zero or, after one scalar normalization, the universal unilateral shift of countably infinite multiplicity. This includes pairwise refinement commutators and the direct-composite-versus-prime-factorization defect. The only surviving norm data are finite coefficient correlations of cyclotomic path masks; for the direct-versus-prime-path comparison they reduce exactly to `N`, the classical coefficient energy `h_N`, and the classical value `Phi_N(1)`.

This closes finite **linear coherent interference among forward paths with a fixed endpoint**. It does not classify a joint path-labelled algebra before scalar combination, interleaved adjoints/transfer operators involving native composite masks, matrix-valued path couplings, simultaneous growth in endpoint and path family, nonlinear/off-circle interactions, or global uniformization/accessory data.

## 1. Every forward refinement path has one endpoint block mask

Work on `H^2(D)` with monomial basis `e_k(z)=z^k`, `k>=0`, and retain the source-forced weighted covers of PC-209,

\[
W_n:=M_{\Phi_n}C_n,
\qquad
(C_nf)(z)=f(z^n),
\qquad n\ge2.
\tag{1}
\]

For a finite ordered path

\[
\mathbf n=(n_1,\ldots,n_r),
\qquad
N_j:=\prod_{i=1}^j n_i,
\qquad N_0:=1,
\qquad N:=N_r,
\tag{2}
\]

repeated use of `C_m M_g=M_{g(z^m)}C_m` gives the exact identity already underlying PC-210,

\[
A_{\mathbf n}:=W_{n_1}\cdots W_{n_r}
=M_{G_{\mathbf n}}C_N,
\tag{3}
\]

with

\[
G_{\mathbf n}(z)
=\prod_{j=1}^r
\Phi_{n_j}\!\left(z^{N_{j-1}}\right).
\tag{4}
\]

Because `deg Phi_n=varphi(n)<=n-1`,

\[
\deg G_{\mathbf n}
=\sum_{j=1}^r N_{j-1}\varphi(n_j)
\le N-1.
\tag{5}
\]

Every cyclotomic polynomial with index `>1` has constant term `1`, hence

\[
G_{\mathbf n}(0)=1.
\tag{6}
\]

Thus different factorization paths to the same endpoint `N` differ only in a polynomial mask living inside one common length-`N` covering block.

## 2. Zero-sum same-endpoint interference is a single weighted cover

Take finitely many paths `\mathbf n^{(1)},...,\mathbf n^{(s)}` with the same endpoint product `N`, and coefficients `c_1,...,c_s in C` satisfying

\[
\sum_{a=1}^s c_a=0.
\tag{7}
\]

The zero-sum condition is the natural one for a relational defect: it removes the common path-independent baseline and includes ordinary differences and commutators. Define

\[
D:=\sum_{a=1}^s c_a A_{\mathbf n^{(a)}}.
\tag{8}
\]

Equations (3)--(6) give

\[
\boxed{
D=M_QC_N,
\qquad
Q(z):=\sum_{a=1}^s c_aG_{\mathbf n^{(a)}}(z),
\qquad
\deg Q<N,
\qquad
Q(0)=0.
}
\tag{9}
\]

This identity is the decisive reduction. The different refinement histories have interfered, but after scalar combination their entire relational content is one finite mask inside the same endpoint block.

Write

\[
Q(z)=\sum_{j=1}^{N-1}q_jz^j.
\tag{10}
\]

For every `k>=0`,

\[
De_k=z^{Nk}Q(z),
\tag{11}
\]

whose support lies in

\[
B_k=\operatorname{span}\{z^{Nk},\ldots,z^{Nk+N-1}\}.
\tag{12}
\]

The blocks `B_k` are pairwise orthogonal. Therefore

\[
\boxed{
D^*D=\|Q\|_{H^2}^2I.
}
\tag{13}
\]

So either `Q=0` and the proposed path defect vanishes exactly, or

\[
V_Q:=\|Q\|_{H^2}^{-1}D
\tag{14}
\]

is an isometry.

## 3. Every nonzero endpoint defect is pure with universal multiplicity

Assume `Q!=0`, and let

\[
a:=\min\{j:q_j\ne0\}.
\tag{15}
\]

Because `Q(0)=0`, one has `a>=1`. Iteration gives

\[
D^r
=M_{Q_r}C_{N^r},
\qquad
Q_r(z)=\prod_{t=0}^{r-1}Q\!\left(z^{N^t}\right).
\tag{16}
\]

The smallest exponent appearing in `Q_r` is exactly

\[
a(1+N+\cdots+N^{r-1})
=a\frac{N^r-1}{N-1},
\tag{17}
\]

which tends to infinity. Hence every vector in `D^rH^2` has its first

\[
a\frac{N^r-1}{N-1}
\]

Fourier coefficients equal to zero. Therefore

\[
\boxed{
\bigcap_{r\ge0}V_Q^rH^2=\{0\}.
}
\tag{18}
\]

Thus `V_Q` is a pure isometry. Equation (12) shows that its range contains one vector in every `N`-dimensional block, so each block contributes an `(N-1)`-dimensional orthogonal complement. Consequently

\[
\dim\ker V_Q^*=\aleph_0.
\tag{19}
\]

The Wold--von Neumann classification now yields

\[
\boxed{
V_Q\simeq S^{(\aleph_0)},
\qquad
D\simeq\|Q\|_{H^2}S^{(\aleph_0)}.
}
\tag{20}
\]

In particular,

\[
\boxed{
\operatorname{Spec}(D)
=\{\lambda\in\mathbb C:|\lambda|\le\|Q\|_{H^2}\}.
}
\tag{21}
\]

The full abstract operator class of a nonzero finite same-endpoint scalar path defect therefore remembers only one finite coefficient norm. It has no discrete eigenvalue list, no compact resolvent, no determinant divisor capable of locating the Riemann zeros, and no distinguished `1/2` or `s<->1-s` symmetry.

## 4. Pairwise refinement commutators obey the same collapse

For two conductors `m,n>=2`, equations (3)--(4) give

\[
W_mW_n
=M_{\Phi_m(z)\Phi_n(z^m)}C_{mn},
\tag{22}
\]

and

\[
W_nW_m
=M_{\Phi_n(z)\Phi_m(z^n)}C_{mn}.
\tag{23}
\]

Hence

\[
\boxed{
[W_m,W_n]
=M_{\Delta_{m,n}}C_{mn},
}
\tag{24}
\]

where

\[
\Delta_{m,n}(z)
=\Phi_m(z)\Phi_n(z^m)
-\Phi_n(z)\Phi_m(z^n).
\tag{25}
\]

Both terms have constant coefficient `1` and degree at most `mn-1`, so `Delta_{m,n}(0)=0`. Therefore the commutator is either zero or

\[
\boxed{
[W_m,W_n]
\simeq
\|\Delta_{m,n}\|_{H^2}S^{(\aleph_0)}.
}
\tag{26}
\]

This is stronger than saying that the two ordered products have the same abstract class, as in PC-210: even their **coherent difference**, which could in principle have retained path phase information, has only the universal pure-shift class up to one scalar.

For distinct primes `p,q`, PC-210 already gives `W_pW_q=W_qW_p=M_{S_{pq}}C_{pq}`, so the commutator vanishes. Nonzero composite examples do not help spectrally. For instance

\[
G_{(2,4)}=1+z+z^4+z^5,
\qquad
G_{(4,2)}=1+z^2+z^4+z^6,
\]

so

\[
\Delta_{2,4}=z+z^5-z^2-z^6,
\qquad
\|\Delta_{2,4}\|_{H^2}=2,
\tag{27}
\]

and therefore

\[
[W_2,W_4]\simeq2S^{(\aleph_0)}.
\tag{28}
\]

The concrete noncommutativity is real, but its abstract spectrum is still just a disk.

## 5. Direct composite shell versus its prime-refinement path

PC-210 explicitly left open retaining both the direct composite primitive operator and the refinement path that reaches the same endpoint. Let

\[
N=\prod_{j=1}^r p_j
\tag{29}
\]

be the prime factorization with repetitions. Because every prime generator has `Phi_p=S_p`, the prime path telescopes exactly to

\[
A_{\mathrm{prime\ path}}
=W_{p_1}\cdots W_{p_r}
=M_{S_N}C_N,
\qquad
S_N(z)=1+z+\cdots+z^{N-1}.
\tag{30}
\]

The direct primitive operator is

\[
W_N=M_{\Phi_N}C_N.
\tag{31}
\]

Their unnormalized path defect is therefore

\[
\boxed{
A_{\mathrm{prime\ path}}-W_N
=M_{S_N-\Phi_N}C_N.
}
\tag{32}
\]

For prime `N` it vanishes, exactly because every nontrivial `N`-th root is primitive. For composite `N` it is nonzero, but (20) gives

\[
\boxed{
A_{\mathrm{prime\ path}}-W_N
\simeq
\sqrt{N+h_N-2\Phi_N(1)}\;S^{(\aleph_0)},
}
\tag{33}
\]

where

\[
h_N:=\|\Phi_N\|_{H^2}^2.
\tag{34}
\]

Indeed `||S_N||_2^2=N`, while

\[
\langle S_N,\Phi_N\rangle
=\sum_j[z^j]\Phi_N(z)
=\Phi_N(1).
\tag{35}
\]

More generally the complete two-path Gram data before taking the difference are already scalar:

\[
\boxed{
\begin{pmatrix}
W_N^*W_N & W_N^*A_{\mathrm{prime\ path}}\\
A_{\mathrm{prime\ path}}^*W_N & A_{\mathrm{prime\ path}}^*A_{\mathrm{prime\ path}}
\end{pmatrix}
=
\begin{pmatrix}
h_N & \Phi_N(1)\\
\Phi_N(1) & N
\end{pmatrix}\otimes I.
}
\tag{36}
\]

The familiar cyclotomic evaluation is

\[
\Phi_N(1)=
\begin{cases}
p,&N=p^a,\\
1,&N>1\text{ has at least two distinct prime divisors}.
\end{cases}
\tag{37}
\]

Thus the direct/path angle does retain a prime-power selector, but it is exactly the classical `Phi_N(1)` datum already present in elementary cyclotomic theory. The remaining scalar `h_N` is the ordinary coefficient `L^2` energy already isolated by PC-209. Equation (36) therefore does not uncover a new relational zeta carrier; it packages two classical finite polynomial statistics into a `2x2` Gram matrix.

## 6. General path Gram matrices retain only finite mask correlations

The same block calculation gives, for any two same-endpoint paths `a,b`,

\[
\boxed{
A_a^*A_b
=\langle G_a,G_b\rangle_{H^2}I.
}
\tag{38}
\]

Therefore for a finite family of paths the whole operator-valued Gram matrix is

\[
\boxed{
[A_a^*A_b]_{a,b}
=[\langle G_a,G_b\rangle]_{a,b}\otimes I.
}
\tag{39}
\]

All quadratic interference norms are consequently finite coefficient correlations of the endpoint masks. Such correlations can certainly distinguish different path factorizations, but the Hilbert-space operator part contributes no additional spectrum: every scalar path combination is controlled by this finite Gram matrix, and every zero-sum nonzero combination has the universal pure-shift class (20).

This gives a matched nonarithmetic control stronger than a prime/composite example. Replace the cyclotomic path masks by **any** finite collection of polynomial masks `P_a` of degree `<N` with the same constant coefficient. Their zero-sum scalar interference has exactly equations (9), (13), and (18)--(21). The pure-shift collapse is forced by one-block support plus baseline cancellation, not by roots of unity.

## 7. Prior-art and novelty audit

The operator-theoretic ingredients are classical. Weighted composition operators `M_gC_phi` on Hardy space and their isometric/Wold behavior are standard, and PC-209 already records that prior-art boundary for the single-mask operator. PC-210 records the standard Haar-refinement and integer-dilation neighborhood for prime-generated paths. A directed literature check also finds an established theory of differences and finite linear combinations of weighted composition operators; the current exact reduction is much simpler than that general setting because all paths share the **same composition symbol** `z^N`, so linearity factors the whole combination immediately as `M_QC_N`.

No novelty is claimed for weighted composition operators, Wold decomposition, finite filter-mask Gram matrices, Haar refinement, the cyclotomic factorization of `z^N-1`, or the value `Phi_N(1)`. The project-local contribution is the boundary theorem tying these classical facts to a specific Prime-Circle escape: finite coherent forward-path interference at one endpoint cannot manufacture a new spectral species from the distinction between direct primitive birth and refinement history.

The exact result is self-contained and does not rely on an absence-of-literature argument. Equations (9), (13), and (17)--(20) prove the collapse, while (36) identifies the most natural direct/path cross-Gram datum explicitly. The literature audit therefore classifies the surrounding operator mechanism as mature prior art rather than supporting a novelty claim.

## 8. Research consequence and remaining boundary

The natural chain

\[
\text{several finite cyclotomic refinement paths to one endpoint}
\longrightarrow
\text{scalar path difference/commutator/interference}
\longrightarrow
\text{new spectrum or RH divisor}
\]

is closed. If the interference is nonzero, its abstract operator is only a scalar multiple of `S^(aleph_0)`; if it vanishes, there is no carrier at all. The direct primitive shell versus its complete prime-refinement path is the cleanest example: the path discrepancy can detect compositeness at finite level, but only through the already-classical cyclotomic mask and `Phi_N(1)` data, while its operator spectrum is universal.

A surviving relational refinement mechanism must therefore retain more than a scalar coherent sum of forward paths with fixed endpoint. Possibilities outside this theorem include a genuinely path-labelled matrix/tensor before scalar contraction, native composite masks interleaved with adjoint transfer so that no common endpoint composition symbol factors out, simultaneous growth of conductor and relational state with a source-forced normalization, nonlinear or off-circle harmonic couplings, or the global uniformization/accessory branch. Any such proposal must still pass the Prime-Circle matched-control and prior-art gates rather than count generic noncommutativity as progress.