# VIS-028 — the exact Farey endpoint fan forces an `r = Theta(n)` Dirichlet spectral scale

## Claim

Let

`0=x_0<x_1<...<x_N=1`

be the Farey sequence of order `n`, indexed so that `N=sum_(q<=n) phi(q)` is the number of gaps, and let

`D_k=x_k-k/N`,  `1<=k<=N-1`

be its rank-grid discrepancy.

Put `L_n=floor(n/2)+1`. Then the first `L_n` positive Farey fractions are exactly

`x_k = 1/(n-k+1)`,  `1<=k<=L_n`.

By Farey reflection, the same deterministic unit-fraction fan appears at the right endpoint with `D_(N-k)=-D_k`.

Define the endpoint-fan discrepancy `D^fan` by retaining those two endpoint pieces and setting the interior to zero. Then, uniformly for `u=k/n` in the endpoint fan,

`n D_k -> f(u) := 1/(1-u) - (pi^2/3) u`,  `0<=u<=1/2`,

because `N/n^2 -> c := 3/pi^2`.

Consequently

`n ||D^fan||_2^2 -> C_fan`

with

`C_fan = 2 integral_0^(1/2) f(u)^2 du`

`      = 2 + 2 pi^2/3 - (4 pi^2/3) log 2 + pi^4/108`

`      = 0.3602210103...`.

Now use the orthonormal Dirichlet sine basis from `VIS-027`,

`v_m(k)=sqrt(2/N) sin(pi m k/N)`,

and write `d_m^fan=<D^fan,v_m>`. Reflection forces `d_m^fan=0` for odd `m`. For every fixed `x>0`, with `r=floor(x n)`,

`n d_(2r)^fan -> G(x)`

where

`G(x) = 2 sqrt(2/c) integral_0^(1/2) f(u) sin(2 pi x u/c) du`.

Equivalently,

`G(x) = 2 pi sqrt(2/3) integral_0^(1/2) [1/(1-u)-(pi^2/3)u] sin((2 pi^3/3) x u) du`.

More strongly, for every fixed `X>0`,

`n sum_(1<=r<=X n) (d_(2r)^fan)^2 -> integral_0^X G(x)^2 dx`.

Thus an even-mode transition on the scale `r = Theta(n)` is forced already by the elementary endpoint unit-fraction geometry. A finite collapse of the full Farey discrepancy spectrum under `r/n` scaling is therefore **not by itself evidence** for a deeper denominator-, mediant-, or cross-scale arithmetic mechanism.

**Evidence/status:** `CLASSICAL FAREY ENDPOINT STRUCTURE + EXACT-DERIVED ASYMPTOTIC CONTROL + FINITE NUMERICAL VALIDATION`.

No asymptotic formula for the complete Farey `L^2` discrepancy, strengthened Franel–Landau criterion, or RH implication is claimed.

## Exact endpoint fan

Two reduced fractions `a/b<c/d` are neighbors in the Farey sequence of order `n` when `bc-ad=1` and `b+d>n`. For consecutive unit fractions

`1/q < 1/(q-1)`

the determinant is one. Starting from `1/n`, the neighbor condition remains true down to `q=ceil(n/2)`. Therefore the initial positive segment is

`1/n, 1/(n-1), ..., 1/ceil(n/2)`,

which contains exactly `L_n=floor(n/2)+1` fractions. The involution `a/b -> (b-a)/b` gives the reflected terminal segment.

For `1<=k<=L_n` we therefore have the exact discrepancy

`D_k = 1/(n-k+1) - k/N`.

This is a deterministic boundary layer: it does not require any information about the complicated Farey ordering in the interior.

## Spatial scaling and endpoint energy

The classical summatory-totient estimate gives

`N = (3/pi^2)n^2 + O(n log n)`.

For `k/n -> u` with `0<=u<=1/2`,

`n/(n-k+1) -> 1/(1-u)`

and

`n k/N -> (pi^2/3)u`.

Hence `nD_k -> f(u)` uniformly on the endpoint interval up to the vanishing lattice endpoint correction.

Because `D_k=O(1/n)` on `Theta(n)` endpoint ranks, the fan contributes `Theta(1/n)` squared discrepancy energy. Direct Riemann summation gives

`n ||D^fan||_2^2`
` = 2n sum_(k=1)^L_n D_k^2`
` -> 2 integral_0^(1/2) f(u)^2 du`
` = C_fan`.

The explicit constant follows by elementary integration.

For finite orders, `n||D^fan||_2^2` equals approximately

`0.335726, 0.351819, 0.354443, 0.357804, 0.358688`

at `n=100,200,400,800,1600`, respectively, approaching the unconditional constant `0.360221...`.

As a relevance diagnostic only, direct full-Farey evaluation shows that the two fan regions contain about `0.553, 0.570, 0.568, 0.557, 0.548` of the complete finite `E_2=sum D_k^2` at `n=200,400,800,1600,2000`. No limit for this ratio is asserted; the full discrepancy is precisely the difficult RH-sensitive object.

