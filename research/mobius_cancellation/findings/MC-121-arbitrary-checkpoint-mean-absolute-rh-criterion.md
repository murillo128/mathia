# MC-121 — Pintz's mean-absolute lower bound removes the checkpoint-density requirement

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `TARGET-REDUCTION`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad
D_M(Y)=\frac1Y\int_1^Y |M(x)|\,dx.
\]

A theorem of Pintz from 1987 gives a stronger scale statement than the monotone interpolation route isolated in `MC-116`. If

\[
\rho_0=\beta_0+i\gamma_0,
\qquad
\zeta(\rho_0)=0,
\qquad
\beta_0>\frac12,
\qquad
\gamma_0>0,
\]

then Pintz's Theorem A states

\[
\boxed{
D_M(Y)>\frac{Y^{\beta_0}}{\gamma_0^5}
\qquad (Y>\gamma_0^5).
}
\tag{1}
\]

(The paper integrates from `0`; with the standard convention `M(x)=0` for `0<x<1`, this is the same quantity.) In particular an off-critical zero forces excessive **mean-absolute mass at every sufficiently large scale**, not merely on a limsup sequence.

Consequently, for **any** sequence

\[
1<X_1<X_2<\cdots\to\infty,
\]

with no condition on the gaps,

\[
\boxed{
\mathrm{RH}
\iff
D_M(X_j)=O_\varepsilon(X_j^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\tag{2}
\]

Thus the `log X_(j+1)/log X_j -> 1` condition in `MC-116` is needed only for that finding's **zero-free interpolation through all intermediate physical scales**. It is not necessary if the sole target is RH itself and one is allowed to use Pintz's established zero-to-mean lower bound. Even power-lacunary, super-power-lacunary, or otherwise arbitrarily sparse unbounded checkpoints retain the RH endpoint.

Equivalently,

\[
\boxed{
\mathrm{RH}
\iff
\liminf_{Y\to\infty}
\frac{\log D_M(Y)}{\log Y}
\le \frac12.
}
\tag{3}
\]

This is a target reduction, not a new proof mechanism. The hard arithmetic problem remains to obtain square-root-scale control of `D_M` from information genuinely weaker than RH. What changes is that such control need not be produced on a dense scale mesh.

## 1. The finite-scale zero-exclusion wedge

Equation `(1)` immediately gives a quantitative finite-scale converse. Suppose for some `Y>gamma_0^5` one has

\[
D_M(Y)\le C Y^{1/2+\delta}.
\tag{4}
\]

Then any zero `rho_0=beta_0+i gamma_0` with `beta_0>1/2` must satisfy

\[
\frac{Y^{\beta_0}}{\gamma_0^5}
< C Y^{1/2+\delta},
\]

hence

\[
\boxed{
\beta_0
<
\frac12+\delta
+
\frac{\log C+5\log\gamma_0}{\log Y}.
}
\tag{5}
\]

Pintz states the `C=1`, `delta=0` specialization as Corollary A: if a zero lies to the right of

\[
\frac12+\frac{5\log|\gamma_0|}{\log Y},
\]

then `D_M(Y)>sqrt(Y)`.

The important feature for this line is the quantifier **for every `Y` beyond a zero-dependent fixed threshold**. The height penalty `gamma_0^5` is constant once a hypothetical zero is fixed, while an unbounded checkpoint sequence eventually passes it.

## 2. Arbitrary checkpoints prove RH

Assume that `(2)` holds along some arbitrary unbounded sequence `(X_j)` and suppose RH is false. By the functional equation and conjugation symmetry there is a nontrivial zero

\[
\rho_0=\beta_0+i\gamma_0
\]

with `beta_0>1/2` and `gamma_0>0`.

Choose

\[
0<\varepsilon<\beta_0-\frac12.
\]

The checkpoint hypothesis supplies a constant `C_epsilon` such that, for all sufficiently large `j`,

\[
D_M(X_j)\le C_\varepsilon X_j^{1/2+\varepsilon}.
\tag{6}
\]

For the same sufficiently large `j`, `X_j>gamma_0^5`, so Pintz gives

\[
D_M(X_j)>
\frac{X_j^{\beta_0}}{\gamma_0^5}.
\tag{7}
\]

Combining `(6)` and `(7)` would require

\[
X_j^{\beta_0-1/2-\varepsilon}
< C_\varepsilon\gamma_0^5,
\]

which is impossible as `j->infinity`. Therefore no off-critical zero exists and RH follows.

Conversely RH gives the classical pointwise Mertens estimate

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon}),
\]

so the same bound holds for `D_M(x)` at every scale and hence on every checkpoint sequence. This proves `(2)`.

No interpolation between checkpoints appears anywhere in this argument. In particular, if

\[
X_{j+1}=X_j^{100},
\qquad
X_j=\exp(\exp(j)),
\]

or the gaps grow even faster, the implication is unchanged.

## 3. The liminf formulation

If RH holds, the preceding pointwise upper bound gives

\[
\limsup_{Y\to\infty}\frac{\log D_M(Y)}{\log Y}\le\frac12,
\]

so the right-hand side of `(3)` follows.

If RH is false, fix any zero with `beta_0>1/2`. Equation `(1)` holds for every sufficiently large `Y`, and therefore

\[
\liminf_{Y\to\infty}
\frac{\log D_M(Y)}{\log Y}
\ge
\beta_0>\frac12.
\tag{8}
\]

