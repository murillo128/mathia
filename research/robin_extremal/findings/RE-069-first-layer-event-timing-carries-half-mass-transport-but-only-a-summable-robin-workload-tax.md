# RE-069 — first-layer event timing carries half-mass transport but only a summable Robin-workload tax

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FIRST-LAYER-TIMING + TRANSPORT-AREA + ABSOLUTELY-SUMMABLE-ROBIN-TAX + UNBOUNDED-PACKET + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-068` shows that a complete matched `0 -> 0` first-layer fan packet cannot be detected by changing the additive prime weight at the two endpoints: the ordinary primes crossed by the adaptive selectors are exactly the physical first-layer event labels. One source-specific datum survives that set identity: the physical event attached to `p` does not occur at `p`, but at the delayed CA coordinate `eta_p=eta_{p,1}>p`. The natural next question is whether this **prime/event timing transport** can accumulate across a large first-layer takeover and become visible to the exact Robin workload of `RE-001`.

It can accumulate macroscopically in ordinary Euclidean area, but the answer for the Robin kernel is negative in a much stronger sense. Let

\[
\Phi_1(x):=\sum_{\eta_p\le x}\log p,
\qquad
B_1(x):=\vartheta(x)-\Phi_1(x),
\qquad
 g(x):=\frac1{x\log x}.
\tag{1}
\]

Then the first-layer timing discrepancy is exactly a superposition of positive delay pulses,

\[
\boxed{
B_1(x)
=\sum_p (\log p)\,\mathbf 1_{[p,\eta_p)}(x).
}
\tag{2}
\]

For each prime, the complete pulse has Robin-kernel mass

\[
\boxed{
-\int_p^{\eta_p}(\log p)g'(x)\,dx
=\frac1p-\log\!\left(1+\frac1p\right)
=:\kappa_p>0.
}
\tag{3}
\]

In particular,

\[
0<\kappa_p<\frac1{2p^2},
\tag{4}
\]

so the total first-layer timing tax is absolutely summable and its late tail satisfies the elementary bound

\[
\boxed{
0\le
-\int_X^\infty B_1(x)g'(x)\,dx
\ll \frac1X.
}
\tag{5}
\]

No packet-cardinality hypothesis enters (5). Collapsing **all future first-layer CA events** from their delayed coordinates `eta_p` back to their ordinary-prime locations `p` changes the entire remaining exact Robin workload by only `O(1/X)`.

The contrast with unweighted timing is sharp. For a late complete `0 -> 0` first-layer-only fan packet from selected state `C_-` to `C_+`, let

\[
Y_\pm:=\log C_\pm,
\qquad
\mathcal E:=\{p:(p,1)\text{ occurs in the packet}\}.
\tag{6}
\]

By `RE-068`, the packet labels are exactly the ordinary primes between the two adaptive selectors, and both endpoint fringe corrections vanish. Every corresponding delay pulse is therefore complete inside the selector interval. Hence

\[
\boxed{
\int_{Z_-}^{Z_+}B_1(x)\,dx
=\sum_{p\in\mathcal E}(\log p)(\eta_p-p)
=\left(\frac12+o(1)\right)(Y_+-Y_-),
}
\tag{7}
\]

uniformly as the packet moves to infinity, even when `#E` is unbounded. The same packet nevertheless contributes only

\[
\boxed{
\int_{Z_-}^{Z_+}B_1(x)g'(x)\,dx
=-\sum_{p\in\mathcal E}\kappa_p,
\qquad
\left|\int_{Z_-}^{Z_+}B_1g'\right|
\ll \frac1{Z_-}.
}
\tag{8}
\]

