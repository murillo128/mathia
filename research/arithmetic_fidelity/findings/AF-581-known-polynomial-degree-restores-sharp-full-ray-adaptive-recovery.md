# AF-581 — Known polynomial degree restores sharp full-ray adaptive recovery

## Status

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · SHARP-ADAPTIVE-BUDGET · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## The degree promise changes the positive-noise stopping boundary

AF-580 rules out reliable finite stopping under unknown, unbounded polynomial calibration degree, even below a positive full-ray noise margin. A **known finite degree bound** changes that conclusion. On the full positive ray, every fixed degree has the same sharp one-extra-adaptive-probe phenomenon previously established only for constant and affine drift in AF-568/569.

Use the registered prime-edit curves
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad
 \Phi_p(a)=(P-h_p)^{-1}(E_1(a)),\qquad
 E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
 \tag{1}
\]
For a known finite set of odd rational-prime edit locations
\(S=\{p_1<\cdots<p_m\}\), observe
\[
 y(a)=\Phi_{p_i}(a)+b(a)+\eta(a),\qquad
 b\in\Pi_r,\quad |\eta(a)|\le\varepsilon,\quad a>0.
 \tag{2}
\]
Here \(r\) is a known nonnegative integer and \(\Pi_r\) denotes the real polynomials of degree at most \(r\). Coefficients are unrestricted, and one polynomial is shared by every reading of an input. Different source hypotheses may use different polynomials. The proofs also permit adversarial errors at individual queries. No error independence, centering or averaging is assumed.

Write \(\varepsilon_k^{[r]}(S)\) and \(\varepsilon_k^{[r],{\rm ad}}(S)\) for the supremal noise radii allowing guaranteed identification by at most \(k\) fixed or deterministic adaptive queries. These are worst-case guarantees, not randomized success probabilities. Put
\[
 G_i=\Phi_{p_{i+1}}-\Phi_{p_i},\quad
 d(S)=\min_{i<m}\sup_{a>0}G_i(a),\quad
 \rho=\frac{8e}{9}\log\frac32=0.9797052759\ldots.
 \tag{3}
\]

**Theorem.** For each known finite \(r\), and every finite \(S\) with sufficiently large \(\min S\),
\[
 \boxed{\varepsilon_{r+3}^{[r],{\rm ad}}(S)
 =\varepsilon_{\rm full}^{[r]}(S)=\frac{d(S)}4.}
 \tag{4}
\]
The full-curve identity holds for every finite \(S\). For every such set,
\[
 \varepsilon_{r+2}^{[r],{\rm ad}}(S)
 =\varepsilon_{r+2}^{[r]}(S),
 \tag{5}
\]
and the sharp worst-family ratio is, for each fixed \(r\),
\[
 \boxed{\lim_{P_0\to\infty}
 \inf_{\substack{S\ {\rm finite\ odd\ primes},\ |S|\ge2\\\min S\ge P_0}}
 \frac{\varepsilon_{r+2}^{[r],{\rm ad}}(S)}
      {\varepsilon_{\rm full}^{[r]}(S)}=\rho.}
 \tag{6}
\]
The same four-prime families as AF-562 realize the upper limit for every fixed \(r\). Thus \(r+3\) is the smallest budget that universally captures the full margin in this regime. At most \(r+1\) queries cannot identify even two labels at zero noise.

The new ingredients are a polynomial-annihilating anchor construction whose noise norm approaches that of a constant-offset contrast, and a signed-measure certificate that bounds **all** higher-degree one-dimensional quotient contrasts. Merely counting nuisance coefficients would prove neither (4) nor (6).

## Full-curve geometry and the one-dimensional query quotient

AF-559/579 establish that each ordered gap \(G_{i,j}=\Phi_{p_j}-\Phi_{p_i}\) is positive, bounded, and vanishes at both ends of the ray. Every nonconstant polynomial has infinite uniform error against a bounded function on this domain. Consequently
\[
 \operatorname{dist}_{L^\infty(0,\infty)}(G_{i,j},\Pi_r)
 =\inf_c\|G_{i,j}-c\|_\infty
 =\frac12\sup G_{i,j}.
 \tag{7}
\]
Nonadjacent gaps are sums of positive adjacent gaps, so the minimum pair distance is \(d(S)/2\). Dividing by two for intersection of two noise balls proves the full-curve part of (4). At \(\varepsilon=d(S)/4\), a closest constant-shifted pair has a common midpoint observation, defeating even full-curve identification. All equalities of radii below concern suprema, with guarantees strictly below their endpoint.

