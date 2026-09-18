---
id: WP-356
title: Hecke-truncation commutator is positive cusp-annulus energy but does not isolate the Weil prime weight
branch: weil_positivity
status: supported
kind: hecke-cusp-boundary-defect-positive-annulus-no-go
claim_strength: exact constant-mode Hecke/cusp-cutoff operator identity plus Eisenstein matched controls and critical half-density obstruction
created: 2026-09-18
related: [WP-226, WP-237, WP-345, WP-348, WP-353]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - classical self-adjoint normalization of Hecke operators on weight-zero Maass forms
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - classical Maaß-Selberg relations and Arthur truncation
  - Tian An Wong, Explicit formulas for the spectral side of the trace formula of SL(2), Acta Arith. 195 (2020), 149-175, arXiv:1608.02296
  - elementary cutoff/translation commutator calculus
---

# WP-356 — Hecke-truncation commutator is positive cusp-annulus energy but does not isolate the Weil prime weight

## Claim

The simplest source-defined operation that genuinely couples a finite prime correspondence to the archimedean cusp boundary **before** taking a positive norm can be computed exactly, and it gives a sharp negative control for the surviving Maaß–Selberg route.

On the constant Fourier mode of the modular cusp, the self-adjointly normalized prime Hecke operator becomes the sum of two translations by `±log p` after the natural unitary change to log height. Its commutator with the sharp height projection is a partial boundary defect whose positive square is exactly the projection onto the log-height annulus of width `2 log p`:

\[
\boxed{
 [P_\tau,\mathcal T_p]^*[P_\tau,\mathcal T_p]
 =\mathbf 1_{(\tau-\log p,\,\tau+\log p]}.
}
\tag{1}
\]

Thus a genuine source-native positive form does recover the logarithmic prime scale geometrically. But it recovers it only as **unsigned annulus size/background**. On a critical Eisenstein constant term, all scattering information appears in a sign-indefinite interference term inside that positive annulus energy. Averaging away the interference leaves only `log p`; isolating the interference requires subtracting the positive background and loses inherited positivity. Moreover the natural Hecke normalization has no surviving critical `p^{-1/2}` attenuation in this norm: the Jacobian exactly cancels it, and any scalar repair enters the energy quadratically.

The result closes the most literal constant-mode realization of the clue's remaining `finite-prime operator × archimedean truncation boundary → positive form` escape. It does **not** close couplings through nonconstant Fourier modes, several Hecke operators before scalarization, higher-rank/adelic truncation, nonlocal operator order, or a source theorem that canonically installs the critical half-density at vector level before the positive square is taken.

## 1. Exact representation map: prime Hecke correspondence becomes log-height translation

For the full modular group, use the standard self-adjoint normalization of the prime Hecke operator on weight-zero Maass forms,

\[
(\mathsf T_pF)(z)
=\frac1{\sqrt p}
\left(
F(pz)+\sum_{b=0}^{p-1}F\!\left(\frac{z+b}{p}\right)
\right).
\tag{2}
\]

On the `x`-independent cusp constant mode `F(y)`, (2) is

\[
(\mathsf T_pF)(y)
=p^{-1/2}F(py)+p^{1/2}F(y/p).
\tag{3}
\]

The radial cusp Hilbert measure is `dy/y^2`. Set `y=e^x` and conjugate by the exact unitary map

\[
(\mathcal UF)(x)=e^{-x/2}F(e^x),
\qquad
\mathcal U:L^2(\mathbb R_+,dy/y^2)\to L^2(\mathbb R,dx).
\tag{4}
\]

If `L=log p` and `(S_af)(x)=f(x+a)`, then the two Jacobian factors in (3) cancel the explicit powers of `p` and give

\[
\boxed{
\mathcal U\mathsf T_p\mathcal U^{-1}=S_L+S_{-L}.
}
\tag{5}
\]

This is the relevant source-to-geometry dictionary. The finite prime is not inserted as a kernel coefficient: its Hecke correspondence supplies the translation length `L=log p`, while the cusp metric supplies the log-height coordinate and Hilbert norm.

As a consistency check, the critical Eisenstein constant term

\[
F_t(y)=y^{1/2+it}+\varphi(t)y^{1/2-it},
\qquad |\varphi(t)|=1,
\tag{6}
\]

becomes

\[
f_t(x)=e^{itx}+\varphi(t)e^{-itx},
\tag{7}
\]

and (5) gives the usual prime Hecke eigenvalue

\[
(S_L+S_{-L})f_t=2\cos(t\log p)f_t.
\tag{8}
\]

Thus no arithmetic frequency has been introduced by hand.

## 2. The Hecke/cusp-cutoff commutator has an exact positive annulus square

Let

\[
P_\tau=\mathbf 1_{(\tau,\infty)}
\tag{9}
\]

be the sharp log-height projection corresponding to the cusp boundary `y=e^\tau`. Define the boundary defect

\[
D_{p,\tau}:=[P_\tau,S_L+S_{-L}].
\tag{10}
\]

The two translation branches are elementary:

\[
[P_\tau,S_L]f(x)
=-\mathbf 1_{(\tau-L,\tau]}(x)f(x+L),
\tag{11}
\]

