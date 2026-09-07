# PF-211 — energy-normalized DtN gluing removes exterior amplification from the low-mode gate

**Status:** `LITERATURE+DERIVED + EXACT-BOUNDARY-FACTORIZATION + CONDITIONAL-APPLICATION + POSITIVE/ROUTE-NARROWING`. PF-209 shows that fixed-profile artificial-boundary corrections have the right nonendpoint Schatten order once they are localized, while PF-210 isolates a remaining global low-frequency target: per prime module, an unresolved exterior/interface sector of rank `O(1+a_n)` and operator norm `O(d_n)` is already globally weak trace class by prime-density counting. The norm part of that target does not require a separate low-frequency bound on the exterior Dirichlet-to-Neumann map. At the positive shifted resolvent `(Delta+1)^{-1}`, the standard interior/exterior Krein formula can be normalized by the **interior DtN energy** so that every exterior dependence is a positive contraction. After projecting any chosen finite-dimensional boundary low-frequency space *before* that contraction, the resulting native gradient-resolvent correction has rank at most the boundary rank and operator norm at most one. Inside the PF quadratic metric-resolvent word, the established seam coefficient `||F_n||_infty=O(d_n)` therefore supplies PF-210's `O(d_n)` norm automatically. Moreover, a fixed physical-frequency space on a one-dimensional module interface of length/component complexity `O(1+a_n)` has rank `O(1+a_n)`. Thus the low-mode part of PF-210 is reduced to an exact **module-scale placement/reassembly gate**, not an exterior-amplification estimate. The high-frequency complement is also protected from exterior amplification in every Schatten ideal, but its required uniform local Poisson-factor estimate still has to be proved in the actual PF buffer geometry.

## Claim

Let a complete smooth Riemannian surface be cut along a compact smooth interface `Sigma` into an interior buffer `Q` and an exterior `E`, and put

\[
L=\Delta+1.
\tag{1}
\]

Let `R` be the full resolvent `L^{-1}`, `R_Q^D` the Dirichlet resolvent on `Q`, and `K_Q` the Poisson operator solving

\[
Lu=0\quad\text{in }Q,
\qquad
u_D u=\varphi\quad\text{on }\Sigma.
\tag{2}
\]

Write `Lambda_Q,Lambda_E` for the positive-energy Dirichlet-to-Neumann forms on the two sides, with compatible outward-normal conventions, and

\[
S=\Lambda_Q+\Lambda_E.
\tag{3}
\]

The standard domain-decomposition/Krein formula has, up to the harmless sign fixed by the normal convention,

\[
R|_Q-R_Q^D
=K_QS^{-1}K_Q^*.
\tag{4}
\]

All square roots below are understood in the boundary energy rigging defined by the positive closed form `Lambda_Q`; this avoids pretending that the Sobolev trace maps are unbounded operators on one raw `L^2(Sigma)` space. Define

\[
A:=\nabla K_Q\Lambda_Q^{-1/2},
\qquad
M:=K_Q\Lambda_Q^{-1/2},
\tag{5}
\]

and

\[
D:=\Lambda_Q^{1/2}S^{-1}\Lambda_Q^{1/2}.
\tag{6}
\]

The energy identity for the Poisson extension is

\[
\langle\Lambda_Q\varphi,\varphi\rangle
=
\|\nabla K_Q\varphi\|_2^2
+
\|K_Q\varphi\|_2^2.
\tag{7}
\]

Consequently

\[
\boxed{
A^*A+M^*M=I,
\qquad
\|A\|\le1,
\qquad
\|M\|\le1.
}
\tag{8}
\]

Since `Lambda_E>=0`, form order gives `S>=Lambda_Q`; inverse monotonicity therefore gives

\[
\boxed{
0\le D\le I.
}
\tag{9}
\]

Taking one gradient in (4), equations (5)--(6) give the exact normalized factorization

\[
\boxed{
\nabla(R|_Q-R_Q^D)=A D M^*.
}
\tag{10}
\]

Let `P` be any orthogonal projection of rank `r` in the normalized boundary energy space and split

\[
C_{\rm lo}:=ADPM^*,
\qquad
C_{\rm hi}:=AD(I-P)M^*.
\tag{11}
\]

