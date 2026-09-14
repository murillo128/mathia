# NB-121 — finite nested-cutoff coherence collapses to the maximal section

**Status:** `EXACT-DERIVED + NB-120-COROLLARY + CROSS-CUTOFF-MATCHED-CONTROL + PERFECT-TARGET-CAPTURE + NEGATIVE/ROUTE-NARROWING + CLUE-RESOLUTION + REPRESENTATION-AUDIT`.

`NB-120` leaves cross-cutoff coherence as one of the few ambient resources not yet tested against the inverse-section matched control. Its control is rebuilt for each declared cell cutoff `R`, so it is natural to ask whether requiring one common source vector to work at two or more nested cutoffs forces extra norm beyond order `R`.

For any **fixed finite nested ladder**, it does not. In the natural-cell model, the simultaneous exact constraints are already equal to the single constraint at the largest cell cutoff together with the largest Nyman section. Consequently the `NB-120` control at the maximal section is automatically a common control for every smaller cutoff, and every bounded-ratio cutoff retains the same inverse-section order.

More precisely, let

\[
2\le R_1\le\cdots\le R_J=R_*,
\qquad
\frac{R_j}{R_*}\longrightarrow c_j\in(0,1],
\tag{1}
\]

for a fixed `J`, and let `M_j>=2` be the Nyman-section depths required at those cutoffs. Put

\[
M_*:=\max_{1\le j\le J}M_j,
\tag{2}
\]

and assume the growing mixed-tail regime

\[
M_*\longrightarrow\infty,
\qquad
\frac{M_*^6(1+\log M_*)}{R_*}\longrightarrow0.
\tag{3}
\]

Retain the objects of `NB-118`--`NB-120`,

\[
V_M=\operatorname{span}\{g_2,\ldots,g_M\},
\qquad
Q_R=P_{\operatorname{span}\{\psi_n:1\le n<R\}},
\qquad
e_R=Q_Re,
\qquad
L_R=\|e_R\|^2=1-\frac1R.
\tag{4}
\]

Then there is a **single** vector `f_*` satisfying, simultaneously for every `j`,

\[
f_*\perp V_{M_j},
\qquad
Q_{R_j}f_*=e_{R_j},
\qquad
q_{R_j}(f_*)=1,
\tag{5}
\]

and its retained fraction at each cutoff obeys

\[
\boxed{
\frac{\|Q_{R_j}f_*\|^2}{\|f_*\|^2}
=
\frac{c_j+o(1)}{\kappa_\infty R_j},
}
\tag{6}
\]

where `kappa_infty` is the finite positive constant of `NB-120`,

\[
\kappa_\infty
=
12\sum_p\frac{p^2(\log p)^2}{(p^2-1)^2}.
\tag{7}
\]

Thus bounded-ratio same-source coherence changes leading constants but **does not improve the inverse-section exponent**. In particular a dyadic pair `R,2R` has a common perfect-target control with retention `Theta(1/R)` at both cutoffs.

## 1. The simultaneous constraint set is exactly the maximal one

The key point is algebraic and does not use asymptotics. The natural-cell projections are nested:

\[
R\le S
\quad\Longrightarrow\quad
Q_RQ_S=Q_R.
\tag{8}
\]

Since `e_S=Q_Se`, this also gives

\[
Q_Re_S=e_R.
\tag{9}
\]

The Nyman sections are nested as well:

\[
M\le N
\quad\Longrightarrow\quad
V_M\subseteq V_N.
\tag{10}
\]

Therefore, for any finite collection `(R_j,M_j)` with maxima `(R_*,M_*)`,

\[
\boxed{
\begin{aligned}
&\{f:\ Q_{R_j}f=e_{R_j},\ f\perp V_{M_j}\ \text{for every }j\}\\
&\qquad=
\{f:\ Q_{R_*}f=e_{R_*},\ f\perp V_{M_*}\}.
\end{aligned}
}
\tag{11}
\]

The inclusion from left to right uses the members attaining `R_*` and `M_*`. For the reverse inclusion, `(8)`--`(10)` imply every smaller target equation and every smaller orthogonality equation automatically.

