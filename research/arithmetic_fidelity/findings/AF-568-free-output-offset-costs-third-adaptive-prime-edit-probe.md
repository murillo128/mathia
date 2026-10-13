# AF-568 — A free output offset costs a third adaptive prime-edit probe

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-EDIT · OUTPUT-CALIBRATION-QUOTIENT · ADAPTIVE-IDENTIFICATION · SHARP-MINIMAX-OBSTRUCTION · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Theorem: two-query saturation is not invariant under an unknown output origin

Use the **same** commonly registered prime-edit profiles and rational-prime edit locations as AF-559, AF-562, AF-563, and AF-567. Thus, for each odd rational prime \(p\),
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\qquad
Q_p(s)=P(s)-[p^{-s}-(p+1)^{-s}],\qquad
\Phi_p(a)=Q_p^{-1}(E_1(a)),\quad a>0,
\]
where \(E_1(a)=\int_a^\infty e^{-v}\,dv/v\). The systems \(Q_p\) are generalized-prime **matched controls**, not distinct rational-prime systems. The critical coordinate \(a\) is still commonly registered; the new uncertainty is a *further additive output-origin nuisance* in the observation channel, not a change in the definition of \(\Phi_p\).

Let \(S=\{p_1<\cdots<p_m\}\) be any known finite set of at least two odd-prime locations. Observations of the unknown source \(i\) are
\[
y_j=\Phi_{p_i}(a_j)+b+\eta_j,\qquad
b\in\mathbb R,\quad |\eta_j|\le\varepsilon. \tag{1}
\]
Within one experiment the nuisance \(b\) is constant across all queries; it is unknown and unrestricted, and alternative hypotheses may have **different** nuisance values. Errors at different queries are independently adversarial within the displayed pointwise bounds. A query location may depend deterministically on all earlier readings. Put
\[
G_i(a)=\Phi_{p_{i+1}}(a)-\Phi_{p_i}(a)>0,\quad
D_i=\sup_{a>0}G_i(a),\quad
d(S)=\min_{i<m}D_i. \tag{2}
\]
Define \(\varepsilon^{\rm off,ad}_k(S)\) as the supremal worst-case unique-identification radius with at most \(k\) adaptive observations, and \(\varepsilon^{\rm off}_k(S)\) for nonadaptive observations. Define \(\varepsilon^{\rm off}_{\rm full}(S)\) by observing the entire commonly registered curve, still with one unknown constant \(b\) and a uniform pointwise error bound.

**Sharp calibration-sensitive budget law.** There exists \(P_0\) such that whenever \(\min S\ge P_0\),
\[
\boxed{\quad
\varepsilon^{\rm off}_{\rm full}(S)=\frac{d(S)}4,
\qquad
\varepsilon^{\rm off,ad}_3(S)=\frac{d(S)}4.
\quad} \tag{3}
\]
Every single observation is compatible with every source, even at zero noise. For **every finite \(S\), without an asymptotic assumption**, two-query adaptivity is entirely ineffective:
\[
\boxed{\quad
\varepsilon^{\rm off,ad}_2(S)=\varepsilon^{\rm off}_2(S)
=\frac14\sup_{a_0,a_1>0}\min_{i<j}
\left|G_{i,j}(a_1)-G_{i,j}(a_0)\right|,
\quad
G_{i,j}:=\Phi_{p_j}-\Phi_{p_i}.
\quad} \tag{4}
\]
But, writing
\[
\rho=\frac{8e}{9}\log\frac32=0.9797052759\ldots,
\]
the exact asymptotic worst-family ratio is
\[
\boxed{\quad
\lim_{P\to\infty}
\inf_{\substack{S\ {\rm finite\ odd\ prime\ locations}\\
|S|\ge2,\ \min S\ge P}}
\frac{\varepsilon^{\rm off,ad}_2(S)}
     {\varepsilon^{\rm off}_{\rm full}(S)}
=\rho<1.
\quad} \tag{5}
\]
Consequently **three**, rather than AF-567's **two**, are the smallest universally full-margin adaptive query budget for sufficiently remote prime-edit candidates **in the new unknown-offset channel**. Equation (5) is an obstruction to transporting AF-567's two-query conclusion through an unregistered output origin; it does not contradict AF-567's calibrated experiment.

