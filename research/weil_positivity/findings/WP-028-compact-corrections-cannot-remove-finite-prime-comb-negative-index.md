# WP-028 — Compact corrections cannot remove the finite prime comb's negative index

**Status:** `EXACT-DERIVED + CLASSICAL-PERTURBATION + DECISIVE-NEGATIVE` for the finite-rank / compact-correction and finite-codimension quotient escape left open by WP-005, WP-015, and WP-026. The general stability of essential spectrum under compact perturbations is classical Weyl perturbation theory. The Mathia-specific result below is stronger at the compact-window level and is proved directly: as soon as one prime-power shift is active, the exact finite Weil prime operator has an **infinite-dimensional subspace on which its quadratic form is uniformly negative**. Therefore no compact self-adjoint correction — in particular no finite-rank polar term, finite-dimensional cohomological correction, or finite-rank boundary-mode insertion — can make that finite-prime form positive. Likewise, deleting or quotienting only finitely many global modes cannot remove the obstruction.

## 1. Claim

For a compact logarithmic window `[-L,L]`, let

\[
\mathcal A_L
=
\{a_n=\log n:\ n=p^k,\ a_n<2L\},
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}>0.
\]

Extend functions in

\[
H_L=L^2([-L,L])
\]

by zero to `R`, and write `P_L` for restriction back to the window. The exact finite-prime Weil operator from WP-005 is the bounded self-adjoint compression

\[
A_L
=-\sum_{a_n\in\mathcal A_L}
 w_n P_L(\tau_{a_n}+\tau_{-a_n})P_L.
\tag{1}
\]

Its quadratic form is exactly the finite-place contribution

\[
\langle f,A_Lf\rangle
=-2\sum_{a_n\in\mathcal A_L}w_n
\operatorname{Re}\langle f,\tau_{a_n}f\rangle.
\tag{2}
\]

WP-005 proved that this form is indefinite whenever `mathcal A_L` is nonempty. The stronger statement is:

> **Infinite negative-index theorem.** If `mathcal A_L` contains at least one shift `a_*`, then there is a closed infinite-dimensional subspace `M subset H_L` and a constant `c>0` such that
> \[
> \langle f,A_Lf\rangle\le -c\|f\|^2
> \qquad(f\in M).
> \tag{3}
> \]
> In fact one may take `c=w_*`, the Weil weight of any chosen active shift after isolating that shift geometrically.

Consequently, for every compact self-adjoint operator `K` on `H_L`,

\[
\boxed{A_L+K\not\succeq0.}
\tag{4}
\]

And if `Y subset H_L` is any closed subspace of finite codimension, then

\[
\boxed{A_L|_Y\not\succeq0.}
\tag{5}
\]

Thus a finite-dimensional quotient, finite-rank Schur/polar correction, or any other compact after-the-fact repair cannot be the missing sign mechanism. Any successful completion must contribute an **infinite-rank/noncompact global sector before positivity is taken**.

## 2. Exact paired-bump construction of an infinite negative subspace

Fix one active shift

\[
a_*=\log(p^k)<2L,
\qquad
w_*=\frac{\log p}{p^{k/2}}>0.
\]

Because the active set `mathcal A_L` is finite and its shifts are distinct, choose a nonempty open interval

\[
I\subset(-L,L-a_*)
\]

so short that:

1. `I` and `I+a_*` are disjoint;
2. for every active `b != a_*`, neither translation by `+/-b` maps either of the two intervals into the other;
3. no active nonzero shift maps either interval into itself.

This is possible because only finitely many positive distances must be avoided. Concretely, choose the length of `I` smaller than a fixed fraction of

\[
\min\Bigl(
 a_*,
 2L-a_*,
 \min_{b\in\mathcal A_L,\,b\ne a_*}|b-a_*|,
 \min_{b\in\mathcal A_L}b
\Bigr),
\]

with the duplicate occurrence of `a_*` omitted from the relevant minima.

For `u in L^2(I)`, let

\[
f_u=u+\tau_{a_*}u.
\tag{6}
\]

The two summands have disjoint support, so

\[
\|f_u\|^2=2\|u\|^2.
\tag{7}
\]

By the interval separation, every active shift except `a_*` contributes zero to (2). For the selected shift,

\[
\langle f_u,(\tau_{a_*}+\tau_{-a_*})f_u\rangle
=2\|u\|^2.
\tag{8}
\]

Therefore

\[
\boxed{
\langle f_u,A_Lf_u\rangle
=-2w_*\|u\|^2
=-w_*\|f_u\|^2.
}
\tag{9}
\]

The map

\[
u\longmapsto 2^{-1/2}f_u
\]

is an isometry from the infinite-dimensional Hilbert space `L^2(I)` into `H_L`. Its image `M` is closed, infinite-dimensional, and satisfies (3) with `c=w_*` **exactly**.