Thus first-layer timing is not absent: in raw transport coordinates it carries asymptotically **half of the packet's logarithmic mass**. What kills it in the Robin comparison is the specific derivative kernel `g'`. The exact CA event equation converts each half-unit displacement into the quadratic reciprocal tax (3), and those taxes have a convergent prime tail.

This closes one of the explicit escape directions left by `RE-068`. A polynomial or even arbitrarily large pure first-layer takeover cannot become visible merely by aggregating the delayed locations `eta_p-p` through the **linear exact Robin workload**. Any successful use of first-layer timing must be nonlinear, must interact with selector placement/support geometry before the `g'` integration, or must couple to higher layers or packet history. The direct timing contribution itself is asymptotically too small.

## 1. The ordinary-prime and first-layer event staircases differ by delay pulses

For the first layer, the CA threshold is

\[
g(\eta_p)
=\frac{\log(1+p^{-1})}{\log p}.
\tag{9}
\]

Since

\[
\log(1+p^{-1})<p^{-1},
\tag{10}
\]

we have `g(eta_p)<g(p)`. The function `g` is strictly decreasing, so

\[
\boxed{\eta_p>p}
\tag{11}
\]

for every prime. Therefore

\[
\begin{aligned}
B_1(x)
&=\sum_p(\log p)
\left(\mathbf1_{\{p\le x\}}-\mathbf1_{\{\eta_p\le x\}}\right)\\
&=\sum_p(\log p)\mathbf1_{[p,\eta_p)}(x),
\end{aligned}
\tag{12}
\]

which proves (2). In particular `B_1(x)>=0` identically.

`RE-042` gives the sharper location law

\[
\eta_p-p
=\frac12-\frac1{2(\log p+1)}+O(p^{-1}),
\tag{13}
\]

so, for all sufficiently large primes,

\[
p<\eta_p<p+\frac12.
\tag{14}
\]

The pulses are therefore short and, in the late regime, pairwise disjoint. Disjointness is useful for the geometric interpretation but is not needed for the integral identities below; linearity of the staircase difference is enough.

The identity (12) is the precise form of the timing information that survives `RE-068`. Endpoint prime-set conservation says that a matched pure first-layer packet sees the same primes on the ordinary and physical sides. Equation (12) records the remaining difference: the two staircases place the same `log p` atom at coordinates separated by `eta_p-p`.

## 2. The Robin kernel converts one delay pulse into a quadratic reciprocal tax

Integrating one pulse against the positive measure `-g'(x)dx` gives

\[
\begin{aligned}
-\int_p^{\eta_p}(\log p)g'(x)\,dx
&=(\log p)\bigl(g(p)-g(\eta_p)\bigr)\\
&=\frac1p-\log\!\left(1+\frac1p\right),
\end{aligned}
\tag{15}
\]

where the last equality uses (9) and

\[
(\log p)g(p)=\frac1p.
\tag{16}
\]

This proves the exact formula (3). It is not an asymptotic expansion: the CA threshold equation makes the kernel integral collapse to an elementary prime term.

For `u>0`,

\[
0<u-\log(1+u)<\frac{u^2}{2}.
\tag{17}
\]

Putting `u=1/p` proves (4). Consequently

\[
\sum_p\kappa_p
\tag{18}
\]

converges absolutely. More quantitatively, for `X>=2`,

\[
\sum_{p\ge X}\kappa_p
\le\frac12\sum_{n\ge\lceil X\rceil}\frac1{n^2}
\ll\frac1X.
\tag{19}
\]

If `X` happens to lie inside one delay pulse, the initial partial pulse contributes at most the full `kappa_p` of a prime `p=X+O(1)`, hence `O(X^{-2})`. Adding (19) proves the arbitrary-cut tail estimate (5).

This bound deliberately uses no prime number theorem. PNT would sharpen the complete-prime tail to order `1/(X log X)`, but that refinement is irrelevant to the obstruction: `O(X^{-1})` is already far below the `X^{-b}` scales with `b<1/2` that drive the false-RH fan.

## 3. The full CA workload admits an exact instantaneous-first-layer decomposition

Write the complete CA event staircase as

