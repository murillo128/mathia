# AF-181 — Euler-product half-plane recovery has independent edge and bandwidth gates

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-180 fixed one vertical line `Re(s)=sigma>1` and showed that exact Euler-product fidelity can still be badly conditioned: high-scale generator changes are attenuated by `p^{-sigma}`, while resolving a unit norm displacement in phase requires vertical frequency of order `p`.

Allowing the observer to use an entire right half-strip reveals that these are **two independent recovery resources**. Moving left toward the absolute-convergence boundary repairs the Laplace-amplitude loss only on a logarithmic horizontal scale, while increasing vertical bandwidth repairs the phase-resolution loss only on the reciprocal frequency-separation scale.

Let `p>=3` be an odd rational prime, put

\[
q=p+1,
\qquad
\delta_p=\log(q/p)=\log(1+1/p),
\tag{1}
\]

and let `\mathcal P` be the ordinary rational-prime norm system while `\mathcal Q_p` replaces the single generator `p` by the composite generator `q` and leaves every other generator unchanged. In `Re(s)>1`, write

\[
P_{\mathcal P}(s)=\sum_r r^{-s},
\qquad
Z_{\mathcal P}(s)=\zeta(s),
\tag{2}
\]

with the analogous generalized-prime objects for `\mathcal Q_p`. Use the analytic Euler logarithm on the absolute-convergence half-plane.

For a left edge `sigma_0>1` and vertical bandwidth `0<=T<=infinity`, define

\[
H_{\sigma_0,T}
=
\{s=\sigma+it:\sigma\ge\sigma_0,\ |t|\le T\},
\tag{3}
\]

and

\[
D^P_{\sigma_0,T}(p)
=
\sup_{s\in H_{\sigma_0,T}}
|P_{\mathcal Q_p}(s)-P_{\mathcal P}(s)|,
\tag{4}
\]

\[
D^Z_{\sigma_0,T}(p)
=
\sup_{s\in H_{\sigma_0,T}}
|\log Z_{\mathcal Q_p}(s)-\log\zeta(s)|.
\tag{5}
\]

Then the following hold.

### 1. The prime-sum half-strip supremum is attained on its left edge

For every `sigma_0>1`,

\[
\boxed{
D^P_{\sigma_0,T}(p)
=
p^{-\sigma_0}
\left[
(1-r_p)^2
+4r_p\sin^2\!\left(
\frac{\min\{T\delta_p,\pi\}}2
\right)
\right]^{1/2},
}
\tag{6}
\]

where

\[
r_p=e^{-\sigma_0\delta_p}=(p/q)^{\sigma_0}.
\tag{7}
\]

Thus expanding the observation from one vertical line to the whole half-strip to its right does not buy any additional first-order generator contrast. The useful horizontal direction is toward the convergence edge, not further into the half-plane.

### 2. Euler logarithms have the same leading half-strip profile

For finite `T`, the higher prime-power remainder satisfies the sharper cancellation bound

\[
\boxed{
|D^Z_{\sigma_0,T}(p)-D^P_{\sigma_0,T}(p)|
\le
\frac{\sqrt{\sigma_0^2+T^2}\,p^{-2\sigma_0-1}}
{1-p^{-\sigma_0}}.
}
\tag{8}
\]

For arbitrary bandwidth, including `T=infinity`, one always has the uniform bound

\[
\boxed{
|D^Z_{\sigma_0,T}(p)-D^P_{\sigma_0,T}(p)|
\le
\frac{p^{-2\sigma_0}}{1-p^{-\sigma_0}}
+
\frac{q^{-2\sigma_0}}{1-q^{-\sigma_0}}.
}
\tag{9}
\]

The fixed-line remainder estimate of AF-180 therefore remains lower order after taking the whole right half-strip, and `(8)` shows that at bounded bandwidth the cancellation from moving only one nearby generator is one additional power of `p` better than the crude separate-tail estimate.

### 3. The entire absolute-convergence half-plane still has two different stability regimes

Let

\[
D^\bullet_{>1,T}(p)
=
\sup_{\sigma>1,\ |t|\le T}(\cdots)
\tag{10}
\]

denote the corresponding supremum over the open absolute-convergence half-plane. For each fixed finite `T`,

