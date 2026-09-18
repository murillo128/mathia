# WI-339 — deleting the Gowers cube diagonal still does not force bow variance cancellation

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED + CLASSICAL-IDENTITY`.

WI-338 closes the ordinary-Gowers route at its natural diagonal threshold: for matched-energy Rademacher sources, zero-increment cubes force the usual normalized `U^s` amplitude to stop being small when

\[
R_s(K,N):=\frac{2^s\log\log N}{\log K}
\]

reaches `2`, while below that threshold the same random source can have small local `U^s` on every interval and still retain the full WI-195 sliding variance. A natural repair is to remove the zero-increment cubes before taking the `2^{-s}` root, so that the deterministic diagonal floor is no longer present.

The literal repair is still insufficient. The Walsh expansion in WI-338 makes the diagonal-deleted cube sum exactly the **centered Rademacher cube chaos**. Its `L^2` fluctuation is much smaller than the removed diagonal, and hypercontractivity yields a matched-energy sign source whose diagonal-deleted amplitude is small on every bow-scale interval through every growing order satisfying a fixed margin below

\[
\boxed{R_s=s+1,}
\]

while the distinguished sliding square remains `(1+o(1))NK\log N`. Thus subtracting the ordinary Gowers diagonal does not create the signed two-point information required by the bow. It moves the random-countermodel frontier from `R_s=2` to a substantially higher growing-order curve, but it does not couple the statistic to the required negative covariance.

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

For every fixed `eta` with `0<eta<1`, for all sufficiently large `N` there is a real sequence

\[
b_n=\sqrt{\log N}\,\varepsilon_n,
\qquad \varepsilon_n\in\{-1,+1\},
\tag{2}
\]

such that, simultaneously for every integer interval `I\subset[1,N]` with `K\le |I|\le2K` and every integer `s\ge2` satisfying

\[
\boxed{
R_s(K,N)\le(1-\eta)(s+1),
}
\tag{3}
\]

one has

\[
\boxed{
\|b\|_{\dot U^s(I)}
\le
(\log N)^{-\eta/(4(1-\eta))},
}
\tag{4}
\]

while the same realization satisfies

\[
\boxed{
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^{K}b_{x+j}u_{x+j}\right|^2
=(1+o(1))NK\log N.
}
\tag{5}
\]

Hence every fixed margin below `R_s=s+1` admits an all-interval diagonal-deleted countermodel with full destination variance. This reaches to within `O_{\kappa,\eta}(1)` orders of `\log_2\log N`: if

\[
s=\lfloor\log_2\log N\rfloor-C,
\]

then

\[
\frac{R_s}{s+1}
\le
\frac{(\log 2)2^{-C}}{\kappa}(1+o(1)).
\tag{6}
\]

(The floor contributes a bounded factor, so an asymptotic equality without tracking its fractional part would be false.) Choosing fixed `C` large enough that the displayed constant is below `1-\eta` places these orders in the countermodel regime.

## 1. Diagonal deletion is exactly centering for Rademacher cubes

Retain the notation of WI-338. For independent Rademacher signs `\varepsilon_n`, write

\[
Q_{s,I}=\sum_c\chi_{A(c)}(\varepsilon),
\qquad
F_{s,I}=Q_{s,I}/D_{s,I},
\tag{7}
\]

where the sum is over all additive cubes inside `I`. WI-338 encodes the parity support by

\[
P_c(X)=X^x\prod_{j=1}^s(1+X^{h_j})
\quad\text{in }\mathbb F_2[X,X^{-1}].
\tag{8}
\]

Because this Laurent polynomial ring is an integral domain,

\[
A(c)=\varnothing
\quad\Longleftrightarrow\quad
h_j=0\text{ for at least one }j.
\tag{9}
\]

A Rademacher monomial has expectation zero unless its parity support is empty. Therefore

\[
\mathbb E Q_{s,I}
=
\#\{c:\text{some }h_j=0\},
\tag{10}
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
\tag{11}
\]

Thus the most literal diagonal renormalization is not a new random object: it is precisely the centered Walsh polynomial already exposed by WI-338.

For the energy-matched source `b_n=\sqrt{\log N}\varepsilon_n`, every `2^s`-vertex product gains the common factor `(\log N)^{2^{s-1}}`. Taking the `2^{-s}` root in (1) gives the exact identity

\[
\boxed{
\|b\|_{\dot U^s(I)}
=\sqrt{\log N}\,|P_{s,I}|^{1/2^s}.
}
\tag{12}
\]

## 2. Centering exposes much stronger random concentration

WI-338 proves, uniformly for `|I|=L` and `s=O(\log\log N)`,

\[
\|P_{s,I}\|_2
\le
L^{-(s+1)/2}
\exp\!\bigl(O(s\log(s\log L))\bigr).
\tag{13}
\]

The centered polynomial has Walsh degree at most `d=2^s`, so the classical Bonami--Beckner inequality gives, for every `q\ge2`,

\[
\|P_{s,I}\|_q
\le(q-1)^{2^{s-1}}\|P_{s,I}\|_2.
\tag{14}
\]

Condition (3) implies

\[
2^s
\le
(1-\eta)(s+1)\frac{\log K}{\log\log N},
\tag{15}
\]

and hence `s=O(\log\log N)`, so (13) applies. Unlike the ordinary-`U^s` argument of WI-338, after deleting the diagonal we can take a sufficiently large **fixed** moment `q`: the `L^2` decay carries `(s+1)` powers of `K`, while the hypercontractive loss contributes only `2^s=O((s+1)\log K/\log\log N)` in the logarithm.

Set

\[
a_s:=\frac{1-\eta/2}{2}(s+1),
\qquad
t_s:=K^{-a_s}.
\tag{16}
\]

Using `L\ge K`, (13)--(15), and fixed `q`,

\[
\begin{aligned}
\log\frac{\|P_{s,I}\|_q}{t_s}
&\le
2^{s-1}\log(q-1)
-\frac{s+1}{2}\log K
+a_s\log K
+O(s\log(s\log K))\\
&=
-\frac{\eta}{4}(s+1)\log K
+o\bigl((s+1)\log K\bigr).
\end{aligned}
\tag{17}
\]

Indeed the hypercontractive term is

\[
O_q\!\left(\frac{(s+1)\log K}{\log\log N}\right),
\tag{18}
\]

and the multiplicity error in (13) is `O((\log\log N)^2)`, both lower order than the fixed-`eta` negative term in (17).

Markov's inequality now gives

\[
\mathbb P(|P_{s,I}|>t_s)
\le
\exp\!\left(-q\frac{\eta}{4}(s+1)\log K
+o_q((s+1)\log K)\right).
\tag{19}
\]

Since `\log K=(\kappa+o(1))\log N`, choose the fixed `q=q(\kappa,\eta)` large enough that even the smallest retained order `s=2` makes the main exponent in (19) larger than `(1+\kappa+1)\log N`. There are only `O(NK)` integer intervals with length in `[K,2K]` and `O(\log\log N)` retained orders. A union bound therefore yields, with probability `1-o(1)`,

\[
\boxed{|P_{s,I}|\le K^{-a_s}}
\tag{20}
\]

for every such interval and every order satisfying (3).

## 3. Energy normalization leaves a logarithmic power saving

Insert (20) into (12):

\[
\log\|b\|_{\dot U^s(I)}
\le
\frac12\log\log N
-\frac{a_s}{2^s}\log K.
\tag{21}
\]

By (3),

\[
\frac{\log K}{2^s}
\ge
\frac{\log\log N}{(1-\eta)(s+1)}.
\tag{22}
\]

Using (16),

\[
\begin{aligned}
\log\|b\|_{\dot U^s(I)}
&\le
\left[
\frac12-
\frac{1-\eta/2}{2(1-\eta)}
\right]\log\log N\\
&=
-\frac{\eta}{4(1-\eta)}\log\log N,
\end{aligned}
\tag{23}
\]

which is exactly (4).

The point is structural: diagonal subtraction removes the deterministic floor at `R_s=2`, but the random off-diagonal chaos remains uniformly tiny much farther upward. The new random-countermodel scale is governed by the competition between the `(s+1)` powers in the centered `L^2` fluctuation and the `2^s` root needed to return to source-amplitude normalization.

## 4. The bow sliding square survives the same realization

WI-338 proves for the same Rademacher model and any prescribed unit carrier `u_n` that

\[
V(\varepsilon)
:=
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^K\varepsilon_{x+j}u_{x+j}\right|^2
=(1+o(1))NK
\tag{24}
\]

with probability `1-o(1)`. Multiplying by `\log N` gives (5). The all-interval event (20) also has probability `1-o(1)`, so their intersection has positive probability for all sufficiently large `N`. This proves the existence of one realization satisfying (4) and (5) simultaneously.

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

Smallness of this statistic, even uniformly on every relevant interval and through all growing orders satisfying a fixed margin below `R_s=s+1`, does not imply a saving over the diagonal-scale WI-195 sliding variance.

This does **not** rule out every statistic that could reasonably be called renormalized. A useful replacement might subtract a carrier-dependent or source-dependent local covariance, retain the signed two-point structure of `\Lambda-\Lambda^\sharp`, use a relative linear-forms object rather than an ordinary cube average, or couple several cube orders in a way not controlled by (1). The present proof also leaves a top growing-order strip where `R_s/(s+1)` approaches or exceeds `1`; (13)--(14) do not by themselves produce the amplitude-small countermodel there.

The conclusion is therefore an interface restriction, not a theorem that all higher-order methods fail. Any surviving diagonal-renormalized route must retain mathematical information absent from the centered ordinary cube chaos.

## 6. Relation to the bow defect problem

The accepted local clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` asks for a source-specific mechanism forcing

