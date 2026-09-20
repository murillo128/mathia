# VIS-345 — long frequency windows resolve translated Wang phase fibers

## Claim

Let Wang's exact multiplier be

`m(xi)=4(1+i xi)/(4+xi^2)`,

and let

`M(xi)=sum_j c_j exp(-i b_j xi) m(a_j xi)`

be a finite translated-dilate bank with `a_j>0`, real `b_j`, and frequency-independent complex coefficients. Group equal translations and, for each translation fiber `b`, define the inverse-scale moments

`S_(b,k)=sum_(j:b_j=b) c_j a_j^(-k)`.

Let the distinct active translations be `b_1,...,b_B`; when `B>=2`, put

`Delta=min_(p!=q)|b_p-b_q|`.

For each fixed integer `k>=1`, suppose the lower fiber moments vanish,

`S_(b,1)=...=S_(b,k-1)=0`

for every active `b`. Then there is a constant `C_k`, depending only on the fixed bank and `k`, such that for every interval `I=[X,X+L] subset [X,2X]`,

`RMS_I(xi^k M(xi)) >= |beta_k| q(L,Delta,B)^(1/2) (sum_b |S_(b,k)|^2)^(1/2) - C_k/X`,

where `beta_k != 0` is the `k`-th coefficient in the large-`xi` expansion of `m`,

`q(L,Delta,B)=1-2(B-1)/(L Delta)`

for `B>=2`, while `q=1` for `B=1`, and

`RMS_I(f)^2=(1/L) integral_I |f(xi)|^2 dxi`.

In particular, if `B>=2` and

`L Delta >= 4(B-1)`,

then

`RMS_I(xi^k M(xi)) >= (|beta_k|/sqrt(2)) (sum_b |S_(b,k)|^2)^(1/2) - C_k/X`.

Consequently, for a **fixed bank with separated translations**, cancellation confined to moving frequency windows does not evade the fiberwise moment obstruction of `VIS-344` once the windows are long enough to resolve the phase spacing. If for some integer `r>=2` there is a sequence of intervals

`I_X subset [X,2X]`, `X->infinity`,

whose lengths satisfy `L_X Delta >= 4(B-1)` and on which

`sup_(xi in I_X)|M(xi)|=O(X^(-r))`,

then necessarily

`S_(b,k)=0`, `k=1,...,r-1`,

for every translation fiber `b`. Thus the same fiberwise Vandermonde cost as in the uniform-tail theorem is forced by any arbitrarily high sequence of phase-resolving windows.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL NONHARMONIC-FOURIER/INGHAM STRUCTURE + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

The claim does not exclude genuinely short windows, translation spacings that shrink with the window scale, frequency-dependent/adaptive coefficients, changing banks whose conditioning degenerates, or estimates coupled to signed arithmetic structure of the source `G`.

## 1. Wang's tail reduces each order to an exponential polynomial

For every fixed `K>=1`, `VIS-343` gives the asymptotic expansion

`m(z)=sum_(ell=1)^K beta_ell z^(-ell)+O(|z|^(-K-1))`,

with every `beta_ell != 0` (`beta_1=4i`). Hence

`M(xi)=sum_(ell=1)^K beta_ell xi^(-ell) P_ell(xi)+O(|xi|^(-K-1))`,

where

`P_ell(xi)=sum_b S_(b,ell) exp(-i b xi)`.

If the fiber moments below order `k` vanish, then uniformly for `xi>=X`,

`xi^k M(xi)=beta_k P_k(xi)+O(X^(-1))`.

The remaining question is therefore quantitative: how small can the finite exponential polynomial `P_k` be throughout a moving interval?

## 2. A phase-resolving interval has a uniform lower frame bound

Write

`P(xi)=sum_(p=1)^B d_p exp(-i b_p xi)`

with distinct real `b_p`. On any interval `I=[A,A+L]`, direct integration gives

`(1/L) integral_I |P(xi)|^2 dxi`

`=sum_p |d_p|^2 + sum_(p!=q) d_p conjugate(d_q) exp(-i(b_p-b_q)A) J_((b_p-b_q),L)`,

where

`J_(omega,L)=(1-exp(-i omega L))/(i omega L)`

and therefore

`|J_(omega,L)| <= 2/(L|omega|)`.

If `Delta=min_(p!=q)|b_p-b_q|`, then

`|(off-diagonal contribution)|`

`<= [2/(L Delta)] sum_(p!=q)|d_p||d_q|`.

By Cauchy-Schwarz,

`(sum_p |d_p|)^2 <= B sum_p |d_p|^2`,

so

`sum_(p!=q)|d_p||d_q| <= (B-1) sum_p |d_p|^2`.

Hence

`(1/L) integral_I |P|^2 >= [1-2(B-1)/(L Delta)] sum_p |d_p|^2`.

