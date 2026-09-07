# AF-184 — Adaptive Euler clusters remain super-algebraically invisible below a logarithmic Rayleigh scale

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-182 constructs, for every fixed order `m`, two positive parity-split generalized-prime clusters whose normalized source separation is exactly first order in the node spacing while their bounded-band Euler-log discrepancy vanishes to order `m`. AF-183 then proves the sharp visibility scale for each **fixed** `m`, but explicitly leaves open the joint regime in which the cluster order grows as the spacing shrinks.

The fixed-order statement cannot simply be sent to `m -> infinity`: the derivative constant grows factorially with `m`. Nevertheless, the exact uniform bound from AF-182 is strong enough to give a rigorous joint obstruction.

Fix

\[
x>0,\qquad \sigma>0,
\]

and for `0<\delta<1` let the observed vertical bandwidth be `T=T(\delta)>=0`. Put

\[
S_\delta=\sqrt{\sigma^2+T(\delta)^2},
\qquad
\varepsilon_\delta=\delta S_\delta,
\qquad
L_\delta=\log(1/\delta).
\tag{1}
\]

Assume

\[
\boxed{
\varepsilon_\delta L_\delta\longrightarrow0.
}
\tag{2}
\]

When `T(\delta)->infinity`, this is equivalent to

\[
T(\delta)
=o\!\left(\frac1{\delta\log(1/\delta)}\right).
\tag{3}
\]

Choose the cluster order adaptively by

\[
\boxed{
m_\delta
=\left\lfloor
\sqrt{\frac{L_\delta}{\varepsilon_\delta}}
\right\rfloor.
}
\tag{4}
\]

For sufficiently small `\delta`, `m_\delta>=2`. Let `\mu_{+,\delta}` and `\mu_{-,\delta}` be the normalized parity-split probability measures from AF-182 at order `m_\delta`:

\[
\mu_{+,\delta}-\mu_{-,\delta}
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta}.
\tag{5}
\]

Write

\[
F_s(u)=-\log(1-e^{-su}),
\qquad
s=\sigma+it,
\tag{6}
\]

and define the observed discrepancy

\[
D_\delta
=
\sup_{|t|\le T(\delta)}
\left|
\int F_{\sigma+it}(u)
\,d(\mu_{+,\delta}-\mu_{-,\delta})(u)
\right|.
\tag{7}
\]

Then all of the following hold.

### 1. The source separation remains exactly first order

For every `\delta`, AF-182 gives

\[
\boxed{
W_1(\mu_{+,\delta},\mu_{-,\delta})=\delta.
}
\tag{8}
\]

The controls also agree on every polynomial log-coordinate statistic of degree below `m_\delta`.

### 2. The whole cluster still collapses to one local source point

Although the cancellation order diverges,

\[
m_\delta\longrightarrow\infty,
\tag{9}
\]

its support diameter satisfies

\[
\boxed{
m_\delta\delta\longrightarrow0.}
\tag{10}
\]

Thus the construction does not obtain increasing cancellation by spreading over a macroscopically larger source interval. Both positive controls concentrate into the same shrinking neighborhood of `x`.

### 3. Euler-log discrepancy becomes smaller than every algebraic power

For every fixed `N>0`,

\[
\boxed{
D_\delta=o(\delta^N).
}
\tag{11}
\]

Hence the same local positive-control family is **super-algebraically indistinguishable** in the declared bounded-band Euler-log metric, despite having exact source distance `\delta`.

In particular, for every `\alpha>0` there is no uniform inverse Hölder estimate

\[
W_1(\mu,\nu)
\le C D(\mu,\nu)^\alpha
\tag{12}
\]

on any source class containing these adaptive-order clusters for all sufficiently small `\delta`.

Therefore the fixed-order gates of AF-183 can be combined into a genuine growing-order no-go, but only after paying attention to the factorial growth of the Euler derivatives:

\[
\boxed{
\delta\sqrt{\sigma^2+T(\delta)^2}\log(1/\delta)\to0
\quad\Longrightarrow\quad
\text{adaptive positive Euler clusters defeat every uniform inverse power law.}
}
\tag{13}
\]

This is a sufficient obstruction regime, not a sharp joint `m`--`\delta`--`T` threshold.

## Derivation

AF-182 proves, for every finite order `m`,

