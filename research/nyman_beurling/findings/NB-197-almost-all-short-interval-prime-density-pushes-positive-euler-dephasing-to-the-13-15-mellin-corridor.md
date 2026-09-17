# NB-197 — Almost-all short-interval prime density pushes positive Euler dephasing to the 13/15 Mellin corridor

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + SPECIFIC-BLOCK + POINTWISE-DEPHASING + NB-196-REFINEMENT`.

`NB-196` converts Guth--Maynard's uniform prime number theorem on intervals of length `x^(17/30+epsilon)` into pointwise dephasing of the true positive Euler shell through the complementary Mellin scale `x^(13/30-epsilon)`. The apparent barrier there is spatial: resolving every cell uniformly forces the mesh to remain above exponent `17/30`.

Guth--Maynard also prove a much shorter **almost-all** interval theorem. Corollary 1.4 resolves intervals of length `x^(2/15+epsilon)` outside an exponentially sparse set of integer starting points. For the normalized positive Euler shell, uniform control of every spatial cell is stronger than necessary. A shifted-grid averaging argument chooses a partition in which the exceptional cells occupy only exponentially small total length. Their entire positive von-Mangoldt mass can then be discarded at `o(1)` cost, uniformly for the Mellin phase.

This gives the same continuum shell asymptotic as `NB-196`, but now uniformly through

\[
\boxed{
1\le |t|\le x_a^{13/15-\epsilon},
\qquad x_a=e^{r_0/a}.
}
\tag{1}
\]

The complementary exponent is now `1-2/15=13/15`. Consequently every fixed positive-return tolerance is excluded pointwise throughout this larger corridor. In the coupled physical-block regime, if

\[
\boxed{
\limsup_{T\to\infty}
\frac{a_T\log(2T)}{r_0}<\frac{13}{15},
}
\tag{2}
\]

then `[T,2T]` is eventually positive-return-free.

The gain is source-specific: an almost-all theorem about the actual prime support is enough because positivity lets the exceptional spatial cells be bounded by their total source mass. It does **not** resolve signed or complex aggregate synthesis, and `13/15` is the complement of the presently imported `2/15` almost-all interval exponent rather than an intrinsic Nyman--Beurling threshold.

## Claim

Fix `r_0>0`, `Delta>0`, and put

\[
x_a=e^{r_0/a},\qquad y_a=e^\Delta x_a.
\tag{3}
\]

Use the exact full von-Mangoldt shell

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=
\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\tag{4}
\]

and define

\[
\mathcal C_a(t):=\sum_n w_{n,a}e^{-it\log n},
\qquad
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\tag{5}
\]

For every fixed `epsilon>0`, uniformly in the corridor (1),

\[
\boxed{
\mathcal C_a(t)
=
e^{-it\log x_a}
\frac{a\bigl(1-e^{-(a+it)\Delta}\bigr)}
{(a+it)(1-e^{-a\Delta})}
+o_{\epsilon,r_0,\Delta}(1)
}
\tag{6}
\]

as `a->0`.

Hence for every fixed `0<eta<1` there exist constants `T_eta>=1` and `a_0>0` such that

\[
0<a<a_0,
\qquad
T_\eta\le |t|\le x_a^{13/15-\epsilon}
\quad\Longrightarrow\quad
\boxed{\mathcal A_a(t)>\eta}.
\tag{7}
\]

The endpoint `13/15` is not claimed. A fixed exponent margin is used both in the almost-all prime theorem and in freezing the Mellin phase on each spatial cell.

## Derivation

### 1. Almost-all prime density can be converted into a mostly-good partition

Guth--Maynard Corollary 1.4 implies the following weakened form, sufficient here. For every fixed `delta>0`, if

\[
X^{2/15+\delta}\le h\le X^{0.99},
\tag{8}
\]

then all but

\[
O_\delta\!\left(Xe^{-c_\delta(\log X)^{1/4}}\right)
\tag{9}
\]

integer starts `u in [X,2X]` satisfy

\[
\pi(u+h)-\pi(u)
=
\frac{h}{\log u}\bigl(1+o_\delta(1)\bigr),
\tag{10}
\]

with an exponentially decaying uniform error after weakening constants. Only the fact that both the exceptional proportion and the relative counting error tend to zero faster than any power of `1/log X` is used below.

Fix the corridor margin `epsilon>0` and choose an integer mesh length

\[
h=\left\lfloor x_a^{2/15+\epsilon/2}\right\rfloor.
\tag{11}
\]

Split the fixed multiplicative shell `[x_a,y_a]` into `O_Delta(1)` slabs `[X,2X]` (with the final slab truncated if necessary). Since `X\asymp_{\Delta}x_a`, the length (11) lies in the admissible range (8), with a smaller fixed margin, for all sufficiently small `a`.

On one such slab, call an integer start *bad* if (10) fails. Consider the `h` residue-class grids with starts congruent to `s mod h`, `0<=s<h`. Every integer start belongs to exactly one such grid. Averaging (9) over `s` therefore gives a shift `s_*` for which the number of bad grid cells is

\[
\ll_\epsilon \frac{X}{h}
 e^{-c_\epsilon(\log X)^{1/4}}.
\tag{12}
\]

Thus the union of bad cells in that shifted partition has total length

\[
\ll_\epsilon
X e^{-c_\epsilon(\log X)^{1/4}}.
\tag{13}
\]

Choose such a shift independently on each of the finitely many slabs. The resulting `O_Delta(1)` boundary fragments have total length `O_Delta(h)` and will be negligible. Crucially, the chosen spatial partitions depend on the source and on `a`, but **not** on `t`; the later Mellin estimate is therefore simultaneous over the whole corridor (1).

### 2. Bad cells carry negligible normalized Euler mass

On a good cell `[u,u+h]`, (10) and the fact that `log p=log u+O(h/u)` for primes in the cell give

\[
\sum_{u<p\le u+h}\log p
=h\bigl(1+o(1)\bigr)
\tag{14}
\]

uniformly over all good cells in the shell.

For the bad cells no cancellation is needed. Their total number of integer sites is bounded by (13), and trivially `Lambda(n)<=log y_a`. Hence their total weighted contribution satisfies

\[
\sum_{\substack{x_a\le n<y_a\\n\text{ in bad cells}}}
\Lambda(n)n^{-1-a}
\ll_{r_0,\Delta}
 e^{-c_\epsilon(\log x_a)^{1/4}}\log x_a
=o(1).
\tag{15}
\]

The omitted continuum integral over the same bad region is also `o(1)`, and the boundary fragments cost

\[
O_\Delta\!\left(\frac{h\log x_a}{x_a}\right)=o(1).
\tag{16}
\]

Corollary 1.4 is stated for primes rather than the full von-Mangoldt measure, but proper prime powers are lower order on this shell. Directly,

\[
\sum_{\substack{x_a\le p^k<y_a\\k\ge2}}
\frac{\log p}{p^{k(1+a)}}
\ll_{r_0,\Delta}
\frac{\log x_a}{\sqrt{x_a}}
=o(1).
\tag{17}
\]

Thus the good-cell prime asymptotic plus (15)--(17) controls the same full positive source appearing in (4), without flattening its support or amplitudes.

### 3. The mostly-good mesh transfers to Mellin frequency `x^(13/15-epsilon)`

Let

\[
f_t(u)=u^{-1-a-it}.
\tag{18}
\]

On any mesh cell with `u\asymp x_a`, the relative variation obeys

\[
\sup_{v\in[u,u+h]}
\frac{|f_t(v)-f_t(u)|}{|f_t(u)|}
\ll
(1+|t|)\frac{h}{x_a}.
\tag{19}
\]

Uniformly for `|t|<=x_a^(13/15-epsilon)`, equations (11) and (19) give

\[
(1+|t|)\frac{h}{x_a}
\ll
x_a^{-13/15+\epsilon/2}
+x_a^{-\epsilon/2}
=o(1).
\tag{20}
\]

On every good cell, freeze `f_t` at its left endpoint, use (14), and compare with the corresponding integral. The sum of these errors remains `o(1)` because the total absolute continuum mass of the fixed log-width shell is bounded. Equations (15)--(17) control everything omitted. Therefore, uniformly over (1),

\[
\sum_{x_a\le n<y_a}
\Lambda(n)n^{-1-a-it}
=
\int_{x_a}^{y_a}u^{-1-a-it}\,du+o(1).
\tag{21}
\]

The same argument at `t=0` gives

\[
D_a
=
\int_{x_a}^{y_a}u^{-1-a}\,du+o(1)
=
e^{-r_0}\frac{1-e^{-a\Delta}}a+o(1)
=
e^{-r_0}\Delta+o(1).
\tag{22}
\]

The numerator integral is explicit:

\[
\int_{x_a}^{y_a}u^{-1-a-it}\,du
=
x_a^{-a-it}
\frac{1-e^{-(a+it)\Delta}}{a+it}.
\tag{23}
\]

Dividing (23) by (22) proves the uniform asymptotic (6). The improvement over `NB-196` is exactly the shift from a mesh that must be good everywhere at scale `x^(17/30+epsilon)` to a shifted mesh whose bad portion has vanishing total source mass at scale `x^(2/15+epsilon)`.

### 4. Continuum dephasing excludes every positive return in the corridor

For `|t|>=1` and sufficiently small `a`, the continuum factor in (6) satisfies

\[
\left|
\frac{a(1-e^{-(a+it)\Delta})}
{(a+it)(1-e^{-a\Delta})}
\right|
\le
\frac{C_\Delta}{|t|}.
\tag{24}
\]

Choose `T_eta` so large that `C_Delta/T_eta<(1-eta)/2`. By the uniform `o(1)` in (6), for sufficiently small `a` we then have

\[
|\mathcal C_a(t)|<1-\eta
\tag{25}
\]

throughout the range in (7). But positivity of the weights gives

\[
\mathcal A_a(t)\le\eta
\quad\Longrightarrow\quad
|1-\mathcal C_a(t)|\le\eta
\quad\Longrightarrow\quad
|\mathcal C_a(t)|\ge1-\eta.
\tag{26}
\]

This contradicts (25), proving (7).

### 5. Coupled physical-block consequence

Assume `a_T->0` and (2). Choose a fixed `epsilon>0` such that eventually

\[
\frac{a_T\log(2T)}{r_0}
<
\frac{13}{15}-\epsilon.
\tag{27}
\]

Since `log x_{a_T}=r_0/a_T`, equation (27) is equivalent to

\[
2T<x_{a_T}^{13/15-\epsilon}.
\tag{28}
\]

Also `T>=T_eta` eventually. Applying (7) pointwise therefore excludes positive `eta`-returns at every `t in [T,2T]` for all sufficiently large `T`.

## Stress tests and limits

The almost-all spatial theorem does **not** itself provide pointwise control on every short interval. The shifted-grid averaging is the load-bearing extra step: it turns an exceptional set of starting points into a partition whose bad cells have negligible *total positive source mass*. This use of positivity is why the conclusion remains pointwise in `t` despite an almost-all input in the spatial variable.

The selected grid shifts need not be canonical and can vary with `a` and with the finitely many dyadic slabs. That causes no quantifier problem because the partitions are only a proof device; the shell sum is unchanged, and the chosen shifts are independent of `t`.

The exponent `13/15` is not claimed as intrinsic. It is the reciprocal-resolution complement of Guth--Maynard's current almost-all short-interval exponent `2/15`. Any improvement of that source theorem would feed directly into the same argument. Conversely, this finding does not say that positive returns exist beyond this corridor.

Most importantly, this remains an obstruction to **positive** shell recurrence. Signed or complex aggregate acquisition can cancel bad-cell mass rather than paying its absolute mass, so (15) does not by itself constrain the source-faithful signed synthesis frontier identified after `NB-187`--`NB-193`. No claim about the full Nyman realized range, the optimal approximation distance, or RH follows from (6)--(7).

## Prior-art boundary

The only new load-bearing external input beyond `NB-196` is a different corollary of the same Guth--Maynard paper: Corollary 1.4 gives a prime number theorem for almost all intervals down to length `x^(2/15+epsilon)`, with an exponentially sparse exceptional set. The passage from that theorem to (21) is derived here by shifted-grid averaging, positivity of the von-Mangoldt source, and an elementary cellwise Mellin approximation. Searches for short-interval prime results combined with Mellin/Dirichlet-polynomial dephasing did not locate this exact positive-shell transfer.

`SOURCES.md` therefore needs no new bibliography entry, but its Guth--Maynard anchor is expanded to record the Corollary 1.4 dependency and the distinct role it plays here.