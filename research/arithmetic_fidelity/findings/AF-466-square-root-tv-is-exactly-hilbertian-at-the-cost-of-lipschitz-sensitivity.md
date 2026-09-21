# AF-466 — Square-root TV is exactly Hilbertian at the cost of Lipschitz sensitivity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-METRIC-REPAIR`, `QUANTITATIVE-FIDELITY`, `NONLINEAR-TARGET`, `NO-NOVELTY-CLAIM`

## Claim

AF-464 shows that a Hilbert-valued nonlinear encoder cannot preserve total-variation geometry with complexity-independent bi-Lipschitz constants when the source contains growing Hamming cubes. AF-465 then shows that merely removing those cubes is not a positive Hilbert-fidelity certificate. There is, however, an exact positive repair for the full probability simplex once the source metric itself is changed in a controlled way.

Let `A` be finite or countable and let

\[
\Delta(A)=\left\{\mu\in\ell^1(A):\mu(a)\ge0,\ \sum_{a\in A}\mu(a)=1\right\}.
\]

Use the Arithmetic Fidelity convention

\[
d_{TV}(\mu,\nu)=\|\mu-\nu\|_1,
\tag{1}
\]

so `0<=d_{TV}<=2`. Define

\[
H=L^2(A\times[0,1],\#\otimes dt)
\]

and the nonlinear subgraph map

\[
\Phi(\mu)(a,t)=\mathbf 1_{[0,\mu(a)]}(t).
\tag{2}
\]

Then:

1. **The square-root TV metric embeds isometrically in Hilbert space.** For all `mu,nu in Delta(A)`,
   \[
   \boxed{
   \|\Phi(\mu)-\Phi(\nu)\|_H^2
   =\|\mu-\nu\|_1
   =d_{TV}(\mu,\nu).
   }
   \tag{3}
   \]
   Hence
   \[
   \boxed{
   (\Delta(A),d_{TV}^{1/2})\hookrightarrow H
   }
   \tag{4}
   \]
   is an exact isometric embedding. In fact every image point lies on the unit sphere because `||Phi(mu)||_H^2=sum_a mu(a)=1`.

2. **Relative to the original TV metric, inverse recovery is uniformly stable.** Since `d_{TV}<=2`,
   \[
   \|\Phi(\mu)-\Phi(\nu)\|_H
   =d_{TV}(\mu,\nu)^{1/2}
   \ge \frac1{\sqrt2}d_{TV}(\mu,\nu).
   \tag{5}
   \]
   Thus the map has a positive complexity-independent lower TV gain even on the full infinite simplex.

3. **The price is infinite upper TV-Lipschitz sensitivity.** There is no finite `L` such that
   \[
   \|\Phi(\mu)-\Phi(\nu)\|_H\le Ld_{TV}(\mu,\nu)
   \tag{6}
   \]
   for all distinct laws. For two atoms `a!=b`, take
   \[
   \mu=\delta_a,
   \qquad
   \nu_\varepsilon=(1-\varepsilon)\delta_a+\varepsilon\delta_b.
   \]
   Then
   \[
   d_{TV}(\mu,\nu_\varepsilon)=2\varepsilon,
   \qquad
   \|\Phi(\mu)-\Phi(\nu_\varepsilon)\|_H=\sqrt{2\varepsilon},
   \]
   and therefore
   \[
   \frac{\|\Phi(\mu)-\Phi(\nu_\varepsilon)\|_H}
        {d_{TV}(\mu,\nu_\varepsilon)}
   =\frac1{\sqrt{2\varepsilon}}
   \longrightarrow\infty.
   \tag{7}
   \]
   The map is exactly `1/2`-Hölder in TV, not TV-Lipschitz.

4. **This is the precise metric-change escape left open by AF-464.** AF-464 assumes a finite upper TV-Lipschitz modulus `L(F)` and proves a lower-modulus obstruction from metric type. The map `(2)` escapes because its upper TV modulus is infinite, not because Hilbert geometry somehow defeats the cube obstruction. Equivalently, it preserves the snowflaked metric `d_{TV}^{1/2}` exactly rather than preserving `d_{TV}` bi-Lipschitzly.

5. **The repair is universal for TV source families but is not a compression theorem.** Every subset `S subset Delta(A)` inherits `(3)` without any thinness, doubling, cube-exclusion, or arithmetic hypothesis. At the same time `Phi` retains the complete labeled law: for every atom,
   \[
   \mu(a)=\int_0^1\Phi(\mu)(a,t)\,dt.
   \tag{8}
   \]
   Thus AF-466 is a category boundary showing exactly how a Hilbert representation can recover full TV information after a metric deformation. It is not evidence that a later finite-dimensional, compact, spectral, quotient, positive, or asymptotic compression preserves the same information.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{full-simplex TV data are exactly Hilbertian after }d\mapsto\sqrt d,
\text{ and the cost is singular forward sensitivity in the original TV scale.}
}
\tag{9}
\]

