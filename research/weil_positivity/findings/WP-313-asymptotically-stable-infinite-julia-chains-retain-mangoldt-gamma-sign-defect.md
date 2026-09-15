---
id: WP-313
title: Asymptotically stable infinite Julia chains retain the Mangoldt–Gamma sign defect
branch: weil_positivity
status: supported
kind: infinite-fixed-boundary-julia-asymptotic-stability-obstruction
claim_strength: exact monotonic obstruction for every countable chain of fixed real Julia–Nevanlinna reductions whose high-energy asymptotic invariants pass to the limit; regular reductions accumulate a nonnegative log-over-linear defect with no cancellation, while pure pole stripping keeps the second curvature positive and exhaustive Mangoldt pole stripping makes it diverge
created: 2026-09-15
related: [WP-305, WP-310, WP-311, WP-312]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for classical Julia–Nevanlinna boundary reduction and its continued-fraction parametrization
  - Tryphon T. Georgiou and Pramod P. Khargonekar, Spectral Factorization and Nevanlinna-Pick Interpolation, SIAM Journal on Control and Optimization 25 (1987), 754-766, DOI 10.1137/0325043, for convergence of an infinite recursive Nevanlinna–Pick linear-fractional algorithm and the dependence of convergence on interpolation-point placement
  - Tom M. Apostol, Introduction to Analytic Number Theory, Springer, 1976, for classical Mertens estimates for prime-weighted sums
  - NIST Digital Library of Mathematical Functions, Section 5.11, especially Eq. 5.11.2, for the Riemann digamma asymptotic used in WP-305
---

# WP-313 — Asymptotically stable infinite Julia chains retain the Mangoldt–Gamma sign defect

## Claim

`WP-312` closes every **finite** chain of classical Julia–Nevanlinna reductions at fixed real boundary nodes of the reflected critical Mangoldt Herglotz response `m_-`, but deliberately leaves an infinite chain open because local convergence of Pick functions need not control asymptotics at infinity. That caveat is essential, but it can now be isolated sharply.

For any Pick function with unit logarithmic end, define the translation-invariant first asymptotic defect

\[
L(f):=
\lim_{y\to\infty}
\frac{y}{\log y}
\left(
\operatorname{Re}f(iy)-\log y-c(f)
\right),
\qquad
c(f):=\lim_{y\to\infty}
\left(
\operatorname{Re}f(iy)-\log y
\right),
\tag{1}
\]

whenever these limits exist. If `L(f)=0`, define the second real curvature

\[
C(f):=
\lim_{y\to\infty}
y^2
\left(
\operatorname{Re}f(iy)-\log y-c(f)
\right)
\tag{2}
\]

when it exists. For the canonical reflected Mangoldt source of `WP-305`,

\[
L(m_-)=0,
\qquad
C(m_-)=A_{\rm M}>0,
\tag{3}
\]

whereas the Riemann archimedean digamma target has, after its irrelevant real constant is removed,

\[
L(\Gamma_{\rm R})=0,
\qquad
C(\Gamma_{\rm R})=-\frac1{24}.
\tag{4}
\]

Now let `f_N` be any countable sequence obtained from `f_0=m_-` by fixed-real-node Julia–Nevanlinna reductions, returning every regular reduction to unit logarithmic normalization exactly as in `WP-312`. At the `j`-th regular node let `d_j>0` be the boundary derivative of the current Pick function. Then every finite stage satisfies the exact recurrence

\[
\boxed{
L(f_N)
=
\pi\sum_{\substack{1\le j\le N\\ j\;\mathrm{regular}}}
\frac1{d_j}
\ge0.
}
\tag{5}
\]

Pole reductions leave `L` unchanged. Hence if **any** regular reduction occurs, from its first occurrence onward

\[
L(f_N)\ge \frac{\pi}{d_{j_0}}>0.
\tag{6}
\]

If no regular reduction occurs, the chain only strips original Mangoldt poles. For the finite removed set `S_N`,

\[
\boxed{
C(f_N)
=
A_{\rm M}
+
\sum_{n\in S_N}
\frac{\Lambda(n)\log n}{n+1}
>A_{\rm M}>0.
}
\tag{7}
\]

The sequence is monotone. If the removed-pole union is infinite but the positive series converges, its limiting curvature is still at least `A_M`; if it diverges, no finite second curvature survives. In particular, stripping **all** Mangoldt poles forces divergence, already on the prime subfamily:

\[
\sum_{p\le X}
\frac{(\log p)^2}{p+1}
=
\frac12(\log X)^2+O(\log X)
\longrightarrow\infty.
\tag{8}
\]

