# PL-037 — Centered Bohr–Toeplitz prime adjacency has exact `1` and `1/2` thresholds but is zero-blind

## Claim

There is a natural self-adjoint field obtained by symmetrizing the prime-coordinate shifts of the exponent lattice. It escapes one limitation of `PL-031`: with amplitudes `p^(-sigma)` rather than positive Dirichlet-form conductances `p^(-2 sigma)`, it gives a canonical **unbounded self-adjoint** operator throughout the strip

```text
1/2 < sigma <= 1.
```

However, its spectrum and its critical behavior are completely determined by elementary product probability and prime summability, and the vertical Kronecker parameter is pure gauge. The construction therefore does **not** localize Riemann-zero ordinates.

Let

```text
S_p e_n = e_(pn)
```

on `ell^2(N)` and define the coordinate adjacency

```text
A_p = S_p + S_p^*.
```

For a finite prime cutoff `y`, set

```text
X_(sigma,y)
  = sum_(p<=y) p^(-sigma) A_p.
```

Then the exponent factorization

```text
ell^2(N)
  ~= tensor_product_p ell^2(N_0)
```

turns each `A_p` into the free half-line Jacobi matrix `S+S^*` on the `p`-coordinate. Its vacuum spectral measure is the Wigner semicircle law

```text
d mu_sc(x) = (1/(2 pi)) sqrt(4-x^2) 1_[-2,2](x) dx.
```

Consequently the joint spectral representation sends `X_(sigma,y)` to multiplication by the sum of independent centered semicircle variables

```text
sum_(p<=y) p^(-sigma) x_p,
qquad x_p iid mu_sc,
E[x_p]=0,
Var(x_p)=1.
```

This yields an exact two-threshold classification:

```text
sigma > 1:
    X_sigma exists as a bounded self-adjoint norm limit,
    spectrum(X_sigma) = [-2 P(sigma), 2 P(sigma)].

1/2 < sigma <= 1:
    X_sigma exists canonically as an unbounded self-adjoint
    strong-resolvent limit,
    spectrum(X_sigma) = R.

0 < sigma <= 1/2:
    the unrenormalized independent coordinate series diverges a.s.,
    and X_(sigma,y) has no self-adjoint strong-resolvent limit.
```

Here

```text
P(s)=sum_p p^(-s)
```

is used only in its ordinary convergent half-plane `Re(s)>1`.

At the critical exponent `sigma=1/2`, the vacuum variance is

```text
V_y = sum_(p<=y) 1/p
    = log log y + B_1 + o(1),
```

and the normalized vacuum spectral laws satisfy

```text
X_(1/2,y) / sqrt(V_y)
    -> N(0,1)
```

in distribution. Thus `1/2` is again selected by a mathematically genuine prime-lattice spectral threshold, but the critical scaling is the ordinary Lindeberg Gaussian limit rather than a zeta-zero law.

Adding the vertical Bohr/Kronecker phases does not change this. For

```text
X_(sigma,t,y)
 = sum_(p<=y) p^(-sigma)
     (p^(-it) S_p + p^(it) S_p^*),
```

and

```text
D_t e_n = n^(-it) e_n,
```

one has exactly

```text
X_(sigma,t,y)=D_t X_(sigma,0,y) D_t^*.
```

The same equivalence survives every self-adjoint limit above. Since `D_t e_1=e_1`, even the vacuum spectral measure is independent of `t`. No spectral invariant in this family can distinguish a Riemann-zero ordinate.

**Evidence/status:** `EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` for the route

```text
symmetrized prime-coordinate shifts
+ canonical Bohr radial amplitudes p^(-sigma)
+ vertical Kronecker phases exp(-it log p)
    -> self-adjoint spectrum or critical scaling that localizes zeta zeros.
```

The single-coordinate free Jacobi/semicircle transform, independent-random-series criteria, and Lindeberg central limit theorem are classical. The arithmetic specialization and the two-threshold synthesis are derived here. A targeted novelty search found the standard Jacobi and Hardy/Bohr ingredients but no exact prime-weighted construction of this form; no novelty claim is made for the synthesis.

## Exact exponent-lattice tensor model

Write

```text
n = product_p p^(alpha_p),
alpha=v(n) in N_0^(P).
```

Unique factorization gives the Hilbert-space identification

```text
e_n <-> tensor_product_p delta_(alpha_p),
```

with all but finitely many tensor factors equal to the vacuum `delta_0`. Under this identification,

```text
S_p
```

