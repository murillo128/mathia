# AF-569 — Affine output drift forces four adaptive prime-edit probes

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-EDIT · AFFINE-OUTPUT-QUOTIENT · ADAPTIVE-IDENTIFICATION · THREE-PROBE-OBSTRUCTION · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## The experiment and the sharp four-query budget

Retain AF-559/AF-562's commonly registered critical prime-edit profiles, with odd rational-prime **edit locations** \(S=\{p_1<\cdots<p_m\}\), \(m\ge2\):
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
Q_p(s)=P(s)-[p^{-s}-(p+1)^{-s}],\quad
\Phi_p(a)=Q_p^{-1}(E_1(a)),\quad
E_1(a)=\int_a^\infty e^{-v}\frac{dv}{v}.
\tag{1}
\]
The edited systems are generalized-prime matched controls, **not** different rational-prime systems. Relative to AF-568's unknown constant origin, add an unrestricted affine output calibration shared across observations of one unknown source:
\[
y_j=\Phi_{p_i}(a_j)+b_0+b_1a_j+\eta_j,\qquad
b_0,b_1\in\mathbb R,\quad |\eta_j|\le\varepsilon.
\tag{2}
\]
Different hypothetical sources may use different \(b_0,b_1\), but each source uses the *same* pair throughout the experiment. Query coordinates are positive and unrestricted and may be selected adaptively from previous readings. Errors may vary adversarially at each query.

Set
\[
G_i(a)=\Phi_{p_{i+1}}(a)-\Phi_{p_i}(a)>0,\quad
D_i=\sup_{a>0}G_i(a),\quad d(S)=\min_{i<m}D_i.
\tag{3}
\]
Let \(\varepsilon^{\rm aff}_{\rm full}(S)\), \(\varepsilon^{\rm aff}_k(S)\), and \(\varepsilon^{\rm aff,ad}_k(S)\) be the supremal worst-case unique-identification noise radii for the whole curve, at most \(k\) fixed coordinates, and at most \(k\) adaptive coordinates, respectively.

**Theorem.** There is an absolute \(P_0\) such that every finite set \(S\) with \(\min S\ge P_0\) satisfies
\[
\boxed{\varepsilon^{\rm aff,ad}_4(S)
=\varepsilon^{\rm aff}_{\rm full}(S)=\frac{d(S)}4.}
\tag{4}
\]
The full-curve identity holds for *every* finite \(S\), without the eventual restriction. One or two observations cannot identify an arbitrary source even with zero noise, since an unrestricted affine law fits any two distinct readings.

For every finite \(S\), three-query adaptivity supplies **no improvement** over a fixed three-coordinate design:
\[
\boxed{
\varepsilon^{\rm aff,ad}_3(S)=\varepsilon^{\rm aff}_3(S)
=\frac14\sup_{0<a_0<a_1<a_2}
\min_{i<j}\left|
G_{i,j}(a_1)
-\frac{a_2-a_1}{a_2-a_0}G_{i,j}(a_0)
-\frac{a_1-a_0}{a_2-a_0}G_{i,j}(a_2)
\right|,
}
\tag{5}
\]
where \(G_{i,j}=\Phi_{p_j}-\Phi_{p_i}\).

Moreover there are sets \(S_n\) of **four actual odd rational-prime edit locations**, with \(\min S_n\to\infty\), for which
\[
\limsup_{n\to\infty}
\frac{\varepsilon^{\rm aff,ad}_3(S_n)}
     {\varepsilon^{\rm aff}_{\rm full}(S_n)}
\le\kappa<1,
\tag{6}
\]
with the explicit, source-independent variational constant
\[
\kappa=
\sup_{0\le x_0<x_1<x_2<\infty}
\min\{|C_f(x_0,x_1,x_2)|,\ |C_g(x_0,x_1,x_2)|\},
\quad
f(x)=xe^{1-x},\quad g(x)=f(3x/2),
\tag{7}
\]
and
\[
C_h(x_0,x_1,x_2)
=h(x_1)-\frac{x_2-x_1}{x_2-x_0}h(x_0)
-\frac{x_1-x_0}{x_2-x_0}h(x_2).
\tag{8}
\]
In particular \(\rho\le\kappa<1\), where \(\rho=(8e/9)\log(3/2)\) is AF-562's one-sample maximin value; **no numerical or exact evaluation of \(\kappa\) is asserted**. Thus three adaptive probes are not universally full-margin, whereas four are: the affine nuisance costs one more observation than AF-568's free constant offset.

