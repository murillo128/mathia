# FD-206 — Root-aligned lowbit anchors already contain the RH-equivalent dyadic Mertens increment

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** root-aligned prime-shell anchor / dyadic Mertens criterion / lowbit-route obstruction
- **Depends on:** FD-201, FD-204, FD-205
- **Classification:** `EXACT-DERIVED + DYADIC-MERTENS-EQUIVALENCE + ROOT-ALIGNED-SHELL-ANCHOR + DECISIVE-ROUTE-RESTRICTION`

## Claim

The critical-power lowbit-energy criterion of `FD-205` is stronger than needed for a more elementary reason than the binary quotient ladder used there. The positive endpoint anchor already contains an RH-equivalent scalar Mertens increment on a source-independent cofinal family of root-aligned Farey horizons.

For every sufficiently large integer `n`, let `p_n` be the largest prime not exceeding `n`, and define

\[
H_n:=n p_n,
\qquad
K_n:=\lfloor\sqrt{H_n}\rfloor.
\tag{1}
\]

Let `p_1<\cdots<p_m` be the primes in the critical shell

\[
K_n/2<p\le K_n
\]

used by `FD-204`, and retain the `r=2` sensor

\[
S_{2,H}(p)
=
M\!\left(\left\lfloor\frac{2H}{p}\right\rfloor\right)
-
M\!\left(\left\lfloor\frac H p\right\rfloor\right).
\tag{2}
\]

Then `p_n` is exactly the largest shell prime `p_m`, hence the root of the lowbit tree, and

\[
\boxed{
S_{2,H_n}(p_m)=M(2n)-M(n).
}
\tag{3}
\]

Consequently the anchored lowbit energy satisfies the exact positive lower bound

\[
\boxed{
\mathcal G_{2,H_n}^{\mathrm{lb}}
\ge
K_n\,|M(2n)-M(n)|^2.
}
\tag{4}
\]

Moreover,

\[
\boxed{
\mathrm{RH}
\iff
M(2n)-M(n)=O_\varepsilon(n^{1/2+\varepsilon})
\text{ for every }\varepsilon>0.
}
\tag{5}
\]

Therefore it is already enough to assume

\[
\boxed{
\mathcal G_{2,H_n}^{\mathrm{lb}}
=O_\varepsilon(H_n^{1+\varepsilon})
\quad\text{for the single horizon family }H_n=n p_n
}
\tag{6}
\]

in order to imply RH. No lowbit point-evaluation resistance estimate and no realization of the separate transition `n -> 2n+1` are needed for that implication.

More quantitatively, if

\[
\mathcal G_{2,H_n}^{\mathrm{lb}}
=O\!\left(H_n\log^A H_n\right),
\tag{7}
\]

then

\[
\boxed{
M(N)=O\!\left(N^{1/2}\log^{A/2}N\right)
}
\tag{8}
\]

(up to an absorbed `O(log N)` term). This improves the logarithmic exponent `(A+1)/2` obtained by passing through the worst-case lowbit resistance in `FD-205`.

The main implication of `FD-205` remains correct, but one boundary statement there is not: control only of the doubling increment does **not** merely reach powers of two and their fixed multiples. Odd binary transitions differ from the corresponding doubling transition by the single bounded coefficient `mu(2n+1)`, so doubling control alone telescopes to arbitrary integers.

The research consequence is restrictive. A proof of the full positive lowbit bound (6) must already prove an RH-equivalent square-root estimate for its scalar root anchor. The nonnegative tree-edge terms cannot make that upper bound easier by cancellation. Thus the post-`FD-204` problem is not merely to control a favorable multiscale graph energy: as currently anchored, that energy contains the classical Mertens difficulty as a positive one-row subproblem.

## 1. The largest prime below `n` is the lowbit root at `H_n=n p_n`

By the prime number theorem (and much less would suffice), for every sufficiently large `n`,

\[
\frac n2<p_n\le n.
\tag{9}
\]

Since `p_n<=n`,

\[
p_n^2\le n p_n=H_n,
\]

so `p_n<=K_n`. On the other hand `H_n<=n^2`, hence `K_n<=n`. Because `p_n` is by definition the largest prime at most `n`, and `K_n<=n`, there is no prime in `(p_n,K_n]`. Therefore `p_n` is the largest prime at most `K_n`.

