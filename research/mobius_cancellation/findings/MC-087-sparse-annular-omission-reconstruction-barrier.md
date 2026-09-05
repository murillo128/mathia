# MC-087 — Sparse omission from the exact sawtooth annulus remains Mertens-equivalent at target resolution

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The physical-space escape left open by `MC-086` can be narrowed beyond the source-natural initial reciprocal slabs. For the exact Huxley--Watt sawtooth annulus, **any** retained subset whose omitted pair support is already small enough to be restored by the boundedness of the sawtooth kernel remains quantitatively equivalent to the corresponding global Mertens bound once the source-prescribed coarse terms are kept.

Retain the notation of `MC-084`:

\[
M(N)=\sum_{n\le N}\mu(n),
\qquad
H(N)=\sum_{n\le N}\frac{\mu(n)}n,
\]

\[
z(x)=\left\lfloor x\right\rfloor+\frac12-x,
\qquad |z(x)|\le \frac12,
\]

and let

\[
\mathcal A_N:=\{(m,n):m,n\le N,\ mn>N\}
\tag{1}
\]

be the full product annulus. Write

\[
C_N:=N^2H(N)^2-\frac12M(N)^2,
\tag{2}
\]

\[
I_N:=
\sum_{\substack{m,n\le N\\mn\le N}}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right),
\qquad
I_N=O(N\log N),
\tag{3}
\]

and

\[
W_N:=
\sum_{(m,n)\in\mathcal A_N}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right).
\tag{4}
\]

For an **arbitrary** subset `E_N subseteq A_N`, interpreted as the omitted physical-space pairs, define

\[
T_N(E_N)
:=
\sum_{(m,n)\in E_N}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right),
\tag{5}
\]

\[
W_N^{\mathrm{ret}}(E_N)
:=W_N-T_N(E_N),
\tag{6}
\]

and the source-coupled retained statistic

\[
\boxed{
P_N(E_N):=C_N+W_N^{\mathrm{ret}}(E_N).
}
\tag{7}
\]

The exact scale-doubling identity from `MC-084` gives

\[
\boxed{
P_N(E_N)
=
2M(N)-M(N^2)-I_N-T_N(E_N).
}
\tag{8}
\]

while boundedness of the exact source kernel gives the support-only estimate

\[
\boxed{
|T_N(E_N)|\le \frac12\#E_N.
}
\tag{9}
\]

Consequently, fix `1/2<beta<1`. If the omitted support satisfies

\[
\#E_N=O(N^{2\beta}),
\tag{10}
\]

then

\[
\boxed{
P_N(E_N)=O(N^{2\beta})
\quad\Longleftrightarrow\quad
M(x)=O(x^\beta).
}
\tag{11}
\]

No geometric regularity, slab ordering, monotonicity, or source-natural initial-segment assumption on `E_N` is needed. Thus **selectivity by itself does not lower the information burden**. Any noninitial or irregular physical-space selection whose omitted pairs are already target-subordinate under the generic support bound (9) is still an approximate coordinate system for the doubled Mertens target.

Equivalently, if

\[
\#E_N=N^{\gamma+o(1)},
\tag{12}
\]

then support-only restoration of the omitted part cannot make a retained source-coupled statistic cheaper at a Mertens exponent `beta` unless

\[
\gamma\le 2\beta.
\tag{13}
\]

At the RH epsilon boundary, a family of omissions satisfying

\[
\#E_{N,\varepsilon}
=O_\varepsilon(N^{1+\varepsilon})
\tag{14}
\]

still leaves an RH-equivalent coupled target. Therefore a genuinely under-resolved physical-space route must discard **supercritical pair mass** and then control its signed contribution by arithmetic information stronger than the generic cardinality estimate, or avoid restoring that complement altogether through a different coupled recurrence.

This strictly generalizes the reconstruction logic behind the initial reciprocal-slab result `MC-086`. It does not subsume the Fourier result `MC-085`, because removing Fourier modes changes the weight on essentially every annular pair rather than deleting a subset of physical-space pairs.

