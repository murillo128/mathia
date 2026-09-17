# MC-360 — Hellinger affinity tensorizes a bounded latent/component source-edge tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-359` replaced the singularity-sensitive KL/Jeffreys tariff by total variation, which stays bounded and has a direct common-coupling interpretation. Total variation is useful for exact source-flip stability, but it does not factor cleanly through an independently generated multicomponent transcript. A second bounded currency closes that compositional gap.

For probability laws `P,Q` define the Hellinger affinity and normalized squared Hellinger distance

\[
\operatorname{Aff}(P,Q)
:=\int \sqrt{dP\,dQ},
\qquad
H^2(P,Q):=1-\operatorname{Aff}(P,Q)\in[0,1].
\tag{1}
\]

Continue the even-rank reciprocal endpoint notation

\[
n=2^R,
\qquad
m=n-1,
\qquad
S=\{-1,+1\}^R\setminus\{(+1,\ldots,+1)\},
\tag{2}
\]

with `X` uniform on `S`, complete admitted transcript `Y`, and

\[
P_x:=\operatorname{Law}(Y\mid X=x).
\tag{3}
\]

For every surviving Hamming edge `e={x,x'}` put

\[
h_e^2:=H^2(P_x,P_{x'})
\]

and define the normalized output Hellinger edge budget

\[
\mathfrak H_1
:=
\frac{2}{m}\sum_{e\in E(S)}h_e^2.
\tag{4}
\]

Then

\[
\boxed{
I(X;Y)
\le
\mathfrak H_1
+
\frac{2(R-1)}{m}.
}
\tag{5}
\]

Consequently the transcript-capacity lower bound of `MC-340` forces a positive extensive Hellinger boundary. If

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad C<\infty,
\quad \eta>0,
\tag{6}
\]

then

\[
\boxed{
\frac{\mathfrak H_1}{R}
\ge
\frac{\eta^2}{2C}
-
\frac{1}{2m^2}
-
\frac{\operatorname{TC}(X)}{R}
-
\frac{2(R-1)}{mR}.
}
\tag{7}
\]

For even `R`, `MC-340` proves `TC(X)->0`, hence

\[
\boxed{
\liminf_{R\to\infty,\ R\ \mathrm{even}}
\frac{\mathfrak H_1}{R}
\ge
\frac{\eta^2}{2C}.
}
\tag{8}
\]

The main additional point is architectural. Suppose a source edge `e={x,x'}` admits a common latent coordinate `Theta` and, conditional on that coordinate, a finite product transcript

\[
\Theta\sim\nu_x,
\qquad
Y=(Y_1,\ldots,Y_k),
\qquad
Y_j\mid\Theta=\theta\sim K_{x,j}(\cdot\mid\theta)
\tag{9}
\]

with the `Y_j` conditionally independent given `Theta`; use the analogous law under `x'`. Let `kappa` dominate `nu_x,nu_{x'}` and write

\[
r_x=\frac{d\nu_x}{d\kappa},
\qquad
r_{x'}=\frac{d\nu_{x'}}{d\kappa},
\]

and

