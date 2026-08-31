# PL-061 — PNT-resolution boundary bands are archimedean-negligible in the full completed Weil form

## Claim

The moving-frequency estimate of `PL-060` can be upgraded from the bounded pole-minus-prime sector to the **full completed Weil form** on the same Dirichlet-frequency window. More importantly, the archimedean logarithmic frequency cost cannot balance the prime-shell discrepancy at the natural PNT-resolution scale.

Fix `R>0` and retain the notation

```text
X_L=exp(2L),
psi(x)=sum_(n<=x) Lambda(n),

r_(L,R)
 = sup_(X_L exp(-2R) <= x <= X_L)
     |psi(x)-x|/x.
```

Let `J_(L,R)` be the two-end boundary embedding from `PL-051`, let `P_N` project onto the first `N` Dirichlet sine modes of `L^2(0,R)`, and write

```text
Pi_N=P_N direct_sum P_N.
```

For each finite `N`, let `W_(L,R,N)` be the unique self-adjoint operator on `Ran(Pi_N)` representing the naturally normalized completed Weil quadratic form,

```text
<u,W_(L,R,N)u>
 = exp(-L) Q_W^L(J_(L,R)u),
 u in Ran(Pi_N).
```

Then there is `A_R<infinity` such that, for all sufficiently large `L` and all `N>=1`,

```text
boxed:
||W_(L,R,N)||
 <= A_R [
      N r_(L,R)
      + exp(-L)(1+log(1+N))
    ].
```

The first term is exactly the quantitative pole/PNT-centered prime-shell discrepancy of `PL-060`. The second term is the entire remaining scalar plus archimedean contribution on the moving band.

For the ordinary rational integers there is also the elementary lower bound

```text
boxed:
r_(L,R) >= (1/2) exp(-2L)
```

for all sufficiently large `L`. It uses only that `psi(x)` is constant between consecutive integers while `x` increases with slope `1`.

Consequently, if

```text
N(L) r_(L,R) = O(1),
```

then automatically

```text
exp(-L) log(1+N(L)) -> 0.
```

In particular, the single condition already used in `PL-060`,

```text
N(L) r_(L,R) -> 0,
```

now implies the **full completed-form compression**

```text
boxed:
||W_(L,R,N(L))|| -> 0.
```

Thus the archimedean sector is not a hidden obstruction to the `PL-060` no-go. It is asymptotically negligible throughout the entire frequency range at or below the natural PNT-resolution transition `N=O(1/r_(L,R))`.

There is a complementary scale separation. The displayed upper bound leaves room for an order-one normalized archimedean contribution only when

```text
log N(L) comparable to exp(L)
```

or larger. But the staircase bound then forces

```text
N(L) r_(L,R)
 >= (1/2) exp(log N(L)-2L)
 -> infinity
```

whenever `log N(L) >= c exp(L)` along a subsequence for some `c>0`. Hence a Dirichlet band cannot simultaneously sit at PNT resolution and make the archimedean logarithmic cost order one.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` only for the routes

```text
full completed fixed-depth Weil boundary form
+ first N(L) Dirichlet modes
+ N(L) r_(L,R) -> 0
    -> nontrivial mesoscopic norm limit,
```

and

```text
Dirichlet-band PNT transition N(L) r_(L,R)=O(1)
+ archimedean logarithmic frequency cost
    -> common order-one prime/archimedean balance.
```

The result does **not** determine what happens when `N r` is bounded away from zero, because the prime discrepancy estimate is then only `O(1)`. It also does not rule out frequencies far beyond `1/r`, a non-band-limited topology, a different moving form-domain scaling, or a mechanism using more than the raw norm of the compressed form.

## Archimedean multiplier bound

For the completed zeta function, the archimedean distribution can be written on the Fourier side using the logarithmic derivative of the gamma factor. Up to the fixed normalization and scalar term already used in `PL-059`, its multiplier is

```text
m_infinity(t)
 = -log(pi)
   + Re digamma(1/4+i t/2).
```

The classical digamma asymptotic gives a global bound

```text
|m_infinity(t)|
 <= C [1+log(2+|t|)].
```

For

```text
phi=v*v_tilde,
```

one has

```text
phi_hat(t)=|v_hat(t)|^2,
```

so the archimedean quadratic form satisfies

```text
|Q_infinity(v)|
 <= C integral_R
        |v_hat(t)|^2
        [1+log(2+|t|)] dt.
```

This is the same logarithmic high-frequency behavior that underlies the prime-free localized Weil analysis in `PL-044` and the pointwise tail barrier in `PL-045`; no new gamma-factor phenomenon is being claimed here.

## Uniform logarithmic cost on the first N boundary modes

Take

```text
u=(f,g) in Ran(Pi_N)
```

and put

```text
v=J_(L,R)u.
```

Every Dirichlet sine mode vanishes at the endpoints of `(0,R)`. Hence the zero extensions of `f` and `g` belong to `H^1(R)`, and translating them to the two boundary intervals near `-L` and `+L` introduces no derivative jump. The endpoint embedding is isometric and preserves the derivative energy:

```text
||v||_2^2
 = ||f||_2^2+||g||_2^2,

