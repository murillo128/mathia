# PC-278 — single-source dual-window phase spectra are diagonal-unitary pure gauge

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most direct positive/Hermitian spectralization of the vector/directional near-resonance escape left open by PC-277.

PC-277 leaves open enriched observables that retain the minimizing direction `(h,k)` or other signed/vector information before the scalar compression

\[
D_B(x,y)=\min_{0<\max(|h|,|k|)\le B}\|hx+ky\|_{\mathbb R/\mathbb Z}.
\]

A particularly natural attempt is not to minimize at all: keep the full finite dual-window phase field

\[
(h,k)\longmapsto e^{2\pi i(hp+kr)/q}
\]

and spectralize it through a fixed two-dimensional mask, Gram matrix, singular-value problem, or Hermitian nonlocal kernel. For a **single source pair** `(p,r)`, that entire positive/Hermitian route is pure gauge.

Let `q>=2`, let `H,K subset Z` be finite, let

\[
\zeta_q=e^{2\pi i/q},
\]

and let `A=(A_{h,k})_{h\in H,k\in K}` be any complex matrix independent of `(p,r)`. Define the source-modulated window

\[
W_{p,r}^{(q)}(h,k)
:=A_{h,k}\,\zeta_q^{hp+kr}.
\tag{1}
\]

With

\[
D_p:=\operatorname{diag}_{h\in H}(\zeta_q^{hp}),
\qquad
E_r:=\operatorname{diag}_{k\in K}(\zeta_q^{kr}),
\tag{2}
\]

we have the exact factorization

\[
\boxed{
W_{p,r}^{(q)}=D_p A E_r.
}
\tag{3}
\]

Both factors are diagonal unitaries. Hence every singular value of `W_{p,r}^{(q)}` is exactly a singular value of `A`, independently of whether `p,r` are prime, composite, random residues, or any other admissible source values. In particular

\[
\boxed{
\operatorname{rank}W_{p,r}^{(q)}=\operatorname{rank}A,
\qquad
s_j(W_{p,r}^{(q)})=s_j(A),
}
\tag{4}
\]

and every Schatten norm, the operator norm, Frobenius norm, singular-value determinant, and every spectral statistic of the positive Gram operators are source-independent:

\[
W_{p,r}W_{p,r}^*
=D_p(AA^*)D_p^*,
\qquad
W_{p,r}^*W_{p,r}
=E_r^*(A^*A)E_r.
\tag{5}
\]

For a square mask, `|det W_{p,r}|=|det A|`; only the explicit separable determinant phase can change. For the unweighted full window `A_{h,k}=1`, the matrix is rank one for every source pair, with its unique nonzero singular value equal to `sqrt(|H||K|)`. Restricting to a fixed box, annulus, primitive-direction mask, or any other source-independent coefficient set changes only `A`, not the conclusion.

## 1. The Hermitian/nonlocal version is an exact coboundary gauge

The same collapse is not peculiar to rectangular matrices. Let `S subset Z^2` be finite, write `u=(h,k)`, and let `K=(K_{u,v})_{u,v\in S}` be any source-independent Hermitian kernel. Put

\[
U_{p,r}:=\operatorname{diag}_{u\in S}
\zeta_q^{u\cdot(p,r)}
\tag{6}
\]

and modulate the edge/kernel phases by

\[
K^{(p,r)}_{u,v}
:=K_{u,v}\,
\zeta_q^{(u-v)\cdot(p,r)}.
\tag{7}
\]

Then exactly

\[
\boxed{
K^{(p,r)}=U_{p,r} K U_{p,r}^*.
}
\tag{8}
\]

Therefore the complete Hermitian spectrum, characteristic polynomial, resolvent traces, heat traces, functional calculus, inertia, and every unitary spectral invariant are independent of the source pair.

Geometrically the phase on an oriented coefficient-graph edge `u->v` is the discrete gradient of the vertex potential

\[
\theta_{p,r}(u)=\frac{2\pi}{q}u\cdot(p,r).
\tag{9}
\]

Consequently every cycle has trivial holonomy:

\[
\prod_{j=1}^{m}
\zeta_q^{(u_j-u_{j+1})\cdot(p,r)}
=
\zeta_q^{(u_1-u_2+u_2-u_3+\cdots+u_m-u_1)\cdot(p,r)}
=1.
\tag{10}
\]

Thus the source supplies no gauge-invariant magnetic flux on the coefficient graph. It only chooses a diagonal gauge representative.

## 2. Why this matters for the PC-277 frontier

The full phase field is strictly richer pointwise than the scalar minimum `D_B`: before quotienting, it retains the signed coefficient pair and the complete source-dependent phase. But the most direct positive/Hermitian spectralization throws that extra placement information away again. The map

\[
(p,r)
\longmapsto
\left(\zeta_q^{hp+kr}\right)_{h,k}
\longmapsto
\operatorname{Spec}_{\mathrm{sing/Gram/Hermitian}}
\tag{11}
\]

is constant once the coefficient-domain mask/kernel is fixed.

This is a stronger matched-control obstruction than merely showing that prime and non-prime laws become asymptotically close. For the class (1) or (7), **every source pair is exactly isospectral at every finite `q` and every finite bandwidth**. No limiting argument, PNT input, or Diophantine estimate is needed.

