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

The clue is therefore **accepted** as a viable first-mode-specific route, but not resolved. The exact IMS/source budget is now established; the unresolved gate is quantitative coercivity. Current results do not lower-bound the product `lambda_b^- ||chi v||_2^2` at a useful scale, do not force enough interior mass, and do not upper-bound the signed source flux on the actual zero-mode class. Future work should target those quantities, or a compatibility theorem for several nested cutoffs, rather than re-derive the localization identity or return to a uniform all-odd discrepancy bound.