# PL-443 — Correlation normalization makes trace-matched Reynolds stationarization exactly the Hardy--Littlewood dephasing of the Frobenius stationary fit

**Evidence/status:** `EXACT-DERIVED + PRIOR-ART-AUDITED + REPRESENTATION-REFINEMENT + STRICT-CERTIFICATION-STRENGTHENING`.

**Parent findings:** `PL-421`, `PL-441`, `PL-442`.

## Claim

The `PL-421` local-factor image cone is invariant under positive diagonal congruence, while the raw covariance residuals used in `PL-442` are not. Passing first to the normalized correlation matrix removes this mismatch and exposes an exact compatibility between the zero-extension Reynolds construction and the Hardy--Littlewood dephasing coefficient.

Let `p` be an odd prime, put

\[
U_p=(\mathbb Z/p\mathbb Z)^\times,\qquad n=p-1,
\]

and let `S\succeq0` be a real symmetric covariance on `U_p` with strictly positive diagonal

\[
D=\operatorname{Diag}(S)>0.
\]

Define its correlation normalization

\[
C=D^{-1/2}SD^{-1/2},
\qquad \operatorname{Diag}(C)=I.
\tag{1}
\]

By `PL-421`, with

\[
\delta_p=\frac1{p-1},
\qquad
r_p=\frac{p-2}{p-1}=1-\delta_p,
\tag{2}
\]

the exact local-factor image condition is

\[
S-\delta_pD\succeq0
\iff
C-\delta_p I\succeq0.
\tag{3}
\]

Thus residue-wise positive rescaling is a gauge symmetry of the target cone.

For each nonzero additive lag `h mod p`, write

\[
L_h=\sum_{\substack{a\in U_p\\a+h\in U_p}} C_{a,a+h}.
\tag{4}
\]

There are exactly `p-2` directed pairs in (4). Let `F` be the Frobenius-best restricted lag-stationary fit to `C`. Then

\[
F_{aa}=1,
\qquad
F_{a,a+h}=\frac{L_h}{p-2}.
\tag{5}
\]

Now zero-extend `C` to `\mathbb Z/p\mathbb Z`, take the cyclic Reynolds average exactly as in `PL-442`, compress back to `U_p`, and multiply by the unique trace-matching factor `p/(p-1)`. Call the resulting unit-diagonal stationary matrix `H_R`. Its nonzero-lag coefficients are

\[
(H_R)_{a,a+h}=\frac{L_h}{p-1}.
\tag{6}
\]

Consequently

\[
\boxed{
H_R
=
\delta_p I+r_pF
=
\Psi_p(F),
}
\tag{7}
\]

where `\Psi_p(X)=r_pX+\delta_p\operatorname{Diag}(X)` is exactly the normalized Hardy--Littlewood local-factor insertion map from `PL-421`.

Equivalently,

\[
\boxed{
\Psi_p^{-1}(H_R)=F.
}
\tag{8}
\]

The same coefficient `r_p=(p-2)/(p-1)` therefore appears twice for the same finite-combinatorial reason: a nonzero translation orbit in the zero-extended `p`-cycle loses two endpoints, while the local Hardy--Littlewood factor attenuates off-diagonal residue coherence by exactly `r_p`.

At the live prime `p=5`, if

\[
U=C_{12}+C_{23}+C_{34},
\qquad
V=C_{13}+C_{14}+C_{24},
\tag{9}
\]

then

\[
F=T\!\left(1,\frac U3,\frac V3\right),
\qquad
H_R=T\!\left(1,\frac U4,\frac V4\right)
=
\frac14I+\frac34F,
\tag{10}
\]

and hence

\[
\boxed{
H_R-\frac14I=\frac34F.
}
\tag{11}
\]

So the trace-matched Reynolds surrogate lies in the `PL-421` image cone **if and only if the ordinary Frobenius stationary correlation fit is positive semidefinite**. The Reynolds construction is not merely a positivity-preserving averaging trick after correlation normalization: it is exactly local-factor dephasing applied to the stationary fit.

This identity also shows that fixing the Reynolds point is unnecessarily restrictive for perturbative certification. The entire stationary shrinkage segment between the identity and the Frobenius fit is explicit and can be optimized by one scalar quadratic.

