# RE-083 — mixed fan segments have exact first-layer support conservation and only a summable timing tax

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + MIXED-FAN-SEGMENT + FIRST-LAYER-SUPPORT-CONSERVATION + UNIQUE-FACTORIZATION + TIMING-TAIL + LONG-FAN + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-082` leaves the discrete assembly of genuine CA states as the live obstruction after showing that the smooth common-amplitude selector law itself already realizes the complementary long-fan transport front. One natural arithmetic input left on that frontier is ordinary-prime first-layer conservation: perhaps the genuine prime support cannot keep feeding the smooth selector-dilation profile over a long fan once higher-layer events are interleaved.

At the endpoint/additive level, that hope fails exactly. The first-layer prime-set conservation of `RE-068` does **not** require a first-layer-only packet. It extends to every ordered pair of selected fan states, with arbitrary higher-layer events between them. Higher layers cancel because the adjusted Chebyshev identity of `RE-059` is already the logarithm of the radical.

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on a sufficiently late common positive CA counterexample block from `RE-040`. Take any two ordered selected states on its rightmost threshold fan,

\[
C_0<C_1,
\qquad
Y_i:=\log C_i,
\qquad
Z_i:=Z_{b_i}(C_i),
\qquad
Z_0<Z_1.
\tag{2}
\]

At each endpoint write the standard first-layer correction as

\[
\delta_\vartheta(Z_i)=\chi_i\log r_i,
\qquad
\chi_i\in\{0,1\},
\tag{3}
\]

with the prime `r_i` omitted when `chi_i=0`. Let

\[
\mathcal S_{01}:=\{q\text{ prime}:Z_0<q\le Z_1\}
\tag{4}
\]

be the ordinary primes crossed by the selector, and let

\[
\mathcal B_{01}
:=\{p\text{ prime}:p\nmid C_0,\ p\mid C_1\}
\tag{5}
\]

be the primes whose first layer is born between the two CA states. Equivalently, `B_01` is the set of labels `(p,1)` among the complete physical CA events crossed between `C_0` and `C_1`. There is no restriction on the number or depths of the other events in the segment.

Then the exact multiset identity is

\[
\boxed{
\mathcal S_{01}\uplus\chi_0\{r_0\}
=
\mathcal B_{01}\uplus\chi_1\{r_1\}.
}
\tag{6}
\]

Consequently, for **every** function `w` on the ordinary primes,

\[
\boxed{
\sum_{Z_0<q\le Z_1}w(q)+\chi_0w(r_0)
=
\sum_{p\in\mathcal B_{01}}w(p)+\chi_1w(r_1).
}
\tag{7}
\]

Thus interleaving arbitrarily many higher-layer events cannot create an additive first-layer source mismatch. The genuine mixed CA staircase crosses exactly the same ordinary-prime support set as the adjusted selector, up to the one possible pending prime at each endpoint.

The only first-layer datum not contained in this endpoint set identity is the delay between an ordinary prime and its first CA event. Retain the timing discrepancy of `RE-069`,

\[
\mathfrak B_1(x)
:=\vartheta(x)-\Phi_1(x)
=\sum_p(\log p)\mathbf 1_{[p,\eta_p)}(x),
\tag{8}
\]

where `eta_p=eta_(p,1)` is the first-layer event coordinate. Put

\[
R_{01}
:=\log\operatorname{rad}(C_1)
-\log\operatorname{rad}(C_0)
=\sum_{p\in\mathcal B_{01}}\log p.
\tag{9}
\]

Then, uniformly on late mixed fan segments,

\[
\boxed{
\int_{Z_0}^{Z_1}\mathfrak B_1(x)\,dx
=
\frac12R_{01}
+O\!\left(
\frac{R_{01}}{\log Z_0}+\log Z_1
\right),
}
\tag{10}
\]

while the same timing transport against the exact Robin kernel has the packet-cardinality-free bound

\[
\boxed{
\left|
\int_{Z_0}^{Z_1}\mathfrak B_1(x)g'(x)\,dx
\right|
\ll \frac1{Z_0},
\qquad
g(x)=\frac1{x\log x}.
}
\tag{11}
\]

The contrast is especially sharp on the long same-block branch of `RE-080`. If

\[
r:=Y_1/Y_0\to\infty,
\tag{12}
\]

then `RE-081` gives

\[
P_{C_1}-P_{C_0}
=o(Y_1),
\tag{13}
\]

where `P_C` is the active depth-at-least-two log-mass. Hence

\[
\boxed{R_{01}=(1+o(1))Y_1,}
\tag{14}
\]

and therefore

\[
\boxed{
\int_{Z_0}^{Z_1}\mathfrak B_1(x)\,dx
=\left(\frac12+o(1)\right)Y_1.
}
\tag{15}
\]

So first-layer timing remains macroscopically present in the flat metric even on a mixed long fan. Nevertheless its direct Robin-kernel contribution is still only `O(1/Y_0)`. The full reciprocal-weighted long-fan transport of `RE-080` satisfies

\[
W\gg_JY_0^{-b_1},
\tag{16}
\]

and therefore

\[
\boxed{
\frac{
\left|\int_{Z_0}^{Z_1}\mathfrak B_1g'\right|
}{W}
\ll_JY_0^{b_1-1}
\longrightarrow0.
}
\tag{17}
\]

Thus the ordinary-prime first layer occupies an interesting but strategically restrictive position in the long-fan assembly. It carries essentially all of the radical growth and an order-`Y_1` raw timing area, yet its endpoint additive content is already fixed exactly by the selector prime set, while its direct contribution through the exact Robin kernel is summable and asymptotically negligible. A source-specific contradiction after `RE-082` therefore cannot come from **first-layer conservation in isolation**, nor from feeding the first-layer delay discrepancy linearly into the Robin workload. It must use information that survives both collapses: the nonlinear way first-layer event positions constrain support chambers and tied spans, the ordering/interleaving with higher-layer thresholds, or another joint functional that does not factor through the endpoint support multiset and the linear `g'` timing tax.

