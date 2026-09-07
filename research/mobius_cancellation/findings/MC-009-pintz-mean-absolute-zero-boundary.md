# MC-009 — Pintz mean-absolute Möbius exponent recovers the rightmost zero boundary

**Status:** `LITERATURE+DERIVED`, `NEEDS-AUDIT`, `CORRECTED-BY-MC-115`.

## Claim

Let

\[
\vartheta=\sup_{\rho:\zeta(\rho)=0}\operatorname{Re}\rho
\]

where the supremum runs over nontrivial zeros, and define

\[
D_M(x)=\frac1x\int_0^x |M(u)|\,du,
\qquad
S_{M,\delta}(x)=\max_{x^{1-\delta}\le u\le x}|M(u)|
\]

for fixed `delta>0`.

The current version of Pintz's very recent preprint (`MC-S19`, arXiv:2608.24878v2, 1 September 2026) states in Theorem 2.2 that

\[
\log D_M(x)\sim \log S_{M,\delta}(x)\sim \log Z(x),
\tag{1}
\]

where

\[
Z(x)=\max_{\rho:\gamma>0}\frac{x^\beta}{\gamma},
\qquad \rho=\beta+i\gamma.
\tag{2}
\]

Together with the zero-edge definition of `vartheta`, `(1)` yields the full logarithmic-order statement

\[
\boxed{
\lim_{x\to\infty}\frac{\log D_M(x)}{\log x}
=
\lim_{x\to\infty}\frac{\log S_{M,\delta}(x)}{\log x}
=\vartheta.}
\tag{3}
\]

Conditional on the still-pending proof audit of Pintz's theorem, this says that global absolute averaging and a broad near-end maximum preserve not merely a limsup obstruction but the **entire power exponent** of the rightmost zeta-zero boundary.

A correction to the original version of this finding is essential. The weaker equivalence

\[
\boxed{
RH
\iff
D_M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0
}
\tag{4}
\]

does **not** depend on Pintz. `MC-115` proves `(4)` directly: the mean-absolute bound makes

\[
s\int_1^\infty M(x)x^{-s-1}\,dx
\]

absolutely convergent in `Re(s)>1/2+epsilon`, where it analytically continues the classical Dirichlet series `1/zeta(s)`. Any zero in that half-plane would contradict holomorphy. Pintz's contribution is therefore the stronger two-sided/full-limit fidelity `(1)`--`(3)` and the terminal-window comparison, not the bare RH implication of the mean-absolute upper bound.

## 1. The zero-edge exponent of `Z(x)` is exactly `vartheta`

The deduction from Pintz's Theorem 2.2 to `(3)` is elementary once `(1)` is granted.

For every zero `rho=beta+i gamma` with `gamma>0`,

\[
\frac{x^\beta}{\gamma}\le C_\rho x^\vartheta,
\]

so

\[
\limsup_{x\to\infty}\frac{\log Z(x)}{\log x}\le\vartheta.
\tag{5}
\]

Conversely, for any `eta>0`, the definition of the supremum supplies a fixed zero `rho_eta=beta_eta+i gamma_eta` with

\[
\beta_\eta>\vartheta-\eta.
\]

Then

\[
Z(x)\ge\frac{x^{\beta_\eta}}{\gamma_\eta},
\]

and hence

\[
\liminf_{x\to\infty}\frac{\log Z(x)}{\log x}\ge\vartheta-\eta.
\]

Letting `eta` tend to zero gives

\[
\frac{\log Z(x)}{\log x}\longrightarrow\vartheta.
\tag{6}
\]

Combining `(6)` with `(1)` proves `(3)`. Thus, if Pintz's theorem survives audit, for every fixed `epsilon>0` and all sufficiently large `x`,

\[
x^{\vartheta-\varepsilon}
\le D_M(x)
\le x^{\vartheta+\varepsilon},
\tag{7}
\]

and the analogous logarithmic-order statement holds for `S_{M,delta}`.

## 2. What is elementary and what genuinely belongs to Pintz

The classical pointwise Mertens RH criterion

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0
\tag{8}
\]

trivially implies the corresponding mean-absolute upper bound. The reverse implication in `(4)` is also classical-mechanism mathematics after `MC-115`: although an absolute mean does not generically recover pointwise values, it controls the weighted absolute integral strongly enough to continue the Möbius Mellin transform and exclude zeros.

Therefore the correct hierarchy is:

- **mean-absolute RH-scale upper bound implies RH:** exact and independent of `MC-S19`, by `MC-115`;
- **a zero at real part `beta` forces the limsup mean exponent to be at least `beta`:** also exact from the contrapositive of `MC-115`;
- **the logarithmic exponent of `D_M(x)` actually converges to `vartheta`, with the same exponent for a terminal-window maximum:** the substantially stronger statement supplied by Pintz and still under audit here.

Sparse spikes remain a valid reason why no generic real-variable pointwise recovery exists. They are simply irrelevant to the analytic implication `(4)`: zero exclusion comes from Mellin convergence, not from reconstructing `M(x)` pointwise.

