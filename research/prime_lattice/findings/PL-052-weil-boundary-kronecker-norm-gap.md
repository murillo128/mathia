# PL-052 — Prime-log recurrence prevents norm convergence of the universal Weil boundary model

## Claim

`PL-051` proves that, after the natural `exp(-L)` normalization and a fixed-depth blow-up of the two endpoints of the localized Weil window, the non-archimedean operator converges **strongly** to a universal rank-one Hankel model. That convergence is genuinely topology-sensitive: for every fixed boundary depth `R>0`, it is **not** operator-norm convergence.

Using the notation of `PL-051`, let

```text
B_(L,R)
 = exp(-L) J_(L,R)^* K_L J_(L,R)
```

on

```text
H_R direct_sum H_R,
H_R=L^2(0,R),
```

and let

```text
B_R = [ 0    P_R ]
      [ P_R  0   ],

P_R=|h_R><h_R|,
h_R(a)=exp(-a/2).
```

Then `PL-051` gives

```text
B_(L,R) -> B_R strongly.
```

Nevertheless,

```text
boxed:
liminf_(L->infinity) ||B_(L,R)-B_R||
 >= 1-exp(-R) > 0.
```

The lower bound is produced by boundary profiles whose modulus is the PNT-selected eigenprofile `h_R` but whose phases oscillate faster and faster. For each finite `L`, Kronecker recurrence of the finitely many active rational-prime logarithms makes those oscillations align the entire atomic outer-shell measure, while the absolutely continuous PNT limit is killed by the Riemann--Lebesgue lemma.

Thus the same prime-log recurrence that blocks pointwise cancellation in `PL-045` also blocks norm convergence of the boundary homogenization in `PL-051`.

A direct consequence is that the most naive second-order centered operator scale cannot exist in norm:

```text
|| exp(L) (B_(L,R)-B_R) ||
 >= (1-exp(-R)+o(1)) exp(L).
```

There is, however, a weaker smooth-test scale. If one centers the outer-shell von-Mangoldt distribution against a fixed smooth deficit test, the classical explicit formula gives an exact zero-mode expansion. In that weak topology each nontrivial zero `rho` contributes a separable boundary Hankel mode with `L`-dependence

```text
exp((2 rho-1)L).
```

On the critical line these factors are pure phases; off the line they are exponentially growing or decaying mode-by-mode. This is a useful dictionary, but it is **the classical explicit formula in boundary coordinates**, not a new Hilbert--Polya operator.

Accordingly, the centered-boundary escape left open by `PL-051` splits sharply:

```text
raw L^2 operator topology
    -> prime-log high-frequency recurrence survives
    -> no norm convergence, no bounded exp(L)-centered operator;

fixed smooth probes
    -> high-frequency atomic structure is suppressed
    -> classical explicit formula exposes the zeta zero divisor.
```

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
PNT-center the fixed-depth boundary operator
+ take a bounded/operator-norm second-order limit
    -> obtain a new zeta-zero spectral operator.
```

The Kronecker ingredient is classical and already anchored by `PL-045`; the fixed-depth boundary model is `PL-051`; the smooth zero expansion is an exact specialization of the classical von Mangoldt / Weil explicit formula. No novelty claim is made for those ingredients or for generic strong-versus-norm convergence phenomena.

## Boundary-shell operator recalled

For fixed `R>0`, define the normalized outer-shell measure

```text
mu_(L,R)
 = exp(-L)
   sum_(2L-2R<log n<2L)
     Lambda(n)/sqrt(n)
     delta_(2L-log n).
```

`PL-051` proves weak convergence

```text
mu_(L,R) -> mu_R,

d mu_R(delta)
 = exp(-delta/2) 1_[0,2R](delta) d delta.
```

The cross-end block of `B_(L,R)` is the Hankel-type operator

```text
(H_(mu_(L,R)) f)(b)
 = integral f(delta-b) d mu_(L,R)(delta),
```

where `f` is extended by zero outside `(0,R)`. The limiting cross block is

```text
H_(mu_R)=P_R,

(P_R f)(b)
 = exp(-b/2)
   integral_0^R exp(-a/2) f(a) da.
```

The same-end blocks come only from fixed small lags `log n<R` and have norm `O_R(exp(-L))`; they are irrelevant for the norm lower bound below because a cross-block compression already supplies it.

## Oscillatory boundary profiles recover the atomic shell

Let

```text
N_R = ||h_R||_2^2 = 1-exp(-R),
```

and for a real frequency `xi` define two unit vectors in `H_R` by

```text
f_xi(a)
 = N_R^(-1/2) exp(+i xi a) exp(-a/2),

