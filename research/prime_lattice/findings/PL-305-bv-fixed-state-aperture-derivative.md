# PL-305 — BV regularity makes every lower-order Suzuki aperture term `C^1`, including prime activations

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-ROUTE-REFINEMENT`

**Status:** `FIXED-STATE-LOWER-ORDER-DERIVATIVE-RESOLVED + BRANCH-BV-AND-BOUNDARY-STRESS-OPEN`

## Claim

The source-structured escape left after `PL-304` can be sharpened. For Suzuki's exact fixed-domain localized-Weil form, once a fixed state has the regularity

\[
w\in C_0((-1,1))\cap BV_0((-1,1)),
\]

all **lower-order** dependence on the aperture `a` is genuinely `C^1`. This includes the discrete prime-power shift contribution, the activation of a new prime-power channel at `2a=log n`, and the completed archimedean integral term. No `H^{1/2}` assumption or absolute first Fourier moment is needed.

Write the zero extension of `w` again as `w` and define its autocorrelation

\[
C_w(h)=\int_{\mathbb R}w(x+h)\overline{w(x)}\,dx.
\]

Then `C_w in C^1(R)`, and because `supp(w) subset [-1,1]`,

\[
C_w(h)=C_w'(h)=0\qquad (|h|\ge2).
\]

Using Suzuki's scaled formula (4.5), the arithmetic part is

\[
q_a^{\rm ar}(w)
=-2\sum_{\substack{n\ge2\\ \Lambda(n)>0\\ \log n<2a}}
\frac{\Lambda(n)}{\sqrt n}\,\Re C_w\!\left(\frac{\log n}{a}\right).
\]

Hence, away from an activation threshold,

\[
\boxed{
\frac d{da}q_a^{\rm ar}(w)
=
2\sum_{\log n<2a}
\frac{\Lambda(n)\log n}{a^2\sqrt n}\,
\Re C_w'\!\left(\frac{\log n}{a}\right).
}
\]

At `a_n=(log n)/2`, the new lag equals the support diameter, `h_n(a_n)=2`. Since both `C_w(2)` and `C_w'(2)` vanish, the newly activated term and its first aperture derivative both enter with value zero. Therefore the arithmetic contribution is `C^1` **through every prime-power activation** for a fixed `C_0 cap BV` state.

The completion term is also `C^1` and costs no extra state regularity. In Suzuki's notation,

\[
q_a^{\rm comp}(w)
=-a\int_I\int_I r''(a(x-y))w(y)\overline{w(x)}\,dx\,dy.
\]

The explicit decomposition in Section 2.4 gives

\[
r_0(t)=-4(e^{t/2}+e^{-t/2}-2),
\qquad
r_1''(t)=\frac{e^{-|t|/2}}{1-e^{-2|t|}}-\frac1{2|t|}.
\]

For `x>0`,

\[
r_1''(x)=\frac14-\frac{x}{48}+O(x^2),
\]

so

