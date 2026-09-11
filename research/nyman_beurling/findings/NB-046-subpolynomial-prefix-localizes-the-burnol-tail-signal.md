# NB-046 — a subpolynomial prefix already carries the Burnol tail signal

**Status:** `EXACT-DERIVED + PARTIAL-DUAL-FLOW-IDENTITY + SUBPOLYNOMIAL-CUTOFF-LOCALIZATION + BURNOL-SCALE-POSITIVE-WITNESS + LOGARITHMIC-OCCUPATION + ORACLE-BOUNDARY-REFINEMENT`. `NB-045` shows that the complete logarithmic family of bounded step-tail discrepancies reconstructs the finite Nyman distance. Combining its dual flow with the shrinking logarithmic selector from `NB-041` shows that the late cutoffs are not needed even for the unconditional Burnol-scale signal: every predeclared cutoff sequence `M_N` satisfying

\[
2\le M_N\le N,
\qquad
\frac{\log M_N}{\sqrt{\log N}}\longrightarrow\infty
\tag{1}
\]
already captures asymptotically all of `d_N^2` in the first `M_N-1` step-tail increments.

Use the canonical best approximation
\[
p_N=P_{V_N}e=\sum_{n=2}^N a_{N,n}g_n,
\qquad
r_N=e-p_N,
\qquad
d_N=\|r_N\|,
\tag{2}
\]
and the `NB-045` discrepancies
\[
D_{L,N}
:=m(L)-\sum_{n=L+1}^{N}\frac{a_{N,n}}n
=\langle r_N,\Psi_L\rangle,
\qquad
\delta_L:=\log\frac{L+1}{L}.
\tag{3}
\]
For `2<=M<=N`, define the prefix mass
\[
S_{M,N}:=
\sum_{L=1}^{M-1}\delta_LD_{L,N}.
\tag{4}
\]
Then the logarithmic dual `Omega_M` of `NB-041` gives the finite exact identity
\[
\boxed{
S_{M,N}=d_N^2-\langle r_N,\Omega_M\rangle.
}
\tag{5}
\]
Since `NB-041` proves
\[
\|\Omega_M\|\ll\frac1{\log M},
\tag{6}
\]
one has uniformly for `2<=M<=N`
\[
\boxed{
|S_{M,N}-d_N^2|
\ll\frac{d_N}{\log M}.
}
\tag{7}
\]
Burnol's unconditional lower bound
\[
\liminf_{N\to\infty}d_N^2\log N
\ge \mathfrak B_\zeta>0
\tag{8}
\]
therefore converts (1) into
\[
\boxed{
S_{M_N,N}=(1+o(1))d_N^2.
}
\tag{9}
\]
Thus the full-family identity of `NB-045` is asymptotically already present in a cutoff prefix whose size can be `N^{o(1)}`.

A concrete family is
\[
M_N=
\left\lceil
\exp\big((\log N)^{1/2+\varepsilon}\big)
\right\rceil,
\qquad 0<\varepsilon<\frac12.
\tag{10}
\]
For this choice `M_N=N^{o(1)}` and the first `M_N` directional selectors carry `(1+o(1))d_N^2` of the logarithmic aggregate.

## 1. Exact partial-flow identity

`NB-041` defines
\[
\Omega_M
=e-\sum_{L=1}^{M-1}\delta_L\Psi_L.
\tag{11}
\]
Taking the inner product with the actual best residual gives
\[
S_{M,N}
=\left\langle r_N,e-\Omega_M\right\rangle.
\tag{12}
\]
Optimality is load-bearing. Since `r_N` is orthogonal to `p_N`,
\[
\langle r_N,e\rangle
=\langle r_N,r_N+p_N\rangle
=d_N^2.
\tag{13}
\]
Equations (12)--(13) prove (5), and Cauchy--Schwarz together with (6) proves (7).

