# VIS-328 — Minkowski decimation closes the maximally fragmented Wang regime

## Claim

Keep the denominator-`k` Wang branch of `VIS-325`--`VIS-327`. Thus

`gcd(u,v)=1`, `u != v`,

`M/2 < u,v <= 2M`,

`m=max(u,v)`, `n=min(u,v)`, `k=|u-v|`, `sigma=sign(v-u)`,

`L=2 floor(D)+1 < k`,

and, after the bounded renormalization error of `VIS-325`, one frozen branch is

`t_j(h)=floor(A+d h/k)-j`,

`P_j(h)=(u t_j(h)-b h, v t_j(h)-a h)`,

for `j in {0,1,2}`, `|h|<=floor(D)`, `A=2M/m`, and the canonical Bézout pair `au-bv=1`. The reduced slope satisfies `gcd(d,k)=1`.

The first Christoffel parents used by `VIS-326`--`VIS-327` are not needed to exhaust the fragmented range. For any integers `s,p` with

`1<=s<k`, `e=d s-p k`, `0<|e|<k`,

put `E=|e|` and

`G=(g_1,g_2)=(u p-b s, v p-a s)`.

Then:

1. among the admissible edges `h -> h+s`, at most `E` fail to have displacement exactly `G`; every exceptional edge has displacement `G+sign(e)(u,v)`;
2. deleting those exceptional edges partitions the branch into at most `s+E` constant-step affine runs;
3. on every such run starting at `h_0`, with `P_j(h_0)=(Q_0,R_0)`, the two-form resultant is

   `Delta=Q_0 g_2-R_0 g_1=p h_0-s t_j(h_0)`,

   and satisfies `|Delta|<4s+E/2`, hence `|Delta|<=4s+E`;
4. the step itself has the exact orientation-free formula

   `G=((sigma s-u e)/k, (sigma s-v e)/k)`,

   so `g_2-g_1=-sigma e` and

   `max(|g_1|,|g_2|) <= 1+E(J+1)`, `J=floor(m/k)`;
5. a step can be coordinate-degenerate only in the `J=1` regime, and then necessarily

   `(s,e)=r(n,sigma)`

   for some positive integer `r`.

Now consider the determinant-`k` approximation lattice

`Lambda_(d,k)={(s,e) in Z^2 : e == d s (mod k)}`.

It has covolume `k`. Minkowski's convex-body theorem applied to the square

`|s|<=2 sqrt(k)`, `|e|<=2 sqrt(k)`

gives a nonzero lattice point. For `k>4`, neither coordinate can vanish; after changing sign if necessary one may choose

`1<=s<=2 sqrt(k)`, `1<=E<=2 sqrt(k)`.

At the natural Wang scale

`L asymp M/log log(3M)`, `L<k`,

this Minkowski decimation has

`s+E=O(sqrt(M))=o(L)`.

Moreover the same-shell condition gives `n>M/2`, so the coordinate-degenerate ray from item 5 has `s>=n>M/2` and cannot contain the Minkowski vector for large `M`. Thus the selected step is genuinely two-dimensional even in the `J=1` case that left a first-parent axis degeneracy in `VIS-326`--`VIS-327`.

Applying the classical dimension-two Selberg upper-bound sieve to the resulting affine runs yields

`P_j << Omega_(s,e) [ L/log^2(3+L/(s+E)) + s+E ]`,

where one may take

`Omega_(s,e) = (1+log log(3+C_(s,e)))^2`,

`C_(s,e)=(1+E(J+1))^2(4s+E)`.

In the fragmented natural regime, `J=O(log log M)`, so the Minkowski vector gives

`Omega_(s,e)=O((log log M)^2)`

and therefore

`P_j << L (log log M)^2/log^2 M`.

The bounded branch-renormalization and moving-gate errors from `VIS-321` and `VIS-325` do not change this scale. Relative to the natural two-prime cell scale `L/log^2 M`, every maximally fragmented center `k>L` consequently has excess

`A_M=O((log log M)^2)`.

