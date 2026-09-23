# WI-423 — the canonical Blaschke Riesz source is atomic, so planar absolute continuity already forces zero defect

Status: `CLASSICAL-IDENTITY + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`

Parents: `WI-409`, `WI-411`, `WI-416`, `WI-417`, `WI-421`, `WI-422`

## Claim

The translated Blaschke kernel used in the recent source-regularity thread is not merely analogous to a half-plane Green kernel: for the canonical zeta Blaschke defect it *is* the Green kernel, and its canonical Riesz source is exactly the off-critical zero-counting measure.

Write

\[
H=\{z=x+iy:x>0\},\qquad
w_\rho=(\beta-\tfrac12)+i\gamma\in H
\]

for a zero \(\rho=\beta+i\gamma\) with \(\beta>1/2\), and let

\[
w_\rho^*=-(\beta-\tfrac12)+i\gamma
\]

be its reflection across \(\partial H\). For the half-plane Blaschke factorization of Kunik, define

\[
U(z):=-\log|B(\tfrac12+z)|.
\]

Then, distributionally on \(H\),

\[
\boxed{
-\Delta U
=2\pi\mu_{\rm off},\qquad
\mu_{\rm off}
=\sum_{\Re\rho>1/2}m_\rho\,\delta_{w_\rho}.
}
\]

Consequently, if the *canonical exact source* of this defect admitted a representation

\[
U=G(f\,dA)+h
\]

with \(f\in L^1_{\rm loc}(H)\) (hence, a fortiori, with an \(L^p\) planar density) and \(h\) harmonic, then \(\mu_{\rm off}=f\,dA\). The left-hand side is purely atomic and the right-hand side is absolutely continuous, so both must vanish. There are no zeros with \(\Re\rho>1/2\); by the functional equation and conjugation symmetry there are then no nontrivial zeros with \(\Re\rho<1/2\) either.

Thus **planar absolute continuity, let alone \(L^p\) regularity, of the canonical exact Blaschke/Riesz source is already an RH-level conclusion rather than an intermediate regularity theorem**.

This does **not** invalidate the auxiliary-source estimates of `WI-417`–`WI-422`. It separates two objects that must not be conflated:

1. the **canonical Riesz source** of the exact zeta Blaschke defect, which is the atomic off-line zero measure above; and
2. an **auxiliary probe/coefficient source** \(\nu(a,b)\) used to superpose translated kernels in a coercive inequality, which may in principle have an \(L^p\), Lorentz, density, or other concentration-sensitive norm bound.

Any viable continuation of the source-regularity program must obtain the second object from genuinely independent prime-side, boundary, or explicit-formula information and prove a quantitative coupling from it to the off-line defect. It cannot obtain a nontrivial intermediate theorem merely by smoothing or re-describing the first object while retaining exact equality modulo a harmonic term.

## Exact derivation

Kunik's half-plane factorization uses, for each zero \(\rho\) with \(\Re\rho>1/2\), the factor

\[
B_\rho(s)
=
\frac{1-s/\rho}{1-s/(1-\bar\rho)}
\left|\frac{\rho}{1-\rho}\right|.
\]

Taking moduli cancels the normalizing constants:

\[
|B_\rho(s)|
=
\frac{|s-\rho|}{|s-(1-\bar\rho)|}.
\]

After shifting \(s=1/2+z\), the reflected zero \(1-\bar\rho\) becomes \(w_\rho^*\), so

\[
-\log|B_\rho(\tfrac12+z)|
=
\log|z-w_\rho^*|-\log|z-w_\rho|
=:q_{w_\rho}(z).
\]

In coordinates \(w=a+ib\) and \(z=d+i\gamma\), this is exactly the translated kernel already used in `WI-411`–`WI-422`:

\[
q_{a,b}(\gamma,d)
=
\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2}.
\]

The classical distributional identity

\[
\Delta\log|z-w|=2\pi\delta_w
\]

now gives, inside \(H\),

\[
-\Delta q_w=2\pi\delta_w,
\]

because \(w^*\notin H\). Summing with zero multiplicities yields the displayed formula for \(-\Delta U\). This is local as a distributional statement: zeros are discrete, and away from their singularities the remaining Blaschke contribution is harmonic. Equivalently, \(\mu_{\rm off}\) is the Riesz measure of the positive Green potential \(U\).

If another exact representation \(U=G(f\,dA)+h\) held with \(h\) harmonic, applying \(-\Delta\) would give

