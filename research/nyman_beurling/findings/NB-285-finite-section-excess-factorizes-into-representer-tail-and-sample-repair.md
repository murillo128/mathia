# NB-285 — finite-section excess factorizes into representer tail and sample repair

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-282, NB-283, NB-284
- **Classification:** `EXACT-DERIVED + FIRST-FREE-JET-COST + FINITE-SECTION-GRAM + REPRESENTER-TAIL + OPTIMAL-RIGHT-INVERSE + MOVING-PACKET-CONDITIONING + ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-284` isolates the genuine finite-section penalty

\[
\mathfrak A_M(Z)
=
\mathcal C_M(Z)-\mathcal C_\infty(Z)
\ge0,
\tag{1}
\]

and proves that it vanishes when the zero packet `Z` is fixed and the Dirichlet cutoff `M` tends to infinity. Its proof uses two qualitative ingredients: approximation of an infinite-source feasible vector by finite-source vectors, and one bounded finite right inverse that repairs the resulting interpolation defect.

Those two ingredients admit an exact quantitative separation. For every fixed packet and every eventually feasible section, the finite-section penalty is

\[
\boxed{
\mathfrak A_M(Z)
=
\mathfrak T_M(Z)+\mathfrak R_M(Z),
}
\tag{2}
\]

where `T_M` is the squared finite-section tail of the **infinite minimum-norm interpolation representer**, while `R_M` is the minimum extra norm needed to repair the sample defect created by truncating that representer.

More precisely, write

\[
\mathcal H
:=
\mathcal H_Z^\infty,
\qquad
V_M:=V_{M,Z}\subset\mathcal H,
\qquad
L:=L_Z:\mathcal H\to\mathbb C^N,
\tag{3}
\]

using the closed infinite quotient-source space, nested finite quotient-source sections, and first-free value map of `NB-284`. Let `P_M` be the orthogonal projection of `H` onto `V_M`, and define the infinite and finite sampling Gramians

\[
K_\infty:=LL^*,
\qquad
K_M:=LP_ML^*.
\tag{4}
\]

`NB-282` gives eventual surjectivity of `L|_{V_M}`, so for all sufficiently large `M`, both matrices in `(4)` are positive definite. If `y` is the prescribed first-free datum and

\[
a:=K_\infty^{-1}y,
\qquad
E_M:=K_\infty-K_M=L(I-P_M)L^*\succeq0,
\tag{5}
\]

then

\[
\boxed{
\mathfrak T_M
=
a^*E_Ma
=
\|(I-P_M)L^*a\|_{H^2}^2,
}
\tag{6}
\]

and

\[
\boxed{
\mathfrak R_M
=
(E_Ma)^*K_M^{-1}(E_Ma).
}
\tag{7}
\]

Hence

\[
\boxed{
\mathfrak A_M
=
a^*E_Ma
+(E_Ma)^*K_M^{-1}(E_Ma).
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\mathfrak A_M
=
y^*(K_M^{-1}-K_\infty^{-1})y
=
\|h_M-h_\infty\|_{H^2}^2,
}
\tag{9}
\]

where `h_M` and `h_infty` are the finite and infinite minimum-norm interpolants.

The optimal finite-section right inverse is

\[
R_M^{\rm opt}
:=
P_ML^*K_M^{-1},
\tag{10}
\]

and satisfies

\[
\boxed{
\|R_M^{\rm opt}\|^2
=
\frac1{\lambda_{\min}(K_M)}.
}
\tag{11}
\]

Thus the vague nonuniformity left by `NB-284` separates into two explicit mechanisms:

1. **representer non-compressibility**, measured by the finite-dimensional tail Gram `E_M`; and
2. **sample-repair amplification**, measured optimally by `K_M^{-1}` on the specific defect `E_Ma`.

In particular,

\[
\boxed{
\mathfrak T_M
\le
\mathfrak A_M
\le
\mathfrak T_M
\left(
1+
\frac{\|E_M\|}{\lambda_{\min}(K_M)}
\right).
}
\tag{12}
\]

