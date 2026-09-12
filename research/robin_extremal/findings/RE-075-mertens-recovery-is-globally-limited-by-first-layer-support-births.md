# RE-075 — Mertens recovery is globally limited by first-layer support births

**Status:** `EXACT-DERIVED + CORRECTION/GENERALIZATION + MIXED-PACKET-PRIME-SET-CONSERVATION + GLOBAL-FAN-SEGMENT + FIRST-LAYER-SUPPORT-BIRTH-BUDGET + MERTENS-RESET-CAPACITY + PHYSICAL-SPAN-COST + QUANTITATIVE-RH-FAILURE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-068` proved exact prime-set conservation for a first-layer-only fan packet, while `RE-074` showed that bounded packets can recover only `O(log Y/Y)` of the logarithmic Mertens source per adjacent fan step. The first-layer-only restriction in `RE-068` is in fact unnecessary, and removing it changes the reset frontier materially.

For every selected regular CA state `C` with

\[
Y:=\log C,
\qquad Z:=Z_b(C),
\]

`RE-059` gives the exact identity

\[
\vartheta(Z)-\delta_\vartheta(Z)
=Y-P_C
=\sum_{p\mid C}\log p
=\log\operatorname{rad}(C).
\tag{1}
\]

The last form is the key. Higher-layer events change exponents but do not change `rad(C)`. Therefore they disappear automatically when two selected endpoints are compared; one does not need to assume that the higher-layer mass `P_C` is constant.

Let `(C_0,Z_0)` and `(C_1,Z_1)` be two ordered selected endpoints on one monotone segment of the late rightmost fan, with

\[
C_0\mid C_1,
\qquad Z_0<Z_1.
\tag{2}
\]

Let

\[
\mathcal S:=\{q\text{ prime}:Z_0<q\le Z_1\}
\tag{3}
\]

be the ordinary primes crossed by the selector, and let

\[
\mathcal E_1:=\{p:p\mid C_1,\ p\nmid C_0\}
\tag{4}
\]

be the primes whose depth-one CA events occur between the two physical states. At each endpoint write the first-layer fringe correction as

\[
\delta_\vartheta(Z_i)=\chi_i\log r_i,
\qquad \chi_i\in\{0,1\},
\tag{5}
\]

with the prime omitted when `chi_i=0`.

Then exactly

\[
\boxed{
\mathcal S\uplus\chi_0\{r_0\}
=
\mathcal E_1\uplus\chi_1\{r_1\}.
}
\tag{6}
\]

There is no restriction on the number of intervening fan switches, on their packet cardinalities, or on how many higher-layer event occurrences are mixed into them. In particular, every additive ordinary-prime source satisfies

\[
\boxed{
\sum_{Z_0<q\le Z_1}w(q)+\chi_0w(r_0)
=
\sum_{p\in\mathcal E_1}w(p)+\chi_1w(r_1)
}
\tag{7}
\]

for every function `w` on the primes.

This corrects the boundary statement in Section 5 of `RE-068`, which called the first-layer-only hypothesis essential for prime-set conservation. The theorem proved there remains valid, but it is the special case in which no higher-layer occurrences are present. The reason the stronger statement was missed is that the earlier proof froze `P_C`; equation (1) instead eliminates `P_C` by passing directly to the radical of the CA state.

The logarithmic Mertens error

\[
E_\ell(x)
:=\sum_{p\le x}-\log(1-p^{-1})-\gamma-\log\log x
\tag{8}
\]

therefore has a packet-independent reset budget. Put

\[
F:=\#\mathcal E_1.
\tag{9}
\]

For arbitrary mixed fan motion satisfying (2),

\[
\boxed{
\bigl(E_\ell(Z_1)-E_\ell(Z_0)\bigr)_+
\le
\frac{F+1}{Z_0-1}.
}
\tag{10}
\]

Thus **higher-layer complexity has no independent Mertens-reset capacity**. A large positive recovery can occur only by creating many new first-layer prime supports; grouping those births with arbitrarily many higher-layer events does not increase the ordinary-source budget.

Applied after a matched `0 -> 0` run from `RE-072`--`RE-074`, this removes the main packet-complexity escape left by `RE-074`. Let `W` be the terminal physical scale of the run, let

\[
w:=\beta_m-\beta_1>0,
\]

and write

\[
B:=E_\ell(Z_L)-E_\ell(Z_R)>0.
\tag{11}
\]

For the compact false-RH fan `J=[b_0,b_1]\Subset(1-\Theta,1/2)`, `RE-072` gives

\[
B\gg_J W^{-b_1}w.
\tag{12}
\]

Suppose that at any later selected endpoint on the same oriented fan segment one has recovered a fixed fraction `lambda in (0,1]`,

\[
E_\ell(Z_*)-E_\ell(Z_R)\ge\lambda B.
\tag{13}
\]

