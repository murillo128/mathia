# MI-013 — Möbius cancellation has a signed near-diagonal middle category, and the logarithmic split isolates its rough parity price

**Evidence level:** exact finite-algebra, Gallagher-localization, variance-pricing, smooth-remainder, and logarithmic rough-factor results through MC-180

## Core intuition

Gallagher localization supplies a genuine middle category between phase-blind support information and a global Mertens endpoint: its finite-time heat energy is an exact signed near-diagonal Möbius energy. The difficulty is quantitative. Strong local suppression has an explicit global price, and several familiar decomposition routes lose the needed power before they reach polynomial windows.

The newest source-specific result changes where the burden sits. Möbius squarefree support allows all primes above a logarithmic cutoff to be carried by one structured **rough parity block**, eliminating the dense smooth-support remainder without paying growing one-prime-at-a-time extraction depth. The missing theorem is now signed cancellation inside that rough block.

## Strongest justified principle

MC-172 derives the signed near-diagonal Gallagher energy; MC-173 shows that support-only autocorrelation can erase exactly the phase it needs. MC-174--MC-177 price local variance strength against zero-free/Mertens consequences, including the critical-shell and direct-transfer exponent budgets.

MC-178 shows that Chinis's published square-root mechanism and block extension remain only subpower better than coherent variance at fixed polynomial windows because a polynomial smooth cutoff leaves a positive-density smooth sector. MC-179 proves that lowering the terminal cutoff and continuing to discard that sector by support requires prime-by-prime extraction depth of order `log X/log log X` for a fixed-power gain.

MC-180 bypasses that method barrier using the exact convolution `mu=f_y*g_y` at `y=c log X`. The small-prime squarefree factor has only subpowerly many divisor states and support below `X`, so the pure small-prime sector vanishes on the target interval. A uniform fixed-power variance bound for the resulting rough factor at the divisor-scaled windows transfers to full Möbius variance with the same exponent up to subpower loss.

## Program consequence

Treat the rough parity block as the current source-attainable candidate currency. Prove a phase-sensitive local second-moment gain for it, or identify an exact obstruction showing that its parity structure still costs the same as full Möbius cancellation. Keep the horizon, averaging measure, variance exponent, and induced global Mertens consequence explicit.

The gain in MC-180 is architectural, not yet analytic: it removes the smooth-support/depth bookkeeping obstruction but does not supply rough-number cancellation.

## Counterevidence / boundary

MC-180 does not prove any new Möbius variance estimate. Its transfer requires uniform control across the scaled rough windows, and support density or roughness alone does not control the signed off-diagonal. Other signed local statistics may bypass the Gallagher interface, but they must still be priced in their final currency.

## Epistemic status

**Supported signed intermediate category with an exact source-specific rough-factor reduction and explicit quantitative pricing; no new Möbius variance theorem or RH consequence is established.**

## Falsification criterion

Refute the MC-180 exact logarithmic split/variance transfer, or produce a support-only argument that controls the signed Gallagher energy despite the matched phase controls. A positive continuation should prove and price genuine cancellation in the rough parity block or another source-sensitive intermediate category.