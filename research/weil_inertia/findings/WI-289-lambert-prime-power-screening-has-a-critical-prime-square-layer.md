# WI-289 — Lambert prime-power screening has a critical prime-square layer

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the arithmetic endpoint isolated by `WI-288` for the **one-signed, completely screened, symmetric two-island** branch. The question is whether higher prime powers make the nearest-prime-power Lambert obstruction substantially stronger than an ordinary prime-gap obstruction.
- **Result:** the nearest-prime-power condition has an exact root-scale decomposition. At the `WI-288` Lambert threshold, prime squares are the unique higher-power layer with a macroscopic root-scale constraint: they demand a prime-free interval of approximately one mean prime gap around `sqrt(x)`. Every exponent `k>=3` produces only a subunit root-scale window. On a dyadic `x`-shell, all `k>=3` Lambert neighborhoods together have measure `O(X^(5/6) log X)`, while the square layer has total interval budget

  \[
  X-\left(2+o(1)\right)\frac{X\log\log X}{\log X}.
  \]

  Therefore all **composite** prime-power Lambert neighborhoods together leave at least

  \[
  \boxed{\left(2+o(1)\right)\frac{X\log\log X}{\log X}}
  \]

  of `[X,2X]` uncovered. Higher powers cannot uniformly fill the arithmetic gap left by current prime-in-short-interval information. At this scale the unresolved two-island obstruction is a coupled two-scale problem: a very large prime desert near `x` plus an approximately mean-gap prime desert near `sqrt(x)`, with `k>=3` contributing only sparse resonance exclusions.
- **What it does not claim:** this does not construct a center satisfying the full `WI-288` condition, prove that a sufficiently large prime gap near `x` intersects the composite-power-free residual set, rule out the two-island branch, or assert independence of prime-gap events at `x` and `sqrt(x)`.
- **Novelty boundary:** prime-power parametrization, the prime number theorem, average prime-gap scale, and the Lambert-`W` expansion are classical. Ford--Heath-Brown--Konyagin and Maier--Rassias show that long prime gaps can contain fixed perfect powers, including powers of primes. The line-local deductions here are the exact root decomposition at the `WI-288` threshold, the identification of `k=2` as the unique critical higher-power layer, and the dyadic coverage barrier. Targeted searches found the classical large-gap/power-placement literature but not this particular Lambert-scale reduction or coverage estimate; search absence is audit context only.

## Claim

For `y>1`, let

\[
\delta_{\mathrm p}(y)
:=\min_{p\,\text{prime}}|\log p-\log y|,
\tag{1}
\]

and recall

\[
\delta_{\mathrm{pp}}(x)
:=\min_{p\,\text{prime},\,k\ge1}|k\log p-\log x|.
\tag{2}
\]

Then exactly

\[
\boxed{
\delta_{\mathrm{pp}}(x)
=\min_{k\ge1}k\,\delta_{\mathrm p}(x^{1/k}).
}
\tag{3}
\]

Fix `c>0` and define the Lambert radius

\[
D_c(x):=\frac{W(c\sqrt{x})}{\sqrt{x}}.
\tag{4}
\]

The `WI-288` necessary condition is of the form

\[
\delta_{\mathrm{pp}}(x)\ge D_c(x)
\tag{5}
\]

for one fixed absolute `c>0`. By (3), this is equivalent to

\[
\boxed{
\delta_{\mathrm p}(x^{1/k})\ge\frac{D_c(x)}k
\qquad(k\ge1).
}
\tag{6}
\]

The corresponding prime-free interval around `x^(1/k)` has exact additive length

\[
2x^{1/k}\sinh\!\left(\frac{D_c(x)}k\right)
=\frac2k x^{1/k-1/2}W(c\sqrt{x})(1+o(1)).
\tag{7}
\]

Thus

\[
\begin{aligned}
k=1:&\quad 2\sqrt{x}\,W(c\sqrt{x})(1+o(1)),\\
k=2:&\quad W(c\sqrt{x})(1+o(1)),\\
k\ge3:&\quad O(x^{-1/6}\log x)=o(1).
\end{aligned}
\tag{8}
\]

Since

