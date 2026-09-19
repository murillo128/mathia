# WI-303 — Finite-rank tail rank is noncanonical; the compact-endpoint obstruction requires noncompact tail retention

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

WI-302 isolated a structural question suggested by Vincent Liu's unreplayed `L=17/16` certificate: after the tail-dropped compact localization fails beyond `log 8 / 2`, is the positive rank-two term used in the claimed block-Schur certificate a mathematically necessary or minimal tail invariant? The answer is **no at the structural level**. The rank-two term is one optional finite-rank Loewner minorant of a stronger positive tail operator. Its rank is a certificate-design choice, not an invariant forced by the post-threshold obstruction.

The source-exact distinction is instead between retaining a **noncompact positive tail supplier** and trying to repair the tail-dropped comparison by a fixed compact operator. Liu's own obstruction theorem rules out the latter after the threshold. The rank-two term, being finite rank and hence compact, cannot by itself be what evades that obstruction.

This finding does **not** upgrade Liu's `17/16` positivity claim: the `N=448` finite certificate and the analytic transfer remain at the `NEEDS-INDEPENDENT-REPLAY` evidence level of WI-302.

## 1. Exact finite-rank minorant lemma

Let `S=S^* >= 0` be a bounded positive operator on a Hilbert space and let

\[
V:\mathbb C^r\to\mathcal H
\]

have finite rank. Assume

\[
G:=V^*SV>0.
\]

Then

\[
\boxed{
0\preceq S V G^{-1}V^*S\preceq S.
}
\tag{1}
\]

Indeed, with

\[
W=S^{1/2}VG^{-1/2}
\]

one has `W^*W=I`, so `WW^*` is an orthogonal projection and hence `0 <= WW^* <= I`. Congruence by `S^{1/2}` gives (1).

For one trial vector `v` with `\langle v,Sv\rangle>0`, (1) becomes

\[
\boxed{
S\succeq
\frac{|Sv\rangle\langle Sv|}{\langle v,Sv\rangle}.
}
\tag{2}
\]

For several trial vectors the full Gram inverse in (1) is the exact finite-dimensional statement. If the trial vectors are mutually `S`-orthogonal, the Gram matrix is diagonal and the rank-one minorants add. This is classical positive-operator/shorting machinery; no novelty is claimed for (1)--(2). Anderson--Trapp's shorted-operator framework is a natural classical reference.

## 2. Application to Liu's retained tail

At the pinned source commit used in WI-302, Liu first proves the stronger operator lower bound

\[
T_{\rm tail}\succeq C\,(I-B_{\rm band}),
\qquad C=\frac{123}{1280}.
\tag{3}
\]

The source fixes

\[
\delta=2^{-49158},
\qquad
\tau=2^{-49162},
\]

and writes

\[
S:=I-B_{\rm band}-\delta I\succeq0,
\qquad
I-B_{\rm band}=\delta I+S.
\tag{4}
\]

For the first two normalized Legendre/parity modes `v_0,v_1`, it defines

\[
h_j=Sv_j,
\qquad
e_j=\langle v_j,(I-B_{\rm band})v_j\rangle,
\]

so that

\[
\langle v_j,Sv_j\rangle=e_j-\delta.
\tag{5}
\]

Parity gives the required `S`-orthogonality. Applying (2) simultaneously to the two modes gives

\[
S\succeq
\frac{|h_0\rangle\langle h_0|}{e_0-\delta}
+
\frac{|h_1\rangle\langle h_1|}{e_1-\delta}.
\tag{6}
\]

The manuscript and its exact scalar checker verify the strict rational inequalities

\[
81(e_0-\delta)<C,
\qquad
27(e_1-\delta)<C,
\qquad
C\delta>\tau,
\tag{7}
\]

and therefore obtain

\[
T_{\rm tail}
\succeq C\delta I+CS
\succeq
\tau I+81|h_0\rangle\langle h_0|+27|h_1\rangle\langle h_1|.
\tag{8}
\]

Equation (8) shows exactly what the rank-two term is: a deliberately under-filled finite-dimensional minorant extracted from the stronger operator `CS`. It is not a canonical decomposition of the tail.

In particular, deleting either positive summand in (8) preserves a valid source-exact lower bound. Deleting both preserves

\[
\boxed{T_{\rm tail}\succeq\tau I.}
\tag{9}
\]

More generally, (1) extracts a valid rank-`r` minorant from any finite collection of trial directions for which the Gram matrix is nonsingular. Hence the source supplies valid finite-rank extractions of rank `0`, `1`, `2`, and higher rank. Nothing in the exact tail inequality singles out rank two as a minimal structural invariant.

This does **not** say that the particular `N=448` final matrix stays positive after deleting one or both rank-one terms. That is a package-specific finite-certificate question and still requires an independent replay if it is to be used mathematically. It says only that rank two is not forced by source exactness or by the operator structure of the retained tail.

## 3. Why this does not contradict the compact-endpoint obstruction

