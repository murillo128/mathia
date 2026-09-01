# WI-082 — Vandermonde congruence fixes signed scalar inertia before overcompleteness

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes a many-modulus inertia escape left open by WI-081 for any source-faithful signed scalar Ramanujan reduction.

After aggregating duplicate scalar moduli, let

\[
A_\omega^{(N)}=\sum_m \omega_m B_m^{(N)},
\qquad
B_m^{(N)}=U_m^{(N)}(U_m^{(N)})^*,
\]

where `omega_m` are nonzero real coefficients and the columns of `U_m^(N)` are the primitive Fourier nodes `e(ax/m)` sampled on `N` consecutive integers. Put

\[
K_+=\sum_{\omega_m>0}\varphi(m),
\qquad
K_-=\sum_{\omega_m<0}\varphi(m),
\qquad
K=K_++K_-.
\]

Then the exact weighted synthesis factorization is

\[
\boxed{A_\omega^{(N)}=WJW^*,}
\]

where `W` is obtained by concatenating `sqrt(|omega_m|) U_m^(N)` and

\[
J=\operatorname{diag}(I_{K_+},-I_{K_-}).
\]

All primitive fractions belonging to distinct reduced denominators are distinct Fourier nodes. Hence the combined `N x K` matrix `W` is a rectangular Vandermonde matrix up to invertible diagonal column scalings and

\[
\boxed{\operatorname{rank}W=\min(N,K).}
\tag{1}
\]

This immediately gives a stronger global inertia statement than the pairwise boundary-rank bookkeeping of WI-081.

If `K<=N`, then

\[
\boxed{
 n_+(A_\omega^{(N)})=K_+,
 \qquad
 n_-(A_\omega^{(N)})=K_-,
 \qquad
 n_0(A_\omega^{(N)})=N-K.
}
\tag{2}
\]

Thus **finite-window leakage cannot erase even one positive or negative inertia direction before the signed primitive-frequency dictionary becomes overcomplete**. Cross-modulus nonorthogonality, pairwise lcm boundary defects, singular-value sizes and outer coefficient magnitudes do not affect the signature in this regime.

If `K>=N`, let `E=\operatorname{ran}W^*\subset\mathbf C^K`. Then `\dim E=N` and the form represented by `A_omega^(N)` is congruent to the restriction of `J` to `E`. Consequently

\[
\boxed{
 n_+(A_\omega^{(N)})\ge (N-K_-)_+,
 \qquad
 n_-(A_\omega^{(N)})\ge (N-K_+)_+.
}
\tag{3}
\]

Moreover the radical of the restricted form satisfies

\[
\boxed{n_0(A_\omega^{(N)})\le \min\{N,K-N\}.}
\tag{4}
\]

In particular, any scalar signed mechanism that hopes to make **both** inertia signs small must carry at least about `N` primitive modes on each sign side. Merely arranging many pairwise leakage channels is insufficient. If `K_+>=N` and `K_->=N`, the positive and negative dictionaries each span the full sample space and the global cross Gram has the exact rank

\[
\boxed{\operatorname{rank}(U_+^*U_-)=N.}
\tag{5}
\]

So the many-family possibility mentioned in WI-081 — that shared dependencies might make the full cross rank much smaller than the sum of pairwise ranks — disappears completely once both sign-side dictionaries individually saturate the window. At rank/inertia level the only nontrivial transition is therefore **overcompleteness**, not pairwise boundary leakage.

## 1. Exact signed synthesis factorization

For one modulus `m`, write

\[
(U_m^{(N)})_{x,a}=e(ax/m),
\qquad 0\le x<N,
\qquad a\in(\mathbf Z/m\mathbf Z)^\times.
\]

As in WI-079--WI-081,

\[
B_m^{(N)}=U_m^{(N)}(U_m^{(N)})^*
\]

has Ramanujan kernel `c_m(x-y)`. Aggregate repeated copies of the same scalar modulus first; if the aggregate coefficient vanishes, discard that block.

Order the surviving positive blocks first and negative blocks second, and set

\[
W=\bigl[\sqrt{|\omega_m|}\,U_m^{(N)}\bigr]_m.
\]

Then direct multiplication gives

\[
WJW^*
=\sum_m\operatorname{sgn}(\omega_m)|\omega_m|
 U_m^{(N)}(U_m^{(N)})^*
=A_\omega^{(N)}.
\tag{6}
\]

No large-sieve inequality, common-period completion or asymptotic estimate is involved.

## 2. Distinct reduced denominators give full Vandermonde rank

A column of the combined dictionary is the sampled exponential

\[
(1,z,z^2,\ldots,z^{N-1})^T,
\qquad
z=e(a/m),
\]

with `(a,m)=1`. If

\[
e(a/m)=e(b/n)
\]

for primitive residue classes, then the reduced fractions `a/m` and `b/n` agree modulo one. Choosing their standard representatives forces the reduced denominators and numerators to agree. Thus distinct `(m,a)` labels after modulus aggregation give distinct nonzero nodes `z`.

