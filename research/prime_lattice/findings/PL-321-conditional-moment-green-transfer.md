# PL-321 — Conditional endpoint moments already suffice for the moving Green transfer

**Evidence:** `EXACT-DERIVED + POSITIVE-TRANSFER + ANALYTIC-GATE-CLOSURE`

**Status:** `CONDITIONAL-MOMENT-SUFFICES + ABSOLUTE-L1-NOT-NEEDED + PL320-REDUCES-TO-SINGULAR-REMAINDER-TRACE`

## Precise claim

`PL-314` proves the rank-one corner transfer under the sufficient assumptions

\[
m\in L^1(0,\infty),
\qquad
Qm(Q)\to0,
\]

while `PL-320` shows that convergence of the full logarithmic source trace and singular translation remainder naturally gives only

\[
Qm(Q)\to0
\quad\text{and}\quad
\int_0^R m(Q)\,dQ\to M
\]

with the residual moment possibly only conditionally convergent. The absolute `L^1` gap is not genuine: the exact pre-diagonal Green kernel has a bounded-variation Abel weight, so conditional convergence is enough.

Fix `r>0`, put

\[
x_s(r)=1-2e^{-r/s},
\]

and define, exactly as in `PL-314`,

\[
\mathcal A_s[m](r)
:=\frac1s\int_{-1}^{1}G_s(x_s(r),y)\widetilde m(y)\,dy,
\qquad
\widetilde m(y)=m\!\left(-\log\frac{1-y}{2}\right).
\tag{PL321-1}
\]

Assume only

\[
m\in L^1_{\rm loc}(0,\infty),
\qquad
\boxed{\lim_{R\to\infty}\int_0^R m(Q)\,dQ=M\in\mathbb C,}
\qquad
\boxed{Qm(Q)\to0.}
\tag{PL321-2}
\]

Then

\[
\boxed{
\mathcal A_s[m](r)
\longrightarrow
 e^{-r}M
\qquad(s\downarrow0).
}
\tag{PL321-3}
\]

No absolute integrability of `m` is required. In particular, the smooth control from `PL-320`,

\[
m_*(Q)=\frac{\sin Q}{Q\log Q}
\]

after a harmless cutoff, satisfies the theorem despite `m_*\notin L^1`.

Consequently the last absolute-integrability gate left by `PL-320` is removed. If the actual completed-Weil tail satisfies the single local condition

\[
H_{Q_0}g(Q)\to H_\infty,
\]

then `PL-320` already produces a coefficient `C`, a residual `m=g-CQ^{-1/2}` with `Qm(Q)->0`, and a convergent improper residual moment. After splitting off the compact endpoint complement, (PL321-3) applies. The remaining endpoint matching problem is therefore the convergence of the singular remainder itself, not absolute `L^1(dQ)` control.

## 1. Exact factorization before the moving diagonal

Write the stretched Green measure from `PL-310` as

\[
d\mu_{s,r}(q)=k_s(r,q)\,dq,
\]

so that

\[
\mathcal A_s[m](r)
=\frac1s\int_0^\infty m(q/s)\,d\mu_{s,r}(q)
=\int_0^\infty k_s(r,sQ)m(Q)\,dQ.
\tag{PL321-4}
\]

Split at

\[
B_s:=\frac{r}{2s}.
\tag{PL321-5}
\]

For `0<q<r`, `PL-314` records Bucur's exact one-dimensional Green formula in the variables

\[
t=e^{-r/s},
\qquad
u=e^{-q/s},
\]

as

\[
k_s(r,q)
=\frac{u(u-t)^{2s-1}}{s\Gamma(s)^2}
\int_0^R\frac{z^{s-1}}{\sqrt{1+z}}\,dz,
\]

where

\[
R=\frac{4tu(1-t)(1-u)}{(u-t)^2}.
\tag{PL321-6}
\]

Define

