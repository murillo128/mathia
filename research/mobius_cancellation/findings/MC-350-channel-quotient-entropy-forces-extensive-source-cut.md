# MC-350 — Channel-quotient entropy forces an extensive reciprocal-source cut

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the even-rank reciprocal endpoint source from `MC-338`--`MC-340`. Put

\[
n=2^R,
\qquad
m=n-1,
\qquad
S=\{-1,+1\}^R\setminus\{(+1,\ldots,+1)\},
\]

and let `X` be uniform on `S`. Give `S` the induced Hamming-neighbor graph from the full `R`-cube.

Let `Y` be any complete admitted transcript and write

\[
P_x:=\operatorname{Law}(Y\mid X=x).
\]

Define the **channel-law quotient**

\[
q_Y:S\to Q_Y,
\qquad
q_Y(x)=q_Y(x')
\iff
P_x=P_{x'}.
\tag{1}
\]

Thus `q_Y` identifies exactly those reciprocal source states that the transcript channel treats identically. Let

\[
Q:=q_Y(X),
\]

let `E_Q` be the set of Hamming edges of `S` whose endpoints have different `Q`-labels, and define its average cut degree

\[
\kappa_Q:=\frac{2|E_Q|}{m}.
\tag{2}
\]

If `H_bit(Q)` denotes Shannon entropy in **bits**, then

\[
\boxed{
\kappa_Q
\ge
H_{\rm bit}(Q)-\frac{2R}{m}.
}
\tag{3}
\]

Moreover the channel factors as

\[
X\longrightarrow Q\longrightarrow Y,
\]

so, with mutual information measured in nats,

\[
\boxed{
H_{\rm bit}(Q)
\ge
\frac{I(X;Y)}{\log 2}.
}
\tag{4}
\]

Combining `(3)`--`(4)` with the global transcript-capacity bound `MC-340` gives a source-geometric strengthening of that obstruction. If

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad \eta>0,
\]

then

\[
\boxed{
\kappa_Q
\ge
\frac1{\log2}
\left[
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-\operatorname{TC}(X)
\right]
-\frac{2R}{m}.
}
\tag{5}
\]

For fixed positive `eta` and `C`, every feasible bounded-energy architecture with a fixed nontrivial dephasing gain therefore has

\[
\boxed{
\kappa_Q
\ge
\frac{\eta^2}{2C\log2}\,R-O(1).
}
\tag{6}
\]

In particular, the transcript cannot mediate such dephasing through a quotient whose source boundary is `o(R)` on average.

At matched-filter energy the conclusion is stronger. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\]

and

\[
\theta=\varepsilon-\frac{\varepsilon^2}{2},
\]

then `MC-340` gives

\[
I(X;Y)\ge\log m-Rh(\theta),
\]

where `h` is binary entropy in natural logarithms. Hence

\[
\boxed{
\kappa_Q
\ge
\log_2m
-\frac{R}{\log2}h(\theta)
-\frac{2R}{m}.
}
\tag{7}
\]

Thus `epsilon -> 0` forces

\[
\frac{\kappa_Q}{R}\to1.
\tag{8}
\]

At exact unit-energy dephasing, `epsilon=0`, the quotient `q_Y` is injective on `S`; consequently every surviving Hamming edge crosses the quotient and

\[
\boxed{
\kappa_Q
=
R\frac{2^R-2}{2^R-1}.
}
\tag{9}
\]

No estimate for `M(x)` follows. The advance is finite and structural: the linear information tariff of `MC-340` is not merely an abstract entropy count. For the canonical exact quotient carried by the transcript channel, it forces an extensive cut in the same reciprocal source graph used by the destination-relative reliability theorem `MC-349`.

## 1. The channel-law quotient is the canonical deterministic bottleneck

By definition `(1)`, the conditional law of `Y` given `X=x` depends only on `q_Y(x)`. Therefore

\[
X\to Q\to Y
\tag{10}
\]

is a Markov chain. Since `Q` is a deterministic function of `X`, data processing gives

\[
I(X;Y)=I(Q;Y)\le H(Q).
\tag{11}
\]

The entropy on the right of `(11)` is in nats. Dividing by `log 2` proves `(4)`.

The same conclusion holds for any proposed deterministic mediator `q:S->Q'` for which the transcript channel really factors through `q`, meaning `P_x` is constant on every `q`-fiber. Such a mediator may refine the canonical quotient, but it cannot have smaller entropy than the information already carried by `Y`.

