# PC-414 — arbitrary conductor-only descendant tensors factor through a rank-one source channel

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for source-independent conductor-only readouts applied after the PC-405 descendant reduction. No multiplicativity, Euler product, prime-locality, sparsity, or bounded matrix rank is required. In particular, a kernel may couple valuations at different rational primes and may be an arbitrary dense matrix at each finite cutoff. The Prime-Circle source still enters each fixed Mellin frequency through a one-dimensional channel, so every bilinear or fixed-arity multilinear conductor tensor pulls back to an outer source factor times a universal conductor contraction. A matched arbitrary-profile control reproduces the entire conductor factor exactly.

This closes the first surviving boundary stated in PC-413 for **cross-prime conductor kernels**, and also shows that merely letting the support or rank of such a source-independent conductor operator grow with the cutoff does not repair source identifiability. It does **not** cover tensors derived from the embedded roots/chords/old-new geometry before conductor scalarization, nonlinear laws that change the descendant state itself, or constructions in which the source and conductor operator are coupled before the PC-405 Mellin reduction.

## 1. The descendant map is rank one in the source variable

PC-405 and the subsequent descendant findings use the exact frequencywise law

\[
\widehat{h_{nm}}(t)
=
c_{n,m}(t)\widehat h_n(t),
\tag{1}
\]

where the coefficient \(c_{n,m}(t)\) is fixed by the refinement/descendant law. PC-413 exploited the multiplicative structure of \(c_{n,m}\) to classify prime-local two-label kernels. For the present obstruction, no arithmetic factorization of \(c_{n,m}\) is needed.

Fix a finite conductor set \(I_N\subset\mathbb N\), for example \(I_N=\{1,\ldots,N\}\), and write

\[
c_{n}^{(N)}(t)
=
\bigl(c_{n,m}(t)\bigr)_{m\in I_N}.
\tag{2}
\]

The map from one source Mellin amplitude to the full descendant vector is

\[
D_{n,t}^{(N)}:\mathbb C\longrightarrow \mathbb C^{I_N},
\qquad
z\longmapsto z\,c_n^{(N)}(t).
\tag{3}
\]

Hence

\[
\boxed{\operatorname{rank}D_{n,t}^{(N)}\le 1.}
\tag{4}
\]

This is the structural fact that survives after forgetting the Euler-product representation. All conductor coordinates at a fixed frequency are scalar multiples of the same source amplitude.

## 2. Arbitrary cross-prime bilinear kernels still separate exactly

Let

\[
W_N(t,u)
=
\bigl(W_{m,k}^{(N)}(t,u)\bigr)_{m,k\in I_N}
\tag{5}
\]

be an arbitrary complex matrix chosen independently of the Prime-Circle source profile. It may depend on \(n,N,t,u\), on the complete prime factorizations of \(m,k\), and on relations between different rational primes. No assumption analogous to the primewise product

\[
W(m,k)=\prod_p w_p(v_p(m),v_p(k))
\]

from PC-413 is imposed.

Define the bilinear descendant response

\[
\mathcal A_{h,W}^{(N)}(t,u)
=
\sum_{m,k\in I_N}
W_{m,k}^{(N)}(t,u)\,
\widehat{h_{nm}}(t)\,
\overline{\widehat{h_{nk}}(u)}.
\tag{6}
\]

Substituting (1) gives the exact factorization

\[
\boxed{
\mathcal A_{h,W}^{(N)}(t,u)
=
\widehat h_n(t)\,
\overline{\widehat h_n(u)}\,
K_{n,W}^{(N)}(t,u),
}
\tag{7}
\]

where

\[
\boxed{
K_{n,W}^{(N)}(t,u)
=
\sum_{m,k\in I_N}
W_{m,k}^{(N)}(t,u)\,
c_{n,m}(t)\,
\overline{c_{n,k}(u)}.
}
\tag{8}
\]

Equations (7)--(8) require no convergence argument because they are finite identities. They remain true for a completely nonfactorizable cross-prime matrix. For example, \(W_{m,k}\) may explicitly compare \(v_p(m)\) with \(v_q(k)\) for \(p\ne q\), couple radicals or complete factorization patterns, or be a dense matrix with no arithmetic product structure at all.

Thus the loophole left deliberately open by PC-413 is real only if the cross-prime kernel carries **additional source-derived geometry**. Cross-prime dependence by itself does not help.

## 3. Matched-control blindness is exact before any Euler product

Let \(g_n\) be an arbitrary Mellin-tame noncyclotomic base profile and propagate it by the same descendant law,

\[
\widehat{g_{nm}}(t)
=
c_{n,m}(t)\widehat g_n(t).
\tag{9}
\]