For a moving Ford packet, an order-one finite-section obstruction therefore cannot remain an undifferentiated failure of density. It must be visible either as an order-one tail of the canonical interpolation representer, or as a sufficiently ill-conditioned repair of a tail-induced sample defect.

The generic Hilbert/RKHS identities underlying `(8)` are classical minimum-norm interpolation algebra. The research-specific point is their application to the exact finite-versus-infinite source penalty `A_M` isolated by `NB-284`, including the identification of the two quantities that must now be controlled uniformly in the moving Nyman/Ford regime.

---

## 1. The correct Gram lives in the closed quotient-source space

Fix a packet

\[
Z=\{(\rho_j,m_j):1\le j\le N\}
\tag{13}
\]

as in `NB-284`, with selected zeros strictly inside `Re s>1/2`, and retain all of its notation. After division by the selected packet Blaschke factor, the first-free constraints are ordinary values

\[
Lh
=
\bigl(h(\rho_1),\ldots,h(\rho_N)\bigr)
=
y.
\tag{14}
\]

The relevant infinite source space is not ambient `H^2` but

\[
\mathcal H
=
\mathcal H_Z^\infty
=
\overline{\bigcup_MV_{M,Z}}^{H^2}.
\tag{15}
\]

This distinction is essential. In general

\[
\mathcal H
\subseteq
C_ZH^2
\subseteq
H^2,
\tag{16}
\]

and `NB-284` deliberately does not assume either inclusion is an equality.

Restrict `L=L_Z` to `H`. Because `NB-282` supplies a finite section on which `L` is already onto `C^N`, the map

\[
L:\mathcal H\to\mathbb C^N
\tag{17}
\]

is surjective. Therefore

\[
K_\infty=LL^*
\tag{18}
\]

is positive definite.

The adjoint in `(18)` is the adjoint **inside `H`**. If `k_{\rho_j}` denotes the ambient half-plane Hardy evaluation kernel, then the canonical source-space evaluation representer is

\[
g_j
:=
L^*e_j
=
P_{\mathcal H}k_{\rho_j},
\tag{19}
\]

not necessarily the ambient kernel itself. Consequently `K_infty` should not be confused with the reduced ambient zero Gram of `NB-283/284` unless an additional completeness equality has been proved.

For each finite section let

\[
P_M:\mathcal H\to V_M
\tag{20}
\]

be the orthogonal projector. The finite sampling operator is the restriction `L|_{V_M}`, and its Gram on the data space is

\[
K_M
=
(L|_{V_M})(L|_{V_M})^*
=
LP_ML^*.
\tag{21}
\]

For all `M` beyond the eventual-surjectivity threshold of `NB-282`, `K_M` is positive definite.

Because the spaces `V_M` are nested,

\[
P_M\preceq P_{M+1}\preceq I
\tag{22}
\]

as quadratic forms, hence

\[
0\prec K_M\preceq K_{M+1}\preceq K_\infty.
\tag{23}
\]

Define the missing sampling Gram

\[
\boxed{
E_M
:=
K_\infty-K_M
=
L(I-P_M)L^*
\succeq0.
}
\tag{24}
\]

This matrix is the exact finite-dimensional shadow of everything the current section has not yet captured from the evaluation representers.

---

## 2. The finite and infinite minimum-norm interpolants are explicit

The infinite constrained problem of `NB-284` is

\[
\mathcal C_\infty
=
\min\{\|h\|^2:h\in\mathcal H,\ Lh=y\}.
\tag{25}
\]

Since `L` is onto, the unique minimum-norm solution is

\[
\boxed{
h_\infty
=L^*K_\infty^{-1}y.
}
\tag{26}
\]

Indeed `Lh_infty=y`, while `h_infty` lies in `ran L^*=(ker L)^perp`, so every other feasible vector differs from it by an orthogonal element of `ker L`. Therefore

\[
\boxed{
\mathcal C_\infty
=y^*K_\infty^{-1}y.
}
\tag{27}
\]

Likewise, for an eventually feasible finite section,

\[
\mathcal C_M
=
\min\{\|h\|^2:h\in V_M,\ Lh=y\}.
\tag{28}
\]

