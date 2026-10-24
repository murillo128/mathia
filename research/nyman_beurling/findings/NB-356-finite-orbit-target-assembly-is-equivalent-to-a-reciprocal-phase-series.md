# NB-356 — Finite-orbit target assembly is equivalent to a reciprocal phase series

- **Status:** proved (literature theorem plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the exact orbit spaces and target projection; NB-355 for the two-orbit obstruction and scalar weighted-return bound
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-MEMBERSHIP + NEGATIVE/OBSTRUCTION

## Claim and scope

There is an exact summability test for assembling the projected Nyman target from finitely many closed real-dilation seed spaces. The test is sufficient as well as necessary: interpolation on one seed's zero lattice supplies the missing reverse implication. It shows that adding any fixed finite number of seeds whose logarithms still have rational rank two cannot remove NB-355's physical-norm obstruction. Seed count alone is not the relevant distinction.

In \(H=L^2(0,1;dx)\), put
\[
e(x)=1,\quad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\quad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_j=\overline{\operatorname{span}}\{A_ag_j:a\ge1\text{ real}\}.
\]
Let \(J\subset\mathbb N_{\ge2}\) be finite with at least two elements, choose \(q\in J\), and write \(J'=J\setminus\{q\}\). Let \(\mathcal N\) be the full continuous Nyman space, \(t=P_{\mathcal N}e\), and \(b=B(1)>0\), where \(B\) is its zeta-zero inner factor. Set
\[
L=\log q,\quad \tau=2\pi/L,\quad s_\ell=1+i\tau\ell,\quad
\alpha_j=\frac{\log j}{\log q},\qquad
\mathfrak S_{J,q}=\sum_{\ell=1}^{\infty}
\frac{1}{\ell^2\sum_{j\in J'}\|\ell\alpha_j\|_{\mathbb R/\mathbb Z}^2}.
\tag{1}
\]
A zero denominator means an infinite summand. Then
\[
\boxed{t\in\sum_{j\in J}\mathcal C_j
\quad\Longleftrightarrow\quad \mathfrak S_{J,q}<\infty.}
\tag{2}
\]
The sum of subspaces in (2) is the **algebraic sum**: one finite-norm vector from each closed orbit space. It is not their closed span, nor a finite sum of actual dilation generators.

If
\[
\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}\{\log j:j\in J\}=2,
\tag{3}
\]
then \(\mathfrak S_{J,q}=\infty\), although NB-354 gives \(\overline{\sum_j\mathcal C_j}=\mathcal N\). Moreover, for every decomposition \(w=\sum_j u_j\), \(u_j\in\mathcal C_j\), with \(\varepsilon=\|t-w\|\) sufficiently small and positive,
\[
\boxed{\sum_{j\ne q}\|u_j\|^2\ge c_{J,q,b}\log(1/\varepsilon)-O_{J,q,b}(1),
\qquad c_{J,q,b}>0.}
\tag{4}
\]
Thus a finite collection such as \(\{2,3,6,12,18\}\) still requires divergent total component energy near the optimal target distance. This does not assert divergence of every individual component in a family of three or more seeds.

## 1. Transport the physical target and norm

Use the unitary Mellin map to \(H^2(\Re s>1/2)\), with boundary norm \((2\pi)^{-1}\int|F(1/2+iy)|^2dy\). NB-354 gives
\[
\mathcal M\mathcal C_j=B\Theta_jH^2,\quad
\Theta_j(s)=\frac{s}{s-1}\frac1{\sqrt j}
\frac{1-j^{1-s}}{1-j^{-s}},\quad
\mathcal Mt(s)=\frac{bB(s)}s.
\tag{5}
\]
Each \(\Theta_j\) is a pure Blaschke product with simple zeros \(1+2\pi i\ell/\log j\), \(\ell\ne0\). Its apparent singularity at \(s=1\) is removable and nonzero.

Writing \(\mathcal Mu_j=B\Theta_jU_j\) gives \(\|u_j\|=\|U_j\|\). Therefore (2) asks whether
\[
f(s):=b/s=\sum_{j\in J}\Theta_j(s)U_j(s),\qquad U_j\in H^2.
\tag{6}
\]
Division by \(B\) takes place only on its invariant range and is isometric there. In particular, no lower bound for \(|B(s)|\) is assumed. For an approximate decomposition,
\[
\|e-w\|^2=1-b^2+\|t-w\|^2.
\tag{7}
\]
All assertions concern the actual best target projection unconditionally; under RH, and only then, \(t=e\).

## 2. The lattice sampler is onto, with explicit bounds

For every \(F\in H^2\), the sampling inequality proved in NB-355 is
\[
\sum_{\ell\in\mathbb Z}|F(s_\ell)|^2\le C_q\|F\|^2,
\qquad C_q=\frac{L}{1-q^{-1}}.
\tag{8}
\]
Briefly, write \(F(s)=\int_0^\infty h(v)e^{-(s-1/2)v}dv\) and periodize
\(P(v)=\sum_{k\ge0}h(v+kL)e^{-(v+kL)/2}\) on \([0,L)\). Cauchy--Schwarz bounds its squared norm by \((1-q^{-1})^{-1}\|h\|^2\), and Fourier Parseval supplies the factor \(L\) in (8).

Conversely, for arbitrary \(d=(d_\ell)_{\ell\in\mathbb Z}\in\ell^2\), define in \(L^2(0,L)\)
\[
P_d(v)=\frac1L\sum_{\ell\in\mathbb Z}d_\ell e^{i\tau\ell v},\qquad
h_d(v)=e^{v/2}P_d(v)\mathbf1_{[0,L)}(v).
\]
Its Laplace transform \(R_qd\) belongs to \(H^2\) and satisfies
\[
(R_qd)(s_\ell)=d_\ell,\qquad
\|R_qd\|^2=\int_0^L e^v|P_d(v)|^2dv
\le\frac qL\sum_\ell|d_\ell|^2.
\tag{9}
\]
All Fourier identities hold in \(L^2\); on this finite interval the defining integrals are legitimate by Cauchy--Schwarz. Thus every square-summable lattice datum has a bounded linear Hardy lift. For data specified only at \(\ell\ne0\), set \(d_0=0\). The value at \(s_0=1\) imposes no divisibility condition because it is not a zero of \(\Theta_q\).

## 3. Necessary and sufficient weighted sample condition

Set, for \(\ell\ne0\),
\[
a_\ell=\sum_{j\in J'}|\Theta_j(s_\ell)|^2,\qquad
T_{J,q}=\sum_{\ell\ne0}\frac{|f(s_\ell)|^2}{a_\ell}.
\tag{10}
\]
If (6) holds, its restriction to the zeros of \(\Theta_q\) and Cauchy--Schwarz give
\[
\frac{|f(s_\ell)|^2}{a_\ell}\le\sum_{j\in J'}|U_j(s_\ell)|^2.
\]
When \(a_\ell=0\), (6) is impossible since \(f(s_\ell)\ne0\). Otherwise summing and applying (8) proves
\[
T_{J,q}\le C_q\sum_{j\in J'}\|u_j\|^2.
\tag{11}
\]

For sufficiency assume \(T_{J,q}<\infty\). Choose the minimum Euclidean-norm solution at each lattice point:
\[
d_{j,\ell}=\frac{f(s_\ell)\overline{\Theta_j(s_\ell)}}{a_\ell}
\quad(j\in J',\ \ell\ne0),\qquad d_{j,0}=0.
\tag{12}
\]
Then \(\sum_j\Theta_j(s_\ell)d_{j,\ell}=f(s_\ell)\) and
\(\sum_{j,\ell}|d_{j,\ell}|^2=T_{J,q}\). Use (9) to construct \(U_j=R_qd_j\), so
\[
\sum_{j\in J'}\|U_j\|^2\le(q/L)T_{J,q}.
\tag{13}
\]
The Hardy function \(F=f-\sum_{j\in J'}\Theta_jU_j\) vanishes at every zero of \(\Theta_q\). Because that inner function is exactly the simple-zero Blaschke product for this lattice, Hardy factorization gives \(F/\Theta_q\in H^2\). Set \(U_q=F/\Theta_q\); this proves (6). In particular,
\[
\|U_q\|=\|F\|\le b+\sqrt{|J'|qT_{J,q}/L}<\infty.
\tag{14}
\]
No interpolation condition at a zeta zero or bounded analytic corona inverse was inserted.

Finally, putting \(\delta_{j,\ell}=\|\ell\alpha_j\|_{\mathbb R/\mathbb Z}\), the explicit factors give
\[
|\Theta_j(s_\ell)|=
\frac{|s_\ell|}{\tau|\ell|\sqrt j}
\frac{|1-e^{-2\pi i\ell\alpha_j}|}{|1-j^{-1}e^{-2\pi i\ell\alpha_j}|}
\asymp_{j,q}\delta_{j,\ell}.
\tag{15}
\]
Indeed \(4\delta\le|1-e^{2\pi i\delta}|\le2\pi\delta\), the denominator lies between \(1-j^{-1}\) and \(1+j^{-1}\), and \(|s_\ell|/(\tau|\ell|)\) is bounded above and below. Also \(|f(s_\ell)|\asymp_{q,b}1/|\ell|\). Thus \(T_{J,q}<\infty\) is equivalent to (1), proving (2).

When finite, the minimum non-\(q\) component cost \(E_{J,q}\), defined as the infimum of \(\sum_{j\in J'}\|u_j\|^2\) over exact decompositions of \(t\), obeys
\[
\boxed{C_q^{-1}T_{J,q}\le E_{J,q}\le(q/L)T_{J,q}.}
\tag{16}
\]
These constants need not be optimal. Finiteness of (1) is independent of which member \(q\) is chosen, because (2) identifies it with the same physical membership question.

## 4. Every fixed family of logarithmic rank two still loses the target

Assume (3). Choose \(p\in J\) with \(\alpha=\log p/\log q\) irrational. Clearing the finitely many rational denominators gives integers \(D\ge1,A_j,B_j\) such that
\[
D\alpha_j=A_j+B_j\alpha\qquad(j\in J').
\tag{17}
\]
At least one \(B_j\ne0\). On the sublattice \(\ell=Dn\),
\[
\|Dn\alpha_j\|=\|B_jn\alpha\|\le |B_j|\,\|n\alpha\|.
\tag{18}
\]
Consequently (1) dominates a positive constant times
\(\sum_n(n^2\|n\alpha\|^2)^{-1}\), which diverges by the weighted Dirichlet bound below. This proves exclusion of \(t\) for every such finite family, not merely the two-seed case.

For the quantitative version, write \(r=f-\sum_j\Theta_jU_j\), so \(\|r\|=\varepsilon\). Evaluation at every \(s_\ell\) has norm one. For any finite set \(I\subset\mathbb Z\setminus\{0\}\), (8) therefore implies
\[
\sum_{j\in J'}\|u_j\|^2\ge\frac1{C_q}
\sum_{\ell\in I}\frac{[b/|s_\ell|-\varepsilon]_+^2}{a_\ell}.
\tag{19}
\]
Let \(S_q=\sqrt{1+\tau^2}\). By (15), there are fixed \(K_j>0\) with \(|\Theta_j(s_\ell)|\le K_j\delta_{j,\ell}\). Put \(K^2=\sum_{j\in J'}K_j^2B_j^2>0\). Equations (17)--(18) give
\(a_{Dn}\le K^2\|n\alpha\|^2\), while \(|s_{Dn}|\le S_qDn\). If
\[
X=\frac{b}{2S_qD\varepsilon}\ge1,
\]
choose \(I=\{Dn:1\le n\le X\}\) in (19) to obtain
\[
\sum_{j\in J'}\|u_j\|^2\ge
\frac{b^2}{4C_qS_q^2D^2K^2}
\sum_{n\le X}\frac1{n^2\|n\alpha\|^2}
\ge\frac{b^2}{4C_qS_q^2D^2K^2}(1+\lfloor\log_2X\rfloor).
\tag{20}
\]
The last inequality is NB-355's elementary weighted-return lemma. To recall why sparsely spaced returns do not invalidate it: for each dyadic scale \(2^k\le X\), Dirichlet gives \(n_k\le2^k\) with \(\|n_k\alpha\|\le2^{-k}\). If one integer is reused at \(r\) scales, its reciprocal-square weight is at least \(4^{r-1}\ge r\). Summing over distinct selected integers pays for all \(1+\lfloor\log_2X\rfloor\) scales. This proves (4) without an irrationality measure or bounded partial quotients.

## 5. A real-seed control prevents an unjustified higher-rank no-go

The factorization and interpolation arguments above also hold for real seed indices \(j>1\): the Mellin identity (5) and its outer multiplier \((1-j^{-s})/\sqrt j\) have the same properties. This is a control within the continuous Nyman family, not an assertion about specified integer seeds.

Fix \(q>1\), and take \(J=\{q,q^\alpha,q^\beta\}\), \((\alpha,\beta)\in(1,2)^2\). For Lebesgue-almost every such pair, (1) is finite and hence the projected target has a finite-energy three-orbit decomposition. Here is a direct metric check. Put
\(R_n=\max(\|n\alpha\|,\|n\beta\|)\). Multiplication by \(n\) preserves Haar measure on the two-dimensional torus, so
\[
\operatorname{meas}\{R_n<1/n\}=O(n^{-2}),\qquad
\int \frac{\mathbf1_{R_n\ge1/n}}{n^2R_n^2}\,d\alpha\,d\beta
=O\!\left(\frac{\log n}{n^2}\right).
\tag{21}
\]
The first estimate and Borel--Cantelli leave only finitely many omitted terms almost surely. The second and Tonelli make the truncated series finite almost surely. Exact zero denominators form a null set. Since \(R_n^2\le\|n\alpha\|^2+\|n\beta\|^2\le2R_n^2\), this proves the claim.

This control shows that the two-seed obstruction cannot be generalized solely from finite seed count or density of simultaneous phase returns. It does **not** establish convergence for \((\alpha,\beta)=(\log3/\log2,\log5/\log2)\), a specified point in a measure-zero arithmetic family. No almost-everywhere theorem is a substitute for that arithmetic estimate.

## Prior art, mathematical delta, and boundaries

Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies the target projection and common inner factor in (5)--(7); NB-354 supplies the seed factors. Classical Hardy interpolation is the relevant general mechanism: Shapiro and Shields, *On some interpolation problems for analytic functions*, Amer. J. Math. 83 (1961), 513--532, DOI `10.2307/2372892`, characterize weighted Hardy interpolation. Its bounded-onto formulation is explicitly reviewed in Arcozzi, Rochberg and Sawyer, *Carleson Measures and Interpolating Sequences for Besov Spaces on Complex Balls*, [Introduction, pp. 3--4 of the author manuscript](https://math.mcmaster.ca/~sawyer/Publications/arsball17.pdf). The original Shapiro--Shields paper was checked bibliographically; the stated theorem comparison uses that accessible author manuscript. The special lattice right inverse needed here is proved directly in (9).

Douglas, *Variations on a theme of Beurling*, [Section 6](https://nyjm.albany.edu/j/2011/17a-1v.pdf), is the surrounding corona/invariant-subspace prior-art boundary. A uniform corona bound would be stronger than the target-specific summability condition here. Borda's [squared reciprocal-sum analysis, Section 4](https://arxiv.org/pdf/1606.07946), already cited in NB-355, is the scalar Diophantine prior-art boundary; no new interpolation, corona, factorization, metric approximation, or reciprocal-sum theorem is claimed.

The local mathematical delta is the sufficient direction in (2), with an explicit Hardy lift and physical cost bounds, and its exclusion of all fixed logarithmic-rank-two repairs. NB-355 supplied only necessary lattice bounds for two components. The real-seed control (21) makes the boundary of that obstruction explicit. These are classical tools specialized to the source family and the retained target, not a new RH criterion or a novelty claim based on unsuccessful searching.

- Common nonzero seed-lattice zeros make (1) infinite immediately; the commensurable case still has NB-354's strictly smaller closure. Rank two has full continuous closure but cannot attain its best target projection in the algebraic sum.
- For a fixed integer family of rank at least three, (2) is exact, but convergence of its particular arithmetic series is not established here. Linear independence of logarithms alone is not a quantitative summability estimate.
- The seed set is fixed. Constants in (20) depend on its rational coordinates and can deteriorate when the family grows. No uniform no-go for an increasing number of seeds follows.
- A finite-energy orbit vector can require infinitely many generating dilations. Neither (2) nor (16) supplies bounded dilation range, absolute-coefficient cost, or a finite-section convergence rate.
- The upper construction in (13)--(14) applies when the full series converges. It does not reverse the logarithmic lower bound (20) into a matching error-versus-budget rate when the series diverges.

Decisive audit points are the onto map (9), conjugation in (12), division by precisely the simple-zero Blaschke product in (5), retention of \(b\), and the sublattice denominator clearing in (17). Evidence is the analytic derivation; no numerical optimum, Lean verification, independent adversarial approval, or RH advance is asserted.
