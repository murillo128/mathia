# PF-017 — interior/exterior inversion is ambient, not an intrinsic hyperbolic symmetry

**Status:** NEGATIVE/OBSTRUCTION.

## Exact geometry

For one orthogonal circle in the unit-disk construction, write

```text
alpha = pi (1/p - 1/q),
D     = sec(alpha),
rho   = tan(alpha).
```

The two radial extrema of the full Euclidean circle are

```text
r_- = D-rho = sec(alpha)-tan(alpha),
r_+ = D+rho = sec(alpha)+tan(alpha).
```

Hence exactly

```text
r_- r_+ = 1.
```

For `0 < alpha < pi/2`,

```text
0 < r_- < 1 < r_+.
```

Equivalently,

```text
r_- = tan(pi/4-alpha/2),
r_+ = cot(pi/4-alpha/2).
```

Thus the familiar reciprocal pair is real and exact, but one point lies in the Poincare disk and the other lies outside it.

## The crucial model distinction

The hyperbolic plane in the Poincare disk model is the open unit disk

```text
D = { z : |z| < 1 }.
```

A hyperbolic geodesic is the **intersection with D** of a Euclidean line/circle orthogonal to the unit boundary. The full Euclidean orthogonal circle is not itself a single geodesic in the chosen hyperbolic surface; only its interior arc belongs to that copy of `H^2`.

Circle inversion in the unit circle,

```text
I(z) = 1/conj(z),
```

fixes every orthogonal Euclidean circle setwise and exchanges its interior and exterior arcs. Therefore the relation

```text
r_+ = 1/r_-
```

is best understood as an **ambient inversive duality**.

If one equips the exterior region `|z|>1` with the same Poincare-form metric, inversion identifies it isometrically with another copy of the hyperbolic plane. But that exterior copy is not part of the prime-flute quotient constructed from the interior disk. The unit circle is at infinite hyperbolic distance, so the two copies are not two adjacent sheets of one connected hyperbolic surface unless an additional construction is introduced explicitly.

## Spectral consequence

This rules out an important interpretation used heuristically earlier:

```text
interior/exterior pair
    -> two intrinsic hyperbolic channels
    -> spectral involution
    -> s <-> 1-s.
```

The first implication is false for the prime-flute as presently defined.

The interior/exterior involution does not act as a nontrivial self-map of the interior prime-flute Hilbert space `L^2(X_prime)`. It exchanges the chosen disk model with the exterior copy. Consequently it cannot, by itself, provide the operator-theoretic origin of a functional equation or of a scattering symmetry on the prime-flute.

This strengthens PF-016. The standard scattering identity `Phi(s) Phi(1-s)=I` is already universal for finite-area cusped hyperbolic surfaces; PF-017 shows that the visually compelling interior/exterior inversion is not even an intrinsic second channel of the prime-flute whose scattering could explain that identity.

## What survives

The inversion symmetry remains valuable as exact **ambient Euclidean/inversive geometry**:

```text
orthogonal circle is invariant setwise,
r_- r_+ = 1,
inside arc <-> outside arc.
```

It can still motivate algebraic identities or a deliberately doubled construction. But any doubled surface/operator must be defined as a new object and audited independently; its spectral data cannot be attributed to the original prime-flute.

## Novelty assessment

This is not a new theorem of hyperbolic geometry. The facts about the Poincare disk and circle inversion are standard. Its value here is a decisive correction to the prime-flute research program: it removes an apparently natural but invalid route from the original circle picture to an intrinsic `s <-> 1-s` spectral duality.

## Literature anchors

- Cornell notes on the Poincare disk: the underlying space is the open unit disk and hyperbolic lines are intersections of the disk with circles perpendicular to its boundary: https://pi.math.cornell.edu/~mec/Winter2009/Mihai/section7.html
- University of Glasgow hyperbolic-geometry notes: an h-line is `L ∩ D` for an inversive line/circle `L` orthogonal to the boundary, explicitly distinguishing the complete orthogonal circle from the hyperbolic object: https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/hplane.html
- Cornell Math 6640 notes: inversion fixes setwise circles orthogonal to the inversion circle; the same notes define the Poincare disk metric and its geodesics: https://e.math.cornell.edu/people/bdozier/math6640-fall23/course_notes/course_notes6640.pdf
