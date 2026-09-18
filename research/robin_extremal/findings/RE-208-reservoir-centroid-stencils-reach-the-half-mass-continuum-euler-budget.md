# RE-208 — Reservoir-centroid stencils reach the half-mass continuum Euler budget

**Status:** `LITERATURE+DERIVED + CONTINUUM-VERTICAL-EULER + ADAPTIVE-CENTROID-MOMENTS + SHORT-INTERVAL-PNT + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + LOGARITHMIC-HEIGHT + KV-FIDELITY + INTEGER-MULTIPLICITIES`.

**Parent finding:** RE-207.

`RE-207` leaves one apparently arithmetic obstruction in the logarithmic-height continuum construction. The signed order-eight stencil cancels the *nominal* microbin locations, but the all-interval prime theorem only places each selected prime somewhere inside an interval of length `X^theta`. Treating every unknown within-bin displacement adversarially creates the first-order placement term

\[
Q^{\kappa+\theta-1+o(1)},
\]

which, with the current unconditional boundary `theta>17/30`, restricts the coefficient-variation exponent to `kappa<13/30`.

That first-order term is not intrinsic. Each short interval contains far more primes than a single stencil coefficient needs. Use those primes first as a **reservoir**, define the stencil on the empirical logarithmic centroids of the reservoirs, and only then choose the required subsets. Sampling without replacement gives a subset whose first centered moment is smaller than the interval diameter by a square-root population factor. The remaining centroid-level moments can be cancelled to any fixed order on the actual empirical nodes.

The consequence is that the short-interval location uncertainty ceases to be the active exponent barrier. Retain the continuum synthesis of `RE-205`--`RE-207`:

\[
T_Q=c\log Q,
\qquad
\epsilon_Q=Q^{-\rho},
\qquad
\kappa:=12H(\log 2)c+2\rho,
\qquad
H:=\log 8,
\]

and put

\[
d_Q:=\frac1{\sqrt Q\log Q}.
\]

Then for every fixed `c,rho>0` satisfying

\[
\boxed{\kappa<\frac12}
\tag{1}
\]

there is, for all sufficiently large `Q`, a finite ordinary-prime perturbation `c_q\in\{-1,+1\}` such that

\[
D_Q(s):=\sum_q c_q\log(1-q^{-s})^{-1}
\]

obeys

\[
\boxed{
\sup_{|t|\le c\log Q}|D_Q(1+it)|=o(d_Q).
}
\tag{2}
\]

Before the first remote repair cloud arrives, the local packet still has

\[
D_{Q,\mathrm{local}}(1)=\Theta(d_Q).
\tag{3}
\]

The perturbation uses only multiplicities `{0,1,2}` relative to the ordinary-prime baseline and, for every fixed `b>0`, satisfies

