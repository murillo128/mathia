# PL-058 — Canonically amplified interior Weil boundary layers are exact copies of a smaller window

## Claim

The most direct **spatial tail-renormalization** escape left open by `PL-057` is not a new mesoscopic regime. If the two boundary layers of the localized non-archimedean Weil operator are moved inward and their exponentially smaller natural amplitude is compensated by the corresponding factor, the resulting operator is **exactly** the original boundary problem at a smaller effective window size.

Recall from `PL-051` the prime-power translation operator

```text
H_L=L^2(-L,L),

K_L
 = sum_(log n<2L) Lambda(n)/sqrt(n)
     (T_(log n)+T_(log n)^*),
```

where `T_u` is translation by `u` compressed to `(-L,L)`. Fix inward depths

```text
d_- >= 0,
d_+ >= 0,
D=d_-+d_+,

L' = L-D/2 > 0,
c  = (d_- - d_+)/2.
```

Then the interior interval

```text
I_(L;d_-,d_+)
 = (-L+d_-, L-d_+)
 = c+(-L',L')
```

has half-length `L'`. Let

```text
U_(c,L',L):L^2(-L',L') -> L^2(-L,L)
```

be translation by `c` followed by zero extension. One has the exact finite-section identity

```text
boxed:
U_(c,L',L)^* K_L U_(c,L',L) = K_(L').
```

Now fix `0<R<L'` and let `J_(L;d_-,d_+,R)` embed two inward boundary profiles into

```text
(-L+d_-, -L+d_-+R)
```

and

```text
(L-d_+-R, L-d_+).
```

These are exactly the endpoint strips of the interior interval `I_(L;d_-,d_+)`, so

```text
J_(L;d_-,d_+,R)
 = U_(c,L',L) J_(L',R),
```

with `J_(L',R)` the ordinary endpoint embedding from `PL-051`. Consequently

```text
boxed:
e^(-L)
J_(L;d_-,d_+,R)^* K_L J_(L;d_-,d_+,R)

 = e^(-D/2) B_(L',R),
```

where

```text
B_(L',R)
 = e^(-L') J_(L',R)^* K_(L') J_(L',R).
```

Equivalently, after the unique exponential compensation that restores the natural boundary normalization,

```text
boxed:
e^(D/2)e^(-L)
J_(L;d_-,d_+,R)^* K_L J_(L;d_-,d_+,R)

 = B_(L',R).
```

This is an **exact identity**, not an asymptotic consequence of the prime number theorem. The factor `e^(D/2)` is precisely what changes the original normalization `e^(-L)` into the natural normalization `e^(-L')` of the smaller effective window.

Therefore pure spatial recentering plus its canonical exponential tail amplification does not reveal a second boundary operator. It simply restarts the already-audited family at the remaining half-length `L'`.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
move the two Weil boundary layers inward
+ compensate their e^(-D/2) amplitude loss
+ keep the same prime-translation operator topology
    -> new mesoscopic zeta-sensitive boundary regime.