The first `r=min(N,K)` rows and any `r` columns form an ordinary Vandermonde matrix on distinct nodes, with nonzero determinant

\[
\prod_{i<j}(z_j-z_i).
\]

The additional factors `sqrt(|omega_m|)` are nonzero diagonal column scalings. Hence (1) follows. Translating the consecutive sample window only multiplies columns by unit complex phases and does not change rank or inertia.

This is the global piece missing from a pairwise leakage analysis: **the union of all active signed primitive Fourier atoms remains linearly independent until their total count reaches the sample dimension**.

## 3. Undercomplete dictionaries preserve the entire sign ledger

Assume `K<=N`. Equation (1) says that `W` has full column rank. Therefore `W^*:C^N -> C^K` is surjective and has kernel dimension `N-K`.

On `(ker W^*)^perp`, the map `W^*` is an isomorphism onto `C^K`, and by (6)

\[
\langle x,A_\omega^{(N)}x\rangle
=\langle W^*x,JW^*x\rangle.
\tag{7}
\]

Thus the nondegenerate part of the finite-window form is congruent to `J`. Sylvester's law of inertia gives exactly `K_+` positive and `K_-` negative directions, while `ker W^*` contributes the `N-K` zeros. This proves (2).

The conclusion is stronger than saying that pairwise cross correlations are small. They can be large and even full rank on many pairs; as long as the **combined** primitive-frequency synthesis is undercomplete, those correlations amount only to a change of coordinates of the same indefinite form.

Hence a sign-sensitive scalar proposal cannot obtain an inertia saving from finite-window mixing in the regime `K<=N`. To change the sign ledger it must first cross the information-theoretic threshold

\[
\boxed{K>N.}
\tag{8}
\]

## 4. Overcompleteness gives universal sign-side lower bounds

Assume `K>=N`. Now `W` has full row rank, so

\[
W^*:C^N\longrightarrow C^K
\]

is injective. Let

\[
E=\operatorname{ran}W^*,
\qquad \dim E=N.
\]

Equation (7) identifies the inertia of `A_omega^(N)` with the inertia of the nondegenerate ambient signature form `J` restricted to `E`.

Let `H_+` and `H_-` be the coordinate eigenspaces of `J`, of dimensions `K_+` and `K_-`. Grassmann's dimension inequality gives

\[
\dim(E\cap H_+)
\ge N+K_+-K=N-K_-,
\]

and `J` is positive definite on `H_+`. Therefore

\[
n_+(A_\omega^{(N)})\ge(N-K_-)_+.
\]

The negative statement is identical, proving (3).

The radical is

\[
E\cap E^{\perp_J},
\]

where orthogonality is taken with respect to the nondegenerate `J`-form. Since

\[
\dim E^{\perp_J}=K-N,
\]

its dimension is at most `min(N,K-N)`, proving (4).

Thus `K-N` is the first global **redundancy budget** available to create null directions of the compressed indefinite form. Pairwise lcm defects do not provide an independent nullity budget.

## 5. Double sign-side saturation forces full global cross rank

Write `U_+` and `U_-` for the concatenated unweighted positive and negative primitive-frequency dictionaries. Their ranks are

\[
\operatorname{rank}U_+=\min(N,K_+),
\qquad
\operatorname{rank}U_-=\min(N,K_-)
\tag{9}
\]

by the same Vandermonde argument.

If `K_+>=N` and `K_->=N`, then `U_-:C^{K_-}->C^N` is surjective and `U_+^*:C^N->C^{K_+}` is injective. Their composition therefore has rank `N`:

\[
\operatorname{rank}(U_+^*U_-)=N.
\]

This is (5). In that doubly saturated regime, no many-family linear dependence can reduce the rank of the total opposite-sign coupling. Any useful signed cancellation must instead use the **metric** data discarded by rank — coefficient magnitudes, singular-value geometry and the exact location of `E` relative to the positive/negative cones — or must retain source labels that were already lost in the scalar reduction.

## 6. Relation to WI-079--WI-081 and the Yang route

WI-079 showed that an ordinary positive sparse-moduli large sieve discards the outer signs and that a surviving scalar route must estimate the signed Ramanujan operator itself. WI-080 showed that complete-period modulus blocks are orthogonal projectors, so any scalar sign interaction is created by finite time-limiting. WI-081 then quantified that interaction pairwise through nearest-lcm boundary ranks and showed that pairwise rank is often maximal.

The present result changes the global interpretation of those pairwise couplings. For **inertia**, one does not need to add their ranks while `K<=N`: the entire signed family is a full-column-rank indefinite Gram synthesis, and Sylvester congruence fixes the signature exactly. Once `K>N`, equations (3)--(4) show that the only universal rank-level resource for changing the sign ledger is redundancy of the combined dictionary. When both sign families already have at least `N` primitive modes, even the aggregate cross rank is forced to be full.

