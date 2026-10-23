# NB-352 — Finite Nyman patches cannot remove the geometric target obstruction

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-351; classical Mellin identity, simultaneous approximation, and zeta growth on the 1-line
- **Classification:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FINITE-NORMED-DUAL + CLASSICAL-INGREDIENTS

## Claim and scope

In \(H=L^2(0,1;dx)\), write
\[
e(x)=1,\qquad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\qquad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{(0,1/a]}(x).
\]
Fix an integer \(q\ge2\), and let
\[
\mathcal C_q=\overline{\operatorname{span}}\{A_ag_{q^k}:a\ge1,\ k\ge1\}.
\]
Choose any **fixed finite** list of columns
\[
f_\nu=A_{a_\nu}g_{j_\nu},\qquad
a_\nu\ge1,\quad j_\nu\in\mathbb N,\ j_\nu\ge2,
\quad 1\le\nu\le d,
\qquad D=\operatorname{span}(f_1,\ldots,f_d).
\]
The dilation parameters \(a_\nu\) may be real. Then, unconditionally,
\[
\boxed{\operatorname{dist}(e,\mathcal C_q+D)>0.}\tag{1}
\]
In particular, adjoining any fixed old section \(V_N=\operatorname{span}(g_2,\ldots,g_N)\) does not remove NB-351's obstruction, even when every real dilation of every geometric seed is available. The same conclusion holds for its smaller integer late-dilation spaces \(\mathcal C_{q,M}\).

There is a finite normed dual certificate for (1) using at most \(d+1\) Mellin evaluations on the geometric zero lattice. Its exact norm and target pairing are given below. The positive constant depends on the added columns; no uniform bound as \(d,N,q\), or the columns vary is asserted.

## 1. The lattice relaxation

Use the unnormalized Mellin transform
\(\mathcal Mf(s)=\int_0^1 f(x)x^{s-1}dx\). Set
\[
\tau=\frac{2\pi}{\log q},\qquad s_\ell=1+i\tau\ell\quad(\ell=1,2,\ldots),
\qquad E_\ell(f)=s_\ell\mathcal Mf(s_\ell).
\]
Each \(E_\ell\) is a continuous complex-linear functional on \(H\), with
\[
\|E_\ell\|=|s_\ell|,\qquad E_\ell(e)=1.
\tag{2}
\]
Define the closed enlargement
\[
X_q^+=\bigcap_{\ell\ge1}\ker E_\ell.
\]
Only positive lattice indices are needed here. NB-351's two-sided lattice relaxation is contained in \(X_q^+\).

The classical identities, including the support cutoff in \(A_a\), are
\[
\mathcal Mg_j(s)=\frac{\zeta(s)}s(j^{-1}-j^{-s}),\qquad
\mathcal M(A_af)(s)=a^{1/2-s}\mathcal Mf(s).
\tag{3}
\]
For \(j=q^k\), the elementary factor vanishes at every \(s_\ell\), so
\(\mathcal C_q\subset X_q^+\). None of these evaluations is at \(s=1\), where the zeta pole cancels the elementary zero. No assumption about nontrivial zeta zeros is used.

For the added columns, let \(v_\ell\in\mathbb C^d\) be the row vector
\[
v_{\ell,\nu}=E_\ell(f_\nu)
=\frac{a_\nu^{-1/2-i\tau\ell}}{j_\nu}\,
\zeta(s_\ell)\left(1-e^{-2\pi i\ell\alpha_\nu}\right),
\qquad \alpha_\nu=\frac{\log j_\nu}{\log q}.
\tag{4}
\]

## 2. Simultaneous returns overpower the zeta growth

For every integer \(Q\ge2\), the pigeonhole proof of simultaneous Dirichlet approximation gives an integer
\[
1\le\ell_Q\le Q^d,\qquad
\max_\nu\|\ell_Q\alpha_\nu\|_{\mathbb R/\mathbb Z}\le Q^{-1}.
\tag{5}
\]
Indeed, put the \(Q^d+1\) fractional-part vectors with indices \(0,\ldots,Q^d\) into \(Q^d\) boxes of side \(1/Q\), and subtract two vectors in the same box. No rational independence of the logarithms is required.

