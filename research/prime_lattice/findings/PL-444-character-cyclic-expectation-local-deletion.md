# PL-444 — Character-side cyclic expectation fixes the circulant sector and amplifies only noncirculant coherence under local-factor deletion

**Evidence/status:** \`EXACT-DERIVED + PRIOR-ART-AUDITED + REPRESENTATION-REFINEMENT + STRICT-CERTIFICATION-STRENGTHENING\`.

**Parent findings:** \`PL-421\`, \`PL-424\`, \`PL-443\`.

## Claim

The exact dephasing image cone of \`PL-421\` has a second normal form in the Dirichlet-character basis that separates **harmless cyclic coherence** from the genuinely dangerous noncyclic sector.

Let

\[
n=p-1,\qquad
\delta_p=\frac1n,\qquad
r_p=1-\delta_p=\frac{n-1}{n},
\]

let \(F\) be the unitary character table of \(U_p\), and write the residue covariance and character covariance as

\[
S=FKF^*.
\tag{1}
\]

Define the character-side cyclic conditional expectation

\[
\boxed{
\mathcal C(K)
:=
F^*\operatorname{Diag}(FKF^*)F.
}
\tag{2}
\]

After choosing a generator of the cyclic group \(U_p\) and ordering characters accordingly, \(\mathcal C\) is exactly the cyclic Reynolds projection

\[
\mathcal C(K)
=
\frac1n\sum_{j=0}^{n-1}U^jKU^{-j},
\tag{3}
\]

where \(U\) is the cyclic shift on the character indices. Equivalently, \(\mathcal C\) is the Frobenius-orthogonal conditional expectation onto the circulant matrix algebra. This algebraic definition is independent of the particular generator presentation: intrinsically it is \(F^*(\text{residue-diagonal algebra})F\).

Put

\[
K_{\mathrm{cyc}}=\mathcal C(K),
\qquad
K_\perp=K-\mathcal C(K).
\tag{4}
\]

Then exact local-factor deletion satisfies

\[
\boxed{
F^*\Psi_p^{-1}(S)F
=
K_{\mathrm{cyc}}
+
\frac1{r_p}K_\perp.
}
\tag{5}
\]

Thus deletion leaves the cyclic/conditional-expectation component **unchanged** and amplifies only the transverse component by

\[
\frac1{r_p}=\frac{p-1}{p-2}.
\]

At the live prime \(p=5\), the amplification is exactly \(4/3\).

Equivalently, the \`PL-421\` image-cone gate becomes

\[
\boxed{
S\in\Psi_p(M_n^+)
\iff
r_pK_{\mathrm{cyc}}+K_\perp\succeq0
\iff
K\succeq\delta_p\,\mathcal C(K).
}
\tag{6}
\]

Because \(\mathcal C\) is positive, \(K\succeq0\) implies \(K_{\mathrm{cyc}}\succeq0\). Hence **every positive character covariance already lying in the cyclic fixed-point algebra passes the local-factor gate automatically**, regardless of the size of its off-diagonal character coherences. Only the component transverse to that algebra can destroy positivity under deletion.

This strictly sharpens the earlier global coherence budget in \`PL-421\`: total off-diagonal character coherence is not the correct quantity to suppress.

## 1. Exact conditional-expectation normal form

The inverse dephasing map from \`PL-421\` is

\[
\Psi_p^{-1}(S)
=
\frac1{r_p}
\left(
S-\delta_p\operatorname{Diag}(S)
\right).
\tag{7}
\]

Conjugating by \(F\) and using (1)--(2),

\[
F^*\Psi_p^{-1}(S)F
=
\frac1{r_p}
\left(
K-\delta_p\mathcal C(K)
\right).
\tag{8}
\]

Since

\[
K=K_{\mathrm{cyc}}+K_\perp,
\]

and \(1-\delta_p=r_p\),

\[
K-\delta_p\mathcal C(K)
=
r_pK_{\mathrm{cyc}}+K_\perp.
\tag{9}
\]

Dividing by \(r_p\) gives (5), while positivity of (8) gives (6).

The interpretation is therefore exact rather than heuristic. Local-factor insertion in residue coordinates damps off-diagonal residue coherence. The inverse operation, viewed in character coordinates, does **not** amplify every character coherence uniformly. It fixes the component that is already compatible with residue-diagonal structure and amplifies only the complementary component.

This is the character-side counterpart of the representation refinements in \`PL-442\`--\`PL-443\`, but it is not their zero-extension Reynolds construction. Here no artificial residue is added: \(\mathcal C\) is intrinsic to the exact residue-diagonal term already appearing in the \`PL-421\` cone.

## 2. Relative lower-frame criterion

When \(K_{\mathrm{cyc}}\succ0\), (6) has the exact normalized form

\[
\boxed{
\lambda_{\min}
\left(
K_{\mathrm{cyc}}^{-1/2}
K
K_{\mathrm{cyc}}^{-1/2}
\right)
\ge
\delta_p.
}
\tag{10}
\]

Equivalently,

\[
\boxed{
\lambda_{\min}
\left(
K_{\mathrm{cyc}}^{-1/2}
K_\perp
K_{\mathrm{cyc}}^{-1/2}
\right)
\ge
-r_p.
}
\tag{11}
\]

Thus the local-factor gate is a lower-frame condition **relative to the covariance's own cyclic expectation**. A convenient sufficient condition is

\[
\boxed{
\left\|
K_{\mathrm{cyc}}^{-1/2}
K_\perp
K_{\mathrm{cyc}}^{-1/2}
\right\|_{\mathrm{op}}
\le r_p.
}
\tag{12}
\]

The unnormalized Weyl version is

\[
\boxed{
\|K_\perp\|_{\mathrm{op}}
\le
r_p\,\lambda_{\min}(K_{\mathrm{cyc}})
\quad\Longrightarrow\quad
S\in\Psi_p(M_n^+).
}
\tag{13}
\]

Equations (10)--(13) separate the theorem target into a **safe positive cyclic background** and a source-specific noncyclic defect. They do not require the whole character covariance to be close to diagonal.

Two previous exact slices are recovered immediately.

- If \(K\) is cyclic/circulant, then \(K_\perp=0\), so the gate is automatic.
- If \(K\) is diagonal, then
  \[
  K_{\mathrm{cyc}}=\frac{\operatorname{tr}K}{n}I,
  \]
  and (6) reduces exactly to the character-variance floor from \`PL-421\`,
  \[
  V_\chi\ge\frac{\operatorname{tr}K}{n^2}.
  \]

So the character-diagonal theorem is one boundary slice of a broader conditional-expectation geometry rather than the generic coherence model.

## 3. A strict control: large cyclic coherence is harmless

The distinction from the total-coherence sufficient bound in \`PL-421\` is not cosmetic.

At \(p=5\), let

\[
K_t=(1-t)I_4+t\mathbf1\mathbf1^*,
\qquad
0<t<1.
\tag{14}
\]

This is positive definite and circulant, with eigenvalues

\[
1+3t,\qquad 1-t,\qquad1-t,\qquad1-t.
\]

Therefore

\[
\mathcal C(K_t)=K_t,
\qquad
K_{\perp,t}=0,
\]

and the exact gate passes with

\[
K_t-\frac14\mathcal C(K_t)
=
\frac34K_t\succ0.
\tag{15}
\]

However, the robust bound (29c) of \`PL-421\` treats all off-diagonal character coherence as potentially dangerous. Here

\[
A_t=K_t-\operatorname{Diag}(K_t)
=t(\mathbf1\mathbf1^*-I_4),
\]

so

\[
\|A_t\|_{\mathrm{op}}=3t,
\qquad
\min_\chi\left(V_\chi-\frac{T}{16}\right)=\frac34.
\tag{16}
\]

That earlier bound requires

\[
\frac34\ge\frac54(3t),
\]

hence only \(t\le1/5\). At the explicit nondegenerate control \(t=1/2\), it fails by a factor \(5/2\):

\[
\frac34
<
\frac{15}{8},
\]

while (15) is strictly positive.

The lesson is exact: **large character coherence can be completely harmless when it belongs to the cyclic fixed-point algebra**. An arithmetic theorem aimed at suppressing \(\|K-\operatorname{Diag}K\|\) may therefore spend strength on a sector that local-factor deletion does not endanger.

## 4. A scalar noncyclic-energy obstruction

Because \(\mathcal C\) is the Frobenius-orthogonal projection onto the circulant algebra,

\[
\langle K_{\mathrm{cyc}},K_\perp\rangle_F=0.
\tag{17}
\]

The candidate positive preimage in character coordinates is

\[
\widehat R
=
K_{\mathrm{cyc}}+r_p^{-1}K_\perp.
\tag{18}
\]

Therefore

\[
\boxed{
\|\widehat R\|_F^2
=
\|K_{\mathrm{cyc}}\|_F^2
+
r_p^{-2}\|K_\perp\|_F^2.
}
\tag{19}
\]

The conditional expectation is trace preserving, so

\[
\operatorname{tr}\widehat R
=
\operatorname{tr}K
=:T.
\tag{20}
\]

If the exact gate passes, then \(\widehat R\succeq0\). Any positive matrix of trace \(T\) obeys \(\|\widehat R\|_F^2\le T^2\), giving the necessary scalar condition

\[
\boxed{
\|K_\perp\|_F^2
\le
r_p^2
\left(
T^2-\|K_{\mathrm{cyc}}\|_F^2
\right).
}
\tag{21}
\]

This is not sufficient, but unlike the marginal variance shadow it detects some purely coherent failures.

For the \`PL-424\` bad control

\[
K_{\mathrm{bad}}=vv^*,
\qquad
v=(1,i,1,-i)^T,
\]

the biunimodularity identity gives

\[
K_{\mathrm{cyc}}=I_4,
\qquad
\|K_\perp\|_F^2=12,
\qquad
T=4.
\tag{22}
\]

At \(p=5\), \(r_p=3/4\), so (21) would require

\[
12
\le
\frac9{16}(16-4)
=
\frac{27}{4},
\]

which is false. Equivalently,

\[
\|\widehat R\|_F^2
=
4+\frac{16}{9}\,12
=
\frac{76}{3}
>
16=T^2.
\tag{23}
\]

Thus the noncyclic-energy shadow already distinguishes the bad matched control from \(K_{\mathrm{good}}=I_4\), even though their four character variances and four residue variances are identical.

## 5. Prior art and novelty audit

The generic matrix operations used here are classical.

- Cyclic averaging / Reynolds projection onto the circulant algebra is standard finite-group averaging. Chan, Jin and Yeung (1991) study the circulant projection operator, including equivalent formulations and norm properties.
- Pinching and averaging onto matrix subalgebras are standard conditional-expectation operations; Bhatia (2000) is an audit-friendly matrix-analysis reference.
- The Frobenius-nearest circulant literature already recorded in the Prime-Lattice source ledger, including Chan (1988) and Tyrtyshnikov (1992), calibrates the structured-projection side.

No novelty is claimed for conditional expectations, circulant projection, Frobenius orthogonality, finite-group Reynolds averaging, or the generic relative-eigenvalue manipulation in (10).

The line-specific content is the exact arithmetic identification (5)--(6): the inverse Hardy--Littlewood local factor from \`PL-421\` acts in character coordinates as the identity on the cyclic conditional-expectation component and as multiplication by \((p-1)/(p-2)\) on the transverse component. That identity yields the relative lower-frame criterion (10), the strict safe-coherence control (14)--(16), and the noncyclic-energy obstruction (21).

A targeted prior-art audit around circulant projection, matrix pinching/averaging, covariance shrinkage, and conditional expectations found the generic machinery but no number-theoretic result supplying the actual-prime bound required by (10)--(13). The arithmetic estimate remains the unresolved part.

## 6. Boundaries and falsification conditions

1. **The cyclic algebra is representation-defined, not a new arithmetic symmetry theorem.** A generator of \(U_p\) makes it look circulant; intrinsically it is the character-side conjugate of the residue-diagonal algebra.

2. **This does not assert that the actual prime covariance is close to the cyclic algebra.** The exact decomposition identifies the defect that matters; it does not bound that defect.

3. **The relative normalization requires support care.** Equations (10)--(12) assume \(K_{\mathrm{cyc}}\succ0\). The unnormalized gate (6) remains valid without that hypothesis, and singular cases should be reduced on the active support rather than inverted blindly.

4. **The operator-norm bound is sufficient, not necessary.** The exact verdict is the lower generalized-eigenvalue condition (10), not the two-sided norm estimate (12).

5. **The Frobenius energy test is necessary, not sufficient.** Passing (21) does not imply positivity of the preimage.

6. **The \`PL-424\` obstruction remains load-bearing.** Marginal character variances still do not determine the noncyclic sector. The present result explains more precisely where that missing information lives.

7. **No unconditional prime covariance theorem or RH consequence is supplied.** Closing the route still requires source-scale control of the actual noncyclic character covariance relative to its cyclic expectation.

## Consequence for the line

The current character-side theorem target can be narrowed again.

It is unnecessarily strong to demand that the full mixed-character covariance be small, or even that all off-diagonal character coherences be small. The exact local-factor inverse tolerates arbitrary positive coherence inside the cyclic conditional-expectation algebra. What must be controlled is the **transverse noncyclic defect**

\[
K_\perp
=
K-\mathcal C(K)
\]

relative to the positive cyclic background \(\mathcal C(K)\).

A source theorem proving the one-sided relative floor (10), or the stronger but simpler estimate (12), would close the finite-dimensional local-factor gate without first diagonalizing the actual covariance. Conversely, any proposed scalar or norm estimate that spends its budget suppressing the safe cyclic component is quantitatively misaligned with the exact deletion geometry.

This does not reduce the required arithmetic scale: the bound must still hold for the actual centered fixed-modulus prime covariance at covariance strength. It does, however, remove another representation-induced overpayment from the theorem surface and isolates the character coherence that local-factor deletion genuinely amplifies.
