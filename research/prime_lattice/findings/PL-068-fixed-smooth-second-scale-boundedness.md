# PL-068 — Fixed-smooth second-scale boundedness is RH-equivalent, but regular scalar renormalizations do not converge

## Claim

Fix `R>0`, and let `W_(L,R)^(+-)` be the left-to-right cross-end block of the naturally `exp(-L)`-normalized **completed** Weil boundary form from `PL-059`--`PL-067`, after the zeta pole has canonically canceled the universal PNT rank-one mode. For fixed

```text
f,g in C_c^infinity(0,R),
```

set

```text
T_(f,g)(L)
  = exp(L) <g,W_(L,R)^(+-) f>.
```

`PL-067` gives the exact continued zero expansion

```text
T_(f,g)(L)
 = sum_rho c_rho(f,g) exp(lambda_rho L)
   + O_(f,g,R)(exp(-L)),

lambda_rho = 2(rho-1/2),

c_rho(f,g)
 = A_f(rho-1/2)
   conjugate(A_g(conjugate(rho)-1/2)),

A_f(z)=integral_0^R f(a) exp(-z a) da.
```

The sum is over nontrivial zeros with multiplicity. No Euler-product identity is continued into the strip; this is the already-audited completed explicit formula.

There exist fixed smooth probe pairs `(f,g)` for which

```text
c_rho(f,g) != 0
```

for **every** nontrivial zeta zero `rho`. In fact such pairs form a residual set in any fixed nontrivial Frechet test core `C_K^infinity x C_K^infinity`, with `K` compactly contained in `(0,R)` and with nonempty interior.

For every such pair,

```text
boxed:
RH
  <=>
T_(f,g)(L) is bounded for L -> +infinity.
```

Under RH, the stronger description from `PL-067` holds:

```text
T_(f,g)(L)=F_(f,g)(L)+o(1),

F_(f,g)(L)
 = sum_(rho=1/2+i gamma)
     c_rho(f,g) exp(2 i gamma L),
```

where `F_(f,g)` is a nonconstant Bohr uniformly almost-periodic function for the residual probe pairs above. Hence the RH-equivalent second-scale signal is **bounded but generically nonconvergent**.

There is also a complete trichotomy for every positive scalar normalization `a(L)` whose ratio to the critical second amplitude has an extended limit

```text
r(L)=a(L) exp(-L)
   -> r_infinity in [0,+infinity].
```

Assuming RH:

```text
r_infinity=0
    -> a(L)<g,W_(L,R)^(+-)f> -> 0
       for every fixed smooth pair;

0<r_infinity<infinity
    -> for residual fixed smooth pairs the coefficient has no limit;

r_infinity=+infinity
    -> for residual fixed smooth pairs the coefficient is unbounded
       along a sequence L_j -> infinity.
```

Therefore no such **regular scalar renormalization** produces a nonzero finite pointwise sesquilinear-form limit on the full fixed-smooth cross-end core. The only distinguished scalar scale is `exp(L)`, and at that scale the natural object is a bounded recurrent zero signal rather than a limiting operator.

**Evidence/status:** `EXACT-DERIVED + CLASSICALIZED-MECHANISM + NEGATIVE/OBSTRUCTION`. The boundedness equivalence is a precise positive criterion inside the line-specific completed boundary coordinates, but analytically it is an explicit-formula/Laplace-pole detection principle rather than new RH rigidity. It is `DECISIVE-NEGATIVE` for the route

```text
fixed boundary depth
+ fixed smooth probes
+ scalar amplitude renormalization with a(L) exp(-L) -> extended limit
    -> nonzero finite boundary-form limit
    -> new spectral rigidity.
```

## Generic fixed probes do not annihilate any zero

Fix a compact interval

```text
K subset (0,R)
```

with nonempty interior, and work in the Frechet space `C_K^infinity` of smooth functions supported in `K`.

For each nontrivial zero `rho`, define the continuous linear functional

```text
ell_rho(f)
 = A_f(rho-1/2)
 = integral_K f(a) exp(-(rho-1/2)a) da.
```

This functional is not identically zero. Indeed, the exponential factor never vanishes, and a sufficiently localized smooth bump gives a nonzero integral. Hence

```text
ker(ell_rho)
```

is a proper closed hyperplane and therefore nowhere dense in `C_K^infinity`.

The nontrivial zeta zeros form a countable set. By the Baire category theorem,

```text
G
 = intersection_rho {f : ell_rho(f) != 0}
```

is residual and dense in `C_K^infinity`. Apply the same argument to the countable family

```text
g -> A_g(conjugate(rho)-1/2).
```

Thus there is a residual set of pairs `(f,g)` for which every coefficient `c_rho(f,g)` is nonzero.

This genericity statement is only a non-annihilation device. It does **not** make the probes canonical, constructive, or arithmetically distinguished.

