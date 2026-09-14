# PL-313 — The compressed physical corner transfers to the outer Volterra problem through one rank-one endpoint functional

**Evidence:** `LITERATURE+EXACT-DERIVED + SOURCE-SELECTION-REFINEMENT + MATCHED-ASYMPTOTIC-GATE`

**Status:** `EXACT-CORNER-TRANSFER + OUTER-COKERNEL-IDENTIFIED + ACTUAL-BRANCH-WEIGHTED-MATCHING-OPEN + ARITHMETIC-SIGN-OPEN`

## Precise claim

`PL-311` showed that every fixed physical point is compressed into the `r=O(s)` corner of the stretched variable

\[
x_s(r)=1-2e^{-r/s},
\]

and `PL-312` showed that the limiting outer defect `I-T` has exactly one `C^1` solvability condition, namely vanishing of the endpoint value of the forcing. What was still missing was an exact map from physical-scale information in that compressed corner to the forbidden outer direction.

The one-dimensional fractional Green kernel supplies that map explicitly. Let `G_s` be the zero-exterior Green kernel of `(-Delta)^s` on `I=(-1,1)`, and let `T_s` denote the stretched Green operator of `PL-310`:

\[
(T_sF)(r)
=\int_0^\infty F(q)\,d\mu_{s,r}(q),
\qquad
 d\mu_{s,r}(q)
=G_s(x_s(r),x_s(q))\frac{2}{s}e^{-q/s}\,dq.
\tag{PL313-1}
\]

For every compact `K\Subset(-1,1)` and every compact outer interval `J\Subset(0,\infty)`, Bucur's explicit interval Green kernel gives the uniform double-scale limit

\[
\boxed{
\sup_{r\in J,\,y\in K}
\left|
\frac{G_s(x_s(r),y)}{s}
-\frac{e^{-r}}{1-y}
\right|\longrightarrow0.
}
\tag{PL313-2}
\]

Consequently, for every `m\in C_c(-1,1)`, define the physical-corner perturbation in stretched coordinates by

\[
F_{s,m}(q)
:=s^{-1/2}m(x_s(q)).
\tag{PL313-3}
\]

Then, locally uniformly for `r>0`,

\[
\boxed{
\frac1{\sqrt s}(T_sF_{s,m})(r)
\longrightarrow
 e^{-r}\,\mathcal M_+(m),
\qquad
\mathcal M_+(m)
:=\int_{-1}^{1}\frac{m(y)}{1-y}\,dy.
}
\tag{PL313-4}
\]

Thus an `O(1)` perturbation of the physical state living in the `r=O(s)` corner becomes, after the `U_s=s^{-1/2}w_s` outer normalization, an `O(\sqrt s)` perturbation in **exactly one outer direction**: `e^{-r}`. The full physical shape is compressed to the single weighted scalar `\mathcal M_+(m)`.

By reflection, the corresponding left-boundary outer chart has the scalar functional

\[
\boxed{
\mathcal M_-(m)=\int_{-1}^{1}\frac{m(y)}{1+y}\,dy.
}
\tag{PL313-5}
\]

This is the missing structural link between the qualitative `r=O(s)` localization in `PL-311` and the one-dimensional cokernel detected by `PL-312`: **the corner itself arrives in the outer equation precisely in the forbidden endpoint direction.**

The result does not yet prove the matching law for the actual completed-Weil eigenbranch. To obtain that law one must identify the physical corner mismatch relative to the singular outer profile in a class for which `\mathcal M_\pm` is meaningful and prove that all other `O(\sqrt s)` contributions are controlled. Under such a decomposition, however, the outer solvability condition is necessarily scalar rather than a hidden functional family.

## 1. Direct derivation from the exact Green kernel

Bucur's one-dimensional unit-ball Green kernel, already used in `PL-309` and `PL-310`, is

\[
G_s(x,y)
=\frac{|x-y|^{2s-1}}{2^{2s}\Gamma(s)^2}
\int_0^{R(x,y)}\frac{z^{s-1}}{\sqrt{1+z}}\,dz,
\qquad
R(x,y)=\frac{(1-x^2)(1-y^2)}{|x-y|^2}.
\tag{PL313-6}
\]

Fix `r` in a compact subset of `(0,\infty)` and `y` in `K\Subset(-1,1)`. Put

\[
t=e^{-r/s},\qquad x_s(r)=1-2t.
\]

Then `t` is exponentially small uniformly in `r`, while `1-y` stays bounded away from zero. Hence

\[
R(x_s(r),y)=O(t)
\]

uniformly on `J\times K`, and

\[
\int_0^{R}\frac{z^{s-1}}{\sqrt{1+z}}\,dz
=\frac{R^s}{s}(1+o(1))
\tag{PL313-7}
\]

with a uniform error. Substituting `1-x_s(r)^2=4t(1-t)` and using `t^s=e^{-r}` yields

