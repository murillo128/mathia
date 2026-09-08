# ANF-118 — uniform Gaussian Gram comparison controls growing interior-saddle translation clouds

**Status:** `EXACT-DERIVED + UNIFORM-LAPLACE + FULL-MESOSCOPIC-PROFILE + GAUSSIAN-GRAM + CANCELLATION-SAFE + GROWING-CLOUD-EXCISION + EXPONENTIAL-WEIGHT-BOUNDARY`. `ANF-115` constructs distinct physical packets whose Montgomery--Taylor source mass concentrates at a stable interior saddle, while `ANF-117` shows that every fixed saddle-phase jet can vanish in a growing positive translation cloud without forcing source excision. The missing object can be controlled uniformly without truncating the phase jet.

Fix `gamma>0` and the exact `ANF-115` packet `P_A`. Put
\[
a=\frac2\pi\arctan\frac1{\pi\gamma},
\qquad
c=\frac{1+\pi^2\gamma^2}{2\gamma},
\qquad
E_A=E_0(P_A).
\]
For arbitrary real translations `tau_{j,A}` and positive integer weights `w_{j,A}`, let
\[
T_A=\bigsqcup_j w_{j,A}(P_A+\tau_{j,A}),
\qquad
p_A(\alpha)=\sum_jw_{j,A}e^{-2\pi i\alpha\tau_{j,A}},
\qquad
V_A=\sum_jw_{j,A},
\]
and define
\[
Z_A=\frac{E_0(T_A)}{E_A}.
\]
Then the complete mesoscopic profile is governed by the positive-semidefinite Gaussian Gram form
\[
\boxed{
\mathcal G_A=
\sum_{j,k}w_{j,A}w_{k,A}
e^{-2\pi^2(\tau_{j,A}-\tau_{k,A})^2/(cA)}
\cos\!\bigl(2\pi a(\tau_{j,A}-\tau_{k,A})\bigr).
}
\tag{1}
\]

There are constants `C,c_*,kappa>0`, depending only on `gamma`, such that for every `1<=U<=kappa A^(1/6)` and every physical translation cloud,
\[
\boxed{
|Z_A-\mathcal G_A|
\le
C\frac{1+U^3}{\sqrt A}\,\mathcal G_A
+
CV_A^2e^{-c_*U^2}.
}
\tag{2}
\]
Consequently, for every fixed `b>=0` and `d>0`,
\[
V_A\le A^b
\quad\Longrightarrow\quad
\boxed{
|Z_A-\mathcal G_A|
\le
C_{\gamma,b,d}\frac{(\log A)^{3/2}}{\sqrt A}\,\mathcal G_A
+
C_{\gamma,b,d}A^{-d}.
}
\tag{3}
\]
More generally,
\[
\log(e+V_A)=o(A^{1/3})
\quad\Longrightarrow\quad
\boxed{
|Z_A-\mathcal G_A|=o(1)\mathcal G_A+o(1).
}
\tag{4}
\]

Thus, throughout this subexponential envelope, source excision of a same-saddle translation aggregate is equivalent to vanishing of one explicit full-profile Gaussian quadratic form. This remains valid for arbitrary growing translation ranges, repeated sites, and arbitrarily deep finite saddle-jet cancellation. The result also has a sharp scope boundary: positive clouds with weight `V_A=exp(Theta(A))` can move the physical saddle itself, and then the fixed-saddle Gaussian proxy has the wrong exponential rate.

## 1. The exact physical packet has a multiplicative Gaussian density on a widening window

Retain the `ANF-115` notation
\[
F_\gamma(x)=x+2\gamma\log\cos\frac{\pi x}{2},
\qquad
F_\gamma'(a)=0,
\qquad
F_\gamma''(a)=-c.
\tag{5}
\]
Let
\[
d\nu_A(\alpha)
=
\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{E_A}\,d\alpha.
\]
This probability measure is even. Condition it on `alpha>0`, put
\[
u=\sqrt A(\alpha-a),
\]
and denote the resulting probability density by `f_A(u)`, extended by zero outside its physical interval. Let
\[
\varphi_c(u)=\sqrt{\frac c{2\pi}}e^{-cu^2/2}.
\tag{6}
\]

