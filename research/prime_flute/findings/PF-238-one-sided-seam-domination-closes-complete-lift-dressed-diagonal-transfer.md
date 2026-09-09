# PF-238 — one-sided seam domination closes the complete-lift dressed diagonal transfer

**Status:** `EXACT-DERIVED + ONE-SIDED-FORM-DOMINATION + NONCOMMUTATIVE-BLOCK-FACTORIZATION + SINGULAR-VALUE-ENVELOPE + POSITIVE/ROUTE-NARROWING`. PF-237 proves that the complete lifted actual PF-205 seam and the PF-236 operator-matched seam cannot be two-sided form-comparable: the former has noncompact inverse while the latter has compact inverse. The missing observation is that the **opposite one-sided order is true and is already sufficient for the normalized crossing estimate**. Endpoint escape makes the actual seam softer than the matched confining seam; it does not make it larger.

On the exact PF-233 diagonal neighboring-cuff corridor, let

\[
B=M_{a^{-1}},\qquad T_a\ge c_0s^2A,
\qquad A=-\partial_\theta^2+\csc^2\theta,
\qquad K=T_a^{1/2},
\]

and put

\[
r_i=\frac{w_i}{s},\qquad
q_i^{\rm mat}=K\tanh(r_iK),\qquad
Q_i^{\rm mat}=B^{1/2}q_i^{\rm mat}B^{1/2}.
\]

Let `Q_i^{act}` denote the **complete lifted actual symmetric seam form** after [[research/prime_flute/findings/PF-235-hypercycle-boundary-compactification-has-only-quadratic-prime-dependent-defect|PF-235]]'s exact hypercycle transport and the density-corrected fixed `tau<->theta` compactification used in [[research/prime_flute/findings/PF-237-complete-lift-seam-spectral-type-blocks-direct-matched-normalizer-comparison|PF-237]]. Then

\[
\boxed{
Q_i^{\rm act}\le_{\rm form} C_i Q_i^{\rm mat},
\qquad
C_i=2\cosh^3\rho_i\frac{C_\delta}{c_0},
}
\tag{1}
\]

where

