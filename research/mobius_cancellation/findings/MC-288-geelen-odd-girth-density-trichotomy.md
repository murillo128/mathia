# MC-288 — Geelen odd-girth rigidity collapses the collision-rich branch to affine obstruction or exponentially sparse occupancy

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the projected shell setup of `MC-281`, `MC-286`, and `MC-287`. Let

\[
S\subset \mathbf F_2^d
\]

be the set of distinct occupied projected Legendre-sign cells, write

\[
K=|S|,
\qquad
N=\sum_{s\in S} n_s,
\qquad
r=\dim_{\mathbf F_2}\langle S\rangle,
\]

and fix an odd target shell weight `t>=3`. Suppose the projected shell contains **no** exact `t`-element endpoint row and that the collision excess satisfies

\[
N-K\ge t-1.
\tag{1}
\]

Then exactly the finite geometry relevant to Geelen's geometric Andrásfai--Erdős--Sós theorem becomes available. The support `S` has no odd circuit of length at most `t`. Consequently one of the following two alternatives must hold:

\[
\boxed{\text{Affine obstruction: }0\notin\operatorname{aff}(S),}
\tag{2}
\]

or

\[
\boxed{
K\le (t+2)2^{r-t-1}.
}
\tag{3}
\]

Equivalently, on the non-affine branch the occupied support has density inside its **own linear span** at most

\[
\boxed{
\frac{K}{2^r}\le \frac{t+2}{2^{t+1}}.
}
\tag{4}
\]

Combining `(2)`--`(4)` with the collision-poor escape already isolated in `MC-287` gives the sharper deterministic trichotomy: every odd-weight endpoint-normalized empirical-Christoffel candidate with energy `<1` must satisfy at least one of

\[
\boxed{
N-K\le t-2,
}
\tag{5a}
\]

\[
\boxed{
0\notin\operatorname{aff}(S),
}
\tag{5b}
\]

or

\[
\boxed{
\frac{K}{2^r}\le \frac{t+2}{2^{t+1}}.
}
\tag{5c}
\]

The affine branch `(5b)` is not merely geometric terminology. By `MC-286`, it is equivalent to the existence of a nonzero linear functional `lambda` with

\[
\lambda(s)=1\qquad(s\in S),
\tag{6}
\]

so the corresponding generated quadratic product character is identically `-1` on every occupied shell prime. Thus the broad `K<=2^{d-1}` concentration branch left by `MC-287` has collapsed to either one exact constant-negative character obstruction or an exponentially sparse non-affine support.

At the live scale

\[
t=\left(\frac1{\log 2}+o(1)\right)\log\log y,
\tag{7}
\]

`(4)` becomes

\[
\frac{K}{2^r}\le (\log y)^{-1+o(1)}.
\tag{8}
\]

No Möbius summatory estimate, annihilator-triviality statement, or RH consequence follows. The result is a finite-geometric frontier refinement of the current shell-occupancy route.

## 1. Collision excess turns every short odd circuit into the forbidden target row

Let `B\subset S` be an odd zero-sum subset of odd cardinality `j<=t`. The exact pair-padding capacity of `MC-286` is

\[
P_B=\sum_{s\in S}\left\lfloor\frac{n_s-1_B(s)}2\right\rfloor.
\tag{9}
\]

The support-only lower bound proved in `MC-287` gives

\[
P_B\ge \left\lceil\frac{N-K-j}{2}\right\rceil.
\tag{10}
\]

Under `(1)`,

\[
N-K-j\ge t-1-j.
\]

Because both `t` and `j` are odd,

\[
\left\lceil\frac{t-1-j}{2}\right\rceil=\frac{t-j}{2},
\]

so `(10)` supplies at least `(t-j)/2` disjoint equal-cell pairs. Reserving one shell prime in each cell of `B` and adjoining those pairs produces `t` distinct shell primes whose projected product is the all-positive endpoint.

Therefore the assumed absence of a target row implies:

\[
\boxed{
S\text{ contains no odd zero-sum subset of size }\le t.
}
\tag{11}
\]

In particular `0\notin S`, and the simple binary matroid represented by the distinct nonzero vectors of `S` has no odd circuit of length at most `t`.

## 2. Geelen's sharp odd-girth theorem applies at `k=t+2`

Jim Geelen's geometric Andrásfai--Erdős--Sós theorem states that, for each odd integer `k>=5`, a simple rank-`r` binary matroid with no odd circuit of length less than `k` and

\[
|M|>k\,2^{r-k+1}
\tag{12}
\]

is a restriction of the rank-`r` binary affine geometry. The bound is sharp for `r>=k-1`.

Set

\[
k=t+2.
\tag{13}
\]

This is odd and at least five. Condition `(11)` says precisely that there is no odd circuit of length `<k`.

There is one small rank case to dispose of before invoking the theorem. If `r<=t` and `S` were non-affine, `MC-286` would give an odd zero-sum subset; taking an inclusion-minimal one gives an odd circuit of size at most `r+1`. Since `r+1<=t+1` and the circuit size is odd, it is at most `t`, contradicting `(11)`. Hence every non-affine surviving support has

\[
r\ge t+1=k-1,
\tag{14}
\]

which is exactly the rank range of Geelen's theorem.

If now

\[
K>(t+2)2^{r-t-1},
\tag{15}
\]

