# PL-280 — Localized Weil Morse index is one-sided under aperture growth

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PROVED-STRUCTURAL-REDIRECT + NEGATIVE-OBSTRUCTION + PRIOR-ART-AUDITED`

## Claim

Let `q_a` denote the localized completed Weil/Suzuki lower-bounded closed quadratic form at aperture `a>0`, realized on the canonical form domain `D_a` and associated with a self-adjoint compact-resolvent operator `A_a`. Under the natural zero-extension embedding, the localized domains are nested:

\[
0<a<b \quad\Longrightarrow\quad D_a\subset D_b,
\]

and `q_b` restricted to `D_a` is the same global completed Weil form as `q_a`. If

\[
\lambda_1(a)\le \lambda_2(a)\le\cdots
\]

are the ordered min-max eigenvalues of `A_a`, counted with multiplicity, then for every fixed `k`,

\[
\boxed{\lambda_k(b)\le \lambda_k(a)\qquad (0<a<b).}
\]

Consequently the negative Morse index

\[
\nu(a):=\#\{k:\lambda_k(a)<0\}
\]

is nondecreasing with aperture. Once a variational level has crossed below zero, enlarging the arithmetic window cannot make that negative direction disappear. Cross-aperture arithmetic evolution may prevent a crossing from occurring, or may create further negative levels, but it cannot later repair an already negative min-max level.

This is a generic nested-domain consequence of the min-max principle, not a new RH-specific spectral theorem. Its value for the present line is a route restriction: after `PL-278` and `PL-279`, the surviving zeta-specific problem is not a possible late cancellation or healing of negative modes, but the prevention of every forbidden crossing in the first place.

## 1. Variational derivation

For each aperture `a`, compact resolvent and lower semiboundedness give the standard Courant-Fischer characterization

\[
\lambda_k(a)
=
\inf_{\substack{V\subset D_a\\ \dim V=k}}
\ \sup_{0\ne v\in V}
\frac{q_a[v]}{\|v\|^2}.
\]

If `a<b`, every `k`-dimensional trial subspace of `D_a` is also an admissible trial subspace of `D_b`. On such a common subspace, zero extension does not alter the underlying test function and the localized form is simply the restriction of the same completed Weil form, so

\[
q_b[v]=q_a[v],\qquad v\in D_a.
\]

The infimum defining `lambda_k(b)` is therefore taken over a superset of the trial spaces available at aperture `a`. Hence

\[
\lambda_k(b)
\le
\inf_{\substack{V\subset D_a\\ \dim V=k}}
\ \sup_{0\ne v\in V}
\frac{q_b[v]}{\|v\|^2}
=
\lambda_k(a).
\]

No differentiability of eigenvalue branches, continuity in `a`, or perturbative description of individual prime-power activations is required.

## 2. One-sided residual Morse-index ledger

Define the onset aperture of the `k`th ordered level by

\[
a_k:=\inf\{a>0:\lambda_k(a)<0\},
\]

with `a_k=+infinity` if the set is empty. Since `lambda_k(a)` is nonincreasing in `a`, the negativity set of each ordered level is an upper interval: if `lambda_k(a_0)<0`, then

\[
\lambda_k(a)<0\qquad\text{for every }a>a_0.
\]

Because the eigenvalues are ordered at every aperture, the onset thresholds satisfy

\[
a_1\le a_2\le a_3\le\cdots.
\]

Equivalently, `nu(a)` is a one-sided counting process. It can stay fixed or increase as the aperture grows, but cannot decrease.

This sharpens the finite-index conclusion of `PL-278`. There is a finite low/mesoscopic negative sector at every fixed aperture, but its cross-aperture evolution is not an arbitrary finite-dimensional spectral motion: negative index cannot be lost by subsequent source activation. In particular, a scenario in which one prime-power event creates a negative mode and later prime-power events collectively restore positivity is incompatible with the variational ordering of the canonical localized problem.

## 3. Interaction with prime-threshold softness

`PL-279` showed that an individual newly active prime-power atom enters the canonical `H_0^1` form only quadratically in its overlap width. That local softness might suggest that later arithmetic events could compensate an earlier negative excursion. The present monotonicity result rules out that interpretation at the level that matters for positivity.

The source decomposition itself is not termwise monotone, and individual prime-power contributions may have either sign on a chosen vector. Nevertheless, after minimization over the enlarged form domain, every ordered variational level is one-sided. Thus the arithmetic question is more rigid than the behavior of the separate source terms: the completed localized form must avoid producing the first forbidden negative trial subspace at all.

For RH-oriented work this changes the target from tracking signed local shocks to proving a global inequality of the form

\[
q_a[v]\ge0
\qquad\text{for every }a>0\text{ and }v\in D_a,
\]

or an equivalent mechanism that blocks every onset `a_k`. If an off-line zero forces strict negativity at some finite aperture as in `PL-266`, no later aperture can undo that witness in the min-max spectrum.

## 4. Adversarial checks

- **Not monotonicity of individual arithmetic atoms.** The statement concerns ordered min-max levels of the full localized form under nested domains. It does not say that the contribution of a particular `p^m` is monotone in `a` or has a fixed sign.
- **Not eigenbranch tracking.** Eigenvalue crossings and multiplicities may occur. The claim uses ordered variational levels and therefore does not require a canonical labeling of analytic eigenbranches.
- **No continuity claim.** Monotonicity alone does not establish continuity, differentiability, or a Hadamard-type derivative with respect to aperture.
- **No source-specific proof of positivity.** The mechanism is generic spectral theory. It constrains how a zeta-specific proof must work but supplies no arithmetic inequality that excludes the first crossing.
- **No contradiction with local softness.** `PL-279` controls the size of a newly activated prime-power term near its own threshold. Domain enlargement simultaneously creates new trial directions, and the min-max principle concerns the full form rather than the perturbation coefficient alone.
- **Compact-resolvent hypothesis matters for the eigenvalue ledger.** The monotonicity argument can be stated variationally more generally, but the discrete ordered sequence and finite Morse index used here are those already justified for the canonical localized Suzuki completion in `PL-278`.

## 5. Novelty / literature audit

The mathematical engine is the classical Courant-Fischer/min-max principle together with domain monotonicity for nested quadratic-form domains; it is standard operator theory and is not claimed as novel. The 2026 Suzuki operator realization supplies the canonical completed localized Weil form and compact-resolvent setting used by this line. A targeted audit around localized Weil forms, support intervals, Morse index, domain monotonicity, and recent Suzuki/Connes--van Suijlekom operator work did not locate a source presenting this full ordered-level/Morse-index consequence as a new arithmetic theorem; that absence is not used as a novelty claim.

The durable contribution here is therefore a **negative/structural redirect** internal to the research program: it closes the proposed mechanism of cross-aperture healing and converts the residual question into prevention of the first and subsequent zero crossings.

## Consequence for the line

The live frontier after `PL-278`--`PL-280` can be stated more sharply. Generic operator theory already gives compact resolvent, a finite negative sector at every finite aperture, quadratic softness of isolated prime-power activation, and now one-sided persistence of every negative variational level. Therefore a useful prime-lattice mechanism must explain why the actual zeta source keeps all ordered levels nonnegative for every aperture; it cannot rely on later arithmetic cancellation repairing an earlier spectral defect.

The promising observables are consequently those that control **crossing prevention**: coercive inequalities for the completed Weil form, source-specific constraints on the first variational level, or collective arithmetic structure capable of bounding the accumulated low/mesoscopic source before any `lambda_k(a)` reaches zero. Mere signed bookkeeping of later prime-power events is insufficient.

## Sources

- Suzuki, *Weil's quadratic form via the screw function* (2026), as recorded in `research/prime_lattice/SOURCES.md`: canonical localized completed Weil quadratic form and self-adjoint operator framework.
- Classical Courant-Fischer/min-max principle for lower-semibounded closed forms with compact resolvent; used only as standard operator-theoretic prior art.
- `PL-266`: first strict negative threshold is persistent at ground-state level.
- `PL-278`: canonical localized completion has compact resolvent and finite negative index at each finite aperture.
- `PL-279`: isolated prime-power activation is quadratically soft in the canonical Sobolev form topology.
