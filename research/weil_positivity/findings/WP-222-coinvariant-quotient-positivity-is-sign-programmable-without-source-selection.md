# WP-222 — Coinvariant quotient positivity is sign-programmable without source selection

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + ONE-PRIME + COINVARIANT-MODEL-SPACE + TRUNCATED-TOEPLITZ + SIGN-PROGRAMMABILITY + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICAL-TOOLS + NOT-A-WEIL-BRIDGE`.

`WP-221` proves that every nonzero source-shift-invariant Hardy submodule retains both signs of the critical Bost--Connes finite-place Weil defect. It deliberately leaves quotient/coinvariant geometry open because compression to a coinvariant model space does not preserve the localization mechanism used for invariant submodules.

That escape is real but underdetermined. For every fixed finite rank `N>=1`, the same one-prime source Toeplitz defect admits finite-dimensional coinvariant compressions that are strictly positive definite and others that are strictly negative definite. The sign can be selected by moving the zero of a repeated-root finite Blaschke quotient toward a boundary point where the source symbol has the desired sign. By contrast, the untuned polynomial quotient `K_{z^N}` is indefinite for every `N>=2`.

Thus **quotient positivity by itself is not source-forced evidence**. A Bost--Connes quotient/conditioning proposal survives only if the source arithmetic, KMS/modular data, or a genuine finite--archimedean completion canonically selects the quotient before the Weil sign is inspected. Choosing an inner function because its compression is positive is target coding in exactly the sense excluded by the research mandate.

## 1. One-prime source block

Fix a prime `p` and put

\[
\rho=p^{-1/2}\in(0,1).
\tag{1}
\]

The critical one-prime block isolated in `WP-216`--`WP-221` is

\[
A_\rho=(\log p)(I-T_{P_\rho})=T_{w_\rho}
\tag{2}
\]

on `H^2(D)`, where

\[
P_\rho(e^{it})
=\frac{1-\rho^2}{|1-\rho e^{it}|^2},
\qquad
w_\rho(e^{it})=(\log p)(1-P_\rho(e^{it})).
\tag{3}
\]

The symbol changes sign. At the two distinguished boundary points,

\[
w_\rho(-1)
=(\log p)\frac{2\rho}{1+\rho}>0,
\tag{4}
\]

while

\[
w_\rho(1)
=-(\log p)\frac{2\rho}{1-\rho}<0.
\tag{5}
\]

`WP-221` shows that no nonzero invariant submodule can hide either sign. We now test the orthogonal quotient category.

## 2. Finite model-space quotients can localize any continuous symbol value

Let `Theta` be inner and write the standard model/coinvariant space

\[
K_\Theta=H^2\ominus \Theta H^2.
\tag{6}
\]

For a bounded real symbol `w`, its compression is the self-adjoint truncated Toeplitz operator

\[
A_w^\Theta=P_{K_\Theta}T_w|_{K_\Theta}.
\tag{7}
\]

Fix `a in D`, let

\[
b_a(z)=\frac{z-a}{1-\overline a z},
\qquad
\Theta_a=b_a^N,
\tag{8}
\]

and keep `N` finite and fixed. A Takenaka--Malmquist basis of `K_{b_a^N}` is

\[
e_{a,k}(z)
=\frac{\sqrt{1-|a|^2}}{1-\overline a z}\,b_a(z)^k,
\qquad 0\le k<N.
\tag{9}
\]

On the unit circle, `|b_a|=1`, so for all `j,k`,

\[
|e_{a,j}(\xi)\overline{e_{a,k}(\xi)}|
=\frac{1-|a|^2}{|1-\overline a\xi|^2}
=:P_a(\xi).
\tag{10}
\]

Let `w in C(T,R)` and let `zeta in T`. Since the vectors in (9) are orthonormal,

\[
\begin{aligned}
&\left|\left\langle
(A_w^{b_a^N}-w(\zeta)I)e_{a,k},e_{a,j}
\right\rangle\right|\\
&\qquad\le
\int_{\mathbb T}|w(\xi)-w(\zeta)|P_a(\xi)\,dm(\xi).
\end{aligned}
\tag{11}
\]

As `a -> zeta` radially (or nontangentially), the Poisson measures `P_a dm` converge weakly to the point mass at `zeta`. Continuity of `w` therefore sends the right-hand side of (11) to zero. Because `N` is fixed, entrywise convergence in the basis (9) is norm convergence:

\[
\boxed{
\|A_w^{b_a^N}-w(\zeta)I_N\|\longrightarrow0
\quad(a\to\zeta).
}
\tag{12}
\]

This is the exact mechanism missed by the invariant-submodule no-go. A repeated-root quotient can move an entire fixed finite-dimensional compression toward whichever boundary value of the scalar symbol its zero approaches.

## 3. The Bost--Connes defect therefore has quotients of either strict sign

Apply (12) to `w=w_rho`. By (4), for every fixed `N` there is an `a` sufficiently close to `-1` such that

\[
A_{w_\rho}^{b_a^N}\succ0.
\tag{13}
\]

By (5), there is another `a` sufficiently close to `+1` such that

\[
A_{w_\rho}^{b_a^N}\prec0.
\tag{14}
\]

Hence

\[
\boxed{
\text{the same source block admits finite coinvariant quotients of either strict sign.}
}
\tag{15}
\]

No arithmetic change occurred between (13) and (14). Only the quotient parameter changed. Positivity of one such compression therefore cannot be credited to the Bost--Connes source unless the source independently singles out that quotient.

The statement is stronger than merely observing that some arbitrary compression of an indefinite operator can be positive. The positive and negative examples live in the standard finite model-space/truncated-Toeplitz category naturally adjacent to the invariant Hardy modules tested in `WP-219`--`WP-221`, and the sign selection is controlled explicitly by a one-parameter finite-Blaschke family.

## 4. Matched canonical control: the polynomial quotient stays indefinite

The most immediate untuned finite quotient is

\[
\Theta(z)=z^N,
\qquad
K_{z^N}=\operatorname{span}\{1,z,\ldots,z^{N-1}\}.
\tag{16}
\]

Since the Fourier coefficients of `P_rho` are `rho^{|j-k|}`, the compressed matrix of (2) is

\[
A_{w_\rho}^{z^N}
=(\log p)\,[\delta_{jk}-\rho^{|j-k|}]_{0\le j,k<N}.
\tag{17}
\]

Its leading `2 x 2` principal block is

\[
(\log p)
\begin{pmatrix}
0&-\rho\\
-\rho&0
\end{pmatrix},
\tag{18}
\]

with eigenvalues `+-(log p)rho`. Equivalently the two vectors supported on the first two monomials with coefficients `(1,1)` and `(1,-1)` have opposite-sign quadratic forms. Thus

\[
\boxed{
A_{w_\rho}^{z^N}\text{ is indefinite for every }N\ge2,
}
\tag{19}
\]

while for `N=1` it is the zero operator.

This control matters because it separates **existence of a positive quotient** from **canonicality of the quotient**. The elementary source-aligned truncation does not repair the sign; strict positivity appears only after choosing a different quotient geometry.

## 5. Aggressive falsification and matched non-arithmetic controls

Nothing in Sections 2--4 uses primality. Replace `(log p,rho)` by arbitrary constants

\[
c>0,
\qquad 0<r<1,
\tag{20}
\]

and set `w=c(1-P_r)`. The same theorem produces positive repeated-root model-space compressions near `-1`, negative ones near `+1`, and an indefinite polynomial compression for every rank at least two. The effect therefore survives arbitrary-generator and generalized-product controls.

This is appropriate for the negative conclusion: the sign-programming freedom is an operator-theoretic feature of choosing a quotient, not arithmetic specificity. Conversely, a future positive proposal cannot point to the mere existence of a positive model-space compression as evidence that the Riemann source chose it.

Several possible overclaims are explicitly excluded.

First, (15) does **not** say that every coinvariant quotient is arbitrary or that no Bost--Connes quotient can be canonical. It says that the category is large enough to encode the desired sign, so canonical source selection is an additional theorem that must be proved.

Second, the argument is finite-rank. It does not classify infinite inner functions, de Branges--Rovnyak spaces, unbounded form quotients, shorted operators, or non-Hardy KMS/GNS quotients. Those remain possible only if their defining data are fixed independently of the target sign.

Third, no archimedean or polar term is generated. Even a canonically selected positive finite-place quotient would still need a single source-derived finite--archimedean/global construction matching the completed Weil form and carrying an independent positivity theorem.

## 6. Prior-art and novelty audit

The operator-theoretic setting is classical. Sarason's 2007 theory of truncated Toeplitz operators studies precisely compressions `P_{K_Theta}T_w|_{K_Theta}` on model spaces `K_Theta=H^2\ominus Theta H^2`. Cima, Ross, and Wogen (2008), *Truncated Toeplitz Operators on Finite Dimensional Spaces*, studies their finite-dimensional realizations for finite Blaschke products. Takenaka--Malmquist bases and Poisson-kernel concentration are standard Hardy/model-space tools.

No novelty is claimed for model spaces, finite Blaschke products, truncated Toeplitz operators, Takenaka--Malmquist bases, or Poisson localization. Equation (12) is included with a complete proof because it is the exact bridge needed for the Mathia falsification and avoids relying on a stronger literature theorem than necessary.

The durable Mathia delta is the application to the specific critical Bost--Connes Weil defect left open by `WP-221`: **coinvariant escape exists, but positivity in that category is target-programmable unless the source supplies an independent quotient-selection law**. A literature audit found no reason to identify an arbitrary finite-Blaschke model-space choice with a canonical Bost--Connes/KMS arithmetic quotient, and no such source-selection theorem is asserted here.

## 7. Consequences for the Weil-positivity line

`WP-219`--`WP-221` showed that ordinary source-shift-invariant restrictions cannot repair the critical finite-place sign. The present result prevents the opposite mistake of treating an arbitrary non-invariant quotient as a solution merely because positivity can now be obtained.

The surviving route is narrower:

\[
\boxed{
\text{source/KMS/global geometry}
\Longrightarrow
\text{canonical quotient or shorting}
\Longrightarrow
\text{correct finite Weil orientation}
\Longrightarrow
\text{finite--archimedean completed form with independent sign theorem}.
}
\tag{21}
\]

The first arrow is now load-bearing. If the quotient, inner function, boundary condition, or shorting datum is selected after looking at positivity, the construction is disqualified as target coding. If a source-forced quotient is found, it must additionally survive the generalized-product controls above and generate the Gamma and polar pieces without a separate hand-picked correction.

So `WP-222` does not establish Weil positivity or RH. It is a decisive narrowing of the principal quotient/coinvariant loophole deliberately left open by `WP-221`: quotient positivity is available, but it is too programmable to count unless Mathia or the Bost--Connes source canonically fixes the quotient before the target sign is known.
