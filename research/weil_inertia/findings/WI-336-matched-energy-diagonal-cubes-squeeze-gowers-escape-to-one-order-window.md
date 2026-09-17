# WI-336 — matched-energy diagonal cubes squeeze the Gowers escape to one critical order

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED + CLASSICAL-IDENTITY`.

WI-334 and WI-335 show that very strong local Gowers-uniformity information can coexist with the full diagonal-scale sliding variance required by the unresolved WI-195 bow gate. There is also an obstruction in the opposite direction that becomes decisive once the Gowers order is allowed to grow: for a source with the relevant `L^2` energy, the zero-increment cubes inside the Gowers norm impose a deterministic floor. Consequently ordinary normalized `U^s=o(1)` cannot persist arbitrarily far up the hierarchy.

Together, the probabilistic obstruction and the deterministic energy floor squeeze the possible black-box Gowers-smallness escape to an asymptotically one-order window. Write

\[
R_s(L,N):=\frac{2^s\log\log N}{\log L}.
\tag{1}
\]

For every fixed `eta>0` and fixed-power scale `L\asymp K=N^{\kappa+o(1)}`:

- there are matched-energy Rademacher models with `U^s=o(1)` simultaneously on every `K`-scale interval for all orders with `R_s(K,N)\le 1-\eta`, while their prescribed-carrier sliding variance remains `(1+o(1))NK\log N`;
- for **every** sequence on an interval with energy `\sum_I|f|^2\ge cL\log N`, ordinary normalized `U^s(I)=o(1)` is impossible once `R_s(L,N)\ge 2+\eta`; indeed the norm then diverges at least as a positive power of `\log N`.

Since increasing `s` by one doubles `R_s`, the unresolved region between the two statements has asymptotic width only one binary Gowers-order step, up to fixed margins and endpoint effects. This does not prove that the remaining critical order is sufficient. It shows that the route “keep increasing the Gowers order while asking for smallness of the same normalized norm” has almost exhausted its available scale: below the critical strip generic countermodels survive, while above it diagonal cubes themselves prevent smallness. A viable continuation must either exploit the narrow critical order quantitatively, renormalize/remove the diagonal inside a different statistic, or use source-specific signed arithmetic covariance.

## 1. Deterministic diagonal-cube energy floor

Let `I` be an integer interval of length `L`, let `f` be supported on `I`, and use the normalized interval convention appearing in the MRSTT short-interval results,

\[
\|f\|_{U^s(I)}
:=
\frac{\|f1_I\|_{U^s(\mathbb Z)}}
     {\|1_I\|_{U^s(\mathbb Z)}}.
\tag{2}
\]

Put

\[
E:=\sum_{n\in I}|f(n)|^2,
\qquad
Q_s(f):=\|f\|_{U^s(\mathbb Z)}^{2^s}.
\tag{3}
\]

Then for every integer `s>=2`,

\[
\boxed{
\|f\|_{U^s(I)}
\ge
\sqrt{\frac{E}{2L}}\,L^{-1/2^s}.
}
\tag{4}
\]

The proof uses only the recursive Gowers identity and nonnegativity. In the recurrence

\[
Q_s(f)=\sum_h Q_{s-1}(f\,\overline{T_hf}),
\tag{5}
\]

every summand is nonnegative. Keeping only `h=0` gives

\[
Q_s(f)\ge Q_{s-1}(|f|^2).
\tag{6}
\]

We need a lower bound for the right-hand side that does not assume any distribution of the energy inside `I`.

### Nonnegative cube lemma

If `g>=0` is supported on an interval of length `L`, then for every `d>=1`,

\[
\boxed{
Q_d(g)
\ge
2^{-(2^d-d-1)}
\frac{\left(\sum g\right)^{2^d}}
     {L^{2^d-d-1}}.
}
\tag{7}
\]

For `d=1` this is the identity `Q_1(g)=(\sum g)^2`. Suppose it holds for `d-1` and write `q=2^{d-1}` and

\[
C_h:=\sum_x g(x)g(x+h).
\tag{8}
\]

Applying the induction hypothesis to `g_h(x)=g(x)g(x+h)`, whose support is contained in an interval of length at most `L`, gives

\[
Q_{d-1}(g_h)
\ge
2^{-(q-d)}\frac{C_h^q}{L^{q-d}}.
\tag{9}
\]

There are at most `2L-1` shifts with `C_h\ne0`, while

\[
\sum_h C_h=\left(\sum g\right)^2.
\tag{10}
\]

Hölder therefore yields

\[
\sum_h C_h^q
\ge
\frac{(\sum g)^{2q}}{(2L)^{q-1}}.
\tag{11}
\]

Summing (9) over `h` proves (7), since the constants obey

\[
2^{-(q-d)}2^{-(q-1)}
=2^{-(2^d-d-1)}.
\tag{12}
\]

Now set `d=s-1` and `g=|f|^2`. Equations (6)--(7) give

\[
Q_s(f)
\ge
2^{-(2^{s-1}-s)}
\frac{E^{2^{s-1}}}{L^{2^{s-1}-s}}.
\tag{13}
\]

For the denominator in (2), every cube lying in `I` has its base point in one of `L` positions and each increment in an interval of fewer than `2L` integers. Hence

\[
Q_s(1_I)\le L(2L)^s=2^sL^{s+1}.
\tag{14}
\]

Dividing (13) by (14) gives the particularly simple form

\[
\frac{Q_s(f)}{Q_s(1_I)}
\ge
\frac1L\left(\frac{E}{2L}\right)^{2^{s-1}}.
\tag{15}
\]

Taking the `2^{-s}` power is exactly (4).

## 2. Matched source energy forces high-order norms to become large

Assume now that the local source has the bow-relevant energy scale

\[
E\ge cL\log N
\tag{16}
\]

for some fixed `c>0`. From (4),

\[
\log\|f\|_{U^s(I)}
\ge
\frac12\log\log N
-\frac{\log L}{2^s}
+O_c(1).
\tag{17}
\]

In terms of (1),

\[
\log\|f\|_{U^s(I)}
\ge
\left(\frac12-\frac1{R_s(L,N)}\right)\log\log N
+O_c(1).
\tag{18}
\]

Therefore, for every fixed `eta>0`,

\[
R_s(L,N)\ge2+\eta
\quad\Longrightarrow\quad
\|f\|_{U^s(I)}
\ge
(\log N)^{\eta/(2(2+\eta))+o(1)}.
\tag{19}
\]

The important point is logical rather than the exact exponent: at this order ordinary normalized Gowers **smallness is incompatible with the required quadratic energy before any arithmetic information is used**. The obstruction is the family of zero-increment/degenerate cubes already present in the norm.

This also explains why a hypothetical extension of a fixed-order theorem to all orders tending to infinity cannot simply retain the same statement `\|f\|_{U^s(I)}=o(1)` while preserving the source normalization. At sufficiently high order the statement contradicts (4).

## 3. WI-335 can be sharpened from `o(log log K)` to every fixed margin below the critical ratio

WI-335 chose a convenient hierarchy satisfying

\[
2^{S_N}\log\log N=o(\log K).
\tag{20}
\]

The same probabilistic proof actually reaches every fixed margin below ratio one. Fix `eta\in(0,1)` and let `S_N` satisfy

\[
2^{S_N}\log\log N\le(1-\eta)\log K.
\tag{21}
\]

Let `epsilon_n` be independent Rademacher signs, set

\[
b_n=\sqrt{\log N}\,\varepsilon_n,
\tag{22}
\]

and retain WI-335's notation

\[
F_{s,I}
:=
\frac{\|\varepsilon1_I\|_{U^s(\mathbb Z)}^{2^s}}
     {\|1_I\|_{U^s(\mathbb Z)}^{2^s}}.
\tag{23}
\]

The explicit cube count and bounded-difference estimates from WI-335 are uniform in this range:

\[
\mathbb E F_{s,I}\le\frac{(Cs)^s}{|I|},
\qquad
|\Delta_rF_{s,I}|\le\frac{(Cs)^s}{|I|},
\tag{24}
\]

and hence, for `K<=|I|<=2K`,

\[
\mathbb P(F_{s,I}-\mathbb EF_{s,I}>t)
\le
\exp\!\left(-\frac{2|I|t^2}{(Cs)^{2s}}\right).
\tag{25}
\]

Choose

\[
a:=\frac{1-\eta/2}{2},
\qquad 0<a<\frac12,
\qquad t:=K^{-a}.
\tag{26}
\]

Condition (21) implies `s=O(\log\log N)`, so

\[
(Cs)^{2s}=K^{o(1)}.
\tag{27}
\]

Thus the expectation in (24) is `K^{-1+o(1)}=o(K^{-a})`, while the exponent in (25) is

\[
K^{1-2a-o(1)}=K^{\eta/2-o(1)}.
\tag{28}
\]

A union bound over all `O(NK)` intervals of lengths in `[K,2K]` and all `s<=S_N` therefore gives, with probability `1-o(1)`,

\[
F_{s,I}\le2K^{-a}
\tag{29}
\]

simultaneously for every such interval and every retained order.

After the energy normalization (22),

\[
\log\|b\|_{U^s(I)}
\le
\frac12\log\log N
-\frac{a\log K}{2^s}
+o(\log\log N).
\tag{30}
\]

Using (21),

\[
\frac{a\log K}{2^s}
\ge
\frac{1-\eta/2}{2(1-\eta)}\log\log N,
\tag{31}
\]

so

\[
\boxed{
\sup_{\substack{I\subset[1,N]\text{ interval}\\K\le|I|\le2K}}
\sup_{2\le s\le S_N}
\|b\|_{U^s(I)}
\le
(\log N)^{-\eta/(4(1-\eta))+o(1)}
=o(1).
}
\tag{32}
\]

The sliding-square argument in WI-335 does not depend on `S_N`. For any prescribed unit-modulus carrier `u_n`, the same high-probability event can therefore be intersected with

\[
\boxed{
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^K b_{x+j}u_{x+j}\right|^2
=(1+o(1))NK\log N.
}
\tag{33}
\]

Thus every fixed-margin hierarchy below `R_s=1` is still insufficient as a black-box implication from local norm smallness to bow-variance cancellation.

## 4. The remaining generic Gowers-smallness strip has width one order

Combine (19) and (32). For a matched-energy source on a fixed-power interval:

\[
\begin{array}{ll}
R_s\le1-\eta:
&\text{generic all-interval countermodels with full diagonal variance exist},\\[2mm]
R_s\ge2+\eta:
&\text{normalized }U^s=o(1)\text{ is deterministically impossible}.
\end{array}
\tag{34}
\]

The ratio `R_s` doubles when `s` is incremented once. Therefore the unresolved band between the two statements is asymptotically only one Gowers-order step. This is sharper than saying merely that a Gowers-only route must reach “order about `log log K`”: the hierarchy reaches a point where its own diagonal degeneracies force a change of observable almost immediately after the random-model obstruction stops being proved by the present concentration argument.

No sufficiency claim is made in the strip

\[
1\lesssim R_s\lesssim2.
\tag{35}
\]

A stronger concentration theorem for random cubes could narrow it from below; a stronger deterministic diagonal estimate could narrow it from above. Conversely, a genuinely arithmetic theorem at the critical order could still be useful even when the normalized norm is not `o(1)`, provided it yields information beyond black-box smallness.

## 5. Consequence for the distinguished-bow clue

The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` asks for a signed two-point statement at the actual bow twist, strong enough to cancel a diagonal of order `XK\log X`. WI-334 and WI-335 already show that generic uniformity is not such a statement. The present result narrows the last obvious “just increase the order” escape in both directions.

