# PL-051 — Fixed-depth boundary blow-up of the localized Weil prime operator converges strongly to a universal rank-one Hankel model

## Claim

`PL-050` shows that after the natural normalization `exp(-L)` and global dilation of the compact Weil window, the non-archimedean operator converges strongly to zero while order-one spectral edges escape into physical boundary layers of depth `O(1)`. The most immediate escape route is therefore to **blow up those endpoint layers instead of dilating them away**.

That boundary blow-up has an exact leading model, and it is arithmetic-universal.

Let

```text
H_L = L^2(-L,L),

K_L
 = sum_(log n<2L) Lambda(n)/sqrt(n)
     (T_(log n)+T_(log n)^*),
```

with the compressed translation convention of `PL-046`--`PL-050`. Fix a boundary depth `R>0` and let

```text
H_R = L^2(0,R).
```

Embed two inward endpoint profiles by the isometry

```text
J_(L,R) : H_R direct_sum H_R -> H_L
```

defined, for `L>R`, by

```text
(J_(L,R)(f,g))(-L+a)=f(a),
(J_(L,R)(f,g))( L-b)=g(b),
0<a,b<R,
```

and zero away from the two endpoint strips. Define the boundary-compressed normalized operator

```text
B_(L,R)
 = exp(-L) J_(L,R)^* K_L J_(L,R).
```

Then, for every fixed `R`,

```text
boxed:
B_(L,R) -> B_R strongly on H_R direct_sum H_R,
```

where

```text
B_R = [ 0    P_R ]
      [ P_R  0   ]
```

and

```text
(P_R f)(b)
 = exp(-b/2) integral_0^R exp(-a/2) f(a) da.
```

Thus

```text
P_R = |h_R><h_R|,
h_R(a)=exp(-a/2),
```

is rank one, with

```text
||h_R||^2 = 1-exp(-R).
```

Consequently the entire nonzero spectrum of the fixed-depth boundary model is

```text
boxed:
sigma(B_R) \ {0}
 = { +(1-exp(-R)), -(1-exp(-R)) }.
```

As `R->infinity`, the limiting half-line boundary model has exactly the two nonzero spectral values `+1` and `-1`.

This recovers the matched endpoint states of `PL-050`, but strengthens their interpretation: they are not merely good Rayleigh test vectors. They are the eigenvectors of the **universal first-order boundary operator** selected by the prime number theorem shell density.

The leading boundary blow-up therefore does not retain zeta-specific zero information. It depends only on the positive von-Mangoldt shell law

```text
exp(-L)
 sum Lambda(n)/sqrt(n)
 delta_(2L-log n)
 -> exp(-delta/2) d delta
```

on each fixed shell. Any matched positive-frequency or Beurling system with the same local shell limit has the same boundary operator.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the specific route

```text
natural exp(-L) normalization
+ fixed O(1)-depth endpoint blow-up
+ first-order operator limit
    -> zeta-specific boundary spectrum.
```

The result does **not** rule out a second-order centered boundary fluctuation, a depth `R=R(L)` growing with `L`, threshold-by-threshold spectral flow, or coupling to the archimedean and pole terms of the full Weil form.

## Exact endpoint decomposition

Take `L` sufficiently large compared with fixed `R`. The compressed endpoint geometry splits the positive lags into three disjoint regimes.

### Small lags: `0 < u < R`

Such translations can act within one endpoint strip, but only finitely many prime powers satisfy `log n<R`. Hence their total operator norm after normalization is bounded by

```text
2 exp(-L)
  sum_(log n<R) Lambda(n)/sqrt(n)
 -> 0.
```

So the same-end diagonal blocks of `B_(L,R)` vanish in operator norm.

### Intermediate lags: `R <= u <= 2L-2R`

These translations are too long to remain inside either endpoint strip and too short to bridge the two strips. Their boundary compression is exactly zero.

### Outer lags: `u=2L-delta`, `0<delta<2R`

These are the only lags surviving the fixed-depth blow-up. If `a` and `b` denote inward distances from the left and right endpoints, respectively, then the cross-end geometry is

```text
boxed: delta = a+b.
```

For a single outer lag, the off-diagonal boundary action is the truncated reflection

```text
(H_delta f)(b)
 = f(delta-b)
```

whenever both `b` and `delta-b` lie in `(0,R)`, and zero otherwise. Therefore, up to the vanishing small-lag diagonal term,

```text
B_(L,R)
 = [ 0          H_(mu_(L,R)) ]
   [ H_(mu_(L,R))       0     ]
   + o_(op)(1),
```

where

```text
mu_(L,R)
 = exp(-L)
   sum_(2L-2R<log n<2L)
     Lambda(n)/sqrt(n)
     delta_(2L-log n)
```

