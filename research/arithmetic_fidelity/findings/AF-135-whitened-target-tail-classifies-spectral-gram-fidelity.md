# AF-135 — Whitened target tails exactly classify spectral Gram fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `TARGET-RELATIVE`, `STABILITY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a Hilbert space, let `psi_1,...,psi_m in H`, and define the synthesis map

\[
A:\mathbb C^m\to H,
\qquad
Aa=\sum_{j=1}^m a_j\psi_j.
\]

For a fixed target `k in H`, write

\[
G=A^*A,
\qquad
b=A^*k,
\qquad
\kappa=\|k\|^2.
\tag{1}
\]

Then the generator Gram matrix `G` alone does not determine the target-relative approximation distance. The exact missing datum is target alignment with the source span. More precisely:

1. `b` automatically lies in `ran(G)`, and
   \[
   \boxed{
   d^2:=\operatorname{dist}(k,\operatorname{ran}A)^2
   =\kappa-b^*G^\dagger b.
   }
   \tag{2}
   \]
   Thus `(G,b,kappa)` is exactly sufficient for this finite target-distance observable.

2. Let `E_B=1_B(G)` denote the spectral projector of `G` for a Borel set `B subset (0,infty)`. Define the **whitened target spectral measure**
   \[
   \mu_{G,b}(B)
   :=\left\|E_B G^{\dagger/2}b\right\|^2.
   \tag{3}
   \]
   Its total mass is the squared projection energy:
   \[
   \mu_{G,b}((0,\infty))=b^*G^\dagger b=\|P_{\operatorname{ran}A}k\|^2.
   \tag{4}
   \]

3. If a spectral Gram compression retains only modes with eigenvalue at least `tau>0`, its target-distance estimate is
   \[
   d_\tau^2
   :=\kappa-\left\|E_{[\tau,\infty)}G^{\dagger/2}b\right\|^2.
   \tag{5}
   \]
   The fidelity defect is exactly
   \[
   \boxed{
   d_\tau^2-d^2
   =\mu_{G,b}((0,\tau))
   =\left\|E_{(0,\tau)}G^{\dagger/2}b\right\|^2.
   }
   \tag{6}
   \]
   Therefore, for any family `(G_n,b_n,kappa_n)` and cutoff schedule `tau_n`, spectral truncation preserves the exact target distance asymptotically iff the discarded whitened target mass tends to zero:
   \[
   \boxed{
   \mu_{G_n,b_n}((0,\tau_n))\longrightarrow0.
   }
   \tag{7}
   \]
   This is a target-relative discrete-Picard condition: small eigenvalues are harmless exactly when the target has sufficiently little **whitened** mass in those modes.

