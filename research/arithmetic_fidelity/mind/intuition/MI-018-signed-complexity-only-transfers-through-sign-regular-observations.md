# MI-018 — Finite sign complexity transfers only through a source certificate that survives recoding

**Evidence level:** supported by AF-217--AF-220 and sharpened quantitatively by [AF-338](../../findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order.md), with the source-side boundary localized through [AF-341](../../findings/AF-341-prime-layer-retains-rh-pole-discriminator-and-leading-sign-complexity.md)--[AF-345](../../findings/AF-345-prime-gap-occupancy-is-exact-sign-currency.md). The observation theorem is fixed-finite-order in the absolutely convergent half-plane; no uniform growing-order total positivity, critical-line transport or stable inverse bound is claimed.

The useful observation currency is not positivity of every minor. It is a **finite sign-variation budget matched to a finite observation order**. AF-217 shows that the Euler-log family is not globally totally positive, while AF-218--AF-220 recover strict sign regularity at fixed order under quantitative sampling geometry. AF-338 keeps the collision structure discarded by the earlier tail estimate and proves that, for fixed order `r`, row spacing `h`, and `q_j in [P,AP]`, the full Euler-log sampling matrix is eventually strictly sign-regular through order `r` whenever `sigma>r-1`.

AF-339--AF-341 show that the pole-cancelled zero-sensitive source is not sign-simple. The centered prime layer alone still has exactly the zeta-zero poles in `Re(s)>1/2` after its pole at `1` is cancelled, while its ordered sign variation is `Theta(P/log P)`. Higher prime powers are one-signed and holomorphic in that half-plane, so they carry neither the relevant zero poles nor the leading sign burden.

AF-342 proves that an arbitrary baseline cannot lower that prime-layer variation without reacting on a prime-scale set of prime or prime-adjacent sites. AF-343 rules out fixed periodic and more generally syndetic positive-composite repairs. AF-344 then shows why those cardinality bounds are not representation-independent: a fixed prime-independent perfect-power background remains residue-one and zero-pole-blind while reducing the residual zero-deleted sign variation to `O(P^(1/k))`; the cost moves into sparse support and amplitudes `asymp P^(1-1/k)`.

AF-345 identifies the exact quotient seen by the sign statistic for the whole nonnegative, sub-prime-height class. For consecutive primes let

`m_j = sum_(p_j<n<p_(j+1)) b(n)`

be the composite background mass in the `j`-th prime gap and let `J_b=# {j:m_j>0}`. After zeros are deleted, every occupied gap contributes the pattern `+,-,...,-,+` and every empty gap contributes `+,+`, hence

`V = 2 J_b`.

So ordered sign variation is exactly **prime-gap occupancy**. It is blind to the number of nonzero sites inside an occupied gap, their amplitudes and their description complexity. If `M=sum m_j` and `S_q=sum m_j^q`, Holder gives the sharp concentration law

`V^(q-1) S_q >= 2^(q-1) M^q`.

Equivalently the effective number of gaps carrying the retained mass is at most `V/2`. With pointwise amplitude `A` and maximum available interior gap width `G`, one also has `A V G >= 2M`. AF-344 is therefore not an isolated sparse construction: it exemplifies a general conservation law in which lowering sign variation forces surviving composite mass to concentrate into fewer prime gaps and pay through mass moments, amplitude, gap capacity or some combination.

The next bridge is consequently more precise than a generic “joint complexity” proposal. A source certificate used with finite sign-regular observation must either control a **prime-gap mass-concentration functional** that the observation theorem actually consumes, or prove a growing-order theorem whose constants charge that concentration. The prime-gap partition itself is an audit coordinate extracted from the arithmetic source and is not a cheap retained mark. A certificate that merely stores `J_b` or `(m_j)` without pricing how they were obtained would reintroduce the source information it claims to compress.

**Boundary.** AF-345 assumes nonnegative background and keeps the prime landmarks positive; signed backgrounds or baselines that neutralize primes require a different state variable. Its mass `M` excludes prime-site baseline mass, and the theorem is source-side: it does not prove that gap-mass moments are the correct destination norm or upgrade AF-338 to growing observation order. The durable conclusion is exact but narrow: once the source is recoded in this class, sign complexity survives only as occupied-prime-gap complexity, and reducing it necessarily reallocates retained mass into concentration.