Also `K_n<=n<2p_n`, so

\[
K_n/2<p_n\le K_n.
\tag{10}
\]

Thus `p_n` belongs to the critical shell and is exactly its terminal prime `p_m`, which `FD-204` uses as the tree root and scalar anchor.

At this horizon there are no floor errors:

\[
\left\lfloor\frac{H_n}{p_n}\right\rfloor=n,
\qquad
\left\lfloor\frac{2H_n}{p_n}\right\rfloor=2n.
\tag{11}
\]

Substitution into (2) proves (3).

The scales are uniformly comparable. From (9),

\[
\frac{n^2}{2}<H_n\le n^2,
\qquad
\frac n2<K_n\le n.
\tag{12}
\]

Hence the root anchor is not hidden at an anomalous scale: it is a genuine square-root-shell coordinate with source length `Theta(n)`.

## 2. The positive lowbit norm contains the dyadic increment without conditioning loss

Recall from `FD-204`

\[
\mathcal G_{2,H}^{\mathrm{lb}}
=
K\left(
Q_{\mathrm{lb}}(S)+|S_m|^2
\right),
\tag{13}
\]

where every term in `Q_lb` is nonnegative. At the root-aligned horizon (1), equations (3) and (13) give (4) immediately.

Suppose first that (7) holds. Using (12),

\[
\begin{aligned}
|M(2n)-M(n)|^2
&\le
\frac{\mathcal G_{2,H_n}^{\mathrm{lb}}}{K_n}\\
&\ll
\frac{H_n\log^A H_n}{K_n}\\
&\ll
n\log^A n.
\end{aligned}
\tag{14}
\]

Therefore

\[
\boxed{
|M(2n)-M(n)|
\ll
n^{1/2}\log^{A/2}n.
}
\tag{15}
\]

No `1+floor(log_2 m)` point-evaluation factor appears, because the target coordinate is itself the root anchor rather than a vertex recovered through the tree.

Likewise, if (6) holds for every positive energy exponent, then after renaming exponents,

\[
M(2n)-M(n)=O_\varepsilon(n^{1/2+\varepsilon}).
\tag{16}
\]

This already has the RH power scale.

## 3. Doubling increments alone recover every Mertens value

Put

\[
\Delta(n):=M(2n)-M(n).
\tag{17}
\]

For an arbitrary integer `N`, define the descending binary prefixes

\[
n_0:=N,
\qquad
n_{j+1}:=\left\lfloor\frac{n_j}{2}\right\rfloor
\]

until a fixed bounded terminal value is reached. Write

\[
n_j=2n_{j+1}+b_j,
\qquad b_j\in\{0,1\}.
\tag{18}
\]

Then the exact one-step identity is

\[
\boxed{
M(n_j)-M(n_{j+1})
=
\Delta(n_{j+1})
+b_j\,\mu(2n_{j+1}+1).
}
\tag{19}
\]

For `b_j=0` this is the doubling increment itself. For `b_j=1`, the odd transition differs from the even one by exactly one Mobius coefficient, whose modulus is at most one. This is the missing elementary observation in the corresponding discussion of `FD-205`.

Telescoping (19) gives

\[
M(N)
=
O(1)
+
\sum_j \Delta(n_{j+1})
+
O(\log N).
\tag{20}
\]

Since `n_{j+1}<=N/2^{j+1}`, a bound

\[
|\Delta(n)|\ll n^{1/2}L(n)
\]

with nondecreasing `L` gives

\[
\sum_j |\Delta(n_{j+1})|
\ll
N^{1/2}L(N)
\sum_{j\ge0}2^{-(j+1)/2}
\ll
N^{1/2}L(N).
\tag{21}
\]

Applying (15) proves (8). Applying (16) gives

\[
M(N)=O_\varepsilon(N^{1/2+\varepsilon}),
\tag{22}
\]

and the classical Littlewood--Mertens criterion then gives RH.

Conversely, RH implies `M(x)=O_epsilon(x^(1/2+epsilon))`, so subtraction immediately gives the same bound for `Delta(n)`. This proves the equivalence (5).

