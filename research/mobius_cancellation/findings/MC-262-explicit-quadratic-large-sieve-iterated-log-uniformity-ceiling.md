# MC-262 — Explicit quadratic large-sieve uniformity reaches only fourth-iterated-log shell orders

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the quadratic shell matrix from `MC-238`, `MC-242`, `MC-252`, and `MC-253`. Let

\[
\mathcal P_y=\{p\le y:p\text{ odd prime}\},
\qquad
\mathcal R_y=\{r:y<r\le2y,\ r\text{ prime}\},
\]

write

\[
k_y=|\mathcal P_y|,
\qquad
N_y=|\mathcal R_y|,
\]

and for a `t`-element subset `T\subset\mathcal R_y` put

\[
B_y(T)
:=
\sum_{p\in\mathcal P_y}
\prod_{r\in T}\left(\frac pr\right).
\tag{1}
\]

`MC-253` proved, using Heath-Brown's quadratic large sieve, that for every **fixed** `t`, almost every `t`-fold shell parity is asymptotically balanced. It deliberately did not let `t` grow because the usual `\ll_\varepsilon(MN)^\varepsilon` formulation hides the dependence of the implied constant on `\varepsilon`.

Zihao Liu's 2026 explicit quadratic large-sieve theorem now makes that hidden dependence quantitative. Specializing Liu's estimate to `(1)` gives a genuine growing-order extension:

\[
\boxed{
 t=t(y)=o(\log^{(4)}y)
 \quad\Longrightarrow\quad
 \frac1{\binom{N_y}{t}}
 \sum_{|T|=t}
 \left|\frac{B_y(T)}{k_y}\right|^2
 =y^{-1+o(1)}.
}
\tag{2}
\]

Here

\[
\log^{(4)}y
:=
\log\log\log\log y
\]

for sufficiently large `y`. Thus the fixed-order statement of `MC-253` can be pushed unconditionally to a slowly growing parity order.

However, the same explicit dependence shows that the **black-box quadratic-large-sieve route is quantitatively incapable of reaching the support scale where a blind shell relation can still exist**. `MC-242` already proved that every nonzero quadratic blind vector has support

\[
|T|
\ge
\left(\frac1{\log 2}-o(1)\right)\log\log y.
\tag{3}
\]

Since

\[
\log^{(4)}y=o(\log\log y),
\tag{4}
\]

the growing-order range `(2)` lies entirely below the existing blind-support floor `(3)`.

More sharply, Liu's explicit form of Heath-Brown's theorem contains the factor

\[
\exp_4(C\varepsilon^{-1})(MN)^\varepsilon,
\tag{5}
\]

where `\exp_4` is the fourth iterated exponential. If `t/\log^{(4)}y\to\infty`, then for the shell-product modulus scale `M\asymp y^t` and coefficient scale `N\asymp y`, **every choice of `\varepsilon` makes `(5)` consume at least a factor of order `y`**. The ordinary all-squarefree-moduli envelope therefore no longer yields a nontrivial normalized mean-square estimate after one passes from all moduli up to `M` to the sparse family of shell products.

Consequently the suggestion left open in `MC-253` — use explicit uniformity in the quadratic large sieve to let the parity order grow until it sees blind relations — now has an exact obstruction:

\[
\boxed{
\text{published explicit quadratic-large-sieve uniformity}
\quad\text{reaches at most an iterated-log regime far below}\quad
\text{the live }\log\log y\text{ blind-support scale.}
}
\tag{6}
\]

This does **not** prove that growing-order shell balance is false beyond `\log^{(4)}y`. It proves that the current black-box all-squarefree-moduli large sieve, even with its 2026 explicit constant dependence, cannot bridge the existing support gap. A useful next theorem would have to exploit the sparse product family

\[
\left\{\prod_{r\in T}r:T\subset\mathcal R_y\right\}
\tag{7}
\]

more efficiently than embedding it in all squarefree moduli up to `y^t`, or bypass parity-rank generation and attack the surviving source-selected Möbius coset directly.

No new bound for `M(X)`, no increase of the blind-support floor `(3)`, and no proof of `H=G` is obtained.

## 1. Liu makes the hidden `\varepsilon`-dependence explicit

