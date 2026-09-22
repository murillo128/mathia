# FD-268 — Frequency-capped Mellin packets sharpen the deep repair barrier

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** canonical full-grid repair / Mellin zero packets / finite differencing / divisor smoothing / frequency cap / spectral-complexity threshold / source-side route pruning
- **Depends on:** FD-040, FD-234, FD-260, FD-261, FD-262, FD-265, FD-266, FD-267
- **Classification:** `EXACT-DERIVED + MELLIN-PACKET + FREQUENCY-CAPPED-DIFFERENCE + DIVISOR-REPLICATION-BOUND + REFINED-SPECTRAL-COMPLEXITY + ROUTE-PRUNING`

## Claim

FD-267 proves that a fixed finite Mellin packet cannot supply the superlinear divisor-depth amplification needed to improve the first-row obstruction. Its packet norm

\[
W(F)=\sum_j |a_j|(1+|\rho_j|)
\]

comes from the derivative estimate for one consecutive Mellin increment. That estimate is correct but becomes very wasteful when the spectral frequency `|rho|` is larger than the divisor scale being sampled: a unit-step difference cannot grow indefinitely with frequency because its two endpoints already have bounded modulus.

This gives a sharper, band-dependent theorem.

Fix `0<theta<1` and a finite Mellin packet

\[
F(t)=\sum_{j=1}^J a_j t^{\rho_j},
\qquad
\rho_j=\sigma_j+i\gamma_j,
\qquad
0<\sigma_j\le\theta,
\tag{1}
\]

with `F(0)=0`. For `N>=1`, put

\[
U_{F,N}(q)=F(Nq)-F(N(q-1)),
\qquad
G_{F,N}(d)=\sum_{q\mid d}U_{F,N}(q).
\tag{2}
\]

For a dyadic coefficient band `I_x={d:x<d<=2x}`, `x>=2`, define the frequency-capped packet complexity

\[
\boxed{
\mathcal W_{\theta,x}(F)
:=
\sum_{j=1}^J
|a_j|\bigl(1+\min\{|\rho_j|,x\}\bigr)^\theta .
}
\tag{3}
\]

Then

\[
\boxed{
\sum_{x<d\le2x}|G_{F,N}(d)|
\ll_\theta
N^\theta x\,\mathcal W_{\theta,x}(F).
}
\tag{4}
\]

Consequently the real canonical correction

\[
\widetilde c_{F,N}(d)=-\frac12G_{F,N}(d)
\]

satisfies

\[
\boxed{
\sum_{x<d\le2x}(-\widetilde c_{F,N}(d))_+
\ll_\theta
N^\theta x\,\mathcal W_{\theta,x}(F).
}
\tag{5}
\]

The dependence on spectral frequency has therefore been overcounted in FD-267. A mode with `|rho|<<x` costs only about `|rho|^theta`, not `|rho|`, while a mode with `|rho|>>x` saturates at cost `x^theta`; increasing the frequency further cannot buy more divisor-depth leverage from this absolute-value mechanism.

At depth `x asymp D`, if a growing packet family obeys

\[
\mathcal W_{\theta,D}(F_D)=D^{\omega+o(1)},
\tag{6}
\]

then its effective repair-depth exponent is at most

\[
\alpha\le1+\omega.
\tag{7}
\]

FD-261 therefore still requires

\[
\boxed{
\omega>1-\beta
=0.4150374992\ldots,
\qquad
\beta=\log_2\frac32,
}
\tag{8}
\]

before this spectral route can become decisive at or before the independent first-row scale. The threshold is the same number as in FD-267, but it now applies to the strictly smaller frequency-capped complexity (3). High spectral height by itself cannot evade the barrier.

## 1. A Mellin block increment has two independent ceilings

Consider one mode `a t^rho` and write `R=|rho|`, `sigma=Re(rho)<=theta`. For every integer `q>=2`, the endpoint bound gives

\[
|q^\rho-(q-1)^\rho|
\le q^\sigma+(q-1)^\sigma
\le2q^\theta.
\tag{9}
\]

On the other hand, the derivative identity used in FD-267 gives

\[
q^\rho-(q-1)^\rho
=
\rho\int_{q-1}^{q}t^{\rho-1}\,dt.
\]

