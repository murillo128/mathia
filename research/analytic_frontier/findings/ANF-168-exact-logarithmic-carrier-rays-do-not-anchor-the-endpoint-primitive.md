# ANF-168 — exact logarithmic carrier rays do not anchor the endpoint primitive

**Status:** `EXACT-DERIVED + MATCHED-INFORMATION-CONTROL + EXACT-LOG-CARRIER-RAY + TWO-SIDED-LOCAL-MOMENT-BUDGET + ENDPOINT-CHARGE-PERSISTENCE`. `ANF-166` and `ANF-167` show that arbitrary fixed logarithmic cancellation on every interval above the current activation length, even together with the correct moving diagonal and two-sided local `L^1/L^2` activity, does not control the absolute endpoint primitive. Their matched controls leave one conspicuous source-side escape: after the distinguished twist is restored, the actual coefficients have the rigid form

\[
b_n=r_X(X+n)(X+n)^{-iU},
\qquad r_X(X+n)\in\mathbb R,
\tag{1}
\]

so each complex coefficient lies on a prescribed logarithmic carrier ray. The synthetic controls in `ANF-166`--`ANF-167` did not enforce this pointwise phase constraint.

That escape can be closed. For every fixed height window `A X^2<=U<=B X^2` and every bow scale in the current difficult range, there exist **real** weights `w_n` such that

\[
b_n=w_n(X+n)^{-iU}
\tag{2}
\]

satisfies simultaneously the exact carrier-ray constraint, exact global centering, the bow diagonal scale, the pointwise `O(log X)` envelope, two-sided local `L^1/L^2` activity on every currently controlled interval, and stronger-than-every-fixed-log interval cancellation, while its endpoint completion still has size `asymp X K log X`.

The construction uses three pieces. A tiny real edge bias is signed against the exact carrier so that it stores a complex charge of size `sqrt(X log X)`. A sparse real Rademacher calibrator, multiplied by the same exact carrier, supplies the required local and global quadratic mass while all of its interval sums are only square-root size. Finally a diffuse real correction in the full-incidence region enforces exact complex centering. `ANF-161` supplies the only nontrivial geometric input needed for that correction: on a macroscopic block, the doubled logarithmic carrier has vanishing normalized vector sum, so its real two-dimensional Gram matrix is uniformly invertible.

Consequently **carrier phase rigidity and reality of the pre-demodulated coefficients are not the missing endpoint anchor**. The remaining source-side theorem must use the arithmetic law of the real amplitudes themselves: prime/rough placement, the fixed positive-prime versus negative-rough amplitude alphabet, or a correlation consequence of that law.

## 1. Bow geometry and the exact carrier-ray constraint

Use the integer moving-window geometry of `ANF-157`. Let

\[
N=X,\qquad M=N+K-1,
\tag{3}
\]

where `X` is an integer tending to infinity and

\[
K=X^{1-2\varepsilon+o(1)},
\qquad 0<\varepsilon<\frac1{16}.
\tag{4}
\]

Fix constants

\[
0<A<B<\infty,
\qquad
AX^2\le U\le BX^2.
\tag{5}
\]

For `1<=n<=M` put

\[
m_n:=X+n,
\qquad
v_n:=m_n^{-iU},
\qquad |v_n|=1.
\tag{6}
\]

Thus a coefficient vector respects the exact distinguished logarithmic carrier whenever

\[
\boxed{b_n=w_nv_n\quad\text{with }w_n\in\mathbb R.}
\tag{7}
\]

Choose the same all-interval activation scale used in `ANF-166`--`ANF-167`,

\[
H_0=X^{5/8+\eta},
\tag{8}
\]

with fixed `eta>0` small enough that `H_0=o(K)`; for direct comparison with `ANF-165` one may take

\[
0<\eta<\frac{1-16\varepsilon}{24}.
\tag{9}
\]

Fix a sufficiently small constant `delta>0` and set

\[
a_X:=\sqrt{\delta X\log X}.
\tag{10}
\]

The target is to keep a left endpoint primitive at least of order `a_X` for `Theta(K)` prefix lengths while preserving all of the aggregate information already known to be insufficient.

## 2. The exact carrier can always be signed to charge one endpoint

Consider the first `H_0` carrier directions `v_1,...,v_{H_0}`. For every angle `theta`,

