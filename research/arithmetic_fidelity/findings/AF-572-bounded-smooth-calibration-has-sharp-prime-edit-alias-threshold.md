# AF-572 — Bounded smooth calibration has a sharp prime-edit alias threshold

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · CALIBRATION-MISSPECIFICATION · EXACT-ALIASING · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Question and experiment

AF-571 obtains exact small-window identification with a minimal number of probes when the shared output drift is **exactly polynomial**. Allow a bounded smooth departure from that model. Does shrinking the observation window remove the departure faster than the source signal?

Retain the registered generalized-prime edit curves
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\qquad
h_p(s)=p^{-s}-(p+1)^{-s},\qquad
\Phi_p(a)=(P-h_p)^{-1}(E_1(a)),
\quad E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
\tag{1}
\]
Here \(p\) is an odd rational-prime edit location. Fix a known finite set
\(S=\{p_1<\cdots<p_m\}\), \(m\ge2\), and observe only \(0<a\le A\).
For a fixed integer \(n\ge1\) and \(L\ge0\), the nuisance class is
\[
\mathcal B_{n,L}(A)=
\{b\in C^n[0,A]:\ \|b^{(n)}\|_\infty\le L\}.
\tag{2}
\]
Thus \(b=q+u\), where \(q\in\Pi_{n-1}\), \(u^{(j)}(0)=0\) for \(0\le j<n\), and \(\|u^{(n)}\|_\infty\le L\). Lower-order polynomial coefficients are unrestricted. This is an additive output law in the fixed coordinate \(a\), not an arbitrary postcomposition or a bound invariant under rescaling that coordinate.

The observation is \(y(a)=\Phi_p(a)+b(a)+\eta(a)\), with one fixed \(b\) shared by all observations and \(|\eta(a)|\le\varepsilon\). Different hypothetical sources may have different nuisance functions in (2). Write \(\varepsilon_{\rm full}^{n,L}(A,S)\) and \(\varepsilon_k^{n,L}(A,S)\) for the supremal unique-identification noise radii from the full window and the best fixed \(k\)-point design. A radius of zero below includes explicit failure even at zero noise, not merely absence of a positive robustness margin.

## Sharp small-window threshold

Put \(G_i=\Phi_{p_{i+1}}-\Phi_{p_i}\), \(\sigma=(-1)^{n-1}\), and
\[
\beta_n(S)=\min_{i<m}|[a^n]G_i|,
\qquad L_{\rm crit}(S,n)=\frac{n!}{2}\beta_n(S).
\tag{3}
\]
There is a threshold on \(\min S\), depending only on \(n\), such that the following holds. Fix such an \(S\), and then fix \(L\).

**Below threshold:** if \(0\le L<L_{\rm crit}\), then for every sufficiently small \(A>0\),
\[
\boxed{
\varepsilon_{n+1}^{n,L}(A,S)
=\varepsilon_{\rm full}^{n,L}(A,S)
=\frac12\operatorname{dist}_{C[0,A]}
 \left(\sigma G_{i_*}-\frac{2L}{n!}a^n,\Pi_{n-1}\right)>0,
}
\tag{4}
\]
where \(i_*\) is a pointwise least signed \(n\)th-derivative adjacent gap on the small window. Moreover,
\[
\boxed{
\varepsilon_{\rm full}^{n,L}(A,S)
=\frac{\beta_n(S)-2L/n!}{4^n}A^n+O_{S,n,L}(A^{n+1}).
}
\tag{5}
\]
No policy with at most \(n\) queries can identify every source even at zero noise. Thus the minimal nonadaptive query count still captures the full reduced margin.

**At or above threshold:** if \(L\ge L_{\rm crit}\), then for every sufficiently small \(A>0\), two distinct candidates with admissible nuisance functions give the **same full observation curve**. Full-window and arbitrary adaptive identification both fail at zero noise. In particular,
\[
\boxed{\varepsilon_{\rm full}^{n,L}(A,S)=0.}
\tag{6}
\]
The equality case \(L=L_{\rm crit}\) is exact; it is not inferred from a vanishing leading term in (5).

As in AF-571, (4) is equality of suprema. A closed-window optimal design can use \(a=0\); admissible positive nodes approach its margin. Window thresholds depend on \(S,n,L\), and need not stay positive as \(L\uparrow L_{\rm crit}\). No simultaneous prime/window/degree limit is asserted.

## Derivative-constrained approximation certificate

For any two sources with gap \(g\), the distance between their noiseless observation classes is
\[
d_{n,L}(g)=\inf_{b\in\mathcal B_{n,2L}(A)}\|g-b\|_\infty,
\tag{7}
\]
because \(\mathcal B_{n,L}-\mathcal B_{n,L}=\mathcal B_{n,2L}\). The inclusion from right to left follows by writing \(b=b/2-(-b/2)\). The two-source noise radius is \(d_{n,L}(g)/2\): balls with radii \(\varepsilon\) about two curves intersect precisely when their separation is at most \(2\varepsilon\); infima give the same statement for supremal radii. For finitely many candidates take the least pairwise distance.

