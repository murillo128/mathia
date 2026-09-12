# MC-243 — Blind-support growth gives only coding-scale rank pressure

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the quadratic blind-sector notation of `MC-238`. For a shell set

\[
S\subset\{r\text{ prime}:y<r\le 2y\},
\qquad n:=|S|,
\]

let

\[
A_{p,r}=\frac{1-(\frac pr)}2\in\mathbb F_2,
\qquad p\le y\text{ prime},\ r\in S,
\]

and write

\[
K_y(S):=\ker_{\mathbb F_2}A,
\qquad
R_y(S):=\operatorname{rank}_{\mathbb F_2}A.
\]

By `MC-238`, `K_y(S)` is exactly the quadratic smooth-dilation blind sector. By `MC-242`, every nonzero blind vector has Hamming weight

\[
\operatorname{wt}(v)
\ge
\left(\frac1{\log 2}-o(1)\right)\log\log y.
\tag{1}
\]

Thus `K_y(S)` is a binary linear code whose minimum distance grows at least at the double-logarithmic scale.

The coding interpretation converts `(1)` into a genuine rank lower bound, but also proves a sharp information barrier for any route that keeps only the minimum blind support.

If `K_y(S)\ne\{0\}` and

\[
d_y:=\min_{0\ne v\in K_y(S)}\operatorname{wt}(v),
\qquad
t_y:=\left\lfloor\frac{d_y-1}{2}\right\rfloor,
\]

then the binary Hamming sphere-packing bound gives exactly

\[
\boxed{
R_y(S)
\ge
\log_2\!\left(
\sum_{j=0}^{t_y}\binom nj
\right).
}
\tag{2}
\]

For the active first-shell scaling from `MC-238`,

\[
n
=
(\alpha+o(1))\frac{\log X}{\log\log X},
\qquad
y=c\log X,
\]

so

\[
n=\left(\frac\alpha c+o(1)\right)\frac y{\log y},
\qquad
\log n\sim\log y.
\tag{3}
\]

Combining `(1)`--`(3)` yields the unconditional rank consequence

\[
\boxed{
R_y(S)
\ge
\left(
\frac{1}{2(\log 2)^2}-o(1)
\right)
\log y\,\log\log y.
}
\tag{4}
\]

whenever the quadratic blind sector is nontrivial; if it is trivial, of course `R_y(S)=n` already.

However, the same coding language shows that this is essentially the most one can infer from a double-logarithmic **minimum-support statement alone**. The linear Gilbert--Varshamov/Varshamov existence bound gives binary linear codes of length `n` and minimum distance at least `d` with redundancy

\[
n-\dim C
\le
\log_2\!\left(
\sum_{j=0}^{d-2}\binom{n-1}{j}
\right)+O(1).
\tag{5}
\]

For

\[
d\asymp\log\log y,
\qquad
n\asymp\frac y{\log y},
\]

this is only

\[
O(\log y\,\log\log y).
\tag{6}
\]

Hence there are abstract binary linear kernels satisfying the same minimum-support scale as `MC-242` while still having

\[
\dim C
=
n-O(\log y\,\log\log y).
\tag{7}
\]

The Varshamov comparison is a **matched coding-theory control**, not an assertion that such a large kernel occurs for the Legendre matrix `A`. Its role is to isolate what the support information itself can and cannot force.

Consequently:

\[
\boxed{
\text{minimum blind support}
\quad\not\Rightarrow\quad
\text{small blind-sector dimension or annihilator triviality}.
}
\tag{8}
\]

At the current `MC-242` scale, minimum-support information yields only a `Theta(log y log log y)` generic coding-pressure scale for the rank, whereas full quadratic generation requires rank `n asymp y/log y`. Closing that gap requires arithmetic structure of the Legendre matrix, a direct count/dimension estimate for blind modes, or a source-coupling theorem; further support lower bounds by themselves do not supply the missing implication.

No estimate for the Möbius progression amplitudes, no bound for `M(X)`, and no consequence for the zeta zero set is proved.

## 1. The quadratic blind sector is literally a binary linear code

For `v in F_2^S`, `MC-238` associates the quadratic character

\[
\chi_v(m)
=
\prod_{r\in S}
\left(\frac mr\right)^{v_r}.
\]

The condition that every small prime is invisible to this character is

\[
\chi_v(p)=1
\quad(p\le y\text{ prime}),
\]

which is equivalent to

\[
Av=0.
\]

Therefore `K_y(S)` is not merely analogous to a code: it is an actual binary linear subspace of block length `n`, and the local character support is exactly Hamming weight. Since a linear code's minimum distance equals the least nonzero codeword weight, `MC-242` is precisely a lower bound for the minimum distance of this code.

This representation uses no heuristic independence of Legendre symbols and no random-matrix model.

## 2. Sphere packing turns the support floor into a rank lower bound

Put

\[
k:=\dim K_y(S)=n-R_y(S).
\]

If the minimum distance is `d_y`, Hamming balls of radius

\[
t_y=\left\lfloor\frac{d_y-1}{2}\right\rfloor
\]

around distinct codewords are disjoint. Each ball contains

\[
V_2(n,t_y)
=
\sum_{j=0}^{t_y}\binom nj
\]

binary vectors. Therefore

\[
2^kV_2(n,t_y)\le 2^n.
\]

