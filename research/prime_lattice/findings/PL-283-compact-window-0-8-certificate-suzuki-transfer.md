# PL-283 — The compact-window `0.8` certificate transfers to the canonical Suzuki operator

**Evidence:** `LITERATURE (NON-PEER-REVIEWED, COMPUTER-ASSISTED) + DERIVED`

**Status:** `BOUNDED-SUPPORT POSITIVITY FRONTIER + TEST-SPACE BRIDGE + PRIOR-ART SYNTHESIS + NEEDS-INDEPENDENT-CERTIFICATE-REPRODUCTION`

## Claim

The computer-assisted compact-window result recorded as source 58, arXiv:`2608.24827`, reports the unconditional bound

\[
Q_W(f)\ge 8.9\times10^{-18}\,\|f\|_2^2
\]

for every complex test function supported in `[-0.8,0.8]`. Combining that theorem with the already-audited common-form dictionary of `PL-265` and the Suzuki test-space bridge used in `PL-269` gives the corresponding canonical localized operator inequality

\[
\boxed{A_{0.8}\ge 8.9\times10^{-18}I>0.}
\]

Here `A_a` is Suzuki's Friedrichs representative of the completed Weil form localized to `(-a,a)`. Consequently, by the nested-domain min--max monotonicity of `PL-280`,

\[
\boxed{
\lambda_1(a)\ge\lambda_1(0.8)\ge8.9\times10^{-18}
\qquad(0<a\le0.8).
}
\]

Thus any first strict-negative aperture for the canonical support-localized Weil family must satisfy

\[
\boxed{a_->0.8.}
\]

This strictly improves the bounded-support canonical frontier of `PL-282`, whose independent literature source reports positivity only through `a=0.72`. It does **not** provide an aperture-uniform RH mechanism: the new input is a finite-window computer-assisted certificate already present in the literature, and the transfer to `A_a` is an exact restriction/closure argument.

## 1. The lower-bound transfer is in the safe direction

`PL-265` identifies the semilocal/CvS and Suzuki localizations as the same completed Weil quadratic form, with additive support interval `[-a,a]`. Suzuki's symmetric operator has domain `H_0^1(-a,a)`, and its Friedrichs extension is `A_a`; on that Sobolev core,

\[
Q_W^a(v)=Q_W(v)=\langle B_av,v\rangle.
\]

`PL-269` already audited this normalization and test-space dictionary against source 58 when transferring its conditional large-window **upper** bound to Suzuki's operator. For the present lower bound the logical direction is simpler. The external theorem is stated for every complex `f` supported in `[-0.8,0.8]`, so in particular it applies to every

\[
v\in H_0^1(-0.8,0.8).
\]

Hence on the Friedrichs core,

\[
Q_W^{0.8}(v)
\ge
8.9\times10^{-18}\|v\|_2^2.
\]

A uniform lower form bound passes to the closure. Therefore the closed form associated with `A_0.8` has the same lower bound, which is equivalent to

\[
A_{0.8}\ge8.9\times10^{-18}I.
\]

No comparison between two different operators, no Galerkin convergence theorem, and no extrapolation from finitely many trial vectors is used in this transfer. The certificate itself is the external computer-assisted input; Mathia's derived step is only that a lower bound on the larger supported test class restricts to Suzuki's core and survives Friedrichs closure.

Endpoint conventions do not matter here: `[-0.8,0.8]` versus `(-0.8,0.8)` differ only on null endpoints, while `H_0^1` supplies the zero trace required by Suzuki's core.

## 2. The arithmetic window still contains exactly `2,3,4`

At `a=0.8`, the localized prime-power horizon is

\[
\log n<2a=1.6.
\]

Since

\[
4<e^{1.6}<5,
\]

the active von-Mangoldt channels are exactly

\[
n=2,3,4.
\]

In exponent-lattice coordinates these are

\[
e_2,\qquad e_3,\qquad 2e_2.
\]

Thus the improvement from `0.72` to `0.8` does not come from crossing another prime-power activation. It rules out a first negative crossing through almost the entire source-static interval before the next event

\[
a_5=\frac{\log5}{2}\approx0.8047189562.
\]

This is a useful correction to the boundary emphasized in `PL-282`: positivity at `0.72` did not imply positivity until the next prime threshold because the domain and archimedean part continue to evolve between source activations. The source-58 certificate now rules out such a crossing through `0.8`, leaving only the short interval

\[
0.8<a<\frac{\log5}{2}
\]

uncovered before the `5` channel enters.

## 3. Relation to the current first-crossing program

`PL-280` proves that every ordered localized eigenvalue is nonincreasing in aperture. Therefore the positive lower bound at `0.8` propagates backward to every smaller support without any continuity assumption. `PL-281` then says that any eventual global compact-support negative defect must become visible at a finite aperture and remain in the Morse-index ledger.

The present certificate therefore advances a real finite boundary of the first-crossing search, but it does not alter the asymptotic burden. `PL-269` shows that under RH the ground level must eventually decrease to zero, while off RH a finite negative crossing persists. Better finite-window certification alone cannot distinguish those two asymptotic possibilities unless one obtains a source-specific estimate that is uniform in growing aperture.