This qualification is load-bearing. An arbitrary downstream statistic need not be a bottleneck for the entire transcript. If `Y` contains source information that is discarded before that statistic is formed, the statistic's quotient cannot be substituted into `(4)` without proving the required factorization.

## 2. Partition entropy forces boundary on the punctured cube

Let

\[
V=\{-1,+1\}^R,
\qquad |V|=n,
\]

and restore the missing vertex

\[
v_0=(+1,\ldots,+1).
\]

Extend `q_Y` arbitrarily to a partition map

\[
\widetilde q:V\to\widetilde Q.
\]

Let `E(\widetilde q)` be the full-cube edges whose endpoints receive different labels. Restoring `v_0` adds only its `R` incident edges, so

\[
|E(\widetilde q)|
\le
|E_Q|+R.
\tag{12}
\]

For each partition cell `B_z={v:\widetilde q(v)=z}`, the standard weak edge-isoperimetric inequality on the Boolean cube is

\[
|\partial B_z|
\ge
|B_z|\log_2\frac{n}{|B_z|}.
\tag{13}
\]

Summing `(13)` over all cells counts every cut edge twice. If `U` is uniform on `V`, then

\[
2|E(\widetilde q)|
\ge
\sum_z|B_z|\log_2\frac{n}{|B_z|}
=
nH_{\rm bit}(\widetilde q(U)).
\tag{14}
\]

Let `B=1_{\{U\in S\}}`. Conditioning cannot increase average uncertainty, hence

\[
H_{\rm bit}(\widetilde q(U))
\ge
H_{\rm bit}(\widetilde q(U)\mid B).
\tag{15}
\]

The conditional entropy at `B=0` is zero because the missing set contains only `v_0`, whereas at `B=1` it is exactly `H_bit(Q)`. Therefore

\[
H_{\rm bit}(\widetilde q(U))
\ge
\frac mn H_{\rm bit}(Q).
\tag{16}
\]

Equations `(12)`, `(14)`, and `(16)` yield

\[
2(|E_Q|+R)
\ge
mH_{\rm bit}(Q),
\]

which is exactly `(3)` after division by `m`.

The correction `2R/m` is exponentially small. It is the complete price of passing from the full cube to the punctured even-rank reciprocal source for this entropy-boundary argument.

## 3. Bounded-energy dephasing therefore forces an extensive channel cut

For even `R`, `MC-340` proves

\[
\operatorname{TC}(X)	o0
\tag{17}
\]

and, under `E(W)<=C` and `delta(W)<=1-eta`,

\[
I(X;Y)
\ge
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-\operatorname{TC}(X).
\tag{18}
\]

Substituting `(18)` into `(3)`--`(4)` proves `(5)`. Since `m=2^R-1`, both the puncture term `2R/m` and the `R/m^2` term vanish exponentially, while `(17)` is `o(1)`. This gives `(6)`.

The geometric statement is stronger than merely saying that the transcript needs exponentially many distinguishable global states. Any exact channel quotient capable of bounded-energy constant-factor dephasing must separate neighboring reciprocal source states in a positive fraction of the `R` available directions on average.

This is precisely the source geometry charged by `MC-349`: its reliability bound depends on the cut of the actual destination quotient, not just on output alphabet size. The present result proves that the **channel's own exact quotient** cannot realize the bounded-energy dephasing requirement with a sparse source cut.

## 4. Near matched-filter dephasing forces almost full source sensitivity

Under `E(W)<=1` and `delta(W)<=epsilon`, equation (9) of `MC-340` gives

\[
I(X;Y)
\ge
H(X)-Rh(\theta),
\qquad
\theta=\varepsilon-\varepsilon^2/2.
\tag{19}
\]

For even `R`, `H(X)=log m`. Combining `(19)` with `(3)`--`(4)` proves `(7)`. Because `log_2 m=R+o(1)` and `h(theta)->0` as `epsilon->0`, equation `(8)` follows.

At `epsilon=0`, `MC-340` gives

\[
I(X;Y)=H(X)=\log m.
\tag{20}
\]

But `(11)` and deterministicity also give

\[
I(X;Y)\le H(Q)\le H(X).
\]

Thus equality holds throughout and

\[
H(X\mid Q)=0.
\tag{21}
\]

