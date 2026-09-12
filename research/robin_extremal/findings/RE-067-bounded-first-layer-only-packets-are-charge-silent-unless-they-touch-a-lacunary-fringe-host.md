# RE-067 — bounded first-layer-only packets are charge-silent unless they touch a lacunary fringe host

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + BOUNDED-EVENT-PACKET + FIRST-LAYER-ONLY-CHARGE-LAW + FRINGE-HOST-LACUNARITY + POLYNOMIAL-LEDGER-REFINEMENT + NEGATIVE/OBSTRUCTION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-065`--`RE-066` reduce the strong off-critical polynomial-span fan to three currencies: packets whose cardinality exceeds a fixed bound, bounded packets with no higher-layer source event, and genuinely negative bounded source-bearing charge. The middle class is still too coarse. The packet calculation behind `RE-061` does not actually become silent when the higher-layer multiset is empty; it becomes **purely an endpoint-fringe law**. Combining that empty-source case with the all-packet double-fringe exclusion of `RE-064` and the base-two fringe-host sparsity of `RE-063` shows that almost every bounded first-layer-only packet is forced into one very specific architecture: matched `0 -> 0`, with asymptotically zero normalized selected-residual charge.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on sufficiently late common positive CA counterexample blocks from `RE-040`. Fix a packet-cardinality bound `K`. At a rightmost-fan breakpoint let

\[
C_-<C_+,
\qquad
Y_\pm:=\log C_\pm,
\qquad
Y:=Y_-,
\tag{2}
\]

be consecutive exposed fan states, and suppose their complete physical packet has at most `K` event occurrences. Let `\chi_\pm\in\{0,1\}` be the endpoint fringe bits and let

\[
Q:=
\frac{b\sqrt Y}{\log Y}
\left(
\mathcal R_b(Z_+)-\mathcal R_b(Z_-)
\right)
\tag{3}
\]

be the normalized selected-residual charge. If the packet is **first-layer-only**, meaning that every crossed physical occurrence has depth `j=1`, then uniformly for fixed `J,K`,

\[
\boxed{
Q=\chi_+-\chi_-+\rho^{(1)}_{J,K}(Y),
\qquad
\rho^{(1)}_{J,K}(Y)\longrightarrow0.
}
\tag{4}
\]

Moreover `RE-064` excludes `(\chi_-,\chi_+)=(1,1)` for every sufficiently late bounded packet. Hence every bounded first-layer-only switch falls into exactly one of the three asymptotic charge classes

\[
\boxed{
0\to0:\ Q=o_{J,K}(1),
\qquad
0\to1:\ Q=1+o_{J,K}(1),
\qquad
1\to0:\ Q=-1+o_{J,K}(1).
}
\tag{5}
\]

The two nonzero classes are globally sparse. If `F^{\ne0}_{K}(T)` counts bounded first-layer-only fan switches with at least one nonzero endpoint fringe bit and with both endpoint state scales at most `T`, then

\[
\boxed{
F^{\ne0}_{K}(T)=O_{J,K}(\log T).
}
\tag{6}
\]

Indeed every such switch has a fringe endpoint, every selected fringe state is one of the base-two hosts of `RE-063`, and one exposed state can be an endpoint of at most two consecutive fan switches. Thus the apparently large first-layer-only structural class of `RE-065` splits into a logarithmically sparse signed part and a potentially large **charge-silent matched part**.

This sharpens the polynomial interruption ledger. In the strong off-critical setting of `RE-065`, fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1-\theta),
\qquad
\delta:=1-b_1-\theta>0,
\tag{7}
\]

and restrict to blocks whose exposed physical fan span satisfies

\[
W_{\mathcal B}\le X_{\mathcal B}^{A}
\tag{8}
\]

for one fixed `A`. Choose `\epsilon_X\to0` larger than the fixed-`J,K` packet-law remainder modulus. Let

- `U_{\mathcal B}` count switches whose physical packet has more than `K` occurrences;
- `F^{00}_{\mathcal B}` count bounded first-layer-only switches with fringe pattern `0 -> 0`;
- `N^{-}_{\ge2,\mathcal B}` count bounded packets containing at least one higher-layer event and satisfying `Q<-\epsilon_{X_{\mathcal B}}`.

Then

\[
\boxed{
U_{\mathcal B}
+F^{00}_{\mathcal B}
+N^{-}_{\ge2,\mathcal B}
\ge
X_{\mathcal B}^{\delta-o(1)}.
}
\tag{9}
\]

Thus the `no higher-layer event` term in `RE-066` is not an undifferentiated structural escape. Up to only `O_A(\log X_{\mathcal B})` switches, it is forced to be a **fringe-free first-layer takeover with vanishing normalized charge**. On a polynomial physical span, the surviving polynomial burden is therefore carried by only three mechanisms: unbounded packet complexity, charge-silent matched first-layer packets, or genuinely negative source-bearing packets.

## 1. The raw packet identity already contains the empty higher-layer case

The packet proof of `RE-061` starts before any conversion of higher-layer bases into reciprocal depths. For every bounded packet it telescopes the source-separated residual of `RE-045` and obtains

\[
\mathcal R_b(Z_+)-\mathcal R_b(Z_-)
=
\frac{
-H_{\ge2}
+\chi_+\log r_+
-\chi_-\log r_-}
{b\sqrt Y}
+o_{J,K}\!\left(\frac{\log Y}{\sqrt Y}\right),
\tag{10}
\]

where

\[
H_{\ge2}
:=
\sum_{(p,j)\text{ in packet},\ j\ge2}\log p,
\tag{11}
\]

and an absent fringe term is interpreted as zero. The derivation of (10) uses only bounded packet cardinality, the tied same-amplitude geometry, and the exact event changes of the higher-layer mass and finite-exponent tail. It does not require `H_{\ge2}` to be nonzero.

For a first-layer-only packet,

\[
H_{\ge2}=0.
\tag{12}
\]

Every nonzero endpoint correction comes from one ordinary prime in the terminal half-unit before its delayed first-layer CA event. Bounded packet geometry gives

\[
Y_+-Y_-=O_K(\log Y),
\qquad
Z_+-Z_-=O_{J,K}(\log Y),
\tag{13}
\]

and hence any endpoint fringe prime satisfies

\[
r_\pm\sim Z_\pm\sim Y,
\qquad
\frac{\log r_\pm}{\log Y}\longrightarrow1.
\tag{14}
\]

Multiplying (10) by `b\sqrt Y/\log Y` therefore yields exactly (4).

One can alternatively regard (4) as the empty-sum specialization of the layer-uniform law of `RE-062`,

\[
Q=-\sum_i\frac1{j_i}+\chi_+-\chi_-+o_{J,K}(1),
\tag{15}
\]

provided the reciprocal-depth sum is explicitly allowed to be empty. The point of recording (4) separately is not the algebraic empty-sum convention. It is the global consequence: first-layer-only packets were deliberately left outside the source-bearing count in `RE-065`, and the empty case shows exactly which part of that structural class is genuinely invisible to the charge mechanism.

Interior first-layer events disappear for the same reason as in `RE-045` and `RE-061`. Once an ordinary prime and its delayed first-layer CA event have both fired before the selected upper endpoint, their leading contributions are reconciled. A bounded packet does not retain one residual quantum per crossed first-layer prime. At the `\log Y/\sqrt Y` scale it remembers only whether an unmatched ordinary prime remains at either endpoint.

## 2. Double fringe exclusion leaves exactly three first-layer charge states

`RE-064` proves, without assuming any higher-layer event and without using the charge law, that a sufficiently late bounded packet cannot connect two fringe hosts:

\[
(\chi_-,\chi_+)\ne(1,1).
\tag{16}
\]

Its proof compares two incompatible scales. A bounded packet moves the logarithmic state coordinate only by `O_K(\log Y)`, so its endpoints have ratio tending to one. But `RE-063` maps every selected fringe state to the predecessor of a unique deep base-two event, and distinct such hosts are multiplicatively separated by asymptotic ratio at least two. Therefore two fringe endpoints cannot belong to one bounded packet.

Combining (16) with (4) leaves only

\[
(0,0),\qquad(0,1),\qquad(1,0),
\tag{17}
\]

and immediately gives (5). This makes the sign law especially rigid in the pure first-layer chamber. There is no Egyptian reciprocal-depth mass to tune and no growing-depth escape to exploit. The only order-one charge comes from entering or leaving the same ordinary-prime/CA-event mismatch already isolated by `RE-045`.

The `0 -> 0` case is therefore a genuine matched control for the signed-charge strategy. It can cross one or several first-layer physical events, but after both endpoints are matched the entire bounded packet is invisible at normalized leading order. The statement is only

\[
Q=o(1),
\tag{18}
\]

not `Q=0`: the lower-order normalization motion and finite-exponent effects remain. No rate strong enough to turn (18) into an aggregate contradiction is supplied here.

## 3. Every nonzero first-layer-only charge touches the lacunary base-two host set

A `0 -> 1` packet has its upper selected state in the fringe-host family of `RE-063`; a `1 -> 0` packet has its lower selected state in the same family. Let

\[
\mathcal F(T)
:=
\{C:\ C\text{ is an exposed selected state with }\chi_C=1,
\ \log C\le T\}.
\tag{19}
\]

`RE-063` gives

\[
|\mathcal F(T)|=O(\log T),
\tag{20}
\]

and maps the states in `\mathcal F` injectively to deep base-two event levels whose physical coordinates are multiplicatively lacunary.

In an ordered rightmost fan, one exposed state can occur as the upper endpoint of at most one switch and as the lower endpoint of at most one switch. Hence at most two first-layer-only nonzero-charge switches can be charged to any one fringe host. Therefore

\[
F^{\ne0}_{K}(T)
\le2|\mathcal F(T)|+O(1)
=O(\log T),
\tag{21}
\]

which proves (6).

This count treats both signs simultaneously. `RE-066` had already shown that positive bounded **source-bearing** charge is logarithmically sparse. Equation (21) adds the missing source-free half: a negative first-layer-only packet is just as sparse as a positive one, because its lower endpoint must itself be a fringe host. Thus first-layer-only packets cannot support polynomial complexity through a large signed charge ledger of either sign.

There is also a compatible one-step picture. A `0 -> 1` first-layer-only packet lands on a fringe host. By `RE-063` that state is immediately followed physically by a deep base-two event. If the fan continues through another bounded packet, that next packet necessarily contains a higher-layer event; `RE-064`--`RE-066` then force the successor out of the `1` fringe state with charge at most `-1+o(1)`. The positive pure-first-layer anomaly is therefore both sparse and followed, under bounded continuation, by the same negative debt already found for positive source-bearing switches.

## 4. The strong off-critical interruption ledger collapses to three live currencies

Use the polynomial-span strong-off-critical setting of `RE-065`. Its exposed-state count satisfies

\[
N_{\mathcal B}
\gg_J
X_{\mathcal B}^{\delta}\log X_{\mathcal B},
\qquad
\delta=1-b_1-\theta>0,
\tag{22}
\]

and its deep-layer capacity argument shows that at least

\[
X_{\mathcal B}^{\delta-o(1)}
\tag{23}
\]

switches fail to be quiet source-bearing for any fixed `K` and a sufficiently slow `\epsilon_X\to0`.

Partition those nonquiet switches more finely. Packets with more than `K` events contribute `U_{\mathcal B}`. Among bounded source-bearing packets, `RE-066` shows that positive nonquiet charges contribute only

\[
O(\log W_{\mathcal B})=O_A(\log X_{\mathcal B})
\tag{24}
\]

on the polynomial span (8); the remaining nonquiet source-bearing packets are counted by `N^-_{\ge2,\mathcal B}`.

It remains to refine the bounded packets having no higher-layer event. By Sections 1--3, all such first-layer-only switches except the matched `0 -> 0` class are again only

\[
O(\log W_{\mathcal B})=O_A(\log X_{\mathcal B}).
\tag{25}
\]

Therefore the complete `RE-065` nonquiet count is bounded above by

\[
U_{\mathcal B}
+F^{00}_{\mathcal B}
+N^-_{\ge2,\mathcal B}
+O_A(\log X_{\mathcal B}).
\tag{26}
\]

Combining (23) and (26), and absorbing the logarithmic term into the polynomial lower bound, proves (9).

The refinement matters because the three terms in (9) have genuinely different mathematical meanings. `U_{\mathcal B}` is a packet-complexity escape where the fixed-`K` local theory ceases to apply. `N^-_{\ge2,\mathcal B}` is a source-bearing signed obstruction tied to genuine higher-layer prime-power mass. `F^{00}_{\mathcal B}` is different from both: it is a bounded, source-free, charge-silent takeover by ordinary first-layer events. Treating all first-layer-only packets as generic structural interruptions hides that distinction.

## 5. Stress tests and the resulting obstruction

Equation (9) is **not** closer to a contradiction merely because it has fewer labels. The new `F^{00}` branch may be large. Ordinary first-layer events form the dense ambient mesh used in `RE-051`, and the present result gives no theorem preventing a polynomial number of matched `0 -> 0` packets from being exposed. In particular, one must not feed `F^{00}` into the growing-depth event count of `RE-065`: these packets contain no deep event to which that injection could attach.

The theorem also does not assert that a first-layer-only packet consists of one adjacent physical transition. It may skip finitely many first-layer CA states, provided no higher-layer or tied higher-layer occurrence lies in the complete physical packet. The cancellation in (4) is precisely robust under such bounded skipping: every interior first-layer atom reconciles before the upper selected endpoint.

The fixed packet bound remains essential. It is used in the common-scale estimate (13), in the uniform residual remainder, and in the double-fringe exclusion. With unbounded cardinality, two endpoint scales need not coalesce and distinct base-two fringe hosts are no longer ruled out by the local argument.

Nor does the result improve the short-interval exponent frontier of `RE-051`; the polynomial ledger remains available only in the strong off-critical chamber where `\Theta>\theta`. The present delta is orthogonal: once polynomial fan complexity has been forced, it identifies exactly what a source-free bounded contribution must look like.

This is also a falsification of one natural continuation of `RE-066`. It is not enough to prove that positive charges are sparse and then hope that every remaining first-layer interruption contributes negative drift. Most bounded first-layer-only packets can instead be perfectly matched at both endpoints and carry no leading charge at all. Any closing argument based on the signed selected-residual ledger must therefore add a statistic that sees these matched first-layer packets, or prove independently that they cannot dominate the exposed fan.

## 6. Prior-art boundary and research consequence

The underlying CA threshold structure is classical Alaoglu--Erdos material. Recent work of Mantovanelli organizes CA evolution into exact prime-layer event packets and verifies packet identities, while Zimov studies neighboring CA transitions and prime/semiprime quotients. A targeted current search of colossally abundant transition packets, Robin residuals, and consecutive CA quotients found those expected boundaries but no external result coupling Mathia's adaptive false-RH fan, the endpoint ordinary-prime/CA-event fringe bit, and the empty-higher-layer specialization (4)--(9). No new external theorem is load-bearing, so `SOURCES.md` requires no update.

The elementary statement that an empty higher-layer sum is zero is of course not a novelty claim. The durable line-specific delta is the global classification it unlocks: **bounded first-layer-only packets with nonzero normalized charge must touch the lacunary base-two fringe-host family and are only logarithmically numerous; every potentially polynomial bounded first-layer takeover is therefore `0 -> 0` and charge-silent.**

This materially sharpens the live escape map after `RE-065`--`RE-066`. On polynomial physical spans in the strong off-critical regime, a surviving false-RH fan must now spend polynomial complexity in at least one of three places:

\[
\boxed{
\text{unbounded packet complexity},
\qquad
\text{matched first-layer takeover},
\qquad
\text{negative higher-layer charge}.
}
\tag{27}
\]

The second branch is a clean matched control for the current charge observable. It should be attacked with a different cross-cell invariant—most naturally one that measures the ordering or cumulative geometry of first-layer support updates rather than their already-reconciled endpoint residual. The third branch remains the target for a genuinely signed accumulation argument.