Thus `sqrt(A_M)=O(log log M)=o((log log M)^(3/2))`, which is compatible with the taper-weighted destination of `VIS-316`. The maximally fragmented range `k>L` is therefore no longer a live Wang occupancy obstruction.

The remaining branchwise frontier is the near-maximal but non-fragmented transition

`k<=L`, `k=M^(1-o(1))`,

where `VIS-324` leaves only subpolynomial first-level run length and the bounded-error denominator-`k` replacement used here is no longer available in this form.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + GEOMETRY-OF-NUMBERS RANGE-CLOSURE + SELBERG-SIEVE + NO-NOVELTY-CLAIM`.

No new Minkowski theorem, Diophantine-approximation theorem, Selberg-sieve theorem, prime-pair asymptotic, lower bound, full Wang natural-window theorem, or stronger RH criterion is claimed.

## 1. Arbitrary short Diophantine decimation

Write

`x_h=A+d h/k`.

Since `d s/k=p+e/k`,

`t_j(h+s)-t_j(h)`
` = floor(x_h+p+e/k)-floor(x_h)`.

If `e>0`, this equals `p` except when `{x_h}>=1-e/k`, where it equals `p+1`. If `e<0`, it equals `p` except when `{x_h}<E/k`, where it equals `p-1`.

Because `gcd(d,k)=1` and the observation interval contains fewer than `k` consecutive determinant indices, the phases `{x_h}` are distinct points of one translated `1/k` grid. An interval of length `E/k` contains at most `E` such grid points. Hence at most `E` admissible `s`-edges are exceptional.

For every ordinary edge,

`P_j(h+s)-P_j(h)=G`.

At an exceptional edge, the extra `+1` or `-1` in `t_j` adds exactly `sign(e)(u,v)`.

Before removing exceptional edges, the `s` residue classes of the consecutive determinant interval form at most `s` chains. Deleting at most `E` edges creates at most one additional component per deletion, so the whole branch decomposes into at most

`s+E`

constant-step runs.

`VIS-327` is the special case `E=1` supplied by a Farey parent. The present observation keeps the approximation error `E` explicit and trades a few more exceptional edges for a potentially much shorter decimation length.

## 2. Exact step formula and degeneracy boundary

From `e=d s-p k`,

`p=(d s-e)/k`.

The orientation-dependent definitions of `d` in `VIS-325` satisfy the two exact identities

`u d-b k=sigma`,

`v d-a k=sigma`.

Therefore

`g_1=u p-b s=(sigma s-u e)/k`,

`g_2=v p-a s=(sigma s-v e)/k`.

Subtracting gives

`g_2-g_1=-sigma e`.

Also `m/k<J+1` and `s/k<1`, hence

`max(|g_1|,|g_2|) <= 1+E(J+1)`.

Suppose one coordinate vanishes. If `g_1=0`, then `sigma s=u e`; if `g_2=0`, then `sigma s=v e`. Since `0<s<k<m`, the larger center coordinate cannot occur on the right-hand side. Thus a zero coordinate is possible only through the smaller coordinate `n`, with

`s=n r`, `e=sigma r`, `r>=1`.

Such a vector exists with `s<k` only when `n<k`, equivalently `m>2n`, equivalently `J=1`. This recovers the axis-parent phenomenon of `VIS-326` but shows that it is one thin lattice ray, not an unavoidable feature of the fragmented branch.

## 3. Resultants stay at the decimation scale

Fix one constant-step component and its first point

`P_j(h_0)=(Q_0,R_0)`.

The unimodular map

`(t,h) -> (u t-b h, v t-a h)`

has determinant `-1`, while `G` is the image of `(p,s)`. Hence

`Delta=det(P_j(h_0),G)`
` =p h_0-s t_j(h_0)`.

Write

`t_j(h_0)=A+d h_0/k-theta-j`, `theta={A+d h_0/k}`.

Using `p=d s/k-e/k` gives

`Delta=-e h_0/k-s A+s(theta+j)`.

The fragmented condition `L<k` implies `|h_0|<k/2`. The same-shell bounds give `1<=A<4`, while `0<=theta+j<3`. Therefore

`|Delta|<E/2+4s`.

This is the same conductor collapse as `VIS-327`, now with a controlled Diophantine error `E` rather than exact Farey error one.

## 4. Sieve cost for many affine pieces

Assume `g_1 g_2 !=0`. Along a constant-step component of `r` vertices the two prime candidates are affine forms

`Q(a)=Q_0+a g_1`,

`R(a)=R_0+a g_2`.

For a prime `ell` not dividing

`g_1 g_2 Delta`,

the two forms have exactly two distinct roots modulo `ell`. All departures from this generic dimension-two local factor are therefore supported on primes dividing that conductor. After fixed-divisor components are separated, the worst correction is bounded by

`prod_(ell|g_1 g_2 Delta, ell>2) (1-2/ell)^(-1)`

and the standard Mertens estimate gives the crude but sufficient bound

`<< (1+log log(3+|g_1 g_2 Delta|))^2`.

Using Sections 2--3 gives the displayed `Omega_(s,e)`.

The classical Selberg upper-bound sieve therefore gives, uniformly in the translating offsets,

`#prime-pairs on a run of length r`
` << Omega_(s,e) r/log^2(3+r)+1`.

