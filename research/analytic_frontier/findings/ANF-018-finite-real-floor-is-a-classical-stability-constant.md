# ANF-018 — the finite-real floor is a classical stability constant

**Status:** `EXACT-DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-BOUNDARY`. The finite-real functional isolated in `ANF-017` is not an ad hoc zeta-specific minimization. For every continuous real-even `J>=0` supported in `[-1,1]`, with `F=widehat J`, its floor

\[
q_{\rm real}(J)
=\inf_X\frac1{|X|}\sum_{x,y\in X}F(x-y)
\]

is exactly the optimal classical stability constant of the pair potential `F`, after restoring the diagonal self-energy. This converts the remaining universal-affine Montgomery--Taylor question into a sharp one-dimensional many-particle binding problem for positive-type compact-spectrum potentials. The classical statistical-mechanics literature already studies precisely this Fourier-positive interaction class, but its standard stability inequality is far too weak for the Montgomery--Taylor threshold; the new load-bearing quantity is the **best** stability constant, including finite-volume binding below the thermodynamic unit-chain energy.

More precisely, write

\[
F_0:=F(0)=\int_{-1}^{1}J(\alpha)\,d\alpha,
\qquad
j_0:=J(0),
\qquad
I(J):=\int_{-1}^{1}|\alpha|J(\alpha)\,d\alpha,
\]

so that the BGSST cost is

\[
C(J)=j_0+I(J).
\]

If `B_stab(F)` denotes the least stability constant in

\[
\sum_{1\le i<j\le n}F(x_i-x_j)\ge-B_{\rm stab}(F)n
\qquad\text{for every finite real configuration},
\]

then

\[
\boxed{q_{\rm real}(J)=F_0-2B_{\rm stab}(F).}
\]

Consequently the universal finite-real no-go target

\[
\frac{C(J)}{q_{\rm real}(J)}\ge C_{\rm MT}
\]

is equivalent to the sharp **minimum-binding requirement**

\[
\boxed{
B_{\rm stab}(F)
\ge
\frac12\left(F_0-\frac{C(J)}{C_{\rm MT}}\right).
}
\]

This is the correct classical-mechanics quantity to attack next.

## 1. Exact identification with the optimal stability constant

For a finite set `X={x_1,...,x_n}` of distinct real points define the off-diagonal pair energy

\[
U_F(X):=\sum_{1\le i<j\le n}F(x_i-x_j).
\tag{1}
\]

The full Gram energy and the normalized energy of `ANF-017` are

\[
E_F(X)
=\sum_{i,j=1}^nF(x_i-x_j)
=nF_0+2U_F(X),
\tag{2}
\]

and therefore

\[
e_J(X)
=\frac{E_F(X)}n
=F_0+2\frac{U_F(X)}n.
\tag{3}
\]

The classical stability constant is the smallest `B>=0` such that `U_F(X)>=-Bn` for every finite configuration. Equivalently,

\[
B_{\rm stab}(F)
:=\sup_X\left(-\frac{U_F(X)}{|X|}\right).
\tag{4}
\]

Taking the infimum of (3) gives the exact identity

\[
\boxed{
q_{\rm real}(J)=F_0-2B_{\rm stab}(F).
}
\tag{5}
\]

The convention about coincident particles does not affect this optimum here. `F` is continuous, so any finite multiset can be approximated arbitrarily closely in energy by a set of distinct points, while sets are already a subclass of multisets.

Because `J>=0`, Fourier inversion gives for every finite configuration

\[
E_F(X)
=\int_{-1}^{1}J(\alpha)
\left|\sum_{x\in X}e^{-2\pi i\alpha x}\right|^2d\alpha
\ge0.
\tag{6}
\]

Hence

\[
0\le q_{\rm real}(J)\le F_0,
\qquad
0\le B_{\rm stab}(F)\le\frac{F_0}{2}.
\tag{7}
\]

The right inequality is the familiar positive-type stability bound. Equation (5) says that the Mathia quantity `q_real` records how far the **optimal** stability constant lies below or above any particular finite or thermodynamic test.

## 2. The compact-spectrum class is a classical ground-state class

Sütő's 2005 ground-state theorem studies translation-invariant pair potentials whose Fourier transform is nonnegative and vanishes outside a finite wave-number ball. This is exactly the present structural class after Fourier-convention rescaling: our support `|alpha|<=1` corresponds to Sütő bandwidth `K_0=2pi`.

Under Sütő's additional absolute-integrability hypotheses, the one-dimensional critical density is therefore

\[
\rho_1=\frac{K_0}{2\pi}=1.
\tag{8}
\]

At that density the uniform chain is the distinguished periodic ground state when the spectrum is strictly positive in the interior; above the threshold there is the familiar degeneracy of compact-spectrum or "stealthy" ground states. Sütő's Fourier-square identity is the same mechanism as (6), and his generic stability conclusion is `U_F(X)>=-F_0|X|/2`.

