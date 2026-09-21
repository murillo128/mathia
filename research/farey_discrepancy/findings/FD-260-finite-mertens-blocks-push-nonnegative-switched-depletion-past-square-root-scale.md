# FD-260 — Finite Mertens blocks push nonnegative switched depletion past square-root scale

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response positivity / quantitative switched stability / exact finite Mertens kernel / dyadic capacity depletion / source-side boundary obstruction
- **Depends on:** FD-230, FD-257
- **Evidence:** exact derivation plus exhaustive finite computation, independently cross-checked by two integer Möbius sieves through `2^19`
- **Classification:** `EXACT-DERIVED + FINITE-EXACT-COMPUTATION + NONNEGATIVE-CAPACITY + BOUNDED-SWITCHED-ROWS + SUPER-SQUARE-ROOT-DEPLETION`

## Claim

FD-257 proves that bounded switched rows force a fixed positive power of dyadic capacity depletion for every nonnegative linear-capacity coefficient profile. Its explicit exponent

\[
\beta=\log_2(24/23)=0.0614005\ldots
\]

comes from retaining only the first two exact dyadic Mertens maxima and then replacing every later block by the trivial estimate `|M(q)|<=q`.

The same proof becomes much stronger after inserting only finitely many additional exact Mertens blocks.

Let

\[
(\mathscr A b)(m)
=
\sum_{d\le m}b_d M\!\left(\left\lfloor\frac md\right\rfloor\right),
\]

assume

\[
0\le b_d\le Cd,
\]

put

\[
B_k=[2^k,2^{k+1})\cap\mathbb N,
\qquad
s_k=4^{-(k+1)}\sum_{d\in B_k}b_d,
\]

and suppose the period-three switched schedule of FD-257 satisfies

\[
|(E-I)^{r_j}(\mathscr A b)(2^j)|\le B,
\qquad
r_j=(1,4,4,1,4,4,\ldots).
\]

Then there is an absolute constant `A` such that

\[
\boxed{
 s_k\le A(C+B)\left(\frac23\right)^k.
}
\tag{1}
\]

Equivalently, at divisor scale `x=2^k`,

\[
\boxed{
\frac{\sum_{x\le d<2x}b_d}
     {\sum_{x\le d<2x}d}
\ll
(C+B)x^{-\beta_*},
\qquad
\beta_*:=\log_2\frac32
=0.5849625007\ldots .
}
\tag{2}
\]

Thus the general nonnegative signed-increment case of FD-257 already has a certified depletion exponent **strictly larger than `1/2`**. No sign condition on `mu*b` is used; the inverse-linear theorem of FD-259 remains strictly stronger and structurally different.

This is an exponent sharpening of the existing FD-257 mechanism, not a new mechanism. Its significance is that the crude `0.0614...` rate was almost entirely an artifact of discarding finite arithmetic information: nineteen dyadic Mertens blocks suffice to move the same Volterra argument past the inverse-square-root scale.

## 1. Reuse the exact FD-257 response and positivity reductions

FD-257 already proves from bounded switched rows that, with

\[
y_j=(\mathscr A b)(2^j),
\qquad
u_j=4^{-j}y_j,
\]

one has

\[
\boxed{|u_j|\ll(C+B)2^{-j}.}
\tag{3}
\]

Its positivity reduction, inherited from FD-230, is

\[
|u_j-s_{j-1}|
\le
\sum_{\ell=2}^{j}c_\ell s_{j-\ell}
+O(C2^{-j}),
\tag{4}
\]

where

\[
\boxed{
c_\ell
=
4^{1-\ell}
\max_{2^{\ell-1}\le q\le2^\ell}|M(q)|.
}
\tag{5}
\]

Putting `k=j-1`, equations (3)--(4) give

\[
\boxed{
s_k
\le
A_0(C+B)2^{-k}
+
\sum_{\ell=2}^{k+1}c_\ell s_{k+1-\ell}.
}
\tag{6}
\]

