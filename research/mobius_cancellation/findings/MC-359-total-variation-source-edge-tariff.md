# MC-359 — Total variation gives a bounded source-edge tariff for reciprocal dephasing

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-350` turns the global transcript-information floor into an extensive **exact** source cut: neighboring source states whose transcript laws are unequal must occupy different quotient cells. `MC-351`--`MC-353` then replace row inequality by KL/Jeffreys separation, but that currency becomes infinite at the deterministic/singular endpoint. There is a useful bounded interpolation between those two regimes.

Continue the even-rank reciprocal endpoint notation

\[
n=2^R,
\qquad
m=n-1,
\qquad
S=\{-1,+1\}^R\setminus\{(+1,\ldots,+1)\},
\]

with `X` uniform on `S`. Let `Y` be the complete admitted transcript and

\[
P_x:=\operatorname{Law}(Y\mid X=x).
\]

For every surviving Hamming edge `e={x,x'}` of the punctured cube define

\[
t_e:=\operatorname{TV}(P_x,P_{x'})\in[0,1]
\]

and the normalized total-variation edge budget

\[
\mathfrak T_1
:=
\frac{2}{m}\sum_{e\in E(S)} t_e.
\tag{1}
\]

Then

\[
\boxed{
I(X;Y)
\le
(\log2)\,\mathfrak T_1
+
\frac{2(R-1)\log2}{m}.
}
\tag{2}
\]

Combining `(2)` with the independently derived transcript-capacity lower bound `MC-340` gives an extensive **bounded** source-edge tariff. If

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad
C<\infty,
\quad \eta>0,
\]

then

\[
\boxed{
\frac{\mathfrak T_1}{R}
\ge
\frac{\eta^2}{2C\log2}
-
\frac{1}{2m^2\log2}
-
\frac{\operatorname{TC}(X)}{R\log2}
-
\frac{2(R-1)}{mR}.
}
\tag{3}
\]

For even `R`, `MC-340` proves `TC(X)->0`, so

\[
\liminf_{R\to\infty,\ R\ \mathrm{even}}
\frac{\mathfrak T_1}{R}
\ge
\frac{\eta^2}{2C\log2}.
\tag{4}
\]

Thus bounded-energy constant-factor reciprocal dephasing requires a positive average total-variation separation across source directions. Merely having many distinct rows, as in `MC-350`, is not enough.

At matched-filter energy the conclusion approaches the maximal possible TV boundary. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\qquad
\theta=\varepsilon-\frac{\varepsilon^2}{2},
\]

then

\[
\boxed{
\frac{\mathfrak T_1}{R}
\ge
\frac{\log m}{R\log2}
-
\frac{h(\theta)}{\log2}
-
\frac{2(R-1)}{mR},
}
\tag{5}
\]

where `h` is binary entropy in nats. Hence `epsilon->0` and `R->infinity` force `mathfrak T_1/R->1`. At exact unit-energy dephasing, every pair of distinct source states has mutually singular transcript laws and therefore every surviving source edge has `t_e=1`; exactly

\[
\boxed{
\mathfrak T_1
=R\frac{m-1}{m}.
}
\tag{6}
\]

The practical advantage over KL is architectural. If a candidate channel is generated from genuine source-independent shared randomness,

\[
Y=F(x,U_0),
\qquad U_0\perp X,
\]

then coupling neighboring rows with the same seed gives

\[
\boxed{
\operatorname{TV}(P_x,P_{x'})
\le
\mathbf P\bigl(F(x,U_0)\ne F(x',U_0)\bigr).
}
\tag{7}
\]

Therefore an architecture in which a one-source flip changes the exact transcript on only a small fraction of shared seeds has a small `mathfrak T_1` and cannot realize fixed nontrivial bounded-energy dephasing. This gives a bounded coupling-based upper-theorem surface even when the neighboring output laws are singular and Jeffreys/KL is infinite.

No estimate for `M(x)` follows. The theorem is a finite reciprocal-endpoint admission result; its role is to bridge exact row cuts and divergence tariffs with a metric that remains finite at singularity and has a direct coupling interpretation.

## 1. Full-cube mutual information is bounded by edge total variation

First restore the full cube

\[
V=\{-1,+1\}^R,
\qquad |V|=n,
\]

and let `U` be uniform on `V`. For an arbitrary channel `u -> P_u`, write

\[
T_V:=\sum_{e\in E(V)}\operatorname{TV}(P_u,P_v).
\]

We claim

\[
\boxed{
I(U;Y)
\le
\frac{2\log2}{n}\,T_V.
}
\tag{8}
\]

The proof uses only the bitwise mutual-information chain rule, convexity of total variation, and one elementary Jensen--Shannon bound.

For probability laws `P,Q`, let

\[
\operatorname{JS}(P,Q)
:=
\frac12D\!\left(P\middle\|\frac{P+Q}{2}\right)
+
\frac12D\!\left(Q\middle\|\frac{P+Q}{2}\right).
\]

If `t=TV(P,Q)`, split their common mass to write

\[
P=(1-t)R+tP_1,
\qquad
Q=(1-t)R+tQ_1,
\]

with `P_1 perp Q_1`. Jensen--Shannon divergence is jointly convex, while `JS(R,R)=0` and `JS(P_1,Q_1)=log2`; hence

\[
\boxed{
\operatorname{JS}(P,Q)
\le
(\log2)\operatorname{TV}(P,Q).
}
\tag{9}
\]

Now order the independent uniform bits of `U`. The chain rule gives

\[
I(U;Y)
=
\sum_{i=1}^R I(U_i;Y\mid U_{<i}).
\tag{10}
\]

For each fixed prefix `U_<i=a`, the `i`th conditional term is the Jensen--Shannon divergence between the two output laws obtained by averaging `P_u` over the common suffix with `U_i=+1` and `U_i=-1`. By `(9)` and joint convexity of total variation, that term is at most `log2` times the average TV of the paired `i`-edges with prefix `a`. Averaging over prefixes yields

\[
I(U_i;Y\mid U_{<i})
\le
\frac{2\log2}{n}
\sum_{e\parallel i} t_e.
\tag{11}
\]

Summing `(11)` over coordinates proves `(8)`.

This estimate is deliberately bounded. One singular source edge contributes at most one unit of TV rather than infinite KL cost.

## 2. Puncturing one source state costs only an exponentially small correction

Let

\[
v_0=(+1,\ldots,+1)
\]

be the missing vertex. Extend the punctured channel to `v_0` by choosing one Hamming neighbor `v_1 in S` and setting

\[
P_{v_0}:=P_{v_1}.
\tag{12}
\]

Among the `R` restored edges incident to `v_0`, the edge `{v_0,v_1}` has TV zero and the remaining `R-1` edges have TV at most one. Therefore

\[
T_V
\le
\sum_{e\in E(S)}t_e+(R-1).
\tag{13}
\]

Let `B=1_{\{U\in S\}}`. Conditional on `B=1`, `U` has exactly the source law `X`; conditional on `B=0`, `U` is deterministic. Hence

\[
I(U;Y)
=I(B;Y)+\frac mn I(X;Y)
\ge
\frac mn I(X;Y).
\tag{14}
\]

Combining `(8)`, `(13)`, and `(14)` gives

\[
I(X;Y)
\le
\frac{2\log2}{m}
\left(\sum_{e\in E(S)}t_e+R-1\right),
\]

which is exactly `(2)` after using definition `(1)`.

The correction `2(R-1)log2/m` is exponentially small. No exact-quotient construction and no edge-isoperimetric theorem are needed for this quantitative version.

## 3. The transcript-capacity floor becomes an extensive TV tariff

Under `E(W)<=C` and `delta(W)<=1-eta`, equation (8) of `MC-340` states

\[
I(X;Y)
\ge
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-
\operatorname{TC}(X).
\tag{15}
\]

Combining `(15)` with `(2)` and dividing by `R log2` proves `(3)`. For even rank, `TC(X)->0`, which proves `(4)`.

The normalization has a useful endpoint check. The punctured cube contains

\[
|E(S)|
=
\frac{Rn}{2}-R
=
\frac{R(m-1)}{2}
\]

surviving edges, so

\[
0\le\mathfrak T_1\le R\frac{m-1}{m}.
\tag{16}
\]

Thus `(4)` says a fixed positive fraction of the available normalized TV boundary is necessary. It is stronger than the statement that `Omega(R)` edges are merely unequal: arbitrarily tiny changes on every edge no longer suffice.

## 4. Near matched-filter energy forces nearly maximal TV boundary

For `E(W)<=1` and `delta(W)<=epsilon`, `MC-340` gives

\[
I(X;Y)
\ge
H(X)-Rh(\theta),
\qquad
\theta=\varepsilon-\frac{\varepsilon^2}{2}.
\tag{17}
\]

At even rank, `H(X)=log m`. Combining `(17)` with `(2)` proves `(5)`.

Since

\[
\frac{\log m}{R\log2}\to1,
\qquad
\frac{2(R-1)}{mR}\to0,
\]

letting `epsilon->0` forces `mathfrak T_1/R->1`, the asymptotic maximum in `(16)`.

At `epsilon=0`, `MC-340` gives `H(X|Y)=0`: there is a measurable decoder recovering the source state from the transcript almost surely. The decoder fibers give disjoint full-measure sets for the conditional laws `P_x`, so those laws are pairwise mutually singular. Every surviving edge therefore has `TV=1`, proving `(6)` directly.

This exact endpoint agrees with `MC-350`: its 0/1 channel quotient cut is precisely the deterministic endpoint of the TV metric when all distinguishable neighboring rows become singular.

## 5. Shared randomness turns TV into an architecture-facing source-flip probability

Suppose the channel is realized by a genuine source-independent random seed `U_0` and an exact transcript map `F` as in `(7)`. For neighboring source states `x,x'`, the pair

\[
(F(x,U_0),F(x',U_0))
\]

is a coupling of `P_x,P_{x'}`. Total variation is bounded by the disagreement probability under **any** coupling, so `(7)` follows immediately.

Summing `(7)` over source edges gives

\[
\mathfrak T_1
\le
\frac2m
\sum_{\{x,x'\}\in E(S)}
\mathbf P\bigl(F(x,U_0)\ne F(x',U_0)\bigr).
\tag{18}
\]

This is the point of introducing TV rather than another unbounded divergence. A concrete randomized Möbius endpoint architecture may admit a natural common-noise or common-latent realization for which the probability in `(18)` can be estimated directly from arithmetic stability under one source flip. If that average probability is `o(1)` per source direction, `(3)` rules out fixed nontrivial bounded-energy dephasing.

The deterministic case is the sharp 0/1 limit: with no random seed, two identical exact outputs contribute zero and two different outputs contribute TV one. Then `(18)` reduces to an edge-cut count of the same kind as `MC-350`.

## Prior art and novelty boundary

The information-theoretic ingredients used above are classical. Jensen--Shannon divergence, total variation, mutual-information chain rules, convexity/data processing of statistical distances, and the coupling characterization of total variation are standard. Equation `(9)` is included with its complete common-mass proof, and `(8)` is derived explicitly rather than imported as a black-box cube theorem.

A targeted prior-art audit on 17 September 2026 found the underlying Jensen--Shannon/TV and coupling mechanisms to be classical. No novelty is claimed for `(7)`--`(11)` as abstract information theory, nor for total variation as a statistical distance. No external literature theorem is load-bearing for the stored claim, so this finding adds no new literature anchor to `SOURCES.md`.

The durable Mathia-specific delta is the composition with the punctured reciprocal source and the already established endpoint information floor: `(2)`--`(6)` interpolate quantitatively between the exact quotient-cut obstruction `MC-350` and the KL/Jeffreys source-edge tariffs `MC-351`--`MC-353`. The coupling corollary `(18)` exposes a different architecture-specific upper route: source-flip stability under genuine shared randomness can now be compared directly with the lower dephasing tariff without requiring finite likelihood ratios.

## Boundaries and falsification tests

- **Even rank is load-bearing.** The proof restores one missing vertex of a full Hamming cube. Odd rank has the parity-constrained source image and needs its own edge/TV argument.
- **The full transcript law is required.** Bounding TV for a downstream statistic does not upper-bound TV of the complete admitted transcript unless the transcript actually factors through that statistic.
- **TV is a necessary-resource currency, not a sufficient mechanism.** Large edge TV does not imply that the architecture can realize the required dephasing coefficients.
- **Metric amplitude is irrelevant for exact deterministic outputs.** Two distinct deterministic real or complex transcript values have TV one however close their numerical values are. Thus `(2)` does not repair the inverse-precision escape exposed by `MC-342`; it prices exact distinguishability, not analog resolution.
- **The shared-randomness coupling must be real.** Equation `(7)` is useful only when the same source-independent seed has genuine architectural meaning under both source states. A post-hoc coupling chosen solely to reduce disagreement is not an arithmetic source-stability theorem.
- **Source-dependent hidden randomness must be represented.** If branch choices, seeds, latent labels, metadata, or side channels change with the source, they belong in the lifted architecture before claiming a small common-seed disagreement probability.
- **Singularity is not a loophole.** Unlike KL/Jeffreys, TV remains finite when rows are singular; singular neighboring laws simply pay the maximal edge cost `1`.
- **No arithmetic TV upper bound has yet been proved.** The remaining task is to expose an actual Möbius-derived endpoint channel with a natural shared-randomness/latent coupling and prove a small source-edge disagreement budget, or show that the arithmetic architecture necessarily pays an extensive TV boundary.
- **No `M(x)` estimate follows.** This remains a finite reciprocal-endpoint admission theorem and does not import `1/zeta`, contour shifting, zero-free regions, or an RH-equivalent Mertens estimate.

## Research consequence

The reciprocal endpoint now has three compatible source-edge currencies. `MC-350` gives the 0/1 exact channel cut; `MC-351`--`MC-353` give likelihood-ratio/Jeffreys tariffs when neighboring laws are regular enough; and the present theorem gives a bounded total-variation tariff that survives the singular endpoint and admits direct coupling upper bounds.

This does **not** justify another generic divergence-classification campaign. The productive next step is architecture-specific: identify a genuine Möbius endpoint realization with source-independent common randomness or a canonical latent coupling, then prove an arithmetic upper bound on the average one-source transcript disagreement in `(18)`. If no such stable coupling exists, that failure itself identifies where the architecture is forced to carry extensive source sensitivity.