# AF-287 — Independent rowwise jitter has the same inverse-log scale after frame sparsification

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `FINITE-BREADTH`, `TIMING`, `STABILITY`, `FRAME-SPARSIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-286 left a `sqrt(N)` gap for independent timing jitter. Its elementary samplewise estimate gave a sufficient scale `T=O(1/(sqrt(N) log N))`, while the common-offset subclass already forced the necessary scale `T=O(1/log N)` for fixed relative coefficient distortion.

That gap is not intrinsic to independent rowwise jitter. For the known ordinary-Dirichlet prefix `1,...,N`, there is an **unweighted subset of `O(N)` raw two-prime mixed samples** whose nominal sampling matrix has condition number bounded by an absolute constant. On such a frame, arbitrary independent timing perturbations

\[
|\tau_j|\le T
\]

obey the operator perturbation bound

\[
\boxed{
\|\widetilde A-A\|_{2\to2}
\le
\|A\|_{2\to2}\bigl(e^{T\log N}-1\bigr).
}
\]

Consequently, if `K` is the uniform condition-number bound of the selected frame, the nominal least-squares decoder satisfies

\[
\boxed{
\frac{\|\widehat b-b\|_2}{\|b\|_2}
\le
K\bigl(e^{T\log N}-1\bigr).
}
\]

For every fixed target distortion `rho>0`, it is therefore sufficient that

\[
\boxed{
T\le \frac{\log(1+\rho/K)}{\log N}.
}
\]

AF-286 proves that the common-offset subclass already requires `T=O(1/log N)` for any fixed coefficient-distortion threshold below `2`. Hence the worst-case timing scale for arbitrary rowwise jitter is order-sharp:

\[
\boxed{T_{\mathrm{jitter}}(N)=\Theta(1/\log N).}
\]

The previous `sqrt(N)` loss came from converting an `ell^1` source bound to `ell^2` after using only a lower singular-value estimate for AF-285's selected frame. It is removed by selecting a linearly sized frame with **both** lower and upper spectral bounds.

## Step 1: the complete two-prime frame is uniformly conditioned

Use AF-283's complete mixed square at

\[
L=30N,
\qquad
M=L^2=900N^2.
\]

Let `A_full in C^{M x N}` be its observation matrix. AF-282 gives torus separation `q_N >= c_0/N`, so `q_N L` is bounded below by a constant strictly larger than `8`.

Kunis, Nagel, and Strotmann prove explicit lower bounds for the smallest singular value and upper bounds for the largest singular value/condition number of separated multivariate Vandermonde matrices. Their Theorem 4.2 supplies AF-283's lower bound

\[
\sigma_{\min}(A_{\mathrm{full}})>0.9L,
\]

while their general separated-node upper bound gives

\[
\sigma_{\max}(A_{\mathrm{full}})\le C_1L
\]

for an absolute constant `C_1` in this fixed two-dimensional, fixed-separation regime. Therefore

\[
\kappa(A_{\mathrm{full}})\le K_1
\]

with `K_1` independent of `N`.

Primary source: Stefan Kunis, Dominik Nagel, and Anna Strotmann, **“Multivariate Vandermonde matrices with separated nodes on the unit circle are stable,”** *Applied and Computational Harmonic Analysis* 58 (2022), 50–59, DOI `10.1016/j.acha.2022.01.001`, arXiv:`2103.08167`.

## Step 2: Kadison-Singer sparsification gives an unweighted `O(N)` subframe with bounded condition number

Write the rows of `A_full` as vectors `a_j in C^N` and set

\[
S=A_{\mathrm{full}}^*A_{\mathrm{full}}.
\]

Whiten the frame:

\[
u_j=S^{-1/2}a_j^*.
\]

Then

\[
\sum_{j=1}^{M}u_ju_j^*=I_N.
\]

Every raw row has squared norm exactly `N`, while `lambda_min(S)>0.81L^2`. Hence

\[
\|u_j\|_2^2
\le
\frac{N}{0.81L^2}
=
O(1/N).
\]

The Marcus-Spielman-Srivastava solution of Weaver's `KS_2` theorem says that an isotropic family with maximum squared vector norm `delta` admits a bipartition for which each part has frame operator within `O(sqrt(delta))` of one half of the identity. Equivalently, for small `delta`, both halves have lower and upper frame bounds comparable to `1/2`.

Iterate this partitioning procedure. At every stage choose the half with no more vectors, whiten that selected half again, and continue while the maximum whitened leverage remains below a fixed sufficiently small absolute threshold `delta_*`.

The leverage recurrence has the form

\[
\delta_{r+1}
\le
\frac{\delta_r}
{1/2-\sqrt{2\delta_r}-\delta_r}.
\]

Thus `delta_r` grows essentially like `2^r delta_0`; the multiplicative correction is bounded because the accumulated discrepancy is controlled by the convergent geometric sum of `sqrt(delta_r)` up to the fixed threshold. Starting from `delta_0=O(1/N)`, one may therefore perform `log_2 N-O(1)` halvings before reaching `delta_*`.

The selected family then has

\[
|\Omega_N|=O(M/N)=O(N)
\]

rows. At the same time, the product of the successive upper/lower frame-bound ratios stays bounded by an absolute constant. Undoing the initial whitening and using the uniform condition number of `A_full` yields

\[
\boxed{
|\Omega_N|\le C_2N,
\qquad
\kappa(A_{\Omega_N})\le K
}
\]

for absolute constants `C_2,K`.

No weights, repeated observations, or row rescalings are retained: `Omega_N` is an ordinary subset of the original raw mixed samples. This is the same acquisition semantics as AF-285, but the selection is chosen to retain a bounded **condition number**, not merely a bounded pseudoinverse under samplewise additive error.

Primary partition source: Adam W. Marcus, Daniel A. Spielman, and Nikhil Srivastava, **“Interlacing Families II: Mixed Characteristic Polynomials and the Kadison-Singer Problem,”** *Annals of Mathematics* 182(1), 327–350 (2015), DOI `10.4007/annals.2015.182.1.8`.

Closely adjacent modern prior art is Marcin Bownik, **“Selector form of Weaver's conjecture, Feichtinger's conjecture, and frame sparsification,”** arXiv:`2405.18235` (2024), which develops iterated selector/KS mechanisms and nearly tight frame sparsification. No frame-sparsification novelty is claimed here.

## Step 3: rowwise timing jitter is an operator perturbation, not an `ell^1` source perturbation

For the selected nominal times `t_j`, write

\[
A_{j,n}=e^{-it_j\log n}.
\]

Under independent timing errors `tau_j`,

\[
\widetilde A_{j,n}
=A_{j,n}e^{-i\tau_j\log n}.
\]

Let

\[
D_{\tau^k}=\operatorname{diag}(\tau_1^k,\ldots,\tau_q^k),
\qquad
\Lambda=\operatorname{diag}(\log1,\ldots,\log N).
\]

Entrywise expansion of the exponential gives the exact matrix identity

\[
\widetilde A-A
=
\sum_{k\ge1}
\frac{(-i)^k}{k!}
D_{\tau^k}A\Lambda^k.
\]

Since `||D_{tau^k}||<=T^k` and `||Lambda||=log N`,

\[
\begin{aligned}
\|\widetilde A-A\|
&\le
\|A\|
\sum_{k\ge1}
\frac{(T\log N)^k}{k!}\\
&=
\boxed{\|A\|\bigl(e^{T\log N}-1\bigr)}.
\end{aligned}
\]

This estimate acts directly in coefficient `ell^2`. It never passes through `||b||_1`, so the `sqrt(N)` conversion in AF-286 disappears.

## Nominal decoding and perturbed-frame stability

With noiseless jittered observations

\[
\widetilde y=\widetilde A b
\]

and the nominal decoder `A^dagger`,

\[
\widehat b-b
=A^\dagger(\widetilde A-A)b.
\]

Therefore

\[
\frac{\|\widehat b-b\|_2}{\|b\|_2}
\le
\|A^\dagger\|\,\|\widetilde A-A\|
\le
\kappa(A)(e^{T\log N}-1)
\le
K(e^{T\log N}-1).
\]

The same estimate also controls whether the actual jittered acquisition remains a stable frame. Weyl's inequality gives

\[
\sigma_{\min}(\widetilde A)
\ge
\sigma_{\min}(A)
\left[1-K(e^{T\log N}-1)\right].
\]

Thus any fixed `T log N` small enough that

\[
K(e^{T\log N}-1)<1
\]

preserves injectivity and a breadth-uniform condition margin.

## Matching lower bound from the common-offset subclass

Independent jitter permits the special choice

\[
\tau_j=\tau
\qquad\text{for all }j.
\]

AF-286 proves that this common offset acts exactly as the coefficient gauge

\[
b\mapsto D_\tau b
\]

and that the worst-case relative coefficient displacement reaches a fixed nonzero level when `|tau| log N` is a fixed nonzero constant. In particular, no decoder that must recover arbitrary complex coefficients can tolerate `T log N -> infinity` with fixed worst-case relative distortion.

Combining that necessary subclass with the bounded-condition sufficiency above closes the order gap:

\[
\boxed{
T_{\mathrm{independent\ jitter}}(N)
=\Theta(1/\log N).
}

The exact constant depends on the target distortion and the selected frame condition number; the order does not.

## Prior art and novelty assessment

No novelty is claimed for multivariate Vandermonde conditioning, Kadison-Singer/Weaver partitioning, frame sparsification, or exponential-sum timing perturbation.

The new retained content is the **resource bridge inside the Arithmetic Fidelity two-prime channel**. AF-283 supplies a uniformly conditioned dense arithmetic frame; classical KS partitioning sparsifies it to linearly many unweighted raw samples without losing bounded condition number; the exact rowwise exponential perturbation factorization then converts bounded frame condition directly into an inverse-log timing law. This removes the artificial `sqrt(N)` source-norm loss left by AF-286.

## Boundaries and failure modes

- The source support is still the known finite prefix `1,...,N`. Unknown support and infinite Dirichlet sources are not covered.
- The `O(N)` subset obtained through iterated KS partitioning is existential. No simple arithmetic closed form or efficient selection algorithm is asserted here.
- The linear-size constant from this argument is not optimized and can be much larger than AF-285's explicit `8N` count. The point is bounded condition number and timing stability, not the best cardinality constant.
- The timing model is adversarial absolute rowwise offset `|tau_j|<=T`. Relative clock error, drift with additional structure, quantized requested times, correlated stochastic jitter, and clock-rate error are different models.
- The decoder bound concerns the weighted coefficient vector `b_n=a_n n^{-c}` in `ell^2`. A different downstream norm or target can have a different timing budget.
- Common-offset-invariant downstream targets can require less calibration than full coefficient recovery; AF-286's gauge quotient remains relevant for such targets.
- No analytic continuation, zero-location statement, functional equation, or RH consequence follows from this finite-prefix timing theorem alone.

## Decisive audit test

When independent timing jitter is claimed to require precision asymptotically finer than `1/log N` solely because a samplewise estimate produces `||b||_1`, first ask whether the nominal raw frame has been selected with a bounded condition number.

For a bounded-condition frame, expand the rowwise phase perturbation at matrix level. The exact factorization above gives

\[
\|\widetilde A-A\|
\le
\|A\|(e^{T\log N}-1),
\]

so coefficient stability depends on `T log N` and the frame condition number, not on an additional `sqrt(N)` source-norm conversion. Any stronger precision obstruction must therefore identify an acquisition restriction that prevents bounded-condition `O(N)` subframes, a different target norm, unknown support, or a more demanding timing-error model.

## Consequence for the research line

The finite-prefix two-prime timing frontier opened by AF-286 is closed at order level. Observation count can be `Theta(N)`, mixed degree/time horizon can be `Theta(N)`, and arbitrary independent rowwise timing jitter requires only the same order of fractional calibration as the common-mode obstruction:

\[
\boxed{T=\Theta(1/\log N).}
\]

The next useful questions should no longer treat the `sqrt(N)` jitter gap as a live obstruction. The remaining timing work is target-sensitive: determine which RH-relevant or arithmetic downstream functionals descend through the common clock gauge and therefore need no clock-origin lift, and which require the full coefficient-level timing fidelity quantified here.