# MC-351 — Transcript information forces an extensive source-edge KL budget

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-350` shows that bounded-energy reciprocal dephasing forces the exact channel-law quotient to cut an extensive part of the reciprocal source graph, but leaves open a quantitative loophole: distinct channel rows may be arbitrarily close, so an extensive exact cut alone does not force an extensive KL expenditure.

That loophole can be closed on the **lower-bound side** without assuming a raw-query model, a finite transcript alphabet, Gaussian noise, or reliable recovery of a chosen downstream quotient.

For source states `x,x'`, keep the symmetrized transcript divergence of `MC-348`--`MC-349`,

\[
b(x,x')
:=\frac12\left(D(P_x\|P_{x'})+D(P_{x'}\|P_x)\right),
\qquad
P_x:=\operatorname{Law}(Y\mid X=x).
\tag{1}
\]

Define the puncture defect

\[
\Gamma_d
:=
\frac1{2^d-1}
\sum_{k=0}^{d-1}
(2^{k+1}-1)
\,h\!\left(\frac{2^k}{2^{k+1}-1}\right),
\tag{2}
\]

where `h(p)=-p log p-(1-p)log(1-p)` is binary entropy in nats and the `k=0` term is zero. Then

\[
0\le\Gamma_d<2\log2.
\tag{3}
\]

### Even rank

For even `R`, let

\[
S=\{-1,+1\}^R\setminus\{\mathbf1\},
\qquad m=2^R-1,
\]

with `X` uniform on `S`, and let `E_1` be the surviving Hamming-one edges. Put

\[
\mathfrak J_1
:=\frac2m\sum_{e\in E_1}b_e.
\tag{4}
\]

Then every transcript channel satisfies

\[
\boxed{
I(X;Y)
\le
\frac12\mathfrak J_1+\Gamma_R.
}
\tag{5}
\]

Equivalently,

\[
\boxed{
\mathfrak J_1
\ge
2\,[I(X;Y)-\Gamma_R]_+.
}
\tag{6}
\]

### Odd rank

For odd `R>=3`, use the notation of `MC-348`: let `E_0={X\ne\mathbf1}`, so

\[
\Lambda_R:=\mathbf P(E_0)=\frac{2^R-2}{2^R-1},
\]

and conditioned on `E_0` the source is uniform on the even-parity cube with the all-`+1` vertex removed. Let `E_2` be its surviving pair-flip graph and

\[
\mathfrak J_2
:=
\frac{2\Lambda_R}{(2^{R-1}-1)(R-1)}
\sum_{e\in E_2}b_e.
\tag{7}
\]

Then

\[
\boxed{
\mathfrak J_2
\ge
\frac{R}{R-1}
\left[
I(X;Y)-h(\Lambda_R)-\Lambda_R\Gamma_{R-1}
\right]_+.
}
\tag{8}
\]

Thus in either parity

\[
I(X;Y)=\Omega(R)
\quad\Longrightarrow\quad
\mathfrak J=\Omega(R),
\tag{9}
\]

for the source-natural edge budget `mathfrak J` already used by `MC-348`--`MC-349`.

For the canonical channel-law quotient `Q=q_Y(X)` of `MC-350`, every non-cut edge has `P_x=P_{x'}` and therefore `b_e=0`. Consequently the all-edge budget in `(4)` or `(7)` is already supported entirely on the exact channel cut. The linear information floor of `MC-340` therefore forces not only an extensive **number** of cut directions, but an extensive **aggregate statistical separation** across them.

In particular, under bounded coefficient energy

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad \eta>0,
\tag{10}
\]

`MC-340` gives

\[
I(X;Y)
\ge
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-\operatorname{TC}(X).
\tag{11}
\]

Hence for fixed `eta,C`,

\[
\boxed{
\mathfrak J_1
\ge
\frac{\eta^2}{C}R-O(1)
\qquad(R\ \text{even}),
}
\tag{12}
\]

and

\[
\boxed{
\mathfrak J_2
\ge
\frac{\eta^2}{2C}R-O(1)
\qquad(R\ \text{odd}).
}
\tag{13}
\]

At matched-filter energy, if `E(W)<=1` and `delta(W)<=epsilon`, `MC-340` gives

\[
I(X;Y)
\ge
H(X)-R h(\theta),
\qquad
\theta=\varepsilon-\frac{\varepsilon^2}{2}.
\tag{14}
\]

Therefore `epsilon_R -> 0` forces an asymptotically linear edge-KL budget. At exact unit-energy dephasing, `I(X;Y)=H(X)`, so `X` is determined by `Y`; the row measures `P_x` are then pairwise mutually singular. Every surviving source edge has infinite KL in both directions and

