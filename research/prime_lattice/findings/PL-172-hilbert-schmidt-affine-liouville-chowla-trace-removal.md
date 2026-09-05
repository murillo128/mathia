# PL-172 — Hilbert--Schmidt regularization of the affine Liouville correlation crosses `Re(s)=1/2` only by deleting the unsolved Chowla trace

## Claim

`PL-169`--`PL-171` isolate ordinary addition as the first genuinely rational-integer structure that is absent from the free prime-exponent monoid. There is a canonical way to combine that additive shift with a native exponent-lattice observable that does **not** telescope: the Liouville parity character.

On `ell^2(N_{>=1})`, let

```text
H e_n = (log n)e_n,
S_h e_n = e_(n+h),
J e_n = lambda(n)e_n,
```

where `h>=1` is fixed and `lambda(n)=(-1)^Omega(n)`. The operator `J` is the parity character of the full prime-exponent lattice, since

```text
J mu_p = - mu_p J
```

for every prime shift `mu_p e_n=e_(pn)`. Define

```text
K_h := J S_h^* J S_h.
```

Then

```text
K_h e_n = lambda(n)lambda(n+h)e_n.
```

Thus `K_h` is a self-adjoint unitary whose diagonal is exactly the fixed-shift two-point Liouville correlation. Set

```text
T_h(s) := exp(-sH) K_h.
```

For `sigma=Re(s)`, its singular values are `n^(-sigma)`, so

```text
T_h(s) in S_1  iff sigma>1,
T_h(s) in S_2  iff sigma>1/2.
```

In the trace-class half-plane,

```text
C_h(s)
 := Tr T_h(s)
 = sum_(n>=1) lambda(n)lambda(n+h)n^(-s),
qquad Re(s)>1,
```

which is the Dirichlet series attached to the fixed-shift two-point Chowla correlation.

The standard Hilbert--Schmidt determinant therefore exists one full half-plane farther left:

```text
D_h(z,s) := det_2(I-zT_h(s)),
qquad Re(s)>1/2.
```

But the apparent gain is exactly the regularization counterterm, not a continuation of `C_h(s)`. In the safe Taylor disk `|z|<1`,

```text
log D_h(z,s)
 = - sum_(r>=2) z^r/r * Tr(T_h(s)^r).
```

Since `lambda(n)lambda(n+h)` is a sign,

```text
Tr(T_h(s)^(2m))
 = zeta(2m s),

Tr(T_h(s)^(2m+1))
 = C_h((2m+1)s)
```

whenever these traces are taken in their ordinary trace-class domains. Consequently, throughout `Re(s)>1/2`, every coefficient retained by `det_2` is already absolutely convergent:

```text
even r>=2:  Re(r s)>1,
odd  r>=3:  Re(r s)>3/2>1.
```

The only first-scale shifted-correlation term,

```text
C_h(s)=Tr T_h(s),
```

is precisely the `r=1` term removed by `det_2`.

Therefore the canonical Hilbert--Schmidt regularization of this mixed multiplicative-additive Liouville operator **does cross the ordinary trace wall down to `Re(s)>1/2`, but it does so by deleting the unsolved fixed-shift Chowla channel at the original spectral scale**. The surviving determinant does not provide analytic continuation of `C_h(s)` and does not turn the Hilbert--Schmidt boundary into an RH-localizing mechanism.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION`, decisive for the scoped route

```text
prime-exponent parity
+ canonical integer shift
+ logarithmic Hamiltonian
+ standard det_2 regularization
    -> continuation to the critical half-plane carrying the original
       fixed-shift Liouville/Chowla trace.
```

No novelty is claimed for Liouville correlations, Chowla's conjecture, Schatten ideals, or regularized Fredholm determinants. The line-specific result is the exact operator audit showing that the most immediate `S_2` repair of the first non-telescoping affine arithmetic channel removes the hard first-order trace and retains only rescaled correlations already back inside absolute convergence.

## 1. The affine Liouville operator is a genuine mixed lattice observable

The shift calculation is exact:

```text
S_h e_n = e_(n+h),
J S_h e_n = lambda(n+h)e_(n+h),
S_h^* J S_h e_n = lambda(n+h)e_n,
J S_h^* J S_h e_n = lambda(n)lambda(n+h)e_n.
```

Thus

```text
K_h = diag_n a_n,
qquad a_n=lambda(n)lambda(n+h) in {+1,-1}.
```

Unlike the relative heat trace of `PL-170`, this construction does not compare a tail with its translate and therefore does not telescope to a finite head. The coefficient `a_n` simultaneously depends on multiplicative factorization and on the additive relation `n -> n+h`; it is exactly the kind of mixed arithmetic datum that survived the free-monoid and affine-semiring audits.

The ordinary heat trace is

```text
Tr(exp(-sH)K_h)
 = sum_n a_n n^(-s)
