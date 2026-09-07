# AF-185 — Gevrey derivative budgets impose logarithmic adaptive-cluster fidelity gates

**Status:** `EXACT-DERIVED`, `GENERAL-THEORY`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-182--AF-184 derive an arithmetic instability mechanism for bounded-band Euler-log observations: positive parity-split generalized-prime clusters can cancel arbitrarily many low-order source moments, and when the cancellation order is allowed to grow with the source spacing, the observed discrepancy can become smaller than every algebraic power of that spacing.

The logarithm in AF-184 is not specific to the Euler product. It is the analytic-order instance of a general derivative-budget law.

Fix a Gevrey order

\[
q\ge 1,
\tag{1}
\]

and a base point `x`. For each sufficiently small `0<\delta<1`, let `\Lambda_\delta` be an observation-index set and let

\[
K_{\delta,\lambda}(u),\qquad \lambda\in\Lambda_\delta,
\tag{2}
\]

be real- or complex-valued smooth observation kernels on one fixed neighborhood `[x,x+r]`, `r>0`. Assume there are constants

\[
C>0,\qquad a_0>0,
\tag{3}
\]

and scales `A_\delta\ge a_0` such that for every integer `m>=1`, every `\lambda\in\Lambda_\delta`, and every `u\in[x,x+r]`,

\[
\boxed{
|\partial_u^m K_{\delta,\lambda}(u)|
\le
C A_\delta^m (m!)^q.
}
\tag{4}
\]

Thus `q=1` is the analytic derivative budget, while `q>1` allows Gevrey growth.

Put

\[
\varepsilon_\delta=A_\delta\delta,
\qquad
L_\delta=\log(1/\delta),
\qquad
\rho_\delta=\varepsilon_\delta L_\delta^q.
\tag{5}
\]

Assume

\[
\boxed{
\rho_\delta
=
A_\delta\delta\,[\log(1/\delta)]^q
\longrightarrow0.
}
\tag{6}
\]

Choose

\[
\boxed{
m_\delta
=
\left\lfloor
L_\delta\,\rho_\delta^{-1/(2q)}
\right\rfloor.
}
\tag{7}
\]

For small enough `\delta`, form the normalized positive parity-split measures

\[
\mu_{+,\delta}-\mu_{-,\delta}
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta}.
\tag{8}
\]

Then:

1. `m_\delta->infinity` and the complete support still collapses to the base point,
   \[
   m_\delta\delta\to0;
   \tag{9}
   \]
2. the controls agree on every polynomial source statistic of degree below `m_\delta`;
3. their source separation remains exactly
   \[
   \boxed{W_1(\mu_{+,\delta},\mu_{-,\delta})=\delta;}
   \tag{10}
   \]
4. if
   \[
   D_\delta
   =
   \sup_{\lambda\in\Lambda_\delta}
   \left|
   \int K_{\delta,\lambda}(u)
   \,d(\mu_{+,\delta}-\mu_{-,\delta})(u)
   \right|,
   \tag{11}
   \]
   then for every fixed `N>0`,
   \[
   \boxed{D_\delta=o(\delta^N).}
   \tag{12}
   \]

Consequently no uniform inverse Hölder estimate

\[
W_1(\mu,\nu)
\le C_0 D(\mu,\nu)^\alpha
\tag{13}
\]

with any fixed `\alpha>0` can hold on a source class containing these adaptive positive clusters.

The reusable gate is therefore

\[
\boxed{
A_\delta\delta\,[\log(1/\delta)]^q\to0
\quad\Longrightarrow\quad
\text{Gevrey-order-}q\text{ observations admit adaptive positive clusters invisible to every inverse power law.}
}
\tag{14}
\]

This is a sufficient instability theorem. It does **not** assert stable recovery when `(14)` fails.

## Derivation

### 1. Finite differences convert derivative growth into observation flatness

For an integer `m>=1`, the forward finite difference satisfies the exact integral identity

\[
\Delta_\delta^m K(x)
=
\int_{[0,\delta]^m}
K^{(m)}(x+u_1+\cdots+u_m)
\,du_1\cdots du_m.
\tag{15}
\]

Whenever the cluster lies inside `[x,x+r]`, `(4)` gives

\[
|\Delta_\delta^m K_{\delta,\lambda}(x)|
\le
C(A_\delta\delta)^m(m!)^q
=
C\varepsilon_\delta^m(m!)^q.
\tag{16}
\]

The normalization in `(8)` therefore yields

\[
D_\delta
\le
C2^{1-m}\varepsilon_\delta^m(m!)^q.
\tag{17}
\]

Using the elementary bound `m!<=m^m`,

\[
\boxed{
D_\delta
\le
2C
\left(
\frac{\varepsilon_\delta m^q}{2}
\right)^m.
}
\tag{18}
\]

This isolates the only competition needed below: increasing cancellation order contributes the `m`-th power, while the regularity class charges the factor `m^q` inside that power.

### 2. The logarithmic Gevrey scale is exactly the order-selection feasibility gate

The adaptive construction needs two asymptotic properties:

