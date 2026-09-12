---
id: CLUE-weil-inertia-first-odd-mode-cutoff-flux-constraint
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-247-rh-failure-forces-a-finite-odd-zero-mode.md
  - research/weil_inertia/findings/WI-249-odd-compact-window-discrepancy-has-exponentially-large-recurrent-quasimodes.md
---

# Do interior cutoff flux identities constrain the arithmetic phase of a first odd zero mode?

## Observation

WI-247 supplies more than an odd compactly supported test: a hypothetical first odd zero mode v at radius a satisfies A_a v=0 while every smaller odd window has strictly positive bottom eigenvalue. WI-249's recurrent odd carriers can have discrepancy of order e^a/a, but they are not asserted to satisfy either the zero-mode equation or the first-crossing constraints. Consequently another uniform upper bound on discrepancy over all odd tests is the wrong problem.

A concrete candidate-specific test is to cut the same hypothetical eigenvector into strictly smaller windows and retain the exact signed localization defect. Smooth even cutoffs preserve odd parity. Their quadratic identities compare the original null equation with the already-positive interior forms, without selecting arbitrary new test vectors or discarding the prime-minus-continuum sign.

## Research question

Use the closed odd form q_a=Q_W^a=Q_mean-2 Delta_Lambda^a of WI-247, with zero extension outside [-a,a]. Let ||v||_2=1, A_a v=0, and lambda_b^->0 for every b<a. For a real even smooth multiplier chi supported in (-b,b), define by polarization

\[
\mathcal E_\chi^a(v)
:=q_a(\chi v)-\operatorname{Re}q_a(v,\chi^2v).
\]

Can its exact arithmetic representation, imposed simultaneously for interior cutoffs of different widths, yield a quantitative collar-mass or signed-correlation restriction on v that defeats WI-249's phase-aligned mechanism? The starting identity to audit is

\[
\mathcal E_\chi^a(v)=q_b(\chi v)
\ge\lambda_b^-\|\chi v\|_2^2.
\]

This is a necessary first-mode constraint, not yet the sought arithmetic inequality. The substantive target is a source-derived consequence of these constraints: either a strictly insufficient discrepancy charge relative to Q_mean(v)/2, or a quantitatively restricted phase/mass class on which that charge can be tested independently.

## Why it may matter

The discrepancy tariff cannot be closed by improving a phase-blind bound: WI-249 rules that out. Cutoff flux instead weights the same signed prime translations by where the candidate changes between interior and collar. It offers a specific way for positivity at smaller radii to enter the arithmetic estimate. It also makes falsification possible: a proposed collar restriction must be checked against the recurrent carriers and against an operator with a genuine first crossing.

## Decisive test

First justify multiplication by smooth chi and chi^2 on the actual logarithmic form domain. Start on the smooth odd core and pass to the closure. Do not silently grant H^1 regularity, classical endpoint values, or an operator-domain double commutator to v. The formal operator identity

\[
\mathcal E_\chi^a(v)
=-\tfrac12\langle v,[\chi,[\chi,A_a]]v\rangle
\]

is only a sign/domain calibration; the polarized form is the primary object.

Retain WI-249's exact signed source measure

\[
d\nu_a(h)=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dh)
-e^{h/2}\mathbf1_{(0,2a)}(h)\,dh
\]

and define

\[
D_\chi(v;h)=\int_{\mathbb R}(\chi(x+h)-\chi(x))^2
\operatorname{Re}\bigl(v(x+h)\overline{v(x)}\bigr)\,dx.
\]

Reconstruct, with consistent polarization, the candidate localization formula

\[
\mathcal E_\chi^a(v)
=\mathcal E_{\chi,\mathrm{mean}}(v)
+\int_0^{2a}D_\chi(v;h)\,d\nu_a(h).
\]

The minus sign in q_a=Q_mean-2 Delta is essential. Compute the mean-sector term in the same normalization, rather than replacing it by an unrelated local Dirichlet energy.

Take cutoffs equal to one on a central interval and transitioning across collars of specified width ell, all strictly inside [-a,a]. Before any absolute bound, keep the exact overlap and the factor (chi(x+h)-chi(x))^2 at each h=log n. Compare at least two nested cutoffs so that one can distinguish interior mass from mass supported near the outermost collar. Seek a quantitative inequality whose coefficients follow from the actual source and controlled cutoff errors. Mere positivity lambda_b^->0 is available; a uniform lower bound as b approaches a is not. Any quantitative use of lambda_b^- must be established independently, not assumed as the missing coercivity.

