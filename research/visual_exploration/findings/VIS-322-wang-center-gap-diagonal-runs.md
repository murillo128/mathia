# VIS-322 — center-gap decimation splits fixed-gate Wang paths into fixed-gap diagonal runs

## Claim

Keep the same-shell Bézout-strip setting and canonical Bézout representative of `VIS-319`--`VIS-321`:

`gcd(u,v)=1`, `u != v`,

`M/2 < u,v,q,r <= 2M`,

`h=qv-ur`, `|h|<=D`,

`au-bv=1`, `0<a<v`, `0<=b<u`,

and

`(q_j(h),r_j(h))=(u t_j(h)-bh, v t_j(h)-ah)`,

`t_j(h)=floor(U(h))-j`, `j=0,1,2`.

Let

`k=|v-u|`, `m=max(u,v)`, `sigma=sign(v-u)`,

and assume the subperiod condition

`2 floor(D)+1 < m`.

Then the large period `m` from `VIS-320` hides a second exact scale: the center gap `k`.

If `v>u`, put `d=a-b`. Then

`a/v = d/k - 1/(kv)`.

If `u>v`, put `d=b-a`. Then

`b/u = d/k + 1/(ku)`.

Equivalently, the mechanical rotation slope `c/m` from `VIS-321` and `d/k` are Farey neighbours:

`|dm-ck|=1`.

For every integer `h` for which both `h` and `h+k` lie in the determinant window, the candidate branch satisfies

`(q_j(h+k),r_j(h+k))-(q_j(h),r_j(h))=(sigma,sigma)`

except at **at most one** value of `h` in the whole subperiod window. At that single possible wrap one instead has

`(q_j(h+k),r_j(h+k))-(q_j(h),r_j(h))`
` = (sigma,sigma)-sigma(u,v)`.

This exceptional location is independent of the branch index `j`.

Now freeze the branch threshold as in `VIS-321`:

`B_j^0(h)=1[{U(h)}<T_j(0)]`.

Partition the determinant indices by their residue class modulo `k`. Away from the unique possible wrap, the phase along each such class moves monotonically by exactly `1/m` per `k`-step. Hence the fixed-gate admitted points on each residue class form at most one contiguous diagonal run; the one residue class containing the wrap can form at most two. If

`L=2 floor(D)+1`,

then each fixed-gate branch is therefore the disjoint union of at most

`min(k,L)+1`

runs on which

`(q,r)=(Q+n sigma,R+n sigma)`

for consecutive integers `n`. In particular `r-q` is constant on every run: each run is an ordinary fixed-gap prime-pair interval, not a genuinely mechanical prime sequence.

By the moving-to-frozen mask estimate of `VIS-321`, the actual Wang branch differs from this diagonal-run model by at most

`1+floor(2D/min(u,v))`

points. At the natural Wang scale `D=O(M/log log M)` this is eventually at most one point per branch.

