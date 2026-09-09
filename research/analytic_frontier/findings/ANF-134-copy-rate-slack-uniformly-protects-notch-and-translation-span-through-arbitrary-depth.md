# ANF-134 — copy-rate slack uniformly protects notch and translation span through arbitrary depth

**Status:** `EXACT-DERIVED + DEPTH-UNIFORM-INVARIANT + POSITIVE-TRANSLATION-CASCADE + COPY-RATE-SLACK + FIXED-NOTCH-DARK + LOGARITHMIC-SPAN-LAW + SOURCE-PREFACTOR-GATE`. `ANF-133` shows that the critical positive saddle-annihilator construction can be iterated to every fixed finite depth while preserving bounded macroscopic source and exponential affine/cardinality slack. Its explicit boundary is depth uniformity: as the depth grows, the central notch, annihilator shifts, chamber count, Laplace constants, and physical translation span were all left as potentially deteriorating quantities.

Two of those apparent failure modes are not independent. For every positive-translation cascade built on the `ANF-115` packet, the single scalar

\[
\boxed{
\delta:=f_\gamma-2R
}
\tag{1}
\]

— the remaining copy-rate slack below the source-critical ceiling — controls both the central notch and the translation geometry. At the limiting-pressure level,

\[
\boxed{
G(\alpha)\le F_\gamma(\alpha)-\delta\le \alpha-\delta,
\qquad 0\le\alpha<1.
}
\tag{2}
\]

Consequently every source-critical chamber satisfies `xi>=delta`; every positive saddle-annihilator shift `tau=1/(2xi)` is at most `1/(2delta)`; and the whole interval `0<=alpha<=delta/2` has pressure at most `-delta/2`.

More importantly, the notch conclusion has an **exact finite-`A` version that is independent of cascade depth and chamber count**. If a positive translation cloud of the base packet has total coefficient/copy mass `V_A` and

\[
\limsup_{A\to\infty}\frac1A\log V_A
\le \frac{f_\gamma-\delta_*}{2}
\tag{3}
\]

for some fixed `delta_*>0`, then for every fixed `0<eta<delta_*`,

\[
\boxed{
\limsup_{A\to\infty}
\frac1A\log\frac{E_\eta(X_A)}{E_A}
\le \eta-\delta_*<0.
}
\tag{4}
\]

Thus an arbitrarily deep diagonal cascade `D=D(A)->infinity` with a uniform copy-rate slack automatically retains a fixed exponentially dark central notch. No uniform control of the number, curvature, or Laplace constants of its regenerated chambers is needed for this statement.

The same slack gives an integrated physical span law for the `ANF-133` retuning steps. If `delta_d` is the slack after the `d`th critical retuning layer, then the total additional positive translation span of all annihilator layers through depth `D` satisfies

\[
\boxed{
\frac{\operatorname{Span}_{\rm ann}(D,A)}{A}
\le
\frac1{4\log2}
\log\frac{\delta_0}{\delta_D}.
}
\tag{5}
\]

In particular, if `inf_D delta_D>=delta_*>0`, the entire annihilator cascade has `O_{gamma,delta_*}(A)` horizontal span **uniformly in depth**, even if the number of critical chambers proliferates. If the span does diverge through this mechanism, the copy-rate slack must simultaneously collapse toward zero. The remaining depth-uniform obstruction in `ANF-133` is therefore narrower than it first appears: it is enough to understand whether the critical retuning exhausts the scalar budget `delta`, and whether the total source mass/Laplace prefactor remains uniformly macroscopic. Notch collapse and translation-span growth are consequences of budget saturation, not separate free pathologies.

## 1. Positive translation factors have a universal pressure ceiling

Keep the `ANF-115` notation

\[
F_\gamma(\alpha)
=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2},
\qquad
f_\gamma=\max_{0<\alpha<1}F_\gamma(\alpha)>0.
\tag{6}
\]

Consider any finite positive-translation pressure architecture

\[
G(\alpha)
=
F_\gamma(\alpha)-f_\gamma
+2\sum_{\ell=1}^{L}r_\ell\log|P_\ell(\alpha)|,
\tag{7}
\]

where

\[
P_\ell(\alpha)
=
\sum_v c_{\ell,v}e^{-2\pi i t_{\ell,v}\alpha},
\qquad
c_{\ell,v}>0,
\qquad
V_\ell:=P_\ell(0)=\sum_v c_{\ell,v},
\tag{8}
\]

and

\[
R:=\sum_{\ell=1}^{L}r_\ell\log V_\ell.
\tag{9}
\]

The triangle inequality gives the exact pointwise estimate

\[
|P_\ell(\alpha)|\le V_\ell.
\tag{10}
\]

Define the copy-rate slack by (1). Then (7)--(10) imply