## 1. Exact arbitrary-subset recovery identity

`MC-084` proves the exact full coupled identity

\[
C_N+W_N
=
2M(N)-M(N^2)-I_N.
\tag{15}
\]

For any `E_N subseteq A_N`, equations (5)--(7) give

\[
P_N(E_N)
=C_N+W_N-T_N(E_N).
\]

Substituting (15) yields (8) with no approximation. The omitted family can depend arbitrarily on `N`; it can be disconnected, noninitial in the reciprocal-floor coordinate, selected by arithmetic predicates, or chosen from multiple slab ranges. The only input used below is its cardinality.

Since `|mu(m)mu(n)|<=1` and `|z|<=1/2`, equation (9) follows immediately. In particular, no Möbius cancellation, zero-free region, divisor estimate, or distribution theorem is hidden in the complement bound.

This makes the information test independent of the geometry used to describe the subset. A selective slab family, a union of hyperbolic boxes, or an irregular source-measurable mask is not cheaper merely because it uses fewer physical coordinates; what matters under absolute restoration is the power scale of the omitted pair mass.

## 2. Fixed-exponent equivalence

Assume first that

\[
M(x)=O(x^\beta),
\qquad \beta>\frac12,
\tag{16}
\]

and that (10) holds. From (8),

\[
|P_N(E_N)|
\le
2|M(N)|+|M(N^2)|+|I_N|+|T_N(E_N)|.
\tag{17}
\]

The four terms are respectively

\[
O(N^\beta),
\quad O(N^{2\beta}),
\quad O(N\log N),
\quad O(N^{2\beta}),
\]

so

\[
P_N(E_N)=O(N^{2\beta}).
\tag{18}
\]

Conversely suppose

\[
P_N(E_N)=O(N^{2\beta})
\tag{19}
\]

and (10) holds, without assuming any prior Mertens power saving. Equation (8), the trivial bound `|M(N)|<=N`, (3), and (9) give

\[
M(N^2)=O(N^{2\beta}).
\tag{20}
\]

For arbitrary real `x`, put `N=floor(sqrt(x))`. Since each increment of `M` has absolute value at most one,

\[
|M(x)-M(N^2)|\le x-N^2\le 2N+1.
\tag{21}
\]

Because `beta>1/2`, equations (20)--(21) give `M(x)=O(x^beta)`. This proves (11).

The equivalence therefore does not arise from a special arrangement of the retained set. It follows from three facts only: the exact source-coupled scale-doubling identity, the cheap `O(N log N)` low-product interior, and target-subordinate absolute restoration of the omitted annular coordinates.

## 3. Support exponent as a reconstruction budget

Suppose the omitted support has power scale (12). The generic complement estimate is then

\[
T_N(E_N)=O(N^{\gamma+o(1)}).
\tag{22}
\]

After the square-scale interpolation in the reverse direction, this corresponds to a Mertens exponent floor

\[
\frac\gamma2.
\tag{23}
\]

Thus an omission with `gamma>1` cannot be ignored by cardinality alone at the RH boundary. To ask for exponent `beta`, the support-only restoration route requires `gamma<=2 beta`, which is exactly (13).

For the initial reciprocal slabs in `MC-086`, the omitted region is

\[
N<mn\le \frac{N^2}{K}.
\]

When `K=N^theta`, elementary hyperbola counting gives

\[
\#E_N\ll N^{2-\theta}(1+\log N),
\]

so `gamma=2-theta` up to logarithms. Condition (13) becomes

\[
\theta>2-2\beta
\]

when one asks for a strict power margin, reproducing the `MC-086` threshold. The earlier initial-slab calculation is therefore one geometric realization of the more general support-resolution budget.

The new consequence concerns **selective/noninitial physical-space masks**. If such a mask omits only target-subordinate pair mass, its apparent selectivity cannot be credited as information reduction: equation (11) recovers the same Mertens target. If it omits more pair mass, the route remains open only if it proves cancellation in that complement or obtains a recurrence that never needs to restore it by (9).

