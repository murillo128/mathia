# ANF-084 — a moving Euler-product line gives superpolynomial relative Xi periodization

**Status:** `LITERATURE+DERIVED + XI-SOURCE-INTERFACE + ZERO-FREE-EULER-PRODUCT-LINE + RELATIVE-PERIODIZATION + DERIVATIVE-STABLE + GAUSSIAN-PRIME-LEAKAGE`. The accepted clue `CLUE-gaussian-xi-source-periodization-relative-error` left a specific source-side gate: a Gaussian periodization of the actual Riemann Xi function had to be controlled **relative to Xi itself**, on a moving zero-free line, with enough uniformity to survive fixed-order differentiation. That gate can be closed without RH and without any positive-time Euler product.

Write

\[
H_0(z):=\frac18\xi\!\left(\frac12+\frac{iz}{2}\right),
\qquad
\xi(s):=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{1}
\]

For `T` sufficiently large put

\[
\ell:=\log T,
\qquad
\sigma_T:=1+\ell^{-1},
\qquad
a_T:=2\sigma_T-1=1+2\ell^{-1},
\tag{2}
\]

\[
w:=\ell,
\qquad
L:=\ell^3,
\qquad
U_T(z):=H_0(T+z),
\qquad
V_T(z):=e^{-z^2/(2w^2)}U_T(z),
\tag{3}
\]

and periodize

\[
V_{T,L}(z):=\sum_{m\in\mathbb Z}V_T(z+mL).
\tag{4}
\]

Then there is an absolute constant `C>0` such that on the moving rectangle

\[
\mathcal R_T:=
\left\{z=x+ib:
|x|\le\frac L4,
\ |b-a_T|\le\frac1\ell
\right\}
\tag{5}
\]

the denominator `V_T(z)` is zero-free, the image sum in (4) converges normally, and

\[
\boxed{
\left|\frac{V_{T,L}(z)}{V_T(z)}-1\right|
\le
C\ell^{11}\exp\!\left(-\frac{\ell^4}{8}\right).
}
\tag{6}
\]

Moreover, for every fixed integer `k>=0` there is `C_k>0` such that, on the center line `z=x+ia_T` with `|x|<=L/5`,

\[
\boxed{
\left|\partial_z^k\left(\frac{V_{T,L}}{V_T}-1\right)(z)\right|
+
\left|\partial_z^k\log\frac{V_{T,L}}{V_T}(z)\right|
\le
C_k\ell^{11+k}e^{-\ell^4/8}.
}
\tag{7}
\]

The logarithm is the analytic branch tending to zero with the image error. Thus every fixed derivative seminorm of the **relative/logarithmic source error** is smaller than any negative power of `log T`. This resolves the moving-line, denominator, normal-convergence, and fixed-derivative pieces of the accepted source clue. What remains is destination-specific: one must still prove that the reference-divided positive-time transport and its actual normalized target norm have only polynomial-or-better conditioning and retain a nontrivial transition signal.

## 1. The reflected source strip stays uniformly inside the Euler-product half-plane

For `z=x+ib`, the functional equation `xi(s)=xi(1-s)` gives

\[
U_T(z)
=\frac18\xi\!\left(
\frac12-\frac{i(T+z)}2
\right)
=\frac18\xi\!\left(
\frac12+\frac b2-\frac{i(T+x)}2
\right).
\tag{8}
\]

If `z in R_T`, its reflected Xi argument has real part

\[
\sigma(z)=\frac12+\frac b2
\in
\left[
1+\frac1{2\ell},
1+\frac3{2\ell}
\right].
\tag{9}
\]

Hence `Re s>1` throughout the whole rectangle, not merely on its center line. In particular `zeta(s)` and therefore `xi(s)` are zero-free there. The same is true after every real translation `z -> z+mL`, because that translation changes only the ordinate of the reflected Xi argument. Thus `V_T` is zero-free on `R_T` and all relative quotients below are legitimate without assuming anything about critical-line zeros.

For `sigma>1`, the Euler product gives the elementary bounds

\[
\frac1{\zeta(\sigma)}
\le
|\zeta(\sigma+it)|
\le
\zeta(\sigma),
\tag{10}
\]

where the lower bound follows, for example, from

\[
|1/\zeta(\sigma+it)|
\le\prod_p(1+p^{-\sigma})
=\frac{\zeta(\sigma)}{\zeta(2\sigma)}
\le\zeta(\sigma).
\]

Also

\[
\zeta(\sigma)
\le1+\frac1{\sigma-1}.
\tag{11}
\]

On (9), therefore, every Euler-product loss is at most polynomial in `ell`; specifically the numerator/denominator ratio below costs only `O(ell^2)`.

