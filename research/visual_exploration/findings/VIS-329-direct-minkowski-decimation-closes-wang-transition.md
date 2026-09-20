# VIS-329 — direct Minkowski decimation of the original Wang rotation closes the remaining center-gap transition

## Claim

Keep the original same-shell Wang branch representation of `VIS-319`--`VIS-321`, before the center-gap renormalization of `VIS-325`. Thus

`gcd(u,v)=1`, `u != v`,

`M/2 < u,v <= 2M`,

`m=max(u,v)`,

`L=2 floor(D)+1 < m`,

and use the canonical Bezout pair

`au-bv=1`, `0<a<v`, `0<=b<u`.

For `j in {0,1,2}`, write the candidate branch on the `L` consecutive determinant indices `|h|<=floor(D)` as

`P_j(h)=(u t_j(h)-b h, v t_j(h)-a h)`,

where

` t_j(h)=floor(A+c h/m)-j`, `A=2M/m`,

with

`c=a` if `v>u`, and `c=b` if `u>v`.

The actual Wang strip is a subset of these three candidate branches, selected by the branch-admission masks of `VIS-320`; therefore an upper bound for simultaneous primality on the complete candidate branches is automatically an upper bound for strip occupancy.

No center-gap split is needed for that upper bound.

Consider the approximation lattice

`Lambda_(c,m)={(s,e) in Z^2 : e == c s (mod m)}`.

It has covolume `m`. Minkowski's convex-body theorem supplies, for `m>4`, a nonzero lattice point with, after changing sign if necessary,

`1<=s<=2 sqrt(m)`, `1<=E=|e|<=2 sqrt(m)`.

Write

`e=c s-p m`.

Then the following hold.

1. Among all admissible edges `h -> h+s`, at most `E` fail to have one fixed lattice displacement `G`; every exceptional edge differs by `sign(e)(u,v)`.
2. Removing those exceptional edges partitions the complete candidate branch into at most `s+E` constant-step affine runs.
3. On a run beginning at `h_0`, with `P_j(h_0)=(Q_0,R_0)`, the two-form resultant

   `Delta=Q_0 g_2-R_0 g_1`

   satisfies

   `Delta=p h_0-s t_j(h_0)`

   and

   `|Delta|<4s+E/2`.
4. The ordinary step is automatically small. If `v>u`,

   `G=((s-u e)/v,-e)`;

   if `u>v`,

   `G=(-e,(-s-v e)/u)`.

   Hence

   `max(|g_1|,|g_2|)<E+1`.
5. At the natural Wang scale the Minkowski step is nondegenerate: both coordinates of `G` are nonzero for all sufficiently large `M`.

Consequently the classical dimension-two Selberg upper-bound sieve, applied to the at most `s+E` affine pieces, gives

`P_j << Omega_(s,e) [ L/log^2(3+L/(s+E)) + s+E ]`,

where `P_j` is the number of indices on the complete candidate branch for which both coordinates are prime, and one may take

`Omega_(s,e)=(1+log log(3+C_(s,e)))^2`,

`C_(s,e)=(E+1)^2(4s+E)`.

At the natural Wang scale

`L asymp M/log log(3M)`, `m asymp M`,

the Minkowski vector has `s+E=O(sqrt(M))=o(L)`, while `C_(s,e)` is polynomial in `M`. Therefore

`P_j << L (log log M)^2/log^2 M`.

The same bound holds after summing the at-most-three candidate branches, uniformly in the center gap

`k=|u-v|`.

Relative to the natural two-prime Fourier-cell scale `L/log^2 M`, the branchwise excess is therefore

`A_M=O((log log M)^2)`

throughout the original subperiod regime `L<m`. Thus

`sqrt(A_M)=O(log log M)=o((log log M)^(3/2))`,

which is compatible with the taper-weighted destination isolated in `VIS-316`.

