# RE-065 — fringe-free deep-layer runs have subpolynomial capacity on polynomial scale windows

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + ADAPTIVE-FAN-RUN + GROWING-DEPTH-EVENT-COUNT + SUBPOLYNOMIAL-DEEP-LAYER-CAPACITY + POLYNOMIAL-FAN-INTERRUPTION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-064` leaves one bounded source-bearing architecture capable of sustaining a consecutive run of asymptotically vanishing selected-residual charges: zero-fringe packets whose higher-layer depths all escape to infinity. The local classification alone does not say whether such packets are plentiful enough to carry the polynomial fan complexity forced by `RE-051`. The missing comparison is a growing-depth version of the event-count hierarchy already implicit in `RE-004`.

Let

\[
M_{\ge r}(T)
:=\#\{(p,j):j\ge r,\ \eta_{p,j}\le T\},
\tag{1}
\]

count higher-layer event occurrences with their layer identity, including tied occurrences separately. Uniformly for every integer `r>=2`,

\[
\boxed{
M_{\ge r}(T)
\le
\log_2\!\left(\frac{T\log T}{\log2}\right)
\left(\frac{T\log T}{\log2}\right)^{1/r}.
}
\tag{2}
\]

Consequently, for any integer-valued depth cutoff `r(T)->infinity`,

\[
\boxed{M_{\ge r(T)}(T)=T^{o(1)}.}
\tag{3}
\]

This elementary extension becomes restrictive when combined with the bounded-packet charge law. Fix `A>=1`, one compact threshold interval

\[
J\Subset(1-\Theta,\tfrac12),
\tag{4}
\]

and one packet-cardinality bound `K`. On sufficiently late common positive CA blocks, consider a consecutive run of rightmost-fan switches whose exposed endpoint state scales

\[
Y=\log C
\]

all lie in

\[
\boxed{X\le Y\le X^A.}
\tag{5}
\]

Assume every physical packet in the run has at most `K` event occurrences, contains at least one higher-layer occurrence, and its normalized charge `Q` from `RE-062` obeys

\[
\boxed{
\sup_{\text{switches in the run}}|Q|\longrightarrow0
\qquad (X\to\infty).
}
\tag{6}
\]

Then the run length `L_X` satisfies

\[
\boxed{L_X=X^{o(1)}.}
\tag{7}
\]

Thus the fringe-free deep-layer escape is not merely sparse in ambient transition density. **On every polynomial physical-scale window it has only subpolynomial capacity as a consecutive bounded near-zero-charge fan mechanism.**

There is a direct global consequence in the strong off-critical regime of `RE-051`. Let `theta` be any exponent for which every sufficiently large `[x-x^theta,x]` contains a prime, assume `Theta>theta`, and fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1-\theta),
\qquad
\delta:=1-b_1-\theta>0.
\tag{8}
\]

For a late common block `\mathcal B`, put

\[
X_{\mathcal B}:=
\min_{C\in\mathcal E(\mathcal B,J)}\log C,
\qquad
W_{\mathcal B}:=
\max_{C\in\mathcal E(\mathcal B,J)}\log C.
\tag{9}
\]

`RE-051` gives

\[
N_{\mathcal B}
:=|\mathcal E(\mathcal B,J)|
\gg_J X_{\mathcal B}^{\delta}\log X_{\mathcal B}.
\tag{10}
\]

Fix `A` and restrict to blocks satisfying

\[
W_{\mathcal B}\le X_{\mathcal B}^A.
\tag{11}
\]

Fix also `K`, and let `\epsilon_{\mathcal B}->0`. Call a switch **quiet source-bearing** when its complete physical packet has at most `K` occurrences, contains a higher-layer event, and satisfies `|Q|<=epsilon_B`. If `B_{\mathcal B}` is the number of switches that are not quiet source-bearing, then

\[
\boxed{
B_{\mathcal B}
\ge
X_{\mathcal B}^{\delta-o(1)}.
}
\tag{12}
\]

Equivalently, on a polynomial-span strong-off-critical fan, polynomial complexity cannot be carried by long bounded source-bearing runs whose normalized charges vanish. Polynomially many interruptions must occur, and every interruption has at least one of three concrete forms:

\[
\boxed{
\text{packet cardinality}>K,
\quad
\text{no higher-layer event},
\quad\text{or}\quad
|Q|>\epsilon_{\mathcal B}.
}
\tag{13}
\]

If one tries to avoid such a polynomial interruption count for every fixed `A`, the remaining geometric escape is that the exposed fan itself has superpolynomial physical span `W_B=X_B^{\omega(1)}` along a subsequence.

## 1. The higher-layer count is uniform in a growing depth cutoff

`RE-004` proves the finite event-location inequality

\[
p^j\log p
\le
\eta_{p,j}\log\eta_{p,j}.
\tag{14}
\]

If `eta_(p,j)<=T`, put

\[
\mathcal Y(T):=\frac{T\log T}{\log2}.
\tag{15}
\]

Since `log p>=log2`, equation (14) gives

\[
p^j\le\mathcal Y(T).
\tag{16}
\]

Hence `p<=mathcal Y(T)^(1/j)`, and no such event exists once `2^j>mathcal Y(T)`. Counting primes by all integers therefore yields, for every `r>=2`,

\[
\begin{aligned}
M_{\ge r}(T)
&\le
\sum_{r\le j\le\log_2\mathcal Y(T)}
\mathcal Y(T)^{1/j}\\
&\le
\log_2\mathcal Y(T)\,
\mathcal Y(T)^{1/r},
\end{aligned}
\tag{17}
\]

which is (2). Unlike the fixed-`r` asymptotic quoted in `RE-004`, no implied constant depends on `r` here.

If `r=r(T)->infinity`, then

\[
\frac{\log M_{\ge r(T)}(T)}{\log T}
\le
\frac{1+o(1)}{r(T)}
+o(1)
\longrightarrow0,
\tag{18}
\]

proving (3). The statement counts event occurrences rather than distinct coordinates, so ties can only make any later injection easier.

## 2. Uniformly small charge forces every nonterminal switch deep and fringe-free

For a bounded source-bearing packet, `RE-062` gives uniformly in all layer depths

\[
Q
=-s+\chi_+-\chi_-+\rho,
\qquad
s:=\sum_i\frac1{j_i},
\tag{19}
\]

where, for fixed `J` and `K`,

\[
\sup_{Y\ge X}|\rho|\longrightarrow0.
\tag{20}
\]

Let

\[
q_X:=\sup_{\text{run}}|Q|,
\qquad
\omega_X:=\sup_{Y\ge X}|\rho|.
\tag{21}
\]

By (6), `q_X+omega_X->0`.

The fringe difference `d:=chi_+-chi_-` belongs to `{-1,0,1}`. The value `d=-1` is impossible eventually under (6), because (19) gives `Q<=-1+o(1)`. If `d=0`, then

\[
0<s\le q_X+\omega_X.
\tag{22}
\]

`RE-064` excludes the bounded-packet endpoint pattern `(1,1)`, so this equal-bit case is necessarily

\[
\chi_- = \chi_+ =0.
\tag{23}
\]

Moreover, if `j_min` is the smallest higher-layer depth in the packet, then `s>=1/j_min`; hence

\[
\boxed{
j_{\min}\ge\frac1{q_X+\omega_X}\longrightarrow\infty.}
\tag{24}
\]

The remaining value `d=1` is the Egyptian `0->1` possibility. `RE-064` proves that, if such a switch is followed by another bounded packet, the next normalized charge is at most `-1+o(1)`. Under the uniform near-zero assumption (6), an Egyptian switch can therefore occur only as the terminal switch of the run.

Thus, after discarding at most the final switch, **every packet in the run is `0->0` and all of its higher-layer depths exceed one common cutoff `r_X->infinity`.** This uniformity across the whole run is stronger than the one-packet subsequence statement of `RE-064` and is exactly what the global counting step needs.

## 3. Disjoint packets inject the run into the growing-depth event inventory

Consecutive exposed fan states are ordered CA states, so the complete physical event packets between successive exposed endpoints are disjoint in the event ladder. Select one higher-layer event from every nonterminal packet. By (24), the selected event has depth at least `r_X`, and different switches select different event occurrences.

The bounded-packet geometry of `RE-061`--`RE-062` gives uniformly

\[
\eta=Y_-(1+o_{J,K}(1))
\tag{25}
\]

for every event coordinate in a packet whose lower endpoint scale is `Y_-`. Under (5), all selected event coordinates therefore satisfy

\[
\eta\le2X^A
\tag{26}
\]

for sufficiently large `X`. Hence

\[
L_X-1
\le M_{\ge r_X}(2X^A).
\tag{27}
\]

Apply (2). Since `r_X->infinity`,

\[
\log M_{\ge r_X}(2X^A)
\le
\frac{A+o(1)}{r_X}\log X+o(\log X)
=o(\log X),
\tag{28}
\]

so (7) follows.

The mechanism is simple but source-specific: bounded near-zero charge forces the packet to consume progressively deeper genuine prime-power events, while the global supply of those events inside a polynomial coordinate window becomes subpolynomial.

## 4. Polynomial fan complexity therefore requires polynomially many interruptions

On a block satisfying (11), decompose its consecutive exposed switches into maximal quiet source-bearing runs separated by nonquiet switches. Let `B_B` be the number of separators. By (7), the maximum length of any quiet run is

\[
L_B=X_B^{o(1)},
\tag{29}
\]

uniformly over the block, because all endpoint scales are at least `X_B` and at most `X_B^A`.

There are at most `B_B+1` quiet runs, so the total number of switches satisfies

\[
N_B-1
\le
B_B+(B_B+1)L_B
\le
(B_B+1)(L_B+1).
\tag{30}
\]

Using the polynomial lower bound (10),

\[
B_B+1
\ge
\frac{N_B-1}{L_B+1}
=
X_B^{\delta-o(1)},
\tag{31}
\]

which proves (12). By definition, a nonquiet switch fails at least one of the three conditions in (13).

This is the first point in the packet-charge route where the polynomial fan complexity of `RE-051` and the higher-layer hierarchy of `RE-004` interact quantitatively. The local deep-layer escape of `RE-064` cannot simply be repeated often enough on a polynomial physical window to absorb the whole fan.

## 5. Stress tests and exact boundary

The theorem does **not** prove that the exposed fan has polynomial physical span. If `W_B/X_B^A` becomes unbounded for every fixed `A`, the event inventory up to `W_B` can be much larger, and (12) need not follow. Superpolynomial block/fan stretch is therefore a genuine geometric escape, consistent with the older block-stretch warnings in `RE-026`.

The theorem also does not eliminate first-layer-only packets. Such a packet has no higher-layer source occurrence to which the charge law (19) applies, and first-layer events have density one in the ambient transition count by `RE-004`. Equation (13) deliberately exposes a **first-layer takeover** as one possible global escape rather than hiding it inside the deep-layer classification.

Likewise, (12) does not say that all interruptions have large charge. Some may instead have growing packet cardinality, and some may contain no higher-layer event. Nor does a large count of nonquiet switches by itself force a sign contradiction for the selected residual. The result is a capacity obstruction, not an RH proof.

The event count uses occurrences, not distinct transition coordinates, so tied prime-power events cannot invalidate the injection. The run argument needs a uniform bound `K`: without it, `RE-064` no longer excludes double fringe and the packet coordinate may move by more than `O(log Y)`. This is exactly the separate unbounded-packet escape retained by the current frontier.

## 6. Prior-art boundary and research consequence

The classical Alaoglu--Erdos threshold structure and the recent Mantovanelli prime-layer framework supply the underlying prime-power event language; Mantovanelli's public companion verifies finite event sweeps and packet identities, while Zimov studies neighboring CA transitions. A targeted current search found no prior result coupling a **growing layer-depth cutoff** to the adaptive false-RH fan and then using the resulting event-capacity bound to force polynomially many packet interruptions. No new external theorem enters the proof, so `SOURCES.md` requires no new anchor.

The standalone estimate (2) is elementary and should not be treated as deep novelty; it is the uniform-in-`r` form of the counting argument already present in `RE-004`. The durable line-specific delta is the splice with `RE-062`--`RE-064`: vanishing bounded source-bearing runs automatically drive `r` to infinity, which collapses their available event inventory to `X^{o(1)}` on polynomial windows. Combining that with `RE-051` yields the interruption lower bound (12).

This changes the live global escape map. In the strongly off-critical chamber `Theta>theta`, a polynomial-span fan cannot be explained by one long sequence of bounded fringe-free deep-layer cancellations. To survive, it must instead generate polynomially many **nonquiet interruptions**—through unbounded packet complexity, first-layer-only switches, or charges that fail to vanish—or else stretch its exposed physical scale superpolynomially. Those are now the concrete global alternatives to attack.