The bound is independent of the interval location. Translation phases can line up destructively at selected frequencies, but once the interval length resolves their beat spacing, they cannot remain collectively small across the whole window unless the coefficient vector itself is small.

For `B=1`, the identity is exact with factor `1`.

## 3. Transfer to the Wang mixture

Apply the previous bound to

`P_k(xi)=sum_b S_(b,k) exp(-i b xi)`.

On `I subset [X,2X]`, the asymptotic reduction gives

`xi^k M(xi)=beta_k P_k(xi)+R_k(xi)`,

with

`sup_I |R_k| <= C_k/X`.

The reverse triangle inequality in `L^2(I)` yields

`RMS_I(xi^k M) >= |beta_k| RMS_I(P_k)-C_k/X`.

Combining with the phase-frame bound proves the claimed inequality.

When `L Delta >= 4(B-1)`, the bracket is at least `1/2`, giving the explicit phase-resolving lower bound.

## 4. Moving long windows recover the fiberwise moment obstruction

Assume the fixed bank satisfies

`sup_(xi in I_X)|M(xi)|=O(X^(-r))`

on a sequence `I_X subset [X,2X]` with `X->infinity` and `L_X Delta >= 4(B-1)`.

For `k=1`,

`RMS_(I_X)(xi M)=O(X^(1-r))->0`.

The order-one lower bound therefore forces every `S_(b,1)=0`.

Inductively, suppose all moments below order `k<r` vanish. Then

`RMS_(I_X)(xi^k M)=O(X^(k-r))->0`,

while the phase-resolving inequality forces

`sum_b |S_(b,k)|^2=0`.

Thus all fiber moments through order `r-1` vanish. `VIS-344`'s Vandermonde argument then applies inside each phase fiber: an active fiber producing order `r` needs at least `r` distinct scales.

So a moving-window construction is not a distinct asymptotic resource merely because the center of the window changes. For a fixed separated bank, a window longer than the reciprocal phase-resolution scale sees the same moment budget as the uniform tail.

## 5. What finite-window localization still leaves open

The result identifies the precise escape hatch rather than closing all nonuniform localization.

For a scale-dependent bank indexed by `X`, write `B_X` for the number of translations and `Delta_X` for their minimum spacing. A window can avoid the phase-resolution lower bound only if at least one of the following becomes material:

- `L_X Delta_X` stays comparable to or below `B_X`, so the window is shorter than the collective beat-resolution scale;
- translation frequencies cluster with `Delta_X->0`;
- coefficients/scales vary with `X` and the asymptotic remainder constant or coefficient norm becomes poorly conditioned;
- coefficients depend on frequency or on the source itself;
- the claimed gain is a signed estimate for `G`, rather than a small multiplier norm on a whole interval.

These are now quantitative obligations. A future packet argument cannot cite "moving windows" alone; it must specify which phase-resolution assumption fails and then control the cost of that failure.

## Prior-art audit

The interval lower bound is classical nonharmonic Fourier-series structure. A. E. Ingham, **Some trigonometrical inequalities with applications to the theory of series**, *Mathematische Zeitschrift* 41 (1936), 367–379, DOI `10.1007/BF01180426`, established the foundational gap inequalities comparing interval `L^2` norms of nonharmonic exponential sums with their coefficient `ell^2` norms. Modern literature refers to these as Ingham inequalities.

The estimate used here is deliberately more elementary and cruder than the general Ingham theorem: because only finitely many frequencies occur, direct integration plus the minimum-gap bound already gives the explicit factor `1-2(B-1)/(L Delta)`. No novelty is claimed for the harmonic-analysis inequality. The Mathia-specific content is its specialization to the successive inverse-frequency moment polynomials of Wang's exact multiplier and the resulting conclusion that sufficiently long moving windows recover the same phase-fiber cancellation constraints as the uniform-tail argument.

## Dependencies

- `VIS-333`: exact Wang multiplier `m(xi)`.
- `VIS-343`: asymptotic coefficients of pure Wang dilates and within-fiber Vandermonde cancellation.
- `VIS-344`: phase-fiber decomposition and the uniform-tail cancellation theorem.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue whose moving-window escape is narrowed here.

## Research consequence

The finite-window branch splits at an explicit phase-resolution scale. **For fixed separated translations, any sequence of windows long enough that `L Delta` dominates the number of phase fibers forces the same inverse-scale moment cancellations as uniform asymptotic smoothing.** Cross-phase interference can only remain a distinct mechanism on windows too short to resolve the translation gaps, in banks whose translations coalesce with scale, or through genuinely adaptive/source-coupled structure.

The next useful question is therefore no longer whether moving windows permit cancellation in principle. It is whether the normalized Chebyshev-theta remainder `G` supplies a mathematically controlled short-window or scale-dependent localization whose phase-spacing, coefficient-conditioning, signed-cancellation, and downstream derivative costs remain favorable.