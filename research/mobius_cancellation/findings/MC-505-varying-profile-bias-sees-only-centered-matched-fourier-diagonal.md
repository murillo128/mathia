# MC-505 — Varying-profile bias sees only the centered matched Fourier diagonal

**Finding ID:** `MC-505`

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `CLASSICAL-LINEAR-ALGEBRA+DERIVED` · `PRIOR-ART-AUDITED` · `NO-GENERAL-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-503` and `MC-504` price a quadratic-character bias by first decomposing the first-exit data into start weights and hard-mask profile classes. That class decomposition is not intrinsic. For an arbitrary varying-profile source matrix, the character kernel sees only one canonical one-dimensional slice of its two-dimensional Fourier transform, and the resulting decomposition-free tariff is the nuclear norm of the **doubly centered start-profile interaction**.

Let `p` be an odd prime and let

\[
F:\mathbf F_p\to\mathbf C
\]

satisfy

\[
\sum_{t\in\mathbf F_p}F(t)=0,
\qquad
\max_{k\in\mathbf F_p}|\widehat F(k)|\le C\sqrt p,
\tag{1}
\]

with the unnormalized Fourier convention

\[
\widehat F(k)=\sum_{t\in\mathbf F_p}F(t)e_p(-kt).
\tag{2}
\]

This includes the centered quadratic-character trace kernels used in the current first-exit branch.

For any real coefficient matrix

\[
B=(B_{x,j})_{x,j\in\mathbf F_p},
\tag{3}
\]

define

\[
\mathcal C_F(B)
:=
\sum_{x,j\in\mathbf F_p}B_{x,j}F(x+j).
\tag{4}
\]

In the hard-mask application, `x` is the physical start residue and `j` is the profile offset; `B_{x,j}` is the total coefficient mass occupying that start-offset cell. Thus `(4)` allows arbitrary profile variation without choosing profile classes first.

For

\[
d_k(B)
:=
\frac1p\sum_{x,j}B_{x,j}e_p(kx)e_p(kj),
\tag{5}
\]

Fourier inversion gives the exact identity

\[
\boxed{
\mathcal C_F(B)
=
\sum_{k\ne0}\widehat F(k)d_k(B).
}
\tag{6}
\]

The zero frequency disappears because `F` is centered. Consequently

\[
\boxed{
|\mathcal C_F(B)|
\le
C\sqrt p\sum_{k\ne0}|d_k(B)|.
}
\tag{7}
\]

So the quadratic-character bias does **not** see the full two-dimensional Fourier spectrum of the start-profile table. It sees only the matched diagonal where the start and profile-offset frequencies are equal.

Let

\[
P=I-\frac1p\mathbf1\mathbf1^{\!T},
\qquad
B^\circ=PBP.
\tag{8}
\]

Then `d_k(B)=d_k(B^\circ)` for every `k!=0`, hence

\[
\mathcal C_F(B)=\mathcal C_F(B^\circ).
\tag{9}
\]

Start-only marginals, offset-only marginals, and the grand mean are therefore annihilated exactly. Only genuine centered start-by-profile interaction can contribute.

Moreover,

\[
\boxed{
\sum_{k\ne0}|d_k(B)|
\le
\|B^\circ\|_*,
}
\tag{10}
\]

where `||.||_*` is the nuclear/trace norm. Combining `(7)` and `(10)` gives the canonical decomposition-free bound

\[
\boxed{
|\mathcal C_F(B)|
\le
C\sqrt p\,\|B^\circ\|_*.
}
\tag{11}
\]

For a nonnegative physical coefficient table let

\[
W=\sum_{x,j}B_{x,j}.
\tag{12}
\]

When `B^circ != 0`, define the interaction participation

\[
R_{\rm int}(B)
:=
\frac{W^2}{\|B^\circ\|_*^2},
\tag{13}
\]

and set `R_int=+infinity` when `B^circ=0`. Then

\[
\boxed{
\frac{|\mathcal C_F(B)|}{W}
\le
C\sqrt{\frac{p}{R_{\rm int}(B)}}.
}
\tag{14}
\]

Thus the varying-profile branch has a sharper decisive object than the number of profile classes or their marginal supports: the centered interaction complexity of the actual source-start/profile incidence table. Proving `R_int >> p` would force cancellation through this certificate; `R_int=O(p)` leaves order-one bias compatible with the square-root Fourier multiplier.

This is a certificate refinement, not a proof that the first-exit matrix has large `R_int`, and not a bound for `M(x)`.

## Derivation

Fourier inversion gives

\[
F(x+j)
=
\frac1p\sum_k\widehat F(k)e_p(kx)e_p(kj).
\tag{15}
\]

Substitution into `(4)` yields

\[
\mathcal C_F(B)
=
\sum_k\widehat F(k)d_k(B).
\tag{16}
\]

Since `Fhat(0)=0`, this is `(6)`, and `(1)` immediately gives `(7)`.

To prove `(10)`, let `U` be the unitary Fourier matrix

\[
U_{x,k}=p^{-1/2}e_p(kx).
\tag{17}
\]

Then

\[
(U^TBU)_{k,k}=d_k(B).
\tag{18}
\]

Both `U` and `U^T` are unitary, so

\[
\|U^TBU\|_*=\|B\|_*.
\tag{19}
\]

For any matrix, the `l^1` norm of its diagonal is at most its nuclear norm. Applying this after double centering gives

\[
\sum_{k\ne0}|d_k(B)|
=
\sum_{k\ne0}|d_k(B^\circ)|
\le
\|B^\circ\|_*.
\tag{20}
\]

