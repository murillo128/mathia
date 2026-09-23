# FD-295 — Short complete zero packets are automatically capacity-subcritical below square-root height

- **Date:** 2026-09-23
- **Status:** proved an RH/simple-zero local packet upper bound and corrected the interpretation of the FD-294 cancellation certificates
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** short spectral packets / reciprocal-log clusters / background conditioning / positive-capacity threshold / route pruning
- **Depends on:** FD-261, FD-276, FD-278, FD-294
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + SIMPLE-ZERO + SHORT-PACKET-UPPER-BOUND + BACKGROUND-THRESHOLD + ROUTE-PRUNING`

## Claim

FD-294 shows that any inverse-polylogarithmic occupation certificate for remainder-good zero gaps forces `H^(1-o(1))` pairwise disjoint, polylogarithmically short zero packets whose **physical Farey band norm** is at most twice the chosen remainder budget. That was described as a local signed-cancellation demand.

At the positive-capacity scale relevant to FD-261, this interpretation is too strong. The existing reciprocal-log cluster bounds imply that, below a substantially higher spectral-height threshold, every such short complete packet is already power-smaller than the capacity ceiling whenever its desingularized cluster backgrounds are tame. No inter-cluster cancellation is needed.

Assume RH and simple nontrivial zeros. Work in the fixed polynomial-depth regime

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{1}
\]

and put

\[
\beta:=\log_2\frac32,
\qquad
c:=1-\beta=0.4150374992788438\ldots,
\qquad
L:=\log(2Nx),
\qquad
a:=1+\frac1\lambda.
\tag{2}
\]

Let a complete zero packet `mathcal Z` lie in a dyadic height window

\[
J=[H,2H],
\qquad
H=x^{\tau+o(1)},
\tag{3}
\]

and suppose its spectral span is `x^(o(1))`; in particular this includes every FD-294 packet, whose span is `O(L^P/log log H)` for fixed `P`. Partition `mathcal Z` into the maximal FD-276 reciprocal-log clusters `mathcal C`, obtained by joining consecutive simple critical zeros across gaps `<2/L`.

For each component write

\[
\mathfrak B_{\mathcal C}:=
\mathfrak B_{\mathcal C}(L^{-1})
\]

for the FD-276 reciprocal background envelope. Suppose

\[
\mathfrak B_*:=
\max_{\mathcal C\subset\mathcal Z}
\max(1,\mathfrak B_{\mathcal C})
=x^{b+o(1)}.
\tag{4}
\]

Let `Q_C(N,d)` denote the normalized grouped complex packet of FD-274--FD-276 and define the normalized real packet

\[
\widetilde{\mathcal P}_{\mathcal Z}(d)
:=
2\Re\sum_{\mathcal C\subset\mathcal Z}Q_{\mathcal C}(N,d).
\tag{5}
\]

The physical critical-line packet is `N^(1/2)` times (5). Then

\[
\boxed{
\sum_{x<d\le2x}
|\widetilde{\mathcal P}_{\mathcal Z}(d)|
\le
x^{1+\kappa(\tau,\lambda)+b+o(1)},
}
\tag{6}
\]

where

\[
\boxed{
\kappa(\tau,\lambda)
:=
\frac{\tau}
{2\left(1-\dfrac{\tau}{\pi(1+1/\lambda)}\right)}
}
\qquad
(0\le\tau<\pi a).
\tag{7}
\]

Consequently the physical packet obeys

\[
\boxed{
\sum_{x<d\le2x}
|\mathcal P_{\mathcal Z}(d)|
\le
N^{1/2}
 x^{1+\kappa(\tau,\lambda)+b+o(1)}.
}
\tag{8}
\]

Compare this with the RH-calibrated FD-261 positive-capacity scale

\[
N^{1/2}x^{2-\beta}
=N^{1/2}x^{1+c}.
\tag{9}
\]

Every short complete packet is therefore power-subcritical whenever

\[
\boxed{
\kappa(\tau,\lambda)+b<c.
}
\tag{10}
\]

Equivalently, for `0<=b<c`, define

\[
\boxed{
\tau_{\rm auto}(\lambda,b)
:=
\frac{2(c-b)}
{1+\dfrac{2(c-b)}{\pi(1+1/\lambda)}}.
}
\tag{11}
\]

Then

\[
\tau<\tau_{\rm auto}(\lambda,b)
\quad\Longrightarrow\quad
\|\mathcal P_{\mathcal Z}\|_{\ell^1(x,2x]}
=o\!\left(N^{1/2}x^{2-\beta}\right)
\tag{12}
\]

with a fixed power margin.

For tame backgrounds, `b=0`, the weakest value of (11) over all fixed `lambda>0` occurs as `lambda -> infinity` and is

\[
\boxed{
\inf_{\lambda>0}\tau_{\rm auto}(\lambda,0)
=
0.6565900638\ldots .
}
\tag{13}
\]

At balanced depth `lambda=1`,

\[
\boxed{
\tau_{\rm auto}(1,0)
=0.7332102033\ldots .
}
\tag{14}
\]

Both are strictly larger than the current Perron prime-witness range `tau<1/2` of FD-284--FD-294. In fact, throughout that whole current range one has uniformly in fixed `lambda>0`

\[
\kappa(\tau,\lambda)
<
\frac{\pi}{2(2\pi-1)}
=0.2973199377\ldots,
\tag{15}
\]

so a threshold-sized short packet would require at least

\[
\boxed{
b
\ge
0.1177175615\ldots-o(1)}
\tag{16}
\]

of external background conditioning. At `lambda=1`, the corresponding margin improves to

\[
\boxed{
b
\ge
0.1434231131\ldots-o(1).}
\tag{17}
\]

Thus the local packet-smallness conclusion of FD-294 is **automatically compatible** with the current low-height route for tame backgrounds. The restrictive part of FD-294 is not, at near-capacity budgets, that the packet increment must be small; it is that the hard residue partial-sum path must return repeatedly to the fixed remainder target.

## 1. A polylogarithmically short packet has only subpolynomially many components

FD-294 produces packets whose spectral spans satisfy

\[
h
\ll_{P,\delta_P}
\frac{L^P}{\log\log H}
\tag{18}
\]

for fixed `P`. More generally, the argument below needs only `h=x^(o(1))` together with a subpolynomial local zero count.

For the FD-294 packets, Riemann--von Mangoldt plus the RH estimate

\[
|S(t)|
\le
\left(\frac14+o(1)\right)
\frac{\log t}{\log\log t}
\tag{19}
\]

already used there gives

\[
\#\mathcal Z
\ll
h\log H+
\frac{\log H}{\log\log H}
=x^{o(1)}.
\tag{20}
\]

In particular the number `R_Z` of reciprocal-log components in the packet satisfies

\[
\boxed{R_{\mathcal Z}=x^{o(1)}.}
\tag{21}
\]

This is the key difference from the global aggregate family of FD-278. There, components available below height `T` could have population exponent as large as `r<=tau`. A **short local packet** has population exponent exactly `r=0` at power scale, even if some of its individual components have growing cardinality.

The safe-core endpoints in FD-294 ensure that the packet is a union of complete reciprocal-log components: no `<2/L` cluster edge crosses either boundary. Hence every component in this local partition satisfies the FD-276 collar hypothesis.

## 2. The FD-276 cluster ledger gives the local packet bound

For a complete component `mathcal C` of cardinality `m_C`, FD-276 gives, with an absolute implied constant,

\[
\sum_{x<d\le2x}|Q_{\mathcal C}(N,d)|
\ll
x(2L)^{m_{\mathcal C}-1}
\mathfrak B_{\mathcal C}.
\tag{22}
\]

Let

\[
m_*:=
\max_{\mathcal C\subset\mathcal Z}m_{\mathcal C}.
\tag{23}
\]

Triangle inequality is deliberately sufficient here; no cancellation between distinct clusters is assumed. From (5), (21), and (22),

\[
\begin{aligned}
\sum_{x<d\le2x}
|\widetilde{\mathcal P}_{\mathcal Z}(d)|
&\le
2\sum_{\mathcal C\subset\mathcal Z}
\sum_{x<d\le2x}|Q_{\mathcal C}(N,d)|\\
&\ll
xR_{\mathcal Z}(2L)^{m_*-1}\mathfrak B_*.
\end{aligned}
\tag{24}
\]

Every component lies below `2H=x^(tau+o(1))`. The RH cluster-packing estimate of FD-278 therefore gives

\[
m_*
\le
\left(
\kappa(\tau,\lambda)+o(1)
\right)
\frac{\log x}{\log\log x}.
\tag{25}
\]

Because

\[
\log(2L)=\log\log x+O(1),
\tag{26}
\]

one obtains

\[
(2L)^{m_*-1}
\le
x^{\kappa(\tau,\lambda)+o(1)}.
\tag{27}
\]

Insert (4), (21), and (27) into (24). This proves (6). On RH every critical zero residue carries the common physical factor `N^(1/2)` removed in the FD-271/FD-274 normalization, so (8) follows.

The proof has used only upper bounds and triangle inequality. Therefore the conclusion is stronger than a statement about favorable phase cancellation: the packet is small at the relevant power scale even if all complete cluster contributions align adversarially.

## 3. The automatic-subcritical height boundary

At the positive-capacity scale, equations (8)--(9) show that a short packet could reach threshold only if

\[
1+\kappa(\tau,\lambda)+b
\ge
1+c-o(1),
\]

or

\[
\boxed{
b+\kappa(\tau,\lambda)\ge c-o(1).}
\tag{28}
\]

This is the **local short-packet tariff**. It is stronger than the global aggregate tariff in FD-278 because the local packet has only `x^(o(1))` components; it does not get to spend a population exponent `r`.

For `b<c`, solving the strict reverse inequality in (28) for `tau` gives exactly (11). Indeed, with `d:=c-b>0`,

\[
\frac{\tau}{2(1-\tau/(\pi a))}<d
\]

is equivalent to

\[
\tau
<
\frac{2d}{1+2d/(\pi a)}.
\tag{29}
\]

For `b=0`, the right side decreases as `a=1+1/lambda` decreases, so its uniform minimum over fixed positive `lambda` is attained at `a->1`. Substitution gives (13). Setting `a=2` gives (14).

For the current `tau<1/2` regime, `kappa` is increasing in `tau` and decreasing in `a`. Hence the worst case is the simultaneous limit `tau->1/2`, `a->1`, giving

\[
\kappa
\le
\frac{1/2}{2(1-(1/2)/\pi)}
=
\frac{\pi}{2(2\pi-1)}
=0.2973199377\ldots .
\tag{30}
\]

Subtracting this from `c` yields (16). At `lambda=1`, so `a=2`, the same calculation gives

\[
\kappa
\le
\frac{\pi}{4\pi-1}
=0.2716143860\ldots,
\tag{31}
\]

and hence (17).

The threshold statement can be phrased directly in terms of a remainder budget. Suppose

\[
B_{N,x}
=
\frac{N^{1/2}x^{2-\beta}}{\ell(x)},
\tag{32}
\]

where `ell(x)->infinity` but `ell(x)=x^(o(1))`, for example any fixed power of `log x`. If

\[
b+\kappa(\tau,\lambda)
\le
c-\delta
\tag{33}
\]

for some fixed `delta>0`, then (8) gives

\[
\frac{
\|\mathcal P_{\mathcal Z}\|_{\ell^1(x,2x]}
}{B_{N,x}}
\le
x^{-\delta+o(1)}\ell(x)
\longrightarrow0.
\tag{34}
\]

Thus every FD-294 short packet automatically satisfies its necessary bound `||mathcal P_Z||_1<=2B_{N,x}` for all sufficiently large `x` at these near-capacity budgets. No special signed cancellation event is needed.

## 4. Consequence for the FD-291--FD-294 occupation route

FD-291 asks for reciprocal-log-safe remainder-good occupation slightly larger than the phase-exceptional budget. FD-292 makes that phase budget `H/L^P` for arbitrary fixed `P`; FD-293 shows that such occupation requires `H^(1-o(1))` good zero gaps; FD-294 then converts consecutive selected returns into `H^(1-o(1))` short packet increments of norm at most `2B`.

The present calculation shows that the final packet-increment condition does **not** by itself sharpen the route near the FD-261 capacity boundary when the cluster backgrounds are tame. In the current sub-square-root height range, every complete polylogarithmic packet already has a deterministic power ceiling below that boundary. The word “cancellation” in the FD-294 certificate should therefore not be read as evidence that many exceptional inter-cluster phase alignments are required.

What remains genuinely restrictive is the **absolute location** of the hard partial-sum path. Writing, as in FD-294,

\[
\mathcal R_{T,N}
=
\mathcal A-\mathcal V(T),
\tag{35}
\]

a small packet says only that two values of `mathcal V` are close to each other. A remainder-good gap requires `mathcal V(T)` itself to lie close to the fixed target `mathcal A`. Equation (34) shows that small local increments can be plentiful for deterministic size reasons while the path still stays far from that target everywhere.

Therefore a decisive next theorem cannot merely lower-bound the norms of generic short zero packets at the capacity scale unless it also proves the polynomial background anomaly required by (28). The more direct live target remains one of the following equivalent-strength objects: a lower bound preventing frequent returns of `mathcal V(T)` to the target ball, an upper bound on the safe occupation of remainder-good gaps, or a direct estimate on the full complementary remainder itself.

This also cleanly separates two possible failure modes. If future work proves that some of the forced packets are threshold-sized despite their shortness, (28) localizes the cause to a polynomially bad desingularized background. If the backgrounds remain tame, then packet increments are not the obstruction and the problem is recurrence/absolute positioning of the residue partial sum.

## 5. Adversarial checks and boundaries

The first check is the remainder budget. FD-294 allows an arbitrary `B`; the automatic conclusion here is **not** valid for every `B=o(N^(1/2)x^(2-beta))`. It applies whenever `B` stays above the deterministic short-packet ceiling in (8), including the important near-capacity budgets obtained by dividing the capacity scale by a subpower factor such as `log^A x`. A budget with an additional power saving larger than the margin in (10) can make packet smallness nontrivial again.

Second, the subpolynomial component count is essential. It comes from the short spectral span. A family containing polynomially many complete components regains the population exponent `r` from FD-278 and can reach the capacity scale without violating (28). The theorem therefore does not replace the global aggregate ledger.

Third, the maximum background envelope in (4) is an actual hypothesis/resource. A single cluster with `mathfrak B_C=x^(b+o(1))` above the threshold in (28) can invalidate automatic subcriticality. The theorem does not prove that the zeta backgrounds are tame; it quantifies exactly how much bad conditioning is required before a short packet can become capacity-sized.

Fourth, simplicity is inherited from the reciprocal-log cluster formalism of FD-276--FD-278. The exact FD-294 packet telescoping remains valid with multiple zeros grouped at one ordinate, but (6)--(17) do not claim a confluent-Hermite analogue for those multiple-zero packets.

Fifth, the broader automatic boundary (11) can lie above `tau=1/2`, but this does **not** extend the current complete Perron argument beyond square-root height. The `tau<1/2` ceiling in FD-284--FD-290 comes from counting primes in robust phase sectors with the RH prime-number-theorem error. FD-295 only controls the zero-packet side.

Finally, the proof is an upper-bound argument. It cannot establish that remainder-good gaps exist, that the hard partial sum returns to its target, or that the full contour repair is small. Its role is negative but strategic: it prevents the local packet condition produced by FD-294 from being mistaken for a stronger obstruction than it actually is near the present capacity threshold.

## 6. Prior-art audit

The analytic ingredients are already anchored in the line. FD-276 supplies the uniform reciprocal-log cluster bound, while FD-278 obtains the RH cluster-cardinality ceiling from Riemann--von Mangoldt and the Carneiro--Chandee--Milinovich bound on `S(t)`. No new external theorem is load-bearing, so `SOURCES.md` needs no modification.

A fresh targeted search covered short Mertens zero sums, reciprocal zeta-derivative moments, close zeta zeros, grouped explicit-formula residues, and Farey discrepancy/Mertens formulas. The search recovered the standard Mertens explicit-formula setting, the Bui--Florea--Milinovich work on negative moments of `zeta'(rho)` and close-spacing sensitivity, and recent Farey local-discrepancy work using Mertens sums. It did not reveal a theorem coupling reciprocal-log complete-zero clustering to the consecutive-difference/divisor-replicated Farey band norm, nor the local short-packet exponent boundary (11).