g_xi(b)
 = N_R^(-1/2) exp(-i xi b) exp(-b/2).
```

For a single shell atom at deficit `delta`, the corresponding truncated reflection gives

```text
<g_xi,H_delta f_xi>
 = exp(i xi delta)
   exp(-delta/2) tau_R(delta) / N_R,
```

where

```text
tau_R(delta)
 = delta,       0<=delta<=R,
 = 2R-delta,   R<=delta<=2R.
```

The phase is independent of the integration coordinate because the opposite modulations of `f_xi` and `g_xi` cancel there. Hence

```text
<g_xi,H_(mu_(L,R)) f_xi>
 = integral exp(i xi delta)
     exp(-delta/2) tau_R(delta)/N_R
     d mu_(L,R)(delta).
```

Every atom of `mu_(L,R)` has

```text
delta_n=2L-log n,
n=p^k,
```

because `Lambda` is supported on prime powers. For the finite set of underlying primes active at fixed `L`, unique factorization makes their logarithms rationally independent. Kronecker recurrence therefore gives arbitrarily large `xi` such that

```text
exp(-i xi log p) -> 1
```

simultaneously for every active prime. Since only finitely many powers occur, this also gives

```text
exp(i xi delta_n)
 = exp(i 2L xi) exp(-i xi log n)
 -> exp(i 2L xi)
```

simultaneously for all shell atoms.

All non-phase factors in the atomic sum are nonnegative. Consequently, for every fixed `L`, taking a recurrent sequence `xi_j->infinity` yields

```text
lim_j
|<g_(xi_j),H_(mu_(L,R)) f_(xi_j)>|

 = integral
     exp(-delta/2) tau_R(delta)/N_R
     d mu_(L,R)(delta).
```

## The continuum rank-one limit disappears at the same frequencies

For the rank-one limit,

```text
<g_xi,P_R f_xi>

 = N_R^(-1)
   [ integral_0^R exp(-a) exp(i xi a) da ]^2.
```

The integral tends to zero as `|xi|->infinity`; this is the elementary Riemann--Lebesgue effect for the absolutely continuous boundary profile.

Therefore the recurrent frequencies can simultaneously make the atomic shell nearly fully coherent and make the continuum model arbitrarily small. Since operator norm dominates every unit-vector matrix element,

```text
||H_(mu_(L,R))-P_R||

 >= integral
      exp(-delta/2) tau_R(delta)/N_R
      d mu_(L,R)(delta).
```

The cross block is a compression of `B_(L,R)-B_R`, hence

```text
||B_(L,R)-B_R||
 >= ||H_(mu_(L,R))-P_R||.
```

Now use the fixed-width PNT shell convergence from `PL-049`--`PL-051`. The right-hand side tends to

```text
N_R^(-1)
 integral_0^(2R)
   tau_R(delta) exp(-delta) d delta.
```

The integral factors through the convolution of `h_R`:

```text
integral_0^(2R)
  tau_R(delta) exp(-delta) d delta

 = [ integral_0^R exp(-a) da ]^2
 = (1-exp(-R))^2.
```

Dividing by `N_R=1-exp(-R)` proves

```text
boxed:
liminf_(L->infinity) ||B_(L,R)-B_R||
 >= 1-exp(-R).
```

This lower bound is exactly the magnitude of the nonzero eigenvalue of the first-order rank-one boundary model. In particular, taking `R` moderately large makes the norm gap arbitrarily close to `1`, even though every fixed vector sees strong convergence to `B_R`.

## Why strong convergence still holds

There is no contradiction with `PL-051`. The vectors used above are not fixed as `L` grows. For each `L`, the Kronecker recurrence may require a new and very large frequency `xi_L`; the modulated profiles then converge weakly to zero along any sequence with `|xi_L|->infinity`.

Thus there are now two distinct escape mechanisms in the localized prime operator:

```text
PL-050:
    global dilation to (-1,1)
    -> spatial mass escapes into shrinking endpoint layers;

PL-052:
    fixed endpoint blow-up
    -> spatial boundary layer is retained,
       but norm-defect states escape to arbitrarily high boundary frequency.
