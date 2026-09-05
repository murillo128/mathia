# PL-174 — Logarithmic affine Liouville spectrum is Haar-flat

## Claim

The nonuniform affine-shift escape left after `PL-172` and `PL-173` has a sharp theorem-controlled obstruction once one passes from ordinary Cesaro traces to logarithmic averaging. The canonical prime-lattice parity

```text
lambda(n)=(-1)^Omega(n)=(-1)^(sum_p v_p(n))
```

retains its multiplicative provenance, and the additive shifts `n -> n+h` are genuinely outside the multiplicative exponent lattice. Nevertheless, the entire **fixed finite second-order shift spectrum** becomes universal under logarithmic averaging: its limiting correlation function is the Kronecker delta and hence its Herglotz spectral measure is normalized Haar measure on the circle.

More precisely, let

```text
H_X=sum_(n<=X) 1/n,

J_j e_n=lambda(n+j)e_n,

phi_X(D)=H_X^(-1) sum_(n<=X) (1/n)<D e_n,e_n>,
```

where `j>=1` is fixed. Then Terence Tao's logarithmically averaged two-point Chowla theorem implies

```text
phi_X(J_j J_k) -> delta_(j,k)
```

for every fixed pair `j,k>=1`. Consequently, for every fixed `R` and every `c_1,...,c_R in C`,

```text
phi_X((sum_(j<=R) c_j J_j)^*(sum_(k<=R) c_k J_k))
   -> sum_(j<=R) |c_j|^2.
```

Equivalently, the fixed finite logarithmic Gram matrices of additive Liouville translates converge to the identity. If one records only the limiting two-point correlation

```text
r(h)=lim_(X->infinity)
     H_X^(-1) sum_(n<=X) lambda(n+1)lambda(n+1+h)/n,
```

then `r(0)=1` and `r(h)=0` for every nonzero integer `h`; by Herglotz, the corresponding spectral measure is normalized Haar/Lebesgue measure on `T`.

This is not a claim that the full logarithmic Liouville Furstenberg system is Bernoulli or that all higher correlations are known. It is exactly a second-order statement. Dynamical reformulations and structural analysis of logarithmic Möbius/Liouville systems are established prior art; the line-local content here is the obstruction obtained by inserting Tao's theorem into the affine prime-parity operator channel isolated in `PL-172`--`PL-173`.

A very recent preprint of Jizhou Guo gives a further, currently non-peer-reviewed, strengthening at growing shift scales. Assuming that preprint's theorem as stated, any **diffuse direct shift filter** with bounded `ell^1` mass and individual weights of order `1/H` is also flattened uniformly for every `H<=X`, apart from a super-logarithmically sparse exceptional set of shifts. Thus the residual route

```text
prime-lattice Liouville parity
+ additive shifts
+ theorem-accessible logarithmic second-order averaging
+ fixed or diffuse shift spectral filter
    -> new RH-sensitive carrier
```

is obstructed. A surviving affine route must instead use ordinary Cesaro correlations (and face the fixed-shift Chowla barrier), concentrate on exceptional shifts in a source-forced non-arbitrary way, use higher-order/nonlinear data, or couple the shift system directly to completed-zeta/Nyman/explicit-formula structure before the logarithmic second-order spectrum classicalizes.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION` for logarithmically averaged **second-order** affine Liouville spectral filters. No novelty claim is made for logarithmic Chowla, Herglotz spectralization, or logarithmic Furstenberg systems themselves.

## Exact fixed-filter derivation

For fixed `j,k>=1`, define

```text
G_X(j,k)
 =H_X^(-1) sum_(n<=X)
   lambda(n+j)lambda(n+k)/n.
```

The diagonal is exact:

```text
G_X(j,j)=1,
```

because `lambda(m)^2=1` for every positive integer `m`.

For `j!=k`, Tao's theorem applies with

```text
a_1=a_2=1,

b_1=j,