## Full-curve affine quotient equals the constant-offset quotient

AF-559 proves that \(G_{i,j}(a)>0\) is bounded and tends to zero at both \(a\downarrow0\) and \(a\to\infty\). In comparing the two hypotheses under arbitrary affine output laws, the center separation modulo their nuisance difference is
\[
\inf_{\alpha,\beta\in\mathbb R}
\sup_{a>0}|G_{i,j}(a)-\alpha-\beta a|.
\tag{9}
\]
Every \(\beta\ne0\) gives an infinite supremum, because \(G_{i,j}\) is bounded on the entire unbounded positive axis. For \(\beta=0\), best constant approximation to a positive function of infimum zero and supremum \(D_{i,j}\) has error \(D_{i,j}/2\). The two uniform error balls intersect at radius half of that quotient distance, giving \(D_{i,j}/4\). Pointwise ordering and the sum of positive adjacent gaps show
\[
\min_{i<j}D_{i,j}=\min_i D_i=d(S).
\tag{10}
\]
This proves \(\varepsilon^{\rm aff}_{\rm full}(S)=d(S)/4\), and the same pairwise midpoint transcript after optimal constant shifts defeats *any* adaptive policy at \(\varepsilon=d(S)/4\).

The unrestricted domain matters: on a bounded observation interval a nonzero affine slope can improve best uniform approximation, so neither (9) nor its radius should be transported unaltered to a bounded-window experiment.

## Exact three-query affine contrast and absence of adaptation gain

Fix ordered distinct coordinates \(a_0<a_1<a_2\) and put \(t=(a_2-a_1)/(a_2-a_0)\in(0,1)\). The contrast
\[
R(y)=y(a_1)-t\,y(a_0)-(1-t)y(a_2)
\tag{11}
\]
annihilates both the constant and linear nuisance terms. Under source \(i\), its noiseless center is \(R(\Phi_{p_i})\) and its error satisfies
\[
|R(\eta)|\le(1+t+(1-t))\varepsilon=2\varepsilon.
\tag{12}
\]
The full interval \([-2\varepsilon,2\varepsilon]\) is attainable by bounded errors. Since the affine nuisance subspace of triples at distinct coordinates is exactly \(\ker R\), a given observed triple is compatible with source \(i\) **if and only if** its contrast differs from \(R(\Phi_{p_i})\) by at most \(2\varepsilon\). Thus a pair is indistinguishable exactly when its contrast centers differ by at most \(4\varepsilon\), proving the fixed-design part of (5).

For an adaptive protocol, the first observation may be any real number under every source, by choosing \(b_0\). Conditional on any first reading, a second reading at a *distinct* chosen coordinate is also completely arbitrary under every source: choose \(b_1\) and then \(b_0\) to interpolate the pair exactly. Conditional on **any two such readings**, all hypotheses therefore reach the third coordinate with the same possible histories; the third reading's possible intervals are separated only by (11), with the same \(4\varepsilon\) compatibility threshold. Each resulting triple is itself a permitted fixed design. An adaptive strategy cannot outperform the supremum over fixed triples, while a fixed triple is an adaptive strategy. Repeated first/second coordinates cannot improve identification: they provide only repeated errors at one location, leaving the affine slope unrestricted and at most two distinct coordinates after the third observation. This proves (5).

