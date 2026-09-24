# FD-310 — Principal-frequency phase-growth exponents obey an exact shell-depth barrier

- **Date:** 2026-09-24
- **Status:** proved exact theorem-design threshold for principal-frequency pointwise bounds and quantified the balanced-depth exponent required to close the live shell range
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens source ceiling / Fejér low-pass witness / principal-frequency pointwise bounds / shell-depth squeeze / theorem-design barrier
- **Depends on:** FD-300, FD-304, FD-307, FD-308, FD-309
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL-REDUCTION + CONDITIONAL-THEOREM-TEMPLATE + THRESHOLD-PHASE-DIAGRAM + NEGATIVE/OBSTRUCTION + FRONTIER-REFINEMENT`

## Claim

Let

\[
c:=1-\log_2(3/2)=0.4150374992\ldots
\tag{1}
\]

and retain the near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)},
\qquad
x=N^{\lambda+o(1)}.
\tag{2}
\]

FD-300 gives the unconditional source ceiling

\[
\lambda\le \lambda_{\rm src}:=\frac1{2c}
=1.2047104198\ldots .
\tag{3}
\]

Under RH, throughout the nonvacuous common-window range

\[
\lambda>\lambda_{\rm cw}:=\frac{3}{10c}
=0.7228262519\ldots,
\tag{4}
\]

FD-304 and FD-307 give a capacity-bearing shell

\[
Q=x^{\rho+o(1)},
\qquad
2c\le\rho\le1,
\qquad
X=NQ=N^{1+\lambda\rho+o(1)},
\tag{5}
\]

and a frequency `alpha_*` satisfying

\[
\|\alpha_*\|_{\mathbb T}
\le
\delta_N
:=N^{-1/4-(3c/2)\lambda+o(1)}
\tag{6}
\]

and

\[
|F_X(\alpha_*)|
\ge
X^{1/2}
N^{(9c/4)\lambda-5/8-o(1)},
\tag{7}
\]

where

\[
F_X(\alpha)
=
\sum_{X\le n<2X}\mu(n)e(n\alpha).
\tag{8}
\]

Consider the following theorem template on that **same fixed dyadic block**: for a fixed `theta` with

\[
0\le\theta\le\frac12,
\tag{9}
\]

suppose one can prove, uniformly throughout the FD-307 principal neighborhood,

\[
\boxed{
|F_X(\alpha)|
\le
X^{1/2+o(1)}
\bigl(1+X\|\alpha\|_{\mathbb T}\bigr)^\theta
\qquad
(\|\alpha\|_{\mathbb T}\le\delta_N).
}
\tag{10}
\]

This is a theorem-design hypothesis, not a claim that such an estimate is currently known for `theta<1/2`.

Then survival of the near-capacity premise forces

\[
\boxed{
\lambda
\le
\Lambda_\theta(\rho)
:=
\frac{5+6\theta}
{18c+12c\theta-8\theta\rho}.
}
\tag{11}
\]

For `theta>0`, the same condition can be written as the shell-depth requirement

\[
\boxed{
\rho
\ge
R_\theta(\lambda)
:=
\frac{3c}{2}
+
\frac1\lambda
\left(
\frac{(9c/4)\lambda-5/8}{\theta}
-
\frac34
\right).
}
\tag{12}
\]

The denominator in (11) is positive throughout `0<=theta<=1/2` and `2c<=rho<=1`. For `theta>0`, `Lambda_theta(rho)` is increasing in `rho`, so the deepest allowed shell `rho=1` is the shell-uniform obstruction.

The exact source-ceiling comparison is

\[
\boxed{
\Lambda_\theta(1)<\lambda_{\rm src}
\quad\Longleftrightarrow\quad
\theta<c.
}
\tag{13}
\]

Hence, **within the pointwise principal-frequency template (10), a phase-growth exponent strictly below `c=0.415037...` is necessary and sufficient for the resulting shell-uniform contradiction threshold to enter below the existing source ceiling**. At `theta=c`, the deepest shell `rho=1` is exactly tangent to `lambda_src`; at `theta=1/2`, the shallow shell `rho=2c` is exactly tangent to `lambda_src`, recovering the Baker--Harman tangency in FD-309.

At balanced depth `lambda=1`, the condition becomes especially concrete. A theorem of the form (10) kills **every** RH-allowed carrying shell precisely when

\[
\boxed{
\theta<\theta_{\rm bal}
:=
\frac{18c-5}{2(7-6c)}
=0.2739244180\ldots .
}
\tag{14}
\]

The shallow-shell threshold is

\[
\boxed{
\theta_{\rm sh}
:=
\frac{18c-5}{2(3+2c)}
=0.3225361106\ldots .
}
\tag{15}
\]

Thus at `lambda=1`:

- if `theta>=theta_sh`, (10) adds no shell-depth information beyond the existing `rho>=2c` floor;
- if `theta_bal<theta<theta_sh`, it forces the carrier deeper, namely `rho>=R_theta(1)` with `2c<R_theta(1)<1`;
- if `theta<theta_bal`, it contradicts the FD-307 witness for every `rho in [2c,1]` and therefore closes the balanced near-capacity route within the current reduction.

For example, `theta=0.3` would already force

\[
\rho\ge0.9020041601\ldots
\tag{16}
\]

at balanced depth, whereas `theta=0.25` would force `R_theta(1)>1` and hence give a contradiction.

This quantifies the phrase "substantially improve Baker--Harman" left qualitative in FD-309. A tiny improvement from the Baker--Harman phase-growth exponent `1/2` is not enough to settle balanced depth. Without extra shell structure, the exponent must fall below approximately `0.274`.

## 1. Comparison of a generic phase-growth bound with the forced witness

From (5)--(6),

\[
X\delta_N
=
N^{A(\lambda,\rho)+o(1)},
\tag{17}
\]

where

\[
A(\lambda,\rho)
:=
\frac34
+
\lambda\left(\rho-\frac{3c}{2}\right).
\tag{18}
\]

Because `rho>=2c`,

\[
A(\lambda,\rho)
\ge
\frac34+\frac{c\lambda}{2}>0.
\tag{19}
\]

Therefore the hypothetical estimate (10), evaluated at the selected frequency from FD-307, gives

\[
|F_X(\alpha_*)|
\le
X^{1/2}
N^{\theta A(\lambda,\rho)+o(1)}.
\tag{20}
\]

The forced lower bound (7) exceeds (20) by a fixed power exactly when

\[
\frac{9c\lambda}{4}-\frac58
>
\theta
\left[
\frac34+\lambda\left(\rho-\frac{3c}{2}\right)
\right].
\tag{21}
\]

Multiplying by `8` and collecting the `lambda` terms gives

\[
\lambda
\bigl(18c+12c\theta-8\theta\rho\bigr)
>
5+6\theta.
\tag{22}
\]

This proves (11). Equality is only tangency: the `o(1)` terms in the lower and upper bounds do not yield a contradiction there, so every exclusion statement above uses a strict inequality.

For `theta>0`, rearranging (21) instead for `rho` gives (12). Thus the same calculation has two interpretations: a sufficiently strong theorem either kills the route outright or squeezes any surviving source carrier toward larger denominator shells.

The endpoint `theta=0` is simpler. Then (10) is a square-root-scale pointwise estimate and (21) reduces to

\[
\lambda>\frac{5}{18c}
=0.6692835666\ldots .
\tag{23}
\]

Since this is already below the common-window onset (4), a genuine square-root principal-frequency theorem would kill the entire FD-307-active interval.

## 2. Two exact tangencies explain the present barrier

Set `theta=1/2` in (11). One obtains

\[
\Lambda_{1/2}(\rho)
=
\frac{2}{6c-\rho}
=
\frac1{3c-\rho/2},
\tag{24}
\]

which is exactly the Baker--Harman principal-frequency threshold derived in FD-309. At the shallow shell `rho=2c`,

\[
\Lambda_{1/2}(2c)
=
\frac1{2c}
=\lambda_{\rm src}.
\tag{25}
\]

So FD-309 is recovered as the `theta=1/2` edge of the full phase diagram.

The opposite shell edge reveals a second exact tangency. At `rho=1`, comparing (11) with (3) gives

\[
\frac{5+6\theta}
{18c+12c\theta-8\theta}
<
\frac1{2c}
\tag{26}
\]

if and only if

\[
2c(5+6\theta)
<18c+12c\theta-8\theta,
\tag{27}
\]

which simplifies exactly to

\[
\theta<c.
\tag{28}
\]

At `theta=c`, the deepest shell is tangent to the source ceiling. Consequently, lowering the phase-growth exponent from `1/2` to a value in `[c,1/2)` can improve shallow-shell information near the source ceiling, but it still cannot yield a shell-uniform contradiction anywhere below that ceiling. To enter the live interval uniformly, one must cross the stronger boundary `theta<c`.

This is not a statement that `c` is an intrinsic exponent of Möbius exponential sums. It is the exact exponent at which the **current Farey source demand, FD-307 localization, and maximal allowed shell depth** balance.

## 3. Balanced depth requires a much stronger exponent than source-ceiling entry

At `lambda=1`, the forced excess over square-root size in (7) is

\[
\Delta_{\rm bal}
:=
\frac{9c}{4}-\frac58
=0.3088343734\ldots .
\tag{29}
\]

The phase-growth cost in (20) is

\[
\theta
\left(
\frac34+\rho-\frac{3c}{2}
\right).
\tag{30}
\]

This cost increases with `rho`. At the deepest shell `rho=1`, a contradiction therefore requires

\[
\theta
<
\frac{\Delta_{\rm bal}}
{7/4-3c/2}
=
\frac{18c-5}{2(7-6c)},
\tag{31}
\]

which is (14). At the shallow shell `rho=2c`, the corresponding threshold is

\[
\theta
<
\frac{\Delta_{\rm bal}}
{3/4+c/2}
=
\frac{18c-5}{2(3+2c)},
\tag{32}
\]

which is (15).

The interval between these two constants is a genuine shell-squeeze regime. For `theta` in that interval the theorem template is strong enough to eliminate low-`rho` carriers but not strong enough to eliminate the deepest shells. Equation (12) gives the exact surviving shell floor.

More generally, for any fixed active depth `lambda`, the shell-uniform critical phase exponent is

\[
\boxed{
\Theta_{\rm unif}(\lambda)
:=
\frac{(9c/4)\lambda-5/8}
{3/4+\lambda(1-3c/2)}.
}
\tag{33}
\]

A bound (10) with `theta<Theta_unif(lambda)` closes that depth for all carrying shells; equality is tangent. This critical exponent rises from about

\[
0.0488841579\ldots
\tag{34}
\]

at the common-window boundary `lambda=lambda_cw` to exactly

\[
c=0.4150374992\ldots
\tag{35}
\]

at the source ceiling `lambda=lambda_src`. Balanced depth sits well inside this interpolation at the value (14).

This phase diagram makes the theorem target scale-sensitive. A result strong enough merely to enter the top of the live interval need not come close to settling `lambda=1`; conversely, a theorem reaching `theta<0.273924...` would settle balanced depth without first improving the source ceiling or localizing the carrying shell further.

## 4. Prior-art and evidence boundary

The only load-bearing external theorem behind the present comparison is still the Baker--Harman GRH estimate already anchored in `SOURCES.md` and audited in FD-309. The calculation here is internal: it replaces Baker--Harman's specific exponent `theta=1/2` by a symbolic phase-growth exponent and solves the resulting Farey shell constraints exactly.

A fresh literature check on 2026-09-24 did not identify a theorem that supplies (10) with the required exponent in this shrinking `q=1` neighborhood. Cha--Kim's 2025 fixed-irrational estimate has a different regime, while Robles' September 2026 effective rational-approximation theorem assumes nontrivial denominator range `3<=R<=q` and therefore does not furnish the principal `q=1` estimate needed here. The new September 2026 squarefree exponential-sum theorem concerns `mu^2`, not the signed Möbius block (8). These are prior-art boundary checks only; none is used in the derivation, so `SOURCES.md` requires no new load-bearing anchor for this finding.

The finding does **not** prove that a bound with `theta<c`, `theta<theta_bal`, or any other improved exponent exists. It also does not show that every possible pointwise theorem must have the form (10). A theorem exploiting the source-selected shell, joint frequency-shell arithmetic, averaging rather than pointwise control, a sharper FD-307 witness, or additional Farey structure can evade this template entirely.

Likewise, failure of (21) is not evidence that a carrying shell exists; it says only that the pointwise upper bound (10), combined with the present lower witness, does not contradict it by a power. The shell interval (5), the common-window threshold (4), and the witness (6)--(7) remain RH-conditional inputs inherited from FD-304 and FD-307.

The practical frontier is therefore quantitative. If the route remains a generic principal-frequency Möbius problem, the target is no longer merely "better than Baker--Harman": it must cross `theta<c` to penetrate the live source interval uniformly and must reach `theta<0.2739244180...` to close balanced depth without further shell information. Alternatively, a Farey-specific improvement that forces `rho<1`, increases the witness amplitude, or narrows the frequency window would change these thresholds and is the more line-specific way to avoid collapsing entirely into `mobius_cancellation`.