acts only on the `p`-coordinate as the unilateral shift

```text
S delta_k = delta_(k+1).
```

Thus

```text
A_p=S_p+S_p^*
```

is the coordinate half-line adjacency. For distinct primes the coordinate operators strongly commute.

The same object has a direct Bohr/Hardy interpretation. In `H^2(T^infinity)`, the monomial corresponding to `n` is

```text
z^(v(n)),
```

and `S_p` is multiplication by the coordinate `z_p`. Hence `A_p` is the Toeplitz compression of

```text
z_p + conjugate(z_p) = 2 Re(z_p).
```

The field `X_(sigma,t,y)` is therefore the finite-coordinate Toeplitz quantization of the real linear functional obtained by sampling the Bohr curve amplitudes

```text
p^(-sigma) exp(-it log p).
```

This is not an arbitrary graph operator added to the lattice: it is the most direct self-adjoint linearization of its canonical prime-coordinate shifts.

## One prime is the free Jacobi / semicircle model

Let

```text
J=S+S^*
```

on `ell^2(N_0)`. Define the rescaled Chebyshev polynomials of the second kind

```text
q_k(x)=U_k(x/2).
```

They are orthonormal for

```text
d mu_sc(x)
 = (1/(2 pi)) sqrt(4-x^2) dx,
-2<=x<=2,
```

and satisfy

```text
x q_0 = q_1,
x q_k = q_(k+1)+q_(k-1),   k>=1.
```

Therefore the unitary spectral transform

```text
delta_k -> q_k
```

conjugates `J` to multiplication by `x` on `L^2(mu_sc)`.

This is the classical free half-line Jacobi matrix. For prior-art control, Killip and Simon use the same free Jacobi operator `J_0` with spectrum `[-2,2]` as the reference object in their spectral theory of Jacobi matrices:

- Rowan Killip, Barry Simon, “Sum rules for Jacobi matrices and their applications to spectral theory,” *Annals of Mathematics* **158**(1) (2003), 253–321, DOI `10.4007/annals.2003.158.253`, arXiv:`math-ph/0112008`.

The prime-lattice step is only to place independent copies of this classical coordinate operator on the prime tensor factors.

## Joint spectral representation

Tensoring the one-coordinate transforms yields

```text
U : ell^2(N)
    -> L^2(mu_sc^(tensor P)).
```

The vacuum vector `e_1`, whose exponent vector is zero, becomes the constant function `1`. Under `U`,

```text
U A_p U^* = M_(x_p),
```

where the coordinate variables `{x_p}` are independent under the product measure, each with the semicircle law.

Since

```text
E[x_p]=0,
E[x_p^2]=1,
|x_p|<=2,
```

we obtain

```text
U X_(sigma,y) U^*
 = M_(Z_(sigma,y)),

Z_(sigma,y)
 = sum_(p<=y) p^(-sigma) x_p,

Var Z_(sigma,y)
 = sum_(p<=y) p^(-2 sigma).
```

The spectral question for the prime adjacency field has therefore become an exact classical independent-random-series problem.

## The square-summability threshold is exactly `sigma=1/2`

For `sigma>1/2`,

```text
sum_p p^(-2 sigma)=P(2 sigma)<infinity.
```

The summands

```text
p^(-sigma) x_p
```

are independent, centered, uniformly bounded, and have summable variances. Hence their series converges almost surely and in `L^2` to a real random variable

```text
Z_sigma=sum_p p^(-sigma)x_p.
```

Let

```text
X_sigma = U^* M_(Z_sigma) U.
```

Multiplication by a finite real random variable is self-adjoint on its maximal domain. Moreover, for every nonreal `z`,

```text
1/(Z_(sigma,y)-z)
 -> 1/(Z_sigma-z)
```

almost surely and is uniformly bounded by `1/|Im z|`. Dominated convergence therefore gives strong convergence of resolvents:

```text
(X_(sigma,y)-z)^(-1)
 -> (X_sigma-z)^(-1).
```

Thus the infinite prime field has a canonical self-adjoint strong-resolvent limit throughout `sigma>1/2`, including the entire open critical strip immediately to the right of the critical line.

For `0<sigma<=1/2`,

```text
sum_p p^(-2 sigma)=infinity.
```

Because the centered summands tend uniformly to zero and are eventually below any fixed truncation threshold, Kolmogorov's three-series criterion reduces the convergence question to variance summability. The series therefore does **not** converge almost surely.

There is an operator-level strengthening. Put

