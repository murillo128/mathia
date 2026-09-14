---
type: adversarial-review
target: research/robin_extremal/findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md
repo: murillo128/mathia
path: research/robin_extremal/findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md
original_hash: 7f9c2f15e4e8898077e6ab03a5cd736d75021c59
status: open
overall_status: concerns
---

# Adversarial review — RE-113

## Summary

The main mechanism is sound: the reciprocal-ordinate summability already established in `RE-112` permits an extreme-face decomposition of the normalized explicit formula, and coupling that profile to the exact `RE-034` selector gives a genuine new restriction on sublinear recovery. The recovery conclusion follows from `RE-110` once the event-phase estimate is uniform over the crossed interval.

The draft should be tightened in four places before acceptance. None changes the main claim.

## Issues

### 1. `F_Theta` should be explicitly real-valued

**Severity:** minor.

The displayed series is complex term-by-term, while later inequalities use its sign. State explicitly that conjugate zeros are both included and hence the absolutely convergent series pairs to a real-valued function on real `u`.

**Remediation:** add the conjugate-pair observation immediately after the definition.

### 2. Uniformity over all crossed events needs to be stated rather than inferred

**Severity:** moderate.

Equation (20) uses one `o(Y^Theta)` bound simultaneously over every crossed event. The global asymptotic in (8) is enough, but the draft should make the quantifiers explicit: write the remainder as `r(x)x^Theta` with `sup_(x>=X)|r(x)| -> 0`, first use boundedness of `F_Theta` and `u_e=Y+o(Y)` to deduce `eta_e asymp Y`, then use uniform continuity of `F_Theta` on the shrinking logarithmic interval.

**Remediation:** add this argument in Section 4 before concluding `M_+=o(Y^Theta)`.

### 3. The near-minimal conclusion needs fixed constants emphasized

**Severity:** minor.

The contradiction in Section 5 is valid only for a family with one fixed constant `K` in the near-minimal upper bound; if `K` were allowed to diverge, `lambda_Y -> 0` would not force `L=o(Y)`. The draft says “one fixed K” but the headline conclusion should preserve this qualifier.

**Remediation:** add “fixed-constant” to the summary statement and final frontier wording wherever near-minimality is invoked.

### 4. Prior-art boundary should distinguish classical almost periodicity from the stronger uniform edge-face expansion

**Severity:** minor.

Akbary--Ng--Shahabi work in a broad Besicovitch almost-periodic/limiting-distribution framework. The draft should not suggest that their theorem is the exact uniform expansion proved here under a finite attained zero edge. Conversely, the edge-phase representation itself is a straightforward explicit-formula consequence once high-strip reciprocal summability is available and should not be advertised as a novel general theorem.

**Remediation:** state that the cited almost-periodic literature is a conceptual prior-art boundary, while the displayed uniform extreme-face expansion is derived here from the specific `RE-112` summability input.

## Tests and reasoning

- Checked the sign convention against `psi_0(x)-x=-sum x^rho/rho+...`; therefore `x-psi_0(x)` has the positive edge series used in the draft.
- Checked dominated convergence: for `Re rho>=sigma_0`, `|x^(rho-Theta)/rho|<=1/|rho|`, and `RE-112` supplies summability of these coefficients.
- Checked edge-tail truncation: absolute convergence makes the omitted `|gamma|>x` edge tail uniformly `o(1)`.
- Checked the selector scale: `RE-034` gives `Z/Y->1` and `log Z-log Y->0`, so uniform continuity transfers the phase from `Z` to `Y`.
- Checked the sublinear bootstrap: `L=o(Y)` plus the scalar `RE-112` lower bound forces `lambda_Y=o(1)`; phase locking then makes every crossed positive forward defect `o(Y^Theta)`, and `RE-110` upgrades the corridor from `Omega(lambda_Y Y)` to `omega(lambda_Y Y)`.
- Checked the nonattained-edge corollary: `F_Theta=0` gives `lambda_Y->0`; a fixed-constant near-minimal upper bound would then make `L=o(Y)`, contradicting the upgraded corridor.

No arithmetic counterexample or prior-art collision was found. Accept after the four clarifications above.