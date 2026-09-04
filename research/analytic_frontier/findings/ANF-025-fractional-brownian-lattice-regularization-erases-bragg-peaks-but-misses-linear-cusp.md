# ANF-025 — fractional-Brownian lattice regularization erases Bragg peaks but misses the linear cusp

**Status:** `LITERATURE+DERIVED + EXACT-ASYMPTOTIC + NEGATIVE/OBSTRUCTION + DIFFRACTION-DUAL`. `ANF-023` shows that iid lattice perturbations can have excellent small-frequency diffuse behavior but fail the Montgomery--Taylor budget because cloaking a reciprocal-lattice atom transfers too much mass into the diffuse part. `ANF-024` then excludes iid-gap renewal processes. A natural correlated-displacement escape has now appeared in the literature: Thomassey--Lachièze-Rey--Shapira regularize the Palm lattice by a fractional Brownian motion (fBm) with stationary increments. Their construction genuinely removes the nonzero lattice Bragg peaks and, for Hurst index `0<H<1/2`, produces a hyperuniform stationary process.

That escape nevertheless fails the exact diffraction target of `ANF-020` already at zero frequency. In the paper's angular-frequency convention, the one-dimensional fBm-regularized Palm lattice has structure factor

\[
s_H(t)\sim \alpha_H |t|^{1-2H},
\qquad
\alpha_H=2H\Gamma(2H)\sin(\pi H)>0.
\]

After conversion to the Mathia convention `e^{-2\pi i h x}`, and after arbitrary spatial dilation to intensity `rho>0`, its diffuse density satisfies

\[
\boxed{
S_{H,\rho}(h)
\sim
\kappa_H\,\rho^{2H-1}|h|^{1-2H},
\qquad
\kappa_H
=
2H\Gamma(2H)\sin(\pi H)(2\pi)^{1-2H}>0.
}
\]

Consequently, for every finite `a>0`,

\[
\boxed{
\frac{S_{H,\rho}(h)}{a|h|}
\longrightarrow+\infty
\qquad(h\to0).
}
\]

Thus no fixed fBm regularization, at any Hurst index or intensity, can satisfy even the local diffuse part of

\[
\mu\le a\delta_0+a|h|\,dh
\]

on a neighborhood of zero. In particular it cannot realize the Montgomery--Taylor witness with `a=a_MT=C_MT^{-1}`. The obstruction also survives any fixed convex mixture of fBm-regularized profiles: nonnegativity and Fatou force the same infinite ratio at the origin.

The result identifies a sharp tradeoff between two natural lattice-regularization mechanisms. Independent stationary displacements can make the diffuse term vanish quadratically but retain Bragg peaks; fractional-Brownian stationary-increment regularization erases those peaks but makes the zero-frequency diffuse spectrum vanish strictly slower than linearly whenever it is hyperuniform. **Hyperuniformity by itself is therefore far below the spectral regularity required by the Montgomery--Taylor order interval.**

## 1. The correlated regularization is a genuine escape from iid Bragg persistence

Thomassey, Lachièze-Rey and Shapira consider a stationary point process of intensity one through its Palm distribution and perturb its Palm points by an independent Gaussian field with stationary increments. Their Theorem 1.1 proves that for a fractional Brownian field the perturbed Palm configuration is the Palm distribution of an ergodic stationary point process of the same intensity and that its Bartlett spectrum is absolutely continuous away from the trivial forward component.

For the one-dimensional Palm lattice `Z`, the paper emphasizes the distinction from stationary iid lattice perturbations: the atomic spectral component carrying the underlying reciprocal lattice is erased. Proposition 1.3 then gives, for fBm variance

\[
\operatorname{Var}(B_t)=|t|^{2H},
\qquad 0<H<1,
\]

the exact small-frequency asymptotic

\[
s_H(t)\sim
\alpha_H |t|^{1-2H},
\qquad
\alpha_H=2H\Gamma(2H)\sin(\pi H).
\tag{1}
\]

Since `H in (0,1)`, every factor in `alpha_H` is positive. The same proposition states that the process is hyperuniform exactly for `H<1/2`.

This is not the iid model already killed in `ANF-023`. For `H\ne1/2`, increments of fBm are correlated, and the construction acts on the Palm lattice by a stationary-increment field precisely to eliminate the persistent Bragg structure that survives ordinary stationary perturbations.

## 2. Montgomery--Taylor requires a linear cusp, not merely vanishing structure factor

The Fourier convention in `ANF-020` is `e^{-2\pi i h x}`, whereas the source uses angular frequency `t`. Put

\[
S_H(h):=s_H(2\pi h).
\]

Equation (1) becomes

\[
S_H(h)
\sim
\kappa_H|h|^{1-2H},
\qquad
\kappa_H:=\alpha_H(2\pi)^{1-2H}>0.
\tag{2}
\]

Now dilate the unit-intensity process spatially so its intensity is `rho>0`. For normalized per-particle diffraction, spatial dilation sends the forward atom to `rho delta_0` and sends the diffuse profile to

\[
S_{H,\rho}(h)=S_H(h/\rho).
\tag{3}
\]

Combining (2) and (3),

\[
S_{H,\rho}(h)
\sim
\kappa_H\rho^{2H-1}|h|^{1-2H}.
\tag{4}
\]

The target measure of `ANF-020` is

\[
\nu_a=a\delta_0+a|h|\,dh.
\tag{5}
\]

Measure domination by (5) would require

\[
S_{H,\rho}(h)\le a|h|
\quad\text{for a.e. sufficiently small }h.
\tag{6}
\]

But (4) gives

