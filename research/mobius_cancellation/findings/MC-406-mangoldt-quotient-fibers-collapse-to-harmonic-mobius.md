# MC-406 — Mangoldt quotient fibers collapse to a harmonic Möbius kernel

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-IDENTITIES` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-405` showed that the exact retained-source identity

\[
\sum_{n\le x}\mu(n)\log n
=-\sum_{b\le x}\Lambda(b)M(\lfloor x/b\rfloor)
\tag{1}
\]

genuinely keeps a quotient variable but still self-couples to the Mertens function. There is a sharper representation-level diagnosis.

For an integer `x>=1`, group source labels `b` by the quotient

\[
k=\left\lfloor\frac{x}{b}\right\rfloor .
\]

If

\[
\psi(y):=\sum_{n\le y}\Lambda(n),
\]

then the exact weight of quotient fiber `k` is

\[
W_k(x)
:=\sum_{\substack{b\le x\\ \lfloor x/b\rfloor=k}}\Lambda(b)
=\psi(x/k)-\psi(x/(k+1)).
\tag{2}
\]

Hence

\[
\boxed{
\sum_{b\le x}\Lambda(b)M(\lfloor x/b\rfloor)
=
\sum_{k=1}^{x}M(k)W_k(x).
}
\tag{3}
\]

So once the downstream observable is only `M(floor(x/b))`, the individual source label `b` is no longer retained: all `b` in the same floor-quotient fiber are compressed to one scalar `W_k(x)`. The map has at most `2 floor(sqrt(x))` distinct quotient values. Source-variable retention in `(1)` is therefore real but only up to this canonical hyperbola quotient.

Now split

\[
\psi(y)=y+E(y),
\qquad E(y):=\psi(y)-y.
\]

Then `(2)` gives the exact decomposition

\[
W_k(x)
=
\frac{x}{k(k+1)}
+
E(x/k)-E(x/(k+1)),
\tag{4}
\]

and therefore

\[
\boxed{
\sum_{b\le x}\Lambda(b)M(\lfloor x/b\rfloor)
=
x\left(m(x)-\frac{M(x)}{x+1}\right)
+
\sum_{k=1}^{x}M(k)
\bigl(E(x/k)-E(x/(k+1))\bigr),
}
\tag{5}
\]

where

\[
m(x):=\sum_{n\le x}\frac{\mu(n)}{n}.
\]

The first term in `(5)` is not a new source-side cancellation mechanism. It follows from the exact identity

\[
\boxed{
\sum_{k=1}^{K}\frac{M(k)}{k(k+1)}
=
\sum_{n\le K}\frac{\mu(n)}{n}
-
\frac{M(K)}{K+1}.
}
\tag{6}
\]

Thus the **PNT main component of the Mangoldt quotient fibers collapses exactly to classical harmonic Möbius cancellation**. Any extra leverage available to a method that keeps only quotient-fiber totals must come from the error increments

\[
E(x/k)-E(x/(k+1)),
\]

or from additional structure retained before the `b -> floor(x/b)` compression.

There is also an immediate scale warning. The first quotient fiber is

\[
W_1(x)=\psi(x)-\psi(x/2)=\frac{x}{2}+o(x)
\tag{7}
\]

by the prime number theorem, and it is multiplied by `M(1)=1`. Therefore even the `k=1` fiber already contributes positive linear mass. A sublinear total in `(3)` necessarily requires large cancellation across quotient fibers. Bounding fibers independently, or applying Cauchy/triangle estimates after this compression without an additional signed relation, cannot explain the desired power saving.

No bound for `M(x)` is improved here. The result refines the live retained-variable branch: **quotient survival alone is insufficient, and quotient-fiber aggregation already compresses the Mangoldt source to a positive harmonic main kernel plus prime-counting fluctuations.**

## 1. Exact quotient-fiber factorization

For every positive integer `k`,

\[
\left\lfloor\frac{x}{b}\right\rfloor=k
\quad\Longleftrightarrow\quad
\frac{x}{k+1}<b\le\frac{x}{k}.
\tag{8}
\]

