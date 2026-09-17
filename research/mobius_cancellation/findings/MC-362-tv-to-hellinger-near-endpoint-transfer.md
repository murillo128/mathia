# MC-362 — Total variation transfers near-endpoint dephasing to an almost-maximal Hellinger tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-360` gives the bounded compositional Hellinger tariff

\[
I(X;Y)\le \mathfrak H_1+\frac{2(R-1)}m,
\]

but its direct Jensen--Shannon/Hellinger comparison leaves a permanent near-endpoint slack: as the matched-filter dephasing error tends to zero, that route forces only `mathfrak H_1/R >= log 2+o(1)` although the exact endpoint has `mathfrak H_1/R -> 1`.

The sharper binary-entropy capacity curve of `MC-361`, combined with the total-variation edge theorem `MC-359` and the classical TV--Hellinger comparison, removes that artificial gap.

Continue the even-rank reciprocal endpoint notation

\[
m=2^R-1,
\qquad
q_R:=\frac{m-1}{m},
\]

with `X` uniform on the punctured source cube, complete transcript `Y`, neighboring conditional laws `P_x,P_{x'}`, edge total variation

\[
t_e:=\operatorname{TV}(P_x,P_{x'}),
\]

and normalized squared Hellinger distance

\[
z_e:=H^2(P_x,P_{x'})
=1-\operatorname{Aff}(P_x,P_{x'}).
\]

Use the normalized budgets from `MC-359` and `MC-360`,

\[
\mathfrak T_1=\frac2m\sum_{e\in E(S)}t_e,
\qquad
\mathfrak H_1=\frac2m\sum_{e\in E(S)}z_e.
\tag{1}
\]

Then every channel satisfies the exact aggregate transfer inequality

\[
\boxed{
\frac{\mathfrak T_1}{Rq_R}
\le
\sqrt{
\frac{\mathfrak H_1}{Rq_R}
\left(
2-\frac{\mathfrak H_1}{Rq_R}
\right)
}.
}
\tag{2}
\]

Equivalently, with

\[
\Psi(s):=1-\sqrt{1-s^2},
\qquad 0\le s\le1,
\tag{3}
\]

any lower bound

\[
\frac{\mathfrak T_1}{Rq_R}\ge s
\]

forces

\[
\boxed{
\frac{\mathfrak H_1}{R}
\ge
q_R\Psi(s).
}
\tag{4}
\]

Now let

\[
c_R:=\frac{2(R-1)\log2}{m}.
\tag{5}
\]

Under the bounded-energy dephasing hypotheses of `MC-361`,

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad
\tau:=\max\left\{\frac1m,\frac\eta{\sqrt C}\right\},
\tag{6}
\]

that finding gives

\[
I(X;Y)
\ge
H(X)-R h\!\left(\frac{1+\tau}{2}\right).
\tag{7}
\]

`MC-359` gives

\[
I(X;Y)\le (\log2)\mathfrak T_1+c_R.
\tag{8}
\]

Therefore, whenever the hypotheses are consistent, define

\[
s_{R,C,\eta}
:=
\frac{
\left[
H(X)-R h\!\left(\frac{1+\tau}{2}\right)-c_R
\right]_+
}{Rq_R\log2}
\in[0,1].
\tag{9}
\]

Then

\[
\boxed{
\frac{\mathfrak H_1}{R}
\ge
q_R\Psi(s_{R,C,\eta}).
}
\tag{10}
\]

Since `MC-360` proves `mathfrak H_1 <= mathfrak A_1` for its latent/product architecture cost, the same lower bound holds with `mathfrak A_1` in place of `mathfrak H_1`.

The improvement is decisive near matched-filter energy. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\tag{11}
\]

then `MC-361` gives

\[
I(X;Y)\ge \log m-Rh(\varepsilon/2),
\]

so set

\[
s_{R,\varepsilon}
:=
\frac{
\left[
\log m-Rh(\varepsilon/2)-c_R
\right]_+
}{Rq_R\log2}.
\tag{12}
\]

Equation `(10)` becomes

\[
\boxed{
\frac{\mathfrak H_1}{R}
\ge
q_R\left(1-\sqrt{1-s_{R,\varepsilon}^2}\right).
}
\tag{13}
\]

For fixed `epsilon` and even `R -> infinity`,

\[
s_{R,\varepsilon}
\longrightarrow
\left[
1-\frac{h(\varepsilon/2)}{\log2}
\right]_+,
\]

and hence

\[
\boxed{
\liminf_{R\to\infty,\ R\ \mathrm{even}}
\frac{\mathfrak H_1}{R}
\ge
1-
\sqrt{
1-
\left(
1-\frac{h(\varepsilon/2)}{\log2}
\right)^2
}.
}
\tag{14}
\]

In particular the right side tends to `1` as `epsilon -> 0`. Thus near-exact unit-energy dephasing forces an **almost-maximal Hellinger source boundary**, not merely the `log 2` fraction left by the direct linear Hellinger argument in `MC-360`.

Writing

\[
a_\varepsilon:=\frac{h(\varepsilon/2)}{\log2},
\]

the deficit in `(14)` is

\[
\sqrt{2a_\varepsilon-a_\varepsilon^2}
\sim
\sqrt{
\frac{\varepsilon\log(2e/\varepsilon)}{\log2}
}
\qquad(\varepsilon\downarrow0).
\tag{15}
\]

For the source-independent product architecture of `MC-360`, where

\[
\mathfrak A_1
\le
q_R\sum_j\sum_{i\in A_j}\alpha_{j,i},
\tag{16}
\]

we therefore also obtain

\[
\boxed{
\frac1R\sum_j\sum_{i\in A_j}\alpha_{j,i}
\ge
\Psi(s_{R,C,\eta}),
}
\tag{17}
\]

and, in the matched-filter asymptotic regime, the right side tends to one as `epsilon -> 0`. Splitting the transcript into many weak conditionally independent components therefore cannot hide the near-endpoint cost: the aggregate squared-Hellinger source incidence must become almost maximal per source direction.

No estimate for `M(x)` follows. This remains a finite reciprocal-endpoint admission theorem. Its value is to close a metric-conversion slack in the current architecture frontier so that Hellinger tensorization can be used without losing the singular/near-deterministic endpoint.

## 1. Edgewise TV is controlled by Hellinger affinity

Let `P,Q` have densities `p,q` with respect to a common dominating measure and put

\[
z:=H^2(P,Q)=1-\int\sqrt{pq}.
\]

Then Cauchy--Schwarz gives

\[
\begin{aligned}
\operatorname{TV}(P,Q)
&=\frac12\int |\sqrt p-\sqrt q|(\sqrt p+\sqrt q)\\
&\le
\frac12
\left(\int(\sqrt p-\sqrt q)^2\right)^{1/2}
\left(\int(\sqrt p+\sqrt q)^2\right)^{1/2}\\
&=\sqrt{z(2-z)}.
\end{aligned}
\tag{18}
\]

This is the classical probability specialization of the fidelity/trace-distance inequality commonly associated with Fuchs--van de Graaf. The proof above is included because no external theorem is needed for the stored result.

Define

\[
\phi(z):=\sqrt{z(2-z)},
\qquad 0\le z\le1.
\]

It is increasing and strictly concave on `(0,1)`, since

\[
\phi''(z)
=-\frac1{[z(2-z)]^{3/2}}<0.
\tag{19}
\]

The punctured cube has

\[
|E(S)|=\frac{R(m-1)}2.
\tag{20}
\]

Hence the ordinary edge averages are

\[
\bar t
=\frac{\mathfrak T_1}{Rq_R},
\qquad
\bar z
=\frac{\mathfrak H_1}{Rq_R}.
\tag{21}
\]

Averaging `(18)` over edges and applying Jensen to `phi` gives

\[
\bar t
\le
\frac1{|E(S)|}\sum_e\phi(z_e)
\le
\phi(\bar z),
\]

which is `(2)`. Since

\[
\phi(z)^2=1-(1-z)^2,
\]

inverting on `[0,1]` gives `(4)`.

The transfer is sharp as an aggregate inequality when all edge pairs have the same Hellinger cost and saturate the TV--affinity inequality. No such homogeneity is asserted for the arithmetic channel; the point is that no distribution of edge costs can do better than `(2)` at fixed average Hellinger budget.

## 2. Binary posterior entropy sharpens the TV floor before metric conversion

The previous near-endpoint Hellinger bound in `MC-360` used

\[
\operatorname{JS}(P,Q)\le H^2(P,Q)
\]

directly inside the bitwise mutual-information argument. That inequality is locally sharp when neighboring laws are close but has endpoint slack because mutually singular laws satisfy

\[
\operatorname{JS}(P,Q)=\log2,
\qquad
H^2(P,Q)=1.
\]

The new route deliberately avoids paying that slack at every edge. `MC-361` first uses the binary posterior structure of the source to lower-bound the **global** mutual information sharply. `MC-359` then converts that amount of information into a nearly maximal average TV boundary using the endpoint-sharp inequality

\[
\operatorname{JS}(P,Q)\le(\log2)\operatorname{TV}(P,Q).
\]

Only after this global TV requirement is established do we pass from TV to Hellinger with `(2)`. Near singularity the TV--Hellinger relation itself forces Hellinger distance to be near one, so the permanent `log 2` loss disappears.

This order matters. Replacing the direct JS--Hellinger step by another local linear comparison cannot recover the exact endpoint because any coefficient that is sharp near equality of laws need not also be sharp at mutual singularity.

## 3. The compositional consequence is the architecture-facing gain

`MC-360` introduced Hellinger not because its direct mutual-information constant was better than TV, but because affinity factorizes for conditionally independent components and yields the lifted architecture cost `mathfrak A_1`.

Equation `(10)` preserves that benefit while importing the sharper endpoint information from TV. For a source-independent latent law and components with edge costs bounded by `alpha_{j,i}`, `MC-360` proves `(16)`. Combining it with `(10)` yields `(17)`.

Thus a near-exact product architecture has only two possibilities: either a large fraction of source directions create order-one Hellinger change in the component collection, or several weaker component changes accumulate to an order-one total incidence per direction. Merely proliferating many individually tiny components does not reduce the total required sensitivity.

This is still only a necessary-resource statement. It does not show that a concrete Möbius-derived channel has small component Hellinger incidence. The live arithmetic task remains to compute or bound that incidence for an actual source-natural endpoint construction.

## Prior art and novelty boundary

The edgewise inequality `(18)` is classical. A targeted literature check on 18 September 2026 found it as the commuting/probability case of the Fuchs--van de Graaf fidelity/trace-distance inequalities; see C. A. Fuchs and J. van de Graaf, *Cryptographic distinguishability measures for quantum-mechanical states*, IEEE Transactions on Information Theory 45 (1999), 1216--1227, originally arXiv:quant-ph/9712042. Relations among total variation, Hellinger/Bhattacharyya affinity, and binary testing are substantially older in classical statistics.

No novelty is claimed for `(18)`, concavity of `phi`, Jensen's inequality, or the underlying information metrics. No external literature theorem is load-bearing because `(18)`--`(19)` are derived explicitly.

The durable Mathia-specific delta is the composition of three already established reciprocal-endpoint currencies: the sharper binary-entropy information floor of `MC-361`, the endpoint-sharp bounded TV tariff of `MC-359`, and the tensorizing Hellinger architecture cost of `MC-360`. Equations `(10)`--`(17)` remove the near-endpoint `log 2` loss while retaining the compositional upper-theorem surface needed for concrete channel audits.

## Boundaries and falsification tests

- **Even rank is load-bearing.** The normalization and entropy `H(X)=log m` use the punctured full source cube. Odd rank requires its parity-constrained source law to be treated separately.
- **The same complete transcript laws are required.** The TV and Hellinger budgets must be computed from the identical conditional laws `P_x`; metric bounds on different downstream statistics cannot be spliced together.
- **Near-maximal Hellinger is necessary, not sufficient.** Large `mathfrak H_1` or `mathfrak A_1` does not construct dephasing coefficients or imply Mertens cancellation.
- **The architecture lift remains one-sided.** `mathfrak H_1 <= mathfrak A_1`; a large lifted cost may be wasteful and does not imply the output channel actually uses that information efficiently.
- **The product incidence bound inherits every hypothesis of `MC-360`.** Conditional independence, the latent representation, source-independence when used, and the component sensitivity bounds must be genuine properties of the arithmetic architecture rather than a post-hoc factorization.
- **The TV step does not price analog precision.** Distinct deterministic transcript values have TV one regardless of numerical separation. The result closes the Hellinger endpoint slack but does not repair the inverse-precision escape identified in `MC-342`.
- **Finite-rank exactness is stronger at epsilon zero.** At exact unit-energy dephasing `MC-359` and `MC-360` already prove every surviving edge is mutually singular, so `mathfrak T_1=mathfrak H_1=Rq_R` exactly. Equation `(13)` is chiefly the quantitative near-endpoint bridge.
- **No arithmetic upper bound has been supplied.** The next substantive step must still expose a concrete Möbius-derived channel for which the shared-seed TV change probability, Hellinger component incidence, Jeffreys/Fisher action, or another source-native discrimination cost can be bounded independently of the dephasing target.
- **No RH input is used.** The argument is finite, information-theoretic, and contains no use of `1/zeta`, contour shifting, zero-free regions, or an RH-scale estimate for `M(x)`.