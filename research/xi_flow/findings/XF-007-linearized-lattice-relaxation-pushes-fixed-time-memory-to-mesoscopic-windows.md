# XF-007 — linearized lattice relaxation pushes fixed heat-time memory to mesoscopic windows

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NEGATIVE/OBSTRUCTION` for perturbative local-equilibrium mechanisms. Rodgers--Tao supply the exact zero-motion law and the arithmetic-progression equilibrium; the new line-specific calculation diagonalizes that law around the lattice and combines it with the Xi zero density. The conclusion is exact for the linearized lattice model: a perturbation involving only `O(1)` neighboring gaps relaxes on the vanishing heat-time scale `O(1/log^2 T)`, while retaining `O(1)` heat-time memory requires about `log^2 T` gaps, i.e. a physical window of length `O(log T)` in the `H_t` zero coordinate.

## 1. Claim

Consider the real-simple zero dynamics

\[
 x_j'(t)=2\sum_{k\ne j}'\frac{1}{x_j(t)-x_k(t)}
\]

in the symmetric principal-value sense used for the de Bruijn--Newman flow. The exact arithmetic lattice

\[
 x_j=jh,
 \qquad h>0,
\]

is stationary. Linearize around it by writing

\[
 x_j=jh+\varepsilon y_j+O(\varepsilon^2).
\]

For bounded perturbations, symmetric cancellation removes the `1/m` background and the first variation is the absolutely convergent operator

\[
\boxed{
 y_j'=\frac{2}{h^2}\sum_{m\ne0}\frac{y_{j+m}-y_j}{m^2}.
}
\]

The Fourier mode `y_j=e^{ij\theta}` is therefore an eigenmode with

\[
\boxed{
 \lambda_h(\theta)
 =\frac{4}{h^2}\sum_{m\ge1}\frac{\cos(m\theta)-1}{m^2}
 =-\frac{\theta(2\pi-\theta)}{h^2},
 \qquad 0\le\theta\le2\pi.
}
\]

Thus every non-translation bounded mode decays forward in heat time. More importantly for `xi_flow`, the decay scale is set by `h^2` times the mode's index wavelength.

For a mode of period `N` gaps, `\theta=2\pi/N`, hence

\[
\boxed{
 |\lambda_{h,N}|
 =\frac{4\pi^2}{Nh^2}\left(1-\frac1N\right),
 \qquad
 \tau_{h,N}:=|\lambda_{h,N}|^{-1}
 =\frac{Nh^2}{4\pi^2(1-1/N)}.
}
\]

At Xi height `T`, the fixed-`t` zero-counting law gives the local mean spacing

\[
 h_T\sim\frac{4\pi}{\log T}
\]

in the Rodgers--Tao `H_t` coordinate. Consequently

\[
\boxed{
 \tau_{T,N}\sim \frac{4N}{(\log T)^2}.
}
\]

A bounded-radius perturbation `N=O(1)` therefore loses its linearized memory on the same `O(1/log^2 T)` scale that appeared independently in XF-004 from the squared-gap collision clock. Conversely, a mode that retains order-one memory across a fixed heat-time interval must have

\[
 N\asymp (\log T)^2,
\]

which occupies physical zero-coordinate length

\[
\boxed{
 L_T=Nh_T\asymp\log T.
}
\]

The conclusion is not that every Xi perturbation is small or Fourier-pure. It is a sharp scaling obstruction for any argument that first places high zeros perturbatively near arithmetic equilibrium and then hopes that a fixed number of normalized neighboring gaps can carry information across a fixed amount of heat time.

## 2. Exact linearization

Put `k=j+m`. Then

\[
 x_j-x_{j+m}
 =-mh+\varepsilon(y_j-y_{j+m})+O(\varepsilon^2).
\]

For bounded `y`, expansion of the reciprocal gives, uniformly summably after symmetric pairing,

\[
 \frac{1}{x_j-x_{j+m}}
 =-\frac1{mh}
 +\frac{\varepsilon}{m^2h^2}(y_{j+m}-y_j)
 +O\!\left(\frac{\varepsilon^2}{|m|^3}\right).
\]

The first term cancels in symmetric principal value, while the derivative term is absolutely summable. Dividing by `\varepsilon` yields the displayed linearized operator.

For a Fourier mode,

\[
 \lambda_h(\theta)
 =\frac{2}{h^2}\sum_{m\ne0}\frac{e^{im\theta}-1}{m^2}
 =\frac{4}{h^2}\sum_{m\ge1}\frac{\cos(m\theta)-1}{m^2}.
\]

The classical Bernoulli/Fourier identity

\[
 \sum_{m\ge1}\frac{\cos(m\theta)}{m^2}
 =\frac{\pi^2}{6}-\frac{\pi\theta}{2}+\frac{\theta^2}{4},
 \qquad 0\le\theta\le2\pi,
\]

gives the exact symbol `-theta(2pi-theta)/h^2`. The only zero eigenvalue among bounded Fourier modes is `theta=0`, corresponding to common translation. This is the expected neutral symmetry; every genuine spacing perturbation is linearly damped.

## 3. Relation to the normalized exterior field `R`

Let

\[
 g_j=x_{j+1}-x_j=h(1+u_j)
\]

with `u_j` infinitesimal. Differences commute with the translation-invariant linearized operator, so `u_j` has the same Fourier eigenvalue `lambda_h(theta)`. Since XF-005 gives

\[
 q_j'=4(2-R_j),
 \qquad q_j=g_j^2,
\]

linearization around `q=h^2`, `R=2` yields

\[
 2h^2u_j'=-4(R_j-2),
\]

and therefore for a Fourier mode

\[
\boxed{
 R_j-2
 =\frac12\theta(2\pi-\theta)u_j.
}
\]

So `R=2` is not only an instantaneous equilibrium threshold. Near the lattice, the deficit/excess `R-2` is the multiplier that generates relaxation, and its multiplier is scale-free while the physical heat-time rate carries the factor `h^{-2}`.

This separates two roles that were mixed in XF-005. `R` is the correct dimensionless local coordinate, but **dimensionless does not mean fixed-time**: converting its local imbalance into evolution still costs the shrinking microscopic time unit `h^2`.

## 4. The `log T` spatial scale is forced by the linearized dynamics

The fixed-`t` counting law used in XF-004 has density

\[
 \frac{dN_t}{dT}\sim\frac{\log T}{4\pi},
\]

so `h_T~4pi/log T`. A Fourier mode with index wavelength `N` has relaxation time asymptotic to `4N/log^2 T`. Hence three scales separate cleanly:

- `N=O(1)` gaps: relaxation time `O(log^{-2}T)`;
- a physical interval of fixed length, containing `N\asymp log T` gaps: relaxation time `O(log^{-1}T)`;
- fixed heat-time memory: `N\asymp log^2 T` gaps, corresponding to physical length `L\asymp log T`.

This is strikingly consistent with Rodgers--Tao's proof architecture. Under the hypothetical negative-`Lambda` regime, their available zero-counting control for `H_t` at negative time only reaches intervals of physical length about `log T`, and their energy argument uses growing spatial cutoffs to obtain local equilibrium before contradicting zeta zero statistics. The present calculation does **not** claim that their cutoff scale was derived by this Fourier analysis. It explains why a `log T` mesoscopic window is the natural scale at which a perturbative lattice mode can still remember an order-one amount of heat time.

## 5. Matched-control and nonlinear stress test

The arithmetic progression is a universal backward-heat equilibrium, not an Xi-specific one: functions of the form

\[
 e^{ta^2}\cos(az)
\]

solve the same backward heat equation and keep their equally spaced zeros fixed. The linearized operator above follows solely from the universal zero ODE. Therefore neither its damping sign nor the `h^2` microscopic clock can by itself select the Xi flow.

This is also compatible with XF-006. That finding showed that every fixed finite collision jet can be reproduced by real-rooted polynomial controls. XF-007 adds a spatial version near equilibrium: increasing the **derivative order** at one collision does not recover Xi-specific information, and keeping a **fixed number of neighboring gaps** near a high arithmetic-lattice regime does not carry fixed-time dynamical memory either. A viable fixed-time mechanism must let its spatial information content grow with height or use a genuinely nonperturbative/nonlocal observable.

The obstruction is intentionally perturbative. Nonlinear configurations with a large defect, rare close pair, higher-multiplicity event, or coherent structure outside the small-lattice regime are not controlled by the Fourier linearization. Nor is every abstract lattice perturbation asserted to come from a globally admissible Xi-type entire function. What is exact is the first variation of the actual zero-motion law wherever an arithmetic-lattice local model is legitimate.

## 6. Prior-art and novelty boundary

Rodgers and Tao, **The de Bruijn--Newman constant is non-negative**, *Forum of Mathematics, Pi* 8 (2020), e6, are the primary source for the zero ODE in the relevant real-simple regime and explicitly identify arithmetic progressions as local equilibria. Their proof also develops a renormalized energy and growing-window local-equilibrium mechanism. The Fourier-series evaluation used above is classical Bernoulli-polynomial theory.

No novelty is claimed for the zero ODE, arithmetic-progression equilibrium, Fourier diagonalization of translation-invariant convolution operators, or the Bernoulli identity. The Mathia-specific result is the exact combination of these ingredients with the `H_t` density normalization: the lattice symbol converts the previously observed `1/log^2 T` microscopic clock into a forced `log^2 T`-gap / `log T`-physical-window scale for order-one heat-time memory.

This should be treated as a structural scaling law, not a new theorem about the full nonlinear Xi flow. Its value is to rule out an entire class of perturbative local-equilibrium strategies before they are mistaken for fixed-time upper-bound mechanisms.

## 7. Consequence for `xi_flow`

XF-004 showed that an absolute minimum gap has only `O(1/log^2 T)` backward reach. XF-005 supplied the scale-free equilibrium coordinate `R`, and XF-006 ruled out finite local collision jets as Xi-specific selectors. The present result shows why simply replacing the absolute gap by a **bounded-radius normalized neighborhood around `R=2`** still does not solve the fixed-time problem: near lattice equilibrium, bounded-radius information relaxes on the same vanishing microscopic time scale.

The next serious upper-bound route should therefore target one of two genuinely stronger objects. Either it must control a mesoscopic block containing on the order of `log^2 T` gaps (physical length `log T`) with an observable that survives the infinite-system limit, or it must find a nonperturbative global statistic whose information is not mediated by linear relaxation around the arithmetic lattice. This gives a concrete scale at which inputs from `analytic_frontier` would have to couple to the Xi-flow dynamics rather than merely constraining one or a few normalized gaps.