Summing `Lambda(b)` over `(8)` proves `(2)`. Since `M(floor(x/b))=M(k)` is constant on the same fiber, summing `(1)` by fibers gives `(3)`.

This identifies the representation actually seen by the aggregate transform:

- **encoding:** the prime-power source labels `b` with weights `Lambda(b)`;
- **downstream quotient coordinate:** `k=floor(x/b)`;
- **retained source statistic inside each fiber:** only its total Mangoldt mass `W_k(x)`;
- **target estimator:** the signed pairing `sum_k M(k)W_k(x)`.

Two different arrangements of source weight inside one fiber are indistinguishable to `(3)`. The representation is therefore strictly coarser than the original `b`-labeled family even though it is finer than the lcm-only incidence algebra ruled out by `MC-404`.

## 2. Only square-root many quotient coordinates survive

Let `r=floor(sqrt(x))`. If `b<=r`, there are at most `r` source labels and hence at most `r` quotient values. If `b>r`, then

\[
\left\lfloor\frac{x}{b}\right\rfloor<\frac{x}{r}\le r+1,
\]

so these labels contribute at most `r+1` small quotient values. In particular the number of distinct values of `floor(x/b)` is `O(sqrt(x))`, with the standard elementary bound `<=2 floor(sqrt(x))+1` sufficient here.

This familiar Dirichlet-hyperbola compression is useful as a representation audit, not as an analytic estimate. Reducing `x` source labels to `O(sqrt(x))` fibers does not imply square-root cancellation because the retained weights are highly nonuniform and the first few fibers have macroscopic mass.

## 3. The PNT main kernel is harmonic Möbius cancellation

Insert `psi(y)=y+E(y)` into `(2)`. The deterministic main term is

\[
\frac{x}{k}-\frac{x}{k+1}
=
\frac{x}{k(k+1)},
\]

which proves `(4)`.

To identify its signed pairing, expand `M(k)` and interchange two finite sums:

\[
\begin{aligned}
\sum_{k=1}^{K}\frac{M(k)}{k(k+1)}
&=
\sum_{k=1}^{K}\frac{1}{k(k+1)}
\sum_{n\le k}\mu(n)\\
&=
\sum_{n\le K}\mu(n)
\sum_{k=n}^{K}\frac{1}{k(k+1)}\\
&=
\sum_{n\le K}\mu(n)
\left(\frac1n-\frac1{K+1}\right)\\
&=
m(K)-\frac{M(K)}{K+1}.
\end{aligned}
\tag{9}
\]

This is `(6)`. Taking `K=x` in `(4)` and `(9)` gives `(5)` exactly. No analytic continuation, reciprocal-zeta continuation, contour shift, or zero-free region is used in this derivation.

The prime number theorem is classically equivalent to `M(x)=o(x)` and implies `m(x)->0`; it is also equivalent to `psi(x)~x`. Consequently the leading harmonic kernel in `(5)` is only a PNT-scale cancellation carrier. Treating it as a new route to RH would merely move a classical Möbius cancellation problem into quotient coordinates.

## 4. A linear endpoint fiber forces cross-fiber cancellation

For `k=1`, `(2)` is

\[
W_1(x)=\psi(x)-\psi(x/2).
\]

The PNT gives `(7)`. Since `M(1)=1`, the `k=1` summand of `(3)` alone is asymptotic to `x/2`.

More generally, for any fixed `k`, the PNT gives

\[
W_k(x)
\sim
\frac{x}{k(k+1)}.
\tag{10}
\]

The large positive source masses therefore do not become small merely because the quotient representation has only `O(sqrt(x))` coordinates. The small final value forced by `(1)` arises from signed cancellation among the `M(k)` factors across scales.

This complements the triangle-inequality obstruction in `MC-405`. There the full unsigned coefficient mass destroyed every fixed sublinear input exponent. Here the obstruction is localized: even a single macroscopic quotient fiber must be cancelled by other fibers, while the aggregate PNT main kernel is exactly the weighted Möbius sum `(6)`.

