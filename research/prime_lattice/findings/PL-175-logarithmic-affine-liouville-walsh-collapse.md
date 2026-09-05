# PL-175 — Logarithmic affine Liouville Walsh sectors collapse through odd order and degree two

## Claim

The nonlinear fixed-shift escape left open by `PL-174` is substantially narrower than “higher-order data” suggests. For the canonical Liouville parity

\[
\lambda(n)=(-1)^{\Omega(n)}=(-1)^{\sum_p v_p(n)},
\]

logarithmically averaged fixed affine translates already have the same expectations as independent fair signs for every Walsh observable whose nonconstant Fourier-Walsh support consists only of odd degrees and degree two.

Precisely, fix distinct positive shifts `h_1,...,h_r` and let

\[
H_X=\sum_{n\le X}\frac1n,
\qquad
L_j(n)=\lambda(n+h_j).
\]

For a function `F:{-1,+1}^r -> C`, write its Walsh expansion

\[
F(\varepsilon)=\sum_{S\subseteq[r]}\widehat F(S)
\prod_{j\in S}\varepsilon_j.
\]

If

\[
\widehat F(S)=0
\quad\text{for every even }|S|\ge4,
\]

then the published logarithmic two-point Chowla theorem of Tao together with the published odd-order logarithmic Chowla theorem of Tao--Teräväinen imply

\[
\frac1{H_X}\sum_{n\le X}\frac{F(L_1(n),\ldots,L_r(n))}{n}
\longrightarrow
\widehat F(\varnothing)
=
2^{-r}\sum_{\varepsilon\in\{\pm1\}^r}F(\varepsilon).
\]

In particular, for **three distinct fixed shifts**, every function on the three signs satisfies the hypothesis automatically. Hence

\[
(L_1,L_2,L_3)
\]

has the full independent-fair-sign joint law under canonical logarithmic averaging: every one of the eight sign patterns has limiting logarithmic density `1/8`. Thus nonlinear observables of at most three fixed affine Liouville translates are not a surviving non-Haar carrier after `PL-174`.

