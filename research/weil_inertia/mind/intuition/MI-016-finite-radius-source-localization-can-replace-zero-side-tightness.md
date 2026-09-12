# MI-016 — First-crossing localization compresses to one signed radial source-flux budget, but prime reflection removes the generic positive-ground-state shortcut

**Evidence level:** supported through WI-252; the finite-radius reserve, first-mode localization identities, layer-cake reduction, and odd-sector Beurling--Deny obstruction are exact/anchored in the persisted Weil model, while the arithmetic contradiction remains open.

WI-244--WI-247 calibrate the positive archimedean reserve and force, under RH failure, an attained first odd zero mode `v` at a finite radius `a`, with strict odd positivity at every smaller radius. WI-248--WI-249 close phase-blind alternatives: uniform symbol and all-odd discrepancy bounds are exponentially more expensive than the first-crossing tariff, so the source estimate must be conditioned on the actual zero mode.

WI-250 supplies that conditioning. WI-251 then removes the arbitrary smooth-collar optimization by averaging the nested sharp cutoffs `eta_r=1_{|x|<r}`. The layer-cake identity turns the entire cutoff family into one radial metric and gives

\[
\overline{\mathcal E}_{a,\mathrm{mean}}(v)
+\int_0^{2a}R_v(h)\,d\nu_a(h)
\ge
\int_0^a\lambda_r^-\|\eta_rv\|_2^2\,dr,
\]

where the right side is strictly positive and the mean localization cost has a finite universal bound. The remaining localization gate is therefore the **signed radial von-Mangoldt flux** of the forced first zero mode.

A natural attempted shortcut is to prove that the positive-half profile of this first odd mode has one sign. For such a profile the radial correction satisfies a favorable sign identity, which would constrain the layer-cake flux. WI-252 shows why that sign cannot be imported from ordinary ground-state theory.

Transfer the odd form to `L^2(0,a)`. A prime-power shift `h=log n` contributes

\[
-2w_nA_h(g)+w_nH_h(g),
\]

where `H_h` is a reflected anti-diagonal/Hankel interaction. For every `a>\log2/2`, the `p=2` term alone produces disjoint nonnegative bumps `f,g` with

\[
q_a^-(f,g)>0.
\]

This violates the first Beurling--Deny criterion, so the associated odd half-line semigroup is not positivity preserving. Zhu's certified compact-window positivity through `a=0.8` implies that any hypothetical first odd RH-failure crossing satisfies `a_*^->0.8>\log2/2`. The first crossing therefore occurs only after the arithmetic reflection has already destroyed the standard cone order.

The structural lesson is concrete: **the same prime source whose signed flux must be controlled also destroys the generic order mechanism that would have made that flux easy to sign**. Constant phase is not refuted, but it must come from the zeta-specific eigen-equation, another source-sensitive invariant, or a different cone/order compatible with the reflected atoms.

The live routes are correspondingly narrow: prove a direct incompatibility/upper bound for `int R_v dnu_a`; obtain quantitative information on the positive integrated gap-times-mass term; derive a phase/nodal theorem from the signed source itself; or identify a genuinely different order structure. Taking absolute values or invoking Perron--Frobenius/Krein--Rutman without checking Beurling--Deny reintroduces a false shortcut.

**Boundary.** WI-252 proves failure of positivity preservation, not a nodal theorem. The first zero mode may still be one-signed for a different reason. The application to the forced first crossing uses the external certified positivity radius; the local `p=2` obstruction itself does not.