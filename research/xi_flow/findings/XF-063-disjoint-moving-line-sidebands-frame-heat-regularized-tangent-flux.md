# XF-063 — disjoint moving-line sidebands frame heat-regularized tangent flux

**Status:** `EXACT-DERIVED` + `LINEARIZED-FRAME` + `MATCHED-CONTROL` + `STRUCTURAL/REPAIR`. XF-060 identifies the derivative-matched moving-line square function needed to calibrate selector amplitude against triple flux, while XF-061 shows that no such slow-frequency norm can control an arbitrary static sparse defect. XF-062 then proves that fixed positive heat time removes precisely that spectral-support escape in the arithmetic-lattice tangent flow: any surviving critical tangent flux must lie in the XF-059 slow cone. The remaining tangent-level gap was a lower frame from the continuous moving-line selector family to the Fourier energy `\mathcal Q_M` of XF-062.

That frame is already present in the exact XF-056 probe geometry. Compact support of `\widehat g` makes distinct periodic tangent modes produce **disjoint selector sidebands**, because the selector resolution width is `1/M` whereas the `N=2M` periodic Fourier spacing is `\pi/M>2/M`. Consequently the derivative-weighted continuous selector square function diagonalizes the tangent field with the same `M^3|m(\xi)|^6` symbol as `\mathcal Q_M`, up to the fixed window constant.

Use the XF-062 scales

\[
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
N=2M,
\qquad
s=\frac{4\pi}{\log(T/4\pi)},
\tag{1}
\]

and fix the nonzero XF-056 envelope `g` with

\[
\chi:=\widehat g\in C_c^\infty((-1,1)),
\qquad
C_g:=\int_{\mathbb R}|\chi(u)|^2\,du>0.
\tag{2}
\]

Let `a=(a_j)` be a real `N`-periodic root-displacement tangent. Write its unitary discrete Fourier expansion using principal frequencies `\xi_\ell\in(-\pi,\pi]`,

\[
a_j=\frac1{\sqrt N}\sum_\ell \widehat a_\ell e^{i\xi_\ell j},
\qquad
\xi_\ell\in\frac{2\pi}{N}\mathbb Z,
\tag{3}
\]

and put `m(\xi)=e^{i\xi}-1` as in XF-062. The first variation at the arithmetic lattice of the exact moved selector

\[
\sum_{j\in\mathbb Z}
 g\!\left(\frac{j+\varepsilon a_j}{M}\right)
 e^{-i\theta(j+\varepsilon a_j)}
\tag{4}
\]

is

\[
\boxed{
\mathcal L_{M,a}(\theta)
:=
\sum_{j\in\mathbb Z}
a_j
\left[
\frac1M g'(j/M)-i\theta g(j/M)
\right]e^{-i\theta j}.
}
\tag{5}
\]

Fix `\tau>0`. For a constant `C>C_*(\tau)` large enough for the ultraviolet estimate in XF-062, define

\[
B_T^{\rm in}
:=
\left[
2q^{-3/2},
\frac{C\log\log T}{q}
\right],
\tag{6}
\]

\[
B_T^{\rm out}
:=
\left[
q^{-3/2},
\frac{(C+1)\log\log T}{q}
\right].
\tag{7}
\]

Then every real periodic tangent satisfies the asymptotic lower-frame inequality

\[
\boxed{
M\int_{B_T^{\rm out}}
(M\theta^2)^2
|\mathcal L_{M,a}(\theta)|^2\,d\theta
\ge
\left(\frac{C_g}{4}+o(1)\right)
\mathcal Q_M
\bigl(B_T^{\rm in}\cup(-B_T^{\rm in}),0\bigr),
}
\tag{8}
\]

where the `o(1)` is uniform over the tangent field. The same identity applies at any time after replacing `a` by `a(t)`.

Combining (8) with XF-062 gives the decisive positive-time consequence. If `\|a(0)\|_{\ell^\infty}\le A_0` and

\[
\liminf_{T\to\infty}
\mathcal F_M^{\rm lin}(\tau;a)>c_0>0,
\tag{9}
\]

then

\[
\boxed{
\liminf_{T\to\infty}
M\int_{B_T^{\rm out}}
(M\theta^2)^2
|\mathcal L_{M,a(\tau)}(\theta)|^2\,d\theta
\ge
\frac{C_gc_0^2}{18}>0.
}
\tag{10}
\]

