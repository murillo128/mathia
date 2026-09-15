# AF-360 — Riesz dyadic projective shape is asymptotically endpoint-blind

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `MOVING-PARAMETER-OBSTRUCTION`, `ZERO-SENSITIVE-SOURCE`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

Retain AF-359's logarithmically normalized Riesz family and assume RH. For each distinct positive zeta-zero ordinate `gamma`, with multiplicity `m_gamma`, write

\[
\rho_\gamma=\frac12+i\gamma,
\qquad
M_\delta(\rho)
=
\Gamma(1+\delta)\frac{\Gamma(\rho+1)}{\Gamma(\rho+1+\delta)},
\tag{1}
\]

so that

\[
\widehat E_\delta(\gamma)
=M_\delta(\rho_\gamma)\widehat E_0(\gamma).
\tag{2}
\]

AF-359 showed that the **absolute** size of this multiplier has its endpoint transition when `delta log T` is order one. The present finding separates that radial attenuation from the relative phase/shape information inside a multiplicative frequency band.

For `T>0`, form the finite critical-shell vector

\[
V_{\delta,T}(\gamma)
:=
\sqrt2\,(1+\gamma^2)^{1/4}\widehat E_\delta(\gamma),
\qquad T<\gamma\le2T,
\tag{3}
\]

so that

\[
\|V_{\delta,T}\|_2^2=\mathcal A_\delta(T)
\tag{4}
\]

in the notation of AF-359. Define the scalar

\[
c_{\delta,T}
:=
\Gamma(1+\delta)(iT)^{-\delta}
\tag{5}
\]

with the principal logarithm.

Then for every moving sequence

\[
\delta_j\downarrow0,
\qquad
T_j\to\infty,
\tag{6}
\]

with **no assumption at all on** `delta_j log T_j`, one has

\[
\boxed{
\sup_{T_j<\gamma\le2T_j}
\left|
\frac{M_{\delta_j}(\rho_\gamma)}{c_{\delta_j,T_j}}-1
\right|
\longrightarrow0.
}
\tag{7}
\]

In fact the left side is `O(delta_j)+o(1)` uniformly on the dyadic shell. Consequently

\[
\boxed{
\frac{
\|V_{\delta_j,T_j}-c_{\delta_j,T_j}V_{0,T_j}\|_2
}{
\|V_{\delta_j,T_j}\|_2
}
\longrightarrow0.
}
\tag{8}
\]

Equivalently, the projective classes satisfy

\[
\boxed{
[V_{\delta_j,T_j}]-[V_{0,T_j}]\longrightarrow0
}
\tag{9}
\]

for any projective metric induced by the shell Hilbert norm. In particular, the normalized coherence obeys

\[
\boxed{
\frac{
|\langle V_{\delta_j,T_j},V_{0,T_j}\rangle|
}{
\|V_{\delta_j,T_j}\|_2\|V_{0,T_j}\|_2
}
\longrightarrow1.
}
\tag{10}
\]

Thus **relative phase geometry, normalized cross-frequency shape, and every continuous scale-invariant observable confined to one dyadic zero shell are asymptotically blind to the small-order Riesz endpoint comparison.** This remains true even along frequencies far beyond the absolute transition scale `exp(Theta(1/delta))`: the shell norm can collapse relative to the endpoint while its projective shape still converges to the endpoint shape.

There is a complementary cross-scale law. For `R>=1` define, whenever the two shell energies are nonzero,

\[
\mathcal Q_\delta(T,R)
:=
\frac{
\mathcal A_\delta(RT)/\mathcal A_0(RT)
}{
\mathcal A_\delta(T)/\mathcal A_0(T)
}.
\tag{11}
\]

Let `delta_j -> 0`, `T_j -> infinity`, and `R_j>=1`. If

\[
\delta_j\log R_j\longrightarrow v\in[0,\infty],
\tag{12}
\]

then

\[
\boxed{
\mathcal Q_{\delta_j}(T_j,R_j)
\longrightarrow e^{-2v},
}
\tag{13}
\]

with `e^{-infinity}:=0`. Therefore any relative shell-amplitude comparison whose two scales satisfy

\[
\log R_\delta=o(1/\delta)
\tag{14}
\]

is also asymptotically blind: its Riesz attenuation ratio tends to one. An order-one cross-scale discriminator requires multiplicative scale separation

\[
R_\delta=\exp(\Theta(1/\delta)).
\tag{15}
\]

This closes one specific escape left open by AF-359. **Intra-band phase sensitivity does not bypass the exponential endpoint scale**, because the Riesz multiplier becomes a common scalar on every fixed-ratio shell. Cross-scale information can see the multiplier only when the scales themselves are exponentially separated in `1/delta`, unless one permits an observer with diverging conditioning or introduces source information before the Riesz compression.

## Derivation

### 1. The small-order multiplier is asymptotically scalar on fixed-ratio shells