```text
V_y=sum_(p<=y) p^(-2 sigma).
```

Since `V_y->infinity` and the summands are bounded,

```text
max_(p<=y) |p^(-sigma)x_p| / sqrt(V_y) -> 0.
```

The Lindeberg condition is automatic, so

```text
Z_(sigma,y)/sqrt(V_y)
 -> N(0,1)
```

in distribution. Hence for every fixed `R`,

```text
Prob(|Z_(sigma,y)|<=R) -> 0.
```

It follows that

```text
1/(Z_(sigma,y)-i) -> 0
```

in probability; boundedness by `1` upgrades this to strong convergence of the corresponding multiplication operators to zero. But the zero operator cannot equal `(H-i)^(-1)` for any self-adjoint `H`. Therefore the unrenormalized partial sums have **no self-adjoint strong-resolvent limit** at or below `1/2`.

This is a genuine operator threshold, not merely divergence of a chosen norm.

## The second threshold at `sigma=1`

For `sigma>1`, absolute prime summability gives

```text
sum_p p^(-sigma)=P(sigma)<infinity.
```

Since `||A_p||=2`,

```text
sum_p ||p^(-sigma)A_p||
 <= 2 P(sigma)<infinity,
```

so `X_sigma` converges in operator norm and is bounded.

In the product representation,

```text
|Z_sigma| <= 2 P(sigma).
```

Its support is exactly the entire interval

```text
[-2P(sigma),2P(sigma)].
```

Indeed, finite partial sums have support equal to the Minkowski sum of their coordinate intervals, and the absolutely summable tail has arbitrarily small deterministic diameter. Therefore

```text
boxed: spectrum(X_sigma)
       =[-2P(sigma),2P(sigma)],
       sigma>1.
```

For `1/2<sigma<=1`, square summability still constructs the self-adjoint field but

```text
sum_p p^(-sigma)=infinity.
```

Its support is then all of `R`. To see this without heuristic endpoint arguments, fix `x in R` and `epsilon>0`. Choose a finite prime cutoff `y` so large that simultaneously

```text
2 sum_(p<=y) p^(-sigma) > |x|+epsilon
```

and the variance of the remaining tail is small enough that

```text
Prob(|tail|<epsilon/2)>0.
```

The finite partial sum has a continuous convolution density positive on the interior of its support interval, so it has positive probability to lie within `epsilon/2` of `x`. Independence of the tail then gives

```text
Prob(|Z_sigma-x|<epsilon)>0.
```

for every `x,epsilon`. Thus the essential range is `R`, and

```text
boxed: spectrum(X_sigma)=R,
       1/2<sigma<=1.
```

So the apparently promising unbounded self-adjoint escape does exist, but its spectrum is maximally non-discrete rather than a Riemann-zero spectrum.

## Critical scaling is Gaussian

At `sigma=1/2`,

```text
V_y=sum_(p<=y) 1/p.
```

Mertens' theorem for primes gives

```text
V_y=log log y+B_1+o(1).
```

The same Lindeberg argument therefore yields

```text
Z_(1/2,y)/sqrt(log log y+B_1+o(1))
 -> N(0,1).
```

Since `e_1` is the product vacuum, this is exactly convergence of the normalized **vacuum spectral measures** of the finite self-adjoint operators `X_(1/2,y)`.

Thus the critical exponent is not merely where a formal series changes convergence class. It has a canonical finite-cutoff spectral scaling law. But that law is universal Gaussian behavior of many small independent coordinate contributions. It contains no visible Riemann-zero spacing, no functional equation, and no analytic-continuation input.

The same square-summability boundary holds for the vertical-tangent amplitudes

```text
b_p(sigma)=(log p)p^(-sigma),
```

because

```text
sum_p (log p)^2 p^(-2 sigma)
```

converges exactly for `sigma>1/2`; absolute summability of

```text
sum_p (log p)p^(-sigma)
```

starts exactly at `sigma>1`. Thus inserting the canonical tangent weight `log p` changes the variance scale but not either threshold.

## Vertical Kronecker flow is exact unitary gauge

Define

```text
D_t e_n=n^(-it)e_n.
```

Then

```text
D_t S_p D_t^* e_n
 = p^(-it)S_p e_n,
```

so

```text
D_t S_p D_t^*=p^(-it)S_p,
D_t S_p^* D_t^*=p^(it)S_p^*.
```

Consequently, for every finite cutoff,

```text
X_(sigma,t,y)
 =D_t X_(sigma,0,y)D_t^*.
```

