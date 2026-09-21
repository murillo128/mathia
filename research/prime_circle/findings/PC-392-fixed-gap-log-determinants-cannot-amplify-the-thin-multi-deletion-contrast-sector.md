# PC-392 — fixed-gap log-determinants cannot amplify the thin multi-deletion contrast sector

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the fixed-positive-spectral-gap determinant/log-determinant escape left open by PC-391.

PC-391 showed that, after subtracting the independent one-vertex star responses from a simultaneous Buchstab/Kron deletion, the genuinely connected correction is positive semidefinite and has rank at most `k-1`, where `k` is the number of deleted boundary points. On every fixed polynomial primorial window its rank fraction is `O(log p/p)`, which rules out a distinct limiting bulk empirical spectrum but deliberately left determinant and log-determinant observables open: a low-rank perturbation can in principle have a large determinant effect.

For the positive regularized inverse-power chord Laplacians of PC-390/PC-391, that escape can be narrowed sharply. After adding any spectral regularization `lambda_p>0`, the determinant ratio is exactly a determinant on the deleted-vertex contrast space, and its normalized logarithm obeys

\[
0\le
\frac1{|S|}
\log\frac{\det(L_{\rm red}+\lambda_p I)}
{\det(L_{\rm ind}+\lambda_p I)}
\le
O\!\left(\frac{\log p}{p\,\lambda_p}\right).
\tag{1}
\]

Consequently every fixed `lambda>0`, and more generally every `lambda_p >> (log p)/p`, gives a vanishing normalized log-determinant correction. Thus the thin contrast sector cannot be promoted into a new extensive free-energy/log-determinant law merely by taking a determinant at fixed positive spectral gap. Any surviving determinant route must enter the singular regime `lambda_p=O((log p)/p)` or smaller, use the unregularized pseudodeterminant, retain an unnormalized exceptional contribution, or exploit cross-level/nonlinear structure not covered here.

## 1. Exact determinant reduction to the deleted contrast space

Use the notation of PC-391. Let `S` be the surviving boundary, `m:=|S|`, and let `T={t_1,...,t_k}` be the vertices deleted at one sieve/refinement step. With boundary-to-deleted conductance matrix `B`, diagonal incidence sums

\[
D=\operatorname{diag}(d_1,\ldots,d_k),
\qquad
d_i=\sum_{a\in S}b_{ai},
\tag{2}
\]

and internal deleted-vertex Laplacian `K`, PC-391 proved

\[
\Delta_T
:=L_{\rm red}-L_{\rm ind}
=
B\left[D^{-1}-(D+K)^{-1}\right]B^\top
\succeq0.
\tag{3}
\]

Set

\[
A:=D^{-1/2}KD^{-1/2},
\qquad
C:=A(I+A)^{-1},
\qquad
U:=BD^{-1/2}.
\tag{4}
\]

Then

\[
\boxed{\Delta_T=UCU^\top.}
\tag{5}
\]

Moreover `C` has the same kernel and rank as `A`, hence as `K`. In particular, for the positive complete chord kernel on `T`,

\[
\operatorname{rank}C=k-1,
\qquad
C D^{1/2}\mathbf1=0.
\tag{6}
\]

Thus `C` contains only the deleted-vertex contrast modes; the normalized common deleted mode is absent exactly as in PC-391.

For `lambda>0`, define

\[
G_\lambda:=L_{\rm ind}+\lambda I_m.
\tag{7}
\]

This is positive definite even though `L_ind` itself is a Laplacian. Applying the standard matrix determinant lemma / Weinstein--Aronszajn identity to (5) gives the exact reduction

\[
\boxed{
\frac{\det(L_{\rm red}+\lambda I_m)}
{\det(L_{\rm ind}+\lambda I_m)}
=
\det\!\left(
I_k+
C^{1/2}U^\top G_\lambda^{-1}U C^{1/2}
\right).
}
\tag{8}
\]

The nontrivial determinant therefore lives on a space of dimension at most `rank K`, and for the complete deleted graph at most `k-1`. The full `m x m` determinant does not create additional independent spectral directions beyond the contrast sector already isolated in PC-391.

For the first nontrivial case `k=2`, PC-391 gives

\[
\Delta_{\{u,v\}}
=
\gamma vv^\top,
\qquad
\gamma=\frac{cXY}{XY+c(X+Y)},
\qquad
v=\frac{x}{X}-\frac{y}{Y},
\tag{9}
\]

where `x,y` are the two survivor-incidence profiles, `X=1^\top x`, `Y=1^\top y`, and `c` is their internal conductance. Equation (8) then collapses further to

