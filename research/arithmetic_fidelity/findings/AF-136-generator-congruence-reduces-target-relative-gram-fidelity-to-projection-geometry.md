# AF-136 — Generator congruence reduces target-relative Gram fidelity to projection geometry

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `GAUGE-CLASSIFICATION`, `TARGET-RELATIVE`, `PRIOR-ART-BOUNDARY`, `NO-NOVELTY-CLAIM`

## Claim

AF-135 identifies the exact target-sensitive datum missing from an unmarked generator Gram matrix, but it also leaves a coordinate boundary: Gram eigenvalues, condition numbers, and spectral cutoffs are invariant under unitary changes of generator coordinates, not under arbitrary invertible reparameterizations. The boundary can be classified exactly.

Let `H` be a complex Hilbert space, let

\[
A:\mathbb C^m\to H
\]

be a finite synthesis map with source span

\[
M=\operatorname{ran}A,
\]

and let

\[
U:\mathbb C^d\to H,
\qquad U^*U=I_d,
\]

be an orthonormal frame for a declared finite-dimensional target subspace `K=ran U`. Define

\[
G=A^*A,
\qquad
C=A^*U,
\qquad
Q=C^*G^\dagger C.
\tag{1}
\]

Then:

1. **The target projection Gram is coordinate-free.** One has
   \[
   \boxed{
   Q=U^*P_MU,
   }
   \tag{2}
   \]
   where `P_M` is the orthogonal projection onto `M`. Consequently, under any invertible generator reparameterization
   \[
   A\mapsto AR,
   \qquad R\in GL_m(\mathbb C),
   \tag{3}
   \]
   the target-relative Gram data transform as
   \[
   G\mapsto R^*GR,
   \qquad
   C\mapsto R^*C,
   \tag{4}
   \]
   while `M` and `Q` remain unchanged.

2. **For fixed coefficient dimension, `(rank G,Q)` completely classifies target-relative Gram data modulo arbitrary generator congruence.** More precisely, let `(G_1,C_1)` and `(G_2,C_2)` be two pairs with `G_i` positive semidefinite in `M_m(C)` and every column of `C_i` in `ran G_i`. Then there exists `R in GL_m(C)` such that
   \[
   G_2=R^*G_1R,
   \qquad
   C_2=R^*C_1
   \tag{5}
   \]
   iff
   \[
   \boxed{
   \operatorname{rank}G_1=\operatorname{rank}G_2,
   \qquad
   C_1^*G_1^\dagger C_1=C_2^*G_2^\dagger C_2.
   }
   \tag{6}
   \]
   Thus all positive Gram eigenvalue magnitudes disappear under the full generator gauge. What survives is source-span rank together with target projection geometry.

3. **For one fixed target, the collapse is almost total.** If `d=1`, write `U1=k/||k||` for nonzero target `k`, or equivalently use AF-135's unnormalized data
   \[
   b=A^*k,
   \qquad
   \kappa=\|k\|^2,
   \qquad
   q=b^*G^\dagger b.
   \tag{7}
   \]
   For fixed `m`, the pair `(G,b)` is classified under generator congruence by
   \[
   \boxed{(\operatorname{rank}G,q)}.
   \tag{8}
   \]
   Moreover
   \[
   q=\|P_Mk\|^2,
   \qquad
   \operatorname{dist}(k,M)^2=\kappa-q.
   \tag{9}
   \]
   Hence, without an independently justified coefficient metric, there is no nontrivial GL-invariant source spectral profile left to truncate: the complete target-relative invariant is already the target projection energy itself, together with rank.

4. **For a target subspace, the intrinsic profile is the principal-angle spectrum.** If the target frame is changed by `U -> UV` with `V in U(d)`, then `Q -> V^*QV`. Therefore the coordinate-free target-subspace invariant is the spectrum of `Q`. If
   \[
   1\ge \lambda_1(Q)\ge\cdots\ge\lambda_d(Q)\ge0,
   \tag{10}
   \]
   then
   \[
   \boxed{
   \lambda_j(Q)=\cos^2\theta_j(K,M),
   }
   \tag{11}
   \]
   with the usual principal angles ordered so that their cosines are nonincreasing.