## 1. The adjusted Chebyshev identity is already a support identity

For a selected state `C` with tangent selector `Z`, `RE-059` proves

\[
\vartheta(Z)-\delta_\vartheta(Z)=Y-P_C,
\tag{18}
\]

where

\[
P_C=\Phi_{\ge2}(Z)
\tag{19}
\]

is the total active higher-layer log-mass. But the full event mass is exactly

\[
Y=\sum_{p^a\Vert C}a\log p,
\tag{20}
\]

while the depth-at-least-two part is

\[
P_C=\sum_{p^a\Vert C}(a-1)\log p.
\tag{21}
\]

Therefore

\[
\boxed{
Y-P_C
=\sum_{p\mid C}\log p
=\log\operatorname{rad}(C).
}
\tag{22}
\]

Substituting (3) into (18) gives the exact pointwise relation

\[
\boxed{
\vartheta(Z_i)-\chi_i\log r_i
=\log\operatorname{rad}(C_i).
}
\tag{23}
\]

Exponentiating,

\[
\boxed{
\frac{\displaystyle\prod_{q\le Z_i}q}
{r_i^{\chi_i}}
=\operatorname{rad}(C_i).
}
\tag{24}
\]

Every factor on both sides is an ordinary prime. Unique factorization therefore upgrades the logarithmic equality to equality of prime sets:

\[
\boxed{
\{q\text{ prime}:q\le Z_i\}
=
\{p:p\mid C_i\}\uplus\chi_i\{r_i\}.
}
\tag{25}
\]

This is the pointwise form of first-layer conservation. It does not mention what happened between selected states. Higher layers have disappeared because they change `Y` and `P_C` by the same `log p` and hence leave `Y-P_C=log rad(C)` unchanged.

The physical CA event sweep is monotone in the exponent vector as the supporting parameter decreases, so between ordered states `C_0<C_1` the prime support grows exactly by the first-layer births `B_01`. Subtracting the two finite prime-set identities (25) proves (6). Equation (7) is then immediate and requires no analytic estimate.