The weak Gaussian limit in `ANF-117` can be strengthened to the uniform multiplicative estimate
\[
\boxed{
\sup_{|u|\le U}
\left|
\frac{f_A(u)}{\varphi_c(u)}-1
\right|
\le
C\frac{1+U^3}{\sqrt A},
\qquad
1\le U\le\kappa A^{1/6},
}
\tag{7}
\]
together with the two-sided tail bound
\[
\boxed{
\int_{|u|>U}(f_A(u)+\varphi_c(u))\,du
\le
Ce^{-c_*U^2}.
}
\tag{8}
\]

To see this directly from the physical product, write
\[
n=\lfloor\gamma A\rfloor,
\qquad
t_{k,A}=\frac12+A^{-2}3^{-k}.
\]
On a fixed neighborhood of `a` contained in `(0,1)`, the exact factorization of `ANF-115` gives
\[
\log\!\left(
\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{|P_A|^2}
\right)
=
AF_\gamma(\alpha)+B_A(\alpha),
\tag{9}
\]
where
\[
\begin{aligned}
B_A(\alpha)={}&
\log J_0(\alpha)-\log4
+2\log(1+e^{-A\alpha})\\
&+2(n-\gamma A)\log\cos(\pi\alpha/2)\\
&+2\sum_{k=1}^{n}
\left[
\log\cos(\pi\alpha t_{k,A})
-\log\cos(\pi\alpha/2)
\right].
\end{aligned}
\tag{10}
\]
All cosines in this fixed neighborhood are positive for large `A`. The floor coefficient is uniformly bounded, the total ternary perturbation is `O(A^-2)`, and `J_0` is smooth and positive at the interior saddle. Hence
\[
\sup_A\sup_{|\alpha-a|\le\delta}
\bigl(|B_A(\alpha)|+|B_A'(\alpha)|+|B_A''(\alpha)|\bigr)<\infty
\tag{11}
\]
for some fixed `delta=delta_gamma>0`, while `exp(B_A)` is bounded above and away from zero there.

For `alpha=a+u/sqrt(A)`, Taylor expansion of `F_gamma` and (11) give
\[
A(F_\gamma(\alpha)-F_\gamma(a))
=
-\frac{cu^2}{2}
+
O_\gamma\!\left(\frac{|u|^3}{\sqrt A}\right),
\]
and
\[
B_A(\alpha)-B_A(a)
=
O_\gamma\!\left(\frac{|u|}{\sqrt A}+\frac{u^2}{A}\right).
\]
Uniformly for `|u|<=kappa A^(1/6)`, after reducing `kappa` if necessary, the combined logarithmic error is bounded and equals
\[
O_\gamma\!\left(\frac{|u|+|u|^3}{\sqrt A}\right).
\]
Integrating this expansion against a Gaussian majorant shows that the positive-saddle normalization differs from its Gaussian normalization by `O_gamma(A^-1/2)`. Exponentiating then yields (7).

The tail estimate (8) is also uniform. Strict concavity of `F_gamma` gives quadratic decay inside a fixed saddle neighborhood and a fixed exponential gap outside it. Before `alpha=1-A^-1`, the perturbed factors satisfy
\[
0<\cos(\pi\alpha t_{k,A})
\le
\cos(\pi\alpha/2),
\]
and the floor error costs only a polynomial factor, which is absorbed by the fixed exponential gap. In the endpoint layer `1-A^-1<alpha<1`, every cosine factor has modulus `O(A^-1)`, so their product contributes
\[
\exp[-2\gamma A\log A+O(A)],
\]
which is superexponentially negligible relative to the interior saddle. Near zero, `cosh^2(A alpha/2)<=e^(A alpha)` and `F_gamma(a)>F_gamma(0)=0` supply the missing fixed gap. These regions combine with the local quadratic bound to prove (8). No logarithm is taken through the tiny endpoint zero crossings.

## 2. Comparing the complete modulation before expansion gives the cancellation-safe bound

Because all translations and weights are real,
\[
|p_A(-\alpha)|=|p_A(\alpha)|.
\]
Evenness of `nu_A` therefore gives the exact identity
\[
\boxed{
Z_A
=
\int_{\mathbb R}
\left|
p_A\!\left(a+\frac{u}{\sqrt A}\right)
\right|^2
f_A(u)\,du.
}
\tag{12}
\]

Replacing `f_A` by its Gaussian model can be integrated exactly before any expansion of the cancelling sum:
\[
\begin{aligned}
\int_{\mathbb R}
\left|
p_A\!\left(a+\frac{u}{\sqrt A}\right)
\right|^2
\varphi_c(u)\,du
&=
\sum_{j,k}w_jw_k
e^{-2\pi^2(\tau_j-\tau_k)^2/(cA)}
e^{-2\pi ia(\tau_j-\tau_k)}\\
&=\mathcal G_A.
\end{aligned}
\tag{13}
\]
The left side is nonnegative, so (13) also proves directly that the real matrix in (1) is positive semidefinite despite its possibly negative off-diagonal entries.

On `|u|<=U`, equation (7) bounds the error by
\[
C\frac{1+U^3}{\sqrt A}
\int_{|u|\le U}|p_A(a+u/\sqrt A)|^2\varphi_c(u)\,du
\le
C\frac{1+U^3}{\sqrt A}\mathcal G_A.
\]
On the complement, `|p_A|<=V_A` and (8) give
\[
CV_A^2e^{-c_*U^2}.
\]
This proves (2). The order of operations is essential: a termwise approximation of the Gram entries followed by a triangle inequality would pay `V_A^2` even on the saddle window and would lose precisely in the high-cancellation regime exposed by `ANF-117`.

If `V_A<=A^b`, take `U^2=K log A` with `c_*K>2b+d`. Then `U=o(A^(1/6))`,
\[
\frac{1+U^3}{\sqrt A}
=
O\!\left(\frac{(\log A)^{3/2}}{\sqrt A}\right),
\]
and the tail is `O(A^-d)`, proving (3).

For the larger envelope (4), choose `U_A` so that
\[
\log(e+V_A)=o(U_A^2),
\qquad
U_A^2=o(A^{1/3}).
\]
Such a choice exists exactly under the stated hypothesis. Then the local multiplicative error tends to zero and the tail term is `o(1)`, proving (4).

A useful reformulation is therefore
\[
Z_A\to0
\quad\Longleftrightarrow\quad
\mathcal G_A\to0
\tag{14}
\]
for every cloud satisfying (4)'s growth envelope. Conversely, whenever `liminf G_A>0`,
\[
\frac{Z_A}{\mathcal G_A}\to1.
\tag{15}
\]
This is the full mesoscopic replacement for every fixed saddle jet.

## 3. The comparison survives the ANF-117 controls but fails at exponential cloud weight

For the `ANF-117` order-`s` root cloud,
\[
p_A(\alpha)
=
\left[
\sum_{j=0}^{r_A-1}
e^{-2\pi i\alpha j/(r_Aa)}
\right]^s,
\qquad
\frac{r_A}{\sqrt A}\to\rho,
\]
all saddle derivatives below order `s` vanish exactly. On the mesoscopic coordinate,
\[
p_A(a+u/\sqrt A)\to\left(\frac{\rho u}{a}\right)^s.
\]
Equation (13) therefore recovers the existing calibration
\[
\boxed{
\mathcal G_A
\longrightarrow
\frac{\rho^{2s}(2s-1)!!}{a^{2s}c^s}>0,
}
\tag{16}
\]
so (3) correctly classifies these clouds as non-excisable at scale `E_A` even though every prescribed finite phase jet can be zero.

The growth restriction is not cosmetic. Fix `lambda>0` and take the positive physical binomial cloud
\[
p_A(\alpha)
=
(1+e^{-\pi i\alpha})^{\lfloor\lambda A\rfloor},
\qquad
V_A=2^{\lfloor\lambda A\rfloor}.
\tag{17}
\]
Multiplication by this cloud adds `lambda A+O(1)` half-step factors to the exact packet. Writing
\[
f_g=F_g(a_g),
\qquad
a_g=\frac2\pi\arctan\frac1{\pi g},
\]
Laplace's principle gives the true source-ratio exponent
\[
\boxed{
\lim_{A\to\infty}\frac1A\log Z_A
=
2\lambda\log2+f_{\gamma+\lambda}-f_\gamma.
}
\tag{18}
\]

The fixed-saddle Gaussian form instead has exponent
\[
\boxed{
\lim_{A\to\infty}\frac1A\log\mathcal G_A
=
\sup_{x\in\mathbb R}
\left\{
2\lambda\log2
+2\lambda\log|\cos(\pi x/2)|
-\frac c2(x-a)^2
\right\}.
}
\tag{19}
\]
The proxy objective is even under the period-two reflection and has a unique maximizer `x_*` in `(0,a)`. On this interval,
\[
|F_\gamma''(x)|<|F_\gamma''(a)|=c,
\]
so strict integration of the curvature inequality yields
\[
F_\gamma(x)-f_\gamma
>
-\frac c2(x-a)^2
\qquad(0<x<a).
\tag{20}
\]
Evaluating the exact rate function at `x_*` shows that the exponent in (18) is strictly larger than the exponent in (19). Hence `Z_A/G_A` has exponential growth: a fixed Gaussian saddle cannot remain a relative approximation once the cloud itself carries `exp(Theta(A))` weight and shifts the dominant saddle. This is a matched control against extrapolating (2)--(4) beyond their actual window.

## 4. Fixed-notch invisibility extends to every admitted source-heavy cloud

Let `0<eta<a` be fixed and use the same triangular notch energy `E_eta` as `ANF-099`. `ANF-115` gives
\[
\frac{E_\eta(P_A)}{E_A}
=
\exp[-d_{\eta,\gamma}A+o(A)],
\qquad
d_{\eta,\gamma}=F_\gamma(a)-F_\gamma(\eta)>0.
\tag{21}
\]
Since `|p_A(alpha)|<=V_A`,
\[
\boxed{
\frac{E_\eta(T_A)}{E_A}
\le
V_A^2\exp[-d_{\eta,\gamma}A+o(A)].
}
\tag{22}
\]
Under `log(e+V_A)=o(A^(1/3))`, the right side tends to zero exponentially. Thus every source-heavy cloud detected by a nonvanishing Gaussian Gram form remains asymptotically invisible to any fixed notch lying strictly inside the saddle.

This does not prove that such a source-heavy cloud can be deleted from a global near-extremizer. Its source norm can still be cancelled by an external remainder, and the affine denominator must remain unchanged in any completion argument. What is now closed is the **internal same-saddle phase-recycling problem**: any polynomial or admitted subexponential family of translates can be aggregated first, and its complete source remainder is decided by `G_A`, not by a phasor or a finite collection of derivatives.

## 5. Prior-art boundary, adversarial checks, and research consequence

The local ingredient is the classical nondegenerate Laplace method, and (13) is the elementary Fourier transform of a Gaussian/Gram-matrix identity. A targeted prior-art check of standard Laplace/saddle-point references and Gaussian positive-definite kernels found these general ingredients but not a theorem that directly supplies the cloud-uniform comparison (2) for the exact `ANF-115` packet. No external theorem is load-bearing: (7)--(8) are reconstructed from the exact packet product, and (13) is evaluated directly. This is therefore a Mathia-specific quantitative specialization, not a claim that uniform Laplace asymptotics or Gaussian Gram positivity are new.

Several failure modes are explicit. Constants depend on fixed `gamma`; the proof is not uniform when `a_gamma` approaches zero or the spectral endpoint. The theorem treats translates of one packet shape and one saddle parameter, not mixtures of different `gamma` values. It controls source energy relative to `E_A`, not automatically relative to an arbitrary ambient affine scale. It does not produce a fatal near-extremizer, improve an unconditional zero proportion, bound `beta_eta`, or imply RH. Equation (17) shows that unrestricted exponential cloud growth is actually false, rather than merely unproved.

The live frontier is correspondingly sharper. `ANF-117` showed that finite saddle jets lose the `A^-1/2` profile; the present result captures that entire profile uniformly for all subexponentially weighted same-saddle translation clouds up to the stated envelope. Any remaining fatal mechanism must now enter through coupling to an external near-extremal remainder, a different packet/saddle family, or a regime large enough to alter the saddle itself. Replacing the complete Gaussian Gram observable by another finite jet cannot close that remaining gap.
