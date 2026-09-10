---
type: negative
research_line: xi_flow
finding_id: XF-164
status: canonical
---

# XF-164 — Analytic soft splicing preserves shifted nonreal zeros beyond every Xi tail scale

**Confidence:** high. The construction is explicit, positivity and all-time heat admissibility follow by domination by the Xi source, bounded-spacetime convergence follows from dominated convergence, and persistence of a chosen nonreal zero is a direct Rouché argument. The only external Xi fact used is the established Rodgers--Tao bound `Lambda_Xi >= 0`, already anchored in `SOURCES.md`. This finding does **not** produce a second theta kernel or alter the actual Xi source; it proves that even analytic source data agreeing with Xi beyond every fixed theta-tail scale can fail to determine the distinguished `t=0` zero geometry.

## Statement

XF-163 showed that the normalized Xi tail jet of XF-162 is blind to the Gaussian heat-origin gauge `rho(u) -> e^{-tau u^2}rho(u)`. A natural response is to strengthen the source data until the Gaussian tilt is detected, for example by retaining the full subleading tail rather than only the `e^{4u}`-normalized action/hazard/curvature.

That repair is still insufficient at the level of asymptotic tail information, even if one keeps strict positivity, real analyticity, and all finite positive heat times.

Fix any `tau>0`. For `R>0` define the even entire cutoff profile

\[
w_R(u):=\exp\!\bigl(-\exp(u^2-R^2)\bigr)
\tag{1}
\]

and the positive analytic multiplier

\[
q_{\tau,R}(u):=\exp\!\bigl(-\tau u^2 w_R(u)\bigr).
\tag{2}
\]

Set

\[
\boxed{
\rho_{\tau,R}(u):=\Phi(u)q_{\tau,R}(u),
}
\tag{3}
\]

where `Phi` is the Xi theta source. Then:

1. `rho_{tau,R}` is strictly positive and real analytic on the real axis, and

\[
e^{-\tau u^2}\Phi(u)\le \rho_{\tau,R}(u)\le\Phi(u).
\tag{4}
\]

Consequently it admits every finite quadratic heat multiplier just as Xi does.

2. For every fixed `R`, the source agrees with Xi at `+infinity` **beyond every fixed theta-exponential scale**. More precisely, for every fixed derivative order `j>=0` and every `c>0`,

\[
\boxed{
 e^{c e^{4u}}
 \frac{d^j}{du^j}
 \bigl(\log\rho_{\tau,R}(u)-\log\Phi(u)\bigr)
 \longrightarrow0
 \qquad (u\to+\infty).
}
\tag{5}
\]

In particular the complete algebraic `e^{-4u}` expansion from the dominant theta term and every fixed `e^{-c e^{4u}}` tail scale are unchanged by `(3)`.

3. Nevertheless, as `R->infinity`, the complete heat orbit of `(3)` converges locally uniformly on every bounded spacetime window to the **shifted Xi orbit**:

\[
\boxed{
\mathcal H^{(\tau,R)}_t(z)
:=\int_0^\infty e^{tu^2}\rho_{\tau,R}(u)\cos(zu)\,du
\longrightarrow
H_{t-\tau}(z)
}
\tag{6}
\]

uniformly for `t` in any compact real interval and `z` in any compact subset of `C`.

4. Since Rodgers--Tao gives `Lambda_Xi>=0`, `H_{-tau}` has at least one nonreal zero for every `tau>0`. Equation `(6)` and Rouché's theorem therefore imply that for every `tau>0` and all sufficiently large `R`,

\[
\boxed{
\mathcal H^{(\tau,R)}_0
\text{ has a nonreal zero.}
}
\tag{7}
\]

Thus **no source criterion that depends only on an arbitrarily detailed asymptotic germ at `+infinity` can force the distinguished `t=0` slice to be real-rooted**, even after adding positivity, real analyticity and all-time heat admissibility. The missing Xi rigidity must couple the tail to finite/mesoscopic source structure through an exact global identity, not merely describe the tail to higher asymptotic precision.

## 1. The analytic splice interpolates between the tilted core and the exact Xi tail asymptotically

For real `u`, `(1)` satisfies `0<w_R(u)<1`. Therefore

\[
e^{-\tau u^2}
\le
q_{\tau,R}(u)
\le1,
\tag{8}
\]

which proves `(4)`. Since both `w_R` and `q_{tau,R}` are even entire functions of `u`, multiplying by the real-analytic Xi source preserves strict positivity and real analyticity on the real axis.

For each fixed `u`,

\[
w_R(u)\longrightarrow1
\qquad (R\to\infty),
\tag{9}
\]

so

\[
q_{\tau,R}(u)\longrightarrow e^{-\tau u^2}.
\tag{10}
\]

On the other hand, for fixed `R` and `u->+infinity`,

