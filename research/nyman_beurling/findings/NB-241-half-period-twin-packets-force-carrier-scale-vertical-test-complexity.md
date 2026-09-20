# NB-241 — Half-period twin packets force carrier-scale vertical test complexity

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + NEGATIVE/METHOD-BOUNDARY + MATCHED-CONTROL + CARRIER-SCALE-RESOLUTION + NB-237/NB-240-REFINEMENT + SOURCE-ONLY`.

`NB-237` identified the unresolved source observable as a microlocal signed average of the `R^{-1} zeta'/zeta` current, while `NB-238`--`NB-240` showed that published zero detectors, large-zeta-sum forcing, and fixed-test pair statistics are too coarse for the `Theta(1/R)` carrier packet. Those audits leave a sharper structural question: **what vertical test complexity is intrinsically required even before importing another zeta theorem?**

There is an exact matched-control answer for first-order local statistics. In the normalized Ford coordinate

\[
\tau:=H(\gamma-t),
\qquad
Y:=\frac XR,
\qquad
J:=\frac RH,
\]

the carrier frequency is

\[
\omega:=\frac XH=YJ.
\]

Construct two same-depth, same-population, same-spacing packets which differ only by a common **half carrier period**. Their normalized empirical measures are separated by `O(1/J)` in the Lipschitz/transport geometry, so every first-order test with derivative budget `o(YJ)` gives asymptotically the same answer on the two packets. Yet the exact Ford carrier gives `+1` on one packet and `-1` on the other. After restoring the `1/J` residue normalization and `Theta(J)` packet population, the two exact Ford contributions differ by order one.

Thus, in the Ford regime where `Y` stays bounded above and below, **carrier-scale vertical complexity `Theta(J)` in the normalized coordinate, equivalently physical resolution `Theta(1/R)`, is necessary in a sharp matched-control sense for any first-order detector intended to determine the unresolved coefficient.** Merely shrinking the height window while retaining a subcarrier smooth test cannot work.

## 1. Ford coordinate and the dangerous packet scale

Retain the notation used in `NB-231`--`NB-240`. At height `T`, write

\[
Q:=\log T,
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
X\asymp R,
\tag{1}
\]

and let the Ford smoothing width satisfy

\[
J:=\frac RH\to\infty.
\tag{2}
\]

Set

\[
Y:=\frac XR.
\tag{3}
\]

On the diagonal used throughout the current source analysis, there are fixed constants

\[
0<Y_-\le Y\le Y_+<\infty.
\tag{4}
\]

For a zero ordinate `gamma`, the normalized local coordinate is

\[
\tau=H(\gamma-t).
\tag{5}
\]

The phase appearing in the exact carrier is therefore

\[
e^{iX(\gamma-t)}
=
e^{i(X/H)\tau}
=
e^{i\omega\tau},
\qquad
\boxed{\omega=YJ.}
\tag{6}
\]

The `NB-231` transition packet lives at a common bounded Ford depth

\[
d:=X(1-\beta)-\log J=O(1)
\tag{7}
\]

and contains `Theta(J)` poles inside a fixed `tau`-window. Up to the common depth factor, each pole contributes at scale `1/J`; the unresolved order-one effect comes from coherent addition of `Theta(J)` such terms.

Equation (6) already suggests that a detector whose vertical complexity stays `o(J)` may be too smooth. The next lemma makes that sharp without any probabilistic or zeta-specific input.

## 2. Half-period twin lemma

Fix a sufficiently small constant `delta>0` and put

\[
M:=\lfloor\delta J\rfloor,
\qquad
a:=\frac{2\pi}{\omega}=\frac{2\pi}{YJ}.
\tag{8}
\]

Define two probability measures on the normalized ordinate coordinate by

\[
\mu_J
:=
\frac1M\sum_{j=0}^{M-1}\delta_{ja},
\qquad
\nu_J
:=
\frac1M\sum_{j=0}^{M-1}\delta_{(j+1/2)a}.
\tag{9}
\]

They have the same number of atoms, the same spacing `a`, and differ only by the common translation `a/2`.

### Lemma