b_2=k,
```

for which `a_1 b_2-a_2 b_1=k-j!=0`. His theorem states, for arbitrary `omega(X)->infinity` with `1<=omega(X)<=X`,

```text
sum_(X/omega(X)<n<=X)
 lambda(n+j)lambda(n+k)/n
   =o(log omega(X)).
```

Taking `omega(X)=X` yields

```text
sum_(1<n<=X) lambda(n+j)lambda(n+k)/n=o(log X).
```

Adding the omitted `n=1` term changes the sum by `O(1)`, while

```text
H_X=log X+O(1).
```

Hence

```text
G_X(j,k)->0
```

for every fixed `j!=k`.

For fixed `R`, entrywise convergence of the `R x R` matrix `G_X` to the identity is automatically convergence in every matrix norm. Therefore

```text
H_X^(-1) sum_(n<=X) (1/n)
 |sum_(j=1)^R c_j lambda(n+j)|^2
   -> sum_(j=1)^R |c_j|^2.
```

The statement is stronger than merely saying that each individual fixed-shift correlation vanishes: every fixed finite second-order filter sees the same limiting quadratic form as independent unbiased signs.

## Herglotz interpretation: the accessible second-order spectrum is Haar

Set, for fixed integer `h`,

```text
r_X(h)=H_X^(-1) sum_(n<=X)
       lambda(n+1)lambda(n+1+h)/n
```

when `h>=0`, and use `r_X(-h)=conjugate(r_X(h))` for the symmetric extension. The Liouville values are real, and the preceding calculation gives

```text
r(h)=lim r_X(h)=delta_(h,0).
```

The positive-definite function `r(h)=delta_(h,0)` has, by the Herglotz theorem, the unique representing probability measure

```text
dsigma(theta)=dtheta/(2 pi).
```

Thus the second-order Koopman/spectral observable obtained from fixed additive translates of the prime-lattice parity is spectrally **white** in the logarithmic theorem regime.

This conclusion must not be promoted to a statement about all orders. Two-point Haar spectrum does not imply a Bernoulli process, mixing of all orders, or the full Chowla conjecture. Existing ergodic work on Möbius/Liouville systems makes exactly this distinction important: structural statements about Furstenberg systems require more than the two-point correlation alone.

## Growing diffuse filters under the current all-shift-scale preprint

Guo's preprint `arXiv:2608.23500v4` states that there is an absolute `c>0` such that, for every sufficiently large `X`, one can choose a single exceptional set `E_X subset [1,X]` satisfying, for every fixed `A>0`,

```text
|E_X intersect [1,H]| <<_A H (log X)^(-A)
```

uniformly for `1<=H<=X`, while for every `h<=X` outside `E_X`,

```text
sup_(1<=Y<=X)
 |sum_(n<=Y) lambda(n)lambda(n+h)/n|
   << (log X)^(1-c).
```

Normalize

```text
rho_X(h)=1/(log X)
         sum_(n<=X) lambda(n)lambda(n+h)/n.
```

For good shifts,

```text
|rho_X(h)| << (log X)^(-c).
```

For all shifts, trivially

```text
|rho_X(h)| <= H_X/(log X)=1+o(1).
```

Now let `1<=H<=X` and let deterministic weights `w_h=w_h(X)` obey

```text
sum_(h<=H) |w_h| <= C,

max_(h<=H) |w_h| <= C/H,
```

with `C` independent of `X,H`. Splitting good and exceptional shifts gives

```text
|sum_(h<=H) w_h rho_X(h)|
 <= O_C((log X)^(-c))
    +(C/H)|E_X intersect [1,H]|(1+o(1))

 <<_A,C (log X)^(-c)+(log X)^(-A).