\[
D_T
\le
2^{1-m}\delta^m S_T^m(m-1)!
\frac{e^{-\sigma x}}{(1-e^{-\sigma x})^m}.
\tag{14}
\]

Set

\[
r=e^{-\sigma x},
\qquad
B=\frac1{2(1-r)}.
\tag{15}
\]

With `\varepsilon=\delta S_T`, equation `(14)` becomes

\[
\boxed{
D_T\le 2r(B\varepsilon)^m(m-1)!.
}
\tag{16}
\]

This form exposes the joint-order issue. Higher finite-difference cancellation contributes `\varepsilon^m`, but the analytic derivative budget contributes `(m-1)!`.

Now specialize to `(1)`--`(4)`. Condition `(2)` implies

\[
\varepsilon_\delta\to0,
\qquad
m_\delta\to\infty,
\tag{17}
\]

and

\[
m_\delta\varepsilon_\delta
\le
\sqrt{L_\delta\varepsilon_\delta}
\longrightarrow0.
\tag{18}
\]

Using the elementary bound

\[
(m-1)!\le m^m,
\tag{19}
\]

we obtain

\[
D_\delta
\le
2r\left(Bm_\delta\varepsilon_\delta\right)^{m_\delta}.
\tag{20}
\]

Put

\[
a_\delta
=-\log\!\left(B\sqrt{L_\delta\varepsilon_\delta}\right).
\tag{21}
\]

By `(2)`, `a_\delta->infinity`, and `(18)` gives, eventually,

\[
D_\delta\le 2r e^{-m_\delta a_\delta}.
\tag{22}
\]

Since the quantity under the floor in `(4)` diverges, eventually

\[
m_\delta
\ge
\frac12\sqrt{\frac{L_\delta}{\varepsilon_\delta}}.
\tag{23}
\]

Consequently,

\[
\frac{m_\delta a_\delta}{L_\delta}
\ge
\frac{a_\delta}{2\sqrt{L_\delta\varepsilon_\delta}}
\longrightarrow\infty.
\tag{24}
\]

For any fixed `N>0`, equation `(24)` eventually gives

\[
m_\delta a_\delta>(N+1)L_\delta.
\tag{25}
\]

Substituting into `(22)`,

\[
D_\delta
\le
2r\,\delta^{N+1}
=o(\delta^N),
\tag{26}
\]

proving `(11)`.

To prove the locality statement, `(4)` gives

\[
m_\delta\delta
\le
\delta\sqrt{\frac{L_\delta}{\delta S_\delta}}
=
\sqrt{\frac{\delta L_\delta}{S_\delta}}
\le
\sqrt{\frac{\delta L_\delta}{\sigma}}
\longrightarrow0,
\tag{27}
\]

which proves `(10)`.

Finally, suppose `(12)` held for some `\alpha>0`. Choose `N>1/\alpha`. By `(11)`,

\[
D_\delta^\alpha=o(\delta^{N\alpha})=o(\delta),
\tag{28}
\]

while `(8)` says the left side of `(12)` is exactly `\delta`. This is impossible for fixed `C`, proving the all-Hölder obstruction.

## Exact controls

### Positivity is preserved at every adaptive order

For each finite `m_\delta`, the two sides of `(5)` arise by splitting the binomial row according to parity of the sign. Before probability normalization, each side is a positive generalized-prime multiset with integer multiplicities and total mass

\[
2^{m_\delta-1}.
\tag{29}
\]

The signed finite difference appears only after subtracting those two legitimate positive systems. As in AF-182, a common sufficiently sparse tail can be appended to embed each finite block into an infinite Beurling generalized-prime system.

### Complexity is the resource that creates the stronger cancellation

The number of distinct cluster nodes is `m_\delta+1`, while the unnormalized multiplicity mass grows as `2^{m_\delta-1}`. The theorem therefore does not apply to source classes with a fixed support-size, multiplicity, entropy, or cluster-order budget.

The normalized probability formulation isolates geometric recovery from this exploding multiplicity. In the unnormalized equal-mass multisets, both the observation discrepancy and the Wasserstein transport cost acquire the same factor `2^{m_\delta-1}`, so the conditioning ratio is unchanged.

### The logarithm is not an arbitrary technical artifact

