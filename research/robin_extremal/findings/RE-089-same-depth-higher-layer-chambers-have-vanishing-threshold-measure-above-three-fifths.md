# RE-089 — same-depth higher-layer chambers have vanishing threshold measure above three-fifths

**Status:** `EXACT-DERIVED + EXTERNAL-LOAD-BEARING-PRIME-GAP-MASS + SAME-DEPTH-HIGHER-LAYER-SCARCITY + THRESHOLD-MEASURE-VANISHING + THREE-FIFTHS-FRONTIER + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-088` shows that, once a false-RH zero frontier lies beyond the available all-short-interval exponent, sufficiently deep selected support boundaries occupy vanishing threshold measure. It also isolates the obstruction that ambient event counting cannot remove depth `2`: the second-layer event count lives at the square-root scale. The missing distinction is that a selected CA **chamber with the same higher layer on both boundaries** is much more expensive than one isolated second-layer event. Such a chamber contains no first-layer event at all, so the distance between its two higher-layer boundary atoms must fit inside an ordinary prime gap at the physical scale.

That physical gap is automatically at least square-root sized. A theorem of D. R. Heath-Brown on the **total length** of square-root-sized prime gaps then gives a summable resource that was absent from the marginal event count of `RE-087` and the ambient boundary count of `RE-088`.

Assume RH is false and

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac35.
\tag{1}
\]

Fix

\[
J=[b_0,b_1]\Subset(1-\Theta,2/5)
\tag{2}
\]

and work on the sufficiently late common positive CA blocks of `RE-040`. For an exposed state `C`, write

\[
Y_C=\log C,
\qquad
I_C=\{b\in J:C\text{ is the rightmost maximizer of }A_b\},
\tag{3}
\]

and let

\[
\xi_-(C)<\xi_+(C)
\tag{4}
\]

be its adjacent physical CA support coordinates. For a fixed layer `j>=2`, call `C` **`j/j`-bounded** if both support coordinates contain a `j`-th layer event atom,

\[
\xi_-(C)=\eta_j(p),
\qquad
\xi_+(C)=\eta_j(q)
\tag{5}
\]

for primes `p<q`; either coordinate may also be a tied event involving other layers. Put

\[
J_{j,j}(\mathcal B)
:=
\bigcup_{C\text{ exposed and }j/j\text{-bounded}} I_C.
\tag{6}
\]

Then for every fixed `j>=2` and every `epsilon>0`, if `X_\mathcal B` is the minimum physical scale of the selected states in the block,

\[
\boxed{
|J_{j,j}(\mathcal B)|
\ll_{J,j,\epsilon}
\frac{X_\mathcal B^{\,b_1-2/5+\epsilon}}
{\log X_\mathcal B}.
}
\tag{7}
\]

Choosing

\[
0<\epsilon<\frac25-b_1
\tag{8}
\]

gives

\[
\boxed{|J_{j,j}(\mathcal B)|\longrightarrow0.}
\tag{9}
\]

The case `j=2` is the important boundary case: **pure second-layer chambers have vanishing threshold measure whenever `Theta>3/5`.** More generally, any fixed finite collection of same-depth higher-layer chambers has vanishing threshold measure.

Combined with `RE-088`, this gives a sharper finite-depth classification. Using the current unconditional all-short-interval exponent `theta=0.52`, choose `r` so large that

\[
\frac1r<1-b_1-0.52.
\tag{10}
\]

Then, outside a subset of `J` whose measure tends to zero, every selected cell either has a first-layer atom on at least one adjacent support boundary, or its two higher-layer boundary depth sets are genuinely different. In the simple untied case the surviving alternative is therefore

\[
\boxed{
2\le j_-\ne j_+<r.
}
\tag{11}
\]

Thus above the `3/5` zero frontier the second layer does not survive as a free square-root-density chamber mechanism. What remains is a **finite mixed-depth resonance problem**, together with cells touching the first layer.

## 1. Same-depth adjacency forces a long ordinary-prime gap at the physical scale

For fixed `j`, `RE-054` gives the real event map

\[
\eta_j(x)\log\eta_j(x)
=
\frac{\log x}{\lambda_j(x)},
\qquad
\eta_j(x)=\frac{x^j}{j}\left(1+O_j\!\left(\frac1{\log x}\right)\right),
\tag{12}
\]

with

\[
\eta_j'(x)
=x^{j-1}\left(1+O_j\!\left(\frac1{\log x}\right)\right).
\tag{13}
\]

If `C` is `j/j`-bounded as in (5), there is no CA event in the open chamber

\[
(\eta_j(p),\eta_j(q)).
\tag{14}
\]

In particular there is no `j`-th layer prime event there. Since `eta_j` is strictly increasing, `p` and `q` are consecutive ordinary primes. Hence, for large `p`,

\[
q-p\ge2.
\tag{15}
\]