This identity is the decisive representation audit. Adding finitely many nested cell cutoffs and finitely many nested Nyman sections does **not** add a new linear source constraint once their maxima are already present. Any apparent two-cutoff incompatibility must therefore come either from how one normalizes the same common vector, from a non-nested observable, or from source structure absent from the ambient `V_M^perp` class.

## 2. The maximal `NB-120` repair is already the common repair

Apply `NB-120` to `(M_*,R_*)`. Under `(3)` it supplies an exact minimum-norm matched control

\[
f_*=f_{M_*,R_*}\in V_{M_*}^\perp,
\qquad
Q_{R_*}f_*=e_{R_*},
\tag{12}
\]

whose norm satisfies

\[
\|f_*\|^2
=L_{R_*}+\kappa_\infty R_*+o(R_*)
=\kappa_\infty R_*+o(R_*).
\tag{13}
\]

Equation `(11)` shows that the same vector solves the whole ladder exactly. Moreover the simultaneous feasible set is literally the maximal-cutoff feasible set, so the minimum-norm solution of the simultaneous perfect-target problem is not a new optimization problem: it is the same minimum-norm repair already solved by `NB-120`.

For each `j`, equations `(5)` and `(13)` give

\[
\frac{\|Q_{R_j}f_*\|^2}{\|f_*\|^2}
=
\frac{L_{R_j}}
     {L_{R_*}+\kappa_\infty R_*+o(R_*)}
=
\frac{1+o(1)}{\kappa_\infty R_*}.
\tag{14}
\]

Using `R_j/R_* -> c_j` turns `(14)` into `(6)`. Because every `c_j` is positive, each member of a fixed bounded-ratio ladder remains at `Theta(1/R_j)` retention.

The fixed-section version is identical. If `M_*` is fixed instead of tending to infinity, `NB-119` gives

\[
\frac{\|Q_{R_j}f_*\|^2}{\|f_*\|^2}
=
\frac{c_j+o(1)}{\kappa_{M_*}R_j}.
\tag{15}
\]

So the collapse is not a peculiarity of the limiting constant `kappa_infty`; it is already present before the growing-section limit.

## 3. The dyadic constant gap is real but source-free

Take the cheapest test proposed by `CLUE-cross-cutoff-coherence-breaks-inverse-section-repair`, namely the pair `R` and `2R`. The common control obtained from the larger cutoff satisfies

\[
\frac{\|Q_Rf_*\|^2}{\|f_*\|^2}
=
\frac{1+o(1)}{2\kappa_\infty R},
\tag{16}
\]

while

\[
\frac{\|Q_{2R}f_*\|^2}{\|f_*\|^2}
=
\frac{1+o(1)}{2\kappa_\infty R}
=
\frac{1+o(1)}{\kappa_\infty(2R)}.
\tag{17}
\]

Both cutoffs therefore achieve the sharp **inverse-section scale**, although the smaller cutoff loses a factor `2` relative to its independently rebuilt `NB-120` control.

That constant loss is unavoidable for a much simpler reason than arithmetic coherence. For any common vector having perfect target capture at both cutoffs,

\[
Q_Rf=e_R,
\qquad
Q_{2R}f=e_{2R},
\tag{18}
\]

its two retained fractions have the exact ratio

\[
\boxed{
\frac{\|Q_Rf\|^2/\|f\|^2}
     {\|Q_{2R}f\|^2/\|f\|^2}
=
\frac{L_R}{L_{2R}}.
}
\tag{19}
\]

Thus no common perfect-target vector can simultaneously reproduce the two independently normalized leading constants, whose ratio tends to `2`. If one measures the two-cutoff objective on their own inverse-section scales, the independent minima give

\[
R\eta_R^{\rm ind}
+(2R)\eta_{2R}^{\rm ind}
\longrightarrow
\frac{2}{\kappa_\infty},
\tag{20}
\]

whereas the common minimum-norm control gives

\[
R\eta_R^{\rm com}
+(2R)\eta_{2R}^{\rm com}
\longrightarrow
\frac{3}{2\kappa_\infty}.
\tag{21}
\]

