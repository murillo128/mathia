---
id: WP-314
title: Empty-side moving Julia nodes have a universal arithmetic-blind logarithmic boundary layer
branch: weil_positivity
status: supported
kind: moving-boundary-julia-universal-tangent-obstruction
claim_strength: exact scaling-limit obstruction for classical Julia–Nevanlinna reductions whose regular boundary node escapes to the positive empty side of the reflected Mangoldt support; after the canonical unit-log normalization, the only nondegenerate node-scale boundary layer converges to the Julia reduction of the pure logarithmic Lebesgue control and therefore forgets the arithmetic counting remainder, while on fixed spectral compacta the family degenerates to a constant
created: 2026-09-15
related: [WP-304, WP-305, WP-312, WP-313]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), no. 3-4, 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for the classical Julia–Nevanlinna reduction and preservation of the Pick class
  - Tom M. Apostol, Introduction to Analytic Number Theory, Springer, 1976, for the weighted Mertens estimate used in WP-305 to obtain the density-one Mangoldt counting law
  - NIST Digital Library of Mathematical Functions, Section 5.11, especially Eq. 5.11.2, for the logarithmic large-argument tangent of the digamma/Gamma channel already used in WP-305
---

# WP-314 — Empty-side moving Julia nodes have a universal arithmetic-blind logarithmic boundary layer

## Claim

`WP-312` rules out every finite Julia–Nevanlinna chain at fixed real boundary nodes, and `WP-313` shows that an asymptotically stable infinite fixed-node chain cannot repair the Mangoldt–Gamma sign defect. The remaining scalar loophole was explicitly nonuniform: let the boundary node itself escape with the high-energy scale so that the node limit and the spectral limit do not commute.

For the most canonical such escape on the **empty side** of the reflected Mangoldt support, the nonuniform limit can be computed exactly, and it is not arithmetic.

Let

\[
\mu=\sum_{n=p^k}\frac{\Lambda(n)}{n+1}\,\delta_{\log n}
\tag{1}
\]

be the positive measure from `WP-304`/`WP-305`, with counting law

\[
M(R):=\mu([0,R])=R+C_++\varepsilon(R),
\qquad \varepsilon(R)\to0.
\tag{2}
\]

Reflect it to the negative half-line and write its regularized Pick/Herglotz response as

\[
m(z)
=\int_0^\infty
\left(
-\frac1{E+z}+\frac{E}{1+E^2}
\right)d\mu(E),
\qquad z\in\mathbb H.
\tag{3}
\]

Thus `m=m_-` in the notation of `WP-305`. Every `X>0` is a regular real boundary point because the reflected support is contained in `(-infinity,0)`. Put

\[
w_X=m(X),
\qquad
d_X=m'(X)=\int_0^\infty\frac{d\mu(E)}{(E+X)^2}>0.
\tag{4}
\]

The canonically unit-log-normalized Julia reduction of `WP-312` is

\[
\mathcal J_X[m](z)
=
\frac{d_X(z-X)(m(z)-w_X)}
{d_X(z-X)-(m(z)-w_X)}
+\beta_X,
\qquad \beta_X\in\mathbb R.
\tag{5}
\]

Then, locally uniformly for `zeta` in the upper half-plane,

\[
\boxed{
\mathcal J_X[m](X\zeta)-\beta_X
\longrightarrow
J_*(\zeta)
:=
\frac{(\zeta-1)\Log\zeta}
{(\zeta-1)-\Log\zeta}
}
\qquad (X\to\infty).
\tag{6}
\]

The limit is exactly the same as for the synthetic unit-density control `dE`, whose reflected Herglotz response is simply `Log z`. In fact

\[
J_*(\zeta)=\mathcal J_1[\Log](\zeta)
\tag{7}
\]

with zero real translation. Therefore the full arithmetic remainder in (2), including the source-specific constant and the positive `WP-305` curvature coefficient, disappears from the moving-node boundary layer.

At the same time, if the observation variable is held in a fixed compact subset of `H` while `X->infinity`, then

\[
\boxed{
\mathcal J_X[m](z)-\beta_X\longrightarrow1
}
\tag{8}
\]

locally uniformly. Hence an empty-side moving node has only two canonical limits in the original and node-scaled coordinates: a degenerate constant on fixed spectral scales, or the universal logarithmic-control profile `J_*` on the boundary-layer scale `z~X`.

