# NB-154 — Boundary approach renormalizes signed conditioning by the line-one gap

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + BOUNDARY-APPROACH + CONDITIONING-RENORMALIZATION + NB-153-FRONTIER`.

`NB-153` shows that a zero-mass signed sampler supported in a fixed compact subset of `Re w>0` cannot isolate an `Omega(log G)` target packet while its total variation per unit target charge is sublogarithmic. One explicit escape left open there is to let the support approach the boundary `Re w=0`, equivalently to sample `xi'/xi` and `zeta'/zeta` closer and closer to the line `Re s=1`. Tracking the constants shows that boundary approach by itself does not remove the conservation obstruction. It changes the relevant conditioning variable.

Let `A,B>0` be fixed. For arbitrarily large `G`, choose a number

\[
0<a_G\le A
\tag{1}
\]

and a compact set

\[
K_G\subset
\{w\in\mathbf C:
 a_G\le \Re w\le A,
\ |\Im w|\le B\}.
\tag{2}
\]

Let `mu_G` be a finite real signed Borel measure supported on `K_G` with

\[
\mu_G(K_G)=0,
\qquad
V_G:=\|\mu_G\|_{\rm TV}.
\tag{3}
\]

For a nontrivial zero `rho=beta+i gamma`, counted with multiplicity, define

\[
Q_G(\rho)
:=
\Re\int_{K_G}
\frac{d\mu_G(w)}{1+w+iG-\rho}.
\tag{4}
\]

Suppose a packet `F_G` of positive-ordinate zeros satisfies

\[
d_G:=|F_G|\ge \kappa\log G
\tag{5}
\]

for a fixed `kappa>0`, and every target zero has positive charge

\[
q_G:=\inf_{\rho\in F_G}Q_G(\rho)>0.
\tag{6}
\]

Write

\[
C_G:=\frac{V_G}{q_G}
\tag{7}
\]

for the absolute conditioning used in `NB-153`, and introduce the gap-normalized conditioning

\[
\boxed{
D_G:=\frac{C_G}{a_G}
=\frac{V_G}{a_G q_G}.
}
\tag{8}
\]

Then the signed zero sum is absolutely convergent and satisfies the uniform boundary-sensitive conservation law

\[
\boxed{
\sum_\rho Q_G(\rho)
=O_{A,B}\!\left(\frac{V_G}{a_G}\right).
}
\tag{9}
\]

Consequently, with

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\ \gamma>0}}
(Q_G(\rho))_-,
\tag{10}
\]

one has

\[
\boxed{
A_G^-
\ge
q_G\bigl(\kappa\log G-O_{A,B}(D_G)\bigr).
}
\tag{11}
\]

In particular, every family with

\[
D_G=o(\log G)
\tag{12}
\]

still obeys

\[
A_G^-\ge(\kappa-o(1))q_G\log G.
\tag{13}
\]

The adverse debt remains local in ordinate. There are constants `R_0=R_0(B)` and `M=M(A,B,kappa)` such that under `(12)` the radius

\[
R_G:=R_0+M C_G
\tag{14}
\]

captures a fixed fraction of the negative charge:

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\ \gamma>0\\ |\gamma-G|\le R_G}}
(Q_G(\rho))_-
\gg_{A,B,\kappa}
q_G\log G.
}
\tag{15}
\]

Moreover this window contains at least

\[
\boxed{
\Omega_{A,B,\kappa}\!\left(
\frac{\log G}{D_G}
\right)
=
\Omega_{A,B,\kappa}\!\left(
\frac{a_G\log G}{C_G}
\right)
}
\tag{16}
\]

adverse zeros. Thus moving the sampler toward `Re s=1` changes the natural condition number from `C_G` to `C_G/a_G`. If `C_G/a_G=o(log G)`, boundary approach cannot by itself isolate a logarithmic target packet.

## 1. The prime-side remainder costs exactly one inverse boundary gap at this level of control

As in `NB-153`, zero total mass makes the zero sum absolutely summable after subtracting any reference point `w_0 in K_G`:

\[
\int_{K_G}\frac{d\mu_G(w)}{1+w+iG-\rho}
=
\int_{K_G}
\left(
\frac1{1+w+iG-\rho}
-
\frac1{1+w_0+iG-\rho}
\right)d\mu_G(w).
\tag{17}
\]

For large `|G-gamma|`, the right side is `O_{A,B}(V_G/(G-gamma)^2)`. Only finitely many zeros remain in every bounded ordinate window, so the full zero sum is absolutely convergent for each `G`. Termwise integration in the genus-one Hadamard formula therefore gives

\[
\sum_\rho Q_G(\rho)
=
\Re\int_{K_G}
\frac{\xi'}{\xi}(1+w+iG)\,d\mu_G(w).
\tag{18}
\]

The rational terms in `xi'/xi` are `O_{A,B}(V_G/G)`, and Stirling gives uniformly on `(2)`

