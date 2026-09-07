# MI-012 — Radial parity filters fail at the finite-support boundary before they reach the needed transfer range

**Evidence level:** exact transfer-range and finite-support obstruction through MC-114

## Core intuition

The Hamming/radial branch is now closed more sharply than “fixed local filters are too weak.” MC-113 shows that polynomial attenuation of a proportional transfer band requires filter range `Theta(log N)`. MC-114 compares that requirement with the actual source: the physical Hamming degree is only `O(log N/log log N)`. A one-sided filter strong enough to suppress the unwanted band therefore extends beyond the entire radial source.

Once this happens, small filtered coefficients cease to diagnose Möbius cancellation. They can be produced universally by zero extension because the filter is spending most of its mass where no physical shell exists. The signed endpoint has merely been displaced into boundary terms that the physical readout omitted.

## Strongest justified principle

MC-112 rules out every fixed finite transfer polynomial after absoluteization, and MC-113 quantifies the minimum growing range needed for uniform fixed-power attenuation. MC-114 then writes the parity-filter operation as an exact Laurent identity. If parity is to remain exact, negative-index boundary terms must accompany the shifted physical coefficients. Dropping those terms and retaining only nonnegative physical shells converts source truncation into apparent cancellation.

The binomial high-pass control makes the failure explicit: with normalized `ell^1` mass, the physical outputs can be made uniformly tiny for arbitrary source data once the filter range greatly exceeds the shell degree. A monomial source exhibits the same effect without any arithmetic cancellation. Thus **one-sided radial attenuation beyond the physical support is a boundary artifact unless the displaced signed source term is controlled.**

## Counterevidence / boundary

MC-114 does not rule out a source-justified two-sided extension, a signed identity that relates the negative-index boundary to physical Möbius data, or a genuinely nonlocal/nonradial carrier. It also does not rule out a different transform whose useful range remains inside the physical degree budget.

What is closed is the strategy of interpreting small physical coefficients from a long one-sided radial filter as endpoint cancellation without accounting for the boundary it has moved outside the source.

## Epistemic status

**Proved route boundary.** The algebraic finite-support mechanism is exact and independent of RH.

## Falsification criterion

Construct a parity-normalized one-sided filter with polynomial attenuation on the declared proportional transfer band whose effective range stays within the `O(log N/log log N)` physical shell degree, or derive an exact arithmetic theorem that reconstructs the omitted negative-index boundary from the physical source with the required signed control. Either would reopen a radial route.