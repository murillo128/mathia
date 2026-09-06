# MI-012 — Hamming endpoint cancellation is a signed cross-degree resource, not shell magnitude

**Evidence level:** exact source decomposition plus classical Landau--Selberg--Delange/Sathe--Selberg input through MC-111

## Core intuition

The Hamming deformation now exposes the endpoint obstruction across the entire natural shell scale. The shell coefficients remain positive through fixed proportional degree and across the turning window near `2 log log N`; direct truncations retain a boundary-sized remainder rather than the tiny Möbius endpoint. Taking norms of the shell magnitudes loses exactly the cross-degree signs that produce the endpoint.

The first signed local repairs do not solve this. A fixed finite filter that preserves parity but only cancels the locally flat shell profile to first order still leaves almost-square filtered coefficients, so taking absolute values after that filter merely relocates the same loss. The surviving radial resource must retain **higher-order or genuinely nonlocal signed interaction between many degrees before absoluteization**.

## Strongest justified principle

MC-107 extends the positive shell cascade to every fixed proportional Sathe--Selberg scale and identifies its peak near `k=2 log log N`. MC-109 shows that even in the critical turning regime an alternating prefix is asymptotically a fixed fraction of its boundary shell, with the omitted tail forced to cancel it. The endpoint is therefore not localized by stopping near the peak.

MC-110 proves a stronger information-loss statement. Every positive diagonal `L^p`/Hölder certificate, with arbitrary shell weights, is bounded below by the actual central shell and therefore remains `N^{2-o(1)}`. Parseval and the shell square function display the same almost-square energy. The missing resource is not a better radial weight; it is cancellation between different degrees before magnitudes are taken.

MC-111 tests the first non-diagonal escape. For a fixed finite filter `A`, `A(-1)` is exactly its parity transfer and `A(1)` its response to a locally flat positive shell profile. If `A(1) != 0`, the central bulk survives directly. If `A(1)=0` but `A'(1) != 0`, the filtered central coefficients are still of order `N^2/log log N`, and their absolute variation remains almost square. Thus adjacent even/odd pairing and every fixed first-order local difference fail as endpoint certificates once their outputs are absoluteized.

## What remains possible

A fixed filter with a zero of order at least two at `z=1` and `A(-1) != 0` is not yet classified. Neither are filters whose order/range grows with `N`, signed recurrences that control the filtered sequence without absoluteization, or non-radial/product-fiber relations that never collapse to Hamming degree.

These are materially different possibilities. A higher-order zero may simply take more derivatives of the same smooth central profile and still leave an almost-square floor; that must be proved rather than assumed. A genuinely nonlocal relation could instead couple enough of the critical shell profile to transport parity directly.

## Status / novelty

The analytic asymptotics and finite-difference background are classical; the persisted Mathia contribution is the source-specific sequence of no-go boundaries. The durable synthesis is now: **Möbius endpoint information is stored in signed cross-degree coherence across the critical shell profile, and neither direct truncation, positive diagonal shell norms, nor first-order fixed local filtering preserves enough of that resource after absoluteization.** No improved Mertens estimate or RH consequence is claimed.

## Falsification criterion

Produce a valid direct cutoff in the proportional/critical shell regime whose retained prefix is already at the Möbius endpoint scale; construct a positive diagonal shell certificate with fixed polynomial saving despite MC-110; or exhibit a fixed parity-preserving first-order local filter whose absoluteized reconstruction beats the MC-111 floor. Otherwise the next radial mechanism must be higher-order/growing/nonlocal and must keep signed cross-degree cancellation visible.
