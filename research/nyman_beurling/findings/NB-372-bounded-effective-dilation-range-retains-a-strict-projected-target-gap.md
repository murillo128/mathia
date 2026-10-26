# NB-372 — Bounded effective dilation range retains a strict projected-target gap

- **Status:** proved (classical ingredients plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the continuous Nyman projection; NB-371 for the separate coefficient-budget boundary
- **Classification:** LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-SUPPORT-CLOSURE

## Claim and scope

Increasing coefficients and the number of columns cannot compensate for a fixed upper bound on the **effective dilation** \(av\). This remains true for approximation of the unconditional projected target, so the obstruction is an excess above the Burnol floor, not merely that floor itself.

Use
\[
H=L^2(0,1;dx),\qquad e=1,\qquad
g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad v>1,
\]
\[
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad a\ge1,
\qquad \mathcal N=\overline{\operatorname{span}}\{g_v:v>1\}.
\]
Let \(t=P_{\mathcal N}e\). With the normalization of NB-354,
\[
\mathcal Mt(s)=\frac{bB(s)}s,\qquad b=B(1)>0,
\qquad \|e-t\|^2=1-b^2,
\tag{1}
\]
where \(B\) is the common inner factor on \(\Re s>1/2\).

For every finite \(R>1\), define the closed space
\[
\mathcal W_R=
\overline{\operatorname{span}}
\{A_ag_v:a\ge1,\ v>1,\ av\le R\}.
\tag{2}
\]
There is no bound on coefficients or column count, including along sequences used to take this closure. Then
\[
\boxed{\Delta_R:=\operatorname{dist}(t,\mathcal W_R)>0,\qquad
\operatorname{dist}(e,\mathcal W_R)^2=1-b^2+\Delta_R^2.}
\tag{3}
\]
Nevertheless \(\Delta_R\to0\) as \(R\to\infty\). Thus every sequence of finite actual-generator sums approaching \(t\) must have its maximal effective dilation tending to infinity. For a fixed finite seed family this forces the maximal dilation \(a\) itself to tend to infinity. If seed indices may grow, only the product \(av\) is constrained.

The result supplies no rate for \(\Delta_R\), no effective upper synthesis, and no implication that \(b=1\). The central issue is passing the source-support restriction through Hilbert closure despite unrestricted cancellation of coefficients.

## 1. Recover the source locally by Möbius inversion

Work in logarithmic time using the unitary map
\[
(Uf)(u)=e^{-u/2}f(e^{-u}),\qquad u\ge0,
\]
and extend its output by zero to \(u<0\). The isometry \(A_a\) becomes right translation by \(\log a\).

Introduce the locally integrable causal kernel and two locally finite measures
\[
k(u)=e^{-u/2}\lfloor e^u\rfloor\mathbf1_{u\ge0},\qquad
Z=\sum_{n\ge1}n^{-1/2}\delta_{\log n},\qquad
M=\sum_{n\ge1}\mu(n)n^{-1/2}\delta_{\log n}.
\tag{4}
\]
Here \(\mu\) is the Möbius function. All convolutions below are between distributions supported in \([0,\infty)\); on each compact time interval only finitely many atoms of \(Z,M\) contribute. In particular, these identities require no boundary convergence of a Dirichlet series.

Writing \(D=d/du\) for distributional differentiation, the jumps of \(k\), including its jump at zero, give
\[
(D+1/2)k=Z,\qquad M*Z=\delta_0.
\tag{5}
\]
The second identity is the finite divisor identity

\[
[\delta_{\log n}](M*Z)
=n^{-1/2}\sum_{d\mid n}\mu(d)
=\mathbf1_{n=1}.
\]

For any \(h\in L^2(0,\infty)\), define its inverse source as a distribution
\[
\mathscr I h:=M*(D+1/2)h.
\tag{6}
\]
This map is continuous from the Hilbert norm to distributions on each compact interval. Indeed, differentiation is continuous from \(L^2_{\rm loc}\) to distributions, and each compact test involves only finitely many fixed translates. It need not be a bounded operator into a global Hilbert space or into finite measures.

The floor-function cancellation is exact:
\[
Ug_v(u)=v^{-1}k(u)-v^{-1/2}k(u-\log v).
\tag{7}
\]
Consequently every finite synthesis has the recovered source
\[
\mathscr I U\!\left(\sum_{\nu=1}^Jc_\nu A_{a_\nu}g_{v_\nu}\right)
=\sum_{\nu=1}^Jc_\nu
\left(v_\nu^{-1}\delta_{\log a_\nu}
-v_\nu^{-1/2}\delta_{\log(a_\nu v_\nu)}\right).
\tag{8}
\]
The square-root weights in this formula come from the unitary logarithmic normalization. They cannot be dropped.

If every \(a_\nu v_\nu\le R\), the distribution (8) is supported in \([0,\log R]\). Support in this fixed closed interval is preserved by distributional convergence. Hence
\[
\boxed{w\in\mathcal W_R\quad\Longrightarrow\quad
\operatorname{supp}(\mathscr I Uw)\subseteq[0,\log R].}
\tag{9}
\]
This includes limits with colliding parameters and arbitrarily large coefficients: the limiting source can be a distribution, rather than a finite measure. Assuming a bounded coefficient measure here would lose the main conclusion.

## 2. The projected target cannot have a compact inverse source

Suppose, for contradiction, that \(\nu_t:=\mathscr I Ut\) has compact support. Its transform
\[
E(s)=\langle\nu_t(u),e^{-(s-1/2)u}\rangle
\tag{10}
\]
is entire. For a compactly supported distribution this follows directly by differentiating the exponential against the distribution on its compact support; no converse Paley--Wiener theorem is needed.

For \(\Re s>1\), the series for \(M\) is absolutely convergent after exponential weighting, and the zero-extended distributional derivative in (6) has multiplier \(s\). Thus
\[
E(s)=\frac{s\mathcal Mt(s)}{\zeta(s)}
=\frac{bB(s)}{\zeta(s)}.
\tag{11}
\]
For completeness, exponential weighting of \(Ut\in L^2\) makes its Laplace integral absolutely convergent; the sum of absolute measure weights is \(\sum n^{-\Re s}<\infty\). These facts justify the convolution-transform product in this half-plane. No reciprocal-zeta series is asserted to converge on the critical line.

The identity theorem extends
\[
\zeta(s)E(s)=bB(s)
\tag{12}
\]
through \(\Re s>1/2\), with the possible singularity at \(s=1\) removable. Take almost-everywhere boundary values. Since \(B\) is inner,
\[
|\zeta(1/2+iy)E(1/2+iy)|=b
\quad\text{for almost every real }y.
\tag{13}
\]
The left side is continuous in \(y\), so it must equal \(b\) everywhere. At any critical-line zero of zeta it is zero, contradicting \(b>0\). Existence of such zeros is unconditional; neither simplicity nor RH is used.

Therefore \(\nu_t\) is not compactly supported. Equation (9) implies \(t\notin\mathcal W_R\). Since \(\mathcal W_R\) is closed, its distance from \(t\) is strictly positive.

This argument does not evaluate a generic Hardy function at a boundary point. The continuous object in (13) is the product of zeta with the hypothetical **entire compact-source transform**. Only the almost-everywhere modulus of \(B\) is used; analytic continuation of \(B\) across a boundary zero is unnecessary.

Finally,
\[
A_ag_v=\sqrt a\,(g_{av}-v^{-1}g_a),\qquad g_1=0,
\tag{14}
\]
so
\[
\mathcal W_R=\overline{\operatorname{span}}\{g_v:1<v\le R\}
\subseteq\mathcal N.
\tag{15}
\]
Orthogonality of \(e-t\) to \(\mathcal N\) proves (3). The increasing union of these spaces is dense in \(\mathcal N\), proving \(\Delta_R\to0\). This is fully compatible with every finite \(\Delta_R\) being positive.

## 3. Bounded dual certificates for each fixed range

The support proof also gives genuine Hilbert duals, rather than a boundary-point functional. Set \(T=\log R\). Because \(\nu_t\) is causal and not compactly supported, there is a test function \(\varphi\in C_c^\infty((T,\infty))\) with
\(\nu_t(\overline\varphi)\ne0\). Choose \(L>T\) above its support and put
\[
\psi_\varphi(u)=
\sum_{n\le e^L}\frac{\mu(n)}{\sqrt n}
\left[-\varphi'(u+\log n)+\frac12\varphi(u+\log n)\right],
\qquad u\ge0.
\tag{16}
\]
This is a finite sum in \(L^2(0,\infty)\), supported in \([0,L]\). Distributional integration by parts gives, with the inner product linear in the first argument,
\[
\langle Uh,\psi_\varphi\rangle
=(\mathscr I Uh)(\overline\varphi)
\qquad(h\in H).
\tag{17}
\]
It vanishes for every \(h\in\mathcal W_R\), by (9), but not for \(h=t\). Therefore
\[
\boxed{\Delta_R\ge
\frac{|\nu_t(\overline\varphi)|}{\|\psi_\varphi\|_2}>0.}
\tag{18}
\]
For example the elementary norm estimate
\[
\|\psi_\varphi\|_2
\le2e^{L/2}\|{-\varphi'+\varphi/2}\|_{L^2(\mathbb R)}
\tag{19}
\]
follows by the triangle inequality and \(\sum_{n\le X}n^{-1/2}\le2\sqrt X\).

The nonzero test in (18) is existential. Its choice and response depend on the actual projected target, hence on \(B\). Equations (16)--(19) do not provide an effective source-only estimate uniform in \(R\).

## Controls, prior art, and consequence

Under RH, \(t=e\), and the inverse source is simply
\[
\mathscr I Ue=M,
\tag{20}
\]
since \((D+1/2)(e^{-u/2}\mathbf1_{u\ge0})=\delta_0\). Its support is unbounded because there are arbitrarily large squarefree integers. This verifies the sign, boundary atom, and compact-support obstruction in a direct control. The general proof retains the unknown inner factor and does not assume this simplification.

The cutoff conclusion is independent of NB-371's fixed absolute-coefficient budget: (3) allows that budget to be unbounded. Together they require divergent coefficients and divergent effective range along convergent finite syntheses. Neither result quantifies the column count without an additional condition. A zero coefficient, a redundant column, or a rescaling of the chosen atoms does not affect the range-space statement (2). There is no claim that every strict increase of \(R\) strictly decreases \(\Delta_R\).

Burnol's *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2, equation (2.3) and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies the Mellin factor and target projection (1). Hardy's critical-line zero theorem is the classical input recorded in Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*, second edition, [Section 10.2](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf), also used by NB-371.

Burnol's *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, [Theorem 1.3](https://arxiv.org/pdf/math/0103058), is the closest cutoff-rate comparison. It bounds distance from the original indicator in the \(L^2(0,\infty)\) fractional-part formulation. Its displayed bound becomes trivial when the limiting distance is positive; it cannot simply be subtracted from that positive floor to obtain a bound on \(\Delta_R\). The present conclusion is qualitative strict excess above the continuous projected-target floor in \(L^2(0,1)\), not an improvement of Burnol's logarithmic rate.

Jousse, *Étude d'un problème de continuité lié à l'hypothèse de Riemann*, Ann. Inst. Fourier 55 (2005), 1373--1410, [Sections 4.2--4.3](https://www.numdam.org/item/10.5802/aif.2127.pdf), treats projection continuity and approximation with a fixed number of variable dilates, including an anchored variant. Those finite-count results must be distinguished from the fixed-range closure here, which allows unbounded count and uses the distributional source limit.

The mechanism is classical local Möbius convolution inversion, closed support, and entire transforms of compact distributions. No new general support theorem or bibliographic priority is claimed. The line-local delta is that finite-range source synthesis cannot attain the full projected target even with unrestricted coefficient blowup. NB-354's full-orbit closure and NB-371's coefficient obstruction alone do not establish this closed-range exclusion. The earlier compact-time defect spaces of NB-058--NB-061 concern a different object: physical/deflated orthogonal defects, not the inverse source (6).

Evidence is the analytic proof, with exact rational checks of (14) and finite divisor checks of (5) used only as normalization controls. No numerical distance, matching upper rate, Lean verification, independent adversarial approval, or RH advance is asserted. A consequential falsification would require failure of local distributional continuity in (6), the source support in (8), or the retained target modulus in (13).
