# MI-021 — Support-matched high moments reduce to a radial signed source-walk theorem

**Evidence level:** the amplification threshold and tensor/Krawtchouk representation are exact through [MC-264](../../findings/MC-264-support-matched-high-moment-blind-threshold.md); [MC-265](../../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md) rules out first-order balance plus termwise absolute values; [MC-266](../../findings/MC-266-tensor-pair-krawtchouk-radial-source-walk-collapse.md) exactly collapses the weighted pair geometry to a radial `2m`-step Boolean-cube source walk. The required signed support-resolved estimate remains open.

The surviving blind relation lives on a shell-prime subset of size `t`. At the first admissible support `t~(1/log 2)log log y`, low moments cannot isolate one exceptional subset from the fixed-weight family. MC-264 shows that one extra tensor power is enough: at `m=t+1`, the normalized diagonal cost is of order

`2^(t+1) sqrt(t)/k_y`,

which tends rapidly to zero. Thus a near-diagonal `2(t+1)`-th moment estimate has ample room to exclude every blind subset.

MC-265 identifies why generic shell balance is not that estimate. Even at exact Hamming balance, the even Krawtchouk kernel is still parametrically too large for pairwise triangle-inequality control. The needed gain has to occur before absolute values are taken.

MC-266 then removes the pair indices themselves. If `a_y=sum_p delta_(e_p)` on the lower-prime Boolean cube and `c_m=a_y^(*m)`, exponent two gives the exact autocorrelation identity

`sum_u c_m(u)c_m(uq)=c_(2m)(q)`.

Therefore

`S_(2m,y)(t)=sum_q c_(2m,y)(q) K_t(d_y(q);N_y)`.

The coefficient `c_(2m,y)(q)` is radial in `s=omega(q)`. Writing

`H_(s,y)(t)=sum_(omega(q)=s) K_t(d_y(q);N_y)`

and

`C_(2m,k)(s)=(2m)! [z^(2m)] (sinh z)^s (cosh z)^(k-s)`,

the whole target becomes

`S_(2m,y)(t)=sum_(s even, 0<=s<=2m) C_(2m,k_y)(s) H_(s,y)(t)`.

The diagonal is `s=0`. Every nontrivial collision-depth layer can have raw positive coefficient mass of higher polynomial degree in `k_y` than the diagonal, so radial reduction is not a small-error argument. Its value is structural: **the missing theorem is a finite hierarchy of signed arithmetic shell sums over products of exactly `s` lower primes, not an arbitrary weighted two-source distance distribution.**

At the live `m=t+1~log log y`, one can therefore attack the support layers directly, derive recurrences that couple neighboring even `s`, or estimate the exact radial mixture without absoluteizing each layer. If available character-sum technology only controls `H_s` at the scale of its raw layer mass, the route still fails; if arithmetic produces signed cancellation across the hierarchy, this is the direct route back to the MC-264 threshold.

**Boundary.** Radiality is source-side only: the Legendre-signature distance `d_y(q)` need not depend only on `omega(q)`. MC-266 proves no new moment estimate and excludes no blind relation. It changes the primitive analytic object that must be controlled.
