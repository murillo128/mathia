# MI-077 — Factor multiplicity does not survive a Möbius-sign projection

**Evidence level:** exact combinatorial synthesis from [MC-425](../../findings/MC-425-growing-factor-depth-does-not-create-polynomial-mobius-sign-channels.md), following the state-count bounds of MC-423--MC-424. This is a source-channel obstruction, not a cancellation theorem for richer factor data.

A large family of ordered factorizations is not automatically a large family of arithmetic source states. For squarefree `n`, an active factorization `n=u_1...u_d` partitions the prime factors of `n` into labeled blocks. If the construction retains from each block only `mu(u_j)`, then each coordinate remembers only the parity of the block size.

At depth `d`, all sign vectors lie in one parity hyperplane and there are at most `2^(d-1)` of them. Summing over every arithmetically possible active depth still gives fewer than `2^omega(n)` source-sign vectors. Since `omega(n)=O(log X/log log X)` for `n<=X`, the total sign-state family is only

`X^(o(1))`.

This remains true even when depth grows to its arithmetic maximum. Hence a factor lift can have polynomially many raw tuple states while exposing only subpolynomially many distinct Möbius-sign channels. **State multiplicity must be counted after projecting to the source information the mechanism actually uses.** Unit slots, factor labels and tuple multiplicity are not independent arithmetic bandwidth if the source phase identifies them.

The practical first-kill test is therefore to remove unit padding and project every active factor to its retained arithmetic datum before crediting any factor-state gain. A sign-only projection cannot supply a fixed polynomial channel exponent. A surviving growing-depth construction must justify richer retained information—sizes, residues, characters, additive phases, intrinsic relations—or obtain analytic leverage from correlations inside the subpolynomial sign family.

**Boundary.** MC-425 does not rule out growing-depth lifts carrying richer factor data, signed analytic cancellation, source-dependent weights or canonical labels beyond Möbius sign. It also does not say that a subpolynomial channel family is analytically useless. The exact obstruction is to deriving polynomial source complexity from raw factor multiplicity when the retained coordinate state is only `mu(u_j)`.