Thus **every bounded periodic lattice tangent that retains critical triple flux after a fixed positive heat time is detected by the same derivative-weighted moving-line selector norm that is `o(1)` on the actual Xi carrier by XF-059--XF-060**. Pure waves, chirps, and sparse defects no longer need separate tangent-level tests once heat regularization is imposed.

This closes the selector-frame boundary explicitly left open in XF-062, but only in the periodic tangent model. It does not supply a nonlinear finite-amplitude frame, preserve transition flux for a fixed positive delay, or cross a collision/complex-root interval. No upper bound on the de Bruijn--Newman constant follows.

## 1. Poisson summation diagonalizes the linearized selector

Substitute (3) into (5). For one Fourier mode with principal frequency `\xi`, Poisson summation gives, whenever the probe center lies in the slow positive range and the active alias is the principal one,

\[
\sum_j g(j/M)e^{-i(\theta-\xi)j}
=M\chi\!\left(M(\theta-\xi)\right),
\tag{11}
\]

and

\[
\sum_j \frac1M g'(j/M)e^{-i(\theta-\xi)j}
=iM(\theta-\xi)
\chi\!\left(M(\theta-\xi)\right).
\tag{12}
\]

The envelope derivative and carrier derivative therefore combine exactly:

\[
iM(\theta-\xi)-iM\theta=-iM\xi.
\tag{13}
\]

Hence on `B_T^{\rm out}`,

\[
\boxed{
\mathcal L_{M,a}(\theta)
=-\frac{iM}{\sqrt N}
\sum_{\xi_\ell>0}
\xi_\ell\widehat a_\ell
\chi\!\left(M(\theta-\xi_\ell)\right),
}
\tag{14}
\]

where only frequencies within `1/M` of the probe center can occur. Modes elsewhere, including the translation mode, contribute exactly zero.

The principal Fourier spacing is

\[
\xi_{\ell+1}-\xi_\ell
=\frac{2\pi}{N}
=\frac\pi M.
\tag{15}
\]

Because `\operatorname{supp}\chi\subset(-1,1)`, the sideband of one mode is contained in

\[
|\theta-\xi_\ell|<\frac1M.
\tag{16}
\]

Two such sidebands have total half-width `2/M`, strictly smaller than the spacing `\pi/M`. Therefore **no two periodic Fourier modes overlap in the continuous selector variable**. This is stronger than an almost-orthogonality estimate: the quadratic selector energy is diagonal mode by mode.

The exact cancellation in (13) is the arbitrary-mode version of the pure-wave calculation in XF-060. It also explains why the selector sees one derivative of root displacement before the explicit second-difference weight supplies the remaining two derivatives required by triple flux.

## 2. The derivative-weighted square function has the XF-062 `H^3` symbol

Every sideband centered at `\xi\in B_T^{\rm in}` lies inside `B_T^{\rm out}` for sufficiently large `T`. At the lower edge,

\[
2q^{-3/2}-M^{-1}
>q^{-3/2},
\tag{17}
\]

and at the upper edge `M^{-1}=q^{-2}` is negligible compared with the added `q^{-1}\log\log T` margin.

Using the exact disjointness from Section 1 and changing variables

\[
u=M(\theta-\xi),
\tag{18}
\]

gives the contribution of one positive inner-band mode to the weighted selector energy:

\[
\frac{M^2}{N}\,
\xi^2|\widehat a(\xi)|^2
\int_{-1}^{1}
\left[
M\left(\xi+\frac uM\right)^2
\right]^2
|\chi(u)|^2\,du.
\tag{19}
\]

Uniformly on `B_T^{\rm in}`,

\[
M\xi\ge2q^{1/2}\longrightarrow\infty,
\qquad
\sup_{\xi\in B_T^{\rm in}}|\xi|\longrightarrow0.
\tag{20}
\]

Therefore

\[
\int
\left[
M\left(\xi+\frac uM\right)^2
\right]^2
|\chi(u)|^2du
=
M^2\xi^4C_g(1+o(1)),
\tag{21}
\]

uniformly in the mode, while

\[
|m(\xi)|^6
=\xi^6(1+o(1)).
\tag{22}
\]