\[
\Phi(x)=\Phi_1(x)+\Phi_{\ge2}(x)
\tag{20}
\]

and the exact workload of `RE-001` as

\[
D(x)=x-\Phi(x).
\tag{21}
\]

Introduce only as a comparison object

\[
D_{\rm inst}(x)
:=x-\vartheta(x)-\Phi_{\ge2}(x),
\tag{22}
\]

which moves the first-layer atoms from `eta_p` back to `p` while leaving every higher layer untouched. This is **not** asserted to be the workload of another CA system. It is simply an exact algebraic decomposition. By (1),

\[
\boxed{
D(x)=D_{\rm inst}(x)+B_1(x).
}
\tag{23}
\]

Hence on any interval `[a,b]`,

\[
\boxed{
\int_a^bD(x)g'(x)\,dx
=
\int_a^bD_{\rm inst}(x)g'(x)\,dx
+
\int_a^bB_1(x)g'(x)\,dx.
}
\tag{24}
\]

Equation (5) now has a direct workload interpretation. Once the event axis has reached scale `X`, the total difference between the genuine future Robin workload and the comparison in which **every remaining first-layer event is instantaneous at its prime** is `O(1/X)`, even if infinitely many first-layer events are included. Higher-layer events are not approximated and no cancellation among different primes is being assumed.

The sign is also rigid. Since `B_1>=0` and `g'<0`,

\[
\int B_1g'\le0.
\tag{25}
\]

Delaying a first-layer atom from `p` to `eta_p` therefore contributes a small negative tax to the exact Robin workload relative to the instantaneous-first-layer comparison.

This sign should not be overinterpreted. `D_inst` is not a valid replacement CA process, and (25) does not prove monotonicity of `G`. It isolates only the contribution caused by the first-layer spatial staggering itself.

## 4. Matched first-layer packets have large raw transport and tiny workload transport

Consider the complete first-layer-only packet of (6) and assume the matched branch

\[
\chi_-=\chi_+=0.
\tag{26}
\]

`RE-068` proves the exact prime-set identity

\[
\mathcal E
=\{p\text{ prime}:Z_-<p\le Z_+\}.
\tag{27}
\]

Because the selected endpoints are regular support points, every physical first-layer event crossed by the packet lies between them. The fringe-free endpoint condition excludes partial first-layer pulses at `Z_-` and `Z_+`. Therefore all and only the pulses indexed by `p in E` are complete inside `[Z_-,Z_+]`. Equations (12) and (15) immediately give

\[
\int_{Z_-}^{Z_+}B_1(x)\,dx
=\sum_{p\in\mathcal E}(\log p)(\eta_p-p)
\tag{28}
\]

and

\[
\int_{Z_-}^{Z_+}B_1(x)g'(x)\,dx
=-\sum_{p\in\mathcal E}\kappa_p.
\tag{29}
\]

The exact state ratio in a first-layer-only packet is

\[
\frac{C_+}{C_-}=\prod_{p\in\mathcal E}p,
\qquad
Y_+-Y_-=\sum_{p\in\mathcal E}\log p.
\tag{30}
\]

Let `P:=min E` when the packet is nonempty. Substituting (13) into (28),

\[
\begin{aligned}
\int_{Z_-}^{Z_+}B_1(x)\,dx
&=\frac12(Y_+-Y_-)
-\frac12\sum_{p\in\mathcal E}\frac{\log p}{\log p+1}\\
&\qquad+O\!\left(\sum_{p\in\mathcal E}\frac{\log p}{p}\right).
\end{aligned}
\tag{31}
\]

Since

\[
\#\mathcal E
\le\frac{Y_+-Y_-}{\log P},
\qquad
\sum_{p\in\mathcal E}\frac{\log p}{p}
\le\frac{Y_+-Y_-}{P},
\tag{32}
\]

we obtain

