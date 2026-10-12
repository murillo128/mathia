# PC-428 — marked Hilbert cyclic transport is unbounded throughout the right critical half-strip

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE for a **bounded translation-equivariant marked-vector comparison** between the actual Prime-Circle Hilbert--Schmidt shell sector and PC-424's zero-free control. Although PC-427 identifies their embedded closed cyclic space and unmarked translation representation, on every fixed line \(1/2<\sigma<1\) the unique equivariant operator carrying a control shell to the corresponding genuine shell is necessarily unbounded, and so is its inverse. The source/control marked spectral measures are mutually absolutely continuous but have no uniform comparison in either direction. The obstruction follows from classical Bohr--Courant value density, **whether or not the line contains zeta zeros**, and cannot locate zeros or prove RH.

A canonical closed, densely defined transport **does** exist; even the two native shifts \(\log2,\log3\) determine its graph closure. This distinguishes *existence of a marked unbounded transport* from *bounded similarity* and from equality of the unmarked spectral multiplicity. Nothing is asserted for non-equivariant maps or other source-forced cross-shell couplings.

## 1. Exact marked spectral model

Fix \(1/2<\sigma<1\). Use the closed Hilbert--Schmidt Fourier sector from PC-427,
\[
\mathcal E=L^2\!\left(\mathbb R,\frac2\pi|t|\,dt\right),
\qquad
\mathcal A=\mathcal J(\mathcal E)
\subset\mathcal S_2(L^2(\mathbb R)).
\tag{1}
\]
Here \(\mathcal J\) is the isometry defined by the Hilbert-commutator Fourier kernel, and log-radius conjugations act as
\[
\mathcal J^{-1}\mathcal T_a\mathcal J f(t)=e^{iat}f(t).
\tag{2}
\]
The arithmetic Bose seed and the explicitly zero-free matched seed from PC-424 have the spectral coordinates
\[
g_\sigma(t)=\frac{\Gamma(s)\zeta(s)}{\sqrt{2\pi}},
\qquad
g_{0,\sigma}(t)=\frac{Z_0(s)}{\sqrt{2\pi}},
\quad
Z_0(s)=-\frac{1+s}{2(1-s)}\Gamma(s),
\quad s=\sigma-it.
\tag{3}
\]
Both lie in \(\mathcal E\); \(g_{0,\sigma}(t)\) is nonzero for every real \(t\), and \(g_\sigma\) is nonzero almost everywhere, since zeros of an analytic nonidentically-zero function on this line are isolated.

Consequently the **unique** measurable multiplier carrying the distinguished control seed into the actual seed is
\[
\boxed{\
R_\sigma(t)=\frac{g_\sigma(t)}{g_{0,\sigma}(t)}
=-2\,\frac{1-\sigma+it}{1+\sigma-it}\,\zeta(\sigma-it).
}
\tag{4}
\]
For every primitive layer \(n>1\), PC-427 gives
\[
g_{n,\sigma}=q_{n,\sigma}g_\sigma,\qquad
g_{0,n,\sigma}=q_{n,\sigma}g_{0,\sigma},
\quad
q_{n,\sigma}(t)=-n^{1-s}
\prod_{p\mid n}(1-p^{s-1}).
\tag{5}
\]
The function \(q_{n,\sigma}\) is bounded and bounded away from zero on \(\mathbb R\), so the **same** ratio \(R_\sigma\) transfers every matched primitive-shell pair. No additional prime-shell multiplier can repair its upper or lower essential bounds.

## 2. Absolute continuity does not imply bounded equivalence

Let \(\mu(dt)=(2/\pi)|t|dt\), and let
\[
d\nu_\sigma=|g_\sigma|^2d\mu,\qquad
d\nu_{0,\sigma}=|g_{0,\sigma}|^2d\mu.
\]
These finite spectral measures are equivalent as measure classes (PC-427), but their exact Radon--Nikodym ratio is
\[
\boxed{
\frac{d\nu_\sigma}{d\nu_{0,\sigma}}(t)=|R_\sigma(t)|^2
}\quad\text{almost everywhere}.
\tag{6}
\]
A uniform two-sided comparison of their quadratic forms, meaning
\[
A\int|f|^2d\nu_{0,\sigma}
\le\int|f|^2d\nu_\sigma
\le B\int|f|^2d\nu_{0,\sigma}
\quad\text{for all simple }f
\tag{7}
\]
with \(0<A\le B<\infty\), holds **if and only if**
\[
0<\operatorname*{ess\,inf}_{t}|R_\sigma(t)|
\le\operatorname*{ess\,sup}_{t}|R_\sigma(t)|<\infty.
\tag{8}
\]
The same criterion is equivalent to a bounded, boundedly invertible multiplication operator on \(\mathcal E\) carrying one marked vector to the other while commuting with every \(\mathcal T_a\). We now show that both inequalities in (8) fail.