\[
C_\delta=\max\{2,1+2\delta^2\},
\qquad
\delta=\left\|\frac{a'}{2a}\right\|_\infty,
\qquad
c_0=\frac{(1-\eta)^2}{C_\delta}.
\tag{2}
\]

No reverse inequality is asserted; PF-237 proves that none can hold globally on the complete lift.

More importantly, if

\[
Q^{\rm act}=\operatorname{diag}(Q_1^{\rm act},Q_2^{\rm act}),
\qquad
D^{\rm act}
=\left(I+(Q^{\rm act})^{-1/2}\Lambda_a(Q^{\rm act})^{-1/2}\right)^{-1},
\tag{3}
\]

where `Lambda_a` is PF-233's exact diagonal corridor DtN matrix, then

\[
\boxed{
s_{m+1}(D^{\rm act}_{21})
\le
C_*\frac{\sqrt{w_1w_2}}s\,
F\!\left(\sqrt{c_0}\,s(m+\alpha)\right),
\qquad
F(z)=\frac z{\sinh z},
}
\tag{4}
\]

with

\[
\alpha=\frac{1+\sqrt5}{2},
\qquad
C_*=\sqrt{C_1C_2}
=2(\cosh\rho_1\cosh\rho_2)^{3/2}\frac{C_\delta}{c_0}.
\tag{5}
\]

PF-233 makes `c_0` and `C_delta` uniform on the canonical tail, while `cosh(rho_i)=1+O(w_i^2)`. Thus PF-238 preserves the **PF-236 amplitude currency, `O(s^{-1})` inverse-seam channel count, and exponential high-mode envelope up to one uniform constant**, now for the actual complete lifted seam rather than the operator-matched surrogate.

The proof needs no central/endpoint cutoff. It combines an exact compactification identity, variational one-sided DtN comparison, and a positive block-inverse factorization showing that normalized off-diagonal transfer is contractively dominated by a single off-diagonal block of `Q^{1/2}Lambda_a^{-1}Q^{1/2}`. That block contains the corridor factor `K^{-1}csch K`, which kills the endpoint escape exposed by PF-237.

## Claim

For a positive self-adjoint operator `X` and `h>0`, write

\[
f_h(X):=X^{1/2}\tanh(hX^{1/2}).
\tag{6}
\]

Let

\[
\tau=\log\tan\frac\theta2,
\qquad
U:L^2(\mathbb R,d\tau)\to L^2((0,\pi),d\theta),
\qquad
(U\phi)(\theta)=\sin^{-1/2}\theta\,\phi(\tau(\theta)),
\tag{7}
\]

and define

\[
L:=U(1-\partial_\tau^2)U^*.
\tag{8}
\]

Then:

1. on the natural closed form domain,
   \[
   \boxed{
   L=-\partial_\theta(\sin^2\theta\,\partial_\theta)
   +\frac34(1+\sin^2\theta),
   \qquad
   0<L\le_{\rm form}2A;
   }
   \tag{9}
   \]
2. for every `w>0`,
   \[
   \boxed{f_w(L)\le_{\rm form}2f_w(A);}
   \tag{10}
   \]
3. PF-235 and (10) imply
   \[
   Q_i^{\rm act}\le_{\rm form}
   2\cosh^3\rho_i\,f_{w_i}(A);
   \tag{11}
   \]
4. PF-233's lower bound on `T_a`, together with its boundary-mass factor, implies
   \[
   \boxed{
   Q_i^{\rm mat}\ge_{\rm form}
   \frac{c_0}{C_\delta}f_{w_i}(A),
   }
   \tag{12}
   \]
   proving (1);
5. more generally, if positive seam forms `Q_i` satisfy
   \[
   Q_i\le_{\rm form}C_iQ_i^{\rm mat},
   \tag{13}
   \]
   and `D` is defined as in (3) with `Q=diag(Q_1,Q_2)`, then the singular-value bound (4) holds with `C_*=sqrt(C_1C_2)`.

Taking `Q_i=Q_i^{act}` proves the actual-seam result.

## 1. The fixed compactification is controlled by the corridor transverse operator

The unitary (7) is forced by `d tau=csc(theta)d theta`. Writing

\[
\phi(\tau(\theta))=\sin^{1/2}\theta\,y(\theta),
\qquad
\partial_\tau=\sin\theta\,\partial_\theta,
\]

gives, first on `C_c^infinity(0,pi)` and then by closure,

\[
Ly=-\partial_\theta(\sin^2\theta\,y')
+\frac34(1+\sin^2\theta)y.
\tag{14}
\]

There is an exact comparison identity

\[
M_{\sin\theta}AM_{\sin\theta}
=-\partial_\theta(\sin^2\theta\,\partial_\theta)
+(1+\sin^2\theta),
\tag{15}
\]

so

\[
\boxed{
L=M_{\sin\theta}AM_{\sin\theta}
-\frac14(1+\sin^2\theta).
}
\tag{16}
\]

Positivity of `L` follows from its unitary definition. The form of the first term on the right is

\[
\int_0^\pi
\left[
\sin^2\theta|y'|^2
+(1+\sin^2\theta)|y|^2
\right]d\theta,
\tag{17}
\]

which is at most `2<y,Ay>` because `sin^2(theta)<=1` and `csc^2(theta)>=1`. This proves (9).

The symmetric product-strip DtN form has the variational representation

\[
\boxed{
\langle g,f_h(X)g\rangle
=\frac12
\inf_{\substack{u(-h)=g\\u(h)=g}}
\int_{-h}^h
\left(\|u_x\|^2+\|X^{1/2}u\|^2\right)dx.
}
\tag{18}
\]

Therefore form order of the transverse operator passes directly to the boundary form. From `L<=2A`,

\[
f_w(L)\le f_w(2A).
\]

Since both terms on the right are functions of `A`, the scalar inequality

\[
\sqrt2\tanh(\sqrt2 z)\le2\tanh z
\]

gives `f_w(2A)<=2f_w(A)`, proving (10).

PF-235 gives, before the fixed compactification,

\[
\widetilde Q_i^{\rm act}
\le_{\rm form}
\cosh^3\rho_i\,f_{w_i}(1-\partial_\tau^2).
\tag{19}
\]

Conjugating by `U` and applying (10) proves (11). Thus PF-237's translation escape is a **one-sided loss of coercivity**, not an uncontrolled increase of the actual seam form.

## 2. The matched seam dominates the same compactified control

PF-233 gives

\[
T_a\ge c_0s^2A.
\tag{20}
\]

Apply (18) with strip halfwidth `r_i=w_i/s`:

\[
q_i^{\rm mat}=f_{r_i}(T_a)
\ge f_{r_i}(c_0s^2A).
\tag{21}
\]

Put `c=sqrt(c_0)<=1`. Since `tanh(cz)>=c tanh(z)` for `0<c<=1`, scalar functional calculus in `A` gives

\[
\boxed{q_i^{\rm mat}\ge c_0s f_{w_i}(A).}
\tag{22}
\]

The remaining boundary mass factor does not commute with `A`, but it can be handled at the strip-energy level. Define

\[
R=M_{\sqrt{s/a}}=\sqrt{s}\,B^{1/2},
\qquad
h=R^{-1}=M_{\sqrt{a/s}}.
\tag{23}
\]

Then `0<h<=1` and `|h'/h|<=delta`. For every product-strip test function,

\[
|\partial_\theta(hu)|^2
\le2|u_\theta|^2+2\delta^2|u|^2,
\]

while the transverse derivative and `csc^2(theta)` potential do not increase. Since `csc^2(theta)>=1`, the full strip energy satisfies

\[
\mathcal E_A[hu]\le C_\delta\mathcal E_A[u].
\tag{24}
\]

Taking the infimum over extensions with common boundary value `Ry` yields

\[
\langle y,f_w(A)y\rangle
\le C_\delta\langle Ry,f_w(A)Ry\rangle.
\tag{25}
\]

Using `B^{1/2}=s^{-1/2}R` and (22),

\[
\begin{aligned}
\langle y,Q_i^{\rm mat}y\rangle
&=\frac1s\langle Ry,q_i^{\rm mat}Ry\rangle\\
&\ge c_0\langle Ry,f_{w_i}(A)Ry\rangle\\
&\ge\frac{c_0}{C_\delta}\langle y,f_{w_i}(A)y\rangle.
\end{aligned}
\tag{26}
\]

This proves (12), and (11)+(12) prove (1). The direction is exactly compatible with PF-237: a softer actual form may have noncompact inverse even though the harder matched form has compact inverse.

## 3. The normalized inverse contracts to one inverse-corridor crossing

Let `Lambda>0` and block-diagonal `Q>0` be positive on `H\oplus H`, and set

\[
D=(I+Q^{-1/2}\Lambda Q^{-1/2})^{-1},
\qquad
\mathcal G=Q^{1/2}\Lambda^{-1}Q^{1/2}.
\tag{27}
\]

Then

\[
D=\mathcal G(I+\mathcal G)^{-1}
=I-(I+\mathcal G)^{-1}.
\tag{28}
\]

Write `mathcal G=(G_ij)` and set

\[
E=I+G_{22},
\qquad
S=I+G_{11}-G_{12}E^{-1}G_{21}.
\tag{29}
\]

Because

\[
\begin{pmatrix}G_{11}&G_{12}\\G_{21}&I+G_{22}\end{pmatrix}
=\mathcal G+\begin{pmatrix}0&0\\0&I\end{pmatrix}\ge0,
\]

its Schur complement gives `S>=I`; also `E>=I`. Block inversion of `I+mathcal G` therefore gives

\[
\boxed{D_{21}=E^{-1}G_{21}S^{-1},}
\tag{30}
\]

with both outside factors contractions. Consequently

\[
\boxed{s_j(D_{21})\le s_j(G_{21}).}
\tag{31}
\]

This is the key noncommutative step: the normalized off-diagonal inverse is controlled by a **single actual crossing of `Lambda^{-1}`**, without comparing the entire inverse in Loewner order.

For the unbounded form realizations here, one may first apply (30)--(31) on common bounded spectral/form truncations. The factorization below gives uniform boundedness and the closed-form limit.

## 4. One-sided seam order inserts the PF-236 factors around the inverse corridor

PF-233 writes

\[
\Lambda_a
=\mathcal B\,
K
\begin{pmatrix}
\coth K&-\operatorname{csch}K\\
-\operatorname{csch}K&\coth K
\end{pmatrix}
\mathcal B,
\qquad
\mathcal B=\operatorname{diag}(B^{1/2},B^{1/2}).
\tag{32}
\]

Since `coth^2-csch^2=1`,

\[
\boxed{
(\Lambda_a^{-1})_{21}
=B^{-1/2}K^{-1}\operatorname{csch}K\,B^{-1/2}.
}
\tag{33}
\]

Assume only (13). The form version of Douglas factorization gives contractions `V_i` such that

\[
Q_i^{1/2}
=\sqrt{C_i}\,V_i(q_i^{\rm mat})^{1/2}B^{1/2}
\tag{34}
\]

on the common form core and then by closure. Hence

\[
\begin{aligned}
G_{21}
&=Q_2^{1/2}(\Lambda_a^{-1})_{21}Q_1^{1/2}\\
&=\sqrt{C_1C_2}\,V_2
\Bigl[(q_2^{\rm mat})^{1/2}K^{-1}\operatorname{csch}K(q_1^{\rm mat})^{1/2}\Bigr]V_1^*.
\end{aligned}
\tag{35}
\]

All operators inside the square brackets are functions of the same `K`. Since `q_i^{mat}=K tanh(r_iK)`, the middle factor is

\[
H_{r_1,r_2}(K)
=\sqrt{\tanh(r_1K)\tanh(r_2K)}\,\operatorname{csch}K.
\tag{36}
\]

Using `tanh(y)<=y`,

\[
0\le H_{r_1,r_2}(K)
\le\sqrt{r_1r_2}\,K\operatorname{csch}K
=\frac{\sqrt{w_1w_2}}sF(K).
\tag{37}
\]

PF-233 gives ordered transverse eigenvalues

\[
k_m:=\sqrt{\lambda_m(T_a)}
\ge\sqrt{c_0}\,s(m+\alpha).
\tag{38}
\]

Since `F(z)=z/sinh(z)` is decreasing, (31), the ideal property of singular values, and (37)--(38) give exactly (4).

This explains why PF-237's endpoint packets are not counterexamples to dressed transfer. Every normalized cross-boundary contribution is forced through `(Lambda_a^{-1})_{21}`. The one-sided seam inequality supplies at most the matched square-root factors, turning `K^{-1}csch K` into the PF-236 envelope. The endpoint barrier is therefore already encoded globally in the inverse corridor; no explicit endpoint cutoff is needed.

## 5. Canonical prime-flute consequence

For PF-205's neighboring seams,

\[
w_i=\sinh\rho_i=\kappa d_i=O(P_i^{-1}),
\tag{39}
\]

while PF-230/PF-233 give uniform canonical-tail bounds for `eta` and `delta`. Hence `sup_i C_i<infinity`. Equation (4) therefore has the same asymptotic content as PF-236: only `O(s^{-1})` channels occur in each fixed scaled band, every such channel has amplitude `O(sqrt(w_1w_2)/s)`, and the singular values decay exponentially above that band. The spectral-type mismatch from PF-237 costs **no additional prime-dependent factor**.

This resolves `CLUE-conformal-rectangle-dtn-normalizer-transfer` positively for the exact PF-233 diagonal corridor with the actual complete lifted PF-205 seam. The next local theorem is no longer endpoint normalization; it is stability of (4) after inserting PF-232's reciprocal-prime-small **shear at the normalized off-diagonal inverse level**. Physical `P/H` recoupling, finite one-cusp-pant completion, neighboring-cell extension, and PF-222 nested-cut reassembly remain separate later gates.

## 6. Prior-art and novelty audit

The ingredients are individually classical. Variational positive DtN forms and quadratic-form methods are standard; PF-232 already records Olaf Post, *Boundary pairs associated with quadratic forms*, Mathematische Nachrichten 289 (2016), 1052--1099, arXiv `1210.4707`, as representative background. General DtN/boundary-Laplacian comparison is surveyed by Girouard--Karpukhin--Levitin--Polterovich, *The Dirichlet-to-Neumann map, the boundary Laplacian, and Hörmander's rediscovered manuscript*, Journal of Spectral Theory 12 (2022), 195--225, DOI `10.4171/JST/399`. Schur complements, Douglas factorization, and singular-value ideal inequalities are standard operator theory.

A structure-directed audit for strip DtN functional calculus, positive block/off-diagonal singular-value inequalities, and DtN/boundary-Laplacian comparison did not locate a theorem whose content is the PF-specific chain here. No novelty is claimed for those general tools. The project-specific result is their exact combination with PF-235's compactification, identity (16), the only seam-form order compatible with PF-237, and PF-233's inverse corridor block (33), yielding the actual complete-lift envelope (4). The proof is self-contained from the current prime-flute corpus plus elementary functional analysis; no external theorem is imported as a PF-specific black box.

## 7. Falsification and boundary checks

1. **No reverse seam comparison.** PF-238 proves `Q_act<=C Q_mat`; PF-237 proves a global lower bound `Q_act>=c Q_mat` is impossible on the complete lift.
2. **Complete lifted control only.** `Q_i^{act}` is the complete lifted symmetric seam used by PF-234/PF-235/PF-237, not the closed-cuff or finite one-cusp-pant boundary operator.
3. **Diagonal corridor only.** `Lambda_a` is PF-233's variable-width diagonal corridor. PF-232's shear is not inserted into (32), and full-form comparability alone still does not prove off-diagonal inverse stability.
4. **Canonical density is essential.** Identity (9) uses the density-corrected unitary (7), not an unweighted coordinate substitution.
5. **Uniform constant, not asymptotic identity.** The `cosh^3(rho_i)` part is `1+O(w_i^2)`, but `C_delta/c_0` is only uniformly bounded by current corridor estimates. The theorem preserves scale/envelope up to a uniform constant, not `1+o(1)` equivalence.
6. **No hidden compactness assumption.** The proof never requires `(Q_i^{act})^{-1}` to be compact. Compactness of `D_{21}^{act}` comes from the explicit `F(K)` factor after crossing the corridor.
7. The physical `P/H` projections, finite pant completion, neighboring-cell recoupling, and global Schur/nested-cut operations may still alter the local block and remain unproved.
8. Nothing here proves the full first relative resolvent is in weak `S_1`, wave-operator equivalence, determinant/resonance control, prime/clone separation, a zeta-zero statement, or RH.

## Consequences for the research line

The endpoint-normalization branch is closed positively at the complete-lift **diagonal** level. Do not build a central/endpoint cutoff merely to repair PF-237's noncompact inverse seam: PF-238 shows that the exact inverse corridor already supplies the required suppression globally.

The next local gate is sharper: start from (4) and determine whether PF-232's `O(P_n^{-1})` shear perturbation can be propagated through the normalized off-diagonal inverse **without losing the `F(sm)` singular-value envelope**. That must be an inverse/off-diagonal theorem, not another Loewner comparison of the full positive DtN form. After shear, physical `P/H` recoupling and finite-pant completion remain before PF-222's overlapping nested weak-trace reassembly becomes the main global target.
