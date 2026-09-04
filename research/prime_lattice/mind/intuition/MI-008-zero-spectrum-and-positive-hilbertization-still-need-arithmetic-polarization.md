# MI-008 — Native positivity and outward positive transport do not supply the completed arithmetic polarization

**Evidence level:** supported by exact literature-backed spectral, RKHS, screw, explicit-formula, and Volterra constructions through PL-145

## Core intuition

Prime-exponent geometry carries several genuine positive structures, but they lie on different sides of the completion boundary. Native Euler/Bohr positivity is unconditional and broadly universal. Completed screw/CND/Lévy positivity is zero-sensitive but already RH-equivalent. The newest deformation result adds a directional gate: the natural positive shift semigroup transports the completed datum **outward toward easier zero-free half-planes**, while the inverse direction needed for RH is not positivity preserving.

Thus neither another native positive avatar nor generic positive interpolation can supply the missing theorem. The live object remains an arithmetic sign/polarization that controls inward return to the critical boundary for the special completed zeta datum.

## Strongest justified principle

PL-142--PL-143 classify the native HLS kernel: complete Pick fails on a finite two-prime face, while every positive kernel power remains positive and `log K` is a generic prime-power compound-Poisson carrier. This does not cross the Euler-product boundary.

PL-144 identifies the completed side. Suzuki screw positivity, Schoenberg negative type, and Nakamura--Suzuki Lévy/infinite-divisibility formulations collapse to the same zero-sensitive architecture; for the actual completed zeta function the scalar sign `Psi(t)>=0` is already equivalent to RH.

PL-145 then exposes the exact shift geometry. Suzuki's family satisfies a Volterra semigroup law `T_eta T_delta=T_{eta+delta}`. For `eta>0`, `T_eta` preserves nonnegativity and damps high prime-axis energy while moving the zero-free boundary outward. But `T_{-eta}` is not order preserving; even `T_{-eta}1=1-eta t` changes sign. Starting from the unconditional positive endpoint `omega=1/2`, the direction required to reach `omega=0` is precisely this non-positive inverse.

## What remains possible

A useful route must derive a zeta-specific inward estimate, completed arithmetic polarization, or coupling between finite prime-power and archimedean terms that controls `T_{-eta}` on the special trajectory. A generic semigroup/order argument cannot do it. Mixed exponent geometry matters only if it forces that completed sign rather than decorating an already RH-equivalent object.

## Status / novelty

All ambient kernel, screw, Schoenberg, and Volterra ingredients are prior art or exact persisted consequences. The synthesis is the directional completion gate: **known positivity flows toward safer half-planes; RH requires source-specific control in the opposite direction**.

## Falsification criterion

Derive `Psi_0>=0` from the unconditional shifted positive endpoint using a source-forced estimate that is not itself an RH-equivalent assumption, or exhibit a native HLS positivity transition that survives the generic controls and genuinely constrains the completed divisor.

## Lean-formalizable core

- Native complete-Pick obstruction and kernel-power positivity.
- Screw/CND sign reduction.
- Volterra semigroup composition.
- Forward cone preservation and explicit failure of inverse positivity.