Thus the remaining simultaneous-prime problem has an exact **center-gap fragmentation parameter**. Near-diagonal represented centers (`k` small) produce few long fixed-gap prime-pair runs; widely separated centers (`k` large) produce many short runs. The mechanical denominator `m asymp M` by itself does not describe the true sieve geometry.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-REDUCTION + FAREY/CHRISTOFFEL PRIOR-ART BOUNDARY + PRIME-SIEVE FRONTIER + NO-NOVELTY-CLAIM`.

No prime-pair upper bound on those runs, no uniform control of their singular series, no estimate for the large-`k` fragmented regime, no Wang natural-window estimate, and no stronger RH criterion is proved here.

## 1. The center gap is a Farey-neighbour denominator

Suppose first that `v>u` and write `k=v-u`. With `d=a-b`, the Bézout identity becomes

`du-bk=1`.

Using `a=b+d` and `v=u+k` also gives

`dv-ak=1`.

Therefore

`a/v = d/k - 1/(kv)`.

The active upper boundary from `VIS-320` is

`U(h)=2M/v+(a/v)h`,

so

`U(h+k)=U(h)+d-1/v`.

If instead `u>v`, write `k=u-v` and `d=b-a`. Then

`bk-du=1`,

`ak-dv=1`,

and hence

`b/u = d/k + 1/(ku)`.

Now

`U(h)=2M/u+(b/u)h`,

so

`U(h+k)=U(h)+d+1/u`.

In either orientation the rational slope with denominator `m=max(u,v)` lies exactly one Farey determinant away from a rational with denominator `k=|u-v|`. This relation is forced by the same Bézout identity that made the two one-step vectors in `VIS-321` unimodular.

## 2. A `k`-step is diagonal except at one wrap

Let

`f(h)={U(h)}`.

When `v>u`,

`floor(U(h+k))-floor(U(h))`

is `d` unless `f(h)<1/v`, in which case it is `d-1`.

For an ordinary `d` increment,

`q_j(h+k)-q_j(h)=ud-bk=1`,

`r_j(h+k)-r_j(h)=vd-ak=1`.

At the wrap the increment is instead

`(1-u,1-v)`.

When `u>v`, the floor increment is `d` unless `f(h)>=1-1/u`, where it is `d+1`. The ordinary coordinate increment is

`(-1,-1)`,

and the wrap increment is

`(u-1,v-1)`.

These are exactly the two cases in the compact formula of the claim.

Why can the wrap occur at most once? `VIS-320` gives an exact period `m`, and under

`2 floor(D)+1<m`

the phases `f(h)` in the determinant window are distinct points of one translated `1/m` grid. The wrap cell has half-open length exactly `1/m`: `[0,1/m)` when `v>u`, or `[1-1/m,1)` when `u>v`. Such a cell contains at most one phase from the subperiod sample.

The same conclusion holds simultaneously for `j=0,1,2` because subtracting `j` from `t_j` does not change any floor increment or phase.

## 3. Fixed branch gates become contiguous fixed-gap runs

Fix a branch `j` and its frozen threshold

`T=T_j(0)`.

On a residue class `h=h_0+n k`, the phase relation is

`f(h+k)=f(h)-1/v (mod 1)`

when `v>u`, and

`f(h+k)=f(h)+1/u (mod 1)`

when `u>v`.

Apart from the single possible wrap identified above, this is monotone motion by one grid cell. Therefore the threshold indicator

`1[f(h)<T]`

can change only once along a no-wrap residue class. The residue class containing the wrap can split into at most two admitted pieces.

There are at most `min(k,L)` nonempty residue classes modulo `k` in an interval of `L` consecutive determinant indices. Hence the admitted fixed-gate branch contains at most

`min(k,L)+1`

contiguous pieces.

On every such piece there is no wrap, so successive admitted indices differ by `k` and the corresponding lattice points differ by `(sigma,sigma)`. Reversing the parameter when `sigma=-1` if desired, every piece has the form

`(Q+n,R+n)`, `n=0,...,ell-1`,

for some integers `Q,R`. The gap `R-Q` is constant.

This removes a possible ambiguity in the phrase "prime pairs on a mechanical path". After decimation by the center gap, the fixed-gate path is made from ordinary diagonal prime-pair intervals; the only complexity is how many such intervals occur and how their fixed gaps vary across residue classes and branches.

## 4. The actual moving gate changes only boundedly many points

The diagonal decomposition above uses the frozen masks of `VIS-321`, not the original affine threshold.

That distinction is harmless at the natural Wang scale for the same exact reason already established there. Per branch,

`#{h: B_j(h) != B_j^0(h)}`
` <= 1+floor(2D/min(u,v))`.

Consequently the actual admitted branch is obtained from the diagonal-run model by adding or deleting only that many isolated points. With

`D=O(M/log log M)`, `min(u,v)>M/2`,

this is eventually at most one point per branch.

Across all three possible branches, the complete strip is therefore an `O(1)` perturbation of at most

`3[min(k,L)+1]`

fixed-gap diagonal runs.

The result is structural, not probabilistic: it does not assume any distribution of primes, any genericity of `u/v`, or any equidistribution beyond the exact subperiod grid already proved in `VIS-320`.

## 5. What this changes in the sieve frontier

`VIS-321` left a uniform simultaneous-prime problem on fixed-gate subperiod Christoffel paths. The present result shows that this is still too coarse a description.

If `k=|u-v|` is small compared with the determinant length, the branch consists of a small number of long diagonal intervals. On each one the primality conditions are simply

`Q+n prime`, `R+n prime`

with fixed difference `R-Q`. Classical Brun/Selberg upper-bound sieve machinery is therefore the natural local tool; no new "prime on a mechanical word" theorem is intrinsically required for that subregime.

