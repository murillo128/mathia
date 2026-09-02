# PL-111 — Second Riesz smoothing repairs the fixed-depth totient criterion but remains a scalar Mellin test

## Claim

The unsmoothed RH criterion audited and rejected in `PL-110` can be repaired canonically by a second Riesz mean, but the repaired statement still contains no new prime-lattice rigidity: it is exactly a Mellin test for the already-scalarized quotient

```text
F_l(s)=zeta(s-1)/zeta(l(s-1)+1).
```

For fixed integer `l>=1`, let

```text
phi_l(n)
 = n product_(p: v_p(n)>=l) (1-1/p),

alpha_l = 1-1/(2l),

R_(l,2)(x)
 = sum_(n<=x) phi_l(n) (1-n/x)^2.
```

Then

```text
RH
<=>
R_(l,2)(x)
 = x^2/(12 zeta(l+1))
   + O_(l,epsilon)(x^(alpha_l+epsilon))
for every epsilon>0.
```

Thus smoothing genuinely removes the elementary prime-jump obstruction of `PL-110`: the repaired criterion is realizable and RH-equivalent. But `alpha_l` is still only the affine image of the zeta critical line under

```text
rho -> s_rho = 1+(rho-1)/l,
```

and the Riesz kernel is a nonvanishing Mellin multiplier throughout the relevant half-plane. It does not move, constrain, pair, or geometrize the transported zero divisor.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-MELLIN-REPAIR + NEGATIVE-REDIRECT`.

No novelty is claimed for Riesz smoothing, Mellin inversion, or the use of zero-free continuation to characterize summatory errors. Ahmed Gaber's 2026 preprint supplies the arithmetic function and its scalar Dirichlet quotient; the result here is the exact repair of the specific smoothing escape left open by `PL-110` and the corresponding prime-lattice falsification consequence.

## 1. Exact Mellin kernel and main term

`PL-110` records, initially for `Re(s)>2`,

```text
F_l(s)
 := sum_(n>=1) phi_l(n)n^(-s)
  = zeta(s-1)/zeta(l(s-1)+1).
```

For `c>2`, the elementary beta-integral identity

```text
(1-y)_+^2
 = (1/(2 pi i)) integral_(Re(s)=c)
     [2/(s(s+1)(s+2))] y^(-s) ds
```

gives

```text
R_(l,2)(x)
 = (1/(2 pi i)) integral_(Re(s)=c)
     F_l(s) K_2(s) x^s ds,

K_2(s)=2/(s(s+1)(s+2)).
```

The only pole of `F_l` crossed before the transported zero divisor is the pole at `s=2` coming from `zeta(s-1)`. Its residue is

```text
Res_(s=2) F_l(s)=1/zeta(l+1),
```

while

```text
K_2(2)=1/12.
```

Hence the pole contribution is exactly

```text
x^2/(12 zeta(l+1)).
```

The Euler-product derivation of `F_l` is used only in `Re(s)>2`. All contour movement below uses the meromorphic continuation of the zeta quotient, not termwise continuation of the product.

## 2. RH implies the Riesz error bound

Fix a sufficiently small

```text
0<epsilon<1/(2l)
```

and shift the contour to

```text
sigma=alpha_l+epsilon
      =1-1/(2l)+epsilon.
```

Under RH, every nontrivial zero `rho` of zeta has `Re(rho)=1/2`; therefore every corresponding denominator pole

```text
s_rho=1+(rho-1)/l
```

lies exactly on `Re(s)=alpha_l`. The shifted line is strictly to their right, so only the pole at `s=2` is crossed. Denominator poles coming from the trivial zeta zeros lie still farther left.

The required vertical integrability can be obtained from standard consequences of RH without a delicate reciprocal-zeta estimate. On the shifted line,

```text
w=l(s-1)+1
```

has

```text
Re(w)=1/2+l epsilon.
```

Under RH, the classical Littlewood/Mertens consequence

```text
M(u)=sum_(n<=u) mu(n)=O_delta(u^(1/2+delta))
```

holds for every `delta>0`. Choosing `delta<l epsilon` and using partial summation gives, uniformly on this fixed line,

```text
1/zeta(w)
 = w integral_1^infinity M(u)u^(-w-1) du
 = O_(l,epsilon)(1+|Im(w)|).
