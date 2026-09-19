# MC-398 — Selberg divisor-pair retention collapses exactly to lcm fibers

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact source-signature/Selberg setup of `MC-397`. Let

\[
f(n)=\left(\sum_{d\mid n}g(d)\right)^2,
\qquad g(d)=0\quad(d>B),
\]

and for every positive integer `\ell` define the **lcm-fiber coefficient**

\[
\boxed{
C_g(\ell):=
\sum_{\substack{d_1,d_2\le B\\[d_1,d_2]=\ell}}
 g(d_1)g(d_2).
}
\tag{1}
\]

Then the quadratic Selberg weight has the exact one-variable divisor expansion

\[
\boxed{
f(n)=\sum_{\ell\mid n}C_g(\ell).}
\tag{2}
\]

Consequently, equation `(9)` of `MC-397`—which was the first candidate location for retaining the two Selberg divisor labels inside a Stadlmann-type Cauchy/`q`-van-der-Corput step—compresses identically to

\[
\boxed{
\sum_{\ell\le B^2} C_g(\ell)
\sum_{m\le N/\ell}
\mathbf 1_{(\ell m,P)=1}
\left|\widehat a\!\left(\Phi(\ell m)\right)\right|^2.
}
\tag{3}
\]

For the normalized uniform source vector this becomes

\[
\boxed{
H\sum_{\substack{\ell\le B^2\\(\ell,P)=1}} C_g(\ell)
\#\left\{
 m\le N/\ell:
 (m,P)=1,
 \Phi(m)=\Phi(\ell)^{-1}
\right\}.
}
\tag{4}
\]

Thus **the pair `(d_1,d_2)` in the already-squared Selberg majorant is not a surviving arithmetic averaging dimension**. Once the divisibility constraints are imposed, the arithmetic inner expression depends on the pair only through its least common multiple. Every pair in one lcm fiber carries exactly the same inner arithmetic object; all information specific to the pair is the scalar coefficient sum `(1)`.

This rules out the most literal remaining interpretation of the accepted averaged-`q`-vdC clue: one cannot obtain a Stadlmann-like diagonal thinning merely by refusing to sum the `(d_1,d_2)` labels in equation `(9)` of `MC-397`. Any gain that treats those labels as independent arithmetic samples but disappears after the exact regrouping `(1)`--`(3)` is representation-dependent bookkeeping, not a new cancellation resource.

The result **does not rule out the lcm variable `\ell` itself**, nor a genuinely different pre-quadratic/bilinear representation in which two divisor variables enter the arithmetic phase or congruence separately before the condition `d_1\mid n`, `d_2\mid n` has collapsed to `[d_1,d_2]\mid n`. It narrows the live retained-variable branch from

`source modes / Selberg divisor pairs / lcm / other shell variables`

to

`lcm or a genuinely arithmetic variable that survives before lcm compression`.

No estimate for `M(x)` follows.

## 1. Exact lcm compression of the quadratic majorant

Expand the square:

\[
\begin{aligned}
f(n)
&=\sum_{d_1\mid n}\sum_{d_2\mid n}g(d_1)g(d_2)\\
&=\sum_{d_1,d_2\le B}g(d_1)g(d_2)
\mathbf 1_{d_1\mid n}\mathbf 1_{d_2\mid n}.
\end{aligned}
\tag{5}
\]

But

\[
\mathbf 1_{d_1\mid n}\mathbf 1_{d_2\mid n}
=
\mathbf 1_{[d_1,d_2]\mid n}.
\tag{6}
\]

Grouping `(5)` by `\ell=[d_1,d_2]` proves `(2)` immediately. Notice that this is not an estimate: the map

\[
(d_1,d_2)\longmapsto[d_1,d_2]
\]

is a sufficient statistic for every occurrence of the divisor pair inside this quadratic weight.

Now insert the source-signature factor from `MC-397`. The exact expression there is

\[
\sum_{d_1,d_2\le B}g(d_1)g(d_2)
\sum_{m\le N/[d_1,d_2]}
\mathbf 1_{([d_1,d_2]m,P)=1}
\left|\widehat a\!\left(\Phi([d_1,d_2]m)\right)\right|^2.
\tag{7}
\]

