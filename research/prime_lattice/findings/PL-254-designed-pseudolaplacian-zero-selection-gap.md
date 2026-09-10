# PL-254 — Designed pseudo-Laplacians self-adjointize only a selected L-zero subset

## Claim

Bombieri–Garrett's designed pseudo-Laplacians provide a sharp prior-art control for a tempting Hilbert–Pólya escape left open by `PL-033` and `PL-253`: start from automorphic Eisenstein/scattering data carrying the zeta divisor, impose a natural global boundary/period condition, and take a self-adjoint Friedrichs extension so that spectral reality forces the critical line.

That mechanism exists, and it genuinely does force critical-line localization **for every zero that survives the spectral selector**. What it does not supply is the converse statement that every relevant zeta zero becomes an eigenvalue. For a Heegner distribution `theta_k` attached to a complex quadratic field `k`, the Eisenstein period has the form

`theta_k E_s = C_k(s) zeta_k(s)/zeta(2s)`,

with an explicit nonzero elementary factor `C_k(s)` in the spectral range. If `lambda_w=w(1-w)>1/4` is an eigenvalue of the designed self-adjoint pseudo-Laplacian, then the corresponding Eisenstein period vanishes, hence the relevant Dedekind-zeta factor vanishes. Self-adjointness makes `lambda_w` real, and `lambda_w>1/4` then forces `Re(w)=1/2`.

However, the L-zero condition is only necessary. The exact eigenvalue criterion contains an additional target-relative resolvent/boundary condition, equivalently a zero of a scalar secular function `theta u_(theta,w)`. Thus the operator spectrum is in general a **selected sub-divisor** of the L-zero set rather than the whole divisor. Bombieri–Garrett further prove a spacing constraint for these selected eigenparameters; assuming RH and Montgomery pair correlation, at most `94%` of the ordinary Riemann-zeta zeros can occur as eigenparameters for any one designed operator of the audited type.

