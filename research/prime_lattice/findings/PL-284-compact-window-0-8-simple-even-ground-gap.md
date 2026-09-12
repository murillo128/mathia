# PL-284 — The `0.8` compact window has a certified simple even ground state and an explicit spectral gap

**Evidence:** `LITERATURE (NON-PEER-REVIEWED, COMPUTER-ASSISTED) + DERIVED`

**Status:** `FINITE-WINDOW SPECTRAL REFINEMENT + PRIOR-ART TRANSFER + NEEDS-INDEPENDENT-CERTIFICATE-REPRODUCTION`

## Claim

Source 58, arXiv:`2608.24827v2`, proves parity-resolved computer-assisted min--max bounds for the localized completed Weil form at support aperture `a=0.8`. In the paper's even and odd sectors, Theorem 6.2 gives

\[
8.9\times10^{-18}
\le \lambda^{\mathrm{even}}_1
\le 2.523\times10^{-16},
\]

\[
\lambda^{\mathrm{even}}_2\ge2.085\times10^{-12},
\qquad
\lambda^{\mathrm{odd}}_1\ge8.206\times10^{-15}.
\]

Using the exact source-58/Suzuki quadratic-form dictionary already audited in `PL-265`, `PL-269`, and `PL-283`, these bounds transfer to the parity reductions of Suzuki's canonical Friedrichs operator `A_0.8` on `L^2(-0.8,0.8)`. Hence the global ground eigenvalue is the first even eigenvalue, it is simple and even, and

\[
\boxed{
8.9\times10^{-18}
\le \lambda_1(A_{0.8})
\le2.523\times10^{-16}.
}
\]

Moreover the next global eigenvalue satisfies

\[
\boxed{
\lambda_2(A_{0.8})
\ge8.206\times10^{-15},
}
\]

so the spectral gap obeys the explicit lower bound

\[
\boxed{
\lambda_2(A_{0.8})-\lambda_1(A_{0.8})
\ge7.9537\times10^{-15}.
}
\]

This is a finite-window spectral refinement of `PL-283`, not a new proof of the source theorem and not an RH mechanism. The source itself already states the corresponding simple/even conclusion in its compact-window formulation; the substantive Mathia delta is the exact transfer to the canonical Suzuki operator and the resulting global second-eigenvalue and gap bounds in the operator used by the current first-crossing program.

## 1. Parity decomposition transfers with the common quadratic form

The completed localized Weil kernel is invariant under reflection `x -> -x`. Therefore the closed quadratic form and its Friedrichs operator commute with the reflection involution

\[
(Rf)(x)=f(-x),
\]

and

\[
L^2(-0.8,0.8)
=
H_{\mathrm{even}}\oplus H_{\mathrm{odd}}
\]

is a reducing orthogonal decomposition for `A_0.8`. Write the ordered eigenvalues of the two restrictions as

\[
e_1\le e_2\le\cdots,
\qquad
o_1\le o_2\le\cdots.
\]

`PL-265` identifies the CvS/source-58 and Suzuki localizations as the same completed Weil quadratic form at the same additive support radius. `PL-269` audits the test-space normalization, and `PL-283` shows that the source-58 full supported-function lower bound passes to Suzuki's `H_0^1` core and its Friedrichs closure. No additional rescaling, Galerkin-limit assumption, or analytic continuation step is introduced here. Restricting the same form to its reflection eigenspaces identifies the source's parity min--max levels with `e_j` and `o_j` for the canonical operator.

Thus Theorem 6.2 of source 58 supplies

\[
8.9\times10^{-18}\le e_1\le2.523\times10^{-16},
\]

\[
e_2\ge2.085\times10^{-12},
\qquad
o_1\ge8.206\times10^{-15}.
\]

The lower bound on `e_1` is compatible with, and refines by parity, the global positivity transferred in `PL-283`.

## 2. The global ground state is isolated, simple, and even

Because the full spectrum is the multiset union of the even and odd spectra,

\[
\lambda_1(A_{0.8})=\min(e_1,o_1).
\]

The certified inequalities give

\[
e_1\le2.523\times10^{-16}
<8.206\times10^{-15}
\le o_1,
\]

so the global ground state lies in the even sector. The second even level is also separated:

\[
e_1\le2.523\times10^{-16}
<2.085\times10^{-12}
\le e_2.
\]

Therefore `e_1` has multiplicity one within the even sector and no odd eigenvalue shares its value. Consequently

\[
\boxed{\lambda_1(A_{0.8})=e_1\text{ is simple and even}.}
\]

The second global eigenvalue must be

\[
\lambda_2(A_{0.8})=\min(e_2,o_1),
\]

hence

\[
\lambda_2(A_{0.8})
\ge
\min(2.085\times10^{-12},8.206\times10^{-15})
=
8.206\times10^{-15}.
\]

Combining this with the certified upper bound on the ground level yields

\[
\lambda_2-\lambda_1
\ge
8.206\times10^{-15}-2.523\times10^{-16}
=
7.9537\times10^{-15}.
\]

The gap estimate uses the **upper** certificate for `e_1`; using only the positive lower bound from `PL-283` would not justify it.

