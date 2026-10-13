# WI-450 — Sharp aggregate support budget for simultaneous reciprocal-lattice orthogonality

**Status:** EXACT-DERIVED + CLASSICAL-JENSEN/PALEY-WIENER-SPECIALIZATION + SHARP-EXISTENCE/OBSTRUCTION + NON-RH + NO-NOVELTY-CLAIM

**Local dependencies:** WI-445 (bounded-span triple Gram rigidity), WI-446 (single-lattice smooth escape), WI-448 (commensurate single-lattice energy), WI-449 (incommensurate single-lattice endpoint tariff).

**Source anchors:** B. Ya. Levin, *Distribution of Zeros of Entire Functions*, revised edition, AMS Translations of Mathematical Monographs 5 (1980), DOI 10.1090/MMONO/005; N. Levinson, *Gap and Density Theorems*, AMS Colloquium Publications 26 (1940), DOI 10.1090/COLL/026; Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, arXiv:2609.07918v2, Proposition 4.1.

## Exact statement

Fix the convention
\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt.
\]
Let \(p_j>0\), with finitely or countably many indices, satisfy \(p_i/p_j\notin\mathbb Q\) whenever \(i\ne j\), and write \(S=\sum_jp_j\in(0,+\infty]\).

**Necessity.** If \(f\in L^1(\mathbb R)\) is supported in an interval of length \(L<\infty\), \(\int f=1\), and
\[
\widehat f(k/p_j)=0\quad(j\ \text{arbitrary},\ k\in\mathbb Z\setminus\{0\}),
\tag{1}
\]
then
\[
\boxed{S\le L.} \tag{2}
\]
Neither positivity nor evenness is needed.

**Sharp Wang-class converse.** For \(0<\lambda\le1\), define Wang's admissible smooth-square densities by
\[
\mathcal F_\lambda=
\left\{\eta^2:\eta\in C_c^\infty((-\lambda/2,\lambda/2);\mathbb R),
\quad \eta\ {\rm even},\quad\int\eta^2=1\right\}.
\]
A prescribed finite or countable pairwise-incommensurate family admits *one* \(f\in\mathcal F_\lambda\) satisfying every constraint (1) **if and only if**
\[
\boxed{S<\lambda.} \tag{3}
\]
In particular, countably infinitely many independent reciprocal lattices can be realized exactly in a single Wang test, provided their total period budget fits the open support window. Each lattice is internally orthogonal, but the union of lattices need not be one mutually orthogonal exponential family.

**Near-optimality.** For any \(\varepsilon>0\) there exist a countably infinite pairwise-incommensurate family with arbitrarily small \(S>0\) and an exactly feasible \(f\in\mathcal F_\lambda\) for which \(0<C(f)-C_\lambda<\varepsilon\), where
\[
C(f)=\|f\|_2^2+\iint |t-u|f(t)f(u)\,dt\,du
\]
and \(C_\lambda=C(f_*)\) is Wang's unique cosine-optimizer value. The periods and test function are chosen together; the statement does not supply a uniform height-dependent zeta test.

## Proof of necessity: Jensen counts disjoint grids

Translate the support to be centered at the origin, multiplying its transform by a nowhere-vanishing exponential. The resulting entire function \(F\) has \(F(0)=1\), unchanged zeros, and
\[
|F(re^{i\vartheta})|
\le \|f\|_1 \exp(\pi Lr|\sin\vartheta|).
\]
For any fixed finite subfamily of \(m\) periods, irrationality of the ratios makes their nonzero reciprocal grids disjoint. Thus the number \(n_F(r)\) of zeros in \(|z|\le r\), counted with multiplicity, obeys
\[
n_F(r)\ge2\sum_{j=1}^m\lfloor p_jr\rfloor.
\]
Jensen's formula (using radii avoiding zeros on the boundary) gives
\[
\int_0^R\frac{n_F(r)}r\,dr
=\frac1{2\pi}\int_0^{2\pi}\log|F(Re^{i\vartheta})|d\vartheta
\le\log\|f\|_1+2LR.
\]
For each fixed \(p>0\),
\(\int_0^R\lfloor pr\rfloor\,dr/r=pR+O_p(\log(2+R))\).
Divide by \(2R\) and let \(R\to\infty\) to obtain \(\sum_{j=1}^mp_j\le L\). Since every finite subfamily satisfies this bound, (2) follows even if the number of periods is countable. An admissible Wang density has actual compact support in a strictly smaller interval than the open window, forcing \(S<\lambda\).

## Constructive sharp converse, including the smooth-square condition