\[
\frac{m_\delta}{L_\delta}\to\infty
\tag{19}
\]

so that an exponentially small-in-`m` observation can beat every fixed power `\delta^N=e^{-NL_\delta}`, and

\[
\varepsilon_\delta m_\delta^q\to0
\tag{20}
\]

so that the base in `(18)` tends to zero.

There exists **some** integer sequence `m_\delta` satisfying `(19)`--`(20)` if and only if

\[
\boxed{
\varepsilon_\delta L_\delta^q\to0.
}
\tag{21}
\]

Necessity is immediate:

\[
\varepsilon_\delta L_\delta^q
=
(\varepsilon_\delta m_\delta^q)
\left(\frac{L_\delta}{m_\delta}\right)^q
\to0.
\tag{22}
\]

For sufficiency, use `(7)`. Since `\rho_\delta->0`, the unfloored quantity in `(7)` diverges and

\[
\frac{m_\delta}{L_\delta}
\sim
\rho_\delta^{-1/(2q)}
\to\infty.
\tag{23}
\]

Moreover,

\[
\varepsilon_\delta m_\delta^q
\le
\varepsilon_\delta L_\delta^q\rho_\delta^{-1/2}
=
\sqrt{\rho_\delta}
\to0.
\tag{24}
\]

Thus `(21)` is the sharp threshold for the **existence of adaptive cancellation orders satisfying this generic derivative-envelope proof mechanism**. It is not claimed to be a sharp information-theoretic threshold for every kernel family.

### 3. Every algebraic output scale is defeated

From `(18)` and `(24)`, eventually

\[
D_\delta
\le
2C
\left(
\frac{\sqrt{\rho_\delta}}2
\right)^{m_\delta}.
\tag{25}
\]

Taking logarithms and dividing by `L_\delta`,

\[
\frac{-\log D_\delta}{L_\delta}
\ge
\frac{m_\delta}{L_\delta}
\left(
-\tfrac12\log\rho_\delta+\log2
\right)
-o(1).
\tag{26}
\]

Both factors on the right diverge positively by `(23)` and `\rho_\delta->0`. Hence

\[
\frac{-\log D_\delta}{L_\delta}\to\infty.
\tag{27}
\]

For every fixed `N>0`, `(27)` is exactly

\[
D_\delta=o(e^{-NL_\delta})=o(\delta^N),
\tag{28}
\]

proving `(12)`.

### 4. The adaptive clusters remain local

Because `A_\delta>=a_0`,

\[
\rho_\delta
=A_\delta\delta L_\delta^q
\ge
a_0\delta L_\delta^q.
\tag{29}
\]

Using `(7)`,

\[
m_\delta\delta
\le
\delta L_\delta\rho_\delta^{-1/(2q)}
\le
a_0^{-1/(2q)}
\delta^{1-1/(2q)}L_\delta^{1/2}
\to0.
\tag{30}
\]

So increasing cancellation order is not purchased by spreading the controls over a macroscopic source interval.

### 5. Positivity and exact source distance survive unchanged

The signed measure `(8)` is obtained by splitting one binomial row by sign. Each side has positive coefficients and equal total mass `2^{m_\delta-1}` before normalization. The standard finite-difference identity gives equality of moments of degrees `0,...,m_\delta-1`.

As proved for the same normalized parity split in AF-182, the one-dimensional cumulative-distribution calculation gives exactly

\[
W_1(\mu_{+,\delta},\mu_{-,\delta})=\delta.
\tag{31}
\]

Thus `(12)` is not small merely because the source pair itself collapses faster than first order in its declared metric.

Finally, if `(13)` held for some `\alpha>0`, choose `N>1/\alpha`. Then `(12)` gives

\[
D_\delta^\alpha=o(\delta^{N\alpha})=o(\delta),
\tag{32}
\]

contradicting `(31)` for fixed `C_0`.

## Euler-product specialization

AF-182 gives, for

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+it,
\tag{33}
\]

and `u>=x>0`,

\[
|F_s^{(m)}(u)|
\le
|s|^m(m-1)!
\frac{e^{-\sigma x}}{(1-e^{-\sigma x})^m}.
\tag{34}
\]

On the vertical window `|t|<=T(\delta)`, take

\[
A_\delta
=
\frac{\sqrt{\sigma^2+T(\delta)^2}}
{1-e^{-\sigma x}},
\qquad
q=1,
\qquad
C=e^{-\sigma x}.
\tag{35}
\]

Since `(m-1)!<=m!`, `(4)` holds. The general gate `(14)` becomes, up to the fixed factor `(1-e^{-\sigma x})^{-1}`,

\[
\delta\sqrt{\sigma^2+T(\delta)^2}\log(1/\delta)\to0,
\tag{36}
\]

which is exactly AF-184's adaptive Euler-cluster regime. The order choice `(7)` also reduces to AF-184's `m` scale up to a fixed constant.

Therefore AF-184 is the analytic (`q=1`) arithmetic instance of a broader rule:

\[
\boxed{
\text{derivative factorial exponent }q
\quad\leftrightarrow\quad
\text{logarithmic resolution penalty }[\log(1/\delta)]^q.
}
\tag{37}
\]