\[
G_s(x_s(r),y)
=
 e^{-r}\frac{s}{\Gamma(1+s)^2}
 (1-y)^{s-1}(1+y)^s(1+o(1)).
\tag{PL313-8}
\]

Since `\Gamma(1+s)\to1` and the powers converge uniformly on `K`, (PL313-2) follows. This is a genuine simultaneous `s\downarrow0`, `x_s(r)\uparrow1` limit; no interchange of a fixed-`s` boundary limit with `s\downarrow0` is being assumed.

Now (PL313-1) is merely the physical Green integral written under the pushforward `y=x_s(q)`. Therefore

\[
(T_sF_{s,m})(r)
=s^{-1/2}\int_{-1}^{1}G_s(x_s(r),y)m(y)\,dy.
\tag{PL313-9}
\]

Divide by `\sqrt s`, apply (PL313-2) on the compact support of `m`, and use dominated convergence. This gives (PL313-4) immediately.

Equivalently, with the physical logarithmic-distance coordinate

\[
Q=-\log\frac{1-y}{2},
\qquad
 y=1-2e^{-Q},
\qquad
 dQ=\frac{dy}{1-y},
\tag{PL313-10}
\]

the transfer coefficient is simply

\[
\mathcal M_+(m)
=\int m(1-2e^{-Q})\,dQ.
\tag{PL313-11}
\]

So the relevant corner mass is ordinary mass in the physical log-distance variable. This is exactly the coordinate that becomes `q=sQ` in the outer stretching.

## 2. Why the `sqrt(s)` scale is the matching scale

The outer state is normalized in `PL-310` as

\[
U_s(r)=s^{-1/2}w_s(x_s(r)).
\tag{PL313-12}
\]

A physical-scale difference `m(y)=O(1)` between the true bulk/corner state and an outer extrapolation therefore appears in `U_s` as `s^{-1/2}m(x_s(q))`, exactly (PL313-3). Equation (PL313-4) then says that after one Green propagation its outer effect is

\[
\sqrt s\,e^{-r}\mathcal M_+(m)+o(\sqrt s).
\tag{PL313-13}
\]

This is the same order as the completed-Weil lower source in the stretched eigen-equation of `PL-310`,

\[
U_s=T_s\bigl[\alpha_sU_s-2\sqrt s\,a^{2s}g_s\bigr],
\qquad
\alpha_s=1+O(s).
\tag{PL313-14}
\]

At fixed outer `r`, a boundary limit `g_s\to g_+` contributes

\[
-2\sqrt s\,g_+e^{-r}+o(\sqrt s),
\tag{PL313-15}
\]

because `T_s1\to e^{-r}`. The `O(s)` scalar correction `\alpha_s-1` is smaller on the regular fixed-`r` outer scale. Hence the physical corner and the lower completed-Weil source naturally meet at the same first nontrivial `\sqrt s` order and in the same outer direction.

This does **not** by itself prove that those are the only `O(\sqrt s)` terms for the actual branch. In particular, a complete matching theorem must control the singular principal profile through the overlap and show that the residual kernel error contributes no additional independent endpoint scalar.

## 3. Combination with the exact outer range theorem

`PL-312` proves that for a `C^1` first outer correction `f`,

\[
(I-T)f=h
\]

is solvable in `C([0,R])` exactly when

\[
h(0)=0.
\tag{PL313-16}
\]

The mode `e^{-r}` has endpoint value one, so (PL313-4) shows that a compact physical corner perturbation lands exactly in the unique obstructed direction of the regular outer equation. There is no mismatch of codimensions: the compressed physical problem supplies a scalar and the outer range loses a scalar.

For example, suppose a justified first-order matched expansion has no other endpoint-active `O(\sqrt s)` term and its corner mismatch is represented by `m`, while the lower source has the boundary value `g_+`. Then the `e^{-r}` coefficient in the first outer forcing is

\[
\mathcal M_+(m)-2g_+,
\]

and (PL313-16) forces the scalar compatibility law

\[
\boxed{\mathcal M_+(m)=2g_+.}
\tag{PL313-17}
\]

Equation (PL313-17) is stated only as the consequence of those explicit matching hypotheses, not as an established identity for the completed-Weil branch. Its significance is structural: the sought corner-to-outer matching condition now has a canonical candidate functional rather than an unspecified endpoint correction.

## 4. Relation to the singular amplitude

The outer homogeneous mode is

\[
F_C(r)=\frac{C}{\sqrt{e^{2r}-1}}
\sim\frac{C}{\sqrt{2r}}
\qquad(r\downarrow0).
\tag{PL313-18}
\]

In the overlap `r=sQ` with `Q\to\infty` but `sQ\to0`, this predicts the physical boundary behavior

\[
w_s(1-2e^{-Q})
=\sqrt s\,U_s(sQ)
\sim\frac{C}{\sqrt{2Q}}.
\tag{PL313-19}
\]

