# WI-300 — the L=0.8 compact-window certificate would kill complete one-signed screening

**Status:** `PRIOR-ART-REDIRECT + RECENT-PREPRINT + COMPUTATIONAL-CERTIFICATE-NEEDS-INDEPENDENT-REPLAY + EXACT-DERIVED-CONDITIONAL`.

A recent compact-window Weil-positivity preprint materially changes the live first-crossing gate left by WI-298--WI-299. Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law*, arXiv:2608.24827v2 (revised 2 September 2026), reports a certified full-window inequality

\[
\boxed{
Q(f)\ge 8.9\times10^{-18}\,\|f\|_2^2
\qquad
\text{for every complex }f\text{ supported in }[-0.8,0.8].
}
\tag{1}
\]

The theorem surface is the same compactly supported Weil quadratic form used in Suzuki's localized operator. Consequently, **if the published v2 certificate is independently replayed and validated**, then in the notation of WI-238

\[
\boxed{
\lambda_{0.8}\ge 8.9\times10^{-18}>0.
}
\tag{2}
\]

WI-238 gives monotonicity of the localized ground-state profile and defines, under RH failure, the first crossing

\[
a_*:=\inf\{a>0:\lambda_a\le0\}.
\]

Equation (2) would force

\[
\boxed{a_*>0.8.}
\tag{3}
\]

But WI-298 proves that a hypothetical first-crossing null mode which is both one-signed and completely prime-power screened must satisfy

\[
\boxed{
a_*\le r_2:=\frac{\log2}{2}=0.346573590\ldots .
}
\tag{4}
\]

Since `r_2<0.8`, (3) and (4) are incompatible. Thus a successful independent replay of Zhu's `L=0.8` certificate would immediately eliminate the **entire one-signed complete-screening first-crossing branch**. It would do so without needing to finish the much narrower endpoint certificate `lambda_{r_2}>0` pursued after WI-299.

This is a prior-art redirect, not an unconditional Mathia theorem yet. The analytic reduction is explicit in the v2 manuscript, but the decisive lower bound is computer-assisted and has not been independently replayed inside Mathia. Until that replay is complete, (2)--(4) are a conditional consequence, not established evidence that the branch is actually closed.

## 1. Exact dictionary to Suzuki's localized ground state

Suzuki's 2026 operator paper defines the closed localized Weil form `Q_W^a` on functions supported in `(-a,a)` and its attained ground-state value

\[
\lambda_a
=\inf_{0\ne v}
\frac{Q_W^a(v)}{\|v\|_2^2}.
\tag{5}
\]

On compactly supported smooth functions his zeros-side definition is

\[
Q_W(v_1,v_2)
=\sum_{\gamma}m_\gamma
\widehat v_1(\gamma)
\overline{\widehat v_2(\bar\gamma)},
\tag{6}
\]

and `Q_W^a` is the corresponding closed restriction to the aperture. This is the same Bombieri/Weil quadratic functional represented by the geometric side of the explicit formula.

Zhu starts from the same Weil form. For compactly supported `f`, with `g=f\star\widetilde f`, the manuscript writes

\[
Q(f)
=\sum_\rho
\widehat g\!\left(\frac{\rho-1/2}{i}\right),
\tag{7}
\]

and uses the Bombieri normalization of the geometric explicit formula. Under the standard Fourier dictionary, (7) is the diagonal form (6). The v2 parity argument extends its certified even-sector lower bound to all real odd functions and then to arbitrary complex `f` by real/imaginary decomposition. Therefore its Corollary 6.3 is exactly the theorem surface needed to lower-bound Suzuki's unrestricted localized Rayleigh infimum at `a=0.8`; there is no missing parity restriction in the implication to (2).

Primary sources:

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), especially the definition of `Q_W^a`, the self-adjoint operator `A_a`, and the ground-state value `lambda_a`: https://arxiv.org/abs/2606.09096.
- Xuefeng Zhu, **Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law**, arXiv:2608.24827v2, revised 2 September 2026: https://arxiv.org/abs/2608.24827v2.

## 2. What the v2 certificate actually claims

For `supp f subset [-L,L]`, Zhu rewrites the geometric side as

\[
Q(f)
=2F(i/2)^2
+\frac1{2\pi}\int_{\mathbb R}|F(t)|^2\Psi_L(t)\,dt,
\tag{8}
\]

