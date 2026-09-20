# WI-371 — Desogus's corrected gamma floor has linearly growing negative index

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + LINEAR-NEGATIVE-INDEX + DECISIVE-REPAIR-BARRIER + NON-ESTABLISHED-RH`.

## Claim

WI-369 reconstructed the exact gamma-corrected odd archimedean block from Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* (`arXiv:2609.20367v1`) as

\[
\mathcal A_A+C_\Gamma I=R_A\succeq0,
\qquad
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\tag{1}
\]

where `R_A` is the sum of a screened difference form, a positive endpoint multiplier and a positive Hankel image. WI-369 proved that the form bottom tends to `-C_Gamma` by testing one fixed interior function. The same exact decomposition is much more rigid: the near-floor sector is not one-dimensional, nor merely of unbounded finite multiplicity. Its negative form index grows at least **linearly in `A`**.

Define the negative form index on the common core by

\[
\iota_0(A):=
\sup\left\{\dim V:
V\subset C_c^1(0,1),\ 
\mathcal A_A[f]<0\text{ for every }0\ne f\in V
\right\}.
\tag{2}
\]

Let

\[
M_2:=\int_0^\infty s^2h(s)\,ds
=7\zeta(3)+\frac{\pi^3}{4},
\qquad
C_1:=\frac{16\pi^2}{3}M_2,
\tag{3}
\]

with `h(s)=e^{-s/2}/(1-e^{-2s})`, as in WI-369, and put

\[
c_*:=\sqrt{\frac{C_\Gamma}{4C_1}}>0.
\tag{4}
\]

Then for all sufficiently large `A`,

\[
\boxed{
\iota_0(A)\ge \lfloor c_*A\rfloor.
}
\tag{5}
\]

Numerically `c_* = 0.0397278747...`, but no numerical approximation is used in the proof.

Consequently, any additive positive correction that makes the corrected archimedean block nonnegative must have genuinely growing complexity. More precisely:

- if `K_A\succeq0` and `rank(K_A)\le r` uniformly, then
  \[
  \iota_0(\mathcal A_A+K_A)\ge \lfloor c_*A\rfloor-r
  \tag{6}
  \]
  for all sufficiently large `A`;
- if `1\le p<\infty`, `K_A\succeq0`, and `\sup_A\|K_A\|_{\mathfrak S_p}\le M`, then
  \[
  \boxed{
  \iota_0(\mathcal A_A+K_A)
  \ge
  \lfloor c_*A\rfloor-
  \left(\frac{4M}{C_\Gamma}\right)^p
  }
  \tag{7}
  \]
  up to replacing the final real quantity by its integer floor/ceiling as appropriate;
- in particular, if `\mathcal A_A+K_A\succeq0` for all sufficiently large `A`, then necessarily
  \[
  \operatorname{rank}K_A\gtrsim A,
  \qquad
  \|K_A\|_{\mathfrak S_p}\gtrsim A^{1/p}
  \tag{8}
  \]
  for every finite `p` for which `K_A` belongs to that Schatten class;
- any single fixed compact positive operator `K` still leaves a linearly growing negative form index for `\mathcal A_A+K`.

Thus WI-370's scalar-budget obstruction is only the first manifestation of the corrected gamma problem. A successful repair cannot consist of a uniformly finite-dimensional collection of positive source/polar modes, a fixed compact positive correction, or an `A`-dependent positive correction of uniformly bounded finite Schatten norm. It must supply positive coercivity on a sector whose dimension itself grows on the `A` scale, or use a non-additive coupling that changes the bulk near-floor geometry.

This remains a repair barrier, not a disproof of the full Desogus program and not a result about RH. The paper's active arithmetic/source geometry grows with the localization scale, so it is not covered by a bounded-rank hypothesis merely because each fixed-`A` Schur block is finite-dimensional.

## 1. A sharper screened-difference estimate

WI-369 used the pointwise Lipschitz bound `|f(u)-f(v)|\le\|f'\|_\infty|u-v|` to make the screened difference remainder vanish for one fixed function. For a whole growing-dimensional subspace it is better to retain the `L^2` derivative.

For `0<t<1`, the fundamental theorem of calculus and Cauchy--Schwarz give

\[
|f(u+t)-f(u)|^2
\le
 t\int_u^{u+t}|f'(x)|^2\,dx.
\tag{9}
\]

Integrating over `0<u<1-t`, each `x` is counted for an interval of `u` of length at most `t`, hence

\[
\int_0^{1-t}|f(u+t)-f(u)|^2\,du
\le t^2\|f'\|_2^2.
\tag{10}
\]

Using symmetry in the first positive term of WI-369's exact identity,

