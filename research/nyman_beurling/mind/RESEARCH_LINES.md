# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun, and NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale. NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

The unresolved operator transition therefore remains in the genuinely intermediate window `N<<m<=O(N^2)`: determine the singular geometry there rather than infer it from endpoint models. Even a complete source-side theorem is not yet the destination theorem. Any useful singular direction must be occupied by the actual moving first-free datum after the sampling/null decomposition, lower-section conditioning and off-critical contraction; operator norm or support mass alone does not imply a Nyman target gain.

## Separate adjacent-witness phase cancellation from genuine operator mixing

NB-316--NB-326 show that the most obvious primitive and weighted estimates do not produce a clean scale transition inside the subquadratic window. The centered Cesaro primitive has sharp `Theta(N^(3/2))` growth, the exact bounded-linear Cesaro extremizer retains that scale after conversion to the physical Nyman norm, and the actual `1/t^2` pairing suppresses primitive growth but leaves a canonical `1/sqrt(log n)` rank-one-error resonance on exact rational folds.

NB-322--NB-325 progressively remove the apparent denominator-size and parity thresholds on the exact divisor skeleton. For growing divisors `q|n`, the adjacent cancellation gives `n E_(n,q)->(log 2)/4` regardless of the relative size or parity of `q`, so exact divisor folds realize the same logarithmic resonance at every fixed power scale `m=n^(alpha+o(1))`, `1<=alpha<2`.

NB-327 shows that divisibility itself is not the sustaining mechanism. For every integer `d>=1`, with no relation `d|n`, the lattice

`m^-_(n,d)=d(n-1)`

satisfies

`E^-_(n,d)=log(2)/(4n)+O(d/n^2)`.

Hence every sequence `d_n=o(n)` retains the same `1/sqrt(log n)` operator-norm obstruction, including every fixed subquadratic power scale. The mechanism is cellwise centering rather than a common global period.

NB-328 moves one full selector cell to the neighboring lattice `m^+_(n,d)=dn` and finds the same magnitude with opposite sign. NB-329 resolves the entire intermediate cell for the same adjacent witness. Writing

`m=d(n-1)+r`, `rho=r/d in [0,1]`,

the weighted coefficient obeys

`E_(n,d,r)=(1-2rho) log(2)/(4n)+O(d/n^2)`

uniformly, so for `d=o(n)` the two endpoint resonances are one affine phase law. At half-cell drift `rho=1/2`, the leading adjacent coefficient cancels exactly cell by cell and `n E_(n,d,r)->0`; away from half drift the logarithmic operator-norm lower bound survives with factor `|1-2rho|`.

This identifies a genuine **witness-level cancellation window**, but not an operator transition. NB-329 does not show that the optimized norm becomes small at half drift; another source direction may remain resonant there. The live source-side question is therefore to test `rho=1/2` and its shrinking neighborhoods against optimized or structurally independent witnesses. If the operator norm remains logarithmically large, the adjacent zero is only channel cancellation. If a norm-level upper estimate emerges, the theorem must explain why all competing resonant directions are simultaneously suppressed rather than merely why one coefficient crosses zero.

A useful mixing theorem can no longer rely on denominator size, parity, divisibility, leaving one resonant lattice, or the sign of this adjacent channel. The relevant transition, if one exists, must be an operator-level property of the half-drift geometry or another exact off-lattice mechanism.

The resonance remains source-side. NB-327--NB-329 do not show that the moving first-free Ford datum occupies these directions, do not produce a finite-section excess or a Nyman approximation rate, and have no RH consequence by themselves. Any destination claim must still pass the sampling/null decomposition, lower-section conditioning and off-critical contraction with the actual target source.