\[
\frac{S_{H,\rho}(h)}{a|h|}
\sim
\frac{\kappa_H}{a}\rho^{2H-1}|h|^{-2H}
\longrightarrow+\infty.
\tag{7}
\]

This contradiction is independent of the forward-atom condition `rho<=a`. Reducing the intensity can change only the positive coefficient in (4); it cannot change the exponent.

The three Hurst regimes make the mismatch transparent:

- `0<H<1/2`: `S(h)->0`, so the process is hyperuniform, but the exponent `1-2H` lies strictly between zero and one and the decay is too slow for a linear envelope;
- `H=1/2`: `S(h)` tends to a positive constant;
- `1/2<H<1`: `S(h)` diverges at the origin.

Hence no member of the fBm family even reaches the local `O(|h|)` regularity needed before the rest of the support-one band is tested.

## 3. Fixed convex mixtures cannot average away the exponent defect

Let `pi` be a probability measure on parameter pairs `(H,rho)` with

\[
0<H<1,\qquad \rho>0,
\]

and suppose the barycenter of the corresponding normalized diffraction profiles is locally finite. Its diffuse density is

\[
\overline S(h)
=
\int S_{H,\rho}(h)\,d\pi(H,\rho).
\tag{8}
\]

All integrands are nonnegative. For every fixed parameter pair, (7) implies

\[
\liminf_{h\to0}
\frac{S_{H,\rho}(h)}{|h|}
=+\infty.
\]

Fatou's lemma therefore gives

\[
\boxed{
\liminf_{h\to0}
\frac{\overline S(h)}{|h|}
\ge
\int
\liminf_{h\to0}
\frac{S_{H,\rho}(h)}{|h|}
\,d\pi
=+\infty.
}
\tag{9}
\]

So a fixed convex mixture of Hurst indices and spatial scales cannot satisfy `\overline S(h)<=a|h|` near zero for any finite `a`. Unlike the symplectic mixtures in `ANF-021`, which pass the local cusp gate and fail only at a moderate frequency, fBm mixtures are eliminated before any finite-frequency optimization is needed.

Equation (9) also shows that adding other nonnegative diffraction components cannot repair a mixture that assigns positive total mass to fBm-regularized components; there is no cancellation available in the positive measure cone.

## 4. The obstruction exposes a Bragg-versus-cusp tradeoff

The contrast with `ANF-023` is load-bearing. For an iid displacement law with finite nonzero variance, the diffuse factor

\[
1-|\varphi(h)|^2
\]

is typically `O(h^2)` at the origin, which is comfortably below a linear target. Its failure is instead at the first reciprocal-lattice frequency: removing the Bragg atom there forces unit diffuse intensity at the same location.

The fBm Palm regularization was designed to remove precisely that periodic spectral memory. It succeeds: the nonzero lattice atoms disappear. But the price is long-range correlated displacement whose diffuse structure factor has the power law (1). In the hyperuniform regime this exponent is always strictly less than one. Thus these two canonical regularizations fail on complementary sides:

\[
\text{iid stationary displacement: good local cusp, persistent Bragg obstruction;}
\]

\[
\text{fBm stationary-increment displacement: Bragg erasure, bad local cusp.}
\]

The Montgomery--Taylor budget demands both properties simultaneously: no nonzero atoms in the open band and at most a linear diffuse cusp with the sharp coefficient `a_MT`.

## 5. Prior-art and novelty boundary

The stationary-increment Palm regularization, absolute continuity of its Bartlett spectrum, disappearance of the lattice Bragg component, and the asymptotic (1) are prior art from Loïc Thomassey, Raphaël Lachièze-Rey and Assaf Shapira, *Regularization of a stationary point process by a stationary increments perturbation*, arXiv:2602.19773v1 (23 February 2026), Theorem 1.1 and Proposition 1.3.

What is derived here is the exact specialization of that asymptotic to the diffraction order interval of `ANF-020`: the Fourier-convention conversion (2), arbitrary-intensity scaling (3)--(4), the local impossibility (7), and the fixed-mixture obstruction (9). A targeted search did not locate this Montgomery--Taylor specialization. No publication-level novelty claim is made.

This result does **not** rule out arbitrary correlated displacement fields. The source explicitly notes that the spectral cancellation formula is special to fractional Brownian fields and that general Gaussian stationary-increment perturbations can behave differently. Nor does it rule out a parameter-dependent weak-* limiting construction in which `H` itself tends to the boundary `0` while the candidate changes; the asymptotic (1) is not uniform in `H` there. That boundary must be audited separately before claiming closure of the full fBm-generated weak-* family.

## 6. Consequence for the scalar frontier

`ANF-024` showed that independent successive gaps are too rigid: linear-cusp domination forces a renewal law to collapse to a lattice. `ANF-025` now shows that introducing a canonical long-range correlated stationary-increment displacement is not enough either. Even though the correlations erase the reciprocal lattice completely, fractional-Brownian self-similarity forces the wrong infrared exponent.

A stochastic diffraction witness for `ANF-020` must therefore meet a sharper first gate than generic hyperuniformity:

\[
\boxed{S(h)=O(|h|)\quad(h\to0)}
\]

with no nonzero pure-point mass in the support-one band. Only after that local condition is met does the coefficient `a_MT` and the rest of the band become relevant. Candidate correlated processes whose structure factor behaves like `|h|^\gamma` with `0<\gamma<1` can now be rejected immediately, regardless of how effectively they suppress Bragg peaks.

The configuration-level branch from `ANF-006` remains untouched: this obstruction concerns only the universal-affine scalar diffraction realization obtained after pair compression.
