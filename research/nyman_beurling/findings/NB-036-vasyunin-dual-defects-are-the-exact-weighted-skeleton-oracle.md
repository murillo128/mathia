# NB-036 — Vasyunin dual defects are the exact missing target oracle for the weighted skeleton

**Status:** `CLASSICAL-VASYUNIN-BIORTHOGONALITY + EXACT-DERIVED-SOURCE-DUALITY + EXACT-DEFECT-MATRIX-REDUCTION + LINEAR-SCALE-MOBIUS-LOCKING + TARGET-DATA-METHOD-BOUNDARY`. `NB-034` gives an `N`-uniformly conditioned weighted-tail quotient but leaves its projected Gram matrix and target pairings apparently dependent on the full tail. `NB-035` then makes the quotient's one tail source coordinate explicit through a bounded reciprocal-Möbius selector. The missing information can be localized exactly by combining those constructions with Vasyunin's classical finite-support biorthogonal family.

Use the canonical generators

\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_N=\operatorname{span}(g_2,\ldots,g_N),
\qquad e(x)=1,
\tag{1}
\]

and harmonic shells

\[
I_t=\left(\frac1{t+1},\frac1t\right],
\qquad
E_t:=t(t+1)\mathbf 1_{I_t},
\qquad E_0:=0.
\tag{2}
\]

For `n>=2` define the sign-adjusted Vasyunin dual

\[
\boxed{
\xi_n:=-\sum_{d\mid n}\mu\!\left(\frac nd\right)(E_d-E_{d-1}).
}
\tag{3}
\]

Vasyunin's Theorem 7 gives the corresponding biorthogonal system for the floor-function convention `e_n^{V}=-g_n`; therefore, in the present fractional-part convention,

\[
\boxed{
\langle g_j,\xi_n\rangle=\delta_{jn},
\qquad
\langle e,\xi_n\rangle=-\mu(n).
}
\tag{4}
\]

The first identity is classical prior art, not a new biorthogonality theorem. The line-local consequences below are the substantive reduction.

First, the explicit two-shell support in (3) gives the elementary uniform norm estimate

\[
\boxed{
\|\xi_n\|^2\le4\sigma_2(n)\le4\zeta(2)n^2,
\qquad
\|\xi_n\|\le2\sqrt{\zeta(2)}\,n.
}
\tag{5}
\]

Hence every finite approximant `v=\sum_{j=2}^N a_jg_j`, with residual `r=e-v`, obeys

\[
\boxed{
|a_n+\mu(n)|
=|\langle r,\xi_n\rangle|
\le2\sqrt{\zeta(2)}\,n\|r\|,
\qquad 2\le n\le N.
}
\tag{6}
\]

For the canonical best residual `r_N=e-P_{V_N}e`, this locks a **whole** growing prefix to Möbius values whenever `Y_N d_N->0`, where `d_N=\|r_N\|`. In particular, uniform locking is available up to a fixed multiple of `d_N^{-1}`; the extra `log(e/d_N)` used by the elementary divisor bound in `NB-027` is not intrinsic to that coefficient-recovery step.

Second, the bounded selectors `\Psi_L` from `NB-035` are exactly reciprocal partial sums of these classical dual vectors. With `\Psi_L` normalized as in `NB-035`, one has

\[
\boxed{
\xi_n=n(\Psi_{n-1}-\Psi_n),
\qquad
\Psi_L=E_1-\sum_{n=2}^L\frac{\xi_n}{n}.
}
\tag{7}
\]

Thus the absolute norm bound for `\Psi_L` should not be interpreted as a second unrelated dual mechanism: it is a uniformly bounded cumulative combination of Vasyunin's biorthogonal family, organized by the harmonic-shell endpoint functional.

The main new reduction concerns the `NB-034` weighted skeleton. For `2<=M<=N`, let

\[
\widehat W_{M,N}
=\operatorname{span}(ng_n-(n+1)g_{n+1}:M\le n<N),
\qquad
\widehat Q=I-P_{\widehat W_{M,N}},
\tag{8}
\]

