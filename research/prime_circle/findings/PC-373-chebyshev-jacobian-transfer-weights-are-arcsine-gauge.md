# PC-373 — Chebyshev Jacobian transfer weights are an arcsine gauge

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the derivative-weighted transfer-operator branch left open by PC-372. On the shell-2 real-cyclotomic coordinate, the canonical Jacobian weight of the source-forced Chebyshev refinement is a multiplicative coboundary. On every finite primitive/order-shell transfer diagram, and algebraically on finitely supported functions on interior torsion points, the derivative-weighted operator is exactly a diagonal gauge of the unweighted Chebyshev transfer operator, up to the scalar `p^{-s}`. Along refinement paths the gauge telescopes, so the Jacobian contributes no new shell arithmetic or RH spectral parameter.

This is deliberately not a theorem about every global Banach/Hilbert completion on `[0,1]`: the gauge vanishes at the endpoints and can become singular there. Any genuinely new spectrum caused by endpoint domain conditions is therefore outside this no-go and would need an independently source-forced boundary construction. The finite primitive-shell arithmetic itself has no such endpoint obstruction.

## 1. The exact Jacobian is an endpoint ratio

PC-372 identifies the source refinement on

\[
\lambda(z)=\frac{2+z+z^{-1}}4=\cos^2\frac\theta2
\]

with

\[
C_p(\lambda)=\frac{1+T_p(2\lambda-1)}2,
\qquad C_p(\lambda(z))=\lambda(z^p).
\tag{1}
\]

For `0<lambda<1`, write `2 lambda-1=cos theta` with `0<theta<pi`, and define the intrinsic arcsine gauge

\[
h(\lambda):=2\sqrt{\lambda(1-\lambda)}=\sin\theta.
\tag{2}
\]

Since `T_p'(x)=p U_{p-1}(x)`, differentiation of (1) gives

\[
C_p'(\lambda)
=p\,U_{p-1}(2\lambda-1)
=p\frac{\sin(p\theta)}{\sin\theta}.
\tag{3}
\]

Moreover

\[
h(C_p(\lambda))=|\sin(p\theta)|.
\tag{4}
\]

Hence, away from the endpoint/critical locus,

\[
\boxed{
|C_p'(\lambda)|
=p\,\frac{h(C_p(\lambda))}{h(\lambda)}.
}
\tag{5}
\]

Equivalently,

