# MI-040 — Shift-filter rigidity is squeezed between programmability, periodicity and a manufactured Banach abscissa ladder

**Evidence level:** exact synthesis from [PL-363](../../findings/PL-363-finite-signed-lattice-filter-crosses-positive-convergence-wall-but-does-not-select-critical-line.md) through [PL-367](../../findings/PL-367-lp-filter-abscissa-ladder.md), using classical Möbius inversion, Holder duality and Abel/Dirichlet-series control as audited there.

Signed multiplicative-shift filtering now has a sharply classified sequence of regimes, and none of the obvious norm classes supplies critical-line selectivity.

For finite support, PL-363 shows that the coefficient-one source is sent to a periodic divisor-filter sequence. Cancelling the mean produces ordinary convergence on `Re(s)>0`, but the result is just `B(s)=P(s)zeta(s)` with a finite Dirichlet polynomial `P`. The continuation is classical periodic/Hurwitz continuation, and extra zeros belong to the chosen filter.

At the opposite extreme, PL-364 removes every analytic restriction from an infinite fixed filter. The coefficient map is exactly `c -> b=c*1`, and Möbius inversion gives `c=mu*b`. This class can therefore program every arithmetic output sequence. Infinite signed support is not a richer rigid model unless its admissible law is fixed independently of the desired target.

PL-365 inserts the first natural analytic restriction: `c in ell^1`. Arbitrary programmability disappears, but the output is uniformly limit-periodic and satisfies `sum_(n<=x)b_n=x C(1)+O(||c||_1)`. When `C(1)=0`, every nonzero output has `sigma_c=0` and `sigma_a=1`. Strong norm control restores rigidity only by collapsing the outputs into a universal almost-periodic class.

PL-366 then enlarges to `ell^2`. Pole neutrality gives `sum_(n<=x)b_n=O(sqrt(x)||c||_2)` by Cauchy--Schwarz against the floor-function residual. The output series converges on `Re(s)>1/2`; bounded Dirichlet-Hardy multipliers are included. The apparent RH exponent is therefore guaranteed for the entire pole-neutral Hilbert class, independently of zeta's zero geometry.

PL-367 proves the Hilbert value is one point on a full ambient ladder. For `1<p<infinity`, with conjugate `q=p/(p-1)` and `theta=1/q=1-1/p`, every pole-neutral `c in ell^p` satisfies

`sum_(n<=x)b_n=O_p(x^theta ||c||_p)`.

This exponent is sharp: there are explicit pole-neutral filters in `ell^p` whose output has ordinary abscissa exactly `theta`. As `p` varies, `theta` fills `(0,1)`. One can therefore manufacture **any** desired convergence wall between zero and one by selecting the ambient coefficient topology; `p=2` gives the sharp half-plane `Re(s)>1/2` only because Hilbert duality chooses `theta=1/2`.

The reusable lesson is stronger than “the half exponent may be a norm artifact.” **A whole continuum of critical-looking abscissae is an ambient Banach artifact.** Filter complexity is non-monotone with arithmetic rigidity: more support can give programmability, strong norm restriction can give universal almost periodicity, and intermediate `ell^p` geometry can place a sharp convergence boundary wherever its Holder conjugacy dictates.

A viable intermediate construction must therefore pass three controls simultaneously. Its admissible coefficient family must be narrow enough that Möbius inversion cannot program arbitrary targets; its output class must not collapse to periodicity or a generic `ell^p` abscissa; and the restriction that distinguishes it must be source-forced and imply a zero-sensitive relation that generic members of the same norm class do not satisfy. In particular, the critical line must remain distinguished after comparison with the entire `ell^p` ladder rather than being selected by choosing `p=2`.

**Boundary.** PL-367 does not say that every structured `ell^p`, `ell^2` or bounded-multiplier construction is useless. Additional multiplicative, functional-equation, positivity, trace, target-relative or non-coefficientwise identities could still distinguish a source-native subclass. The no-go is specifically that ambient coefficient topology plus scalar pole neutrality can manufacture both the summatory exponent and the ordinary convergence boundary, including the RH-shaped value `1/2`, without selecting any zeta zeros.