```

For the numerator, `Re(s-1)=-1/(2l)+epsilon<0`. The functional equation and absolute convergence on the reflected line give

```text
zeta(s-1)
 = O_(l,epsilon)((1+|t|)^(1/2+1/(2l)-epsilon)).
```

Since

```text
K_2(s)=O(|t|^(-3)),
```

the shifted integrand, after removing the factor `x^sigma`, is

```text
O_(l,epsilon)(
  |t|^(-3/2+1/(2l)-epsilon)
),
```

which is integrable; for the worst case `l=1` the exponent is `-1-epsilon`. The same polynomial bounds justify the horizontal sides of a standard truncated contour shift. Therefore

```text
R_(l,2)(x)
 = x^2/(12 zeta(l+1))
   + O_(l,epsilon)(x^(alpha_l+epsilon)).
```

Proving this for all sufficiently small positive `epsilon` implies the stated form for every positive `epsilon` after enlarging the constant where necessary.

## 3. The Riesz error bound implies RH

The converse is cleaner and does not require contour estimates. For `Re(s)>2`, Tonelli/Fubini and the substitution `y=n/x` give the exact Mellin identity

```text
integral_1^infinity R_(l,2)(x)x^(-s-1) dx
 = K_2(s) F_l(s),
```

because for every integer `n>=1`,

```text
integral_n^infinity
  (1-n/x)^2 x^(-s-1) dx
 = n^(-s) integral_0^1 (1-y)^2 y^(s-1) dy
 = n^(-s) K_2(s).
```

Assume now that for every `epsilon>0`,

```text
R_(l,2)(x)
 = C_l x^2 + O_(l,epsilon)(x^(alpha_l+epsilon)),

C_l=1/(12 zeta(l+1)).
```

Then

```text
K_2(s)F_l(s)-C_l/(s-2)
 = integral_1^infinity
     [R_(l,2)(x)-C_l x^2] x^(-s-1) dx
```

extends holomorphically to

```text
Re(s)>alpha_l+epsilon.
```

Because this holds for every `epsilon>0`, the left side is holomorphic throughout

```text
Re(s)>alpha_l,
```

apart from the explicitly removed pole at `s=2`. The multiplier

```text
K_2(s)=2/(s(s+1)(s+2))
```

has no zeros, and its own poles `0,-1,-2` lie outside this half-plane.

Suppose zeta had a nontrivial zero

```text
rho=beta+i gamma,
qquad beta>1/2.
```

Then

```text
s_rho=1+(rho-1)/l
```

satisfies

```text
Re(s_rho)>alpha_l.
```

At this point the denominator `zeta(l(s-1)+1)` vanishes. As proved in `PL-110`, the numerator `zeta((rho-1)/l)` cannot vanish there, so `F_l` has a genuine pole whose order equals the multiplicity of `rho`. This contradicts the holomorphy forced by the Riesz bound. Hence there are no nontrivial zeta zeros with real part greater than `1/2`; the functional-equation symmetry then gives RH.

## 4. What smoothing repairs — and what it does not

The unsmoothed summatory function in `PL-110` has order-`p` jumps at primes. That makes an error `o(x)` against a smooth quadratic main term impossible before zeta zeros enter. The factor

```text
(1-n/x)^2
```

removes precisely that boundary defect: as `x` crosses an integer, the newly entering term has zero weight and the Mellin kernel gains cubic decay in vertical frequency.

This is a genuine analytic repair, not a new geometric mechanism. The arithmetic input still begins with the full-lattice depth observable

```text
phi_l(v)
 = exp(<v,(log p)_p>)
   product_(p:v_p>=l)(1-1/p),
