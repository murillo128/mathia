# WI-340 — sparse cube deletion does not lower the renormalized Gowers chaos floor

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-IDENTITY`.

**Parent findings:** WI-338, WI-339.

WI-339 removes the literal zero-increment contribution from the growing-order Gowers cube statistic and shows that the matched-energy Rademacher obstruction still survives until the moving threshold

\[
R_s(K,N):=\frac{2^s\log\log N}{\log K}=s+1.
\]

That leaves a natural repair attempt: perhaps `h_j=0` was too narrow a notion of "diagonal", and one should delete every combinatorially degenerate cube — for example every cube with repeated vertices — before asking for smallness. This finding closes that whole sparse-deletion class.

Let `I` be an integer interval of length `L`, let `s\ge2`, and let `\mathcal C_{s,I}` be the set of additive `s`-cubes

\[
c=(x,h_1,\ldots,h_s)
\]

whose `2^s` vertices `x+\omega\cdot h`, `\omega\in\{0,1\}^s`, all lie in `I`. Write

\[
D_{s,I}:=|\mathcal C_{s,I}|.
\]

Let `\mathcal C^{\mathrm{inj}}_{s,I}` be the subfamily whose `2^s` vertices are pairwise distinct. In the bow regime `L=N^{\kappa+o(1)}` and throughout the growing orders `s=O(\log\log N)`, one has

\[
\boxed{
|\mathcal C_{s,I}\setminus\mathcal C^{\mathrm{inj}}_{s,I}|
=o(D_{s,I}).
}
\tag{1}
\]

Thus **all vertex-collision diagonals occupy only a vanishing fraction of the cube geometry**.

More generally, take any deterministic geometry-only retained family

\[
\mathcal R_{s,I}\subseteq\mathcal C^{\mathrm{inj}}_{s,I},
\qquad
M_{s,I}:=|\mathcal R_{s,I}|,
\qquad
q_{s,I}:=\frac{M_{s,I}}{D_{s,I}}.
\]

For independent Rademacher signs `\varepsilon_n\in\{\pm1\}`, define the full-denominator deleted-cube chaos

\[
P^{\mathcal R}_{s,I}
:=
\frac1{D_{s,I}}
\sum_{c\in\mathcal R_{s,I}}
\prod_{\omega\in\{0,1\}^s}
\varepsilon_{x+\omega\cdot h}.
\tag{2}
\]

Then, uniformly for `s=O(\log\log N)` and `L=N^{\kappa+o(1)}`,

\[
\boxed{
\sqrt{\frac{q_{s,I}}{D_{s,I}}}
\le
\|P^{\mathcal R}_{s,I}\|_2
\le
\sqrt{\frac{q_{s,I}B_s(L)}{D_{s,I}}},
}
\tag{3}
\]

where the character-multiplicity bound already proved in WI-338 gives

\[
B_s(L):=\bigl(2s(1+\log_2L)\bigr)^s=L^{o(1)}.
\tag{4}
\]

Consequently, if the deletion is sparse in the only sense relevant to combinatorial diagonals,

\[
q_{s,I}=1-o(1),
\]

then

\[
\boxed{
\|P^{\mathcal R}_{s,I}\|_2
=L^{-(s+1)/2+o(1)}.
}
\tag{5}
\]

This is exactly the WI-339 chaos scale. Deleting **every repeated-vertex cube**, or indeed deleting any `o(D_{s,I})` deterministic collection of cube configurations, does not change it.

There is also a sharper quantitative statement at the unresolved top strip. With the matched-energy normalization `b_n=\sqrt{\log N}\,\varepsilon_n`, take `L\asymp K=N^{\kappa+o(1)}` and suppose

\[
R_s(K,N)=s+1+O(1).
\tag{6}
\]

The `L^2` chaos scale in (3), after the same `2^{-s}` root used by the normalized Gowers statistic, has logarithm bounded below by

\[
\frac{\log\log N}{2}
\left(1-\frac{s+1}{R_s(K,N)}\right)
+
\frac{\log q_{s,I}}{2^{s+1}}
+o(1).
\tag{7}
\]

At (6), `2^s\asymp\log N`, so the first term is only `O(1)`. Therefore deleting cube terms can make this random-chaos floor tend to zero only if

\[
\boxed{
-\log q_{s,I}\gg 2^s,
}
\tag{8}
\]

and at the top strip this means

\[
\boxed{
q_{s,I}=N^{-\omega(1)}.
}
\tag{9}
\]

Retaining a density-one family, a fixed positive fraction, or even any fixed polynomial fraction `q=N^{-C}` therefore leaves a non-vanishing rooted `L^2` chaos scale at the top transition. A deletion-only repair would have to discard all but a **superpolynomially small fraction** of the generic nondegenerate cubes before it changes the random floor asymptotically.

This does **not** prove that every statistic in the bounded additive strip `R_s=s+1+O(1)` fails to control the bow variance. Equation (3) is an `L^2` statement over the random-sign model, not a deterministic lower bound for every sign realization. The surviving possibility from WI-339 remains real: a statistic that changes or cancels a positive-density family of generic cube monomials, couples several orders, or retains source/carrier-specific signed information could still encode something the present countermodel does not. What is now closed is the simpler idea that one only needs a more exhaustive notion of combinatorial diagonal deletion.

## 1. Repeated-vertex cubes are sparse

A cube fails to be injective exactly when two distinct vertices coincide. If

\[
\omega,\omega'\in\{0,1\}^s,
\qquad
\omega\ne\omega',
\]

then the collision condition is

\[
(\omega-\omega')\cdot h=0.
\tag{10}
\]

Put

\[
d:=\omega-\omega'\in\{-1,0,1\}^s\setminus\{0\}.
\]

There are at most `3^s-1` possible nonzero vectors `d`. Fix one and choose an index `j` with `d_j=\pm1`. Because every vertex lies in an interval of length `L`, each increment satisfies `|h_i|\le L-1`. After choosing `x` and the other `s-1` increments, equation (10) determines `h_j` uniquely if it has an admissible integer value. Hence the number of cubes satisfying the fixed collision equation is at most

\[
L(2L-1)^{s-1}.
\]

The union bound therefore gives

\[
\boxed{
|\mathcal C_{s,I}\setminus\mathcal C^{\mathrm{inj}}_{s,I}|
\le
(3^s-1)L(2L-1)^{s-1}.
}
\tag{11}
\]

WI-338 already supplies the elementary lower bound

\[
D_{s,I}\ge \frac{L^{s+1}}{(Cs)^s}
\tag{12}
\]

for an absolute constant `C`, by restricting the base point to the middle of `I` and all increments to a small box. Combining (11) and (12),

\[
\frac{|\mathcal C_{s,I}\setminus\mathcal C^{\mathrm{inj}}_{s,I}|}
{D_{s,I}}
\le
\frac{(C's)^s}{L}.
\tag{13}
\]

When `s=O(\log\log N)` and `L=N^{\kappa+o(1)}`, the numerator in (13) is `N^{o(1)}`, while `L=N^{\kappa+o(1)}`. This proves (1), in fact with a power saving `L^{-1+o(1)}`.

Thus replacing "delete zero increments" by "delete every cube with any repeated vertex" changes only a vanishing fraction of the cube population at the orders relevant to the bow problem.

## 2. Parseval sees a full-degree chaos on every injective cube

For an injective cube `c`, all `2^s` vertices are distinct. Its Rademacher monomial is therefore the Walsh character

\[
\chi_{A(c)}(\varepsilon)
:=
\prod_{n\in A(c)}\varepsilon_n,
\qquad
|A(c)|=2^s.
\tag{14}
\]

In particular, `A(c)` is nonempty and

\[
\mathbb E\chi_{A(c)}=0.
\tag{15}
\]

For the retained family `\mathcal R_{s,I}`, let `m_A^{\mathcal R}` be the number of retained cubes with vertex set `A`. Then

\[
D_{s,I}P^{\mathcal R}_{s,I}
=
\sum_A m_A^{\mathcal R}\chi_A.
\tag{16}
\]

Orthogonality of Walsh characters gives the exact identity

\[
D_{s,I}^2
\|P^{\mathcal R}_{s,I}\|_2^2
=
\sum_A (m_A^{\mathcal R})^2.
\tag{17}
\]

Since every multiplicity is a nonnegative integer,

\[
\sum_A(m_A^{\mathcal R})^2
\ge
\sum_A m_A^{\mathcal R}
=M_{s,I}.
\tag{18}
\]

This proves the lower half of (3).

For the upper half, deletion cannot increase any character multiplicity:

\[
m_A^{\mathcal R}\le m_A,
\]

and WI-338 proved for every nonconstant cube character

\[
m_A\le B_s(L)
=\bigl(2s(1+\log_2L)\bigr)^s.
\tag{19}
\]

Therefore

\[
\sum_A(m_A^{\mathcal R})^2
\le
B_s(L)
\sum_A m_A^{\mathcal R}
=B_s(L)M_{s,I},
\tag{20}
\]

which finishes (3).

To read off the scale, use the trivial upper count

\[
D_{s,I}\le L(2L)^s
\tag{21}
\]

and the lower count (12). For `s=O(\log\log N)`, all factors depending only subexponentially on `s` are `L^{o(1)}`. Hence when `q=1-o(1)`, (3) becomes exactly (5).

This is the key point that a more literal "remove all diagonals" proposal misses: after all repeated-vertex configurations are removed, almost every surviving term is still a full `2^s`-degree Walsh character, and there are still `D_{s,I}(1-o(1))` such terms. Their orthogonality alone already forces the same random-chaos variance scale.

## 3. Any sparse geometry-only deletion inherits the WI-339 countermodel below the top strip

The preceding argument is not limited to vertex collisions. Suppose a proposed diagonal renormalization selects, for every `(s,I)`, a deterministic retained family `\mathcal R_{s,I}` of injective cubes, independently of the source signs and of the distinguished bow carrier. The polynomial (2) has Walsh degree at most `2^s`, and (20) gives an `L^2` upper bound no larger than the corresponding WI-338/WI-339 scale.

Therefore the same Bonami--Beckner plus union-bound argument used in WI-338 and WI-339 applies without deterioration: for the matched-energy Rademacher source one can simultaneously make the deleted-cube statistic `o(1)` on every `K`-scale interval throughout the regime already covered by WI-339,

\[
R_s(K,N)\le s+1-\rho_N,
\qquad
\rho_N\to\infty,
\tag{22}
\]

while the sliding square against any predetermined unit-modulus carrier remains

\[
(1+o(1))NK\log N.
\tag{23}
\]

Deleting additional deterministic cube configurations therefore cannot repair the implication in the whole region where WI-339 already supplies the all-interval countermodel. It can only weaken the statistic there.

The only potentially interesting place for deletion is the bounded additive transition strip left by WI-339. Equations (7)--(9) show how severe the deletion would have to be even to move the natural Rademacher scale in that strip.

## 4. The top-strip deletion threshold is superpolynomial

Let

\[
K=N^{\kappa+o(1)},
\qquad
\ell_N:=\log\log N,
\qquad
R_s:=\frac{2^s\ell_N}{\log K}.
\]

From the lower bound in (3) and (21),

\[
\|P^{\mathcal R}_{s,I}\|_2
\ge
q_{s,I}^{1/2}
2^{-s/2}K^{-(s+1)/2+o(1)}.
\tag{24}
\]

The matched-energy normalization contributes the factor `\sqrt{\log N}`, and the Gowers root contributes exponent `2^{-s}`. Thus the logarithm of the rooted `L^2` scale is at least

\[
\begin{aligned}
&\frac12\ell_N
+\frac1{2^s}\log\|P^{\mathcal R}_{s,I}\|_2\\
&\qquad\ge
\frac12\ell_N
-\frac{s+1}{2^{s+1}}\log K
+\frac{\log q_{s,I}}{2^{s+1}}
+o(1)\\
&\qquad=
\frac{\ell_N}{2}
\left(1-\frac{s+1}{R_s}\right)
+\frac{\log q_{s,I}}{2^{s+1}}
+o(1).
\end{aligned}
\tag{25}
\]

If `R_s=s+1+O(1)`, then necessarily

\[
s=\log_2\log N+O(1)
\]

and, more precisely,

\[
2^s\asymp\log N.
\tag{26}
\]

The first term in (25) is then only `O(1)`. Hence to force the right side to `-\infty` through deletion alone one needs

\[
\frac{-\log q_{s,I}}{2^s}\to\infty,
\]

which is (8). By (26) this is equivalent to (9).

This does not say that a specially structured deterministic source cannot make (2) small. It says something narrower and robust: **the random-chaos floor itself is insensitive to every diagonal deletion that leaves even a polynomial fraction of generic cubes**. So the bounded top strip cannot be made harmless merely by broadening "diagonal" from zero increments to collisions, repeated vertices, or any other sparse geometry-defined exceptional family.

## 5. Prior-art and novelty audit

The ingredients are deliberately elementary and their provenance is clear.

- The additive-cube/Gowers formalism is classical. The Walsh-character expansion, Parseval identity and Bonami--Beckner concentration used for this line were already made load-bearing in WI-338.
- The distinction between statistics over all tuples and over tuples with distinct entries is classical in the `V`-statistic/`U`-statistic and Hoeffding-decomposition literature. That vocabulary motivates "remove all repeated indices", but no external U-statistic theorem is needed here: the collision count (11) and the variance identity (17) are proved directly.
- WI-339 is the immediate line-local precursor: it deletes the exact constant Walsh sector generated by zero increments and identifies the moving `R_s=s+1` random-chaos transition. The present finding does not change that theorem; it shows that expanding the deleted set to every sparse combinatorial degeneracy leaves the same transition.
- A targeted search of Gowers-norm, degenerate-cube and Rademacher-chaos literature did not locate a published zeta/bow statement with the growing order `s\asymp\log\log N`, the full-denominator deletion convention, and the threshold (9). **No priority claim is made** for the elementary counting/Parseval synthesis.

No external source beyond those already anchored for WI-338/WI-339 is load-bearing, so `SOURCES.md` does not need a new entry.

## 6. Research consequence

The accepted distinguished-bow clue should no longer treat "delete more diagonals" as an unspecified escape. In the bow-scale growing-order regime, all repeated-vertex cubes are only a `K^{-1+o(1)}` fraction, and any `o(D)` geometric deletion leaves the exact same Rademacher chaos scale. Even in the bounded top strip, deleting any fixed polynomial fraction of generic cubes is insufficient to make that scale vanish after the `2^{-s}` root.

A genuinely different renormalization must therefore do at least one of the following:

- alter or cancel a positive-density family of **generic injective** cube monomials rather than merely remove degenerate configurations;
- couple several cube orders or introduce coefficients whose cancellations are not representable as sparse deletion;
- retain the actual `\Lambda-\Lambda^\sharp` shifted-correlation signs and/or the distinguished logarithmic carrier.

That is the durable boundary. WI-340 closes sparse combinatorial diagonal deletion; it does **not** close the bounded additive top strip itself and does not prove the source-specific signed covariance required by WI-195.