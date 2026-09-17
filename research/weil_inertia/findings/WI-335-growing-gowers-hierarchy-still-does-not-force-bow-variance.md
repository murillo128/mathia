# WI-335 — a growing Gowers hierarchy still does not force bow variance cancellation

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED + PRIOR-ART-REDIRECT`.

WI-334 proves that every **fixed finite** hierarchy of local Gowers norms can be power-small on all bow-scale intervals while the WI-195 sliding square remains at full diagonal scale. The same probabilistic construction can be pushed much further. The order may grow with the ambient scale almost as fast as `log_2 log K`, and the obstruction still survives.

Precisely, fix

\[
0<\kappa<1,
\qquad
K=\lfloor N^\kappa\rfloor,
\]

and any deterministic unit-modulus carrier `u_n`. Define

\[
S_N
:=
\left\lfloor
\log_2\!\left(\frac{\log K}{(\log\log N)^2}\right)
\right\rfloor
\tag{1}
\]

whenever the quantity inside the logarithm exceeds `1`. Then for all sufficiently large `N` there is a real sequence

\[
b_n=\sqrt{\log N}\,\varepsilon_n,
\qquad
\varepsilon_n\in\{-1,+1\},
\tag{2}
\]

such that simultaneously:

\[
\boxed{
\sup_{\substack{I\subset[1,N]\text{ interval}\\K\le |I|\le2K}}
\ \sup_{2\le s\le S_N}
\|b\|_{U^s(I)}=o(1),
}
\tag{3}
\]

while

\[
\boxed{
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^{K}b_{x+j}u_{x+j}\right|^2
=(1+o(1))NK\log N.
}
\tag{4}
\]

Since

\[
S_N
=
\log_2\log K
-2\log_2\log\log N
+O(1)
=
(1-o(1))\log_2\log K,
\tag{5}
\]

this rules out substantially more than the fixed-order shortcut. Any argument whose only source information is vanishing local Gowers norms through orders `s<=S_N` can still coexist with the entire bow diagonal. A pure Gowers-hierarchy escape from WI-334 therefore cannot merely let the order drift slowly to infinity: it must reach essentially the `log_2 log K` scale (or use quantitatively stronger/arithmetic information not encoded by norm smallness alone).

This is an information-interface obstruction, not a statement about the actual sequence `Lambda-Lambda^sharp`. It does not preclude a signed shifted-prime covariance theorem, a source identity before absolute values/Cauchy--Schwarz, a relative linear-forms estimate using the prime majorant, or some theorem at/above the threshold in (5). It does show that the `K`-dependent-order escape explicitly left open by WI-334 remains blocked through an asymptotically maximal sub-`log log` hierarchy.

## 1. Exact interface and normalization

The unresolved WI-195 source gate has the schematic form

\[
\int_X^{2X}
\left|
\sum_{x<n\le x+K}
(\Lambda(n)-\Lambda_X^\sharp(n))n^{iU}
\right|^2dx
=o(XK\log X).
\tag{6}
\]

Its raw diagonal is of order `XK log X`. WI-334 tests exactly whether local Gowers uniformity, treated as a black-box pseudorandomness input, forces the off-diagonal cancellation needed to remove that diagonal. The model (2) uses the same quadratic-energy normalization:

\[
\sum_{n\le N}|b_n|^2=N\log N.
\tag{7}
\]

The Gowers norm is the interval normalization used by Matomäki--Radziwiłł--Shao--Tao--Teräväinen (MRSTT):

\[
\|f\|_{U^s(I)}
=
\frac{\|f1_I\|_{U^s(\mathbb Z)}}
{\|1_I\|_{U^s(\mathbb Z)}}.
\tag{8}
\]

The only strengthening relative to WI-334 is that `s` is no longer fixed before `N->infinity`.

## 2. Explicit cube bounds remain uniform for `s` of order `log log N`

Let `epsilon_n` be independent Rademacher signs. For an integer interval `I` of length `L`, put

\[
Q_{s,I}
:=\|\varepsilon1_I\|_{U^s(\mathbb Z)}^{2^s},
\qquad
D_{s,I}
:=\|1_I\|_{U^s(\mathbb Z)}^{2^s},
\qquad
F_{s,I}:=Q_{s,I}/D_{s,I}.
\tag{9}
\]

The point of keeping the elementary constants visible is that the fixed-`s` notation `O_s(1)` in WI-334 can then be allowed to grow.

For `L` sufficiently large compared with `s`, restrict the cube count defining `D_{s,I}` to base points in the middle half of `I` and increments satisfying

\[
|h_j|\le \frac{L}{8s}.
\]

Every vertex then remains in `I`. Consequently there is an absolute constant `C>=2` such that

\[
D_{s,I}\ge \frac{L^{s+1}}{(Cs)^s}.
\tag{10}
\]

For the numerator, a Rademacher cube monomial has nonzero expectation only if every sign index appears an even number of times. In particular two distinct cube vertices must coincide. For a fixed pair `omega != omega'`, the collision imposes