The prime number theorem gives `q/p->1`, so integrating (13) across the consecutive-prime interval gives

\[
\Delta_C
:=\xi_+(C)-\xi_-(C)
=
(1+o_j(1))p^{j-1}(q-p).
\tag{16}
\]

Therefore

\[
\boxed{
\Delta_C\ge(2-o_j(1))p^{j-1}.
}
\tag{17}
\]

`RE-088` proves uniformly on the exposed late fan that the adjacent support coordinates satisfy

\[
\boxed{
\frac{\xi_\pm(C)}{Y_C}\longrightarrow1.
}
\tag{18}
\]

Together with (12), this implies

\[
\Delta_C\gg_j Y_C^{1-1/j}.
\tag{19}
\]

For `j=2` the constant is safely above the square-root threshold: because `eta_2(p)~p^2/2` and `xi_-(C)~Y_C`, (17) gives

\[
\Delta_C\ge(2\sqrt2-o(1))\sqrt{Y_C}.
\tag{20}
\]

Now pull the physical chamber back through the **first-layer** event map:

\[
Q_C
:=
\eta_1^{-1}\!\bigl((\xi_-(C),\xi_+(C))\bigr).
\tag{21}
\]

The interval `Q_C` contains no ordinary prime. Indeed, a prime `s\in Q_C` would place its first-layer CA event `eta_1(s)` strictly inside the support chamber (14), contradicting adjacency. Since `RE-054` with `j=1` gives

\[
\eta_1'(x)=1+O(1/\log x),
\tag{22}
\]

we also have

\[
|Q_C|=(1+o(1))\Delta_C.
\tag{23}
\]

Consequently `Q_C` lies inside one consecutive ordinary-prime gap at scale `asymp Y_C`. Equations (19)--(23) show that for every fixed `j>=2` this containing gap eventually satisfies

\[
p_{n+1}-p_n\ge\sqrt{p_n}.
\tag{24}
\]

This is the key difference from the marginal anchored gaps in `RE-086`: two same-depth support boundaries force a **large gap at the physical scale**, not merely a base-prime gap at scale `Y^{1/j}`.

## 2. Heath-Brown bounds the total physical chamber width

The load-bearing external input is Heath-Brown's theorem on large consecutive-prime gaps: for every fixed `epsilon>0`,

\[
\boxed{
\sum_{\substack{p_n\le x\\p_{n+1}-p_n\ge\sqrt{p_n}}}
(p_{n+1}-p_n)
\ll_\epsilon x^{3/5+\epsilon}.
}
\tag{25}
\]

This is Theorem 1 of D. R. Heath-Brown, *The Differences Between Consecutive Primes, V*, International Mathematics Research Notices **2021** (22), 17514--17562, DOI `10.1093/imrn/rnz295`, arXiv:1906.09555.

Fix a dyadic physical shell

\[
X\le Y_C<2X.
\tag{26}
\]

Distinct exposed CA states have disjoint open support chambers. Because `eta_1^{-1}` is increasing, their intervals `Q_C` in (21) are also disjoint. Several such intervals may lie inside the same large ordinary-prime gap, but their **total** length inside that gap is at most the gap length itself. Therefore (23)--(25) give

\[
\boxed{
\sum_{\substack{C\ j/j\text{-bounded}\\X\le Y_C<2X}}
\Delta_C
\ll_{j,\epsilon}X^{3/5+\epsilon}.
}
\tag{27}
\]

The point is that (27) controls **physical chamber mass**, not the number of higher-layer events. This is why it reaches the square-root layer that defeated the counting argument of `RE-088`.

## 3. CA support capacity converts physical large-gap mass into threshold measure

`RE-040` gives the exact support-capacity inequality

\[
|I_C|
\le
\frac{Y_C\bigl(\varepsilon_-(C)-\varepsilon_+(C)\bigr)}{a(C)},
\qquad
a(C)=1-e^{-h(C)}.
\tag{28}
\]

The support slopes are

\[
\varepsilon_-(C)=g(\xi_-(C)),
\qquad
\varepsilon_+(C)=g(\xi_+(C)),
\qquad
g(x)=\frac1{x\log x}.
\tag{29}
\]

On the dyadic shell (26), (18) and

\[
|g'(x)|\asymp\frac1{x^2\log x}
\tag{30}
\]

give

\[
\varepsilon_-(C)-\varepsilon_+(C)
\ll_J
\frac{\Delta_C}{X^2\log X}.
\tag{31}
\]

The false-RH threshold construction also supplies the uniform amplitude floor from `RE-040`,

\[
a(C)\gg_J X^{-b_1}.
\tag{32}
\]

Substituting (31)--(32) into (28),

\[
|I_C|
\ll_J
\frac{\Delta_C\,X^{b_1-1}}{\log X}.
\tag{33}
\]

