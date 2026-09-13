# VIS-211 — translated Brun–Titchmarsh bounds close the one-cancellation Schur frontier

## Claim

Keep the autocorrelation-taper prime-anchor kernel of `VIS-203` and `VIS-209`. Fix `0<=alpha<1/2`, put

`beta=1-2alpha>0`,

`Q_y=sum_(p<=y) p^(-2alpha)`,

and for distinct primes `u,t<=y` let

`Psi_(u,t)=Q_y^(-1)(ut)^(-alpha) rho(H log(u/t))`,

with `Psi_(u,u)=0`, where the fixed autocorrelation taper has `rho>=0` even and rapidly decreasing.

Define the weighted Schur mass

`S(y,H)=sup_(u<=y, u prime) sum_(t<=y, t prime, t!=u) t^(-2alpha) rho(H log(u/t))`.

Then, as `y->infinity`, uniformly throughout every diverging strictly subcritical scale

`H=H(y)->infinity`, `H log y / y -> 0`,

one has

`S(y,H) = o(Q_y/sqrt(H))`.

More explicitly, for every fixed `A>1`,

`S(y,H) << H^(beta-1) + y^beta/[H log(y/H)] + Q_y H^(-A)`

once `y/H` is sufficiently large.

Consequently the weighted Schur test from `CLUE-one-cancellation-weighted-schur-kernel` gives

`||Psi||_op <= Q_y^(-1) S(y,H) = o(H^(-1/2))`.

Since `VIS-192` proves `R_v(y,H) asymp 1/H` in the same strictly subcritical regime,

`||Psi||_op^2=o(R_v(y,H))`.

The exact `VIS-209` Gram inequality therefore yields

`E_1/R_v(y,H)^2 <= 4 ||Psi||_op^2/R_v(y,H) -> 0`.

Thus the **entire one-cancellation prime/prime shell energy is negligible in long-start mean square throughout every diverging strictly subcritical scale** for this autocorrelation-taper class. The one-cancellation Gram frontier exposed by `VIS-209` is closed at the level needed for the long-start Cesaro problem.

**Evidence/status:** `LITERATURE+DERIVED + UNIFORM SCHUR BOUND + ONE-CANCELLATION FRONTIER CLOSED + NO-NOVELTY-CLAIM`.

This does not prove worst-start uniformity, control higher-cancellation shell families, or establish the sharper heuristic `S(y,H)<<Q_y/H` uniformly.

## 1. Weighted Schur reduces the operator norm to one prime-window supremum

The proposed clue already records the exact weighted Schur reduction. Take positive weights

`h_u=u^(-alpha)`.

Because `Psi` is symmetric and nonnegative,

`h_u^(-1) sum_t Psi_(u,t) h_t`
` = Q_y^(-1) sum_(t!=u) t^(-2alpha) rho(H log(u/t))`.

Hence the weighted Schur test gives

`||Psi||_op <= Q_y^(-1) S(y,H)`.

It remains only to prove the displayed uniform estimate for `S(y,H)`. No spectral approximation or finite-anchor model is used.

The autocorrelation construction in `VIS-203` starts from a fixed `C_c^infinity` function `g` and has

`rho(theta)=|g_hat(theta)|^2/|g_hat(0)|^2`.

Therefore for every fixed `A>0`,

`rho(theta) <<_(A,g) (1+|theta|)^(-A)`.

This rapid decay is the only taper input below.

## 2. Prime anchors split into far, small, and translated-window regimes

Fix a prime anchor `u<=y` and write its Schur sum as `S_u`.

First consider primes outside the multiplicative near region `[u/2,2u]`. There

`|log(u/t)| >= log 2`,

so rapid decay gives, for every fixed `A>0`,

`S_(u,far) << H^(-A) sum_(t<=y) t^(-2alpha)`
` << Q_y H^(-A)`.

It remains to treat `u/2<=t<=2u`, where `t^(-2alpha) asymp u^(-2alpha)`.

### Small anchors: `u<2H`

For `u/2<=t<=2u` one has

`|log(t/u)| >= c |t-u|/u`

with an absolute `c>0`. Since distinct primes are distinct integers, `m=|t-u|>=1`. Ignoring primality only enlarges the sum, and for `A>1`,

`sum_(m>=1) (1+cHm/u)^(-A) << u/H`

when `H/u>=1/2`. Therefore

`S_(u,near) << u^(-2alpha) u/H`
` = u^beta/H`
` << H^(beta-1)`.

This already handles the discrete regime where a physical kernel window contains only `O(1)` integers; no artificial `+1` term per logarithmic band is needed.

### Large anchors: `u>=2H`

Put

`Delta=u/H>=2`.

Partition each side of `u` inside `[u/2,2u]` into translated additive intervals of length comparable to `Delta`. On the `k`-th such interval,

`H|log(t/u)| >= c k`

for an absolute constant `c>0`, while `t^(-2alpha) asymp u^(-2alpha)`.

Montgomery and Vaughan's large-sieve form of Brun–Titchmarsh gives, for positive integers `M,N`,

`pi(M+N)-pi(M) <= 2 pi(N)`.

After rounding the interval length and using the standard upper bound `pi(N)<<N/log N`, every translated interval of length `Delta>=2` contains

`<< Delta/log Delta`

primes, uniformly in its location. Summing the rapidly decaying intrinsic bands gives

`S_(u,near)`
` << u^(-2alpha) [Delta/log Delta] sum_(k>=0) (1+k)^(-A)`
` << u^beta/[H log(u/H)]`.

Combining the three pieces,

`S_u << H^(beta-1) + u^beta/[H log(u/H)] + Q_y H^(-A)`

