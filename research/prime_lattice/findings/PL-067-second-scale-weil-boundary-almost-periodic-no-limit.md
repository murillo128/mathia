# PL-067 — The critical second Weil-boundary amplitude is an almost-periodic zero signal, not a limit

## Claim

The fixed-smooth escape left implicit by `PL-052` and explicitly outside the scope of `PL-066` can be closed at the most obvious second amplitude scale.

Fix `R>0`. Let `W_(L,R)^(+-)` denote the left-to-right cross-end block of the naturally `exp(-L)`-normalized **completed** Weil boundary form used in `PL-059`--`PL-066`, after the zeta pole has canonically canceled the universal PNT rank-one mode. For

```text
f,g in C_c^infinity(0,R),
```

define

```text
A_f(z)=integral_0^R f(a) exp(-z a) da,
A_g(z)=integral_0^R g(a) exp(-z a) da.
```

Then the exact zero expansion of `PL-063`, together with the endpoint expansion of the pole and archimedean terms in `PL-059`, gives

```text
boxed:
exp(L) <g,W_(L,R)^(+-) f>

 = sum_rho
     exp(2L(rho-1/2))
     A_f(rho-1/2)
     conjugate(A_g(conjugate(rho)-1/2))
   + O_(f,g,R)(exp(-L)).
```

The sum is over nontrivial zeta zeros with multiplicity. No Euler product is used here; this is the already-continued completed explicit formula evaluated on fixed smooth boundary probes.

Consequently, **under RH** the second-scaled cross coefficient has the asymptotic form

```text
boxed:
exp(L) <g,W_(L,R)^(+-) f>
 = F_(f,g)(L)+o(1),
```

where

```text
F_(f,g)(L)
 = sum_(rho=1/2+i gamma)
     c_rho(f,g) exp(2 i gamma L),

c_rho(f,g)
 = A_f(i gamma) conjugate(A_g(-i gamma)).
```

For fixed smooth `f,g` this Fourier series converges absolutely and uniformly, so `F_(f,g)` is a Bohr uniformly almost-periodic function. There exist fixed smooth probes for which at least one coefficient `c_rho(f,g)` is nonzero; for every such pair `F_(f,g)` is nonconstant and therefore has **no finite limit as `L->infinity`**.

Thus even assuming RH, the direct second amplitude

```text
exp(L) times the already-centered completed boundary residual
```

does not stabilize on fixed smooth cross-end probes. It resolves into persistent almost-periodic oscillations whose frequencies are exactly the zeta-zero ordinates already present in the classical explicit formula.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
canonical pole/PNT centering
+ fixed boundary depth
+ fixed smooth cross-end probes
+ second amplitude exp(L)
    -> convergent nontrivial boundary form/operator limit
    -> new RH rigidity.
```

This does not rule out moving test spaces, a different amplitude/topology, averaging or hull constructions, or a genuinely new rational-prime coupling. It does show that the simplest second-order smooth limit is not merely hard to prove: **under RH it generically does not exist**.

## Why `exp(L)` is the critical second amplitude

Put

```text
X=exp(2L).
```

For the centered prime cross block

```text
D_(L,R)=H_(mu_(L,R))-P_R,
```

`PL-063` gives, for fixed smooth probes,

```text
<g,D_(L,R)f>
 = - sum_rho
       X^(rho-1)
       A_f(rho-1/2)
       conjugate(A_g(conjugate(rho)-1/2))
   + O_(f,g,R)(X^(-3)).
```

A zero `rho=beta+i gamma` therefore appears with amplitude

```text
X^(beta-1)=exp(-2L(1-beta)).
```

The factor `exp(L)=X^(1/2)` is exactly the next scalar scale at which a critical-line zero has order-one size:

```text
X^(1/2) X^(rho-1)
 = X^(rho-1/2)
 = exp(2L(rho-1/2)).
```

Hence on RH the critical-line divisor stops decaying and becomes pure phase. This amplitude is not being claimed as a new geometrically forced normalization; it is the direct second scale suggested by the zero expansion and was deliberately left outside `PL-066`.

## Completion does not add another order-one cross term at this scale

The point of using the **cross-end block** is that the remaining completion terms can be audited exactly rather than hidden in the coarser full-form bound.

`PL-059` writes the normalized pole quadratic form as

```text
2 Re(G_- conjugate(F_-))

+ 2 exp(-L)
    Re(F_+ conjugate(F_-)+G_- conjugate(G_+))

+ 2 exp(-2L)
    Re(F_+ conjugate(G_+)).
