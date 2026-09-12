# RE-064 — bounded packets exclude double fringe and isolate Egyptian cancellation

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + BOUNDED-EVENT-PACKET + DOUBLE-FRINGE-EXCLUSION + EGYPTIAN-RESONANCE-ISOLATION + NEGATIVE-CHARGE-REBOUND + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-062` leaves two asymptotically vanishing charge architectures for a bounded fan-switch packet: a deep-layer escape with equal endpoint fringe bits, and an Egyptian-core escape with fringe pattern `0 -> 1`. The equal-bit branch still appears to allow both `0 -> 0` and `1 -> 1`. `RE-063` supplies exactly the missing geometry. A selected endpoint with fringe bit `1` is a predecessor of one deep base-two event, and distinct such hosts are multiplicatively lacunary in the physical scale. A bounded physical packet, however, moves the logarithmic state scale by only `O(log Y)` and hence has endpoint ratio tending to one. These two facts are incompatible.

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on the sufficiently late common positive CA counterexample blocks of `RE-040`. Let `b_n\in J` be fan breakpoints and let

\[
C_{-,n}<C_{+,n}
\tag{2}
\]

be the consecutive exposed fan states tied at `b_n`. Put

\[
Y_{\pm,n}:=\log C_{\pm,n},
\tag{3}
\]

and suppose the complete physical CA event packet between the endpoints has cardinality at most one fixed `K`. Let

\[
\chi_{\pm,n}\in\{0,1\}
\tag{4}
\]

be the endpoint ordinary-fringe bits of `RE-059`--`RE-063`, evaluated at the common breakpoint.

Then, for all sufficiently large `n`,

\[
\boxed{
(\chi_{-,n},\chi_{+,n})\ne(1,1).
}
\tag{5}
\]

This exclusion is independent of the residual charge and of the depths crossed by the packet. It uses only bounded packet cardinality and the genuine ordinary-prime/CA-event source mismatch encoded by a nonzero fringe bit.

Consequently the vanishing-charge classification of `RE-062` sharpens. If the packet contains at least one higher-layer event and

\[
Q_n:=
\frac{b_n\sqrt{Y_{-,n}}}{\log Y_{-,n}}
\left(
\mathcal R_{b_n}(Z_{+,n})-
\mathcal R_{b_n}(Z_{-,n})
\right)
\longrightarrow0,
\tag{6}
\]

then every subsequence has a further subsequence of exactly one of the following two types:

1. **Zero-fringe deep-layer escape:**
   \[
   \boxed{
   \chi_{-,n}=\chi_{+,n}=0,
   \qquad
   \min_i j_{i,n}\to\infty.
   }
   \tag{7}
   \]

2. **Egyptian-core escape:**
   \[
   \boxed{
   \chi_{-,n}=0,
   \qquad
   \chi_{+,n}=1,
   }
   \tag{8}
   \]
   with the fixed bounded-depth core of `RE-062` satisfying
   \[
   \sum_a\frac1{d_a}=1,
   \tag{9}
   \]
   while every noncore depth tends to infinity.

Thus **every asymptotically cancelling bounded packet has lower fringe bit zero**. The `1 -> 1` deep-layer escape is not merely sparse; it is impossible in the bounded-packet regime.

There is a further one-step consequence. Suppose an Egyptian-core packet as in (8)--(9) has upper state `C_{1,n}` which is not the terminal exposed state of its fan, and let `C_{2,n}>C_{1,n}` be the next exposed state at the next distinct breakpoint. If the physical packet from `C_{1,n}` to `C_{2,n}` also has cardinality at most `K`, then its normalized residual charge satisfies

\[
\boxed{
Q^{\rm next}_n
\le -1+o_{J,K}(1).
}
\tag{10}
\]

In particular,

\[
\boxed{
\liminf_n |Q^{\rm next}_n|\ge1.
}
\tag{11}
\]

So an Egyptian cancellation cannot be followed by another bounded asymptotically cancelling fan switch. Within any consecutive run of bounded packets whose normalized charges tend to zero, all nonterminal switches must be of the zero-fringe deep-layer type (7); at most the final switch can be Egyptian.

## 1. Bounded packets force the two physical state scales to coalesce

The bounded-packet geometry was established in `RE-061` and used uniformly in the depths in `RE-062`. Every physical event multiplies the CA state by its generating prime, so

\[
Y_{+,n}-Y_{-,n}
=
\sum_{e\in\mathcal P_n}\log p_e.
\tag{12}
\]

All event primes lie below the first-layer frontier of the upper state, which is asymptotic to `Y_{+,n}` on the late regular fan. With at most `K` event occurrences,

\[
\boxed{
Y_{+,n}-Y_{-,n}=O_K(\log Y_{+,n}).
}
\tag{13}
\]

Hence

\[
\boxed{
\frac{Y_{+,n}}{Y_{-,n}}\longrightarrow1.
}
\tag{14}
\]

This conclusion does not use the charge law and does not require fixed layer depths.

## 2. Two fringe endpoints would have to lie on different base-two rungs

Assume for contradiction that along an escaping subsequence

\[
\chi_{-,n}=\chi_{+,n}=1.
\tag{15}
\]

Apply `RE-063` separately to both selected endpoints at their common threshold `b_n`. Their immediate outgoing physical events are unique deep base-two events,

\[
\xi_{-,n}=\eta_{2,j_{-,n}},
\qquad
\xi_{+,n}=\eta_{2,j_{+,n}},
\tag{16}
\]

with

\[
Y_{\pm,n}\sim\xi_{\pm,n}.
\tag{17}
\]

Distinct regular selected states cannot have the same immediate outgoing event. Thus `j_{-,n}\ne j_{+,n}`. Since `Y_{+,n}>Y_{-,n}` and (17) holds uniformly on the compact fan, the ordering must eventually be

\[
j_{+,n}>j_{-,n}.
\tag{18}
\]

The exact base-two event equation used in `RE-063` gives

\[
\eta_{2,j}\log\eta_{2,j}
=(\log2)2^{j+1}(1+o(1)),
\tag{19}
\]

and therefore

\[
\frac{\eta_{2,j+1}}{\eta_{2,j}}\to2.
\tag{20}
\]

For depths differing by at least one, (18)--(20) imply

\[
\boxed{
\liminf_n
\frac{\xi_{+,n}}{\xi_{-,n}}\ge2.
}
\tag{21}
\]

Using (17),

\[
\boxed{
\liminf_n
\frac{Y_{+,n}}{Y_{-,n}}\ge2,
}
\tag{22}
\]

contradicting (14). This proves the double-fringe exclusion (5).

The argument is stronger than the count statement of `RE-063`: it shows that **one bounded packet cannot connect two selected fringe hosts at all** once the scale is sufficiently large. The obstruction is the mismatch between additive `O(log Y)` packet motion and multiplicative base-two host spacing.

## 3. The vanishing bounded-packet classification loses the `1 -> 1` branch

The layer-uniform charge law of `RE-062` is

\[
Q_n
=-s_n+\chi_{+,n}-\chi_{-,n}+o_{J,K}(1),
\qquad
s_n:=\sum_i\frac1{j_{i,n}}.
\tag{23}
\]

If `Q_n->0`, `RE-062` proves that, after subsequence extraction, either

\[
\chi_{+,n}=\chi_{-,n},
\qquad
s_n\to0,
\tag{24}
\]

or the Egyptian alternative (8)--(9) holds. Equation (5) removes the equal-bit value `1`. Hence (24) necessarily means

\[
\chi_{-,n}=\chi_{+,n}=0,
\tag{25}
\]

and `s_n->0`, equivalently every higher-layer depth diverges. This proves (7) and leaves (8)--(9) as the only other cancellation architecture.

Notice that this conclusion does **not** exclude deep-layer escape. It identifies its only remaining endpoint configuration. The difficult branch is now genuinely fringe-free.

## 4. Egyptian cancellation forces a negative charge rebound at the next bounded switch

Take an Egyptian-core switch from an exposed state `C_{0,n}` to `C_{1,n}`. At its breakpoint `beta_n`,

\[
\chi_{C_{1,n}}(\beta_n)=1.
\tag{26}
\]

Assume `C_{1,n}` is not terminal in the fan, and let `beta'_n>beta_n` be its next distinct breakpoint, with next exposed state `C_{2,n}`. By the convex-envelope ordering of `RE-038`, `C_{1,n}` owns the intervening threshold cell. Inside that fixed cell `RE-059` gives

