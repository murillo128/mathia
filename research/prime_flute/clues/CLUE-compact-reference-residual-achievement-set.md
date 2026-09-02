---
id: CLUE-prime-flute-compact-reference-residual-achievement-set
type: research-clue
status: proposed
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-164-connected-ruelle-cusp-is-compact-reference-unstable.md
  - research/visual_exploration/findings/VIS-002-compact-reference-residual-achievement-interval.md
  - research/visual_exploration/visualizations/prime-flute-compact-reference-achievement-set.md
---

# What is the full achievement set of compact-reference cusp-coefficient residuals?

## Observation

PF-164 gives the exact additive coefficient change for arbitrary finite-support modifications of the ordered all-composite comparison surface. VIS-002 isolates the legal `+2` subfamily and proves that, after subtracting its obvious integer displacement, the residual cotangent corrections form an achievement set whose sufficiently far tails are compact intervals. Therefore the closure of the *full* compact-reference residual family already has nonempty interior; it cannot be only a Cantor dust.

The same decomposition also gives, for a general replacement `q'_j`,

\[
2\delta_j
=
2(q'_j-q_j)
+
2\bigl(f(q'_j)-f(q_j)\bigr),
\qquad
f(x)=\pi\cot(\pi/x)-x.
\]

The first term lies in `2Z`, while the second is a small signed nonlinear residual whose possible values are constrained jointly by ordering and composite-label admissibility.

## Research question

For a sufficiently far tail, classify the closure

\[
\mathcal E_J
=
\overline{
\left\{
2\sum_{j\in F}
\bigl(f(q'_j)-f(q_j)\bigr):
F\ \text{finite},\ j\ge J,
\ \{q'_j\}\ \text{legal ordered composite replacements}
\right\}
}.
\]

Is `E_J` a single interval, a finite union of intervals, a Cantorval, or another explicitly describable compact set? Determine its exact positive/negative endpoints or sharp asymptotic width as `J -> infinity`, and determine how simultaneous ordering constraints change the naïve Minkowski sum of the one-site residual sets.

## Why it may matter

PF-164 establishes severe reference dependence, but it does not describe the *geometry of the reference action* on the cusp coefficient. VIS-002 shows that the nonlinear residue already has interval interior in a restricted subfamily. A full classification would say whether quotienting the obvious `2Z` displacement leaves only a small continuous gauge freedom, a more structured compact set, or some residual invariant.

That distinction is relevant before abandoning every normalized version of the connected cusp coefficient: an intrinsic quantity could only survive if it is constant on, or descends through, the full compact-reference action.

## Decisive test

Write each legal local move as its integer displacement plus the residual atom `2(f(q'_j)-f(q_j))`. First derive exact monotone envelopes from the neighboring reference labels. Then analyze the infinite tail as a constrained achievement/Minkowski-sum system.

A decisive positive result would prove that the tail domination and ordering constraints force `E_J` to be an explicit interval (or finite union) and compute its endpoints/asymptotic width. A decisive negative result would exhibit persistent gaps after arbitrarily deep tails, establishing Cantorval or other non-interval topology. The restricted `+2` interval from VIS-002 must appear as a subset/control in either analysis.

## Evidence boundary

VIS-002 proves interval filling only for one legal positive `+2` perturbation family after removing its `4|F|` integer contribution. It does not classify negative moves, larger displacements, multiple choices at one site, or the coupled ordering constraints of the complete all-composite reference family.

No claim is made that any topology of `E_J` is intrinsic to the full prime flute, relevant to RH, or preserved by genuine spectral/scattering/Ruelle objects. This clue concerns only the PF-161--PF-164 selected relative cusp coefficient and the exact compact-reference action already shown to affect it.
