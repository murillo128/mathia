# RE-054 — threshold cells force synchronized prime gaps across CA layers

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + ADAPTIVE-THRESHOLD-CA + MULTISCALE-PRIME-EVENT-COUPLING + PRIME-FREE-INVERSE-LAYERS + SYNCHRONIZED-GAP-LADDER + AGGREGATE-SQUARE-ROOT-CAPACITY + SHORT-INTERVAL-STRESS-TEST + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-052` shows that every positive-width cell of the false-RH adaptive threshold fan consumes ordinary-prime-free selector length at the physical scale `Y=log C`. `RE-053` then shows that this first-layer metric information, even with PNT-scale label density and a pointwise gap exponent, is sharp as an information class: generalized first-layer labels can still carry a bounded fan on the near-critical side of the exponent barrier.

The genuine CA staircase contains more source information than that first-layer control. **The same ordinary primes generate an event in every fixed prime-power layer.** Pulling one exposed selector chamber back through each layer-event map therefore creates a synchronized family of ordinary-prime-free intervals at the scales

\[
Y,\quad (2Y)^{1/2},\quad (3Y)^{1/3},\quad\ldots .
\tag{1}
\]

For the second layer this gives a new unconditional square-root-scale burden for every threshold cell. It does not by itself improve the current short-interval exponent barrier: applying the same one-scale prime-gap upper bound separately to layer `j` gets weaker as `j` increases. The durable gain is instead a **cross-scale common-source constraint** absent from `RE-053`: one and the same fan cell must be compatible with prime deserts in several deterministically linked regions of the ordinary prime sequence.

Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{2}
\]

Fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2)
\tag{3}
\]

and work on a sufficiently late common positive CA block of `RE-040`. For an exposed state `C`, write

\[
Y:=\log C,
\qquad
h:=\log G(C)-\gamma>0,
\qquad
a:=1-e^{-h},
\tag{4}
\]

and let

\[
I_C:=\{b\in J:C\text{ is the rightmost maximizer of }A_b\},
\qquad
A_b(C)=Y^b(e^h-1).
\tag{5}
\]

For `b` in the interior of a positive-width cell, let `Z_C(b)` be the exact regular adaptive selector,

\[
g(Z_C(b))=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x},
\tag{6}
\]

and put

\[
S_C:=Z_C(I_C^\circ).
\tag{7}
\]

`RE-040` gives `Z_C(b)/Y->1` uniformly over the fan, while `RE-052` gives the selector speed. In fact retaining its asymptotic form rather than only its lower bound gives

\[
\boxed{
|S_C|
=(1+o_J(1))\,aY\log Y\,|I_C|.
}
\tag{8}
\]

Now fix an integer layer `j>=1`. Extend the exact CA layer increment from primes to real `x>1` by

\[
\lambda_j(x)
:=
\log\!\left(
1+\frac1{x+x^2+\cdots+x^j}
\right),
\tag{9}
\]

and define its real event coordinate `eta_j(x)` by

\[
\boxed{
\eta_j(x)\log\eta_j(x)
=
\frac{\log x}{\lambda_j(x)}.
}
\tag{10}
\]

For an ordinary prime `p`, `eta_j(p)` is exactly the genuine CA event where the `j`-th abundance layer at `p` fires. For every fixed `j`, the map `eta_j` is eventually strictly increasing and

\[
\boxed{
\eta_j(x)
=
\frac{x^j}{j}\left(1+O_j\!\left(\frac1{\log x}\right)\right),
\qquad
\eta_j'(x)
=
x^{j-1}\left(1+O_j\!\left(\frac1{\log x}\right)\right).
}
\tag{11}
\]

Define the layer-`j` inverse selector interval

\[
\boxed{
Q_{C,j}:=\eta_j^{-1}(S_C).
}
\tag{12}
\]

Then, for every fixed `j` and every sufficiently late positive-width exposed cell,

\[
\boxed{
Q_{C,j}\cap\mathbb P=\varnothing.
}
\tag{13}
\]

Moreover the interval is centered at the deterministic layer scale

\[
q=(jY)^{1/j}(1+o_{J,j}(1))
\quad(q\in Q_{C,j}),
\tag{14}
\]

and its length satisfies the asymptotic law

\[
\boxed{
|Q_{C,j}|
=
\left(j^{-(j-1)/j}+o_{J,j}(1)\right)
 a\,|I_C|\,Y^{1/j}\log Y.
}
\tag{15}
\]

The quantitative false-RH inheritance in `RE-040` gives uniformly

\[
a\gg_JY^{-b_1},
\tag{16}
\]

so

\[
\boxed{
|Q_{C,j}|
\gg_{J,j}
|I_C|Y^{1/j-b_1}\log Y.
}
\tag{17}
\]

In particular the second layer is always on the growing side because `b_1<1/2`:

\[
\boxed{
Q_{C,2}\cap\mathbb P=\varnothing,
\qquad
Q_{C,2}\text{ lies at }(2Y)^{1/2}(1+o_J(1)),
}
\tag{18}
\]

\[
\boxed{
|Q_{C,2}|
=
\left(2^{-1/2}+o_J(1)\right)
 a|I_C|\sqrt Y\log Y
\gg_J
|I_C|Y^{1/2-b_1}\log Y.
}
\tag{19}
\]

Thus the same adaptive cell that consumes a prime-free interval near `Y` also consumes, deterministically, another prime-free interval near `sqrt(2Y)`. This square-root companion is forced by the genuine common prime source; it is not an additional assumption about prime gaps.

## 1. Fixed layer events have an explicit inverse scale and Jacobian

For fixed `j`, let

\[
S_j(x):=x+x^2+\cdots+x^j.
\tag{20}
\]

As `x->infinity`,

\[
S_j(x)=x^j(1+O_j(x^{-1})),
\tag{21}
\]

so

\[
\lambda_j(x)
=\log(1+S_j(x)^{-1})
=x^{-j}(1+O_j(x^{-1})).
\tag{22}
\]

Hence the right side of (10) is

\[
R_j(x):=\frac{\log x}{\lambda_j(x)}
=x^j\log x\,(1+O_j(x^{-1})).
\tag{23}
\]

Since `u mapsto u log u` is strictly increasing for large `u`, equation (10) has a unique large solution. Evaluating at `x^j/j` gives

\[
\frac{x^j}{j}\log\frac{x^j}{j}
=x^j\log x\left(1+O_j((\log x)^{-1})\right),
\tag{24}
\]

which proves the first asymptotic in (11).

Differentiating (10) gives

\[
\eta_j'(x)
=
\frac{R_j'(x)}{\log\eta_j(x)+1}.
\tag{25}
\]

Differentiating (23), using the differentiable expansion inherited from (22), yields

\[
R_j'(x)
=x^{j-1}(j\log x+1)
\left(1+O_j((\log x)^{-1})\right).
\tag{26}
\]

The first part of (11) gives

\[
\log\eta_j(x)+1
=j\log x+O_j(1),
\tag{27}
\]

and therefore the derivative formula in (11). In particular `eta_j'(x)>0` eventually. The real interpolation is used only to measure interval lengths; at prime arguments it is the exact arithmetic CA event map.