Accordingly, the apparently natural continuation

\[
\text{retain all dual-window directions/phases}
\longrightarrow
\text{fixed positive or Hermitian spectral operator}
\longrightarrow
\text{prime/RH discriminator}
\tag{12}
\]

is closed before any asymptotic analysis begins.

## 3. Why the scalar near-resonance observable is not covered

This result does **not** contradict PC-272--PC-277. The scalar carrier uses distance to a distinguished absolute phase `1`:

\[
\left\|\frac{hp+kr}{q}\right\|_{\mathbb R/\mathbb Z}
\quad\text{or equivalently}\quad
\operatorname{dist}\!\left(\zeta_q^{hp+kr},1\right).
\tag{13}
\]

That nonlinear anchoring is not invariant under independent row and column phase multiplication. It breaks the diagonal gauge before minimization, which is exactly why the ordered source placement survives finite-window scalar evaluation and why the matched-control analysis of PC-273--PC-277 is nontrivial.

The same distinction applies to threshold masks selected **from** the source phases, nonlinear entrywise maps, conditioned near-resonance subgraphs, or any construction that first compares the phases to a fixed external anchor and only then forms an operator. Those are not of the fixed-mask forms (1) or (7).

## 4. Prior-art and novelty audit

The abstract mechanism is classical. Equation (3) is elementary left/right diagonal-unitary equivalence, and invariance of singular values under unitary factors is standard linear algebra. Equation (8) is the corresponding discrete gauge equivalence familiar from magnetic graph/Laplacian theory: a phase field that is an exact one-form/coboundary has zero cycle flux and is removed by diagonal unitary conjugation.

A targeted prior-art search against diagonal-unitary matrix equivalence, complex Hadamard equivalence, and discrete magnetic graph gauge transformations found the expected standard framework. In particular, the mathematical content needed here does not depend on a new external theorem: the complete proof is the explicit factorizations (3) and (8) and the telescoping identity (10).

No novelty is claimed for unitary invariance of singular values, diagonal gauge transformations, or zero-flux magnetic equivalence. The project-local content is the exact specialization to the Prime-Circle dual-window source phase: the obvious two-dimensional positive/Hermitian spectral lift of the surviving near-resonance directional data contains **zero source information** unless some structure is introduced that is not removable by this gauge.

No new durable literature dependency is required, so `SOURCES.md` is unchanged.

## 5. Sharp boundaries and surviving channels

The theorem deliberately does not claim that every spectralization of the raw matrix `W_{p,r}` is source-independent. If the row and column spaces are artificially identified and one studies the generally nonnormal eigenvalues of `D_pAE_r`, left/right unitary equivalence does not preserve those eigenvalues. Even for a square rank-one all-ones mask, the single nonzero eigenvalue can depend on the source phases. Such a construction must justify why the identification of the two coefficient axes is intrinsic rather than a coordinate choice, and it no longer follows from positive/Hermitian spectral geometry.

Other genuine ways to evade the obstruction are:

- source-dependent masks or weights selected by the near-resonance geometry;
- nonlinear anchoring to the fixed phase `1` before operator formation;
- kernels with genuine nonzero cycle flux not expressible as `(u-v)\cdot(p,r)`;
- cross-source or cross-level operators comparing two different source configurations before gauge quotienting;
- joint multi-source tensors whose relative phases cannot be removed by one diagonal potential.

These are mathematical changes of hypothesis, not loopholes in (3) or (8). They are the appropriate places to look if directional information is to survive spectral compression.

## 6. Falsification and audit tests

The exact claim has direct finite tests.

1. Choose any finite `H,K`, arbitrary complex `A`, and any two source pairs. The singular values of `D_pAE_r` must equal those of `A` to machine precision; an exact counterexample would refute (3) or unitary invariance.
2. For any Hermitian `K` and finite direction graph `S`, the eigenvalues of `U_{p,r}KU_{p,r}^*` must equal those of `K` exactly.
3. Multiply the source-induced edge phases around any closed coefficient-graph cycle. The product must be `1`; a nontrivial product would contradict the coboundary form (7).
4. Any proposed prime discriminator that uses only a source-independent mask/kernel and only singular, Gram, or Hermitian spectral invariants should be tested on two arbitrary residue source pairs. Dependence on the source would contradict the explicit factorization.
5. A source-dependent threshold, absolute-phase nonlinearity, cross-source coupling, or nonnormal eigenvalue problem is outside the theorem rather than a counterexample.

## 7. Consequences for the research line

PC-277 leaves an intermediate normalized scalar window and richer directional/nonlocal observables as legitimate continuations. PC-278 narrows the latter sharply: **merely retaining the entire two-dimensional phase window and then applying a fixed positive/Hermitian spectral wrapper does not preserve the extra information.** The source placement is a diagonal-unitary gauge and disappears exactly.

Thus a serious directional continuation must break this pure-gauge structure before spectral compression. The mathematically meaningful survivors are anchor-sensitive nonlinear selection, true coefficient-graph flux, or relative/cross-source and cross-level couplings. Those mechanisms remain subject to the Prime-Circle mandate's matched-control and prior-art gates; the existence of the raw vector field alone is not evidence of a new RH bridge.