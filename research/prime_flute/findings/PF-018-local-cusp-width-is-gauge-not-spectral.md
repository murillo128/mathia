# PF-018 — local cusp width is gauge, not a prime-specific spectral modulus

**Status:** `NEGATIVE/OBSTRUCTION` + `EXACT-DERIVED` + standard cusp-normalization literature.

## Claim

For three consecutive real endpoint coordinates

```text
a < b < c
```

with the prime-flute generator convention

```text
G(x,y) = 1/(y-x) * [[x+y, -2xy], [-2, x+y]],
```

the adjacent product

```text
P(a,b,c) = G(a,b) G(b,c)^(-1)
```

is parabolic:

```text
det P = 1,
tr P  = -2.
```

Writing

```text
X = b-a,
Y = c-b,
```

a direct simplification gives

```text
P = [[ 2b(1/X+1/Y)-1,  2b^2(1/X+1/Y)],
     [   -2(1/X+1/Y), -2b(1/X+1/Y)-1]].
```

Its double fixed point is `-b` in this matrix convention.  Conjugate it to infinity with

```text
C_b(z) = -1/(z+b),
```

represented by `[[0,-1],[1,b]]`. Then exactly

```text
C_b P C_b^(-1)
  = [[-1, 2(1/X+1/Y)],
     [ 0,             -1]]
```

and therefore, projectively,

```text
z -> z - W,

W(a,b,c) = 2(1/(b-a) + 1/(c-b)).
```

The sign of the translation depends on orientation conventions; the positive magnitude `W` is the relevant coefficient.

For the exact prime vertices

```text
u_n = cot(pi/p_n),
Delta_n = u_{n+1}-u_n,
```

this becomes

```text
W_n = 2(1/Delta_{n-1} + 1/Delta_n)
```

and hence, using `Delta_n ~ g_n/pi`,

```text
W_n ~ 2 pi (1/g_{n-1} + 1/g_n).
```

At first sight this looks like a local cusp parameter carrying two consecutive prime gaps.

## Obstruction

It is not an intrinsic modulus of the hyperbolic cusp.

For a Fuchsian cusp, a standard scaling matrix `sigma_c` is chosen so that the primitive parabolic stabilizer is conjugated to the **unit translation**

```text
sigma_c^(-1) gamma_c sigma_c = [[1,1],[0,1]].
```

Equivalently, after sending the parabolic fixed point to infinity, an additional diagonal hyperbolic dilation rescales every nonzero translation length `W` to `1`.

Thus every complete rank-one cusp tail, after the usual normalization, is isometric to the standard cusp

```text
<z -> z+1> \ {0 <= x <= 1, y >= Y}.
```

The apparent `W_n` above is therefore a coordinate-dependent feature of the chosen ideal-polygon embedding, not a local spectral invariant of the quotient cusp.

## Spectral consequence

This rules out a tempting branch:

```text
adjacent prime gaps
    -> raw parabolic translation coefficient W_n
    -> one-cusp Eisenstein/scattering/transfer datum
    -> prime-specific spectral signal.
```

The local cusp tail does not retain `W_n` after canonical normalization. In particular, the `Re(s)=1/2` threshold obtained by accelerating powers of a single parabolic remains the universal rank-one cusp threshold already recorded in the parabolic-transfer finding.

This does **not** imply that a diagonal entry of a global scattering matrix is independent of prime geometry. Such an entry can depend on the entire surface through return paths. The point is narrower and stronger: any such dependence must be **global/relational**; it cannot come from a local cusp-width modulus, because no such intrinsic modulus exists.

Prime-specific information can therefore survive only in data invariant under the independent cusp normalizations, for example cross-cusp/double-coset geometry, nonlocal cross-ratios, or words involving more than one cusp.

## Relation to earlier findings

- strengthens the earlier negative result that the accelerated parabolic `1/2` threshold is universal;
- is compatible with PF-003: adjacent-gap information is present in the marked fan/shear process, but not as an isolated cusp modulus;
- reinforces PF-004: Möbius-invariant multi-endpoint cross-ratios remain the natural place where relational prime information survives normalization;
- does not use the exterior arc as a second hyperbolic channel; PF-017 remains in force.

## Literature / novelty status

The normalization of a primitive parabolic to `z -> z+1` and the resulting standard cusp model are classical. The exact formula

```text
W_n = 2(1/Delta_{n-1}+1/Delta_n)
```

is an elementary calculation specialized to the prime-flute generators. A targeted search did not locate this prime-gap specialization, but the mathematical value here is primarily the **negative structural conclusion**, not a novelty claim about cusp theory.

Useful standard references located during the audit include treatments of scaling matrices for Eisenstein series that require

```text
sigma_c^(-1) gamma_c sigma_c = [[1,1],[0,1]],
```

and descriptions of all normalized cusp tails as isometric copies of the same standard cusp. See the research-session source trail associated with this finding before promoting it beyond exploratory status.

## Lean candidate

High-value finite formalization:

1. prove `det P = 1` and `tr P = -2`;
2. prove the double fixed point at `-b` for this convention;
3. prove the conjugation formula and exact `W(a,b,c)`;
4. keep the statement that all `W != 0` translations are conjugate separate from analytic scattering theory.