Let an interval `S` have all of its points equal to `Y(1+o(1))`, and let `Q=eta_j^{-1}(S)`. Equations (11) and the mean-value theorem give uniformly for fixed `j`

\[
q=(jY)^{1/j}(1+o_j(1))
\quad(q\in Q),
\tag{28}
\]

and

\[
\boxed{
|Q|
=
\left(j^{-(j-1)/j}+o_j(1)\right)
Y^{-(j-1)/j}|S|.
}
\tag{29}
\]

Applying this to `S=S_C` and inserting (8) proves (14)--(15).

## 2. A genuine support chamber is event-free in every layer

Let

\[
\xi_-(C)<\xi_+(C)
\tag{30}
\]

be the adjacent genuine CA event coordinates supporting `C`. Simultaneous regularity in `RE-040` gives

\[
S_C\subset(\xi_-(C),\xi_+(C)).
\tag{31}
\]

By definition of adjacent support events, the open interval in (31) contains **no CA event of any prime-power layer**. Suppose, contrary to (13), that an ordinary prime `p` lies in `Q_{C,j}`. Then by definition of the inverse interval

\[
\eta_j(p)\in S_C.
\tag{32}
\]

But `eta_j(p)` is a genuine layer-`j` CA event coordinate, contradicting (31). Thus `Q_{C,j}` is an ordinary-prime-free interval.

