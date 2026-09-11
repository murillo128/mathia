# MI-016 — First-crossing localization turns interior positivity into a signed source-flux budget

**Evidence level:** supported; the finite-radius mean reserve and the first-mode cutoff identity are exact in the persisted Weil model, while the arithmetic contradiction remains open.

Localized Weil theory has now isolated the useful finite-radius object more sharply than a uniform discrepancy bound. WI-244--WI-246 calibrate the positive archimedean reserve and show that recombining the same positive digamma resolvents cannot improve its leading `a^-2` tariff. WI-247 then forces, under RH failure, an attained first odd zero mode `v` at a finite radius `a`, with strict odd positivity at every smaller radius `b<a`.

WI-248--WI-249 close the phase-blind alternatives. Uniform symbol control and even density-subtracted all-odd discrepancy estimates are exponentially more expensive than the first-crossing reserve. The source estimate must therefore be conditioned on the actual zero mode rather than hold over the whole odd window.

WI-250 provides that conditioning exactly. For a real even smooth cutoff `chi` supported in `(-b,b)`, the zero-mode equation and the localized Weil decomposition give

\[
q_b(\chi v)
=\mathcal E_{\chi,\mathrm{mean}}(v)
+\int_0^{2a}D_\chi(v;h)\,d\nu_a(h),
\]

where `nu_a` is the signed von-Mangoldt-minus-continuum measure and

\[
D_\chi(v;h)=\int (\chi(x+h)-\chi(x))^2
\operatorname{Re}(v(x+h)\overline{v(x)})\,dx.
\]

The nonlocal IMS defect has the explicit universal bound

\[
|\mathcal E_{\chi,\mathrm{mean}}(v)|
\le \frac14\zeta(3,5/4)\|\chi'\|_\infty^2\|v\|_2^2.
\]

Interior positivity therefore forces the directional arithmetic inequality

\[
\int_0^{2a}D_\chi(v;h)\,d\nu_a(h)
\ge
\lambda_b^-\|\chi v\|_2^2
-\frac14\zeta(3,5/4)\|\chi'\|_\infty^2.
\]

This is stronger conceptually than another global source envelope: every nested cutoff probes the same attained first-crossing mode, and the signed source term keeps its orientation instead of being replaced by total variation.

The remaining theorem is now quantitative. One needs either a lower bound for the interior reserve times captured mode mass, a zeta-specific upper constraint on the signed cutoff flux, or a compatibility theorem showing that the same source cannot satisfy the nested cutoff inequalities simultaneously. Merely improving the mean-side resolvent decomposition or proving a radius-only bound over arbitrary odd tests cannot close this gap.

**Boundary.** The localization identity and its IMS cost are not themselves RH evidence: ordinary operators with a genuine first crossing can satisfy analogous formulas. The missing contradiction must use the actual von-Mangoldt source. No lower rate for `lambda_b^-`, no uniform lower bound for `||chi v||`, and no incompatible signed-flux estimate has yet been proved.
