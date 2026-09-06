# WP-175 — Weak boundary limits of passive Schur responses cannot reach the Gamma phase even distributionally

**Status:** `LITERATURE+DERIVED + WEAK-BOUNDARY-CLOSURE + LUZIN-PRIVALOV-RIGIDITY + ARCHIMEDEAN-GAMMA + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-174` closes ordinary singular parameter limits when the passive approximants remain Schur on a common interior domain, but deliberately leaves **weak/boundary-only convergence** open. That escape is smaller than it appears. For the exact real-place phase

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})},
\qquad |R_\infty(\tau)|=1\quad(\tau\in\mathbb R),
\tag{1}
\]

there is no sequence of ordinary scalar passive Schur responses whose boundary traces converge to `R_infty` **even in the sense of distributions on any nonempty open real interval**. In particular, weak-* `L^infty`, weak `L^p_loc`, local `L^1`, convergence in measure, and almost-everywhere convergence of uniformly contractive boundary responses are all impossible ways to obtain the exact Gamma phase.

The mechanism is classical but decisive. The unit ball of `H^infty` boundary functions is weak-* compact and weak-* closed. Any uniformly contractive boundary sequence therefore has a Schur weak-* cluster point. If the same sequence converges distributionally to (1) on an interval, that cluster point has boundary values equal to `R_infty` there. The Luzin--Privalov boundary uniqueness theorem then forces the Schur function to coincide with the holomorphic continuation of `R_infty` in the upper half-plane. `WP-170` proves that this continuation is not Schur, because its zero sequence violates the Blaschke condition. Contradiction.

Thus the weak-boundary escape explicitly retained by `WP-174` does **not** survive for the raw scalar passive response. A viable singular real-place mechanism must lose more than compact-open convergence: it must leave the uniformly contractive scalar Hardy class itself, change the domain/category before taking the boundary trace, use an unbounded or renormalized observable with a new sign theorem, or couple finite and archimedean sectors nonseparably before any scalar Gamma readout is formed.

## 1. Boundary compactness of the Schur ball

Let

\[
\mathbb H^+=\{z\in\mathbb C:\operatorname{Im}z>0\},
\qquad
\mathcal S=\{s\in H^\infty(\mathbb H^+):\|s\|_\infty\le1\}.
\tag{2}
\]

Every `s in S` has an almost-everywhere nontangential boundary trace `s^*` with

\[
|s^*(t)|\le1\quad\text{a.e. on }\mathbb R.
\tag{3}
\]

After a Cayley transform to the disk, these traces are exactly the unit ball of the Hardy subalgebra `H^infty(T) subset L^infty(T)`. That subalgebra is weak-* closed: equivalently, its forbidden Fourier coefficients vanish, and each coefficient is a weak-* continuous pairing with an `L^1` test function. Banach--Alaoglu then makes its unit ball weak-* compact.

Consequently, for every sequence `s_m in S` there is a subsequence and an `s in S` such that the transformed boundary traces converge weak-* to `s^*`. Returning to the real line gives the corresponding local statement on every bounded interval. No lossless assumption is involved: the approximants may be strictly contractive on the boundary.

This is the boundary analogue of the normal-family compactness used in `WP-174`, but the topology is much weaker. It does not require pointwise convergence at interior points, continuous boundary phases, or uniform boundary convergence.

## 2. Distributional identification on one interval already forces analytic identity

Let `I subset R` be any nonempty open interval and suppose, for contradiction, that

\[
s_m^*\longrightarrow R_\infty
\qquad\text{in }\mathcal D'(I).
\tag{4}
\]

Choose a bounded open interval `J` with compact closure inside `I`. By the weak-* compactness above, pass to a subsequence whose boundary traces converge weak-* to the trace of some `s in S`. Weak-* convergence implies distributional convergence on `J`, while the full sequence already has the distributional limit (1). Uniqueness of distributional limits therefore gives

\[
s^*(t)=R_\infty(t)
\quad\text{for a.e. }t\in J.
\tag{5}
\]

The Gamma quotient (1) is holomorphic through the real axis. More precisely, its first singularities below the axis occur at

\[
\tau=-\frac{i}{2},-\frac{5i}{2},\ldots,
\tag{6}
\]

so `R_infty` is holomorphic on a neighborhood of every compact real interval and throughout `H^+`.

Take a small upper half-disk `U` whose diameter lies in `J`. On `U`,

\[
F(z)=s(z)-R_\infty(z)
\tag{7}
\]

is bounded and holomorphic, and by (5) its angular boundary values vanish on a set of positive measure on the diameter. The Luzin--Privalov boundary uniqueness theorem gives

