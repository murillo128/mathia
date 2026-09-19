# RE-227 — Fixed-corridor real single-center Wiener gap is uniform

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + EXACT-REMAINDER + DIAGONAL-COMPACTNESS + FIXED-CORRIDOR-UNIFORMIZATION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-222--RE-226.

RE-226 closes every asymptotic boundary mechanism for one **individual** fixed-corridor positive-real single-center family and proves that its normalized Wiener liminf is strictly larger than two. Its stated boundary is deliberately cautious: the proof as written does not exhibit one numerical margin valid for all differently tuned families, so it leaves open the possibility that their individual gaps could form a sequence tending to zero.

That possibility is incompatible with the same theorem. The admissible class is closed under diagonal extraction: if differently tuned families had gaps tending to zero, one can choose one sufficiently advanced predictor from each family so that prediction error tends to zero, the prediction scale tends to infinity, the fixed corridor is preserved, and the normalized Wiener rate tends to two. Those selected predictors themselves form a single admissible family, contradicting RE-226.

More precisely, fix `R>1`. Consider any sequence of exact normalized positive-real single-center predictors

\[
F_\nu(z)
=
F_{m_\nu,N_\nu,a_\nu}(z)
=
\frac{Q_{m_\nu,N_\nu,a_\nu}(z)}{Q_{m_\nu,N_\nu,a_\nu}(1)},
\tag{1}
\]

with

\[
Q_{m,N,a}(z)
:=
z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\tag{2}
\]

and moving arcs `0<alpha_nu<pi/2`. Call such a family `R`-admissible when

\[
\epsilon_\nu
:=
\sup_{|\theta|\le\alpha_\nu}
|F_\nu(e^{-i\theta})-1|
\to0,
\qquad
m_\nu\alpha_\nu\to\infty,
\tag{3}
\]

when the single-center contraction condition

\[
r(\alpha_\nu,a_\nu)
:=
\left|1-\frac{e^{-i\alpha_\nu}}{a_\nu}\right|<1
\tag{4}
\]

holds, and when

\[
\lambda_\nu:=\frac{N_\nu}{m_\nu}
\le R-1+o(1).
\tag{5}
\]

Under the RE-216 scaling, (5) is exactly the asymptotic fixed delay corridor `[H,RH+o(H)]`. Put

\[
c_\nu
:=
\frac{\log\|F_\nu\|_A}{m_\nu\alpha_\nu}.
\tag{6}
\]

Then there exists a constant `eta_R>0`, depending only on the fixed corridor ratio, such that **every** `R`-admissible family satisfies

\[
\boxed{
\liminf_{\nu\to\infty} c_\nu
\ge 2+\eta_R.
}
\tag{7}
\]

Equivalently, if

\[
\underline C_{1c,+}(R)
:=
\inf_{\mathcal F\;R\text{-admissible}}
\liminf c_\nu,
\tag{8}
\]

then

\[
\boxed{
\underline C_{1c,+}(R)>2.
}
\tag{9}
\]

The corresponding infimum defined with `limsup`, matching the convention used for `C_sep` in RE-217, is therefore also strictly larger than two. The result is nonconstructive at the final step: it proves existence of `eta_R` but does not supply a useful numerical value.

## 1. The apparent family-wise loophole is diagonally closed

Assume (7) is false for some fixed `R`. Then for every integer `j>=1` there exists an `R`-admissible family

\[
\mathcal F^{(j)}
=
\left\{
F^{(j)}_k,
\alpha^{(j)}_k,
 m^{(j)}_k,
 N^{(j)}_k,
 a^{(j)}_k
\right\}_{k\ge1}
\tag{10}
\]

such that

\[
\liminf_{k\to\infty}
\frac{\log\|F^{(j)}_k\|_A}
{m^{(j)}_k\alpha^{(j)}_k}
<2+\frac1j.
\tag{11}
\]

Because each family is admissible, its prediction error tends to zero, its product `m alpha` tends to infinity, and its corridor excess in (5) tends to zero. Because (11) is a liminf statement, arbitrarily far out in that same family there are predictors whose normalized rate is below `2+2/j`.

Choose one index `k(j)` sufficiently far out that all of the following hold simultaneously:

\[
\epsilon^{(j)}_{k(j)}<\frac1j,
\qquad
m^{(j)}_{k(j)}\alpha^{(j)}_{k(j)}>j,
\qquad
m^{(j)}_{k(j)}>j,
\tag{12}
\]

\[
\frac{N^{(j)}_{k(j)}}{m^{(j)}_{k(j)}}
\le R-1+\frac1j,
\tag{13}
\]

and

\[
\frac{\log\|F^{(j)}_{k(j)}\|_A}
{m^{(j)}_{k(j)}\alpha^{(j)}_{k(j)}}
<2+\frac2j.
\tag{14}
\]

There is no synchronization problem: the first three requirements eventually hold for all sufficiently large indices, while the liminf condition supplies infinitely many arbitrarily large indices satisfying (14).

Now discard the superscripts and regard the selected predictors

\[
\widetilde F_j:=F^{(j)}_{k(j)}
\tag{15}
\]

as one new sequence. Every defining property of the representation is pointwise, so each selected predictor is still an exact normalized positive-real single-center polynomial satisfying contraction. Equations (12)--(13) give

\[
\widetilde\epsilon_j\to0,
\qquad
\widetilde m_j\widetilde\alpha_j\to\infty,
\qquad
\widetilde\lambda_j\le R-1+o(1).
\tag{16}
\]