\[
\boxed{
\mathfrak J=+\infty
\qquad(\mathcal E(W)\le1,\ \delta(W)=0).
}
\tag{15}
\]

No estimate for `M(x)` follows. The advance is a finite-source converse: the information requirement of `MC-340` now has a channel-free local statistical currency on the exact source graph. The remaining analytic problem is one-sided and concrete: an admissible Möbius/endpoint architecture must upper-bound this forced edge-KL expenditure from its actual coefficient, precision, bandwidth, or regularity resources.

## 1. Binary information is bounded by neighboring Jeffreys divergence

For two probability laws `P,Q`, let

\[
M=\frac12(P+Q).
\]

The Jensen--Shannon divergence

\[
\operatorname{JS}(P,Q)
:=\frac12D(P\|M)+\frac12D(Q\|M)
\]

is the mutual information of an equiprobable binary selector passed through the channel with rows `P,Q`. The classical Lin inequality gives

\[
\operatorname{JS}(P,Q)
\le
\frac14\left(D(P\|Q)+D(Q\|P)\right)
=\frac12 b(P,Q).
\tag{16}
\]

Also, KL divergence is jointly convex. Therefore, for equally weighted pairs `(P_z,Q_z)`,

\[
\operatorname{JS}\!\left(
\frac1N\sum_zP_z,
\frac1N\sum_zQ_z
\right)
\le
\frac1{2N}\sum_z b(P_z,Q_z).
\tag{17}
\]

Equation `(17)` is the only information-theoretic estimate needed for the even-rank proof.

## 2. A chain decomposition prices the punctured cube up to an O(1) defect

Write

\[
X=(X_1,\ldots,X_R)
\]

and expand mutual information by the chain rule:

\[
I(X;Y)
=
\sum_{i=1}^R I(X_i;Y\mid X_{<i}).
\tag{18}
\]

Fix `i` and a prefix `a in {-1,+1}^{i-1}` that is **not** the all-`+1` prefix. Because the missing source state is `mathbf1`, once the prefix already contains a `-1`, both values of `X_i` are equiprobable and the remaining suffix `z in {-1,+1}^{R-i}` is uniform in each branch.

Let

\[
Q_{a,+}
=2^{-(R-i)}\sum_z P_{(a,+,z)},
\qquad
Q_{a,-}
=2^{-(R-i)}\sum_z P_{(a,-,z)}.
\tag{19}
\]

Then

\[
I(X_i;Y\mid X_{<i}=a)
=\operatorname{JS}(Q_{a,+},Q_{a,-})
\le
\frac1{2^{R-i+1}}
\sum_z b\bigl((a,+,z),(a,-,z)\bigr)
\tag{20}
\]

by `(17)`. The prefix has probability

\[
\mathbf P(X_{<i}=a)
=rac{2^{R-i+1}}m,
\tag{21}
\]

so its contribution to `(18)` is at most

\[
\frac1m
\sum_z b\bigl((a,+,z),(a,-,z)\bigr).
\tag{22}
\]

Summing `(22)` over every non-all-plus prefix and every coordinate charges a subset of the surviving Hamming edges, each exactly once, and is therefore at most

\[
\frac1m\sum_{e\in E_1}b_e
=\frac12\mathfrak J_1.
\tag{23}
\]

It remains to pay for the unique all-plus prefix at each level. Put `k=R-i`. Given

\[
X_{<i}=\mathbf1,
\]

there are `2^{k+1}-1` admissible completions: `2^k` with `X_i=-1` and `2^k-1` with `X_i=+1`. Hence

\[
\mathbf P(X_{<i}=\mathbf1)
=rac{2^{k+1}-1}{m}
\tag{24}
\]

and the corresponding conditional mutual information is bounded by the binary entropy

\[
h\!\left(\frac{2^k}{2^{k+1}-1}\right).
\tag{25}
\]

Summing `(24)`--`(25)` over `k=0,...,R-1` gives exactly `Gamma_R`. Combining with `(23)` proves `(5)`.

Since `h<=log2`,

\[
\Gamma_R
\le
\frac{\log2}{2^R-1}
\sum_{k=0}^{R-1}(2^{k+1}-1)
<2\log2,
\tag{26}
\]

which proves `(3)`. Thus deleting one source vertex from the cube costs only a dimension-free additive entropy defect.

## 3. The parity-constrained odd source is covered by every pivot chart

For odd `R`, condition on `E_0`. The conditional support

\[
S_0
=\left\{x\in\{-1,+1\}^R:
\prod_{j=1}^R x_j=+1\right\}
\setminus\{\mathbf1\}
\tag{27}
\]