where the middle term is needed only for `u/H>=2`.

## 3. The anchor supremum has only two endpoint scales

For `z>=2`, consider

`f(z)=z^beta/log z`.

Its derivative changes sign at most once:

`f'(z)=z^(beta-1) [beta log z-1]/(log z)^2`.

Thus on any interval `[2,Y]` its maximum is attained, up to fixed constants, at an endpoint. Substituting `z=u/H` gives

`sup_(2H<=u<=y) u^beta/[H log(u/H)]`
` << H^(beta-1) + y^beta/[H log(y/H)]`.

Therefore

`S(y,H)`
` << H^(beta-1)`
`    + y^beta/[H log(y/H)]`
`    + Q_y H^(-A)`.

The first term is the genuinely discrete small-anchor boundary. The second is the bulk translated-prime-window contribution. The third is the rapidly decaying multiplicative tail.

## 4. Every term is below the Schur threshold

`VIS-192` records, for fixed `alpha<1/2`,

`Q_y asymp y^beta/log y`.

Normalize the preceding estimate by `Q_y/sqrt(H)`.

For the small-anchor term the ratio is

`<< log y H^(beta-1/2)/y^beta`.

If `beta<=1/2`, then `H^(beta-1/2)<=1`, so this is `o(1)`. If `beta>1/2`, strict subcriticality implies eventually `H<=y/log y`, and the ratio is at most

`y^(-1/2) (log y)^(3/2-beta) -> 0`.

For the bulk term the ratio is

`<< log y/[sqrt(H) log(y/H)]`.

If `H<=sqrt(y)`, then `log(y/H)>=(1/2)log y`, so the ratio is `O(H^(-1/2))=o(1)`. If `H>sqrt(y)`, then strict subcriticality gives `y/H->infinity`; in particular,

`log y/[sqrt(H) log(y/H)]`
` <= log y/y^(1/4)`
` ->0`

once `log(y/H)>=1`.

Finally the far-tail ratio is

`<< H^(1/2-A)`,

which tends to zero for any fixed `A>1/2`; the derivation above already permits `A>1`.

Hence

`S(y,H)=o(Q_y/sqrt(H))`

uniformly for every `H->infinity` with `H log y/y->0`.

## 5. Consequence for the exact one-cancellation energy

The weighted Schur reduction now gives

`||Psi||_op=o(H^(-1/2))`.

Squaring,

`||Psi||_op^2=o(1/H)`.

In the same regime `VIS-192` has

`R_v(y,H) asymp 1/H`,

so

`||Psi||_op^2=o(R_v(y,H))`.

Substitution into the exact `VIS-209` bound

`E_1/R_v^2 <= 4 ||Psi||_op^2/R_v`

proves

`E_1=o(R_v^2)`.

This is precisely the sufficient condition requested by the weighted-Schur clue. It suppresses all exact one-cancellation prime/prime shells simultaneously, including their full anchor multiplicity, without the withdrawn finite-support diagonalization of former `VIS-210`.

## Prior-art audit

The translated-prime input is classical. H. L. Montgomery and R. C. Vaughan, **The large sieve**, *Mathematika* 20:2 (1973), 119–134, DOI `10.1112/S0025579300004708`, gives the large-sieve form of Brun–Titchmarsh used here; its standard Corollary 2 is the location-uniform inequality

`pi(M+N)-pi(M) <= 2 pi(N)`.

The weighted Schur test, rapid decay of the Fourier transform of a smooth compactly supported function, and the prime-sum asymptotic `Q_y asymp y^beta/log y` are classical ingredients. The last asymptotic was already part of the audited `VIS-192` framework.

No novelty is claimed for Brun–Titchmarsh, the large sieve, Schur's test, Schwartz decay, or weighted prime counting. The Mathia-specific result is their assembly with the exact `VIS-209` prime-anchor kernel: the proposed spectral-concentration condition is not merely plausible but follows throughout the full diverging strictly subcritical regime from a one-dimensional translated-prime bound.

## Boundaries and falsification

The result fixes `0<=alpha<1/2` and a fixed autocorrelation taper from `VIS-203`. Constants may depend on `alpha` and the taper. The proof uses nonnegativity and rapid decay of `rho`; it does not automatically extend to arbitrary signed or slowly decaying centered taper spectra.

The conclusion is asymptotic and strictly subcritical:

`H->infinity`, `H log y/y->0`.

It does not claim the same estimate at the critical scale `H asymp y/log y`, nor does it prove the stronger orientation `S<<Q_y/H` uniformly. The translated Brun–Titchmarsh bound is used only as an upper bound; no short-interval prime asymptotic is assumed.

Most importantly, `E_1=o(R_v^2)` is a **long-start mean-square** statement inherited from the `VIS-192`--`VIS-209` framework. It does not yield a uniform-in-start estimate. Higher cancellation classes and the remaining finite-start coherence problem require separate arguments.

Falsify this finding by locating an error in the weighted Schur reduction, the multiplicative-to-additive band comparison, the translated-interval prime count, the endpoint maximization of `z^beta/log z`, the normalization by `Q_y`, or the use of `VIS-192`'s `R_v asymp 1/H` regime.

## Research consequence

The one-cancellation Gram operator is no longer the unresolved obstruction in the diverging strictly subcritical long-start regime. Its complete shell energy is `o(R_v^2)`.

The active frontier should therefore move to mechanisms not covered by this theorem: higher cancellation classes in the exact difference-shell expansion, or the separate problem of upgrading start-averaged/density-one control to a genuinely uniform finite-start statement. Those are new coherent investigations rather than reasons to extend this finding further.
