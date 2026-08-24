# PF-023 — Patterson–Sullivan critical data are universal for the prime-flute

**Status:** NEGATIVE/OBSTRUCTION + LITERATURE+DERIVED.

This note closes a broad global Patterson–Sullivan / pressure-exponent branch. The general theorems are classical; the project-specific content is that the already-established coarse prime-flute geometry forces the extremal value of those invariants, so they cannot retain fine prime-gap fluctuations.

## Claim

For the complete zero-twist prime-flute `X_prime = H^2 / Gamma_prime`,

```text
delta(Gamma_prime) = 1,
```

where `delta` is the critical exponent of the Poincaré series. Moreover `Gamma_prime` is of divergence type at `delta=1`. Consequently, after normalization, its Patterson–Sullivan measure on the boundary circle is the ordinary Lebesgue/spherical measure.

Thus the following global quantities cannot be prime-gap spectral signatures:

```text
critical exponent delta,
Patterson–Sullivan boundary dimension,
pressure root corresponding only to delta,
coarse orbital-growth exponent,
normalized Patterson–Sullivan boundary measure.
```

The associated Bowen–Margulis measure is the Liouville measure and has infinite total mass because the prime-flute has infinite area.

## 1. The distinguished cuffs already force `lambda_0 = 0`

PF-021 proved from the exact cuff coordinate

```text
exp(-ell_n/2) = tanh(h_n/4)
```

and the bound

```text
ell_n = O(log n)
```

that there are escaping Følner pants blocks. Hence

```text
inf sigma_ess(Delta_X_prime) = 0.
```

In particular the bottom of the full spectrum is

```text
lambda_0(X_prime) = 0.
```

This step uses only coarse distinguished-cuff growth, not exceptional prime-gap subsequences.

## 2. Elstrodt–Patterson–Sullivan forces `delta = 1`

For an arbitrary Fuchsian group acting on `H^2`, the Elstrodt–Patterson–Sullivan relation is

```text
lambda_0 = 1/4                         if delta <= 1/2,
lambda_0 = delta (1 - delta)          if delta >= 1/2.
```

Sullivan's extension applies to arbitrary discrete groups of hyperbolic isometries; finite generation or geometric finiteness is not required for this implication.

Since a Fuchsian critical exponent satisfies

```text
0 <= delta <= 1
```

and PF-021 gives `lambda_0=0`, the only possibility is

```text
delta(Gamma_prime) = 1.
```

This gives an independent spectral route to the same extremal exponent suggested by the first-kind/parabolic description of PF-012.

## 3. Parabolicity upgrades this to divergence type

PF-012 records that the zero-twist prime-flute lies in the parabolic/first-kind regime of the known tight-flute criterion.

The Hopf–Tsuji–Sullivan equivalences for hyperbolic surfaces identify parabolicity/Brownian recurrence with divergence of the covering group's Poincaré series

```text
sum_{gamma in Gamma} exp(-d(z, gamma z)).
```

The recent infinite-surface literature uses exactly this equivalence when formulating the type problem in Fenchel–Nielsen coordinates.

Because the critical exponent is already `delta=1`, this is divergence at the critical exponent itself. Therefore

```text
Gamma_prime is of divergence type.
```

The parabolicity input matters: a first-kind infinitely generated Fuchsian group need not be assumed divergence type merely from its limit set.

## 4. The Patterson–Sullivan measure is just Lebesgue measure

For a non-elementary divergence-type Fuchsian/Kleinian group, the conformal density of dimension `delta(Gamma)` is unique up to scale.

At `delta=1` on `S^1`, ordinary spherical/Lebesgue measure is a `1`-conformal density. Uniqueness therefore gives, after probability normalization,

```text
mu_PS = normalized Lebesgue measure on S^1.
```

So the boundary measure itself contains no distinguished prime-gap weighting. In particular, no statistic depending only on

```text
(S^1, visual metric, mu_PS)
```

can distinguish the prime-flute from another divergence-type Fuchsian group with `delta=1`.

This is stronger than the coarse statement that the limit set is the full circle: the canonical critical conformal measure is also the standard one.

## 5. Bowen–Margulis consequence

With `delta=1` and the Lebesgue conformal density, the Bowen–Margulis measure coincides, up to normalization conventions, with Liouville measure on `T^1 X_prime`.

The prime-flute contains infinitely many pairs of pants, each of area `2 pi`, hence

```text
area(X_prime) = infinity.
```

Therefore the Bowen–Margulis/Liouville measure has infinite total mass.

This rules out importing finite-measure thermodynamic conclusions without an additional infinite-measure normalization.

## 6. Transfer-operator consequence

A standard thermodynamic construction often identifies `delta` as the real parameter where a pressure vanishes or a leading transfer-operator eigenvalue reaches `1`.

For the prime-flute, any candidate whose only proposed arithmetic content is

```text
pressure(s) = 0  <=>  s = delta
```

is therefore already fixed at

```text
s = 1.
```

That value is forced by the coarse amenable/parabolic geometry and is insensitive to the prime-gap fluctuations.

This does **not** rule out transfer operators carrying finer information in their non-leading spectrum, relative determinants, cross-cusp channels, or correlation/return data. It rules out the critical exponent / leading-pressure root as the sought prime-specific invariant.

## 7. Relation to the earlier findings

The result sharpens PF-012 and PF-021:

```text
PF-021:
    distinguished cuff growth
      -> escaping Folner blocks
      -> lambda_0 = 0

PF-023:
    lambda_0 = 0
      -> delta = 1

PF-012 + Hopf–Tsuji–Sullivan:
    parabolicity
      -> divergence at s = 1
      -> divergence type

therefore:
    Patterson–Sullivan measure = Lebesgue.
```

It also complements PF-015/PF-016: another tempting globally spectral quantity is universal before one reaches the multi-gap geometry.

## 8. Novelty check

The ingredients are established literature:

- Patterson and Sullivan relate the critical exponent of arbitrary Fuchsian/discrete hyperbolic groups to the bottom of the Laplacian;
- Hopf–Tsuji–Sullivan relates recurrence/parabolicity, ergodicity and divergence of the Poincaré series;
- divergence-type groups have a unique Patterson–Sullivan conformal density at the critical exponent;
- when the critical exponent is the boundary dimension `1`, that density is normalized Lebesgue measure.

Relevant literature anchors include S. J. Patterson, *Spectral theory and Fuchsian groups* (1977); D. Sullivan, *The density at infinity of a discrete group of hyperbolic motions* (1979); the modern tight-flute/type-problem work of Arredondo–Morales–Ramírez Maluendas and Basmajian–Hakobyan–Šarić; and standard divergence-type Patterson–Sullivan uniqueness results.

Targeted searches did not locate a prior prime-endpoint specialization. No novelty is claimed for the general theorem. The substantive project result is negative: **the exact prime-flute sits at the universal extremal Patterson–Sullivan exponent and measure, so this entire global branch cannot encode the fine prime-gap fluctuations.**

## 9. What remains alive

This does not make the group dynamics trivial. Possible prime-specific data may still survive in

```text
multi-gap cross-ratios,
non-leading transfer spectra,
return-time/correlation asymptotics,
relative scattering data,
right-limit operators,
renormalized cross-cusp interactions.
```

Those objects use the action/group geometry in addition to the bare Patterson–Sullivan measure and are not ruled out here.

The ambient interior/exterior inversion duality remains exactly as in PF-017; it does not change the intrinsic Patterson–Sullivan conclusion for the interior hyperbolic surface.