The same source also supplies a reason not to interpret its finite certificate as a scalable mechanism: the pointwise-envelope method has the Kronecker obstruction analyzed in `PL-045`, with a doubly exponential worst-case frequency threshold. The durable lesson is therefore not that the one-stroke method can be iterated to RH, but that the canonical localized operator is rigorously bounded away from zero substantially deeper into the first nontrivial prime-power regime than `PL-282` alone records.

## 4. Evidence and novelty audit

The numerical lower bound is not a Mathia computation. Source 58 is a recent arXiv preprint and reports a certified finite-matrix/interval-arithmetic proof at `L=0.8`; this Research Watch did not independently reproduce that computation. Accordingly the number `8.9e-18` is preserved as a **non-peer-reviewed computer-assisted literature claim**. The result is falsifiable by independently reconstructing the paper's finite matrix, pointwise tail bound, interval arithmetic, and positive-semidefinite certificate.

The external result itself was already known to this line: `PL-045` mentions the `L=0.8` certificate while studying the distinct prime-Kronecker pointwise barrier, and source 58 in `SOURCES.md` records it explicitly. `PL-282`, however, subsequently made `a=0.72` the canonical bounded-support operator frontier because it analyzed a different AIRR certificate and its Stieltjes hierarchy. The substantive delta here is therefore **not** a novelty claim for positivity at `0.8`; it is the exact synthesis showing that source 58's full supported-function inequality transfers directly to the same Suzuki `A_a` used by `PL-278`--`PL-282`, and hence dominates the `0.72` frontier.

Public indexes for arXiv:`2608.24827` currently disagree on mutable author/title metadata across versions, while the repository's source 58 pins the v2 record. The mathematical statement used here is identified by the arXiv number, version-pinned repository source, support `[-0.8,0.8]`, and displayed lower bound; no claim depends on the mutable author display.

No new `SOURCES.md` entry is required because the exact paper is already source 58.

## 5. Adversarial checks and boundaries

- **Superclass-to-core direction.** The source lower bound is stated for all complex supported test functions, so restricting it to Suzuki's `H_0^1` core is valid. This is not an inference from a finite-dimensional trial subspace to the continuum.
- **Closure.** A uniform quadratic-form lower bound on a Friedrichs core persists under form closure. The operator inequality therefore follows without spectral convergence assumptions.
- **Normalization.** `PL-265` and the source-58 bridge already audited in `PL-269` identify the same completed Weil form and the same additive support radius. No factor-of-two rescaling of the aperture is introduced here.
- **Complex/parity sector.** The source explicitly states the final certificate for arbitrary complex functions of support `1.6`; no even-only bound is being promoted to the full operator without justification.
- **Strict cutoff convention.** At `a=0.8`, neither `5` nor any other new prime power lies at the endpoint, so `<` versus `<=` does not affect the active set `2,3,4`.
- **Tiny margin.** The reported lower bound is only `8.9e-18`; ordinary floating-point agreement would not validate it. The certificate should remain literature-level until independently reproduced.
- **No next-prime theorem.** The finding proves positivity only through `0.8`. It does not fill `(0.8,log(5)/2]`, and it does not imply that a crossing must coincide with a prime-power activation.
- **No RH conclusion.** A positive finite support window, however strong the certificate, does not prove the all-aperture Weil criterion.

## Consequence for the line

The canonical finite-aperture frontier should now be read as

\[
\boxed{
A_a>0\quad\text{for every }0<a\le0.8
}
\]

conditional only on the correctness of the reported source-58 computer-assisted certificate, with the transfer to Suzuki's operator exact. The first possible negative crossing is pushed beyond `0.8`, while the next prime-power event remains at `log(5)/2`.

The live RH-facing question is unchanged but sharper: obtain an **aperture-uniform, source-specific crossing-prevention inequality** for the completed rational-prime Weil form. Finite-window certification has now reached almost to the next source event, so further progress is most valuable if it explains why the positive margin survives growing arithmetic complexity rather than merely extending the numerical aperture by another isolated amount.

## Sources

- arXiv:`2608.24827`, version-pinned as source 58 in `research/prime_lattice/SOURCES.md`: computer-assisted lower bound `Q_W(f)>=8.9e-18 ||f||_2^2` for arbitrary complex `f` supported in `[-0.8,0.8]`, plus the pointwise-envelope/Kronecker scalability barrier.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2`, source 56: canonical localized closed form, `H_0^1(-a,a)` core, and Friedrichs operator `A_a`.
- `PL-265`: exact CvS/Suzuki common-form and support-radius dictionary.
- `PL-269`: audited source-58/Suzuki test-space bridge and large-aperture ground-level order parameter.
- `PL-280`: nested-domain eigenvalue monotonicity.
- `PL-281`: negative-index exhaustion.
- `PL-282`: prior bounded-support canonical frontier at `a=0.72` from a different external certificate.