\[
|\Delta\vartheta(x)|=o\!\left(xe^{-bV(x)}\right),
\qquad
V(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\tag{4}
\]

through and beyond all affected scales.

Since `rho` can be taken arbitrarily small after `c`, (1) gives the explicit logarithmic-height range

\[
\boxed{
0<c<\frac1{24H\log2}
=0.0289079\ldots .
}
\tag{5}
\]

This replaces the `RE-207` sufficient range `kappa<13/30`. More importantly, every fixed `kappa<1/2` is now realizable. The value `1/2` is not claimed to be a source-rigidity threshold: it is the ceiling of the present **absolute-variation/KV realization**, because the repair uses at most `Q^{1/2+kappa+o(1)}` Chebyshev edit mass. Below `1/2` that is polynomially smaller than every fixed KV envelope; at the endpoint the automatic argument disappears.

## 1. Keep the continuum synthesis and choose a genuine short-interval exponent

Use the real spectral-gap synthesis already proved in `RE-204` and specialized at logarithmic height in `RE-205`. It gives `J=O(log Q)` remote shell centers

\[
X_j=X_0e^{L_j},
\qquad
X_0=2Q,
\qquad
H\le L_j\le L_{\max}=O_{c,\rho}(1),
\tag{6}
\]

and real coefficients `b_j` satisfying

\[
\sup_{|t|\le T_Q}
\left|1-\sum_{j=1}^{J}b_je^{-itL_j}\right|
\le Q^{-\rho},
\qquad
\sum_{j=1}^{J}|b_j|=:A_Q\le Q^{\kappa+o(1)}.
\tag{7}
\]

The adjacent `L_j` are separated by `asymp 1/log Q`.

Fix once and for all

\[
\frac{17}{30}<\theta<\frac35.
\tag{8}
\]

Guth--Maynard's uniform prime number theorem in intervals of length `x^theta` supplies, at every center used below,

\[
\#\{p\in[y,y+y^\theta]\}
=(1+o(1))\frac{y^\theta}{\log y}.
\tag{9}
\]

All centers remain within a fixed multiplicative neighborhood of `Q`, so choose a uniform reservoir size

\[
M_Q\asymp\frac{Q^\theta}{\log Q}
\tag{10}
\]

strictly below the prime count guaranteed in every microbin.

The load-bearing external input in this finding is therefore exactly the Guth--Maynard short-interval theorem already anchored in `SOURCES.md`; no stronger prime-localization statement is being assumed.

## 2. Reservoir centroids remove the adversarial first-order placement term

Fix a remote shell `j`. As in `RE-207`, its ideal population scale is

\[
N_j:=\left\lfloor |b_j|e^{L_j}B\right\rceil,
\qquad
B\asymp\frac{\sqrt Q}{\log Q}.
\tag{11}
\]

We will distribute these edits across many short prime bins, but unlike `RE-207` the moment stencil is defined only *after* the prime reservoirs have been seen.

Let `r>=2` be a fixed integer to be chosen later. Take a large constant `C_r` and define the logarithmic spacing

\[
h_Q:=C_rQ^{\theta-1}.
\tag{12}
\]

For shell `j`, set

\[
R_j:=\max\left\{R_r,
\left\lceil C_r\frac{N_j}{M_Q}\right\rceil
\right\},
\tag{13}
\]

where `R_r` is a sufficiently large constant depending only on `r`. Around the nominal log-locations `k h_Q`, `-R_j\le k\le R_j`, take mutually disjoint one-sided physical intervals of length `asymp Q^theta`. Choosing `C_r` large makes neighboring intervals disjoint. From each interval choose exactly `M_Q` primes as a reservoir `\mathcal P_{j,k}`.

For each reservoir define its empirical logarithmic centroid relative to `X_j` by

\[
\bar u_{j,k}
:=\frac1{M_Q}
\sum_{q\in\mathcal P_{j,k}}
\log\frac q{X_j}.
\tag{14}
\]

Since every reservoir lies inside one short interval,

\[
\bar u_{j,k}
=k h_Q+O(Q^{\theta-1}).
\tag{15}
\]

Normalize by the cloud width:

\[
x_{j,k}:=\frac{\bar u_{j,k}}{R_jh_Q}
=\frac{k}{R_j}+O_r\!\left(\frac1{R_j}\right).
\tag{16}
\]

By increasing `C_r` first and then `R_r`, these are uniformly quasi-uniform nodes on a fixed interval.

Now form the fixed-dimensional empirical Gram matrix

\[
G_j(a,b)
:=\frac1{R_j}
\sum_{k=-R_j}^{R_j}x_{j,k}^{a+b},
\qquad 0\le a,b<r.
\tag{17}
\]

For the exact uniform grid this converges to the positive-definite monomial Gram matrix on `[-1,1]`; the perturbation in (16) is uniformly small. Hence `G_j^{-1}` is bounded by a constant depending only on `r`. Solve

\[
G_j\alpha_j=e_0,
\qquad
P_j(x):=\sum_{a=0}^{r-1}\alpha_{j,a}x^a,
\qquad
w_{j,k}:=\frac1{R_j}P_j(x_{j,k}).
\tag{18}
\]

Then, **on the actual empirical centroids**, not on nominal bin centers,

\[
\sum_k w_{j,k}=1,
\qquad
\sum_k w_{j,k}\bar u_{j,k}^m=0
\quad(1\le m<r),
\tag{19}
\]

and uniformly

\[
|w_{j,k}|\ll_r R_j^{-1},
\qquad
\sum_k|w_{j,k}|\ll_r1.
\tag{20}
\]

This removes the circularity that would arise from trying to recenter a stencil *after* its edit counts were chosen: the reservoirs are fixed first, their centroids are measured second, and only then are the weights and edit counts defined.

Set

\[
n_{j,k}:=\left\lfloor N_j|w_{j,k}|\right\rceil.
\tag{21}
\]

The choice (13), with a sufficiently generous constant, ensures `n_{j,k}\le M_Q` for every `j,k`.

The final step is to avoid paying the full reservoir diameter when choosing `n_{j,k}` actual primes. For a reservoir with logarithmic deviations

\[
e_q:=\log(q/X_j)-\bar u_{j,k},
\qquad
\sum_{q\in\mathcal P_{j,k}}e_q=0,
\qquad
|e_q|\ll Q^{\theta-1},
\tag{22}
\]

choose a uniformly random subset of size `n=n_{j,k}`. Sampling without replacement gives

\[
\mathbb E\left|\sum_{q\in S}e_q\right|^2
\le n\max_q|e_q|^2.
\tag{23}
\]

Therefore at least one deterministic subset satisfies

\[
\boxed{
\left|\sum_{q\in S_{j,k}}e_q\right|
\ll Q^{\theta-1}\sqrt{n_{j,k}}.
}
\tag{24}
\]

Use such a subset. Give all its primes the sign prescribed by `-sgn(b_j)sgn(w_{j,k})`; a positive coefficient duplicates an ordinary prime and a negative coefficient deletes it. Distinct microbins guarantee no prime is reused, so every final multiplicity remains in `{0,1,2}`.

Equation (24) is the new arithmetic gain. `RE-207` bounded the first centered moment by `n Q^{theta-1}`. Reservoir selection replaces `n` by `sqrt(n)`.

## 3. Uniform Euler error of one empirical cloud

Let

\[
s=1+it,
\qquad |t|\le T_Q,
\qquad
\delta_Q:=Q^{\theta-1}.
\tag{25}
\]

Since `T_Q\delta_Q=o(1)`, Taylor expansion around the empirical centroid gives, for the selected subset in one microbin,

\[
\sum_{q\in S_{j,k}}
 e^{-s\log(q/X_j)}
=
 e^{-s\bar u_{j,k}}
\left(
 n_{j,k}
 -s\sum_{q\in S_{j,k}}e_q
 +O(n_{j,k}|s|^2\delta_Q^2)
\right).
\tag{26}
\]

There are three errors to control.

First, replace the integer signed count by the ideal value `N_jw_{j,k}`. The error is at most one atom per microbin, hence `O(R_j)` atoms per cloud.

Second, the first centered moment in (26) contributes at most

\[
\ll T_Q\delta_Q
\sum_k\sqrt{n_{j,k}}
\ll_r T_Q\delta_Q\sqrt{R_jN_j},
\tag{27}
\]

using Cauchy--Schwarz and (20). The quadratic within-bin remainder is

\[
\ll_r N_jT_Q^2\delta_Q^2+O(R_jT_Q^2\delta_Q^2).
\tag{28}
\]

Third, the ideal centroid measure has exact moments (19). Put

\[
\Delta_j:=R_jh_Q+O(\delta_Q).
\tag{29}
\]

Then (19)--(20) and the Taylor remainder yield

\[
\sum_k w_{j,k}e^{-s\bar u_{j,k}}
=1+O_r((T_Q\Delta_j)^r).
\tag{30}
\]

From (10)--(13),

\[
\Delta_j
\ll_r
Q^{\theta-1}
+|b_j|Q^{-1/2+o(1)}.
\tag{31}
\]

Because `kappa<1/2`, this is `o(1/log Q)` uniformly. Thus every microcloud is much narrower than the `asymp1/log Q` spacing between the continuum-synthesis centers `L_j`, and all clouds can be chosen disjoint.

## 4. The global error budget is below selector scale for every fixed kappa<1/2

Normalize every first-harmonic error by `d_Q\asymp B/X_0`. The centroid-stencil remainder (30) contributes

\[
\sum_j |b_j|(T_Q\Delta_j)^r
\ll
Q^{\kappa+r(\theta-1)+o(1)}
+
Q^{(r+1)\kappa-r/2+o(1)}.
\tag{32}
\]

For a prescribed fixed `kappa<1/2`, choose the fixed moment order `r` so large that

\[
\boxed{
\kappa<r(1-\theta),
\qquad
(r+1)\kappa<\frac r2.
}
\tag{33}
\]

Such an `r` always exists because `theta<3/5` and `kappa<1/2`. Both terms in (32) are then `o(1)`.

The integer-count error contributes, exactly as in `RE-207`,

\[
\frac1B\sum_jR_j
\ll
Q^{\kappa-\theta+o(1)}+Q^{-1/2+o(1)}
=o(1),
\tag{34}
\]

because `kappa<1/2<theta`.

For the new reservoir-selection term (27), split clouds according as the second term in (13) is active. On the large-population clouds,

\[
R_j\asymp \frac{N_j}{M_Q},
\]

so their aggregate normalized first-moment error is

\[
\ll
T_Q\delta_Q\frac{A_Q}{\sqrt{M_Q}}
=
Q^{\kappa+\theta/2-1+o(1)}
=o(1).
\tag{35}
\]

On the bounded-`R_j` clouds, Cauchy--Schwarz over the `O(log Q)` synthesis shells gives

\[
\ll
T_Q\delta_Q B^{-1/2}
\sum_j\sqrt{|b_j|}
\ll
Q^{\kappa/2+\theta-5/4+o(1)}
=o(1).
\tag{36}
\]

Both inequalities are uniform for every `kappa<1/2` because `theta<3/5`. The quadratic within-bin term (28) contributes

\[
\ll
A_QT_Q^2\delta_Q^2
+
 o(1)
=
Q^{\kappa+2\theta-2+o(1)}
+o(1)
=o(1).
\tag{37}
\]

The small extra terms coming from the `O(R_j)` rounding populations are already dominated by (34).

The local packet can be chosen from one short interval near `X_0`. Its logarithmic diameter is `O(delta_Q)`, so replacing it by the ideal point packet costs only `O(T_Q delta_Q)d_Q=o(d_Q)`.

Finally, on `Re s=1`, replacing the exact Euler atom

\[
\log(1-q^{-s})^{-1}
\]

by its first harmonic `q^{-s}` costs `O(q^{-2})` per edited prime. Since the total selected population is

\[
\ll BA_Q+\sum_jR_j
=Q^{1/2+\kappa+o(1)},
\tag{38}
\]

the aggregate prime-power remainder, relative to `d_Q`, is

\[
Q^{\kappa-1+o(1)}=o(1).
\tag{39}
\]

Combining the continuum synthesis error `Q^{-rho}`, (32), (34)--(37), the local placement error and (39) proves (2).

## 5. Selector debt and KV fidelity survive unchanged

The first remote synthesis center satisfies `L_j>=H=log8`. The local packet is centered near `2Q`, while the remote clouds remain `o(1)` in logarithmic width. Hence there is a fixed multiplicative interval after the local edit and before the first remote repair on which

\[
D_{Q,\mathrm{local}}(1)
=(1+o(1))\frac{B}{2Q}
=\Theta(d_Q),
\tag{40}
\]

which is the same selector-scale transient used throughout `RE-203`--`RE-207`.

For Chebyshev fidelity we do not rely on cancellation. The absolute logarithmic edit mass over all affected primes is, from (38),

\[
Q^{1/2+\kappa+o(1)}.
\tag{41}
\]

If `kappa<1/2`, then for every fixed `b>0`,

\[
Q^{1/2+\kappa+o(1)}
=o\!\left(Qe^{-bV(Q)}\right),
\tag{42}
\]

because `e^{bV(Q)}=Q^{o(1)}` while `Q^{1/2-kappa}` is a fixed positive power. All edited shells lie within a fixed multiplicative neighborhood of `Q`, so the same estimate controls every partial excursion through the construction and the final tail. This proves (4).

The mechanism therefore reaches every `kappa<1/2` without asking for primes in intervals shorter than the current unconditional all-`x` theorem. The old `13/30` wall was not the short-interval theorem itself; it came from paying the full interval diameter independently for every edited prime.

## 6. Prior-art and novelty audit

The external arithmetic input is the already anchored Guth--Maynard theorem, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics **203** (2026), 623--675, whose short-interval consequence gives the PNT uniformly for every fixed `theta>17/30`. A fresh prior-art check confirms the same boundary; Gafni--Tao also summarize the consequence as an all-`x` short-interval PNT for `theta>17/30`. No stronger short-interval theorem is used here.

The two additional ingredients are elementary and are derived above rather than imported as black boxes: fixed-dimensional moment fitting on a quasi-uniform empirical grid is finite linear algebra, and (23)--(24) is the variance identity for sampling without replacement plus the probabilistic method. Searches around signed quadrature, empirical-node moment fitting, and subset-centroid discrepancy found only generic approximation/discrepancy machinery, not this prime-Euler matched-control construction. No new load-bearing literature dependency is therefore added to `SOURCES.md`.

The line-specific content is the coupling of four pieces: short-interval prime reservoirs, empirical-centroid moment cancellation, square-root subset-centroid selection, and the existing logarithmic-height Euler continuum synthesis. That coupling removes the location term that was load-bearing in `RE-207` and makes the coefficient-variation budget, rather than current prime localization, the active constraint.

## 7. Adversarial self-review and surviving boundary

The most important possible failure is circularity: if the stencil weights were chosen from centroids that themselves depended on the final subset sizes, (19) would not define a legitimate construction. The reservoir order above avoids this. Each full reservoir and its centroid are fixed before the moment system is solved; only afterward is a subset of the required cardinality extracted from that fixed reservoir.

A second concern is that centering only a count measure might ignore the reciprocal factor present in Euler data. Equation (26) expands the complete first harmonic `e^{-s log(q/X_j)}` with `s=1+it`; the real damping and vertical phase are handled simultaneously. The small first centered moment is therefore the correct first-order quantity, not merely a geometric surrogate.

A third concern is the large fixed moment order needed as `kappa` approaches `1/2`. This is harmless for the stated theorem: `kappa` is fixed before `Q->infinity`, so `r`, `C_r`, `R_r` and all Gram-matrix constants are fixed. The result does **not** claim uniformity as `kappa=kappa(Q)->1/2`.

Finally, the endpoint `kappa=1/2` is not proved coercive. The construction only stops being automatically KV-small there because the absolute edit mass in (41) reaches `Q^{1+o(1)}`. More elaborate interleaving or source-side cancellation could in principle cross that ceiling. Thus the new frontier is precise:

\[
\boxed{
\text{all fixed }\kappa<1/2\text{ are continuum-Euler noncoercive by honest prime controls;}
}
\]

but the half-mass endpoint and any genuinely source-native obstruction remain open.

This also changes the next useful experiment. Improving the unconditional short-interval exponent below `17/30` would no longer enlarge the present fixed-`kappa<1/2` range. To obtain a new obstruction one must instead show that a real Robin/CA source cannot spend `Q^{1/2+\kappa}` bounded-multiplicity edits with the freedom used here, or identify an observable whose cost is not reducible by reservoir averaging and finite moment fitting.