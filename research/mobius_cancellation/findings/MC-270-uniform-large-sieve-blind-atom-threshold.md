# MC-270 — Coefficient-uniform large-sieve bounds hit the blind-atom threshold exactly

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the Christoffel flat-energy formulation of `MC-268` and `MC-269`. Write

\[
\mathcal B_m=\{S\subseteq\mathcal P_y:|S|\le m\},
\qquad
Z=|\mathcal B_m|,
\]

\[
\mathcal T_t=\{T\subseteq\mathcal R_y:|T|=t\},
\qquad
C=|\mathcal T_t|=\binom{N_y}{t},
\]

and form the `C\times Z` sign matrix

\[
A_{T,S}=\chi_T(q_S)
=\prod_{r\in T}\left(\frac{q_S}{r}\right).
\tag{1}
\]

The flat Christoffel energy isolated in `MC-269` is

\[
F_{t,m}(y)
:=\sum_{T\in\mathcal T_t}
\left|\sum_{S\in\mathcal B_m}A_{T,S}\right|^2
=\|A\mathbf 1_Z\|_2^2.
\tag{2}
\]

The desired diagonal-scale estimate is

\[
F_{t,m}(y)\le L_y C Z.
\tag{3}
\]

A blind row `T` has `A_{T,S}=1` for every `S`, so one blind relation alone contributes exactly

\[
Z^2
\tag{4}
\]

to `(2)`. Hence a bound of the form `(3)` can exclude every blind row only in the strict range

\[
\boxed{L_y<Z/C.}
\tag{5}
\]

Now suppose one tries to prove `(3)` by first upgrading the flat vector to a coefficient-uniform large-sieve inequality

\[
\boxed{
\|Aa\|_2^2\le D_y\|a\|_2^2
\qquad\text{for every }a\in\mathbb C^Z.
}
\tag{6}
\]

Every row of `A` has exactly `Z` entries of modulus one, hence Euclidean norm `\sqrt Z`. Therefore

\[
\boxed{
\|A\|_{\mathrm{op}}^2\ge Z.
}
\tag{7}
\]

Consequently every valid uniform constant in `(6)` satisfies

\[
D_y\ge Z.
\tag{8}
\]

Applying `(6)` to the flat vector gives

\[
F_{t,m}(y)\le D_y Z,
\tag{9}
\]

but the right-hand side certified by any such operator-norm inequality is necessarily at least

\[
D_y Z\ge Z^2.
\tag{10}
\]

Thus a coefficient-uniform `\ell^2` large sieve, **even with the exact optimal operator norm of the sparse shell matrix**, cannot by itself prove the strict inequality `F_{t,m}(y)<Z^2` needed to exclude one blind row.

Equivalently, if a uniform large-sieve theorem is parametrized in the target normalization as

\[
D_y\le L_y C,
\tag{11}
\]

then `(8)` forces

\[
\boxed{L_y\ge Z/C,}
\tag{12}
\]

whereas blind exclusion requires the opposite strict inequality `(5)`. The obstruction lands **exactly at the blind-atom threshold**, independently of how efficiently the theorem exploits the sparse row family.

At the live Christoffel choice

\[
m=t+1,
\qquad
t\asymp\log\log y,
\]

with `k_y=|\mathcal P_y|\sim y/\log y` and `N_y=|\mathcal R_y|\sim y/\log y`, one has

\[
\boxed{
\frac ZC
=(1+o(1))\frac{k_y}{t+1}.
}
\tag{13}
\]

So the operator-norm floor `(12)` is precisely the same scale that `MC-268` identified as the maximal admissible loss. In particular, the desired regime `L_y=o(k_y/m)` cannot arise from a coefficient-uniform operator-norm estimate.

This sharpens the frontier left by `MC-269`. The missing theorem is **not** merely a better sparse quadratic large sieve in the usual coefficient-uniform sense. It must exploit the special flat source vector, or equivalent additional structure, before taking an operator norm.

No blind relation is excluded, `(3)` remains open, and no new bound for `M(X)` follows.

## 1. The row-norm floor is exact linear algebra

For any fixed `T`, the row vector

\[
r_T=(A_{T,S})_{S\in\mathcal B_m}
\]

satisfies

\[
\|r_T\|_2^2
=\sum_{S\in\mathcal B_m}|A_{T,S}|^2
=Z.
\tag{14}
\]

The operator norm obeys

\[
\|A\|_{\mathrm{op}}
=\|A^*\|_{\mathrm{op}}
\ge
\frac{\|A^*e_T\|_2}{\|e_T\|_2}
=\|r_T\|_2
=\sqrt Z,
\tag{15}
\]

which proves `(7)`. Equivalently, `AA^*` has diagonal entries `Z`, so its largest eigenvalue is at least `Z`.

This lower floor does not use quadratic reciprocity, prime distribution, or any estimate for off-diagonal correlations. It is present for every `C\times Z` matrix with unimodular entries.

The Frobenius identity makes the same geometry transparent:

\[
\|A\|_F^2=CZ.
\tag{16}
\]

Since `A` has rank at most `C`, the average squared nonzero singular value is at least `Z`. Even a perfectly orthogonal row family, for which

