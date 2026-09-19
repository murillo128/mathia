# PC-362 — subcritical unbounded raising perturbations remain spectrally blind

- **Finding ID:** `PC-362`
- **Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE`
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact unbounded-operator / relative-bound obstruction
- **Scope:** extends PC-361 from bounded strictly grade-raising Prime-Circle signature terms to genuinely unbounded terms that are subcritical relative to the chosen proper grade Hamiltonian; ordinary eigenvalues remain completely fixed until the raising term crosses the compact-resolvent/graph-growth boundary or some other load-bearing hypothesis is broken
- **RH relevance:** high as a boundary result. Merely making the all-depth Prime-Circle signature operator unbounded does not escape the triangular spectral no-go. For the canonical number operator, every strictly raising signature term with relative bound below one is still eigenvalue-blind. Any surviving ordinary-spectrum route must therefore use critical/supercritical grade growth, nontriangular coupling, source-dependent domain data, or a different non-eigenvalue observable, and the normalization that makes a perturbation “large” must itself be geometry-forced rather than chosen as a spectral wrapper.

## Claim

PC-361 proves spectral blindness when the strictly grade-raising term is bounded on the Hilbert completion. Its main explicit escape hatch is an **unbounded signature perturbation**. That escape is too broad: a large natural class of unbounded raising terms is still spectrally invisible.

Let

\[
\mathcal H=\bigoplus_{m\ge 0}\mathcal H_m,
\qquad
0<\dim\mathcal H_m<\infty,
\]

and let

\[
H_0|_{\mathcal H_m}=\epsilon_m I,
\qquad
\epsilon_m\in\mathbb R,
\qquad
\epsilon_m\to+\infty,
\]

with

\[
\mathcal D(H_0)
=
\left\{x:\sum_m |\epsilon_m|^2\|x_m\|^2<\infty\right\}.
\]

Let \(Q:\mathcal D(H_0)\to\mathcal H\) be a possibly unbounded operator satisfying:

1. **strict raising on grade vectors**
   \[
   P_jQP_k=0\qquad (j\le k);
   \tag{1}
   \]
2. **subcritical \(H_0\)-relative bound:** there exist \(0\le a<1\) and \(b\ge0\) such that
   \[
   \|Qx\|
   \le
   a\|H_0x\|+b\|x\|,
   \qquad x\in\mathcal D(H_0).
   \tag{2}
   \]

For

\[
H=H_0+Q,
\qquad
\mathcal D(H)=\mathcal D(H_0),
\]

one has

\[
\boxed{\operatorname{Spec}(H)=\{\epsilon_m:m\ge0\}.}
\tag{3}
\]

For every distinct energy value \(\lambda\),

\[
\boxed{
\operatorname{algmult}_{H}(\lambda)
=
\sum_{m:\epsilon_m=\lambda}\dim\mathcal H_m.
}
\tag{4}
\]

Thus PC-361 does not stop at bounded \(Q\): the same eigenvalue rigidity persists for genuinely unbounded strictly raising data throughout the entire relative-bound-\(<1\) regime.

The hypothesis \(a<1\) is a **sufficient structural boundary, not a claimed universal sharp threshold**. An explicit weighted-shift family below shows that supercritical relative growth can in fact destroy all bare eigenvectors while the operator remains closed, so the restriction cannot simply be deleted.

## 1. Relative boundedness extends strict raising to the full domain

Equation (2) makes \(Q\) continuous from \(\mathcal D(H_0)\) with its graph norm into \(\mathcal H\).

For \(x\in\mathcal D(H_0)\), let

\[
x^{(M)}=\sum_{m\le M}P_mx.
\]

Because \(H_0\) is diagonal by grades,

\[
x^{(M)}\to x
\]

in the graph norm of \(H_0\). Hence

\[
Qx^{(M)}\to Qx.
\tag{5}
\]

Suppose \(m\) is the least grade with \(P_mx\ne0\). Every finite truncation \(x^{(M)}\) has no component below \(m\), and (1) gives

\[
P_mQx^{(M)}=0.
\]

Taking the limit in (5),

\[
\boxed{P_mQx=0.}
\tag{6}
\]

This graph-norm passage is load-bearing. For an unbounded \(Q\), strict triangularity on finite grade vectors alone would not justify applying the least-grade argument to an arbitrary vector in \(\mathcal D(H_0)\).

## 2. The whole homotopy keeps compact resolvent

A scalar shift of \(H_0\) changes neither the grading nor the spectral-rigidity question, and preserves the same relative coefficient \(a\) after changing only \(b\). We may therefore assume

\[
H_0\ge0.
\]

For \(R>0\), put

\[
K_R=Q(H_0+R)^{-1}.
\]

Using (2),

\[
\begin{aligned}
\|K_R\|
&\le
 a\|H_0(H_0+R)^{-1}\|
+b\|(H_0+R)^{-1}\|\\
&\le a+\frac bR.
\end{aligned}
\tag{7}
\]

Choose \(R\) so large that

\[
q:=a+\frac bR<1.
\tag{8}
\]

For the homotopy

\[
H_t=H_0+tQ,
\qquad 0\le t\le1,
\]

one then has the exact factorization

\[
H_t+R
=
\left(I+tK_R\right)(H_0+R).
\tag{9}
\]

Since \(\|tK_R\|\le q<1\), the first factor is boundedly invertible for every \(t\in[0,1]\). Therefore every \(H_t\) is closed on the common domain \(\mathcal D(H_0)\), \(-R\) is a common resolvent point, and

\[
(H_t+R)^{-1}
=
(H_0+R)^{-1}
(I+tK_R)^{-1}.
\tag{10}
\]

Because \(\epsilon_m\to+\infty\) and each grade is finite-dimensional, \((H_0+R)^{-1}\) is compact. Equation (10) then gives

\[
\boxed{H_t\text{ has compact resolvent for every }t\in[0,1].}
\tag{11}
\]

No standalone closedness assumption on \(Q\) is needed.

More generally, the proof only needs a common \(R\) for which \(Q(H_0+R)^{-1}\) is bounded with norm below one. Relative bound \(a<1\) is a transparent sufficient condition forced by graph growth rather than an extra spectral ansatz.

## 3. Strict raising still pins every eigenvalue to a bare grade

Let \(x\ne0\) satisfy

\[
H_tx=\lambda x.
\]

Choose the least \(m\) with \(P_mx\ne0\). By (6),

\[
P_mQx=0.
\]

Projecting the eigenvalue equation onto \(\mathcal H_m\) gives

\[
\epsilon_mP_mx=\lambda P_mx,
\]

hence

\[
\boxed{\lambda=\epsilon_m.}
\tag{12}
\]

Compact resolvent from (11) implies that every finite spectral point is an isolated eigenvalue of finite algebraic multiplicity. Therefore

\[
\operatorname{Spec}(H_t)
\subseteq
\{\epsilon_m:m\ge0\}
\qquad(0\le t\le1).
\tag{13}
\]

This is the same triangular obstruction as PC-361, but the graph-norm argument and the common compact-resolvent factorization are what make it survive an unbounded \(Q\).

## 4. Bare energies cannot disappear

Fix a distinct bare energy \(\lambda\). Since \(\epsilon_m\to+\infty\), it is isolated from the other distinct grade energies. Choose a small contour \(\Gamma_\lambda\) around it containing no other bare energy.

Equation (13) implies

\[
\Gamma_\lambda\subset\rho(H_t)
\qquad(0\le t\le1).
\]

For \(z\in\Gamma_\lambda\),

\[
H_t-z
=
\left(I+tQ(H_0-z)^{-1}\right)(H_0-z).
\tag{14}
\]

The operator \(Q(H_0-z)^{-1}\) is bounded by (2). Since both factors in (14) represent invertible operators for \(z\in\Gamma_\lambda\), the inverse depends norm-continuously on \(t\). Hence the Riesz projection

\[
\Pi_\lambda(t)
=
\frac{1}{2\pi i}
\int_{\Gamma_\lambda}(z-H_t)^{-1}\,dz
\tag{15}
\]

is norm-continuous in \(t\). Its finite rank is integer-valued and therefore constant on the connected interval \([0,1]\). At \(t=0\),

\[
\operatorname{rank}\Pi_\lambda(0)
=
\sum_{m:\epsilon_m=\lambda}\dim\mathcal H_m.
\]

The same rank holds at \(t=1\), proving (3)--(4).

Thus even an unbounded one-sided Prime-Circle signature can change eigenvectors, generalized eigenspaces, Riesz-projection conditioning and resolvent growth while leaving all ordinary eigenvalues and their algebraic multiplicities source-blind.

## 5. Sharpness control: a supercritical weighted shift loses every bare eigenvector

The relative-bound hypothesis is not a technical decoration. On

\[
\mathcal H=\ell^2(\mathbb N_0),
\qquad
Ne_n=ne_n,
\]

define the strictly raising weighted shift

\[
Q_ce_n=c(n+1)e_{n+1},
\qquad
\mathcal D(Q_c)=\mathcal D(N),
\tag{16}
\]

with \(c>0\).

Since

\[
Q_c=cS(N+I)
\]

for the unilateral shift \(S\),

\[
\|Q_cx\|
\le
c\|Nx\|+c\|x\|.
\tag{17}
\]

Testing on \(e_n\) shows that the optimal relative coefficient is exactly \(c\):

\[
\frac{\|Q_ce_n\|}{\|Ne_n\|}
=
c\frac{n+1}{n}
\longrightarrow c.
\tag{18}
\]

For \(0<c<1\), the theorem applies and

\[
\operatorname{Spec}(N+Q_c)=\mathbb N_0.
\]

The eigenvector at \(m\in\mathbb N_0\) has the explicit tail

\[
x_{m+k}
=
(-c)^k\binom{m+k}{k}x_m,
\tag{19}
\]

which is square-summable because a polynomial factor is dominated by \(c^k\).

For \(c>1\), set

\[
H_c=N+Q_c=(I+cS)N+cS.
\tag{20}
\]

The bounded operator \(I+cS\) is bounded below:

\[
\|(I+cS)x\|
\ge
(c-1)\|x\|.
\tag{21}
\]

A bounded-below left factor preserves closedness of a closed operator, so \((I+cS)N\) is closed; adding the bounded \(cS\) shows that \(H_c\) is closed on \(\mathcal D(N)\).

If \(H_cx=\lambda x\) with \(x\ne0\), the least occupied coordinate \(m\) forces \(\lambda=m\), and the recurrence is again (19). For \(c>1\), that tail cannot lie in \(\ell^2\). Hence

\[
\boxed{\sigma_p(H_c)=\varnothing\qquad(c>1).}
\tag{22}
\]

Nevertheless,

\[
(H_cx)_0=0
\]

for every \(x\in\mathcal D(N)\), so \(H_c\) is not onto at \(\lambda=0\). Therefore

\[
0\in\operatorname{Spec}(H_c)
\]

as a non-eigenvalue spectral point. The compact-resolvent/pure-point picture has genuinely failed.

Every finite truncation of \(H_c\) is triangular and still has eigenvalues \(0,1,\ldots,M\), for every \(c\). Thus this transition is an intrinsically infinite-depth/domain effect that no finite truncation can detect.

No universal claim is made at \(c=1\), and the example does not claim that every perturbation with relative bound at least one escapes isospectrality. It shows only that the subcritical hypothesis cannot be removed wholesale.

## 6. Prime-Circle consequence

PC-361 left “make the signature perturbation unbounded” as one of the live category changes. The present result narrows that route:

\[
\boxed{
\text{strictly raising }Q
+
\operatorname{relbd}_{H_0}(Q)<1
\Longrightarrow
\text{ordinary spectrum remains grade-only}.
}
\tag{23}
\]

For the canonical number operator \(N\), an unbounded all-depth Prime-Circle signature whose graph growth is subcritical relative to tensor degree therefore remains spectrally blind. The arithmetic data may survive strongly in nonnormal geometry, but not in the eigenvalue locations.

This also exposes a normalization trap. Relative size is measured against the chosen diagonal Hamiltonian. If the grade energies can be rescaled arbitrarily, multiplying \(H_0\) by a large scalar can make many fixed \(H_0\)-controlled perturbations formally subcritical. Therefore the threshold itself is **not** a new arithmetic invariant. Any RH-facing use of critical/supercritical growth must first justify the grade-energy normalization intrinsically from the roots-of-unity construction; otherwise it is another externally chosen spectral wrapper.

The ordinary-eigenvalue frontier is consequently narrower than PC-361 stated. A surviving mechanism must use at least one of:

- critical/supercritical raising growth for a geometry-forced grade Hamiltonian, with the resulting domain/resolvent transition controlled;
- same-grade, backward, or genuinely two-sided coupling;
- source-dependent boundary/domain conditions not reducible to a common graph-norm perturbation;
- a non-eigenvalue observable such as resolvent growth, pseudospectrum, semigroup behavior, or resonance data, followed by a fresh matched-control and zeta-destination audit.

Unboundedness by itself is not the category change.

## Prior-art and novelty audit

The functional-analysis ingredients are classical. Tosio Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, Classics in Mathematics (1995), DOI `10.1007/978-3-642-66282-9`, is the standard reference for relatively bounded perturbations, common-domain analytic families and Riesz-projection perturbation theory.

Unbounded triangular operator matrices are also an established subject. Qingmei Bai, Junjie Huang and Alatancang Chen, *Essential, Weyl and Browder spectra of unbounded upper triangular operator matrices*, **Linear and Multilinear Algebra** 64:8 (2016), 1583--1594, DOI `10.1080/03081087.2015.1111290`, study spectral inheritance for unbounded triangular matrices with diagonal domains. Abdelaziz Tajmouati, Abdeslam El Bakkali and Mohammed Karmouni, *On some local spectral theory and bounded local resolvent of operator matrices*, **Mathematica Bohemica** 143:2 (2018), 113--122, DOI `10.21136/MB.2017.0052-16`, treats local spectral questions for upper triangular operator matrices with unbounded entries.

No novelty is claimed for relative-bounded perturbation theory, Riesz projections, weighted shifts, or abstract triangular-operator spectral theory. I did not locate a source whose theorem is exactly the graded statement (3)--(4), but that absence is **not** a novelty claim. The line-local contribution is the exact closure of the specific escape left by PC-361: Prime-Circle all-depth signature data remain eigenvalue-blind even after becoming unbounded, provided their growth is subcritical relative to the fixed proper grading. The supercritical weighted-shift control identifies the genuine infinite-depth failure mode instead of treating all unboundedness as one category.

The proof above is self-contained; the cited literature is a novelty/prior-art boundary rather than a load-bearing theorem invocation, so no new `SOURCES.md` dependency is required.

## Falsification / disproof audit

- **Bounded limit:** if \(Q\) is bounded, its \(H_0\)-relative bound is zero, and the theorem reduces to PC-361.
- **Graph-domain check:** (5)--(6) is required before the least-grade argument. The proof does not silently extend algebraic triangularity from finite vectors to the domain.
- **Common-resolvent check:** the single estimate \(\|Q(H_0+R)^{-1}\|<1\) gives a common resolvent point for the entire homotopy and compactness through (10); compact resolvent is not assumed.
- **Repeated-energy check:** distinct grades may share an energy. Equation (15) preserves the total Riesz rank of the whole repeated-energy cluster, yielding exactly (4).
- **Infinite-depth check:** the \(Q_c\) family has identical finite-truncation eigenvalues on both sides of \(c=1\), while the closed infinite operator for \(c>1\) has no point spectrum. The obstruction is therefore genuinely topological/domain-sensitive.
- **Threshold check:** \(c>1\) gives a closed strict-raising counterfamily in which bare eigenvectors disappear, so “unbounded strict raising is always isospectral” is false. Conversely, no universal theorem is asserted for relative bound \(=1\) or \(>1\).
- **Normalization check:** the relative-bound threshold has no intrinsic arithmetic meaning unless the scale of \(H_0\) is itself forced by Prime-Circle geometry.
- **Directionality check:** adding a lowering channel, same-grade block, or source-dependent domain invalidates the proof and remains outside this no-go.
- **RH check:** neither the Riemann zeros, the critical line, the gamma factor nor the functional equation enters (3). Installing any of them directly into the grade energies would be an arbitrary spectral wrapper excluded by the research mandate.

## Boundary assessment

This is a decisive negative for the natural continuation

`Prime-Circle all-depth signature -> unbounded but subcritical one-sided raising term -> proper grade Hamiltonian -> compact-resolvent eigenvalue spectrum -> RH mechanism`.

The correct boundary after PC-361 is not bounded versus unbounded. It is whether the source-forced raising term remains graph-subcritical enough to preserve a common compact-resolvent homotopy. Below that boundary, ordinary eigenvalues are still completely determined by the externally chosen grade energies. Beyond it, the weighted-shift control shows that genuinely new infinite-depth spectral behavior can occur, but it is not automatically arithmetic and must be justified from the intrinsic roots-of-unity geometry.

## Artifact status

Single durable finding. No clue disposition, review response, `README.md`, `mind/**`, or `SOURCES.md` update is required.
