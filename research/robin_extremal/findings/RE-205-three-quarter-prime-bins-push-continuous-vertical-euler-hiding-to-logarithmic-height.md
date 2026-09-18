# RE-205 — Three-quarter prime bins push continuous vertical Euler hiding to logarithmic height

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + SHORT-INTERVAL-PNT + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + LOGARITHMIC-HEIGHT + KV-FIDELITY + INTEGER-MULTIPLICITIES`.

**Parent finding:** RE-204.

`RE-204` leaves a precise critical experiment: its continuous vertical hiding theorem assumes

\[
H T_Q+\log(1/\epsilon_Q)=o(V(Q)),
\qquad
V(Q)=\frac{(\log Q)^{3/5}}{(\log\log Q)^{1/5}},
\]

because the ordinary-prime realization places each synthesized shell in a Korobov--Vinogradov logarithmic bin. The continuum approximation itself does not require that scale. Replacing KV-width bins by unconditional power-short intervals reveals that the apparent phase-resolution frontier is not source-coercive.

Put

\[
d_Q:=\frac1{\sqrt Q\log Q},
\qquad H:=\log 8.
\tag{1}
\]

Fix constants `c>0` and `rho>0`, and set

\[
T_Q:=c\log Q,
\qquad
\epsilon_Q:=Q^{-\rho}.
\tag{2}
\]

If

\[
\boxed{
12H(\log 2)c+2\rho<\frac14,
}
\tag{3}
\]

then for all sufficiently large `Q` there is a finite ordinary-prime perturbation with coefficients `c_q\in\{-1,+1\}` such that, for

\[
D_Q(s):=\sum_q c_q\log(1-q^{-s})^{-1},
\tag{4}
\]

one has

\[
\boxed{
\sup_{|t|\le c\log Q}|D_Q(1+it)|=o(d_Q).
}
\tag{5}
\]

Before the first remote repair shell arrives, the local packet still has

\[
D_{Q,\mathrm{local}}(1)=\Theta(d_Q).
\tag{6}
\]

The perturbation uses only multiplicities `{0,1,2}` relative to the ordinary-prime baseline and, for every fixed `b>0`, satisfies

\[
|\Delta\vartheta(x)|=o\!\left(xe^{-bV(x)}\right)
\tag{7}
\]

through and beyond the affected scales.

Since `rho` may be chosen arbitrarily small after `c`, (3) gives a nonempty explicit logarithmic-height range

\[
\boxed{
0<c<\frac1{48H\log 2}
=0.01445\ldots .
}
\tag{8}
\]

Thus an entire vertical Euler interval of height a fixed positive multiple of `log Q` can be made selector-scale blind by an honest ordinary-prime `{0,1,2}` source. This is asymptotically much taller than the `o(V(Q))` windows of `RE-204`.

## 1. The continuum synthesis has only polynomial cost at logarithmic height

Use exactly the one-sided spectral-gap construction of `RE-204`. With

\[
\delta:=\frac1{4T_Q},
\qquad
m:=\left\lceil\frac H\delta\right\rceil,
\qquad
r:=\left\lceil\log_2(1/\epsilon_Q)\right\rceil,
\qquad
N:=m+r,
\tag{9}
\]

there are real coefficients `b_0,\ldots,b_N` and logarithmic displacements

\[
L_j:=(m+j)\delta\ge H
\tag{10}
\]

such that

\[
G_Q(t):=\sum_{j=0}^{N}b_je^{-itL_j}
\tag{11}
\]

satisfies

\[
\sup_{|t|\le T_Q}|1-G_Q(t)|\le\epsilon_Q,
\qquad
G_Q(0)=1.
\tag{12}
\]

The coefficient estimate proved there is

\[
A_Q:=\sum_{j=0}^{N}|b_j|
\le (N+1)2^{m+2N}.
\tag{13}
\]

Here

\[
m=4Hc\log Q+O(1),
\qquad
r=\frac{\rho}{\log2}\log Q+O(1),
\tag{14}
\]

so, writing

\[
\kappa:=12H(\log2)c+2\rho,
\tag{15}
\]

we obtain

\[
\boxed{
A_Q\le Q^{\kappa+o(1)}.
}
\tag{16}
\]

There are only `O(log Q)` repair shells. Moreover

\[
L_{\max}=(m+N)\delta
=2H+\frac{\rho}{4c\log2}+o(1),
\tag{17}
\]

so every shell center remains within a fixed multiplicative factor of `Q`. The continuum approximation therefore costs polynomial, rather than subpolynomial, reciprocal variation once `T_Q` is a fixed multiple of `log Q`; the exponent is the explicit `kappa` in (15).

## 2. Power-short prime intervals convert that polynomial cost into an honest source

The load-bearing external input is the unconditional prime number theorem in short intervals. Guth--Maynard, Corollary 1.3, gives the prime-count asymptotic uniformly for intervals of length `x^theta` for every fixed `theta>17/30`. We use only the much softer value

\[
\theta=\frac34.
\tag{18}
\]

Put

\[
X_0:=2Q,
\qquad
X_j:=X_0e^{L_j}.
\tag{19}
\]

For every local or remote center use the one-sided prime bin

\[
I_j:=[X_j,X_j+X_j^{3/4}].
\tag{20}
\]

Since consecutive logarithmic centers are separated by

\[
\delta\asymp\frac1{\log Q},
\tag{21}
\]

the physical center spacing is `asymp Q/log Q`, while each bin has length `asymp Q^{3/4}`. Hence the bins are pairwise disjoint for large `Q`. The short-interval PNT gives, uniformly over these `O(log Q)` centers,

\[
\#\{q\text{ prime}:q\in I_j\}
=(1+o(1))\frac{X_j^{3/4}}{\log X_j}
=Q^{3/4+o(1)}.
\tag{22}
\]

Choose

\[
B\asymp\frac{\sqrt Q}{\log Q}
\tag{23}
\]

ordinary primes from `I_0` and assign coefficient `+1`. For each remote shell choose

\[
N_j:=\left\lfloor |b_j|e^{L_j}B\right\rceil
\tag{24}
\]

ordinary primes from `I_j` and assign each coefficient

\[
c_q=-\operatorname{sgn}(b_j).
\tag{25}
\]

There are enough distinct primes. By (16)--(17), every required population is at most

\[
N_j\le Q^{1/2+\kappa+o(1)},
\tag{26}
\]

whereas (22) supplies `Q^{3/4+o(1)}` primes. Condition (3) is exactly strong enough to ensure

\[
\kappa<\frac14,
\tag{27}
\]

so the required fraction of every bin tends to zero. All edits are genuine deletions or duplications of ordinary primes; no continuous shell weight or generalized prime remains.

More generally, if one uses a short-interval exponent `theta`, the supply constraint is

\[
\kappa<\theta-\frac12.
\tag{28}
\]

The choice `theta=3/4` will also optimize the independent phase-placement constraint below.

## 3. The same quarter exponent controls phase placement

For `q\in I_j`,

\[
q=X_j\left(1+O(Q^{-1/4})\right).
\tag{29}
\]

Uniformly for `|t|\le T_Q=c\log Q`, elementary differentiation gives

\[
q^{-1-it}
=X_j^{-1-it}
\left(1+O((1+T_Q)Q^{-1/4})\right).
\tag{30}
\]

Ignoring this bin width and integer rounding, the local first Euler harmonic is

\[
B X_0^{-1-it},
\tag{31}
\]

while the remote shells contribute

\[
-BX_0^{-1-it}\sum_{j=0}^{N}b_je^{-itL_j}
=-BX_0^{-1-it}G_Q(t).
\tag{32}
\]

Equation (12) therefore leaves at most `epsilon_Q d_Q` at the ideal first-harmonic level.

The total absolute ideal reciprocal variation is `ll d_Q A_Q`. Thus (30) contributes

\[
\ll d_Q A_Q(1+T_Q)Q^{-1/4}
=d_Q Q^{\kappa-1/4+o(1)}
=o(d_Q)
\tag{33}
\]

by (27). Rounding the `O(log Q)` shell populations contributes only

\[
O\!\left(\frac{\log Q}{Q}\right)=o(d_Q).
\tag{34}
\]

Finally, uniformly on `Re s=1`,

\[
\log(1-q^{-s})^{-1}=q^{-s}+O(q^{-2}).
\tag{35}
\]

The complete higher-prime-power error is

\[
\ll \frac{d_QA_Q}{Q}
=d_QQ^{\kappa-1+o(1)}
=o(d_Q).
\tag{36}
\]

Since `epsilon_Q=Q^{-rho}`, equations (12), (33), (34) and (36) prove (5).

For a general power-short interval exponent `theta`, the placement condition corresponding to (33) is

\[
\kappa<1-\theta.
\tag{37}
\]

Hence the realizable polynomial synthesis budget is

\[
\kappa<\min\!\left(\theta-\frac12,1-\theta\right).
\tag{38}
\]

This is maximized at

\[
\boxed{\theta=\frac34,\qquad \kappa<\frac14.}
\tag{39}
\]

The `3/4` bin scale is therefore not decorative: it balances the number of available primes against the phase error incurred by not placing them exactly at the ideal shell center.

## 4. KV fidelity becomes easier, not harder

The local packet contributes Chebyshev mass `O(B log Q)=O(sqrt Q)`. Across all remote shells, (16)--(17) give total absolute Chebyshev edit mass

\[
\ll B\log Q\,A_Qe^{L_{\max}}
=Q^{1/2+\kappa+o(1)}.
\tag{40}
\]

Because `kappa<1/4`, this is `Q^{3/4-o(1)}` up to a fixed strict power margin. Every affected shell lies at `x\asymp Q`, while for each fixed `b>0`

\[
xe^{-bV(x)}=Q^{1-o(1)}.
\tag{41}
\]

Consequently even the total absolute edit mass, and hence every partial Chebyshev excursion inside every bin or between bins, is `o(xe^{-bV(x)})`. After the last shell the discrepancy is fixed while the KV envelope is eventually increasing. This proves (7) without using cancellation between remote shells.

Because `L_0\ge H=\log8`, the first repair center is at least `16Q`. Before it arrives, the local packet alone satisfies

\[
\sum_{q\in I_0}\log(1-q^{-1})^{-1}
=\Theta(B/Q)
=\Theta(d_Q),
\tag{42}
\]

which proves (6).

## Representation audit

The binomial/FIR approximation is the same generic Fourier construction already isolated in `RE-204`; no novelty is claimed for it. Likewise, the prime-number theorem in power-short intervals is external analytic-number-theory input. The current Guth--Maynard theorem is substantially stronger than needed here: `theta=3/4` lies safely inside its uniform all-interval range.

The line-specific new step is to combine the **polynomial coefficient cost at `T_Q=Theta(log Q)`** with power-short ordinary-prime bins and track both source constraints that those bins create. A bin of length `Q^theta` supplies `Q^{theta-1/2}` excess multiplicity over the selector packet, while its logarithmic width creates phase error `Q^{theta-1}`. Their balance gives the quarter-power budget (38)--(39). This removes the `V(Q)` placement bottleneck of `RE-204` using actual prime abundance rather than a generalized or continuously weighted source.

The resulting architectural correction is substantial: the Korobov--Vinogradov scale in `RE-204` was a **bin-resolution limit of that realization**, not a coercivity threshold for the ordinary-prime source class. Continuous complex-Euler observation remains noncoercive on a window whose height is a fixed positive fraction of `log Q`.

## Adversarial self-review

**Does a `Q^{3/4}` bin overlap the neighboring synthesis shell when there are `Theta(log Q)` shells?** No. Neighboring centers are separated by relative distance `delta=Theta(1/log Q)`, hence absolute distance `Theta(Q/log Q)`, which dominates `Q^{3/4}`.

**Does the short-interval PNT provide enough primes after the polynomial coefficient blow-up?** Yes. The worst required shell population is `Q^{1/2+kappa+o(1)}`, while each bin contains `Q^{3/4+o(1)}` primes. The strict inequality `kappa<1/4` leaves a fixed power margin.

**Can the broad bins destroy uniform phase cancellation at height `c log Q`?** Their relative width is only `Q^{-1/4}`. Multiplication by the height costs a logarithm, and multiplication by the full coefficient variation costs `Q^kappa`; (33) still tends to zero exactly when `kappa<1/4`.

**Do exact prime powers become visible once the coefficient mass is polynomial?** No. Equation (36) leaves an additional factor `Q^{-1}`. The allowed `kappa<1/4` is far below that threshold.

**Could the Chebyshev fidelity fail inside a bin before opposite edits arrive?** No. The proof uses total absolute Chebyshev edit mass, not cancellation. It is already `Q^{1/2+kappa+o(1)}=o(Qe^{-bV(Q)})` for every fixed `b>0`.

**Is the constant in (8) sharp?** No. It comes from the explicit but nonoptimized coefficient `ell^1` estimate of `RE-204`. Better continuum synthesis can improve the numerical constant. The durable conclusion is the scale jump from `o(V(Q))` to `c log Q` for some fixed `c>0`, together with the quarter-power source budget for this realization.

**Does this now reproduce a full Robin counterexample or the entire matched controls of `RE-188`--`RE-199`?** No. As in `RE-204`, the local packet exhibits a genuine selector reciprocal debt `Theta(d_Q)` and the full source is ordinary-prime/KV-faithful, but this finding does not prove that this packet alone creates the complete order-one Robin destination displacement or simultaneously matches every earlier source coordinate.

**Does the argument show that all windows of height `C log Q` are noncoercive for arbitrary `C`?** No. The construction has a polynomial coefficient cost whose exponent grows linearly with `C`, and the present `{0,1,2}` realization exhausts its quarter-power per-bin budget once (3) fails. This is a limitation of the construction, not a proof of coercivity beyond it.

## Research consequence

The next scalar-complex frontier is no longer the KV phase scale. A positive fraction of `log Q` is already invisible to an ordinary-prime source. The next useful test is therefore to determine whether the logarithmic-height coefficient/supply barrier is intrinsic: either derive a source-wide lower bound showing that uniform hiding on `[-C log Q,C log Q]` forces more reciprocal variation or per-phase prime capacity than `{0,1,2}` plus KV fidelity can provide, or construct a multi-bin architecture that redistributes large shell coefficients and pushes the continuum alias beyond the quarter-power budget.

A mere refinement of the Korobov--Vinogradov bin constant cannot decide that question; the `V(Q)` bottleneck has been bypassed.

## Sources

- `RE-204`, *Continuous vertical Euler windows remain noncoercive below the KV phase scale*.
- Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics **203** (2026), no. 2, 623--675, DOI `10.4007/annals.2026.203.2.6`, especially Corollary 1.3 on the prime number theorem in short intervals. This source is already anchored in `research/robin_extremal/SOURCES.md`.
