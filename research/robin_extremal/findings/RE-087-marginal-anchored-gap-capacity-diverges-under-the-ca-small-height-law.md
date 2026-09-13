# RE-087 — marginal anchored-gap capacity diverges under the CA small-height law

**Status:** `EXACT-DERIVED + FIXED-LAYER + PRIME-GAP-TELESCOPING + UNIFORM-SMALL-HEIGHT + MARGINAL-CAPACITY-DIVERGENCE + NEGATIVE/ROUTE-NARROWING + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-085` shows that higher-layer physical mass disappears from every bounded fixed-order observable on a stretched late fan, so any surviving higher-layer mechanism must be singular. `RE-086` isolates one such mechanism: if a fixed-layer event `eta_j(p)` is actually selected as a support boundary, then the chamber-facing ordinary prime gap at its generating base prime must satisfy

\[
\frac{\mathcal G_C(p,j)}{p\log p}
\ge (1-o_J(1))a(C)|I_C|,
\qquad
a(C)=1-e^{-h(C)}.
\tag{1}
\]

A natural next hope is to sum these one-sided gap constraints over possible boundary primes and show that ordinary prime gaps provide too little total threshold capacity to carry a fixed-width false-RH fan. That route does **not** work at the marginal gap-size level. The uniform CA small-height law from `RE-040` makes the opposite true: after converting ordinary gap length into threshold width by dividing by the selected amplitude, the total candidate capacity in every fixed-layer dyadic base-prime shell diverges.

Fix a layer `j>=1`. For an ordinary prime `p`, write

\[
d^-(p):=p-p^-,
\qquad
d^+(p):=p^+-p
\tag{2}
\]

for its previous- and next-prime gaps. Define the two marginal normalized gap budgets on a dyadic shell by

\[
B^\pm(P)
:=
\sum_{P<p\le2P}
\frac{d^\pm(p)}{p\log p}.
\tag{3}
\]

Then the prime number theorem and telescoping of consecutive prime gaps give

\[
\boxed{
B^-(P)\asymp\frac1{\log P},
\qquad
B^+(P)\asymp\frac1{\log P}.
}
\tag{4}
\]

No short-interval theorem and no pointwise prime-gap bound are needed.

On the other hand, `RE-040` proves globally over sufficiently large positive CA states that

\[
h(C)\log Y_C\longrightarrow0,
\qquad Y_C:=\log C,
\tag{5}
\]

and hence also

\[
a(C)\log Y_C\longrightarrow0.
\tag{6}
\]

For a fixed-layer boundary event `eta_j(p)` with `P<p<=2P`, `RE-086` gives

\[
Y_C=\frac{p^j}{j}(1+o_J(1)),
\tag{7}
\]

so uniformly on such candidates

\[
\boxed{
a(C)\log P\longrightarrow0.}
\tag{8}
\]

Let `alpha_j(P)` be any eventual amplitude envelope for positive CA states at this fixed-layer physical scale, chosen so that

\[
a(C)\le\alpha_j(P)
\quad\text{whenever}\quad
Y_C\asymp_j P^j,
\qquad
\alpha_j(P)\log P\longrightarrow0.
\tag{9}
\]

Such an envelope exists by (5)--(8). The total **marginal threshold-width capacity** supplied by one orientation of the ordinary prime gaps is then

\[
\mathfrak C_j^\pm(P)
:=
\sum_{P<p\le2P}
\frac{d^\pm(p)}{\alpha_j(P)p\log p}
=
\frac{B^\pm(P)}{\alpha_j(P)}.
\tag{10}
\]

Combining (4) and (9),

\[
\boxed{
\mathfrak C_j^-(P)\to\infty,
\qquad
\mathfrak C_j^+(P)\to\infty.
}
\tag{11}
\]

Thus even if every candidate layer-`j` boundary is charged to a distinct base prime and only one chamber orientation is allowed, the sum of the individual `RE-086` width ceilings eventually exceeds any fixed threshold interval length. Equivalently, for every fixed `L>0` and all sufficiently large `P`, there are nonnegative widths `w_p`, supported on primes `P<p<=2P`, such that

\[
\sum_p w_p=L,
\qquad
\alpha_j(P)w_p
\le
\frac{d^\pm(p)}{p\log p}
\tag{12}
\]

for every used prime. Since an actual selected amplitude satisfies `a(C)<=alpha_j(P)`, the entire allocation passes the **marginal** anchored-gap inequality (1).

This is a negative but useful conclusion. `RE-086` remains a genuine singular arithmetic constraint, but its force cannot come from the total amount of one-sided ordinary-gap length available at one fixed layer. Any successful continuation must exploit **which** event primes the rightmost-maximizer fan selects, joint/tied resonances across power-related scales, or another adjacency/nonlocal condition that is lost when the inequalities are summed independently.

