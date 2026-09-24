# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, while NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun. NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale, and NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

The unresolved operator transition lies in the genuinely intermediate window `N<<m<=O(N^2)`: determine whether coherent centered shell modes survive there or whether the rank-one mixing picture can be pushed down to that scale. That source-side theorem is still not the destination theorem. Any useful singular direction must also be occupied by the actual moving first-free datum after the sampling/null decomposition, lower-section conditioning and off-critical contraction. Operator norm or support mass alone does not imply a Nyman target gain.

## Quantify the weighted mixing transition directly; logarithmic resonances reach both quadratic and linear rational scales

NB-316--NB-318 isolate the multiplicative loss in the centered reciprocal-shell primitive estimate. The centered Cesaro shell factor has sharp `Theta(N^(3/2))` norm growth, and bounded linear reciprocal time admits an `O_C(N^2)` physical Hilbert evaluation bound even though the top-index adjacent witness reaches its largest primitive excursion only at quadratic time.

NB-319 removes the interpretation that this primitive obstruction is confined near the quadratic endpoint. For every `8<=M<=N^2/2`, nested adjacent cancellations with index `n=floor(sqrt(2M))` give an exact evaluation inside the annulus `[M,3M]` with

`H_N(M) >= M/(32 sqrt(log M))`,

where `H_N(M)` is the Hilbert-normalized supremum of the centered primitive over that annulus. Thus every mesoscopic reciprocal annulus up to the quadratic frontier contains a source direction whose primitive is within a square-root logarithm of linear growth in the annulus radius. No uniform estimate `sup_(M<=T<=3M)|G_u(T)| <= C M^(1-epsilon)||u||_2` can hold across this range for fixed `epsilon>0`.

NB-320 shows that the actual signed `1/t^2`-weighted bilinear pairing behaves much better than that primitive envelope on the canonical adjacent witness, but not polynomially better. For even `n`, with

`u_n=g_n-((n-1)/n)g_(n-1)`

and resonant half-period dilation `m=n(n-1)/2`, one has a Hilbert-normalized rank-one error of order `1/sqrt(log n)`. The weight suppresses the primitive obstruction by a full quadratic factor, confirming that primitive-sup control was genuinely wasteful, but the surviving resonance forbids any uniform `O(n^(-delta))` rank-one error rate for fixed `delta>0` along these dilations.

NB-321 shows that the half-period point is not isolated. Writing `P_n=n(n-1)`, every fixed rational quadratic scale `m=P_n/q` admits a finite rational-period boundary reduction in terms of centered-primitive samples on the `q`-grid of one adjacent period. The `q=4` calculation gives another explicit `1/sqrt(log n)` obstruction, but NB-321 by itself leaves open cancellation for other fixed denominators and does not control the remainder uniformly when `q` grows.

NB-322 removes both limitations on the two canonical congruence subsequences `q|n` or `q|(n-1)`. The first boundary term collapses to the alternating residue coefficient

`C_q=sum_(k>=1) (-1)^k phi_q(k)/k^2`, `phi_q(k)=r(q-r)`, `r=k mod q`,

and `C_q<0` for every `q>=2`, with the uniform lower bound `|C_q|>=q/10`. The exact folding remainder is bounded by `O(q^2/n^2)`. Consequently, whenever `q=q_n=o(sqrt(n))` divides `n` or `n-1`, the adjacent witness still forces

`||sqrt(m_(n,q))T_(n,m_(n,q))-R_n|| >> 1/sqrt(log n)`,

with `m_(n,q)=n(n-1)/q`. Thus exact rational folding supplies logarithmic rank-one-error obstructions at explicit scales `m=n^(alpha+o(1))` for every fixed `3/2<alpha<=2`. These are absolute source-side operator errors tending to zero, not order-one channels and not target-occupation statements.

NB-323 shows that the `q=o(sqrt n)` range is not an intrinsic endpoint of the same adjacent resonance. At the opposite extreme `q=n`, equivalently the linear dilation `m=n-1` along even `n`, the exact weighted matrix coefficient satisfies

`< (sqrt(n-1)T_(n,n-1)-R_n)g_2, u_n > = (H_n-H_(n/2))/(4n) + O(n^(-2))`

and therefore its Hilbert-normalized size is again `Theta(1/sqrt(log n))`. The leading term comes from an exact one-period alternating-harmonic pulse calculation, while all later periods contribute only `O(n^(-2))`. Thus the `O(q^2/n^2)` absolute remainder used in NB-322 is not describing the actual maximal-denominator endpoint, and `q~sqrt n` cannot be declared a genuine resonance cutoff from that estimate alone. NB-323 is one explicit matrix coefficient at `q=n`; it does not prove uniform persistence across the whole intermediate denominator range.

The live source question is now the **intermediate-denominator geometry**. The same adjacent channel has logarithmic rank-one-error resonances for every fixed exponent above `3/2` through NB-322 and again at the linear endpoint through NB-323, so the unresolved issue is whether the resonance persists, oscillates or undergoes narrower cancellations for `sqrt(n)<<q<<n`. This requires a sharper signed analysis than the absolute second-primitive remainder, ideally resolving the actual `q`-dependence of the rational-period boundary terms and tails. Near-rational ratios not satisfying the exact divisibility geometry and genuinely irrational ratios remain separate questions.

Any useful upper theorem across `N<<m<=O(N^2)` must therefore accommodate explicit logarithmic resonances at both the previously established `n^(3/2+epsilon)`-to-quadratic scales and the linear edge. It must exploit the actual `1/t^2` weight, reciprocal-shell phase cancellation, square-function/frequency structure or denominator arithmetic rather than a monotone interpolation of the current absolute remainder. Even a sharp source-side mixing theorem remains separate from target occupation, first-free gain and the final Nyman/RH destination.
