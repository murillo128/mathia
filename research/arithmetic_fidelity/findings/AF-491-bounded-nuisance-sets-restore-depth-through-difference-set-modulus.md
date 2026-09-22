# AF-491 — Bounded nuisance sets restore depth through a difference-set modulus

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `BOUNDED-NUISANCE`, `MINIMAX-RESOLUTION`, `DIFFERENCE-SET`, `DIRICHLET-SAMPLING`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-490 shows that an **unrestricted linear nuisance** quotients away every discriminator component parallel to the nuisance subspace. Bounded nuisance behaves differently: once the nuisance has exhausted its finite excursion, absolute signal depth becomes informative again.

Let `Y` be a finite-dimensional normed real vector space, let `s in Y` be nonzero, let `K subset Y` be a nonempty compact nuisance set, and observe

\[
y=v-\theta s+u,
\qquad v\in K,
\qquad \|u\|\le \rho.
\]

Define the difference-set separation profile

\[
d_K(\delta;s):=\operatorname{dist}(\delta s,K-K),
\qquad \delta\ge0,
\]

and the largest target displacement that the nuisance plus radius-`rho` noise can still hide,

\[
\Delta_K(\rho;s)
:=
\max\{\delta\ge0:d_K(\delta;s)\le2\rho\}.
\]

Then the deterministic minimax worst-case absolute error for estimating `theta` is exactly

\[
\boxed{R^*(K,s,\rho)=\frac12\Delta_K(\rho;s).}
\]

Thus bounded-nuisance fidelity is governed not by the quotient norm of AF-490 but by the **one-dimensional escape profile of the discriminator ray through the nuisance difference set**. The unrestricted-subspace theorem is the homogeneous limit in which `K-K` contains an entire nuisance direction; a compact nuisance can absorb only a finite amount of that direction.

For bounded log-amplitude uncertainty this produces a sharp crossover. In `ell_infinity`, a fixed-width sample window first behaves like the unrestricted-amplitude quotient of AF-490, with recovery controlled only by sample spread. After sufficient common translation to the right, the finite amplitude budget saturates and the minimax error decays as inverse absolute depth.

## Exact bounded-nuisance minimax theorem

For an observation `y`, let

\[
\Theta(y)
=
\{\theta:\exists v\in K,\ \exists u,\ \|u\|\le\rho,
\ y=v-\theta s+u\}
\]

be the feasible target set.

Take any two feasible targets `theta_0,theta_1` for the same datum. Their witnesses satisfy

\[
y=v_j-\theta_j s+u_j,
\qquad v_j\in K,
\qquad \|u_j\|\le\rho.
\]

Subtracting gives

\[
(\theta_1-\theta_0)s-(v_1-v_0)=u_1-u_0.
\]

Since `K-K` is symmetric,

\[
d_K(|\theta_1-\theta_0|;s)
\le
\|u_1-u_0\|
\le2\rho.
\]

Therefore every feasible target set has diameter at most `Delta_K(rho;s)`. The midpoint of its extremal target values consequently has worst-case error at most `Delta_K/2`.

For the reverse inequality, compactness of `K-K` makes `d_K(delta;s)` continuous and attained, while boundedness of `K-K` and `s!=0` imply `d_K(delta;s)->infinity` as `delta->infinity`. Hence the defining set for `Delta_K` is compact and its maximum is attained. Choose `v_0,v_1 in K` such that

\[
\|\Delta_K s-(v_1-v_0)\|
=d_K(\Delta_K;s)
\le2\rho.
\]

The two noiseless centers corresponding to targets separated by `Delta_K` are therefore at distance at most `2rho`. Their midpoint lies in both closed radius-`rho` noise balls. One datum is compatible with two targets separated by `Delta_K`, so every estimator incurs error at least `Delta_K/2` on one of them.

Combining both directions proves

\[
R^*(K,s,\rho)=\frac12\Delta_K(\rho;s).
\]

No convexity of `K` is required. The only nuisance geometry relevant to two-point indistinguishability is the difference set `K-K`.

## Coarse bounded-diameter law

Let

\[
D:=\operatorname{diam}(K).
\]

