# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, while NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun. NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale, and NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

The unresolved operator transition lies in the genuinely intermediate window `N<<m<=O(N^2)`: determine whether coherent centered shell modes survive there or whether the rank-one mixing picture can be pushed down to that scale. That source-side theorem is still not the destination theorem. Any useful singular direction must also be occupied by the actual moving first-free datum after the sampling/null decomposition, lower-section conditioning and off-critical contraction. Operator norm or support mass alone does not imply a Nyman target gain.

## Localize any remaining superquadratic Hilbert primitive amplification to superlinear reciprocal time

NB-316--NB-317 isolate the multiplicative loss in the centered primitive estimate. For the centered Cesàro shell factor `D_N`, NB-317 proves the sharp growth `||D_N||_2=Theta(N^(3/2))`; the first multiplicative factor is therefore not a loose coefficient-count artifact.

NB-318 shows that this sharp Cesàro exponent is already attained at reciprocal time `K=floor(N/2)`, but that the physical Hilbert norm prevents the two worst-case losses from being simultaneously saturated on any bounded linear reciprocal-time window. Writing `G_u(K)` for the centered primitive and `Q_N^0(u)` for the centered shell energy, NB-318 proves

`sup_(u!=0) |G_u(K)|/||u||_2 = O_C(N^2)`

uniformly for `K<=CN`, while at `K=floor(N/2)` the corresponding Cesàro-normalized evaluation is `Theta(N^(3/2))`. Thus a profile with `Q_N^0(u)=1` and primitive size `>>N^(3/2)` in a linear window must satisfy `||u||_2 >>_C N^(-1/2)`: the raw `sqrt(Q_N^0)/||u||_2=O(N)` comparison loses a half-power exactly where the primitive is large.

This closes the `N^(5/2)` versus `N^2` half-power gap on bounded linear reciprocal-time windows, but not globally. The adjacent witness from NB-316 reaches its exact primitive maximum at `K=Theta(N^2)` and still supplies the current global lower bound `Pi_N >> N^2/sqrt(log N)`. Therefore any genuinely superquadratic global Hilbert-normalized primitive amplification must come from reciprocal times with `K/N -> infinity`.

The live source question is to determine the Hilbert-normalized primitive norm in that **superlinear reciprocal-time window**, especially between linear and quadratic time, and decide whether `Pi_N=O(N^2)` or a larger scale is possible. A proof must keep the reciprocal-time incidence exposed rather than multiply independent worst-case shell and Hilbert bounds. Even a sharp source-side answer remains separate from target occupation, first-free gain and the final Nyman/RH destination.