## 1. Consecutive prime gaps provide `1/log P` normalized mass in every dyadic shell

Let

\[
p_0<p_1<\cdots<p_m
\tag{13}
\]

be consecutive primes with

\[
p_0\le P<p_1,
\qquad
p_m\le2P<p_{m+1}.
\tag{14}
\]

For the previous-gap orientation,

\[
\sum_{P<p\le2P}d^-(p)
=
\sum_{i=1}^m(p_i-p_{i-1})
=
p_m-p_0.
\tag{15}
\]

The prime number theorem implies

\[
p_0=P(1+o(1)),
\qquad
p_m=2P(1+o(1)),
\tag{16}
\]

and therefore

\[
\sum_{P<p\le2P}d^-(p)
=P(1+o(1)).
\tag{17}
\]

Since every denominator in (3) lies between `P log P` and `2P log(2P)`, equations (3) and (17) give two absolute positive constants `c,C` such that

\[
\frac{c}{\log P}
\le B^-(P)
\le\frac{C}{\log P}
\tag{18}
\]

for all sufficiently large `P`.

The next-gap orientation is identical after shifting one endpoint:

\[
\sum_{P<p\le2P}d^+(p)
=
\sum_{i=1}^m(p_{i+1}-p_i)
=
p_{m+1}-p_1
=P(1+o(1)),
\tag{19}
\]

again by the prime number theorem. This proves (4).

The point is not the exact constant. The normalized one-sided gaps carry only `Theta(1/log P)` total mass in a dyadic shell. If the right side of (1) had an amplitude bounded below by a constant, this budget would vanish. The CA fan has exactly the opposite scaling: its positive height, and hence `a(C)`, tends to zero faster than `1/log Y`.

## 2. The CA small-height law reverses the apparent scarcity

`RE-040` reconstructs the global estimate

\[
h(C)\log Y_C\to0
\tag{20}
\]

for sufficiently large positive CA states, uniformly on the late common blocks used by the false-RH fan. Because

\[
0<a(C)=1-e^{-h(C)}\le h(C),
\tag{21}
\]

we also have

\[
a(C)\log Y_C\to0.
\tag{22}
\]

Now suppose an adjacent support boundary is the fixed-depth event `eta_j(p)` with `P<p<=2P`. The fixed-layer event asymptotic used in `RE-086` gives

\[
Y_C\asymp_j P^j,
\qquad
\log Y_C=j\log P+O_j(1).
\tag{23}
\]

Consequently the convergence in (22) is uniform on this shell and yields an envelope `alpha_j(P)` satisfying (9).

For intuition, write

\[
\alpha_j(P)=\frac{\varepsilon_j(P)}{\log P},
\qquad
\varepsilon_j(P)\to0.
\tag{24}
\]

Then (4) and (10) give

\[
\boxed{
\mathfrak C_j^\pm(P)
\asymp
\frac1{\varepsilon_j(P)}
\longrightarrow\infty.
}
\tag{25}
\]

So the `1/log P` scarcity of normalized ordinary-gap mass is cancelled by the `o(1/log P)` selected amplitude, and more than cancelled: the resulting amount of admissible threshold width diverges.

This remains true in the slowest decay regime permitted by the present small-height theorem. For example, if along some shell

\[
a(C)\asymp\frac1{\log Y\,L(Y)}
\tag{26}
\]

with any `L(Y)->infty`, then the marginal shell capacity grows like `L(P^j)` up to constants. In the quantitative false-RH lower-scale regime used elsewhere in the line, where `a` is of polynomial order `Y^{-b}`, the surplus is much larger:

\[
\mathfrak C_j^\pm(P)
\asymp
\frac{P^{jb}}{\log P}
\tag{27}
\]

at the level of exponents.

The divergence in (11) is therefore not an artefact of assuming exceptionally small heights. It already follows from the weakest global small-height information currently built into the CA fan.

## 3. A fixed-width threshold interval can be allocated inside the marginal gap budget

Equation (11) has a direct falsification consequence for an aggregate-capacity proof based only on (1). Fix one orientation, say the outgoing side, and define the individual abstract capacities

\[
c_p
:=
\frac{d^-(p)}{\alpha_j(P)p\log p},
\qquad P<p\le2P.
\tag{28}
\]

Then

\[
\sum_pc_p=\mathfrak C_j^-(P)\to\infty.
\tag{29}
\]

Given any fixed `L>0`, for large enough `P` choose

\[
w_p
:=
\frac{L}{\mathfrak C_j^-(P)}c_p.
\tag{30}
\]

The scaling factor is at most one, so

