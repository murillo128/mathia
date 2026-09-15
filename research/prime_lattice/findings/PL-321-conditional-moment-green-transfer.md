# PL-321 — Conditional endpoint moments already suffice for the moving Green transfer

**Evidence:** `EXACT-DERIVED + POSITIVE-TRANSFER + ANALYTIC-GATE-CLOSURE`

**Status:** `CONDITIONAL-MOMENT-SUFFICES + ABSOLUTE-L1-NOT-NEEDED + PL320-REDUCES-TO-SINGULAR-REMAINDER-TRACE`

## Precise claim

`PL-314` proves the rank-one corner transfer under the sufficient assumptions `m in L^1(dQ)` and `Qm(Q)->0`. `PL-320` naturally produces the second condition together with only a conditionally convergent residual moment. The absolute `L^1` gap is not genuine.

Fix `r>0`, put

\[
x_s(r)=1-2e^{-r/s},
\]

and define, as in `PL-314`,

\[
\mathcal A_s[m](r)
:=\frac1s\int_{-1}^{1}G_s(x_s(r),y)\widetilde m(y)\,dy,
\qquad
\widetilde m(y)=m\!\left(-\log\frac{1-y}{2}\right).
\tag{PL321-1}
\]

Assume

\[
m\in L^1_{\rm loc}(0,\infty),
\qquad
\lim_{R\to\infty}\int_0^R m(Q)\,dQ=M\in\mathbb C,
\qquad
Qm(Q)\to0.
\tag{PL321-2}
\]

Then

\[
\boxed{
\mathcal A_s[m](r)\longrightarrow e^{-r}M
\qquad(s\downarrow0).
}
\tag{PL321-3}
\]

No absolute integrability is required. In particular, after a harmless cutoff, the `PL-320` control `m_*(Q)=\sin Q/(Q\log Q)` satisfies the theorem although `m_*` is not in `L^1(dQ)`.

## 1. Exact pre-diagonal Green factorization

Write the stretched Green measure from `PL-310` as

\[
d\mu_{s,r}(q)=k_s(r,q)\,dq,
\]

so

\[
\mathcal A_s[m](r)
=\frac1s\int_0^\infty m(q/s)\,d\mu_{s,r}(q)
=\int_0^\infty k_s(r,sQ)m(Q)\,dQ.
\tag{PL321-4}
\]

Split at `B_s=r/(2s)`. For `0<q<r`, set

\[
t=e^{-r/s},
\qquad
u=e^{-q/s}.
\]

Bucur's exact interval Green formula, in the form already recorded in `PL-314`, is

\[
k_s(r,q)
=\frac{u(u-t)^{2s-1}}{s\Gamma(s)^2}
\int_0^R\frac{z^{s-1}}{\sqrt{1+z}}\,dz,
\qquad
R=\frac{4tu(1-t)(1-u)}{(u-t)^2}.
\tag{PL321-5}
\]

For `R>=0` define

\[
\vartheta_s(R)
:=sR^{-s}\int_0^R\frac{z^{s-1}}{\sqrt{1+z}}\,dz,
\]

with continuous value `1` at `R=0`. Then

\[
(1+R)^{-1/2}\le\vartheta_s(R)\le1.
\tag{PL321-6}
\]

Putting `q=sQ`, hence `u=e^{-Q}`, and using `s^2\Gamma(s)^2=\Gamma(1+s)^2` gives the exact identity

\[
\boxed{
k_s(r,sQ)=a_s(r)w_s(Q)E_s(r,Q),}
\tag{PL321-7}
\]

where

\[
a_s(r)=e^{-r}\frac{(1-e^{-r/s})^s}{\Gamma(1+s)^2}\to e^{-r},
\tag{PL321-8}
\]

\[
\boxed{w_s(Q)=\bigl(4e^{-Q}(1-e^{-Q})\bigr)^s,}
\tag{PL321-9}
\]

and

\[
E_s(r,Q)=\frac{1}{1-t/u}\vartheta_s(R).
\tag{PL321-10}
\]

