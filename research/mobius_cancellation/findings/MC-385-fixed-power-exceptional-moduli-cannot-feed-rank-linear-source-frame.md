# MC-385 — Fixed-power exceptional-modulus counts cannot feed the rank-linear source frame

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the endpoint source-frame setup of `MC-374` and `MC-381`. Let

\[
W\le \mathbb F_2^R,
\qquad d:=\dim W,
\qquad H:=|W|=2^d,
\]

be any surviving endpoint-mode subspace, and for `I\in W` let `v_I` be the normalized prime-shell row of the corresponding primitive quadratic source character. Exact endpoint row constancy gives

\[
\operatorname{rank}G\le R,
\qquad
\operatorname{tr}G=H,
\qquad
G_{I,J}=\langle v_I,v_J\rangle,
\]

so

\[
\lambda_{\max}(G)\ge \frac HR.
\tag{1}
\]

Suppose a collective analytic theorem controls every nonzero pair-difference mode except a set `\mathcal E\subset W\setminus\{0\}` of size `E`, with

\[
|G_{I,J}|\le \varepsilon
\qquad\text{whenever }I+J\notin\mathcal E,
\tag{2}
\]

while no nontrivial estimate is available for differences in `\mathcal E`, so only `|G_{I,J}|\le1` is used there. Because pair differences on the additive group `W` form a Cayley pattern, every row has exactly `E` exceptional off-diagonal entries. Hence

\[
\boxed{
\lambda_{\max}(G)
\le 1+E+H\varepsilon.
}
\tag{3}
\]

Combining `(1)` and `(3)` gives the exact frame budget

\[
\boxed{
\frac HR\le 1+E+H\varepsilon.
}
\tag{4}
\]

Therefore a sufficient collective replacement for uniform single-character cancellation is

\[
\boxed{
E=o(H/R),
\qquad
\varepsilon=o(1/R).
}
\tag{5}
\]

This is strictly weaker than controlling every source mode: the frame can tolerate exponentially many bad characters when `H=2^{\Theta(R)}`. But it also shows exactly why a standard **fixed-power exceptional-modulus theorem** does not realize the collective escape left open after `MC-384`.

Under the trial source bound

\[
P\le y^A,
\tag{6}
\]

the fixed-power cutoff of `MC-381` gives, for fixed `\beta>0`,

\[
d\ge R-A/\beta,
\qquad
H\ge2^{R-A/\beta}.
\tag{7}
\]

Assume an almost-all-moduli theorem says that, among primitive characters with conductor at most `P`, every relevant character is good except those whose conductor belongs to an exceptional set of cardinality

\[
E(P)\ll P^\theta
\tag{8}
\]

for some fixed `\theta>0`. Distinct endpoint difference modes have distinct primitive quadratic characters and hence distinct primitive conductors in the present squarefree source dictionary, so count information alone gives at best

\[
E\le E(P)\ll y^{\theta A}.
\tag{9}
\]

To make `(9)` strong enough to guarantee the first condition in `(5)` from `(7)`, one needs

\[
y^{\theta A}
=o\!\left(\frac{2^{R-A/\beta}}R\right),
\tag{10}
\]

or equivalently

\[
\theta A\log y
+\frac{A}{\beta}\log2
+\log R
< R\log2-\omega(1).
\tag{11}
\]

For fixed `\theta,\beta`, `(11)` permits only

\[
\boxed{
A=O(R/\log y).
}
\tag{12}
\]

at the level of a worst-case certificate from the exceptional-set count. This is far below the already proved source-cost scale

\[
\frac{\log P}{\log y}
\gg \min\{R,\log\log y\}
\tag{13}
\]

from `MC-381`. In particular, no estimate of the form `(8)` with fixed positive `\theta` can by cardinality alone extend the current rank-linear branch. The obstruction persists even if one **grants for free** perfect cancellation on every nonexceptional character, all interval-to-prime transfer, and all theorem-admission conditions.

The issue is not that collective information is useless. Equation `(5)` identifies the useful theorem surface precisely: an exceptional-set theorem adapted to the actual source family must leave `o(H/R)` bad **difference modes**, not merely `O(P^\theta)` bad ambient moduli. Equivalently, it must exploit the exponentially structured endpoint family rather than measure exceptional volume against the full conductor interval `[1,P]`.

No estimate for `M(x)` and no RH consequence follows.

## 1. The endpoint Gram matrix is a Cayley frame

