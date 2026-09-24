# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, while NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun. NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale, and NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

The unresolved operator transition lies in the genuinely intermediate window `N<<m<=O(N^2)`: determine whether coherent centered shell modes survive there or whether the rank-one mixing picture can be pushed down to that scale. That source-side theorem is still not the destination theorem. Any useful singular direction must also be occupied by the actual moving first-free datum after the sampling/null decomposition, lower-section conditioning and off-critical contraction. Operator norm or support mass alone does not imply a Nyman target gain.

## Quantify the weighted mixing transition directly; primitive-sup power savings and polynomial quadratic-rate mixing are both excluded

NB-316--NB-318 isolate the multiplicative loss in the centered reciprocal-shell primitive estimate. The centered Cesaro shell factor has sharp `Theta(N^(3/2))` norm growth, and bounded linear reciprocal time admits an `O_C(N^2)` physical Hilbert evaluation bound even though the top-index adjacent witness reaches its largest primitive excursion only at quadratic time.

NB-319 removes the interpretation that this primitive obstruction is confined near the quadratic endpoint. For every `8<=M<=N^2/2`, nested adjacent cancellations with index `n=floor(sqrt(2M))` give an exact evaluation inside the annulus `[M,3M]` with

`H_N(M) >= M/(32 sqrt(log M))`,

where `H_N(M)` is the Hilbert-normalized supremum of the centered primitive over that annulus. Thus every mesoscopic reciprocal annulus up to the quadratic frontier contains a source direction whose primitive is within a square-root logarithm of linear growth in the annulus radius. No uniform estimate `sup_(M<=T<=3M)|G_u(T)| <= C M^(1-epsilon)||u||_2` can hold across this range for fixed `epsilon>0`.

NB-320 shows that the actual signed `1/t^2`-weighted bilinear pairing behaves much better than that primitive envelope on the canonical adjacent witness, but not polynomially better. For even `n`, with

`u_n=g_n-((n-1)/n)g_(n-1)`

and resonant half-period dilation `m_n=n(n-1)/2`, one has

`< (sqrt(m_n)T_(n,m_n)-R_n)g_2, u_n > = pi^2/(64(n-1))+O(n^(-2))`.

Since `||u_n||_2=Theta(sqrt(log n)/n)`, the Hilbert-normalized coefficient is `Theta(1/sqrt(log n))`, hence

`||sqrt(m_n)T_(n,m_n)-R_n|| >> 1/sqrt(log n)`

along this quadratic sequence. The weight suppresses the primitive obstruction by a full quadratic factor, confirming that primitive-sup control was genuinely wasteful, but the surviving resonance forbids any uniform `O(n^(-delta))` rank-one error rate for fixed `delta>0` along these dilations. Because the lower bound still tends to zero, this is a rate obstruction, not a non-mixing theorem.

The live source question is therefore to **characterize the weighted bilinear mixing error itself across `N<<m<=O(N^2)` at the correct subpower scale**. A useful upper theorem must exploit the actual weight, cancellation between reciprocal-shell phases, square-function/frequency structure or reduced-denominator arithmetic, while accommodating the NB-320 half-period resonances rather than majorizing them by a primitive maximum. It remains open whether the quadratic corridor admits a uniform logarithmic/subpower rank-one mixing law, which other resonant families saturate it, and where the transition to the far-external NB-315 regime occurs. Even a sharp source-side mixing theorem remains separate from target occupation, first-free gain and the final Nyman/RH destination.
