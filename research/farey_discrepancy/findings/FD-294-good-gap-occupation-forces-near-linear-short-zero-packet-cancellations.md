# FD-294 — Good-gap occupation forces near-linear short zero-packet cancellations

- **Date:** 2026-09-23
- **Status:** proved an RH-conditional local cancellation certificate forced by every FD-292/293 inverse-polylog remainder-good occupation certificate
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** complementary hard remainder / zero-gap occupation / short spectral packets / exact telescoping / route sharpening
- **Depends on:** FD-280, FD-291, FD-292, FD-293
- **Classification:** `EXACT-DERIVED + RH-POPULATION-TRANSFER + SHORT-PACKET-CANCELLATION-CERTIFICATE + NECESSARY-CONDITION`

## Claim

FD-293 shows that, under RH, any inverse-polylogarithmic remainder-good occupation certificate of the form

\[
\Omega_B(J)\ge \delta_P\frac{H}{L^P},
\qquad
J=[H,2H],
\qquad
L:=\log(2Nx),
\tag{1}
\]

with fixed `P>0` and `delta_P>0`, requires a near-linear population of remainder-good zero gaps:

\[
K_B(J)
\ge
\left(\frac{\delta_P}{\pi}-o(1)\right)
\frac{H\log\log H}{L^P}.
\tag{2}
\]

That population requirement has a stronger local consequence. Consecutive remainder-good gaps in the selected population cannot be far apart too often, and the exact hard-complement identity of FD-280 forces the complete zero packet between any two such good gaps to be small in the **physical Farey band norm**.

More precisely, let the physical hard remainder be

\[
\mathcal R_{T,N}(d)
=
\sum_{q\mid d}
\bigl(E_T(Nq)-E_T(N(q-1))\bigr),
\tag{3}
\]

and write

\[
\mathscr R_{N,x}(T)
:=
\sum_{x<d\le 2x}
|\mathcal R_{T,N}(d)|.
\tag{4}
\]

A zero gap is `B`-good when the gapwise-constant value of (4) is at most `B`, as in FD-291. List the `K=K_B(J)` good gaps with nonempty reciprocal-log-safe core in increasing order and choose one representative

\[
T_r\in G_{j_r}^{\rm safe}(J),
\qquad
1\le r\le K.
\tag{5}
\]

For `r<K`, let

\[
\mathcal Z_r
:=
\{\rho: T_r<\Im\rho\le T_{r+1}\}
\tag{6}
\]

with multiplicity, and let its physical grouped packet be

\[
\mathcal P_r(d)
:=
\sum_{\rho\in\mathcal Z_r}
\mathcal G_{\rho,N}(d),
\tag{7}
\]

where `mathcal G_{rho,N}` denotes the physical consecutive-sampling plus divisor-replication image of the residue contribution at `rho`, with all terms at a repeated ordinate grouped in the same hard-cutoff jump.

Then the FD-280 cutoff identity gives **exactly**

\[
\boxed{
\mathcal P_r
=
-\bigl(\mathcal R_{T_{r+1},N}-\mathcal R_{T_r,N}\bigr).
}
\tag{8}
\]

Since both endpoint gaps are `B`-good,

\[
\boxed{
\sum_{x<d\le2x}|\mathcal P_r(d)|
\le 2B.
}
\tag{9}
\]

Thus every pair of consecutive selected good gaps already yields a signed zero-packet cancellation certificate in the physical norm. The population floor (2) then forces **many such certificates on short spectral intervals**. Because all `T_r` lie in `J`,

\[
\sum_{r=1}^{K-1}(T_{r+1}-T_r)
=T_K-T_1
\le H.
\tag{10}
\]

Hence at least `(K-1)/2` indices satisfy

\[
T_{r+1}-T_r
\le
\frac{2H}{K-1}.
\tag{11}
\]

Combining (2) and (11), every certificate (1) forces at least

\[
\boxed{
\left(\frac{\delta_P}{2\pi}-o(1)\right)
\frac{H\log\log H}{L^P}
}
\tag{12}
\]

pairwise disjoint zero packets whose spectral spans obey

\[
\boxed{
T_{r+1}-T_r
\le
\left(\frac{2\pi}{\delta_P}+o(1)\right)
\frac{L^P}{\log\log H}
}
\tag{13}
\]