\[
\operatorname{Off}_X(U_{\rm bow})=-D_X+o(D_X)
\]

or for a canonical subtraction after which the same variance saving follows. WI-338 showed that increasing ordinary Gowers order cannot provide that sign information before the ordinary diagonal floor intervenes.

The present finding tests the most immediate escape from that floor. Removing zero-increment cubes makes the Gowers statistic diagonal-free, but random matched-energy sources can be uniformly small in that statistic through a much larger hierarchy while retaining full positive diagonal-scale destination variance. The missing bow input is therefore not merely “remove the Gowers diagonal.” It must encode a relation to the distinguished carrier or to the signed shifted-prime covariance itself.

For the surviving fixed-power bow range, `K=X^{\kappa+o(1)}` with fixed positive `\kappa`. Equation (6) shows that this countermodel reaches to within a constant number of the `\log_2\log X`-scale orders. A generic hierarchy that hopes to evade the result solely by going to higher diagonal-deleted Gowers order is therefore compressed into a top-order strip rather than reopening the broad hierarchy closed by WI-338.

## 7. Prior-art and novelty audit

The ingredients are classical or already persisted. Standard Gowers cube averages and inverse theory are classical additive combinatorics. Bonami--Beckner hypercontractivity on the Boolean cube is classical; WI-338 records Ryan O'Donnell, *Analysis of Boolean Functions* (Cambridge University Press, 2014), Chapter 9, as a modern reference. Random functions as small-Gowers benchmarks are classical; WI-338 also records Fouvry--Kowalski--Michel, *An inverse theorem for Gowers norms of trace functions over F_p*, *Math. Proc. Cambridge Philos. Soc.* 155 (2013), 277--295.

