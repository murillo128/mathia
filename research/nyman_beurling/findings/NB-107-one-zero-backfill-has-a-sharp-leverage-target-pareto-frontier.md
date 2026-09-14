# NB-107 — one-zero backfill has a sharp leverage-target Pareto frontier

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + SINGLE-OFF-CRITICAL-ZERO + FULL-EARLY-CELL-BACKFILL + TARGET-AWARE-STATE-GEOMETRY + SHARP-PARETO-FRONTIER + NEGATIVE/METHOD-BOUNDARY`.

`NB-106` shows that the one-zero causal state at the natural ordinate-scale start is much more target-poor than its ambient terminal band: at fixed positive radial depth its normalized target energy is of order `a/G^3`, where

\[
\rho=\frac12+a+i\gamma,
\qquad G=|\gamma|.
\]

It deliberately leaves open the most obvious cross-scale repair: perhaps the same zero-state becomes target-bearing once all earlier, target-rich integer cells are restored. That repair does **not** occur for the maximal one-zero state direction. At the same time, the complete rank-one state channel remains noncoercive for the target in a sharp way.

Let

\[
\rho_j=\frac12+a_j+i\gamma_j
\]

be actual zeta zeros with `a_j>0`, `a_j -> 0`, and `G_j:=|gamma_j| -> infinity`. Put

\[
m_j=\lceil G_j\rceil,
\qquad R_j=m_jq_j,
\qquad 2a_j\log q_j\longrightarrow L\in(0,\infty),
\tag{1}
\]

with integers `q_j>=2`. For any fixed integer `r>=1`, let

\[
\mathcal E_{r,R}
=
\operatorname{span}\{\phi_n:r\le n<R\},
\qquad
\phi_n(t)=e^{-t/2}\mathbf 1_{[\log n,\log(n+1))}(t),
\tag{2}
\]

and let `u_(r,R)` be the Riesz representer on this complete cell space of the one-zero causal functional from `NB-094`. Let

\[
e_{r,R}=e^{-t/2}\mathbf 1_{[\log r,\log R)}(t)
\tag{3}
\]

be the visible part of the canonical target. Then, with

\[
\delta_{r,R}
:=
\frac{|\langle e_{r,R},u_{r,R}\rangle|}
{\|e_{r,R}\|\,\|u_{r,R}\|},
\tag{4}
\]

one has along `(1)`

\[
\boxed{
\delta_{r,R_j}^{\,2}
=
O_{r,L}\!\left(a_jG_j^{2a_j-2}\right)
=
O_{r,L}\!\left(\frac{a_j}{G_j}\right)
\longrightarrow0.
}
\tag{5}
\]

Thus even backfilling the state all the way from the ordinate scale to any fixed natural scale -- including `r=1`, where the visible target mass tends to one -- does not rotate the **maximal one-zero causal state direction** toward the target.

The stronger conclusion is an exact leverage-versus-target frontier. For nonzero `f in E_(r,R)`, define its fraction of the maximal one-zero state gain and its visible target occupation by

\[
\eta(f)
:=
\frac{|L_{\rho,R}(f)|^2}
{\|u_{r,R}\|^2\,\|f\|^2},
\qquad
\chi(f)
:=
\frac{|\langle e_{r,R},f\rangle|^2}
{\|e_{r,R}\|^2\,\|f\|^2}.
\tag{6}
\]

For every `theta in [delta_(r,R)^2,1]`,

\[
\boxed{
\sup_{\eta(f)\ge\theta}\sqrt{\chi(f)}
=
\delta_{r,R}\sqrt\theta
+
\sqrt{1-\delta_{r,R}^2}\sqrt{1-\theta}.
}
\tag{7}
\]

Consequently, for every fixed `theta in (0,1]`,

\[
\boxed{
\sup_{\eta(f)\ge\theta}\chi(f)
=
1-\theta+o(1).
}
\tag{8}
\]

The endpoint `theta=1` recovers `(5)`: the maximal state-gain direction is target-orthogonal asymptotically. But for every fixed `theta<1`, vectors carrying a `theta` fraction of the **maximal** source gain can still retain asymptotically the complementary target fraction `1-theta`. Hence a large one-zero generalized Gram eigenvalue, by itself, cannot produce a coercive finite-window target obstruction even after the early cells are restored. To force target-poorness from this rank-one channel, one must force the relevant vector to carry an asymptotically full fraction of the available state leverage.

## 1. The full backfilled state has an exact target pairing

`NB-094` identifies the one-zero state functional on the integer-cell space as

\[
L_{\rho,R}(f)
=
\sqrt{2a}
\int_0^{\log R}
 e^{\lambda(\log R-v)}f(v)\,dv,
\qquad
\lambda=\rho-\frac12,
\tag{9}
\]

and gives its value on the orthogonal cell basis:

\[
L_{\rho,R}(\phi_n)
=
\frac{\sqrt{2a}}{\rho}
R^\lambda
\left(n^{-\rho}-(n+1)^{-\rho}\right).
\tag{10}
\]

Because

\[
\|\phi_n\|_2^2=\frac1{n(n+1)},
\tag{11}
\]

the squared Riesz norm on `E_(r,R)` is exactly

\[
\boxed{
\tau_{r,R}
:=
\|u_{r,R}\|^2
=
\frac{2a}{|\rho|^2}R^{2a}
\sum_{n=r}^{R-1}
 n(n+1)
\left|n^{-\rho}-(n+1)^{-\rho}\right|^2.
}
\tag{12}
\]

The target restricted to the same cells is simply

\[
e_{r,R}=\sum_{n=r}^{R-1}\phi_n,
\]

so

\[
\boxed{
\|e_{r,R}\|^2
=
\sum_{n=r}^{R-1}\frac1{n(n+1)}
=
\frac1r-\frac1R.
}
\tag{13}
\]

Summing `(10)` telescopes without approximation:

\[
\boxed{
\langle e_{r,R},u_{r,R}\rangle
=
\frac{\sqrt{2a}}{\rho}
R^\lambda
\left(r^{-\rho}-R^{-\rho}\right),
}
\tag{14}
\]

up to the harmless conjugation convention for the complex inner product. Thus the entire effect of restoring all cells below the ordinate scale on the target coupling is an endpoint term. No coefficient reconstruction or Gram inversion is needed for `(14)`.

## 2. Positive terminal depth already lower-bounds the fully backfilled state norm

Take the boundary sequence `(1)`. Since the cells are orthogonal, `(12)` gives monotonically

\[
\tau_{r,R_j}\ge\tau_{m_j,R_j}
\tag{15}
\]

for every fixed `r` once `m_j>=r`. The terminal quantity on the right is exactly the one-zero leverage evaluated in `NB-106`. Because `m_j/G_j -> 1` and `2a_j log q_j -> L`, that result gives

\[
\boxed{
\tau_{m_j,R_j}
\longrightarrow e^L-1>0.
}
\tag{16}
\]

Meanwhile `(14)` gives

\[
|\langle e_{r,R_j},u_{r,R_j}\rangle|^2
=
\frac{2a_j}{|\rho_j|^2}
R_j^{2a_j}
\left|r^{-\rho_j}-R_j^{-\rho_j}\right|^2.
\tag{17}
\]

For fixed `r`, the last factor is bounded uniformly. Also

\[
|\rho_j|\sim G_j,
\qquad
R_j^{2a_j}
=
G_j^{2a_j}e^{L+o(1)},
\tag{18}
\]

because `m_j/G_j -> 1`. Combining `(13)`, `(15)`--`(18)` gives

\[
\delta_{r,R_j}^2
=
O_{r,L}\!\left(a_jG_j^{2a_j-2}\right).
\tag{19}
\]

Every nontrivial zeta zero satisfies `beta<1`, so `a<1/2`; hence

\[
G^{2a-2}\le G^{-1}.
\tag{20}
\]

This proves `(5)`. Notice that no bound on the target-access depth `2a log G` is required. Even in the regime where `NB-106` allows a band starting at the target origin to retain a positive fraction of determinant volume, the **specific maximal one-zero state direction** remains asymptotically target-orthogonal after that backfill.

This does not contradict the sharp converse in `NB-106`: that converse concerns the target mass available in the ambient cell space, not the angle of the state maximizer inside that space.

## 3. Rank-one Gram repair makes the leverage fraction intrinsic

The quantity `eta` in `(6)` is not an arbitrary diagnostic. `NB-093` proves that removing one actual Blaschke zero changes the finite visible Gram by one positive rank-one state update,

\[
K_R^{(\rho)}=A_R+s_Rs_R^*.
\tag{21}
\]

On a consecutive raw band the triangular integer-cell map is invertible, so every `f in E_(r,R)` is represented by a unique raw coefficient vector `c`. Under that identification,

\[
c^*A_Rc=\|f\|^2,
\qquad
|s_R^*c|^2=|L_{\rho,R}(f)|^2.
\tag{22}
\]

Therefore

\[
\frac{c^*K_R^{(\rho)}c}{c^*A_Rc}-1
=
\frac{|L_{\rho,R}(f)|^2}{\|f\|^2},
\tag{23}
\]

and the maximum of the right-hand side is precisely

\[
\tau_{r,R}=\|u_{r,R}\|^2.
\tag{24}
\]

Thus `eta(f)` is exactly the fraction of the maximal one-zero generalized Gram gain attained by `f`. The maximizer is `u_(r,R)` itself, whose target correlation tends to zero by `(5)`.

This also makes the matched control in the next section source-compatible at the finite raw/state level: the extremizing vectors correspond to actual coefficient vectors in the same consecutive innovation band. They are not arbitrary vectors imported from a larger Hilbert space.

## 4. Two-vector geometry gives the exact Pareto envelope

Normalize

\[
\widehat u=\frac{u_{r,R}}{\|u_{r,R}\|},
\qquad
\widehat e=\frac{e_{r,R}}{\|e_{r,R}\|},
\qquad
\delta=|\langle\widehat e,\widehat u\rangle|.
\tag{25}
\]

After a harmless phase change, write

\[
\widehat e
=
\delta\widehat u
+
\sqrt{1-\delta^2}\,z,
\qquad
z\perp\widehat u,
\qquad
\|z\|=1.
\tag{26}
\]

For a unit vector `f` with `eta(f)=eta`, decompose

\[
f=\alpha\widehat u+v,
\qquad
|\alpha|=\sqrt\eta,
\qquad
v\perp\widehat u,
\qquad
\|v\|=\sqrt{1-\eta}.
\tag{27}
\]

Cauchy--Schwarz gives

\[
\sqrt{\chi(f)}
\le
\delta\sqrt\eta
+
\sqrt{1-\delta^2}\sqrt{1-\eta}.
\tag{28}
\]

Equality is attained by taking `v` parallel to `z` with aligned phases. The right-hand side is maximized at `eta=delta^2`; hence under the constraint `eta>=theta>=delta^2` its maximum occurs at `eta=theta`. This proves the exact formula `(7)`.

Along `(1)`, equation `(5)` gives `delta -> 0`. For every fixed `theta>0`, eventually `theta>delta^2`, and `(7)` becomes

\[
\sup_{\eta(f)\ge\theta}\chi(f)
=
\left(
\delta\sqrt\theta
+
\sqrt{1-\delta^2}\sqrt{1-\theta}
\right)^2
=
1-\theta+o(1),
\tag{29}
\]

which is `(8)`. The asymptotic frontier is therefore sharp on both sides: it is an upper bound and is attained within the complete raw cell band.

The interpretation is deliberately asymmetric. If `theta_j -> 1`, then every vector carrying that nearly maximal fraction of the state gain is target-poor. But if `theta<1` is fixed, a complementary fraction `1-theta` of target occupation survives. A polynomially large maximal generalized eigenvalue does not alter this normalized tradeoff.

## 5. Adversarial controls and what this does not prove

The first control is the `NB-106` ambient-space converse. When `2ad log G` is small, a band reaching the target origin can retain a prescribed determinant-volume fraction and nearly all of its ambient target mass. Equation `(5)` shows that this does not make the zero-state maximizer target-bearing; equation `(8)` shows exactly where the ambient target can hide instead -- in directions transverse to the maximizer, at the price of giving up the same fraction of state leverage asymptotically.

Second, the result is a **single-zero rank-one statement**. Several zeros give a finite- or growing-rank state matrix rather than one vector. The relevant target geometry then involves principal angles between the target and a state subspace, and a growing effective state dimension could behave differently. Nothing here bounds that multi-state problem.

Third, `E_(r,R)` is the visible raw integer-cell space and `(21)` is the one-zero finite-window state update. The theorem does not identify the target pairing of a fully Blaschke-deflated Nyman approximant, does not control the unseen tail beyond `R`, and does not lower-bound the canonical finite-section residual. Multiplication by an inner factor is norm preserving on generators but does not preserve pairing with the fixed target. The accepted target-aware finite-section and adjoint-dual clues therefore remain unresolved.

Fourth, the boundary scaling in `(1)` has fixed positive `L`. The proof uses the positive terminal state norm `e^L-1`; it does not claim a uniform theorem as `L -> 0` simultaneously. For larger terminal depth the state norm can only become more favorable to target orthogonality, but that regime is not needed for the present claim.

Finally, `(7)` is elementary two-vector Hilbert geometry. No novelty is claimed for that abstract formula, rank-one update algebra, or principal-angle language. The line-local content is the actual-zeta state identity `(9)`--`(14)`, the boundary backfill estimate `(5)`, and the fact that the generic Pareto envelope becomes a **sharp source-compatible finite-cell control** through the invertible Nyman innovation flag.

## 6. Prior-art boundary and research consequence

The classical Nyman--Beurling/Baez--Duarte and Burnol Hardy-space sources in `SOURCES.md` remain the background boundary. Calderaro--Manzur--Noor--Santos study orthogonality and de Branges--Rovnyak structure for the Hardy Nyman span; Yang studies Friedrichs-angle geometry between Nyman--Beurling subspaces; and the 2026 Gram-spectral BNBD preprint already separates a Blaschke zero component from an arithmetic Gram projection defect. A targeted search across those themes did not identify the specific finite-cell statement that an actual one-zero causal-state maximizer stays target-orthogonal after fixed-scale backfill, together with the exact retained-leverage/target frontier `(7)`. Search absence is not a priority claim.

No external theorem is load-bearing in the derivation: the source-specific inputs are the exact local identities already proved in `NB-093`, `NB-094`, and `NB-106`, while the remaining step is finite-dimensional Hilbert geometry. The existing literature anchors in `SOURCES.md` already cover the closest prior-art boundaries, so no source update is required.

The live target-conversion question is now narrower. **Earlier cells do not rescue the maximal one-zero state direction**, so simply extending the terminal state back toward the target origin cannot turn the large one-zero leverage into a target obstruction. But **earlier cells do rescue target occupation at any fixed submaximal leverage fraction**, and they do so sharply. A successful next bridge must therefore add structure that is absent from a single rank-one state channel: force the actual Nyman residual/dual toward near-maximal state leverage, exploit a genuinely multi-zero state subspace with source-controlled target angles, or construct a target-aware reverse channel that sees the deflated target rather than only the raw finite-cell state geometry.