\[
G(\alpha)
\le
F_\gamma(\alpha)-f_\gamma+2R
=
F_\gamma(\alpha)-\delta.
\tag{11}
\]

Since

\[
\log\cos\frac{\pi\alpha}{2}\le0
\qquad(0\le\alpha<1),
\]

one also has the elementary but decisive bound

\[
F_\gamma(\alpha)\le\alpha.
\tag{12}
\]

Combining (11) and (12) proves (2). In particular, for every `0<eta<delta`,

\[
\boxed{
\sup_{0\le\alpha\le\eta}G(\alpha)
\le -(\delta-\eta).
}
\tag{13}
\]

Choosing `eta=delta/2` gives a pressure gap at least `delta/2` on the whole positive half of the central notch; conjugation symmetry supplies the negative half.

This identifies `delta` intrinsically as more than copy-count bookkeeping. In the `ANF-133` setting all translation factors have zero logarithmic derivative at the origin, so

\[
G(0)=-\delta,
\qquad
G'_+(0)=1.
\tag{14}
\]

Thus `delta` is exactly the pressure deficit at the origin. The strict ceiling `R<f_gamma/2` in `ANF-133` is equivalently `delta>0`.

## 2. A source-critical chamber cannot approach the origin faster than the slack

Assume now that (7) is source-critical,

\[
\sup_{0\le\alpha<1}G(\alpha)=0,
\tag{15}
\]

and let `xi` be any finite interior maximizer. Equations (11) and (15) give

\[
0=G(\xi)
\le F_\gamma(\xi)-\delta,
\]

hence

\[
F_\gamma(\xi)\ge\delta.
\tag{16}
\]

Using (12),

\[
\boxed{
\xi\ge\delta.
}
\tag{17}
\]

There is also an upper compactness bound. Because `F_gamma(alpha)->-infinity` as `alpha->1-`, the positive superlevel set

\[
K_{\gamma,\delta}
:=\{\alpha\in(0,1):F_\gamma(\alpha)\ge\delta\}
\tag{18}
\]

is compact. If

\[
b_\gamma(\delta):=\sup K_{\gamma,\delta}<1,
\]

then every critical chamber lies in

\[
\boxed{
\delta\le\xi\le b_\gamma(\delta)<1.
}
\tag{19}
\]

The positive annihilator used by `ANF-133` places at such a chamber the binomial

\[
1+e^{-2\pi i\tau\alpha},
\qquad
\tau=\frac1{2\xi}.
\tag{20}
\]

Therefore

\[
\boxed{
\frac1{2b_\gamma(\delta)}
\le\tau\le\frac1{2\delta}.
}
\tag{21}
\]

So a lower bound on copy-rate slack automatically prevents the saddle skeleton from colliding with the origin or the endpoint and prevents the physical annihilator shifts from escaping to infinity. Chamber proliferation can still occur, but it cannot by itself create unbounded individual shifts while `delta` stays positive.

## 3. The fixed-notch estimate survives arbitrary diagonal depth

The pressure argument above is already depth-free, but positivity gives a stronger finite-scale statement that does not require the final cascade to admit a uniform Laplace expansion.

Let `P_A=P_{A,floor(gamma A)}` be the base `ANF-115` packet, with

\[
E_A:=E_0(P_A).
\tag{22}
\]

Let `X_A` be **any** positive translation cloud of `P_A`, with multiplier

\[
M_A(\alpha)
=
\sum_v c_{A,v}e^{-2\pi i t_{A,v}\alpha},
\qquad
c_{A,v}\ge0,
\]

and total coefficient mass

\[
V_A:=M_A(0)=\sum_v c_{A,v}.
\tag{23}
\]

Positivity gives exactly

\[
|M_A(\alpha)|\le V_A.
\tag{24}
\]

Hence for a fixed central notch `|alpha|<=eta`,

\[
E_\eta(X_A)
\le
V_A^2E_\eta(P_A).
\tag{25}
\]

The exact packet asymptotics used throughout `ANF-115` give, for fixed `eta<1`,

\[
\limsup_{A\to\infty}
\frac1A\log\frac{E_\eta(P_A)}{E_A}
\le
\sup_{0\le\alpha\le\eta}F_\gamma(\alpha)-f_\gamma.
\tag{26}
\]

By (12), the right side is at most `eta-f_gamma`. Combining (25), (26), and the copy-rate hypothesis (3) yields

\[
\limsup_{A\to\infty}
\frac1A\log\frac{E_\eta(X_A)}{E_A}
\le
(f_\gamma-\delta_*)+(\eta-f_\gamma)
=
\eta-\delta_*.
\tag{27}
\]

This proves (4).

