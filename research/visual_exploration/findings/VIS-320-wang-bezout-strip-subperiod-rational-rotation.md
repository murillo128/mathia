# VIS-320 — natural Wang Bézout strips split into at most three subperiod rational-rotation branches

## Claim

Keep the represented same-shell determinant geometry of `VIS-315`--`VIS-319`:

`gcd(u,v)=1`, `u != v`,

`M/2 < u,v,q,r <= 2M`,

`h=qv-ur`, `|h|<=D`,

and choose any Bézout pair `a,b in Z` with

`au-bv=1`.

Write the `VIS-319` unimodular coordinates as

`q=ut-bh`, `r=vt-ah`.

Assume

`0<=D<M/2`.

For real `h`, define

`L_u(h)=(M/2+bh)/u`, `U_u(h)=(2M+bh)/u`,

`L_v(h)=(M/2+ah)/v`, `U_v(h)=(2M+ah)/v`.

Then the shell condition is exactly

`max(L_u(h),L_v(h)) < t <= min(U_u(h),U_v(h))`.

The two max/min choices do **not** switch anywhere in `|h|<=D`:

- if `v>u`, then `L=L_u` and `U=U_v` throughout the strip;
- if `u>v`, then `L=L_v` and `U=U_u` throughout the strip.

Moreover the width

`W(h)=U(h)-L(h)`

is affine with slope `+1/(uv)` when `v>u` and `-1/(uv)` when `u>v`, and always satisfies `W(h)<3`.

Consequently every lattice point in the strip belongs to one of at most three exact branches. For `j=0,1,2`, put

`t_j(h)=floor(U(h))-j`.

Then

`Omega_(M,D)(u,v) cap Z^2`

is exactly the disjoint union over integer `|h|<=D` and `j in {0,1,2}` satisfying

`{U(h)}+j < W(h)`

of the points

`(t,h)=(t_j(h),h)`.

The fractional-part process `{U(h)}` is a rational rotation of exact period

`m=max(u,v)`.

Indeed its step is `a/v` when `v>u` and `b/u` when `u>v`; the Bézout identity gives `gcd(a,v)=gcd(b,u)=1`.

At the natural Wang resolution from `VIS-319`,

`D asymp M^2/V`, `V asymp M log log M`,

so `D asymp M/log log M`. Hence, for sufficiently large `M` (with the asymptotic constants fixed),

`2 floor(D)+1 < m`.