If `Delta=0`, the two affine forms are proportional to the same primitive direction after removing their common step content. Since `e!=0` gives `g_1!=g_2`, simultaneous primality then occurs only for `O(1)` parameter values; fixed-divisor components are equally harmless for an upper bound.

It remains only to sum over at most

`F=s+E`

components whose total length is at most `L`. The elementary dyadic grouping inequality

`sum_i r_i/log^2(3+r_i)`
` << L/log^2(3+L/F)+F`

holds for positive `r_i` with `sum_i r_i<=L` and at most `F` terms: group the `r_i` by dyadic size relative to `L/F`; the large-size bins retain the logarithm of `L/F`, while the geometrically shrinking small bins are absorbed by the main term and the final `O(F)` tail.

Combining these estimates proves

`P_j << Omega_(s,e) [ L/log^2(3+L/F)+F ]`.

## 5. Minkowski supplies a square-root packet for every slope

Consider

`Lambda_(d,k)={(s,e) in Z^2 : e-d s in k Z}`.

The vectors `(1,d)` and `(0,k)` form a basis, so

`det Lambda_(d,k)=k`.

The symmetric convex square

`B={ (s,e): |s|<=2 sqrt(k), |e|<=2 sqrt(k) }`

has area `16k`, strictly larger than the `4 det Lambda` threshold in dimension two. Minkowski's convex-body theorem therefore supplies a nonzero lattice point `(s,e)` in `B`.

For `k>4`, `|s|,|e|<k`. If `s=0`, the lattice congruence forces `k|e`, hence `e=0`; if `e=0`, `gcd(d,k)=1` forces `k|s`, hence `s=0`. Both contradict nonzeroness. After replacing the vector by its negative if necessary,

`1<=s<=2 sqrt(k)`, `1<=E<=2 sqrt(k)`.

This is standard geometry of numbers. Minkowski's theorem in the needed determinant form is recorded in the *Encyclopedia of Mathematics*, “Minkowski theorem”; see also J. W. S. Cassels, *An Introduction to the Geometry of Numbers*, Springer, Classics in Mathematics, DOI `10.1007/978-3-642-62035-5`. No novelty is claimed for the lattice approximation itself.

## 6. Natural Wang scale closes the fragmented range

Let

`ell=log log(3M)`

and specialize to

`L asymp M/ell`, `L<k`.

Since both center coordinates lie in `(M/2,2M]`, one has `k=O(M)`. The Minkowski vector therefore satisfies

`F=s+E=O(sqrt(M))=o(L)`

and

`log(3+L/F) >> log M`.

Furthermore `k>L` and `m<=2M` imply

`J=floor(m/k)=O(ell)`.

Hence Sections 2--3 give a polynomial-size conductor with

`Omega_(s,e)=O(ell^2)`.

The coordinate-degenerate ray from Section 2 has `s>=n>M/2`, whereas the Minkowski vector has `s=O(sqrt(M))`; for sufficiently large `M` the chosen step is therefore nondegenerate for every center, including `J=1`.