\[
\boxed{
\int_{Z_-}^{Z_+}B_1(x)\,dx
=\left(\frac12+O\!\left(\frac1{\log P}\right)\right)(Y_+-Y_-).
}
\tag{33}
\]

No upper bound on `#E` was used. The raw source transport remains half-mass even for an unbounded packet.

By contrast, every `p in E` satisfies `p>Z_-`, so (4) gives

\[
0<\sum_{p\in\mathcal E}\kappa_p
\le\frac12\sum_{n>Z_-}\frac1{n^2}
\ll\frac1{Z_-},
\tag{34}
\]

which is (8). Equations (33)--(34) are the key comparison: the same collection of delayed atoms has order-`Y_+-Y_-` transport in the flat metric and only order-`Z_-^{-1}` transport in the exact Robin metric.

## 5. Boundary tests and falsification

The result does **not** say that first-layer event locations are irrelevant to the adaptive fan. Support chambers, cell widths, fringe formation, and selector placement depend on where the event coordinates occur; `RE-043`--`RE-050` and `RE-063` exploit precisely such geometry. Equations (3)--(5) rule out only the direct strategy of feeding the first-layer delay discrepancy linearly into the exact Robin workload and hoping that many small delays accumulate to a macroscopic late effect.

The matched-packet half-mass statement (7) requires complete first-layer pulses. For `0 -> 1` or `1 -> 0` packets, one boundary pulse is only partially represented and must be kept explicitly. The global tail estimate (5), however, is unaffected: any such partial pulse is bounded by its full `kappa_p` and remains within the same `O(1/X)` tail.

Higher layers are deliberately untouched. Their event locations need not be within a bounded distance of an ordinary prime, and their workload charges are exactly the effects isolated by `RE-060`--`RE-066`. Nothing here bounds the higher-layer component `Phi_{>=2}` or a nonlinear interaction between higher layers and first-layer timing.

The comparison workload `D_inst` is not claimed to come from an admissible CA exponent vector. It is a bookkeeping device for isolating one information channel inside the genuine exact workload. Therefore one cannot infer a new extremal sequence or a new Robin criterion from (22)--(24).

Finally, the `O(1/X)` estimate is an upper bound on the **entire future first-layer timing tax**, not on the full workload error. Standard prime-distribution fluctuations and higher-layer structure can be much larger. The result narrows the source of a possible obstruction; it does not supply the missing global sign theorem.

## 6. Prior-art boundary and research consequence

The critical first-layer threshold `g(eta_p)=log(1+1/p)/log p` is classical Alaoglu--Erdos structure, and the exact workload `integral D g'` is already part of Mantovanelli's 2026 prime-layer framework and `RE-001`; no novelty is claimed for either ingredient. The convergence mechanism in (4) is also elementary Euler-product/Mertens territory: after the linear `1/p` term is removed, the remainder is quadratic and summable.

A targeted current literature search checked the recent exact prime-layer workload material and searches for the specific combination of the first-layer delay staircase with the ordinary Chebyshev staircase. I found no external statement isolating the pulse identity (2), the exact per-prime Robin timing tax

\[
\frac1p-\log(1+1/p),
\tag{35}
\]

and its consequence that an arbitrarily large matched first-layer takeover has only `O(1/X)` total direct timing contribution to the late Robin workload. No priority claim is made. The external ingredients needed for the derivation are already anchored in `SOURCES.md`, so no source-file change is required.

The durable consequence is a sharper post-`RE-068` frontier. Pure first-layer packets have now exhausted two natural source-local attacks: endpoint additive prime statistics are exactly conserved, and direct prime/event timing transport is annihilated to an absolutely summable tail by the Robin kernel. A successful continuation must spend information **before** this compression — for example selector placement relative to event/prime gaps, nonlinear relations among successive packets, interaction with the higher-layer history, or a statistic whose kernel does not reduce each delayed first-layer atom to the quadratic reciprocal remainder (35).