Moreover `J_*` is not the logarithmic tangent even up to an additive real normalization. Around the removable boundary point `zeta=1`,

\[
J_*(1+h)=2+\frac h3-\frac{h^2}{9}+O(h^3),
\qquad
\Log(1+h)=h-\frac{h^2}{2}+O(h^3).
\tag{9}
\]

Thus the moving Julia layer changes the universal logarithmic shape before any Riemann-specific Gamma curvature is reached. Since the Riemann digamma/Gamma channel has the same large-scale logarithmic tangent, an empty-side moving classical Julia reduction cannot be the missing finite–archimedean completion.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + MOVING-BOUNDARY-JULIA + EMPTY-SIDE-SCALING-LIMIT + UNIVERSAL-LOGARITHMIC-TANGENT + ARITHMETIC-BLIND + MATCHED-LEBESGUE-CONTROL + PICK-POSITIVITY-PRESERVED + NONUNIFORM-LIMIT-CLASSIFIED + NOT-WEIL-POSITIVITY`.

## 1. The reflected Mangoldt source has a density-one scaling limit

The only arithmetic input needed for the moving-node calculation is the exact counting law (2), already derived in `WP-305` from the weighted Mertens estimate. Define the rescaled positive measures

\[
d\nu_X(t):=\frac1X\,d\mu(Xt).
\tag{10}
\]

For every fixed `t>0`,

\[
\nu_X([0,t])
=\frac{M(Xt)}X
=t+\frac{C_++\varepsilon(Xt)}X
\longrightarrow t.
\tag{11}
\]

Thus `nu_X` converges vaguely to Lebesgue measure on `[0,infinity)`. Because (2) also gives the uniform linear counting bound needed at infinity, this convergence extends to the two decaying kernels required below.

First, subtracting the boundary value at the moving node cancels the regularizing term in (3):

\[
\begin{aligned}
F_X(\zeta)
&:=m(X\zeta)-m(X)\\
&=\int_0^\infty
\left(
\frac1{E+X}-\frac1{E+X\zeta}
\right)d\mu(E)\\
&=\int_0^\infty
\left(
\frac1{1+t}-\frac1{t+\zeta}
\right)d\nu_X(t).
\end{aligned}
\tag{12}
\]

The kernel in the last line is `O(t^-2)` uniformly when `zeta` ranges over a compact subset of `H`. Therefore (11), an elementary tail integration by parts, and dominated compactness give

\[
F_X(\zeta)
\longrightarrow
\int_0^\infty
\left(
\frac1{1+t}-\frac1{t+\zeta}
\right)dt
=\Log\zeta
\tag{13}
\]

locally uniformly on `H`.

Second,

\[
Xd_X
=
\int_0^\infty\frac{d\nu_X(t)}{(1+t)^2}
\longrightarrow
\int_0^\infty\frac{dt}{(1+t)^2}
=1.
\tag{14}
\]

No zero data, Gamma factor, or fitted scale is used. Equations (13) and (14) are forced directly by the density-one positive source.

A useful point is that (13) is stronger than the one-ray asymptotic in `WP-305`. It identifies the complete node-scale analytic tangent of the reflected source. The arithmetic remainder in (2) is lower order under this dilation: after division by the moving scale `X`, both `C_+` and `epsilon` disappear.

## 2. The moving Julia layer converges to a universal Pick function

Evaluate (5) at `z=X zeta`. With (12),

\[
\mathcal J_X[m](X\zeta)-\beta_X
=
\frac{(Xd_X)(\zeta-1)F_X(\zeta)}
{(Xd_X)(\zeta-1)-F_X(\zeta)}.
\tag{15}
\]

Substituting (13) and (14) gives (6).

The apparent denominator causes no new admissibility issue. The function on the right is precisely the classical Julia–Nevanlinna reduction of the Pick function `Log z` at the regular boundary node `1`, followed by the forced unit-log inversion of `WP-312`. Hence it is itself Pick class; any apparent singularity in the formula is absent in `H` or removable. In particular, the positivity theorem survives the scaling limit.

That survival is exactly why the result is a useful falsification rather than a positivity failure. The moving-node construction retains classical Pick positivity but loses the arithmetic structure that was supposed to be completed.

The fixed-scale degeneration is equally direct. On a compact set `K subset H`, (2)-(4) give

\[
m(X)=\log X+O(1),
\qquad
Xd_X=1+o(1),
\tag{16}
\]

while `m(z)` is bounded on `K`. Therefore

\[
m(z)-m(X)=-\log X+O_K(1),
\qquad
d_X(z-X)=-1+o_K(1).
\tag{17}
\]

Putting these into (5) yields (8). A moving node escaping into the empty half-line therefore does not converge on the original spectral plane to a new nonconstant Herglotz completion. The only nontrivial profile appears after blowing up the observation coordinate together with the node.

## 3. The matched Lebesgue control is exact, not merely asymptotic

Replace the Mangoldt measure by the positive unit-density control

\[
d\mu_0(E)=dE.
\tag{18}
\]

Its reflected regularized Herglotz response is exactly

\[
\begin{aligned}
m_0(z)
&=\int_0^\infty
\left(
-\frac1{E+z}+\frac{E}{1+E^2}
\right)dE\\
&=\Log z.
\end{aligned}
\tag{19}
\]

Indeed the cutoff integral is

\[
-\Log(R+z)+\Log z+\frac12\log(1+R^2),
\tag{20}
\]

which tends to `Log z` as `R->infinity`.

At the node `X`,

\[
m_0(X)=\log X,
\qquad
m_0'(X)=\frac1X,
\qquad
m_0(X\zeta)-m_0(X)=\Log\zeta.
\tag{21}
\]

Consequently (15) is **identically**

\[
\mathcal J_X[m_0](X\zeta)-\beta_X=J_*(\zeta)
\tag{22}
\]

for every `X>0`, not merely in the limit. The arithmetic source converges to exactly the same boundary-layer profile as this featureless control.

This is the decisive matched-control failure. The first source-specific invariant found in `WP-305`,

\[
A_0
=\gamma^2+2\gamma_1
+\sum_{n\ge2}\frac{\Lambda(n)\log n}{n(n+1)}>0,
\tag{23}
\]

is invisible in (6). So are the discrete pole locations, the von-Mangoldt support, and the constant offset `C_+`. The moving positive geometry has become universal precisely at the scale where nonuniformity keeps it nontrivial.

The same argument works for any positive measure with `M(R)=R+O(1)` (and, with the obvious mild tail condition, for the larger density-one class `M(R)=R+o(R)`). Therefore the boundary layer cannot distinguish the Riemann arithmetic source from broad synthetic density-one controls.

## 4. The universal layer is not asymptotically neutral

One might still hope that a universal positive layer could act as an arithmetic-independent archimedean renormalization. Equation (9) rules out the simplest version of that escape.

The source itself has the scale tangent

\[
m(X\zeta)-m(X)\longrightarrow\Log\zeta.
\tag{24}
\]

The normalized moving Julia operation replaces this by `J_*(zeta)`. A real translation `beta_X` can alter only the additive normalization; it cannot change the derivative or higher shape of the limit. From (9), after any constant matching,

\[
J_*'(1)=\frac13
\neq
1=(\Log)'(1).
\tag{25}
\]

Thus the operation is not a neutral boundary correction that leaves the leading logarithmic geometry intact while repairing only the Riemann-specific `y^-2` term. It changes the leading node-scale shape first.

This matters directly for the Gamma comparison. The large-argument digamma expansion used in `WP-305` implies, on every fixed non-tangential scaled sector,

\[
\psi(a+X\zeta)-\psi(a+X)
\longrightarrow\Log\zeta
\tag{26}
\]

for fixed `a` after the irrelevant constant scale convention is absorbed. Hence the actual archimedean channel shares the logarithmic tangent (24), not the Julia tangent (6). The moving empty-side reduction therefore misses the target before the opposite-sign `-1/(24y^2)` curvature even enters.

## 5. Aggressive falsification and remaining escape routes

The result is deliberately limited to the canonical classical Julia mechanism and the positive empty half-line.

Allowing `beta_X` to depend on `X` does not help: (6) is written after subtracting that arbitrary real translation. Allowing a different positive Möbius multiplier at each stage also does not supply a free parameter. As shown in `WP-312`, the general automorphism sending the reduced boundary value `0` back to infinity is `beta-lambda/u`, and matching the unit logarithmic coefficient forces `lambda=1` at every finite `X`. A later renormalization that restores unit logarithmic growth returns to the same normalization.

Choosing a different proportional node scale does not recover arithmetic either. If the node is `aX` with fixed `a>0` and the observation coordinate is scaled by that same node, the change of variable simply reproduces (6). Finite perturbations of the source or any bounded counting remainder are also washed out by (10)-(14).

The exact control (22) falsifies the interpretation that the boundary layer is detecting a hidden prime/Gamma coupling. It is already present, unchanged, in the continuum measure with no primes at all.

What remains genuinely outside the theorem is narrower and more source-sensitive:

- regular nodes escaping down the **negative support side**, where they must interact with the increasingly fine prime-power pole geometry rather than an empty half-line;
- triangular or moving-node schemes whose coordinate blow-up is not proportional to the node and is independently forced by a Mathia construction;
- matrix/operator-valued Julia or generalized-resolvent reductions;
- a nonseparable finite–archimedean coupling introduced before scalarization;
- a separate archimedean channel with its own independently derived positive theorem.

The first item is now the only classical scalar moving-boundary route capable of retaining arithmetic at the node scale. It is also much harder to regard as a generic geometric completion, because its node placement must confront the actual source atoms rather than a universal density-one tail.

No claim is made here that such support-side moving nodes fail. Nor does (6) rule out a deliberately constructed two-scale tangent theory as an interesting object. It says that the canonical empty-side tangent is both **universal** and **wrong-shaped** for the logarithmic/Gamma completion, so merely invoking noncommutation of the node and high-energy limits does not rescue the route left open by `WP-313`.

## 6. Prior-art and novelty audit

The Julia–Nevanlinna reduction itself is classical. Agler and Young give the regular-boundary reduction used in `WP-312`, prove preservation of the Pick class, and identify reduction with Schur complementation of the boundary Pick matrix. No novelty is claimed for that theorem, the positivity of the boundary derivative, or the Möbius normalization.

The density-one law (2) is also classical analytic-number-theory input once the exact Mathia weight `Lambda(n)/(n+1)` has been fixed: `WP-305` derives it from weighted Mertens asymptotics. The passage from (11) to the scaled Cauchy/Stieltjes transform is an elementary dilation/vague-convergence argument, closely related to standard regular-variation and Stieltjes-transform asymptotics.

A bounded literature audit over Julia–Nevanlinna boundary reduction, boundary Nevanlinna–Pick interpolation, asymptotics at infinity of Pick/Herglotz functions, and moving interpolation nodes did not identify a source asserting the specific limit (6) for a density-one reflected Herglotz source or its comparison with the Mangoldt/Gamma completion. No classical novelty is claimed if an equivalent scaling lemma exists elsewhere.

The Mathia-specific content is the exact collision of three already-fixed structures: `WP-304`/`WP-305` force the pole-normalized Mangoldt measure and expose its first source-specific curvature; `WP-312` forces the classical positivity-preserving Julia normalization; and `WP-313` leaves nonuniform moving-node limits as a live escape. Equations (6), (8), and (22) show that the most canonical such escape on the empty side either degenerates or collapses onto a featureless continuum control.

## 7. Consequence for the research frontier

The scalar Julia frontier can now be split by **which side of the arithmetic support the moving node sees**.

On the positive empty side, moving the node to infinity does create a genuine noncommuting boundary layer, but that layer is exactly universal: it is the Julia reduction of `Log`, shared by every density-one positive source. It therefore cannot carry the finite-prime information or manufacture the Riemann archimedean correction. On fixed coordinates it degenerates to a constant, so there is no hidden nonconstant Pick limit either.

The only classical scalar moving-node possibility not covered is consequently source-side motion through the negative prime-power support, where the local pole spacing and weights can survive a blow-up. Any useful continuation should test that route against matched synthetic atomic density-one controls and ask whether a canonical node rule is forced independently of the Gamma target. If the node rule must be tuned to individual prime gaps or to the desired archimedean coefficient, the route fails the same canonicality criterion even before positivity is considered.

## Conclusion

`WP-313` left open a nonuniform moving-boundary escape because stable passage of high-energy invariants can fail when the Julia node itself goes to infinity. `WP-314` computes the canonical empty-side escape exactly. The positivity survives, but the arithmetic does not: after scaling with the node, the reflected Mangoldt response converges to the pure logarithmic control and its normalized Julia reduction converges to the universal Pick function `J_*`; without that scaling, the family collapses to a constant.

So the noncommuting limit is real, but it is not yet the missing geometry. To remain relevant to Weil positivity, a scalar moving-boundary mechanism must now interact intrinsically with the arithmetic support itself, or the program must leave the classical scalar Julia category.