\[
\boxed{
D^Z_{>1,T}(p)
=
\sqrt{1+T^2}\;p^{-2}
\left(1+O_T(p^{-1})\right).
}
\tag{11}
\]

With unlimited vertical bandwidth,

\[
\boxed{
D^Z_{>1,\infty}(p)
=
\frac1p+\frac1{p+1}+O(p^{-2})
=
2p^{-1}+O(p^{-2}).
}
\tag{12}
\]

Hence access to every `sigma>1` removes the fixed-`sigma` amplitude exponent from AF-180 only when the observer also has enough vertical frequency to resolve the nearby log-frequencies. At fixed bandwidth the discrepancy remains one full additional factor `p^{-1}` smaller.

### 4. Moving left edge and moving bandwidth give a sharp two-parameter gate

Let

\[
\sigma_p=1+\varepsilon_p>1,
\qquad
T_p\ge0,
\tag{13}
\]

with `sigma_p delta_p ->0`, which includes every regime in which `varepsilon_p=o(p)`. If

\[
T_p\delta_p\longrightarrow\tau\in(0,\infty],
\tag{14}
\]

then

\[
\boxed{
D^Z_{\sigma_p,T_p}(p)
=
2p^{-\sigma_p}
\sin\!\left(\frac{\min\{\tau,\pi\}}2\right)
(1+o(1)).
}
\tag{15}
\]

If instead `T_p delta_p ->0`, then

\[
\boxed{
D^Z_{\sigma_p,T_p}(p)
=
p^{-\sigma_p}\delta_p
\sqrt{\sigma_p^2+T_p^2}
(1+o(1)).
}
\tag{16}
\]

For the natural logarithmic source displacement

\[
d_{\log}(\mathcal P,\mathcal Q_p)=\delta_p\sim p^{-1},
\tag{17}
\]

equation `(15)` gives

\[
\boxed{
\frac{D^Z_{\sigma_p,T_p}(p)}{d_{\log}(\mathcal P,\mathcal Q_p)}
=
2p^{-\varepsilon_p}
\sin\!\left(\frac{\min\{\tau,\pi\}}2\right)
(1+o(1)).
}
\tag{18}
\]

This isolates two independent necessary gates for this matched control not to destroy uniform local Lipschitz recovery in logarithmic generator geometry:

- **bandwidth gate:** `T_p` must be of order `p`, equivalently `T_p delta_p` must not tend to zero;
- **edge gate:** the observation edge must approach `Re(s)=1` on the scale `varepsilon_p=O(1/log p)`, equivalently `varepsilon_p log p` must not tend to infinity.

Indeed, if either

\[
T_p/p\to0
\tag{19}
\]

or, after phase resolution,

\[
\varepsilon_p\log p\to\infty,
\tag{20}
\]

then

\[
\frac{D^Z_{\sigma_p,T_p}(p)}{d_{\log}(\mathcal P,\mathcal Q_p)}\to0,
\tag{21}
\]

so no uniform inverse Lipschitz estimate can hold along these controls.

Conversely, if `T_p/p->c>0` and `varepsilon_p log p->a<infinity`, then this particular control has a nonzero limiting output/source ratio

\[
2e^{-a}\sin\!\left(\frac{\min\{c,\pi\}}2\right)
\tag{22}
\]

when `c` is interpreted through `T_p delta_p->c`. This is **not** a global inverse theorem; it says only that the unit-shift control ceases to be a Lipschitz obstruction once both resources scale correctly.

### 5. No amount of half-plane data repairs the unweighted absolute source geometry

In the unweighted generator bottleneck metric,

\[
d_{\rm abs}(\mathcal P,\mathcal Q_p)=|q-p|=1.
\tag{23}
\]

But `(12)` gives

\[
D^Z_{>1,\infty}(p)\to0.
\tag{24}
\]

Therefore there is no uniform inverse modulus `omega(u)->0` with

\[
d_{\rm abs}
\le
\omega(D^Z_{>1,\infty})
\tag{25}
\]

on this matched family. Even observing the **entire absolute-convergence half-plane with unlimited vertical bandwidth** does not make exact Euler-product inversion uniformly continuous in absolute generator geometry.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{exact half-plane Euler data are qualitatively norm-faithful, but stable recovery is metric- and resource-dependent;}\\
\text{vertical bandwidth resolves log-frequency separation at scale }T\delta_p\asymp1;\\
\text{horizontal access counters Laplace attenuation only when }(\sigma-1)\log p=O(1);\\
\text{neither resource substitutes for the other.}
\end{array}}
\tag{26}
\]

