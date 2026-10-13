# AF-563 — Universal sharp one-sample minimax ratio for discrete prime edits

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-TAIL · MINIMAX-IDENTIFICATION · UNIVERSAL-ONE-SAMPLE-BOUND · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Theorem: the two-scale penalty of AF-562 is the worst asymptotic penalty

Use exactly the common-output-calibration-invariant critical curves and deterministic additive-noise experiment of AF-559/AF-562. For an odd rational prime \(p\), let
\[
Q_p(s)=P(s)-h_p(s),\qquad
h_p(s)=p^{-s}-(p+1)^{-s},\qquad
\Phi_p(a)=Q_p^{-1}(E_1(a)),
\]
where \(P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s}\) and
\(E_1(a)=\int_a^\infty e^{-v}\,dv/v\).
For any finite \(S=\{p_1<\cdots<p_m\}\) of at least two odd primes set
\[
G_i(a)=\Phi_{p_{i+1}}(a)-\Phi_{p_i}(a)>0,\quad
D_i=\sup_{a>0}G_i(a),\quad
d(S)=\min_{i<m}D_i=2\varepsilon_{\rm full}(S).
\tag{1}
\]
As proved in AF-562, the one-sample radius is
\(2\varepsilon_1(S)=\sup_{a>0}\min_iG_i(a)\).
Write \(B_1\) for the Meissel--Mertens reciprocal-prime constant and define
\[
\kappa=6\log(3/2),\qquad
\rho=\frac{8e}{9}\log(3/2)=0.9797052759\ldots.
\tag{2}
\]

**Universal sharp theorem.** For *every* sequence of finite candidate sets \(S\) with \(\min S\to\infty\), with neither a cardinality nor a logarithmic-diameter restriction, the single source-independent sample (conditional on the known candidate set)
\[
\boxed{
a_S=\frac{e^{-B_1}\kappa}{\log[1/d(S)]}
}
\tag{3}
\]
satisfies
\[
\boxed{
\liminf_{\min S\to\infty}
\frac{\varepsilon(\{a_S\},S)}{\varepsilon_{\rm full}(S)}
\ge\rho.
}
\tag{4}
\]
Consequently the *optimal* one-sample design satisfies the sharp worst-family identity
\[
\boxed{
\lim_{P_0\to\infty}
\inf_{\substack{S\subset\{\text{odd primes}\}\\
2\le |S|<\infty,\ \min S\ge P_0}}
\frac{\varepsilon_1(S)}{\varepsilon_{\rm full}(S)}
=\rho.
}
\tag{5}
\]
The upper bound/sharpness in (5) is attained asymptotically by the actual four-prime family constructed in AF-562. Thus its roughly \(2.03\%\) loss is a **universal worst-case asymptotic loss**, not just the loss of one illustrative family.

The guarantee is a *relative* fraction of a generally vanishing absolute noise margin; it does not supply a nonvanishing precision threshold or an RH discriminator.

## Uniform relative boundary estimate (needed below the normalized-profile tail)

Let \(\Phi=P^{-1}\circ E_1\), \(r_t(s)=Q_t^{-1}(P(s))\), and
\[
B_{p,q}=p^{-2}-q^{-2},\qquad L_p=\log p.
\]
AF-559 proves \(D_{p,q}=B_{p,q}/(eL_p)[1+o(1)]\), uniformly in every larger odd prime \(q>p\). Its globally uniform *additive* normalized-profile convergence alone does **not** justify a relative estimate when the normalized profile tends to zero. We require the following strengthened local consequence of the exact inverse equation:

For every fixed sufficiently small \(x_0>0\), uniformly in \(0<x\le x_0\) and all odd primes \(q>p\to\infty\),
\[
\boxed{
r_q(1+x)-r_p(1+x)
=B_{p,q}\,x\,e^{-L_px}
\bigl[1+O(x+p^{-1})\bigr].
}
\tag{6}
\]
In particular its error is *multiplicative*, even when \(L_px\to0\).

