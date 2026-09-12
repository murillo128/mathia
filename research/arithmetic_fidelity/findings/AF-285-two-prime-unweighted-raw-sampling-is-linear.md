# AF-285 — Two-prime unweighted raw sampling is linear

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `FINITE-BREADTH`, `STABILITY`, `SUBSET-SELECTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-284 reduced the complete two-prime mixed square from `Theta(N^2)` raw observations to an unweighted subset of `O(N log N)` observations, leaving open whether the logarithmic factor is intrinsic to unweighted acquisition or merely an artifact of independent random row sampling.

It is an artifact. In the same known-prefix model and with the same mixed cutoff `L=30N`, there exists an **unweighted subset of at most `8N` distinct raw complex mixed moments** whose least-squares inverse remains uniformly stable under adversarial absolute error on each retained sample.

More precisely, with AF-283's observation matrix

\[
A=V_{N,L}^{T}\in\mathbb C^{M\times N},
\qquad
L=30N,
\qquad
M=L^2=900N^2,
\]

there is a subset

\[
\Omega_N\subset\{0,\ldots,L-1\}^2,
\qquad
|\Omega_N|\le 8N,
\]

such that `A_{Omega_N}` has full column rank. If the retained complex observations are perturbed by arbitrary errors satisfying

\[
|\eta_\nu|\le\epsilon
\qquad(\nu\in\Omega_N),
\]

then least-squares reconstruction satisfies

\[
\boxed{
\|\widehat b-b\|_2
<
\frac{64\sqrt2}{27}\,\epsilon
<3.36\,\epsilon.
}
\]

Since any linear recovery of an arbitrary vector in `C^N` requires at least `N` complex scalar observations by rank, the unweighted raw sample complexity in this finite-prefix two-prime channel is therefore sharp in order:

\[
\boxed{|\Omega_N|=\Theta(N).}
\]

The general matrix theorem used here is classical. The Mathia-specific step is to realify the complex arithmetic frame, apply deterministic column subset selection to individual real measurement components, and then close every selected component under its underlying complex raw sample. This preserves the exact unweighted acquisition semantics of AF-284.

## Classical subset-selection input

Avron and Boutsidis prove a deterministic subset-selection theorem for a full-row-rank real matrix

\[
X\in\mathbb R^{n\times m},
\qquad m>n,
\]

and an oversampling parameter `k>n`. Their Theorem 3.4 gives a subset `S` of at most `k` columns such that

\[
\boxed{
\|X_S^\dagger\|_2^2
\le
\left(1+\sqrt{\frac{m}{k}}\right)^2
\left(1-\sqrt{\frac{n}{k}}\right)^{-2}
\|X^\dagger\|_2^2.
}
\]

The proof uses dual-set spectral sparsification internally, but the final output `X_S` is the ordinary **unweighted column submatrix** indexed by `S`; the sparsification weights are not retained in the selected matrix.

Primary source:

Haim Avron and Christos Boutsidis, **“Faster Subset Selection for Matrices and Applications,”** *SIAM Journal on Matrix Analysis and Applications* 34(4), 1464–1499 (2013), DOI `10.1137/120867287`, arXiv:`1201.0127`. Theorem 3.4 is the spectral/Frobenius pseudoinverse subset bound used here.

No new subset-selection or sparsification theorem is claimed.

## Realifying the AF-283 frame

AF-283 proves for the full mixed square at `L=30N` that

\[
\boxed{
\sigma_{\min}(A)>0.9L=27N.
}
\]

Use the standard realification

\[
\mathcal A=
\begin{pmatrix}
\Re A&-\Im A\\
\Im A&\Re A
\end{pmatrix}
\in\mathbb R^{2M\times2N}.
\]

The singular values of `mathcal A` are exactly the singular values of `A`, each with doubled multiplicity. Hence

\[
\sigma_{\min}(\mathcal A)
=
\sigma_{\min}(A)
>27N.
\]

Transpose it:

\[
X=\mathcal A^T
\in\mathbb R^{2N\times2M}.
\]

Then `X` has full row rank and

\[
\|X^\dagger\|_2^2
=
\frac{1}{\sigma_{\min}(\mathcal A)^2}
<
\frac{1}{729N^2}.
\]

For the Avron--Boutsidis theorem the dimensions are therefore

\[
n=2N,
\qquad
m=2M=1800N^2.
\]

## Selecting only linearly many real measurement rows

Choose

\[
k=8N.
\]

Then

\[
\sqrt{\frac{m}{k}}
=
\sqrt{\frac{1800N^2}{8N}}
=15\sqrt N,
\qquad
\sqrt{\frac{n}{k}}
=
\frac12.
\]

The subset-selection theorem gives a set `S` of at most `8N` columns of `X`, equivalently at most `8N` rows of `mathcal A`. Let `B` be the corresponding selected-row matrix. Since `X_S=B^T`,

\[
\|B^\dagger\|_2^2
<
\frac{4(1+15\sqrt N)^2}{729N^2}.
\]

Thus `B` has full column rank and

\[
\boxed{
\sigma_{\min}(B)
>
\frac{27N}{2(1+15\sqrt N)}.
}
\]

This already removes the logarithm at the level of scalar real measurement components. One more step is needed because the physical/raw channel in AF-284 records complete complex moments rather than independently addressable real and imaginary components.

## Closing selected components under raw complex samples

Every row of `mathcal A` is one of the two real scalar components associated with an original complex observation row of `A`. For every selected real row in `S`, retain the underlying complex mixed moment and therefore both of its realified component rows. Let `Omega_N` be the set of underlying mixed indices.

Several selected real rows can belong to the same complex sample, so

\[
\boxed{|\Omega_N|\le |S|\le8N.}
\]

The full realification `mathcal A_{Omega_N}` contains every row of `B` and possibly additional companion rows. Consequently

\[
\mathcal A_{\Omega_N}^T\mathcal A_{\Omega_N}
\succeq
B^TB,
\]

and therefore

\[
\sigma_{\min}(\mathcal A_{\Omega_N})
\ge
\sigma_{\min}(B).
\]

Realification preserves the singular values of the corresponding complex matrix, so

\[
\boxed{
\sigma_{\min}(A_{\Omega_N})
>
\frac{27N}{2(1+15\sqrt N)}.
}
\]

Crucially, no weight, row rescaling, repeated observation, or averaging has been introduced. `Omega_N` is an ordinary subset of the original raw mixed moments.

## Uniform absolute-noise stability

Let the retained complex error vector satisfy `|eta_nu|<=epsilon` samplewise. Then

\[
\|\eta\|_2
\le
\sqrt{|\Omega_N|}\,\epsilon
\le
\sqrt{8N}\,\epsilon.
\]

Least-squares recovery gives

\[
\begin{aligned}
\|\widehat b-b\|_2
&\le
\frac{\|\eta\|_2}
{\sigma_{\min}(A_{\Omega_N})}\\
&<
\sqrt{8N}\,\epsilon
\frac{2(1+15\sqrt N)}{27N}\\
&=
\frac{4\sqrt2(1+15\sqrt N)}{27\sqrt N}\,\epsilon\\
&\le
\boxed{\frac{64\sqrt2}{27}\,\epsilon}.
\end{aligned}
\]

The final inequality uses `N>=1`. The inverse modulus is therefore independent of source breadth under exactly the same adversarial per-sample absolute-noise semantics used in AF-284.

## Matching lower bound

An observation subset of `q` complex mixed moments gives a matrix in `C^{q x N}`. Exact recovery of every arbitrary coefficient vector in `C^N` requires injectivity, hence rank `N`, and therefore

\[
q\ge N.
\]

Together with the construction above,

\[
N
\le
q_{\mathrm{stable,raw}}(N)
\le
8N.
\]

Thus the open `Omega(N)` versus `O(N log N)` acquisition-order gap from AF-284 closes at `Theta(N)` for this model. This is an order statement, not an optimal-constant claim.

## Prior art and novelty assessment

The matrix-selection mechanism is classical. Avron--Boutsidis Theorem 3.4 is specifically stronger for this question than invoking a generic restricted-invertibility theorem that selects only a fixed fraction of the `N` coefficient dimensions: a subset with fewer than `N` complex observations cannot be injective on all of `C^N`, regardless of how well conditioned it is on a smaller span.

AF-284 had already noted Batson--Spielman--Srivastava weighted linear-size sparsification as a boundary marker, but correctly did not identify it with unweighted acquisition. The important prior-art correction here is that classical **matrix subset selection itself** already removes the weights in the final selected submatrix while retaining a pseudoinverse guarantee. The internal weighted sparsification certificate therefore does not force weighted raw observations.

The retained Mathia result is the specialization and acquisition-semantics bridge: realification converts the complex two-prime frame into the theorem's real setting, and closing selected scalar components under their source complex moments can only improve the Gram lower bound. This yields a genuine unweighted raw subset of linear size.

## Boundaries and failure modes

- The source support is still known a priori to be `1,...,N`. Unknown-support recovery is not addressed.
- The theorem is finite-breadth. It does not establish stable inversion for an infinite Dirichlet source or a limit as `N -> infinity` in a fixed observation space.
- The recovered variables are AF-283's weighted coefficients `b_n=a_n n^{-c}`. Passing to another target norm can reintroduce breadth-dependent conditioning.
- The result reduces the **number** of retained observations, not the coordinatewise cutoff. Every selected index still lies in the full square `0<=nu_j<30N`, so maximal mixed degree and maximal sampling time remain `O(N)`.
- Timing perturbations, relative error, correlated noise, finite timestamp precision, and coefficient-model mismatch require separate stability analyses.
- The subset is deterministically constructible through the classical algorithm, but no simple arithmetic closed form for `Omega_N` is obtained.
- The explicit constant `8` is convenient rather than optimized. Other choices `k=cN` with `c>2` produce the same linear-order conclusion with different stability constants.
- The lower bound `N` uses only rank. It does not say that every `N`-sample subset is stable, nor that the optimal stable subset has size exactly `N`.
- No zeta-zero, analytic-continuation, functional-equation, or RH consequence follows from the finite-prefix sampling statement alone.

## Decisive audit test

When a finite-prefix two-prime argument claims that unweighted raw acquisition intrinsically requires a logarithmic oversampling factor, form the complete AF-283 frame and ask whether the claim survives deterministic column subset selection applied to its realified transpose.

At `L=30N`, the inherited full-frame bound `sigma_min(A)>27N` and Avron--Boutsidis Theorem 3.4 imply a selected real component frame of size at most `8N`. Replacing each selected component by its complete underlying complex raw observation only adds positive-semidefinite Gram terms, so it cannot degrade the lower singular value. Any genuine superlinear lower bound must therefore impose an additional restriction absent from this model, such as a prescribed geometric sampling pattern, a smaller time horizon, timing precision, unknown support, or a different source/target norm.

## Consequence for the research line

The observation-count frontier opened by AF-283 and narrowed by AF-284 is now closed in order:

\[
\boxed{
q_{\mathrm{stable,raw}}(N)=\Theta(N).
}
\]

The remaining acquisition questions should no longer spend effort on whether generic unweighted raw sampling needs `N log N` observations. The live constraints are elsewhere: explicit/arithmetic structure of good subsets, maximal time horizon and timestamp precision, unknown-support recovery, source/target norm conversion, and whether any finite-prefix fidelity mechanism survives a meaningful infinite-source limit.