For `sigma>1/2`, strong-resolvent uniqueness passes the identity to the infinite limit:

```text
X_(sigma,t)=D_t X_(sigma,0)D_t^*.
```

Therefore spectrum, spectral type, resolvent norms, and all unitary spectral invariants are independent of `t`.

The vacuum is fixed:

```text
D_t e_1=e_1.
```

Hence even the scalar spectral measure

```text
<e_1, f(X_(sigma,t)) e_1>
```

is exactly independent of `t`. This is the same pure-gauge principle that appeared for the Hasse Laplacian in `PL-031`, now applied to an unbounded self-adjoint field that actually exists in `1/2<sigma<=1`.

Thus no ordinate `t=gamma` of a zeta zero can be selected by the spectrum or vacuum law of this construction.

## Characteristic function sees only convergent prime-zeta data

For one radius-`2` semicircle variable,

```text
phi_sc(u)
 = integral exp(iux) dmu_sc(x)
 = J_1(2u)/u,
```

with the value at `u=0` understood by continuity.

For `sigma>1/2`, independence gives the exact vacuum characteristic function

```text
phi_sigma(t)
 = product_p
   [J_1(2t p^(-sigma))/(t p^(-sigma))].
```

Near `t=0`,

```text
log phi_sc(u)
 = -u^2/2 - u^4/24 + O(u^6),
```

and more generally the Taylor expansion of `log phi_sigma` is a linear combination of

```text
P(2 sigma), P(4 sigma), P(6 sigma), ... .
```

Every one of these arguments lies strictly to the right of `1` when `sigma>1/2`. Therefore the entire local spectral-cumulant structure uses the prime zeta function only in its **ordinary absolutely convergent domain**.

No identity here analytically continues the Euler product or prime zeta through `Re(s)=1`. Importing the known continuation formula for `P(s)` and then pointing to its inherited zeta-zero singularities would simply add external zeta information to a field whose native spectral law does not require it.

This domain audit is important: the construction singles out `1/2` because the **squared** radial amplitudes cross the ordinary prime-sum abscissa at

```text
2 sigma=1,
```

not because the Riemann zero divisor has entered the operator.

## Beurling / arbitrary-frequency control

Nothing in the random-series mechanism depends on a special relation among rational primes beyond the chosen amplitude sequence.

For any positive frequency list `{lambda_j}`, take a free exponent cone with coordinate shifts and amplitudes

```text
a_j(sigma)=exp(-sigma lambda_j).
```

The identical tensor/Jacobi construction has:

```text
self-adjoint random-series existence
    <=> sum_j exp(-2 sigma lambda_j)<infinity,

boundedness by absolute convergence
    <= sum_j exp(-sigma lambda_j)<infinity.
```

The rational-prime value `1/2` occurs because `lambda_j=log p_j` makes the first condition

```text
sum_p p^(-2 sigma)<infinity.
```

Thus the threshold is controlled by the abscissa of convergence of the **one-prime counting measure**, not by the location of zeros of a completed zeta function. Beurling systems with the same relevant summability profile reproduce the same operator threshold regardless of their zero divisor.

This is consistent with the flexibility obstruction in `PL-015`: square-summability geometry can be meaningful without being RH-rigid.

## Relation to PL-001, PL-030, and PL-031

`PL-001` showed that the Bohr evaluation curve enters the `ell^2` polydisk exactly for `sigma>1/2`. `PL-030` found the same boundary as a Kakutani measure-class transition for the canonical GCD/Poisson product measure. `PL-031` found it again for positive Hasse-graph conductances `p^(-2 sigma)`, but there the form is bounded above the threshold and has trivial finite-energy domain below it.

The present field explains a distinct operator meaning of the same exponent:

```text
sigma>1/2
    <=> the centered prime-coordinate amplitudes are square summable
    <=> the symmetrized Bohr–Toeplitz field has a self-adjoint random-series limit.
```

Crucially, this gives an actual unbounded self-adjoint operator for

```text
1/2<sigma<=1,
```

so it is not merely another bounded-kernel observation. The negative comes only after constructing the operator: its spectrum is `R`, its vertical flow is gauge, and its critical finite-cutoff law is Gaussian.

## Prior-art and novelty assessment

The following ingredients are classical and are not discoveries:

