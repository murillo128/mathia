# PL-110 — Fixed exponent-depth totients scalarize to a zeta ratio, and the proposed unsmoothed RH criterion is defective

## Claim

A July 2026 preprint of Ahmed Gaber studies the multiplicative function

```text
phi_l(n)
 = n product_(p: v_p(n)>=l) (1-1/p),
```

for fixed integer `l>=1`. In prime-exponent coordinates this is an unusually direct **full-lattice fixed-depth observable**:

```text
phi_l(v)
 = exp(<v,(log p)_p>)
   product_(p: v_p>=l) (1-1/p).
```

It therefore provides a useful prior-art/control case for the `prime_lattice` mandate: the observable genuinely inspects every coordinate threshold `v_p>=l`, rather than restricting to prime-power axes as in `PL-087`--`PL-090`.

Nevertheless its Dirichlet transform scalarizes completely. For `Re(s)>2`, where the Euler product is absolutely convergent,

```text
F_l(s)
 := sum_(n>=1) phi_l(n)n^(-s)
  = zeta(s-1)/zeta(l(s-1)+1).
```

The quotient then supplies the meromorphic continuation. A nontrivial zeta zero `rho` is transported affinely to

```text
s_rho = 1 + (rho-1)/l,
```

so the Riemann critical line is transported to

```text
Re(s)=1-1/(2l).
```

This is a reparameterization of the zeta divisor, not a geometric mechanism that independently selects `1/2`.

More importantly, the preprint's advertised unsmoothed summatory framework has two decisive defects and one pole-order overstatement:

1. its claim that the nontrivial-zero poles of `F_l` are simple silently assumes simplicity of the corresponding zeta zeros; the correct pole order is their multiplicity;
2. Theorem 4.3(i), which claims `RH => Phi_l(x)=x^2/(2 zeta(l+1))+O_l,epsilon(x)` for every fixed `l`, is already false for `l=1` by Montgomery's unconditional `Omega_+- (x sqrt(log log x))` theorem for the classical totient remainder; the displayed proof also omits an exact fractional-part term;
3. Theorem 4.3(ii)'s supposed sufficient condition

```text
Phi_l(x)
 = x^2/(2 zeta(l+1))
   + O_l,epsilon(x^(1-1/(2l)+epsilon))
   for every epsilon>0
```

is **impossible for every fixed `l`**, independently of RH, because the summatory step function has order-`p` jumps at primes whereas the proposed remainder is `o(p)` after choosing `epsilon<1/(2l)`.

Thus the zeta quotient itself is a valid and relevant fixed-depth full-lattice identity, but the proposed unsmoothed summatory RH criterion does not provide a usable new equivalence. The durable line-specific lesson is that a multiplicative coordinate-depth threshold can collapse to a one-variable zeta quotient, while an unsmoothed smooth-main-term remainder is constrained by elementary lattice-point jumps before zeta-zero geometry enters.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + CORRECTION/DECISIVE-NEGATIVE`. The correction is decisive for the **unsmoothed `Phi_l` criterion as stated** and for interpreting the transported line `1-1/(2l)` as new exponent-lattice rigidity. It does not rule out smoothed transforms, different renormalizations, or genuinely mixed-coordinate depth couplings.

## 1. Exact exponent-depth structure and Dirichlet scalarization

For a prime power the definition gives

```text
phi_l(p^a)=p^a                  if a<l,
phi_l(p^a)=p^a(1-1/p)          if a>=l.
```

Hence `phi_l` is multiplicative and its local Dirichlet factor, initially for `Re(s)>2`, is

```text
sum_(a>=0) phi_l(p^a)p^(-as)
 = (1-p^(-[l(s-1)+1]))/(1-p^(-(s-1))).
