# RE-091 — mean-square gap sparsity forces first-layer boundary contact above the 469/600 frontier

**Status:** `EXACT-DERIVED + EXTERNAL-LOAD-BEARING-PRIME-GAP-SECOND-MOMENT + DEEP-BOUNDARY-THRESHOLD-MEASURE-VANISHING + FIRST-LAYER-CONTACT-REDUCTION + FOUR-SIXTY-NINE-OVER-SIX-HUNDRED-FRONTIER + PRIOR-ART-AUDITED`.

`RE-088` shows that sufficiently deep CA support boundaries have vanishing threshold measure once the false-RH frontier clears a depth-dependent complexity cutoff, while `RE-090` removes selected chambers whose two boundaries share the same fixed higher depth above `Theta>0.57`. Their residual higher-layer-only escape is therefore a finite family of mixed-depth resonances. The first unresolved member is depth `3`: the ambient count is only `X^(1/3+o(1))`, but the pointwise short-interval argument of `RE-088` still needs `Theta>0.853...` to make that count affordable.

There is a stronger aggregate route. A selected support chamber contains no first-layer event, so its inverse image under the first-layer event map is an ordinary prime-free interval of essentially the same physical length. If one of the chamber boundaries contains a depth-at-least-three event, `RE-004` gives only `X^(1/3+o(1))` possible boundary hosts. Cauchy--Schwarz can therefore pair that sparse host count with Julia Stadlmann's unconditional second-moment theorem for ordinary prime gaps,

\[
\sum_{p_n\le x}(p_{n+1}-p_n)^2\ll_\varepsilon x^{1.23+\varepsilon}.
\tag{1}
\]

The result is a physical chamber-mass exponent

\[
\frac12\left(\frac13+1.23\right)
=\frac{469}{600}.
\tag{2}
\]

After the exact CA threshold-capacity conversion, this eliminates **every selected cell touching depth `3` or deeper** whenever `Theta>469/600`. Splicing with `RE-090` then collapses the higher-layer-only residual completely: outside vanishing threshold measure, every sufficiently late selected cell must have a first-layer atom on at least one adjacent support boundary.

Assume RH is false and

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac{469}{600}.
\tag{3}
\]

Fix

\[
J=[b_0,b_1]\Subset
\left(1-\Theta,\frac{131}{600}\right)
\tag{4}
\]

and work on the sufficiently late common positive CA blocks of `RE-040`. For an exposed selected state `C`, write

\[
Y_C=\log C,
\qquad
I_C=\{b\in J:C\text{ is the rightmost maximizer of }A_b\},
\tag{5}
\]

and let

\[
\xi_-(C)<\xi_+(C),
\qquad
\Delta_C:=\xi_+(C)-\xi_-(C)
\tag{6}
\]

be its adjacent physical CA support coordinates and chamber width. Let `C` be **deep-bounded** if at least one of `xi_-(C),xi_+(C)` contains an event atom of depth `j>=3`; ties are allowed. For a block `\mathcal B`, put

\[
J_{\ge3}(\mathcal B)
:=\bigcup_{C\text{ exposed and deep-bounded}}I_C.
\tag{7}
\]

If `X_\mathcal B` is the minimum selected physical scale in the block, then for every sufficiently small `epsilon>0`,

\[
\boxed{
|J_{\ge3}(\mathcal B)|
\ll_{J,\varepsilon}
X_\mathcal B^{\,b_1-131/600+\varepsilon}
(\log X_\mathcal B)^{-1/3}.
}
\tag{8}
\]

In particular, choosing

\[
0<\varepsilon<\frac{131}{600}-b_1
\tag{9}
\]

gives

\[
\boxed{|J_{\ge3}(\mathcal B)|\longrightarrow0.}
\tag{10}
\]

Because `469/600>0.57`, `RE-090` is simultaneously available. Outside the union of two threshold subsets of measure `o(1)`, no support boundary contains depth `j>=3`, and no selected chamber has depth `2` on both boundaries. Every support boundary is a nonempty CA event coordinate. Therefore a surviving selected cell with no first-layer atom would have to be `2/2`-bounded, which `RE-090` excludes. Hence

