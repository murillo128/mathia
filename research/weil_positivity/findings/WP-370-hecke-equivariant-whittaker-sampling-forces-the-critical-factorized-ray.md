---
id: WP-370
title: Hecke-equivariant Whittaker sampling forces the critical factorized ray
branch: weil_positivity
status: supported
kind: hecke-equivariant-index-sampling-rigidity
claim_strength: exact classification of diagonal height samplers intertwining the prime Hecke branches on the smooth cusp core, with exact reduction to the factorized critical Whittaker ray
created: 2026-09-19
related: [WP-358, WP-366, WP-368, WP-369]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - classical Fourier-mode action of normalized Hecke operators on the modular surface
  - classical Kirillov/Whittaker realization of GL(2) automorphic Fourier coefficients
---

# WP-370 — Hecke-equivariant Whittaker sampling forces the critical factorized ray

## Claim

`WP-369` leaves one narrow version of index-adapted Whittaker sampling open: a source-forced nonconstant transition sequence

\[
t_n=nY_n
\]

that stays in a compact positive range, so the critical half-density survives while the Whittaker profile `Psi_r(t_n)` still couples the finite index to the archimedean coordinate. The standard Hecke source geometry does **not** supply such a sequence.

Let `a_n(y)` denote the `n`-th positive Fourier coefficient of a smooth finite Fourier packet in the cusp model, and let a diagonal height sampler be

\[
(R_Ya)_n:=a_n(Y_n),\qquad Y_n>0.
\tag{1}
\]

For the Petersson-normalized prime Hecke operator used in `WP-358`,

\[
(T_pF)(z)=p^{-1/2}\left(F(pz)+\sum_{b=0}^{p-1}F\!\left(\frac{z+b}{p}\right)\right),
\tag{2}
\]

the Fourier coefficients satisfy

\[
(T_pa)_m(y)
=p^{1/2}a_{pm}(y/p)
+\mathbf 1_{p\mid m}\,p^{-1/2}a_{m/p}(py).
\tag{3}
\]

Define the corresponding coefficient-sequence Hecke action

\[
(H_pb)_m
=p^{1/2}b_{pm}
+\mathbf 1_{p\mid m}\,p^{-1/2}b_{m/p}.
\tag{4}
\]

Then, on the smooth finite-Fourier cusp core,

\[
\boxed{R_YT_p=H_pR_Y\ \text{for every prime }p}
\tag{5}
\]

holds **if and only if**

\[
\boxed{Y_{pm}=\frac{Y_m}{p}\qquad(p\text{ prime},\ m\ge1).}
\tag{6}
\]

Equivalently,

\[
\boxed{t_{pm}=t_m.}
\tag{7}
\]

Prime factorization therefore forces

\[
\boxed{Y_n=\frac c n,\qquad t_n=c,\qquad c:=Y_1>0.}
\tag{8}
\]

Thus exact Hecke equivariance selects precisely the unique critical ray already isolated in `WP-369`, but it also freezes the finite--archimedean incidence. For the normalized Eisenstein Whittaker mode

\[
w_{r,n}(Y)=\lambda_r(n)\sqrt Y\,K_{ir}(2\pi nY),
\tag{9}
\]

one gets

\[
\boxed{
w_{r,n}(Y_n)
=\sqrt c\,K_{ir}(2\pi c)\,
\frac{\lambda_r(n)}{\sqrt n}.
}
\tag{10}
\]

If the common Bessel factor vanishes, the sampled channel is null; otherwise the arithmetic and archimedean factors separate exactly. The ordinary positive boundary Hilbert norm then has the same `|lambda_r(n)|^2/n` diagonal and the same global divergence proved in `WP-369`.

So **Hecke naturality does not rescue the surviving nonconstant-transition escape**. Within diagonal point sampling, requiring the sampler itself to intertwine the intrinsic Hecke correspondence forces the constant-`nY` ray and hence the factorized, square-divergent geometry. A viable source-forced nonconstant `t_n` must therefore break this exact diagonal Hecke equivariance, or replace point sampling by a genuinely cross-index/operator-valued construction whose sign theorem is derived independently.

