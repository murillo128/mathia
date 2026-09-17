# AF-406 — Finite coefficient Pólya-frequency positivity is not zero-set faithful under exponential gauge

**Status:** `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-FIDELITY`, `TOTAL-POSITIVITY`, `LAGUERRE-POLYA`, `RIEMANN-XI`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-REDIRECT`, `NO-NOVELTY-CLAIM`

## Claim

Finite-order **coefficient-sequence** Pólya-frequency positivity is not a faithful invariant of the zero set, even on the classical Riemann-`xi` generating-function family.

Write

\[
\xi_1(z)=\xi(\sqrt z+1/2)=\sum_{k\ge 0} b_k z^k.
\tag{1}
\]

Katkova proved three facts that are decisive for the fidelity interpretation of finite coefficient total positivity:

1. `xi_1 in PF_44` unconditionally;
2. `xi_1 in APF_m` for every finite `m`;
3. for every finite `m` there exists `n_0(m)` such that, for every integer `n >= n_0(m)`,

\[
e^{nz}\xi_1(z)\in PF_m.
\tag{2}
\]

The multiplier `e^{nz}` has no zeros, so

\[
Z(e^{nz}\xi_1)=Z(\xi_1)
\tag{3}
\]

with multiplicity. Therefore, for every fixed finite `m`, the truth value of coefficient-sequence membership in `PF_m` can be changed to positive along a **zero-preserving exponential gauge orbit** without changing the discriminator relevant to RH.

Consequently, a finite-order coefficient Pólya-frequency verdict cannot by itself be a zero-set-faithful certificate. Any attempt to use finite coefficient `PF_m` positivity as a proxy for the Laguerre–Pólya / RH target must either fix the exponential gauge by an independent canonical normalization or retain additional structure that is not manufactured by the gauge.

This strengthens AF-372 in a source-specific direction. AF-372 gives generic false positives at every bounded determinant order. Katkova's theorem shows, for the actual `xi_1` source, that finite coefficient positivity is also **gauge-manufacturable while the entire zero divisor is held fixed**.

The qualifier "coefficient-sequence" is load-bearing. Continuous Pólya-frequency / total-positivity questions for a translation kernel `f(x-y)` transform differently under an exponential tilt of the profile: there the same-looking affine exponential factor is already a positive row/column gauge and cannot change any translation-minor sign. The exact distinction is derived below.

## Exact fidelity statement for coefficient sequences

Let

\[
F_n(z)=e^{nz}\xi_1(z),
\qquad n\ge 0,
\tag{4}
\]

and let the target discriminator be any property depending only on the zero divisor, for example

\[
D(F)=\mathbf 1_{\{Z(F)\subset(-\infty,0]\}}.
\tag{5}
\]

Equation `(3)` gives

\[
D(F_n)=D(\xi_1)
\qquad\text{for every }n.
\tag{6}
\]

For a fixed finite `m`, define the **coefficient-sequence** observable

\[
C_m(F)=\mathbf 1_{\{(a_k(F))_{k\ge0}\in PF_m\}},
\tag{7}
\]

where `F(z)=sum_k a_k(F) z^k`. Katkova's Theorem 3 gives an `n_0(m)` for which

\[
C_m(F_n)=1
\qquad(n\ge n_0(m)).
\tag{8}
\]

Thus `C_m` is not invariant on zero-divisor fibers. In Arithmetic Fidelity language, it cannot be an intrinsic observable of the quotient that forgets the zero-free exponential factor.

The obstruction is stronger than ordinary finite-order insufficiency. It is not merely that two unrelated functions may share the same finite positivity verdict. Here a transformation that preserves **all zeros exactly** can force the finite coefficient-positivity verdict after sufficiently strong exponential tilting.

## Category boundary: translation total positivity already quotients affine exponential profile gauges

Now consider a different classical Pólya-frequency category: a real profile `f` through its translation kernel

\[
K_f(x,y)=f(x-y).
\tag{9}
\]

For real `a,b`, put

\[
\widetilde f(t)=e^{at+b}f(t).
\tag{10}
\]

Then

\[
K_{\widetilde f}(x,y)
=e^b e^{ax}K_f(x,y)e^{-ay}.
\tag{11}
\]

Hence every `r x r` translation minor obeys the exact covariance law

\[
\boxed{
\det\bigl(K_{\widetilde f}(x_i,y_j)\bigr)
=
 e^{br+a\sum_i x_i-a\sum_j y_j}
\det\bigl(K_f(x_i,y_j)\bigr).
}
\tag{12}
\]

The multiplier in `(12)` is strictly positive. Therefore, for every fixed order `r` and also at all orders, weak or strict translation total positivity/sign regularity is **exactly invariant** under `(10)`. No canonical normalization is needed to protect translation-minor signs from this affine exponential gauge: the determinant representation has already quotiented it by positive diagonal row/column equivalence.

The same statement holds for the local confluent hierarchy used in AF-403--AF-405. Define

\[
H_r(f;t)
=(-1)^{r(r-1)/2}
\det\bigl(f^{(i+j)}(t)\bigr)_{0\le i,j<r}.
\tag{13}
\]

Let `P_r(a)` be the lower-unitriangular binomial matrix

\[
(P_r(a))_{ij}=\binom{i}{j}a^{i-j}
\qquad(0\le j\le i<r).
\tag{14}
\]

Since

\[
(e^{at+b}f)^{(k)}
=e^{at+b}(D+a)^k f,
\tag{15}
\]

Vandermonde's identity gives the derivative-Hankel matrix factorization

\[
M_r(\widetilde f;t)
=e^{at+b}P_r(a)M_r(f;t)P_r(a)^T.
\tag{16}
\]

Because `det P_r(a)=1`,

\[
\boxed{
H_r(\widetilde f;t)=e^{r(at+b)}H_r(f;t).
}
\tag{17}
\]

In the normalized notation of AF-404,

\[
R_r(f;t)=\frac{H_r(f;t)}{f(t)^r},
\qquad
q_f=-(\log f)'',
\tag{18}
\]

one therefore has the exact gauge invariants

\[
\boxed{
R_r(\widetilde f)=R_r(f),
\qquad
q_{\widetilde f}=q_f.
}
\tag{19}
\]

In particular the current order-five Toda gate for the full Euler-log profile,

\[
(\log R_4)''<4q,
\tag{20}
\]

is itself invariant under every affine exponential profile tilt `(10)`.

Equations `(12)`--`(20)` are elementary consequences of the translation-kernel representation, but they materially delimit the AF-406 obstruction: **Katkova's exponential smoothing acts on the coefficient Toeplitz representation, whereas affine exponential tilting of a translation profile acts only by positive diagonal equivalence.** The two uses of Pólya-frequency language must not be identified.

## Relation to all-order coefficient total positivity

There is no contradiction with the all-order coefficient criterion.

Katkova recalls the classical Aissen–Schoenberg–Whitney–Edrei equivalence

\[
\xi_1\in PF_\infty
\quad\Longleftrightarrow\quad
\xi_1\in L\!\! -\! P^+
\quad\Longleftrightarrow\quad
\mathrm{RH}.
\tag{21}
\]

Her finite-order smoothing result states that, for each fixed `m`, one can choose `n` large enough to obtain coefficient `PF_m`. It does **not** provide one finite `n` for which the tilted function is in `PF_m` simultaneously for every `m`, unless the all-order target is already satisfied.

Hence the quantifiers are the essential surviving structure:

\[
\forall m\ \exists n_0(m)\ \forall n\ge n_0(m): F_n\in PF_m
\tag{22}
\]

is strictly weaker than

\[
\exists n\ \forall m: F_n\in PF_m.
\tag{23}
\]

This is another concrete instance of the Arithmetic Fidelity theme that every fixed finite compression can look fully positive while the unbounded relational hierarchy retains the target information.

## Consequence for the current confluent-Hankel branch

AF-404 and AF-405 study the signed confluent determinants `(13)` for the full Euler/log translation kernel. These are local confluent certificates for a **continuous translation-minor hierarchy**, not coefficient Toeplitz minors of `xi_1`.

Katkova's result therefore does **not** settle the open `H_5` sign question, and it also does not create an exponential-gauge-normalization requirement for that branch. Equations `(17)`--`(20)` show more strongly that `H_5` sign, every translation-minor sign, and the normalized Toda gate are already invariant under the affine exponential profile gauge.

A proof of `H_5>0` would thus be a genuine structural fact about the Euler-log translation kernel, not a signature that can be manufactured by the particular tilt used in `(10)`. It still would not by itself become evidence for RH: AF-217 proves that the same translation kernel eventually fails at some finite order, and no theorem here identifies its finite-order signs with the zero-divisor target. The live question remains the exact finite-order boundary and what source/target relation, if any, makes that hierarchy arithmetically discriminating.

This distinction repairs a dangerous transfer error. The right audit is not "all finite positivity must first be normalized against exponentials." The right audit is: **identify the representation on which the target-preserving transformation acts, then test whether the proposed observable actually varies along that orbit.**

## Prior-art and novelty audit

- Olga M. Katkova, **“Multiple Positivity and the Riemann Zeta-Function,”** *Computational Methods and Function Theory* **7**(1) (2007), DOI `10.1007/BF03321628`; arXiv:`math/0505174`. Role: Theorem 1 proves `xi_1 in PF_44`; Theorem 2 proves `xi_1 in APF_m` for every finite `m`; Theorem 3 proves that for each finite `m`, sufficiently large exponential multipliers `e^{nz}` put the **coefficient sequence** of `xi_1` in `PF_m` without changing its zero set.
- I. J. Schoenberg, **“On the Zeros of the Generating Functions of Multiply Positive Sequences and Functions,”** *Annals of Mathematics* **62** (1955), 447–471, DOI `10.2307/1970073`. Role: classical finite-order multiple-positivity and zero-location background used by Katkova.
- M. Aissen, I. J. Schoenberg, A. Whitney and A. Edrei, **“On the Generating Functions of Totally Positive Sequences,”** *Journal d'Analyse Mathématique* **2** (1953), 93–109. Role: classical coefficient-sequence Toeplitz total positivity / generating-function characterization underlying the all-order RH equivalence for `xi_1`.
- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* **1** (1951), 331–374, DOI `10.1007/BF02790092`. Role: classical continuous Pólya-frequency-function theory, where total positivity is attached to a translation kernel rather than to the coefficient Toeplitz matrix of a power series.
- I. J. Schoenberg and Anne Whitney, **“On Pólya Frequency Functions. III. The Positivity of Translation Determinants With an Application to the Interpolation Problem by Spline Curves,”** *Transactions of the American Mathematical Society* **74** (1953), 246–259, DOI `10.2307/1990881`. Role: direct classical prior art for positivity of translation determinants.

No novelty is claimed for Katkova's finite-order theorems, zero preservation under multiplication by a zero-free exponential, continuous Pólya-frequency definitions, or positive diagonal invariance of determinant signs. The Arithmetic Fidelity contribution is the category-level audit: **coefficient finite multiple positivity is not invariant under a natural zero-preserving gauge, while continuous translation total positivity is invariant under the corresponding affine profile tilt.** A fidelity obstruction belongs only to the representation on which the observable actually changes.

## Decisive audit rule

When finite-order positivity is proposed as evidence for a target invariant under a transformation, first specify the positivity category and compute the transformation on that representation.

For a generating function whose **coefficient sequence** is tested for `PF_m`, Katkova shows that `F(z) -> e^{az}F(z)` can force any fixed finite order while preserving the zero divisor, so the finite coefficient verdict is not a zero-set quotient invariant.

For a **continuous translation kernel** `K_f(x,y)=f(x-y)`, the affine profile tilt `f(t) -> e^{at+b}f(t)` changes every minor only by the positive factor `(12)` and changes every normalized confluent certificate by no amount at all. That gauge is already invisible to the observable and cannot manufacture translation total positivity.

Do not transfer a gauge obstruction from one Pólya-frequency representation to another merely because both use the same terminology or an exponential multiplier.