then `(12)` holds with `k=t+2`; Geelen's theorem makes the represented matroid affine. For a binary representation this means precisely that all columns lie in an affine hyperplane of their span, equivalently there exists a nonzero linear functional satisfying `(6)`. This is `(2)`.

Taking the contrapositive proves `(3)` and `(4)` on the non-affine branch.

## 3. This strictly refines the half-cube branch of `MC-287`

`MC-287` used only the elementary fact that more than half of `F_2^d` forces a three-term odd zero sum. Its necessary escape condition was

\[
K\le2^{d-1}
\quad\text{or}\quad
N-K\le t-2.
\tag{16}
\]

The first alternative mixed together two qualitatively different mechanisms:

1. true affine concentration, where every odd zero-sum is forbidden by one linear parity functional; and
2. non-affine supports whose density was simply too low for the half-cube lemma to say anything.

The Geelen theorem separates them. In the collision-rich regime `N-K>=t-1`, a non-affine support cannot occupy an arbitrary sub-half fraction. Its density in its own rank-`r` span is at most `(t+2)/2^{t+1}`, exponentially small in the target odd weight.

This is materially stronger than replacing ambient `d` by `r`: for growing `t`, the permitted non-affine density tends to zero. In particular, at the double-log support scale suggested by `MC-242`, the non-affine branch is only a `(log y)^{-1+o(1)}` fraction of its span.

The theorem is also sharp at the level of general binary matroids. Geelen constructs examples meeting the density threshold, so no purely finite-geometric argument using only odd girth and rank can replace `(4)` by an asymptotically smaller universal density without extra arithmetic structure from the actual Legendre shell.

## 4. Consequence for the arithmetic target

The current shell route now has three genuinely different escapes rather than one broad concentration alternative.

The **near-injective branch** `(5a)` is already expensive: `MC-287` shows that when `K` is close to the full shell size it forces roughly `log_2 y` effective pattern dimensions and primorial-scale coordinate conductor.

The **affine branch** `(5b)` is now an exact one-character problem. It asks whether a product of the used quadratic-coordinate characters can equal `-1` on every shell prime. This is a much narrower analytic target than arbitrary half-cube concentration.

The remaining **non-affine branch** `(5c)` must compress the shell image to exponentially small density in its own span while still maintaining enough multiplicity structure to avoid the target endpoint. Any future arithmetic occupancy theorem need not prove full cube coverage: it is enough to rule out this much weaker density collapse, while separate character-sum technology attacks `(5b)`.

That separation is the durable gain. `MC-284` showed full cube coverage only for moderate coordinate conductor; `MC-287` left half-cube concentration as the alternate escape. The present result says that beyond that moderate-conductor range the non-affine escape is not merely "at most half": it must become sparse at the scale `2^{-t}`.

## 5. Prior art and novelty audit

The decisive external theorem is established prior art: Jim Geelen, *A geometric version of the Andrásfai--Erdős--Sós Theorem*, Advances in Applied Mathematics 59 (2014), 1--7, DOI `10.1016/j.aam.2014.02.002`, arXiv `1401.5769`. Theorem 1.1 is exactly the implication used in `(12)`, including the sharp threshold and rank condition. The author's published PDF and arXiv record agree on the theorem statement.

The equivalence between a binary matroid being affine and having no odd circuit is classical binary-matroid theory and is also the finite-linear-algebra content already isolated in `MC-286`. The pair-padding inequality comes from `MC-287` and is elementary.

No novelty is claimed for Geelen's theorem, affine binary matroids, or the extremal density threshold. A targeted search found the theorem and later dense-binary-matroid work using the same critical-number/odd-circuit language, but not a separate statement formulated for this shell multiplicity problem. The Mathia contribution recorded here is only the exact composition of the classical odd-girth density theorem with the `MC-286` padding criterion and the `MC-281` endpoint-energy gate.

## Boundaries and falsification tests

- The collision hypothesis `(1)` is essential. Without enough repeated shell cells, a short odd circuit need not pad to the prescribed weight `t`.
- The theorem controls **distinct occupied cells**, not multiplicities. Very many shell primes may still concentrate on a sparse non-affine support.
- The rank in `(3)`--`(4)` is `r=dim span(S)`, not automatically the number `d` of available coordinate characters. Replacing `r` by `d` gives a weaker but valid bound only because `r<=d`.
- Affineness in `(2)` does not itself contradict the arithmetic shell. It identifies the exact constant-negative product-character obstruction that must be killed analytically.
- The non-affine density threshold is a general finite-geometric barrier and is sharp in that category. Arithmetic Legendre images may be much more rigid, but proving that requires new arithmetic input.
- At `t=(1/log 2+o(1))log log y`, `(8)` is only an asymptotic density statement; it does not by itself lower-bound `r` unless `K` is independently controlled from below.
- No use is made of RH, GRH, zeta zero-free regions, or reciprocal-zeta continuation.

## Consequence for the research line

The unresolved occupancy problem has become substantially more structured. To keep an odd-weight Christoffel certificate below unit energy, the actual Legendre shell must now do one of three things: encode almost every shell prime distinctly, satisfy one exact constant-negative quadratic character relation, or occupy only about a `2^{-t}` fraction of its own binary span. This gives the next arithmetic investigation a sharper target than generic half-cube concentration and prevents further work from treating all sparse-support escapes as one undifferentiated case.