## Four adaptive queries: two nuisance anchors, one locator, one targeted separator

Fix any \(0\le\varepsilon<d/4\). AF-563 provides a known-set locator \(a_*\) for sufficiently large \(\min S\) such that
\[
\min_iG_i(a_*)>(\rho-o(1))d>d/2.
\tag{13}
\]
Choose \(\delta>0\) with \(\min_iG_i(a_*)>d/2+\delta\) and \(2\delta<d-4\varepsilon\). Because \(S\) is finite and all adjacent gaps tend to zero at *both* endpoints, choose \(0<a_L<a_*<a_R\) such that
\[
\max_i\{G_i(a_L),G_i(a_R)\}<\delta,
\tag{14}
\]
and \(a_R\) is beyond one chosen near-maximum of every \(G_i\). All selections depend only on the known set and the announced noise bound, not on the unknown source or its nuisance.

Query \(a_L\) and \(a_R\) first. For any interior \(a\), let
\[
w_L(a)=\frac{a_R-a}{a_R-a_L},\quad
w_R(a)=\frac{a-a_L}{a_R-a_L},\quad
Z(a)=y(a)-w_L(a)y(a_L)-w_R(a)y(a_R).
\tag{15}
\]
Both affine nuisance parameters cancel exactly and \(w_L,w_R\in[0,1]\), \(w_L+w_R=1\). The noise in \(Z(a)\) is bounded by \(2\varepsilon\). Let \(z_i(a)\) be its noiseless source center. From (14), for every adjacent pair and every interior \(a\),
\[
G_i(a)-\delta
<z_{i+1}(a)-z_i(a)\le G_i(a).
\tag{16}
\]
Query \(a_*\) third. Its adjacent center gaps are \(>d/2\). Any actual \(Z(a_*)\) is within \(2\varepsilon\) of the true center; since \(4\varepsilon<d\), no three ordered centers can be compatible (their span exceeds \(d\)). The version space contains either one source or two adjacent sources.

If two remain, say \(i,i+1\), select as fourth coordinate a near-maximum \(a_i^\sharp\in(a_L,a_R)\) with \(G_i(a_i^\sharp)>d-\delta\). By (16),
\[
z_{i+1}(a_i^\sharp)-z_i(a_i^\sharp)>d-2\delta>4\varepsilon.
\tag{17}
\]
The same two anchor readings remove the nuisance in this fourth contrast; its error is bounded by \(2\varepsilon\), so the candidate intervals are disjoint. Four readings identify the source for *every* admissible noise sequence. Together with the full-curve upper bound this proves (4). Correlation induced by reusing the anchor errors cannot invalidate decoding, because the fourth-step disjointness uses a necessary marginal error bound only.

This is a reusable ordered-profile result: (4) follows for any finite pointwise-ordered source family with adjacent positive gaps vanishing at two accessible endpoints, finite peak suprema, and one locator where all gaps exceed half their minimum full peak. The rational-prime input is precisely AF-563's *uniform* locator, not a generic feature of all inverse problems.

## Actual-prime four-location witness that three queries do not saturate

Use AF-562's unconditional PNT construction of four odd rational primes \(p<r<q<t\), with two equally tight but separated gaps. Write \(d_n=d(S_n)\), \(c=e^{B_1}\), and \(x=ca\log p\). AF-559/AF-562 give *uniformly in \(a>0\)*, along this family,
\[
G_{p,r}(a)/d_n=f(x)+o(1),\qquad
G_{q,t}(a)/d_n=f(3x/2)+o(1).
\tag{18}
\]
Since the interpolation coefficients in (8) are nonnegative and sum to one, uniform \(o(1)\) errors remain \(o(1)\) after forming either affine contrast, **uniformly over moving triples** of query coordinates. Restricting the pairwise minimum in (5) to those two bottleneck pairs therefore yields (6) with the variational constant (7).