\[
F\equiv0\quad\text{on }U.
\tag{8}
\]

Since both functions are holomorphic on the connected upper half-plane, the identity theorem propagates (8):

\[
\boxed{s(z)\equiv R_\infty(z)\qquad(z\in\mathbb H^+).}
\tag{9}
\]

But `WP-170` gives the exact upper-half-plane zeros

\[
\tau_n=i\left(2n+\frac12\right),\qquad n\ge0,
\tag{10}
\]

and

\[
\sum_{n\ge0}
\frac{\operatorname{Im}\tau_n}{1+|\tau_n|^2}
=\infty.
\tag{11}
\]

The zero set of a nonzero bounded analytic function must satisfy the Blaschke condition. Hence `R_infty notin H^infty(H^+)`, contradicting `s in S`. Therefore

\[
\boxed{
\nexists\,(s_m)\subset\mathcal S
\text{ with }s_m^*\to R_\infty
\text{ in }\mathcal D'(I)
}
\tag{12}
\]

for every nonempty open interval `I`.

The important point is that (12) is **local on the boundary**. One does not need convergence on the whole critical line or on an interval spanning the phase-velocity reversal from `WP-170`. Exact weak convergence on any positive-length frequency window is already rigid enough to recover an analytic Schur cluster point, and boundary uniqueness then propagates the forbidden Gamma continuation.

## 3. Common weaker convergence modes are therefore closed too

Equation (12) immediately rules out several apparently weaker regularization schemes used for boundary/scattering responses.

If

\[
s_m^*\stackrel{*}{\rightharpoonup}R_\infty
\quad\text{in }L^\infty(I),
\tag{13}
\]

then (4) holds because smooth compactly supported test functions belong to `L^1(I)`. Thus weak-* convergence is impossible.

If `1<p<infinity` and

\[
s_m^*\rightharpoonup R_\infty
\quad\text{in }L^p(I),
\tag{14}
\]

then again every compactly supported smooth test belongs to the dual space, so (4) holds. The same is true for local `L^1` convergence.

If the boundary traces converge in measure on a finite subinterval, the uniform bound (3) makes the family uniformly integrable; convergence in measure to the bounded target then implies `L^1` convergence along the standard finite-measure argument. Likewise, almost-everywhere convergence plus (3) gives local `L^1` convergence by dominated convergence. Hence neither convergence in measure nor pointwise almost-everywhere convergence can produce (1) from ordinary passive Schur traces.

This is substantially stronger than the uniform-lossless phase-order control in `WP-174`. There the approximants were continuous unimodular responses with monotone phase lifts, and the contradiction required an interval spanning the sign reversal of the Gamma phase velocity. Here the approximants may be lossy, discontinuous as boundary traces, and convergence may be arbitrarily weak; the analytic Hardy constraint alone rules out the limit on every open interval.

## 4. The opposite causal orientation also fails

Changing half-plane orientation does not rescue the construction. A lower-half-plane Schur sequence can be reflected into the upper half-plane by

\[
\widetilde s_m(z)=\overline{s_m(\overline z)}.
\tag{15}
\]

If the original lower-half-plane boundary traces converged weakly to `R_infty`, the reflected upper-half-plane traces would converge to

\[
\overline{R_\infty(t)}=R_\infty(t)^{-1}.
\tag{16}
\]

The reciprocal is holomorphic across the real axis, so the same weak-* compactness and boundary-uniqueness argument forces an upper-half-plane Schur cluster point to agree locally with `R_infty^{-1}`. But `R_infty^{-1}` has poles at the upper-half-plane points (10). Analytic continuation from the boundary strip therefore collides with the first pole at `i/2`, contradicting bounded analyticity.

Thus neither causal orientation admits the exact real-place phase as a weak boundary limit of uniformly contractive scalar passive responses.

## 5. Aggressive falsification and matched controls

**Finite or measure-zero sampling is not ruled out.** The proof uses boundary uniqueness on a set of positive measure. Matching finitely many frequencies, a discrete lattice, or an exceptional null set can evade (12). Such interpolation remains only a fit unless the source geometry supplies a continuum identification and an independent positive theorem.

**Loss of the uniform Schur bound is a genuine escape.** If the visible responses are multiplied by factors with unbounded norm, divided by vanishing outer factors, or otherwise renormalized before the limit, weak-* compactness of the passive unit ball no longer applies. But then the inherited passivity theorem no longer proves positivity of the visible scalar. The renormalization itself needs a source-forced coercive or intersection theorem; choosing it to recover Gamma is the hand-picked-regularization failure mode in the research mandate.

