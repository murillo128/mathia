# MC-085 — A source-resolved proper Fourier annulus remains Mertens-equivalent once its truncation error is small enough

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The proper finite Fourier family left open by `MC-084` does not become an independently weaker source-coupled target merely because fewer than `N` reciprocal modes are retained.

Keep the Huxley--Watt notation

\[
M(N)=\sum_{n\le N}\mu(n),
\qquad
H_1(N)=\sum_{n\le N}\frac{\mu(n)}n,
\]

and write the coarse term

\[
C_N:=N^2H_1(N)^2-\frac12M(N)^2.
\tag{1}
\]

For a Fourier cutoff `K`, let

\[
\mathcal F_K(N)
:=
\sum_{1\le h\le K}\frac{Q_h(N)}{\pi h},
\tag{2}
\]

with

\[
Q_h(N)
=
\sum_{m,n\le N}\mu(m)\mu(n)
\sin\!\left(\frac{2\pi hN^2}{mn}\right),
\tag{3}
\]

and split the retained Fourier aggregate at the product hyperbola as in `MC-032`:

\[
\mathcal F_K
=
\mathcal F_K^{\rm int}+\mathcal F_K^{\rm ann},
\qquad
mn\le N\ \text{or}\ mn>N.
\tag{4}
\]

Huxley and Watt's source truncation gives

\[
\mathbf m^{\rm T}Z\mathbf m
=
\mathcal F_K(N)+E_{N,K},
\qquad
E_{N,K}
=O\!\left(
\frac{N^2(\log N)^2\log K}{K}
\right),
\tag{5}
\]

while `MC-032` proves uniformly in `K`

\[
\mathcal F_K^{\rm int}(N)=O(N\log N).
\tag{6}
\]

Define the **proper low-frequency annular coupling**

\[
\boxed{
P_{N,K}
:=
C_N+\mathcal F_K^{\rm ann}(N).
}
\tag{7}
\]

Combining the exact Huxley--Watt scale-doubling identity with (4)--(6) gives

\[
\boxed{
P_{N,K}
=
2M(N)-M(N^2)
-\mathcal F_K^{\rm int}(N)
-E_{N,K}.
}
\tag{8}
\]

Thus, once `K` is large enough that the **published generic truncation error** lies below a proposed Mertens power scale, the proper Fourier coupling is already quantitatively equivalent to that Mertens scale.

More precisely, fix `beta>1/2` and choose

\[
K=N^\theta,
\qquad
\theta>2-2\beta.
\tag{9}
\]

Then

\[
E_{N,K}=o(N^{2\beta}),
\qquad
\mathcal F_K^{\rm int}=o(N^{2\beta}),
\tag{10}
\]

and

\[
\boxed{
P_{N,K}=O(N^{2\beta})
\quad\Longleftrightarrow\quad
M(x)=O(x^\beta).
}
\tag{11}
\]

The reverse implication uses no prior power saving: `|M(N)|<=N`, (6), (10), and the `O(N)` gaps between consecutive squares suffice to recover the global bound from square arguments.

The RH epsilon-family survives the same **proper** truncation. For every fixed `epsilon>0`, take

\[
K_\varepsilon(N)=\left\lfloor N^{1-\varepsilon/2}\right\rfloor.
\tag{12}
\]

Then `K_epsilon(N)<N` for large `N`, but

\[
P_{N,K_\varepsilon(N)}
=O_\varepsilon(N^{1+\varepsilon})
\quad\text{for every }\varepsilon>0
\tag{13}
\]

is equivalent, after the harmless reparameterization of epsilon in the reverse direction, to

\[
M(x)=O_\delta(x^{1/2+\delta})
\quad\text{for every }\delta>0.
\tag{14}
\]

So **properness of the initial Fourier family is not enough to make the coupled estimate cheaper**. If the standard Huxley--Watt remainder is the mechanism used to discard the omitted frequencies, then retaining exactly enough low modes to place that remainder below the desired scale produces an approximate coordinate system for the same Mertens target.

This closes the most direct finite-Fourier escape left by `MC-084`. It does not show that the annular Fourier aggregate `\mathcal F_K^{\rm ann}` alone is Mertens-equivalent, nor does it rule out a theorem giving a substantially sharper arithmetic estimate for the omitted high-frequency complement. A viable Fourier route must obtain new information from the split itself, not merely truncate the source expansion at the resolution needed to reconstruct the full residual.

## 1. Exact recovery identity for the partial annular coupling

For `g=1`, the exact Huxley--Watt identity used throughout this line is

\[
M(N^2)
=
2M(N)-C_N-\mathbf m^{\rm T}Z\mathbf m.
\tag{15}
\]

Insert (5) and then (4):

\[
M(N^2)
=
2M(N)-C_N
-\mathcal F_K^{\rm int}
-\mathcal F_K^{\rm ann}
-E_{N,K}.
\tag{16}
\]

Rearranging gives (8) exactly, with the only uncertainty being the source remainder already bounded in (5).

This is the key difference from merely observing that a finite Fourier sum approximates the sawtooth kernel. The object in (7) keeps the **coarse source counterterms plus only the annular low modes**, so it is the natural strict-partial candidate relevant to the coupled-residual escape. Equation (8) shows how much of the next Mertens value it already carries after the cheap interior and controlled Fourier tail are restored.

## 2. Fixed-exponent resolution threshold

Let `K=N^theta`. From (5),

\[
E_{N,K}
=O\!\left(
N^{2-\theta}(\log N)^3
\right)
\tag{17}
\]

for fixed positive `theta`. If (9) holds, then