The adjoint of `L|_{V_M}` is `P_ML^*`, so its minimum-norm interpolant is

\[
\boxed{
h_M
=P_ML^*K_M^{-1}y,
}
\tag{29}
\]

with cost

\[
\boxed{
\mathcal C_M
=y^*K_M^{-1}y.
}
\tag{30}
\]

Subtracting `(27)` from `(30)` gives the first exact Gram formula for the finite-section penalty:

\[
\boxed{
\mathfrak A_M
=
y^*(K_M^{-1}-K_\infty^{-1})y.
}
\tag{31}
\]

Since `K_M<=K_infty`, inverse order gives

\[
K_M^{-1}\succeq K_\infty^{-1},
\tag{32}
\]

so positivity of `A_M` is visible directly from the data-space Gram.

There is also an exact geometric identity. Both `h_M` and `h_infty` interpolate `y`, hence

\[
h_M-h_\infty\in\ker L.
\tag{33}
\]

The infinite minimizer satisfies `h_infty perpendicular ker L`; therefore

\[
\|h_M\|^2
=
\|h_\infty\|^2
+
\|h_M-h_\infty\|^2.
\tag{34}
\]

Thus

\[
\boxed{
\mathfrak A_M
=
\|h_M-h_\infty\|^2.
}
\tag{35}
\]

So the finite-section excess is not merely a difference between two optimization values. It is exactly the squared distance between the two canonical constrained interpolants.

---

## 3. Exact tail-plus-repair factorization

Set

\[
a:=K_\infty^{-1}y,
\tag{36}
\]

so that

\[
h_\infty=L^*a.
\tag{37}
\]

Project the infinite minimizer into the finite section:

\[
P_Mh_\infty=P_ML^*a.
\tag{38}
\]

Its lost norm is

\[
\begin{aligned}
\|(I-P_M)h_\infty\|^2
&=a^*L(I-P_M)L^*a\\
&=a^*E_Ma.
\end{aligned}
\tag{39}
\]

Define

\[
\boxed{
\mathfrak T_M
:=
a^*E_Ma.
}
\tag{40}
\]

This is the **representer-tail term**.

The projected vector `(38)` need not remain feasible. Its data are

\[
LP_Mh_\infty
=K_Ma
=(K_\infty-E_M)a
=y-E_Ma.
\tag{41}
\]

Hence truncating the infinite minimizer creates the exact sample defect

\[
\boxed{
d_M:=E_Ma.
}
\tag{42}
\]

Among all finite-section vectors whose samples equal a prescribed `d`, the minimum-norm correction is supplied by

\[
R_M^{\rm opt}
:=
P_ML^*K_M^{-1}.
\tag{43}
\]

Indeed

\[
LR_M^{\rm opt}
=K_MK_M^{-1}
=I.
\tag{44}
\]

The finite minimizer can therefore be reconstructed exactly as

\[
\boxed{
h_M
=P_Mh_\infty
+R_M^{\rm opt}d_M.
}
\tag{45}
\]

To verify `(45)`, use `y=K_infty a=(K_M+E_M)a`, giving

\[
K_M^{-1}y
=a+K_M^{-1}E_Ma,
\tag{46}
\]

and substitute into `(29)`.

Subtracting `h_infty` yields

\[
h_M-h_\infty
=
-(I-P_M)h_\infty
+R_M^{\rm opt}d_M.
\tag{47}
\]

The first term lies in `V_M^perp` and the second in `V_M`, so the two terms are orthogonal. Therefore

\[
\mathfrak A_M
=
\|(I-P_M)h_\infty\|^2
+
\|R_M^{\rm opt}d_M\|^2.
\tag{48}
\]

The first term is `(40)`. For the second,

\[
(R_M^{\rm opt})^*R_M^{\rm opt}
=K_M^{-1},
\tag{49}
\]

because

\[
K_M^{-1}LP_ML^*K_M^{-1}
=K_M^{-1}.
\tag{50}
\]

Consequently

\[
\boxed{
\mathfrak R_M
:=
\|R_M^{\rm opt}d_M\|^2
=
(E_Ma)^*K_M^{-1}(E_Ma).
}
\tag{51}
\]

