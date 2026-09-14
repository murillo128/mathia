# NB-113 — common-ordinate multi-zero deflation is exactly orthogonal

**Status:** `EXACT-DERIVED + ARBITRARY-FINITE-RANK + COMMON-ORDINATE-CLASSIFICATION + CANONICAL-DEFLATION-IDENTITY + HARDY-TARGET-AUDIT + ACTUAL-ZETA-ZERO-COUNT-BOUND + MULTI-ZERO-FRONTIER-REDUCTION`.

`NB-112` closes the true-multiplicity rescue for a single off-critical zero: the complete multiplicity of one zero lies below the logarithmic `1/8` target-access window of `NB-111`. The surviving branch therefore has to obtain rank from several distinct zeros. Before studying arbitrary multi-center packets, there is a sharp geometric kill test suggested by `NB-097`--`NB-099`: can many distinct right-half-plane zero states lying at one common ordinate create the collective canonical shear that first appears in `NB-098`?

They cannot. Let

\[
F=(\lambda_1,\ldots,\lambda_d),
\qquad
\lambda_k=a_k+i\Gamma,
\qquad
a_k>0,
\tag{1}
\]

be any ordered finite family with pairwise distinct `a_k`. Let

\[
G_F(r,s)
=\frac{2\sqrt{a_ra_s}}
       {\lambda_r+\overline{\lambda_s}}
\tag{2}
\]

be the normalized half-line state Gram, let `T_F` be the exact canonical causal-deflation matrix of `NB-095`/`NB-098`, and put

\[
C_F=T_F^*G_FT_F.
\tag{3}
\]

Then for every size, every ordering, every common ordinate, and every amount of horizontal crowding short of an actual collision,

\[
\boxed{C_F=I_d.}
\tag{4}
\]

Equivalently, the explicit Cauchy Cholesky factor `Q_F` of `NB-098` satisfies

\[
\boxed{Q_FT_F=I_d.}
\tag{5}
\]

Thus exact common-ordinate packets have no canonical shear at all: every transformed singular value equals one. The `d=2` same-ordinate cancellation observed in `NB-097` is not a low-dimensional accident; it persists at arbitrary finite rank.

There is a complementary target statement in the classical Hardy model. Let `D_+(\gamma)` denote the total multiplicity of actual zeta zeros with positive ordinate `\gamma` and `\Re\rho>1/2`. For the finite Blaschke product `B_\gamma` made from those right-half zeros, counted with multiplicity,

\[
\boxed{
\|P_{K_{B_\gamma}}k_1\|^2
=1-|B_\gamma(1)|^2
\le \frac{D_+(\gamma)}{\gamma^2}.
}
\tag{6}
\]

The Bellotti--Wong zero-counting estimate already anchored by `NB-112`, together with the same-ordinate functional-equation symmetry, gives

\[
D_+(\gamma)
\le
E(\gamma)
:=0.10076\log\gamma
 +0.24460\log\log\gamma
 +8.08344
\tag{7}
\]

for sufficiently large `\gamma` in the normalization used there. Hence

\[
\boxed{
\|P_{K_{B_\gamma}}k_1\|^2
\ll \frac{\log\gamma}{\gamma^2}
\longrightarrow0.
}
\tag{8}
\]

Equation `(8)` is a Hardy/model-space statement, not a finite-window Nyman projection theorem. Its role here is to show that exact same-height crowding is benign in both pieces of geometry that can be tested without solving the remaining finite-window source-to-target bridge: it is perfectly conditioned after canonical half-line deflation, and its classical Blaschke obstruction carries vanishing target mass at high ordinate.

## 1. Common vertical translation reduces the problem to positive real nodes

`NB-099` proves exact common-vertical-translation invariance:

\[
G_{F+i\Gamma}=G_F,
\qquad
T_{F+i\Gamma}=T_F,
\qquad
C_{F+i\Gamma}=C_F.
\tag{9}
\]

Indeed the formulas depend only on `a_r`, differences `\lambda_r-\lambda_s`, and reflected sums `\lambda_r+\overline{\lambda_s}`, all unchanged by a common vertical shift. It therefore suffices to set `\Gamma=0` and take pairwise distinct positive real nodes

\[
a_1,\ldots,a_d>0.
\tag{10}
\]

Work in the shifted Hardy half-plane `H^2(Re z>0)` and use the normalized Cauchy kernels

\[
u_k(z):=\frac{\sqrt{2a_k}}{z+a_k}.
\tag{11}
\]

Their Gram matrix is exactly `(2)` at `\Gamma=0`. Define the elementary half-plane Blaschke factors and the ordered rational states