\[
(C_p'(\lambda))^2 h(\lambda)^2
=p^2 h(C_p(\lambda))^2.
\tag{6}
\]

Equation (5) is the decisive identity. The logarithmic geometric potential is

\[
-s\log|C_p'|
=-s\log p+s\log h-s\log(h\circ C_p),
\tag{7}
\]

so it is a constant plus a dynamical coboundary.

For the primitive order sets of PC-372 with `n>2`, every `lambda in Lambda_n` lies strictly in `(0,1)`. A critical point of `C_p` maps to `0` or `1`, so no preimage of an interior primitive-shell point is critical. Thus (5) is finite and nonzero on every finite shell incidence relevant here.

## 2. Perron–Frobenius/Ruelle weighting is exact diagonal gauge

For complex `s`, using the positive real logarithm of `|C_p'|`, consider the canonical geometric transfer operator on interior points,

\[
(\mathcal L_{p,s}f)(x)
:=\sum_{C_p(y)=x}|C_p'(y)|^{-s}f(y).
\tag{8}
\]

Let `\mathcal L_{p,0}` denote the unweighted preimage sum and `M_g` multiplication by `g`. From (5), for every interior target `x`,

\[
|C_p'(y)|^{-s}
=p^{-s}h(y)^s h(x)^{-s}.
\]

Therefore

\[
\boxed{
\mathcal L_{p,s}
=p^{-s}M_{h^{-s}}\,\mathcal L_{p,0}\,M_{h^s}.
}
\tag{9}
\]

On any finite primitive/order-shell diagram all diagonal factors are invertible. The Jacobian-weighted incidence matrix is therefore exactly left/right diagonally equivalent to the unweighted incidence matrix, with the only prime-dependent scalar `p^{-s}`.

For `s=1`, the same identity immediately recovers the classical invariant arcsine density. Since an interior point has `p` preimages,

\[
\mathcal L_{p,1}(h^{-1})=h^{-1}.
\tag{10}
\]

After the affine change from `[-1,1]` to `[0,1]`, this is the density proportional to `1/sqrt(lambda(1-lambda))`.

A rectangular child-to-parent shell block should not be called a similarity: its Euclidean singular values may change under the two endpoint diagonal factors. The invariant statement needed here is the stronger path statement below: the weights themselves contain only endpoint gauge and the scalar covering degree.

## 3. Every refinement path telescopes

Chebyshev refinement composes multiplicatively,

\[
C_m\circ C_n=C_{mn}.
\tag{11}
\]

Applying (5) to `C_m` gives, for every interior point on which the orbit avoids the endpoints,

\[
\boxed{
|C_m'(\lambda)|
=m\frac{h(C_m(\lambda))}{h(\lambda)}.
}
\tag{12}
\]

Consequently a chain of prime refinements `p_1,...,p_k` has total Jacobian weight

\[
\prod_{j=1}^k |C_{p_j}'(\lambda_{j-1})|^{-s}
=(p_1\cdots p_k)^{-s}
\frac{h(\lambda_0)^s}{h(\lambda_k)^s}.
\tag{13}
\]

All intermediate geometry cancels. In particular, on a closed interior periodic cycle of length `k` for `C_p`,

\[
\boxed{
\prod_{j=0}^{k-1}|C_p'(C_p^j\lambda)|^{-s}=p^{-sk}.
}
\tag{14}
\]

Thus the canonical geometric potential assigns no orbit-dependent arithmetic weight at all after the endpoint coboundary is removed.

The same conclusion survives a finite combination of prime directions on a common interior state space:

\[
\sum_p a_p\mathcal L_{p,s}
=M_{h^{-s}}
\left(\sum_p a_p p^{-s}\mathcal L_{p,0}\right)
M_{h^s}.
\tag{15}
\]

Equation (15) does **not** say that an arbitrary chosen prime sum has trivial spectrum. It says that the derivative/Jacobian geometry contributes only the scalar factors `p^{-s}` and one common diagonal gauge. Any zeta or Dirichlet series obtained by summing those scalars with chosen coefficients comes from the external semigroup aggregation, not from new Prime-Circle shell geometry; this is precisely the classical cyclotomic/Bost–Connes boundary already identified locally before PC-372.

## 4. Why endpoint singularities do not rescue the finite shell arithmetic

The conjugating multiplier `h^s` is harmless on every finite primitive shell, because `Lambda_n subset (0,1)` for `n>2`. It is also harmless algebraically on finitely supported functions on the union of interior torsion/preperiodic points. There equation (9) is an exact invertible diagonal conjugacy whenever domain and codomain are assembled on a common invariant interior space.

Globally on `[0,1]`, however, `h(0)=h(1)=0`. Multiplication by `h^{s}` or `h^{-s}` can therefore be unbounded or noninvertible on a chosen Banach/Hilbert completion. A transfer operator with boundary conditions sensitive to this singularity can have additional domain-dependent spectral information. That possibility is **not** ruled out here.

But such information is not present in the finite primitive-shell incidence data: the endpoints correspond to the exceptional real roots `z=1` and `z=-1`, not to primitive `n>2` shell points. To turn the endpoint singularity into a Prime-Circle mechanism, one would have to derive the completion, boundary condition, and observable from the original geometry and then survive a separate novelty/RH audit. Merely choosing a function space in which the gauge becomes singular is not an intrinsic spectral mechanism.

## 5. Prior-art and novelty audit

The dynamical ingredients are classical. Abraham Boyarsky and Paweł Góra, **Invariant measures for Chebyshev maps**, *Journal of Applied Mathematics and Stochastic Analysis* 14:3 (2001), 257–264, DOI `10.1155/S1048953301000211`, explicitly record the invariant density `dx/(pi sqrt(1-x^2))` for integer Chebyshev maps and the differential conjugacy to piecewise-linear Markov dynamics. Qiao Bi and I. Antoniou, **Spectral decomposition of Chebyshev maps**, *Physica A* 233 (1996), 449–457, DOI `10.1016/S0378-4371(96)00219-1`, give a classical Frobenius–Perron spectral decomposition for Chebyshev maps. David Ruelle, **The thermodynamic formalism for expanding maps**, *Communications in Mathematical Physics* 125 (1989), 239–262, DOI `10.1007/BF01217908`, is the standard transfer-operator/dynamical-zeta background for geometric potentials.

No historical novelty is claimed for the arcsine measure, Chebyshev/tent-map conjugacy, or transfer operators. The project-local contribution is the exact classification of the **specific derivative-weighted branch left open by PC-372**: once the shell-2 order coordinate is known to be the real-cyclotomic Chebyshev quotient, its canonical Jacobian potential is not an additional arithmetic decoration. Equations (5), (9), and (13) show directly that it is a coboundary plus the scalar degree.

The negative conclusion therefore does not depend on failure to find a paper attaching RH to this construction. It follows from exact cohomological triviality of the only canonical derivative weight supplied by the Chebyshev refinement itself.

## 6. Falsification controls and surviving frontier

The argument can be killed only by changing a load-bearing hypothesis. Direct checks are:

1. verify (6) polynomially for each `p`; it follows identically from `T_p'(x)=pU_{p-1}(x)` and `1-T_p(x)^2=(1-x^2)U_{p-1}(x)^2`;
2. verify that critical points map to endpoints, so finite primitive-shell transfers never divide by zero;
3. build the weighted child/parent incidence matrix from PC-372 and check entrywise that it equals `p^{-s}D_parent^{-s} A D_child^s`;
4. multiply such blocks along a refinement path and confirm cancellation of every intermediate diagonal factor;
5. distinguish this diagonal equivalence from Euclidean singular-value invariance of one rectangular block, which is not claimed.

What survives is correspondingly narrower. A viable order-sensitive transfer mechanism must use a weight **not cohomologous to the arcsine endpoint gauge**, a source-forced endpoint/domain structure with genuine arithmetic content, a nonlinear/nonlocal cross-shell interaction, or a coupling of prime directions whose extra weights are not just products of the Jacobians of the commuting Chebyshev maps. The canonical derivative-weighted Perron–Frobenius/Ruelle repair itself is closed.

## Research consequence

PC-372 left derivative-weighted transfer operators outside its theorem. The canonical such weight is now classified exactly:

\[
\boxed{
\text{Chebyshev Jacobian weight}
=\text{degree scalar}\times\text{endpoint coboundary}.
}
\tag{16}
\]

So passing from unweighted real-cyclotomic refinement to its natural Jacobian-weighted transfer operator does not add an independent arithmetic carrier. Any future Prime-Circle transfer candidate must identify a different source-forced weight or domain effect and justify why that extra structure is intrinsic rather than inserted to manufacture zeta-sensitive spectrum.