\[
\kappa(t):=r''(t)+t r'''(t)\quad(t\ne0)
\]

has a bounded continuous extension across `t=0`. Consequently, on every compact aperture interval on which Suzuki's scaled formula is used,

\[
\boxed{
\frac d{da}q_a^{\rm comp}(w)
=-\int_I\int_I
\kappa(a(x-y))w(y)\overline{w(x)}\,dx\,dy,
}
\]

and this derivative is a bounded quadratic form on `L^2(I)`, uniformly for `a` in compact sets.

Thus the lower-order arithmetic/completion part is **not** the remaining analytic obstruction in the accepted zero-order Hadamard route once uniform `C_0+BV` control of the state is available. The unresolved gates are now narrower: establish that regularity uniformly for the actual regularized completed-Weil simple ground branch, obtain the intrinsic zero-order boundary stress, and then prove a rational-prime-specific sign or first-crossing law. The completion term and prime-power activation themselves do not introduce an additional first-derivative singularity.

## 1. Why `BV cap C_0` is exactly enough for the shift derivative

For compactly supported `w in C_0 cap BV`, its distributional derivative `Dw` is a finite measure. The autocorrelation can be written as a convolution, and in distributions

\[
C_w'=\widetilde{\overline w}*Dw
\]

(up to the harmless convention for reflection). A continuous compactly supported function convolved with a finite measure is continuous. Therefore `C_w in C^1(R)`.

This is the same physical-space currency isolated in `PL-299`, but here it is inserted into the **full exact scaled arithmetic form**, rather than only used to pass a pure-principal small-order limit at one fixed lag.

Because `C_w` is identically zero for `|h|>=2` and is globally `C^1`, its derivative also vanishes at the support edge. Hence the function

\[
a\longmapsto
1_{\{\log n<2a\}}
C_w\!\left(\frac{\log n}{a}\right)
\]

is `C^1` at `a=(log n)/2`: the value and the one-sided first derivative from the active side both tend to zero. The apparent discontinuous change in Suzuki's finite prime-power index set is therefore harmless at first order on this state class.

Locally in `a` there are only finitely many active prime powers, so termwise differentiation is legitimate and yields the displayed arithmetic derivative.

## 2. The completed archimedean remainder has a bounded aperture derivative

Suzuki separates the non-prime remainder into `r=r_0+r_1`. The smooth `r_0` part is immediate. For the only potentially delicate part, set for `x>0`

\[
F(x)=\frac{e^{-x/2}}{1-e^{-2x}}-\frac1{2x}.
\]

A Taylor expansion gives

\[
F(x)=\frac14-\frac{x}{48}-\frac{x^2}{32}+O(x^3).
\]

Since `r_1''(t)=F(|t|)`, `r_1''` is even and Lipschitz at the origin although its ordinary third derivative has opposite one-sided limits. The combination that aperture differentiation actually produces is better behaved:

\[
F(x)+xF'(x)=\frac14-\frac{x}{24}+O(x^2).
\]

Thus `r_1''(t)+t r_1'''(t)` extends continuously through zero. Away from zero it is smooth. On every compact difference range `|t|<=2a_*`, the resulting kernel is bounded.

Differentiating

\[
a r''(a\tau)
\]

therefore gives the bounded continuous kernel

\[
\kappa(a\tau)=r''(a\tau)+(a\tau)r'''(a\tau),
\]

with the value at `tau=0` understood by continuous extension. Dominated convergence then proves the completion formula for every `w in L^2(I)`; `BV` is not needed for this part.

In particular, on a compact aperture set `K subset (0,infinity)`, there is a finite constant `M_K` such that

\[
\left|\frac d{da}q_a^{\rm comp}(w)\right|
\le M_K\|w\|_2^2,
\qquad a\in K.
\]

The exact value of `M_K` is irrelevant here; the point is that the completion does not ask for the missing spatial derivative.

## 3. Full fixed-state derivative and relation to the live branch problem

For a normalized fixed state, the scaled form has the decomposition

\[
q_a(w)
=
\mathcal L(w)-(2A+1+\log a)\|w\|_2^2
+q_a^{\rm ar}(w)+q_a^{\rm comp}(w).
\]

Therefore, for `w in C_0 cap BV` with `\|w\|_2=1`,

\[
\boxed{
\partial_a q_a(w)
=-\frac1a
+2\sum_{\log n<2a}
\frac{\Lambda(n)\log n}{a^2\sqrt n}
\Re C_w'\!\left(\frac{\log n}{a}\right)
-\iint_{I^2}\kappa(a(x-y))w(y)\overline{w(x)}\,dx\,dy.
}
\]

The same expression extends continuously through the prime-power thresholds because the activating autocorrelation slope is zero there.

This is a **fixed-state** statement. It does not prove differentiability of `a -> lambda_a` or of a varying eigenvector branch. For a simple eigenbranch, a Feynman--Hellmann conclusion still requires a perturbation theorem whose hypotheses are valid for the actual form family, or a direct variational argument. More importantly for the present research line, it does not prove the load-bearing hypothesis

\[
\sup_s TV(u_{s,a})<\infty
\]

for the fractional regularizations of the completed-Weil branch. `PL-300`--`PL-304` show that this cannot be obtained from generic spectral stability, an `L^2` gap, any ordinary `L^p` forcing norm, or the full finite-measure forcing space.

What the calculation does prove is that **if** the source-specific BV compactness demanded after `PL-304` is obtained, then the two lower-order issues still listed in the Hadamard clue do not require another regularity theorem: the discrete shift derivatives and the completion derivative are already controlled, and source activation is `C^1`.

## 4. Adversarial and novelty audit

The main external input is Suzuki's exact scaled formula (4.5) and his explicit remainder formula in Section 2.4. Suzuki proves continuity of the lowest eigenvalue in `a`; he does not state the `C_0 cap BV` fixed-state `C^1` aperture formula above, nor a Hadamard/Feynman--Hellmann theorem for the completed ground branch. A targeted search for derivatives of Suzuki's localized Weil Rayleigh quotient and for logarithmic-Laplacian Hadamard formulas located the known fractional Hadamard theory but no published theorem giving this completed fixed-state formula.

No novelty is claimed for the individual analytic ingredients: differentiation of translations through BV autocorrelations, convolution of a continuous function with a finite measure, or dominated differentiation of a bounded kernel are standard. The line-local contribution is the exact combination with Suzuki's rational-prime lags and the observation that **every activation threshold is first-order transparent**, while the completed remainder has a bounded `L^2` derivative.

The result is deliberately weaker than a shape derivative of the eigenvalue. It cannot be used to infer the sign of `lambda_a'`, monotonicity of the ground branch, or RH. It also remains universal under replacement of the rational-prime weights by any locally finite collection of fixed positive shift weights with the same support geometry; rational-prime rigidity would have to enter through the actual values of the weighted autocorrelation slopes or another source-specific constraint.

The calculation does not resurrect an ambient coercivity route closed by `PL-304`: `C^1` dependence of the scalar form on `a` is not a bound of `TV(w)` by the resolvent or by `|partial_a q_a(w)|`.

## Consequence for `prime_lattice`

The accepted zero-order Hadamard clue can now be narrowed again. Its lower-order test separates cleanly:

\[
\boxed{
C_0+BV\text{ state control}
\Longrightarrow
\text{all prime-shift and completion aperture terms are }C^1,
}
\]

including across prime-power activation. The remaining analytic burden is therefore **state-side**, not kernel-side: obtain source-structured uniform BV/derivative-measure compactness for the actual regularized completed-Weil ground branch and an intrinsic logarithmic boundary stress. The remaining arithmetic burden is independent: show that the resulting derivative identity has a rational-prime-specific sign or first-crossing mechanism rather than a universal matched-weight analogue.

## Dependencies

- `PL-297`: the renormalized Hadamard stress is not equivalent to a uniform `H^{1/2}` bound.
- `PL-298`: fixed-order prime-shift autocorrelations can be differentiated in physical space.
- `PL-299`: uniform `C_0+BV` compactness passes those derivatives to zero order on the pure principal branch.
- `PL-300`--`PL-304`: generic perturbation, gap, ordinary `L^p`, and finite-measure coercivity do not supply the needed BV state control.
- Source `56` in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2 (2026), especially formulas (4.5), (2.5), and the explicit `r_1''` formula in Section 2.4.
