# XF-014 — full real-zero gap dynamics form a nonlinear positive-conductance diffusion

**Status:** `EXACT-DERIVED` + `LITERATURE-CALIBRATED` + `STRUCTURAL/BOUNDARY`. XF-007 through XF-013 extracted a positive Markov/Cauchy smoothing structure after linearizing the real-zero ODE around an arithmetic lattice. That positivity is not merely a first-order artifact. On every real-simple slice of the de Bruijn--Newman flow, the **exact adjacent-gap vector** satisfies a nonlinear graph heat equation with symmetric positive conductances. The nonlinearity is entirely in those conductances.

This gives an exact nonlinear interpretation of the equilibrium coordinate `R` from XF-005 and an exact convex-entropy balance on every finite gap block. The bulk term always dissipates; the only obstruction to a local monotonicity statement is a boundary flux from gaps outside the block. Near an arithmetic lattice, the quadratic bulk dissipation becomes the same inverse-square / `H^{1/2}` Dirichlet form that generates the Cauchy limit of XF-008.

The mechanism is universal for ordered one-dimensional logarithmic repulsion, so it is **not** by itself an Xi-specific selector and does not upper-bound `Lambda`. Its value is to move the nonlinear obstruction: the sign of the bulk dynamics is exact, while the hard problem is now the boundary/cutoff term and the arithmetic information needed to control it.

## 1. Exact nonlinear gap equation

Work on any real-simple slice of the de Bruijn--Newman flow on which the Rodgers--Tao zero-motion law applies (in their contradiction regime, `Lambda < t <= 0`). Relabel the complete ordered zero set as

\[
\cdots < x_{i-1}(t)<x_i(t)<x_{i+1}(t)<\cdots
\]

and set

\[
g_i:=x_{i+1}-x_i>0.
\]

Rodgers--Tao's zero-motion law is

\[
x_i'
=
2\sum_{k\ne i}'\frac{1}{x_i-x_k},
\tag{1}
\]

with principal-value summation. Subtract the equations for `x_{i+1}` and `x_i`, and reindex the first sum by one place. The boundary term created by shifting a symmetric principal-value cutoff tends to zero because `|x_k|\asymp |k|/\log_+|k|`. One obtains

