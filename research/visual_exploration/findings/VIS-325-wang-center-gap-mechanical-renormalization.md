# VIS-325 — the maximally fragmented Wang branch renormalizes to the center-gap mechanical denominator

## Claim

Keep the fixed-gate Wang branch setting of `VIS-321`--`VIS-324`:

`gcd(u,v)=1`, `u != v`,

`M/2 < u,v,q,r <= 2M`,

`h=qv-ur`, `|h|<=D`,

with the canonical Bézout pair

`au-bv=1`, `0<a<v`, `0<=b<u`,

and candidate branches

`(q_j(h),r_j(h))=(u t_j(h)-bh, v t_j(h)-ah)`,

`t_j(h)=floor(U(h))-j`, `j=0,1,2`.

Put

`m=max(u,v)`, `n=min(u,v)`, `k=|v-u|`, `sigma=sign(v-u)`,

and let

`L=2 floor(D)+1`.

Assume the **maximally fragmented diagonal regime**

`L<k`.

Define

`c=a`, `d=a-b` when `v>u`,

and

`c=b`, `d=b-a` when `u>v`.

Then `gcd(d,k)=1`, `0<d<k`, and the exact Farey-neighbour identity of `VIS-322` is

`|d m-c k|=1`.

Write the active branch phase as

`U(h)=A+(c/m)h`, `A=2M/m`,

and define the **center-gap-renormalized phase**

`U_k(h)=A+(d/k)h`.

On the whole determinant window, the original fixed-gate branch and the branch obtained by replacing `U` by `U_k` differ at only `O(1)` determinant indices, uniformly in `u,v,M,D` under `L<k`:

1. `floor(U(h)) != floor(U_k(h))` for at most one `h`;
2. for every fixed threshold `T in [0,1]`, the masks `1[{U(h)}<T]` and `1[{U_k(h)}<T]` differ for at most two `h`;
3. consequently one frozen branch from `VIS-321` differs from its denominator-`k` renormalized branch at at most three determinant indices.

Combining this with the moving-to-frozen gate estimate of `VIS-321`, the actual Wang branch differs from the denominator-`k` renormalized branch at at most

`4+floor(2D/n)`

indices. At the natural Wang scale `D=O(M/log log M)` this is eventually at most four indices per branch.

The renormalized increment word has exact period `k`, contains exactly `d` one-steps per period, and its period displacement in `(q,r)`-coordinates is

`d s_1+(k-d)s_0=(sigma,sigma)`,

where

`s_0=(-b,-a)`, `s_1=(u-b,v-a)`.

Thus the diagonal `k`-step motion found in `VIS-322` is the period monodromy of a **lower-denominator rational mechanical path**, not merely an accidental decimation identity.

The regime `k>L`, where the first diagonal decomposition has run length one, is therefore not representation-final. Up to a bounded perturbation, the same observed Wang branch is a subperiod mechanical path with denominator `k<m`. The correct next structural question is whether continued-fraction/Christoffel renormalization of that lower-denominator path produces a primitive direction with usable repetition before the observation scale is exhausted, or whether the surviving continued-fraction regime instead supplies a discrepancy/energy estimate directly.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-REDUCTION + FAREY/CHRISTOFFEL RENORMALIZATION + SIEVE-FRONTIER + NO-NOVELTY-CLAIM`.

No iterative continued-fraction sieve theorem, prime-count estimate, Wang natural-window theorem, or stronger RH criterion is claimed.

## 1. The center-gap slope is exactly one Farey step from the original slope

Suppose first that `v>u`. Then `m=v`, `k=v-u`, `c=a`, and `d=a-b`. The identities already derived in `VIS-322` give

`d v-a k=1`,

hence

`a/v=d/k-1/(kv)`.

Therefore

`c/m=d/k-1/(km)`.

If instead `u>v`, then `m=u`, `k=u-v`, `c=b`, and `d=b-a`. The corresponding identities are

`b k-d u=1`,

so

`b/u=d/k+1/(ku)`

and therefore

`c/m=d/k+1/(km)`.

In both orientations,

`|c/m-d/k|=1/(km)`.

The same determinant-one identities show `gcd(d,k)=1`. In the present regime `k>L>=1`, the degenerate `k=1` endpoint is absent, and the displayed slope relation with `0<c<m` gives `0<d<k`.

So the unresolved center-gap denominator is not just a convenient partition size. It is the denominator of the unique adjacent rational slope forced by the same Bézout geometry.

## 2. Replacing the slope changes at most one floor value

Let

`D_0=floor(D)`.

For `|h|<=D_0`,

`|U(h)-U_k(h)|=|h|/(km)<=D_0/(km)`.

Since

`2D_0+1=L<k<m`,

one has

`2D_0/m<1`

and hence

`2D_0/(km)<1/k`.

Because `gcd(d,k)=1`, the phases

`{U_k(h)}`, `-D_0<=h<=D_0`,

are distinct points of one translated `1/k` grid: the window has fewer than `k` indices, so no phase repeats.

If `floor(U(h))` and `floor(U_k(h))` differ, the segment joining the two real numbers crosses an integer. Therefore `{U_k(h)}` lies within circular distance at most `D_0/(km)` of `0`.

The corresponding boundary arc has total length at most

`2D_0/(km)<1/k`.

A translated `1/k` grid contains at most one point in an arc shorter than one grid spacing. Thus

`#{h: floor(U(h)) != floor(U_k(h))}<=1`.