Then

\[
\boxed{
\operatorname{rank}C_{\rm lo}\le r,
\qquad
\|C_{\rm lo}\|\le1.
}
\tag{12}
\]

Moreover, for every Schatten exponent `p>0` for which the right side is finite,

\[
\boxed{
\|C_{\rm hi}\|_{\mathcal S_p}
\le
\|(I-P)M^*\|_{\mathcal S_p}.
}
\tag{13}
\]

Thus the exterior DtN map cannot amplify either the low-sector operator norm or the high-sector singular values after energy normalization. It may mix boundary modes through `D`, but bounded left multiplication cannot increase rank or a Schatten norm once the low/high split has already been inserted on the right of `D`.

Now let `g,h` be the two PF source/target metrics, apply (10)--(13) separately to each metric, and consider one quadratic metric-resolvent word

\[
T=G_h^*M_FG_g,
\qquad
G_k=\nabla(\Delta_{g_k}+1)^{-1}.
\tag{14}
\]

Spectral calculus gives the metric-independent operator bound

\[
\|G_k\|
\le
\sup_{\lambda\ge0}
\frac{\sqrt\lambda}{1+\lambda}
=\frac12.
\tag{15}
\]

Replacing either gradient resolvent in (14) by its low boundary-recoupling piece therefore produces a finite-rank operator `E_lo` satisfying

\[
\boxed{
\operatorname{rank}E_{\rm lo}
\le C(r_g+r_h),
\qquad
\|E_{\rm lo}\|
\le C\|F\|_\infty,
}
\tag{16}
\]

where the constant is absolute up to the fixed finite expansion into left/right/double recoupling terms. In particular, for the PF-205--PF-210 seam coefficient

\[
\|F_n\|_\infty\le C d_n,
\tag{17}
\]

we obtain

\[
\boxed{
\|E_{n,\rm lo}\|\le C d_n.
}
\tag{18}
\]

Equation (18) is the norm hypothesis of PF-210. No independent estimate of the exterior low-frequency DtN inverse is needed.

Finally suppose the unresolved global-to-buffer correction is placed on a module-scale one-dimensional interface `Sigma_n`. Let `L_n` be its total arclength and `m_n` its number of connected components. For a fixed physical tangential-frequency cutoff `kappa`, let `V_{n,kappa}` be the span of the boundary Laplacian modes with frequency at most `kappa`, and let `P_n` be the energy-orthogonal projection onto the same finite-dimensional subspace. Elementary one-dimensional eigenvalue counting gives

\[
\boxed{
\operatorname{rank}P_n
\le C\bigl(m_n+\kappa L_n\bigr).
}
\tag{19}
\]

For circles this is the literal Fourier-mode count; for intervals the Dirichlet/Neumann count gives the same bound. Hence any PF module interface satisfying

\[
m_n+L_n=O(1+a_n)
\tag{20}
\]

has, at fixed `kappa`,

\[
\boxed{
\operatorname{rank}E_{n,\rm lo}=O(1+a_n),
\qquad
\|E_{n,\rm lo}\|=O(d_n).
}
\tag{21}
\]

These are exactly PF-210's per-module hypotheses. Therefore, once the actual PF global-to-buffer architecture places the low sector on such module interfaces and supplies the same finite-color/two-sided block organization required by PF-210, the entire low-frequency family is in `S_{1,infinity}` by the prime-density threshold count already proved there.

## 1. Why the exterior disappears from the norm estimate

The key point is not an unnormalized inequality such as `S^{-1}<=Lambda_Q^{-1}` by itself. That inequality can be useless on a shrinking low boundary mode because `Lambda_Q^{-1}` may be large. The useful object is the **energy-normalized Schur complement** `D` in (6). Equation (7) normalizes the Poisson operator and its gradient simultaneously, while (9) makes the exterior factor a contraction between them.

This is exactly the structure of a Schur-complement/domain-decomposition formula. The exterior can have complicated global geometry and a difficult low-frequency DtN response, but at the fixed positive spectral point its contribution enters as additional nonnegative boundary energy. After conjugation by the interior energy, it cannot have norm larger than one.