No prime asymptotic, RH implication, or claim of new general Reynolds/correlation-matrix theory is contained in this finding.

## 1. Diagonal congruence is the natural gauge of the target cone

Equation (3) is a congruence identity:

\[
S-\delta_pD
=
D^{1/2}(C-\delta_p I)D^{1/2}.
\tag{12}
\]

Therefore the local-factor verdict is unchanged under arbitrary positive residue-wise rescaling

\[
S\longmapsto ASA,
\qquad
A=\operatorname{diag}(a_1,\ldots,a_{p-1}),
\quad a_j>0.
\tag{13}
\]

Indeed the normalized correlation matrix remains `C`.

This matters for stationarization. A raw Frobenius residual on `S` penalizes heterogeneity of the residue variances even though such heterogeneity is removable exactly by the target cone's own congruence symmetry. Correlation normalization removes that false direction before any stationary approximation is chosen.

The restriction to strictly positive diagonal is deliberate. If a diagonal entry vanishes, positive semidefiniteness forces the corresponding row and column to vanish, as already recorded in `PL-421`; the active support then has a different finite geometry and is not silently identified with the four-channel `p=5` problem.

## 2. Frobenius stationarization and trace-matched Reynolds differ by the local dephasing coefficient

For a fixed nonzero lag `h`, exactly two starting residues are forbidden in the zero extension: `a=0` and `a=-h`. Hence the restricted stationary Frobenius fit averages `p-2` entries, giving (5).

By contrast, the full cyclic Reynolds coefficient is the orbit average over all `p` positions,

\[
\frac{L_h}{p}.
\tag{14}
\]

The diagonal coefficient of that full average is `(p-1)/p`. Multiplying the compressed Reynolds matrix by `p/(p-1)` makes the diagonal equal to one and changes (14) to `L_h/(p-1)`, proving (6).

Combining (5)--(6),

\[
\frac{L_h}{p-1}
=
\frac{p-2}{p-1}\frac{L_h}{p-2}
=
r_pF_{a,a+h}.
\tag{15}
\]

The diagonal identity `1=\delta_p+r_p` completes (7).

This also explains a positivity fact implicit in `PL-442`. Since `H_R\succeq0` for every correlation input `C\succeq0`,

\[
\lambda_{\min}(F)\ge -\frac{\delta_p}{r_p}
=-\frac1{p-2}.
\tag{16}
\]

At `p=5`, every such Frobenius stationary correlation fit satisfies `\lambda_{\min}(F)\ge-1/3`, even though it need not itself be positive semidefinite.

Equation (11) is stronger for the live cone. It gives

\[
H_R-\frac14I\succeq0
\iff
F\succeq0,
\tag{17}
\]

and, on the strict branch,

\[
\lambda_{\min}\!\left(H_R-\frac14I\right)
=
\frac34\lambda_{\min}(F).
\tag{18}
\]

Thus the stationary margin of the normalized Reynolds surrogate is controlled by ordinary positivity of `F`, not by the stronger `1/4` dephasing floor for `F` itself.

## 3. The whole stationary shrinkage segment is exactly tractable

At `p=5`, write

\[
K=F-I,
\qquad
E=C-F.
\tag{19}
\]

Because `F` is the Frobenius orthogonal projection of `C` onto the restricted stationary subspace, `E\perp K` in Frobenius inner product. For

\[
H_\alpha=I+\alpha K,
\qquad 0\le\alpha\le1,
\tag{20}
\]

the identity, trace-matched Reynolds, and Frobenius stationary choices are respectively

\[
\alpha=0,
\qquad
\alpha=\frac34,
\qquad
\alpha=1.
\tag{21}
\]

Let

\[
\lambda=\lambda_{\min}(F),
\qquad
\varepsilon^2=\|C-F\|_F^2,
\qquad
\beta=\|F-I\|_F^2.
\tag{22}
\]

Then orthogonality gives the exact residual law

\[
\boxed{
\|C-H_\alpha\|_F^2
=
\varepsilon^2+(1-\alpha)^2\beta.
}
\tag{23}
\]

Since `I` commutes with `F`,

