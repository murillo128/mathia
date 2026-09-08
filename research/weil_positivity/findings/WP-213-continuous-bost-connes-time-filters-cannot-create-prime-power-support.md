# WP-213 — Continuous Bost–Connes time filters cannot create prime-power support; exact spectral selection is necessarily singular

**Status:** `DERIVED + EXACT + BOST-CONNES-KMS + CONTINUOUS-FUNCTIONAL-CALCULUS + DENSE-RATIONAL-LOG-GRADES + PRIME-POWER-SUPPORT-OBSTRUCTION + BOREL-SINGULAR-ESCAPE + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-209`--`WP-212` leave an explicit escape after bounded KMS correlations fail: perhaps an unbounded affiliated observable, distributional vector, or closable positive form can retain the source-forced critical half-density while carrying the missing Mangoldt support and mass. There is a sharp distinction inside that escape.

The Bost--Connes time grading is indexed by positive rationals,

\[
\Gamma:=\{\log q:q\in\mathbb Q_+^\times\}\subset\mathbb R,
\]

while the signed prime-power frequencies required by the finite Weil term are

\[
\mathcal P
:=\{\pm k\log p:p\text{ prime},\ k\ge1\}.
\]

The set `Gamma` is dense in `R`, whereas `P` is locally finite. Consequently

\[
\boxed{\Gamma\setminus\mathcal P\text{ is dense in }\mathbb R.}
\]

This elementary topology gives a complete obstruction to every **continuous scalar functional-calculus selector** of the physical time generator. If `F:R->C` is continuous and

\[
F(\log q)=0
\qquad
\text{for every }\log q\in\Gamma\setminus\mathcal P,
\]

then necessarily

\[
\boxed{F\equiv0.}
\]

Thus no nonzero continuous, smooth, analytic, resolvent-generated, semigroup-generated, Bernstein, operator-monotone, or other continuous scalar function of the Bost--Connes time energy can by itself erase all mixed rational grades while retaining the prime-power grades. Allowing the scalar function to be unbounded does not help: continuity, not boundedness, is the obstruction.

There is also a quantitative version. If `F` is continuous and

\[
|F(\gamma)|\le\varepsilon
\qquad(\gamma\in\Gamma\setminus\mathcal P),
\]

then density forces `|F(x)|<=epsilon` for **every** real `x`. Hence a regular time filter cannot even keep an order-one prime-power response while uniformly suppressing all unwanted rational grades. Any exact or uniformly sharp selector must leave the norm-continuous functional calculus.

The spectral theorem also identifies the escape exactly. Since `P` is a closed locally finite Borel subset of `R`, its indicator defines the bounded Borel projection

\[
\mathbf 1_{\mathcal P}(H),
\]

whenever `H` denotes the self-adjoint generator in a representation carrying the corresponding time spectrum. More generally the nonnegative Borel symbol

\[
M_\Lambda(E)
:=
\begin{cases}
\log p,&E=\pm k\log p,\\
0,&E\notin\mathcal P
\end{cases}
\]

defines a positive self-adjoint spectral multiplier and therefore a closed positive quadratic form on its natural form domain. So **positivity and closability do not obstruct a target-coded prime-power selector at all** once arbitrary Borel functional calculus is admitted.

That is not a positive result for the Mathia mandate. The same construction works for any chosen locally finite frequency set and any prescribed nonnegative weights. The Borel symbol has simply been told which grades are prime powers and what Mangoldt weight to assign them. It is exactly the kind of inserted arithmetic kernel that the research contract excludes unless an independent geometric construction forces it.

The surviving Bost--Connes question is therefore narrower than `WP-209`--`WP-212` stated. An unbounded or closable **scalar time-functional-calculus** repair has only two regimes:

\[
\boxed{
\text{regular/continuous calculus}
\Longrightarrow
\text{cannot create prime-power support},
}
\]

whereas