\[
\sum_{n\le H_0}
|\operatorname{Re}(e^{-i\theta}v_n)|
\tag{11}
\]

is nonnegative. Averaging in `theta` and using

\[
\frac1{2\pi}\int_0^{2\pi}|\cos\theta|\,d\theta
=\frac2\pi
\tag{12}
\]

gives some `theta=theta_X` for which

\[
\sum_{n\le H_0}
|\operatorname{Re}(e^{-i\theta_X}v_n)|
\ge \frac2\pi H_0.
\tag{13}
\]

Choose signs

\[
\sigma_n
:=\operatorname{sgn}\operatorname{Re}(e^{-i\theta_X}v_n)
\in\{-1,1\},
\tag{14}
\]

with either sign allowed when the real part vanishes, and define the real edge weights

\[
e_n=
\begin{cases}
q_X\sigma_n,&1\le n\le H_0,\\
0,&n>H_0,
\end{cases}
\qquad
q_X:=\frac{\pi a_X}{2H_0}.
\tag{15}
\]

Their carrier-modulated total charge is

\[
E_X:=\sum_{n=1}^{H_0}e_nv_n.
\tag{16}
\]

By (13)--(15),

\[
\operatorname{Re}(e^{-i\theta_X}E_X)
=q_X
\sum_{n\le H_0}|\operatorname{Re}(e^{-i\theta_X}v_n)|
\ge a_X,
\tag{17}
\]

and therefore

\[
\boxed{|E_X|\ge a_X.}
\tag{18}
\]

At the same time there is no hidden large coefficient. From (8), (10), and (15),

\[
q_X
\asymp
X^{-1/8-\eta}\sqrt{\log X}
=o_A((\log X)^{-A})
\tag{19}
\]

for every fixed `A>0`. Every interval sees at most the total variation of the charging block,

\[
\boxed{
\left|\sum_{n\in I}e_nv_n\right|
\le q_XH_0
=\frac\pi2 a_X.
}
\tag{20}
\]

Thus the prescribed carrier directions do not prevent a tiny **real** source perturbation from storing the critical absolute charge. The signs in (14) simply select, at each site, which of the two allowed directions on the carrier ray contributes positive projection onto a common axis.

This is deliberately not yet source-faithful to `r_X`: the actual prime-minus-rough amplitudes do not offer arbitrary `+-q_X` choices. The point is to isolate the information value of the carrier-ray condition itself.

## 3. A carrier-faithful random calibrator supplies local and global mass

Let

\[
L:=\lceil\log X\rceil
\tag{21}
\]

and let

\[
\mathcal G:=\{jL:1\le j\le J\},
\qquad
J:=\lfloor M/L\rfloor.
\tag{22}
\]

Choose independent Rademacher signs `epsilon_j in {-1,1}` and define real calibrator weights

\[
c_{jL}:=L\epsilon_j,
\qquad
c_n:=0\quad(n\notin\mathcal G).
\tag{23}
\]

A standard probabilistic estimate is enough; no discrepancy theorem is needed. Fix a consecutive block of `m` grid points. For either real coordinate of

\[
\sum \epsilon_jv_{jL},
\tag{24}
\]

Hoeffding's elementary exponential-moment argument gives

\[
\mathbb P\left(
\left|\sum \epsilon_j\operatorname{Re}v_{jL}\right|\ge t
\right)
\le 2e^{-t^2/(2m)},
\tag{25}
\]

and the same bound for the imaginary coordinate. Hence

\[
\mathbb P\left(
\left|\sum \epsilon_jv_{jL}\right|
\ge 4\sqrt{m\log X}
\right)
\le 4X^{-4}.
\tag{26}
\]

There are fewer than `X^2` consecutive grid blocks. A union bound therefore shows that, for all sufficiently large `X`, there exists one deterministic signing for which **every** consecutive grid block of `m>=1` points satisfies

\[
\boxed{
\left|\sum \epsilon_jv_{jL}\right|
\le4\sqrt{m\log X}.
}
\tag{27}
\]

Fix such a signing from now on. Any contiguous physical interval `I` of length `H` intersects a consecutive grid block with

\[
m\le H/L+2.
\tag{28}
\]

Multiplying (27) by `L` gives the uniform carrier-faithful interval bound