## 2. Two-sided Stirling bounds give the exact image-shift cost

Let

\[
t_0:=-\frac{T+x}{2},
\qquad
t_m:=t_0-\frac{mL}{2},
\qquad
p_\sigma:=\frac{\sigma+3}{2}.
\tag{12}
\]

Because `L=(log T)^3=o(T)`, uniformly for `|x|<=L/4` one has `|t_0|\asymp T`. Uniform two-sided Stirling bounds for `Gamma(s/2)` on `1<=Re s<=2`, together with (10)--(11), imply for all sufficiently large `T`

\[
|\xi(\sigma+it_0)|
\ge
c\ell^{-1}(1+|t_0|)^{p_\sigma}
 e^{-\pi|t_0|/4},
\tag{13}
\]

and, uniformly for every real `t`,

\[
|\xi(\sigma+it)|
\le
C\ell(1+|t|)^{p_\sigma}
 e^{-\pi|t|/4}.
\tag{14}
\]

The bounded-`t` part of (14) is absorbed by continuity of the entire Xi function on `1<=sigma<=2`; no small-ordinate Stirling assertion is being made. The large ordinate in the denominator is the only place where the lower Stirling bound is used.

The real part `sigma` is identical for `z` and `z+mL`. Since

\[
|t_m-t_0|=\frac{|m|L}{2}
\]

and `p_sigma<3` for large `T`, equations (13)--(14) yield

\[
\boxed{
\left|\frac{U_T(z+mL)}{U_T(z)}\right|
\le
C\ell^2(1+|m|L)^3
\exp\!\left(\frac{\pi|m|L}{8}\right).
}
\tag{15}
\]

The coefficient `pi/8` is forced by the `z/2` normalization in (1): the Gamma decay is `e^{-pi|t|/4}`, while a real translation by `mL` changes the Xi ordinate by exactly `mL/2`.

## 3. Gaussian suppression dominates every translated Xi image

For `z=x+ib`, the Gaussian ratio is exact:

\[
\left|
\exp\!\left(
-\frac{(z+mL)^2-z^2}{2w^2}
\right)
\right|
=
\exp\!\left(
-\frac{m^2L^2+2mLx}{2w^2}
\right).
\tag{16}
\]

If `|x|<=L/4` and `m\ne 0`, then

\[
m^2L^2+2mLx
\ge
m^2L^2-\frac{|m|L^2}{2}
\ge
\frac{m^2L^2}{2},
\]

so

\[
\left|
\frac{e^{-(z+mL)^2/(2w^2)}}{e^{-z^2/(2w^2)}}
\right|
\le
\exp\!\left(-\frac{m^2L^2}{4w^2}\right).
\tag{17}
\]

For `ell>=pi`, the chosen scales satisfy `L>=pi w^2`. Combining (15) and (17),

\[
\left|\frac{V_T(z+mL)}{V_T(z)}\right|
\le
C\ell^2(1+|m|L)^3
\exp\!\left(-\frac{m^2L^2}{8w^2}\right).
\tag{18}
\]

Because `L^2/w^2=ell^4`, the right-hand side is summable normally on `R_T`. Summing `m\ne0` and using

\[
(1+m\ell^3)^3\ll m^3\ell^9
\qquad(m>=1)
\]

gives

\[
\sum_{m\ne0}
\left|\frac{V_T(z+mL)}{V_T(z)}\right|
\le
C\ell^{11}
\sum_{m\ge1}m^3e^{-m^2\ell^4/8}
\le
C'\ell^{11}e^{-\ell^4/8},
\tag{19}
\]

which proves (6). The estimate is genuinely relative: no lower bound for `|H_0|` on or near the critical line is imported, and the potentially tiny Gamma factor has already cancelled through the quotient on the zero-free reflected line.

## 4. Cauchy turns the same estimate into fixed-order logarithmic control

Take any `z_0=x+ia_T` with `|x|<=L/5`. For large `T`, the disk

\[
|z-z_0|\le\frac1{2\ell}
\]

lies inside `R_T`. Applying Cauchy's estimate to the analytic relative error

\[
R_T(z):=\frac{V_{T,L}(z)}{V_T(z)}-1
\]

and (6) gives, for fixed `k`,

\[
|R_T^{(k)}(z_0)|
\le
k!(2\ell)^k
C\ell^{11}e^{-\ell^4/8}.
\tag{20}
\]

For sufficiently large `T`, the bound in (6) is below `1/2`; hence `1+R_T` is zero-free on the same disks and the analytic branch `log(1+R_T)` satisfies `|log(1+R_T)|<=2|R_T|`. A second application of Cauchy gives the logarithmic half of (7).

