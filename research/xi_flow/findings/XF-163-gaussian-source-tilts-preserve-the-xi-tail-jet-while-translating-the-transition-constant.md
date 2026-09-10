---
type: negative
research_line: xi_flow
finding_id: XF-163
status: canonical
---

# XF-163 — Gaussian source tilts preserve the Xi tail jet while translating the transition constant

**Confidence:** high. The source transformation and transition-time identity are exact consequences of the defining Fourier integral. Preservation of the XF-162 normalized tail action, hazard, and curvature is elementary. The only external theorem used for the sign conclusion is the established Rodgers--Tao bound `Lambda_Xi >= 0`, already anchored in `SOURCES.md`. This finding does **not** construct a maximal-contact packet with the Xi theta coefficients; it proves a stronger obstruction to using the XF-162 tail jet itself as an absolute transition-time coercivity law.

## Statement

XF-162 found a genuine Xi-specific discriminator against the XF-160/XF-161 controls:

\[
\mathfrak T_\Phi(u)\to\pi,
\qquad
\mathfrak H_\Phi(u)\to4\pi,
\qquad
-e^{-4u}(\log\Phi)''(u)\to16\pi,
\tag{1}
\]

where

\[
\mathfrak T_\rho(u):=-e^{-4u}\log\rho(u),
\qquad
\mathfrak H_\rho(u):=-e^{-4u}(\log\rho)'(u).
\tag{2}
\]

Those limits are not, however, tied to an absolute heat origin. For every `tau>=0`, define the Gaussian source tilt

\[
\boxed{
\Phi_\tau(u):=e^{-\tau u^2}\Phi(u).
}
\tag{3}
\]

Let

\[
H_t^{(\tau)}(z)
:=\int_0^\infty e^{t u^2}\Phi_\tau(u)\cos(zu)\,du.
\tag{4}
\]

Then, identically for every real `t` and complex `z`,

\[
\boxed{
H_t^{(\tau)}(z)=H_{t-\tau}(z).
}
\tag{5}
\]

Consequently, if `Lambda_Xi` is the de Bruijn--Newman constant of the original Xi source and `Lambda_tau` is the all-real threshold of `(4)`, then

\[
\boxed{
\Lambda_\tau=\Lambda_{\rm Xi}+\tau.
}
\tag{6}
\]

Thus the transition constant moves by an exactly prescribed amount while all three normalized tail limits in `(1)` remain unchanged:

\[
\boxed{
\mathfrak T_{\Phi_\tau}(u)\to\pi,
\qquad
\mathfrak H_{\Phi_\tau}(u)\to4\pi,
\qquad
-e^{-4u}(\log\Phi_\tau)''(u)\to16\pi.
}
\tag{7}
\]

Moreover `Phi_tau` remains a strictly positive smooth source and retains quadratic exponential moments of every order. Hence `(3)` gives a one-parameter family of positive all-time source deformations with the **same XF-162 tail jet** but transition constants separated by any prescribed `tau`.

Since Rodgers--Tao proves `Lambda_Xi>=0`, every `tau>0` even gives

\[
\boxed{
\Lambda_\tau\ge\tau>0.
}
\tag{8}
\]

Therefore the tail action/hazard/curvature limits of XF-162, even augmented by positivity, smoothness, and all-time quadratic-moment admissibility, cannot force `Lambda<=0`, cannot upper-bound the absolute transition time, and cannot by themselves exclude a positive transition constant.

## 1. Gaussian multiplication is exactly a heat-origin translation

Substituting `(3)` into `(4)` gives

\[
\begin{aligned}
H_t^{(\tau)}(z)
&=\int_0^\infty
 e^{t u^2}e^{-\tau u^2}\Phi(u)\cos(zu)\,du\\
&=\int_0^\infty
 e^{(t-\tau)u^2}\Phi(u)\cos(zu)\,du\\
&=H_{t-\tau}(z),
\end{aligned}
\tag{9}
\]

which proves `(5)`. No approximation or zero perturbation argument is involved.

By definition, the zeros of the original `H_s` are all real exactly for `s>=Lambda_Xi`. Equation `(5)` therefore gives

\[
H_t^{(\tau)}\text{ has only real zeros}
\quad\Longleftrightarrow\quad
t-\tau\ge\Lambda_{\rm Xi},
\tag{10}
\]

and `(6)` follows. The source tilt is thus not merely analogous to changing heat time: it **is** a change of the heat-time origin on the same orbit.

This is the relevant stress test for any proposed source invariant. A quantity invariant under `rho(u) -> e^{-tau u^2}rho(u)` cannot distinguish where the origin `t=0` has been placed, whereas `Lambda` transforms affinely under exactly that operation.

## 2. The XF-162 tail jet is invariant under the heat-origin gauge

From `(3)`,

\[
\log\Phi_\tau(u)=\log\Phi(u)-\tau u^2.
\tag{11}
\]

Therefore

\[
\mathfrak T_{\Phi_\tau}(u)
=\mathfrak T_\Phi(u)+\tau u^2e^{-4u},
\tag{12}
\]

and

\[
\mathfrak H_{\Phi_\tau}(u)
=\mathfrak H_\Phi(u)+2\tau u e^{-4u}.
\tag{13}
\]

Differentiating once more gives