\[
AA^*=ZI_C,
\tag{17}
\]

has `\|A\|_{\mathrm{op}}^2=Z`. Thus improving arithmetic row orthogonality all the way to the ideal operator-norm configuration still does not make the uniform estimate strict enough to rule out one blind atom through `(9)`.

## 2. Why the flat vector can still be much better than the operator norm

The obstruction concerns only the relaxation from the specific vector `\mathbf 1_Z` to arbitrary coefficients.

For a random-looking `C\times Z` sign matrix with `Z\gg C`, the natural size of the flat energy is

\[
\|A\mathbf1_Z\|_2^2\asymp CZ,
\tag{18}
\]

while the unavoidable operator-norm scale is at least

\[
\|A\|_{\mathrm{op}}^2\|\mathbf1_Z\|_2^2
\ge Z^2.
\tag{19}
\]

The ratio between these two scales is

\[
Z/C,
\tag{20}
\]

which is exactly the Christoffel blind-exclusion budget. The desired gain is therefore a **vector-specific cancellation statement**: it asks that the all-one source vector avoid the large singular directions of the arithmetic matrix. A theorem uniform over arbitrary source coefficients deliberately discards that information.

This also explains why ordinary large-sieve duality does not repair the issue. Passing to the adjoint preserves the same operator norm, and `(7)` remains true. Any route that uses Cauchy--Schwarz or Hilbert-space duality to replace the flat coefficients by an unrestricted coefficient vector before the decisive arithmetic estimate inherits the same floor.

## 3. The live asymptotic threshold

For `m=o(k_y)`,

\[
Z
=\sum_{s=0}^m\binom{k_y}{s}
=\binom{k_y}{m}\left(1+O(m/k_y)\right).
\tag{21}
\]

For `t=o(N_y)`,

\[
C=\binom{N_y}{t}.
\tag{22}
\]

Set `m=t+1`. Then

\[
\frac ZC
=(1+o(1))
\frac{\binom{k_y}{t+1}}{\binom{N_y}{t}}
=(1+o(1))
\frac{k_y}{t+1}
\left(\frac{k_y}{N_y}\right)^t.
\tag{23}
\]

The prime number theorem gives

\[
\frac{k_y}{N_y}=1+O(1/\log y),
\tag{24}
\]

and `t=O(\log\log y)` implies

\[
\left(\frac{k_y}{N_y}\right)^t=1+o(1).
\tag{25}
\]

This proves `(13)`.

A blind row contributes `Z^2`. Dividing that atom by the target diagonal `CZ` gives exactly `Z/C`. Hence the combinatorial ratio in `(13)` is not an artifact of the detector analysis: it is simultaneously

- the amplification of one blind row above the natural diagonal;
- the maximal loss allowed before blindness becomes invisible; and
- the unavoidable loss floor of every coefficient-uniform operator-norm estimate.

## 4. Prior art and novelty boundary

The Hilbert-space duality principle and its operator-norm formulation are classical ingredients of large-sieve theory; no novelty is claimed for `(6)`--`(10)`, singular values, Frobenius norms, or the equality of the norms of an operator and its adjoint. The generic and sparse large-sieve literature already audited in `MC-262`, `MC-263`, and `MC-269` remains the relevant comparison surface, including Heath-Brown/Liu for quadratic characters and Baier/Iwaniec for sparse or prime-modulus variants.

A targeted literature search through 13 September 2026 did not identify a flat-coefficient theorem for this exact shell-product/Hamming-ball matrix that bypasses the coefficient-uniform operator norm. That search boundary is not a novelty claim. The durable delta here is the exact collision of two scales **inside the current Mathia object**: the row-norm lower bound forces the usual uniform large-sieve constant to meet or exceed the contribution of one blind row precisely when the Christoffel detector needs to go strictly below it.

## 5. Boundaries and updated frontier

- `(7)` is a lower bound on a **uniform operator norm**, not on the actual flat energy `(2)`. It does not disprove the diagonal-scale target `(3)`.
- The obstruction applies to proofs that pass through an unrestricted coefficient inequality of the form `(6)`. A theorem specialized to `a_S\equiv1`, or to a genuinely restrictive structured coefficient class that retains the flat vector without paying the full operator norm, is not covered.
- Weighted norms or preconditioners are not excluded in general. They must be audited against the blind-row atom after translating back to the original flat energy; a hidden renormalization cannot count as a gain.
- Sparse-modulus arithmetic remains relevant, but the useful question is now narrower than "prove a better sparse large sieve": one needs **flat-vector discrepancy / signed off-diagonal cancellation**, not merely a smaller coefficient-uniform operator norm.
- The layerwise absolute-value route remains separately blocked by `MC-269`'s precision ladder.

The next decisive test is therefore to exploit the equal flat coefficients before any uniformization step: derive a signed bilinear or combinatorial identity for

\[
\langle\mathbf1_Z,A^*A\mathbf1_Z\rangle-CZ
\]

whose off-diagonal cancellation can be bounded directly at `o((Z/C)CZ)=o(Z^2)`, or construct an admissible arithmetic configuration showing that such flat-vector cancellation fails.