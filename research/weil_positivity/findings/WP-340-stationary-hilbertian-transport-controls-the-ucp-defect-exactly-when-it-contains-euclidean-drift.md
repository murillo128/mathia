---
id: WP-340
title: Stationary Hilbertian transport controls the UCP defect exactly when it contains Euclidean drift
branch: weil_positivity
status: supported
kind: stationary-negative-type-transport-rigidity
claim_strength: exact classification on the intrinsic dyadic prime-power ray; a translation-invariant squared-Hilbert transport cost from a Z-cocycle forces vanishing UCP Kadison defect under channel convergence exactly when the cocycle has a nonzero invariant drift component, equivalently when its conditionally negative-definite symbol has a positive quadratic Levy-Khinchin coefficient; pure spectral/jump Hilbert geometries remain subquadratic and admit the WP-339 exact-barycentric rare-long-jump obstruction
created: 2026-09-16
related: [WP-115, WP-333, WP-336, WP-337, WP-338, WP-339]
prior_art:
  - I. J. Schoenberg, Metric Spaces and Positive Definite Functions, Transactions of the American Mathematical Society 44 (1938), 522-536, DOI 10.2307/1989894
  - Uffe Haagerup and Soren Knudby, A Levy-Khinchin formula for free groups, Proceedings of the American Mathematical Society 143 (2015), 1477-1489, DOI 10.1090/S0002-9939-2014-12466-X
  - Christian Berg, Jens Peter Reus Christensen, and Paul Ressel, Harmonic Analysis on Semigroups, Graduate Texts in Mathematics 100, Springer, 1984
---

# WP-340 — Stationary Hilbertian transport controls the UCP defect exactly when it contains Euclidean drift

## Claim

`WP-339` classified arbitrary scalar displacement penalties by their tail growth: on the intrinsic dyadic prime-power ray, a cost can uniformly close the moving-tail UCP loophole only if it pays at least quadratically for large logarithmic displacements. That leaves a geometrically natural question rather than another hand-picked scalar cost:

> Can a canonical stationary Hilbert geometry supply the required quadratic tail automatically?

For the full translation-invariant negative-type/Hilbertian class on a prime-power ray, the answer is exact.

Let `U` be a unitary operator on a Hilbert space `H`, let `b:Z->H` be a normalized `1`-cocycle for the representation `n |-> U^n`, and write

\[
b(m+n)=b(m)+U^m b(n),
\qquad b(0)=0.
\tag{1}
\]

Put `xi=b(1)` and let `P` be the orthogonal projection onto the fixed space

\[
H^U=\ker(U-I).
\tag{2}
\]

On the intrinsic dyadic logarithmic ray with spacing

\[
h=\log 2,
\tag{3}
\]

define the stationary squared-Hilbert displacement cost

\[
c_b(|m-n|h):=\|b(m-n)\|^2.
\tag{4}
\]

Then

\[
\boxed{
\lim_{n\to\infty}
\frac{c_b(nh)}{(nh)^2}
=
\frac{\|P\xi\|^2}{h^2}.
}
\tag{5}
\]

Consequently the `WP-339` UCP defect criterion becomes

\[
\boxed{
\text{stationary Hilbertian transport closes the moving-tail defect}
\iff
P\xi\ne0.
}
\tag{6}
\]

Equivalently, if `psi(n)=||b(n)||^2` is written in the classical Levy-Khinchin form for symmetric conditionally negative-definite functions on `Z`,

\[
\psi(n)
=
 a n^2
+
\int_{(0,\pi]}
(1-\cos n\theta)\,\rho(d\theta),
\qquad a\ge0,
\tag{7}
\]

with

\[
\int_{(0,\pi]}(1-\cos\theta)\,\rho(d\theta)<\infty,
\tag{8}
\]

then

\[
\boxed{
\lim_{|n|\to\infty}\frac{\psi(n)}{n^2}=a
=\|P\xi\|^2.
}
\tag{9}
\]

Thus **every pure spectral/jump stationary Hilbert geometry has zero quadratic coefficient and fails the defect test**. The only successful stationary Hilbertian costs contain an honest Euclidean drift `n P xi`; after scaling by `h`, that is precisely the squared logarithmic displacement already identified as the sharp `W_2` tail in `WP-338`--`WP-339`.

This is a decisive negative for a natural escape: replacing an explicitly chosen quadratic transport cost by a stationary Schoenberg/Hilbert geometry does not make the quadratic control emerge from richer spectral structure. The spectral/jump part is asymptotically subquadratic; the entire quadratic tail comes from a translation-invariant affine drift direction.

