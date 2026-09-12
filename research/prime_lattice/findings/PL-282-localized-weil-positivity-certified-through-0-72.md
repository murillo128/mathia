# PL-282 — A computer-assisted certificate pushes localized Weil positivity through `a=0.72`; fixed-support strict positivity has a terminating Stieltjes hierarchy

**Evidence:** `LITERATURE (NON-PEER-REVIEWED, COMPUTER-ASSISTED) + DERIVED`

**Status:** `BOUNDED-SUPPORT POSITIVITY + PRIOR-ART / FRONTIER REDIRECT + NEEDS-INDEPENDENT-CERTIFICATE-REPRODUCTION`

## Claim

A 2026 computer-assisted preprint by Lluis Eriksson reports a rigorous interval-arithmetic certificate for the canonical localized Weil operator in the Suzuki normalization at aperture

\[
a=0.72,
\]

namely

\[
\boxed{A_{0.72}\ge 5.890\times 10^{-17}I>0.}
\]

The source supplies a public reproducibility bundle and a claim ledger, but it is an AIRR founder-owned pilot record and explicitly does **not** claim independent peer review or independent frontier-model verification. This Research Watch inspected the paper, the published source/reproducibility bundle, the claim ledger, and the release-verification metadata, but did **not** rerun the expensive Arb certificate. Accordingly, the numerical lower bound is recorded here as a literature claim whose source integrity is auditable, not as an independently reproduced Mathia computation.

Conditional on the correctness of that certificate, `PL-280` immediately gives

\[
\boxed{\lambda_1(a)>0\qquad(0<a\le 0.72),}
\]

for the lowest localized eigenvalue, because the localized domains are nested and `lambda_1(a)` is nonincreasing with aperture. Hence any first strict-negative crossing in the canonical support-localized Weil family must satisfy

\[
\boxed{a_->0.72.}
\]

This is source-sensitive progress rather than a prime-free window result: at `a=0.72`, the prime-power support condition `log n<2a=1.44` activates exactly

\[
n=2,3,4,
\]

since `4<e^{1.44}<5`. Thus, conditional on the reported certificate, strict localized Weil positivity survives the complete activation of the first three prime-power source channels.

The same paper supplies a second structural result relevant to the current line. At every **fixed** aperture, its Gauss--Stieltjes lower approximants `R_m` to the archimedean boundary potential form an increasing hierarchy of finite lower operators whose eigenvalues monotonically converge upward to those of the exact localized operator. In particular, for fixed `a`, strict positivity of the exact localized operator is equivalent to strict positivity of some finite stage of this hierarchy. Therefore fixed-support strict positivity has a terminating finite certificate mechanism. The remaining RH-facing difficulty is not certification at a prescribed finite aperture but controlling the source-side arithmetic as the aperture grows and new prime powers enter.

## 1. Exact source geometry at `a=0.72`

In the localized Suzuki/Weil normalization audited in `PL-265`--`PL-281`, the arithmetic term has the exact form

\[
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(f(\log n)+f(-\log n)\bigr),
\]

with only `log n<2a` active on aperture `a`. At `a=0.72`, therefore,

\[
2a=1.44,
\qquad
\log 2,\log 3,\log 4<1.44<\log 5,
\]

so the source contains precisely the channels `2,3,4`.

After scaling the support interval to `(-1,1)`, Eriksson writes the dominant archimedean operator as

\[
L=A_2+V,
\]

where

\[
(A_2w)(x)=\frac12\int_{-1}^1\frac{w(x)-w(y)}{|x-y|}\,dy,
\qquad
V(x)=-\frac12\log(1-x^2),
\]

and the Legendre basis diagonalizes the singular part via

\[
A_2P_n=H_nP_n.
\]

The active source translations occur at normalized displacements

\[
\frac{\log2}{a},\qquad
\frac{\log3}{a},\qquad
\frac{\log4}{a}.
\]

The paper partitions the interval at the induced translation/reflection breakpoints. For `a=0.72` this gives thirteen subintervals whose translation graph decomposes into components of sizes `7`, `4`, and `2`. Local Legendre bases make each exact translation an identity block, and reflection symmetry splits the finite certificate into two parity blocks of size `78 x 78` at the chosen truncation. These are implementation details of the reported certificate, not independent arithmetic structure claimed by Mathia.

## 2. Fixed-support Gauss--Stieltjes hierarchy

The more reusable part of the paper is analytic. The boundary potential admits an exact increasing Gauss--Stieltjes lower hierarchy

\[
0<R_1<R_2<\cdots<V,
\]

with explicit positive-square remainders and positive rank-one/Schur increments. If

\[
L_{a,m}=A_2+R_m+B_a
\]