\[
\begin{aligned}
D_A[f]
&:=\frac A2\iint h(A|u-v|)|f(u)-f(v)|^2\,du\,dv\\
&=A\int_0^1h(At)
  \int_0^{1-t}|f(u+t)-f(u)|^2\,du\,dt\\
&\le
A\|f'\|_2^2\int_0^1t^2h(At)\,dt\\
&\le
\boxed{\frac{M_2}{A^2}\|f'\|_2^2.}
\end{aligned}
\tag{11}
\]

This is an exact deterministic estimate on the common core. It is the step that turns the one-vector sharpness argument into an inertia statement with a quantitative dimension scale.

## 2. An explicit `m`-dimensional interior bulk space

Fix the interior interval `[1/4,3/4]`. For an integer `m\ge1`, partition it into `m` adjacent intervals `I_j=[a_j,a_j+\ell]` of equal length

\[
\ell=\frac1{2m}.
\tag{12}
\]

On each interval define

\[
\phi_j(u)=
\begin{cases}
\ell^{-1/2}\sqrt{\frac83}\,
\sin^2\!\left(\pi\frac{u-a_j}{\ell}\right),&u\in I_j,\\
0,&u\notin I_j.
\end{cases}
\tag{13}
\]

Because both the function and its first derivative vanish at the interval endpoints, `\phi_j\in C_c^1(0,1)`. The supports have disjoint interiors and

\[
\|\phi_j\|_2=1,
\qquad
\|\phi_j'\|_2^2
=\frac{4\pi^2}{3}\ell^{-2}
=\frac{16\pi^2}{3}m^2.
\tag{14}
\]

Hence the `m` functions are orthonormal. On

\[
V_m:=\operatorname{span}\{\phi_1,\ldots,\phi_m\},
\tag{15}
\]

the disjoint support also gives, for every `f\in V_m`,

\[
\boxed{
\|f'\|_2^2
=\frac{16\pi^2}{3}m^2\|f\|_2^2.
}
\tag{16}
\]

Combining (11) and (16), the screened difference contribution obeys

\[
D_A[f]\le C_1\frac{m^2}{A^2}\|f\|_2^2.
\tag{17}
\]

The other two positive pieces of `R_A` are uniformly negligible on this entire space because every function is supported in `[1/4,3/4]`. WI-369's exact formulas give

\[
\int\bigl(H(Au)+H(A(1-u))\bigr)|f(u)|^2du
\le 2H(A/4)\|f\|_2^2,
\tag{18}
\]

and, since `u+v\ge1/2` on the support and `\|f\|_1\le\|f\|_2`,

\[
0\le\langle f,J_Af\rangle
\le
\frac{Ae^{-A/4}}{1-e^{-A}}\|f\|_2^2.
\tag{19}
\]

Therefore

\[
0\le R_A[f]
\le
\left[
C_1\frac{m^2}{A^2}
+2H(A/4)
+\frac{Ae^{-A/4}}{1-e^{-A}}
\right]\|f\|_2^2.
\tag{20}
\]

## 3. Linear growth of the negative index

Choose

\[
m_A=\lfloor c_*A\rfloor,
\qquad
c_*^2=\frac{C_\Gamma}{4C_1}.
\tag{21}
\]

Then the first term in the brackets in (20) is at most `C_Gamma/4`. The remaining two terms tend to zero exponentially, so for all sufficiently large `A` their sum is at most `C_Gamma/4`. Thus on the whole space `V_{m_A}`,

\[
R_A[f]\le\frac{C_\Gamma}{2}\|f\|_2^2.
\tag{22}
\]

Using (1),

\[
\boxed{
\mathcal A_A[f]
\le -\frac{C_\Gamma}{2}\|f\|_2^2
\qquad(f\in V_{m_A}).
}
\tag{23}
\]

This proves (5). It also gives a stronger form-level statement than merely `\lambda_A\to-C_\Gamma`: for arbitrarily large `A` there is an explicit subspace of dimension proportional to `A` on which the entire corrected archimedean block remains uniformly below zero by a fixed amount.

No self-adjoint closure or discreteness assertion is needed. Everything above is a quadratic-form statement on `C_c^1(0,1)`.

## 4. Finite-rank and Schatten repair barriers

Let `K_A\succeq0` be a bounded positive operator on `L^2(0,1)`.

If `rank K_A\le r`, then

\[
\dim(V_{m_A}\cap\ker K_A)\ge m_A-r.
\tag{24}
\]

On this intersection `K_A` vanishes, while (23) remains strict. This proves (6). In particular, a positive additive correction making `\mathcal A_A+K_A` nonnegative must have rank at least `m_A`, hence rank `\Omega(A)`.

Now suppose `K_A\in\mathfrak S_p`, `1\le p<\infty`, with `\|K_A\|_{\mathfrak S_p}\le M`. Compress to `V_{m_A}`:

\[
B_A=P_{V_{m_A}}K_AP_{V_{m_A}}\succeq0.
\tag{25}
\]

Compression does not increase the Schatten norm. Therefore the number `q_A` of eigenvalues of `B_A` exceeding `C_Gamma/4` satisfies

\[
q_A\left(\frac{C_\Gamma}{4}\right)^p
\le\|B_A\|_{\mathfrak S_p}^p
\le M^p,
\tag{26}
\]

so

\[
q_A\le\left(\frac{4M}{C_\Gamma}\right)^p.
\tag{27}
\]

On the orthogonal complement of those `q_A` directions inside `V_{m_A}`, one has

\[
\langle f,K_Af\rangle
\le\frac{C_\Gamma}{4}\|f\|_2^2.
\tag{28}
\]

Together with (23), this leaves the total form at most `-C_Gamma/4`. Hence (7) follows.

There is also a direct necessary-norm formulation. If `\mathcal A_A+K_A\succeq0`, then (23) forces

\[
P_{V_{m_A}}K_AP_{V_{m_A}}
\succeq\frac{C_\Gamma}{2}I_{V_{m_A}},
\tag{29}
\]

and therefore

\[
\boxed{
\|K_A\|_{\mathfrak S_p}
\ge
\frac{C_\Gamma}{2}\,m_A^{1/p}.
}
\tag{30}
\]

This proves the second statement in (8) with an explicit constant.

Finally, let `K\succeq0` be one fixed compact operator. The spectral subspace of `K` for eigenvalues larger than `C_Gamma/4` has some finite dimension `N`. Intersecting its orthogonal complement with `V_{m_A}` leaves dimension at least `m_A-N`; on that intersection `K\preceq(C_Gamma/4)I`. Equation (23) again leaves a negative margin `-C_Gamma/4`. Thus a fixed compact positive correction cannot remove the growing negative sector.

## 5. Provenance and novelty audit

**Primary source under audit.** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, `arXiv:2609.20367v1`, submitted 17 September 2026, with supplementary material DOI `10.5281/zenodo.22799713`. The present result uses the gamma-corrected exact form reconstructed from that source in WI-369; it does not accept the preprint's RH conclusion as established.

**Internal exact dependencies.** WI-369 supplies (1), the exact functions `h,H`, positivity of the three remainder channels, and the moment identity (3). WI-370 supplies the separate scalar-budget obstruction. The new step here is to replace WI-369's `L^infinity` derivative estimate by the translation estimate (10), then build an explicit growing-dimensional interior subspace whose `H^1` cost is `O(m^2)`.

**Classical background.** The rank argument is finite-dimensional dimension counting. The Schatten estimate is the elementary eigenvalue-counting consequence of `\sum s_j(K)^p=\|K\|_{\mathfrak S_p}^p`; the fixed-compact conclusion is the corresponding finite-above-threshold property of compact positive operators. These are standard min--max/compact-perturbation mechanisms, not zeta-specific claims.

**Novelty audit.** The local Mathia trail contains earlier generic observations that fixed finite-rank or compact corrections cannot move an essential/infinite-dimensional obstruction (notably MI-029, MI-032 and WI-303), but none supplies this gamma-corrected form or the quantitative `Omega(A)` near-floor sector. A targeted audit of the Desogus source and the current `weil_inertia` findings did not locate this linear negative-index statement or the repair-complexity bounds (6)--(8). This is recorded as an audit result, not as a claim of historical priority.

## 6. Boundary and research consequence

The conclusion is deliberately about the **corrected odd archimedean block plus additive positive repairs**. It does not show that Desogus's complete source network has bounded rank, bounded trace, or bounded Schatten norm; in fact its active arithmetic/source space grows with the localization scale. Nor does it rule out an operator-valued Schur mechanism whose coupling changes the relevant subspace rather than simply adding an independent PSD correction.

What it does impose is a quantitative necessary condition on any such repair. The gamma error is not a single bad mode that can be patched by one scalar reserve or finitely many polar directions. The corrected block contains at least `c_*A+O(1)` independent interior directions with a fixed negative margin. Therefore any additive source/polar repair must act coercively on a linearly growing bulk sector; if encoded by a finite Schatten-class positive operator, its `S_p` mass must grow at least as `A^{1/p}`.

This sharpens the next test for the rooted/Schur route: determine the actual effective rank and singular-value budget of the source-conditioned positive correction on these explicit bulk spaces `V_{m_A}`. If that budget is sublinear in rank or uniformly finite in a Schatten class, the repaired Gate-II architecture is excluded. If it scales strongly enough, the remaining question is whether its range actually couples to the disjoint interior quasimodes rather than merely growing elsewhere in the source graph.
