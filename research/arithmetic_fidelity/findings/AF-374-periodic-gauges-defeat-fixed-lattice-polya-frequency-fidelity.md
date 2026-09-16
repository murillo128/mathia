# AF-374 — Periodic gauges defeat fixed-lattice Pólya-frequency fidelity even for entire Gaussian-decay sources

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

Fix `a>0`. Let `f_0:\mathbb R\to(0,\infty)` be an integrable Pólya-frequency function, and let `p:\mathbb R\to(0,\infty)` be bounded and `a`-periodic. Define

\[
f(t)=p(t)f_0(t).
\]

Then every Toeplitz minor whose row locations lie in the fixed lattice `a\mathbb Z` differs from the corresponding minor for `f_0` by a positive column factor. Consequently, all signs and zero patterns of all such minors are unchanged. In particular, `f` is `a\mathbb Z`-Pólya-frequency whenever `f_0` is, even though `f` need not be a Pólya-frequency function on all real translates.

This non-fidelity persists inside a very regular source class. For example,

\[
f_\varepsilon(t)=\exp\!\left(-t^2+\varepsilon\cos(2\pi t)\right)
\]

is strictly positive, entire, integrable, and has Gaussian decay on the real axis. It passes every integer-row Toeplitz-minor test, yet for

\[
\varepsilon>\frac{1}{2\pi^2}
\]

it fails already at order two and hence is not a full Pólya-frequency function.

Therefore a single fixed arithmetic lattice is not made determining merely by imposing positivity, analyticity/entireness, or rapid decay. A source class that hopes to recover full Pólya-frequency structure from one fixed lattice must exclude or trivialize the corresponding positive periodic multiplicative gauge, or retain additional non-lattice information.

## Exact fixed-lattice gauge identity

Take increasing lattice rows

\[
u_i=a n_i,\qquad n_i\in\mathbb Z,
\]

and arbitrary increasing real column locations `x_j`. Since `p` is `a`-periodic,

\[
p(u_i-x_j)=p(a n_i-x_j)=p(-x_j).
\]

Hence

\[
f(u_i-x_j)=p(-x_j)f_0(u_i-x_j).
\]

For every `k\times k` minor,

\[
\det\bigl[f(u_i-x_j)\bigr]_{i,j=1}^k
=
\left(\prod_{j=1}^k p(-x_j)\right)
\det\bigl[f_0(u_i-x_j)\bigr]_{i,j=1}^k.
\]

The prefactor is strictly positive. Thus the entire fixed-lattice determinant-sign structure, at every order and for arbitrary column locations, is invariant under multiplication by positive `a`-periodic functions.

This identifies an exact observational gauge rather than merely another isolated false positive.

## Entire Gaussian-decay false positive

Set `a=1`, take the Gaussian

\[
f_0(t)=e^{-t^2},
\]

and choose the positive entire `1`-periodic gauge

\[
p_\varepsilon(t)=e^{\varepsilon\cos(2\pi t)}.
\]

Then

\[
f_\varepsilon(t)=e^{-t^2+\varepsilon\cos(2\pi t)}
\]

is entire, strictly positive on `\mathbb R`, bounded above and below by positive multiples of the Gaussian on `\mathbb R`, and therefore integrable with Gaussian decay. By the gauge identity, every Toeplitz minor with row locations in `\mathbb Z` has the same sign as the corresponding Gaussian minor, so all integer-row tests pass.

To show that `f_\varepsilon` need not be globally Pólya-frequency, write

\[
\phi(t)=\log f_\varepsilon(t)=-t^2+\varepsilon\cos(2\pi t).
\]

Then

\[
\phi''(t)=-2-4\pi^2\varepsilon\cos(2\pi t),
\]

so at `t=1/2`,

\[
\phi''(1/2)=-2+4\pi^2\varepsilon.
\]

If `\varepsilon>1/(2\pi^2)`, this is positive. For sufficiently small `h>0`, Taylor expansion gives

\[
2\phi(1/2)-\phi(1/2-h)-\phi(1/2+h)<0,
\]

