# VIS-327 — Christoffel-parent decimation turns visible repetition into small-conductor affine runs

## Claim

Keep the denominator-`k` Wang branch of `VIS-325`--`VIS-326`. Thus

`gcd(u,v)=1`, `u != v`,

`m=max(u,v)`, `k=|u-v|`, `sigma=sign(v-u)`,

`L=2 floor(D)+1 < k`,

and for one frozen branch

`t_j(h)=floor(A+d h/k)-j`, `j in {0,1,2}`,

`P_j(h)=(u t_j(h)-b h, v t_j(h)-a h)`,

on the `L` consecutive determinant indices `|h|<=floor(D)`, with `A=2M/m` and `au-bv=1` as before.

Take either of the two Farey/Christoffel parents from `VIS-326`. Write its one-step count and block length as `(p,s)`, so

`d s-p k=epsilon`, `epsilon in {+1,-1}`,

and define its Wang monodromy

`G=(g_1,g_2)=(u p-b s, v p-a s)`.

Then the parent length `s`, rather than the full denominator `k`, gives an exact second decimation of the observed branch.

1. For every `h` for which both `h` and `h+s` lie in the observation interval,

   `P_j(h+s)-P_j(h)=G`

   except at at most one value of `h`. At that exceptional edge the displacement is `G+epsilon(u,v)`.

2. If `s<L`, decimating the `L` observed indices by residue modulo `s` decomposes the entire branch into at most `s+1` affine runs with constant step `G`. Before the unique possible exceptional split, each residue chain has either

   `floor(L/s)` or `ceil(L/s)`

   vertices. Thus the visible copy-index scale of this parent is exactly `L/s`, up to one split chain.

3. On every constant-step run, let `(Q_0,R_0)=P_j(h_0)` be its first point and define the two-form resultant

   `Delta=Q_0 g_2-R_0 g_1`.

   Then

   `Delta=p h_0-s t_j(h_0)`

   and, uniformly for all three frozen branches,

   `|Delta|<=4s`.

   Hence first-parent renormalization controls not only the step vector but also the arithmetic conductor of the affine prime-pair run: the resultant is of the same order as the parent length, not of order `M`.

4. Suppose the chosen parent is nondegenerate, meaning `g_1 g_2 !=0`. `VIS-326` shows this for both parents when `J=floor(m/k)>=2`, and for the complementary parent when `J=1`. Since `g_1,g_2` are consecutive integers, they are primitive. For a run with `Delta !=0`, the standard dimension-two Selberg upper-bound sieve has only the usual local correction from primes dividing

   `g_1 g_2 Delta`.

   Its singular factor is

   `<< log log(3+|g_1 g_2 Delta|)`.

   If `Delta=0`, primitivity makes the two forms proportional to one primitive integer vector, and the run contains at most `O(1)` simultaneous prime points; this degenerate case is therefore harmless for an upper bound.

Consequently, for any nondegenerate parent with `s<L`, the simultaneous-prime count `P_j` on one frozen branch satisfies

`P_j << Lambda_s [ L/log^2(3+L/s) + s ]`,

where

`Lambda_s = 1 + log log(3+4s(J+1)^2)`.

At the natural Wang scale

`L asymp M/log log M`, `k>L`, `J<<log log M`,

if some nondegenerate first parent has

`s<=M^(1-delta)`

for a fixed `delta>0`, then

`P_j <<_delta [L log log M]/log^2 M`.

Relative to the natural two-prime cell scale `L/log^2 M`, such a center has excess factor only

`A=O_delta(log log M)`.

This is comfortably below the `VIS-316` taper-weighted allowance: `sqrt(A)=O(sqrt(log log M))`, whereas the destination permits aggregate growth up to `o((log log M)^(3/2))`.

Therefore a first-parent obstruction that can still threaten the Wang natural-window route must avoid every polynomially short **nondegenerate** parent. In particular:

- when `J>=2`, both parents are nondegenerate, so any unresolved center must have

  `min(q,k-q)=M^(1-o(1))`;