\[
\boxed{
\Theta>\frac{469}{600}
\Longrightarrow
\text{for threshold measure }|J|-o(1),
\text{ every selected cell has a first-layer boundary atom.}
}
\tag{11}
\]

This is a qualitative strengthening of the finite-depth reduction in `RE-090`: above `469/600`, the surviving problem is no longer a family of purely higher-layer cross-depth resonances. Any positive-threshold-measure escape must now remain attached to the ordinary-prime frontier on at least one side.

## 1. Depth-three-or-higher boundaries have only cubic-root host count

`RE-004` proves that for every fixed `r>=2`, the number of event occurrences of depth at least `r` with physical coordinate at most `T` satisfies

\[
M_{\ge r}(T)
=O_r\!\left((T\log T)^{1/r}\log T\right).
\tag{12}
\]

Taking `r=3`,

\[
\boxed{
M_{\ge3}(T)
=O\!\left(T^{1/3}(\log T)^{4/3}\right).
}
\tag{13}
\]

`RE-088` gives uniform physical localization on the late compact fan,

\[
\xi_\pm(C)=(1+o_J(1))Y_C.
\tag{14}
\]

Fix a dyadic shell

\[
X\le Y_C<2X.
\tag{15}
\]

Then every deep boundary of a selected cell in this shell has physical coordinate `O_J(X)`. A single physical CA event coordinate can border at most two open support chambers. Counting event occurrences rather than distinct coordinates only overestimates tied events. Therefore the number `N_X` of deep-bounded selected cells in the shell obeys

\[
\boxed{
N_X\ll_J X^{1/3}(\log X)^{4/3}.
}
\tag{16}
\]

This is the only place where higher-layer sparsity enters. Unlike `RE-088`, no pointwise upper bound for ordinary prime gaps is used.

## 2. Every support chamber carries an ordinary prime-free interval of the same length

For any exposed selected state, not just a deep-bounded one, pull the open physical support chamber back through the first-layer event map from `RE-054`:

\[
Q_C:=
\eta_1^{-1}\!\left((\xi_-(C),\xi_+(C))\right).
\tag{17}
\]

There is no CA event in the open support chamber. If an ordinary prime `p` lay in `Q_C`, its first-layer atom `eta_1(p)` would lie strictly between the adjacent support boundaries, a contradiction. Thus

\[
\boxed{Q_C\cap\mathbb P=\varnothing.}
\tag{18}
\]

The first-layer map satisfies

\[
\eta_1'(x)=1+O(1/\log x),
\tag{19}
\]

so uniformly in the shell,

\[
\boxed{|Q_C|=(1+o_J(1))\Delta_C.}
\tag{20}
\]

Distinct exposed states have disjoint open physical support chambers; monotonicity of `eta_1^{-1}` therefore makes the intervals `Q_C` pairwise disjoint. Each `Q_C` lies inside some consecutive ordinary-prime gap

\[
G_n=(p_n,p_{n+1}),
\qquad d_n:=p_{n+1}-p_n.
\tag{21}
\]

Several `Q_C` may lie in one `G_n`; no injectivity is needed. If `\mathcal G_X` is the set of distinct ordinary gaps used by the deep-bounded cells in the shell, disjointness gives

\[
\sum_{C\text{ deep-bounded}}|Q_C|
\le
\sum_{G_n\in\mathcal G_X}d_n,
\tag{22}
\]

and trivially

\[
\#\mathcal G_X\le N_X.
\tag{23}
\]

Because the inverse first-layer intervals lie at physical scale `O(X)`, every containing gap has initial prime `p_n=O(X)`; enlarging the constant if necessary also covers a boundary-crossing gap. Thus the global second moment up to `O(X)` controls every gap in `\mathcal G_X`.

## 3. Stadlmann's second moment converts sparse hosts into physical chamber-mass sparsity

The load-bearing external theorem is Theorem 1 of Julia Stadlmann, *On the mean square gap between primes*, arXiv:2212.10867 (2022). For every `epsilon>0`,

