# MC-015 — Qualitative Chowla with exact Möbius support permits near-quadratic excursion mass

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

The support-matched Chowla construction of `MC-004` already furnishes a decisive matched control for the excursion-square carrier isolated in `MC-014`.

There exists a deterministic sequence

\[
a:\mathbb N\to\{-1,0,1\}
\]

with the exact Möbius zero set

\[
|a(n)|=\mu(n)^2,
\tag{1}
\]

and the full qualitative index-two Chowla property, yet along an infinite sequence `Y_j -> infinity` its summatory walk

\[
A(k)=\sum_{n\le k}a(n)
\]

has both

\[
\boxed{
D_a(Y_j):=\frac1{Y_j}\sum_{k=0}^{Y_j-1}|A(k)|
\gg \frac{Y_j}{(\log Y_j)^2}
}
\tag{2}
\]

and

\[
\boxed{
E_{2,a}(Y_j):=\sum_r \ell_r(Y_j)^2
\gg \frac{Y_j^2}{(\log Y_j)^2},
}
\tag{3}
\]

where `ell_r(Y)` are the lengths of the maximal nonzero excursions of `A(k)` among `k=0,...,Y-1` as in `MC-014`.

More precisely, the construction gives

\[
D_a(Y_j)
\ge
\left(\frac{18}{\pi^4}+o(1)\right)
\frac{Y_j}{(\log Y_j)^2}
\tag{4}
\]

and

\[
E_{2,a}(Y_j)
\ge
\left(\frac{36}{\pi^4}+o(1)\right)
\frac{Y_j^2}{(\log Y_j)^2}.
\tag{5}
\]

Therefore exact square-free support plus **all qualitative fixed-shift Chowla limits** do not imply any fixed power saving for the mean-absolute summatory statistic, and they cannot imply the excursion-square estimate

\[
E_2(Y)\ll_\varepsilon Y^{3/2+\varepsilon}
\tag{6}
\]

for any fixed `epsilon<1/2`.

This directly narrows the accepted mean-absolute transfer clue: the excursion carrier is cancellation-respecting, but qualitative Chowla information is still far too weak to control it. Any successful route must use a genuinely quantitative growing-scale input, multiplicative consistency not present in this matched control, or another datum that prevents sparse coherent excursions.

## 1. Reuse the exact-support Chowla construction

Write

\[
q(n)=\mu(n)^2.
\]

`MC-004` constructs a deterministic Chowla sequence `a` with `|a|=q` by starting from a support-matched random-sign Chowla realization and changing signs only on sparse, widely separated intervals

\[
I_j=(N_j,N_j+L_j],
\qquad
L_j=\left\lfloor\frac{N_j}{\log N_j}\right\rfloor,
\tag{7}
\]

with the intervals separated rapidly enough that their union has natural density zero.

At the beginning of the `j`-th block, put

\[
\sigma_j=
\begin{cases}
+1,&A(N_j)\ge0,\\
-1,&A(N_j)<0,
\end{cases}
\tag{8}
\]

and set

\[
a(n)=\sigma_j q(n)
\qquad(n\in I_j).
\tag{9}
\]

Outside the sparse union the original Chowla realization is unchanged. As proved in `MC-004`, a density-zero perturbation changes every fixed finite Chowla correlation on only `o(X)` starting indices, so the full qualitative Chowla property survives, while (1) is preserved pointwise.

Let

\[
X_j=N_j+L_j,
\qquad
Y_j=X_j+1,
\tag{10}
\]

and denote by

\[
Q_j=\sum_{N_j<n\le X_j}q(n)
\tag{11}
\]

the number of square-free integers in the coherent block. The classical square-free counting estimate used in `MC-004` gives

\[
Q_j
=\left(\frac6{\pi^2}+o(1)\right)L_j
=\left(\frac6{\pi^2}+o(1)\right)
\frac{Y_j}{\log Y_j}.
\tag{12}
\]

The same block that created the large endpoint bias in `MC-004` therefore contains a positive-density set of nonzero increments, all with the same sign relative to the current partial sum.

## 2. Coherent blocks force large mean-absolute area

For `0<=t<=L_j`, define

\[
Q_j(t)=\sum_{N_j<n\le N_j+t}q(n).
\tag{13}
\]

The sign choice (8) gives the exact identity

\[
A(N_j+t)
=
\sigma_j\bigl(|A(N_j)|+Q_j(t)\bigr),
\tag{14}
\]

including the case `A(N_j)=0`. Hence

\[
|A(N_j+t)|\ge Q_j(t).
\tag{15}
\]

Summing over the block,

\[
Y_jD_a(Y_j)
=\sum_{k=0}^{X_j}|A(k)|
\ge
\sum_{t=1}^{L_j}Q_j(t).
\tag{16}
\]

For any binary sequence of length `L_j` with exactly `Q_j` ones, the sum of its cumulative counts is minimized when all ones occur as late as possible. Therefore

\[
\sum_{t=1}^{L_j}Q_j(t)
\ge
1+2+\cdots+Q_j
=
\frac{Q_j(Q_j+1)}2.
\tag{17}
\]

Combining (12), (16), and (17) yields

\[
D_a(Y_j)
\ge
\frac{Q_j(Q_j+1)}{2Y_j}
=
\left(\frac{18}{\pi^4}+o(1)\right)
\frac{Y_j}{(\log Y_j)^2},
\tag{18}
\]

which proves (4).

Thus the same exact-support qualitative-Chowla control from `MC-004` is even worse for the mean-absolute endpoint than the endpoint-only formulation made explicit: it permits almost-linear **integrated absolute mass**, not merely a large value at one terminal index.

