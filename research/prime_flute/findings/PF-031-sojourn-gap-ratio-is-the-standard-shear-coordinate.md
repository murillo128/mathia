# PF-031 — the PF-030 sojourn-time gap ratio is the standard shear coordinate

**Status:** `NEGATIVE/OBSTRUCTION + EXACT REDUCTION + LITERATURE-BACKED`.

PF-030 remains algebraically correct on the four-punctured tangent surface `Y_H`, but its strongest proposed novelty interpretation does not survive comparison with decorated/Thurston Teichmuller geometry. The quantity

```text
T_12 - T_23 = log(d_1/d_2)
```

is, up to the conventional orientation sign, exactly the **Thurston shear coordinate of the underlying ideal quadrilateral**. Thus marked direct cusp-to-cusp sojourn times are reading back a classical geometric coordinate that was already present as the prime-gap cross-ratio; they do not define a new spectral invariant or a new spectral mechanism.

This finding does **not** invalidate PF-029 or the exact PF-030 scattering calculation. It narrows what can count as genuinely new spectral information.

## 1. The tangent quadrilateral and its prime-gap modulus

For three offsets

```text
eta_1 < eta_2 < eta_3,
d_1 = eta_2-eta_1,
d_2 = eta_3-eta_2,
r = d_1/d_2,
```

PF-029 produces the candidate tangent surface `Y_H`, the double of the ideal quadrilateral with ordered vertices

```text
z_1 = -eta_3,
z_2 = -eta_2,
z_3 = -eta_1,
z_4 = infinity.
```

The positive cross-ratio attached to the diagonal `z_1 z_3` is

```text
Y = ((z_1-z_2)(z_3-z_4)) / ((z_2-z_3)(z_1-z_4)).
```

Taking the standard limit at `z_4=infinity` gives exactly

```text
Y = (eta_3-eta_2)/(eta_2-eta_1)
  = d_2/d_1
  = 1/r.
```

Therefore the corresponding Thurston shear is

```text
x = log Y = log(d_2/d_1) = -log r.
```

Reversing the diagonal/orientation changes only the sign convention. In particular,

```text
boxed:
log(d_1/d_2) = +/- (the standard shear coordinate of the ideal quadrilateral).
```

This is not a new coordinate specific to primes. The prime construction merely selects a particular rational value of the ordinary moduli coordinate.

## 2. Standard Teichmuller interpretation

For two ideal triangles sharing a diagonal, Thurston's shear coordinate is the signed displacement needed to glue them along that diagonal. Standard references give two equivalent descriptions:

1. it is the logarithm of the positive cross-ratio of the four ideal endpoints;
2. in decorated Teichmuller theory it is a logarithmic ratio of lambda lengths around the quadrilateral.

Penner's lambda length between two decorated cusps is

```text
lambda = exp(delta/2),
```

where `delta` is the signed hyperbolic distance between the corresponding horocycles along their connecting geodesic. Thus logarithmic combinations of renormalized cusp-to-cusp lengths are precisely the standard raw material from which shear coordinates are constructed.

Useful references:

- Robert C. Penner, *Decorated Teichmuller Theory*, EMS, 2012.
- Standard shear-coordinate formula: for an ideal quadrilateral with vertices `z_1,...,z_4`, `log Y` for the positive cross-ratio `Y` is the shear along the chosen diagonal.
- Fock/Penner/Thurston formulations equivalently express the shear as a log-ratio of lambda lengths.

## 3. PF-030 becomes exactly this classical shear

PF-030 independently computed, using the width-one cusp normalizations of `Y_H`,

```text
C_12 = 2 sqrt(1+r),
C_23 = 2 sqrt(1+1/r).
```

Guillemin's standard formula for the marked direct scattering geodesics gives

```text
T_12 = 2 log(a C_12),
T_23 = 2 log(a C_23),
```

so that the common cusp cutoff cancels:

```text
T_12-T_23
 = 2 log(C_12/C_23)
 = log r
 = log(d_1/d_2).
```

Combining this with Section 1 yields

```text
boxed:
T_12-T_23 = -x
```

for the stated orientation convention, where `x` is the ordinary Thurston shear of the quadrilateral.

Hence the apparently new chain

```text
prime-gap ratio
 -> relative scattering sojourn time
```

factors through the already-known geometric identity

```text
prime-gap ratio
 -> ideal-quadrilateral cross-ratio
 -> Thurston shear
 -> renormalized cusp-to-cusp lengths / sojourn times.
```

The scattering theory is genuinely standard: Guillemin associated sojourn times to scattering geodesics on finite-volume hyperbolic surfaces, and Ji-Zworski related these times to oscillation frequencies/singularities of scattering matrices. What PF-030 reads in the two marked direct channels is therefore a standard Teichmuller coordinate encoded through a standard scattering-geodesic observable.

## 4. Consequence for novelty

The exact identity in PF-030 may still be a useful **prime-flute specialization**, but it should not be presented as a new spectral law.

In particular, proving that the two direct polygon channels are the shortest or first visible scattering singularities would strengthen recoverability, but would not change the mathematical content of the recovered number: it would still be the classical shear/cross-ratio modulus of an ideal quadrilateral.

Therefore this branch is closed as a route to a genuinely new prime/spectral mechanism:

```text
boxed:
marked direct sojourn-time differences do not contain spectral information
beyond the classical ideal-quadrilateral shear already supplied by the
prime-gap cross-ratio.
```

A future inverse-scattering statement of the form

```text
first marked sojourn times -> d_1/d_2
```

would be an explicit reconstruction formula for this special family, not evidence of a new relation comparable to a trace formula or a Riemann-type spectral correspondence.

## 5. What remains genuinely spectral

This negative result does **not** say that all spectral data of `Y_H` reduce to shear coordinates. The metric itself is of course determined by its Teichmuller parameters, but nonlinear spectral objects can respond to those parameters in highly nontrivial ways.

The surviving questions must therefore involve data that are not simply marked renormalized geodesic lengths in disguise, for example:

```text
- locations and multiplicities of resonances/scattering poles as functions of H;
- the scattering determinant after the finite tangent surface is rigorously obtained;
- nontrivial Selberg-zeta zeros, after separating the explicitly known primitive factors;
- small eigenvalue positions, not merely their topologically forced count;
- arithmetic/nonarithmetic specializations of the tangent groups;
- genuinely global transfer-operator spectra rather than a coordinate readout.
```

Even these only become statements about the full prime-flute after the PF-029 Chabauty/geometric-limit gate is proved.

## 6. Relation to earlier findings

PF-031 fits the repeated obstruction pattern:

```text
PF-003: one-step shear potential is a coboundary;
PF-018: local cusp width is gauge;
PF-022: cuff-only half-threshold is renormalizable;
PF-026: standard metric-spine Laplacian gauges away the subdivisions;
PF-031: marked direct scattering-time difference is the ordinary shear itself.
```

The multi-gap geometry remains real and intrinsic, but merely re-expressing its Teichmuller coordinate in another standard geometric language is not enough. A successful spectral candidate must show a nontrivial effect of that geometry on a spectral object, not just recover the geometry from a marked geodesic length.

## Lean candidates

The custom reduction is finite and suitable for formalization:

1. for `z_1=-eta_3`, `z_2=-eta_2`, `z_3=-eta_1`, `z_4=infinity`, prove that the positive cross-ratio limit is `d_2/d_1`;
2. combine with PF-030 to prove `T_12-T_23 = -log(Y)` under the chosen orientation convention;
3. keep the theorem `log(Y) = Thurston shear` and the scattering interpretation as imported geometry/analysis layers.
