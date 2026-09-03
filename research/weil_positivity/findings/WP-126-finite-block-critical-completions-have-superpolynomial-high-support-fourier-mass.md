# WP-126 — Finite-block critical completions have superpolynomial high-support Fourier mass

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATED-BLOCK-CLASS + POLYNOMIAL-TAIL-MULTIPLIERS + GAMMA-BANDPASS + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-113` proves that every finite-block convex-product completion underlying the correlated `WP-101` construction has infinite Kronecker cost for every multiplier that stays nondegenerate at zero. `WP-125` then closes every nonzero continuous scalar multiplier for the independent `WP-097` product completion and, as a stress test, shows that the canonical Gamma heat-dissipation multiplier

\[
w_\tau(t)=H_\infty(t)e^{-\tau H_\infty(t)},\qquad \tau>0,
\]

still diverges there even though it vanishes at zero and, for `\tau>2`, suppresses the compulsory prime axes strongly enough to make the axis series finite.

The finite-block correlated class had remained outside that band-pass argument because correlations can delete cross-block mixed coefficients and therefore need not put mass in every fixed interior Kronecker band. Nevertheless that class has a different exact obstruction. On a sufficiently wide prime shell, the **same block factorization that pays for positivity creates superpolynomial squared Fourier mass on high-support all-positive subset characters**. Any positive multiplier whose high-frequency tail is bounded below by a polynomial must see that mass. In particular every Gamma heat-dissipation form `w_\tau`, including the endpoint-adapted `\tau>2` forms, has infinite cylindrical cost on every `WP-101`-type finite-block completion.

This result is still not architecture-free. An arbitrary correlated positive completion need not have the finite-block product coefficients used below, and a multiplier with compact spectral support or sufficiently superpolynomial tail is not excluded by this theorem. The surviving route is therefore narrower: defeating both `WP-114` and the present result requires correlations beyond the finite-block product class or a much sharper spectral cutoff than the intrinsic Gamma heat family supplies.

## 1. Finite-block critical completion

Use the notation of `WP-113`. Let

\[
C_* = \frac{2\log 2}{\sqrt2-1},
\qquad
 a_p=\frac{\log p}{C_*\sqrt p},
\qquad p\ge3.
\tag{1}
\]

Partition the primes `p>=3` into arbitrary finite disjoint blocks `B_j`, choose `\alpha_j>0` with

\[
\sum_j\alpha_j=1,
\tag{2}
\]

and assume the exact local positivity threshold

\[
\alpha_j\ge d_p
:=\frac{2\log p}{C_*(\sqrt p-1)}
\qquad(p\in B_j).
\tag{3}
\]

Set

\[
F_{p,\alpha_j}(\theta_p)
=1+\frac{\log p}{C_*\alpha_j}
\left(1-P_{p^{-1/2}}(\theta_p)\right),
\qquad
H_j=\prod_{p\in B_j}F_{p,\alpha_j},
\tag{4}
\]

and

\[
H=\sum_j\alpha_jH_j.
\tag{5}
\]

Then `H>=0`, `int H dm=1`, and the exact critical prime rays are retained. For the first harmonic define

\[
t_{p,j}:=\frac{a_p}{\alpha_j}
\qquad(p\in B_j).
\tag{6}
\]

Because `d_p>2a_p`, positivity gives the useful uniform bound

\[
0<t_{p,j}<\frac12.
\tag{7}
\]

For any nonempty finite subset `S subset B_j`, let `1_S` denote the Fourier multi-index with coefficient `+1` on `S` and zero elsewhere. Product factorization inside `H_j` and the convex mixture give exactly

\[
\boxed{
\widehat H(1_S)
=\alpha_j(-1)^{|S|}\prod_{p\in S}t_{p,j}.
}
\tag{8}
\]

No other mixture block contributes to this coefficient. The optional saturated prime-2 factor of `WP-101` has mean one and therefore does not change coefficients supported only on primes `p>=3`.

## 2. A wide critical shell forces superpolynomial subset mass

For large `X`, let

\[
Q_X=\{p\text{ prime}:X<p\le X^2\}.
\tag{9}
\]

Put

\[
Q_{X,j}=Q_X\cap B_j,
\qquad
s_{X,j}=\sum_{p\in Q_{X,j}}a_p^2,
\qquad
S_X=\sum_js_{X,j}
=\sum_{p\in Q_X}a_p^2.
\tag{10}
\]

The prime number theorem and partial summation give

\[
\sum_{X<p\le X^2}\frac{(\log p)^2}{p}
=\left(\frac32+o(1)\right)(\log X)^2,
\tag{11}
\]

hence

\[
\boxed{
S_X
=\left(\frac{3}{2C_*^2}+o(1)\right)(\log X)^2.
}
\tag{12}
\]

Now sum the squared coefficients (8) over every nonempty all-positive subset inside each block. With

\[
\beta_j:=\alpha_j^2,
\qquad
\lambda_{X,j}:=
\sum_{p\in Q_{X,j}}t_{p,j}^2
=\frac{s_{X,j}}{\beta_j},
\tag{13}
\]

one has the exact identity

\[
\sum_{\varnothing\ne S\subset Q_{X,j}}
|\widehat H(1_S)|^2
=
\beta_j
\left[
\prod_{p\in Q_{X,j}}(1+t_{p,j}^2)-1
\right].
\tag{14}
\]

Since `0<=t_{p,j}^2<1/4`, the elementary inequality `log(1+x)>=x/2` gives

\[
\prod_{p\in Q_{X,j}}(1+t_{p,j}^2)
\ge
\exp\!\left(\frac12\lambda_{X,j}\right).
\tag{15}
\]

Let

\[
B_X=\sum_{j:Q_{X,j}\ne\varnothing}\beta_j.
\tag{16}
\]

Because `sum_j alpha_j=1`,

\[
0<B_X\le\sum_j\alpha_j^2\le1.
\tag{17}
\]

Moreover

\[
\sum_j\beta_j\lambda_{X,j}=S_X.
\tag{18}
\]

Applying Jensen to the convex weights `\beta_j/B_X` yields

\[
\sum_j\beta_j
\exp\!\left(\frac12\lambda_{X,j}\right)
\ge
B_X\exp\!\left(\frac{S_X}{2B_X}\right).
\tag{19}
\]

For `S_X>=2` and `0<B_X<=1`,

\[
B_X\exp\!\left(\frac{S_X}{2B_X}\right)
\ge
\exp\!\left(\frac{S_X}{2}\right).
\tag{20}
\]

Indeed the logarithm of the ratio to the right side is

\[
\log B_X+rac{S_X}{2}\left(\frac1{B_X}-1\right),
\]

which is nonnegative on `(0,1]` when `S_X/2>=1`.

Combining (14)--(20) gives the partition- and weight-independent lower bound

\[
\boxed{
A_X
:=
\sum_j
\sum_{\varnothing\ne S\subset Q_{X,j}}
|\widehat H(1_S)|^2
\ge
\exp\!\left(\frac{S_X}{2}\right)-1.
}
\tag{21}
\]

Using (12),

\[
\boxed{
A_X
\ge
\exp\!\left[
\left(\frac{3}{4C_*^2}+o(1)\right)(\log X)^2
\right].
}
\tag{22}
\]

Thus the squared Fourier mass of these explicitly identified characters grows faster than every power of `X`. This is a different obstruction from the low-frequency pair mass of `WP-113`: it comes from the combinatorics of high-support characters within the positive finite blocks.

## 3. Every polynomial-tail positive multiplier diverges

Let

\[
w:[0,\infty)\to[0,\infty)
\tag{23}
\]

be a fixed multiplier for which there exist constants `c>0`, `rho>=0`, and `T>0` such that

\[
\boxed{
w(t)\ge c\,t^{-\rho}
\qquad(t\ge T).}
\tag{24}
\]

For a nonempty subset `S subset Q_X`, its Kronecker frequency is

\[
E(1_S)=\sum_{p\in S}\log p.
\tag{25}
\]

For large `X`,

\[
\log X\le E(1_S)
\le\sum_{p\le X^2}\log p
\le 2X^2,
\tag{26}
\]

where the last bound follows from the prime number theorem (a coarse Chebyshev bound would already suffice). Therefore every such mode lies in the tail region and (24) implies

\[
w(E(1_S))
\ge c(2X^2)^{-\rho}.
\tag{27}
\]

For the cylindrical spectral form

\[
\mathcal Q_{w,P}(H)
=
\sum_{\gamma\in\mathbb Z^P}
 w(|E(\gamma)|)|\widehat H_P(\gamma)|^2,
\tag{28}
\]

retain only the modes in (21). Equations (22) and (27) give

\[
\mathcal Q_{w,Q_X}(H)
\ge
c(2X^2)^{-\rho}A_X
\longrightarrow+\infty.
\tag{29}
\]

Hence

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal Q_{w,P}(H)=+\infty
}
\tag{30}
\]

for every fixed nonnegative multiplier with a polynomial lower tail.

The theorem does **not** require `w(0)>0`. It therefore reaches a class of endpoint-degenerate band-pass forms that lies outside the hypotheses of both `WP-113` and the architecture-free covariance theorem `WP-114`.

## 4. The intrinsic Gamma heat band-pass is closed for the whole block class

`WP-117` derives the canonical Prime-Circle/Riemann Gamma symbol

\[
H_\infty(t)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-
\psi\!\left(\frac14\right),
\tag{31}
\]

with

\[
H_\infty(t)=\log t+O(1)
\qquad(t\to\infty)
\tag{32}
\]

and `H_infty(t)>0` for `t>0`. For every fixed `tau>0`, define as in `WP-125`

\[
w_\tau(t)
=H_\infty(t)e^{-\tau H_\infty(t)}.
\tag{33}
\]

From (32), there are `c_tau>0` and `T_tau` such that

\[
\boxed{
w_\tau(t)\ge c_\tau t^{-\tau}
\qquad(t\ge T_\tau).}
\tag{34}
\]

Thus (30) applies with `rho=tau`:

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal Q_{w_\tau,P}(H)=+\infty
\qquad(\tau>0)
}
\tag{35}
\]

for **every** admissible finite-block convex-product completion (5).

This is especially decisive for `tau>2`. `WP-125` shows that in that range the compulsory prime-axis series

\[
\sum_p
w_\tau(\log p)
\frac{(\log p)^2}{p}
\tag{36}
\]

converges, so the ultraviolet one-prime test is passed. Also `w_tau(0)=0`, so the low-frequency nondegeneracy tests of `WP-113` and `WP-114` do not apply. Equation (35) identifies the remaining failure: finite-block positivity creates exponentially many high-support Fourier characters, and Gamma heat has only polynomial decay in the Kronecker frequency because its generator grows logarithmically.

The sharp Haar-equivalent critical completion `W_*` of `WP-101` is a particular case and therefore fails (35). For the `C>C_*` variants obtained by adding Haar background, every nonzero Fourier coefficient is multiplied by the fixed factor `C_*/C`; the divergence is merely rescaled and survives unchanged.

## 5. What correlations have and have not achieved

This result distinguishes three mechanisms that should not be conflated.

The independent product completion of `WP-097` is spectrally saturated in every fixed band by `WP-125`; **every** nonzero continuous multiplier fails there, even one with compact support.

Finite-block correlations can delete many cross-block coefficients, so that fixed-band theorem does not automatically transfer. `WP-113` and `WP-114` only force divergence when the multiplier remains positive at zero. The present theorem closes a different region: even after the multiplier is made zero-degenerate at the origin, **polynomial high-frequency decay is still too weak** because the block factors generate the superpolynomial subset mass (22).

What remains logically open is correspondingly sharper. A finite-block completion is not excluded by the present theorem if its scalar multiplier decays faster than every polynomial—compact support is the extreme case—while also vanishing strongly enough at zero to evade `WP-113`. More importantly, an arbitrary non-block correlated completion need not obey (8) at all. Such a completion may redistribute or suppress high-support coefficients while preserving the exact one-prime marginals.

Neither escape is automatically acceptable under the research mandate. A compact or superpolynomial spectral cutoff chosen merely to hide the forced modes would be a hand-picked kernel unless another Mathia structure independently selects it. Likewise a more general correlated completion must have a canonical geometric origin and still produce the archimedean and polar terms together with an RH-independent sign theorem.

## 6. Matched controls

### Supercritical attenuation removes the wide-shell explosion

At attenuation exponent `sigma>1/2`, replace (1) by

\[
a_p(\sigma)=\frac{\log p}{C}p^{-\sigma}.
\tag{37}
\]

Then on the same shell

\[
S_X(\sigma)
=\sum_{X<p\le X^2}|a_p(\sigma)|^2
=O_{\sigma,C}\!\left(
X^{1-2\sigma}\log X
\right)
\longrightarrow0.
\tag{38}
\]

The Jensen exponent driving (22) disappears. Thus the result is tied to the exact critical `sigma=1/2` amplitude density rather than to finite-block products as such.

### Sparse generalized generators do not force the same growth

For a free multiplicative control with generator energies `E_j=j` and critical-looking amplitudes `E_je^{-E_j/2}`, the squared-amplitude mass in a wide energy shell `[L,2L]` tends exponentially to zero. The analogue of `S_X` therefore does not grow like `(log X)^2`, and (22) has no counterpart. Ordinary prime density at the critical amplitude scale is essential to the superpolynomial shell mass.

### Pairwise analysis alone misses this obstruction

A zero-degenerate multiplier can strongly suppress the nearby-prime pair modes used in `WP-113` and `WP-114`; those theorems deliberately do not claim otherwise. Equation (21) shows why testing only pair differences is insufficient for the finite-block product architecture. Positivity propagates the first prime rays multiplicatively to characters of arbitrarily high support, and their aggregate squared mass is the decisive quantity for polynomial-tail band-pass forms.

## 7. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the ingredients.

- Finite Riesz-product factorization of Fourier coefficients is classical harmonic analysis. The branch already records Kilmer--Saeki, *On Riesz product measures; mutual absolute continuity and singularity*, Ann. Inst. Fourier 38 (1988), and the Hedenmalm--Lindqvist--Seip prime-polytorus/Dirichlet-series realization.
- The product identity in (14), Jensen's inequality, and the elementary bound `log(1+x)>=x/2` are standard.
- The shell asymptotic (11) is an immediate prime-number-theorem/partial-summation calculation.
- The digamma asymptotic and the Gamma/Schoenberg interpretation are already audited in `WP-117`, `WP-118`, and `WP-125`.

A bounded literature audit of Riesz products, Fourier coefficients of product measures, prime-polytorus harmonic analysis, and spectral multipliers found the standard ambient machinery but no external result that changes the branch-local conclusion above. In particular, standard Riesz-product references explicitly encode finite subset Fourier coefficients as products of the local coefficients; the new point here is only the Mathia-specific combination of that classical identity with the exact critical prime amplitudes, the convex positivity budget, and the Gamma heat tail.

The conclusion is therefore a branch-internal obstruction, not a claim that superpolynomial subset mass in Riesz products is a new phenomenon in harmonic analysis.

## Research consequence

The correlated finite-block escape left open by the Gamma band-pass stress test is now closed:

\[
\boxed{
\begin{gathered}
\text{exact critical `WP-101` finite-block completion}
\\
+\ \text{any fixed positive multiplier with polynomial lower tail}
\\
\Longrightarrow\ \text{infinite cylindrical Kronecker cost}.
\end{gathered}
}
\tag{39}
\]

In particular, the independently selected Prime-Circle Gamma geometry cannot be rescued merely by replacing its Markov symbol by the natural heat-dissipation band-pass `H_infty e^{-tau H_infty}` while retaining the strongest explicit correlated prime-torus completion currently available.

The surviving frontier is now more specific: either a **genuinely non-block/nonseparable correlation architecture** must suppress the high-support multiplicative propagation, or a geometrically forced scalar form must have both a zero-frequency degeneracy and a superpolynomial/compact high-frequency cutoff. Either route still has to generate the finite Mangoldt term, the Gamma and polar counterterms, and a global sign theorem before any Weil-positivity claim is available.