Therefore any infinite fixed-node Julia chain whose convergence is strong enough that the relevant high-energy invariants in (1)-(2) pass to the limit still cannot reach the Riemann Gamma asymptotic. More precisely:

\[
\boxed{
\begin{array}{c}
L(f_\infty)=\lim_N L(f_N)
\\[2mm]
\text{and, when all }L(f_N)=0,
\quad C(f_\infty)=\lim_N C(f_N)
\end{array}
\Longrightarrow
f_\infty\text{ cannot have the Riemann Gamma end.}
}
\tag{9}
\]

Thus the infinite-chain escape left by `WP-312` survives only by becoming **nonuniform at infinity**: the chain limit must fail to commute with the high-energy asymptotic extraction that defines the Gamma comparison. A merely convergent infinite Schur/Julia algorithm is not enough. It must exhibit a genuine moving boundary layer, scale-dependent reference, or another mechanism that destroys asymptotic stability while retaining an independent positivity theorem.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + INFINITE-JULIA-CHAIN + ASYMPTOTIC-STABILITY-NO-GO + MONOTONE-REGULAR-DEFECT + MONOTONE-POLE-CURVATURE + EXHAUSTIVE-POLE-DIVERGENCE + CLASSICAL-ALGORITHM-PRIOR-ART + MATCHED-CONTROLS + NOT-WEIL-POSITIVITY`.

## 1. The two asymptotic invariants are the exact Gamma discriminators

The real constant in a Herglotz response is normalization-dependent, so it should not be used to distinguish a candidate geometry from the Riemann archimedean factor. Equations (1)-(2) remove that ambiguity. They also isolate exactly the orders at which `WP-311` and `WP-312` found obstructions.

For `m_-`, `WP-305` proves

\[
\operatorname{Re}m_-(iy)
=
\log y-B+\frac{A_{\rm M}}{y^2}+o(y^{-2}),
\qquad A_{\rm M}>0,
\tag{10}
\]

so (3) follows. The Riemann digamma term instead has

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=
\log\frac y2-\frac1{24y^2}+O(y^{-4}),
\tag{11}
\]

which gives (4). Any exact scalar completion at this stage must therefore preserve `L=0` and reverse the sign of `C`.

These invariants are unchanged by the arbitrary real translations allowed after each regular Julia normalization. They are therefore better suited than constant terms for following an infinite reduction chain.

## 2. Regular reductions make `L` monotone and strictly positive

`WP-312` proves the following one-step formula. Suppose the current Pick function has

\[
\operatorname{Re}f(iy)
=
\log y+c+A\frac{\log y}{y}+O(y^{-1}),
\qquad
\operatorname{Im}f(iy)
=
q+O\!\left(\frac{(\log y)^2}{y}\right),
\qquad q>0.
\tag{12}
\]

At a fixed regular real boundary point `x`, with `d=f'(x)>0`, classical Julia reduction followed by the unique upper-half-plane automorphism restoring the unit logarithmic coefficient gives

\[
L(\mathcal J_x[f])
=
L(f)+\frac{2q}{d}.
\tag{13}
\]

The same calculation shows that the limiting imaginary height `q` survives the normalized step. Pole stripping changes only inverse-power terms and also preserves `q`. Starting from `m_-`, therefore,

\[
q=\frac\pi2
\tag{14}
\]

at every finite stage, and each regular step contributes exactly `pi/d_j`. Induction gives (5).

This already settles every infinite chain containing a regular node **provided the first asymptotic coefficient is stable under the limit**. Since the index set is the natural numbers, any nonempty set of regular stages has a first element `j_0`. After that stage the coefficient can only increase. Even if later derivatives become arbitrarily large and the total series `sum 1/d_j` converges, its limit remains at least `1/d_{j_0}`. There is no cancellation channel inside fixed-node Julia reduction.

Notice what this does *not* prove. Local uniform convergence `f_N -> f_infinity` on the upper half-plane does not by itself imply `L(f_N)->L(f_infinity)`, because `L` samples `y->infinity`. A sequence can converge on every compact set while moving its asymptotic defect farther and farther out. The obstruction is therefore deliberately stated for asymptotically stable convergence rather than silently exchanging the limits `N->infinity` and `y->infinity`.

## 3. Pure pole chains make `C` monotone and positive

If the chain contains no regular step, every stage is the classical pole reduction

\[
f(z)\longmapsto f(z)-\frac{R}{z-x},
\qquad R<0.
\tag{15}
\]

For the reflected Mangoldt source the original poles and residues are