\[
\widehat K_{M,N}=V_N\cap\widehat W_{M,N}^{\perp},
\qquad
\widehat k_j=\widehat Qg_j\quad(2\le j\le M),
\tag{9}
\]

and write `\widehat H_{M,N}` for the Gram matrix of `(\widehat k_2,\ldots,\widehat k_M)`. Define

\[
\boxed{
\lambda_j^{(M)}:=\xi_j\quad(2\le j<M),
\qquad
\lambda_M^{(M)}:=M\Psi_{M-1}.
}
\tag{10}
\]

Every `\lambda_j^{(M)}` is supported on the first `M-1` shells. Since `NB-034` proves that `\widehat W_{M,N}` is exactly the kernel of those shell observations, the vectors in (10) lie in `\widehat W_{M,N}^{\perp}`. Equations (4) and the exact pairing law of `NB-035` then give

\[
\boxed{
\langle\widehat k_i,\lambda_j^{(M)}\rangle=\delta_{ij}
\qquad(2\le i,j\le M).
}
\tag{11}
\]

Consequently the source coordinates of the weighted skeleton have explicit dual readouts that require no computation of `P_{\widehat W}`. If

\[
\widehat Qv=
\sum_{j=2}^{M}c_j\widehat k_j,
\qquad
v=\sum_{n=2}^Na_ng_n,
\]

then

\[
\boxed{
 c_j=\langle v,\lambda_j^{(M)}\rangle=a_j\quad(j<M),
\qquad
 c_M=\langle v,\lambda_M^{(M)}\rangle
 =M\sum_{n=M}^{N}\frac{a_n}{n}.
}
\tag{12}
\]

The dual norms are also explicit at the correct retained scale:

\[
\|\lambda_j^{(M)}\|
\le2\sqrt{\zeta(2)}\,j\quad(j<M),
\qquad
\|\lambda_M^{(M)}\|
\le C_*M,
\tag{13}
\]

where `C_*` is the absolute selector constant from `NB-035`.

## 1. The Vasyunin norm estimate gives inverse-distance prefix locking

From (3), the coefficient of `E_t` in `\xi_n` is

\[
c_t
=-\mathbf 1_{t\mid n}\mu(n/t)
+\mathbf 1_{t+1\mid n}\mu(n/(t+1)).
\tag{14}
\]

Because `\|E_t\|^2=t(t+1)` and the shell supports are disjoint,

\[
\|\xi_n\|^2
=\sum_{t=1}^{n}t(t+1)|c_t|^2.
\tag{15}
\]

Using `|u-v|^2<=2|u|^2+2|v|^2`, then grouping the contributions belonging to the same divisor `d|n`, gives

\[
\begin{aligned}
\|\xi_n\|^2
&\le
2\sum_{d\mid n}d(d+1)
+2\sum_{\substack{d\mid n\\d\ge2}}d(d-1)\\
&\le4\sum_{d\mid n}d^2
=4\sigma_2(n)
\le4\zeta(2)n^2.
\end{aligned}
\tag{16}
\]

Equation (6) now follows immediately from (4):

\[
\langle r,\xi_n\rangle
=\langle e,\xi_n\rangle-a_n
=-\mu(n)-a_n.
\tag{17}
\]

This improves the uniform fallback `|a_n+\mu(n)|<=2d_N\sigma(n)` of `NB-020` when the entire initial interval is to be locked. It does not improve every weighted coefficient-budget consequence of `NB-020`: the two estimates have different arithmetic weights, and the new statement is only a direct `O(nd_N)` coordinate estimate.

## 2. The bounded selector is the cumulative Vasyunin dual

Vasyunin's finite dual vector `\xi_n` is supported on shells `I_1,\ldots,I_n`. The difference `n(\Psi_{n-1}-\Psi_n)` has the same support bound. Using the exact `NB-035` pairings,

