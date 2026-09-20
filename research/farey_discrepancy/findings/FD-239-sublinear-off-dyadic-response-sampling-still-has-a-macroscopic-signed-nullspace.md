# FD-239 — Low positive-density off-dyadic response sampling still has a macroscopic signed nullspace

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / positive-density point sampling / signed capacity / exact prescribed zeros / response-density boundary
- **Depends on:** FD-225, FD-231, FD-238
- **Classification:** `EXACT-DERIVED + COUNTERMODEL + LOW-POSITIVE-DENSITY-SAMPLING-NULLSPACE + SIGNED-LINEAR-CAPACITY + RESPONSE-DENSITY-BOUNDARY`

## Claim

FD-238 shows that exact dyadic response coordinates leave a macroscopic signed nullspace. The same obstruction survives not only sublinear off-dyadic sampling, but an explicit nonzero density of arbitrarily placed point samples in every dyadic octave.

Let `S subset N` be any prescribed sampling set and write

\[
B_k=(2^{k-1},2^k]\cap\mathbb N,
\qquad
s_k=|S\cap B_k|,
\qquad
\eta=\limsup_{k\to\infty}\frac{s_k}{|B_k|}.
\]

Since `|B_k|=2^{k-1}`, assume

\[
\boxed{
\eta<\eta_0:=\frac9{\pi^2}-\frac34
=0.161890652\ldots .
}
\tag{1}
\]

Then there exists an integer sequence `(b_n)` satisfying

\[
\boxed{|b_n|\le n\qquad(n\ge1),}
\tag{2}
\]

whose divisor response

\[
(\mathscr A b)(m)
=
\sum_{d\le m}b_dM\!\left(\left\lfloor\frac md\right\rfloor\right)
\tag{3}
\]

vanishes at every prescribed sample and at every dyadic endpoint:

\[
\boxed{
(\mathscr A b)(s)=0\quad(s\in S),
\qquad
(\mathscr A b)(2^j)=0\quad(j\ge0).
}
\tag{4}
\]

Its full off-sample response remains only linear,

\[
\boxed{(\mathscr A b)(m)=O(m),}
\tag{5}
\]

while its coefficient mass obeys the quantitative lower bound

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\ge
\frac{12}{\pi^2}-1-\frac43\eta.
}
\tag{6}
\]

The right-hand side is positive precisely under `(1)`. Both signs are macroscopic:

\[
\boxed{
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^+}
     {\sum_{n\in B_k}n},
\quad
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}b_n^-}
     {\sum_{n\in B_k}n}
\ge
\frac12\left(
\frac{12}{\pi^2}-1-\frac43\eta
\right).
}
\tag{7}
\]

Thus **even an arbitrary fixed positive fraction of all integer response coordinates per octave can fail to be signed-coercive**: every sampling pattern with asymptotic octave density below `16.18%` is annihilated exactly by a macroscopic signed profile in the natural linear-capacity box.

The threshold `eta_0` is a guaranteed survival range for this construction, not a claimed sharp coercivity threshold. Positive-density sampling above `eta_0` may still have a macroscopic nullspace; this argument simply stops certifying one there. At the opposite endpoint, retaining every integer response is injective by the exact divisor inversion of FD-225.

The construction is signed and therefore is not a physical nonnegative prime-reservoir occupancy. Positivity and source coherence remain possible mechanisms of transversality.

## 1. Exact reset points at every requested sample

As in FD-238, start from an integer arithmetic function `g` and set

\[
b=\mathbf1*g,
\qquad
b_n=\sum_{d\mid n}g(d).
\tag{8}
\]

Since `mu*1=epsilon`, the divisor response has the exact cumulative form

\[
\boxed{
(\mathscr A b)(m)
=
\sum_{n\le m}g(n)
=:Y(m).
}
\tag{9}
\]

Set `g(1)=0`. Fix a dyadic band `B_k`. Order the points of `S cap B_k`, adjoin the right endpoint `2^k`, and use them as consecutive cell boundaries. The band is partitioned into at most

\[
s_k+1
\tag{10}
\]

nonempty consecutive integer cells. The left endpoint `2^{k-1}` already has zero cumulative sum from the preceding band.

Treat each cell independently. Choose a pivot `e` for which `phi(e)` is maximal. Process all nonpivot integers in increasing order and assign

\[
g(n)\in\{-\varphi(n),+\varphi(n)\}
\tag{11}
\]

with sign opposite to the current nonpivot partial sum. If `W` is the largest nonpivot `phi`-weight in the cell, this greedy rule keeps that running sum in `[-W,W]`. At the end set the pivot equal to the negative final nonpivot sum. Maximality of `phi(e)` gives

\[
|g(e)|\le W\le\varphi(e).
\tag{12}
\]

Hence every cell has exact total zero, every `g(n)` is integral, and

\[
|g(n)|\le\varphi(n).
\tag{13}
\]

Every requested sample and every dyadic endpoint is a completed-cell boundary, so `(9)` gives `(4)` exactly.

## 2. Full response and coefficient envelope

Inside a cell the nonpivot greedy sum has modulus at most `W`. If the pivot occurs before the end in natural order, inserting its final correction changes a partial sum into a difference of two greedy partial sums, hence into a quantity of modulus at most `2W`. For `m in B_k`, `W<=2^k`, so

\[
|Y(m)|\le2^{k+1}=O(m).
\tag{14}
\]

