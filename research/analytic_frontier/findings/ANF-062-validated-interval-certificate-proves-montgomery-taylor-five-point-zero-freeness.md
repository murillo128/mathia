# ANF-062 — validated interval certificate proves Montgomery--Taylor five-point zero-freeness

**Status:** `COMPUTER-ASSISTED + ARB-INTERVAL-CERTIFIED + EXACT-OUTER-REDUCTIONS + FIVE-POINT-ZERO-FREENESS + CENTRAL-NOTCH-SURVIVAL`. The exact reductions `ANF-045`, `ANF-057`, `ANF-059`, `ANF-060`, and `ANF-061` turn the fixed Montgomery--Taylor two-conjugate-pair plus one-real-point obstruction into a bounded sign problem after analytic treatment of the real-axis and common-translation escapes. A dedicated validated computation under Mathia issue [#121](https://github.com/murillo128/mathia/issues/121) now closes that sign problem: the exact Montgomery--Taylor defect is strictly positive at every genuine geometry,

\[
\boxed{
H_{\rm MT}(y_1,y_2;t_1,t_2)>0
\qquad
(y_1,y_2>0,\ t_1,t_2\in\mathbb R).
}
\tag{1}
\]

The certificate is computer-assisted rather than a closed-form analytic inequality. It combines the canonical exact outer-domain reductions with an Arb/FLINT interval cover of the remaining compact closure, including the limiting `y=0` and `q=1` faces and an analytic half-line bound for common translation. The compact cover inspected `804375` rational boxes, produced `402188` positive leaves, and left no unresolved cell after precision escalation from 128 to 512 bits. On the residual box the smallest certified lower endpoint for the normalized defect was

\[
\boxed{
\frac{H_{\rm MT}}{y_1^2+y_2^2}
>3.91727782744812265709656\times 10^{-6}.
}
\tag{2}
\]

This is a margin for the residual interval enclosure, not a claim that the global sharp coercivity constant is of that size.

By the zero-set dichotomy of `ANF-053`, (1) immediately settles the cardinality-five gate for the central-notch separator ray: there exists `eta_*>0` such that every sufficiently narrow nontrivial notch `J_{eta,s}` with `0<eta<eta_*` and `0<s<=1` has strictly positive two-pair five-point defect at every genuine geometry. The result does **not** address larger conjugation-invariant multisets, does not provide a sharp all-height coercivity constant, and does not by itself imply RH.

## 1. Exact defect and cancellation-safe normalization

Retain the Hilbert normal form of `ANF-045`. Put

\[
d=t_1-t_2,
\qquad t=t_2,
\qquad a_j(\alpha)=\cosh(2\pi\alpha y_j)-1,
\tag{3}
\]

\[
u_d(\alpha)=a_1(\alpha)e^{2\pi i\alpha d}+a_2(\alpha),
\tag{4}
\]

and

\[
\begin{aligned}
Q&=\int J_{\rm MT}(\alpha)|u_d(\alpha)|^2\,d\alpha,\\
P&=2\int J_{\rm MT}(\alpha)(a_1+a_2)
       (1+\cos(2\pi\alpha d))\,d\alpha,\\
Z(t)&=\int J_{\rm MT}(\alpha)e^{2\pi i\alpha t}u_d(\alpha)\,d\alpha.
\end{aligned}
\tag{5}
\]

Then

\[
\boxed{H_{\rm MT}=Q+P+\operatorname{Re}Z.}
\tag{6}
\]

The computation parameterizes the ordered heights by

\[
y_1=y(1+q),\qquad y_2=y(1-q),\qquad 0\le q\le1,
\tag{7}
\]

so

\[
S:=y_1^2+y_2^2=2y^2(1+q^2).
\tag{8}
\]

For a spectral node `x`, define `f_1=1+q`, `f_2=1-q` and

\[
A_j=2(\pi x f_j)^2\operatorname{sinc}(i\pi x y f_j)^2.
\tag{9}
\]

Because `y^2 A_j=cosh(2 pi x y f_j)-1=a_j`, direct substitution into (6) gives the cancellation-safe normalized integrand

\[
\boxed{
\frac{1}{2(1+q^2)}\Bigl[
 y^2\bigl((A_1-A_2)^2+2A_1A_2C\bigr)
 +2(A_1+A_2)C
 +A_1\cos(2\pi x(t+d))
 +A_2\cos(2\pi xt)
\Bigr],
}
\tag{10}
\]

where `C=1+cos(2 pi x d)`. This identity is exact and remains regular at `y=0` and `q=1`; the interval implementation therefore does not obtain positivity by imposing an artificial positive cutoff on either limiting face.

The Research Watch reconstruction checked (10) algebraically from `ANF-045`, rather than treating the compute clue as evidence by itself. It also verified that the compute source revision `fcb42ecf9aeffe1742a575a60a9d54c49b2ddd15` and the current canonical branch have identical load-bearing `analytic_frontier` findings: the only line-local change after that source revision before this finding was the proposed compute-return clue.

## 2. Canonical outer reductions leave one explicit compact closure

`ANF-057`, `ANF-059`, and `ANF-060` prove that every zero or negative value would have to satisfy

\[
0<y<0.7501775,
\qquad q>0.1409,
\qquad 0.545<|d|<1.01.
\tag{11}
\]

The exact reflection

\[
(d,t)\mapsto(-d,-t)
\tag{12}
\]

allows the compact computation to use positive `d` without losing the negative-separation branch.

The small-height face is discharged analytically. The validated curvature calculation gives

\[
m>0.06344,
\qquad m_5(J_{\rm MT})>0.03532,
\tag{13}
\]

and the fourth-order `cosh` remainder then yields

\[
\boxed{
0\le y\le\frac1{16}
\quad\Longrightarrow\quad
\frac{H_{\rm MT}}{S}>0.4889.
}
\tag{14}
\]

No sampled lower height cutoff is used.

For the common-translation escape, `ANF-061` writes

\[
R_y(s)=\int J_{\rm MT}(\alpha)
\frac{\cosh(2\pi\alpha y)-1}{y^2}
 e^{2\pi i\alpha s}\,d\alpha
\tag{15}
\]

with the continuous `y=0` value and the cancellation-safe representation

\[
R_y(s)
=-\frac12\int_{-1}^{1}(1-|u|)
F_{\rm MT}''(s+iuy)\,du.
\tag{16}
\]

Using the closed Montgomery--Taylor transform from `ANF-059`, the validated rational/exponential derivative envelope at

\[
Y=1.500355,
\qquad T_{\rm tail}=64
\tag{17}
\]

certifies

\[
\sup_{0\le y\le1.500355,\ |s|\ge64}|R_y(s)|<1.127145
<2\pi^2m.
\tag{18}
\]

Accounting for `|d|<=1.01`, every possible nonpositive point is therefore captured by

\[
|t|\le65.01.
\tag{19}
\]

The resulting interval domain is the closed box

\[
\boxed{
(y,q,d,t)\in
[1/16,0.7501775]\times[0.1409,1]
\times[0.545,1.01]\times[-65.01,65.01].
}
\tag{20}
\]

The endpoint enlargement in (20) is intentional: canonical strict exclusions justify it, while including the faces makes the exhaustive cover outward-safe.

## 3. Validated interval cover has no unresolved cell

Issue #121 executed the frozen computation with Python 3.12.3, `python-flint 0.9.0`, FLINT 3.6.0, and Arb balls. Every certificate comparison used outward-rounded interval arithmetic. Cells began at 128-bit precision; any undecided cell was re-evaluated at 512 bits before subdivision.

On `[0,1]` the exact even Montgomery--Taylor density used by the quadrature was

\[
2J_{\rm MT}(x)=
\frac{(1-x)\cos(\sqrt2x)+\sin(\sqrt2(1-x))/\sqrt2}
{2\sin^2(1/\sqrt2)}.
\tag{21}
\]

Arb-enclosed Gauss--Legendre roots and weights were combined with a full analytic derivative-error term. The implementation used only sufficient positive filters: the canonical height/phase splice, the global translation tail, the phase-blind `Q+P-L` barrier, quadrature-plus-local-tail bounds, and finally direct evaluation of (10). Failure of any sufficient filter triggered refinement; it was never interpreted as a negative witness.

The exhaustive traversal inspected

\[
804375
\tag{22}
\]

rational boxes and ended with `402188` positive leaves and zero unresolved cells. The positive leaves were discharged as follows: `52211` by the height/phase splice, `13507` by the global tail, `111404` by the phase-blind filter, `11203` by quadrature plus a local tail, and `213863` by the full normalized integrand. The deterministic leaf-traversal digest recorded by the executor is

`d9d7b0505f6c86634fa972373ee209419428edead6d559384fce8ba3b0898588`.

The smallest certified lower endpoint among the residual leaves is the value in (2). Since every cell in (20) is positively certified and Sections 1--2 cover its limiting and noncompact complements, no genuine zero remains.

## 4. Independent implementation controls and evidence boundary

Before the interval cover was trusted, the executor compared the direct integrand of `ANF-045` with the independent `Q+P+Re Z` implementation on seven predeclared interior and boundary-near points. At 90 decimal digits the normalized discrepancy was below `1.8e-75`, including removable-singularity arguments. Five additional 220-digit direct quadratures were enclosed at both 128 and 512 bits. These are implementation controls only; the proof of (1) is the exhaustive interval cover plus the analytic boundary/tail reductions, not agreement at sampled points.

The curvature input was also certified independently from the exact transform. Evaluating `K=-F''/(4 pi^2)` on the `0.001` grid through `1.01`, combining it with the exact `ANF-059` Lipschitz bound, and using the already proved outer interval gives

\[
K(t)>-0.091557341196778
\qquad(t\in\mathbb R),
\tag{23}
\]

which supplies (13). The half-line tail in (18) is analytic, not sampled decay.

This evidence status is deliberately narrower than `EXACT-DERIVED`: the finite closure is a validated computer-assisted certificate whose reproduction specification lives in issue #121. Ordinary floating-point searches made during the compute audit are not used in (1), and no claim below depends on them.

## 5. Consequence for the central-notch separator ray

`ANF-053` proves the exact dichotomy

\[
H_{\rm MT}\text{ zero-free on genuine shapes}
\Longleftrightarrow
\exists\eta_*>0\ \forall 0<\eta<\eta_*\ \forall 0<s\le1:
H_{\eta,s}>0
\tag{24}
\]

throughout the genuine two-pair domain. Applying (1) to (24) yields the right-hand side. Thus the signed cubic perturbation found in `ANF-053` is no longer an unresolved danger: the base profile has no zero on which that negative cubic term can act, and uniform family compactness transfers strict positivity to every sufficiently narrow notch.

Combined with the separately proved finite-real gain and normalization control of `ANF-034` and `ANF-046`, the central-notch direction now survives the complete cardinality-five scalar test. What remains is no longer a five-point base-zero problem. Any route toward the line mandate must either control larger conjugation-invariant multisets or replace the scalar carrier with genuinely richer horizontal information.

## 6. Prior art and remaining frontier

A targeted current-literature check found the Montgomery--Taylor extremal kernel, unconditional pair-correlation work, and recent finite-block/validated-Arb improvements of the simple-critical-zero constant, but no external theorem deciding this exact Mathia two-pair Fourier--Laplace defect. Those nearby computations use different block or Gram carriers and do not substitute for (1). No new external theorem is load-bearing here, so `SOURCES.md` is unchanged.

The most natural structural strengthening is now different from zero-freeness. The compute return isolated an all-order even-moment condition that would imply the sharp coercive inequality

\[
H_{\rm MT}
\ge 2\pi^2m_5(J_{\rm MT})(y_1^2+y_2^2)
\tag{25}
\]

and monotonicity of the normalized defect under simultaneous height dilation. That condition is not part of the present certificate and remains unproved. Likewise, (1) does not certify any larger multiset and does not itself close the universal zeta argument.