```

for `Re(s)>1`. Writing

```text
A_h(x)=sum_(n<=x) a_n,
```

partial summation shows why extending this scalar series leftward is an arithmetic problem rather than an operator-ideal formality: quantitative cancellation in `A_h(x)` directly controls its half-plane of convergence. The original fixed-shift two-point Chowla conjecture asks only for `A_h(x)=o(x)`, while a square-root-quality estimate `A_h(x)=O_epsilon(x^(1/2+epsilon))` would be vastly stronger and would place the Dirichlet series near the RH scale.

Tao proved the logarithmically averaged two-point Chowla conjecture, not the ordinary fixed-shift Cesaro statement. A very recent quantitative logarithmic result of Guo, submitted 24 August 2026, explicitly states that it still does **not** prove the ordinary Cesaro two-point Chowla conjecture. Thus the first-order trace removed below is not a channel whose needed ordinary cancellation has already been supplied by current theorem-level literature.

## 2. The `1/2` threshold is exact but sign-blind

Because `K_h` is unitary and commutes with `H`,

```text
|T_h(s)| = exp(-sigma H).
```

Hence for every `q>=1`,

```text
||T_h(s)||_(S_q)^q
 = sum_(n>=1) n^(-q sigma)
 = zeta(q sigma)
```

in its convergence domain. In particular,

```text
T_h(s) in S_q iff q sigma>1.
```

This is independent of `h` and independent of every correlation sign `a_n`. The critical value `sigma=1/2` is therefore the universal `ell^2` boundary of the logarithmic integer spectrum, exactly as in earlier Schatten findings, not evidence of square-root cancellation in `A_h(x)`.

A matched control makes the point explicit. Replacing `a_n` by **any** unimodular diagonal sequence leaves every singular value and every Schatten threshold unchanged. Whatever arithmetic information the Liouville shift supplies can only survive through sign-sensitive traces/products, not through membership in `S_2` itself.

## 3. `det_2` removes exactly the first-scale correlation

For a Hilbert--Schmidt operator `T`, the standard second regularized determinant is

```text
det_2(I-zT)
 = det((I-zT)exp(zT)).
```

It is entire in the coupling `z`. For `|z|` sufficiently small, its logarithm has the standard expansion

```text
log det_2(I-zT)
 = -sum_(r>=2) z^r/r * Tr(T^r).
```

The missing `r=1` coefficient is the defining counterterm of the regularization.

For the present diagonal operator,

```text
T_h(s)^r e_n
 = a_n^r n^(-rs)e_n.
```

When `Re(s)>1/2`, every `r>=2` power is trace class. Since `a_n^2=1`,

```text
Tr(T_h(s)^(2m))
 = sum_n n^(-2ms)
 = zeta(2ms),
```

while for odd `r=2m+1>=3`,

```text
Tr(T_h(s)^r)
 = sum_n a_n n^(-rs)
 = C_h(rs).
```

The key domain separation is exact. If `Re(s)>1/2`, then every even argument `2ms` lies in `Re>1`, and every retained odd argument `(2m+1)s` lies in `Re>3/2`. Thus **none of the Taylor coefficients of the regularized determinant requires continuing the shifted-correlation series through its original `Re(s)=1` boundary**.

Equivalently, in the diagonal product representation,

```text
D_h(z,s)
 = product_(n>=1)
   [(1-z a_n n^(-s)) exp(z a_n n^(-s))].
