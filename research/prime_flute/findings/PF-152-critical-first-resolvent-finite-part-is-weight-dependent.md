# PF-152 — critical first-resolvent finite part is weight-dependent

**Status:** `DECISIVE-NEGATIVE / CLASSICAL-ANOMALY + EXACT-DERIVED` for the natural escape route left by PF-151 in which one subtracts the universal critical first-resolvent residue and treats the remaining zeta/weighted finite part as an intrinsic prime-sensitive scalar. The weighted-trace anomaly is classical. The project-specific conclusion is that vanishing of the total Wodzicki residue on matched equal-area prime/shift compact models does **not** canonize the finite part: for every genuinely nonisometric matched pant model there are admissible elliptic weights of the same order whose finite parts differ.

This finding does **not** assert that every conceivable global relative regularization on the exact infinite flute is noncanonical. It rules out obtaining canonicity merely from the PF-151 residue cancellation.

## 1. The finite-part loophole left by PF-151

PF-151 identifies the critical order of the first Laplace resolvent in dimension two:

```text
R_g(mu) = (Delta_g + mu)^(-1) in Psi^(-2),
```

with principal symbol

```text
sigma_-2(R_g)(x,xi) = |xi|_g^(-2),
```

and Wodzicki residue density

```text
wres_x(R_g) = (1/(2 pi)) dA_g.
```

On each exact hyperbolic pant the area is `2 pi`, independent of the two prime-dependent cuff lengths. Consequently, the leading critical logarithmic residue is topology/area only.

A natural attempted repair is therefore

```text
first-resolvent relative operator
  -> cancel/subtract the common logarithmic residue
  -> retain the finite part
  -> use that finite part as a prime-gap spectral scalar.
```

The missing question is whether cancellation of the total residue makes the finite part independent of the regularizing weight. It does not.

## 2. A boundary-free compact audit of one matched pant

The exact prime pant has one cusp and two geodesic cuffs. To test the finite-part mechanism without importing a boundary pseudodifferential calculus, use the standard compact approximation in Fenchel--Nielsen coordinates.

Fix a prime pant index `n` and a common `epsilon>0`. Replace the cusp in the prime pant and in its exact all-composite shift-clone pant by a third geodesic boundary of length `epsilon`, leaving the two distinguished cuff lengths unchanged. Denote the resulting compact hyperbolic pants by

```text
P_{n,epsilon},    P^+_{n,epsilon}.
```

Double each across all three geodesic boundaries. This gives closed genus-two hyperbolic surfaces

```text
(M,g),    (M,h)
```

after choosing the natural doubled marking and pulling the clone metric back to the same smooth closed surface `M`.

Gauss--Bonnet gives exactly

```text
Area_g(M) = Area_h(M) = 4 pi,
```

independently of all three boundary lengths before doubling. Thus this compact model preserves the exact equal-area cancellation relevant to PF-151 while removing cusp and artificial-boundary analytic issues.

Whenever at least one corresponding prime/shift cuff length differs, the two marked hyperbolic metrics are not identical. In particular their cotangent quadratic forms differ somewhere.

Work on scalar half-densities, so no auxiliary choice of volume-unitary identification enters the principal-symbol comparison. Put

```text
A := (Delta_h+mu)^(-1) - (Delta_g+mu)^(-1),    mu>0.
```

Then `A` is a classical pseudodifferential operator of order `-2` with

```text
a_-2(x,xi)
  := sigma_-2(A)(x,xi)
   = |xi|_h^(-2) - |xi|_g^(-2).
```

Because `g` and `h` are not identical,

```text
a_-2 is not identically zero.
```

Nevertheless PF-151's local residue formula and equal area give

```text
Wres(A)
  = (Area_h(M)-Area_g(M))/(2 pi)
  = 0.
```

So this is exactly the strongest version of the proposed loophole: the pole/residue cancels globally before any finite part is extracted.

## 3. Classical weighted-trace anomaly

Let `Q` be an admissible positive invertible elliptic classical pseudodifferential operator of positive order `q`. Its weighted trace is the finite part

```text
tr^Q(A) := f.p._{z=0} Tr(A Q^(-z)).
```

For two admissible weights `Q_0,Q_1` of the same positive order `q`, the classical Cardona--Ducourtioux--Magnot--Paycha anomaly formula is

```text
tr^{Q_1}(A) - tr^{Q_0}(A)
  = -(1/q) Wres(A (log Q_1 - log Q_0)).
```