This closes the near-maximal transition `k<=L`, `k=M^(1-o(1))` left open by `VIS-328`. More strongly, it shows that the center-gap split used in `VIS-322`--`VIS-328` is not needed for the upper-bound occupancy closure at all: applying the same short-vector argument directly to the original period-`m` rational rotation covers every center gap at once.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + GEOMETRY-OF-NUMBERS RANGE-CLOSURE + SELBERG-SIEVE + REPRESENTATION-SIMPLIFICATION + NO-NOVELTY-CLAIM`.

No new Minkowski theorem, Diophantine-approximation theorem, Selberg-sieve theorem, prime-pair asymptotic, lower bound, full Wang theorem, or stronger RH criterion is claimed.

## 1. The original rational rotation already has the required short vector

`VIS-320` gives an exact rational phase

`x_h=A+c h/m`

with `gcd(c,m)=1` and observation length `L<m`.

The lattice

`Lambda_(c,m)={(s,e): e-cs in m Z}`

has determinant `m`. The symmetric square

`|s|<=2 sqrt(m)`, `|e|<=2 sqrt(m)`

has area `16m`, so Minkowski supplies a nonzero lattice point. For `m>4`, the coordinate bounds are strictly smaller than `m`. If `s=0`, the lattice congruence forces `m|e`, hence `e=0`; if `e=0`, coprimality of `c,m` forces `m|s`, hence `s=0`. Thus both coordinates are nonzero. Change the overall sign so that `s>0` and put `E=|e|`.

This is the same classical geometry-of-numbers input used in `VIS-328`, but applied one representation level earlier. The point is not a stronger approximation theorem: it is that the original Wang mechanical denominator `m` is already suitable for the short-vector decimation.

## 2. Short-vector decimation creates only `s+E` affine pieces

Since

`c s/m=p+e/m`,

one has

`t_j(h+s)-t_j(h)`
` = floor(x_h+p+e/m)-floor(x_h)`.

For `e>0`, this equals `p` except when `{x_h}>=1-E/m`, where it equals `p+1`. For `e<0`, it equals `p` except when `{x_h}<E/m`, where it equals `p-1`.

Because `gcd(c,m)=1` and the observation contains fewer than `m` consecutive determinant indices, the sampled phases `{x_h}` are distinct points of one translated `1/m` grid. The exceptional phase cell has length exactly `E/m`, so at most `E` eligible starts are exceptional.

Before deleting those edges, the `s` residue classes modulo `s` form at most `s` chains. Deleting at most `E` edges creates at most `E` additional components. Hence there are at most

`F=s+E`

constant-step affine runs.

This argument does not use `k=|u-v|`, continued fractions, center-gap periods, or a denominator-`k` replacement.

## 3. The direct step has coefficients of order only `E`

Let

`G=(g_1,g_2)=(u p-b s, v p-a s)`.

If `v>u`, then `m=v`, `c=a`, and `e=a s-pv`. Using `au-bv=1`,

`g_2=-e`,

`g_1=(s-u e)/v`.

If `u>v`, then `m=u`, `c=b`, and `e=b s-pu`. The same Bezout identity gives

`g_1=-e`,

`g_2=(-s-v e)/u`.

In either orientation one coordinate is exactly `-e`, while the other has absolute value below `E+1` because the smaller center coordinate is below `m` and `s<m`.

Thus

`max(|g_1|,|g_2|)<E+1`.

The step is also genuinely two-dimensional at the natural scale. In the `v>u` case, `g_1=0` would force `s=u e`; with `s>0`, this requires `e>0` and hence `s>=u>M/2`. In the `u>v` case, `g_2=0` would force `s=-v e`; with `s>0`, this requires `e<0` and hence `s>=v>M/2`. But Minkowski gives `s<=2 sqrt(m)=O(sqrt(M))`. Therefore neither degeneracy can occur for sufficiently large `M`.

This direct step bound is actually cleaner than the denominator-`k` bound in `VIS-328`: no Euclidean quotient `J=floor(m/k)` appears in the conductor.

## 4. The affine resultant remains at the short-vector scale

Fix one constant-step component and a point

`P_j(h_0)=(Q_0,R_0)`.

The Bezout coordinate map

`(t,h) -> (u t-b h, v t-a h)`

has determinant `-1`, and `G` is the image of `(p,s)`. Hence

`Delta=det(P_j(h_0),G)=p h_0-s t_j(h_0)`.

Writing

`t_j(h_0)=A+c h_0/m-theta-j`, `theta={A+c h_0/m}`,

and using `p=cs/m-e/m`, one gets the exact cancellation

`Delta=-e h_0/m-s A+s(theta+j)`.

The subperiod condition `L<m` implies `|h_0|<m/2`. Also `1<=A<4` and `0<=theta+j<3`. Therefore

`|Delta|<E/2+4s`.

The large prime coordinates have disappeared from the resultant. Together with the step bound, this gives the polynomial conductor

`|g_1 g_2 Delta| <= (E+1)^2(4s+E)`.

## 5. Selberg sieving the direct affine decomposition

On one ordinary component the candidate prime coordinates are

`Q(r)=Q_0+r g_1`,

`R(r)=R_0+r g_2`.

If one form has a fixed prime divisor, the component contains at most `O(1)` simultaneous-prime points and is harmless for an upper bound. Otherwise, for primes not dividing

`g_1 g_2 Delta`,

the two forms contribute the generic dimension-two pair of residue roots. All exceptional local factors are supported on primes dividing that conductor. The standard Mertens estimate therefore gives the same crude but sufficient correction used in `VIS-328`, bounded by

`Omega_(s,e)=(1+log log(3+C_(s,e)))^2`.

If `Delta=0`, the two affine forms are proportional along the run; because the step is nondegenerate, simultaneous primality occurs for only `O(1)` parameter values after fixed divisors are separated.

Apply the classical Selberg upper-bound sieve to each positive part of each affine component. Trimming a run to the indices on which both coordinates are positive does not increase the number of components, because each nonzero affine coordinate changes monotonically along the run.

For component lengths `r_i`, with at most `F=s+E` components and total length at most `L`, the same elementary dyadic grouping used in `VIS-328` gives

`sum_i r_i/log^2(3+r_i) << L/log^2(3+L/F)+F`.

Hence

`P_j << Omega_(s,e)[L/log^2(3+L/F)+F]`.

The branch-admission mask need not be analyzed for this upper bound: the true Wang branch is a subset of the complete candidate branch. This is why the direct original-period argument avoids both the center-gap fragmentation bookkeeping and the moving/frozen gate correction.

## 6. Natural-scale consequence

Let

`ell=log log(3M)`

and specialize to the natural subperiod scale already isolated in `VIS-320`,

`L asymp M/ell`, `m asymp M`.

Minkowski gives

`F=s+E=O(sqrt(M))`,

so

`L/F >> sqrt(M)/ell`

and therefore

`log(3+L/F) >> log M`.

Also

`C_(s,e)=O(M^(3/2))`,

so

`Omega_(s,e)=O(ell^2)`.

The additive component cost is negligible:

`ell^2 F = o(L ell^2/log^2 M)`.

Thus

`P_j << L ell^2/log^2 M`.

Summing over `j=0,1,2` changes only the absolute constant. In the `VIS-315`--`VIS-316` normalization this means

`A_M=O(ell^2)`

for the whole represented center, independently of `k`.

The center-gap analysis of `VIS-322`--`VIS-328` remains mathematically correct and exposes useful finer structure, but it is no longer required to close the upper-bound occupancy channel. In particular, the distinction between `k<=L` and `k>L` is a distinction of one representation, not a surviving obstruction of the underlying candidate set.

## Prior-art and novelty boundary

The two external ingredients are classical and already audited in the immediately preceding Wang findings.

Minkowski's convex-body theorem in determinant form is standard geometry of numbers; `VIS-328` records the *Encyclopedia of Mathematics* entry “Minkowski theorem” and J. W. S. Cassels, *An Introduction to the Geometry of Numbers*, Springer, Classics in Mathematics, DOI `10.1007/978-3-642-62035-5`.

The dimension-two upper-bound sieve for two affine prime forms is classical; `VIS-324` and `VIS-327` anchor it to Iwaniec--Kowalski, *Analytic Number Theory*, Chapter 6, and Friedlander--Iwaniec, *Opera de Cribro*, Chapters 7--8.

Rational mechanical words and the floor/rotation representation are classical as recorded in `VIS-320`--`VIS-322`. No novelty is claimed for any of those general tools.

A repository-level duplication check finds `VIS-328` as the closest prior Mathia result. Its short-vector argument is performed after replacing the original period `m` by the center-gap denominator `k`, which required `L<k`. The present result removes that unnecessary intermediate representation and applies the same classical machinery directly to the original period-`m` phase, whose already-proved subperiod condition is only `L<m`.

The durable new Mathia content is therefore a representation simplification and range closure, not a new theorem of geometry of numbers or sieve theory.

## Boundaries and falsification

The exact exceptional-edge count uses `L<m`. If an observation contains a full period or more, phase points repeat and the bound must include completed periods. The current Wang natural regime satisfies the subperiod condition by `VIS-320`.

The result is an upper bound for candidate-branch occupancy. It does not give a prime-pair asymptotic, lower bound, phase cancellation, or a pointwise Wang estimate.

The sieve conclusion is asymptotic and uses that `M` is large enough for the Minkowski step to be nondegenerate. Small `M` can be absorbed into absolute constants and is irrelevant to the natural-window asymptotic.

The proof deliberately counts candidate points not admitted by the exact branch mask. This can only weaken an upper bound; it would be invalid for a lower bound or an exact occupancy formula.

Falsify the exact result by exhibiting an admissible subperiod branch for which the direct approximation lattice does not have determinant `m`, more than `E` short-vector edges have the exceptional floor increment, one of the displayed step formulas fails, the resultant identity fails, or the candidate branch cannot be partitioned into at most `s+E` constant-step pieces after deleting the exceptional edges.

## Dependencies

- `VIS-315`: Fourier-cell occupancy reduction.
- `VIS-316`: taper-weighted shell-excess destination.
- `VIS-319`: unimodular Bezout coordinates preserving both prime-coordinate exclusions.
- `VIS-320`: original at-most-three rational mechanical branches and the subperiod condition `L<m`.
- `VIS-321`: canonical Bezout representative and candidate-path step representation.
- `VIS-324`: classical two-form Selberg upper-bound scale on affine runs.
- `VIS-328`: short-vector/Minkowski decimation method and conductor bookkeeping in the more restrictive denominator-`k` representation.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the moving-upper occupancy frontier.

## Research consequence

The moving-upper **local occupancy** route no longer has a live center-gap subregime at the natural subperiod scale. The same original-period short-vector decomposition gives a sufficient two-prime upper bound for every represented center, including the near-maximal `k<=L` transition left open by `VIS-328`.

The next Wang work should therefore not continue subdividing center gaps or descending further through Christoffel parents in search of branchwise density. Any remaining obstruction must lie outside this local occupancy channel: in the separate fixed-power source route, in a global bookkeeping step not already covered by the `VIS-316` criterion, or in another term of Wang's error budget. Further center-gap renormalization would refine a representation that is already sufficient for the upper-bound destination.