and whose complete physical band norms obey (9).

Under RH, the Carneiro--Chandee--Milinovich bound on `S(t)` already used in FD-293 also gives, uniformly for intervals satisfying (13),

\[
\#\mathcal Z_r
\ll_{P,\delta_P}
\frac{L^{P+1}}{\log\log H},
\tag{14}
\]

where zeros are counted with multiplicity. Therefore an FD-292 occupation certificate does not merely require `H^{1-o(1)}` good gaps. It requires `H^{1-o(1)}` **disjoint, polylogarithmically short zero packets** whose full signed physical contribution is at most `2B`.

In the simple-critical-zero reciprocal-log clustering formalism of FD-279, the packets in (8) are also unions of **complete** clusters: each representative lies in a safe core, so the boundary gap has length at least `2/L` and no `<2/L` cluster edge crosses either cutoff.

This is a necessary condition for the current FD-292/293 occupation route, not a proof that such cancellation packets exist. It converts the remaining aggregate remainder-goodness problem into a much more local spectral cancellation demand.

## 1. Exact packet telescoping between two good gaps

FD-280 starts from the exact hard decomposition

\[
A(y)=C(y)+P_T(y)+E_T(y),
\tag{15}
\]

where `A` and `C` are independent of the hard spectral cutoff and `P_T` is the residue packet through height `T`. Therefore, for arbitrary `T_0<T_1`,

\[
E_{T_1}-E_{T_0}
=-\bigl(P_{T_1}-P_{T_0}\bigr).
\tag{16}
\]

The physical Farey map is linear: first take the consecutive difference at the arguments `N(q-1),Nq`, then sum over divisors `q|d`. Applying that map to (16) gives

\[
\mathcal R_{T_1,N}(d)-\mathcal R_{T_0,N}(d)
=-\mathcal G_{(T_0,T_1],N}(d),
\tag{17}
\]

where the right side is the complete physical packet of all residue jumps whose ordinates lie in `(T_0,T_1]`. Equation (8) is (17) with `T_0=T_r` and `T_1=T_{r+1}`.

No approximation, contour estimate, RH assumption, zero-spacing law, or simplicity hypothesis enters (8). It is purely the hard-cutoff algebra already isolated in FD-280. Repeated zeros at one ordinate cause a single grouped jump and are automatically included in (17).

Because the endpoints lie in `B`-good gaps,

\[
\|\mathcal R_{T_r,N}\|_{\ell^1(x,2x]}
\le B,
\qquad
\|\mathcal R_{T_{r+1},N}\|_{\ell^1(x,2x]}
\le B.
\tag{18}
\]

Taking the physical band norm in (8) and using only the triangle inequality proves (9). The direction is important: two small complementary remainders force the *intervening signed packet* to be small. No converse is claimed; a small increment can connect two large remainders.

This also prevents a misleading coordinatewise interpretation. Equation (9) is a statement after the exact physical consecutive-sampling and divisor-replication map and after summing the zero contributions with their signs. It does not imply that individual residues, individual divisor coordinates, or individual reciprocal-log clusters are small.

## 2. Near-linear good-gap population forces many short packet intervals

Let the selected representatives be ordered as in (5). Since every representative belongs to `[H,2H]`, their consecutive spacings are nonnegative and telescope as in (10). Set

\[
D:=\frac{2H}{K-1}.
\tag{19}
\]

If more than `(K-1)/2` spacings exceeded `D`, their sum would exceed

\[
\frac{K-1}{2}D=H,
\tag{20}
\]

contradicting (10). Thus at least `(K-1)/2` of the intervals `(T_r,T_{r+1}]` have length at most `D`.

Now assume the FD-292 occupation hypothesis (1). FD-293 supplies (2) under RH, so

\[
D
\le
\left(\frac{2\pi}{\delta_P}+o(1)\right)
\frac{L^P}{\log\log H},
\tag{21}
\]

and

\[
\frac{K-1}{2}
\ge
\left(\frac{\delta_P}{2\pi}-o(1)\right)
\frac{H\log\log H}{L^P}.
\tag{22}
\]

