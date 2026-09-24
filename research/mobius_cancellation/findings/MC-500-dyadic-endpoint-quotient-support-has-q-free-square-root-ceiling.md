# MC-500 — Dyadic endpoint quotient support has a Q-free square-root ceiling

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-FLOOR-QUOTIENT+DERIVED` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-499` shows that the `MC-497`/`MC-498` endpoint-dispersion certificate can fail before any coefficient audit because one repeated conductor residue contains only `O(1+Q/p)` labels in a dyadic block `Q<=q<=2Q`. There is a second, opposite source-cardinality constraint that becomes stronger when `Q` is large: the physical endpoint quotient `ceil(Z/q)` itself has only `O(1+Z/Q)` possible values on that dyadic block.

Combining the two constraints gives a **Q-free ceiling** on the number of physical start residues available to the endpoint-only branch.

Fix an odd prime conductor `p`, a repeated residue `a mod p`, a dyadic label range

\[
Q\le q,r\le 2Q,
\qquad q\equiv r\equiv a\pmod p,
\tag{1}
\]

and a positive source interval `[X,X+Y]` with `X+h>0`. As in `MC-498`, define

\[
u_q=\left\lceil\frac Xq\right\rceil,
\qquad
v_r=\left\lceil\frac{X+h}{r}\right\rceil,
\qquad
x_{q,r}=\max(u_q,v_r).
\tag{2}
\]

Let any selected family of nonempty overlaps carry arbitrary nonnegative pair weights `lambda_{q,r}`, and let

\[
w(\xi)=\sum_{q,r}\lambda_{q,r}
\mathbf 1_{x_{q,r}\equiv\xi\pmod p}
\tag{3}
\]

be the weighted physical-start histogram modulo `p`. Put

\[
R_{\rm start}=\frac{\|w\|_1^2}{\|w\|_2^2}.
\tag{4}
\]

For every `Z>0`, the endpoint image of one repeated-residue label family satisfies

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
\tag{5}
\]

The same bound holds a fortiori after restricting `q` to primes or active first-exit labels. Since every overlap start in `(2)` is literally one of the two endpoint values,

\[
\boxed{
R_{\rm start}
\le
\min\left(1+\frac Qp,2+\frac{X}{2Q}\right)
+
\min\left(1+\frac Qp,2+\frac{X+h}{2Q}\right).
}
\tag{6}
\]

Using

\[
\min(1+x,2+y)
\le 2+\min(x,y)
\le2+\sqrt{xy},
\tag{7}
\]

with `x=Q/p` and `y=Z/(2Q)` removes the dyadic scale entirely:

\[
\boxed{
R_{\rm start}
\le
4+\sqrt{\frac{X}{2p}}
+\sqrt{\frac{X+h}{2p}}.
}
\tag{8}
\]

In particular, with

\[
Z_*:=\max(X,X+h),
\]

one has the simpler ceiling

\[
\boxed{
R_{\rm start}
\le 4+\sqrt{\frac{2Z_*}{p}}.
}
\tag{9}
\]

Thus changing `Q` cannot make the effective physical-start population arbitrarily large. Small `Q` is limited by the number of labels in one residue class; large `Q` is limited by reciprocal-quotient compression. The best possible support scale occurs only near the hyperbola balance `Q/p approx Z_*/Q`, namely `Q approx sqrt(pZ_*)`, and is at most order `sqrt(Z_*/p)`.

Now write the `MC-498` maximal-second-moment tariff as

\[
T_{p,H}
:=
\frac pH\log^2(2H)+\sqrt p\log(2H).
\tag{10}
\]

Its endpoint-only estimate is

\[
\frac{|B|}{M}
\ll
\sqrt{\frac{T_{p,H}}{R_{\rm start}}}.
\tag{11}
\]

Therefore, for this certificate to prove a fixed target bound `|B|/M<=delta`, a necessary feasibility condition is

\[
\boxed{
T_{p,H}
\ll_\delta
4+\sqrt{\frac{2Z_*}{p}}.
}
\tag{12}
\]

Once `T_{p,H}` is larger than a fixed constant depending only on `delta`, `(12)` forces the Q-free source-height gate

\[
\boxed{
Z_*
\gg_\delta
p\,T_{p,H}^2.
}
\tag{13}
\]

Two immediate necessary consequences are

\[
\boxed{
Z_*
\gg_\delta
p^2\log^2(2H)
}
\tag{14}
\]

from the `sqrt(p) log(2H)` term, and

\[
\boxed{
Z_*
\gg_\delta
\frac{p^3}{H^2}\log^4(2H)
}
\tag{15}
\]

from the `p/H` term.

Hence there is a parameter regime where **no dyadic first-exit scale `Q` can make the current exceptional-start dispersion certificate succeed**, even under perfectly flat reconstruction weights: if the source height is below the Q-free threshold `(13)`, increasing `Q` to gain more repeated-residue labels loses physical quotient values at the reciprocal rate, while decreasing `Q` restores quotient values but loses labels.

This is a ceiling on the `MC-497`/`MC-498` proof method, not evidence that the true endpoint bias is large and not a bound for `M(x)`.

## 1. Exact dyadic quotient-value count

For fixed `Z>0`, the map

\[
q\mapsto\left\lceil\frac Zq\right\rceil
\]

is nonincreasing. On `Q<=q<=2Q`, every attained value lies between

\[
\left\lceil\frac{Z}{2Q}\right\rceil
\quad\text{and}\quad
\left\lceil\frac ZQ\right\rceil.
\]

Therefore the total number of possible **integer quotient values**, even before imposing a residue condition on `q`, is at most

\[
\left\lceil\frac ZQ\right\rceil
-
\left\lceil\frac{Z}{2Q}\right\rceil
+1
\le
2+\frac{Z}{2Q}.
\tag{16}
\]