For every fixed `c>0`,

\[
\frac{Y/(\log Y)^2}{Y^{1-c}}
=\frac{Y^c}{(\log Y)^2}\to\infty.
\tag{19}
\]

Consequently no fixed power-saving estimate for `D_a(Y)` can follow from exact support plus qualitative Chowla alone.

## 3. The same block forces a near-quadratic excursion square

During the coherent block, once the first square-free position is reached, equation (14) shows that `A(k)` remains nonzero and has fixed sign through `k=X_j`. Let `m_j` be that first square-free position. The nonzero excursion containing `[m_j,X_j]` has length at least

\[
X_j-m_j+1.
\tag{20}
\]

All `Q_j` square-free positions of the block lie in `[m_j,X_j]`, so trivially

\[
X_j-m_j+1\ge Q_j.
\tag{21}
\]

Hence one excursion already contributes at least `Q_j^2` to the second moment:

\[
E_{2,a}(Y_j)\ge Q_j^2.
\tag{22}
\]

Using (12),

\[
E_{2,a}(Y_j)
\ge
\left(\frac{36}{\pi^4}+o(1)\right)
\frac{Y_j^2}{(\log Y_j)^2},
\tag{23}
\]

which is (5).

For every fixed `epsilon<1/2`,

\[
\frac{Y^2/(\log Y)^2}{Y^{3/2+\varepsilon}}
=
\frac{Y^{1/2-\varepsilon}}{(\log Y)^2}\to\infty.
\tag{24}
\]

Therefore the sufficient excursion estimate from `MC-014` cannot be obtained from these qualitative fixed-shift inputs as a black box.

## 4. What information the counterexample destroys and what it preserves

The construction deliberately preserves two pieces of Möbius-facing information exactly:

1. the zero set `|a(n)|=mu(n)^2`, hence the square-free support; and
2. every fixed finite qualitative Chowla correlation.

The obstruction works because these data are insensitive to a coherent sign overwrite on a density-zero family of blocks. The blocks are sparse enough to disappear from every fixed correlation limit, but each individual block is long enough to create an excursion of length about `Y/log Y`, producing quadratic excursion mass and almost-linear mean-absolute area.

This is precisely the kind of rare coherent contribution that the line's local-to-global controls warn can be lost under averaging. Here the loss is explicit: the Chowla limits remember asymptotic finite-pattern frequencies but forget a sparse family of anchored blocks whose contribution to `E_2` is quadratic in block length.

The result also explains why replacing the pointwise Mertens target by the Pintz-style mean-absolute endpoint does not by itself make qualitative correlation information quantitatively sufficient. The absolute integral averages in time, but a coherent interval of length `Y/log Y` contributes order `Y/(log Y)^2` after normalization, still above every fixed power-saving scale.

## Prior art and novelty assessment

No new external ingredient is needed beyond the sources already attached to `MC-004` and `MC-014`.

- Shi (`MC-S10`) supplies the qualitative Chowla-sequence framework and the independent random construction used for the exact-support base.
- Pincus and Singer (`MC-S11`) provide adjacent symbolic-dynamics prior art showing that density-zero changes can preserve qualitative normality while allowing arbitrarily slow bias.
- The square-free counting input is the classical estimate recorded as `MC-S12`.
- `MC-004` supplies the exact support-matched sparse-block construction, and `MC-014` supplies the excursion-square statistic and its role in the mean-absolute transfer problem.

A targeted literature search around Chowla sequences, Mertens zero crossings, return times, and excursion lengths did not reveal an established theorem with this exact support-matched sparse-block conclusion. That absence is **not** used as evidence of novelty. Equations (14)–(23) are elementary consequences of the already-persisted construction, so the finding is stored as a line-specific matched-control obstruction and makes no standalone novelty claim.

## Boundaries and failure modes

The decisive missing structure remains multiplicativity. The sparse coherent overwrite in `MC-004` is not multiplicatively consistent. Therefore this finding does **not** show that quantitative or qualitative Chowla information is useless when combined with the full multiplicative identities of Möbius.

It also does not address the strongest currently available quantitative averaged or almost-all results. In particular:

- a uniform polynomial-strength correlation estimate over a growing shift family could detect the sparse blocks even though each fixed qualitative limit cannot;
- multiplicative relations across scales could forbid the block overwrite entirely;
- stronger local information controlling exceptional intervals at polynomial strength could constrain long excursions without passing through fixed-shift Chowla limits;
- the excursion-square bound (6) is sufficient, not necessary, for small mean-absolute area, so ruling out one black-box route to (6) does not rule out other cancellation-respecting carriers.

The sequence `a` is a matched information control, not a model for the actual distribution of Möbius signs. No probabilistic inference about Mertens excursions is drawn from it.

## Consequences for the line

The accepted mean-absolute transfer direction is now narrower.

The following route is decisively ruled out:

```text
exact square-free support
        +
all qualitative fixed-shift Chowla limits
        |
        v
excursion-square bound E_2(N) << N^(3/2+epsilon)
        |
        v
RH-scale mean-absolute cancellation
```

The first implication fails on the explicit control inherited from `MC-004`; in fact that control has `E_2` almost quadratic and `D_a` almost linear along a subsequence.

A surviving approach must therefore identify the extra information that kills sparse coherent excursions. The most concrete remaining candidates are quantitative growing-scale correlation/local estimates with a polynomial information budget, or genuinely multiplicative constraints tying the signs inside a long excursion to data outside it. This is a stricter target than merely asking for more qualitative pseudorandomness.