## 3. Bohr--Courant gives simultaneous blow-up and near-vanishing

The elementary non-zeta factor in (4) obeys the exact sharp bounds
\[
\boxed{
\frac{2(1-\sigma)}{1+\sigma}
\le
\left|2\frac{1-\sigma+it}{1+\sigma-it}\right|
<2
\quad(t\in\mathbb R).
}
\tag{9}
\]
The strict upper inequality becomes an equality only in the limit \(|t|\to\infty\).

The classical Bohr--Courant theorem (1914) states that for **each fixed**
\(1/2<\sigma<1\), the value set
\[
\{\zeta(\sigma+it):t\in\mathbb R\}
\]
is dense in \(\mathbb C\). Applying it to arbitrarily large complex values and to values arbitrarily near zero, then using (9), proves
\[
\sup_{t\in\mathbb R}|R_\sigma(t)|=\infty,
\qquad
\inf_{t\in\mathbb R}|R_\sigma(t)|=0.
\tag{10}
\]
Since \(R_\sigma\) is continuous, every arbitrarily large or arbitrarily small value has a **positive-measure interval** of similarly extreme values. Thus (10) holds in the essential sense required by (8):
\[
\boxed{
\operatorname*{ess\,sup}|R_\sigma|=\infty,\qquad
\operatorname*{ess\,inf}|R_\sigma|=0.
}
\tag{11}
\]
It follows that neither domination \(\nu_\sigma\le B\nu_{0,\sigma}\) nor domination \(\nu_{0,\sigma}\le B\nu_\sigma\) is possible for finite \(B\).

Crucially, the failure of the **inverse** bound does not imply that \(\zeta\) actually vanishes on this line. If the line has no zeta zero, the near-zero sequence guaranteed by Bohr--Courant must escape every compact \(t\)-interval; if a subsequence stayed bounded, continuity would give an actual zero. A zero-free line can therefore have arbitrarily poor marked inverse conditioning. This remains the conclusion under the hypothesis that RH is true.

For finite spectral cutoffs \(|t|\le T\), the forward multiplication operator is bounded, but its norm tends to infinity as \(T\to\infty\). Where the inverse cutoff is bounded (i.e. no zero lies on the cutoff interval), its norm cannot remain uniformly bounded as the cutoff expands. Actual zeros can make a finite-cutoff inverse already unbounded; they are **not needed** for the global no-go.

## 4. There is a canonical closed, unbounded, two-prime-determined transfer

Let \(G=\mathbb Z\log2+\mathbb Z\log3\), dense in \(\mathbb R\) by unique factorization. On the linear span of the two-prime control orbit define
\[
W_\sigma^{(0)}:
P(t)g_{0,\sigma}(t)\longmapsto P(t)g_\sigma(t),
\qquad
P(t)=\sum_{a\in F\subset G}c_ae^{iat}.
\tag{12}
\]
This is well defined: if \(Pg_{0,\sigma}=0\) almost everywhere, nonvanishing of \(g_{0,\sigma}\) forces \(P=0\) almost everywhere, and hence \(Pg_\sigma=0\). It is equivariant under the group action, and its orbit domain is dense by PC-427.

Consider the maximal multiplication operator
\[
W_\sigma=M_{R_\sigma},\qquad
\operatorname{Dom}W_\sigma
=\{f\in\mathcal E:R_\sigma f\in\mathcal E\}.
\tag{13}
\]
It is closed, densely defined, injective, and has dense range. Injectivity and dense range follow because \(R_\sigma\ne0\) almost everywhere. It maps \(g_{0,\sigma}\) to \(g_\sigma\) and commutes with all character multipliers on its invariant domain. The inverse \(M_{1/R_\sigma}\) on the range is also closed, densely defined, and unbounded.