At \(r+2\) distinct nodes \(a_0,\ldots,a_{r+1}\), polynomial evaluations have codimension one. Choose their annihilator \(\lambda\) with
\[
 \sum_{k=0}^{r+1}|\lambda_k|=1,\qquad
 \sum_k\lambda_k a_k^j=0\quad(0\le j\le r).
 \tag{8}
\]
For example, normalize the divided-difference weights
\(\prod_{l\ne k}(a_k-a_l)^{-1}\). The exact discrete quotient distance of a gap is \(|\sum_k\lambda_kG(a_k)|\): the quotient is one-dimensional and the dual norm is normalized by (8). Equivalently, the attainable contrast errors fill \([-\varepsilon,\varepsilon]\). Thus the fixed-design radius is
\[
 \frac12\min_{i<j}\left|\sum_k\lambda_kG_{i,j}(a_k)\right|.
 \tag{9}
\]

Adaptivity supplies no gain with only \(r+2\) readings. For any first \(r+1\) distinct coordinates and any reported values \(v_0,\ldots,v_r\), every source is feasible because its polynomial can interpolate those values, even at zero noise. Let \(l_k(a)\) interpolate at those first coordinates. Conditional on that prefix, the possible final values under label \(i\) form exactly the interval centered at
\[
 \sum_k l_k(a)v_k+F_i(a)-\sum_k l_k(a)F_i(a_k)
\]
with radius \(\varepsilon(1+\sum_k|l_k(a)|)\), where \(F_i=\Phi_{p_i}\). Any extremal combination of prefix errors is permitted, with a polynomial fitted to the resulting prefix; this verifies exact attainability, not just an upper bound. The selected final coordinate and this prefix therefore give a fixed design with the same separation test (9). If the adaptive policy works for all inputs, that fixed design must separate all labels. Conversely fixed designs are adaptive policies, proving (5). Repetitions or earlier stopping leave at most \(r+1\) distinct coordinates and admit a noiseless polynomial-interpolation alias. This argument does not choose an adversary after a random seed; randomized probabilistic guarantees are outside the theorem.

## Escaping anchors remove a fixed polynomial at asymptotic noise cost two

The following construction applies to any finite ordered family whose adjacent gaps are bounded and tend to zero at zero. Fix a finite set \(K\subset(0,\infty)\) of potential informative coordinates. Choose one small anchor \(L<\min K\) and, for \(r\ge1\), the remaining anchors
\[
 t_0=L,\qquad t_k=kR\quad(1\le k\le r).
 \tag{10}
\]
For the Lagrange weights \(l_k^{L,R}(a)\), uniformly on \(K\) as \(R\to\infty\) with \(L,r,K\) fixed,
\[
 l_0^{L,R}(a)=\prod_{k=1}^r\frac{a-kR}{L-kR}\longrightarrow1,
 \qquad l_k^{L,R}(a)=O_{L,r,K}(R^{-1})\quad(k\ge1),
 \qquad \Lambda_{L,R}(a):=\sum_{k=0}^r|l_k^{L,R}(a)|\longrightarrow1.
 \tag{11}
\]
For \(k\ge1\), the factor \((a-L)/(kR-L)\) gives \(R^{-1}\), while all other factors stay bounded. For \(r=0\), simply take \(l_0=1\). Every degree-at-most-\(r\) polynomial is reproduced **exactly** at every finite \(R\).

For any bounded gap \(G\),
\[
 \sum_{k=0}^r l_k^{L,R}(a)G(t_k)\longrightarrow G(L).
 \tag{12}
\]
Consequently, by first taking \(L\) small and then \(R\) large, the common anchors make both the source correction in (12) and \(\Lambda-1\) arbitrarily small, simultaneously for all adjacent gaps and all \(a\in K\). Boundedness alone controls the remote terms; tail decay is not required for this particular lemma.

After the \(r+1\) anchor readings form
\[
 Z(a)=y(a)-\sum_k l_k^{L,R}(a)y(t_k),\quad
 z_i(a)=F_i(a)-\sum_k l_k^{L,R}(a)F_i(t_k).
 \tag{13}
\]
The nuisance cancels exactly and
\[
 |Z(a)-z_i(a)|\le\varepsilon(1+\Lambda_{L,R}(a)),\qquad
 z_{i+1}(a)-z_i(a)=G_i(a)+o(1).
 \tag{14}
\]
For higher degree the interpolation weights can be negative. Replacing \(\Lambda\) by one at finite \(R\) would be wrong; (11) is precisely the needed stability statement. Vanishing weights on remote coordinates can still annihilate large polynomial moments, so this is not convergence of those moments to the constant-offset experiment.

## One locator and one pair-specific follow-up

