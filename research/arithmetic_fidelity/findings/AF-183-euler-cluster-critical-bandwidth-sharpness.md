# AF-183 — Euler-cluster critical bandwidth is sharp for the parity-split control

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-182 proved that an order-`m` positive parity-split generalized-prime cluster can have normalized source separation `W_1=delta` while its bounded-band Euler-log discrepancy is only `O(delta^m T^m)`. It followed that this explicit control remains a Lipschitz obstruction whenever

\[
T(\delta)=o\!\left(\delta^{-(m-1)/m}\right).
\]

That exponent is not an artifact of the upper bound. For the same control it is the exact transition scale at which the Euler observation becomes comparable to its `W_1` source separation.

Fix

\[
m\ge2,\qquad x>0,\qquad \sigma>0,
\]

and let `mu_+(delta),mu_-(delta)` be the normalized parity-split measures of AF-182,

\[
\mu_+-\mu_-
=
2^{1-m}\sum_{j=0}^{m}(-1)^{m-j}\binom mj\delta_{x+j\delta}.
\tag{1}
\]

Write

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+it,
\tag{2}
\]

and define

\[
D_T(\delta)
=
\sup_{|t|\le T}
\left|
\int F_{\sigma+it}(u)\,d(\mu_+-\mu_-)(u)
\right|.
\tag{3}
\]

AF-182 gives exactly

\[
W_1(\mu_+,\mu_-)=\delta.
\tag{4}
\]

Now let the bandwidth satisfy

\[
T=T(\delta)\to\infty,
\qquad
T(\delta)\,\delta\to0.
\tag{5}
\]

Define the positive constant

\[
A_m(\sigma,x)
=
\sum_{k\ge1}k^{m-1}e^{-k\sigma x}.
\tag{6}
\]

Then

\[
\boxed{
D_T(\delta)
=
2^{1-m}A_m(\sigma,x)\,\delta^m T^m\,(1+o(1)).
}
\tag{7}
\]

Consequently,

\[
\boxed{
\frac{D_T(\delta)}{W_1(\mu_+,\mu_-)}
=
2^{1-m}A_m(\sigma,x)\,\delta^{m-1}T^m\,(1+o(1)).
}
\tag{8}
\]

In particular, if

\[
T(\delta)\,\delta^{(m-1)/m}\longrightarrow c\in[0,\infty),
\tag{9}
\]

then

\[
\boxed{
\frac{D_T(\delta)}{W_1(\mu_+,\mu_-)}
\longrightarrow
2^{1-m}A_m(\sigma,x)c^m.
}
\tag{10}
\]

Thus this matched cluster has three regimes inside the small-phase window `T delta ->0`:

1. `T=o(delta^{-(m-1)/m})`: the output/source ratio tends to zero, reproducing the AF-182 obstruction;
2. `T asymp delta^{-(m-1)/m}`: the ratio is order one and the control ceases to certify loss of a uniform lower-Lipschitz scale;
3. `delta^{-(m-1)/m} << T << delta^{-1}`: the ratio grows, so this particular cancellation is already resolved before the usual reciprocal-separation phase scale `1/delta` is reached.

The reusable conclusion is therefore sharper than the one-way gate in AF-182:

\[
\boxed{
\text{for a fixed order-}m\text{ moment-cancelling Euler cluster, }
T_c(\delta)\asymp\delta^{-(m-1)/m}
\text{ is the sharp bandwidth scale for }W_1\text{-level visibility.}
}
\tag{11}
\]

This is a sharpness statement for one explicit matched family, not a global stable-inversion theorem.

## Derivation

AF-182 gives the exact Fourier-Laplace representation

\[
\Delta_\delta^mF_s(x)
=
\sum_{k\ge1}\frac{e^{-ksx}}k
\left(e^{-ks\delta}-1\right)^m,
\tag{12}
\]

with

\[
D_T(\delta)
=
2^{1-m}\sup_{|t|\le T}
|\Delta_\delta^mF_{\sigma+it}(x)|.
\tag{13}
\]