```

The first line is precisely the PNT rank-one cross block `P_R`. The `exp(-L)` line is **same-end/diagonal**. Therefore the error of the pole cross block relative to `P_R` is only

```text
O_(f,g,R)(exp(-2L))
```

at the first normalized scale, and becomes `O(exp(-L))` after multiplication by the second amplitude `exp(L)`.

The scalar completion term has no left-right matrix coefficient. The archimedean cross-end kernel is already `O_(f,g,R)(exp(-L))` before the first boundary normalization because the two endpoints are separated by `2L+O_R(1)`; after first normalization and then multiplication by `exp(L)` it is again `O(exp(-L))`.

Finally,

```text
W_(L,R)^(+-)
 = -D_(L,R)
   + O_(f,g,R)(exp(-2L))
```

in fixed smooth cross matrix coefficients. Multiplying the `PL-063` formula by `exp(L)=X^(1/2)` therefore gives the claimed completed formula, with the trivial-zero error even smaller:

```text
X^(1/2) O(X^(-3))=O(X^(-5/2)).
```

This sign and scaling audit is important: the order-one second-scale zero signal is not an artifact of dropping the pole or the archimedean place.

## Under RH the smooth zero series is uniformly almost periodic

Assume RH, so every nontrivial zero has

```text
rho=1/2+i gamma.
```

For every integer `M>=0`, integration by parts on a compactly supported smooth probe gives

```text
|A_f(i gamma)| <= C_(f,M) (1+|gamma|)^(-M),
|A_g(i gamma)| <= C_(g,M) (1+|gamma|)^(-M).
```

The classical Riemann--von Mangoldt estimate implies that the number of zeros, with multiplicity, in a unit-height interval is `O(log(2+|gamma|))`. Therefore

```text
sum_rho |c_rho(f,g)| < infinity.
```

The series

```text
F_(f,g)(L)=sum_rho c_rho(f,g) exp(2 i gamma L)
```

thus converges absolutely and uniformly for all real `L`. It is consequently a Bohr uniformly almost-periodic function, with Bohr frequencies contained in the doubled zero ordinates `{2 gamma}`.

This is stronger regularity than the mean-square/Stepanov almost periodicity that occurs for unsmoothed normalized prime-number-theorem error terms, but the strengthening comes only from the rapid Fourier decay of the **fixed smooth test functions**. It does not introduce a new arithmetic mechanism.

## Nontrivial fixed probes force nonconvergence

The almost-periodic function need not be nonzero for every specially chosen pair of probes, so the no-limit statement should not be over-quantified. What is needed for the route obstruction is existence of ordinary fixed probes with a nonzero zero coefficient.

Choose any nontrivial zero

```text
rho_0=1/2+i gamma_0.
```

For fixed `gamma_0`, the map

```text
f -> A_f(i gamma_0)
```

is a nonzero continuous linear functional on `C_c^infinity(0,R)`. Hence one can choose `f` with `A_f(i gamma_0) != 0`, and independently choose `g` with `A_g(-i gamma_0) != 0`. The Fourier coefficient at frequency `2 gamma_0` is then nonzero (with the zero multiplicity multiplying the same coefficient), so `F_(f,g)` is nonconstant.

A uniformly almost-periodic function that has a finite limit as `L->+infinity` must be constant. Indeed, for every `epsilon>0` its `epsilon`-almost-periods are relatively dense. For a fixed `L_0`, choose an arbitrarily large almost-period `tau`; then `L_0+tau` lies in the convergence tail while

```text
|F(L_0+tau)-F(L_0)|<epsilon.
```

Letting the tail approach its putative limit shows `F(L_0)` equals that limit for every `L_0`.

Therefore, for the probes above,

```text
F_(f,g) nonconstant
    => F_(f,g)(L) has no limit as L->infinity
    => exp(L)<g,W_(L,R)^(+-)f> has no limit.