\[
b_a(z):=\frac{z-a}{z+a},
\qquad
\Psi_k(z)
:=u_k(z)\prod_{\ell<k}b_{a_\ell}(z).
\tag{12}
\]

Each `b_a` is inner, so multiplication by any product of the preceding factors is an isometry on `H^2`. Moreover, if `j<k`, remove the common inner factor `\prod_{\ell<j}b_{a_\ell}` from both states. The remaining second state contains the factor `b_{a_j}` and therefore vanishes at `z=a_j`. Since `u_j` is the normalized reproducing kernel at `a_j`,

\[
\langle\Psi_j,\Psi_k\rangle=0,
\qquad
\|\Psi_k\|=1.
\tag{13}
\]

Hence

\[
\boxed{
\{\Psi_1,\ldots,\Psi_d\}
\text{ is orthonormal for every ordered distinct positive node set.}
}
\tag{14}
\]

This is the familiar finite Takenaka--Malmquist mechanism, but no external basis theorem is needed here; `(13)` is the complete finite proof.

## 2. The canonical Nyman deflation matrix is exactly the partial-fraction map to that orthonormal system

The important line-specific step is not the classical orthogonality in `(14)`, but identifying the exact causal-deflation coordinates already used in `NB-095`--`NB-099` with this rational system.

Because `\Psi_k` has simple poles only at `-a_1,\ldots,-a_k`, its partial-fraction expansion in the raw kernels `(11)` is

\[
\Psi_k
=\sum_{r\le k} \tau_{rk}u_r.
\tag{15}
\]

Residues at `-a_k` give

\[
\tau_{kk}
=
\prod_{\ell<k}
\frac{a_k+a_\ell}{a_k-a_\ell},
\tag{16}
\]

while residues at `-a_r`, `r<k`, give

\[
\tau_{rk}
=
-\frac{2\sqrt{a_ra_k}}{a_k-a_r}
\prod_{\substack{\ell<k\\\ell\ne r}}
\frac{a_r+a_\ell}{a_r-a_\ell}.
\tag{17}
\]

Equations `(16)`--`(17)` are exactly the specialization to real nodes of the canonical-deflation coefficients `(9)`--`(10)` in `NB-098`. Therefore

\[
\tau=T_F,
\tag{18}
\]

and the transformed columns are precisely the orthonormal states `\Psi_k`. Taking their Gram matrix proves `(4)` immediately:

\[
T_F^*G_FT_F
=
[\langle\Psi_r,\Psi_s\rangle]_{r,s}
=I_d.
\tag{19}
\]

The same statement can be read directly in the explicit Cauchy factorization `G_F=Q_F^*Q_F` from `NB-098`. Equation `(19)` forces the positive-diagonal triangular factor to be the identity, and with the present real-node normalization one obtains `(5)` exactly. Common vertical translation then returns the result to arbitrary `\Gamma`.

Two consequences are worth separating. First, the identity is **order-independent**: changing the deflation order changes the individual rational functions but again produces a Takenaka--Malmquist orthonormal family, so the transformed Gram remains `I_d`. Second, horizontal crowding by itself is harmless at the geometric level. As two `a_k` approach one another the entries of `T_F` and the raw Cauchy conditioning can individually become large, but their cancellation in `(19)` is exact for every distinct packet.

This also explains exactly why the `NB-098` pathology is transverse. Its three nodes vary simultaneously in real part and ordinate. If all ordinate differences are set to zero, the inverse-`epsilon` collective shear coefficient disappears not merely to leading order but identically at every rank.

## 3. Actual same-ordinate zeta packets also have vanishing classical Hardy target mass

The half-line state identity `(4)` is about conditioning. Target access is a separate question, so it is useful to audit the same geometry directly against the classical Burnol obstruction without identifying the two objects.

For a finite right-half-plane zeta divisor `F`, let `B_F` be its half-plane Blaschke product, with multiplicity. Burnol's model-space projection formula gives

\[
\|P_{K_{B_F}}k_1\|^2
=1-|B_F(1)|^2.
\tag{20}
\]

For a zero

\[
\rho=\beta+i\gamma,
\qquad \frac12<\beta<1,
\tag{21}
\]

the corresponding factor satisfies

\[
|b_\rho(1)|^2
=
\frac{(1-\beta)^2+\gamma^2}
     {\beta^2+\gamma^2},
\tag{22}
\]

so

\[
1-|b_\rho(1)|^2
=
\frac{2\beta-1}{\beta^2+\gamma^2}
\le \frac1{\gamma^2}.
\tag{23}
\]

