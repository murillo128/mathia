# PF-060 — collapsing prime necks block the standard localization-at-infinity closure

**Status:** `DECISIVE-NEGATIVE` for upgrading the pointed-tangent inclusions of PF-034/PF-050 to a complete description of the essential spectrum by off-the-shelf limit-operator / localization-at-infinity theory. `STRUCTURAL` for the collapse channel.

## 1. The tempting next step

PF-034 and PF-050 give explicit non-collapsed pointed tangents \(Y_H\) arising from recurrent isolated prime patterns and show that their low-energy spectral data occur in the essential spectrum / local spectral measures of the prime flute.

A natural next move would be to invoke a general localization-at-infinity theorem and claim schematically

\[
\sigma_{\rm ess}(\Delta_X)
\stackrel{?}{=}
\overline{\bigcup_{Y\in\mathscr T_\infty(X)}\sigma(\Delta_Y)},
\]

where \(\mathscr T_\infty(X)\) denotes pointed geometric/right limits. This would turn the explicit tangent construction into a classification theorem.

For the prime flute this standard route is not available because the geometry collapses at infinity.

## 2. Exact failure of the non-collapsing hypothesis

From PF-020/PF-034 there are distinct simple primitive separating geodesics

\[
\gamma_j,\qquad L_j:=\ell(\gamma_j)\to0.
\]

The collar theorem gives an embedded collar around \(\gamma_j\)

\[
C_j=\{(r,\theta):|r|<w(L_j),\ \theta\in\mathbb R/\mathbb Z\},
\]

with

\[
ds^2=dr^2+L_j^2\cosh^2r\,d\theta^2,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)}\to\infty.
\]

Let \(x_j\in\gamma_j\) and fix any radius \(R>0\). For large \(j\), \(w(L_j)>R\), and the metric ball \(B(x_j,R)\) lies in the strip \(|r|<R\). Hence

\[
\operatorname{Area} B(x_j,R)
\le
\int_{-R}^{R}\int_0^1 L_j\cosh r\,d\theta\,dr
=2L_j\sinh R
\longrightarrow0.
\]

Therefore

\[
\boxed{
\inf_{x\in X}\operatorname{Area}B(x,R)=0
\qquad\text{for every fixed }R>0.
}
\]

In particular the injectivity radius has no positive lower bound and the prime flute is not a bounded-geometry / uniformly non-collapsed metric-measure space.

## 3. Why this blocks the standard localization theorem

Georgescu's localization-at-infinity theorem for elliptic operators on proper metric-measure spaces assumes, among other conditions,

\[
\inf_x\mu(B_x(r_0))>0
\]

for a fixed positive radius (his Theorem 2.1 uses \(r_0=1/2\)), together with a Property-A-type condition. Under those assumptions the essential spectrum is the closure of the union of spectra of the localizations at infinity.

The ball-area estimate above violates precisely this non-collapsing hypothesis.

Later limit-operator frameworks on general metric-measure spaces likewise advertise **bounded geometry** as a core assumption. Graph \(R\)-limit theorems have analogous uniform-geometry/growth hypotheses. Thus none of these results can simply be cited to upgrade

\[
\sigma(\Delta_{Y_H})\subset\sigma_{\rm ess}(\Delta_X)
\]

into an equality over the ordinary pointed tangents of the prime flute.

This is not a claim that no collapse-aware localization theorem can exist. It is a decisive negative only for the off-the-shelf right-limit/localization route.

## 4. The missing collapsing channel has a universal local blow-up

The collapse can itself be analyzed exactly. On the collar \(C_L\), the nonnegative Laplacian is

\[
\Delta_L
=-\partial_r^2-\tanh r\,\partial_r
-\frac1{L^2\cosh^2r}\partial_\theta^2.
\]

For the Fourier mode \(e^{2\pi i m\theta}\),

\[
H_{m,L}
=-\partial_r^2-\tanh r\,\partial_r
+\frac{(2\pi m)^2}{L^2\cosh^2r}.
\]

On every fixed compact \(r\)-window, the potential of every \(m\ne0\) mode tends to \(+\infty\) as \(L\to0\). Thus the only fixed-energy mode surviving in the central collar blow-up is the transverse constant mode

\[
H_0=-\partial_r^2-\tanh r\,\partial_r
\quad\text{on }L^2(\mathbb R,\cosh r\,dr).
\]

Conjugating by \((\cosh r)^{1/2}\) gives

\[
\boxed{
\widetilde H_0
=-\frac{d^2}{dr^2}
+\frac14+rac1{4\cosh^2r}.
}
\]

Hence

\[
\sigma_{\rm ess}(\widetilde H_0)=[1/4,\infty),
\]

and because its potential is everywhere \(\ge1/4\), it has no spectrum below \(1/4\).

So the most obvious **pure-collapse** localization channel is universal and gap-blind at fixed energy below \(1/4\). The prime gap enters only through the scale \(L\) that has been sent to zero.

This fits the previous picture:

- the universal cusp/collapse channels account naturally for the threshold \(1/4\) and above;
- the prime-specific low-energy data in \((0,1/4)\) found in PF-034--PF-056 live in non-collapsed finite tangents and in their weighted-neck interactions.

It does **not** yet prove that these are the only channels below \(1/4\); that would require a genuine two-scale/collapse-aware localization theorem.

## 5. Consequence for the research program

The attractive shortcut

\[
\boxed{
\text{enumerate ordinary pointed tangents}
\to
\text{take the union of their spectra}
\to
\sigma_{\rm ess}(\Delta_X)
}
\]

cannot be justified by the standard localization-at-infinity machinery, because the prime flute violates its uniform local-volume / bounded-geometry hypotheses in the strongest possible way.

The correct next-level object, if one wants a complete essential-spectrum theorem, must carry **two types of limits simultaneously**:

1. non-collapsed pointed tangents \(Y_H\), which retain the relative prime-gap/cuff moduli;
2. collapsed collar blow-ups, whose central fixed-energy channel is the universal operator
   \(-d^2/dr^2+1/4+\tfrac14\operatorname{sech}^2r\).

Any theorem claiming completeness of PF-034/PF-050 without accounting for the second class would currently have a real analytic gap.

## Novelty check

- Georgescu's 2011 theorem already describes essential spectra by localizations at infinity for a broad metric-space class, but explicitly requires a uniform lower bound on ball measures.
- Modern limit-operator extensions on metric-measure spaces are formulated under bounded-geometry hypotheses.
- The hyperbolic collar model and its Fourier decomposition are standard; no novelty is claimed for the one-dimensional \(\operatorname{sech}^2\) operator.
- Directed searches did not locate a collapse-aware localization-at-infinity theorem tailored to an infinite-type hyperbolic surface with infinitely many simple closed geodesics tending to zero.

The substantive result for the prime-flute program is therefore negative/structural: **the standard right-limit closure is unavailable exactly because the same prime-derived short-neck phenomenon that creates the interesting tangents destroys non-collapse.**