**Classification:** `EXACT-DERIVED + CLASSICAL-LEVY-KHINTCHINE + CLASSICAL-MEAN-ERGODIC + SOURCE-RAY-SPECIALIZATION + STATIONARY-HILBERTIAN + SHARP-IFF + EXACT-BARYCENTER-CONTROL + MATCHED-CONTROL + DECISIVE-NEGATIVE + NOT-WEIL-POSITIVITY`.

## 1. Every stationary Hilbertian squared distance is a cocycle norm

Conditionally negative-definite kernels are the classical Schoenberg class associated with squared Hilbert distances. On the group `Z`, a translation-invariant negative-type cost can be represented as

\[
\psi(m-n)=\|b(m)-b(n)\|^2
=\|b(m-n)\|^2
\tag{10}
\]

for an affine isometric action, equivalently a unitary representation together with a `1`-cocycle.

For the cyclic group it is enough to inspect one vector. If

\[
\xi=b(1),
\tag{11}
\]

then for `n>=1`, the cocycle identity gives

\[
\boxed{
b(n)=\sum_{k=0}^{n-1}U^k\xi.}
\tag{12}
\]

This is the exact geometric quantity whose growth determines whether the Hilbertian transport cost sees the rare long jumps of `WP-333`--`WP-339`.

No arithmetic has yet entered. The arithmetic specialization will be only the canonical spacing `h=log 2` of the dyadic prime-power ray.

## 2. Mean ergodicity isolates the only quadratic component

Divide (12) by `n`:

\[
\frac{b(n)}n
=
\frac1n\sum_{k=0}^{n-1}U^k\xi.
\tag{13}
\]

The von Neumann mean ergodic theorem gives strong convergence

\[
\boxed{
\frac1n\sum_{k=0}^{n-1}U^k\xi
\longrightarrow P\xi,
}
\tag{14}
\]

where `P` projects onto `H^U`.

Taking norms and squaring,

\[
\frac{\|b(n)\|^2}{n^2}
\longrightarrow
\|P\xi\|^2.
\tag{15}
\]

Since a displacement of `n` dyadic exponent steps has logarithmic length `nh`, (15) is exactly (5).

The decomposition is also geometrically transparent. Write

\[
\xi=P\xi+(I-P)\xi.
\tag{16}
\]

The invariant part sums coherently:

\[
\sum_{k=0}^{n-1}U^kP\xi=nP\xi.
\tag{17}
\]

The orthogonal spectral part satisfies

\[
\left\|
\sum_{k=0}^{n-1}U^k(I-P)\xi
\right\|=o(n).
\tag{18}
\]

Therefore the cost has quadratic asymptotics if and only if the affine action contains a nonzero invariant translation direction. Oscillatory spectral content can change the lower-order geometry but cannot generate the required quadratic tail.

## 3. Levy-Khinchin gives the same classification spectrally

Haagerup--Knudby record the classical `Z` Levy-Khinchin representation: every symmetric conditionally negative-definite `psi:Z->R_+` with `psi(0)=0` has the unique form (7)--(8), up to harmless normalization conventions for the coefficient and measure.

The integral term is always `o(n^2)`. Indeed,

\[
\frac{1-\cos(n\theta)}{n^2}
\le
1-\cos\theta,
\tag{19}
\]

because `|sin(nu)|<=n|sin u|`. For every fixed `theta` in `(0,pi]`,

\[
\frac{1-\cos(n\theta)}{n^2}\to0.
\tag{20}
\]

The right side of (19) is integrable by (8), so dominated convergence gives

\[
\frac1{n^2}
\int(1-\cos n\theta)\,\rho(d\theta)
\longrightarrow0.
\tag{21}
\]

Hence

\[
\boxed{
\frac{\psi(n)}{n^2}\to a.
}
\tag{22}
\]

Comparing (15) and (22) identifies

\[
a=\|P\xi\|^2.
\tag{23}
\]

So the probabilistic and Hilbert-geometric descriptions locate exactly the same surviving component:

\[
\boxed{
\text{quadratic Levy/Gaussian part}
\longleftrightarrow
\text{invariant affine drift}.
}
\tag{24}
\]

The remainder can be arbitrarily rich as a stationary negative-type geometry, but it is asymptotically too weak for the critical UCP tail unless the drift is present.

## 4. The exact dyadic rare-long-jump witness kills every drift-free geometry

Assume

\[
P\xi=0.
\tag{25}
\]

Then by (5),

\[
\frac{c_b(ah)}{(ah)^2}\to0.
\tag{26}
\]

Use the exact `WP-339` dyadic witness on the three prime-power coordinates