Thus a finite `\mathcal M_+` for the mismatch between the actual zero-order physical state and the outer extrapolation requires, at minimum, matching their leading `Q^{-1/2}` boundary coefficients. If the coefficients disagree, the integral in (PL313-11) diverges like `\sqrt Q`, signaling that the amplitude has not yet been matched rather than producing a finite regular forcing.

This gives a precise hierarchy for a future theorem:

1. identify `C` with the coefficient of the logarithmic `Q^{-1/2}` boundary law strongly enough that the mismatch is integrable in `dQ`;
2. evaluate the finite remainder `\mathcal M_+(m)`;
3. balance it against the completed source through the single outer compatibility condition.

The first item is stronger than the presently known two-sided Hopf/boundary scale and is not proved here. In particular, `PL-313` does not claim existence of a logarithmic boundary quotient trace.

## 5. Adversarial controls and evidence boundaries

The exact theorem is only (PL313-2)--(PL313-5). Several controls are essential.

**No generic bulk-convergence shortcut.** `PL-309` already proves that ordinary `C_0` or `L^infty` convergence does not determine the renormalized fractional boundary trace. The present result does not contradict that obstruction: it assumes an explicitly resolved physical corner component and computes how that component propagates outward.

**No universal profile is being rebranded as arithmetic information.** The kernel factor `e^{-r}/(1-y)` is generated entirely by the pure fractional Green geometry. Rational-prime specificity can enter only through the actual corner mismatch `m`, the lower source `g_+`, or a relation between them forced by the completed-Weil eigen-equation.

**Compact support is the exact theorem's safe class.** It avoids claiming an unjustified endpoint trace. Extension from `C_c(-1,1)` to a genuine matched mismatch reaching `y=1` requires weighted integrability against `(1-y)^{-1}dy`, equivalently `L^1(dQ)`, and uniform control of the Green asymptotic in the overlap. That extension is precisely part of the remaining matching problem.

**No sign theorem.** The scalar `\mathcal M_+(m)` can have either sign. Even a successful completed-Weil matching law would still need an arithmetic mechanism controlling the resulting amplitude/virial sign at a first crossing.

## Prior-art and novelty audit

The load-bearing Green formula and its fixed-order boundary trace are classical; Bucur's interval/ball Green kernel is source `102` in `research/prime_lattice/SOURCES.md`. `PL-309` already derived the endpoint trace normalization and exponential coordinate, while `PL-310` derived the fixed-outer Green-measure limit. `PL-311` and `PL-312` isolated and then completely characterized the outer endpoint range obstruction.

A targeted literature audit around small-order fractional-Laplacian boundary layers, logarithmic-Laplacian boundary regularity/Hopf estimates, Green-function asymptotics, and recent small-order `s`-harmonic asymptotics found the established ingredients but no directly matching theorem that couples the physical `r=sQ` corner to the specific `PL-310` outer Volterra limit through (PL313-4). Search absence is not treated as evidence of broad novelty. The durable claim is narrower and exact: combining the classical Green kernel with the line's stretched coordinate yields the rank-one corner transfer and identifies its scalar with the very cokernel direction already proved in `PL-312`.

## Consequence for the research line

The finite-`s` matching frontier is now more concrete. `PL-311` said that the missing compensation must live in the `r=O(s)` corner; `PL-313` shows exactly what that corner can communicate to the first regular outer correction: one weighted scalar per endpoint,

\[
\mathcal M_\pm(m)=\int_{-1}^{1}\frac{m(y)}{1\mp y}\,dy,
\]

carried by the outer mode `e^{-r}`. This matches the one scalar solvability obstruction of `PL-312` rather than generating an uncontrolled infinite-dimensional interface.

The next theorem should therefore not search for additional smooth outer Fredholm conditions. It should prove a genuine overlap decomposition for the actual completed-Weil eigenbranch, identify the singular amplitude with the logarithmic boundary coefficient strongly enough to make the residual mismatch `L^1(dQ)`, and then compute the resulting `\mathcal M_\pm` balance including the finite active prime-power/completion source. Only after that analytic matching law is established does the separate rational-prime sign problem become available.

## Sources

- Claudia Bucur, “Some observations on the Green function for the ball in the fractional Laplace framework,” *Communications on Pure and Applied Analysis* **15**(2) (2016), 657–699. DOI: https://doi.org/10.3934/cpaa.2016.15.657. arXiv: https://arxiv.org/abs/1502.06468.
- `PL-309`: exact small-order Green trace and exponential boundary layer.
- `PL-310`: stretched Green-measure limit and universal Volterra fixed profile.
- `PL-311`: endpoint range obstruction and localization of physical bulk to `r=O(s)`.
- `PL-312`: exact regular range and right inverse for the limiting Volterra defect.
