# PC-230 — Cauchy-residue-weighted chord refinement renormalizes to the parent Laplacian

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the most canonical operator-insertion escape left explicit by PC-229. PC-229 proves that the Cauchy pole residue transported through a fresh-prime refinement gives an exact weighted branching map, but leaves open an intrinsic operator inserted on the refined primitive shell before compression back to the parent. Inserting the source-native inverse-square chord Laplacian does create finite-prime parent mixing, yet that mixing has no new fixed-base limit: after the exact normalization forced by the residue branching, the compressed fine operator converges in operator norm to the **same parent primitive-shell chord Laplacian**.

More precisely, fix `N>2`, write

\[
\Phi_N(z)=\sum_{k=0}^{d}c_kz^k,
\qquad d=\varphi(N),
\qquad h_N=\sum_{k=0}^{d}c_k^2,
\]

and let

\[
A_N:=N^{-2}L_N^{\rm int}
\]

be the normalized primitive-shell inverse-square chord Laplacian of PC-155. For a fresh prime `p\nmid N`, PC-229 gives the residue branching

\[
(B_{N,p}f)(x)
=\frac{\Phi_N(\zeta_{Np}^{x})}{p}
 f(x\bmod N),
\qquad x\in U(Np).
\]

If `p>d`, PC-229 proves exactly that

\[
B_{N,p}^*B_{N,p}=\frac{h_N}{p}I.
\]

Hence

\[
\boxed{
U_{N,p}:=\sqrt{\frac p{h_N}}B_{N,p}
}
\]

is an isometry from the parent primitive-root space to the refined one. The canonical residue-weighted chord compression is therefore

\[
\boxed{
C_{N,p}:=U_{N,p}^*A_{Np}U_{N,p}.
}
\]

Then, through fresh primes,

\[
\boxed{
\|C_{N,p}-A_N\|=O_N(p^{-1/2}).
}
\tag{1}
\]

For distinct parent vertices the convergence is sharper:

\[
\boxed{
(C_{N,p})_{ab}-(A_N)_{ab}
=O_N\!\left(\frac{\log p}{p}\right),
\qquad a\ne b.
}
\tag{2}
\]

Thus the first geometry-forced operator that genuinely mixes the PC-229 parent fibers is an asymptotic refinement fixed point rather than a new expanding spectral carrier. The result is deliberately fixed-base: it does not classify simultaneous `N,p -> infinity`, an operator different from the chord Hessian, or a source-forced operation acting on the complete PC-227 packet before this residue/chord compression.

## 1. The PC-229 residue branching is exactly isometric above the no-alias threshold

Use exponent labels for primitive roots. For `a in U(N)`, the `p` solutions over the parent root `zeta_N^a` have labels

\[
x=a+Nj,
\qquad j\in\mathbb Z/p\mathbb Z.
\tag{3}
\]

Exactly one of them is divisible by `p`; that point is an old primitive `N`-th root rather than a primitive `Np`-th root. But its branching weight vanishes because it is a zero of `Phi_N`. Consequently sums involving the weight `Phi_N(zeta_{Np}^x)` may include all `p` lifts without changing the primitive-child operator matrix elements in which that weight appears.

PC-229 derives

\[
\kappa_{Np}(\beta)
=\frac{\Phi_N(\beta)}p\kappa_N(\beta^p)
\]

for the angular Cauchy residue `kappa_n(alpha)=1/(alpha Phi_n'(alpha))`. Its positive square is a coefficient-autocorrelation profile. When `p>d`, no two coefficient indices are congruent modulo `p`, so that profile is constant and

\[
B_{N,p}^*B_{N,p}=\frac{h_N}{p}I.
\tag{4}
\]

Equation (4) is the reason for using `U_{N,p}` above. No adjustable renormalization is introduced in PC-230: the normalization is exactly the one already forced by the residue transport.

## 2. The off-diagonal compressed conductance has an exact weighted cosecant formula

Let

\[
K_n(h):=rac{1}{4n^2\sin^2(\pi h/n)}.
\tag{5}
\]

For distinct primitive parent labels `a,b in U(N)`, the off-diagonal entry of `A_N` is `-K_N(a-b)`. Put

\[
E_N(z):=\sum_{k=0}^{d}c_k^2z^k,
\qquad E_N(1)=h_N.
\tag{6}
\]

The corresponding entry of `C_{N,p}` can be evaluated exactly. Write `n=Np`, group child pairs by `m=j-k mod p`, and average over the remaining fiber index. Since `p>d`, finite Fourier orthogonality kills every cross-coefficient term:

\[
\frac1p\sum_{k=0}^{p-1}
\overline{\Phi_N\!\left(
\zeta_n^{a+N(k+m)}
\right)}
\Phi_N\!\left(
\zeta_n^{b+Nk}
\right)
=
E_N\!\left(
 e^{-2\pi i(a-b+Nm)/n}
\right).
\tag{7}
\]

The factor `p` from the fiber average cancels the `1/p` in the normalized branching weights. Therefore

\[
\boxed{
(C_{N,p})_{ab}
=-\frac1{h_N}
\sum_{m=0}^{p-1}
E_N\!\left(
 e^{-2\pi i(a-b+Nm)/(Np)}
\right)
K_{Np}(a-b+Nm).
}
\tag{8}
\]

This identity is finite and exact. It also explains why a finite-prime compression need not literally commute with the parent operator: the coefficient-energy polynomial `E_N` inserts a phase-dependent weight along the `p` lifted chord classes. The question is whether that weight survives as a new operator when the fresh prime grows.

## 3. Removing the coefficient-energy phase gives exactly the parent chord

The unweighted sum in (8) is not merely asymptotic. The classical differentiated cotangent multiplication identity gives, for `a\ne b mod N`,

\[
\sum_{m=0}^{p-1}
\csc^2\!\left(
\frac{\pi(a-b+Nm)}{Np}
\right)
=
p^2\csc^2\!\left(
\frac{\pi(a-b)}N
\right).
\tag{9}
\]

After the normalizations in (5),

\[
\boxed{
\sum_{m=0}^{p-1}K_{Np}(a-b+Nm)
=K_N(a-b).
}
\tag{10}
\]

Hence (8) differs from the parent off-diagonal entry only by replacing the constant `h_N` with `E_N` evaluated at roots converging to `1` on the singular chord classes.

Put

\[
M_N:=\sum_{k=0}^{d}k c_k^2.
\tag{11}
\]

For `theta in R`,

\[
|E_N(e^{-2i\theta})-h_N|
\le
2M_N|\sin\theta|,
\tag{12}
\]

because `|sin(k theta)|<=k|sin theta|`. Multiplying (12) by the inverse-square kernel in (8) leaves one cosecant. For the shifted `p`-grid in (9), the elementary harmonic estimate

\[
\sum_{m=0}^{p-1}
\left|
\csc\!\left(
\frac{\pi(a-b+Nm)}{Np}
\right)
\right|
=O_N(p\log p)
\tag{13}
\]

therefore yields

\[
\boxed{
(C_{N,p})_{ab}
= -K_N(a-b)
+O_N\!\left(\frac{\log p}{p}\right)
}
\qquad(a\ne b),
\tag{14}
\]

which is (2). The limiting off-diagonal geometry is exactly the original parent geometry, not a new coefficient-weighted kernel.

## 4. The residual row-sum defect also vanishes

The only remaining issue is the diagonal. Because the branching weights vary inside each child fiber, `C_{N,p}` is not itself exactly a graph Laplacian at finite `p`; one cannot infer its diagonal from (14) by row sum alone. The row-sum defect is nevertheless forced to zero by the same low-frequency structure of `Phi_N`.

Let `1` denote the constant vector on `U(N)`. On the primitive child shell,

\[
(U_{N,p}1)(x)
=
\frac{\Phi_N(\zeta_{Np}^{x})}{\sqrt{p h_N}}.
\tag{15}
\]

Extend the right side to all `Np` vertices of the regular polygon. The internal primitive-shell Dirichlet energy is bounded by the full-polygon Dirichlet energy because it uses only a subset of the positive edges. The normalized full regular-polygon inverse-square chord Laplacian has the classical Fourier eigenvalues

\[
\lambda_k^{(n)}
=
\frac{k(n-k)}{2n^2},
\qquad 0\le k<n,
\tag{16}
\]

so Parseval applied to `Phi_N(z)=sum c_kz^k` gives the exact bound

\[
\begin{aligned}
\langle 1,C_{N,p}1\rangle
&=
\langle U_{N,p}1,A_{Np}U_{N,p}1\rangle\\
&\le
\frac1{2p h_N(Np)}
\sum_{k=0}^{d}c_k^2k(Np-k)\\
&\le
\boxed{
\frac{M_N}{2p h_N}.
}
\tag{17}
\end{aligned}
\]

The same edge-subset comparison and (16) give the uniform operator bound

\[
0\le C_{N,p}\le \frac18 I.
\tag{18}
\]

For a positive operator, `C^2<=||C||C`; therefore (17)--(18) imply