## Exact quotient geometry: the full-curve radius is halved

AF-559 proves that every \(G_{i,j}\) is positive, has finite supremum \(D_{i,j}\), and tends to \(0\) as \(a\downarrow0\) and \(a\to\infty\). The distance between two complete profiles after independently fitting their admissible constant offsets is
\[
\begin{aligned}
\inf_{c\in\mathbb R}\sup_{a>0}|G_{i,j}(a)-c|
&=\frac{\sup_aG_{i,j}(a)-\inf_aG_{i,j}(a)}2\\
&=\frac{D_{i,j}}2. \tag{6}
\end{aligned}
\]
Two radius-\(\varepsilon\) observation balls intersect exactly when the offset-quotiented center separation is at most \(2\varepsilon\); the midpoint of the optimally shifted centers is an explicit common observation. The sharp pairwise radius is therefore \(D_{i,j}/4\). Since every nonadjacent \(G_{i,j}\) is a sum of positive adjacent gaps, \(D_{i,j}\ge\min_{\ell}D_\ell=d(S)\). The minimum is attained by an adjacent pair with \(D_i=d(S)\). This proves the first equality in (3), and gives an upper bound \(d(S)/4\) for **any** adaptive query budget: the same suitably shifted midpoint transcript defeats every deterministic policy at that noise radius.

Unlike the calibrated AF-562/AF-567 radius \(d(S)/2\), the unknown output origin destroys the common vertical reference, even when the complete shape remains observable. All ratios below are normalized by the **new** full-curve radius \(d(S)/4\), not by the old radius.

## Exact two-query lemma: the first response has no source information

The first reading \(y_0\) can be **any real number under every source**, since \(b\) is unrestricted. After a first location \(a_0\) and a second location \(a_1=a_1(y_0)\), eliminate \(b\) by subtraction:
\[
y_1-y_0
=\Delta_i(a_0,a_1)+(\eta_1-\eta_0),\qquad
\Delta_i=\Phi_{p_i}(a_1)-\Phi_{p_i}(a_0).
\tag{7}
\]
Conditional on **any fixed** \(y_0\), every value in the exact interval
\[
[y_0+\Delta_i-2\varepsilon,\ y_0+\Delta_i+2\varepsilon] \tag{8}
\]
can be realized under hypothesis \(i\): choose errors with any prescribed difference in \([-2\varepsilon,2\varepsilon]\) and set \(b=y_0-\Phi_{p_i}(a_0)-\eta_0\). Thus two hypotheses have a common possible pair of observations precisely when
\[
|\Delta_i-\Delta_j|
=|G_{i,j}(a_1)-G_{i,j}(a_0)|
\le4\varepsilon. \tag{9}
\]

A policy must work for **every** first reading \(y_0\). Equation (9) shows that every possible second query must itself make *every* pair contrast exceed \(4\varepsilon\). Allowing \(a_1\) to depend on \(y_0\) cannot improve the optimum over a constant second location; conversely any two fixed locations satisfying these inequalities uniquely decode from the difference (7). Taking suprema yields (4), with strict inequalities at attainable radii and the usual possible tie at the supremum. This proof works for any finite real-valued source family with an unrestricted shared additive offset; ordering and prime structure enter only in the next steps.

## Uniform two-query lower bound and sharp four-prime obstruction

