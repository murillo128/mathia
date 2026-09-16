# PL-332 — The source-selected critical boundary coefficient is L2-continuous across first-prime activation

**Evidence:** `EXACT-DERIVED + POSITIVE-GATE-NARROWING + PARAMETER-STABILITY`

**Status:** `UNIFORM-PL329-REMAINDER + L2-BRANCH-CONTINUITY => COEFFICIENT-CONTINUITY + COEFFICIENT-COLLAPSE-NOT-INDEPENDENT`

## Precise claim

`PL-329` isolates two branch-specific difficulties at the first rational-prime activation

\[
a_\delta=\frac{\log 2}{2}+\delta,
\qquad \delta\downarrow0:
\]

control the endpoint source amplitude and prevent collapse of the source-selected coefficient `C_delta` in

\[
g_\delta(Q)
=C_\delta Q^{-1/2}+r_\delta(Q).
\]

`PL-330` independently proves norm-resolvent continuity through this activation, hence `L^2` convergence of a phase-aligned isolated eigenbranch on the fixed interval `I=(-1,1)`. By itself that topology is too weak to see a moving endpoint layer. The point is that, once the uniform residual estimate of `PL-329` is available, the coefficient is no longer hidden on a shrinking layer: it can be recovered from any sufficiently remote **fixed** logarithmic endpoint block. This converts ordinary `L^2` branch continuity into continuity of `C_delta`.

Put

\[
x(Q)=1-2e^{-Q},
\qquad
g_\delta(Q)=u_\delta(x(Q)),
\]

for a family `u_delta in L^2(-1,1)` with

\[
\boxed{u_\delta\longrightarrow u_0\quad\text{in }L^2(-1,1).}
\tag{PL332-1}
\]

Assume that there are fixed constants `R_0,K>0` and coefficients `C_delta` such that

\[
\boxed{
|g_\delta(Q)-C_\delta Q^{-1/2}|
\le \frac KQ
\qquad(Q\ge R_0)
}
\tag{PL332-2}
\]

uniformly for all sufficiently small `delta`, including `delta=0`. Then

\[
\boxed{C_\delta\longrightarrow C_0.}
\tag{PL332-3}
\]

In particular, the hypotheses of `PL-329` imply (PL332-2) whenever its critical envelope is uniform and

\[
\sup_{\delta}S_\delta<\infty,
\qquad
S_\delta=\sup_{Q\ge Q_0}|F_\delta(Q)|,
\tag{PL332-4}
\]

because the exponentially decaying term in `PL329-4` can be absorbed into `K/Q` on a fixed tail. Therefore, for an isolated completed-Weil eigenbranch transported by `PL-330`, **coefficient collapse is not a separate moving-layer gate once the uniform `PL-329` source/remainder control is proved**.

If additionally

\[
C_0\ne0,
\tag{PL332-5}
\]

then `|C_delta|>=|C_0|/2` for small `delta`, and the sharp criterion `PL329-7` becomes automatic under a uniformly bounded source:

\[
\frac{1+S_\delta}{|C_\delta|\sqrt{L_\delta}}
\longrightarrow0,
\qquad
L_\delta=\log\frac{a_\delta}{\delta}.
\tag{PL332-6}
\]

Thus, conditional on the already-isolated uniform endpoint/source estimate, the first-prime sign problem reduces from a two-parameter family condition to the fixed-threshold question `C_0 != 0`.

## 1. The coefficient is visible on a fixed logarithmic block

For `R>=R_0`, define

\[
D_R:=\int_R^{R+1}Q^{-1}e^{-Q}\,dQ>0
\tag{PL332-7}
\]

and the block functional

\[
N_{\delta,R}
:=\int_R^{R+1}
 g_\delta(Q)Q^{-1/2}e^{-Q}\,dQ.
\tag{PL332-8}
\]

Write

\[
g_\delta(Q)=C_\delta Q^{-1/2}+r_\delta(Q).
\]

The uniform remainder bound (PL332-2) gives

\[
N_{\delta,R}=C_\delta D_R+E_{\delta,R},
\]

with

\[
|E_{\delta,R}|
\le K\int_R^{R+1}Q^{-3/2}e^{-Q}\,dQ
\le K R^{-1/2}D_R.
\tag{PL332-9}
\]

