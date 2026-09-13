# PL-291 — Localized Weil eigenstates bootstrap to every logarithmic Fourier moment

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-REFINEMENT + ROUTE-NARROWING`

**Status:** `ALL-LOG-MOMENTS + RAPID-LOG-TRANSPORT + NO-POWER-LAW-CLAIM`

## Claim

`PL-289` proves that every eigenstate of Suzuki's fixed-domain localized Weil operator lies in the graph domain of the one-dimensional logarithmic Laplacian, hence has a squared-log Fourier moment. `PL-290` then shows that this `log^2` control is the sharp endpoint on the **whole graph ball**. The actual eigen-equation contains more structure than graph-domain membership, and that structure bootstraps indefinitely.

Let `I=(-1,1)`, let `E` denote zero extension to `R`, and put

\[
\ell(\xi)=1+\log(2+|\xi|),
\qquad
X_m(I)=\left\{u\in L^2(I):
\int_{\mathbb R}\ell(\xi)^{2m}|\widehat{Eu}(\xi)|^2\,d\xi<\infty\right\}.
\]

On every compact source-static aperture interval `J`, Suzuki's fixed-domain operator has the form

\[
A_a=T+K_a,
\qquad a\in J,
\]

where the principal operator `T` has whole-line symbol

\[
m(\xi)=\log|\xi|+\gamma,
\]

and `K_a` consists of scalar terms, finitely many compressed prime-power translations, and a compactly supported continuous-kernel term.

Then every `L^2` eigenstate `u` of `A_a` satisfies

\[
\boxed{u\in\bigcap_{m\ge0}X_m(I).}
\]

More quantitatively, for every fixed integer `m>=0`, normalized eigenstates whose eigenvalues stay in a bounded set and whose apertures range in a compact source-static interval obey a uniform bound

\[
\sup_{a,u}\int\ell(\xi)^{2m}|\widehat{Eu}(\xi)|^2\,d\xi<\infty.
\]

Consequently, for every fixed `m>=1`, their compressed-translation autocorrelations satisfy

\[
\boxed{
|\langle S_{h+\delta}u,u\rangle-
\langle S_hu,u\rangle|
=O_m\!\left(\frac1{\log^{2m}(1/|\delta|)}\right)
\qquad(\delta\to0),
}
\]

uniformly for interior lags `h` in a compact set. On a compact source-static aperture interval the lowest localized-Weil eigenvalue therefore satisfies, for every fixed `m`,

\[
\boxed{
|\lambda_1(a)-\lambda_1(b)|
=O_m\!\left(\frac1{\log^{2m}(1/|a-b|)}\right).
}
\]

This strictly separates the actual low spectral family from the sharp graph-ball obstruction in `PL-290`. It does **not** imply any Hölder modulus, positive-order Sobolev regularity, or Feynman--Hellmann derivative: the constants may grow arbitrarily fast with `m`, and membership in every logarithmic scale is much weaker than any fixed positive power of `|xi|`.

## 1. The cutoff lemma for logarithmic Fourier spaces

The key boundary operation is multiplication by an interval or half-line indicator in physical space. For every fixed `m`, this is bounded on `X_m`.

Indeed, the Fourier transform of multiplication by a half-line indicator is, up to harmless constants and phase factors, `I` plus the Hilbert transform in the frequency variable. The classical Hunt--Muckenhoupt--Wheeden theorem gives boundedness of the Hilbert transform on `L^2(w dxi)` whenever `w` is an `A_2` weight.

Here

\[
w_m(\xi)=\ell(\xi)^{2m}
\]

is an `A_2` weight. This can be checked directly from the definition. On an interval whose distance from the origin dominates its length, `ell` is comparable to a constant. On intervals meeting a fixed multiple of the origin, the elementary slowly-varying estimates

\[
\frac1R\int_0^R\ell(x)^{\alpha}\,dx
\asymp \ell(R)^{\alpha}
\]

hold for every fixed real `alpha`; applying this for `alpha=2m` and `alpha=-2m` gives the `A_2` product bound. Thus half-line cutoffs are bounded on `X_m`, and an interval cutoff, being a difference of two half-line cutoffs, is bounded as well.

Translations in the physical variable multiply the Fourier transform by a phase and are isometries on every `X_m`. Hence every operator built from finitely many translations and interval cutoffs preserves all the spaces `X_m`.

This is precisely the structure of Suzuki's compressed prime-power channels.

## 2. The exterior logarithmic-Laplacian term preserves every `X_m`

Write

\[
H=\frac12L_\Delta+\gamma I,
\]

so that `H` has Fourier multiplier `m(xi)=log|xi|+gamma`. `PL-289`, using Chen--Weth's singular-integral formula, proves that for a function supported in `I`, the exterior restriction of `H(Eu)` is

\[
H(Eu)(x)=-\frac12\int_{-1}^{1}\frac{u(y)}{x-y}\,dy,
\qquad x>1,
\]

with the analogous formula on the left.

Outside the support this is simply a cross-boundary piece of the ordinary Hilbert transform in the physical variable. The ordinary Hilbert transform is the Fourier multiplier `-i sign(xi)`, hence is an isometry on every `X_m`; the exterior cutoff is bounded on `X_m` by the preceding lemma. Therefore the boundary operator

\[
G:u\longmapsto 1_{I^c}H(Eu)
\]

satisfies

\[
\boxed{G:X_m(I)\to X_m(\mathbb R)}
\quad\text{boundedly for every fixed }m.
}
\]

This is the higher-log analogue of the `L^2` exterior Carleman estimate used in `PL-289`. The new point is not a stronger Carleman norm; it is that the cross-boundary operator factors through operations that preserve the whole logarithmic scale.

## 3. Suzuki's bounded arithmetic remainder preserves every `X_m`

On a source-static interval, the finite arithmetic part of `K_a` is a sum of compressed translations with lags

\[
h_n(a)=\frac{\log n}{a}
\]

for finitely many active prime powers. By Section 1, each such channel preserves every `X_m`, uniformly when `a` stays in a compact source-static interval.

The remaining non-scalar term has kernel `-a r''(a(x-y))` on `I x I`. Suzuki decomposes `r=r_0+r_1`, with `r_0` smooth and

\[
r_1''(t)=
\frac{e^{-|t|/2}}{1-e^{-2|t|}}-\frac1{2|t|}.
\]

For `t>0`, expansion at the origin gives

\[
r_1''(t)=\frac14-\frac{t}{48}-\frac{t^2}{32}+O(t^3).
\]

Thus the even extension has only a finite cusp at zero and is of bounded variation on every compact interval; away from zero it is smooth. After restricting `x-y` to `[-2,2]`, the convolution kernel is compactly supported and of bounded variation, uniformly for `a` in a compact aperture interval. Its Fourier transform therefore satisfies

\[
|\widehat{k_a}(\xi)|\le \frac{C_J}{1+|\xi|}.
\]

Whole-line convolution by `k_a` maps `L^2` boundedly into `H^1`, hence into every `X_m` for fixed `m`. The final output restriction to `I` is again bounded on `X_m` by Section 1. Consequently

\[
\boxed{K_a:X_m(I)\to X_m(I)}
\]

for every `m`, with operator norm locally uniform in a source-static compact aperture interval.

The scalar part is trivial. Therefore the entire bounded remainder, including the finite von-Mangoldt prime comb, preserves the full logarithmic scale.

## 4. Eigen-equation bootstrap

Let `u` be an eigenstate,

\[
(T+K_a)u=\lambda u.
\]

By `PL-289`, `u in X_1(I)`. Assume inductively that `u in X_m(I)` for some `m>=1`. Since `K_a` preserves `X_m`,

\[
Tu=(\lambda-K_a)u\in X_m(I).
\]

On the whole line, `PL-289` identifies the interior part of `H(Eu)` with `ETu`, while Section 2 controls the exterior part:

\[
H(Eu)=E(Tu)+G(u).
\]

Both terms belong to `X_m(R)`, hence

\[
\int\ell(\xi)^{2m}|m(\xi)|^2
|\widehat{Eu}(\xi)|^2\,d\xi<\infty.
\]

For large `|xi|`, `|m(xi)|` is comparable to `ell(xi)`, so the high-frequency part is exactly the `X_{m+1}` condition. Near frequency zero there is no obstruction: compact support gives `Eu in L^1 cap L^2`, hence `widehat{Eu}` is bounded, while every finite power of `|log|xi||` is locally integrable. Thus

\[
u\in X_{m+1}(I).
\]

Induction proves membership in every `X_m`.

The same proof gives uniform estimates. On a compact source-static aperture interval the cutoff constants are fixed, the active source set is finite, the kernel-BV bounds are uniform, and `K_a` has uniformly bounded `X_m -> X_m` norm for each fixed `m`. If `|lambda|` is uniformly bounded, the induction gives a finite constant `C_m` for each level. No useful growth bound in `m` is asserted.

## 5. Rapid logarithmic transport of actual eigenstates

For zero extension of a normalized state,

\[
F_u(h)=\langle S_hu,u\rangle
=\frac1{2\pi}\int e^{ih\xi}|\widehat{Eu}(\xi)|^2\,d\xi.
\]

If `u in X_m`, then

\[
|F_u(h+\delta)-F_u(h)|
\le C_m(u)
\sup_{\xi}
\frac{|e^{i\delta\xi}-1|}{\ell(\xi)^{2m}}.
\]

With `L=log(1/|delta|)`, split at `|xi|=|delta|^{-1}e^{-sqrt(L)}` as in `PL-289`. The low-frequency part is exponentially small in `sqrt(L)`, while on the complement `ell(xi)>=L-sqrt(L)+O(1)`. Therefore

\[
\sup_{\xi}
\frac{|e^{i\delta\xi}-1|}{\ell(\xi)^{2m}}
=O_m(L^{-2m}).
\]

Thus actual eigenstates beat the sharp `Theta(L^-2)` graph-ball modulus of `PL-290` by **every fixed inverse power of `L`**.

For the lowest eigenvalue, the two min--max inequalities

\[
\lambda_1(b)-\lambda_1(a)
\le(q_b-q_a)(u_a),
\qquad
\lambda_1(a)-\lambda_1(b)
\le(q_a-q_b)(u_b)
\]

apply to normalized ground states. The finite prime comb is controlled by the preceding estimate with `delta_n=(log n)(1/b-1/a)`. Suzuki's scalar and continuous-kernel aperture terms are locally Lipschitz and are therefore asymptotically smaller than every fixed inverse logarithmic power. This yields the stated `O_m(log^-2m)` eigenvalue modulus on compact source-static intervals.

No simplicity is required for this scalar lowest-eigenvalue estimate. Simplicity remains relevant only when one wants a canonically tracked normalized eigenvector branch.

## 6. Adversarial boundary checks

**This does not contradict PL-290.** The phase-locked witnesses proving graph-ball sharpness depend on the aperture increment and have only the graph-level cost `log^2|xi|`. They do not lie in a uniformly bounded subset of all `X_m`. The eigen-equation selects a much smaller subset of the graph domain.

**All logarithmic moments are not Sobolev regularity.** The intersection of the weights `log^{2m}(2+|xi|)` over all fixed `m` is strictly larger than every positive-order Sobolev space. No estimate of the form `int |xi|^{2s}|uhat|^2<infinity` for any `s>0` is obtained.

**No aperture derivative follows.** Differentiating a moving shift introduces a factor `xi`. Arbitrarily high powers of `log|xi|` do not control that multiplier. A Feynman--Hellmann formula still needs positive-order regularity or a separate cancellation identity.

**Constants are the quantitative bottleneck.** The `X_m` cutoff norms, kernel bounds, and induction constants may grow very rapidly with `m`. The theorem gives rapid decay on the logarithmic scale for each fixed `m`, but it does not justify optimizing `m=m(delta)` and does not yet transport the `~10^-17` certified margin through a macroscopic aperture increment.

**The mechanism is not uniquely arithmetic.** The bootstrap uses the fact that the arithmetic remainder is a finite sum of compressed translations on each source-static interval. A matched finite-shift model with the same logarithmic principal operator has the same regularity mechanism. Rational-prime rigidity must therefore enter through the coefficients, source activations, or a later cancellation/positivity theorem, not through the bootstrap alone.

**Source activations remain separate gates.** At `2a=log n`, the active finite comb changes. The result is uniform only on compact intervals avoiding those thresholds. It does not remove the activation bookkeeping needed for global support transport.

## 7. Prior-art and novelty audit

Source 56 (Suzuki) supplies the fixed-domain decomposition into the logarithmic principal operator, finite compressed prime-power translations, and the continuous `r''` kernel. Source 96 (Chen--Weth) supplies the logarithmic-Laplacian singular-integral representation used by `PL-289` and hence the exact exterior formula. The weighted-cutoff input is the classical theorem of R. Hunt, B. Muckenhoupt and R. Wheeden, “Weighted norm inequalities for the conjugate function and Hilbert transform,” *Transactions of the American Mathematical Society* **176** (1973), 227--251.

The regularity literature on the Dirichlet logarithmic Laplacian already proves boundedness, interior continuity and sharp boundary behavior of eigenfunctions; in particular, Feulefack--Jarohs--Weth, *Journal of Fourier Analysis and Applications* **28** (2022), Article 18, gives `L^infinity`, interior continuity and boundary decay results. A targeted search did not locate the specific all-log Fourier bootstrap above, nor its application to Suzuki's moving prime-power channels. Search absence is not treated as proof of novelty.

The durable claim is deliberately line-local: once `PL-289` has identified the exact one-dimensional graph domain, the **specific structured bounded remainder** in the localized Weil eigen-equation preserves every logarithmic Fourier scale, and the exterior boundary operator does too. This converts the one-step squared-log gain into an arbitrary finite logarithmic gain and closes the possibility that `PL-290`'s graph-ball `log^-2` modulus is the true regularity endpoint of the actual eigenstates.

## Consequence for the research line

Generic form regularity and generic graph regularity are now both exhausted as explanations of the low branch. The actual localized-Weil eigenstates are much smaller than either ambient ball: on every source-static compact interval they have uniformly bounded moments of every fixed logarithmic order and hence rapid logarithmic prime-shift transport.

The next falsifiable gate is quantitative. A useful continuation theorem must control the growth of the constants `C_m` strongly enough to optimize the logarithmic hierarchy, prove a genuine positive-order Fourier moment for the actual ground state, derive a source-specific cancellation identity, or certify positivity directly on a nontrivial aperture interval. Merely adding another finite logarithmic moment cannot change the problem.