This proves `(10)`--`(11)`.

There is an equivalent kernel proof. Put

\[
K_{x,j}=F(x+j).
\tag{21}
\]

If `R` is the column-reversal permutation `j -> -j`, then `KR` is the circulant convolution matrix with kernel `F`. Hence its singular values are `|Fhat(k)|`, so

\[
\|K\|_{\rm op}
=
\max_k|\widehat F(k)|
\le C\sqrt p.
\tag{22}
\]

Because `F` is centered,

\[
K\mathbf1=0,
\qquad
K^T\mathbf1=0,
\qquad
K=PKP.
\tag{23}
\]

Schatten duality therefore gives

\[
|\mathcal C_F(B)|
=|\operatorname{tr}((B^\circ)^T K)|
\le
\|B^\circ\|_*\|K\|_{\rm op},
\tag{24}
\]

again yielding `(11)`. The actual first-exit coefficient matrices are real and nonnegative; for complex `B`, the same estimate follows by applying trace duality to the entrywise conjugate matrix.

## Relation to MC-503 and MC-504

For one factorized profile class,

\[
B=a b^T.
\tag{25}
\]

Then

\[
B^\circ=(Pa)(Pb)^T
\tag{26}
\]

and therefore

\[
\|B^\circ\|_*
=
\|Pa\|_2\,\|Pb\|_2.
\tag{27}
\]

So `(11)` gives

\[
|\mathcal C_F(B)|
\le
C\sqrt p\,\|Pa\|_2\|Pb\|_2,
\tag{28}
\]

which sharpens the uncentered `sqrt(p)||a||_2||b||_2` tariff of `MC-503`: constant marginal mass is proved irrelevant rather than paid for.

More generally, any profile-class representation used in `MC-504`,

\[
B=\sum_c a_c b_c^T,
\tag{29}
\]

obeys

\[
\|B^\circ\|_*
\le
\sum_c\|Pa_c\|_2\|Pb_c\|_2
\le
\sum_c\|a_c\|_2\|b_c\|_2.
\tag{30}
\]

The nuclear norm is the infimum of the rank-one projective cost over all such decompositions. Therefore `(11)` is never weaker than paying the classwise triangle inequality in `MC-504`, and it removes dependence on an arbitrary choice of profile partition.

The matched-diagonal bound `(7)` can be stronger still: it discards every Fourier mode of `B` transverse to the diagonal `frequency(start)=frequency(offset)`. The actual arithmetic problem can therefore be narrowed further to estimating either this matched-diagonal `l^1` mass directly or, more conservatively, the centered nuclear norm.

## What changes in the current decisive test

The current branch should no longer ask first how many distinct hard-mask profiles occur or whether each profile separately has large start participation. Those quantities remain useful sufficient controls, but they are representation dependent.

For an actual repeated-residue cross-root block, form its physical nonnegative table `B_{x,j}` after all first-exit and sieve restrictions. Then test, in order:

1. the matched Fourier diagonal `d_k(B)` for `k!=0`;
2. when direct control is unavailable, the centered interaction norm `||PBP||_*`;
3. only as an upper bound on that norm, a convenient profile-class factorization such as the one used in `MC-504`.

This separates two failure modes that were previously conflated. A source may have many profile classes and broad marginals yet still have very small centered interaction; conversely, broad start/profile supports do not help if their coupled interaction remains low-participation after centering.

## Prior art and novelty boundary

The linear-algebra ingredients are standard: finite Fourier diagonalization of circulant matrices, Schatten `S_1`/operator-norm duality, unitary invariance of nuclear norm, and the projective rank-one characterization of the nuclear norm. Large-sieve arguments are routinely expressible as operator-norm estimates, and `MC-503`/`MC-504` already use the corresponding Fourier/Parseval viewpoint.

No general novelty is claimed for any of these facts. The durable Mathia contribution is their exact specialization to the first-exit varying-profile coefficient table, together with the observation that centering removes both marginals and that the quadratic-character kernel probes only the matched Fourier diagonal. This replaces the profile-class bookkeeping of `MC-504` by a canonical interaction object.

## Boundaries and failure modes

- `(11)` is an upper-bound certificate. A large nuclear norm does not imply a large character bias because the matched Fourier diagonal can still cancel against `Fhat(k)`.
- Small `||PBP||_*` proves small bias for this square-root-multiplier kernel, but the current work has not shown that the physical first-exit matrices enjoy such a bound.
- Raw marginal dispersion is insufficient. `PBP` deliberately deletes information that the centered character kernel cannot see.
- The theorem is conductor-local. Summing over many conductors or source roots may introduce additional outer weights and interference that must be audited separately.
- Lower-prime hard-mask arithmetic is not erased: it determines the entries of `B`. The result only identifies the quotient of that arithmetic visible to the current character correlation.
- Replacing the square-root Fourier multiplier by a stronger arithmetic estimate would change the tariff. The present result does not manufacture such an estimate.
- The matched-diagonal reduction must be applied after the exact physical first-exit reconstruction; using an artificial or relaxed coefficient table can give a misleadingly favorable interaction norm.

## Consequence

The immediate frontier is now precise and decomposition independent: determine the centered matched-diagonal Fourier mass, or at least the nuclear interaction norm, of the actual repeated-residue first-exit source matrix. If the physical sieve geometry forces that interaction participation above the conductor scale, the current character certificate yields genuine cancellation. If not, the obstruction is no longer merely “too few profile classes” or “too few starts”; it is concentration in the exact start-profile interaction channel seen by the quadratic-character kernel.