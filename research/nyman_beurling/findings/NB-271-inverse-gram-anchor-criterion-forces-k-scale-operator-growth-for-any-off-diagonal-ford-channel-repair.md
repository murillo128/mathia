# NB-271 — Inverse-Gram anchor criterion forces `K`-scale operator growth for any off-diagonal Ford-channel repair

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + GENERAL-PSD-GRAM-CRITERION + MOORE-PENROSE-ANCHOR-MINIMIZER + OFF-DIAGONAL-COERCIVITY-CLASSIFICATION + H2-DOMINATION-NO-GO + K-SCALE-OPERATOR-GROWTH + SUMMABLE-ROW-DECAY-NO-GO + BANDWIDTH-LOWER-BOUND + NB-269-270-REFINEMENT + DESTINATION-METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-269` shows that, on the resolved multi-shell Ford channel, the canonical full-line Hardy energy is equivalent to an unweighted `ell^2` norm of the shell coefficients and can be only `Theta(1/K)` on the Euler-normalized uniform carrier. `NB-270` then gives the exact threshold for every **diagonal** repair: a shell weight `q_j` produces rank-uniform anchor coercivity exactly when `sum_j q_j^{-1}` stays bounded.

The remaining loophole in `NB-270` was a genuinely off-diagonal positive Gram form. For that entire finite-rank class there is again an exact answer. If `A_K >= 0` is the Hermitian matrix of a positive quadratic form

\[
Q_K(c)=c^*A_Kc,
\qquad
\mathbf 1^*c=1,
\]

then its optimal Euler-anchor coercivity is determined by the inverse Gram response to the all-ones vector. When `\mathbf 1` lies in the range of `A_K`,

\[
\boxed{
\inf_{\mathbf 1^*c=1}Q_K(c)
=
\frac{1}{\mathbf 1^*A_K^\dagger\mathbf 1}.
}
\]

If the nullspace of `A_K` has any component visible to the anchor, the infimum is exactly zero. Thus the diagonal reciprocal-summability theorem of `NB-270` is only the diagonal specialization of a more general inverse-Gram criterion.

The criterion has a sharp consequence for the route left open by `NB-270`: **no positive quadratic form that is uniformly bounded by the same canonical Hardy norm can restore rank-uniform coercivity.** Indeed, the uniform anchored vector

\[
u_K=\frac1K(1,\ldots,1)
\]

has `||u_K||_2^2=1/K`. Hence for every positive `A_K`,

\[
\boxed{
\eta_K:=\inf_{\mathbf 1^*c=1}c^*A_Kc
\le
u_K^*A_Ku_K
\le
\frac{\|A_K\|_{\rm op}}{K}.
}
\]

Therefore a rank-uniform floor `eta_K >= eta > 0` forces

\[
\boxed{
\|A_K\|_{\rm op}\ge \eta K.
}
\]

After the `NB-269` resolved-shell Hardy normalization this says that any successful off-diagonal repair must become at least `Theta(K)` stronger than the ordinary projected `H^2` norm in an anchor-relevant direction. Uniformly bounded perturbations, finite-range Gram corrections, and uniformly summable off-diagonal kernels cannot do it.

---

## 1. Resolved Ford-channel normalization

Use the same resolved `H`-spaced shell family as `NB-269` and `NB-270`, with

\[
J=mK,
\qquad
m\to\infty,
\qquad
K\to\infty,
\]

and disjoint normalized frequency bands

\[
j+\operatorname{supp}\phi,
\qquad
0\le j<K.
\]

For a shell coefficient vector `c=(c_0,\ldots,c_{K-1})`, the exact full-line projected current from `NB-269` satisfies

\[
\mathcal H_{J,K}(c)
:=
\int_{\mathbb R}|G_J^{(c)}(z)|^2\,dz
=
\sum_{j=0}^{K-1}r_{j,J}|c_j|^2,
\]

where

\[
r_{j,J}
=
2\pi\int_a^b|\phi(u)|^2|A_{j,J}(u)|^2\,du.
\]

On the live shallow matched packet, the channel amplitudes of `NB-269` obey uniform two-sided bounds, so there are constants independent of `J,K,j` such that

\[
0<r_-\le r_{j,J}\le r_+<\infty.
\]

Consequently

\[
r_-\|c\|_2^2
\le
\mathcal H_{J,K}(c)
\le
r_+\|c\|_2^2.
\tag{1}
\]

The Euler normalization remains

\[
\boxed{\mathbf 1^*c=\sum_{j=0}^{K-1}c_j=1.}
\tag{2}
\]

`NB-269` already used the particular choice `u_K=K^{-1}\mathbf 1` to obtain `\mathcal H_{J,K}(u_K)=Theta(1/K)`. The question here is whether another **positive quadratic destination quantity**, perhaps with substantial off-diagonal coupling between the resolved bands, can be both controlled by the exact Nyman/Hardy geometry and uniformly coercive on (2).

---

## 2. Exact inverse-Gram anchor theorem

Let `A=A^*>=0` be any `K x K` Hermitian positive-semidefinite matrix and define

\[
Q_A(c)=c^*Ac.
\]

Write `e=\mathbf 1`. There are exactly two cases.

### 2.1 Anchor-visible nullspace

If

\[
P_{\ker A}e\ne0,
\]

then take `v=P_{\ker A}e`. Since

\[
e^*v=\|v\|_2^2>0,
\]

the vector

\[
c=\frac{v}{e^*v}
\]

satisfies `e^*c=1` and `Ac=0`. Therefore

\[
\boxed{
\inf_{e^*c=1}Q_A(c)=0.
}
\tag{3}
\]

So any positive Gram form whose nullspace is visible to the Euler anchor fails immediately.

### 2.2 Anchor contained in the Gram range

Suppose instead

\[
e\perp\ker A.
\]

Because `A` is Hermitian in finite dimension, this is equivalent to `e in ran A`. Let `A^\dagger` denote the Moore-Penrose pseudoinverse. For every anchored `c`,

\[
1
=|e^*c|
=
\left|
(A^{\dagger/2}e)^*A^{1/2}c
\right|.
\]

Cauchy-Schwarz gives

\[
1
\le
(e^*A^\dagger e)^{1/2}
(c^*Ac)^{1/2},
\]

hence

\[
Q_A(c)
\ge
\frac1{e^*A^\dagger e}.
\tag{4}
\]

Equality is attained by

\[
\boxed{
c_*
=
\frac{A^\dagger e}{e^*A^\dagger e},}
\tag{5}
\]

because `AA^\dagger e=e`. Therefore

\[
\boxed{
\inf_{e^*c=1}c^*Ac
=
\frac1{e^*A^\dagger e}.
}
\tag{6}
\]

Equations (3) and (6) completely classify positive quadratic anchor coercivity at every finite rank. In particular, a sequence `A_K` has a rank-uniform positive lower bound on the Euler hyperplane if and only if the anchor never sees the nullspace and

\[
\boxed{
\sup_K e_K^*A_K^\dagger e_K<\infty.
}
\tag{7}
\]

This is the exact off-diagonal analogue of reciprocal-weight summability.

---

## 3. `NB-270` is the diagonal specialization

For

\[
A_K=\operatorname{diag}(q_0,\ldots,q_{K-1}),
\qquad q_j>0,
\]

we have

\[
e^*A_K^{-1}e
=
\sum_{j=0}^{K-1}\frac1{q_j}.
\]

Thus (6) becomes exactly the theorem of `NB-270`:

\[
\inf_{\sum c_j=1}
\sum_jq_j|c_j|^2
=
\left(\sum_jq_j^{-1}\right)^{-1}.
\]

The advantage of (6) is that it identifies what an off-diagonal rescue would actually have to accomplish. It is not enough for `A_K` to have many nonzero cross terms or a favorable spectrum in directions unrelated to the anchor. The **inverse** Gram seen by `e_K` must remain bounded:

\[
e_K^*A_K^\dagger e_K=O(1).
\]

This is an anchor-alignment condition, not merely a lower bound on average eigenvalues.

---

## 4. Uniform Hardy domination rules out every such repair

Let

\[
R_{J,K}=\operatorname{diag}(r_{0,J},\ldots,r_{K-1,J}),
\]

so that the canonical projected Hardy energy is

\[
\mathcal H_{J,K}(c)=c^*R_{J,K}c.
\]

Suppose a proposed positive quadratic invariant `Q_K(c)=c^*A_Kc` is uniformly controlled by this same channel norm:

\[
\boxed{
Q_K(c)
\le
C\,\mathcal H_{J,K}(c)
\quad\text{for every }c,
}
\tag{8}
\]

with `C` independent of `J,K`. This is the natural comparison one would need if `Q_K` were to be inserted as a lower-bound certificate extracted from the same Hardy-projected Ford channel.

Testing (8) on the uniform anchor `u_K=e_K/K` and using (1),

\[
\inf_{e^*c=1}Q_K(c)
\le
Q_K(u_K)
\le
C\mathcal H_{J,K}(u_K)
\le
\frac{Cr_+}{K}.
\tag{9}
\]

Hence

\[
\boxed{
\inf_{e^*c=1}Q_K(c)=O(1/K).
}
\tag{10}
\]

No off-diagonal arrangement can change this conclusion while (8) holds uniformly.

Equivalently, if `Q_K` has a uniform anchor floor

\[
Q_K(c)\ge\eta>0
\qquad
(e^*c=1),
\]

then its generalized operator norm relative to the Hardy metric,

\[
\Lambda_K
:=
\left\|
R_{J,K}^{-1/2}A_KR_{J,K}^{-1/2}
\right\|_{\rm op},
\]

must satisfy

\[
\boxed{
\Lambda_K\ge \frac{\eta}{r_+}K.
}
\tag{11}
\]

Thus **`Theta(K)` relative growth is necessary** for any positive quadratic repair living on these same resolved shell coordinates.

The scale is sharp as an abstract statement. The rank-one matrix

\[
A_K=e_Ke_K^*
\]

has

\[
Q_K(c)=|e_K^*c|^2=1
\]

on the anchor hyperplane and

\[
\|A_K\|_{\rm op}=K.
\]

So the theorem does not say off-diagonal coercivity is algebraically impossible. It says that restoring it requires a **macroscopically coherent, rank-growing coupling**, not a bounded correction to the ordinary Hardy Gram.

---

## 5. Local and summably decaying off-diagonal kernels also leak

The operator-growth condition gives a useful structural filter before computing any detailed Nyman Gram matrix.

Let

\[
A_K=(a_{jk})_{0\le j,k<K}
\]

be Hermitian positive semidefinite. If its absolute row sums obey

\[
\sup_{K}\sup_j\sum_{k<K}|a_{jk}|\le M<\infty,
\tag{12}
\]

then Hermitian symmetry gives the same column bound, and the elementary Schur matrix estimate yields

\[
\|A_K\|_{\rm op}\le M.
\]

Equation (9) therefore gives

\[
\boxed{
\inf_{e^*c=1}c^*A_Kc
\le
\frac{M}{K}
\to0.
}
\tag{13}
\]

So any off-diagonal Gram structure with uniformly summable rows is automatically too local to repair the `NB-269` leak.

For example, if

\[
|a_{jk}|
\le
C(1+|j-k|)^{-p},
\]

then:

- for `p>1`, the row sum is `O(1)` and the anchor floor is `O(1/K)`;
- for `p=1`, the row sum is `O(log K)` and the floor is at most `O((log K)/K)`;
- for `0<p<1`, the row sum is `O(K^{1-p})` and the floor is at most `O(K^{-p})`.

Every positive power of off-diagonal decay still leaks. A uniformly bounded-entry kernel needs correlations extending across `Theta(K)` shell separation, with non-summable total row mass, before an order-one floor is even possible.

Likewise, if `A_K` has bandwidth `B_K` and `|a_{jk}|<=C`, then

\[
\|A_K\|_{\rm op}=O(B_K)
\]

and therefore

\[
\boxed{
\inf_{e^*c=1}Q_K(c)
=O(B_K/K).
}
\tag{14}
\]

A rank-uniform floor requires `B_K=Omega(K)` unless the matrix entries themselves grow. Thus a fixed-band, polylog-band, or any `o(K)`-band positive Gram correction cannot be the missing destination bridge.

This substantially narrows the phrase “genuinely off-diagonal structure” left open by `NB-270`: the missing structure, if it exists on the resolved Ford channel, must be **global in rank or unbounded in amplitude**.

---

## 6. Relation to `NB-269` and the full Nyman target

There is no contradiction with `NB-269`. That finding already proves directly that the exact local hard-window Hardy form of the explicit uniform resolved carrier is `Theta(1/K)`. The present theorem abstracts the reason and identifies the strongest possible class of positive quadratic repairs that can be discarded without another detailed projection calculation.

Nor does this finding prove that the complete Nyman-Beurling distance leaks. The distinction is essential. The matrix `A_K` here acts on the **same resolved projected Ford-channel coefficients**. The full Nyman residual may contain additional components, target cross terms, global arithmetic constraints, or another exact invariant not uniformly controlled by this channel's `H^2` norm. Any of those could lie outside assumption (8).

The result therefore converts the surviving route into a more precise dichotomy:

1. if the missing destination quantity is a uniformly `H^2`-continuous positive quadratic observable of the resolved Ford channel, it cannot restore rank-uniform coercivity;
2. if a positive off-diagonal form does restore coercivity, its strength relative to the canonical channel norm must grow at least linearly in `K`, and its inverse Gram must remain uniformly controlled in the anchor direction.

The second possibility is not ruled out, but it is now a sharply testable property of any proposed exact Nyman Gram form.

---

## 7. Adversarial audit

### 7.1 The operator-norm condition is necessary, not sufficient

Large `||A_K||_op` alone does not imply anchor coercivity. A matrix may have an eigenvalue of size `K` entirely in a direction orthogonal to `e_K` and still have an anchored null direction. The exact condition is (3)/(7), namely the behavior of `A_K^\dagger` against the anchor.

The `Omega(K)` growth in (11) is therefore only a quick rejection test. Passing it does not establish a usable destination invariant.

### 7.2 Positivity is essential

The theorem classifies positive semidefinite quadratic forms. An indefinite sesquilinear identity may contain large cancellations and need not be bounded by the same argument. To turn such an identity into a lower bound for a norm, however, one eventually needs a positive or otherwise coercive quantity; the present statement deliberately stops before claiming that every possible nonpositive identity is irrelevant.

### 7.3 The comparison must be rank-uniform

A bound

\[
Q_K\le C_K\mathcal H_{J,K}
\]

with `C_K` growing like `K` is fully compatible with uniform anchor coercivity. The theorem rules out only a **uniform** Hardy-dominated repair and quantifies the exact growth any nonuniform comparison must pay.

### 7.4 This is not a theorem about the actual zeta zero set

No new zero configuration is asserted. The resolved Ford packet remains the matched compatibility control inherited from `NB-269`; it is used to test which destination mechanisms could possibly convert that control into a rank-uniform lower bound.

### 7.5 The rank-one control is intentionally circular as a Nyman invariant

`A_K=e_Ke_K^*` shows sharpness of the `K` operator scale, but it simply squares the Euler anchor itself. It is not proposed as a new Nyman lower bound. Its role is only to show that the abstract growth threshold cannot be improved without using more structure.

---

## 8. Prior-art and source audit

A fresh targeted search found the general Moore-Penrose constrained-quadratic minimization framework in Dimitrios Pappas, *Minimization of Constrained Quadratic Forms in Hilbert Spaces* (arXiv:1003.5676, 2010). That is the natural generic functional-analytic home of (6). The finite-dimensional identity needed here is proved directly above, so no external theorem is load-bearing.

The search also reconfirmed Hugh Carvill's 2025 preprint *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing* (arXiv:2510.18132), which proves polynomial off-diagonal decay and block-compressibility for a different Beurling-Nyman ladder Gram geometry. It does **not** identify the resolved Ford-channel matrix studied here, so its decay theorem cannot simply be imported into (13). It is nevertheless conceptually relevant: the present calculation shows that a uniformly summable off-diagonal decay pattern, if it occurred in the live resolved Ford destination Gram, would be too weak to restore rank-uniform anchor coercivity.

The new content of this finding is therefore not the generic pseudoinverse formula by itself. It is its application to the `NB-269` resolved Hardy normalization and the resulting destination boundary: **any successful positive off-diagonal repair must have `K`-scale relative operator growth and anchor-aligned inverse-Gram coercivity; uniformly summable or sublinear-band coupling cannot suffice.** No new external source is load-bearing, so `SOURCES.md` does not need an update.

---

## 9. Next discriminating question

`NB-270` left “genuinely off-diagonal structure” as an open class. The present theorem shows that most benign off-diagonal structures are already excluded. The next useful calculation should therefore not try another arbitrary Toeplitz kernel or modest cross-shell correction.

Instead, derive the coefficient-space Gram matrix of the **complete admissible Nyman residual**, or of the smallest exact destination component not already contained in the `NB-269` projected Ford current, and test two quantities:

\[
\left\|
R_{J,K}^{-1/2}A_KR_{J,K}^{-1/2}
\right\|_{\rm op}
\]

and

\[
e_K^*A_K^\dagger e_K.
\]

If the first remains `o(K)`, rank-uniform positive coercivity is impossible immediately. If it reaches `Theta(K)` or larger, the second quantity decides whether that growth is actually aligned with the Euler anchor or is spectrally irrelevant.

This gives a substantially sharper destination-side test than “look for off-diagonal terms.” The missing Nyman bridge must exhibit **macroscopic shell coherence tied specifically to the anchor direction**, or else it must come from structure outside the resolved Ford channel altogether.

## Conclusion

The diagonal threshold of `NB-270` extends exactly to arbitrary positive Gram forms: the anchor floor is the reciprocal of the inverse-Gram mass seen by the all-ones vector. On the resolved Ford channel, the canonical Hardy metric is uniformly equivalent to `ell^2`, so the uniform anchored carrier has norm squared `Theta(1/K)`. Consequently no uniformly Hardy-dominated positive quadratic observable—diagonal or off-diagonal—can turn that channel into an order-one obstruction.

A successful off-diagonal repair must pay at least `Theta(K)` in relative operator strength and must place that strength in the anchor direction. In particular, uniformly summable off-diagonal decay and every `o(K)`-band bounded Gram correction are now ruled out as destination bridges. The live question has moved from the existence of cross terms to whether the **full Nyman target contains a genuinely rank-global, anchor-aligned coupling that is absent from the local projected Ford channel**.