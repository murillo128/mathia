# MC-445 — Natural fixed-rank squarefree sources collapse to the terminal gap shape

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-443` showed that at every fixed rank the **support** of selected-prime projective gap shapes is dense in the whole positive simplex, and `MC-444` showed that interior target shapes can already be realized at polynomial source-height cost. Those results left a genuinely different escape open: perhaps the **natural-source distribution** of fixed-rank prime-divisor shapes carries rich arithmetic information even though its support is dense.

For the most direct natural ensemble, the opposite happens. Fix `r>=3` and let

\[
\mathcal A_r(X)
=
\{n\le X:\mu(n)^2=1,\ \omega(n)=r\}.
\tag{1}
\]

For `n in A_r(X)`, write its ordered prime divisors as

\[
p_1(n)<\cdots<p_r(n)
\]

and define the normalized adjacent-gap shape exactly as in `MC-443`,

\[
\sigma(n)
=
\left(
\frac{p_2-p_1}{p_r-p_1},\ldots,
\frac{p_r-p_{r-1}}{p_r-p_1}
\right)
\in\Delta_{r-2}^{\circ}.
\tag{2}
\]

Let

\[
e_{r-1}=(0,\ldots,0,1)
\tag{3}
\]

be the terminal vertex of the closed gap simplex. If `n` is chosen uniformly from `A_r(X)`, then

\[
\boxed{
\mathbb P_X\!\left(
\|\sigma(n)-e_{r-1}\|_\infty>2X^{-1/2}
\right)
\ll_r \frac1{\log\log X}.
}
\tag{4}
\]

In particular,

\[
\boxed{\sigma(n)\longrightarrow e_{r-1}\quad\text{in probability}.}
\tag{5}
\]

Equivalently, for almost every fixed-rank squarefree source in this counting ensemble, the largest prime divisor asymptotically dominates all earlier prime divisors on the **linear prime-value scale**:

\[
\frac{p_{r-1}(n)}{p_r(n)}\longrightarrow0
\quad\text{in probability}.
\tag{6}
\]

Consequently, every continuous scale-invariant fixed-rank gap statistic that extends continuously to the closed simplex has a degenerate natural-source limit:

\[
\Phi(\sigma(n))\longrightarrow\Phi(e_{r-1})
\quad\text{in probability}.
\tag{7}
\]

Thus the distributional loophole left by `MC-443` is not a rich interior measure for the simplest natural fixed-rank source ensemble. There is a sharp support-versus-measure separation: prime-derived shapes are dense in the open simplex, yet natural squarefree sources of bounded rank concentrate at one boundary vertex.

This is a representation obstruction, not a Möbius bound. On the fixed stratum `omega(n)=r`, one already has `mu(n)=(-1)^r`, so no sign cancellation can occur inside that stratum.

## 1. A correct-order lower bound for the natural fixed-rank population

The proof needs only a lower bound of the classical Landau order, not the full Landau asymptotic.

Fix `r>=2` and put

\[
W=X^{1/(8(r-1))}.
\tag{8}
\]

Let `m` run over squarefree integers having exactly `r-1` prime factors, all at most `W`. Then

\[
m\le W^{r-1}=X^{1/8}.
\tag{9}
\]

For every such `m`, choose a prime `q` in

\[
\frac{X}{2m}<q\le\frac Xm.
\tag{10}
\]

The ordinary prime number theorem, uniformly for the present range `X/m >= X^(7/8)`, gives

\[
\#\left\{q:\frac{X}{2m}<q\le\frac Xm\right\}
\gg \frac{X}{m\log X}.
\tag{11}
\]

Moreover `q >> X^(7/8) >> W`, so `q` is distinct from and larger than every prime factor of `m`. Hence `n=mq` is squarefree, has exactly `r` prime factors, and lies in `(X/2,X]`. The representation is unique because `q` is its largest prime factor.

By the reciprocal-prime estimate recorded in `MC-S6`,

\[
\sum_{p\le W}\frac1p
=
\log\log W+O(1)
=
\log\log X+O_r(1).
\tag{12}
\]

For fixed `r`, the elementary symmetric sum over `r-1` distinct primes therefore satisfies

\[
\sum_{\substack{m\ \mathrm{squarefree}\\
\omega(m)=r-1\\ P^+(m)\le W}}
\frac1m
\gg_r (\log\log X)^{r-1}.
\tag{13}
\]

Indeed, expanding `(sum_(p<=W) 1/p)^(r-1)`, the terms with repeated prime indices contribute only `O_r((log log X)^(r-3))` because `sum_p 1/p^2<infinity`; the distinct-index terms give `(r-1)!` times the sum in `(13)`.

Summing `(11)` over `m` gives the lower bound

\[
\boxed{
|\mathcal A_r(X)|
\gg_r
\frac{X(\log\log X)^{r-1}}{\log X}.
}
\tag{14}
\]

This has the classical fixed-`r` Landau order. The full asymptotic is standard prior art but is not needed below.

## 2. Two large prime factors are rare at fixed rank

Fix a constant `a>0` and set

\[
z=X^a.
\tag{15}
\]

If `p_(r-1)(n)>z`, then `n` has at least two prime factors exceeding `z`. Remove two such factors and write the remaining part as `m`. It is enough to overcount pairs of primes

\[
z<p<q,
\qquad pq\le Y:=X/m.
\]

For `Y>=z^2`, let `B(Y,z)` denote the number of such pairs. Since the smaller member satisfies `p<=sqrt(Y)`, the prime number theorem upper bound gives

\[
B(Y,z)
\le
\sum_{z<p\le\sqrt Y}\pi(Y/p)
\ll
\frac{Y}{\log X}
\sum_{z<p\le\sqrt Y}\frac1p.
\tag{16}
\]

Here `Y>=z^2=X^(2a)` ensures

\[
\log(Y/p)\ge\tfrac12\log Y\ge a\log X,
\]

which accounts for the `log X` denominator in `(16)`. Because `Y<=X`, Mertens' reciprocal-prime estimate implies

\[
\sum_{z<p\le\sqrt Y}\frac1p
=O_a(1).
\tag{17}
\]

Therefore

\[
B(Y,z)\ll_a\frac{Y}{\log X}.
\tag{18}
\]

Summing over the remaining `r-2` prime factors and using

\[
\sum_{\substack{m\le X\\\omega(m)=r-2}}\frac1m
\le
\frac1{(r-2)!}
\left(\sum_{p\le X}\frac1p\right)^{r-2}
\ll_r(\log\log X)^{r-2}
\tag{19}
\]

shows

\[
\#\{n\in\mathcal A_r(X):p_{r-1}(n)>X^a\}
\ll_{r,a}
\frac{X(\log\log X)^{r-2}}{\log X}.
\tag{20}
\]

Combining `(14)` and `(20)` yields

\[
\boxed{
\mathbb P_X\big(p_{r-1}(n)>X^a\big)
\ll_{r,a}\frac1{\log\log X}.
}
\tag{21}
\]

So for every fixed positive power threshold, the second-largest prime factor falls below that threshold with probability tending to one.

## 3. The largest prime factor then absorbs the linear gap scale

Choose

\[
a=\frac1{2(r+1)}.
\tag{22}
\]

Besides the exceptional set in `(21)`, discard sources with

\[
n<X^{1-a}.
\tag{23}
\]

Their proportion is negligible even by the trivial numerator bound, because `(14)` gives

\[
\frac{X^{1-a}}{|\mathcal A_r(X)|}
\ll_r
X^{-a}\frac{\log X}{(\log\log X)^{r-1}}
=o\!\left(\frac1{\log\log X}\right).
\tag{24}
\]

On the remaining set,

\[
p_{r-1}\le X^a,
\qquad
n\ge X^{1-a}.
\tag{25}
\]

Since

\[
p_1\cdots p_{r-1}\le p_{r-1}^{r-1}\le X^{a(r-1)},
\]

we obtain

\[
p_r
=\frac{n}{p_1\cdots p_{r-1}}
\ge X^{1-ar}.
\tag{26}
\]

Hence the chosen value of `a` gives the quantitative dominance

\[
\frac{p_{r-1}}{p_r}
\le
X^{-1+a(r+1)}
=X^{-1/2}.
\tag{27}
\]

Write `S=p_r-p_1`. For every `i<=r-2`,

\[
0<\frac{p_{i+1}-p_i}{S}
\le
\frac{p_{r-1}}{p_r-p_1}
\le
\frac{X^{-1/2}}{1-X^{-1/2}},
\tag{28}
\]

while for the last coordinate

\[
1-\frac{p_r-p_{r-1}}S
=
\frac{p_{r-1}-p_1}{p_r-p_1}
\le
\frac{X^{-1/2}}{1-X^{-1/2}}.
\tag{29}
\]

For sufficiently large `X`, the right-hand side is at most `2X^(-1/2)`. Equations `(21)`, `(24)`, `(28)` and `(29)` prove `(4)` and `(5)`.

The argument also proves `(6)` directly. No zero-free region, contour shift, probabilistic independence assumption, or conjectural prime-tuple input appears.

## 4. Support density and natural-source measure point in opposite directions

There is no contradiction with `MC-443` or `MC-444`.

`MC-443` is existential: for every interior projective shape and every neighborhood, some selected rational primes realize a point in that neighborhood. `MC-444` makes those exceptional realizations quantitatively accessible with polynomial source height. The present result asks a different question: choose **uniformly among all squarefree sources of bounded height having fixed rank**. Under that natural counting measure, almost all mass moves toward the terminal boundary vertex.

Thus at fixed rank one simultaneously has

\[
\overline{\{\sigma(n):n\ \text{squarefree},\ \omega(n)=r\}}
=\Delta_{r-2}
\]

at the support level, while the empirical probability measures satisfy

\[
\frac1{|\mathcal A_r(X)|}
\sum_{n\in\mathcal A_r(X)}\delta_{\sigma(n)}
\Longrightarrow
\delta_{e_{r-1}}.
\tag{30}
\]

The source of the collapse is simple but load-bearing: fixed-`r` almost-prime counting gets its `log log X` powers from reciprocal-prime mass among the smaller factors, whereas the final prime is free to absorb essentially the entire multiplicative size of `n`. On the **linear** prime-value scale used by the gap geometry, that hierarchy forces the final adjacent gap to absorb the projective span.

For any continuous `Phi` on the closed simplex, `(30)` immediately gives `(7)`. Therefore changing from one continuous normalized fixed-rank path/gap observable to another does not produce a nondegenerate natural limiting distribution: all such observables are asymptotically evaluated at the same terminal shape.

## 5. Prior art and novelty boundary

The ingredients are classical. `MC-S6` supplies Mertens' reciprocal-prime estimate, and `MC-S15` supplies the prime-number-theorem input used in the dyadic prime interval count. Landau's classical fixed-`r` almost-prime theorem gives the sharper asymptotic

\[
|\mathcal A_r(X)|
\sim
\frac{X(\log\log X)^{r-1}}{(r-1)!\log X},
\]

but the proof above deliberately uses only the elementary lower bound `(14)`. Paul Kinlaw, *Lower Bounds for Numbers With Three Prime Factors*, Integers 19 (2019), A22, records Landau's formula and the squarefree fixed-factor notation explicitly.

The closest gap-distribution literature found in the audit studies a different scale and ensemble. Efthymios Sofos, *Gaps between prime divisors and analogues in Diophantine geometry*, Glasgow Mathematical Journal 65 (2023), S129–S147, studies gaps in `log log p_i(n)` for typical unrestricted integers and proves moment/Poisson results. Régis de la Bretèche and Gérald Tenenbaum, *On the gap distribution of prime factors*, Proceedings of the American Mathematical Society 151 (2023), 1905–1917, likewise studies multiplicative/logarithmic neighboring-prime-factor gaps for unrestricted integers. Those theorems are adjacent but do not supply the fixed-`omega`, linearly normalized projective statement `(4)`.

No novelty is claimed for fixed-`r` almost-prime counting, the reciprocal-prime estimates, or the fact that small factors dominate the harmonic combinatorics. The durable Mathia result is the consequence for the exact projective gap branch opened by `MC-443`: the simplest surviving **distribution/natural-source-frequency** escape collapses to a boundary point rather than producing a rich interior measure.

## Boundaries and falsification tests

- **Fixed rank is essential.** The constants and the threshold in `(4)` depend on `r`. When `r` grows with `X`, the smaller-prime cloud need not remain negligible on the same scale; this result does not address that live escape.
- **The source ensemble is specific.** Uniform counting on squarefree `n<=X` with `omega(n)=r` is the canonical bounded-height ensemble used here. Logarithmic weighting, constrained largest factor, balanced-factor ensembles, or other source measures can produce different limits.
- **The linear prime-value gap scale is essential.** Sofos/Tenenbaum-type `log log p` coordinates deliberately resolve the smaller factors instead of letting the largest prime absorb the full span. The present collapse is therefore not a contradiction to their nondegenerate gap laws.
- **Dense support remains true.** Rare interior shapes from `MC-443` and `MC-444` are not excluded; `(4)` says only that their total natural-source mass vanishes.
- **The rate is not claimed sharp.** The `O_r(1/log log X)` exceptional proportion and the `X^(-1/2)` geometric neighborhood are convenient consequences of the proof, not optimized distribution theory. A refined rate or rare-event law remains logically possible.
- **No rational-prime-specific discriminator has been proved.** A generalized-prime system with comparable prime counting and reciprocal-prime mass may exhibit the same one-large-factor mechanism. The result closes a representation route; it does not yet distinguish rational primes from matched Beurling controls.
- **No Möbius cancellation follows.** On `omega(n)=r`, the Möbius sign is constant. Any route to `M(x)` must couple ranks, absolute scale, or another structure that survives the full-interaction gate of `MC-437`.
- **Discontinuous/arithmetic observables remain outside the conclusion.** Equation `(7)` applies to continuous statistics extending to the closed simplex; exact congruence, integrality, or source-label information can behave differently.

## Consequence for the research line

`MC-443` left distribution, source height, growing rank, absolute scale, and discontinuous arithmetic structure as possible escapes from fixed-rank projective density. `MC-444` removed the naive fixed-rank source-height escape. The present result now sharply narrows the distributional one: under the direct natural bounded-height ensemble, fixed-rank projective gap geometry becomes **less**, not more, informative asymptotically, because almost every source collapses to the same terminal shape.

A useful continuation cannot merely ask for the limiting distribution of another continuous normalized fixed-rank gap functional. It must instead exploit at least one ingredient that this theorem does not collapse: growing rank, a deliberately non-natural/balanced source ensemble justified by the analytic target, absolute scale, rare-event rates, or a genuinely arithmetic/discontinuous statistic. Any such candidate must still pass `MC-437`'s separate full-prime-interaction survival gate before it can plausibly contribute to Möbius cancellation.