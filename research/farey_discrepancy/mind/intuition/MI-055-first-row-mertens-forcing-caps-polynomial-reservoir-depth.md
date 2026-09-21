# MI-055 — First-row Mertens forcing caps polynomial reservoir depth

**Evidence level:** exact source-side synthesis from [FD-258](../../findings/FD-258-first-switched-row-imposes-a-zero-frontier-polynomial-depth-ceiling.md), using the Mertens zero-frontier calibration already recorded in FD-046 and the exact reservoir geometry of FD-226.

The deep-band positivity loss of MI-054 is not the only physical-source constraint. In the exact FD-226 selected-prime reservoirs, the first switched row already satisfies

`X_N(2N)-X_N(N) = M(2N)-M(N) + 2(a_2-a_1)`.

The first two cells contain only `O(N/D)` possible flips, so any realization with first-row tolerance `B_N` must obey

`|M(2N)-M(N)| <= B_N + N/D + 2`.

The dyadic increment `M(2N)-M(N)` has the same limsup polynomial exponent `Theta` as the Mertens function, where `Theta` is the supremum of the real parts of nontrivial zeta zeros. Therefore, if `B_N=N^{o(1)}`, every all-large-`N` family in this exact reservoir architecture has

`liminf log D_N / log N <= 1-Theta <= 1/2`.

This separates two source-side regimes. At the currently certified depth `D=N^{o(1)}`, the first-row slot count is much larger than the zero-frontier forcing, so FD-258 does not obstruct the FD-225--FD-226 construction; the live issue there remains the one-sided slack comparison from MI-054. But any attempt to push the same reservoir geometry to polynomial depth eventually encounters the arithmetic baseline before later-row conditioning or positive-capacity depletion matters. Improving those later mechanisms cannot produce a uniform exponent above `1-Theta` without changing which source variables can affect the samples at `N` and `2N`.

**Boundary.** This is a necessary condition for the FD-226 selected-prime reservoir architecture, not a matching construction theorem and not an RH criterion. It gives no sufficiency below `1-Theta`, does not obstruct the present subpolynomial depth, and may be evaded by a genuinely different first-row source geometry.