Using `k=n-R_y(S)` gives `(2)` exactly.

Now fix any

\[
0<\theta<\frac1{\log2}.
\]

`MC-242` implies that for all sufficiently large `y`, every nonzero blind vector has

\[
d_y>\theta\log\log y.
\]

Thus

\[
t_y
\ge
\left(\frac\theta2-o(1)\right)\log\log y.
\]

Under `(3)`, `t_y=o(n)` and

\[
\log\binom n{t_y}
=
t_y\log\frac n{t_y}+O(t_y)
=
\left(\frac\theta2-o(1)\right)
\log y\,\log\log y.
\]

Since `V_2(n,t_y)>=binom(n,t_y)`, division by `log 2` gives

\[
R_y(S)
\ge
\left(\frac\theta{2\log2}-o(1)\right)
\log y\,\log\log y.
\]

Letting `theta` tend to `1/log 2` proves `(4)`.

This is a new quantitative consequence for the exact `MC-238` matrix, but it remains far below the full-rank scale `n asymp y/log y`.

## 3. Minimum distance alone cannot bridge the remaining rank gap

The converse control is classical coding theory. The linear Varshamov construction gives a binary linear code of length `n` and minimum distance at least `d` whenever a parity-check redundancy `r` is chosen with

\[
2^r
>
\sum_{j=0}^{d-2}\binom{n-1}{j}.
\tag{9}
\]

Equivalently one may take

\[
r
\le
\log_2\!\left(
\sum_{j=0}^{d-2}\binom{n-1}{j}
\right)+O(1),
\]

which is `(5)`.

For `d=o(n)`, the upper sum has logarithm

\[
O\!\left(d\log\frac nd\right).
\tag{10}
\]

At the `MC-242` scale this becomes `(6)`, so abstract linear codes can have the required growing minimum support while their parity-check rank remains only `O(log y log log y)` and their kernel dimension remains `n-o(n)`.

There is an even simpler endpoint warning: a one-dimensional binary subspace `{0,v}` may have its unique nonzero vector supported on all `n` coordinates. Therefore **no lower bound on minimum support that stays within the possible range `d<=n` can, by itself, prove that a binary kernel is trivial**. Support information can force quantitative redundancy, but annihilator triviality is a different invariant.

The relevant Mathia consequence is not that the actual Legendre kernel is large. It is that any proof using only the scalar statistic

\[
\min_{0\ne v\in K_y(S)}\operatorname{wt}(v)
\]

has discarded the information needed to decide whether `K_y(S)` has one element, two elements, or exponentially many elements once nontriviality is not already ruled out.

## 4. Prior art and novelty audit

The sphere-packing inequality used in `(2)` is the classical Hamming bound. See R. W. Hamming, *Error Detecting and Error Correcting Codes*, Bell System Technical Journal 29 (1950), 147--160, DOI `10.1002/j.1538-7305.1950.tb00463.x`.

The existence comparison `(9)` is the classical linear Varshamov/Gilbert--Varshamov mechanism. See R. R. Varshamov, *Estimate of the number of signals in error correcting codes*, Doklady Akademii Nauk SSSR 117 (1957), 739--741, and E. N. Gilbert, *A Comparison of Signalling Alphabets*, Bell System Technical Journal 31 (1952), 504--522, DOI `10.1002/j.1538-7305.1952.tb01393.x`.

The coding bounds, their Hamming-ball asymptotics, and the fact that minimum distance does not determine code dimension are classical. **No novelty is claimed for any coding-theory statement.**

A targeted literature search found extensive work on Hamming/Gilbert--Varshamov bounds and on specialized Legendre-symbol matrices, but no source was used to claim a rank theorem for this particular lower-prime/shell-prime matrix. The durable delta here is only the exact specialization of the classical coding bounds to the blind-sector identity of `MC-238` plus the quantitative distance input of `MC-242`.

## Decisive audit

The rank lower bound `(4)` uses only two ingredients: the exact identity `K_y(S)=ker A` from `MC-238` and the minimum-support theorem `MC-242`. It makes no probabilistic assumption about Legendre symbols.

The Varshamov construction is deliberately **not** transferred to the arithmetic matrix. It certifies only an information-theoretic no-go: minimum-distance data of the current size are compatible, in the category of binary linear subspaces, with almost maximal kernel dimension. Any stronger conclusion for `A` must use structure absent from a generic code.

There is no contradiction between `(4)` and `(7)`: `(4)` is a lower bound on the rank of the actual Legendre matrix, while `(7)` exhibits abstract comparison codes showing that a rank of the same logarithmic order is compatible with the same minimum-distance scale.

## Boundaries and updated frontier

- `MC-242` now implies the explicit rank lower bound `(4)` for the quadratic Legendre matrix at the active shell scaling.
- The bound is still `o(n)` and therefore does not materially approach full column rank.
- Increasing only the minimum blind support cannot establish annihilator triviality; even a full-support lone kernel vector remains compatible with a nontrivial kernel.
- The next rank-level progress must exploit arithmetic dependencies among the Legendre rows/columns, bound the **number or dimension** of blind characters directly, or bypass rank by proving that surviving modes have negligible coupling to the Möbius progression vector.
- Support size, blind-sector dimension, Fourier decay, and signed source amplitude remain separate currencies.