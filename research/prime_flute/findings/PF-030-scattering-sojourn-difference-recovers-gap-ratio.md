# PF-030 — a scattering sojourn-time difference exactly recovers a consecutive-gap ratio

**Status:** `EXACT-DERIVED ON THE PF-029 TANGENT SURFACE + LITERATURE-BACKED SCATTERING INTERPRETATION / CONDITIONAL ON THE PF-029 FULL GEOMETRIC-LIMIT GATE`.

This finding strengthens PF-029 in a genuinely spectral direction. For the first nontrivial tangent surface — the four-punctured sphere obtained from three offsets — a ratio of two consecutive prime gaps is not merely a Teichmuller modulus or a closed-geodesic length. It appears exactly as a **difference of two cusp-to-cusp sojourn times**, and those sojourn times are standard oscillation frequencies of the scattering matrix in Guillemin's theory.

The identity is exact on the finite-area tangent surface `Y_H`. Implantation of this datum into the full infinite prime-flute remains conditional on the Chabauty/pointed-geometric convergence gate stated in PF-029.

## 1. Four-punctured tangent surface

Take the three-offset pattern

```text
eta_1 < eta_2 < eta_3,
d_1 = eta_2 - eta_1,
d_2 = eta_3 - eta_2,
r = d_1/d_2.
```

PF-029 produces the finite-area reflection-symmetric four-punctured sphere `Y_H`, the double of the ideal quadrilateral with finite cusp fixed points

```text
c_i = -eta_i
```

and one cusp at infinity.

For the three finite cusp parabolics, write

```text
Q(c,D)
 = [[1+cD, -c^2 D],
    [D,       1-cD]].
```

The exact width parameters are

```text
D_1 = 2/d_1,
D_2 = 2(1/d_1 + 1/d_2),
D_3 = 2/d_2.
```

These are the same canonical primitive parabolics already obtained in PF-029.

## 2. Width-one cusp normalization

For a parabolic `Q(c,D)`, choose a determinant-one scaling matrix sending the fixed point `c` to infinity and conjugating the primitive stabilizer to unit translation. As in PF-019, for two normalized cusps `i,j`, the lower-left entry of the identity double-coset representative has absolute value

```text
C_ij = sqrt(D_i D_j) |c_i-c_j|.
```

Therefore the two adjacent finite cusp channels satisfy exactly

```text
C_12^2
 = D_1 D_2 d_1^2
 = 4(1 + d_1/d_2)
 = 4(1+r),

C_23^2
 = D_2 D_3 d_2^2
 = 4(1 + d_2/d_1)
 = 4(1+1/r).
```

Equivalently,

```text
C_12 = 2 sqrt(1+r),
C_23 = 2 sqrt(1+1/r).
```

Using the PF-029 closed-geodesic lengths,

```text
sinh(L_12/4)^2 = r,
sinh(L_23/4)^2 = 1/r,
```

this is also

```text
C_12 = 2 cosh(L_12/4),
C_23 = 2 cosh(L_23/4).
```

Thus the same multi-gap modulus occurs simultaneously in a closed-geodesic channel and in normalized cusp-to-cusp scattering geometry.

## 3. Guillemin's sojourn-time formula

For a finite-area hyperbolic surface with width-one cusps, truncate every standard cusp at the same height `a >> 1`. Guillemin associates to a cusp-to-cusp scattering geodesic represented by a matrix

```text
[[*,*],[c,*]]
```

in normalized cusp coordinates a sojourn time

```text
T = 2 log(a |c|).
```

This is explicit in Appendix B of:

- Victor Guillemin, *Sojourn times and asymptotic properties of the scattering matrix*, in the Lax-Phillips hyperbolic-surface setting. The calculation gives `T = 2 log(ca)` after the cusp stabilizers have been normalized to `z -> z+1`.

Guillemin's main formula expresses each scattering-matrix entry as a sum over scattering geodesics with oscillatory/exponential factors determined by these sojourn times. Ji-Zworski later generalized the relation between scattering-matrix oscillation frequencies and sojourn times to Q-rank-one locally symmetric spaces.

Useful literature anchors:

- V. Guillemin, *Sojourn times and asymptotic properties of the scattering matrix*; the online EMS text explicitly derives `T = 2 log(ca)`.
- L. Ji and M. Zworski, *Scattering matrices and scattering geodesics of locally symmetric spaces*, Ann. Sci. ENS 34 (2001), 441–469.

## 4. Exact prime-gap / scattering-frequency identity

Apply Guillemin's formula to the two direct identity-double-coset scattering geodesics between cusp pairs `(1,2)` and `(2,3)` of `Y_H`:

```text
T_12 = 2 log(a C_12),
T_23 = 2 log(a C_23).
```

The common truncation parameter cancels. Hence

```text
T_12 - T_23
 = 2 log(C_12/C_23)
 = log(d_1/d_2).
```

