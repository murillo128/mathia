# MC-331 — Common-coefficient prefilters cannot cross the quartic horizon

**Status:** `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint and common-modulus character family of `MC-329`–`MC-330`. Let

\[
G=\mathbf F_2^R,
\qquad
\chi_a=\prod_{i=1}^R\chi_i^{a_i}
\quad(a\in G),
\]

and let `\mathcal A_y` be the prime shell, with

\[
A:=|\mathcal A_y|.
\]

For each shell prime `r`, write its generator-sign cell as `s(r)\in G`, normalized so that

\[
\chi_a(r)=(-1)^{a\cdot s(r)}.
\tag{1}
\]

At the exact reciprocal endpoint, the shell is partitioned equally among the `R` one-defect cells

\[
S=\{\mathbf1+e_j:1\le j\le R\},
\qquad
\#\{r\in\mathcal A_y:s(r)=s\}=\frac AR
\quad(s\in S),
\tag{2}
\]

and the normalized unweighted character biases are

\[
x(a)=(-1)^{|a|}\left(1-\frac{2|a|}{R}\right).
\tag{3}
\]

Now allow **any common complex coefficient vector**

\[
w=(w_r)_{r\in\mathcal A_y}\in\mathbf C^A,
\]

chosen using arbitrary source-natural information but used identically for every character in the family. Define the filtered character sums

\[
T_w(a):=\sum_{r\in\mathcal A_y}w_r\chi_a(r).
\tag{4}
\]

Then the exact endpoint evaluation matrix satisfies

\[
\boxed{
\sum_{a\in G}|T_w(a)|^2
=
2^R\sum_{s\in S}
\left|\sum_{\substack{r\in\mathcal A_y\\s(r)=s}}w_r\right|^2
\le
\frac{2^R A}{R}\sum_{r\in\mathcal A_y}|w_r|^2.
}
\tag{5}
\]

For `R>=2`, deleting the principal mode does not improve the operator norm:

\[
\boxed{
\sup_{w\ne0}
\frac{
\sum_{a\ne0}|T_w(a)|^2
}{
\sum_r|w_r|^2
}
=
\frac{2^R A}{R}.
}
\tag{6}
\]

The supremum is attained by coefficient vectors constant on each endpoint cell whose `R` cell constants sum to zero. By contrast, the original unweighted vector `w_r=1` has

\[
\frac{
\sum_{a\ne0}|T_1(a)|^2
}{
\sum_r|1|^2
}
=
A\left(\frac{2^R}{R}-1\right).
\tag{7}
\]

Hence optimizing over **all possible common prime weights** can improve the endpoint signal-to-coefficient-`L^2` ratio by at most

\[
\boxed{
\frac{2^R/R}{2^R/R-1}
=1+O\!\left(\frac{R}{2^R}\right).
}
\tag{8}
\]

This closes a natural escape left by `MC-330`. Schlage-Puchta's prime Halász–Montgomery inequality used in `MC-329` already permits arbitrary prime-supported coefficients and charges them only through `\sum_r|w_r|^2`. Therefore **no mode-independent linear prefilter that merely replaces the shell indicator by one common coefficient vector can push the fixed-common-modulus contradiction past exponent `4`**. The unweighted endpoint already saturates the relevant `L^2` operator norm up to the asymptotically negligible removal of the principal character.

Equivalently, any translation-invariant convolution/filter on the character cube also fails: under Walsh duality it is just multiplication of shell sign cells by a scalar, hence a special case of `(4)`. Hamming adjacency, cube Laplacians, noise operators, radial convolution kernels, and arbitrary Walsh multipliers are all contained in this no-go.

A genuine pre-compression escape must therefore use information that is **not representable by one common coefficient vector across all modes**—for example a mode-dependent or bilinear/joint prime-character statistic—or it must replace the present `L^2` prime-family theorem by an estimate that exploits additional structure of the coefficients instead of only their quadratic norm. No estimate for `M(x)` follows.

## 1. Exact endpoint orthogonality

For `s\in S`, put

\[
W_s:=\sum_{\substack{r\in\mathcal A_y\\s(r)=s}}w_r.
\tag{9}
\]

Grouping `(4)` by sign cell gives

\[
T_w(a)=\sum_{s\in S}W_s(-1)^{a\cdot s}.
\tag{10}
\]

Character orthogonality on `G` yields

\[
\sum_{a\in G}(-1)^{a\cdot(s+t)}
=
2^R\mathbf1_{s=t}.
\tag{11}
\]

Expanding the square in `(10)` and applying `(11)` proves the equality in `(5)`:

\[
\sum_{a\in G}|T_w(a)|^2
=2^R\sum_{s\in S}|W_s|^2.
\tag{12}
\]

Each endpoint cell has exactly `A/R` primes. Cauchy–Schwarz inside each cell gives

\[
|W_s|^2
\le
\frac AR
\sum_{\substack{r\in\mathcal A_y\\s(r)=s}}|w_r|^2.
\tag{13}
\]

Summing `(13)` proves the upper bound in `(5)`.

This already permits arbitrary variation of `w_r` inside a sign cell. A scalar Walsh multiplier is not being privileged: the exact matrix bound covers every common coefficient vector, including weights depending on prime size or on additional arithmetic data.

## 2. Removing the principal character leaves the same top singular value

The principal row is

\[
T_w(0)=\sum_s W_s.
\tag{14}
\]

Hence

\[
\sum_{a\ne0}|T_w(a)|^2
=
2^R\sum_s|W_s|^2-\left|\sum_sW_s\right|^2.
\tag{15}
\]

Choose any nonzero vector of cell constants `c_s` satisfying

\[
\sum_{s\in S}c_s=0,
\tag{16}
\]

and set `w_r=c_{s(r)}`. Then

\[
W_s=\frac ARc_s,
\qquad
\sum_r|w_r|^2=\frac AR\sum_s|c_s|^2.
\tag{17}
\]

The principal term in `(15)` vanishes, and the quotient in `(6)` is exactly `2^R A/R`. Together with `(5)`, this proves `(6)`.

For the unweighted vector, `W_s=A/R` for every `s`. Formula `(15)` gives

\[
\sum_{a\ne0}|T_1(a)|^2
=
2^R R\frac{A^2}{R^2}-A^2
=A^2\left(\frac{2^R}{R}-1\right),
\tag{18}
\]

which proves `(7)` and `(8)`.

Thus the only linear gain available by reweighting the shell is to remove the principal-direction loss `A^2`. At the live endpoint scale `2^R/R\to\infty`, that is a relative `o(1)` correction, not a new power of `y`.

## 3. Why Schlage-Puchta absorbs every common prefilter

`MC-329` audits Schlage-Puchta's Theorem 3 in exactly the form needed here: for one cubefree common modulus `q`, a family `\Xi` of distinct characters, and **arbitrary** prime-supported coefficients `a_p`, the character-family mean square is bounded by an analytic factor times

\[
\sum_p|a_p|^2.
\tag{19}
\]

Apply that theorem to the nonprincipal endpoint family

\[
\Xi=\{\chi_a:a\ne0\}
\tag{20}
\]

and set `a_r=w_r`. Under `q\le y^{4-\delta}`, the same parameter choice as in `MC-329` gives, after normalization by the shell size,

\[
\sum_{a\ne0}
\left|
\frac1A T_w(a)
\right|^2
\le
C_\delta
\left(
1+(2^R-1)y^{-c_\delta}\log y
\right)
\frac1A\sum_r|w_r|^2.
\tag{21}
\]

The endpoint itself can force at most

\[
\sum_{a\ne0}
\left|
\frac1A T_w(a)
\right|^2
\le
\frac{2^R}{R}
\frac1A\sum_r|w_r|^2
\tag{22}
\]

by `(6)`. The common coefficient norm cancels between the analytic upper bound and the endpoint signal. Optimizing `w` therefore cannot change the power balance in `MC-329`; it can only replace the unweighted factor `2^R/R-1` by at most `2^R/R`.

This is the key distinction from `MC-330`. There the no-go applied **after** the bias vector had already been compressed to its `L^2` energy. Here the arbitrary coefficient vector is inserted on the prime side **before** the character-family transform. The failure survives because the analytic theorem is itself coefficient-uniform and measures exactly the same quadratic resource that controls the endpoint matrix norm.

## 4. Character-cube convolutions are a strict special case

Let `C_c` be any translation-invariant operator on functions of `a\in G`,

\[
(C_cf)(a)=\sum_{h\in G}c(h)f(a+h).
\tag{23}
\]

Its Walsh multiplier is

\[
b(s)=\sum_{h\in G}c(h)(-1)^{h\cdot s}.
\tag{24}
\]

For a shell bias vector

\[
\beta(a)=\frac1A\sum_r\chi_a(r),
\]

one has exactly

\[
(C_c\beta)(a)
=
\frac1A\sum_r b(s(r))\chi_a(r).
\tag{25}
\]

Thus every such cube filter is equation `(4)` with the common coefficient choice

\[
w_r=b(s(r)).
\tag{26}
\]

The tempting Hamming-adjacency filter illustrates the cancellation. Its multiplier is `R-2|s|`. On the reciprocal endpoint cells `|s|=R-1`, this multiplier is the constant `2-R`, so the endpoint signal is amplified by `|R-2|`; the coefficient `L^2` bill in `(21)` is amplified by exactly the same factor squared. The normalized contradiction is unchanged.

No convolutional spectral filter on the mode cube can evade this, regardless of degree or localization, because Walsh inversion identifies the entire class with scalar shell-cell reweighting already covered by `(6)`.

## 5. Prior art and novelty boundary

No novelty is claimed for finite-group character orthogonality, Walsh diagonalization of convolution, singular-value/operator-norm language, Cauchy–Schwarz, or the large-sieve principle that arbitrary coefficients are charged in `L^2`. These are classical mechanisms; `MC-328` already audits standard Boolean-cube Fourier references, and `MC-329` audits the exact Schlage-Puchta prime Halász–Montgomery theorem used in `(21)`.

A targeted literature check on 16 September 2026 found the standard large-sieve formulation with arbitrary complex coefficients in Montgomery–Vaughan's classical large-sieve work and modern treatments, and standard Walsh/convolution machinery in Boolean Fourier analysis. No external theorem is needed for `(5)`–`(8)`, which are direct finite identities and inequalities.

No standalone novelty claim is made for the general operator statement. The durable Mathia delta is the **composition at the live reciprocal endpoint**: the exact one-defect sign-cell geometry makes the unweighted shell vector asymptotically extremal for every common-coefficient `L^2` prefilter, while the strongest available subquartic prime-family estimate is uniform in exactly those coefficients. This removes the most immediate interpretation of `MC-330`'s proposed "structured `BT` before compression" escape without pretending to close genuinely joint or mode-dependent source couplings.

## Boundaries and falsification tests

- **Exact equal endpoint cells are load-bearing.** Equation `(2)` is stronger than the unequal endpoint partition used in `MC-305`. With cell sizes `n_s`, the full-matrix norm becomes `2^R\max_s n_s`; a highly unequal endpoint could make coefficient selection materially different.
- **Common coefficients are load-bearing.** The same `w_r` must feed every character. Mode-dependent coefficients `w_{a,r}`, bilinear forms coupling two modes, or higher tensors are not covered.
- **The analytic input is `L^2`-uniform.** The no-go says that an estimate depending on coefficients only through `\sum|w_r|^2` cannot gain by optimizing those coefficients. A theorem exploiting arithmetic structure, sparsity, oscillation, or correlations of the chosen weights could behave differently.
- **No positivity assumption on `w`.** Complex signed weights are allowed, so the obstruction is stronger than a nonnegative reweighting statement.
- **No restriction to radial or low-degree filters.** Every mode-cube convolution is included, including high-degree and non-radial multipliers.
- **No circular zero information.** The proof uses only exact endpoint character geometry plus the same unconditional prime-family theorem already audited in `MC-329`.
- **No RH-scale conclusion.** This is a method-boundary theorem for one endpoint obstruction, not a cancellation theorem for Möbius.

## Consequence for the research line

`MC-330` left two broad ways to escape the quartic energy wall: move structured information before `L^2` compression, or use a genuinely higher-order invariant. The first option is now narrower. **Any pre-compression operation that ultimately supplies one common scalar coefficient vector to the existing character-family mean-square theorem is powerless at fixed-power scale.**

The next viable linear target must be mode-dependent or genuinely joint—for example an estimate for a matrix of coefficients `w_{a,r}` whose arithmetic structure couples character mode and shell prime before squaring. Otherwise the common coefficient vector is absorbed by Schlage-Puchta and the exact endpoint matrix norm returns the same quartic horizon.