This strengthens the two-bump sign test of WP-005. The negative direction is not an isolated vector that a low-rank correction might remove. It comes with arbitrary internal degrees of freedom carried by `u`.

## 3. Arbitrary compact corrections fail

Let `K=K^*` be compact on `H_L`. Choose an orthonormal sequence `(f_j)` in the subspace `M` from Section 2. Then

\[
f_j\rightharpoonup0.
\]

Compactness implies

\[
\|Kf_j\|\to0,
\]

and hence

\[
\langle f_j,Kf_j\rangle\to0.
\tag{10}
\]

Combining (9) and (10),

\[
\langle f_j,(A_L+K)f_j\rangle
=-w_*+o(1)<0
\]

for all sufficiently large `j`. Thus (4) follows without invoking any abstract perturbation theorem.

On the full-line Fourier representation the same conclusion is the familiar Weyl-theory picture. The finite comb has continuous multiplier

\[
m_L(t)
=-2\sum_{a_n\in\mathcal A_L}w_n\cos(a_nt),
\]

with

\[
m_L(0)=-2\sum_nw_n<0.
\]

Hence the negative spectral set contains an open neighborhood of zero, so negative spectrum is essential and survives compact perturbations. Classical Weyl theory says precisely that compact self-adjoint perturbations do not change essential spectrum. The compact-window paired-bump proof is useful because it establishes the relevant infinite negative index directly on the actual support-restricted test space, where a bare Fourier-essential-spectrum argument would not by itself be enough.

## 4. Finite-codimension quotients and cohomological mode deletion also fail

Let `Y subset H_L` be closed with finite codimension. Since `M` is infinite-dimensional,

\[
M\cap Y
\]

is still infinite-dimensional. Pick any nonzero `f in M cap Y`. Equation (9) gives

\[
\langle f,A_Lf\rangle=-w_*\|f\|^2<0.
\]

Therefore restricting to `Y`, or equivalently deleting only finitely many orthogonal global modes, cannot make the finite-prime operator positive.

This matters for the cohomological/quotient escape repeatedly left open in earlier findings. A construction of the form

```text
finite prime comb
    -> remove constants / polar states / finitely many cohomological modes
    -> inherit positivity on the quotient
```

cannot work. The negative index is infinite before the archimedean sector is added.

The statement is deliberately about **finite-dimensional** quotients. An infinite-codimension localization/compression, such as a genuine Sonin-type or semilocal projection, lies outside the obstruction and is exactly the sort of operation that could change the operator category rather than merely remove a few bad modes.

## 5. The standard polar sector is too small by itself

On a fixed compact window, the usual pole terms in the Riemann explicit formula are built from finitely many bounded evaluation/Laplace functionals of the test function, schematically

\[
\ell_\pm(f)=\int_{-L}^{L}f(x)e^{\pm x/2}\,dx.
\]

Any quadratic form assembled from finitely many such functionals is represented by a finite-rank operator on `H_L`. Its exact sign and normalization are irrelevant to the present obstruction: finite rank is compact, so Section 3 applies.

Hence the polar correction **cannot by itself** repair the finite prime comb. This is consistent with the compact-window global picture cited in WP-005: where an assembled restricted Weil form is provably positive, the archimedean digamma sector is an infinite-rank operator and participates essentially in the cancellation. The result here isolates the categorical minimum:

\[
\boxed{
\text{prime comb + polar/finite-dimensional correction alone}
\quad\text{cannot be PSD.}
}
\tag{11}
\]

The theorem does **not** say the archimedean sector cannot repair the prime comb. It says that if it does, it must do so through genuinely infinite-dimensional geometry/order, not through a finite number of global counterterm states.

## 6. Relation to WP-026 and WP-015

WP-026 ruled out a different repair mechanism. There the hidden bulk was passive and Schur/Kron reduction could not leave the loopy-Laplacian cone to generate the required negative self-energy. That is a **sign-cone obstruction**.

WP-028 allows the added correction `K` to have arbitrary sign and to be completely noncommuting with the translations. The only hypothesis is compactness. The failure therefore survives far beyond passive networks:

```text
WP-026:
    arbitrary passive bulk complexity
        -> Schur response stays passive
        -> wrong constant-mode sign

WP-028:
    arbitrary signed compact correction
        -> infinite negative subspace survives
        -> no global positivity
```

WP-015 similarly showed that ordinary outgoing DtN continuation on the critical scattering line does not inherit the zero-energy positive form. WP-028 says that replacing the missing boundary mechanism by only finitely many boundary channels cannot solve the finite-prime sign problem either. A surviving boundary construction must carry infinitely many effective degrees of freedom or otherwise be noncompact/singular on the Weil test space.

## 7. Matched controls

Nothing in Sections 2–4 uses primality beyond positivity and discreteness of the chosen shift weights. Replace the active prime powers by any finite set of distinct positive shifts

