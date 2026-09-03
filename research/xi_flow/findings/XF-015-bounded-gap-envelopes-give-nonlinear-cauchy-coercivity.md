# XF-015 — bounded gap envelopes give nonlinear Cauchy coercivity

**Status:** `EXACT-DERIVED` + `STRUCTURAL/BOUNDARY`. XF-014 showed that on every real-simple slice the exact Xi gap vector satisfies a nonlinear positive-conductance diffusion

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0.
\]

Near an arithmetic lattice, XF-014 recovered the inverse-square Dirichlet form and hence the half-Laplacian/Cauchy structure of XF-008. That fractional coercivity is in fact not perturbative. On any finite block whose gaps stay within a fixed multiplicative envelope of a reference spacing, the exact nonlinear conductances are uniformly comparable to the inverse-square Cauchy kernel. Even more strongly, the **lower coercive bound needs only an upper bound on the gaps**: small gaps increase conductances rather than weakening the bulk smoothing.

Thus finite-amplitude nonlinear deformation does not destroy the mesoscopic `H^{1/2}` mechanism. The remaining ways to lose a useful relaxation estimate are large-gap excursions, uncontrolled boundary flux, or leaving the real-simple regime.

## 1. Exact conductance bounds from interval sums

Let

\[
I=\{a,a+1,\ldots,b\},
\qquad N=|I|\ge2,
\]

be a finite block of adjacent gaps on a real-simple slice, and fix a reference scale `h>0`. For `i<k` in `I`, put `n=k-i`. Since

\[
x_k-x_i=\sum_{r=i}^{k-1}g_r,
\qquad
x_{k+1}-x_{i+1}=\sum_{r=i+1}^{k}g_r,
\tag{1}
\]

the conductance from XF-014 can be written exactly as

\[
\boxed{
 c_{ik}
 =\frac1{
 \left(\sum_{r=i}^{k-1}g_r\right)
 \left(\sum_{r=i+1}^{k}g_r\right)}.
}
\tag{2}
\]

Assume first only the upper envelope

\[
0<g_r\le Mh
\qquad(r\in I).
\tag{3}
\]

Each sum in (2) contains exactly `n` gaps, hence

\[
\sum_{r=i}^{k-1}g_r\le nMh,
\qquad
\sum_{r=i+1}^{k}g_r\le nMh,
\]

and therefore

\[
\boxed{
 c_{ik}\ge\frac1{M^2h^2(k-i)^2}.
}
\tag{4}
\]

No lower gap bound is required for this coercive direction.

If in addition

\[
mh\le g_r\le Mh
\qquad(r\in I)
\tag{5}
\]

for some `m>0`, then the reverse interval-sum bounds give

\[
\boxed{
\frac1{M^2h^2(k-i)^2}
\le c_{ik}\le
\frac1{m^2h^2(k-i)^2}.
}
\tag{6}
\]

Thus the exact state-dependent conductance network is uniformly comparable, on the whole finite-amplitude block, to the inverse-square kernel that appeared only after linearization in XF-007--XF-008.

## 2. Nonperturbative `H^{1/2}` bulk coercivity

Write

\[
a_i:=\frac{g_i}{h}
\]

and define the inverse-square discrete seminorm

\[
\mathcal S_I(a)
:=\sum_{\substack{i<k\\i,k\in I}}
\frac{(a_i-a_k)^2}{(k-i)^2}.
\tag{7}
\]

The quadratic bulk dissipation from XF-014 is

\[
\mathcal D_I(g)
:=2\sum_{\substack{i<k\\i,k\in I}}
c_{ik}(g_i-g_k)^2.
\tag{8}
\]

Using (4) and `g_i-g_k=h(a_i-a_k)` gives the exact lower bound

\[
\boxed{
\mathcal D_I(g)
\ge\frac{2}{M^2}\mathcal S_I(a).
}
\tag{9}
\]

Under the two-sided envelope (5), equation (6) gives the full comparison

\[
\boxed{
\frac{2}{M^2}\mathcal S_I(a)
\le\mathcal D_I(g)
\le\frac{2}{m^2}\mathcal S_I(a).
}
\tag{10}
\]

The key point is that (9) is **finite-amplitude and nonperturbative**. The coefficient does not deteriorate when one or more gaps become small. In the real-simple regime, a small gap shortens one or both interval sums in (2), which makes the corresponding conductances larger. A near-collision is therefore not a soft direction of the bulk gap diffusion.

The lower bound can fail uniformly only if the relevant block contains gaps much larger than the chosen local scale `h`, so that `M` itself becomes large, or if the argument loses the block through its boundary.

## 3. Elementary fractional Poincaré scale on a finite block

Let

\[
\bar a_I:=\frac1N\sum_{i\in I}a_i.
\]

Because `|k-i|\le N-1`,

\[
\mathcal S_I(a)
\ge\frac1{(N-1)^2}
\sum_{i<k}(a_i-a_k)^2.
\tag{11}
\]

The exact variance identity

\[
\sum_{i<k}(a_i-a_k)^2
=N\sum_{i\in I}(a_i-\bar a_I)^2
\tag{12}
\]

therefore yields

\[
\boxed{
\mathcal S_I(a)
\ge\frac{N}{(N-1)^2}
\sum_{i\in I}(a_i-\bar a_I)^2.
}
\tag{13}
\]

Combining (9) and (13),

\[
\boxed{
\mathcal D_I(g)
\ge
\frac{2N}{M^2(N-1)^2}
\sum_{i\in I}(a_i-\bar a_I)^2.
}
\tag{14}
\]

Now define the physical gap variance

