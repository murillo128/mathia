# MI-032 — Reserve lifting plus the clipped source tail converts the essential obstruction into a gapped finite-sector problem

**Evidence level:** exact-derived operator redirect from [WI-307](../../findings/WI-307-exterior-reserve-lifting-removes-the-fixed-essential-obstruction.md), strengthened by the source-exact clipped-tail decomposition [WI-308](../../findings/WI-308-clipped-source-tail-gives-a-coercive-fredholm-witness.md), refining the frozen-reserve essential-band results WI-304--WI-306. The Weyl/finite-negative-index and Fourier-multiplier steps are classical operator theory; the source-valid reserve/tail construction is the line-specific content.

WI-304--WI-306 show that Liu's tail-dropped bounded comparison with high-frequency reserve frozen at `beta_0=1/16` develops an essential negative band as soon as the first prime channel is active. Same-width localizer optimization cannot remove it.

WI-307 shows that this obstruction is not invariant under admissible changes of the bounded comparison. On every fixed outer aperture `L`, the unit-window archimedean symbol tends to `+infinity` at high frequency. By moving the exterior Fourier cutoff far enough, one can choose an arbitrarily large reserve `B` while preserving a valid lower comparison. After localization,

`D_(L,chi,B) = B I - A_(L,chi) + K_(L,chi,B)`,

with `A_(L,chi)` the finite active prime-power translation sum and `K` compact. Choosing `B>||A_(L,chi)||` makes the essential spectrum strictly positive, so any remaining negative spectrum is finite and discrete.

WI-308 keeps the source material discarded by that comparison instead of replacing it with an arbitrary finite-rank correction. Clip the exact unit-window source symbol `sigma_1` at `B` and write its omitted positive tail as `q_B=(sigma_1-B)_+`. Sliding localization turns this tail into the exact Fourier multiplier

`r_(chi,B)(xi) = (1/(2 pi)) int q_B(t)|F_chi(t-xi)|^2 dt`.

Because `q_B` is positive on both remote frequency tails and `F_chi` is entire/nonzero, `r_(chi,B)(xi)>0` at every finite `xi`; continuity and `r_(chi,B)(xi)->infinity` as `|xi|->infinity` give

`c_(chi,B):=inf_xi r_(chi,B)(xi) > 0`.

Thus the full Weil form has the exact decomposition

`Q = D_(L,chi,B) + T_(chi,B)`,  with  `T_(chi,B) >= c_(chi,B) I`.

At fixed aperture, the source-valid positivity question is therefore the concrete finite-sector inequality

`lambda_min(D_(L,chi,B)) >= -c_(chi,B)`.

Under a first RH-failure crossing, the zero mode instead forces `lambda_min(D)<=-c<0`, so the crossing becomes a **gapped Fredholm witness** rather than a zero-margin mode. The source bill has not vanished; it has been priced by an explicit positive tail reserve.

The remaining frontier is quantitative and global. `c_(chi,B)` must be made effective and compared with the finite negative spectrum while `L` grows, with the reserve/Fourier-cutoff cost tracked jointly. A robust impossibility theorem must survive every admissible reserve/tail choice; a construction must prove that the source-exact tail budget dominates the discrete modes uniformly enough for the global limit.

**Boundary.** WI-308 is a fixed-aperture reduction, not a proof of Weil positivity. It does not establish `lambda_min(D)>=-c`, does not validate Liu's finite certificate, and does not make an arbitrary finite-rank repair source-valid. WI-304--WI-306 remain exact for their frozen comparison; WI-307--WI-308 change the architecture-wide interpretation.