Calibrate against v_t=w sin(tx)/||w sin(tx)|| from WI-249. Evaluate both the localized source term and the nonzero weak eigen-equation residual q_a(v_t,chi^2 v_t). Large discrepancy alone cannot make that residual vanish. An exclusion of these carriers is useful only if the estimate extends to the relevant candidate class or gives an independently testable restriction on it; eliminating one chosen envelope does not exclude a general first mode.

Also test an ordinary Dirichlet operator -d^2/dx^2-c, c>0, in its odd sector as the radius passes its first odd zero. It has an authentic first crossing and obeys the abstract cutoff identities. Thus a contradiction based only on first-crossing minimality and the double-commutator algebra is invalid: the decisive extra sign or cancellation must come from the actual Weil source.

A meaningful positive outcome is a quantitative source/collar inequality beyond the null equation itself, with a stated implication for the tariff in WI-247. A meaningful negative outcome shows that the tested cutoff constraints still admit the dangerous phase/mass geometry, identifying the absent input. Simply re-proving the localization identity, or restating the desired discrepancy bound as a definition, does not resolve this clue.

## Evidence boundary

No collar estimate, prime-phase exclusion, first-mode contradiction, or RH consequence is supplied. The standard localization algebra is a proposed diagnostic, not a new positivity mechanism. WI-247 provides the candidate class and smaller-window positivity; WI-249 provides the adversarial calibration, not a first-zero-mode counterexample. Suzuki's localized-form framework is the existing primary-source anchor, arXiv:2606.09096; its form-domain and normalization statements must be checked when reconstructing the test. Check current findings and adjacent review sidecars before relying on either input.

## Research disposition

`WI-250-first-odd-mode-cutoff-flux-has-an-explicit-nonlocal-ims-budget.md` validates the candidate localization formula on the closed form domain, fixes the source sign and factor, and computes the mean-sector error exactly from the positive exponential-resolvent expansion. For every first odd zero mode and every even cutoff supported in `(-b,b)`, it obtains

\[
\int_0^{2a}D_\chi(v;h)\,d\nu_a(h)
\ge
\lambda_b^-\|\chi v\|_2^2
-
\frac14\zeta\!\left(3,\frac54\right)\|\chi'\|_\infty^2.
\]

`WI-251-layer-cake-averaging-removes-the-smooth-ims-collar-cost.md` then integrates the full nested family of sharp radial cutoffs. Sharp cutoff multiplication is form-admissible for almost every radius, and the layer-cake identity converts the nested IMS defects to the absolute-radius metric `||x|-|y||`. This removes the artificial `O(ell^{-2})` smooth-collar cost and gives the single necessary first-mode constraint

\[
\int_0^{2a}R_v(h)\,d\nu_a(h)
\ge
\int_0^a\lambda_r^-\|\mathbf1_{|x|<r}v\|_2^2\,dr
-C_{\rm lc}(a),
\]

where the gap-times-mass integral is strictly positive and

\[
C_{\rm lc}(a)
=\frac14\sum_{m\ge1}
\frac{(1-e^{-2b_ma})^2}{b_m^2}
<\frac14\zeta\!\left(2,\frac54\right).
\]

`WI-252-first-prime-reflection-breaks-odd-semigroup-positivity.md` closes a tempting phase shortcut. After unitary transfer of the odd form to `(0,a)`, the `p=2` source atom contributes a positive reflected Hankel interaction on `u+t=log 2`; disjoint positive bumps concentrated on that anti-diagonal violate the first Beurling--Deny criterion for every `a>(log 2)/2`. Zhu's certified compact-window theorem (arXiv:2608.24827v2) gives strict odd-sector positivity through `a=0.8`, hence any first odd RH-failure radius satisfies `a_*^->0.8` and necessarily lies in this non-order-preserving regime. Thus constant phase of the first odd mode cannot be imported from generic Perron--Frobenius/Krein--Rutman ground-state theory; any usable phase/nodal restriction must itself be zeta-specific.

The clue remains **accepted**, not resolved: localization and nested-cutoff compatibility now impose a finite quantitative signed-correlation restriction without choosing a collar width, but no zeta-specific upper bound for this radial von-Mangoldt flux is known. The live gate is therefore narrower: control that exact signed radial flux on the first-zero-mode class, combine it with independent information on the positive integrated gap-times-mass term, or prove a genuinely arithmetic phase restriction not based on semigroup positivity. Returning to a uniform all-odd discrepancy bound, optimizing a single smooth collar, or assuming a one-signed half-profile from generic ground-state theory would discard or contradict structure already established by `WI-249`--`WI-252`.