\[
2-\theta<2\beta,
\]

so (17) is `o(N^(2 beta))`. Equation (6) is also `o(N^(2 beta))` because `2 beta>1`.

Assume first `M(x)=O(x^beta)`. Equation (8) gives

\[
P_{N,K}
=
O(N^\beta)+O(N^{2\beta})+o(N^{2\beta})
=
O(N^{2\beta}).
\tag{18}
\]

Conversely assume

\[
P_{N,K}=O(N^{2\beta}).
\tag{19}
\]

Using (8), `|M(N)|<=N`, (6), and (10),

\[
M(N^2)=O(N^{2\beta}).
\tag{20}
\]

For arbitrary real `x`, put `N=floor(sqrt(x))`. Since each increment of `M` has absolute value at most one,

\[
|M(x)-M(N^2)|\le x-N^2\le 2N+1.
\tag{21}
\]

Because `beta>1/2`, (20)--(21) imply `M(x)=O(x^beta)`. This proves (11).

The threshold has a useful interpretation. Even if one somehow proved an extremely small bound for `P_{N,N^theta}`, the **generic source tail alone** has scale `N^(2-theta+o(1))`; after square interpolation this corresponds to the Mertens exponent

\[
1-\frac\theta2.
\tag{22}
\]

Thus a fixed compression exponent `theta<1` leaves a fixed gap `(1-theta)/2` above the critical exponent unless additional arithmetic information improves the omitted Fourier tail. This is the reverse-recovery form of the resolution budget first quantified in `MC-031`.

## 3. The RH epsilon-family can use proper cutoffs and still be equivalent

Take the cutoff (12). The source error is

\[
E_{N,K_\varepsilon}
=O\!\left(
N^{1+\varepsilon/2}\operatorname{polylog}N
\right)
=O_\varepsilon(N^{1+\varepsilon}).
\tag{23}
\]

and (6) has the same target bound. If the RH-equivalent Mertens family holds, use it at exponent `1/2+epsilon/2` in (8) to obtain (13).

Conversely suppose (13) holds for every fixed positive `epsilon`. Then (8), (6), (23), and `|M(N)|<=N` give

\[
M(N^2)=O_\varepsilon(N^{1+\varepsilon}).
\tag{24}
\]

Square interpolation yields

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon/2}).
\tag{25}
\]

Given any target `delta>0`, apply (25) with `epsilon=2delta`. This gives (14).

Hence the fact that every fixed epsilon permits a genuinely sublinear polynomial cutoff does not weaken the whole RH-equivalent family. The cutoff exponent itself moves toward one as the requested Mertens exponent moves toward one half, exactly compensating the apparent Fourier compression.

## 4. What remains genuinely open

The negative conclusion is deliberately narrower than a no-go for Fourier methods.

First, `\mathcal F_K^{\rm ann}` **without** the coarse term `C_N` is not classified by (11). A theorem for that standalone signed statistic could still be informative, but to yield a scale-doubling gain it must explain how its interaction with `C_N` is controlled without separately assuming target-strength information.

Second, (11) uses the published generic tail (5). A genuinely arithmetic theorem for the omitted high modes could make a much smaller cutoff sufficient. Such a result would be new input; it cannot be credited to Fourier truncation itself.

Third, the result treats the source-natural initial family `1<=h<=K`. A selective noninitial mode family, a proper reciprocal slab family, or another source-forced projection is outside the theorem unless its complement is controlled by a comparable recovery identity.

Finally, direct cancellation between retained and omitted modes could evade the positive-error bookkeeping only if proved before triangle inequalities are applied. Merely noting that the tail is signed does not supply such a theorem.

Accordingly, the finite-Fourier branch survives only if it can do at least one of the following: prove a stronger arithmetic high-frequency tail, identify a strict selective projection with an independently cheaper complement, or derive a direct signed relation that does not use the standard truncation error as the bridge back to the full Huxley--Watt residual.

## 5. Prior art and novelty boundary

The exact scale-doubling identity, sawtooth matrix `Z`, Fourier modes `Q_h(N)`, and truncation estimate (5) are from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20--34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`; see `MC-S24`. The primary paper explicitly discusses Fourier approximation of the residual. `MC-031` records its epsilon-dependent resolution budget, and `MC-032` proves the uniform `O(N log N)` bound for the low-product part of the retained aggregate.

The passage from square-scale bounds to all `x`, the power comparison in (17), and the epsilon reparameterization are elementary. A targeted literature check around the Huxley--Watt paper, its Fourier treatment, and later references found the published source and adjacent exponential-sum work, but did not provide a basis for claiming a new classical theorem here. **No novelty claim is made.**

The durable line-specific result is the reverse-recovery audit required by the current accepted clue: once the source truncation error is made subordinate to a proposed cancellation scale, the proper low-frequency annular coupling plus the exact coarse terms is already equivalent to the corresponding Mertens bound. The Fourier family is therefore a representation split, not by itself a weaker proof obligation.

## Consequence for the research line

`MC-083` killed the constant annular weight, and `MC-084` showed that the fully recombined exact sawtooth coupling recovers the doubled Mertens target. The present result fills the natural interval between them for the **source-resolved initial Fourier truncation**: keeping a proper low-frequency family does not escape target equivalence when the omitted frequencies are disposed of only through the standard Huxley--Watt remainder.

The active annular clue is therefore narrower. A future Fourier candidate must justify why its omitted information is cheaper than the source-generic tail or why a selective projection has an independent arithmetic estimate that yields a strict net gain after recombination and scale coverage. Simply choosing `K<N` and calling the retained family partial is no longer a viable mechanism.