5. **Principal angles give the exact best rank-`s` target-fidelity compression inside the source span.** For `0 <= s < d`, define
   \[
   \Delta_s(M,K)
   :=
   \inf_{\substack{S\subseteq M\\ \dim S\le s}}
   \sup_{\substack{k\in K\\ \|k\|=1}}
   \left[
   \operatorname{dist}(k,S)^2
   -
   \operatorname{dist}(k,M)^2
   \right].
   \tag{12}
   \]
   With the convention `lambda_j(Q)=0` beyond `rank Q`,
   \[
   \boxed{
   \Delta_s(M,K)=\lambda_{s+1}(Q)=\cos^2\theta_{s+1}(K,M).
   }
   \tag{13}
   \]
   In particular, the smallest retained dimension giving zero additional target-distance defect for every target in `K` is
   \[
   \boxed{
   \operatorname{rank}(P_M|_K)=\operatorname{rank}Q.
   }
   \tag{14}
   \]

6. **A source-Gram eigenvalue cutoff can be arbitrarily worse than the intrinsic target-relative optimum.** The ordering of the nonzero eigenvalues of `G` can be changed by rescaling generator coordinates while `M`, `K`, `Q`, and every target distance remain fixed. There are two-dimensional examples in which a rank-one largest-eigenvalue Gram cutoff has worst-case squared target defect `1`, while the optimal rank-one source subspace has defect `alpha^2 -> 0`.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{full generator }GL\text{-gauge destroys source Gram spectral scale;}\\
\text{target-relative information descends exactly to projection geometry;}\\
\text{a spectral cutoff is intrinsic only after its coefficient metric or restricted gauge is independently justified.}
\end{array}}
\tag{15}
\]

This sharpens AF-135's coordinate warning. A whitened target tail is an exact fidelity diagnostic **inside a declared coefficient Hilbert geometry**; it is not an invariant of the abstract source span. If an arithmetic application has no canonical reason to privilege that generator metric, the coordinate-free replacement is target projection/principal-angle data, which may itself be too close to the desired target observable to count as a useful compression.

## Derivation

### The generalized Gram quotient is exactly target projection geometry

The Moore-Penrose projection identity gives

\[
P_M=AG^\dagger A^*.
\tag{16}
\]

Therefore

\[
C^*G^\dagger C
=U^*AG^\dagger A^*U
=U^*P_MU,
\tag{17}
\]

which proves `(2)`.

Under `A -> AR`, the source span is unchanged because `R` is invertible. Equation `(17)` therefore proves invariance of `Q` without requiring any false covariance rule for the Moore-Penrose inverse under nonunitary congruence.

There is also a purely algebraic way to see the same invariance. Since `C` lies in `ran G`, choose any matrix `X` satisfying

\[
GX=C.
\tag{18}
\]

Then

\[
C^*X=C^*G^\dagger C=Q.
\tag{19}
\]

The value is independent of the chosen solution because differences of solutions lie in `ker G`, orthogonal to `ran G` and hence to every column of `C`. After `(4)`,

\[
X'=R^{-1}X
\]

solves

\[
(R^*GR)X'=R^*C,
\]

and

\[
(R^*C)^*X'=C^*RR^{-1}X=C^*X.
\tag{20}
\]

Thus `Q` is the exact quadratic form induced on the target marks after quotienting out the generator coordinate gauge.

### Sylvester reduction plus Gram uniqueness gives a complete orbit classification

For a positive-semidefinite Hermitian matrix of rank `r`, Sylvester's law of inertia gives an invertible congruence reducing it to

\[
J_r=
\begin{pmatrix}
I_r&0\\
0&0
\end{pmatrix}.
\tag{21}
\]

Choose `S_i in GL_m(C)` such that

\[
S_i^*G_iS_i=J_r,
\tag{22}
\]

and set

\[
D_i=S_i^*C_i.
\tag{23}
\]

Because `C_i in ran G_i` columnwise, `D_i in ran J_r`, so

\[
D_i=
\begin{pmatrix}
Z_i\\
0
\end{pmatrix}
\tag{24}
\]

for some `Z_i in C^{r x d}`. In this normalized gauge,

\[
Q_i=D_i^*J_rD_i=Z_i^*Z_i.
\tag{25}
\]

If `Q_1=Q_2`, the two column families `Z_1` and `Z_2` have the same Gram matrix. Hence there is a unitary `W in U(r)` taking one realization to the other:

\[
Z_2=WZ_1.
\tag{26}
\]

The block matrix

\[
R_0=
\begin{pmatrix}
W^*&0\\
0&I_{m-r}
\end{pmatrix}
\tag{27}
\]

stabilizes `J_r` and satisfies

\[
R_0^*D_1=D_2.
\tag{28}
\]

Composing the two Sylvester normalizations with this stabilizer gives an invertible `R` satisfying `(5)`. The converse follows immediately from rank preservation and `(20)`. This proves `(6)`.

