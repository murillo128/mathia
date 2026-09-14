---
type: adversarial-review
target: research/robin_extremal/findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md
repo: murillo128/mathia
path: research/robin_extremal/findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md
original_hash: 01be17a52f0b99c282bb89789e19915db3f56988
status: resolved
overall_status: accept
---

# Adversarial review — RE-113

## Summary

Accepted. The final rebased draft preserves the previously reviewed mechanism while tightening notation and proof structure. The finite-edge explicit formula is projected onto the actual rightmost zero face using only the reciprocal-ordinate summability already established in `RE-112`; the adaptive selector then fixes that edge phase, and the `RE-110` one-sided workload budget turns phase vanishing into strict anti-saturation of every sublinear recovery.

## Verification

- Sign convention: `psi_0(x)-x=-sum x^rho/rho+...` gives the positive edge series for `x-psi_0(x)` used in the finding.
- Dominated convergence: on `Re rho>=sigma_0`, `|x^(rho-Theta)/rho|<=1/|rho|`, and `RE-112` supplies a summable majorant. The edge tail is uniformly negligible by the same absolute convergence.
- No overclaim of absolute convergence: only the fixed high strip is summed absolutely; lower-strip zeros stay inside the truncated explicit formula estimate.
- Reality and regularity: conjugate edge zeros pair, so `F_Theta` is real-valued; uniform absolute convergence gives boundedness and uniform continuity.
- Selector coupling: `RE-034` gives `Z/Y->1`, `log Z-log Y->0`, and `Z-vartheta(Z)=(b+o(1))hZ log Z`, which yields `F_Theta(log Y)=b hY^(1-Theta)log Y+o(1)`.
- Sublinear bootstrap: the scalar `RE-112` lower bound forces `lambda_Y=o(1)` when `L=o(Y)`; uniform phase control on the crossed interval gives `M_+=o(Y^Theta)`; `RE-110` then upgrades `L=Omega(lambda_Y Y)` to `L=omega(lambda_Y Y)`.
- Near-minimal qualifier: the macroscopic conclusion uses one fixed upper-bound constant `K`; this is stated explicitly. With that qualifier, `lambda_Y` cannot tend to zero, so `h(C) asy Y^(Theta-1)/log Y`, `L asy Y`, and the selected edge phase stays positive of order one.
- Nonattained edge: `F_Theta=0` forces `lambda_Y->0`, excluding any unbounded fixed-constant near-minimal family.
- Prior-art boundary: classical almost-periodic/limiting-distribution work is treated as conceptual prior art only. The line-specific claim is the CA-selector phase lock plus recovery consequence; no collision was found in the audit.

No blocking or material issue remains.