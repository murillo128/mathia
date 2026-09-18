# WI-339 — deleting the Gowers cube diagonal still does not force bow variance cancellation

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED + CLASSICAL-IDENTITY`.

WI-338 closes the ordinary-Gowers route at its natural diagonal threshold: for matched-energy Rademacher sources, zero-increment cubes force the usual normalized `U^s` amplitude to stop being small when

\[
R_s(K,N):=\frac{2^s\log\log N}{\log K}
\]

reaches `2`, while below that threshold the same random source can have small local `U^s` on every interval and still retain the full WI-195 sliding variance. A natural repair is to remove the zero-increment cubes before taking the `2^{-s}` root, so that the deterministic diagonal floor is no longer present.

The literal repair is still insufficient, and the obstruction reaches substantially closer to its own natural random-chaos boundary than the first version of this finding showed. The Walsh expansion in WI-338 makes the diagonal-deleted cube sum exactly the **centered Rademacher cube chaos**. Its `L^2` size has the sharp power

\[
K^{-(s+1)/2+o(1)}.
\]

A direct second-moment union bound therefore produces one matched-energy sign source whose diagonal-deleted amplitude is small on every bow-scale interval for every growing order satisfying

\[
\boxed{
s+1-R_s(K,N)\longrightarrow\infty,
}
\]

while the distinguished sliding square remains `(1+o(1))NK\log N`. Thus subtracting the ordinary Gowers diagonal does not create the signed two-point information required by the bow. The random-countermodel frontier moves from the ordinary threshold `R_s=2` to the much higher curve `R_s=s+1`, and even a shrinking **relative** margin below that curve is insufficient: only a bounded additive strip below it escapes the present countermodel.

Precisely, fix

\[
0<\kappa<1,\qquad K=N^{\kappa+o(1)},
\]

and a deterministic unit-modulus carrier `u_n`. For an interval `I` and `s\ge2`, let `D_{s,I}` be the total number of additive `s`-cubes with all vertices in `I`, with the same convention as WI-338. Define the **diagonal-deleted cube amplitude**

\[
\|b\|_{\dot U^s(I)}
:=
\left|
\frac1{D_{s,I}}
\sum_{\substack{x,h_1,\ldots,h_s\\
                 x+\omega\cdot h\in I\ \forall\omega\\
                 h_1\cdots h_s\ne0}}
\prod_{\omega\in\{0,1\}^s}
 b_{x+\omega\cdot h}
\right|^{1/2^s}.
\tag{1}
\]

This is only a diagnostic amplitude; after diagonal deletion it need not be a norm, and the quantity before the outer absolute value need not be nonnegative.

Choose any constant

\[
C_\kappa>\frac12\left(1+\frac1\kappa\right).
\tag{2}
\]

Then for all sufficiently large `N` there is a real sequence

\[
b_n=\sqrt{\log N}\,\varepsilon_n,
\qquad \varepsilon_n\in\{-1,+1\},
\tag{3}
\]

such that simultaneously for every integer interval `I\subset[1,N]` with `K\le |I|\le2K` and every integer `s\ge2` with `R_s(K,N)\le s+1`, one has

\[
\boxed{
|P_{s,I}|
\le
K^{-(s+1)/2+C_\kappa},
}
\tag{4}
\]

where `P_{s,I}` is the centered cube polynomial defined below, and the same realization satisfies

\[
\boxed{
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^{K}b_{x+j}u_{x+j}\right|^2
=(1+o(1))NK\log N.
}
\tag{5}
\]

Consequently, writing

\[
\Delta_s:=s+1-R_s(K,N),
\tag{6}
\]

we have the explicit all-interval bound

\[
\boxed{
\log\|b\|_{\dot U^s(I)}
\le
-\frac{\Delta_s-2C_\kappa}{2R_s(K,N)}\log\log N.
}
\tag{7}
\]

In particular, for any sequence `\rho_N\to\infty`, all growing orders satisfying

\[
R_s(K,N)\le s+1-\rho_N
\tag{8}
\]

obey

\[
\sup_{K\le |I|\le2K}\|b\|_{\dot U^s(I)}=o(1)
\tag{9}
\]

on the same realization. This strictly strengthens the earlier fixed-relative-margin statement `R_s\le(1-\eta)(s+1)`: the relative margin may now tend to zero, provided the additive gap from `s+1` tends to infinity.

## 1. Diagonal deletion is exactly centering for Rademacher cubes

Retain the notation of WI-338. For independent Rademacher signs `\varepsilon_n`, write

\[
Q_{s,I}=\sum_c\chi_{A(c)}(\varepsilon),
\qquad
F_{s,I}=Q_{s,I}/D_{s,I},
\tag{10}
\]

where the sum is over all additive cubes inside `I`. WI-338 encodes the parity support by

\[
P_c(X)=X^x\prod_{j=1}^s(1+X^{h_j})
\quad\text{in }\mathbb F_2[X,X^{-1}].
\tag{11}
\]

Because this Laurent polynomial ring is an integral domain,

\[
A(c)=\varnothing
\quad\Longleftrightarrow\quad
h_j=0\text{ for at least one }j.
\tag{12}
\]

A Rademacher monomial has expectation zero unless its parity support is empty. Therefore

\[
\mathbb E Q_{s,I}
=
\#\{c:\text{some }h_j=0\},
\tag{13}
\]

and deleting exactly the zero-increment cubes gives

\[
\boxed{
\frac{Q_{s,I}^{\circ}}{D_{s,I}}
:=
\frac1{D_{s,I}}
\sum_{c:\,h_1\cdots h_s\ne0}\chi_{A(c)}
=
F_{s,I}-\mathbb EF_{s,I}
=:P_{s,I}.
}
\tag{14}
\]

Thus the most literal diagonal renormalization is not a new random object: it is precisely the centered Walsh polynomial already exposed by WI-338.

For the energy-matched source `b_n=\sqrt{\log N}\varepsilon_n`, every `2^s`-vertex product gains the common factor `(\log N)^{2^{s-1}}`. Taking the `2^{-s}` root in (1) gives the exact identity

\[
\boxed{
\|b\|_{\dot U^s(I)}
=\sqrt{\log N}\,|P_{s,I}|^{1/2^s}.
}
\tag{15}
\]

## 2. The centered `L^2` exponent is sharp

WI-338 proves, uniformly for `|I|=L` and `s=O(\log\log N)`,

\[
\boxed{
\|P_{s,I}\|_2
\le
L^{-(s+1)/2}
\exp\!\bigl(O(s\log(s\log L))\bigr).
}
\tag{16}
\]

The power `L^{-(s+1)/2}` cannot be improved for the Rademacher model by a sharper upper-bound argument. Indeed Parseval gives

\[
\operatorname{Var}(Q_{s,I})
=\sum_{A\ne\varnothing}m_A^2,
\tag{17}
\]

where `m_A` counts cubes with parity support `A`. Every nonzero-increment cube contributes to some nonempty `A`, and `m_A^2\ge m_A`. If `M_{s,I}` is the number of nonzero-increment cubes, then

\[
\operatorname{Var}(Q_{s,I})\ge M_{s,I}.
\tag{18}
\]

The zero-increment cubes are at most `sL(2L)^{s-1}`, while WI-338's elementary interior-cube count gives

\[
D_{s,I}\ge \frac{L^{s+1}}{(Cs)^s}.
\tag{19}
\]

For `s=O(\log\log N)` and `L=N^{\kappa+o(1)}`, the ratio of those two quantities is `L^{-1+o(1)}`. Hence

\[
M_{s,I}=(1-o(1))D_{s,I}.
\tag{20}
\]

Also trivially `D_{s,I}\le L(2L)^s`. Therefore

\[
\boxed{
2^{-s/2}L^{-(s+1)/2}(1-o(1))
\le
\|P_{s,I}\|_2
\le
L^{-(s+1)/2+o(1)}.
}
\tag{21}
\]

So the exponent `(s+1)/2` is the genuine random-chaos scale. This matters at the top boundary: when `R_s=s+1+O(1)`, the energy-normalized `2^{-s}` root of a typical `L^2` fluctuation is only of constant size, not automatically `o(1)`. Closing a bounded additive strip cannot come from merely improving the multiplicity constants in (16).

## 3. A second-moment union bound closes every diverging additive gap

Condition `R_s\le s+1` implies `s=O(\log\log N)`: if `s` were larger than a sufficiently large constant multiple of `\log\log N`, the exponential growth of `2^s` would make `R_s` exceed `s+1`. Thus (16) applies uniformly to every order under consideration, and its subexponential factor is `K^{o(1)}`.

Set

\[
t_s:=K^{-(s+1)/2+C_\kappa}.
\tag{22}
\]

Chebyshev's inequality and (16) give, uniformly in `I` and `s`,

\[
\begin{aligned}
\mathbb P(|P_{s,I}|>t_s)
&\le t_s^{-2}\|P_{s,I}\|_2^2\\
&\le K^{s+1-2C_\kappa}K^{-(s+1)+o(1)}\\
&=K^{-2C_\kappa+o(1)}.
\end{aligned}
\tag{23}
\]

There are `O(NK)=K^{1+1/\kappa+o(1)}` integer intervals with length in `[K,2K]` and only `O(\log\log N)` retained orders. By (2),

\[
1+\frac1\kappa-2C_\kappa<0,
\]

so a union bound shows that (4) holds for every retained `(s,I)` simultaneously with probability `1-o(1)`.

Substitute (4) into the exact scaling identity (15). Since

\[
\frac{\log K}{2^s}
=
\frac{\log\log N}{R_s(K,N)},
\tag{24}
\]

we obtain

\[
\begin{aligned}
\log\|b\|_{\dot U^s(I)}
&\le
\frac12\log\log N
-\left(\frac{s+1}{2}-C_\kappa\right)\frac{\log K}{2^s}\\
&=
-\frac{s+1-2C_\kappa-R_s}{2R_s}\log\log N,
\end{aligned}
\tag{25}
\]

which is (7).

If (8) holds, the numerator in (25) is at least `\rho_N-2C_\kappa`. Moreover `R_s\le s+1=O(\log\log N)`, so `\log\log N/R_s` is bounded below by a positive absolute constant throughout the growing top-order regime. Hence the right side tends to `-\infty` as `\rho_N\to\infty`, proving (9).

For fixed low orders, the original fixed-moment hypercontractive argument from the first version of this finding still gives all-interval `o(1)` directly. The new second-moment estimate is needed only to squeeze the growing-order frontier from a fixed **relative** gap to a diverging **additive** gap.

## 4. The bow sliding square survives the same realization

WI-338 proves for the same Rademacher model and any prescribed unit carrier `u_n` that

\[
V(\varepsilon)
:=
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^{K}\varepsilon_{x+j}u_{x+j}\right|^2
=(1+o(1))NK
\tag{26}
\]

with probability `1-o(1)`. Multiplying by `\log N` gives (5). The all-interval event (4) also has probability `1-o(1)`, so their intersection has positive probability for all sufficiently large `N`. This proves the existence of one realization satisfying the diagonal-deleted bounds and the full bow-scale destination variance simultaneously.

No property of the carrier beyond `|u_n|=1` enters. In particular the countermodel applies to the distinguished bow carrier just as in WI-333--WI-338.

## 5. What this rules out

The result kills the **literal** diagonal-renormalization repair of ordinary Gowers uniformity:

\[
\text{ordinary cube average}
\longmapsto
\text{delete all zero-increment cubes}
\longmapsto
2^{-s}\text{ root}.
\]

Smallness of this statistic, even uniformly on every relevant interval and through every growing order whose additive distance below `R_s=s+1` tends to infinity, does not imply a saving over the diagonal-scale WI-195 sliding variance.

This does **not** rule out every statistic that could reasonably be called renormalized. A useful replacement might subtract a carrier-dependent or source-dependent local covariance, retain the signed two-point structure of `\Lambda-\Lambda^\sharp`, use a relative linear-forms object rather than an ordinary cube average, or couple several cube orders in a way not controlled by (1). Nor does the present proof cover the bounded additive strip `s+1-R_s=O_\kappa(1)` or orders above the curve `R_s=s+1`.

The conclusion is therefore an interface restriction, not a theorem that all higher-order methods fail. Any surviving diagonal-renormalized route must either operate at that top chaos scale or retain mathematical information absent from the centered ordinary cube chaos.

## 6. Relation to the bow defect problem

The accepted local clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` asks for a source-specific mechanism forcing

