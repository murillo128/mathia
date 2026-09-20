# Möbius-cancellation research lines

This file records the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a task queue or history.

## Retain arithmetic structure that survives exact quotient changes without Abel-collapsing back to the same Möbius convolution

**Linked intuition:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`.

MC-397--MC-404 progressively consume source-mode averaging, divisor-pair multiplicity, lcm phase, moving endpoints, complete endpoints, generic truncation and finally every finite divisor-incidence enrichment. Formal family size and finite incidence nonlinearity are not independent cancellation resources once the downstream arithmetic has collapsed them to signature or lcm data.

MC-405 leaves the lcm semilattice by retaining the prime-power label in `M(floor(x/b))`, but the complete Mangoldt-weighted family is an exact first-order self-coupling of `M`. MC-406 then identifies the actual quotient seen downstream: only the `O(sqrt(x))` floor-quotient masses survive, and their PNT main kernel is exactly classical harmonic Möbius cancellation.

MC-407 closes the apparent remaining “Mertens values versus prime-error increments” escape in that representation. If `psi(y)=y+E(y)`, the increment remainder

`R(x)=sum_k M(k)(E(x/k)-E(x/(k+1)))`

Abel-collapses exactly to

`sum_(a<=x) mu(a) E(x/a) + x M(x)/(x+1)`.

Together with the main term, the full quotient identity is just another coordinate presentation of the finite Möbius--PNT-error convolution equivalent to `-sum_(n<=x) mu(n) log n`. A pointwise power bound on `E` gives only linear scale after absolute summation, so the increment coordinates themselves do not create a new contraction.

The live route is now sharper. Either prove a genuinely new **signed correlation theorem** for `sum mu(a)E(x/a)` whose proof does not already contain the desired Mertens estimate, or retain information inside the floor-quotient fibers that is lost before Abel summation—phase, congruence, translation or another source coordinate with an independently controllable destination. Merely switching between quotient increments, Abel sums and convolution coordinates is not new information.

## Keep retained variables, quotient dimension, coordinate changes and independent cancellation theorems distinct

A variable can survive one quotient and still be analytically redundant. Divisor tuples collapse to lcm; source labels collapse to floor-quotient masses; deterministic PNT mass collapses to harmonic Möbius cancellation; and MC-407 shows that the residual increment pairing collapses under Abel summation to the same Möbius-weighted error convolution.

Future candidates should therefore be reduced through all exact regroupings and summation-by-parts identities before being credited with a second observable. Genuine progress requires a signed estimate not algebraically equivalent to the target estimate, or a finer retained variable that survives the final quotient where the current Abel collapse no longer applies.