Hence

\[
\boxed{
\left|
C_\delta-\frac{N_{\delta,R}}{D_R}
\right|
\le K R^{-1/2}.
}
\tag{PL332-10}
\]

The important order of limits is now explicit. `R` is chosen large but **fixed**. The block `[R,R+1]` is therefore not the shrinking first-prime overlap `Q~L_delta`; it is a fixed positive-measure region in the scaled interval.

## 2. Fixed-block moments are continuous in the branch `L2` topology

The endpoint coordinate has exact Jacobian

\[
dx=2e^{-Q}\,dQ.
\tag{PL332-11}
\]

Therefore (PL332-1) implies, for every fixed `R`,

\[
\int_R^{R+1}
|g_\delta(Q)-g_0(Q)|^2e^{-Q}\,dQ
\longrightarrow0.
\tag{PL332-12}
\]

By Cauchy--Schwarz,

\[
|N_{\delta,R}-N_{0,R}|
\le
\left(
\int_R^{R+1}|g_\delta-g_0|^2e^{-Q}\,dQ
\right)^{1/2}
D_R^{1/2},
\tag{PL332-13}
\]

so

\[
\frac{N_{\delta,R}-N_{0,R}}{D_R}\longrightarrow0
\qquad(\delta\downarrow0)
\tag{PL332-14}
\]

for each fixed `R`.

Combining (PL332-10) at `delta` and at `0` yields

\[
\limsup_{\delta\downarrow0}|C_\delta-C_0|
\le 2K R^{-1/2}.
\tag{PL332-15}
\]

Since `R` is arbitrary, sending `R->infinity` proves (PL332-3).

No pointwise convergence of `u_delta`, positive-order Sobolev control, or aperture derivative is used. The proof needs only `L^2` convergence on the fixed domain plus a **uniform asymptotic remainder**.

## 3. Application to the first-prime completed-Weil branch

`PL-330` writes Suzuki's aperture family on a fixed interval and proves norm-resolvent continuity through

\[
a_0=\frac12\log2.
\]

For a simple isolated eigenvalue, spectral projection continuity permits a phase/sign choice with normalized eigenstates satisfying (PL332-1). More generally, the argument above applies to any selected normalized branch for which this `L^2` convergence is known.

`PL-329` proves, from the exact endpoint source identity and the positive tail comparison, that a family satisfying a uniform critical envelope obeys

\[
|g_\delta(Q)-C_\delta Q^{-1/2}|
\le
\frac{K_1(1+S_\delta)}Q
+K_1e^{-\eta(Q-R_1)}.
\tag{PL332-16}
\]

Thus `sup_delta S_delta<infinity` gives (PL332-2) with a fixed `K`. The source-selected coefficient therefore inherits the `L^2` continuity that was invisible before the residual was controlled.

This sharpens the branch-specific frontier stated in `PL-329`. Under its uniform envelope, one no longer has to prove an independent continuity theorem for `C_delta`: source control supplies the uniform tail expansion, and norm-resolvent branch transport supplies the fixed-block convergence. The remaining independent fixed-aperture issue is whether the threshold coefficient `C_0` is nonzero.

If `C_0!=0`, then (PL332-6) closes the first-prime reflected-correlation sign under bounded source amplitude. This is still only the first source activation; no later-prime or global Weil-positivity statement follows.

## 4. Why the uniform remainder is load-bearing

`L^2` convergence alone cannot control a boundary coefficient. Let `R_delta->infinity` and choose two distinct constants `C_0,C_1`. A family can agree with the `C_0 Q^{-1/2}` profile for `Q<R_delta` and transition to `C_1 Q^{-1/2}` for `Q>R_delta+1`. Its coefficient at infinity is `C_1`, but the physical `L^2` cost of the changed tail is exponentially small:

\[
\int_{R_\delta}^{\infty}
Q^{-1}e^{-Q}\,dQ
=O\!\left(\frac{e^{-R_\delta}}{R_\delta}\right).
\tag{PL332-17}
\]

