# WI-081 — pairwise LCM boundary rank controls finite-window Ramanujan leakage

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens the finite-section escape left by WI-080: even when the common period of the entire signed modulus family is astronomically larger than the source window, interaction between any two distinct Ramanujan modulus blocks is confined to a rank determined only by how far the window length is from the **nearest multiple of their pairwise lcm**.

For distinct positive integers `m,n`, let

\[
U_m^{(N)}=(e(ax/m))_{0\le x<N,\ a\in(\mathbf Z/m\mathbf Z)^\times},
\qquad
B_m^{(N)}=U_m^{(N)}(U_m^{(N)})^*.
\]

Then `B_m^(N)` is exactly the WI-079 Ramanujan block,

\[
(B_m^{(N)})_{x,y}=c_m(x-y).
\]

Put

\[
\ell_{m,n}=\operatorname{lcm}(m,n),
\qquad
r_{m,n}=N\bmod \ell_{m,n},
\]

and define the nearest-period boundary defect

\[
\boxed{
\delta_N(m,n)
:=
\min\{r_{m,n},\ \ell_{m,n}-r_{m,n}\},
}
\]

with `delta_N(m,n)=0` when `r_{m,n}=0`. The cross Gram matrix obeys the exact rank bound

\[
\boxed{
\operatorname{rank}
\bigl((U_m^{(N)})^*U_n^{(N)}\bigr)
\le \delta_N(m,n).
}
\tag{1}
\]

Consequently, if

\[
\mathcal S_m^{(N)}=\operatorname{ran}U_m^{(N)},
\qquad
d_m=\dim\mathcal S_m^{(N)}=\min\{N,\varphi(m)\},
\]

then

\[
\boxed{
\dim(\mathcal S_m^{(N)}\cap(\mathcal S_n^{(N)})^\perp)
\ge d_m-\delta_N(m,n),
}
\tag{2}
\]

and symmetrically with `m,n` exchanged. Thus finite-window truncation can mix at most `delta_N(m,n)` spectral directions of either Ramanujan subspace with the other.

For opposite signs this becomes an inertia statement. For every `alpha,beta>0`,

\[
A=\alpha B_m^{(N)}-\beta B_n^{(N)}
\]

satisfies

\[
\boxed{
 n_+(A)\ge(d_m-\delta_N(m,n))_+,
\qquad
 n_-(A)\ge(d_n-\delta_N(m,n))_+.
}
\tag{3}
\]

The result extends to an arbitrary finite signed scalar family. After aggregating repeated copies of the same modulus, let

\[
A_\omega=\sum_m\omega_m B_m^{(N)},
\qquad
\mathcal P=\{m:\omega_m>0\},
\qquad
\mathcal M=\{m:\omega_m<0\}.
\]

Because primitive fractions with distinct reduced denominators are distinct Fourier nodes,

\[
D_+=\dim\sum_{m\in\mathcal P}\mathcal S_m^{(N)}
=\min\!\left(N,\sum_{m\in\mathcal P}\varphi(m)\right),
\]

and similarly

\[
D_-=\min\!\left(N,\sum_{n\in\mathcal M}\varphi(n)\right).
\]

Define the crude but exact opposite-sign boundary-rank budget

\[
\Delta_N
:=
\sum_{m\in\mathcal P}\sum_{n\in\mathcal M}
\delta_N(m,n),
\qquad
R_N:=\min\{D_+,D_-,\Delta_N\}.
\]

Then

\[
\boxed{
 n_+(A_\omega)\ge D_+-R_N,
\qquad
 n_-(A_\omega)\ge D_--R_N.
}
\tag{4}
\]

Hence a signed scalar mechanism cannot erase a macroscopic part of either sign-side spectral dimension unless the **aggregate opposite-sign pairwise boundary-rank budget is itself macroscopic**. This is a strictly more local obstruction than WI-080's single global-common-period defect and remains informative in examples where that global defect is vacuous.

## 1. Exact pairwise boundary factorization

Fix distinct `m,n` and write `ell=lcm(m,n)`. For primitive residues `a mod m` and `b mod n`, the fractions `a/m` and `b/n` are distinct modulo one: equality would identify two reduced fractions and force `m=n`. Therefore

\[
z_{a,b}:=e(b/n-a/m)
\]

is a nontrivial `ell`-th root of unity, so

\[
\sum_{x=0}^{\ell-1}z_{a,b}^x=0.
\tag{5}
\]

Write `N=q ell+r`, `0<=r<ell`. The `(a,b)` entry of the cross Gram is

\[
\sum_{x=0}^{N-1}z_{a,b}^x
=
\sum_{x=0}^{r-1}z_{a,b}^x,
\tag{6}
\]

because the `q` complete periods vanish by (5). At the matrix level, (6) expresses the whole cross Gram as a sum of `r` rank-one sample outer products, hence