Thus `\widetilde F_j` is itself an `R`-admissible fixed-corridor family. But (14) gives

\[
\limsup_{j\to\infty}
\frac{\log\|\widetilde F_j\|_A}
{\widetilde m_j\widetilde\alpha_j}
\le2,
\tag{17}
\]

and in particular its liminf is at most two.

This contradicts equation (6) of RE-226, which applies to **every** admissible fixed-corridor positive-real single-center family and gives a strict liminf larger than two. The contradiction proves (7)--(9).

The argument is intentionally phrased with a liminf in (11), which is stronger than needed for the `C_sep`-style limsup extremal constant. It shows that the family-wise conclusion of RE-226 is sequentially uniform once the corridor ratio is fixed.

## 2. Why no hidden regularity assumption is lost in the diagonal

A diagonal argument would be invalid if admissibility imposed coherence between consecutive members of one family: monotonicity of parameters, a prescribed analytic parameter curve, a common expansion center, or a convergence rate uniform before the limit. The single-center extremal problem imposes none of those conditions.

The hypotheses used by RE-222--RE-226 are exactly the stagewise representation identities plus the asymptotic conditions in (3)--(5). The polynomial order may pass to any subsequence; `alpha`, `a`, and `lambda=N/m` are already allowed to drift arbitrarily; and all lower bounds are formulated for such moving sequences. Selecting one late stage from each differently tuned family therefore creates no new object outside the theorem class.

The `o(1)` in the corridor condition also causes no uniformity problem. For the `j`-th source family, choose `k(j)` after its own corridor error is below `1/j`. Equation (13) then makes the diagonal corridor error itself tend to zero. The same device handles prediction error and the expanding-window condition.

This is the exact place where fixing `R` matters. If the corridor ratios themselves were allowed to satisfy `R_j\to\infty`, the selected diagonal would no longer lie in any fixed corridor and RE-226 would not apply. The theorem therefore gives one positive `eta_R` for each finite `R`; it does not claim that `inf_R eta_R` is positive.

## 3. Relation to the existing lower-bound chain

No new analytic estimate is needed. RE-223 is what prevents a bounded-rate diagonal from hiding in `lambda->0`; RE-224 keeps its positive real center bounded inside a fixed corridor; RE-225 collapses contraction-boundary escape into a vanishing arc; RE-226 makes that vanishing arc infinitely expensive; and RE-222 supplies a strict gap on whatever compact interior remains. Those ingredients prove strictness for every possible diagonal sequence, and the present extraction turns that sequential strictness into a class-level gap.

The result corrects the only remaining logical caveat in the positive-real single-center closure. It is no longer possible that a sequence of separately tuned fixed-corridor families has individual rates

\[
2+\eta_1,
\quad
2+\eta_2,
\quad\ldots,
\qquad
\eta_j\downarrow0,
\tag{18}
\]

while each family separately obeys RE-226. If such families existed, choosing successively later near-liminf members would manufacture precisely the forbidden rate-two diagonal family.

This still does **not** improve the universal separated-measure lower bound

\[
C_{\rm sep}\ge1.
\tag{19}
\]

The theorem prices only the positive-real single-center negative-binomial representation. Complex-center exact cancellation, multi-center coefficient recombination, minimax polynomials, rational prediction, and other approximation bases remain outside it. Nor does (9) sharpen the current constructive upper bound; it says only that further optimization inside this fixed-corridor real single-center class cannot make the class constant converge to two.

## 4. Adversarial and prior-art audit

The decisive falsification check is diagonal closure itself. The contradiction would fail if any hypothesis of RE-226 were not inherited by the selected stages. Equations (12)--(16) verify all asymptotic hypotheses explicitly, while positivity/reality of the center, exact DC normalization, and contraction are properties of each selected polynomial. No assumption about the speed of convergence is imported across source families.

A second check is the order of the two limits. The proof does not interchange a nonuniform `j`-limit with a within-family `k`-limit. For each fixed `j`, all requirements are first satisfied by choosing one sufficiently large `k(j)`; only after that finite choice is made does `j` tend to infinity. This is the standard diagonal construction and needs no uniform convergence theorem.

The surrounding mathematics is classical. Ferreira--Kempf and later superoscillation work study exponential dynamic-range/energy penalties for reproducing frequencies outside a spectral band; Temme and Nemes--Olde Daalhuis study the incomplete-beta asymptotics underlying this representation. Broad prior-art search also finds general Wiener-algebra norm inequalities and stable band-limited extrapolation. None supplies or is required for the line-specific statement (7): the new step is only the elementary diagonal closure of the exact representation-local theorems RE-222--RE-226. No novelty is claimed for the diagonal principle itself, and no external theorem is load-bearing, so `SOURCES.md` requires no change.

## Research consequence

The positive-real single-center frontier is now closed at the level of the **class constant**, not merely family by family. For every fixed finite delay corridor there is a genuine, if presently nonquantified, margin above Wiener rate two. Therefore even an arbitrarily elaborate sequence of real-center retunings cannot asymptotically squeeze this representation down to the factor-two boundary.

The next useful constructive question should change geometry rather than continue scalar retuning. The live routes remain genuinely complex-center exact cancellation, multi-center/minimax prediction, or another basis. A separate high-value problem is to make `eta_R` quantitative; that could reveal whether the known explicit rate `5.996390` is merely a poor construction inside the class or whether a much larger part of the remaining gap is representation-intrinsic.