More generally, for possibly different orders `q_0,q_1`, the discrepancy is

```text
-Wres(A (log Q_1/q_1 - log Q_0/q_0)).
```

Thus `Wres(A)=0` only kills the special change `log Q_1-log Q_0 = constant`. It does not kill the general local anomaly.

That distinction is decisive here: equal hyperbolic area removes the angular average of the critical symbol, but it does not force the whole critical symbol `a_-2(x,xi)` to vanish.

## 4. The ambiguity is nonzero for every genuinely different matched metric

The anomaly can be made explicit rather than merely asserted generically.

Choose any smooth background cotangent norm `r(x,xi)` and define the real degree-zero homogeneous symbol

```text
c(x,xi) := r(x,xi)^2 a_-2(x,xi).
```

Since `a_-2` is not identically zero, neither is `c`.

Take a positive elliptic weight `Q_0` of order `q`. For sufficiently small real `t`, choose an invertible order-zero scalar operator `B_t` with positive principal symbol

```text
sigma_0(B_t) = exp(t c/2),
```

and define

```text
Q_t := B_t^* Q_0 B_t.
```

Then `Q_t` is again positive, invertible and elliptic of the same order `q`, and its leading symbol differs from that of `Q_0` by the factor `exp(t c)`. Hence

```text
sigma_0(log Q_t - log Q_0) = t c.
```

Because `A` has order exactly `-2`, while the logarithmic difference has order zero, only the product of their leading symbols contributes at critical degree `-2`; all symbol-composition derivative terms have lower degree. Therefore, with the standard residue normalization and with `S_r^*M={r=1}`,

```text
Wres(A(log Q_t-log Q_0))
  = t (2 pi)^(-2)
      integral_{S_r^* M} a_-2(x,xi)c(x,xi) dSigma

  = t (2 pi)^(-2)
      integral_{S_r^* M} a_-2(x,xi)^2 dSigma.
```

The last integral is strictly positive. Consequently, for every nonzero sufficiently small `t`,

```text
boxed:

tr^{Q_t}(A) - tr^{Q_0}(A)
  = - t/(q(2 pi)^2)
      integral_{S_r^* M} a_-2(x,xi)^2 dSigma
  != 0.
```

This is stronger than the scalar-volume observation. Even if one deliberately chooses an area-preserving marking so that the **pointwise angular average** of `a_-2` vanishes, a direction-dependent admissible weight detects the nonzero anisotropic part of the relative principal symbol. Weight independence would require the critical principal symbol itself to vanish, i.e. equality of the two metrics at principal-symbol level, not merely equality of total area.

## 5. Why the Kontsevich--Vishik trace does not repair this automatically

There is a canonical trace for broad classes of classical pseudodifferential operators, but its existence at integer critical order is conditional rather than a consequence of total-residue cancellation.

For arbitrary closed manifolds the Kontsevich--Vishik canonical trace is canonical on noninteger-order operators. Extensions at integer order require additional local symbol conditions, classically formulated through vanishing residue density and parity classes; Paycha's uniqueness/existence analysis makes this local requirement explicit. In particular, the standard parity extension is for odd-class operators in odd dimensions and even-class operators in even dimensions.

Our relative first resolvent sits at integer order `-2` in dimension two. The equality

```text
Wres(A)=0
```

is only an integrated statement and by itself does not place `A` in a canonical-trace class. A special area-preserving or parity-compatible gauge may improve the local residue structure, but that is extra structure which must itself be selected and shown intrinsic. The prime-flute construction does not acquire such a choice merely because the two matched pants have the same Gauss--Bonnet area.

Accordingly, PF-152 does not claim that no specially structured canonical trace can ever be defined. It proves the narrower and needed statement:

```text
common Wodzicki residue
  + subtraction of the common logarithmic divergence
```

is **insufficient** to produce a weight-independent finite part.

## 6. Relation to the exact infinite flute

The `epsilon`-pants doubles are an audit device, not a replacement for the exact prime flute. As `epsilon -> 0`, the compact pants converge in the usual Fenchel--Nielsen sense to the exact one-cusp prime and shift-clone pants. PF-152 uses them only to test whether a proposed *local critical finite-part principle* is canonical after the residue has cancelled.

Since the ambiguity already exists on every compact boundary-free approximant with genuinely different marked metrics, no argument of the form

```text
same pant area
  -> same critical residue
  -> therefore the remaining finite part is canonical
```

is valid.

