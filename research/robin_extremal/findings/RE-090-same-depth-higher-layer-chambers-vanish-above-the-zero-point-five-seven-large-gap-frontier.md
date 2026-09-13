# RE-090 — same-depth higher-layer chambers vanish in threshold measure above the 0.57 large-gap frontier

**Status:** `EXACT-DERIVED + EXTERNAL-LOAD-BEARING-PRIME-GAP-MASS + SAME-DEPTH-HIGHER-LAYER-SCARCITY + THRESHOLD-MEASURE-VANISHING + ZERO-POINT-FIVE-SEVEN-FRONTIER + FINITE-MIXED-DEPTH-REDUCTION + ADVERSARIAL-CORRECTED + PRIOR-ART-BOUNDED`.

`RE-088` shows that, once a false-RH zero frontier lies beyond the available all-short-interval exponent, sufficiently deep selected support boundaries occupy vanishing threshold measure. The difficult residual case is the second layer: its ambient event count lives exactly at square-root scale, so the counting-plus-cell-width argument cannot eliminate it.

The missing selection information is that a selected CA chamber whose two adjacent support boundaries share the same higher depth is much more expensive than one isolated higher-layer event. Such a chamber contains no first-layer event, and same-depth adjacency forces its physical width into an ordinary consecutive-prime gap of at least square-root size. Olli Järviniemi's dyadic theorem on the **total length** of square-root-sized prime gaps then gives the aggregate resource needed to control these selected chambers.

Assume RH is false and

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>0.57.
\tag{1}
\]

Fix

\[
J=[b_0,b_1]\Subset(1-\Theta,0.43)
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
\frac{X_\mathcal B^{\,b_1-0.43+\epsilon}}
{\log X_\mathcal B}.
}
\tag{7}
\]

Choosing

\[
0<\epsilon<0.43-b_1
\tag{8}
\]

gives

\[
\boxed{|J_{j,j}(\mathcal B)|\longrightarrow0.}
\tag{9}
\]

In particular, **pure second-layer selected chambers have vanishing threshold measure whenever `Theta>0.57`**. More generally, any fixed finite collection of same-depth higher-layer chamber families has vanishing threshold measure.

Combining this with `RE-088` and the currently anchored all-large short-interval exponent `theta=0.52` gives a uniform finite-depth reduction. Because `b_1<0.43`,

\[
\delta:=1-b_1-0.52>0.05=\frac1{20}.
\tag{10}
\]

Therefore `RE-088` applies with the fixed cutoff `r=20`: outside a subset of `J` whose measure tends to zero, no adjacent support boundary contains an event of depth `j>=20`. Applying (9) for `j=2,...,19` removes all surviving higher-layer-only chambers whose two boundary depth sets share any common depth. Thus, up to `o(1)` threshold measure, every selected cell satisfies one of two alternatives:

1. at least one adjacent support boundary contains a first-layer atom; or
2. neither boundary contains a first-layer atom, every participating depth lies in `{2,...,19}`, and the two boundary depth sets are disjoint.

For untied boundaries the second alternative is simply

\[
\boxed{2\le j_-\ne j_+<20.}
\tag{11}
\]

Hence above the `0.57` zero frontier, the higher-layer-only escape is reduced to a **finite mixed-depth resonance problem** rather than an unrestricted square-root-density second-layer mechanism.

## 1. Same-depth adjacency forces a square-root-or-larger ordinary prime gap

For fixed `j`, `RE-054` gives the real event map

\[
\eta_j(x)\log\eta_j(x)
=
\frac{\log x}{\lambda_j(x)},
\qquad
\eta_j(x)
=
\frac{x^j}{j}\left(1+O_j\!\left(\frac1{\log x}\right)\right),
\tag{12}
\]

with

\[
\eta_j'(x)
=x^{j-1}\left(1+O_j\!\left(\frac1{\log x}\right)\right).
\tag{13}
\]

If `C` is `j/j`-bounded, there is no CA event in the open chamber

\[
(\eta_j(p),\eta_j(q)).
\tag{14}
\]

In particular there is no `j`-th layer prime event there. Since `eta_j` is strictly increasing, `p` and `q` are consecutive ordinary primes. Hence `q-p>=2` for large odd primes, and the prime number theorem gives `q/p->1`. Integrating (13) across the consecutive-prime interval yields

\[
\Delta_C
:=\xi_+(C)-\xi_-(C)
=
(1+o_j(1))p^{j-1}(q-p),
\tag{15}
\]

so

\[
\boxed{
\Delta_C\ge(2-o_j(1))p^{j-1}.
}
\tag{16}
\]