Suppose more generally that adjacent gaps \(g_i\in C^n[0,A]\) satisfy
\[
2L<\sigma g_{i_*}^{(n)}(a)\le\sigma g_i^{(n)}(a)
\quad\text{for every }a,i.
\tag{8}
\]
Let \(r=\sigma g_{i_*}-2La^n/n!\), and let \(q_*\in\Pi_{n-1}\) be its best uniform approximant, with error \(d>0\). Alternation supplies \(n+1\) nodes \(t_0<\cdots<t_n\). Set
\[
v_j=\prod_{k\ne j}(t_j-t_k)^{-1},\qquad
\lambda_j=\frac{v_j}{\sum_k|v_k|},\qquad
\Lambda f=\sum_j\lambda_j f(t_j),\qquad
\mu=\Lambda(a^n/n!)>0.
\tag{9}
\]
Then \(\|\Lambda\|=1\), \(\Lambda\Pi_{n-1}=0\), and \(\Lambda r=d\). The last sign follows from \(r^{(n)}>0\): the divided difference at the alternating nodes is positive, selecting the orientation of the alternating residual.

The divided-difference mean-value formula gives both
\[
\|b^{(n)}\|_\infty\le 2L
\ \Longrightarrow\ |\Lambda b|\le2L\mu,
\qquad
f^{(n)}\ge0\ \Longrightarrow\ \Lambda f\ge0.
\tag{10}
\]
Every source gap \(h\) in increasing source order is a sum of adjacent gaps. Thus (8) implies
\[
\Lambda(\sigma h-b)\ge
\Lambda(\sigma g_{i_*})-2L\mu=d
\quad(b\in\mathcal B_{n,2L}).
\tag{11}
\]
Consequently every pair has full-window distance at least \(d\), and the same holds already on these \(n+1\) nodes. For \(g_{i_*}\), the admissible approximant \(\sigma(2La^n/n!+q_*)\) attains error \(d\), giving a matching upper bound. This proves (4) under (8), without invoking a general existence theorem for derivative-constrained approximants.

If an endpoint node is zero, move it to a small positive value. The weights in (9), \(\mu\), and all finitely many source contrasts vary continuously. Bound (10) holds at the perturbed nodes too, so their worst-case margin tends to \(d\). This proves the legal-design supremum assertion despite the infinite-dimensional nuisance class.

The lower query bound survives unchanged: along any hypothetical all-zero transcript with at most \(n\) distinct queried coordinates, interpolate \(-\Phi_p\) separately for each candidate with a polynomial in \(\Pi_{n-1}\). These nuisances have zero \(n\)th derivative and belong to (2) for every \(L\). Every candidate realizes the same transcript, including for a deterministic adaptive policy. A guarantee for every realization of a randomized policy cannot evade this obstruction either.

## Prime-edit jets decide the threshold, including equality

AF-571 proves, for every fixed order \(k\), uniformly over all \(q>p\to\infty\),
\[
[a^k](\Phi_q-\Phi_p)
=(-1)^{k-1}\frac{c^k}{(k-1)!}
 \delta_{p,q}(\log p)^{k-1}
 [1+O_k(1/\log p)],
\quad
c=e^{B_1},\quad
\delta_{p,q}=\frac1{p(p+1)}-\frac1{q(q+1)}>0.
\tag{12}
\]
For \(k=1\) the relative error is \(O(p^{-2})\). Here \(B_1\) is the Meissel--Mertens constant. The formula comes from differentiating the exact inverse equation with respect to the real edit parameter and integrating its positive sensitivity, not subtracting independent asymptotic errors. Its load-bearing ingredients can be checked directly: \(B_v(a)=\Phi_v(a)-1=K_va+O(a^2)\), \(K_v=ce^{-1/[v(v+1)]}\), and
\[
\partial_v B_v(a)=
\frac{B_v(a)w_v(1+B_v(a))}
 {1-B_v(a)\{R'(B_v(a))-h_v'(1+B_v(a))\}},
\quad
w_v(s)=s(s+1)\int_v^{v+1}u^{-s-2}\,du,
\tag{13}
\]
where \(R(x)=P(1+x)+\log x\) is analytic near zero. In \(\partial_v B_v/w_v(1)\), the top power of \(\log v\) at order \(a^k\) comes from \(e^{-B_v(a)\log v}\), with coefficient \(K_v^k(-\log v)^{k-1}/(k-1)!\). The positive \(w_v(1)\asymp v^{-3}\) weight controls the integrated logarithmic moments uniformly in the upper edit location. This reconstructs the sign information needed here.

Apply (12) at **both orders \(n\) and \(n+1\)**, increasing the prime threshold if necessary. For every adjacent gap,
\[
\sigma G_i^{(n)}(0)>0,
\qquad \sigma G_i^{(n+1)}(0)<0.
\tag{14}
\]
On a sufficiently small common interval, each signed \(n\)th derivative is positive and strictly decreasing. Analyticity and finiteness of \(S\) also give a total pointwise ordering of these derivatives: the difference of any two analytic germs either vanishes or has a fixed sign sufficiently close to zero. This ordering includes ties at the endpoint. A pointwise least gap must have the least endpoint derivative \(n!\beta_n(S)\).