with

\[
\Psi_L(t)
=\Re\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi
-\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n).
\tag{9}
\]

Write

\[
A_L:=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}.
\]

The manuscript proves a one-stroke lower reduction: after choosing `T^sharp` with a positive tail floor `beta^*`, the infinite form is bounded below by

\[
R(f)
=2F(i/2)^2
+\frac1\pi\int_0^{T^\sharp}
(\Psi_L(t)-\beta^*)|F(t)|^2\,dt
+\beta^*\|f\|_2^2.
\tag{10}
\]

In a normalized Legendre basis, the remaining head is finite-dimensional up to an explicitly bounded super-exponential tail. At `L=0.8` the reported primary certificate uses

\[
T^\sharp=200,
\qquad
N=200\ \text{even Legendre modes},
\qquad
\beta^*=0.5134\ldots,
\tag{11}
\]

with 50-digit arithmetic. The paper reports Bernstein-ellipse quadrature error below `10^-42`, head/tail and coupling errors below `10^-100`, and a verified Cholesky residual at shift `8.9e-18` with remainder below `10^-50`. A second computation at `T^sharp=150` reportedly certifies the weaker positive floor `1.2e-18`.

The odd sector is treated separately and is reported to satisfy

\[
Q(f)\ge 8.2065\times10^{-15}\|f\|_2^2
\]

for real odd `f`. The manuscript then obtains (1) for arbitrary complex functions. These are stronger statements than the even-only inequality needed for many compact-window applications and remove a possible dictionary loophole in the implication to Suzuki's `lambda_a`.

The manuscript also gives a certified variational upper bound

\[
\lambda^*(0.8)\le2.27\times10^{-17},
\]

so its claimed lower floor lies in a narrow positive interval rather than being separated from the observed window minimum by many orders of magnitude. This upper bound is not needed for the branch-elimination implication.

## 3. Why this supersedes the live `r_2` gate for the screened branch

WI-298 is an exact source-side structural theorem. It says that if the **first** Suzuki crossing mode is nonnegative and completely screened by all prime-power translations, symmetric decreasing rearrangement produces a nonpositive test supported already at the first-prime aperture:

\[
Q_W^{r_2}(v^*)\le0.
\]

Hence such a branch requires `a_*<=r_2`. WI-299 then showed that the smooth-kernel tail estimate needed by a separate finite-mode architecture reaches all the way to `r_2`; the only remaining task in that architecture was the low-mode interval-Schur certificate on the narrow interval above `69/200`.

The new prior art changes that priority. To refute the screened branch one does not need positivity exactly at `r_2`. Any certified positive aperture strictly larger than `r_2` suffices, because `lambda_a` is nonincreasing in `a`: positivity at `0.8` implies positivity at every smaller aperture and therefore forbids a first crossing at or below `r_2`.

Thus, conditional on independent certification of (1), the logical chain is simply

\[
\lambda_{0.8}>0
\Longrightarrow
a_*>0.8
\Longrightarrow
a_*>r_2,
\]

whereas complete one-signed screening gives `a_*<=r_2`. This is substantially stronger than the earlier public `FP-0.35` candidate audited in WI-259--WI-262: `0.8` is far beyond the first-prime threshold, and Zhu's reduction is a different certificate architecture rather than a repair of the defective FP-0.35 checker.

The endpoint work of WI-299 is not mathematically invalidated. It remains useful as an independent finite-scale route and as a way to understand the first-prime transition. It is simply no longer the shortest verification target for eliminating this particular branch if the `L=0.8` certificate survives replay.

## 4. Evidence boundary: this is not yet imported as an unconditional theorem

The v2 manuscript calls Theorem 1.2 a certified unconditional result and describes concrete interval/error-control ingredients. That is materially stronger provenance than a floating-point experiment. Nevertheless it is a fresh unrefereed computer-assisted preprint, and Mathia has not yet independently reconstructed its finite matrix, quadrature enclosure, tail/coupling bounds, or verified-Cholesky step.

This distinction is especially important because the paper itself records a correction between drafts: an earlier exploratory support-`2.38` calculation used an incorrect prime-comb mass and is withdrawn in v2. The current v2 claim is only the support-`1.6` theorem above. The explicit correction is positive evidence of self-audit, but it is also a reason not to collapse `author-certified` into `independently established`.

