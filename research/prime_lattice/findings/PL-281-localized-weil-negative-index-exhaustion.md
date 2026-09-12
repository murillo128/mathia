# PL-281 — Localized Weil Morse index exhausts the global compact-support negative index

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PROVED-STRUCTURAL + NEGATIVE-INDEX-EXHAUSTION + CONDITIONAL-BRIDGE + PRIOR-ART-AUDITED`

## Claim

Let `q` be the completed Weil quadratic form in the canonical localized Suzuki realization used in `PL-278`--`PL-280`. For each aperture `a>0`, let `D_a` be its localized form domain, identified by zero extension, and let

\[
\nu(a):=\operatorname{ind}_-(q|_{D_a})
\]

be the negative Morse index. By `PL-278`, `nu(a)<infinity` for every finite `a`, and by `PL-280` the domains are nested and `nu(a)` is nondecreasing.

Define the compact-support form domain

\[
\mathcal D_c:=\bigcup_{a>0}D_a
\]

and its global compact-support negative index

\[
\kappa_c
:=
\sup\left\{
\dim E:
E\subset\mathcal D_c\text{ finite-dimensional and }
q[v]<0\text{ for every }0\ne v\in E
\right\},
\]

where `kappa_c` takes values in `N_0 union {infinity}`. Then

\[
\boxed{
\kappa_c
=
\sup_{a>0}\nu(a)
=
\lim_{a\to\infty}\nu(a).
}
\]

Consequently:

- if `kappa_c=r<infinity`, then there is a finite aperture `a_0` such that
  \[
  \boxed{\nu(a)=r\qquad(a\ge a_0);}
  \]
- if `kappa_c=infinity`, then `nu(a)` is unbounded as `a to infinity`;
- a finite-dimensional negative sector of the global compact-support Weil form cannot drift outward in such a way that every finite localization misses it.

For the canonical support-localized family, `PL-260`'s generic warning that negative directions can drift with a changing truncation therefore does **not** apply at the level of the negative index itself. It remains valid when one tries to identify this localized index with Bombieri's different Fourier-side truncation count: that identification still needs an independent theorem.

The mechanism is generic functional analysis for nested compact-support form domains. It does not explain Weil positivity, does not identify `kappa_c` from the zeta zeros, and is not claimed as a new arithmetic theorem.

## 1. Exact exhaustion identity

The inequality

\[
\sup_a\nu(a)\le\kappa_c
\]

is immediate because each `D_a` is contained in `D_c`: every negative subspace admitted by a fixed localized problem is also a compact-support negative subspace of the global form.

For the reverse inequality, let

\[
E\subset\mathcal D_c
\]

be an `r`-dimensional subspace on which `q` is strictly negative. Choose a basis `v_1,...,v_r` of `E`. By definition of the union, each `v_j` lies in some `D_{a_j}`. With

\[
a_E:=\max_{1\le j\le r}a_j,
\]

nestedness gives `v_j in D_{a_E}` for every `j`, hence

\[
E\subset D_{a_E}.
\]

Therefore

\[
r\le\nu(a_E)\le\sup_a\nu(a).
\]

Taking the supremum over all finite-dimensional negative `E` yields

\[
\kappa_c\le\sup_a\nu(a),
\]

and hence

\[
\boxed{\kappa_c=\sup_a\nu(a).}
\]

By `PL-280`, `nu(a)` is a nondecreasing integer-valued function of `a`. Its supremum is therefore its monotone limit as `a to infinity`, proving the full displayed identity.

No spectral convergence theorem is needed. In particular, the argument does not require convergence of individual eigenfunctions, norm-resolvent convergence of `A_a`, or compactness across changing apertures. It uses only nested form domains and the fact that a finite-dimensional subspace has a finite basis, whose supports fit inside one common window.

## 2. Finite global defect forces exact finite-aperture stabilization

Suppose

\[
\kappa_c=r<\infty.
\]

Since `nu(a)` is integer-valued, nondecreasing, and has supremum `r`, it must attain `r` at some finite aperture. Otherwise `nu(a)<=r-1` for every `a`, contradicting the definition of the supremum. Thus there is `a_0<infinity` with

\[
\nu(a_0)=r.
\]

Monotonicity and the global upper bound `nu(a)<=kappa_c=r` now give

\[
\boxed{\nu(a)=r\qquad\text{for all }a\ge a_0.}
\]

This is stronger than merely saying that each fixed aperture has finite Morse index. A globally finite compact-support negative defect is captured completely after a finite support radius and can never be lost or supplemented later.

Conversely, if `kappa_c=infinity`, then for every integer `R` there exists a finite-dimensional compact-support negative subspace of dimension at least `R`. The common-support argument places it in some finite `D_a`, so

\[
\forall R\ge1\quad\exists a_R<\infty:\quad\nu(a_R)\ge R.
\]

Thus an infinite global negative index cannot hide at spatial infinity as infinitely many directions that are individually invisible to every finite window: the localized Morse index itself must become arbitrarily large.

## 3. Relation to smooth Weil test functions

In the canonical Sobolev realization used in `PL-279`, the fixed-aperture domain is `H_0^1(-a,a)` and the closed localized Weil form is obtained from the smooth compact-support test form by closure. Hence `C_c^infty(-a,a)` is a form core. This means the same finite negative index can be detected on smooth compactly supported test functions.

Indeed, if `E subset D_a` is finite-dimensional and strictly negative, compactness of the unit sphere of `E` gives a uniform negative margin after choosing any Hilbert norm on `E`. Approximate a basis of `E` sufficiently closely in the form norm by vectors in `C_c^infty(-a,a)`. The Gram matrix remains nonsingular and the finite form matrix remains negative definite. Therefore every finite-dimensional negative subspace of the closed localized form has a smooth compact-support negative subspace of the same dimension.

Thus `kappa_c` is not an artifact of closing the form domain: it is the negative-index exhaustion of the classical compact-support Weil test geometry as represented by the canonical Suzuki form. In particular, positivity on every finite aperture is the zero-index case,

\[
\kappa_c=0
\quad\Longleftrightarrow\quad
\nu(a)=0\text{ for every }a>0,
\]

which is the localized operator formulation of Weil positivity used throughout this line. The equality above is an exhaustion statement; the RH content remains entirely in proving that its common value is zero.

## 4. What this does and does not resolve from PL-260

`PL-260` retained an important caution when importing Bombieri's finite Fourier-side theorem: a negative direction for one truncation family may move with truncation scale, so an exact finite defect count proved for one family cannot simply be assigned to another family.

The present result removes one particular version of that concern **inside the canonical support-localized family**. A fixed finite-dimensional negative subspace of the global compact-support form has a finite basis and therefore a common finite support radius. It must occur inside some `D_a`; once present, `PL-280` says its contribution to the Morse index cannot disappear. Hence the canonical support exhaustion has no hidden finite negative defect at infinity.

What remains unjustified is the arithmetic identification

\[
\kappa_c
\stackrel{?}{=}
\frac12\,N_{\mathrm{off}},
\]

where `N_off` denotes an appropriate count of off-critical-line zeros in the finite-defect setting considered by Bombieri. Bombieri's theorem concerns a different finite Fourier-side truncation. The equality of the two indices is **not** proved here, and no claim is made that Bombieri's stabilization theorem transfers automatically to the Suzuki support-localized operator.

If a future zero-side theorem independently identifies the global compact-support index `kappa_c=r`, however, no further localization theorem is needed: the present exhaustion identity immediately forces `nu(a)` to stabilize to exactly `r` at finite aperture.

## 5. Adversarial checks

- **No eigenvector convergence is assumed.** Individual negative eigenfunctions may change or move outward with `a`. The theorem concerns only the maximal dimension of negative subspaces.
- **No uniform finite-aperture bound is manufactured.** `PL-278` gives finiteness separately for each `a`; `PL-281` says that unbounded global index forces those finite indices to become unbounded.
- **No zero count is inferred.** The theorem does not convert `kappa_c` into the number of off-line zeros. That is a separate arithmetic/spectral problem.
- **No contradiction with drifting truncations.** The common-support argument is special to this nested support exhaustion. It says nothing about a nonnested Galerkin or Fourier truncation in which the relevant trial spaces change in another way.
- **No source-specific positivity.** The identity is true for any quadratic form on a nested union of form domains. Rational primes enter only through the actual Weil form whose index is being exhausted.
- **The finite-dimensional hypothesis is essential to the common-window step.** An infinite-dimensional subspace of the union need not be contained in one `D_a`. The theorem handles an infinite global index by finding arbitrarily large finite-dimensional negative subspaces, each with its own finite aperture.

## 6. Novelty / literature audit

The mathematical engine is standard: negative Morse index as a variational dimension, exhaustion by nested form domains, finite-dimensional compactness, and form-core approximation. No novelty is claimed for this functional-analytic lemma. A targeted audit around the Weil quadratic form, localized Suzuki operators, Morse index, negative squares, and support exhaustion did not locate a source stating this exact canonical support-localization identity; absence of such a hit is not used as evidence of novelty.

Bombieri's finite-defect stabilization remains the relevant arithmetic prior art and is already recorded in `PL-260`. Suzuki's 2026 realization supplies the canonical localized completed Weil form and the Sobolev/compact-resolvent framework already recorded in `research/prime_lattice/SOURCES.md`. No new external source is required for the present derivation.

The durable project-level contribution is the **exhaustion bridge** between `PL-260` and `PL-280`: support localization cannot lose a finite global negative defect through drift. The unresolved arithmetic problem is to determine the value of that global index, or more strongly to prove it is zero.

## Consequence for the line

The current crossing-prevention program can now separate two questions cleanly. There is no additional compactness problem about whether a global compact-support negative defect eventually becomes visible: it must. The live RH-facing problem is source-specific and sign-theoretic—whether the actual completed Weil form ever creates the first negative subspace at all.

Equivalently, if the line succeeds in proving

\[
\nu(a)=0\qquad\text{for every finite }a,
\]

then there is no residual negative direction waiting beyond all finite windows. Conversely, any compact-support violation of Weil positivity occurs at a finite aperture and, by `PL-280`, remains in the Morse-index ledger thereafter. The next useful progress must therefore constrain the actual arithmetic source strongly enough to prevent that first crossing, rather than seek a separate theorem excluding negative-index escape to infinity.

## Sources

- Suzuki, *Weil's quadratic form via the screw function* (2026), already recorded in `research/prime_lattice/SOURCES.md`: canonical localized completed Weil form, Sobolev realization, and self-adjoint compact-resolvent framework.
- Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, already recorded in `research/prime_lattice/SOURCES.md` and analyzed in `PL-260`: finite-defect stabilization for a different Fourier-side truncation.
- `PL-278`: finite negative Morse index at every fixed canonical aperture.
- `PL-279`: canonical fixed-aperture Sobolev form geometry on `H_0^1(-a,a)`.
- `PL-280`: nested domains and monotone nondecreasing localized negative Morse index.