is the lower operator obtained by replacing the exact potential `V` with `R_m` while retaining the exact finite arithmetic source `B_a`, then for every fixed aperture `a` the ordered eigenvalues of `L_{a,m}` increase to those of the exact localized operator `L_a` as `m to infinity`.

The resulting fixed-support completeness statement is

\[
\boxed{
L_a>0
\quad\Longleftrightarrow\quad
\exists m<\infty:\ L_{a,m}>0.
}
\]

The forward implication is the important one: a strictly positive exact operator has a positive finite lower certificate at a sufficiently deep Stieltjes stage. The reverse implication follows because each `L_{a,m}` is a lower operator for `L_a`.

This does **not** decide the semidefinite boundary case in which the exact ground-state eigenvalue is zero. It also gives no aperture-uniform rate for the depth `m` or for the positive spectral margin as `a to infinity`. Those omissions are essential: the hierarchy is a complete certificate system at each fixed support, not a uniform RH proof.

The paper supplements this hierarchy with a mode-sensitive high-tail Schur estimate. Schematically, if the positive tail satisfies

\[
D\ge\sum_n d_n P_n,
\]

then the Schur correction obeys

\[
BD^{-1}B^*
\le
\sum_n\frac{(BP_n)(BP_n)^*}{d_n}.
\]

Banding the tail can make this majorant close to the exact tail contribution with only slowly growing numbers of bands. This is useful certification technology, but by itself it is not the missing arithmetic mechanism: the hard issue remains the sign as the source gains new prime-power atoms.

## 3. Derived consequence from localized monotonicity

`PL-280` proved that the canonical localized domains are nested and that the ordered min--max eigenvalues are nonincreasing in `a`. Therefore, if the reported Eriksson certificate is correct,

\[
\lambda_1(0.72)>0
\]

implies

\[
\lambda_1(a)\ge\lambda_1(0.72)>0
\qquad(0<a\le0.72).
\]

Consequently the first strict-negative aperture, if it exists, lies to the right of `0.72`.

No stronger threshold statement follows. In particular, one must **not** infer that the first crossing can occur only when the next prime `5` activates at

\[
a=\frac{\log5}{2}.
\]

Between source thresholds the domain and archimedean part still vary continuously, and the lowest eigenvalue may decrease. A crossing could therefore occur in the open interval

\[
0.72<a<\frac{\log5}{2}
\]

without any new discrete prime-power activation.

The source-sensitive content is instead that the already-active channels `2,3,4` have been accommodated simultaneously by a reported positive lower certificate through `a=0.72`. This advances the bounded-support frontier beyond the first prime-free/first-source thresholds considered in earlier localized work.

## 4. Relation to the prime-exponent lattice

The source term is concentrated exactly on the prime-power axis rays

\[
v(p^k)=k e_p,
\]

at energies

\[
\log(p^k)=k\log p.
\]

Increasing `a` exposes these atoms in the energy order `log n<2a`. The Eriksson certificate therefore tests a genuinely arithmetic stage of the exponent-lattice filtration: it survives simultaneous contributions from `e_2`, `e_3`, and `2e_2`.

At the same time, the result reinforces the redirect already isolated by `PL-278`--`PL-281`. Generic operator completion, compactness, finite Morse index, and nested-domain monotonicity are not the bottleneck. Even fixed-support strict positivity now comes with a finite certificate hierarchy. What remains unproved is a **source-side mechanism uniform in aperture** that prevents the first variational crossing while infinitely many prime-power atoms enter.

A successful continuation of this line therefore needs to control the arithmetic source as a growing structured family, not merely improve finite-window diagonalization. Plausible targets include source stratifications or Schur-complement estimates whose sign margin survives the cumulative growth of the active von-Mangoldt comb. Such a theorem would have to use more than the fact that each finite window is, in principle, certifiable.

## 5. Prior-art and novelty audit

The paper is very recent. Targeted searches by exact title, author, the bound `A_0.72`, localized Weil positivity, and the Stieltjes hierarchy found the AIRR record and its public repository bundle but no independent journal/arXiv version, citation, review, or third-party verification as of this audit. Absence of a search hit is not evidence of novelty; the result is treated simply as current external literature.

The AIRR record is unusually explicit about provenance. It supplies the canonical PDF hash

`e4fd12894f2d15bd503370a016f259aa0e2f619810ba309108ca6a1150a02935`,

a source/reproducibility tree, a claim ledger, interval-arithmetic scripts, certificate JSON, and release-verification documents. The record also explicitly states that its acceptance/source-integrity checks are **not peer review** and do not constitute independent mathematical validation. The author is the AIRR founder-editor for this pilot record. These facts materially lower the evidentiary status compared with a refereed theorem and are part of the finding, not incidental metadata.