This proves `(3)`. More generally, every fixed off-critical zero supplies its own lower bound in `(8)`; taking zeros arbitrarily close to the rightmost zero boundary strengthens the lower obstruction when such zeros exist. No assertion about equality with that boundary is needed here.

The liminf criterion is strictly a statement about the **actual Möbius mean**. It does not generalize to an arbitrary bounded-increment path or generic multiplicative comparator. That distinction is exactly why the balanced-block controls in `MC-117`--`MC-120` do not contradict it.

## 4. Relation to `MC-115`, `MC-116`, and the active transfer program

`MC-115` proves directly that a uniform family

\[
D_M(X)=O_\varepsilon(X^{1/2+\varepsilon})
\]

forces zero-freeness by absolute Mellin convergence. That route is self-contained but needs an all-scale upper bound before applying the transform.

`MC-116` showed how monotonicity of

\[
A(X)=\int_1^X|M(u)|\,du
\]

can manufacture such an all-scale bound from sampled estimates when

\[
\log X_{j+1}/\log X_j\to1.
\]

Its explicit exponent loss for power-lacunary checkpoints remains correct **for that interpolation mechanism**.

The present finding uses a different classical bridge. Pintz starts with a hypothetical off-critical zero and proves that it forces a lower bound for `D_M(Y)` at every sufficiently large `Y`. Therefore a square-root upper bound at even one unbounded family of checkpoints eventually collides directly with the zero. There is no need to fill the physical-scale gaps first.

This materially shrinks the output surface of the active mean-absolute transfer question. A source-natural argument may target

\[
D_M(X_j)=O_\varepsilon(X_j^{1/2+\varepsilon})
\]

on **any rigorously produced unbounded sequence of scales**. The sequence need not be subpower-dense. Of course this does not make the arithmetic estimate weaker in exponent: producing it at arbitrarily sparse scales for the actual Möbius function is already RH-strength by `(2)`.

## Prior art and novelty assessment

The primary source is János Pintz, *An effective disproof of the Mertens conjecture*, Astérisque 147--148 (1987), 325--333. Theorem A on p. 329 states `(1)` for every zero `beta_0+i gamma_0` with `beta_0>1/2`, without a simplicity hypothesis, and Corollary A on p. 330 gives the finite `sqrt(Y)` exclusion boundary used above. The scanned primary text is available from Numdam:

https://www.numdam.org/item/AST_1987__147-148__325_0/

A modern independent exposition is Daniel R. Johnston and Tim Trudgian, *A round of Pintz to celebrate oscillations in sums*, Analysis Mathematica (published 10 August 2026), DOI `10.1007/s10476-026-00181-1`, arXiv:2511.09978v4. Their introduction records the general Pintz mean-value framework for `D_M`, and their final remark explicitly recalls the 1987 bound `(1)`, noting that it applies to every off-critical zero without a simplicity assumption. Their paper also gives a separate explicit Landau--Pintz theorem for simple zeros.

The theorem, finite-scale inequality, and reverse arithmetic-to-zero philosophy are therefore established prior art. No novelty is claimed for them. The Mathia-derived content is the consequence relevant to the current research frontier: **the subpower-density condition previously attached to the sampled mean-absolute endpoint is unnecessary for RH itself**. A targeted search did not identify a separately named theorem packaging the arbitrary-checkpoint or liminf formulations `(2)`--`(3)`; absence of such a label is not treated as novelty evidence.

This result is independent of the still-audited 2026 Pintz preprint used in `MC-009` and `MC-037`. It relies on the 1987 theorem, whose printed proof supplies the finite lower bound directly. Thus failure or correction of the newer `MC-S19` theorem would not affect `(1)`--`(3)`.

## Boundaries and falsification tests

- This finding does not improve any unconditional upper bound for `D_M` or `M`.
- It does not derive a source-natural local-to-global transfer. It only reduces how many output scales such a transfer must control.
- The use of Pintz is deliberately on the **zero-to-arithmetic lower-bound side**. The checkpoint hypothesis itself contains no zero data, but the final RH implication is not the Mellin-only bridge of `MC-115`.
- `MC-116` is not false or obsolete: its monotone interpolation theorem still describes exactly what sampled first-moment information implies at intermediate physical scales without invoking a separate zero theorem.
- Generic comparators from `MC-117`--`MC-120` are not counterexamples. Pintz's theorem is specific to Möbius through its zeta/Mellin structure; those comparators do not inherit `(1)`.
- The theorem's `gamma_0^5` penalty is harmless for the asymptotic checkpoint criterion because `gamma_0` is fixed before `j->infinity`, but it matters substantially for finite computational use.
- A claim that a sparse local statistic proves RH still needs an actual theorem transferring that statistic to `D_M(X_j)` at square-root exponent. Merely selecting empirically favorable checkpoints is not evidence.

## Consequence for the line

The current mean-absolute program should no longer treat **scale density of the output `D_M` estimate** as a necessary gate. The surviving burden is information content, not physical-scale interpolation: find a Möbius-specific local, signed, bilinear, multiplicative, or multiscale statistic whose polynomial control forces an RH-scale first absolute mean on some unbounded sequence.

This makes the remaining obstruction chain sharper. `MC-117`--`MC-120` show that weak sub-`L^1` statistics can miss rare coherent excursions even after exact support, multiplicativity, finite-window scale continuity, and fixed-function recurrence are added. `MC-121` says that if a genuinely Möbius-specific mechanism ever upgrades such information all the way to `D_M` itself, it does **not** need to do so densely in scale. The decisive missing ingredient is therefore a source-specific recovery of first-moment amplitude, not an interpolation theorem for the final endpoint.