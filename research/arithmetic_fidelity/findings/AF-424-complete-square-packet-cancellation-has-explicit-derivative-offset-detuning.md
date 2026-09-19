# AF-424 — Complete square-packet cancellation has explicit derivative-offset detuning

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `SQUARE-TRANSITION` · `SIGNED-RESUMMATION` · `SCHUR-CAUCHY` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-421--AF-423 on a fixed square-transition fiber. Fix `m>=1` and `a>0`, write

\[
s_n=2n+d_n,
\qquad
\alpha_n=\frac{d_n}{n}\longrightarrow0,
\]

and assume

\[
b_n=a\,n^{\alpha_n}\longrightarrow m^2.
\]

Retain AF-422's rectangle quantities

\[
\Xi_{n,m}
=
\log n+n\log\!\left(\frac{b_n}{m^2}\right)-d_n\log m,
\]

\[
K_m
=
\frac{4m e^{2m}}{(2m-1)^2\zeta(2m)},
\qquad
F_{n,m}=\frac{C_{n,m}}{C_{n,m-1}},
\]

and AF-423's complete adjacent-packet ratio

\[
Q_{n,m}
=
F_{n,m}\frac{G_{n,m}}{G_{n,m-1}}.
\]

Then the rectangle ratio has the uniform refinement

\[
\boxed{
\log F_{n,m}
=
\Xi_{n,m}+\log K_m+m\alpha_n
+
\frac{-m^2+m-1-\frac12m^2\alpha_n}{n}
+O(n^{-2}).
}
\tag{1}
\]

The residual Schur--Cauchy packets satisfy the sharper varying-depth law

\[
\boxed{
\log\frac{G_{n,m}}{G_{n,m-1}}
=
\frac{a e^{2+\alpha_n}(2+\alpha_n)}{n}
+O(n^{-2}).
}
\tag{2}
\]

Consequently, if

\[
\Omega_{n,m}
:=
\Xi_{n,m}+\log K_m+m\alpha_n,
\tag{3}
\]

then

\[
\boxed{
\log Q_{n,m}
=
\Omega_{n,m}
+
\frac{
-m^2+m-1-\frac12m^2\alpha_n
+a e^{2+\alpha_n}(2+\alpha_n)
}{n}
+O(n^{-2}).
}
\tag{4}
\]

This makes AF-423's first complete-packet cancellation condition explicit in the underlying square-fiber coordinates. In particular,

\[
n\log Q_{n,m}\longrightarrow0
\]

if and only if

\[
\boxed{
 n\Omega_{n,m}
-
 m^2+m-1-rac12m^2\alpha_n
+a e^{2+\alpha_n}(2+\alpha_n)
\longrightarrow0.
}
\tag{5}
\]

Since `alpha_n->0`, an equivalent simpler limit condition is

\[
\boxed{
 n\bigl(\Xi_{n,m}+\log K_m\bigr)+m d_n
\longrightarrow
m^2-m+1-2ae^2.
}
\tag{6}
\]

Thus AF-422's leading condition `Xi_{n,m}->-log K_m` and AF-423's abstract condition `n log F_{n,m}->-2ae^2` hide one more retained coordinate: the derivative-offset term `m alpha_n` in the rectangle ratio. Equation `(6)` is the first-order complete-packet cancellation interface written entirely in the source parameters.

The residual drift itself has the expansion

\[
\boxed{
\log\frac{G_{n,m}}{G_{n,m-1}}
=
\frac{2ae^2}{n}
+
\frac{3ae^2d_n}{n^2}
+O\!\left(\frac{d_n^2}{n^3}+\frac1{n^2}\right).
}
\tag{7}
\]

If `a!=m^2`, the square condition implies

\[
\alpha_n\log n
\longrightarrow
\log\!\left(\frac{m^2}{a}\right),
\]

so `(7)` exposes a deterministic `1/(n log n)` correction before the ordinary `1/n^2` scale. This correction is invisible if one first replaces `alpha_n` by its limit zero.

Equations `(4)--(6)` still do **not** make polynomial cancellation sufficient for boundedness. For `m>=2`, the tied saddle rate `Lambda_m>1`; after `(6)` the remaining `O(n^{-2})` relative mismatch is still exponentially amplified unless still finer tuning removes it. Eventually the exponentially small residual tall-column and neighboring-saddle scales become load-bearing.

## 1. Refining the exact rectangle ratio

AF-422 gives the exact factorization

