# RE-052 — threshold-cell width forces same-scale prime-free selector intervals

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + PRIME-EVENT-COUPLING + PRIME-FREE-SELECTOR-CAPACITY + CELL-WIDTH/GAP-TRADEOFF + FULL-OFF-CRITICAL-CHAMBER + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-051` uses an unconditional prime-in-short-interval theorem to show that, when the hypothetical rightmost zero frontier lies beyond the available short-interval exponent, every exposed adaptive threshold cell must be small. The argument can be factored one level earlier, before inserting any external prime-gap bound. The exact first-layer staggering and the adaptive selector speed imply a source-specific local law: **a wide threshold cell itself creates a long ordinary-prime-free interval at the same physical scale.**

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

Let `xi_-(C)<xi_+(C)` be the adjacent genuine CA event coordinates supporting `C`. Then `S_C` is an interval contained in the open support chamber `(xi_-,xi_+)`, and uniformly over every exposed positive-width cell,

\[
\boxed{
|S_C|
\gg_J
|I_C|\,Y^{1-b_1}\log Y.
}
\tag{7}
\]

The same support chamber has a prime-free core. For every sufficiently late state,

\[
\boxed{
(\xi_-(C),\,\xi_+(C)-1/2]
\quad\text{contains no ordinary prime.}
}
\tag{8}
\]

Consequently `S_C` contains an ordinary-prime-free subinterval of length `P_C` satisfying

\[
\boxed{
P_C+\frac12
\ge |S_C|
\gg_J
|I_C|\,Y^{1-b_1}\log Y.
}
\tag{9}
\]

Equations (7)--(9) are the local capacity law. They require no theorem about how small prime gaps actually are. They say instead that the false-RH adaptive fan must **pay for threshold width with genuine prime-free physical length**.

A macroscopic threshold cell therefore has a strong arithmetic consequence. If along an escaping block sequence one has

\[
|I_C|\ge\delta>0,
\tag{10}
\]

then, since `b_1<1/2`,

\[
\boxed{
P_C\gg_{J,\delta}Y^{1-b_1}\log Y,
\qquad
\frac{P_C}{\sqrt Y}\longrightarrow\infty.
}
\tag{11}
\]

Because `RE-040` gives `Z_C(b)/Y->1` uniformly, this is a **same-scale** prime-free interval: it lies at ordinates `(1+o_J(1))Y`, not at some unrelated later scale. Hence it is contained in an ordinary consecutive-prime gap of at least the same length.

This immediately turns the bounded-complexity escape left open by `RE-038`--`RE-041` into a prime-gap alternative valid throughout the entire false-RH chamber. If the number of exposed cells on `J` is bounded by one fixed `K` on infinitely many common blocks, then one cell on each such block has width at least `|J|/K`, and therefore there are infinitely many ordinary prime gaps at selected scales `x` satisfying

\[
\boxed{
p_{n+1}-p_n
\gg_J x^{1-b_1}\log x.
}
\tag{12}
\]

Given any `epsilon>0`, `J` may be chosen with

\[
1-\Theta<b_0<b_1<1-\Theta+\epsilon,
\tag{13}
\]

so bounded fan complexity would force infinitely many gaps

\[
\boxed{
p_{n+1}-p_n
\gg_{J,\epsilon}p_n^{\Theta-\epsilon}}
\tag{14}
\]

(up to the harmless stronger logarithmic factor before converting scales). Thus a bounded coherent false-RH fan can survive only by transferring the off-critical zero frontier almost directly into the ordinary prime-gap exponent.

This clarifies the near-critical chamber left open by `RE-051`. With the current unconditional short-interval exponent `0.52`, the case `Theta>0.52` cannot sustain bounded cells and `RE-051` gives the stronger polynomial cell-count theorem. When `1/2<Theta<=0.52`, the bounded-fan escape is no longer featureless: it requires source-selected prime gaps at exponents arbitrarily close below `Theta`, hence strictly beyond the square-root scale. Present unconditional technology does not exclude those gaps.

## 1. The selector image expands at speed `a Y log Y`

For a fixed exposed state `C`, the quantities `Y`, `h`, and `a` do not vary while `b` moves inside `I_C`. Differentiate the exact selector equation (5). Since

\[
g'(x)
=-\frac{\log x+1}{x^2(\log x)^2},
\tag{15}
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
\tag{16}
\]

`RE-040` proves uniformly on the whole compact fan that

\[
\frac{Z_C(b)}Y\longrightarrow1.
\tag{17}
\]

Therefore

\[
\boxed{
Z_C'(b)
=(1+o_J(1))aY\log Y.
}
\tag{18}
\]

The quantitative false-RH inheritance on the common blocks gives one constant `c_0>0` such that every selected state satisfies

\[
A_b(C)=Y^b(e^h-1)\ge c_0.
\tag{19}
\]

Put `R=e^h-1`. Since `b<=b_1`,

\[
R\ge c_0Y^{-b_1}.
\tag{20}
\]

The uniform small-height regime gives `R->0`, and

\[
a=\frac R{1+R},
\]

so eventually

\[
\boxed{a\gg_JY^{-b_1}.}
\tag{21}
\]

Combining (18)--(21),

\[
Z_C'(b)
\gg_J
Y^{1-b_1}\log Y
\tag{22}
\]

throughout the interior of the cell. Since `Z_C` is increasing, integrating over `I_C` proves (7):

\[
|S_C|
=
\int_{I_C^\circ}Z_C'(b)\,db
\gg_J
|I_C|Y^{1-b_1}\log Y.
\tag{23}
\]

Breakpoint endpoints have zero measure and do not affect the identity. Degenerate zero-width cells contribute nothing.

The point of (23) is different from the support-width upper bound used in `RE-051`. Here the false-RH amplitude is used in the forward direction: a given amount of threshold occupancy forces a minimum amount of physical selector travel.

## 2. A genuine CA support chamber is prime-free except possibly in its final half unit

By the simultaneous regularity theorem of `RE-040`, for every `b in I_C^circ` the selector lies strictly inside the genuine CA support chamber,

\[
\xi_-<Z_C(b)<\xi_+.
\tag{24}
\]

We now use the exact first-layer source coupling from `RE-042`. For every sufficiently large ordinary prime `q`, its first-layer CA event coordinate satisfies

\[
\boxed{q<\eta_q<q+\frac12.}
\tag{25}
\]

Suppose, toward a contradiction, that an ordinary prime lies in the nonterminal part of the chamber:

\[
\xi_-<q\le\xi_+-\frac12.
\tag{26}
\]

Then (25) gives

\[
\xi_-<q<\eta_q<q+\frac12\le\xi_+.
\tag{27}
\]

But `eta_q` is itself a genuine first-layer CA event coordinate. Equation (27) would place a CA event strictly between the two adjacent support events `xi_-` and `xi_+`, impossible by definition of the chamber. This proves (8).

No assumption is made that either support boundary is first-layer. Higher-layer and tied events are allowed. Nor is the Alaoglu--Erdos conjecture on consecutive CA quotients used. The argument needs only that every ordinary prime has its own first-layer event less than one half-unit to its right.

Since `S_C` is an interval inside `(xi_-,xi_+)`, removing the terminal half-unit `(xi_+-1/2,xi_+)` deletes length at most `1/2`. What remains is an interval contained in the prime-free core (8). If its length is denoted by `P_C`, then

\[
P_C\ge(|S_C|-1/2)_+,
\tag{28}
\]

or equivalently

\[
P_C+\frac12\ge|S_C|.
\tag{29}
\]

Combining (29) with (23) proves the capacity law (9).

The half-unit loss is real at the present level of information. `RE-044`--`RE-049` show exactly why: an ordinary prime can occur in the final half-unit while its associated first-layer event still lies beyond the selected point. Removing that fringe uniformly is therefore not justified.

## 3. Bounded fan complexity transfers the zero frontier into ordinary prime gaps

Assume that on infinitely many late common blocks the fan on fixed `J` exposes at most `K` states. The rightmost-maximizer cells partition `J` up to endpoints, so on each block at least one state `C` satisfies

\[
|I_C|\ge\frac{|J|}{K}.
\tag{30}
\]

Applying (9),

\[
P_C
\gg_{J,K}
Y^{1-b_1}\log Y.
\tag{31}
\]

The selected blocks escape to infinity, hence so do these `Y`. The prime-free interval lies inside `S_C`, and (17) places all of `S_C` at `(1+o_J(1))Y`. Let `p_n<p_{n+1}` be the consecutive ordinary primes bracketing this prime-free interval. Since `P_C=o(Y)` at the exponent displayed in (31) and the interval itself is at scale `Y`, both bracketing primes are also `(1+o_J(1))Y` after harmlessly shortening the interval if necessary. Thus

\[
p_{n+1}-p_n\ge P_C
\gg_{J,K}
p_n^{1-b_1}\log p_n,
\tag{32}
\]

which is (12).

Now fix `epsilon>0`. Because `J` may be any compact subinterval of `(1-Theta,1/2)`, choose its right endpoint so that

\[
1-\Theta<b_1<\min\left(\frac12,1-\Theta+\epsilon\right).
\tag{33}
\]

Then

\[
1-b_1>\Theta-\epsilon.
\tag{34}
\]

Equation (32) therefore implies (14). This is not a theorem that false RH itself forces such gaps: the conclusion is conditional on **bounded exposed fan complexity**. Its role is to identify the exact arithmetic price of that escape.

There is also a useful local formulation with no bounded-complexity hypothesis. If a sequence of exposed cells satisfies

\[
|I_C|Y^{1/2-b_1}\log Y\longrightarrow\infty,
\tag{35}
\]

then (9) yields

\[
\boxed{P_C/\sqrt Y\longrightarrow\infty.}
\tag{36}
\]

Thus any threshold cell wider than the scale

\[
Y^{b_1-1/2}/\log Y
\tag{37}
\]

by a divergent factor necessarily produces a same-scale prime-free interval beyond square-root length.

## 4. `RE-051` is recovered by inserting a prime-gap capacity theorem

The new law is deliberately prior to any short-interval theorem. Suppose one has an exponent `theta in (1/2,1)` such that every sufficiently large interval `[x-x^theta,x]` contains a prime. At selector scale `Z~Y`, this gives a uniform upper bound

\[
P_C\ll Y^\theta
\tag{38}
\]

for the prime-free interval in (9). Hence

\[
|I_C|Y^{1-b_1}\log Y
\ll_J
Y^\theta+1,
\]

and therefore

\[
\boxed{
|I_C|
\ll_J
\frac{Y^{b_1+\theta-1}}{\log Y}.
}
\tag{39}
\]

This is exactly the cell-width estimate underlying `RE-051`. When `b_1<1-theta`, summing the cells over the fixed interval `J` gives its polynomial fan-complexity lower bound.

Thus `RE-051` can be read as the strong-off-critical consequence of the more primitive source law (9). The exponent barrier is now transparent. With Runbo Li's current unconditional `theta=0.52`, prime-gap capacity rules out a macroscopic cell whenever `b_1<0.48`. If `Theta<=0.52`, every admissible `J` begins at `1-Theta>=0.48`, so this external capacity theorem no longer beats the lower physical travel forced by (9). The remaining near-critical escape is precisely the possibility of ordinary gaps between square-root size and the current `x^0.52` frontier at the CA-selected scales.

## 5. Stress tests and exact boundary

This result does not prove that the fan has bounded complexity, nor does it prove that the near-critical prime gaps required by a bounded fan exist. It is a deterministic alternative: **threshold occupancy and ordinary prime-free capacity cannot both be small.** A fan may avoid long gaps by fragmenting `J` into many sufficiently thin cells, including skipped-state, higher-layer, or tied transitions.

The theorem is independent of the nonzero-fringe channel of `RE-045`--`RE-050`. It does not show that many exposed states generate many `chi_p=1` bits. Instead it supplies a second source-sensitive currency for the full fan: every cell has a prime-free-capacity cost even when all fringe bits vanish. This is why it directly addresses the separation recorded in `MI-001` between cell complexity and sparse base-two interruptions without falsely identifying the two counts.

The prime-free interval is obtained from the **selector image** of one cell, not from the whole CA support chamber. This distinction is essential: the fan may use only a tiny portion of a large chamber, and support width alone does not imply threshold occupancy. Conversely, (7) uses amplitude maximality through the false-RH lower bound on `a`; an arbitrary synthetic staircase such as the controls of `RE-041` is not forced to satisfy the same ordinary-prime/event coupling (25).

Equation (14) should not be read as an unconditional lower bound for maximal prime gaps. It is conditional on false RH plus a bounded coherent fan. Nor does a prime-free interval by itself locate a special first-layer switch or a nonzero fringe bit. The only source label needed is the universal first-layer event attached to every ordinary prime.

Finally, the terminal `1/2` loss cannot currently be sharpened to zero uniformly. The exact first-layer stagger is `eta_q-q=1/2+o(1)` from below, and the endpoint-fringe configurations of `RE-044`--`RE-049` show that a prime may legitimately occupy that last half-unit before its CA event fires.

## 6. Prior-art boundary and consequence

The CA supporting-slope/event chambers are classical Alaoglu--Erdos structure and are represented explicitly in Mantovanelli's 2026 prime-layer workload framework. Zimov's 2025 preprint studies restrictions from consecutive CA quotients near a hypothetical Robin exception. Runbo Li supplies the current `0.52` short-interval theorem used only when deriving the `RE-051` corollary. All are already anchored in `SOURCES.md`.

A targeted current literature search of Robin/CA counterexamples, consecutive CA transitions, prime gaps, and the 2026 prime-layer event framework found no result coupling the **width of an adaptive false-RH threshold cell** to a same-scale ordinary-prime-free selector interval as in (9), nor the bounded-fan transfer (14). No new external theorem is load-bearing for (7)--(14), so `SOURCES.md` needs no new dependency.

The mathematical delta is the factorization of the fan-capacity problem into two exact currencies. `RE-051` says a sufficiently strong external prime-gap upper bound forces many cells. `RE-052` identifies the prior source law valid without that upper bound: a cell of threshold width `w` must consume at least order

\[
wY^{1-b_1}\log Y
\]

of physical selector length, and all but at most one half-unit of that length is ordinary-prime-free. In the near-critical chamber this converts the old bounded-fan escape into a concrete arithmetic demand for prime gaps approaching the hypothetical zero-frontier exponent, rather than leaving bounded fan complexity as an abstract convex-envelope possibility.