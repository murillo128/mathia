# WI-316 — Capped comparison bottoms converge to the global Weil variational floor

**Status:** `EXACT-DERIVED + CLASSICAL-MINMAX + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

**Parent findings:** WI-311, WI-314, WI-315.

WI-315 shows that on the actual nested compact-support Weil domains, the strict comparison count below the fixed threshold `-1/2` is already inertia-complete along any cofinal capped-tail diagonal with cap error tending to zero. There is a sharper quantitative statement at the bottom of the Rayleigh spectrum.

Let `L_j -> infinity`, and suppose the WI-311 source-exact construction gives on

\[
\mathcal D_{L_j}=C_c^\infty((-L_j,L_j);\mathbf C)
\]

an exact decomposition

\[
Q=\widehat{\mathcal D}_j+\widehat{\mathcal T}_j,
\qquad
\left(\frac12-\delta_j\right)I
\preceq\widehat{\mathcal T}_j
\preceq\frac12I,
\qquad
\delta_j\to0.
\tag{1}
\]

Put

\[
E_j:=\frac12I-\widehat{\mathcal T}_j.
\]

Then

\[
0\preceq E_j\preceq\delta_j I,
\qquad
\boxed{\widehat{\mathcal D}_j+\frac12I=Q+E_j.}
\tag{2}
\]

If

\[
\lambda_j
:=
\inf_{0\ne f\in\mathcal D_{L_j}}
\frac{Q[f]}{\|f\|_2^2}
\]

and

\[
\widehat\lambda_j
:=
\inf_{0\ne f\in\mathcal D_{L_j}}
\frac{(\widehat{\mathcal D}_j+\frac12I)[f]}{\|f\|_2^2},
\]

then (2) gives the exact two-sided enclosure

\[
\boxed{
\lambda_j
\le
\widehat\lambda_j
\le
\lambda_j+\delta_j.
}
\tag{3}
\]

Now define the global compact-support variational floor

\[
\lambda_c
:=
\inf_{0\ne f\in C_c^\infty(\mathbf R;\mathbf C)}
\frac{Q[f]}{\|f\|_2^2}
\in[-\infty,\infty).
\tag{4}
\]

The nesting of the physical Weil windows implies, for every cofinal sequence `L_j -> infinity`,

\[
\boxed{\lambda_j\longrightarrow\lambda_c.}
\tag{5}
\]

Combining (3), (5), and `delta_j -> 0` yields

\[
\boxed{\widehat\lambda_j\longrightarrow\lambda_c}
\tag{6}
\]

in the extended-real sense.

Consequently an asymptotically accurate lower bound at the capped comparison threshold is **not a weaker intermediate target**. If for one source-exact cofinal vanishing-cap diagonal one could prove merely

\[
\boxed{
\widehat{\mathcal D}_j
\succeq
-\left(\frac12+\varepsilon_j\right)I,
\qquad
\varepsilon_j\to0,
}
\tag{7}
\]

then (6) would force `lambda_c >= 0`, and Weil's criterion would give RH. Conversely, under RH equation (2) gives the exact stronger bound

\[
\widehat{\mathcal D}_j\succeq-\frac12I
\]

for every `j`. Thus, once the WI-311 cap error itself vanishes, even an `o(1)` loss in the comparison floor is already RH-equivalent.

This sharpens the research boundary left by WI-315. A soft operator argument whose only intended output is `-1/2-o(1)` on a cofinal capped comparison has not isolated a tractable approximation to the RH problem; it has already targeted an equivalent sign theorem. A genuinely intermediate estimate must either retain a nonvanishing error and supply an additional bootstrap that contracts it, control a narrower source/eigenfunction class by information not equivalent to the global floor, or introduce another invariant that can be iterated toward zero defect.

## 1. Exact perturbation enclosure

Equation (2) is the source-exact identity already present in WI-315. For every nonzero `f in D_{L_j}`,

\[
0
\le
\frac{E_j[f]}{\|f\|_2^2}
\le
\delta_j.
\tag{8}
\]

Hence

\[
\frac{Q[f]}{\|f\|_2^2}
\le
\frac{(Q+E_j)[f]}{\|f\|_2^2}
\le
\frac{Q[f]}{\|f\|_2^2}+\delta_j.
\tag{9}
\]

Taking infima over the same domain proves (3). No eigenvalue existence, compact resolvent, commutation, or spectral discreteness is used. The statement is only the variational monotonicity of a quadratic form under a positive bounded perturbation whose norm is at most `delta_j`.

Equivalently,

\[
\boxed{
\widehat\lambda_j-\delta_j
\le
\lambda_j
\le
\widehat\lambda_j.
}
\tag{10}
\]

Thus the capped comparison bottom is a certified upper approximation to the physical window floor, with a deterministic error interval of width exactly at most the cap defect.

For the explicit WI-311 construction,

\[
\delta_j
=
\frac1{4N_j}+\frac{\epsilon_j}{2},
\tag{11}
\]

so the variational approximation can be made arbitrarily accurate at every fixed aperture by increasing the number of smooth carrier pairs and decreasing `epsilon_j`. WI-312 shows that doing so transfers complexity into the continuous archimedean compact sector; (3) shows that this complexity trade is occurring while the comparison bottom itself is converging to the source bottom.

## 2. Cofinal window floors converge to the compact-support floor

The proof of (5) uses only the actual nested Weil domains emphasized in WI-315. Since every `D_{L_j}` is a subset of the global compact-support core,

\[
\lambda_j\ge\lambda_c
\tag{12}
\]

for every `j`.

Suppose first that `lambda_c` is finite. For every `eta>0`, choose one compactly supported nonzero test `f_eta` such that

\[
\frac{Q[f_\eta]}{\|f_\eta\|_2^2}
<\lambda_c+\eta.
\tag{13}
\]

Its support is contained in one fixed interval `(-L_eta,L_eta)`. Since `L_j -> infinity`, the same test belongs to every `D_{L_j}` for all sufficiently large `j`. Therefore

\[
\limsup_{j\to\infty}\lambda_j
\le\lambda_c+\eta.
\tag{14}
\]

Letting `eta -> 0` and using (12) proves (5).

If `lambda_c=-infinity`, then for every real `M` there is a fixed compact test with Rayleigh quotient below `M`; that test is again eventually present in every cofinal window. Hence eventually `lambda_j<M`. Since `M` is arbitrary,

\[
\lambda_j\to-\infty.
\tag{15}
\]

No monotonicity of the numerical sequence `L_j` is required. Cofinality alone is enough because every individual compact witness is eventually contained in every window.

Equation (6) now follows immediately from the squeeze (3).

## 3. Vanishing threshold error is already equivalent to RH

Bombieri's formulation of Weil's criterion gives

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
Q[f]\ge0
\quad\text{for every }f\in C_c^\infty(\mathbf R;\mathbf C),
\tag{16}
\]

and therefore

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\lambda_c\ge0.
}
\tag{17}
\]

By (6), every WI-311 cofinal vanishing-cap diagonal satisfies

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\liminf_{j\to\infty}\widehat\lambda_j\ge0.
}
\tag{18}
\]

Now assume only the approximate comparison floor (7). It says

\[
\widehat\lambda_j\ge-\varepsilon_j.
\tag{19}
\]

Since `epsilon_j -> 0`, (18) proves RH. One can also see the implication without naming the variational limits: from (1) and (7),

\[
Q
=
\widehat{\mathcal D}_j+\widehat{\mathcal T}_j
\succeq
-(\varepsilon_j+\delta_j)I
\tag{20}
\]

on `D_{L_j}`. Every fixed compactly supported test eventually belongs to all these domains, so sending `j -> infinity` gives `Q[f]>=0` for that test. This is exactly Weil's criterion.

The converse is stronger. If RH holds, then `Q>=0` on every compact window and `E_j>=0`, so (2) gives

\[
\widehat{\mathcal D}_j+\frac12I=Q+E_j\succeq0
\tag{21}
\]

at every aperture, with no asymptotic loss.

If RH fails, choose any fixed compact witness with

\[
Q[f]=-\eta\|f\|_2^2,
\qquad\eta>0.
\tag{22}
\]

For all sufficiently large `j`, the witness lies in `D_{L_j}` and `delta_j<eta/2`. Then

\[
\widehat\lambda_j
\le
\frac{(Q+E_j)[f]}{\|f\|_2^2}
\le
-\eta+\delta_j
<-rac\eta2.
\tag{23}
\]

So failure of RH cannot hide behind a comparison bottom that merely drifts to `0^-`: one old compact witness forces a fixed negative asymptotic gap along every cofinal vanishing-cap diagonal.

## 4. What this closes, and what remains genuinely intermediate

WI-315 closed a limit-order loophole for **negative index**: exact exclusion below `-1/2` on one cofinal vanishing-cap diagonal is sufficient for RH. The present result closes a nearby quantitative loophole: replacing that exact exclusion by a vanishing additive error does not weaken the target. Any theorem of the form

\[
\widehat{\mathcal D}_j
\succeq
-\left(\frac12+o(1)\right)I
\tag{24}
\]

is already an RH theorem when combined with the source-exact cap identity.

This is a useful no-go for several natural continuations of WI-311--WI-312. For example, trying to show that the difficult compact/source correction has operator norm `o(1)` relative to the `-1/2` threshold would not produce a merely approximate positivity result: if it is strong enough to imply (24) cofinally, it has solved the sign problem itself. Likewise, an aperture-dependent spectral estimate that approaches the threshold with no new contracting mechanism should be evaluated as an RH-equivalent target rather than as an incremental coercivity theorem.

A fixed nonvanishing error is different. A bound

\[
\widehat{\mathcal D}_j
\succeq
-\left(\frac12+c\right)I
\qquad(c>0\text{ fixed})
\tag{25}
\]

only yields `Q >= -c I` on the compact core through this argument. Nothing here promotes such a fixed-error semiboundedness statement to RH. It can therefore be a legitimate intermediate theorem if some independent source-specific mechanism subsequently contracts the defect `c`.

The research target should consequently be split cleanly. Either obtain genuinely new arithmetic/source structure that forces the exact sign, or prove a **defect-contraction rule** that takes a nonzero comparison error to a strictly smaller one and can be iterated. Merely replacing exact `-1/2` control by an unspecified `o(1)` loss does not create an easier frontier.

## 5. Prior art and novelty boundary

The ingredients are classical or already established locally:

- Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I* (2000), proves that Weil's quadratic functional is positive semidefinite exactly under RH and studies its restrictions to fixed support intervals; the paper also proves attainment of the fixed-window minimum in the relevant `L^2` unit ball.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026), develops finite-interval self-adjoint realizations of the same localized Weil problem and provides modern operator-theoretic context for window ground-state quantities.
- Marcus Chuk, *Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*, arXiv:2608.24827 (2026), explicitly studies the fixed-window profile `lambda^*(L)=inf Q(f)/||f||_2^2`. Its computational positivity claims and asymptotic profile analysis are independent of the capped-tail diagonal deduction here.
- Monotonicity of Rayleigh infima under bounded self-adjoint form perturbations is elementary min--max theory; no novelty is claimed for (3) in isolation.

A targeted prior-art audit around compact-window Weil minima, increasing support domains, bounded perturbation/min--max convergence, and the recent clipped/capped localization literature found no source stating the combined implication (6)--(7): that the WI-311 source-exact capped comparison bottom converges to the global compact-support Weil floor and hence that a cofinal `-1/2-o(1)` lower bound is already RH-equivalent. Search absence is not a priority claim.

The line-local contribution is therefore the **research boundary**, not a new functional-analysis theorem: once WI-311's cap approximation and WI-315's nested-domain geometry are combined, vanishing threshold error is already the full sign problem.

### Validation boundary

All statements are variational on the common smooth compact-support core. No assertion is made about norm-resolvent convergence of completed global operators, convergence of eigenvectors, compact resolvent, or the existence of a global self-adjoint operator with bottom `lambda_c`. None is required for (3)--(23).

The result does not prove RH, does not validate Liu's unreplayed `17/16` computational certificate, and does not improve the current simple-zero proportion. It is a decisive negative result for a proposed approximation strategy: **an `o(1)` lower-floor error on a cofinal capped comparison is not an intermediate result short of RH.**

## Research consequence

The capped-tail branch should no longer target an asymptotic estimate of the bare form `Dhat_j >= -(1/2+o(1)) I` unless the argument plausibly contains the missing RH-level source information. A more informative next theorem would keep a fixed quantitative defect and derive a source-valid contraction/bootstrapping map for that defect, or isolate a restricted class of comparison modes on which arithmetic structure supplies a strict improvement that can be propagated. This is precisely the kind of defect-to-zero mechanism demanded by the canonical research mandate.