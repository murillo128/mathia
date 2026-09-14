# WI-289 — Lambert prime-power screening has a critical prime-square layer

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the arithmetic endpoint isolated by `WI-288` for the **one-signed, completely screened, symmetric two-island** branch. This finding asks whether the union of higher prime powers can itself supply enough extra local density to make the nearest-prime-power Lambert obstruction substantially stronger than an ordinary prime-gap obstruction.
- **Result:** the full nearest-prime-power condition admits an exact root-scale decomposition. At the `WI-288` Lambert threshold, prime squares are the unique higher-power layer with a macroscopic root-scale constraint: they demand a prime-free interval of length about one mean prime gap around `sqrt(x)`. Every exponent `k>=3` produces only a subunit root-scale window and, on a dyadic `x`-shell, the union of all corresponding Lambert neighborhoods has measure `O(X^(5/6) log X)`. The square layer is genuinely critical rather than negligible: its total interval budget on `[X,2X]` is

  \[
  X-\left(2+o(1)\right)\frac{X\log\log X}{\log X}.
  \]

  Consequently the union of **all composite prime-power** Lambert neighborhoods still leaves a set of measure at least

  \[
  \boxed{
  \left(2+o(1)\right)\frac{X\log\log X}{\log X}
  }
  \]

  uncovered. Thus higher powers cannot uniformly fill the arithmetic gap left by current prime-in-short-interval theorems. The unresolved two-island obstruction reduces, at this scale, to a coupled two-scale problem: a very large prime desert near `x`, together with an approximately mean-gap prime desert near `sqrt(x)`; exponents `k>=3` impose only sparse resonance exclusions.
- **What it does not claim:** this does not produce an `x` satisfying the full `WI-288` condition, does not prove that a large prime gap near `x` can be chosen simultaneously away from prime-square neighborhoods, does not rule out the two-island branch, and does not assert statistical independence between prime gaps at `x` and at `sqrt(x)`. Existing large-gap constructions containing powers of primes are a specific warning against such an independence assumption.
- **Novelty boundary:** the prime number theorem, the parametrization `p^k` of prime powers, average prime-gap scale, and the Lambert-`W` asymptotic are classical. Ford--Heath-Brown--Konyagin and Maier--Rassias show that long prime gaps can be arranged to contain perfect powers, including fixed powers of primes. The new line-local deductions are the exact root-scale decomposition of `WI-288`'s nearest-prime-power distance, the identification of `k=2` as the unique critical higher-power layer at the Lambert endpoint, and the dyadic measure barrier showing that even the entire composite-prime-power union leaves `gg X log log X / log X` of each large dyadic shell uncovered. Targeted searches did not locate this specific Lambert-scale decomposition or coverage estimate; search absence is audit context only, not a priority claim.

## Claim

For `y>1`, define the nearest-prime logarithmic distance

\[
\delta_{\rm p}(y)
:=\min_{p\ {m prime}}|\log p-\log y|.
\tag{1}
\]

Recall from `WI-288`

\[
\delta_{\rm pp}(x)
:=\min_{p\ {m prime},\ k\ge1}|k\log p-\log x|.
\tag{2}
\]

Then, **exactly**,

\[
\boxed{
\delta_{\rm pp}(x)
=\min_{k\ge1} k\,\delta_{\rm p}(x^{1/k}).
}
\tag{3}
\]

Let `c>0` be fixed and put

\[
D_c(x):=\frac{W(c\sqrt{x})}{\sqrt{x}}.
\tag{4}
\]

Thus the `WI-288` necessary condition has the form

\[
\delta_{\rm pp}(x)\ge D_c(x)
\tag{5}
\]

for some absolute fixed `c>0`. By (3), (5) is equivalent to the simultaneous family

\[
\boxed{
\delta_{\rm p}(x^{1/k})\ge\frac{D_c(x)}{k}
\qquad(k\ge1).
}
\tag{6}
\]

At the first three depth regimes this says:

\[
\begin{aligned}
k=1:&\quad
\text{a prime-free interval around }x
\text{ of total length }
2\sqrt{x}\,W(c\sqrt{x})(1+o(1));\\

k=2:&\quad
\text{a prime-free interval around }\sqrt{x}
\text{ of total length }
W(c\sqrt{x})(1+o(1));\\

k\ge3:&\quad
\text{a prime-free interval around }x^{1/k}
\text{ of total length }
\frac{2}{k}x^{1/k-1/2}W(c\sqrt{x})(1+o(1)).
\end{aligned}
\tag{7}
\]

In particular,

\[
W(c\sqrt{x})
=\log\sqrt{x}-\log\log\sqrt{x}+O(1),
\tag{8}
\]

so the square constraint has length

\[
\boxed{
\log\sqrt{x}-\log\log\sqrt{x}+O(1),
}
\tag{9}
\]

which is just below the classical mean prime-gap scale `log sqrt(x)`, while uniformly for every `k>=3`

\[
\frac{2}{k}x^{1/k-1/2}W(c\sqrt{x})\to0.
\tag{10}
\]

There is also a quantitative coverage barrier. Define the composite-prime-power Lambert neighborhood on the dyadic shell by

\[
\mathcal C_{\ge2}(X)
:=\left\{
 x\in[X,2X]:
 \exists\ p\text{ prime},\ k\ge2,
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

More precisely, if `\mathcal C_2(X)` is the contribution from prime squares and `\mathcal C_{\ge3}(X)` the contribution from exponents at least three, then

\[
\boxed{
|\mathcal C_2(X)|
\le
X-\left(2+o(1)\right)
\frac{X\log\log X}{\log X},
}
\tag{13}
\]

whereas

\[
\boxed{
|\mathcal C_{\ge3}(X)|
\ll X^{5/6}\log X
=o\!\left(\frac{X\log\log X}{\log X}\right).
}
\tag{14}
\]

Thus prime squares are the only composite layer whose Lambert neighborhoods have first-order dyadic coverage. Even they are slightly subcritical because the `-log log` correction in `W` leaves a deterministic coverage deficit larger than the entire contribution of all `k>=3` layers.

## 1. Exact root-scale decomposition

For each fixed `k>=1`,

\[
\begin{aligned}
\min_{p\ {m prime}}
|k\log p-\log x|
&=k\min_{p\ {m prime}}
\left|\log p-\frac1k\log x\right|\\
&=k\,\delta_{\rm p}(x^{1/k}).
\end{aligned}
\tag{15}
\]

Taking the minimum over `k` proves (3). No asymptotic arithmetic input is used here.

The logarithmic condition in (6) says that the interval

\[
\left(
 x^{1/k}e^{-D_c(x)/k},
 x^{1/k}e^{D_c(x)/k}
\right)
\tag{16}
\]

contains no prime. Its additive length is exactly

\[
2x^{1/k}\sinh\!\left(\frac{D_c(x)}k\right).
\tag{17}
\]

Since

\[
D_c(x)
=O\!\left(\frac{\log x}{\sqrt{x}}\right)\to0,
\tag{18}
\]

(17) equals

\[
\frac{2}{k}x^{1/k-1/2}W(c\sqrt{x})(1+o(1)).
\tag{19}
\]

This proves (7). For `k=2`, putting `y=sqrt(x)` gives

\[
2y\sinh\!\left(\frac{W(cy)}{2y}\right)
=W(cy)+o(1),
\tag{20}
\]

and the standard expansion

\[
W(cy)=\log y-\log\log y+O(1)
\tag{21}
\]

gives (9). For `k>=3`,

\[
x^{1/k-1/2}W(c\sqrt{x})
\le x^{-1/6}W(c\sqrt{x})
=O(x^{-1/6}\log x),
\tag{22}
\]

which proves (10).

This identifies the scale transition exactly:

\[
\boxed{
\text{prime layer: macroscopic }\sqrt{x}\log x;
\quad
\text{square layer: mean-gap }\log\sqrt{x};
\quad
k\ge3: o(1).
}
\tag{23}
\]

The `k>=3` statement is about the additive size of the forbidden interval in the root variable. It does not say the corresponding exact arithmetic exclusions disappear; it says they are thin resonance conditions rather than macroscopic prime-free intervals.

## 2. A single prime square consumes `2 p W(cp)` of x-space

The criticality of squares is more precise than the scale comparison (23). Put

\[
Y:=\sqrt X,
\qquad
w(t):=W(ct).
\tag{24}
\]

Write `x=z^2`, so `z in [Y,sqrt(2)Y]`. A prime square `p^2` excludes those `z` satisfying

\[
2|\log(z/p)|<\frac{w(z)}{z}.
\tag{25}
\]

Any solution with `p\asymp Y` has

\[
|z-p|=O(\log Y),
\tag{26}
\]

because the right side of (25) is `O(log Y/Y)`. On this window,

\[
2\log(z/p)
=\frac{2(z-p)}p
+O\!\left(\frac{(\log Y)^2}{Y^2}\right),
\tag{27}
\]

while the exact derivative identity

\[
\frac{d}{dt}\left(\frac{W(ct)}t\right)
=-\frac{W(ct)^2}{t^2(1+W(ct))}
\tag{28}
\]

gives

\[
\frac{w(z)}z
=\frac{w(p)}p
+O\!\left(\frac{(\log Y)^2}{Y^2}\right).
\tag{29}
\]

Therefore the two endpoints of the forbidden `z`-interval satisfy

\[
z_\pm
=p\pm\frac12w(p)
+O\!\left(\frac{(\log Y)^2}{Y}\right).
\tag{30}
\]

Returning to `x=z^2`, the corresponding interval has length

\[
\boxed{
z_+^2-z_-^2
=2pW(cp)+O((\log Y)^2).
}
\tag{31}
\]

This explains why squares are exactly critical. Near height `p`, the average prime spacing is `log p`; the square-neighborhood width in the root variable is `W(cp)=log p-log log p+O(1)`, just short of that spacing.

## 3. PNT gives a logarithmic coverage deficit for the square layer

The union of square neighborhoods is at most the sum of their lengths. Squares whose neighborhoods meet the endpoints of `[X,2X]` but whose roots lie just outside `[Y,sqrt(2)Y]` contribute only

\[
O(Y(\log Y)^2),
\tag{32}
\]

which is negligible below. Summing (31) over the interior primes gives

\[
|\mathcal C_2(X)|
\le
2\sum_{Y<p\le\sqrt2Y}pW(cp)
+O(Y(\log Y)^2).
\tag{33}
\]

Use the classical prime number theorem with its standard zero-free-region error term and partial summation. Since `t` remains in a fixed multiplicative interval,

\[
2\sum_{Y<p\le\sqrt2Y}pW(cp)
=
\int_Y^{\sqrt2Y}
\frac{2tW(ct)}{\log t}\,dt
+o\!\left(\frac{Y^2}{\log Y}\right).
\tag{34}
\]

Uniformly on this interval,

\[
W(ct)
=\log t-\log\log t+O(1),
\tag{35}
\]

so

\[
\frac{W(ct)}{\log t}
=1-\frac{\log\log Y}{\log Y}
+O\!\left(\frac1{\log Y}\right).
\tag{36}
\]

Because

\[
\int_Y^{\sqrt2Y}2t\,dt=Y^2=X,
\tag{37}
\]

we obtain

\[
2\sum_{Y<p\le\sqrt2Y}pW(cp)
=
X-X\frac{\log\log Y}{\log Y}
+O\!\left(\frac X{\log Y}\right).
\tag{38}
\]

Since

\[
\frac{\log\log Y}{\log Y}
=
\left(2+o(1)\right)
\frac{\log\log X}{\log X},
\tag{39}
\]

(13) follows.

The key point is the second-order term. If the square-root forbidden radius had been based on `log p+O(1)` rather than

\[
W(cp)=\log p-\log\log p+O(1),
\tag{40}
\]

its summed interval budget would already be of order the full dyadic shell. The Lambert `-log log` correction leaves a macroscopic deficit of order `X log log X / log X`.

No disjointness between the square neighborhoods is assumed. Overlaps only decrease their union, so (13) is an unconditional upper bound.

## 4. All exponents k>=3 are negligible even in union

Suppose a prime power `q=p^k`, `k>=3`, has a Lambert neighborhood meeting `[X,2X]`. Since

\[
D_c(x)=O(\log X/\sqrt X)
\tag{41}
\]

uniformly on the shell, such a `q` lies in `[X/2,3X]` for all sufficiently large `X`. The number of prime powers of exponent at least three in that range is bounded by

\[
\sum_{3\le k\le\log_2(3X)}(3X)^{1/k}
=O(X^{1/3}).
\tag{42}
\]

For each such `q`, the set of `x\asymp X` satisfying

\[
|\log q-\log x|<D_c(x)
\tag{43}
\]

has length

\[
O\!\left(q\frac{\log X}{\sqrt X}\right)
=O(\sqrt X\log X).
\tag{44}
\]

A union bound therefore gives

\[
|\mathcal C_{\ge3}(X)|
\ll X^{1/3}\sqrt X\log X
=X^{5/6}\log X,
\tag{45}
\]

which is (14).

Combining (13) and (14),

\[
\begin{aligned}
|\mathcal C_{\ge2}(X)|
&\le |\mathcal C_2(X)|+|\mathcal C_{\ge3}(X)|\\
&\le X-
\left(2+o(1)\right)
\frac{X\log\log X}{\log X},
\end{aligned}
\tag{46}
\]

and (12) follows.

This is a stronger statement than the elementary fact that higher prime powers have zero natural density. The relevant neighborhoods themselves grow with `X`; (12) says that even after thickening every composite prime power by exactly the Lambert radius forced by the Suzuki spectral balance, they still fail to cover every possible center.

## 5. The unresolved arithmetic target is now explicitly two-scale

Let

\[
\mathcal R(X):=[X,2X]\setminus\mathcal C_{\ge2}(X).
\tag{47}
\]

For `x in \mathcal R(X)`, every composite prime power already satisfies

\[
|k\log p-\log x|\ge D_c(x)
\qquad(k\ge2).
\tag{48}
\]

Hence on this residual set the full `WI-288` arithmetic condition reduces exactly to the ordinary prime condition

\[
\boxed{
\delta_{\rm pp}(x)\ge D_c(x)
\quad\Longleftrightarrow\quad
\delta_{\rm p}(x)\ge D_c(x)
\qquad(x\in\mathcal R(X)).
}
\tag{49}
\]

But (12) alone gives no reason for the set of centers of very large prime gaps to meet `\mathcal R(X)`. Equivalently, before passing to the measure relaxation, the exact root formulation (6) shows that the load-bearing simultaneous constraints are

\[
\boxed{
\begin{cases}
\delta_{\rm p}(x)\ge D_c(x),\\[2mm]
\delta_{\rm p}(\sqrt{x})\ge D_c(x)/2,
\end{cases}
}
\tag{50}
\]

plus the sparse `k>=3` resonance exclusions.

The first line of (50) is the very large prime-gap obstruction already exposed by `WI-288`. The second is qualitatively different: it asks only for a prime gap around `sqrt(x)` of total length

\[
W(c\sqrt{x})+o(1)
=\log\sqrt{x}-\log\log\sqrt{x}+O(1),
\tag{51}
\]

which is at approximately the average prime-gap scale. Thus prime squares do not create another square-root-scale miracle requirement; they create a **critical root-scale compatibility condition**.

This changes the useful arithmetic question. A route trying to close the two-island branch via prime powers should not seek a generic theorem saying merely that prime powers are denser than primes. It needs a theorem coupling a hypothetical prime desert of size about `sqrt(x) log x` near `x` to prime occurrence in the much shorter interval (51) near `sqrt(x)`, or else a direct uniform bound for nearest prime powers at the `WI-288` Lambert scale.

## 6. Prior-art audit and why independence is not available

The prime-counting input in (34) is classical. A quantitative prime number theorem with the classical de la Vallee Poussin zero-free-region error is far stronger than the precision needed to detect the `log log / log` deficit in (38).

The relevant large-gap literature gives an important falsification control. Kevin Ford, D. R. Heath-Brown and Sergei Konyagin, **Large Gaps Between Consecutive Prime Numbers Containing Perfect Powers**, in *Analytic Number Theory* (2015), 83--92, DOI `10.1007/978-3-319-22240-0_5`, prove that for every fixed `k` there are very long prime gaps containing perfect `k`-th powers. Helmut Maier and Michael Th. Rassias, **Large gaps between consecutive prime numbers containing perfect k-th powers of prime numbers**, *Journal of Functional Analysis* 272:6 (2017), 2659--2696, DOI `10.1016/j.jfa.2016.08.014`, strengthen this in the direction relevant here by placing `k`-th powers of primes inside infinitely many long prime gaps for fixed `k>=2`.

These gaps are on the Erdos--Rankin polylogarithmic scale, far below the hypothetical `sqrt(x) log x` gap forced by `WI-288`, so they neither prove nor refute (50). They do show that one cannot justify (50) by pretending that prime-gap location and prime-power location are independent random events.

For scale context, Kevin Ford, Ben Green, Sergei Konyagin and Terence Tao, **Large gaps between consecutive prime numbers**, *Annals of Mathematics* 183 (2016), 935--974, DOI `10.4007/annals.2016.183.3.4`, gives the modern unconditional large-gap lower-bound framework. On the opposite side, the peer-reviewed uniform short-interval baseline and the stronger current-preprint frontier remain the Baker--Harman--Pintz and Runbo Li inputs already audited in `WI-286` and `SOURCES.md`; neither approaches the Lambert endpoint needed by `WI-288`.

Targeted searches around consecutive prime powers, prime powers in short intervals, perfect powers inside prime gaps, and prime-square placement found the above prime-avoidance constructions and numerical/sequence literature, but no theorem coupling an every-`x` `sqrt(x) log x`-scale prime gap constraint to the mean-gap-scale square-root condition (51), and no uniform nearest-prime-power theorem at the required Lambert scale. This absence is not used as a historical-priority claim.

## 7. Stress tests and boundaries

- **The root identity is exact, not heuristic.** Equation (3) is simply the minimization over the unique prime-base/exponent representation of prime powers. No density model enters it.
- **The square layer is not declared negligible.** Its Lambert neighborhoods have first-order total budget `X`; the useful fact is the negative second-order correction in (38). Calling all higher powers sparse without isolating squares would miss the critical layer.
- **The coverage estimate is one-sided.** The sum of square-neighborhood lengths bounds the union from above. Overlap can only make the uncovered set larger; no spacing independence or pair-correlation theorem for primes is used.
- **The residual set is not a counterexample.** Equation (12) says many centers avoid composite prime powers at Lambert resolution, not that any of those centers also have the enormous prime-free interval required by `k=1`.
- **No statistical independence.** Maier--Rassias and Ford--Heath-Brown--Konyagin explicitly demonstrate arithmetic constructions where large prime gaps contain prescribed kinds of powers. Any future intersection argument must use an actual theorem, not a random-model product.
- **The `k>=3` union estimate is deliberately crude.** It is already `o(X log log X/log X)`, so improving its exponent cannot alter the conclusion that squares are the unique critical composite layer.
- **Fixed `c>0`.** The unknown absolute constant inherited from the `WI-288` spectral inequality affects only `O(1)` terms in `W(c sqrt(x))`. It does not change the `-log log` coverage deficit or the scale classification.
- **Only the symmetric two-island complete-screening branch is addressed.** Sign-changing cancellation, incomplete screening, many-component supports, and amplitude information from the global Suzuki null equation remain outside this reduction.

## Research consequence

`WI-288` reduced complete two-island support screening to a nearest-prime-power gap. The present finding resolves what the higher-power part of that arithmetic object can buy at the exact spectral endpoint:

\[
\boxed{
\text{Lambert nearest-prime-power obstruction}
=
\text{huge prime-gap condition at }x
+\text{critical prime-square condition at }\sqrt{x}
+\text{sparse higher-root resonances}.
}
\tag{52}
\]

The tempting route

\[
\text{``use all prime powers because they are denser than primes''}
\tag{53}
\]

is therefore too coarse. Exponents `k>=3` are quantitatively incapable of filling the square-layer coverage deficit, and squares themselves leave `gg X log log X/log X` of every large dyadic shell untouched at the required Lambert resolution.

The live arithmetic escape is sharper: prove that centers of prime gaps large enough for `WI-288` cannot simultaneously satisfy the square-root prime-gap condition in (50), or obtain a direct uniform nearest-prime-power bound at that scale. Otherwise the source-specific route remains the global Suzuki null equation or a support topology with genuinely several independent macroscopic separations.