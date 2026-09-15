# MI-032 — Reserve lifting converts the frozen essential obstruction into a finite negative-index problem

**Evidence level:** exact-derived operator redirect from [WI-307](../../findings/WI-307-exterior-reserve-lifting-removes-the-fixed-essential-obstruction.md), refining the frozen-reserve essential-band results WI-304--WI-306. The Weyl/finite-negative-index step is classical operator theory; the source-valid reserve construction is the line-specific content.

WI-304--WI-306 show that Liu's tail-dropped bounded comparison with high-frequency reserve frozen at `beta_0=1/16` develops an essential negative band as soon as the first prime channel is active. Same-width localizer optimization cannot remove it.

WI-307 shows that this obstruction is not invariant under admissible changes of the bounded comparison. On every fixed outer aperture `L`, the unit-window archimedean symbol tends to `+infinity` at high frequency. By moving the exterior Fourier cutoff far enough, one can therefore choose an arbitrarily large reserve `B` while preserving a valid lower comparison.

After localization the operator has the exact structure

`D_(chi,B) = B I - A_(L,chi) + K_(L,chi,B)`,

where `A_(L,chi)` is the finite sum of active compressed prime-power translations and `K` is compact. Since `||A_(L,chi)||<infinity` for fixed `L`, choosing `B>||A_(L,chi)||` makes the essential spectrum strictly positive. Any remaining negative spectrum is then finite and discrete; its negative part is finite-rank as an operator-theoretic correction.

This does **not** prove Weil positivity. The finite-rank negative part cannot simply be added to the lower bound: a successful argument must show that the omitted source-exact remainder dominates those discrete modes or otherwise controls them with legitimate arithmetic information. The gain is a change in obstruction type, not a positivity theorem.

The new frontier has two scales. At fixed aperture, the frozen essential obstruction can always be lifted away. Uniformly as `L->infinity`, however, the required reserve and Fourier cutoff can become expensive; the explicit construction already makes the cutoff grow exponentially in `B`. A robust impossibility theorem must therefore survive arbitrary admissible reserve choice, or prove that the reserve/cutoff cost grows incompatibly with the global architecture.

**Boundary.** WI-304--WI-306 remain exact for their frozen comparison. WI-307 only removes the stronger architecture-wide interpretation. It does not validate Liu's finite certificate, does not establish source-valid domination of the discrete negative sector, and does not prove the full Weil form positive.