\[
\boxed{
\left|\sum_{n\in I}c_nv_n\right|
\ll \sqrt H\,\log X+(\log X)^{3/2}.
}
\tag{29}
\]

The same construction provides the mass normalization deterministically, because signs and carrier phases do not change moduli. Every interval of length `H>=H_0` contains

\[
\frac HL+O(1)
\tag{30}
\]

grid points. Consequently

\[
\sum_{n\in I}|c_n|
=H+O(L),
\qquad
\sum_{n\in I}|c_n|^2
=HL+O(L^2).
\tag{31}
\]

Thus the calibrator already has the local `L^1` and `L^2` orders needed by `ANF-167`, now while obeying the exact pointwise logarithmic carrier.

## 4. Macroscopic carrier curvature gives an exact real centering correction

The preliminary vector `c+e` need not have zero total complex sum. We can impose exact centering without touching either endpoint region and without leaving the carrier rays.

For sufficiently large `X`, `K=o(X)`. Choose a fixed central block

\[
\mathcal J
:=\{n:\lfloor N/3\rfloor\le n\le\lfloor2N/3\rfloor\}.
\tag{32}
\]

It lies inside the full-incidence region `K<=n<=N`, and therefore it contributes to neither prefix nor suffix in `E_\partial` for lengths `r<K`.

Write

\[
u_n:=(\operatorname{Re}v_n,\operatorname{Im}v_n)\in\mathbb R^2
\tag{33}
\]

and form the two-dimensional Gram matrix

\[
G_X:=\sum_{n\in\mathcal J}u_nu_n^{\mathsf T}.
\tag{34}
\]

For every unit vector `(cos theta,sin theta)`,

\[
\sum_{n\in\mathcal J}
\operatorname{Re}(e^{-i\theta}v_n)^2
=
\frac{|\mathcal J|}{2}
+
\frac12\operatorname{Re}
\left(e^{-2i\theta}\sum_{n\in\mathcal J}v_n^2\right).
\tag{35}
\]

Hence

\[
\lambda_{\min}(G_X)
=
\frac12\left(
|\mathcal J|-\left|\sum_{n\in\mathcal J}v_n^2\right|
\right).
\tag{36}
\]

Now

\[
v_n^2=(X+n)^{-2iU}.
\tag{37}
\]

The block `mathcal J` has length `asymp X`, its physical base point is `asymp X`, and `2U` remains in a fixed `asymp X^2` height window. The uniform supercubic carrier estimate of `ANF-161`, applied with the doubled height, therefore gives

\[
\left|\sum_{n\in\mathcal J}v_n^2\right|=o(X).
\tag{38}
\]

It follows that

\[
\boxed{G_X\succeq cX I_2}
\tag{39}
\]

for some constant `c=c(A,B)>0` and all sufficiently large `X`.

Let

\[
Z_X:=\sum_{n=1}^{M}(c_n+e_n)v_n.
\tag{40}
\]

Taking `I=[1,M]` in (29), and using (20), yields

\[
|Z_X|\ll \sqrt X\log X.
\tag{41}
\]

Identify `Z_X` with its vector in `R^2`. For `n in mathcal J`, define the real correction

\[
d_n:=-u_n^{\mathsf T}G_X^{-1}Z_X,
\qquad
d_n:=0\quad(n\notin\mathcal J).
\tag{42}
\]

Then by construction

\[
\sum_{n=1}^{M}d_nu_n
=-G_XG_X^{-1}Z_X=-Z_X,
\tag{43}
\]

so, in complex notation,

\[
\boxed{
\sum_{n=1}^{M}(c_n+e_n+d_n)v_n=0.
}
\tag{44}
\]

Moreover (39)--(41) give the pointwise bound

\[
\boxed{
\|d\|_\infty
\ll \frac{\log X}{\sqrt X}
=o(1).
}
\tag{45}
\]

This correction is diffuse, real before modulation, and supported away from both endpoint square functions. It therefore restores exact global centering at negligible source cost.

## 5. The full control matches every current aggregate source budget

Define the real pre-demodulated weights and complex coefficients

\[
w_n:=c_n+e_n+d_n,
\qquad
b_n:=w_nv_n.
\tag{46}
\]

Equations (6), (44), and (46) give the two exact structural constraints

\[
\boxed{
b_n(X+n)^{iU}=w_n\in\mathbb R,}
\qquad
\boxed{
\sum_{n=1}^{M}b_n=0.
}
\tag{47}
\]

