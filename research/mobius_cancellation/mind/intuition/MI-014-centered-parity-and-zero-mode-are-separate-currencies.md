# MI-014 — Centered rough-parity control and the rough zero mode are separate fixed-power currencies

**Evidence level:** exact parity-deformation interpolation, rough zero-mode identity, current rough-sum literature, and Korobov--Vinogradov transfer through MC-187

## Core intuition

After unsigned rough support is controlled, the remaining Möbius difficulty does not collapse to one centered sign-fluctuation estimate. A centered phase-sensitive theorem can still miss a scalar zero mode whose size is fixed by a macroscopic rough Möbius increment.

The distinction is quantitative. The parity endpoint can be reached from centered positive deformations at only subpower interpolation cost, while the mean requires a genuine fixed power of global rough cancellation that current unconditional technology does not provide.

## Strongest justified principle

MC-185 introduces the rough parity polynomial and shows that its degree is `O(log X/log log X)`. Centered values on a stable positive interval therefore determine the centered Möbius endpoint with only `X^{o(1)}` loss. But orthogonality to constants gives an exact decomposition of the uncentered variance into centered variance plus `X|\overline P_X(-1)|^2`, and the latter is governed by `H(G_y(2X)-G_y(X))` up to the stated edge error.

To fit a target `X^{1+o(1)}H^{2-eta}`, the rough zero mode must satisfy a fixed-power bound `G_y(2X)-G_y(X) \ll X^{1-theta eta/2+o(1)}` in the active polynomial-window range.

MC-186 checks the current 2026 rough-sum expansion and obtains savings by every fixed logarithmic power at `y=c log X`, but the expansion order would need to grow on the order of `log X/log log X` to reach a fixed power, outside the theorem's uniformity. MC-187 then uses the exact inverse convolution `g_y=mu*s_y` to transfer the classical Korobov--Vinogradov-shaped Mertens bound to `G_y`; this is stronger than every fixed log power but still `X^{1-o(1)}`, not `X^{1-delta}`.

## Program consequence

Treat the centered signed parity field and its zero mode as separate proof obligations unless a new source identity couples them. A continuation should either obtain fixed-power global cancellation for the logarithmically rough Möbius sum, prove an uncentered local theorem that handles both pieces simultaneously, or derive a structural cancellation making the zero mode disappear from the target normalization.

Do not count stronger logarithmic savings as progress across the fixed-power boundary merely because they are numerically small at accessible scales.

## Counterevidence / boundary

The zero-mode lower requirement comes from the current variance target and polynomial window parametrization; another formulation could change the required exponent. MC-187 transfers the best classical Mertens cancellation available to the rough sum but does not prove that roughness can never support a stronger theorem. Centered parity interpolation also does not itself establish the centered variance estimate.

## Epistemic status

**Exact separation of centered parity transport from an independent fixed-power rough zero-mode obligation; current unconditional zero-mode bounds remain strictly subpower.**

## Falsification criterion

Show that the uncentered variance target follows from centered parity control without the stated rough-mean bound, invalidate the zero-mode identity, or derive a fixed-power estimate for `G_{c\log X}` from existing subpower inputs. A positive continuation should cross the zero-mode power boundary or couple it away structurally.
