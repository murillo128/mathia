# PL-279 — Canonical Sobolev prime-power activation is quadratically soft in overlap width

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PROVED-BOUND + REPRESENTATION-CORRECTION + NEGATIVE-REDIRECT + PRIOR-ART-AUDITED`

## Claim

In the canonical localized Weil/Suzuki quadratic-form geometry on `H_0^1(-a,a)`, a newly active prime-power source at shift

\[
h=\log q,\qquad q=p^m,
\]

does not enter with an order-one form effect when the aperture crosses its activation threshold `2a=h`. If

\[
\delta:=2a-h>0,
\]

then its full symmetric Weil contribution obeys

\[
\boxed{
\left|
-\frac{\Lambda(q)}{\sqrt q}\bigl(F_v(h)+F_v(-h)\bigr)
\right|
\le
\frac{\pi}{4}\frac{\Lambda(q)}{\sqrt q}\,\delta^2\,\|v'\|_{L^2(-a,a)}^2,
}
\]

for every `v in H_0^1(-a,a)`, where `F_v=v*\widetilde v` is the Hermitian autocorrelation used in Weil's quadratic form.

Thus an isolated prime-power atom turns on at most **quadratically in the physical overlap width** `delta=2a-log q` in the natural Sobolev form topology. This corrects the interpretation suggested by the finite rescaled edge model of `PL-264`: an order-one edge shock can occur after a cutoff-dependent rescaling, but it is not an intrinsic order-one singularity of the canonical `H_0^1` localized Weil form.

The result does not make the source arithmetic irrelevant away from threshold. It redirects the prime-lattice search toward accumulated/multi-edge coupling and the finite low/mesoscopic negative sector identified in `PL-278`, rather than toward isolated threshold shocks.

## 1. Exact arithmetic term in the localized Weil form

Suzuki's 2026 formulation starts from the Weil functional. For a test function `F`, its prime-power contribution is

\[
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(F(\log n)+F(-\log n)\bigr).
\]

For the quadratic form one inserts the Hermitian autocorrelation `F_v=v*\widetilde v`. If `v` is supported in `(-a,a)`, then `F_v` is supported in `[-2a,2a]`; hence the atom `q` can contribute only when `h=log q<2a`. At equality the overlap has measure zero, so the threshold is strict.

For `h>0` write

\[
C_h(v):=\int_{\mathbb R}v(x)\overline{v(x-h)}\,dx.
\]

With the standard Hermitian convention,

\[
F_v(h)=C_h(v),\qquad F_v(-h)=\overline{C_h(v)},
\]

and the `q`-source contribution is therefore

\[
-2\frac{\Lambda(q)}{\sqrt q}\operatorname{Re}C_h(v).
\]

This is an identity from the completed Weil explicit formula; no Euler product is being continued into the critical strip.

## 2. Boundary traces force quadratic threshold softness

Assume `0<h<2a` and set `delta=2a-h`. Because `v in H_0^1(-a,a)`, its one-dimensional Sobolev representative has zero traces at both endpoints. The overlap of `v(x)` and `v(x-h)` is `x in (h-a,a)`. Put

\[
x=h-a+y=a-\delta+y,\qquad 0<y<\delta.
\]

Then

\[
x-h=-a+y,
\]

so the two factors lie respectively at distances `delta-y` from the right boundary and `y` from the left boundary. The fundamental theorem of calculus and Cauchy--Schwarz give

\[
|v(-a+y)|\le \sqrt y\,\|v'\|_2,
\qquad
|v(a-(\delta-y))|\le \sqrt{\delta-y}\,\|v'\|_2.
\]

Consequently

\[
\begin{aligned}
|C_h(v)|
&\le \|v'\|_2^2
\int_0^\delta \sqrt{y(\delta-y)}\,dy\\
&=\frac{\pi}{8}\delta^2\|v'\|_2^2.
\end{aligned}
\]

Since `|F_v(h)+F_v(-h)| <= 2|C_h(v)|`, multiplication by the exact von-Mangoldt weight gives

\[
\left|
\frac{\Lambda(q)}{\sqrt q}\bigl(F_v(h)+F_v(-h)\bigr)
\right|
\le
\frac{\pi}{4}\frac{\Lambda(q)}{\sqrt q}\delta^2\|v'\|_2^2.
\]

The estimate is uniform over the unit ball of the Dirichlet seminorm. Its content is therefore form-norm softness, not merely pointwise vanishing for a fixed smooth test function.

## 3. Relation to the prime-exponent lattice

The threshold condition for the prime power `q=p^m` is

\[
2a=m\log p.
\]

In exponent coordinates this is exactly the moment at which the axis point `m e_p` reaches the log-energy window. `PL-264` showed that, in a finite Connes--van Suijlekom-style rescaled Galerkin model, the newly activated edge has a universal rank-two local shape, with arithmetic entering only through `Lambda(q)` and the shift position. The present estimate shows that the corresponding activation in the canonical Suzuki/Bombieri Sobolev form is qualitatively softer: before any rescaling that keeps a shrinking overlap at finite size, its form effect is `O((2a-m log p)^2)` relative to derivative energy.

Therefore the finite-model edge shock should not be promoted to a representation-independent arithmetic singularity. The durable common content of both pictures is the activation location and von-Mangoldt weight; the local amplitude law depends on the functional geometry used to probe that activation.

## 4. Consequence for the current frontier

`PL-278` isolates the finite negative spectral sector of the canonical compact-resolvent operator as the only place where the completed fixed-aperture problem can retain RH-sensitive arithmetic information. The present estimate rules out a tempting mechanism for that sector: a single newly entering prime power does not produce an intrinsic order-one Sobolev-form impulse at its threshold.

Any source-specific spectral rigidity must therefore survive despite this quadratic local onset. Plausible targets are coherent accumulation of many already active prime-power shifts, interactions between several shifts, or global motion of the finite negative sector across a substantial aperture range. A mechanism that depends only on an isolated edge appearing discontinuously is representation-dependent and is not supported by the canonical form geometry.

## 5. Prior-art and adversarial audit

Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096, supplies the exact Weil functional, the localized `H_0^1(-a,a)` setup, and the prime-power source with weights `Lambda(n)/sqrt(n)`. It is already source 56 in `research/prime_lattice/SOURCES.md`. The quadratic overlap estimate above is a direct Sobolev derivation from those formulas; no independent literature novelty is claimed for the inequality itself.

Kim--Hong--Kim--Choi--Jang--Shin--Kim, *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator*, arXiv:2607.24830, reports numerically that the lowest eigenvalue passes smoothly through the first prime threshold. That observation is adjacent prior art and is consistent with the bound, but it is not used as a theorem and does not supply the uniform `H_0^1` form estimate proved here.

Repository audit against `PL-264`, `PL-266`, `PL-269`, and `PL-278` found no stored derivation of the `O(delta^2)` threshold law. The novelty claimed here is only the project-level structural correction: the canonical Sobolev realization suppresses an isolated prime-power activation quadratically, so the finite-rescaled local edge shock of `PL-264` is not an intrinsic threshold singularity.

## 6. Boundaries and falsification

The estimate is local to a newly active shift and uses the Dirichlet trace condition of `H_0^1(-a,a)`. It does not prove differentiability of any eigenvalue as a function of `a`, does not prove continuity or monotonicity of higher eigenvalues, and does not give a uniform cross-aperture perturbation theorem because the form domains themselves vary with `a`.

It also does not say that prime-power terms remain small after their overlap becomes macroscopic, nor that several simultaneously active shifts cannot combine into a substantial low-spectrum effect. The coefficient `Lambda(q)/sqrt(q)` remains genuinely arithmetic. The claim would be falsified by a function `v in H_0^1(-a,a)` violating the displayed overlap bound or by a different canonical Weil-source normalization in which the `q` contribution is not the symmetric autocorrelation term stated above; both ingredients are explicit in the derivation.