The classical bound on the 1-line gives a constant depending only on \(q\) such that
\[
|\zeta(1+i\tau\ell)|\le C_q(1+\log\ell),\qquad \ell\ge1.
\tag{6}
\]
For completeness, the required coarse bound follows directly from Euler summation. For integer \(K\ge1\), \(\Re s>0\), \(s\ne1\),
\[
\zeta(s)=\sum_{n\le K}n^{-s}+\frac{K^{1-s}}{s-1}
-s\int_K^\infty\{u\}u^{-s-1}\,du.
\tag{7}
\]
At \(s=1+it\), \(t\ge1\), choose \(K=\lceil t\rceil\). The three terms are bounded by \(1+\log K\), \(1/t\), and \(|s|/K\), respectively. The remaining compact interval \(\tau\le t\le1\), if nonempty, stays away from the pole and is bounded. This proves (6) without RH or a zero-free-region estimate.

Combining (4)--(6) yields
\[
|v_{\ell_Q,\nu}|
\le\frac{2\pi C_q}{j_\nu\sqrt{a_\nu}}
\frac{1+d\log Q}{Q}\longrightarrow0.
\tag{8}
\]
In particular, zero belongs to the closure of the set of rows \(v_\ell\). The indices \(\ell_Q\) need not tend to infinity: if a bounded index recurs along arbitrarily large \(Q\), it has exact phase cancellation in every column and its row is zero. That case is also covered by (8).

If \(e=x+\sum c_\nu f_\nu\) with \(x\in X_q^+\), applying \(E_{\ell_Q}\) would give
\[
1=v_{\ell_Q}c\longrightarrow0,
\]
a contradiction. Thus \(e\notin X_q^++D\). This sum is closed: it is the inverse image under \(H\to H/X_q^+\) of the finite-dimensional image of \(D\). Consequently
\[
\operatorname{dist}(e,\mathcal C_q+D)
\ge\operatorname{dist}(e,X_q^++D)>0,
\tag{9}
\]
which proves (1).

The finite-dimensional step is essential. The functionals in (2) have unbounded norms, so (8) alone cannot be passed through arbitrary norm limits of an increasing patch family.

## 3. A finite certificate with its physical norm

Let \(r\le d\) be the dimension of the row span of \(\{v_\ell:\ell\ge1\}\). If \(r=0\), any one \(E_\ell\) already annihilates the patch and detects the target. Suppose \(r>0\). Choose indices \(\ell_1,\ldots,\ell_r\) whose rows form a basis. Every other row has unique coordinates
\[
v_\ell=\sum_{i=1}^r\lambda_i(\ell)v_{\ell_i}.
\tag{10}
\]
These coordinates depend continuously on the row in this fixed finite-dimensional space. Hence (8) gives \(\lambda_i(\ell_Q)\to0\). Select one index \(\ell_*\) for which
\[
\left|\sum_i\lambda_i(\ell_*)\right|\le\frac12.
\]
It is distinct from the basis indices. Then
\[
\mathcal L=E_{\ell_*}-\sum_{i=1}^r\lambda_i(\ell_*)E_{\ell_i}
\tag{11}
\]
annihilates \(X_q^++D\) and satisfies
\(\mathcal L(e)=1-\sum_i\lambda_i(\ell_*)\ne0\).
This proves the existence of the asserted certificate using \(r+1\le d+1\) evaluations, including when the added columns are dependent modulo \(X_q^+\).

More generally, given distinct positive indices \(m_0,\ldots,m_r\) and coefficients \(b_0,\ldots,b_r\) satisfying
\[
\sum_{k=0}^r b_kv_{m_k}=0,\qquad B:=\sum_{k=0}^r b_k\ne0,
\tag{12}
\]
put \(\mathcal L=\sum_k b_kE_{m_k}\). Its integral kernel is
\[
P(x)=\sum_k b_ks_{m_k}x^{s_{m_k}-1},\qquad
\mathcal L(f)=\int_0^1 f(x)P(x)\,dx.
\]
Direct integration gives the **physical** \(L^2(dx)\) dual norm
\[
G:=\|\mathcal L\|^2=\int_0^1|P(x)|^2dx
=\sum_{k,h}b_k\overline{b_h}
\frac{s_{m_k}\overline{s_{m_h}}}{s_{m_k}+\overline{s_{m_h}}-1}>0.
\tag{13}
\]
Here \(G>0\) also follows from \(\mathcal L(e)=B\ne0\). Cauchy--Schwarz supplies the explicit finite certificate
\[
\boxed{\operatorname{dist}(e,\mathcal C_q+D)^2
\ge\frac{|B|^2}{G}>0.}\tag{14}
\]
The cruder fully explicit denominator \((\sum_k|b_ks_{m_k}|)^2\) may replace \(G\). Formulae (12)--(14) specify what a numerical implementation must certify: annihilation of the full trial space, nonzero target response, and a valid norm bound. Small columnwise residuals do not suffice when coefficients are unbounded; an unchecked floating-point nullspace is not a certificate.