To prove \(\kappa<1\) without an unsupported numerical maximization, suppose triples could make *both* contrast magnitudes tend to one. Both \(f\) and \(g\) take values in \([0,1]\), vanish at zero and infinity, are positive in between, and have **distinct unique maximizers** \(1\) and \(2/3\). Write \(u_h=h(x_1)\) and \(v_h=t h(x_0)+(1-t)h(x_2)\), each in \([0,1]\), with \(t=(x_2-x_1)/(x_2-x_0)\). If \(|u_h-v_h|\to1\), pass to a subsequence of constant sign: either \(u_h\to1,v_h\to0\) (positive sign), or \(u_h\to0,v_h\to1\) (negative sign).

If both \(f,g\) have positive sign, the single middle point must approach both distinct maximizers, impossible. If signs differ, the middle point must approach the maximizer of one function while the other tends to zero there, also impossible because each is strictly positive at the other's maximizer. If both signs are negative, both convex combinations \(v_f,v_g\) tend to one. At least one endpoint carries interpolation weight at least \(1/2\); along a further subsequence the same endpoint does so each time. Both \(f\) and \(g\) must tend to one at that endpoint, again impossible for distinct unique maximizers. These exhaustive cases contradict simultaneous unit contrasts, proving \(\kappa<1\).

For the lower comparison \(\kappa\ge\rho\), take \(x_0\downarrow0\), \(x_2\to\infty\), and \(x_1=2\log(3/2)\). Both endpoint interpolants vanish in the limit and \(f(x_1)=g(x_1)=\rho\). No equality \(\kappa=\rho\), decimal estimate, or sharper obstruction is needed for the strict universal three-versus-four theorem.

## Prior art, falsification tests, and boundaries

Eliminating an affine nuisance by a three-point interpolation residual, the minimax \(L^\infty\) quotient, and sequential model discrimination are classical techniques. Chebyshev's best-uniform-approximation/alternation theory gives their standard approximation-theoretic setting, while Atkinson--Cox (1974) and Rosa--Harman (2016), already anchored under AF-568 in SOURCES.md, establish model-discrimination and nuisance-resistant design precedents. These sources do **not** establish this source-specific four-prime, three-versus-four adaptive budget. The derivation of the bounded-noise contrast and \(\kappa<1\) is given here, without a general-method priority claim.

Key checks: the pairwise full-curve radius is \(d/4\), not \(d/2\); a fitted nonzero affine slope is ruled out only by the **unbounded observation domain**; the three-point residual has noise magnitude at most \(2\varepsilon\), hence pairwise compatibility threshold \(4\varepsilon\); the initial two readings convey no source information because **both** affine nuisance coefficients are unrestricted; the four-query anchors must have simultaneously negligible gaps for *every* member of the known finite set; the first decisive locator must exceed **half** the bottleneck peak, not merely be positive; the adversary's errors are independent but not assumed identical; and the strict \(\kappa<1\) proof handles both signs of an affine contrast, even when a query drifts to infinity.

The theorem has no finite-index, bounded-coordinate, unknown-source-family, random-noise, or independently re-calibrated-query extension built in. In particular a freely *different* affine drift at each observation defeats the shared-nuisance cancellation. The full and finite margins can vanish as the prime locations grow. These generalized-prime matched controls do not separate rational primes from arbitrary generalized primes, and no RH implication follows without an independent faithful and stable arithmetic-to-zeros transfer.

## Consequence for Arithmetic Fidelity

The number of shared nuisance parameters can change the **minimal adaptive sensing budget** without changing the full-curve quotient radius: for these source profiles, known calibration needs two probes (AF-567), an unknown constant offset needs three (AF-568), and an unknown affine output law needs four. The extra adaptive observation is not a generic parameter-count slogan: it is certified by an explicit four-rational-prime obstruction, an exact three-point quotient formula, and a source-uniform locator. Recovering the erased calibration structure from an actual downstream mathematical representation remains a separate question.
