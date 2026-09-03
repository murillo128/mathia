# XF-008 — fixed-time mesoscopic gap flow has a Cauchy half-Laplacian limit

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NEGATIVE/OBSTRUCTION` for local or exponentially localized fixed-time closures. XF-007 gives the exact lattice linearization of the Xi zero-motion law. On the unique `h^2` gap-index scale that preserves order-one heat-time dynamics, that linearization has Fourier multiplier `-2π|κ| + h^2 κ^2` and therefore converges to the Cauchy/half-Laplacian semigroup `exp(-2πt|D|)`. In the same scaling, the normalized exterior-field defect `R-2` is only `O(h^2)`. At Xi height `T`, this is `O(1/log^2 T)`, even while the relative gap profile changes by order one over fixed heat time.

The consequence is sharper than the window-counting law in XF-007: a fixed-time perturbative mechanism must resolve an `O(log^-2 T)` departure from local equilibrium coherently across `Θ(log^2 T)` gaps, and its linearized spatial dependence has Cauchy tails rather than exponential localization.

## 1. Claim

Start from the arithmetic-lattice linearization of the real-simple zero dynamics from XF-007. If

\[
 g_j=h(1+\varepsilon u_j)+O(\varepsilon^2)
\]

is the relative gap perturbation around spacing `h`, then

\[
\boxed{
 u_j'
 =\frac{2}{h^2}\sum_{m\ne0}\frac{u_{j+m}-u_j}{m^2}.
}
\tag{1}
\]

Introduce the mesoscopic coordinate

\[
 X_j=h^2j.
\]

For a Fourier mode `u_j=e^{iκX_j}` with `|κ|<=π/h^2`, put `θ=κh^2`. The exact symbol from XF-007, written on the principal Brillouin zone, is

\[
\lambda_h(\theta)
 =-\frac{|\theta|(2\pi-|\theta|)}{h^2}.
\]

Hence on the `X=h^2j` scale,

\[
\boxed{
 \lambda_h(\kappa)
 =-2\pi|\kappa|+h^2\kappa^2.
}
\tag{2}
\]

For every fixed Fourier frequency, and therefore for smooth profiles after the usual Fourier cutoff argument,

\[
\boxed{
 \partial_t U=-2\pi|D_X|U
}
\tag{3}
\]

is the continuum limit of the linearized gap flow as `h->0`.

Thus the fixed-time hydrodynamic limit is **first-order fractional diffusion**, not ordinary second-order diffusion. Its semigroup is

\[
 \widehat U(t,\kappa)
 =e^{-2\pi t|\kappa|}\widehat U(0,\kappa),
\]

with Cauchy kernel

\[
\boxed{
 P_t(X)
 =\frac{2t}{X^2+4\pi^2t^2},
 \qquad t>0.
}
\tag{4}
\]

The scale and the kernel both follow from the exact Xi-flow zero ODE linearized at arithmetic equilibrium; no stochastic model is inserted.

## 2. Why `h^2 j` is the fixed-time coordinate

A perturbation of wavelength `N` gaps has index frequency `|θ|~N^{-1}`. Equation (2) shows that an order-one heat-time rate requires

\[
 |\theta|\asymp h^2,
 \qquad
 N\asymp h^{-2}.
\]

This recovers XF-007's `N~h^-2` law, but now as an actual continuum generator rather than a single-mode relaxation-time estimate.

At Xi height `T`,

\[
 h_T\sim\frac{4\pi}{\log T}.
\]

Therefore one `X`-unit contains

\[
 h_T^{-2}
 \sim\frac{(\log T)^2}{16\pi^2}
\]

gaps and occupies physical zero-coordinate length

\[
 h_T^{-1}
 \sim\frac{\log T}{4\pi}.
\]

A fixed positive heat-time interval therefore naturally couples a block of `Theta(log^2 T)` gaps over physical length `Theta(log T)`. The `log T` window in XF-007 is not merely the wavelength at which one mode happens to decay slowly: it is the spatial scale on which the full linearized evolution has a nontrivial fixed-time hydrodynamic limit.

## 3. The normalized exterior field hides the evolution in an `O(h^2)` defect

XF-005 defines the scale-free exterior coordinate `R=qS`, and XF-007 gives at linear order

\[
 2h^2u_j'=-4(R_j-2).
\]

Thus, without specializing to a Fourier mode,

\[
\boxed{
 R_j-2=-\frac{h^2}{2}u_j'.
}
\tag{5}
\]

For the mesoscopic mode `e^{iκh^2j}`, equations (2) and (5) give

\[
\boxed{
 R_j-2
 =\left(\pi h^2|\kappa|-\frac{h^4\kappa^2}{2}\right)u_j.
}
\tag{6}
\]

Therefore a relative gap profile with order-one amplitude can evolve by order one over an order-one interval of heat time while its instantaneous equilibrium coordinate satisfies

\[
 R-2=O(h^2).
\]

At Xi height `T`, this is

\[
\boxed{
 R-2=O\!\left(\frac{1}{(\log T)^2}\right).
}
\tag{7}
\]

This is an information-scale obstruction. A prospective fixed-time barrier cannot treat `R<2`, `R=2`, and `R>2` only at order-one resolution and expect to control the mesoscopic modes that actually retain memory. It must resolve a vanishing `log^-2 T` equilibrium defect and aggregate it coherently across a growing block.

The statement is perturbative: it does not say that every Xi gap has `R-2=O(log^-2 T)`, nor that a large Lehmer-type defect cannot be dynamically important. It says that the slow modes relevant to fixed heat time become invisible at any coarser precision around arithmetic equilibrium.

## 4. Fixed-time influence is algebraically nonlocal

The limiting kernel (4) has tail mass

\[
 \int_{|X|>A}P_t(X)\,dX
 =1-\frac{2}{\pi}\arctan\!\left(\frac{A}{2\pi t}\right)
 \sim\frac{4t}{A}
 \qquad(A\to\infty).
\tag{8}
\]

Hence the perturbative fixed-time flow has no exponentially localized spatial closure. Truncating the mesoscopic field to `|X|<=A` leaves only algebraic `O(t/A)` tail mass in the limiting propagator.

Translated back to Xi coordinates, a cutoff `|X|<=A` corresponds to physical length

\[
 L_T\asymp \frac{A}{h_T}\asymp A\log T.
\]

To make the bare linearized propagation tail smaller than `epsilon`, the Cauchy limit requires `A` of order `t/epsilon`, so a direct cutoff argument pays physical width of order

\[
\boxed{
 \frac{t}{\epsilon}\log T
}
\tag{9}
\]

up to constants. This does not prove that every nonlinear Xi estimate must pay exactly that cost; cancellations, weighted energies, or arithmetic structure may do better. It does show that exponential-locality heuristics are false already in the exact lattice linearization.

## 5. Matched-control and falsification boundary

Nothing in equations (1)--(4) is Xi-specific. The arithmetic progression is the universal equilibrium of the same real-zero ODE, and the `1/m^2` linearized interaction is inherited by matched real-entire or large polynomial controls. The half-Laplacian/Cauchy limit therefore cannot itself distinguish the Xi flow from positive-transition controls.

Its use is instead diagnostic. Any proposed Xi-specific upper-bound mechanism that is perturbative near local equilibrium must add information not contained in the universal semigroup. In particular it needs either:

- an arithmetic/statistical constraint on the mesoscopic initial field at `Theta(log^2 T)`-gap scale;
- a weighted nonlocal observable that controls the Cauchy tails uniformly;
- or a genuinely nonperturbative mechanism that leaves the lattice regime.

A theorem about only a fixed number of neighboring gaps cannot be promoted to a fixed-time barrier merely by iterating the local zero ODE: XF-007 gives the scale mismatch, while the present Cauchy kernel shows the corresponding nonlocal propagation law.

## 6. Prior art and novelty boundary

Rodgers and Tao, **The de Bruijn--Newman constant is non-negative**, *Forum of Mathematics, Pi* 8 (2020), e6, remain the source for the real-simple zero ODE and arithmetic-progression local equilibrium used here. The Fourier identity producing the exact lattice symbol is classical and was already recorded in XF-007.

Long-range lattice operators with algebraically decaying kernels and continuum fractional-Laplacian limits are classical. Óscar Ciaurri, Luz Roncal, Pablo R. Stinga, José L. Torrea and Juan L. Varona, **Nonlocal discrete diffusion equations and the fractional discrete Laplacian, regularity and applications**, *Advances in Mathematics* 330 (2018), 688--738, rigorously develop discrete fractional diffusion and convergence to continuum fractional Laplacians. Their canonical finite-mesh fractional discrete Laplacian is **not** being identified with equation (1); the exact finite-`h` symbols differ. The relevant prior-art boundary is only that a `1/m^2` long-range lattice generator having a first-order fractional continuum limit belongs to a standard nonlocal-diffusion universality class.

No novelty is claimed for the Cauchy semigroup, the half-Laplacian, or fractional diffusion in abstract lattice systems. The Mathia-specific contribution is the exact normalization bridge for the Xi zero flow: the `h_T~4π/log T` spacing converts the lattice symbol into a fixed-time `X=h_T^2j` Cauchy hydrodynamic scale, and equation (5) shows that the corresponding order-one gap evolution is encoded in an `R-2` signal of only order `log^-2 T`.

## 7. Consequence for `xi_flow`

The sequence XF-004--XF-008 now separates three increasingly strong obstructions. Absolute gaps only reach backward time `O(log^-2 T)`; a scale-free local coordinate `R` exists but bounded-radius lattice information still relaxes on that microscopic clock; and the first nontrivial fixed-time limit occurs only after enlarging to `Theta(log^2 T)` gaps, where the evolution becomes algebraically nonlocal and the driving `R-2` defect shrinks to `Theta(log^-2 T)`.

This gives a concrete target for upstream zero statistics. An `analytic_frontier` input useful to Xi-flow dynamics should not merely say that one or a few normalized gaps are atypical. In the perturbative equilibrium regime it must constrain a mesoscopic field on roughly `log^2 T` consecutive gaps, or an equivalent nonlocal functional, at enough quantitative precision to see a `log^-2 T` equilibrium defect. Without that scale match, the statistic is too local or too coarse to survive a fixed amount of heat time.