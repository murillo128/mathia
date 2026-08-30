# PL-048 — Hedenmalm’s prime-dilation theta pencil is a universal Mellin spectralizer; the missing rigidity lies in the seed metric

## Claim

Håkan Hedenmalm's 2026 theta-function construction gives a particularly direct and rigorous bridge from the ordinary rational-prime dilation semigroup to the completed Riemann `Xi` function and then to a generalized differential eigenvalue problem. In prime-exponent coordinates, his dilation-sum operator is

```text
E f(t) = sum_{n>=1} f(nt)
       = sum_{alpha in N_0^(P)} f(exp(<alpha,log p>) t),
```

with the pointwise factorization

```text
E = product_p E_p,
E_p f(t) = sum_{k>=0} f(p^k t),
```

whenever the relevant sums are absolutely meaningful. Applied to a fixed archimedean Hermite seed `h_00`, it produces the positive Jacobi-theta kernel

```text
Theta_00(i t^2) = t^(1/2) E h_00(t),
```

whose Mellin transform is the entire function

```text
Xi(alpha) = xi(1/2+i alpha)
          = integral_0^infinity Theta_00(i t^2) t^(i alpha) dt/t.
```

Hedenmalm then constructs a second-order differential pencil whose admissible complex eigenparameters are exactly the zeros of `Xi`.

This is **genuine prior art for a completed prime-lattice -> spectral-zero route**, and it is stronger than simply inserting the meromorphic scalar `zeta` into a functional calculus: the theta kernel and its Mellin transform cross the continuation barrier through Jacobi/Poisson structure.

However, the eigenvalue encoding and the rational-prime dilation factorization themselves have no zero-localization rigidity. The same differential pencil works for a broad class of positive inversion-symmetric Mellin kernels, and on a fast-decay class the same ordinary-prime dilation operator `E` is Möbius-invertible. Consequently one can build an explicit positive inversion-symmetric kernel with the **same rational-prime dilation architecture** whose Mellin transform has non-real zeros in the same `|Im alpha|<1/2` strip.

Therefore the route

```text
ordinary prime-exponent dilation lattice
+ positive inversion-symmetric completed kernel
+ Mellin transform
+ Hedenmalm-type differential eigenvalue pencil
    -> real zero spectrum / RH
```

is decisively insufficient. The genuinely hard zeta-specific step is the extra positive Hilbert-space metric/self-adjointness condition that Hedenmalm proposes but does not construct.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route above. Hedenmalm's theta identity, complex-zero boundary-value theorem, and conditional self-adjoint-pair implication are literature results. The universal pencil calculation, Möbius-inverse control, and explicit off-axis Gaussian-mixture example below are exact derived identities under stated absolute-convergence hypotheses. No novelty claim is made for the classical Möbius inversion or for the general fact that positive even Fourier kernels need not be real-rooted.

## The ordinary exponent lattice is literally present

Let

```text
D_n f(t) = f(nt).
```

Unique factorization gives

```text
D_n = product_p D_p^(v_p(n)),
```

and therefore

```text
E = sum_{n>=1} D_n
  = sum_{alpha in N_0^(P)} product_p D_p^(alpha_p).
```

Writing `x=log t`, each prime direction becomes the one-sided translation

```text
x -> x + log p,
```

and an integer `n` acts by

```text
x -> x + log n
     = x + <v(n),(log p)_p>.
```

Thus Hedenmalm's `E` is not merely analogous to the exponent lattice: it is the positive prime cone acting by logarithmic translations, subsequently compressed through the energy map `alpha -> <alpha,log p>`.

The paper records the Euler-type operator factorization

```text
E = product_p E_<p>,
E_<p> f(t) = sum_{k>=0} f(p^k t),
```

with the explicit caveat that the sums/products must be meaningful on the functions under consideration. For the rapidly decaying theta seed used below, the integer sum is pointwise absolutely convergent for every fixed `t>0`; no claim of a bounded-operator Euler product on a global Hilbert space is needed here.

## The archimedean seed completes the lattice into an entire object

