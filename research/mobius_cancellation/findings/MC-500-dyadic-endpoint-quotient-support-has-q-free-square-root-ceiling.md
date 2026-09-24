# MC-500 — Dyadic endpoint quotient support has a Q-free square-root ceiling

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-FLOOR-QUOTIENT+DERIVED` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-499` shows that the endpoint-dispersion certificate can fail before any coefficient audit because one repeated conductor residue contains only `O(1+Q/p)` labels in a dyadic block `Q<=q<=2Q`. There is an opposite source-cardinality constraint when `Q` is large: the physical endpoint quotient `ceil(Z/q)` has only `O(1+Z/Q)` possible values on that block. Combining the two gives a `Q`-free ceiling on the effective physical-start population.

Fix an odd prime conductor `p`, one repeated residue `a mod p`, a dyadic label range

\[
Q\le q,r\le2Q,
\qquad q\equiv r\equiv a\pmod p,
\tag{1}
\]

and positive source endpoints `X` and `X+h`. Define

\[
u_q=\left\lceil\frac Xq\right\rceil,
\qquad
v_r=\left\lceil\frac{X+h}{r}\right\rceil,
\qquad
x_{q,r}=\max(u_q,v_r).
\tag{2}
\]

Give any selected family of nonempty overlaps arbitrary nonnegative pair weights `lambda_{q,r}` and put

\[
w(\xi)=\sum_{q,r}\lambda_{q,r}
\mathbf1_{x_{q,r}\equiv\xi\pmod p},
\qquad
R_{\rm start}=\frac{\|w\|_1^2}{\|w\|_2^2}.
\tag{3}
\]

For every `Z>0`,

\[
\boxed{
\#\left\{
\left\lceil\frac Zq\right\rceil:
Q\le q\le2Q,
\ q\equiv a\pmod p
\right\}
\le
\min\left(
1+\frac Qp,
\ 2+\frac{Z}{2Q}
\right).
}
\tag{4}
\]

The same bound holds after restricting `q` to primes or active first-exit labels. Since each physical overlap start is one of its two endpoint values,

\[
\boxed{
R_{\rm start}
\le
\min\left(1+\frac Qp,2+\frac{X}{2Q}\right)
+
\min\left(1+\frac Qp,2+\frac{X+h}{2Q}\right).
}
\tag{5}
\]

Using

\[
\min(1+x,2+y)\le2+\min(x,y)\le2+\sqrt{xy}
\tag{6}
\]

removes `Q`:

\[
R_{\rm start}
\le
4+\sqrt{\frac{X}{2p}}
+
\sqrt{\frac{X+h}{2p}}.
\tag{7}
\]

With

\[
Z_*:=\max(X,X+h),
\]

this gives the simpler ceiling

\[
\boxed{
R_{\rm start}
\le4+\sqrt{\frac{2Z_*}{p}}.
}
\tag{8}
\]

Thus varying the dyadic first-exit scale cannot make the available endpoint-start population arbitrarily large: small `Q` is label-limited, large `Q` is quotient-compression-limited, and the best possible scale is at most `O(sqrt(Z_*/p))`.

After the Fourier-Parseval correction in `MC-497`, the `MC-498` maximal-second-moment tariff is

\[
\boxed{
T_{p,H}:=\frac pH\log^2(2H).
}
\tag{9}
\]

and

\[
\frac{|B|}{M}
\ll\sqrt{\frac{T_{p,H}}{R_{\rm start}}}.
\tag{10}
\]

Therefore, for this certificate to prove a fixed target bound `|B|/M<=delta`, a necessary feasibility condition is

\[
T_{p,H}
\ll_\delta
4+\sqrt{\frac{2Z_*}{p}}.
\tag{11}
\]

Once `T_{p,H}` is larger than a fixed constant depending only on `delta`, equation `(11)` forces the `Q`-free source-height gate

\[
\boxed{
Z_*
\gg_\delta
pT_{p,H}^2
=
\frac{p^3}{H^2}\log^4(2H).
}
\tag{12}
\]

The previous version also displayed a separate necessary term `Z_* >> p^2 log^2(2H)`. That term came from the nonsharp `sqrt(p) log(2H)` contribution in the old `MC-498` tariff and is removed by the corrected Fourier-Parseval second moment. The surviving source-height obstruction `(12)` is still strong in the unresolved short-overlap regime. Near the `MC-496` completion boundary, where `H` is comparable to `sqrt(p) log p`, it is already of order `p^2` times logarithmic factors; for shorter `H` it becomes stronger.

Hence there remains a parameter regime where **no dyadic first-exit scale `Q` can make the current exceptional-start dispersion certificate succeed**, even under perfectly flat reconstruction weights. This is a ceiling on the proof method, not evidence that the true endpoint bias is large and not a bound for `M(x)`.

## 1. Exact dyadic quotient-value count

For fixed `Z>0`, the map

\[
q\mapsto\left\lceil\frac Zq\right\rceil
\]

is nonincreasing. On `Q<=q<=2Q`, every attained integer lies between

\[
\left\lceil\frac{Z}{2Q}\right\rceil
\quad\text{and}\quad
\left\lceil\frac ZQ\right\rceil.
\]

