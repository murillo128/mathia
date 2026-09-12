# RE-076 — endpoint-corrected Chebyshev deficit is a global radical-gap Lyapunov coordinate

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + GLOBAL-FAN-LYAPUNOV + RADICAL-GAP-IDENTITY + ARBITRARY-PACKET + CHEBYSHEV-NO-RESET + MATCHED-RUN-ACCUMULATION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-072` proves one-sided Chebyshev drift only while the selected fan remains in consecutive matched `0 -> 0` first-layer packets. `RE-074`--`RE-075` then price how later fan motion could recover the reciprocal Mertens source, but they leave the standard Chebyshev source looking as though higher-layer, unmatched, or arbitrarily large packets might reset it as well.

They cannot, once the single ordinary-prime fringe correction is retained.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on a sufficiently late common positive CA counterexample block from `RE-040`. For any selected state `C` on the oriented rightmost fan write

\[
Y:=\log C,
\qquad Z:=Z_b(C),
\qquad
H_\vartheta(Z):=Z-\vartheta(Z),
\tag{2}
\]

and let `delta_vartheta(Z)` be the binary first-layer fringe correction of `RE-059`. Define the corrected deficit

\[
\widehat H(C,b)
:=H_\vartheta(Z)+\delta_\vartheta(Z).
\tag{3}
\]

Then `RE-059` gives the exact identity

\[
\boxed{
\widehat H(C,b)
=Z-\log\operatorname{rad}(C)
=(Z-Y)+P_C,
}
\tag{4}
\]

where `P_C` is the total active depth-at-least-two CA event mass. The quantity in (4) is a **strict Lyapunov coordinate for the whole late rightmost fan**: it increases inside every exposed threshold cell and across every exposed-state switch, with no restriction on packet cardinality, layer composition, or fringe pattern.

More precisely, inside a fixed-state cell,

\[
\boxed{
\frac{d}{db}\widehat H(C,b)=\frac{dZ_C}{db}>0.
}
\tag{5}
\]

At a breakpoint `b in J`, let `C_-<C_+` be two successive exposed states, put `Y_\pm=\log C_\pm`, and let `Z_\pm` be their tied selectors. If `P_{\ge2}(-,+)` denotes the total logarithmic mass of all higher-layer event occurrences in the complete physical packet from `C_-` to `C_+`, then exactly

\[
\boxed{
\widehat H_+-\widehat H_-
=
\bigl[(Z_+-Y_+)-(Z_--Y_-)\bigr]
+P_{\ge2}(-,+).
}
\tag{6}
\]

The first term is strictly positive on every sufficiently late block. Indeed the two tied states have the same threshold `b` and adaptive amplitude `c`, so they lie on the common-amplitude selector curve of `RE-070`. That finding proves, uniformly between the tied states,

\[
\frac{d}{dY}(Z_c(Y)-Y)
=
b(1-b)a_c(Y)\log Y
\left(
1+O_J\!\left(\frac1{\log Y}+a_c(Y)\log Y\right)
\right)>0.
\tag{7}
\]

Consequently

\[
\boxed{
\widehat H_+>\widehat H_-.
}
\tag{8}
\]

Thus the matched-first-layer hypothesis in the **standard-prime half** of `RE-072` is not actually needed after the endpoint correction. Higher-layer packets do not reset the corrected Chebyshev deficit; they increase it by their full higher-layer event mass in addition to the positive selector-dilation term. First-layer packets also increase it, through selector dilation alone. Arbitrarily large mixed packets behave the same way.

The raw deficit differs only by the current fringe atom:

\[
H_\vartheta(Z)=\widehat H(C,b)-\delta_\vartheta(Z).
\tag{9}
\]

Therefore for any two ordered selected fan points `0<1`,

\[
\boxed{
H_\vartheta(Z_1)-H_\vartheta(Z_0)
>
\delta_\vartheta(Z_0)-\delta_\vartheta(Z_1).
}
\tag{10}
\]

In particular, between any two fringe-free selected endpoints the ordinary Chebyshev deficit is strictly increasing **regardless of every intervening packet type**. From a fringe-free starting endpoint, the entire possible net loss at a later endpoint is carried by the one final unmatched ordinary prime; no collection of higher-layer rearrangements or first-layer support births can create an additional Chebyshev reset channel.

## 1. The corrected deficit is exactly a selector-minus-radical gap

`RE-059` proves for every selected regular state

\[
\vartheta(Z)-\delta_\vartheta(Z)
=Y-P_C
=\sum_{p\mid C}\log p
=\log\operatorname{rad}(C).
\tag{11}
\]

Subtracting (11) from `Z` gives (4) immediately:

\[
Z-\vartheta(Z)+\delta_\vartheta(Z)
=Z-\log\operatorname{rad}(C).
\tag{12}
\]

This form separates the two mechanisms cleanly. `Z` is the adaptive tangent coordinate, while `log rad(C)` records only which ordinary prime supports have entered the CA state. Higher-layer exponent changes do not alter the radical.

Inside a threshold cell the state and its radical are fixed. `RE-059` gives `Z_C'(b)>0`, hence (5). If the selector crosses the cell's possible fringe prime, raw `H_vartheta` jumps downward by `log r` while `delta_vartheta` jumps upward by exactly the same amount. The corrected coordinate therefore keeps increasing through that raw-prime discontinuity rather than acquiring a hidden reset.

