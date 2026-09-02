# WP-113 — Finite-block correlated critical completions still have infinite low-frequency Kronecker cost

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATED-BLOCK-CLASS + ALL-SOBOLEV-ORDERS + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-110` closes every inhomogeneous Sobolev/Kronecker smoothing escape for the explicit **independent product** completion of `WP-097`, but deliberately leaves correlated completions open. `WP-101` then supplies the strongest concrete correlated counterexample to the product-specific obstruction: at the sharp critical mass it builds a Haar-equivalent positive completion as a convex mixture of finite-block products while preserving every exact one-prime Weil ray.

That explicit correlated escape still cannot support a nondegenerate Kronecker spectral energy. In fact the obstruction is not tied to the particular geometric block weights chosen in `WP-101`.

Let

\[
C_*=\frac{2\log2}{\sqrt2-1},
\qquad
a_p:=\frac{\log p}{C_*\sqrt p},
\qquad p\ge3,
\tag{1}
\]

and let the primes `p>=3` be partitioned into arbitrary finite disjoint blocks `B_j`. Choose positive weights `alpha_j` with

\[
\sum_j\alpha_j=1
\tag{2}
\]

and form the `WP-101` local factors

\[
F_{p,\alpha_j}(\theta_p)
=
1+\frac{\log p}{C_*\alpha_j}
\left(1-P_{p^{-1/2}}(\theta_p)\right),
\qquad p\in B_j.
\tag{3}
\]

Assume only the exact positivity condition

\[
\alpha_j\ge d_p
:=\frac{2\log p}{C_*(\sqrt p-1)}
\qquad(p\in B_j),
\tag{4}
\]

and define

\[
H_j=\prod_{p\in B_j}F_{p,\alpha_j},
\qquad
H=\sum_j\alpha_jH_j.
\tag{5}
\]

Then `H>=0`, `int H dm=1`, and every first prime-coordinate moment is exact:

\[
\widehat H(e_p)=-a_p.
\tag{6}
\]

For **every** such finite-block convex completion, not merely the particular block partition in `WP-101`, the mixed coefficients forced by positivity have unbounded squared Fourier mass in every fixed neighborhood of zero Kronecker frequency. More precisely, for every `epsilon>0`,

\[
\boxed{
\sup_{P\Subset\mathcal P}
\sum_{\substack{p,q\in P,\ p\ne q\\
|\log p-\log q|<\epsilon}}
|\widehat H(e_p-e_q)|^2
=+\infty.
}
\tag{7}
\]

Consequently, if `w:[0,infinity)->[0,infinity)` is continuous at zero with `w(0)>0`, every cylindrical positive Kronecker spectral form

\[
\mathcal S_{w,P}(H)
=
\sum_{\beta\in\mathbb Z^P}
 w(|E(\beta)|)|\widehat H_P(\beta)|^2,
\qquad
E(\beta)=\sum_{p\in P}\beta_p\log p,
\tag{8}
\]

has unbounded finite-prime marginals. In particular,

\[
\boxed{
\sup_{P\Subset\mathcal P}\mathcal S_{s,P}(H)=+\infty
\qquad\text{for every }s\in\mathbb R,
}
\tag{9}
\]

for the inhomogeneous Sobolev symbols `w_s(t)=(1+t^2)^s`.

Thus the explicit correlated Haar-equivalent repair from `WP-101` closes the measure-class objection of `WP-100`, but it does **not** close the infrared spectral obstruction of `WP-110`. Correlation changes which mixed modes appear; the finite-block convex mechanism still has to place enough same-block pairs among nearby primes that their low-frequency mass diverges.

This is not a theorem about every correlated completion. It closes the entire finite-block convex-product class underlying `WP-101`, including arbitrary block partitions and admissible mixture weights. More general correlations can still alter the two-prime coefficients and remain logically open.

## 1. Same-block correlations are explicit and unavoidable

For `k!=0`, the Poisson Fourier series gives

\[
\widehat F_{p,\alpha_j}(k)
=-\frac{\log p}{C_*\alpha_j}p^{-|k|/2}.
\tag{10}
\]

Therefore (6) follows immediately after multiplying the unique block containing `p` by its mixture weight `alpha_j`.

For distinct `p,q` in the same block `B_j`, product factorization inside `H_j` gives

\[
\boxed{
\widehat H(e_p-e_q)
=\alpha_j
\left(-\frac{a_p}{\alpha_j}\right)
\left(-\frac{a_q}{\alpha_j}\right)
=\frac{a_pa_q}{\alpha_j}.
}
\tag{11}
\]

If `p,q` lie in different blocks, this coefficient vanishes because no mixture component contains nonconstant factors in both coordinates. Hence the block mixture suppresses many mixed-prime modes relative to the full product completion, but the modes that remain are amplified by `1/alpha_j`.

The optional saturated prime-2 factor `G_2` of `WP-101` is irrelevant here. It has Haar mean one and is independent of all coordinates `p>=3`, so coefficients supported only on primes `>=3` are unchanged after multiplication by `G_2`.

## 2. Positivity converts the convex budget into a sharp pair-mass lower bound

Fix a finite prime shell `Q` and put

\[
b_p:=a_p^2=\frac{(\log p)^2}{C_*^2p},
\qquad
s_j:=\sum_{p\in B_j\cap Q}b_p,
\qquad
S_Q:=\sum_{p\in Q}b_p=\sum_js_j.
\tag{12}
\]

Using (11), the total squared Fourier mass of ordered distinct same-block pairs from `Q` is exactly

\[
M_Q
:=
\sum_j\frac1{\alpha_j^2}
\left(
 s_j^2-
 \sum_{p\in B_j\cap Q}b_p^2
\right).
\tag{13}
\]

The first term cannot be made small by splitting the primes among many convex components. Since `sum_j alpha_j=1` and `0<alpha_j<=1`, Cauchy--Schwarz gives

\[
S_Q^2
=
\left(\sum_j\alpha_j\frac{s_j}{\alpha_j}\right)^2
\le
\sum_j\frac{s_j^2}{\alpha_j}
\le
\sum_j\frac{s_j^2}{\alpha_j^2}.
\tag{14}
\]

The diagonal subtraction in (13) is also uniformly controlled by positivity. From (4),

\[
d_p
=
2a_p\frac{\sqrt p}{\sqrt p-1}
>2a_p,
\tag{15}
\]

so for every `p in B_j`,

\[
\frac{b_p}{\alpha_j^2}
=
\frac{a_p^2}{\alpha_j^2}
<\frac14.
\tag{16}
\]

Consequently

\[
\sum_j\frac1{\alpha_j^2}
\sum_{p\in B_j\cap Q}b_p^2
=
\sum_{p\in Q}b_p\frac{b_p}{\alpha_{j(p)}^2}
<\frac14S_Q.
\tag{17}
\]

Combining (13)--(17) yields the block-partition-independent inequality

\[
\boxed{
M_Q\ge S_Q^2-\frac14S_Q.
}
\tag{18}
\]

This is the decisive point. The correlations in `WP-101` are not free parameters once positivity and the exact one-prime moments are imposed. A smaller convex weight makes a local factor harder to keep positive and simultaneously amplifies every same-block mixed coefficient. The global convex budget (2) therefore cannot distribute the mandatory prime rays among finite blocks without paying at least the quadratic pair mass (18).

## 3. Short prime shells force the pair mass to infinity at zero Kronecker frequency

Fix `epsilon>0` and choose `delta>0` with

\[
\log(1+\delta)<\epsilon.
\tag{19}
\]

Let

\[
Q_X=\{p\text{ prime}:X<p\le(1+\delta)X\}.
\tag{20}
\]

For every distinct `p,q in Q_X`,

\[
|E(e_p-e_q)|
=|\log p-\log q|
<\epsilon.
\tag{21}
\]

The prime number theorem and partial summation give

\[
\sum_{X<p\le(1+\delta)X}\frac{(\log p)^2}{p}
=
\log(1+\delta)\log X+O_\delta(1).
\tag{22}
\]

Therefore

\[
S_{Q_X}
=
\frac{\log(1+\delta)}{C_*^2}\log X+O_\delta(1)
\longrightarrow+\infty.
\tag{23}
\]

Equation (18) now gives

\[
\boxed{
M_{Q_X}
\ge
S_{Q_X}^2-\frac14S_{Q_X}
\asymp_\delta \log^2X,
}
\tag{24}
\]

which proves (7). Notice that no assumption about consecutive blocks, block sizes, or the particular geometric sequence of mixture weights used in `WP-101` appears in the estimate.

There is also no exact nontrivial zero frequency: unique factorization still gives `E(beta)=0` only for `beta=0`. The obstruction is an infrared accumulation of distinct modes approaching or remaining inside arbitrarily small fixed neighborhoods of zero.

## 4. Every nondegenerate low-frequency positive spectral geometry diverges

Let `w` be continuous at zero with `w(0)>0`. Choose `epsilon>0` and `c_w>0` such that

\[
w(t)\ge c_w
\qquad(0\le t<\epsilon).
\tag{25}
\]

Taking the finite marginal on `Q_X` and retaining only the same-block modes in (13),

\[
\mathcal S_{w,Q_X}(H)
\ge c_w M_{Q_X}
\longrightarrow+\infty.
\tag{26}
\]

This proves (8)--(9). In particular, negative Sobolev order cannot help: it suppresses high Kronecker frequencies but is bounded below on every fixed neighborhood of zero.

The result should be read together with `WP-109`. For arbitrary completions, mandatory one-prime modes force divergence through Sobolev order `s>=-1`; for the finite-block correlated class, the required same-block positivity correlations add enough low-frequency mass to close **all** `s<-1` as well. `WP-110` obtained the same all-order boundary for the independent product, with factorized two-prime coefficients. Here factorization is used only inside each finite block, and the convex-budget inequality (18) replaces global product structure.

## 5. The full `WP-101` sharp completion and its `C>C_*` variants are covered

The sharp Haar-equivalent density of `WP-101` is

\[
W_*=G_2H,
\tag{27}
\]

with one particular admissible choice of blocks and weights. As noted above, (7)--(9) apply unchanged to modes supported on primes `>=3`. Hence that explicit correlated completion has infinite cylindrical Kronecker spectral cost at every Sobolev order despite being mutually absolutely continuous with Haar.

For every fixed `C>C_*`, `WP-101` defines

\[
\mu_C=\mu_*+(C-C_*)m.
\tag{28}
\]

After probability normalization, every nonzero Fourier coefficient of `W_*` is merely multiplied by the fixed factor `C_*/C`. The lower bound (24) is therefore multiplied by `(C_*/C)^2` and still diverges. Adding a fixed positive Haar background repairs lower-density regularity but not the low-frequency spectral mass.

## 6. Matched controls and falsifiers

### Supercritical attenuation

Replace the critical amplitudes by

\[
a_p(\sigma)=\frac{\log p}{C}p^{-\sigma},
\qquad\sigma>\frac12.
\tag{29}
\]

On the same short shell,

\[
S_{Q_X}(\sigma)
=
\frac1{C^2}
\sum_{X<p\le(1+\delta)X}
(\log p)^2p^{-2\sigma}
=O_\delta\!\left(X^{1-2\sigma}\log X\right)
\longrightarrow0.
\tag{30}
\]

So the critical pair-mass explosion (24) disappears on the convergent side. This matches `WP-100`/`WP-110`, where the simple supercritical product completion has finite cylindrical `L^2` mass and hence finite negative-order inhomogeneous spectral cost. The obstruction is tied to the `sigma=1/2` prime-density boundary, not to the formal use of convex block products.

### Sparse generalized-generator control

For a free multiplicative system with energies `E_j` and critical-looking amplitudes `E_je^{-E_j/2}/C`, the proof replaces (23) by the squared-amplitude mass in a fixed-width energy window. If, for example, `E_j=j`, every fixed-width window contains only `O(1)` generators and that mass tends to zero exponentially. The shell step therefore fails. What is special here is the density of the ordinary prime energies `E_p=log p`, not a universal property of free multiplicative generators.

### Arbitrary-correlation falsifier

Equation (11) is compulsory only for the finite-block convex-product architecture (5). A genuinely nonseparable correlated measure can choose different two-prime coefficients while preserving all one-prime marginals; `WP-101` itself was introduced to show why product-only claims must not be overgeneralized. Thus `WP-113` does **not** strengthen `WP-109` into an all-order theorem for every exact critical completion.

### Low-frequency-degenerate spectral forms

As in `WP-110`, a multiplier with `w(0)=0` is outside the theorem. A geometrically forced homogeneous or band-pass form that vanishes strongly enough at zero could evade the infrared estimate. It would still have to survive the one-prime high-frequency obstruction, generate the exact finite selector plus Gamma/polar terms, and derive its zero from geometry rather than insert a spectral notch by hand.

## 7. Prior-art and novelty audit

The ingredients are classical. The Bohr lift/prime-polytorus representation is the Hedenmalm--Lindqvist--Seip framework already recorded in `research/weil_positivity/SOURCES.md` (Duke Math. J. 86 (1997), DOI `10.1215/S0012-7094-97-08601-4`). Positive Riesz-product and generalized Riesz-product constructions on locally compact abelian groups are classical; a targeted audit anchor is Shelby J. Kilmer and Sadahiro Saeki, *On Riesz product measures; mutual absolute continuity and singularity*, Ann. Inst. Fourier 38 (1988), 63--93, DOI `10.5802/aif.1135`. The Zygmund/Steinhaus regularity background used by `WP-101` is likewise classical; Odysseas Bakas, *On a Problem of Pichorides*, J. Geom. Anal. 31 (2021), 7455--7512, DOI `10.1007/s12220-020-00550-8`, is the branch's modern audit reference. The prime-number-theorem shell estimate and Cauchy--Schwarz are standard.

No novelty is claimed for those ingredients, for Riesz products, or for low-frequency Fourier accumulation in general. The branch-specific content is the exact inequality (18): **within the `WP-101` positive finite-block completion architecture, the same convex weights that make all local prime factors positive force a quadratic amount of nearby-prime mixed Fourier mass, independently of how the blocks and weights are chosen.** A targeted literature search found the expected classical Riesz-product/absolute-continuity and lacunary-Fourier theory but no prior statement that changes this exact Mathia-specific compatibility conclusion.

The conclusion remains an obstruction inside classical harmonic/Dirichlet-series territory. It is not a new Weil criterion, not evidence for RH, and not a claim that the underlying harmonic-analysis tools are new.

## Consequence for the primary question

`WP-101` was an important falsifier because it proved that arbitrary correlations can restore Haar equivalence at the exact critical diagonal. `WP-113` now shows that the **specific positive correlation mechanism that realizes that escape** cannot simultaneously provide a finite nondegenerate Kronecker spectral energy: its mandatory same-block mixed modes accumulate with divergent mass near zero frequency.

The surviving route is therefore narrower. A candidate must either use correlations more genuinely nonseparable than a convex mixture of finite positive prime blocks, derive a spectral form intrinsically degenerate at zero while also controlling the one-prime high-frequency tail, or couple the finite-prime carrier to the archimedean/polar sector **before** the prime-torus completion and scalar spectral geometry are formed. None of those mechanisms is supplied here, and the full global Weil positivity problem remains open.