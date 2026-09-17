# MI-027 — Odd reflection reverses the threshold Archimedean remainder into a Hopf-favorable source

**Evidence level:** exact/literature synthesis from [PL-324](../../findings/PL-324-odd-threshold-beurling-deny-persists-to-first-prime.md), [PL-333](../../findings/PL-333-threshold-archimedean-remainder-reverses-the-hopf-sign.md), and [PL-335](../../findings/PL-335-odd-threshold-antisymmetric-hopf-noncollapse.md).

The fixed first-prime threshold `a_0=(1/2)log 2` has opposite Hopf geometry on globally nonnegative and odd states. PL-333 shows that the completed Archimedean remainder has the wrong forcing sign for an ordinary positive-state logarithmic-Laplacian Hopf argument. PL-335 shows that odd reflection reverses exactly that remainder.

Writing `q=-r''`, the completed Archimedean kernel is strictly increasing on the whole threshold range `[0,log 2]`. For an odd threshold ground state chosen nonnegative on `(0,1)`, folding the remainder against the reflected negative half gives

`K_0 u(x)=a_0 int_0^1 [q(a_0|x-y|)-q(a_0(x+y))]u(y)dy < 0`.

Thus the threshold equation becomes a logarithmic-Laplacian **supersolution** on the positive half interval. The antisymmetric strong maximum principle and Hopf lemma then force

`liminf_(Q->infinity) sqrt(Q) u_0(1-2e^(-Q)) > 0`.

So the canonical half-log boundary amplitude cannot collapse on the lowest odd threshold branch. Whenever the matched boundary quotient exists, its coefficient `C_0` is strictly positive. The fixed-threshold nonvanishing gate is therefore closed in the RH-relevant odd sector without asserting positivity preservation of the full completed operator.

The reusable point is that parity can change the sign of a nonlocal completed remainder through **kernel comparison with the reflected point**, even when the same remainder destroys a global Markov/Hopf argument. Principal-form positivity and state-specific antisymmetric maximum principles are different resources.

**Boundary.** This does not prove post-threshold order positivity or the branchwise first-prime sign. PL-329 still requires a uniform source/remainder estimate as `a` approaches `a_0` from above. The mechanism is specific to the odd ground sector and the exact monotonicity of Suzuki's threshold Archimedean kernel.