For every branch index `j`, replacing

`t_j(h)=floor(U(h))-j`

by

`t_(j,k)(h)=floor(U_k(h))-j`

therefore changes the candidate lattice point at at most one determinant index. At every other index the two candidate points are exactly identical, not merely close.

## 3. A fixed branch gate changes at most two memberships

Now fix any threshold `T in [0,1]`; in the Wang application this is the frozen threshold `T_j(0)` from `VIS-321`.

Compare

`B(h)=1[{U(h)}<T]`

with

`B_k(h)=1[{U_k(h)}<T]`.

Changing the phase by at most `D_0/(km)` can change membership in the circular interval `[0,T)` only when `{U_k(h)}` lies near one of its two boundary points, `0` or `T`.

Around each boundary, the relevant arc has length at most

`2D_0/(km)<1/k`.

Again the sampled `U_k` phases are distinct points of a translated `1/k` grid, so each boundary arc contains at most one sampled phase. Consequently

`#{h: B(h) != B_k(h)}<=2`.

The candidate-point change from Section 2 and the gate-membership change may overlap, but without using that overlap one already gets the uniform bound of three affected determinant indices for one frozen branch.

This is stronger than a small metric perturbation. Away from those at most three indices, the admitted renormalized branch is literally the same set of integer lattice points as the original frozen Wang branch.

## 4. The true moving gate remains only a bounded correction

`VIS-321` proves that the actual branch mask with affine threshold `T_j(h)` differs from its frozen version at no more than

`1+floor(2D/n)`

indices.

Combining that result with Sections 2--3 yields

`# {indices where actual branch and denominator-k renormalized branch differ}`
` <= 4+floor(2D/n)`.

At the natural scale

`D=O(M/log log M)`, `n>M/2`,

one has `2D/n=o(1)`, so the right-hand side is eventually at most four.

Across the at-most-three Wang branches this is still an absolute `O(1)` perturbation. Such a bounded change is already beneath the explicit leading `1` allowed in the local occupancy criterion of `VIS-315`--`VIS-316`; it cannot by itself create the unbounded excess needed to obstruct the natural-window mean-square target.

## 5. The renormalized period has diagonal monodromy

The denominator-`k` word

`delta_k(h)=floor(U_k(h+1))-floor(U_k(h))`

is a rational mechanical word of slope `d/k`. Since `gcd(d,k)=1`, it has exact period `k` and exactly `d` one-steps in each complete period.

Its lattice steps are still the original unimodular pair

`s_0=(-b,-a)`,

`s_1=(u-b,v-a)`.

If `v>u`, the identities

`d u-b k=1`, `d v-a k=1`

give

`d s_1+(k-d)s_0=(1,1)`.

If `u>v`, the identities

`b k-d u=1`, `a k-d v=1`

give

`d s_1+(k-d)s_0=(-1,-1)`.

Hence in both cases

`d s_1+(k-d)s_0=(sigma,sigma)`.

This identifies the exact structural meaning of `VIS-322`'s center-gap decimation. Advancing one full period of the renormalized denominator-`k` word moves the branch by one diagonal lattice unit. The fixed-gap diagonal runs are the period fibres of this lower-denominator mechanical representation.

When `k<=L`, several such periods are visible and the diagonal-run sieve of `VIS-324` is the natural representation. When `k>L`, no complete denominator-`k` period is visible, but the same representation still describes the branch up to bounded error. The apparent loss of all run length is therefore a failure of the **first period direction**, not a proof that the path has no deeper arithmetic repetition.

## 6. The remaining frontier becomes a continued-fraction renormalization problem

`VIS-324` correctly shows that branchwise fixed-gap Selberg sieving closes every polynomially long first-level run and stalls when `k=M^(1-o(1))`, especially for `k>L`.