||v'||_2^2
 = ||f'||_2^2+||g'||_2^2.
```

The Dirichlet cutoff gives

```text
||v'||_2
 <= (pi N/R) ||v||_2.
```

Normalize first to `||v||_2=1`. By Plancherel, the probability measure proportional to `|v_hat(t)|^2 dt` has second moment `||v'||_2^2` up to the fixed Fourier normalization. Since `x -> log(2+x)` is concave, Jensen and Cauchy--Schwarz give

```text
integral |v_hat(t)|^2 log(2+|t|) dt
 <= A_R log(2+||v'||_2)
 <= A_R [1+log(1+N)].
```

Therefore

```text
boxed:
|Q_infinity(J_(L,R)u)|
 <= A_R [1+log(1+N)] ||u||_2^2.
```

The remaining scalar multiple of

```text
phi(0)=||v||_2^2
```

is `O(||u||_2^2)` and is absorbed by the same bound. After the natural boundary normalization `exp(-L)`, the full scalar-plus-archimedean contribution on `Ran(Pi_N)` is therefore

```text
O_R(exp(-L)[1+log(1+N)]).
```

This is a genuine uniform moving-state estimate, unlike the fixed-profile `O(1)` statement in `PL-059`.

## Combination with the canonically centered prime sector

`PL-059` decomposes the completed boundary form into the pole term, the non-archimedean von-Mangoldt term, the scalar term, and the archimedean term. The first two form the bounded centered operator

```text
C_(L,R)=E_(L,R)-B_(L,R).
```

`PL-060` proves directly on `Ran(Pi_N)` that

```text
||Pi_N C_(L,R) Pi_N||
 <= A_R [N r_(L,R)+exp(-L)].
```

Adding the preceding scalar/archimedean estimate gives

```text
||W_(L,R,N)||
 <= A_R [
      N r_(L,R)
      + exp(-L)(1+log(1+N))
    ],
```

which is the first displayed theorem.

No zero sum is used in this estimate. The completed Weil formula supplies the already-continued global object, `PL-059` supplies its canonical pole/PNT centering, the PNT remainder controls the atomic shell, and the gamma factor supplies only the elementary logarithmic Fourier weight.

## The integer staircase forces scale separation

The remaining point is elementary but structurally important. Put

```text
a_L=X_L exp(-2R),
b_L=X_L.
```

For sufficiently large `L`, the shell `[a_L,b_L]` contains a full unit interval `(m,m+1)`. On that open interval there is no integer, hence no jump of `psi`; therefore

```text
E(x)=psi(x)-x
```

is affine with slope `-1`. Its values across the interval differ by arbitrarily close to `1`, so

```text
sup_(m<x<m+1) |E(x)| >= 1/2.
```

Since every such `x` satisfies `x<=X_L`,

```text
r_(L,R)
 >= 1/(2X_L)
 = (1/2)exp(-2L).
```

This lower bound is not an analytic estimate for the PNT. It is the unavoidable quantization error caused by the ordinary integer support of the von-Mangoldt staircase.

Now suppose

```text
N(L) r_(L,R) <= M
```

for some fixed `M`. Then

```text
N(L)
 <= M/r_(L,R)
 <= 2M exp(2L),
```

and hence

```text
exp(-L) log(1+N(L))
 <= exp(-L)[2L+O_M(1)]
 ->0.
```

So the archimedean caveat in `PL-060` disappears not only in its collapsing regime `N r->0`, but throughout the complete `N r=O(1)` transition window.

Conversely, if the normalized logarithmic frequency penalty fails to vanish, then along some subsequence

```text
log(1+N(L)) >= c exp(L).
```

The same staircase bound yields

```text
N(L) r_(L,R)
 >= (1/2) exp(c exp(L)-2L+o(1)),
```

which diverges. Thus the simple Dirichlet-band topology contains two parametrically separated scales:

```text
PNT-resolution scale:
    N = O(1/r_(L,R)) <= O(exp(2L));

possible archimedean order-one scale:
    log N = Omega(exp(L)),
    N >= exp(c exp(L)).
```

They cannot coincide.

## Relation to the exponent lattice and `PL-045`

The shell in `PL-060` samples prime-power axis vectors

```text
v(n)=m e_p,
<v(n),(log q)_q>=log n approximately 2L.
```

PNT homogenization forgets the axis label and replaces the atomic shell by a continuum deficit measure. The quantity `r_(L,R)` measures how well the ordinary prime-power staircase can imitate that continuum on the fixed-ratio shell. The unit spacing of the ambient integer `n` prevents this imitation from ever being more accurate than order `1/X_L` in relative sup norm.

The archimedean term, in contrast, sees boundary Fourier frequency and charges only its logarithm. After the natural factor

