# PL-103 — Poisson bulk already forces exponential prime-Gram determinant decay

## Claim

The hard-edge caveat left in `PL-085` does **not** preserve the most basic logarithmic-determinant signal. Under the same full local Hardy--Littlewood hierarchy used there, the unweighted prime-support Gram matrix at every fixed mean-gap observation scale already has a strictly negative one-sided per-site log-determinant rate forced solely by its generic Poisson bulk law.

Fix

```text
0<a<b<infinity,
c>0,
P_X={p prime : aX<p<=bX},
M_X=|P_X|,
T_X=c X/log X,
```

and

```text
G_X(p,q)
 =(1/T_X) integral_0^(T_X)
   exp(i t(log p-log q)) dt,
p,q in P_X.
```

Let

```text
mu_X=(1/M_X) sum_(j=1)^(M_X)
       delta_(lambda_j(G_X)).
```

Assume the full local Hardy--Littlewood hierarchy of `PL-085`, so that

```text
W_2(mu_X,nu_(a,b,c))->0,
```

where `nu_(a,b,c)` is the macroscopic Poisson-sinc Euclidean-random-matrix bulk law. Then, with `log 0=-infinity`, define the extended Poisson logarithmic mean

```text
L_Pois(a,b,c)
 = integral_[0,infinity) log(lambda) d nu_(a,b,c)(lambda).
```

It satisfies

```text
boxed:
L_Pois(a,b,c)<0,
```

possibly with value `-infinity`, and

```text
boxed:
limsup_(X->infinity)
 (1/M_X) log det G_X
 <= L_Pois(a,b,c)<0.
```

Consequently there is a constant

```text
kappa_(a,b,c)>0
```

such that, for all sufficiently large `X`,

```text
boxed:
det G_X <= exp(-kappa_(a,b,c) M_X).
```

The mechanism is not an arithmetic rigidity signal. `PL-083` gives

```text
int lambda d nu_(a,b,c)(lambda)=1,

int lambda^2 d nu_(a,b,c)(lambda)
 =1+pi(a+b)/c>1,
```

so the limiting bulk is nondegenerate. Strict concavity of `log` therefore makes its geometric mean strictly smaller than its arithmetic mean. The law producing that gap is exactly the generic Poisson sinc law already identified in `PL-085`.

At the Nyquist value of `PL-102`, this adds a second matched-control obstruction:

```text
prime critical S_1 excess from smooth continuum
    = generic Poisson shot-noise effect;

prime per-site log-determinant decay
    <= generic Poisson bulk entropy/geometric-mean effect.
```

Thus a negative or exponentially decaying raw prime-Gram determinant at `T~X/log X` cannot by itself be evidence of analytic continuation, the zeta zero divisor, or a rational-prime-specific exponent-lattice mechanism.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-ROUTED + CONJECTURAL-INPUT + DECISIVE-NEGATIVE` for the route

```text
unweighted prime basis directions
+ sharp finite-time logarithmic Gram
+ fixed mean-gap scale T=cX/log X
+ exponentially small determinant / negative per-site log determinant
    -> rational-prime-specific or RH-sensitive evidence by itself.
```

The result is intentionally one-sided. It does **not** determine the exact limit of `(1/M_X) log det G_X`; hard-edge mass near zero may make the true rate more negative or even drive it to `-infinity`. It also does not exclude finer arithmetic information in a properly renormalized hard-edge statistic after the generic Poisson contribution has been removed.

## 1. The finite prime Gram is strictly positive definite

For every finite `X`, the frequencies `{log p:p in P_X}` are distinct. For any coefficient vector `u=(u_p)`,

```text
<u,G_X u>
 =(1/T_X) integral_0^(T_X)
   |sum_(p in P_X) u_p exp(-it log p)|^2 dt.
