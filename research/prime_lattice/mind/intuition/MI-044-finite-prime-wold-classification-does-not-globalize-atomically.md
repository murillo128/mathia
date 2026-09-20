# MI-044 — Zero-faithful continuation is invisible to the standard quotient averages, and the critical-conductor one-sided Gram still becomes Haar

**Evidence level:** exact/literature-aware synthesis from PL-379--[PL-394](../../findings/PL-394-critical-conductor-functional-equation-shell.md), including [PL-391](../../findings/PL-391-finite-jessen-half-line-density-is-not-rh.md), [PL-392](../../findings/PL-392-euler-maclaurin-renormalization-besicovitch-null.md), and [PL-393](../../findings/PL-393-jessen-mean-forgets-euler-maclaurin-tail.md). No RH conclusion is claimed.

PL-392 gives the matched pair: `Q_N(s)=P_N(s)+N^(1-s)/(s-1)` converges locally uniformly to zeta on `Re(s)>0` away from the pole and is therefore fixed-zero faithful, while the Euler--Maclaurin tail is `B^2`-null on every fixed interior vertical line. The corrected representative and the raw Dirichlet polynomial are identical in the native mean-square quotient.

PL-393 shows that moving from quadratic mean to the standard nonlinear two-sided Jessen logarithmic mean does not repair this at fixed `N`. The height-decaying continuation tail tends locally uniformly to zero under large translations, so `Q_N` and `P_N` have the same hull limits and the same infinite-height logarithmic mean even though only `Q_N` is continuation-faithful.

PL-394 then tests the canonical coupled-height escape. For the frozen positive Dirichlet packet with `N asymp sqrt(T)`, the Montgomery--Vaughan estimate gives
`||G_{T,N}-I||=O(N/T)=O(T^(-1/2))`.
Thus growing the one-sided cutoff at the Riemann--Siegel conductor still leaves its full quadratic geometry asymptotically Haar. Coupling `N` to `T` is not by itself the missing continuation carrier.

The classical approximate functional equation shows what does change. On the critical line the continuation-faithful leading representation contains the positive packet, its reflected negative packet, and the archimedean factor `chi(1/2+it)=e^(-2i theta(t))`. Cross terms have phase derivative `2 theta'(t)-log(nm)` and become stationary near `nm=t/(2 pi)`, equivalently on a moving sum-energy shell `<v(n)+v(m),log p> approx log(t/(2 pi))`. This is a concrete representation-level distinction from the same-sign Haar Gram, but it is classical functional-equation geometry, not a zero-localization theorem.

The remaining route is therefore more specific than “use a coupled cutoff”: retain the distinguished continuation representative through a finite-height observable that keeps the opposite-mode/Gamma-phase cross channel (or another equally representative-sensitive mechanism) and is sensitive to individual zeros. Same-sign positive-cone quadratic data at the canonical conductor are already ruled out as that carrier.

**Boundary.** PL-394 uses the frozen-cutoff Gram estimate to restrict the one-sided route; the balanced approximate functional equation itself has a moving cutoff. It does not rule out every moving-cutoff nonlinear statistic, and the stationary sum-energy shell does not imply RH. The critical line enters through self-duality of the functional equation, not through an intrinsic localization theorem of the prime lattice.
