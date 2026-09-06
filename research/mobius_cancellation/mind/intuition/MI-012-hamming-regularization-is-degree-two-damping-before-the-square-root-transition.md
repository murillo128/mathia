# MI-012 — Hamming endpoint cancellation survives only in signed cross-degree structure beyond fixed local filtering

**Evidence level:** exact source decomposition, proportional-shell asymptotics, and Chebyshev transfer obstruction through MC-113

## Core intuition

The Hamming deformation makes the Möbius endpoint a signed cross-degree resource. Positive shell bulk persists through every fixed proportional Sathe--Selberg scale, and the endpoint is obtained only after cancellation among those large degrees. Taking magnitudes before that cancellation loses the decisive information.

This failure is now complete for every **fixed finite local parity filter**, not merely first-order differences. MC-112 shows that any fixed transfer polynomial reappears with almost-square amplitude on some off-center proportional shell. MC-113 then quantifies the first growing-filter escape: uniformly suppressing a fixed proportional ratio band by a fixed power of `N` while retaining parity already costs `Theta(log N)` filter range at the ideal transfer level.

## Strongest justified principle

MC-107--MC-109 identify the positive shell cascade, its turning scale near `2 log log N`, and the failure of alternating truncation to isolate the small endpoint. MC-110 proves that every positive diagonal shell certificate with arbitrary Hölder weights is bounded below by an actual almost-square shell.

MC-111 tests local signed preprocessing. Its first-order central calculation left higher-order zeros at `z=1` formally open. MC-112 removes that boundary by moving away from the flat saddle: at `k~2 beta log log N`, fixed shifts satisfy `C_{k+j}/C_k -> beta^{-j}`, so a finite filter has asymptotic response `A(beta^{-1})`. A nonzero polynomial cannot vanish on the continuum of positive ratios, and one may choose a surviving ratio arbitrarily near the peak while `C_k=N^{2-o(1)}`. Absoluteizing after the filter therefore recreates the same endpoint loss for every fixed finite order.

MC-113 asks how much range an adaptive filter needs even before source-uniformity is addressed. The exact exterior Chebyshev problem with `P(-1)=1` gives minimax response `1/T_r(3)` on `[1/2,2]`. Hence `N^{-delta}` uniform attenuation requires `r=Theta(log N)` and `r=o(log N)` can buy only `N^{-o(1)}` suppression somewhere on the band.

The durable principle is therefore sharper: **finite local differencing cannot expose Möbius cancellation after absoluteization, and a growing local design must already pay logarithmic range before it can even hope for fixed-power uniform attenuation.**

## What remains possible

MC-113 does not prove that a logarithmic-range filter works on the true shell sequence. Growing-shift Sathe--Selberg uniformity, coefficient conditioning, and signed endpoint reconstruction remain independent arithmetic obligations. A source-specific recurrence could avoid uniform transfer suppression entirely by exploiting exact relations among the `C_{k,N}`.

Non-radial product-fiber or bilinear structure also remains open because it may preserve signs and prime couplings that one-dimensional Hamming degree forgets. Those routes should be judged by the exact signed relation they retain, not by the size of the representation.

## Status / novelty

Sathe--Selberg asymptotics, finite-difference transfer functions, and Chebyshev minimax are classical mechanisms. The persisted Mathia synthesis is the source-specific boundary: **all fixed local radial filters are closed after absoluteization, and sublogarithmic growing filters cannot uniformly buy a polynomial gain even at the ideal transfer level.** No Mertens or RH estimate follows.

## Falsification criterion

Exhibit a fixed nonzero parity-preserving filter whose response is `o(C_{k,N})` on every proportional shell; invalidate the exact transfer limit in MC-112; or produce a parity-normalized degree-`r` polynomial with sup norm on `[1/2,2]` below `1/T_r(3)`. Any such result would reopen the corresponding boundary.