## 2. Every tied switch has positive radical-gap increment

At a fan breakpoint the tied states satisfy

\[
A_b(C_-)=A_b(C_+)=c>0.
\tag{13}
\]

The common-amplitude selector curve used in `RE-070` is defined by

\[
a_c(Y)=\frac{cY^{-b}}{1+cY^{-b}},
\qquad
g(Z_c(Y))=g(Y)-\frac{b\,a_c(Y)}Y.
\tag{14}
\]

The geometric derivation of `RE-070`, before any first-layer prime-set identity is imposed, gives (7). The late small-height regime makes `a_c(Y)\log Y=o(1)` uniformly, while `b<=b_1<1/2`; hence the derivative is positive on the whole interval `[Y_-,Y_+]`. Thus

\[
\boxed{
(Z_+-Y_+)-(Z_--Y_-)>0.
}
\tag{15}
\]

Now compare the state mass with the radical mass. The CA event sweep only increments prime exponents. Across the complete packet,

\[
Y_+-Y_-
=\sum_{\text{all event occurrences }(p,j)}\log p,
\tag{16}
\]

whereas

\[
\log\operatorname{rad}(C_+)-\log\operatorname{rad}(C_-)
=\sum_{\text{first-layer births }p}\log p.
\tag{17}
\]

Therefore

\[
\boxed{
P_{\ge2}(-,+)
:=(Y_+-Y_-)
-\bigl(\log\operatorname{rad}(C_+)-\log\operatorname{rad}(C_-)\bigr)
\ge0
}
\tag{18}
\]

is exactly the logarithmic mass of the higher-layer event occurrences in the packet. Combining (12), (15), and (18) proves (6)--(8).

The switch contribution has the more quantitative late form

\[
\boxed{
\widehat H_+-\widehat H_-
=
P_{\ge2}(-,+)
+b(1-b)
\int_{Y_-}^{Y_+}a_c(t)\log t\,dt\,(1+o_J(1)).
}
\tag{19}
\]

No bounded-packet or sublinear-span hypothesis is used: the error in the common-amplitude derivative is uniform along the late tied segment, because `a_c(t)\log t` is already in the uniform small-height regime.

Two controls expose the meaning of (19). For a pure first-layer packet, `P_(>=2)=0`, so (19) reduces to the selector-dilation mechanism isolated in `RE-070`; matching the fringe was needed there only to identify the **raw** endpoint Chebyshev masses. For a pure higher-layer packet the radical is unchanged, so the corrected increment is simply `Z_+-Z_->0`; the whole physical exponent mass is automatically retained rather than canceled by new ordinary supports.

## 3. Matched-run Chebyshev costs now accumulate through arbitrary interruptions

Let a fan segment contain disjoint consecutive matched `0 -> 0` first-layer runs `R_1,...,R_s` of the type treated in `RE-072`. Let `w_k` be the threshold width of `R_k` and `X_k` its initial physical scale. Since every endpoint of such a run is fringe-free,

\[
\Delta_{R_k}\widehat H
=
\Delta_{R_k}H_\vartheta.
\tag{20}
\]

