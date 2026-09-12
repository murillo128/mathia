# MI-016 — First-crossing localization compresses to one signed radial source-flux budget

**Evidence level:** supported through WI-251; the finite-radius mean reserve, first-mode localization identities, and layer-cake reduction are exact in the persisted Weil model, while the arithmetic contradiction remains open.

WI-244--WI-247 calibrate the positive archimedean reserve and force, under RH failure, an attained first odd zero mode `v` at a finite radius `a`, with strict odd positivity at every smaller radius. WI-248--WI-249 close phase-blind alternatives: uniform symbol and all-odd discrepancy bounds are exponentially more expensive than the first-crossing tariff, so the source estimate must be conditioned on the actual zero mode.

WI-250 supplies that conditioning. For a real even smooth cutoff `chi` supported in `(-b,b)`, the zero-mode equation gives an exact signed source-flux inequality, with an explicit nonlocal IMS error bounded by a multiple of `||chi'||_infty^2`. This preserves the prime-minus-continuum orientation but leaves a collar-width optimization.

WI-251 removes that optimization by averaging the full nested family of sharp radial cutoffs

\[
\eta_r=\mathbf1_{\{|x|<r\}}.
\]

Sharp multiplication is form-admissible for almost every radius, and the layer-cake identity

\[
\int_0^a(\eta_r(x)-\eta_r(y))^2dr
=\bigl||x|-|y|\bigr|
\]

converts the family of cutoff defects into one exact radial kernel. For the same first zero mode,

\[
\overline{\mathcal E}_{a,\mathrm{mean}}(v)
+\int_0^{2a}R_v(h)\,d\nu_a(h)
\ge
\int_0^a\lambda_r^-\|\eta_rv\|_2^2\,dr,
\]

where

\[
R_v(h)=\int\bigl||x+h|-|x|\bigr|\,
\operatorname{Re}(v(x+h)\overline{v(x)})\,dx.
\]

The integrated gap-times-mass term is strictly positive. The mean localization cost is finite and universal at fixed radius:

\[
|\overline{\mathcal E}_{a,\mathrm{mean}}(v)|
\le C_{\rm lc}(a)
<\frac14\zeta\!\left(2,\frac54\right).
\]

Thus the old `O(ell^{-2})` smooth-collar penalty is not a structural obstruction. The nested first-crossing constraints have been compressed to a single necessary arithmetic compatibility condition for the **signed radial von-Mangoldt flux** of the forced zero mode.

The remaining theorem must use the actual source. Either prove a zeta-specific upper/incompatibility bound for `int R_v dnu_a`, or obtain independent quantitative information on the positive integrated gap profile and combine it with that signed flux. Taking absolute values would return to the phase-blind losses already ruled out.

**Boundary.** Layer-cake localization is classical and ordinary operators with a genuine first crossing can satisfy analogous identities. WI-251 does not supply the missing arithmetic sign, a lower rate for the interior eigenvalue profile, or RH. Its contribution is to remove the arbitrary collar parameter and identify one finite source-oriented observable as the remaining localization gate.