# XF-133 — central packets hide exponentially from a fixed macroscopic local heat patch

**Status:** `EXACT-DERIVED` + `NEGATIVE/CONDITIONING-BOUNDARY` + `TEMPORAL-OBSERVABILITY` + `SPATIAL-OBSERVABILITY` + `UNIT-CIRCLE-ADMISSIBLE` + `CROSS-SCALE`. XF-130 proves that one off-circle heat trace determines the complete periodic unit-circle divisor exactly, while XF-132 shows that the temporal inversion of that one trace can be exponentially ill-conditioned even when observation starts at the target slice. One apparent repair is to add several nearby spatial probes, or even observe a whole local complex patch simultaneously. That does not remove the worst-case instability.

For even degree `N=2M`, use the XF-067 coefficient heat flow

\[
E(w,s)=\sum_{k=0}^{2M} E_k e^{-a k(2M-k)s}w^k,
\qquad a>0.
\tag{1}
\]

There is a real-palindromic coefficient direction `Delta E`, supported on central shells, with coefficient `ell^infinity` norm bounded below by an absolute constant, such that its complete future traces are exponentially small **uniformly over a two-dimensional complex family of spatial probes**. More precisely, for any integer `1<=r<M`, one may choose `Delta E` so that for

\[
\zeta_{\beta,N}:=-e^{\beta/N},
\qquad \beta\in\mathbb C,
\tag{2}
\]

one has, for every `B>=0`,

\[
\boxed{
\sup_{s\ge0}\sup_{|\beta|\le B}
|\Delta E(\zeta_{\beta,N},s)|
\le
 e^B\frac{(r!)^2}{(M^2-r^2)^r}.
}
\tag{3}
\]

Since `r!<=r^r`,

\[
\boxed{
\sup_{s\ge0,\ |\beta|\le B}
|\Delta E(\zeta_{\beta,N},s)|
\le
 e^B
\left(\frac{r^2}{M^2-r^2}\right)^r.
}
\tag{4}
\]

Taking

\[
r=\left\lfloor\frac M3\right\rfloor
\tag{5}
\]

gives

\[
\boxed{
\sup_{s\ge0,\ |\beta|\le B}
|\Delta E(\zeta_{\beta,N},s)|
\le e^B 8^{-r}.
}
\tag{6}
\]

Thus every spatial aperture with

\[
B_N\le \left(\frac{\log2}{2}-\eta\right)N
\tag{7}
\]

for fixed `eta>0` has an exponentially small singular direction:

\[
\boxed{
\sup_{s\ge0,\ |\beta|\le B_N}
|\Delta E(\zeta_{\beta,N},s)|
\le
\exp(-\eta N+O(1)).
}
\tag{8}
\]

The physical XF-067 coordinate satisfies

\[
w=-e^{-2\pi i z/L}.
\tag{9}
\]

Hence `(2)` corresponds locally to

\[
z=\frac{i\beta L}{2\pi N}.
\tag{10}
\]

Equation `(7)` therefore includes a genuine fixed macroscopic disk

\[
\boxed{
|z|
\le
\left(\frac{\log2}{4\pi}-\varepsilon\right)L
}
\tag{11}
\]

for any fixed `epsilon>0`, after choosing the corresponding positive `eta`. Numerically `log(2)/(4 pi)\approx0.055`. So the XF-132 instability is not repaired merely by replacing one root-spacing probe with finitely many probes, a growing number of probes, or even continuum access to the normalized heat solution on a local complex patch occupying a fixed small fraction of the whole period.

The bad direction again lies inside the exact simple unit-circle class: for every fixed `M`, arbitrarily small nonzero real multiples of `Delta E` can be added to `1+w^{2M}` while keeping all `2M` roots simple and on the unit circle. Therefore `(3)`--`(8)` give a local inverse condition-number obstruction on the admissible divisor manifold, not merely on the ambient coefficient space.

The conclusion remains deliberately about stable **full-state tomography**. It does not prove that the periodic Newman transition time itself is exponentially unstable at zero delay. A direct transition functional could still discard these central state directions. Nor does the theorem cover observation norms containing high spatial derivatives with exponentially increasing weights or spatial apertures comparable with an unrestricted fraction of the full period.

## 1. A probe-independent central divided-difference packet

Let the barycentric weights for the quadratic nodes

