# MC-334 — Exact dephasing requires matched-filter-scale mode variation

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-331` shows that one common prime coefficient vector cannot cross the reciprocal endpoint's quartic horizon. `MC-332` then shows that unrestricted mode-dependent rows can erase every character phase, while `MC-333` prices that escape by shared row-space rank and total Frobenius energy. There is a complementary exact resource that does not appear in the rank calculation: **how far the coefficient rows must move away from one common input**.

Use the exact endpoint notation of `MC-332`--`MC-333`. Let

\[
G=\mathbf F_2^R,\qquad
\Xi=G\setminus\{0\},\qquad
m=2^R-1,
\]

and let

\[
B=(b_{a,r})_{a\in\Xi,\ r\in\mathcal A}\in\{\pm1\}^{m\times A}
\]

be the endpoint character-evaluation matrix, with the `A` shell-prime columns equally distributed among the `R` one-defect sign cells. For a coefficient matrix `W=(w_{a,r})`, write `w_a\in\mathbf C^A` for its row and define the **cross-mode variation energy**

\[
\mathcal V(W)
:=\min_{u\in\mathbf C^A}\sum_{a\in\Xi}\|w_a-u\|_2^2
=\sum_{a\in\Xi}\|w_a-\bar w\|_2^2,
\qquad
\bar w=\frac1m\sum_a w_a.
\tag{1}
\]

For target amplitudes `c=(c_a)_{a\in\Xi}`, call `W` an exact dephaser when

\[
\sum_{r\in\mathcal A}w_{a,r}b_{a,r}=A c_a
\qquad(a\in\Xi).
\tag{2}
\]

Then the minimum possible mode-variation energy is exactly

\[
\boxed{
\inf_{W\text{ satisfying }(2)}\mathcal V(W)
=A\,\operatorname{dist}\!\left(c,\operatorname{col}B\right)^2.
}
\tag{3}
\]

Thus the obstruction to an almost-common mode-dependent filter is not rank but the component of the desired amplitude profile orthogonal to everything a common coefficient vector can already produce.

For the uniform all-mode target `c=\mathbf1`, the endpoint Gram matrix from `MC-332` gives

\[
\boxed{
\operatorname{dist}(\mathbf1,\operatorname{col}B)^2
=m-\frac{R}{2^R-R},
}
\tag{4}
\]

and hence

\[
\boxed{
\inf_{W:\,T_W(a)=A\ \forall a}\mathcal V(W)
=A\left(2^R-1-\frac{R}{2^R-R}\right).
}
\tag{5}
\]

This is essentially the full unconstrained matched-filter scale `Am`. Indeed the direct matched filter `W=B` has

\[
\boxed{
\mathcal V(B)=A\left(m-\frac1m\right),
}
\tag{6}
\]

so

\[
\frac{\mathcal V(B)}{\inf\mathcal V}
=1+O\!\left(\frac{R}{4^R}\right).
\tag{7}
\]

The conclusion is stronger than merely saying that the rows cannot all be equal. **Any exact all-mode dephaser must spend matched-filter-order quadratic energy specifically in cross-mode variation.** A large common component cannot hide the phase-matching cost.

The statement is robust to approximate dephasing. If

\[
\frac1A T_W=c+e,
\tag{8}
\]

then

\[
\boxed{
\mathcal V(W)
\ge
A\,\operatorname{dist}(c+e,\operatorname{col}B)^2
\ge
A\left(\operatorname{dist}(c,\operatorname{col}B)-\|e\|_2\right)_+^2.
}
\tag{9}
\]

For `c=\mathbf1`, if `\mathcal V(W)\le\theta Am`, then the normalized RMS dephasing error obeys

\[
\boxed{
\frac{\|e\|_2}{\sqrt m}
\ge
\sqrt{1-\frac{R}{m(2^R-R)}}-\sqrt\theta.
}
\tag{10}
\]

Consequently a coefficient architecture with `\mathcal V(W)=o(Am)` cannot even approximately erase a positive fraction of the all-mode character oscillation in RMS; conversely, RMS error `o(1)` forces `\mathcal V(W)=(1-o(1))Am` at this endpoint.

No estimate for `M(x)` follows. This is a finite endpoint admission theorem for the structured joint-coefficient route left open by `MC-333`.

## 1. Exact reduction to distance from the common-input image

For fixed `u\in\mathbf C^A`, write

\[
w_a=u+v_a.
\]

The dephasing condition `(2)` becomes

\[
\langle v_a,b_a\rangle
=A c_a-(Bu)_a,
\tag{11}
\]

where the `b_a` are real sign vectors, so the harmless convention for the complex inner product does not affect any norm formula. Since

\[
\|b_a\|_2^2=A,
\]

the minimum squared norm of a row correction satisfying `(11)` is exactly

\[
\min_{v_a:\,(11)}\|v_a\|_2^2
=
\frac{|A c_a-(Bu)_a|^2}{A},
\tag{12}
\]

attained by the projection of the required scalar constraint onto the line spanned by `b_a`.

Now use the elementary variance identity

\[
\mathcal V(W)=\min_u\sum_a\|w_a-u\|_2^2.
\tag{13}
\]

Minimizing jointly over the exact-dephasing rows and the common center gives

\[
\begin{aligned}
\inf_W\mathcal V(W)
&=\min_u\sum_a\frac{|A c_a-(Bu)_a|^2}{A}\\
&=\frac1A\operatorname{dist}(A c,\operatorname{col}B)^2\\
&=A\operatorname{dist}(c,\operatorname{col}B)^2,
\end{aligned}
\tag{14}
\]

which proves `(3)`. This is an equality, not only a lower bound.

Equation `(14)` supplies the exact dictionary between the previous two extremes. `MC-331` studies `\mathcal V(W)=0`, where every row is one common coefficient vector. `MC-332` permits arbitrary `\mathcal V(W)`. The new quantity measures continuously how much genuinely mode-dependent coefficient information is required before exact phase erasure becomes possible.

## 2. The constant target is almost orthogonal to the common-weight image

Repeated shell primes do not change `\operatorname{col}B`, so collapse the `A` columns to the `R` one-defect sign cells and use the matrix

\[
V_{a,s}=(-1)^{a\cdot s},
\qquad
a\in G\setminus\{0\},\ s\in S.
\tag{15}
\]

`MC-332` computed

\[
V^*V=2^R I_R-\mathbf1\mathbf1^*.
\tag{16}
\]

For every nonzero Walsh column, summing over all `a\in G` gives zero; deleting the principal row therefore gives

\[
V^*\mathbf1=-\mathbf1_R.
\tag{17}
\]

On the constant direction, the Gram matrix `(16)` has eigenvalue `2^R-R`. Hence the squared norm of the orthogonal projection of `\mathbf1\in\mathbf C^m` onto `\operatorname{col}V=\operatorname{col}B` is

\[
\|P_{\operatorname{col}B}\mathbf1\|_2^2
=(V^*\mathbf1)^*(V^*V)^{-1}(V^*\mathbf1)
=\frac{R}{2^R-R}.
\tag{18}
\]

Since `\|\mathbf1\|_2^2=m`, Pythagoras gives `(4)` and therefore `(5)`.

The least-squares common center can be chosen constant on every shell prime. In the normalization above it is

\[
u_r=-\frac{R}{2^R-R}.
\tag{19}
\]

The exact minimizing rows are then obtained by adding to this tiny common center the minimum-norm rowwise correction from `(12)`. The optimizer therefore makes the geometry transparent: the common part explains only the exponentially small projection `(18)`; almost the entire constant target has to be supplied by mode-varying corrections.

## 3. The direct matched filter is already variation-optimal up to an exponentially tiny relative gap

For `W=B`, every column corresponds to one nonzero Walsh character restricted to `\Xi`. Its mean over the `m` nonprincipal modes is `-1/m`. Therefore the mean row vector of `B` is the constant vector

\[
\bar b=-\frac1m\mathbf1_A.
\tag{20}
\]

Using `\|B\|_F^2=Am` gives

\[
\mathcal V(B)
=\|B-\mathbf1_m\bar b^*\|_F^2
=Am-m\|\bar b\|_2^2
=A\left(m-\frac1m\right),
\tag{21}
\]

which proves `(6)`.

Subtracting `(5)` from `(6)` gives

\[
A\left(\frac{R}{2^R-R}-\frac1m\right)
=
A\frac{(R-1)2^R}{(2^R-R)(2^R-1)}.
\tag{22}
\]

Relative to the lower bound `(5)`, this is `O(R/4^R)`, proving `(7)`. Thus replacing the raw conjugate-character matched filter by the optimally centered exact dephaser saves only an exponentially tiny fraction of its cross-mode variation energy.

## 4. Approximate dephasing cannot hide in an almost-common family

If `(8)` holds, repeat the fixed-center argument with target `c+e`. Equation `(14)` yields

\[
\mathcal V(W)\ge A\operatorname{dist}(c+e,\operatorname{col}B)^2.
\tag{23}
\]

Distance to a closed subspace is `1`-Lipschitz, so

\[
\operatorname{dist}(c+e,\operatorname{col}B)
\ge
\operatorname{dist}(c,\operatorname{col}B)-\|e\|_2,
\tag{24}
\]

which proves `(9)`.

For `c=\mathbf1`, divide `(9)` by `Am`, use `(4)`, and rearrange to obtain `(10)`. In particular, a source-natural class whose mode-dependent rows remain close in quadratic mean to one common prime vector cannot approximate the unrestricted matched filter merely by increasing rank or by hiding a small exceptional set of row perturbations inside a large common component. To make the RMS output error small, the rows must separate from their common center at essentially the same aggregate scale as the direct character-evaluation matrix itself.

This does not say that every analytically natural joint coefficient class has small `\mathcal V`. It supplies a cheap finite calibration: if a proposed class is advertised as a mild mode-dependent perturbation of the common-input architecture from `MC-331`, its admissible variation budget can be tested against `(5)`--`(10)` before attempting a new prime-family estimate.

## 5. Prior art and novelty boundary

No novelty is claimed for least squares, orthogonal projection, the Moore--Penrose pseudoinverse, minimum-norm interpolation under one linear constraint, the variance identity `(13)`, or Walsh/Hadamard character orthogonality. These are classical mechanisms. Roger Penrose's *A generalized inverse for matrices* (Proc. Cambridge Philos. Soc. **51** (1955), 406--413, DOI `10.1017/S0305004100030401`) gives the generalized-inverse/projector framework, and *On best approximate solutions of linear matrix equations* (Proc. Cambridge Philos. Soc. **52** (1956), 17--19, DOI `10.1017/S0305004100030929`) explicitly treats best least-squares solutions. Modern minimum-norm interpolation and frame/RKHS literature contains much broader versions of the same projection principle.

A targeted literature audit on 16 September 2026 found no reason to present `(3)` as a new matrix-analysis theorem; it is an elementary specialization of these standard Hilbert-space ideas. The durable Mathia delta is instead the **exact specialization to the reciprocal endpoint character frame**: the all-mode target lies almost completely outside the image of every common coefficient vector, so exact or small-RMS dephasing necessarily carries matched-filter-scale cross-mode variation. This is stored because it changes the admission test for the live source-natural joint-coefficient route, not because the underlying linear algebra is novel.

## Boundaries and falsification tests

- **The exact identity `(3)` is general for this rowwise interpolation architecture.** The endpoint geometry enters only when evaluating the distance in `(4)`.
- **Equal one-defect endpoint cells are used to inherit the exact `MC-332` Gram matrix.** Unequal cell populations change the explicit projection geometry.
- **Cross-mode variation is a new accounting choice, not an arithmetic theorem.** A future source-natural class need not have small `\mathcal V`; the result only says what such a restriction would buy.
- **The theorem does not replace `MC-333`.** Rank/total Frobenius energy and centered mode-variation energy are independent resources. A matrix can have rank `\Theta(R)` and baseline total energy yet still be ruled in or out by a separate variation constraint.
- **Approximation is measured in family `L^2`.** Sparse exceptional modes or a supremum-norm objective require separate analysis; `(9)` keeps the exact `L^2` error dependence rather than silently upgrading it.
- **The common center is arbitrary.** It may use any prime-side arithmetic information allowed by `MC-331`; `(1)` optimizes over all `u\in\mathbf C^A`.
- **No analytic character-sum theorem is invoked.** The result is a finite endpoint calibration and does not itself improve the quartic modulus horizon.
- **No zero information or RH-scale estimate is imported.** The proof uses only the endpoint evaluation matrix already established in `MC-332` and elementary Hilbert-space projection.

## Consequence for the research line

The live joint-coefficient escape now has a third independent admission currency alongside the two from `MC-333`: not only shared row-space dimension and total coefficient energy, but also **cross-mode variation away from the best common prime vector**. A source-natural family described as a controlled perturbation of common weights must pay almost the full matched-filter variation scale to erase the endpoint oscillation, even approximately in family RMS.

The next useful analytic target is therefore narrower than “structured mode dependence.” It should specify a coefficient class whose mode variation is controlled for an arithmetic reason, or else identify another coupling norm that excludes conjugate-character matching without collapsing back to the common-weight `L^2` theorem. Any such norm can now be calibrated against `(3)`--`(10)` before expensive prime-sum analysis begins.