Everything below is therefore reduced to proving that the positive convolution kernel in (6) is a strict contraction in the weight `r^k` for `r=2/3`.

## 2. Exact finite Mertens block certificate

For

\[
m_\ell:=\max_{2^{\ell-1}\le q\le2^\ell}|M(q)|,
\]

an exhaustive integer Möbius sieve through `2^19=524288` gives the following exact values. The final two columns record one point attaining each maximum and its signed Mertens value.

| `ell` | dyadic interval | `m_ell` | witness `q` | `M(q)` |
| ---: | ---: | ---: | ---: | ---: |
| 2 | `[2,4]` | 1 | 3 | -1 |
| 3 | `[4,8]` | 2 | 5 | -2 |
| 4 | `[8,16]` | 3 | 13 | -3 |
| 5 | `[16,32]` | 4 | 31 | -4 |
| 6 | `[32,64]` | 4 | 32 | -4 |
| 7 | `[64,128]` | 6 | 114 | -6 |
| 8 | `[128,256]` | 8 | 199 | -8 |
| 9 | `[256,512]` | 9 | 443 | -9 |
| 10 | `[512,1024]` | 12 | 665 | -12 |
| 11 | `[1024,2048]` | 16 | 1637 | -16 |
| 12 | `[2048,4096]` | 25 | 2803 | -25 |
| 13 | `[4096,8192]` | 29 | 7021 | -29 |
| 14 | `[8192,16384]` | 43 | 9861 | -43 |
| 15 | `[16384,32768]` | 73 | 31990 | 73 |
| 16 | `[32768,65536]` | 113 | 59577 | -113 |
| 17 | `[65536,131072]` | 132 | 96014 | -132 |
| 18 | `[131072,262144]` | 154 | 230399 | -154 |
| 19 | `[262144,524288]` | 258 | 355733 | -258 |

The computation was independently reproduced in two elementary ways: a linear Euler sieve for `mu(n)`, and a prime-multiple sieve that flips the sign on multiples of each prime and zeros multiples of `p^2`. The two arrays agreed pointwise for every `n<=2^19`, after which cumulative summation gave the same block maxima above. No floating-point arithmetic enters this certificate.

For all later blocks we deliberately return to the trivial estimate

\[
|M(q)|\le q,
\]

so

\[
c_\ell\le2^{2-\ell}
\qquad(\ell\ge20).
\tag{7}
\]

Thus the theorem uses no asymptotic Mertens estimate and no external numerical table.

## 3. The weight `r=2/3` is a strict contraction

Set

\[
r=\frac23.
\]

Using the exact values above in (5), direct rational arithmetic gives

\[
\sum_{\ell=2}^{19}c_\ell r^{1-\ell}
=
\frac{8605747233769089}{9007199254740992}
=0.9554298723\ldots .
\tag{8}
\]

For the remaining tail, (7) gives a geometric series:

\[
\begin{aligned}
\sum_{\ell\ge20}c_\ell r^{1-\ell}
&\le
\sum_{\ell\ge20}2^{2-\ell}
\left(\frac23\right)^{1-\ell}\\
&=
\frac{3^{19}}{2^{35}}\\
&=
\frac{1162261467}{34359738368}
=0.03382626068\ldots .
\end{aligned}
\tag{9}
\]

Combining (8)--(9),

\[
\boxed{
\sum_{\ell\ge2}c_\ell r^{1-\ell}
\le
\frac{8910427103774337}{9007199254740992}
=0.9892561329\ldots
<1.
}
\tag{10}
\]

The contraction margin is therefore more than `0.0107`; it is not a rounding artifact.

Since `2^{-k}<=(2/3)^k`, the induction of FD-257 now applies verbatim to (6). Enlarge the initial constant to cover the finitely many starting indices. If

\[
s_h\le A(C+B)r^h
\qquad(h<k),
\]