The existence proof does not provide a uniform bound on the basis conditioning or the selected evaluation heights. At large height, \(G\) can be large; there is no claim that (14) is sharp or computationally inexpensive.

## Boundaries, controls, and mathematical delta

NB-351's infinite codimension alone did not settle whether this particular target could be recovered by a finite patch. Equations (8)--(9) supply the missing target-specific argument. It applies to unbounded patch coefficients because the conclusion is separation from a closed sum, with (14) giving an actual bounded functional on the whole sum.

The restriction concerns finitely many **added columns**, not finitely many seed types with all their dilations. Adding the entire orbit of a multiplicatively independent seed, such as all \(A_ag_3\) when \(q=2\), is an infinite-dimensional change and is not ruled out. Likewise an arbitrary finite-dimensional extension is not covered: adjoining \(e\) itself plainly destroys the conclusion. The Nyman form (4) is load-bearing.

With no added columns, a single evaluation gives a weaker positive bound than NB-351's exact two-sided relaxation floor. With only geometric added sources, all rows vanish and the same simple control applies. For a fixed non-geometric patch, the exact common zero of all columns may disappear; simultaneous small responses, followed by finite row elimination, replace it.

The result does not obstruct \(N\to\infty\) approximation by \(V_N+\mathcal C_q\), prove a uniform distance floor, classify the orbit of two independent seeds, or imply anything about RH. It rules out one fixed finite repair of geometric source compression.

## Prior art and evidence boundary

The Mellin identity and dilation framework are classical; see Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2, equation (2.3)](https://arxiv.org/pdf/math/9910055), and Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, [Theorem 7](https://arxiv.org/pdf/math/0607733). Common-zero annihilators, finite-dimensional quotient closedness, and Hilbert duality are not new principles.

The simultaneous-approximation argument is Dirichlet's classical pigeonhole theorem, proved here in the needed form. Locally, NB-127 already uses the same recurrence to show instability of finite-base zero-phase information; it does not give a target certificate for the present augmented source space. The new local implication combines the recurrence with the slow growth of the actual source factor \(\zeta(1+it)\), then eliminates the fixed patch exactly.

For the external growth boundary, Dhir Patel, *An explicit upper bound for* \(|\zeta(1+it)|\), Indag. Math. 33 (2022), 1012--1032, DOI `10.1016/j.indag.2022.04.007`, records the classical logarithmic estimate in [the introduction, equation (1)](https://arxiv.org/pdf/2009.00769); the coarse proof (7) suffices here. No sharp modern constant or conditional bound is imported.

The prior-art search also checked geometric sequences, restricted generators, finite extensions, and dilation completeness. Yang, *Geometric sequences and zero-free region of the zeta function*, C. R. Math. 356 (2018), 133--137, [Theorem 1.2](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2017.11.021.pdf), concerns an \(L^\infty\) approximation-to-zero-free-region implication, not this fixed-patch separation. Yang's *A fundamental set in* \(L^2(0,1)\), Acta Arith. 199 (2021), 269--274, DOI `10.4064/aa200216-31-8`, has a related restricted-generator topic, but only its publisher abstract was available; no theorem-level comparison or priority claim is made against it. Search absence is not a novelty claim.

As a secondary diagnostic, for \(q=2\) and \(D=\operatorname{span}(g_3)\), evaluations at lattice indices 1 and 5 gave a nonzero target response after the patch was eliminated. Direct integration of its kernel over the first 100,000 harmonic cells tested eight pairings: the patch column and seven integer dilates of \(g_2,g_4\). All truncated pairings were inside the analytic tail bound \(\sqrt m\sum_k|b_ks_{m_k}|/100001\), with maximum ratio below \(0.009\). Floating-point zeta evaluation and summation were not interval-certified; this is a sign/normalization check, not a certified numerical distance bound.

The evidence for (1)--(14) is the analytic derivation. No Lean validation, independent review, or new general completeness theorem is asserted.
