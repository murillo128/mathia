# XF-079 — disjoint selector sidebands make the weighted Vieta resource center-pointwise

**Status:** `EXACT-DERIVED` + `SOURCE-NORM-LOCALIZATION` + `DESTINATION-MATCHED` + `STRUCTURAL/REPAIR`. XF-069 recovers periodic power sums by Fourier analysis in the translated selector center, and XF-070 uses Parseval in that center to obtain the weighted log-Vieta resource matched to the XF-065--XF-066 `H^3` destination geometry. That presentation makes a full scan through one periodic center interval look load-bearing for the source-to-periodic interface.

For the actual window already fixed in those findings, it is not. The compact Fourier support

\[
\chi=\widehat g\in C_c^\infty((-1,1))
\]

and the normalization `N=2M` put adjacent selector sidebands at scaled distance `pi>2`. Hence the sidebands are disjoint. At each physical frequency `theta`, at most one center Fourier harmonic is present. Consequently the modulus of the periodic selector is **exactly independent of the translated center**, and the center-averaged XF-070 resource equals the same weighted norm at every single center.

More precisely, with

\[
\xi_k=\frac{2\pi k}{N}=\frac{\pi k}{M},
\qquad
P_k=\sum_{j=0}^{N-1}e^{-i\xi_kx_j},
\]

one has the exact Fourier expansion

\[
\boxed{
\mathcal S_r(\theta)
=
\frac{M}{N}
\sum_{k\in\mathbb Z}
\chi\!\bigl(M(\theta-\xi_k)\bigr)
P_k e^{i\xi_k r}.
}
\tag{1}
\]

Since `supp(chi) subset (-1,1)` and

\[
M(\xi_{k+1}-\xi_k)=\pi,
\]

for every `theta` there is at most one index `k` with a nonzero summand in (1). Therefore

\[
\boxed{
|\mathcal S_r(\theta)|
\text{ is independent of }r.
}
\tag{2}
\]

For every measurable frequency set `B`, the exact XF-070 norm thus satisfies, for **every** center `r_0`,

\[
\boxed{
\|\mathcal S_{r_0}\|_{X(B)}^2
=
\frac1N\int_0^N\|\mathcal S_r\|_{X(B)}^2\,dr
=
\frac1{4M^2}
\sum_{k\in\mathbb Z}|P_k|^2
\int_{U_{k,B}}(\pi k+u)^4|\chi(u)|^2\,du.
}
\tag{3}
\]

At the exact DFT node `theta=xi_k` the statement is even pointwise:

\[
\boxed{
P_k
=
\frac{2}{\chi(0)}
 e^{-i\xi_k r_0}
\mathcal S_{r_0}(\xi_k).
}
\tag{4}
\]

Thus the full-center mismatch introduced as a sufficient interface target in XF-069 is strictly stronger than necessary for the weighted source state. A source-to-periodic theorem may work at one safe center and still control the entire XF-070 visible weighted resource. This removes a center-coverage mismatch between the center-local Gaussian/Appell route of XF-073--XF-078 and the weighted Vieta source norm. It does **not** yet convert the Gaussian quotient into the periodic selector, and it does not provide the positive-`Lambda` transition mass required at the destination.

## 1. Fourier reconstruction already gives the full center dependence

Use the periodic index-coordinate model of XF-069,

\[
M=q^2,
\qquad
N=2M,
\qquad
x_{j+N}=x_j+N,
\tag{5}
\]

and

\[
\mathcal S_r(\theta)
:=
\sum_{j\in\mathbb Z}
 g\!\left(\frac{x_j-r}{M}\right)
 e^{-i\theta(x_j-r)}.
\tag{6}
\]

The function `r -> S_r(theta)` is `N`-periodic. XF-069 proves that its `k`th center-Fourier coefficient is

\[
\frac1N\int_0^N
\mathcal S_r(\theta)e^{-i\xi_kr}\,dr
=
\frac{M}{N}
\chi\!\bigl(M(\theta-\xi_k)\bigr)P_k.
\tag{7}
\]

Because `g` is Schwartz, the translated sum and its center Fourier series are absolutely well behaved on the real periodic configuration used in XF-069. Fourier reconstruction of (7) gives (1). No new approximation is introduced.