\[
0^2,1^2,\ldots,r^2
\tag{12}
\]

be

\[
\omega_j
:=
\frac{1}{\prod_{0\le \ell\le r,\ \ell\ne j}(j^2-\ell^2)},
\qquad 0\le j\le r.
\tag{13}
\]

As in XF-132,

\[
\omega_0=\frac{(-1)^r}{(r!)^2}.
\tag{14}
\]

Put

\[
W_r:=\max_{0\le j\le r}|\omega_j|,
\qquad
c_j:=\frac{\omega_j}{W_r}.
\tag{15}
\]

Then

\[
\max_j|c_j|=1,
\qquad
\frac1{W_r}\le(r!)^2.
\tag{16}
\]

The key modification from XF-132 is to choose the coefficient perturbation **before** choosing any spatial probe:

\[
\boxed{
\Delta E(w)
=
(-1)^M c_0 w^M
+
\frac12\sum_{j=1}^r
(-1)^{M-j}c_j
\left(w^{M-j}+w^{M+j}\right).
}
\tag{17}
\]

It is real and palindromic. Since some `|c_j|=1`, its coefficient sup norm satisfies

\[
\boxed{
\frac12\le
\|\Delta E\|_{\mathrm{coeff},\infty}
\le1.
}
\tag{18}
\]

For the probe `(2)`, one has exactly

\[
\zeta_{\beta,N}^{M-j}
+
\zeta_{\beta,N}^{M+j}
=
2(-1)^{M-j}e^{\beta/2}
\cosh\!\left(\frac{\beta j}{N}\right).
\tag{19}
\]

The central heat rates satisfy

\[
a(M-j)(M+j)=a(M^2-j^2).
\tag{20}
\]

Consequently the complete heat trace of `(17)` is

\[
\boxed{
\Delta Q_\beta(s)
:=
\Delta E(\zeta_{\beta,N},s)
=
 e^{\beta/2}e^{-aM^2s}
\sum_{j=0}^r
c_j e^{aj^2s}
\cosh\!\left(\frac{\beta j}{N}\right).
}
\tag{21}
\]

For a single fixed `beta`, this resembles the central packet of XF-132. The new point is that the same coefficients `c_j` work simultaneously for every `beta` in a complex patch.

## 2. Cauchy control makes the divided difference uniform in space and time

Set

\[
x:=as\ge0
\tag{22}
\]

and define the entire function of the quadratic spectral variable

\[
g_{x,\beta}(y)
:=
e^{xy}
\cosh\!\left(\frac{\beta\sqrt y}{N}\right).
\tag{23}
\]

There is no branch ambiguity in `(23)`: the even Taylor series of `cosh` makes it an entire power series in `y`.

By the definition of the barycentric weights,

\[
\sum_{j=0}^r c_j g_{x,\beta}(j^2)
=
\frac1{W_r}
[0^2,1^2,\ldots,r^2]g_{x,\beta},
\tag{24}
\]

where the bracket is the order-`r` divided difference.

Let

\[
R:=M^2-r^2>0.
\tag{25}
\]

For any real `y in [0,r^2]`, apply Cauchy's derivative estimate to `(23)` on the circle `|z-y|=R`. On this circle,

\[
|z|\le y+R\le M^2,
\qquad
\Re z\le M^2.
\tag{26}
\]

Since `N=2M`, for `|beta|<=B`,

\[
\left|
\cosh\!\left(\frac{\beta\sqrt z}{N}\right)
\right|
\le
\exp\!\left(\frac{|\beta|\sqrt{|z|}}N\right)
\le e^{B/2}.
\tag{27}
\]

Also

\[
|e^{xz}|\le e^{xM^2}.
\tag{28}
\]

Therefore

\[
\frac{|g_{x,\beta}^{(r)}(y)|}{r!}
\le
R^{-r}e^{xM^2+B/2}.
\tag{29}
\]

For real interpolation nodes, the elementary divided-difference mean-value/Hermite--Genocchi bound yields

\[
\left|
[0^2,1^2,\ldots,r^2]g_{x,\beta}
\right|
\le
R^{-r}e^{xM^2+B/2}.
\tag{30}
\]

Combining `(16)`, `(21)`, `(24)`, and `(30)`, and using `|e^{\beta/2}|<=e^{B/2}`, cancels the full heat factor `e^{-xM^2}` and gives