## Dirichlet spectral scaling

For the reflected fan, pair the left endpoint rank `k` with `N-k`. Since

`D_(N-k)^fan=-D_k^fan`

and

`v_m(N-k)=(-1)^(m+1)v_m(k)`,

all odd coefficients vanish exactly. For `m=2r`,

`d_(2r)^fan`
` = 2 sqrt(2/N) sum_(k=1)^L_n D_k sin(2 pi r k/N)`.

Put `r=floor(xn)`. Using `N/n^2->c`, `k/n->u`, and the spatial limit above, the finite sum is a uniform Riemann sum on every bounded `x` interval:

`n d_(2r)^fan`
` -> 2 sqrt(2/c) integral_0^(1/2) f(u) sin(2 pi x u/c) du`
` = G(x)`.

The same uniform approximation gives, for fixed `X`,

`n sum_(r<=Xn) (d_(2r)^fan)^2`
` -> integral_0^X G(x)^2 dx`.

Sine-transform Plancherel is consistent with the spatial energy constant:

`integral_0^infinity G(x)^2 dx = C_fan`.

This identifies the scale without fitting it. The endpoint layer has width `Theta(n)` in rank space while the full Farey sequence has `N=Theta(n^2)` gaps, so its Dirichlet content naturally lives around wavelengths `N/r=Theta(n)`, i.e. `r=Theta(n)`.

For the normalized endpoint-fan energy, direct evaluation of the continuum transform gives cumulative fractions through `r/n=0.25,0.5,1,2` of approximately

`0.2977, 0.6729, 0.8274, 0.9064`.

At `n=1600` the corresponding finite values are approximately

`0.2991, 0.6736, 0.8289, 0.9080`.

These finite spectral numbers only validate the asymptotic scale; the claim does not depend on visual curve fitting.

## Prior art and novelty assessment

The endpoint localization is classical territory, not a claimed new Farey theorem. François Dress, **Discrépance des suites de Farey**, *Journal de théorie des nombres de Bordeaux* 11:2 (1999), 345–367, DOI `10.5802/jtnb.255`, proves that the absolute Farey discrepancy is exactly `1/n`, attained at the local point `1/n`, and records the standard asymptotic `sum_(q<=n) phi(q)=(3/pi^2)n^2+O(n log n)`.

R. Tomás, **Partial Franel Sums**, *Journal of Integer Sequences* 25 (2022), Article 22.1.5, explicitly studies endpoint neighborhoods and partial Franel sums. Rogelio Tomás García, **Farey Fractions with Equal Numerators and the Rank of Unit Fractions**, *Integers* 24 (2024), #A63, DOI `10.5281/zenodo.12685697`, studies ranks of unit fractions in `F_n`. Those works make clear that endpoint/unit-fraction structure is established prior art.

The Dirichlet sine/Green organization is likewise standard and already classified in `VIS-027`. A targeted structure-based search did not locate the specific endpoint-fan-to-`r/n` spectral scaling statement above, but absence in that search is not a novelty claim. The durable Mathia contribution is the **control boundary**: the same `r=Theta(n)` scale that looked suggestive in the full Farey spectral diagnostic is already generated by a deterministic classical endpoint layer.

## Boundary conditions and falsification

This finding isolates only the exact unit-fraction endpoint fan. It does **not** say that the fan determines the full Farey spectral profile. In spectral coordinates the endpoint and interior pieces interfere coefficient by coefficient, even though their spatial `L^2` energies add because their supports are disjoint.

The statement also does not determine the asymptotic size of the complete Farey Franel energy. Finite values of `||D^fan||_2^2 / ||D||_2^2` are retained only to show that the control is quantitatively non-negligible at accessible orders.

The `r=Theta(n)` conclusion concerns the natural transition scale forced by the endpoint fan. A genuinely additional multiscale invariant could still survive after the fan is removed, after stronger controls preserve it, or in cross-band relations not reconstructible from the endpoint contribution.

A material falsification would require an error in the exact endpoint indexing, the totient asymptotic normalization, or the Riemann/sine-transform derivation.

## Research consequence

The cross-line Farey clue

`research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md`

must be strengthened with this control. Its current `Phi_n(floor(xn))` collapse remains a useful finite observation, but the **existence of an `r/n` collapse scale is no longer a discriminating signal**: elementary endpoint geometry forces that scale independently.

The next useful Farey test is therefore residual. Remove the exact endpoint fan from the discrepancy path before forming the modal profile, or compare against a matched ensemble that preserves the same endpoint layer, and only then ask whether a stable even-mode shape remains that requires denominator strata, mediant ancestry, long-range gap ordering, or another arithmetic mechanism beyond the classical scalar discrepancy.
