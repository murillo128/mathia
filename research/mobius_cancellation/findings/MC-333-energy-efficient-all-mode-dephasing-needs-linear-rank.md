# MC-333 — Energy-efficient all-mode dephasing needs linear rank

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-332` shows that the reciprocal endpoint's character oscillation can be erased exactly by a mode-dependent coefficient matrix of rank only `R`, despite there being `2^R-1` nonprincipal modes. Rank alone is therefore too weak a complexity measure. There is nevertheless a quantitative obstruction once exact dephasing is required to remain **Frobenius-energy efficient**.

Use the exact reciprocal sign-cell model of `MC-332`. Let

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\qquad
m:=|\Xi|=2^R-1,
\]

and assume the `A` shell-prime columns are distributed equally among the `R` one-defect sign cells, so `R\mid A`. Let

\[
B=(b_{a,r})_{a\in\Xi,\ r\in\mathcal A}\in\{\pm1\}^{m\times A}
\]

be the endpoint character-evaluation matrix from `MC-332`. For a coefficient matrix

\[
W=(w_{a,r})\in\mathbf C^{m\times A},
\]

call `W` an **exact dephaser for target amplitudes** `c=(c_a)_{a\in\Xi}` when

\[
\sum_{r\in\mathcal A} w_{a,r}b_{a,r}=A c_a
\qquad(a\in\Xi).
\tag{1}
\]

Let `1\le d\le R`, and suppose

\[
\operatorname{rank}W\le d.
\tag{2}
\]

Then for `d\le R-1`, every exact dephaser satisfies

\[
\boxed{
\|W\|_F^2
\ge
\frac{A R}{d\,2^R}\,\|c\|_1^2.
}
\tag{3}
\]

For the uniform all-mode target `c_a=1`, write `N_d` for the minimum Frobenius energy among rank-at-most-`d` exact dephasers. Then

\[
\boxed{
A m\,\frac{R}{d}(1-2^{-R})
\le
N_d
\le
A m\,\frac{R}{d}
\qquad(1\le d\le R-1),
}
\tag{4}
\]

while at full endpoint rank

\[
\boxed{N_R=A m.}
\tag{5}
\]

Thus the exact matched filter `W=B` is energy-optimal at rank `R`, and reducing the shared row-space dimension to `d` incurs, up to the factor `1-2^{-R}`, an unavoidable Frobenius-energy overhead `R/d`.

Equivalently, **any exact all-mode dephaser whose coefficient energy stays within a fixed constant factor of the unconstrained matched-filter energy must have `d=\Omega(R)`**. Low rank relative to the exponential mode population remains possible, but low rank relative to the number of independent endpoint sign cells is not compatible with constant-factor energy efficiency.

More generally, since `\|W\|_F^2` is compared naturally with the rowwise matched-filter baseline `A\|c\|_2^2`, `(3)` gives

\[
\boxed{
\frac{\|W\|_F^2}{A\|c\|_2^2}
\ge
\frac{R}{d}\,
\frac{\|c\|_1^2}{2^R\|c\|_2^2}
}
\tag{6}
\]

whenever `c\ne0`. Hence the same linear-rank requirement holds for target families whose amplitudes are sufficiently spread that

\[
\frac{\|c\|_1^2}{2^R\|c\|_2^2}\ge\kappa>0.
\tag{7}
\]

No estimate for `M(x)` follows. This is a finite endpoint complexity theorem that sharpens the admission test from `MC-332`.

## 1. Rank `d` means one common `d`-dimensional row space

Let `U\subset\mathbf C^A` be the row space of `W`; then

\[
\dim U\le d.
\]

For each mode `a`, write `b_a\in\{\pm1\}^A` for the corresponding row of `B`, and let `P_U` be orthogonal projection onto `U`. Because `w_a\in U`, condition `(1)` is

\[
\langle w_a,b_a\rangle=A c_a,
\tag{8}
\]

where the endpoint vectors are real and the Hermitian-inner-product convention is immaterial to the sign values.

Only the projected character vector can contribute:

\[
\langle w_a,b_a\rangle
=
\langle w_a,P_U b_a\rangle.
\]

Therefore Cauchy--Schwarz gives

\[
\|w_a\|_2^2
\ge
\frac{A^2|c_a|^2}{\|P_Ub_a\|_2^2},
\tag{9}
\]

with the right-hand side interpreted as `+\infty` if `P_Ub_a=0` and `c_a\ne0`. Equality is attained, for a fixed admissible `U`, by the projection-matched row

\[
w_a=
\frac{A c_a}{\|P_Ub_a\|_2^2}\,P_Ub_a
\tag{10}
\]

(up to the harmless conjugation dictated by the chosen inner-product convention).

Set

\[
x_a:=\|P_Ub_a\|_2^2.
\]

Summing `(9)` gives

\[
\|W\|_F^2
\ge
A^2\sum_a\frac{|c_a|^2}{x_a}.
\tag{11}
\]

Weighted Cauchy--Schwarz yields

\[
\left(\sum_a|c_a|\right)^2
\le
\left(\sum_a\frac{|c_a|^2}{x_a}\right)
\left(\sum_a x_a\right),
\tag{12}
\]

so

\[
\|W\|_F^2
\ge
A^2\frac{\|c\|_1^2}{\sum_a x_a}.
\tag{13}
\]

The problem has reduced to bounding how much total character energy a `d`-dimensional common row space can capture.

## 2. The endpoint spectrum fixes the maximum captured energy

The projection energies satisfy

\[
\sum_a x_a
=
\operatorname{tr}(P_U B^*B).
\tag{14}
\]

`MC-332` computed the sign-cell Gram matrix. If `V` is the `(2^R-1)\times R` matrix with one column per sign cell, then

\[
V^*V=2^R I_R-\mathbf1\mathbf1^*,
\tag{15}
\]

whose eigenvalues are

\[
2^R\quad(R-1\text{ times}),
\qquad
2^R-R\quad(1\text{ time}).
\tag{16}
\]

Repeating every sign-cell column `A/R` times multiplies the nonzero eigenvalues of `B^*B` by `A/R`. Hence

\[
\lambda(B^*B)=
\begin{cases}
(A/R)2^R,& R-1\text{ times},\\
(A/R)(2^R-R),&1\text{ time},\\
0,&A-R\text{ times}.
\end{cases}
\tag{17}
\]

For `d\le R-1`, Ky Fan's maximum principle for a positive-semidefinite matrix gives

\[
\operatorname{tr}(P_U B^*B)
\le
\sum_{j=1}^{d}\lambda_j(B^*B)
=
\frac{A}{R}d\,2^R.
\tag{18}
\]

Combining `(13)` and `(18)` proves `(3)`.

This is the precise point at which endpoint sign-cell dimension, rather than the exponentially larger number of modes, enters the cost. A rank-`d` coefficient matrix supplies only a `d`-dimensional common source subspace, and the character frame can deposit at most the sum of the top `d` Gram eigenvalues into that subspace.

## 3. Uniform dephasing is pinned to an `R/d` energy window

For `c_a=1`, equation `(3)` becomes

\[
\|W\|_F^2
\ge
\frac{A R}{d2^R}(2^R-1)^2
=
A m\frac{R}{d}(1-2^{-R}),
\tag{19}
\]

which is the lower bound in `(4)`.

For the upper bound, choose any `d` of the `R` endpoint sign cells and let `U` be the span of their column-indicator vectors in `\mathbf C^A`. Every character row has modulus one on every selected cell, so

\[
\|P_Ub_a\|_2^2=\frac{A d}{R}
\qquad\text{for every }a.
\tag{20}
\]

Using the projection-matched choice `(10)` therefore gives exact dephasing with

\[
\|w_a\|_2^2
=
\frac{A^2}{Ad/R}
=
\frac{A R}{d}
\tag{21}
\]

for every one of the `m` modes. All rows lie in `U`, hence `\operatorname{rank}W\le d`, and

\[
\|W\|_F^2=A m\frac{R}{d}.
\tag{22}
\]

This proves the upper bound in `(4)`. The two bounds differ only by the finite endpoint factor `1-2^{-R}`.

At `d=R`, the matched filter `W=B` from `MC-332` has

\[
\|B\|_F^2=A m.
\tag{23}
\]

Conversely, rowwise Cauchy--Schwarz applied to `(1)` with `c_a=1` and `\|b_a\|_2^2=A` gives `\|w_a\|_2^2\ge A` for every mode, hence `\|W\|_F^2\ge Am`. This proves `(5)` exactly.

## 4. What the bound changes after MC-332

`MC-332` killed two overly broad proposals: unrestricted mode dependence and a bare rank cap of order `R`. It deliberately left open what additional restriction might make a joint mode-prime coefficient class nontrivial.

The present calculation identifies one quantitative resource hidden by bare rank. Exact phase matching at rank `d<R` is still possible, but it cannot simultaneously retain the matched filter's coefficient-energy scale: its minimum cost is confined to the narrow interval `(4)`. Thus a future family theorem that both

1. restricts coefficient matrices to a common row-space dimension `d=o(R)`, and
2. charges them on the natural Frobenius `L^2` scale without permitting an `R/d` norm inflation,

would genuinely exclude energy-efficient all-mode phase erasure in this endpoint model.

This does **not** establish that such a coefficient class is arithmetically natural, nor that a Frobenius-energy budget supplies any new Möbius estimate. It only turns the vague phrase "low-complexity mode dependence" into a falsifiable two-parameter requirement: shared row-space dimension and coefficient energy must be controlled together.

The remaining frontier is still the one stated by `MC-332`: find a source-natural restriction whose analytic meaning is independent of the endpoint calibration and whose family estimate gains more than the common-weight theorem. The new obstruction says that any candidate admitting constant-energy exact dephasing must carry at least linear rank in the sign-cell dimension.

## 5. Prior art and novelty boundary

The proof uses only classical finite-dimensional Hilbert-space and matrix mechanisms: minimum-norm interpolation by orthogonal projection, Cauchy--Schwarz, the Frobenius/Hilbert--Schmidt norm, and Ky Fan's maximum principle for sums of leading eigenvalues. Ky Fan's original source is K. Fan, *Maximum properties and inequalities for the eigenvalues of completely continuous operators*, Proceedings of the National Academy of Sciences **37** (1951), 760--766, DOI `10.1073/pnas.37.11.760`.

A targeted literature audit on 16 September 2026 also found the broad modern literature on rank-constrained Frobenius approximation, but no external theorem is needed beyond these standard ingredients. For example, S. Friedland and A. Torokhti, *Generalized Rank-Constrained Matrix Approximations*, SIAM Journal on Matrix Analysis and Applications **29** (2007), 656--659, DOI `10.1137/06065551`, treats explicit Frobenius-optimal rank-constrained approximation problems in a much more general matrix setting. The present statement is not claimed as a new matrix-analysis theorem.

The durable Mathia delta is the specialization of those classical mechanisms to the exact reciprocal character frame already derived in `MC-332`, yielding the near-sharp endpoint tradeoff `(4)`. It is stored as a research-line obstruction because it changes the admissibility test for the next mode-dependent coefficient class; **no novelty claim is made for the underlying linear algebra**.

## Boundaries and falsification tests

- **Finite calibration only.** Equations `(3)`--`(6)` concern the exact reciprocal sign-cell endpoint from `MC-332`; they are not a theorem about Möbius cancellation or arbitrary character families.
- **Equal cell multiplicity is used.** The displayed constants assume exactly `A/R` repeated prime columns per one-defect sign cell. Unequal populations require the weighted Gram spectrum instead.
- **`R\ge2`.** The nonprincipal endpoint family and the split between the top `R-1` eigenvalues and the constant direction are used in the stated form.
- **Exact dephasing is load-bearing.** Approximate target matching leads to a different optimization problem and may admit a different rank-energy tradeoff.
- **The lower bound for `d<R` is not claimed optimal.** The explicit construction and lower bound differ by the factor `1-2^{-R}`. Only `N_R=Am` is exact here.
- **Frobenius energy is a chosen analytic cost, not an arithmetic theorem.** The result says what happens if a future estimate charges the coefficient matrix on that natural quadratic scale; it does not prove that every source-natural coefficient class should be measured this way.
- **Sparse target families can evade the linear-rank corollary.** Equation `(6)` retains the amplitude-spread factor. The `d=\Omega(R)` conclusion requires a lower bound such as `(7)`.
- **Low rank still permits exact phase erasure.** The result does not reverse `MC-332`: even rank one can dephase all modes with a suitable row space, but the explicit uniform construction pays order `R` more Frobenius energy than the full-rank matched filter.
- **No zero information is imported.** The argument uses only the finite character-evaluation matrix and its exact Gram spectrum.
- **No RH-scale conclusion is claimed.** This is an endpoint complexity obstruction and a design constraint for future joint coefficient classes.

## Consequence for the research line

Bare mode-dependent rank is not the right next invariant, but **rank together with quadratic coefficient cost is nontrivial**. At the reciprocal endpoint, constant-factor-energy exact dephasing of a spread all-mode target requires row-space dimension proportional to the number of independent sign cells, even though that is still logarithmic in the number of modes.

Any next proposed joint coefficient architecture should therefore be tested on three separate questions before analytic work begins: whether it excludes direct conjugate-character matching, what row-space dimension it effectively exposes, and what Frobenius (or comparably justified) coefficient cost is required to reproduce endpoint dephasing. A class that looks low-rank but hides an `R/d` norm inflation is analytically different from the unrestricted matched filter; a class that allows both rank `\Theta(R)` and baseline energy still retains the MC-332 obstruction.