Summing (33) over the `j/j`-bounded states in the shell and using (27) yields

\[
\boxed{
\sum_{\substack{C\ j/j\text{-bounded}\\X\le Y_C<2X}}
|I_C|
\ll_{J,j,\epsilon}
\frac{X^{b_1-2/5+\epsilon}}{\log X}.
}
\tag{34}
\]

Because `b_1<2/5`, choose `epsilon` as in (8). The exponent in (34) is then negative. Summing the dyadic shells above the minimum block scale `X_\mathcal B` is a convergent geometric tail and proves (7)--(9).

This mechanism has a clean exponent interpretation. If the large-gap mass theorem (25) were available with exponent `beta` in place of `3/5`, the same argument would require

\[
b_1<1-\beta.
\tag{35}
\]

Since the false-RH fan requires `b_1>1-Theta`, such a window exists exactly when

\[
\Theta>\beta.
\tag{36}
\]

Thus the `3/5` frontier here is not an artifact of optimizing CA parameters: it is exactly the current exponent in the external square-root large-gap-mass theorem.

## 4. Splicing with `RE-088` leaves only finite mixed-depth resonances

Take the current all-short-interval exponent `theta=0.52` used in `RE-088`. Under (1)--(2),

\[
\delta:=1-b_1-0.52>0.08.
\tag{37}
\]

Choose a fixed integer `r` with

\[
\frac1r<\delta.
\tag{38}
\]

`RE-088` then shows that the union of cells having **any** adjacent support boundary of depth at least `r` has threshold measure tending to zero. We may therefore restrict, up to `o(1)` threshold measure, to the finitely many depths

\[
1,2,\ldots,r-1.
\tag{39}
\]

For each fixed `j=2,...,r-1`, (9) removes the cells whose two adjacent boundaries both contain depth `j`. A finite union of `o(1)` sets is still `o(1)`. Therefore, outside vanishing threshold measure, a surviving cell must satisfy one of two alternatives:

1. at least one adjacent support boundary contains a first-layer atom; or
2. neither boundary contains a first-layer atom, but the two higher-layer boundary depth sets have no common element.

For untied boundaries this is exactly the mixed-depth condition (11). Hence the square-root second layer survives only through **cross-layer resonance** with another low layer, not as a same-layer chamber family of positive threshold measure.

This is a stricter target than the conclusion of `RE-088`. The remaining arithmetic problem is no longer "control layer 2 despite its square-root event count." It is to control a finite collection of mixed event equations

\[
\eta_j(p)\lesssim Z_b(C)\lesssim\eta_k(q),
\qquad j\ne k,
\tag{40}
\]

including tied or near-tied low-layer resonances and their compatibility with the rightmost-maximizer rule.

## 5. Boundary checks and falsification

The theorem does **not** say that second-layer events themselves are sparse. Their ambient count remains of square-root order, exactly as `RE-088` records. What becomes sparse in threshold measure is the much more restrictive configuration in which two adjacent selected support boundaries share the same higher depth.

One higher-layer boundary is insufficient: without a same-depth atom on the opposite side, the physical chamber width need not inherit the spacing between consecutive base primes. Likewise, two boundaries of different depths can be arbitrarily close through a cross-layer resonance, so (17) has no mixed-depth analogue. Those are genuine exclusions, not proof gaps.

Ties do not invalidate the charging argument. If both support coordinates contain a depth-`j` atom, the open CA chamber still contains no event of any layer, and the two depth-`j` base primes are consecutive. Different `Q_C` remain disjoint even if one or both endpoints are tied. If several `Q_C` lie in the same ordinary-prime gap, disjointness ensures that the gap is charged at most by its own total length.

The `3/5` hypothesis is also real for this argument. When `Theta<=3/5`, the false-RH threshold interval forces `b>1-Theta>=2/5`, while the exponent in (34) can no longer be made negative from Heath-Brown's current `3/5+epsilon` large-gap-mass bound. No pointwise short-interval theorem repairs that mismatch; the proof specifically spends **aggregate square-root-gap length**.

## Prior-art boundary

A targeted audit included Alaoglu--Erdos/Robin CA structure, Mantovanelli's 2026 exact prime-layer workload, Zimov's consecutive-CA transition analysis, and the literature on large gaps between consecutive primes. Heath-Brown's theorem (25) is the load-bearing external input and is recorded in `SOURCES.md`. The search did not locate the specific coupling used here: same-depth CA chamber adjacency -> a square-root-or-larger ordinary prime gap at the physical scale -> aggregate large-gap-mass bound -> vanishing adaptive-threshold measure. No priority claim is made beyond that line-specific derived coupling.

The durable consequence is the change of the post-`RE-088` frontier for `Theta>3/5`: **same-depth higher-layer chambers are asymptotically negligible; after the finite-depth cutoff, the only higher-layer-only escape is a finite mixed-depth resonance family.**