# AF-555 — Remote generator perturbations have a sharp critical-curve resolution scale

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-TAIL · INVERSE-CONDITIONING · MOVING-OBSERVATION · MATCHED-CONTROL · NO-NOVELTY-CLAIM

## Claim: the full critical curve becomes polynomially insensitive to a remote norm

Let \(P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s}\) for real \(s>1\), and let
\[
\Phi(a)=P^{-1}(E_1(a)),\qquad
E_1(a)=\int_a^\infty e^{-u}\frac{du}{u},\qquad a>0.
\tag{1}
\]
By AF-554, this is the exact increasing-index critical limit of the common-output-calibration-invariant prime-tail transitions, using source-natural samples \(s=1+a/\log n\).

For each odd rational prime \(p\to\infty\), choose a positive real displacement \(\Delta_p\) satisfying
\[
0<\Delta_p<p_{\rm next}-p,\qquad \Delta_p/p\longrightarrow0.
\tag{2}
\]
Replace the single generator \(p\) by \(p+\Delta_p\) and retain every other prime norm, in its original marked order. This defines an admissible ordered generalized-prime generator system (not a new rational-prime sequence), with reference
\[
Q_p(s)=P(s)-h_p(s),\qquad
h_p(s):=p^{-s}-(p+\Delta_p)^{-s}>0.
\tag{3}
\]
The Mertens coefficient remains \(1\), all sufficiently remote indexed tails agree exactly, and AF-554 gives the companion limiting curve
\(\Phi_p(a)=Q_p^{-1}(E_1(a))<\Phi(a)\).

In the **target/source-\(s\)-coordinate supremum geometry** of the complete limiting curves, define
\[
D_p:=\sup_{a>0}[\Phi(a)-\Phi_p(a)].
\tag{4}
\]
Then the sharp separation law is
\[
\boxed{\displaystyle
D_p=\frac{\Delta_p}{e\,p^2\log p}\,(1+o(1)).
}
\tag{5}
\]
In particular, the source-natural discrete control \(p\mapsto p+1\) (valid for every odd \(p\)) has
\(D_p\sim(e p^2\log p)^{-1}\).

The maximum in (4) is attained. If \(a_p\) is any sequence of maximizers, or any asymptotically maximizing sequence whose separation divided by \(D_p\) tends to \(1\), then
\[
\boxed{\displaystyle
\Phi(a_p)=1+\frac{1+o(1)}{\log p},
\qquad
a_p\log p\longrightarrow e^{-B_1},
}
\tag{6}
\]
where \(B_1\) is the Meissel--Mertens constant
\(\sum_{\ell\le x,\ \ell\ {\rm prime}}1/\ell-\log\log x\to B_1\).
Thus the most discriminating point **moves toward \(a=0\)** as the modified generator goes to infinity. For every fixed compact \(K\Subset(0,\infty)\), with \(\sigma_K:=\min_{a\in K}\Phi(a)>1\),
\[
\sup_{a\in K}[\Phi(a)-\Phi_p(a)]
=O_K(\Delta_p\,p^{-1-\sigma_K})
=o(D_p).
\tag{7}
\]
There is no fixed interior critical-parameter window that captures the global sharp separation.

## Exact inverse displacement and its uniform control