```

The factor `exp(z a_n n^(-s))` is exactly what cancels the linear trace-log term. Any zero of this determinant as a function of the coupling is consequently just a zero of one of the elementary diagonal factors, not a newly derived Riemann-zero divisor.

## 4. Holomorphy in `s` does not continue the deleted trace

On every compact subset of `Re(s)>1/2`, the map

```text
s -> T_h(s)
```

is holomorphic with values in `S_2`: derivatives introduce powers of `log n`, and

```text
sum_n (log n)^(2k) n^(-2 sigma_0)<infinity
```

for every fixed `sigma_0>1/2`. Standard analytic dependence of `det_2` therefore makes `D_h(z,s)` holomorphic in `s` throughout that half-plane for each fixed `z`.

That holomorphy must not be misread as analytic continuation of

```text
C_h(s)=Tr T_h(s).
```

The determinant was defined precisely in a class where `Tr T_h(s)` need not exist, and its Taylor expansion starts at quadratic order. Reconstructing the deleted linear term would require additional information not contained in the standard `det_2` normalization. Supplying an independently continued `C_h(s)` as a counterterm would put the hard arithmetic channel back by hand.

This is the affine analogue of `PL-009`, but with an important difference in interpretation. `PL-009` showed that prime-mode `det_2` removes the first prime-zeta term carrying zeta-divisor information. Here the deleted term is not a one-particle Euler logarithm: it is the **first genuinely mixed multiplicative-additive Liouville correlation** singled out by the recent affine findings. The same regularization obstruction therefore persists after adding nontrivial rational-integer arithmetic structure.

## 5. Adversarial audit and scope

The conclusion is intentionally narrow.

First, it does not claim that fixed-shift Chowla itself is equivalent to RH, nor that square-root cancellation for `A_h(x)` follows from RH. The correlation is used because it is the canonical non-telescoping observable produced by combining prime-exponent parity with ordinary addition.

Second, the logarithmic expansion is invoked only in a safe neighborhood of `z=0` (for example `|z|<1` here). The determinant is entire in `z`, but there can be elementary coupling zeros outside that disk. In particular the `n=1` factor can make `z=1` a trivial zero when `lambda(h+1)=1`; no claim is made by evaluating the determinant at that coupling.

Third, the argument does not rule out a **different non-diagonal operator** in which additive and multiplicative data survive in higher cyclic traces, a relative/scattering determinant with independently justified comparison data, or an archimedean/adelic construction that supplies a functional equation and positivity. It rules out the standard diagonal Hilbert--Schmidt regularization of this canonical affine correlation operator as a way to carry the original fixed-shift trace through `Re(s)=1`.

Fourth, `det_2` does retain shifted-correlation information at the rescaled arguments `3s,5s,...`. The negative claim is not that this information is identically absent; it is that throughout `Re(s)>1/2` those arguments are already in the absolutely convergent region and therefore do not constitute continuation of the original channel at `s`.

Finally, the finding is robust under replacing Liouville by any sign sequence: `det_2` always deletes the first trace. What is special to Liouville is the clean even/odd power split, where even powers collapse exactly to zeta and odd powers sample the same affine correlation at higher spectral arguments.

## 6. Prior art and current-status audit

- Terence Tao, “The logarithmically averaged Chowla and Elliott conjectures for two-point correlations,” *Forum of Mathematics, Pi* **4** (2016), e8, DOI https://doi.org/10.1017/fmp.2016.6, arXiv: https://arxiv.org/abs/1509.05422. This proves the logarithmically averaged two-point theorem while stating the ordinary fixed-shift Cesaro correlation as the Chowla conjecture.
- Jizhou Guo, “Quantitative Logarithmic Chowla Correlations Uniformly over Growing Shifts,” arXiv:2608.23500 (submitted 24 August 2026), https://arxiv.org/abs/2608.23500. The abstract explicitly distinguishes its logarithmically weighted estimate from the still-unproved ordinary Cesaro two-point statement.
- Thomas Britz, Alan Carey, Fritz Gesztesy, Roger Nichols, Fedor Sukochev, Dmitriy Zanin, “The product formula for regularized Fredholm determinants,” *Proceedings of the American Mathematical Society, Series B* **8** (2021), 42--51, DOI https://doi.org/10.1090/bproc/70, arXiv: https://arxiv.org/abs/2007.12834. Standard anchor for `det_2` and Schatten regularized determinant identities; already recorded in `research/prime_lattice/SOURCES.md` for `PL-009`.

The novelty search found the component ingredients separately but no source identifying this exact affine-Liouville operator/determinant combination. That absence is **not** used as a novelty claim. The construction is classified as exact derived negative evidence: its value is to close a natural route created by `PL-169`--`PL-171`, not to claim a new theorem about Chowla correlations or Fredholm determinants.

## 7. Consequence for the research line

The recent affine branch now has a sharper separation.

`PL-170` showed that an additive finite difference gains trace-class decay but destroys the arithmetic tail by telescoping. `PL-171` showed that congruence/Dirichlet twists retain an infinite arithmetic tail but do not improve the ordinary trace-class threshold. The present calculation shows that even when the additive shift is coupled to the multiplicative Liouville parity so that a genuinely hard non-telescoping correlation survives, the canonical move from `S_1` to `S_2` still does not solve the problem: **standard regularization crosses the half-plane by subtracting the hard trace itself**.

A surviving mixed additive-multiplicative route must therefore do more than manufacture an `S_2` operator at the critical boundary. It must retain the first-order shifted arithmetic data in a canonically defined quantity -- or move that data into higher nontrivial cycles -- without importing an analytic continuation as an external counterterm. That is the meaningful target left by this obstruction.