\[
\vartheta_s(R)
:=sR^{-s}\int_0^R\frac{z^{s-1}}{\sqrt{1+z}}\,dz,
\]

with the continuous value `1` at `R=0`. Since the integrand factor `(1+z)^{-1/2}` lies between `(1+R)^{-1/2}` and `1`, one has the exact bounds

\[
(1+R)^{-1/2}\le\vartheta_s(R)\le1.
\tag{PL321-7}
\]

Now set `q=sQ`, so `u=e^{-Q}`. Substituting `R^s` from (PL321-6), using `s^2\Gamma(s)^2=\Gamma(1+s)^2`, and using `t^s=e^{-r}`, gives the exact factorization

\[
\boxed{
k_s(r,sQ)=a_s(r)\,w_s(Q)\,E_s(r,Q),}
\tag{PL321-8}
\]

where

\[
a_s(r)=e^{-r}\frac{(1-e^{-r/s})^s}{\Gamma(1+s)^2},
\tag{PL321-9}
\]

\[
\boxed{
w_s(Q)=\bigl(4e^{-Q}(1-e^{-Q})\bigr)^s,}
\tag{PL321-10}
\]

and

\[
E_s(r,Q)=\frac{1}{1-t/u}\,\vartheta_s(R).
\tag{PL321-11}
\]

The scalar satisfies

\[
a_s(r)\to e^{-r}.
\tag{PL321-12}
\]

The key point is that `w_s`, not the residual `m`, carries all the relevant pre-diagonal variation. It obeys

\[
0\le w_s(Q)\le1,
\qquad
w_s(Q)\to1\quad(Q>0\text{ fixed}),
\tag{PL321-13}
\]

and is increasing on `(0,\log2)` and decreasing on `(\log2,\infty)`, with maximum `w_s(\log2)=1`. Thus its total variation is at most `2`, uniformly in `s`; on every tail `[A,\infty)` with `A>\log2` it is simply monotone decreasing.

For `0<Q\le B_s`, equivalently `0<q\le r/2`,

\[
\varepsilon:=\frac tu
=e^{-(r-q)/s}
\le e^{-r/(2s)}=:\eta_s.
\]

Equation (PL321-6) gives

\[
0\le R\le\frac{4\eta_s}{(1-\eta_s)^2}.
\]

Combining this with (PL321-7) yields

\[
\boxed{
\sup_{0<Q\le B_s}|E_s(r,Q)-1|
=O_r(\eta_s).
}
\tag{PL321-14}
\]

Hence, before the moving diagonal, the exact Green kernel is an exponentially accurate perturbation of the explicit bounded-variation Abel weight `a_s(r)w_s(Q)`.

## 2. Conditional moments pass through the Abel weight

Let

\[
T(A):=\int_A^\infty m(Q)\,dQ,
\]

which is well-defined by (PL321-2). The Cauchy criterion for the improper integral gives

\[
\sup_{Q\ge A}|T(Q)|\longrightarrow0
\qquad(A\to\infty).
\tag{PL321-15}
\]

Fix `A>\log2`. On `[A,B_s]`, `w_s` is decreasing. Since `m=-T'` almost everywhere on finite intervals, integration by parts gives

\[
\int_A^{B_s}w_s(Q)m(Q)\,dQ
=
w_s(A)T(A)-w_s(B_s)T(B_s)
+\int_A^{B_s}T(Q)\,dw_s(Q).
\tag{PL321-16}
\]

Therefore

\[
\left|\int_A^{B_s}w_s m\right|
\le3\sup_{Q\ge A}|T(Q)|,
\tag{PL321-17}
\]

uniformly for all sufficiently small `s` with `B_s>A`. On the fixed interval `(0,A)`, `w_s(Q)->1` for almost every `Q` and `|w_s|\le1`, so local dominated convergence gives

\[
\int_0^A w_s(Q)m(Q)\,dQ
\to\int_0^A m(Q)\,dQ.
\tag{PL321-18}
\]

