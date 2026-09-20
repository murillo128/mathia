# WI-372 — The gamma bulk forces a full spectral profile on every additive repair

**Status:** `EXACT-DERIVED + CLASSICAL-SPECTRAL-MINMAX + STRICT-SCHATTEN-STRENGTHENING + SOURCE-SINGULAR-VALUE-GATE + DECISIVE-REPAIR-BARRIER + NON-ESTABLISHED-RH`.

## Claim

WI-371 proves that the corrected odd archimedean block from Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* (`arXiv:2609.20367v1`) has a depth-resolved family of negative subspaces. With

\[
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\qquad
M_2=7\zeta(3)+\frac{\pi^3}{4},
\tag{1}
\]

and

\[
c_\eta=
\frac1\pi\sqrt{\frac{C_\Gamma-\eta}{M_2}},
\qquad 0<\eta<C_\Gamma,
\tag{2}
\]

WI-371 establishes

\[
\liminf_{A\to\infty}\frac{\iota_\eta(\mathcal A_A)}A
\ge c_\eta.
\tag{3}
\]

The same information forces substantially more than the rank and one-threshold Schatten bounds recorded there.

Let `K_A` be any bounded self-adjoint additive correction in the same Hilbert geometry such that

\[
\mathcal A_A+K_A\succeq0.
\tag{4}
\]

For `t>0`, define its positive spectral counting function

\[
N_A^+(t)
:=
\dim\operatorname{Ran}\mathbf 1_{[t,\infty)}(K_A),
\tag{5}
\]

allowing the value `+infinity`. Then for every fixed `0<t<C_Gamma`,

\[
\boxed{
\liminf_{A\to\infty}\frac{N_A^+(t)}A
\ge
\frac1\pi\sqrt{\frac{C_\Gamma-t}{M_2}}.
}
\tag{6}
\]

Thus the repair requirement is a **full positive spectral distribution law**, not merely a bulk-rank requirement at depth zero.

When `K_A` is compact, list its positive eigenvalues in non-increasing order as

\[
\kappa_{A,1}\ge\kappa_{A,2}\ge\cdots>0,
\tag{7}
\]

padding by zeros when necessary. Put

\[
c_{\rm bulk}
=\frac1\pi\sqrt{\frac{C_\Gamma}{M_2}}
=0.1834951935083428577\ldots .
\tag{8}
\]

Then for every fixed `0<alpha<c_bulk`,

\[
\boxed{
\liminf_{A\to\infty}
\kappa_{A,\lceil\alpha A\rceil}
\ge
C_\Gamma-\pi^2M_2\alpha^2.
}
\tag{9}
\]

In particular an additive repair cannot satisfy the rank condition from WI-371 by supplying an arbitrarily weak cloud of nonzero eigenvalues. A positive-density initial segment of its spectrum must remain quantitatively bounded away from zero, with the explicit parabolic lower envelope (9).

There is also a strict strengthening of WI-371's Schatten lower bound. If `K_A in S_p`, `1<=p<infinity`, then

\[
\boxed{
\liminf_{A\to\infty}
A^{-1/p}\|K_A\|_{\mathfrak S_p}
\ge
\tau_p,
}
\tag{10}
\]

where

\[
\boxed{
\tau_p
:=
\left[
\frac{p\,C_\Gamma^{p+1/2}}{\pi\sqrt{M_2}}
B\!\left(p,\frac32\right)
\right]^{1/p}.
}
\tag{11}
\]

This is strictly larger than the one-threshold constant `sigma_p` in WI-371 for every finite `p>=1`. Numerically,

\[
\tau_1=0.6571798907154163\ldots
\quad\text{versus}\quad
\sigma_1=0.3794229868105544\ldots,
\tag{12}
\]

and

\[
\tau_2=1.6805929697222691\ldots
\quad\text{versus}\quad
\sigma_2=1.2311491353204316\ldots .
\tag{13}
\]

Finally, if an additive positive repair factors as

\[
K_A=B_A^*B_A
\tag{14}
\]

with `B_A` compact, then (6)--(9) become direct singular-value requirements on the source/coupling map:

\[
\#\{j:s_j(B_A)\ge\sqrt t\}
\ge (c_t-o(1))A
\tag{15}
\]

for every fixed `0<t<C_Gamma`, and

\[
\boxed{
\liminf_{A\to\infty}
 s_{\lceil\alpha A\rceil}(B_A)
\ge
\sqrt{C_\Gamma-\pi^2M_2\alpha^2}
}
\tag{16}
\]

for `0<alpha<c_bulk`. More generally, if

\[
K_A=B_A^*W_AB_A,
\qquad 0\preceq W_A\preceq M I
\tag{17}
\]

with one fixed finite `M`, the right-hand side of (16) is divided by `sqrt(M)`.

