# PL-300 — Norm-vanishing finite-rank perturbations can destroy zero-order BV and fixed-lag shift transport

**Evidence:** `EXACT-DERIVED + ADVERSARIAL-CONTROL + DECISIVE-REGULARITY-OBSTRUCTION`

**Status:** `GENERIC-PERTURBATION-ROUTE-CLOSED + ACTUAL-WEIL-STRUCTURE-REQUIRED`

## Claim

The uniform-BV mechanism of `PL-299` cannot be transferred from the pure fractional/logarithmic principal branch to the completed-Weil branch by abstract perturbation theory alone. In fact, even **operator-norm vanishing, self-adjoint perturbations of rank at most two** can preserve an isolated simple ground branch and uniform `C_0` convergence while making both total variation and a prescribed nonzero-lag autocorrelation derivative blow up.

Let `I=(-1,1)`. Let `T_s` denote the normalized zero-exterior fractional principal family used in the small-order route of `PL-297`--`PL-299`, with whole-space principal multiplier

\[
m_s(\xi)=\frac{|\xi|^{2s}-1}{2s}+\gamma
\]

(up to the harmless normalization convention used to match Suzuki's `log|xi|+gamma` principal operator), and let `u_s` be its normalized positive principal eigenfunction. Let `u_0` be the principal logarithmic-Laplacian limit. Fix any lag

\[
0<h_0<2.
\]

Then there are sequences `s_j->0+` and bounded self-adjoint operators `B_j` of rank at most two such that

\[
\|B_j\|\longrightarrow0,
\]

and the unique normalized ground state `v_j` of `T_{s_j}+B_j` satisfies

\[
v_j\longrightarrow u_0\qquad\text{uniformly on }\mathbb R,
\]

while

\[
\boxed{\operatorname{TV}(v_j)\to\infty}
\]

and, writing

\[
C_{v_j}(h)=\int_{\mathbb R}v_j(x)v_j(x+h)\,dx,
\]

one can arrange

\[
\boxed{|C_{v_j}'(h_0)|\to\infty.}
\]

Thus none of the following package is sufficient for the shift-derivative limit required by the accepted zero-order Hadamard clue:

\[
\text{norm-small bounded perturbation}
+\text{simple isolated branch}
+\text{uniform state convergence}.
\]

The missing hypothesis must control the **specific structure** of Suzuki's arithmetic/completion remainder strongly enough to yield BV or derivative-measure compactness. Kato-type spectral stability, a fixed positive gap, and norm-resolvent convergence cannot supply that regularity by themselves.

## 1. A high-frequency packet whose log energy is cheap compared with its variation

Choose a real `chi in C_c^infty(I)` such that

\[
E(h_0):=\int_{\mathbb R}\chi(x)\chi(x+h_0)\,dx>0.
\]

This is possible for every `0<h_0<2`. Choose frequencies `K_j->infinity` satisfying

\[
K_jh_0=\frac\pi2+2\pi j,
\]

and set

\[
L_j=\log K_j,
\qquad
s_j=L_j^{-2},
\qquad
\varepsilon_j=L_j^{-2},
\qquad
\phi_j(x)=\chi(x)\cos(K_jx).
\]

Because `s_j log K_j=1/L_j->0`, the normalized fractional symbol stays on the logarithmic scale near the packet frequency:

\[
m_{s_j}(K_j+\eta)=O(L_j)
\]

on the Fourier mass of the shifted Schwartz function `widehat chi(eta)`. Rapid decay of `widehat chi` handles the tails, including the low-frequency region. Hence

\[
\boxed{\|T_{s_j}\phi_j\|_2=O(L_j).}
\]

By contrast, direct differentiation gives

\[
\operatorname{TV}(\phi_j)\ge cK_j-O(1)
\]

for some `c>0` depending only on `chi`. Therefore

\[
\varepsilon_j\|T_{s_j}\phi_j\|_2=O(L_j^{-1})\to0,
\]

while

\[
\varepsilon_j\operatorname{TV}(\phi_j)
\gg\frac{K_j}{L_j^2}\to\infty.
\]

This scale separation is exactly what the logarithmic principal symbol permits: high spatial oscillation costs only `log K` in graph energy but costs `K` in variation.

## 2. The oscillatory state can be made the exact simple ground state by a vanishing rank-two perturbation

Let `alpha_j` be the principal eigenvalue of `T_{s_j}` and normalize

\[
w_j=\frac{u_{s_j}+\varepsilon_j\phi_j}
{\|u_{s_j}+\varepsilon_j\phi_j\|_2}.
\]

`PL-299` gives uniform convergence `u_s->u_0` and a uniform BV bound for the pure principal branch. Since `epsilon_j||phi_j||_infty->0`,

\[
\boxed{w_j\to u_0\text{ uniformly}.}
\]

At the same time the triangle inequality for total variation and the uniform pure-branch BV bound give

\[
\operatorname{TV}(w_j)
\ge (1+o(1))
\bigl(\varepsilon_j\operatorname{TV}(\phi_j)-\operatorname{TV}(u_{s_j})\bigr)
\to\infty.
\]

Now put

\[
\lambda_j=\langle T_{s_j}w_j,w_j\rangle,
\qquad
r_j=(T_{s_j}-\lambda_j)w_j.
\]

Then `r_j perpendicular w_j`. Since `u_{s_j}` is an exact eigenvector and `||T_{s_j}phi_j||=O(L_j)`, expansion of the Rayleigh quotient gives

\[
\lambda_j-\alpha_j=O(\varepsilon_j^2L_j),
\qquad
\|r_j\|_2=O(\varepsilon_jL_j)=O(L_j^{-1}).
\]

Define the bounded self-adjoint finite-rank operator

\[
B_j
=-|r_j\rangle\langle w_j|
-|w_j\rangle\langle r_j|.
\]

Because `r_j perpendicular w_j`, this acts on their two-dimensional span by the off-diagonal matrix with entries `-||r_j||`, so

\[
\boxed{\|B_j\|=\|r_j\|_2=O(L_j^{-1})\to0.}
\]

Moreover

\[
(T_{s_j}+B_j)w_j=\lambda_jw_j.
\]

The first two normalized fractional eigenvalues converge, after the same small-order normalization, to the first two logarithmic-Laplacian eigenvalues. The pure principal eigenvalue is simple, so the limiting first gap is positive. Hence the gap of `T_{s_j}` is bounded below for all large `j`. Since `||B_j||->0` and `lambda_j-alpha_j->0`, min--max gives, for large `j`,

\[
\lambda_j<\lambda_2(T_{s_j}+B_j).
\]

Thus `w_j` is not merely an engineered eigenvector: it is the **unique ground state** of the perturbed operator. Set `v_j=w_j`.

This leaves every ordinary Hilbert-space perturbative signal benign: the perturbation tends to zero in operator norm, the ground state remains simple and isolated, its eigenvalue follows the pure branch, and the eigenvector converges uniformly. BV nevertheless diverges.

## 3. The failure reaches any prescribed active prime-shift lag

The preceding variation blow-up already shows that the compactness hypothesis used by `PL-299` is not perturbatively stable. More strongly, the actual observable needed by the localized prime source can fail at a fixed nonzero lag.

For the packet autocorrelation,

\[
C_{\phi_j}(h)
=\int\chi(x)\chi(x+h)
\cos(K_jx)\cos(K_j(x+h))\,dx.
\]

The product-to-sum identity yields

\[
C_{\phi_j}(h)
=\frac12\cos(K_jh)E(h)
+\frac12\int\chi(x)\chi(x+h)
\cos(2K_jx+K_jh)\,dx.
\]

Repeated integration by parts in the second term, uniformly for `h` near `h_0`, gives

\[
C_{\phi_j}'(h_0)
=-\frac{K_j}{2}\sin(K_jh_0)E(h_0)+O(1)
=-\frac{K_j}{2}E(h_0)+O(1).
\]

The pure derivatives `C_{u_{s_j}}'(h_0)` stay bounded and in fact converge by `PL-299`. The cross terms between `u_{s_j}` and `phi_j` contribute only `O(epsilon_j)`: uniform BV of `u_{s_j}` turns the apparent factor `K_j` into a uniformly bounded oscillatory integral by one-dimensional integration by parts against the derivative measure. Therefore

\[
C_{v_j}'(h_0)
=
C_{u_{s_j}}'(h_0)
-\frac{E(h_0)}2\varepsilon_j^2K_j
+o(\varepsilon_j^2K_j),
\]

and

\[
\varepsilon_j^2K_j
=
\frac{K_j}{(\log K_j)^4}\to\infty.
\]

Consequently

\[
\boxed{|C_{v_j}'(h_0)|\to\infty.}
\]

Because `h_0` was arbitrary in `(0,2)`, it may be chosen to equal any fixed active prime-power translation in the scaled localized-Weil interval. The counterexample therefore attacks the precise physical-space observable, not merely an auxiliary BV norm.

## 4. What this does and does not rule out

This is a **matched adversarial control**, not a model of the actual completed zeta remainder. The perturbations `B_j` are engineered finite-rank operators and do not have Suzuki's special form of finitely many compressed prime-power translations plus the completed continuous-kernel/archimedean remainder. The result therefore does not show that the actual regularized Weil ground branch lacks uniform BV, nor that its shift derivatives fail to converge.

What it rules out is a generic proof. Boundedness of the remainder, convergence of that remainder in operator norm, norm-resolvent convergence of the full operators, persistence of a simple spectral gap, and even uniform convergence of the tracked eigenfunctions are all compatible with catastrophic loss of BV and fixed-lag derivative transport. Any successful transfer of `PL-299` must use a property absent from arbitrary bounded finite-rank perturbations—for example a variation-diminishing/order property, a uniform BV mapping estimate for the specific source/completion operators together with a coercive estimate for the principal resolvent, or a direct equation for the derivative measures.

The same conclusion applies a fortiori to an argument that invokes only Kato perturbation theory. Spectral projection convergence is an `L^2`-level statement and does not upgrade to the Banach regularity needed here without an independent estimate.

## 5. Prior-art and novelty audit

The load-bearing small-order facts are already stored in the line: `PL-297`--`PL-299` use Feulefack--Jarohs--Weth for small-order eigenvalue/eigenfunction convergence and standard fractional rearrangement for the pure-branch uniform BV bound. `PL-289` identifies Suzuki's zero-order principal symbol as `log|xi|+gamma`, explaining the logarithmic high-frequency cost exploited above.

Finite-rank perturbation theory and norm-resolvent/spectral-projection stability are classical. A structure-based literature search for finite-rank perturbations combined with BV/eigenfunction regularity, norm-resolvent convergence with stronger eigenfunction norms, and autocorrelation-derivative stability found broad perturbation and norm-resolvent theories but did not locate this exact logarithmic high-frequency counterexample or a theorem that would invalidate it. No novelty is claimed for the rank-two eigenvector-engineering trick in isolation; the line-local contribution is the exact scale match

\[
\text{logarithmic graph cost }O(\log K)
\quad\text{versus}\quad
\text{variation/shift-derivative cost }O(K),
\]

which shows that the current zero-order Weil regularity gate cannot be discharged abstractly.

No new external source is required beyond the literature already recorded for `PL-289` and `PL-297`--`PL-299`.

## 6. Consequence for `prime_lattice`

The live regularity target is now sharper. It is no longer enough to prove that a fractional regularization of Suzuki's completed operator converges in norm resolvent sense and that its simple ground state converges uniformly. Those conclusions can coexist with divergence of the prime-shift derivative at any chosen active lag.

The next useful theorem must therefore exploit the **actual completed-Weil remainder**. On a source-static interval, the finite arithmetic part is a finite sum of compressed translations, which individually preserve BV at the ambient level; the decisive unresolved issue is whether the coupled eigen-equation plus the archimedean/completion term yields a uniform derivative-measure estimate for the isolated branch as `s->0+`. If it does, `PL-299` supplies the transport mechanism. If it does not, the accepted zero-order Hadamard route loses its shift-control input even though its Hilbert-space spectral branch remains perfectly stable.
