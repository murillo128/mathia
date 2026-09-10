# PL-255 — A Dirac square root cannot repair designed pseudo-Laplacian zero-selection incompleteness

## Claim

`PL-254` leaves a natural escape: replace the second-order designed pseudo-Laplacian by a first-order self-adjoint Dirac-type operator and hope that the first-order formulation has a sufficiently large discrete spectrum to capture the full principal zeta divisor. There is a sharp operator-theoretic control on that move.

If a self-adjoint operator `D` satisfies

`D^2 = T_theta`

**as an equality of self-adjoint operators**, where `T_theta` is one of the Bombieri–Garrett designed pseudo-Laplacians audited in `PL-254`, then `D` cannot enlarge the selected zero set at all. Every `D`-eigenvector with eigenvalue `lambda` is a `T_theta`-eigenvector with eigenvalue `lambda^2`, and conversely the spectral measure of `D^2` is the push-forward of the spectral measure of `D` under `x -> x^2`. A grading or sign choice can split a positive `T_theta` eigenvalue into `+/-sqrt(mu)`, but cannot create a new squared eigenvalue. Therefore the selector incompleteness of `T_theta`, including the conditional `94%` ceiling from `PL-254`, survives any literal self-adjoint square-root construction.

The only genuine first-order escape is consequently a **domain/coupling escape**: the first-order operator must be defined so that its self-adjoint domain changes the squared operator. A formal differential-expression identity such as `D_formal^2=-Delta` is not enough. For a closed operator,

`Dom(D^2) = {u in Dom(D) : D u in Dom(D)}`,

