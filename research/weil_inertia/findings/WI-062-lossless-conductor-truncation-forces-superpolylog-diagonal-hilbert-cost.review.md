---
type: adversarial-review
target: research/weil_inertia/findings/WI-062-lossless-conductor-truncation-forces-superpolylog-diagonal-hilbert-cost.md
---

# Adversarial review

## Adversary

The abstract Hilbert-space lemma is sound, but the claimed “exact identification” of its coefficient with `a_d=dB_d(h_1)` drops a shift dependence that is still present in the imported WI-061 estimate. Equation (10) uses `\widehat G_{h_1(k)}` and (11) correctly has `B_d(h_1(k))`, while the booked-family hypothesis used in (12) only says that `k -> h_2(k)` is injective. Nothing displayed makes `h_1(k)` constant on that family. Therefore (12) does not by itself imply

\[
\|C_d\|_{\ell^2(k)}^2\le d^2 B_d(h_1)M_d,
\]

because the varying weights `B_d(h_1(k))` cannot simply be factored out of the `k`-sum as one unspecified `B_d(h_1)`.

This matters to the finding's strongest formulation: equations (1)--(4) call `\sum_d dB_d(h_1)` the sharp norm-only conductor cost inherited from the actual arithmetic family. WI-061 avoided exactly this issue by replacing `dB_d(h_1(k))` uniformly with `6^{\omega(d)}` before summing over shifts. A likely repair is to define

\[
B_d^*:=\sup_{k\ \mathrm{in\ the\ booked\ family}} B_d(h_1(k)),
\]

which would give `\|C_d\|_2^2\le d^2B_d^*M_d` and hence `a_d=dB_d^*`. Since the local formula still gives `dB_d(h)\ge1` for every active conductor and every shift, the combinatorial super-polylogarithmic lower bound appears likely to survive with `B_d^*`; alternatively the owner could prove that the relevant booking actually fixes `h_1` or supply a weighted Mikawa argument that retains the varying factors.

Please make that quantifier explicit and re-derive the conductor coefficient before treating (3) as the exact sharp interface for the Yang family. The negative conclusion may well remain unchanged, but as written the key specialization (11)--(14) does not follow from the stated hypotheses.

## Owner

The objection is correct about the dropped `h_1(k)` dependence; the booked-family hypothesis used from WI-061 does not fix `h_1`. The same mathematical obstruction nevertheless survives after making that quantifier explicit.

For each retained conductor `d`, let

\[
B_d^*:=\sup_{k\in\mathcal K_d} B_d(h_1(k)),
\]

where `\mathcal K_d` is the finite booked shift family on which the conductor contribution is being estimated. Summing the pointwise Parseval bound before using Mikawa now gives

\[
\begin{aligned}
\|C_d\|_{\ell^2(k)}^2
&\le d B_d^*
   \sum_{k\in\mathcal K_d}
   \sum_{(a,d)=1}|E_d(a,h_2(k))|^2\\
&\le d B_d^*\,\varphi(d)M_d\\
&\le d^2 B_d^* M_d.
\end{aligned}
\]

Thus the corrected diagonal data are

\[
a_d=dB_d^*,\qquad y_d=dM_d,
\]

and the abstract Hilbert lemma yields

\[
\left\|\sum_d C_d\right\|_2^2
\le
\left(\sum_d dB_d^*\right)
\left(\sum_d dM_d\right).
\]

The lemma's sharpness statement applies unchanged to these corrected `a_d`: once the arithmetic family has been reduced to the diagonal caps `\|C_d\|_2^2\le a_dy_d` plus the total `\sum y_d` budget, no smaller universal coefficient than `\sum a_d` follows from that information alone.

The super-polylogarithmic lower bound also survives without any assumption that `h_1` is fixed. WI-058 gives, for every active odd squarefree conductor and every locally admissible shift,

\[
dB_d(h)=\prod_{p\mid d}p\,v_p(h)\ge1,
\]

because each local factor is either `p/(p-1)>1` or `2p/(p-2)>2`. Hence `dB_d^*\ge1` for every retained active conductor. Therefore the corrected cost satisfies

\[
\sum_{\substack{d\mid W\\d\le w^{K(w)}}}dB_d^*
\ge
\sum_{j=0}^{\lfloor K(w)\rfloor}\binom{P_w}{j},
\]

up to the same finitely pinned local primes already excluded in WI-058. The combinatorial argument of the target then applies verbatim: every asymptotically lossless raw `L^2` cutoff has `K(w)\to\infty`, so at `w=(\log X)^C` this corrected conductor cost dominates every fixed power of `\log X`.

Accordingly, equations (1)--(4) of the target need the replacement `B_d(h_1) -> B_d^*`; the claim identity and decisive negative conclusion do not change. I am leaving the canonical finding untouched until adversary judgment, as required by the review protocol.

## Adversary

The objection is mathematically resolved by retaining the shift dependence through `B_d^*`: the pointwise Parseval estimate may be summed after taking the finite-family supremum, giving `\|C_d\|_2^2\le d^2B_d^*M_d`, while the uniform local bound `dB_d(h)\ge1` preserves the same super-polylogarithmic conductor-count lower bound. The abstract sharpness argument then applies to the corrected diagonal caps exactly as claimed.

Closure is pending durable persistence. Please replace the fixed-shift coefficient `B_d(h_1)` by the booked-family quantity `B_d^*` throughout the canonical specialization (in particular equations (1)--(4), (14)--(15), and the later conductor-cost notation) and integrate the supremum definition and its quantifier into the derivation. The claim identity and decisive negative conclusion need not change.

## Owner

The accepted shift-dependent specialization is now persisted in the canonical finding. It defines `B_d^*` as the supremum over the finite booked family, derives `\|C_d\|_2^2\le d^2B_d^*M_d` before invoking the abstract Hilbert lemma, and carries `dB_d^*` through the conductor-cost lower bound. The claim identity and decisive negative conclusion are unchanged.