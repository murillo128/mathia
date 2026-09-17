# VIS-262 — Rodgers' diagonal reduction freezes every fixed-order BK–GUE source moment

## Claim

Use the fixed-margin smooth pair-correlation setting of `VIS-260` and the physical-moment dictionary of `VIS-261`. Fix a real even weight `omega` whose Fourier transform is smooth and compactly supported. Let

`D_T(u)=omega(u)[T^(-1) integral_0^T (Q_t(u)-K_t(u)) dt]`

be the weighted Bogomolny--Keating-minus-naive-GUE physical-space kernel, and for every fixed integer `m>=0` define

`M_(2m)(T)=integral_R u^(2m) D_T(u) du`.

Rodgers' final comparison in the proof of Theorem 1.4 introduces `tilde Q_t` and proves, for the allowed smooth band-limited test class, that the weighted transform of `Q_t-tilde Q_t` is `O_delta(T^(-delta))` inside every fixed support margin. At frequency `alpha=0`, multiplication of the test weight by `u^(2m)` preserves the same class because

`widehat{u^(2m) omega}`

is a constant multiple of the `2m`-th derivative of `widehat{omega}` and therefore remains smooth and compactly supported.

Moreover Rodgers obtains the exact `t`-independent difference

`F(u)=tilde Q_t(u)-K_t(u)`

`    =(1/(2 pi^2))[Re((zeta'/zeta)'(1+iu)-B(iu))+1/u^2]`,

with the singularity at `u=0` understood by the same continuous cancellation used in the paper. Hence for every fixed `m` and every fixed `delta<1/2`,

`M_(2m)(T)=C_(2m)(omega)+O_(omega,m,delta)(T^(-delta))`,

where

`C_(2m)(omega)=integral_R u^(2m) omega(u) F(u) du`.

Equivalently, with the frequency residual `R_T(alpha)` of `VIS-261`,

`R_T^(2m)(0)`
` =(-1)^m (log T)^(2m) C_(2m)(omega)`
`  +O_(omega,m,delta)(T^(-delta)(log T)^(2m))`.

All odd derivatives still vanish for even `omega`.

The quadratic channel is not universally zero over Rodgers' admissible fixed-weight class. Rodgers explicitly notes that `F` is not identically zero. Since `F` is real and even, choose `u_0!=0` with `F(u_0)!=0`. There exists a real even nonnegative Schwartz approximate identity `phi_a` with smooth compactly supported Fourier transform; for example start from a band-limited Schwartz function `g`, set `phi=|g|^2/integral |g|^2`, and scale `phi_a(u)=a phi(au)`. Then

`omega_(a,u_0)(u)=(phi_a(u-u_0)+phi_a(u+u_0))/2`

is admissible, real and even, and

`C_2(omega_(a,u_0)) -> u_0^2 F(u_0)`

as `a->infinity`. Therefore `C_2(omega)!=0` for at least one fixed admissible weight chosen entirely from the explicit prediction, before any confirmation-zero data are inspected.

For such a fixed weight, take the sharp symmetric quadratic packet of `VIS-257`, supported on `[-b,b]`, with zero mass, exact `|alpha|` cancellation, `m_2=1`, and total variation `8b^(-2)`. Combining `VIS-261` with the same Rodgers reduction applied to `u^4 omega` gives, throughout a fixed support margin,

`integral R_T(alpha) dnu_b(alpha)`
` = -(C_2(omega)/2)(log T)^2`
`   + O(T^(-delta)(log T)^2 + b^2 (log T)^4)`.

Under RH, Theorem 1.4 and `VIS-260` add the actual-zeta transfer error

`O(T^(-delta)b^(-2))`.

Thus if `b=T^(-beta)` and

`0<2 beta<delta<epsilon/2`,

then the fixed-margin actual pair statistic minus the matched naive-GUE prediction satisfies

`integral [P_T(alpha)-GUE_T(alpha)] dnu_b(alpha)`
` = -(C_2(omega)/2)(log T)^2 + o((log T)^2)`.

