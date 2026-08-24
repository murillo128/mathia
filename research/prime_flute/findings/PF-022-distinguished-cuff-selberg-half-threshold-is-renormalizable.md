# PF-022 — distinguished-cuff Selberg half-threshold is renormalizable and non-spectral

**Status:** NEGATIVE/OBSTRUCTION + EXACT-DERIVED, conditional only on the previously recorded square-summability input for the logarithmic mesh.

This note tests the most direct Selberg-type object built from the distinguished prime-flute cuffs themselves. The classical Selberg Euler factor is standard; the custom content is the exact specialization to the prime endpoint geometry and the resulting renormalization at `s=1/2`.

The conclusion is negative: the canonical cuff-only Euler subproduct does have an absolute-convergence threshold at `Re(s)=1/2`, but at the real boundary point its entire divergence is an explicitly removable endpoint-growth factor. After that geometric renormalization the product converges to a finite positive constant. Thus this occurrence of `1/2` cannot by itself encode Riemann-zero-type spectral information.

## 1. Exact cuff variable

Recall the exact prime-flute identities

```text
u_n = cot(pi/p_n)
h_n = log(u_n/u_{n-1}) > 0
q_n = exp(-ell_n/2) = tanh(h_n/4).
```

Also

```text
sum_{n=m}^N h_n = log(u_N/u_{m-1}).
```

The existing arithmetic audit records

```text
sum_n h_n^2 < infinity.
```

Hence `h_n -> 0`, and therefore

```text
q_n = h_n/4 + O(h_n^3).
```

Since the finite telescoping sum of the `h_n` tends to `+infinity`, while `sum h_n^3` converges, we obtain the useful ideal-class fingerprint

```text
sum_n q_n = infinity,
sum_n q_n^2 < infinity.
```

More generally, using `h_n = O(g_{n-1}/p_n)`, the Baker-Harman-Pintz bound `g_n << p_n^theta` with `theta<1`, and a dyadic estimate

```text
sum_{p_n in [x,2x]} g_n^alpha
    <= (max g_n)^(alpha-1) sum g_n
    << x^(theta(alpha-1)) x,
```

one gets

```text
sum_n q_n^alpha < infinity
```

for every fixed `alpha>1`.

Thus the sequence is in every `ell^alpha`, `alpha>1`, but not in `ell^1`.

## 2. The natural distinguished-cuff Selberg subproduct

For a primitive closed geodesic of length `ell`, the standard Selberg factor is

```text
prod_{k=0}^infinity (1 - exp(-(s+k) ell)).
```

Every distinguished pants cuff is a primitive closed geodesic. Therefore the marked prime-flute geometry canonically singles out the partial Euler product

```text
Z_cuff,m,N(s)
  = prod_{n=m}^N prod_{k=0}^infinity
      (1 - exp(-(s+k) ell_n))

  = prod_{n=m}^N prod_{k=0}^infinity
      (1 - q_n^(2(s+k))).
```

This is not asserted to be the Selberg zeta function of the full infinite surface. PF-006/PF-020 already show that the ordinary full Selberg product is obstructed by the separate family of primitive lengths accumulating at zero. `Z_cuff` is only the most natural candidate built directly from the distinguished cuff sequence.

Because `sum q_n^alpha < infinity` for every `alpha>1`, the double product converges absolutely for

```text
Re(s) > 1/2.
```

At the real point `s=1/2`, the `k=0` terms are `1-q_n` and `sum q_n=infinity`, while all `k>=1` terms are absolutely summable. Thus `1/2` is the exact real boundary for this direct Euler construction.

## 3. Exact renormalization at `s=1/2`

Set `x=h_n/4`. The elementary identity

```text
1 - tanh x = exp(-x) / cosh x
```

gives exactly

```text
1 - q_n
  = exp(-h_n/4) sech(h_n/4).
```

Multiplying from `m` to `N`,

```text
prod_{n=m}^N (1-q_n)
 = exp(-(1/4) sum_{n=m}^N h_n)
   prod_{n=m}^N sech(h_n/4)

 = (u_{m-1}/u_N)^(1/4)
   prod_{n=m}^N sech(h_n/4).
```

Since

```text
log sech x = -x^2/2 + O(x^4)
```

and `sum h_n^2<infinity`, the product

```text
prod_{n=m}^infinity sech(h_n/4)
```

converges to a strictly positive finite constant.

