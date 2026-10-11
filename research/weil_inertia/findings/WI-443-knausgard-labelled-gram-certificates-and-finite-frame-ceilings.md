# WI-443 — Knausgård's labelled Gram certificates improve global zero proportions but expose sharp finite-frame ceilings

**Status:** PRIMARY-SOURCE-AUDIT + LITERATURE+DERIVED + EXACT-COUNT-COROLLARIES + RECENT-UNREFEREED-PREPRINT + COMPUTATIONAL-CERTIFICATE + INDEPENDENT-REPLAY-PENDING + PRIOR-ART-REDIRECT + NON-RH + NO-NOVELTY-CLAIM

Source: Kristian Muri Knausgård, *More than 83.9% of the zeros of the Riemann zeta function are distinct and more than 67.35% are simple and on the critical line*, arXiv:2610.08965v1 (6 October 2026), https://arxiv.org/abs/2610.08965. Primary proof/certificate repository (revision inspected): https://github.com/kristianmk/839/tree/b280d51bef5ab32b3280b0955d040085ed522d59. Theorems 1.1–1.5, Lemma 2.5, Theorem 2.6, Propositions 7.2–7.3, Corollary 7.9, and Section 8.

Related local evidence: WI-013 (fixed Montgomery–Taylor pressure-bridge ceiling), WI-027 (an earlier independently unreplayed seven-point candidate), WI-172 (independently kernel-replayed Montgomery–Taylor four-point result), WI-226/WI-442 (Wang's *short-interval* certificates). Those are not interchangeable theorem interfaces.

## 1. Precise primary-source claims

Write N(T) for nontrivial zeta zeros with positive ordinate at most T, counted with multiplicity; Nd(T) for distinct zeros regardless of their horizontal position; Ns(T) for globally simple zeros; N0s(T) for simple zeros *on* Re(s)=1/2; and NsOr0(T) for zeros that are simple or on that line, counted with multiplicity. The source claims the following *unconditional* asymptotic statements:

\[
\begin{aligned}
\liminf_{T\to\infty}\frac{N_d(T)}{N(T)}
 &\ge q:=\frac{1645064}{1960733}=0.839004596750\ldots,\\
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
 &\ge s:=\frac{1669159}{2478195}=0.673538200182\ldots,\\
\liminf_{T\to\infty}\frac{N_{s\cup0}(T)}{N(T)}
 &\ge u:=\frac{50652159}{56956375}=0.889315006441\ldots .
\end{aligned}
\tag{1}
\]

These correspond respectively to Theorems 1.1, 1.3, and 1.5 of the **unrefereed source**, whose analytic/formal and finite-computation trust boundaries are separated below. The second number concerns simple critical-line zeros; the first and third do not assert that distinct or simple zeros lie on the line.

Two exact count consequences can be checked without replaying any numerical certificate. For each zero location of multiplicity m, its contribution to the simple count is at least twice its contribution to distinct count minus its multiplicity: for m=1 equality holds (1=2-1), and for m>=2 one has 0>=2-m. Thus

\[
N_s(T)\ge 2N_d(T)-N(T),\quad
\liminf N_s/N\ge 2q-1
=\frac{1329395}{1960733}=0.678009193501\ldots .
\tag{2}
\]

Likewise NsOr0 counts every zero except the off-critical multiple zeros. The source's Theorem 1.5 therefore implies

\[
\limsup_{T\to\infty}
\frac{N_{\mathrm{off},\,m\ge2}(T)}{N(T)}
\le 1-u=\frac{6304216}{56956375}
=0.110684993559\ldots .
\tag{3}
\]

Equation (3) counts the omitted off-line multiple-zero mass **with multiplicity**. It gives no bound on the off-line *simple* mass beyond the independent bound supplied by N0s/N, and in particular no individual-zero exclusion.

## 2. Where the numerical improvement actually enters

The source stays within the unconditional support-one Montgomery pair-correlation/Weil-inertia interface. For an even probability window f supported on [-1/2,1/2], with K=Fourier(f), its trace/energy resource is

\[
\operatorname{tr}A=N,\qquad
\operatorname{tr}A^2=(C(f)+o(1))N,\quad
C(f)=\int f^2+\iint |x-y|f(x)f(y)\,dx\,dy .
\tag{4}
\]

The full Weil-form operator A may be indefinite because of off-line zero pairs. The nonnegative Gram pair energy used in the certificate is restricted to the permitted critical-line subset, and clipping is retained where required. In a subset of critical-line points y_i of multiplicity d_i in {1,2}, the source couples the otherwise diagonal multiplicity expense with

\[
\sum_i d_i^2
+\sum_{i\ne j}d_i d_j K(y_i-y_j)^2 .
\tag{5}
\]

For the **distinct-zero** certificate it matches close points, bounds the Gram spectrum on the remaining 17/20-separated set by a Selberg/large-sieve majorant, and uses a seven-consecutive-point inequality with labels 1 and 2 and clipping level c=67/20. The **simple-critical** theorem instead uses a different ten-cosine window, an eight-point inequality without multiplicity labels, a different majorant/separation regime, and clipping level c=2. These are two distinct certificate problems, not one universal improved trace inequality.

The exact local-to-global bookkeeping is especially useful. The source's seven-point correction is a coboundary: on consecutive frames it has the form

\[
\Phi(g_0,\ldots,g_4;d_0,\ldots,d_5)
-\Phi(g_1,\ldots,g_5;d_1,\ldots,d_6).
\tag{6}
\]

On summing frames, each interior state cancels with its successor. The total storage penalty is at most osc(Phi), an endpoint constant independent of the number of frames (Lemma 2.5), not a loss proportional to N(T). The actual reward coefficients x1,x2, the gap tariff, the Gram clipping/majorant hypotheses, and the finite continuum inequality must *all* hold for the gain to reach (1). Mere telescoping is classical and is not by itself a new zeta theorem.

The six-cosine distinctness window pays slightly more in C(f) than the Montgomery–Taylor minimizer but extracts considerably more off-diagonal multiplicity-weighted pair energy. Thus the numerical improvement is **kernel/geometry-specific source information after matching and clipping**, not a gain obtainable by changing only the abstract rank/trace inequality or asserting positive semidefiniteness of the full off-line form.

## 3. Explicit ceilings on this certificate interface

The same source supplies admissible periodic trial-state upper limits on what the specified lower-bound certificate can prove; these are **ceilings on an inference method**, not upper bounds for the actual proportions of zeta zeros. For the first, six-cosine window, a seven-point local inequality cannot certify more than 0.83916, while even an all-pairs bound for that fixed window has ceiling 0.83998 (Proposition 7.2). For the second, ten-cosine window, an eight-point certificate cannot certify more than 0.67357, and its all-pairs version has ceiling 0.67383 (Proposition 7.3).

In particular the printed main certificates are only about

\[
0.83916-q=0.00015540325\ldots,\qquad
0.67357-s=0.00003179982\ldots
\tag{7}
\]

below their respective **fixed-frame** ceilings. This comparison is a direct subtraction of exact theorem ratios from the paper's stated ceiling constants; it does not establish an optimum for every test family. The broader ceiling 0.84093 in Corollary 7.9 assumes the specific regularity hypothesis V(f)<=10 B(f); its critical-line counterpart 0.68185 has its own stated scheme and hypotheses. Neither is a theorem that all support-one inertia arguments are blocked at that value.

These ceilings do not conflict with WI-013's approximately 0.676552 Montgomery–Taylor *pressure-bridge* ceiling: the functional windows, local matching and global assembly are different. They do show that pushing the current seven/eight-point inequalities much harder **at their fixed windows and within the same transfer architecture** has very little headroom; progress toward an individual off-line-zero theorem needs a qualitatively different information carrier.

## 4. Provenance and independent-verification boundary

The source repo at the pinned revision reports Lean v4.33.0-rc2, Mathlib 51e6992efd06126df61a496bebf8f49482a4e129 and a zeta23 base from anthropics/formal-math commit fbdc36bbf17d20af3fd0447c6d1a8a02773c9844. Its Lean statements explicitly concern Mathlib's zeta zero-count objects; the analytic bridge and search-checker soundness are formalized. However the advertised main theorems each retain **one additional computational axiom** recording that a finite checker returned true; three distinct certificate searches supply the three windows. This is *not* an axiom-free kernel execution of all three enormous searches.

The author's deposited C++ result files report PASS_COB_CONTINUUM with respectively 60,467,309, 535,332,163 and 572,959,453 visited boxes for the first, second and third certificates; the source repo documents a separate Python reference search only for the first. The source also reports matching Lean-built kernel tables. Those are **provenance and reported verification outputs**, not an independent Mathia replay. The source-paper claims are a substantial, reproducibly specified new prior-art frontier, but the exact high-dimensional finite certificates, their program/toolchain environment, and the analytic-to-count correspondences have not been independently executed in this watch. No Mathia independent verification or peer review is implied.

A falsifying audit would find an incorrect real/complex zero normalization in (4), a loss in passage from the indefinite full form to the critical Gram subset, failure of the separated-set Gram bound at its actual separation parameter, a nonvanishing per-frame correction overlooked in (6), a false bound for the continuum interval checker, or a Lean statement that counts a different zeta population. Any such failure would require demoting the corresponding number in (1). An end-to-end independent replay would instead strengthen the evidence tier without changing its RH scope.

## 5. Consequence for Weil inertia

Compared to the independently checked WI-172 four-point certificate 0.6728603588..., the source's claimed simple-critical value 0.6735382002... is higher by about 0.0006778413. It also improves the cited 0.6725007 Alpöge–Furman/Montgomery–Taylor baseline. This is genuinely material quantitative prior art, but the source's certificate-dependent headline is kept separate from Mathia's independently replayed evidence.

The transfer is **global in T**. Neither Theorem 1.1 nor Theorem 1.3 proves the same proportion in Wang's shorter interval (T,T+T^theta], so it does not supply WI-226/WI-442's missing source-compatible bow-scale simple-critical reservoir. Even if all bounds in (1) pass independent replay, a finite or zero-density set of off-line zero pairs alters each global ratio by o(1) and survives all the displayed certificates. No Weil positivity, strict defect bootstrap, or elimination of an individual exceptional zero follows. The decisive missing step remains a source-justified individual-defect observable insensitive neither to the zero's tiny horizontal depth nor to its vanishing asymptotic density.
