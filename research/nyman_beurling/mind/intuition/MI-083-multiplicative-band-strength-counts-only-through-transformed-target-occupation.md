# MI-083 — Multiplicative band strength splits into uniform coercivity and target occupation

**Evidence level:** exact synthesis from NB-292--[NB-295](../../findings/NB-295-aggregate-off-critical-displacement-forces-conditioning-free-multiplicative-band-log-volume.md), for finite off-critical zero packets after the lower section is first-free-surjective.

NB-292 identifies a genuine positive matrix carrier beyond the scalar sample/pivot data that matched controls can reproduce, and NB-293 gives its exact destination map. Neutralizing the multiplicative quotient band by minimum-norm old-section sample repair maps it onto the new first-free null block, with gain

`Delta(y)=x^* M(I+M)^(-1)x`,

where `A=D_Z(m)K D_Z(m)^*`, `M=A^(-1/2) Gamma A^(-1/2)` and `x=A^(-1/2)y`. Without further structure, a large trace, determinant, operator norm or rank says nothing about the gain for a prescribed datum unless that datum occupies the strong spectral directions.

NB-294 identifies the regime in which this target-occupation issue disappears. If `delta_min=min_j(Re rho_j-1/2)` and `kappa(K)` is the lower-section sampling condition number, then the canonical dilation and section nesting force

`M >= (m^(2 delta_min)/kappa(K)-1)_+ I`.

Thus `2 delta_min log m-log kappa(K)->+infinity` is a sufficient **uniform coercivity gate**: every target direction receives asymptotically complete relative gain. The generic target-miss counterexample from NB-293 cannot occur above this gate because the entire whitened spectrum is large.

NB-295 exposes a weaker pressure that does not pay the condition number. Writing `H_Z=sum_j(Re rho_j-1/2)` and `delta_bar=H_Z/|Z|`, the exact determinant factorization gives

`det(I+M)=m^(2H_Z) det(K^+)/det(K) >= m^(2H_Z)`.

Consequently `sum log(1+mu_j)>=2H_Z log m` and `mu_max(M)>=m^(2 delta_bar)-1`. If `delta_bar log m` diverges, at least one generalized band mode becomes arbitrarily strong and one optimally chosen target direction receives asymptotically complete relative gain, even when a tiny minimum displacement or poor conditioning destroys the uniform NB-294 estimate.

The two gates answer different questions. The minimum-displacement/conditioning gate controls the **worst target direction**; the average-displacement determinant gate controls only total log-volume and therefore guarantees a **best direction**. Large aggregate pressure can concentrate spectrally, so it does not by itself certify the actual Ford first-free datum. In the intermediate regime where the uniform gate fails but the determinant gate is strong, the live arithmetic quantity is precisely the projection of the transformed Ford datum onto the forced strong spectral subspace, or an equivalent canonical pairing such as `d^*A^(-1)y`.

This refines rather than abandons the target-occupation principle: target alignment is unnecessary once source geometry produces a uniform spectral floor, but remains indispensable when the source proves only existential spectral capacity. The useful distinction is therefore not “matrix strength versus target occupation” in all regimes; it is **uniform coercivity versus aggregate capacity versus actual target occupation**.

**Boundary.** Both coercivity statements compare the enlarged canonical section with the old **dilated** section. They quantify repair of dilation-induced first-free synthesis cost, not a direct decrement of the ordinary Nyman distance or the finite-section excess. NB-295 also does not show that determinant growth spreads across many modes. No RH implication follows without a bridge from these multiplicative interpolation gains to the actual Nyman approximation quantity.