\[
\operatorname{Off}_X(U_{\rm bow})=-D_X+o(D_X)
\]

or for a canonical subtraction after which the same variance saving follows. WI-338 showed that increasing ordinary Gowers order cannot provide that sign information before the ordinary diagonal floor intervenes.

The present finding tests the most immediate escape from that floor. Removing zero-increment cubes makes the Gowers statistic diagonal-free, but random matched-energy sources can be uniformly small in that statistic through essentially the whole subcritical random-chaos hierarchy while retaining full positive diagonal-scale destination variance. The missing bow input is therefore not merely “remove the Gowers diagonal.” It must encode a relation to the distinguished carrier or to the signed shifted-prime covariance itself, unless one can exploit the narrow bounded-additive top strip by genuinely new information.

Because `R_{s+1}=2R_s`, the transition through `R_s\asymp s+1` occurs in only a constant number of integer orders. Thus the broad hierarchy is not reopened by diagonal deletion: the first order not defeated by the present random countermodel is pinned to the top `\log_2\log N` scale, while all lower growing orders at diverging additive distance are excluded as black-box routes.

## 7. Prior-art and novelty audit

The ingredients are classical or already persisted. Standard Gowers cube averages and inverse theory are classical additive combinatorics. WI-338 records the classical Bonami--Beckner hypercontractive inequality and random functions as small-Gowers benchmarks. The present sharpening itself uses only Parseval/orthogonality already present in WI-338, Chebyshev's inequality, and a union bound.

