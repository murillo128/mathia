# MI-024 — Arithmetic-image blind exclusion is directional leverage with a parity-sensitive support barrier

**Evidence level:** exact variational reduction/certificate from [MC-281](../../findings/MC-281-empirical-christoffel-leverage-blind-certificate.md), sharpened by the separated-prime control [MC-282](../../findings/MC-282-separated-simplex-leverage-failure.md), the Page--Siegel shell-universality obstruction [MC-284](../../findings/MC-284-page-siegel-stretched-exponential-shell-legendre-universality.md), the deterministic even-weight support barrier [MC-285](../../findings/MC-285-even-shell-pairing-christoffel-support-barrier.md), and the exact odd-weight affine-span criterion [MC-286](../../findings/MC-286-odd-shell-affine-span-criterion.md). No theorem is claimed that the required Christoffel certificate exists for the actual shell.

Let `A` be the degree-`m` feature matrix of the actual fixed-weight arithmetic shell and `v=1_Z` the virtual blind row. The endpoint-normalized energy

`C = inf_(v^*a=1) ||Aa||_2^2`

kills blindness when `C<1`; dually the minimum synthesis cost `Lambda` of `v` from the actual rows satisfies `C=1/Lambda`. MC-282 shows why this is a genuinely directional property: a structured separated-prime realization can be completely nonblind while still having `Lambda<1`, even tending to zero. Nonblindness, feature surplus and Legendre provenance do not imply favorable leverage.

MC-284 then shows that the localized shell is Boolean-complete on every lower-prime coordinate set whose effective conductor satisfies `Q(U)<=exp(b sqrt(log y))`. A certificate with energy below one therefore cannot live entirely in that moderate-conductor shadow.

MC-285 makes the obstruction much stronger for **even shell weight**. If `U` uses `d` sign coordinates, `K_U` projected patterns are occupied, and `N_y-K_U>=t`, equal-pattern pairing produces a size-`t` shell row whose projected product is the all-positive endpoint. Hence an even-weight certificate with energy `<1` must satisfy

`K_U>N_y-t`, and therefore `2^d>N_y-t`.

At live weight `t=O(log log y)` this forces `d` of order `log y` and, for prime coordinates, `log Q(U) >= (1/log 2+o(1)) log y log log y`. The even branch is therefore blocked by elementary multiplicity geometry far beyond the Page--Siegel conductor window; no delicate character-distribution theorem is needed to reach that necessary support scale.

MC-286 identifies the exact surviving **odd-weight** obstruction. Writing the distinct occupied projected cells as `S subset F_2^d`, some odd endpoint row exists iff

`0 in aff_F2(S)`.

Equivalently, there is no nonzero linear functional `lambda` that equals `1` on every occupied cell. In product-character language, the only support-level obstruction is a nonempty coordinate set `J` for which

`chi_J(r) = prod_(p in J) (p/r) = -1`

for every shell prime `r`. For a prescribed odd weight, MC-286 adds the exact same-cell pair-capacity condition after choosing an odd zero-sum nucleus; a minimal nucleus has size at most `d+1`.

The live source-native theorem is therefore no longer generic “high-conductor directional separation.” It is parity-sensitive. Even weights already face a deterministic logarithmic-support barrier. Odd weights reduce to a precise arithmetic question: **can the actual shell sustain a generated product-character direction that is identically negative, or can prime-character information rule out every such affine-hyperplane concentration in the growing-support regime?** Full Boolean pattern realization is sufficient but stronger than necessary.

**Boundary.** Excluding all affine obstructions would produce projected endpoint rows, not an RH bound by itself. The exact fixed-size occupancy condition still matters, and large coordinate support does not imply that a favorable Christoffel certificate exists. The result narrows the obstruction; it does not construct the inverse.