\[
0<a_1<\cdots<a_N<2L
\]

with positive weights `w_j`. The same interval-isolation argument produces, for each chosen shift, an infinite-dimensional negative subspace for

\[
-\sum_jw_jP_L(\tau_{a_j}+\tau_{-a_j})P_L.
\]

Thus the no-go survives generalized-prime systems, random positive shift combs, and density-matched controls. This is appropriate for an obstruction: it is a structural property of trying to repair an autocorrelation comb with only compact global data, not a hidden arithmetic theorem.

Conversely, this universality prevents overinterpretation. WP-028 does not distinguish the rational primes from matched controls and supplies no RH evidence by itself. Its value is to remove a broad class of apparently plausible **global repair architectures**.

## 8. Prior-art and novelty audit

No novelty is claimed for:

- invariance of essential spectrum under compact self-adjoint perturbations (classical Weyl perturbation theory);
- the fact that a compact operator sends weakly null orthonormal sequences to norm-null sequences;
- finite-rank perturbations as a special case of compact perturbations;
- generic spectral interlacing/index bounds under finite-dimensional changes of boundary conditions.

A modern literature check confirms the standard boundary: Yuming Shi, *Stability of essential spectra of self-adjoint subspaces under compact perturbations*, Journal of Mathematical Analysis and Applications **433** (2016), 832–851, DOI `10.1016/j.jmaa.2015.08.017`, proves essential-spectrum invariance under compact perturbations in the more general setting of self-adjoint linear relations, explicitly including finite-rank perturbations. The operator case used conceptually here is classical and substantially older.

The project-specific content is instead the exact construction (6)–(9): **the compact-window finite Weil prime comb itself has an explicitly embedded `L^2(I)` negative sector with a uniform gap `w_*`.** That observation turns the general perturbation theorem into a sharp Mathia consequence and closes a specific escape route left open after WP-005/WP-026.

This is not another reformulation of zeta or of the zero set. It uses only the finite prime-power shifts and their positive coefficients; no analytic continuation, zeros, RH assumption, or spectral realization of zeros enters the proof.

## 9. Boundary of the obstruction

WP-028 does **not** rule out:

- the genuine archimedean infinite-rank operator participating in the sign theorem;
- an infinite-codimension compression/localization whose range removes or reorganizes the whole negative sector;
- a noncompact or singular boundary response;
- a coupled finite/archimedean bulk formed before the prime comb is separated as (1);
- a relative operator with a separately proved Loewner-order theorem;
- a cohomological construction with infinitely many degrees of freedom and an independent Hodge/intersection sign theorem;
- a change of Hilbert space or base measure for which the compactness/index statement above no longer describes the relevant operation.

These are substantive escapes. In particular, the finding should **not** be quoted as saying that finite-rank terms never matter in the full explicit formula. It says they cannot convert the finite-prime autocorrelation operator into a positive operator because the latter has infinitely many uniformly negative directions.

## 10. Falsification tests and research consequence

The exact claim is falsified if any one of the following fails:

1. for an active shift `a_*`, intervals `I` and `I+a_*` can be isolated from the finite set of other active translations;
2. on `f_u=u+tau_{a_*}u`, every other active shift has zero correlation;
3. the selected shift gives equation (8);
4. therefore equation (9) holds on an isometric copy of `L^2(I)`;
5. a compact operator can remove all negative vectors from such a uniformly negative infinite-dimensional subspace;
6. a finite-codimension subspace can have trivial intersection with that `M`.

Items 1–4 are direct support geometry. Items 5–6 contradict standard Hilbert-space compactness/dimension facts.

The research consequence is a sharper global-category requirement. After WP-027, preserving the signed/oriented Mangoldt selector through finite–archimedean coupling was already necessary. WP-028 now adds:

\[
\boxed{
\text{the coupling that finally creates positivity must be infinite-rank/noncompact
(or change the space) before the sign theorem is applied.}
}
\]

A finite-dimensional polar/cohomological patch cannot carry the burden. The next serious candidate should therefore expose a canonical **infinite-dimensional order structure** — for example an archimedean compression, relative boundary operator, or global cohomological/intersection space — and prove its positivity independently, while retaining the finite Mangoldt cancellation rather than inserting the Weil functional by hand.

## Internal dependencies

- `research/weil_positivity/findings/WP-005-prime-lattice-axis-positivity-does-not-survive-weil-autocorrelation-lift.md`
- `research/weil_positivity/findings/WP-015-prime-flute-dtn-positivity-does-not-survive-critical-scattering-continuation.md`
- `research/weil_positivity/findings/WP-026-passive-kron-reduction-preserves-weil-self-energy-obstruction.md`
- `research/weil_positivity/findings/WP-027-positive-commutator-energy-radializes-the-mangoldt-selector.md`