Since `q-1>=q/2`, `0<sigma<=theta<1`,

\[
|q^\rho-(q-1)^\rho|
\le
R(q-1)^{\sigma-1}
\le
2R q^{\theta-1}.
\tag{10}
\]

Combining (9) and (10),

\[
\boxed{
|q^\rho-(q-1)^\rho|
\le
2q^\theta\min\left\{1,\frac Rq\right\}.
}
\tag{11}
\]

At `q=1`, with `0^rho=0`, the difference is exactly one. Formula (11) is the key refinement: the derivative regime is relevant only while `R` is below the local block index. Once `R` is much larger than `q`, endpoint size rather than derivative size controls the increment.

This also identifies the scale at which frequency can matter. Consecutive sampling probes phase variation only down to one unit in `q`; frequencies much larger than the sampled divisor band cannot generate a block increment larger than the two endpoint amplitudes.

## 2. Divisor replication converts the cap into a `theta`-power cost

Let

\[
m_x(q)
=
\#\{d:x<d\le2x,\ q\mid d\}.
\tag{12}
\]

As in FD-263 and FD-267,

\[
m_x(q)\le\frac{2x}{q}\quad(q\le x),
\qquad
m_x(q)=1\quad(x<q\le2x).
\tag{13}
\]

For one mode, triangle inequality and (11) give, apart from the harmless `q=1` contribution,

\[
\sum_{x<d\le2x}|G_{\rho,N}(d)|
\le
|a|N^\theta
\sum_{q\le2x}
|q^\rho-(q-1)^\rho|m_x(q).
\tag{14}
\]

For the shallow part `2<=q<=x`, (11)--(13) reduce the relevant sum to

\[
x\sum_{q\le x}q^{\theta-1}
\min\left\{1,\frac Rq\right\}.
\tag{15}
\]

Put `Y=min(R,x)`. If `1<=R<=x`, split at `q=R`:

\[
\sum_{q\le R}q^{\theta-1}
+
R\sum_{R<q\le x}q^{\theta-2}
\ll_\theta R^\theta.
\tag{16}
\]

If `R>x`, the first sum alone is `O_theta(x^theta)`; if `R<1`, the entire expression is `O_theta(1)`. Uniformly,

\[
\boxed{
\sum_{q\le x}q^{\theta-1}
\min\left\{1,\frac Rq\right\}
\ll_\theta
(1+Y)^\theta.
}
\tag{17}
\]

For the deep shell `x<q<=2x`, there is no divisor replication. If `R<=x`, the derivative estimate gives

\[
\sum_{x<q\le2x}|q^\rho-(q-1)^\rho|
\ll_	heta R x^\theta
\ll_	heta x(1+R)^\theta,
\tag{18}
\]

where the second inequality uses `R<=x` and `0<theta<1`. If `R>x`, the endpoint estimate instead gives

\[
\sum_{x<q\le2x}|q^\rho-(q-1)^\rho|
\ll_	heta x^{1+\theta}
\ll_	heta x(1+x)^\theta.
\tag{19}
\]

Combining the `q=1` term, (17), (18), and (19) proves the one-mode bound

\[
\boxed{
\sum_{x<d\le2x}|G_{\rho,N}(d)|
\ll_\theta
|a|N^\theta x
\bigl(1+\min\{R,x\}\bigr)^\theta.
}
\tag{20}
\]

Summing (20) over the packet proves (4), and (5) follows from

\[
(-\widetilde c_{F,N}(d))_+
\le\frac12|G_{F,N}(d)|.
\]

No phase assumption is used. Interference between modes can only reduce the absolute packet bound after the triangle inequality.

## 3. What changes for zeta-zero packets

For a simple zeta-zero residue of the standard form