and

```text
(H_mu f)(b)
 = integral f(delta-b) d mu(delta).
```

The boundary blow-up has therefore converted the prime-power translation sum into a Hankel-type operator whose kernel depends on the sum of inward endpoint coordinates.

## PNT shell measure and strong convergence

The fixed-width PNT rescaling already used in `PL-049` and `PL-050` says that, for every continuous `phi` on `[0,2R]`,

```text
integral phi(delta) d mu_(L,R)(delta)

 -> integral_0^(2R)
      phi(delta) exp(-delta/2) d delta.
```

Thus

```text
mu_(L,R) -> mu_R
```

weakly, where

```text
d mu_R(delta)=exp(-delta/2) 1_[0,2R](delta) d delta.
```

The total masses are uniformly bounded and in fact converge to

```text
mu_R([0,2R])
 = 2(1-exp(-R)).
```

Weak convergence of the measures is enough here to obtain **strong operator convergence** of the associated boundary Hankel operators.

Extend `f in H_R` by zero to the whole real line and write

```text
check(f)(x)=f(-x).
```

On the full line,

```text
H_mu f
```

is the restriction to `(0,R)` of the convolution

```text
mu * check(f).
```

For every real Fourier frequency `xi`, weak convergence gives

```text
hat(mu_(L,R))(xi) -> hat(mu_R)(xi).
```

Uniform boundedness of the total masses gives a frequency-independent dominating bound. By Plancherel and dominated convergence,

```text
||(mu_(L,R)-mu_R)*check(f)||_2 -> 0
```

for every fixed `f in L^2(0,R)`. Restricting back to `(0,R)` yields

```text
H_(mu_(L,R)) f -> H_(mu_R) f
```

strongly.

Combining this with the norm-vanishing small-lag blocks proves

```text
B_(L,R) -> B_R
```

strongly.

This is stronger than convergence of the particular Rayleigh quotients used in `PL-050`, while deliberately avoiding an operator-norm convergence claim. Weak convergence of the atomic shell measures does not by itself imply uniform convergence of their Fourier transforms, so no norm-limit statement is needed or asserted.

## Why the limiting Hankel operator is rank one

For `0<a,b<R`, the limiting shell density is evaluated at

```text
delta=a+b.
```

Hence

```text
k_R(a,b)
 = exp(-(a+b)/2)
 = exp(-a/2) exp(-b/2).
```

Therefore

```text
(H_(mu_R) f)(b)
 = integral_0^R
     exp(-(a+b)/2) f(a) da
 = h_R(b) <h_R,f>,
```

so

```text
H_(mu_R)=P_R=|h_R><h_R|.
```

The two-component operator then diagonalizes under symmetric and antisymmetric endpoint combinations:

```text
(f,f)  -> +P_R f,
(f,-f) -> -P_R f.
```

Since `P_R` has sole nonzero eigenvalue

```text
||h_R||^2
 = integral_0^R exp(-a) da
 = 1-exp(-R),
```

the nonzero boundary spectrum is exactly

```text
+/- (1-exp(-R)).
```

The normalized profile from `PL-050`,

```text
g_R=h_R/sqrt(1-exp(-R)),
```

is therefore the exact rank-one eigenprofile of the first-order boundary model. Its previously derived Rayleigh limits

```text
+/- (1-exp(-R))
```

are now explained structurally rather than variationally.

## Exponent-lattice interpretation

The boundary model sees only the outer logarithmic energy shell

```text
2L-2R
 < <v(n),(log p)_p>
 < 2L.
```

Because the completed Weil prime distribution is supported on `Lambda(n)`, the active exponent vectors remain the prime-power rays

```text
v(n)=m e_p.
```

At first boundary order, however, even that axis identity disappears. The shell is compressed to the one-dimensional deficit coordinate

```text
delta
 = 2L-log n
 = 2L-<v(n),(log p)_p>,
```

and the PNT replaces the discrete arithmetic measure by the deterministic density

```text
exp(-delta/2) d delta.
```

The factorization

```text
exp(-(a+b)/2)
 = exp(-a/2) exp(-b/2)
```

then forces rank one. Thus the first-order endpoint zoom performs two successive information losses:

```text
prime-power lattice shell
    -> scalar energy deficit delta
    -> PNT continuum density exp(-delta/2)d delta
    -> rank-one Hankel kernel exp(-(a+b)/2).
```

Neither rational independence of the prime logs, fine prime correlations, the functional equation, nor the nontrivial zero divisor survives this quotient.

## Beurling / matched-control audit

The proof needs only the fixed-width shell convergence

