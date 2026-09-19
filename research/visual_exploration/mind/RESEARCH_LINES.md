# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Resolve exceptional finite-height coherence after Bohr/Haar identification

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-301 show that Wang's displayed localization ceiling is not structural. Decomposition isolates one inside--outside coherence term, and the unconditional Vinogradov--Korobov zero-free region suppresses it far enough that the first generic `H`-scale obstruction moves into the interior Montgomery--Vaughan mean-value estimate.

VIS-302 specializes that estimate to Wang's exact coefficients and saves one logarithm. VIS-303 uses the actual support to remove the power-of-two/odd-shift sector. VIS-304 applies the weighted Hilbert inequality on the actual prime-power logarithmic frequencies and obtains an absolute spacing cost `O(x log log x)`, moving the generic pointwise range to `x log log x=o(H)`.

VIS-305 shows that this absolute reciprocal-spacing scale is not arithmetic by itself: a parity- and density-matched Bernoulli support already has expected cost `Theta(x log log x)`. VIS-306 then evaluates the signed endpoint form on that control and obtains expectation `O(x)`, variance `O(x log^3 x)` and hence `o_p(H)` at `H~x log log x`.

VIS-307 removes support-geometry ambiguity. It keeps every actual prime power, every prime-power spacing and every Wang coefficient magnitude, but assigns an independent Steinhaus phase to each support point. The signed quadratic remainder still has second moment `O(x log^3 x)` and is `o_p(H)` at the boundary. Exact support, spacing and magnitudes are therefore insufficient when deterministic relative phases are destroyed.

VIS-308 strengthens the matched control by preserving complete multiplicativity of the phases. One Steinhaus variable is assigned per base prime and `f(p^k)=f(p)^k`, so every harmonic phase relation inside the family `p,p^2,p^3,...` survives exactly. The only additional torus-character collisions are same-prime equal-exponent-difference fibers, and Wang's taper makes their total contribution negligible. The same `O(x log^3 x)` second-moment bound survives.

VIS-309 then compares that Haar model to the **actual deterministic common-time orbit**. For fixed `x,H`, time averaging `p^{-it}` over arbitrarily long intervals has the same quadratic mean as Haar averaging the completely multiplicative prime phases, because the surviving logarithmic-frequency relations are exactly the multiplicative character collisions. The Bohr mean square remains `O(x log^3(3x))`; at the critical `H~x log log x` scale, large signed remainders therefore occupy vanishing long-time density in the corresponding calibration.

VIS-310 quantifies the most naive attempt to convert that Bohr statement into a finite-window theorem. Hard truncating the prime-power series at `Y`, controlling the discarded tail in uniform norm, and applying Montgomery--Vaughan only through the **global minimum gap** of retained rational-ratio frequencies gives

`V^(-1) integral |R_(x,H)(T)|^2 dT << x L^3 + H^(4/3)x^(7/3)L V^(-1/3)`

after optimizing `Y`, with `L=log(3x)`. At `H~x log log x`, this particular route reaches `o(H^2)` only for the sufficient scale

`V >> x^5 L^3/(log log x)^2`.

That quintic horizon is not a true dephasing lower bound. It measures the information thrown away by **uniform tail control plus worst-gap compression**. The local scale `V~H` remains open to a coefficient-weighted/nontruncated argument.

The live arithmetic object is consequently narrower than “cross-prime deterministic alignment.” Generic common-time alignment is already Haar-typical in the infinite-time quadratic mean, while the first straightforward finite-time transfer is far too lossy. A genuine pointwise mechanism must live in **exceptional finite heights, coefficient-weighted finite-window dephasing of the growing ratio spectrum, a joint moving regime `x=x(T)`, or another endpoint interaction invisible to both the quadratic Bohr average and the hard-cutoff worst-gap estimate**. The next useful control should preserve the nonuniform ratio-spectrum energy rather than collapsing it to one global gap.

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, localization leakage, cross-coherence, coefficient-specific mean-value weight, ambient versus support-sensitive frequency spacing, matched random spacing controls, signed matched-control cancellation, exact prime-power support, independent versus completely multiplicative random phases, common-time torus motion, Bohr/Haar equivalence, hard versus energy-sensitive tail treatment, global minimum ratio gap versus coefficient-weighted local spacing, finite-height discrepancy, actual endpoint phase, deterministic gamma normalization and analytic domain of the source transform.

VIS-294--VIS-310 give a repeated control pattern. Exact deterministic pieces can be split too early; generic coefficient majorants can lose logarithms; sparse-frequency geometry can improve ambient bounds; matched support models can show an absolute norm is generic; exact support can still cancel after phase randomization; all same-base harmonic relations can be preserved without restoring the boundary; the actual deterministic phase orbit has the same long-time quadratic mean as that Haar control; and the direct hard-truncation/global-gap route can still lose powers large enough to be useless locally. A structural transition is credible only after the surviving **finite-height/moving-frequency coherence mechanism** itself defeats a control that preserves the weighted frequency geometry at the destination scale.