Thus any **fixed** derivative order costs only another polynomial power of `log T`. This is the precise point needed by a later normalized source norm: Gaussian image suppression is so strong that no fixed-order Cauchy loss can consume it. A destination norm whose order or conditioning itself grows superpolynomially is not covered by this statement and must be analyzed separately.

## 5. The prime part has an independent Gaussian leakage bound

The same moving line also gives a clean frequency-separation estimate for the Euler-product derivative. For `sigma>1`, absolute convergence permits

\[
-\frac{\zeta'}{\zeta}(\sigma+iy)
=\sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}e^{-iy\log n}.
\tag{21}
\]

Therefore, for any real center `Y`, width `w>0`, and `|omega|<=omega_0<log 2`, termwise Gaussian integration gives

\[
\begin{aligned}
&\left|
\int_{\mathbb R}
 e^{-(y-Y)^2/(2w^2)}
 \left(-\frac{\zeta'}{\zeta}(\sigma+iy)\right)
 e^{i\omega(y-Y)}dy
\right|\\
&\qquad\le
\boxed{
\sqrt{2\pi}\,w
\left(-\frac{\zeta'}{\zeta}(\sigma)\right)
\exp\!\left(
-\frac{w^2(\log2-\omega_0)^2}{2}
\right).
}
\end{aligned}
\tag{22}
\]

At `sigma=sigma_T` and `w=ell`, the classical pole behavior `-zeta'/zeta(1+1/ell)=O(ell)` makes (22) `O(ell^2 e^{-c ell^2})` for every fixed `omega_0<log 2`. In the `z/2` coordinate of (1), the first prime frequency is correspondingly `log 2/2`. This leakage is slower than the image error (6) but still beats every negative power of `log T`.

Equation (22) is independent of the periodization argument and does not smuggle in a compact Fourier cutoff: it quantifies exactly what is paid when the compact cutoff is replaced by a Gaussian source window.

## 6. Adversarial audit and evidence boundary

There are six load-bearing checks. First, the functional equation is applied before any lower bound, moving the whole denominator neighborhood to `Re s>1`; no zero-free assertion is made in the critical strip. Second, the same reflected real part is used for every translated image, so the moving Euler-product deterioration is only polynomial and does not accumulate an additional `m`-dependent strip loss. Third, the Gamma exponential changes by at most `exp(pi|m|L/8)`, not `exp(pi|m|L/4)`, because the Xi ordinate moves by `mL/2`. Fourth, the Gaussian estimate is uniform in the imaginary part of `z`, since only `Re z` enters the modulus of (16). Fifth, differentiation is performed only after normal convergence and zero-freeness of the relative quotient have been established on a nonzero-width rectangle. Sixth, the prime estimate uses the absolutely convergent von Mangoldt series only at `sigma>1` and says nothing about a positive-time Euler product.

The Xi normalization and de Bruijn--Newman heat-flow framework are classical; Polymath15 uses exactly the normalization (1) and develops effective estimates for `H_t`. The functional equation, Euler product, and uniform Gamma asymptotics used in (8)--(15) are classical, with standard references in DLMF sections 25.4 and 5.11. Gaussian periodization and Cauchy estimates are likewise classical. A targeted search did not locate a source giving the specific moving-line **relative** image estimate (6), its fixed-derivative logarithmic form (7), or the particular scale splice `sigma-1=1/log T`, `w=log T`, `L=(log T)^3`; those are derived here from the classical ingredients. No publication-level novelty claim is made.

This finding is source-side only. It does not prove stability of the reference-divided state under positive heat time, does not identify the destination weighted norm, does not show that the retained state is nonzero when `Lambda>0`, and does not imply RH. In particular, the Euler product is never propagated to `H_t` for `t>0`.

## 7. Consequence for the live source clue

The accepted clue `CLUE-gaussian-xi-source-periodization-relative-error` no longer has a moving-contour or differentiated-image obstruction at the proposed scales. The actual Xi source can be periodized on a strip of width `asymp 1/log T` around `sigma_T=1+1/log T`, with relative and logarithmic errors `exp(-Theta((log T)^4))` up to polynomial factors, while the prime leakage is `exp(-Theta((log T)^2))` up to polynomial factors.

The remaining gate is therefore not source approximation. It is the **destination conditioning and transport theorem**: express the reference-divided state in the target normalized norm, prove that the positive-time evolution does not amplify these source errors beyond `o(1)`, and show that a positive-`Lambda` transition leaves nontrivial retained mass. Until that step is supplied, this source theorem is an interface result rather than a de Bruijn--Newman contradiction.
