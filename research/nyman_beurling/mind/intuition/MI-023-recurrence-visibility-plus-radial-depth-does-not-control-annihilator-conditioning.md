# MI-023 — Recurrence visibility plus radial depth does not control annihilator conditioning

**Evidence level:** exact matched-control route boundary from [NB-133](../../findings/NB-133-zero-count-visibility-and-vinogradov-korobov-depth-still-permit-superpolynomial-annihilator-collapse.md), refining the source-faithful visibility regime of `NB-132`

NB-132 shows that for genuine right-half-plane zeta zeros in a fixed-width polynomial-height band, explicit zero counting can force the recurrence rank below the natural `q`-geometric observation depth. In that regime the formal linear-rank interpolation escape is removed: the annihilating recurrence is visible inside the natural prefix.

NB-133 proves that visibility plus the current radial source law is still not a conditioning theorem. It constructs simple formal packets with `d_R=c log R+O(1)` inside the same numerical rank allowance, at polynomial height and safely on the allowed side of the Vinogradov--Korobov zero-free boundary, while their sampled characteristic roots occupy a shrinking phase arc around the missing target root.

For these packets the full recurrence remains visible, yet the exact normalized NB-124 annihilator margin satisfies

`mathfrak s_R <= R^(-(4c/3+o(1)) log log R)`,

so it is smaller than every fixed power of `R`. The collapse is angular: zero counting controls population and the zero-free region controls radial depth, but neither controls the relative phase arrangement of `Theta(log R)` roots.

The reusable boundary is therefore: **effective-rank visibility and radial separation are not enough to make an annihilator coercive**. A target-margin theorem needs source-specific arrangement information as well: angular anti-clustering or spacing for the actual sampled roots, coupling across multiplicatively independent bases, natural-grid phase geometry stronger than one-base recurrence, or a different target-bearing functional that does not multiply all rootwise distances.

**Boundary.** The NB-133 packet is a matched formal control, not a set of zeta zeros. Its superpolynomially small margin does not prove near-perfect Nyman target capture; it proves that the current NB-124 certificate cannot obtain a polynomial separation from rank/count information plus Vinogradov--Korobov horizontal depth alone. A theorem about actual zeros may still exclude the phase cluster through additional source geometry.