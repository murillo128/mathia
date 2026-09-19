# NB-230 — Bellotti local counts compress shallow Ford danger to logarithmic carrier width

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + ZETA-SPECTRAL-MATCHED-CONTROL + EXACT-FORD-SCALE + LOCAL-ZERO-COUNT + CARRIER-WIDTH/DEPTH-TRADEOFF + SHALLOW-GAP-REFINEMENT + NB-224/NB-229-SYNTHESIS + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-229` localizes every potentially order-one exact-Ford zero contribution to normalized depths `D=O(log Q)` and identifies the moving range

\[
1\ll D\ll \log Q
\]

as the remaining zero-density uniformity gap. That frontier is still too broad once the vertical carrier width is retained. `NB-224` had already derived from Bellotti's local zero-disk lemma the weighted population law

\[
\mathcal M_{t,H}(D)
\ll
D+\frac RH
\]

through the Bellotti shallow range, but used it only in the log-wide regime `H=Theta(R)`.

Combining that local law with the exact Ford damping of `NB-228` shows that the quantity `R/H` enters the dangerous horizontal depth only **logarithmically**. Put

\[
J:=1+\frac RH.
\]

Then, throughout the moving Bellotti range, every depth satisfying

\[
YD-\log J\longrightarrow+\infty
\]

is already absolutely harmless. Equivalently, the unresolved moving shallow region is confined to

\[
\boxed{
D\lesssim \frac1Y\log\!\left(1+\frac RH\right)
}
\]

up to a diverging additive margin and the endpoint where Bellotti's local lemma itself stops being available.

This substantially sharpens the `1<<D<<log Q` frontier whenever `log(R/H)=o(log Q)`. It also explains the depth chosen by the matched packets of `NB-225`--`NB-227`: their logarithmic horizontal displacement is not arbitrary, but is precisely the scale at which the vertical carrier capacity `R/H` can pay the Ford factor.

No new zero-density theorem is proved. The result is an exact synthesis of the existing Bellotti local count with the source-faithful Ford carrier, and it corrects the search target after `NB-229`: a new shallow zero-density theorem is needed only inside the carrier-width depth window, not throughout every moving depth `D=o(log Q)`.

## 1. Keep the carrier-width parameter visible

Use the exact-Ford notation of `NB-224`--`NB-229`:

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

and work along a sequence

\[
Y\longrightarrow Y_*\in(0,\infty).
\tag{2}
\]

For fixed `r>0`, let

\[
\sigma_X=1+\frac rX,
\qquad
h_{X,H}(u)
=\frac1H\phi\!\left(\frac{u-X}{H}\right),
\qquad
1\le H\le CX,
\tag{3}
\]

with nonzero `phi in C_c^infinity((0,1))`. Write

\[
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\tag{4}
\]

For a nontrivial zero `rho=beta+i gamma`, counted with multiplicity `m(rho)`, put

\[
d_\rho=R(1-\beta),
\qquad
v_\rho=(\gamma-t)+i(\sigma_X-\beta).
\tag{5}
\]

The exact residue carrier from `NB-228` is

\[
\mathcal Z_{X,H}(t)
=
 e^{-r}
\sum_\rho
m(\rho)e^{-Yd_\rho}
 e^{iX(\gamma-t)}F(Hv_\rho).
\tag{6}
\]

Define the absolute weighted population

\[
\mathcal M_{t,H}(D)
:=
\sum_{d_\rho\le D}
m(\rho)|F(Hv_\rho)|
\tag{7}
\]

and the nested signed carrier

\[
\mathcal C_{X,H,t}(D)
:=
\sum_{d_\rho\le D}
m(\rho)e^{iX(\gamma-t)}F(Hv_\rho).
\tag{8}
\]

Finally set

\[
\boxed{
J:=1+\frac RH.
}
\tag{9}
\]

The harmless `1` makes the formulas uniform when `H` is comparable with or larger than `R`. The interesting sublinear-shell case has `R/H->infinity`, so `J~R/H` there.

## 2. Bellotti already gives `M(D) << D+J`

Because `phi` is smooth and supported away from the left endpoint, repeated integration by parts gives, uniformly for `Im z>=0`,

\[
|F(z)|
\ll_{A,\phi}
(1+|z|)^{-A}
\tag{10}
\]

for every fixed `A>0`. In particular,

\[
|F(Hv_\rho)|
\ll_{A,\phi}
(1+H|\gamma-t|)^{-A}.
\tag{11}
\]

`NB-224`, using Bellotti's Lemma 2.4, proves that there is a fixed `c_B>0` such that for

\[
1\le D\le c_B L
\tag{12}
\]

one has

\[
\sum_{d_\rho\le D}
m(\rho)(1+H|\gamma-t|)^{-A}
\ll_{A,\phi}
D+\frac RH.
\tag{13}
\]

The mechanism is worth retaining because it is exactly source-matched. A Bellotti disk of radius `D/R` contains `O(D)` zeros. The vertical carrier has effective width `1/H`, so it intersects about

\[
\frac{1/H}{D/R}
=\frac{R}{HD}
\]

such disks. Multiplying by `O(D)` zeros per disk produces the extra capacity `R/H`.

Combining (11)--(13),

\[
\boxed{
\mathcal M_{t,H}(D)
\ll
D+J,
\qquad
1\le D\le c_B L.
}
\tag{14}
\]

Consequently the actual nested signed process obeys the same bound,

\[
\boxed{
|\mathcal C_{X,H,t}(D)|
\le
\mathcal M_{t,H}(D)
\ll
D+J.
}
\tag{15}
\]

No phase theorem is being used here. This is a purely absolute consequence of the local zero population and the actual smooth carrier.

## 3. The `NB-229` moving-depth benchmark is automatically satisfied above `log J`

`NB-229` proposes, as a clean sufficient benchmark in the moving shallow range,

\[
\log \mathcal M_{t,H}(D)
\le
(Y-\delta)D+o(D)
\tag{16}
\]

for some fixed `delta>0`. Equation (14) shows that a large part of this benchmark needs no new zero-density theorem.

Let `D=D(Q)` satisfy

\[
D\to\infty,
\qquad
D=o(L),
\qquad
\log J=o(D).
\tag{17}
\]

Then

\[
\log \mathcal M_{t,H}(D)
\le
\log(D+J)+O(1)
=o(D).
\tag{18}
\]

Since `Y->Y_*>0`, for every fixed `0<delta<Y_*` sufficiently close to zero,

\[
\boxed{
\log \mathcal M_{t,H}(D)
\le
(Y-\delta)D
}
\tag{19}
\]

for all sufficiently large `Q`. The stronger signed quantity satisfies the same conclusion by (15).

Thus the moving zero-density gap isolated in `NB-229` cannot occur at depths much larger than `log J`. In that region the already-published local disk theorem is vastly stronger than the required exponential benchmark: it gives only polynomial growth in `D` plus the fixed carrier-capacity term `J`.

Equivalently, a critical-type excursion

\[
|\mathcal C(D)|\asymp e^{YD}
\tag{20}
\]

of the kind required by the matched controls of `NB-225`--`NB-228` can only fit inside the Bellotti population budget if

\[
e^{YD}
\lesssim D+J.
\tag{21}
\]

For moving `D`, the `D` term is negligible on the exponential scale, leaving the transition

\[
\boxed{
YD\lesssim \log J.
}
\tag{22}
\]

This is the carrier-width depth law.

## 4. Stieltjes summation gives an absolute shallow-tail estimate

The previous conclusion is pointwise in depth. The same input also controls an entire moving depth interval at once.

For

\[
1\le D_0<D_1\le c_B L,
\]

consider the absolute residue mass in that slab,

\[
\mathcal T(D_0,D_1)
:=
\sum_{D_0<d_\rho\le D_1}
m(\rho)e^{-Yd_\rho}|F(Hv_\rho)|.
\tag{23}
\]

Regard `M(D)=mathcal M_{t,H}(D)` as a monotone Stieltjes distribution. Then

\[
\mathcal T(D_0,D_1)
=
\int_{(D_0,D_1]}e^{-YD}\,dM(D).
\tag{24}
\]

Integration by parts and monotonicity give

\[
\mathcal T(D_0,D_1)
\le
 e^{-YD_1}M(D_1)
+
Y\int_{D_0}^{D_1}e^{-YD}M(D)\,dD.
\tag{25}
\]

Insert (14). Once `D_0` is large enough that `e^{-YD}(D+J)` is decreasing for `D>=D_0`, the boundary term is bounded at the left endpoint, while the integral can be extended to infinity. Hence

\[
\boxed{
\mathcal T(D_0,D_1)
\ll
 e^{-YD_0}
\left(D_0+J+1\right),
}
\tag{26}
\]

uniformly in every `D_1<=c_B L`.

Therefore, whenever

\[
D_0\to\infty,
\qquad
YD_0-\log J\to+\infty,
\qquad
D_0<c_B L,
\tag{27}
\]

one has

\[
\boxed{
\sup_{D_0<D_1\le c_B L}
\mathcal T(D_0,D_1)
=o(1).
}
\tag{28}
\]

Because the signed residue is bounded by this absolute mass, every moving shallow depth above that threshold is harmless simultaneously; no cancellation among zero phases is required.

A convenient parameterization is

\[
D_0
=
\frac{\log J+w(Q)}{Y},
\qquad
w(Q)\to\infty.
\tag{29}
\]

Provided this lies inside the Bellotti range, (26) becomes

\[
\mathcal T(D_0,D_1)
\ll
 e^{-w(Q)}
+
\frac{\log J+w(Q)}{J}e^{-w(Q)}
=o(1).
\tag{30}
\]

This is the quantitative form of the logarithmic carrier-width cutoff.

## 5. The width/depth phase diagram

The law is easiest to read through examples. Since `J~R/H` when the shell is sublinear, the dangerous depth scale is

\[
D_{\rm width}
:=
\frac1Y\log\!\left(1+\frac RH\right).
\tag{31}
\]

If `H=Theta(R)`, then `J=O(1)` and `D_width=O(1)`. Every moving depth `D->infinity` inside Bellotti's local range is absolutely negligible. This is the population mechanism already exploited by `NB-224`, now expressed in the depth language of `NB-228`--`NB-229`.

If

\[
\frac RH=L^A
\]

for fixed `A>0`, then

\[
D_{\rm width}
=\frac{A}{Y}\log L+O(1).
\tag{32}
\]

The broad `D=o(L)` frontier of `NB-229` collapses to only logarithmic-in-`L` depth.

More generally, if

\[
\frac RH=\exp(L^\alpha),
\qquad
0<\alpha<1,
\]

then

\[
D_{\rm width}
=\frac1Y L^\alpha+O(1).
\tag{33}
\]

Again, every moving depth satisfying `L^alpha<<D<<L` is already controlled by the existing local theorem.

By contrast, if `H` is a fixed power of `R` strictly below one, then `log(R/H)=Theta(L)`. In that regime the width cutoff remains on the same `Theta(L)` scale as the coarse localization of `NB-229`; no asymptotic compression should be claimed from (31). Fixed-width shells lie in this genuinely hard regime.

Thus the relevant distinction is not simply `H=o(R)` versus `H=Theta(R)`. The finer source parameter is

\[
\boxed{
\log(R/H),
}
\tag{34}
\]

because Ford damping turns a linear vertical-capacity loss into a logarithmic horizontal-depth budget.

## 6. Relation to the matched packets of `NB-225`--`NB-227`

The new upper envelope explains why the earlier adversarial packets choose logarithmic depth.

`NB-225` sets

\[
J_0=\frac RH,
\qquad
M=\min\{J_0^{1/2},L\},
\qquad
D=\frac{\log M}{Y},
\tag{35}
\]

and places `M` phase-aligned zeros at common depth `D`. Their Ford factor is

\[
e^{-YD}=M^{-1},
\]

so the population `M` and the damping cancel exactly. When `J_0<=L^2`, this gives

\[
D=\frac{1}{2Y}\log J_0,
\tag{36}
\]

which is the same logarithmic carrier-width scale as (31), up to the deliberately conservative factor `1/2` used to keep the packet in a flat part of the carrier.

`NB-226` replaces full phase alignment by a fixed-power discrepancy `M^vartheta` and moves the common depth to

\[
D=\frac{\vartheta}{Y}\log M.
\tag{37}
\]

Again the relevant depth is logarithmic in the available vertical population. `NB-227` then shows that multiplying a separable phase law by an arbitrarily strong predetermined depth penalty does not solve the problem because the packet may let this logarithmic depth diverge sufficiently slowly.

Equations (31)--(37) put the positive and negative sides in the same currency. Bellotti's local count says that the carrier can supply at most about `J` extra absolute population beyond the horizontal-depth term. Ford damping charges `e^{YD}` for an order-one residue. The balance is therefore exactly

\[
J\approx e^{YD}.
\tag{38}
\]

The existing packets show that this balance is not merely an artifact of taking absolute values. At least in the moderately sublinear regimes where their conservative construction can use a power of `J`, coherent matched controls live on the same logarithmic depth scale.

For extremely narrow shells with `log J=Theta(L)`, the packet constructions in `NB-225`--`NB-227` do not prove sharpness all the way to the upper envelope (31); they intentionally use smaller populations to stay within every other published density allowance. The remaining gap there is real and should not be hidden by the present synthesis.

## 7. What this changes in the research frontier

The phrase “uniform zero density for every `1<<D<<L`” is now too strong as the next target. The existing Bellotti local-disk theorem already supplies the required subcritical population bound whenever

\[
D\gg \log\!\left(1+\frac RH\right)
\tag{39}
\]

inside its range.

The unresolved source-side theorem can therefore be localized further. For a given shell width, the interesting moving depths are

\[
\boxed{
1\ll D
\lesssim
\frac1Y\log\!\left(1+\frac RH\right),
}
\tag{40}
\]

plus any `Theta(L)` transition interval lying beyond the admissible radius of the local-disk lemma and before the coarse `NB-229` tail cutoff. When `log(R/H)=o(L)`, (40) is a genuine asymptotic reduction of the moving shallow gap.

Inside (40), population information alone may still be insufficient, as the matched packets demonstrate. The live improvements remain genuinely joint: a local estimate that couples vertical population with horizontal depth more strongly than `D+R/H`, a phase-sensitive bound for `mathcal C(D)`, or an arithmetic restriction showing that the abstract packet geometry cannot occur for actual zeta zeros.

The destination bridge is unchanged. Even a complete source-side residue estimate would not by itself prove a quantitative Nyman--Beurling distance lower bound; the line still lacks a theorem forcing a successful Nyman approximant to realize the particular positive Euler return tested here.

## 8. Adversarial and prior-art audit

The main falsification check is the Stieltjes step. Equation (26) does **not** infer a tail bound from a pointwise estimate at one chosen depth. It integrates the monotone absolute population law (14) over the whole slab, preserving the Ford weight. This is why the carrier-capacity term `J` becomes `J e^{-YD_0}` rather than being paid independently at every depth.

A second check is the Bellotti range. Nothing here extrapolates Lemma 2.4 past `D<=c_B L`. Equation (28) is explicitly restricted to that range. `NB-229` separately controls sufficiently deep zeros by the crude global carrier budget, but the two intervals need not overlap for every fixed exact-Ford constant `Y_*` and every shell width. The possible `Theta(L)` transition band is therefore left open rather than silently patched.

A third check is multiplicity. Bellotti's local count and the ordinary zero-counting laws used in `NB-224` count zeros with multiplicity, and `mathcal M` carries the same multiplicity. No simplicity assumption is introduced.

The arithmetic input is exactly the Bellotti local zero-disk estimate already used and audited in `NB-224` and already anchored in this research line's sources. No new external theorem is load-bearing, so `SOURCES.md` requires no change. The passage from `M(D)<<D+J` to the logarithmic cutoff is generic Laplace/Stieltjes geometry; the zeta-specific content is that Bellotti supplies that population law at the Vinogradov--Korobov scale and that the explicit formula supplies the damping `e^{-YD}`.

The representation audit therefore separates cleanly:

- **generic:** a cumulative weighted population `O(D+J)` under exponential damping `e^{-YD}` can only sustain critical mass through depth `D=O(log J)`;
- **zeta-specific:** `D=R(1-beta)`, `J=R/H`, Bellotti's local disk population, and the exact moving-shell residue coefficient;
- **not proved:** any new theorem about actual zeta zero correlations, any elimination of the narrow-shell matched packets, or any Nyman--Beurling destination rate.

## Research consequence

The shallow Ford problem has a second localization parameter beyond `L=log Q`: the vertical carrier capacity `R/H`. Existing local zero counts already force its effect through the much smaller quantity

\[
\boxed{
D_{\rm width}
=\frac1Y\log\!\left(1+\frac RH\right).
}
\]

For near-wide shells this removes most of the moving shallow interval that `NB-229` had left open. For very narrow shells the cutoff rises back to `Theta(L)`, consistent with the matched-control obstructions of `NB-225`--`NB-227`.

The next source-side search should therefore be parameterized by `D/log(1+R/H)`, not by `D/L` alone. A candidate theorem that only improves global zero density outside this carrier-width window is solving a region that Bellotti's existing local theorem already makes subcritical.