\[
W(c\sqrt{x})
=\log\sqrt{x}-\log\log\sqrt{x}+O(1),
\tag{9}
\]

the square condition is a prime-free interval around `sqrt(x)` of length

\[
\boxed{\log\sqrt{x}-\log\log\sqrt{x}+O(1),}
\tag{10}
\]

just below the classical mean prime-gap scale there.

Now define the composite-prime-power Lambert neighborhood

\[
\mathcal C_{\ge2}(X)
:=\left\{x\in[X,2X]:
\exists\ p\,\text{prime},\ k\ge2,
\ |k\log p-\log x|<D_c(x)
\right\}.
\tag{11}
\]

Then

\[
\boxed{
|[X,2X]\setminus\mathcal C_{\ge2}(X)|
\ge
\left(2+o(1)\right)
\frac{X\log\log X}{\log X}.
}
\tag{12}
\]

If `\mathcal C_2(X)` denotes the square contribution and `\mathcal C_{\ge3}(X)` all deeper powers, the stronger component estimates are

\[
\boxed{
|\mathcal C_2(X)|
\le X-\left(2+o(1)\right)
\frac{X\log\log X}{\log X},
}
\tag{13}
\]

and

\[
\boxed{
|\mathcal C_{\ge3}(X)|
\ll X^{5/6}\log X
=o\!\left(\frac{X\log\log X}{\log X}\right).
}
\tag{14}
\]

## 1. Exact root decomposition

For each fixed `k`,

\[
\min_{p\,\text{prime}}|k\log p-\log x|
=k\min_{p\,\text{prime}}\left|\log p-\frac1k\log x\right|
=k\,\delta_{\mathrm p}(x^{1/k}).
\tag{15}
\]

Taking the minimum over `k` proves (3). Equation (6) follows immediately. The empty-prime interval is

\[
\left(x^{1/k}e^{-D_c(x)/k},\ x^{1/k}e^{D_c(x)/k}\right),
\tag{16}
\]

whose length is (7). Because `D_c(x)=O(log x/sqrt(x))`, the small-argument expansion of `sinh` is uniform for all fixed or growing `k>=1`. For `k>=3`,

\[
x^{1/k-1/2}W(c\sqrt{x})
\le x^{-1/6}W(c\sqrt{x})
=O(x^{-1/6}\log x),
\tag{17}
\]

so every deeper root interval is subunit. This does **not** delete its exact arithmetic condition; it classifies it as a thin resonance constraint rather than a macroscopic prime-free interval.

## 2. Prime squares are the critical layer

Put

\[
Y:=\sqrt X,
\qquad
w(t):=W(ct),
\tag{18}
\]

and write `x=z^2`. For `z in [Y,sqrt(2)Y]`, a prime square `p^2` violates the Lambert separation precisely when

\[
2|\log(z/p)|<\frac{w(z)}z.
\tag{19}
\]

Any solution with `p` in the relevant fixed multiplicative range has `|z-p|=O(log Y)`. On that window,

\[
2\log(z/p)
=\frac{2(z-p)}p
+O\!\left(\frac{(\log Y)^2}{Y^2}\right).
\tag{20}
\]

Also

\[
\frac{d}{dt}\left(\frac{W(ct)}t\right)
=-\frac{W(ct)^2}{t^2(1+W(ct))},
\tag{21}
\]

hence

\[
\frac{w(z)}z
=\frac{w(p)}p
+O\!\left(\frac{(\log Y)^2}{Y^2}\right).
\tag{22}
\]

The two endpoints of the forbidden `z`-interval are therefore

\[
z_\pm
=p\pm\frac12W(cp)
+O\!\left(\frac{(\log Y)^2}{Y}\right),
\tag{23}
\]

and the corresponding interval in `x=z^2` has length

\[
\boxed{
z_+^2-z_-^2
=2pW(cp)+O((\log Y)^2).
}
\tag{24}
\]

This is the scale match: the root-variable width is `W(cp)=log p-log log p+O(1)`, just below the mean spacing `log p` of primes near `p`.

## 3. PNT exposes the square-layer deficit

The square union is bounded by the sum of its interval lengths. Roots just outside the two endpoints but whose neighborhoods still meet the shell contribute only `O(Y(log Y)^2)`. Thus

