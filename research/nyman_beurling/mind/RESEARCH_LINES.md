# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, while NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun. NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale, and NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

The unresolved operator transition lies in the genuinely intermediate window `N<<m<=O(N^2)`: determine whether coherent centered shell modes survive there or whether the rank-one mixing picture can be pushed down to that scale. That source-side theorem is still not the destination theorem. Any useful singular direction must also be occupied by the actual moving first-free datum after the sampling/null decomposition, lower-section conditioning and off-critical contraction. Operator norm or support mass alone does not imply a Nyman target gain.

## Quantify the weighted mixing transition directly; growing rational denominators carry logarithmic resonances down to every exponent above `3/2`

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

The live source question is now narrower. Fixed denominators are no longer candidates for a cancellation escape on the canonical congruence subsequences, and the rational skeleton is not confined to `m asymp n^2`. The next discriminator is the actual `q`-dependence of the second-order folding error near and beyond `q asymp sqrt(n)`: determine whether cancellation improves the current `O(q^2/n^2)` bound enough to continue the logarithmic resonance toward the linear regime, or whether `q asymp sqrt(n)` marks a genuine `m asymp n^(3/2)` transition for this adjacent channel. Near-rational ratios not satisfying the exact divisibility geometry and genuinely irrational ratios remain separate questions.

Any useful upper theorem across `N<<m<=O(N^2)` must therefore accommodate explicit logarithmic resonances throughout `n^(3/2+epsilon)` to quadratic scales, while exploiting the actual `1/t^2` weight, reciprocal-shell phase cancellation, square-function/frequency structure or denominator arithmetic in the remaining regime. Even a sharp source-side mixing theorem remains separate from target occupation, first-free gain and the final Nyman/RH destination.