Let \(d=d(S)\). AF-563 proves that its known-source-set single coordinate
\[
a_1(S)=\frac{e^{-B_1}\,6\log(3/2)}{\log(1/d(S))} \tag{10}
\]
obeys, **uniformly over arbitrary finite \(S\)** as \(\min S\to\infty\),
\[
\min_iG_i(a_1(S))\ge(\rho-o(1))d. \tag{11}
\]
Since \(S\) is finite and all the gaps vanish at the left endpoint, choose a positive first coordinate \(a_0(S)\downarrow0\) sufficiently far into that endpoint that
\(\max_iG_i(a_0)=o(d)\), with no restriction on how small the coordinate may be. Hence every adjacent *contrast* is at least \((\rho-o(1))d\):
\[
G_i(a_1)-G_i(a_0)\ge(\rho-o(1))d.
\]
Every nonadjacent contrast is a sum of these **positive** adjacent contrasts. Equation (4) gives
\[
\frac{\varepsilon^{\rm off,ad}_2(S)}
{\varepsilon^{\rm off}_{\rm full}(S)}
\ge\rho-o(1) \tag{12}
\]
uniformly in the cardinality and logarithmic diameter of \(S\).

For sharpness, reuse AF-562's four **actual odd prime** edit locations \(p<r<q<t\) with two equal bottleneck gaps and scale ratio \(\lambda=\log q/\log p\to3/2\). The intermediate gap is much larger. Let \(f(x)=xe^{1-x}\) (\(x\ge0\)); AF-559 gives **globally uniform** normalized responses for the two bottlenecks:
\[
G_{p,r}(a)/d=f(ca\log p)+o(1),\qquad
G_{q,t}(a)/d=f(\lambda ca\log p)+o(1), \tag{13}
\]
with error uniform over \(a>0\), where \(c=e^{B_1}\) and \(d\) is the full-curve minimum separation (the two bottleneck peaks agree asymptotically). Uniformity extends to observations moving towards either endpoint.

Therefore (4), after discarding all but those two necessary pairs, gives the upper bound
\[
\limsup
\frac{\varepsilon^{\rm off,ad}_2(S)}
{\varepsilon^{\rm off}_{\rm full}(S)}
\le
\sup_{x,y\ge0}
\min\left\{|f(x)-f(y)|,\
|f(3x/2)-f(3y/2)|\right\}. \tag{14}
\]
The right side is **exactly** \(\rho\), not a potentially larger two-point range-covering constant. For the lower bound choose \(y=0\) (a limit point) and \(x=2\log(3/2)\), when \(f(x)=f(3x/2)=\rho\).

For the reverse inequality, suppose both absolute differences in (14) exceed \(\rho\). Relabel \(x,y\) to arrange \(f(x)>\rho\), \(f(y)<1-\rho\) (the range of \(f\) is \([0,1]\)). Since \(f(2)=2/e<\rho\) and \(f\) decreases for \(x>1\), this forces \(x<2\). But
\[
f(3x/2)=\tfrac32e^{-x/2}f(x)>
\frac{3\rho}{2e}>1-\rho. \tag{15}
\]
For the second absolute difference to exceed \(\rho\), its value at \(3x/2\) must then be the *larger* one, so \(f(3x/2)>\rho\). This contradicts the exact one-sample equalizer
\[
\sup_{x\ge0}\min\{f(x),f(3x/2)\}=\rho
\]
from AF-562. Thus the supremum in (14) cannot exceed \(\rho\). Combined with (12), the four-prime family proves (5). This argument uses **neither** a short-interval prime theorem nor an unjustified pointwise approximation in a shrinking response tail.

## Three-query adaptive recovery, for every sufficiently remote finite candidate set

Fix any \(0\le\varepsilon<d/4\). AF-563 and \(\rho>1/2\) give, for all sufficiently large \(\min S\), a location \(a_1\) with
\(\min_iG_i(a_1)>d/2+\delta\) for some \(\delta>0\). Choose a positive anchor \(a_0\) so close to the left endpoint that **every**
\[
0<G_i(a_0)<\min\{\delta,\ d-4\varepsilon\}. \tag{16}
\]
The first two readings determine, by (7), a version space of indices whose noiseless contrasts \(v_i=\Phi_{p_i}(a_1)-\Phi_{p_i}(a_0)\) lie inside an interval of width \(4\varepsilon<d\). They are strictly increasing, with every consecutive gap
\[
v_{i+1}-v_i=G_i(a_1)-G_i(a_0)>d/2. \tag{17}
\]
Consequently at most **two adjacent indices** are compatible; three would span more than \(d>4\varepsilon\).