\[
|\mathcal C_2(X)|
\le
2\sum_{Y<p\le\sqrt2Y}pW(cp)
+O(Y(\log Y)^2).
\tag{25}
\]

The classical prime number theorem with a standard zero-free-region error term, followed by partial summation, gives

\[
2\sum_{Y<p\le\sqrt2Y}pW(cp)
=
\int_Y^{\sqrt2Y}\frac{2tW(ct)}{\log t}\,dt
+o\!\left(\frac{Y^2}{\log Y}\right).
\tag{26}
\]

Uniformly over this fixed multiplicative interval,

\[
W(ct)=\log t-\log\log t+O(1),
\tag{27}
\]

so

\[
\frac{W(ct)}{\log t}
=1-\frac{\log\log Y}{\log Y}
+O\!\left(\frac1{\log Y}\right).
\tag{28}
\]

Since

\[
\int_Y^{\sqrt2Y}2t\,dt=Y^2=X,
\tag{29}
\]

we obtain

\[
2\sum_{Y<p\le\sqrt2Y}pW(cp)
=X-X\frac{\log\log Y}{\log Y}
+O\!\left(\frac X{\log Y}\right).
\tag{30}
\]

Finally

\[
\frac{\log\log Y}{\log Y}
=\left(2+o(1)\right)\frac{\log\log X}{\log X},
\tag{31}
\]

which proves (13). No disjointness or random-spacing model is used: overlaps only reduce the union.

The `-log log` term in Lambert `W` is load-bearing. A root width `log p+O(1)` would have first-order interval budget `X`; the actual `log p-log log p+O(1)` width leaves the deterministic deficit in (13).

## 4. Exponents k>=3 cannot fill that deficit

If `q=p^k`, `k>=3`, has a Lambert neighborhood meeting `[X,2X]`, then `q in [X/2,3X]` for all large `X`. The number of such prime powers is at most

\[
\sum_{3\le k\le\log_2(3X)}(3X)^{1/k}
=O(X^{1/3}).
\tag{32}
\]

For each one, `D_c(x)=O(log X/sqrt(X))` on the shell, so its excluded `x`-interval has length

\[
O\!\left(q\frac{\log X}{\sqrt X}\right)
=O(\sqrt X\log X).
\tag{33}
\]

A union bound yields

\[
|\mathcal C_{\ge3}(X)|
\ll X^{5/6}\log X,
\tag{34}
\]

which is negligible compared with `X log log X/log X`. Equations (13) and (14) then imply (12).

This is stronger than the statement that higher prime powers have zero natural density: the neighborhoods here themselves expand with `X`, at exactly the Lambert radius forced by the `WI-288` spectral balance.

## 5. What remains is a two-scale prime-gap problem

Let

\[
\mathcal R(X):=[X,2X]\setminus\mathcal C_{\ge2}(X).
\tag{35}
\]

For every `x in R(X)`, all composite prime powers are already at logarithmic distance at least `D_c(x)`. Therefore

\[
\boxed{
\delta_{\mathrm{pp}}(x)\ge D_c(x)
\iff
\delta_{\mathrm p}(x)\ge D_c(x)
\qquad(x\in\mathcal R(X)).
}
\tag{36}
\]

But (12) does not show that centers of the enormous prime gaps demanded by the right side meet `\mathcal R(X)`. In the exact root formulation, the two load-bearing conditions are

\[
\boxed{
\delta_{\mathrm p}(x)\ge D_c(x),
\qquad
\delta_{\mathrm p}(\sqrt{x})\ge\frac12D_c(x),
}
\tag{37}
\]

plus the sparse deeper-root resonances.

The first condition asks for the `WI-288` prime gap of total size about `sqrt(x) log x`. The second asks for a prime gap around `sqrt(x)` of total size

\[
W(c\sqrt{x})+o(1)
=\log\sqrt{x}-\log\log\sqrt{x}+O(1),
\tag{38}
\]

which is only at the average-gap scale. Thus squares create a genuine compatibility condition, but not a second square-root-scale obstruction.