The packet intervals associated with consecutive representatives are pairwise disjoint except for endpoints, and no zero lies at a representative because the representatives are interior to zero gaps. Hence the zero multisets in these packets are disjoint. Equations (21), (22), and (9) prove (12)--(13) and the stated near-linear family of disjoint cancellation certificates.

Since `L asymp log H asymp log x` in the polynomial Perron regime, the count in (22) is

\[
H^{1-o(1)},
\tag{23}
\]

while each spectral span in (21) is only polylogarithmic in `H`. This is substantially stronger than the statement that isolated favorable cutoffs must exist.

The constants in (21)--(22) are not asserted to be optimal. The factor `2` comes from the elementary median/Markov argument on the consecutive spacings. Any additional information on the distribution of the selected good gaps could improve it, but no such information is needed for the exponent-scale conclusion.

## 3. Each short interval contains only polylogarithmically many zeros under RH

Let `(U,U+h]` be one of the short packet intervals, so `U asymp H` and

\[
h\ll_{P,\delta_P}\frac{L^P}{\log\log H}.
\tag{24}
\]

Riemann--von Mangoldt gives

\[
N(U+h)-N(U)
=
\frac{h}{2\pi}\log H
+S(U+h)-S(U)
+O\!\left(1+\frac{h^2+1}{H}\right),
\tag{25}
\]

uniformly in this polylogarithmic range. Under RH the pointwise estimate already used in FD-293,

\[
|S(t)|
\le
\left(\frac14+o(1)\right)
\frac{\log t}{\log\log t},
\tag{26}
\]

implies

\[
N(U+h)-N(U)
\le
\frac{h}{2\pi}\log H
+
\left(\frac12+o(1)\right)
\frac{\log H}{\log\log H}
+O(1).
\tag{27}
\]

Substituting (24), and using `log H asymp L`, yields (14). The count is with multiplicity, so it also upper-bounds the number of distinct ordinates.

This zero-count estimate is not needed for the exact packet norm bound (9). Its role is to show that the forced cancellations are genuinely local also in **spectral population**, not only in height width: each certificate involves at most a fixed polylogarithmic number of zero terms while there are `H^{1-o(1)}` pairwise disjoint certificates.

## 4. The packet boundaries are reciprocal-log cluster breaks

Every selected gap has a nonempty FD-291 safe core

\[
G_j^{\rm safe}(J)
=
J\cap
\left[
\gamma_j+\frac1L,
\gamma_{j+1}-\frac1L
\right].
\tag{28}
\]

Ignoring only the harmless truncation by the window boundary, nonemptiness forces

\[
\gamma_{j+1}-\gamma_j\ge\frac2L.
\tag{29}
\]

The FD-279 reciprocal-log cluster relation joins consecutive simple critical zeros only across gaps strictly smaller than `2/L`. Thus a cutoff placed in the safe core lies in a cluster-breaking gap. A packet between two such cutoffs cannot contain only part of a reciprocal-log cluster: every cluster encountered after the lower cutoff is completed before the upper cutoff.

For safe cores clipped by an endpoint of `J`, the same conclusion still follows directly from the definition whenever a representative exists at distance at least `1/L` from both neighboring zero ordinates; this is exactly the zero-safe property used in FD-291. A `<2/L` gap cannot contain such a point.

Therefore, under the simple-critical-zero hypotheses of FD-279, each packet in (8) is a union of complete reciprocal-log clusters. This is useful because the close-zero cancellation mechanism of FD-274--FD-278 may be applied internally without generating a boundary `1/gap` singularity.

This cluster statement is an interpretation layer, not an extra hypothesis for the core theorem. Equations (8)--(14) remain valid at the level of grouped hard-cutoff jumps without zero simplicity.

## 5. Consequence for the live remainder gate

FD-293 showed that an inverse-polylog occupation theorem cannot be supported by a sparse exceptional family of good gaps. FD-294 strengthens the necessary condition: such a theorem must produce a near-linear family of **local recurrence events** for the vector-valued hard residue partial sum.

Indeed, define the physical packet partial sum along hard cutoffs by

\[
\mathcal V(T):=\mathcal P_{T,N}
\tag{30}
\]

and the fixed physical target by

\[
\mathcal A:=\text{physical image of }A-C.
\tag{31}
\]

Then