\[
\boxed{
\text{arbitrary Borel calculus}
\Longrightarrow
\text{can encode essentially any desired support and weights by definition}.
}
\]

A genuine escape must explain a singular spectral projection from additional source geometry, put the prime-power support into the source object before scalar time calculus is applied, or use a non-scalar/noncommutative/global coupling. Mere unboundedness, self-adjointness, positivity, or closability is no longer evidence that the arithmetic selector has been derived.

## 1. The unwanted rational-log grades are dense

The positive rationals are dense in `R_+`, and logarithm is a homeomorphism from `R_+` to `R`. Therefore

\[
\Gamma=\log\mathbb Q_+^\times
\]

is dense in `R`.

By contrast, `P` is locally finite. For every `R>0`, a point of `P cap [-R,R]` has the form `+- log(p^k)` with

\[
p^k\le e^R.
\]

There are only finitely many integers, hence only finitely many prime powers, below `e^R`. Thus every compact real interval meets `P` in finitely many points.

Removing a locally finite subset from a dense subset of the real line leaves a dense subset. Explicitly, let `I` be any nonempty open interval. Since `P cap I` is finite after shrinking to a bounded subinterval, choose a still smaller open interval `J subset I` avoiding those finitely many prime-power points. Density of `Gamma` gives `gamma in Gamma cap J`, and then automatically `gamma notin P`. Therefore

\[
\boxed{\overline{\Gamma\setminus\mathcal P}=\mathbb R.}
\tag{1}
\]

This uses only the rational multiplicative grading already present in the Bost--Connes dynamics. No zeta zero data, explicit formula, or RH-equivalent condition enters.

## 2. Continuous physical-time calculus cannot be a Mangoldt support selector

Let

\[
F:\mathbb R\to\mathbb C
\]

be continuous and suppose it is intended to act grade-by-grade through the physical time energy `E=log q`. To create exact finite Weil support from a source that has nonzero components on all unwanted rational grades, the multiplier must satisfy

\[
F(\gamma)=0
\qquad(\gamma\in\Gamma\setminus\mathcal P).
\tag{2}
\]

By (1), the zero set in (2) is dense. Continuity therefore gives

\[
\boxed{F(x)=0\quad\text{for every }x\in\mathbb R.}
\tag{3}
\]

In particular `F` also vanishes at every prime-power energy. There is no continuous scalar filter whose meaning is “delete every non-prime-power rational grade but retain the prime-power grades.”

The statement is independent of sign. Requiring `F>=0` because `F(H)` is to define a positive energy only narrows the class further. It is also independent of boundedness: an unbounded continuous function still satisfies (3).

This places a broad family of natural operator constructions on one side of the boundary. Functions obtained from heat/Markov semigroups, resolvents, smooth or holomorphic functional calculus, complete Bernstein functions, operator-monotone functions, and finite algebraic combinations of such regular spectral responses are continuous on their finite domain. None can manufacture the selector from the full rational-log grading.

The claim is deliberately about **creating support**. If a source observable or cohomological object has already annihilated all unwanted grades, then a continuous multiplier may act on the surviving prime-power sector. In that case, however, the arithmetic selector has been supplied upstream and must itself pass the Mathia canonicality and positivity audit.

## 3. Uniform suppression has the same obstruction

The density argument has a useful stable form. Suppose

\[
|F(\gamma)|\le\varepsilon
\qquad
(\gamma\in\Gamma\setminus\mathcal P).
\tag{4}
\]

For any `x in R`, take a sequence `gamma_j in Gamma\setminus P` with `gamma_j->x`. Continuity gives

\[
|F(x)|
=\lim_{j\to\infty}|F(\gamma_j)|
\le\varepsilon.
\tag{5}
\]

Hence

\[
\boxed{\sup_{x\in\mathbb R}|F(x)|\le\varepsilon.}
\tag{6}
\]

So there is no sequence of continuous filters which, at a fixed stage, uniformly makes every unwanted rational grade small while retaining an order-one response on a desired prime-power grade. An exact selector can arise from regular filters only through a **non-uniform singular limit** whose transition regions collapse onto the prescribed prime-power set.