The Abel weight satisfies `0<=w_s<=1`, converges pointwise to `1` for every fixed `Q>0`, is increasing up to `Q=log 2`, and is decreasing afterwards, with maximum exactly `1`. Its total variation is therefore at most `2`, uniformly in `s`.

For `0<Q<=B_s`, equivalently `0<q<=r/2`,

\[
\varepsilon:=t/u=e^{-(r-q)/s}\le e^{-r/(2s)}=:\eta_s,
\]

and

\[
0\le R\le\frac{4\eta_s}{(1-\eta_s)^2}.
\]

Using (PL321-6),

\[
\boxed{
\sup_{0<Q\le B_s}|E_s(r,Q)-1|=O_r(e^{-r/(2s)}).
}
\tag{PL321-11}
\]

Thus a fixed stretched distance before the moving pole, the exact kernel is an exponentially accurate perturbation of the explicit bounded-variation weight `a_s(r)w_s(Q)`.

## 2. Conditional convergence passes through the Abel weight

Let

\[
T(A):=\int_A^\infty m(Q)\,dQ.
\]

The improper convergence in (PL321-2) implies

\[
\sup_{Q\ge A}|T(Q)|\to0
\qquad(A\to\infty).
\tag{PL321-12}
\]

Fix `A>log 2`. On `[A,B_s]`, `w_s` is decreasing. Since `m=-T'` almost everywhere on finite intervals, Stieltjes integration by parts gives

\[
\int_A^{B_s}w_s(Q)m(Q)\,dQ
=w_s(A)T(A)-w_s(B_s)T(B_s)
+\int_A^{B_s}T(Q)\,dw_s(Q).
\]

Hence

\[
\left|\int_A^{B_s}w_s m\right|
\le3\sup_{Q\ge A}|T(Q)|.
\tag{PL321-13}
\]

On every fixed `(0,A)`, local dominated convergence gives `\int_0^A w_s m -> \int_0^A m`. Letting first `s->0` and then `A->infinity` yields

\[
\boxed{
\int_0^{B_s}w_s(Q)m(Q)\,dQ\to M.
}
\tag{PL321-14}
\]

This is a standard Abel/Dirichlet bounded-variation argument. The line-specific fact is the exact Green factorization (PL321-7).

## 3. Exact-kernel and moving-diagonal errors

Because `Qm(Q)->0`, for large `Q` one has `|m(Q)|<=C/Q`. Therefore

\[
\int_0^{B_s}|m(Q)|\,dQ
=O_m(1+\log(1/s)).
\tag{PL321-15}
\]

Combining (PL321-7), (PL321-11), and `0<=w_s<=1`,

\[
\left|
\int_0^{B_s}k_s(r,sQ)m(Q)\,dQ
-a_s(r)\int_0^{B_s}w_s(Q)m(Q)\,dQ
\right|
=o(1),
\tag{PL321-16}
\]

because the exponentially small factor `e^{-r/(2s)}` dominates the logarithm in (PL321-15). Thus the pre-diagonal contribution tends to `e^{-r}M`.

For the remaining region define

\[
\omega(R):=\sup_{Q\ge R}Q|m(Q)|\to0.
\]

When `q>=r/2`, `Q=q/s>=B_s`, so

\[
\frac1s|m(q/s)|
\le\frac{\omega(B_s)}q
\le\frac2r\omega(B_s).
\]

The exact torsion identity used in `PL-310` and `PL-314` gives a uniformly bounded total Green mass. Hence

\[
\boxed{
\left|
\frac1s\int_{q\ge r/2}m(q/s)\,d\mu_{s,r}(q)
\right|
\le C_r\omega(B_s)\to0.
}
\tag{PL321-17}
\]

This proves (PL321-3).

## 4. Consequence for the completed-Weil endpoint

`PL-320` proves that if the actual endpoint tail `g` satisfies

\[
g(Q)\to0,
\qquad
F(Q)\to F_\infty,
\qquad
H_{Q_0}g(Q)\to H_\infty,
\]