Put

\[
z=s\delta
\]

and

\[
h(w)=\frac{e^{-w}-1}{-w},
\qquad h(0)=1.
\tag{14}
\]

Then `(12)` becomes

\[
\Delta_\delta^mF_s(x)
=
(-z)^m
\sum_{k\ge1}
 k^{m-1}e^{-ksx}h(kz)^m.
\tag{15}
\]

Under `(5)`,

\[
\sup_{|t|\le T}|z|
\le
\delta\sqrt{\sigma^2+T^2}
\longrightarrow0.
\tag{16}
\]

The series in `(15)` therefore has the uniform approximation

\[
\sum_{k\ge1}
 k^{m-1}e^{-ksx}h(kz)^m
=
\sum_{k\ge1}k^{m-1}e^{-ksx}+o(1)
\tag{17}
\]

for `|t|<=T`. To justify uniformity, split the sum at a fixed `K`. On `k<=K`, `h(kz)->1` uniformly by `(16)`. For the tail use

\[
|h(w)|\le e^{|w|},
\]

and choose `delta` so small that `m|z|<=sigma x/2`; then the tail is dominated by the summable sequence

\[
k^{m-1}e^{-k\sigma x/2}.
\]

Since

\[
\left|
\sum_{k\ge1}k^{m-1}e^{-k(\sigma+it)x}
\right|
\le A_m(\sigma,x),
\tag{18}
\]

relations `(15)`--`(18)` give the upper bound

\[
\sup_{|t|\le T}
|\Delta_\delta^mF_{\sigma+it}(x)|
\le
A_m(\sigma,x)\,\delta^m(\sigma^2+T^2)^{m/2}(1+o(1)).
\tag{19}
\]

Because `T->infinity`, `(19)` is

\[
\le A_m(\sigma,x)\delta^mT^m(1+o(1)).
\tag{20}
\]

For the matching lower bound, choose the largest nonnegative frequency below `T` that phase-aligns every Euler harmonic at the base point `x`:

\[
t_\delta
=
\frac{2\pi}{x}
\left\lfloor\frac{xT}{2\pi}\right\rfloor.
\tag{21}
\]

Then

\[
t_\delta\le T,
\qquad
\frac{t_\delta}{T}\to1,
\qquad
 e^{-ik t_\delta x}=1
\quad(k\ge1).
\tag{22}
\]

At `s_delta=sigma+i t_delta`, equation `(17)` therefore becomes

\[
\sum_{k\ge1}
 k^{m-1}e^{-ks_\delta x}h(ks_\delta\delta)^m
=
A_m(\sigma,x)+o(1).
\tag{23}
\]

Moreover,

\[
|s_\delta|^m\delta^m
=T^m\delta^m(1+o(1)).
\tag{24}
\]

Substituting `(23)`--`(24)` into `(15)` yields

\[
|\Delta_\delta^mF_{s_\delta}(x)|
=
A_m(\sigma,x)\delta^mT^m(1+o(1)),
\tag{25}
\]

which matches `(20)`. Equations `(13)` and `(25)` prove `(7)`, and `(4)` then gives `(8)`--`(10)`.

## Exact controls

### The source pair remains positive

Nothing in the sharpness argument replaces AF-182's admissibility construction. Before probability normalization, each side of `(1)` is a positive generalized-prime multiset with integer binomial multiplicities. The signed finite difference arises only by subtracting two legitimate positive systems.

### The critical scale is weaker than full phase separation

At the critical bandwidth

\[
T\asymp\delta^{-(m-1)/m},
\]

one still has

\[
T\delta\asymp\delta^{1/m}\to0.
\]

Thus the order-one ratio in `(10)` does not come from resolving adjacent generators by an `O(1)` relative phase. It comes from amplifying the first nonvanishing `m`-th response until its `delta^mT^m` size matches the source metric `W_1=delta`.