\[
h_{e,j}^2(\theta)
:=
H^2\!\left(
K_{x,j}(\cdot\mid\theta),
K_{x',j}(\cdot\mid\theta)
\right).
\tag{10}
\]

Define the lifted bounded architecture cost

\[
\boxed{
 a_e
 :=
 H^2(\nu_x,\nu_{x'})
 +
 \sum_{j=1}^k
 \int
 \sqrt{r_x(\theta)r_{x'}(\theta)}\,
 h_{e,j}^2(\theta)\,d\kappa(\theta).
}
\tag{11}
\]

Then

\[
\boxed{
H^2(P_x,P_{x'})\le a_e.
}
\tag{12}
\]

Thus, with

\[
\mathfrak A_1
:=
\frac{2}{m}\sum_{e\in E(S)}a_e,
\tag{13}
\]

we have

\[
\mathfrak H_1\le\mathfrak A_1,
\]

so every lower bound `(7)`--`(8)` remains valid with `mathfrak A_1` in place of `mathfrak H_1`. Source dependence in a latent law and source dependence in conditionally independent transcript components therefore cannot both become negligible on average while retaining fixed nontrivial bounded-energy reciprocal dephasing.

When the latent law is genuinely source-independent, `nu_x=nu`, the latent term vanishes and `(11)` becomes an average of component Hellinger costs. If component `j` depends on source coordinates only through `A_j subseteq {1,...,R}` and, for every surviving edge in direction `i in A_j`,

\[
h_{e,j}^2(\theta)\le\alpha_{j,i}
\qquad\text{for `nu`-almost every `theta`,}
\tag{14}
\]

then every coordinate direction has exactly `(m-1)/2` surviving edges, and

\[
\boxed{
\mathfrak A_1
\le
\frac{m-1}{m}
\sum_{j=1}^k\sum_{i\in A_j}\alpha_{j,i}.
}
\tag{15}
\]

Combining `(15)` with `(8)` yields the asymptotic weighted-incidence tariff

\[
\boxed{
\liminf_{R\to\infty,\ R\ \mathrm{even}}
\frac1R
\sum_{j=1}^k\sum_{i\in A_j}\alpha_{j,i}
\ge
\frac{\eta^2}{2C}.
}
\tag{16}
\]

Hence a product architecture cannot evade the global transcript-information floor by splitting source dependence into many individually weak local components. The total source-coordinate sensitivity, measured in bounded Hellinger currency, must still be extensive.

No estimate for `M(x)` follows. The result is a finite reciprocal-endpoint admission theorem. Its role is to convert the global information floor into a bounded, distributional, componentwise tariff that is exact enough to audit conditionally independent Möbius-derived architectures without requiring finite likelihood ratios or a hand-chosen coupling.

## 1. Jensen--Shannon divergence is bounded by normalized squared Hellinger distance

The full-cube argument needs one pointwise divergence comparison. For arbitrary probability laws `P,Q`,

\[
\boxed{
\operatorname{JS}(P,Q)\le H^2(P,Q),
}
\tag{17}
\]

where logarithms are natural and `JS` is the equal-weight Jensen--Shannon divergence.

This can be proved directly, including the sharp local constant. Let `lambda` dominate `P,Q` with densities `p,q`. It suffices by homogeneity to prove, for `t>0`,

\[
\frac12\left[
 t^2\log\frac{2t^2}{1+t^2}
 +
 \log\frac{2}{1+t^2}
\right]
\le
\frac12(t-1)^2.
\tag{18}
\]

Let the right side minus the left side be `Phi(t)`. Then

\[
\Phi(1)=\Phi'(1)=0,
\]

and a direct differentiation gives

\[
\Phi''(t)
=
 u-1-\log u,
\qquad
u:=\frac{2t^2}{1+t^2}>0.
\tag{19}
\]

Since `u-1-log u>=0` for every positive `u`, `Phi` is convex and has its minimum at `t=1`; therefore `Phi(t)>=0`. The cases where one density vanishes follow by continuity. Integrating `(18)` proves `(17)`.

This normalization matters. `H^2` has ceiling one, while `JS` has ceiling `log 2`. Near equality of the laws the two agree to second order, whereas at mutual singularity `(17)` has slack `1-log 2`. The Hellinger tariff is therefore chosen for composition, not because it uniformly improves the TV constant in `MC-359`.

## 2. The full-cube mutual information is bounded by Hellinger edge energy

Restore the full cube

\[
V=\{-1,+1\}^R,
\qquad |V|=n,
\]

and let `U` be uniform on `V`. For an arbitrary channel `u -> P_u`, write

\[
H_V:=\sum_{e\in E(V)}H^2(P_u,P_v).
\]

We claim

\[
\boxed{
I(U;Y)\le\frac{2}{n}H_V.
}
\tag{20}
\]

Order the independent source bits. The chain rule gives

\[
I(U;Y)
=
\sum_{i=1}^R I(U_i;Y\mid U_{<i}).
\tag{21}
\]

For a fixed prefix `U_<i=a`, the conditional term is the Jensen--Shannon divergence between the two output laws obtained by averaging over the common suffix with `U_i=+1` and `U_i=-1`. By `(17)` this is at most their squared Hellinger distance.

Squared Hellinger distance is an `f`-divergence and is jointly convex. Equivalently, the affinity is jointly concave by the pointwise concavity of the geometric mean. Pairing the two suffix mixtures therefore gives

\[
I(U_i;Y\mid U_{<i})
\le
\frac{2}{n}
\sum_{e\parallel i}H^2(P_u,P_v).
\tag{22}
\]

Summing over coordinates proves `(20)`.

Now puncture the single source state

\[
v_0=(+1,\ldots,+1).
\]

As in `MC-359`, choose one Hamming neighbor `v_1 in S` and extend the channel by `P_{v_0}:=P_{v_1}`. One restored edge has Hellinger cost zero and each of the other `R-1` restored edges has cost at most one, so

\[
H_V
\le
\sum_{e\in E(S)}h_e^2+(R-1).
\tag{23}
\]

With `B=1_{\{U\in S\}}`, conditional on `B=1` the source is exactly `X`, while conditional on `B=0` it is deterministic. Hence

\[
I(U;Y)
\ge
\frac mn I(X;Y).
\tag{24}
\]

Combining `(20)`, `(23)`, and `(24)` proves `(5)`.

## 3. The existing transcript-capacity floor gives the extensive Hellinger tariff

Under hypotheses `(6)`, `MC-340` proves

\[
I(X;Y)
\ge
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-
\operatorname{TC}(X).
\tag{25}
\]

Combining `(25)` with `(5)` and dividing by `R` gives `(7)`. For even rank, `TC(X)->0`, yielding `(8)`.

At matched-filter energy, `MC-340` also gives, when

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\qquad
\theta=\varepsilon-\frac{\varepsilon^2}{2},
\]

that

\[
I(X;Y)\ge\log m-Rh(\theta).
\]

Therefore

\[
\frac{\mathfrak H_1}{R}
\ge
\frac{\log m}{R}
-h(\theta)
-
\frac{2(R-1)}{mR}.
\tag{26}
\]

As `R->infinity` and `epsilon->0`, this lower bound tends to `log 2`, not to one. This is the precise endpoint price of using `(17)`: unlike the TV inequality in `MC-359`, the Hellinger comparison has slack at singularity.

At exact unit-energy dephasing there is no such ambiguity. `MC-340` gives `H(X|Y)=0`, so the conditional output laws for distinct source states are mutually singular. Hence every surviving edge has `h_e^2=1` and exactly

\[
\boxed{
\mathfrak H_1
=R\frac{m-1}{m}.
}
\tag{27}
\]

Thus Hellinger is maximally charged at the exact deterministic endpoint even though the mutual-information lower route alone is not asymptotically sharp as `epsilon->0`.

## 4. Hellinger affinity gives the latent/product decomposition

For one source edge, lift the output law to the joint law

\[
Q_x(d\theta,dy_1\cdots dy_k)
:=
\nu_x(d\theta)
\prod_{j=1}^k K_{x,j}(dy_j\mid\theta),
\tag{28}
\]

and similarly for `x'`. Marginalizing away `Theta` is a Markov map, so squared Hellinger distance contracts:

\[
H^2(P_x,P_{x'})
\le
H^2(Q_x,Q_{x'}).
\tag{29}
\]

This direction can also be seen directly: integrating out a coordinate increases Hellinger affinity by Cauchy--Schwarz.

Conditional product structure makes the joint affinity explicit:

\[
\operatorname{Aff}(Q_x,Q_{x'})
=
\int
\sqrt{r_x(\theta)r_{x'}(\theta)}
\prod_{j=1}^k
\left(1-h_{e,j}^2(\theta)\right)
\,d\kappa(\theta).
\tag{30}
\]

Therefore

\[
\begin{aligned}
H^2(Q_x,Q_{x'})
={}&H^2(\nu_x,\nu_{x'})\\
&+
\int
\sqrt{r_xr_{x'}}
\left[
1-
\prod_{j=1}^k(1-h_{e,j}^2)
\right]
\,d\kappa.
\end{aligned}
\tag{31}
\]

For numbers `z_j in [0,1]`,

\[
1-\prod_j(1-z_j)\le\sum_j z_j.
\tag{32}
\]

Applying `(32)` to `(31)` gives exactly the architecture bound `(12)` with cost `(11)`.

This is the compositional advantage missing from `MC-359`. No coupling has to be chosen after the fact: for genuinely conditionally independent transcript components, Hellinger affinity factorizes automatically. The price is also bounded componentwise, including when some paired component laws are singular.

## 5. Sparse source dependence forces an extensive weighted incidence budget

Assume now the useful special case `nu_x=nu` for every source state. Suppose component `j` depends only on source coordinates in `A_j`. If an edge flips coordinate `i notin A_j`, then the paired conditional component laws agree and its Hellinger cost is zero.

For a fixed coordinate direction of the punctured cube there are exactly

\[
\frac n2-1
=
\frac{m-1}{2}
\]

surviving edges. Under the uniform bound `(14)`, summing `(11)` over edges therefore yields `(15)`.

Combining `(15)` and `(7)` gives the finite-rank admission inequality

\[
\frac{m-1}{mR}
\sum_{j=1}^k\sum_{i\in A_j}\alpha_{j,i}
\ge
\frac{\eta^2}{2C}
-
\frac{1}{2m^2}
-
\frac{\operatorname{TC}(X)}{R}
-
\frac{2(R-1)}{mR}.
\tag{33}
\]

The asymptotic form is `(16)`.

At the exact dephasing endpoint, `(27)` and `mathfrak H_1<=mathfrak A_1` force

\[
\sum_{j=1}^k\sum_{i\in A_j}\alpha_{j,i}\ge R.
\tag{34}
\]

Thus, for example, an architecture with exactly one source-local component per coordinate cannot reach exact dephasing unless every one of those component directions is maximally Hellinger-separated. Overlapping components may redistribute the charge, but cannot make the total weighted incidence sublinear.

## Prior art and novelty boundary

The ingredients used here are classical statistical-information mechanisms. Jensen--Shannon divergence goes back to the standard entropy symmetrization literature; squared Hellinger distance is a classical `f`-divergence; inequalities comparing Jensen--Shannon, Hellinger, and related symmetric divergences have a substantial existing literature; and Hellinger/Bhattacharyya affinity factorization for product measures is standard. A targeted literature audit on 17 September 2026 confirmed that these underlying mechanisms are established prior art.

No novelty is claimed for `(17)`, joint convexity/data processing of Hellinger distance, or the product identity `(30)` in abstract probability theory. They are proved or reduced explicitly above, so no external literature theorem is load-bearing and this finding does not add a source anchor to `SOURCES.md`.

The durable Mathia-specific delta is their composition with the punctured reciprocal source and the already established transcript-capacity floor: `(5)`--`(8)` give a bounded Hellinger source-edge tariff, while `(11)`--`(16)` turn conditional product structure into an architecture-facing latent/component budget. This closes a specific gap between `MC-358`'s KL latent/component split and `MC-359`'s bounded but coupling-facing TV tariff.

## Boundaries and falsification tests

- **Even rank is load-bearing.** The one-vertex puncture argument is the even-rank reciprocal source model. Odd rank needs its own source geometry.
- **Conditional product structure is load-bearing for `(30)`.** Arbitrarily correlated transcript components do not have multiplicative Hellinger affinity. Treating a correlated output as a product is invalid.
- **The common latent coordinate must be genuine.** A source-dependent reparameterization that changes the meaning of `theta` between `x` and `x'` can manufacture or erase component costs. The two kernels must be compared on an actual shared latent state space.
- **Unobserved source paths must be lifted.** If source dependence enters through metadata, branch selection, clocks, seeds, or other hidden state not represented by `Theta` and the `K_j`, the architecture cost `(11)` is incomplete.
- **The bound is one-way.** Large latent/component Hellinger cost does not imply useful dephasing; it is only a necessary resource upper bound for the output separation.
- **Hellinger is not uniformly sharper than TV.** Near singularity the Jensen--Shannon/Hellinger comparison loses the factor visible in `MC-359`; the reason to use Hellinger here is exact affinity factorization and boundedness.
- **A source-independent latent is required for the sparse incidence corollary `(15)`.** If `nu_x` itself moves with the source, its Hellinger term may pay the tariff and must be controlled separately.
- **Coordinate support must be structural, not chosen post hoc.** The sets `A_j` must reflect actual dependence of the conditional component law on source coordinates. A decoder that first reconstructs the whole source and then labels components as local does not satisfy the hypothesis.
- **No arithmetic component decomposition has yet been proved.** To affect the Möbius problem, one still needs an intrinsic Möbius-derived endpoint architecture whose transcript admits a genuine latent/product representation with quantitatively small source-coordinate Hellinger costs, or a theorem showing that the arithmetic construction necessarily incurs the extensive cost.
- **No `M(x)` estimate follows.** Nothing here uses `1/zeta`, contour shifting, a zero-free region, or an RH-scale summatory estimate.

## Dependencies

- `MC-340-global-transcript-information-capacity.md` — supplies the reciprocal endpoint mutual-information lower bounds and exact-dephasing decoder.
- `MC-358-source-dependent-mixture-component-tariff.md` — supplies the adjacent KL latent/component accounting problem and identifies source-dependent components as an architectural resource.
- `MC-359-total-variation-source-edge-tariff.md` — supplies the bounded edge-tariff predecessor and the punctured-cube normalization/coupling comparison.
