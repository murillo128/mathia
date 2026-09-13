# PL-292 — Quantified all-log bootstrap gives explicit subpower transport, while cutoff growth blocks a generic Hölder upgrade

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-REFINEMENT + METHOD-BARRIER`

**Status:** `QUANTIFIED-ALL-LOG-CONSTANTS + OPTIMIZED-SUBPOWER-TRANSPORT + FACTORIAL-CUTOFF-BARRIER`

## Claim

`PL-291` proves that localized-Weil eigenstates lie in every fixed logarithmic Fourier space

\[
X_m(I)=\left\{u:\int_{\mathbb R}\ell(\xi)^{2m}|\widehat{Eu}(\xi)|^2\,d\xi<\infty\right\},
\qquad \ell(\xi)=1+\log(2+|\xi|),
\]

but deliberately leaves the growth of the constants in `m` uncontrolled. That growth can be bounded explicitly from the same proof.

On every compact source-static aperture interval `J`, for normalized eigenstates of Suzuki's fixed-domain localized Weil operator whose eigenvalues stay in a bounded set, there is a constant `C_J>1` such that

\[
\boxed{
\|Eu\|_{X_m}
\le \exp\!\bigl(C_J m^2\log(m+2)\bigr)
\qquad(m\ge1).
}
\]

Consequently their compressed-translation autocorrelations obey, uniformly for interior lags `h`,

\[
\boxed{
|\langle S_{h+\delta}u,u\rangle-\langle S_hu,u\rangle|
\le
C_J\exp\!\left[-c_J
\frac{(\log\log(1/|\delta|))^2}
{\log\log\log(1/|\delta|)}\right]
}
\]

for all sufficiently small `|delta|`, with the iterated logarithms understood only in that asymptotic range. The same modulus holds for the lowest localized-Weil eigenvalue on `J` by the two min--max inequalities used in `PL-291`.

This is strictly stronger than every fixed inverse power of `log(1/|delta|)` proved separately in `PL-291`, because

\[
\exp\!\left[-c\frac{Q^2}{\log Q}\right]=o(e^{-NQ})
\qquad(Q\to\infty)
\]

for every fixed `N`. It is still much weaker than every Hölder modulus `|delta|^alpha`, since `Q^2/log Q=o(log(1/|delta|))` when `Q=log log(1/|delta|)`.

There is also a genuine obstruction inside this proof architecture: the physical half-line cutoff on `X_m` has operator norm at least

\[
\boxed{
\|1_{(0,\infty)}\|_{X_m\to X_m}\ge (c m)^m
}
\]

for all large `m`. Thus the unrestricted cutoff step itself has superexponential-in-`m` cost. The generic `PL-291` bootstrap cannot be upgraded to positive-order Sobolev regularity merely by hoping that its cutoff constants are uniformly exponential in `m`. Any Hölder/Feynman--Hellmann improvement must exploit cancellation or state structure that avoids the worst-case cutoff mechanism.

## 1. Quantitative `A_2` growth of the logarithmic weights

Put

\[
w_m(\xi)=\ell(\xi)^{2m}.
\]

`PL-291` uses only that `w_m in A_2` for each fixed `m`. The dependence on `m` can be made explicit:

\[
\boxed{
(c m)^{2m}
\le [w_m]_{A_2}
\le (C(m+1))^{2m}.
}
\]

For the upper bound it is enough, up to an absolute factor, to consider intervals `[0,R]`. The weight is increasing, so

\[
\frac1R\int_0^R w_m\le \ell(R)^{2m}.
\]

For `R` large, split the reciprocal average at `sqrt R`. On `[sqrt R,R]`, `ell(x)>=c ell(R)`, while `[0,sqrt R]` occupies only the fraction `R^{-1/2}`. Hence

\[
\frac1R\int_0^R w_m^{-1}
\le
R^{-1/2}\ell(0)^{-2m}+c^{-2m}\ell(R)^{-2m}.
\]

Multiplication by the first average leaves

\[
C^{2m}+C^{2m}(1+\log R)^{2m}R^{-1/2}.
\]

Writing `t=log R`, the second term is maximized at `t=O(m)` and is at most `(C(m+1))^{2m}`. Intervals far from the origin see only a bounded ratio of `ell` across the interval; intervals close to or crossing the origin compare with `[0,R]` after an absolute enlargement. This gives the stated upper bound.

For the lower bound take `R=e^{4m}`. The upper half of `[0,R]` contributes order `m^{2m}` to the positive average, while the fixed subinterval `[0,1]` contributes order `e^{-4m}` to the reciprocal average. Their product is at least `(c m)^{2m}`.

Petermichl's sharp weighted Hilbert-transform theorem gives

\[
\|\mathcal H\|_{L^2(w_m)\to L^2(w_m)}
\le C[w_m]_{A_2},
\]

so the half-line Fourier projection, and hence every interval cutoff in physical space, has

\[
\boxed{
B_m:=\sup_J\|1_J\|_{X_m\to X_m}
\le (C(m+1))^{2m}.
}
\]

The literature input here is standard weighted harmonic analysis: S. Petermichl, “The sharp bound for the Hilbert transform on weighted Lebesgue spaces in terms of the classical `A_p` characteristic,” *American Journal of Mathematics* **129** (2007), 1355–1375, DOI `10.1353/ajm.2007.0036`. The special `m`-dependence above is a direct calculation for the particular logarithmic weights used by `PL-291`.

## 2. The cutoff cost is necessarily superexponential in logarithmic order

The preceding upper estimate is not merely an artifact of a very coarse weighted theorem. There is a direct lower bound showing that cutoff norms cannot be bounded by `A^m` with fixed `A`.

Choose a Schwartz function `phi` whose Fourier transform is supported in a fixed compact interval and with `phi(0) != 0`. Then

\[
\|\phi\|_{X_m}\le C^m\|\phi\|_2.
\]

Let `g=1_(0,infinity) phi`. Integration by parts gives

\[
\widehat g(\xi)=\frac{\phi(0)}{i\xi}+O(|\xi|^{-2}),
\qquad |\xi|\to\infty.
\]

Therefore, for a fixed sufficiently large `xi_0`,

\[
\|g\|_{X_m}^2
\ge
c\int_{\xi_0}^{\infty}
\frac{(\log\xi)^{2m}}{\xi^2}\,d\xi.
\]

With `t=log xi`, this is

\[
c\int_{\log\xi_0}^{\infty} t^{2m}e^{-t}\,dt.
\]

Restricting just to a unit interval around `t=2m` gives

\[
\|g\|_{X_m}\ge (c m)^m.
\]

After division by the exponentially bounded input norm,

\[
\boxed{B_m\ge(c m)^m.}
\]

The mechanism is transparent: a physical cutoff creates a boundary jump, whose `1/xi` Fourier tail carries a `2m`-th logarithmic moment of factorial scale. This lower bound is only a **method barrier**. It does not prove that the actual Weil ground state saturates the cutoff norm, nor that the ground state lacks positive Sobolev regularity.

## 3. Quantitative version of the `PL-291` eigen-equation bootstrap

On a compact source-static interval, write as before

\[
A_a=T+K_a.
\]

The three operations in the proof of `PL-291` now have explicit order dependence.

First, each compressed prime-power translation is a translation followed by an interval cutoff, so its `X_m` norm is at most `B_m`. Second, the exterior cross-boundary logarithmic-Laplacian term is an ordinary Hilbert transform in the physical variable followed by exterior cutoffs; the Hilbert transform is an `X_m` isometry, so this term also costs at most a constant times `B_m`.

Third, Suzuki's continuous-kernel remainder has whole-line Fourier multiplier bounded by `C_J/(1+|xi|)`. Hence before the final output cutoff,

\[
\|R_af\|_{X_m}
\le
C_J\sup_\xi\frac{\ell(\xi)^m}{1+|\xi|}\,\|f\|_2
\le (C_J(m+1))^m\|f\|_2,
\]

because the maximum of a logarithmic power divided by a linear power occurs at logarithmic frequency `O(m)`. The final restriction to `I` contributes one more factor `B_m`.

Thus, uniformly for `a in J`, both the bounded remainder and the exterior operator satisfy a coarse but explicit estimate

\[
\|K_a\|_{X_m\to X_m}+\|G\|_{X_m\to X_m}
\le (C_J(m+1))^{C m}
\]

with an absolute numerical `C` independent of `m`.

Let

\[
M_m(u)=\|Eu\|_{X_m}.
\]

For an eigenstate `(T+K_a)u=lambda u`, the whole-line reconstruction in `PL-291` gives

\[
H(Eu)=E(Tu)+G(u),
\qquad Tu=(\lambda-K_a)u.
\]

Since `ell(xi)<=C(1+|log|xi|+gamma|)`, one logarithmic step obeys

\[
M_{m+1}(u)
\le (C_J(m+1))^{C m}M_m(u)
\]

for normalized eigenstates with `|lambda|` uniformly bounded. Iteration yields

\[
\log M_m(u)
\le C_J\sum_{j\le m}j\log(j+2)
\le C'_Jm^2\log(m+2),
\]

which is the claimed quantitative all-log bound.

## 4. Optimizing the logarithmic hierarchy

The fixed-`m` estimate of `PL-291` can now be optimized because the `m`-dependence is explicit. Let

\[
L=\log(1/|\delta|).
\]

For every `m`, split frequencies at `|xi|=|delta|^{-1/2}`. Below the split,

\[
|e^{i\delta\xi}-1|\le e^{-L/2},
\]

while above it `ell(xi)>=cL`. Therefore

\[
\sup_\xi
\frac{|e^{i\delta\xi}-1|}{\ell(\xi)^{2m}}
\le e^{-L/2}+2(C/L)^{2m}.
\]

Together with the moment bound this gives

\[
|F_u(h+\delta)-F_u(h)|
\le
\exp\!\bigl(C_0m^2\log(m+2)\bigr)
\left(e^{-L/2}+2(C/L)^{2m}\right).
\]

Put `Q=log L` and choose

\[
m=\left\lfloor\eta\frac{Q}{\log Q}\right\rfloor
\]

with fixed `eta>0` sufficiently small relative to `C_0`. Then

\[
C_0m^2\log m-2m\log L
\le
-c\frac{Q^2}{\log Q}
\]

for all sufficiently large `Q`; the `e^{-L/2}` term is much smaller. Hence

\[
\boxed{
|F_u(h+\delta)-F_u(h)|
\le C\exp\!\left[-c
\frac{(\log\log(1/|\delta|))^2}
{\log\log\log(1/|\delta|)}\right].
}
\]

The finite active prime-power lags satisfy `delta_n=(log n)(1/b-1/a)`, so replacing `delta` by `|a-b|` changes the nested logarithms only by asymptotically harmless constants. The scalar and continuous-kernel aperture terms are locally Lipschitz and therefore smaller. The two min--max inequalities then transfer the same modulus to `lambda_1(a)` on `J`.

## 5. Adversarial checks

**No hidden Hölder conclusion.** The optimized exponent is `o(log(1/|delta|))`, so this estimate is subpower in `|delta|`. It does not justify differentiating the moving shifts and does not supply Feynman--Hellmann.

**The cutoff lower bound is not an eigenstate lower bound.** The witness used in Section 2 is an arbitrary band-limited function cut at a half-line. It proves that the generic cutoff operator in the `PL-291` induction is expensive. A zeta-specific eigenstate may avoid this worst case through endpoint cancellation or another structural identity.

**The `A_2` estimate is used only for an upper bound.** The lower bound on `B_m` is proved directly from the boundary-generated Fourier tail; no converse weighted-Hilbert theorem is assumed.

**Recent logarithmic-Laplacian regularity does not close the global gap.** Feulefack--Jarohs--Weth (2022) prove boundedness and continuity properties for Dirichlet logarithmic-Laplacian eigenfunctions, and Biswas--Roy--Sen--Sharma, arXiv:2608.07315 (August 2026), prove interior Schauder/Hölder estimates for logarithmic-Laplacian equations. These results concern local/interior regularity or the pure Dirichlet operator. The aperture derivative here depends on the zero extension and on compressed translations whose moving cut boundaries are exactly the operations measured by `B_m`. No inspected theorem gives a uniform positive Sobolev moment for the Suzuki eigenbranch that would make the moving prime shifts differentiable.

**Matched controls still pass.** The quantitative bootstrap uses only a logarithmic principal multiplier, finitely many compressed shifts and a smoothing remainder. A matched nonarithmetic finite-shift model receives the same subpower estimate. This finding improves the continuation machinery but is not itself rational-prime rigidity or an RH mechanism.

## 6. Prior-art and novelty audit

Weighted Hilbert-transform theory and function spaces of logarithmic smoothness are established subjects. Petermichl supplies the sharp linear `A_2` dependence used above. Dominguez--Tikhonov, *Function Spaces of Logarithmic Smoothness: Embeddings and Characterizations* (Memoirs AMS **282**, 2023; arXiv:1811.06399), provides broad prior-art context for logarithmic Fourier scales and moduli of smoothness. The logarithmic-Laplacian regularity literature cited in `PL-291` and above supplies further controls.

The literature audit was run by structure (`logarithmic Fourier weight` + cutoff/Hilbert `A_2`, logarithmic smoothness + translation modulus, logarithmic Laplacian + eigenfunction regularity), not by the wording of this finding. No inspected source gives the specific combination used here: the `m`-uniform cutoff growth for the `PL-291` spaces, its propagation through Suzuki's localized Weil remainder, and optimization into the displayed source-static eigenvalue modulus. This is therefore recorded as a **line-local exact quantitative refinement**, not as a broad novelty claim in weighted harmonic analysis.

## Consequence for the research line

The immediate quantitative gate left by `PL-291` is partially resolved. The all-log hierarchy can be optimized and gives a single explicit modulus faster than every inverse logarithmic power. At the same time, the boundary cutoff intrinsic to compressed prime shifts has factorial-scale logarithmic moments, so the same black-box bootstrap is structurally ill-suited to produce a power law.

The next useful step must therefore be one of two qualitatively stronger mechanisms: prove that the actual low eigenstate has endpoint/source cancellation that bypasses the generic cutoff cost, or derive a positive-order Fourier/Sobolev estimate by a different equation-level argument. Merely sharpening the `A_2` bookkeeping or adding further fixed logarithmic moments cannot cross that boundary.