\[
0\le w_p\le c_p,
\qquad
\sum_pw_p=L.
\tag{31}
\]

Multiplying by `alpha_j(P)` gives exactly (12). Therefore the family of marginal necessary inequalities admits an abstract full-width allocation using distinct ordinary primes from a **single dyadic base-prime shell**.

This construction is deliberately not claimed to be a CA fan. It ignores support ordering, rightmost-maximizer selection, exact event coincidences, the other support boundary, and all cross-layer constraints. That is precisely the falsification test: a proof that merely sums the individual anchored-gap inequalities cannot distinguish the true fan from this allocation, so such a proof cannot close the singular channel.

In physical coordinates the shell is still local up to a fixed multiplicative factor. For fixed `j`,

\[
\eta_j(P)\asymp_j P^j,
\qquad
\eta_j(2P)\asymp_j 2^jP^j.
\tag{32}
\]

Thus the divergence does not rely on pooling candidate events over arbitrarily many decades of physical scale. It is already present in one bounded-ratio event shell.

## 4. What survives from `RE-086`

The result does **not** weaken the exact local law of `RE-086`. If the true fan selects `eta_j(p)` as a boundary, the corresponding neighboring ordinary gap must still be large enough for that particular cell. What fails is only the most immediate global strategy: replacing the selected set by all possible base primes and trying to derive a contradiction from the total amount of marginal one-sided gap length.

Three selection-sensitive mechanisms remain untouched and are now more clearly isolated.

First, the rightmost-maximizer fan may be forced to select a much thinner and arithmetically structured subset of the primes in `(P,2P]`. Equation (11) says nothing about the capacity of that **selected** subset. A theorem showing that eligible boundary primes have vanishing normalized gap budget could still close the channel.

Second, a tied boundary from `RE-086` requires simultaneous anchored gaps at power-related base-prime scales. The separate marginal budgets at the two scales can both be abundant while the exact joint resonance set is sparse. No independence assumption is available, so this requires a deterministic correlation or coincidence theorem rather than multiplication of marginal densities.

Third, `RE-085` leaves singular mechanisms that do not put the higher-layer event on an adjacent boundary at all: skipped-span conditioning and discontinuous rightmost-maximizer effects. The present calculation neither constrains nor models those mechanisms.

## 5. Stress tests and exact boundary of the negative result

The little-`o` in the CA small-height law is decisive. If one knew only

\[
a(C)=O(1/\log Y_C),
\tag{33}
\]

then (10) would yield only a constant-order marginal shell capacity. The stronger `a(C)log Y_C->0` supplied by `RE-040` is exactly what turns constant-order capacity into divergence.

The conclusion is fixed-layer. If `j=j(P)` grows, `RE-086` already warns that the event asymptotic `Y~p^j/j` is not uniform in arbitrary depth. Nothing here upgrades that missing uniformity.

The argument also uses all ordinary primes in the base shell as **potential** layer-`j` boundary events. It does not prove that the adaptive fan can select them, singly or collectively. Therefore (11) is not an existence theorem for exceptional support boundaries and cannot be used in the opposite direction to claim that higher-layer singular events are common.

Finally, the calculation is a marginal first-moment statement. It says nothing about exact ties `eta_j(p)=eta_k(q)`, correlations between the two chamber-facing gaps of one cell, or compatibility with the first-layer endpoint reconstruction of `RE-083`--`RE-084`. Those are now the natural places where genuine scarcity could still enter.

## 6. Prior-art boundary and research consequence

The estimate (4) is elementary prime-number-theorem bookkeeping: consecutive gaps telescope over a dyadic shell and the normalization is `p log p`. No novelty is claimed for that prime-gap fact. The line-specific content is the splice with the global CA small-height law (5) and the anchored boundary exchange rate (1), which reverses the naive scarcity heuristic and produces the divergent threshold-capacity law (11).

A targeted current search against the closest CA literature found Mantovanelli's 2026 prime-layer workload and Zimov's work on consecutive CA transitions, but no statement combining a fixed-layer anchored base-prime gap budget with the uniform `h log log C -> 0` CA height scale to classify this aggregate-capacity route. No external theorem beyond the standard prime number theorem is load-bearing, so `SOURCES.md` needs no expansion.

The durable consequence is negative and precise: **the support-boundary route cannot be closed by marginal ordinary-gap capacity alone.** After `RE-086`, the useful target is no longer “show there is not enough neighboring prime-gap length.” There is asymptotically more than enough after the CA amplitude conversion. A viable theorem must instead show that the adaptive fan cannot repeatedly select the primes carrying that capacity, or must exploit joint/tied, skipped-span, or rightmost-maximizer structure that the marginal allocation deliberately discards.