This extends `RE-068` in the direction that matters after `RE-081`--`RE-082`. `RE-068` assumed that the complete packet itself was first-layer-only so that `P_C` was frozen. The pointwise radical form (22) shows that this freezing was stronger than necessary: arbitrary higher-layer motion cancels before the endpoint prime-set comparison is made.

## 2. Mixed first-layer timing has one bulk term and at most two boundary pulses

The exact first-layer threshold equation gives

\[
g(\eta_p)
=\frac{\log(1+p^{-1})}{\log p},
\tag{26}
\]

and `RE-069` derives

\[
\eta_p-p
=\frac12-
\frac1{2(\log p+1)}+O(p^{-1}).
\tag{27}
\]

For sufficiently late primes these delay intervals are short and disjoint. Equation (25) also tells us exactly how they sit relative to an arbitrary selected segment.

If a prime `p` is born strictly inside the segment and is not the lower fringe prime, then both

\[
Z_0<p<\eta_p\le Z_1
\tag{28}
\]

hold, so its whole delay pulse lies inside `[Z_0,Z_1]`. Conversely, every ordinary prime strictly crossed by the selector has its first-layer event inside the segment unless it is the upper fringe prime. Therefore all mismatch between the pulse integral over `[Z_0,Z_1]` and the sum of complete birth pulses is confined to the possible lower and upper fringe pulses. Their total flat area is

\[
O(\log Z_1),
\tag{29}
\]

because each delay has length below `1/2` eventually.

It follows that

\[
\int_{Z_0}^{Z_1}\mathfrak B_1(x)\,dx
=
\sum_{p\in\mathcal B_{01}}
(\log p)(\eta_p-p)
+O(\log Z_1).
\tag{30}
\]

Insert (27). Since every nonboundary birth has `p>Z_0` and the possible lower boundary prime only changes the estimate by `O(log Z_1)`,

\[
\sum_{p\in\mathcal B_{01}}
\frac{\log p}{\log p+1}
\ll
\frac{R_{01}}{\log Z_0}+\log Z_1,
\tag{31}
\]

and

\[
\sum_{p\in\mathcal B_{01}}
\frac{\log p}{p}
\ll
\frac{R_{01}}{Z_0}+rac{\log Z_1}{Z_0}.
\tag{32}
\]

Equations (30)--(32) prove (10). In the fringe-free case the boundary error disappears entirely, recovering the half-mass phenomenon of `RE-069` without any first-layer-only assumption.

The Robin-kernel estimate needs even less structure. `RE-069` proves globally that one complete timing pulse has exact cost

\[
\kappa_p
:=-\int_p^{\eta_p}(\log p)g'(x)\,dx
=
\frac1p-\log\left(1+\frac1p\right),
\tag{33}
\]

with

\[
0<\kappa_p<\frac1{2p^2}.
\tag{34}
\]

Since `mathfrak B_1>=0` and `g'<0`, any finite interval beginning at `Z_0` is dominated by the whole future tail. Hence

\[
\left|
\int_{Z_0}^{Z_1}\mathfrak B_1g'
\right|
\le
-\int_{Z_0}^{\infty}\mathfrak B_1g'
\ll Z_0^{-1},
\tag{35}
\]

which is (11). No purity, fringe condition, packet cardinality, or long-fan hypothesis enters this bound.

## 3. On a stretched fan, almost all intrinsic growth is first-layer support growth

For any selected endpoint, (22) can be rearranged as

\[
\log\operatorname{rad}(C)=Y-P_C.
\tag{36}
\]

Therefore

\[
R_{01}
=(Y_1-Y_0)-(P_{C_1}-P_{C_0}).
\tag{37}
\]

On the long-stretched branch of `RE-080`, `Y_1/Y_0=r->infinity`, so

\[
Y_1-Y_0=(1+o(1))Y_1.
\tag{38}
\]

