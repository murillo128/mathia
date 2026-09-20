# MC-418 — Operator-valued positive finite-band kernels inherit the Fejér diagonal floor

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-417` closes every **scalar** positive finite-band translation-invariant quadratic shift kernel, but leaves matrix/operator-valued positivity as a possible higher-dimensional escape. Merely retaining finitely or infinitely many source channels inside a positive stationary kernel does **not** remove the same diagonal/DC obstruction.

Let `G` be a complex Hilbert space and let

\[
P(\theta)=\sum_{|h|<H}K_h e(h\theta),
\qquad K_{-h}=K_h^*,
\tag{1}
\]

be an `L(G)`-valued trigonometric polynomial satisfying

\[
P(\theta)\succeq0
\qquad\text{for every }\theta\in\mathbb R/\mathbb Z.
\tag{2}
\]

Write `K_0` for its zero Fourier coefficient and `P(0)=sum_h K_h` for its DC response. Then

\[
\boxed{
K_0\succeq \frac1H P(0).
}
\tag{3}
\]

Thus the scalar `1/H` floor from `MC-417` survives **in Loewner order**. There is no improvement by the number of retained channels, the rank of the kernel, or the dimension of `G`. In particular, if the target subspace is DC-normalized so that `P(0)=I`, then every positive operator-valued bandwidth-`H` kernel satisfies

\[
K_0\succeq \frac1H I.
\tag{4}
\]

The operator Fejér–Riesz theorem gives a polynomial spectral factor

\[
Q(z)=\sum_{j=0}^{H-1}B_j z^j,
\qquad
P(\theta)=Q(e(\theta))^*Q(e(\theta)).
\tag{5}
\]

Hence

\[
K_0=\sum_{j=0}^{H-1}B_j^*B_j,
\qquad
P(0)=\left(\sum_jB_j\right)^*\left(\sum_jB_j\right),
\tag{6}
\]

and the diagonal floor has the exact positive decomposition

\[
\boxed{
H K_0-P(0)
=
\sum_{0\le j<k<H}(B_j-B_k)^*(B_j-B_k)
\succeq0.
}
\tag{7}
\]

Equality in `(3)` as an operator identity holds exactly when all spectral-factor coefficients are equal,

\[
B_0=B_1=\cdots=B_{H-1},
\tag{8}
\]

in which case

\[
P(\theta)
=
\left|\sum_{j=0}^{H-1}e(j\theta)\right|^2 C,
\qquad C\succeq0.
\tag{9}
\]

So even the operator-valued extremizer is only a fixed positive channel operator multiplied by the ordinary scalar Fejér profile. Positive channel mixing does not buy a smaller normalized zero shift.

For a finitely supported vector sequence `a_n in G`, `a_n=0` outside `[1,N]`, put `S=sum_n a_n` and

\[
B_t^{(a)}:=\sum_{j=0}^{H-1}B_j a_{t+j}.
\tag{10}
\]

Then

\[
\sum_t B_t^{(a)}=Q(1)S
\tag{11}
\]

and at most `N+H-1` terms are nonzero, so

\[
\boxed{
\langle P(0)S,S\rangle
\le
(N+H-1)\sum_t\|B_t^{(a)}\|^2.
}
\tag{12}
\]

The zero-shift part of the energy on the right is

\[
D_0
=
\sum_n\langle K_0 a_n,a_n\rangle
\ge
\frac1H\sum_n\langle P(0)a_n,a_n\rangle.
\tag{13}
\]

Thus a stationary positive matrix/operator kernel that genuinely reconstructs a DC target cannot reduce its normalized diagonal by spreading that target over internal coordinates. Any higher-dimensional escape from `MC-417` must obtain value from structure **other than channel multiplicity itself**: source-specific off-diagonal cancellation, nonstationarity, an indefinite controlled form, more than one translation variable, or a pre-quadratic arithmetic operation that changes the state before positive closure.

No improved character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. The Loewner floor already follows by scalarization

For any fixed `v in G`,

\[
p_v(\theta):=\langle P(\theta)v,v\rangle
\tag{14}
\]

is a scalar nonnegative trigonometric polynomial of degree at most `H-1`. Its constant Fourier coefficient is `\langle K_0v,v\rangle`, while its value at zero is `\langle P(0)v,v\rangle`.

Applying the scalar extremal inequality from `MC-417` gives

\[
\langle K_0v,v\rangle
\ge
\frac1H\langle P(0)v,v\rangle
\qquad(v\in G).
\tag{15}
\]

Because `(15)` holds for every vector, it is exactly the operator inequality `(3)`. This proof is important for the research boundary: the obstruction does not depend on a choice of basis, a finite channel count, a rank estimate, or even on constructing a particular operator spectral factor.

If the actual degree is `m<H-1`, scalarization gives the sharper operator inequality

\[
K_0\succeq\frac1{m+1}P(0).
\tag{16}
\]

Padding a shorter operator kernel with zero coefficients therefore cannot manufacture a better ratio.

## 2. Operator Fejér–Riesz gives the exact defect

Rosenblum's one-variable operator Fejér–Riesz theorem states that every positive operator-valued Laurent polynomial admits a same-degree analytic spectral factor. Applying it to `(1)`–`(2)` gives `(5)`.

Taking the constant coefficient and evaluating at `z=1` gives `(6)`. Expanding

\[
\sum_{j<k}(B_j-B_k)^*(B_j-B_k)
\tag{17}
\]

shows directly that it equals

\[
H\sum_jB_j^*B_j
-
\left(\sum_jB_j\right)^*\left(\sum_jB_j\right),
\tag{18}
\]

which proves `(7)` without a dimension-dependent constant.

Equation `(7)` is the Hilbert-space version of the coefficient Cauchy–Schwarz step in `MC-416`–`MC-417`. It also identifies the equality case: the defect vanishes as an operator exactly when every `(B_j-B_k)^*(B_j-B_k)` vanishes, hence all `B_j` agree. Substituting into `(5)` yields `(9)`.

A weaker equality can of course occur only on a chosen target subspace: if `(3)` is saturated on vectors in `U subseteq G`, then `(B_j-B_k)v=0` for all `v in U`. Outside `U` the kernel may retain additional channel structure. This does not change the `1/H` floor on the reconstructed target directions.

## 3. Reconstruction preserves the same diagonal budget

The factorization also gives the vector-valued analogue of the reconstruction step in `MC-417`. From `(10)` and zero extension,

\[
\sum_tB_t^{(a)}
=\sum_jB_j\sum_ta_{t+j}
=Q(1)S,
\tag{19}
\]

so Hilbert-space Cauchy–Schwarz over the at most `N+H-1` nonzero windows yields `(12)`.

Expanding the positive energy `sum_t ||B_t^(a)||^2` produces the operator-valued shift kernel `K_h`; its `h=0` contribution is precisely `D_0`. Inserting `(3)` gives `(13)`.

If `P(0)=I` on the target channel space, `(12)` reconstructs `||S||^2` while `(13)` forces at least

\[
\frac1H\sum_n\|a_n\|^2
\tag{20}
\]

of raw zero-shift mass before any off-diagonal terms are estimated. More generally, for a rank-one target response `P(0)=u u^*`, the same statement becomes

\[
D_0\ge\frac1H\sum_n|\langle a_n,u\rangle|^2.
\tag{21}
\]

Therefore a matrix kernel cannot hide the target diagonal in orthogonal auxiliary channels: the floor follows the actual DC response in Loewner order.

## 4. Consequence for retained source coordinates

The open boundary after `MC-417` allowed the possibility that a genuinely higher-dimensional source state might survive until after positive quadratic closure. The present result separates two different ideas that should not be conflated.

Merely replace a scalar sequence by a source/channel vector and use a **one-variable, finite-band, translation-invariant positive operator kernel**: this is now closed as a diagonal-removal mechanism. The DC direction in every retained source subspace carries the same reciprocal-bandwidth zero-shift cost.

Use the extra coordinates to prove a new **off-diagonal theorem** before they collapse: this remains live. Matrix entries can encode cross-channel correlations that a scalar kernel cannot see, and `(3)` does not say those correlations are analytically useless. It says only that positive channel lifting cannot purchase them by diluting the diagonal.

Likewise, a genuinely multivariable arithmetic state is not covered merely because its values can be placed in a Hilbert space. If the kernel depends on additional translation variables, on the base point, on modulus factors that evolve under differencing, or enters through an indefinite identity before positive closure, the one-variable argument above no longer classifies the architecture.

## 5. Prior art and novelty boundary

The operator factorization used here is classical. Marvin Rosenblum proved the full one-variable operator Fejér–Riesz theorem in 1968; an accessible modern statement and proof is Michael A. Dritschel and James Rovnyak, *The Operator Fejér–Riesz Theorem*, in *A Glimpse at Hilbert Space Operators: Paul R. Halmos in Memoriam*, Operator Theory: Advances and Applications 207 (2010), 223–254, DOI `10.1007/978-3-0346-0347-8_14`, arXiv `0903.3639`. Their Theorem 2.1 states exactly that a positive operator-valued Laurent polynomial of degree `m` factors as `P(z)^*P(z)` with an operator polynomial of degree `m`.

The same one-variable operator theorem is recalled as the classical base case in Michael A. Dritschel, *Factoring non-negative operator valued trigonometric polynomials in two variables*, Mathematische Annalen (2024), DOI `10.1007/s00208-024-02895-9`. No novelty is claimed for operator Fejér–Riesz factorization, the Hilbert-space Cauchy identity `(7)`, or the scalarized Fejér inequality.

A targeted literature audit on 20 September 2026 found the matrix/operator spectral-factorization framework to be standard prior art. The durable Mathia result is the frontier classification obtained by combining that classical theorem with `MC-417`: **the matrix/operator-valued stationary positive enlargement does not evade the Fejér-optimal diagonal/DC floor either**. This removes channel dimension itself as the remaining higher-dimensional escape.

## Boundaries and falsification tests

- **One translation variable is load-bearing.** The theorem treats an operator-valued polynomial in one shift variable. A genuinely multivariable positive kernel has a different factorization problem and is not classified here.
- **Translation invariance is load-bearing.** A kernel depending on the base point `n`, divisor state, modulus factor, or differencing history need not have one operator-valued trigonometric symbol.
- **Positivity is load-bearing.** An indefinite matrix correlation form can cancel its diagonal, but then an independent arithmetic estimate must control its negative part.
- **Finite bandwidth fixes the constant.** Infinite-support kernels need their own convergence and normalization analysis. The finite theorem cannot be improved by truncating an infinite kernel without accounting for the tails.
- **The result controls the diagonal/DC tradeoff, not the off-diagonal.** Cross-channel arithmetic correlations may still yield a stronger estimate for the full energy. They do not reduce the forced zero-shift coefficient itself.
- **The DC response must encode the target.** If `P(0)` annihilates the desired global-sum direction, `(12)` does not reconstruct that target; a small diagonal obtained by deleting the response is not an escape.
- **No dimension factor is available.** Any proposed gain proportional to the number or rank of channels contradicts `(3)` unless some hypothesis above has genuinely been left.
- **No zeta information enters.** The argument uses only finite Fourier/operator algebra, one-variable operator Fejér–Riesz factorization, and Hilbert-space Cauchy–Schwarz.

## Consequence for the research line

`MC-417` left operator/matrix-valued positivity as one concrete architecture requiring separate analysis. `MC-418` supplies that analysis and closes the naive version: keeping source labels as vector coordinates through a stationary positive finite-band quadratic form does not lower the Fejér diagonal at all.

The live fork is therefore narrower. Either use the retained coordinates to prove enough **source-specific off-diagonal cancellation** to pay the unavoidable diagonal, or leave one-variable stationary positivity itself through a nonstationary/modulus-factorized process, an independently controlled indefinite form, or a genuinely multivariable pre-quadratic architecture. A future candidate whose only novelty is replacing the scalar Fejér kernel by a positive matrix/operator-valued one is already classified by `(3)` and should not be counted as a new escape.