For `I,J\in W`, multiplication of the quadratic characters gives

\[
\chi_I\chi_J=\chi_{I+J}.
\tag{14}
\]

Consequently the normalized shell correlation between rows `I` and `J` depends only on the difference `I+J`. In particular, if `\mathcal E` is the set of difference modes for which the analytic estimate is unavailable, then for every fixed row `I` the exceptional neighbors are exactly

\[
\{I+K:K\in\mathcal E\}.
\tag{15}
\]

Translation on `W` is bijective, so every row has exactly `E=|\mathcal E|` such neighbors. The diagonal contributes `1`; every exceptional off-diagonal entry has absolute value at most `1`; and all remaining entries have absolute value at most `\varepsilon`. Therefore the maximum absolute row sum is at most

\[
1+E+(H-1-E)\varepsilon
\le1+E+H\varepsilon.
\tag{16}
\]

Since `G` is Hermitian,

\[
\lambda_{\max}(G)\le\|G\|_{\infty}
\le1+E+H\varepsilon,
\]

which is `(3)`.

On the other hand, exact endpoint constancy places every row in the `R`-dimensional space of functions constant on the `R` defect cells. Thus `rank(G)<=R`; every normalized row has squared norm one, so `tr(G)=H`; and positivity gives `(1)`. No character-sum theorem enters this lower bound.

This calculation sharpens the phrase “a collective theorem could avoid uniform single-character control” left in `MC-384`: the allowed exceptional mass is not qualitative. At the frame level it is naturally measured against `H/R`.

## 2. Source cutoff converts an ambient exceptional count into a rank budget

Under `(6)`, `MC-381` deletes source primes above the fixed shell power `y^beta`. There are at most `A/beta` such primes, hence the annihilator subspace satisfies `(7)`.

Every nonzero element of `W` gives a distinct endpoint character. In the current primitive quadratic squarefree source dictionary, two distinct modes cannot share the same primitive conductor while defining different primitive quadratic characters: the primitive real quadratic character is determined by its conductor/discriminant data. Thus an ambient theorem that declares at most `E(P)` conductors exceptional can make at most `E(P)` of the source difference modes exceptional.

This injectivity is favorable to the almost-all route; no multiplicity loss is charged. Nevertheless, substituting the fixed-power count `(8)` and the lower bound `(7)` into the required frame budget `E=o(H/R)` gives `(10)`--`(11)`.

The leading terms in `(11)` are `theta A log y` on the ambient-exception side and `R log 2` on the endpoint-family side. The source-codimension term `(A/beta)log2` only makes the constraint stronger. Therefore, for fixed positive `theta`, the count can certify the needed sparsity only while

\[
A\lesssim \frac{\log2}{\theta}\frac R{\log y},
\]

up to lower-order terms. This is `(12)`.

The conclusion is deliberately one-way. Failure of `(11)` does **not** mean that the actual exceptional set intersects the endpoint family heavily. It means that the ambient cardinality theorem `(8)` alone gives no certificate preventing all endpoint source conductors from lying inside its exceptional set.

## 3. Concrete prior-art audit: arbitrarily small fixed exceptional exponents are still the wrong scale

A close theorem shape appears in Oleksiy Klurman, Igor E. Shparlinski and Joni Teräväinen, *On Artin's conjecture on average and short character sums*, Bulletin of the London Mathematical Society **57** (2025), 2429--2443, DOI `10.1112/blms.70103`, arXiv:`2412.13355`.

Their Theorem 1.2 proves strong short-character-sum cancellation simultaneously for all primitive characters modulo every `q<=x` outside `O(x^{0.49})` exceptional natural moduli, in an explicit short-length range. Remark 1.4 states that, after changing the length constant by a large **fixed** factor `K`, the exceptional count can be reduced to

\[
O(x^{c/K})
\tag{17}
\]

for an absolute `c>0`. Thus the exceptional exponent can be made arbitrarily small but remains a fixed positive power for each fixed theorem choice.

For the present audit, grant much more than that theorem actually states: set the ambient modulus parameter to `x=P`, pretend every nonexceptional modulus supplies the exact prime-shell correlation bound required by `(2)`, and even set `\varepsilon=0`. Equation `(17)` still has the shape `(8)` with `\theta=c/K>0`, so `(10)` forces the same `A=O(R/log y)` certificate horizon. The obstruction therefore comes from **ambient exceptional volume**, not from the quality of the character-sum saving, the passage from integer intervals to shell primes, or the paper's admission condition.