\[
\chi_{C_{1,n}}(b)
=\mathbf 1_{\{r_{C_{1,n}}\le Z_{C_{1,n}}(b)\}},
\tag{27}
\]

and `Z_{C_{1,n}}(b)` is increasing. Therefore the fringe bit cannot return from one to zero while the same state remains selected:

\[
\boxed{
\chi_{C_{1,n}}(\beta'_n)=1.
}
\tag{28}
\]

Now suppose the physical packet from `C_{1,n}` to `C_{2,n}` has cardinality at most `K`. By the double-fringe exclusion (5), its upper bit must be zero:

\[
\boxed{
\chi_{C_{2,n}}(\beta'_n)=0.
}
\tag{29}
\]

Moreover `RE-063` says that `C_{1,n}` is immediately followed physically by a deep base-two event. Since `C_{2,n}` is a later exposed CA state, the intervening physical packet necessarily crosses that event, so it contains at least one higher-layer occurrence and the charge law (23) applies. Equations (28)--(29) give

\[
Q^{\rm next}_n
=-s^{\rm next}_n-1+o_{J,K}(1)
\le -1+o_{J,K}(1),
\tag{30}
\]

which proves (10)--(11).

Thus the Egyptian mechanism is not an indefinitely repeatable zero-charge architecture. It spends its `0 -> 1` endpoint compensation once, lands on a base-two fringe host, and a bounded continuation must immediately pay back at least one normalized unit with opposite sign. To avoid that rebound, the fan must terminate there or the next physical packet must leave the bounded-cardinality regime.

## 5. Stress tests and evidence boundary

The conclusion is conditional on the same false-RH compact-fan framework as `RE-040` and on a **uniform bound on physical packet cardinality**. If the number of crossed CA events diverges, (13) no longer forces endpoint scale ratio one and the double-fringe exclusion does not apply. This is a real remaining escape, not a technicality.

The theorem does not show that the selected residual charges themselves must tend to zero on most switches. It says what is possible **if** a bounded packet is in the vanishing-charge regime, and it gives the nonvanishing rebound after an Egyptian cancellation when the following packet stays bounded. Nor does it exclude long runs of the zero-fringe deep-layer type. That `0 -> 0` branch remains the principal bounded-packet obstruction.

No Alaoglu--Erdos consecutive-CA prime-quotient conjecture is assumed. The only quotient-`2` input is the line-internal theorem `RE-063`, which deduces it for selected fringe hosts from amplitude curvature and the sub-half-unit ordinary-prime/first-layer mismatch. The bounded packet estimate is already proved in `RE-061` without any conjecture on consecutive CA quotients.

A current prior-art audit against Alaoglu--Erdos, the August 2026 Mantovanelli prime-layer packet framework, and Zimov's work on neighboring CA transitions found the expected classical threshold structure, exact packet bookkeeping, and restrictions on consecutive transitions, but no result coupling an adaptive Robin fringe host to base-two lacunarity and then to a bounded fan-packet charge law. No external theorem beyond the sources already anchored in `SOURCES.md` is used here, and no priority claim is needed for the elementary composition itself.

## Consequence

The exceptional bounded-packet architecture of `RE-062` is now substantially smaller. A vanishing bounded packet is either a **fringe-free** deep-layer escape or an Egyptian `0 -> 1` resonance. The Egyptian branch is terminal inside any run of bounded vanishing-charge switches: if the fan continues through another bounded packet, the next normalized charge is negative and bounded away from zero by one unit.

Accordingly, a future closing argument no longer needs to treat `1 -> 1` deep-layer escape or recurrent Egyptian cancellation as independent long-run possibilities. For bounded packets, the only architecture capable of supporting an extended near-zero-charge fan is the `0 -> 0` deep-layer regime. The other global escape is explicitly unbounded packet cardinality.