Thus the entire relevant determinant strip samples **less than one period** of the rational rotation. The remaining occupancy problem is not a generic two-dimensional box-distribution problem: it is a simultaneous-prime problem on at most three moving rational mechanical branches over a subperiod orbit, with the Wang taper still controlling how shellwise excess is aggregated.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-REDUCTION + PRIME-PAIR SIEVE FRONTIER + PRIOR-ART BOUNDARY + NO-NOVELTY-CLAIM`.

No prime-pair counting estimate, thin-strip sieve theorem, Beatty-prime theorem, Wang natural-window estimate, or stronger RH criterion is proved here.

## 1. The shell boundaries have no crossover in the natural strip

The four affine boundary functions satisfy two exact difference identities. First,

`L_u(h)-L_v(h)`
` = [M(v-u)/2-h]/(uv)`.

Second,

`U_u(h)-U_v(h)`
` = [2M(v-u)-h]/(uv)`.

These follow directly from `au-bv=1`.

If `v>u`, then `v-u>=1`. Under `|h|<=D<M/2`,

`M(v-u)/2-h > 0`

and

`2M(v-u)-h > 0`.

Therefore `L_u>L_v` and `U_u>U_v`, so the intersection uses

`L=L_u`, `U=U_v`

for every `h` in the strip.

If `u>v`, both signs reverse throughout the strip, giving

`L=L_v`, `U=U_u`.

The apparent moving polygon from `VIS-319` therefore has a fixed pair of active sides at the natural determinant scale. No internal change of boundary regime occurs.

## 2. The strip width is almost constant and has fewer than three integer levels

When `v>u`,

`W(h)=U_v(h)-L_u(h)`
` = 2M/v-M/(2u)+h/(uv)`.

When `u>v`,

`W(h)=U_u(h)-L_v(h)`
` = 2M/u-M/(2v)-h/(uv)`.

Thus the total width variation across the whole determinant window is at most

`2D/(uv)`.

Since `u,v>M/2`, this is `O(D/M^2)` and therefore `O(1/(M log log M))` at the natural Wang scale.

Independently of that sharper variation bound, the intersection is contained in each single-coordinate shell interval. For example,

`M/2 < ut-bh <= 2M`

has `t`-length

`3M/(2u) < 3`.

Hence `W(h)<3` whenever the intersection is nonempty.

For any interval `(L,U]` of length below three, its integer points are among

`floor(U)`, `floor(U)-1`, `floor(U)-2`.

Writing `U=L+W`, the point `floor(U)-j` lies above the strict lower boundary exactly when

`floor(U)-j>L`

which is equivalent to

`{U}+j<W`.

This proves the three-branch decomposition without approximation.

## 3. The branch mask is an exact rational rotation

Suppose `v>u`. Then the active upper boundary is

`U(h)=2M/v+(a/v)h`.

Any common divisor of `a` and `v` divides both `au` and `bv`, hence divides `au-bv=1`; therefore

`gcd(a,v)=1`.

So as integer `h` advances, `{U(h)}` follows a rational rotation with exact period `v`.

If `u>v`, the active upper boundary is

`U(h)=2M/u+(b/u)h`,

and the same Bézout argument gives `gcd(b,u)=1`, hence exact period `u`.

Changing the Bézout solution by

`(a,b) -> (a+kv,b+ku)`

adds the integer `kh` to the active upper boundary for integer `h`. The fractional-part orbit and the branch masks are therefore independent of which Bézout representative is chosen.

For each admitted branch point, the prime coordinates are still

`q_j(h)=u t_j(h)-bh`,

`r_j(h)=v t_j(h)-ah`.

So the two coordinatewise primality conditions that were visible modulo every prime in `VIS-319` have not been projected away. They are now carried by at most three one-parameter rational mechanical sequences.

## 4. The natural Wang regime is subperiod, not equidistributed over a full rational cycle

Let

`m=max(u,v)`.

Because `u,v>M/2`, one has `m>M/2`. At the natural Fourier resolution,

`D asymp M/log log M`.

For fixed implied constants, eventually

`2 floor(D)+1 < M/2 < m`.

Hence the determinant interval `-D<=h<=D` visits fewer than `m` consecutive states of the period-`m` rational rotation.

This matters for proof strategy. Exact full-period residue balance of a rational rotation cannot by itself supply the required prime-pair occupancy estimate, because the relevant window ends before one full orbit is seen. The remaining theorem must control a **subperiod** segment uniformly as the denominator/slope moves with the represented prime ratio, or bypass that worst-cell question through the weighted-energy route already allowed by `VIS-316`.

This also explains why the two correct statements from `VIS-318` and `VIS-319` coexist. A fixed determinant fibre has only `O(1)` candidates, yet the family of `O(D)` fibres is not an amorphous two-dimensional cloud: it is organized by a low-width rational rotation carrying both prime coordinates.

## Prior-art and novelty boundary

Mechanical/floor sequences and primes in Beatty-type sequences are classical subjects. Banks and Shparlinski, **Prime numbers with Beatty sequences**, *Colloquium Mathematicum* 115:2 (2009), 147--157, DOI `10.4064/cm115-2-1`, prove prime asymptotics for fixed positive irrational slopes of finite type, including congruence restrictions. Harman, **Primes in Beatty sequences in short intervals**, *Mathematika* 62:2 (2016), 572--586, DOI `10.1112/S0025579315000376`, shows that sieve methods for primes in short intervals can be adapted to Beatty sequences. Brüdern and Kawada, **The localisation of primes in arithmetic progressions of irrational modulus**, *Colloquium Mathematicum* 123:1 (2011), 53--61, DOI `10.4064/cm123-1-5`, likewise obtain a short-interval Beatty-prime asymptotic.

Those sources establish that floor/rotation structure plus primality is not a new general mechanism. They do **not**, by the statements audited here, supply the present moving regime: the slope is rational with denominator `m asymp M`, the observed determinant interval has length `D=o(m)`, two prime coordinates must be imposed simultaneously, the represented center moves, and the destination only needs the taper-weighted aggregate criterion of `VIS-316`.

For comparison, the standard rational-slope reduction itself is elementary: a rational mechanical sequence is periodic modulo its denominator (equivalently, a rational Beatty-type set decomposes into finitely many congruence patterns). The point of this finding is not that fact, but the exact identification of the `VIS-319` Wang strip with **at most three** such subperiod branches and the resulting sharpening of the missing proof obligation.

No novelty is claimed for Bézout parametrization, rational rotations, Beatty/mechanical sequences, or the cited prime-sieve machinery.

## Boundaries and falsification

The no-crossover statement uses `D<M/2`. This holds eventually in the natural Wang regime `D asymp M/log log M`; it need not hold for a much wider determinant strip. Outside this range the active sides may switch and the branch description must be partitioned into the corresponding affine regimes.

The subperiod conclusion is asymptotic and uses fixed constants in `D asymp M/log log M`. It does not assert pseudorandomness or non-randomness of the visited orbit segment. In particular, being subperiod is a warning against importing full-cycle equidistribution, not a proof that useful discrepancy bounds are impossible.

The exact branch decomposition alone gives no `1/log^2 M` prime density. The local factor `(1-1/ell)^2` from `VIS-319` remains only a residue-space input until a sieve/discrepancy argument controls the actual moving branch segment.

Falsify the exact claim by finding admissible `u,v,M,D,h` with `D<M/2` for which the displayed active-bound choice switches, by finding a strip lattice point not represented by `j in {0,1,2}` and `{U(h)}+j<W(h)`, or by finding a Bézout solution for which the active fractional-part step does not have period `max(u,v)`.

## Dependencies

- `VIS-315`: reduces a Fourier-resolution prime-ratio cell to a thin determinant strip around a represented slope.
- `VIS-316`: shows that the destination needs only a Wang-taper-weighted shell occupancy profile.
- `VIS-317`: proves that scalar determinant projection destroys the two coordinatewise prime exclusions.
- `VIS-318`: proves that each fixed determinant fibre has only bounded same-shell lattice length.
- `VIS-319`: restores both prime exclusions by the joint unimodular Bézout coordinates and isolates thin-domain distribution as the remaining obstacle.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining pair-preserving natural-window frontier.

## Research consequence

`VIS-319` left the live route as a uniform sieve/discrepancy problem on a moving long-thin two-dimensional lattice domain. The present reduction makes that object substantially more rigid.

At the natural Wang scale, one may equivalently seek a uniform upper-bound sieve or congruence-discrepancy estimate for at most three simultaneous-prime rational mechanical branches of length

`D asymp M/log log M`

whose rotation denominator is

`m asymp M`,

then feed the resulting shell excess into the weighted criterion of `VIS-316`. A successful theorem need not prove a generic two-dimensional lattice-point distribution statement beyond what these branches actually use.

Conversely, a counterexample route should now exhibit a subperiod rational-rotation segment whose branch masks create excessive prime-pair crowding in a central or weakly tapered shell and whose Wang coefficient mass survives aggregation. Full-period rational equidistribution, scalar determinant sieving, and fixed-fibre long-sieve arguments do not address this sharpened frontier.
