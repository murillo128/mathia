# PC-071 — homeomorphic scalar dilation covariance cannot rescue compact resolvent

**Status:** `EXACT-DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the regular nonlinear scalar-covariance escape left open by PC-070 on the compatible Prime-Circle solenoid.

## Claim

PC-064 identifies the compatible all-level Prime-Circle refinement with the arithmetic solenoid

\[
\Sigma_{\mathbb Q}\cong\widehat{\mathbb Q},
\qquad
L^2(\Sigma_{\mathbb Q})
=\overline{\operatorname{span}}\{\chi_q:q\in\mathbb Q\},
\]

and PC-069/PC-070 classify scalar **affine** covariance under the intrinsic power automorphism. For `m\ge2`, let

\[
V_m\chi_q=\chi_{mq}
\]

be the Haar-Koopman unitary induced by the compatible dilation. PC-070 explicitly leaves open the possibility that a nonlinear scalar spectral law

\[
\boxed{V_m^*HV_m=\Phi(H)}
\]

might evade the affine no-go.

It does not, for the natural regular scalar class.

Let `\Phi:\mathbb R\to\mathbb R` be a continuous bijection, equivalently a real homeomorphism. There is **no** self-adjoint compact-resolvent operator `H` on either the natural mean-zero space

\[
L^2_0(\Sigma_{\mathbb Q})=\mathbf1^\perp
\]

or the full `L^2(\Sigma_{\mathbb Q})` satisfying

\[
\boxed{V_m^*HV_m=\Phi(H)}
\]

as an equality of self-adjoint operators.

The reason is exact and exhausts all real homeomorphisms.

- If `\Phi` is increasing and has a fixed point, every non-fixed spectral orbit accumulates at a finite fixed point, contradicting compact resolvent, while a fixed eigenvalue would give a finite-dimensional `V_m`-invariant subspace.
- If `\Phi` is increasing and fixed-point-free, it is conjugate by a real homeomorphism `g` to a translation. Then `K=g(H)` still has compact resolvent and satisfies

  \[
  V_m^*KV_m=K\pm I,
  \]

  exactly the additive covariance already ruled out by PC-070.
- If `\Phi` is decreasing, `\Phi^2` is increasing and has a fixed point; squaring the unitary covariance reduces to the first case for `V_m^2=V_{m^2}`.

Thus a regular nonlinear reparametrization of one self-adjoint spectrum is not a new escape from PC-069/PC-070. Any surviving dilation-based Prime-Circle mechanism must leave this scalar-homeomorphic class: for example by using a non-bijective or genuinely singular law forced by geometry, an operator-valued/non-scalar relation, a one-sided semigroup representation, a non-ordinary spectral framework, or symmetry-breaking data before the solenoid quotient.

## 1. Functional calculus transports eigenspaces along `\Phi`

Assume

\[
V_m^*HV_m=\Phi(H).
\]

Multiplying by `V_m` on the left gives

\[
HV_m=V_m\Phi(H).
\]

If

\[
H\psi=\lambda\psi,
\]

then functional calculus gives

\[
\Phi(H)\psi=\Phi(\lambda)\psi,
\]

and therefore

\[
\boxed{H(V_m\psi)=\Phi(\lambda)V_m\psi.}
\]

Because `\Phi` is injective, the unitary `V_m` maps each eigenspace bijectively onto the next one:

\[
\boxed{V_m E_\lambda(H)=E_{\Phi(\lambda)}(H).}
\]

A self-adjoint compact-resolvent operator on an infinite-dimensional Hilbert space has discrete real spectrum, finite-dimensional eigenspaces, and no finite accumulation point of eigenvalues. Those elementary facts are the only analytic input needed below.

The other representation-theoretic input is already established in PC-069/PC-070. On the mean-zero solenoid, multiplication `q\mapsto mq` decomposes `\mathbb Q^\times` into infinitely many bilateral orbits, so `V_m` has **no nonzero finite-dimensional invariant subspace** there. On the full space, the only finite-dimensional invariant sector is the constant character `\mathbb C\mathbf1`.

## 2. An increasing law with a fixed point is incompatible with discrete spectrum

Suppose `\Phi` is increasing and let

\[
F=\{x\in\mathbb R:\Phi(x)=x\}.
\]

Assume first that `F` is nonempty.

If an eigenvalue `\lambda` belongs to `F`, then

\[
V_mE_\lambda(H)=E_\lambda(H).
\]

Compact resolvent makes `E_\lambda(H)` finite-dimensional. On `L^2_0(\Sigma_{\mathbb Q})` this contradicts the absence of finite-dimensional `V_m`-invariant subspaces. On the full space such an eigenspace can only lie in `\mathbb C\mathbf1`, so fixed eigenvalues can account for at most the one-dimensional constant sector.

Now let `\lambda\notin F`. It lies in a connected component `I` of `\mathbb R\setminus F`. Since `F\ne\varnothing`, every such component has at least one finite endpoint in `F`. On `I`, continuity and the absence of fixed points force one strict sign:

\[
\Phi(x)>x\quad\text{for all }x\in I,
\]

or

\[
\Phi(x)<x\quad\text{for all }x\in I.
\]

In the direction pointing toward a finite endpoint of `I`, the iterates

\[
\Phi^k(\lambda),\qquad k\in\mathbb Z,
\]

form a strict monotone sequence bounded by that endpoint. Its limit `a` satisfies

\[
\Phi(a)=a
\]

by continuity, so `a\in F` and is finite.

But every `\Phi^k(\lambda)` is again an eigenvalue of `H`, with the same finite multiplicity, because `V_m^k` transports the eigenspaces exactly. Hence `H` would have infinitely many distinct eigenvalues accumulating at the finite point `a`, impossible for compact resolvent.

Therefore an increasing `\Phi` with fixed points allows no non-fixed eigenvalues at all and, on the full space, at most the constant fixed sector. Such eigenspaces cannot span the infinite-dimensional Hilbert space. Thus no compact-resolvent `H` exists.

## 3. A fixed-point-free increasing law is just additive covariance in another spectral coordinate

The only remaining increasing case is

\[
F=\varnothing.
\]

Then either

\[
\Phi(x)>x\quad\forall x
\]

or

\[
\Phi(x)<x\quad\forall x.
\]

The required real-line conjugacy can be constructed directly, so no external classification theorem is needed.

Assume first `\Phi(x)>x`. Choose `x_0\in\mathbb R`. Since `\Phi` has no fixed point,

\[
\Phi^k(x_0)\to+\infty\quad(k\to+\infty),
\qquad
\Phi^k(x_0)\to-\infty\quad(k\to-\infty).
\]

Choose any increasing homeomorphism

\[
g_0:[x_0,\Phi(x_0)]\to[0,1]
\]

with the corresponding endpoints matched. Extend it to the interval

\[
[\Phi^k(x_0),\Phi^{k+1}(x_0)]
\]

by

\[
\boxed{
g(x)=k+g_0(\Phi^{-k}(x)).
}
\]

The endpoint definitions agree, so `g:\mathbb R\to\mathbb R` is an increasing homeomorphism and satisfies

\[
\boxed{g\circ\Phi=g+1.}
\]

For `\Phi(x)<x`, the same construction gives an increasing homeomorphism with

\[
\boxed{g\circ\Phi=g-1.}
\]

Now define the self-adjoint operator

\[
K=g(H)
\]

by functional calculus. A real homeomorphism is proper, so `|g(x)|\to\infty` as `|x|\to\infty`; consequently `K` has compact resolvent whenever `H` does. Unitary covariance of functional calculus gives

\[
\begin{aligned}
V_m^*KV_m
&=V_m^*g(H)V_m\\
&=g(V_m^*HV_m)\\
&=g(\Phi(H))\\
&=(g\circ\Phi)(H)\\
&=K\pm I.
\end{aligned}
\]

This is precisely the nonzero additive law ruled out by PC-070. Therefore **every fixed-point-free increasing nonlinear homeomorphic law is spectrally just PC-070 in a different coordinate**.

This is the central redirection: replacing affine covariance by a regular nonlinear scalar reparametrization does not add a new dynamical degree of freedom. It only changes the coordinate on the real spectrum.

## 4. Every decreasing homeomorphic law is excluded after two dilation steps

A decreasing homeomorphism `\Phi:\mathbb R\to\mathbb R` has a unique fixed point. Indeed `\Phi(x)-x` is strictly decreasing and runs from `+\infty` to `-\infty`.

Set

\[
\Psi=\Phi^2.
\]

Then `\Psi` is increasing and has at least that fixed point. Iterating the covariance twice gives

\[
\begin{aligned}
(V_m^2)^*HV_m^2
&=V_m^*(V_m^*HV_m)V_m\\
&=V_m^*\Phi(H)V_m\\
&=\Phi(V_m^*HV_m)\\
&=\Phi(\Phi(H))\\
&=\Psi(H).
\end{aligned}
\]

But

\[
V_m^2\chi_q=\chi_{m^2q}=V_{m^2}\chi_q,
\]

and `V_{m^2}` has the same bilateral-orbit obstruction as `V_m`. Section 2 therefore applies to the increasing homeomorphism `\Psi` and yields the same contradiction.

Thus decreasing scalar homeomorphisms do not provide a separate escape.

## 5. Relation to the affine no-go and exact controls

The theorem contains the earlier affine cases as controls rather than competing with them.

- `\Phi(x)=x` is the fixed-point case and recovers the commuting obstruction from PC-069.
- `\Phi(x)=x+d`, `d\ne0`, is fixed-point-free and Section 3 reduces directly to PC-070.
- `\Phi(x)=cx+d` with `c>0`, `c\ne1`, has a fixed point and is killed by Section 2, consistently with PC-069's affine scaling result.
- `\Phi(x)=-x` is decreasing; squaring gives the identity law for `V_{m^2}`, reproducing the `c=-1` control in PC-069.

The new content is that **there is no regular nonlinear scalar interval between those affine examples and a viable compact-resolvent model**. The complete homeomorphism class collapses to the same two obstructions: finite fixed-point accumulation/invariant eigenspaces, or additive covariance after a spectral coordinate change.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the abstract ingredients.

- Spectral functional calculus, compact-resolvent discreteness, and transport of eigenspaces under unitary conjugation are standard operator theory.
- The classification used in Section 3 — an increasing fixed-point-free homeomorphism of `\mathbb R` is conjugate to a translation — is classical one-dimensional dynamics. The exact conjugacy needed here is rederived explicitly rather than used as an external black box.
- `research/prime_circle/SOURCES.md` already records Funakawa–Matsuzawa–Sasaki–Suzuki–Teranishi on unitary time operators. Their examples confirm that additive covariance can be well behaved in other representations; PC-070's obstruction is specifically the fixed mode and infinite bilateral multiplicity of Prime-Circle solenoid dilation.
- Targeted literature searches around nonlinear unitary covariance, crossed-product/twisted spectral triples, unitary time operators, and real-line homeomorphism conjugacy did not locate this exact Prime-Circle solenoid no-go. That absence is not a novelty proof.

The durable project-specific contribution is therefore a **closure theorem for the research frontier left by PC-070**, not a claim that the underlying dynamical or operator-theoretic lemmas are new:

\[
\boxed{
\text{compatible solenoid dilation}
+\text{ scalar homeomorphic spectral covariance}
+\text{ ordinary compact resolvent}
\quad\text{are incompatible}.}
\]

## 7. Boundary of the obstruction

PC-071 deliberately assumes that the scalar law `\Phi` is a homeomorphism of the whole real line. It does **not** rule out:

- a non-bijective scalar law whose spectral folding is independently forced by Prime-Circle geometry;
- a discontinuous or spectrum-specific scalar law, although such a construction falls directly under the repository's arbitrary-spectral-wrapper warning unless its singularity is derived before spectralization;
- an operator-valued or matrix covariance in which `V_m^*HV_m` is not a scalar function of `H`;
- a one-sided semigroup/isometry representation instead of the two-sided solenoid automorphism;
- a semifinite spectral triple or another framework not requiring ordinary compact resolvent;
- symmetry breaking by the common anchor, primitive/old decomposition, or embedded chord geometry before passage to the abstract solenoid;
- nonlinear determinant/transfer data that are not functional calculus of one self-adjoint operator;
- or the global primitive-root uniformization/accessory branch of PC-017.

A future nonlinear covariance proposal therefore has a sharp audit test: if its claimed novelty is only a continuous bijective reparametrization of one scalar spectrum, PC-071 reduces it to an already closed branch. To survive, the proposal must explain exactly which additional Prime-Circle datum forces it outside that class.

## 8. Exact audit tests

The finding has direct falsifiers.

1. Starting from `V_m^*HV_m=\Phi(H)`, verify by functional calculus that `V_mE_\lambda(H)=E_{\Phi(\lambda)}(H)`.
2. For increasing `\Phi` with nonempty fixed set, choose a component of `\mathbb R\setminus\operatorname{Fix}(\Phi)` and verify that one direction of the orbit of every point converges to a finite fixed endpoint.
3. Check that such an orbit would give a forbidden finite accumulation point of compact-resolvent eigenvalues.
4. For a fixed eigenvalue, verify that its finite-dimensional eigenspace is `V_m`-invariant and compare with the no-finite-dimensional-subspace statement of PC-069/PC-070.
5. For fixed-point-free increasing `\Phi`, construct `g` interval by interval and verify exactly `g\circ\Phi=g\pm1`.
6. Verify that real-homeomorphism properness preserves compact resolvent under `K=g(H)`.
7. Apply unitary functional calculus and recover `V_m^*KV_m=K\pm I`, contradicting PC-070.
8. For decreasing `\Phi`, verify existence of a fixed point, square the covariance, and apply the increasing fixed-point case to `V_{m^2}`.
9. Test the affine controls `\Phi(x)=x`, `x+d`, `cx+d`, and `-x` against PC-069/PC-070.

Failure of any of items 1–8 would invalidate the claimed closure. Item 9 prevents the theorem from silently changing the already audited affine boundary.

## Consequence for the Prime-Circle program

PC-069 and PC-070 ruled out every scalar affine covariance law under the intrinsic two-sided power automorphism of the compatible solenoid. The most immediate remaining repair was to replace affine scaling by a nonlinear scalar spectral dynamics while retaining the same canonical dilation symmetry.

PC-071 closes that regular repair:

\[
\boxed{
V_m^*HV_m=\Phi(H),\quad
\Phi\in\operatorname{Homeo}(\mathbb R)
\quad\Longrightarrow\quad
H\text{ cannot be an ordinary compact-resolvent Prime-Circle Hamiltonian}.}
\]

The surviving search should therefore not spend further effort on smooth/continuous monotone scalar reparametrizations of a single solenoid Hamiltonian. Any viable next operator mechanism must obtain new information from **non-scalar coupling, pre-quotient embedded geometry, one-sided dynamics, or a different spectral framework**, rather than from a nonlinear change of spectral coordinate.