```

The first-order PNT model is therefore correct for every fixed boundary profile but is not a uniform spectral approximation over the unit sphere of `L^2(0,R)`.

## Smooth centering recovers the classical zero divisor

The norm obstruction does not prevent a weaker distributional second scale. Let

```text
phi in C_c^infinity(0,2R)
```

and define the **raw centered shell probe**

```text
C_L(phi)
 = sum_n Lambda(n)n^(-1/2)
       phi(2L-log n)

   - exp(L)
     integral_0^(2R)
       exp(-delta/2) phi(delta) d delta.
```

Only the shell `2L-2R<log n<2L` contributes. Apply the classical von Mangoldt explicit formula in distribution form

```text
d psi(x)
 = dx
   - sum_rho x^(rho-1) dx
   - dx/[x(x^2-1)],
```

where `rho` runs over the nontrivial zeros, and test it against

```text
w_L(x)
 = x^(-1/2) phi(2L-log x).
```

The support stays away from `x=1` for large `L`. With

```text
Phi_phi(z)
 = integral_0^(2R) phi(delta) exp(-z delta) d delta,
```

the change of variables `x=exp(2L-delta)` gives exactly

```text
boxed:
C_L(phi)
 = - sum_rho
     exp((2 rho-1)L)
     Phi_phi(rho-1/2)
   + E_(L,phi),
```

with

```text
E_(L,phi)=O_(R,phi)(exp(-5L)).
```

The zero sum is absolutely convergent after this fixed smooth testing: repeated integration by parts makes `Phi_phi(beta-1/2+i gamma)` decay faster than every power of `|gamma|`, uniformly for `0<=beta<=1`, while the zero counting function has order `T log T`.

For a zero

```text
rho=beta+i gamma,
```

the `L` factor is

```text
exp((2 beta-1)L) exp(2 i gamma L).
```

Hence the centered boundary variable makes the critical line dynamically visible:

```text
beta=1/2
    -> pure oscillation in L;

beta>1/2
    -> exponentially growing mode-by-mode amplitude;

beta<1/2
    -> exponentially decaying mode-by-mode amplitude.
```

Under RH, for every fixed smooth `phi`, the displayed absolutely convergent zero series is uniformly bounded in `L`. No converse boundedness theorem is claimed here: isolating one off-line mode from possible global cancellations requires an additional argument and would amount to a zero-detection criterion, not merely to the displayed identity.

This derivation does not analytically continue an Euler product. It starts from the already-continued explicit formula, and the test function makes the zero sum rigorous.

## Hankel interpretation of the smooth zero modes

For smooth boundary profiles `f,g` supported in `(0,R)`, set

```text
phi_(f,g)(delta)
 = integral conjugate(g(b)) f(delta-b) db,
```

with zero extension outside `(0,R)`. Its Laplace transform factors:

```text
Phi_(phi_(f,g))(z)
 = [integral f(a) exp(-z a) da]
   [integral conjugate(g(b)) exp(-z b) db].
```

Thus each zero term in the centered shell form has boundary kernel

```text
exp(-(rho-1/2)(a+b)),
```

which is separable, hence rank one at the bilinear-form level. Formally, the smooth centered cross-boundary distribution is a superposition

```text
- sum_rho
    exp((2 rho-1)L)
    exp(-(rho-1/2)(a+b)),
