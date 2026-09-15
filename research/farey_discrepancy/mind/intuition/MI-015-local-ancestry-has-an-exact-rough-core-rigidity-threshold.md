# MI-015 — Local ancestry has an exact rough-core rigidity threshold

**Evidence level:** exact finite-horizon classification from [FD-135](../../findings/FD-135-local-ancestry-rigidity-has-an-exact-rough-core-threshold.md), refining the averaged-ancestry escapes in `FD-130`--`FD-134`

For squarefree-unit sources `a_n in {±1}` anchored to Möbius on `omega(n)<=K`, impose exact ancestry `a_(pn)=-a_n` for every admissible prime edge with `p<=Y`. In the Möbius gauge `g(n)=mu(n)a_n`, these edges make `g` constant exactly on classes with the same `Y`-rough core `r_Y(n)`.

The rank-`K` anchor pins precisely the components whose rough core has at most `K` prime factors. The first free component is therefore the product

`Q_(K+1)(Y)=prod_(j=1)^(K+1) p_j^+(Y)`

of the first `K+1` primes above `Y`. Hence

`Q_(K+1)(Y)>H`

is equivalent to complete reconstruction `a_n=mu(n)` on `[1,H]`; if `Q_(K+1)(Y)<=H`, flipping that rough-core component gives an exact counterexample. The convenient sufficient threshold `Y^(K+1)>=H` already forces reconstruction.

There is no soft `L^infinity` regime in this unit-sign class. Every local defect `|a_(pn)+a_n|` is `0` or `2`, so `D_infinity(H,Y;a)<2` is already exact ancestry. A vanishing local supremum condition therefore crosses directly from permissive averaged control to component rigidity and, beyond the rough-core threshold, to full source recovery.

The reusable boundary is that **locality can eliminate dilution by becoming too rigid**. Mean ancestry misses a moving multiplicative-rank interface, but edgewise ancestry plus a finite rank anchor can reconstruct the whole horizon at a polynomial prime cutoff. A useful intermediate source law must retain the moving rank defect without silently collapsing to this exact rough-core reconstruction.

**Boundary.** This classification uses the squarefree unit-sign source class and exact/local ancestry. It does not show that an intermediate `L^p`, weighted, mesoscopic, or destination-side condition is coercive, and full source reconstruction is not itself progress on the Farey endpoint.