**Classification:** `EXACT-DERIVED + FULL-PRIME-HECKE-INTERTWINING + DIAGONAL-HEIGHT-SAMPLER + UNIQUE-C/N-RIGIDITY + CRITICAL-HALF-DENSITY + FINITE-ARCHIMEDEAN-FACTORIZATION + NEGATIVE/NARROWING + MATCHED-CONTROL + NO-ZERO-DATA + NO-GRAND-NOVELTY-CLAIM`.

## 1. Fourier-mode Hecke transport fixes the sampling recurrence

Write a smooth finite Fourier packet as

\[
F(x+iy)=\sum_{n\in\mathbb Z}a_n(y)e(nx).
\tag{11}
\]

The direct branch in (2) is

\[
F(pz)=\sum_n a_n(py)e(pnx),
\tag{12}
\]

so it contributes to output mode `m` only when `p|m`, with radial profile `a_{m/p}(py)`. The averaged inverse branch is

\[
\sum_{b=0}^{p-1}F\!\left(\frac{x+b}{p}+i\frac yp\right).
\tag{13}
\]

The sum over `b` kills input indices not divisible by `p`; writing the surviving index as `pn`, it contributes `p a_{pn}(y/p)e(nx)`. Multiplying both branches by `p^{-1/2}` gives (3).

Now sample output mode `m` at `y=Y_m`. Equation (3) gives

\[
(R_YT_pa)_m
=p^{1/2}a_{pm}(Y_m/p)
+\mathbf1_{p\mid m}p^{-1/2}a_{m/p}(pY_m).
\tag{14}
\]

By contrast, applying (4) after sampling gives

\[
(H_pR_Ya)_m
=p^{1/2}a_{pm}(Y_{pm})
+\mathbf1_{p\mid m}p^{-1/2}a_{m/p}(Y_{m/p}).
\tag{15}
\]

On the smooth cusp core the radial profiles can be varied independently. Therefore equality of (14) and (15) for all packets forces

\[
Y_{pm}=Y_m/p
\tag{16}
\]

from the first branch. When `p|m`, the second branch forces `Y_{m/p}=pY_m`, which is the same recurrence with `m` replaced by `m/p`. Conversely, (16) makes both branches agree term by term, so it is sufficient as well as necessary.

This is an operator-level statement. It does not rely on accidental identities inside one Eisenstein eigenspace, and it avoids a point-evaluation issue on bare `L^2` by making the classification on the smooth finite-Fourier core where every evaluation is defined.

## 2. All-prime equivariance collapses the transition coordinate

Set `t_n=nY_n`. Multiplying (16) by `pm` gives

\[
t_{pm}=pm\,Y_{pm}=mY_m=t_m.
\tag{17}
\]

For

\[
n=\prod_{j=1}^k p_j^{\alpha_j},
\tag{18}
\]

repeated use of (17) yields `t_n=t_1`. Hence (8) follows exactly.

There is no hidden use of Hecke eigenvalues in this step. The scalar normalization in (2) affects the amplitudes in (3), but not the two coordinate maps `y->py` and `y->y/p` that force (16). In fact either Hecke branch by itself already imposes the same recurrence if the sampler is required to commute branchwise with that correspondence.

The free constant `c` is only a global rescaling of the radial section. It cannot carry prime-by-prime arithmetic information. Thus the entire family of exactly Hecke-equivariant diagonal sections is one-dimensional and has constant Kirillov coordinate `nY_n`.

## 3. The forced ray is exactly the WP-369 factorized critical ray

Using the normalized Whittaker coefficient (9) at the forced height (8),

\[
\begin{aligned}
w_{r,n}(c/n)
&=\lambda_r(n)\sqrt{\frac c n}\,
K_{ir}(2\pi c)\\
&=B_r(c)\frac{\lambda_r(n)}{\sqrt n},
\qquad
B_r(c):=\sqrt c\,K_{ir}(2\pi c),
\end{aligned}
\tag{19}
\]

which is (10). Exact Hecke equivariance therefore does something initially attractive: it derives the critical `n^{-1/2}` scale from the correspondence rather than choosing that exponent by hand. But the same derivation makes `nY_n` constant, so the Whittaker profile no longer supplies any nontrivial finite--archimedean incidence.

This distinction matters for the Weil-positivity mandate. Equation (19) is not yet a positive form, and the inherited Hilbert positivity does not preserve the linear half-density. For a finite Fourier packet, Parseval gives