The point of `(37)` is not terminology. It predicts how the admissible source complexity must be coupled to resolution before a compression can claim a uniform power-law inverse.

## Prior art and novelty assessment

No novelty is claimed for Gevrey classes, finite-difference derivative estimates, moment-cancelling source pairs, or cluster-size-dependent super-resolution instability.

- Maurice Gevrey, **“Sur la nature analytique des solutions des équations aux dérivées partielles. Premier mémoire,”** *Annales scientifiques de l'École Normale Supérieure* 35 (1918), 129--190, DOI `10.24033/asens.706`, is the foundational source for the regularity scale now carrying his name.
- Luigi Rodino, ***Linear Partial Differential Operators in Gevrey Spaces***, World Scientific (1993), ISBN `9789810208455`, is a standard monograph source for Gevrey derivative-growth classes and their analytic/microlocal setting.
- David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, is classical prior art for severe sub-Rayleigh instability and its dependence on source-complexity restrictions.
- Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, prove sharp clustered-Fourier conditioning bounds whose exponent depends on maximal cluster size.
- Ping Liu and Habib Ammari, **“Super-resolution of positive near-colliding point sources,”** *Information and Inference: A Journal of the IMA* 12(4) (2023), 3087--3111, DOI `10.1093/imaiai/iaad048`, show that positivity does not remove cluster-size-dependent ill-posedness for positive point sources.

A targeted literature audit found strong prior art for every ingredient and for the general principle that cluster complexity controls super-resolution conditioning, but no authoritative source was identified that needs the exact criterion `(21)` in this Arithmetic Fidelity form. That absence is **not** treated as a novelty claim. The durable value here is the exact portable synthesis: once a compression supplies a Gevrey-order derivative envelope, `(21)` gives an immediate adaptive positive-control obstruction, and the Euler theorem AF-184 becomes one checked specialization rather than an isolated arithmetic calculation.

## Boundaries and failure modes

1. **Not a converse recovery theorem.** Failure of `(6)` does not imply stable inversion. The theorem gives a sufficient adaptive-cluster obstruction and an exact feasibility threshold only for the two asymptotic requirements `(19)`--`(20)` used by this derivative-envelope mechanism.

2. **The derivative envelope is a real hypothesis.** A kernel family with better structure, cancellations not visible in the uniform derivative bound, or a different source geometry may behave differently. Conversely, if the effective `A_\delta` is underestimated, the claimed gate is invalid.

3. **Uniform Gevrey constants matter.** The constant `C` is independent of `m`, `\delta`, and `\lambda`, while all allowed scale growth is exposed in `A_\delta`. Hiding additional order-dependent constants inside `C` destroys the conclusion.

4. **The fixed-neighborhood hypothesis prevents a moving-domain loophole.** Equation `(4)` must hold on a neighborhood large enough to contain the complete adaptive cluster. Equation `(30)` verifies that the selected cluster eventually stays inside every fixed `r>0`.

5. **Complexity diverges.** The number of nodes is `m_\delta+1`, and the unnormalized binomial multiplicity mass is `2^{m_\delta-1}`. Fixed support size, bounded multiplicity, entropy constraints, minimum separation, or another source-complexity cap can evade this no-go.

6. **The source metric is normalized `W_1`.** Other metrics or non-normalized counting measures change the comparison scale and therefore the order-selection condition.

7. **No exact collision is asserted.** For every finite `\delta`, the full observation family may distinguish the two controls. The theorem concerns quantitative conditioning and the impossibility of a uniform inverse power law.

8. **`q` classifies the declared derivative budget, not the entire compression category.** Two kernels in the same Gevrey class can have very different exact inverse structure. The result isolates one reusable obstruction, not a complete taxonomy of Gevrey inverse problems.

9. **No RH consequence is asserted.** A concrete arithmetic route must still show that its actual downstream theorem consumes the source metric and observation family used here and that its admissible control class permits the adaptive clusters.

## Consequences for Arithmetic Fidelity

AF-180--AF-184 show that exact injectivity, source scale, observation bandwidth, and source complexity must be declared together for Euler products. AF-185 extracts the reusable regularity law behind that example.

For a future compression, a stable-fidelity audit can now proceed in a precise order: identify the source metric, determine the strongest admissible positive matched clusters, derive the observation kernel's uniform derivative-growth class, expose every scale-dependent factor in `A_\delta`, and compare `A_\delta\delta[\log(1/\delta)]^q` with one. If it tends to zero on an unrestricted-complexity source class, no later argument may assume a uniform inverse Hölder recovery of that source discriminator from the compressed observations.

The theorem also clarifies why a generic statement such as “the observation is smooth” is too weak. **The exact derivative-growth budget controls how quickly adaptive source complexity can manufacture near-collisions.** Analytic observations pay one logarithm; Gevrey order `q` pays `q` logarithmic powers under this mechanism. Any claimed escape must therefore come from a source-complexity restriction, a stronger observation scale, a different metric, or additional structure not captured by the declared Gevrey envelope.