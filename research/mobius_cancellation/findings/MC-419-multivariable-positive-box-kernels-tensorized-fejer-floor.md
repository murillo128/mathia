# MC-419 — Multivariable positive box kernels pay a tensorized Fejér floor

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-417` closes scalar one-variable positive finite-band kernels and `MC-418` shows that retaining arbitrarily many Hilbert-space channels under the same translation variable does not lower the normalized Fejér diagonal. The remaining phrase “genuinely multivariable” has a precise first boundary: independent translation variables can lower the forced diagonal, but only by the **volume of their independent bandwidth box**.

Let `G` be a complex Hilbert space, let `d>=1`, and let `H_1,...,H_d` be positive integers. Consider an operator-valued trigonometric polynomial on the `d`-torus

\[
P(\theta)
=
\sum_{\substack{h\in\mathbb Z^d\\ |h_j|<H_j\ \forall j}}
K_h e(h\cdot\theta),
\qquad
K_{-h}=K_h^*,
\tag{1}
\]

with

\[
P(\theta)\succeq0
\qquad(\theta\in\mathbb T^d).
\tag{2}
\]

Write

\[
K_0=\int_{\mathbb T^d}P(\theta)\,d\theta,
\qquad
V_H:=\prod_{j=1}^d H_j.
\tag{3}
\]

Then for every `xi in T^d`,

\[
\boxed{
P(\xi)\preceq V_H K_0.
}
\tag{4}
\]

Equivalently,

\[
\boxed{
K_0\succeq \frac{1}{V_H}P(\xi).
}
\tag{5}
\]

In particular, for the DC response,

\[
K_0\succeq
\frac{1}{\prod_jH_j}P(0).
\tag{6}
\]

The constant is sharp over the rectangular degree class. For any fixed positive operator `C`, the product Fejér symbol

\[
P(\theta)
=
C\prod_{j=1}^d
\left|\sum_{r=0}^{H_j-1}e(r\theta_j)\right|^2
\tag{7}
\]

satisfies

\[
P(0)=\left(\prod_jH_j^2\right)C,
\qquad
K_0=\left(\prod_jH_j\right)C,
\tag{8}
\]

so equality holds in `(6)`.

Thus a true `d`-variable positive stationary architecture can improve the one-variable `1/H` floor to reciprocal **bandwidth volume** `1/V_H`; it cannot obtain a further gain merely from channel count, matrix rank, or the nominal dimension of a state space. Extra dimensions matter here only when they are genuine independent translation axes carrying independent Fourier bandwidth.

For the Möbius line this is a classification, not an RH estimate. The original sequence `mu(n)` is one-dimensional. To exploit `(6)`, a candidate must first produce an intrinsic multivariable arithmetic lift with genuinely independent shifts and then prove that its DC response reconstructs the desired one-dimensional Möbius target. Merely storing divisor/source labels in a vector and applying one shift variable remains under `MC-418` and still pays the one-dimensional floor.

No bound for `M(x)`, no new character-sum estimate, and no RH consequence follows from `(4)`–`(6)` alone.

## 1. The point/mean bound tensorizes one coordinate at a time

Fix `v in G` and scalarize:

\[
p_v(\theta):=\langle P(\theta)v,v\rangle.
\tag{9}
\]

By `(2)`, `p_v` is a nonnegative scalar trigonometric polynomial. In coordinate `j` its degree is at most `H_j-1`.

For a nonnegative one-variable trigonometric polynomial `f` of degree at most `H-1`, the classical Fejér extremal inequality gives

\[
f(0)\le H\int_{\mathbb T}f(t)\,dt.
\tag{10}
\]

Apply `(10)` first to the `theta_1` variable with all remaining coordinates fixed at zero:

\[
p_v(0,\ldots,0)
\le
H_1\int_{\mathbb T}p_v(\theta_1,0,\ldots,0)\,d\theta_1.
\tag{11}
\]

The function

\[
q_2(\theta_2)
:=
\int_{\mathbb T}p_v(\theta_1,\theta_2,0,\ldots,0)\,d\theta_1
\tag{12}
\]

is again nonnegative and has degree at most `H_2-1`. Hence

\[
q_2(0)
\le
H_2\int_{\mathbb T}q_2(\theta_2)\,d\theta_2.
\tag{13}
\]

Continuing through all coordinates and using Fubini gives

\[
p_v(0)
\le
\left(\prod_{j=1}^dH_j\right)
\int_{\mathbb T^d}p_v(\theta)\,d\theta
=
V_H\langle K_0v,v\rangle.
\tag{14}
\]

Because `(14)` holds for every `v`, it is exactly the Loewner inequality

\[
P(0)\preceq V_HK_0.
\tag{15}
\]

For arbitrary `xi`, apply the same argument to the translated polynomial `theta -> P(theta+xi)`. Translation preserves positivity, coordinate degrees, and the zero Fourier coefficient, proving `(4)`.

The proof uses only the one-variable Fejér point/mean inequality, positivity, scalarization, and Fubini. It does **not** require a multivariable Fejér–Riesz factorization.

## 2. Multivariable factorization is not the hidden assumption

This distinction matters because one-variable and multivariable positivity have different factorization behavior. In one variable, the operator Fejér–Riesz theorem used in `MC-418` factors a positive operator-valued trigonometric polynomial as one Hermitian square of the same degree. In several variables, factorization is subtler: even strictly positive polynomials generally require finite sums of squares with degree control depending on the positivity margin, and the merely nonnegative case has additional difficulties.

Michael A. Dritschel, *Factoring non-negative operator valued trigonometric polynomials in two variables*, **Mathematische Annalen** 391 (2025), 515–537, DOI `10.1007/s00208-024-02895-9`, proves a two-variable finite-dimensional operator-valued sum-of-Hermitian-squares result and explicitly contrasts it with the classical one-variable theorem. The article was published online 27 June 2024. Its introduction and Theorems 1.1–1.2 make the one-variable/multivariable distinction explicit.

Equation `(4)` bypasses that factorization question completely. Scalar sections `p_v` remain nonnegative, and the coordinatewise Fejér inequality can be iterated directly. Consequently the diagonal floor holds for arbitrary Hilbert-space-valued coefficients under `(1)`–`(2)`, without a finite-dimensional assumption or a multivariable spectral factor.

This also marks a boundary on what can be imported from `MC-417`–`MC-418`: the **point/mean floor** tensorizes, but the one-variable “one filter reconstructs the target” representation does not automatically tensorize for a general multivariable positive symbol.

## 3. The sharp gain is bandwidth volume, not dimension

The extremizer `(7)` is the tensor product of the one-variable Fejér extremizers. Its normalized diagonal/DC ratio is exactly

\[
\frac{1}{V_H}
=
\prod_{j=1}^d\frac1{H_j}.
\tag{16}
\]

Therefore the full rectangular class genuinely differs from the one-variable class. If all `H_j=H`, the sharp floor becomes `H^{-d}` rather than `H^{-1}`.

But this gain has a precise cost: there are `V_H` independent analytic bandwidth cells in the product box. Merely declaring a larger vector state does nothing. If a new coordinate has `H_j=1`, it contributes no extra translation bandwidth and no improvement to `(16)`. Likewise, replacing a scalar coefficient by a high-rank matrix while retaining one translation variable is exactly the setting already closed by `MC-418`.

This separates two notions that were previously grouped together under “higher-dimensional retained state”:

- **internal channel dimension** under one stationary shift: no diagonal improvement (`MC-418`);
- **independent translation dimension** with rectangular Fourier support: an exact reciprocal-volume improvement, sharp by `(7)`.

The second is a genuine mathematical escape from the one-variable constant, but not a free one: an arithmetic application must justify every independent translation axis and its bandwidth.

## 4. Consequence for Möbius and source-frame architectures

A one-dimensional Möbius sum

\[
M(N)=\sum_{n\le N}\mu(n)
\tag{17}
\]

has only one canonical translation variable `n -> n+h`. A multivariable positive kernel becomes relevant only after an arithmetic transformation creates additional coordinates with their own independent translation actions—for example a factor/source variable, modulus coordinate, or genuinely multidimensional incidence state—and preserves enough information to recover `(17)`.

The theorem therefore imposes three separate obligations on any proposed multivariable escape:

1. exhibit an intrinsic `d`-variable arithmetic state rather than a reversible relabelling of one-dimensional samples;
2. prove that the relevant shifts act independently enough that the Fourier support is genuinely multivariable;
3. give a target-reconstruction argument and off-diagonal arithmetic estimates strong enough that the improved `1/V_H` diagonal budget survives the return to the one-dimensional Möbius sum.

Failure at the first two steps collapses the proposal back to `MC-418`. Failure at the third leaves a correct multivariable positivity theorem with no Mertens consequence.

The rectangular bound is also deliberately not a complete classification of support geometry. If the Fourier support is sparse, lower-dimensional, or constrained to a non-product set, `V_H` can overcount its effective degrees of freedom and a stronger support-sensitive extremal constant may exist. This enters the classical family of Turán/positive-definite support extremal problems rather than being a new Möbius phenomenon.

Kolountzakis and Révész, *On Pointwise Estimates of Positive Definite Functions With Given Support*, **Canadian Journal of Mathematics** 58 (2006), 401–418, arXiv `math/0302193`, studies multidimensional pointwise/support extremal problems for positive definite functions on groups including `R^d` and `T^d`. Lawton, *Spectral factorization of trigonometric polynomials and lattice geometry*, **Acta Arithmetica** 155 (2012), 145–160, develops the relation between multivariable trigonometric polynomial factorization and lattice geometry. These provide the appropriate prior-art boundary for any attempt to replace the rectangular degree count by a sharper arithmetic support invariant.

## Prior art and novelty boundary

No novelty is claimed for the one-variable Fejér inequality, tensor-product Fejér kernels, coordinatewise iteration of a one-variable inequality, multivariable positive-trigonometric-polynomial theory, or the cited support-extremal literature.

A targeted literature audit on 20 September 2026 found the relevant analytic ingredients to be classical and the multivariable factorization problem to have substantial existing theory. The durable Mathia result is the **frontier classification relative to `MC-417`–`MC-418`**: once channel dimension and independent translation dimension are separated, the latter has a sharp positive-kernel floor `1/prod H_j`, while the former provides no gain at all. This identifies exactly what a purported “higher-dimensional” Möbius escape must supply before it can change the one-dimensional diagonal budget.

## Boundaries and falsification tests

- **Rectangular coordinate-degree control is the theorem proved here.** The bound is valid for any support inside the box `|h_j|<H_j`, but it need not be optimal for a sparse or structured subset. A support-sensitive improvement requires a separate extremal theorem.
- **Independent translation variables are load-bearing for the interpretation.** A formal embedding of one shift index into several coordinates does not create new bandwidth volume if the data remain confined to a diagonal or other lower-rank orbit.
- **Positivity is load-bearing.** An indefinite multivariable form may cancel its diagonal, but its negative part then requires independent arithmetic control.
- **Stationarity is load-bearing.** Base-point-dependent kernels need not possess one torus symbol with fixed Fourier support.
- **Finite coordinate bandwidth is load-bearing.** Infinite-support kernels require convergence, tail, and normalization control before any limiting version of `(4)` can be used.
- **The theorem is only a point/mean diagonal bound.** It supplies neither a general same-degree multivariable spectral factor nor a reconstruction theorem for `M(N)`.
- **No off-diagonal estimate is obtained.** Even an exact `1/V_H` diagonal can be useless if the remaining correlations are not controlled at the matching scale.
- **No arithmetic axes are manufactured.** An application must prove that the additional coordinates exist intrinsically in the Möbius/source construction and are not just auxiliary labels.
- **No RH information enters.** The derivation uses only positivity and finite Fourier degree; any later RH-scale consequence must come from an independent arithmetic bridge.

## Consequence for the research line

`MC-418` left “genuinely multivariable” positivity as a possible escape without quantifying what it could buy. `MC-419` supplies that quantitative boundary. Positive stationary kernels on a rectangular `d`-torus can lower the forced DC diagonal exactly to reciprocal bandwidth volume, and no further through dimension alone.

The live question is therefore no longer whether adding dimensions abstractly helps. It is whether the Möbius/source-frame constructions expose **genuine independent arithmetic translation directions** whose bandwidth volume grows faster than the cost of reconstructing the one-dimensional target, while their off-diagonal correlations remain controllable. If not, the multivariable lift is only a repackaging of the one-variable obstruction; if so, that arithmetic lift—not positivity itself—is the new information that must be proved.