For fixed `\ell`, the entire inner sum in `(7)` is identical for every divisor pair in the fiber `[d_1,d_2]=\ell`. Therefore regrouping by that fiber gives `(3)` with no loss and no change of hypotheses.

For the uniform source vector, `MC-397` gives

\[
|\widehat a(\Phi(n))|^2
=H\mathbf 1_{\Phi(n)=1}
\]

on `(n,P)=1`. Multiplicativity of `\Phi` then turns `(3)` into `(4)`.

## 2. Why keeping the pair labels cannot by itself change the diagonal geometry

Suppose one postpones the regrouping and applies Cauchy or a differencing inequality while `(d_1,d_2)` are still written explicitly. The fiber identity above gives a mandatory representation check.

For each fixed `\ell`, all pairs in

\[
\mathcal F_\ell
:=\{(d_1,d_2):d_i\le B,[d_1,d_2]=\ell\}
\]

multiply the **same** arithmetic quantity

\[
T(\ell)
:=
\sum_{m\le N/\ell}
\mathbf 1_{(\ell m,P)=1}
|\widehat a(\Phi(\ell m))|^2.
\]

Hence their total contribution is exactly

\[
\sum_{(d_1,d_2)\in\mathcal F_\ell}
 g(d_1)g(d_2)T(\ell)
=C_g(\ell)T(\ell).
\tag{8}
\]

There is no arithmetic phase, congruence, interval endpoint, source signature, or shell variable left that distinguishes two members of the same fiber. The pair multiplicity is therefore coefficient multiplicity, not sample multiplicity.

This provides a sharp falsification test for a proposed retained-pair argument. If a claimed saving arises because Cauchy counts `(d_1,d_2)` as separate observations even though the argument would be unchanged after replacing the full fiber by the single coefficient `C_g(\ell)`, then the saving is an artifact of the chosen expansion. A genuine Stadlmann-type gain must survive exact regrouping because the retained variable must alter the arithmetic diagonal itself.

The distinction is exactly the one exposed in `MC-397` for source modes. There the Fourier-dual source index collapsed to a signature projector. Here the Selberg divisor-pair labels collapse to an lcm coefficient. In both cases a formal high-dimensional index disappears under an exact representation change before any analytic estimate is needed.

## 3. Squarefree Selberg support makes the fiber structure especially explicit

In the usual squarefree Selberg setting, assume `g(d)` vanishes unless `d` is squarefree. Then `C_g(\ell)` also vanishes unless `\ell` is squarefree. For a squarefree `\ell`, each prime `p\mid\ell` has exactly three possible memberships inside a pair with lcm `\ell`:

- `p\mid d_1`, `p\nmid d_2`;
- `p\nmid d_1`, `p\mid d_2`;
- `p\mid d_1`, `p\mid d_2`.

Ignoring the individual cutoff `d_i\le B`, this is the classical `3^{\omega(\ell)}` lcm-fiber count; the cutoff only removes members of the fiber. Thus the familiar `3^{\omega(\ell)}` factors in Selberg-sieve remainder estimates are the combinatorial shadow of precisely the same compression.

If the coefficient system factorizes locally without a global cutoff, the lcm-fiber transform is itself local. For example, on squarefree support one has formally

\[
C_g(p)=2g(p)+g(p)^2
\tag{9}
\]

at one prime, and the global coefficient is obtained by multiplying these local lcm contributions. The standard finite-level cutoff can destroy literal multiplicativity of `C_g`, but it does not restore a second arithmetic variable: `(2)` and `(3)` remain exact.

This is useful for the present frontier because it distinguishes two questions that should not be conflated:

1. how complicated the **scalar lcm coefficient** `C_g(\ell)` is; and
2. whether the arithmetic inner sum indexed by `\ell` has enough structure for a new cancellation theorem.

Only the second can supply the retained arithmetic dimension sought by the clue.

## 4. What remains genuinely open