`RE-088` proves uniformly on the exposed late fan that

\[
\frac{\xi_\pm(C)}{Y_C}\longrightarrow1.
\tag{17}
\]

Together with (12), this gives

\[
\Delta_C\gg_j Y_C^{1-1/j}.
\tag{18}
\]

At the critical depth `j=2`, the constant is safely larger than one:

\[
\boxed{
\Delta_C\ge(2\sqrt2-o(1))\sqrt{Y_C}.
}
\tag{19}
\]

Now pull the physical chamber back through the first-layer event map,

\[
Q_C
:=
\eta_1^{-1}\!\bigl((\xi_-(C),\xi_+(C))\bigr).
\tag{20}
\]

The interval `Q_C` contains no ordinary prime, because a prime `s` in `Q_C` would place its first-layer event `eta_1(s)` strictly inside the support chamber. Since `RE-054` gives

\[
\eta_1'(x)=1+O(1/\log x),
\tag{21}
\]

we have

\[
|Q_C|=(1+o(1))\Delta_C.
\tag{22}
\]

Thus `Q_C` lies inside one consecutive ordinary-prime gap. Its endpoints are at scale `asymp Y_C`; by the prime number theorem the containing gap's initial prime is also `asymp Y_C`. Equations (18)--(22) imply that for every fixed `j>=2`, and in particular with room to spare for `j=2`, the containing gap eventually satisfies

\[
\boxed{p_{n+1}-p_n\ge\sqrt{p_n}.}
\tag{23}
\]

This is the crucial selection upgrade: two same-depth support boundaries force a **large ordinary-prime gap at the physical CA scale**.

## 2. Järviniemi's large-gap mass theorem gives exponent `0.57`

The load-bearing external input is Theorem 1.1 of Olli Järviniemi, *On large differences between consecutive primes*, arXiv:2212.10965v2. For every `epsilon>0`,

\[
\boxed{
\sum_{\substack{p_n\in[x,2x]\\
p_{n+1}-p_n\ge x^{1/2}}}
(p_{n+1}-p_n)
\ll_\epsilon x^{0.57+\epsilon}.
}
\tag{24}
\]

This improves the earlier `3/5+epsilon` square-root-gap mass exponent of Heath-Brown.

Fix a dyadic physical shell

\[
X\le Y_C<2X.
\tag{25}
\]

By (17), (20)--(23), the ordinary gaps containing the intervals `Q_C` have initial primes in a bounded number of dyadic shells comparable with `X`, and each satisfies the square-root threshold in the corresponding shell. Distinct exposed CA states have disjoint open support chambers; because `eta_1^{-1}` is increasing, their intervals `Q_C` are also disjoint. Several `Q_C` may lie inside the same ordinary-prime gap, but their total length there is at most the gap length.

Applying (24) on those finitely many comparable dyadic shells and using (22) therefore gives

\[
\boxed{
\sum_{\substack{C\ j/j\text{-bounded}\\X\le Y_C<2X}}
\Delta_C
\ll_{j,\epsilon}X^{0.57+\epsilon}.
}
\tag{26}
\]

The gain over ambient second-layer counting is that (26) controls **physical chamber mass**, not merely the number of possible higher-layer events.

## 3. CA support capacity converts gap mass into threshold measure

`RE-040` gives the exact support-capacity inequality

\[
|I_C|
\le
\frac{Y_C\bigl(\varepsilon_-(C)-\varepsilon_+(C)\bigr)}{a(C)},
\qquad
a(C)=1-e^{-h(C)}.
\tag{27}
\]

The support slopes are

\[
\varepsilon_-(C)=g(\xi_-(C)),
\qquad
\varepsilon_+(C)=g(\xi_+(C)),
\qquad
g(x)=\frac1{x\log x}.
\tag{28}
\]

On the shell (25), (17) and

\[
|g'(x)|\asymp\frac1{x^2\log x}
\tag{29}
\]

give

\[
\varepsilon_-(C)-\varepsilon_+(C)
\ll_J
\frac{\Delta_C}{X^2\log X}.
\tag{30}
\]

The false-RH threshold construction supplies the uniform amplitude floor from `RE-040`,

\[
a(C)\gg_J X^{-b_1}.
\tag{31}
\]

Substitution into (27) yields

\[
|I_C|
\ll_J
\frac{\Delta_C\,X^{b_1-1}}{\log X}.
\tag{32}
\]

Summing (32) over the `j/j`-bounded states in the shell and applying (26),