\[
2\pi\mu_{\rm off}=2\pi f\,dA.
\]

Uniqueness here is therefore not a functional-analytic subtlety: it is equality of distributions. A measure supported on discrete atoms cannot equal a locally integrable planar density unless both vanish.

## Consequence for the current research frontier

`WI-417`–`WI-422` correctly identify concentration-sensitive source regularity as sufficient to turn translated Blaschke probes into coercivity. The present result sharpens what kind of source theorem could actually be useful.

A theorem saying that the **exact canonical zeta Riesz source** belongs to \(L^p(dA)\), or is merely absolutely continuous with respect to area, would already exclude all off-line zeros. Treating such a statement as a modest bridge from arithmetic data would hide essentially the whole target conclusion inside the hypothesis.

The viable version must instead introduce an auxiliary generation/smoothing operator

\[
\text{accessible arithmetic or boundary data}
\longmapsto \nu
\]

for which one can prove both:

- a target-independent concentration budget for \(\nu\) (for example an \(L^p\), Lorentz, bounded-density, or comparable norm); and
- an exact or quantitatively controlled inequality coupling the resulting probe potential to \(\mu_{\rm off}\).

Smoothing \(\mu_{\rm off}\) itself can certainly create an \(L^p\) density, but then it changes the Green potential and loses the exact Riesz-source identity. The approximation/error term becomes the entire mathematical issue and must be controlled explicitly; regularity of the smoothed density alone carries no RH consequence.

## Boundary and falsification

This is a barrier only to a specific interpretation of the source-regularity route.

- It does **not** prove RH, improve the current simple-critical-zero proportion, or provide the missing arithmetic source budget.
- It does **not** rule out auxiliary \(L^p\) coefficient measures, regularized probe families, or inequalities rather than exact potential identities.
- It does **not** say that every useful source variable must be singular. It says that the canonical Riesz source of the exact Blaschke defect is singular whenever off-line zeros exist.
- If a future construction uses a different source whose potential equals \(U\) only after a non-harmonic correction, the atomicity argument no longer closes it automatically; the correction must instead be audited quantitatively.
- Boundary zeros on \(\Re s=1/2\) do not appear in \(\mu_{\rm off}\), as expected: this finding concerns the off-line defect, not simplicity or multiplicity on the critical line.

The claim would be falsified by an error in the identification of Kunik's factor modulus with the half-plane Green factor or in the distributional Laplacian normalization. Both reduce directly to the displayed elementary identities.

## Prior art and novelty audit

The ingredients are classical and no priority claim is made.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829 (2008), gives the relevant half-plane factorization and Blaschke product over zeros with \(\Re\rho>1/2\).
- The identity \(\Delta\log|z-w|=2\pi\delta_w\), the interpretation of zeros as the Riesz measure of logarithmic potentials, and the half-plane Green kernel are standard potential theory / Poincare--Lelong material; see, e.g., Thomas Ransford, *Potential Theory in the Complex Plane*, Cambridge University Press (1995).
- Igor E. Pritsker, *Inequalities for sums of Green potentials and Blaschke products*, Bull. London Math. Soc. 43 (2011), 561--575, provides classical context for the Green-potential viewpoint on Blaschke products.

The repository-local novelty check is narrower. `WI-409`–`WI-422` developed translated Blaschke charges and increasingly strong regularity classes for **auxiliary coefficient measures**, culminating in the sharp \(L^p\) threshold of `WI-422`; they did not explicitly identify the canonical zeta Riesz source with the atomic off-line zero measure and therefore left room for reading a future "source regularity theorem" as regularity of that canonical source. The substantive delta here is the resulting no-go/semantic separation: **canonical-source absolute continuity is already zero defect; useful intermediate regularity must belong to an independently generated auxiliary source.**

## Evidence state

- Kunik half-plane Blaschke factorization: `LITERATURE` / primary source.
- Green-kernel and distributional Laplacian identities: `CLASSICAL-IDENTITY`.
- Identification \(-\Delta U=2\pi\mu_{\rm off}\) for the shifted zeta Blaschke defect: `EXACT-DERIVED`.
- Absolute-continuity-implies-zero-defect consequence: `EXACT-DERIVED`.
- Programmatic conclusion separating canonical and auxiliary sources: `PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

No numerical computation, conjectural zero statistics, RH assumption, wider Fourier support, or unproved moment input is used.