```

If this vanishes, the finite exponential polynomial inside the absolute value vanishes almost everywhere on an interval, hence identically. Linear independence of distinct real exponentials then gives

```text
u_p=0
```

for every `p`. Therefore

```text
G_X>0
```

and

```text
(1/M_X) log det G_X
 = integral log(lambda) d mu_X(lambda)
```

is finite for each finite `X`.

This positivity fact is elementary and is used only to make the finite determinant well-defined. No uniform lower frame bound is asserted; `PL-082` in fact rules such a bound out along subsequences.

## 2. `W_2` bulk convergence gives an upper-semicontinuous log-determinant bound

The singularity of `log(lambda)` at zero is exactly why `PL-085` did not claim convergence of log determinants from `W_2` convergence alone. But that singularity obstructs only a **lower** bound. It does not prevent the one-sided upper bound needed here.

For `epsilon>0`, put

```text
f_epsilon(lambda)=log(max(lambda,epsilon)).
```

On `[0,infinity)`, `f_epsilon` is globally Lipschitz with constant at most `1/epsilon`, and it has sublinear growth at infinity. Hence `W_2`, and therefore `W_1`, convergence gives

```text
integral f_epsilon d mu_X
 -> integral f_epsilon d nu_(a,b,c).
```

Since

```text
log(lambda)<=f_epsilon(lambda)
```

for every `lambda>0`,

```text
limsup_(X->infinity)
 integral log(lambda) d mu_X(lambda)

 <= integral f_epsilon(lambda)
      d nu_(a,b,c)(lambda).
```

As `epsilon` decreases to zero, the right-hand side decreases to the extended integral

```text
integral log(lambda)d nu_(a,b,c)(lambda).
```

Indeed the positive part is integrable because `log^+(lambda)<=lambda`, while continuity from above applies after fixing any initial `epsilon_0>0`; if the negative part diverges, the limit is simply `-infinity`. Therefore

```text
boxed:
limsup_(X->infinity)
 (1/M_X) log det G_X
 <= L_Pois(a,b,c).
```

This is a general semicontinuity fact for positive spectral measures with convergent first moment. No number theory enters this step after `PL-085` has supplied the limiting law.

## 3. The Poisson logarithmic mean is strictly negative

The Gram diagonal is exactly one, so

```text
integral lambda d mu_X(lambda)
 =(1/M_X)Tr G_X
 =1.
```

`W_2` convergence preserves the first two moments. Hence

```text
integral lambda d nu_(a,b,c)(lambda)=1.
```

The second moment from `PL-083`, propagated through `PL-085`, is

```text
integral lambda^2 d nu_(a,b,c)(lambda)
 =1+pi(a+b)/c.
```

Since `c>0` and `a+b>0`, this is strictly larger than `1`; therefore

```text
nu_(a,b,c) != delta_1.
```

If `L_Pois=-infinity`, strict negativity is immediate. Otherwise Jensen's inequality for the strictly concave function `log` gives

```text
L_Pois(a,b,c)
 =integral log(lambda)d nu
 <=log(integral lambda d nu)
 =0.
```

Equality in Jensen would force `lambda` to be constant `nu`-almost surely, i.e. `nu=delta_1`, contradicting the second moment. Thus

```text
boxed:
L_Pois(a,b,c)<0.
```

Choose any finite positive `kappa_(a,b,c)` smaller than `-L_Pois` when the latter is finite; if `L_Pois=-infinity`, choose any fixed positive `kappa`. The limsup inequality then yields

```text
det G_X <= exp(-kappa_(a,b,c) M_X)
```

for all sufficiently large `X`.

The determinant decay therefore comes from the same nonzero bulk variance that already identifies the local point cloud as non-orthogonal Poisson sampling.

## 4. Why the hard edge remains open but no longer rescues the raw determinant signal

`W_2` convergence cannot control the negative part of `log(lambda)` uniformly near zero. A vanishing fraction of exceptionally small eigenvalues can contribute an arbitrarily large negative amount to

```text
(1/M_X)log det G_X
```

without affecting the `W_2` limit. This is consistent with `PL-082`, where bounded prime clusters force subsequential lower-edge collapse, and with the explicit hard-edge caveat in `PL-085`.

Accordingly, the present argument does **not** prove

```text
(1/M_X)log det G_X
 -> L_Pois(a,b,c).