Combining `(40)` and `(51)` proves `(8)`.

The same identity follows algebraically from the resolvent formula

\[
K_M^{-1}-K_\infty^{-1}
=K_M^{-1}E_MK_\infty^{-1},
\tag{52}
\]

but the orthogonal decomposition `(47)` is more informative: it identifies separately the norm discarded by truncation and the extra norm paid to restore the exact first-free values.

---

## 4. The right-inverse constant in NB-284 has a canonical optimal value

The proof of fixed-packet convergence in `NB-284` chooses some finite right inverse

\[
R:\mathbb C^N\to V_{M_0}
\tag{53}
\]

and pays its norm when repairing an approximate interpolant. That proves convergence, but the right-inverse constant depends on the chosen construction.

At a given feasible section `M`, `(43)` is the Moore--Penrose/minimum-norm right inverse of `L|_{V_M}`. Its norm is therefore controlled exactly by the smallest singular value of that sampling map. Since

\[
K_M
=(L|_{V_M})(L|_{V_M})^*,
\tag{54}
\]

we have

\[
\boxed{
\|R_M^{\rm opt}\|
=
\frac1{\sigma_{\min}(L|_{V_M})}
=
\frac1{\sqrt{\lambda_{\min}(K_M)}}.
}
\tag{55}
\]

This matters for the interpretation of `NB-282`. Its sparse prime-power Vandermonde construction proves that a finite right inverse exists, but a badly conditioned particular Vandermonde is not by itself evidence that first-free neutralization is intrinsically expensive. The intrinsic conditioning quantity is `(55)`, optimized over **all** finite-section realizations automatically.

Likewise, if one constructs a source-faithful right inverse with norm `B_M`, then necessarily

\[
\lambda_{\min}(K_M)^{-1/2}
\le B_M.
\tag{56}
\]

Such a construction gives an upper bound on the optimal repair price; a lower bound on every right inverse requires control in the opposite direction through `lambda_min(K_M)`.

---

## 5. The missing Gram is a Gram of canonical representer tails

Equation `(24)` has a useful finite-dimensional interpretation. Let

\[
g_j=L^*e_j
\qquad(1\le j\le N)
\tag{57}
\]

be the canonical evaluation representers inside `H`. Then

\[
E_M
=
\bigl((I-P_M)L^*\bigr)^*
\bigl((I-P_M)L^*\bigr).
\tag{58}
\]

Thus `E_M` is exactly the Gram matrix of the tail vectors

\[
(I-P_M)g_1,\ldots,(I-P_M)g_N.
\tag{59}
\]

In particular,

\[
\boxed{
\|E_M\|
=
\|(I-P_M)L^*\|^2.
}
\tag{60}
\]

This sharpens the approximation problem left by `NB-284`. To control the genuine finite-section penalty, one does **not** need a uniform approximation theorem for arbitrary vectors of the whole infinite quotient-source space. It is enough to control the finite-dimensional canonical representer span `ran L^*`, together with the conditioning of the finite sample map.

This is still not an oracle-free arithmetic estimate. The vectors `g_j=P_H k_{rho_j}` and the limiting Gram `K_infty` depend on the closed quotient-source space, which may itself be difficult to describe. The reduction says which finite-dimensional part of that closure matters; it does not make that part explicit for free.

There is nevertheless a fully source-section decomposition of the tail Gram. Define

\[
\Delta K_r
:=
K_{r+1}-K_r
=
L(P_{r+1}-P_r)L^*
\succeq0.
\tag{61}
\]

Because the nested projections converge strongly to the identity on `H` and the data space is finite dimensional,

\[
K_M\longrightarrow K_\infty
\quad\text{in operator norm}
\tag{62}
\]

for every fixed packet. Therefore

\[
\boxed{
E_M
=
\sum_{r=M}^{\infty}\Delta K_r
}
\tag{63}
\]

with operator-norm convergence.

Increasing the Dirichlet cutoff from `r` to `r+1` introduces at most one new quotient-source atom, so

\[
\operatorname{rank}(P_{r+1}-P_r)\le1,
\qquad
\operatorname{rank}(\Delta K_r)\le1.
\tag{64}
\]