The pointwise source envelope is immediate from (19), (21), and (45):

\[
\boxed{|b_n|=|w_n|\ll\log X.}
\tag{48}
\]

At every grid point, the calibrator has magnitude `L`, while the edge and centering corrections are `o(1)`. Since every `H>=H_0` interval contains `H/L+O(1)` grid points, equations (19), (30), and (45) imply absolute constants `0<c<C<infty` such that

\[
\boxed{
 cH\le\sum_{n\in I}|b_n|\le CH,
}
\tag{49}
\]

and

\[
\boxed{
 cH\log X\le\sum_{n\in I}|b_n|^2\le CH\log X
}
\tag{50}
\]

for every interval `I` of length `H>=H_0` and all sufficiently large `X`.

The interval discrepancy is much smaller. Combining (20), (29), and the trivial correction estimate from (45),

\[
\left|\sum_{n\in I}b_n\right|
\ll
 a_X+\sqrt H\log X+H\frac{\log X}{\sqrt X}.
\tag{51}
\]

For `H>=H_0`, division by `H` and (8), (10) give

\[
\frac1H
\left|\sum_{n\in I}b_n\right|
\ll
X^{-1/8-\eta}\sqrt{\log X}
+X^{-5/16-\eta/2}\log X
+X^{-1/2}\log X.
\tag{52}
\]

Each term beats every fixed logarithmic power. Therefore, for every fixed `A_0>0`, uniformly for every interval `|I|>=H_0`,

\[
\boxed{
\left|\sum_{n\in I}b_n\right|
=o_{A_0}\!\left(H(\log X)^{-A_0}\right).
}
\tag{53}
\]

So imposing the exact logarithmic carrier does not weaken the matched control at the scale of the all-interval theorem used in `ANF-165`.

It also preserves the moving-window diagonal. Let `omega_n` be the incidence count of coefficient `n` in the `N` length-`K` windows. For the sparse calibrator,

\[
K\sum_n|c_n|^2
=(1+o(1))XK\log X.
\tag{54}
\]

Only `O(K/L)` grid points lie in each incidence ramp, so replacing the full weight `K` by `omega_n` loses only

\[
O(K^2L)=o(XK\log X).
\tag{55}
\]

Thus

\[
\sum_n\omega_n|c_n|^2
=(1+o(1))XK\log X.
\tag{56}
\]

The edge charge contributes only

\[
\sum_n\omega_n|e_n|^2
\ll q_X^2H_0^2
\asymp X\log X,
\tag{57}
\]

and the central correction contributes

\[
\sum_n\omega_n|d_n|^2
\ll K|\mathcal J|\|d\|_\infty^2
\ll K\log^2X.
\tag{58}
\]

The corresponding cross terms are lower order, either directly from their supports and (19), (45), or by Cauchy--Schwarz against (56)--(58). Hence

\[
\boxed{
D_{N,K}(b)
:=\sum_n\omega_n|b_n|^2
=(1+o(1))XK\log X.
}
\tag{59}
\]

The control therefore matches the same diagonal and local-moment currencies as `ANF-167`, with the additional exact pointwise carrier-ray constraint (47).

## 6. The critical endpoint charge survives for almost the full bow horizon

For the left endpoint primitive write

\[
S_r^-:=\sum_{n=1}^{r}b_n,
\qquad 1\le r<K.
\tag{60}
\]

The correction block `mathcal J` begins at `asymp X`, while `K=o(X)`, so it contributes nothing to (60). For every `r>=H_0`, the edge contribution has already saturated at `E_X`. The calibrator contribution is bounded by (29): uniformly for `H_0<=r<K`,

\[
\left|\sum_{n=1}^{r}c_nv_n\right|
\ll \sqrt K\log X.
\tag{61}
\]

Since (4) and (10) imply

\[
\frac{\sqrt K\log X}{a_X}
=
X^{-\varepsilon+o(1)}\sqrt{\log X}
\longrightarrow0,
\tag{62}
\]

(18) and (61) give

\[
\boxed{
|S_r^-|
\ge (1-o(1))a_X
\qquad(H_0\le r<K)
}
\tag{63}
\]

uniformly across almost the entire endpoint horizon.

The exact endpoint completion of `ANF-157` therefore satisfies