**True domain degeneration is not covered.** The argument needs each approximant to define an ordinary scalar Schur function on one causal half-plane before taking boundary values. A sequence of relations or forms whose domains pinch to the boundary, or responses defined only on shrinking strips with no common Hardy realization, is outside the theorem. That is precisely a change of analytic category, not a weak limit inside the passive class.

**Operator-valued weak limits are only ruled out when a fixed contractive scalar readout is retained.** If `S_m(z)` are operator-valued Schur functions on a fixed Hilbert space and fixed vectors `u,v` are used, then `s_m(z)=<u,S_m(z)v>` satisfies (2), so (12) rules out convergence of that coefficient to `R_infty`. Changing dimensions, test vectors, Fredholm determinants, singular compressions, or renormalized scalarizations are not covered automatically; each such operation becomes part of the proposed mechanism and needs its own sign theorem.

**A positive control survives exactly when the target is genuinely passive.** For an upper-half-plane inner function such as

\[
S_a(z)=e^{iaz},\qquad a\ge0,
\tag{17}
\]

the constant sequence `s_m=S_a` trivially converges in every topology above. More generally, any actual Schur target is allowed. The contradiction is therefore not caused by weak convergence itself; it comes from attempting to place the exact Gamma boundary data in a weak-* closed passive Hardy class to which it does not belong.

**The theorem is archimedean, not an arithmetic discriminator.** As in `WP-174`, the compactness/uniqueness argument knows nothing about primes. It removes a proposed real-place positivity mechanism. The finite Mangoldt selector, polar terms, and the final global Weil sign still have to arise from one assembled Mathia-native geometry.

## 6. Prior-art and novelty audit

All functional-analytic ingredients are classical. Boundary values and weak-* compactness/closedness of bounded Hardy functions are standard `H^infty` theory; John B. Garnett, *Bounded Analytic Functions*, Springer GTM 236 (2007), is the same durable Hardy/inner reference already used in `WP-170` and `WP-174`. Paul Koosis, *Introduction to H^p Spaces*, 2nd ed., Cambridge University Press (1998/2008 printing), treats the upper-half-plane Hardy theory and duality explicitly.

The boundary-uniqueness step is the classical Luzin--Privalov theorem: N. N. Luzin and I. I. Privalov, *Sur l'unicité et la multiplicité des fonctions analytiques*, Annales scientifiques de l'École Normale Supérieure 42 (1925), 143--191. In the form needed here, a meromorphic function with angular boundary value zero on a boundary set of positive measure is identically zero. The present proof only needs the easier bounded-analytic local case.

The monotone phase structure of meromorphic inner functions discussed in `WP-170` is also classical; modern meromorphic-inner-function literature routinely writes `Theta(t)=e^{i phi(t)}` with a real-analytic strictly increasing phase. The new step here does not require differentiability or phase monotonicity of the approximants, so it is stronger than that control while remaining wholly within classical Hardy theory.

No novelty is claimed for Banach--Alaoglu, Hardy weak-* closure, Fatou boundary traces, Luzin--Privalov uniqueness, Blaschke necessity, or the identity theorem. The Mathia-specific substantive content is their application to the exact source-derived phase of `WP-169`--`WP-170` and to the **explicit weak-boundary escape left open by `WP-174`**:

\[
\boxed{
\text{ordinary scalar passive Schur approximants}
+\text{ any positive-measure weak boundary identification of }R_\infty
\Longrightarrow\bot.
}
\tag{18}
\]

This is a prior-art classicalization and a decisive narrowing, not a new theorem in Hardy-space theory and not a proof of Weil positivity.

## 7. Research consequence

`WP-174` left two broad-looking singular routes: lose the common interior analytic limit, or retain only weak boundary convergence. `WP-175` removes the second route **as long as the regularized visible responses remain uniformly contractive scalar Hardy functions on a causal half-plane**. Boundary weakening alone does not escape passivity: compactness recreates a Schur limit, and positive-measure boundary agreement analytically rigidifies it back to the forbidden Gamma transfer.

The remaining passive-looking architecture is therefore much narrower. A viable real-place completion must do at least one of the following before scalar Gamma identification:

- use a genuinely degenerating domain or relation-valued limit with a proved closed positive form;
- apply an unbounded/source-forced renormalization and prove a new coercivity theorem after renormalization;
- use changing-dimensional or infinite-index structure whose final positive termination is not a fixed Schur coefficient;
- or, most aligned with the branch mandate, couple finite-prime and archimedean data nonseparably so that `R_infty` is only a derived signed observable after the global positive theorem, not the passive characteristic function itself.

Merely replacing compact-open convergence by weak, almost-everywhere, or distributional convergence of ordinary passive boundary responses is no longer a live escape.