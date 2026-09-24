# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun, and NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale. NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

NB-316--NB-329 then show that the most obvious primitive, denominator and phase effects do not create a clean transition inside the subquadratic window. The centered Cesaro primitive has sharp `Theta(N^(3/2))` growth, exact divisor folds and the full lattice `m=d(n-1)` retain a canonical `1/sqrt(log n)` rank-one-error resonance, and moving one selector cell to `m=dn` flips the adjacent coefficient's sign. On the intermediate cell `m=d(n-1)+r`, `rho=r/d`, the outer adjacent coefficient is `(1-2rho)log 2/(4n)+O(d/n^2)`, so that particular channel vanishes at half drift.

NB-330 proves that this half-cell zero is only witness cancellation. Shifting the target inward by one adjacent mode produces a cell coefficient independent of `rho`, with

`F_(n,d,r)=-log(2)/(4(n-1))+O(d/(n-1)^2)`,

uniformly across the entire drift cell. Consequently every sequence `d_n=o(n)` retains the same logarithmic operator obstruction even at the outer witness's half-cell zero.

NB-331 removes the remaining gaps between those one-cell bands. The same intrinsic adjacent-index calculation works at any `8<=q<=n`: if `m=dq+r`, `0<=r<=d`, the `q`-adjacent witness has the same leading coefficient with error `O(d/q^2)`. For every integer sequence

`n <= m_n = o(n^2)`

one can choose an explicit adaptive inner index `q_n<=n` so that

`q_n <( (sqrt(m_n) T_(n,m_n)-R_n) g_2, nu_(q_n) ) -> -log(2)/4`

and therefore

`liminf sqrt(log n) ||sqrt(m_n)T_(n,m_n)-R_n|| >= sqrt(log 2)/(2 sqrt 2)`.

Thus there is **no faster-mixing external subquadratic window at the operator-norm level** detectable by escaping between the previous resonant lattices: every `n<=m=o(n^2)` carries an adaptive adjacent resonance of the same logarithmic scale. The bound still tends to zero, so it does not prove a fixed positive norm gap.

NB-332 now reaches a genuine part of the quadratic boundary. On the exact critical lattice `m=dq` with `d/q -> delta in (0,infinity)`, the adjacent coefficient has the explicit limit

`q F_(n;q,d) -> Phi(delta) = -(1/(4 delta)) sum_(k>=1) ||k delta||_Z^2/k^2`.

Hence `Phi(delta)<0` for every nonintegral aspect ratio and vanishes exactly at integer `delta`. Every fixed nonintegral ratio therefore retains a `1/sqrt(log q)` operator-norm obstruction even when `m asymp n^2` (for `q/n` bounded away from zero). The quadratic boundary is not a featureless disappearance of the subquadratic resonance: it carries an explicit Diophantine profile. The integer nodes are only zeros of this particular adjacent channel and are not evidence that the operator itself mixes there.

The source-side transition question is therefore narrower. Resolve the full critical profile when `d/q asymp 1` but the remainder phase `m=dq+r` is nonzero, and determine whether the integer zeros of `Phi` survive optimization over admissible witness indices or are routed around as the half-cell zero was in NB-330. Then connect that critical family to the superquadratic rank-one asymptotic without mistaking a moving lower bound of order `1/sqrt(log n)` for a nonzero limiting gap. On the destination side the older warning remains decisive: NB-330--NB-332 concern available source directions, not occupation by the actual moving first-free Ford datum. Any Nyman consequence must still pass the sampling/null decomposition, lower-section conditioning and off-critical contraction with the physical target source.