Define the sideband

\[
I_k
:=
\left\{\theta:
|M(\theta-\xi_k)|<1
\right\}.
\tag{8}
\]

The centers of consecutive sidebands have scaled separation `pi`, while each sideband has scaled radius one. Hence the `I_k` are pairwise disjoint. If `theta in I_k`, equation (1) collapses to

\[
\boxed{
\mathcal S_r(\theta)
=
\frac12
\chi\!\bigl(M(\theta-\xi_k)\bigr)
P_k e^{i\xi_k r}.
}
\tag{9}
\]

If `theta` lies in no sideband, the selector is zero. Equation (2) follows immediately. The center variable carries only a phase once the physical frequency has selected a sideband.

## 2. XF-070 Parseval is therefore pointwise in the center

XF-070 defines

\[
\|F\|_{X(B)}^2
:=M^3\int_B\theta^4|F(\theta)|^2\,d\theta.
\tag{10}
\]

Substituting (9) directly, without averaging in `r`, gives

\[
\|\mathcal S_{r_0}\|_{X(B)}^2
=
\frac{M^3}{4}
\sum_k|P_k|^2
\int_{B\cap I_k}
\theta^4
\left|\chi\!\bigl(M(\theta-\xi_k)\bigr)\right|^2d\theta.
\tag{11}
\]

With `u=M(theta-xi_k)` and `M xi_k=pi k`, this becomes

\[
\|\mathcal S_{r_0}\|_{X(B)}^2
=
\frac1{4M^2}
\sum_k|P_k|^2
\int_{U_{k,B}}
(\pi k+u)^4|\chi(u)|^2du,
\tag{12}
\]

which is exactly the XF-070 center-Parseval identity. Thus the center average in that derivation is a valid proof device but not extra information. Equation (3) holds at every center.

If `I_k subset B`, the corresponding coefficient weight remains

\[
w_k
=
\frac1{4M^2}
\int_{-1}^{1}
(\pi k+u)^4|\chi(u)|^2du
\asymp_g\frac{k^4}{M^2}.
\tag{13}
\]

Hence all consequences of XF-070 concerning the `k^6/M^2` log-Vieta weight, the `delta<4/7` infrared threshold, and the tangent match to the `M^3H^3` destination geometry remain unchanged. What changes is the localization burden required to access that resource.

## 3. One safe-center interface estimate is enough

Let `S_r^per` be a periodic surrogate selector and `S_r^Xi` the actual Xi source statistic in the same normalization. Fix a center `r_0` for which the Xi source estimate and the interface comparison are valid. On a source-visible band `B`, suppose

\[
\|\mathcal S_{r_0}^{\Xi}\|_{X(B)}
\le \varepsilon_{\rm src},
\qquad
\|\mathcal S_{r_0}^{\rm per}
-
\mathcal S_{r_0}^{\Xi}\|_{X(B)}
\le \varepsilon_{\rm int}.
\tag{14}
\]

Then the triangle inequality and (3) give the exact conditional transfer

\[
\boxed{
\left[
\frac1{4M^2}
\sum_k|P_k^{\rm per}|^2
\int_{U_{k,B}}(\pi k+u)^4|\chi(u)|^2du
\right]^{1/2}
\le \varepsilon_{\rm src}+\varepsilon_{\rm int}.
}
\tag{15}
\]

No supremum over centers and no normalized `L^2([0,N]_r)` mismatch is required. At a DFT node inside the source cone, the corresponding pointwise statement from (4) is

\[
|P_k^{\rm per}|
\le
\frac{2}{|\chi(0)|}
\left(
|\mathcal S_{r_0}^{\Xi}(\xi_k)|
+
|\mathcal S_{r_0}^{\rm per}(\xi_k)
-
\mathcal S_{r_0}^{\Xi}(\xi_k)|
\right).
\tag{16}
\]

The improvement over XF-069 is not a better estimate of the interface error; it is a smaller domain on which that error needs to be proved.

## 4. Relation to the Gaussian/Appell center-local route

XF-073 proves relative Xi recovery for the Gaussian/Appell quotient on