The line-specific consequence is decisive for the route "self-adjointize the existing automorphic zeta scattering channel by a Friedrichs/boundary restriction": self-adjointness solves axis localization only after a selector has already discarded part of the divisor. The missing theorem is not spectral reality but **spectral completeness of the principal zeta divisor**.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`.

The pseudo-Laplacian construction, period formula, self-adjointness, necessary zero condition, exact secular condition, spacing theorem, and conditional `94%` cap are literature. The comparison with the prime-lattice frontier is derived. No new pseudo-Laplacian theorem, zero-density theorem, or Hilbert–Pólya construction is claimed.

## 1. A self-adjoint automorphic operator really does localize selected zeros

Bombieri and Garrett work in the automorphic Hilbert space for `SL_2(Z)\H` and restrict the invariant Laplacian by imposing distributional boundary conditions. Given a suitable distribution `theta`, they form a symmetric restriction and its Friedrichs extension `\widetilde S_theta`. The resulting operator is self-adjoint, and its discrete spectrum above the continuous threshold is described through Eisenstein spectral data and a meromorphic resolvent vector `u_(theta,w)`.

For the arithmetic examples relevant here, `theta` is built from Heegner points of a complex quadratic field `k`. The Eisenstein period is an explicit Hecke formula of the shape

`theta_k E_s = C_k(s) zeta_k(s)/zeta(2s)`.

On the unitary line `s=1/2+it`, the denominator is `zeta(1+2it)`, which is nonzero for `t != 0`; the elementary factor is also controlled. Hence a vanishing Heegner Eisenstein period in the nonexceptional spectral range is genuinely an L-zero statement, not a formal use of the Euler product inside the critical strip. The continuation is supplied by Eisenstein/automorphic spectral theory.

For `lambda_w=w(1-w)>1/4`, an eigenvalue of a self-adjoint operator must be real. Writing `w=beta+i gamma`,

`Im(w(1-w)) = gamma(1-2 beta)`.

For a nonreal spectral parameter `gamma != 0`, reality therefore forces `beta=1/2`; then

`lambda_w = 1/4 + gamma^2 > 1/4`.

This is a genuine Hilbert-space localization mechanism: **if a nontrivial L-zero is admitted as a discrete eigenparameter, self-adjointness places it on the critical line automatically**. This is stronger in exactly the direction missing from the non-self-adjoint Lax–Phillips realization in `PL-033`.

## 2. The converse fails at the selector

The crucial point is that `theta E_w=0` is not the full eigenvalue criterion. Bombieri–Garrett derive the resolvent vector `u_(theta,w)` from

`(-Delta-lambda_w) u_(theta,w) = theta`

in the appropriate Sobolev/distributional sense. Their later spectral characterization identifies the designed discrete spectrum by an additional scalar boundary condition of the form

`theta u_(theta,w)=0`.

In the relevant half of the functional equation, this secular condition implies the Eisenstein-period vanishing needed for the L-zero relation; conversely, period vanishing alone does not make `w` an eigenparameter. Schematically, the proved implication is

`w in discrete spectrum(\widetilde S_theta)  =>  theta E_w=0  =>  L-data vanish`,

not

`L-data vanish  =>  w in discrete spectrum(\widetilde S_theta)`.

This asymmetry is the exact failure mode that matters for RH. A self-adjoint operator can safely localize any points that enter its spectrum while hypothetical off-line zeros can simply fail the domain/secular selector and remain invisible. Therefore the construction does not turn self-adjointness into a proof that **all** zeros lie on the axis.

The distinction also prevents a common conceptual shortcut. The Heegner period is not merely a rewriting of the bare prime-exponent lattice: it inserts global automorphic geometry and a distinguished distribution `theta`. The resulting boundary condition is additional global data. It can create a self-adjoint spectral problem, but that data simultaneously decides which zeros are visible.

## 3. The functional equation does not remove the selector for free

Bombieri–Garrett explicitly analyze a tempting but invalid symmetry argument. One might hope that the resolvent family were simply invariant under `w <-> 1-w`; combined with the zeta functional equation, such a symmetry would make the selector look automatically compatible with the full zero divisor.

The actual functional relation for `u_(theta,w)` contains an additional Eisenstein term. That extra term vanishes precisely when the period `theta E_w` vanishes. Consequently, using the simplified `w <-> 1-w` symmetry **before** proving the period condition is circular: the symmetry one wants is recovered only on the locus already selected by the L-zero condition.

This is a useful adversarial control for the wider prime-lattice program. A completed functional equation can center a spectral parameter at `1/2`, but it does not by itself prove that a target-relative domain or secular determinant sees every zero. Whenever a proposed self-adjointization relies on a reflection identity for a resolvent, model space, boundary condition, or period, the identity must be checked before imposing the zero condition rather than only on its zero locus.

## 4. Spacing gives a quantitative completeness obstruction

The designed pseudo-Laplacian selector has additional real-variable rigidity. On the critical spectral axis, Bombieri–Garrett express the relevant scalar resolvent pairing as a real meromorphic function with a partial-fraction structure of the form

`theta v_(theta,1/2+i tau) = sum_j |theta(f_j)|^2 / (t_j^2-tau^2)`.

Between adjacent poles this function is strictly monotone. The selected designed eigenparameters therefore interleave with the underlying pseudo-Laplacian secular spectrum and obey a lower-spacing bound. At height `T`, adjacent selected parameters satisfy asymptotically

`|w_(j+1)-w_j| >= (1-epsilon) pi/log T`

in the regime of their theorem.

This is incompatible with capturing every Riemann zero if the standard pair-correlation picture is imposed. Bombieri–Garrett derive the concrete consequence that, **assuming RH and Montgomery's pair-correlation conjecture**, no particular designed pseudo-Laplacian in their setup can have more than `94%` of the ordinary zeta zeros as eigenparameters. The numerical constant is therefore a conditional density obstruction, not an unconditional theorem about the zeta zero set.

The conditional result is still conceptually important. It shows that the missing converse is not a cosmetic gap expected to disappear by a routine strengthening of the same boundary construction. The selector imposes its own spacing geometry, whereas the expected zeta zero process has a positive density of pairs too close to fit that spectrum. Under the standard spectral-statistics model, the architecture is intrinsically incomplete.

## 5. Relation to the current prime-lattice frontier

`PL-033` and the present finding expose complementary one-sided operator realizations.

- In automorphic Lax–Phillips scattering, the full nontrivial zeta divisor is realized as the spectrum of a generator with multiplicities, but the generator is not supplied as a self-adjoint operator whose spectral theorem forces the axis.
- In designed pseudo-Laplacians, the operator is genuinely self-adjoint and therefore forces the critical axis for its nonreal spectral parameters, but only a selected subset of the relevant L-zero divisor is admitted as discrete spectrum.

Thus neither classical route gives the bidirectional Hilbert–Pólya statement

`rho is a zeta zero  <=>  rho corresponds to an eigenvalue of one self-adjoint operator`.

This also sharpens `PL-253`. Maaß–Selberg positivity already supplies a global positive continued spectral distribution containing the Weil zero functional, but the zero part is accompanied by a signed residual term. Designed pseudo-Laplacians make a different trade: the self-adjoint boundary problem removes the axis ambiguity, but at the price of **spectral selection**. In both cases, adding genuine global automorphic Hilbert-space structure does not automatically transfer its positivity/reality to the complete principal zeta divisor.

For the exponent-lattice mandate this is a falsification control, not a new lattice geometry. The prime-power axis skeleton and the frequencies `log p` feed the zeta/Eisenstein arithmetic data, but the decisive self-adjoint structure comes from the global automorphic quotient plus the boundary distribution. Therefore a new prime-lattice construction cannot claim progress merely because it embeds the divisor into a larger self-adjoint problem. It must show that the self-adjoint domain or determinant captures the **entire** rational-prime zeta divisor rather than a target-dependent sub-divisor.

## 6. Prior art and novelty audit

The primary source is:

- **Enrico Bombieri, Paul Garrett**, “Designed Pseudo-Laplacians,” arXiv:2002.07929 [math.NT] (2020), authors' current manuscript: https://www-users.cse.umn.edu/~garrett/m/v/Bombieri-Garrett_current_version.pdf. The introduction states the self-adjoint Friedrichs-extension construction and the necessary Dedekind-zeta-zero condition. The body derives the Heegner Eisenstein period, the resolvent/selector equations, the functional-equation correction term, interleaving/spacing results, and the conditional pair-correlation density bound; Corollary 69 gives the `94%` statement for ordinary zeta zeros under RH plus pair correlation.

Historical pseudo-Laplacian work predates this paper, including Yves Colin de Verdière's program relating self-adjoint pseudo-Laplacians to the Riemann zeros. Bombieri–Garrett's contribution used here is the designed boundary/distributional refinement and, crucially, the explicit audit of why its discrete spectrum need not exhaust the zero set.

A current-literature audit found later work continuing to treat this incompleteness as a motivation rather than a solved completeness theorem. That search is used only as a novelty check; the durable mathematical claims above rely on the Bombieri–Garrett theorem chain itself.

Internal duplication was checked against the current local frontier, especially `PL-033`, `PL-039`, `PL-043`, `PL-044`, `PL-252`, and `PL-253`. `PL-033` records the converse tradeoff (complete zero spectrum without self-adjointness). `PL-043` and `PL-044` audit de Branges/Sonine and localized Weil self-adjoint constructions but not this automorphic zero-selection theorem. `PL-252` and `PL-253` test positive automorphic quadratic/trace mechanisms rather than a Friedrichs spectral selector. The present result is therefore a distinct prior-art redirect.

## 7. Adversarial boundaries

1. **Not a no-go theorem for Hilbert–Pólya.** The obstruction concerns the Bombieri–Garrett designed pseudo-Laplacian architecture and the broader inference that a self-adjoint automorphic boundary restriction automatically captures the full zeta divisor. It does not rule out another self-adjoint operator with a different domain, relative trace, cohomological construction, Dirac-type structure, or other global coupling.
2. **The `94%` bound is conditional.** It assumes RH and Montgomery pair correlation. The unconditional theorem is the one-way zero-selection mechanism and the self-adjoint localization of admitted parameters.
3. **Dedekind zeta is not ordinary zeta.** For a complex quadratic field, `zeta_k(s)=zeta(s)L(s,chi_k)`. A vanishing period can therefore come from either factor. Statements about the ordinary Riemann-zeta subset require keeping this factorization explicit.
4. **Off-line zeros are not excluded.** A hypothetical off-critical zeta zero can simply fail the pseudo-Laplacian secular condition. Self-adjointness constrains the operator's eigenparameters; it does not constrain zeros that are absent from its spectrum.
5. **No formal Euler continuation is used.** The period and scattering expressions are continued by automorphic Eisenstein theory. Euler products are used only where convergent; the critical-strip conclusions use the meromorphically continued global objects.
6. **Selector completeness is the load-bearing issue.** Numerical coincidences between some eigenparameters and zeta zeros, or construction of more flexible boundary distributions, do not advance RH unless accompanied by a theorem that every principal zeta zero enters the same self-adjoint spectral problem.
7. **The prime lattice alone does not produce the Friedrichs domain.** Heegner distributions, the automorphic quotient, and Sobolev/Friedrichs extension theory are essential external global structure. The lattice dictionary is useful for locating arithmetic input but is not the source of the self-adjointness theorem.

## Research implication

The frontier should no longer be phrased as "take the automorphic zeta scattering system and impose a self-adjoint boundary condition." Classical designed pseudo-Laplacians already execute that move. They demonstrate the precise tradeoff: **self-adjointness can force the critical line only after a separate secular/domain condition has selected which L-zeros are spectral**.

Any surviving operator route must therefore prove a completeness theorem of a qualitatively stronger kind. For a candidate self-adjoint operator `H`, it is not enough to establish

`lambda in sigma_p(H)  =>  corresponding zeta/L datum vanishes`.

One needs the reverse implication for the principal zeta divisor, with multiplicities, or an equivalent trace/determinant identity whose zeros cannot be lost to boundary selection. In the present line this becomes a concrete audit question for every proposed global coupling: **what theorem prevents a hypothetical off-line Riemann zero from simply failing the domain/secular selector?** If there is no answer, the construction has reproduced the designed-pseudo-Laplacian gap rather than advanced beyond it.