Suppose \(S<\lambda\). Independently choose
\(U_j\sim{\rm Uniform}[-p_j/2,p_j/2]\).
For infinitely many indices the series \(\sum_jU_j\) converges absolutely for every realization, because \(\sum_j|U_j|\le S/2\). Let \(\mu\) be its even probability distribution; its support is contained in \([-S/2,S/2]\). For every \(j\), independence and the uniform sinc transform imply
\[
\widehat\mu(k/p_j)=0\quad(k\in\mathbb Z\setminus\{0\}).
\]
Choose \(0<\delta<\lambda-S\) and the even, normalized, strictly positive-inside superflat bump
\[
g(t)=Z^{-1}\exp\!\left[-\frac1{1-(2t/\delta)^2}\right]
{\bf1}_{\{|t|<\delta/2\}},\qquad \int g=1.
\]
Then \(f=\mu*g\) is even, smooth, nonnegative, normalized, supported in an interval of length \(S+\delta<\lambda\), and satisfies all (1) **exactly** by the product rule for Fourier transforms.

It remains essential to check \(\eta=\sqrt f\in C_c^\infty\), since a generic nonnegative smooth function need not have a smooth square root. For every integer \(n\ge0\) and every \(0<\alpha<1\), the explicit superflat bump satisfies
\[
|g^{(n)}(t)|\le C_{n,\alpha}\,g(t)^\alpha.
\]
Differentiating the convolution and applying Jensen's inequality to the probability measure \(\mu\) yields
\[
|f^{(n)}(t)|\le C_{n,\alpha}
\int g(t-u)^\alpha\,d\mu(u)
\le C_{n,\alpha}f(t)^\alpha. \tag{4}
\]
On \(\{f>0\}\), each term in the \(n\)-th derivative of \(\sqrt f\) is a constant times
\(f^{1/2-r}\prod_{\ell=1}^r f^{(n_\ell)}\), with \(1\le r\le n\) and \(\sum_\ell n_\ell=n\).
By (4), it is \(O(f^{1/2-r(1-\alpha)})\).
Choose \(\alpha>1-1/(2n)\), so every such exponent is positive. All derivatives therefore extend continuously by zero across the zero set; induction by the mean-value theorem gives \(\sqrt f\in C_c^\infty\). Evenness and normalization are preserved, so \(f=\eta^2\in\mathcal F_\lambda\). This proves (3) for any finite or countable family.

## Near-optimal construction and audit boundaries

Let \(f_*\) be Wang's positive cosine optimizer on the *closed* window, with jump discontinuities at its endpoints. Pick even superflat squared cutoffs of \(f_*\), normalized to probability densities \(g_\delta\), whose supports remain strictly inside the window and satisfy \(\|g_\delta-f_*\|_2\to0\). Their smooth endpoint profiles obey the derivative-power bounds used in (4). Fix a cutoff, then take a countable sequence of pairwise-incommensurate periods with total \(S\downarrow0\), e.g. a suitably rescaled geometric family \(p_j=c e^{-j}\). Their uniform-sum laws \(\mu_S\) form an approximate identity:
\[
\|\mu_S*g_\delta-g_\delta\|_2
\le\sup_{|u|\le S/2}\|g_\delta(\cdot-u)-g_\delta\|_2\longrightarrow0.
\]
The construction above gives smooth squares with all Fourier zeros exact. Continuity of \(C\) on a common compact support and Wang's exact second-variation identity yield \(C(\mu_S*g_\delta)\to C_\lambda\) in the ordered limit. Strict inequality \(C(f)>C_\lambda\) holds because the unique optimizer \(f_*\) is not endpoint-smooth.

**Falsification controls.** Repeated grids cannot be double-counted: if \(p_1=p_2\), the two constraints coincide and (2) with \(p_1+p_2\) fails; rational ratios similarly require intersection correction. No bound on the size of a single mutually orthogonal *union* follows from this theorem. The equality \(S=\lambda\) is accessible to the wider closed-support convolution class but impossible when support is strictly inside Wang's open window. All estimates concern prescribed real-frequency grids; there is no zeta-ordinate packing hypothesis or indefinite Weil-block control.

**Prior art and relevance.** Jensen zero counting, exponential type/Paley--Wiener bounds, sinc factors, and convolution are classical (Levin, Levinson). The sharp iff statement and smooth-square construction are a source-specific assembly, not a claim of a novel general method or priority. WI-448--WI-449 control the *energy price* of one reciprocal lattice; this finding instead controls the *total support feasibility* of multiple disjoint lattices. The gap to RH remains the absence of an independent arithmetic mechanism forcing actual off-line zeta blocks into these prescribed grids or imposing an individual defect certificate. No density-one or critical-line simplicity conclusion, much less RH, is obtained.