\[
\begin{aligned}
E_\partial(b)
&=
\sum_{r=1}^{K-1}|S_r^-|^2
+
\sum_{r=1}^{K-1}|S_r^+|^2\\
&\ge
\sum_{r=H_0}^{K-1}|S_r^-|^2\\
&\ge
(1-o(1))(K-H_0)a_X^2.
\end{aligned}
\tag{64}
\]

Using `H_0=o(K)` and (10),

\[
\boxed{
E_\partial(b)
\ge
(\delta-o(1))XK\log X.
}
\tag{65}
\]

Thus a prescribed positive fraction of the bow scale remains compatible with every condition (47)--(59). The endpoint memory mechanism is not an artifact of having assigned arbitrary complex phases to the synthetic coefficients: it survives when every coefficient is forced onto the **exact** logarithmic carrier ray of the distinguished twist.

## 7. Information boundary: the remaining rigidity is arithmetic amplitude and placement

The construction is still synthetic. It does **not** assert that the actual source

\[
r_X(m)=\vartheta(m)-Q_R(m)
\tag{66}
\]

can realize the weights `w_n` above. `ANF-149` shows that, after negligible prime powers are removed, the true real amplitudes are much more rigid: on bulk primes,

\[
r_X(p)=\log p-c_R>0,
\tag{67}
\]

on `R`-rough composites,

\[
r_X(n)=-c_R,
\tag{68}
\]

and elsewhere they vanish, with the rough counterterm carrying its exact finite Ramanujan structure. The signs in the edge charger (14), the Rademacher signs in the calibrator (23), and the diffuse real correction (42) are not allowed by that arithmetic alphabet.

That distinction is now the live boundary. `ANF-161` already proved that the bare logarithmic carrier cannot sustain the critical endpoint spike on the required supercubic support. `ANF-168` proves the complementary statement that **allowing arbitrary real source amplitudes restores the obstruction even while the carrier is kept exact**. Together they bracket the missing theorem tightly:

\[
\text{carrier alone is harmless on threat support,}
\qquad
\text{carrier + arbitrary real amplitudes is not.}
\tag{69}
\]

Therefore a successful endpoint argument must use a property that distinguishes the true amplitude field (67)--(68) from arbitrary real carrier-adapted weights. Plausible currencies are a source-faithful autocorrelation/return law, an estimate coupling prime and rough locations to the exact carrier, or a direct square-function theorem for the signed prime-minus-Ramanujan primitive. Merely adding the facts that the coefficients are real before demodulation, that their phase is exactly `m^{-iU}`, that local mass is present everywhere, or that all currently controlled intervals have arbitrary logarithmic cancellation cannot close the gate.

## Prior-art audit and novelty boundary

A fresh audit checked prefix/vector discrepancy and signed-vector balancing as the nearest general frameworks. Those subjects contain much stronger generic balancing theorems than are needed here. No such theorem is load-bearing: the only signing statement used above is the elementary Rademacher estimate (25)--(27), obtained by an exponential-moment/Hoeffding bound and a union bound over fewer than `X^2` intervals. The exact centering step is elementary two-dimensional linear algebra once the internal carrier estimate `ANF-161` gives (38).

Accordingly no novelty is claimed for probabilistic vector balancing itself. The line-specific content is the **matched information obstruction**: the `ANF-167` endpoint-charge control can be upgraded to respect the exact logarithmic carrier ray at every site, while retaining all of its bow-normalized budgets and exact global centering. No new external theorem is needed, so `research/analytic_frontier/SOURCES.md` requires no change.

## Consequence for the research line

The phase side of the endpoint gate is now cleaner. A future pass should not spend effort proving only that `r_X(m)m^{-iU}` lies on prescribed carrier rays, nor on generic vector cancellation for those rays: that information has a matched control with target-size endpoint memory. The next useful source theorem must touch the discrete arithmetic amplitude law itself.

A decisive positive step would show that the actual prime/rough field (67)--(68), at the distinguished `U`, cannot keep a primitive of size `asymp sqrt(X log X)` for `Theta(K)` consecutive prefix lengths. A decisive negative step would construct an equally strong matched control that also respects the prime/rough amplitude alphabet or a quantitatively faithful surrogate of its placement law. Either outcome would cross a genuinely new information boundary rather than moving the same endpoint charge between generic phase models.