Since `N=2M`, (19)--(22) yield

\[
M\int_{B_T^{\rm out}}
(M\theta^2)^2
|\mathcal L_{M,a}(\theta)|^2d\theta
\ge
\left(\frac{C_g}{2}+o(1)\right)
M^3
\sum_{\xi_\ell\in B_T^{\rm in}}
|m(\xi_\ell)|^6|\widehat a_\ell|^2.
\tag{23}
\]

For real `a`, Fourier energy is symmetric between `\xi` and `-\xi`. The sum in (23) is one half of the symmetric XF-062 energy, proving (8).

The factor `C_g/4` is therefore not a fitted constant. One factor `1/2` comes from the exact period choice `N=2M`; the second comes from using only the positive-frequency Xi selector to control a real tangent whose `H^3` energy is symmetric.

## 3. Fixed heat time removes everything outside the framed band

XF-062 proves the high-frequency estimate

\[
\mathcal Q_M\!\left(
|\xi|>\frac{C\log\log T}{q},\tau
\right)=o(1)
\tag{24}
\]

for `C>C_*(\tau)` and every bounded source-compatible tangent family. Its infrared argument also works unchanged with the harmless factor `2` in (6). Indeed, using `|m(\xi)|\le|\xi|`, semigroup contraction, `M=q^2`, and `\|a(0)\|_\infty\le A_0`,

\[
\begin{aligned}
\mathcal Q_M(|\xi|<2q^{-3/2},\tau)
&\le
M^3(2q^{-3/2})^6\|a(\tau)\|_2^2\\
&\le128A_0^2M^4q^{-9}
=O_{A_0}(q^{-1})
=o(1).
\end{aligned}
\tag{25}
\]

Consequently

\[
\mathcal Q_M
\bigl(B_T^{\rm in}\cup(-B_T^{\rm in}),\tau\bigr)
=
\mathcal Q_M(( -\pi,\pi],\tau)+o(1).
\tag{26}
\]

XF-062 also gives

\[
\bigl(\mathcal F_M^{\rm lin}(\tau;a)\bigr)^2
\le\frac92\,
\mathcal Q_M(( -\pi,\pi],\tau).
\tag{27}
\]

Thus (9) implies

\[
\liminf_{T\to\infty}
\mathcal Q_M
\bigl(B_T^{\rm in}\cup(-B_T^{\rm in}),\tau\bigr)
\ge\frac{2c_0^2}{9}.
\tag{28}
\]

Substituting (28) into (8) proves (10).

This closes the exact logical gap between the two halves already established separately: XF-062 forces surviving tangent flux into the slow cone, and XF-059--XF-060 make the actual Xi source rapidly small in the derivative-weighted continuous selector norm on a slightly larger cone.

## 4. The actual Xi source remains negligible on the enlarged frame band

The outer band (7) is an XF-059 cone with infrared exponent `\delta=1/2` and a changed fixed upper constant. Hence XF-059 gives, for every fixed `B>0` and `t_0>0`,

\[
\sup_{0\le t\le t_0}
\sup_{\theta\in B_T^{\rm out}}
|\mathcal S_{T,\theta}(t)|
=O_B((\log T)^{-B}).
\tag{29}
\]

The derivative weight has the same polylogarithmic cost already estimated in XF-060:

\[
\sup_{\theta\in B_T^{\rm out}}
(M\theta^2)^2
=O((\log\log T)^4),
\tag{30}
\]

and

\[
M|B_T^{\rm out}|
=O(q\log\log T).
\tag{31}
\]

Therefore

\[
\boxed{
\sup_{0\le t\le t_0}
M\int_{B_T^{\rm out}}
(M\theta^2)^2
|\mathcal S_{T,\theta}(t)|^2d\theta
=o(1).
}
\tag{32}
\]

Equations (10) and (32) are a genuine matched separation at the periodic tangent level: fixed-time critical tangent flux forces an order-one weighted selector norm, while the actual Xi carrier has vanishing norm on the identical family of probes.

The comparison does **not** assert that Xi itself is an arithmetic-lattice tangent. It says that the selector family has no hidden frame defect within the model in which XF-062 performs the heat-regularized spectral reduction.

## 5. Stress tests and evidence boundary