In the present normalization, the full energy per particle of the unit chain is `j_0`. Independently of the extra hypotheses needed for the infinite-volume ground-state theorem, the finite Fejer limit already used in `ANF-013` gives

\[
\boxed{q_{\rm real}(J)\le j_0.}
\tag{9}
\]

Thus the thermodynamic tests of `ANF-013`--`ANF-016` have a standard many-particle interpretation: they probe bulk ground-state energy. `ANF-017` then shows why that is not the whole problem. A finite cluster can bind **below** the bulk unit-chain value because boundary degrees of freedom disappear in the infinite-volume limit.

Define that finite-configuration binding gain by

\[
b_{\rm fin}(J):=j_0-q_{\rm real}(J)\ge0.
\tag{10}
\]

It need not always be literally a surface term, but for the cubic witness of `ANF-017` it is produced by detuning only the two boundary gaps.

## 3. Montgomery--Taylor becomes an exact binding threshold

Put

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=1.327499296320588\ldots,
\qquad
m_{\rm MT}:=C_{\rm MT}-1
=0.327499296320588\ldots .
\tag{11}
\]

If `q_real(J)=0`, the shape cannot support a positive improved universal-affine bound, so suppose `q_real(J)>0`. Using `C(J)=j_0+I(J)` and `q_real=j_0-b_fin`, the desired finite-real no-go inequality is equivalent to

\[
\boxed{
C_{\rm MT}\,b_{\rm fin}(J)+I(J)
\ge
m_{\rm MT}\,j_0.
}
\tag{12}
\]

This splits the scalar frontier cleanly. If

\[
I(J)\ge m_{\rm MT}j_0,
\tag{13}
\]

the thermodynamic unit-chain test `q_real<=j_0` already forces Montgomery--Taylor. Only spectra with an unusually small normalized first moment

\[
I(J)<m_{\rm MT}j_0
\tag{14}
\]

need any finite-volume correction at all. In that residual region, the exact amount required is

\[
\boxed{
b_{\rm fin}(J)
\ge
\frac{m_{\rm MT}j_0-I(J)}{C_{\rm MT}}.
}
\tag{15}
\]

Using (5), the same condition is

\[
\boxed{
B_{\rm stab}(F)
\ge
\frac12\left(F_0-\frac{C(J)}{C_{\rm MT}}\right).
}
\tag{16}
\]

When the right side of (16) is nonpositive, even the singleton test is enough. When it is positive, a putative scalar survivor is exactly a compact-spectrum positive-type potential whose optimal attractive binding is **too weak** to reach the threshold in (16).

This is more useful than another finite configuration search because it identifies the quantity that must eventually be bounded globally. Individual configurations only give lower bounds on `B_stab`; proving a true scalar survivor requires an **upper** bound on the optimal stability constant below the right side of (16).

## 4. The cubic of ANF-016 sits almost exactly on the binding threshold

For the cubic spectrum killed in `ANF-017`,

\[
j_0=1,
\qquad
I(J_*)=\frac{13}{40}=0.325,
\qquad
F_0=\frac{49}{48},
\qquad
C(J_*)=\frac{53}{40}.
\tag{17}
\]

Its first spectral moment misses the automatic thermodynamic threshold by only

\[
m_{\rm MT}-\frac{13}{40}
=0.002499296320588\ldots .
\tag{18}
\]

Equation (15) therefore demands the finite binding gain

\[
\boxed{
b_{\rm fin}(J_*)\ge0.00188271009070635\ldots .}
\tag{19}
\]

The explicit 15-site edge-detuned configuration of `ANF-017` has

\[
e_*(X_*)=0.998079905262228\ldots,
\]

so it proves

\[
b_{\rm fin}(J_*)
\ge1-e_*(X_*)
=0.001920094737772\ldots,
\tag{20}
\]

crossing the exact requirement by only

\[
3.73846470656\times10^{-5}.
\tag{21}
\]

The same calibration in stability language is

\[
B_{\rm stab}(F_*)
\ge\frac12\left(\frac{49}{48}-e_*(X_*)\right)
=0.0113767140355527\ldots,
\tag{22}
\]

whereas Montgomery--Taylor requires only

\[
B_{\rm stab}(F_*)
\ge0.0113580217120198\ldots .
\tag{23}
\]

The thermodynamic unit chain itself supplies

\[
B_{\rm chain}
=\frac12\left(\frac{49}{48}-1\right)
=\frac1{96}
=0.0104166666666667\ldots .
\tag{24}
\]

Thus the finite edge relaxation in `ANF-017` contributes an additional

\[
0.000960047368886\ldots
\]

of binding beyond the unit chain, just exceeding the additional

\[
0.000941355045353\ldots
\]

