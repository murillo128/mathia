# XF-090 — Polymath reference subtraction leaves a xi-log-squared Volterra forcing

**Status:** `EXACT-DERIVED` + `STRUCTURAL/BRIDGE-CORRECTION` + `FORCED-VOLTERRA` + `NONPERTURBATIVE-GUARDED-DEFECT`. XF-089 shows that the Polymath15 high-line reference freezes the complete degree-`-1` endpoint sector of the Xi carrier: the residue remains exactly `-1/4` for every `0<=t<=1/2`, so the logarithmic mesh counterterm of XF-088 has a time-independent coefficient. That makes dynamic reference subtraction the natural way to remove the singular endpoint before comparing the continuum Volterra flow with the XF-087 periodic trapezoid.

There is, however, a second dynamic term that cannot be dropped. The explicit Polymath reference `M_t` is an asymptotic model for `H_t`; it is **not itself an exact solution of the heat equation**. Its normalized heat defect can be computed exactly. After the XF-051 positive-frequency transform, this defect becomes a deterministic forcing in the residual Volterra equation. Near the endpoint that forcing has the sharp form

\[
\boxed{
\mathcal D_t(\xi)
=
\frac{t}{16}\,\xi
\bigl(\log\xi+\gamma+\log(4\pi)\bigr)^2
+O_t(\xi),
\qquad \xi\downarrow0.
}
\tag{1}
\]

Thus reference subtraction removes the `1/xi` pole but does **not** leave a homogeneous Volterra problem. More importantly, `(1)` is small pointwise yet not perturbative in the destination-matched guarded resource. On the canonical Xi mesh, the single block `m\asymp q` already gives

\[
\boxed{
\mathcal R_{[q,2q]}(\mathcal D_t)
\asymp_{g,t_0}
(\log q)^4
\qquad
(t_0\le t\le1/2),
}
\tag{2}
\]

for every fixed `t_0>0`. Hence a continuum-to-periodic theorem that subtracts `M_t` and then evolves only the residual by the **homogeneous** XF-087 trapezoid has a diverging guarded vector-field mismatch. The deterministic reference forcing must either be transported explicitly on both sides or removed by a genuinely heat-compatible reference.

## 1. Exact normalized heat defect of the Polymath reference

Use the notation of XF-089. On `3<a<4`, put

\[
s=s_a(x):=\frac{1+a-ix}{2},
\qquad
B_{t,a}(x):=M_t(s_a(x)),
\tag{3}
\]

with

\[
M_t(s)=\exp\!\left(\frac t4\alpha(s)^2\right)M_0(s),
\qquad
\alpha(s):=(\log M_0)'(s).
\tag{4}
\]

Write

\[
\beta_t(s):=\partial_s\log M_t(s)
=\alpha(s)+\frac t2\alpha(s)\alpha'(s).
\tag{5}
\]

Because `partial_x=(-i/2)partial_s`, an exact heat solution in this coordinate would satisfy `partial_t M=(1/4)partial_s^2 M`. Define the normalized reference defect

\[
\mathfrak e_t(s)
:=
\frac1{M_t(s)}
\left(
\partial_tM_t(s)-\frac14\partial_s^2M_t(s)
\right).
\tag{6}
\]

Equations `(4)`--`(5)` give, with no asymptotic approximation,

