# RE-018 — bounded ordinary envelopes force fixed-base event-ladder near-collisions

**Status:** `EXACT-DERIVED + BOUNDED-ENVELOPE-HOST-COUNT + FIXED-BASE-NEAR-COLLISION + DIOPHANTINE-REDUCTION + COUNTEREXAMPLE-NARROWING + NEGATIVE/OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-017` shows that the ordinary-prime envelope around the two adjacent CA transitions of a regular self-tangent local Robin peak controls both the prime bases and the layer depths occurring at those transitions. In the bounded-envelope regime this can be sharpened substantially: the admissible host set has only logarithmic size, and any infinite escape is forced onto two fixed distinct prime-power event ladders whose critical slopes approach one another at exponentially fine relative scale.

Fix `G>0`. Let `C` range over sufficiently large regular self-tangent CA local peaks with

\[
X:=\log C
\]

and ordinary-prime envelope gap `g(C)` as in `RE-017`, satisfying

\[
g(C)\le G.
\tag{1}
\]

Write `eta_-<X<eta_+` for the adjacent CA transition coordinates. Then:

1. every prime factor `r` occurring at either boundary transition belongs to a finite set depending only on `G`; explicitly, for all sufficiently large peaks,

\[
\boxed{r<\exp(2G+3).}
\tag{2}
\]

2. if `N_G(Z)` counts such peaks with `X<=Z`, then

\[
\boxed{N_G(Z)=O_G(\log Z).}
\tag{3}
\]

3. if there are infinitely many such peaks, then after passing to an infinite subsequence there exist two **fixed distinct primes** `r!=s` and layer indices `j_n,k_n -> infinity` such that

\[
\eta_{r,j_n}=\eta_-^{(n)},
\qquad
\eta_{s,k_n}=\eta_+^{(n)},
\]

and

\[
\boxed{
0<\eta_{s,k_n}-\eta_{r,j_n}<G+1.
}
\tag{4}
\]

Equivalently, for the critical CA slopes

\[
\varepsilon_{r,j}
:=\frac{\lambda_{r,j}}{\log r}
=\frac1{\eta_{r,j}\log\eta_{r,j}},
\]

one has

\[
\boxed{
\left|
\varepsilon_{r,j_n}-\varepsilon_{s,k_n}
\right|
=O_G\!\left(\frac1{X_n^2\log X_n}\right),
}
\tag{5}
\]

and therefore

\[
\boxed{
\frac{|\varepsilon_{r,j_n}-\varepsilon_{s,k_n}|}
{\varepsilon_{r,j_n}}
=O_G(X_n^{-1}).
}
\tag{6}
\]

Thus bounded ordinary envelopes do not merely push the boundaries into the generic higher-layer chamber. They force an infinite hypothetical escape into repeated near-coincidences between two fixed prime-power event ladders. Since `X_n` grows exponentially in the relevant layer depth, (6) is an exponentially fine relative approximation in those indices.

## 1. Bounded envelopes freeze the boundary prime bases

`RE-017` proves that every prime factor `r` at either adjacent boundary satisfies

\[
\log r<2g(C)+2+o(1).
\tag{7}
\]

Under (1), the `o(1)` is below `1` for all sufficiently large peaks, hence

\[
\log r<2G+3,
\]

which is (2). Therefore every boundary transition is assembled from event atoms whose prime bases lie in the fixed finite set

\[
\mathcal P_G:=\{r\text{ prime}: r<e^{2G+3}\}.
\tag{8}
\]

At the same time `RE-017` gives

\[
j(r)\ge
\frac{\log X-O(1)}{2g(C)+2+o(1)},
\tag{9}
\]

so every layer index occurring at either boundary tends to infinity along any unbounded family satisfying (1). Bounded envelopes therefore freeze the bases while driving the event depths upward.

## 2. The bounded-envelope host set is only logarithmic

For a fixed prime `r`, let `eta_(r,j)` denote its layer-`j` CA event coordinate. The event-size inequality of `RE-017` is

\[
r^j\log r
\le
\eta_{r,j}\log\eta_{r,j}.
\tag{10}
\]

Hence every event of base `r` with `eta_(r,j)<=Z` satisfies

\[
j\log r
\le
\log Z+\log\log Z-\log\log r,
\tag{11}
\]

so the number of such layers is `O_r(log Z)`. Summing over the finite set `mathcal P_G` gives

\[
\#\{(r,j):r\in\mathcal P_G,\ \eta_{r,j}\le Z\}
=O_G(\log Z).
\tag{12}
\]

As in `RE-017`, a regular self-tangent state in an open CA event gap is unique, so mapping a peak to its left boundary transition is injective. A tied transition contains at most two event atoms by the Alaoglu--Erdos consecutive-CA theorem; in particular the number of transition coordinates is no larger than the number of event atoms. Since the left boundary lies below `X<=Z`, (12) proves (3).

This improves the generic subpolynomial host-set conclusion of `RE-017` in the fixed bounded-gap regime from `O_epsilon(Z^epsilon)` to `O_G(log Z)`. It remains a host-set theorem: logarithmically many admissible locations are still enough to support an infinite counterexample subsequence.

## 3. An infinite bounded-envelope family forces two fixed distinct ladders

Assume now that infinitely many peaks satisfy (1). At each peak choose one event atom from the left boundary transition and one from the right. By (2), only finitely many ordered pairs of prime bases can occur. Passing to an infinite subsequence therefore fixes bases `r,s in mathcal P_G`, while (9) forces their corresponding layer indices `j_n,k_n` to infinity.

The envelope construction in `RE-017` gives

\[
\eta_+-\eta_-<g(C)+1\le G+1,
\tag{13}
\]

so (4) follows once we show that `r` and `s` cannot be the same prime.