This is stronger than merely observing that higher-layer transitions are sparse. It uses the same ordinary prime set twice: first to define the layer event `eta_j(p)`, and then to assert that absence of events in the selected CA chamber means absence of ordinary primes in its inverse image. No probabilistic independence or distribution hypothesis enters.

Ties cause no problem. Several layer events may coincide at `xi_-` or `xi_+`, but `S_C` lies in the open chamber, so only interior events would contradict support. Endpoint primes are irrelevant to the open prime-free interval and to its length.

## 3. The adaptive selector supplies the width of every inverse gap

Inside one cell the state variables `Y,h,a` are fixed. Differentiating (6), exactly as in `RE-052`, gives

\[
Z_C'(b)
=
\frac{aZ_C(b)^2(\log Z_C(b))^2}
{Y(\log Z_C(b)+1)}.
\tag{33}
\]

Uniformly over the compact fan, `Z_C(b)/Y->1`, hence

\[
Z_C'(b)
=(1+o_J(1))aY\log Y.
\tag{34}
\]

Integrating over `I_C^\circ` proves (8). Combining (8) with the layer Jacobian (29) proves (15).

The quantitative inheritance is the same one used in `RE-040` and `RE-052`. If `R=e^h-1`, every selected state satisfies

\[
Y^bR\ge c_0
\quad(b\in J)
\tag{35}
\]

for one block-independent `c_0>0`, and therefore

\[
R\ge c_0Y^{-b_1}.
\tag{36}
\]

Since the whole late fan is in the uniform small-height regime, `a=R/(1+R)=(1+o(1))R`, proving (16) and (17).

For `j=2`, (15) becomes

\[
|Q_{C,2}|
=
(2^{-1/2}+o_J(1))a|I_C|\sqrt Y\log Y,
\tag{37}
\]

and (16) produces (19). Thus any sequence of cells whose threshold width is bounded below forces square-root-scale prime gaps tending to infinity at least as `Y^(1/2-b_1) log Y`. More generally, for every fixed layer with `1/j>b_1`, a nonvanishing threshold width forces a growing ordinary prime-free interval at scale `Y^(1/j)`.

## 4. The square-root burden also survives arbitrary fan fragmentation in aggregate

Distinct exposed states have disjoint selector images `S_C`, because they lie in distinct open CA support chambers. Since `eta_j` is eventually increasing, their inverse intervals `Q_{C,j}` are pairwise disjoint for every fixed `j`.

Let

\[
X_{\mathcal B}:=
\min_{C\in\mathcal E(\mathcal B,J)}Y_C
\tag{38}
\]

on a sufficiently late common block. If `1/j>b_1`, the function

\[
Y^{1/j-b_1}\log Y
\tag{39}
\]

is eventually increasing. Summing (17) and using the threshold partition

\[
\sum_C|I_C|=|J|
\tag{40}
\]

therefore gives

\[
\boxed{
\sum_C|Q_{C,j}|
\gg_{J,j}
X_{\mathcal B}^{1/j-b_1}\log X_{\mathcal B}.
}
\tag{41}
\]

The universal nontrivial case is `j=2`:

\[
\boxed{
\sum_C|Q_{C,2}|
\gg_J
X_{\mathcal B}^{1/2-b_1}\log X_{\mathcal B}
\longrightarrow\infty.
}
\tag{42}
\]

Thus fragmenting `J` into arbitrarily many thin cells cannot remove the total square-root-layer prime-free demand; it only distributes that demand among many disjoint intervals near the square-root images of the exposed selector chambers.

Equation (42) is a length statement, not a count of distinct consecutive-prime gaps. Two disjoint subintervals can in principle extend into the same larger ordinary gap, so no independence or gap-counting conclusion is being smuggled into the aggregation.

## 5. Independent pointwise gap bounds do not improve the `RE-051` frontier

The multiscale ladder must be stress-tested against the current short-interval input before treating it as a route through the near-critical band. Suppose `theta in (1/2,1)` is such that every sufficiently large interval `[x-x^theta,x]` contains a prime. Then every prime-free interval at local scale `x` has length `O(x^theta)`.

The interval `Q_{C,j}` lies at scale

\[
x_j\asymp Y^{1/j},
\tag{43}
\]

so (17) and the pointwise gap ceiling give

\[
|I_C|Y^{1/j-b_1}\log Y
\ll_{J,j}Y^{\theta/j}.
\tag{44}
\]

Therefore