To prove (6), the prime-zeta expansion gives
\(-P'(1+y)=y^{-1}+O(1)\) uniformly for small positive \(y\).
The defining equation for \(r_t(1+x)<1+x\) is
\[
P(r_t(1+x))-P(1+x)=h_t(r_t(1+x)).
\]
Since \(h_t(1+y)=O(t^{-2})\) in the same small interval, the mean-value theorem and \(-P'(1+y)\asymp y^{-1}\) imply
\[
0<(1+x)-r_t(1+x)\le Cx/t^2.
\tag{7}
\]
This relative-to-\(x\) displacement bound, rather than the cruder global \(O((t^2\log t)^{-1})\) bound, is essential when \(x\) is arbitrarily small.

With \(k_{p,q}=h_p-h_q\), the exact same-denominator identity from AF-559 is
\[
r_q(1+x)-r_p(1+x)
=\frac{k_{p,q}(r_q(1+x))}{-Q_p'(\xi)},
\qquad r_p(1+x)<\xi<r_q(1+x).
\tag{8}
\]
AF-559's uniform relative-gap identity gives
\[
k_{p,q}(1+x)
=B_{p,q}e^{-L_px}[1+O(x+p^{-1})]
\tag{9}
\]
for \(0<x\le x_0\), without any hypothesis on \(q/p\) or \(q-p\). Its logarithmic-derivative bound
\(|(\log k_{p,q})'(s)|\le\log(q+1)+2\), together with (7) for \(t=q\), shows
\(k_{p,q}(r_q(1+x))/k_{p,q}(1+x)=1+O(x\log(q+1)/q^2)=1+O(x)\)
uniformly in \(q>p\).
Finally (7) implies \(\xi-1=x[1+O(p^{-2})]\); because
\(Q_p'=P'-h_p'\) and \(|h_p'|=O((\log p)/p^2)\) in the boundary interval,
\[
[-Q_p'(\xi)]^{-1}=x[1+O(x+p^{-1})].
\]
Substitution in (8)--(9) proves (6), with errors uniform over the full candidate family.

## Proof of the universal lower bound

Let \(d=d(S)\), \(H=\log(1/d)\), and \(L_i=\log p_i\). By AF-559,
\[
D_i=\frac{B_i}{eL_i}[1+o(1)],\qquad
B_i=p_i^{-2}-p_{i+1}^{-2},
\tag{10}
\]
where the \(o(1)\) is *uniform for every adjacent pair* as \(\min S\to\infty\). Because \(d\le D_i\le(1+o(1))p_i^{-2}/(eL_i)\), one has
\[
2L_i+\log L_i\le H+O(1),\qquad
0<t_i:=L_i/H\le\tfrac12+o(1)
\tag{11}
\]
uniformly in \(i\). In particular \(H\to\infty\).

At \(a=a_S\), the fixed boundary relation
\(a=e^{-B_1}x[1+O(x)]\), where \(x=\Phi(a)-1\), gives
\[
x=\frac{\kappa}{H}[1+O(H^{-1})].
\]
Apply (6), using \(L_i\le H/2+O(1)\) to control the exponent uniformly:
\[
G_i(a_S)
=\frac{\kappa B_i}{H}e^{-\kappa t_i}[1+o(1)]
\quad\text{uniformly in every }i.
\tag{12}
\]
Since \(d\le D_i=B_i/(eL_i)[1+o(1)]\),
\[
\frac{G_i(a_S)}d
\ge[1-o(1)]\,\kappa t_i e^{1-\kappa t_i}
=[1-o(1)]f(\kappa t_i),
\qquad f(u)=u e^{1-u}.
\tag{13}
\]

For \(t_i\ge 1/3-\eta\), where \(\eta>0\) is fixed and small, (11) and the unimodality of \(f\) imply
\[
\frac{G_i(a_S)}d\ge\rho-O(\eta)-o(1).
\tag{14}
\]
Indeed, \(f(\kappa/3)=f(\kappa/2)=\rho\), while \(f\) rises then falls between these two arguments; extending the left endpoint by \(\eta\) changes the minimum continuously.

What if \(t_i\) is much smaller than \(1/3\), where the preceding \(f\)-bound becomes weak? **Here discreteness of the edit locations becomes decisive.** Distinct odd primes satisfy \(p_{i+1}\ge p_i+2\), so
\[
B_i\ge p_i^{-2}-(p_i+2)^{-2}
=(4+O(p_i^{-1}))p_i^{-3}.
\tag{15}
\]
Equations (12) and \(d=e^{-H}\) therefore imply
\[
\frac{G_i(a_S)}d
\ge\frac{(4-o(1))\kappa}{H}
\exp\{H-3L_i-\kappa t_i\}.
\tag{16}
\]
Whenever \(t_i<1/3-\eta\), the right-hand side is at least
\(C_\eta e^{3\eta H}/H\to\infty\), uniformly in \(i\). Such lower-scale pairs are *too strongly separated in absolute amplitude* to be bottlenecks at this universal sample. Combining (14) and (16), then taking \(\eta\downarrow0\), yields
\[
\min_iG_i(a_S)/d\ge\rho-o(1).
\]
By (1) and AF-562's exact adjacent-pair minimax reduction this is precisely (4).

For sharpness, AF-562 constructs four actual odd prime edit locations with two asymptotically equal smallest gaps, one at scale \(\log p\) and one at scale \((3/2)\log p\). Its exact maximin calculation gives
\(\varepsilon_1/\varepsilon_{\rm full}\to(8e/9)\log(3/2)=\rho\). This supplies the reverse inequality for the infimum in (5) and proves the asserted limit.

## Structural meaning, prior art, and falsification boundaries

The two ingredients governing the sharp constant are the **upper amplitude envelope** \(D_{p,q}\lesssim p^{-2}/\log p\) and the **spacing-imposed lower envelope** \(B_{p,q}\gtrsim p^{-3}\) for distinct odd prime edit locations. At a minimax margin \(d=e^{-H}\) they force all potentially tight logarithmic scales into \([H/3,H/2]\) up to a vanishing boundary layer. The ratio of the endpoint scales is \(3/2\); equalizing the two universal response profiles yields (2). Pairs at smaller scales are excluded by an explicit amplitude estimate, not by an unjustified uniform relative-error division.

The elementary minimax/equalizer step belongs to classical discrimination-design and Chebyshev-type maximin thinking, including the several-model work of Atkinson--Fedorov (1975) cited in the line's \`SOURCES.md\` under AF-562. The prime-zeta boundary, exact inverse and PNT ingredients are already anchored under AF-552, AF-559 and AF-562. No claim of novelty is made for those general methods or for the numerical constant outside this exact source model. The extra Mathia-specific implication is the **sharp uniform infimum over arbitrarily large and arbitrarily log-dispersed finite odd-prime candidate sets**, whereas AF-562 proved losslessness for localized sets and exhibited just one two-scale family. No new bibliographic anchor beyond the existing source entries is required.

The spacing floor (15) is necessary to this proof; it would also hold for suitable separated integer edit grids and is **not** a discriminator of rational primes against every generalized-prime system. Arbitrarily close real-valued edit positions have no \(p^{-3}\) floor and are outside (5). Source registration, common output calibration, the complete critical-index limit, additive \(L^\infty\)-noise geometry, and preknown candidate set \(S\) all remain fixed. The selected parameter (3) uses the full-curve theoretical margin \(d(S)\) known from the candidate model; it is not an observation-dependent or unknown-family adaptive rule. For fixed nonasymptotic \(S\), no literal \(0.9797\) lower bound is claimed: (4)--(5) are asymptotic with possibly slow convergence.

Decisive independent checks: (i) verify (7) stays \(O(x/t^2)\) even for \(x\ll t^{-2}\), where the global AF-559 absolute profile error is insufficient; (ii) check (8)--(9) keep relative-gap errors uniform in \(q>p\), including \(q-p=2\); (iii) verify \(L_i\le H/2+o(H)\) without an upper bound on \(\max S\); (iv) check the competing \(t_i<1/3-\eta\) bound instead of dividing an \(o(1)\) normalized-profile error by a vanishing \(f\); (v) confirm AF-562's actual-prime construction saturates the bound for **optimal** one-sample design, not merely the explicit sampler.

## Consequence for Arithmetic Fidelity

In this deterministic prime-edit critical-curve model, one well-placed observation *always* retains at least \(\rho-o(1)\) of the full-curve identification margin, irrespective of how many admissible prime alternatives or how many logarithmic scales are present. The AF-562 four-prime obstruction is already the worst possible asymptotic relative one-sample loss. This turns its local counterexample into a complete minimax sampling-ratio classification for the declared source family; it does not improve absolute conditioning, prove recovery through an RH-facing representation, or assert any RH consequence.