```

plus the exponentially small trivial-zero term.

This is a genuine and useful local dictionary between the boundary Hankel coordinate `a+b` and the zeta zero divisor. But it does **not** contradict the norm-gap theorem: the dictionary exists only after fixed smooth testing, precisely the operation that suppresses the arbitrarily high boundary frequencies used by the Kronecker lower bound.

## Prior art and novelty audit

All essential mechanisms are classical or already persisted.

- The von Mangoldt / Riemann explicit formula and its smooth Weil--Guinand form already identify prime-power distributions with transformed sums over the nontrivial zeros. `SOURCES.md` records Weil's 1952 explicit-formula paper and Bombieri's treatment of Weil's quadratic functional. The `C_L(phi)` identity above is a translated, square-root-normalized test-function specialization of that classical formula.
- `PL-045`, anchored by Marcus Chuk's August 2026 compact-window Weil paper, records the exact Kronecker/Weyl recurrence obstruction for finite rational-prime logarithms. The new norm lower bound reuses that classical recurrence inside the boundary model rather than claiming a new recurrence theorem.
- `PL-049`--`PL-051` supply the fixed-width PNT shell asymptotic, boundary escape, and rank-one first-order Hankel model.
- Exponential separable kernels are elementary finite-rank Hankel structure; no novelty is claimed for recognizing a single exponential as rank one.

A targeted search across smoothed explicit formulas, Hankel/operator formulations, and compact-window Weil literature located the classical explicit-formula mechanism and recent exact finite Guinand--Weil dictionaries, but not a stronger theorem needed to overturn the norm-gap derivation above. Search absence is not treated as evidence of novelty. The durable content is the audited **topology boundary** for this concrete research branch: weak PNT homogenization and smooth zero reconstruction coexist with a nonvanishing raw operator-norm defect forced by the prime-log phase geometry.

## Beurling and matched-control audit

The norm-gap proof uses only

```text
1. positive atomic shell weights;
2. rational independence of the finitely many primitive frequencies;
3. the same fixed-width continuum shell law as PL-051.
```

A matched generalized-prime system with rationally independent primitive energies and the same positive shell limit has the same phenomenon: strong homogenization on fixed profiles, but high-frequency recurrence prevents norm homogenization.

Therefore the norm gap is **not** zeta-specific rigidity. It is another obstruction showing that bare free-frequency geometry can preserve microscopic atomic information that disappears under weak PNT averaging.

The smooth zero-mode identity, by contrast, is zeta-specific only because the ordinary von Mangoldt distribution is linked to the Riemann zero divisor by the completed explicit formula. Replacing the primes by a Beurling system replaces that divisor by whatever analytic object its generalized zeta and explicit formula support. The coordinate change itself supplies no zero localization.

## Analytic-continuation boundary

The two parts of the finding live on cleanly separated sides of the audit.

The norm-gap proof is finite at every `L`; it uses only the finite prime-power shell, PNT asymptotics, and finite-dimensional Kronecker recurrence. No Euler product is continued.

The zero-mode formula uses the classical analytically continued von Mangoldt / Weil explicit formula as its starting theorem. It does not infer critical-strip identities from the absolutely convergent Euler product. Smooth compact support makes the translated test legitimate and the nontrivial-zero sum rapidly convergent.

## Falsification and boundary tests

The norm-gap theorem reduces to five checkable steps:

1. the cross-boundary matrix element of one deficit atom on the opposite modulations `f_xi,g_xi` is `exp(i xi delta) exp(-delta/2) tau_R(delta)/N_R`;
2. finite rational-prime logarithms recur arbitrarily close to simultaneous phase `1`;
3. the same matrix element of `P_R` tends to zero as `|xi|->infinity`;
4. the fixed-width PNT turns the aligned shell sum into `N_R^(-1) integral tau_R(delta)exp(-delta)d delta`;
5. that integral equals `(1-exp(-R))^2`.

Any failure of one of these statements falsifies the claimed constant. Items 1, 3, and 5 are elementary calculations; item 2 is the classical Kronecker theorem plus unique factorization; item 4 is the PNT shell limit already audited in `PL-049`--`PL-051`.

The finding does **not** rule out:

```text
- a weaker distributional or Sobolev topology for centered fluctuations;
- quantitative prime-error information after imposing a fixed smoothing scale;
- mesoscopic boundary depth R=R(L);
- threshold-by-threshold spectral flow before homogenization;
- coupling to the archimedean/pole part of the full Weil operator;
- a new positivity or trace identity that constrains the smooth zero modes.
```

It does rule out treating the fixed-depth PNT boundary model as an operator-norm approximation from which a bounded `exp(L)`-centered spectral correction can simply be extracted.

## Consequence for the research line

The compact-Weil boundary ledger is now

```text
natural global normalization
    -> bulk strong limit 0, edge states escape spatially       [PL-050]

fixed-depth endpoint blow-up
    -> strong rank-one PNT Hankel model                        [PL-051]

uniform operator topology on that boundary layer
    -> prime-log recurrence retains an O(1) norm defect
    -> no norm convergence; exp(L)-centered norm diverges      [PL-052]

fixed smooth centered probes
    -> classical explicit formula
    -> separable zero modes exp((2 rho-1)L)                    [PL-052]
```

So the next useful question is no longer whether the centered first boundary layer *contains* the zeros: after smoothing, the explicit formula says exactly how they appear. The hard question is whether there is a **natural arithmetic topology, positivity principle, or target-relative observable** that controls those zero modes without either (a) being destroyed by high-frequency prime recurrence, or (b) merely restating the explicit formula / RH-equivalent Weil positivity criterion.