\[
\mathcal R_{T,N}=\mathcal A-\mathcal V(T).
\tag{32}
\]

A `B`-good gap is a plateau on which the step path `mathcal V(T)` lies within `B` of the fixed target in the physical band `ell^1` norm. Two consecutive selected returns to that `B`-ball differ by a packet increment of norm at most `2B`; FD-293 plus the spacing argument shows that an occupation certificate forces `H^{1-o(1)}` such returns separated by only polylogarithmic spectral distance.

This reformulation gives a sharper adversarial test for proposed remainder estimates. A theorem proving small complement on only isolated cutoffs still cannot close the route. More strongly, a proposed mechanism for (1) must be compatible with near-linear many disjoint short zero blocks satisfying

\[
\left\|
\sum_{\rho\ \text{in block}}
\mathcal G_{\rho,N}
\right\|_{\ell^1(x,2x]}
\le2B.
\tag{33}
\]

Conversely, (33) alone does not prove remainder-goodness: small packet increments can occur far from the target `mathcal A`. A successful argument must control both recurrence to the target and the local increments, or prove the occupation directly.

This is now a natural interface with the earlier close-zero work. FD-274--FD-278 show how internal reciprocal-gap singularities cancel when complete clusters are grouped. The present finding says that the live hard-remainder route would need that local grouping, plus any remaining inter-cluster cancellation, to succeed on `H^{1-o(1)}` disjoint polylogarithmic packets. Whether such cancellation can occur at the repair budget is the next genuinely spectral question.

## 6. Prior-art and adversarial audit

The exact increment identity (8) is a specialization of the elementary fact that the complement of a hard partial sum changes by minus the newly included terms; the norm estimate (9) is the triangle inequality. No novelty is claimed for either generic statement. The substantive Mathia-specific content is the combination with the FD-291 physical Farey remainder, the FD-293 RH good-gap population floor, and the reciprocal-log cluster boundary geometry to obtain the near-linear family (12)--(14) of disjoint local cancellation certificates.

No new external theorem is load-bearing. The only analytic zero input is the same Riemann--von Mangoldt plus Carneiro--Chandee--Milinovich `S(t)` estimate already anchored and used in FD-293, so `SOURCES.md` does not need a new entry.

The main adversarial checks are as follows.

First, many good gaps do **not** automatically imply many adjacent good gaps in the full zero-gap sequence. The proof does not use adjacency there. It orders only the selected good gaps and studies the zero packet spanning each consecutive pair; the packet may contain many intervening bad gaps. Equations (21) and (27) quantify exactly how many zero ordinates can intervene.

Second, the small packet conclusion is one-way. Two endpoint remainders bounded by `B` imply a packet increment bounded by `2B`; the reverse implication fails without one known return to the target.

Third, the short-span conclusion uses only the total length of the dyadic height window after FD-293 has supplied the population floor. It does not assume randomness, pair correlation, independence of remainder-goodness from zero spacing, or equidistribution of good gaps.

Fourth, the core packet identity is valid with multiple zeros when all residue data at one ordinate are grouped into one hard-cutoff jump. The optional complete-cluster interpretation inherits the simple-critical-zero formalism of FD-279 and is not silently promoted beyond those hypotheses.

Fifth, the physical norm is taken only after exact consecutive sampling, divisor replication, and signed zero summation. Nothing here provides a lower bound for individual residues or for the packet before the Farey map, so there is no conflict with the close-zero cancellation results.

A decisive falsification of the route can now target (33): prove that, at the repair budget `B=o(N^theta x^{2-beta})` relevant to FD-261, too few cluster-complete polylogarithmic zero packets can have physical norm at most `2B`. Conversely, a constructive remainder theorem must implicitly or explicitly generate the near-linear family required above.

## Net effect

The live FD-292/293 gate is no longer only an aggregate occupation requirement. Under RH, any inverse-polylog remainder-good occupation certificate forces `H^{1-o(1)}` pairwise disjoint, cluster-complete-at-the-boundaries, polylogarithmically short zero packets whose **signed physical Farey contribution** has band norm at most twice the allowed remainder budget.

This turns the next question from “are there enough good remainder gaps?” into the more local and falsifiable question: **can the physical zero packets exhibit near-linear many short recurrence/cancellation events at the repair scale?**