## 5. What information could still escape the collapse

Equation `(5)` does not rule out quotient methods. It separates two possible places where genuinely additional information can live.

First, a method may exploit the prime-distribution fluctuation increments

\[
E(x/k)-E(x/(k+1))
\]

jointly with `M(k)`. Such a result would need an independently controlled signed relation between Mertens values and prime-counting errors; applying absolute values simply replaces one cancellation problem by two difficult factors.

Second, a method may retain structure **inside** a quotient fiber before summing the source weights to `W_k(x)`: phases, congruence labels, another source coordinate, or an off-diagonal relation that distinguishes two `b` values with the same `floor(x/b)`. Such a construction would genuinely lie outside the representation tested here.

The boundary is therefore sharper than “retain a quotient variable.” A candidate must specify what discriminator survives the canonical floor-quotient fibers and why that discriminator supports a signed estimator rather than merely increasing notation.

## 6. Prior art and novelty boundary

All mathematical ingredients used above are classical or elementary:

- grouping by `floor(x/n)` is standard Dirichlet-hyperbola bookkeeping and underlies sublinear summatory-function algorithms;
- `psi(x)~x` and `M(x)=o(x)` are standard equivalent forms of the prime number theorem;
- harmonic Möbius sums `m(x)=sum_{n<=x} mu(n)/n` and their relation to PNT are classical;
- Möbius--Mangoldt convolution identities and Selberg/Apostol inversion formulae already provide many exact quotient self-couplings.

A targeted literature search on 20 September 2026 found these ingredients in standard PNT/Möbius sources, Apostol-style Selberg inversion, and modern work on summing `mu(n)`, but did not motivate treating `(2)`--`(6)` as a new theorem family. **No novelty is claimed for any displayed identity or asymptotic.** The durable contribution is only the Mathia frontier diagnostic: MC-405's retained Mangoldt source factors through `O(sqrt(x))` floor-quotient fibers; its PNT main component is exactly harmonic Möbius cancellation; and any extra fiber-total leverage must enter through the prime-error increments in `(5)`.

## Boundaries and falsification tests

- **Not an impossibility theorem for quotient methods.** A candidate that retains `b`-dependent data inside fibers, or proves a new signed relation involving the `E` increments, is outside this obstruction.
- **The `O(sqrt(x))` coordinate count is not an analytic gain.** Fiber weights are nonuniform and macroscopic near small `k`.
- **The endpoint fiber is not a lower bound for the total.** Its linear size demonstrates the cancellation obligation; other fibers can and do cancel it.
- **PNT is used only to interpret the main kernel and fixed-fiber masses.** Equations `(2)`--`(6)` are finite exact identities.
- **No circular RH input.** Nothing assumes a zero-free half-plane beyond what is already contained in the classical PNT statements used for interpretation.
- **Prime-error information remains live.** The remainder in `(5)` is not declared small enough for RH; controlling it is a separate arithmetic problem.
- **Fiber-total methods only.** This finding does not address representations that retain phases, congruences, tuple structure, or other labels before the Mangoldt weights are summed inside each quotient fiber.

## Consequence for the research line

The retained-variable branch now has three successive gates. `MC-404` shows that divisor-incidence algebra collapses to lcm fibers. `MC-405` supplies a canonical quotient variable that escapes that lcm collapse but proves that its full aggregate is an exact Mertens self-coupling and that absolute values destroy every fixed sublinear exponent. This finding adds the next representation gate: **after quotienting, the Mangoldt source itself collapses to floor-quotient fiber masses, whose PNT main kernel is exactly classical harmonic Möbius cancellation.**

Accordingly, the next useful candidate should not merely preserve `b`, `x/b`, or the total source mass in each hyperbola fiber. It should identify either a provably useful signed coupling to the prime-error increments in `(5)` or an intrinsic within-fiber discriminator that survives the `b -> floor(x/b)` compression and supports a non-tautological estimator.