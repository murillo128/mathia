# NB-367 — Third-orbit failure has exact half-dimensional size at minimal type

- **Status:** proved (classical dimension theorems plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 for exact real-orbit target membership; NB-360 for the full physical component-cost comparison
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-OBSTRUCTION + SINGULAR-MEASURE-COMPLETION

## Claim and scope

Fix real seeds \(p,q>1\), with irrational
\(\alpha=\log p/\log q\). Suppose that its optimal return exponent is one, in the precise sense
\[
\text{for every }\nu>1\text{ there is }\gamma_\nu>0
\text{ such that }\delta_n:=\|n\alpha\|_{\mathbb R/\mathbb Z}
\ge\gamma_\nu n^{-\nu}\quad(n\ge1).
\tag{1}
\]
This includes bounded-partial-quotient ratios, but does not require bounded partial quotients. It is stronger than merely having some finite Diophantine type; in particular, known finite-type bounds for integer-seed logarithmic ratios do not automatically establish (1).

Define
\[
S_\alpha(\beta)=\sum_{n\ge1}
\frac1{n^2(\delta_n^2+\|n\beta\|^2)},\qquad
\mathcal E_\alpha=\{\beta\in\mathbb R:S_\alpha(\beta)=\infty\}.
\tag{2}
\]
For every nonempty bounded open interval \(I\),
\[
\boxed{\dim_H(\mathcal E_\alpha\cap I)=\frac12,
\qquad \mathcal H^{1/2}(\mathcal E_\alpha\cap I)=\infty.}
\tag{3}
\]
The lower bound and infinite half-dimensional measure hold for **every irrational** \(\alpha\), without (1). The upper bound proved here uses (1).

There is a stronger selection statement than Lebesgue-almost-everywhere completion. Let \(\mu\) be a finite Borel measure supported in \([1,2]\), with
\[
\mu(J)\le A|J|^s\quad\text{for all intervals }J,
\qquad \frac12<s<1.
\tag{4}
\]
Then
\[
\boxed{\int S_\alpha(\beta)\,d\mu(\beta)<\infty.}
\tag{5}
\]
Thus the third seed can be drawn from a sufficiently diffuse singular measure and still have a finite-mean physical completion certificate. This is a property of the measure, not just the dimension of its support.

In \(H=L^2(0,1;dx)\), retain the actual Nyman objects
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},
\]
\[
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\},
\quad \mathcal N=\overline{\operatorname{span}}\{g_v:v>1\},
\quad t=P_{\mathcal N}e.
\]
By NB-356, \(\mathcal E_\alpha\cap(1,2)\) is exactly the set of parameters for which
\[
t\notin\mathcal C_q+\mathcal C_p+\mathcal C_{q^\beta}.
\tag{6}
\]
These are algebraic sums of three closed real-dilation spaces. The exceptional set remains half-dimensional after removing the countable set \(\mathbb Q+\mathbb Q\alpha\); failure therefore persists for uncountably many triples of logarithmic rank three. No discrete-section approximation rate follows.

## 1. Integrate the complete positive series against a Frostman measure

Fix \(s\) as in (4). For \(0<y\le1/2\), the set
\(\{\beta\in[1,2]:\|n\beta\|\le y\}\) is covered by at most \(n+2\) intervals of length \(2y/n\). Consequently
\[
\mu\{\|n\beta\|\le y\}\le C_s A n^{1-s}y^s.
\tag{7}
\]
For \(0<a\le1/2\), split into \(\|n\beta\|\le a\) and the successive annuli with radii \(2^ka\), ending at \(1/2\). Equation (7), together with the convergent geometric sum \(\sum_{k\ge0}2^{k(s-2)}\), gives
\[
\int\frac{d\mu(\beta)}{a^2+\|n\beta\|^2}
\le C_s A n^{1-s}a^{s-2}.
\tag{8}
\]
The final annulus is bounded using its actual endpoint \(1/2\), or by the larger radius in the same upper estimate. In particular no invariance of \(\mu\) under multiplication by \(n\) is assumed. Such an invariance is generally false for singular measures.

Tonelli now reduces (5) to a one-coordinate weighted return sum:
\[
\int S_\alpha\,d\mu
\le C_s A\sum_{n\ge1}n^{-1-s}\delta_n^{s-2}.
\tag{9}
\]
This controls divergence from accumulated small terms as well as terms that fail to tend to zero. A limsup estimate for individual large summands alone would not prove the upper bound in (3).

## 2. Return spacing makes the Frostman integral finite

Choose
\[
1<\nu<\frac{1+s}{2-s},\qquad
\kappa=1+s-\nu(2-s)>0,
\tag{10}
\]
which is possible exactly because \(s>1/2\). Use (1) with this \(\nu\), and write \(\gamma=\gamma_\nu\).

