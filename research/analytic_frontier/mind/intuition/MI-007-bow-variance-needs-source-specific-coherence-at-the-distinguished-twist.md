# MI-007 — Bow cancellation requires source-specific near-nullspace alignment at the distinguished twist

**Evidence level:** exact post-sieve normal forms, matched local-statistics controls, and Gram/Rayleigh reduction through ANF-152

## Core intuition

The analytic bow is no longer plausibly explained by generic prime randomness, correct local density, or a finite list of singular-series correlations. After the known local structure is conditioned away, the surviving arithmetic innovation must be organized relative to the **specific moving-window Gram geometry selected by the bow**.

The sharp formulation is spectral. Small bow energy requires the normalized post-sieve innovation to concentrate asymptotically in directions whose Gram eigenvalues collapse. Ordinary decorrelation leaves the innovation spread across positive-eigenvalue directions and therefore reproduces the diagonal rather than cancelling it.

## Strongest justified principle

ANF-150 writes the residual after small-prime conditioning in an exact post-sieve form and constructs a sieved-Cramér matched control that reproduces the finite Ramanujan pair profile and conditional density while retaining diagonal bow variance. ANF-151 strengthens the control: even agreement with a growing truncated Hardy--Littlewood local hierarchy does not force the selected cancellation.

ANF-152 converts the remaining target into a Rayleigh-quotient statement for the moving-window Gram operator. If a fixed fraction of the innovation energy remains in spectral directions bounded away from zero, the bow cannot become subdiagonal. The desired cancellation therefore demands near-nullspace alignment, not merely weak dependence or improved local tuple statistics.

## Program consequence

Search for a source theorem that couples the exact distinguished twist, the post-sieve innovation, and the Gram eigenstructure before any componentwise absolute-value estimate is taken. A useful theorem should either force concentration in the collapsing spectral sector or prove a quantitative delocalization lower bound that closes this route.

## Counterevidence / boundary

The near-nullspace criterion is an exact reformulation of the selected quadratic target, not evidence that the actual primes satisfy it. The matched controls show only that increasingly rich local statistics do not imply the alignment. They do not rule out a genuinely global arithmetic relation that does.

## Epistemic status

**Exact destination-space reduction with strong matched controls; the source mechanism producing or forbidding the required alignment is open.**

## Falsification criterion

Derive subdiagonal bow energy while a fixed positive fraction of the normalized post-sieve innovation remains uniformly above a positive Gram spectral threshold, or invalidate the ANF-152 Rayleigh reduction. A positive continuation should instead prove source-forced spectral concentration in the near-null sector.