\[
\psi((1+w+iG)/2)
=
\log(iG/2)+O_{A,B}(1/G).
\tag{19}
\]

The common logarithm disappears against `(3)`. The only term whose uniform bound worsens as the support approaches `Re w=0` is the Euler-product term. Absolute convergence on `Re s>1` gives

\[
\left|
\frac{\zeta'}{\zeta}(1+w+iG)
\right|
\le
-\frac{\zeta'}{\zeta}(1+a_G).
\tag{20}
\]

The simple pole of `zeta` at `1`, equivalently the standard estimate already used in `NB-144`, gives uniformly for `0<a_G\le A`

\[
-\frac{\zeta'}{\zeta}(1+a_G)
\ll_A \frac1{a_G}.
\tag{21}
\]

Equations `(18)`--`(21)` prove `(9)`. This identifies the source of the renormalization: the completed-function background still cancels exactly, but the unsigned Euler majorant available near `Re s=1` grows like the reciprocal horizontal gap.

## 2. A logarithmic target packet still forces real adverse zero charge when the normalized condition is sublogarithmic

The target packet contributes at least

\[
\sum_{\rho\in F_G}Q_G(\rho)
\ge \kappa q_G\log G.
\tag{22}
\]

Negative-ordinate zeros remain a quadratic-distance tail. Uniformly in `(2)`,

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_{A,B}
V_G\frac{\log G}{G}.
\tag{23}
\]

Because `a_G\le A`, the term in `(23)` is absorbed by `O_{A,B}(V_G/a_G)` for large `G`. Splitting the positive-ordinate zeros outside `F_G` into positive and negative charges and using `(9)` therefore yields

\[
A_G^-
\ge
\kappa q_G\log G
-O_{A,B}\!\left(\frac{V_G}{a_G}\right),
\tag{24}
\]

which is exactly `(11)` after substituting `(8)`. The boundary layer has therefore not destroyed the sign-debt mechanism; it has only changed the size of the source-side remainder that may absorb it.

The pointwise Poisson bound tracks the same scale. Since every nontrivial zero has `beta<1`,

\[
1+\Re w-\beta\ge a_G,
\]

and hence

\[
|Q_G(\rho)|
\le
\frac{V_G}{a_G}
=q_GD_G.
\tag{25}
\]

Applying `(25)` to a target zero also shows

\[
D_G\ge1.
\tag{26}
\]

Thus `D_G`, not `C_G` alone, is the scale-invariant measure of how much coefficient variation is being spent relative to the largest pointwise amplification naturally supplied by the shrinking horizontal gap.

## 3. Boundary amplification does not buy long-range ordinate escape

For `|G-gamma|` larger than a fixed multiple of `B+1`, the real Poisson kernel itself gives a bound independent of the small horizontal gap:

\[
|Q_G(\rho)|
\ll_{A,B}
\frac{V_G}{(G-\gamma)^2}.
\tag{27}
\]

Riemann--von Mangoldt shell counting therefore gives, for `R>=R_0(B)` and `R=o(G)`,

\[
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_{A,B}
V_G
\left(
\frac{\log G}{R}
+
\frac{\log G}{G}
\right).
\tag{28}
\]

Under `(12)`, one has `C_G=a_GD_G=O_A(D_G)=o(log G)`, so `(14)` is `o(G)`. Substituting `V_G=q_GC_G` and `R=R_0+M C_G` in `(28)` gives

\[
\sum_{|\gamma-G|\ge R_G}|Q_G(\rho)|
\le
O_{A,B}(M^{-1}q_G\log G)
+o(q_G\log G).
\tag{29}
\]

Choosing `M` sufficiently large and combining `(13)` with `(29)` proves `(15)`. Finally each adverse zero contributes at most `q_GD_G` by `(25)`, so dividing the mass in `(15)` by that pointwise maximum proves `(16)`.

There are therefore two different effects of approaching the line `Re s=1`. It can amplify the useful target charge by the factor `1/a_G`, but the same factor appears in the worst-case Euler-product remainder and in the maximum adverse charge per zero. It does not improve the quadratic ordinate decay. Once conditioning is measured relative to that boundary amplification, the `NB-153` population-versus-displacement mechanism survives.

## 4. What this closes and what remains open

For a fixed positive gap `a_G>=a_0`, `D_G` is comparable to `C_G`, and the result reduces to the scaling of `NB-153`. The new regime is `a_G->0`. There, even an absolute condition number `C_G` that tends to zero need not represent good effective conditioning: the relevant quantity is `C_G/a_G`.

In particular, if

\[
C_G=O(a_G),
\tag{30}
\]

then `D_G=O(1)` and the sampler still forces `Omega(log G)` adverse zeros in an ordinate window of bounded radius. More generally, every

\[
C_G=o(a_G\log G)
\tag{31}
\]

forces a divergent adverse population of order at least

\[
\frac{a_G\log G}{C_G}.
\tag{32}
\]

Thus simply moving a well-conditioned compact sampler toward `Re s=1` is not a new escape from signed conservation. The first gap-normalized conditioning scale not excluded by this argument is logarithmic:

\[
\frac{C_G}{a_G}\asymp \log G.
\tag{33}
\]

Equation `(33)` is a boundary of this method, not a construction. The theorem does not show that logarithmic normalized conditioning isolates the packet, and it does not exploit any cancellation inside the signed Euler/von-Mangoldt combination. It also keeps horizontal width and vertical diameter uniformly bounded. Growing support, macroscopic height mixing, or a target-aware Nyman/prime-side identity that controls the Euler term more sharply than `(20)` remain genuinely different currencies.

The conclusion is likewise not an intrinsic zero-spacing theorem. It is a statement about exterior zero-mass Cauchy/Poisson samplers and the actual zeta source. The packet hypothesis `(5)` is conditional: if such a target packet exists and the sampler charges it uniformly positively, then the remaining actual zeros must carry the stated adverse debt.

## Prior-art search

Bruna and Melnikov, *On translates of the Poisson kernel and zeros of harmonic functions*, Bull. London Math. Soc. 39 (2007), 317--326, treat completeness and uniqueness for Poisson translates. Differenced logarithmic derivatives are classical in zero-free-region arguments; Ethan S. Lee, *On an explicit zero-free region for the Dedekind zeta-function*, J. Number Theory 224 (2021), 307--322, is a modern explicit example. Chirre and Molero, *Explicit conditional bounds for zeta(s) at the edge of the critical strip*, Port. Math. (published online 19 June 2026), use extremal Poisson majorants/minorants to control logarithmic derivatives on `Re s=1` under RH.

These sources delimit the nearby harmonic-analysis and logarithmic-derivative landscape, but they do not provide the target-conditioned conclusion `(11)`--`(16)` for a zero-mass measure whose exterior support itself approaches `Re s=1`. The only additional analytic input beyond `NB-153` is the classical `1/a_G` Euler-product bound already explicitly derived and used in `NB-144`. No new external theorem is load-bearing, so no `SOURCES.md` update is required.

## Source map

- `NB-144`: the uniform exterior Euler-product estimate `|zeta'/zeta(1+a+it)| <= -zeta'/zeta(1+a) = 1/a+O(1)` that supplies the moving-boundary cost.
- `NB-148`: zero total mass cancels the common Hadamard logarithm and necessarily creates signed Poisson debt.
- `NB-151`--`NB-153`: actual-zero conservation, localization and conditioning/population tradeoffs for fixed exterior geometry.
- Riemann--von Mangoldt/unit-interval zero counting and the completed `xi` logarithmic derivative are already anchored inputs of the line.

## Consequence for the line

The `Re s=1` boundary-approach loophole left by `NB-153` is closed for gap-well-conditioned compact samplers. **A zero-mass sampler supported at horizontal distance at least `a_G` from the one-line cannot isolate an `Omega(log G)` target packet whenever `V_G/(a_G q_G)=o(log G)`: it still exports `Omega(q_G log G)` adverse charge, a fixed fraction remains within ordinate radius `O(1+C_G)`, and at least `Omega(log G/D_G)` actual adverse zeros are required.**

The surviving compact signed route must therefore do more than move toward the boundary. It must spend logarithmic-or-worse conditioning after normalization by the boundary gap, obtain genuinely better signed prime-side cancellation than the absolute Euler bound, or leave bounded compact geometry altogether.