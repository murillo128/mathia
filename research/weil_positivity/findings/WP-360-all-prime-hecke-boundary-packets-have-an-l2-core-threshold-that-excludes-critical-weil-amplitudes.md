---
id: WP-360
title: All-prime Hecke boundary packets have an l2 core threshold that excludes critical Weil amplitudes
branch: weil_positivity
status: supported
kind: all-prime-hecke-boundary-l2-core-obstruction
claim_strength: exact single-mode orthogonality across all primes; exact finite-Fourier-core square-summability threshold for fixed bounded cusp cutoffs; exact exclusion of critical p^-1/2 and Mangoldt amplitudes from the ordinary strong completion
created: 2026-09-18
related: [WP-032, WP-226, WP-247, WP-356, WP-358, WP-359]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - classical self-adjoint normalized Hecke algebra on the modular surface
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - Claire Burrin, Uri Shapira, and Shucheng Yu, Translates of rational points along expanding closed horocycles on the modular surface, Mathematische Annalen 382 (2022), 655-717
  - Florin Radulescu, A universal non-commutative C*-algebra associated to the Hecke algebra of double cosets, arXiv:1008.1008
---

# WP-360 — All-prime Hecke boundary packets have an l2 core threshold that excludes critical Weil amplitudes

## Claim

`WP-359` left two related escapes from the fixed-prime cusp-boundary obstruction: retain coherent Fourier correlations before scalarization, or pass to an **infinite all-prime completion** in which convergence itself may impose new arithmetic structure. The second escape already has a sharp obstruction on the ordinary cusp Hilbert space.

Keep the exact prime-Hecke boundary commutators of `WP-359`,

\[
D_{p,q}
=[M_q,\mathcal U T_p\mathcal U^{-1}]
=V_pA_p+V_p^*B_p,
\qquad
A_p=[M_q,S_{\log p}],
\quad
B_p=[M_q,S_{-\log p}],
\tag{1}
\]

on

\[
\mathcal H=L^2(\mathbb T_u\times\mathbb R_x).
\tag{2}
\]

Let `(a_p)` be arbitrary complex prime coefficients and, for a finite set of primes `F`, form the finite packet

\[
D_F(a)=\sum_{p\in F}a_pD_{p,q}.
\tag{3}
\]

For every nonzero angular Fourier mode `e_r`, the outputs belonging to **different primes are mutually orthogonal**. More precisely,

\[
\boxed{
\|D_F(a)(e_r\otimes f)\|^2
=
\sum_{p\in F}|a_p|^2\|A_pf\|^2
+
\sum_{\substack{p\in F\\p\mid r}}
|a_p|^2\|B_pf\|^2,
\qquad r\ne0.
}
\tag{4}
\]

Assume only that the bounded cutoff has a fixed left tail,

\[
q(x)=q_-
\qquad (x\le -R),
\tag{5}
\]

and is not almost everywhere equal to that tail value. Then

\[
\boxed{
\|A_pf\|^2
\longrightarrow
E_-(f):=
\int_{\mathbb R}|q(y)-q_-|^2|f(y)|^2\,dy
\qquad(p\to\infty).
}
\tag{6}
\]

Consequently, whenever `E_-(f)>0`, the all-prime packet converges strongly on `e_r\otimes f` **if and only if**

\[
\boxed{
\sum_p|a_p|^2<\infty.
}
\tag{7}
\]

The same threshold holds for convergence on the whole natural finite-Fourier cusp core: square summability is sufficient, while failure of square summability already destroys convergence on the elementary vector `e_1\otimes f` for any `f` with `E_-(f)>0`.

Thus the critical arithmetic amplitudes do not belong to the ordinary all-prime strong completion. In particular,

\[
a_p=p^{-1/2}
\quad\Longrightarrow\quad
\sum_p|a_p|^2=\sum_p\frac1p=\infty,
\tag{8}
\]

and