This does not criticize the Klurman--Shparlinski--Teräväinen theorem; its exceptional set is highly effective for its intended averaging problem. It shows only that the current endpoint source frame asks a different question: whether a very thin, exponentially parameterized arithmetic family can be prevented from concentrating entirely inside an ambient exceptional set.

The generic row-sum estimate `(3)` is elementary linear algebra on a Cayley Gram matrix, and the comparison `(10)`--`(12)` is elementary exponent bookkeeping. No novelty is claimed for almost-all character-sum methods, exceptional-set counting, Gershgorin/row-sum norm bounds, or the cited theorem. A targeted search through 19 September 2026 found no theorem giving the source-family-specific `o(H/R)` exceptional-difference control required by `(5)`; absence from that search is not evidence of novelty.

## 4. Relation to earlier Mathia obstructions

This result is not the same as `MC-223` or `MC-263`.

`MC-223` concerns the first square-defect shell, where only polylogarithmically many character sectors are averaged and one fixed-power bad sector already exceeds the Möbius square-root budget. Here the endpoint family has `H=2^{Theta(R)}` rows, so many bad characters are tolerable; the exact admissible count is `o(H/R)`.

`MC-263` concerns zero-versus-nonzero detection of an exact quadratic blind relation by a scalar second moment over shell subsets. There one isolated blind codeword can be invisible to an almost-all balance statement. Here the objective is instead the **rank contradiction for a source-character frame**: isolated exceptions are harmless, and only the regular bad-difference degree matters.

`MC-383` rules out a different collective theorem shape whose error contains a fixed positive power of one global modulus. `MC-384` then shows that Chang's factorization-sensitive single-character theorem has an admission condition that itself stops at the `log log` conductor horizon. The present finding isolates a third collective failure mode: excellent estimates for nonexceptional moduli still do not help when the theorem measures exceptions by a fixed positive power of the ambient conductor range.

These distinctions matter for the frontier. The surviving target is not “an almost-all character-sum theorem” in the usual ambient sense. It is a theorem aligned to the **endpoint difference family** or another mechanism that couples bad modes strongly enough to keep their Cayley degree below `H/R`.

## Boundaries and falsification tests

- **Certificate barrier, not impossibility theorem.** Equation `(12)` limits what follows from the count `E(P)<<P^theta` alone. A theorem proving that the exceptional moduli avoid the structured source conductors can evade it even with the same global count.
- **Difference-family structure is essential.** The regular degree `E` in `(16)` uses that the rows are indexed by a subspace `W` and pair correlations depend on `I+J`. For an arbitrary family the bad-neighbor degree, not the total exceptional count, is the correct quantity.
- **Distinct primitive source characters are load-bearing.** If a future source dictionary admits many endpoint modes with the same conductor but different relevant objects, the conductor-count translation must be redone. The current primitive quadratic squarefree setting has the needed injectivity.
- **The theorem may leave many exceptions.** Uniform cancellation is stronger than necessary. Any future source-adapted result with `E=o(H/R)` and `epsilon=o(1/R)` is enough for the frame contradiction, even if `E` tends to infinity exponentially.
- **No claim about actual KST exceptions is made.** Their theorem gives an upper bound for an ambient exceptional set; it does not say source conductors are exceptional, nor is its interval estimate asserted here to transfer automatically to the prime shell.
- **No new source-cost lower bound is obtained.** Since the fixed-power ambient exceptional count reaches only `(12)`, it is weaker than `MC-381`. The result narrows the theorem shape needed to improve the analytic branch.
- **No RH or Möbius global-cancellation input is used.** The claim is internal to the endpoint/source-frame obstruction program and implies no estimate for `M(x)`.

## Research consequence

After `MC-382`--`MC-384`, the collective escape can now be stated quantitatively. A useful replacement for uniform high-conductor character cancellation must either:

1. control all but `o(H/R)` **source difference modes** directly;
2. show that ambient exceptional moduli intersect the source-conductor image in only `o(H/R)` points;
3. exploit signed/operator cancellation among the bad differences so that their contribution to the Gram norm is `o(H/R)` despite a larger count; or
4. bypass the source frame entirely.

A theorem whose only exceptional-set information is `O(P^theta)` for fixed `theta>0`, however small, does not reach the current rank-linear source-cost frontier through cardinality alone.