For integers \(N\le n<2N\), every return distance is at least
\(h=\gamma(2N)^{-\nu}\). The circular distances between two distinct points \(n\alpha\pmod1\) are also at least \(h\), by applying (1) to their positive index difference. An arc of radius \(y\le1/2\) contains at most \(1+2y/h\) such points. If the distances are ordered as \(d_1\le\cdots\le d_N\), then
\[
d_j\ge jh/4\quad(1\le j\le N).
\tag{11}
\]
For \(j=1\) use the separate first-return bound; for \(j\ge2\), use \(d_j\ge(j-1)h/2\). It would be incorrect to assume that the absolute distances themselves are all \(h\)-separated: opposite sides of zero can give nearly equal distances.

Since \(2-s>1\), (11) yields
\[
\sum_{N\le n<2N}\delta_n^{s-2}
\le(4/h)^{2-s}\sum_{j\ge1}j^{-(2-s)}
\le C_{s,\nu,\gamma}N^{\nu(2-s)}.
\tag{12}
\]
Multiplying by \(N^{-1-s}\) and summing over dyadic \(N\) proves (9). More quantitatively, with
\[
S_{\alpha,\ge N}(\beta)=\sum_{n\ge N}
\frac1{n^2(\delta_n^2+\|n\beta\|^2)},
\]
the same calculation gives
\[
\boxed{\int S_{\alpha,\ge N}\,d\mu
\le C_{s,\nu,\gamma}A N^{-\kappa}\quad(N\ge1).}
\tag{13}
\]
This is a mean tail estimate for the scalar completion cost, not an error bound for a finite Nyman generator section. Constants are not uniform over ratios satisfying (1).

## 3. Upper dimension bound via the Borel form of Frostman's lemma

Each finite partial sum in (2) is continuous, since \(\delta_n>0\). Therefore
\[
\mathcal E_\alpha=\bigcap_{m\ge1}\bigcup_{K\ge1}
\left\{\beta:\sum_{n\le K}
\frac1{n^2(\delta_n^2+\|n\beta\|^2)}>m\right\}
\tag{14}
\]
is Borel (indeed \(G_\delta\)). If its intersection with \([1,2]\) had dimension greater than \(1/2\), choose \(s\) strictly between those two numbers and below one. The Borel version of Frostman's lemma supplies a nonzero finite measure concentrated on a compact subset of that intersection and satisfying (4). But (5) says \(S_\alpha\) is finite almost everywhere for this measure, contradicting its support in \(\mathcal E_\alpha\).

For the exact theorem being used, see Bishop–Peres, [Lemma 3.1.1 and Theorem B.2.5 in the author manuscript](https://www.math.stonybrook.edu/~bishop/classes/math324.F15/book1Dec15.pdf): the appendix justifies passing from the Borel exceptional set to a compact positive-measure subset. Integer periodicity of (2), and a countable cover by unit intervals, give the upper bound for every \(I\) in (3).

## 4. A half-dimensional family of failures for every irrational fixed ratio

Let \(P_j/Q_j\) be the continued-fraction convergents of any irrational \(\alpha\), omitting the possible duplicate initial denominator. They satisfy
\[
Q_j\|Q_j\alpha\|<Q_j/Q_{j+1}<1.
\tag{15}
\]
Consider the denominator-restricted limsup set
\[
\mathcal F_\alpha=
\limsup_{j\to\infty}\ \bigcup_{a\in\mathbb Z}
\left(\frac a{Q_j}-\frac1{Q_j^2},
      \frac a{Q_j}+\frac1{Q_j^2}\right).
\tag{16}
\]
If \(\beta\) belongs to a ball at stage \(j\), then
\(Q_j\|Q_j\beta\|<1\). Together with (15), its \(n=Q_j\) summand in (2) exceeds \(1/2\). Unbounded, distinct denominators occur infinitely often, so
\[
\mathcal F_\alpha\subset\mathcal E_\alpha.
\tag{17}
\]

Apply Beresnevich–Velani's [Mass Transference Principle, Theorem 2, p. 977](https://annals.math.princeton.edu/wp-content/uploads/annals-v164-n3-p06.pdf), with ambient dimension one and gauge \(f(r)=r^{1/2}\). The balls in (16) have radius \(Q_j^{-2}\); the inflated balls have radius \(Q_j^{-1}\), so their grid covers the line at every stage. For a literal single sequence with radii tending to zero, retain only \(|a|\le jQ_j\) at stage \(j\) and enumerate these finite stages in order. Every fixed bounded interval eventually lies in the covered region, and its original limsup is unchanged. The theorem gives
\[
\mathcal H^{1/2}(\mathcal F_\alpha\cap I)
=\mathcal H^{1/2}(I)=\infty.
\tag{18}
\]
No coprimality, independence, or bounded growth ratio of the \(Q_j\) is required.

For comparison, this explicit subset itself always has dimension exactly \(1/2\): in a fixed bounded interval, stage \(j\) uses \(O_I(Q_j)\) balls, so for every \(u>1/2\) the sum of their \(u\)-dimensional costs is bounded by
\[
C_{I,u}\sum_j Q_j^{1-2u}<\infty.
\tag{19}
\]
Continued-fraction denominators grow at least at Fibonacci rate. The tails of this cover give \(\mathcal H^u(\mathcal F_\alpha\cap I)=0\). Equations (17)–(18) prove the universal lower statement, and Section 3 completes (3) under (1).

## 5. Transport back to the physical target and all three component norms

The required dictionary is the exact NB-356/NB-360 one:
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,
\qquad \mathcal Mt=Bb/s,\qquad b=B(1)>0,
\]
\[
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})},
\qquad H^2=H^2(\Re s>1/2).
\tag{20}
\]
At the nonzero zero lattice \(z_k=1+2\pi ik/\log q\) of \(\Theta_q\), the squared target samples are comparable to \(k^{-2}\), while
\[
|\Theta_p(z_k)|^2+|\Theta_{q^\beta}(z_k)|^2
\asymp\delta_{|k|}^2+\||k|\beta\|^2.
\]
The bounded lattice sampler proves necessity of (2). Its bounded right inverse lifts the minimum-norm sample split, and the remaining numerator is divisible by the pure Blaschke factor \(\Theta_q\), supplying the anchor component as well. Division by the common \(B\) takes place isometrically on its range, with the target \(b/s\) retained; the point \(s=1\) is removable and not a zero of \(\Theta_q\).