Therefore a future scalar repair should first compute the source-faithful ledgers `K_+`, `K_-` and `N` after exact coefficient aggregation. If the relevant source range is undercomplete, the scalar inertia route is closed outright. If it is overcomplete, pairwise boundary-rank optimization is no longer the decisive quantity; the live problem is the weighted position of the Vandermonde image `E=ran W^*` inside the ambient Pontryagin space, or a richer labelled/two-dimensional representation before scalarization.

This remains conditional on the source-interface premise already stated in WI-079--WI-081: Mathia has **not** proved that the entire post-local-main Yang covariance reduces exactly to a signed scalar operator of the form (6). The result is an exact barrier for that proposed interface, not a proof of the Yang--Yang theorem.

## 7. Prior art and novelty boundary

Every load-bearing algebraic ingredient is classical.

- Sylvester's law of inertia is the standard congruence invariant for Hermitian/symmetric quadratic forms. A textbook reference is Richard Kaye and Robert Wilson, *Linear Algebra*, Oxford University Press (1998), Chapter 7, **Quadratic forms and Sylvester's law of inertia**. The complex Hermitian `*`-congruence version used in (7) is the standard analogue.
- The indefinite-Gram/Pontryagin-space viewpoint `W J W^*` is standard. For a recent modern use of indefinite Gram matrices and full-rank congruence arguments, see A. Belton et al., **Negativity-preserving transforms of tuples of symmetric matrices**, *Proceedings of the London Mathematical Society* (2026), DOI `10.1112/plms.70147`.
- Vandermonde full-rank on distinct Fourier nodes, Grassmann dimension inequalities and the radical bound for a restricted nondegenerate form are classical finite-dimensional linear algebra.
- The Ramanujan-subspace dictionary itself is established prior art: P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals** and **Part II: FIR Representations and Applications**, *IEEE Transactions on Signal Processing* 62 (2014), and the finite-duration/near-orthogonality developments cited in WI-080--WI-081.

A targeted search of signed/indefinite Gram matrices, Ramanujan-subspace finite dictionaries and finite-window periodic dictionaries located the classical ingredients and the established signal-processing framework, but not a source making this exact WI-079 scalar-interface deduction. **No priority claim is made.** The durable Mathia content is the application of those classical facts to close the many-family inertia ambiguity left by WI-081.

## 8. Falsification and boundary conditions

1. **Real aggregated coefficients.** The signature factorization requires real `omega_m`, as in the signed scalar interface isolated in WI-079. Complex outer coefficients would not define the same Hermitian inertia problem.
2. **Aggregate equal moduli first.** Two copies of the same scalar modulus share identical primitive nodes and must be combined into one coefficient before counting `K_+` or `K_-`; a zero aggregate is removed.
3. **Primitive nodes are essential.** The Vandermonde count uses the exact primitive-residue dictionaries underlying the Ramanujan blocks. A different scalarization with repeated or aliased Fourier nodes must recompute the synthesis rank rather than import (1).
4. **Consecutive finite window.** Consecutive integer samples give the ordinary Vandermonde matrix. Translation is harmless; arbitrary sparse sampling can introduce aliasing and is outside the statement.
5. **Inertia is not operator norm.** Equation (2) fixes sign counts, not eigenvalue sizes. In the overcomplete regime a small operator norm or weighted cancellation could still be possible even when rank is full.
6. **Overcomplete bounds are lower bounds, not exact generic signatures.** Equations (3)--(4) use only ambient dimensions. The exact inertia for `K>N` can depend on weights and the detailed finite-window geometry.
7. **Source-faithful scalar reduction remains unproved.** This finding must not be used as though the locked four-prime Yang covariance had already been shown to equal (6).
8. **No zeta theorem is upgraded.** The current unconditional simple-critical proportion remains the previously certified Mathia bound; WI-082 is a structural barrier/redirection only.

## 9. Consequence for the research program

The generic pairwise-rank branch is now exhausted one step further. WI-081 already showed that many individual prime-pair leakage ranks are maximal; WI-082 shows that, before overcompleteness, **none of those couplings can change inertia at all**, because they sit inside a full-rank congruence of the original sign matrix. After overcompleteness, the first universal control is the sign-side primitive-frequency ledger `(K_+,K_-,N)`, not the sum of nearest-lcm boundary ranks.

The cheapest decisive test for any future source-faithful signed scalar proposal is therefore:

\[
\boxed{
\text{aggregate exact scalar coefficients}
\;\longrightarrow\;
(K_+,K_-,N)
\;\longrightarrow\;
\text{apply (2) or (3) before any large-sieve work}.
}
\]

If the source ledger is undercomplete, the inertia escape is dead. If it is overcomplete but one sign side has fewer than `N` primitive modes, equation (3) forces a residual inertia of the opposite sign. Only the doubly saturated regime leaves a genuinely unconstrained scalar sign-cancellation problem, and there the next invariant must be metric/weighted or source-labelled rather than another generic rank estimate.