\[
\langle g_j,\Psi_L\rangle
=0\quad(j\le L),
\qquad
\langle g_j,\Psi_L\rangle=1/j\quad(j>L),
\tag{18}
\]

shows that `n(\Psi_{n-1}-\Psi_n)` pairs with `g_j` as `\delta_{jn}`. The early-shell rank statement of `NB-034` makes these finite shell observations nondegenerate, so this vector equals `\xi_n`. Telescoping yields the second identity in (7). Its target pairing is consistent with

\[
\langle e,\Psi_L\rangle
=1-\sum_{n=2}^L\frac{\langle e,\xi_n\rangle}{n}
=\sum_{n\le L}\frac{\mu(n)}n
=m(L).
\tag{19}
\]

This relation explains why the selector family can remain bounded even though the individual dual norms grow linearly: the reciprocal Möbius-weighted cumulative geometry contains substantial cancellation. No asymptotic Möbius estimate is needed for the finite identity (7).

## 3. The projected metric differs from the explicit early-shell metric by one positive defect Gram matrix

Let `B_M` be the explicit early-shell Gram matrix from `NB-034`,

\[
(B_M)_{ij}
=\sum_{t=1}^{M-1}
\frac{\{t/i\}\{t/j\}}{t(t+1)}.
\tag{20}
\]

The vectors `\lambda_j^{(M)}` are the dual basis to the first-shell restrictions of `g_2,\ldots,g_M`. Therefore their Gram matrix is exactly

\[
\boxed{
\bigl(\langle\lambda_i^{(M)},\lambda_j^{(M)}\rangle\bigr)
=B_M^{-1}.
}
\tag{21}
\]

Now project these explicit duals onto the full finite Nyman space and define their unresolved defects

\[
p_j:=P_{V_N}\lambda_j^{(M)}\in\widehat K_{M,N},
\qquad
z_j:=(I-P_{V_N})\lambda_j^{(M)}\in V_N^\perp,
\tag{22}
\]

\[
Z_{M,N}:=\bigl(\langle z_i,z_j\rangle\bigr)_{2\le i,j\le M}\succeq0.
\tag{23}
\]

Because `(p_j)` is the dual basis to `(\widehat k_j)` inside `\widehat K_{M,N}`, its Gram matrix is `\widehat H_{M,N}^{-1}`. Orthogonal decomposition in (22) and (21) give the exact identity

\[
\boxed{
\widehat H_{M,N}^{-1}
=B_M^{-1}-Z_{M,N}.
}
\tag{24}
\]

Thus every bit of metric information missing when one replaces the true retained Gram by the explicit early-shell model is carried by a **single positive semidefinite defect Gram matrix** formed from the `V_N^\perp` components of explicit finite-shell dual vectors. In particular `Z_{M,N}\prec B_M^{-1}` because the retained Gram is positive definite.

## 4. The target data require one additional defect correlation vector, and nothing else

Let

\[
r_N=e-P_{V_N}e,
\qquad d_N=\|r_N\|,
\tag{25}
\]

and define

\[
\eta_{M,N}:=
\bigl(\langle r_N,z_j\rangle\bigr)_{2\le j\le M},
\tag{26}
\]

\[
u_M:=
\bigl(-\mu(2),\ldots,-\mu(M-1),\,M m(M-1)\bigr)^T.
\tag{27}
\]

If `c_{M,N}` denotes the source-coordinate vector of `P_{\widehat K_{M,N}}e` in the basis `(\widehat k_2,\ldots,\widehat k_M)`, then the duality above gives

\[
\boxed{
c_{M,N}=u_M-\eta_{M,N}.
}
\tag{28}
\]

For `j<M`, this is simply `a_{N,j}=-\mu(j)-\eta_j`; at the endpoint it is the `NB-035` identity `\tau_{M,N}=Mm(M-1)-\eta_M`.

The defect vector and matrix obey the automatic PSD control