Therefore the total number of possible quotient values, before imposing a residue condition, is at most

\[
\left\lceil\frac ZQ\right\rceil
-
\left\lceil\frac{Z}{2Q}\right\rceil+1
\le2+\frac{Z}{2Q}.
\tag{13}
\]

Independently, one residue class modulo `p` contains at most `1+Q/p` integers in `[Q,2Q]`. The endpoint image cannot contain more values than source labels, so the minimum of the two bounds proves `(4)`.

## 2. Pair multiplicity cannot exceed the endpoint images

Equation `(2)` gives

\[
\operatorname{supp}(w)
\subseteq
\{u_q\bmod p\}
\cup
\{v_r\bmod p\}.
\tag{14}
\]

Reduction modulo `p` can only identify quotient values. Applying `(4)` to the two endpoint families yields `(5)`, while Cauchy gives

\[
R_{\rm start}\le\#\operatorname{supp}(w).
\tag{15}
\]

The geometric-mean inequality `(6)` then proves `(7)`--`(8)`. The square-root scale is exactly the balance between the label resource `Q/p` and the quotient-value resource `Z/Q`.

## 3. Consequence for the corrected MC-498 certificate

The endpoint certificate can prove a fixed saving only when `R_start` exceeds a fixed `delta`-dependent multiple of `T_{p,H}`. Substituting `(8)` gives `(11)`, and squaring after the constant term is dominated gives `(12)`.

This sharpens `MC-499` in a way independent of the dyadic first-exit scale. The per-block population gate requires roughly

\[
Q/p\gg T_{p,H},
\]

but increasing `Q` cannot evade that requirement indefinitely because it simultaneously shrinks the endpoint quotient range like `Z_*/Q`. Their product is controlled by `Z_*/p`, so maximal start support is only square-root in the source-height ratio.

The audit order is therefore:

1. apply the `Q`-free source-height gate `(11)`;
2. only if it passes, apply the `MC-499` per-block source-population gate;
3. only then compute the exact `MC-498` participation ratios and quotient fibres.

## 4. Relation to the MC-496 long-overlap threshold

`MC-496` already controls endpoint-only overlap families whose weighted average length is much larger than `sqrt(p) log p` by worst-case Fourier completion. The current branch is therefore relevant below or near that conductor-square-root scale.

At `H` comparable to `sqrt(p) log p`, the corrected gate `(12)` has scale roughly

\[
\frac{p^3}{p\log^2 p}\,\log^4 p
\asymp p^2\log^2 p,
\]

up to constants from replacing `log(2H)` by a constant multiple of `log p`. Thus the earlier `p^2` logarithmic scale survives near the interface with `MC-496`, but now for the correct reason: it comes from the `p/H` start-dispersion tariff evaluated at the completion boundary, not from a separate artificial `sqrt(p)` floor.

## Prior art and novelty boundary

No new theorem about floor quotients is claimed. The hyperbola structure and `O(sqrt(x))` global cardinality of reciprocal floor-quotient sets are classical. Randell Heyman, *Cardinality of a floor function set* (arXiv:1905.00533), and Yahui Yu and Jie Wu, *Distribution of elements of a floor function set in arithmetical progression* (arXiv:2112.14427), are neighboring references.

The participation-ratio inequality is elementary Cauchy, and the corrected analytic tariff comes from `MC-497`/`MC-498` using the classical mixed Weil estimate recorded in `MC-S55`. No novelty is claimed for those ingredients.

The durable Mathia result is their composition with the exact physical first-exit start map, producing the `Q`-free method barrier `(11)`--`(12)`.

## Boundaries and falsification tests

- **Endpoint-only branch.** Lower-prime pair-sieve variation and q-dependent signed/complex pre-aggregation coefficients remain outside this ceiling.
- **Method ceiling, not a true-bias lower bound.** Failing `(11)` says only that the current effective-support certificate cannot prove the target saving.
- **Positive physical endpoints.** The displayed square-root form assumes positive `X` and `X+h`; outside that regime the elementary range count must be rewritten with appropriate absolute heights.
- **One repeated conductor residue.** Pooling distinct residues changes the conductor phase organization.
- **No prime-distribution input.** Restricting labels to primes can only shrink the endpoint images.
- **No claim of sharp attainment.** The upper bound does not assert that eligible prime labels exist near the balancing scale, that their quotient values are distinct, or that reconstruction weights are flat.
- **No global Möbius conclusion.** There is no estimate for `M(x)`, zero-free region, or RH.

## Consequence for the accepted clue

The endpoint-only part of the accepted q-vdC clue has a strict admission order. First apply the corrected `Q`-free source-height gate

\[
Z_*
\gg_\delta
\frac{p^3}{H^2}\log^4(2H).
\]

If it fails, no dyadic first-exit scale can make the current exceptional-start dispersion certificate close the block family. If it passes, use `MC-499` and then the exact `MC-498` start-participation/fibre audit. This prevents spending effort on detailed quotient fibres in a source-height regime where the corrected harmonic certificate is structurally unable to succeed.