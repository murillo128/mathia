# NB-229 — Carrier decay localizes exact-Ford danger to the shallow zero-density uniformity gap

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + CANDIDATE-MECHANISM + ZETA-SPECTRAL-MATCHED-CONTROL + EXACT-FORD-SCALE + SCHWARTZ-CARRIER-LOCALIZATION + SHALLOW-DEPTH-REDUCTION + ZERO-DENSITY-BOUNDARY + NB-228-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-228` rewrites the exact-Ford moving-shell zero contribution as the Laplace transform of the nested depth-phase process

\[
\mathcal C_{X,H,t}(D)
=
\sum_{d_\rho\le D}
 m(\rho)e^{iX(\gamma-t)}F(Hv_\rho).
\]

That reduction leaves an apparently long depth interval `0 <= D <= R`. This finding shows that the actual smooth carrier collapses the dangerous interval dramatically: **all depths beyond order `log Q` are absolutely negligible before any zero-density or phase-cancellation theorem is used**. Here

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR\to Y_*\in(0,\infty).
\]

More precisely, for every depth cutoff `D_0`, the exact-Ford residue tail satisfies

\[
\boxed{
|\mathcal Z_{d\ge D_0}|
\ll_{\phi,r}
Qe^{-YD_0}.
}
\]

Consequently `D_0=(L+omega(1))/Y` already gives `o(1)`, and any fixed enlargement `D_0=(1+delta)L/Y` gives a power saving `O(Q^{-delta})`. The surviving source-side problem is therefore not a theorem over the full Ford depth `R`; it is a **moving shallow-depth problem on `D=O(L)`**, with the genuinely delicate range `D -> infinity`, `D=o(L)` left exposed.

A prior-art audit then reveals a precise mismatch. Classical density estimates with the desired `eta^(3/2)` exponent have logarithmic or fixed-parameter losses that dominate exactly in this moving shallow regime, while available log-free estimates with exponent linear in `eta` have the wrong Ford normalization. Thus the next useful zeta input is much more specific than “a stronger zero-density theorem”: it is a local, weighted or phase-sensitive estimate uniform for

\[
\eta=\frac DR,
\qquad
1\ll D\ll L,
\]

or a direct bound for the nested carrier `mathcal C(D)` itself.

No Nyman--Beurling distance theorem is proved here. This is a source-side localization and a method-boundary result.

## 1. Exact-Ford residue notation

Keep the notation of `NB-228`. Let

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR,
\tag{1}
\]

with

\[
Y\longrightarrow Y_*\in(0,\infty).
\tag{2}
\]

For fixed `r>0`, put

\[
\sigma_X=1+\frac rX,
\]

and use the smooth logarithmic shell

\[
h_{X,H}(u)
=\frac1H\phi\!\left(\frac{u-X}{H}\right),
\qquad
1\le H\le CX,
\qquad
\phi\in C_c^\infty((0,1)).
\tag{3}
\]

Its carrier is

\[
L_{X,H}(v)=e^{iXv}F(Hv),
\qquad
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\tag{4}
\]

For a nontrivial zero `rho=beta+i gamma` of multiplicity `m(rho)`, define

\[
d_\rho=R(1-\beta),
\qquad
v_\rho=(\gamma-t)+i(\sigma_X-\beta).
\tag{5}
\]

Then `NB-228` gives the exact factorization

\[
L_{X,H}(v_\rho)
=
 e^{-r}e^{-Yd_\rho}
 e^{iX(\gamma-t)}F(Hv_\rho),
\tag{6}
\]

and hence

\[
\mathcal Z_{X,H}(t)
=
 e^{-r}
\sum_\rho
 e^{-Yd_\rho}b_\rho,
\qquad
b_\rho
=
m(\rho)e^{iX(\gamma-t)}F(Hv_\rho).
\tag{7}
\]

The sum is over distinct zeros with multiplicity carried by `m(rho)`; equivalently one may sum over zeros with multiplicity and omit that factor.

## 2. The smooth carrier has only `O(Q)` total absolute zero weight

Because `phi` is smooth and compactly supported strictly inside `(0,1)`, repeated integration by parts gives, for every fixed `A>0`,

\[
|F(z)|
\ll_{A,\phi}
(1+|z|)^{-A},
\qquad
\operatorname{Im}z\ge0.
\tag{8}
\]

The half-plane condition is automatic here because `sigma_X>1>beta`. Since `H>=1`,

\[
|F(Hv_\rho)|
\ll_{A,\phi}
(1+|v_\rho|)^{-A}
\le
C_{A,\phi}(1+|\gamma-t|)^{-A}.
\tag{9}
\]

Now use only the classical local zero count, with multiplicity,

\[
N(T+1)-N(T)
\ll \log(2+|T|).
\tag{10}
\]

Partition the ordinate axis into unit intervals according to

\[
k\le |\gamma-t|<k+1,
\qquad k=0,1,2,\ldots .
\]

For `A>2`, (9)--(10) imply

\[
\begin{aligned}
\sum_\rho
m(\rho)|F(Hv_\rho)|
&\ll_{A,\phi}
\sum_{k\ge0}
\frac{Q+\log(k+2)}{(1+k)^A}\\
&\ll_{\phi} Q.
\end{aligned}
\tag{11}
\]

This estimate is deliberately crude horizontally: it uses no density theorem near `beta=1`, no cancellation among zero phases, and no special choice of `H` beyond `H>=1`. The vertical Schwartz decay alone turns the whole zero set into an absolute carrier budget of size `O(Q)`.

## 3. Exponential Ford damping makes all depths beyond `log Q` harmless

For `D_0>=0`, restrict (7) to zeros with `d_rho>=D_0`. Since `Y>0`,

\[
\begin{aligned}
|\mathcal Z_{d\ge D_0}|
&\le
 e^{-r}e^{-YD_0}
 \sum_{d_\rho\ge D_0}|b_\rho|\\
&\le
 e^{-r}e^{-YD_0}
 \sum_\rho m(\rho)|F(Hv_\rho)|.
\end{aligned}
\]

Using (11),

\[
\boxed{
|\mathcal Z_{d\ge D_0}|
\ll_{\phi,r}
Qe^{-YD_0}.
}
\tag{12}
\]

This is the main localization statement. Writing `L=log Q`, if

\[
D_0=\frac{L+w(Q)}{Y},
\qquad
w(Q)\to\infty,
\tag{13}
\]

then

\[
|\mathcal Z_{d\ge D_0}|
\ll e^{-w(Q)}=o(1).
\tag{14}
\]

For every fixed `delta>0`, the cleaner cutoff

\[
D_0=\frac{(1+\delta)L}{Y}
\tag{15}
\]

gives

\[
\boxed{
|\mathcal Z_{d\ge D_0}|
\ll Q^{-\delta}.
}
\tag{16}
\]

On the exact-Ford sequence `Y -> Y_* in (0,infinity)`, this active depth is

\[
D_0\asymp L
\ll
R=Q^{2/3}L^{1/3}.
\tag{17}
\]

So the full Ford depth interval from `NB-228` is far larger than the region capable of carrying order-one residue mass. **The difficult zeros are necessarily shallow in normalized depth.** Deep Ford packets are killed absolutely by the product of carrier localization and residue damping; no phase theorem is needed there.

## 4. What remains is the moving range `1 << D << L`

The reduction does not by itself control the active shallow layer. In particular, the adversarial packets of `NB-225`--`NB-227` can be placed at depths that tend to infinity arbitrarily slowly, hence well inside (17). The ordinary zero-free region excludes a fixed initial portion of the depth axis, but does not settle the whole moving interval between that boundary and `D=O(L)`.

A natural positive target is a weighted population estimate

\[
\mathcal M_{t,H}(D)
:=
\sum_{d_\rho\le D}
 m(\rho)|F(Hv_\rho)|,
\tag{18}
\]

with, for some fixed `delta>0`,

\[
\log \mathcal M_{t,H}(D)
\le
(Y-\delta)D+o(D)
\tag{19}
\]

uniformly over the moving range `1 << D << L`. Stronger and more source-faithful would be a direct phase-sensitive estimate for

\[
\mathcal C_{X,H,t}(D)
=
\sum_{d_\rho\le D}
 m(\rho)e^{iX(\gamma-t)}F(Hv_\rho),
\tag{20}
\]

because (20) is the exact Abel dual identified in `NB-228`.

The point is not that (19) is known to be necessary in this precise form. It is a clean sufficient benchmark showing what kind of uniformity is now relevant. The carrier reduction has removed every depth `D >> L`; the remaining theorem must work as the horizontal parameter itself moves to zero with `t`.

## 5. Published global zero-density forms expose the missing uniformity

This section is a prior-art boundary audit, not an input to the proof of (12).

Put

\[
\eta=1-\sigma=\frac DR.
\tag{21}
\]

The classical Halasz--Turan type density shape near one is

\[
N(1-\eta,T)
\ll
T^{C\eta^{3/2}}(\log T)^A.
\tag{22}
\]

At Ford normalization,

\[
(\log T)\eta^{3/2}
\asymp
Q\left(\frac D{Q^{2/3}L^{1/3}}\right)^{3/2}
=
\frac{D^{3/2}}{\sqrt L}.
\tag{23}
\]

The main exponent in (22) is therefore structurally excellent: it is `o(D)` whenever `D=o(L)`. But the prefactor contributes

\[
A\log\log T
\asymp AL,
\tag{24}
\]

to the logarithm of the bound, and that dominates the desired `O(D)` scale throughout the genuinely shallow regime `D=o(L)`. Thus the classical global estimate has the right exponent but the wrong uniform loss for this coupled limit.

Janos Pintz, *Density theorems for Riemann's zeta-function near the line Re s=1*, Acta Arith. 208 (2023), 363--379, DOI `10.4064/aa220909-20-4`, obtains modern `eta^(3/2)`-scale density estimates close to the 1-line. His displayed theorems are formulated with fixed auxiliary parameters: for example, for every fixed `epsilon>0` one obtains a bound of the form

\[
N(\sigma,T)
\ll_\epsilon
T^{(3\sqrt2+\epsilon)(1-\sigma)^{3/2}+\epsilon}
\tag{25}
\]

in the stated near-one range. The `T^epsilon` term is harmless for fixed-parameter density questions but is fatal if inserted naively into (19): it contributes `epsilon Q`, enormously larger than `D=O(L)`. One cannot set `epsilon=epsilon(T)` without a theorem uniform in that dependence. This is a quantifier boundary, not a criticism of the density theorem.

Conversely, an explicit log-free estimate of the schematic form

\[
N(1-\eta,T)
\ll
T^{B\eta}
\tag{26}
\]

such as the log-free framework in Chiara Bellotti, *An explicit log-free zero density estimate for the Riemann zeta-function*, J. Number Theory 273 (2025), 400--418, DOI `10.1016/j.jnt.2024.10.001`, removes the logarithmic prefactor but has a linear `eta` exponent. In the Ford coordinates this costs

\[
Q\eta
=
\frac{QD}{R}
=
D\,Q^{1/3}L^{-1/3},
\tag{27}
\]

which is much larger than `D`.

The two failures are complementary:

- `eta^(3/2)` density has the right Ford exponent but published global forms do not provide the required moving shallow-depth uniformity for free;
- log-free linear-`eta` density removes the prefactor but pays too much in the horizontal exponent.

Therefore simply invoking a stronger-looking **global** zero-density estimate does not close `NB-228`. What is missing is specifically a local/unit-window, carrier-weighted, or phase-sensitive estimate whose constants remain uniform when `eta=D/R` moves through `1 << D << L`.

This audit does **not** assert that no suitable theorem exists in the literature; it records that the inspected published global forms do not directly provide the needed coupled estimate.

## 6. Representation audit

The localization proof (8)--(16) is largely generic spectral geometry. It would hold for any discrete spectral set satisfying an `O(Q)` unit-window counting law, combined with a Schwartz vertical carrier and an external damping factor `e^{-Yd}`. In that sense the fact that the active depth collapses to `O(log Q)` is not specifically arithmetic.

The zeta-specific content enters in three places: the Ford depth coordinate

\[
d_\rho=R(1-\beta),
\]

the exact residue damping `e^{-Yd_rho}`, and the actual distribution of zeta zeros inside the surviving shallow layer. The live question after this finding is therefore genuinely arithmetic even though the tail truncation itself is not.

The result also remains strictly **source-side**. It controls the zero contribution to the moving-shell explicit-formula mechanism developed in `NB-218`--`NB-228`; it does not show that an optimal Nyman--Beurling approximant must expose this source observable, and it does not imply a lower or upper bound for the Nyman distance.

## 7. Consequence for the research frontier

`NB-228` made the exact-Ford problem a nested depth-phase problem. This finding shrinks that problem from `0 <= D <= R` to an active layer of width only `O(log Q)`. Any order-one obstruction must now be manufactured inside

\[
D\lesssim\frac{\log Q}{Y},
\tag{28}
\]

while all deeper zeros are absolutely negligible.

That changes the next useful search target. A theorem about the whole zero set is unnecessarily broad. The most direct positive routes are now:

1. a local zero-density estimate in ordinate windows matched to `F(Hv)`, uniform for `eta=D/R` with `1 << D << L` and with no loss larger than `exp(o(D))`; or
2. a direct cancellation estimate for the cumulative carrier `mathcal C_{X,H,t}(D)` that makes it subcritical relative to `e^(YD)` on that same moving interval.

The corresponding negative route is equally concrete: construct or justify zeta-compatible shallow packets whose nested cumulative phase actually attains critical exponential type inside `D=O(L)`. Either direction attacks the only depth range still capable of surviving the exact-Ford damping.