\[
\mathfrak e_t
=\frac14\bigl(\alpha^2-\beta_t^2-\beta_t'\bigr).
\tag{7}
\]

Expanding this identity gives the useful explicit formula

\[
\boxed{
\mathfrak e_t
=
-\frac14\alpha'
-\frac t4\alpha^2\alpha'
-\frac{t^2}{16}\alpha^2(\alpha')^2
-\frac t8\bigl((\alpha')^2+\alpha\alpha''\bigr).
}
\tag{8}
\]

This is the exact quantity that measures the fact that the Polymath `M_t` is a high-line asymptotic reference rather than an exact caloric reference.

Let

\[
q^M_{t,a}:=\partial_x\log B_{t,a}.
\tag{9}
\]

Since

\[
\frac{\partial_tB_{t,a}+\partial_x^2B_{t,a}}{B_{t,a}}
=\mathfrak e_t(s_a(x)),
\tag{10}
\]

the logarithmic derivative satisfies the **forced** Burgers identity

\[
\boxed{
\partial_tq^M_{t,a}
+\partial_x^2q^M_{t,a}
+2q^M_{t,a}\partial_xq^M_{t,a}
=
\partial_x\mathfrak e_t(s_a(x)).
}
\tag{11}
\]

The sign can be checked directly from `B_xx/B=q_x+q^2`. If the right side vanished, `(11)` would reduce to the exact XF-051 Burgers equation for `H_t`.

## 2. Reference subtraction gives an exact forced triangular Volterra equation

Use the XF-051 carrier normalization

\[
\mathcal Z_t^M(\xi)
:=
\frac{i}{2\pi}e^{a\xi}\widehat{q^M_{t,a}}(\xi),
\qquad \xi>0.
\tag{12}
\]

Transforming `(11)` in exactly the same convention as XF-051 gives

\[
\boxed{
\partial_t\mathcal Z_t^M
=
\xi^2\mathcal Z_t^M
-\xi(\mathcal Z_t^M*\mathcal Z_t^M)
+\mathcal D_t,
}
\tag{13}
\]

where the deterministic reference forcing is

\[
\boxed{
\mathcal D_t(\xi)
:=-\frac{\xi}{2\pi}e^{a\xi}
\widehat{\mathfrak e_t(s_a(\cdot))}(\xi).
}
\tag{14}
\]

The actual Xi carrier `mathcal Z_t` satisfies the homogeneous XF-051 Volterra equation. Therefore, with the XF-089 residual

\[
\mathcal R_t:=\mathcal Z_t-\mathcal Z_t^M,
\tag{15}
\]

one gets the exact residual evolution

\[
\boxed{
\partial_t\mathcal R_t
=
\xi^2\mathcal R_t
-\xi\bigl(
2\mathcal Z_t^M*\mathcal R_t
+\mathcal R_t*\mathcal R_t
\bigr)
-\mathcal D_t.
}
\tag{16}
\]

This remains one-sided and triangular in positive frequency, so the useful Volterra geometry survives reference subtraction. What changes is that the residual is **forced**, not homogeneous. The forcing is fully deterministic and depends only on the explicit reference.

## 3. The forcing has a universal `xi log^2 xi` endpoint cusp

Set

\[
b:=1+a,
\qquad
w:=b-ix=2s_a(x),
\qquad
\ell(x):=\Log\frac{w}{4\pi}.
\tag{17}
\]

From the explicit Polymath logarithmic derivative used in XF-089,

\[
\alpha(s)
=
\frac12\Log\frac{s}{2\pi}
+\frac{3}{2s}
+O(s^{-2}),
\tag{18}
\]

and therefore

\[
\alpha'(s)=\frac1{2s}+O(s^{-2}),
\qquad
\alpha''(s)=-\frac1{2s^2}+O(s^{-3}).
\tag{19}
\]

Substituting `(18)`--`(19)` into the exact defect `(8)` yields, uniformly for `0<=t<=1/2`,

\[
\boxed{
\mathfrak e_t(s_a(x))
=
-\frac1{4w}
-\frac{t}{16}\frac{\ell(x)^2}{w}
+O_t\!\left(\frac{\log^2(2+|x|)}{1+x^2}\right).
}
\tag{20}
\]

The remainder is integrable on the high line. The two positive-frequency transforms needed for the singular terms follow from the same analytic family used in XF-089:

\[
\widehat{\frac1{b-i\cdot}}(\xi)
=2\pi e^{-b\xi},
\qquad \xi>0,
\tag{21}
\]

and

\[
\boxed{
\widehat{
\frac{\Log^2((b-i\cdot)/(4\pi))}{b-i\cdot}
}(\xi)
=
2\pi e^{-b\xi}
\left[
\bigl(\log\xi+\gamma+\log(4\pi)\bigr)^2
-\frac{\pi^2}{6}
\right].
}
\tag{22}
\]

For `(22)`, differentiate twice at `nu=1` the standard transform

\[
\widehat{(b-i\cdot)^{-\nu}}(\xi)
=
\frac{2\pi}{\Gamma(\nu)}e^{-b\xi}\xi^{\nu-1},
\qquad \xi>0,
\tag{23}
\]

and then shift the logarithm by `log(4 pi)`. The `-pi^2/6` term is `-psi_1(1)`.

Inserting `(20)`--`(22)` into `(14)` and using `b-a=1` gives

\[
\mathcal D_t(\xi)
=
\frac{\xi}{4}e^{-\xi}
+
\frac{t\xi}{16}e^{-\xi}
\left[
\bigl(\log\xi+\gamma+\log(4\pi)\bigr)^2
-\frac{\pi^2}{6}
\right]
+O_t(\xi).
\tag{24}
\]

The final `O_t(xi)` includes the Fourier transform of the integrable remainder in `(20)`, so the complete constant coefficient of `xi` is not asserted by `(24)`. The logarithmic coefficients are unaffected. In particular,

\[
\boxed{
\mathcal D_t(\xi)
=
\frac{t}{16}\xi
\bigl(\log\xi+\gamma+\log(4\pi)\bigr)^2
+O_t(\xi),
}
\tag{25}
\]

which is `(1)`. At `t=0` the reference defect is only `O(xi)`; every fixed positive heat time creates the sharper `xi log^2 xi` cusp. Crucially, no new `1/xi` or `log xi` state singularity appears, so XF-089's frozen pole and XF-088's unique logarithmic mesh counterterm remain intact.

## 4. Pointwise smallness is not guarded-resource smallness

The cusp in `(25)` tends to zero as `xi->0`, but the XF-070/XF-079 selector norm differentiates strongly in the Vieta index. This makes the distinction between pointwise and guarded smallness load-bearing.

Use the canonical XF-071 scales

\[
M=q^2,
\qquad
N=2q^2,
\qquad
\Delta=\frac{2\pi}{L},
\qquad
\Delta^2\asymp q^{-3},
\tag{26}
\]

with grid frequencies `xi_m=m Delta`, source guard `J\asymp q^{1/4}`, and upper visible cutoff `K\asymp q\log\log T`. For all sufficiently large scales the block

\[
S_q:=\{m:\lceil q\rceil\le m\le\lfloor2q\rfloor\}
\tag{27}
\]

lies inside the visible band. On this block,

\[
\xi_m\asymp q^{-1/2},
\qquad
\log\xi_m=-\frac12\log q+O(1).
\tag{28}
\]

Hence for every fixed `t_0>0`, uniformly for `t_0<=t<=1/2`, equation `(25)` gives

\[
|\mathcal D_t(\xi_m)|
\asymp_{t_0}
q^{-1/2}(\log q)^2,
\qquad m\in S_q.
\tag{29}
\]

Measure this vector-field defect in the exact selector resource of XF-086,

\[
\mathcal R_S(Q)
:=
\frac1{4M^2}
\sum_{m\in S}|Q_m|^2 I_m,
\qquad
I_m:=\int_{-1}^1(\pi m+u)^4|\chi(u)|^2\,du.
\tag{30}
\]

For `m\asymp q`, one has `I_m\asymp_g q^4`. There are `asymp q` indices in `S_q`, while `M^2=q^4`. Combining this with `(29)` yields

\[
\boxed{
\mathcal R_{S_q}
\bigl((\mathcal D_t(\xi_m))_m\bigr)
\asymp_{g,t_0}
(\log q)^4.
}
\tag{31}
\]

This proves `(2)`. The mismatch actually diverges on a block far below the full cutoff `K`; no estimate involving only the extreme top of the visible cone is responsible.

Consequently the forcing cannot be hidden in the `o(1)` continuum-to-grid error budget used by XF-071 and XF-088. The fact that `mathcal D_t(xi)->0` pointwise is insufficient because the destination resource contains four selector derivatives plus the extra power-sum/log-Vieta factor encoded in `I_m`.

## 5. Falsification checks

There are four independent checks on the calculation.

First, setting `t=0` in `(8)` leaves `mathfrak e_0=-alpha'/4`; the `log^2` endpoint term disappears exactly, as `(25)` requires. Second, the high-line parameter cancels from the singular Fourier factors: `(20)` has physical decay `e^{-b xi}` while the XF-051 carrier contributes `e^{a xi}`, leaving the same `e^{-xi}` as in XF-089 because `b-a=1`. Third, differentiating the analytic-family transform once reproduces the XF-089 identity for `Log(b-ix)/(b-ix)`; differentiating twice gives `(22)` and fixes both the sign and `pi^2/6` constant. Fourth, direct symbolic expansion of `(7)` with `beta_t=alpha+(t/2)alpha alpha'` reproduces every term in `(8)`; numerical evaluation of the exact alpha formula on `3<a<4` confirms the asymptotic `(20)` with relative error tending to zero at large `|x|`.

The potential failure mode would be cancellation of the `xi log^2 xi` coefficient by the remainder in `(20)`. This cannot occur: that remainder is `L^1` in `x`, so its Fourier transform is bounded at `xi=0`, and multiplication by the carrier factor `xi` contributes only `O(xi)`. Thus the coefficient `t/16` in `(25)` is invariant under all lower-order high-line terms.

## 6. Prior-art boundary

The load-bearing external definition is the same D. H. J. Polymath reference already anchored in `research/xi_flow/SOURCES.md`: *Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn-Newman constant*, Research in the Mathematical Sciences 6 (2019), article 31. XF-089 already records the explicit `M_t` and `alpha` formulas and the high-line quotient estimate from Proposition 9.1(ii).

The passage from a multiplicative heat defect to a forced logarithmic Burgers equation is classical Cole--Hopf algebra. The line-specific content here is the exact defect `(8)` of this particular Polymath reference, its positive-frequency endpoint law `(25)`, and the guarded Xi-scale lower bound `(31)`. A targeted literature search found no de Bruijn--Newman result formulating the Polymath high-line reference subtraction as this forced Volterra system or identifying the resulting `xi log^2 xi` forcing and its nonperturbative guarded resource. The proof is self-contained once the already-anchored `M_t` definition is accepted, so `SOURCES.md` needs no new entry.

## 7. Consequence for `xi_flow`

XF-087 says the periodic power-sum flow is exactly the homogeneous trapezoidal semidiscretization of the Xi Volterra equation. XF-088 and XF-089 then make it natural to remove the endpoint pole with a dynamic analytic reference. XF-090 shows the precise limitation of that move:

\[
\boxed{
\text{dynamic Polymath-reference subtraction}
\neq
\text{homogeneous residual heat transport}.
}
\tag{32}
\]

The residual still has excellent one-sided Volterra structure, but it carries the explicit deterministic forcing `(14)`. Because `(31)` is not perturbative, a viable source-to-periodic theorem must do one of two things: include a discretization of `mathcal D_t` exactly enough that continuum and periodic forced systems share the same deterministic reference dynamics, or replace `M_t` by a reference that solves the heat equation exactly while retaining the endpoint and high-line control needed by XF-089. Simply feeding residual moments into the unforced equal-weight carrier of XF-085--XF-087 is not justified.

This sharpens rather than reopens the static carrier gate. XF-085--XF-086 still give exact equal-weight realization once the finite visible state has controlled guarded resource, and XF-087 still gives the correct homogeneous evolution for a total periodic carrier. The remaining source bridge is now explicit: **renormalize the endpoint, match the deterministic reference forcing, and prove guarded continuum-to-grid stability only for the genuinely Xi-specific remainder**. The separate implication from a hypothetical positive `Lambda` transition to nontrivial destination guarded mass remains untouched.