Below the critical strip, arbitrarily rich growing-order norm smallness still admits a model retaining the whole diagonal. Above the strip, the matched source energy itself forces the ordinary normalized norm to be large. Thus a useful higher-order continuation must change what information is retained: for example a diagonal-renormalized cube statistic, a signed covariance identity before Cauchy--Schwarz/absolute-value losses, a relative arithmetic linear-forms statement, or another source-specific invariant. None of those possibilities is ruled out here.

In particular, this result does **not** establish the desired prime off-diagonal sign, does not show that the actual `Lambda-Lambda^sharp` bow variance is diagonal-sized, and does not convert a density statement into exclusion of individual off-critical zeros. It is an interface barrier telling us where generic Gowers-smallness information ceases to be a plausible carrier for the needed defect-elimination mechanism.

## 6. Prior-art and novelty audit

The arithmetic theorem surface being tested is the established fixed-order work of Matomäki, Radziwiłł, Shao, Tao and Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`. Their theorem quantifies over each fixed Gowers order; it does not assert a hierarchy with `s=s(N)` and does not conflict with the high-order energy floor above.

The recursive identity (5), positivity of the Gowers cube form, and the fact that random functions are basic small-uniformity models are classical higher-order Fourier-analysis ingredients. A bounded prior-art search around diagonal/degenerate-cube lower bounds, random high-order Gowers norms, and growing-order concentration did not locate the combined line-specific statement (4), (32), and the one-order squeeze (34). No priority claim is made for the elementary ingredients or for the probabilistic method. The Mathia delta is the exact interface conclusion obtained by putting the deterministic matched-energy floor against the sharpened all-interval WI-335 countermodel.

## 7. Boundary conditions and decisive audit tests

This finding must be narrowed if any of the following checks fails.

1. Verify the unnormalized recurrence (5) for the exact `U^s(\mathbb Z)` convention used by MRSTT and that the `h=0` term is exactly `Q_{s-1}(|f|^2)`.
2. Recheck the induction in (7), especially the support length, the identity `\sum_h C_h=(\sum g)^2`, the `2L-1` shift count, and the exponent `2^d-d-1`.
3. Verify the denominator bound (14) directly from the condition that all singleton vertices `x+h_j` lie in `I`.
4. For the probabilistic half, repeat WI-335's cube-sensitivity count with `t=K^{-a}` and verify that (28) dominates the polynomial number of intervals and the `O(\log\log N)` hierarchy depth.
5. Check the threshold algebra in (30)--(32); the fixed margin is essential because the present concentration proof requires `a<1/2`.
6. Independently recheck that the full sliding-variance event (33) remains high probability and can be intersected with the simultaneous Gowers event.

The local energy hypothesis (16) is essential to the deterministic side. The result also leaves the critical strip (35) open and says nothing against arithmetic information not encoded by ordinary normalized Gowers smallness. These are genuine escape routes, not technical footnotes.