Suppose a finite ordered family has a known locator \(a_*\) satisfying
\[
 \gamma:=\min_iG_i(a_*)>d/2,\qquad d=\min_i\sup G_i>0.
 \tag{15}
\]
Fix \(\varepsilon<d/4\). Choose \(\nu>0\) and a source-error tolerance \(\tau>0\) small enough that
\[
 \gamma-\tau>\varepsilon(2+\nu),\qquad
 d-2\tau>2\varepsilon(2+\nu).
 \tag{16}
\]
These strict inequalities are possible because \(\gamma>d/2>2\varepsilon\) and \(d>4\varepsilon\). For each adjacent pair choose a finite \(a_i^\sharp\) with \(G_i(a_i^\sharp)>d-\tau\). Apply (10)--(12) to
\(K=\{a_*\}\cup\{a_i^\sharp\}\), arranging \(\Lambda\le1+\nu\) and absolute source correction below \(\tau\).

Query the anchors, then \(a_*\). Every label-compatible center lies within \(E=\varepsilon(2+\nu)\) of \(Z(a_*)\). Adjacent centers are separated by more than \(\gamma-\tau>E\); three centers, or two nonadjacent centers, therefore cannot fit in an interval of length \(2E\). At most two adjacent labels survive. If two remain, query their \(a_i^\sharp\). Their new centers differ by more than \(d-2\tau>2E\), so their error intervals are disjoint. Reusing the anchors correlates the contrast errors, but these necessary marginal bounds already suffice for identification.

This uses at most \(r+3\) values. AF-563 supplies (15) uniformly for all sufficiently remote finite prime-edit sets, since it proves a locator with \(\gamma/d\ge\rho-o(1)>1/2\). It proves (4) without a cardinality or logarithmic-diameter restriction on \(S\).

Using only the anchors and locator instead gives a fixed \(r+2\)-query radius approaching \(\gamma/4\). To see this directly, the adjacent unnormalized contrasts in (14) approach \(G_i(a_*)\), their noise norm approaches two, and every nonadjacent contrast is a sum of positive adjacent ones. For fixed \(S,r\) the anchors can approach the required limits independently of the prime asymptotics. AF-563 therefore gives the lower bound \(\rho\) in (6).

## A signed-measure certificate gives the degree-independent sharp obstruction

Put
\[
 f(x)=xe^{1-x},\qquad g(x)=f(cx),\qquad
 c=3/2,\quad x_*=2\log c,\quad f(x_*)=g(x_*)=\rho.
 \tag{17}
\]
For **every finite signed measure** \(\mu\) on \([0,\infty)\) satisfying
\(\mu([0,\infty))=0\) and \(\|\mu\|_{\rm TV}=1\),
\[
 \boxed{\min\{|\mu(f)|,|\mu(g)|\}\le\rho/2.}
 \tag{18}
\]
This removes the three-node restriction of AF-569's contrast bound. No higher moment constraints or support-size assumptions are needed.

**Same-sign case.** Since \(1/c<x_*<1\), the coefficient
\[
 \theta=\frac{c-1/x_*}{c-1}\in(0,1)
\]
makes \(h=\theta f+(1-\theta)g\) stationary at \(x_*\). Both profiles increase before \(1/c\) and decrease after one. On \([1/c,1]\), both are strictly concave: \(f''(x)=e^{1-x}(x-2)<0\) and \(g''(x)=c^2e^{1-cx}(cx-2)<0\). Hence
\[
 0\le h(x)\le h(x_*)=\rho\quad(x\ge0).
 \tag{19}
\]
The positive and negative Jordan masses of \(\mu\) are each \(1/2\), so \(|\mu(h)|\le\rho/2\). If \(\mu(f)\) and \(\mu(g)\) have the same sign and both magnitudes exceed \(\rho/2\), their convex combination contradicts this bound.

