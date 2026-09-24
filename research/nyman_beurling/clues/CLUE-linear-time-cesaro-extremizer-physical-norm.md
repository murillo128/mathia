---
id: CLUE-nyman-beurling-linear-time-cesaro-extremizer-physical-norm
type: research-clue
status: proposed
origin: independent-review
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/findings/NB-317-reduced-denominator-shell-coordinates-make-cesaro-primitive-loss-sharp-n3over2.md
  - research/nyman_beurling/formalization/NB317ReducedShell.lean
  - research/nyman_beurling/findings/NB-318-linear-reciprocal-windows-recover-the-missing-half-power-in-hilbert-primitive-control.md
---

# What is the physical Nyman norm of the linear-time Cesàro Riesz extremizer?

## Observation

NB-317's checked diagonal form has free reduced-denominator coordinates (B_q), with energy (sum_q W(q)B_q^2). At a fixed integer time (K), its exact Riesz extremizer is (B_q=D_q(K)/W(q)), and Möbius inversion recovers genuine shell coefficients from this vector. Thus the formalization identifies a specific source profile that attains the Cesàro-to-primitive evaluation norm.

NB-318 shows that (K_N=\lfloor N/2\rfloor) already has fixed-time Cesàro evaluation norm of order (N^{3/2}). It also restores the physical reciprocal-shell weights and bounds all Hilbert-normalized evaluations in bounded linear windows by (O(N^2)), but it does not determine the physical norm of this particular Riesz extremizer. That norm controls how well the sharp direction for the Cesàro metric transfers to the physical Nyman metric.

## Research question

For (K_N=\lfloor N/2\rfloor), set

\[
\widetilde B_q=\frac{D_q(K_N)}{W(q)\,\mathcal A_N(K_N)},\qquad
\mathcal A_N(K_N)^2=\sum_{q=2}^N\frac{D_q(K_N)^2}{W(q)}.
\]

Recover

\[
x_j=\sum_{\ell\le N/j}\mu(\ell)\widetilde B_{j\ell},\qquad
u_N(k)=\sum_{j=2}^N x_j(k\bmod j),
\]

so that the centered Cesàro energy is one and the primitive at (K_N) has size (\mathcal A_N(K_N)\). Determine the asymptotic scale of the physical norm

\[
\|u_N\|_2^2=\sum_{k\ge1}\frac{|u_N(k)|^2}{k(k+1)}.
\]

## Why it may matter

Write \(E_N:=\|u_N\|_2^2\). The exact profile saturates the \(N^{3/2}\) Cesàro primitive growth, so its Hilbert-normalized evaluation is \(\mathcal A_N(K_N)/\sqrt{E_N}\). If \(E_N=\Theta(1)\), this ratio is \(\Theta(N^{3/2})\); if \(E_N=\Theta(N^{-1/2})\), it is \(\Theta(N^{7/4})\); and if \(E_N=\Theta(N^{-1})\), it is \(\Theta(N^2)\), matching the linear-window upper bound. These scales distinguish how the divisor-coordinate extremizer interacts with the physical shell metric.

## Decisive test

Use the exact reduced-residue or NB-318 Möbius formula for \(D_q(K_N)\), Möbius inversion for \(x_j\), and the source shell formula to prove matching asymptotic bounds for \(E_N=\sum_{k\ge1}|u_N(k)|^2/[k(k+1)]\), then derive the corresponding scale of \(\mathcal A_N(K_N)/\sqrt{E_N}\). A uniform positive lower bound for \(E_N\) would rule out decay for this extremizer; an explicit decaying upper and matching lower bound would quantify its Hilbert gain. Finite computations can check the reconstruction and expose sign or normalization errors, but cannot establish the asymptotic.

## Evidence boundary

Lean proves the finite Riesz extremizer in the centered Cesàro metric, not its physical Nyman norm. NB-318's universal linear-window bounds leave the exact norm of this selected profile undetermined. This clue proposes a source-side compatibility test; it establishes neither its asymptotic nor a global bound for \(\Pi_N\).