Because `0 in K-K` and every element of `K-K` has norm at most `D`,

\[
\delta\|s\|-D
\le
 d_K(\delta;s)
\le
\delta\|s\|.
\]

The exact theorem immediately yields

\[
\boxed{
\frac{\rho}{\|s\|}
\le
R^*(K,s,\rho)
\le
\frac{D+2\rho}{2\|s\|}.}
\]

Thus any nuisance family with uniformly bounded diameter restores the raw inverse-sensitivity scale `1/||s||` up to constants. This is qualitatively different from an unrestricted nuisance subspace, where the parallel component of `s` can be removed at arbitrary magnitude and only the quotient norm survives.

The distinction is therefore not simply “nuisance versus no nuisance.” The relevant question is whether the nuisance **difference set remains bounded along the discriminator ray**.

## Exact capped log-amplitude crossover in `ell_infinity`

Consider the logarithmic single-exponential channel from AF-490, but restrict the unknown log-amplitude to a finite interval:

\[
z_i=\alpha-\theta s_i+u_i,
\qquad
\alpha\in[A,B],
\qquad
\|u\|_\infty\le\rho,
\]

with positive sample locations `s_i`. Put

\[
L:=B-A,
\qquad
a:=\min_i s_i,
\qquad b:=\max_i s_i,
\]

and define midpoint and half-span

\[
m:=\frac{a+b}{2},
\qquad
h:=\frac{b-a}{2}.
\]

Here

\[
K-K=\{c\mathbf1:|c|\le L\}.
\]

For `delta>=0`, the coordinates of `delta s` fill an interval whose extreme values are `delta a` and `delta b`. The best admissible constant is the projection of their midpoint `delta m` onto `[-L,L]`. Therefore

\[
\boxed{
d_K(\delta;s)
=
\delta h+(\delta m-L)_+.}
\]

Assume first `h>0`. Solving `d_K(delta;s)<=2rho` gives two exact regimes.

If

\[
2\rho m\le Lh,
\]

then the amplitude cap is not reached at the minimax collision scale and

\[
\Delta_K=\frac{2\rho}{h},
\qquad
\boxed{R^*=\frac{\rho}{h}
=\frac{2\rho}{b-a}.}
\]

This is precisely the **transverse-spread** law of the unrestricted-amplitude quotient: common depth contributes nothing because the bounded nuisance is still wide enough to absorb the relevant target displacement.

If instead

\[
2\rho m\ge Lh,
\]

then the amplitude budget saturates before the worst indistinguishable target displacement is reached. The root lies in the second affine piece and

\[
\Delta_K=\frac{L+2\rho}{b},
\qquad
\boxed{R^*=\frac{L+2\rho}{2b}.}
\]

At equality the two formulas coincide. If `h=0`, there is no transverse spread and only the capped-depth regime remains:

\[
R^*=\frac{L+2\rho}{2b}.
\]

The limiting cases are consistent. When `L=0` the amplitude is known and `R^*=rho/b`, the raw `ell_infinity` sensitivity law. When amplitude is unrestricted, `L` is effectively infinite and the spread-only regime persists forever, recovering AF-490.

## Translation of a fixed-width sampling window

Let

\[
s_i=t+r_i
\]

with fixed offsets `r_i` and let `t->infinity`. Then `h` is fixed, while

\[
m=t+O(1),
\qquad
b=t+O(1).
\]

For every fixed finite `L`, fixed `rho>0`, and nonzero span `h`, the crossover condition eventually enters

\[
2\rho m\ge Lh.
\]

Hence

\[
\boxed{
R^*(t)
=
\frac{L+2\rho}{2(t+r_{\max})}
\sim
\frac{L+2\rho}{2t}.}
\]

So **bounded amplitude uncertainty restores inverse-depth recovery after a sharp finite crossover**. AF-490's translation invariance is not robust to imposing a fixed amplitude range: it is a singular consequence of allowing the nuisance direction unlimited excursion.

For an actual amplitude constraint `a_amp in [a_-,a_+]`, the logarithmic nuisance width is

\[
L=\log(a_+/a_-).
\]