\[
\boxed{
\frac{\det(L_{\rm red}+\lambda I)}
{\det(L_{\rm ind}+\lambda I)}
=
1+\gamma\,v^\top G_\lambda^{-1}v.
}
\tag{10}
\]

So even the determinant amplification of the first multi-deletion interaction is exactly one Green-energy scalar of the normalized incident-profile contrast.

## 2. A trace bound controls the full nonlinear log-determinant

The rank statement alone is not enough: a vanishing rank fraction can still carry exponentially large eigenvalues. Here positivity and the bounded prime-circle chord weights give a stronger estimate.

Because `K\succeq0` and `D\succ0`,

\[
0\preceq
D^{-1}-(D+K)^{-1}
\preceq D^{-1}.
\tag{11}
\]

Hence

\[
0\preceq\Delta_T\preceq BD^{-1}B^\top,
\tag{12}
\]

and

\[
\begin{aligned}
\operatorname{tr}\Delta_T
&\le
\operatorname{tr}(BD^{-1}B^\top)\\
&=
\sum_{i=1}^k\frac{\|b_i\|_2^2}{d_i}\\
&\le
\sum_{i=1}^k\|b_i\|_\infty.
\end{aligned}
\tag{13}
\]

The last inequality uses `||b_i||_2^2 <= ||b_i||_infty ||b_i||_1` and `||b_i||_1=d_i`.

For the normalized regularized inverse-power chord kernel of PC-390,

\[
\kappa_N(d)
=
N^{-2\alpha}
\left[
2\left(
\cosh\frac{\tau}{N}
-\cos\frac{2\pi d}{N}
\right)
\right]^{-\alpha},
\qquad
\alpha>0,\quad\tau\ge0,
\tag{14}
\]

all exponent coordinates in a polynomial window satisfy `|d|<<N`. For sufficiently large primorial conductor `N`, the kernel is decreasing for `1<=|d|<=H` and

\[
\kappa_N(1)
=
(\tau^2+4\pi^2)^{-\alpha}(1+o(1)).
\tag{15}
\]

Thus there is a constant `C_{alpha,tau}` independent of `p`, `H`, `k`, and the particular deleted layer such that

\[
\boxed{\operatorname{tr}\Delta_T\le C_{\alpha,\tau}k.}
\tag{16}
\]

Now set

\[
X_\lambda
=
G_\lambda^{-1/2}\Delta_TG_\lambda^{-1/2}
\succeq0.
\tag{17}
\]

Since `G_lambda\succeq\lambda I`,

\[
\begin{aligned}
0
&\le
\log\frac{\det(G_\lambda+\Delta_T)}{\det G_\lambda}\\
&=
\operatorname{tr}\log(I+X_\lambda)\\
&\le
\operatorname{tr}X_\lambda\\
&\le
\lambda^{-1}\operatorname{tr}\Delta_T\\
&\le
\frac{C_{\alpha,\tau}}{\lambda}\,k.
\end{aligned}
\tag{18}
\]

The only nonlinear input is the elementary scalar inequality `log(1+x)<=x` on the nonnegative eigenvalues of `X_lambda`.

## 3. Primorial deletion density forces the normalized log-determinant to vanish

For the successive primorial sieve step of PC-391,

\[
T=q\,R_p(H/q),
\qquad
k=|T|\le H/q,
\tag{19}
\]

while the surviving set `S=R_q(H)` contains the anchor and every prime in `(q,H]`, so

\[
m=|S|\ge\pi(H)-\pi(q)+1.
\tag{20}
\]

On every fixed polynomial window

\[
H=p^u,\qquad u>1,
\tag{21}
\]

the prime number theorem and `q\sim p` give

\[
\frac{k}{m}
=
O\!\left(\frac{\log p}{p}\right).
\tag{22}
\]

Combining (18) and (22), for any positive sequence `lambda_p`,

\[
\boxed{
0\le
\frac1m
\log\frac{\det(L_{\rm red}+\lambda_p I)}
{\det(L_{\rm ind}+\lambda_p I)}
\le
O_{\alpha,\tau}\!\left(
\frac{\log p}{p\,\lambda_p}
\right).
}
\tag{23}
\]

Therefore

\[
\boxed{
\lambda_p\frac{p}{\log p}\longrightarrow\infty
\quad\Longrightarrow\quad
\frac1m
\log\frac{\det(L_{\rm red}+\lambda_p I)}
{\det(L_{\rm ind}+\lambda_p I)}
\longrightarrow0.
}
\tag{24}
\]