\[
w_R(u)=\exp\!\bigl(-e^{u^2-R^2}\bigr)
\tag{11}
\]

is much smaller than every `exp(-c e^{4u})`. Since

\[
\log\rho_{\tau,R}(u)-\log\Phi(u)
=-\tau u^2 e^{-e^{u^2-R^2}},
\tag{12}
\]

we immediately obtain `(5)` for `j=0`: for every fixed `c>0`,

\[
c e^{4u}-e^{u^2-R^2}+O(\log u)\longrightarrow-\infty.
\tag{13}
\]

For a fixed derivative order `j`, differentiating `(12)` introduces only finite sums of polynomial factors in `u` and powers of `e^{u^2-R^2}` multiplying the same factor `e^{-e^{u^2-R^2}}`. Those factors remain negligible against the outer exponential in `(11)`, so the same comparison proves `(5)` for every fixed `j`.

This is substantially stronger than preserving the three normalized limits of XF-162/XF-163. For example, XF-162 has

\[
\log\Phi(u)
=-\pi e^{4u}+9u+\log(2\pi^2)
+\log\!\left(1-\frac{3}{2\pi}e^{-4u}\right)
+O(e^{-3\pi e^{4u}}).
\tag{14}
\]

The perturbation `(12)` is smaller than every fixed `e^{-c e^{4u}}`, so sharpening `(14)` by any finite hierarchy of algebraic or theta-exponential tail terms still cannot see the splice.

## 2. The whole bounded heat orbit converges to a Gaussian time shift

Let `I` be a compact real time interval and `K` a compact subset of `C`. Put

\[
T:=\max I,
\qquad
Y:=\max_{z\in K}|\operatorname{Im}z|.
\tag{15}
\]

Using `(10)`, the difference between the spliced orbit and the Gaussian-shifted Xi orbit is

\[
\mathcal H^{(\tau,R)}_t(z)-H_{t-\tau}(z)
=
\int_0^\infty
 e^{tu^2}\Phi(u)
 \bigl(q_{\tau,R}(u)-e^{-\tau u^2}\bigr)
 \cos(zu)\,du.
\tag{16}
\]

For `t in I` and `z in K`,

\[
\left|e^{tu^2}\Phi(u)
\bigl(q_{\tau,R}(u)-e^{-\tau u^2}\bigr)
\cos(zu)\right|
\le
\Phi(u)e^{Tu^2+Yu}.
\tag{17}
\]

The right-hand side is integrable because the Xi source decays like `exp(-pi e^(4u)+O(u))`; in particular XF-162 already proves every finite positive quadratic moment. The factor in parentheses in `(16)` tends pointwise to zero by `(10)`. Dominated convergence applied to the uniform majorant `(17)` proves

\[
\sup_{t\in I}\sup_{z\in K}
\left|
\mathcal H^{(\tau,R)}_t(z)-H_{t-\tau}(z)
\right|
\longrightarrow0,
\tag{18}
\]

which is `(6)`.

This is stronger than matching a few source moments or a few values of the heat trace. Any finite collection of compact spacetime observations of the shifted Xi orbit can be reproduced arbitrarily accurately while the far tail of the source is asymptotically indistinguishable from the original Xi tail beyond every fixed theta scale.

## 3. A nonreal zero survives the splice

Fix `tau>0`. XF-163 recalls the exact Gaussian identity

\[
H_t^{(\tau)}(z)=H_{t-\tau}(z).
\tag{19}
\]

The established bound `Lambda_Xi>=0` gives `-tau<Lambda_Xi`. By the defining de Bruijn--Newman dichotomy, `H_{-tau}` therefore has at least one nonreal zero; choose one and call it `z_tau`.

Because zeros of a nonzero entire function are isolated, choose a closed disk `D_tau` centered at `z_tau` whose closure is disjoint from the real axis and whose boundary contains no zero of `H_{-tau}`. Then

\[
m_\tau:=\min_{z\in\partial D_\tau}|H_{-\tau}(z)|>0.
\tag{20}
\]

Apply `(18)` with the single time `t=0` and `K=partial D_tau`. For all sufficiently large `R`,

\[
\sup_{z\in\partial D_\tau}
\left|
\mathcal H^{(\tau,R)}_0(z)-H_{-\tau}(z)
\right|
<m_\tau.
\tag{21}
\]

Rouché's theorem now gives the same number of zeros, counted with multiplicity, inside `D_tau`. Since `H_{-tau}` has at least one there, so does `mathcal H_0^(tau,R)`, and every point of the disk is nonreal. This proves `(7)`.

The argument does not require the selected zero to be simple. It also extends immediately to any finite list of isolated nonreal zero events at finitely many heat times: choose disjoint zero contours and use the uniform bounded-spacetime convergence `(18)`.