This proves `(5)`.

From `(8)`, `(13)`, and the classical identity

\[
\sum_{d\mid n}\varphi(d)=n,
\]

we get

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|
\le
\sum_{d\mid n}\varphi(d)
=n,
\tag{15}
\]

which proves `(2)`.

## 3. Quantitative capacity retained at positive sampling density

Every nonpivot integer remains saturated:

\[
|g(n)|=\varphi(n).
\tag{16}
\]

For such an `n`, separate the top divisor in `(8)`:

\[
\begin{aligned}
|b_n|
&\ge
|g(n)|-
\sum_{\substack{d\mid n\\d<n}}|g(d)|\\
&\ge
\varphi(n)-
\sum_{\substack{d\mid n\\d<n}}\varphi(d)\\
&=
2\varphi(n)-n.
\end{aligned}
\tag{17}
\]

Let `P_k` be the pivot set in `B_k`. Since `|P_k|<=s_k+1` and `2phi(n)-n<=n<=2^k`, summing `(17)` over the nonpivots gives

\[
\sum_{n\in B_k}|b_n|
\ge
\sum_{n\in B_k}(2\varphi(n)-n)
-(s_k+1)2^k.
\tag{18}
\]

The standard totient asymptotic

\[
\sum_{n\le x}\varphi(n)
=
\frac3{\pi^2}x^2+O(x\log x)
\tag{19}
\]

yields

\[
\sum_{n\in B_k}(2\varphi(n)-n)
=
\left(\frac9{2\pi^2}-\frac38\right)4^k
+O(k2^k).
\tag{20}
\]

Because `|B_k|=2^{k-1}`, the definition of `eta` gives

\[
(s_k+1)2^k
\le
\left(\frac\eta2+o(1)\right)4^k.
\tag{21}
\]

Therefore

\[
\sum_{n\in B_k}|b_n|
\ge
\left(
\frac9{2\pi^2}-\frac38-\frac\eta2-o(1)
\right)4^k.
\tag{22}
\]

Since

\[
\sum_{n\in B_k}n
=
\frac38\,4^k+O(2^k),
\tag{23}
\]

dividing `(22)` by `(23)` proves `(6)`. The coefficient in `(22)` is positive exactly when

\[
\eta<2\left(\frac9{2\pi^2}-\frac38\right)
=
\frac9{\pi^2}-\frac34,
\]

which is `(1)`.

For `eta=0`, `(6)` recovers the FD-238/previous FD-239 lower bound `12/pi^2-1`. The strengthening is that the same exact-zero construction still retains positive capacity after paying a **linear** number of pivots, as long as their octave density is below the explicit constant above.

## 4. Both signs remain macroscopic

Let

\[
B(x)=\sum_{n\le x}b_n.
\]

Using `(8)` and Abel summation with `Y(d)=O(d)` from `(14)`,

\[
B(x)
=
Y(x)
+
\sum_{d<x}Y(d)
\left(
\left\lfloor\frac xd\right\rfloor
-
\left\lfloor\frac{x}{d+1}\right\rfloor
\right)
=
O(x\log x).
\tag{24}
\]

Hence the signed sum over `B_k` is `O(k2^k)=o(4^k)`. Under `(1)`, `(6)` supplies absolute mass `Omega(4^k)`. Splitting total variation into positive and negative parts proves `(7)`.

## 5. What point sampling can and cannot repair

The earlier sublinear formulation identified positive density as the first regime where the coarse `o(4^k)` pivot-loss argument stopped applying automatically. Tracking the constant shows that this was **not** the actual boundary of the construction. A linear number of exact reset constraints is still harmless while its density is sufficiently small.

Consequently, a response-topology refinement cannot claim signed coercivity merely because it samples `Theta(2^k)` integers per octave. At least for densities below `eta_0`, arbitrary sample placement still leaves a macroscopic exact kernel. Any genuinely coercive point-sampling theorem must therefore either exceed this quantitative range, exploit structure beyond raw sampled values, or use the physical nonnegative/source-coherent class essentially.

This result does not show that `eta_0` is sharp. The only exact opposite endpoint currently available is full all-integer response, where `(mathscr A b)(m)=0` for every `m` forces successive differences of `(9)` to give `g=0`, hence `b=0`.

## Prior-art / novelty audit

The cellwise sign assignment is a one-dimensional discrepancy-balancing argument, and general prefix/vector balancing belongs to the classical Steinitz/discrepancy literature. A targeted search of that literature and of prescribed-zero interval balancing did not locate the line-local quantitative statement here: exact annihilation of an arbitrary positive-density sampling set for the Mertens divisor-response transform while retaining a fixed fraction of the natural linear coefficient capacity.

No external theorem is load-bearing beyond the standard totient identities already used in FD-231 and FD-238. The mathematical delta over the previous version of FD-239 is the explicit pivot-loss calculation `(18)--(23)`, which pushes the nullspace obstruction from sublinear sampling into the positive-density regime and replaces the qualitative open boundary by the certified interval `eta<9/pi^2-3/4`.

## Status

**Proved.** For every prescribed sampling set of asymptotic octave density below `9/pi^2-3/4`, the construction gives exact zero response on all samples and dyadic endpoints, uniform linear full-response control, the natural coefficient envelope, and an explicit positive amount of capacity in both signs. It is a signed response-topology countermodel, not a physical nonnegative source and not an RH estimate.