A targeted external search around diagonal-free/nondegenerate Gowers cubes, centered cube statistics, degenerate U-statistics, and Rademacher chaos located the general probability literature on centered/degenerate U-processes and Rademacher chaoses, including Peter Eichelsbacher, *Moderate deviations for degenerate U-processes*, *Stochastic Processes and their Applications* 87 (2000), 255--279. Those sources support the general viewpoint that centering leads to a Rademacher-chaos object; they do not supply the interval-uniform growing-order statement (3)--(5) or its comparison with the WI-195 bow variance.

The Mathia deduction is narrower: combine WI-338's specific Walsh multiplicity/`L^2` estimate with fixed-moment hypercontractivity, then retain the `2^{-s}` source normalization after deleting the zero-increment cubes. A local corpus check found no existing finding stating this diagonal-deleted barrier. No priority claim is made beyond that repository delta.

## 8. Boundary and falsification checks

The argument has four important boundaries. First, (9) is exact for the real Rademacher model: expectation-one cubes are precisely those with at least one zero increment. A renormalization removing a larger or source-dependent family is not identified with `P_{s,I}` by (11).

Second, the source is a matched-energy countermodel, not the primes. The result is information-theoretic: an implication consuming only (1), interval length, energy normalization and a prescribed carrier is false. Arithmetic hypotheses not shared by the Rademacher model remain legitimate escape routes.

Third, `eta` is fixed. Shrinking margins would require retaining the exact gap `s+1-R_s` in (17)--(23); no such strengthening is claimed here.

Fourth, (1) is not asserted to be a norm. The finding concerns the most literal diagonal-subtracted ordinary Gowers interface, not a pre-existing canonical object of additive combinatorics.

The decisive audit test is direct: if WI-338's centered `L^2` bound (13), its degree bound `2^s`, or the exact centering identity (11) fails under the stated interval convention, this finding must be narrowed or withdrawn. Otherwise a future generic diagonal-renormalized proposal must identify information absent from (1), rather than merely deleting zero-increment cubes.

## 9. Research consequence

WI-338 showed that the ordinary norm is blocked by its own diagonal exactly when random countermodels stop being ordinary-Gowers-small. WI-339 shows that **removing that diagonal still does not reveal the bow covariance**: the centered cube chaos can remain uniformly tiny through every fixed margin below `R_s=s+1` while the destination variance remains full.

The live source-side route is therefore more specific. A useful statistic must be carrier-aware, source-aware, or explicitly two-point/covariance-aware; deleting universal Gowers self-contractions is not enough. This sharpens the remaining defect-elimination question without changing any unconditional zeta-zero proportion.