The quantifier is the useful part. The multiplier `M_A` may contain a number of factors or retuning layers that grows with `A`; its zero set, chamber count, and local Hessians may all vary. None of them enter (24)--(27). Therefore, for a diagonal `ANF-133` cascade through depth `D(A)`, a uniform terminal slack

\[
\delta_{D(A)}\ge\delta_*>0
\tag{28}
\]

already implies a single fixed exponentially dark notch, for example

\[
\eta=\frac{\delta_*}{2},
\qquad
E_\eta(X_A)
\le
\exp[-(\delta_*/2+o(1))A]E_A.
\tag{29}
\]

This conclusion does **not** assume a depth-uniform source lower bound for `X_A`; it says that if the total source remains macroscopic, it cannot hide in a collapsing central chamber while the copy-rate slack stays positive.

## 4. Retuning spends slack and translation span in the same currency

Now specialize to the iterative saddle-annihilator step of `ANF-133`. Suppose stage `d-1` is source-critical with copy rate `R_{d-1}`, slack

\[
\delta_{d-1}=f_\gamma-2R_{d-1}>0,
\tag{30}
\]

and positive critical skeleton

\[
\mathcal K_{d-1}
=\{\xi_{1,d-1},\ldots,\xi_{J_{d-1},d-1}\}.
\tag{31}
\]

The annihilator is

\[
Q_{d-1}(\alpha)
=
\prod_{j=1}^{J_{d-1}}
\left(
1+e^{-2\pi i\alpha/(2\xi_{j,d-1})}
\right),
\tag{32}
\]

and the first critical retuning density supplied by `ANF-133` is `theta_d>0`. Its coefficient mass is `2^{J_{d-1}}`, so

\[
R_d
=R_{d-1}+\theta_dJ_{d-1}\log2.
\tag{33}
\]

Equivalently,

\[
\boxed{
\delta_d
=
\delta_{d-1}
-2\theta_dJ_{d-1}\log2.
}
\tag{34}
\]

The slack is therefore a monotone Lyapunov budget for the retuning. Summing (34) gives the exact weighted-layer identity

\[
\boxed{
\sum_{d=1}^{D}
\theta_dJ_{d-1}
=
\frac{\delta_0-\delta_D}{2\log2}.
}
\tag{35}
\]

At scale `A`, implement the layer with

\[
m_{d,A}:=\lfloor\theta_dA\rfloor
\tag{36}
\]

copies of the annihilator factor. Equation (17), applied at stage `d-1`, gives

\[
\tau_{j,d-1}
:=\frac1{2\xi_{j,d-1}}
\le\frac1{2\delta_{d-1}}.
\tag{37}
\]

The support of `Q_{d-1}` lies between zero and

\[
\sum_{j=1}^{J_{d-1}}\tau_{j,d-1},
\]

so the additional translation span created by its `m_{d,A}`th power is at most

\[
\begin{aligned}
\Delta\operatorname{Span}_{d,A}
&\le
m_{d,A}
\sum_{j=1}^{J_{d-1}}\tau_{j,d-1}\\
&\le
A\theta_d\frac{J_{d-1}}{2\delta_{d-1}}\\
&=
\frac{A}{4\log2}
\frac{\delta_{d-1}-\delta_d}{\delta_{d-1}}.
\end{aligned}
\tag{38}
\]

Because `0<delta_d<=delta_{d-1}`,

\[
1-\frac{\delta_d}{\delta_{d-1}}
\le
-\log\frac{\delta_d}{\delta_{d-1}}.
\tag{39}
\]

Summing (38)--(39) telescopes logarithmically:

\[
\begin{aligned}
\frac{\operatorname{Span}_{\rm ann}(D,A)}A
&\le
\frac1{4\log2}
\sum_{d=1}^{D}
\left(1-\frac{\delta_d}{\delta_{d-1}}\right)\\
&\le
\frac1{4\log2}
\sum_{d=1}^{D}
\log\frac{\delta_{d-1}}{\delta_d}\\
&=
\frac1{4\log2}
\log\frac{\delta_0}{\delta_D}.
\end{aligned}
\tag{40}
\]

This is (5). The initial critical digit block has its own `O(A)` translation span from `ANF-129`; adding that fixed first-stage contribution does not change the conclusion. In particular, if

\[
\delta_D\ge\delta_*>0
\]

for all stages under consideration, the total physical span remains `O(A)` with a constant independent of `D`. Conversely, any divergence of this upper bound is tied quantitatively to `delta_D->0`; chamber count `J_d` cancels from the integrated budget.

## 5. What this removes from the arbitrary-depth gate

`ANF-133` listed several quantities that might deteriorate when `d=d(A)->infinity`. Equations (4), (21), and (40) show that three of them are controlled by one scalar condition:

