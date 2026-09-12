# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Control the arithmetic dependence of low-order primary blind codes, or cancel the exact rough Möbius coset

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`.

MC-238--MC-246 reduce the complete blind source to one rough Möbius coset and identify the quotient `Q=G/H`. MC-247--MC-250 couple witness support, prime-power torsion order, order-compatible shell occupancy and primary multiplicity. At level `ell^a`, the blind shadow is an `F_ell` code with dimension `m_(ell,a)` and minimum distance at least `D_y`.

MC-251 applies q-ary Hamming sphere packing to that exact level code. With `t_y=floor((D_y-1)/2)`,

`n_d-m_(ell,a) >= log_ell V_ell(n_d,t_y)`,

which strengthens Singleton by a growing logarithmic factor when the compatible shell is wide. Unconditionally the fixed-order generic rank deficit is `Omega(log y log log y)` at the Brun--Titchmarsh shell scale; under the ERH support floor it is `Omega(sqrt(y))`.

The gain is still sublinear relative to a fixed-order compatible shell of size `Theta(y/log y)`. Generic coding theory therefore does not close the low-order quotient even after family-size packing. The next theorem must use arithmetic structure of the residue-symbol matrix beyond minimum support—simultaneous dependencies, generalized weights/distance profiles, reciprocity/Kummer structure, or a comparable constraint—or bypass generation by proving fixed-power signed cancellation for the exact rough Möbius coset / complete-annihilator aggregate.

## Keep support, torsion order, shell occupancy, code-family deficit, quotient index and signed amplitude separate

MC-251 substantially strengthens the low-order multiplicity squeeze but does not make the blind quotient small in the sense needed downstream. A large code of dimension `n_d-o(n_d)` remains possible. Future work should not treat another generic coding inequality as likely to finish the problem unless it uses genuinely arithmetic structure or produces a linear-size deficit.