A targeted prior-art search around diagonal-free/nondegenerate Gowers cubes, centered cube statistics, and Rademacher chaos did not locate a published statement matching the interval-uniform growing-order comparison with the WI-195 bow variance. That absence is not a priority claim. The mathematical delta here is narrower and repository-local: the `L^2` exponent in WI-338 is both lower- and upper-sharp for the Rademacher model, and using it directly squeezes WI-339's former fixed-relative-margin boundary down to a bounded additive strip.

No new external theorem is needed for this strengthening, so the literature anchors already recorded for WI-338 remain sufficient provenance for the classical ingredients.

## 8. Boundary and falsification checks

The argument has five important boundaries.

First, (12) is exact for the real Rademacher model: expectation-one cubes are precisely those with at least one zero increment. A renormalization removing a larger or source-dependent family is not identified with `P_{s,I}` by (14).

Second, the source is a matched-energy countermodel, not the primes. The result is information-theoretic: an implication consuming only (1), interval length, energy normalization and a prescribed carrier is false. Arithmetic hypotheses not shared by the Rademacher model remain legitimate escape routes.

Third, the new sharpening does **not** claim small diagonal-deleted amplitude when `s+1-R_s` stays bounded. Equation (21) shows why this is not merely a loose concentration constant: the centered `L^2` scale itself reaches constant source amplitude in that regime.