For numbers `0\le q_j\le1`,

\[
1-\prod_jq_j
\le\sum_j(1-q_j).
\tag{24}
\]

Applying `(24)` to the squared factor magnitudes and counting repeated factors proves `(6)`.

It remains to bound how many right-half factors can occur at one ordinate. Let

\[
J(\gamma):=N(\gamma)-N(\gamma^-)
\tag{25}
\]

be the zero-count jump. The main term in the Bellotti--Wong approximation to `N(T)` is continuous, so the two one-sided error bounds give

\[
J(\gamma)\le2E(\gamma).
\tag{26}
\]

Every right-half zero `\rho=\beta+i\gamma` of multiplicity `m` has the distinct left-half companion

\[
1-\overline\rho=(1-\beta)+i\gamma
\tag{27}
\]

with the same multiplicity. Critical-line zeros, if present at the same ordinate, only increase `J(\gamma)`. Hence

\[
J(\gamma)\ge2D_+(\gamma),
\tag{28}
\]

and `(7)` follows from `(26)`--`(28)`. Combining with `(6)` proves `(8)`.

The estimate deliberately counts multiplicity even though the canonical identity `(4)` was stated for distinct centers. Genuine repeated zeros require the confluent/Jordan state realization studied in `NB-103`--`NB-112`; no singular distinct-node limit is being substituted for that realization here.

## 4. Adversarial controls show that the classification is rigid but not vacuous

The strongest matched control is already present in the line. `NB-098` gives three nodes separated by `O(\varepsilon)` in both horizontal and vertical directions for which the canonical condition number grows like `\varepsilon^{-4}`. Therefore `(4)` does **not** imply a perturbative theorem saying that nearly common ordinates are uniformly well conditioned. The exact common-ordinate slice is a rigid zero-shear manifold, and transverse departures can be singular.

Conversely, the identity does not deteriorate with packet size. For every fixed finite `d`, and indeed for arbitrarily large finite `d`, `(19)` is exact. Thus there is no hidden accumulation of pairwise benign horizontal interactions into the collective shear seen in `NB-098`. Any such shear requires nontrivial relative ordinate geometry.

An exact symbolic audit of the formulas `(16)`--`(17)` against the Cauchy factor `(8)` of `NB-098` gives `Q_FT_F=I` for generic three-state variables and for multiple four-state rational controls under different orders. These checks are not evidence needed by the proof; they only guard the residue/sign normalization in the stored formulas.

There are two important non-implications. First, `(8)` concerns the Hardy model-space obstruction `K_{B_\gamma}`. It does not say that a finite full-backfill Nyman section resolves the same packet with energy `O(\log\gamma/\gamma^2)`. `NB-104` already shows why absolute ordinate can re-enter finite arithmetic windows through cell averaging even though it is a gauge variable for the continuum half-line Gram. Second, `(4)` is a distinct-center statement. At an exact repeated center the coefficients `(16)`--`(17)` are singular and must be replaced by the genuine confluent/Jordan realization rather than by an arbitrary collision path.

## 5. Prior-art boundary and the remaining multi-zero frontier

Takenaka--Malmquist orthogonality in Hardy spaces is classical; a broad prior-art check found standard finite and infinite formulations, including upper-half-plane rational orthogonal systems. Burnol's Blaschke/model-space target projection is also classical and is already load-bearing in `SOURCES.md`. The Bellotti--Wong zero-count estimate used in `(7)` was added as a load-bearing source by `NB-112`. None of those ingredients is claimed new here, and no new external theorem is required by the derivation.

The line-local contribution is narrower. The exact causal-deflation matrix developed in `NB-095`--`NB-098` is identified on the common-ordinate slice with the partial-fraction map to the finite Takenaka--Malmquist system, yielding the all-rank identity `(4)` and showing that the two-state cancellation of `NB-097` survives arbitrarily many distinct horizontal centers. Combined with the already-anchored zero-count and Burnol projection formulas, exact same-height packets also have vanishing classical target obstruction at high ordinate.

This removes one natural realization of the post-`NB-112` multi-zero escape. **Several distinct off-critical centers do not become dangerous merely by crowding horizontally at one height.** For the canonical half-line state geometry, any surviving collective-shear mechanism must use nonzero relative ordinate spread. For the actual finite Nyman target, the remaining possibilities are correspondingly sharper: genuinely multi-ordinate packets, interactions between distinct centers and confluent multiplicity in the finite arithmetic window, or a different terminal representation that bypasses this canonical state geometry altogether.