## 3. Relation to the local-to-global obstruction chain

This finding does not weaken the barriers in `MC-001` or `MC-006`. `MC-001` shows that almost-all short-interval magnitude plus exceptional-set measure, passed through triangle inequality, produces an error budget whose known logarithmic rates do not yield fixed-power global saving. `MC-006` similarly shows that the available averaged two-point Chowla rate gives only logarithmic saving through the audited black-box van der Corput route.

What changes is only the endpoint that a successful arithmetic transfer must hit. A source-natural local, correlation, bilinear, or multiscale argument need not prove the pointwise estimate `(8)` if it can instead prove

\[
D_M(x)\ll_\varepsilon x^{1/2+\varepsilon}.
\tag{9}
\]

Once `(9)` is available, `MC-115` supplies the exact zero-free implication with no dependency on the fresh Pintz theorem. The current local and averaged inputs still do not deliver `(9)` at polynomial strength.

## 4. The stronger off-critical signature supplied by Pintz

The README asks whether a hypothetical off-critical zero forces a detectable signature in Möbius observables beyond merely rewriting `1/zeta(s)`. `MC-115` already proves the robust one-sided statement

\[
\zeta(\rho)=0,\quad\operatorname{Re}\rho=\beta
\Longrightarrow
D_M(x)\ne O(x^\alpha)
\quad(\alpha<\beta),
\tag{10}
\]

which is a limsup power obstruction.

Pintz's Theorem 2.2, if fully verified, is stronger:

\[
D_M(x)=x^{\vartheta+o(1)}
\quad\text{in logarithmic order},
\tag{11}
\]

and simultaneously

\[
S_{M,\delta}(x)=x^{\vartheta+o(1)}
\quad\text{in logarithmic order}
\tag{12}
\]

for every fixed positive `delta`. It therefore rules out deep persistent downward exponent fluctuations and ties the global average to a broad terminal maximum. That full two-sided rigidity is the part of this finding that remains genuinely dependent on `MC-S19`.

## Prior art and novelty assessment

`MC-S19` is the primary source. The current arXiv metadata is `arXiv:2608.24878v2`, revised 1 September 2026. Theorems 2.1--2.2 state the asymptotic comparisons used in `(1)`--`(3)`. The paper traces its mean-absolute lower-bound program back to Pintz's 1982/83 work and presents the new theorem as the Möbius analogue of earlier sharp results for the prime-number-theorem error term.

No novelty is claimed here for Pintz's theorem, the classical Mertens criterion, the definition of `vartheta`, or the direct Mellin mechanism now separated into `MC-115`. The Mathia-derived content of this finding is the research-facing extraction of the full logarithmic zero-edge consequence and its audited dependency boundary.

The v2 text still displays the three proof-presentation defects already isolated in the audit chain:

- the signed denominator `gamma` in equation `(2.10)` although the positive `|gamma|` quantity is required;
- the dropped shifted-height factor in the displayed kernel estimate `(6.23)`;
- the `epsilon'=epsilon/9` cap in Section 7 being applied down to the wider `epsilon/8` window.

`MC-010`, `MC-011`, and `MC-012` give explicit repairs for those defects, but the remaining Section 5 contour/nonvanishing input has not been reconstructed end-to-end. A newer arXiv version therefore does not by itself justify upgrading this finding beyond `NEEDS-AUDIT`.

## Boundaries and falsification tests

This finding does **not** improve the unconditional upper bound for `M(x)` or `D_M(x)`, and it does not show that the mean-absolute target `(9)` is arithmetically easy.

The exact RH equivalence `(4)` is no longer part of the Pintz audit surface; falsifying Pintz's stronger theorem would not remove the Mellin implication in `MC-115`. What remains audit-sensitive here is the full-limit assertion `(3)` and the terminal-window equivalence `(12)`.

Finite computations of `M(x)` cannot validate those asymptotic statements. The decisive remaining audit is theorem-level: reconstruct the load-bearing Section 5 upper-bound contour and the rest of the `vartheta=1` assembly under the precise parameter ranges, while preserving the repairs already recorded in `MC-010`--`MC-012`.

If that audit fails, `(1)`--`(3)` and `(11)`--`(12)` must be narrowed or withdrawn. `MC-115` and the mean-absolute RH criterion `(4)` would remain unaffected.

## Consequences for the line

The line should now treat the mean-absolute endpoint in two layers. First, `D_M(x)=O_epsilon(x^(1/2+epsilon))` is an **exact RH-complete arithmetic target** by the direct transform argument of `MC-115`. Second, Pintz's fresh theorem proposes a much more rigid description of the entire mean-absolute growth profile and its near-end maxima, but that stronger statement remains under active proof audit.

A future arithmetic mechanism can therefore aim at the weaker mean-absolute upper bound without carrying the fresh-preprint dependency into the final zero-free step. The real unresolved burden is still upstream: obtain the polynomial mean-absolute cancellation from source-natural local, multiscale, bilinear, or multiplicative information that is independently weaker than the target itself.