`RE-081` identifies the higher-layer increment with the entire discrete higher-layer transport mass and proves

\[
0\le P_{C_1}-P_{C_0}
\ll
\sqrt{Z_1}(\log Z_1)^{3/2}
=o(Y_1),
\tag{39}
\]

because `Z_1~Y_1`. Substituting into (37) gives (14), and (10) then gives (15). Thus the statement that higher-layer atoms are negligible has a complementary support interpretation: **almost all logarithmic state growth on a stretched fan comes from new ordinary-prime support births.**

This does not revive first-layer conservation as an obstruction. Equation (6) says that those many births are exactly the ordinary primes crossed by the adaptive selector, modulo the two endpoint fringe bits. Their additive arithmetic content is therefore already reconciled. Nor does their large raw timing area revive the direct workload route: (17) shows that the exact Robin derivative kernel suppresses it below the long-fan reciprocal moment by a fixed power.

The combination is stronger than either negative statement separately. The first layer is not negligible in cardinality, log-mass, or flat timing geometry; it is in fact the dominant support-growth layer. What is exhausted is the **information channel** provided by its endpoint additive statistics and its linear delayed-event Robin tax.

## 4. Stress tests and what remains available

The result does not say that first-layer event locations are irrelevant to the fan. They determine genuine CA chamber boundaries and can constrain how smooth common-amplitude arcs splice to fixed-state cells. `RE-043`--`RE-050` exploit exactly such placement information. Equation (11) rules out only the direct linear workload accumulated from the delays after the staircase has already been formed.

Nor does (6) remove higher layers from the assembly problem. Higher-layer events do not alter the radical, but their thresholds change the exponent vector, the supporting slopes, and the order in which exposed states become available. A nonlinear statistic depending on the **interleaving** of first-layer and higher-layer events is not determined by the endpoint prime set and is untouched here.

The endpoint fringe corrections are load-bearing for exactness. Without them, a selector can cross an ordinary prime before its first-layer event and the raw support sets differ by one prime. `RE-052` ensures that there is at most one such pending prime per late support chamber, which is why the boundary error in (10) remains only `O(log Z_1)`.

Equation (25) is also not presented as a new theorem about the support shape of CA numbers. The fact that CA exponent profiles are organized prime by prime is classical. The line-specific point is the adaptive-selector identity: after the exact fringe correction, the primes below the selected tangent coordinate are **exactly** the radical support of the selected state, and this converts `RE-068` from a pure first-layer packet statement into an arbitrary mixed-segment conservation law.

Finally, the long-fan statements (14)--(17) are conditional on the same hypothetical false-RH stretched blocks used in `RE-080`--`RE-082`. They do not assert that such fans exist unconditionally, nor do they turn the negative control into evidence against RH.

## 5. Prior-art boundary and next target

Alaoglu--Erdos is the classical source for the CA prime-exponent threshold structure and monotone prime support. Mantovanelli's 2026 prime-layer workload is the closest recent framework for exact event bookkeeping, endpoint factorization, packet-mass conservation, and the prime-frontier decomposition. A directed current search found no statement combining the adaptive endpoint fringe correction with arbitrary **mixed** fan segments to obtain (6), nor the subsequent long-front conclusion that the dominant first-layer support growth is simultaneously additive-source-silent and Robin-kernel-timing-negligible. No external theorem beyond sources already anchored in `SOURCES.md` is load-bearing here, so that file requires no change.

The practical consequence is a further narrowing of the `RE-082` assembly frontier. “Use ordinary-prime first-layer conservation” is not enough if it means endpoint prime sets or any additive prime weight: those are identities for every mixed segment. “Use the first-layer delay” is not enough if it means its direct linear contribution to the exact Robin workload: its entire future tail is summable. A viable source-specific theorem now has to use information that is genuinely joint and non-additive — for example the allowed **ordering and spacing of first- and higher-layer thresholds inside the support staircase**, the admissible tied-switch spans determined by those thresholds, or a nonlinear coupling between selector dilation and event placement before the `g'` integration collapses the timing data.