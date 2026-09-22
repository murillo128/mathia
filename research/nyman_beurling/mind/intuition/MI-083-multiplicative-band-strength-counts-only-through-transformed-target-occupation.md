# MI-083 — Multiplicative band strength counts only through transformed target occupation

**Evidence level:** exact synthesis from NB-292 and [NB-293](../../findings/NB-293-multiplicative-quotient-bands-neutralize-into-an-exact-sample-null-innovation-cocycle.md), for a finite zero packet after the lower section is first-free-surjective.

NB-292 identifies a genuine positive matrix carrier beyond the scalar sample/pivot data that matched controls can reproduce. NB-293 closes the next logical gap: it gives the exact map from that carrier into the minimum-norm target cost. Neutralizing the multiplicative quotient band `W_(m,n,Z)` by its old-section sample repair maps it bijectively onto the new first-free-null block

`Q_(m,n,Z)=D_(mn-1,Z) \ominus S_mD_(n-1,Z)`.

If `g_(m,n)(y)` is the old minimum-norm realization of first-free datum `y`, the whole gain from the multiplicative enrichment is exactly

`Delta_(m,n,Z)(y)=||P_(Q_(m,n,Z))g_(m,n)(y)||^2`.

Whitening the band Gram makes the accounting explicit. With `A=D_Z(m)K_(n-1,Z)D_Z(m)^*`, `M=A^(-1/2)Gamma_(m,n,Z)A^(-1/2)` and `x=A^(-1/2)y`,

`Delta=x^*M(I+M)^(-1)x`.

Therefore a large trace, determinant, operator norm, rank or scalar dilation loss is not target leverage by itself. What matters is the spectral mass of the **actual transformed datum** in the directions where the canonical band is strong. This is the exact multiplicative version of the target-aware null-innovation principle from NB-287.

The canonical innovation defect gives one explicit occupation certificate: `Delta` is bounded below by the squared pairing `|d^*A^(-1)y|^2` divided by its exact repair cost. Conversely, a band direction that is already sample-null is unchanged by neutralization but remains orthogonal to the old source, so it is silent for this direct enrichment. The existence of null-band mass and its immediate target usefulness are different statements.

Multiplicative composition has the same discipline. The gains telescope only after transporting the datum contravariantly by the relevant `D_Z(k)^(-1)` action. Reusing a fixed datum across multiplicative scales would erase part of the exact source geometry.

The remaining arithmetic problem is thus sharply localized: prove a moving-packet lower bound on transformed target occupation, for example through `d^*A^(-1)y`, or an equivalent spectral projection quantity strong enough to control the future-null Parseval tail. The carrier and its destination map are already known; the missing resource is source-specific occupation.

**Boundary.** The identities are for finite zero packets beyond the first-free surjectivity cutoff. NB-293 proves no uniform occupation lower bound and no Nyman approximation rate. Generic matrix size or conditioning cannot substitute for the missing arithmetic pairing.