From the exact Gamma quotient `(1)`,

\[
\log M_\delta(\rho)
=
\log\Gamma(1+\delta)
-
\int_0^\delta\psi(\rho+1+t)\,dt.
\tag{16}
\]

Uniformly for `0<=delta<=1` and `|rho|` large in the vertical sector containing the nontrivial zeros,

\[
\psi(\rho+1+t)
=
\log\rho+O(|\rho|^{-1})
\tag{17}
\]

for `0<=t<=delta`. Hence

\[
M_\delta(\rho)
=
\Gamma(1+\delta)\rho^{-\delta}
\left(1+O\!\left(\frac\delta{|\rho|}\right)\right),
\tag{18}
\]

uniformly in the same range.

For `T<gamma<=2T`, divide `(18)` by `(5)`. Since

\[
\frac{\rho_\gamma}{iT}
=
\frac\gamma T-\frac{i}{2T},
\tag{19}
\]

its modulus remains between `1+o(1)` and `2+o(1)`, while its argument is `O(1/T)`. Therefore

\[
\log\frac{M_\delta(\rho_\gamma)}{c_{\delta,T}}
=
-\delta\log\!\left(\frac{\rho_\gamma}{iT}\right)
+O\!\left(\frac\delta T\right),
\tag{20}
\]

and so

\[
\sup_{T<\gamma\le2T}
\left|
\log\frac{M_\delta(\rho_\gamma)}{c_{\delta,T}}
\right|
\le
\delta\log2+O(\delta/T)+o(\delta).
\tag{21}
\]

Whenever `delta->0` and `T->infinity`, `(21)` proves `(7)`. Crucially, the large common term `delta log T` has disappeared into the scalar `c_{delta,T}`. It controls shell amplitude but not shell shape.

### 2. Scalarization forces projective convergence

Write

\[
M_\delta(\rho_\gamma)
=c_{\delta,T}(1+r_{\delta,T}(\gamma)),
\qquad
\varepsilon_{\delta,T}
:=
\sup_{T<\gamma\le2T}|r_{\delta,T}(\gamma)|.
\tag{22}
\]

By `(7)`, `epsilon_{delta,T}->0` along every path `(6)`. Equation `(2)` then gives componentwise

\[
V_{\delta,T}
=c_{\delta,T}(I+R_{\delta,T})V_{0,T},
\qquad
\|R_{\delta,T}\|_{\ell^2\to\ell^2}
\le\varepsilon_{\delta,T}.
\tag{23}
\]

Hence

\[
\|V_{\delta,T}-c_{\delta,T}V_{0,T}\|_2
\le
|c_{\delta,T}|\varepsilon_{\delta,T}\|V_{0,T}\|_2,
\tag{24}
\]

while

\[
\|V_{\delta,T}\|_2
\ge
|c_{\delta,T}|(1-\varepsilon_{\delta,T})\|V_{0,T}\|_2.
\tag{25}
\]

For all sufficiently large shells the denominator is nonzero by Riemann--von Mangoldt. Dividing `(24)` by `(25)` yields

\[
\frac{
\|V_{\delta,T}-c_{\delta,T}V_{0,T}\|_2
}{
\|V_{\delta,T}\|_2
}
\le
\frac{\varepsilon_{\delta,T}}{1-\varepsilon_{\delta,T}},
\tag{26}
\]

which proves `(8)` and therefore `(9)`--`(10)`.

The conclusion is stronger than AF-359's finite-`u` scalar limit. Suppose, for example, that `delta log T -> infinity`. Then `|c_{delta,T}| -> 0`, so AF-359 says the smoothed shell loses essentially all endpoint critical energy. Nevertheless `(26)` still tends to zero: after quotienting out the vanishing common amplitude, the remaining relative complex geometry is asymptotically unchanged.

This distinction is exactly the fidelity issue. The Riesz transform destroys a radial resource on the shell before it destroys the shell's projective phase/shape resource. But the surviving projective resource cannot distinguish the smoothed profile from the endpoint because both occupy the same asymptotic projective class.

### 3. Relative attenuation between two shells depends only on logarithmic scale separation

Equation `(23)` also gives

\[
\frac{\mathcal A_\delta(T)}{\mathcal A_0(T)}
=
|c_{\delta,T}|^2(1+O(\varepsilon_{\delta,T}))
=
\Gamma(1+\delta)^2T^{-2\delta}(1+o(1))
\tag{27}
\]

uniformly along every path `delta->0`, `T->infinity`. Apply `(27)` once at `T` and once at `RT`. The Gamma factors cancel, giving

\[
\mathcal Q_\delta(T,R)
=
R^{-2\delta}(1+o(1)).
\tag{28}
\]

This remains valid when `R=R_delta` moves, because each individual dyadic shell still has fixed internal ratio `2`; no uniformity over the entire interval `[T,2RT]` is being asserted. If `delta log R -> v`, `(28)` gives `(13)`.

