# RE-068 — first-layer-only fan packets obey exact endpoint prime-set conservation

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + FIRST-LAYER-ONLY-PACKET + PRIME-SET-CONSERVATION + UNIQUE-FACTORIZATION-LIFT + ALL-ADDITIVE-SOURCE-INVARIANCE + UNBOUNDED-PACKET-EXTENSION + NEGATIVE/OBSTRUCTION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-067` shows that a bounded first-layer-only fan packet has normalized selected-residual charge

\[
Q=\chi_+-\chi_-+o(1),
\]

so the scalable branch left by that result is the matched `0 -> 0` packet. The cancellation is stronger than the particular Chebyshev/Mertens normalization used to define `Q`. At the two adaptive endpoints, a first-layer-only packet satisfies an **exact conservation law for the whole prime set**. The proof uses the endpoint-corrected Chebyshev invariant of `RE-059`, the fact that the higher-layer mass does not change across a first-layer-only packet, and unique factorization.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on sufficiently late common positive CA counterexample blocks from `RE-040`. At a rightmost-fan breakpoint `b\in J`, let

\[
C_-<C_+,
\qquad
Y_\pm:=\log C_\pm,
\tag{2}
\]

be consecutive exposed fan states tied for the same adaptive amplitude, and let `Z_-`, `Z_+` be their adaptive tangent selectors. Suppose that the **complete physical event packet** from `C_-` to `C_+` is first-layer-only: every crossed occurrence has depth `j=1`.

Let

\[
\mathcal E:=\{p:\ (p,1)\text{ occurs in the physical packet}\}
\tag{3}
\]

be its set of prime labels. At each endpoint write the first-layer correction of `RE-059` as

\[
\delta_\vartheta(Z_\pm)
=\chi_\pm\log r_\pm,
\qquad
\chi_\pm\in\{0,1\},
\tag{4}
\]

with the corresponding prime omitted when `\chi_\pm=0`. The common-amplitude selector map is eventually increasing, so `Z_-<Z_+`; define the ordinary-prime set crossed by the two selectors by

\[
\mathcal S
:=\{q\text{ prime}: Z_-<q\le Z_+\}.
\tag{5}
\]

Then one has the exact multiset identity

\[
\boxed{
\mathcal S\uplus\chi_-\{r_-\}
=
\mathcal E\uplus\chi_+\{r_+\}.
}
\tag{6}
\]

Equivalently,

\[
\boxed{
\left(\prod_{q\in\mathcal S}q\right)
 r_-^{\chi_-}
=
\left(\prod_{p\in\mathcal E}p\right)
 r_+^{\chi_+}.
}
\tag{7}
\]

The matched branch therefore satisfies the stronger exact law

\[
\boxed{
\chi_-=\chi_+=0
\quad\Longrightarrow\quad
\mathcal S=\mathcal E.
}
\tag{8}
\]

There is **no packet-cardinality hypothesis** in (6)--(8). In particular, a pure first-layer packet does not become arithmetically distinguishable merely because it contains many events.

Because (6) is equality of prime multisets, it immediately lifts from the logarithmic Chebyshev weight to every additive prime weight. For any function `w` on the primes,

\[
\boxed{
\sum_{Z_-<q\le Z_+}w(q)
+\chi_-w(r_-)
=
\sum_{p\in\mathcal E}w(p)
+\chi_+w(r_+).
}
\tag{9}
\]

Thus a matched `0 -> 0` first-layer packet is exactly invisible, at the **source-update level**, to every endpoint statistic whose arithmetic input is only an additive sum over the primes crossed by the selector. The weights `w(p)=\log p`, `w(p)=-\log(1-p^{-1})`, and `w(p)=1` give the Chebyshev mass, logarithmic Mertens source, and prime count respectively. The obstruction is therefore not special to the particular mixed prime-race coordinate used in `RE-045`--`RE-067`.

This does not make the packet invisible to all arithmetic information. The delayed event locations `p<\eta_{p,1}<p+1/2`, the selector positions inside the surrounding prime gaps, the Robin heights, higher-layer history, and non-additive relations between successive packets remain available. What (6)--(9) rule out is a broad proposed continuation of `RE-067`: **changing the additive endpoint prime weight cannot reveal the matched first-layer takeover.** Any successful statistic must spend information that is not already determined by the same crossed prime set.

## 1. The tied selector map preserves the order of the exposed states

At the breakpoint, put

\[
c:=A_b(C_-)=A_b(C_+)>0.
\tag{10}
\]

Along the formal common-amplitude curve define

\[
e^{h(Y)}-1=cY^{-b},
\qquad
 a(Y):=1-e^{-h(Y)}
=\frac{cY^{-b}}{1+cY^{-b}},
\tag{11}
\]

and let `Z(Y)` solve the same tangent equation as the selected states,

\[
g(Z(Y))
=g(Y)-\frac{b\,a(Y)}Y,
\qquad
g(x)=\frac1{x\log x}.
\tag{12}
\]

Differentiating `a` gives

\[
a'(Y)=-\frac{b}{Y}a(Y)(1-a(Y)),
\tag{13}
\]

hence, for the right-hand side `F(Y)` of (12),

\[
F'(Y)
=g'(Y)
+\frac{b\,a(Y)}{Y^2}
\bigl(1+b(1-a(Y))\bigr).
\tag{14}
\]

Now

\[
-g'(Y)
=\frac{\log Y+1}{Y^2(\log Y)^2}.
\tag{15}
\]

The uniform small-height regime of `RE-040` gives

\[
a(Y)\log Y\longrightarrow0
\tag{16}
\]

through the late positive fan. On the interval between two tied late states the same bound remains uniform because `a(Y)` decreases with `Y`. Therefore the positive term in (14) is `o(|g'(Y)|)`, and

\[
F'(Y)<0
\tag{17}
\]

throughout the relevant interval for all sufficiently late blocks. Since `g` is strictly decreasing, `g^{-1}` is also strictly decreasing, so

\[
\boxed{Z'(Y)>0.}
\tag{18}
\]

In particular

\[
\boxed{Y_-<Y_+\quad\Longrightarrow\quad Z_-<Z_+.}
\tag{19}
\]

This is the order statement underlying the local `dZ/dY=1+o(1)` calculation used in `RE-061`, but only monotonicity is needed here. No bounded-packet estimate enters.

## 2. First-layer-only motion freezes the higher-layer mass exactly

For a selected state `C` and its tangent selector `Z`, `RE-059` defines

\[
P_C:=\Phi_{\ge2}(Z)
\tag{20}
\]

and proves the exact endpoint-corrected Chebyshev invariant

\[
\boxed{
\vartheta(Z)-\delta_\vartheta(Z)=Y-P_C,
\qquad Y=\log C.
}
\tag{21}
\]

Because the complete physical packet from `C_-` to `C_+` contains no event of depth at least two, the active higher-layer mass is unchanged:

\[
\boxed{P_{C_+}=P_{C_-}.}
\tag{22}
\]

Every first-layer event `(p,1)` introduces the prime `p` with exponent one, so the exact state ratio is

\[
\frac{C_+}{C_-}
=\prod_{p\in\mathcal E}p.
\tag{23}
\]

Taking logarithms,

\[
\boxed{
Y_+-Y_-
=\sum_{p\in\mathcal E}\log p.
}
\tag{24}
\]

Apply (21) at the two selected endpoints and subtract. Using (4), (22), and (24),

\[
\begin{aligned}
\vartheta(Z_+)-\vartheta(Z_-)
&=Y_+-Y_-
+\delta_\vartheta(Z_+)-\delta_\vartheta(Z_-)\\
&=\sum_{p\in\mathcal E}\log p
+\chi_+\log r_+
-\chi_-\log r_-.
\end{aligned}
\tag{25}
\]

By (19) and right-continuity of `vartheta`, the left side is exactly

\[
\vartheta(Z_+)-\vartheta(Z_-)
=\sum_{q\in\mathcal S}\log q.
\tag{26}
\]

Thus

\[
\sum_{q\in\mathcal S}\log q
+\chi_-\log r_-
=
\sum_{p\in\mathcal E}\log p
+\chi_+\log r_+.
\tag{27}
\]

Exponentiating gives the integer product identity (7).

## 3. Genuine primality upgrades one conserved mass into a conserved prime multiset

Equation (27) by itself is an equality of one additive weight. The crucial extra input is that every label on both sides is an **ordinary prime**. The factors are positive integers, and the first-layer event `(p,1)` occurs at most once for each prime. Unique factorization therefore upgrades (7) to equality of prime multisets, proving (6).

This is where the ordinary-`sigma` fidelity isolated in `RE-057`--`RE-058` matters conceptually. A generalized or composite substitute label can preserve one logarithmic mass identity without making its event labels identifiable with the ordinary primes in the selector interval. For genuine first-layer CA atoms, the logarithmic mass is injective at the multiset level because

\[
\prod p^{m_p}=\prod p^{n_p}
\quad\Longrightarrow\quad
m_p=n_p\ \text{ for every prime }p.
\tag{28}
\]

No estimate, PNT error term, or linear-independence theorem for real logarithms is being used. The statement is simply uniqueness of integer prime factorization after the exact product equality has been obtained.

In the fringe-free case, (6) reduces immediately to (8). Hence the physical first-layer labels are exactly the ordinary primes lying between the two adaptive selector endpoints. They form one consecutive block of ordinary primes; there are no omitted primes and no extra ordinary primes in that selector interval.

More generally, (6) gives exact set-level versions of the three bounded classes of `RE-067`. When `RE-064` excludes the late bounded `1 -> 1` pattern, the remaining possibilities are

\[
\begin{array}{rcl}
0\to0&:&\mathcal S=\mathcal E,\\[2mm]
0\to1&:&\mathcal S=\mathcal E\uplus\{r_+\},\\[2mm]
1\to0&:&\mathcal E=\mathcal S\uplus\{r_-\}.
\end{array}
\tag{29}
\]

Thus the `+1` and `-1` normalized charges in `RE-067` have an exact pre-asymptotic source interpretation: the upper selector has crossed one prime whose first-layer event is still pending, or the lower selector starts with one pending prime whose event is consumed by the packet. The `0 -> 0` class is not merely small after normalization; its endpoint first-layer source is exactly reconciled.

## 4. Every additive endpoint prime statistic obeys the same conservation law

Once (6) is known, (9) is immediate for any function `w` on the primes because both sides are finite multisets. Several choices clarify what has and has not been gained.

For

\[
w(p)=\log p,
\tag{30}
\]

one recovers the Chebyshev/source-mass identity used in the proof. For

\[
w(p)=-\log(1-p^{-1}),
\tag{31}
\]

one obtains exact conservation of the raw logarithmic Mertens source across the same first-layer packet, including the same endpoint fringe correction. This is consistent with the second source invariant of `RE-059`, but now follows automatically from the prime-set identity rather than requiring a separate asymptotic comparison. For

\[
w(p)=1,
\tag{32}
\]

one gets the exact count relation

\[
\#\mathcal S+\chi_-
=\#\mathcal E+\chi_+.
\tag{33}
\]

The same holds for any finite arithmetic decoration `w(p)`: powers of `p^{-1}`, logarithmic powers, residue-class indicators, or another additive prime observable. In the matched case the selector interval and physical packet are literally summing over the same finite prime set.

This establishes a reusable no-go principle for the current frontier. Suppose a proposed refinement of the selected-residual charge replaces the Chebyshev or reciprocal-prime weight by another additive endpoint source while keeping only the set of ordinary primes crossed between `Z_-` and `Z_+`. On a `0 -> 0` first-layer-only packet, that source increment is already fixed exactly by the physical packet through (9). No choice of additive weight can create a source mismatch that is absent at the set level.

The conclusion is deliberately source-local. A statistic can still distinguish the packet if it uses information beyond the endpoint prime multiset: the positions `p` relative to their delayed coordinates `\eta_{p,1}`, the locations of `Z_-` and `Z_+` inside the neighboring prime gaps, the order and spacing of successive packets, higher-layer events, or a non-additive/global functional of the historical CA state. `RE-042` is an example of information that lives in transient prime/event timing; `RE-059` explains why that information is no longer present as an unmatched endpoint atom after complete reconciliation.

## 5. Boundary tests

The first-layer-only hypothesis is essential. If a higher-layer event occurs, then

\[
P_{C_+}-P_{C_-}\ne0
\tag{34}
\]

in general, and subtraction of (21) leaves exactly the higher-layer source mass that drives the negative charge in `RE-060`--`RE-066`. The set identity (6) is not valid after simply deleting that term.

The endpoint fringe terms are also essential. Dropping them would incorrectly assert `\mathcal S=\mathcal E` for `0 -> 1` and `1 -> 0` packets, precisely the two cases where `RE-067` finds a nonzero normalized charge. Equation (6) is the exact correction.

Completeness of the physical packet is essential as well. The state ratio (23) records every event occurrence between the two exposed states. Applying the claim to a selected subset of intervening first-layer events would destroy (24) and hence the product identity.

No bounded-cardinality assumption is needed for the exact source law, but this does **not** remove the unbounded-packet escape from the global ledger. A large first-layer packet may still create difficult selector geometry, and a large mixed packet can contain higher-layer events for which (6) fails. The result removes only a possible hope that pure first-layer complexity becomes visible merely because many first-layer atoms are crossed.

The theorem also does not show that matched packets are sparse. A consecutive block of ordinary primes can satisfy (8) without any contradiction. In that sense the result is principally negative: it identifies a whole class of endpoint observables that cannot be the missing statistic requested after `RE-067`.

Finally, the result does not claim that the normalized residual itself is exactly constant. Smooth normalization terms, Robin-height changes, finite-exponent tails, and selector displacement can still change between the endpoints. What is exact is the **arithmetic first-layer source multiset**. The `Q=o(1)` statement of `RE-067` is a stronger asymptotic statement about one normalized residual but requires bounded-packet control; (6)--(9) are exact source identities and require no such bound.

## 6. Prior-art boundary and research consequence

Alaoglu--Erdos supplies the classical prime-exponent threshold structure behind first-layer CA events. Mantovanelli's 2026 prime-layer workload framework gives exact packet-mass conservation and endpoint factorization for CA packets; the public companion explicitly checks packet identities by endpoint factorization, intervening event sums, and workload integration. Those are the closest prior-art structures, and no novelty is claimed for the state-ratio identity (23), unique factorization, or packet-mass bookkeeping separately.

A targeted current literature search found no external statement coupling those packet identities to the **adaptive ordinary-prime selector endpoints** of the false-RH fan and then upgrading the endpoint-corrected Chebyshev equality to the multiset law (6). No priority claim is made, and no external theorem beyond the sources already anchored in `SOURCES.md` is load-bearing. `SOURCES.md` therefore remains unchanged.

The durable line-specific consequence is a sharper description of the first-layer takeover left by `RE-067`. Matched `0 -> 0` packets do not merely have vanishing leading residual charge: **the ordinary primes crossed by the adaptive selectors are exactly the physical first-layer event labels, so every additive endpoint prime source is already reconciled.**

This narrows the next viable attack. To control a polynomial `F^{00}` takeover, one must use information that survives equality of the endpoint prime sets: prime/event timing, selector placement inside neighboring gaps, Robin-height or finite-tail evolution, higher-layer interaction, or a genuinely non-additive dependence across successive packets. Reweighting the same endpoint prime set cannot supply the missing obstruction.