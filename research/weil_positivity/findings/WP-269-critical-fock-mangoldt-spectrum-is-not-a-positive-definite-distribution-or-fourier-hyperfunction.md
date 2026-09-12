---
id: WP-269
title: Critical Fock Mangoldt spectrum is too large for positive-definite distributions or Fourier hyperfunctions
branch: weil_positivity
status: supported
kind: boundary-category-obstruction
claim_strength: exact generalized-Bochner threshold for the source-native Mangoldt time spectrum
created: 2026-09-12
refined: 2026-09-12
related: [WP-009, WP-132, WP-256, WP-259, WP-261, WP-267, WP-268]
prior_art:
  - Bochner--Schwartz theorem for positive-definite distributions
  - Chung--Kim generalized Bochner--Schwartz theorem for Fourier hyperfunctions
  - positive-definite Fourier ultra-hyperfunctions and exponential-growth measures
  - classical Dirichlet series for -zeta'/zeta
---

# WP-269 — Critical Fock Mangoldt spectrum is too large for positive-definite distributions or Fourier hyperfunctions

## Claim

`WP-268` shows that the critical common-vacuum Fock row is not mathematically unhostable: although it lies beyond every finite Hamiltonian Hilbert scale, it is a continuous functional on the source-native rapid-energy nuclear rigging

\[
\Phi_{\exp}=\bigcap_{a>0}\operatorname{Dom}e^{aH}.
\]

That leaves an important possible bridge open. One could try to restore the missing Weil translation geometry by evolving the critical boundary amplitudes with the arithmetic time flow and reading their positive squared amplitudes as the spectral measure of a stationary positive-definite boundary covariance.

This route has a sharp obstruction before any Gamma or polar completion is considered. The exact source-native full prime-power spectral measure is

\[
\boxed{
\nu_{1/2}
:=\frac12\sum_p\sum_{k\ge1}
(\log p)p^{-k/2}
\bigl(\delta_{k\log p}+\delta_{-k\log p}\bigr).
}
\tag{1}
\]

Its one-prime-layer submeasure already has weights

\[
\frac{\log p}{\sqrt p},
\tag{2}
\]

which are exactly the squared critical boundary amplitudes of `WP-261`--`WP-268`. The full measure (1) is likewise the exact diagonal Mangoldt half-density of `WP-256`/`WP-259`, placed at its source arithmetic frequencies.

The measure (1) is **not tempered**. More strongly, it is not infra-exponentially tempered: its exponential moment has the exact threshold

\[
\boxed{
\int_{\mathbb R}e^{-a|\xi|}\,d\nu_{1/2}(\xi)<\infty
\quad\Longleftrightarrow\quad
a>\frac12.
}
\tag{3}
\]

Consequently the classical Bochner--Schwartz theorem forbids any positive-definite distribution whose Fourier spectral measure is (1), and the generalized Bochner--Schwartz theorem for Fourier hyperfunctions forbids the same realization even after passing to that larger standard generalized-function category. Positive-definite distributions are Fourier transforms of positive **tempered** measures; positive-definite Fourier hyperfunctions require positive **infra-exponentially tempered** measures. The critical Mangoldt spectrum satisfies neither growth condition.

Thus the exponential rigging found in `WP-268` solves **hostability of the boundary functional**, but it does not make the corresponding arithmetic-time orbit into an ordinary stationary positive covariance on the additive Weil line. The obstruction is exactly the arithmetic spectral density, not a missing choice of polynomial Sobolev order.

There is a precise surviving category. The critical measure has fixed exponential growth, so the literature on positive-definite Fourier **ultra-hyperfunctions**, whose spectral side allows positive measures of exponential growth, is large enough in principle. That is a genuine category change, not a positivity theorem for Weil. It still supplies no Gamma/polar completion and no reason that the resulting ultra-hyperfunctional covariance has the required Weil autocorrelation orientation.

**Classification:** `EXACT-DERIVED + LITERATURE-REDIRECT + DECISIVE-CATEGORY-NARROWING + NOT-A-WEIL-BRIDGE`.

## 1. The source-native stationary spectrum is forced by the Fock carrier

On the symmetric prime-power axis, retain the arithmetic Hamiltonian