\[
F_{n,m}
=
n\left(\frac{b_n}{m^2}\right)^n
m^{1-d_n}
\left(1+\frac mn\right)^{2n+d_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(2+\frac{2m-1}{n}\right)^2
\frac1{(2m-1)^2}.
\tag{8}
\]

Subtracting `Xi_{n,m}+log K_m` from its logarithm leaves

\[
(2n+d_n-1)\log\!\left(1+\frac mn\right)
-2m
+
2\log\!\left(1+\frac{2m-1}{2n}\right)
+
\log\zeta(2(n+m)).
\tag{9}
\]

Because `alpha_n=d_n/n->0`, Taylor expansion with `alpha_n` retained gives

\[
(9)
=
m\alpha_n
+
\frac{-m^2+m-1-\frac12m^2\alpha_n}{n}
+O(n^{-2}),
\tag{10}
\]

while `log zeta(2(n+m))` is exponentially small. This proves `(1)`.

The point is structural: the factor `(1+m/n)^{d_n}` is asymptotically invisible in AF-422's zeroth-order limit but contributes `m alpha_n` before the inverse-`n` scale. On a square fiber with `a!=m^2`, this is normally of order `1/log n`, not `1/n`.

## 2. A fixed residual partition retains the varying derivative depth

For a residual partition `mu` with `mu_n=0`, put

\[
D=|\mu|,
\qquad
\kappa_\mu
=
\sum_{j\ge1}\mu_j(\mu_j-2j+1)
=
2\sum_{u\in\mu}c(u),
\tag{11}
\]

where `c(u)` is the box content. For the AF-421 packet around `r` full columns, let

\[
W_{n,r}(\mu)
=
(-1)^D\left(\frac{a}{n^2}\right)^D
s_\mu(1^n)^2
\mathcal R_{n,r,\mu}^{(s_n)}.
\tag{12}
\]

If row `j` has length `delta=mu_j`, its active index is `i=n+1-j`. Writing `c_j=r+1-j`, the power part of `mathcal R` has

\[
\log\!\left(1+\frac{\delta}{n+c_j}\right)
=
\frac{\delta}{n}
-
\frac{c_j\delta+\delta^2/2}{n^2}
+O_\mu(n^{-3}).
\tag{13}
\]

Multiplication by `s_n-1=n(2+alpha_n)-1`, addition of the odd-distance factor, and summation over rows yield

\[
\log \mathcal R_{n,r,\mu}^{(s_n)}
=
(2+\alpha_n)D
+
\frac{
D-(2+\alpha_n)\left((r+\tfrac12)D+\tfrac12\kappa_\mu\right)
}{n}
+O_\mu(n^{-2}).
\tag{14}
\]

The zeta ratios contribute only exponentially small errors for fixed `mu`, because every active zeta argument is `2n+O_\mu(1)`.

The hook-content formula gives

\[
s_\mu(1^n)
=
\frac{n^D}{H_\mu}
\prod_{u\in\mu}\left(1+\frac{c(u)}n\right),
\]

hence

\[
2\log\!\left(
\frac{H_\mu s_\mu(1^n)}{n^D}
\right)
=
\frac{\kappa_\mu}{n}+O_\mu(n^{-2}).
\tag{15}
\]

Set

\[
x_n=-a e^{2+\alpha_n}.
\tag{16}
\]

Combining `(12)--(16)` gives the signed fixed-shape expansion

\[
\boxed{
W_{n,r}(\mu)
=
\frac{x_n^D}{H_\mu^2}
\left[
1-
\frac{
2rD+\alpha_n\left((r+\tfrac12)D+\tfrac12\kappa_\mu\right)
}{n}
+O_\mu(n^{-2})
\right].
}
\tag{17}
\]

The shape-sensitive first correction is exactly the content statistic `kappa_mu` multiplied by `alpha_n`. It disappears after summing the packet, but that disappearance has to be proved rather than assumed.

## 3. Conjugation kills the first shape correction

For each degree `D`, partition conjugation preserves the hook product and reverses all box contents:

\[
H_{\mu'}=H_\mu,
\qquad
\kappa_{\mu'}=-\kappa_\mu.
\]

Self-conjugate partitions have `kappa_mu=0`. Therefore

\[
\boxed{
\sum_{\mu\vdash D}
\frac{\kappa_\mu}{H_\mu^2}=0.
}
\tag{18}
\]

Together with the hook-length identity

\[
\sum_{\mu\vdash D}\frac1{H_\mu^2}=\frac1{D!},
\tag{19}
\]

this turns `(17)` into a scalar packet correction. Summing over `D` and using

\[
\sum_D\frac{x_n^D}{D!}=e^{x_n},
\qquad
\sum_D D\frac{x_n^D}{D!}=x_n e^{x_n},
\]

gives

\[
\boxed{
G_{n,r}
=
e^{x_n}
\left[
1-
\frac{x_n}{n}
\left(2r+\alpha_n(r+\tfrac12)\right)
+O(n^{-2})
\right].
}
\tag{20}
\]

The exchange of the expansion with the complete packet uses the same split as AF-423. Choose `eta` with `1/2<eta<1`. On residual partitions with no column higher than `eta n`, Taylor remainders in `(13)--(15)` are bounded by a fixed polynomial in the degree divided by `n^2`; AF-423's positive Schur--Cauchy majorant has uniformly finite polynomial degree moments. A slowly growing degree cutoff makes the complementary non-tall factorial tail `o(n^{-2})`. On the tall-column sector, AF-421's strict condition

\[
b<(r+2)^2
\]

holds at `b=m^2` for both `r=m-1` and `r=m`, so that sector is exponentially small and remains `o(n^{-2})`. Since `alpha_n` is bounded, the constants can be chosen uniformly along the sequence.

Taking logarithms in `(20)` and subtracting the cases `r=m` and `r=m-1` gives

\[
\log\frac{G_{n,m}}{G_{n,m-1}}
=
-\frac{x_n(2+\alpha_n)}{n}+O(n^{-2}),
\]

which is `(2)`. Expanding `e^{alpha_n}(2+alpha_n)=2+3alpha_n+O(alpha_n^2)` yields `(7)`.

## 4. The first complete cancellation coordinate

Equation `(4)` shows that the square-transition hierarchy has one more explicit layer:

\[
\Xi_{n,m}
\quad\leadsto\quad
\Omega_{n,m}=\Xi_{n,m}+\log K_m+m\alpha_n
\quad\leadsto\quad
n\log Q_{n,m}.
\]

The leading coordinate `Xi` decides whether the two rectangles can even approach the same amplitude. The correction `m alpha_n` is the first information discarded when the varying derivative depth is replaced by its limit `alpha_n->0`. The inverse-`n` term then combines the rectangle expansion with the residual-packet drift.

Multiplying `(4)` by `n` proves `(5)`, and using `n alpha_n=d_n` plus `alpha_n->0` gives `(6)`. Expanding `(1)` also shows directly that `(6)` is equivalent to AF-423's condition `n log F_{n,m}->-2ae^2`; the new content is the explicit translation of that condition into the square-fiber source parameters and the uniform varying-depth packet correction `(2)`.

For `m>=2`, satisfying `(6)` only removes the first polynomial mismatch. Because

\[
\Lambda_m
=
\frac{m^{2m-2}}{((m-1)!)^2}>1,
\]

any residual whose relative nth-root tends to one is still exponentially amplified by the tied saddle. The next decisive object is therefore not another zeroth-order square coordinate: it is either the next complete-packet term if it already forbids admissible tuning, or the first beyond-all-orders residual/tall-column scale once polynomial terms have been canceled.

## Prior-art and novelty audit

The hook-content and hook-length formulas, Schur Cauchy identities, and partition-conjugation symmetry used above are classical symmetric-function and symmetric-group representation theory; AF-421 already audits these ingredients against I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed. Okounkov's **“Infinite wedge and random partitions,”** *Selecta Mathematica* 7 (2001), 57--81, arXiv `math/9907127`, places Schur measures and their Toda structure in the established literature. Borodin--Okounkov--Olshanski's **“Asymptotics of Plancherel measures for symmetric groups,”** *JAMS* 13 (2000), 481--515, arXiv `math/9905032`, is classical background for poissonized-Plancherel partition asymptotics.

A targeted search across hook-content asymptotics, Schur/Plancherel measures, rectangular partitions, and coalescing-saddle expansions did not locate the exact varying-derivative Euler-log packet formulas `(1)--(7)`. **No novelty claim is made**: the durable content is the direct specialization that exposes the derivative-offset coordinate and converts AF-423's implicit packet condition into the explicit detuning law `(6)`.

## Boundaries and falsification checks

- The result fixes `m` and `a` and assumes `alpha_n=d_n/n->0` with `b_n->m^2`. It does not cover a growing saddle index or the genuinely supercritical regime `s_n/n->sigma>2`.
- The `O(n^{-2})` packet error uses the strict residual tall-column gap for `r=m-1,m`. It must not be transported to a parameter boundary where that gap closes.
- Equation `(18)` removes only the first content correction after summing the complete Schur packet. It is not a claim that all shape-sensitive higher corrections vanish.
- If `a=m^2`, the `1/(n log n)` corollary from `(7)` has zero leading coefficient; finer behavior of `alpha_n` then matters.
- Equation `(6)` is necessary and sufficient only for cancellation through the `n log Q` scale. It is not sufficient for boundedness, convergence, recovery of the fixed-partition exponential, a zeta-zero discriminator, or RH.
- For `m=1`, formulas `(1)--(7)` remain valid, but `Lambda_1=1`; the exponential-amplification consequence for `m>=2` does not apply.
- No rational-prime discriminator or RH implication is established here.

## Consequence for the research line

The odd square-transition interface is now explicit through its first complete-packet polynomial scale. The apparent single tuning `Xi_{n,m}->-log K_m` actually contains a nested hierarchy: the varying derivative offset first contributes `m alpha_n`, and the rectangle and Schur-packet corrections then combine at order `1/n`. The source-coordinate condition `(6)` is exactly what survives after these compressions are undone.

The accepted full-tail clue is therefore narrower. Future work should impose `(6)` rather than merely `n log F->-2ae^2`, derive the next nonzero term of `Q_{n,m}-1`, and compare it with the first exponentially smaller residual/tall-column and neighboring-saddle families. If successive polynomial coefficients can all be tuned away, the problem has crossed from ordinary asymptotic refinement to a beyond-all-orders fidelity question.