```

Hence, conditional only on the correctness of that currently unrefereed preprint theorem,

```text
sum_(h<=H) w_h rho_X(h) -> 0
```

uniformly across the full range `1<=H<=X` for every such diffuse family of direct weights.

This covers normalized uniform weights and many smooth/Fejer-type direct shift averages whose individual coefficients are `O(1/H)`. It does **not** cover weights that put nonnegligible mass on a sparse exceptional set, nor does it identify the exceptional shifts arithmetically. Since `E_X` is an output of the theorem rather than a canonical prime-lattice construction, deliberately choosing weights from it would not by itself provide a source-forced RH mechanism.

Because Guo's result is a September 2026 preprint rather than a peer-reviewed theorem, the robust stored conclusion is layered: Tao's 2016 published theorem already gives the unconditional fixed-filter Haar-flat obstruction; Guo's current result is retained only as a sharpened all-shift-scale control for diffuse growing filters.

## Relation to `PL-172` and `PL-173`

`PL-172` found the exact affine parity operator

```text
K_h=J S_h^* J S_h
    =diag(lambda(n)lambda(n+h)),
```

whose first heat trace

```text
C_h(s)=sum_n lambda(n)lambda(n+h)n^(-s)
```

is the fixed-shift Chowla Dirichlet series in `Re(s)>1`; the Hilbert--Schmidt determinant `det_2` crosses the `1/2` Schatten threshold only by deleting that hard first trace.

`PL-173` then showed that the canonical uniform operator average over shifts collapses strongly to zero and that the complete finite-window all-pair sum reduces exactly to the one-point quantity `[L(N)^2-N]/2`. Its remaining live branch was a nonuniform, source-forced weighting/comparison that retained shifted arithmetic rather than averaging it away.

The present finding shows that **logarithmic weighting does not rescue that branch at second order**. For fixed filters it makes the limiting Gram exactly identity/Haar; under Guo's current theorem, diffuse growing direct filters are also forced to zero. Thus the distinction is now sharper:

```text
ordinary Cesaro affine correlations
    -> retain fixed-shift Chowla difficulty;

logarithmic second-order affine correlations
    -> theoremically accessible,
       but fixed-filter spectrum becomes Haar-flat;

canonical/diffuse shift averaging
    -> collapses further rather than creating zero data.
```

The logarithmic result is not an analytic continuation of `C_h(s)`. The weight `1/n` is a statistical averaging device and the limit above is not the value of a meromorphic continuation of the Dirichlet series at `s=1`. No statement about continuation of `C_h(s)` across its convergence boundary is used or obtained.

## Prime-lattice interpretation and RH relevance

The multiplicative source is canonical:

```text
lambda(n)=(-1)^Omega(n)
         =(-1)^(sum_p v_p(n)),
```

so Liouville is precisely the total-parity character of the full exponent lattice. The additive shift `n -> n+h`, however, is the nonmultiplicative operation isolated by `PL-169` as the first standard place where multiplicative Dirichlet data acquires genuinely new arithmetic coupling.

The present obstruction says that one natural way of turning that coupling into a spectral object loses the source information again. After logarithmic second-order averaging, the correlations do not retain a special prime-frequency density, zeta divisor, completed functional equation, or critical-line selector: they reduce to the universal Haar spectral measure.

This is a matched-control failure internal to the actual Liouville sequence rather than a deformation argument. It therefore differs from saying merely that generic random signs have flat spectrum. The arithmetic theorem itself forces the canonical exponent-parity sequence to have the same fixed second-order logarithmic spectrum.

Accordingly, the following route should no longer be pursued as an RH mechanism without additional structure:

```text
prime-exponent parity
 -> additive shift family
 -> logarithmic two-point state
 -> Herglotz/Toeplitz spectrum
 -> RH localization.