Then the identical calculation gives

\[
\mathcal A_{g,W}^{(N)}(t,u)
=
\widehat g_n(t)\,
\overline{\widehat g_n(u)}\,
K_{n,W}^{(N)}(t,u).
\tag{10}
\]

At frequencies where the outer amplitudes are nonzero,

\[
\boxed{
\frac{\mathcal A_{h,W}^{(N)}(t,u)}
{\widehat h_n(t)\overline{\widehat h_n(u)}}
=
\frac{\mathcal A_{g,W}^{(N)}(t,u)}
{\widehat g_n(t)\overline{\widehat g_n(u)}}
=
K_{n,W}^{(N)}(t,u).
}
\tag{11}
\]

Therefore any zero, pole after continuation, spectral feature, sign pattern, or cross-prime arithmetic structure contained in \(K_{n,W}^{(N)}\) is reproduced by the matched control. The actual Prime-Circle profile contributes only the outer one-frequency amplitudes already present before \(W_N\) is introduced.

This is stronger in one respect than the Euler-factor calculation of PC-413: there is no need to classify \(W_N\) arithmetically. A kernel may generate complicated zeta or \(L\)-data, but if that data sits in \(K_{n,W}^{(N)}\), it belongs to the chosen conductor readout together with the universal descendant law, not to an interaction newly forced by the roots-of-unity source.

## 4. Spectral matrices and determinants cannot hide an entanglement

Choose finitely many Mellin frequencies \(t_1,\ldots,t_r\) and suppose the construction produces a Hermitian kernel matrix

\[
\mathbf A_h
=
\bigl(\mathcal A_{h,W}^{(N)}(t_i,t_j)\bigr)_{i,j=1}^r.
\tag{12}
\]

Put

\[
H_h
=
\operatorname{diag}
\bigl(\widehat h_n(t_1),\ldots,\widehat h_n(t_r)\bigr)
\tag{13}
\]

and

\[
\mathbf K
=
\bigl(K_{n,W}^{(N)}(t_i,t_j)\bigr)_{i,j=1}^r.
\tag{14}
\]

Equation (7) becomes the exact diagonal congruence

\[
\boxed{
\mathbf A_h
=
H_h\,\mathbf K\,H_h^*.
}
\tag{15}
\]

Whenever all source amplitudes in (13) are nonzero,

\[
\operatorname{rank}\mathbf A_h
=
\operatorname{rank}\mathbf K,
\tag{16}
\]

the Hermitian inertia of \(\mathbf A_h\) equals that of \(\mathbf K\), and

\[
\boxed{
\det\mathbf A_h
=
\left|\prod_{j=1}^r\widehat h_n(t_j)\right|^2
\det\mathbf K.
}
\tag{17}
\]

Consequently a finite spectral determinant cannot mix the source with a cross-prime conductor kernel in a new way. Its zeros separate into zeros already carried by the source amplitudes and zeros of the source-independent conductor matrix. The latter are reproduced by (9)--(11).

This also blocks a common spectral-wrapper escape: diagonalizing \(W_N\), replacing it by a resolvent or a finite functional calculus, or allowing its eigenvectors to mix many rational primes may make \(\mathbf K\) complicated, but does not change the source-channel rank in (3).

## 5. Fixed-arity conductor tensors have the same obstruction

The rank-one pullback is not specifically quadratic. Let \(T_N\) be an arbitrary \(r\)-linear tensor on \(r\) descendant conductor spaces, with any chosen mixture of linear and conjugate-linear slots, and let the corresponding source frequencies be \(t_1,\ldots,t_r\). For linear slots, (3) gives

\[
D_{n,t_j}^{(N)}z_j
=
z_jc_n^{(N)}(t_j),
\]

and conjugate-linear slots behave analogously. Multilinearity therefore gives

\[
\boxed{
T_N\!\left(
D_{n,t_1}^{(N)}z_1,\ldots,
D_{n,t_r}^{(N)}z_r
\right)
=
\left(\prod_j z_j^{\epsilon_j}\right)
T_N\!\left(
c_n^{(N)}(t_1),\ldots,
c_n^{(N)}(t_r)
\right),
}
\tag{18}
\]

where \(z^{\epsilon_j}\) denotes \(z\) or \(\bar z\) according to the slot.

Thus every fixed-arity homogeneous conductor-only tensor has the same matched-control blindness. PC-408 treated a highly structured same-index product and PC-413 treated arbitrary prime-local two-label bilinear kernels. Equation (18) isolates the more general reason both families remain source blind after the descendant reduction: each frequency enters conductor space through a rank-one source map.