Accordingly, this finding does **not** assert unconditionally that `lambda_0.8>0`, does not close the screened branch yet, and does not upgrade WI-238/WI-298 to RH. Its exact unconditional content is the logical implication:

\[
\boxed{
\text{valid Zhu v2 }L=0.8\text{ certificate}
\Longrightarrow
\text{no one-signed completely screened first-crossing null mode}.
}
\tag{12}
\]

The implication uses only the already established localized-Weil dictionary, WI-238 monotonicity, and WI-298.

## 5. The pointwise-envelope barrier prevents overinterpreting the result

Zhu also proves a barrier internal to the certificate architecture. With

\[
T_1(L)=2\pi e^{A_L},
\]

the one-stroke reduction requires `T^sharp>T_1(L)`. The prime-comb supremum is exactly `A_L`, so no uniform pointwise majorant of that comb can lower this threshold. By the prime number theorem,

\[
A_L=(4+o(1))e^L,
\]

and the required matrix dimension therefore grows doubly exponentially with `L`.

This is not a no-go for Weil positivity itself, only for this pointwise-envelope certificate class. It is nevertheless directly relevant to the line mandate: even if the `L=0.8` computation is correct, repeatedly extending the same construction to arbitrarily large aperture is not a credible route to RH without new arithmetic information controlling phase alignment.

For the current screened branch, however, no large-`L` iteration is needed. WI-298 has already converted the branch into a **finite threshold contradiction**, so one validated certificate at any aperture above `r_2` is enough.

## 6. Prior-art and novelty assessment

All of the compact-window lower-bound architecture, the `L=0.8` numerical constants, the one-stroke reduction, the parity extension, and the pointwise-envelope barrier belong to Zhu's preprint. No Mathia novelty is claimed for those statements.

The Mathia contribution recorded here is narrower and line-specific: integrating this new prior art with the exact first-crossing logic of WI-238 and the rearrangement theorem WI-298. That combination shows that the certificate, if independently validated, has a much stronger consequence for the current `weil_inertia` program than merely extending a known compact-support positivity range: it would **close an entire structural branch of possible RH failure** already isolated by the line.

A targeted audit of the current line sources found no prior anchor to arXiv:2608.24827, and the current frontier after WI-299 still treated `lambda_{r_2}>0` as the live finite positivity gate. The present finding therefore changes the verification priority rather than rediscovering a stored local result.

## 7. Decisive audit test

The next evidence-changing test is an **independent replay of the v2 `L=0.8` lower certificate**, not another optimization of the first-prime endpoint. A successful replay must establish all of the following against the current v2 source and artifacts:

1. the geometric quadratic form and Fourier normalization agree with the Bombieri/Suzuki localized `Q_W^a` used in WI-238;
2. the pointwise envelope and `beta^*` tail inequality are rigorous on the stated domains;
3. the finite Legendre head at `L=0.8`, `T^sharp=200`, `N=200` encloses the exact matrix entries, including quadrature error;
4. the discarded tail block and head-tail coupling satisfy the claimed explicit bounds;
5. the verified Cholesky/residual argument is genuinely outward or exact enough to imply positive definiteness at the stated shift, rather than merely evaluating an approximate factorization;
6. the odd-sector argument and real/imaginary decomposition really give the all-complex function statement used in (2).

The independent `T^sharp=150` computation is a useful cross-check but is not logically required if the primary `T^sharp=200` certificate is reconstructed from first principles. Conversely, reproducing only a floating-point eigenvalue is insufficient.

If this audit passes, the evidence status of (2) can be upgraded and the branch in (12) becomes unconditionally closed. If it fails, WI-298--WI-299 remain intact and the finite `r_2` certificate architecture remains a live fallback.

## Research consequence

The immediate verification priority for the one-signed complete-screening branch is now external-certificate replay at `L=0.8`. The mathematical reason is unusually clean:

\[
0.8>\frac{\log2}{2},
\]

so a single independently established positive compact window beyond the first-prime aperture contradicts the exact support compression forced by complete screening.

This does not resolve the sign-changing first-crossing branch, does not show that every off-critical zero creates a one-signed screened mode, and does not by itself prove RH. It does, however, convert a fresh finite-window computational theorem candidate into a precise branch-killing test with a binary outcome and no remaining asymptotic step.