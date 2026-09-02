# PL-109 — Prime-axis Lindelöf control already characterizes RH, but the criterion is thin-set and Beurling portable

## Claim

There is already a classical RH-equivalent harmonic criterion that uses only the **prime coordinate axes** of the exponent lattice, and in its most direct form only the basis points themselves.

Along the canonical prime Kronecker orbit

```text
z_p(t)=p^(-it)=exp(-it log p),
```

define the prime-axis polynomial

```text
Q_x(z)=sum_(p<=x) z_p.
```

Then

```text
Q_x(z(t))=sum_(p<=x) p^(-it).
```

Gonek, Graham, and Lee prove that the generalized Lindelöf hypothesis for the prime sequence is equivalent to RH. In the form used in their proof, for every `epsilon>0` and every fixed `B>0`, uniformly for

```text
2<=x<=|t|^B,
```

the required estimate is

```text
sum_(p<=x) p^(-it)
 = integral_2^x u^(-it)/log(u) du
   + O_(epsilon,B)(x^(1/2)|t|^epsilon),
```

with harmless logarithmic factors absorbed into `|t|^epsilon` in this polynomial range. Thus an RH-equivalent vertical-flow criterion already exists on the set

```text
{e_p : p prime}
```

without using any mixed-support exponent vector.

By partial summation Gonek--Graham--Lee pass to the equivalent von Mangoldt form

```text
sum_(n<=x) Lambda(n)n^(-it)
 = x^(1-it)/(1-it)
   + O_(epsilon,B)(x^(1/2)|t|^epsilon).
```

In exponent coordinates this has support only on

```text
v(n)=k e_p,
```

because `Lambda(n)` vanishes away from prime powers. Hence even the analytic proof uses only the union of one-dimensional prime-power rays, not the higher-dimensional lattice.

This is a **decisive prior-art redirect** for the route

```text
mixed-prime exponent geometry
  -> vertical log-prime Fourier cancellation
  -> RH equivalence.
```

Obtaining an RH-equivalent cancellation statement along the distinguished flow does not by itself demonstrate that mixed-support lattice geometry contributes anything. Moreover, Banks showed that suitably chosen arbitrarily small relative-density subsets of the ordinary primes can retain an RH-equivalent Lindelöf criterion, and Broucke--Weishäupl extended the prime-sequence equivalence to Beurling generalized prime systems satisfying a sharp square-root regularity hypothesis on their generalized-integer counting function. The **criterion schema is therefore portable** and is not, by itself, a rigid signature of the exact rational-prime exponent lattice.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/DECISIVE-REDIRECT` for the claim that axis-only vertical-flow cancellation already suffices for an RH-equivalent criterion and that this schema survives thin-prime and Beurling controls. The conclusion is deliberately restricted: it does **not** say mixed-prime geometry can never matter to a stronger mechanism, nor that arbitrary generalized-prime systems reproduce ordinary zeta.

## 1. Exact prime-axis formulation in Bohr coordinates

The exponent vector of a prime is the basis vector

```text
v(p)=e_p.
```

The Bohr character attached to the canonical vertical flow is

```text
chi_t(alpha)
 = exp(-it <alpha,(log p)_p>).
```

Therefore

```text
chi_t(e_p)=exp(-it log p)=p^(-it),
```

and

```text
sum_(p<=x) p^(-it)
 = sum_(p<=x) chi_t(e_p).
```

No multiplication of distinct prime directions occurs in this observable. It is the Fourier transform of the counting measure on the truncated set of coordinate basis points,

```text
nu_x=sum_(p<=x) delta_(e_p),
```

evaluated at the one-parameter character `chi_t`.

Gonek--Graham--Lee define a generalized Lindelöf property for admissible sequences and prove, as their Theorem 1,

```text
LH(P) <=> RH,
```

where `P` is the sequence of ordinary primes. In the prime case, the estimate used in the proof is

```text
sum_(p<=x) p^(-it)
 = integral_2^x u^(-it)/log(u) du
   + O_(epsilon,B)(x^(1/2)|t|^epsilon)