```text
exp(-L)=X_L^(-1/2),
```

all polynomial-in-`X_L` frequency bands have vanishing archimedean cost. An order-one cost is first compatible with frequencies of size

```text
exp(c sqrt(X_L)),
```

which is doubly exponential in `L`.

This is consistent with, but distinct from, `PL-045`. There the pointwise Weil symbol must wait until vertical height roughly

```text
exp(A_L),
A_L approximately 4 exp(L),
```

before logarithmic archimedean growth can dominate the recurrent all-aligned prime comb. Here a different boundary/Galerkin calculation independently places any possible archimedean order-one effect at the same qualitative `exp(c exp(L))` frequency scale. The present finding does not reprove Chuk's pointwise theorem; it shows that the much smaller PNT-resolution band isolated by `PL-060` cannot realize the hoped-for prime/archimedean balance either.

## Matched-control audit

The estimate

```text
archimedean cost
 <= A_R exp(-L)[1+log(1+N)]
```

is universal gamma-factor/one-dimensional Fourier geometry. Likewise the `N r` shell-discrepancy estimate of `PL-060` works for matched generalized-prime systems possessing the analogous quantitative PNT remainder.

The automatic implication

```text
N r=O(1)
 -> archimedean cost ->0
```

uses one extra feature of the ordinary rational system: the von-Mangoldt counting function is a staircase supported on ordinary integers, so its relative sup error cannot beat `1/(2X_L)`. A Beurling system with a much denser generalized-integer support need not satisfy that exact lower bound without an additional spacing hypothesis.

This rational-integer specificity does **not** create an RH mechanism. It only proves a stronger no-go for the ordinary system: the two candidate scales are separated before any zero-sensitive information is invoked.

## Analytic-continuation boundary

No Euler product or Dirichlet series is continued in the proof. The completed Weil form is already the analytically continued explicit-formula object. The prime contribution at finite `L` is a finite von-Mangoldt sum, the pole term is the completed residue contribution, and the archimedean multiplier comes from the gamma factor.

The PNT appears only through `r_(L,R)->0` and the quantitative estimate already proved in `PL-060`. The new staircase lower bound is elementary and does not use a zero-free region. Therefore the conclusion does not smuggle RH-scale zero information into the moving-frequency normalization.

## Prior-art and novelty audit

The ingredients are classical or already canonical in this line:

- Weil's explicit formula and Bombieri's analysis of the Weil quadratic functional supply the gamma-factor/archimedean term and its Fourier interpretation (`SOURCES.md` 25--26);
- Suzuki's localized Weil framework supplies the current form/operator setting (`SOURCES.md` 56);
- `PL-044` and the current numerical audit source `SOURCES.md` 57 already identify logarithmic archimedean spectral growth as universal rather than zeta-specific;
- `PL-045` supplies the independent pointwise double-exponential scale comparison;
- `PL-059` supplies the canonical pole/PNT cancellation;
- `PL-060` supplies the direct `N r_(L,R)` moving-band estimate.

A targeted literature audit around localized Weil forms, moving/Galerkin frequency cutoffs, PNT boundary remainders, and archimedean logarithmic costs found nearby finite-Galerkin and archimedean-tail work, but no source stating the combined boundary estimate or the elementary `N r=O(1)` scale-separation consequence above. **No novelty is claimed for the component estimates.** The stored result is an exact project-derived synthesis that closes the explicit archimedean caveat left by `PL-060`.

The theorem would be falsified by any of the following:

1. failure of the standard logarithmic bound for the gamma-factor multiplier;
2. failure of the `H^1` derivative bound on the zero-extended Dirichlet band;
3. failure of the `PL-060` `N r` estimate;
4. a counterexample to the unit-staircase bound `r_(L,R)>=exp(-2L)/2` for ordinary `psi`.

Items 1--2 are standard Fourier/special-function facts, item 3 is the immediately preceding canonical finding, and item 4 follows from an interval on which `psi` is constant. The result therefore has a short independent audit surface.

## Consequence for the research line

The moving-boundary ledger can now be sharpened to

```text
fixed profiles
    -> completed pole/PNT cancellation;

N(L) r_(L,R) ->0
    -> full completed Weil compression ->0 in norm;

N(L) r_(L,R)=O(1)
    -> archimedean sector still ->0 uniformly;
       only the atomic prime discrepancy can remain order one;

log N(L) comparable to exp(L)
    -> archimedean cost may become order one,
       but this is already far beyond PNT resolution;

unrestricted high frequency
    -> prime-log recurrence survives in Calkin.
```

Therefore `CLUE-mesoscopic-weil-boundary-topology` should no longer seek a simultaneous archimedean/prime balance at the PNT-resolution transition of a fixed-depth Dirichlet band. A surviving construction must either extract a stable rational-prime-specific invariant from the prime discrepancy itself at `N r` of order one, move to frequencies far beyond `1/r`, or use a genuinely different full-form topology in which the above band estimate is not the governing scale.