```

It proves only that the bulk law already forces the determinant to be at least exponentially small. Any unresolved hard-edge contribution can only push the logarithmic determinant farther downward.

This distinction matters for interpretation. The following observations are now separated:

```text
raw determinant is exponentially small
    -> already generic Poisson bulk;

exact normalized log-det rate
or additional hard-edge correction
    -> still requires new information.
```

Therefore the hard edge remains a legitimate mathematical question, but it cannot rehabilitate **mere determinant collapse** as an RH-sensitive phenomenon.

## 5. Matched-control and novelty audit

The load-bearing external input is exactly the prior art already audited for `PL-083`--`PL-085`:

- Gallagher's Hardy--Littlewood-to-Poisson local-prime mechanism;
- Freiberg's joint short-interval Poisson formulation;
- Bordenave's Euclidean-random-matrix moment/spectral framework used for the compact-range Poisson control.

A fresh search of Euclidean-random-matrix, random Fourier/Vandermonde, and sinc-kernel determinant literature found no reason to treat the semicontinuity step as a new random-matrix theorem. The general implication

```text
spectral-law convergence
+ nondegenerate mean-one limit
    -> strictly negative one-sided log-determinant rate
```

is elementary operator/probability theory. The durable content here is the **line-specific collision**: the Poisson bulk law already stored in `PL-085` settles the sign and exponential scale of the prime-Gram determinant that its hard-edge caveat had left uninterpreted.

No `SOURCES.md` update is required. Entries 65--67 already record every external theorem used in the argument; no newly found paper is load-bearing.

## 6. Adversarial boundaries

1. **The prime statement is conditional.** The full local Hardy--Littlewood hierarchy assumed by `PL-085` is unproved. This finding is a falsification control for interpreting determinant decay, not an unconditional prime theorem.

2. **No exact log-determinant limit is claimed.** `W_2` gives the upper bound but cannot stop a thin hard edge from making the normalized log determinant more negative.

3. **No zero information is used.** The proof never invokes analytic continuation, the functional equation, an explicit formula, or any Riemann zero. Once `PL-085` supplies the Poisson bulk law, the determinant conclusion is purely spectral-measure calculus.

4. **The matched control is structural.** The limiting law is by construction the generic Poisson sinc Euclidean-random-matrix law. Hence the negative logarithmic mean is a property of ordinary random sampling at fixed local density, not of the rational-prime norm map.

5. **Weights and targets remain outside scope.** The argument says nothing about von Mangoldt/Möbius weighted determinants, Nyman target-relative objects, completed Weil operators, or a determinant from a genuinely continued zeta object.

6. **A renormalized hard-edge excess is not ruled out.** If one could subtract or quotient the generic Poisson determinant contribution in a canonical way and prove a residual that survives Beurling/Poisson controls, that would be a different claim requiring a new novelty and continuation audit.

## Consequence for the research line

The `PL-083`--`PL-085` Poisson classicalization now reaches farther than fixed polynomial bulk observables and the `PL-102` trace-class separation. It already controls the first qualitative logarithmic-determinant question:

```text
Does the critical prime Gram have exponentially collapsing volume?
```

Under the same local Hardy--Littlewood model, yes -- but for the generic reason that a nondegenerate mean-one Poisson bulk has geometric mean strictly below one.

A determinant-based continuation of the prime-support branch must therefore target something finer than the existence, sign, or exponential scale of raw Gram-volume decay. The surviving possibilities are an **exact hard-edge correction beyond the Poisson law**, a distinguished arithmetic weight/target, or an operator/determinant that genuinely imports the continued zeta structure rather than only prime support at finite Fourier resolution.
