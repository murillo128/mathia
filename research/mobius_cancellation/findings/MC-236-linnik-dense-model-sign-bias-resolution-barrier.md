# MC-236 — Linnik dense modeling preserves principal sign bias and the published transference has only subpower relative resolution

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-235` shows that the Matomäki--Teräväinen Linnik machinery already gives each Möbius sign essentially full occupancy exponent in every fixed interior source-selected hard progression, but does not control the signed difference. Inspecting the dense-model and transference stages identifies a sharper reason why the published argument does not automatically upgrade sign abundance to the near-balance needed by the first-shell route.

For each sign-specific sparse function `f_k^+`, `f_k^-` and its dense model `g_k^+`, `g_k^-`, Proposition 3.3(iv) of Matomäki--Teräväinen preserves the principal character coefficient **exactly**:

\[
\mathbb E g_k^\Delta=\mathbb E f_k^\Delta
\qquad (\Delta\in\{+,-\}).
\]

Therefore

\[
\boxed{
\mathbb E(g_k^+-g_k^-)=\mathbb E(f_k^+-f_k^-)
}
\tag{1}
\]

with no contraction factor. The dense-model replacement transports a pre-existing sign imbalance; it does not regularize it toward zero.

The subsequent combinatorial stage is intentionally one-sided. It thresholds the nonnegative models into sets

\[
A_k^\Delta=\{a:g_k^\Delta(a)\ge \varepsilon^2\}
\]

and proves coverage/lower-bound statements for sign-specific triple convolutions. In the basic argument Lemma 5.7 gives, for example,

\[
|A^+|+|A^-|\ge (1-\varepsilon)\varphi(q),
\tag{2}
\]

while the final Theorem 1.2 proof asks only for a positive lower bound on a sparse convolution for each requested output sign. Neither statement bounds the difference of the two sign masses. Thus the exact principal-mode information in `(1)` is not converted by the published support/product-set argument into a signed discrepancy estimate.

There is also a quantitative resolution barrier to the most direct repair, namely subtracting separately transferred positive and negative convolutions. In the general Theorem 1.2 transference lemma, one explicit error term is

\[
E_1
\ll
\frac{\varphi(q)}q\frac{(\log q)^3}{q}\,Q_1^{-1/90},
\tag{3}
\]

whereas the one-sided main threshold used in the final proof is

\[
M_1
\asymp
\frac{\varphi(q)}q\frac{(\log q)^3}{q}\,
\frac{Q_1^{-1/100}}{\log^2 Q_1}.
\tag{4}
\]

Consequently the **published bound** has relative precision only

\[
\frac{E_1}{M_1}
\ll
Q_1^{-1/900}\log^2 Q_1.
\tag{5}
\]

For the Möbius specialization used in Corollary 1.3 and `MC-235`, `Q_1=L_1(q)=q^{o(1)}`. Hence `(5)` is only `q^{-o(1)}` resolution. The dense-model character approximation itself is also run with

\[
\delta=(\log q)^{-1/4}=q^{-o(1)}.
\tag{6}
\]

By contrast, a fixed interior first-shell component with

\[
q=X^{2\alpha+o(1)},\qquad
Z=X^{1-\beta+o(1)},\qquad
\alpha>0,\qquad
d:=\frac12-2\alpha-\beta>0
\]

requires the relative sign bias from `MC-235` to satisfy

\[
\frac{|N_+-N_-|}{N_{\rm sf}}
\le X^{-d+o(1)}
=q^{-d/(2\alpha)+o(1)},
\tag{7}
\]

a **fixed negative power of `q`**. Therefore the currently published dense-model/transference estimates cannot certify `(7)` merely by transferring the two signs separately and subtracting: their stated comparison tolerance is subpower, asymptotically coarser than the fixed-power target.

This is not an impossibility theorem for the underlying method. A new argument could couple the two signs *before* absolute values and thresholding, derive a power-resolution estimate for a signed Fourier/convolution combination, or obtain cancellation only after recombining the smooth-dilation family of `MC-233`. What is ruled out is the naive continuation in which the existing nonnegative dense models, support expansion, and published separate-sign transference inequalities are reused unchanged and then subtracted at the end.

No new bound for `M_mu(Z;q,a)`, `B_S`, `M(X)`, or the zeta zero set is proved here.

## 1. Exact mean preservation identifies the missing upstream quantity

Matomäki and Teräväinen's Proposition 3.3 constructs a bounded nonnegative model `g` for a sparse nonnegative function `f`. Besides approximating all character coefficients, property (iv) states exactly

\[
\mathbb E_{a\in\mathbb Z_q^\times}g(a)
=
\mathbb E_{n\in[I]_q}f(n).
\tag{8}
\]

The theorem is applied separately to the positive- and negative-sign detectors. Subtracting the two identities gives `(1)`.

This matters because the principal character is precisely the frequency carrying the total signed mass of a sign split. Pseudorandomness of the majorant and the existence of a bounded dense model do not create cancellation in that coefficient. If the original sign-specific block has a large mean imbalance, the corresponding pair of dense models has the same imbalance.

For nonprincipal characters the generic dense-model guarantee is only

\[
|\widehat f(\chi)-\widehat g(\chi)|\le\delta,
\tag{9}
\]

with the paper's choice `(6)`. Thus even away from the principal mode, the model theorem as instantiated is not itself a fixed-power-resolution signed approximation. Any power-scale balance theorem must therefore use additional arithmetic input or a more delicate signed transference statement, rather than expecting the dense-model theorem to suppress the bias automatically.

## 2. Thresholding changes the question from amplitude to coverage

After dense modeling, the proof defines `A^Delta={a:g^Delta(a)>=epsilon^2}`. Lemma 5.7 uses exact preservation of the **sum** of the two model means to obtain `(2)` and obtains lower bounds on intersections with index-two cosets. The information demanded by the first-shell amplitude problem is different: it is a quantitative comparison between the two signs.

The later product-set argument is correspondingly a coverage theorem. Proposition 5.8 assumes a large triple convolution for one sign and uses separate prime and square-free factors to force either desired output sign. In the full theorem, equation (10.1) again asks for a positive lower bound for one sign-specific sparse convolution. These are exactly the mechanisms that explain why the proof is powerful enough to produce both signs in every residue class while remaining silent about their near-balance.

This does **not** say the threshold sets contain no information about imbalance. It says the published deductions from them use support size, coset concentration and one-sided convolution lower bounds, not a theorem that converts `A_k^+` versus `A_k^-` into a power-saving signed discrepancy.

## 3. The published transference tolerance is too coarse for the fixed interior target

Lemma 8.2 compares each sparse sign-pattern convolution `S` to its dense analogue `T`. Its first error contribution is `(3)`. The final case analysis targets `(4)`, up to the same common normalization factors. Dividing gives `(5)`.

In the Möbius corollary, the parameter selected to eliminate the character obstruction satisfies `Q_1=q^{o(1)}`; this is the same subpower fact used in `MC-235` to extract full-exponent sign abundance. Hence every fixed power `q^{-kappa}` with `kappa>0` eventually lies below the relative scale provided by `(5)`.

Now fix an interior source scaling pair with `alpha>0`. The deficit

\[
d=\frac12-2\alpha-\beta
\]

is positive and fixed. Equation `(7)` then asks for a fixed-power relative imbalance. If one separately writes

\[
S^+=T^++O(E),\qquad S^-=T^-+O(E)
\]

using the published transference estimate, subtraction gives

\[
S^+-S^-=(T^+-T^-)+O(E),
\]

but the available error budget is not fine enough to certify a signal at the scale required by `(7)`. One would first need a cancellation estimate for the **signed combined expression** whose error also enjoys fixed-power resolution, or a different route that never pays the two separate absolute errors.

The second term in Lemma 8.2 depends on the `U`-mass and additional logarithmic factors; nothing in the published theorem upgrades the comparison to a uniform fixed-power relative signed estimate. The first term alone is enough to show that the stated bound is not already such an estimate. This is a limitation of what the published inequalities certify, not a lower bound on the true transference error.

## 4. Prior-art and novelty boundary

The dense-model theorem, exact mean preservation, threshold sets, transference lemma, and final one-sided convolution threshold are all prior art from Kaisa Matomäki and Joni Teräväinen, *Linnik's problem for multiplicative functions*, arXiv:2605.27833v1 (27 May 2026). Proposition 3.3 itself is stated there as a slight interval variant of Proposition 4.1 from Matomäki--Teräväinen, *Products of primes in arithmetic progressions*, J. Reine Angew. Math. 808 (2024), 193--240.

The closest broader progression-distribution result located in the source paper is Klurman--Mangerel--Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proc. Lond. Math. Soc. 127 (2023), 366--446. It gives variance/distribution information for almost all moduli, while the Linnik paper explicitly notes that its zero-free/zero-density route does not extend to every modulus without substantially stronger zero-free information. That quantifier surface is different from the source-selected individual progression required here.

No novelty is claimed for mean preservation, dense modeling, product-set expansion, or the numerical exponents `1/90` and `1/100`. The Mathia-specific contribution is the information-flow and scale audit: combining those exact published properties with the fixed-interior relative-bias requirement isolated in `MC-235` shows where the existing Linnik architecture stops being an amplitude argument.

Primary sources audited:

- K. Matomäki and J. Teräväinen, *Linnik's problem for multiplicative functions*, arXiv:2605.27833v1, especially Proposition 3.3, Lemma 5.7, Proposition 5.8, Lemma 8.2 and equation (10.1): https://arxiv.org/abs/2605.27833
- O. Klurman, A. P. Mangerel and J. Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proc. Lond. Math. Soc. 127 (2023), 366--446, arXiv:1909.12280: https://arxiv.org/abs/1909.12280

## 5. Boundaries and falsification tests

- Equation `(1)` concerns the sign-specific sparse blocks to which the dense-model theorem is applied. It is not by itself an identity for the final full progression sum.
- Mean preservation does not rule out cancellation created later by a genuinely signed combination of several factors or by recombination across the smooth-dilation family.
- The comparison `(5)` concerns the **published upper bound** for transference error. The actual error can be smaller; a sharper theorem could therefore evade this barrier.
- The fixed-power comparison `(7)` is stated for fixed `alpha>0` and fixed interior deficit `d>0`. The `alpha=0` regime and moving sequences with `d->0` require a separate scale audit.
- Separate lower bounds for `N_+` and `N_-`, even at full occupancy exponent as in `MC-235`, do not control their difference. This finding does not reinterpret abundance as discrepancy.
- A successful repair must not import the desired progression cancellation through a GRH-strength character estimate or zero-free region without accounting for that circularity.

## Consequence for the live frontier

The immediate Linnik-proof mining route is now narrower than after `MC-235`. The dense-model theorem preserves the principal sign bias exactly, while the published downstream machinery thresholds the models for coverage and transfers separate nonnegative convolutions at only subpower relative resolution in the Möbius specialization.

A viable continuation must therefore expose a **signed comparative invariant before the one-sided quotient**. The natural object is not another lower bound for `f_k^+` and `f_k^-` separately, but a controlled combination such as `F_k^+(chi)-F_k^-(chi)` or a signed convolution in which the positive and negative contributions are coupled before triangle inequalities and support thresholding. To help the first-shell route at a fixed interior point, that new estimate must ultimately have fixed-power resolution matching `(7)`, or it must exploit aggregate cancellation across the smooth-dilation components so that the componentwise target itself is avoided.