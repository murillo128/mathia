# PL-421 — Local-factor insertion is exact dephasing; its positive image cone has a `1/(p-1)` spectral floor

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + RANGE-CHARACTERIZATION`.

**Parent findings:** `PL-414`, `PL-415`, `PL-419`, `PL-420`.

## Claim

`PL-420` leaves one precise escape: although exact deletion of the odd-prime Hardy--Littlewood local factor is not positive on the full PSD cone, it could still be positive on the smaller cone actually produced by arithmetic local-factor insertion. For the two-level prime-pair factor used in this line, that smaller cone can be characterized **exactly and non-circularly**.

Let

\[
U_p=(\mathbb Z/p\mathbb Z)^\times,
\qquad n=p-1,
\]

and let `B_p` be the local-factor Schur symbol from `PL-420`, with

\[
(B_p)_{aa}=d_p:=\frac{p}{p-1},
\qquad
(B_p)_{ab}=c_p:=\frac{p(p-2)}{(p-1)^2}
\quad(a\ne b).
\tag{1}
\]

After removing the harmless overall scalar `d_p`, define

\[
\Psi_p(R):=d_p^{-1}(B_p\circ R).
\tag{2}
\]

Then

\[
\boxed{
\Psi_p(R)
= r_p R+\delta_p\operatorname{Diag}(R),
\qquad
r_p=\frac{p-2}{p-1},
\qquad
\delta_p=\frac1{p-1},
}
\tag{3}
\]

with `r_p+delta_p=1`. Thus ordinary local-factor insertion is, up to scale, exactly a **uniform dephasing / covariance-shrinkage map**: it preserves the diagonal and attenuates every cross-residue coherence by the same factor `r_p`.

Its inverse is

\[
\boxed{
\Psi_p^{-1}(S)
=\frac1{r_p}
\left(S-\delta_p\operatorname{Diag}(S)\right).
}
\tag{4}
\]

Therefore the exact image of the positive cone is

\[
\boxed{
\Psi_p(M_n^+)
=
\left\{
S=S^*:
S-\frac1{p-1}\operatorname{Diag}(S)\ge0
\right\}.
}
\tag{5}
\]

If all diagonal entries of `S` are positive and

\[
D:=\operatorname{Diag}(S),
\qquad
C:=D^{-1/2}SD^{-1/2},
\tag{6}
\]

so that `C` is the normalized correlation matrix, then (5) is equivalent to the sharp spectral-floor condition

\[
\boxed{
\lambda_{\min}(C)\ge\frac1{p-1}.
}
\tag{7}
\]

For the live `p=5` repair,

\[
\boxed{
\Psi_5(R)=\frac34R+\frac14\operatorname{Diag}(R),
\qquad
S\in\Psi_5(M_4^+)
\iff
\lambda_{\min}(C_S)\ge\frac14.
}
\tag{8}
\]

So the restricted arithmetic cone left open by `PL-420` is not an unspecified exotic subset of PSD matrices. It is exactly the cone of residue covariance matrices whose normalized Gram geometry has a fixed lower Riesz bound. The remaining arithmetic question becomes quantitative and falsifiable: **do the actual residue/character correlation matrices relevant to the source transfer have a uniform lower spectral floor of at least `1/4` after the required normalization?**

This does not prove that they do. It converts the surviving positivity escape into a concrete matrix inequality that can be attacked by cross-residue decorrelation, a lower-frame estimate, or an operator-norm bound.

## 1. The local Schur map is a normalized dephasing map

From (1),

\[
\frac{c_p}{d_p}
=
\frac{p-2}{p-1}
=:r_p,
\qquad
1-r_p
=
\frac1{p-1}
=: \delta_p.
\tag{9}
\]

Let `A_p=d_p^{-1}B_p`. Then `A_p` has diagonal `1` and constant off-diagonal value `r_p`, so

\[
A_p=r_p\mathbf1\mathbf1^*+\delta_p I.
\tag{10}
\]

Taking the Schur product with `R` gives

\[
A_p\circ R
=
r_pR+\delta_p(I\circ R)
=
r_pR+\delta_p\operatorname{Diag}(R),
\tag{11}
\]

which is (3).

The terminology is standard rather than novel. A Schur-product quantum/dephasing channel is a completely positive map `X -> A circ X` with `A` a correlation matrix; equivalently it preserves diagonal entries while damping off-diagonal coherence. In covariance estimation, convex combinations with a diagonal or identity target are the classical linear-shrinkage architecture. The line-specific point is not either general framework, but the exact arithmetic parameter

\[
\boxed{\delta_p=1/(p-1)}
\tag{12}
\]

forced by the Hardy--Littlewood local factor.

## 2. Exact image-cone theorem

Because `r_p>0` for every odd prime,

\[
S=\Psi_p(R)
\iff
R=\frac1{r_p}
\left(S-\delta_p\operatorname{Diag}(S)\right).
\tag{13}
\]

Hence

\[
R\ge0
\iff
S-\delta_p\operatorname{Diag}(S)\ge0,
\tag{14}
\]

which proves (5). This is stronger than merely restating `G_p circ S>=0`: the special two-level local factor collapses the inverse-Schur condition to a single Loewner lower bound against the **observable diagonal of `S` itself**.

Notice that (14) already implies `S>=0`. Indeed its diagonal is

\[
(1-\delta_p)S_{aa}=r_pS_{aa}\ge0,
\tag{15}
\]

and

\[
S
=
\left(S-\delta_p\operatorname{Diag}(S)\right)
+
\delta_p\operatorname{Diag}(S)
\ge0.
\tag{16}
\]

Thus no separate PSD hypothesis is required in (5).

If some `S_{aa}=0`, (14) forces the corresponding row and column to vanish, and the criterion reduces to the positive-diagonal support. If all diagonal entries are positive, congruence by `D^{-1/2}` turns (14) into

\[
C-\delta_pI\ge0,
\tag{17}
\]

which proves (7).

The inverse map therefore fails positivity precisely by trying to subtract more diagonal floor than the target covariance actually contains. The rank-one witness `11^*` from `PL-420` is now transparent: its normalized correlation matrix has eigenvalues `(n,0,...,0)`, so its smallest eigenvalue is `0<1/n=1/(p-1)`.

## 3. Gram geometry: local insertion adds a private orthogonal component

The range criterion has an exact Hilbert-space realization. Suppose

\[
R_{ab}=\langle u_a,u_b\rangle.
\tag{18}
\]

Let `{e_a}` be an orthonormal family in a fresh orthogonal summand and define

\[
w_a
:=
\sqrt{r_p}\,u_a
\oplus
\sqrt{\delta_p}\,\|u_a\|e_a.
\tag{19}
\]

Then

\[
\langle w_a,w_b\rangle
=
\begin{cases}
\|u_a\|^2,&a=b,\\
r_p\langle u_a,u_b\rangle,&a\ne b,
\end{cases}
\tag{20}
\]

so

\[
\boxed{\operatorname{Gram}(w_a)=\Psi_p(R).}
\tag{21}
\]

Thus the normalized local factor acts geometrically by retaining a fraction `r_p` of the shared coherence and adding to each residue direction a mutually orthogonal private component of squared weight `delta_p`.

Conversely, a target Gram matrix `S` can be de-aliased while preserving positivity exactly when that private orthogonal floor can be removed. For normalized unit vectors with Gram matrix `C`, condition (7) says

\[
\left\|\sum_a z_av_a\right\|^2
\ge
\frac1{p-1}\sum_a|z_a|^2
\qquad
\text{for every }z\in\mathbb C^{p-1}.
\tag{22}
\]

So the surviving arithmetic cone is exactly a **lower-Riesz-bound cone**. At `p=5`, no linear combination of the four normalized residue vectors may lose more than a factor `1/4` of squared norm.

This formulation is materially different from generic PSD. Positive semidefiniteness only gives a lower bound `0`; exact local deletion needs the quantitative gap

\[
\lambda_{\min}(C)\ge1/4.
\tag{23}
\]

## 4. A direct cross-coherence target

Equation (7) can be attacked without reconstructing the inverse Schur map. Since

\[
C=I+(C-I),
\tag{24}
\]

a sufficient condition is

\[
\boxed{
\|C-I\|_{\mathrm{op}}
\le
1-\frac1{p-1}
=
\frac{p-2}{p-1}.
}
\tag{25}
\]

A still more elementary sufficient condition follows from Gershgorin:

\[
\max_a\sum_{b\ne a}|C_{ab}|
\le
\frac{p-2}{p-1}.
\tag{26}
\]

For `p=5`, either

\[
\|C-I\|_{\mathrm{op}}\le\frac34
\tag{27}
\]

or the row-wise bound

\[
\max_a\sum_{b\ne a}|C_{ab}|\le\frac34
\tag{28}
\]

is enough. In particular, the simple pairwise estimate

\[
|C_{ab}|\le\frac14
\qquad(a\ne b)
\tag{29}
\]

already suffices because there are three off-diagonal entries per row.

These are only sufficient conditions; the exact criterion is (7). Their value is analytic: they turn the abstract restricted-cone escape of `PL-420` into concrete **cross-residue decorrelation estimates**. A theorem giving `C=I+o(1)` in operator norm for the relevant actual-prime or zero-side matrix would eventually make exact local deletion positive. But if such a theorem is proved only under GRH, it cannot serve as an RH mechanism; the lower-frame estimate has to come from non-circular arithmetic input at the stage where it is used.

## 5. Relation to `PL-419` and the current source-transfer frontier

`PL-419` shows that retaining only the positive diagonal residue energies loses the off-diagonal information needed by the mod-5 signed supertrace. `PL-420` then shows that retaining the full matrix still does not make exact local deletion positive automatically. The present calculation identifies the exact missing quantitative statement.

Let `S_arith` denote whichever full residue covariance matrix is proposed to carry the ordinary `p=5` local factor through the source/zero transfer, and let

\[
C_{\rm arith}
=
\operatorname{Diag}(S_{\rm arith})^{-1/2}
S_{\rm arith}
\operatorname{Diag}(S_{\rm arith})^{-1/2}
\tag{30}
\]

on its positive diagonal support. Then

\[
\boxed{
G_5\circ S_{\rm arith}\ge0
\iff
\lambda_{\min}(C_{\rm arith})\ge\frac14.
}
\tag{31}
\]

The irrelevant positive scalar relating `G_5` to `Psi_5^{-1}` does not affect semidefinite order.

This means there is no longer a generic matrix-theory ambiguity about what an “arithmetic restricted cone” would have to be. Any successful positive route must prove that the actual matrices land inside the spectral-floor cone (31), or else use a different representation in which the source repair is not this inverse dephasing operation.

Crucially, (31) is a **matrix-level requirement**, not the scalar power-saving target of `PL-407`/`PL-415`. As `PL-418` already shows, a signed scalar source estimate does not imply the stronger coercivity needed for spectral reality. Here the same separation appears one step earlier: even the raw/full covariance needs a uniform lower-frame theorem before exact local-factor deletion preserves ordinary positivity.

## 6. Prior-art and novelty audit

The general matrix mechanisms are classical.

- The Schur product theorem and complete positivity of PSD Schur symbols are already audited in `PL-420`.
- Uniform damping of off-diagonal entries while preserving the diagonal is the standard Schur/dephasing-channel architecture. Modern quantum-information treatments explicitly call correlation-matrix Schur multipliers generalized dephasing or Hadamard channels.
- Linear shrinkage of covariance/correlation matrices toward a diagonal or identity target is classical; in particular Ledoit--Wolf study convex linear shrinkage toward the identity as a way to impose conditioning.

Targeted searches for the exact Hardy--Littlewood local-factor map did not locate prior art stating the arithmetic specialization (3)--(8). No novelty is claimed for dephasing channels, shrinkage estimators, Gershgorin, Gram matrices, or the elementary eigenvalue argument.

The durable line-specific result is the **exact range characterization forced by the prime-pair local factor**: after normalization, the local `p`-factor is the fixed shrinkage `R -> ((p-2)/(p-1))R+(1/(p-1))Diag(R)`, and positivity of exact deletion is equivalent to the normalized covariance having spectral floor `1/(p-1)`. This resolves the abstract restricted-cone question left by `PL-420` at the representation level without assuming that actual arithmetic data satisfy the condition.

## 7. Adversarial audit

1. **Range characterization is not range membership.** Equation (31) does not prove that the actual prime or zero correlation matrices satisfy the `1/4` floor. That is now the arithmetic theorem to be established or falsified.

2. **Normalization does not hide a sign assumption.** The positive overall factor `d_p` is removed only because positive scalar multiplication preserves semidefinite order. Zero diagonal entries are handled by restricting to the forced nonzero support, as noted after (16).

3. **The criterion is stronger than pairwise Cauchy--Schwarz.** Ordinary PSD gives `|C_ab|<=1` and `lambda_min(C)>=0`; neither yields the required `1/(p-1)` gap. The sufficient coherence bounds (25)--(29) are genuine extra input.

4. **No claim is made about the source-subtracted residual.** Even if the raw local-factor deletion lands in the positive cone, subtracting the Hardy--Littlewood model can destroy positivity, as `PL-418` shows. This finding characterizes only the local de-aliasing gate isolated in `PL-420`.

5. **No analytic continuation is used.** The derivation is finite-dimensional local-factor algebra. It neither assumes nor proves RH/GRH and does not continue an Euler product into the critical strip.

6. **The terminology is calibration, not discovery.** Calling (3) dephasing or shrinkage recognizes standard prior art; the mathematical content stored here is the exact arithmetic parameter and its spectral-floor consequence.

## Consequence for the line

The next positive-operator question after `PL-420` is no longer “perhaps actual arithmetic matrices occupy some favorable subcone.” The favorable cone is exactly known:

\[
\boxed{
C_{\rm arith}\ge\frac1{p-1}I.
}
\tag{32}
\]

At the live prime `p=5`, the required theorem is

\[
\boxed{
C_{\rm arith}\ge\frac14I.
}
\tag{33}
\]

Equivalently, the four normalized residue vectors must form a Riesz sequence with lower bound `1/4`. This is a much sharper research target than generic covariance positivity: it asks for quantitative independence of the residue channels strong enough to survive exact removal of the local Hardy--Littlewood factor.

A useful next audit is therefore analytic rather than representational: determine whether established prime/Dirichlet-`L` correlation estimates imply any non-circular lower-frame bound of this strength, or whether matched arithmetic controls can force `lambda_min(C_arith)` arbitrarily close to zero. Either outcome would materially settle the remaining positivity escape.