# MI-040 — Shift-filter critical walls can be manufactured by coefficient topology or canonical Hardy geometry

**Evidence level:** exact synthesis from [PL-363](../../findings/PL-363-finite-signed-lattice-filter-crosses-positive-convergence-wall-but-does-not-select-critical-line.md) through [PL-368](../../findings/PL-368-hardy-hp-filter-universal-half-wall.md), using classical Möbius inversion, Holder duality, Bohr--Bohnenblust--Hille/Bayart theory and Abel/Dirichlet-series control as audited there.

Signed multiplicative-shift filtering now has a sharply classified sequence of regimes, and none of the obvious ambient function classes supplies critical-line selectivity.

For finite support, PL-363 shows that the coefficient-one source is sent to a periodic divisor-filter sequence. Cancelling the mean produces ordinary convergence on `Re(s)>0`, but the result is just `B(s)=P(s)zeta(s)` with a finite Dirichlet polynomial `P`. At the opposite extreme, PL-364 removes every analytic restriction from an infinite fixed filter: `b=c*1` and Möbius inversion `c=mu*b` make the class fully programmable. PL-365 inserts `c in ell^1`; programmability disappears, but the outputs become uniformly limit-periodic with universal `sigma_c=0`, `sigma_a=1` after pole neutrality.

PL-366--PL-367 show how intermediate coefficient topology manufactures any desired critical-looking ordinary-convergence wall. For `1<p<infinity`, pole-neutral `c in ell^p` satisfies

`sum_(n<=x)b_n=O_p(x^(1-1/p)||c||_p)`,

and the exponent is sharp. As `p` varies, the wall fills `(0,1)`; the Hilbert value `1/2` is only the `p=2` point of a Holder/Banach continuum.

PL-368 supplies a complementary control rather than another point on that ladder. In the canonical scalar Hardy spaces of Dirichlet series `H^p`, every `1<=p<=infinity` has the same sharp absolute-convergence wall `Re(s)=1/2` by Bohr--Bohnenblust--Hille/Bayart theory. If `C(s)=sum c_d d^-s` lies in `H^p` and `C(1)=0`, the exact divisor residual gives

`sum_(n<=x)(c*1)(n)=O_(C,epsilon)(x^(1/2+epsilon))`.

Hence `B(s)=zeta(s)C(s)` is holomorphic on `Re(s)>1/2`, but any hypothetical zeta zero in that half-plane is simply inherited. The half-wall is therefore still not a selector. Vector-valued Hardy theory makes the calibration explicit: the wall becomes `1-1/Cot(X)`, with scalar `1/2` just the cotype-`2` case.

The reusable lesson is stronger than “the half exponent may be a norm artifact.” **A critical boundary can be ambient in two opposite ways.** Raw coefficient spaces can move it continuously by changing duality exponents, while a canonical analytic scale can pin it at `1/2` for every scalar `p` because monomial/Bohr geometry does so generically. Stability of the number `1/2` across a natural family is therefore not evidence of arithmetic rigidity if a matched ambient theorem already explains it and a Banach-valued deformation moves it.

A viable intermediate construction must pass both controls. Its admissible family must be narrow enough that Möbius inversion cannot program arbitrary targets; it must not collapse to periodicity or limit-periodicity; its critical boundary must not be explained by the `ell^p` ladder or generic Hardy/cotype geometry; and the extra restriction must be source-forced and imply a zero-sensitive relation that generic members of the same ambient class do not satisfy.

**Boundary.** PL-368 does not say that every structured Hardy-space or `ell^p` construction is useless. Additional multiplicative, functional-equation, positivity, trace, target-relative or non-coefficientwise identities could distinguish a source-native subclass. The no-go is that ambient norm/Hardy membership plus scalar pole neutrality can manufacture RH-shaped summatory or convergence behavior without selecting any zeta zeros.