\[
-e^{-4u}(\log\Phi_\tau)''(u)
=
-e^{-4u}(\log\Phi)''(u)+2\tau e^{-4u}.
\tag{14}
\]

All correction terms in `(12)`--`(14)` vanish as `u->infinity`, proving `(7)`. More generally, any finite normalized logarithmic tail jet whose normalization kills polynomial additions to `log rho` will share the same obstruction.

The all-time moment property is also preserved. XF-162 proves

\[
\int_0^\infty e^{s u^2}\Phi(u)\,du<\infty
\quad\text{for every real finite }s,
\tag{15}
\]

with negative `s` immediate from positivity and the `s>=0` case proved from the double-exponential theta tail. Hence

\[
\int_0^\infty e^{s u^2}\Phi_\tau(u)\,du
=
\int_0^\infty e^{(s-\tau)u^2}\Phi(u)\,du<\infty
\tag{16}
\]

for every real finite `s`. Multiplication by the positive entire Gaussian also preserves positivity and the smooth/analytic source regularity already possessed by `Phi`.

A small additional gauge check is useful. The tilt does not even change the source value at the origin:

\[
\Phi_\tau(0)=\Phi(0).
\tag{17}
\]

What detects the shift is necessarily finer finite-scale information; for example

\[
(\log\Phi_\tau)''(0)
=(\log\Phi)''(0)-2\tau.
\tag{18}
\]

Thus fixing a genuine heat origin requires at least one source datum that is **not** invariant under the Gaussian tilt.

## 3. Gauge-invariant source laws cannot control absolute `Lambda`

The preceding calculation is not special to the three limits in XF-162. Let `I(rho)` be any collection of source data satisfying

\[
I(e^{-\tau u^2}\rho)=I(\rho)
\quad\text{for all }\tau\ge0
\tag{19}
\]

through a class on which the de Bruijn--Newman threshold is defined. Whenever the source orbit remains admissible,

\[
\Lambda(e^{-\tau u^2}\rho)=\Lambda(\rho)+\tau.
\tag{20}
\]

Therefore no finite upper bound on absolute `Lambda` can be a function only of `I`. In particular, an invariant class containing Xi and closed under positive Gaussian tilts contains sources with arbitrarily large transition constants while retaining exactly the same invariant data.

This is a structural obstruction rather than another matched-control construction. XF-160/XF-161 asked whether generic positivity and analytic regularity could realize the maximal-contact mechanism. XF-162 then found a tail discriminator excluding those controls. XF-163 shows that the discriminator is **gauge-blind**: before one even tries to splice the XF-160 packet into an Xi-like tail, the Xi heat orbit itself already supplies sources with identical tail limits and translated transition times.

Hence a successful source theorem must break the Gaussian heat-origin symmetry. It must use some finite/mesoscopic datum, an exact theta differential identity, coefficient organization, or another normalization that transforms nontrivially under `(3)` and thereby pins the distinguished Xi slice `t=0`.

## Prior-art and novelty audit

Gaussian multiplication of a Fourier-side measure is classical in the de Bruijn--Newman framework; Newman's 1976 paper formulates its real-zero problem precisely using factors of the form `exp(-b u^2)`. Rodgers--Tao use the normalization `H_t(z)=integral exp(tu^2)Phi(u)cos(zu)du` and establish `Lambda_Xi>=0`. A directed literature search around Gaussian source factors and de Bruijn--Newman time translation found the classical Gaussian operation, but no reason to treat identity `(5)` itself as new; it is immediate from the definition.

The Mathia-specific content is narrower: combining this exact covariance with the XF-162 normalized tail quantities shows that the proposed tail action/hazard/curvature discriminator is invariant along an orbit on which the target transition constant translates arbitrarily. No external theorem is needed for `(5)`--`(7)`; Rodgers--Tao is used only for the optional strict-positive lower bound `(8)`. Both classical anchors are already recorded in `SOURCES.md`, so no source-file update is required.

## Falsification boundary

This finding does **not** show that a source with the exact Xi theta coefficient formula can have a different transition constant. The tilted source `Phi_tau` is not the original theta kernel for `tau!=0`; it lies on the same heat orbit but changes finite-scale source shape. An exact theta identity that fixes that shape can therefore evade the obstruction.

It also does not reproduce the XF-160 maximal-contact blind packet inside the Xi-tail class, and it does not improve any target-side visibility estimate. Its claim is logically prior: the asymptotic tail jet isolated in XF-162 cannot itself be the coercive datum because it fails to determine the heat origin even on Xi's own Gaussian orbit.

Finally, `(8)` is not a new lower bound for the actual Xi constant. It is simply the Rodgers--Tao bound transported through the exact shift `(6)` to the modified source.

## Consequence for `xi_flow`

The no-splicing question from XF-162 has a decisive negative answer at the level of tail-hazard coercivity. One does not need a delicate splice: the Gaussian tilt `(3)` preserves the complete XF-162 tail limits, positivity, smoothness, and all-time heat admissibility while translating `Lambda` by an arbitrary prescribed amount.

The source-side frontier therefore moves one level deeper. The next useful question is not whether the Xi tail is sufficiently double-exponential, but **which non-Gaussian-gauge-invariant theta datum pins the physical `t=0` slice and couples it to the mesoscopic mass relevant to transition formation**. Any proposed invariant should first be tested against `(3)`; if it survives unchanged, it cannot by itself control absolute `Lambda`.