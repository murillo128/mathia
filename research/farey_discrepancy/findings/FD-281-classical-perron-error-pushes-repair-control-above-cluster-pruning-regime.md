# FD-281 — Classical Perron error pushes repair control above the cluster-pruning regime

- **Date:** 2026-09-23
- **Status:** proved method-level truncation/remainder tariff
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** truncated Perron / Mertens remainder / divisor-replicated repair / spectral-height tariff / cluster-population comparison / route pruning
- **Depends on:** FD-261, FD-267, FD-278, FD-279, FD-280
- **Classification:** `EXACT-DERIVED + CLASSICAL-PERRON-INPUT + REPAIR-WEIGHTED-ERROR-LEDGER + SPECTRAL-HEIGHT-CERTIFICATE + CLUSTER-REGIME-SEPARATION + ROUTE-CORRECTION`

## Claim

FD-280 identifies the non-circular spectral target: estimate the complementary Mertens remainder **directly at a cluster-complete cutoff**, rather than trying to compare the remainder before and after cluster completion. The first obvious input is the classical pointwise truncated-Perron error for `1/zeta(s)`.

That input is quantitatively too expensive for the present cluster-pruning strategy. Even after summing it through the exact divisor-replication geometry instead of first taking a uniform supremum, it retains a power-scale spectral-height tariff.

Let

\[
I_{T,c}(y)
:=
\frac{1}{2\pi i}
\int_{c-iT}^{c+iT}
\frac{y^s}{s\zeta(s)}\,ds,
\qquad c>1,
\tag{1}
\]

and let `e_T(y)` denote the difference between the ordinary Mertens value `M(y)` and the truncated Perron approximation, including the harmless half-endpoint correction when `y` is an integer. Fix integers `N,x>=2`, put

\[
Y:=2Nx,
\qquad
c:=1+\frac1{\log Y},
\tag{2}
\]

and assume `T>=2`. The classical absolute-coefficient truncated-Perron estimate gives, uniformly for `1<=y<=Y`,

\[
\boxed{
|e_T(y)|
\ll
1+\frac{y\log Y}{T}.
}
\tag{3}
\]

Apply the same physical operations as in FD-267: consecutive sampling at spacing `N` and divisor replication,

\[
\Delta_N e_T(q)
:=e_T(Nq)-e_T(N(q-1)),
\qquad
\mathcal E_{T,N}(d)
:=\sum_{q\mid d}\Delta_N e_T(q).
\tag{4}
\]

Then on the dyadic depth band `I_x={d:x<d<=2x}` one has

\[
\boxed{
\sum_{d\in I_x}|\mathcal E_{T,N}(d)|
\ll
\frac{N x^2\log(2Nx)}{T}
+x\log(2x).
}
\tag{5}
\]

The important point is the power `x^2/T`. Using the exact replication multiplicity removes the extra logarithm that would arise from inserting a uniform remainder bound into FD-267, but it does **not** remove a power of divisor depth.

Consequently, if the spectral packet is being tested at arithmetic amplitude `N^theta` against the FD-261 same-amplitude deep-repair threshold

\[
N^\theta x^{2-\beta},
\qquad
\beta:=\log_2\frac32,
\tag{6}
\]

then the classical pointwise Perron certificate makes the truncation remainder negligible only in the range

\[
\boxed{
T
\gg
N^{1-\theta}x^\beta\log(2Nx)
}
\tag{7}
\]

(up to any desired extra slowly growing factor if an `o(1)` comparison is required). This is a **sufficient-height requirement of this certificate**, not a lower bound for the true remainder.

In the polynomial-depth regime

\[
x=N^{\lambda+o(1)},
\tag{8}
\]

the power of `x` required by (7) is

\[
\boxed{
\tau_{\rm Perron}
=
\beta+\frac{1-\theta}{\lambda}.
}
\tag{9}
\]

At the critical-line calibration `theta=1/2`,

\[
\tau_{\rm Perron}
=
\beta+\frac1{2\lambda}.
\tag{10}
\]

Thus at the independent first-row depth `lambda=1/2`, classical pointwise Perron control requires

