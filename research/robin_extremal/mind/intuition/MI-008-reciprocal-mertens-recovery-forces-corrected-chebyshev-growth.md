# MI-008 — The two late Robin Lyapunov coordinates are kernel-dual moments of one positive fan transport measure

**Evidence level:** exact on sufficiently late common positive rightmost CA fans under the hypotheses through RE-079; no contradiction with false RH or source-specific restriction on the transport-measure profile is proved.

RE-076 makes corrected Chebyshev `Hhat(C,b)=Z_b(C)-log rad(C)` strictly increasing along the late positive rightmost fan. RE-078 makes fringe-corrected logarithmic Mertens `Ehat(C,b)=E_l(Z_b(C))-delta_l(Z_b(C))` strictly decreasing and shows that a matched-run descent larger than the one-fringe scale cannot later be substantially reset.

RE-079 identifies the exact dependence hidden behind those opposite monotonicities. For any ordered selected fan segment `0<1`, there is a canonical positive finite measure `mu_(0,1)` supported on the selector interval `[Z_0,Z_1]` such that

`mu_(0,1)([Z_0,Z_1]) = Hhat_1-Hhat_0`

and

`Ehat_0-Ehat_1+B_1(0,1) = int_[Z_0,Z_1] (1/(s log s)) dmu_(0,1)(s)`.

Inside a fixed state cell the measure is simply `dZ`. Across a tied switch, the smooth common-amplitude selector dilation gives a positive continuous measure and every higher-layer exponent increment contributes an atom of mass `log p` at its event coordinate. New first-layer support births contribute no `Hhat` atom; instead they create the exact correction `B_1=sum -log(1-p^(-2))` in the reciprocal ledger.

Because the kernel `g(s)=1/(s log s)` is positive and decreasing,

`g(Z_1)(Hhat_1-Hhat_0) <= Ehat_0-Ehat_1+B_1 <= g(Z_0)(Hhat_1-Hhat_0)`.

Hence on bounded-dilation selector windows the two corrected increments are equivalent after multiplying the reciprocal decrement by `Z log Z`. They are **not independent source capacities** that can be added or multiplied to obtain extra coercivity; they are unweighted and `g`-weighted moments of one transport ledger.

The sole exact mismatch, first-layer births, has an absolutely summable late tail: all future `B_1` after scale `Z_0` are `O(1/Z_0)`. That does not make the correction negligible on every arbitrarily short segment, but it prevents it from creating a second macroscopic long-range budget.

The surviving source information is therefore the **distribution in selector scale** of `mu`: whether false-RH fan motion would require transport mass concentrated where the decreasing kernel gives an impossible weighted moment, whether actual prime-layer arithmetic forbids the needed concentration profile, whether first-layer births impose an additional spacing law, or whether an external prime-source estimate controls one moment more sharply than the other.

**Boundary.** RE-079 does not prove RH, constrain the transport-measure distribution enough for contradiction, or make `B_1` relatively negligible on every local segment. Its strategic effect is negative but important: opposite monotonicity alone supplies one transport degree of freedom, not two. New leverage must use scale separation or source-specific arithmetic.