\[
\boxed{
\eta_\alpha
:=
\lambda_{\min}\!\left(H_\alpha-\frac14I\right)
=
\frac34+\alpha(\lambda-1).
}
\tag{24}
\]

Therefore every `\alpha` with `\eta_\alpha>0` supplies the rigorous transfer certificate

\[
\boxed{
\varepsilon^2+(1-\alpha)^2\beta
<
\eta_\alpha^2
\quad\Longrightarrow\quad
C-\frac14I\succ0.
}
\tag{25}
\]

The best Frobenius certificate on this segment is obtained by maximizing the explicit quadratic

\[
G(\alpha)
=
\left(\frac34+\alpha(\lambda-1)\right)^2
-
\varepsilon^2-(1-\alpha)^2\beta
\tag{26}
\]

over the interval where `0\le\alpha\le1` and `\eta_\alpha>0`. Hence the fixed Reynolds point `\alpha=3/4` is one admissible structural choice, not an optimization principle.

For the concrete mod-`5` coordinates (9),

\[
\boxed{
\varepsilon^2
=
\|C\|_F^2-4-\frac23(U^2+V^2),
}
\tag{27}
\]

and

\[
\boxed{
\beta
=
\frac23(U^2+V^2).
}
\tag{28}
\]

At the Reynolds point,

\[
\|C-H_R\|_F^2
=
\varepsilon^2+\frac1{16}\beta
=
\|C\|_F^2-4-\frac58(U^2+V^2),
\tag{29}
\]

recovering the exact cost of shrinking the Frobenius fit by `3/4`.

The remaining use of Frobenius norm in (25) is only sufficient:

\[
\|C-H_\alpha\|_{\rm op}
\le
\|C-H_\alpha\|_F.
\tag{30}
\]

Failure of (25) therefore does not imply failure of the true cone.

## 4. Two exact controls show why normalization and alpha-optimization matter

### Arbitrary diagonal heteroscedasticity

Let

\[
S=\operatorname{diag}(a_1,a_2,a_3,a_4),
\qquad a_j>0.
\tag{31}
\]

Then

\[
C=I,
\qquad
F=H_R=I,
\qquad
\varepsilon=\beta=0,
\qquad
\eta_\alpha=\frac34
\tag{32}
\]

for every `\alpha`. The correlation-normalized certificate is exact and insensitive to the variance imbalance, as the target cone itself must be.

By contrast, `PL-442` shows that its raw-covariance dephased-ray certificate on a diagonal covariance succeeds only when

\[
r_{\rm raw}
=
\frac{(\operatorname{tr}S)^2}{\|S\|_F^2}
>3.
\tag{33}
\]

For example,

\[
S=\operatorname{diag}(10,1,1,1)
\tag{34}
\]

has

\[
r_{\rm raw}=\frac{169}{103}<3.
\tag{35}
\]

The raw certificate therefore fails although the exact gate is trivially positive, while the normalized certificate has zero residual. This is a strict gain, not a change of the underlying cone.

### Exact stationary data

Take the stationary correlation matrix with common off-diagonal value

\[
C_t=(1-t)I+t\mathbf1\mathbf1^T,
\qquad t=\frac7{10}.
\tag{36}
\]

Here `F=C_t`, so `\varepsilon=0`. Its eigenvalues are `1+3t=31/10` and `1-t=3/10` with multiplicity three. Hence

\[
\lambda_{\min}\!\left(C_t-\frac14I\right)
=
\frac1{20}>0,
\tag{37}
\]

so the exact stationary gate passes.

The Frobenius endpoint `\alpha=1` certifies this with zero residual. The fixed Reynolds point `\alpha=3/4`, however, has

\[
\|C_t-H_{3/4}\|_F^2
=
\frac1{16}\|C_t-I\|_F^2
=
\frac{147}{400},
\tag{38}
\]

while

\[
\eta_{3/4}
=
\frac34\frac3{10}
=
\frac9{40},
\qquad
\eta_{3/4}^2
=
\frac{81}{1600}.
\tag{39}
\]

Thus the Reynolds Frobenius transfer test fails even though the covariance is **exactly stationary** and satisfies the target cone with positive margin. The shrinkage optimization (20)--(26) removes this artifact.