\[
a_p=\frac{\log p}{\sqrt p}
\quad\Longrightarrow\quad
\sum_p|a_p|^2
=
\sum_p\frac{(\log p)^2}{p}
=\infty.
\tag{9}
\]

More generally, both analytic families `a_p=p^{-\sigma}` and `a_p=(\log p)p^{-\sigma}` have the exact ordinary-Hilbert boundary

\[
\boxed{
\operatorname{Re}\sigma>\frac12.
}
\tag{10}
\]

The critical line is the endpoint where the all-prime Hecke boundary field leaves the standard strong Hilbert completion.

This does **not** rule out a genuinely global automorphic state with infinitely many correlated Fourier modes, a renormalized/distributional Hecke field, analytic continuation from `Re sigma>1/2`, or a different Hilbert/incomplete-tensor sector. It shows that any such rescue is a real category/domain change: cross-prime coherence cannot first be assembled as the strong limit of the critical finite-prime boundary packets on the canonical algebraic cusp core and only afterwards squared into positivity.

## 1. Exact orthogonality across primes on one Fourier mode

From `WP-359`, for `r\ne0`,

\[
D_{p,q}(e_r\otimes f)
=
e_{pr}\otimes A_pf
+
\mathbf 1_{p\mid r}\,e_{r/p}\otimes B_pf.
\tag{11}
\]

Fix distinct primes `p` and `s`. The forward outputs `e_{pr}` and `e_{sr}` are different. A forward output cannot equal a backward output from another prime: if `s\mid r` and

\[
pr=\frac r s,
\tag{12}
\]

then `ps=1`, impossible. Finally, the backward outputs `e_{r/p}` are distinct and occur only for the finitely many prime divisors of `r`. Therefore every summand in (11), as the prime varies, lies in a distinct angular Fourier channel. Pythagoras gives (4) exactly.

This is stronger than the fixed-prime statement in `WP-359`. There the surviving smooth interference for a general input lived on the `p^2` orbit graph. Equation (4) shows that an all-prime packet has **no cross-prime cancellation at all on a single nonzero Fourier input**. Any all-prime interference mechanism must therefore enter through a state that already correlates different input Fourier modes before the packet is applied.

## 2. The asymptotic boundary response is independent of the prime

Write `L=log p`. From the explicit commutator formula,

\[
A_pf(x)
=
(q(x)-q(x+L))f(x+L).
\tag{13}
\]

After the change of variable `y=x+L`,

\[
\|A_pf\|^2
=
\int_{\mathbb R}
|q(y-L)-q(y)|^2|f(y)|^2\,dy.
\tag{14}
\]

For every fixed `y`, condition (5) gives

\[
q(y-L)\longrightarrow q_-
\qquad(L\to\infty).
\tag{15}
\]

Since `q` is bounded, dominated convergence applies and yields exactly (6). Hence if `E_-(f)>0`, there is a prime threshold beyond which

\[
\|A_pf\|^2\ge \frac12E_-(f).
\tag{16}
\]

Substituting (16) into (4) proves the necessity of (7). The second term of (4) is irrelevant to the tail because only finitely many primes divide a fixed nonzero `r`.

For the sharp cusp wall `q=1_{(\tau,\infty)}`, the statement is even more transparent. If `f` is supported in a compact interval above `tau`, then for all sufficiently large primes

\[
\|A_pf\|=\|f\|,
\tag{17}
\]

so the prime packet literally contains the orthogonal vector family

\[
(a_pe_p\otimes A_pf)_p
\tag{18}
\]

up to the harmless fixed Fourier label `r`. No regular ordering of the prime sum can cancel that Hilbert mass.

## 3. The finite-Fourier core has the same sharp threshold

Let

\[
\mathcal C_{\mathrm{fin}}
=
\left\{
\sum_{r\in S}e_r\otimes f_r:
S\subset\mathbb Z\setminus\{0\}\text{ finite}
\right\}.
\tag{19}
\]