## 4. RH epsilon-family form

Let `E_{N,epsilon}` be any epsilon-dependent family of omitted annular subsets satisfying (14), and define `P_{N,epsilon}` by (7). If the RH-equivalent Mertens family holds, then (8), (3), (9), and (14) give

\[
P_{N,\varepsilon}
=O_\varepsilon(N^{1+\varepsilon})
\tag{24}
\]

after the usual harmless shrinking of the Mertens epsilon when needed.

Conversely, suppose (24) holds for every positive epsilon together with (14). Equation (8) gives

\[
M(N^2)=O_\varepsilon(N^{1+\varepsilon}).
\tag{25}
\]

Square interpolation then yields

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon/2}).
\tag{26}
\]

and reparameterizing epsilon gives the standard family

\[
M(x)=O_\delta(x^{1/2+\delta})
\quad\text{for every }\delta>0.
\tag{27}
\]

Hence a proper or highly irregular physical-space projection can discard `N^{1+o(1)}` annular coordinates and still carry the full RH-equivalent family once its omitted part is restored only by bounded-kernel cardinality.

## 5. Prior art and novelty boundary

The scale-doubling identity, the matrix decomposition, and the exact sawtooth kernel are prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function* (2018), recorded as `MC-S24`. The boundedness of the centered fractional-part function, pair counting, and interpolation between consecutive squares are elementary classical mechanisms.

A targeted literature check around the Huxley--Watt identity, its sawtooth residual, truncation, and subset/exponential-sum language recovered the source and adjacent classical exponential-sum work but did not provide a reason to assert a separate classical theorem for the arbitrary-subset statement above. **No novelty claim is made.**

The durable line-specific content is a no-go abstraction forced by `MC-084`--`MC-086`: the reconstruction barrier is not peculiar to initial reciprocal slabs. Every physical-space mask with target-subordinate omitted cardinality lies on the same side of the information boundary, regardless of how cleverly the retained coordinates are selected.

## 6. Boundaries and decisive continuation

This result does **not** show that every selective or noninitial projection is Mertens-equivalent. Its hypothesis is precisely that the omitted contribution is restored using only the generic support estimate (9) at or below the target scale.

In particular, it does not rule out:

- an omitted set with supercritical cardinality but strong Möbius cancellation proved from independently weaker arithmetic input;
- a selective mask whose retained and omitted pieces are estimated jointly before absolute values are taken;
- a weighted projection that changes coefficients rather than simply omitting physical-space pairs;
- a recurrence that produces a strict scale contraction without reconstructing the full Huxley--Watt coupled residual;
- Fourier-mode selection, which is governed by the distinct coefficient-space reconstruction audit in `MC-085`.

It also does not prove any nontrivial estimate for the retained statistic `W_N^{ret}` alone. The equivalence concerns the **source-coupled** object `C_N+W_N^{ret}`, because the coarse harmonic and Mertens-square terms cannot be separated cheaply at the critical scale by `MC-020`.

The decisive continuation for the accepted annular clue is therefore sharper. A physical-space survivor must deliberately cross the cardinality barrier: omit enough pair mass that support-only restoration is too expensive, then derive a signed estimate for that omitted mass, or construct a joint bilinear coupling whose scale-doubling recurrence closes without restoring it. A candidate that advertises a sparse or selective mask but ultimately pays `|T|<=#E/2` below the target scale is killed by (11).

## Consequence for the research line

`MC-083`--`MC-086` progressively closed constant weighting, complete exact sawtooth coupling, initial Fourier truncation at generic remainder resolution, and initial reciprocal-slab truncation at generic support resolution. `MC-087` removes the remaining dependence on **which** physical slabs or annular coordinates are retained whenever the omitted support is already cheap in absolute mass.

The viable physical-space frontier is no longer "find a better subset." It is: **find arithmetic cancellation in a deliberately information-losing complement, or find a genuinely joint coupling that never reconstructs that complement by a generic bound.**