If the version space has one member, decode. Otherwise it is \(\{i,i+1\}\). For this pair, \(D_i\ge d>4\varepsilon+G_i(a_0)\) by (16). Hence some third location \(a_2\), chosen *after the first two readings*, has
\[
G_i(a_2)-G_i(a_0)>4\varepsilon. \tag{18}
\]
Subtracting the first reading from the third again removes \(b\), and (18) makes the two candidate difference intervals, each of radius \(2\varepsilon\), disjoint. The third reading therefore identifies the source for every admissible noise sequence. This proves \(\varepsilon^{\rm off,ad}_3(S)\ge d/4\); the full-curve upper bound proves equality in (3). The choice of \(a_0\) may depend on the announced \(\varepsilon\), as is appropriate for a supremal worst-case radius, and no uniform lower bound on allowable coordinate size is assumed.

## Prior art, falsification checks, and limits

Unknown additive intercepts, invariant contrasts, minimax noise balls, and sequential experiment design are established mathematics. AF-490 already identifies the quotient by an unrestricted nuisance subspace in a different deterministic single-exponential experiment. The classical discrimination and sequential-design setting is described by Atkinson--Cox (1974), and resistance to additive nuisance effects is central in Rosa--Harman (2016); neither is claimed as a new general construction here. This finding's source-specific delta is the **sharp two-query/three-query budget change** for AF-559's prime-edit critical curves, with the AF-562 four-prime obstruction and AF-563 uniform localization giving both matching minimax directions.

The full-curve radius is **one quarter**, not one half, of the minimum adjacent full-curve gap; the factor comes from two distinct halvings (quotient distance and midpoint adversarial noise). With two readings, the observable contrast has error **up to \(2\varepsilon\)** and pairwise compatibility threshold \(4\varepsilon\), not \(2\varepsilon\). The offset is *the same* within each hypothetical source and is allowed to differ between alternative hypotheses; imposing one externally known offset common to all hypotheses collapses back to AF-567, not this experiment. The apparently free first observation is genuinely uninformative because \(b\) ranges over all \(\mathbb R\); a bounded or probabilistic prior on \(b\) could restore partial localization.

The four-prime upper bound needs the global-uniform AF-559 response because the two query locations may themselves move to the critical-window endpoints. The inequality (15) prevents a hidden two-point strategy from exploiting opposite signs of the two bottleneck differences. The three-query proof uses only **one** endpoint anchor, a known-set robust locator, and a targeted last query; it does not assume the errors at the different queries coincide or are stochastic. Exact equality of optimal radii is in the *supremal* sense: unique identification can fail at the boundary \(\varepsilon=d/4\). The source alternatives remain generalized-prime edits at rational-prime locations; the critical-index limit, common coordinate registration, known candidate family, unrestricted query locations, and deterministic absolute-noise convention remain essential. No nonvanishing absolute margin, prime-specific zero divisor, or RH consequence follows.

## Consequence for Arithmetic Fidelity

An observation protocol can be **adaptively sufficient before compression** yet lose that finite-budget sufficiency after quotienting an apparently harmless acquisition mark. AF-567's calibrated two-query full-margin theorem and this unknown-offset three-query theorem refer to different observation spaces; carrying the vertical origin is mathematically load-bearing. One initial near-endpoint observation restores the missing difference reference, but does not itself locate the edited prime. This is a sharp, source-realized example in which the minimal adaptive observation budget changes under a one-dimensional nuisance quotient, even though the complete quotient curve still identifies every candidate at a positive (but vanishing) noise radius.