\[
|\Re z|\le L/4
\tag{17}
\]

with super-polynomial error on the moving high line. XF-078 shows that the matched Gaussian quotient is also finitely compressible on this same center rectangle at the ordinary Vieta mode count, despite its global seam bandwidth obstruction.

The source geometry in (15) may now choose `r_0=0`, or any other center whose physical shift `sr_0` lies inside the safe center region. Therefore the Gaussian route does **not** have to extend its source comparison across an entire physical period merely to satisfy the center average appearing in XF-070. In particular, the theta seam of XF-074--XF-077 cannot be reintroduced solely by arguing that the weighted Vieta source norm itself demands a full-center scan.

A genuine interface theorem is still missing. XF-073 controls a relative quotient of heat solutions, while (14) asks for the destination-matched selector statistic associated with a periodic Vieta surrogate. Passing from the former to the latter must control the finite surrogate construction, logarithmic normalization, any auxiliary roots, and the residual created when the frozen center-local approximation is transported in heat. XF-079 removes only the artificial **center-coverage** part of that burden.

## 5. Stress tests and failure boundary

The support separation is load-bearing. More generally, the argument works whenever the scaled support radius of `chi` is strictly below `pi/2`. If two neighboring translated supports overlap, equation (1) contains two or more center harmonics at the same `theta`; cross terms then depend on `r`, and center averaging becomes genuinely different from a single slice. The present Mathia window has the stronger fixed support `supp(chi) subset (-1,1)`, so it has a uniform separation margin.

The exact node formula (4) also uses `chi(0) != 0`, already part of the XF-069 admissible window. A clipped band `B` causes no difficulty for (3): it merely replaces the full sideband weight by `U_{k,B}` exactly as in XF-070.

The proof has the same periodic-real source scope as XF-069. It does not assert that an arbitrary nonperiodic Xi statistic has center-independent modulus, nor that a periodic surrogate exists with small `epsilon_int`. It also does not upgrade the tangent `H^3` identification of XF-070 to a nonlinear equivalence with the XF-066 transition criterion.

Finally, source localization is only one of the two major gates. Even a perfect one-center transfer in (15), followed by the guarded periodic transport of XF-071, would still need a theorem that a hypothetical positive-`Lambda` transition produces nonvanishing guarded destination mass. Nothing here supplies that transition theorem or an upper bound on `Lambda`.

## 6. Prior-art and novelty boundary

Equation (1) is ordinary Fourier reconstruction of the XF-069 translated-window coefficient formula, and the disjoint-support step is the classical no-aliasing regime of Poisson-summation/Gabor or filter-bank analysis. The literature audit found the expected neighboring sampling and Gabor-frame framework; no novelty is claimed for Fourier reconstruction, sideband separation, or the fact that a single active harmonic has center-independent modulus. No external theorem is load-bearing, so `SOURCES.md` does not need a new anchor.

The line-specific mathematical delta is the observation that the **exact support constants already chosen in XF-069--XF-070 force this no-aliasing regime**. Consequently the supposedly center-averaged destination-matched Vieta resource is exactly pointwise in center, equations (3) and (15) replace the full-center interface target by a one-center target, and the center-local Gaussian/Appell program no longer has a center-domain mismatch with the weighted source norm.

## 7. Consequence for `xi_flow`

The live Gaussian-to-Vieta bridge is narrower after XF-079. XF-073 supplies actual Xi data on a safe center-local high-line rectangle; XF-078 shows that ordinary Vieta bandwidth is sufficient there for a matched control; XF-079 now shows that the XF-070 weighted source resource itself can be read at one such center. A future positive bridge therefore does not need to cross the Gaussian theta seam just to average over selector centers.

The remaining source obligation is an **object/dictionary problem rather than a center-coverage problem**: turn the center-local Gaussian quotient (or a controlled finite surrogate of it) into the periodic selector/log-Vieta state with `o(1)` error in the exact `X(B)` norm at one safe center. XF-071 then already supplies guarded periodic heat transport once that weighted source resource is small. Separately, a positive-`Lambda` state must still be shown to carry order-one guarded destination mass. No consequence for RH is claimed before those source-dictionary and transition gates are both closed.