This statement deliberately does **not** cover an interaction that changes the descendant state before the tensor is evaluated, nor an inhomogeneous nonlinear feedback law in which different source degrees are dynamically mixed. Those are different mechanisms.

## 6. Growing support or operator rank alone does not escape

Suppose \(I_N\) grows and \(W_N\) has support, matrix rank, or cross-prime complexity growing arbitrarily with \(N\). At every finite \(N\), equation (7) remains exact. Therefore, if a source-independent normalization \(a_N\) and a topology are chosen in which

\[
a_N^{-1}K_{n,W}^{(N)}(t,u)
\longrightarrow
K_{n,W}(t,u),
\tag{19}
\]

then automatically

\[
\boxed{
a_N^{-1}\mathcal A_{h,W}^{(N)}(t,u)
\longrightarrow
\widehat h_n(t)\overline{\widehat h_n(u)}
K_{n,W}(t,u).
}
\tag{20}
\]

So the mere fact that interaction rank or depth grows with conductor does not defeat the obstruction. To do so, the limiting construction must fail one of the actual hypotheses: for example the operator itself must be derived from source geometry, the state must be changed nonlinearly before scalarization, or the limiting operation must couple source and conductor data before the factorization (1) is available.

This sharpens the fourth surviving boundary in PC-413. Growing complexity is only a candidate escape when it is **structurally coupled to new source data**, not when it is merely a larger externally chosen conductor matrix.

## 7. Representation audit

The obstruction is coordinate-free. Let \(S_t\) be any invertible change of basis on the finite conductor space at frequency \(t\). Then

\[
c_n^{(N)}(t)\mapsto S_t c_n^{(N)}(t),
\tag{21}
\]

while the bilinear kernel transforms contragrediently,

\[
W_N(t,u)
\mapsto
S_t^{-\mathsf T}W_N(t,u)\,\overline{S_u}^{\,-1}.
\tag{22}
\]

The scalar contraction (8) is unchanged. In particular, changing from conductor labels to a basis that mixes primes, diagonalizing the kernel, or representing the same form as a tensor network cannot turn (3) into a higher-rank source channel.

This is the required representation stress test: the negative result is not an artifact of the valuation/Euler-product coordinates used in PC-413. It is the pullback of an arbitrary multilinear form along a rank-one map.

## 8. Prior-art and novelty audit

No novelty is claimed for the multilinear algebra in (3), (7), or (18). Pullback of multilinear forms and basis-independent tensor contraction are standard linear algebra; the representation statement in (21)--(22) is ordinary covariance under change of basis. The project-specific content is the application of that elementary fact to the exact PC-405 descendant law and the resulting closure of a live Prime-Circle escape hatch.

The local duplicate audit distinguishes this result from nearby findings. PC-408 classifies fixed-degree products sharing one descendant index and derives their shifted-zeta hypercube. PC-409--PC-412 classify several join/meet/lcm and cross-frequency bilinear conductor kernels. PC-413 allows arbitrary **prime-local multiplicative** two-label arrays and derives their two-dimensional incidence difference. The present result does not refine those Euler factors; instead it removes primewise multiplicativity entirely and proves a source-identifiability obstruction for arbitrary conductor tensors at finite cutoff.

Accordingly the mathematical status is a decisive negative for a project-specific mechanism, not a new theorem of multilinear algebra and not a claim that an arbitrary \(K_{n,W}\) is analytically simple. A deliberately engineered \(W_N\) can contain any amount of spectral or zeta structure; that is exactly why the canonical mandate treats arbitrary spectral wrappers as a falsification case.

## 9. Consequence for the research line

The following route is now closed:

\[
\boxed{
\text{PC-405 scalar descendant law}
\;\longrightarrow\;
\text{arbitrary source-independent conductor-only tensor}
\;\longrightarrow\;
\text{cross-prime spectral determinant}
\;\longrightarrow\;
\text{Prime-Circle-specific RH mechanism}.
}
\tag{23}
\]

The surviving boundary is correspondingly narrower. A useful continuation must introduce information **before or outside** this rank-one conductor channel: a tensor/operator canonically derived from angular, chord, old/new, or other embedded root geometry; a source-dependent or state-changing nonlinear interaction; a genuinely two-dimensional/nonlocal operation that prevents reduction to (1); or a limit whose defining source/conductor coupling is not already separated at every finite stage.

A direct falsification of this finding would require either a counterexample to the exact descendant identity (1) in the regime being used, or a purported source-independent conductor tensor whose contraction cannot be written as the multilinear pullback (18). Merely exhibiting a nonmultiplicative cross-prime kernel, a dense matrix, a large-rank operator, or an interesting zero set in \(K_{n,W}\) does not falsify it.