Hedenmalm defines a particular rapidly decaying function `h_00`, a linear combination of Hermite functions of degrees `0` and `4`, and proves

```text
Theta(t) := Theta_00(i t^2)
          = t^(1/2) E h_00(t).
```

The Jacobi identity gives

```text
Theta(1/t)=Theta(t),
```

and the paper proves `Theta(t)>0` together with Gaussian decay at both multiplicative ends after using this inversion symmetry.

In logarithmic coordinates,

```text
q(x) = Theta(e^x)
```

is therefore a positive even rapidly decaying function. Its ordinary Fourier transform is exactly Riemann's completed function in the centered parameter:

```text
Xi(alpha)
  = integral_R q(x) exp(i alpha x) dx
  = xi(1/2+i alpha).
```

For a nontrivial zeta zero

```text
rho = beta + i gamma,
```

the corresponding spectral parameter is

```text
alpha = gamma + i(1/2-beta).
```

Hence

```text
Re(rho)=1/2  <=>  alpha is real.
```

This explains exactly where the critical line becomes a real spectral axis in this formulation: first the archimedean Jacobi/Poisson completion centers the functional equation at `1/2`, and then Mellin becomes Fourier transform in `log t`.

This is not a continuation of the scalar Euler product into the critical strip. The integral defining `Xi(alpha)` is entire because `Theta(e^x)` decays rapidly at both ends. The prime-dilation representation is an absolutely meaningful real-variable sum on the special seed, while the passage to the entire function uses the theta/Jacobi identity. This distinction survives the analytic-continuation audit demanded by this research line.

## Hedenmalm's differential pencil encodes all complex zeros

Set

```text
D_x f(t) = (t/i) f'(t),
phi(t)   = -log Theta(t),
L_phi f  = D_x f + f D_x phi.
```

Equivalently,

```text
L_phi f = exp(-phi) D_x(exp(phi) f).
```

Hedenmalm proves first for real `alpha`, and then in Theorem 3.3.3 for complex `alpha`, that the boundary-value problem

```text
L_phi D_x u + alpha L_phi u = 0
```

with the stated decay at `0` and `infinity` has a nonzero solution exactly when

```text
Xi(alpha)=0.
```

The solution is explicitly

```text
u_alpha(t)
  = t^(-i alpha)
    integral_0^t y^(i alpha) Theta(y) dy/y.
```

For actual zeta zeros, Hedenmalm notes a stronger super-polynomial boundary condition that is independent of `alpha`, so the complex eigenvalue statement is not obtained by hiding the zero in an `alpha`-dependent boundary condition.

The calculation behind the pencil is short:

```text
D_x u_alpha + alpha u_alpha = (1/i) Theta,
```

and since `Theta=exp(-phi)`, one has

```text
L_phi Theta = 0.
```

Therefore

```text
L_phi(D_x u_alpha + alpha u_alpha)=0.
```

The second boundary condition at `infinity` is precisely what imposes the vanishing of the full Mellin transform.

## The pencil mechanism is universal for Mellin kernels

The same calculation does not use any special arithmetic identity once the kernel `Theta` has been supplied.

Let `Theta:(0,infinity)->(0,infinity)` be smooth and decay faster than every power at both `0` and `infinity`. Define

```text
F(alpha)
  = integral_0^infinity Theta(t)t^(i alpha) dt/t,
phi=-log Theta,
```

and define `u_alpha` by the same integral formula. Then, identically,

```text
L_phi D_x u_alpha + alpha L_phi u_alpha = 0.
```

Whenever `F(alpha)=0`, the two tails of the rapidly decaying Mellin integral give the same parameter-independent super-polynomial boundary decay as in the theta case. Thus zeros of `F` become generalized eigenparameters of exactly the same type of differential pencil.

So the implication

```text
Mellin zero -> Hedenmalm-type generalized eigenvalue
```

is a broad transform identity, not a zeta-localization theorem. The zeta-specific question is whether the particular theta pencil carries an additional positive/self-adjoint structure that generic kernels do not.