```

for every `epsilon,B>0` and `2<=x<=|t|^B`.

Thus the prime-coordinate Fourier data alone can carry an RH-equivalent uniform cancellation statement.

## 2. The proof compresses further to the prime-power axis skeleton

Gonek--Graham--Lee explicitly replace the prime sum by

```text
psi(x,t)=sum_(n<=x) Lambda(n)n^(-it)
```

and show that the required prime estimate is equivalent, at the precision relevant to their theorem, to

```text
psi(x,t)
 = x^(1-it)/(1-it)
   + O_(epsilon,B)(x^(1/2)|t|^epsilon).
```

Since

```text
Lambda(n)=log p  if n=p^k,
Lambda(n)=0      otherwise,
```

this becomes exactly

```text
sum_p sum_(k>=1, p^k<=x)
    (log p) exp(-it k log p).
```

In exponent coordinates its support is

```text
{ k e_p : p prime, k>=1 }.
```

This is the same axis-ray compression emphasized for the completed Weil channel in `PL-013`, but here it appears in a different theorem: a **uniform exponential-sum criterion equivalent to RH**.

The distinction from `PL-086` is also important. `PL-086` shows that, after prime support has already been selected in a fixed macroscopic band, inserting the half-weighted factor `Lambda(p)p^(-1/2)` does not change the asymptotic finite-time Gram bulk beyond deterministic grading. The present result is not a Gram-law statement. It concerns a strong, pointwise-in-`t`, multi-scale cancellation estimate with enough uniformity to control analytic continuation and hypothetical zeros.

## 3. Analytic continuation enters legitimately, not by extending the Euler product termwise

The axis identity itself is finite and needs no continuation. The RH implication and converse use analytic information about zeta through its logarithmic derivative.

For `Re(s)>1`,

```text
-zeta'(s)/zeta(s)
 = sum_(n>=1) Lambda(n)n^(-s).
```

Gonek--Graham--Lee use Perron inversion and contour shifting for `-zeta'/zeta` to derive the axis-ray estimate under RH. In the converse direction they start from the uniform remainder

```text
R(x,t)
 = sum_(n<=x) Lambda(n)n^(-it)
   - x^(1-it)/(1-it)
 = O(x^(1/2)|t|^epsilon)
```

and construct a Mellin integral whose meromorphic expression contains `zeta'/zeta`. A hypothetical zero

```text
rho_0=beta_0+i gamma_0,
beta_0>1/2,
```

then produces a residue incompatible with the assumed square-root bound after a suitable choice of the polynomial range parameter `B`.

So the result genuinely crosses the absolute-convergence boundary, but the bridge is the classical meromorphic continuation of `zeta'/zeta` plus contour analysis. It is **not** obtained by declaring the prime-axis Euler series convergent in the critical strip.

## 4. Why the critical exponent does not emerge from prime-lattice geometry here

The theorem is highly relevant to the research line because it is a real RH equivalence written directly in the log-prime flow. But it does not explain why the critical line should be `Re(s)=1/2`.

The square-root exponent is already the demanded strength of the generalized Lindelöf estimate. In the converse proof, that exponent is exactly what rules out a zero with `beta_0>1/2`: a contribution growing like a power determined by `beta_0` eventually exceeds the assumed `x^(1/2)` scale.

Schematically,

```text
assume square-root axis cancellation
        |
        v
Mellin transform / -zeta'/zeta
        |
        v
no zero with beta>1/2
        |
functional-equation symmetry
        v
RH.
```

This is a powerful analytic equivalence, not a geometric derivation of the half-axis from the torus. The value `1/2` is present in the cancellation hypothesis whose equivalence is being proved.

This distinction matters for `prime_lattice`: a new proposal does not become an explanatory RH mechanism merely because an estimate for a Bohr/Kronecker observable is equivalent to RH.

## 5. Thin ordinary-prime sets show that even the full set of basis directions is not necessary

Banks sharpened the Gonek--Graham--Lee phenomenon. For arbitrarily small fixed relative densities, he constructs subsets

```text
P_epsilon subset P
```