The present result changes the interpretation of that stall. In the fully fragmented range, the branch may be replaced, at bounded cost, by the exact rational mechanical word of slope `d/k`. Rational mechanical words admit the classical continued-fraction/Christoffel hierarchy: their shorter Farey neighbours and standard-word decompositions expose successive primitive block directions.

What is **not** proved here is that iterating that hierarchy necessarily yields a block long enough for the two-prime sieve target. A continued-fraction denominator near the observation length can still leave only short repetitions, and replacing one representation by another does not manufacture prime cancellation.

But it is now incorrect to treat `k>L` as intrinsically point-fragmented. It is only point-fragmented after quotienting by the first diagonal period. A next useful theorem can ask a sharper dichotomy:

- a large partial quotient may create many repeats of a shorter Christoffel block, yielding a new primitive affine direction on which ordinary two-linear-form sieve methods can act;
- a bounded-type or otherwise nonrepetitive continued-fraction regime may instead have enough deterministic discrepancy/energy control to bypass per-block sieving.

Either route must eventually be evaluated against the weighted destination `B(x,V)=o((log log x)^(3/2))` of `VIS-316`, rather than against an unnecessarily uniform theorem over every center.

## Prior-art and novelty boundary

Farey neighbours, rational mechanical words, Christoffel paths, and their continued-fraction/standard-word renormalizations are classical. The prior-art boundary is the same one already audited in `VIS-321`--`VIS-322`, including Jean-Pierre Borel and Christophe Reutenauer, **On Christoffel classes**, *RAIRO - Theoretical Informatics and Applications* 40:1 (2006), 15--27, DOI `10.1051/ita:2005038`, and Jean Berstel, Aaron Lauve, Christophe Reutenauer, Franco Saliola, **Combinatorics on Words: Christoffel Words and Repetitions in Words**, CRM Monograph Series 27, American Mathematical Society, DOI `10.1090/crmm/027`.

No novelty is claimed for replacing one rational slope by a Farey neighbour in abstract symbolic dynamics, for Christoffel standard words, or for continued fractions.

The Mathia-specific durable content is the exact Wang specialization: the first lower denominator is **precisely the center gap `k=|u-v|`**, the slope displacement is exactly `1/(km)`, the whole natural determinant window in the previously "maximally fragmented" regime changes at only boundedly many indices, and the lower-denominator period monodromy is exactly the diagonal vector `(sigma,sigma)` used by the prior sieve decomposition.

## Boundaries and falsification

The bounded-error renormalization uses `L<k`. When the observation interval contains a full denominator-`k` period, the diagonal-run representation of `VIS-322`--`VIS-324` is already the more direct description.

The comparison uses the same intercept `A` and the same frozen branch threshold. Choosing a different intercept may change the exact finite mismatch count, though classical conjugacy of rational mechanical words still applies at the representation level.

The result controls branch geometry and gate membership only. It does not estimate primes, sieve remainders, Wang phases, coefficient-weighted energy, or occupancy after further renormalization.

The continued-fraction discussion in Section 6 is a research consequence, not an established iteration theorem for the Wang problem. In particular, no claim is made that every continued-fraction branch eventually supplies polynomially long affine runs before the relevant scale is exhausted.

Falsify the exact result by exhibiting an admissible `L<k` Wang branch for which `|c/m-d/k|!=1/(km)`, `gcd(d,k)!=1`, more than one sampled `U_k` phase lies in either sub-grid-spacing boundary arc used above, the frozen admitted sets differ at more than three determinant indices, or the denominator-`k` period displacement differs from `(sigma,sigma)`.

## Dependencies

- `VIS-316`: weighted shell-occupancy destination for the natural Wang mean square.
- `VIS-321`: fixed-gate mechanical-path reduction and moving-to-frozen `O(1)` error.
- `VIS-322`: center-gap Farey-neighbour identity and first diagonal decimation.
- `VIS-323`: aggregate singular-series neutrality of the first diagonal decomposition.
- `VIS-324`: closure of all polynomially long first-level diagonal runs by classical Selberg sieve.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining natural-window occupancy frontier.

## Research consequence

Do not treat `k>L` as the terminal geometry of the Wang branch. Before switching entirely to a generic multi-run or energy theorem, exploit the exact lower-denominator representation: the observed branch is an `O(1)` perturbation of the rational mechanical path with slope `d/k`, and its diagonal `k`-step is exactly that path's period monodromy.

The next coherent question is whether the **continued-fraction hierarchy of `d/k`**, together with the preserved two-prime local factor and the Wang taper, yields a useful repeated primitive direction or a complementary discrepancy/energy bound in the `k=M^(1-o(1))` frontier. Any positive result must still supply real arithmetic control; representation renormalization alone is not cancellation.