Write \(r_p(s)=Q_p^{-1}(P(s))<s\) and \(W_p(s)=s-r_p(s)>0\).
Since \(a\mapsto E_1(a)\) maps \((0,\infty)\) onto \((0,\infty)\), and \(s=\Phi(a)\) likewise ranges over all \(s>1\),
\[
D_p=\sup_{s>1}W_p(s).
\tag{8}
\]
The mean-value theorem applied to
\(Q_p(r_p(s))-Q_p(s)=h_p(s)\) yields an exact point \(\xi_{p,s}\in(r_p(s),s)\) such that
\[
W_p(s)=\frac{h_p(s)}{-Q_p'(\xi_{p,s})}.
\tag{9}
\]
No linearized inverse is being assumed here.

The integral identity
\[
h_p(s)=s\int_p^{p+\Delta_p}u^{-s-1}\,du
\tag{10}
\]
also gives
\[
|h_p'(s)|
\le C s\Delta_p\log(p+\Delta_p)\,p^{-s-1}
\quad (s\ge1).
\tag{11}
\]
For large \(p\), \(h_p'(s)<0\) for \(s\ge1\). Since
\[
-P'(s)=\sum_{\ell\ {\rm prime}}(\log\ell)\ell^{-s}
\ge (\log2)\,2^{-s},
\tag{12}
\]
and \(s(2/p)^s\) is decreasing for \(s\ge1\) when \(p\) is large, (11)--(12) show
\[
\epsilon_p:=\sup_{s>1}\frac{|h_p'(s)|}{-P'(s)}
=O\left(\frac{\Delta_p\log p}{p^2}\right)=o(1).
\tag{13}
\]
Consequently
\(-Q_p'(s)\ge(1-\epsilon_p)(-P'(s))\).
Furthermore, \(P''>0\), so \(-P'(\xi_{p,s})\ge-P'(s)\).
Equation (9) therefore supplies the **global**, not merely local, upper bound
\[
0<W_p(s)\le
(1-\epsilon_p)^{-1}\frac{h_p(s)}{-P'(s)}
\qquad(s>1).
\tag{14}
\]

## Sharp maximization and localization

The classical prime-zeta normal form, already used in AF-552, is
\[
P(1+x)=-\log x+(B_1-\gamma)+O(x),
\qquad
-P'(1+x)=x^{-1}+O(1)
\quad(x\downarrow0),
\tag{15}
\]
where \(\gamma\) is Euler's constant. Put \(L=\log p\).

Fix a sufficiently small \(\delta>0\). For \(0<x\le\delta\), (10) gives, uniformly under (2),
\[
h_p(1+x)
=\Delta_p\,p^{-2-x}(1+x)
\left[1+O(\Delta_p/p)\right].
\tag{16}
\]
Combining this with (15),
\[
\frac{h_p(1+x)}{-P'(1+x)}
=\frac{\Delta_p}{p^2}\,
x e^{-Lx}\,[1+O(x)+O(\Delta_p/p)].
\tag{17}
\]
For \(L^{-1/2}\le x\le\delta\) this is
\(o(\Delta_p/(p^2L))\), using \(e^{-Lx}\le e^{-\sqrt L}\).
For \(x\ge\delta\), (10) and (12) instead give
\[
\frac{h_p(1+x)}{-P'(1+x)}
\le
\frac{\Delta_p(1+x)}{p\log2}
\left(\frac2p\right)^{1+x}
=O_\delta(\Delta_p p^{-2-\delta})
=o\!\left(\frac{\Delta_p}{p^2L}\right),
\tag{18}
\]
where the displayed upper envelope is decreasing in \(x\) for large \(p\).

On \(0<x<L^{-1/2}\), set \(u=Lx\). Equation (17) becomes
\[
\frac{h_p(1+x)}{-P'(1+x)}
=\frac{\Delta_p}{p^2L}\,
u e^{-u}[1+o(1)]
\tag{19}
\]
with uniform relative error, and \(u e^{-u}\) has its unique global maximum \(e^{-1}\) at \(u=1\).
Equations (14) and (17)--(19) prove
\[
\limsup_{p\to\infty}
\frac{p^2L}{\Delta_p}D_p\le e^{-1}.
\tag{20}
\]

For the matching lower bound, take \(s_0=1+1/L\).
Equation (14) first yields
\(W_p(s_0)=O(\Delta_p/(p^2L))=o(1/L)\).
Thus the mean-value point in (9) satisfies
\(\xi_{p,s_0}-1\sim1/L\).
By (15), \(-P'(\xi_{p,s_0})\sim-P'(s_0)\sim L\);
by (13), the same holds for \(-Q'(\xi_{p,s_0})\).
Substitute into (9) and (16) to obtain
\[
W_p(s_0)\sim
\frac{\Delta_p}{e\,p^2L}.
\tag{21}
\]
Together (20)--(21) prove (5).

As \(s\downarrow1\), the common logarithmic singularity implies
\(r_p(s)-1\sim e^{-h_p(1)}(s-1)\), so \(W_p(s)\to0\).
As \(s\to\infty\), (14) and (12) imply \(W_p(s)\to0\).
Hence \(W_p\) attains its positive supremum in the interior.
The uniqueness of the maximum of \(u e^{-u}\), combined with (14), (19), and the sharp lower bound, forces \(L(s_p-1)\to1\) for every (asymptotic) maximizing \(s_p\).

Finally the small-argument expansion
\(E_1(a)=-\gamma-\log a+O(a)\), together with (15) and
\(E_1(a_p)=P(s_p)\), yields
\[
a_p/(s_p-1)\longrightarrow e^{-B_1},
\tag{22}
\]
proving the location claim (6).

For compact \(K\Subset(0,\infty)\), \(s=\Phi(a)\) stays in a compact subset of \((1,\infty)\). The mean-value formula (9) and \(h_p(s)=O_K(\Delta_p p^{-s-1})\) give (7), after bounding \(-Q_p'\) away from zero there.

## Fidelity tariff against a matched generalized-prime control

The marked generator coordinate changes by \(\Delta_p\), while its logarithm changes by
\[
\log(p+\Delta_p)-\log p
=\frac{\Delta_p}{p}(1+o(1)).
\tag{23}
\]
If a decoder of the **entire limiting critical curve**, equipped with the supremum distance (4), outputs the norm of that marked generator and is Lipschitz on a class containing both source systems, its Lipschitz constant is at least
\[
\frac{\Delta_p}{D_p}\sim e\,p^2\log p.
\tag{24}
\]
For a decoder returning the marked **log norm**, the corresponding lower bound is
\[
\frac{\log(p+\Delta_p)-\log p}{D_p}
\sim e\,p\log p.
\tag{25}
\]
These are pairwise inverse-conditioning lower bounds, not unconditional minimax error rates or lower bounds for representations with extra source information.

The critical curves are calibration-invariant because they arise from the AF-550/AF-554 relative transitions; their **source** coordinate and marked index remain fixed. The supremum norm here is a deliberate observation geometry, not an invariant under arbitrary input-coordinate reparameterization. A nonlinear warp of \(s\), independently applied to the two profiles, would define a different experiment. Formula (7) further shows that an instrument sampling only a fixed compact \(a\)-window faces a strictly smaller signal than the global supremum.

The limits are ordered: for each fixed deformed source, first form its \(n\to\infty\) critical-index transition limit; then let the modified index/prime \(p\to\infty\). Nothing above asserts uniform finite-\(n\) accuracy when \(p\) and \(n\) grow simultaneously. In particular, the universal \(E_1\) tail profile has not independently manufactured a rational-prime-specific discriminator; the source dependence remains the retained reference inverse.

## Prior art, failure modes, and consequences

AF-554 supplies the limiting critical-curve identity and the common-calibration quotient; AF-561 supplies the relevant horizontal/registration perspective and the need for an admissible matched control; AF-552 supplies the prime-zeta logarithmic boundary expansion. Classical antecedents are Mertens' reciprocal-prime asymptotic (including the constant \(B_1\)), the Möbius-inversion/prime-zeta expansion (Fröberg; see also Kawalec, arXiv:2603.21535, recent preprint), and elementary inverse-function perturbation and monotone registration. Their bibliographic anchors are already recorded in the line's `SOURCES.md` under AF-017 and AF-550--AF-554. No literature priority is claimed for those ingredients or for the general principle that an inverse map amplifies small perturbations by the reciprocal derivative. The derived line-specific outcome is the sharp \(p^{-2}(\log p)^{-1}\) global metric tariff and its **moving optimal observation location** for a source-admissible single-generator control.

Decisive checks: the deformed generator must remain ordered and the coefficient of the logarithmic singularity must stay equal to one; the derivative perturbation must be uniform for **all** \(s>1\), not just in the maximizing window; the \(\gamma\) terms in (15) and \(E_1\) must cancel to give precisely \(e^{-B_1}\); the \(a\)-supremum in (4) must be converted to an \(s\)-supremum only after retaining the reference-inverse parameterization. The simple integer displacement \(p+1\) is admissible for odd primes but not for \(p=2\), where it would duplicate the next prime. The decay and decoder bounds concern this specific limiting-curve metric, not noisy raw outputs before calibration, not joint \(p,n\) limits, and not zero locations of \(\zeta\).

**Arithmetic Fidelity consequence.** Exact reconstruction of a full reference Dirichlet profile from its critical limit (AF-554) coexists with a sharp, source-realized loss of uniform stability for distant individual generators. Increasing precision alone cannot turn a fixed interior critical-parameter window into a uniformly faithful high-index detector: the optimal window migrates to \(a\asymp1/\log p\) while the maximally available separation still shrinks as \(\Delta_p/(p^2\log p)\). An RH-facing destination must first be shown to preserve a suitable target-sensitive observation geometry and its stability modulus; this theorem neither excludes off-critical zeros nor proves RH.