Thus there are two distinct bandwidths. A dyadic shell has bounded **internal** logarithmic width, so its normalized shape always scalarizes as `delta->0`. To compare the amount of attenuation at two shells, their **separation** must have logarithmic width `Theta(1/delta)` before an order-one relative effect survives.

## Arithmetic-fidelity interpretation

AF-359 deliberately left phase-sensitive and cross-scale observables as possible ways around its magnitude-only shell obstruction. The exact multiplier shows that these two possibilities behave differently.

Within one dyadic shell, relative phase and normalized cross-frequency structure cannot help. Every zero coefficient is multiplied by the same scalar up to `o(1)`. A bispectral, correlation, marked, or other phase-sensitive statistic that is continuous after quotienting common complex scale therefore sees the same asymptotic shell shape at `delta>0` as at the endpoint. An unnormalized homogeneous statistic can still see the common attenuation, but then its first order-one transition is the same radial transition already quantified by AF-359 rather than a new phase channel.

Cross-scale information is not completely killed, but `(13)` prices it. Comparing polynomially or otherwise subexponentially separated frequencies cannot yield an order-one attenuation discriminator. The scale ratio itself must be `exp(Theta(1/delta))`, or the observable must amplify an `o(1)` difference with a condition number that diverges correspondingly.

The remaining live escape is therefore narrower than in AF-359. A successful route that avoids exponentially separated zero scales must use information **not representable as a well-conditioned continuous observable of the post-Riesz dyadic coefficient shapes and their subexponentially separated amplitudes**. Natural candidates are source-native signed short-interval structure, maximal/tail information, cancellation coupled before smoothing, or another nonlinear operation applied before the Riesz multiplier has scalarized the available band data.

## Boundaries and falsification

- The result assumes RH only to retain AF-358/AF-359's Fourier-shell interpretation of the normalized zeta-zero coefficients. The Gamma-ratio scalarization itself is an analytic statement about the multiplier.
- `Projective` means quotient by one common nonzero complex scalar on a shell. Absolute amplitude is intentionally removed; AF-359 already shows that amplitude carries the `delta log T` transition.
- The no-go statement covers continuous, well-conditioned observables of relative complex shell geometry. An observer whose Lipschitz/condition number diverges as `delta->0` may amplify the vanishing residual in `(7)`; this finding does not call such an unstable amplification faithful.
- The shell must have bounded multiplicative width. More generally the same proof works for `[T,R_delta T]` whenever `delta log R_delta->0`. It does not say a single exponentially wide band is projectively scalar.
- Equation `(13)` concerns relative **amplitude attenuation** between separate dyadic shells. It does not rule out a source-side mechanism that couples arithmetic information across scales before the Riesz compression.
- No simplicity, pair-correlation, zero-spacing, or linear-independence conjecture is used. Multiplicity remains inside `V_{delta,T}` and cancels from the diagonal-multiplier comparison.
- Nothing here implies that every RH proof needs exponentially high zeros. The obstruction belongs to this Riesz channel and to observers that act after the multiplier in the stated metric.

A direct falsification would be a sequence `delta_j->0`, `T_j->infinity`, and ordinates `gamma_j,gamma'_j in (T_j,2T_j]` for which the relative multipliers fail to satisfy

\[
\frac{M_{\delta_j}(\rho_{\gamma_j})}
{M_{\delta_j}(\rho_{\gamma'_j})}
\longrightarrow1.
\tag{29}
\]

The uniform Gamma-ratio estimate `(20)` excludes such a sequence. A scope falsification would be an explicitly defined post-Riesz phase observable that is both uniformly well-conditioned in the shell projective metric and nevertheless has an order-one endpoint separation; `(26)` excludes that possibility by continuity.

## Source / prior-art audit

The analytic inputs are classical and already underwrite AF-359. G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* **41** (1916), 119--196, DOI `10.1007/BF02422942`, supplies the Riesz-mean explicit-formula multiplier. NIST DLMF §5.11, especially the Gamma-ratio asymptotics in Eqs. 5.11.12--5.11.13 and the corresponding `psi` expansion, supplies the uniform high-frequency reduction used in `(16)`--`(21)`. Riemann--von Mangoldt zero counting is classical; see E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford (1986), Chapter 9.

A targeted search for small-order Riesz means, Gamma-ratio regular variation, dyadic zeta-zero shell multipliers, and projective/phase-sensitive Riesz observables did not locate this exact shell-projective formulation or the cross-scale law `(13)`. That search result is not evidence of novelty. The durable claim here is intentionally narrower: once the classical Riesz multiplier is viewed through Arithmetic Fidelity's separation of radial and projective resources, its small-order action is asymptotically scalar on every fixed-ratio high-frequency shell, and the surviving relative shape therefore cannot repair endpoint discrimination.