\[
|\Delta Q_\beta(s)|
\le
 e^B\frac{(r!)^2}{(M^2-r^2)^r}.
\tag{31}
\]

This proves `(3)`. The estimate is simultaneous in **all** `s>=0` and **all** complex `beta` in the disk; the heat coefficient `a` disappears entirely. As in XF-132, the observation of arbitrarily late times does not recover the hidden packet, but now neither does adding arbitrarily many bounded spatial samples inside the controlled patch.

Using `r!<=r^r` gives `(4)`. For `(5)`,

\[
\frac{r^2}{M^2-r^2}
\le\frac18,
\tag{32}
\]

so `(6)` follows. Since `r=N/6+O(1)`,

\[
8^{-r}
=
\exp\!\left(-\frac{\log8}{6}N+O(1)\right)
=
\exp\!\left(-\frac{\log2}{2}N+O(1)\right).
\tag{33}
\]

This proves `(7)`--`(8)` and the physical aperture `(11)`.

## 3. The obstruction also survives relative normalization on a fixed exterior patch

The target-side norm in `(3)` is absolute. There is nevertheless a clean relative version on any fixed patch that stays radially off the unit circle.

Take as base polynomial

\[
E_*(w)=1+w^{2M}.
\tag{34}
\]

Its heat evolution is stationary, because only the zero-rate endpoint coefficients are present. At `(2)`,

\[
Q_{*,\beta}(s)
=1+\zeta_{\beta,N}^{2M}
=1+e^\beta.
\tag{35}
\]

Fix `sigma_0>0`. On every probe region satisfying

\[
\Re\beta\ge\sigma_0,
\tag{36}
\]

one has

\[
|1+e^\beta|
\ge e^{\sigma_0}-1.
\tag{37}
\]

For

\[
E_\varepsilon=E_*+\varepsilon\Delta E,
\tag{38}
\]

therefore

\[
\boxed{
\sup_{s\ge0}
\sup_{\substack{|\beta|\le B\\\Re\beta\ge\sigma_0}}
\left|
\frac{Q_{\varepsilon,\beta}(s)}{Q_{*,\beta}(s)}-1
\right|
\le
\frac{|\varepsilon|}{e^{\sigma_0}-1}
 e^B\frac{(r!)^2}{(M^2-r^2)^r}.
}
\tag{39}
\]

Thus on a fixed one-root-spacing exterior complex patch, where `B` and `sigma_0` are constants, the **relative** whole-history signal of the central packet is exponentially small as well. This does not by itself identify the relative norm produced by the actual Xi Gaussian-reference interface, but it rules out the idea that the instability of XF-132 is merely caused by measuring an unnormalized value at one unlucky point.

## 4. The simultaneous bad direction lies in the simple unit-circle divisor class

It remains to verify that `(17)` is a tangent direction to admissible real divisors. For real `epsilon`, divide `(38)` by `w^M` and put

\[
z=w+w^{-1}.
\tag{40}
\]

Then

\[
w^{-M}E_\varepsilon(w)
=R_\varepsilon(z),
\tag{41}
\]

where

\[
R_\varepsilon(z)
=
2T_M(z/2)
+
\varepsilon\left[
(-1)^M c_0
+
\sum_{j=1}^r(-1)^{M-j}c_jT_j(z/2)
\right].
\tag{42}
\]

The perturbation in brackets has degree at most `r<M`. At `epsilon=0`, the `M` roots of `R_0` are simple and strictly inside `(-2,2)`. For each fixed `M`, sufficiently small real `epsilon` preserves one simple real root near each of them and hence preserves all `M` roots inside `(-2,2)`. Every such root lifts through `(40)` to two distinct conjugate unit-circle roots of `E_epsilon`. Therefore

\[
\boxed{
E_\varepsilon
\text{ has }2M\text{ simple unit-circle roots}
}
\tag{43}
\]

for all sufficiently small nonzero real `epsilon`.

The admissible radius may shrink with `M`; this is irrelevant to the local conditioning ratio. From `(18)` and `(31)`,

\[
\frac{
\|E_\varepsilon-E_*\|_{\mathrm{coeff},\infty}
}{
\sup_{s\ge0,\ |\beta|\le B}
|Q_{\varepsilon,\beta}(s)-Q_{*,\beta}(s)|
}
\ge
\frac12 e^{-B}
\frac{(M^2-r^2)^r}{(r!)^2}.
\tag{44}
\]