## 3. Consequence for Suzuki's finite-window spectral construction

Suzuki's localized theory uses the Friedrichs ground level `lambda_a` as the lower spectral threshold. The source-58 transfer now gives more at the explicit non-infinitesimal aperture `a=0.8`: the unshifted parameter `lambda=0` lies strictly below the ground level,

\[
0<8.9\times10^{-18}\le\lambda_1(A_{0.8}),
\]

and the ground level is isolated from the rest of the spectrum by at least `7.9537e-15` under the source certificate.

This verifies, at `a=0.8`, a concrete finite-window regime in which the canonical localized operator has a nondegenerate even ground state and a positive spectral separation. It can be used as a stable local base point for perturbative or continuation questions in aperture, provided any such argument separately controls how the parity-reduced eigenvalues move with `a`.

It does **not** imply that the ground state remains simple, even, or uniformly gapped for all larger apertures. Ordered eigenvalue monotonicity from `PL-280` controls levels under domain enlargement, but by itself does not preserve a quantitative gap between two independently moving levels.

## 4. Evidence and novelty audit

The parity-resolved inequalities are not Mathia computations. They are taken from Theorem 6.2 of source 58, a recent non-peer-reviewed arXiv preprint whose `v2` provenance is pinned in `research/prime_lattice/SOURCES.md`. This Research Watch inspected the load-bearing theorem in the primary paper but did not independently reconstruct its interval-arithmetic certificate. All numerical constants therefore remain **literature-level computer-assisted evidence** until independently reproduced.

The source theorem itself already concludes that the compact-window ground state at `L=0.8` is simple and even. Accordingly there is **no novelty claim** for that qualitative fact. Suzuki independently proves simplicity/evenness only in a sufficiently small-aperture regime in his canonical operator framework. The line-local contribution here is narrower: because `PL-265`, `PL-269`, and `PL-283` have already established that source 58 and Suzuki use the same localized completed Weil form with the same aperture normalization, the parity-resolved source bounds can be read as spectral bounds for the canonical `A_0.8`. The explicit global lower bound for `lambda_2(A_0.8)` and the `7.9537e-15` gap are immediate but useful consequences of that transfer.

No new `SOURCES.md` entry is required: source 58 already records arXiv:`2608.24827v2`, and source 56 already records Suzuki's localized operator theory.

## 5. Adversarial checks and boundaries

- **No parity promotion without reduction.** The full-operator conclusion uses reflection invariance and the reducing decomposition into even and odd subspaces; it does not infer a global statement from an even-sector computation alone.
- **Ground simplicity uses both sectors.** `e_2>e_1` excludes even multiplicity, while `o_1>e_1` excludes an odd degeneracy at the same eigenvalue.
- **Gap arithmetic.** The lower bound `7.9537e-15` is obtained from the certified lower bound on the second global level and the certified upper bound on the first, not from two lower bounds.
- **Common-form normalization.** The transfer relies on the exact support-radius and quadratic-form dictionary already audited in `PL-265`, `PL-269`, and `PL-283`; no new factor-of-two convention is introduced.
- **Certificate status.** The tiny values make ordinary floating-point reproduction inadequate. The numerical inequalities remain contingent on the source's rigorous computer-assisted certificate.
- **No all-aperture gap.** Neither min--max monotonicity nor positivity through `0.8` gives a uniform lower bound on `lambda_2-lambda_1` as `a` grows.
- **No characteristic-function convergence claim.** Suzuki's finite-dimensional characteristic-function approximation is a separate issue; the present spectral transfer does not prove its conjectural continuum convergence.
- **No RH conclusion.** A simple positive ground state with an explicit gap at one finite aperture does not establish Weil positivity for all compact supports.

## Consequence for the line

`PL-283` established that the canonical localized operator is strictly positive through aperture `0.8`. The stronger local spectral picture at the endpoint is now

\[
\boxed{
0<8.9\times10^{-18}
\le\lambda_1(A_{0.8})
\le2.523\times10^{-16}
<8.206\times10^{-15}
\le\lambda_2(A_{0.8}),
}
\]

with a **simple even** ground state and a certified gap of at least `7.9537e-15`, conditional only on the correctness of source 58's computer-assisted proof.

This does not change the global first-crossing target: the missing mechanism is still an aperture-uniform, source-specific prevention of negative crossing for the rational-prime completed Weil form. What it does provide is a rigorously isolated canonical ground state very near the next prime-power activation at `log(5)/2`, giving a sharper finite-window boundary condition for any future perturbative analysis of that first crossing.

## Sources

- arXiv:`2608.24827v2`, source 58 in `research/prime_lattice/SOURCES.md`, Theorem 6.2: certified parity-resolved min--max bounds at `L=0.8`, including the simple/even ground-state conclusion.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096`, source 56: canonical localized closed form, Friedrichs operator `A_a`, and finite-window spectral framework.
- `PL-265`: exact CvS/Suzuki common-form and support-radius dictionary.
- `PL-269`: audited source-58/Suzuki test-space bridge.
- `PL-280`: nested-domain ordered-eigenvalue monotonicity.
- `PL-283`: transfer of source 58's global `0.8` positivity certificate to `A_0.8`.