## Boundedness forces the absence of zeros to the right of the critical line

Assume that one of the non-annihilating pairs above satisfies

```text
|T_(f,g)(L)| <= C
```

for all sufficiently large `L`. Choose `L_0` beyond that threshold and define its one-sided Laplace transform

```text
H(s)
 = integral_(L_0)^infinity
     exp(-s L) T_(f,g)(L) dL.
```

Boundedness makes `H` holomorphic in

```text
Re(s)>0.
```

Write the `PL-067` remainder as `E(L)=O(exp(-L))`. Then

```text
E_hat(s)
 = integral_(L_0)^infinity exp(-sL) E(L) dL
```

is holomorphic for `Re(s)>-1`.

For `Re(s)>1`, absolute convergence permits termwise integration of the zero expansion, giving

```text
H(s)-E_hat(s)
 = sum_rho
     c_rho(f,g)
     exp(-(s-lambda_rho)L_0)
     /(s-lambda_rho).
```

For fixed smooth probes, repeated integration by parts gives, for every `M`,

```text
|c_rho(f,g)|
 <= C_(f,g,M) (1+|Im rho|)^(-M).
```

Together with the classical zero-counting bound

```text
N(T+1)-N(T)=O(log(2+T)),
```

this implies that the displayed partial-fraction series converges locally uniformly away from its poles. It therefore defines a meromorphic function of `s`, with a pole at

```text
s=lambda_rho=2(rho-1/2)
```

whenever the corresponding total residue is nonzero. Repeated copies of the same zero merely multiply the same nonzero coefficient by its multiplicity.

But on `Re(s)>1` this meromorphic function agrees with the holomorphic function `H-E_hat`. By analytic continuation, it must be holomorphic throughout `Re(s)>0`. Consequently it can have no pole there.

For the non-annihilating probe pair this excludes every zero with

```text
Re(lambda_rho)>0
    <=>
Re(rho)>1/2.
```

The functional equation maps every hypothetical zero with `Re(rho)<1/2` to a zero with real part `>1/2`. Hence no nontrivial zero can lie off the critical line, and RH follows.

This argument does not need a rightmost zero, does not compare competing exponential terms directly, and does not assume simplicity. The Laplace transform separates the exponential modes as poles.

## RH gives boundedness and almost-periodic recurrence

Conversely assume RH. Then every exponent is purely imaginary:

```text
lambda_rho=2 i gamma.
```

`PL-067` proves that the zero series is absolutely and uniformly convergent for fixed smooth probes, so

```text
F_(f,g)(L)
 = sum_rho c_rho(f,g) exp(2 i gamma L)
```

is Bohr uniformly almost periodic and bounded. Since the completed remainder is `O(exp(-L))`, `T_(f,g)` is bounded as well.

For the residual non-annihilating pairs, at least one nonzero-frequency Fourier coefficient is present, indeed all are. Therefore `F_(f,g)` is nonconstant. A nonconstant Bohr almost-periodic function cannot have a finite limit at `+infinity`: relatively dense almost-periods return arbitrarily late values arbitrarily close to any fixed earlier value. Thus

```text
RH
  -> T_(f,g) bounded
  but T_(f,g) has no limit
```

for the generic fixed probe pairs relevant to the criterion.

The distinction matters. The second amplitude contains exact RH information through **boundedness of the orbit**, but not through convergence to a static spectral object.

## Regular scalar amplitudes have only three outcomes

Return to the first-scale cross coefficient

```text
C_(f,g)(L)
 = <g,W_(L,R)^(+-)f>
 = exp(-L) T_(f,g)(L).
```

Let `a(L)>0` and assume

```text
r(L)=a(L) exp(-L)
```

has an extended limit. Then

```text
a(L) C_(f,g)(L)
 = r(L) T_(f,g)(L).
```

Under RH, write `T=F+o(1)`.

### Subcritical scalar amplitude

If

```text
r(L)->0,
```

boundedness of `F` gives

```text
a(L) C_(f,g)(L)->0
```

for every fixed smooth pair. Thus every regular amplitude smaller than `exp(L)` still collapses.

### Critical-comparable scalar amplitude

If

```text
r(L)->c,
0<c<infinity,
```

and a generic coefficient had a finite limit, division by `r(L)` would force `F(L)+o(1)` to have a finite limit. This contradicts nonconstancy of the almost-periodic `F`. Hence every amplitude asymptotic to a positive multiple of `exp(L)` inherits the `PL-067` nonconvergence.

### Supercritical scalar amplitude

If

```text
r(L)->+infinity,
```

choose a generic pair and a point `L_*` with

```text
|F(L_*)|=delta>0.
```

Uniform almost periodicity supplies arbitrarily large positive almost-periods `tau_j` such that

```text
|F(L_*+tau_j)-F(L_*)|<delta/4.
```