This distinction is important. Strong spectral limits of continuous positive functions can converge to Borel projections; the theorem does not deny that standard fact. It says that such a limit is genuinely singular in the energy topology and cannot be mistaken for an ordinary regular functional-calculus consequence of the Bost--Connes Hamiltonian.

## 4. Borel spectral calculus makes the selector trivial rather than canonical

The prime-power set `P` is countable and locally finite, hence closed and Borel. Standard Borel functional calculus for a self-adjoint generator `H` therefore permits

\[
P_{\rm pp}:=\mathbf1_{\mathcal P}(H),
\tag{7}
\]

an orthogonal spectral projection. This is positive and bounded.

One can also insert the Mangoldt scale itself. Define the nonnegative Borel function

\[
M_\Lambda(E)
=
\sum_{p}\sum_{k\ge1}
(\log p)
\mathbf1_{\{k\log p,-k\log p\}}(E).
\tag{8}
\]

Local finiteness makes (8) a well-defined finite-valued Borel function at every finite `E`, though it is unbounded as `|E|->infinity`. The spectral theorem produces the positive self-adjoint operator

\[
M_\Lambda(H)
\tag{9}
\]

with its standard closed quadratic form

\[
Q_\Lambda(\xi)
=\|M_\Lambda(H)^{1/2}\xi\|^2.
\tag{10}
\]

Equations (7)--(10) show why **closability is not, by itself, the missing theorem** in the unbounded escape left by `WP-209`--`WP-212`. If the desired arithmetic set and weights are supplied as a Borel symbol, positivity and closedness come for free from the spectral theorem.

The matched control is fatal to interpreting this as Mathia-native geometry. Let `S subset R` be any locally finite set unrelated to the primes and let `a:S->[0,infinity)` be arbitrary. Then

\[
M_{S,a}(E)
=\begin{cases}
a(E),&E\in S,\\0,&E\notin S\end{cases}
\]

is equally Borel and equally gives a positive self-adjoint multiplier `M_{S,a}(H)` with a closed positive form. The spectral theorem cannot distinguish the Mangoldt choice from a random, composite-only, or hand-designed control choice. The arithmetic content resides entirely in the symbol.

Therefore a proposal of the form “choose the positive spectral projection onto prime powers” or “take the closed positive multiplier with value `Lambda` on the arithmetic spectrum” is not a derivation. It is a repackaging of the target data.

## 5. Relation to the existing Mathia boundary

This result complements rather than duplicates the nearby findings.

`WP-209` proves that the critical KMS midpoint canonically supplies `q^{-1/2}` but a bounded correlation vector cannot carry the all-prime Mangoldt mass. `WP-211` shows that Duhamel/Bogoliubov averaging has a strictly positive logarithmic-mean multiplier, so it preserves unwanted spectral support. `WP-212` shows the inverse Kubo--Mori metric is also support-preserving and requires even worse underlying bounded mass.

The present finding removes a possible response to those support statements: replacing the specific canonical multipliers by a more general **continuous** time-energy filter cannot create the missing selector either. The obstruction is not that the Duhamel or inverse-BKM functions happened to be strictly positive; it is that non-prime-power rational grades are dense in the physical energy variable.

`WP-098` addresses a different category. It proves that the exact first-order Fourier projector on the prime torus, which deletes mixed-prime characters while preserving coordinate characters, is not an order-positive map and that positive unital same-algebra quotients cannot perform that deletion. Here the input is instead a **scalar function of the one-parameter physical time generator**. The new obstruction is continuity in the dense rational-log energy topology, and the Borel escape is an ordinary Hilbert spectral projection whose positivity says nothing about positivity preservation on the observable algebra.

There is no contradiction between the two. An orthogonal spectral projection may be a positive Hilbert-space operator while the corresponding grade-deletion map on observables fails to preserve the order cone. `WP-098` already warns against conflating those notions.