## Exact derivation

For every `mu in Delta(A)`, Tonelli gives

\[
\|\Phi(\mu)\|_H^2
=\sum_{a\in A}\int_0^1
\mathbf 1_{[0,\mu(a)]}(t)\,dt
=\sum_{a\in A}\mu(a)
=1.
\tag{10}
\]

For two laws, the square of the pointwise difference of the two indicators is the indicator of the symmetric difference of the intervals. Since two intervals anchored at zero have symmetric-difference length `|mu(a)-nu(a)|`,

\[
\begin{aligned}
\|\Phi(\mu)-\Phi(\nu)\|_H^2
&=\sum_{a\in A}\int_0^1
\left|
\mathbf 1_{[0,\mu(a)]}(t)-
\mathbf 1_{[0,\nu(a)]}(t)
\right|^2dt\\
&=\sum_{a\in A}|\mu(a)-\nu(a)|\\
&=\|\mu-\nu\|_1.
\end{aligned}
\tag{11}
\]

This proves `(3)` directly and does not require a finite-dimensional approximation or compactness argument.

Equation `(8)` also gives an explicit left inverse on the image. The representation therefore separates two different issues that AF-464 intentionally couples in its bi-Lipschitz distortion:

- **inverse conditioning:** target closeness controls source TV because `(5)` gives a fixed positive lower linear gain;
- **forward sensitivity:** arbitrarily small source changes are magnified from scale `d` to scale `sqrt(d)`, making the upper linear modulus infinite by `(7)`.

The distinction is load-bearing. A downstream theorem that only requires injectivity or a stable inverse can tolerate `(2)`. A theorem that requires a uniformly bounded response to small TV perturbations cannot.

## Relation to Schoenberg negative type

The metric identity is classical. Schoenberg proved that `L^p` and `ell^p` metrics for `0<p<=2` become Hilbert-embeddable after raising the metric to the power `p/2` or less. Setting `p=1` gives precisely the general statement that the square root of an `L^1` metric embeds isometrically into Hilbert space.

In modern metric-embedding language, a metric space `(X,d)` is of negative type when `(X,sqrt(d))` embeds isometrically into Hilbert space. The probability simplex with `d_{TV}=||.||_1` is therefore a concrete negative-type source. Equation `(2)` is an explicit layer-cake/cut realization specialized to nonnegative `ell^1` probability vectors.

The explicit formula matters for Arithmetic Fidelity because it exposes where the information lives. The Hilbert coordinate `(a,t)` records both the original atom label `a` and the subgraph level `t`; no provenance has been discarded before taking the Hilbert norm.

## Strict relation to AF-456, AF-464, and AF-465

AF-456 proves that no **bounded linear/barycentric** map from the full infinite probability simplex into Hilbert space can be bounded below in the original `ell^1`/TV metric. AF-466 does not contradict it: `Phi` is nonlinear as a map of probability laws. In particular,

\[
\Phi\!\left(\tfrac12\mu+\tfrac12\nu\right)
\ne
\tfrac12\Phi(\mu)+\tfrac12\Phi(\nu)
\]

in general.

AF-464 removes linearity but assumes a finite upper TV-Lipschitz modulus. AF-466 again lies exactly outside that hypothesis by `(7)`. It therefore realizes one of AF-464's declared escape routes — change the source metric or accept growing/singular upper sensitivity — in an exact, dimension-free form.

AF-465 shows that deleting known negative substructures such as Hamming cubes cannot certify Hilbert fidelity in the original metric. AF-466 supplies a different kind of positive statement: instead of trying to characterize which TV subspaces embed bi-Lipschitzly, it identifies a universal metric transformation under which **every** TV source family becomes Hilbertian. The theorem is therefore a repair of metric category, not a positive certificate for the original metric.

## Prior art and novelty audit

The embedding mechanism is classical and **no theorem-level novelty is claimed**.