so a first-order boundary or distributional condition can make the operator square differ from the Friedrichs extension of the corresponding restricted Laplacian even when the interior differential expressions square identically. This domain distinction is the load-bearing place where a Dirac-type program could evade the designed-pseudo-Laplacian sparsity obstruction.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`.

The designed pseudo-Laplacian zero-selection theorem and conditional `94%` bound are literature from Bombieri–Garrett and already anchored in `SOURCES.md` item 85 / `PL-254`. The square-spectrum inheritance and domain criterion are direct consequences of the spectral theorem and the definition of an operator square. No new Dirac spectral theorem, zeta-zero theorem, or completeness result is claimed.

## 1. Exact same-square inheritance

Let `D=D*` on a Hilbert space and set `T=D^2`. By functional calculus,

`T = integral_R x^2 dE_D(x)`.

Hence the spectral measure of `T` is the push-forward of `E_D` by `x -> x^2`. At the point-spectrum level this is elementary: if

`D psi = lambda psi`,

then

`T psi = D^2 psi = lambda^2 psi`.

Conversely, on an eigenspace of `T` with eigenvalue `mu>0`, `D` preserves that eigenspace and its spectrum there is contained in `{+sqrt(mu),-sqrt(mu)}`. Thus a first-order square root can add sign/chirality information, but not additional values of `mu`.

Apply this to the designed pseudo-Laplacian `T_theta` from `PL-254`. Its discrete eigenparameters are not the full zero divisor: they satisfy the target-relative secular/domain selector in addition to the relevant Eisenstein-period zero condition. If `D^2=T_theta` as operators, the point spectrum of `D` projects exactly into that already-selected point spectrum. A zeta zero excluded by the `T_theta` selector cannot reappear merely because the same operator has been written as a square.

Under the same hypotheses used by Bombieri–Garrett for their density obstruction, this immediately inherits the conditional counting ceiling. If one fixed `T_theta` can contain at most `94%` of the ordinary Riemann-zeta zeros as eigenparameters, no self-adjoint `D` with `D^2=T_theta` can contain the missing zeros in a way whose squares are the corresponding `T_theta` eigenvalues. The statement is conditional only to the extent that the numerical `94%` bound is conditional; the same-square spectral inheritance is unconditional.

## 2. Formal factorization is not operator equality

The useful escape hatch is also exact. For an unbounded closed operator `D`, the square is not determined solely by the formal differential expression. Its domain is

`Dom(D^2) = {u in Dom(D) : D u in Dom(D)}`.

A self-adjoint realization of a first-order Dirac expression therefore carries boundary/domain information twice when squared. By contrast, the Bombieri–Garrett operator is obtained by taking a specific symmetric restriction of a second-order automorphic Laplacian and then a Friedrichs extension. There is no general theorem saying that “first restrict/fix a self-adjoint Dirac domain, then square” equals “restrict the Laplacian, then take the Friedrichs extension.”

This order-of-operations issue is not cosmetic. If the two constructions give the same self-adjoint operator, Section 1 proves that no spectral-completeness gain is possible. If they give different self-adjoint operators, then any enlarged discrete spectrum comes from the changed domain/boundary/coupling structure, not from first-order notation itself. A viable Dirac route must therefore identify the exact first-order domain and prove that its square has a different selector with stronger completeness properties.

This also prevents a common heuristic shortcut in automorphic settings. An interior identity of differential expressions of the form

`D_formal^2 = -Delta`

does not establish equality between the corresponding self-adjoint realizations. The RH-relevant content would have to lie precisely in the global automorphic boundary conditions, distributional source, grading, or other domain data that survives this distinction.

## 3. Relation to the prime-lattice frontier

The result does not manufacture new prime-exponent geometry. It is a route restriction on the global operator structure that the canonical research mandate explicitly allows as a possible way of preserving prime arithmetic through analytic continuation.

The prime lattice supplies the rational-prime Euler/explicit-formula channel and the frequencies `log p`, but `PL-254` already showed that the decisive self-adjointness came from global automorphic geometry plus a target-relative Friedrichs domain. The present control says that passing from that second-order realization to a first-order square root cannot, by itself, repair the missing reverse implication

`zeta zero  =>  spectral point`.

Therefore a first-order construction should be audited by asking two separate questions:

1. Is its self-adjoint square literally the already-audited designed pseudo-Laplacian? If yes, spectral incompleteness is inherited.
2. If not, what precise domain/coupling term changes the squared operator, and why does that change force **all** principal zeta zeros, with multiplicities, into one self-adjoint spectrum rather than merely changing which sub-divisor is selected?

Without an answer to the second question, “use a Dirac operator” is not yet a mechanism relevant to RH.

## 4. Prior art and novelty audit

The primary arithmetic source remains:

- **Enrico Bombieri, Paul Garrett**, “Designed Pseudo-Laplacians,” arXiv:2002.07929 [math.NT] (2020), authors' current manuscript at the University of Minnesota. This is `SOURCES.md` item 85 and the theorem-level anchor for `PL-254`.

A current-literature audit was run specifically around automorphic Dirac operators, designed pseudo-Laplacians, Friedrichs extensions, and zeta-zero spectral constructions. It confirms that Dirac-type automorphic operators are an active proposed escape from the small-discrete-spectrum problem, but the audit did not locate a published theorem asserting that a self-adjoint Dirac operator whose square is the same designed pseudo-Laplacian captures a larger zeta-zero set. That absence is used only as a novelty boundary, not as evidence for a nonexistence theorem.

The mathematical control stored here is elementary functional calculus plus domain bookkeeping. It is not claimed as a novel theorem. Its value is diagnostic: it separates a vacuous square-root reformulation from the only place a first-order program can add mathematical content, namely a genuinely different self-adjoint domain or coupling before squaring.

Internal duplication was checked against the current local frontier. `PL-033` audits a non-self-adjoint automorphic scattering generator that realizes the full zero divisor; `PL-043` audits Dirac/canonical-system and Sonine routes; `PL-044` audits localized Weil self-adjoint extensions; and `PL-254` isolates the designed pseudo-Laplacian selector gap. None of those findings records the same-square spectral-inheritance test as the explicit gate for a Dirac escape from `PL-254`.

## 5. Adversarial boundaries

1. **Not a no-go theorem for automorphic Dirac operators.** A first-order operator with a different self-adjoint domain, boundary triple, source coupling, grading, or Hilbert space may have a square different from `T_theta` and can evade this control.
2. **Formal equality is insufficient.** The conclusion requires `D^2=T_theta` as self-adjoint operators, including domains, not merely equality of differential expressions on compactly supported smooth vectors.
3. **Signs do not fix completeness.** Passing from `mu` to `+/-sqrt(mu)` can add symmetry but cannot increase the set of squared spectral values.
4. **The `94%` number remains conditional.** It uses RH plus Montgomery pair correlation exactly as in `PL-254`; the unconditional statement is only inheritance of whatever selector/spectral set the fixed `T_theta` actually has.
5. **A changed domain can matter enormously.** This finding must not be used to reject a Dirac proposal merely because its interior square is `-Delta`. The correct audit is whether its operator square, with domain, coincides with the old pseudo-Laplacian.
6. **No zeta divisor is created by functional calculus.** The spectral theorem transports an existing self-adjoint spectrum; arithmetic completeness still needs an independent theorem coupling the full principal zeta divisor to that spectrum.

## Research implication

The immediate frontier after `PL-254` is narrower than “try a Dirac operator.” A useful first-order construction must exhibit and exploit a **domain-level noncommutativity of the operations restriction/extension and squaring**. It should then prove that this changed global domain eliminates the selector loss rather than merely replacing one selector by another.

For future proposals, the falsification test is sharp: compute `Dom(D^2)` and compare the resulting self-adjoint square with the designed pseudo-Laplacian domain before interpreting any enlarged first-order spectrum. If the square is the same operator, the route is already blocked by `PL-254`; if it is different, the difference itself is the mathematical object that must carry the missing global arithmetic completeness.