# WP-138 — New-prime puncture regular positive spectral responses cannot supply the critical logarithmic local scale

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + POSITIVE-SPECTRAL-SHIFT + MATCHED-COMPOSITE-CONTROL + PRIOR-ART-CLASSICALIZATION` for fixed regular monotone spectral responses of the exact one-hole positive defect classified by `PC-158`.

`PC-158` exposes a genuinely positive new-prime object that is not present in the repeated-prime analysis of `WP-134`--`WP-137`. For a fixed coarse modulus `d>=2`, put `r=phi(d)`. For every integer `m>=2` coprime to `d`, let `M_{d,m}` be the normalized inverse-square chord Laplacian on the complete semi-primitive `m`-fiber and let

\[
\widehat A_{d,m}=A_{d,m}^{\rm hole}\oplus0_r
\]

be the one-hole induced operator padded by the deleted section. When `m=q` is a new prime, the survivor is exactly `U(dq)`. `PC-158` proves

\[
0\preceq \widehat A_{d,m}\preceq M_{d,m}\preceq \frac18 I,
\qquad
K_{d,m}:=M_{d,m}-\widehat A_{d,m}\succeq0,
\tag{1}
\]

with exact trace-class budget

\[
\boxed{
\operatorname{Tr}K_{d,m}
=\frac r{12}
\left[
2\rho_d-\frac{\rho_d+d^{-2}}{m^2}
\right]
<\frac r6,
}
\qquad
\rho_d:=\prod_{p\mid d}\left(1-\frac1p-\frac1{p^2}\right).
\tag{2}
\]

The Loewner positivity in (1) is tempting for Weil positivity: it gives an intrinsic positive response to the geometric operation that removes the old section and, for prime fiber size, creates the true new primitive shell. But the same trace budget that makes the defect positive also makes every **fixed regular monotone spectral scalarization uniformly too small to provide the missing logarithmic prime scale**.

More precisely, if `f:[0,1/8]->R` is fixed, nondecreasing, and `L`-Lipschitz, define

\[
\Delta_f(d,m)
:=
\operatorname{Tr}f(M_{d,m})
-
\operatorname{Tr}f(\widehat A_{d,m}).
\tag{3}
\]

Then

\[
\boxed{
0\le \Delta_f(d,m)
\le L\operatorname{Tr}K_{d,m}
<\frac{Lr}{6}
}
\tag{4}
\]

for every admissible `m`. If `f` is operator monotone, the stronger operator inequality

\[
f(M_{d,m})-f(\widehat A_{d,m})\succeq0
\tag{5}
\]

also holds whenever the functional calculus is defined on the common spectral interval.

In particular, the canonical shifted logarithm

\[
f_\lambda(x)=\log(1+x/\lambda),\qquad \lambda>0,
\tag{6}
\]

is nonnegative, operator monotone, and `1/lambda`-Lipschitz. Hence the regularized log-determinant response is itself Loewner positive,

\[
Q_\lambda(d,m)
:=
\log(I+M_{d,m}/\lambda)
-
\log(I+\widehat A_{d,m}/\lambda)
\succeq0,
\tag{7}
\]

but obeys

\[
\boxed{
0\le\operatorname{Tr}Q_\lambda(d,m)
\le\frac{1}{\lambda}\operatorname{Tr}K_{d,m}
<\frac r{6\lambda}.
}
\tag{8}
\]

Thus a fixed positive spectral regularization cannot turn the new-prime puncture into a `log q` local response as `q` ranges through new primes. Combining it with the independently forced critical root-cover normalization of `WP-073` only sharpens the mismatch: for prime `q` not dividing `d`,

\[
\frac1{\sqrt q}\Delta_f(d,q)
=O_d(q^{-1/2}),
\tag{9}
\]

whereas the exact first-power finite Weil coefficient is

\[
\frac{\Lambda(q)}{\sqrt q}
=\frac{\log q}{\sqrt q}.
\tag{10}
\]

Consequently

\[
\boxed{
\frac{q^{-1/2}\Delta_f(d,q)}{(\log q)/\sqrt q}
\le\frac{Lr}{6\log q}
\longrightarrow0.
}
\tag{11}
\]

The puncture positivity therefore cannot supply the logarithmic factor missing from the canonical half-weight through any fixed regular monotone spectral response. This does not contradict `WP-073`, which obtains `Lambda(n)/sqrt(n)` from a different pointed boundary pairing; it rules out replacing that arithmetic boundary selector by the new positive puncture spectral shift.

## 1. Fixed monotone Lipschitz functional calculus inherits only the trace budget

Let

\[
\alpha_1\le\cdots\le\alpha_{rm},
\qquad
\beta_1\le\cdots\le\beta_{rm}
\]

be the eigenvalues of `widehat A_{d,m}` and `M_{d,m}`. From (1), finite-dimensional Weyl monotonicity gives

\[
\alpha_j\le\beta_j
\qquad(1\le j\le rm).
\tag{12}
\]

For a nondecreasing `L`-Lipschitz scalar function,

\[
0\le f(\beta_j)-f(\alpha_j)
\le L(\beta_j-\alpha_j).
\tag{13}
\]

Summing and using equality of dimensions gives

\[
\begin{aligned}
0\le\Delta_f(d,m)
&\le L\sum_{j=1}^{rm}(\beta_j-\alpha_j)\\
&=L\left(\operatorname{Tr}M_{d,m}-\operatorname{Tr}\widehat A_{d,m}\right)\\
&=L\operatorname{Tr}K_{d,m},
\end{aligned}
\tag{14}
\]

which is (4). No smoothness beyond Lipschitz continuity is needed. The statement is therefore not a peculiarity of traces of powers or of one chosen regularizer; it covers every fixed regular monotone scalar response on the whole normalized spectral interval.

Scalar monotonicity alone does **not** imply `f(M)-f(A)>=0` as an operator. The stronger claim (5) is made only for operator-monotone `f`. This distinction matters because the Weil-positivity mandate asks where the sign actually comes from rather than allowing an eigenvalue-ordering argument to be relabeled as operator positivity.

## 2. Shifted log-determinants remain positive but bounded

For every `lambda>0`, `x -> log(1+x/lambda)` is operator monotone on `[0,infinity)` and has derivative at most `1/lambda`. Equation (1) therefore gives (7), and applying (4) gives (8).

Equivalently,

\[
\operatorname{Tr}Q_\lambda(d,m)
=
\log\frac{\det(\lambda I+M_{d,m})}
{\det(\lambda I+\widehat A_{d,m})},
\tag{15}
\]

because the common dimension cancels the powers of `lambda`. This is a particularly strong control: unlike an arbitrary difference of positive quantities, the matrix difference in (7) is itself positive. Nevertheless its total mass is uniformly bounded in the new-prime degree.

Taking an outer logarithm of a bounded positive response, multiplying it by a hand-chosen `log m`, or choosing `lambda=lambda_m` after seeing the refinement can of course manufacture other scales. None of those operations inherits the fixed geometric positivity in (7). Such a construction would need a separate intrinsic theorem fixing the nonlinear scalarization or the `m`-dependent regularization before the arithmetic target is identified.

## 3. The zero-shift singular boundary is real but universal

The regularity assumption is essential. The unshifted Green/log-determinant boundary is singular because both graph Laplacians have zero modes.

All chord weights between distinct vertices are positive. Hence the ambient graph and the one-hole survivor are connected. Therefore

\[
\dim\ker M_{d,m}=1,
\qquad
\dim\ker A_{d,m}^{\rm hole}=1.
\tag{16}
\]

Padding the survivor by the `r` deleted coordinates gives

\[
\dim\ker\widehat A_{d,m}=r+1.
\tag{17}
\]

Writing `det'` for the product of nonzero eigenvalues and sending `lambda` to zero in (15) yields