Whenever the new atom is linearly independent of `V_r`, let `psi_{r+1}` be its normalized component orthogonal to `V_r`. Then

\[
P_{r+1}-P_r
=
\psi_{r+1}\otimes\psi_{r+1},
\tag{65}
\]

and

\[
\boxed{
\Delta K_r
=v_{r+1}v_{r+1}^*,
\qquad
v_{r+1}:=L\psi_{r+1}\in\mathbb C^N.
}
\tag{66}
\]

Thus the missing Gram is the accumulated first-free sampling energy of the **orthogonalized future Dirichlet source atoms**. This supplies a concrete source-native target for a later quantitative estimate: bound the tail sum of the rank-one sample increments, rather than approximate an arbitrary unknown feasible source.

---

## 6. A sharp two-factor criterion for the moving Ford regime

The exact split immediately yields a useful comparison. Since `E_M` is positive semidefinite,

\[
\|E_Ma\|^2
=a^*E_M^2a
\le
\|E_M\|\,a^*E_Ma
=
\|E_M\|\,\mathfrak T_M.
\tag{67}
\]

Also

\[
\mathfrak R_M
\le
\frac{\|E_Ma\|^2}{\lambda_{\min}(K_M)}.
\tag{68}
\]

Combining `(67)` and `(68)` gives

\[
\boxed{
\mathfrak T_M
\le
\mathfrak A_M
\le
\mathfrak T_M
\left(
1+
\frac{\|E_M\|}{\lambda_{\min}(K_M)}
\right).
}
\tag{69}
\]

Equivalently, define the two intrinsic section diagnostics

\[
\tau_M
:=
\|(I-P_M)L^*\|
=
\sqrt{\|E_M\|},
\tag{70}
\]

and

\[
\sigma_M
:=
\sigma_{\min}(L|_{V_M})
=
\sqrt{\lambda_{\min}(K_M)}.
\tag{71}
\]

Then

\[
\boxed{
\mathfrak A_M
\le
\mathfrak T_M
\left(1+\frac{\tau_M^2}{\sigma_M^2}\right).
}
\tag{72}
\]

For a moving Ford packet `Z_X` with legal cutoff `M_X`, this gives a concrete sufficient condition for the genuine finite-section penalty to vanish:

\[
\mathfrak T_{M_X}(Z_X)=o(1)
\tag{73}
\]

and

\[
\frac{\|E_{M_X}(Z_X)\|}
{\lambda_{\min}(K_{M_X}(Z_X))}
=O(1)
\tag{74}
\]

imply

\[
\boxed{
\mathfrak A_{M_X}(Z_X)=o(1).
}
\tag{75}
\]

Conversely, if `A_{M_X}` stays bounded below while `T_{M_X}->0`, then `(69)` forces

\[
\frac{\|E_{M_X}\|}
{\lambda_{\min}(K_{M_X})}
\longrightarrow\infty.
\tag{76}
\]

So a persistent finite-section obstruction with a compressible infinite minimizer would require a genuine collapse of finite sample stability relative to the remaining representer tail.

The data-aligned statement is sharper than `(76)`: the actual amplification is exactly

\[
(E_Ma)^*K_M^{-1}(E_Ma),
\tag{77}
\]

not the worst direction of `K_M^{-1}`. A small `lambda_min(K_M)` is therefore only a possible mechanism, not by itself a lower bound for the Nyman datum. The defect `E_Ma` must actually occupy the unstable sample direction.

This retains the target-aware warning that has run through the line since `NB-001`: condition numbers and Gram spectra alone do not settle a fixed target problem.

---

## 7. Fixed-packet convergence becomes quantitative

For fixed `Z`, the nested union of `V_M` is dense in `H`. Hence

\[
P_M\to I
\quad\text{strongly on }\mathcal H.
\tag{78}
\]

The range of `L^*` is finite dimensional, so strong convergence is uniform on its unit sphere. Consequently

\[
\|E_M\|
=
\|(I-P_M)L^*\|^2
\longrightarrow0.
\tag{79}
\]

At the same time