then a coefficient `C` emerges automatically and

\[
g(Q)=CQ^{-1/2}+m(Q),
\qquad
Qm(Q)\to0,
\qquad
\int_{Q_0}^R m(Q)\,dQ\to M.
\tag{PL321-18}
\]

The completed-Weil eigen-equation already supplies the finite source trace `F(Q)->F_infinity`, while the established logarithmic-Laplacian boundary estimate gives `g(Q)=O(Q^{-1/2})`. A compactly supported endpoint complement is handled by `PL-313`. Therefore the present theorem removes the only extra absolute-`L^1` requirement left in `PL-320`.

The current endpoint-transfer frontier is reduced to the single local statement

\[
\boxed{H_{Q_0}g(Q)\text{ has a finite endpoint limit}.}
\tag{PL321-19}
\]

If that holds for the actual isolated completed-Weil branch, the same condition generates the leading coefficient, the `o(1/Q)` residual, the conditional endpoint moment, and now the full rank-one Green transfer. The separate rational-prime sign/first-crossing problem remains downstream.

## Prior-art and novelty audit

The Stieltjes integration-by-parts step is classical Abel/Dirichlet analysis and is not claimed as new. Bucur's Green formula is classical and already ledgered as source `102`. A targeted audit around Abelian theorems for conditionally convergent improper integrals, bounded-variation kernels, small-order fractional Green kernels, and boundary-layer limits recovered the standard Dirichlet/Stieltjes mechanism and established fractional Green formulas, but no theorem directly covering this `Q=q/s` Green family with its separate moving diagonal atom. Search absence is not used as evidence of broad novelty.

The durable line-local statement is exact and narrower: **the absolute `L^1(dQ)` assumption in `PL-314` is not load-bearing.** The pre-diagonal Green kernel itself supplies the bounded-variation Abel weight, while the already-required law `Qm(Q)->0` controls the exponentially small factorization error and the moving/post-diagonal mass.

## Adversarial controls and limits

- Conditional convergence by itself is insufficient; `Qm(Q)->0` is still required to suppress the moving diagonal. The sparse `Theta(1/Q)` construction of `PL-314` remains excluded for exactly this reason.
- No monotonicity, BV, Sobolev regularity, or absolute integrability of `m` is assumed. Bounded variation belongs to the explicit kernel weight `w_s`.
- The exponentially accurate factorization is used only on `q<=r/2`, a fixed stretched distance from the diagonal. No shrinking-neighborhood estimate for the atom is smuggled in.
- The theorem is pointwise for each fixed `r>0`; no uniform statement as `r->0`, `r->infinity`, or across aperture activations is made.
- This closes a universal analytic matching gate only. It provides no arithmetic sign, positivity, zero-localization, or rational-prime rigidity.

## Verdict

**Exact analytic gate closure.** A conditionally convergent endpoint moment plus `Qm(Q)->0` is sufficient for the rank-one Green transfer. The absolute residual integrability left open by `PL-320` is unnecessary. For the completed-Weil branch, convergence of the singular translation remainder is now the sole unresolved endpoint-transfer condition in this chain; the arithmetic sign/first-crossing problem remains separate.

## Sources

- Source `102` in `research/prime_lattice/SOURCES.md`: Claudia Bucur, “Some observations on the Green function for the ball in the fractional Laplace framework,” *Communications on Pure and Applied Analysis* **15**(2) (2016), 657–699. Supplies the exact interval Green kernel used above.
- `PL-310`: stretched Green measure, moving diagonal atom, and exact total-mass control.
- `PL-313`: compact-support rank-one corner transfer.
- `PL-314`: previous sufficient theorem with absolute `L^1(dQ)` and the sparse-diagonal counterexample.
- `PL-319`: exact logarithmic endpoint source identity and completed-Weil source-trace convergence.
- `PL-320`: full-tail Volterra reduction giving `Qm(Q)->0` and a convergent improper residual moment from convergence of the singular remainder trace.