\[
\boxed{
\|C_{N,p}1\|
=O_N(p^{-1/2}).
}
\tag{19}
\]

Since `A_N1=0`, equations (14) and (19) determine the diagonal through

\[
(C_{N,p})_{aa}
=(C_{N,p}1)_a-
\sum_{b\ne a}(C_{N,p})_{ab}.
\tag{20}
\]

The parent dimension `phi(N)` is fixed, so (14), (19), and (20) give the operator-norm limit (1).

## 5. Exact control and interpretation

For `N=6`,

\[
\Phi_6(z)=z^2-z+1,
\qquad h_6=3,
\]

and the parent primitive shell is `{1,5}`. Its normalized chord conductance is

\[
K_6(1-5)=\frac1{108},
\]

so

\[
A_6=
\frac1{108}
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix},
\qquad
\operatorname{Spec}(A_6)=\left\{0,\frac1{54}\right\}.
\tag{21}
\]

PC-230 says that the exactly isometric Cauchy-residue branch into every sufficiently large fresh-prime shell, followed by the **full primitive inverse-square chord operator there**, compresses back to (21). The finite-prime matrices can have a small positive constant-mode eigenvalue and complex Hermitian off-diagonal phases, but both effects vanish in the fresh-prime limit. The surviving nonzero spectrum is simply the old parent spectrum.

This is stronger than saying that the residue branching itself is flat. `A_{Np}` genuinely couples distinct child fibers, so `U_{N,p}^*A_{Np}U_{N,p}` is precisely the kind of source-forced parent-mixing insertion that PC-229 left outside its diagonal `B^*B` theorem. The result shows that the most canonical such insertion still renormalizes to the already-present parent chord geometry.

The relationship with PC-155 is complementary. PC-155 compresses the fine chord operator through the **fiber-constant** refinement pullback and obtains an exact finite-prime commuting conjugacy polynomial. PC-230 uses the nonconstant cyclotomic Cauchy-residue weights of PC-229 instead. The finite-prime compression is no longer the PC-155 polynomial, but the coefficient-weighted defect disappears when the new prime resolves the fixed coarse polynomial on an increasingly fine fiber.

## 6. Prior-art and novelty audit

Every analytic ingredient exposed by the proof is classical. Calogero and Perelomov, *Some Diophantine relations involving circular functions of rational angles*, Linear Algebra Appl. 25 (1979), 91--94, compute the regular-polygon `csc^{-2}` Fourier spectrum used in (16); this is already the line's source anchor for PC-032. The cosecant multiplication law in (9) is the differentiated cotangent multiplication formula already used in PC-155 and belongs to standard trigonometric partial-fraction theory. Liu and Xin, *Root-of-unity weighted trigonometric power sums: a constant term approach*, arXiv:2607.29130 (2026), provide a current neighboring boundary for root-of-unity-weighted cosecant sums. Finite-fiber orthogonality in (7) is ordinary discrete Fourier analysis.

A directed literature search around cyclotomic-polynomial weights, primitive-root inverse-square Laplacians, weighted cosecant refinement, and cyclotomic derivative/residue branching did not locate this exact compressed-operator limit. That absence is not treated as a historical novelty claim. The durable content is the project-specific conjunction of the **PC-229 source-derived residue isometry** with the **PC-155/PC-032 source-derived primitive chord Hessian**, and the proof that their canonical composition returns to the parent operator rather than opening a new fixed-base spectral channel.

No Riemann-zeta zero set, functional-equation symmetry, or critical-line constraint is generated by (1). The limit is an operator already present before the fresh prime is adjoined.

## 7. Boundary for the Prime-Circle program

The following route is therefore closed in the fixed-base large-fresh-prime regime:

\[
\boxed{
\text{PC-229 Cauchy-residue branch}
\longrightarrow
\text{primitive inverse-square chord mixing at }Np
\longrightarrow
\text{compress to the parent}
\longrightarrow
\text{new limiting RH operator}.
}
\]

The canonical chord insertion is asymptotically an identity renormalization of `A_N`.

The theorem is intentionally not an all-operator or simultaneous-growth no-go. It does not cover a regime where `N` and the squarefree radical grow together so that the constants in (1)--(2) must be controlled uniformly; fresh primes `p<=phi(N)` where PC-229's branching positive square is already nonflat; a distinct geometry-forced operator inserted before compression; several noncommuting insertions retained without returning to the parent after each step; the full PC-227 numerator/shift/normalization state; or the global uniformization/accessory-parameter sector. Those remain the correct places to look if the squarefree packet architecture is to evade the current chain of fixed-base classicalizations.