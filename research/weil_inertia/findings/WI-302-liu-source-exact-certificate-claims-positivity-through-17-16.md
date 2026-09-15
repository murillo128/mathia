# WI-302 — Liu's source-exact certificate claims Weil positivity through half-width 17/16

**Status:** `PRIOR-ART-REDIRECT + RECENT-PREPRINT + AUTHOR-CERTIFIED-COMPUTATIONAL + NEEDS-INDEPENDENT-REPLAY`.

A fresh 14 September 2026 manuscript by Vincent Liu, released publicly on 15 September with a frozen reproduction package, claims unconditional computer-assisted coercivity of the classical Weil quadratic form on two fixed complex test-function windows:

\[
Q(f)\ge 2^{-151}\|f\|_2^2
\qquad
\bigl(f\in C_c^\infty((-1,1);\mathbb C)\bigr),
\tag{1}
\]

and, more importantly for the present line,

\[
\boxed{
Q(f)\ge 2^{-49162}\|f\|_2^2
\qquad
\bigl(f\in C_c^\infty((-17/16,17/16);\mathbb C)\bigr).
}
\tag{2}
\]

The half-width `17/16=1.0625` is strictly larger than the independently replayed `0.8` window recorded in WI-300 and crosses the first new arithmetic threshold beyond the unit window:

\[
\frac{\log 8}{2}=1.03972077\ldots
<\frac{17}{16}
<\frac{\log 9}{2}=1.09861228\ldots .
\tag{3}
\]

Accordingly, the claimed larger-window certificate retains exactly the active prime powers

\[
2,3,4,5,7,8,
\]

while `9` remains outside the support. The method is materially relevant to the current source-side frontier because it does not obtain the larger window by discarding the newly active arithmetic or by checking only a finite compression. It keeps the full prime source through `8`, proves a quantitative Fourier-band complement estimate, retains a positive rank-two tail contribution, separates finite/complement/cross terms by a block-Schur estimate, and reduces the remaining finite sign problem to exact residual certificates for two real symmetric integer matrices of order `224`.

This is **not yet established Mathia evidence at the level of WI-300**. The public release explicitly states `EXTERNAL_REPRODUCTION = NOT_YET_COMPLETED`. The frozen package contains author-side reconstruction and verification routes, exact certificates, manifests and source hashes, but Mathia has not replayed them independently and has not re-audited every analytic inequality in the manuscript. Equations (1)--(2) must therefore remain literature claims until that gate is discharged.

## 1. Exact theorem and normalization in the submitted source

The frozen manuscript defines, for

\[
\mathcal D_L=C_c^\infty((-L,L);\mathbb C),
\]

\[
F_f(z)=\int_{\mathbb R}f(u)e^{-izu}\,du,
\qquad
H_f(x)=\operatorname{Re}\int_{\mathbb R}f(v+x)\overline{f(v)}\,dv,
\]

and the classical Weil form

\[
Q(f)=\mathcal P(f)
+\frac1{2\pi}\int_{\mathbb R}A(t)|F_f(t)|^2\,dt
-\sum_{n\ge2}\frac{2\Lambda(n)}{\sqrt n}H_f(\log n),
\tag{4}
\]

with