\[
(\omega-\omega')\cdot h=0.
\tag{11}
\]

All `h_j` lie in `[-L,L]` whenever the cube lies in `I`. After choosing `s-1` increments and the base point, (11) determines one remaining increment because some coefficient is `+1` or `-1`. Summing over fewer than `2^{2s}` vertex pairs gives, after enlarging `C`,

\[
\mathbb E Q_{s,I}\le C^sL^s,
\qquad
\boxed{
\mathbb EF_{s,I}
\le \frac{(Cs)^s}{L}.
}
\tag{12}
\]

Now flip one sign `epsilon_r`. A cube can change only if it contains `r`. For each of its `2^s` possible vertices, choosing the `s` increments determines the base point; hence at most `2^s(2L+1)^s` relevant cubes occur. Combining this with (10) gives the bounded-difference estimate

\[
\boxed{
|\Delta_rF_{s,I}|
\le \frac{(Cs)^s}{L}
}
\tag{13}
\]

for another absolute `C`.

McDiarmid's inequality therefore yields

\[
\mathbb P\!\left(
F_{s,I}-\mathbb EF_{s,I}>t
\right)
\le
\exp\!\left(
-\frac{2Lt^2}{(Cs)^{2s}}
\right).
\tag{14}
\]

Take `t=K^{-1/4}` and `K<=L<=2K`. For every `s<=S_N`, (1) implies `s=O(log log N)`, hence

\[
(Cs)^{2s}
=
\exp(O(s\log s))
=N^{o(1)}
=K^{o(1)}.
\tag{15}
\]

Also (12) is `K^{-1+o(1)}=o(K^{-1/4})`. Thus

\[
\mathbb P\!\left(F_{s,I}>2K^{-1/4}\right)
\le
\exp(-K^{1/2-o(1)}).
\tag{16}
\]

There are only `O(NK)` integer intervals with length in `[K,2K]`, and only `S_N=O(log log N)` orders under consideration. A union bound in (16) shows that with probability `1-o(1)`, simultaneously for every such interval and every `2<=s<=S_N`,

\[
F_{s,I}\le2K^{-1/4}.
\tag{17}
\]

No fixed-order constant is being hidden in this union: (10)--(15) explicitly show that its growth is subpower throughout the selected hierarchy.

## 3. The source-scale normalization still drives every one of those norms to zero

From (8), (9), and (17),

\[
\|b\|_{U^s(I)}
\le
\sqrt{\log N}\,
(2K^{-1/4})^{1/2^s}.
\tag{18}
\]

The worst case is the largest order. By (1),

\[
2^{S_N}
\le
\frac{\log K}{(\log\log N)^2}.
\tag{19}
\]

Therefore, uniformly for `s<=S_N`,

\[
\begin{aligned}
\log \|b\|_{U^s(I)}
&\le
\frac12\log\log N
+\frac{\log2-\frac14\log K}{2^s}\\
&\le
\frac12\log\log N
-\frac14(\log\log N)^2
+o((\log\log N)^2)
\longrightarrow-\infty.
\end{aligned}
\tag{20}
\]

This proves (3).

The particular square in `(log log N)^2` is only a convenient margin. The same argument works for any integer sequence `S_N` satisfying

\[
\boxed{
2^{S_N}\log\log N=o(\log K).
}
\tag{21}
\]

Indeed, (21) already implies `S_N=O(log log K)` and hence the subpower constant control (15), while (18) then tends to zero. Thus the obstruction reaches every order hierarchy

\[
S_N
\le
\log_2\log K
-\log_2\log\log N
-\omega(1).
\tag{22}
\]

Equation (1) is kept as the clean explicit representative.

## 4. The sliding square remains diagonal-sized

For completeness, the second half of WI-334 is unchanged and is uniform in the choice of hierarchy. Let

\[
S_x:=\sum_{j=1}^{K}\varepsilon_{x+j}u_{x+j},
\qquad
V:=\sum_{x=0}^{N-K}|S_x|^2.
\tag{23}
\]

Independence and `|u_n|=1` give

\[
\mathbb EV=(N-K+1)K.
\tag{24}
\]

A fourth-moment expansion gives `E|S_x|^4<=3K^2`. Windows at distance at least `K` are independent; only `O(NK)` pairs overlap, and Cauchy--Schwarz bounds each remaining covariance by `O(K^2)`. Hence

\[
\operatorname{Var}(V)=O(NK^3).
\tag{25}
\]

Since `K/N->0`, Chebyshev yields

\[
V=(1+o(1))NK
\tag{26}
\]

with probability `1-o(1)`. This high-probability event intersects the simultaneous growing-order event (17). Selecting one realization and multiplying by `sqrt(log N)` proves (4).

As in WI-334, the same conclusion holds for the corresponding continuous sliding integral up to harmless endpoint terms because the discrete window sum is piecewise constant between consecutive integer starts.

## 5. What threshold has actually been proved

The conclusion is not that `U^s` information becomes sufficient at `s~log_2 log K`. Nothing here proves sufficiency at any order. The exact negative statement is:

\[
\boxed{
\text{vanishing local }U^s\text{ norms for every }
2\le s\le S_N,
\quad
2^{S_N}\log\log N=o(\log K),
}
\]

can coexist with the full diagonal-scale sliding variance (4).

For the fixed-power bow windows `K=N^{kappa+o(1)}`, this means `S_N=(1-o(1))log_2 log K` is still insufficient as a black-box hierarchy. Therefore a Gowers-only strategy that hopes to evade WI-334 by making the order depend on the scale must cross a sharply quantified complexity barrier: it needs information at essentially `log log K` order, or it must exploit extra arithmetic relations that the norm list forgets.

This also explains why the published MRSTT theorem cannot be promoted to the bow `L^2` gate merely by saying “take `s` sufficiently large.” Their 2026 Gowers theorem quantifies over each **fixed** integer `s`; it does not provide a uniform theorem with `s=s(X)` tending to infinity, and the present countermodel shows that even a substantial hypothetical extension into the growing-order regime would still be insufficient if its output were only norm smallness of the form (3).

## 6. Prior-art and novelty audit

The external arithmetic input whose interface is being tested is established prior art:

Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`. Their Theorem 1.3 proves short-interval Gowers uniformity for every **fixed** order `s` in the prime case above the `X^(1/3+epsilon)` threshold. The theorem does not claim order uniformity as `s` grows with `X`.

Random functions as the baseline small-Gowers model are classical. Fouvry--Kowalski--Michel, **An inverse theorem for Gowers norms of trace functions over prime fields**, *Math. Proc. Cambridge Philos. Soc.* 155 (2013), 277--295, explicitly compare their trace-function examples with Gowers norms of random functions. General inverse-theorem literature likewise treats small fixed-order Gowers norm as a quasirandomness notion. A fresh bounded search around random Boolean/Rademacher functions, growing-order Gowers norms, and pseudorandomness found this general principle but did not locate the line-specific statement (3)--(4) or a published threshold matching (21). No priority claim is made for the probabilistic ingredients.

The Mathia delta is the **quantitative growing-order continuation of WI-334**: tracking the `s`-dependence in the cube count and bounded-difference constants shows that the countermodel survives not just every fixed hierarchy but all hierarchy depths below the near-`log log K` threshold (21). That converts WI-334's qualitative escape clause “perhaps let the Gowers order grow with `N`” into a much narrower requirement.

## 7. Boundary conditions and decisive audit tests

This finding is falsified or must be narrowed if any of the following checks fails.

1. In (10), verify that the restricted base points/increments indeed keep all `2^s` vertices inside `I` uniformly for `s<=S_N`, including the harmless integer-floor losses.
2. In (12), verify that every nonzero Rademacher expectation has a repeated cube vertex and that one vertex collision imposes a nontrivial linear equation with a coefficient `+1` or `-1`, giving at most `L(2L+1)^(s-1)` solutions for that pair.
3. In (13), count all cubes containing a flipped site and check that division by (10) gives sensitivity at most `(Cs)^s/L` for an absolute `C`.
4. Check that (21) implies both `(Cs)^(2s)=K^(o(1))` and the decay in (18), so the union bound is genuinely uniform over every interval and every growing order retained.
5. Independently reproduce (24)--(26), including the `O(NK^3)` overlap variance, and intersect the two high-probability events.

The model deliberately does not satisfy prime-specific singular-series identities, positivity of `Lambda`, the exact `Lambda^sharp` structure, or any signed shifted-prime theorem. Those are valid ways to evade the obstruction. Therefore this result must not be read as evidence that the actual bow variance is diagonal-sized.

## Research consequence

The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` becomes more restrictive. WI-334 already ruled out finite PET/fixed-order Gowers uniformity as a standalone solution. WI-335 now rules out the same black-box strategy even if the available local hierarchy grows through

\[
(1-o(1))\log_2\log K
\]

orders. The live source-side targets are consequently the ones that carry information absent from generic norm smallness: a **signed two-point covariance at the distinguished carrier**, a source-fixed subtraction/identity before norm losses, or genuinely prime-specific relative structure. Merely extending existing higher-uniformity technology from fixed order to a slowly growing order would not by itself cross the WI-195 gate.