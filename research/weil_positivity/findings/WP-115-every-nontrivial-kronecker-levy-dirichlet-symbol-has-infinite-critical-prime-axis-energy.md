# WP-115 — Every nontrivial Kronecker Lévy–Dirichlet symbol has infinite critical prime-axis energy

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATION-INDEPENDENT + CLASSICAL-LEVY-KHINTCHINE + MATCHED-CONTROL` for the Markov/Dirichlet part of the zero-frequency-degenerate spectral escape left open by `WP-109` and `WP-114`.

`WP-109` showed that an exact critical positive Prime-Lattice completion can have finite raw Kronecker spectral cost only if its nonnegative multiplier suppresses the compulsory one-prime frequencies more strongly than `t^{-2}`. `WP-114` then proved that every exact critical completion has divergent mixed Fourier mass in every fixed neighborhood of zero Kronecker frequency, ruling out multipliers with `w(0)>0`. Together those results left a narrow-looking possibility: an intrinsic positive multiplier might vanish at zero, suppress high frequencies strongly enough, and thereby avoid both obstructions.

For the canonical **Markov/Dirichlet** version of that escape, this finding closes the gap completely.

Let `X` be the Prime-Lattice Kronecker generator, whose Fourier frequency on an exponent character `alpha` is

\[
E(\alpha)=\sum_p \alpha_p\log p.
\tag{1}
\]

Let `psi:R-> [0,infinity)` be a continuous symmetric conditionally negative-definite function with `psi(0)=0`. Equivalently, `exp(-s psi)` is the Fourier transform of a symmetric convolution semigroup for every `s>0`, so `psi(X)` is the standard one-dimensional Lévy/Markov functional calculus of the Kronecker flow. For a finite prime set `P`, define the positive cylindrical spectral form

\[
\mathcal D_{\psi,P}(\eta_P)
=
\sum_{\alpha\in\mathbb Z^P}
\psi(E(\alpha))
|\widehat\eta_P(\alpha)|^2.
\tag{2}
\]

Suppose `eta_P` is any normalized positive completion carrying the exact critical first harmonics already forced in `WP-096`--`WP-114`, namely

\[
\left|\widehat\eta_P(e_p)\right|
=
\frac{\log p}{C\sqrt p}
\qquad(p\in P)
\tag{3}
\]

for one fixed finite normalization `C>0`. No assumption is made about mixed-prime correlations.

Then every **nonzero** symmetric Lévy exponent has infinite critical cylindrical cost:

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal D_{\psi,P}(\eta_P)=+\infty
\qquad\text{for every nontrivial symmetric CND }\psi.
}
\tag{4}
\]

Thus zero-frequency degeneracy is not enough if the positive spectral multiplier is required to come from an intrinsic conservative Markov/Dirichlet theorem. The only finite critical Kronecker spectral multipliers surviving the endpoint tests must leave this scalar Lévy/Dirichlet cone, or the architecture must change before positivity is taken.

## 1. Exact critical rays already give the decisive lower bound

Positivity of every term in (2) gives, for each finite `P`,

\[
\mathcal D_{\psi,P}(\eta_P)
\ge
\frac1{C^2}
\sum_{p\in P}
\psi(\log p)\frac{(\log p)^2}{p}.
\tag{5}
\]

This lower bound uses only the mandatory one-prime harmonics (3). Therefore arbitrary mixed-prime correlations, including the correlated completions of `WP-101`, cannot lower it.

The question is consequently reduced to a one-dimensional arithmetic statement:

\[
\boxed{
\sum_p
\psi(\log p)\frac{(\log p)^2}{p}
=+\infty
\quad\text{for every nontrivial symmetric continuous CND }\psi.
}
\tag{6}
\]

The point is not merely that familiar derivative symbols grow too fast. A bounded compound-Poisson symbol can have infinitely many exact zeros and can oscillate indefinitely. Equation (6) still holds.

## 2. Lévy–Khintchine reduces every Markov symbol to Brownian and cosine pieces

For a symmetric continuous conditionally negative-definite function on `R` with `psi(0)=0`, the Lévy–Khintchine representation has the form

\[
\boxed{
\psi(t)
=
a t^2
+
\int_{\mathbb R\setminus\{0\}}
\bigl(1-\cos(tx)\bigr)\,\nu(dx),
}
\tag{7}
\]

where `a>=0` and `nu` is a symmetric Lévy measure satisfying

\[
\int_{\mathbb R}(1\wedge x^2)\,\nu(dx)<\infty.
\tag{8}
\]

Harmless convention-dependent constants can be absorbed into `a` and `nu`. The symbol is nontrivial exactly when `a>0` or `nu` is nonzero.

If `a>0`, the Brownian part alone gives

\[
\sum_p
\psi(\log p)\frac{(\log p)^2}{p}
\ge
 a\sum_p\frac{(\log p)^4}{p}
=+\infty.
\tag{9}
\]

So only the pure-jump case needs work.

## 3. Every nonzero Lévy jump contributes infinite weighted prime energy

Fix `x!=0` and define

\[
A_x(Y)
=
\sum_{p\le Y}
\frac{(\log p)^2}{p}
\bigl(1-\cos(x\log p)\bigr).
\tag{10}
\]

The prime number theorem gives the exact leading scale. Writing

\[
\vartheta(t)=\sum_{p\le t}\log p=t+o(t)
\tag{11}
\]

and applying partial summation,

\[
A_x(Y)
=
\int_2^Y
\frac{\log t}{t}
\bigl(1-\cos(x\log t)\bigr)\,dt
+o\bigl((\log Y)^2\bigr).
\tag{12}
\]

With `u=log t`, the main integral is

\[
\int_{\log2}^{\log Y}
 u\bigl(1-\cos(xu)\bigr)\,du.
\tag{13}
\]

For fixed `x!=0`,

\[
\int u\cos(xu)\,du
=
\frac{u\sin(xu)}x+
\frac{\cos(xu)}{x^2},
\tag{14}
\]

so

\[
\boxed{
A_x(Y)
=
\frac12(\log Y)^2
+O_x(\log Y)
+o\bigl((\log Y)^2\bigr).
}
\tag{15}
\]

In particular,

\[
\boxed{
\sum_p
\frac{(\log p)^2}{p}
\bigl(1-\cos(x\log p)\bigr)
=+\infty
\qquad(x\ne0).
}
\tag{16}
\]

This is stronger than a generic lower bound on `psi(log p)`: each individual nonzero jump scale is already sampled with divergent average mass by the logarithms of the primes. Periodic zeros of `1-cos(x log p)` therefore do not rescue the energy.

## 4. Tonelli closes the entire symmetric Lévy/Dirichlet cone

Insert (7) into the prime-axis series. All terms are nonnegative, so Tonelli's theorem gives

\[
\begin{aligned}
&\sum_p
\frac{(\log p)^2}{p}\,\psi(\log p)
\\
&=a\sum_p\frac{(\log p)^4}{p}
+
\int_{\mathbb R\setminus\{0\}}
\left[
\sum_p
\frac{(\log p)^2}{p}
\bigl(1-\cos(x\log p)\bigr)
\right]\nu(dx).
\end{aligned}
\tag{17}
\]

The first term is infinite if `a>0`. By (16), the bracketed quantity is `+infinity` for every `x!=0`; therefore the second term is infinite whenever `nu` is nonzero. Hence (6), and then (4), follow.

No mixed Fourier coefficient of the completion entered the argument. No zeta zero, functional equation, Weil positivity assumption, or regularized subtraction entered either.

## 5. The off-critical matched control passes for every Lévy exponent

The divergence is genuinely tied to the critical `p^{-1/2}` amplitudes, not to a generic pathology of Lévy functional calculus.

At exponent `sigma>1/2`, the same exact first-harmonic normalization becomes

\[
\left|\widehat\eta_{\sigma}(e_p)\right|
=
\frac{\log p}{C p^\sigma}.
\tag{18}
\]

Every symmetric Lévy exponent has at most quadratic growth. Indeed, from (7)--(8) and

\[
1-\cos(tx)\le \min\{2,t^2x^2/2\},
\tag{19}
\]

there is a constant `K_psi` such that

\[
\psi(t)\le K_\psi(1+t^2).
\tag{20}
\]

Therefore the compulsory off-critical axis contribution is bounded by

\[
\frac{K_\psi}{C^2}
\sum_p
\frac{(\log p)^2+(\log p)^4}{p^{2\sigma}}
<\infty
\qquad(\sigma>1/2).
\tag{21}
\]

Thus the **same full Markov symbol class** that is impossible at the Weil exponent passes the mandatory-axis summability test immediately above it. This is the appropriate matched control for the obstruction.

The statement is only a necessary-axis comparison: an off-critical completion may still have additional mixed-mode cost. That does not weaken the critical no-go, which already follows from (5).

## 6. A positive band-pass falsifier shows exactly what remains open

The theorem does not say that every intrinsic nonnegative spectral multiplier diverges. For example, for any `m>2`, consider

\[
w_m(t)=\frac{t^2}{(1+t^2)^m}.
\tag{22}
\]

This multiplier is canonical at the level of ordinary Hilbert functional calculus:

\[
\mathcal Q_m(f)
=
\langle f,
X^*X(1+X^*X)^{-m}f\rangle
\ge0.
\tag{23}
\]

It vanishes quadratically at zero, so the `w(0)>0` hypothesis of `WP-114` does not apply. At the prime axes,

\[
w_m(\log p)\frac{(\log p)^2}{p}
\asymp
\frac{(\log p)^{4-2m}}p,
\tag{24}
\]

and the prime sum converges exactly when `m>2`. Hence this family also passes the high-frequency necessary test of `WP-109`.

But (6) immediately implies that `w_m` cannot be a nontrivial symmetric conditionally negative-definite symbol. Its positivity is **operator positivity only**, not the positivity of a conservative Markov/Dirichlet generator.

This is an aggressive falsifier for the scope of the present result. The endpoint obstructions do not eliminate all positive band-pass functional calculi; they eliminate the geometrically stronger claim that such a surviving multiplier is forced by a scalar Lévy/Dirichlet energy theorem.

## 7. This is distinct from WP-009 and WP-039

The word `Markov` occurs in earlier findings, but the mathematical placements are different.

`WP-009` takes the **prime-power Weil coefficients themselves** as proposed physical jump rates on the real test-function line. It proves that their critical tail is not a Lévy measure and that the resulting passive jump energy differs from the finite Weil form by a divergent positive self-energy.

`WP-039` asks whether the **Fourier symbol itself** of a scalar translation-invariant Markov generator can have Mangoldt support: positive on one-prime directions and zero on mixed-prime directions. It rules that out because the zero set of a conditionally negative-definite symbol is a subgroup.

The present construction asks neither of those questions. The arithmetic data are already encoded in a positive prime-torus completion through its exact Fourier amplitudes (3). The Markov symbol is then an independent intrinsic spectral geometry applied to those data. It may be positive on mixed frequencies, may have no Mangoldt support at all, and may even be bounded and highly oscillatory. The obstruction is instead that **every nontrivial one-dimensional Lévy exponent accumulates infinite energy on the compulsory critical prime axes**.

So the three negatives close genuinely different direct routes:

- `WP-009`: Mangoldt weights cannot themselves be passive critical jump intensities;
- `WP-039`: Mangoldt support cannot itself be a scalar translation-invariant Markov Fourier symbol;
- `WP-115`: an independent scalar Kronecker Lévy/Markov symbol cannot give finite energy to any exact critical positive completion carrying the Mangoldt first harmonics.

## 8. Relation to WP-109 and WP-114

`WP-109` gave the exact general axis condition

\[
\sum_p
w(\log p)\frac{(\log p)^2}{p}<\infty.
\tag{25}
\]

It ruled out regular multipliers with `w(t)\gtrsim t^{-2}` but deliberately left faster high-frequency decay open. Equation (6) now shows that **no nontrivial CND symbol can exploit that escape**, even when it has arbitrarily many pointwise zeros or is bounded.

`WP-114` is complementary. It uses covariance positivity to force divergent mixed-prime Fourier mass arbitrarily close to zero, killing every multiplier continuous at zero with `w(0)>0`. A conservative Dirichlet symbol necessarily has `psi(0)=0`, so it lies exactly outside that hypothesis. `WP-115` closes this specific zero-frequency-degenerate Markov branch by using the mandatory high-frequency axes instead of mixed near-resonances.

Together they leave a sharper spectral frontier:

\[
\boxed{
\text{nondegenerate at zero}
\Rightarrow \text{WP-114 divergence},
}
\tag{26}
\]

while

\[
\boxed{
\text{zero at zero + scalar Kronecker Markov/Dirichlet}
\Rightarrow \text{WP-115 divergence}.
}
\tag{27}
\]

A surviving scalar spectral form must therefore be both zero-frequency-degenerate **and non-Markov**, with sufficiently strong high-frequency suppression, unless some earlier architectural operation changes the state space or readout.

## 9. Prior art and novelty audit

The analytic ingredients are classical and are not claimed as new.

- Lévy–Khintchine representation and the correspondence between continuous negative-definite functions and convolution/Markov semigroups are standard; the durable repository anchor is René L. Schilling, *An Introduction to Lévy and Feller Processes* (2017), already recorded in `SOURCES.md` for `WP-009`.
- The prime-number-theorem input `theta(x)~x` and the partial-summation step are classical analytic number theory.
- Conditionally negative-definite Fourier symbols as the natural class for translation-invariant Markov/Dirichlet semigroups were already audited in `WP-039`.

A bounded literature search for combinations of conditionally negative-definite functions, Lévy–Khintchine exponents, logarithms of primes, and weighted prime sums located the standard CND/Lévy framework but no external theorem matching the arithmetic statement (6). That absence is **not** used as a historical novelty claim.

The retained Mathia-specific content is the synthesis: the exact critical first harmonics already forced by the positive Prime-Lattice completion, when tested against the full classical scalar Kronecker Lévy/Dirichlet cone, make every nontrivial Markov spectral energy infinite. This narrows a live escape left explicitly open by `WP-109` and `WP-114` without assuming RH or importing the Weil functional as the positive form.

## 10. Aggressive falsification, boundaries, and surviving routes

The proof survives the main attempts to evade it within its stated architecture.

**Correlations do not help.** Equation (5) discards all mixed modes and therefore applies to independent, finite-block-correlated, and arbitrary positive completions with the same exact first harmonics.

**Periodic zeros do not help.** A compound-Poisson exponent such as `1-cos(tx)` can vanish on an infinite arithmetic progression of frequencies, but (15) shows that the prime logarithms still sample its positive part with quadratic logarithmic mass.

**Infinite jump activity does not help.** Tonelli is applied to nonnegative terms, so no exchange of conditionally convergent signed quantities is involved.

**Off-critical exact data do not trigger the same axis obstruction.** Equation (21) gives the matched control for every Lévy exponent.

**The theorem is not a global Weil positivity theorem.** It generates neither the archimedean Gamma term nor the pole/global counterterms and does not identify the Weil autocorrelation pairing. It is a no-go for one candidate source of independent geometric positivity.

Genuine escapes remain:

- a non-Markov positive band-pass functional calculus such as (22), if Mathia can force it canonically and if it survives all mixed-mode and global-completion tests;
- non-translation-invariant arithmetic geometry rather than a function of the Kronecker generator alone;
- matrix-valued, graded, boundary, quotient, compression, or cohomological structures in which positivity is established before scalarization;
- a genuinely nonseparable finite--archimedean object that changes the operator/state before the present spectral cost is formed;
- or a positive form on a different test/function space whose relation to the exact completion is not the raw density spectral energy (2).

## Research consequence

The apparent Markov escape left between `WP-109` and `WP-114` is closed:

\[
\boxed{
\text{exact critical Prime-Lattice first harmonics}
+
\text{nontrivial scalar Kronecker Lévy/Dirichlet geometry}
\Longrightarrow
\text{infinite positive energy}.
}
\tag{28}
\]

This matters because `psi(0)=0` is not an arbitrary tuning choice for a conservative Dirichlet energy; it is forced by preservation of constants. The very structural principle that gives the candidate an independent Markov positivity theorem therefore puts it into the class ruled out by (28).

The surviving scalar spectral direction is correspondingly less canonical: it must use a positive but non-Markov band-pass/smoothing multiplier whose shape still requires an independent geometric explanation. The more structural alternatives remain the same ones repeatedly surviving the line's adversarial tests: **change the architecture before positivity**, or find a single global finite--archimedean geometry whose sign theorem acts before the explicit-formula decomposition.