- when `J=1`, the externally selected parent of length `q` is axis-degenerate, so only the complementary length `k-q` closes by this two-form argument. A short axis parent alone does not recover sieve dimension two.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-SELBERG-SIEVE + CONTINUED-FRACTION-RANGE-CLOSURE + NO-NOVELTY-CLAIM`.

No prime-pair asymptotic, lower bound, new Selberg-sieve theorem, full continued-fraction iteration theorem, Wang natural-window theorem, or stronger RH criterion is claimed.

## 1. A parent-length block has only one possible anomalous displacement

For a parent `(p,s)` one has

`d s/k = p + epsilon/k`, `epsilon in {+1,-1}`.

Put

`x_h=A+d h/k`.

Then

`t_j(h+s)-t_j(h)`
` = floor(x_h+p+epsilon/k)-floor(x_h)`.

If `epsilon=+1`, this equals `p+1` only when

`{x_h}>=1-1/k`,

and otherwise equals `p`.

If `epsilon=-1`, it equals `p-1` only when

`{x_h}<1/k`,

and otherwise equals `p`.

Because `gcd(d,k)=1`, the phases `{x_h}` for fewer than `k` consecutive determinant indices are distinct points of one translated `1/k` grid. The eligible starts `h` with `h,h+s` in the observation interval form fewer than `k` consecutive indices because `L<k`. Hence at most one eligible start lies in the exceptional boundary cell of width `1/k`.

For every nonexceptional start,

`P_j(h+s)-P_j(h)`
` =(u p-b s, v p-a s)`
` =G`.

At the exceptional start the extra change of `epsilon` in `t_j` adds exactly `epsilon(u,v)`, giving

`G+epsilon(u,v)`.

Thus the first-parent block is not merely a symbolic factorization. Away from one edge, it is an exact affine translation of the Wang prime-coordinate pair.

## 2. Residue classes modulo the parent length quantify visible repetition

Assume `s<L`. Partition the `L` consecutive determinant indices by their residue modulo `s`.

Without the exceptional edge, every residue class is an affine run under repeated addition of `G`. Since the interval has length `L`, every class contains either

`floor(L/s)` or `ceil(L/s)`

vertices.

The single exceptional `s`-edge can split at most one residue chain into two pieces. Therefore the whole frozen branch is partitioned into at most

`s+1`

constant-step affine runs, and the two pieces created by a split have combined length at most `ceil(L/s)`.

This gives the exact finite-window meaning of “parent repetition.” A parent is useful for copy-index sieving precisely when its block length is shorter than the observed determinant window. Its available repetition count is `asymp L/s`; the full denominator `k` no longer controls that repetition once the Christoffel parent is exposed.

If `s>=L`, this first-parent decimation contains no repeated `s`-edge inside the window and therefore supplies no copy-index gain. One must use the other parent, descend further in the continued-fraction hierarchy, or change to a discrepancy/energy representation.

## 3. The two-form resultant is exactly `p h-s t`

Fix one constant-step run and a point

`P_j(h_0)=(Q_0,R_0)`.

The Bézout coordinate map is

`(t,h) -> (u t-b h, v t-a h)`.

Its matrix

`[[u,-b],[v,-a]]`

has determinant `-1` because `au-bv=1`.

The parent step `G` is the image of `(p,s)` under the same unimodular map. Therefore

`Delta`
` =det(P_j(h_0),G)`
` =-det((t_j(h_0),h_0),(p,s))`
` =p h_0-s t_j(h_0)`.

This identity is exact and is independent of the large center coordinates once the parent data are fixed.

Now write

`t_j(h_0)=A+d h_0/k-theta-j`, `theta={A+d h_0/k}`.

Since

`p-s d/k=-epsilon/k`,

one obtains

`Delta`
` =-epsilon h_0/k-sA+s(theta+j)`.

The maximally fragmented condition `L<k` gives

`|h_0|<=floor(D)<k/2`.

Also the shell bounds `M/2<m<=2M` give

`1<=A=2M/m<4`,

while `0<=theta<1` and `j in {0,1,2}` imply

`0<=theta+j<3`.

Hence

`|Delta|<4s+1/2`.

Since `Delta` is an integer,

`|Delta|<=4s`.

The apparent large-coordinate conductor therefore collapses to the parent scale under the same unimodular representation that produced the small monodromy.

## 4. Local sieve factors depend only logarithmically on the small conductor

Assume `g_1 g_2 !=0`. `VIS-326` gives consecutive coordinates for every first-parent monodromy, so

`gcd(g_1,g_2)=1`.

Along one affine run the two candidate prime coordinates are

`Q(n)=Q_0+n g_1`,

`R(n)=R_0+n g_2`.

For a prime `ell` not dividing

`C=g_1 g_2 Delta`,

the two forms have two distinct roots modulo `ell`. If `ell|Delta` while `ell` divides neither step coefficient, the two roots coincide. If `ell` divides one step coefficient, primitivity prevents it from dividing the other; unless that form has a fixed divisor, the other form contributes the single root. A fixed-divisor run contributes only `O(1)` simultaneous prime points and can be separated.

Thus, apart from the fixed small-prime normalization, the deviation from the generic dimension-two local factor is supported only on primes dividing `C`, with correction bounded by the classical product

`prod_(ell|C, ell>2) (ell-1)/(ell-2)`.

The ordinary Mertens estimate gives

`prod_(ell|C, ell>2) (ell-1)/(ell-2) << log log(3+|C|)`.

`VIS-326` also gives

`|g_1|,|g_2|<=J+1`.

Combining this with `|Delta|<=4s` yields

`|C|<=4s(J+1)^2`,

which gives the stated factor `Lambda_s`.

If `Delta=0`, then `(Q_0,R_0)` is an integer multiple of the primitive vector `(g_1,g_2)`. Along the run both forms are the same scalar parameter times the fixed primitive coordinates. Since the nondegenerate first-parent vectors in `VIS-326` have consecutive nonzero coordinates, at least one absolute coordinate exceeds one. Simultaneous primality can then occur for at most an absolute number of parameter values. Such a run is therefore no worse than the additive sieve remainder.

## 5. Summing the parent runs

Apply the standard dimension-two Selberg upper-bound sieve to every nondegenerate constant-step run. A run of `r` vertices contributes

`<< Lambda_s r/log^2(3+r) + 1`.

All unsplit residue chains have length `floor(L/s)` or `ceil(L/s)`. Their main terms sum to

`<< Lambda_s L/log^2(3+L/s)`.

The one possibly split chain is handled exactly as in `VIS-324`: if its two pieces have lengths `r_1,r_2` with

`r_1+r_2<=ceil(L/s)`,

then

`r_1/log^2(3+r_1)+r_2/log^2(3+r_2)`
` << [L/s]/log^2(3+L/s)+1`.

There are at most `s+1` runs, so the accumulated sieve remainders and the possible resultant-zero/fixed-divisor exceptions are absorbed by

`<< Lambda_s s`.

Therefore

`P_j << Lambda_s [ L/log^2(3+L/s) + s ]`.

This estimate uses the actual parent repetition visible in the finite Wang window; it does not invoke full-period equidistribution of the denominator-`k` mechanical word.

## 6. Polynomially short nondegenerate parents are already sufficient

Specialize to the natural central-shell regime

`L asymp M/ell`, `ell=log log(3M)`.

Because `k>L` and `m<=2M`, `VIS-326` gives

`J=floor(m/k)<<ell`.

Assume a nondegenerate parent has

`s<=M^(1-delta)`

for fixed `delta>0`.

Then

`L/s >> M^delta/ell`,

so

`log(3+L/s)>>_delta log M`.

Also

`Lambda_s << log log M=ell`.

The additive term is negligible on the same scale:

`s ell / (L ell/log^2 M)`
` << M^(-delta) ell log^2 M`
` =o_delta(1)`.

Hence

`P_j <<_delta L ell/log^2 M`.

The `VIS-315`--`VIS-316` natural cell baseline is `L/log^2 M`. Therefore these centers have at most `A=O_delta(ell)` excess. This is much smaller than the aggregate allowance that would become critical only around `A` of order `ell^3`.

For `J>=2`, both first parents are nondegenerate. Choosing the shorter one shows that every center with

`min(q,k-q)<=M^(1-delta)`

is already closed at this first-parent level up to the harmless `O(ell)` local-factor excess.

Thus a surviving `J>=2` center must satisfy

`min(q,k-q)=M^(1-o(1))`.

Equivalently, neither first-parent denominator supplies a polynomially long copy-index run. This is the genuinely nonrepetitive first-Christoffel regime.

For `J=1`, the selected parent is axis-degenerate by `VIS-326`, while the complementary parent is nondegenerate. The same argument closes the center whenever

`k-q<=M^(1-delta)`.

If only the axis parent is short, this theorem deliberately does not claim a two-prime saving; one must use offset averaging, a later continued-fraction level, or another representation.

## Prior-art and novelty boundary

The rational mechanical/Christoffel parent factorization is classical and already anchored in `VIS-325`--`VIS-326` through Jean-Pierre Borel and Christophe Reutenauer, **On Christoffel classes**, *RAIRO - Theoretical Informatics and Applications* 40:1 (2006), 15--27, DOI `10.1051/ita:2005038`, and Jean Berstel, Aaron Lauve, Christophe Reutenauer, Franco Saliola, **Combinatorics on Words: Christoffel Words and Repetitions in Words**, CRM Monograph Series 27, American Mathematical Society, DOI `10.1090/crmm/027`.

The dimension-two upper-bound sieve is classical and already anchored in `VIS-324` through Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, Chapter 6, and John Friedlander and Henryk Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57, Chapters 7--8. The Mertens-type control of finite products over bad primes is likewise standard.

No novelty is claimed for parent words, residue-class decimation, the Selberg sieve, or singular-series products in isolation. The Mathia-specific durable content is their exact specialization to the Wang branch: every first parent gives an `s`-step affine translation with only one exceptional edge, visible repetition is exactly priced by `L/s`, the affine resultant collapses to `p h-s t` with `|Delta|<=4s`, and polynomially short nondegenerate parents cannot generate the natural-window occupancy obstruction.

## Boundaries and falsification

The theorem concerns the denominator-`k` renormalized frozen branch. `VIS-325` already bounds the difference from the true moving Wang branch by `O(1)` determinant indices in the natural regime; those bounded corrections are beneath the leading constant already allowed by the occupancy criterion.

The parent-length decomposition is useful only when `s<L`. When `s>=L`, the observation window contains no repeated `s`-edge and the theorem gives no copy-index sieve gain.

The Selberg estimate is an upper bound, not a prime-pair asymptotic. It does not assert random prime behavior, lower density, cancellation of Wang phases, or independence between different parent runs.

The `O(log log M)` excess is acceptable relative to the `VIS-316` destination, but it is not the near-average `A=O(1)` density that a stronger theorem might prove.

For `J=1`, a short selected parent remains axis-degenerate. Its small block length does not by itself restore the second arithmetic dimension.

Falsify the exact structural claim by exhibiting an admissible `VIS-326` branch and parent `(p,s)` for which more than one eligible `s`-edge has non-parent displacement, residue decimation produces more than one exceptional split, the run resultant differs from `p h-s t`, or `|Delta|>4s`. Falsify the range closure by producing a nondegenerate polynomially short parent whose two-affine-form local sieve conductor is not supported on `g_1 g_2 Delta` or whose standard upper-bound sieve exceeds the displayed scale after the stated local factor is included.

## Dependencies

- `VIS-316`: taper-weighted shell-occupancy destination.
- `VIS-319`: unimodular Bézout coordinates preserving both prime exclusions.
- `VIS-324`: classical branchwise Selberg upper bound and polynomial run-length benchmark.
- `VIS-325`: denominator-`k` mechanical renormalization in the fully fragmented range.
- `VIS-326`: exact first-parent lengths and universal primitive monodromies.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining Wang occupancy frontier.

## Research consequence

The first continued-fraction step is now quantitatively priced. The useful parameter is not merely whether a Christoffel parent exists, but whether a **nondegenerate parent denominator `s` is shorter than the finite observation window and by how much**.

Polynomially short nondegenerate parents already provide enough repeated affine copies for a standard two-prime upper-bound sieve, even after paying the full small-conductor local factor. The remaining first-level frontier is therefore narrower:

- for `J>=2`, both parent lengths must be `M^(1-o(1))`;
- for `J=1`, the nondegenerate complementary parent must be `M^(1-o(1))`, while a short selected axis parent requires a different arithmetic-dimension recovery.

The next independent question is what the **second** continued-fraction step or a deterministic discrepancy/energy representation does in this genuinely nonrepetitive first-parent regime. That is a new research thread and is intentionally not pursued here.