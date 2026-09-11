# MI-004 — A conditioned source-faithful skeleton can still hide an RH-critical target oracle

**Evidence level:** proved

## Core intuition

A useful Nyman compression can quotient a large moving-tail nuisance sector while preserving source coordinates and quantitative conditioning. But representation quality, target loss, scalar source access, projected target geometry, and oracle cost are distinct mathematical gates.

The weighted tail-shell skeleton makes the separation sharp. Its source-faithful quotient has an intrinsic `Theta(1/M)` target-loss floor; one extra target-selected direction removes that loss exactly; the corresponding scalar coordinate has an explicit shrinking Möbius dual; but pushing that dual to its natural square-root norm floor is already RH-equivalent.

## Strongest justified claim

NB-031--NB-034 construct the weighted tail-shell quotient. It preserves low canonical coefficients, compresses the ordinary tail to one weighted scalar, and has polynomial conditioning uniformly in the original section size `N`. NB-037--NB-038 show that its upper-section correction is forced at order `d_N^2` and carries a multiplicatively accurate copy of the original distance in an explicit Möbius/Vasyunin direction.

NB-039 proves that the target loss is sharply `Theta(1/M)` for `N>=2M`, with multiplicative preservation exactly above the inverse-distance scale `M d_N^2 -> infinity`.

NB-040 shows that this loss is not a dimension lower bound. Retaining one additional direction gives an exactly zero-loss `M`-dimensional quotient with `N`-uniform polynomial conditioning. The unique repair direction is precisely `P_W e`, the weighted-tail projection of the target. Exact compression therefore isolates the target oracle into one rank-one geometry rather than eliminating it.

NB-041 separates the scalar and geometric parts of that oracle. It constructs an explicit ambient Möbius dual `Omega_M` whose pairings recover the logarithmic tail coordinate and whose norm satisfies `||Omega_M||=O(1/log M)`. For the optimal coefficients the scalar is source-locked up to `O(d_N/log M)`, uniformly in `N`. Yet projecting `Omega_M` onto the tail reproduces the same target-selected line `P_W e`.

NB-042 identifies the sharp endpoint of the norm route:

`RH  <=>  ||Omega_M||=O_epsilon(M^(-1/2+epsilon)) for every epsilon>0`.

The unavoidable support contribution `M^(-1/2)` is therefore the RH-critical exponent. Improving the ambient dual all the way to that floor is not a cheaper estimate hidden behind better PNT constants. A norm-only argument at this scale also fails to give `o(1/log N)` uniformly for every cutoff with merely `M/log N -> infinity`.

## Synthesis of evidence

The weighted skeleton succeeds as a representation theorem precisely because it exposes where the original difficulty returns. The discarded tail recursively contains the Nyman problem, the reduced Gram correction carries `d_N^2`, exact target repair is a target projection, and the most natural explicit dual has an RH-equivalent critical norm scale.

The remaining opening is directional rather than ambient: an arithmetic identity might estimate the particular projected repair direction or one-sided target functional more cheaply than controlling the whole dual norm or the full Nyman distance. A materially different quotient could also change the target-loss floor. Better conditioning of the same skeleton cannot.

## Counterevidence / boundary cases

NB-039--NB-042 are specific to the current weighted quotient and its explicit logarithmic dual. They do not prove circularity of every possible target certificate or every alternative nuisance subspace.

The RH equivalence concerns near-square-root decay of the **full ambient norm** `||Omega_M||`. It does not rule out a cheaper directional correlation estimate sufficient for one target quadratic form. Likewise the exact rank-one repair of NB-040 is target-aware; it is not a source-only construction.

## Epistemic status

**Exact compression/oracle boundary:** the weighted source skeleton is conditioned, its source-only target loss is sharply `Theta(1/M)`, exact repair is uniquely target-selected, its logarithmic scalar admits an explicit shrinking source dual, and near-square-root decay of that dual is RH-equivalent.

## Novelty/prior-art status

No broad novelty claim is made beyond the finding-level audits. Vasyunin, Burnol, Bagchi, classical Möbius criteria, and Mellin-transform ingredients retain their recorded prior-art status.

## Falsification criterion

Invalidate the sharp dilation loss of NB-039, the rank-one uniqueness statement of NB-040, the dual identities of NB-041, or the RH equivalence of NB-042. Strategically, construct a source-derived projected repair or one-sided target certificate at the required accuracy whose proof neither assumes an RH-equivalent estimate nor reconstructs equivalent finite-distance information; that would materially improve the current boundary without falsifying its existing exact statements.