\[
[P_\tau,S_{-L}]f(x)
=\mathbf 1_{(\tau,\tau+L]}(x)f(x-L).
\tag{12}
\]

Their output supports are disjoint. Pulling the translations back in the norm therefore gives, for every `f in L^2(R)`,

\[
\boxed{
\|D_{p,\tau}f\|_2^2
=\int_{\tau-L}^{\tau+L}|f(u)|^2\,du.
}
\tag{13}
\]

Equivalently,

\[
\boxed{
D_{p,\tau}^*D_{p,\tau}
=\mathbf 1_{(\tau-L,\tau+L]}.
}
\tag{14}
\]

So the positive operator is even more rigid than a generic Gram form: it is exactly an annulus projection. Its sign theorem is independent of zeta zeros, scattering continuation, or RH. The prime enters only through the annulus half-width `log p`.

This is genuinely closer to the line mandate than a post-normalizer scalar manipulation. The finite-prime Hecke correspondence and the archimedean cusp boundary are coupled **before** the square is taken. Nevertheless, (14) already exposes the limitation: the positive square remembers only which log-height layer crosses the boundary under the correspondence.

## 3. On the critical Eisenstein wave, the scattering data is only an interference term

Although the Eisenstein state (7) is not globally in `L^2(R)`, its commutator defect is compactly supported, so (13) is finite. Substitution gives

\[
\begin{aligned}
E_p(t,\tau)
&:=\|D_{p,\tau}f_t\|_2^2\\
&=4L
+2\operatorname{Re}\!\left(
\varphi(t)e^{-2it\tau}\frac{\sin(2tL)}{t}
\right),
\qquad L=\log p,
\end{aligned}
\tag{15}
\]

with the continuous limiting interpretation at `t=0`. Equation (15) is nonnegative because it is exactly the integral of `|f_t|^2` over the annulus; no zero-location statement is used.

The decomposition is decisive. The term

\[
4\log p
\tag{16}
\]

is the universal positive background coming from the two unit-amplitude waves. The only dependence on the scattering normalizer is

\[
2\operatorname{Re}\!\left(
\varphi(t)e^{-2it\tau}\frac{\sin(2t\log p)}{t}
\right),
\tag{17}
\]

which is not separately nonnegative. Varying `tau`, `t`, or an admissible unitary boundary phase changes its sign while the full quantity (15) remains positive.

For `t != 0`, a long Cesàro average in the truncation height removes (17) exactly in the limit:

\[
\lim_{R\to\infty}\frac1{2R}
\int_{-R}^{R}E_p(t,\tau)\,d\tau
=4\log p.
\tag{18}
\]

Thus the most canonical phase-erasing operation retains a clean positive `log p`, but precisely by erasing the scattering/zero information that the clue needs.

There is also a positive shape derivative if the translation length is treated as a continuous matched-control parameter:

\[
\frac{\partial}{\partial L}
\int_{\tau-L}^{\tau+L}|f_t(u)|^2du
=|f_t(\tau+L)|^2+|f_t(\tau-L)|^2\ge0,
\tag{19}
\]

or explicitly

\[
4+4\operatorname{Re}(\varphi(t)e^{-2it\tau})\cos(2tL)\ge0.
\tag{20}
\]

Again the sign belongs to the full boundary intensity, not to the oriented scattering contribution obtained after subtracting the universal `4`.

## 4. The critical half-density is not supplied by this positive square

The branch's standard critical Weil finite-prime ray carries the first-prime amplitude proportional to

\[
\frac{\log p}{\sqrt p}.
\tag{21}
\]

The source-normalized defect (13)--(18) supplies `log p` as an annulus length but no surviving `p^{-1/2}` attenuation. This is not because the Hecke operator was left unnormalized: the factor `p^{-1/2}` in (2) is exactly what, together with the cusp Hilbert Jacobian, produces the equal unit translations in (5).

More generally, multiplying the Hecke correspondence by a scalar `c_p` gives

\[
\|[P_\tau,c_p\mathcal T_p]f\|^2
=|c_p|^2\|D_{p,\tau}f\|^2.
\tag{22}
\]

Therefore forcing the background logarithmic scale to acquire the critical factor `p^{-1/2}` requires

\[
|c_p|^2=p^{-1/2},
\qquad |c_p|=p^{-1/4}.
\tag{23}
\]

No such quarter-power is selected by the tested Petersson/cusp geometry. Equation (23) is not a proof that no richer automorphic construction can produce the half-density; it is an exact obstruction for obtaining it merely by taking the positive norm of this canonical Hecke boundary defect. It is the automorphic analogue of the recurrent problem that a positive self-pairing squares the amplitude one wants to keep linear.

The same point can be stated without committing to a particular explicit-formula convention: **any one-power arithmetic attenuation intended to survive in the quadratic energy must already occur as its square root at vector level**. The present source normalization removes, rather than supplies, such a prime-dependent vector amplitude.

## 5. Matched controls falsify the sign mechanism rather than the Hecke dictionary

### Continuous-dilation control