In particular this holds for every fixed `lambda>0`.

Equation (24) is stronger than the rank-fraction bulk statement of PC-391 for this observable. It says that even after the determinant multiplies all spectral shifts together, the total contrast contribution per surviving degree of freedom still vanishes throughout every spectral regime bounded below by a scale asymptotically larger than `(log p)/p`.

## 4. What remains open at the singular edge

The conclusion is deliberately normalized and spectrally regularized. Equation (23) does **not** imply that the unnormalized determinant ratio tends to one. Indeed its logarithm can be as large as `O(k/lambda_p)`, and `k` itself can diverge.

Nor does the argument control

\[
\lambda_p\lesssim\frac{\log p}{p},
\tag{25}
\]

because the inverse `G_{\lambda_p}^{-1}` can then amplify the contrast sector strongly enough that the universal estimate no longer forces a vanishing density. The endpoint `lambda=0` is especially different: both Laplacians have the constant zero mode and the relevant object is a pseudodeterminant or a determinant on the mean-zero subspace, whose behavior depends on the small positive spectrum of `L_ind`.

Thus PC-391's broad “determinant/log-determinant” escape is now split into two regimes. **Fixed-gap and moderately closing-gap normalized log-determinants are ruled out as a new extensive carrier.** The genuinely open part is singular: pseudodeterminants, spectral parameters closing at least on the `(log p)/p` scale, exceptional/unscaled determinant contributions, or cross-level evolution of the thin contrast subspace.

Nothing in (8)--(24) supplies a zeta zero, a functional-equation symmetry, a critical-line selector, or a Hilbert--Pólya operator.

## 5. Prior-art / novelty audit

The abstract ingredients are classical. Kron reduction is Schur complementation for graph Laplacians; Dörfler and Bullo give the standard network-theoretic framework already anchored in `research/prime_circle/SOURCES.md`. The determinant reduction (8) is the standard matrix determinant lemma / Weinstein--Aronszajn identity, and the log-determinant estimate uses only positivity plus `log(1+x)<=x`.

No novelty is claimed for those linear-algebra identities or for the general fact that finite-rank perturbations admit low-dimensional determinant formulas. The prime-circle-specific delta is the combination of three exact inputs already forced by this line: the deleted-vertex contrast factorization from PC-391, the uniform boundedness of the normalized chord conductances from PC-390, and the exact Buchstab/primorial deletion-density estimate. Together they give the explicit scale

\[
\frac1m\Delta\log\det
=
O\!\left(\frac{\log p}{p\,\lambda_p}\right)
\tag{26}
\]

and identify `(log p)/p` as the first spectral scale at which this universal obstruction ceases to decide the question. This is a boundary classification, not a new determinant theorem and not an RH criterion.

## 6. Audit and falsification checks

The exact determinant formula can be checked on any finite positive weighted Laplacian. Construct `B,D,K`, form `L_ind` and `L_red`, choose `lambda>0`, and verify both (3) and the reduced determinant identity (8). For `k=2`, the ratio must agree with the rank-one formula (10).

The trace estimate can be falsified directly by finding a positive instance with

\[
\operatorname{tr}\Delta_T>
\sum_i\|b_i\|_\infty,
\tag{27}
\]

which would contradict (11)--(13). For the prime-circle kernel, a failure of the asymptotic conclusion would require either the normalized conductance `kappa_N(1)` to become unbounded on the polynomial primorial window or the deletion ratio `k/m` not to satisfy PC-391's `O(log p/p)` bound.

The positivity assumption is essential. Signed or indefinite kernels need not satisfy the Löwner inequalities in (11), so no analogous trace/log-determinant bound is claimed for them. The result also does not cover state spaces whose update is not the graph-Laplacian Schur complement of PC-391.

## Consequence for the research line

One of PC-391's principal exceptional-observable exits is now sharply restricted. A vanishing-rank fraction by itself did not exclude determinant amplification, but the actual positive prime-circle chord geometry also bounds the total trace mass of that contrast correction by `O(k)`. Consequently a fixed positive spectral gap cannot convert the multi-deletion contrast sector into an order-one normalized log-determinant law.

Future work on this branch should therefore concentrate on the singular edge rather than another fixed-gap determinant wrapper: pseudodeterminants/small eigenvalues, spectral parameters at or below the `(log p)/p` scale, unnormalized exceptional modes, or cross-level dynamics of the contrast spaces. Any claimed RH mechanism there must still exhibit arithmetic information beyond the rough-number support and normalized incident profiles classified by PC-388--PC-391.