This gives a precise version of the source-conditioned gate left open by WI-371: an additive factorized source repair must have not only `Omega(A)` effective rank, but `Omega(A)` singular directions following an explicit non-vanishing strength profile.

## 1. Spectral counting from the depth-resolved negative index

Fix `0<t<C_Gamma`. By WI-371, for arbitrarily small fixed loss in the asymptotic coefficient and all sufficiently large `A`, there is a subspace `V_A` of dimension `d_A` such that

\[
\mathcal A_A[f]\le-t\|f\|_2^2
\qquad(f\in V_A),
\tag{18}
\]

and

\[
\liminf_{A\to\infty}\frac{d_A}{A}\ge c_t.
\tag{19}
\]

Positivity of the repaired form gives

\[
\langle f,K_Af\rangle\ge t\|f\|_2^2
\qquad(f\in V_A).
\tag{20}
\]

Let

\[
E_A^+(t)=\mathbf1_{[t,\infty)}(K_A).
\tag{21}
\]

If `dim Ran E_A^+(t)<d_A`, then the restriction of `E_A^+(t)` to `V_A` has nontrivial kernel. Hence there is a nonzero `f in V_A` whose spectral measure for `K_A` is supported in `(-infinity,t)`. The spectral theorem then gives the strict inequality

\[
\langle f,K_Af\rangle<t\|f\|_2^2,
\tag{22}
\]

contradicting (20). Therefore

\[
N_A^+(t)\ge d_A.
\tag{23}
\]

Taking the lower limit proves (6). This is just the max--min principle expressed through spectral projections; no new operator-theoretic lemma is being claimed.

## 2. Inverting the count gives a repair eigenvalue curve

Assume now that `K_A` is compact. Fix `0<alpha<c_bulk` and define

\[
q(\alpha)
:=
C_\Gamma-\pi^2M_2\alpha^2>0.
\tag{24}
\]

For every `t<q(alpha)`, equation (2) gives

\[
c_t>\alpha.
\tag{25}
\]

By (6), for all sufficiently large `A`,

\[
N_A^+(t)\ge\lceil\alpha A\rceil.
\tag{26}
\]

Thus

\[
\kappa_{A,\lceil\alpha A\rceil}\ge t.
\tag{27}
\]

Letting `t` increase to `q(alpha)` proves (9).

The resulting profile is worth separating from the cruder rank statement. WI-371 obtains the zero-depth limit

\[
\operatorname{rank}K_A\ge(c_{\rm bulk}-o(1))A.
\tag{28}
\]

Equation (9) says that for every fraction `alpha` strictly below that endpoint, the corresponding repair eigenvalue must stay above the explicit positive level `q(alpha)`. Only as `alpha` approaches `c_bulk` can the lower envelope decay to zero.

## 3. Integrating the whole profile strengthens every finite Schatten bound

Suppose `K_A in S_p`. Since `K_A` is self-adjoint,

\[
\|K_A\|_{\mathfrak S_p}^p
=\operatorname{Tr}|K_A|^p
\ge\operatorname{Tr}(K_A)_+^p.
\tag{29}
\]

The standard layer-cake identity for the positive compact spectrum is

\[
\operatorname{Tr}(K_A)_+^p
=
 p\int_0^\infty t^{p-1}N_A^+(t)\,dt.
\tag{30}
\]

Take any sequence `A_n -> infinity`. After division by `A_n`, Fatou's lemma and (6) give

\[
\begin{aligned}
\liminf_{n\to\infty}
\frac{\|K_{A_n}\|_{\mathfrak S_p}^p}{A_n}
&\ge
p\int_0^{C_\Gamma}
 t^{p-1}c_t\,dt\\
&=
\frac{p}{\pi\sqrt{M_2}}
\int_0^{C_\Gamma}
 t^{p-1}(C_\Gamma-t)^{1/2}\,dt\\
&=
\frac{p\,C_\Gamma^{p+1/2}}{\pi\sqrt{M_2}}
B\!\left(p,\frac32\right).
\end{aligned}
\tag{31}
\]

Because the original sequence was arbitrary, (10)--(11) follow.

This strictly improves the threshold optimization in WI-371. There the `p`-th power of the normalized lower constant is

\[
\sigma_p^p
=
\max_{0<t<C_\Gamma}t^pc_t.
\tag{32}
\]

By contrast,

\[
\tau_p^p
=
\int_0^{C_\Gamma}p t^{p-1}c_t\,dt.
\tag{33}
\]

For every fixed `x in (0,C_Gamma)`, strict monotonicity of `c_t` gives

\[
\int_0^xpt^{p-1}c_t\,dt
>
c_x\int_0^xpt^{p-1}\,dt
=x^pc_x.
\tag{34}
\]