Letting first `s->0` and then `A->infinity`, (PL321-15)--(PL321-18) prove

\[
\boxed{
\int_0^{B_s}w_s(Q)m(Q)\,dQ\longrightarrow M.
}
\tag{PL321-19}
\]

This is the only Abelian step. It is the standard Dirichlet/Stieltjes mechanism for a conditionally convergent improper integral; the line-specific content is that the exact fractional Green kernel factorizes into precisely such a uniformly bounded-variation weight.

## 3. The exact-kernel error is exponentially negligible

It remains to replace `w_s` by the exact pre-diagonal kernel. From `Qm(Q)->0`, there are `A_0` and `C<infinity` such that

\[
|m(Q)|\le\frac{C}{Q}
\qquad(Q\ge A_0).
\tag{PL321-20}
\]

Consequently

\[
\int_0^{B_s}|m(Q)|\,dQ
=O_m\!\left(1+\log\frac1s\right).
\tag{PL321-21}
\]

Equations (PL321-8), (PL321-14), and `0\le w_s\le1` then imply

\[
\begin{aligned}
&\left|
\int_0^{B_s}k_s(r,sQ)m(Q)\,dQ
-a_s(r)\int_0^{B_s}w_s(Q)m(Q)\,dQ
\right|\\
&\hspace{25mm}\le
C_r e^{-r/(2s)}
\int_0^{B_s}|m(Q)|\,dQ
=o(1).
\end{aligned}
\tag{PL321-22}
\]

Together with (PL321-12) and (PL321-19), the entire pre-diagonal part converges to

\[
e^{-r}M.
\tag{PL321-23}
\]

The role of `Qm(Q)->0` here is mild: it only supplies logarithmic growth of the finite absolute integral needed to absorb the exponentially small kernel-factorization error. The main pre-diagonal passage uses the conditional moment itself.

## 4. The moving and post-diagonal region is still killed by `Qm(Q)->0`

Define

\[
\omega(R):=\sup_{Q\ge R}Q|m(Q)|.
\]

Then `\omega(R)->0`. For `q\ge r/2`, so that `Q=q/s\ge B_s`,

\[
\frac1s|m(q/s)|
\le\frac{\omega(B_s)}{q}
\le\frac{2}{r}\omega(B_s).
\]

Since the total Green mass is uniformly bounded by the exact torsion identity already used in `PL-310` and `PL-314`,

\[
\mu_{s,r}((0,\infty))=O_r(1),
\]

we obtain

\[
\boxed{
\left|
\frac1s\int_{q\ge r/2}m(q/s)\,d\mu_{s,r}(q)
\right|
\le C_r\omega(B_s)\to0.
}
\tag{PL321-24]
\]

Equations (PL321-23) and (PL321-24) prove (PL321-3).

## 5. Consequence for the completed-Weil boundary program

The implication chain from `PL-319` and `PL-320` now closes without an absolute residual estimate. For the actual completed-Weil endpoint, the eigen-equation already supplies a finite source trace, and the logarithmic-Laplacian boundary theory supplies `g(Q)=O(Q^{-1/2})`. If the remaining local singular remainder has a limit,

\[
H_{Q_0}g(Q)\to H_\infty,
\]

then `PL-320` gives

\[
g(Q)=CQ^{-1/2}+m(Q),
\qquad
Qm(Q)\to0,
\qquad
\int_{Q_0}^R m(Q)\,dQ\to M.
\tag{PL321-25}
\]

A compactly supported complement is handled by `PL-313`; the tail residual satisfies the present theorem. Hence the rank-one corner/source balance is stable under exactly the information produced by the Volterra source trace. The oscillatory example `sin Q/(Q log Q)` from `PL-320` is no longer an obstruction: its conditional moment is sufficient.

The analytic frontier is therefore reduced to

\[
\boxed{H_{Q_0}g(Q)\text{ has a finite endpoint limit}.}
\tag{PL321-26}
\]