- I. J. Schoenberg, **“Metric Spaces and Positive Definite Functions,”** *Transactions of the American Mathematical Society* 44(3), 522–536 (1938), DOI `10.1090/S0002-9947-1938-1501980-0`. Theorem 5 states that `ell^p` and `L^p`, `0<p<=2`, become Hilbert-embeddable when their metrics are raised to exponent `p/2` or less; `p=1` gives the square-root `L^1` case used here.
- Jeff Cheeger and Bruce Kleiner, **“Differentiating maps into L1, and the geometry of BV functions,”** *Annals of Mathematics* 171(2), 1347–1385 (2010). The paper uses the standard modern convention that `(Y,d)` has negative type when `(Y,d^{1/2})` embeds isometrically into Hilbert space, and recalls the cut-metric representation of `L^1` distances.

The only line-specific contribution is the exact placement of this classical fact against AF-456/464/465: it identifies a fully explicit positive Hilbert repair for the same probability-law source, while proving that the repair pays exactly in the assumption that made the nonlinear TV obstruction possible — finite forward Lipschitz sensitivity in the original metric.

## Boundary and falsification audit

- **This changes the metric.** Equation `(4)` is an isometry for `sqrt(d_TV)`, not for `d_TV`. A downstream result calibrated to linear TV scale cannot silently substitute the snowflaked metric.
- **This is not Hellinger distance.** The usual square-root-density map `mu -> (sqrt(mu(a)))_a` gives Hellinger geometry, whose squared distance is `sum_a (sqrt(mu(a))-sqrt(nu(a)))^2`. Equation `(2)` instead gives exactly the square root of `ell^1`/TV distance through subgraph indicators.
- **The representation is infinite-dimensional and lossless.** It retains atom labels and all coordinate masses. It does not show that a finite-rank or compact Hilbert compression can preserve the same fidelity; AF-454/455 remain relevant after such postprocessing.
- **Finite upper sensitivity is genuinely absent.** The failure in `(7)` occurs already on two atoms and arbitrarily small mixture perturbations. It is not an infinite-alphabet artifact.
- **The lower linear bound uses bounded diameter.** The constant `1/sqrt(2)` in `(5)` comes from `d_TV<=2` on probability laws. For an unbounded `L^1` cone, `sqrt(d)` does not have a global positive lower linear gain.
- **No prime discriminator is created.** The construction works unchanged on any alphabet. Its role is to classify a permitted information transport, not to distinguish rational primes from matched controls.
- **No claim is made that the square-root metric is acceptable downstream.** That is a separate compatibility question that must be proved for each concrete arithmetic mechanism.

## Arithmetic specialization

Take `A=P`, the rational primes, and let `Delta(P)` be arbitrary probability laws over prime labels. Then the same map gives

\[
\|\Phi(\mu)-\Phi(\nu)\|_H
=\|\mu-\nu\|_1^{1/2}
\tag{12}
\]

for every pair of prime-weight laws, with explicit recovery of each prime weight by `(8)`.

So there is no abstract obstruction to placing the **entire** prime-weight simplex in a Hilbert space with exact square-root-TV geometry. What AF-456 and AF-464 forbid is stronger and more relevant to many spectral proposals: preserving the original TV geometry with a bounded affine carrier or with uniform two-sided Lipschitz control.

A prime-facing construction can therefore use this escape only after answering a concrete compatibility question: does its later analytic/sign/spectral operation consume distinctions at square-root-TV scale, or does it require the original linear TV scale together with bounded forward sensitivity? If the latter, AF-466 is not a repair. If the former, the Hilbert target itself is no longer the obstruction and the next audit must ask which subsequent compression first discards the labeled subgraph information retained by `Phi`.

## Consequence for the line

The source-geometry frontier after AF-465 should no longer be phrased simply as “find a source property implying Hilbert embeddability.” There are two different positive problems:

1. **original-metric fidelity:** identify genuine source geometry yielding a uniform bi-Lipschitz Hilbert/recovery theorem in the metric the downstream mechanism actually consumes;
2. **metric-compatible fidelity:** determine whether the downstream discriminator remains meaningful after a justified metric deformation such as `d -> sqrt(d)`.

AF-466 completely solves the Hilbert embedding part of the second problem for TV source laws, but deliberately leaves the compatibility burden untouched. This turns “change the source metric” from a generic escape hatch into a precise test: the square-root deformation is exact and universal, so any rejection of it must come from the downstream semantics rather than from Hilbert geometry itself.