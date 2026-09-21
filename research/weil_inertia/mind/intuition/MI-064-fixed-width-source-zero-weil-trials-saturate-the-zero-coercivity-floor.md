# MI-064 — Fixed-width source-zero Weil trials saturate the zero coercivity floor

**Evidence level:** exact explicit-formula/operator synthesis from [WI-385](../../findings/WI-385-fixed-width-source-zero-weil-trials-saturate-at-zero.md), closing the fixed-width direct-repair question left by WI-384. The Guinand--Weil explicit formula is classical; the line-specific content is the exact normalization and its application to the admitted source-zero family.

WI-384 leaves, under RH, the arithmetic-plus-polar floor `-A_L-2R_L(1)`. WI-385 shows that this scalar is not an independent repair reserve. Restoring the matching archimedean block and using the explicit formula gives

`A_L + 2R_L(1) = 2 B_L`,

where `B_L` is the one-lobe limiting archimedean energy. For the actual WI-380 profile, `B_L<0`, so the arithmetic-plus-polar layer does contain a positive stationary reserve `-2B_L`; but the full odd trial carries archimedean energy `2B_L+o(1)`. The two contributions cancel exactly at the asymptotic floor.

For the exact localized Weil quadratic form on the admitted fixed-width source-zero trials `f_k`, WI-385 obtains the exhaustive alternative

`RH => liminf W_k[f_k]=0`,

with recurrent near-zero returns, while

`not RH => liminf W_k[f_k]=-infinity`.

Hence, without assuming either branch, there is no fixed `delta>0` for which these trials eventually satisfy a coercive estimate `W_k[f_k]>=delta ||f_k||_2^2`. Under RH they are asymptotic null directions of Weil positivity, not counterexamples to semidefinite nonnegativity.

This closes the fixed-width route to a positive Gate-II tariff on the old quadratic form itself. A surviving rooted/Schur strategy must instead use semidefinite positivity without a fixed reserve, prove that an exact graph/domain condition excludes these trials before the form is tested, or exhibit a source-coupling mechanism that is not equivalent to adding a positive lower bound on the same admitted vectors.

**Boundary.** The conclusion concerns this certified fixed-width source-zero trial family and the exact localized Weil form. It does not refute Weil nonnegativity, Desogus's full theorem, or a different admissible subspace that genuinely excludes the quasimodes. It also does not classify growing-width, different-profile or nonlocal trial families.