The lcm variable in `(3)` is real arithmetic data. It changes the interval length `N/\ell`, translates the source signature by `\Phi(\ell)`, and interacts with the coprimality constraint `(\ell,P)=1`. The present argument does not show that summing over `\ell` is useless.

A valid next step would have to keep `\ell` live inside a Cauchy/differencing argument and demonstrate an exact improvement in its diagonal count, together with an off-diagonal estimate that does not reintroduce either of the two known costs:

\[
2^{-\Omega(A)}
\]

from sequential conductor-depth differencing, or a fixed positive power

\[
P^\theta
\]

of the common source radical.

There is also a logically different escape: change the representation *before* the quadratic Selberg majorant has converted simultaneous divisibility into lcm divisibility. Such a representation must make two divisor/source variables enter an arithmetic phase, congruence, or translation separately. Merely preserving their names while the integrand factors through `[d_1,d_2]` does not do so.

This is now the decisive representation test for the surviving branch:

\[
\text{Does the candidate arithmetic object factor through }[d_1,d_2]?
\]

If yes, the pair labels are compressible to `C_g(\ell)` and cannot be credited as a second averaging dimension. If no, the non-factorization must be exhibited explicitly and shown to change the post-Cauchy diagonal geometry.

## Prior art and novelty boundary

The lcm dependence is classical Selberg-sieve structure. Standard presentations expand the square of a divisor sum into a quadratic form whose arithmetic coefficient depends on `[d_1,d_2]`; equivalently the two divisor labels may be collected into lcm-indexed coefficients. A targeted literature check on 19 September 2026 confirmed this explicitly in standard Selberg-sieve treatments, including the usual quadratic form

\[
\sum_{d_1,d_2}\lambda_{d_1}\lambda_{d_2}\,g([d_1,d_2])
\]

and the standard `3^{\omega(\ell)}` accounting of squarefree lcm fibers. No novelty is claimed for `(1)`, `(2)`, the lcm regrouping, or the combinatorial fiber count.

The Mathia-specific contribution is only a **frontier classification** after `MC-397`: applying the classical lcm compression to the exact source-signature expression shows that the already-squared Selberg divisor pair is not the missing Stadlmann-style retained variable. This narrows the accepted clue without asserting a new sieve theorem.

## Boundaries and falsification tests

- **The lcm variable remains open.** This finding kills only the independent use of the two pair labels after the standard quadratic Selberg expansion.
- **A different pre-quadratic representation is not covered.** If an arithmetic phase or congruence distinguishes `d_1` and `d_2` separately before simultaneous divisibility becomes lcm divisibility, the present compression does not apply.
- **No positivity is inferred for `C_g(\ell)`.** The original square is nonnegative as a whole, but the lcm coefficients may have either sign.
- **The individual cutoff matters only to the coefficient.** Restrictions `d_i\le B` change which pairs contribute to `C_g(\ell)` but do not create pair-dependent arithmetic inside `T(\ell)`.
- **Source-signature equidistribution remains unresolved.** Equation `(4)` still asks for arithmetic control of signature classes in intervals whose length varies with `\ell`.
- **Cauchy cannot manufacture an intrinsic dimension.** Any gain obtained only before the exact fiber regrouping must be rechecked after `(8)`; failure of that representation-invariance test is a no-go for the claimed mechanism.
- **No analytic continuation or zero-free region is used.** The result is finite divisor algebra plus the already-established source-signature representation.
- **No Möbius or RH conclusion.** The result only removes one bookkeeping interpretation of the retained-variable route.

## Consequence for the research line

`MC-397` showed that source-mode averaging is an exact Fourier projector rather than a free arithmetic average. The present result performs the next compression: the divisor-pair labels in the standard squared Selberg majorant are exactly lcm fibers. Therefore the accepted retained-variable clue should no longer spend effort on treating `(d_1,d_2)` from equation `(9)` as two independent arithmetic directions.

The live target is now more specific: **either the single lcm/shell variable must change the Cauchy/`q`-vdC diagonal geometry, or the construction must expose a genuinely non-lcm-factorable arithmetic variable before quadratic compression.**