With `r=floor(M/3)` and `B=B_N` satisfying `(7)`, any local Lipschitz inverse from this heat-patch sup norm to coefficient space has condition number at least

\[
\boxed{
\exp(\eta N-O(1)).
}
\tag{45}
\]

This is a statement internal to an open simple unit-circle neighborhood.

## 5. Relation to XF-081, XF-130, and XF-132

XF-081 already showed that static center-local function approximation has a large Chebyshev nullspace: locally invisible trigonometric corrections can prescribe growing Vieta edge prefixes. That result deliberately did not require the repaired surrogate to be a real divisor and did not use its full heat history. XF-133 is different in both respects. The perturbations `(38)` remain simple unit-circle divisors, and the exponentially small bound holds simultaneously through the exact coefficient heat flow for every future time.

XF-130 remains an exact injectivity theorem. Exact data on even one off-circle probe determine the divisor. Equation `(45)` says that replacing exact equality by a quantitative source-transfer estimate changes the problem completely: nearby admissible divisors can differ in a central coefficient direction by an exponentially larger amount than their entire observed heat patch.

XF-132 established this at one fixed root-spacing probe. XF-133 closes the most immediate multi-channel escape. If all additional spatial channels stay inside a local aperture satisfying `(7)`, their joint sup-norm observation still has the same exponential singular direction. In particular, increasing channel count does not help if the channels only oversample the same local analytic patch.

This does **not** contradict the positive real-divisor dictionary in XF-083. That theorem uses logarithmic-derivative information on a high line; the present observable is the normalized function value of XF-130. The distinction matters near the unit-circle zero set, and no inference from `(45)` to an XF-083 log-derivative norm is being made.

## 6. Prior-art boundary

Exponential observation and control costs for heat equations are classical. The Lebeau--Robbiano spectral-inequality method and later formulations such as Miller, *A direct Lebeau--Robbiano strategy for the observability of heat-like semigroups* (DCDS-B 14 (2010), DOI `10.3934/dcdsb.2010.14.1465`), and Apraiz--Escauriaza--Wang--Zhang, *Observability inequalities and measurable sets* (JEMS 16 (2014), DOI `10.4171/JEMS/490`), provide the broad neighboring framework in which local spatial observation of parabolic evolution naturally carries exponential spectral costs. Severe conditioning of clustered exponential sums is likewise classical and was already audited in XF-132.

Those theories are not load-bearing for `(17)`--`(45)`. The present proof is the explicit combination of the exact quadratic XF-067 heat spectrum, a probe-independent barycentric packet, Cauchy control in the quadratic spectral variable, and the palindromic Chebyshev lift that keeps the direction inside the unit-circle divisor class. The directed audit did not locate an external theorem matching this finite-dimensional periodic construction or its aperture constant. No new external dependency is therefore added to `SOURCES.md`.

The constant `log(2)/(4 pi)` in `(11)` is not claimed optimal. It comes from the convenient choice `r=floor(M/3)`. Optimizing the packet depth changes the numerical aperture but not the qualitative conclusion that a nonzero fixed fraction of the period can remain exponentially ill-conditioned.

## 7. Consequence for the Xi source bridge

After XF-130--XF-133, the target-side one-channel route has a sharper boundary. Exact cross-scale observability can be compressed to one root-spacing off-circle history, but **stable unrestricted divisor reconstruction cannot be recovered merely by sampling more densely near that same spatial location**. Even complete future heat data on a fixed local complex patch have exponentially small admissible directions.

A source-faithful continuation therefore needs at least one ingredient outside this obstruction: source accuracy exponential on the degree scale; a genuinely macroscopic/global spatial observation beyond the controlled local aperture; a preconditioned norm that directly measures the hidden central spectral directions; Xi-specific structure excluding those directions; or a direct statistic-to-transition theorem that never reconstructs the unrestricted Vieta state.

The last option remains especially important. XF-131 is still the transition-sharp obstruction when positive heat delay is present, while XF-132--XF-133 concern full-state inversion at zero delay. No upper bound on the actual de Bruijn--Newman constant follows from this finding, and no actual Xi divisor is asserted to realize the control family.