Hence the full integral in (33) is strictly larger than the maximum in (32), proving `tau_p>sigma_p` without numerical comparison.

For `p=1`, the improvement is especially transparent:

\[
\tau_1
=
\frac{2C_\Gamma^{3/2}}{3\pi\sqrt{M_2}}
=\sqrt3\,\sigma_1.
\tag{35}
\]

## 4. Factorized source maps must transmit a bulk singular-value profile

If `K_A=B_A^*B_A`, the positive eigenvalues of `K_A` are the squared singular values of `B_A`. Equations (6) and (9) therefore immediately give (15)--(16).

For the weighted factorization (17),

\[
0\preceq K_A\preceq M B_A^*B_A.
\tag{36}
\]

The min--max principle then gives, eigenvalue by eigenvalue,

\[
\kappa_{A,j}(K_A)
\le M s_j(B_A)^2.
\tag{37}
\]

Combining (37) with (9) gives

\[
\liminf_{A\to\infty}
 s_{\lceil\alpha A\rceil}(B_A)
\ge
\sqrt{\frac{C_\Gamma-\pi^2M_2\alpha^2}{M}}.
\tag{38}
\]

This is the precise additional information that nominal source-coordinate counting does not provide. A source family may have dimension proportional to `A` and still fail (38) if most of its directions couple only weakly to the gamma-negative bulk.

No claim is made here that Desogus's full common-cut/rooted-Schur source network reduces to (17) with a uniformly bounded `W_A`. WI-361 emphasizes that the proposed mechanism uses a nontrivial common-complement short and true-metric Schur induction. Equations (15)--(38) are therefore a **necessary gate for additive/factorized repairs**, not a refutation of the actual Gate II architecture.

## 5. Prior-art and novelty audit

**Internal dependency.** The only nonclassical input is WI-371's depth profile (3), itself derived from WI-369's independently reconstructed gamma-corrected archimedean block and the one-dimensional Dirichlet-band estimate. WI-371 already records the rank bound and the optimized one-threshold Schatten constant. It does not integrate the family over all depths, state the spectral counting law (6), invert it to the eigenvalue envelope (9), or formulate the factorized singular-value gate (16).

A targeted search of the local `weil_inertia` corpus for layer-cake/Schatten counting and repair eigenvalue-counting statements found no prior finding with this full profile. The current Desogus preprint is prior art for the source-exact rooted-Schur architecture, not for this negative-index repair distribution; WI-371's primary-source audit found no `negative index`, `Schatten`, or `bulk` statement in v1.

**Classical operator theory.** The passage from a uniformly positive compression to a lower bound on the positive spectral counting function is Courant--Fischer/min--max theory. The identity (30) is the standard distribution-function representation of Schatten moments. Ky Fan eigenvalue inequalities and standard matrix/operator-analysis texts contain the surrounding spectral technology. None of those ingredients is claimed as new.

The durable contribution here is the exact specialization of those classical principles to WI-371's gamma depth profile, yielding the explicit count curve (6), quantile curve (9), integrated Schatten constant (11), and source singular-value gate (16). No historical priority claim is made.

## 6. Boundary, falsification test, and research consequence

This finding remains entirely inside the corrected **odd archimedean gamma block plus bounded self-adjoint additive repair** model. It does not prove that the complete Weil form has a linearly growing negative index, does not prove that Desogus's arithmetic source network has insufficient rank or coupling, and does not establish or refute RH.

The result is exact conditional on WI-371's established local depth profile. Its falsification surface is correspondingly narrow: an error would have to occur in the spectral-projection dimension argument (18)--(23), the inversion (24)--(27), or the layer-cake/Fatou passage (29)--(34). These are classical consequences with no numerical certificate or asymptotic interchange beyond Fatou's lemma.

For the live source audit, the useful gate is now sharper than `rank = Omega(A)`. Any proposed additive/factorized rescue of the corrected gamma block should be tested against the full curve

\[
\boxed{
\alpha\longmapsto
C_\Gamma-\pi^2M_2\alpha^2,
\qquad 0<\alpha<c_{\rm bulk}.
}
\tag{39}
\]

If the source-conditioned correction has fewer than `alpha A` directions above that strength at any fixed `alpha<c_bulk`, it cannot make the gamma block nonnegative. Conversely, satisfying this necessary profile would not prove positivity because the actual source directions must also overlap the correct negative subspaces in the common form geometry.

This turns the next audit question from a nominal dimension count into a quantitative overlap/singular-value problem: estimate the singular spectrum of the source-conditioned map on the interior Dirichlet bulk, or show that the rooted Schur/common-cut mechanism is genuinely non-additive in a way that evades the model rather than merely supplying a weak positive perturbation.