More generally, the cited theorems annihilate every odd Walsh sector, at arbitrary fixed odd order, and the degree-two sector. The **first Walsh degree left uncontrolled by these theorem inputs is even degree four**. This last sentence is a boundary statement, not an assertion that a fourth-order limit exists, is nonzero, or is useful for RH.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION`. The odd-order Chowla theorem and the three-sign-pattern consequence are prior art. The line-local content is the explicit Walsh/operator audit showing exactly which part of the `PL-174` nonlinear escape is already universal and which even-order sector first remains outside the cited theorems.

## Exact Walsh derivation

For each subset `S subseteq [r]`, set

\[
C_X(S)=\frac1{H_X}\sum_{n\le X}\frac1n
\prod_{j\in S}\lambda(n+h_j).
\]

The empty-set coefficient is exact:

\[
C_X(\varnothing)=1.
\]

If `|S|` is odd, Tao--Teräväinen's odd-order theorem gives

\[
\frac1{\log X}\sum_{n\le X}\frac1n
\prod_{j\in S}\lambda(n+h_j)=o(1)
\]

for fixed shifts. Since `H_X/log X -> 1`, this yields

\[
C_X(S)\to0
\qquad (|S|\text{ odd}).
\]

If `|S|=2`, the two shifts are distinct by hypothesis, and Tao's logarithmically averaged two-point Chowla theorem gives the same conclusion:

\[
C_X(S)\to0
\qquad (|S|=2).
\]

Therefore, whenever the Walsh expansion of `F` has no nonzero even coefficient of degree at least four,

\[
\begin{aligned}
\frac1{H_X}\sum_{n\le X}\frac{F(L_1(n),\ldots,L_r(n))}{n}
&=\sum_{S\subseteq[r]}\widehat F(S)C_X(S)\\
&\longrightarrow \widehat F(\varnothing).
\end{aligned}
\]

The last quantity is exactly the expectation of `F` under product Haar measure on the finite cube `{-1,+1}^r`.

For `r=3`, there are no even subsets of size at least four, so the result applies to **every** function `F`. Taking

\[
F_{\epsilon}(x_1,x_2,x_3)
=\prod_{j=1}^3\frac{1+\epsilon_jx_j}{2},
\qquad \epsilon_j\in\{\pm1\},
\]

gives

\[
\frac1{H_X}\sum_{n\le X}\frac{
\mathbf 1_{(L_1(n),L_2(n),L_3(n))=\epsilon}}{n}
\longrightarrow \frac18.
\]

This is a complete finite-dimensional statement for a fixed triple, not merely vanishing of its third moment.

## Prime-lattice and operator interpretation

`PL-172`--`PL-174` isolate the affine channel by starting from the intrinsic exponent-lattice character

\[
\lambda(n)=(-1)^{\sum_p v_p(n)}
\]

and then applying the genuinely nonmultiplicative operation `n -> n+h`. `PL-174` proves that the canonical logarithmic **second-order** Gram/Herglotz spectrum of the resulting translates is Haar-flat.

A natural reaction is to replace quadratic observables by a nonlinear function of several shifted parity operators. The present calculation shows that this does not create a new arithmetic carrier merely by passing to third order. If `J_h e_n=lambda(n+h)e_n`, then every fixed diagonal observable generated from at most three distinct `J_h` has, under the logarithmic state

\[
\phi_X(D)=\frac1{H_X}\sum_{n\le X}\frac{\langle De_n,e_n\rangle}{n},
\]

the same limiting value as the corresponding polynomial in three independent Rademacher signs.

More generally, a finite polynomial in fixed shifted parities can retain nonuniversal information under this state only through its even Walsh components of degree at least four. Odd components of any fixed degree are already killed by the odd-order theorem, while quadratic components are killed by Tao's two-point theorem.

This is a stronger matched-control obstruction than `PL-174`'s two-point spectral flatness: for three fixed translates, **the entire joint law**, and hence every bounded nonlinear readout of those three signs, agrees with the Bernoulli control in the logarithmic limit. It still does not imply that the full logarithmic Liouville process is Bernoulli.

## Prior-art / novelty audit

The result is deliberately classified as prior-art redirect rather than a new number-theoretic theorem.

Primary odd-order source:

- Terence Tao, Joni Teräväinen, “Odd order cases of the logarithmically averaged Chowla conjecture,” *Journal de Théorie des Nombres de Bordeaux* **30**(3) (2018), 997--1015. DOI: https://doi.org/10.5802/jtnb.1062. Theorem 1.1 proves the logarithmically averaged Chowla estimate for every fixed odd number of Liouville affine forms.

Broader structural source and explicit sign-pattern prior art:

- Terence Tao, Joni Teräväinen, “The structure of logarithmically averaged correlations of multiplicative functions, with applications to the Chowla and Elliott conjectures,” *Duke Mathematical Journal* **168**(11) (2019), 1977--2027. DOI: https://doi.org/10.1215/00127094-2019-0002. The paper derives the odd-order cases in a broader multiplicative-correlation framework and explicitly lists the conjectured logarithmic density of all Liouville sign patterns of length up to three among its applications.

Degree-two input:

- Terence Tao, “The logarithmically averaged Chowla and Elliott conjectures for two-point correlations,” *Forum of Mathematics, Pi* **4** (2016), e8. DOI: https://doi.org/10.1017/fmp.2016.6. This is already the primary theorem used in `PL-174`.

Thus the `r=3` Bernoulli law is not a novelty claim; for consecutive length-three patterns it is explicit prior art, and for arbitrary fixed distinct triples it is an immediate Walsh consequence of the same published correlation theorems. The operator/Walsh packaging is retained only because it decisively narrows the specific prime-lattice research clue.

## Boundary conditions and adversarial checks

- **Logarithmic, not ordinary Cesaro.** No estimate for `X^(-1) sum_(n<=X)` is inferred. Ordinary fixed-shift Chowla remains stronger.
- **Fixed shifts only.** The argument does not give uniformity when the shifts grow with `X`.
- **No all-order Bernoulli claim.** Full uniformity of every fixed triple does not imply that the infinite shift process is Bernoulli or mixing of all orders.
- **Degree four is only the first uncontrolled sector here.** The cited results do not establish that a fourth-order correlation has a non-Haar limit or even that the needed limit exists. The same caution applies to higher even orders.
- **No analytic-continuation claim.** The weight `1/n` is a logarithmic statistical average; nothing here analytically continues the shifted-correlation Dirichlet series to its boundary.
- **No arbitrary nonlinear escape.** Calling a statistic “nonlinear” is insufficient. Its Walsh support must actually contain an even component of degree at least four, or the construction must leave the fixed-shift logarithmic regime by another independently justified mechanism.
- **No RH implication imported.** The theorem-controlled Bernoulli limit removes information from a proposed carrier; it does not prove a statement about zeta zeros.

## Consequence for the research line

The `PL-174` escape “higher-order or nonlinear observables” should be read much more narrowly. In the canonical fixed-shift logarithmic state, odd order is already theoremically flat at **every** odd degree, degree two is flat, and every three-sign nonlinear observable is completely Bernoulli-universal.

For the active affine clue, the first fixed-shift nonlinear channel not already removed by these published theorems is therefore an **even Walsh component of degree at least four**, beginning with four-point logarithmic Liouville correlation. Other genuinely different escapes remain outside the result: source-forced non-diffuse/growing shift constructions, ordinary Cesaro correlations, and completed or target-relative couplings formed before taking the logarithmic limit.

This does not recommend fourth-order correlation as an RH mechanism. It only removes lower-order nonlinear observables from the search and supplies a precise falsification test for any future affine candidate: expand the proposed fixed-shift readout in Walsh characters first, and reject it immediately if all nonconstant support lies in odd degrees or degree two.