then the convolution term in (6) consumes at most the factor in (10) of the inductive budget, while the forcing term is a fixed multiple of `(C+B)r^k`. The positive margin in (10) absorbs it uniformly. This proves (1), and (2) follows from `x=2^k` and `sum_(d in B_k)d asymp4^k`.

## 4. Stress tests and the kernel-method frontier

The nineteenth block is not decorative. Under the exact-sieve-plus-trivial-tail certification used here, stopping one block earlier does **not** prove the same `r=2/3` contraction. Through `ell=18` the exact prefix plus the trivial tail is

\[
1.0005260046\ldots>1,
\]

whereas including `ell=19` lowers the certified upper bound to (10). This gives a useful reproducibility check on the cutoff.

The finite data also prevent overclaiming the exponent. At

\[
r=\frac{13}{20}=0.65,
\]

the exact prefix alone already satisfies

\[
\sum_{\ell=2}^{19}c_\ell r^{1-\ell}
=
1.0107867316\ldots>1.
\tag{11}
\]

Therefore no estimate on the positive tail can make this particular weighted-kernel argument contract at `r=0.65`. If `r_c` denotes the exact threshold for the full kernel in (5), monotonicity gives the rigorous bracket

\[
\boxed{
0.65<r_c<\frac23.
}
\tag{12}
\]

Hence the best exponent obtainable from the **same positive Volterra kernel without additional structural input** lies in

\[
\boxed{
\log_2\frac32
<
\log_2\frac1{r_c}
<
\log_2\frac{20}{13},
}
\tag{13}
\]

that is, between `0.58496...` and `0.62149...`. This does not assert that the true source-side depletion exponent is in this interval; it brackets only the contraction threshold of the FD-230/FD-257 kernel method.

The result also does not approach the inverse-linear rate of FD-259. There the additional hypothesis `mu*b>=0` removes the signed-increment freedom and yields exponent `1` by a different local argument. FD-260 retains arbitrary signs in `mu*b` and only sharpens what follows from coefficient nonnegativity plus bounded switched rows.

## 5. Prior-art boundary and implications

A targeted literature audit found the expected computational literature for the Mertens function, including Greg Hurst's 2018 all-values computation through `10^16` and his 2026 record computations, as well as the classical exponential-stability theory for Volterra difference equations. No novelty is claimed for computing finite Mertens values, for Möbius sieving, or for weighted convolution stability.

Those external computations are not load-bearing here: the finite values in Section 2 were independently recomputed inside this pass, and the infinite tail uses only `|M(q)|<=q`. Therefore no new source dependency is required in `SOURCES.md`.

What is specific to the Farey-discrepancy line is the quantitative transfer through the exact FD-230 positivity kernel and the bounded period-three switched response of FD-257. The previous explicit rate `x^(-0.0614...)` materially understated what that already-established mechanism proves. The corrected certified ceiling is

\[
\boxed{x^{-0.58496\ldots},}
\]

uniformly over arbitrary redistribution of nonnegative mass inside each dyadic divisor band.

For the live source-side question this strengthens the benchmark against which a physical Mertens repair must be compared: any genuinely signed-increment nonnegative cushion with bounded switched contribution has less than inverse-square-root relative capacity available on sufficiently deep bands. A complete obstruction still requires a lower bound showing that the concrete repair consumes more positive slack than this ceiling on some relevant bands. FD-260 does not supply that lower bound.

## Status

**Proved.** The exact response estimate and positive Volterra recurrence are inherited from FD-257. An exhaustive exact computation of the dyadic Mertens maxima through `2^19`, cross-checked by two independent sieves, makes `r=2/3` a strict weighted contraction even if every later Mertens block is bounded only trivially. Consequently the general nonnegative bounded-switched depletion exponent improves from `log_2(24/23)=0.0614...` to the certified value `log_2(3/2)=0.58496...>1/2`.