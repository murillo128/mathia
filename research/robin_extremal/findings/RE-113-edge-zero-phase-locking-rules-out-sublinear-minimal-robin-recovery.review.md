---
type: adversarial-review
target: research/robin_extremal/findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md
repo: murillo128/mathia
path: research/robin_extremal/findings/RE-113-edge-zero-phase-locking-rules-out-sublinear-minimal-robin-recovery.md
original_hash: 7f9c2f15e4e8898077e6ab03a5cd736d75021c59
reviewed_hash: 9260d6bb400dd3f5c054bd77a64e58ee74bc7852
status: resolved
overall_status: accept
---

# Adversarial review — RE-113

## Summary

Accepted after remediation. The finding correctly projects the finite-edge explicit formula onto the rightmost zero face, couples that phase field to the exact adaptive selector, and uses the one-sided recovery budget to show that genuinely sublinear recoveries are strictly larger than the scalar `RE-112` minimum.

## Resolved issues

The revised finding now states explicitly that conjugate edge zeros make `F_Theta` real-valued, gives the uniform remainder formulation needed to control every crossed event simultaneously, preserves the fixed-constant qualifier on all near-minimal conclusions, and distinguishes the classical almost-periodic prior-art boundary from the specific uniform edge-face expansion derived here.

## Verification

- Sign convention checked against the truncated formula `psi_0(x)-x=-sum x^rho/rho+...`.
- High-strip dominated convergence checked against the reciprocal-ordinate summability already proved in `RE-112`.
- Edge-tail passage checked using absolute convergence on the fixed high strip only; the finding does not assert absolute convergence of the full zero sum.
- Selector coupling checked against `RE-034`: `Z/Y->1`, `log Z-log Y->0`, and `Z-vartheta(Z)=(b+o(1))hZ log Z` give `F_Theta(log Y)=b hY^(1-Theta)log Y+o(1)`.
- Sublinear bootstrap checked: the scalar `RE-112` corridor forces `lambda_Y=o(1)`, phase locking makes the crossed forward defects uniformly `o(Y^Theta)`, and the `RE-110` budget upgrades the spacing to `omega(lambda_Y Y)`.
- Near-minimal corollary checked with one fixed constant `K`: any sequence with `lambda_Y->0` would become sublinear and contradict the upgraded spacing, so fixed-constant near-minimal recovery is necessarily macroscopic and edge-amplitude.
- Nonattained-edge corollary checked: `F_Theta=0` forces `lambda_Y->0`, excluding a fixed-constant near-minimal family.
- Prior-art audit checked against the Akbary--Ng--Shahabi almost-periodic/limiting-distribution framework; no collision was found with the CA-selected phase-lock and recovery conclusions.

No blocking issue remains.