If `k` is large, however, the number of diagonal pieces can be comparable with the available `O(D)` sample length, and applying a separate fixed-gap sieve to every short piece can lose the desired two-logarithm saving through fragmentation. The genuinely difficult part of the worst-cell route is therefore pushed toward **large center gap relative to the determinant window**, or toward finding a way to average the diagonal pieces before paying for them individually.

This is a sharper dichotomy than full-period versus subperiod rotation. Both small-`k` and large-`k` centers have the same mechanical period `m asymp M`; their prime-sieve geometry can nevertheless be very different.

## Prior-art and novelty boundary

The relation `|dm-ck|=1` is classical Farey-neighbour arithmetic, and rational mechanical words/Christoffel paths are classically organized by such neighbouring fractions and continued-fraction data. Jean-Pierre Borel and Christophe Reutenauer, **On Christoffel classes**, *RAIRO - Theoretical Informatics and Applications* 40:1 (2006), 15--27, DOI `10.1051/ita:2005038`, and Jean Berstel, Aaron Lauve, Christophe Reutenauer, Franco Saliola, **Combinatorics on Words: Christoffel Words and Repetitions in Words**, CRM Monograph Series 27, American Mathematical Society, DOI `10.1090/crmm/027`, provide the relevant classical Christoffel-word boundary.

Likewise, sieve methods for primes in Beatty/floor sequences are established prior art; Glyn Harman, **Primes in Beatty sequences in short intervals**, *Mathematika* 62:2 (2016), 572--586, DOI `10.1112/S0025579315000376`, is a nearby reference already relevant to `VIS-320`. No theorem from that literature is imported here to claim a prime count in the moving Wang regime.

No novelty is claimed for Farey neighbours, mechanical words, Christoffel decomposition, fixed-gap Brun/Selberg sieve, or the elementary floor identities themselves. The durable Mathia content is the exact specialization: the Wang branch rotation has a Farey neighbour whose denominator is **precisely the represented center gap `|u-v|`**, and decimation by that gap turns the frozen natural-window branch into at most `min(k,L)+1` fixed-gap diagonal runs with only a bounded correction for the true moving gate.

## Boundaries and falsification

The one-wrap statement requires the same subperiod condition as `VIS-321`. For a window of length at least `m`, the wrap cell can be visited repeatedly and the run count must include the number of completed periods.

The diagonal decomposition is a statement about branch geometry and gate membership. It does not bound the number of primes in a run, the fixed-gap singular series, or the total loss from summing sieve bounds over many short runs.

When `k>=L`, the bound `min(k,L)+1` gives no useful compression beyond the original point count. This is not a defect in the theorem; it identifies exactly where center-gap decimation stops buying averaging length.

The actual-gate `O(1)` conclusion is asymptotic at the natural Wang scale. Outside that scale retain the explicit `1+floor(2D/min(u,v))` correction instead.

Falsify the exact claim by finding admissible `u,v,M,D` and a candidate branch for which the displayed Farey-neighbour identity fails, more than one `k`-step wrap occurs inside a subperiod determinant window, a non-wrap `k`-step is not `(sigma,sigma)`, or a fixed-threshold admitted residue class contains more threshold components than allowed by the unique-wrap argument.

## Dependencies

- `VIS-319`: supplies the unimodular Bézout coordinates and exact two-prime local factor.
- `VIS-320`: supplies the three branches, rational rotation, exact period `m`, and subperiod natural window.
- `VIS-321`: supplies the one-step unimodular mechanical path and the bounded moving-to-frozen gate error.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining natural-window occupancy frontier.

## Research consequence

The next worst-cell sieve step should be organized by the center-gap scale `k=|u-v|`, not only by the mechanical denominator `m`.

The near-diagonal regime can now be attacked using ordinary fixed-gap prime-pair intervals after `k`-decimation, with the run lengths and singular-series cost tracked before recombination. The complementary large-`k` regime is the place where run fragmentation can erase that advantage and where a genuinely uniform congruence-discrepancy theorem, a multi-run sieve, or the coefficient-weighted energy route may still be necessary.

Further generic analysis of the full Christoffel word without separating the center-gap scale would mix these two qualitatively different sieve regimes.