- a fixed lower bound on `delta_d` gives a fixed exponentially dark central notch;
- it keeps every regenerated source chamber in a compact subinterval of `(0,1)` and every annihilator shift uniformly bounded;
- it keeps the **total**, not merely per-layer, annihilator translation span `O(A)` independently of the number of layers and chambers.

The unresolved issue is correspondingly sharper. One must now decide whether the critical retuning law can drive

\[
\delta_d=f_\gamma-2R_d\downarrow0,
\tag{41}
\]

or whether some structural mechanism leaves a positive residual budget. If a positive residual budget exists, central-notch collapse and unbounded translation geometry cannot be the reason an arbitrary-depth cascade fails.

Even that would not complete the construction. A pressure maximum equal to zero is only an exponential-scale statement. When the depth grows, the number of chambers may proliferate, their curvatures may become badly conditioned, and the finite-`A` floor errors in many small retuning densities may accumulate. Those effects can destroy a depth-uniform two-sided estimate

\[
E_0(X_A)\asymp E_A
\tag{42}
\]

even while (29) remains true. The genuine remaining local question is therefore **source prefactor/coercivity at growing depth**, together with the scalar saturation alternative (41), not an independent notch or span problem.

Nor does the present finding construct a fatal Montgomery--Taylor near-extremizer. It only shows that, within the positive same-profile exponential cascade opened by `ANF-129`--`ANF-133`, a substantial part of the previously listed depth-uniform geometry is already controlled.

## 6. Adversarial controls and evidence boundary

The positivity hypothesis is load-bearing. If signed or complex translation coefficients were allowed, `|P(alpha)|<=P(0)` could fail or `P(0)` could be small by cancellation, and the scalar copy-rate ceiling would no longer imply (2) or (4). The `ANF-129`--`ANF-133` architecture uses positive physical unions, so this is the correct class for the present application.

The source-critical hypothesis is needed for the chamber localization (16)--(21), but **not** for the finite-`A` notch inequality (4): that estimate uses only positivity and the total copy-rate bound. Conversely, (4) is an upper bound on central-notch source. It supplies no lower bound for total source energy and cannot replace the missing depth-uniform version of the fixed-depth Laplace argument in `ANF-133`.

The span law (5) is for the explicit `ANF-133` binomial annihilator layers with shifts `1/(2xi)`. It does not bound arbitrary extra translations inserted by a different architecture. Floors in `m_{d,A}=floor(theta_dA)` only decrease the displayed upper bound, so they do not invalidate (38); their effect on **critical source normalization** remains outside this result.

A direct falsification test is therefore precise: construct an `ANF-133`-type positive cascade with `inf_d delta_d>0` but either (i) a critical chamber `xi_d->0`, (ii) annihilator translation span growing faster than `A` after normalizing by the accumulated layers, or (iii) non-exponentially-dark source in the fixed notch `|alpha|<=delta_*/2`. Any of those would contradict respectively (17), (40), or (27). By contrast, a cascade with `delta_d->0` and collapsing notch is fully compatible with this finding.

The derivation is elementary once the `ANF-115` exponent and `ANF-133` copy-rate bookkeeping are available. A directed prior-art audit against classical Riesz-product/trigonometric-product estimates and the Laplace principle found only the standard ambient facts: positive trigonometric factors are bounded by their coefficient mass, and exponential integrals are controlled by their maximal exponent. No external theorem is imported here, and no novelty is claimed for those classical ingredients. The Mathia-specific contribution is the identification of `delta=f_gamma-2R` as a **single depth-uniform budget** simultaneously controlling fixed-notch darkness, critical-skeleton distance from the origin, and the accumulated physical span of the iterative saddle annihilators. No `SOURCES.md` change is required.

This theorem surface is exact but too elementary and application-specific to justify a separate Lean formalization handoff at this stage; the live difficulty is the next source-prefactor/saturation argument rather than verification of (10)--(40).

## Consequence for `analytic_frontier`

The next decisive test is now two-pronged but tightly coupled. First, study the scalar recursion (34) and determine whether `delta_d` can actually be exhausted by successive first-critical retunings. Second, conditional on a positive residual slack, attack the only remaining genuinely depth-sensitive local issue: a uniform lower/upper source-mass estimate despite proliferating chambers and increasingly small retuning densities.

If the residual slack stays positive and the source prefactor can be controlled, then the `ANF-133` construction already carries a fixed central notch and linear physical span through a diagonal depth `D(A)->infinity`. If the residual slack necessarily tends to zero, (34) identifies **copy-rate ceiling saturation** as the concrete mechanism that must be analyzed next. Either outcome is substantially sharper than treating notch width, shift growth, and translation span as unrelated arbitrary-depth failure modes.