## 4. Exact tail equality is possible in `C^infinity`, but analyticity clarifies the true boundary

There is an even simpler smooth version. Let `chi_R` be a `C^infinity` cutoff equal to zero on `(-infinity,R]` and one on `[R+1,infinity)`, and set

\[
\widetilde\rho_{\tau,R}(u)
=
\Phi(u)
\left[
 e^{-\tau u^2}
 +\chi_R(u)(1-e^{-\tau u^2})
\right].
\tag{22}
\]

Then `tilde rho` is strictly positive, smooth, all-time admissible, equals the tilted source on `u<=R`, and equals **exactly** the Xi source on `u>=R+1`. The same tail estimate and Rouché argument show that its `t=0` transform has a nonreal zero for sufficiently large `R`.

This exact-tail version cannot be real analytic unless it is globally Xi: two real-analytic functions that agree on a tail interval agree everywhere on the connected real domain. That is why `(1)`--`(3)` use a soft analytic splice instead. The analytic construction shows that this identity-theorem escape does not rescue ordinary asymptotic source criteria: one can preserve strict analyticity while making the tail error smaller than every fixed theta-exponential scale.

Accordingly, the surviving source rigidity must be genuinely **global and exact**. Examples of the right logical type are a theta/modular identity that analytically links separated source scales, an exact coefficient law, or another relation whose violation cannot be hidden in a beyond-all-orders analytic perturbation. Merely adding more terms to the asymptotic expansion of `Phi` cannot suffice.

## Relation to prior findings

XF-162 established a real source-side separation: the Xi tail hazard and infinite heat-moment radius exclude the concrete XF-160/XF-161 maximal-contact source controls. XF-163 then showed that the normalized tail jet is gauge-blind because Gaussian tilting translates the heat origin while preserving those limits.

XF-164 goes one step further. It is not merely a second gauge example. The source `(3)` tends back to **Xi itself** in the far tail much faster than every fixed theta-exponential correction, yet on every bounded spacetime window its heat orbit tends to the Gaussian-shifted Xi orbit. Thus even source information strong enough to detect the literal Gaussian factor `e^{-tau u^2}` can remain noncoercive if it is still only asymptotic tail information.

This does not contradict XF-162: the discriminator there correctly separates Xi from the specific Appell-smoothed controls. It changes the programmatic interpretation. The tail discriminator is useful for classification, but it cannot become an RH/transition theorem merely by being sharpened to higher and higher asymptotic order.

## Prior-art and novelty audit

The de Bruijn--Newman deformation, Gaussian source multiplication and the threshold `Lambda_Xi` are classical; the Rodgers--Tao lower bound is already anchored in `SOURCES.md`. Rouché stability of isolated zeros under locally uniform holomorphic perturbation is standard complex analysis. Directed searches also find classical and later work on finite Fourier/Pólya approximations to the Xi kernel and on tail-based Xi-kernel shape conditions.

No external theorem found in the audit states the specific Mathia conclusion above: an explicit strictly positive real-analytic source multiplier that is beyond every fixed Xi theta-tail scale while its complete bounded heat orbit converges to a translated Xi orbit, forcing persistence of a nonreal `t=0` zero. The proof is self-contained once the established `Lambda_Xi>=0` anchor is granted. No new external source is load-bearing, so `SOURCES.md` requires no update.

## Falsification boundary

This finding does **not** show that the exact Xi theta formula, modular identity, or full global analytic germ can coexist with different zero geometry. The analytic soft splice is not itself the Xi theta kernel, and exact equality with Xi on an open tail interval would force equality everywhere in the real-analytic class.

It also does not assign a de Bruijn--Newman constant to the modified source or prove that its all-real threshold exists with the same global properties as Xi's. The durable conclusion is only the one actually proved: its distinguished `t=0` transform has a nonreal zero, and finite bounded pieces of its heat orbit can approximate the shifted Xi orbit arbitrarily well.

Finally, the construction does not re-create the XF-160 folded-binomial maximal-contact packet. It attacks a logically broader source-side hope: that sufficiently detailed tail asymptotics, together with positivity, analyticity and all-time admissibility, could themselves force the needed real-zero geometry.

## Consequence for `xi_flow`

The source-side frontier is now sharper than the Gaussian-gauge warning of XF-163. **Tail refinement alone is exhausted as a coercivity strategy.** Even a perturbation invisible beyond every fixed theta-exponential scale can preserve nonreal zero geometry inherited from a negative-time Xi slice.

The next gate should therefore test a genuinely global theta constraint. A useful candidate must link finite/mesoscopic source mass to the far tail by an exact identity and must fail on both the Gaussian tilt of XF-163 and the analytic soft splice `(3)`. If no such coercive identity can be found, the alternative is to return to source-to-destination mechanisms that use the exact Xi coefficients directly rather than trying to summarize them by a tail invariant.