The placement of `P` in (11) is essential. Since it occurs before `D` acts, arbitrary exterior mixing of the selected low boundary space does not increase its dimension: `ADP` has rank at most `rank P`. The same observation is what makes (13) robust: the high-frequency singular-value decay is charged entirely to `(I-P)M^*`, while `A` and `D` are only contractions.

## 2. PF-210's low-mode norm is supplied by the metric coefficient

PF-210 deliberately stated its low-mode hypothesis at the level of the unresolved **quadratic resolvent contribution**, not at the level of a bare scalar resolvent correction. Equation (10) explains why this distinction matters.

A normalized boundary correction `C_lo` need only have operator norm `O(1)`. The PF metric defect already contributes

\[
\|F_n\|_\infty=O(d_n),
\]

and the remaining gradient-resolvent factor is uniformly bounded by (15). Therefore every low left/right/double-recoupling term has norm `O(d_n)` without asking the exterior DtN operator itself to carry a factor `d_n`.

This removes one possible over-demand from the PF-209/PF-210 handoff. The native exterior analysis does **not** have to prove both a small DtN response and a small metric coefficient. The coefficient is already the small factor; the exterior must only be organized so that the low boundary sector has module-scale rank and the complementary high sector retains the local ideal control.

## 3. A finite-dimensional falsifier: positivity alone does not make the whole correction small

The preceding factorization must not be misread as saying `AD M^*=O(d_n)` or `O(w_n)` before the coefficient is inserted. There is a sharp algebraic reason.

For `0<epsilon<1`, on `C^2` set

\[
A_\epsilon=
\begin{pmatrix}
\epsilon&0\\
0&\sqrt{1-\epsilon^2}
\end{pmatrix},
\qquad
M_\epsilon=
\begin{pmatrix}
\sqrt{1-\epsilon^2}&0\\
0&\epsilon
\end{pmatrix}.
\tag{22}
\]

Then

\[
A_\epsilon^*A_\epsilon+M_\epsilon^*M_\epsilon=I,
\qquad
\|A_\epsilon M_\epsilon^*\|
=\epsilon\sqrt{1-\epsilon^2}
=O(\epsilon).
\tag{23}
\]

Let `P_v` be the orthogonal projection onto `v=(1,1)/sqrt2` and fix `0<delta<1`:

\[
D_\delta=\delta I+(1-\delta)P_v.
\tag{24}
\]

Then `0<D_delta<=I`, but

\[
\liminf_{\epsilon\downarrow0}
\|A_\epsilon D_\delta M_\epsilon^*\|
\ge\frac{1-\delta}{2}>0.
\tag{25}
\]

Because `D_delta` is invertible and contractive, it can algebraically be written as

\[
D_\delta=(I+E_\delta)^{-1},
\qquad
E_\delta=D_\delta^{-1}-I\ge0.
\tag{26}
\]

Thus the sole information `D=(I+E)^{-1}` with `E>=0` does not preserve the smallness of the aligned product `AM^*`; a positive contraction may mix a low `M` mode into a gradient-active `A` mode. This two-dimensional model is **not** asserted to be a geometric DtN realization. Its purpose is narrower and exact: a proof based only on Loewner positivity cannot establish the full unprojected small-scale Schatten estimate.

Equations (11)--(13) are the repair. Isolate the finite-dimensional low space before the contraction, pay for it with PF-210's rank counting, and estimate the complementary singular values on the local Poisson factor where elliptic boundary calculus actually applies.

## 4. Prior art and novelty audit

The boundary machinery used here is classical.

- G. Grubb, *The mixed boundary value problem, Krein resolvent formulas and spectral asymptotic estimates*, Journal of Mathematical Analysis and Applications **382** (2011), 339--363, DOI `10.1016/j.jmaa.2011.04.055`, arXiv:1104.0785, gives Krein resolvent formulas and boundary-dimensional singular-value asymptotics for elliptic boundary-condition changes. PF-209 already uses this source for the fixed-buffer singular Green order.
- J. Behrndt, M. M. Malamud, H. Neidhardt, *Scattering matrices and Dirichlet-to-Neumann maps*, Journal of Functional Analysis **273** (2017), 1970--2025, DOI `10.1016/j.jfa.2017.06.001`, arXiv:1511.02376, treats Schrödinger operators on exterior domains and orthogonal interior/exterior couplings. In its hypersurface decomposition the boundary Weyl operator is explicitly built from the **sum of the interior and exterior Dirichlet-to-Neumann maps**, matching the structural denominator in (3)--(4).

