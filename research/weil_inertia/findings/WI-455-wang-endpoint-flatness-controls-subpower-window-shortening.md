# WI-455 — Wang endpoint flatness controls a test-dependent subpower window budget

**Status:** LITERATURE+DERIVED + EXACT-ERROR-BOUND + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** WI-440 (fixed-power smooth endpoint), WI-226 (strict-margin generalized windows), WI-354 (proportion versus individual-defect boundary).

## Claim and quantifiers

Fix \(0<\sigma<1\), a real even \(g\in C_c^\infty(\mathbb R)\) supported in \([-\sigma,\sigma]\), and write \(L=\log T\). For every \(1\le H\le T\), put \(I=(T,T+H]\), count zeta zeros with multiplicity, and define
\[
\mathcal W_I(g)=\sum_{\gamma,\gamma'\in I}
\widehat g\!\left(\frac{i(\rho-\rho')L}{2\pi}\right)
\frac4{4-(\rho-\rho')^2},\qquad
\widehat g(z)=\int g(\alpha)e^{-2\pi i\alpha z}\,d\alpha.
\]
The source estimates in Wang's v2 proof give the uniform bound
\[
\boxed{
\mathcal W_I(g)=\frac{HL}{2\pi}
\left(g(0)+\int |\alpha|g(\alpha)\,d\alpha\right)
+O_{g,\sigma}\!\left(H+L^3J_g(L)\right),\quad
J_g(L)=\int_0^\sigma |g(\alpha)|e^{L\alpha}\,d\alpha.
}
\tag{1}
\]
No relation \(T^\sigma\le H\) is needed for this **error bound**. Its usefulness as an asymptotic does depend on the displayed error. In particular, for every fixed \(B\ge0\),
\[
\boxed{T^\sigma L^{-B}\le H\le T
\quad\Longrightarrow\quad
\mathcal W_I(g)=\frac{HL}{2\pi}\mathcal M(g)+O_{g,\sigma,B}(H),}
\tag{2}
\]
where \(\mathcal M(g)=g(0)+\int|\alpha|g(\alpha)\,d\alpha\).

Thus the support endpoint survives **every fixed logarithmic shortening** of the height window. More rapid subpower shortening is governed by the actual endpoint profile of the fixed test, not just its support radius. Equations (1)--(2) extend the admissible windows in WI-440; they do not cross a fixed positive gap between support and height exponents, improve a limiting zero proportion, or exclude individual off-line zeros.

## Retain the prime norm before comparing it with the window length

Use Wang's notation, with \(\rho=1/2+\delta+i\gamma\) and
\(\mathcal F_I(x)=\sum_{\gamma,\gamma'\in I}x^{\rho-\rho'}4/[4-(\rho-\rho')^2]\):
\[
A(x,t)=\sum_\rho\frac{2x^{\delta+i(\gamma-t)}}{1+((t-\gamma)+i\delta)^2}
=-D_x(t)+B_x(t)+E_x(t),
\]
\[
D_x(t)=\sum_{n\ge2}a_n n^{-it},\quad
a_n=\frac{\Lambda(n)}{\sqrt n}\min(n/x,x/n),\quad
B_x(t)=\frac{\log(t+2)}x.
\tag{3}
\]
The unconditional Montgomery explicit formula, as stated in Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, Lemma 1, yields
\[
E_x(t)\ll x^{-1}+x^{1/2}T^{-2}+x^{-5/2}T^{-1}\ll x^{-1}
\tag{4}
\]
for \(t\in I\), \(1\le H\le T\), and \(1\le x\le T^\sigma\). Here \(x<T\) suffices; \(x<H\) is irrelevant.

The same independence of \(x/H\) holds in the zero-window localization. If \(A_I\) restricts (3) to \(\gamma\in I\), the unit-interval zero count and \(|\delta|<1/2\) give, for \(t\in I\),
\[
|A|+|A_I|\ll\sqrt xL,\qquad
|A-A_I|\ll\sqrt xL
\left(\frac1{1+t-T}+\frac1{1+T+H-t}\right).
\]
The omitted far-zero contribution \(O(\sqrt xL/T)\) is absorbed because \(H\le T\). Outside \(I\),
\( |A_I|\ll\sqrt xL/(1+\operatorname{dist}(t,I))\).
Together with the exact identity \(2\pi\mathcal F_I(x)=\int_{\mathbb R}|A_I(x,t)|^2dt\), these estimates imply
\[
2\pi\mathcal F_I(x)=\int_I|A(x,t)|^2dt
+O\!\left(xL^2[1+\log(2+H)]\right)
=\int_I|A(x,t)|^2dt+O(xL^3).
\tag{5}
\]
This reconstructs Wang's Lemma 2.4 for arbitrary \(1\le H\le T\); it uses no fixed power identity for \(H\).

The coefficient sums and Montgomery--Vaughan mean value theorem give
\[
\sum a_n^2=\log x+O(1),\quad
\sum na_n^2\ll x\log^2(2x),\quad
\|D_x\|_{L^2(I)}^2=H\log x+O(H+x\log^2(2x)).
\tag{6}
\]
Translation of the interval changes coefficients by unimodular factors, so this classical mean value bound is uniform in its starting point and length. Its infinite-series passage is allowed by \(\sum na_n^2<\infty\).

The important change from Wang's simplified proof is to retain
\[
\|D_x\|_2\ll\sqrt{HL}+\sqrt xL,
\qquad
\left|\int_I D_x\overline{E_x}\right|
\ll\frac{H\sqrt L}{x}+\frac{\sqrt H L}{\sqrt x}.
\tag{7}
\]
The second term remains when \(x>H\). It must not be omitted by invoking \(\|D_x\|_2\ll\sqrt{HL}\) outside its justified range.

For completeness, \(\int_I|B_x|^2=HL^2/x^2+O(HL/x^2)\), \(\int_I|E_x|^2\ll H/x^2\), and the \(B_x,E_x\) cross term is \(O(HL/x^2)\). Integration by parts gives
\[
\left|\int_I B_x\overline{D_x}\right|
\ll\frac Lx\sum_{n\ge2}\frac{a_n}{\log n}
\ll\frac L{\sqrt x},
\tag{8}
\]
uniformly in \(H\). Expanding the square in (5) and absorbing \(xL^2\) into \(xL^3\) therefore proves
\[
\mathcal F_I(x)=\frac H{2\pi}\left(\frac{L^2}{x^2}+\log x\right)
+O\!\left(H+\frac{HL}{x^2}+\frac{H\sqrt L}{x}
+\frac{\sqrt H L}{\sqrt x}+xL^3+\frac L{\sqrt x}\right).
\tag{9}
\]

## Integrate first, then impose an interval scale

The exact evenness identity is
\(\mathcal W_I(g)=2\int_0^\sigma g(\alpha)\mathcal F_I(T^\alpha)\,d\alpha\).
The two main terms in (9) contribute \(HL\mathcal M(g)/(2\pi)+O_g(H)\), using
\[
2L^2\int_0^\sigma g(\alpha)e^{-2L\alpha}\,d\alpha
=Lg(0)+O_g(1).
\]
All errors except \(xL^3\) integrate to \(O_g(H)\). In particular, the newly retained cross term costs only
\[
\sqrt H L\int_0^\sigma |g(\alpha)|e^{-L\alpha/2}\,d\alpha
\ll_g\sqrt H\le H\,O_g(1).
\tag{10}
\]
The other bounds are \(HL\int e^{-2L\alpha}d\alpha\ll H\), \(H\sqrt L\int e^{-L\alpha}d\alpha\ll H\), and \(L\int e^{-L\alpha/2}d\alpha\ll1\). This proves (1).

For each fixed nonnegative integer \(N\), smooth compact support implies
\(|g(\sigma-u)|\le C_{g,N}u^N\) on \([0,\sigma]\). Thus
\[
J_g(L)\le C_{g,N}T^\sigma\int_0^\infty u^Ne^{-Lu}du
=C_{g,N}N!\,T^\sigma L^{-N-1}.
\tag{11}
\]
Choosing an integer \(N\ge B+2\) gives \(L^3J_g(L)\ll_{g,B}T^\sigma L^{-B}\le O_{g,B}(H)\), proving (2). The derivative order is fixed after \(B\) is fixed; there is no uniform assertion as \(B\) grows with \(T\).

More generally, set
\[
K_g(L)=e^{-\sigma L}J_g(L)
=\int_0^\sigma |g(\sigma-u)|e^{-Lu}\,du.
\tag{12}
\]
For \(H=T^\sigma e^{-h(L)}\), equation (1) has error \(O_g(H)\) if \(L^3e^{h(L)}K_g(L)=O(1)\), and error \(o(HL)\) if \(L^2e^{h(L)}K_g(L)=o(1)\). These are **sufficient budgets for this absolute-value proof**, not necessary conditions for the actual zeta asymptotic.

For example, suppose a fixed test satisfies \(|g(\sigma-u)|\le C\exp(-c/u^p)\) near its endpoint, with \(c,p>0\). Minimizing \(Lu+cu^{-p}\) gives
\[
K_g(L)\ll_g e^{-C_pL^{p/(p+1)}},\qquad
C_p=(p+1)c^{1/(p+1)}p^{-p/(p+1)}.
\tag{13}
\]
The part away from the endpoint is \(O_g(e^{-\delta L})\); on the endpoint part the integrand is bounded by the exponential in (13). Consequently the same \(O_g(H)\) pair formula holds for
\[
H\ge T^\sigma\exp(-bL^{p/(p+1)}),\qquad 0<b<C_p,
\tag{14}
\]
with constants also depending on the fixed profile and \(b\). Such smooth even tests exist by prescribing this profile near both endpoints and joining it smoothly in the interior. This illustrates the budget in (12), without a new arithmetic estimate.

## Boundary controls

Smoothness alone does not certify the endpoint for **every** \(H=T^{\sigma+o(1)}\) through (1). To see the precise limitation, assume \(g\) is nonzero arbitrarily close to \(\sigma\). For every \(\epsilon>0\), its positive absolute mass in \((\sigma-\epsilon,\sigma)\) gives \(K_g(L)\ge m_\epsilon e^{-\epsilon L}\), where \(m_\epsilon>0\). Dominated convergence also gives \(K_g(L)\to0\). Hence
\[
\log K_g(L)=o(L).
\]
The admissible lengths \(H=T^\sigma K_g(L)^2=T^{\sigma+o(1)}\) satisfy \(1\le H\le T\) eventually, but their normalized localization majorant is
\[
\frac{L^3J_g(L)}{HL}=\frac{L^2}{K_g(L)}\longrightarrow\infty.
\tag{15}
\]
This is a counterexample to a universal deduction from the error budget, **not** a counterexample to the pair-correlation formula.

Likewise, if a fixed test actually reaches \(\sigma>\theta\) and \(H=T^\theta\), then \(J_g(L)=T^{\sigma+o(1)}\). Endpoint flatness cannot absorb the fixed power gap. The construction here reaches slightly above the instantaneous exponent \(\log H/\log T\), by a vanishing amount, without giving fixed-gap support crossing.

The test remains fixed throughout. Arbitrary \(T\)-dependent profiles, hard cutoffs, and uniform derivative bounds across optimizing families are not supplied. The bound (1) itself holds for \(H=1\), but its error there generally overwhelms the main term; this is not a microscopic asymptotic.

## Prior art and mathematical delta

- Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, [arXiv:2609.07918v2](https://arxiv.org/html/2609.07918v2), 6 October 2026: equations (2.7)--(2.22), Lemmas 2.3--2.5, and Proposition 2.6 supply the displayed proof inputs. This remains a recent unrefereed preprint. Theorem 2.2 as printed has fixed \(H=T^\theta\), \(\lambda<\theta\); the generalized weighted error (1) is derived here, not attributed to that theorem.
- H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73--82, [DOI 10.1112/jlms/s2-8.1.73](https://doi.org/10.1112/jlms/s2-8.1.73), Corollary 3, equation (1.11): the classical mean value estimate and infinite-series condition used in (6).
- S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. 214 (2024), 357--376, [arXiv:2306.04799](https://arxiv.org/pdf/2306.04799), Lemma 1: the unconditional explicit formula behind (3)--(4).

The Laplace endpoint estimates are elementary classical analysis. No new mean value theorem, pair-correlation mechanism, or priority claim is made. The delta from WI-226/WI-440 is the full \(x>H\) cross-term audit (7), the uniform weighted bound (1), and its exact separation of logarithmic shortening from test-dependent faster shortening. These form one result; (2), (14), and (15) describe its admitted regime and its limitation.

## Research consequence and audit target

The physical logarithmic shortening of a fixed-power bow does not require a strict support margin for a fixed smooth test. Its endpoint is available with relative error \(O_g(1/L)\). This removes a technical exclusion in the existing endpoint bookkeeping; it neither improves Wang's already limiting variational coefficient nor turns normalized pair statistics into an individual off-line-block certificate. Functional-equation symmetry and multiplicity are retained in \(\mathcal F_I\), not replaced by an assumed critical-line population.

The decisive audit checks are the \(H\)-uniform localization bound (5), preservation of the second term in (7), its integrability in (10), and the fixed-order Taylor estimate (11). A failure of any of these narrows (1)--(2). No computation or formal proof is used as evidence, and no cancellation of the unknown zeta error is claimed.