\[
a_\rho t^\rho
=
\frac{t^\rho}{\rho\zeta'(\rho)},
\tag{21}
\]

the FD-267 derivative-only norm effectively charged each sufficiently high mode by `1/|zeta'(rho)|`. The refined band norm charges instead

\[
\boxed{
\frac{(1+\min\{|\rho|,x\})^\theta}
{|\rho\zeta'(\rho)|}.
}
\tag{22}
\]

Thus for `1<<|rho|<=x` the contribution is

\[
\asymp
\frac{|\rho|^{\theta-1}}{|\zeta'(\rho)|},
\tag{23}
\]

while for `|rho|>x` it is

\[
\asymp
\frac{x^\theta}{|\rho|\,|\zeta'(\rho)|}.
\tag{24}
\]

This is only a calibration of the deterministic theorem. No zero simplicity assumption, estimate for sums over zeros, Riemann hypothesis, or explicit-formula truncation theorem is used in (4).

The distinction matters conceptually. FD-267 left open the possibility that merely extending the packet to very high spectral height might create the required polynomial weighted complexity because the derivative factor grew like `|rho|`. Equations (22)--(24) remove that artificial leverage. Above the physical divisor band, each additional mode is suppressed by its residue coefficient while the finite-difference factor has already saturated.

## 4. The deep-band phase boundary is now a capped spectral-complexity problem

Take `x asymp D` and suppose all packet exponents satisfy `Re(rho)<=theta<1`. Equation (4) has the source-demand scale

\[
N^{\theta+o(1)}D^{1+\omega+o(1)}
\]

when (6) holds. Comparing with FD-261 gives the necessary condition (8). Because

\[
\mathcal W_{\theta,D}(F)
\le
\sum_j |a_j|(1+|\rho_j|),
\tag{25}
\]

FD-268 strictly strengthens the route-pruning statement of FD-267 whenever frequencies grow with depth.

In particular, neither a bounded number of modes at arbitrarily high height nor a packet whose capped norm is `D^{o(1)}` can provide the missing depth exponent. A successful spectral implementation must accumulate genuinely polynomial mass in the band-resolved quantity (3), or else place the needed growth in the explicit-formula remainder or in structure not captured by the absolute packet estimate.

This does **not** prove that the complete Mertens explicit formula has small `mathcal W_{theta,D}`. Establishing such a statement would require real information about the zero residues and the truncation/remainder, which is outside the present theorem. The result is instead a deterministic filter on what any proposed packet explanation must pay.

## 5. Prior-art boundary and finite audit

The use of zeta-zero residues in explicit representations of `M(x)` is classical, and modern explicit work also compares `M(x)` with short sums over nontrivial zeros. The new estimate here does not depend on any external explicit-formula theorem: it is the elementary combination of the endpoint and derivative bounds for a complex power with the exact divisor-replication ledger already used in this line. A targeted prior-art search found no matching theorem for this particular consecutive-block/divisor-smoothed, band-frequency-capped norm, so no new `SOURCES.md` dependency is required.

As a finite scale audit, one-mode calculations with `theta=0.6`, dyadic bands `x=64,256,1024`, and frequencies ranging from `0.1` to `10000` keep both the exact divisor-smoothed `l^1` field and the replication-ledger upper bound bounded after normalization by

\[
x\bigl(1+\min\{|\rho|,x\}\bigr)^\theta.
\]

The replication-ledger ratio stays below about `4.3` in this grid, including the regime `|rho|>>x` where the new endpoint cap is active. This computation is only a convention and scaling check; the proof is (9)--(20).

## Boundary

FD-268 sharpens only the Mellin-packet route. It does not improve the positive-cushion exponent `beta`, does not supply a lower bound for the actual Mertens repair demand, and does not control an infinite zero sum without a separately justified truncation and remainder. It also makes no claim that the capped packet norm is optimal under cancellation between modes.

What it removes is a specific false source of leverage: **spectral frequency cannot be converted linearly into arbitrary divisor-depth amplification once the frequency exceeds the sampled band**. The surviving spectral target is therefore stricter than in FD-267: one must produce at least `D^(1-beta-o(1))` growth in the capped norm `mathcal W_{theta,D}`, not merely in a derivative-weighted norm that can be inflated by very high frequencies.

**Verdict.** Finite differencing itself acts as a frequency cap. For canonical Mellin repair packets, the relevant deterministic complexity at depth `D` is bounded by `sum |a_rho|(1+min(|rho|,D))^theta`, and any attempt to beat the first-row ceiling through this route must make that capped quantity grow polynomially with exponent strictly exceeding `1-beta=0.415037...`.