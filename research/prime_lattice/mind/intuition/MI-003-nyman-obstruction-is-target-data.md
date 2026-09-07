# MI-003 — The Nyman obstruction is target data, but arbitrary-inner compression only reads it

**Evidence level:** proved structural separations and exact arbitrary-Blaschke programmability through PL-204; the residual discrete Nyman classification remains open

## Core intuition

The prime-exponent semigroup already has a serious RH-equivalent Hilbert-space realization in Nyman--Beurling theory. The difficult information is target-relative: whether the distinguished target lies in the closed span and which inner/model-space defect remains after common arithmetic factors are removed. Generator-only Gram geometry cannot see that defect.

PL-204 now closes the most canonical spectralization of the target defect. Compressing the exact prime multipliers to `K_B=H^2\ominus BH` makes each zero of `B` a joint eigencharacter of the adjoint prime tuple. This is faithful zero-sensitive data, but it is fully programmable: the same construction works for every admissible Blaschke divisor, including a one-point off-critical divisor. The model space therefore **reads a supplied zero divisor without constraining it**.

## Strongest justified principle

PL-017 identifies the prime dilation semigroup and its Mellin multipliers `n^(1/2-s)`. PL-019 locates the residual discrete completeness problem at Balazard's known frontier. PL-020 proves that multiplication by the off-line Blaschke factor is an inner isometry, leaving every generator Gram matrix unchanged while changing the target distance by a rigid model-space component.

PL-204 keeps that lost target information explicitly. If `B(rho)=0`, the Hardy kernel `k_rho` lies in `K_B` and satisfies `(C_p^B)^* k_rho = p^(1/2-conj(rho)) k_rho` for every prime. The joint tuple therefore recovers the point `rho`, but an elementary Blaschke factor at any freely chosen `rho_0` produces exactly the same semigroup law and its chosen eigencharacter. For the zeta specialization, `RH iff B_Z=1 iff K_(B_Z)={0}` is an exact restatement, not a selection mechanism.

## What remains fertile

A useful target-relative construction must add a **source-forced relation not functorially determined by an arbitrary inner function**: completed functional-equation structure, explicit-formula positivity, a canonical source/target coupling, a noncommuting relation, or another coercive boundary condition that fails on arbitrary-Blaschke controls.

The discrete Nyman span classification also remains open; PL-204 does not identify the greatest common inner divisor of the discrete generators or solve Balazard's problem.

## Epistemic status

**Exact target-information boundary and exact programmability control; arithmetic selector still missing.**

## Falsification criterion

Derive a critical-line restriction from the compressed prime semigroup using only properties shared by every `K_B`, or show that an arbitrary one-point Blaschke factor cannot realize the displayed joint eigencharacter. A positive escape must identify the additional zeta-specific relation and prove that arbitrary inner controls fail it.