\[
\frac{g_i'}{2}
=
\sum_{k\ne i}
\left(
\frac{1}{x_{i+1}-x_{k+1}}
-
\frac{1}{x_i-x_k}
\right).
\tag{2}
\]

For every `k != i`,

\[
\frac{1}{x_{i+1}-x_{k+1}}
-
\frac{1}{x_i-x_k}
=
\frac{g_k-g_i}
{(x_i-x_k)(x_{i+1}-x_{k+1})}.
\tag{3}
\]

Define

\[
\boxed{
c_{ik}
:=
\frac{1}
{(x_i-x_k)(x_{i+1}-x_{k+1})}.
}
\tag{4}
\]

Because both zero sequences are ordered,

\[
\boxed{c_{ik}=c_{ki}>0\qquad(i\ne k).}
\tag{5}
\]

Hence the full gap equation is

\[
\boxed{
g_i'
=
2\sum_{k\ne i}c_{ik}(g_k-g_i).
}
\tag{6}
\]

Unlike (1), the differenced sum in (6) is absolutely convergent for the Xi zero set in the real-simple regime. For fixed `i`, Rodgers--Tao's macroscopic location estimates give `|x_k|\asymp |k|/\log_+|k|`, while their local counting estimates give the crude adjacent-gap bound `g_k=O(\log_+|k|)` that is already sufficient here. Thus the tail is

\[
c_{ik}|g_k-g_i|
\ll
\frac{\log_+^3|k|}{k^2},
\]

which is summable. Equation (6) is therefore an honest pointwise nonlinear diffusion identity after the principal-value velocities have been differenced.

## 2. The `R` field is exactly the nonlinear gap Laplacian

Let

\[
(\mathcal L_x f)_i
:=
\sum_{k\ne i}c_{ik}(f_k-f_i).
\tag{7}
\]

Then (6) is simply

\[
g'=2\mathcal L_x g.
\tag{8}
\]

The conductances depend on the current zero configuration, so this is not a linear autonomous semigroup. But at every fixed time `\mathcal L_x` is a symmetric graph Laplacian with nonnegative off-diagonal weights.

XF-005 established for `q_i=g_i^2` and the normalized exterior field `R_i` that

\[
q_i'=4(2-R_i).
\tag{9}
\]

Combining (8) with `q_i'=2g_i g_i'` gives the exact identity

\[
\boxed{
2-R_i
=
g_i(\mathcal L_x g)_i
=
g_i\sum_{k\ne i}c_{ik}(g_k-g_i).
}
\tag{10}
\]

Thus the equilibrium threshold `R_i=2` is literally the vanishing of a nonlinear positive-conductance Laplacian applied to the gap field. The smoothing comparison in XF-005 is a maximum-principle statement in this representation: a gap no larger than every other gap has `(\mathcal L_x g)_i>=0` and hence opens forward, while a global maximum has the opposite sign.

This reformulation also shows why `R` is scale free. Under `x -> ax+b`, one has `g -> ag` and `c_{ik}->a^{-2}c_{ik}`, so `g_i\mathcal L_x g_i` is invariant.

## 3. Exact convex-entropy balance on a finite block

Let `I` be a finite interval of gap indices and let `Phi` be differentiable and convex on the relevant gap range. Define

\[
E_{I,\Phi}(t)
:=
\sum_{i\in I}\Phi(g_i(t)).
\tag{11}
\]

Using (6), splitting the interaction into `k in I` and `k notin I`, and symmetrizing the internal pairs gives

\[
\boxed{
\begin{aligned}
\frac{d}{dt}E_{I,\Phi}
={}&
-2\sum_{\substack{i<k\\ i,k\in I}}
c_{ik}
\bigl(\Phi'(g_i)-\Phi'(g_k)\bigr)
(g_i-g_k)
\\
&+
2\sum_{\substack{i\in I\\k\notin I}}
c_{ik}\Phi'(g_i)(g_k-g_i).
\end{aligned}
}
\tag{12}
\]

Convexity gives

\[
\bigl(\Phi'(a)-\Phi'(b)\bigr)(a-b)\ge0,
\tag{13}
\]

so the first line of (12) is always nonpositive. The second line is a **boundary flux** and has no fixed sign.

The same formula applies to deviations from any fixed local target spacing `h>0` by taking

\[
\Phi(g)=\varphi\!\left(\frac{g-h}{h}\right)
\]

with convex `varphi`. Therefore the exact nonlinear flow has a whole family of convex gap entropies whose **bulk** is dissipative. What fails on a finite Xi window is not the sign of the internal dynamics but closure of the window.

This distinction matters because the unweighted entropy over all Xi gaps is generally divergent: the zero density changes with height and the sequence is infinite. One cannot delete the second line of (12) by pretending that the global sum is finite. A usable theorem needs either a renormalized/cutoff balance with a controlled flux, or a limiting averaging procedure that proves the flux is negligible.

## 4. Quadratic dissipation exposes the nonlinear `H^{1/2}` structure

For the centered quadratic choice

\[
\Phi(g)=\frac12(g-h)^2,
\]

equation (12) becomes

\[
\boxed{
\begin{aligned}
\frac{d}{dt}
\frac12\sum_{i\in I}(g_i-h)^2
={}&
-2\sum_{\substack{i<k\\i,k\in I}}
c_{ik}(g_i-g_k)^2
\\
&+
2\sum_{\substack{i\in I\\k\notin I}}
c_{ik}(g_i-h)(g_k-g_i).
\end{aligned}
}
\tag{14}
\]

The first term is a genuine nonlinear Dirichlet form with positive conductances.

Near an arithmetic lattice write

\[
g_i=h(1+\varepsilon u_i).
\tag{15}
\]

Then for fixed index separation,

\[
c_{ik}
=
\frac{1+O(\varepsilon)}{h^2(i-k)^2},
\tag{16}
\]

and hence the internal quadratic dissipation has leading term

\[
\boxed{
2\varepsilon^2
\sum_{\substack{i<k\\i,k\in I}}
\frac{(u_i-u_k)^2}{(i-k)^2}.
}
\tag{17}
\]

This is the discrete inverse-square Dirichlet form whose Fourier symbol is first order, `~|theta|`, and whose mesoscopic limit is the `H^{1/2}` / Cauchy energy associated with XF-008. Thus the half-Laplacian structure is visible directly in the **nonlinear gap entropy production**, not only after diagonalizing the position linearization.

This also clarifies the resonance noted in XF-009 with mesoscopic `H^{1/2}` zero-statistic covariance: the same fractional order arises naturally as the dissipative quadratic form of the exact gap dynamics. That resonance is structural only; the available zeta-zero statistics do not yet supply the cutoff-flux estimate needed here.

## 5. Relation to the endpoint Orlicz route

XF-013 proved an exact `L log L` Lyapunov for **adjacent differences of the linearized gap perturbation**. Its proof used that the linearized generator is translation invariant, so the discrete difference operator commutes with a positive convolution semigroup.

Equation (6) does not make that stronger statement nonlinear. The conductances `c_{ik}` vary with the evolving configuration, so an adjacent difference does not commute with the full operator. In particular, XF-014 does **not** claim that

\[
\sum_i \Phi(|g_{i+1}-g_i|)
\]

is monotone for the nonlinear Xi flow.

What survives exactly is a different and more primitive structure: the gap field itself is transported by a positive symmetric conductance network, and every convex gap entropy has negative internal production plus an explicit boundary flux. The endpoint `L log L` derivative mechanism and the present nonlinear gap-entropy mechanism are therefore complementary rather than interchangeable.

## 6. Prior art and novelty boundary

Rodgers and Tao are the primary source for the Xi zero ODE, its principal-value meaning, the arithmetic-progression local-equilibrium picture, and the necessity of spatial cutoffs and boundary/error control in the infinite zero system. Their proof already develops a much more sophisticated renormalized Hamiltonian/energy method. No novelty is claimed here for the underlying logarithmic repulsion, local equilibration, graph-Laplacian maximum principles, convex entropy dissipation, or inverse-square Dirichlet forms.

The positive-conductance mechanism is also part of the broader one-dimensional log/Riesz-gas landscape. Guillin, Le Bris and Monmarché, **On systems of particles in singular repulsive interaction in dimension one: log and Riesz gas**, *Journal de l'École polytechnique — Mathématiques* 10 (2023), 867--916, DOI `10.5802/jep.235`, exploit ordering and convexity of the singular interaction and prove contraction of the squared distance between synchronously coupled ordered particle systems, with corresponding Wasserstein-2 contraction results under confinement. That work is used here as a prior-art boundary: the dissipative sign is a universal one-dimensional repulsion phenomenon, not an Xi-specific discovery.

The durable Mathia contribution is the exact gap-coordinate organization of that mechanism for the de Bruijn--Newman flow: equations (6), (10), and (12) put the previously separate `R` equilibrium coordinate, the lattice Cauchy linearization, and nonlinear cutoff entropy production into one positive-conductance identity.

## 7. Falsification controls and hard boundary

The line-specific matched-control test is decisive here. Any ordered synthetic zero system obeying the same logarithmic-repulsion ODE inherits the same positive-conductance gap diffusion. Finite polynomial backward-heat controls from XF-006 therefore share the same local bulk sign before their endpoint effects are included. **Bulk convex dissipation cannot select Xi.**

The identity also exists only in the real-simple regime. Under a hypothetical positive `Lambda`, it cannot be applied below the first real-rooted time by simply ordering complex zeros. Nor does it cross a collision: conductances become singular as adjacent zeros merge.

Finally, the boundary flux in (12) is not a technical decoration. At the mesoscopic scale singled out by XF-007--XF-008, a block contains about `log^2 T` gaps and interacts through a long-range inverse-square kernel. A proof must quantitatively show that the information carried by the bulk dissipation is not erased by flux through the growing block boundary. Rodgers--Tao's cutoff machinery is strong evidence that this is the right kind of difficulty, but their estimates do not automatically imply the new entropy inequality required for an upper bound on `Lambda`.

## 8. Consequence for `xi_flow`

The nonlinear frontier is sharper. It is no longer necessary to ask whether the positive Cauchy smoothing seen around the arithmetic lattice survives at finite amplitude at the level of the **gap field**: equation (6) says that it does, with exact positive state-dependent conductances.

The next useful test is therefore a cutoff theorem. On a high Xi block of the natural `N\asymp\log^2 T` gap scale, can one choose a convex normalized-gap entropy for which the boundary flux in (12) is provably lower order than the internal dissipation, using unconditional information that remains legitimate without assuming RH? If yes, (12) provides a source-faithful nonlinear route from arithmetic input to mesoscopic relaxation. If no, the failure identifies the boundary-information channel, rather than nonlinear loss of positivity, as the obstruction.

A second target is to decide whether the quadratic `H^{1/2}` bulk form in (17) can be coupled to a configuration-level zero statistic that remains meaningful when zeros are off the critical line. Until one of these arithmetic interfaces is supplied, XF-014 is a structural mechanism and boundary diagnosis, not an upper bound for `Lambda`.