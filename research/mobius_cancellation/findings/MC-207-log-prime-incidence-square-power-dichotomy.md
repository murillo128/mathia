# MC-207 — Log-weighted prime incidence either completes to a Mertens-equivalent shifted logarithm or leaves square-power defects

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-206` leaves open replacing the shifted square-free-support field by a source-aligned relation whose nonprincipal variation is not confined to the sparse squarefree-hole set. A natural first replacement is the **prime-incidence field** of the shifted partner: instead of asking only whether `n+R` is square-free, retain which primes divide it. With logarithmic prime weights this field is indeed dense, but it has an exact dichotomy.

Fix

\[
y=c\log X,
\qquad
q=q_y=\prod_{p\le y}p,
\qquad
R=hq,
\qquad
1\le R\le X/2,
\qquad
T=X-R,
\tag{1}
\]

and put

\[
g_y(n)=\mu(n)\mathbf 1_{(n,q)=1},
\qquad
G_y(U)=\sum_{n\le U}g_y(n).
\tag{2}
\]

For `1\le U\le T`, define the distinct-prime log-incidence observable

\[
P_R(U)
:=
\sum_{n\le U}g_y(n)\log\operatorname{rad}(n+R),
\tag{3}
\]

and its prime-power completion

\[
L_R(U)
:=
\sum_{n\le U}g_y(n)\log(n+R).
\tag{4}
\]

Because `R` is a multiple of `q`, every source site with `g_y(n)\ne0` satisfies

\[
(n+R,q)=(n,q)=1.
\tag{5}
\]

Thus every prime divisor of `n+R` lies above the logarithmic sieve level `y`. The elementary identities

\[
\log\operatorname{rad}(m)=\sum_{p\mid m}\log p,
\qquad
\log m=\sum_{p^k\mid m,\ k\ge1}\log p
\tag{6}
\]

give the exact source expansions

\[
\boxed{
P_R(U)
=
\sum_{p>y}\log p
\sum_{\substack{n\le U\\n\equiv-R\pmod p}}g_y(n),
}
\tag{7}
\]

and

\[
\boxed{
L_R(U)
=
\sum_{p>y}\log p
\sum_{k\ge1}
\sum_{\substack{n\le U\\n\equiv-R\pmod {p^k}}}g_y(n).
}
\tag{8}
\]

Consequently their difference is supported **only on repeated prime powers**:

\[
\boxed{
E_R(U):=L_R(U)-P_R(U)
=
\sum_{p>y}\log p
\sum_{k\ge2}
\sum_{\substack{n\le U\\n\equiv-R\pmod {p^k}}}g_y(n).
}
\tag{9}
\]

The completed observable `(4)` is not a cheaper cancellation target. Partial summation gives the exact Volterra pair

\[
\boxed{
L_R(U)
=
G_y(U)\log(U+R)
-
\int_1^U\frac{G_y(t)}{t+R}\,dt,
}
\tag{10}
\]

and

\[
\boxed{
G_y(U)
=
\frac{L_R(U)}{\log(U+R)}
+
\int_1^U
\frac{L_R(t)}{(t+R)\log^2(t+R)}\,dt.
}
\tag{11}
\]

In particular, for every fixed `theta>0`, if

\[
\mathcal G_\theta
:=
\sup_{1\le U\le T}
\frac{|G_y(U)|}{(U+R)^\theta},
\qquad
\mathcal L_\theta
:=
\sup_{1\le U\le T}
\frac{|L_R(U)|}{(U+R)^\theta},
\tag{12}
\]

then

\[
\boxed{
\mathcal G_\theta\ll_\theta \mathcal L_\theta,
\qquad
\mathcal L_\theta
\ll_\theta
(1+\log X)\mathcal G_\theta.
}
\tag{13}
\]

Thus prime-power-completed logarithmic incidence and the rough Mertens prefix have the **same fixed-power exponent**, up to a logarithm. Any prefix-uniform `X^{theta+o(1)}` bound for one transfers to the other.

On the other hand, deleting repeated prime powers does not create a free fixed-power saving. From `(9)` and `|g_y|\le1`,

\[
|E_R(U)|
\le
\sum_{p>y}\log p
\sum_{\substack{k\ge2\\p^k\le U+R}}
\left(\frac{U}{p^k}+1\right).
\tag{14}
\]

Chebyshev's bound for `vartheta` and partial summation give

\[
\sum_{p>y}\frac{\log p}{p^2}\ll\frac1y,
\qquad
\sum_{k\ge2}\vartheta(X^{1/k})\ll \sqrt X,
\tag{15}
\]

so uniformly for `U\le T`,

\[
\boxed{
|E_R(U)|\ll \frac{U}{y}+\sqrt X.
}
\tag{16}
\]

At the active logarithmic sieve level `y=c\log X` and terminal scale `U\asymp X`, this is only

\[
|E_R(U)|\ll \frac{X}{\log X},
\tag{17}
\]

which is a logarithmic relative saving, not a fixed-power one.

Therefore the most obvious dense refinement of `MC-206` does **not** provide a third source-information channel at logarithmic weights:

- if all prime-power incidences are retained, their weighted sum is the smooth coordinate `log(n+R)`, and `(10)`--`(13)` make it Mertens-complete at fixed-power scale;
- if only distinct-prime incidences are retained, the departure from that completed coordinate is exactly the repeated-prime-power term `(9)`, supported on the same square-power locus that generated the defect obstruction in `MC-206`.

This does not rule out unweighted `omega(n+R)`, other non-logarithmic prime weights, higher mixed relations, or a genuinely new theorem controlling `(9)` with a fixed power. It rules out treating **log-weighted prime incidence itself** as a free dense escape from the square-defect frontier.

No improved estimate for `G_y`, `M`, a shifted Möbius correlation, or the zeta zero set is claimed.

## 1. Why the logarithmic incidence field has only two pieces

For every positive integer `m`, unique factorization gives

\[
\log m
=
\sum_{p^a\parallel m}a\log p
=
\sum_{p^k\mid m,\ k\ge1}\log p,
\tag{18}
\]

whereas

\[
\log\operatorname{rad}(m)
=
\sum_{p\mid m}\log p.
\tag{19}
\]

Subtracting `(19)` from `(18)` yields

\[
\log\frac{m}{\operatorname{rad}(m)}
=
\sum_{p^k\mid m,\ k\ge2}\log p.
\tag{20}
\]

Apply these identities to `m=n+R`, multiply by `g_y(n)`, and sum over `n\le U`. Equation `(5)` removes every prime `p\le y` automatically and gives `(7)`--`(9)`.

The completion `(8)` is the classical von Mangoldt divisor identity in prime-power coordinates:

\[
\log m=\sum_{d\mid m}\Lambda(d).
\tag{21}
\]

Thus the distinction between `(7)` and `(8)` is not a spectral or representation artifact. It is exactly the arithmetic distinction between retaining a prime once and retaining its full exponent. The only information added by the completion lives at square divisibility and higher.

This is the key relation to `MC-206`. There the shifted support field `mu^2(n+R)` differed from the constant field only on nonsquarefree sites. Here the distinct-prime log field looks much richer because it varies on essentially every shifted source site, but its **difference from the canonical completed logarithmic field** is still confined to repeated prime powers.

## 2. The completed field is prefix-stably invertible

Equation `(10)` is ordinary Abel summation applied to the coefficient sequence `g_y(n)` and the smooth weight `log(n+R)`.

Conversely define the cumulative weighted sum `L_R(t)` as in `(4)`. Since `R\ge1`, the weight never vanishes and

\[
g_y(n)
=
\frac{g_y(n)\log(n+R)}{\log(n+R)}.
\]

A second Abel summation with weight `1/log(t+R)` proves `(11)`.

The rate statement `(13)` is then immediate. If `|G_y(t)|\le \mathcal G_\theta(t+R)^\theta`, equation `(10)` gives

\[
|L_R(U)|
\le
\mathcal G_\theta (U+R)^\theta\log(U+R)
+
\mathcal G_\theta\int_1^U(t+R)^{\theta-1}\,dt,
\]

and hence

\[
\mathcal L_\theta
\ll_\theta(1+\log X)\mathcal G_\theta.
\tag{22}
\]

In the reverse direction, `(11)` gives

\[
|G_y(U)|
\le
\frac{\mathcal L_\theta(U+R)^\theta}{\log(U+R)}
+
\mathcal L_\theta
\int_1^U
\frac{(t+R)^{\theta-1}}{\log^2(t+R)}\,dt.
\]

Using `log(t+R)\ge log 2` and integrating the power proves

\[
\mathcal G_\theta\ll_\theta\mathcal L_\theta.
\tag{23}
\]

The **prefix-uniform** qualifier is load-bearing. A small value of `L_R(T)` at one terminal point does not control the integral in `(11)`. The obstruction is not that the transform is algebraically invertible; it is that its inverse uses the whole preceding weighted path. But once a fixed-power prefix family is the claimed currency, the transform preserves that currency up to a logarithm.

This is the same methodological distinction already forced elsewhere in the line: exact re-encoding is not progress unless the transformed quantity admits an independently stronger estimate after inversion losses are restored.

## 3. Repeated-prime omission is sparse only logarithmically

For each prime power `p^k`, the congruence class in `(9)` contains at most `U/p^k+1` integers up to `U`, irrespective of whether the residue is reduced. Therefore `(14)` follows directly.

For the density part,

\[
\sum_{k\ge2}p^{-k}
=\frac1{p(p-1)}
\ll p^{-2},
\]

and Chebyshev's estimate `vartheta(t)\ll t`, followed by partial summation, gives

\[
\sum_{p>y}\frac{\log p}{p^2}\ll\frac1y.
\tag{24}
\]

For the endpoint `+1` terms,

\[
\sum_{\substack{p^k\le X\\k\ge2}}\log p
=
\sum_{k\ge2}\vartheta(X^{1/k})
\ll \sqrt X;
\tag{25}
\]

the `k=2` term dominates, while the finitely many `k\ge3` terms are `O(X^{1/3}\log X)` and hence smaller. Equations `(24)`--`(25)` prove `(16)`.

The bound is intentionally elementary. It shows exactly what support sparsity buys before any Möbius cancellation is used: at `y=c log X`, only a `1/log X`-type relative gain. Reaching `X^{1/2+epsilon}` would require **signed cancellation inside the prime-power progression family `(9)`**, not merely the fact that repeated prime factors are uncommon.

There is one useful structural simplification compared with the square-divisor expansion in `MC-206`: `(9)` is linear over prime powers rather than an inclusion-exclusion sum over arbitrary squarefree `d`. That may make it a cleaner future analytic target. The present finding does not assert that it is easy, nor that it is equivalent to the `MC-206` defect transform term by term.

## 4. What remains genuinely open after this classification

The result is deliberately weight-specific. The logarithmic choice is special because prime-power completion collapses by `(21)` to `log(n+R)`, a deterministic smooth coordinate whose weighted Möbius prefix is explicitly invertible.

The unweighted field

\[
\omega(n+R)=\sum_{p\mid n+R}1
\]

does not have this collapse: completing prime powers gives `Omega(n+R)`, not a smooth one-dimensional coordinate with an Abel inverse of the form `(11)`. More general prime weights may likewise retain genuinely different source information. They therefore remain legitimate candidates, but they must be tested against their own completion, principal-mode contamination, and matched non-Möbius controls rather than inheriting any positive conclusion from the present calculation.

Likewise, a theorem proving a fixed-power bound for `E_R(U)` uniformly in the required shift/sieve regime would be substantive. It would make distinct-prime and completed incidence interchangeable at that power scale. It would not by itself bound `G_y`: one would still need an independent estimate for `P_R` or another relation that couples the two pieces without reintroducing the target through `(10)`.

The practical frontier is therefore narrower than the broad alternative left by `MC-206`: **do not move from squarefree support to logarithmically weighted prime incidence expecting density alone to create a new cancellation channel.** Either choose a genuinely different prime-factor statistic, or attack the signed repeated-prime-power progression term explicitly.

## 5. Prior art and novelty boundary

The number-theoretic identities used here are classical. The von Mangoldt divisor identity `(21)` is standard; see, for example, the Encyclopedia of Mathematics entry *Mangoldt function* (which records `sum_{d|n} Lambda(d)=log n`) and the standard treatments in Hardy--Wright or Apostol. The relation `log rad(m)=sum_{p|m}log p` is immediate from unique factorization. Abel summation and Chebyshev's bound are also classical.

A modern adjacent language is Dimitris Koukoulopoulos, *A logarithmic structure theorem for multiplicative functions with small partial sums*, arXiv:2605.01412 (2026), which explicitly organizes logarithmically weighted multiplicative structure through a generalized von Mangoldt function defined by `f log = Lambda_f * f`. That work is not used as a theorem about the shifted observable `(3)`--`(4)` and does not establish the present frontier conclusion; it confirms that logarithmic prime-power completion is established analytic-number-theory structure rather than a new Mathia mechanism.

A targeted search for shifted Möbius correlations with `log rad(n+h)`, prime-incidence weights, and additive prime-factor functions found surrounding Möbius-orthogonality and additive-function literature, but no literature-absence statement is needed here. The durable contribution is the **line-specific exact classification** `(7)`--`(17)`: the most immediate dense log-weighted replacement for the `MC-206` support field either completes to a prefix-stably Mertens-equivalent transform or differs from it only on repeated prime powers.

No standalone novelty is claimed for `(6)`, `(10)`, `(11)`, or the support estimate `(16)`.

## 6. Boundaries and falsification tests

- The fixed-power equivalence `(13)` is a statement about **prefix-uniform** control. It does not infer `G_y(T)` from one isolated terminal value `L_R(T)`.
- The terminal interpretation uses `R\le X/2`, so `T=X-R\asymp X`. If the shift approaches `X` so closely that the source interval becomes much shorter, the relevant scale must be restated in terms of `T` rather than imported from this regime.
- The error bound `(16)` is absolute and deliberately crude. Strong cancellation in `(9)` is not ruled out; indeed that is one of the surviving routes.
- Distinct-prime incidence is not claimed to be information-poor in general. The obstruction is specific to the logarithmic weight, whose prime-power completion is exactly `log(n+R)`.
- The repeated-prime-power term `(9)` shares its support locus with the squarefree defect of `MC-206`, but it is a different weighted observable. No termwise equivalence between the two is claimed.
- Primes dividing the shift parameter `h` can make some residues in `(9)` non-coprime. Bound `(16)` does not assume reduced residues and remains valid; any future use of arithmetic-progression theorems must treat that issue explicitly.
- No analytic continuation of `1/zeta`, zero-free region, RH-equivalent bound, probabilistic independence, or random-walk heuristic enters the derivation.

The result would be falsified by an error in the divisor expansions `(6)`--`(9)`, failure of the Abel inverse `(11)`, or a power loss hidden in `(13)` beyond logarithmic/subpower size. All three parts are exact and independently checkable.