4. Raw Euclidean smallness of discarded target pairings is not a uniform stability criterion. There are same-Gram controls with pairing discrepancy tending to zero but order-one target-distance discrepancy. The natural fixed-`G` perturbation metric is
   \[
   \delta_G(b,b')
   :=\left\|G^{\dagger/2}(b-b')\right\|.
   \tag{8}
   \]
   For feasible targets of the same norm `kappa`,
   \[
   \boxed{
   |d^2(b)-d^2(b')|
   \le 2\sqrt{\kappa}\,\delta_G(b,b').
   }
   \tag{9}
   \]
   The modulus is independent of the condition number because the conditioning has been placed explicitly into the data metric.

The theorem is relative to a **declared coefficient Hilbert geometry** on `C^m`. Unitary changes of generator coordinates preserve `(3)`–`(7)`, but arbitrary invertible reparameterizations need not preserve Gram eigenvalues or spectral cutoffs. A claimed spectral certificate must therefore justify its generator normalization/coefficient metric independently rather than treating the span alone as sufficient structure.

## Derivation

### The target pairing is the missing finite Gram mark

Because

\[
\ker(A^*A)=\ker A,
\]

finite-dimensional orthogonal-complement identities give

\[
\operatorname{ran}(G)
=(\ker G)^\perp
=(\ker A)^\perp
=\operatorname{ran}(A^*).
\tag{10}
\]

Hence `b=A^*k in ran(G)`. The minimum-norm coefficient vector whose synthesis equals the orthogonal projection of `k` onto `ran(A)` is

\[
a_*=G^\dagger b.
\tag{11}
\]

Indeed, the normal equations are `Ga=b`, and

\[
\|Aa_*\|^2
=a_*^*Ga_*
=b^*G^\dagger b.
\tag{12}
\]

Orthogonal Pythagoras then gives `(2)`. Equivalently, the augmented Gram matrix

\[
\begin{pmatrix}
G & b\\
b^* & \kappa
\end{pmatrix}
\tag{13}
\]

is positive semidefinite, and `d^2` is its generalized Schur complement with respect to `G`.

### Spectral truncation loses exactly the whitened target tail

Let

\[
G=\sum_{\lambda>0}\lambda E_{\{\lambda\}}
\tag{14}
\]

on its active range. Then

\[
b^*G^\dagger b
=\sum_{\lambda>0}
\frac{\|E_{\{\lambda\}}b\|^2}{\lambda}.
\tag{15}
\]

This is exactly the total mass of `(3)`. Splitting `(15)` at `tau` yields

\[
b^*G^\dagger b
=
\left\|E_{[\tau,\infty)}G^{\dagger/2}b\right\|^2
+
\left\|E_{(0,\tau)}G^{\dagger/2}b\right\|^2,
\tag{16}
\]

so `(6)` follows immediately from `(2)` and `(5)`. Because the defect in `(6)` is nonnegative and exact, `(7)` is both necessary and sufficient; no condition-number upper bound is needed once the target-weighted tail itself is controlled.

In an eigenbasis with `Gv_j=lambda_j v_j` and `beta_j=v_j^*b`, the criterion is simply

\[
d_\tau^2-d^2
=
\sum_{0<\lambda_j<\tau}
\frac{|\beta_j|^2}{\lambda_j}.
\tag{17}
\]

The important quantity is therefore not `|beta_j|` by itself but `|beta_j|/sqrt(lambda_j)`, the target coordinate after whitening the source geometry.

### Raw pairings can converge while the target distance does not

Fix `0<c<1` and let

\[
G_\varepsilon=
\begin{pmatrix}
1&0\\
0&\varepsilon
\end{pmatrix},
\qquad
\kappa=1.
\tag{18}
\]

Compare the feasible target-pairing vectors

\[
b_\varepsilon^{(0)}=(0,0)^T,
\qquad
b_\varepsilon^{(1)}=(0,c\sqrt{\varepsilon})^T.
\tag{19}
\]

They satisfy

\[
\|b_\varepsilon^{(1)}-b_\varepsilon^{(0)}\|
=c\sqrt{\varepsilon}\to0,
\tag{20}
\]

but

\[
(b_\varepsilon^{(1)})^*G_\varepsilon^{-1}b_\varepsilon^{(1)}=c^2.
\tag{21}
\]

Thus their squared target distances are `1` and `1-c^2`: an order-one difference survives while the raw pairing discrepancy vanishes. The augmented Gram matrices remain positive semidefinite because their generalized Schur complements are `1` and `1-c^2`.

This kills any proposed uniform recovery modulus based only on the unweighted Euclidean norm of discarded `b` when arbitrarily small positive Gram eigenvalues are allowed.

### Whitening gives the exact robust geometry

For fixed `G`, put

\[
c=G^{\dagger/2}b,
\qquad
c'=G^{\dagger/2}b'.
\]

Then the recovered projection energies are `q(b)=||c||^2` and `q(b')=||c'||^2`. If both augmented Gram matrices are feasible with the same target norm `kappa`, then `||c||,||c'||<=sqrt(kappa)`. Therefore

\[
|q(b)-q(b')|
\le(\|c\|+\|c'\|)\|c-c'\|
\le2\sqrt{\kappa}\,\delta_G(b,b'),
\tag{22}
\]

which proves `(9)` because `d^2=kappa-q`.

For unsquared distances, the universal consequence is the weaker Hölder estimate

\[
|d(b)-d(b')|
\le\sqrt{2\sqrt{\kappa}\,\delta_G(b,b')}.
\tag{23}
\]

If both distances are bounded below by `d_0>0`, division by `d(b)+d(b')>=2d_0` improves this to

\[
|d(b)-d(b')|
\le\frac{\sqrt{\kappa}}{d_0}\,\delta_G(b,b').
\tag{24}
\]

Thus the apparent singular conditioning is not mysterious: it is exactly the mismatch between raw coefficient-space error and the inverse-Gram geometry relevant to the target observable.

## What is and is not a useful lift

For the single scalar observable `d^2`, storing

\[
q=b^*G^\dagger b
\]

alongside `kappa` is mathematically sufficient. But this is essentially storing the target projection energy itself, so it is not evidence for a source-natural explanatory lift. Likewise, retaining the full vector `b` is exact but may preserve substantially more target-specific information than a compressed certificate is intended to carry.

The spectral measure `(3)` is useful diagnostically because it exposes **where** the target information sits relative to the compression geometry. A spectral truncation can discard many coefficient directions and still be faithful precisely when their whitened target mass is negligible. Conversely, a numerically tiny raw pairing on a small-eigenvalue direction can remain decisively important after whitening.

This gives a concrete audit hierarchy for target-relative Gram compression:

- `G` alone: source-source geometry only; no target-distance sufficiency in general;
- `(G,b,kappa)`: exact finite sufficiency;
- spectral truncation of `b`: exact defect given by `(6)`;
- raw-norm truncation claims without a Picard-type weighted tail bound: no uniform stability.

## Coordinate boundary

If the generators are changed by a unitary coefficient transformation `U`, then

\[
A'=AU,
\qquad
G'=U^*GU,
\qquad
b'=U^*b,
\tag{25}
\]

and the measure `(3)` is unchanged under the corresponding identification. Thus the criterion is intrinsic to the synthesis operator together with its coefficient Hilbert metric.

For a general invertible but nonunitary change of coordinates, Gram eigenvalues and the thresholded spectral split can change. Consequently a spectral cutoff is **not** an invariant of the abstract span `ran(A)` alone. Any application must specify why its coefficient metric, generator weights, or admissible coordinate changes are canonical enough for the truncation to have mathematical meaning.

## Prior art and novelty assessment

No novelty claim is made for the projection formula, pseudoinverse, generalized Schur complement, truncated SVD, or Picard condition.

- Adi Ben-Israel and Thomas N. E. Greville, ***Generalized Inverses: Theory and Applications***, 2nd ed., Springer (2003), DOI `10.1007/b97366`. Role: standard Moore-Penrose pseudoinverse and least-squares/projection theory underlying `(2)` and `(11)`–`(12)`.
- Fuzhen Zhang (ed.), ***The Schur Complement and Its Applications***, Numerical Methods and Algorithms 4, Springer (2005), DOI `10.1007/b105056`. Role: standard generalized Schur-complement and positive-semidefinite block-matrix framework for `(13)`.
- Per Christian Hansen, **“Truncated Singular Value Decomposition Solutions to Discrete Ill-Posed Problems with Ill-Determined Numerical Rank,”** *SIAM Journal on Scientific and Statistical Computing* 11(3), 503–518 (1990), DOI `10.1137/0911028`. Role: classical TSVD regularization and the fact that stable truncation depends jointly on singular values and right-hand-side coefficients through a discrete Picard condition.
- Per Christian Hansen, **“The Discrete Picard Condition for Discrete Ill-Posed Problems,”** *BIT* 30, 658–672 (1990). Role: direct prior art for weighting data coefficients relative to small singular values rather than judging them in an unweighted norm.
- Luis Báez-Duarte, **“New versions of the Nyman-Beurling criterion for the Riemann hypothesis,”** *International Journal of Mathematics and Mathematical Sciences* 31(7), 387–406 (2002), DOI `10.1155/S0161171202013248`. Role: authoritative Hilbert-space approximation context for the eventual Nyman application; AF-135 does not claim any new Nyman-Beurling theorem.

The ingredients are classical. The Arithmetic Fidelity contribution is the **exact target-relative compression audit** `(3)`–`(9)`: it identifies the discarded whitened target mass as the complete fidelity defect for spectral Gram truncation and separates exact finite sufficiency from asymptotic robustness. This is organizational/diagnostic mathematics unless a later application proves a nontrivial family-specific tail estimate or obstruction.

## Consequences for the Nyman target-recovery clue

The abstract part of `CLUE-nyman-target-recovery-profile` is now settled sharply. Full target pairings recover the finite distance through `(2)`; spectral truncation has the exact error `(6)`; and raw smallness of discarded pairings is insufficient by `(18)`–`(21)`.

What remains is genuinely Nyman-specific and is **not** proved here. For a canonically normalized finite Nyman family one must:

1. justify the coefficient Hilbert geometry/admissible coordinate class in which Gram spectral truncation is intrinsic enough to be meaningful;
2. compute or estimate the actual whitened target measure `mu_{G_n,b_n}`;
3. prove or refute a natural cutoff schedule with
   \[
   \mu_{G_n,b_n}((0,\tau_n))\to0;
   \]
4. determine whether any such retained target profile is materially smaller than simply carrying the full target pairing vector.

Until those arithmetic estimates exist, AF-135 gives a **fidelity gate**, not an RH consequence or approximation-rate theorem.