For every complex-valued Lipschitz function `g`,

\[
\boxed{
\left|
\int g\,d\mu_J-
\int g\,d\nu_J
\right|
\le
\frac{\pi}{YJ}\operatorname{Lip}(g).
}
\tag{10}
\]

At the Ford carrier frequency itself,

\[
\boxed{
\int e^{i\omega\tau}\,d\mu_J=1,
\qquad
\int e^{i\omega\tau}\,d\nu_J=-1.
}
\tag{11}
\]

Hence the carrier separates the two controls by exactly `2`.

### Proof

Pair the `j`-th atom of `mu_J` with the `j`-th atom of `nu_J`. Their separation is `a/2`, so

\[
\begin{aligned}
\left|
\int g\,d\mu_J-
\int g\,d\nu_J
\right|
&\le
\frac1M
\sum_{j=0}^{M-1}
\left|g(ja)-g((j+1/2)a)\right|\\
&\le
\frac a2\operatorname{Lip}(g)\\
&=
\frac{\pi}{YJ}\operatorname{Lip}(g).
\end{aligned}
\tag{12}
\]

For the carrier test, `omega a=2 pi`, and therefore

\[
e^{i\omega ja}=1,
\qquad
 e^{i\omega(j+1/2)a}=-1
\tag{13}
\]

for every `j`. This proves (11). `square`

The estimate is already scale-sharp: the separating test `g(\tau)=e^{i\omega\tau}` has

\[
\operatorname{Lip}(g)=\omega=YJ.
\tag{14}
\]

Thus the exact observable itself sits precisely at the derivative scale where the matched controls cease to be forced together.

## 3. Fourier consequence: every subcarrier mode is blind

Taking

\[
g_\xi(\tau)=e^{i\xi\tau}
\]

in (10) gives

\[
\boxed{
\left|
\widehat\mu_J(\xi)-\widehat\nu_J(\xi)
\right|
\le
\frac{\pi|\xi|}{YJ}.
}
\tag{15}
\]

Consequently, for every frequency family satisfying

\[
|\xi_J|=o(YJ),
\tag{16}
\]

the two packets are asymptotically indistinguishable:

\[
\widehat\mu_J(\xi_J)-\widehat\nu_J(\xi_J)=o(1).
\tag{17}
\]

At the moving carrier frequency `xi_J=omega=YJ`, however, their difference is exactly `2` by (11).

More generally, any normalized first-order test family `g_J` with

\[
\operatorname{Lip}(g_J)=o(YJ)
\tag{18}
\]

is blind to the distinction. A band-limited representation also inherits this conclusion whenever its Fourier coefficient mass is uniformly controlled: bandwidth below the carrier cannot be compensated by unbounded coefficients without changing the norm of the detector.

The statement here is deliberately about **controlled first-order tests**, not arbitrary nonlinear statistics. No claim is made that every object colloquially called low-bandwidth is bounded by (10) without an accompanying norm control.

## 4. Translation back to the actual Ford packet

The normalized lattice spacing in (8) corresponds to physical ordinate spacing

\[
\frac aH
=
\frac{2\pi}{YJH}
=
\frac{2\pi}{X}
\asymp
\frac1R.
\tag{19}
\]

The half-period translation between the twins is

\[
\boxed{
\Delta\gamma
=
\frac{a}{2H}
=
\frac\pi X
\asymp
\frac1R.
}
\tag{20}
\]

Their full normalized diameter is

\[
Ma
=
\frac{2\pi M}{YJ}
=
\frac{2\pi\delta}{Y}+o(1),
\tag{21}
\]

so choosing `delta` small puts both packets inside an arbitrarily small fixed patch of the Ford window. In physical height the packet diameter is `O(1/H)`, exactly the regime already admitted in `NB-231`.

Now use the same-depth critical coefficient isolated there. For a fixed bounded depth `d`, its packet contribution has the form

\[
\mathcal R
=
\frac{e^{-r-d}}{J}
\sum_j
F(\tau_j)e^{i\omega\tau_j},
\tag{22}
\]