Fourth, orders above `R_s=s+1` are not ruled out. The diagonal-deleted statistic has no deterministic positivity floor analogous to WI-336, so no contradiction prevents an arithmetic source from being small there.

Fifth, (1) is not asserted to be a norm. The finding concerns the most literal diagonal-subtracted ordinary Gowers interface, not a pre-existing canonical object of additive combinatorics.

The decisive audit tests are direct: verify WI-338's centered `L^2` estimate (16), the Parseval lower bound (17)--(21), the exponent count in the all-interval union bound (23), and the exact source-amplitude conversion (25). Failure of any one of those steps requires narrowing the strengthened range. Otherwise a future generic diagonal-renormalized proposal must identify information absent from (1), rather than merely deleting zero-increment cubes.

## 9. Research consequence

WI-338 showed that the ordinary norm is blocked by its own diagonal exactly when random countermodels stop being ordinary-Gowers-small. WI-339 now shows that **removing that diagonal still does not reveal the bow covariance even when the relative gap to the centered-chaos boundary shrinks to zero**: every diverging additive gap below `R_s=s+1` still admits an all-interval matched-energy countermodel with full destination variance.

The live source-side route is therefore more specific. A useful statistic must be carrier-aware, source-aware, explicitly two-point/covariance-aware, or exploit the bounded-additive top chaos strip in a way unavailable to the generic Rademacher interface. Deleting universal Gowers self-contractions is not enough. This sharpens the remaining defect-elimination question without changing any unconditional zeta-zero proportion.