# VIS-021 — Gram-interval occupancy is the discrete derivative of the zero-counting argument term

## Claim

Let `N(T)` count the nontrivial zeros `rho = beta + i gamma` of `zeta(s)` with `0 < gamma <= T`, counted with multiplicity, and take `T` away from a zero ordinate. Let `theta(t)` be the continuously normalized Riemann–Siegel theta function and let

`S(T) = (1/pi) arg zeta(1/2 + iT)`

use the standard continuous argument convention in the Riemann–von Mangoldt formula. Then

`N(T) = theta(T)/pi + 1 + S(T)`.

For a Gram point `g_n` satisfying `theta(g_n) = n pi`, define the integer discrepancy

`D_n = N(g_n) - (n+1)`.

Whenever `g_n` is not itself a zero ordinate,

`D_n = S(g_n)`.

If

`C_n = N(g_{n+1}) - N(g_n)`

is the number of nontrivial zeros whose ordinates lie in the Gram interval `(g_n, g_{n+1}]`, then exactly

`C_n = 1 + S(g_{n+1}) - S(g_n) = 1 + D_{n+1} - D_n`.

Equivalently,

`D_{n+1} = D_n + C_n - 1`.

Thus a Gram-interval occupancy visualization and the Gram-sampled zero-counting residual are the same discrete information up to one initial integer. In particular, the visual event “this Gram interval contains other than one zero” is exactly a nonzero discrete increment of the sampled `S` term.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED`.

No novelty is claimed for the zero-counting formula, Gram points, or `S(T)`. The useful result here is a visual-independence boundary: three natural-looking baseline views — the zero-counting staircase residual, the sampled argument term, and Gram-interval occupancies — must not be counted as independent geometric channels.

## Exact derivation

The standard Riemann–von Mangoldt/Backlund relation gives

`N(T) = theta(T)/pi + 1 + S(T)`

for the stated conventions. At a Gram point `g_n`, by definition `theta(g_n)/pi = n`, so direct substitution gives

`N(g_n) = n + 1 + S(g_n)`

and hence `D_n=S(g_n)`. Since `N(g_n)` and `n+1` are integers, the sampled value `S(g_n)` is an integer under these conventions whenever the Gram point is not a zero ordinate.

Subtract the formula at two consecutive Gram points:

`N(g_{n+1}) - N(g_n)`

`= [(n+1)+1+S(g_{n+1})] - [n+1+S(g_n)]`

`= 1 + S(g_{n+1}) - S(g_n)`.

This is the claimed occupancy identity. The inverse recurrence `D_{n+1}=D_n+C_n-1` shows that the occupancy sequence recovers the sampled argument residual once a single initial discrepancy is fixed, so the relationship is not merely a correlation.

## What this removes from the visual search space

A plot of `N(T)` against its Riemann–Siegel smooth phase baseline can be useful as a canonical instrument, and a Gram-interval occupancy map can make exceptional local blocks visually obvious. But after sampling at Gram points, these are not separate evidence streams. Coloring an interval by `C_n-1`, plotting the increments of `D_n`, or plotting the increments of `S(g_n)` are exact re-encodings of the same integer sequence.

This matters for a visual atlas because repeated structure across these views does not survive an independent representation change: it is forced by the counting identity. A candidate cross-view pattern must therefore use information not recoverable from this relation — for example modulus geometry away from the counting contour, local spacing data at a finer scale than Gram occupancy, or a prime/zero representation with an independently defined second channel.

The result does **not** say that all Gram-point phenomena are equivalent to occupancy. Sign patterns of Hardy's `Z(g_n)`, magnitudes, local derivatives, and other analytic data can contain information not present in the occupancy count. The obstruction applies specifically to views determined by `N(g_n)`, `S(g_n)`, and their first differences.

## Prior art and novelty assessment

The ingredients are classical. DLMF §25.10 gives the standard Hardy `Z(t)` and Riemann–Siegel `theta(t)` definitions and points to Titchmarsh for the counting machinery. The exact zero-counting decomposition into the smooth theta term plus `S(T)` is standard Riemann–von Mangoldt/Backlund theory; Hall (1999) explicitly recalls this formula and its `S(T)` term. Gram points are the standard level set `theta(g_n)=n pi`.

The displayed occupancy identity is therefore an immediate specialization and subtraction of classical formulas, not a new theorem. Its role in Mathia is a **negative control for visual independence**: it prevents a baseline atlas from treating three algebraically interconvertible pictures as corroborating geometric evidence.

## Boundary conditions

At a zero ordinate the conventional values of `N(T)` and `S(T)` require the usual limiting/averaging convention. The clean formulas above deliberately state the generic case where Gram points do not coincide with zero ordinates. The identity counts all nontrivial zeros in the critical strip by ordinate and does not assume RH; interpreting every counted zero as a zero of `Z(t)` on the critical line would require an additional hypothesis or verified finite-height computation.

The formula also does not prove Gram's law or any asymptotic statement about how often `C_n=1`. It only identifies the exact discrete variable whose increment measures occupancy failure.

## Visual consequence

A local inspection plot of the Gram discrepancy and exceptional occupancies was useful for recognizing the discrete-derivative structure, but no canonical PNG is retained because the plot adds no information beyond the exact identity. Persisting another rendering of the same integer relation would create visual churn rather than a new research instrument.

## Research consequence

`CLUE-zeta-rh-canonical-visual-atlas` should remain live but with an explicit independence quotient: zero-counting staircase residuals, `S(T)` sampled at Gram points, and Gram-interval occupancy belong to one counting/argument family. A minimal canonical atlas should prefer representatives from mathematically non-recoverable families rather than count these as independent views.