up to the already-recorded normalizations of the local carrier profile. The profile used in the line satisfies `F(0)>0` and is continuous. Choose `delta` small enough, using (4) and (21), that throughout the supports of both twins

\[
\Re F(\tau)\ge \frac34 F(0).
\tag{23}
\]

For the first packet, every carrier phase is `+1`; for the translated packet, every phase is `-1`. Hence

\[
\Re\mathcal R_{\mu}
\ge
\frac{3F(0)e^{-r-d}}4\frac MJ,
\tag{24}
\]

while

\[
\Re\mathcal R_{\nu}
\le
-\frac{3F(0)e^{-r-d}}4\frac MJ.
\tag{25}
\]

Since `M/J -> delta`,

\[
\boxed{
\liminf
\left|
\mathcal R_{\mu}-\mathcal R_{\nu}
\right|
\ge
\frac32\,\delta F(0)e^{-r-d}
>0.
}
\tag{26}
\]

Thus the matched controls do not merely change an abstract Fourier coefficient. They change the exact transition-scale Ford residue by order one while preserving population, depth, internal spacing, and window scale.

## 5. The sharp detector-resolution boundary

Suppose a proposed first-order local zero detector compresses the transition packet to statistics of the form

\[
\frac1J\sum_{j=1}^{M}g_J(\tau_j),
\qquad
M\asymp J.
\tag{27}
\]

Applying (10) and multiplying by `M/J=Theta(1)` gives