```

but multiplicativity has already collapsed its Dirichlet transform to the one-variable quotient `F_l`. Riesz smoothing merely multiplies that quotient by `K_2(s)`, and `K_2` is nonzero on the entire zero-sensitive half-plane. Therefore the locations and multiplicities of the transported nontrivial poles are unchanged.

In particular, the exponent

```text
alpha_l=1-1/(2l)
```

is not selected by a lattice metric, spectral self-duality, positivity law, or critical Sobolev threshold. It is exactly the image of `Re(rho)=1/2` under the affine denominator map `rho=l(s-1)+1`.

## 5. Prior art and novelty audit

The arithmetic source is:

- **Ahmed Gaber**, “Euler's `l`-totients and Riemann hypothesis,” arXiv:2607.26114v1 [math.GM], submitted 28 July 2026. The paper supplies `phi_l`, its prime-power values and multiplicativity, the coefficient formula, and the meromorphic quotient `F_l(s)=zeta(s-1)/zeta(l(s-1)+1)`. `PL-110` separately audits defects in its unsmoothed summatory RH criterion.

The Mellin/Riesz method itself is classical. The implication from RH to `M(x)=O_epsilon(x^(1/2+epsilon))`, the functional equation of zeta, and the standard Mellin continuation principle used above belong to classical analytic number theory; see for example E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford University Press, 1986.

A targeted literature search on 2 September 2026 found classical Riesz-mean work for Euler/Dedekind-type totients and many standard RH criteria obtained from smoothed summatory functions, but no source was found that makes this precise second-Riesz statement for Gaber's 2026 `l`-totient family. That absence is **not** used as a novelty claim. Given the exact scalar quotient, the criterion is a direct classical Mellin construction.

## 6. Adversarial boundaries

1. **This does not rehabilitate the unsmoothed theorem.** `PL-110`'s prime-jump contradiction remains exact. The new statement concerns a different, explicitly smoothed observable.
2. **Second-order smoothing is chosen for a clean unconditional contour estimate under RH.** Its `|t|^-3` Mellin decay comfortably dominates the functional-equation growth of `zeta(s-1)` together with the elementary `O(|t|)` reciprocal bound obtained from the RH Mertens estimate. No minimality claim is made for the smoothing order.
3. **No zero simplicity is assumed.** A denominator zero of multiplicity `m` gives a pole of multiplicity `m`; the converse excludes poles regardless of multiplicity.
4. **No Euler product is continued into the strip.** The product establishes the quotient only in its absolute-convergence region. The meromorphic quotient and Mellin transform provide the continuation used by the criterion.
5. **The criterion is an equivalence, not an explanation of `1/2`.** Its critical exponent is inherited from the location of the denominator zeros under an affine change of variable.
6. **Nonmultiplicative depth coupling remains outside this no-go.** A construction that couples several exponent coordinates before scalar Dirichlet transformation need not reduce to a zeta quotient and is not ruled out here.

## Consequence for the research line

`PL-110` left smoothing as the obvious way to evade the unsmoothed jump obstruction. This finding closes that ambiguity sharply: smoothing can indeed produce a mathematically sound RH-equivalent statement, but doing so only restores the ordinary Mellin correspondence between summatory growth and the pole-free half-plane of a scalar zeta quotient.

Hence the route

```text
fixed coordinate depth
 -> multiplicative scalarization
 -> choose a smoother summatory kernel
 -> RH-equivalent error exponent
```

is analytically valid but does not add the structure sought by `prime_lattice`. A future depth-based mechanism must obtain information **before** multiplicativity factorizes the coordinates — for example through a genuinely mixed-coordinate coupling, a non-scalar operator, or a positivity/self-duality principle that constrains zero location rather than merely translating the zeta divisor.