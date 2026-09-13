# MI-021 — Support-matched high moments cross the blind threshold, but first-order shell balance is still too weak

**Evidence level:** the moment threshold, tensor coefficient mass and Krawtchouk identity are exact through [MC-264](../../findings/MC-264-support-matched-high-moment-blind-threshold.md). [MC-265](../../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md) proves that even perfect first-order shell balance is parametrically insufficient for a pointwise-absolute-value proof of the candidate high-moment estimate. The required signed fixed-weight high-moment theorem remains open.

The surviving quadratic blind relation lives on a shell-prime subset `T` of size `t`. Low moments cannot see one exceptional subset against the whole fixed-weight family at the first admissible support scale `t~(1/log 2) log log y`. MC-264 identifies exactly where moment amplification becomes strong enough.

After raising the shell character sum to tensor order `m` and reducing products modulo squares, the coefficient vector has quadratic mass

`D_(m,y) ~ (2m-1)!! k_y^m`

uniformly for `m=O(log log y)`. At `m=t`, the natural diagonal still sits above one blind atom. At **one extra tensor power**, `m=t+1`, the normalized diagonal cost drops to order

`2^(t+1) sqrt(t)/k_y`,

which tends rapidly to zero at the first unresolved support. Thus the family-size obstruction is genuinely a low-moment obstruction: a support-matched `2(t+1)`-th moment estimate near diagonal scale would have ample room to exclude every blind subset.

The exact arithmetic kernel is the fixed-weight Krawtchouk transform

`S_(2m,y)(t) = sum_(u,v) c_m(u)c_m(v) K_t(d_y(u,v);N_y)`.

MC-265 now closes the tempting shortcut “prove every product character is nearly balanced, then bound the off-diagonal terms separately.” At perfect Hamming balance `d=floor(N/2)`, the even layer already satisfies

`|K_t(d;N)|/binom(N,t) ~ (t/(eN))^(t/2)`

for even `t`, up to the explicit constant-scale asymptotic. At the live support this is larger than the pointwise scale required by the diagonal target by

`(k_y/t)^(t/2+o(t))`.

So even ideal first-order sign balance leaves a universal without-replacement parity correlation far too large for triangle-inequality control.

This does **not** lower-bound the actual arithmetic moment. The off-diagonal Krawtchouk terms are signed and may cancel. That cancellation is now the mathematical content of the open route. A successful theorem must control the weighted signed distance distribution as a whole, force the relevant weighted mass close enough to Krawtchouk zeros, or estimate the sparse shell moment directly without absoluteizing pairwise terms.

**Research consequence.** Keep the favorable `m=t+1` amplification, but stop asking for generic pairwise shell balance as the missing input. The required source theorem is an association-scheme/Fourier cancellation statement at order `t`, not a first-moment pseudorandomness estimate.

**Boundary.** MC-264--MC-265 neither prove the candidate moment inequality nor exclude a blind relation. They identify a sufficient amplification scale and rule out one broad proof class for reaching it.