For `d=1`, `Q` is the scalar normalized projection energy. Returning to an unnormalized target only multiplies it by `kappa`, yielding `(7)`--`(9)`. Thus the apparent richness of the Gram eigenvalue list is entirely a choice of coefficient metric once arbitrary invertible generator coordinates are declared equivalent.

### Principal angles are the target-frame-free quotient

Let

\[
B=P_MU:\mathbb C^d\to M.
\tag{29}
\]

Then

\[
B^*B
=U^*P_MU
=Q.
\tag{30}
\]

Hence the singular values of `B` are `sqrt(lambda_j(Q))`. Classical principal-angle theory identifies those singular values with the cosines of the principal angles between `K` and `M`, proving `(11)`.

This also separates two gauges cleanly. Generator `GL_m`-gauge removes arbitrary coordinates and scales on a fixed source span. Target `U(d)`-gauge removes the arbitrary orthonormal basis inside a fixed target subspace. After both quotients, only the relative subspace geometry remains.

### The best retained source dimension is an Eckart-Young problem

For any `S subseteq M` and `k in K`, orthogonal projection inside the nested subspaces `S subseteq M` gives

\[
\operatorname{dist}(k,S)^2
-
\operatorname{dist}(k,M)^2
=
\|(P_M-P_S)k\|^2.
\tag{31}
\]

Writing `k=Ux`, `||x||=1`, the right-hand side is

\[
\|(I-P_S)Bx\|^2.
\tag{32}
\]

Therefore

\[
\Delta_s(M,K)
=
\inf_{\dim S\le s}
\|(I-P_S)B\|_{\mathrm{op}}^2.
\tag{33}
\]

For each `S`, `P_SB` has rank at most `s`, so the Eckart-Young-Mirsky lower bound gives

\[
\|(I-P_S)B\|_{\mathrm{op}}
\ge \sigma_{s+1}(B).
\tag{34}
\]

Equality is attained by taking `S` to contain the first `s` left singular vectors of `B`. Thus

\[
\Delta_s(M,K)=\sigma_{s+1}(B)^2=\lambda_{s+1}(Q),
\]

proving `(13)`. Equation `(14)` follows because the tail vanishes exactly after all nonzero singular directions of `P_M|_K` have been retained.

The theorem is target-relative: directions in `M` orthogonal to the projected target family cost nothing for `(12)`. That is the desired feature, not a defect. A different downstream target family can induce a different optimal retained subspace even when the source span is unchanged.

## Exact control: source spectrum can rank the wrong direction

Let

\[
H=\mathbb R^3,
\qquad
M=\operatorname{span}\{e_1,e_2\},
\]

and for `0<alpha<1` let

\[
K_\alpha
=
\operatorname{span}\left\{
 k_1=e_2,
 \ k_2=\alpha e_1+\sqrt{1-\alpha^2}\,e_3
\right\}.
\tag{35}
\]

The displayed target vectors are orthonormal. Their projections onto `M` are

\[
P_Mk_1=e_2,
\qquad
P_Mk_2=\alpha e_1,
\tag{36}
\]

so

\[
Q=\operatorname{diag}(1,\alpha^2).
\tag{37}
\]

The intrinsic best one-dimensional retained source subspace is therefore

\[
S_*=\operatorname{span}\{e_2\},
\]

with exact worst-case squared defect

\[
\Delta_1(M,K_\alpha)=\alpha^2.
\tag{38}
\]

Now choose generator coordinates

\[
A_\varepsilon(a_1,a_2)
=a_1e_1+\sqrt\varepsilon\,a_2e_2,
\qquad 0<\varepsilon<1.
\tag{39}
\]

Then

\[
G_\varepsilon
=\operatorname{diag}(1,\varepsilon).
\tag{40}
\]

A rank-one cutoff that keeps the largest Gram eigenvalue retains the physical source direction `e_1`, not `e_2`. For target `k_1=e_2`,

\[
\operatorname{dist}(k_1,\operatorname{span}\{e_1\})^2
-
\operatorname{dist}(k_1,M)^2
=1.
\tag{41}
\]

Thus the source-spectrum cutoff has worst-case squared defect `1`, whereas the coordinate-free optimum is `alpha^2`. Letting `alpha -> 0` makes the optimum arbitrarily small while the Gram-eigenvalue rule remains maximally wrong.

Nothing about `M` or `K_alpha` changed. The failure comes only from assigning an arbitrary coefficient scale to the second generator. Conversely, rescaling the first generator can reverse the Gram eigenvalue ordering. This is the concrete falsification control for any claim that a source Gram spectrum is intrinsically ordered without a canonical coefficient Hilbert geometry.