Heath-Brown's quadratic large sieve, in the form used in `MC-253`, gives for squarefree odd variables

\[
\sum_{m\le M}^{*}
\left|
\sum_{n\le N}^{*}
a_n\left(\frac nm\right)
\right|^2
\ll_\varepsilon
(MN)^\varepsilon(M+N)
\sum_{n\le N}^{*}|a_n|^2.
\tag{8}
\]

For fixed `t`, taking `M=(2y)^t` is harmless, because `\varepsilon` can first be fixed arbitrarily small and the implicit constant is then irrelevant asymptotically. For `t=t(y)\to\infty`, that move is invalid unless the `\varepsilon`-dependence is known.

Zihao Liu, *Explicit quadratic large sieve inequality*, Acta Arithmetica **223** (2026), no. 3, 227--252, DOI `10.4064/aa250722-27-1`, arXiv `2505.09637v2`, proves precisely such an explicit form. Theorem 1 gives, for dyadic squarefree odd sums,

\[
\mathcal B(M,N)
\le
\exp_4(C\varepsilon^{-1})
(MN)^\varepsilon(M+N),
\tag{9}
\]

with an absolute `C>0`. In §5.1 Liu performs the dyadic summation explicitly and obtains the corresponding initial-range inequality with the same fourth-iterated-exponential dependence. The paper further observes that choosing `\varepsilon` proportional to `1/\log^{(4)}X` turns the combined loss into

\[
\exp\!\left(
O\!\left(\frac{\log X}{\log^{(4)}X}\right)
\right).
\tag{10}
\]

The recent paper of Munsch--Shparlinski--Sun--Xiao, *A large sieve inequality for sums of Legendre symbols over short intervals*, arXiv `2604.23661v3` (5 August 2026), records the initial-interval consequence in the compact form

\[
M_2(Q;\boldsymbol\alpha,0,h)
\le
(hQ)^{o(1)}(Q+h)h,
\tag{11}
\]

but `(11)` by itself does not justify a varying shell-product order because its `o(1)` hides exactly the uniformity issue at stake. Liu's theorem is what permits the audit below.

No novelty is claimed for `(8)`--`(11)`.

## 2. Direct specialization gives balance for `t=o(log^(4) y)`

For `T\in\binom{\mathcal R_y}{t}`, define

\[
m_T=\prod_{r\in T}r.
\tag{12}
\]

Then `m_T` is squarefree and odd and satisfies

\[
y^t<m_T\le(2y)^t.
\tag{13}
\]

Jacobi-symbol multiplicativity gives

\[
B_y(T)
=
\sum_{p\in\mathcal P_y}
\left(\frac p{m_T}\right).
\tag{14}
\]

Apply Liu's initial-range form of `(9)` with

\[
M=(2y)^t,
\qquad
N=y,
\qquad
a_n=\mathbf 1_{\{n\in\mathcal P_y\}}.
\tag{15}
\]

Every `m_T` is one of the nonnegative outer summands, and

\[
\sum_{n\le y}^{*}|a_n|^2=k_y.
\tag{16}
\]

Writing

\[
X_y=(2y)^t y,
\tag{17}
\]

Liu's optimized explicit loss `(10)` therefore gives

\[
\sum_{|T|=t}|B_y(T)|^2
\le
\exp\!\left(
O\!\left(\frac{\log X_y}{\log^{(4)}X_y}\right)
\right)
\bigl((2y)^t+y\bigr)k_y.
\tag{18}
\]

The prime number theorem gives

\[
k_y\sim\frac y{\log y},
\qquad
N_y\sim\frac y{\log y}.
\tag{19}
\]

For `t=o(\log^{(4)}y)` we have `t=o(N_y)` and

\[
\log X_y=(t+1)\log y+O(t),
\qquad
\log^{(4)}X_y\sim\log^{(4)}y.
\tag{20}
\]

Moreover

\[
\binom{N_y}{t}
\ge
\left(\frac{N_y}{t}\right)^t.
\tag{21}
\]

Divide `(18)` by `\binom{N_y}{t}k_y^2`. Equations `(19)`--`(21)` yield