```

Multiplying over primes yields exactly

```text
F_l(s)=zeta(s-1)/zeta(l(s-1)+1).
```

Equivalently, expanding the reciprocal zeta factor in its absolute-convergence half-plane gives the coefficient identity

```text
phi_l(n)
 = n sum_(d^l | n) mu(d)/d.
```

These statements are theorems in Gaber's preprint. They use the full exponent vector through the coordinate conditions `v_p(n)>=l`, but multiplicativity makes different prime coordinates independent. The entire transform is therefore exhausted by a scalar Euler product.

The convergence boundary must be kept explicit. The Euler-product derivation above is valid for `Re(s)>2`. The formula

```text
zeta(s-1)/zeta(l(s-1)+1)
```

has a meromorphic continuation to the plane because the two zeta factors do. Values or poles of the quotient outside `Re(s)>2` are properties of that continuation; they are not obtained by continuing the prime-by-prime product termwise.

## 2. The critical line is only affinely transported

If `rho` is a nontrivial zero of zeta, a denominator zero occurs when

```text
l(s-1)+1=rho,
```

hence

```text
s_rho=1+(rho-1)/l.
```

The numerator at this point is

```text
zeta((rho-1)/l).
```

For a nontrivial `rho` it cannot vanish: if `(rho-1)/l=rho'` were another zeta zero, then `rho=1+l rho'`; a nontrivial `rho'` would force `Re(rho)>1`, while a trivial `rho'=-2m` would give the negative odd integer `1-2ml`, not a zeta zero. Thus the transported nontrivial denominator zeros are genuine poles.

Their real parts are

```text
Re(s_rho)=1+(Re(rho)-1)/l.
```

Consequently

```text
Re(rho)=1/2
  <=>
Re(s_rho)=1-1/(2l).
```

Nothing in this transformation derives the half-line from the depth geometry. The value `1/2` is already the real part of the zeta zero being affinely re-encoded. This is exactly the kind of distinction required by the line mandate between a useful reformulation and additional RH rigidity.

## 3. Pole-order correction: nontrivial poles are not known to be simple

Corollary 3.3 of the preprint states that the poles associated with nontrivial zeta zeros are simple. The no-cancellation part is valid, but simplicity does not follow.

Let `rho` have multiplicity `m>=1`. Since the affine map

```text
s -> l(s-1)+1
```

has nonzero derivative `l`, the denominator `zeta(l(s-1)+1)` has a zero of exactly order `m` at `s_rho`. As just noted, the numerator is nonzero there. Therefore

```text
ord_pole(F_l,s_rho)=m.
```

So the correct statement is:

```text
each nontrivial zeta zero produces a genuine pole
whose order equals the zero multiplicity.
```

Calling every such pole simple would require the still-unproved assertion that all nontrivial zeros of the Riemann zeta function are simple. This correction changes no pole location and does not affect the affine-divisor observation.

## 4. The exact floor expansion exposes the missing term in Theorem 4.3(i)

Write

```text
Phi_l(x)=sum_(n<=x) phi_l(n).
```

Using the exact coefficient identity and setting

```text
X=x^(1/l),
N_d=floor(x/d^l),
theta_d={x/d^l},
```

one has

```text
Phi_l(x)
 = sum_(d<=X) mu(d)/d * d^l N_d(N_d+1)/2.
```

Since `N_d=x/d^l-theta_d`, direct expansion gives the exact identity

```text
Phi_l(x)
 = x^2/2 sum_(d<=X) mu(d)/d^(l+1)

   + x sum_(d<=X) mu(d)/d (1/2-theta_d)

   + 1/2 sum_(d<=X) mu(d)d^(l-1)
       (theta_d^2-theta_d).