## Consequences for Arithmetic Fidelity

AF-135 showed that, once a coefficient metric is fixed, a spectral Gram cutoff loses exactly the discarded whitened target mass. AF-136 identifies the prior question that must be answered before that criterion can be transported into an arithmetic application:

\[
\boxed{
\text{what mathematical structure makes the coefficient metric part of the object rather than a coordinate choice?}
}
\tag{42}
\]

If only the source span and target family are intrinsic, arbitrary generator `GL`-gauge is admissible and the full source Gram spectral profile has no invariant meaning. The complete target-relative quotient is `Q=U^*P_MU`; after forgetting the target basis, its spectrum is simply principal-angle data. A purported lightweight spectral certificate that depends on more than this must therefore justify the additional generator metric independently.

This gives a sharper minimal-lift audit for Gram-based compression:

- **source span only:** generator eigenvalue scale is gauge;
- **source span plus target family:** `Q` / principal-angle geometry is intrinsic but explicitly target-relative;
- **declared coefficient Hilbert metric:** AF-135's whitened spectral tail becomes meaningful;
- **arithmetic application:** one still must prove that the declared coefficient metric or target-relative profile is canonical and materially smaller than retaining the target information it is meant to predict.

The result does not settle the arithmetic tail condition left after AF-135. It instead prevents a false shortcut: choosing generator weights or a numerically convenient basis cannot manufacture an intrinsic small-eigenvalue tail. A valid arithmetic use must either derive a canonical coefficient geometry from the construction or formulate its compression directly in the projection/principal-angle quotient.

## Prior art and novelty assessment

No novelty claim is made for Hermitian congruence, Gram realization uniqueness, principal angles, or best low-rank approximation.

- Roger A. Horn and Charles R. Johnson, ***Matrix Analysis***, 2nd ed., Cambridge University Press (2012; digital edition 2013), DOI `10.1017/CBO9781139020411`. Role: standard matrix-analysis source for Hermitian congruence/inertia, Gram matrices, unitary equivalence of Gram realizations, singular values, and orthogonal projections.
- Susana Furtado and Charles R. Johnson, **“Congruence and A^{-1}A^*,”** *Portugaliae Mathematica* 64(2), 237–251 (2007), DOI `10.4171/PM/1785`. Role: modern congruence/canonical-form context and extensions of Sylvester-type congruence classification. The positive-semidefinite fixed-rank reduction used here is the classical easy Hermitian case.
- Ake Bjorck and Gene H. Golub, **“Numerical Methods for Computing Angles Between Linear Subspaces,”** *Mathematics of Computation* 27(123), 579–594 (1973), DOI `10.1090/S0025-5718-1973-0348991-3`. Role: classical principal-angle/canonical-correlation framework; the cosines of principal angles are singular values of the cross-projection between orthonormal subspace bases.
- Carl Eckart and Gale Young, **“The Approximation of One Matrix by Another of Lower Rank,”** *Psychometrika* 1(3), 211–218 (1936), DOI `10.1007/BF02288367`; Leon Mirsky, **“Symmetric Gauge Functions and Unitarily Invariant Norms,”** *Quarterly Journal of Mathematics* 11(1), 50–59 (1960), DOI `10.1093/qmath/11.1.50`. Role: classical best low-rank approximation and its unitarily invariant norm extension, giving `(33)`--`(34)`.

The exact orbit statement `(6)` is an elementary combination of Sylvester reduction with uniqueness of Gram realizations. The principal-angle optimization `(13)` is classical SVD geometry. The Arithmetic Fidelity value is the **gauge audit** they provide for AF-135: once arbitrary generator reparameterization is admitted, target-relative Gram compression has no intrinsic source spectral scale beyond projection geometry. Any future novelty or RH relevance must come from proving that an arithmetic construction supplies a smaller canonical gauge, a natural coefficient metric, or a target-relative profile with a nontrivial arithmetic consequence.

## Decisive audit for future applications

For any proposed Gram/spectral compression of an arithmetic generator family, first declare the admissible generator gauge. If it contains arbitrary invertible reparameterizations, reduce the proposal to `(rank G,Q)` and check whether the alleged spectral information survives. If only unitary or norm-preserving changes are admissible, prove why the coefficient Hilbert metric is intrinsic to the arithmetic construction rather than chosen for convenience. Then compare the proposed retained rank/profile against `(13)` and test whether it improves on, or merely repackages, the target projection data.