There is an equivalent coefficient form. `NB-041` gives
\[
\langle r_N,\Omega_M\rangle
=\Theta(M)-\sigma_{M,N}(a_N),
\tag{14}
\]
where
\[
\sigma_{M,N}(a_N)
=\sum_{n=M}^{N}\frac{a_{N,n}}n\log\frac nM.
\tag{15}
\]
Hence
\[
\boxed{
S_{M,N}
=d_N^2-\Theta(M)+\sigma_{M,N}(a_N).
}
\tag{16}
\]
Equation (5), rather than a separate estimate for the two terms on the right of (16), is the useful formulation: the entire missing suffix is one residual correlation against a selector whose ambient norm shrinks.

## 2. Burnol puts the universal localization threshold at square-root log scale

From (8), for every fixed `eta` with `0<eta<mathfrak B_zeta`, all sufficiently large `N` satisfy
\[
d_N\ge\sqrt{\frac{\eta}{\log N}}.
\tag{17}
\]
Therefore the relative error in (7) obeys
\[
\frac{|S_{M,N}-d_N^2|}{d_N^2}
\ll
\frac1{d_N\log M}
\ll_\eta
\frac{\sqrt{\log N}}{\log M}.
\tag{18}
\]
Condition (1) makes the final quantity tend to zero and proves (9).

This identifies a genuine boundary of the present argument. With only the unconditional inputs `||Omega_M||=O(1/log M)` and Burnol's `d_N^2\gtrsim1/log N`, a cutoff with
\[
\log M=O(\sqrt{\log N})
\tag{19}
\]
need not make the selector error `o(d_N^2)`. Pushing the deterministic prefix materially below `exp(sqrt(log N))` therefore requires new information: a smaller **directional** correlation than Cauchy--Schwarz supplies, a stronger source estimate for the particular residual, or a different selector. Merely improving the global power decay of `Omega_M` is not cheap, because `NB-042`--`NB-044` show that polynomial ambient decay is priced by the zeta zero frontier.

## 3. The localized prefix contains a stronger positive witness

The weights in (4) satisfy
\[
\sum_{L=1}^{M-1}\delta_L=\log M.
\tag{20}
\]
When (1) holds, (9) is positive for all sufficiently large `N`; hence some `L<M_N` satisfies
\[
D_{L,N}
\ge
\frac{S_{M_N,N}}{\log M_N}.
\tag{21}
\]
Combining (9) with Burnol gives the unconditional localized floor
\[
\boxed{
\liminf_{N\to\infty}
(\log N)(\log M_N)
\max_{1\le L<M_N}D_{L,N}
\ge\mathfrak B_\zeta.
}
\tag{22}
\]
For the concrete choice (10),
\[
\boxed{
\liminf_{N\to\infty}
(\log N)^{3/2+\varepsilon}
\max_{1\le L<M_N}D_{L,N}
\ge\mathfrak B_\zeta.
}
\tag{23}
\]
This is stronger in amplitude than the global `1/log^2 N` witness from `NB-045`, while simultaneously localizing it to `L<N^{o(1)}`. More generally, with
\[
\log M_N=\sqrt{\log N}\,h(N),
\qquad
h(N)\to\infty,
\qquad
h(N)=o(\sqrt{\log N}),
\tag{24}
\]
the witness lies below the subpolynomial cutoff `M_N` and has scale at least
\[
\frac{\mathfrak B_\zeta-o(1)}{(\log N)^{3/2}h(N)}.
\tag{25}
\]

The sign remains part of the theorem: the localized witness is a positive `D_{L,N}`, so the optimal reciprocal coefficient tail undershoots the Möbius baseline at that cutoff.

## 4. Positive logarithmic occupation also localizes