No novelty is claimed for Riemann--von Mangoldt, the `S(t)` bound, divided-difference cluster compression, or the generic observation that a subpolynomial number of subthreshold terms remains subthreshold. The derived content is the **localization of the FD-278 population ledger to the FD-294 short packets**: their population exponent collapses to zero, producing the stronger tariff (28), the automatic-height boundary (11), and the conclusion that the current FD-294 packet-smallness requirement is power-slack throughout the entire sub-square-root Perron window under tame backgrounds.

## Net effect

FD-294 correctly shows that a remainder-good occupation theorem forces near-linearly many short packet increments between repeated returns of the hard residue path. FD-295 shows that the **smallness of those increments is not itself an exceptional spectral-cancellation event at near-capacity budgets**. Under RH, simple zeros, and tame reciprocal-log backgrounds, every such packet is already power-subcritical below `x^(0.65659...-o(1))` uniformly in polynomial depth, and hence throughout the current `T<x^(1/2-o(1))` Perron range.

The live gate therefore moves back from packet-increment cancellation to target recurrence: prove or obstruct near-linear many returns of the full hard residue partial sum to the remainder-good ball. If a short packet nevertheless reaches the capacity scale in the current height window, the theorem forces a new concrete resource — at least `x^(0.117717...-o(1))` background conditioning uniformly, or `x^(0.143423...-o(1))` at balanced depth.