If \(L<L_{\rm crit}\), continuity makes all these derivatives exceed \(2L\) on a small window, giving (8). Taylor expansion modulo \(\Pi_{n-1}\) gives
\[
r(a)=q(a)+(\beta_n(S)-2L/n!)a^n+O_{S,n,L}(a^{n+1}).
\]
The classical shifted-Chebyshev identity
\(\operatorname{dist}_{C[0,1]}(t^n,\Pi_{n-1})=2^{1-2n}\), followed by the noise-ball factor \(1/2\), yields (5).

If \(L\ge L_{\rm crit}\), choose an adjacent gap \(G_j\) attaining the minimum in (3). Positivity and decrease from (14) imply
\[
\|G_j^{(n)}\|_{C[0,A]}=n!\beta_n(S)\le2L
\tag{15}
\]
on a sufficiently small window. The two admissible nuisances
\(b_{p_j}=G_j/2\) and \(b_{p_{j+1}}=-G_j/2\) therefore produce the identical curve
\[
\Phi_{p_j}+b_{p_j}
=\Phi_{p_{j+1}}+b_{p_{j+1}}
=\frac{\Phi_{p_j}+\Phi_{p_{j+1}}}{2}.
\tag{16}
\]
The opposing signs at successive boundary orders in (14) are essential to the **equality-case** conclusion. As a countercontrol, take the generic analytic gap \(g(a)=2La^n/n!+a^{n+1}\). Although \(g^{(n)}(0)=2L\), any \(n+1\) distinct positive nodes give \(\Lambda(g-b)\ge\Lambda(a^{n+1})>0\) for all \(b\in\mathcal B_{n,2L}\), using (10). Thus this increasing-derivative gap retains a positive higher-order margin at its boundary threshold. The prime-edit equality case cannot be obtained from the leading jet alone.

## Calibration budget and evidence boundary

For a two-source set, (12) gives the source-specific threshold
\[
\boxed{
L_{\rm crit}(\{p,q\},n)
=\frac{n c^n}{2}\delta_{p,q}(\log p)^{n-1}
 [1+O_n(1/\log p)].
}
\tag{17}
\]
For a finite set take the least adjacent threshold. Since \(\delta_{p,q}\le p^{-2}\), every fixed positive smooth-drift budget \(L\) eventually exceeds this threshold for sufficiently remote edit locations. After fixing such a source set, further shrinking the window cannot restore identification. This is exact overlap of admissible observation classes, not just poor numerical conditioning or a proof-search failure. The statement is local in the window; it does not show overlap on an arbitrary preassigned larger interval.

For \(n=2\), \(L\) bounds unknown calibration curvature. AF-570's \(\beta(S)A^2/16\) becomes \((\beta(S)-L)A^2/16+O(A^3)\) when \(L<\beta(S)\), and full-window identification fails exactly for \(L\ge\beta(S)\) on sufficiently small windows. For \(L=0\), (4)--(5) recover AF-571. The small residual estimate \(\|u\|_\infty\le LA^n/n!\) does not make model misspecification negligible: it has the same window power as the quotient-visible source signal.

The approximation tools are classical. De Boor (2005) supplies the divided-difference machinery; the Chebyshev minimax constant is recorded in DLMF §18.38(i). Mironenko (2017; English translation 2018) studies the broader uniform-approximation problem with a bounded highest derivative and perfect splines. Wiens (2009, §2) explicitly treats overlapping model-neighbourhoods as an obstruction in robust model discrimination, in a different stochastic design setting. These are prior art, not new Mathia mechanisms. The source-specific result is the exact smooth-calibration threshold (17), its **noiseless alias at equality** from the alternating prime-edit jets, and the survival of the minimal-probe full-margin certificate strictly below threshold. No general approximation or robust-design priority claim is made.

Audit controls are the factor \(2L\) from two hypothetical calibrations, the separate factor \(1/2\) from bounded observation noise, the \(n!\) relating Taylor coefficients to derivatives, the sign of the order-\(n+1\) boundary jet, and continuity of the nuisance dual bound when the excluded zero node is moved. Exact rational checks at the shifted Chebyshev nodes for \(n=1,2,3\) give normalized \(a^n\) moments \(1/2,1/8,1/32\), hence radius constants \(1/4,1/16,1/64\); these are checks of the proof constants, not numerical evidence for an unproved prime statement.

The nuisance is shared within one experiment but unknown across hypotheses. If it is independently measured, restricted further, or forced to be the same known function across competing sources, the overlap argument need not apply. Bounds are stated in the retained coordinate \(a\); changing coordinate also changes the derivative budget. The candidates remain generalized-prime matched controls indexed by genuine rational primes. No discriminator of the ordinary prime system against all generalized-prime systems, nonvanishing absolute noise margin, or RH implication follows.