\[
y_a=ah,
\qquad y_{2a}=2ah,
\qquad y_{3a}=3ah,
\tag{27}
\]

and modify only the row at `y_{2a}`:

\[
P_{y_{2a}}^{(a)}
=
\left(1-\frac1{a^2}\right)\delta_{y_{2a}}
+
\frac1{2a^2}\delta_{y_a}
+
\frac1{2a^2}\delta_{y_{3a}}.
\tag{28}
\]

The two jumps have exponent displacement `a`, hence Hilbertian cost `||b(a)||^2`. Therefore

\[
J_b(y_{2a})
=
\frac{\|b(a)\|^2}{a^2}
\longrightarrow0.
\tag{29}
\]

At the same time,

\[
\|\Psi_a-I\|=\frac2{a^2}\to0,
\tag{30}
\]

and the two displaced masses are exactly symmetric in the logarithmic coordinate, so

\[
\Psi_a(X)(y_{2a})=y_{2a}
\tag{31}
\]

with no barycentric error.

Nevertheless the Kadison defect stays fixed:

\[
\boxed{
K_a(y_{2a})=(\log2)^2.
}
\tag{32}
\]

Thus **every drift-free stationary Hilbertian geometry fails on the intrinsic dyadic prime-power ray itself**. The failure is not caused by an arbitrary real support, a biased channel, loss of source coordinate, or lack of positivity.

## 5. Nonzero drift succeeds only by reproducing quadratic transport

Now assume

\[
P\xi\ne0.
\tag{33}
\]

Equation (5) gives a positive tail ratio. Hence there are `A` and `alpha>0` such that

\[
c_b(ah)\ge \alpha(ah)^2
\qquad(a\ge A).
\tag{34}
\]

The positive half of `WP-339` then applies: channel convergence together with vanishing `c_b`-transport forces the source-coordinate Kadison defect to vanish uniformly.

But the mechanism is completely exposed by (17). The part doing the work is

\[
\|nP\xi\|^2=n^2\|P\xi\|^2.
\tag{35}
\]

After the dyadic scale conversion `r=nh`, this is just

\[
\frac{\|P\xi\|^2}{h^2}r^2.
\tag{36}
\]

So the successful Hilbertian geometry has not found a softer or more source-selective positivity theorem. It has inserted a Euclidean direction whose squared distance is the same quadratic tail already known to be necessary and sufficient.

Adding any jump/spectral negative-type component to this geometry does not alter that conclusion: it changes lower-order distances, but the invariant drift alone decides the asymptotic threshold.

## 6. Natural candidate geometries fall on the negative side unless they contain drift

The classification immediately audits several tempting stationary Hilbert constructions.

An ordinary unitary-orbit metric

\[
\psi_v(n)=\|U^n v-v\|^2
\tag{37}
\]

is a coboundary cocycle. It is bounded by `4||v||^2`, so its quadratic coefficient is zero and it fails (6).

A pure jump or pure spectral Levy-Khinchin cost has `a=0`, hence is `o(n^2)` and fails. This includes bounded spectral metrics and the usual subquadratic negative-type examples.

The path metric `|n|` on the integer ray is of negative type but has zero quadratic coefficient, so it also misses the rare-long-jump variance. Squaring the Euclidean coordinate to obtain `n^2` succeeds, but that is precisely the invariant-drift case rather than a new stationary spectral mechanism.

These examples matter because they separate **Hilbert embeddability** from the much stronger tail control required here. A positive squared-Hilbert distance can be perfectly canonical and still be too weak to control the unbounded source observable.

## 7. Matched controls show that the surviving quadratic drift is not arithmetic-selective

Nothing in Sections 1--5 uses primality, Mangoldt weights, Gamma factors, the explicit formula, or the archimedean place. Replace the dyadic prime-power coordinates

\[
\{a\log2:a\in\mathbb N\}
\tag{38}
\]

by any equally spaced non-arithmetic lattice

\[
\{ah:a\in\mathbb N\}.
\tag{39}
\]

The cocycle classification and rare-long-jump witness are unchanged.

Therefore a nonzero invariant drift can be useful as a **generic analytic control theorem**, but its positivity cannot by itself explain Weil positivity. A genuinely arithmetic application would still need an independent source theorem forcing this geometry and coupling it to the finite-prime plus archimedean/global Weil structure. The present result removes the possibility that arithmetic selectivity is hidden merely in the stationary Hilbert spectral remainder.

This matched control is also why (6) should not be interpreted as progress toward RH by itself. It closes a natural representation-theoretic escape from the transport obstruction; it does not produce the missing global sign mechanism.

## 8. Relation to WP-115

`WP-115` also uses conditionally negative-definite functions, but at a different mathematical placement.

