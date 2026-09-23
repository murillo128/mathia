# MC-483 — Well-factorable bracket width does not transfer the signed error

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-482` leaves a natural apparent repair: replace the ordinary two-sided beta-sieve bracket by upper/lower sieve weights with stronger factorization, and try to retain the translated-ratio phase instead of taking absolute values over the bracket gap. Well-factorable linear-sieve variants in the Iwaniec tradition make this a serious possibility to test.

The repair does **not** follow from factorability of the upper/lower bracket, or even from factorability of its pointwise width. The obstruction is exact and precedes any analytic estimate.

Let `A(n)` be the exact hard mask and suppose two real functions `B^-(n),B^+(n)` satisfy

\[
B^-(n)\le A(n)\le B^+(n).
\tag{1}
\]

Write

\[
B(n)=\frac{B^+(n)+B^-(n)}2,
\qquad
G(n)=B^+(n)-B^-(n)\ge0.
\tag{2}
\]

Then there is a uniquely determined selector on the set `G(n)>0`,

\[
\theta(n):=\frac{2(A(n)-B(n))}{G(n)},
\qquad |θ(n)|\le1,
\tag{3}
\]

and when `G(n)=0`, `(1)` forces `A(n)=B(n)`, so we may put `theta(n)=0`. Hence

\[
\boxed{
A(n)-B(n)=\frac12\theta(n)G(n),
\qquad |\theta(n)|\le1.
}
\tag{4}
\]

For the translated-ratio phase of the current pair-sieve source frame,

\[
K_h(n)=\chi(n+h)\overline{\chi(n)},
\]

the exact transfer error is therefore

\[
\boxed{
\sum_{n\in I}K_h(n)(A(n)-B(n))
=
\frac12\sum_{n\in I}K_h(n)\theta(n)G(n).
}
\tag{5}
\]

Equation `(5)` isolates the missing information. Even if `G` has a divisor-sum expansion with well-factorable, triply well-factorable, or otherwise strongly factorable **divisor coefficients**, multiplication by the source-dependent selector `theta(n)` does not preserve that divisor-coefficient representation. The phase-coupled object is `K_h theta G`, not `K_h G`.

If no independent information about `theta` is supplied, the bracket returns exactly to the phase-blind estimate used in `MC-482`:

\[
\left|
\sum_{n\in I}K_h(n)(A-B)(n)
\right|
\le
\frac12\sum_{n\in I}|K_h(n)|G(n)
\le
\frac12\sum_{n\in I}G(n).
\tag{6}
\]

Thus **making the bracket width well-factorable does not by itself evade the `MC-482` level-versus-accuracy tariff**. A valid phase-coupled repair must expose additional structure of the selector/error itself, or replace bracketing by an exact signed decomposition in which the retained factor variables survive before coefficientwise absolute values.

This is a proof-input obstruction, not a lower bound for the actual rough×rough discrepancy. The actual selector is highly non-arbitrary because it is determined by the exact pair-sieve mask. A successful argument may exploit that arithmetic structure. What `(4)`--`(6)` rule out is the inference

\[
\text{factorable upper/lower gap}
\Longrightarrow
\text{factorable signed replacement error}
\]

without a separate theorem about the selector.

## 1. The selector is exactly the information discarded by bracketing

The derivation is elementary but load-bearing. From `(1)` and `(2)`,

\[
-\frac{G(n)}2
\le
A(n)-B(n)
\le
\frac{G(n)}2,
\]

which gives `(3)`--`(4)` whenever `G(n)>0`. If `G(n)=0`, the two envelopes coincide and force `A(n)=B(n)`.

Moreover, given the bracket `B,G`, the selector reconstructs the hard mask exactly:

\[
A(n)=B(n)+\frac12\theta(n)G(n).
\tag{7}
\]

So `theta` is not a free cheap auxiliary variable created by the upper/lower sieve. Relative to a fixed bracket it is a re-encoding of precisely the residual hard-mask information that the bracket failed to determine. Any proposed gain from `theta` must therefore come from a proved structural theorem about this particular selector, not from the inequality `|theta|<=1` alone.

This also explains why strong factorization of `G` is insufficient. Suppose schematically

\[
G(n)=\sum_{d\mid n(n+h)}c_d
\tag{8}
\]

with `c_d` well-factorable in `d`. Inserting `(8)` into `(5)` gives

\[
\frac12
\sum_d c_d
\sum_{\substack{n\in I\\d\mid n(n+h)}}
K_h(n)\theta(n).
\tag{9}
\]

The inner source coefficient is now `K_h(n)theta(n)`. The factorability of `c_d` remains true, but it has not removed or represented the new `n`-dependent selector. Any dispersion/completion theorem that was useful for `K_h` alone must be reproved with this extra coefficient, or the selector must itself be decomposed before the factorable modulus structure becomes analytically useful.

## 2. Bracket-width information alone cannot encode phase cancellation

The loss is not specific to beta-sieve notation. Consider the abstract bracket

\[
B^-(n)=0,
\qquad
B^+(n)=1,
\]

so `B=1/2` and `G=1`. The same bracket permits every binary mask `A(n) in {0,1}`; equivalently it permits every selector `theta(n) in {-1,+1}`. For a real phase `K(n) in {-1,+1}`, choosing

\[
A(n)=\frac{1+K(n)}2
\]

gives `theta(n)=K(n)` and hence

\[
K(n)(A(n)-B(n))=\frac12
\]

pointwise. The bracket width is perfectly simple, but it contains no information preventing maximal phase alignment of the signed residual.

This example is **not** a model for the actual Möbius pair sieve. It proves only the information statement needed here: a theorem whose hypotheses see the upper/lower width and its factorability but do not see the selector cannot, on those hypotheses alone, infer cancellation of the signed replacement error. The arithmetic line must supply extra information specific to the exact roughness mask.

## 3. Relation to the two-sided beta-sieve route

`MC-482` constructs the midpoint of classical upper/lower beta-sieve divisor sums and obtains the independent pointwise transfer

\[
|A-B|\le G/2.
\]

It then sums `G` over the source interval by the fundamental lemma plus absolute interval remainders, producing

\[
H V_h(z)s^{-s/2}+D\log(2D),
\]

and shows that fixed conductor-power relative accuracy forces a polylogarithmic cutoff under that phase-blind bookkeeping.

A natural objection is that linear-sieve literature contains factorable modifications of sieve weights, so perhaps the `D log D` cost can be replaced by a dispersion estimate before absolute values. Iwaniec's factorable linear-sieve technology and Lichtman's modern exposition make that objection mathematically legitimate: factorization of sieve weights is a real analytic resource, not merely notation.

But `(5)` shows that a two-sided bracket introduces a second object before such a dispersion argument can start. Even granting a pointwise upper/lower bracket whose gap `G` enjoys the desired factorability, the **actual error** is `theta G/2`. A bound for the twisted sum with `G`, or a distribution theorem for the divisor coefficients defining `G`, is not a bound for the twisted sum with `theta G` unless the theorem is stable under that additional source multiplier or `theta` is itself understood.

Therefore the next viable factorable-sieve continuation is narrower than “use well-factorable upper/lower weights.” It must do one of the following:

- derive an exact signed divisor/factor decomposition of `A-B` itself;
- derive a nontrivial structural representation or correlation theorem for the exact selector `theta`;
- couple the hard mask to factor variables through a first-exit, Buchstab, dispersion, or reciprocity identity **before** it is replaced by a mere order bracket;
- move to the already-separated boundary/nonempty/cross-component channels where an exact signed decomposition survives.

Merely improving the factorability class of `B^+`, `B^-`, or `G` does not cross the transfer gate.

## 4. Prior art and novelty boundary

Henryk Iwaniec, *A new form of the error term in the linear sieve*, Acta Arithmetica 37 (1980), 307--320, DOI `10.4064/AA-37-1-307-320`, is the classical source for reorganizing linear-sieve errors into factorable forms.

Jared Duker Lichtman, *A modification of the linear sieve, and the count of twin primes*, Algebra & Number Theory 19 (2025), 1--38, DOI `10.2140/ANT.2025.19.1`, gives a modern explicit account of well-factorable linear-sieve weights and stronger factorization variants. Its notation includes Iwaniec-style well-factorable weights `\widetilde\lambda^{\pm}` and distinguishes these from the ordinary Rosser upper/lower weights. The paper also emphasizes that standard linear-sieve weights are not themselves automatically well-factorable; the factorable objects are constructed variants.

These sources establish that “repair the two-sided route using factorable sieve weights” is a natural prior-art-informed idea. They do **not** supply the Mathia transfer claimed here, and no novelty is claimed for factorable sieve weights, beta-sieve bracketing, midpoint bounds, or dispersion technology.

The durable Mathia contribution is the candidate-specific algebraic classification `(4)`--`(9)`: once an exact hard pair-sieve mask is replaced only by an order bracket, the signed replacement error acquires a selector which exactly carries the information not fixed by that bracket. Factorability of the bracket width alone therefore cannot be credited as factorability of the signed error. A targeted literature search on 23 September 2026 found the classical factorable-sieve constructions and applications, but no reason to identify this source-frame selector bookkeeping with a stronger known transfer theorem. Accordingly the finding is recorded as an exact obstruction with **no novelty claim**.

## Boundaries and falsification tests

- **Not a lower bound.** Equations `(4)`--`(6)` do not say the actual twisted replacement error is large. They say that the bracket and factorability of its width do not by themselves make it small.
- **Not a claim that `theta` is arbitrary for the pair sieve.** In the real target `theta` is fixed by `A,B^+,B^-`. The abstract binary example proves insufficiency of bracket-width information, not admissibility of every selector in the arithmetic problem.
- **A selector theorem would evade the obstruction.** Any exact formula, short expansion, correlation bound, first-exit rule, or bilinear representation for the actual `theta` that survives the translated-ratio phase would be genuinely new input and must be priced on its own terms.
- **An exact signed surrogate would evade the obstruction.** If one obtains `A-B` directly as a controlled signed factorable combination rather than via an order bracket, `(4)` is only an identity and no longer blocks the route.
- **Factorability is not being dismissed.** `MC-456` already records successful neighboring arguments where factor variables remain inside the arithmetic constraint through dispersion/completion. The present result says only that factorability attached to an upper/lower *width* does not automatically pass through the unknown signed residual.
- **No circular zeta input is used.** The argument is finite and algebraic.
- **No Möbius, Mertens, zero-free, or RH consequence follows.** This is a transfer obstruction inside one staged sieve component.

## Consequence for the research line

`MC-482` showed that a classical phase-blind upper/lower sandwich is independently priceable but quantitatively restricted to polylogarithmic cutoffs if it must deliver conductor-power accuracy on a polynomial short interval. `MC-483` closes the most immediate attempted repair: **strong factorization of the bracket gap is not yet phase-coupled factorization of the exact replacement error**, because the missing hard-mask information reappears as the source selector `theta`.

The live empty-vector question is therefore sharper. Either expose structure of that selector/error before positive bracketing, derive an exact signed first-exit/factorable representation, or leave the empty-vector bracket route and attack a boundary/nonempty/pre-positive cross-component channel. Repackaging the upper/lower gap into a stronger factorability class without addressing `theta` should not be counted as a new escape.