Let `F_*` be the total number of new first-layer support primes introduced between the terminal state of the matched run and that endpoint. Since the matched run ends with fringe bit zero, (6) and (10) give

\[
\boxed{
F_*+1
\ge
\lambda B\,(Z_R-1)
\gg_{J,\lambda}
W^{1-b_1}w.
}
\tag{14}
\]

No bounded-packet assumption remains. If `w` is bounded below, any fixed-fraction recovery requires super-square-root-many new prime supports because `1-b_1>1/2`.

Moreover every one of those physical first-layer events has prime label `p>Z_R`, so the physical logarithmic-size span itself obeys

\[
\boxed{
Y_*-W
\ge
F_*\log Z_R.
}
\tag{15}
\]

Consequently, whenever `W^(1-b_1)w -> infinity`, a fixed-fraction reset forces

\[
\boxed{
Y_*-W
\gg_{J,\lambda}
W^{1-b_1}w\log W.
}
\tag{16}
\]

Thus the remaining reset architecture is not merely "some unbounded packet." It must spend a polynomial number of **new ordinary prime supports** and a corresponding physical CA span.

## 1. The radical identity removes all higher-layer events

Equation (1) is already contained in the exact fixed-cell source invariant of `RE-059`. Apply it at the two endpoints:

\[
\vartheta(Z_i)-\delta_\vartheta(Z_i)
=\log\operatorname{rad}(C_i),
\qquad i=0,1.
\tag{17}
\]

Because the CA event sweep only increments prime exponents, `C_0|C_1`. The ratio of radicals records exactly the primes whose exponent changes from zero to one:

\[
\frac{\operatorname{rad}(C_1)}{\operatorname{rad}(C_0)}
=
\prod_{p\in\mathcal E_1}p.
\tag{18}
\]

Subtract (17). Since `Z_0<Z_1`, right-continuity of `vartheta` gives

\[
\vartheta(Z_1)-\vartheta(Z_0)
=
\sum_{q\in\mathcal S}\log q.
\tag{19}
\]

Using (5),

\[
\sum_{q\in\mathcal S}\log q
+\chi_0\log r_0
=
\sum_{p\in\mathcal E_1}\log p
+\chi_1\log r_1.
\tag{20}
\]

Exponentiating and applying unique factorization proves (6). Notice that no term involving a higher-layer event remains: such events are present in both `Y` and `P_C` in the first form of (1), but are absent from `log rad(C)` in the second form.

For one adjacent tied fan switch, `Z_0<Z_1` follows from the common-amplitude monotonicity proved in Section 1 of `RE-068`; that proof never used the first-layer-only hypothesis. Along an oriented rightmost-fan segment, the same order persists through the whole path: inside a fixed-state cell `Z_C(b)` increases with `b` by `RE-059`, and at a breakpoint the jump to the larger exposed state increases `Z`. Hence (6) can be applied directly to the two endpoints of a multi-switch segment rather than summing packet-by-packet identities.

This also explains how (6) coexists with the higher-layer residual charges of `RE-060`--`RE-066`. Those charges arise because a higher-layer event increases physical event mass and finite-exponent structure without introducing a new ordinary prime support. The raw first-layer source set is nevertheless conserved exactly according to (6).

## 2. Arbitrary mixed motion has a first-layer-count reset budget

Put

\[
m_p:=-\log(1-p^{-1}).
\tag{21}
\]

Exactly,

\[
E_\ell(Z_1)-E_\ell(Z_0)
=
\sum_{q\in\mathcal S}m_q
-
\log\frac{\log Z_1}{\log Z_0}.
\tag{22}
\]

The second term is nonpositive. Hence

\[
\bigl(E_\ell(Z_1)-E_\ell(Z_0)\bigr)_+
\le
\sum_{q\in\mathcal S}m_q.
\tag{23}
\]

Every `q in S` satisfies `q>Z_0`, and

\[
m_q
\le\frac1{q-1}
\le\frac1{Z_0-1}.
\tag{24}
\]

Taking cardinalities in (6),

\[
\#\mathcal S+\chi_0
=F+\chi_1,
\tag{25}
\]

so `#S<=F+1`. Equations (23)--(25) prove (10).

Several limiting cases are useful. If there are no first-layer births at all, `F=0`, then even an arbitrarily complicated higher-layer segment has

\[
\bigl(E_\ell(Z_1)-E_\ell(Z_0)\bigr)_+
\le\frac1{Z_0-1};
\tag{26}
\]

the only possible positive atom is the final fringe prime. If both endpoint fringe bits vanish, then `S=E_1` exactly and the raw ordinary-prime source seen by the selector is literally the set of newly activated supports, regardless of every higher-layer exponent increment in between.

For a bounded mixed packet with `F<=K`, (10) improves the `O_{J,K}(log Y/Y)` estimate of `RE-074` to `O_K(1/Y)` at the source level. More importantly, (10) remains valid when the total higher-layer packet cardinality is unbounded and when many fan switches are grouped into one segment.