The first stress test is XF-061's single-root defect. At `t=0` it carries critical flux almost entirely outside the slow band, so (8) does not claim to detect it. XF-062 proves that after any fixed `\tau>0` this specific tangent defect has `\mathcal F_M^{\rm lin}(\tau)=o(1)`. Thus the new frame and the sparse obstruction are compatible: the frame becomes decisive only after heat regularization has removed ultraviolet support.

The second stress test is a packet occupying many slow modes. There is no cancellation loophole in the selector energy at the periodic tangent level because (15)--(16) make the sidebands disjoint. Arbitrary phases and packet multiplicity disappear after taking the continuous `L^2(d\theta)` norm. This is stronger than the pure-wave and chirp checks of XF-058--XF-060.

The third stress test is the infrared edge. The proof does not attempt to frame modes at `\xi\asymp1/M`, where the selector band touches the zero-frequency background and the relative approximation in (21) fails. That omission is harmless after fixed heat time for the XF-062 flux normalization: (25) shows that all frequencies below `2q^{-3/2}` carry only `o(1)` tangent `H^3` energy under the bounded-displacement hypothesis.

The fourth boundary is finite amplitude. Formula (5) is the first variation of the exact moved-point statistic. Nonlinear root displacement can broaden sidebands and couple frequencies, so disjoint tangent bands do not by themselves produce a nonlinear frame. A future finite-amplitude theorem must control those Taylor/nonlinear commutators at the source-compatible scale rather than merely repeat the linear Plancherel argument.

The fifth boundary is transition geometry. The periodic tangent semigroup exists on the real-simple side and does not cross a collision or an interval of complex zeros. Moreover a collision-created critical defect may dissipate before any fixed positive delay. A source-to-transition theorem still needs either persistence of a collision-safe quantity or a nonlinear/collision-safe mechanism that reaches the heat-regularized regime.

These limitations prevent any RH upgrade. XF-063 closes a specific analytic frame gate inside the tangent repair of XF-062; it does not show `\Lambda\le0`.

## 6. Prior-art and novelty boundary

Poisson summation, Plancherel, Sobolev frequency weights, continuous short-time Fourier/Gabor frame identities, and compact-bandwidth constructions with diagonal or disjoint frame operators are classical. A targeted audit of Gabor/STFT frame theory, Littlewood--Paley/Sobolev square functions, heat-semigroup frequency splitting, and de Bruijn--Newman zero dynamics found the abstract frame mechanism to be standard and found no external theorem matching the Mathia-specific scale conjunction used here.

No novelty is claimed for the general principle that a compact-frequency window yields a painless frame or that derivative weights recover Sobolev energy. The durable line-specific content is the exact matching

\[
\text{selector half-width}=M^{-1},
\qquad
\text{periodic spacing}=\pi M^{-1},
\tag{33}
\]

\[
(M\theta^2)^2\times
\text{selector root-derivative symbol}
\quad\longleftrightarrow\quad
M^3|m(\xi)|^6,
\tag{34}
\]

on precisely the fixed-time surviving band of XF-062, together with the vanishing Xi estimate (32). The proof is self-contained from the Poisson/Plancherel machinery already used in XF-056--XF-060 and introduces no new load-bearing external source, so `SOURCES.md` requires no change.

## 7. Consequence for `xi_flow`

At the lattice tangent level, the spectral-support obstruction of XF-061 and the frame obstruction left open by XF-062 are now both closed after fixed positive heat time. A bounded tangent cannot retain order-one triple flux by hiding below the selector resolution, above the slow cone, between probe centers, across many phases, or in a packet of disjoint slow modes: the first two regions have `o(1)` heat-regularized `H^3` energy, the probe centers are continuous, and the remaining sidebands form the exact diagonal frame (8).

The next gate should therefore move **out of the tangent frame problem**. The useful question is whether this separation survives at finite amplitude and through source-to-transition geometry: either control nonlinear selector broadening/mode transfer strongly enough to obtain a finite-amplitude heat-regularized frame, or construct a source-compatible nonlinear trajectory whose transition flux remains critical after the necessary delay while its entire weighted moving-line selector norm stays small. A counterexample now has to exploit genuinely nonlinear or collision-time structure; another tangent-frequency construction cannot reopen the gate closed here.