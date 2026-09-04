# WP-145 — Resultant-Hessian positivity loses prime-power support and splits the real-place curvature

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + RESULTANT-HESSIAN + INDEPENDENT-LOCAL-NONNEGATIVITY + MATCHED-NONPRIME-CONTROL + ARCHIMEDEAN-CURVATURE-FAILURE + GLOBAL-BRIDGE-FAILURE + PRIOR-ART-CLASSICALIZATION` for the direct multi-mode resultant-Hessian continuation of the Prime-Circle Weil coefficients.

`WP-144` closed metric tuning of the one-mode Kron defect and left a genuinely multi-mode positive response as one possible escape. Prime Circle already contains the most canonical such response: `PC-128` proves that the full vertexwise second variation of the logarithmic resultant interaction between two primitive shells is a maximal-rank positive inverse-square chord Laplacian after the natural sign flip.

That route fails earlier than the Kron route. The **zero-order** logarithmic resultant has the exact prime-power sparsity and `log p` weight used by `PC-002`/`PC-004`, but its independently positive **second variation** has nonzero coupling between every pair of distinct primitive shells. The sparse arithmetic cancellation is destroyed by differentiation. The canonical shell compression is already nonzero on a pair whose cyclotomic resultant is exactly `1`, and the canonical Hessian determinant remains nontrivial on the same kind of control. In addition, continuing the same logarithmic collision potential to the reciprocal radial geometry used by `PC-004` gives opposite second-derivative signs in the `sinh` and `cosh` real-place channels and produces squared inverse-distance kernels rather than the Weil kernels themselves.

Thus the obvious attempt

\[
\text{cyclotomic log resultant}
\longrightarrow
\text{positive vertexwise Hessian}
\longrightarrow
\text{one finite--archimedean positive form}
\]

cannot preserve the load-bearing arithmetic data. The exact finite Weil coefficient lives in the potential value; the direct geometric sign lives in a different derivative-level object.

## 1. The multi-mode candidate is genuinely positive

Let

\[
A=P_m^*=\{\alpha_1,\ldots,\alpha_r\},
\qquad
B=P_n^*=\{\beta_1,\ldots,\beta_s\},
\qquad m\ne n,
\]

with `r=phi(m)` and `s=phi(n)`. Distinct exact-order root shells are disjoint. Give each vertex an independent angular variable and set

\[
E_{m,n}(\theta,\phi)
=
\sum_{i=1}^r\sum_{j=1}^s
\log|e^{i\theta_i}-e^{i\phi_j}|.
\tag{1}
\]

At the undeformed roots, `PC-128` gives

\[
\boxed{
L_{m,n}:=-D^2E_{m,n}
=
\begin{pmatrix}
\operatorname{diag}(C\mathbf 1)&-C\\
-C^T&\operatorname{diag}(C^T\mathbf 1)
\end{pmatrix}
\succeq0,
}
\tag{2}
\]

where

\[
c_{ij}
=
\frac1{|\alpha_i-\beta_j|^2}
=
\frac1{4\sin^2((\theta_i-\phi_j)/2)}
>0.
\tag{3}
\]

For a vertex displacement `(u,v)`, its quadratic form is exactly

\[
\boxed{
\langle (u,v),L_{m,n}(u,v)\rangle
=
\sum_{i,j}c_{ij}|u_i-v_j|^2\ge0.
}
\tag{4}
\]

Because the interaction graph is the complete bipartite graph `K_{r,s}`, the only null direction is common rotation. Hence

\[
\operatorname{rank}L_{m,n}=r+s-1.
\tag{5}
\]

This is therefore not another scalar or one-mode positivity wrapper. It is an intrinsic, maximal-rank positive response of the actual Prime-Circle logarithmic collision energy, and is exactly the sort of candidate left logically open by `WP-144`.

## 2. Positive curvature has full shell support, while the resultant value has prime-power support

Compress (2) to the normalized uniform vectors on the two shells,

\[
e_A=\frac{\mathbf1_A}{\sqrt r},
\qquad
e_B=\frac{\mathbf1_B}{\sqrt s}.
\tag{6}
\]

Put

\[
W_{m,n}:=\sum_{i=1}^r\sum_{j=1}^s c_{ij}.
\tag{7}
\]

Every term in (7) is strictly positive, so

\[
\boxed{W_{m,n}>0\quad\text{for every }m\ne n.}
\tag{8}
\]

The exact two-shell compression is

\[
\boxed{
\begin{pmatrix}
\langle e_A,L e_A\rangle&\langle e_A,L e_B\rangle\\
\langle e_B,L e_A\rangle&\langle e_B,L e_B\rangle
\end{pmatrix}
=
W_{m,n}
\begin{pmatrix}
1/r&-1/\sqrt{rs}\\
-1/\sqrt{rs}&1/s
\end{pmatrix}.
}
\tag{9}
\]

It is positive semidefinite of rank one, and its off-diagonal coupling is nonzero for **every** distinct shell pair:

\[
\boxed{
\langle e_A,L_{m,n}e_B\rangle
=-\frac{W_{m,n}}{\sqrt{rs}}<0.
}
\tag{10}
\]

Compare this with the zero-order logarithmic interaction

\[
I_{m,n}
=
\sum_{\alpha\in P_m^*}\sum_{\beta\in P_n^*}
\log|\alpha-\beta|
=
\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
\tag{11}
\]

Apostol's classical cyclotomic-resultant theorem gives, for `1<m<n`,

\[
|\operatorname{Res}(\Phi_m,\Phi_n)|
=
\begin{cases}
p^{\varphi(m)},&n/m=p^a\text{ for some prime }p,\\
1,&\text{otherwise}.
\end{cases}
\tag{12}
\]

Therefore the normalized zero-order shell matrix element used in `PC-004` is sparse and, on a prime-power ray, equals

\[
\frac{I_{p^a,p^{a+k}}}
{\sqrt{\varphi(p^a)\varphi(p^{a+k})}}
=
\frac{\log p}{p^{k/2}}.
\tag{13}
\]

Equations (8)--(10) show that this sparsity does **not** survive the positive Hessian. The simplest exact control is already decisive. For

\[
(m,n)=(2,3),
\]

one has

\[
|\operatorname{Res}(\Phi_2,\Phi_3)|=1,
\qquad I_{2,3}=0,
\tag{14}
\]

but the two distances from `-1` to the primitive cube roots both have squared length one, so

\[
W_{2,3}=2
\tag{15}
\]

and the compressed positive Hessian is

\[
\boxed{
\begin{pmatrix}
2&-\sqrt2\\
-\sqrt2&1
\end{pmatrix}\succeq0.
}
\tag{16}
\]

Thus a shell pair that contributes **exactly zero** to the cyclotomic/Weil selector contributes a strictly positive relative-mode energy to the canonical Hessian.

The prime-power control shows that the logarithmic weight is lost as well. For `(m,n)=(2,4)`,

\[
I_{2,4}=\log2,
\qquad
\frac{I_{2,4}}{\sqrt{\varphi(2)\varphi(4)}}
=\frac{\log2}{\sqrt2},
\tag{17}
\]

whereas

\[
W_{2,4}=1,
\qquad
\langle e_{P_2^*},L_{2,4}e_{P_4^*}\rangle
=-\frac1{\sqrt2}.
\tag{18}
\]

The half-density normalization survives as an ordinary shell normalization, but the required `log 2` does not.

This is the key structural separation:

\[
\boxed{
\text{prime-power cancellation and }\log p
\text{ live in }E;
\qquad
\text{independent PSD sign lives in }-D^2E.
}
\tag{19}
\]

## 3. Finite algebraic compression cannot put the lost logarithm back

The loss in (19) is not merely a bad choice of the uniform shell mode. Every conductance (3) lies in a real cyclotomic field and is algebraic. Therefore every matrix obtained from finitely many such Hessians by algebraic coordinate changes, finite orthogonal compressions with algebraic coefficients, direct sums, products, inverses on nonsingular blocks, or Schur complements still has algebraic entries.

In contrast, every nonzero finite Weil coefficient

\[
(\log p)p^{-k/2}
\tag{20}
\]

is transcendental: `p^{-k/2}` is nonzero algebraic, while Hermite--Lindemann implies that `log p` is transcendental for algebraic `p>1`.

Consequently, a finite algebraic matrix operation on the positive Hessian cannot by itself recover (20). A logarithmic spectral operation, an integral over a deformation path, or reintroduction of the original zero-order resultant can escape this statement, but each is **new structure beyond Hessian positivity** and must be justified before inspecting the desired arithmetic output.

The most canonical logarithmic spectral escape also fails the sparse-support test. `PC-129` proves that the reduced determinant of `L_{m,n}` is a weighted spanning-tree invariant and gives the exact controls

\[
\kappa_{3,4}=8
\qquad\text{while}\qquad
|\operatorname{Res}(\Phi_3,\Phi_4)|=1,
\tag{21}
\]

and

\[
\kappa_{3,6}=\frac58,
\qquad
|\operatorname{Res}(\Phi_3,\Phi_6)|=4.
\tag{22}
\]

Hence `log kappa` is already nonzero on a coprime/non-prime-power control where the Weil selector vanishes, while on the prime-power control it contains unrelated arithmetic (`log 5` as well as `log 2`). The resultant-normalized invariant `R_{m,n}^2\kappa_{m,n}` is a positive integer (`8` and `10` in these two examples), not a sparse Mangoldt coefficient.

So passing from the Hessian to its raw determinant or pseudodeterminant does not reconstruct the cancellation that differentiation erased. A more elaborate nonlinear functional remains logically possible, but it no longer inherits arithmetic correctness merely from the positive resultant Hessian.

## 4. The same log-collision curvature does not supply both real-place channels

`PC-004` observes that the same circle geometry contains the two reciprocal real-place distance kernels. In the canonical logarithmic scale coordinate `x>0`, the reciprocal radial points are

\[
r_+=e^{x/2},
\qquad r_-=e^{-x/2}.
\tag{23}
\]

On the same ray and on the antipodal ray their distances are respectively

\[
2\sinh(x/2),
\qquad
2\cosh(x/2).
\tag{24}
\]

If the finite resultant-Hessian mechanism is continued using the **same logarithmic collision potential**, the two one-dimensional potentials are

\[
F_{\sinh}(x)=\log\bigl(2\sinh(x/2)\bigr),
\qquad
F_{\cosh}(x)=\log\bigl(2\cosh(x/2)\bigr).
\tag{25}
\]

Their exact second derivatives have opposite sign:

\[
\boxed{
F_{\sinh}''(x)
=-\frac1{4\sinh^2(x/2)}<0,
\qquad
F_{\cosh}''(x)
=+\frac1{4\cosh^2(x/2)}>0.
}
\tag{26}
\]

For comparison, one finite angular edge has

\[
f(\delta)=\log\left|2\sin\frac\delta2\right|,
\qquad
f''(\delta)
=-\frac1{4\sin^2(\delta/2)}<0.
\tag{27}
\]

Thus the sign `-D^2` that makes the finite angular Hessian positive also makes the same-ray `sinh` radial curvature positive, but makes the antipodal `cosh` radial curvature negative. Flipping the Hessian sign merely exchanges the problem. There is no common direct second-variation sign for all three channels in the canonical log-scale parameter.

There is also a functional-shape mismatch. The real-place kernels identified in `PC-004` are

\[
\frac1{2\sinh(x/2)},
\qquad
\frac1{2\cosh(x/2)},
\tag{28}
\]

whereas the curvature continuation produces the **squares** in (26). Taking square roots or otherwise post-processing the curvature returns a nonlinear scalar construction rather than a quadratic Hessian form and does not inherit a bilinear positivity theorem automatically.

This does not rule out the established global/compressed archimedean mechanisms of Weil, Sonin, or Connes--Consani. It rules out the much more specific hope that the same pairwise logarithmic collision energy can be differentiated once into a single sign-definite finite--archimedean Hessian whose local pieces are already the Weil kernels.

## 5. Adversarial controls and escape boundary

The obstruction is robust under the most immediate repairs.

**Matched nonarithmetic configurations.** Equation (4) holds for arbitrary disjoint finite point clouds on the circle. Positivity is therefore geometric but prime-blind. Primitive-shell arithmetic enters the zero-order cancellation (11)--(12), not the sign theorem.

**Population normalization.** Dividing shell vectors by `sqrt(phi(n))` changes magnitudes but cannot change the complete support (10). The exact half-density that makes `PC-004` striking does not restore the vanished zero pattern at Hessian level.

**Finite positive combinations.** Summing the edgewise Hessian energies with nonnegative intrinsic coefficients cannot cancel a non-prime shell pair: every edge term in (4) is nonnegative. A cancellation would require signed/global coupling or a selector acting before the positive sum, so the sign would have to be proved for the assembled object rather than inherited termwise.

**Raw determinant/logdet.** The controls (21)--(22) show that the canonical collective scalar of the maximal-rank Hessian remains nonzero on the wrong support. Taking a logarithm does not repair that.

**Reparametrizing the radial coordinate.** The explicit-formula comparison uses the logarithmic multiplicative coordinate `x=log scale`; changing it merely to alter the sign of (26) also changes the target kernels and requires an independent geometric reason. No such reason is supplied by Prime Circle.

**A genuinely global coupling remains open.** One may couple zero-order resultant data to an archimedean sector before taking a quotient, Schur complement, cohomological pairing, or other global sign theorem. Such a construction would evade this finding precisely because its positivity would no longer be the direct vertexwise Hessian positivity audited here.

The finding therefore does not say that resultants are irrelevant. It says that **differentiating them to obtain the obvious independent positive form removes the exact arithmetic feature that made them relevant to Weil in the first place.**

## 6. Prior art and novelty audit

The ingredients are classical and are not claimed as new mathematics.

- Apostol's theorem on cyclotomic resultants is Tom M. Apostol, *Resultants of cyclotomic polynomials*, Proceedings of the American Mathematical Society **24** (1970), 457--462, DOI `10.1090/S0002-9939-1970-0251010-X`. It supplies the `1` versus prime-power resultant classification used by `PC-002`/`PC-004`.
- Hessians of logarithmic collision/master functions and inverse-square trigonometric interactions belong to classical hyperplane-arrangement/Gaudin and Calogero--Sutherland territory. `PC-128` already audits this boundary; Varchenko's master-function literature explicitly relates Hessians of logarithmic master functions to established geometric/integrable structures rather than a new arithmetic positivity mechanism.
- The weighted determinant statement used in (21)--(22) is the ordinary Matrix--Tree/Kirchhoff structure already audited in `PC-129`.
- Weil's explicit formula and quadratic positivity criterion are the target, not a novelty claim. Connes--Consani's archimedean positivity work (arXiv:`2006.13771`, Selecta Math. 27 (2021), Paper 77) is close prior art showing that a successful sign mechanism at infinity can arise from compression of the scaling action rather than from a bare local positive kernel.

A directed search over cyclotomic resultants, logarithmic/master-function Hessians, inverse-square root-of-unity interactions, and archimedean Weil positivity recovered these expected classical mechanisms. No historical-priority claim is made for the elementary incompatibility derived here. The durable Mathia-specific content is the **cross-branch obstruction** obtained by combining three already canonical facts that were previously favorable in isolation:

\[
\boxed{
\begin{array}{c}
\text{PC-004: zero-order normalized resultants have exact Weil support/weight},\\
\text{PC-128: vertexwise second variation has an independent PSD theorem},\\
\text{PC-004: the same circle has reciprocal real-place distance kernels}
\end{array}
\Longrightarrow
\begin{array}{c}
\text{the PSD Hessian loses the sparse finite selector,}\\
\text{and its direct radial continuation cannot keep one sign or kernel shape.}
\end{array}
}
\tag{29}
\]

This is a negative structural result, not a claim that the underlying classical identities are new.

## 7. Consequence for the Weil-positivity frontier

`WP-140`--`WP-144` showed that the one-hole Kron route can produce a genuine positive SPD logarithmic distance, but its one-mode geometry is prime-blind and globally incomplete. The resultant Hessian looked like a natural next move because it supplies exactly what that route lacked locally: **many coupled modes and an ordinary quadratic positive form**.

The present result closes that direct escape. The multi-mode positivity is real, but it lives after two differentiations of the logarithmic resultant, and those differentiations remove both the prime-power zero pattern and the `log p` amplitude. Even the canonical determinant does not restore the zero pattern, and the obvious same-potential continuation to the two real-place channels is not sign-compatible.

The surviving requirement is therefore sharper. A viable Prime-Circle mechanism must preserve the arithmetic cancellation **before** the positivity theorem rather than hope that a positive local Hessian will remember it. Concretely, it would need a genuinely global object in which zero-order cyclotomic/resultant data, the finite half-density, and the archimedean/pole sector are coupled before taking the relevant quotient, compression, intersection form, boundary response, or cohomological sign theorem. Any proposal that first replaces the resultants by their ordinary positive inverse-square Hessians has already crossed the information-loss boundary established here.