This distinction matters. The reciprocal-separation scale `T asymp 1/delta` remains the natural scale for direct phase separation, but it is stronger than what is needed merely to make this fixed-order cancellation visible at its declared `W_1` scale.

### Unbounded cluster order still drives the gate toward reciprocal separation

For fixed `m`, the exponent is `(m-1)/m`. As `m->infinity`,

\[
\frac{m-1}{m}\uparrow1.
\]

Hence AF-182's unrestricted-cluster conclusion survives intact: if the source class permits arbitrarily high moment-cancellation order, the critical bandwidths approach the reciprocal-separation scale. AF-183 only closes the sharpness question for each fixed order.

## Prior art and novelty assessment

No novelty is claimed for clustered Fourier super-resolution or for cluster-size-dependent polynomial conditioning.

- David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, established the classical sparse super-resolution setting and the deterioration of stable recovery below the nominal Fourier resolution scale.
- Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, prove sharp smallest-singular-value bounds whose polynomial exponent is controlled by the maximal cluster size. This is direct prior art for the principle that cluster order determines the power of the super-resolution factor.
- Dmitry Batenkov, Gil Goldman, and Yosef Yomdin, **“Super-Resolution of Near-Colliding Point Sources,”** *Information and Inference: A Journal of the IMA* 10(2) (2021), 515--572, DOI `10.1093/imaiai/iaaa005`, gives cluster-size-dependent minimax recovery rates for near-colliding sources.

The exact residual established here is the Euler-kernel specialization needed by this line: for AF-182's positive parity-split generalized-prime controls, the bounded vertical Euler-log discrepancy has the explicit asymptotic `(7)`, and the previously derived necessary exponent `(m-1)/m` is therefore attained as the exact `W_1`-visibility threshold for that family. This specialization is recorded as `NO-NOVELTY-CLAIM` and should be read as a calibrated arithmetic instance of the classical clustered-super-resolution mechanism.

## Boundaries and failure modes

1. **Not a global inverse theorem.** At or above the critical scale, this particular matched cluster stops forcing a vanishing lower-Lipschitz ratio. Other controls can still make Euler inversion unstable.

2. **The theorem is pre-Rayleigh.** Equation `(7)` assumes `T delta ->0`. It deliberately studies the derivative-amplification regime before direct phase separation. It does not describe the nonlinear transition near `T delta asymp1` or full-band behavior.

3. **The metric fixes the exponent.** The threshold is defined by comparing output to normalized `W_1=delta`. A different source metric, normalization, or output norm changes the matching condition.

4. **Cluster order is fixed while `delta->0`.** Letting `m` grow with `delta` requires uniform control of `A_m`, the finite-difference remainder, and the binomial normalization. No such joint asymptotic is claimed.

5. **Phase alignment uses the fixed base coordinate.** The lower bound chooses frequencies with `t x` an integer multiple of `2pi`. This is legal for the declared supremum observation, but a discretely sampled frequency set or externally fixed sampling grid would require a separate Diophantine/aliasing analysis.

6. **No RH consequence is asserted.** The result calibrates how much bandwidth is needed to defeat one positive generalized-prime collision mechanism before a downstream argument can claim stable arithmetic provenance.

## Consequences for Arithmetic Fidelity

AF-180 and AF-181 isolated amplitude and pairwise phase resources. AF-182 added cluster complexity and proved a one-way bandwidth obstruction. AF-183 closes the remaining calibration for that explicit family: **the cluster-order exponent is sharp, and the required bandwidth is determined by the scale at which the first surviving derivative becomes as large as the declared source discrepancy.**

This suggests a more precise audit rule for future compressions. For a smooth observation kernel and a matched source pair annihilating the first `m-1` source moments, do not automatically demand full reciprocal-separation resolution. First identify the source metric scale and the first nonzero derivative order; the relevant visibility gate is where the surviving derivative response matches that source scale. Only if cancellation order is unbounded does this family of gates itself converge toward full reciprocal-separation bandwidth.