Therefore

```text
boxed:
T_12 - T_23 = log(d_1/d_2).
```

Equivalently,

```text
boxed:
d_1/d_2 = exp(T_12-T_23).
```

This is invariant under changing the common cusp cutoff `a`, even though each individual sojourn time shifts by the same additive constant.

For a recurrent bounded prime pattern `P+H`, the offsets are exact prime differences, so `d_1,d_2` are exact consecutive gaps inside that pattern. Thus the tangent surface carries the exact relative prime-gap datum as a **relative scattering time**.

## 5. Why this is genuinely scattering data

This is not an arbitrary transform of the gap sequence.

For finite-area cusped surfaces, Guillemin's scattering formula writes the `(i,j)` scattering entry as a sum indexed by cusp-to-cusp scattering geodesics, with the sojourn times as the corresponding oscillation frequencies. Ji-Zworski identify the same times in the singularity/frequency structure of Fourier-transformed scattering matrices.

Consequently the relation above can be read schematically as

```text
consecutive prime-gap ratio
      |
      v
four-punctured tangent modulus
      |
      v
relative sojourn time
      |
      v
frequency difference in standard scattering channels.
```

The surface and its scattering matrix already exist independently of the arithmetic interpretation; no prime Dirichlet series or hand-chosen spectral potential is introduced.

## 6. Relation to PF-019

PF-019 already proved for a four-endpoint configuration that the identity double-coset denominator after width-one normalization is

```text
C = 2 sqrt(1+chi) = 2 cosh(L/4).
```

PF-030 adds a new cancellation specific to the first nontrivial tangent surface. The two reciprocal cross-ratio channels have

```text
chi_12 = r,
chi_23 = 1/r,
```

so their **difference of Guillemin sojourn times** collapses exactly to `log r`.

Unlike the raw local cusp widths killed by PF-018, this survives independent width normalization. Unlike the universal `Re(s)=1/2` effects killed by PF-016 and the parabolic-transfer finding, it varies with the actual Teichmuller modulus.

## 7. Novelty check

The general ingredients are classical:

1. normalized cusp double cosets and their lower-left entries;
2. Guillemin's `T=2 log(a|c|)` formula;
3. scattering frequencies / sojourn times;
4. ideal-quadrilateral / four-punctured-sphere moduli.

There is also recent arithmetic work on scattering geodesics:

- Sudhir Pujahari and Punya Plaban Satpathy, *Prime scattering geodesic theorem*, arXiv:2505.04973 (2025), studies the **fixed modular surface** and relates counting of its scattering geodesics to integers whose prime divisors lie in arithmetic progressions.

That paper is important prior art and means no broad claim such as “first relation between primes and scattering geodesics” is justified.

A targeted search did not locate the present specialization:

```text
prime gaps
 -> prime-defined tight flute
 -> cusp-side ideal-quadrilateral tangent
 -> exact sojourn-time difference
 = log(consecutive-gap ratio).
```

The potentially novel content is this exact compositional identity in the prime-flute construction, not Guillemin's scattering theory or ideal-polygon geometry themselves.

## 8. What is and is not established

Established on `Y_H`:

```text
T_12 - T_23 = log(d_1/d_2)
```

for the two explicitly marked direct scattering geodesics, with common width-one cusp truncation.

Not yet established:

1. that the **full** conjugated prime-flute groups converge to `Gamma_H` as required by PF-029;
2. that these two direct sojourn times can always be recovered as the first/unique singularities of the raw unmarked scattering entries without using the geometric marking;
3. that the resulting tangent scattering data is implanted into any rigorously defined scattering operator of the full infinite-cusp flute.

The first item remains the main geometric gate. The second is a useful next audit: if the direct polygon-side scattering geodesic is the unique shortest geodesic in each adjacent cusp channel, then the ratio `d_1/d_2` would be recoverable directly from the first two marked scattering singularities, strengthening the result from a decomposition identity to an inverse-scattering statement.

## 9. Why this survives the current negative results

PF-030 uses exactly the sector that previous obstructions left alive:

```text
local single-cuff data             -> universal / telescoping;
local cusp width                   -> gauge;
global countable scattering det    -> noncompact obstruction;

multi-gap relative cusp geometry   -> survives normalization.
```

It therefore provides a concrete spectral observable to test before inventing any new determinant for the infinite flute.

## Lean candidates

The custom finite algebra is suitable for formalization:

1. derive `C_ij = sqrt(D_i D_j)|c_i-c_j|` for the chosen scaling matrices;
2. prove `C_12^2=4(1+d_1/d_2)` and `C_23^2=4(1+d_2/d_1)`;
3. prove the exact cancellation
   `2 log(C_12/C_23)=log(d_1/d_2)` for `d_1,d_2>0`.

Guillemin's identification of `2 log(a|c|)` with a scattering-geodesic sojourn time should remain an imported theorem layer.