No novelty is claimed for Krein formulas, DtN positivity, inverse monotonicity, Poisson energy identities, one-dimensional boundary-mode counting, or ideal stability under bounded multiplication. The project-specific derived step is their combination with the PF quadratic gradient-resolvent word and PF-210's prime-density counting: after interior-energy normalization, the exterior no longer needs a separate `O(d_n)` low-mode estimate, because the PF coefficient supplies that factor and the boundary projection supplies the rank.

The finite-dimensional example (22)--(26) is an elementary falsifier, not a new operator-theory theorem. It records why the stronger tempting claim — that positivity alone makes the **whole** native correction inherit the local small-scale bound — is unsupported.

A structure-directed literature search did not reveal a source stating this prime-density/module-rank organization; the underlying analytic pieces are standard and the novelty claim is therefore limited to the Mathia-specific reduction of the PF-209/PF-210 gate.

## 5. Boundary conditions and remaining falsifiers

The claim requires the positive shifted problem. At `Delta+1`, the interior and exterior Poisson problems are coercive in the energy form used in (7), so the normalized factorization is meaningful. A threshold or on-spectrum scattering parameter would require a different limiting-absorption analysis and is not covered here.

The interface must be smooth enough for the standard trace/Poisson/DtN framework. Corners may be treatable, but no uniform corner calculus is asserted. Multiple components are allowed; their number appears explicitly in (19).

Equation (20) is a **placement hypothesis**, not silently established geometry. A future native PF buffer construction must verify that the low-frequency projection is taken on a module-scale interface whose total length and component count are `O(1+a_n)`. Cutting every natural-width seam cell independently and assigning one uncontrolled low mode per cell would instead produce the forbidden `O(a_n/d_n)` rank scale identified by PF-210.

The high complement is not closed by (13) alone. One still needs a uniform estimate on `(I-P_n)M_n^*` in the Schatten class required by the PF-209 quadratic expansion, with the correct physical scaling through the actual module/buffer family. The value of (13) is that **this estimate is purely local/interior after normalization**: no additional exterior amplification constant can appear.

Finally, PF-210's global weak-trace conclusion still needs its two-sided orthogonal block or fixed finite-color reassembly hypothesis. Rank and norm bounds for isolated modules do not create that support structure automatically.

## 6. Consequence for the current prime-flute frontier

PF-209 left the global exterior/interface map as a possible source of low-frequency loss. PF-210 showed that a logarithmic number of `O(d_n)` low modes per prime module would already be harmless. PF-211 removes the need to obtain the `O(d_n)` factor from the exterior map itself:

\[
\boxed{
\text{positive DtN gluing}
+\text{ boundary-energy normalization}
+\text{ module low projection}
\Longrightarrow
\operatorname{rank}=O(1+a_n),\ \|\cdot\|=O(d_n)
}
\tag{27}
\]

whenever the native module interface satisfies (20). The exterior contributes only the contraction `D` and cannot worsen the high-sector Schatten norm either.

The next discriminating task is therefore narrower than PF-210 stated it. Construct the actual **module-scale** native global-to-buffer boundary decomposition, verify (20), choose a fixed physical-frequency projection before the normalized exterior contraction, and prove the complementary local Poisson factor has PF-209's required uniform nonendpoint Schatten scaling. If the resulting module pieces also admit PF-210's finite-color/two-sided reassembly, the smooth-seam exterior gate closes. If the native geometry forces cell-scale rather than module-scale low-mode multiplicity, or the high Poisson factor loses the physical seam scale, the route fails at an explicit remaining location.

This is still an operator-equivalence/control result shared by the exact prime flute and an appropriate matched clone. It supplies no prime/clone separator, determinant formula, explicit-formula term, or RH implication by itself.