needed to restore Montgomery--Taylor. The apparent thermodynamic escape in `ANF-016` was therefore quantitatively a **missing finite-cluster binding energy**.

## 5. Ground-state autocorrelation almost returns to the nonnegative-spatial class, but with an `n`-fold budget loss

There is a tempting route from a minimizing configuration back to the nonnegative-spatial extremal problem of Carneiro--Chandee--Littmann--Milinovich. Let `X={x_1,...,x_n}` and put

\[
S_X(\alpha)=\sum_{j=1}^ne^{-2\pi i\alpha x_j},
\qquad
R_X(t)=\frac1n\sum_{i,j=1}^nF(t+x_i-x_j).
\tag{25}
\]

Then

\[
R_X
=\widehat{H_X},
\qquad
H_X(\alpha)=J(\alpha)\frac{|S_X(\alpha)|^2}{n}\ge0.
\tag{26}
\]

For a translate `t` such that `X` and `X+t` are disjoint,

\[
e_J\bigl(X\cup(X+t)\bigr)=e_J(X)+R_X(t).
\tag{27}
\]

Since the left side is at least `q_real(J)`, continuity extends the inequality

\[
\boxed{R_X(t)\ge q_{\rm real}(J)-e_J(X)\qquad(t\in\mathbb R).}
\tag{28}
\]

Hence an exact finite minimizer, if one exists, has `R_X(t)>=0` everywhere. A minimizing sequence produces autocorrelation kernels that are asymptotically nonnegative from below.

This looks as though the CCLM nonnegative-spatial theorem might close the problem immediately, but the normalization reveals a precise obstruction. At zero frequency,

\[
H_X(0)=nJ(0)=nj_0,
\tag{29}
\]

and, since `|S_X(alpha)|^2/n<=n`,

\[
C(H_X)\le nC(J).
\tag{30}
\]

A black-box CCLM application to an exact minimizer gives `C(H_X)>=C_MT R_X(0)=C_MT q_real(J)`. Combining it only with (30) loses a factor `n` and yields `C(J)>=C_MT q_real(J)/n`, not the desired factor-one inequality.

Therefore **autocorrelation positivity is real but does not preserve the BGSST budget**. Any successful use of this route must exploit substantially more structure of the finite structure factor than the trivial bound in (30), or find a normalization that does not multiply `J(0)` by the particle count.

## 6. Prior-art boundary

The statistical-mechanics identification is classical in its ingredients. Ruelle stability is the standard condition that a pair energy be bounded below by `-BN`; Procacci's modern review uses exactly this stability constant terminology. Sütő proves the Fourier-square positivity and infinite-volume ground-state structure for nonnegative compactly supported Fourier transforms, including the one-dimensional uniform-chain threshold. The later stealthy-hyperuniform literature develops the same compact-spectrum/structure-factor viewpoint and emphasizes the highly degenerate thermodynamic ground-state manifold.

What is derived here is the exact translation of the Mathia finite-real functional into that language, equations (5), (12) and (16), together with the quantitative calibration of the `ANF-017` boundary witness and the budget-loss check (25)--(30). A targeted search across stability constants, compact-Fourier pair potentials, stealthy ground states and the Montgomery--Taylor pair-correlation problem did not locate the specific sharp inequality (16) or its zeta-zero interpretation. No publication-level novelty claim is made.

The literature also does **not** justify replacing `q_real` by a thermodynamic ground-state energy. `q_real` is the finite-configuration optimal stability quantity over all particle numbers and densities. `ANF-017` is already an explicit counterexample to such a replacement: its boundary-relaxed finite cluster lies below the relevant unit-chain bulk energy.

## 7. Next boundary

The scalar frontier can now be stated as a classical sharp-stability problem:

\[
\boxed{
B_{\rm stab}(\widehat J)
\stackrel{?}{\ge}
\frac12\left(
\widehat J(0)-\frac{J(0)+\int|\alpha|J(\alpha)d\alpha}{C_{\rm MT}}
\right)
}
\tag{31}
\]

for every continuous even `J>=0` supported in `[-1,1]`, with the right side understood as vacuous when nonpositive.

This suggests a sharper prior-art and proof search than arbitrary finite enumeration: one-dimensional best stability constants, finite-cluster ground states, boundary corrections, collective-coordinate/structure-factor constraints, and exact lower-energy constructions for positive-type compact-spectrum potentials. A candidate scalar counterexample must do more than survive sampled configurations: it must provide a rigorous **upper bound** on `B_stab` below (31), equivalently a rigorous lower bound `q_real>C/C_MT`.

This finding does not prove (31). It does not close the universal-affine scalar branch, does not constrain the configuration-level escape of `ANF-006`, and does not import Sütő's infinite-volume conclusions into spectra outside his extra integrability hypotheses. Its contribution is to identify the remaining finite-real problem with a mature classical variational object and to expose the exact amount of binding that Montgomery--Taylor requires.