## Matched control: a positive inversion-symmetric kernel with off-real zeros

This flexibility can be made completely explicit while preserving the most visible theta-side geometry.

Take, for example,

```text
q(x)
  = exp(-x^2)
    + (1/4) exp(-(x-4)^2)
    + (1/4) exp(-(x+4)^2).
```

Then `q` is smooth, strictly positive, even, and Gaussian-decaying. Put

```text
Theta_*(t)=q(log t).
```

Therefore

```text
Theta_*(t)>0,
Theta_*(1/t)=Theta_*(t),
```

and it decays faster than every multiplicative power at both endpoints.

Its Mellin transform is elementary:

```text
F_*(alpha)
  = sqrt(pi) exp(-alpha^2/4)
    [1 + (1/2) cos(4 alpha)].
```

There are no real zeros, because for real `alpha`

```text
1 + (1/2) cos(4 alpha) >= 1/2.
```

But there are infinitely many non-real zeros,

```text
alpha_{k,+/-}
  = ((2k+1) pi +/- i arcosh(2))/4,
k in Z.
```

Their imaginary parts satisfy

```text
|Im alpha_{k,+/-}|
  = arcosh(2)/4
  ~= 0.32924
  < 1/2.
```

Thus this control has the same positive-even log-kernel symmetry and places its generalized eigenvalues strictly off the real axis **inside the same vertical alpha-strip in which nontrivial zeta zeros would appear**.

Applying the universal calculation above gives the corresponding differential pencil with these off-real eigenparameters.

This is a direct falsification test for any argument claiming that positivity of the Mellin kernel, inversion symmetry, rapid endpoint decay, or the bare differential-pencil form itself forces spectral reality.

## The same ordinary-prime dilation operator can realize the control

One might object that the Gaussian control no longer comes from the rational-prime exponent lattice. On a sufficiently rapidly decaying class, that objection can be removed exactly by Möbius inversion.

Given any target `Theta_*` as above, put

```text
g(t)=t^(-1/2) Theta_*(t)
```

and define

```text
h(t)=sum_{n>=1} mu(n) g(nt).
```

For the Gaussian-log control, the sum converges absolutely for every fixed `t>0`, and so does the double sum needed below. Then

```text
E h(t)
 = sum_{m>=1} sum_{n>=1} mu(n) g(m n t)
 = sum_{k>=1} g(k t) sum_{n|k} mu(n)
 = g(t).
```

Hence

```text
boxed:
Theta_*(t)=t^(1/2) E h(t).
```

Moreover,

```text
sum_m |h(mt)|
 <= sum_k d(k)|g(kt)|
 < infinity
```

for this control, so the expansion by prime exponents may be rearranged absolutely:

```text
E h
 = sum_{alpha in N_0^(P)} D^alpha h
 = product_p (sum_{j>=0} D_p^j) h.
```

Therefore **the ordinary rational-prime lattice and its exact one-sided prime generators do not select the Riemann kernel**. On this fast-decay class, the dilation sum has the classical Möbius inverse and can be made to produce a positive inversion-symmetric completed kernel whose Mellin zeros are off-axis.

The important scope limitation is that this tailored control seed `h` is not Hedenmalm's distinguished Hermite seed `h_00`. The result rules out rigidity from `E`, inversion symmetry, positivity, and the pencil alone; it does not rule out additional rigidity of the specific Jacobi/heat/Hermite seed.

## Where Hedenmalm places the actual Hilbert–Pólya gap

Hedenmalm does not claim that the differential pencil is already self-adjoint. He introduces the finite span of zero modes, including hypothetical off-real zero modes, and asks for sesquilinear forms satisfying

```text
<u,v>_1 = <L_phi u,L_phi v>_2
```

and the generalized self-adjointness identity

```text
<L_phi D_x u,L_phi v>_2
 = <L_phi u,L_phi D_x v>_2.
```