Independently, one residue class modulo `p` contains at most `1+Q/p` integers in `[Q,2Q]`. The endpoint image cannot contain more values than labels, so taking the minimum proves `(5)`.

This is deliberately weaker than refined distribution theorems for floor-quotient sets. Its advantage here is that it is exact enough for the source-frame admission test and requires no distribution result for primes in arithmetic progressions.

## 2. Pair multiplicity cannot exceed the union of endpoint images

Equation `(2)` gives

\[
\operatorname{supp}(w)
\subseteq
\{u_q\bmod p\}
\cup
\{v_r\bmod p\}.
\tag{17}
\]

Reduction modulo `p` can only identify quotient values, never create new ones. Hence `(5)` on the two endpoint families gives the support bound in `(6)`. As in `MC-499`, Cauchy gives

\[
R_{\rm start}
\le \#\operatorname{supp}(w),
\tag{18}
\]

so pair multiplicity, overlap selection, primality, and reconstruction coefficients cannot enlarge the right side of `(6)`.

The Q-free form `(8)` is just the elementary inequality `(7)`. For one endpoint, increasing `Q` raises the label ceiling `Q/p` while lowering the quotient-range ceiling `Z/Q`. Their minimum is maximized near the geometric-mean balance, which produces the square-root scale `sqrt(Z/p)`. Summing the two root endpoints gives `(8)` and `(9)`.

## 3. Consequence for the MC-498 certificate

The estimate `(11)` can certify a fixed small normalized bias only if `R_start` is larger than a fixed `delta`-dependent multiple of `T_{p,H}`. Substituting `(9)` yields `(12)`.

When `T_{p,H}` tends to infinity, the additive constant `4` is negligible after adjusting the fixed `delta`-dependent constant, so `(12)` implies `(13)`. Since both summands in `(10)` are nonnegative, `(14)` and `(15)` follow separately.

This sharpens the interpretation of `MC-499`. The earlier population gate said that a **given** dyadic block needs roughly

\[
Q/p\gg T_{p,H}
\]

available repeated-residue labels. The present result shows that choosing larger `Q` cannot evade that obstruction indefinitely: the same change shrinks the number of endpoint quotient values like `Z_*/Q`. The product of the two resources is fixed at the source-height scale `Z_*/p`, so the maximal available start support is only square-root in that ratio.

Thus the endpoint audit now has an even cheaper pre-gate. Before inspecting a particular dyadic `Q`, compare the source height with `(13)`. If it fails, **every** dyadic block is method-limited for the current start-dispersion certificate. Only if the source-height gate passes is it useful to apply the `MC-499` per-block population test and then the detailed `MC-498` participation/fibre audit.

## 4. Prior art and novelty boundary

No new theorem about floor quotients is claimed. The reciprocal quotient set

\[
\{\lfloor x/n\rfloor:1\le n\le x\}
\]

and its `O(sqrt(x))` cardinality/hyperbola structure are classical objects. Randell Heyman, *Cardinality of a floor function set* (arXiv:1905.00533), studies the global cardinality explicitly, and Yahui Yu and Jie Wu, *Distribution of elements of a floor function set in arithmetical progression* (arXiv:2112.14427), studies the substantially sharper problem of distributing such quotient values in residue classes.

Equation `(16)` is only the trivial local dyadic range count, while `(18)` is the standard participation-ratio/Cauchy inequality already used in `MC-499`. No novelty is claimed for either ingredient or for the geometric-mean optimization by itself.

The durable Mathia-specific delta is their **composition with the exact physical first-exit start map and the `MC-498` second-moment tariff**. That composition turns the Q-dependent source-population obstruction of `MC-499` into the Q-free source-height barrier `(12)`--`(15)`, and changes the order of the decisive test.

## Boundaries and falsification tests

- **Endpoint-only branch.** The result controls only the physical start support available to the `MC-497`/`MC-498` endpoint-dispersion argument. Lower-prime pair-sieve variation and q-dependent signed/complex pre-aggregation coefficients remain outside it.
- **Method ceiling, not true-bias lower bound.** Failing `(12)` says the current maximal-second-moment/effective-support certificate cannot prove the target saving. The actual endpoint correlation may still be small for stronger arithmetic reasons.
- **Positive physical endpoints.** The displayed square-root form assumes `X>0` and `X+h>0`, as in the positive source interval regime. The elementary range argument can be rewritten with absolute endpoint heights outside that regime.
- **One repeated conductor residue.** Pooling different residues changes the conductor phase organization and is not covered by the repeated-residue reduction.
- **No prime-distribution input.** Restricting labels to primes can only shrink the endpoint images, so irregular primes in progressions cannot invalidate the ceiling.
- **No claim of sharp attainment.** The upper bound does not assert that enough eligible prime labels exist near `Q approx sqrt(pZ_*)`, that their endpoint quotient values are distinct, or that the reconstruction weights are flat. Actual effective support can be much smaller.
- **No global Möbius conclusion.** There is no estimate for `M(x)`, no zero-free region, and no RH implication.

## Consequence for the accepted clue

The endpoint-only part of the accepted q-vdC clue now has a three-stage admission test.

First apply the Q-free source-height gate `(12)` using only `p`, the overlap-length band `H`, and the physical source height `Z_*`. If it fails, no choice of dyadic first-exit scale can make the present exceptional-start dispersion certificate close that block family.

If it passes, apply the per-block `MC-499` source-population gate. Only then compute the exact `MC-498` winning-endpoint participation ratios and quotient fibres on the surviving blocks.

This prevents a new form of futile refinement: increasing the first-exit scale to create more repeated-residue labels cannot beat the endpoint obstruction indefinitely, because reciprocal quotient compression removes start diversity at the compensating rate.