\[
H e_{p^k}=k\log p\,e_{p^k}
\tag{4}
\]

and the positive diagonal carrier from `WP-256`/`WP-259`,

\[
T e_{p^k}
=(\log p)p^{-k/2}e_{p^k}.
\tag{5}
\]

The same coefficient is the squared boundary norm in `WP-261`:

\[
\|C_{1/2}e_{p^k}\|^2
=(\log p)p^{-k/2}.
\tag{6}
\]

For any finite set `F` of prime powers, arithmetic-time evolution therefore gives the canonical positive-definite kernel

\[
K_F(t)
:=\sum_{p^k\in F}
(\log p)p^{-k/2}\cos(tk\log p).
\tag{7}
\]

Indeed (7) is the Fourier transform of the finite positive symmetric measure

\[
\nu_F
=\frac12\sum_{p^k\in F}
(\log p)p^{-k/2}
\bigl(\delta_{k\log p}+\delta_{-k\log p}\bigr).
\tag{8}
\]

No kernel has been fitted here. Frequencies come from `H`, and masses come from the exact source-derived squared boundary norm. Therefore if the finite covariances had a positive-definite generalized-function limit preserving the exact source spectrum, its spectral measure would have to be (1).

The obstruction below already holds on the `k=1` submeasure, so prime-power multiplicity is not responsible for it.

## 2. Polynomial damping never makes the critical spectrum tempered

A positive measure `mu` on `R` is tempered exactly when it has at most polynomial growth in the distributional sense; equivalently it is enough that

\[
\int_{\mathbb R}(1+|\xi|^2)^{-N}\,d\mu(\xi)<\infty
\tag{9}
\]

for some finite `N`.

For (1), retain only the positive `k=1` prime atoms. For every finite `N`, the corresponding contribution is bounded below by

\[
\frac12\sum_p
\frac{\log p}{\sqrt p\,(1+(\log p)^2)^N}.
\tag{10}
\]

Compare its summand with `1/p`. The ratio is

\[
\frac{\displaystyle
\frac{\log p}{\sqrt p(1+(\log p)^2)^N}}
{\displaystyle 1/p}
=
\frac{\sqrt p\,\log p}{(1+(\log p)^2)^N}
\longrightarrow\infty.
\tag{11}
\]

Euler's divergence of `sum_p 1/p` therefore implies

\[
\boxed{
\int(1+|\xi|^2)^{-N}\,d\nu_{1/2}(\xi)=\infty
\quad\text{for every finite }N.
}
\tag{12}
\]

Hence `nu_{1/2}` is not a tempered measure.

This is the spectral-side counterpart of `WP-268`. There the **amplitude** vector

\[
u_p=\sqrt{\log p}\,p^{-1/4}
\tag{13}
\]

survives no finite polynomial Hamiltonian dual scale. Here its **squared** mass becomes a positive measure on the arithmetic-frequency line and survives no finite polynomial distributional weight. The same arithmetic density drives both failures.

## 3. Exponential damping has the exact threshold one half

The full prime-power measure gives a sharper statement. For `a>0`, symmetry and positivity give

\[
\begin{aligned}
I(a)
&:=\int_{\mathbb R}e^{-a|\xi|}\,d\nu_{1/2}(\xi)\\
&=\sum_p\sum_{k\ge1}
(\log p)p^{-k(1/2+a)}.
\end{aligned}
\tag{14}
\]

When `a>1/2`, put `s=1/2+a>1`. The classical Euler-product logarithmic derivative gives