## Derivation

### The left edge dominates the prime-sum half-strip

For `s=\sigma+it`, the single changed term is

\[
q^{-s}-p^{-s}.
\tag{27}
\]

Put

\[
a=\log p,
\qquad
b=\log q,
\qquad
x=e^{-\sigma(b-a)}=(p/q)^\sigma,
\qquad
\theta=t\delta_p.
\tag{28}
\]

Then

\[
|q^{-s}-p^{-s}|^2
=e^{-2a\sigma}
\left(1+x^2-2x\cos\theta\right).
\tag{29}
\]

Differentiating with respect to `sigma` and dividing by the positive factor `2e^{-2a sigma}` gives

\[
-a-bx^2+(a+b)x\cos\theta.
\tag{30}
\]

This is largest when `cos(theta)=1`, in which case

\[
-a-bx^2+(a+b)x
=-(1-x)(a-bx).
\tag{31}
\]

For `p>=3`, the function `u -> log(u)/u` is decreasing, so

\[
\frac{\log p}{p}>
\frac{\log q}{q},
\tag{32}
\]

or equivalently

\[
a>b\frac pq\ge bx.
\tag{33}
\]

Thus `(31)` is strictly negative for every `sigma>0`. For every fixed `t`, the magnitude `(29)` decreases strictly as `sigma` moves right. The half-strip supremum is therefore obtained at its left edge. Maximizing the remaining phase term over `|t|<=T` is exactly the AF-180 calculation and proves `(6)`.

### A cancellation-aware Euler-log remainder

Because every other Euler factor cancels,

\[
\log Z_{\mathcal Q_p}(s)-\log\zeta(s)
=
\log(1-p^{-s})-
\log(1-q^{-s}).
\tag{34}
\]

Expanding in the absolute-convergence region,

\[
\log(1-p^{-s})-\log(1-q^{-s})
=
(q^{-s}-p^{-s})+R_p(s),
\tag{35}
\]

where

\[
R_p(s)
=
\sum_{m\ge2}\frac{q^{-ms}-p^{-ms}}m.
\tag{36}
\]

The crude separate-tail bound gives `(9)`. For finite bandwidth, use instead

\[
\frac{q^{-ms}-p^{-ms}}m
=-s\int_p^q x^{-ms-1}\,dx.
\tag{37}
\]

Hence

\[
|R_p(s)|
\le
|s|\int_p^q
\frac{x^{-2\sigma-1}}{1-x^{-\sigma}}\,dx
\le
\frac{|s|p^{-2\sigma-1}}{1-p^{-\sigma}}.
\tag{38}
\]

On `|t|<=T`, the function

\[
\sigma\mapsto
\frac{\sqrt{\sigma^2+T^2}\,p^{-2\sigma}}
{1-p^{-\sigma}}
\tag{39}
\]

is decreasing for `sigma>=1` when `p>=3`: the positive logarithmic derivative contribution from `sqrt(sigma^2+T^2)` is at most `1`, while the `p^{-2sigma}` term contributes `-2 log p<-2`, and the denominator contributes an additional negative term. Thus `(38)` is maximized at `sigma=sigma_0`, proving `(8)` after the elementary inequality

\[
|\sup|f|-\sup|g||\le\sup|f-g|.
\tag{40}
\]

### Whole-half-plane finite-bandwidth asymptotics

For fixed `T`, take `sigma_0 downarrow 1` in `(6)`. Since

\[
\delta_p=p^{-1}+O(p^{-2}),
\qquad
r_p=e^{-\delta_p}=1-\delta_p+O(\delta_p^2),
\tag{41}
\]

and `T delta_p->0`,

\[
D^P_{>1,T}(p)
=
\sqrt{1+T^2}\,p^{-2}(1+O_T(p^{-1})).
\tag{42}
\]

The cancellation-aware remainder `(8)` is `O_T(p^{-3})`, yielding `(11)`.

With unlimited bandwidth, choose

\[
t_p=\frac{\pi}{\delta_p}=\pi p+O(1).
\tag{43}
\]

