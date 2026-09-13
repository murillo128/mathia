# RE-085 — long mixed fans are first-layer in normalized physical event mass

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + SAME-BLOCK-LONG-STRETCH + PHYSICAL-EVENT-MEASURE + TOTAL-VARIATION-COLLAPSE + FIRST-LAYER-ENDPOINT-RECONSTRUCTION + FIXED-ORDER-STATISTIC-COLLAPSE + NEGATIVE/ROUTE-NARROWING + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-083`--`RE-084` show that the complete first-layer event configuration on an arbitrary mixed fan segment is already reconstructed from the selected endpoints, while `RE-081` shows that higher-layer atoms are negligible in the two Lyapunov transport moments on a stretched same-block fan. The remaining possibility is that the **relative placement** of first- and higher-layer physical thresholds could still carry leading information even though the higher-layer transport mass itself is small.

For every bounded observable of the physical event measure, that possibility also collapses on the stretched branch. In fact the entire log-mass-normalized mixed CA event measure converges in total variation to its first-layer part, and the latter is endpoint-determined. Consequently every fixed-order bounded mass-polynomial statistic of event locations has the same asymptotic value after all higher-layer events are deleted. Any viable cross-layer obstruction must therefore be singular with respect to event log-mass — for example adjacency, conditioning on an exceptional higher-layer event, or a state-selection rule whose sensitivity can remain order one when the higher-layer mass tends to zero.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\]

and take a long-stretched same-block family exactly as in `RE-080`--`RE-084`, with ordered selected endpoints

\[
C_0<C_1,
\qquad
Y_i:=\log C_i,
\qquad
Z_i:=Z_{b_i}(C_i),
\qquad
r:=Y_1/Y_0\longrightarrow\infty.
\tag{1}
\]

Let `E_01` be the multiset of all physical CA layer events crossed between `C_0` and `C_1`. If an event raises the exponent of a prime `p` from `j-1` to `j`, put its atom at the exact event coordinate `eta_(p,j)` and give it its logarithmic state mass `log p`:

\[
\boxed{
\nu_{01}
:=\sum_{(p,j)\in\mathcal E_{01}}
(\log p)\,\delta_{\eta_{p,j}}.
}
\tag{2}
\]

Split

\[
\nu_{01}=\nu_1+\nu_{\ge2}
\tag{3}
\]

according to `j=1` and `j>=2`. Write

\[
L_{01}:=Y_1-Y_0,
\qquad
R_{01}:=\log\operatorname{rad}(C_1)-\log\operatorname{rad}(C_0),
\qquad
P_{01}:=P_{C_1}-P_{C_0},
\tag{4}
\]

where `P_C` is the active depth-at-least-two log-mass of `RE-081`. Then the event decomposition gives the exact identities

\[
\boxed{
\nu_{01}(\mathbb R)=L_{01},
\qquad
\nu_1(\mathbb R)=R_{01},
\qquad
\nu_{\ge2}(\mathbb R)=P_{01},
\qquad
L_{01}=R_{01}+P_{01}.
}
\tag{5}
\]

On the stretched branch, `RE-081` gives

\[
P_{01}
\ll \sqrt{Z_1}(\log Z_1)^{3/2},
\tag{6}
\]

while `RE-080` gives `Z_1\sim Y_1` and (1) gives `L_01=(1+o(1))Y_1`. Hence

\[
\boxed{
\varepsilon_{01}:=\frac{P_{01}}{L_{01}}
\ll
Y_1^{-1/2}(\log Y_1)^{3/2}
\longrightarrow0.
}
\tag{7}
\]

Normalize the full and first-layer measures by

\[
\bar\nu:=\frac{\nu_{01}}{L_{01}},
\qquad
\bar\nu_1:=\frac{\nu_1}{R_{01}}.
\tag{8}
\]

For every bounded measurable function `F`, positivity and (5) give

\[
\boxed{
\left|
\int F\,d\bar\nu-
\int F\,d\bar\nu_1
\right|
\le
2\|F\|_\infty\,\varepsilon_{01}.
}
\tag{9}
\]

Thus, in the dual total-variation norm,

\[
\boxed{
\|\bar\nu-\bar\nu_1\|_{\mathrm{TV},*}
\le2\varepsilon_{01}
\ll
Y_1^{-1/2}(\log Y_1)^{3/2}
\to0,
}
\tag{10}
\]

where `||rho||_(TV,*) := sup_(||F||_infty<=1) |int F d rho|`. No regularity of `F` is required for (9).

The limit measure is not an unknown first-layer object. Let

\[
\mathcal B_{01}:=\{p:p\nmid C_0,\ p\mid C_1\}
\tag{11}
\]

be the first-layer births. `RE-083` reconstructs this prime set exactly from the endpoint selector primes and the two possible fringe primes, and `RE-084` then reconstructs every exact threshold `eta_p=eta_(p,1)`. Therefore

\[
\boxed{
\nu_1
=\sum_{p\in\mathcal B_{01}}(\log p)\delta_{\eta_p}
}
\tag{12}
\]

is completely determined by the selected endpoint data.

Moreover define the translated ordinary-prime measure

\[
\nu_{\mathrm{pr}}
:=\sum_{p\in\mathcal B_{01}}
(\log p)\delta_{p+1/2}.
\tag{13}
\]

The uniform half-delay law of `RE-084` gives, for every Lipschitz `F`,

\[
\boxed{
\left|
\frac1{R_{01}}\int F\,d\nu_1
-
\frac1{R_{01}}\int F\,d\nu_{\mathrm{pr}}
\right|
\ll
\frac{\operatorname{Lip}(F)}{\log Z_0}.
}
\tag{14}
\]

Combining (9) and (14),

\[
\boxed{
\left|
\int F\,d\bar\nu
-
\frac1{R_{01}}\int F\,d\nu_{\mathrm{pr}}
\right|
\ll
\|F\|_\infty
Y_1^{-1/2}(\log Y_1)^{3/2}
+
\frac{\operatorname{Lip}(F)}{\log Z_0}.
}
\tag{15}
\]

Thus every uniformly bounded, uniformly Lipschitz one-event observable of the **complete mixed physical staircase** is asymptotically the same observable of an endpoint-reconstructed ordinary-prime point configuration translated by `1/2`.

The collapse also survives any fixed finite degree. For every fixed integer `k>=1` and bounded measurable `F` on `R^k`, telescoping the product measures gives

\[
\boxed{
\left|
\int F\,d\bar\nu^{\otimes k}
-
\int F\,d\bar\nu_1^{\otimes k}
\right|
\le
2k\|F\|_\infty\,\varepsilon_{01}.
}
\tag{16}
\]

Hence every bounded fixed-order mass-polynomial statistic formed by sampling finitely many event locations according to logarithmic event mass is asymptotically first-layer and endpoint-determined. Merely replacing a linear event observable by a bounded quadratic, cubic, or any fixed finite-order correlation cannot recover an order-one higher-layer assembly signal.

## 1. The physical event measure has an exact mass decomposition

Every event `(p,j)` multiplies the CA state by `p`, so it increments `Y=log C` by exactly `log p`. Summing all crossed events proves the first identity in (5).

A first-layer event creates a new radical factor `p`, hence contributes `log p` to `log rad(C)` and nothing to `P_C`. Every later event at the same prime leaves the radical fixed and contributes `log p` to `P_C`. Therefore the `j=1` atoms sum exactly to `R_01`, the `j>=2` atoms sum exactly to `P_01`, and

\[
Y-\log\operatorname{rad}(C)=P_C
\]

proves the final identity in (5) directly.

Ties create no ambiguity. Several labeled events may occupy the same physical coordinate, but (2) is a positive multiset measure, so coincident atoms simply add their masses. The argument never assumes the Alaoglu--Erdos prime-quotient conjecture or single-event transitions.

## 2. Long stretch makes every bounded higher-layer event observable vanish in mass

Write

\[
\nu_{01}=\nu_1+\nu_{\ge2},
\qquad
L_{01}=R_{01}+P_{01}.
\]

Then for any bounded `F`,

\[
\begin{aligned}
\int F\,d\bar\nu-
\int F\,d\bar\nu_1
={}&
\left(\frac1{L_{01}}-\frac1{R_{01}}\right)
\int F\,d\nu_1
+
\frac1{L_{01}}\int F\,d\nu_{\ge2}.
\end{aligned}
\tag{17}
\]

The absolute value of the first term is at most

\[
\|F\|_\infty\left(1-\frac{R_{01}}{L_{01}}\right)
=\|F\|_\infty\frac{P_{01}}{L_{01}},
\tag{18}
\]

and the second has the same bound. This proves (9) exactly. Equation (7) then follows from the higher-layer mass ceiling of `RE-081` and the long-stretch scale `L_01~Y_1`.

This is different from the transport statement in `RE-081`. There the higher-layer atoms are negligible relative to the corrected Chebyshev and Robin-kernel moments of the adaptive fan measure `mu`. Here the object is the **complete physical CA event point process itself**, first layer included, normalized by the actual logarithmic growth of the state. The conclusion is correspondingly about what can be extracted from mixed event placement before applying the fan transport kernel.

## 3. Endpoint reconstruction upgrades the small-mass statement to an information collapse

Small higher-layer mass alone would only say that most physical state growth comes from first-layer births. `RE-083`--`RE-084` make this stronger: the dominant first-layer point measure carries no hidden mixed-assembly freedom once the selected endpoints are fixed.

Specifically, `RE-083` gives the exact multiset identity

\[
\{q\text{ prime}:Z_0<q\le Z_1\}
\uplus\chi_0\{r_0\}
=
\mathcal B_{01}
\uplus\chi_1\{r_1\},
\tag{19}
\]

and `RE-084` applies the deterministic threshold map `p mapsto eta_p` to reconstruct (12), including order. Its uniform expansion

\[
\eta_p=p+\frac12+O(1/\log Z_0)
\tag{20}
\]

then proves (14).

For product observables, write the difference of `k`-fold product measures as the telescoping sum obtained by replacing one factor at a time,

\[
\bar\nu^{\otimes k}-\bar\nu_1^{\otimes k}
=
\sum_{m=1}^k
\bar\nu^{\otimes(m-1)}\otimes
(\bar\nu-\bar\nu_1)\otimes
\bar\nu_1^{\otimes(k-m)}.
\tag{21}
\]

Each surrounding factor is a probability measure, so (9) bounds each term by `2 ||F||_infty epsilon_01`, proving (16).

Equation (16) is deliberately limited to fixed-order **mass-polynomial** observables. It does not claim that all nonlinear statistics of the staircase are continuous in this metric.

## 4. What remains genuinely cross-layer

The result does **not** make higher-layer events irrelevant. A single higher-layer event can split a first-layer chamber, tie another event, alter the exponent vector permanently, or change which CA states are exposed by the adaptive convex envelope. Such effects can remain order one even though the higher-layer event carries vanishing normalized log-mass.

For exactly that reason, nearest-neighbor adjacency, existence of an exceptional event, conditional statistics given that such an event occurs, and the rightmost-maximizer/state-selection map are outside (9)--(16). They are singular observables from the viewpoint of normalized event mass: deleting an arbitrarily small amount of mass can change them discontinuously.

This identifies a sharper boundary after `RE-084`. Relative first/higher threshold placement cannot matter at leading order merely through any bounded finite-order statistic of the mixed physical event distribution. A successful cross-layer theorem must instead exploit one of the singular channels left above — most naturally, how a sparse higher-layer threshold changes **admissible adjacent states or supporting slopes**, or a source estimate conditioned specifically on the exceptional higher-layer locations. Equivalently, any mass-based observable that still sees higher layers at order one must amplify their contribution by a factor at least comparable to `epsilon_01^{-1}` along the stretched family.

The last statement is a scaling requirement, not a sufficiency claim. An unbounded amplification can just as easily magnify noise or restate the desired Robin estimate.

## 5. Falsification and prior-art boundary

The long-stretch hypothesis is load-bearing. On a bounded-dilation segment, (6) alone does not force `P_01/(Y_1-Y_0)` to vanish, so no total-variation collapse is asserted there.

The normalization is also load-bearing. Higher layers have zero asymptotic **log-mass fraction** on the stretched branch, but they can have nonzero existence probability under a statistic that first conditions on the exceptional set. Count density, physical Lebesgue density, and event-mass density are different notions; (10) concerns only the last one.

Likewise, fixed `k` in (16) cannot grow with scale. Taking a number of samples comparable to `epsilon_01^{-1}` can detect the rare component with order-one probability, exactly as the scaling discussion predicts.

Alaoglu--Erdos supplies the classical prime-exponent threshold staircase, while Mantovanelli's 2026 preprint and computational companion provide the closest prior-art event-measure and packet-bookkeeping framework. `RE-004` already proves zero **count** density of higher-layer transition coordinates, and `RE-081` already proves negligible higher-layer mass in the two adaptive Lyapunov moments. A directed current search of the CA/Robin prime-layer literature found no statement combining the physical event-mass normalization with the endpoint reconstruction of `RE-083`--`RE-084` to obtain the total-variation and fixed-order collapse (9)--(16). No external theorem beyond sources already anchored in `SOURCES.md` is load-bearing, so that file requires no change.

The durable narrowing is therefore not that higher layers disappear. It is that on a stretched false-RH fan **their only possible leading influence is singular**. Regular bounded observables of the mixed event mass asymptotically see only the endpoint-determined first layer.