or equivalently

\[
f_\varepsilon(1/2)^2
<
f_\varepsilon(1/2-h)f_\varepsilon(1/2+h).
\]

This violates the order-two Toeplitz total-nonnegativity/log-concavity inequality, so `f_\varepsilon` is not a full Pólya-frequency function.

For period `a`, the analogous gauge `e^{\varepsilon\cos(2\pi t/a)}` gives the same mechanism, with the Gaussian witness violating midpoint log-concavity once `\varepsilon>a^2/(2\pi^2)`.

## Fidelity interpretation

AF-373 showed that all-order determinant arity does not by itself make a convenient fixed lattice a determining sampling set: sampling geometry is an independent fidelity resource. The present result sharpens the obstruction by identifying a hidden invariance of the fixed-lattice observation itself.

The data retained by one lattice cannot see multiplication by a positive periodic gauge of the same period. This remains true at every determinant order. Therefore increasing relational arity all the way to full total positivity cannot recover information that has already been quotiented out by the sampling geometry.

The obstruction also rules out a tempting repair to AF-373: imposing ordinary smoothness or even strong analyticity and decay conditions is insufficient. The explicit `f_\varepsilon` witness is entire and Gaussian-decaying. What is needed is a source-class uniqueness theorem that breaks this gauge, or additional observations that couple distinct lattice phases.

## Riemann specialization

If a candidate RH reduction replaces a translation kernel by checking all Toeplitz minors only at one fixed arithmetic lattice of output locations, then it must justify that the admissible arithmetic source class contains no nonconstant positive periodic gauge ambiguity at that lattice scale, or else retain extra observations that destroy the ambiguity.

Analyticity, positivity, and fast decay alone do not provide such uniqueness. This is an obstruction about representation fidelity; it does not itself distinguish rational primes, characterize the zeta kernel, or prove any zero-location statement.

## Prior-art and novelty audit

The broad phenomenon that fixed-lattice total positivity is weaker than total positivity on all real translates is classical-adjacent rather than new. Michael I. Ganzburg's *On totally positive sequences and functions*, J. Math. Anal. Appl. **361** (2010), 466–471, DOI `10.1016/j.jmaa.2009.07.036`, studies `a`-shift-generating functions and explicitly exhibits periodic degrees of freedom in their representation; it also shows that one mesh does not in general characterize full total positivity, whereas requiring the shift-generating property for every `a>0` recovers it for continuous nonexponential functions.

The ambient Pólya-frequency/total-positivity theory is classical, in particular I. J. Schoenberg, *On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms*, J. Analyse Math. **1** (1951), 331–374, DOI `10.1007/BF02790092`.

No novelty is claimed for fixed-lattice non-determination or for the existence of periodic freedom in shift-generating theory. The useful Arithmetic Fidelity contribution here is the exact positive-periodic gauge identity at the level of every observed minor and the resulting explicit entire Gaussian-decay matched control, which isolates why ordinary regularity cannot repair fixed-lattice information loss.

## Decisive audit rule

For any proposal that claims a single fixed lattice determines full Pólya-frequency structure, first test whether its admissible source class is closed under multiplication by a nonconstant positive periodic function with that lattice period. If it is, the proposal fails immediately: all fixed-lattice minors are gauge-invariant while off-lattice total positivity may change.

Only after this gauge has been excluded or independently fixed is it meaningful to ask whether the remaining source class is determining from that lattice.

## Consequences

The current frontier should distinguish two independent requirements. Full determinant arity is necessary to avoid the bounded-order false positives of AF-372, while sampling/source identifiability is needed to avoid the periodic-gauge false positives exposed here. Neither resource substitutes for the other.

For arithmetic applications, a promising next question is therefore not merely whether a prime-derived kernel is analytic or rapidly decaying, but whether arithmetic structure supplies a canonical phase anchor, quasi-period incompatibility, normalization, or second sampling geometry that destroys every nonconstant periodic gauge compatible with the proposed observation map.