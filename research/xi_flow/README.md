# Xi Flow

## Research mandate

### Primary object

The line studies the de Bruijn--Newman heat-flow deformation of the Riemann xi function. In the Rodgers--Tao normalization,

\[
H_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(zu)\,du,
\]

with a finite constant `Lambda` such that all zeros of `H_t` are real exactly for `t >= Lambda`. At `t=0`, real-rootedness is equivalent to the Riemann hypothesis; hence RH is equivalent to `Lambda <= 0`, while the proved Newman conjecture gives `Lambda >= 0`.

The intrinsic objects are therefore the zero configuration of `H_t`, its evolution with `t`, collisions and near-collisions, gap geometry, and global quantities that can be justified for this specific heat deformation.

### Objective

Find a source-faithful dynamical mechanism that constrains the transition time `Lambda` from above, ideally forcing `Lambda=0`, or obtain a new rigorous structural/quantitative obstruction to a positive transition time.

Intermediate progress should explain why the actual xi-flow zero configuration cannot follow a candidate positive-`Lambda` collision scenario, rather than merely re-expressing the equivalence between RH and the sign of `Lambda`.

### Priority questions

- Which exact zero-motion equations hold in the real-rooted regime, and do they admit monotone, convex, coercive, or conserved quantities that remain informative as `t` approaches `0`?
- Can unconditional spacing, pair-correlation, or higher-correlation information rule out the local equilibrium or collision geometry required by a hypothetical `Lambda>0`?
- Can Lehmer-type near-collisions be organized into a quantitative local-to-global statement about the transition, rather than used only as numerical evidence?
- Is there an energy, entropy, Lyapunov, discriminant, or gap functional whose behavior distinguishes the actual xi flow from matched real-entire heat flows with positive transition time?
- Can finite truncations or particle models provide a theorem-level invariant that survives a controlled infinite-system limit?
- Can the Rodgers--Tao contradiction mechanism be strengthened by replacing the currently used zero-statistical input with richer unconditional information?

### Scope and exclusions

This line owns the heat deformation, zero dynamics, collision geometry, and the de Bruijn--Newman constant. It does not own generic Hilbert--Polya constructions, compressed-Weil inertia certificates, or unrelated spectral analogies.

Do not extrapolate a zero-motion formula beyond the regime in which the relevant zeros are known to be real and simple. Numerical zero trajectories, finite particle simulations, or visually striking Lehmer pairs are not target results without a controlled stability or limiting argument. Do not assume RH to label, order, or statistically model the very zero configuration whose real-rootedness is at issue.

### Line-specific falsification controls

Any proposed dynamical invariant must be tested against matched even real-entire functions or synthetic zero systems whose heat deformation has a different transition time. If the invariant is shared by those controls, it is not a xi-specific selector.

Track collision singularities explicitly: a quantity that is monotone only while all gaps stay uniformly positive cannot by itself cross the first-collision boundary. For truncated or finite-dimensional models, require a topology and error estimate strong enough to preserve the claimed sign, coercivity, or non-collision property in the infinite limit.

When importing zero statistics, distinguish unconditional statements from RH-conditional versions and verify that the statistic remains meaningful for a hypothetical configuration containing nonreal zeros.

### Prior-art domains

- de Bruijn--Newman deformation and constants;
- dynamics of zeros under heat flow and real-entire/Laguerre--Polya theory;
- Rodgers--Tao and subsequent proofs/generalizations of Newman's conjecture;
- Csordas--Smith--Varga zero-dynamics methods and Lehmer-pair literature;
- Montgomery pair correlation and higher zero statistics when used without circular RH assumptions;
- interacting-particle, logarithmic-energy, and Calogero-type structures only where an exact dictionary with the xi flow is established.

### Relationship to other lines

`analytic_frontier` is a natural upstream source of unconditional zero-density, spacing, and correlation estimates that may constrain xi-flow dynamics. `weil_inertia` also uses zero statistics but owns the compressed Weil form and rank/inertia certificates; a bridge discovered here should be handed off rather than duplicating that machinery.

`visual_exploration` can probe zero trajectories, gap evolution, collision patterns, and candidate energies as clue-generating diagnostics, but any durable xi-flow claim remains owned and proved here.