Then the two first-order terms have opposite phase. Taking `sigma downarrow1` gives the exact prime-sum supremum

\[
D^P_{>1,\infty}(p)
=
\frac1p+\frac1q.
\tag{44}
\]

The uniform tail bound `(9)` is `O(p^{-2})`, proving `(12)`.

### Moving-edge asymptotics

Assume `sigma_p delta_p->0`. If `T_p delta_p->tau>0`, then in `(6)`

\[
r_p=e^{-\sigma_p\delta_p}=1+o(1),
\tag{45}
\]

while the radial term `(1-r_p)^2=o(1)` and the phase term tends to

\[
4\sin^2\!\left(\frac{\min\{\tau,\pi\}}2\right).
\tag{46}
\]

The crude Euler remainder is `O(p^{-2sigma_p})=o(p^{-sigma_p})`, proving `(15)`.

If `T_p delta_p->0`, expand both terms in `(6)`:

\[
1-r_p
=\sigma_p\delta_p(1+o(1)),
\qquad
2\sqrt{r_p}\sin(T_p\delta_p/2)
=T_p\delta_p(1+o(1)).
\tag{47}
\]

Equation `(8)` is lower order than the resulting first term, giving `(16)`.

Finally,

\[
p^{-\sigma_p}/\delta_p
=p^{-1-\varepsilon_p}\,p(1+o(1))
=p^{-\varepsilon_p}(1+o(1)),
\tag{48}
\]

which yields `(18)` and the horizontal threshold `(20)`.

## Exact controls

### Fixed-line control reproduces AF-180

If `sigma_p=sigma>1` is fixed, moving from one vertical line to its whole right half-strip changes no prime-sum supremum at all by `(6)`. With full bandwidth the discrepancy remains order `p^{-sigma}`, so logarithmic source recovery retains AF-180's non-Lipschitz attenuation `p^{1-sigma}->0`.

### Edge-only control does not repair bounded bandwidth

