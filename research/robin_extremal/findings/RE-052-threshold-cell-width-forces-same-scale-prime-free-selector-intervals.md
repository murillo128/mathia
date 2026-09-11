# RE-052 — threshold-cell width forces same-scale prime-free selector intervals

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + PRIME-EVENT-COUPLING + PROPORTIONAL-PRIME-FREE-SELECTOR-CAPACITY + AGGREGATE-GAP-BUDGET + CELL-WIDTH/GAP-TRADEOFF + FULL-OFF-CRITICAL-CHAMBER + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-051` uses an unconditional prime-in-short-interval theorem to show that, when the hypothetical rightmost zero frontier lies beyond the available short-interval exponent, every exposed adaptive threshold cell must be small. The argument can be factored one level earlier, before inserting any external prime-gap bound. The exact first-layer staggering and the adaptive selector speed imply a source-specific local law: **every positive-width threshold cell creates a proportionally long ordinary-prime-free interval at the same physical scale.**

The proportional form strengthens the earlier additive version of this finding. The genuine CA support chamber is prime-free except possibly in its final half-unit. Since that exceptional piece has length less than one, the entire selector image contains at most one ordinary prime. Removing one point can split an interval into at most two prime-free components, so one component retains at least half of the selector length. The previous additive loss `P_C+1/2 >= |S_C|` is therefore unnecessary for the existence of one long prime-free interval.

Assume RH is false and write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix any compact interval

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2),
\tag{2}
\]

with no additional restriction such as `b_1<0.48`. Work on a sufficiently late common positive CA counterexample block of `RE-040`. For an exposed CA state `C`, put

\[
Y:=\log C,
\qquad
h:=\log G(C)-\gamma>0,
\qquad
a:=1-e^{-h},
\tag{3}
\]

and let

\[
I_C:=\{b\in J:C\text{ is the rightmost maximizer of }A_b\},
\qquad
A_b(C)=Y^b(e^h-1).
\tag{4}
\]

For `b` in the interior of `I_C`, let `Z_C(b)` be the regular adaptive selector from `RE-040`,

\[
g(Z_C(b))=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x},
\tag{5}
\]

and define its physical selector image

\[
S_C:=Z_C(I_C^\circ).
\tag{6}
\]

Let `\xi_-(C)<\xi_+(C)` be the adjacent genuine CA event coordinates supporting `C`. Then `S_C` is an interval contained in the open support chamber `(\xi_-,\xi_+)`, and uniformly over every exposed positive-width cell,

\[
\boxed{
|S_C|
\gg_J
|I_C|\,Y^{1-b_1}\log Y.
}
\tag{7}
\]

The same support chamber has the exact first-layer exclusion

\[
\boxed{
(\xi_-(C),\,\xi_+(C)-1/2]
\quad\text{contains no ordinary prime.}
}
\tag{8}
\]

Consequently the whole selector image contains at most one ordinary prime:

\[
\boxed{
\#\bigl(S_C\cap\mathbb P\bigr)\le1.
}
\tag{9}
\]

Let `P_C` denote the length of the longest connected ordinary-prime-free subinterval of `S_C`. Then

\[
\boxed{
P_C
\ge\frac12|S_C|
\gg_J
|I_C|\,Y^{1-b_1}\log Y.
}
\tag{10}
\]

This is the sharpened local capacity law. It has **no additive half-unit loophole**, so it remains informative even when the false-RH fan fragments `J` into arbitrarily thin threshold cells.

If `\mathcal E(\mathcal B,J)` is the exposed-state set of a late block and

\[
X_{\mathcal B}:=
\min_{C\in\mathcal E(\mathcal B,J)}Y_C,
\tag{11}
\]

then the selector images of distinct exposed states lie in distinct open CA support chambers and are pairwise disjoint. Choosing one interval of length `P_C` inside each image therefore gives pairwise disjoint prime-free intervals. Since the cells partition `J` up to endpoints and `Y^{1-b_1}\log Y` is increasing for large `Y`, (10) yields the aggregate blockwise burden

\[
\boxed{
\sum_{C\in\mathcal E(\mathcal B,J)}P_C
\gg_J
X_{\mathcal B}^{\,1-b_1}\log X_{\mathcal B}.
}
\tag{12}
\]

Equivalently, the whole fan satisfies the normalized prime-gap capacity budget

\[
\boxed{
|J|
\ll_J
\sum_{C\in\mathcal E(\mathcal B,J)}
\frac{P_C}{Y_C^{\,1-b_1}\log Y_C}.
}
\tag{13}
\]

Thus fragmentation can replace one huge gap by many smaller selected gaps, but it cannot make the **total prime-free selector demand** disappear.

## 1. The selector image expands at speed `aY log Y`

For a fixed exposed state `C`, the quantities `Y`, `h`, and `a` do not vary while `b` moves inside `I_C`. Differentiate the exact selector equation (5). Since

\[
g'(x)
=-\frac{\log x+1}{x^2(\log x)^2},
\tag{14}
\]

implicit differentiation gives

\[
\boxed{
Z_C'(b)
=
\frac{a}{Y|g'(Z_C(b))|}
=
\frac{a Z_C(b)^2(\log Z_C(b))^2}
{Y(\log Z_C(b)+1)}
>0.
}
\tag{15}
\]

`RE-040` proves uniformly on the whole compact fan that

\[
\frac{Z_C(b)}Y\longrightarrow1.
\tag{16}
\]

Therefore

\[
\boxed{
Z_C'(b)
=(1+o_J(1))aY\log Y.
}
\tag{17}
\]

The quantitative false-RH inheritance on the common blocks gives one constant `c_0>0` such that every selected state satisfies

\[
A_b(C)=Y^b(e^h-1)\ge c_0.
\tag{18}
\]

Put `R=e^h-1`. Since `b\le b_1`,

\[
R\ge c_0Y^{-b_1}.
\tag{19}
\]

The uniform small-height regime gives `R\to0`, and

\[
a=\frac R{1+R},
\]

so eventually

\[
\boxed{a\gg_JY^{-b_1}.}
\tag{20}
\]

Combining (17)--(20),

\[
Z_C'(b)
\gg_J
Y^{1-b_1}\log Y
\tag{21}
\]

throughout the interior of the cell. Since `Z_C` is increasing,

\[
|S_C|
=
\int_{I_C^\circ}Z_C'(b)\,db
\gg_J
|I_C|Y^{1-b_1}\log Y,
\tag{22}
\]

which proves (7). Breakpoint endpoints have zero measure and do not affect the identity. Degenerate zero-width cells contribute nothing.

## 2. Every selector image contains at most one ordinary prime

By the simultaneous regularity theorem of `RE-040`, for every `b\in I_C^\circ` the selector lies strictly inside the genuine CA support chamber,

\[
\xi_-<Z_C(b)<\xi_+.
\tag{23}
\]

`RE-042` gives, for every sufficiently large ordinary prime `q`, the exact first-layer staggering

\[
\boxed{q<\eta_q<q+\frac12.}
\tag{24}
\]

Suppose an ordinary prime lies in the nonterminal part of the chamber,

\[
\xi_-<q\le\xi_+-\frac12.
\tag{25}
\]

Then

\[
\xi_-<q<\eta_q<q+\frac12\le\xi_+,
\tag{26}
\]

placing the genuine first-layer CA event `\eta_q` strictly between the two adjacent support events `\xi_-` and `\xi_+`, which is impossible. This proves (8).

All ordinary primes in the support chamber are therefore confined to the terminal interval `(\xi_+-1/2,\xi_+)`. That interval has length `1/2`, hence contains at most one integer and in particular at most one ordinary prime. Since `S_C\subset(\xi_-,\xi_+)`, equation (9) follows.

If `S_C` contains no prime, take all of `S_C`. If it contains one prime `q`, deleting that single point splits `S_C` into at most two prime-free intervals whose lengths sum to `|S_C|`; one has length at least `|S_C|/2`. This proves (10).

This distinction matters. The terminal half-unit cannot be declared uniformly prime-free: `RE-044`--`RE-049` show that a prime can legitimately occur there before its associated first-layer event fires. But the existence of that one possible point does **not** cost a fixed half-unit when the objective is to extract one long prime-free interval. The correct universal loss is multiplicative by at most `1/2`.

## 3. Fragmentation still forces aggregate prime-free length

For distinct exposed CA states `C\ne D`, the open support chambers are disjoint. Equivalently, the exact event selector `\Phi(Z)` cannot choose two distinct regular states at the same non-event coordinate. Hence their selector images `S_C` and `S_D` are disjoint, and the chosen prime-free intervals of lengths `P_C` can also be taken disjoint.

Summing (10) and using the partition identity

\[
\sum_{C\in\mathcal E(\mathcal B,J)}|I_C|=|J|
\tag{27}
\]

up to finitely many zero-measure breakpoint endpoints gives

\[
\begin{aligned}
\sum_C P_C
&\gg_J
\sum_C |I_C|Y_C^{1-b_1}\log Y_C\\
&\ge
X_{\mathcal B}^{1-b_1}\log X_{\mathcal B}
\sum_C|I_C|,
\end{aligned}
\tag{28}
\]

which is (12). Dividing the cellwise estimate (10) by its physical scale and summing gives (13).

Because `b_1<1/2`, the exponent `1-b_1` is strictly larger than `1/2`. Thus every sufficiently late false-RH common block must carry a **super-square-root total amount of pairwise disjoint prime-free selector length**, even if no individual threshold cell is macroscopic.

This statement is aggregate, not a hidden large-gap theorem. The intervals can be split among many ordinary prime gaps, and several disjoint chosen intervals may sit inside the same larger prime gap if skipped CA chambers separate their selector images. Equation (12) measures physical prime-free length, not the number of distinct ordinary gaps.

## 4. The cell-count/prime-gap tradeoff now has no thin-cell exception

Extend each chosen prime-free interval to the consecutive ordinary-prime gap containing it and let `G_C` denote that gap length. The bracketing primes are `(1+o_J(1))Y_C`: the selector image lies at scale `Z\sim Y_C`, and the prime number theorem gives consecutive-prime ratios tending to one. Therefore

\[
\boxed{
G_C
\gg_J
|I_C|Y_C^{1-b_1}\log Y_C
}
\tag{29}
\]

for **every** exposed positive-width cell.

If a block exposes `N_{\mathcal B}` cells, at least one has width `|J|/N_{\mathcal B}`. Hence

\[
\boxed{
\max_C
\frac{G_C}{Y_C^{1-b_1}\log Y_C}
\gg_J
\frac1{N_{\mathcal B}}.
}
\tag{30}
\]

In particular, bounded fan complexity recovers the previous strong alternative: if `N_{\mathcal B}\le K` along infinitely many blocks, then one obtains infinitely many same-scale gaps

\[
G_C\gg_{J,K}Y_C^{1-b_1}\log Y_C.
\tag{31}
\]

Given any `\varepsilon>0`, choose `b_1` with

\[
1-\Theta<b_1<\min\!\left(\frac12,1-\Theta+\varepsilon\right).
\tag{32}
\]

Then `1-b_1>\Theta-\varepsilon`, so a bounded coherent false-RH fan would force infinitely many selected prime gaps

\[
\boxed{
G_C
\gg_{J,K,\varepsilon}
Y_C^{\Theta-\varepsilon}
}
\tag{33}
\]

with the stronger logarithmic factor retained before the exponent-only simplification.

The gain over the previous version is not in the bounded-complexity corollary, where the additive `1/2` was already negligible. It is that (29) remains nonvacuous for arbitrarily thin cells. Fragmenting `J` into many cells no longer creates cells whose prime-gap consequence disappears below a fixed additive error.

## 5. `RE-051` is exactly the insertion of an external gap-capacity bound

Suppose `\theta\in(1/2,1)` has the property that every sufficiently large interval `[x-x^\theta,x]` contains a prime. At selector scale `Z\sim Y`, every consecutive prime gap satisfies

\[
G_C\ll Y_C^\theta.
\tag{34}
\]

Combining with (29) gives for every exposed cell

\[
\boxed{
|I_C|
\ll_J
\frac{Y_C^{b_1+\theta-1}}{\log Y_C}.
}
\tag{35}
\]

This is the cell-width estimate underlying `RE-051`, now obtained with no additive term at any cell scale. When `b_1<1-\theta`, the exponent in (35) is negative; summing the cells over fixed `J` gives the polynomial fan-complexity lower bound of `RE-051`.

With Runbo Li's current unconditional `\theta=0.52`, this closes the bounded-cell escape when `\Theta>0.52` and `J\Subset(1-\Theta,0.48)`. When `1/2<\Theta\le0.52`, present unconditional technology still does not dominate the required selected gap scale. The strengthened result nevertheless removes a bookkeeping loophole there: **every cell, however thin, has a proportional same-scale prime-gap cost, and the total disjoint prime-free cost over the block is super-square-root by (12).**

## 6. Stress tests and exact boundary

This finding does not prove that the near-critical selected gaps are impossible, and it does not turn the aggregate lower bound (12) into one prime gap of comparable size. A fan may still escape by using many thin cells and distributing the required prime-free length across many physical locations.

The aggregate intervals in (12) are pairwise disjoint as subsets of selector space, but they are not asserted to belong to distinct ordinary consecutive-prime gaps. Therefore one must not combine (12) with a prime-gap counting theorem by simply treating the summands as independent gaps.

The result also remains logically separate from the nonzero-fringe channel of `RE-045`--`RE-050`. A selector image containing one ordinary prime does not by itself identify an adjacent first-layer fan switch or a nonzero `\chi_p`. The present argument uses only the universal first-layer event attached to each ordinary prime and the genuine support chamber of the exposed state.

No Alaoglu--Erdos consecutive-quotient conjecture is used. The support boundaries may be first-layer, higher-layer, or tied events; intervening higher-layer events only shorten a chamber. Nor is any probabilistic or typical-gap hypothesis used. The proportional extraction in (10) is deterministic.

The half-unit staggering remains sharp at its own level: `\eta_q-q=1/2+o(1)` from below. What has changed is only the correct way to spend that fact. A possible terminal prime is a **point obstruction**, not a half-unit loss, when extracting one prime-free connected component.

## 7. Prior-art boundary and consequence

The CA supporting-slope/event chambers are classical Alaoglu--Erdos structure and are represented explicitly in Mantovanelli's 2026 prime-layer workload framework. Zimov's 2025 preprint studies restrictions from consecutive CA quotients near a hypothetical Robin exception. Runbo Li supplies the current `0.52` short-interval theorem used only for the `RE-051` corollary. All are already anchored in `SOURCES.md`.

A targeted current search of Robin/CA counterexamples, consecutive CA transitions, prime gaps, adaptive threshold envelopes, and the 2026 prime-layer event framework found no result coupling the width of a **false-RH adaptive threshold cell** to a proportional same-scale prime-free interval as in (10), nor the aggregate blockwise budget (12)--(13). The observation that an interval containing at most one prime has a prime-free component of at least half its length is elementary and is not itself a novelty claim. No new external theorem is load-bearing, so `SOURCES.md` needs no new dependency.

The mathematical delta is the removal of the only additive defect in the `RE-052` capacity law. Previously a highly fragmented fan could make `|S_C|<1/2` and render the individual bound `P_C\ge(|S_C|-1/2)_+` vacuous. The exact same CA source geometry actually gives `P_C\ge|S_C|/2` for every positive-width cell. This upgrades the local law into the aggregate requirement (12): regardless of fragmentation, a false-RH common block must realize a super-square-root total amount of pairwise disjoint prime-free selector length, while any external upper bound on individual prime gaps converts the same law back into a lower bound on fan complexity.