\[
\left\|B_r(c)\sum_{n\le X}
\frac{\lambda_r(n)}{\sqrt n}e(nx)\right\|_2^2
=|B_r(c)|^2\sum_{n\le X}\frac{|\lambda_r(n)|^2}{n}.
\tag{20}
\]

As recorded exactly in `WP-369`, the Eisenstein Rankin--Selberg Dirichlet series

\[
\sum_{n\ge1}\frac{|\lambda_r(n)|^2}{n^s}
=\frac{\zeta(s)^2\zeta(s+2ir)\zeta(s-2ir)}{\zeta(2s)}
\tag{21}
\]

has a pole at `s=1`; consequently the global norm diverges. Hecke equivariance therefore derives the same critical carrier whose canonical positive square both loses linearity and fails global finiteness.

No zeta zero or RH assumption enters the recurrence (16), the rigidity (8), or the factorization (19). Equation (21) is used only to classify the positive Hilbert readout after the source-level rigidity has already been proved.

## 4. Matched controls and falsification

**One Hecke branch.** The rigidity is not caused by cancellation between the two terms of `T_p`. The direct branch requires `pY_{pm}=Y_m`; the inverse branch requires the identical relation. Dropping either branch does not produce a nonconstant `t_n` while retaining branchwise equivariance.

**Change the Petersson normalization.** Replacing the scalar coefficients in (2) by any nonzero normalization changes only the amplitudes in (14)--(15). The evaluation arguments are unchanged, so (16) survives. The `c/n` law is coordinate rigidity, not an artifact of `p^{-1/2}` normalization.

**Use only a subset of primes.** If equivariance is imposed only for primes in a set `P`, then `t_n` is constant only on multiplicative orbits generated by `P`. The global conclusion (8) specifically uses the full unramified prime Hecke family. This identifies the exact hypothesis rather than silently promoting one-prime covariance to a global theorem.

**Twist the amplitudes.** Unramified character twists can alter scalar Hecke amplitudes or phases but do not alter the radial coordinate maps in the two standard correspondence branches. They therefore do not create a nonconstant Hecke-equivariant transition sequence.

**Generic dilation control.** The same recurrence is forced by any abstract multiplicative correspondence whose two branches relabel `n<->pn` while scaling height by `p^{-/+1}`. Hence the derivation of `c/n` is not itself zeta-specific arithmetic evidence. Its value here is negative: it shows that the most obvious source principle for selecting `Y_n` is too rigid to retain the incidence required by the research mandate.

**Weaken exact equivariance.** An asymptotically equivariant sampler could admit slowly varying `t_n`; this finding does not classify it. Such a weakening must quantify the intertwining defect and show that the defect is source-forced rather than tuned to the Weil coefficient.

**Use a non-diagonal sampler.** An operator-valued or cross-index boundary map can mix several heights or Fourier indices before positivity. Equation (16) does not classify that case. But it is a genuinely new candidate: its kernel, domain, prime/archimedean coupling, and independent positivity theorem must all come from the source geometry.

## 5. Prior-art and novelty audit

The ingredients are classical. Formula (2), its Fourier-mode action, and the Kirillov/Whittaker dependence on `ny` are standard parts of the Hecke theory of automorphic forms; `WP-358` already fixed the exact normalization used here, and `WP-369` fixed the normalized Whittaker carrier. A bounded literature check found the expected standard Hecke/Kirillov scaling mechanisms, not a distinct theorem asserting a new Weil-positivity mechanism from diagonal index-adapted sampling.

The contribution here is therefore deliberately narrow: the exact intertwining classification (5)--(8) closes a live Mathia escape left explicit by `WP-369`. It does **not** claim a new theorem in classical automorphic representation theory, nor does it identify a geometric proof of Weil positivity. It says only that if the missing sampling rule is required to be the obvious diagonal section compatible with the full prime Hecke correspondence, then the source forces the already-known factorized critical ray and cannot supply the needed nonconstant finite--archimedean incidence.

## Consequence for the research line

The surviving Whittaker route is now narrower than after `WP-369`. A nonconstant bounded transition sequence `t_n` cannot be justified merely by saying that the sampling should respect the standard Hecke action: exact respect for that action forces `t_n` to be constant. The next meaningful escape must therefore derive either a controlled **failure** of diagonal Hecke equivariance from the global source, or a non-diagonal/cross-index boundary object on which positivity acts before the critical half-density is squared. Merely choosing a slowly varying `t_n` remains an inserted kernel in different notation.