\[
Q_I:=\frac12\sum_{i\in I}(g_i-\bar g_I)^2,
\qquad
\bar g_I:=\frac1N\sum_{i\in I}g_i.
\tag{15}
\]

The internal contribution to `Q_I'` is exactly `-\mathcal D_I(g)`; the rest is the same external boundary flux diagnosed in XF-014. Since

\[
Q_I=\frac{h^2}{2}
\sum_i(a_i-\bar a_I)^2,
\]

the bulk part alone obeys

\[
\boxed{
(Q_I')_{\rm bulk}
\le
-\frac{4N}{M^2h^2(N-1)^2}Q_I.
}
\tag{16}
\]

For a mesoscopic block

\[
N\asymp \frac{A}{h^2},
\tag{17}
\]

the coefficient in (16) is `Theta(1/A)`, uniformly in `h`. Thus the fixed-heat-time scale `N\asymp h^{-2}` found perturbatively in XF-007--XF-008 survives for finite-amplitude gap profiles as long as an upper multiplicative envelope is available.

At Xi height `T`, where `h_T\asymp1/\log T`, this again corresponds to `N\asymp\log^2T` gaps. The `log^2 T` mesoscopic scale is therefore not an artifact of linearizing around exact arithmetic spacing.

## 4. Two-sided envelopes also preserve the algebraic Cauchy tail

The upper conductance bound in (6) gives a finite-amplitude version of the algebraic nonlocality from XF-008. Suppose the two-sided envelope (5) holds on all intervening gaps needed for a set of interactions with `|k-i|\ge B\ge2`. Then

\[
\sum_{|k-i|\ge B}c_{ik}
\le
\frac1{m^2h^2}
\sum_{|n|\ge B}\frac1{n^2}
\le
\frac{2}{m^2h^2(B-1)}.
\tag{18}
\]

If the interacting gaps themselves remain in `[mh,Mh]`, then `|g_k-g_i|\le(M-m)h`, so their contribution to the normalized gap velocity `a_i'=g_i'/h` is bounded by

\[
\boxed{
|a_i'|_{|k-i|\ge B}
\le
\frac{4(M-m)}{m^2h^2(B-1)}.
}
\tag{19}
\]

Taking `B\asymp A/h^2` gives an `O(1/A)` tail with constants depending only on the finite-amplitude envelope. This is the same algebraic localization scale as the Cauchy kernel in XF-008, now obtained directly from the exact nonlinear conductances rather than from a Fourier linearization.

Equation (19) is conditional on the stated envelope throughout the interactions being estimated. It is not a global Xi tail theorem: far enough in height the mean spacing itself drifts, and under a hypothetical positive `Lambda` one must remain in the real-simple regime. Its role is to show that finite amplitude does not improve the nonlocality to exponential decay.

## 5. Stress tests and boundary cases

The reference scale `h` is not intrinsic unless tied to the local mean spacing or another independently controlled scale. Choosing `h` after seeing the maximum gap can make (3) vacuous; the content of (4), (14), and (16) is quantitative only when `M=O(1)` is established independently on the block.

The lower coercive estimate deliberately does not assume `g_r\ge mh`. This is not an omission: collapsing gaps make conductances larger. However the real-simple zero ODE itself becomes singular at an actual collision, so the estimate cannot be continued through the collision time merely by taking `m=0`.

The block is not closed. Equation (16) controls only the internal contribution to the variance derivative. The boundary flux can have either sign and can be of the same order as the bulk unless a cutoff/buffer argument controls it. Thus (16) is not a monotonicity theorem for `Q_I` and is not an upper bound for `Lambda`.

Finally, all of these estimates are universal for ordered one-dimensional logarithmic repulsion. Synthetic real-rooted heat flows with different transition times inherit the same conductance comparison whenever their gaps satisfy the same envelope. The result therefore passes the matched-control test only as a **structural mechanism**, not as an Xi-specific selector.

## 6. Prior-art and novelty boundary

Rodgers--Tao remain the primary source for the Xi zero-motion law, local-equilibrium scale, and the necessity of spatial cutoffs in the infinite zero system. Guillin--Le Bris--Monmarché provide a peer-reviewed neighboring-field boundary showing that contraction from ordered one-dimensional singular repulsion is a general log/Riesz-gas phenomenon. Both are already anchored in `research/xi_flow/SOURCES.md`.

No novelty is claimed for inverse-square fractional Dirichlet forms, finite-block Poincaré inequalities, positive-conductance comparison, or algebraic tails as abstract analytic facts. A targeted literature check did not identify this exact gap-envelope formulation for the de Bruijn--Newman flow, but absence from the search is not used as evidence. The durable contribution is the elementary consequence of the exact XF-014 conductances: **finite-amplitude Xi gap blocks are uniformly Cauchy-coercive whenever their gaps have an `O(1)` upper envelope, and small gaps do not weaken that bulk coercivity.**

## 7. Consequence for `xi_flow`

XF-014 left open whether the half-Laplacian structure seen near arithmetic equilibrium was robust at finite amplitude. Equations (9)--(16) answer that question at the level of bulk coercivity: yes. The natural `N\asymp h^{-2}\asymp\log^2T` relaxation scale survives without a small-perturbation assumption.

This narrows the nonlinear frontier. A useful upper-bound mechanism no longer needs to prove that the Cauchy bulk survives moderate gap disorder; it needs to obtain an **independent local upper envelope**, control the boundary flux on a growing mesoscopic block, and attach arithmetic information that is legitimate without assuming RH. A failure of such a route should therefore be sought in large-gap/boundary information loss rather than in small-gap degeneration of the nonlinear diffusion.