`RE-072` supplies

\[
\Delta_{R_k}H_\vartheta
\gg_J
X_k^{1-b_1}\log X_k\;w_k.
\tag{21}
\]

All fan motion between those runs has **positive** corrected increment by (5) and (8). Hence, if `X` is the smallest physical scale in the containing segment,

\[
\boxed{
\widehat H_{\rm end}-\widehat H_{\rm start}
\ge
\sum_{k=1}^s\Delta_{R_k}H_\vartheta
\gg_J
X^{1-b_1}\log X
\sum_{k=1}^s w_k.
}
\tag{22}
\]

This is the global accumulation statement that was unavailable in `RE-072`. Matched-run Chebyshev costs cannot be erased by inserting higher-layer packets, Egyptian packets, deep-layer packets, unmatched first-layer packets, or packets of unbounded cardinality. Those interruptions may alter the reciprocal Mertens coordinate and can participate in the reset mechanisms priced by `RE-074`--`RE-075`, but on the corrected standard-prime coordinate they only add nonnegative cost.

Consequently the two sides of the current source ledger are now asymmetric. `RE-075` says a later recovery of a matched-run Mertens descent must be paid for by many new first-layer supports and physical span. `RE-076` says that same recovery architecture has **no corresponding standard-source reset capacity at all**: support births change `Y` and `log rad(C)` together, higher layers increase `P_C`, and selector dilation is positive. The only raw Chebyshev discrepancy left outside this monotone ledger is the single current fringe atom.

## 4. Boundary tests and what this does not prove

The endpoint correction is essential. The ordinary function `H_vartheta(x)=x-vartheta(x)` is not globally monotone; it drops by `log p` at each ordinary prime. Equation (3) removes only the unique ordinary prime that can be present without its delayed first-layer CA event at a selected support point. The theorem is about the **adaptively selected late fan**, not about arbitrary real `x`.

The late compact condition is also load-bearing. Strict selector dilation in (7) uses the common positive small-height regime and the fixed bound `b_1<1/2` (indeed the sign mechanism has margin for every fixed `b<1`). The finding does not assert this Lyapunov law for arbitrary early CA states or arbitrary nonselected state pairs.

The theorem is structural rather than a contradiction to false RH. The matched-run lower exponent in (22) is `1-b_1`, while `b_1>1-Theta` gives

\[
1-b_1<\Theta.
\tag{23}
\]

Thus an off-critical Chebyshev error of natural size `X^Theta` can still absorb the forced monotone excursion. This is the required falsification check: the result removes a cancellation architecture without silently importing an RH-strength source bound.

Likewise, an abstract event staircase engineered with the same ordered-support and common-amplitude geometry can reproduce the monotone radical-gap coordinate. Integrality or monotonicity alone therefore remains insufficient for RH. The arithmetic task is now sharper: control how much total corrected Chebyshev excursion the **actual prime source** can sustain on the same common positive blocks, or force enough threshold width into the complementary charged branches that the higher-layer/fringe laws become prohibitive.

## 5. Prior-art boundary and research consequence

The identities `log rad(C)=sum_(p|C) log p` and monotone CA exponent growth are classical. Alaoglu--Erdos supplies the CA threshold structure, while Mantovanelli's August 2026 prime-layer workload is the closest current prior art for event sweeps, packet conservation, and tangent CA bookkeeping. Zimov's consecutive-CA work studies Robin-ratio changes across selected quotient types. A directed current search found no external statement of the adaptive multi-threshold Lyapunov coordinate

\[
Z_b(C)-\log\operatorname{rad}(C)
\]

or of its monotonicity across arbitrary exposed-fan packets. No claim of external priority is made, and no theorem beyond sources already anchored in `SOURCES.md` is load-bearing, so `SOURCES.md` requires no change.

The live global frontier is therefore narrower than after `RE-075`. The standard Chebyshev side already has a packet-independent monotone potential. What remains is to splice its accumulated growth with either an **upper capacity bound from the genuine prime source** or the reciprocal-source support-birth bill. In particular, future work should not spend effort searching for a higher-layer or unbounded-packet mechanism that resets the corrected Chebyshev deficit: equations (4)--(8) rule that architecture out exactly.