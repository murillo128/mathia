# MI-010 — An actual off-critical zero is coordinate-small but collectively leverage-large after normalization

**Evidence level:** exact through [NB-092](../../findings/NB-092-growing-depth-mobius-annulus-mode-forces-polynomial-blaschke-gram-gain.md), [NB-093](../../findings/NB-093-single-zero-growing-depth-gram-gain-is-rank-one-causal-state-leverage.md), and [NB-094](../../findings/NB-094-zero-cancellation-keeps-coordinate-state-cost-bounded-while-leverage-grows.md) for one actual zero `rho=beta+i gamma` with `beta>1/2`. Multiple interacting zero states and any final Nyman-distance implication remain open.

Growing multiplicative depth exposes a genuine arithmetic near-kernel. On the band `m<=j<mq`, NB-092 constructs a canonical Möbius annulus whose raw Gram energy becomes small while an off-critical Blaschke factor repairs the same direction at scale `q^(2beta-1)`. NB-093 shows that for one zero this repair is exactly one causal-state rank-one update

`K_R^(rho)=A_R+s_R s_R^*`,

with inverse-Gram leverage `tau_(m,R)=s_R^*A_R^(-1)s_R`.

NB-094 resolves the diagonal-normalization ambiguity by using the zero condition itself. In the finite-cutoff state formula, `zeta(rho)=0` cancels the only large coordinate term. Uniformly for every `1<=j<R`,

`|s_(j,R)| <= C_rho R^(-1/2)`.

Since the raw diagonal is bounded below, the total coordinatewise normalization bill satisfies

`sum_(j=m)^(R-1) log(1+nu_(j,R)) = O_rho(1)`

for every band. This is not a generic all-pass fact: away from a zero the uncancelled `j^(1-w)` term prevents the same coordinate suppression.

At the same time the leverage has an exact orthogonal-cell formula and, for `R=mq`, obeys

`1+tau_(m,mq) asymp_rho q^(2beta-1)`.

Therefore the normalized correlation determinant keeps the whole exponent:

`log(det R_(m,mq)^(rho)/det R_tilde_(m,mq)) = (2beta-1) log q + O_rho(1)`.

This fixes both survival and sign. The state is tiny in every generator coordinate but large in the inverse-correlation geometry because the coordinates combine coherently along a near-kernel. **False RH appears here as a correlation-volume repair, equivalently a centered correlation-entropy deficit, not a positive entropy excess.**

The remaining difficulty is no longer normalization of one state. Several Blaschke factors create a finite/multiple-state update on successively deflated sources; the states can interact, and coordinate renormalization after one factor changes the geometry seen by the next. A valid multi-zero theorem must control that interaction directly rather than sum isolated one-zero formulas.

**Research consequence.** Treat `NB-094` as the closed single-zero bridge. Seek a finite-state or aggregate invariant whose normalized volume repair cannot be cancelled by interactions among off-critical zero states, or prove a monotonicity/interlacing law for the successive causal-state updates. Any target statistic must use the sign established here rather than expect a positive centered-entropy charge.

**Boundary.** The result does not prove that the full Burnol product has an additive exponent, does not show that the largest off-critical zero dominates after all other factors, and does not by itself lower-bound the Nyman distance. It proves that diagonal normalization alone cannot erase the polynomial one-zero signal.