\[
\frac1{\binom{N_y}{t}}
\sum_{|T|=t}
\left|\frac{B_y(T)}{k_y}\right|^2
\le
\frac{\log y}{y}
\bigl(Ct\log y\bigr)^t
\exp\!\left(
O\!\left(\frac{t\log y}{\log^{(4)}y}\right)
\right)
\tag{22}
\]

for an absolute constant `C` and sufficiently large `y`.

Taking logarithms, the right side of `(22)` is

\[
-\log y
+O\bigl(t(\log\log y+\log t)\bigr)
+O\!\left(\frac{t\log y}{\log^{(4)}y}\right).
\tag{23}
\]

If `t=o(\log^{(4)}y)`, both error terms are `o(\log y)`, proving `(2)`. In particular, for every fixed `\delta>0`, Markov's inequality gives

\[
\frac{
\#\{T:|T|=t,\ |B_y(T)|\ge\delta k_y\}
}{\binom{N_y}{t}}
\longrightarrow0.
\tag{24}
\]

Thus `MC-253`'s fixed-order parity pseudorandomness genuinely extends to an unbounded parity order. The extension is real but extremely slow.

## 3. The explicit constant dependence exposes a fourth-iterated-log ceiling for the black-box route

The important point is not merely that the proof of `(2)` stops at `o(\log^{(4)}y)`. Liu's explicit theorem shows why the standard all-moduli application cannot be pushed anywhere near `(3)` by choosing `\varepsilon=\varepsilon(y)` more cleverly.

Before optimization, the theorem contributes the multiplier

\[
F_\varepsilon(X_y)
=
\exp_4(C\varepsilon^{-1})X_y^\varepsilon.
\tag{25}
\]

Suppose

\[
\frac{t}{\log^{(4)}y}\longrightarrow\infty.
\tag{26}
\]

For any `\varepsilon>0`, split into two cases.

If

\[
\varepsilon\ge\frac1t,
\]

then from `X_y\ge y^t` we get

\[
X_y^\varepsilon\ge y.
\tag{27}
\]

If instead

\[
\varepsilon<\frac1t,
\]

then

\[
\exp_4(C\varepsilon^{-1})
>
\exp_4(Ct).
\tag{28}
\]

Under `(26)`, eventually `Ct>\log^{(4)}y`, and monotonicity of the fourth iterated exponential gives

\[
\exp_4(Ct)>y.
\tag{29}
\]

Hence in either case

\[
\boxed{
F_\varepsilon(X_y)\ge y
}
\tag{30}
\]

for every `\varepsilon` once `y` is sufficiently large along `(26)`.

The direct all-squarefree-moduli embedding also pays the combinatorial ratio between an ambient modulus range of size about `y^t` and only

\[
\binom{N_y}{t}
\asymp
\frac1{t!}
\left(\frac y{\log y}\right)^t
\tag{31}
\]

shell products. Relative to the row count `k_y\asymp y/\log y`, even the idealized modulus-size contribution has scale

\[
\frac{y^t}{\binom{N_y}{t}k_y}
=
\frac{t!(\log y)^{t+1}}{y}\,e^{O(t)}.
\tag{32}
\]

The factor `y` already consumed in `(30)` therefore erases the only global `1/y` saving in `(32)` before this positive combinatorial penalty is paid. The bound delivered by this black-box route is consequently non-decaying, hence unable to certify growing-order balance in the regime `(26)`.

This is a limitation of the **available inequality plus the all-moduli embedding**, not an impossibility theorem for the shell family. A theorem summing directly over the sparse structured moduli `(7)` could have a fundamentally different leading cost.

## 4. Comparison with the existing blind-support floor

A quadratic blind vector supported on `T` satisfies

\[
\prod_{r\in T}\left(\frac pr\right)=1
\qquad(p\in\mathcal P_y),
\tag{33}
\]

and therefore

\[
B_y(T)=k_y.
\tag{34}
\]

So sufficiently strong high-order control of `(1)` could in principle rule out blind relations.

But `MC-242` already proves that every such nonzero relation has

\[
|T|
\ge
\left(\frac1{\log2}-o(1)\right)\log\log y.
\tag{35}
\]

The ratio of this live support scale to the range established in `(2)` diverges:

\[
\frac{\log\log y}{\log^{(4)}y}\longrightarrow\infty.
\tag{36}
\]

