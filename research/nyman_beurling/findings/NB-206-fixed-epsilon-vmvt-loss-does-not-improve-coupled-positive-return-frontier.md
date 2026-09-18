# NB-206 — Fixed-epsilon VMVT gains do not improve the coupled positive-return frontier

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE + SOURCE-ACQUISITION + EXPONENTIAL-SUM + QUANTIFIER-AUDIT + NB-205-METHOD-BOUNDARY`.

`NB-205` leaves an apparently tempting improvement route: replace Ford's explicit logarithmic exponential-sum estimate by a modern Vinogradov-mean-value bound with a much larger saving constant. Heath-Brown's 2017 estimate seems, at first sight, to do exactly that. For

\[
\tau:=\frac{\log |t|}{\log N}\ge 2
\]

it gives, for every fixed `epsilon>0`,

\[
\boxed{
\sum_{n\in I}n^{-it}
\ll_{\epsilon}
N^{1-49/(80\tau^2)+\epsilon}
}
\tag{1}
\]

for intervals `I subset (N,2N]` in the stated logarithmic-phase class. The coefficient `49/80=0.6125` is vastly larger than Ford's explicit coefficient `1/133.66=0.00748...`.

Nevertheless, **(1) does not improve the `NB-205` coupled corridor as stated**. The fixed `N^epsilon` loss becomes dominant as soon as the logarithmic height ratio `tau` tends to infinity. In particular, the substitution

\[
\frac1{133.66}
\rightsquigarrow
\frac{49}{80}
\]

inside the `NB-205` threshold is invalid.

More generally, any estimate of the form

\[
\left|\sum_{n\in I}n^{-it}\right|
\le C_\epsilon N^{1-c/\tau^2+\epsilon}
\tag{2}
\]

known only **for each fixed `epsilon>0` with uncontrolled `C_epsilon`** cannot by itself feed the `NB-202`/`NB-205` angular-resolution occupancy argument along any regime `tau->infinity`. To reach the Vinogradov--Korobov-scale corridor one needs an epsilon-free estimate, or quantitative uniform control strong enough to let `epsilon=epsilon_N` shrink at least on the scale `log log N/log N` while also controlling `C_(epsilon_N)`.

Thus the modern optimal-VMVT derivative technology and Ford's older explicit Vinogradov--Korobov estimate occupy genuinely different roles here. The former has a better formal exponent for fixed `tau`; the latter remains useful when `tau` grows with the source scale because its saving is explicit and uniform in that parameter.

## 1. Why the larger Heath-Brown coefficient is unusable in the coupled limit

Write

\[
X:=\log N,
\qquad
Q:=\log |t|,
\qquad
\tau=\frac QX.
\tag{3}
\]

Dividing (1) by `N`, the normalized Fourier coefficient is bounded by

\[
C_\epsilon
\exp\!\left\{
-\frac{49}{80}\frac{X}{\tau^2}
+\epsilon X
\right\}.
\tag{4}
\]

For every fixed `epsilon>0`, if `tau->infinity` then eventually

\[
\frac{49}{80\tau^2}<\frac\epsilon2.
\]

Hence the exponent in (4) is eventually at least `epsilon X/2`. The quoted estimate then ceases even to improve the trivial normalized bound `1`. This is not a weakness of the `NB-205` transfer; it occurs before Erdős--Turán is applied.

The quantifiers matter. Equation (1) says

\[
\forall\epsilon>0\text{ fixed},\quad
\exists C_\epsilon,\quad
\text{the estimate holds as }N,t\text{ vary}.
\]

It does **not** provide a uniform theorem for a moving choice `epsilon=epsilon_N->0`. Choosing a new smaller epsilon as `N` grows is therefore not a valid asymptotic substitution unless the dependence of both the implied constant and the threshold of validity on epsilon is supplied.

A diagonal choice of fixed epsilons does not repair this. For any one fixed epsilon, a sequence with `tau->infinity` eventually leaves the nontrivial range `c/tau^2>epsilon`. Covering the tail would require the epsilon itself to vary with the sequence.

## 2. The NB-205 scale makes the lost uniformity quantitative

The `NB-205` frontier has

\[
Q
=\kappa\frac{X^{3/2}}{\sqrt{\log X}},
\qquad
\tau^2
=\kappa^2\frac{X}{\log X}.
\tag{5}
\]

If the `N^epsilon` term were absent, the Heath-Brown saving in (4) would be

\[
\exp\!\left\{
-\frac{49}{80\kappa^2}\log X
\right\}
=
X^{-49/(80\kappa^2)}.
\tag{6}
\]

This would indeed be strong enough to replace Ford's coefficient and enlarge the corridor dramatically. But the actual theorem contributes

\[
e^{\epsilon X},
\tag{7}
\]

which dominates every fixed power of `X` for every fixed positive epsilon.

The full `NB-205` occupancy transfer also pays the Euler atom factor `X` and the Erdős--Turán harmonic factor `log X`. For a generic estimate (2), the required smallness is

\[
C_\epsilon X\log X
\exp\!\left\{
-c\frac{X}{\tau^2}+\epsilon X
\right\}
=o(1).
\tag{8}
\]

At the scale (5), this requires

\[
\log C_\epsilon+\epsilon X
\le
\left(\frac c{\kappa^2}-1-o(1)\right)\log X.
\tag{9}
\]

Consequently any usable moving epsilon must satisfy at least

\[
\epsilon_X=O\!\left(\frac{\log X}{X}\right),
\tag{10}
\]

and the corresponding constant must remain at most polynomial on that coupled choice, more precisely `log C_(epsilon_X)=O(log X)` with enough margin for (9). Heath-Brown's theorem does not provide such dependence.

Equation (9) is the useful method criterion left by this finding. A future VMVT-based replacement for Ford need not be literally epsilon-free, but it must make the epsilon dependence quantitative enough to satisfy (9).

## 3. Why this does not contradict the strength of modern VMVT

Heath-Brown's result is genuinely stronger in its intended fixed-parameter regime. His paper derives new `k`-th derivative estimates from the optimal Vinogradov mean value theorem and records the logarithmic-phase consequence (1). The same paper also explicitly notes the limitation relevant here: the modern VMVT input does not give the explicit dependence on degree/mean-value parameters needed near the `sigma=1` boundary, and the resulting zeta estimate gives no useful information as `sigma` tends to `1`.

That is exactly the analogue of the present coupled obstruction. In Mathia's variables, approaching the one-line corresponds to allowing

\[
\tau=\frac{\log |t|}{\log N}
\]

to grow. A fixed-parameter `N^epsilon` theorem can improve fixed polynomial shell ranges, but it cannot follow this growing ratio without additional uniformity.

This also explains why `NB-204` deliberately used the weaker all-orders derivative theorem of Arias de Reyna: there the constants are explicit and uniformly bounded as the derivative order grows. `NB-205` then improves the height law further using Ford's explicit epsilon-free estimate. Formal exponent quality at fixed parameters and uniformity in a coupled limit are different resources.

## 4. Adversarial checks and representation audit

**Could one simply choose epsilon after seeing `N`?** Not from (1). The theorem supplies a constant for each fixed epsilon. A proof that selects `epsilon_N` needs a stated bound for the resulting constants and validity thresholds. Without it, the inference changes the quantifier order.

**Could the implied constant be ignored because only asymptotics matter?** No. Even if `C_epsilon=1`, the term `epsilon X` already overwhelms the desired saving when epsilon is fixed and `tau->infinity`. The unknown constant is a second obstruction, not the first one.

**Does this show Heath-Brown's estimate is false or weaker than Ford's?** No. It is stronger for many fixed-parameter applications. The claim is only that its published `N^epsilon` form does not dominate Ford in the specific simultaneous limit needed after `NB-205`.

**Does this rule out all modern VMVT improvements?** No. An explicit version with controlled dependence on the degree and epsilon, or a direct logarithmic-sum theorem with no `N^epsilon` loss, could improve the corridor. Equation (9) states the quantitative target such a theorem must meet.

**Is the obstruction arithmetic-specific?** The quantifier failure is generic. What is line-specific is the shrinking angular resolution `1/X`, the Euler atom tariff `X`, and the coupled logarithmic height `tau->infinity`. These turn a normally harmless `N^epsilon` loss into a leading-order obstruction.

**Does any of this improve the Nyman distance directly?** No. As in `NB-205`, this is source-acquisition analysis. Positivity remains load-bearing, and the separate destination bridge from successful Nyman approximation to an `o(a)` positive Euler-shell return is still unproved.

## Prior-art boundary

D. R. Heath-Brown's 2017 paper is the load-bearing literature source. Its equation (7), derived from Theorem 4, gives (1) with the coefficient `49/80`, and its discussion explicitly distinguishes the strong fixed-parameter asymptotic result from the missing uniform information near the one-line. The underlying optimal Vinogradov mean value theorem is classical modern prior art and is not claimed here.

A targeted literature search also checked recent explicit zeta and derivative-estimate work. It did not locate a published replacement for Ford's logarithmic exponential-sum theorem that simultaneously has the stronger modern VMVT exponent and the epsilon/parameter uniformity required by (9). Absence from that search is not treated as a novelty claim.

The durable line-local result is therefore a **negative transfer theorem**: the attractive coefficient `49/80` cannot be imported into `NB-205` by treating `N^epsilon` as lower order. The coupled limit makes it dominant.

## Consequence for the research frontier

The positive-source branch should not spend further effort substituting fixed-epsilon VMVT estimates into the existing Erdős--Turán transfer. `NB-205` remains the stronger usable theorem in the growing-`tau` regime despite its much smaller numerical saving coefficient.

There are now two precise ways to improve that branch. One is an epsilon-free or quantitatively uniform logarithmic exponential-sum estimate satisfying (9). The other is the source-specific route already identified by `NB-205`: estimate the **von-Mangoldt-weighted** logarithmic Fourier coefficients directly, avoiding the all-integers discrepancy plus point-mass tariff. Neither route is supplied by the fixed-epsilon theorem audited here.

The larger structural frontiers remain unchanged: positivity must eventually be left behind to treat signed/complex synthesis, and an independent destination-coupled argument must still show what Euler acquisition condition is actually forced by small Nyman--Beurling approximation error.