In particular, **the fixed-margin smooth-test class contains a rigorously calibrated nonzero quadratic arithmetic carrier**. The remaining difficulty is no longer a universal absence of a low-frequency source coefficient.

**Evidence/status:** `LITERATURE+DERIVED + EXACT TEST-CLASS REDUCTION + SOURCE-CARRIER EXISTENCE + RH-CONDITIONAL ZETA TRANSFER + NO-NOVELTY-CLAIM`.

This does not identify a previously frozen application weight, prove that the original support-edge window has nonzero `C_2`, extend Rodgers' theorem to a moving support edge, or provide the four-level cross-window covariance required by the original edge--edge statistic.

## 1. Rodgers' diagonal kernel freezes the physical moments

Rodgers proves at the end of the paper that, for the smooth band-limited test class and the same fixed-margin frequency range as Theorem 1.4,

`integral omega(u)e(alpha log(T)u/(2pi))`
`  [T^(-1) integral_0^T (Q_t(u)-tilde Q_t(u))dt] du`
` = O_delta(T^(-delta))`.

At `alpha=0`, replace `omega` by `u^(2m)omega`. The transformed weight remains smooth and compactly supported, so the same estimate gives

`integral u^(2m)omega(u)`
`  [T^(-1) integral_0^T (Q_t(u)-tilde Q_t(u))dt] du`
` = O_(omega,m,delta)(T^(-delta))`.

Rodgers also computes exactly

`tilde Q_t(u)-K_t(u)=F(u)`,

and this expression contains no `t`. Adding the two pieces proves

`M_(2m)(T)=integral u^(2m)omega(u)F(u)du+O(T^(-delta))`.

At `alpha=0` one may obtain any fixed `delta<1/2` by choosing a fixed theorem margin `epsilon` with `2delta<epsilon<1`. Constants remain weight-, order-, margin-, and `delta`-dependent; no uniformity in a changing weight or changing support margin is asserted.

The alternative arithmetic expansion recorded by Rodgers is

`F(u)=(1/(2pi^2))[Re((zeta'/zeta)'(1+iu))+1/u^2`
`      + sum_(k>=2) c_k Re((zeta'/zeta)'(k+iku))]`,

`c_k=sum_(d|k) mu(d)d`.

So `C_(2m)(omega)` is an explicit arithmetic functional of the prime/zeta correction already present in the Bogomolny--Keating prediction; it is not a fitted statistic extracted from zero data.

## 2. The quadratic carrier exists in the admissible fixed-weight class

The only point needed for existence is Rodgers' observation that `F` is not identically zero. Because `F` is an ordinary real even function after its removable singularity at the origin is filled continuously, there is some nonzero `u_0` with `F(u_0)!=0`.

Choose an even nonnegative band-limited Schwartz approximate identity and place equal copies at `u_0` and `-u_0`. Each resulting `omega_(a,u_0)` is a fixed admissible weight once `a` is chosen. Dominated/approximate-identity convergence gives

`integral u^2 omega_(a,u_0)(u)F(u)du -> u_0^2F(u_0)`.

The limit is nonzero, so the integral is nonzero for all sufficiently concentrated members of the family. This is an existence theorem for the allowed test class, not an optimization prescription. It uses only the explicit source prediction and no held-out zeros.

This distinction matters experimentally. A later numerical or zero-data test must freeze one explicit weight before inspecting confirmation data. The present result only rules out the stronger obstruction that every admissible smooth fixed weight might annihilate the quadratic arithmetic source.

## 3. The sharp quadratic packet can recover that carrier

For a weight with `C_2(omega)!=0`, `VIS-261` gives

`R_T''(0)=-(log T)^2 M_2(T)`.

The moment reduction above therefore yields

`R_T''(0)=-(log T)^2 C_2(omega)+O(T^(-delta)(log T)^2)`.

The `VIS-257` packet has unit quadratic moment after cancelling the constant and sine-kernel cusp. Taylor's theorem from `VIS-261` gives

`integral R_T dnu_b=R_T''(0)/2+Rem`,

with