More precisely, \(W_\sigma\) is the **graph closure** of the minimal two-prime map (12). On its orbit core,
\[
\|Pg_{0,\sigma}\|_{\mathcal E}^2+
\|Pg_\sigma\|_{\mathcal E}^2
=\int_{\mathbb R}|P(t)|^2
\bigl(d\nu_{0,\sigma}+d\nu_\sigma\bigr).
\tag{14}
\]
The sum on the right is a finite positive measure. Characters for the dense group \(G\) span a dense subspace of its \(L^2\): continuity first upgrades \(G\)-characters to all real characters, and uniqueness of Fourier transforms of finite measures gives totality. By the substitution \(f=Pg_{0,\sigma}\), this density is precisely graph-norm density in (13). Hence
\[
\boxed{\overline{W_\sigma^{(0)}}=M_{R_\sigma}.}
\tag{15}
\]
The corresponding map built from **any** shell pair in (5) has the same graph closure: multiplying the measure in (14) by \(|q_{n,\sigma}|^2\) leaves an equivalent graph norm because \(q_{n,\sigma}\) is bounded and boundedly invertible.

A bounded operator intertwining only the two shifts and carrying one marked seed to the other would also intertwine every real shift (density of \(G\), strong continuity, boundedness). Its restriction to the dense marked orbit must coincide with (12), so (11) and (15) exclude it. The reverse marked intertwiner is excluded for the same reason. Thus the obstruction already holds for the source-native two-prime shift group, not just an arbitrarily enlarged continuum group.

## 5. Prior art, controls, novelty, and boundary

**Classical inputs.** H. Bohr and R. Courant, *Neue Anwendungen der Theorie der Diophantischen Approximationen auf die Riemannsche Zetafunktion*, *Journal für die reine und angewandte Mathematik* 144 (1914), 249--274, DOI 10.1515/crll.1914.144.249, prove the fixed-vertical-line value-density theorem used in (10)--(11). A. Sourmelidis and J. Steuding, *Spirals of Riemann's Zeta-Function -- Curvature, Denseness, and Universality*, arXiv:2306.00460 (2023), give modern value-distribution context. Character totality for finite measures, multiplication-operator commutants, and closed multiplication operators are classical functional analysis. PC-424 and PC-427 supply the **actual source-generated** Hilbert--Schmidt kernels, matched zero-free seed, exact shared cyclic sector, and shell multiplier (5).

**What is genuinely additional here.** PC-427 classifies the unmarked cyclic sector and points out that marked densities differ. This finding determines the precise **bounded-versus-closed-unbounded transport boundary**: on every right critical half-strip line the actual/control densities are equivalent but cannot dominate each other, and the unique source-compatible two-prime transport has the explicit closed graph (13)--(15). No novelty is claimed for Bohr--Courant density, standard multiplier theory, or the abstract graph argument apart from their exact placement in the Prime-Circle shell comparison.

**Source specificity and counterfactual.** A trivial same-seed control has \(R\equiv1\) and a bounded marked transport. The genuine Bose/control pair differs measurably because its marked ratio contains \(\zeta\), yet the failure of bounded comparison follows from **near-zero values, not necessarily actual zeros**. Composite or relabeled shell indices leave (4) unchanged up to boundedly invertible Euler multipliers. Hence the result captures ordinary classical zeta value distribution, not an independent primality discriminator or a new constraint on the critical line.

**Limits and decisive tests.** Check the Gamma cancellation and the sign in (4), the strict positive lower bound in (9), the fixed-line quantifier of Bohr--Courant, and the positive-measure rather than merely pointwise extremes in (11). Check graph-core totality with the finite measure in (14), not with unweighted Lebesgue measure. The theorem is restricted to \(1/2<\sigma<1\), to the Hilbert--Schmidt difference-kernel sector, and to **translation-equivariant** marked transport. It makes no claim for \(\sigma\le1/2\), unmarked unitary equivalence (which PC-427 already provides), externally reweighted Hilbert norms, nonlinear source-sensitive statistics, or a source-forced angular/old--new coupling not reducible to the scalar multiplier (4). Neither spectral absolute continuity nor failure of bounded marked equivalence proves RH.