```text
mu_(L,R) -> C exp(-delta/2)d delta
```

with positive weights, after the chosen normalization. More generally, if a generalized frequency system has

```text
exp(-L)
 sum_j a_j delta_(2L-omega_j)
 -> C exp(-delta/2)d delta
```

on every fixed compact deficit interval, then the same argument gives the boundary model

```text
C [ 0  P_R ]
  [ P_R 0   ].
```

Therefore the leading fixed-depth boundary limit is controlled by a one-dimensional local counting law, not by the exact rational-prime norm map. This is a matched-control obstruction of the same type as `PL-015`, `PL-046`, `PL-049`, and `PL-050`.

## Analytic-continuation boundary

No Euler product or Dirichlet series is continued across `Re(s)=1`. For each finite `L`, `K_L` is the finite non-archimedean operator extracted from the already-completed Weil explicit formula. The large-`L` input is only the prime number theorem, through the fixed-ratio shell asymptotic.

Hence the boundary model genuinely lives on the explicit-formula side of analytic continuation. Its failure to carry zero-specific data cannot be blamed on having stayed inside the Euler-product half-plane.

## Prior-art and novelty audit

The ingredients are classical or already persisted:

- `PL-046` identifies the compressed-shift operator `K_L` from the localized Weil form.
- `PL-049` proves the fixed-width PNT shell asymptotic and the first endpoint Rayleigh lower bound.
- `PL-050` identifies boundary escape after global rescaling and the matched exponential endpoint profile.
- Marcus Chuk, arXiv:2608.24827 (August 2026), studies compact-window Weil positivity, the pointwise prime-comb/Kronecker barrier, and numerical/conditional large-window decay. It does not provide the fixed-depth endpoint operator limit above.
- Exponential kernels are standard finite-rank Hankel structure. In particular D. R. Yafaev, “On finite rank Hankel operators,” *Journal of Functional Analysis* 268 (2015), 1808--1839, DOI `10.1016/j.jfa.2014.12.005`, recalls the classical Kronecker classification in which polynomial-exponential Hankel kernels are exactly the finite-rank class. The limiting kernel `exp(-(a+b)/2)` is the elementary rank-one member of that class.

A targeted search combining localized Weil forms, von-Mangoldt compressed translations, boundary/edge scaling, and finite-rank Hankel limits did not locate this exact specialization. That search absence is **not** treated as evidence of novelty. The durable content is the exact consequence for the stored localized-Weil operator and the resulting no-go for a zeta-specific first-order boundary spectrum.

## Falsification and boundary tests

The claim reduces to independently checkable steps:

1. for fixed endpoint depth `R`, only lags `u<R` and `u>2L-2R` survive the endpoint compression;
2. the normalized `u<R` contribution vanishes in operator norm;
3. the outer shell measure `mu_(L,R)` converges weakly to `exp(-delta/2)d delta` by the PNT;
4. uniform total-mass bounds plus Plancherel upgrade convolution by these measures to strong convergence on each fixed `L^2` profile;
5. the limit kernel is `exp(-(a+b)/2)`, hence rank one;
6. the two-end block has only the nonzero eigenvalues `+/- (1-exp(-R))`.

Items 1, 2, 5, and 6 are elementary. Item 3 is the fixed-width PNT lemma already audited in `PL-049`; item 4 is a standard Fourier dominated-convergence argument.

A failure of any one of these six statements falsifies the stored boundary model.

## Consequence for the research line

The natural large-window sequence is now

```text
K_L
    ||K_L|| = Theta(exp(L))                         [PL-049]
        |
        +-- global dilation + exp(-L)
        |      -> strong bulk limit 0
        |      -> spectral edge states escape       [PL-050]
        |
        +-- fixed-depth endpoint blow-up + exp(-L)
               -> universal rank-one Hankel model
               -> nonzero spectrum -> {+1,-1}
                  as boundary depth grows            [PL-051]
```

So the first boundary repair to `PL-050` does not recover hidden Riemann-zero structure; it recovers the PNT in operator form.

A genuinely arithmetic next step must therefore remove or go beyond this universal leading layer. Plausible surviving targets are deliberately narrower:

```text
- the centered shell fluctuation
    mu_(L,R) - exp(-delta/2)d delta;
- a mesoscopic depth R=R(L) where PNT-level weak convergence is no longer the whole story;
- threshold-by-threshold spectral flow when individual prime powers enter the window;
- coupling of the boundary prime model to the archimedean and pole terms before taking a limit;
- an observable sensitive to prime correlations rather than only positive shell mass.
```

Any such route must be tested against Beurling systems and against the possibility that its apparent spectral structure is again a universal Hankel/finite-section phenomenon.