\[
\mathcal P(f)=2\operatorname{Re}\left(F_f(i/2)\overline{F_f(-i/2)}\right),
\qquad
A(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi.
\tag{5}
\]

The manuscript explicitly states that no reality assumption on `f`, no RH assumption and no vanishing of the pole term are imposed. Its zeros-side identity is

\[
Q(f)=\sum_\rho m_\rho
F_f(\gamma_\rho)\overline{F_f(\overline{\gamma_\rho})},
\qquad
\gamma_\rho=(\rho-1/2)/i.
\tag{6}
\]

Thus the object is the same classical Weil-form object relevant to this line, rather than a positivity statement for a modified finite matrix. The paper itself compares its normalization with Connes--Consani and Zhu. A line-local use through Suzuki's localized ground-state notation should nevertheless retain an explicit normalization/dictionary check when the computational theorem is independently replayed; the present finding does not silently promote that dictionary to a new verified theorem.

For Theorem B the source writes `L=17/16`, `Omega=256`, decomposes

\[
Q(f)=\langle f,(M+K)f\rangle+T_{\rm tail}(f),
\tag{7}
\]

and proves, as analytic inputs to the certificate,

\[
\frac{9617}{10400}I\preceq M\preceq\frac{63183}{10400}I,
\qquad
T_{\rm tail}(f)\ge2^{-49162}\|f\|^2+\langle f,Uf\rangle,
\tag{8}
\]

where `U` is a positive rank-two operator built from the first two normalized Legendre modes after the band-complement operator. The finite Legendre space uses orders `0,...,447`; parity leaves two order-224 real symmetric matrices. The final author-side exact check has the form

\[
2^{-b_s}K_s
=2^{-1024}F_sF_s^*+2^{-480}I+E_s,
\qquad
\max_i\sum_j |(E_s)_{ij}|<2^{-481},
\tag{9}
\]

for both sectors. This is a finite exact-residual closure after analytic approximation and tail estimates, not a floating-point eigenvalue claim.

## 2. Evidence and provenance boundary

The public frozen repository is `luciferyu666/certified-weil-positivity`, source commit

`b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`,

release `v1.0-mcom-submission`. Its README identifies the exact 24-page submitted manuscript by SHA-256

`91126eee6ceb5315a4a40a4d4b2f34d058a71432ae18a8aaf47146f71abf418e`

and the 634,659,625-byte reproduction archive by SHA-256

`7f8e47d265326cbfa4da95197c98bc226fe6cbfd8a22e6896955c18d8cdb376d`.

The release records Mathematics of Computation submission `260914-LiuVincent`, but **no journal acceptance and no external independent reproduction**. The reproduction guide distinguishes Theorem B's clean `FULL_REBUILD` + `FAST_VERIFY` path from Theorem A's retained-proposal verification path and explicitly warns that archive integrity checks are not mathematical verification. Historical internal labels in the frozen data are not external replay evidence.

The correct evidence interpretation is therefore:

- the formulas, theorem statements, constants, support thresholds and certificate architecture above are directly present in the frozen submitted source;
- the package is unusually well pinned and exposes a concrete independent-replay route;
- the mathematical truth of the computer-assisted theorem has **not** yet been independently established by Mathia or another external reproducer located in this audit.

No numerical claim from (1) or (2) is used here to strengthen an established simple-zero proportion.

## 3. Consequence for the current `weil_inertia` frontier

WI-300 independently replayed Zhu's positive half-width `0.8` certificate and therefore may be used as established computer-assisted evidence inside this line. Liu's claim would, after independent replay and normalization audit, move that verified compact-positive aperture from

\[
0.8\quad\text{to}\quad 17/16.
\]

For Suzuki's monotone localized ground-state profile, the immediate exact consequence would then be

\[
\lambda_{17/16}>0
\quad\Longrightarrow\quad
\boxed{a_*>17/16}
\tag{10}
\]

for any hypothetical first nonpositive aperture `a_*` under RH failure. Equation (10) is recorded only as the **post-replay line-local deduction**, not as a currently established theorem.

This does not materially strengthen WI-301's already aperture-independent exclusion of the completely screened one-signed class: that branch was closed using the verified `0.8` theorem plus rearrangement. The new radius matters instead for the branches that survive WI-301 — sign-changing modes, partial screening, and first-crossing configurations whose contradiction depends on how far genuine compact-window positivity has been certified.

The method also redirects how a larger-window certificate should be sought. Liu's manuscript proves a specific negative result for a tail-dropping localization: beyond

\[
L>\frac{\log8}{2},
\]

its normalized high-frequency defect tends to

\[
\frac1{16}-\frac{\log2}{2\sqrt2}< -\frac18,
\tag{11}
\]

and no fixed compact correction repairs that particular comparison. This is not a no-go for the full Weil form. It is a no-go for **dropping the positive tail information** precisely at the first new prime-power threshold. The successful claimed `17/16` architecture instead keeps two positive tail directions. That is directly aligned with this line's instruction to kill weak inertia/kernel refinements quickly: any continuation of compact positivity past `log8/2` should preserve source-exact arithmetic and enough high-frequency tail structure rather than rely on a scalar truncated comparison that (11) already obstructs.

## 4. Prior-art and novelty audit

A targeted audit of the current `weil_inertia` corpus and recent commits found no prior `WI` finding, source anchor or commit naming Vincent Liu, the `17/16` window, or this source-exact block-Schur certificate; `WI-302` was unused at the publication gate. The nearest local result is WI-300, which concerns Zhu's independently replayed `0.8` certificate, and WI-301, which uses that result to close a one-signed complete-screening class. The present claim identity is therefore a **new prior-art redirect**, not a rediscovery of those findings.

No originality is claimed for Liu's mathematics by Mathia. The finding's contribution is to pin the fresh primary source, state its exact evidence level, identify which already-closed branch it does *not* improve, and isolate the surviving line-local consequences that become available if the public Theorem B package survives independent replay.

### Primary sources

- Vincent Liu, **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, submitted manuscript dated 14 September 2026; public dissemination 15 September 2026. Frozen source and reproduction package: https://github.com/luciferyu666/certified-weil-positivity, commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`, release `v1.0-mcom-submission`.
- Frozen submitted source, `frozen-source/publication/manuscript.tex`, especially the normalization, Theorems A--B, block-Schur certificate and Obstruction Theorem.
- Frozen reproduction instructions, `README.md` and `REPRODUCIBILITY.md`, which explicitly record `EXTERNAL_REPRODUCTION = NOT_YET_COMPLETED` and distinguish archive-integrity checks from mathematical verification.

### Verification gate

Do not upgrade (2) to established line evidence until an independent replay checks the frozen archive identity, the Theorem B source-to-certificate reconstruction, both exact residual matrices, the analytic band-complement/tail inequalities, the legal-domain transfer, and the normalization dictionary to the localized `lambda_L` notation. A successful replay would make `17/16` the new verified compact-window aperture available to the surviving first-crossing/signed-screening program; a failure should be persisted as a correction rather than silently retaining the author-side claim.