For a fixed finite set `S`, possible collisions between two forward outputs satisfy

\[
pr=qs,
\qquad r,s\in S,
\tag{20}
\]

with `p,q` prime. For each ordered pair `(r,s)`, after reducing `s/r` there is at most one prime pair `(p,q)` satisfying (20). Thus only finitely many cross-prime forward collisions occur. Backward outputs occur only when a prime divides one of the finitely many indices in `S`, hence also only for finitely many primes.

Outside that finite exceptional set, the prime tails are orthogonal. Because

\[
\|A_p\|,\|B_p\|
\le 2\|q\|_\infty,
\tag{21}
\]

`a in l2(primes)` is sufficient for the finite-prime packets to be Cauchy on every vector of `C_fin`. Conversely, if `a` is not square summable, choose the one-mode vector `e_1\otimes f` with `E_-(f)>0`; (4)--(6) show that the packet is not Cauchy. Therefore

\[
\boxed{
D_F(a)\text{ converges strongly on every vector of }\mathcal C_{\mathrm{fin}}
\iff
(a_p)_p\in\ell^2(\mathbb P).
}
\tag{22}
\]

The statement is deliberately about the canonical finite-Fourier core. It does not claim that no exotic dense domain can be constructed by imposing infinitely correlated Fourier tails. Such a domain would be precisely the additional global structure that the present local Hecke-boundary construction does not provide.

## 4. The critical half-density is exactly outside the core completion

The prime zeta series gives

\[
\sum_pp^{-2\operatorname{Re}\sigma}<\infty
\iff
2\operatorname{Re}\sigma>1.
\tag{23}
\]

Multiplication by a fixed power of `log p` does not move that abscissa. Hence

\[
\sum_p(\log p)^2p^{-2\operatorname{Re}\sigma}<\infty
\iff
\operatorname{Re}\sigma>\frac12.
\tag{24}
\]

There are two natural ways one might try to feed the Weil first-prime coefficient into this boundary geometry, and both hit the same endpoint.

If the logarithmic displacement `L_p=log p` is supposed to supply the `log p` geometrically, the remaining critical amplitude is `a_p=p^{-1/2}`; (8) excludes it from (22). If instead the full first-prime Mangoldt amplitude is placed before the boundary operation, `a_p=(log p)/sqrt p`; (9) excludes it as well. The obstruction is therefore not an accidental choice about where to store the logarithm.

There is an even harsher mismatch if one tries to repair the scalarized backward branch of `WP-359` by weighting the packet. For a fixed-width cutoff that branch has size

\[
|a_p|^2\frac{\log p}{p}.
\tag{25}
\]

Matching `(log p)/sqrt p` would require `|a_p|^2 asymp sqrt p`, hence `|a_p|asymp p^{1/4}`, which is far outside the square-summable region. The diagonal positive branch therefore cannot be tuned to the Weil exponent while remaining in the ordinary all-prime cusp completion.

## 5. Matched controls and surviving escapes

**Generic covering control.** Replace the prime Hecke angular maps by any infinite collection of distinct circle covering isometries `V_m e_r=e_{mr}` with fixed bounded height cutoffs. On `e_1` the forward outputs are again orthogonal. The `l2` threshold is therefore a universal Hilbert-space consequence of distinct covering channels, not a Riemann-specific positivity theorem. Arithmetic enters only through which coefficient sequence one attempts to place at that threshold.

**Ordering and Abel-type controls.** On `e_1\otimes f` with `E_-(f)>0`, the squared norm of every finite packet contains the positive sum `sum_p |a_p|^2||A_pf||^2`. Reordering primes cannot change it. Any regularized family whose prime multipliers tend pointwise to one has unbounded Hilbert norm at the critical non-`l2` sequences unless the regularization also changes the coefficients or subtracts the orthogonal mass. Such a subtraction is no longer ordinary Hilbert positivity and requires its own source-defined sign theorem.