There is therefore a positive leading-constant deficit `1/(2 kappa_infty)` relative to solving the two cutoffs independently. But `(19)` shows what this deficit is: it is the universal shared-norm geometry of nested target projections, not an additional Nyman source equation. It leaves the `1/R` exponent untouched and therefore cannot by itself exclude the inverse-section rescue isolated in `NB-118`.

For a fixed ladder with ratios `c_j`, the same calculation gives

\[
R_j\eta_j^{\rm com}
\longrightarrow
\frac{c_j}{\kappa_\infty},
\tag{22}
\]

so the simultaneous scaled sum is `(sum_j c_j)/kappa_infty`, versus `J/kappa_infty` for independently rebuilt controls. Again the difference records only how far each cutoff sits below the maximal one.

## 4. Stress tests and boundary of the obstruction

Several boundaries matter.

First, `(11)` uses exact nesting of both structures. It does not apply to non-nested observables, to extra tail constraints tied separately to each cutoff, or to a source law whose coefficients must transform in a prescribed way when the cutoff changes. Those are precisely the kinds of cross-scale data that could create a genuinely new compatibility condition.

Second, the bounded-ratio hypothesis in `(1)` is essential to the conclusion about the exponent at **every** cutoff. If a ladder spans a growing range so that `R_j/R_* -> 0` for an early cutoff, `(14)` becomes

\[
\frac{\|Q_{R_j}f_*\|^2}{\|f_*\|^2}
=o(R_j^{-1}).
\tag{23}
\]

Thus a genuinely widening multiscale ladder is not killed by this result. What fails is only the cheapest fixed-ratio test such as `R,2R`, or any other fixed finite collection whose ratios stay bounded away from zero.

Third, the control remains deliberately non-zeta. `f_*` is an ambient Hilbert-space vector in `V_(M_*)^perp`, not necessarily a confluent actual-zero power sum of `NB-117`. The theorem therefore does not show that one actual zero packet can realize `(5)`. It shows that **nested cutoff coherence alone cannot distinguish actual zero packets from the matched-control class at inverse-section order**.

Fourth, the exact target equations can be replaced by a common nonzero scalar multiple without changing the argument or any retained fraction. Because of nesting, if `Q_(R_*)f=alpha e_(R_*)`, then automatically `Q_(R_j)f=alpha e_(R_j)` for every smaller cutoff. The obstruction is therefore not an artifact of choosing unit target amplitude.

These checks also explain why the dyadic leading-constant deficit must not be overinterpreted. A constant mismatch between independently normalized single-cutoff optima is compatible with complete redundancy of the simultaneous constraint set.

## 5. Prior-art and line consequence

A targeted prior-art audit covered the classical Báez-Duarte finite approximation framework, modern Nyman Gram analysis, and work on continuity of Hilbert-space projections for varying Nyman subspaces. Those sources establish the surrounding approximation and projection setting but do not provide a source-specific theorem that changes the calculation above. No external theorem is load-bearing here: the simultaneous-collapse identity `(11)` is elementary nested-projection geometry, and the quantitative inverse-section law comes entirely from the already-canonical `NB-119`--`NB-120` repair. `SOURCES.md` therefore needs no new dependency.

No novelty is claimed for the abstract fact that nested orthogonal projections compose. The durable Mathia result is the **classification of the proposed cross-cutoff escape**: when applied to the exact natural-cell/Nyman matched-control model, every finite bounded-ratio ladder collapses to its maximal section and preserves inverse-section perfect target capture.

This resolves the ambient test in `CLUE-cross-cutoff-coherence-breaks-inverse-section-repair` against the hoped-for exponent gain. The live source theorem is correspondingly sharper. Cross-cutoff coherence can matter only if it introduces information not reducible to the maximal nested section: a widening ladder whose scale ratios vanish, a non-nested or tail-sensitive compatibility law, or the actual confluent zero-power representation itself. Merely requiring one vector to satisfy the same nested target and Nyman equations at `R` and `2R` is not enough.