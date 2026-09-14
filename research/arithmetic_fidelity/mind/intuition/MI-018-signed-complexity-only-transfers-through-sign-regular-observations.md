# MI-018 — Finite sign complexity transfers only through a source certificate that survives recoding

**Evidence level:** supported by AF-217--AF-220 and sharpened quantitatively by [AF-338](../../findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order.md), with the source-side boundary localized through [AF-341](../../findings/AF-341-prime-layer-retains-rh-pole-discriminator-and-leading-sign-complexity.md)--[AF-346](../../findings/AF-346-power-backgrounds-saturate-prime-gap-concentration-exponent.md). The observation theorem is fixed-finite-order in the absolutely convergent half-plane; no uniform growing-order total positivity, critical-line transport or stable inverse bound is claimed.

The useful observation currency is a finite sign-variation budget matched to a finite observation order. AF-338 proves that, for fixed order `r`, spacing `h` and `q_j in [P,AP]`, the full Euler-log sampling matrix is eventually strictly sign-regular through order `r` whenever `sigma>r-1`.

The source side is much less rigid. AF-339--AF-341 isolate a centered prime layer that still carries the RH-complete right-half-plane pole discriminator and `Theta(P/log P)` ordered sign variation. AF-342--AF-343 rule out broad low-exception and periodic/syndetic positive repairs. AF-344 then gives a fixed prime-independent perfect-power background that remains residue-one and zero-pole-blind while reducing the residual variation to `O(P^(1/k))`.

AF-345 identifies the exact quotient seen by that sign statistic. For nonnegative backgrounds below prime height, if `m_j` is the composite mass in the `j`-th consecutive-prime gap and `J_b=# {j:m_j>0}`, then

`V = 2 J_b`,

and for `M=sum m_j`, `S_q=sum m_j^q`,

`V^(q-1) S_q >= 2^(q-1) M^q`.

Thus ordered sign variation is exactly prime-gap occupancy; lowering it forces retained mass to concentrate into fewer gaps.

AF-346 closes the possibility that this Holder trade is already the missing representation-invariant source bill. For every fixed `k>=3`, the same prime-independent weighted `k`-th-power backgrounds satisfy on fixed multiplicative windows

`V asy X^(1/k)`, `M asy X`, `S_q asy X^(q-(q-1)/k)`.

They therefore attain the AF-345 exponent exactly, and on thin multiplicative windows their Holder ratio approaches the sharp constant. The family keeps the RH pole discriminator while saturating the concentration law. Hence neither sign count nor the unavoidable prime-gap `q`-moment, by itself, distinguishes the arithmetic source from this explicit recoding.

The next bridge must use a stronger source certificate: a normalized concentration/locality profile that these power backgrounds violate and the destination actually consumes, or a growing-order observation theorem whose constants quantitatively charge more than one occupancy/moment statistic. Merely strengthening the AF-345 inequality at the same level is impossible at the exponent scale under its present hypotheses.

**Boundary.** AF-345 assumes nonnegative backgrounds and positive prime landmarks. AF-346 proves sharpness only for fixed `k>=3`; the square case is separated by the unresolved consecutive-square prime-gap boundary. None of these findings shows that a particular concentration functional is sufficient for critical-line transport. The durable conclusion is narrower: after source recoding, finite sign complexity survives only through a quotient that simple prime-independent backgrounds can already saturate, so the missing certificate must retain more structure than that quotient.