for which an appropriately normalized generalized Lindelöf hypothesis remains equivalent to ordinary RH. He also constructs still thinner prime subsets whose Lindelöf behavior detects zero-free half-planes, with a strengthened variant again equivalent to RH.

In exponent-lattice language, the RH-sensitive observable may therefore be supported on a sparse subset

```text
{e_p : p in P_epsilon}
```

of the coordinate axes.

This does **not** mean that every thin set of primes detects RH, and Banks's sets are not being promoted to a canonical geometric object. The falsification point is narrower: neither mixed-support lattice points nor even all prime basis vectors are logically necessary for this style of RH-equivalent vertical Fourier criterion.

## 6. Beurling generalized primes make the criterion schema portable

Broucke and Weishäupl extend the Gonek--Graham--Lee theorem to Beurling generalized number systems. If `(P,N)` is a Beurling prime/integer system whose generalized-integer counting function satisfies

```text
N_P(x)=A x+O(x^(1/2))
```

for some `A>0`, they prove

```text
LH(P,Li(x))
  <=>
psi_P(x)=x+O_epsilon(x^(1/2+epsilon))
     for every epsilon>0,
```

where the right-hand statement is their Riemann hypothesis for that Beurling system.

Their logarithmic derivative has the same formal axis-ray structure,

```text
-zeta_P'(s)/zeta_P(s)
 = integral_1^infinity x^(-s) d psi_P(x),
```

with generalized prime powers supplying the von Mangoldt support. Thus the architecture

```text
generated prime frequencies
  -> prime-axis exponential sums
  -> square-root Lindelöf control
  -> zero-free critical half-plane for the associated zeta
```

survives outside the rational-prime system, under a strong and sharp regularity assumption on generalized integers.

The boundary is essential: Broucke--Weishäupl also show that the exponent `1/2` in the hypothesis `N_P(x)=Ax+O(x^(1/2))` is sharp for their theorem. This is therefore **not** a statement that arbitrary Beurling deformations satisfy the same equivalence. It is a matched-control result showing that the criterion form itself is not uniquely tied to the detailed mixed-coordinate geometry of ordinary integer factorization.

## 7. Relationship to the new full-energy-ball inverse theorem `PL-108`

`PL-108` records the 2026 theorem of Dong--Wang--Wang--Zhang:

```text
large |sum_(n<=x)n^(it)|
  -> many ordinary zeta zeros near Re(s)=1.
```

That observable uses every exponent vector in the energy ball

```text
{alpha:E(alpha)<=log x},
```

but both cutoff and phase factor through the scalar energy `E(alpha)=log n`.

The present prior art gives a useful counterpoint:

```text
all lattice points in an energy ball
  -> quantitative inverse zero-forcing near Re(s)=1
```

whereas

```text
prime basis points only
  + a much stronger uniform square-root cancellation hypothesis
  <=> RH.
```

Therefore the number of exponent-lattice directions involved is not what determines RH sensitivity. What matters is the **strength and analytic use of the cancellation estimate**. A full-lattice Fourier observable can be a weaker zero detector, while an axis-only observable can encode an RH equivalence.

This prevents a false inference from `PL-108`: the fact that its finite polynomial sums over the full energy ball is not evidence that mixed-prime combinatorics is the source of its zeta sensitivity.

## Prior art and novelty assessment

The primary theorem-level anchors are:

- **Steven M. Gonek, Sidney W. Graham, Yoonbok Lee**, “The Lindelöf hypothesis for primes is equivalent to the Riemann hypothesis,” *Proceedings of the American Mathematical Society* **148** (2020), 2863–2875. DOI: `10.1090/proc/14974`. Their Theorem 1 is the RH equivalence; the proof explicitly uses the equivalent von Mangoldt sum supported on prime powers.
- **William D. Banks**, “The Riemann and Lindelöf hypotheses are determined by thin sets of primes,” *Proceedings of the American Mathematical Society* **150** (2022), 4213–4222. DOI: `10.1090/proc/15959`. This supplies the thin-axis control.
- **Frederik Broucke, Sebastian Weishäupl**, “On the Lindelöf hypothesis for general sequences,” *Mathematika* **70**(2) (2024), Article e12240. DOI: `10.1112/mtk.12240`. Their Theorem 1.3 supplies the Beurling generalized-prime extension under `N_P(x)=Ax+O(x^(1/2))`.

