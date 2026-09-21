# AF-475 — Compressibility profiles set resolution-dependent Hilbert conditioning

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-RESTRICTION`, `APPROXIMATE-SPARSITY`, `POSITIVE-RECOVERY`, `SCALE-AWARE`, `NO-NOVELTY-CLAIM`

## Claim

AF-474 prices a fixed best-`s`-term tail budget by the pair `(s,epsilon)`. A source class usually supplies something richer: a whole **compressibility profile**, describing how the unresolved tail decreases as the retained support budget grows.

That profile can be converted directly into a resolution-dependent Hilbert condition function.

Let `A` be a finite or countable alphabet and let

\[
\tau_s(\mu)
=
\inf_{S\subset A,\ |S|\le s}\mu(A\setminus S)
\]

be the best `s`-term tail mass. Let `phi:N-> [0,1]` be nonincreasing, and consider the source class

\[
\mathcal C_\phi
=
\{\mu\in\operatorname{Prob}(A):\tau_s(\mu)\le \phi(s)\text{ for every }s\ge1\}.
\tag{1}
\]

For the scaled coordinate Hilbert embedding

\[
H(\mu)=\sqrt2\,\mu\in\ell^2(A),
\]

AF-474 gives, for every integer `s>=1`,

\[
\frac{(d_1(\mu,\nu)-2\phi(s))_+}{\sqrt{s}}
\le
\|H(\mu)-H(\nu)\|_2
\le
 d_1(\mu,\nu),
\tag{2}
\]

where `d_1(mu,nu)=||mu-nu||_1`.

Fix an absolute resolution `delta>0` and require inverse fidelity only for pairs with `d_1(mu,nu)>=delta`. Define

\[
\boxed{
K_\phi(\delta)
:=
\inf_{\substack{s\ge1\\2\phi(s)<\delta}}
\frac{\sqrt{s}}{1-2\phi(s)/\delta}.
}
\tag{3}
\]

Then every pair `mu,nu in C_phi` with `d_1(mu,nu)>=delta` obeys

\[
\boxed{
\frac1{K_\phi(\delta)}d_1(\mu,\nu)
\le
\|H(\mu)-H(\nu)\|_2
\le
 d_1(\mu,\nu),
}
\tag{4}
\]

with the convention that the infimum over an empty set is infinity.

Thus a tail profile induces an explicit **conditioning-versus-resolution curve**. If `phi(s)->0`, then `K_phi(delta)<infinity` for every fixed `delta>0`, even though AF-473 forbids a single finite distortion valid uniformly down to all nonzero scales whenever diffuse tails remain possible.

The effective source resource at resolution `delta` is therefore not a single support number and not a single tail mass. It is the optimized tradeoff

\[
\boxed{
\text{effective support cost at scale }\delta
\quad\sim\quad
\inf_s
\frac{\sqrt{s}}{1-2\phi(s)/\delta}.
}
\tag{5}
\]

This turns the qualitative statement "the source is compressible" into a quantitative object that can be compared directly with the minimum separation consumed by a downstream theorem.

## Derivation

For `mu,nu in C_phi`, AF-474 gives

\[
\|H(\mu)-H(\nu)\|_2
\ge
\frac{d_1(\mu,\nu)-2\phi(s)}{\sqrt{s}}
\]

whenever the numerator is positive. If `d_1(mu,nu)>=delta` and `2phi(s)<delta`, then

\[
\begin{aligned}
\|H(\mu)-H(\nu)\|_2
&\ge
\frac{d_1(\mu,\nu)}{\sqrt{s}}
\left(1-\frac{2\phi(s)}{d_1(\mu,\nu)}\right)\\
&\ge
\frac{1-2\phi(s)/\delta}{\sqrt{s}}
\,d_1(\mu,\nu).
\end{aligned}
\tag{6}
\]

Taking the best admissible `s` gives `(3)`--`(4)`. The upper inequality in `(4)` is the probability-simplex estimate already used in AF-474.

No reconstruction algorithm or finite-dimensional measurement model is involved. The result is a direct conversion from source approximation rate to inverse conditioning of the canonical Hilbert representation.

## Polynomial tail profiles

Suppose there are constants `A>0` and `alpha>0` such that

\[
\phi(s)\le A s^{-\alpha}.
\tag{7}
\]

Ignoring the integer constraint momentarily, the AF-474 bound becomes

\[
F_\delta(s)
=
\frac{\sqrt{s}}
{1-(2A/\delta)s^{-\alpha}}.
\tag{8}
\]

Writing `r=2A/delta`, differentiation of `log F_delta` shows that the continuous optimum occurs when

\[
r s^{-\alpha}=\frac1{2\alpha+1},
\]

or equivalently

\[
s_*(\delta)
=
\left(
\frac{2A(2\alpha+1)}{\delta}
\right)^{1/\alpha}.
\tag{9}
\]

At that balance point, the tail consumes exactly a fixed fraction `1/(2alpha+1)` of the available resolution budget. Substitution gives the continuous envelope

\[
F_\delta(s_*)
=
\frac{2\alpha+1}{2\alpha}
\left(
\frac{2A(2\alpha+1)}{\delta}
\right)^{1/(2\alpha)}.
\tag{10}
\]

For the actual integer problem, take

\[
s_\delta
=
\left\lceil
\left(
\frac{2A(2\alpha+1)}{\delta}
\right)^{1/\alpha}
\right\rceil
\]

in the high-resolution regime where the quantity inside the ceiling is at least one. Since increasing `s` only decreases the tail term,

\[
\boxed{
K_\phi(\delta)
\le
\frac{2\alpha+1}{2\alpha}\sqrt{s_\delta}.
}
\tag{11}
\]

Consequently,

\[
\boxed{
K_\phi(\delta)
=O\!\left((A/\delta)^{1/(2\alpha)}\right)
\qquad(\delta\downarrow0).
}
\tag{12}
\]

A polynomial best-term tail therefore becomes a polynomial loss of inverse Hilbert conditioning, with exponent exactly half the reciprocal tail exponent in this coordinate bound.

## Stretched-exponential tail profiles

Suppose instead that

\[
\phi(s)\le A e^{-c s^\beta}
\tag{13}
\]

for `A,c,beta>0`. For `delta<4A`, choose

\[
s_\delta
=
\left\lceil
\left(
\frac1c\log\frac{4A}{\delta}
\right)^{1/\beta}
\right\rceil.
\tag{14}
\]

Then `phi(s_delta)<=delta/4`, so the denominator in `(3)` is at least `1/2`. Hence

\[
\boxed{
K_\phi(\delta)
\le
2\sqrt{s_\delta}
=
O\!\left(
\left(\log\frac{A}{\delta}\right)^{1/(2\beta)}
\right).
}
\tag{15}
\]

Thus exponentially or stretched-exponentially compressible sources pay only a polylogarithmic conditioning cost as the demanded resolution becomes finer. This is qualitatively different from the power-law deterioration forced by polynomial tail decay.

## Exact boundary checks

The profile formulation recovers the two neighboring regimes without changing the fidelity notion.

If the class has a hard support cap `s_0`, then `phi(s_0)=0`, and `(3)` immediately gives

\[
K_\phi(\delta)\le\sqrt{s_0}
\]

for every `delta>0`, recovering the scale-free positive mechanism of AF-472.

If instead the only available statement is a fixed nonzero tail budget `phi(s)=epsilon` for all relevant `s`, then no `s` is admissible in `(3)` when `delta<=2epsilon`. Above that scale, `(3)` reduces to the AF-474 bound. This matches the obstruction in AF-473: a fixed positive tail can hide unbounded combinatorial complexity at arbitrarily fine scales.

If `phi(s)>0` for every finite `s` but `phi(s)->0`, the intermediate regime is now explicit: every fixed positive resolution has finite coordinate conditioning, while the support budget needed to reach that resolution tends to infinity as `delta->0`. The resulting divergence of the upper bound is not itself an impossibility theorem for every Hilbert embedding, but it cleanly identifies the source resource the coordinate construction consumes.

## Prior-art and novelty audit

The approximation-theoretic mechanism is classical, and **no theorem-level novelty is claimed** for converting decay of best-term approximation errors into rates.

- Ronald A. DeVore, **"Nonlinear approximation,"** *Acta Numerica* 7 (1998), 51--150, DOI `10.1017/S0962492900002816`, develops approximation classes precisely through the decay rate of nonlinear/best-term approximation error. This is the standard language behind treating `s -> phi(s)` as a compressibility profile rather than a single sparsity parameter.
- Albert Cohen, Wolfgang Dahmen, and Ronald DeVore, **"Compressed sensing and best k-term approximation,"** *Journal of the American Mathematical Society* 22(1) (2009), 211--231, DOI `10.1090/S0894-0347-08-00610-3`, relates recovery quality to best `k`-term approximation and instance-optimal error. It is the closest standard framework to the profile optimization performed here.
- Emmanuel J. Candès, Justin Romberg, and Terence Tao, **"Stable signal recovery from incomplete and inaccurate measurements,"** *Communications on Pure and Applied Mathematics* 59(8) (2006), 1207--1223, DOI `10.1002/cpa.20124`, is a classical source for stable recovery in which approximation/noise errors enter quantitatively rather than being treated as exact sparsity.

A targeted prior-art search recovered the mature nonlinear-approximation and compressed-sensing literature, including the standard viewpoint that best-term decay defines approximation classes and recovery rates. It did not support a novelty claim for `(3)` or the polynomial/stretched-exponential substitutions. The Arithmetic Fidelity value is narrower: AF-475 packages the AF-474 probability-tail inequality into the exact quantity needed by this research line, namely a **source-side condition curve indexed by the downstream discrimination scale**.

## Boundary and falsification audit

- **`K_phi(delta)` is an achieved coordinate-Hilbert upper bound, not a minimax optimum over all Hilbert embeddings.** A different representation may improve it on a narrower source class.
- **The profile must be proved at the source layer.** An informal claim of power-law or exponential concentration does not license `(12)` or `(15)`.
- **The resolution is absolute source separation.** If the downstream theorem needs relative error, signed cancellation, phase, provenance, or another metric, its required discriminator must first be related rigorously to `d_1`.
- **The optimization spends two resources against each other.** Larger `s` decreases `phi(s)` but worsens the `sqrt(s)` support factor. Sending `s` to infinity is never free.
- **The polynomial exponent in `(12)` is specific to the AF-474 coordinate estimate.** It should not be promoted to a universal lower bound without a separate hard family showing that every Hilbert embedding pays the same rate.
- **The stretched-exponential estimate uses a convenient half-resolution budget, not an optimized constant.** Its asymptotic polylogarithmic order is the relevant conclusion here.
- **A hard support cap is qualitatively special.** It is the only case among these examples where this argument gives a resolution-independent finite condition number.
- **No arithmetic selectivity is created by fast decay.** A source may be extremely compressible while a matched non-prime control has the same profile. The prime discriminator still has to live in the retained structure.

## Arithmetic-fidelity consequence

AF-474 left the live application question as a three-way tradeoff between effective support `s`, tail mass `epsilon`, and required separation `delta`. AF-475 removes one degree of arbitrariness when the source supplies a full approximation law: the tail profile `phi(s)` determines the best support scale to use at each downstream resolution.

For a prime-derived carrier, the next source-specific target is therefore sharper than "prove approximate sparsity." One should determine or bound

\[
\phi_{\mathrm{arith}}(s)
=
\sup_{\mu\in\mathcal C_{\mathrm{arith}}}\tau_s(\mu),
\]

identify the smallest source separation `delta_arith` that the eventual zero-selection, sign, or rigidity mechanism must resolve, and then evaluate `K_{phi_arith}(delta_arith)`.

A useful arithmetic compression route requires all three facts simultaneously:

1. `phi_arith(s)` actually decays at the layer being compressed;
2. the retained coordinates still carry a rational-prime discriminator against matched controls;
3. the resulting `K_{phi_arith}(delta_arith)` is finite and quantitatively compatible with the downstream theorem.

This is a concrete bridge from source regularity to compression fidelity. Polynomial and stretched-exponential decay no longer merely say that the arithmetic carrier is "concentrated"; they predict explicit power-law or polylogarithmic deterioration in the conditioning required to preserve distinctions at finer resolution.