Thus the explicit large sieve does not merely fall slightly short of the first unresolved supports. Its useful uniformity ends **multiple iterated logarithms earlier**.

This means `(2)` adds no new blind-support exclusion beyond `MC-242`. Its value is diagnostic: it replaces the vague warning in `MC-253` about hidden fixed-parameter dependence with a quantitative barrier extracted from the strongest explicit version currently available.

## 5. Prior-art and novelty assessment

The analytic theorem is Liu's 2026 explicit refinement of Heath-Brown's 1995 quadratic large sieve. The fourth-iterated-exponential dependence in `(9)` and its optimized subpower consequence `(10)` are Liu's results, not Mathia discoveries. The compact `(hQ)^{o(1)}` initial-interval formulation in Munsch--Shparlinski--Sun--Xiao is also literature.

A targeted prior-art search through 13 September 2026 found no later theorem replacing Liu's `\exp_4(C\varepsilon^{-1})` dependence by the substantially stronger uniformity that would be needed here, and Liu explicitly remarks that reducing the iterated-exponential dependence would be desirable; in particular, an `\exp(C\varepsilon^{-1})` dependence would allow fixed powers of logarithms in place of the usual `X^\varepsilon` loss. Absence from this search is not evidence that no sharper specialized shell-product theorem exists.

No novelty is claimed for the quadratic large sieve, explicit constant tracking, Markov's inequality, or the binomial estimates. The durable Mathia delta is the specialization to the **current shell-code frontier**: explicit 2026 uniformity upgrades `MC-253` from fixed to `o(\log^{(4)}y)` parity order, while simultaneously proving that this black-box route cannot overlap the already-established `\asymp\log\log y` minimum support of a surviving blind relation.

## 6. Boundaries and decisive falsification tests

- **No statement beyond the black-box route.** Equations `(26)`--`(32)` do not prove that shell parity balance fails for larger `t`; they show only that Liu/Heath-Brown applied through the ambient all-squarefree-moduli family does not certify it there.
- **The `o(log^(4) y)` range is sufficient, not asserted optimal.** Better bookkeeping may change constants or reach a constant multiple of `\log^{(4)}y`, but cannot remove the iterated-log scale separation from `(35)` without a materially stronger large-sieve input.
- **Squarefree coefficient check.** The coefficients in `(15)` are supported on odd primes, so Liu's squarefree-inner-variable norm is exactly `k_y`; no square-product coefficient loss is hidden.
- **Modulus check.** Every `m_T` is odd and squarefree and lies below `(2y)^t`, so it is legitimately included in the outer large-sieve family.
- **Uniqueness check.** Distinct shell subsets `T` give distinct products `m_T` by unique factorization.
- **Row `p=2`.** As in `MC-253`, the single row `p=2` is omitted. Adding or deleting one row does not alter any asymptotic support or normalized-balance statement.
- **Blindness check.** The comparison with `MC-242` concerns the quadratic blind sector where `(33)` holds; no claim is made that every higher-order blind character is encoded by a binary subset.
- **No RH input.** Liu's quadratic large sieve and the derivation above are unconditional. The GRH-dependent higher-moment theorem in Munsch--Shparlinski--Sun--Xiao is not used.
- **Decisive positive falsifier.** A large-sieve or product-set theorem whose leading cost is proportional to the number of shell products rather than the ambient modulus length, uniformly through `t\asymp\log\log y`, would bypass the obstruction `(30)`--`(32)` and materially reopen the parity-rank route.

## Updated frontier

The quadratic route now has a cleaner quantitative ledger. Shell localization gives fixed-order parity pseudorandomness (`MC-253`), Liu's explicit theorem extends it to `t=o(\log^{(4)}y)`, and iterated differencing already forces every actual blind relation out to `t\gtrsim(1/\log2)\log\log y` (`MC-242`). There is no overlap.

Therefore another generic improvement of the form `(MN)^{o(1)}(M+N)` is not enough unless its dependence is strong enough **after the shell-product order is allowed to grow**. The missing analytic object is more specific: either a sparse/product-family quadratic large sieve adapted to the moduli `(7)` with uniformity at least at the `\log\log y` support scale, a shell-specific algebraic generation theorem as isolated in `MC-261`, or direct signed cancellation for the single source-selected blind pretender left by `MC-259`.