Consequently the infimum \(E_3(\beta)\) of the sum of all three squared physical component norms satisfies
\[
cS_\alpha(\beta)\le E_3(\beta)
\le C(1+S_\alpha(\beta))
\quad(\beta\in[1,2]),
\tag{21}
\]
with infinity meaning that no exact decomposition exists. The upper bound is a measurable constructive certificate. Equations (5) and (21) give an integrable certificate and therefore finite mean minimum cost; in particular \(\mu\{E_3>R\}\le C_\mu/R\). Measurability of the minimum also follows from weak compactness. Write each component as \(B\Theta_v U_v\). Bounded-energy triples of the \(U_v\) have weakly convergent subsequences; the multipliers in (20) and their adjoints vary strongly with \(\beta\), by boundary dominated convergence and Hardy projection. Thus their sums pass to the weak limit as \(\beta\) varies, while squared norms are weakly lower semicontinuous. The minimum is attained when finite, and its energy sublevel sets are closed.

The map \(\beta\mapsto q^\beta\) is bi-Lipschitz on compact parameter intervals, so (3) measures the size of the actual third-seed set as well. Removing \(\mathbb Q+\mathbb Q\alpha\) removes zero \(\mathcal H^{1/2}\)-measure only, proving the rank-three assertion. This excludes an interpretation of the exceptional set as merely duplicated or rationally dependent seed spaces.

## Prior art, mathematical delta, and limits

Mass transference and Frostman's lemma are classical; (18) is an immediate denominator-grid application of the former. The weighted return series in (9) is already in the family of Rivoal's [Lemma 3.2, p. 523](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0A03A2C7A347D4C9E76CF565FDE45DA5/S0013091510001069a.pdf/on-the-convergence-of-diophantine-dirichlet-series.pdf), with exponents \((1+s,2-s)\); (12) is a direct sufficient spacing bound, not a new scalar convergence criterion. The local addition is the complete-series integration against singular measures, the matching dimension bounds, and their transport to the Nyman target and physical completion cost. These claims are recorded as derived applications, with no claim to bibliographic priority for a general Diophantine dimension theorem.

Beresnevich–Ramírez–Velani, [Section 4.5 of *Metric Diophantine Approximation: aspects of recent work*](https://arxiv.org/pdf/1601.01948), describes the neighboring fixed-fiber metric setting. A simultaneous-approximation limsup theorem alone does not control the divergence set of the full positive series in (2); the Frostman first-moment argument supplies that step here. Burnol's [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055) provide the common inner factor and projected target used by the already-persisted interpolation bridge.

NB-366 decides Lebesgue-generic completion through the Brjuno condition. Here the stronger fixed-pair hypothesis (1) yields an exact size for its null failure set and extends successful seed selection to the singular measures (4). It does not settle exceptional completion for 2-Brjuno but non-Brjuno pairs.

- The exponent \(1/2\) in (3) is exact. The argument does not assert (5) at \(s=1/2\); the dyadic exponent in (10) loses positivity there. Neither support dimension alone nor a weaker concentration assumption substitutes for (4).
- For ratios failing (1), only the lower bound (18) is supplied here. In the non-Brjuno regime NB-366 instead makes \(\mathcal E_\alpha\) a full-measure set, so its dimension is one. A universal upper bound of \(1/2\) would be false.
- No assertion is made that a specified integer pair satisfies (1), or that a specified third seed completes it. A null exceptional set of positive Hausdorff dimension cannot exclude prescribed parameters.
- The orbit spaces allow unrestricted real dilation and closure. No finite generator count, bounded dilation range, uniform component budget, or bound on the discrete Nyman distance is established.
- Every orbit sum \(w\) still satisfies \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The Burnol floor and the RH question remain unchanged.

Evidence is the analytic derivation, the inspected primary mass-transference theorem, and the author-source Frostman theorem including its Borel extension. The decisive audits are the \(n^{1-s}\) concentration cost, the first-return bound in addition to pairwise spacing, the strict sign of \(\kappa\), control of the whole series rather than a single limsup, and the square-root change of radii in (18). No finite computation establishes the dimension claim; no Lean verification or independent adversarial approval is asserted.