\[
\operatorname{rank}((U_m^{(N)})^*U_n^{(N)})\le r.
\tag{7}
\]

But (5) also gives

\[
\sum_{x=0}^{r-1}z_{a,b}^x
=-\sum_{x=r}^{\ell-1}z_{a,b}^x.
\tag{8}
\]

Thus the same cross Gram is a sum of `ell-r` rank-one terms and

\[
\operatorname{rank}((U_m^{(N)})^*U_n^{(N)})\le \ell-r.
\tag{9}
\]

Combining (7)--(9) proves (1). A translated source interval changes the cross Gram only by diagonal unitary phase factors on the two primitive-frequency sides, so its rank is unchanged. The statement is therefore intrinsic to the window length, not to the choice of origin.

This also quantifies the qualitative fact that long finite Ramanujan dictionaries become approximately orthogonal: here the failure of orthogonality is confined to an explicitly bounded **number of singular directions**, not merely bounded entrywise on average.

## 2. From cross-Gram rank to subspace dimension

The columns of `U_m^(N)` are consecutive samples of distinct primitive `m`-th roots. The usual Vandermonde argument gives

\[
\operatorname{rank}U_m^{(N)}=\min\{N,\varphi(m)\}=d_m.
\tag{10}
\]

The map `(U_n^(N))^*` restricted to `S_m^(N)` has kernel exactly

\[
\mathcal S_m^{(N)}\cap(\mathcal S_n^{(N)})^\perp.
\]

Since `U_m^(N)` surjects onto `S_m^(N)`, the rank of this restricted map is the rank of the cross Gram. Rank-nullity and (1) therefore give (2).

The point is stronger than small pairwise inner products. Even if individual Dirichlet-kernel entries are not tiny, all nonorthogonality between the two finite Ramanujan spaces is carried by at most `delta_N(m,n)` principal-angle directions.

## 3. Two-block inertia survives outside the boundary directions

For `B_m=U_mU_m^*`, the kernel is `(S_m)^perp`, and the quadratic form is strictly positive on every nonzero vector in `S_m`:

\[
\langle x,B_mx\rangle=\|U_m^*x\|_2^2>0
\qquad(x\in\mathcal S_m\setminus\{0\}).
\tag{11}
\]

On the subspace

\[
\mathcal S_m\cap\mathcal S_n^\perp,
\]

the negative block `B_n` vanishes while the positive block `B_m` is strictly positive. Equation (2) therefore provides a positive-definite subspace of dimension at least `d_m-delta_N(m,n)`. The same argument with the signs reversed gives the negative-definite subspace and proves (3).

For example, take `N=1000`, `m=31`, `n=32`. Their pairwise lcm is `992`, so WI-080's embedding into the **next** complete pairwise period would delete `1984-1000=984` coordinates and give no useful inertia information. Here instead

\[
\delta_{1000}(31,32)=\min\{8,984\}=8.
\]

Since `phi(31)=30` and `phi(32)=16`, every operator

\[
\alpha B_{31}^{(1000)}-\beta B_{32}^{(1000)},\qquad \alpha,\beta>0,
\]

has at least `22` positive and `8` negative eigenvalues. The `992` complete samples *below* the window cancel exactly; only the eight-sample remainder can mix the two subspaces.

## 4. Many-modulus signed inertia gate

Let `U_+` concatenate all `U_m`, `m in P`, and `U_-` concatenate all `U_n`, `n in M`. Reduced primitive fractions attached to distinct moduli are distinct, so the concatenated matrices are again ordinary Vandermonde systems with

\[
\operatorname{rank}U_+=D_+,
\qquad
\operatorname{rank}U_-=D_-.
\tag{12}
\]

Their cross Gram is a block matrix whose `(m,n)` block is `U_m^*U_n`. Therefore

\[
\operatorname{rank}(U_+^*U_-)
\le
\sum_{m\in\mathcal P}\sum_{n\in\mathcal M}
\operatorname{rank}(U_m^*U_n)
\le\Delta_N.
\tag{13}
\]

It is also at most `D_+` and `D_-`, giving the bound `R_N` above.

Write `A_omega=A_+-A_-` with both `A_+,A_-` positive semidefinite. The positive form `A_+` is strictly positive on the span `S_+` of its Ramanujan ranges, while `A_-` vanishes on `S_-^perp`. Hence

\[
\dim(\mathcal S_+\cap\mathcal S_-^\perp)
=D_+-\operatorname{rank}(U_+^*U_-)
\]

is a positive-definite subspace for `A_omega`. The symmetric argument supplies a negative-definite subspace. Inserting (13) proves (4).

The sum in `Delta_N` is intentionally crude: it ignores repeated linear dependencies among boundary couplings and ignores the magnitudes of the nonzero weights. Therefore failure of (4) to give a useful lower bound is **not evidence that cancellation occurs**. Conversely, whenever `Delta_N=o(D_+)` or `o(D_-)`, a macroscopic sign-side inertia survives without any analytic estimate of the Ramanujan-sum amplitudes.