\[
K_M\to K_\infty
\tag{80}
\]

in matrix norm, and since `K_infty` is positive definite,

\[
\lambda_{\min}(K_M)
\longrightarrow
\lambda_{\min}(K_\infty)>0.
\tag{81}
\]

Therefore `(69)` gives

\[
\mathfrak A_M
\le
\mathfrak T_M(1+o(1)),
\tag{82}
\]

while `A_M>=T_M`. Thus, for every fixed packet,

\[
\boxed{
\mathfrak A_M(Z)
\sim
\mathfrak T_M(Z)
\qquad(M\to\infty)
}
\tag{83}
\]

unless the tail is eventually identically zero, in which case both sides are eventually zero.

This strengthens the qualitative convergence `(43)` of `NB-284`: asymptotically, at a fixed packet, the repair term is lower order than the direct representer-tail loss.

Indeed, from `(67)`--`(68)`,

\[
\frac{\mathfrak R_M}{\mathfrak T_M}
\le
\frac{\|E_M\|}{\lambda_{\min}(K_M)}
\to0
\tag{84}
\]

whenever `T_M>0`. The finite source space eventually becomes not only dense but stably able to repair the shrinking sample defect.

No such conclusion is uniform in moving packets, because both dimensions and sampling geometry vary with `X`.

---

## 8. Adversarial audit

### 8.1 This does not assume the infinite quotient-source closure equals a Blaschke subspace

Every operator above acts inside

\[
\mathcal H_Z^\infty.
\tag{85}
\]

No use is made of

\[
\mathcal H_Z^\infty=C_ZH^2
\tag{86}
\]

or of equality with ambient `H^2`. The persistent terms `G(Z)` and `S_infty(Z)` of `NB-284` remain untouched.

### 8.2 The Gram `K_infty` is not the ambient zero-sampling Gram

`K_infty=LL^*` uses evaluation representers projected into the closed quotient-source space. Replacing it silently by

\[
\left(\frac1{\rho_j+\overline{\rho_k}-1}\right)_{j,k}
\tag{87}
\]

would erase exactly the infinite-source restriction separated in `NB-284`. Formula `(87)` is valid for ambient `H^2`, not automatically for `H_Z^infty`.

### 8.3 Eventual feasibility is essential

Before `L|_{V_M}` is onto, `K_M` can be singular and the finite constrained problem can be infeasible. Equations using `K_M^{-1}` are asserted only after the eventual-surjectivity threshold supplied by `NB-282`. One could write pseudoinverse variants for feasible singular sections, but they add no information needed for the present moving-cutoff target.

### 8.4 A bad explicit Vandermonde is not an intrinsic obstruction

`NB-282` uses a sparse prime-power Vandermonde to prove realizability. Its coefficient norm may be huge. The present result shows that the intrinsic best repair constant is `(55)`. Therefore the conditioning of one constructive interpolation basis cannot be promoted to a lower bound without proving that it reflects `lambda_min(K_M)` itself.

### 8.5 Small representer tails do not suffice without sample stability

Even if `T_M` is tiny, the exact correction `(51)` can be large if `E_Ma` lies in a poorly sampled finite-section direction. This is why density alone gives no moving-packet rate.

### 8.6 Poor worst-case conditioning does not suffice either

Conversely, `lambda_min(K_M)` may be tiny while the actual defect `E_Ma` is nearly orthogonal to the unstable eigenspace. The exact data-aligned term `(77)`, not the condition number alone, determines the repair cost.

### 8.7 The rank-one increment representation does not make the tail automatically small

Equation `(66)` is an exact representation, not a decay estimate. The vectors `v_r=L psi_r` can decay slowly, concentrate coherently in one sample direction, or depend badly on the moving packet. Establishing a summable Ford-scale bound remains arithmetic work.

### 8.8 No RH assumption enters

The argument is Hilbert-space interpolation applied to the packet setup already fixed in `NB-284`. It neither assumes RH nor asserts the existence of off-line zeros. As before, selected zeros must lie strictly inside the half-plane where the evaluation functionals used in the setup are bounded.

### 8.9 The result is target-specific, not a theorem about all finite-section vectors

