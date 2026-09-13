# MI-037 — Support height, time height and target margin form a three-stage conditioning window

**Evidence level:** supported by [AF-324](../../findings/AF-324-bounded-prime-height-quantifies-fixed-time-phase-covering.md), [AF-325](../../findings/AF-325-bounded-support-height-uniformizes-prime-antipodal-conditioning.md) and [AF-326](../../findings/AF-326-toeplitz-moment-positivity-couples-singular-second-and-third-harmonics.md), building on AF-322--AF-323. No exact middle-singular incidence theorem or sharp covering asymptotic is claimed.

The support parameter missing from the AF-322/AF-323 quantifier split can be priced explicitly. Fix `m` and `tau != 0`, and let `rho_(m,tau)(H)` be the covering radius in `(S^1)^m` of distinct-prime phase tuples with every prime at most `H`. AF-324 proves

`pi/pi(H) <= rho_(m,tau)(H) <<_(m,tau) H^(-19/40)`.

Thus bounded support height does not restore a fixed phase-space gap. It gives a finite-resolution net whose mesh still shrinks polynomially. AF-325 supplies the complementary finite-height exclusion. Uniformly over every eight-prime support `P` with `max P<=H` and `|t|>=1`, the distance from the four-antipodal-pair locus obeys

`delta_P(t) >= exp[-C (log H)^2 log(e+|t| log H)]`.

On a hypothetical exact middle-singular hit, the same joint `H,t` envelope transfers to the reconstruction denominator `|s_3|`. AF-326 adds a second transfer that is entirely source-independent once the incidence constraints hold. Toeplitz moment positivity gives

`|s_3|^2 <= 8(16-|s_2|^2)(32+|s_2|^2)/(64-|s_2|^2)`

and in particular

`4-|s_2| >= |s_3|^2/64`.

Therefore the source-specific Baker margin does not have to remain hidden in the coordinate used for inversion. Conditional on an exact prime middle-singular hit, it forces an explicit gap from the extremal second-harmonic face. The conditioning chain is now concrete:

`bounded source/time resources -> |s_3| margin -> retained |s_2| margin`.

The implication direction matters. Moment positivity by itself does not lower-bound `|s_3|`; the arithmetic source theorem supplies that input. Conversely, the arithmetic lower bound becomes useful downstream only after one proves that the target representation consumes a coordinate or norm in which the margin survives. AF-326 exhibits one exact instance of such a transfer.

The durable object is therefore a staged resource law rather than a support-independent condition number. Increasing support height enlarges the admissible source family; increasing time allows recurrence on each support; and the destination may consume a different geometric margin than the source theorem naturally controls. A faithful compression theorem must price all three stages under the correct quantifier order.

**Boundary.** AF-324 is a near-incidence theorem, not exact incidence or equidistribution. AF-325 does not decide whether `s_1=e_4=0` is ever attained. AF-326 is conditional on that exact centered middle-singular stratum and does not reverse the moment inequality. The lower and upper `H` scales remain far apart, so no sharp asymptotic for the source separation is known.