Thus the scalar family in (3), not the full lowbit geometry, already carries an RH-equivalent critical estimate.

## 4. What this changes in the lowbit route

`FD-202--FD-204` solved a genuine finite-dimensional problem. Differencing neighboring or lowbit-related prime modes removes repeated long-interval bulk before squaring, and the lowbit tree reduces anchored point-evaluation resistance from `Theta(m)` to `Theta(log m)` while retaining critical **random** power cost. Those statements remain intact.

What changes is the interpretation of the proposed deterministic analytic target. Because the norm in `FD-204` is anchored by the positive summand `|S_m|^2`, a uniform critical upper bound for the whole norm cannot exploit the tree to avoid proving square-root cancellation in that anchor. The root-aligned family (1) makes that anchor exactly the RH-equivalent dyadic Mertens increment.

So the implication

\[
\mathcal G_{2,H}^{\mathrm{lb}}=H^{1+o(1)}
\Longrightarrow \mathrm{RH}
\]

is not evidence by itself that the multiscale graph has created an easier analytic route. On the specific horizons `H_n`, the claimed upper bound already contains

\[
K_n|M(2n)-M(n)|^2
\]

as a nonnegative subterm. Proving the full energy estimate is therefore at least as hard as proving an RH-equivalent scalar estimate on those horizons.

A genuinely new Farey route would need to explain why that scalar estimate follows from additional geometry **without simply assuming it as a positive coordinate of the controlled quantity**, or replace the scalar anchor by a signed/cross-scale mechanism where cancellation can occur before the RH-sized coordinate is bounded. The lowbit edge geometry may still be useful in such a construction, but the present positively anchored energy does not by itself lower the classical analytic barrier.

## 5. Prior art, representation and correction audit

The external theorem boundary is classical. Titchmarsh's Littlewood--Mertens criterion, already anchored in `SOURCES.md`, gives the equivalence between RH and `M(x)=O_epsilon(x^(1/2+epsilon))`; the dyadic-increment formulation (5) follows from that criterion and the elementary telescope (19)--(21). The prime-number theorem already present in `SOURCES.md` is more than sufficient for (9). No new literature dependency is required.

A targeted search for `M(2x)-M(x)` and dyadic Mertens RH criteria found the standard Mertens-growth criterion and computational Mertens identities, but no separate theorem needed here. No novelty is claimed for the elementary fact that dyadic increments recover a summatory function. The Mathia-specific content is the exact root alignment (1)--(4), which shows that the endpoint anchor of the persisted lowbit Farey observable is precisely such a dyadic increment on a source-independent critical-shell family.

The representation audit is exact. `p_n` and `H_n` depend only on `n` and prime locations, never on observed Mobius values. The coordinate in (3) is the native fixed-mode sensor of `FD-201` and the exact endpoint anchor of `FD-204`; no inverse transform, random model, interpolation or asymptotic replacement is used.

This finding also corrects, rather than refutes, `FD-205`. Its principal theorem remains valid: a critical uniform lowbit-energy bound implies RH. However, its assertion that both binary digit transitions are necessary for arbitrary targets is false by (19), and its `(A+1)/2` logarithmic consequence is not sharp on the root-aligned horizon family. The stronger route here needs only the doubling transition and avoids the lowbit resistance factor entirely.

No clue status changes. The accepted local clues concern distinct ordering/Jordan mechanisms. No formalization issue is opened: the finite root-alignment and binary-telescope lemmas are elementary, while the substantive value is the research-route correction that they force.

## Conclusion

The lowbit graph remains a valid way to organize correlated prime-shell increments, but its current positive anchor changes the meaning of the proposed critical-energy theorem. At the source-independent horizons `H_n=n p_n`, the root is exactly the largest prime below `n`, and the anchor is exactly `M(2n)-M(n)`. Square-root control of these doubling increments is already equivalent to RH, because odd binary steps differ by only one bounded Mobius coefficient.

Hence the full `H^(1+o(1))` lowbit-energy target contains an RH-equivalent scalar subproblem before any multiscale resistance argument is used. The next viable Farey mechanism should therefore avoid treating that scalar anchor as a positive standalone cost, or prove its critical bound from genuinely additional signed/cross-scale structure rather than from the lowbit norm alone.