\[
\boxed{
\eta_{M,N}\eta_{M,N}^*
\preceq d_N^2 Z_{M,N},
}
\tag{29}
\]

because for every coefficient vector `q`,

\[
|q^*\eta|^2
=\left|\left\langle r_N,\sum_jq_jz_j\right\rangle\right|^2
\le d_N^2 q^*Zq.
\]

Finally, with

\[
\widehat\kappa_{M,N}
=\operatorname{dist}(e,\widehat K_{M,N}),
\]

the full target-aware reduced certificate has the exact defect form

\[
\boxed{
\widehat\kappa_{M,N}^2
=1-(u_M-\eta_{M,N})^*
(B_M^{-1}-Z_{M,N})^{-1}
(u_M-\eta_{M,N}).
}
\tag{30}
\]

Equations (24), (28), and (30) answer the data-localization part of the weighted-skeleton question exactly. The explicit shell matrix `B_M` and source vector `u_M` are not approximations guessed from the full section; they are finite arithmetic data. The entire remaining dependence on the upper section `N` is the dual-defect pair

\[
\boxed{(Z_{M,N},\eta_{M,N}).}
\tag{31}
\]

No separate hidden target vector or projected-tail parameter remains.

## 5. Prior-art and adversarial boundary

The biorthogonality in (4) is classical. V. I. Vasyunin, *On a biorthogonal system associated with the Riemann hypothesis*, Algebra i Analiz 7:3 (1995), 118–135; English translation St. Petersburg Math. J. 7:3 (1996), 405–419, proves minimality of the canonical step family and gives its explicit finite-support biorthogonal system in Theorem 7. The sign in (3) only converts Vasyunin's floor convention `e_n^V=-g_n` to the fractional-part convention used in this line. This source is therefore load-bearing and is anchored in `SOURCES.md`.

The norm estimate (5), the cumulative identity (7), and the defect formulas (24)--(31) are finite consequences/syntheses of that classical dual system with the already-persisted `NB-034`/`NB-035` quotient geometry. A targeted literature search around Nyman finite sections, Vasyunin biorthogonality, Gram inverses, and finite projection geometry did not locate this exact weighted-tail defect normal form. Search absence is not a priority claim, and generic dual-basis/Schur-complement algebra is of course standard.

The reduction deliberately does **not** claim that `(Z,eta)` is cheap to evaluate or easy to bound. Computing `z_j=(I-P_{V_N})\lambda_j` literally still requires the full Nyman projection and is therefore not a reduced algorithm. Likewise (29) contains the unknown `d_N`; using it alone as an upper bound would be circular for an attempt to prove a new distance rate. The point is localization: any source-specific reduced construction must now control this precise defect pair, or an equivalent quantity, rather than an unspecified projected Gram matrix.

Nor does the inverse-distance locking in (6) prove `d_N->0`, RH, or a new asymptotic approximation rate. It is conditional on the observed residual size and remains one-way. The improvement over the elementary uniform bound used in `NB-027` removes a logarithmic bookkeeping loss in the lockable prefix, but the arithmetic sign-pattern and spectral issues isolated there remain separate.

## 6. Research consequence

The weighted skeleton now separates into an explicit finite arithmetic model and one exact upper-section defect. `B_M` gives the early-shell metric, `u_M` gives the target/source coordinates selected by Möbius inversion, and `(Z_{M,N},eta_{M,N})` measures precisely how the full section changes them. This makes the unresolved target-data problem narrower than constructing `P_{\widehat W}` or estimating every entry of the full Gram matrix.

For the proposed near-logarithmic regime `M=M_N` with `M/log N->infinity`, the next theorem should therefore estimate `(Z_{M,N},eta_{M,N})` strongly enough to control the quadratic form in (30) at the required relative distance scale **without** first solving the `N`-dimensional projection problem. A proof that no such source estimate is available from a stated hypothesis would also be informative. `NB-036` supplies the exact oracle reduction and the projector-free source duals, but not that final arithmetic estimate.