```

Theorem 4.1 of the preprint safely bounds the middle term by `O(x log x)`. But in the proof of Theorem 4.3(i), the displayed refinement replaces it by

```text
x/2 sum_(d<=X) mu(d)/d
```

plus an `O(sum d^(l-1))` remainder. That drops the term

```text
-x sum_(d<=X) mu(d) theta_d/d,
```

which is not absorbed by `O(sum d^(l-1))`.

This is not merely a proof-gap with an obviously true conclusion. At `l=1`, `phi_1=phi` is the ordinary Euler totient, and Montgomery proved unconditionally that for

```text
R(x)=sum_(n<=x) phi(n)-x^2/(2 zeta(2)),
```

one has oscillations of size

```text
Omega_+- (x sqrt(log log x)).
```

Therefore `R(x)=O(x)` is false, whether or not RH holds. Since Theorem 4.3(i) asserts the `O(x)` conclusion for every fixed `l>=1`, its universal statement is false already at `l=1`.

This finding does **not** claim that an `O(x)` theorem is impossible for every `l>=2`; the exact omitted fractional-part term shows that the published argument does not establish it, while Montgomery independently kills the `l=1` instance.

## 5. The converse hypothesis is impossible by prime jumps

The stronger defect is elementary and applies to every fixed depth.

Set

```text
M_l=1/(2 zeta(l+1)),
E_l(x)=Phi_l(x)-M_l x^2.
```

Theorem 4.3(ii) assumes, for every `epsilon>0`,

```text
E_l(x)=O_l,epsilon(x^(alpha_l+epsilon)),
alpha_l=1-1/(2l).
```

Choose once and for all

```text
0<epsilon<1/(2l).
```

Then

```text
beta=alpha_l+epsilon<1,
```

so at integers `n`

```text
E_l(n)-E_l(n-1)=O(n^beta)=o(n).
```

Now take `n=p` prime. The exponent vector is the single basis point `e_p`, hence

```text
phi_1(p)=p-1,
phi_l(p)=p       for l>=2.
```

But exactly

```text
E_l(p)-E_l(p-1)
 = phi_l(p)-M_l(p^2-(p-1)^2)
 = phi_l(p)-(2p-1)/(2 zeta(l+1)).
```

For every fixed `l>=1`, this is

```text
E_l(p)-E_l(p-1)
 = (1-1/zeta(l+1))p + O_l(1).
```

Because `zeta(l+1)>1`, the coefficient is strictly positive. Along the infinite sequence of primes,

```text
|E_l(p)-E_l(p-1)| asymp_l p,
```

contradicting `o(p)`.

Therefore

```text
boxed:
for no fixed l>=1 can the stated
O(x^(1-1/(2l)+epsilon)) bound hold for every epsilon>0.
```

The implication “if this bound holds, then RH” is consequently logically vacuous. Its Mellin-continuation proof may be read as a conditional implication from an impossible premise, but it does not provide a realizable RH criterion for the unsmoothed summatory function.

The obstruction has nothing to do with hypothetical off-line zeros. It is already forced by the size of one-coordinate lattice points `e_p` at the discontinuities of the counting function.

## 6. Prior-art and novelty audit

The primary new-literature anchor is:

- **Ahmed Gaber**, “Euler's `l`-totients and Riemann hypothesis,” arXiv:2607.26114v1 [math.GM], submitted 28 July 2026, https://arxiv.org/abs/2607.26114. The source supplies the definition, multiplicativity, prime-power values, zeta quotient, meromorphic continuation, Möbius coefficient formula, and Theorem 4.3 being audited here.

The independent classical falsification of the `l=1` linear remainder is:

- **Hugh L. Montgomery**, “Fluctuations in the mean of Euler's phi function,” *Proceedings of the Indian Academy of Sciences — Mathematical Sciences* **97** (1987), 239–245. DOI: https://doi.org/10.1007/BF02837826. Montgomery proves the classical totient remainder is `Omega_+- (x sqrt(log log x))`.

There is also pre-2026 evidence that at least the `l=2` arithmetic function was already present independently: OEIS A254503 records in November 2025 the interpretation “number of integers `k` from `1` to `n` that are coprime to the powerful part of `n`,” which is exactly the `l=2` definition. This is used only as a novelty warning, not as theorem-level evidence. No claim is made here that Gaber's general `l`-family itself is new or old.

The durable contribution of this finding is the **line-specific adversarial synthesis and exact correction**:

```text
full exponent-depth threshold
  -> multiplicative scalar zeta quotient
  -> affine transport of the zero divisor,