\[
x_n=-\log n,
\qquad
R_n=-\frac{\Lambda(n)}{n+1},
\qquad n=p^k,
\tag{16}
\]

and pole stripping does not move the remaining poles. Along the imaginary axis,

\[
-\frac{R_n}{iy-x_n}
=
\frac{R_nx_n}{x_n^2+y^2}
+i\frac{R_ny}{x_n^2+y^2},
\tag{17}
\]

so its first real correction is

\[
\frac{R_nx_n}{y^2}
=
\frac{\Lambda(n)\log n}{(n+1)y^2}>0.
\tag{18}
\]

Summing finitely many such steps gives (7). Because every increment is positive, every infinite pure-pole chain has only two possibilities at the second asymptotic order: a finite limit `C_infinity >= A_M>0`, or divergence to `+infinity`. Neither can equal `-1/24` if the second asymptotic coefficient passes to the limit.

This statement is stronger than the finite result in `WP-312`: sparsely removing infinitely many poles can keep the correction finite, but cannot change its sign. Exhaustively removing the arithmetic source is even more singular, as the next section shows.

## 4. Exhaustive Mangoldt pole stripping has divergent curvature

It is enough to keep only prime poles. Define

\[
S(X):=
\sum_{p\le X}
\frac{(\log p)^2}{p+1}.
\tag{19}
\]

Since

\[
\frac1{p+1}=\frac1p+O(p^{-2}),
\tag{20}
\]

and `sum (log p)^2/p^2` converges, `S(X)` has the same main asymptotic as

\[
T(X):=
\sum_{p\le X}
\frac{(\log p)^2}{p}.
\tag{21}
\]

Mertens' first theorem gives

\[
A(X):=
\sum_{p\le X}\frac{\log p}{p}
=
\log X+O(1).
\tag{22}
\]

Stieltjes partial summation then yields

\[
\begin{aligned}
T(X)
&=
\int_{2^-}^{X}\log t\,dA(t)
\\
&=
\log X\,A(X)
-
\int_2^X\frac{A(t)}{t}\,dt
\\
&=
\frac12(\log X)^2+O(\log X).
\end{aligned}
\tag{23}
\]

This proves (8). Because all prime-power contributions are also positive, any enumeration that eventually strips every Mangoldt pole has `C(f_N)->+infinity`, independently of the order of removal.

The divergence is not a hidden use of zero data or RH. It follows from the classical prime-weighted Mertens estimate and positivity of the pole increments. Thus the most literal infinite reduction — remove the entire atomic arithmetic boundary source one pole at a time — destroys rather than repairs the finite second curvature needed for Gamma.

## 5. What convergence would be sufficient, and what escape remains

The theorem does not require a particular Banach or Hilbert topology for the full Pick functions. It requires only the amount of asymptotic stability needed to make the claimed Gamma identification meaningful:

- if regular reductions occur, the limit procedure must preserve the functional `L` in (1);
- if the chain is purely polar, it must preserve the second coefficient `C` in (2).

Any topology or convergence theorem that justifies those passages is enough for (9). Conversely, if an infinite Julia chain evades the result, it must fail one of those passages. The only remaining scalar fixed-node escape is therefore not “take infinitely many reductions” in the abstract, but a precise noncommutation:

\[
\lim_{N\to\infty}\lim_{y\to\infty}
\neq
\lim_{y\to\infty}\lim_{N\to\infty}
\tag{24}
\]

at the first discriminator order relevant to Gamma.

That is a real structural requirement. Classical infinite Schur/Nevanlinna algorithms can converge, and their convergence can depend on the placement of interpolation points. Such convergence alone says nothing about (24). A viable Mathia construction would have to derive the moving scale or boundary-layer mechanism that makes the noncommutation canonical, while still explaining positivity independently. Choosing nodes as a function of the observation scale merely to cancel the known Gamma defect would be target programming and remains excluded by the research contract.

## 6. Aggressive falsification and matched controls

The regular-node monotonicity is not arithmetic-specific. Any Pick source with `q>0` and a unit logarithmic end acquires `+2q/d` under the normalized fixed-node Julia step. Thus the sign is a general consequence of Pick positivity plus fixed boundary reduction, not evidence that the Riemann arithmetic has been geometrized.

The pole sign is also broader than the Mangoldt source. Any positive Herglotz atomic measure supported on the negative real axis has negative pole residues `R<0` at locations `x<0`, so pole stripping contributes `Rx>0` to the real `y^-2` curvature. The arithmetic source adds the stronger fact (8): stripping all of its poles has infinite positive curvature.