\[
T\ge x^{1+\beta+o(1)}
=x^{1.5849625007\ldots+o(1)},
\tag{11}
\]

while even at the balanced depth `lambda=1` it requires

\[
T\ge x^{\beta+1/2+o(1)}
=x^{1.0849625007\ldots+o(1)}.
\tag{12}
\]

This creates a direct incompatibility with the informative regime of the FD-278 aggregate cluster ledger. That ledger needs total population/cardinality/background exponent at least

\[
c_*:=1-\beta
=0.4150374992\ldots .
\tag{13}
\]

But every exponent in (9) satisfies

\[
\tau_{\rm Perron}>\beta>1-\beta=c_*.
\tag{14}
\]

Since Riemann--von Mangoldt permits `x^(tau+o(1))` zeros below height `T=x^(tau+o(1))`, once one raises the cutoff to the height at which the classical pointwise Perron error is certified harmless, **zero population alone is no longer ruled out as the term paying the FD-278 aggregate ledger**. Therefore the chain

`classical pointwise Perron remainder bound -> cluster-complete cutoff -> FD-278 cluster pruning`

cannot by itself finish the spectral obstruction. To preserve the informative low-population regime one needs a genuinely **repair-aware remainder estimate**, obtained before taking pointwise absolute values (or a different smoothed/grouped contour architecture with a controlled bridge back to the physical Mertens blocks).

## 1. Classical Perron error at the sampled Mertens points

For a Dirichlet series `F(s)=sum a_n n^(-s)`, the standard truncated Perron kernel gives an error bounded by

\[
\sum_{n\ge1}|a_n|
\left(\frac yn\right)^c
\min\!\left(1,
\frac1{T|\log(y/n)|}
\right),
\tag{15}
\]

with the usual half-weight convention at an integral endpoint. For `a_n=mu(n)`, use only `|mu(n)|<=1`.

Take `c` from (2). Split the sum into `n<y/2`, `y/2<n<2y`, and `n>2y`. In the middle range,

\[
|\log(y/n)|\gg \frac{|n-y|}{y},
\tag{16}
\]

so all terms except the endpoint contribute

\[
\ll
\sum_{1\le k\ll y}
\min\!\left(1,\frac{y}{Tk}\right)
\ll
1+\frac{y\log(2y)}T.
\tag{17}
\]

In the two far ranges, `|log(y/n)|` is bounded below by an absolute constant, hence the factor in (15) is `O(1/T)`. Because

\[
c-1=\frac1{\log Y}
\tag{18}
\]

and `y<=Y`, the tails are

\[
\ll
\frac{y^c}{T}
\sum_{n\ge1}n^{-c}
\ll
\frac{y\log Y}{T}.
\tag{19}
\]

The integral endpoint contributes `O(1)`. Replacing the Perron half-weight by the ordinary integer-valued `M(y)` changes the source by at most `1/2`, also `O(1)`. This proves (3).

The argument deliberately uses no Möbius cancellation and no RH input. It is exactly the absolute-coefficient pointwise certificate available before exploiting any special structure of the repair.

## 2. Exact divisor replication improves the logarithm, not the depth power

From (3), for `1<=q<=2x`,

\[
|\Delta_Ne_T(q)|
\ll
1+\frac{Nq\log Y}{T}.
\tag{20}
\]

Let

\[
m_x(q)
:=
\#\{d:x<d\le2x,\ q\mid d\}
=
\left\lfloor\frac{2x}{q}\right\rfloor
-
\left\lfloor\frac{x}{q}\right\rfloor .
\tag{21}
\]

Triangle inequality followed by exchange of the finite sums gives

\[
\sum_{d\in I_x}|\mathcal E_{T,N}(d)|
\le
\sum_{q\le2x}|\Delta_Ne_T(q)|m_x(q).
\tag{22}
\]

There are two exact arithmetic ledgers:

\[
\sum_{q\le2x}m_x(q)
=
\sum_{x<d\le2x}\tau(d)
\ll x\log(2x),
\tag{23}
\]

and