`T_M` uses the specific coefficient vector

\[
a=K_\infty^{-1}y,
\tag{88}
\]

associated with the canonical first-free datum. Bounds for the whole operator `E_M` are sufficient controls, but the exact penalty may be substantially smaller because of target alignment.

---

## 9. Prior-art audit

A fresh literature search was made around minimum-norm interpolation in reproducing-kernel Hilbert spaces, finite-dimensional interpolation operators, Gram inverses, and Nyman--Beurling Gram geometry.

The abstract facts used in Sections 2--4 are standard Hilbert/RKHS interpolation machinery: minimum-norm interpolation is represented by adjoint evaluation vectors, the data-space Gram controls the norm, and the Moore--Penrose right inverse is governed by the smallest singular value. Classical minimum-interpolation literature and modern representer-theorem treatments cover that generic framework. These facts are therefore not claimed as new.

The Nyman-specific search again surfaced work on Beurling--Nyman Gram structure and compressibility, but did not supply the particular finite-versus-closed-source decomposition `(8)` for the first-free quotient-source penalty isolated by `NB-284`. No external theorem is load-bearing here: all operator identities and estimates are derived above from the persisted Nyman setup. Accordingly no new entry is added to `SOURCES.md`.

The research contribution of this finding is the localization of `A_M` to the pair `(E_M,K_M)`, the exact orthogonal tail-plus-repair identity, and the resulting moving-packet criterion `(69)`--`(76)`. These are a refinement of the current Mathia research state, not a novelty claim for the underlying Hilbert-space algebra.

---

## 10. Next frontier

`NB-284` left two apparently separate quantitative tasks: find an approximation rate from the infinite quotient-source space into the finite source section, and control a finite right inverse uniformly. Equation `(8)` shows that both can be replaced by two sharper, canonical objects.

The first target is the missing representer Gram

\[
E_{M_X}(Z_X)
=
\sum_{r\ge M_X}\Delta K_r(Z_X),
\tag{89}
\]

or, more economically for the actual datum,

\[
\mathfrak T_{M_X}(Z_X)
=
a_X^*E_{M_X}(Z_X)a_X.
\tag{90}
\]

Because each increment is rank at most one, a useful source-side estimate could come from the first-free sample vectors of the orthogonalized future Dirichlet atoms.

The second target is the **data-aligned repair amplification**

\[
(E_{M_X}a_X)^*
K_{M_X}^{-1}
(E_{M_X}a_X).
\tag{91}
\]

A worst-case lower singular-value estimate is one route, but `(91)` makes clear that it is stronger than necessary. What matters is whether the particular missing-tail defect enters poorly sampled directions.

These two quantities give a decisive classification. If `(90)` tends to zero and `(91)` tends to zero under the legal Ford cutoff, then the genuine first-free finite-section penalty vanishes and this route cannot supply the missing coercivity. If either stays of order one, the surviving obstruction is no longer a vague statement about finite-section density: it has been localized to an explicit representer tail or to explicit sample-repair amplification.

---

## Conclusion

The finite-section term isolated by `NB-284` has an exact internal geometry. With `K_M=LP_ML^*`, `K_infty=LL^*`, `E_M=K_infty-K_M`, and `a=K_infty^{-1}y`,

\[
\boxed{
\mathfrak A_M
=
a^*E_Ma
+(E_Ma)^*K_M^{-1}(E_Ma).
}
\tag{92}
\]

The first term is the norm lost when the infinite minimum-norm interpolant is projected into the finite Dirichlet section. The second is the optimal price of repairing the exact first-free values lost by that projection.

For a fixed packet, the tail Gram tends to zero while the finite sample map becomes uniformly stable, so the repair is lower order and `A_M~T_M`. In a moving Ford packet, that uniformity can fail. The remaining arithmetic question is therefore sharply reduced to **compressibility of a finite set of canonical source-space evaluation representers and target-aligned stability of the finite sample map**.

This is narrower than an arbitrary approximation-rate problem and stronger than inspecting one explicit sparse interpolation basis. It identifies the two precise quantities that a genuine first-free finite-section obstruction must keep large.