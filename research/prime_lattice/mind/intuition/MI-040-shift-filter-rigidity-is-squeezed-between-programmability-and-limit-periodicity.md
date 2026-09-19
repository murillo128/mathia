# MI-040 — Shift-filter rigidity is squeezed between programmability and limit-periodicity

**Evidence level:** exact synthesis from [PL-363](../../findings/PL-363-finite-signed-lattice-filter-crosses-positive-convergence-wall-but-does-not-select-critical-line.md) through [PL-365](../../findings/PL-365-l1-shift-filter-limit-periodic-collapse.md), using classical Möbius inversion and Wiener--Dirichlet control as audited there.

Signed multiplicative-shift filtering has three sharply different regimes, and none of the obvious ones supplies critical-line selectivity.

For finite support, PL-363 shows that the coefficient-one source is sent to a periodic divisor-filter sequence. Cancelling the mean produces ordinary Dirichlet convergence on `Re(s)>0`, but the result is just

`B(s)=P(s)zeta(s)`

with a finite Dirichlet polynomial `P`. The continuation is classical periodic/Hurwitz continuation, and any extra zeros belong to the chosen filter rather than to an arithmetic selector.

At the opposite extreme, PL-364 removes every analytic restriction from an infinite fixed filter. The coefficient map is exactly

`c -> b=c*1`.

Because convolution by `1` is inverted by Möbius convolution, `c=mu*b`, this class can program **every** arithmetic output sequence. Infinite signed support is therefore not a richer rigid model of the prime lattice; without an independently imposed admissible class it is an output oracle in coefficient coordinates.

PL-365 inserts the first natural analytic restriction between those extremes: `c in ell^1`. The filter then converges in operator norm, so arbitrary programmability disappears. But the output has another rigid collapse: it is uniformly limit-periodic because finite divisor-filter truncations approximate it uniformly. Moreover

`sum_(n<=x)b_n=x C(1)+O(||c||_1)`.

If `C(1)=0`, every nonzero output has exact ordinary and absolute convergence abscissae

`sigma_c=0`, `sigma_a=1`.

Thus the first bounded-operator restriction does not reveal a hidden half-plane boundary at `1/2`; it reproduces the same `0/1` convergence geometry already present in the finite periodic case.

The reusable lesson is that **filter complexity is non-monotone with arithmetic rigidity**. More support can move a class from a classical finite continuation to complete coefficient programmability; imposing a strong norm can restore rigidity while collapsing the outputs into a universal almost-periodic class that still has no critical selector. The relevant question is not how many shifts are allowed but what source-native law restricts their coefficients and what invariant survives that restriction.

A viable intermediate shift construction must therefore pass two controls simultaneously. Its admissible coefficient family must be narrow enough that Möbius inversion cannot program arbitrary targets, yet rich enough that its outputs are not forced into the limit-periodic `sigma_c=0`, `sigma_a=1` class. In addition, the restriction itself must be motivated before the desired zeta output is chosen, and any zeros or continuation created by the filter must be separated from inherited zeta data.

**Boundary.** PL-365 treats the sufficient operator-norm condition `ell^1`, not the full multiplier algebra of the Dirichlet Hardy space, weighted `ell^2` classes, scale-dependent filters, distributional limits or non-coefficientwise operators. The source coefficient-one vector also remains outside the native `H^2` Hilbert space, so the arithmetic readout is coefficientwise. These untested classes are not promoted to mechanisms merely because they lie between the three audited regimes.