\[
\sum_{q\le2x}q\,m_x(q)
=
\sum_{x<d\le2x}\sigma_1(d)
\ll x^2.
\tag{24}
\]

Inserting (20) into (22) and applying (23)--(24) proves (5).

Equation (24) also shows why there is no hidden logarithmic artifact in the leading depth power. In fact the classical average order of `sigma_1` gives

\[
\sum_{x<d\le2x}\sigma_1(d)
\sim
\frac{\pi^2}{4}x^2.
\tag{25}
\]

Thus the `q`-weighted replication geometry itself is genuinely quadratic. The theorem does **not** say that the signed Perron errors attain this upper bound; it says that a pointwise absolute-value treatment has no further depth saving available merely from counting divisor copies.

As a finite audit, direct evaluation of (21) gives

\[
\frac1{x^2}
\sum_{q\le2x}q\,m_x(q)
=
2.48633,\ 2.47449,\ 2.46832,\ 2.46805,\ 2.46749
\]

for `x=32,128,512,2048,8192`, respectively, converging to `pi^2/4=2.467401...`. This is only a check on the finite replication ledger; the proof of (5) is analytic.

## 3. Height tariff for the FD-261 threshold

Divide the leading term of (5) by the same-amplitude threshold in (6). The ratio is

\[
\frac{Nx^2\log(2Nx)/T}
{N^\theta x^{2-\beta}}
=
\frac{N^{1-\theta}x^\beta\log(2Nx)}T.
\tag{26}
\]

The endpoint term from (5) is harmless:

\[
\frac{x\log(2x)}
{N^\theta x^{2-\beta}}
=
N^{-\theta}x^{\beta-1}\log(2x)
=o(1)
\tag{27}
\]

in every fixed polynomial-depth regime because `beta<1`. Equation (7) follows.

This comparison should be read as a **certificate boundary**. If `T` is smaller than the scale in (7), (5) does not prove that the actual remainder is large; it only fails to certify that it is negligible. Cancellation between the Perron truncation errors at consecutive sampled points could beat (20), and cancellation after divisor replication could beat (22). Capturing either effect requires keeping the signed kernel longer than the classical pointwise argument does.

At square-root arithmetic amplitude, substitute `theta=1/2` into (9). For the first-row scale `x=N^(1/2+o(1))`, one obtains

\[
T
\gg
N^{(1+\beta)/2+o(1)}
=
N^{0.7924812504\ldots+o(1)}
=
x^{1+\beta+o(1)}.
\tag{28}
\]

So the cutoff that the classical certificate asks us to use is not merely above the reciprocal-log boundary-cluster scale of FD-279; it is polynomially higher than the entire divisor depth.

## 4. Why this loses the FD-278 population obstruction

FD-278 packages the contribution of complete close-zero components below

\[
T=x^{\tau+o(1)}
\tag{29}
\]

into three possible sources of polynomial complexity: component population `R=x^(r+o(1))`, maximum component cardinality `x^(kappa+o(1))`, and desingularized background size `x^(b+o(1))`. Threshold repair requires

\[
r+\kappa+b\ge c_*:=1-\beta.
\tag{30}
\]

The strength of that statement comes from forcing one of those resources to be nontrivial when the available spectral population is small.

Riemann--von Mangoldt gives only

\[
R\le N_\zeta(T)
=x^{\tau+o(1)}.
\tag{31}
\]

At the Perron-certified height (9), however,

\[
\tau_{\rm Perron}
=
\beta+\frac{1-\theta}{\lambda}
>
\beta
>
1-\beta=c_*.
\tag{32}
\]

Therefore zero counting no longer forces `r<c_*`. In other words, at the first height where the classical pointwise remainder certificate becomes small enough, FD-278 can no longer exclude paying its entire exponent ledger through the **number of available components alone**, even if component cardinality and background conditioning stay subpolynomial.

This is not an existence claim for coherent contributions from all those components. It is a route-pruning statement: the deterministic cluster-count theorem ceases to force the anomaly that made the low-height argument informative. Any continuation at this high cutoff would need new cancellation/coherence information across the much larger zero population.