For the remaining Selberg factors at `s=1/2`,

```text
prod_{k=1}^infinity (1-q_n^(2k+1)),
```

absolute convergence follows from

```text
sum_n sum_{k>=1} q_n^(2k+1)
 = sum_n q_n^3/(1-q_n^2)
 < infinity.
```

Therefore there is a constant `C_m` with

```text
0 < C_m < infinity
```

such that

```text
u_N^(1/4) Z_cuff,m,N(1/2) -> C_m.
```

Equivalently, because `u_N ~ p_N/pi`,

```text
Z_cuff,m,N(1/2)
  ~ C'_m p_N^(-1/4)
```

with `0<C'_m<infinity`.

So the vanishing of the unrenormalized partial product at the half-threshold is exactly the coarse radial endpoint growth, plus a convergent positive local correction. There is no zero or sign/phase phenomenon left at the real boundary point after the natural geometric normalization.

## 4. What this rules out

The chain

```text
distinguished cuff lengths
    -> Selberg-type cuff Euler product
    -> threshold Re(s)=1/2
    -> Riemann critical-line mechanism
```

is not viable on the basis of the threshold itself.

The number `1/2` appears because

```text
q_n = exp(-ell_n/2)
```

sits at the `ell^1` / `ell^(1+epsilon)` boundary. At `s=1/2`, the first Selberg factor is exactly `1-q_n`; its divergent linear term is the telescoping logarithmic mesh `sum h_n`, and the non-telescoping remainder is absolutely summable.

Thus this is another instance of the PF-002 mechanism: a local scalar observable of one distinguished cuff loses the fine relational prime-gap information in its divergent part.

The finite positive renormalized constant still depends on the whole local cuff sequence, but treating that scalar as a new arithmetic invariant would merely repackage convergent prime-gap corrections. No independent Laplacian, resonance, scattering, or trace-formula mechanism selects it.

## 5. What is *not* ruled out

This note does **not** prove conditional convergence or analytic continuation of the cuff product on the vertical line

```text
s = 1/2 + it, t != 0.
```

At such points the leading term contains phases `q_n^(2it)`, and cancellation would depend on the distribution of the logarithmic gap variables. Without an independent spectral theorem selecting that continuation, studying those phases would amount to studying another Dirichlet series of prime-gap data, so it is not promoted as a candidate here.

Nor does this note affect the genuinely relational multi-gap sector from PF-004/PF-019, where cross-ratios survive cusp normalization and enter actual cross-cusp scattering coefficients.

## 6. Operator-ideal observation

The exact size statement

```text
(q_n) in ell^2 but not ell^1
```

means that the purely diagonal bookkeeping operator `Q=diag(q_n)` would be Hilbert-Schmidt but not trace class. Hence a genus-one / Carleman-Fredholm regularization is the minimal standard determinant regularization for that artificial diagonal model.

This is **not** yet a spectral operator attached to the Laplacian and should not be promoted to a natural determinant without an independent gluing/scattering construction whose singular values are genuinely comparable to the `q_n`.

## 7. Literature / novelty check

The Selberg factor

```text
prod_[primitive gamma] prod_{k>=0}
  (1-exp(-(s+k) ell_gamma))
```

is classical. Existing continuation results located in the search concern compact, cofinite, convex-cocompact, or more generally geometrically finite Fuchsian groups; for example Borthwick-Judge-Perry study geometrically finite surfaces, and Fedosova-Pohl treat geometrically finite groups with non-expanding cusp monodromy under transfer-operator hypotheses. These results do not supply a standard Selberg determinant for this infinitely generated prime-flute with primitive lengths accumulating at zero.

The tight-flute literature located in the project (Arredondo-Morales-Ramirez and related work) treats the zero-twist geometry, first-kind criterion, and parabolicity, not this distinguished-cuff Euler subproduct.

Targeted searches did not locate the exact prime-flute renormalization above. No general-theorem novelty is claimed: the useful result is the project-specific obstruction that the most direct cuff-based Selberg candidate produces a universal, explicitly removable half-threshold rather than a new spectral encoding of prime gaps.

## 8. Geometry preserved

Everything here uses the exact interior hyperbolic cuff lengths coming from the orthogonal-circle construction. The ambient inversion/interior-exterior duality remains exactly as recorded in PF-017 but plays no role in this product, because it is not an internal symmetry of the prime-flute Laplacian.