AF-183's fixed-order critical exponents approach the Rayleigh exponent `1` as `m` grows, but that observation alone ignores how the constants depend on `m`. Equation `(16)` shows the relevant competition explicitly:

\[
\text{finite-difference gain }\varepsilon^m
\quad\text{versus}\quad
\text{derivative growth }(m-1)!.
\tag{30}
\]

To defeat every source power `\delta^N`, one needs an order much larger than `L_\delta` while still keeping `m\varepsilon` small. Such an order exists under `(2)`. This is why the present proof reaches the logarithmically sub-Rayleigh regime `(3)` rather than automatically proving the same conclusion for every schedule with `T\delta->0`.

## Prior art and novelty assessment

No novelty is claimed for cluster-size-dependent super-resolution instability, moment-cancelling source pairs, or exponential deterioration with growing cluster size.

- David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, established the classical sparse super-resolution setting and its severe sub-Rayleigh instability.
- Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, prove sharp bounds in which the power of the super-resolution factor is controlled by the largest cluster size.
- Dmitry Batenkov and Gil Goldman, **“Single-exponential bounds for the smallest singular value of Vandermonde matrices in the sub-Rayleigh regime,”** arXiv:`2107.09326` (2021), show that clustered Vandermonde conditioning can deteriorate single-exponentially in the largest cluster size even at arbitrarily small minimum separation.
- Ping Liu and Habib Ammari, **“Super-resolution of positive near-colliding point sources,”** *Information and Inference: A Journal of the IMA* 12(4) (2023), 3087--3111, DOI `10.1093/imaiai/iaad048`, show that positivity does not remove the cluster-size-dependent minimax ill-posedness for positive point sources.

These results are strong prior art for the underlying growing-cluster phenomenon. The exact residual recorded here is narrower: the Euler kernel and AF-182's positive parity-split generalized-prime controls give a direct arithmetic instance in which the existing factorial derivative bound can be optimized jointly with cluster order to produce `(11)`--`(13)`. The result is therefore recorded as `NO-NOVELTY-CLAIM`; its value is the explicit recovery gate it supplies for this line, not a claim that growing-cluster super-resolution instability is new.

## Boundaries and failure modes

1. **Not a sharp bandwidth threshold.** The theorem proves an obstruction under `\varepsilon_\delta L_\delta->0`. It does not prove stable recovery when this condition fails.

2. **A logarithmic window remains open.** This construction and bound do not settle schedules in the region
   \[
   \frac1{\delta\log(1/\delta)}
   \lesssim T(\delta)\ll\frac1\delta.
   \]
   In particular, AF-183's fixed-order sharpness cannot be used to close that joint-order window without new uniform analysis.

3. **Cluster complexity diverges.** The conclusion is a no-go for unrestricted-order classes. A fixed support-size, fixed multiplicity, minimum-separation, bounded-entropy, or other complexity hypothesis can evade it.

4. **The source metric is normalized `W_1`.** Other metrics or normalizations can change the comparison scale. The finding does not claim a metric-free instability theorem.

5. **No exact collision is asserted.** For every finite `\delta` and `m_\delta`, the complete analytic observations may still distinguish the controls exactly. The result concerns asymptotic recovery regularity under the declared bandwidth schedule.

6. **No RH consequence is asserted.** The result is a quantitative admissibility test for any later mechanism that expects bounded-band Euler data to preserve rational-prime provenance uniformly across increasingly complicated local source alternatives.

## Consequences for Arithmetic Fidelity

AF-180 and AF-181 isolated scale attenuation, half-plane access, and pairwise phase resolution. AF-182 showed arbitrary finite-order cancellation, and AF-183 calibrated every fixed order sharply. AF-184 adds the missing joint-order lesson: **unbounded cancellation order can be converted into super-algebraic invisibility only after the growth of the recovery constants is audited at the same time.**

That changes the reusable audit rule. A family of fixed-complexity thresholds approaching a limiting scale is not, by itself, evidence for a uniform threshold on an unbounded-complexity class. One must carry the complexity-dependent constants through the limit. For the present Euler family, doing so certifies all-power-law failure up to the logarithmically sub-Rayleigh bandwidth `(3)`, while leaving the final logarithmic gap to reciprocal separation as a precise open problem rather than hiding it behind the formal limit `m->infinity`.