FD-279 and FD-280 fit cleanly into this picture. FD-279 says the boundary component can be completed with an `o(1)` ordinate displacement, so cluster completion does not alter `tau`. FD-280 says that displacement does not make the complementary hard-cutoff remainder continuous. FD-281 now adds that inserting the **standard pointwise Perron estimate** at the completed cutoff demands a value of `tau` already beyond the population-pruning threshold. Thus the missing bridge is not a technical choice of a nearby good ordinate.

## Stress tests and failure modes

The first stress test is to replace the repair-aware summation by the uniform form of FD-267. From (3) at `y<=2Nx`, one gets `sup|e_T| << Nx log(2Nx)/T+1`, and FD-267 would then give an extra divisor-average logarithm:

\[
\sum_{d\in I_x}|\mathcal E_{T,N}(d)|
\ll
\frac{Nx^2\log(2Nx)\log x}{T}
+x\log x.
\]

Equation (5) is therefore a genuine sharpening, but only logarithmic. The spectral-height **power** in (7) survives.

The second stress test is the endpoint convention. Perron's formula naturally returns a half-weight when the sampled argument is an integer, whereas the physical Mertens blocks use the full value. The discrepancy is bounded coordinatewise by `1/2`; after consecutive differencing and divisor replication it contributes at most a constant times (23), namely `O(x log x)`. It cannot alter any exponent in (7)--(12).

The third stress test is a hypothetical signed cancellation in the Perron kernel. Nothing here rules it out. Indeed that is exactly the surviving route: estimate the **transformed** truncation error before applying triangle inequality to each sampled `e_T(Nq)`, or keep the contour and divisor kernel grouped. A power saving there would be new information not present in the classical pointwise Perron estimate.

The fourth stress test is smoothing. A higher-order or smooth Mellin cutoff can improve spectral decay and remove hard boundary discontinuities, but it no longer approximates the sharp Mertens step with the same kernel. Any such strategy must quantify the desmoothing error after consecutive sampling and divisor replication. FD-281 makes no claim that the same height tariff survives every smoothed architecture.

## Prior-art check

The truncated Perron formula and its absolute-coefficient error are classical. The current Lee--Leong Mertens treatment already anchored in `SOURCES.md` records a modern explicit version and uses it as the entry point for comparing `M(x)` with a short zero sum. A fresh search checked truncated Perron errors for the Mertens function, short zero sums, and reciprocal-zeta contour estimates. It found the expected classical/modern pointwise framework but no source carrying that error through the repository-specific composition

\[
\text{sample at }Nq
\;\to\;
\text{consecutive difference}
\;\to\;
\text{divisor replication}
\;\to\;
\text{FD-261 capacity exponent}.
\]

The external input in (3) is therefore standard and already source-anchored; the repair ledger (5) and the exponent comparison (7)--(14) are derived here. No new `SOURCES.md` entry is needed.

## Implications

FD-280 leaves two non-circular possibilities: bound a cluster-complete remainder directly, or keep contour and boundary packet grouped. FD-281 shows that the most immediate implementation of the first option — applying a classical pointwise truncated-Perron error and then transporting it through the repair — is too coarse at the power scale relevant to the current cluster argument.

The next useful theorem should therefore act **before** the pointwise absolute-value loss. A natural target is a signed bound for

\[
\sum_{d\in I_x}
\left|
\sum_{q\mid d}
\bigl(e_T(Nq)-e_T(N(q-1))\bigr)
\right|
\]

that saves a positive power over `Nx^2/T` at a cutoff `T=x^(tau+o(1))` with `tau<c_*`, or at least with `tau` small enough that FD-278 still forces nontrivial cluster cardinality/background cost. Equivalently, one can move the consecutive-difference/divisor kernel **inside the Perron contour** and estimate the grouped contour directly rather than first producing a pointwise Mertens remainder.

This is a sharper frontier than “prove remainder stability.” The issue is now quantitative and structural: **classical pointwise Perron truncation discards exactly the signed information that would be needed to keep the cutoff low enough for the complete-cluster obstruction to remain informative.**