```

The last arrow has no remaining source-specific second-order datum to act on.

## What survives

This is deliberately not a no-go theorem for additive arithmetic. Four materially different routes remain outside the obstruction:

1. **Ordinary Cesaro fixed-shift correlations.** Tao's theorem is logarithmically averaged; ordinary fixed-shift two-point Chowla remains a stronger problem. Returning to that regime restores arithmetic difficulty rather than supplying a solved spectral mechanism.

2. **Exceptional, non-diffuse shift weights.** Guo's current theorem permits an exceptional set. A natural source operation that is proved independently to concentrate on a structurally defined subset of those shifts would not be covered, but choosing the exceptional set after inspecting the correlation is circular.

3. **Higher-order or nonlinear observables.** Pair-correlation Haar flatness does not classify higher-order logarithmic Liouville structure. Any such route must identify a concrete operator/trace consequence rather than invoke generic "randomness" language.

4. **Completed or target-relative coupling.** A construction that couples the additive shift carrier directly to Nyman targets, Weil explicit-formula weights, an archimedean duality, or another independently justified completed-zeta structure before taking the logarithmic limit is not reduced to the bare second-order Herglotz measure proved here.

The research frontier therefore narrows from "find a nonuniform shift average" to a falsifiable requirement: the next affine candidate must retain a **non-Haar, source-forced invariant beyond logarithmic two-point correlation**, or must operate in a regime where such correlation is not already theoremically flattened.

## Prior-art / novelty audit

Primary literature anchor:

- Terence Tao, “The logarithmically averaged Chowla and Elliott conjectures for two-point correlations,” *Forum of Mathematics, Pi* **4** (2016), e8. DOI: https://doi.org/10.1017/fmp.2016.6. arXiv: https://arxiv.org/abs/1509.05422. The theorem used here is the published logarithmic two-point Chowla estimate for fixed affine forms.

Current sharpening, treated explicitly as preprint evidence:

- Jizhou Guo, “Logarithmic Chowla Correlations Across All Shift Scales,” arXiv:2608.23500v4 [math.NT], submitted 24 August 2026, revised 1 September 2026. https://arxiv.org/abs/2608.23500. The only use here is the stated single-exceptional-set, full-shift-range power-logarithmic bound.

Dynamical/spectral context is established prior art rather than a new interpretation. In particular:

- Nikos Frantzikinakis, Bernard Host, “The logarithmic Sarnak conjecture for ergodic weights,” *Annals of Mathematics* **187** (2018), 869–931. DOI: https://doi.org/10.4007/annals.2018.187.3.6. This develops structural results for measure-preserving systems naturally associated with Möbius and Liouville and places logarithmic arithmetic correlations inside an established ergodic framework.

- The general Herglotz/Koopman spectral-measure step is classical harmonic/ergodic analysis; no novelty is claimed for converting a positive-definite correlation function into a circle measure.

The exact line-specific deduction

```text
Tao logarithmic two-point Chowla
+ affine prime-parity operators from PL-172/PL-173
    -> fixed logarithmic Gram tends to identity
    -> second-order spectral measure is Haar
```

is stored as a route audit/redirect, not as a new theorem in analytic number theory.

## Adversarial checks

- **Not ordinary Chowla:** the finding never upgrades logarithmic cancellation to `sum_(n<=X) lambda(n)lambda(n+h)=o(X)`.
- **Not higher-order Bernoulli:** pair correlations `delta_(h,0)` determine only the second-order spectral measure.
- **Not Dirichlet continuation:** `1/n` logarithmic weighting is not used as a claim that `C_h(s)` analytically continues to `s=1`.
- **No exceptional-set erasure:** the growing-filter conclusion explicitly keeps Guo's exceptional set and requires diffuse weights; concentrated/adaptive weights are excluded.
- **Preprint layer separated:** the fixed-filter theorem is peer-reviewed Tao 2016; only the growing all-shift-scale strengthening depends on Guo 2026.
- **No random-model substitution:** the Haar limit is derived for the actual Liouville parity sequence from a theorem, not inferred from a random-sign analogy.
- **No bare-lattice novelty claim:** `lambda(n)=(-1)^(sum_p v_p(n))` is a standard arithmetic character of exponent parity; its role here is to connect the established theorem to the current affine-lattice route.