\[
\boxed{
\sum_{p_n\le x}(p_{n+1}-p_n)^2
\ll_\varepsilon x^{123/100+\varepsilon}.
}
\tag{24}
\]

This is currently a preprint theorem; the present finding is rigorous conditional only on that stated theorem, not on any unproved hypothesis about zeta zeros or prime gaps beyond the explicit false-RH assumption being analyzed.

Cauchy--Schwarz, (16), (22)--(24) give

\[
\begin{aligned}
\sum_{\substack{C\text{ deep-bounded}\\X\le Y_C<2X}}
\Delta_C
&\ll_J
\sum_{G_n\in\mathcal G_X}d_n\\
&\le
(\#\mathcal G_X)^{1/2}
\left(\sum_{p_n\ll X}d_n^2\right)^{1/2}\\
&\ll_{J,\varepsilon}
X^{\frac12(1/3+123/100)+\varepsilon}
(\log X)^{2/3}.
\end{aligned}
\tag{25}
\]

Since

\[
\frac12\left(\frac13+\frac{123}{100}\right)
=\frac{469}{600},
\tag{26}
\]

we obtain

\[
\boxed{
\sum_{\substack{C\text{ deep-bounded}\\X\le Y_C<2X}}
\Delta_C
\ll_{J,\varepsilon}
X^{469/600+\varepsilon}(\log X)^{2/3}.
}
\tag{27}
\]

This is the decisive gain over ambient event counting. The theorem pays for the **total selected chamber width** using the second moment of the same ordinary-prime gaps that contain their first-layer inverse images.

## 4. CA support capacity gives the `469/600` false-RH frontier

`RE-040` gives the exact support-capacity inequality

\[
|I_C|
\le
\frac{Y_C(\varepsilon_-(C)-\varepsilon_+(C))}{a(C)},
\qquad
a(C)=1-e^{-h(C)}.
\tag{28}
\]

As in `RE-090`, the support slopes are

\[
\varepsilon_-(C)=g(\xi_-(C)),
\qquad
\varepsilon_+(C)=g(\xi_+(C)),
\qquad
g(x)=\frac1{x\log x}.
\tag{29}
\]

On the shell, (14) and `|g'(x)|\asymp(x^2\log x)^{-1}` imply

\[
\varepsilon_-(C)-\varepsilon_+(C)
\ll_J\frac{\Delta_C}{X^2\log X}.
\tag{30}
\]

The same false-RH amplitude floor used throughout the compact fan gives

\[
a(C)\gg_J X^{-b_1}.
\tag{31}
\]

Hence

\[
\boxed{
|I_C|
\ll_J
\frac{\Delta_C X^{b_1-1}}{\log X}.
}
\tag{32}
\]

Summing (32) and applying (27),

\[
\boxed{
\sum_{\substack{C\text{ deep-bounded}\\X\le Y_C<2X}}
|I_C|
\ll_{J,\varepsilon}
X^{b_1-131/600+\varepsilon}(\log X)^{-1/3}.
}
\tag{33}
\]

The interval (4) exists precisely because

\[
1-\Theta<\frac{131}{600}
\iff
\Theta>\frac{469}{600}.
\tag{34}
\]

Choose `epsilon` as in (9). The exponent in (33) is negative, so the dyadic tail above `X_\mathcal B` is a convergent geometric series and proves (8)--(10).

This improves the depth-three cutoff supplied by `RE-088` with the currently anchored all-large short-interval exponent `theta=0.52`. That pointwise argument needs

\[
1-b_1-0.52>\frac13,
\tag{35}
\]

which can coexist with `b_1>1-Theta` only for `Theta>0.853\overline3`. The second-moment splice lowers the same deep-boundary exclusion to

\[
\boxed{\Theta>469/600\approx0.781666\ldots.}
\tag{36}
\]

## 5. Splicing with `RE-090` forces first-layer boundary contact

Now remove the threshold set `J_{\ge3}(\mathcal B)` from (10). Every adjacent support boundary of every surviving selected cell contains only depth `1` or depth `2` event atoms.

Suppose a surviving cell contained no first-layer atom on either support boundary. Since each support boundary is an actual CA event coordinate, each boundary must then contain a depth-`2` atom. The cell is therefore `2/2`-bounded in the sense of `RE-090`, ties included. Because `Theta>469/600>0.57`, `RE-090` says that the union of such cells has threshold measure `o(1)`.

After removing both vanishing families, every remaining selected cell has a first-layer atom on at least one boundary. This proves (11). In particular, the purely higher-layer mixed-depth resonance family `{2,...,19}` left by the `RE-088`--`RE-090` splice cannot carry positive asymptotic threshold measure this far off the critical line.

The theorem does **not** say that both boundaries are first-layer, nor that depth-`2` atoms disappear. A surviving cell may have a first-layer atom on one boundary and a second-layer or tied first/second-layer atom on the other. The new reduction is exactly one-sided first-layer contact.

## 6. General exponent law and stress tests

The mechanism has a transparent exponent law. Suppose an external theorem supplied

\[
\sum_{p_n\le x}d_n^2\ll x^{1+\nu+o(1)}
\tag{37}
\]

and one wishes to eliminate boundaries of depth at least `r`. `RE-004` gives host count `X^{1/r+o(1)}`, so Cauchy gives physical mass exponent

\[
\boxed{
\beta_{r,\nu}
=\frac12\left(1+\nu+\frac1r\right).
}
\tag{38}
\]

The compact false-RH fan then admits a vanishing threshold bound exactly when `Theta>beta_{r,nu}`. Stadlmann's `nu=0.23` and `r=3` give `beta=469/600`. Even a conjectural near-optimal full second moment with `nu=0` would make this particular depth-three mechanism stop at `2/3`; reaching the `0.57` frontier would require additional structure rather than only sharpening this second moment.

The proof is insensitive to multiple selected subintervals occupying the same ordinary gap: they are disjoint, so that gap is charged by at most its own length before Cauchy--Schwarz. It is also insensitive to CA event ties: occurrence counting in `RE-004` overcounts tied coordinates, and a physical coordinate borders at most two support chambers.

No assumption that the deep event itself generates the containing ordinary gap is used. The depth event only supplies a sparse **host count**; the ordinary gap comes independently from the event-free support chamber via the first-layer inverse map. This separation is why mixed depths, including arbitrary ties containing a depth-at-least-three atom, are covered uniformly.

No finite computation is load-bearing.

## Prior-art boundary

Stadlmann's arXiv:2212.10867 is the load-bearing external source for (24), improving the earlier full second-moment exponent `1.25+epsilon` to `1.23+epsilon`. A targeted current search by the exact square-sum formula, the Stadlmann title/exponent, recent prime-gap work, and CA/Robin combinations did not locate a later primary source improving the complete second-moment exponent or a prior splice with adaptive colossally-abundant support selection. This is a search boundary, not a priority claim.

The external theorem contains no CA, Robin, support-chamber, or threshold-measure statement. Conversely, the CA ingredients used here are already canonical in `RE-004`, `RE-040`, `RE-054`, `RE-088`, and `RE-090`. The durable new delta is the Cauchy coupling between (i) sparse deep boundary hosts and (ii) the ordinary-prime gaps forced by the same selected support chambers, followed by the exact threshold-capacity conversion.

## Consequence for the research line

Above `Theta=469/600`, generic purely higher-layer selection is no longer the live obstruction: almost all threshold mass is forced to touch the ordinary-prime frontier at one adjacent support boundary. The next theorem should therefore exploit **first-layer contact plus the opposite boundary constraint**, rather than continue to budget arbitrary cross-depth resonances.

Two concrete residual configurations remain: a first-layer atom opposite a depth-`2` atom, and tied first/second-layer boundaries. Both couple an ordinary prime directly to the selected chamber endpoint, so the anchored-gap compatibility of `RE-086` and the exact prime-set transport identities of `RE-083`--`RE-084` can now be applied without first paying an unrestricted higher-layer exception budget.