- the Bohr identification of the Dirichlet-series coefficient Hilbert space with the analytic infinite-torus/polydisk Hardy space (`Hedenmalm–Lindqvist–Seip`, already recorded in `SOURCES.md`);
- the free half-line Jacobi matrix and its semicircle spectral measure (`Killip–Simon` and standard orthogonal-polynomial theory);
- Kolmogorov convergence criteria for independent random series;
- the Lindeberg–Feller central limit theorem;
- convergence of the prime zeta series for `Re(s)>1` and Mertens' divergence/asymptotic for reciprocal primes.

A targeted search across Jacobi operators, Hardy spaces of Dirichlet series, multiplicative shifts, prime-weighted adjacency operators, and semicircle random series did not locate this exact arithmetic synthesis. That absence is not treated as evidence of novelty: the construction is a direct tensor specialization of standard ingredients, and the durable value here is the exact obstruction/classification rather than a priority claim.

## Boundary conditions and adversarial checks

### The half-line semicircle law is not Haar coordinate distribution

On the full torus a coordinate `2 Re(z_p)` under Haar has the arcsine law. The semicircle law appears here because `S_p+S_p^*` is the **Hardy/Toeplitz compression** to the nonnegative exponent half-line. Its spectral transform is the free Jacobi transform, not raw multiplication by `2 cos(theta_p)` on full `L^2(T)`.

This distinction is essential and is why the product spectral measure above is `mu_sc^(tensor P)` rather than Haar pushed forward by cosine coordinates.

### The result does not forbid renormalized critical operators

For `sigma<=1/2`, the statement is only that the unrenormalized partial sums have no self-adjoint strong-resolvent limit. One can normalize the finite cutoffs; at `sigma=1/2` their vacuum laws converge to a Gaussian. A different subtraction, scaling, interaction term, or nonlocal completion could define another object and would require a separate audit.

### Full-real spectrum does not by itself determine spectral type

For `1/2<sigma<=1`, the exact statement needed here is that the essential range, hence the spectrum of the multiplication operator, is all of `R`. No unnecessary claim about absolute continuity, multiplicity, or fine spectral density is made.

### Vertical gauge invariance is exact, not asymptotic

The `t`-independence follows from a unitary conjugacy for every finite cutoff and therefore for every strong-resolvent limit. It cannot be repaired by taking larger prime cutoffs or by examining a different ordinary spectral statistic of the same family.

### Analytic continuation remains external

All prime-zeta quantities used natively satisfy `Re(argument)>1`. The construction neither continues `zeta` nor proves its functional equation. Any later use of analytically continued prime-zeta singularities must identify the extra mechanism that performs that continuation rather than attributing it to this field.

## Falsification / escape test

A future self-adjoint prime-adjacency proposal escapes this negative only if it adds structure not removed by the following controls:

1. **vertical gauge test:** the relevant `t`-dependence must not be unitarily conjugate to `t=0` by `e_n -> n^(-it)e_n`;
2. **independent-coordinate test:** its spectral law must not reduce to a product convolution determined only by one-prime coordinate measures and square-summability;
3. **Beurling test:** it must distinguish rational-prime arithmetic from a free exponent system with a matched amplitude/summability profile;
4. **continuation test:** any use of zeta zeros must come with an independent theorem carrying the construction through `Re(s)=1`, rather than inserting analytically continued `P` or `zeta` afterward;
5. **spectral-rigidity test:** the extra term must change the full-real/interval spectrum or create a genuine positivity, determinant, scattering, or self-duality constraint tied to the completed global problem.

If a candidate still diagonalizes to a sum of independent coordinate variables and its vertical phase is removable by `D_t`, it remains a zero-blind background field even if `1/2` is a sharp existence threshold.

## Consequence for the research line

The prime lattice does support a surprisingly natural self-adjoint spectral object whose existence boundary is exactly the critical line:

```text
Bohr radial amplitudes p^(-sigma)
    + Hardy half-line prime shifts
    + self-adjoint symmetrization
        -> square-summable random Jacobi field
        -> threshold sigma=1/2.
```

But the same derivation explains why that coincidence cannot carry RH by itself:

```text
sigma=1/2
    = variance / square-summability threshold,
not a zeta-zero localization theorem;

1/2<sigma<=1
    -> spectrum = R;

vertical t
    -> exact unitary gauge;

critical cutoff scaling
    -> Gaussian.
```

The surviving spectral target must therefore introduce a **global coupling between prime coordinates** that destroys the independent-product reduction and is not removable by the Kronecker gauge. The adelic/Weil/scattering structures isolated in `PL-013`, `PL-014`, and `PL-033` remain examples of the kind of extra nonlocal completion capable of carrying analytic continuation and the zero divisor.