Therefore such a family converges to the `C_0` state in `L^2` while retaining a different asymptotic coefficient. This is the same topology mismatch exposed by `PL-330` and `PL-331`: fixed graph or all-fixed-log control cannot see a layer escaping to `Q=infinity`.

The theorem works because (PL332-2) prevents that escape uniformly. Once the remainder is `O(1/Q)` with a family-independent constant, the coefficient can already be read to accuracy `O(R^{-1/2})` on a fixed block; only then can `L^2` convergence transport it.

## Prior-art and novelty audit

The weighted block-extraction argument is elementary compactness/uniqueness of an asymptotic coefficient and is not claimed as a new general theorem. The logarithmic-Laplacian critical boundary scale is prior art from Hernández-Santamaría--López Ríos--Saldaña (source `97`), while Suzuki's localized Weil family is source `56`. A targeted search around logarithmic-Laplacian boundary traces/quotients, parameter-dependent eigenfunctions, boundary Harnack estimates, and continuity of critical logarithmic boundary coefficients found the established fixed-operator boundary regularity and Hopf theory, but no result that directly supplies the present first-prime parameter passage. Search absence is not used as evidence of broad novelty.

The durable mathematical delta is line-local and exact: **the coefficient-collapse gate isolated in `PL-329` is automatically controlled by `PL-330` once the uniform `PL-329` residual estimate holds.** This is a compatibility theorem between two previously separate pieces of the line, not a claim that asymptotic-coefficient continuity is novel in analysis.

## Adversarial controls and limits

- **Uniform source/envelope control is still unproved for the actual branch.** The argument does not manufacture (PL332-2). It uses the family-uniform consequence of `PL-329`; deriving the required source bound and uniform critical envelope remains a live branch-specific problem.
- **Threshold noncollapse is not proved.** The result converts moving-family noncollapse to the single fixed question `C_0!=0`; it does not prove that fixed-threshold statement.
- **No contradiction with `PL-330` or `PL-331`.** Those findings show that graph convergence and every fixed logarithmic Fourier scale miss hostile moving layers. Here the additional uniform `O(1/Q)` asymptotic removes precisely that freedom.
- **The phase/sign must be aligned.** Norm-resolvent continuity of a simple eigenprojection gives a continuous eigenvector only after the usual sign/phase choice. Replacing `u_delta` by `-u_delta` also replaces `C_delta` by `-C_delta`; the sign convention must therefore be fixed before asserting (PL332-3). The magnitude conclusion needed for `PL329-7` is phase-insensitive.
- **No operator-norm continuity of the prime shift is assumed.** The proof uses the full norm-resolvent result of `PL-330`, which was obtained despite the operator-norm jump of the newly activated compressed translation.
- **The fixed block must precede the limit `R->infinity`.** Taking `R=R_delta` would return to the moving-layer topology obstruction and invalidate the use of ordinary `L^2` convergence.
- **No RH consequence follows yet.** Even closing the first-prime reflected sign does not control later prime-power activations or establish global positivity of the localized Weil form.

## Consequence for the line

The first-prime source gate now has a cleaner dependency structure. Under the uniform critical-envelope hypothesis of `PL-329`, a bounded actual source would simultaneously give the uniform `O(1/Q)` residual and, through `PL-330`, continuity of the source-selected coefficient. Therefore coefficient collapse need not be controlled separately along the moving branch.

The remaining high-value questions are narrower:

1. prove the actual branch has the uniform endpoint/source estimate needed by `PL-329`; and
2. establish `C_0!=0` for the threshold state by a fixed-aperture argument.

If both hold, `PL-329` and the present continuity theorem force eventual positivity of the first `p=2` reflected correlation.

## Sources

- Source `56` in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, localized completed-Weil/logarithmic-Laplacian operator family and prime-power translations.
- Source `97`: Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*: canonical `ell(dist)^{1/2}` boundary scale.
- `PL-329`: uniform source-selected `Q^{-1/2}+O((1+S_delta)/Q)` endpoint expansion and sharp first-prime source-amplitude criterion.
- `PL-330`: norm-resolvent continuity and fixed-domain eigenbranch transport through first-prime activation.
- `PL-331`: fixed all-log Fourier control still misses the critical moving layer, providing the topology control for the necessity of the uniform asymptotic remainder.