Replace the arithmetic length `log p` by any real `L>0` and define

\[
\mathcal T_L=S_L+S_{-L}.
\tag{24}
\]

The same proof gives

\[
[P_\tau,\mathcal T_L]^*[P_\tau,\mathcal T_L]
=\mathbf 1_{(\tau-L,\tau+L]}.
\tag{25}
\]

Hence positivity and logarithmic-width recovery are translation geometry, not a property unique to primes. Arithmetic is real in (5)—Hecke theory selects `L=log p`—but the **sign theorem** in (14) does not know that `e^L` is prime. This is exactly the distinction required by the representation audit.

### Inner/CDD phase control

More strongly, replace the Eisenstein scattering phase `varphi(t)` in (7) by any measurable boundary phase `eta(t)` with `|eta(t)|=1`. The operator identity (14) is unchanged and

\[
\|D_{p,\tau}(e^{itx}+\eta(t)e^{-itx})\|^2\ge0
\tag{26}
\]

holds identically. In particular the divisor-changing reciprocal inner/CDD controls already used in `WP-345` can change the off-axis meromorphic divisor while preserving the same boundary norm positivity.

Therefore the new Hecke coupling does not repair the core defect of plain Maaß--Selberg boundary positivity: even though the prime operator is now inserted before the sign is taken, **the positive square still cannot distinguish the arithmetic scattering divisor from a matched unitary-phase control**.

### Background subtraction control

One might subtract (16) and keep only (17), because (17) is the part that carries the scattering phase. But then the result changes sign under harmless changes of `tau` or unitary phase. The subtraction therefore converts an independently positive norm into a signed interference observable. Positivity of the original geometry no longer implies the desired sign.

This is not the height-only linear-filter obstruction of `WP-237`: here the prime Hecke correspondence and the boundary are genuinely coupled before the square. The failure occurs one step later, because the positive square packages the phase-sensitive information together with an unavoidable unsigned self-energy.

## 6. Prior-art and novelty audit

The ingredients are classical: normalized Hecke operators on Maass/Eisenstein spaces, the critical Eisenstein constant term, log-height cusp coordinates, Maaß--Selberg/Arthur truncation, and elementary commutator algebra. Standard references such as Iwaniec's *Spectral Methods of Automorphic Forms* supply the automorphic conventions, while Wong supplies the exact positive-truncation/explicit-formula setting used by the active clue.

A bounded literature search for combinations of Hecke operators, Arthur/Maaß--Selberg truncation, cusp cutoffs, commutators, and `log p` did not surface a named theorem asserting the specific identity (14) as an RH/Weil positivity mechanism. **No historical novelty is claimed.** The Mathia contribution here is the exact representation map (2)--(5), the resulting boundary-defect identity (14), and its use as a matched falsifier at the current Weil Positivity frontier.

The route is also distinct from `WP-345`. That finding differentiates the Maaß--Selberg norm in truncation height and obtains a positive boundary square while killing the `T`-independent logarithmic-derivative block. Here a finite-prime Hecke operator is coupled to the boundary **before** the norm is taken. The new computation shows that even this noncentral arithmetic insertion reduces, on the constant cusp mode, to an annulus projection whose positivity is universal and whose phase-sensitive component has no inherited sign.

## 7. Aggressive falsification and surviving scope

The strongest positive reading of the construction is real: (14) is canonical once the modular cusp, the standard normalized Hecke correspondence, and the source truncation boundary are fixed. It produces both a finite-prime label and an archimedean boundary response in one object, and its nonnegativity is independent of RH. So it passes several gates that killed earlier candidates.

It nevertheless fails the decisive bridge for three independent reasons:

1. the positive operator square depends only on the annulus and survives continuous nonarithmetic translation controls;
2. the scattering/divisor information lives only in a signed interference term and survives arbitrary unit-modulus divisor-changing phase controls at the level of positivity;
3. the canonical quadratic norm retains `log p` but not the critical half-density, and a scalar repair would have to insert a target-shaped quarter-power at vector level.

These are structural failures, not a numerical miss that can be repaired by choosing a better truncation height.

The result does **not** rule out a source-defined form involving nonconstant Fourier modes, joint products or correlations of several Hecke correspondences before the square, an adelic/higher-rank truncation where finite and infinite local operators mix nonseparably, a genuine operator-order theorem rather than a Hilbert norm, or a cohomological construction in which the critical half-density is forced before self-pairing. Those are now the relevant escapes. Repeating the constant-mode sharp-boundary commutator with another scalar normalization, another height, or another unitary scattering phase is not.

## Consequence

The accepted Maaß--Selberg clue remains open, but its simplest genuinely arithmetic boundary coupling is now classified:

\[
\boxed{
\text{prime Hecke correspondence}
+\text{cusp cutoff}
\longrightarrow
\text{positive log-height annulus energy},
}
\tag{27}
\]

and the positive energy does not orient the Weil scattering/prime contribution. A surviving construction must make arithmetic enter the **positive operator order itself**, or must force the critical half-density and the phase orientation before quadratic self-pairing. Merely letting a prime correspondence cross the Arthur boundary is not enough.