\[
I(a)
=-\frac{\zeta'(s)}{\zeta(s)}<\infty.
\tag{15}
\]

At `a=1/2`, the prime subseries is

\[
\sum_p\frac{\log p}{p}=\infty,
\tag{16}
\]

and for `0<a<1/2` its terms dominate the `a=1/2` prime terms eventually. Therefore

\[
\boxed{I(a)<\infty\iff a>1/2.}
\tag{17}
\]

In particular `nu_{1/2}` is a positive measure of fixed exponential growth, but it is **not infra-exponentially tempered**, because that condition requires

\[
\int e^{-a|\xi|}\,d\mu(\xi)<\infty
\qquad\text{for every }a>0.
\tag{18}
\]

The factor-of-two relation with `WP-268` is exact. A single exponential Hilbert level `Dom e^{bH}` makes the critical boundary **amplitude** continuous only for `b>1/4`; after squaring to form spectral mass, the stationary-measure damping threshold is `a>1/2`.

## 4. Bochner--Schwartz closes the ordinary distributional covariance route

The classical Bochner--Schwartz theorem states that every positive-definite distribution is the Fourier transform of a positive tempered measure, and conversely. In particular, positive-definite distributions on the compact-test space do not form a larger non-tempered escape class: positivity itself forces temperedness.

Suppose the finite kernels (7) converged, without changing their source frequencies or masses, to a positive-definite distribution `K`. Its Fourier transform would be the positive measure (1), by uniqueness on the increasing finite spectral cylinders. Bochner--Schwartz would then force `nu_{1/2}` to be tempered, contradicting (12).

Therefore

\[
\boxed{
\text{there is no positive-definite distribution on }\mathbb R
\text{ with source spectrum }\nu_{1/2}.
}
\tag{19}
\]

This is stronger than saying that the formal Fourier series in (7) diverges pointwise. No summation method can produce an ordinary positive-definite **distribution** while retaining the same positive spectral masses. A subtraction may define some renormalized signed object, but then the inherited Bochner positivity has been changed rather than extended.

It also clarifies why direct use of the prime measure and stationary covariance are different operations. The locally finite measure (1) acts perfectly well on compactly supported functions of the **frequency/logarithmic-prime variable**. What fails is Fourier transport of that positive measure into the ordinary distribution category on the dual additive-time variable.

## 5. Fourier hyperfunctions are still too small

A natural reaction to (19) is to enlarge distributions to Fourier hyperfunctions. That standard enlargement is still insufficient if one insists on positive definiteness.

Chung and Kim proved a generalized Bochner--Schwartz theorem for Fourier hyperfunctions: every positive-definite Fourier hyperfunction is the Fourier transform of a positive **infra-exponentially tempered** measure. Their 1995 paper, *Distributions with Exponential Growth and Boehner-Schwartz Theorem for Fourier Hyperfunctions*, Publ. RIMS 31, 829--845, DOI `10.2977/prims/1195163720`, gives the relevant characterization. The same growth distinction is emphasized in later work on positive-definite hyperfunctions and stationary hyperfunctional random processes.

Equation (17) violates the required condition for every `0<a<=1/2`. Hence

\[
\boxed{
\text{there is no positive-definite Fourier hyperfunction
with spectral measure }\nu_{1/2}.
}
\tag{20}
\]

Thus the category escape identified abstractly in `WP-268` is sharper than merely saying "use distributions" or "use hyperfunctions". The critical arithmetic density remains too large even for the standard Fourier-hyperfunction Bochner class.

## 6. The matched sigma-family recovers the Euler boundary exactly

The threshold is not peculiar to the numerical value `1/2`. Define the source-matched family

\[
\nu_\sigma
:=\frac12\sum_p\sum_{k\ge1}
(\log p)p^{-k\sigma}
\bigl(\delta_{k\log p}+\delta_{-k\log p}\bigr),
\qquad \sigma>0.
\tag{21}
\]

Then for `a>0`,

\[
\int e^{-a|\xi|}\,d\nu_\sigma(\xi)
=\sum_{p,k}(\log p)p^{-k(\sigma+a)},
\tag{22}
\]

which is finite exactly when

\[
\boxed{\sigma+a>1.}
\tag{23}
\]

Consequently:

- for `sigma>1`, `nu_sigma` has finite total mass and gives an ordinary continuous Bochner covariance;
- at `sigma=1`, it has infinite total mass but is tempered (classically `sum_{n<=x} Lambda(n)/n=log x+O(1)`) and is infra-exponentially tempered;
- for every `0<sigma<1`, it is non-tempered and fails infra-exponential temperedness, with exponential damping required beyond `a>1-sigma`.

The generalized-function boundary is therefore exactly the same Euler boundary that repeatedly appears elsewhere in the branch. At the Weil value `sigma=1/2`, an ordinary positive stationary covariance becomes available only after damping far enough to move the spectral coefficients to exponent `sigma+a>1`.

This is a useful matched control because no zeta zeros or RH enter. The threshold comes from the positive prime-power carrier alone.

## 7. Prior-art and novelty audit

The general theorems are classical. The Bochner--Schwartz theorem identifies positive-definite distributions with Fourier transforms of positive tempered measures. Chung and Kim extended the theorem to Fourier hyperfunctions, where positivity corresponds to positive infra-exponentially tempered spectral measures. Their 1995 Publ. RIMS paper is the direct prior-art reference for the hyperfunction step.

The next standard category is also known. Work of Yoshino and Suwa on positive-definite Fourier ultra-hyperfunctions identifies positive spectral measures with exponential growth as the relevant enlarged class; see, for example, *The Bochner-Schwartz theorem for Fourier ultra-hyperfunctions*, Integral Transforms and Special Functions 17 (2006), and *The structure of positive definite Fourier ultra-hyperfunctions*, Complex Variables and Elliptic Equations 51 (2006). This literature means that moving to an ultra-hyperfunction category would be a prior-art category change, not a new theorem.

The Mathia-specific result is the exact placement of the source-derived critical Fock/Mangoldt spectrum inside this hierarchy:

\[
\text{tempered distributions}
\subset
\text{Fourier hyperfunctions}
\quad\text{are both too small,}
\tag{24}
\]

while the exact exponential threshold (17) points to an ultra-hyperfunctional/exponential-growth category as the first standard generalized Bochner class not excluded by growth alone. The calculation also ties that category boundary directly to the `WP-268` source Hamiltonian rigging and to the exact Mangoldt half-density rather than to an arbitrary exponentially growing measure.

No historical novelty is claimed for Bochner--Schwartz, hyperfunction theory, the identity `-zeta'/zeta`, or the existence of ultra-hyperfunction extensions.

## 8. Aggressive falsification and surviving escape

Several controls prevent overreading this obstruction.

First, it does **not** say that the explicit-formula prime term is ill-defined. The measure (1) is locally finite, so compactly supported frequency-side tests see only finitely weighted mass. The failure concerns the attempt to turn that positive carrier into a global stationary positive-definite object on the dual additive line by ordinary Fourier duality.

Second, an affine change of energy units cannot repair the category. Replacing `H` by `cH+dI`, with `c>0`, only rescales the exponential threshold from `a>1/2` to `a>1/(2c)` (up to the harmless constant shift). There is still some positive `a` below threshold, so infra-exponential temperedness still fails.

Third, a sufficiently sparse generalized-prime energy set can evade the polynomial-growth obstruction. Thus the result uses genuine arithmetic spectral density; it is not a theorem about every countable positive spectrum.

Fourth, a signed or conditionally positive renormalization may evade the literal Bochner theorem. But a finite polynomial/counterterm correction does not change the high-frequency positive mass (1), so it cannot turn that measure itself into a tempered or infra-exponentially tempered positive spectrum. Any successful renormalized sign theorem must therefore be additional structure, not inherited stationary positivity of the original carrier.

Finally, the ultra-hyperfunction redirect is only a host category. Even if the critical spectrum defines a positive-definite ultra-hyperfunctional covariance, that construction still starts from the already-known positive diagonal Mangoldt carrier. It does not generate the Weil translation/autocorrelation sign, the Gamma factor, or the polar term, and it does not distinguish a source-forced completed correspondence from a generalized-function repackaging of known coefficients.

## Consequence

`WP-268` should therefore be read more narrowly. The rapid-energy rigging genuinely retains the critical boundary row, but **continuity of the row does not imply Fourier-positive stationarity on the Weil line**. Once its amplitudes are squared and evolved at the arithmetic frequencies, their exact Mangoldt spectral measure grows too quickly for positive-definite distributions and even for the standard Fourier-hyperfunction extension.

The live route must now do one of two harder things. Either it must derive an ultra-hyperfunctional/exponential-type finite--archimedean correspondence and then independently recover the Weil orientation, or it must introduce a source-forced global cancellation/quotient **before** stationary positivity is read so that the resulting spectral object has fundamentally different growth. Merely embedding the critical row into a larger test topology and applying ordinary Bochner positivity is closed.