The result does **not** rule out a future global relative invariant if the exact infinite prime/shift pair supplies an independently canonical regularizing operator and one proves that its value is invariant under all admissible equivalent constructions. It also does not rule out PF-148's conditional Krein/scattering phase from a genuinely trace-class squared-resolvent comparison; that channel uses a different operator-ideal mechanism.

Nor does this finding prove that weight anomalies remain bounded away from zero down the tail. The prime/shift metric defect tends to zero, so the displayed quadratic anomaly can itself shrink with `n`. What is ruled out is **intrinsic local canonization by residue subtraction**, not every possible globally correlated renormalized limit.

## 7. Prior art and novelty assessment

The operator-theoretic ingredients are classical and are not claimed as new.

- A. Cardona, C. Ducourtioux, J.-P. Magnot, S. Paycha, *Weighted Traces on Algebras of Pseudo-Differential Operators and Geometry of Loop Groups*, Infinite Dimensional Analysis, Quantum Probability and Related Topics 5 (2002), 503--540, DOI `10.1142/S021902570200095X`, arXiv `math/0001117`. This develops weighted traces on classical pseudodifferential operators and the residue-controlled trace anomalies used above.
- S. Paycha, *Weighted trace cochains; a geometric setup for anomalies*, arXiv `math-ph/0503033` (2005). This gives a systematic residue description of algebraic and geometric discrepancies of weighted regularized traces.
- S. Paycha, *The noncommutative residue and canonical trace in the light of Stokes' and continuity properties*, arXiv `0706.2552` (2007). This isolates the role of vanishing residue density and the parity classes on which the canonical trace exists and is unique.
- L. Maniccia, E. Schrohe, J. Seiler, *Uniqueness of the Kontsevich--Vishik trace*, Proceedings of the American Mathematical Society 136 (2008), 747--752. This gives a precise uniqueness scope for the Kontsevich--Vishik trace and its parity extensions.

Directed searches for weighted/relative resolvent traces and hyperbolic-surface finite-part regularizations found the expected classical pseudodifferential anomaly theory and geometrically finite hyperbolic resolvent literature, but no theorem making the prime-flute equal-area cancellation select a canonical finite part. The novelty claim here is therefore intentionally modest: the new durable content is the **application of the classical anomaly formula to the exact PF-151 escape route**, together with the explicit symbol choice above showing that the ambiguity survives even when the total residue is exactly zero.

This should be read as a project-specific no-go specialization, not a new theorem about weighted traces.

## 8. Adversarial checks and falsification boundary

There are four direct checks.

**Equal-area check.** For a hyperbolic pant with three geodesic boundaries, Gauss--Bonnet gives area `2 pi`; doubling gives area `4 pi`. If the two compact matched doubles did not have equal area, the exact residue cancellation used here would fail.

**Principal-symbol check.** The leading symbol of `(Delta_g+mu)^(-1)` must be `|xi|_g^-2`. The spectral shift `mu` enters only lower orders. If the two marked metrics differ, the relative leading symbol cannot vanish identically.

**Anomaly check.** Recompute the weighted-trace change formula. For equal weight orders it must reduce to `-(1/q) Wres(A(log Q_1-log Q_0))`, up to the conventional orientation of the subtraction. Reversing the convention changes only the sign, not the nonvanishing conclusion.

**Weight-construction check.** On the background unit cosphere, the chosen leading logarithmic ratio is `t a_-2`; hence the residue pairing is proportional to `t integral a_-2^2`, which is strictly nonzero. If positivity/ellipticity of `Q_t` failed, the construction would be invalid; taking `Q_t=B_t^*Q_0B_t` with an invertible order-zero `B_t` prevents that failure.

A surviving finite-part program must therefore supply substantially more than PF-151's residue cancellation. It must identify a geometrically canonical weight/regularization, prove its invariance under the natural marking choices, and then show that the resulting global scalar survives the all-composite shift-clone controls rather than merely repackaging the vanishing metric defect.

## Research consequence

Reject the branch

```text
PF-151 equal-area residue cancellation
  -> subtract the universal logarithmic divergence
  -> canonical first-resolvent finite part
  -> prime-gap-sensitive determinant/trace scalar
  -> RH mechanism.
```

The first implication is false without extra structure: the finite part remains a regularization-dependent quantity. Any surviving critical first-resolvent route must provide an independently canonical regularizer or move to genuinely nonlocal relative spectral/scattering data whose definition does not depend on this weighted-trace choice.