# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, while NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun. NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale, and NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

The unresolved operator transition lies in the genuinely intermediate window `N<<m<=O(N^2)`: determine whether coherent centered shell modes survive there or whether the rank-one mixing picture can be pushed down to that scale. That source-side theorem is still not the destination theorem. Any useful singular direction must also be occupied by the actual moving first-free datum after the sampling/null decomposition, lower-section conditioning and off-critical contraction. Operator norm or support mass alone does not imply a Nyman target gain.

## Quantify the weighted mixing transition directly; the full exact-divisor skeleton carries logarithmic resonance from linear to subquadratic scales

NB-316--NB-318 isolate the multiplicative loss in the centered reciprocal-shell primitive estimate. The centered Cesaro shell factor has sharp `Theta(N^(3/2))` norm growth, and bounded linear reciprocal time admits an `O_C(N^2)` physical Hilbert evaluation bound even though the top-index adjacent witness reaches its largest primitive excursion only at quadratic time.

NB-326 closes the physical-normalization question for the **exact linear-time Cesaro Riesz extremizer** left by that analysis. After normalizing the centered Cesaro energy and reconstructing the generator coefficients by finite Möbius inversion, its physical Nyman norm satisfies `||u_N||_2^2=Theta(1)`, while `A_N(floor(N/2))=Theta(N^(3/2))`. Thus the Hilbert-normalized amplification of this exact extremizer remains `Theta(N^(3/2))`: transfer to the physical Nyman metric creates neither a polynomial loss nor the missing extra half-power. Any larger global primitive amplification must therefore use a different profile and/or an evaluation time escaping the bounded linear window. This is source-side and says nothing about actual first-free target occupation.

NB-319 removes the interpretation that the primitive obstruction is confined near the quadratic endpoint. For every `8<=M<=N^2/2`, nested adjacent cancellations give a Hilbert-normalized primitive lower bound within a square-root logarithm of linear growth on an annulus of radius `M`. No uniform power-saving primitive estimate can therefore hold across the full mesoscopic range.

NB-320--NB-322 then move to the actual signed `1/t^2` pairing. The weight suppresses the primitive obstruction by a full quadratic factor, but exact rational folds retain a `1/sqrt(log n)` rank-one-error resonance. On the canonical divisor subsequences `q|n` or `q|(n-1)`, NB-322 proves this while `q=o(sqrt n)`, giving explicit resonant scales `m=n^(alpha+o(1))` for every `3/2<alpha<=2`. These are absolute source-side operator errors tending to zero, not order-one target channels.

NB-323 reaches the opposite endpoint `q=n`, equivalently the linear dilation `m=n-1`, and again finds a Hilbert-normalized `Theta(1/sqrt(log n))` residue from an exact alternating-harmonic pulse calculation. This already shows that the `O(q^2/n^2)` remainder used in NB-322 cannot define an intrinsic transition near `q~sqrt n`.

NB-324 closes the intervening denominator-size gap for every growing **even** divisor `q|n`: if `m=n(n-1)/q`, the canonical matrix coefficient is `(H_q-H_(q/2))/(4n)+O(1/(nq))`, so `nE_(n,q)->(log 2)/4` with no restriction on the relative size of `q` and `n`.

NB-325 removes the remaining parity escape. For an odd divisor `q|n`, the selector no longer closes after one `n`-period, but it flips to its complement; over `2n` the product has exact zero mean. This gives

`E_(n,q)=(H_(q-1)-H_((q-1)/2))/(4n)+O(1/(nq))`.

Hence for **every** sequence of growing divisors `q_n|n`, regardless of parity or relative size, `nE_(n,q_n)->(log 2)/4` and the rank-one-subtracted operator retains a `1/sqrt(log n)` lower bound. Power-of-three subsequences show that purely odd denominators already realize every fixed power scale `m=n^(alpha+o(1))`, `1<=alpha<2`. The denominator-size and parity distinctions are therefore both artifacts on the exact divisor pulse train.

The live source question is now concentrated on **arithmetic geometry outside the exact divisor skeleton**. Determine what happens for nondivisors and near-rational ratios, where selector boundaries drift relative to the adjacent pulse train, and whether that drift can create enough cancellation for a uniform mixing theorem while still accommodating the exact-divisor resonances. A useful upper theorem cannot discriminate by denominator size or parity; it must exploit genuinely nondivisor arithmetic, cancellation unavailable to the adjacent witness, or another target-aware mechanism. NB-326 separately rules out hoping that the exact bounded-linear Cesaro extremizer acquires the missing amplification merely through conversion to the physical Nyman norm.

Even a complete source-side classification would remain separate from target occupation. The NB-324--NB-325 obstruction is a specific rank-one-subtracted matrix coefficient, and NB-326 is a source-side extremizer norm statement. Neither shows that the moving first-free Ford datum occupies the relevant direction, gives a finite-section excess, improves a Nyman approximation rate, or implies RH. Any destination claim must still pass the sampling/null decomposition, lower-section conditioning and off-critical contraction with the actual target source.