The obstruction recorded in WI-302 concerns a different operation: first drop the relevant positive tail information in the localized comparison, then ask whether a fixed compact self-adjoint correction `K_c` can restore positivity once

\[
2L>\log 8.
\]

The source proves that this cannot work. Its high-frequency translates retain a strictly negative limiting defect while every compact correction vanishes on those translates. Consequently **no finite-rank correction can repair that tail-dropped architecture**, because every finite-rank operator is compact.

That observation actually rules out interpreting the rank-two term as the structural cure. The rank-two term in (8) is itself compact. What Liu retains before finite-dimensional extraction is the noncompact positive operator

\[
C(I-B_{\rm band})=C\delta I+CS.
\tag{10}
\]

For the time-band limiting operator used in the source, `B_band` is compact, so (10) contains an identity component and is noncompact. Even the scalar baseline `tau I` in (8) is noncompact. The obstruction therefore separates two logically different questions:

- **structural:** a tail-dropped comparison past the threshold cannot be rescued by any fixed compact correction;
- **certificate design:** once a noncompact/source-exact tail supplier is retained, one may extract whichever finite-dimensional positive minorants are useful for the Schur certificate.

The first statement is a genuine post-threshold barrier. The rank of the optional extraction in the second statement is not.

A further caution is important. Equation (9) does not imply that the tiny scalar `tau I` alone repairs the high-frequency defect in the obstruction theorem; the successful source decomposition and the obstructed tail-dropped comparison are not being identified here. The exact conclusion is only that the source's rank-two extraction is noncanonical, while the obstruction itself can only be evaded by retaining noncompact information or by changing the architecture.

## 4. Consequence for the `weil_inertia` program

The active clue generated from WI-302 asked for a rank-`<=1` impossibility, a rank-`<=1` source-exact counterconstruction, or a representation theorem showing that the rank-two term is merely one realization of a more invariant positive-tail object. Equations (1)--(10) settle that clue in the third sense, and more strongly provide source-exact rank-`<=1` lower bounds immediately.

The useful invariant is therefore not `rank = 2`. It is the availability of a source-exact **noncompact positive complement operator** whose finite-dimensional shadows can be chosen to fit the certificate. Future attempts to push compact-window positivity should not spend effort proving minimality of Liu's two selected Legendre directions. The mathematically relevant tasks are instead to:

1. independently replay and audit the claimed `17/16` certificate before using its positivity conclusion;
2. understand how much of `C(I-B_band)` (or an alternative noncompact tail supplier) must be retained to obtain a robust Schur margin;
3. if seeking a stronger aperture, optimize the trial subspace/minorant only as a finite-certificate design problem, not as a structural rank theorem.

This is a decisive negative for the rank-minimality route, but a positive redirect toward tail-preserving operator inequalities.

## 5. Prior-art and novelty audit

The operator inequality (1) is classical. It is a direct Bessel/projection argument and sits naturally in the theory of shorted positive operators and generalized Schur complements; see W. N. Anderson Jr. and G. E. Trapp, **Shorted Operators II**, *SIAM Journal on Applied Mathematics* 28(1) (1975), 60--71, DOI `10.1137/0128007`. No originality is claimed for that lemma.

The source-side formulas (3)--(8), including the constants `C=123/1280`, `81`, `27`, `delta=2^-49158`, `tau=2^-49162`, the vectors `h_0,h_1`, and the inequalities in (7), are taken directly from Vincent Liu's frozen submitted source and exact scalar checker at commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`. The source uses these terms to build its finite certificate; it does not assert that rank two is necessary or optimal.

A targeted audit of the current `weil_inertia` findings and active clue found no earlier durable result making the distinction proved here. WI-302 records the architecture and its evidence boundary but leaves rank minimality open. The present Mathia contribution is therefore the **diagnosis** obtained by combining the source-exact tail inequality, the classical finite-rank minorant lemma, and the source's own compact-repair obstruction: finite-rank extraction is optional, whereas noncompact tail retention is the structural distinction relevant to the barrier. No priority claim is made beyond that line-local deduction.

### Primary sources

- Vincent Liu, **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, frozen submitted source in `luciferyu666/certified-weil-positivity`, commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`, especially the tail-complement lower bound, rank-two extraction, exact scalar checker, and Obstruction Theorem.
- W. N. Anderson Jr. and G. E. Trapp, **Shorted Operators II**, *SIAM Journal on Applied Mathematics* 28(1) (1975), 60--71, DOI `10.1137/0128007`.

### Validation boundary

The derivation of (1)--(2) is exact operator algebra. Equations (3)--(8) were rechecked against Liu's pinned manuscript source and the self-contained exact-rational `reproduction/scalar.py`, not inferred from an informal summary. The scalar checker itself has no numerical data inputs and verifies the relevant constants with Python `Fraction`/integer arithmetic, but the full author-supplied `N=448` source-to-certificate reconstruction was **not** independently executed here. WI-302's numerical theorem claim therefore remains unreplayed and cannot be promoted to established Mathia evidence.