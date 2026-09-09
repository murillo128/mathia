# NB-016 — the compressed enrichment frame is a multiplication-table operator

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + QUOTIENT-FRAME-FACTORIZATION + MULTIPLICATION-TABLE-RANK-SPARSITY + NEGATIVE/METHOD-BOUNDARY`. `NB-014` and `NB-015` reduce the live finite-section problem to the semigroup defect visible in the genuinely new quotient section

\[
W_{N,M}:=V_{MN}\ominus V_N,
\qquad
C_{N,M}:=P_{W_{N,M}}F_{N,M}P_{W_{N,M}},
\qquad
F_{N,M}:=\sum_{m=2}^{M}A_mP_NA_m^*.
\]

A natural hope is that, after removing the old section, the dilation family forms a geometrically rich frame on most of `W_(N,M)`. In the basic diagonal chamber `2<=M<=N`, the opposite is true in an exact arithmetic sense. The range of the compressed frame is indexed precisely by integers in `(N,MN]` that occur as products `mj` with `2<=m<=M` and `2<=j<=N`. At maximal depth `M=N`, this is the classical Erdős multiplication table. Kevin Ford's theorem on distinct multiplication-table entries therefore implies that the compressed Nyman enrichment frame has **vanishing relative rank** and asymptotic kernel density one.

More precisely, put

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
r_N=e-P_Ne,
\]

and assume throughout this finding that

\[
2\le M\le N.
\tag{1}
\]

For `N<k<=MN`, define the residualized future generator

\[
h_k:=(I-P_N)g_k.
\tag{2}
\]

Then `\{h_k:N<k<=MN\}` is a basis of `W_(N,M)`. Define the multiplication support

\[
\mathcal P_{N,M}
:=\{k:N<k\le MN,\ k=mj
\text{ for some }2\le m\le M,\ 2\le j\le N\}.
\tag{3}
\]

The compressed frame satisfies the exact range and rank identities

\[
\boxed{
\operatorname{Ran}C_{N,M}
=\operatorname{span}\{h_k:k\in\mathcal P_{N,M}\},
}
\tag{4}
\]

\[
\boxed{
\operatorname{rank}C_{N,M}=|\mathcal P_{N,M}|,
\qquad
\dim\ker C_{N,M}=N(M-1)-|\mathcal P_{N,M}|.
}
\tag{5}
\]

In particular,

\[
\boxed{
\dim\ker C_{N,M}
\ge\sum_{m=2}^{M}\left\lfloor\frac Nm\right\rfloor.
}
\tag{6}
\]

Thus the new quotient frame is singular at every depth in (1); source-independent lower-frame coercivity on all of `W_(N,M)` is impossible.

The maximal diagonal is much more singular. Let

\[
T(N):=|\{ab:1\le a,b\le N\}|
\tag{7}
\]

be the number of distinct entries of the `N x N` multiplication table. Then

\[
\boxed{
\operatorname{rank}C_{N,N}=T(N)-N,
\qquad
\dim\ker C_{N,N}=N^2-T(N).
}
\tag{8}
\]

Ford's solution of the multiplication-table problem gives

\[
T(N)
\asymp
\frac{N^2}
{(\log N)^\delta(\log\log N)^{3/2}},
\qquad
\delta
=1-\frac{1+\log\log2}{\log2}
=0.0860713\ldots .
\tag{9}
\]

Since `dim W_(N,N)=N(N-1)`, equations (8)--(9) imply

\[
\boxed{
\frac{\operatorname{rank}C_{N,N}}
     {\dim W_{N,N}}
\asymp
\frac1{(\log N)^\delta(\log\log N)^{3/2}}
\longrightarrow0,
}
\tag{10}
\]

and hence

\[
\boxed{
\frac{\dim\ker C_{N,N}}
     {\dim W_{N,N}}
\longrightarrow1.
}
\tag{11}
\]

This does **not** upper-bound the compressed frame norm `beta_(N,M)=||C_(N,M)||`; a positive operator can have low rank and a large top eigenvalue. Nor does it show that the actual Nyman residual is poorly aligned with the visible multiplication-table subspace. It establishes a different boundary: any useful visibility theorem must be source-specific not only because generic vectors may fail, but because at the strongest diagonal `M=N` the dilation enrichment sees only a vanishing-dimensional arithmetic slice of the new quotient.

## 1. Residualized future generators form the new-section basis

The generators `g_2,g_3,...` are linearly independent; `NB-014` gives a direct proof from their harmonic-interval values. Therefore

\[
\dim V_K=K-1.
\tag{12}
\]

Since `V_N subset V_(MN)`, orthogonal decomposition gives

\[
\dim W_{N,M}
=(MN-1)-(N-1)=N(M-1).
\tag{13}
\]

The vectors in (2) lie in `W_(N,M)` and span it, because every new generator splits into its old projection plus `h_k`. They are also independent: if

\[
\sum_{k=N+1}^{MN}a_kh_k=0,
\]

then `sum a_k g_k` lies in `V_N`, contradicting linear independence of the full family unless every `a_k=0`. Thus (2) is a basis, not merely a spanning family.

Its Gram matrix

\[
\Sigma_{N,M}:=(\langle h_k,h_\ell\rangle)_{N<k,\ell\le MN}
\tag{14}
\]

is positive definite. Equivalently, if the Gram matrix of `g_2,...,g_(MN)` is partitioned into old and future indices, `Sigma_(N,M)` is the corresponding Schur complement of the old `G_N` block.

## 2. Compression turns dilation into multiplication incidence

Use the exact Bagchi-space dilation identity already reconstructed in `NB-014`,

\[
A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m).
\tag{15}
\]

Let

\[
B_m:=P_{W_{N,M}}A_m|_{V_N}
\qquad(2\le m\le M).
\tag{16}
\]

Assumption (1) is load-bearing here: `m<=N`, so `g_m in V_N` and its quotient projection vanishes. Equation (15) therefore gives, for `2<=j<=N`,

\[
\boxed{
B_mg_j=
\begin{cases}
0,&mj\le N,\\
\sqrt m\,h_{mj},&mj>N.
\end{cases}}
\tag{17}
\]

Consequently

\[
\operatorname{Ran}B_m
=\operatorname{span}\{h_{mj}:2\le j\le N,\ mj>N\}.
\tag{18}
\]

The compressed frame decomposes as

\[
C_{N,M}
=\sum_{m=2}^{M}B_mB_m^*.
\tag{19}
\]

For a finite family of operators, the range of the positive sum `sum B_m B_m^*` is the sum of the ranges of the `B_m`: its kernel is `intersection ker B_m^*`, the orthogonal complement of that sum. Combining this with (18) and the independence of the `h_k` proves (4)--(5).

For one fixed `m`, equation (18) contains exactly

\[
N-\left\lfloor\frac Nm\right\rfloor
\tag{20}
\]

distinct basis vectors. Even before paying overlaps between different `m`, subadditivity of rank gives

\[
\operatorname{rank}C_{N,M}
\le
\sum_{m=2}^{M}
\left(N-\left\lfloor\frac Nm\right\rfloor\right)
=N(M-1)-\sum_{m=2}^{M}\left\lfloor\frac Nm\right\rfloor,
\]

which proves (6). The exact support formula (3) is stronger because products with several factorizations contribute only one quotient direction.

## 3. The actual visibility statistic has an exact multiplication-support Gram factorization

The rank statement is not only an abstract property of arbitrary quotient vectors. It identifies exactly which future target pairings can enter the visible-defect statistic of the actual residual.

Index `G_N` by `j=2,...,N`, and define the future residual-pairing vector

\[
q_k:=\langle r_N,g_k\rangle
=\langle r_N,h_k\rangle,
\qquad N<k\le MN.
\tag{21}
\]

These are target-aware finite-section data. If `b` denotes the target-pairing vector for the full generator family, then in block notation

\[
q=b_{\rm new}-G_{{\rm new},{\rm old}}
G_N^{-1}b_{\rm old}.
\tag{22}
\]

For `2<=m<=M`, let `R_m` map future-indexed vectors to old generator coordinates by

\[
(R_mq)_j=
\begin{cases}
q_{mj},&mj>N,\\
0,&mj\le N,
\end{cases}
\qquad 2\le j\le N,
\tag{23}
\]

and set

\[
K_{N,M}
:=\sum_{m=2}^{M}mR_m^*G_N^{-1}R_m.
\tag{24}
\]

Because `r_N perpendicular V_N`, (15) yields

\[
\langle r_N,A_mg_j\rangle
=\sqrt m\,(R_mq)_j.
\tag{25}
\]

The family `A_mg_2,...,A_mg_N` has Gram matrix exactly `G_N` because `A_m` is an isometry. Hence the projection formula gives

\[
\|P_{A_mV_N}r_N\|^2
=m(R_mq)^*G_N^{-1}(R_mq).
\tag{26}
\]

On the other hand, `P_Nr_N=0`, so

\[
\|P_N(A_m^*-m^{-1/2}I)r_N\|^2
=\|P_{A_mV_N}r_N\|^2.
\tag{27}
\]

Summing proves the exact target-aware factorization

\[
\boxed{
\mathcal J_{N,M}=q^*K_{N,M}q.
}
\tag{28}
\]

The coordinate kernel of `K_(N,M)` is exactly the complement of the multiplication support (3): positivity of `G_N^-1` implies `Kq=0` exactly when every `R_mq=0`. Thus the same multiplication incidence that controls `rank C` also controls which future residual pairings can contribute to actual visible enrichment.

The Schur matrix (14) completes the finite certificate. Projection of `r_N` onto `W_(N,M)` gives

\[
\boxed{
d_N^2-d_{MN}^2=q^*\Sigma_{N,M}^{-1}q,
}
\tag{29}
\]

while for `w=sum a_k h_k`, equations (24)--(27) give

\[
\langle w,C_{N,M}w\rangle
=a^*\Sigma_{N,M}K_{N,M}\Sigma_{N,M}a.
\tag{30}
\]

Therefore

\[
\boxed{
\beta_{N,M}
=\lambda_{\max}
\left(\Sigma_{N,M}^{1/2}K_{N,M}\Sigma_{N,M}^{1/2}\right).
}
\tag{31}
\]

Equations (28)--(31) are basis-invariant finite Gram statements despite their convenient coordinates. In particular, the `NB-015` transport inequality is the ordinary Rayleigh bound

\[
q^*Kq
\le
\lambda_{\max}(\Sigma^{1/2}K\Sigma^{1/2})
q^*\Sigma^{-1}q.
\tag{32}
\]

This makes the remaining source problem explicit: one must control how the actual target-residual vector `q` sits relative to the multiplication-supported generalized eigenspaces, not merely count those eigenspaces.

## 4. At `M=N`, Ford's multiplication-table theorem makes the quotient frame asymptotically rank-sparse

Set `M=N`. The support (3) becomes

\[
\mathcal P_{N,N}
=\{ab:N<ab\le N^2,\ 2\le a,b\le N\}.
\tag{33}
\]

Every entry of the `N x N` multiplication table that is greater than `N` automatically has both factors at least `2`, while the table contains every integer `1,...,N` through `1*j`. Therefore

\[
|\mathcal P_{N,N}|=T(N)-N,
\tag{34}
\]

which proves (8).

Ford's Corollary 3, specialized to `x=N^2`, gives (9): the number of distinct entries in the multiplication table is of order

\[
N^2/((\log N)^\delta(\log\log N)^{3/2}).
\]

Substitution into (8) proves (10)--(11). This is substantially stronger than the elementary nullity bound (6) on the maximal diagonal. The collapse comes from repeated factorization: many dilation channels land on the same future generator index, while most quotient basis directions are not multiplication-table entries at all.

## 5. Falsification controls and research consequence

Several boundaries are essential.

First, the theorem is restricted to `M<=N`. If `m>N`, the term `g_m` in (15) is itself a future direction and the simple product-support formula (17) changes. `NB-015` allows the broader corridor `sqrt(M) lesssim N`; nothing here claims the same rank formula throughout that larger region.

Second, low rank does not imply a small top eigenvalue. Equations (10)--(11) do **not** improve the generic bound `beta_(N,M)<=M-1` and do not contradict the full-frame saturation in `NB-014`. Full-space overlap, quotient rank, and quotient operator norm are different quantities.

Third, the actual residual is not a random quotient vector. A vanishing relative rank does not by itself upper-bound `mathcal J_(N,M)` or the visibility fraction `rho_(N,M)`. The future pairings in (21) could be arithmetically concentrated on `mathcal P_(N,M)`. Any claim that they are not must be proved from the Nyman source geometry; dimension counting alone is insufficient.

Fourth, the Schur-complement identities (22), (29) and the projection formula are standard finite-dimensional Hilbert-space algebra. Their role here is to expose the arithmetic support of the already accepted enrichment mechanism. The substantive new boundary is (4)--(11): the compressed dilation frame has exact multiplication-table range, and at `M=N` its relative rank tends to zero by a classical theorem on distinct products.

A targeted prior-art check covered Bagchi's dilation-semigroup formulation, Ehm's 2024 Nyman Gram-matrix decompositions, recent multiscale Nyman Gram work, generalized Nyman approximation papers, and searches combining finite-section dilation/projection with Schur complements or the multiplication-table problem. No located Nyman source identified the quotient enrichment range with distinct multiplication-table entries. Search absence is not a novelty proof. Ford's distinct-product theorem is classical and load-bearing only for the asymptotic rank count; it has been added to `SOURCES.md`.

The live `NB-015` frontier is therefore sharper. A successful source estimate for `rho_(N,M)/beta_(N,M)` cannot come from treating `C_(N,M)` as a generically coercive frame on the new section: on the maximal admissible diagonal its kernel occupies asymptotically the entire quotient. The remaining viable route is to prove that the **specific future target-residual pairings** in (21) concentrate enough on the multiplication support, with the correct Schur metric and semigroup-energy normalization, to make the weighted visibility budget diverge. No such concentration theorem, improved Nyman approximation rate, or RH implication is established here.