The sieve estimate becomes

`P_j << ell^2 [ L/log^2 M + sqrt(M) ]`
` << L ell^2/log^2 M`.

There are at most three frozen Wang branches. `VIS-321` and `VIS-325` show that the actual branch differs from this renormalized fixed-gate model at only `O(1)` determinant indices in the present regime, so the same scale holds for the actual fragmented cell.

In the notation of `VIS-315`--`VIS-316`, its excess over the natural two-prime cell scale is therefore at most

`A_M=O(ell^2)`.

The taper criterion depends on `sqrt(A_M)`, so this contributes only `O(ell)`, strictly below the allowed `o(ell^(3/2))` scale. The first-parent obstruction identified in `VIS-327` was therefore representation-specific: even when both Christoffel parents are almost as long as the full denominator, the determinant-`k` approximation lattice always contains a square-root-scale nondegenerate packet sufficient for the upper-bound sieve.

## Prior-art and novelty boundary

Minkowski's convex-body theorem and the associated short-vector/Diophantine-approximation principle are classical geometry of numbers. The exact statement used here is the standard dimension-two volume-versus-covolume theorem; Cassels is a canonical reference.

The dimension-two Selberg upper-bound sieve for two affine forms is also classical. `VIS-324` already anchors it to Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, Chapter 6, and John Friedlander and Henryk Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57, Chapters 7--8.

The Mathia-specific content is only the composition of these classical tools with the exact Wang representation: the approximation error `e=d s-pk` counts the exceptional branch edges, the same `(s,e)` controls the affine step and resultant, the axis-degenerate locus is an explicit long ray, and a Minkowski short vector is automatically outside that ray at the natural same-shell scale. This composition closes a previously isolated parameter regime but is not presented as a new general theorem in geometry of numbers or sieve theory.

## Boundaries and falsification

The proof uses the maximally fragmented condition `L<k`. When `L>=k`, sampled phases repeat and the `O(E)` exceptional-edge argument must be reformulated over several denominator periods; `VIS-324` covers polynomially long first-level runs but leaves a near-maximal transition where `L/k=M^(o(1))`.

The result is an upper bound for simultaneous-prime occupancy, not an asymptotic and not cancellation of Wang coefficients. It closes this regime only because `VIS-316` requires a taper-weighted upper-bound excess, not a prime-pair asymptotic in every cell.

The square-root constant `2` is deliberately inessential. Any fixed convex-body constant producing `s,E=O(sqrt(k))` gives the same conclusion.

Falsify the exact result by exhibiting an admissible `L<k` branch for which the arbitrary-decimation anomaly count exceeds `E`, the displayed step formula or resultant identity fails, the claimed axis-degenerate classification has another solution, the approximation lattice has determinant different from `k`, or the Selberg recombination fails after all local bad primes are charged to `g_1 g_2 Delta`.

## Dependencies

- `VIS-316`: taper-weighted shell-occupancy destination.
- `VIS-321`: fixed-gate branch reduction and bounded moving-gate error.
- `VIS-324`: Selberg closure of polynomially long first-level runs and the remaining near-maximal transition.
- `VIS-325`: denominator-`k` mechanical renormalization in the fragmented regime.
- `VIS-326`: first Christoffel parent monodromies and the `J=1` axis degeneracy.
- `VIS-327`: exact first-parent decimation, resultant control, and the first-parent near-full-scale frontier.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the Wang natural-window occupancy problem.

## Research consequence

Do not spend further effort descending the continued-fraction hierarchy merely to create repetition inside `k>L`. A geometry-of-numbers short vector already supplies enough repeated two-dimensional affine structure to put every maximally fragmented cell below the `VIS-316` taper allowance.

The next independent branchwise question is the transition that this proof deliberately does not touch:

`k<=L`, `k=M^(1-o(1))`.

There the first-level runs are only subpolynomially long, but the observation window spans one or more complete denominator-`k` periods, so the one-period short-vector argument above cannot simply be reused. Determining whether period aggregation, a multi-period Diophantine decimation, or a coefficient-weighted energy estimate closes that transition is a new research thread and is intentionally left for a later invocation.
