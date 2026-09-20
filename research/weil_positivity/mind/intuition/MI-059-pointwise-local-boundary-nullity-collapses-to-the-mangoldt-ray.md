# MI-059 — Pointwise-local boundary nullity collapses exactly to the Mangoldt ray

**Evidence level:** exact RH-independent synthesis from [WP-386](../../findings/WP-386-pointwise-local-positive-boundary-selectors-collapse-to-the-mangoldt-ray.md), extending the boundary classifications of WP-384--WP-385. The theorem is for positive multiplication-form geometry in the canonical boundary coordinate; nonlocal kernels and delayed finite--archimedean couplings are outside its scope.

WP-385 excludes every closed positive boundary form that remains stationary under the canonical dilation action. WP-386 tests the most immediate nonstationary escape without retaining that symmetry: let `nu` be an arbitrary positive Borel measure on `(0,infinity)` and measure the WP-384 boundary profiles pointwise by `Q_nu(f,g)=int f overline(g) dnu`.

Exact mixed-shell nullity is then completely rigid. Requiring `Q_nu(h_m)=0` for every `m` with at least two distinct prime divisors is equivalent to

`nu([1,infinity))=0`.

The converse is not merely a common-zero-set argument. For every finite interval `[1,X]`, choosing two distinct primes `p,q>X` gives the exact profile `h_pq(x)=H_floor(x)/sqrt(pq)>0` throughout that interval. Positivity of the form means nulling that one mixed shell already removes all measure from `[1,X]`; exhausting `X` forces support into `(0,1)`.

On the forced support interval the arithmetic family collapses exactly:

`h_m(x)=Lambda(m)/sqrt(m)` for `0<x<1`.

Consequently every shell Gram has the form

`Q_nu(h_m,h_n)=M_nu Lambda(m)Lambda(n)/sqrt(mn)`,

and every admissible local-anchor cross term factors through the same scalar `Lambda(m)/sqrt(m)`. The form can recover exact prime-power support, but only on one Mangoldt ray. Changing atoms, singular measures, discontinuous densities or arbitrary nonstationary local weights cannot create a second independent shell-dependent channel.

This complements WP-385 rather than subsuming it. Stationary positive geometry is rigid in Mellin frequency because the finite Euler factors are boundedly invertible; nonstationary pointwise-local geometry is rigid in the native boundary coordinate because fresh mixed shells are strictly positive off `(0,1)`. The surviving mechanism must therefore change the operator category itself: genuinely nonlocal/off-diagonal boundary kernels, derivative/interface forms, a finite-`q` prelimit effect, or delayed finite--archimedean interaction before exact selection.

**Boundary.** WP-386 does not prove that every positive boundary form collapses to rank one. Off-diagonal kernels can use correlations between distinct boundary points, derivative energies are not multiplication forms, and a signed or indefinite finite--archimedean assembly may postpone positivity until a later stage. Those are structurally different categories and require their own source-forcing and sign audits.