```

The result does **not** rule out a genuinely `L`-dependent frequency/regularity topology, a renormalization not reducible to spatial recentering, or a construction using the archimedean and pole terms of the full Weil form.

## Exact finite-section covariance

The proof uses only the geometry of compressed translations.

For `f in L^2(-L',L')`, write `Uf` for its translated zero extension to the interior interval `c+(-L',L')`. For a positive lag `u`, compression of a translation to that interval gives

```text
U^* T_u^(L) U = T_u^(L')
```

when `0<u<2L'`, while

```text
U^* T_u^(L) U = 0
```

for `u>=2L'`. At the endpoint `u=2L'` the overlap has measure zero, so the compressed operator is zero as well. The same statements hold for the adjoints.

The ambient sum `K_L` contains all prime-power lags `log n<2L`. After compression to the interior interval, every term with

```text
2L' <= log n < 2L
```

vanishes exactly, while every term with `log n<2L'` becomes the corresponding compressed translation on `(-L',L')` with the same coefficient `Lambda(n)/sqrt(n)`. Hence

```text
U^* K_L U

 = sum_(log n<2L') Lambda(n)/sqrt(n)
     (T_(log n)^(L')+T_(log n)^(L')^*)

 = K_(L').
```

No PNT estimate, explicit formula, analytic continuation, or limiting argument enters this step.

## The asymmetric inward shift does not create extra structure

Allowing `d_- != d_+` might appear to introduce a relative phase or an additional geometric parameter. It does not. The two endpoint locations are

```text
c-L' = -L+d_-,
c+L' =  L-d_+,
```

so the asymmetry only translates the center of the effective interval by

```text
c=(d_- - d_+)/2.
```

Because the underlying finite-section operator is built from translation lags, this common recentering disappears under the unitary identification `U`. The only surviving spatial parameter is the total removed depth

```text
D=d_-+d_+,
```

through the effective half-length `L'=L-D/2` and the scalar normalization factor `e^(-D/2)`.

Thus even asymmetric movement of the two boundary layers cannot generate a new relative prime phase at this level.

## Consequences for every previously audited boundary topology

The identity transfers the existing boundary results without approximation.

### Effective length tends to infinity, fixed depth

If a sequence of inward shifts satisfies

```text
L'_L = L-(d_-(L)+d_+(L))/2 -> infinity
```

with fixed `R`, then the canonically amplified interior-layer operator is exactly `B_(L'_L,R)`. Therefore `PL-051` and `PL-052` apply verbatim:

```text
B_(L'_L,R) -> B_R strongly,
```

but

```text
liminf ||B_(L'_L,R)-B_R||
 >= 1-e^(-R).
```

The amplified tail has the same universal PNT rank-one strong limit and the same prime-Kronecker operator-norm defect as the original outer boundary.

### Effective length and depth both tend to infinity

If also

```text
R_L -> infinity,
R_L <= L'_L,
```

then the amplified interior problem is exactly in the setting of `PL-057`. After the common half-line embedding it has the same universal rank-two strong limit and the same asymptotic Calkin obstruction. Moving deeper into the original window and compensating the lost mass therefore cannot evade the strong/essential split.

### Fixed Sobolev or regularized-determinant probes

Because the amplified operator is literally `B_(L',R)`, every fixed compact/Sobolev sandwich from `PL-055` and the critical `s=1/2` `det_2` analysis from `PL-056` transfer unchanged after replacing `L` by `L'`. Spatial tail amplification does not restore the high-frequency arithmetic information removed by those fixed smoothings.

### Bounded effective length

If `L'` remains bounded, the amplified problem contains only the prime-power lags below the bounded cutoff `2L'`. There is then no hidden large-`L` boundary asymptotic: after recentering, the operator is a bounded-window finite section `B_(L',R)` determined by a uniformly finite collection of prime powers. Sending the ambient `L` to infinity has introduced no new arithmetic degrees of freedom.

## Matched-control and universality audit

The exact finite-section identity is not specific to the rational primes. Replace the coefficients `Lambda(n)/sqrt(n)` and the lag set `{log n}` by any weighted positive-lag system and define the analogous truncated translation sum. Compression from an interval of half-length `L` to an interior interval of half-length `L'` again discards exactly the lags at least `2L'` and reproduces the smaller finite section.

Therefore the recentering identity survives the line's Beurling/generalized-prime control. Rational-prime information re-enters only through the coefficient/lag family inside the restarted smaller problem, where `PL-051`--`PL-057` have already separated universal PNT behavior from prime-log recurrence. The spatial renormalization itself supplies no discriminator.

This also shows why one should not interpret `e^(D/2)` as a new arithmetic counterterm. It is forced by interval geometry plus the already chosen `e^(-L)` normalization:

```text
e^(D/2)e^(-L)=e^(-L').
```

It does not use the zero divisor and it works equally for matched multiplicative controls.

## Boundary conditions and failure modes

The obstruction is deliberately narrow.

1. It applies to the **non-archimedean prime-translation operator `K_L`** of `PL-051`--`PL-057`. The archimedean and pole pieces of the full Weil quadratic form need not obey the same exact spatial finite-section covariance after a boundary recentering.
2. It applies when the moving topology is obtained solely by choosing interior endpoint strips and multiplying by the natural scalar compensation `e^(D/2)`. An `L`-dependent frequency cutoff, weakening Sobolev order, pseudodifferential weight, or other non-spatial operation is not conjugated away by this identity.
3. It does not say that every possible amplified tail is useless. A different normalization could deliberately magnify a smaller residual, but its canonicity and matched-control discrimination would need an independent argument. The present result removes the most geometrically forced compensation.
4. Prime-power threshold discontinuities at finite effective length are not being smoothed or analytically continued. They are simply inherited exactly from `K_(L')`.

These restrictions are essential: extending the conclusion from the prime translation part to the full Weil operator without checking its additional terms would overstate the result.

## Prior-art and novelty audit

The operator-theoretic ingredient is standard finite-section geometry for translation/convolution (Wiener--Hopf-type) operators: an interior interval, after translation to the origin, sees the same compressed lag operator with the cutoff set by its own length. No novelty claim is made for that fact.

The stored contribution is the exact specialization to the current localized Weil prime operator and the resulting no-go consequence for the spatial tail-renormalization branch left open by `PL-057`. Current localized-Weil work, including Suzuki's screw-function construction recorded in `SOURCES.md` for `PL-044`, studies a richer full Weil operator and a different large-aperture spectral problem; it does not supply a reason to regard this exact prime-translation recentering as a new arithmetic spectral invariant.

The novelty audit therefore classifies the result as a **line-specific exact obstruction**, not new Wiener--Hopf theory and not a new formulation of RH.

## Consequences for the research line

`PL-057` left several possible mesoscopic escapes after showing that raw spatial depth `R(L)->infinity` does not help. This result closes the most immediate companion escape:

```text
open a deeper interior layer
+ amplify by the factor needed to restore order-one boundary mass.
```

That procedure is exactly equivalent to decreasing the effective Weil window and starting the same boundary analysis again.

Accordingly, a surviving mesoscopic construction must introduce structure that cannot be removed by this finite-section conjugacy. The remaining natural candidates are specifically **moving frequency/regularity topology**, a genuinely different and independently forced renormalization, or coupling to the full global Weil terms. Pure spatial tail recentering no longer supplies an independent branch.