\[
\boxed{
|I_C|
\ll_{J,j}
\frac{Y^{\,b_1-(1-\theta)/j}}{\log Y}.
}
\tag{45}
\]

For `j=1`, this is exactly the exponent from `RE-051`--`RE-052`:

\[
b_1+\theta-1.
\tag{46}
\]

For every `j>=2`, the saving `(1-theta)/j` is smaller, so the condition making the exponent in (45) negative is **strictly stronger** than the first-layer condition `b_1<1-theta`. Consequently no argument that merely applies the same pointwise prime-gap theorem independently at each layer can improve the `Theta>theta` frontier of `RE-051`.

With the currently anchored unconditional `theta=0.52`, the second layer would require `b_1<0.24`, whereas the first layer already becomes effective for `b_1<0.48`. The square-root interval is therefore new arithmetic structure but not a stronger one-scale contradiction.

This negative check is load-bearing for interpretation. The useful datum is not that layer two gives another gap in isolation; it is that **the gap near `Y` and the gap near `sqrt(2Y)` are forced by the same exposed CA state and the same selector chamber**, with analogous companions in every fixed layer. A continuation must exploit a theorem about such linked multiscale gaps, or splice the full layer synchronization directly into the standard/reciprocal prime-race source. Reusing one-scale worst-case bounds cannot suffice.

## 6. Relation to the earlier gap/depth ladder and to the generalized control

`RE-017` also couples ordinary prime gaps to higher CA layers, but in a different geometry. It starts from a regular **self-tangent local Robin peak**, envelopes its two adjacent CA transitions by consecutive first-layer primes, and shows that a small enclosing ordinary gap forces the actual boundary factors into deeper layers. The present result starts instead from an exposed **adaptive threshold cell** and pulls its entire selector image backward through each fixed layer map. It therefore produces simultaneous prime-free intervals at several physical scales even when the two support boundaries themselves are not in those layers.

`RE-053` matches the threshold fan, small-height regime, exact adaptive selector, exact generalized first-layer mass/slope/event formulas, PNT-scale label density, and a prescribed worst-case gap exponent. It deliberately does not impose the higher-layer arithmetic of the same ordinary prime set. Equations (12)--(19) identify one precise piece of missing source data: a genuine first-layer support chamber automatically has prime-free inverse images under every fixed higher-layer event map.

This does not yet prove that no richer generalized-prime control can reproduce the same multiscale pattern. It instead raises the bar for a matched control: matching only first-layer labels is no longer enough to test a proposed common-source argument that uses (13). Any such control would have to reproduce the cross-layer event maps and their synchronized prime-free inverse intervals as well.

## 7. Prior-art boundary and research consequence

The layer increment (9), event equation (10), and prime-layer interpretation are classical CA variational structure in Alaoglu--Erdos and are represented explicitly in the recent Mantovanelli prime-layer workload framework; both are already anchored in `SOURCES.md`. `RE-017` previously used the same event-size law to derive a boundary-depth constraint, while `RE-037` used the moving second-layer cutoff to isolate the universal `sqrt(2)` CA correction. No novelty is claimed for the asymptotic scale `eta_j(p)~p^j/j` by itself.

A targeted current search of CA/Robin prime-layer work, higher-layer transition formulas, prime gaps, and simultaneous prime-free intervals found the existing prime-layer framework and neighboring consecutive-CA results, but no result pulling an **adaptive threshold support chamber** back through all fixed CA layer maps to obtain the synchronized prime-gap law (13)--(19) or its aggregate square-root consequence (42). No new external theorem is load-bearing, so `SOURCES.md` requires no addition.

The line-specific delta is therefore structural rather than a new prime-gap estimate. `RE-052` priced each threshold cell in first-layer ordinary-gap currency and `RE-053` showed the limit of that currency. The present finding shows that a genuine cell must pay **several linked ordinary-gap bills at once**, with the second invoice living near `sqrt(2Y)` and retaining positive aggregate power because every admissible threshold satisfies `b<1/2`.

This still does not prove Robin's inequality or exclude the near-critical chamber `1/2<Theta<=0.52`. The next useful theorem would have to exploit dependence between these synchronized gaps, or couple them to the same ordinary-prime standard/reciprocal race that already satisfies the uniform nonlinear selector law of `RE-040`. What is now ruled out as sufficient is another independent insertion of a one-scale worst-case prime-gap ceiling.