\[
\left|
\frac1J\sum g_J(\tau_j)
-
\frac1J\sum g_J(\tau'_j)
\right|
\ll
\frac{\operatorname{Lip}(g_J)}{YJ}.
\tag{28}
\]

Therefore

\[
\boxed{
\operatorname{Lip}(g_J)=o(YJ)
\quad\Longrightarrow\quad
\text{the detector cannot determine the Ford coefficient uniformly over the matched controls.}
}
\tag{29}
\]

By contrast, the exact carrier has derivative budget `YJ` and separates them by order one. The threshold is therefore sharp in scale for this testing model.

In the diagonal regime (4),

\[
YJ\asymp J.
\tag{30}
\]

In the original ordinate variable, a normalized derivative budget `Theta(YJ)` becomes physical frequency

\[
H(YJ)=X\asymp R,
\tag{31}
\]

or spatial resolution

\[
\boxed{\Delta\gamma\asymp R^{-1}.}
\tag{32}
\]

This converts the qualitative warning of `NB-238`--`NB-240` into an exact matched-control lower bound: **for first-order local tests, the `1/R` resolution demanded by the carrier is not merely a feature of the current proof architecture; a subcarrier smooth detector provably loses an order-one degree of freedom of the source coefficient.**

## 6. Relation to NB-240 and the live frontier

`NB-240` gave two theorem-specific obstructions for the new short-interval Montgomery statistic: its published error absorbs an entire `Theta(J)` Ford packet, and its fixed mean-spacing kernel suppresses the packet's off-diagonal carrier lattice. The present result is different. It makes no use of that pair theorem and does not depend on mean-zero spacing. It isolates the **first-order vertical resolution tariff** of the exact carrier itself.

This also sharpens what “retune the detector” must mean. Shortening the height interval alone is insufficient. A first-order replacement for the `R^{-1} zeta'/zeta` edge current must retain test variation on frequency scale

\[
\frac XH=YJ,
\tag{33}
\]

not merely localize its support to the correct `1/H` window. Equivalently, after returning to `gamma`, it must preserve information at ordinate displacement `Theta(1/R)`.

This is consistent with the growing-observable message of `NB-234`: fixed-complexity summaries can remain blind while the exact mark becomes increasingly oscillatory. The present matched control gives the vertical side a simple quantitative currency — derivative/Fourier budget — and identifies its sharp carrier scale.

It does **not** show that a carrier-scale detector suffices. Such a theorem would still have to preserve Ford depth, pole residues, deterministic height localization, and enough arithmetic structure of actual zeta zeros to yield the required `o(1)` estimate.

## 7. Prior-art and representation audit

The inequality (10) is generic transport geometry: two probability measures related by a translation of size `h` differ by at most `h Lip(g)` against a Lipschitz test. It is a direct elementary instance of the standard Lipschitz/Wasserstein dual viewpoint. Likewise, the fact that a Fourier test at frequency `omega` resolves translations of order `1/omega` is standard harmonic-analysis/signal-resolution background. **No novelty is claimed for either generic fact.**

The line-local contribution is the specialization to the exact Ford currencies:

\[
\omega=\frac XH=YJ,
\qquad
\frac1{\omega H}=\frac1X\asymp\frac1R,
\tag{34}
\]

together with the matched packet pair that keeps the admitted Ford depth, population and spacing fixed while flipping the transition residue by order one. This is the part that changes the research frontier after `NB-240`.

A targeted prior-art search covered Lipschitz/Wasserstein control of Fourier observables, band-limited resolution, and recent local-statistics work for zeta zeros. Those literatures contain the generic ingredients above but do not supply a theorem excluding the Ford twin controls or estimating the required depth-conditioned carrier coefficient for actual zeta zeros. Since the proof of the new boundary is self-contained and no external theorem is load-bearing, no new durable `SOURCES.md` anchor is required.

Representation audit: the lemma itself is **not arithmetic**. It would hold for any point measure tested by a moving Fourier carrier. The zeta-specific content enters only through the previously derived identification of the unresolved coefficient, the Ford relations `X asymp R`, `J=R/H`, the `Theta(J)` critical population budget, and the common-depth residue normalization in (22). Consequently this finding is a source-side detector boundary, not a new statement about the Nyman--Beurling distance.

## 8. Adversarial review and falsification boundary

Several restrictions are load-bearing.

First, `mu_J` and `nu_J` are **matched adversarial packets**, not assertions about the actual zero set of `zeta`. A zeta-specific theorem may exclude one or both packet geometries for reasons invisible to the generic test model. That would evade, not contradict, the obstruction.

Second, (29) concerns controlled **first-order linear statistics**. A nonlinear observable can extract information not represented by one Lipschitz test, and a carrier-scale two-point or higher-order theorem may rule out both twins simultaneously. The result therefore does not extend the negative conclusion of `NB-240` to every possible local zero statistic.

Third, the shorthand `Theta(J)` uses the diagonal assumption (4). Outside that regime the exact threshold is `Theta(YJ)=Theta(X/H)`, not `Theta(J)`.

Fourth, calling a detector “band-limited” is insufficient without controlling the norm of its Fourier coefficients. Large coefficients can amplify a small subcarrier distinction. The invariant statement is (10)/(29): the obstruction applies when the effective Lipschitz or bounded-Fourier-mass complexity is `o(YJ)`.

Fifth, the order-one Ford separation uses the existing shell profile with `F(0)>0` and chooses a sufficiently small fixed `delta`. If a future representation changes the profile, normalization, or source observable, the matched control must be rechecked against that exact object rather than imported automatically.

A decisive falsification of the present claim would be an admissible first-order family `g_J` with `Lip(g_J)=o(YJ)` for which the normalized statistics (27) differ by a fixed positive amount on the two explicitly defined packets. Inequality (12) rules that out exactly. What remains open is whether **actual zeta structure** supplies an independent reason those packets cannot occur, or a carrier-scale signed estimate that cancels them.

## 9. Consequence for the research line

The live source problem can now be stated more narrowly. A future theorem does not merely need “local zero information” or a shorter height interval. If it enters through a first-order local statistic, its test complexity must reach the moving carrier frequency

\[
\boxed{\omega=YJ=X/H,}
\]

which is `Theta(J)` on the Ford diagonal and corresponds to `Theta(1/R)` ordinate resolution. Below that scale there are explicit same-depth, same-population, same-spacing controls on which the detector converges to the same value while the exact Ford residue stays separated by order one.

The next source-side gain must therefore come from one of two genuinely stronger inputs: a **carrier-scale** signed estimate for the local logarithmic derivative/zero current, or a zeta-specific structural theorem that excludes the matched `Theta(J)` packet before such generic resolution is needed. Further localization with a subcarrier test does not address the obstruction.