## 3. A matched-run reset forces polynomial support growth

At the right endpoint of a matched `0 -> 0` first-layer run, the fringe bit is zero. Apply (10) from that endpoint `(C_R,Z_R)` to any later selected endpoint `(C_*,Z_*)`. If (13) holds, then

\[
\lambda B
\le
\frac{F_*+1}{Z_R-1},
\tag{27}
\]

which is the first inequality in (14). Uniform late-fan regularity gives

\[
Z_R/W\longrightarrow1,
\tag{28}
\]

and inserting (12) proves the second inequality.

The same exact multiset law gives the physical-span cost. Because the initial fringe bit is zero, (6) specializes to

\[
\mathcal S
=
\mathcal E_1\uplus\chi_*\{r_*\}.
\tag{29}
\]

Therefore every new physical support prime belongs to `S` and is strictly larger than `Z_R`. The complete physical CA event mass from `C_R` to `C_*` contains the first-layer contribution

\[
\sum_{p\in\mathcal E_1}\log p
>F_*\log Z_R.
\tag{30}
\]

All higher-layer contributions are nonnegative, so

\[
Y_*-W
\ge
\sum_{p\in\mathcal E_1}\log p
>F_*\log Z_R,
\tag{31}
\]

which proves (15), and (14) plus (28) gives (16) whenever the right-hand side diverges.

This is a different kind of complexity lower bound from `RE-074`. That finding counted how many bounded interruptions are needed, leaving open the possibility that one or a few enormous mixed packets could provide the reset. Equations (14)--(16) are insensitive to packet grouping: an enormous packet helps only to the extent that it contains the required number of **depth-one support births**. Pure higher-layer size is irrelevant to the ordinary Mertens recovery.

## 4. Falsification and boundary tests

The correction to `RE-068` is narrow but exact. It does not say that mixed packets have zero selected-residual charge. A higher-layer event can and does contribute the quantized negative residual terms of `RE-060`--`RE-066`; equation (6) concerns only the ordinary first-layer source set.

The endpoint fringe correction is essential. Without it, a selector may have crossed one ordinary prime whose delayed first-layer event has not yet fired. Equation (6) says this is the only mismatch between selector primes and physical support births.

The order assumption `Z_0<Z_1` is also essential for the interval notation in (3). It holds on the oriented late rightmost fan by the cell and tie monotonicity cited above. The theorem is not asserted for arbitrary unrelated selected states whose selector order is reversed or whose CA supports are not nested.

Equation (10) controls **net positive recovery between two selected endpoints**, not the total positive variation of `E_ell` along a path that may oscillate. That is exactly what is needed for erasing a previous matched-run descent: if a fixed fraction of the old descent has actually been recovered at a later endpoint, the endpoint difference already satisfies (13).

The physical-span bound is an absolute statement in the logarithmic state coordinate `Y=log C`. It does not by itself contradict false RH: a positive counterexample block could, in principle, stretch far enough to pay (16). The new restriction is that any such reset must visibly create that much ordinary-prime support and physical span; higher-layer rearrangement cannot hide the payment.

A direct control check is a pure higher-layer packet. Then `rad(C_1)=rad(C_0)`, so `E_1` is empty. Equation (6) forces the selector interval to contain no ordinary prime except the single possible endpoint-fringe discrepancy. This is fully compatible with the nonzero higher-layer charge, and rules out the tempting but incorrect picture in which a large higher-layer packet could sweep across many unrelated ordinary-prime Mertens atoms without activating their first layers.

## 5. Prior-art boundary and research consequence

The ingredients `log rad(C)`, unique factorization, and monotone CA exponent growth are classical and are not claimed as new. Alaoglu--Erdos supplies the classical CA exponent-threshold structure, while Mantovanelli's 2026 prime-layer workload framework is the closest current packet bookkeeping: its public companion verifies endpoint factorization, intervening event sums, and packet-mass conservation. A directed current literature search found no external statement coupling the adaptive false-RH selector endpoints to the **radical quotient** of arbitrary mixed CA packets, nor the resulting first-layer-count Mertens reset bound (10). No external theorem beyond sources already anchored in `SOURCES.md` is load-bearing, so `SOURCES.md` requires no change.

The live global frontier is consequently sharper than after `RE-074`. A matched-run Mertens descent has only two endpoint-level possibilities: remain substantially unrecovered, or be paid for by at least

\[
\asymp W^{1-b_1}w
\]

new first-layer supports and a physical span of at least

\[
\asymp W^{1-b_1}w\log W.
\]

The number and size of higher-layer packets no longer constitute an independent reset escape. The next useful target is therefore to compare this forced support-birth/span budget with the finite threshold width and CA support-capacity law of `RE-040`, or to show that a false-RH positive block cannot repeatedly finance such polynomial first-layer growth.