**Infinite Fourier correlations.** The result does not kill the coherent-superposition escape of `WP-359`. A vector with infinitely many Fourier modes can arrange output collisions such as `pr=qs` across different source indices, and a Hecke eigenfunction is precisely a highly correlated arithmetic object rather than a finite Fourier packet. What is now required is stronger: those correlations must be source-forced strongly enough to define the critical all-prime object despite the failure of the canonical core, and the resulting domain/renormalization must still carry an independent positive theorem.

**Constant mode and Maaß--Selberg escape.** The mode `r=0` is excluded from (4) because every Hecke branch collides there. That sector remains tied to constant terms and scattering, where `WP-345`--`WP-357` already isolate a different set of ambiguities. The present obstruction is specifically the nonconstant all-prime completion suggested by `WP-358`--`WP-359`.

**Different representation sector.** `WP-247` found the same critical `l2` boundary for one-prime nonspherical excitations in the canonical spherical-reference restricted tensor product. The present derivation is independent: the orthogonal channels now arise from cusp Fourier outputs `e_{pr}`, not from finite-place tensor factors. Agreement of the two obstructions is evidence that simply moving the critical amplitudes between standard automorphic Hilbert realizations does not remove the completion problem, but it is not a theorem excluding a different incomplete tensor sector or rigged/distributional representation.

## 6. Prior-art and novelty audit

The normalized self-adjoint Hecke operators on the modular surface, their Fourier action, and their simultaneous spectral theory are classical; Iwaniec's monograph is the standard reference, and Burrin--Shapira--Yu give a modern explicit `L^2` treatment with the same `n^{-1/2}` normalization. Abstract operator-algebraic completions of Hecke algebras, including Radulescu's C*-algebraic constructions, are also established prior art. None of those ingredients is claimed as new.

A bounded literature search was run against infinite series of Hecke operators, `L^2`/C*-Hecke completions, prime Hecke sums, cusp truncation, Maaß--Selberg boundary terms, and commutators with cusp cutoffs. It located the standard Hecke-algebra and automorphic frameworks but no theorem identified with the exact claim above: the cusp-height commutator representation of `WP-358`--`WP-359`, followed by prime-by-prime Fourier-output orthogonality and the resulting sharp `l2` threshold on the finite-Fourier boundary core.

The substantive Mathia contribution is therefore a **negative route classification**, not a claim of a new general Hecke theorem. The all-prime escape left open by `WP-359` cannot be realized by taking the ordinary strong sum of critical finite-prime boundary operators on the canonical cusp core. Any remaining construction must introduce the all-prime correlation/domain/renormalization before the positive square is formed.

## 7. Consequence for the Weil-positivity mandate

The local Hecke-boundary route has now crossed three distinct obstructions. A fixed prime retains real arithmetic through divisibility but squares the half-density (`WP-358`). Smoothing the cusp wall adds only `p^2`-orbit coherence and leaves the diagonal `1/p` scale (`WP-359`). Trying to assemble those prime operators first and hope that all-prime coherence repairs the exponent fails on the standard finite-Fourier cusp core exactly at the critical `Re sigma=1/2` boundary.

Thus a surviving automorphic route cannot have the order

\[
\text{critical prime amplitudes}
\to
\text{ordinary all-prime Hecke boundary operator}
\to
D^*D
\to
\text{Weil positivity}.
\tag{26}
\]

The global source must instead create a correlated or renormalized object **before** ordinary Hilbert completion would demand square summability, and that new object must still produce the finite-prime coefficient, Gamma/polar terms, and the required sign from one source-defined geometry. Concrete remaining categories include genuine Maaß--Selberg/Arthur constant-term coupling, a source-defined infinite Fourier/Hecke-eigenstate domain, an adelic/global representation in a different sector with a proved comparison map, or another nonlocal operation whose positivity theorem survives the critical completion.