```

The `o(1)` completed-Weil remainder cannot repair this failure.

## Off-line zeros appear as growth exponents, but no converse is claimed

Without RH, each individual zero contributes

```text
exp(2L(beta-1/2)) exp(2 i gamma L).
```

Thus the horizontal displacement `beta-1/2` becomes a real exponential growth/decay exponent in the second-scale signal. This is the exact boundary-coordinate version of the mode dictionary already noted in `PL-052`.

No global statement such as “boundedness of one fixed coefficient is equivalent to RH” is inferred. Different zeros can interact, a chosen probe can annihilate individual coefficients, and there need not be a rightmost zero. `PL-066` remains the audited inverse theorem for controlled moving bands. The present finding uses only the RH direction needed to kill the proposed **convergent** second-scale limit.

## Prior-art and novelty audit

The ingredients are classical even though the completed boundary specialization is line-specific.

- Weil's explicit formula and Bombieri's treatment of the Weil quadratic functional, already recorded as `SOURCES.md` entries 25--26, are the analytic-continuation foundation. The zero divisor is not produced by a new operator.
- Jerzy Kaczorowski and Olivier Ramaré, “Almost periodicity of some error terms in prime number theory,” *Acta Arithmetica* **106** (2003), 277--297, DOI `10.4064/aa106-3-6`, prove under GRH that a broad normalized Selberg-class explicit-formula error function is almost periodic in the Stepanov `L^2` sense. This is close conceptual prior art for the critical-line zero phases becoming recurrent oscillations.
- Amir Akbary, Nathan Ng, Majid Shahabi, “Limiting distributions of the classical error terms of prime number theory,” *Quarterly Journal of Mathematics* **65** (2014), 743--780, DOI `10.1093/qmath/hat059`, develops the broader `B^p`-almost-periodic/limiting-distribution framework for explicit-formula error terms.

Accordingly, no novelty is claimed for “zeros on the critical line produce almost-periodic prime-error oscillations.” The durable contribution here is the exact **negative specialization to the already-completed `prime_lattice` boundary family**: after the pole/PNT cancellation, the first fixed-smooth amplitude at which critical zeros survive is not a new limiting operator but a uniformly almost-periodic explicit-formula signal, and it generically fails to converge even if RH is true.

A targeted literature search across Guinand-style explicit formulas, normalized PNT error terms, almost-periodic prime-number-theory errors, and limiting distributions found the classical almost-periodicity mechanism above, not an independent boundary operator whose convergence would add RH rigidity.

## Analytic-continuation and matched-control audit

No identity from the Euler-product half-plane is continued formally. The shell sum at finite `L` is finite, and the passage to the zero expansion is the completed von-Mangoldt/Weil explicit formula already audited in `PL-052`, `PL-059`, and `PL-063`. The second scaling is applied only after that exact continued identity is established.

The almost-periodicity mechanism is also not specific to the rational-prime exponent lattice. Any explicit-formula system with a symmetry-line zero divisor, comparable zero counting, and fixed smooth compact probes produces the same absolutely convergent phase expansion. Matched Beurling or other generalized-prime systems can therefore reproduce the **form** of this second-scale behavior whenever their zero geometry is matched. Rational-prime discrimination would have to enter through additional structure, not through almost periodicity of the already-resolved zero sum.

## Falsification and boundary tests

The claim reduces to six auditable points:

1. `PL-063` has the centered cross-prime sign `D_L=-sum_rho X^(rho-1)(...) + error`;
2. `PL-059` gives `completed_cross=-D_L+O(exp(-2L))` at the first normalized scale, because the `exp(-L)` pole corrections are diagonal;
3. the archimedean cross-end contribution is `O(exp(-L))` before first normalization and hence `O(exp(-L))` after the second-scale conversion;
4. under RH, multiplication by `X^(1/2)` turns every zero factor into the pure phase `exp(2 i gamma L)`;
5. compact smooth probes give rapid vertical decay, and standard zero counting makes the resulting Fourier series absolutely/uniformly convergent;
6. a nonzero Fourier coefficient makes the Bohr almost-periodic function nonconstant, and a nonconstant Bohr almost-periodic function cannot converge at `+infinity`.

Failure of points 1--3 would invalidate the completed-Weil formula. Failure of RH removes the pure-phase conclusion but not the exact termwise growth dictionary. The theorem says nothing about a moving probe family whose regularity weakens with `L`, averaging over `L`, a translation-hull invariant, or a different topology in which the almost-periodic orbit itself rather than a pointwise limit is the object.

## Consequence for the mesoscopic clue

This closes one of the explicit survivors left by `PL-066`: merely multiplying the canonically centered fixed-depth boundary residual by `exp(L)` and keeping the probes fixed and smooth does **not** reveal a stable critical-line limit. On RH it reveals the already-known zero frequencies as a recurrent almost-periodic orbit.

The accepted mesoscopic clue therefore remains meaningful only beyond this direct fixed-smooth second amplitude: a surviving construction must use a moving topology/regularity scale, a genuinely different normalization justified independently of the zero expansion, a nontrivial hull/relative invariant with additional arithmetic content, or another rational-prime-specific coupling. Simply replacing first-scale collapse by the next scalar amplitude does not create the missing rigidity.