## 5. Prior art and novelty audit

The generic ingredients are classical.

- Converting a covariance matrix to a unit-diagonal positive-semidefinite correlation matrix by diagonal scaling is standard. The nearest-correlation-matrix literature, including Higham (2002), treats the unit-diagonal PSD cone as a classical structured matrix object.
- Frobenius-nearest circulant/structured approximations are classical; the Prime-Lattice source list already records Chan (1988) and Tyrtyshnikov (1992) as calibration for `PL-442`.
- Group/Reynolds averaging preserving positivity is standard finite-dimensional convexity/representation theory, and linear shrinkage toward the identity is classical covariance regularization.

No novelty is claimed for correlation matrices, diagonal congruence, Frobenius projection, Reynolds averaging, shrinkage, Weyl's inequality, or one-dimensional quadratic optimization.

The line-specific content is the exact compatibility (7)--(8): **after the exact `PL-421` correlation normalization, the trace-matched zero-extension Reynolds stationarization equals the Hardy--Littlewood local-factor dephasing map applied to the ordinary stationary Frobenius fit.** The equality uses the same arithmetic coefficient `(p-2)/(p-1)` on both sides and yields the explicit certification family (20)--(26). Targeted literature checks around nearest correlation matrices, circulant approximation, structured covariance, and periodic covariance extension did not locate this Hardy--Littlewood specialization.

This is a representation refinement, not evidence that the actual prime covariance satisfies the resulting bounds.

## 6. Boundaries and falsification conditions

1. **Positive diagonal is a real branch condition.** Correlation normalization requires the active residue variances to be positive. Vanishing channels must be reduced on their support rather than divided by zero.

2. **Normalization can magnify weak channels.** Even though diagonal congruence is exact algebraically, an arithmetic estimate for `C_{ab}=S_{ab}/\sqrt{S_{aa}S_{bb}}` requires quantitative lower control of the residue variances. A tiny diagonal entry can make normalized error estimates harder, not easier.

3. **The Frobenius fit need not be positive semidefinite.** That is not hidden by (20). If `\eta_1=\lambda-1/4>0`, positivity is automatic; otherwise `\alpha=1` is simply not a valid positive-margin transfer point. The segment permits retreat toward the identity or the Reynolds point.

4. **Reynolds remains structurally canonical, not certification-optimal.** Equation (7) explains why it preserves covariance positivity and how it matches the local dephasing coefficient. Equations (23)--(26) show that this does not make `\alpha=r_p` the best perturbative certificate.

5. **No arithmetic covariance theorem is supplied.** The remaining source task is to control the normalized stationary fit, its smallest eigenvalue, and the nonstationary correlation residual at covariance scale. Existing first-moment or almost-all progression theorems cannot be substituted for this.

6. **No RH consequence follows from the finite matrix identity alone.** The result sharpens one local-factor transport surface inside the existing program.

## Consequence for the line

The current mod-`5` theorem surface should distinguish three layers that were previously conflated.

First, use the `PL-421` diagonal congruence and work with the correlation matrix `C`, because the target cone itself is invariant under residue-wise positive rescaling. Second, form the Frobenius stationary correlation fit `F=T(1,U/3,V/3)`. Third, choose the shrinkage parameter `\alpha` by the exact scalar tradeoff (23)--(26), rather than fixing the zero-extension Reynolds value `3/4` before seeing the target margin.

The trace-matched Reynolds surrogate remains mathematically distinguished: it is exactly `\Psi_5(F)`, and its dephasing margin is `(3/4)\lambda_{\min}(F)`. But for certification it is one point on a larger target-aligned family. In particular, exact stationary data should use `\alpha=1`, while strongly uncertain stationary fits may benefit from shrinking toward the identity.

The unresolved number-theoretic question is now cleaner. One needs variance-scale control of the **normalized** residue correlations sufficient to bound `\lambda_{\min}(F)`, `\varepsilon`, and `\beta`; pure residue-variance imbalance should no longer consume the anisotropy budget. This does not lower the arithmetic difficulty automatically, but it removes a non-invariant obstruction from the finite-dimensional transfer geometry.
