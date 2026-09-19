# MI-040 — Shift-filter rigidity is squeezed between programmability, periodicity and generic Hilbert criticality

**Evidence level:** exact synthesis from [PL-363](../../findings/PL-363-finite-signed-lattice-filter-crosses-positive-convergence-wall-but-does-not-select-critical-line.md) through [PL-366](../../findings/PL-366-l2-pole-neutral-filter-square-root-no-go.md), using classical Möbius inversion and Dirichlet-series Hilbert control as audited there.

Signed multiplicative-shift filtering now has four sharply different regimes, and none of the obvious ones supplies critical-line selectivity.

For finite support, PL-363 shows that the coefficient-one source is sent to a periodic divisor-filter sequence. Cancelling the mean produces ordinary convergence on `Re(s)>0`, but the result is just `B(s)=P(s)zeta(s)` with a finite Dirichlet polynomial `P`. The continuation is classical periodic/Hurwitz continuation, and extra zeros belong to the chosen filter.

At the opposite extreme, PL-364 removes every analytic restriction from an infinite fixed filter. The coefficient map is exactly `c -> b=c*1`, and Möbius inversion gives `c=mu*b`. This class can therefore program every arithmetic output sequence. Infinite signed support is not a richer rigid model unless its admissible law is fixed independently of the desired target.

PL-365 inserts the first natural analytic restriction: `c in ell^1`. Arbitrary programmability disappears, but the output is uniformly limit-periodic and satisfies

`sum_(n<=x)b_n=x C(1)+O(||c||_1)`.

When `C(1)=0`, every nonzero output has `sigma_c=0` and `sigma_a=1`. The first bounded-operator restriction restores rigidity only by collapsing the outputs into a universal almost-periodic class.

PL-366 enlarges to the Hilbert class `c in ell^2`. Now `C(1)=sum c_d/d` is automatically defined, and pole neutrality gives

`sum_(n<=x)b_n=O(sqrt(x)||c||_2)`.

The exponent `1/2` comes directly from Cauchy--Schwarz against the floor-function residual, whose `ell^2` norm is `O(sqrt x)`. The output Dirichlet series consequently converges on `Re(s)>1/2`, and bounded Dirichlet-Hardy multipliers fall inside this regime. This is closer in appearance to RH than the `ell^1` case but weaker as arithmetic evidence: the critical exponent is guaranteed for the entire pole-neutral Hilbert class, independently of zeta's zero geometry.

The reusable lesson is that **filter complexity is non-monotone with arithmetic rigidity, and a critical exponent can itself be a norm artifact**. More support can move from a classical finite continuation to complete coefficient programmability; imposing a strong norm can recover rigidity but produce universal periodic or Hilbert-space thresholds. A half-density is not selective merely because it appears canonically in the ambient function space.

A viable intermediate construction must therefore pass three controls simultaneously. Its admissible coefficient family must be narrow enough that Möbius inversion cannot program arbitrary targets; its output class must not collapse to a generic periodic/Hilbert threshold; and the restriction that distinguishes it must be source-forced and imply a zero-sensitive relation that generic members of the same norm class do not satisfy.

**Boundary.** PL-366 does not say that every structured `ell^2` or bounded-multiplier construction is useless. Additional multiplicative, functional-equation, positivity, trace, target-relative or non-coefficientwise identities could still distinguish a source-native subclass. The no-go is specifically that `ell^2`/multiplier regularity plus the scalar condition `C(1)=0` already manufactures square-root cancellation and the half-plane `Re(s)>1/2`, so those facts alone cannot be credited as RH rigidity.