\[
\boxed{
\sum_{\substack{C\ j/j\text{-bounded}\\X\le Y_C<2X}}
|I_C|
\ll_{J,j,\epsilon}
\frac{X^{b_1-0.43+\epsilon}}{\log X}.
}
\tag{33}
\]

Because `b_1<0.43`, choose `epsilon` as in (8). The exponent in (33) is negative, so summing dyadic shells above `X_\mathcal B` gives a convergent geometric tail and proves (7)--(9).

The exponent bookkeeping is exact for this splice. If the square-root large-gap mass theorem were available with exponent `beta`, the same proof would require

\[
b_1<1-\beta.
\tag{34}
\]

The false-RH fan simultaneously requires `b_1>1-Theta`, so the window exists exactly when

\[
\boxed{\Theta>\beta.}
\tag{35}
\]

With Järviniemi's `beta=0.57`, the live frontier of this mechanism is therefore `Theta>0.57`.

## 4. The splice with `RE-088` leaves only finitely many mixed-depth resonances

Take the unconditional all-large prime-in-short-interval exponent `theta=0.52` already anchored for this line. The interval (2) lies inside `(1-Theta,0.48)`, so the hypotheses of `RE-088` are satisfied. Equation (10) gives

\[
\delta>\frac1{20}.
\tag{36}
\]

`RE-088` therefore shows that cells having any adjacent support boundary of depth at least `20` occupy threshold measure `o(1)`. The finitely many applications of (9) for depths `2,...,19` remove every remaining cell whose two adjacent boundary depth sets share a higher depth.

This includes tied boundaries: if both endpoints contain a depth-`j` atom, the cell is `j/j`-bounded and belongs to the corresponding vanishing family. Thus a surviving higher-layer-only tied cell must have two **disjoint** nonempty depth sets, each contained in `{2,...,19}`. No infinite-depth or same-depth second-layer escape remains at positive threshold measure in this regime.

What remains is genuinely different arithmetic: cross-layer near-resonance between event maps

\[
\eta_j(p)\approx\eta_k(q),
\qquad j\ne k,
\tag{37}
\]

plus the cells touching the first layer. Those configurations can be much closer than same-depth events, so the ordinary-gap spacing argument above does not transfer to them.

## 5. Stress tests and exact boundary of the claim

The theorem does **not** say that second-layer events themselves are sparse. Their ambient count remains of square-root order. It says that the more restrictive selected configuration in which both adjacent support boundaries share depth `2` cannot occupy positive threshold measure when `Theta>0.57`.

One higher-layer boundary is insufficient: without a same-depth atom on the opposite side, the physical chamber width need not inherit the spacing between consecutive base primes. Likewise, two boundaries of different depths can be arbitrarily close through cross-layer resonance; (16) has no mixed-depth analogue. These are genuine exclusions from the claim.

Ties do not invalidate the charging argument. If both support coordinates contain a depth-`j` atom, the open chamber still contains no event of any layer and the two depth-`j` base primes are consecutive. If several `Q_C` lie in one ordinary-prime gap, their disjointness ensures that the gap is charged by at most its own total length.

The `0.57` boundary is a boundary of the **present large-gap-mass/capacity splice**, not a claim that the mathematical phenomenon changes there. When `Theta<=0.57`, the false-RH threshold interval forces `b>1-Theta>=0.43`, while (33) no longer has a negative power from the currently available `0.57+epsilon` aggregate theorem. A stronger aggregate square-root-gap estimate would lower the frontier according to (35).

No finite computation is load-bearing. The proof uses the exact CA event geometry already derived in this line, the compact-fan capacity theorem, the deep-boundary theorem for the final finite-depth splice, and Järviniemi's analytic large-gap mass estimate.

## Prior-art boundary

Järviniemi's arXiv:2212.10965v2 is the load-bearing external theorem and explicitly improves Heath-Brown's earlier `3/5+epsilon` aggregate exponent to `0.57+epsilon` for square-root-sized gaps on dyadic shells. A targeted current search did not locate a later directly applicable improvement of this square-root large-gap mass exponent.

The external theorem contains no CA, Robin, adaptive-threshold, or rightmost-maximizer statement. The line-specific derived coupling is

\[
\text{same-depth selected CA adjacency}
\Longrightarrow
\text{physical square-root prime gap}
\Longrightarrow
\text{aggregate gap-mass bound}
\Longrightarrow
\text{vanishing threshold measure}.
\tag{38}
\]

No priority claim is made beyond this derived coupling. The durable consequence is that for `Theta>0.57`, same-depth higher-layer chambers are asymptotically negligible and, after the `RE-088` cutoff, the higher-layer-only escape is a finite mixed-depth resonance family.