The theorem is exact for additive log-noise. Under bounded source-relative multiplicative noise, taking logarithms again gives a constant-factor transfer as in AF-490; no exact multiplicative-noise constant is claimed here.

## Compression interpretation

The exact formula supplies a three-level fidelity distinction:

1. **Known nuisance value:** the nuisance difference set is `{0}` and all of the discriminator norm is usable.
2. **Bounded nuisance:** the difference set can mask finite displacements, but the discriminator ray eventually escapes it; large depth becomes informative again.
3. **Unrestricted linear nuisance:** the difference set contains an entire subspace, so any discriminator component in that subspace is permanently quotiented out and no amount of common translation restores it.

This makes the geometry of the admissible nuisance class itself a fidelity resource. Passing from a bounded source class to its linear span is not an innocuous simplification: it can change the asymptotic experiment from depth-sensitive to depth-invariant.

## Falsification and boundary audit

- The exact theorem assumes a finite-dimensional normed observation space, compact nuisance set `K`, and deterministic norm-bounded noise. Compactness is used to make the worst indistinguishable displacement attained; the unrestricted-subspace case remains covered separately by AF-490.
- `diam(K)` alone gives only the coarse inverse-norm bounds. Exact constants depend on how `K-K` intersects the discriminator ray, not merely on its diameter.
- The `ell_infinity` crossover formula assumes all sample locations are positive and the nuisance is exactly one bounded common offset in log coordinates.
- A bounded prior support is being treated adversarially, not probabilistically. Bayesian amplitude priors or stochastic noise define different experiments and need not obey the same minimax law.
- The restoration of depth is a parameter-recovery statement, not an arithmetic-provenance theorem. Nothing here distinguishes rational primes from the matched generalized-prime controls of AF-483/AF-484.
- A nuisance family can be unbounded without containing the full discriminator direction, or bounded in some coordinates but not others. The decisive object is `dist(delta s,K-K)`, so crude bounded/unbounded labels should not replace the exact difference-set test.

## Prior-art and novelty audit

The minimax and feasible-set backbone is classical. No broad novelty is claimed for optimal recovery under bounded deterministic error.

- C. A. Micchelli, T. J. Rivlin, and S. Winograd, **“The Optimal Recovery of Smooth Functions,”** *Numerische Mathematik* 26, 191–200 (1976), is classical optimal-recovery prior art for worst-case reconstruction from imperfect information.
- David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *Annals of Statistics* 22(1), 238–270 (1994), DOI `10.1214/aos/1176325367`, develops the minimax/modulus-of-continuity connection between statistical estimation and deterministic optimal recovery.
- Hélène Piet-Lahanier and Eric Walter, **“Exact Description of Feasible Parameter Sets and Minimax Estimation,”** *International Journal of Adaptive Control and Signal Processing* 8, 5–14 (1994), DOI `10.1002/acs.4480080102`, is direct set-membership prior art for affine parameter models with bounded errors and exact minimax estimation from feasible parameter geometry.

The durable Arithmetic Fidelity contribution here is the specialization that exposes the **difference-set escape modulus** as the surviving discriminator after bounded nuisance, and its comparison with AF-490's quotient norm. The capped-amplitude corollary makes the distinction explicit: a fixed-width experiment has a sharp spread-controlled regime followed by a depth-controlled regime, whereas the unrestricted nuisance span erases the latter forever.

## Relationship to AF-487–AF-490

AF-487–AF-489 quantified recovery when the moving atom's amplitude is fixed. AF-490 then showed that promoting amplitude to an unrestricted nuisance removes common depth and replaces raw sensitivity by transverse spread.

AF-491 closes the first structured-nuisance escape left open by AF-490. A finite amplitude range does **not** inherit exact translation invariance. Its difference set can absorb common depth only up to a finite budget, after which the discriminator ray exits the nuisance set and inverse-depth recovery returns. The correct hierarchy is therefore

\[
\text{raw sensitivity}
\;\longrightarrow\;
\text{difference-set escape under bounded nuisance}
\;\longrightarrow\;
\text{quotient sensitivity under unrestricted nuisance}.
\]

This separates three mathematically different resources that should not be conflated in later arithmetic applications: observation depth, transverse sampling geometry, and admissible nuisance excursion.