His Theorem 4.2.2 shows that if such a structure exists, then every non-real zero mode has zero `<.,.>_1` norm. If `<.,.>_2` is an honest Hilbert-space inner product, Corollary 4.2.3 then excludes those modes and forces every zero of `Xi` to be real, hence proves RH.

So the hierarchy is

```text
prime-lattice dilation sum                exact / classical
special theta completion                  exact / classical
Xi Mellin transform                       exact / classical
complex-zero differential pencil          theorem (Hedenmalm 2026)
positive self-adjoint pair metric          OPEN
RH                                         follows if that metric exists
```

The Gaussian control shows why the last step cannot be formal: its off-real zero modes imply that no analogous positive metric can satisfy the required self-adjointness on the full control zero-mode space.

## Relation to previous `prime_lattice` findings

This sharpens several earlier boundaries rather than replacing them.

- `PL-014` showed that the finite-prime valuation skeleton does not itself supply the functional equation; additive Fourier/Poisson and the archimedean place are essential. Hedenmalm gives an especially concrete realization of exactly that completion: a prime dilation sum acting on a special archimedean seed becomes an inversion-symmetric theta kernel.
- `PL-043` showed that ambient Fourier/Sonine/de Branges spectral geometry is too flexible unless one proves a zeta-specific positivity/Hermite–Biehler condition. The present matched control reaches the same conclusion for Hedenmalm's newer differential-pencil formulation.
- `PL-047` showed that the Herichi–Lapidus operator-valued Euler product is literal only in `Re(s)>1`, while the critical-strip operator is obtained by inserting meromorphic `zeta` into functional calculus. Hedenmalm's route is stronger on this point: the theta kernel is produced by an honest rapidly convergent real-variable dilation sum and its Mellin transform is entire. The negative result therefore cannot be blamed on an illicit continuation of the Euler product.

## Prior art and novelty audit

Primary current source:

- **Håkan Hedenmalm**, “Spectral interpretation of Riemann zeta zeros,” arXiv:2606.17494v1 [math.CA], submitted 16 June 2026. In particular: §2.1 for the dilation-sum operator and its prime factorization; §2.2 for the Mellin representation of `Xi`; Theorems 3.3.1 and 3.3.3 for the real/complex boundary-value characterization; Definition 4.2.1, Theorem 4.2.2 and Corollary 4.2.3 for the conditional self-adjoint-pair route to RH.

The inversion

```text
G(t)=sum_n F(nt)
<=>
F(t)=sum_n mu(n)G(nt)
```

under absolute-convergence hypotheses is classical Möbius inversion. Its use here is only as an adversarial matched control showing that the fixed rational-prime dilation sum is too flexible if the seed is unconstrained.

The general problem of deciding which positive even rapidly decaying kernels have Fourier transforms with only real zeros is also classical (Pólya/Lee–Yang theory). The explicit three-Gaussian control above is elementary and is not presented as a new theorem.

Accordingly, the durable contribution of this finding is a **no-go audit and target refinement**, not a novelty claim about the underlying transforms or operators.

## Decisive audit test and surviving target

Any proposed proof using Hedenmalm's architecture should be tested by asking which step fails for the explicit `Theta_*` control above.

If the proof uses only

```text
ordinary rational-prime dilation generators,
unique factorization / Möbius inversion,
positivity of the completed kernel,
inversion symmetry t <-> 1/t,
rapid endpoint decay,
Mellin/Fourier duality,
or existence of the second-order eigenvalue pencil,
```

then it also applies to the control and cannot force reality of the eigenparameters.

A surviving argument must use an additional property of the **distinguished theta/Hermite seed** that the control lacks and must turn that property into the positive self-adjoint metric (or an equivalent coercive/positivity statement). Candidates include genuinely Jacobi/heat/Appell structure, a nontrivial sign/convexity identity for the theta logarithm, or another arithmetic-archimedean constraint strong enough to prohibit the control deformation.

Until such a theorem is supplied, Hedenmalm's construction should be treated as an important completed prime-lattice spectralization and a sharply formulated Hilbert–Pólya program, but not as a mechanism that already explains why `Re(s)=1/2` is forced.