For large `j`, the `o(1)` remainder is also smaller than `delta/4`, so

```text
|T(L_*+tau_j)| >= delta/2.
```

Since `r(L_*+tau_j)->infinity`, the scalar-renormalized coefficient is unbounded along this subsequence.

This includes the elementary exponential hierarchy

```text
a(L)=exp(alpha L):

alpha<1  -> zero,
alpha=1  -> bounded almost-periodic nonconvergence,
alpha>1  -> generic subsequential blow-up,
```

and the same trichotomy around `exp(L)` for polynomial or logarithmic corrections whose ratio has a limit.

## Prior-art and novelty audit

The new statement is not presented as a new independent RH criterion in the classical analytic-number-theory sense.

The ingredients are already standard or persisted:

- the completed Weil explicit formula and zero expansion are the analytic-continuation input already audited in `PL-052`, `PL-059`, `PL-063`, and `PL-067`;
- `PL-067` already identifies the RH-side critical second amplitude as a uniformly almost-periodic zero-frequency signal;
- detecting a right-half-plane exponential mode by a pole of a Laplace/Mellin transform is a classical transform-singularity/oscillation principle in prime-number-theorem error analysis;
- classical work on almost-periodic prime error terms and limiting distributions already shows that critical-line zero phases naturally produce recurrent rather than convergent normalized errors.

A targeted literature audit around Landau/Ingham-style oscillation arguments, smoothed explicit formulas, and almost-periodic prime error terms found the general mechanism above, not a separate theorem asserting that this particular **completed prime-lattice boundary coefficient** supplies new arithmetic rigidity. The durable content is therefore the exact line-specific specialization and the resulting no-go for regular scalar boundary limits.

No novelty is claimed for the principle

```text
transform singularity to the right of the boundary
    -> normalized error cannot remain bounded,
```

nor for critical-line zeros producing almost-periodic oscillation.

## Analytic-continuation and control audit

Nothing in the converse uses the Euler product in the critical strip. The finite prime-shell boundary object is first related to the completed explicit formula by the already-audited continuation in `PL-063` and `PL-067`; only then is the Laplace transform in the external localization variable `L` taken.

The criterion also does not by itself distinguish rational primes from another explicit-formula system with the same zero divisor. If a matched generalized-prime system has the same continued divisor and the same smooth boundary expansion, the same pole-detection argument applies. Thus the criterion is **zero-sensitive but not rational-prime-rigid**.

This is precisely why the result does not solve the line's main objective. It identifies the correct dynamical category of the existing zero-resolved signal, but the zeros have already entered through the classical completed formula.

## Falsification and boundary tests

The claim has seven sharp failure points:

1. the `PL-067` completed cross-end expansion must have the stated exponent `lambda_rho=2(rho-1/2)` and an exponentially decaying remainder;
2. fixed smooth Laplace transforms must have rapid vertical decay sufficient for local uniform convergence of the pole series;
3. boundedness of `T` must give a holomorphic one-sided Laplace transform on `Re(s)>0`;
4. termwise integration must be valid initially in a common right half-plane such as `Re(s)>1`;
5. the Baire argument must supply probes with nonzero residue at every zero under consideration;
6. the zeta functional equation must convert exclusion of `Re(rho)>1/2` into RH;
7. the scalar trichotomy assumes the positive ratio `a(L)exp(-L)` has an extended limit and does not cover an arbitrarily oscillatory, probe-dependent, or zero-dependent demodulation.

The result makes no operator-norm boundedness claim, no effective estimate for how large `L` must be, and no claim that the residual generic probe pair is canonical or computable without zero information. A deliberately oscillatory scalar multiplier could try to demodulate one chosen coefficient, but such a construction would need an independent geometric justification and must work simultaneously on the whole form core; inserting zero phases by hand would merely re-encode the explicit formula.

## Consequence for the mesoscopic boundary search

`PL-067` left open the possibility that a different scalar amplitude might convert the fixed-smooth second-scale orbit into a useful limit. The regular scalar class above is now exhausted:

```text
smaller than exp(L)  -> collapse,
comparable to exp(L) -> recurrent nonconvergence,
larger than exp(L)   -> generic subsequential blow-up.
```

At the same time, the critical amplitude `exp(L)` has a precise meaning: for generic fixed probes, **boundedness itself is equivalent to RH**. This is mathematically sharper than a mere no-limit statement, but it is still classical explicit-formula information rather than the missing geometric cause of RH.

The accepted mesoscopic clue therefore survives only through a genuine change of information geometry: moving probe spaces or regularity, a non-scalar relative topology, an orbit/hull invariant with additional arithmetic structure, a growing-depth/frequency coupling not conjugate to `PL-058`, or another rational-prime-specific observable. Merely choosing another regular scalar amplitude on the same fixed smooth boundary coefficients is no longer a live route.