A useful arithmetic closure theorem would therefore have to couple a hypothetical `sqrt(x) log x`-scale prime desert near `x` to prime occurrence in the much shorter root interval (38), or directly bound the nearest prime power at the `WI-288` Lambert scale. Merely observing that prime powers are denser than primes is insufficient.

## 6. Prior-art audit

The counting step uses only the classical prime number theorem and the standard large-argument expansion of Lambert `W` already present in `WI-287`--`WI-288`.

Kevin Ford, D. R. Heath-Brown and Sergei Konyagin, **Large Gaps Between Consecutive Prime Numbers Containing Perfect Powers**, in *Analytic Number Theory* (2015), 83--92, DOI `10.1007/978-3-319-22240-0_5`, prove that for every fixed `k` very long prime gaps can contain perfect `k`-th powers. Helmut Maier and Michael Th. Rassias, **Large gaps between consecutive prime numbers containing perfect k-th powers of prime numbers**, *Journal of Functional Analysis* 272:6 (2017), 2659--2696, DOI `10.1016/j.jfa.2016.08.014`, place fixed `k`-th powers of primes inside infinitely many long prime gaps. These results are on the Erdos--Rankin polylogarithmic scale, far below the hypothetical `sqrt(x) log x` scale here, but they are a decisive warning that prime-gap and prime-power placement cannot be treated as independent random events.

For large-gap scale context, Kevin Ford, Ben Green, Sergei Konyagin and Terence Tao, **Large gaps between consecutive prime numbers**, *Annals of Mathematics* 183 (2016), 935--974, DOI `10.4007/annals.2016.183.3.4`, gives the modern unconditional large-gap lower-bound framework. On the uniform short-interval side, the Baker--Harman--Pintz peer-reviewed baseline and Runbo Li preprint frontier are already audited in `WI-286` and `SOURCES.md`; neither reaches the Lambert endpoint from `WI-288`.

Targeted searches around consecutive prime powers, prime powers in short intervals, perfect powers inside prime gaps, and prime-square placement found these power-placement constructions and numerical/sequence literature, but no theorem coupling an every-center `sqrt(x) log x`-scale prime-gap constraint to the mean-gap-scale square-root condition (38), and no uniform nearest-prime-power theorem at the required Lambert scale. This absence is not used as a historical-priority claim.

## 7. Stress tests and boundaries

- Equation (3) is exact; no density or randomness model enters it.
- Squares are **not** discarded as sparse. Their neighborhoods have first-order total budget `X`; the useful information is the second-order `-log log` deficit.
- The coverage estimate is one-sided and robust to overlap. Any overlap among square neighborhoods only increases the uncovered set.
- The residual set in (12) is not a counterexample: it need not contain a center of a prime gap large enough to satisfy the `k=1` condition.
- No statistical independence is assumed. The Ford--Heath-Brown--Konyagin and Maier--Rassias constructions explicitly forbid that shortcut.
- The `k>=3` estimate is intentionally crude because it is already negligible relative to the square-layer deficit.
- The fixed constant `c>0` inherited from `WI-288` changes only `O(1)` terms in `W(c sqrt(x))`, not the `-log log` deficit or the exponent classification.
- Only the symmetric two-island complete-screening branch is addressed. Sign-changing cancellation, incomplete screening, many-component supports, and global-null-equation amplitude information remain outside this reduction.

## Research consequence

At the exact endpoint exposed by `WI-288`, the full prime-power obstruction has the structure

\[
\boxed{
\text{huge prime-gap condition at }x
+\text{critical prime-square condition at }\sqrt{x}
+\text{sparse higher-root resonances}.
}
\tag{39}
\]

Therefore the route “use all prime powers because they are denser than primes” is closed at the support-geometric level. Exponents `k>=3` cannot fill the square-layer coverage deficit, and the square layer itself leaves `\gg X\log\log X/\log X` of every sufficiently large dyadic shell untouched at the required Lambert resolution.

The remaining arithmetic target is much sharper: prove that centers of prime gaps large enough for `WI-288` cannot simultaneously satisfy the square-root prime-gap condition (37), or prove a direct uniform nearest-prime-power bound at that scale. Otherwise the surviving source-specific alternatives remain the global Suzuki null equation or a support topology with several genuinely independent macroscopic separations.