## 5. Consequence for the WI-079/WI-080 scalar escape

WI-080 showed that complete common-period Ramanujan blocks are mutually orthogonal projectors, so all useful signed scalar cancellation must be created by finite time-limiting. Its direct interlacing bound becomes vacuous when the lcm of the entire active family is huge compared with the source window.

The present calculation shows that **huge global lcm is not by itself enough to create unconstrained mixing**. The relevant obstruction can be tested pairwise before taking that global lcm. Opposite-sign blocks whose pairwise lcm is close to a divisor/multiple fit of the source length can exchange only a small number of directions. A scalar Yang repair capable of substantially collapsing signature therefore needs a sufficiently large network of opposite-sign pairs with substantial `delta_N(m,n)`, or it must retain richer labelled/two-dimensional structure that is not represented by the scalar blocks at all.

This gives a cheap falsification gate for the surviving scalar route:

\[
\boxed{
\text{compute the source-faithful opposite-sign pairwise }\delta_N(m,n)
\text{ budget before searching for a delicate norm cancellation theorem.}
}
\]

If that budget is submacroscopic compared with the sign-side Ramanujan dimension, the scalar route is dead at the inertia level. If it is macroscopic, the result merely says that time-limiting has enough rank capacity to permit cancellation; it does not prove that the actual weighted operator achieves it.

As in WI-079--WI-080, Mathia has **not** proved that the entire post-local-main Yang covariance reduces exactly to `A_omega`. The result is a structural barrier for that proposed scalar information interface, not a proof of the Yang--Yang fourth-moment theorem and not a no-go for labelled/two-modulus dispersion.

## 6. Prior art and novelty boundary

The ingredients are classical:

- Noboru Ushiroya, **Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums**, *Journal of Integer Sequences* 21 (2018), Article 18.2.6; arXiv:1803.02970. Lemma 1 gives the complete-common-period Ramanujan convolution orthogonality used in WI-080.
- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals**, *IEEE Transactions on Signal Processing* 62:16 (2014), 4145--4157, DOI `10.1109/TSP.2014.2331617`, and **Part II: FIR Representations and Applications**, ibid. 4158--4172, DOI `10.1109/TSP.2014.2331624`. These establish the Ramanujan-subspace language and exact orthogonal decomposition when the relevant periods divide the finite signal length.
- Srikanth V. Tenneti and P. P. Vaidyanathan, **Nested Periodic Matrices and Dictionaries: New Signal Representations for Period Estimation**, *IEEE Transactions on Signal Processing* 63:14 (2015), 3736--3750, DOI `10.1109/TSP.2015.2434318`. The paper explicitly notes that Ramanujan subspaces become approximately mutually orthogonal when the finite data length is sufficiently large; this is the closest located qualitative prior art for non-period-complete windows.
- Finite geometric sums, Vandermonde rank, rank-nullity, and inertia lower bounds from positive/negative definite subspaces are classical linear algebra.

A targeted audit located the qualitative finite-length approximate-orthogonality statement and the exact period-complete projector theory, but no source in the checked Ramanujan-subspace literature stating the exact nearest-pairwise-period rank bound (1), its two-block inertia consequence (3), or the many-modulus boundary-rank budget (4). No priority claim is made. The durable Mathia contribution is the application of those elementary identities to the precise signed Ramanujan operator isolated by WI-079--WI-080 and the resulting source-interface gate.

## 7. Falsification and remaining gates

1. **Distinct primitive frequencies.** Equation (5) requires `m!=n` after duplicate scalar moduli have been aggregated. Primitive fractions with different reduced denominators cannot coincide; if repeated copies are not first aggregated, they belong to the same block and are not covered by the cross-modulus statement.
2. **Nearest-period rank, not norm.** The theorem controls how many singular directions can couple. It does not by itself make the surviving singular values small, and it does not upper-bound the signed operator norm sharply.
3. **Many-family sum can be vacuous.** `Delta_N` is an upper bound obtained by summing block ranks. A dense opposite-sign family can make it exceed `N` even when the true global cross rank is much smaller. Improving that estimate is a separate spectral/combinatorial problem.
4. **Weight magnitude is unused.** The inertia gate depends only on nonzero signs and subspace geometry. A stronger weighted theorem could exploit small coefficients, but cannot invalidate (1)--(4).
5. **Source-faithful scalar reduction remains unproved.** The Yang object is a locked four-prime covariance. If its exact post-local-main residual retains direction labels or does not factor into ordinary scalar Ramanujan blocks, the present theorem is only a test of one proposed reduction.
6. **No new zeta constant.** Nothing here modifies the currently certified simple-critical proportion. The finding narrows the arithmetic route that could provide stronger moment information.