`|Rem| <= O(b^2 sup_(|alpha|<=b)|R_T''''(alpha)|)`.

Apply Rodgers' `Q_t-to-tilde Q_t` reduction again with weight `u^4 omega`, now uniformly for `|alpha|` inside the same fixed margin. The Fourier transform of `u^4 omega F` is bounded, so

`sup_(|alpha|<=b)|R_T''''(alpha)|=O((log T)^4)`

for every `b` staying inside that margin. Hence

`Rem=O(b^2(log T)^4)`.

For any power bandwidth `b=T^(-beta)` with `beta>0`, this Taylor remainder is `o((log T)^2)`. Under RH the remaining zeta-to-Bogomolny--Keating transfer is, by `VIS-260`,

`O(T^(-delta)||nu_b||_TV)=O(T^(-delta)b^(-2))`.

Choosing `2beta<delta<epsilon/2` makes this term negligible as well. The resulting nonzero main term is therefore certified without looking at confirmation zeros.

## 4. Prior art and novelty boundary

The sole external source needed for this reduction is:

Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, DOI `10.1093/qmath/has024`, arXiv `1203.3275`.

Theorem 1.4 supplies the RH-conditional fixed-margin `O_delta(T^(-delta))` comparison between the actual pair statistic and the Bogomolny--Keating prediction. In the concluding comparison Rodgers derives the `Q_t-to-tilde Q_t` error, the exact `t`-independent formula for `tilde Q_t-K_t`, and explicitly notes that this difference is not identically zero. The Fourier derivative/moment identity, closure of the test class under multiplication by a fixed polynomial, approximate-identity argument, and Taylor estimate used here are standard analysis.

No novelty is claimed for Rodgers' arithmetic correction, for Bogomolny--Keating lower-order pair correlation, or for the general fact that Fourier derivatives encode moments. The Mathia-specific content is the composition of those facts with the sharp cusp-packet conditioning already established in `VIS-257`--`VIS-261`, which closes the question of whether the admissible fixed-margin smooth-test class can contain a nonzero quadratic source carrier.

A targeted literature search around Rodgers' `Q_t-K_t` correction, low-frequency derivatives, and pair-correlation moments found the Rodgers paper itself as the directly relevant source and no closer independent theorem that changes this classification.

## 5. Boundaries and falsification

This result does **not** show that a particular previously frozen `omega` has `C_2(omega)!=0`. For any proposed application weight, compute its explicit integral against `F`; if it vanishes, the quadratic branch for that weight is killed and a higher carrier is admissible only after an independent source calculation.

The existence construction may select a weight using the explicit theoretical kernel `F`, but it must not use confirmation-zero data. Once a concrete weight is chosen for an empirical test, freeze it together with the packet family and normalizations before inspecting those data.

Nothing here changes the fixed-margin restriction of `VIS-260`. A family `epsilon_T->0`, an `omega_T` changing with height, or the bounded-tent edge geometry still needs a separate uniform theorem. Likewise the original disjoint edge--edge covariance remains a four-level problem; a two-level nonzero mean carrier does not determine its variance or cross-window averaging law.

Finally, the asymptotic main term is conditional on RH only when transported from the Bogomolny--Keating prediction to the actual zeta pair statistic through Theorem 1.4. The internal `Q_t-to-tilde Q_t` source reduction is an analytic property of Rodgers' prediction and should not be read as an independent proof of RH or of the unrestricted pair-correlation conjecture.

## Research consequence

The fixed-margin branch has crossed one previously open gate: **there is no universal quadratic-source obstruction in Rodgers' admissible smooth-test class**. At least one fixed real even band-limited weight has `C_2!=0`, and for that weight the sharp cusp-cancelled quadratic packet has a certified arithmetic main term after the Rodgers transfer error is paid.

The next coherent step should not climb the moment ladder. Choose and persist one explicit application weight, compute or bound its concrete `C_2(omega)` from the displayed `F`, and only then ask whether that weight has a useful dictionary to the original support-edge observable. The moving-edge uniformity and four-level covariance gates remain separate and unchanged.