For fixed `r`, put

\[
S_{r,j}:=r+r^2+\cdots+r^j
=\frac{r^{j+1}}{r-1}(1-r^{-j}),
\]

\[
\lambda_{r,j}=\log(1+S_{r,j}^{-1}),
\qquad
A_{r,j}:=\frac{\log r}{\lambda_{r,j}}.
\tag{14}
\]

Since `S_(r,j)->infinity`, the elementary expansion `log(1+u)=u+O(u^2)` gives

\[
A_{r,j}
=
\frac{\log r}{r-1}\,r^{j+1}
\bigl(1+O(r^{-j})\bigr).
\tag{15}
\]

The event equation is

\[
\eta_{r,j}\log\eta_{r,j}=A_{r,j},
\]

hence exactly

\[
\eta_{r,j}=\frac{A_{r,j}}{W(A_{r,j})},
\tag{16}
\]

where `W` is the principal Lambert function. From (15),

\[
\frac{A_{r,j+1}}{A_{r,j}}\to r,
\qquad
\frac{W(A_{r,j+1})}{W(A_{r,j})}\to1,
\]

and therefore

\[
\boxed{
\frac{\eta_{r,j+1}}{\eta_{r,j}}\to r>1.
}
\tag{17}
\]

In particular the distance between consecutive points of one fixed prime ladder tends to infinity. Two distinct boundary coordinates at distance at most `G+1` cannot therefore lie on the same fixed ladder once their depths are large. Thus `r!=s`, proving (4).

## 4. Bounded event distance becomes an exponentially fine slope near-collision

The common CA parameter attached to an event coordinate is the decreasing smooth function

\[
f(x):=\frac1{x\log x}.
\tag{18}
\]

For the chosen boundary atoms,

\[
\varepsilon_{r,j_n}=f(\eta_-^{(n)}),
\qquad
\varepsilon_{s,k_n}=f(\eta_+^{(n)}).
\tag{19}
\]

By (13), both boundary coordinates differ from `X_n` by `O_G(1)`. Since

\[
|f'(x)|
=
\frac{\log x+1}{x^2(\log x)^2}
=O\!\left(\frac1{x^2\log x}\right),
\tag{20}
\]

the mean-value theorem gives (5). Also `f(eta_-)=asymp 1/(X_n log X_n)`, yielding (6).

Using (15), each slope itself is asymptotic to

\[
\varepsilon_{r,j}
=
\frac{r-1}{r^{j+1}\log r}
\bigl(1+O(r^{-j})\bigr).
\tag{21}
\]

Thus (5) can be read as a quantitative near-equality between two fixed exponential ladders with different prime bases. Taking logarithms of the main terms leads to an approximation involving

\[
(j_n+1)\log r-(k_n+1)\log s
\]

and a fixed offset containing `log log r` and `log log s`. This is precisely why ordinary linear-forms-in-logarithms heuristics must not be invoked casually here: the normalization constants are not logarithms of known algebraic numbers in the form required by a direct Baker-theory application.

## 5. Prior-art boundary: even exact two-ladder coincidence is a classical open obstruction

Alaoglu and Erdos already identified the exact-tie problem behind consecutive colossally abundant numbers. Their Theorem 10 gives the prime-exponent threshold formula and observes that a jump in the exponent for a prime `q` at parameter `epsilon` makes `q^epsilon` rational. They note that proving two distinct primes cannot jump simultaneously would follow from excluding simultaneous rationality of `p^epsilon` and `q^epsilon` for nonintegral `epsilon`; they explicitly state that they could not prove this. The three-prime theorem communicated by Siegel yields only the weaker classical conclusion that a quotient of consecutive CA numbers is either one prime or a product of two distinct primes.

That source is already anchored in `SOURCES.md`, so no new bibliographic entry is needed. A targeted search of the CA/consecutive-CA and transcendence literature did not locate a quantitative theorem excluding the bounded additive near-collisions (4), nor a result that would turn (5) into a contradiction. No novelty is claimed for the underlying transcendence problem. The Mathia-specific delta is the route reduction: **if regular self-tangent Robin peaks persist inside a fixed ordinary-prime envelope, then the Robin extremal geometry forces exactly such fixed-base near-collisions, and only `O_G(log Z)` event gaps can host them up to height `Z`.**

The distinction between exact and approximate coincidence is load-bearing. The Alaoglu--Erdos discussion does not prove a lower bound for `|eta_(r,j)-eta_(s,k)|`, and the present argument does not manufacture one. A future quantitative separation theorem strong enough to show this distance tends to infinity for every fixed `r!=s` would eliminate the entire bounded-envelope branch, but establishing that separation is a new arithmetic obligation rather than a consequence proved here.

## 6. Research consequence and failure modes

This finding applies to all sufficiently large regular self-tangent CA local peaks satisfying the fixed bound `g<=G`, whether safe or violating. Counterexample status enters only when combined with the `RE-001` reduction under hypothetical RH failure. It does not control peaks for which `g` grows, even as slowly as `log log X`, without an additional uniform argument; `RE-017` remains the authoritative statement for the general sublogarithmic regime.

The result therefore narrows one exceptional escape without closing it. In the bounded-envelope chamber, an infinite counterexample family would have to live on a logarithmically sparse host set and repeatedly synchronize two fixed distinct deep prime-power ladders to additive `O_G(1)` accuracy, equivalently relative critical-slope accuracy `O_G(1/X)`. The clean selected mixed-race annulus of `RE-014`--`RE-016` remains a separate obligation, and no claim is made that this Diophantine synchronization controls that annular race. A useful continuation is either a genuine quantitative separation theorem for the fixed event ladders, or a proof that any remaining counterexample peaks must have unbounded ordinary envelopes; merely citing the classical exact-tie conjecture is not enough.