Let `sigma_p downarrow1` arbitrarily fast but keep `T` fixed. Equation `(11)` gives output order `p^{-2}`` against logarithmic source displacement order `p^{-1}`. Merely approaching the convergence boundary therefore does not resolve a unit generator displacement.

### Bandwidth-only control does not repair a fixed horizontal gap

Fix `sigma=1+epsilon` with `epsilon>0` and take unlimited bandwidth. Then

\[
D^Z_{\sigma,\infty}(p)
=2p^{-1-\epsilon}(1+o(1)),
\tag{49}
\]

so

\[
D^Z_{\sigma,\infty}(p)/d_{\log}
=2p^{-\epsilon}(1+o(1))\to0.
\tag{50}
\]

Arbitrarily high vertical frequency cannot undo Laplace-amplitude attenuation caused by staying a fixed distance to the right of `Re(s)=1`.

### Balanced control

Take

\[
T_p=cp,
\qquad
\varepsilon_p=a/\log p,
\tag{51}
\]

with `c>0`, `a>=0`. Then `T_p delta_p->c` and `p^{-varepsilon_p}->e^{-a}`, so

\[
\frac{D^Z_{\sigma_p,T_p}}{d_{\log}}
\to
2e^{-a}
\sin\!\left(\frac{\min\{c,\pi\}}2\right)>0.
\tag{52}
\]

This control demonstrates that the two thresholds are not artifacts of one another. Scaling both resources at their natural rates removes this particular first-order collapse without asserting global invertibility.

## Prior art and novelty assessment

No theorem-level novelty is claimed for the analytic mechanisms.

- Carl-Erik Fröberg, **“On the prime zeta function,”** *BIT Numerical Mathematics* 8 (1968), 187--202, is classical background for the prime Dirichlet sum and Euler logarithm already used in AF-017 and AF-180.
- Emil Grosswald and Franz J. Schnitzer, **“A class of modified ζ and L-functions,”** *Pacific Journal of Mathematics* 74(2) (1978), 357--362, DOI `10.2140/pjm.1978.74.357`, supply the established generalized-prime interval controls containing `p -> p+1`.
- David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, is classical prior art for the fact that stable recovery of closely separated spectral locations from band-limited Fourier data is governed by bandwidth times separation. Here the vertical variable is exactly Fourier frequency for the log-norm locations, and `delta_p~1/p` makes `T_p~p` the corresponding Rayleigh/super-resolution scale.
- Emmanuel J. Candès and Carlos Fernandez-Granda, **“Towards a Mathematical Theory of Super-resolution,”** *Communications on Pure and Applied Mathematics* 67(6) (2014), 906--956, DOI `10.1002/cpa.21455`, gives modern exact/stable spike-recovery results under inverse-bandwidth separation conditions. It reinforces that the bandwidth gate in `(19)` is a classical Fourier-resolution phenomenon rather than a new arithmetic principle.
- Charles L. Epstein and John Schotland, **“The Bad Truth about Laplace's Transform,”** *SIAM Review* 50(3) (2008), 504--520, DOI `10.1137/060657273`, treats Laplace inversion as a paradigmatically ill-posed inverse problem. Pierre Maréchal, Faouzi Triki, and Walter C. Simo Tao Lee, **“Regularization of the inverse Laplace transform by mollification,”** *Inverse Problems* 40(2) (2024), 025010, DOI `10.1088/1361-6420/ad1609`, derives logarithmic stability estimates in a broader inverse-Laplace setting. These are the natural prior-art boundary for the horizontal amplitude gate.

The exact formulas here are elementary consequences of a one-generator generalized-prime perturbation. The useful residual is organizational and arithmetic: **the same Euler representation exhibits a clean product of a classical Fourier resolution scale and a classical Laplace attenuation scale, and the rational-prime unit shift makes their required observation rates explicit as `T_p=Omega(p)` and `(sigma_p-1)=O(1/log p)` in logarithmic source geometry.** The literature search did not identify this exact prime-by-prime half-strip calibration as a named theorem, but that is not treated as evidence of novelty.

## Boundaries and failure modes

1. **The observation norm is part of the statement.** The result uses a supremum norm of the normalized Euler logarithm over the declared half-strip. Other output geometries can weight `sigma` or `t` differently and therefore change the conditioning profile.

2. **The source metric is decisive.** The absolute generator metric remains unstable even with complete half-plane data, while the logarithmic metric has the finer two-resource threshold `(18)`. A deliberately Laplace-weighted source metric could absorb the attenuation by construction.

3. **The boundary `Re(s)=1` is never inserted as an Euler-product value.** Equations `(11)`--`(12)` use a supremum over the open region `sigma>1` and are obtained as `sigma downarrow1`. The Euler product is not asserted to converge on the boundary.

4. **The balanced regime is not a recovery theorem.** Equation `(52)` only shows that this matched control stops forcing the output/source ratio to zero. Other generalized-prime perturbations, many-generator deformations, or nonlinear conditioning may still prevent any uniform inverse.

5. **The `T_p~p` scale is specific to a unit norm displacement.** For a general nearby replacement `q`, the phase gate is `T|log(q/p)|=Theta(1)`. The arithmetic unit shift turns that into linear bandwidth because `log((p+1)/p)~1/p`.

6. **No analytic continuation or RH claim is made.** The theorem lives entirely in the honest absolute-convergence half-plane. Its use for RH research is as a pre-compression audit: a downstream mechanism cannot recover high-scale prime specificity stably from a right-half-plane representation unless its declared source/output geometry retains the relevant scales.

## Consequences for Arithmetic Fidelity

AF-017 showed that exact Euler-product functions determine the generator-norm multiset; AF-180 showed that one fixed right-half-plane line can nevertheless be quantitatively non-faithful at high scale. AF-181 closes the obvious escape of replacing that line by an entire half-strip.

The resulting audit has **two independent resource coordinates**. For a rational-prime norm near `p`, the log-frequency separation is `delta_p~1/p`, so vertical bandwidth must grow at least linearly to avoid a Fourier-resolution collapse. Independently, the Laplace factor at left edge `1+varepsilon_p` contributes `p^{-varepsilon_p}` relative to logarithmic source scale, so the edge must approach the abscissa within `O(1/log p)` to avoid amplitude collapse.

This is the useful stopping rule: when a proposed compression claims stable access to high-scale prime provenance from Euler/local-factor data, it must declare both **how close to the convergence edge its information reaches** and **how vertical bandwidth scales with the prime norm**. Exact analytic injectivity alone answers neither question.