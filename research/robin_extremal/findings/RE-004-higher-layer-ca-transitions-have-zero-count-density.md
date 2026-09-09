# RE-004 — higher-layer CA transitions have zero count density

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIME-LAYER-SPARSITY + ZERO-COUNT-DENSITY-EXCEPTIONAL-TRANSITIONS + COUNTEREXAMPLE-DICHOTOMY + PRIOR-ART-AUDITED`. `RE-003` leaves two qualitatively different boundary types around a hypothetical regular self-tangent Robin peak: single first-layer prime insertions, where the peak gate becomes an ordinary prime-gap restriction, and transitions involving higher prime-power layers or tied semiprime jumps. The latter chamber is not comparable in frequency to the prime frontier. The exact event-location inequality already established in `RE-003` implies that higher layers are sparse enough that they occupy zero density among CA transition coordinates.

Write

\[
g(X)=\frac1{X\log X},
\qquad
\lambda_{p,j}
=\log\frac{1-p^{-(j+1)}}{1-p^{-j}},
\qquad
\frac1{\eta_{p,j}\log\eta_{p,j}}
=\frac{\lambda_{p,j}}{\log p}.
\tag{1}
\]

Let `T(X)` be the number of **distinct** CA transition coordinates `eta<=X`, and let `E(X)` be the number of those coordinates whose transition is not exactly one first-layer event `(p,1)`. Then

\[
\boxed{
E(X)=O\!\left(\sqrt{X\log X}\right),
}
\tag{2}
\]

while

\[
\boxed{
T(X)=\pi(X)+O\!\left(\sqrt{X\log X}\right).
}
\tag{3}
\]

Consequently, by the prime number theorem,

\[
\boxed{
\frac{E(X)}{T(X)}
=O\!\left(\frac{(\log X)^{3/2}}{\sqrt X}\right)
\longrightarrow0.
}
\tag{4}
\]

Thus, in **transition-count density**, almost every sufficiently remote CA transition is one untied first-layer insertion of a prime. This does not prove the Alaoglu--Erdos prime-quotient conjecture, which asks for every transition; the zero-density exceptional set may still contain infinitely many higher-layer or semiprime transitions.

Combined with `RE-001`--`RE-003`, hypothetical RH failure therefore has a sharp two-chamber consequence. Either infinitely many forced self-tangent counterexample peaks are bracketed by two ordinary first-layer transitions, in which case their boundary primes are consecutive ordinary primes and satisfy

\[
\boxed{
q-p>
\frac{\log p+\log q}{2}-1-o(1)
=(1-o(1))\log p,
}
\tag{5}
\]

or infinitely many counterexample peaks have at least one boundary transition in the zero-density exceptional set counted by (2). The unresolved Robin route is consequently not a generic mixture of prime, prime-power and semiprime geometry: it is a choice between a source-selected large-prime-gap chamber and concentration of self-tangent peaks on a quantitatively sparse higher-layer chamber.

## 1. Higher-layer events have a square-root counting ceiling

`RE-003` proves for every prime layer `(p,j)` the finite inequality

\[
\boxed{
p^j\log p
\le
\eta_{p,j}\log\eta_{p,j}.}
\tag{6}
\]

Fix `X` large and set

\[
Y:=\frac{X\log X}{\log2}.
\tag{7}
\]

If `j>=2` and `eta_{p,j}<=X`, then (6) and `log p>=log2` imply

\[
p^j\le Y,
\qquad
p\le Y^{1/j}.
\tag{8}
\]

Moreover such an event can exist only while `2^j<=Y`, hence

\[
j\le\log_2Y.
\tag{9}
\]

Let

\[
M_{\ge2}(X)
:=\#\{(p,j):j\ge2,\ \eta_{p,j}\le X\},
\tag{10}
\]

where events are counted with their layer identity even when several thresholds coincide. Bounding primes by all integers gives

\[
\begin{aligned}
M_{\ge2}(X)
&\le
\sum_{2\le j\le\log_2Y}Y^{1/j}\\
&\le
Y^{1/2}+(\log_2Y)Y^{1/3}.
\end{aligned}
\tag{11}
\]

Since `log Y=o(Y^{1/6})`,

\[
\boxed{
M_{\ge2}(X)
=O\!\left(\sqrt{X\log X}\right).}
\tag{12}
\]

This bound deliberately counts **event occurrences**, which is at least as large as the number of distinct transition coordinates containing a higher layer. Ties therefore cannot invalidate it.

There is also a depth hierarchy. For every fixed `r>=2`,

\[
M_{\ge r}(X)
:=\#\{(p,j):j\ge r,\ \eta_{p,j}\le X\}
\le
(\log_2Y)Y^{1/r},
\tag{13}
\]

so

\[
\boxed{
M_{\ge r}(X)
=O_r\!\left((X\log X)^{1/r}\log X\right).}
\tag{14}
\]

In particular the only higher layer capable of saturating the square-root scale is `j=2`; genuinely deeper layers are successively thinner in transition count. Equation (14) is not a distribution theorem for self-tangent returns, but it identifies the nested exceptional sets on which any such concentration theorem would have to act.

## 2. First-layer event order is exactly prime order

For `j=1`, `RE-003` proves the much sharper localization

\[
\boxed{p\le\eta_{p,1}<p+1.}
\tag{15}
\]

If `p<q` are distinct primes, then `q>=p+1`, and hence

\[
\eta_{p,1}<p+1\le q\le\eta_{q,1}.
\tag{16}
\]

Thus distinct first-layer events never tie, and their order on the CA event axis is exactly the ordinary order of the primes.

Let

\[
M_1(X)
:=\#\{p:\eta_{p,1}\le X\}.
\tag{17}
\]

Every prime `p<=X-1` contributes, while every contributing prime satisfies `p<=X`. Therefore

\[
\boxed{M_1(X)=\pi(X)+O(1).}
\tag{18}
\]

The error is at most the bounded number of integer prime candidates in the final unit interval. No prime-spacing theorem enters this identity.

Every distinct CA transition coordinate is either one of these first-layer coordinates or contains at least one event with `j>=2`. Consequently

\[
M_1(X)\le T(X)\le M_1(X)+M_{\ge2}(X),
\tag{19}
\]

which proves (3).

Now classify a transition coordinate as exceptional when it is not **exactly one** first-layer insertion. Any such coordinate must contain a higher layer. Indeed, two distinct first-layer events cannot coincide by (16), so a tied transition cannot be composed solely of two first-layer prime insertions. Hence

\[
E(X)\le M_{\ge2}(X),
\tag{20}
\]

and (2) follows.

Alaoglu and Erdos prove that the quotient of two consecutive CA states is either a prime or a product of two distinct primes. Equation (20) gives a useful refinement of how the semiprime possibility enters this line: **every semiprime CA jump belongs to the higher-layer exceptional chamber**, because at least one of the two tied factors must arise from `j>=2`. Semiprime jumps therefore do not form a third asymptotic transition-count chamber independent of higher layers.

Finally, using the standard prime-number theorem `pi(X)~X/log X` in (2)--(3) gives (4). Only this last density ratio uses prime-distribution asymptotics; the square-root exceptional count and the classification (18)--(20) are exact consequences of the event geometry plus elementary inequalities.

## 3. Ordinary peak boundaries select consecutive prime gaps

Let `C` be a sufficiently large regular self-tangent local Robin peak furnished by the reduction in `RE-001`, and let `eta_-<X<eta_+`, `X=log C`, be its two adjacent CA transition coordinates as in `RE-002`--`RE-003`.

Suppose both transitions are nonexceptional. Then there are primes `p<q` such that

\[
\eta_-=\eta_{p,1},
\qquad
\eta_+=\eta_{q,1}.
\tag{21}
\]

They must be **consecutive ordinary primes**. If another prime `r` satisfied `p<r<q`, equation (16) would place its first-layer event strictly between `eta_-` and `eta_+`, contradicting adjacency of the CA transitions.

The boundary jumps are then

\[
w_-=\log p,
\qquad
w_+=\log q.
\tag{22}
\]

`RE-003` proves that every such peak must obey

\[
q-p>
\frac{\log p+\log q}{2}-1-o(1),
\tag{23}
\]

where the vanishing term comes from its uniform `O((log X)^2/X)` secant correction. Bertrand's postulate gives `q<2p` for consecutive sufficiently large primes, so

\[
\frac{\log p+\log q}{2}
=\log p+O(1).
\tag{24}
\]

Along any unbounded sequence of ordinary-boundary peaks, therefore,

\[
\boxed{
\liminf\frac{q-p}{\log p}\ge1.}
\tag{25}
\]

This is not a statement that such prime gaps are rare enough to contradict RH failure. Prime gaps of logarithmic size and larger occur, and ordinary prime-gap existence alone does not encode the self-tangent selection `D(X)=0`. The result identifies the **only** prime-frontier gaps that can host the clean transition chamber of a Robin counterexample peak.

## 4. RH failure must choose one of two asymptotic chambers

`RE-001` proves

\[
\mathrm{RH\ false}
\Longrightarrow
\text{infinitely many regular self-tangent CA counterexample peaks}.
\tag{26}
\]

Classify each such peak according to whether both adjacent transition coordinates are nonexceptional. There are only two possibilities for an infinite set of peaks.

If infinitely many are nonexceptional on both sides, equations (21)--(25) produce infinitely many **source-selected consecutive prime gaps** satisfying the asymptotic lower threshold in (25), with the self-tangent coordinate lying between their first-layer event locations.

Otherwise infinitely many peaks touch an exceptional transition, and hence infinitely many forced counterexample peaks concentrate on the set counted by `E(X)`. By (4), that set has transition-count density zero among all remote CA transitions. More strongly, (14) stratifies this chamber by layer depth; peaks involving arbitrarily deep layers would concentrate on successively thinner event sets.

Thus

\[
\boxed{
\mathrm{RH\ false}
\Longrightarrow
\begin{cases}
\text{infinitely many self-tangent peaks selected inside consecutive-prime gaps}\\
\qquad\text{with }\liminf(q-p)/\log p\ge1,\\[2mm]
\text{or infinitely many self-tangent peaks touch the zero-density higher-layer chamber.}
\end{cases}}
\tag{27}
\]

The alternatives are not asserted mutually exclusive; both may occur infinitely often. Their value is that they require different mathematics. The first asks why self-tangency would repeatedly select large normalized ordinary prime gaps. The second asks why the same nonlinear return condition could concentrate on a transition set whose ambient counting density vanishes.

This is stronger than simply saying that higher prime powers remain unresolved. It supplies a quantitative exceptional-set theorem and shows that semiprime transitions are already contained in that exceptional set.

## 5. Prior art and novelty boundary

The event-axis representation, self-tangent terminology and prime-frontier decomposition are closest to Marco Mantovanelli's August 2026 preprint *Colossally Abundant Numbers, Robin's Inequality, and an Exact Prime-Layer Workload*, already anchored in `SOURCES.md`. Its public Zenodo companion verifies the finite event sweep, regular returns, packet identities and selected prime-frontier decompositions through its certified range. Those objects are treated as prior art here; no novelty is claimed for separating the first prime layer from higher layers.

Alaoglu--Erdos is the load-bearing classical source for the CA threshold structure and the prime-or-product-of-two-distinct-primes theorem for consecutive CA quotients. The open stronger conjecture that every consecutive quotient is prime has extensive numerical support, but it is not assumed. The present statement is deliberately weaker in quantifier and stronger in provenance: it proves only that non-single-first-layer transitions have **zero transition-count density**, directly from the exact layer coordinates. It does not promote numerical prime-quotient evidence to a theorem.

A targeted prior-art search across the consecutive-CA quotient literature, the recent prime-layer workload framework, and formulations of the prime-quotient conjecture did not locate the specific counting splice (2)--(4), the absorption of every semiprime transition into the higher-layer exceptional set via (15)--(20), or the counterexample dichotomy (27). The counting estimate itself is elementary once (6) is exposed and should not be treated as a deep standalone novelty claim. The durable Mathia delta is the exact use of that sparsity inside the `RE-001`--`RE-003` counterexample reduction.

No new source anchor is required: the only non-elementary inputs are already recorded in `SOURCES.md`, and the prime number theorem is used only to convert the exact exceptional-count estimate into the density statement (4), not to obtain a Robin-sign estimate.

## 6. Boundaries and falsification checks

The density in (4) is **counting density of CA transition coordinates**, not Lebesgue density on the event axis and not density among self-tangent returns. A zero-density set of transition coordinates can still contain every member of a much sparser selected subsequence. Therefore (4) alone gives no contradiction to (26).

Likewise, (12) counts layer occurrences, not distinct coordinates. This is intentional: ties can only reduce the number of exceptional coordinates, so occurrence counting is a safe upper bound. Equation (20) uses the strict order (16); without that fact one could not conclude that every tied semiprime transition contains a higher layer.

The prime-gap branch uses the full-event adjacency. Two nonexceptional boundary primes are consecutive ordinary primes because any intervening prime would create an intervening first-layer event. The lower bound (25) is only a necessary condition inherited from `RE-003`; it does not make a large prime gap sufficient for a self-tangent peak.

Finally, the prime-number theorem in (4) must not be confused with the RH-sensitive prime-distribution estimates that would be needed to force the workload sign. No error term stronger than the classical asymptotic is imported. The unresolved implication is selection, not ambient frequency: either exclude repeated self-tangent selection of the large-prime-gap chamber, or prove that regular counterexample returns cannot concentrate on the higher-layer exceptional sets quantified above.

## 7. Consequence for the research line

The local event-gap route now has a cleaner frontier. Generic semiprime bookkeeping and generic higher-prime-power interlacing should not be treated as coequal ambient cases with ordinary prime insertions. In transition count, the prime frontier is the density-one background; every deviation from it is carried by an explicit square-root-sized exceptional family, with deeper layers obeying the hierarchy (14).

A useful next theorem should therefore attack **selection into the exceptional set**, not simply its size. One route is to combine self-tangent return identities with the layer-depth hierarchy and show that zeros of `D(X)=X-Phi(X)` cannot repeatedly align with transitions generated by `j>=2`. The complementary route is to stay in the density-one prime chamber and exploit the fact that every clean counterexample peak must select a consecutive prime gap at least of mean-gap scale while simultaneously satisfying the exact self-tangent mass balance. Either route adds a condition not supplied by ordinary prime-gap existence or by the ambient transition counts alone.