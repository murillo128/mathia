# PL-416 — The repaired mod-5 source is an indefinite virtual Artin supertrace that no scalar L-function preserves at quadratic order

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + DECISIVE-REPRESENTATION-OBSTRUCTION`.

**Parent findings:** `PL-412`, `PL-414`, `PL-415`.

## Claim

`PL-415` diagonalizes the unique `p=5` source repair into the four Dirichlet-character channels modulo `5`. That exact decomposition has a stronger structural consequence than the sign warning recorded there.

On the unit group

\[
G=(\mathbb Z/5\mathbb Z)^\times\cong C_4,
\]

let `chi_0` be the principal character, `chi_2` the quadratic character, and `chi_4,\bar\chi_4` the conjugate quartic pair. The inverse local Hardy--Littlewood factor satisfies

\[
15g_5
=15\chi_0-\chi_2-\chi_4-\bar\chi_4
=16\mathbf 1-\chi_{\rm reg}.
\tag{1}
\]

Thus the repaired source is naturally a **virtual-character supertrace**, not the character of a positive representation. This is not only terminology. As a translation-invariant kernel on `G`, `g_5` has Fourier eigenvalues

\[
4,\qquad -\frac4{15},\qquad -\frac4{15},\qquad -\frac4{15},
\tag{2}
\]

so it is not positive definite. Consequently the exact local repair cannot itself be a Hilbert-space Gram kernel or an ordinary positive representation coefficient.

There is nevertheless a canonical scalar packaging. For the cyclotomic field `K=Q(zeta_5)`, the standard abelian Artin factorization is

\[
\zeta_K(s)
=\zeta(s)L(s,\chi_2)L(s,\chi_4)L(s,\bar\chi_4).
\tag{3}
\]

Hence the virtual character in (1) gives, away from the ramified prime and with the imprimitive principal factor restored exactly,

\[
\boxed{
\mathcal L_5(s)
:=\frac{L(s,\chi_0)^{15}}
{L(s,\chi_2)L(s,\chi_4)L(s,\bar\chi_4)}
=(1-5^{-s})^{15}\frac{\zeta(s)^{16}}{\zeta_K(s)}.
}
\tag{4}
\]

Equation (4) is useful as a control, but it does **not** preserve the quadratic statistic required by `PL-415`. If `A_\chi(x,L)` denotes the short-interval logarithmic-derivative sum in character channel `chi`, then the repaired variance is, after multiplying by `15`,

\[
\boxed{
Q_5(X,L)
=\sum_x A(x,L)^*D\,A(x,L),
\qquad
D=\operatorname{diag}(15,-1,-1,-1),
}
\tag{5}
\]

up to the already-controlled power-of-`5` and model-subtraction terms, where

\[
A=(A_{\chi_0},A_{\chi_2},A_{\chi_4},A_{\bar\chi_4})^T.
\]

By contrast, every **single scalar** product or quotient

\[
F(s)=\prod_\chi L(s,\chi)^{c_\chi}
\tag{6}
\]

has logarithmic-derivative window sum

\[
B(x,L)=\sum_\chi c_\chi A_\chi(x,L),
\]

and therefore ordinary second moment

\[
\sum_x|B(x,L)|^2
=\sum_x A(x,L)^*(cc^*)A(x,L).
\tag{7}
\]

The matrix `cc^*` is positive semidefinite of rank at most one. The matrix `D` in (5) has rank four and signature `(1,3)`. Therefore no scalar `L`-product/quotient can turn its ordinary variance or pair-correlation statistic into the exact repaired variance merely by choosing exponents.

In particular, the obvious virtual Artin scalar (4) has coefficient vector

\[
c=(15,-1,-1,-1),
\tag{8}
\]

so its scalar second moment contains diagonal weights `(225,1,1,1)` together with all mixed cross-character covariances. The required source supertrace instead has diagonal weights `(15,-1,-1,-1)` and no mixed terms. The mismatch is algebraic, before any RH, GRH, zero statistics, or asymptotic estimate is invoked.

The consequence for the live `PL-415` bridge is sharp: a useful zero-side mechanism must retain **graded/block information** long enough to control the indefinite supertrace (5), or estimate that signed source statistic directly. Passing first to one scalar determinant, Artin quotient, or merged signed zero divisor loses exactly the second-order information the source repair requires.

## 1. The local inverse factor is not positive definite

`PL-415` proves, for units `a,b mod 5`,

\[
g_5(a/b)
=\chi_0(a/b)-\frac1{15}
\bigl(\chi_2(a/b)+\chi_4(a/b)+\bar\chi_4(a/b)\bigr).
\tag{9}
\]

Because `chi_0=1` on `G` and the sum of all four characters is the regular character, multiplication by `15` gives (1).

The same statement can be checked without representation-theory terminology. As a class function on the abelian group `G`,

\[
g_5(e)=\frac45,
\qquad
g_5(r)=\frac{16}{15}\quad(r\ne e).
\tag{10}
\]

The characters diagonalize the convolution matrix `K(a,b)=g_5(ab^{-1})`. For the principal character,

\[
\lambda_{\chi_0}
=\frac45+3\frac{16}{15}=4.
\tag{11}
\]

For any nonprincipal character, `sum_(r in G) chi(r)=0`, hence

\[
\lambda_\chi
=\frac45+\frac{16}{15}
\sum_{r\ne e}\overline{\chi(r)}
=\frac45-\frac{16}{15}
=-\frac4{15}.
\tag{12}
\]

This proves (2). A Gram kernel must give a positive-semidefinite matrix on every finite set; here the complete `4 x 4` group kernel already has three negative eigenvalues. Therefore an exact Hilbert-space realization of this local multiplier as

\[
g_5(ab^{-1})=\langle v_a,v_b\rangle
\tag{13}
\]

is impossible.

The statement is deliberately local and exact. It does not say that the full arithmetic quantity `g_5(h)C_X(h)` is negative, nor that no larger positive operator can contain the source after adding auxiliary variables. It says only that the **declared p=5 repair itself** is an indefinite coefficient object; positivity cannot be obtained from that finite local kernel without changing or enlarging the observable.

## 2. The virtual Artin scalar exists, but it is only a first-order packaging

For the abelian extension `K=Q(zeta_5)/Q`, the four characters of `G` are exactly the Dirichlet characters modulo `5`. The regular representation decomposes as their direct sum, so the standard Artin multiplicativity gives (3).

Equation (1) corresponds to the virtual representation

\[
V=16\mathbf 1-\operatorname{Reg}_G
=15\mathbf 1-\chi_2-\chi_4-\bar\chi_4.
\tag{14}
\]

Its scalar Artin `L`-function away from `5` is therefore

\[
L(s,V)=\frac{\zeta(s)^{16}}{\zeta_K(s)}.
\tag{15}
\]

The actual principal character used in `PL-415` is imprimitive:

\[
L(s,\chi_0)=\zeta(s)(1-5^{-s}).
\tag{16}
\]

Inserting the missing local factor gives exactly (4). Thus scalarization is not being rejected because no natural scalar object exists; there is a very natural one.

But (15)--(16) package only the **linear** virtual character law. Differentiating logarithmically produces the linear combination

\[
-\frac{\mathcal L_5'}{\mathcal L_5}
=15\left(-\frac{L'}L(s,\chi_0)\right)
-\sum_{\chi\ne\chi_0}
\left(-\frac{L'}L(s,\chi)\right).
\tag{17}
\]

The `PL-415` target is not the square of this linear combination. It is the signed sum of the **individual squares/variances**. That distinction is precisely the rank/signature obstruction below.

## 3. Quadratic variance does not commute with scalarization

Write the four channel window sums as a column vector `A`. The full four-character version of `PL-415`, before identifying conjugate quartic variances, is

\[
Q_5=\sum_x
\left(
15|A_{\chi_0}|^2
-|A_{\chi_2}|^2
-|A_{\chi_4}|^2
-|A_{\bar\chi_4}|^2
\right),
\tag{18}
\]

which is (5).

For any scalar combination (6), its logarithmic derivative selects one linear functional `c^*A` on the four-dimensional channel space. Squaring it yields the rank-one Hermitian form `cc^*`. No choice of `c` can satisfy

\[
cc^*=D,
\tag{19}
\]

because `cc^*` is positive semidefinite and has rank at most one while `D` is nondegenerate with three negative directions.

For the particular Artin scalar (4), the failure is visible without ranks. With

\[
c=(15,-1,-1,-1),
\]

its variance contains

\[
225|A_{\chi_0}|^2
+|A_{\chi_2}|^2
+|A_{\chi_4}|^2
+|A_{\bar\chi_4}|^2
\tag{20}
\]

plus the six mixed channel covariances with coefficients `c_chi overline{c_psi}`. Neither the signs, the diagonal magnitudes, nor the absence of cross terms in (18) survive.

An algebraic witness makes the information loss explicit. On the formal channel vector

\[
A=(1,15,0,0)^T,
\tag{21}
\]

the Artin scalar channel has `c^*A=0`, but

\[
A^*DA=15-225=-210.
\tag{22}
\]

The actual arithmetic channel vectors need not range freely over `C^4`; (21) is therefore **not** an arithmetic counterexample. Its role is only to prove that scalarization is not an injective representation of the quadratic observable. Any arithmetic recovery would require an additional relation among the channels, and that additional relation — not the scalar quotient itself — would carry the substantive content.

## 4. The same obstruction appears on the zero side

The virtual scalar (4) has a signed divisor: zeros from the principal/zeta channel occur with positive multiplicity, while zeros of the nonprincipal Dirichlet factors enter with negative multiplicity unless cancelled. A pair-correlation statistic formed from this single signed divisor is quadratic in the divisor weights. Schematically it contains

\[
\sum_{\chi,\psi}c_\chi\overline{c_\psi}\,
\mathcal C_{\chi,\psi},
\tag{23}
\]

including cross-correlations between distinct `L`-functions.

The source target from `PL-415` is instead the supertrace

\[
15\mathcal C_{\chi_0,\chi_0}
-\mathcal C_{\chi_2,\chi_2}
-\mathcal C_{\chi_4,\chi_4}
-\mathcal C_{\bar\chi_4,\bar\chi_4},
\tag{24}
\]

with **linear** virtual-character weights and no cross-channel terms. Equations (23)--(24) are the zero-side version of `cc^* != D`.

Therefore a functional equation, zero symmetry, determinant, or superdeterminant for the single scalar `mathcal L_5` cannot by itself provide the `PL-407` power saving for the repaired variance. One would still need a theorem that separates the blocks or proves a special cancellation among the mixed correlations. Such a theorem could be valuable, but it would be new arithmetic input rather than a consequence of scalar Artin packaging.

This also clarifies the GRH guardrail in `PL-415`. Treating the four blocks separately risks importing GRH/pair-correlation hypotheses for the auxiliary Dirichlet `L`-functions. Merging them into one virtual scalar avoids separate notation but does **not** remove the auxiliary channels; it merely replaces the diagonal supertrace by a different quadratic statistic containing their cross-correlations.

## 5. Prior-art and novelty audit

The ingredients surrounding the obstruction are classical. Finite abelian characters diagonalize translation-invariant kernels; Artin `L`-functions multiply under direct sums and extend to virtual characters; for `Q(zeta_5)` the regular-character factorization gives (3); and Dirichlet-`L` short-interval variance / pair-correlation theory is already represented in `SOURCES.md` by Yildirim, Bui--Keating--Smith, and Kandhil--Languasco--Moree. The Artin-normalization literature recorded there, including Keys--Shahidi, is further control that scalar arithmetic `L`-factors and their normalizations are established machinery.

Targeted searches for virtual-character or virtual-Artin pair correlation, signed Dirichlet-`L` variance, and supertrace formulations did not locate the exact line-specific statement `cc^* != D` for the `p=5` inverse Hardy--Littlewood factor. No general novelty is claimed for virtual Artin `L`-functions, character orthogonality, cyclotomic factorization, positive-definite finite-group kernels, or mixed moments. The durable contribution here is narrower: **the exact repaired Mathia source is an indefinite full-rank quadratic supertrace, whereas every one-scalar logarithmic-derivative variance is rank-one positive semidefinite**.

That distinction is falsifiable and representation-level. A proposed scalar replacement must exhibit an additional arithmetic identity that reconstructs (18) from its scalar channel; absent such an identity, the scalar quotient has provably discarded required quadratic information.

## 6. Adversarial audit and boundaries

1. **This is not an impossibility theorem for the signed variance bound.** Arithmetic may force cancellations in the actual channel vector that are invisible to abstract `C^4` linear algebra. The result only says that those cancellations do not follow from replacing the four blocks by one scalar `L`-function.

2. **Several scalar quadratic forms can reconstruct the target.** By retaining four channel projections and taking their signed combination one recovers `D` exactly. But that is precisely the graded/block supertrace (18), not a one-scalar reduction. The finding rejects scalarization, not finite-dimensional block analysis.

3. **A Krein-space or super-Hilbert realization remains open.** Negative Fourier eigenvalues rule out the exact local kernel as a positive Hilbert Gram matrix, but indefinite inner products can represent it. Such a realization would still need a coercive or cancellation theorem at the `PL-407` scale to matter for RH.

4. **The prime `5` is ramified in the cyclotomic field.** Equation (15) is the clean Artin identity away from the ramified coordinate. Equation (4) restores the imprimitive principal factor actually used in `PL-415`; no ramified Euler factor is silently identified with an unramified one.

5. **Functional-equation symmetry is not positivity.** The virtual quotient inherits the expected scalar functional-equation structure from its factors, but a signed quotient with poles from denominator zeros supplies no theorem forcing those auxiliary divisors or the desired supertrace to have a sign. The symmetry itself does not resolve `PL-415`.

6. **The zero-side statement is structural, not an unproved zero-statistics asymptotic.** Equation (23) only records the algebra of squaring a signed scalar divisor/channel. It does not assume a mixed pair-correlation conjecture or claim a particular asymptotic for distinct Dirichlet `L`-functions.

## Consequence for the line

`PL-415` left open whether the special coefficients `1,-1/15,-2/15` might acquire a more rigid meaning on the spectral side. They do: after restoring the conjugate quartic block they are the virtual character `16*1-Reg_G`. But the most obvious payoff — package that virtual character into one Artin `L`-quotient and use its scalar zero statistics — fails at the next operation, because **variance is quadratic**.

The live target is therefore not a scalar virtual `L`-function. It is the graded block observable

\[
\operatorname{Str}_D(A^*A)
=15|A_{\chi_0}|^2
-|A_{\chi_2}|^2
-|A_{\chi_4}|^2
-|A_{\bar\chi_4}|^2,
\tag{25}
\]

or an equivalent source-side formulation preserving the same four-channel information. The next useful pass should test whether explicit-formula machinery for this **block supertrace** produces a cancellation of mixed/auxiliary terms before any triangle inequality, or whether a matched arithmetic control shows that no source-forced cancellation stronger than the componentwise variance bounds is available. A one-scalar determinant or virtual Artin quotient should now be treated only as a control, not as the candidate mechanism.