Once this is established for the actual isolated completed-Weil branch, the endpoint transfer part of the current matching chain has no separate absolute-`L^1` gate. This still does not determine the sign of the resulting scalar or prove an arithmetic first-crossing theorem; those remain separate rational-prime-specific tasks.

## Prior-art and novelty audit

The bounded-variation integration-by-parts argument in Section 2 is classical Abel/Dirichlet analysis and is not claimed as new. Bucur's interval Green formula is likewise classical and is already ledgered as source `102`. A targeted audit around Abelian theorems for conditionally convergent improper integrals, bounded-variation/Stieltjes kernels, small-order fractional Green kernels, and boundary-layer limits recovered the standard Dirichlet/Stieltjes mechanism and established fractional Green formulas, but no theorem directly covering the present `Q=q/s` moving Green family with its separate diagonal atom. Search absence is not used as evidence of broad novelty.

The durable line-local result is narrower and exact: **the absolute `L^1(dQ)` assumption in `PL-314` is not load-bearing.** The exact pre-diagonal Green factorization produces a canonical Abel weight of uniformly bounded variation, while the already-required condition `Qm(Q)->0` controls both the exponentially small factorization error and the moving/post-diagonal Green mass. This is precisely the missing bridge identified in `PL-320`.

## Adversarial controls and limits

- **Conditional convergence alone is not enough.** The pointwise law `Qm(Q)->0` is still used to suppress the moving diagonal and post-diagonal region. Sparse `Theta(1/Q)` bumps of the type in `PL-314` remain excluded for exactly the same reason as before.
- **No regularity of `m` beyond local integrability is hidden in the Abel step.** The bounded variation belongs to the explicit kernel weight `w_s`; the residual itself need not be monotone, BV, Sobolev, or absolutely integrable.
- **The split stays a fixed distance from the diagonal in stretched coordinates.** The exact approximation (PL321-14) is used only for `q<=r/2`. No shrinking-neighborhood control of the Green atom is assumed.
- **The result is pointwise in the outer coordinate.** It is proved for each fixed `r>0`; no uniform claim as `r->0`, `r->infinity`, or across an aperture activation is made.
- **The theorem is universal analytic geometry, not arithmetic rigidity.** It closes an endpoint-transfer gate but supplies no sign, positivity, zero-localization, or rational-prime specificity by itself.
- **No analytic continuation is involved.** The argument stays entirely in the real-variable fractional/logarithmic Green representation already justified in `PL-310`--`PL-320`.

## Verdict

**Exact analytic gate closure.** A conditionally convergent endpoint moment plus the already-required moving-tail law `Qm(Q)->0` is sufficient for the full rank-one Green transfer. The absolute residual integrability left open in `PL-320` is unnecessary. For the completed-Weil branch, convergence of the singular translation remainder now simultaneously generates the leading `Q^{-1/2}` coefficient, the moving-tail anti-concentration, the conditional residual moment, and—by the present theorem—the required Green transfer. The downstream arithmetic sign/first-crossing problem remains untouched.

## Sources

- Source `102` in `research/prime_lattice/SOURCES.md`: Claudia Bucur, “Some observations on the Green function for the ball in the fractional Laplace framework,” *Communications on Pure and Applied Analysis* **15**(2) (2016), 657–699. Supplies the exact interval Green kernel used in (PL321-6).
- `PL-310`: stretched Green measure, diagonal atom, and exact total-mass control.
- `PL-313`: compact-support rank-one corner transfer.
- `PL-314`: previous sufficient theorem with absolute `L^1(dQ)` and the sparse-diagonal counterexample.
- `PL-319`: exact logarithmic endpoint source identity and source-trace convergence for the completed-Weil state.
- `PL-320`: full-tail Volterra reduction giving `Qm(Q)->0` and a convergent improper residual moment from convergence of the singular remainder trace.