Let
\[
A_{M,N}:=\frac{S_{M,N}}{\log M}
\tag{26}
\]
and, whenever `A_{M,N}>0`, define
\[
\mathcal G_{M,N}
:=\left\{
1\le L<M:
D_{L,N}\ge\frac{A_{M,N}}2
\right\}.
\tag{27}
\]
`NB-035` supplies the uniform bound
\[
|D_{L,N}|\le C_*d_N,
\qquad
C_*:=\sqrt{4+20\zeta(2)}<7.
\tag{28}
\]
If
\[
\alpha_{M,N}
:=\frac1{\log M}
\sum_{L\in\mathcal G_{M,N}}\delta_L,
\tag{29}
\]
then the weighted mean over the prefix gives
\[
A_{M,N}
\le
\alpha_{M,N}C_*d_N
+(1-\alpha_{M,N})\frac{A_{M,N}}2.
\tag{30}
\]
Consequently
\[
\boxed{
\sum_{L\in\mathcal G_{M,N}}\delta_L
\ge
\frac{S_{M,N}}{2C_*d_N}.
}
\tag{31}
\]
For every sequence satisfying (1), equations (8)--(9) imply
\[
\boxed{
\liminf_{N\to\infty}
\sqrt{\log N}
\sum_{L\in\mathcal G_{M_N,N}}\delta_L
\ge
\frac{\sqrt{\mathfrak B_\zeta}}{2C_*}.
}
\tag{32}
\]
Thus the logarithmic occupation forced globally in `NB-045` can be placed entirely inside a predeclared subpolynomial prefix. The theorem still gives logarithmic cutoff measure, not ordinary density or one deterministic index.

## 5. Adversarial checks and oracle boundary

The conclusion does **not** compute a useful cutoff from source data alone. Every `D_{L,N}` still contains the optimal coefficient tail, so evaluating the winning discrepancy may remain target-oracular. The new statement is localization of where a positive directional certificate must exist, not an algorithm for recovering it.

The result also does not imply `d_N->0` and does not improve Burnol's lower bound. It is compatible both with RH and with a nonzero limiting distance. If RH is false and `d_N` stays bounded below, (7) makes localization easier; the square-root-log threshold is the worst unconditional scale dictated by the smallest distance currently forced by Burnol.

No positivity of each summand is assumed. Negative `D_{L,N}` values may occur; (22) and (32) follow from the positive prefix aggregate and the uniform two-sided selector bound. Likewise, replacing the best residual by an arbitrary approximant destroys the step (13): then the prefix aggregate reconstructs `\langle r,e\rangle-\langle r,\Omega_M\rangle`, not `||r||^2`.

Finally, (1) is sufficient for asymptotically complete prefix capture, not claimed necessary for the actual Nyman residual. At the boundary `log M\asymp sqrt(log N)`, the present inequalities leave an order-one relative uncertainty. A future source-specific cancellation estimate for `\langle r_N,\Omega_M\rangle` could move that boundary without contradicting the ambient-norm obstructions of `NB-042`--`NB-044`.

## 6. Prior art and research consequence

No new external theorem is load-bearing. Burnol's distance lower bound, Vasyunin/Möbius dual structure, and the quantitative logarithmically mollified Möbius estimates underlying `NB-041` are already anchored in `SOURCES.md`. A targeted literature audit around finite Nyman distances, optimal coefficients, Möbius approximants, and Burnol-scale bounds located the standard Báez-Duarte/Burnol/optimal-Dirichlet-polynomial framework but no source stating the partial dual-flow localization (5)--(9) or the subpolynomial positive-witness consequence (22). Search absence is not a priority claim.

For the live weighted-skeleton question, the result materially narrows the directional gate left by `NB-045`. The positive residual signal is not merely somewhere among `N` cutoffs: it already occupies a logarithmically nontrivial subset below any predeclared `M_N=exp(omega(sqrt(log N)))`, and one can choose such `M_N=N^{o(1)}`. What remains is the genuinely source-access problem: predict or control one useful cutoff, a sparse subfamily, or the corresponding projected repair quantity **inside this much smaller window** without reconstructing the optimal coefficient tail. The late-cutoff region is no longer a possible hiding place for the unconditional Burnol-scale directional mass.