No novelty is claimed for these theorems, for the prime-axis Bohr rewrite, or for the observation that von Mangoldt support is the union of prime-power rays. The durable result is the **combined falsification consequence for this research line**: RH-equivalent harmonic control can live entirely on a one-coordinate skeleton and the theorem schema persists under substantial thinning and generalized-prime deformation.

This consequence is close to, but not duplicated by, `PL-013`, `PL-015`, `PL-086`, or `PL-108`: `PL-013` identifies axis support in the completed Weil channel; `PL-015` tests broad Beurling flexibility; `PL-086` analyzes prime-only Gram weighting; and `PL-108` records a full-energy-ball inverse zero-forcing theorem. The present finding specifically audits the **logical necessity of mixed-support lattice geometry for RH-sensitive vertical-flow cancellation**.

## Adversarial boundaries

### Axis-only equivalence does not prove mixed-prime geometry is useless

Correct. It proves only that mixed-support vectors are not logically required for this class of cancellation criterion. A different mechanism could still use coordinate interactions to derive the needed square-root estimate, a positivity theorem, or a self-duality statement that axis data alone does not explain.

### The criterion may hide ordinary-prime arithmetic in the choice of axes

Correct. The basis vectors are indexed by the ordinary rational primes, and their frequencies are the exact `log p`. The result does not reduce RH to an arbitrary free collection of frequencies. The Beurling comparison weakens, but does not erase, this caveat because its theorem assumes a strong generalized-integer counting law.

### The thin-prime result is not universality for arbitrary sparse subsets

Correct. Banks constructs special subsets with the required property. The result is used only to falsify necessity of the *entire* prime-axis set, not to claim that thinning preserves RH information generically.

### The Beurling extension concerns each system's own zeta function

Correct. It does not preserve the ordinary Riemann zero set under deformation. Its role is a matched control: the same axis-sum-to-RH architecture is available in a wider multiplicative category, so that architecture alone cannot certify a uniquely rational-prime geometric mechanism.

### The half exponent is not derived here

Correct. The theorem states an equivalence between RH and a square-root-strength cancellation property. It does not derive square-root cancellation from exponent-lattice geometry. Any future claim that this provides a natural geometric explanation of `1/2` would be circular unless an independent structure forces that scale.

## Audit / falsification criterion

This finding can be checked through four independent statements:

1. verify Gonek--Graham--Lee Theorem 1 and their displayed prime sum estimate for `2<=x<=|t|^B`;
2. verify their partial-summation reduction to `sum Lambda(n)n^(-it)` and hence support only at `v(n)=k e_p`;
3. verify Banks's existence of arbitrarily small relative-density prime subsets retaining an RH-equivalent generalized Lindelöf criterion;
4. verify Broucke--Weishäupl Theorem 1.3, including the hypothesis `N_P(x)=Ax+O(x^(1/2))` and their Beurling-system RH conclusion.

The finding is falsified or must be narrowed if any of those theorem-level claims fails. It should also be narrowed if a later argument shows that the Gonek--Graham--Lee equivalence secretly uses mixed-prime data beyond the axis-ray logarithmic derivative in a way essential to the proof rather than merely through standard analytic properties of zeta.

## Consequence for the research line

The line should no longer regard

```text
an RH-equivalent estimate along the log-prime Kronecker flow
```

as evidence, by itself, that the higher-dimensional exponent lattice supplies the missing RH mechanism. There is a classical counterexample to that inference: the prime-coordinate observable already has such an equivalence, and the analytic proof compresses to prime-power rays.

A genuinely new mixed-lattice proposal must therefore identify an additional invariant that **cannot be reduced to axis-ray sums or to `-zeta'/zeta`**, and it must survive the line's thin-set and Beurling controls. The relevant question is no longer whether the log-prime flow can encode RH—it certainly can—but whether interactions among several exponent coordinates force a property, such as positivity, self-duality, or zero localization, that the already-complete axis-only harmonic criteria do not provide.