has size

\[
M=2^{R-1}-1.
\]

Fix a pivot coordinate `r`. The map that retains the other `R-1` coordinates and reconstructs

\[
x_r=\prod_{j\ne r}x_j
\tag{28}
\]

identifies `S_0` with a punctured `(R-1)`-cube. Flipping one free coordinate `j ne r` corresponds exactly to the pair flip `(j,r)` in `S_0`.

Let `E_r` be the surviving pair edges containing pivot `r` and define

\[
\mathfrak J_r
:=\frac2M\sum_{e\in E_r}b_e.
\tag{29}
\]

Applying `(5)` in this chart to

\[
I_0:=I(X;Y\mid E_0=1)
\]

gives, for every pivot,

\[
\mathfrak J_r
\ge
2[I_0-\Gamma_{R-1}]_+.
\tag{30}
\]

Every pair edge belongs to exactly two pivot stars. Therefore

\[
\sum_{r=1}^R\mathfrak J_r
=
\frac4M\sum_{e\in E_2}b_e
=
\frac{2(R-1)}{\Lambda_R}\mathfrak J_2.
\tag{31}
\]

Summing `(30)` over all pivots yields

\[
\mathfrak J_2
\ge
\frac{\Lambda_RR}{R-1}
[I_0-\Gamma_{R-1}]_+.
\tag{32}
\]

Because `E_0` is a deterministic function of `X`, while `X` is deterministic on `E_0^c`,

\[
I(X;Y)
=I(E_0;Y)+\Lambda_R I_0
\le
h(\Lambda_R)+\Lambda_R I_0.
\tag{33}
\]

Substitution of `(33)` into `(32)` proves `(8)`.

The use of all `R` pivot charts is load-bearing. A single pivot sees only one star of the pair-flip graph and would lose a factor of order `R`; summing all pivots restores the intrinsic normalization of `MC-348`.

## 4. The channel-law quotient carries the same KL budget

Let `q_Y` be the canonical quotient from `MC-350`:

\[
q_Y(x)=q_Y(x')
\iff
P_x=P_{x'}.
\tag{34}
\]

On every non-cut edge `e={x,x'}` we have `P_x=P_{x'}` and therefore `b_e=0`. Hence

\[
\sum_{e\in E}b_e
=
\sum_{e\in E_{q_Y}}b_e.
\tag{35}
\]

The lower bounds `(6)` and `(8)` are thus already lower bounds for the aggregate divergence on the exact channel quotient cut. No decoder for `q_Y(X)` is assumed and no reliability target is inserted: the result follows solely from how much joint source information the transcript actually carries.

This is the quantitative complement missing from `MC-350`. That finding proved that a high-information transcript has a large exact channel boundary. The present result proves that, on the reciprocal source graph, high transcript information also forces a large total Jeffreys/KL separation across that boundary.

## 5. Composition with dephasing leaves only the analytic upper-bound problem

For bounded-energy constant-factor dephasing, combine `(6)` or `(8)` with the information floor `(11)` from `MC-340`. Since

\[
\operatorname{TC}(X)=O(1),
\qquad
\Gamma_R=O(1),
\qquad
h(\Lambda_R)=o(1),
\]

the even and odd asymptotics `(12)`--`(13)` follow.

For matched-filter energy, substitute `(14)`. In even rank,

\[
\mathfrak J_1
\ge
2\left[
H(X)-Rh(\theta)-\Gamma_R
\right]_+,
\tag{36}
\]

while in odd rank

\[
\mathfrak J_2
\ge
\frac{R}{R-1}
\left[
H(X)-Rh(\theta)-h(\Lambda_R)-\Lambda_R\Gamma_{R-1}
\right]_+.
\tag{37}
\]

Thus `epsilon_R->0` makes the required edge discrimination linear in `R` even before one asks for coordinatewise source recovery.

At `epsilon=0`, `MC-340` gives `H(X|Y)=0`. For discrete `X`, exact recovery partitions transcript space into disjoint measurable decoding regions `A_x` with

\[
P_x(A_x)=1,
\qquad
P_{x'}(A_x)=0
\quad(x'\ne x).
\]

Hence the row laws are pairwise mutually singular, so every divergence across a surviving source edge is infinite. This proves `(15)`.

The frontier is consequently asymmetric now. The **lower** source-edge KL tariff is intrinsic and representation independent. Any viable analytic architecture must escape only by showing that its admitted transcript can actually generate an `Omega(R)` edge-divergence budget at acceptable arithmetic resource cost; conversely, a source-natural theorem giving `mathfrak J=o(R)` for that architecture would rule out fixed nontrivial bounded-energy dephasing immediately.

## Prior art and novelty boundary

The information-theoretic ingredients are classical and **no novelty is claimed** for the abstract inequalities.

Jianhua Lin, *Divergence measures based on the Shannon entropy*, IEEE Transactions on Information Theory **37** (1991), 145--151, DOI `10.1109/18.61115`, introduced the Jensen--Shannon divergence and records the classical upper comparison of Jensen--Shannon information radius by one quarter of the Jeffreys divergence used in `(16)`.

Entropy tensorization and logarithmic-Sobolev control on product spaces provide the broader classical language behind the full-cube version of `(5)`. Pietro Caputo, Georg Menz and Prasad Tetali, *Approximate tensorization of entropy at high temperature*, Annales de la Faculté des sciences de Toulouse **24** (2015), 691--716, DOI `10.5802/afst.1460`, explicitly treats exact tensorization for product measures as the baseline and develops approximate tensorization under dependence. Alex Samorodnitsky, *A modified logarithmic Sobolev inequality for the Hamming cube and some applications*, arXiv `0807.1679`, records the classical Hamming-cube logarithmic-Sobolev/Dirichlet-form setting.

A targeted audit on 17 September 2026 found no basis for claiming novelty for Jensen--Shannon versus Jeffreys comparison, joint convexity of KL, entropy tensorization, or Hamming-cube log-Sobolev ideas. The retained Mathia delta is the explicit punctured-source bookkeeping and its composition with the already-derived reciprocal-source information floor and edge-KL currency. In particular, `(5)` and `(8)` turn the abstract `MC-340` information requirement directly into the exact graph-local divergence resource introduced independently in `MC-348`.

Primary/authoritative audit links:

- Lin 1991, IEEE: `https://doi.org/10.1109/18.61115`.
- Caputo--Menz--Tetali 2015: `https://doi.org/10.5802/afst.1460`.
- Samorodnitsky 2008: `https://arxiv.org/abs/0807.1679`.

## Boundary conditions and falsification tests

- **The result is a lower bound, not the missing arithmetic upper bound.** It proves that a successful transcript must spend extensive source-edge divergence; it does not show that any natural Möbius-derived transcript has `o(R)` divergence.
- **The puncture defect is deliberately coarse.** `Gamma_R<2 log 2` is sufficient for the linear conclusion. Sharper modified log-Sobolev constants for the punctured source graph may improve `O(1)` terms but cannot change the `Omega(R)` frontier.
- **Infinite edge KL is allowed.** If neighboring row laws fail mutual absolute continuity, the corresponding `b_e` is infinite and the theorem is automatic. Any analytic no-go using this result must independently show finite or controlled edge divergence.
- **Even and odd graphs are not interchangeable.** Even rank uses Hamming-one edges. Odd rank uses the parity-preserving pair-flip graph and requires the all-pivot averaging in `(31)`.
- **No decoder is required.** Unlike `MC-348`--`MC-349`, equations `(5)` and `(8)` do not assume reliable recovery of the full source or of a destination quotient. They price the information already present in the transcript.
- **No finite alphabet, query syntax, or observation factorization is required.** The proof applies to arbitrary channel rows whenever the relevant KL divergences are defined, with `+infinity` interpreted in the usual extended sense.
- **No arithmetic zero information is imported.** The argument uses only the finite reciprocal source law and prior endpoint findings; it does not use `1/zeta(s)`, contour shifting, a zero-free region, or an RH-equivalent Mertens estimate.
- **No `M(x)` consequence follows.** A bridge from an actual Möbius analytic transcript to a sublinear edge-KL upper bound remains to be proved.

## Research consequence

`MC-350` left two quantitative possibilities on its extensive exact channel cut: the many distinct rows might differ substantially, or they might be separated only by vanishingly small statistical changes. `MC-351` rules out the second possibility **in aggregate** whenever the transcript performs the bounded-energy dephasing demanded by the endpoint architecture.

The reciprocal-source program now has a representation-independent lower currency:

\[
\text{bounded-energy dephasing}
\Longrightarrow
I(X;Y)=\Omega(R)
\Longrightarrow
\mathfrak J=\Omega(R).
\]

The next admissible step should therefore not seek another abstract reliability converse. It should derive an **analytic upper bound on `mathfrak J` for the actual admitted coefficient transcript**—for example from coefficient energy, precision, harmonic bandwidth, source regularity, or a proved combination of them—and compare that upper bound directly with `(12)`--`(13)`. A sublinear upper bound would become a genuine obstruction; an extensive upper bound with matching construction would identify the resource scale a viable arithmetic mechanism must actually pay.