## 6. Aggressive falsification and exact scope

**Could a discontinuous spectral multiplier select prime powers?** Yes. Equations (7)--(10) exhibit it. This is why the finding is a regularity/canonicity boundary, not an impossibility theorem for all spectral calculus.

**Could a singular limit of continuous positive filters converge strongly to the prime-power projection?** Yes. Because `P` is closed, one can shrink positive continuous bumps around it and obtain the indicator pointwise, hence strongly under the spectral calculus in standard dominated settings. Such a construction must explain why the shrinking neighborhoods of exactly `P` are source-forced. Without that extra theorem it merely approximates an inserted Borel selector.

**Could the source observable already have prime-power support?** Yes. Then no selector is required from `F(H)`. But `WP-209`--`WP-212` show that the obvious bounded positive thermodynamic sources still face mass and weighting obstructions, and the upstream source must be audited independently rather than hidden in the functional calculus.

**Could a non-scalar operator or cross-grade coupling evade the density theorem?** Yes. A matrix/operator-valued construction can couple different grades before scalarization and need not reduce to `F(log q)`. That is precisely one of the live categories left by the accepted finite--archimedean incidence clue.

**Does the Borel projection give the finite Weil sign?** No. It only encodes support, and (8) can additionally encode Mangoldt amplitude. It supplies neither the conventional finite-term orientation nor the archimedean/polar counterterms nor a global sign theorem. Those remain the central mandate.

**Does the theorem depend on RH or zero data?** No. It is an elementary consequence of the Bost--Connes rational grading and the topology of the real energy line.

## 7. Prior-art and novelty boundary

No novelty is claimed for the Bost--Connes time evolution, its rational multiplicative grading, continuous or Borel functional calculus, the spectral theorem, or the von Mangoldt support of the explicit formula. The Bost--Connes system is already anchored in this line's `SOURCES.md` by Bost and Connes (1995).

A directed literature audit for Bost--Connes prime-power spectral projections, von-Mangoldt functional calculus, and prime-power filters found the classical system and arithmetic-thermodynamic discussions but no established theorem identifying a canonical continuous time-functional-calculus operation that produces the Mangoldt selector. That absence is not used as a novelty claim. The operator-theoretic facts used here are standard spectral theory.

The durable Mathia-specific delta is the exact three-way boundary created by combining the current `WP-209`--`WP-212` KMS carrier with the full rational-log grading:

\[
\boxed{
\text{continuous time-energy calculus}
\Rightarrow
\text{no nonzero prime-power selector};
}
\tag{11}
\]

\[
\boxed{
\text{Borel time-energy calculus}
\Rightarrow
\text{selector exists but can encode arbitrary target data};
}
\tag{12}
\]

and therefore

\[
\boxed{
\text{unbounded/closable scalar calculus alone}
\not\Rightarrow
\text{source-forced arithmetic geometry}.
}
\tag{13}
\]

This is not a reformulation of Weil positivity and does not supply an RH criterion.

## 8. Consequence for the research frontier

The surviving Bost--Connes route is now more specific. The phase boundary and KMS midpoint remain a rare source-forced origin of the critical half-density. But the missing Mangoldt selector cannot be obtained from any regular scalar function of the same physical time generator, while arbitrary Borel calculus makes the selector vacuous by allowing it to be inserted explicitly.

A productive next candidate must therefore add structure **before** the final scalar positive form: an intrinsic source object whose grade support is already arithmetic for an independent reason, a non-scalar coupling that mixes grades, a singular spectral projection selected by a source theorem rather than by the target set, or a genuinely global finite--archimedean/cohomological assembly. It must then still prove the global Weil sign independently.

That is a stricter boundary than “try an unbounded observable.” The unbounded object must now explain why its singularity and its arithmetic support are forced by Mathia geometry; otherwise positivity and closability are merely consequences of the spectral theorem applied to data that already contain the answer.