\[
\boxed{
\operatorname{Tr}Q_\lambda(d,m)
=
r\log\frac1\lambda
+
\log\frac{\det' M_{d,m}}
{\det' A_{d,m}^{\rm hole}}
+o(1).
}
\tag{18}
\]

The divergent coefficient is exactly the number `r=phi(d)` of padded deleted coordinates and is **independent of the fiber degree `m`**. Thus the first way the bounded regular theorem can fail is a universal zero-mode divergence, not a prime-sensitive logarithm.

Equation (18) deliberately does not classify the finite pseudodeterminant ratio. A canonical finite-part theorem could in principle leave nontrivial `m`-dependence. But subtracting the universal `r log(1/lambda)` term no longer inherits the raw nonnegativity of (7), and choosing `lambda_m` so that the universal divergence itself becomes proportional to `log m` is a refinement-dependent regularization. Either escape therefore requires new geometric structure and a new sign argument; it is not supplied by the PC-158 puncture positivity alone.

## 4. Matched composite control removes the remaining arithmetic interpretation

The proof above did not use primality. `PC-158` establishes (1)--(2) for every integer `m>=2` coprime to `d` after deleting the same one-point section from each complete fiber. For prime `m=q`, that one-hole survivor happens to be the true primitive shell `U(dq)`; for composite `m`, it is a matched geometric control rather than the full primitive shell.

Hence every object entering (3)--(8)—Loewner order, trace-class budget, regular monotone spectral response, and shifted-log positivity—has the same smooth composite continuation. The positive mechanism knows that a section was deleted, not that the fiber degree was prime. Any prime-specific content must enter through the extra arithmetic fact that the one-hole survivor equals `U(dq)` only for a new prime, or through another selector/coupling not present in the positive spectral shift.

This control prevents a weaker interpretation of the result: even if a bounded response were numerically correlated with some prime quantity over a finite range, its sign theorem would still be a universal one-hole graph theorem rather than a finite-place arithmetic theorem.

## 5. Prior-art and novelty audit

The analytic ingredients of (12)--(18) are classical. Eigenvalue monotonicity for Hermitian matrices under Loewner order, Lipschitz control of ordered spectral sums, operator monotonicity of the logarithm, and zero-mode asymptotics of shifted determinants belong to standard finite-dimensional matrix/spectral-shift theory. A targeted audit against Weyl/min--max perturbation theory and Krein-style trace-formula literature therefore gives no basis for claiming a new general spectral theorem here.

The branch-specific contribution is the exact specialization to the new Mathia object supplied by `PC-158`: its one-hole defect is positive **and** has the explicit uniformly bounded trace budget (2). Combining those two facts with the canonical half-weight already forced in `WP-073` yields the sharp asymptotic mismatch (11). This is the new research boundary: the newest Prime-Circle positive defect cannot provide the required critical logarithmic local scale through any fixed regular monotone spectral calculus.

The result is also distinct from `WP-136` and `WP-137`. Those findings classify whole-spectrum scalarizations of **repeated-prime full cyclic fibers**, where refinement densifies a fixed Bloch pencil. Here the arithmetic event is a **new-prime puncture** of a complete fiber, and the obstruction comes from a bounded positive spectral-shift budget rather than Riemann-sum extensivity or endpoint harmonic poles.

## 6. Consequence for the global Weil-positivity search

The route

\[
\boxed{
\text{new-prime one-hole chord defect}
\to
\text{fixed regular monotone positive spectral response}
\to
\text{canonical }q^{-1/2}\text{ normalization}
\to
\frac{\log q}{\sqrt q}
}
\]

is ruled out. A viable use of the PC-158 positivity must leave at least one hypothesis of this theorem: use a genuinely singular zero-mode finite part with an independently fixed renormalization, use refinement-dependent or nonlinear spectral data justified before seeing the target coefficient, introduce the additional multi-hole arithmetic selector, couple several conductor levels nonseparably, or combine the finite and archimedean sectors before scalarization.

Even success on one of those escapes would still have to produce the Gamma and polar/global counterterms and prove the assembled Weil-type form nonnegative independently of RH or inserted zero data. The present finding supplies no such global positivity theorem; it materially narrows one newly available intrinsic positive Prime-Circle supplier.

### Internal evidence

- [PC-158](../../prime_circle/findings/PC-158-new-prime-puncture-is-a-prime-blind-positive-spectral-shift.md)
- [PC-157](../../prime_circle/findings/PC-157-new-prime-full-chord-bulk-collapses-to-a-fixed-bloch-limit.md)
- [WP-073](WP-073-pointed-dirichlet-root-cover-isometry-forces-critical-half-weight.md)
- [WP-136](WP-136-repeated-prime-full-chord-continuous-positive-spectral-traces-are-extensive.md)
- [WP-137](WP-137-repeated-prime-full-chord-green-trace-is-harmonic-logarithmic-not-exact-mangoldt.md)
