# PL-418 — The canonical mod-5 covariance lift is automatically J-nonnegative, so its real spectrum is arithmetic-blind

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + DECISIVE-NEGATIVE` for the covariance-only spectral route.

**Parent findings:** `PL-415`, `PL-416`, `PL-417`.

## Claim

`PL-417` identifies `J`-nonnegativity as one possible extra property strong enough to repair the failure of bare Pontryagin selfadjointness: if a `J`-selfadjoint operator `T` also satisfies `JT >= 0`, standard Krein theory forces real spectrum. For the canonical operator obtained directly from the mod-5 channel covariance, however, this stronger property is **automatic for purely linear-algebraic reasons and therefore carries no Riemann-zero localization content**.

For a fixed finite `(X,L)` window, write the four character-channel values from `PL-416` as

\[
A_x=
\begin{pmatrix}
A_{\chi_0}(x,L)\\
A_{\chi_2}(x,L)\\
A_{\chi_4}(x,L)\\
A_{\bar\chi_4}(x,L)
\end{pmatrix}
\in\mathbb C^4
\]

and form the ordinary covariance/Gram matrix

\[
C:=\sum_x A_xA_x^*\ge 0.
\tag{1}
\]

The raw quadratic part of the repaired statistic in `PL-416` is

\[
Q_{\rm raw}=\sum_x A_x^*DA_x=\operatorname{tr}(DC),
\qquad
D=\operatorname{diag}(15,-1,-1,-1).
\tag{2}
\]

With the canonical factorization from `PL-417`,

\[
R=\operatorname{diag}(\sqrt{15},1,1,1),
\qquad
J=\operatorname{diag}(1,-1,-1,-1),
\qquad
D=RJR,
\tag{3}
\]

define

\[
B:=RCR\ge0,
\qquad
T:=JB.
\tag{4}
\]

Then

\[
\boxed{Q_{\rm raw}=\operatorname{tr}T}
\tag{5}
\]

and, more importantly,

\[
\boxed{JT=B\ge0.}
\tag{6}
\]

Thus `T` is automatically `J`-selfadjoint and `J`-nonnegative:

\[
T^*J=(BJ)J=B=JT.
\tag{7}
\]

No prime input, explicit formula, functional equation, zero location, or even multiplicativity is used in (1)--(7). The construction works for **every** collection of four complex vectors `A_x`.

The spectral consequence is therefore real but vacuous for RH. Put

\[
H:=B^{1/2}JB^{1/2}=H^*.
\tag{8}
\]

Since

\[
T=(JB^{1/2})B^{1/2},
\qquad
H=B^{1/2}(JB^{1/2}),
\]

Sylvester's determinant identity gives

\[
\det(\lambda I-T)=\det(\lambda I-H).
\tag{9}
\]

Hence

\[
\boxed{\sigma(T)\subset\mathbb R}
\tag{10}
\]

for every channel covariance, including arbitrary matched controls. If `B>0`, this is even the direct similarity

\[
B^{1/2}TB^{-1/2}=B^{1/2}JB^{1/2}.
\tag{11}
\]

Therefore the inference

\[
\text{preserve the PL-416 signed block statistic}
\;\longrightarrow\;
J\text{-nonnegative operator}
\;\longrightarrow\;
\text{real spectrum}
\]

can be realized without solving any arithmetic problem at all. Spectral reality of this canonical lift cannot distinguish RH from a hypothetical off-critical zero configuration.

## 1. The real eigenvalues can be chosen freely inside the signature constraint

The vacuity is stronger than the mere existence of the factorization above. Take arbitrary numbers

\[
b_0,b_2,b_4,b_{\bar4}\ge0
\]

and set

\[
B=\operatorname{diag}(b_0,b_2,b_4,b_{\bar4}).
\tag{12}
\]

Then

\[
C=R^{-1}BR^{-1}\ge0
\]

is a legitimate Gram matrix, and some finite family of vectors `A_x` realizes it by a Cholesky factorization. The corresponding operator is

\[
T=JB
=\operatorname{diag}(b_0,-b_2,-b_4,-b_{\bar4}).
\tag{13}
\]

Thus the four real eigenvalue magnitudes can be prescribed arbitrarily. For `B>0`, Sylvester inertia shows that the Hermitian representative (8), and hence `T`, has exactly the signature `(1,3)` forced by `J`; but **nothing in covariance positivity fixes the locations of those real eigenvalues**.

This gives a matched structural control stronger than the `2 x 2` nonreal witness of `PL-417`. Bare `J`-selfadjointness was too weak because it allowed nonreal pairs. Adding `J`-nonnegativity to the canonical covariance lift swings to the opposite failure: it guarantees reality for every input, so the conclusion is too easy to be RH-sensitive.

## 2. Why an off-line zero control does not break the argument

Suppose a zero-side or explicit-formula construction is used to generate the four channel vectors `A_x`, and suppose hypothetically that some relevant `L`-function zeros are moved off their critical lines while preserving whatever conjugation/functional-equation symmetries the control requires. The numerical values of the vectors change, but the matrix

\[
C=\sum_x A_xA_x^*
\]

remains positive semidefinite by definition. Equations (3)--(10) therefore remain valid unchanged.

Consequently, **real spectrum of `T=JRCR` survives an off-line control automatically**. It cannot serve as the theorem that converts the mod-5 source statistic into zero localization. To obtain a Hilbert--Polya mechanism one would need a separate theorem identifying the relevant zero parameters with eigenvalues of an operator before invoking spectral reality. The covariance lift supplies no such identification; it only repackages a quadratic statistic.

This distinction is consistent with known Krein-space Hilbert--Polya constructions. Kapustin constructs Krein-selfadjoint operators with eigenvalues `1/(rho(1-rho))` attached directly to zeta zeros; the indefinite setting allows the off-line case rather than proving it away. Conversely, standard `J`-nonnegative theory guarantees real spectrum once `JT>=0`. The present calculation shows that, for the `PL-416` covariance representation, this positivity can be obtained **without** attaching the operator spectrum to the zeta divisor. Spectral reality and divisor fidelity are separate gates.

## 3. Source subtraction removes the automatic positivity, and the scalar target cannot restore it

There is an important scope restriction. `PL-415` ultimately needs the **source-subtracted** signed variance

\[
\Delta T_{\chi_0}
-\frac1{15}\Delta T_{\chi_2}
-\frac2{15}\Delta T_{\chi_4},
\tag{14}
\]

whereas (1)--(13) concern the raw positive covariance part appearing in `PL-416`, before the Hardy--Littlewood model subtraction and the controlled power-of-5 terms.

Write the matrix-level residual abstractly as

\[
H:=C-C_{\rm model}=H^*,
\qquad
T_{\rm res}:=J R H R.
\tag{15}
\]

Then

\[
JT_{\rm res}=RHR.
\tag{16}
\]

Because `R` is positive and invertible, congruence preserves semidefinite order, so

\[
\boxed{
JT_{\rm res}\ge0
\iff
H\ge0
\iff
C\ge C_{\rm model}
}
\tag{17}
\]

whenever the last comparison is meaningful between Hermitian matrices. Thus the residual `J`-nonnegativity needed to recover automatic real spectrum is not a consequence of source subtraction; it is exactly a **four-channel Loewner-order theorem**. Equivalently, it requires

\[
u^*Cu\ge u^*C_{\rm model}u
\qquad\text{for every }u\in\mathbb C^4,
\tag{18}
\]

not merely control of the single signed scalar functional selected by `D`.

This separates the spectral gate from the analytic target more sharply than the original observation that `C-C_model` need not be positive. Even an exact estimate

\[
\operatorname{tr}(DH)=0
\tag{19}
\]

cannot imply (17). Consider the Hermitian residual supported only on the principal/quadratic two-channel block,

\[
H_0=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
\tag{20}
\]

Its diagonal vanishes, hence

\[
\boxed{\operatorname{tr}(DH_0)=0.}
\tag{21}
\]

Nevertheless

\[
T_0:=JRH_0R
=
\begin{pmatrix}
0&\sqrt{15}&0&0\\
-\sqrt{15}&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\tag{22}
\]

so

\[
\boxed{
\sigma(T_0)=\{i\sqrt{15},-i\sqrt{15},0,0\}.
}
\tag{23}
\]

The witness can even be realized as a difference of two positive Gram matrices. On the same `2 x 2` block let

\[
C_+=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
C_-=\frac12
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\tag{24}
\]

Both are rank-one positive semidefinite and

\[
H_0=C_+-C_-.
\tag{25}
\]

More generally, every finite-dimensional Hermitian matrix has its positive/negative spectral decomposition

\[
H=H_+-H_-,
\qquad H_\pm\ge0,
\tag{26}
\]

and each positive semidefinite term is a Gram matrix. Therefore **the formal class “difference of two covariances” imposes no residual spectral restriction by itself**. The scalar supertrace can vanish exactly while the canonical residual `J`-lift has a nonreal conjugate pair.

This is a matched structural control, not a claim that the actual Hardy--Littlewood model matrix in `PL-415` is an arbitrary positive covariance or that every formal residual is arithmetically realizable. It deliberately grants the more favorable assumption that both terms in the subtraction are positive Gram matrices and still shows that the scalar target (14) cannot supply residual `J`-nonnegativity. If the arithmetic source has an additional matrix relation that excludes (20), that relation is precisely extra mathematics that must be proved and preserved through the explicit-formula transfer.

Accordingly, a future spectral construction cannot identify the `PL-415` scalar power saving with the missing reality theorem. It must prove a genuinely stronger matrix/coercivity statement such as (17), or derive another zero-faithful property that excludes witnesses like (20). Positivity inherited merely from the raw covariance is not enough, and smallness of one signed trace is not a substitute for positivity after subtraction.

## 4. Prior-art and adversarial audit

The operator-theory ingredients are classical and no novelty is claimed for them. Friedrich Philipp, “Relatively Bounded Perturbations of J-Non-Negative Operators,” *Complex Analysis and Operator Theory* **17** (2023), Article 14, DOI `10.1007/s11785-022-01263-2`, records the standard distinction used by `PL-417`: generic `J`-selfadjoint operators may have nonreal spectrum, while `J`-nonnegative operators with nonempty resolvent have real spectrum. V. V. Kapustin, “Hilbert–Pólya Operators in Krein Spaces,” *Siberian Mathematical Journal* **65** (2024), 72--75, DOI `10.1134/S0037446624010087`, is close RH-specific prior art showing that Krein-selfadjointness can encode the zeta-zero divisor without itself forcing RH.

The extra ingredients in Section 3 are standard finite-dimensional matrix analysis: Loewner order is positivity of a Hermitian difference, invertible congruence preserves positive semidefiniteness, and every Hermitian matrix is the difference of its positive and negative spectral parts. The line-specific contribution is the exact specialization of those facts to the canonical `(1,3)` mod-5 metric and, especially, the explicit witness (20)--(23) showing that **even exact success on the signed scalar source target does not imply residual spectral reality**. No novelty is claimed for the matrix facts themselves.

The main adversarial checks are:

- `B>=0` is exact because `C` is an ordinary Gram matrix and `R` is positive diagonal; no independence or asymptotic assumption is hidden.
- Reality for singular `B` does not require an inverse: (9) follows from `det(lambda I-AB)=det(lambda I-BA)` with `A=JB^(1/2)` and `B=B^(1/2)`.
- Equation (17) is an equivalence, not a heuristic: `RHR>=0` if and only if `H>=0` because `R` is invertible.
- The witness (20) has exactly zero `D`-trace but produces the nonreal pair in (23); equations (24)--(26) show that allowing a difference of positive Gram matrices does not remove the obstruction.
- The construction does **not** claim that the actual arithmetic residual can be chosen arbitrarily. The witness only proves that neither covariance-minus-covariance structure nor the scalar supertrace estimate, by themselves, force the required matrix order.
- Arbitrary formal raw Gram matrices need not arise from actual prime data. They are used only to show that raw spectral reality is representation-theoretic. For the actual prime data the implication is even more immediate, because their covariance is also positive semidefinite.
- No conclusion is drawn that every useful operator preserving the four blocks must equal `T=JB` or `T_res=J R H R`. The obstruction is to the canonical covariance/J-nonnegative shortcut and to the stronger inference that the signed scalar residual estimate itself supplies its missing positivity.

This also matches the guardrail of `PL-263`: manufacturing a positive metric can make a spectral problem real without localizing the original zero divisor. Here the phenomenon occurs inside the exact mod-5 block geometry itself: **raw covariance positivity manufactures `J`-nonnegativity automatically, while source subtraction destroys that implication and a scalar trace bound cannot recover it**.

## Consequence for the research line

The operator frontier after `PL-417` narrows again. It is not enough to retain the signed `(1,3)` block metric and then observe `JT>=0` for the raw covariance operator, because that property survives arbitrary channel data and hypothetical off-line controls. After the required model subtraction, the exact condition becomes the full matrix inequality `C>=C_model`; the `PL-415` signed supertrace is only one linear functional of that residual and can vanish while the canonical `J`-lift has nonreal spectrum.

The analytic and spectral gates are therefore **distinct rather than identical**. Proving the `PL-407`-scale bound for the combined signed character supertrace would solve the current source-replacement estimate, but it would not by itself produce a Hilbert--Pólya reality theorem. A viable operator route must additionally derive matrix-level coercivity or an explicit-formula/divisor attachment that fails under an off-line matched control. Absent that extra structure, real spectrum remains a consequence of representation choices rather than a mechanism forcing `Re(rho)=1/2`.