There, a CND function on the real Kronecker frequency is used as a **Markov/Dirichlet spectral multiplier** on an exact critical positive completion. The theorem says every nontrivial such multiplier accumulates infinite energy on the compulsory prime axes.

Here, a CND function on the discrete translation group `Z` is used as a **squared-Hilbert displacement cost between prime-power exponent sites** for a UCP channel. The issue is not summability of a state against a spectral multiplier; it is whether small transport in that geometry controls the second-moment/Kadison defect of an unbounded coordinate.

The two obstructions therefore complement rather than duplicate each other. `WP-115` kills the scalar Markov spectral-energy route; `WP-340` classifies the stationary Hilbert transport route left after `WP-339`.

## 9. Prior-art and novelty audit

The general harmonic-analysis statements are classical and are not claimed as new mathematics.

Schoenberg's 1938 work is the classical source for the relation between negative-type kernels and Hilbert-space metric representations. Berg--Christensen--Ressel give the systematic semigroup treatment of positive and negative definite functions. Haagerup--Knudby state explicitly, in the introduction to their 2015 paper, the Levy-Khinchin representation (7) for symmetric conditionally negative-definite functions on `Z`; their paper then develops the free-group analogue. The mean ergodic theorem used in (14) is standard.

The Mathia-specific content is the exact synthesis with the live `WP-339` frontier:

- the intrinsic dyadic prime-power geometry reduces every stationary Hilbertian transport candidate to a `Z` cocycle;
- mean ergodicity identifies its asymptotic quadratic tail with the invariant drift component;
- the exact-barycentric dyadic UCP witness kills every drift-free cocycle while preserving channel convergence and vanishing Hilbertian transport cost;
- every successful stationary Hilbertian candidate succeeds only through the explicit Euclidean drift that reproduces quadratic/Wasserstein-2 tail control.

A bounded literature audit found the classical negative-type, cocycle, affine-action, and Levy-Khinchin correspondences, but no external arithmetic theorem is needed for the conclusion. No historical novelty claim is made for the abstract `Z` classification.

## 10. Aggressive falsification and exact boundary

The claim is deliberately narrower than "Hilbert geometry cannot help".

**Nonstationary metrics remain open.** A source-derived Hilbert geometry whose metric changes with exponent location is not represented by a single translation-invariant `Z` cocycle and is outside the theorem.

**Cross-prime coupling remains open.** The argument is one-ray. A genuinely global geometry mixing different primes before positivity is taken may evade the scalar ray classification.

**Operator-valued and noncommutative transport remain open.** The theorem classifies scalar squared-Hilbert displacement costs. It does not reduce an operator-valued transport or correspondence pairing to a scalar CND function.

**A canonical arithmetic theorem forcing drift would be additional structure.** The theorem does not forbid Mathia from producing an invariant affine drift for a deep arithmetic reason. It says only that, once such drift is present, the part that controls the UCP defect is exactly the generic quadratic coordinate direction. Arithmetic content would have to live in the theorem forcing/assembling it, especially in the finite-prime/archimedean bridge, not in the stationary Hilbert positivity itself.

**Quadratic drift is sufficient for this defect, not for Weil positivity.** Closing the Kadison defect does not generate Gamma counterterms, polar terms, a global explicit-formula pairing, or an RH-independent sign theorem for that pairing.

These boundaries are essential: the result closes a natural class of stationary Hilbertian repairs without overclaiming against genuinely global or nonstationary geometric mechanisms.

## Consequence for the Weil-positivity search

The `WP-333`--`WP-339` moving-tail loophole cannot be repaired nontrivially by saying that the source should be close in some canonical stationary Hilbert/Schoenberg metric.

On the intrinsic prime-power ray, the entire class collapses to a sharp dichotomy:

\[
\boxed{
\text{drift-free stationary Hilbert geometry}
\Rightarrow
\text{subquadratic tail}
\Rightarrow
\text{fixed UCP defect can hide in rare long jumps},
}
\tag{40}
\]

whereas

\[
\boxed{
\text{nonzero invariant drift}
\Rightarrow
\text{quadratic tail}
\Rightarrow
\text{defect control already equivalent to the }W_2\text{ scale}.
}
\tag{41}
\]

So a surviving geometry must obtain its source-selective sign from structure **before or beyond** this scalar stationary Hilbert transport layer: a nonstationary arithmetic geometry, cross-prime/global correspondence, operator-valued coupling, or an independent theorem that ties finite and archimedean pieces together. Stationary Hilbert positivity by itself contributes no hidden arithmetic mechanism beyond Euclidean quadratic drift.