**Opposite-sign case.** One has \(\sup_{u>0}|u f'(u)|\le1\). For \(u\le1\), this follows from \(u e^{1-u}(1-u)\le f(u)\le1\). For \(u=1+t\ge1\), it follows from
\[
 e^t-t(t+1)\ge1-t^2/2+t^3/6\ge1/3\quad(t\ge0),
 \tag{20}
\]
where the last cubic has its minimum at \(t=2\). Integration along dilation yields
\[
 \|f-g\|_\infty\le\int_1^c\frac{ds}{s}=\log c<\rho.
 \tag{21}
\]
Opposite-sign integrals both larger in magnitude than \(\rho/2\) would give \(|\mu(f-g)|>\rho\), contradicting (21) and the TV normalization. This proves (18). The constant is sharp: \(\mu=(\delta_{x_*}-\delta_0)/2\) attains equality. If zero is excluded, positive nodes approaching it give the same supremum.

For any \(r+2\)-node design, (8) defines such a measure after the common positive rescaling of the coordinates. Write \(G_{p,q}=\Phi_q-\Phi_p\) for edit locations and let \(B_1\) be the reciprocal-prime Meissel--Mertens constant. AF-562 constructs four actual rational primes \(p<q<u<v\) with two adjacent bottleneck gaps such that, uniformly for all \(a>0\),
\[
 \frac{G_{p,q}(a)}{d(S)}=f(e^{B_1}a\log p)+o(1),\qquad
 \frac{G_{u,v}(a)}{d(S)}=g(e^{B_1}a\log p)+o(1).
 \tag{22}
\]
For clarity, that construction uses a consecutive gap \(q-p=s=O(\log p)\), sets \(Q=p^{3/2}/(2\sqrt{s})\), and takes primes \(u\sim Q\), \(v\sim2Q\). PNT gives these choices. AF-559's uniform peak formula makes both outer peaks asymptotic to \(2s/(ep^3\log p)\), while the middle peak is much larger; \(\log u/\log p\to3/2\). Thus normalization by the actual \(d(S)\) gives (22).

The TV-one normalization carries the uniform \(o(1)\) through **every** design, including ill-conditioned, coalescing or escaping nodes. Applying (18) and then (9) gives
\[
 \varepsilon_{r+2}^{[r]}(S)\le d(S)\{\rho/4+o(1)\}.
 \tag{23}
\]
Together with (5) and the universal lower bound, this proves (6), including sharpness on the four-prime sequence. Unlike a three-node sign argument, (18) controls all the additional alternating weights produced by higher degree.

## Exact non-arithmetic control and validation

There is a complete analytic control with no prime asymptotics. On \(a>0\) take
\[
 F_0=0,\quad F_1=f,\quad F_2=3f+2g,\quad F_3=3f+3g.
 \tag{24}
\]
Its adjacent gaps are \(f,2(f+g),g\), so \(d=1\), the full-curve radius is \(1/4\), and \(x_*\) is a locator with minimum gap \(\rho>1/2\). Equations (10)--(18) give, for **every** fixed known degree \(r\),
\[
 \varepsilon_{r+2}^{[r],{\rm ad}}
 =\varepsilon_{r+2}^{[r]}=\rho/4<1/4
 =\varepsilon_{r+3}^{[r],{\rm ad}}=\varepsilon_{\rm full}^{[r]}.
 \tag{25}
\]
This verifies that the mechanism is not arithmetic-specific and is not only an asymptotic consequence of remote primes.

A scratch-only rational-arithmetic check verified 252 polynomial-reproduction identities for (10)--(11): degrees \(r=0,\ldots,6\), \(R\in\{10,100,10000\}\), \(L=1/1000\), and target coordinates \(2/3,4/5,1\). It also checked that the absolute anchor-weight sums are at least one and approach one. Floating-point checks of (19)--(21) at 10,001 coordinates and of the control (25) at degrees zero through six agreed with the proved constants. Those finite checks validate normalization and implementation of the formulas; the global inequalities, limiting constructions and prime statement rest on the proofs above, not a grid or numerical optimization.

## Prior art, delta and boundaries

Polynomial interpolation, divided-difference annihilators, quotient duality and bounded-error ball intersection are classical. Carl de Boor's *Divided Differences* (2005), already anchored under AF-571, supplies the standard interpolation setting. Dette and Titoff, [*Optimal discrimination designs* (2009), Theorem 2.1](https://arxiv.org/abs/0908.1912), connect classical regression discrimination to best uniform approximation. Rosa and Harman, [*Optimal Approximate Designs for Estimating Treatment Contrasts Resistant to Nuisance Effects*](https://arxiv.org/abs/1504.06079), treat additive nuisance effects and polynomial trends. Their statistical criteria do not directly prove this deterministic adaptive query theorem on an unbounded domain. No general approximation, experimental-design or priority claim is made.

Relative to AF-568/569, the substantive extension is the **all-known-degrees full-ray budget and unchanged sharp ratio**, supported by the stronger signed-measure certificate and the controlled noise norm of escaping anchors. Relative to AF-571, the domain and margin change: that finding recovers the reduced small-window quotient margin with \(r+2\) fixed probes, whereas the present full-ray margin can require \(r+3\) adaptive probes. Relative to AF-580, the supplied degree bound is the explicit hypothesis that restores reliable finite positive-noise recovery.

The load-bearing limits are separate: first fix the finite source set, degree and strict noise slack, then choose legal finite anchors; prime-family limits establish the worst relative ratio. No uniform bound on anchor locations, output magnitudes or finite-precision arithmetic cost is proved. Interpolated values may be enormous, even though their absolute-error amplification is controlled. The theorem fails to address bounded query windows, unknown degree, separately changing calibration between probes, relative rather than absolute error, and randomized minimax error probabilities. It gives an equality of supremal radii, not endpoint recovery or one finite anchor set attaining all limiting margins simultaneously.

The inputs in (1) are generalized-prime matched controls indexed by genuine rational-prime edit locations. Their separability is not a discriminator that certifies the ordinary primes, and none of these query results yields a zero-free region or an RH implication. A downstream arithmetic application must still justify its calibration law, accessible coordinate range and absolute precision.