Hence `q_Y` is injective on the support `S`. The full `R`-cube has `Rn/2` edges; deleting one vertex removes exactly `R` edges, leaving

\[
|E(S)|=\frac{Rn}{2}-R.
\]

All these edges cross an injective quotient, so `(2)` gives `(9)`.

## Relevance to the endpoint frontier

`MC-349` showed that a downstream quotient is priced by its cut geometry: sparse-cut destinations can evade the full-vector reliability tariff, while parity-like destinations remain expensive. The immediate unresolved question was whether the endpoint dephasing mechanism itself might secretly factor through a low-boundary quotient and thereby avoid extensive source discrimination.

Equations `(5)`--`(9)` close that loophole for the **exact transcript-law quotient**. At bounded coefficient energy, any transcript accomplishing nontrivial all-mode dephasing has an `Omega(R)` average source cut; near matched-filter performance the cut approaches the full reciprocal source graph.

This does not yet finish the analytic reliability problem. Distinct channel rows can be arbitrarily close as probability laws. An extensive exact cut therefore does **not** imply an extensive symmetrized-KL budget. The remaining load-bearing question is quantitative: can the admissible Möbius/endpoint architecture upper- and lower-control the aggregate edge divergence on this now-forced extensive cut strongly enough to contradict or price the desired dephasing?

## Prior art and novelty boundary

The ingredients are classical and **no novelty is claimed** for the abstract information-theoretic or Boolean-isoperimetric mechanism.

L. H. Harper, *Optimal Assignments of Numbers to Vertices*, Journal of the Society for Industrial and Applied Mathematics **12** (1964), 131--135, DOI `10.1137/0112012`, is a classical source for Boolean-cube edge isoperimetry. A modern explicit statement of the weak inequality `(13)`, together with its classical provenance, appears in David Ellis, Nathan Keller and Noam Lifshitz, *On a biased edge isoperimetric inequality for the discrete cube*, Journal of Combinatorial Theory, Series A **163** (2019), 118--162, DOI `10.1016/j.jcta.2018.12.001`, arXiv `1702.01675`.

Data processing and the entropy identities in `(10)`--`(11)` are standard information theory. The Mathia-specific delta is the exact composition of these classical facts with the punctured reciprocal source and the independently derived dephasing information floor `MC-340`. That composition turns an abstract `Omega(R)` transcript-information requirement into an `Omega(R)` **source-edge boundary requirement** for the canonical channel quotient and aligns it with the cut geometry introduced in `MC-349`.

## Boundary conditions and falsification tests

- **Even rank is load-bearing here.** The proof uses the punctured full Hamming cube. Odd rank has the parity-constrained source image and the pair-flip graph of `MC-348`--`MC-349`; its corresponding partition-isoperimetric theorem must be proved separately.
- **Exact row equality defines the quotient.** Two channel rows that are merely close remain different cells. Therefore `(3)` alone supplies no quantitative divergence cost; a candidate that turns tiny row differences into a large cut is not refuted by this finding.
- **The mediator must be a real bottleneck.** For a proposed coarser quotient `q`, one must prove `P_x=P_{x'}` whenever `q(x)=q(x')`. A downstream statistic that discards information after the transcript is generated does not automatically satisfy this factorization.
- **The isoperimetric input is weak but sufficient.** Sharper partition inequalities may improve constants or expose cell-shape rigidity, but the linear conclusion `(6)` already follows from the classical weak edge boundary bound.
- **No arithmetic estimate is imported.** The result uses only the finite reciprocal-source construction and earlier canonical endpoint findings. It does not use a zeta zero-free region, `1/zeta(s)`, contour shifting, or an RH-equivalent Mertens estimate.
- **No `M(x)` consequence follows.** A natural arithmetic architecture still has to connect its analytic observations to this finite transcript model and control the resulting edge divergences.

## Research consequence

The reciprocal endpoint frontier has moved from **whether** bounded-energy dephasing needs extensive source sensitivity to **how much statistical separation** must be carried on that extensive boundary.

For even rank, low-boundary exact quotients are no longer an escape from the `MC-340` information floor. The next admissible attack should therefore work on the aggregate symmetrized-KL geometry of the channel-law cut: derive analytic upper bounds from coefficient energy, precision, bandwidth, or source regularity, or prove a destination-relevant lower bound strong enough to combine with `MC-349`. Merely exhibiting many distinct transcript laws is now known to be insufficient.