These controls matter because they prevent a false positive interpretation. The monotone signs are genuine geometric consequences, but they point in the wrong direction for the Riemann Gamma channel and are shared by nonarithmetical controls. The result is therefore an obstruction to the scalar Julia route, not a candidate Weil positivity mechanism.

Could alternating reduction with **augmentation** cancel the defect? Yes in principle, because augmentation is the inverse operation and can reinsert information. But then one is no longer following a reduction-only positive elimination mechanism; arbitrary augmentation parameters can program a target Pick function. Such a route would need an independent Mathia construction fixing every augmentation parameter before the Gamma comparison. It is outside the present claim rather than an exception to it.

Could matrix/operator-valued boundary data evade the scalar monotonicity? Also yes. The present result does not address operator-valued generalized resolvents, noninvertible maps, a new archimedean channel, or a nonseparable finite–archimedean geometry. Those remain legitimate because they change the mechanism rather than taking a singular limit of the same scalar fixed-node algorithm.

## 7. Prior-art and novelty audit

Julia–Nevanlinna reduction, augmentation, positivity preservation, Schur-complement interpretation, and continued-fraction parametrization are classical. Agler and Young give a modern treatment and explicitly trace the recursive boundary method to Julia and Nevanlinna. No novelty is claimed for those operations.

Infinite recursive Nevanlinna–Pick algorithms and their convergence theory are also prior art. Georgiou and Khargonekar, for example, prove convergence of a recursive linear-fractional Nevanlinna–Pick algorithm under conditions on the chosen interpolation points. This is exactly why local or algorithmic convergence cannot be presented as the missing result here: the Mathia question is whether the **Riemann-specific asymptotic discriminator** survives that limit.

The prime estimate (8) is likewise classical. It follows immediately from Mertens' first theorem by partial summation; no novelty is claimed for the asymptotic.

A bounded literature audit over boundary Julia–Nevanlinna reduction, infinite Schur/Nevanlinna recursion, Herglotz asymptotics, von-Mangoldt transforms, and Riemann Gamma asymptotics did not identify the specific monotone collision (5)-(9) for the `WP-305` source. The Mathia-specific contribution is narrower: once `WP-305` fixes the positive reflected Mangoldt source and `WP-312` fixes the one-step defects, countable fixed-node iteration does not create a new cancellation mechanism under any convergence strong enough to preserve the very asymptotic coefficients used to claim Gamma matching.

Relevant standard references:

- Agler–Young, *Boundary Nevanlinna-Pick interpolation via reduction and augmentation*, arXiv:0905.4759, DOI `10.1007/s00209-010-0696-3`.
- Georgiou–Khargonekar, *Spectral Factorization and Nevanlinna-Pick Interpolation*, SIAM J. Control Optim. 25 (1987), 754–766, DOI `10.1137/0325043`.
- Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.
- NIST DLMF 5.11.E2: https://dlmf.nist.gov/5.11.E2

## 8. Consequence for the research frontier

`WP-312` left “an infinite chain with proved convergence” as a formal escape. The present result narrows that substantially. **Asymptotically stable convergence is not enough.** Regular fixed-node steps have a monotone positive first defect; pure pole steps have a monotone positive second defect; exhaustive pole stripping diverges.

Therefore a future scalar boundary construction must explain a canonical nonuniform high-energy limit, not merely establish convergence of infinitely many reductions. The natural decisive test is now two-scale: derive the candidate limit without looking at Gamma, then prove exactly how its reduction depth must grow with spectral height and whether the resulting `N=N(y)` boundary layer has a regulator-independent limit. If the required growth law is chosen only after matching `-1/24`, the route has failed the canonicity gate.

This also sharpens the boundary between scalar and genuinely new structure. If no intrinsic moving-scale law is forced by Mathia, further fixed-node scalar Julia/Schur iteration is exhausted. Attention should move to operator/matrix-valued or nonseparable finite–archimedean constructions where the sign theorem acts before scalarization.

## Conclusion

Countably many fixed boundary Julia reductions do not gain a hidden cancellation unavailable at finite depth. At every finite stage the first relevant asymptotic defect moves monotonically away from the Riemann Gamma target, and any limit that faithfully transports those asymptotic invariants inherits the same obstruction. An all-pole infinite chain is worse: its curvature stays positive, and removing the full Mangoldt support makes it diverge like at least `1/2 (log X)^2` along the prime exhaustion.

The only infinite scalar Julia escape left by this analysis is therefore a **nonuniform-at-infinity limit whose boundary layer is itself canonically forced**. That is a much narrower research target than generic infinite recursion, and it separates a potentially new mechanism from another repackaging of classical Pick positivity.