```

combined with

```text
unsmoothed summatory function
  -> unavoidable prime jumps
  -> no sublinear smooth-main-term remainder.
```

The prime-jump contradiction and the exact missing fractional-part term are elementary derivations and do not depend on absence of prior literature.

## 7. Relationship to nearby prime-lattice findings

`PL-087`--`PL-090` study exponent depth on the **prime-power axis skeleton**, where a fixed ray depth is a time-dilated prime layer and higher-depth tails undergo rank/scale transitions. The present observable is different: `phi_l(n)` is defined on every exponent vector and simultaneously checks all coordinates that have crossed depth `l`.

Despite that genuinely multidimensional input, multiplicativity removes cross-coordinate interaction in the Dirichlet transform. This supplies a complementary negative control:

```text
full-lattice coordinate-depth dependence
   does not imply
mixed-coordinate spectral information.
```

`PL-109` likewise shows that an RH-equivalent harmonic criterion can live on prime axes alone. The present result approaches the same discrimination issue from the opposite direction: a full-lattice observable can look geometrically richer while analytically reducing to an affine zeta quotient.

The prime-jump obstruction also sharpens what a future depth-based candidate must do. If its RH claim is expressed through a counting function with large atomic jumps, demanding a remainder below the jump scale is invalid before any zero-sensitive analysis begins.

## Adversarial boundaries

1. **The zeta quotient is not being rejected.** Its Euler-product identity is correct in `Re(s)>2`, and the quotient gives a legitimate meromorphic continuation beyond that domain.
2. **The transported pole line is mathematically correct under RH.** What fails is interpreting it as an independently selected critical geometry; it is the affine image of the original zeta divisor.
3. **The nontrivial poles are genuine, but not known simple.** Their orders equal the multiplicities of the corresponding zeta zeros.
4. **Theorem 4.3(i) is disproved here only through its `l=1` instance.** Its displayed derivation has a missing fractional-part term for all `l`; no verdict is claimed here on the optimal RH error for every `l>=2`.
5. **Theorem 4.3(ii) is stronger than merely unproved.** Its hypothesis is impossible for every fixed `l`, by the exact prime-jump argument.
6. **Smoothing can evade the jump obstruction.** Mellin/Riesz smoothing, Cesaro averaging, or another kernel can replace atomic jumps by a controlled boundary term. Such a modified criterion would require a fresh derivation and novelty audit.
7. **Nonmultiplicative depth coupling remains open.** An observable coupling several coordinates before taking a transform need not scalarize into independent local factors and is not ruled out by this example.
8. **No Euler product is used inside the critical strip.** All critical-strip statements here refer to meromorphic continuation of the scalar quotient, not convergence of its original Euler product.

## Audit / falsification criterion

The finding can be independently checked by four short tests:

1. derive the local factor from `phi_l(p^a)` and verify `F_l(s)=zeta(s-1)/zeta(l(s-1)+1)` only initially in `Re(s)>2`;
2. at a zeta zero of multiplicity `m`, verify that the affine denominator has zero order `m` and the numerator does not cancel it;
3. expand `floor(x/d^l)=x/d^l-{x/d^l}` exactly and verify the missing term `-x sum mu(d){x/d^l}/d`;
4. assume any remainder `E_l(x)=O(x^beta)` with `beta<1`, evaluate `E_l(p)-E_l(p-1)` at primes, and obtain the contradiction `(1-1/zeta(l+1))p+O_l(1)=o(p)`.

Any failure of one of these checks would invalidate the corresponding correction above.