This Research Watch checked the published formulas, the operator normalization, the prime-power cutoff, the stated Stieltjes monotonicity/completeness mechanism, and the presence and internal organization of the reproducibility bundle. It did **not** independently rerun the high-precision Arb computation that produces the numerical positive margin. The durable Mathia claim is therefore split deliberately:

- the implication from a valid `a=0.72` certificate to positivity for all smaller apertures is `EXACT-DERIVED` from `PL-280`;
- the existence and numerical value of the `a=0.72` certificate are `LITERATURE (NON-PEER-REVIEWED, COMPUTER-ASSISTED)` pending independent reproduction;
- the fixed-support Stieltjes hierarchy is recorded as a literature theorem/derivation from the paper, not as a Mathia novelty claim.

## 6. Adversarial checks and failure modes

- **No independent certificate reproduction.** Source integrity and published reproducibility metadata are not the same as rerunning the Arb proof. If an independent execution fails to reproduce the interval bound, the numerical frontier claim must be withdrawn or corrected.
- **Tiny positive margin.** The reported lower bound is about `5.89e-17`; ordinary floating-point agreement would be inadequate. The claim depends on validated interval arithmetic and exact bookkeeping of the source/Schur tails.
- **No support-uniform theorem.** The finite Stieltjes hierarchy is complete for fixed `a` but supplies no uniform depth or positive gap as `a` grows.
- **No conclusion at a zero ground state.** Monotone lower approximants can certify strict positivity, but the stated hierarchy does not by itself decide an exact semidefinite endpoint.
- **No next-prime barrier.** Positivity at `0.72` does not force positivity until `log(5)/2`.
- **No RH conclusion.** A bounded interval of verified localized positivity, however far beyond the first source thresholds, does not exclude a later negative direction. By `PL-280`, one such first crossing would persist in the Morse-index ledger.
- **No novelty claim for the certification machinery.** The finite-window partition, parity split, Legendre representation, Stieltjes lower bounds, and Schur complements are attributed to the source.

## 7. Decisive audit test

The numerical part of this finding is falsifiable by an independent reconstruction of the canonical `a=0.72` operator and replay of the published interval certificate from the source bundle. The audit must verify at minimum the normalization dictionary to Suzuki's localized Weil form, the active source list `2,3,4`, exact translation/reflection bookkeeping, the Stieltjes lower bound, all Schur-tail enclosures, and the final interval lower bound. A failure at any of those steps invalidates the claimed certified aperture while leaving the exact monotonic implication from `PL-280` untouched.

The analytic hierarchy can be audited independently of the `0.72` computation by checking the positive remainder formula for `V-R_m`, monotonicity `R_m<R_{m+1}<V`, and the fixed-support spectral convergence that yields the finite-certificate equivalence for strict positivity.

## Consequence for the line

The bounded-support problem is now sharper. Conditional on the reported computer-assisted certificate, the canonical completed Weil form remains strictly positive through `a=0.72`, after the prime-power axis atoms `2,3,4` have all become active. More importantly, the fixed-support analytic problem is not open-ended: strict positivity at a prescribed aperture admits a terminating lower-certificate hierarchy.

Accordingly, further work should not treat better finite-window numerics as the missing RH mechanism. The live target is to obtain an **aperture-uniform arithmetic control**—or a source-side induction/stratification strong enough to keep the finite Schur sign positive—as the von-Mangoldt axis comb grows without bound. That target is exactly the first-crossing prevention problem left by `PL-280` and the global exhaustion statement `PL-281`.

## Sources

- Lluis Eriksson, “Certified Localized Weil Positivity Through Support 0.72: Multiband Schur Complements and a Complete Stieltjes Hierarchy,” AIRR record `ARR-2026-7XT7AB8WJP9QPTGT`, version 1, published 13 August 2026. https://airr.science/papers/ARR-2026-7XT7AB8WJP9QPTGT/ . Public source/reproducibility bundle: https://github.com/arr-research/arr-research.github.io/tree/main/papers/2026/08/7X/ARR-2026-7XT7AB8WJP9QPTGT . Non-peer-reviewed founder-owned pilot record; numerical certificate not independently rerun in this Research Watch.
- Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2 (2026), already recorded in `research/prime_lattice/SOURCES.md`: canonical localized operator/form normalization.
- `PL-265`: dictionary between the semilocal Weil cutoff and Suzuki aperture, including `log n<2a` source activation.
- `PL-280`: nested localized domains and nonincreasing ordered eigenvalues / nondecreasing Morse index.
- `PL-281`: exhaustion of the global compact-support negative index by localized Morse indices.
