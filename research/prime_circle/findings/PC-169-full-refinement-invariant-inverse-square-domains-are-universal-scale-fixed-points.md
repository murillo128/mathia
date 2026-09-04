# PC-169 — full-refinement-invariant inverse-square domains are universal scale fixed points

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for obtaining a new Prime-Circle/RH mechanism from the self-adjoint-extension ambiguity of the inverse-square radial operator left open by PC-168. The complete Prime-Circle refinement semigroup does not turn that boundary ambiguity into arithmetic spectral data. In the medium/weak regime it leaves only the classical scale-fixed extensions, at the critical coupling only the no-log fixed extension survives, in the essentially self-adjoint regime there is no boundary freedom at all, and in the supercritical regime no self-adjoint extension can be invariant under both refinements `2` and `3`. Thus the familiar inverse-square limit cycle cannot be made intrinsic to the full roots-of-unity refinement system.

The theorem is deliberately radial. It closes the most canonical domain anomaly attached to PC-168's forced scalar potential `c/t^2`; it does not classify shell-dependent, angular-mode-coupling, nonlocal, or root-supported boundary conditions that use additional old/new incidence.

## 1. The remaining local ambiguity is the domain, not the coefficient

PC-168 showed that exact covariance of a finite-order local operator under every power refinement

\[
D_n(t,\theta)=(nt,n\theta),\qquad n\ge2,
\]

forces its coefficients to universal homogeneous cone form. For a second-order scalar Schrödinger sector the only refinement-covariant local singularity is therefore an inverse-square potential in logarithmic radial distance. The angular-constant sector reduces to

\[
H_g=-\frac{d^2}{dt^2}+\frac{g}{t^2},
\qquad t>0,
\tag{1}
\]

initially on `C_c^\infty(0,\infty)` in `L^2(0,\infty,dt)`. The coefficient `g` is already universal rather than shell-derived. The only canonical local escape left by PC-168 is whether choosing a self-adjoint domain at the singular endpoint `t=0` can supply a nontrivial refinement-sensitive scale or phase.

Use the unitary half-density dilation

\[
(S_a f)(t)=a^{1/2}f(at),\qquad a>0.
\tag{2}
\]

The differential expression obeys

\[
\boxed{H_g S_a=a^2 S_a H_g.}
\tag{3}
\]

A self-adjoint realization is exactly compatible with a Prime-Circle radial refinement `n` when

\[
\boxed{S_n\operatorname{Dom}(H)=\operatorname{Dom}(H).}
\tag{4}
\]

The full intrinsic refinement requirement asks for (4) for every integer `n>=2`. Because `S_n` is unitary, equality is the natural domain version of the operator covariance used in PC-168; it also automatically gives compatibility with the inverse dilation on the radial half-line.

## 2. Medium/weak coupling leaves only two universal scale-fixed domains

For

\[
-\frac14<g<\frac34,
\]

put

\[
\nu=\sqrt{g+\frac14}\in(0,1).
\tag{5}
\]

Both independent zero-energy behaviors are square-integrable at the origin, and every maximal-domain function has boundary coefficients of the form

\[
f(t)=A\,t^{1/2-\nu}+B\,t^{1/2+\nu}+o(t^{1/2+\nu})
\tag{6}
\]

in the standard boundary-coordinate sense. Self-adjoint extensions are the one-real-parameter family of real projective relations between `A` and `B`; write it as

\[
B=\lambda A,
\qquad \lambda\in\mathbb R\cup\{\infty\}.
\tag{7}
\]

Under (2),

\[
A\mapsto a^{1-\nu}A,
\qquad
B\mapsto a^{1+\nu}B,
\]

so the extension parameter transforms exactly as

\[
\boxed{\lambda\mapsto a^{2\nu}\lambda.}
\tag{8}
\]

For any nontrivial dilation `a != 1`, the only fixed points of (8) on the real projective line are

\[
\boxed{\lambda=0\quad\text{and}\quad\lambda=\infty.}
\tag{9}
\]

Hence requiring all Prime-Circle refinements does not select a prime-dependent family: it leaves exactly the two classical scale-free boundary branches already fixed by one dilation. Every finite nonzero extension parameter introduces a length scale and is moved to a different self-adjoint realization by refinement.

At the endpoint `g>=3/4`, the singular endpoint is limit-point, so the minimal operator is essentially self-adjoint and there is no extension parameter to exploit. This entire regime is therefore automatically refinement compatible but spectrally prime-blind at the domain level.

## 3. At the critical coupling only the no-log domain survives

For

\[
g=-\frac14,
\]

the two independent local behaviors coalesce and the boundary expansion becomes

\[
f(t)=t^{1/2}\bigl(A+B\log t\bigr)+o(t^{1/2}).
\tag{10}
\]

Dilation sends

\[
(A,B)\mapsto a\bigl(A+B\log a,\,B\bigr).
\tag{11}
\]

Thus a finite projective boundary parameter is translated by `log a` rather than rescaled. The unique projective fixed line for any `a != 1` is

\[
\boxed{B=0.}
\tag{12}
\]

So even at the critical inverse-square coupling there is no logarithmic boundary phase compatible with the full refinement system. The only invariant extension is the classical no-log scale-fixed domain.

This is already enough to rule out a tempting analogy in which the logarithmic endpoint coordinate itself might encode the multiplicative refinement tower: any nonzero logarithmic admixture is shifted by every power map and cannot define one common self-adjoint realization.

## 4. The supercritical limit cycle is incompatible with refinements 2 and 3

The sharpest obstruction occurs for

\[
g<-\frac14.
\]

Write

\[
\sigma=\sqrt{-g-\frac14}>0.
\tag{13}
\]

Near the origin the two oscillatory scale modes are

\[
f(t)=t^{1/2}\left(A t^{i\sigma}+B t^{-i\sigma}\right)+o(t^{1/2}),
\tag{14}
\]

and self-adjointness fixes their relative modulus, leaving one phase

\[
\frac BA=e^{i\phi}.
\tag{15}
\]

Under dilation,

\[
\frac BA\mapsto a^{-2i\sigma}\frac BA.
\tag{16}
\]

Therefore a supercritical self-adjoint domain is invariant under the scale `a` exactly when

\[
\boxed{\sigma\log a\in\pi\mathbb Z.}
\tag{17}
\]

This is the standard discrete-scale/limit-cycle phenomenon: for one chosen scale there can be a cyclic subgroup of dilations preserving the domain. But the Prime-Circle object does not contain one preferred scale; it contains every integer power refinement. Already `2` and `3` are fatal. Simultaneous invariance would require integers `k,l` with

\[
\sigma\log2=\pi k,
\qquad
\sigma\log3=\pi l.
\tag{18}
\]

Since `sigma>0`, both integers are nonzero. Dividing gives

\[
\frac{\log2}{\log3}=\frac{k}{l}\in\mathbb Q.
\tag{19}
\]

But (19) would imply `2^l=3^k`, impossible by unique factorization. Consequently

\[
\boxed{
 g<-\frac14
 \quad\Longrightarrow\quad
 \text{no self-adjoint domain is invariant under both }S_2\text{ and }S_3.
}
\tag{20}
\]

A fortiori there is no supercritical self-adjoint realization compatible with the complete Prime-Circle refinement semigroup.

This is stronger for the present line than the usual statement that continuous scale invariance is anomalously broken. A supercritical extension can retain a **single** discrete scaling ratio, but two multiplicatively independent intrinsic refinements already destroy that repair. Choosing a special cyclic refinement subgroup instead would discard part of the canonical roots-of-unity refinement structure and insert a preferred scale not supplied by the research object.

## 5. Complete radial-domain classification under full refinement

Combining the four coupling regimes gives the exact refinement-compatible domain classification for (1):

\[
\boxed{
\begin{array}{c|c}
\text{coupling} & \text{self-adjoint domains invariant under all integer refinements}\\
\hline
g\ge 3/4 & \text{the unique self-adjoint realization}\\
-1/4<g<3/4 & \text{exactly the two scale-fixed power-law domains}\\
g=-1/4 & \text{exactly the no-log scale-fixed domain}\\
g<-1/4 & \text{none}
\end{array}}
\tag{21}
\]

Nothing in (21) depends on `phi(n)`, `Lambda(n)`, exact-order shells, Ramanujan modes, old/new incidence, cyclotomic resultants, or the common anchored vertex beyond the universal radial refinement `t -> nt`. In the regimes where a compatible domain exists, all continuous boundary-scale freedom has disappeared. In the regime where a limit-cycle phase exists, the complete integer refinement family is incompatible with it.

The matched control is therefore decisive: erase every root and every primitive-shell label, retain only the half-line together with the two dilations `t -> 2t` and `t -> 3t`, and the classification above is unchanged. The domain mechanism cannot distinguish prime-circle arithmetic from this prime-blind dilation control.

## 6. Prior art and novelty audit

The self-adjoint-extension mathematics is classical, and no novelty is claimed for it. D. M. Gitman, I. V. Tyutin and B. L. Voronov, *Self-adjoint extensions and spectral analysis in Calogero problem*, Journal of Physics A 43 (2010) 145205, DOI `10.1088/1751-8113/43/14/145205`, arXiv:`0903.5277`, gives a rigorous classification of all self-adjoint realizations of `-d^2/dx^2+alpha/x^2` and explicitly analyzes the fate of scale symmetry. In particular it identifies the two scale-symmetric extensions for `-1/4<alpha<3/4`, the unique critical scale-symmetric choice at `alpha=-1/4`, essential self-adjointness/scale symmetry for `alpha>=3/4`, and unavoidable scale-symmetry breaking in the strongly attractive regime.

M. Bawin and S. A. Coon, *Singular inverse square potential, limit cycles, and self-adjoint extensions*, Physical Review A 67 (2003) 042712, DOI `10.1103/PhysRevA.67.042712`, is a primary prior-art anchor for the supercritical limit-cycle interpretation. The newer discussion by S. Ohya, *Scale Invariance Breaking and Discrete Phase Invariance in Few-Body Problems*, arXiv:`2601.09266` (2026), is a current neighboring reminder that inverse-square boundary conditions support several standard discrete remnants of scale symmetry. These sources place the endpoint anomaly itself firmly inside established conformal/inverse-square quantum mechanics.

The line-specific deduction is much narrower: because Prime Circle intrinsically supplies **all** power refinements, not one selected discrete scale, its canonical domain must survive at least two multiplicatively independent dilations. Equation (20) then kills the supercritical limit-cycle escape by the elementary independence of `2` and `3`, while (8) and (11) collapse the remaining extension families to their universal fixed points. Targeted searches across inverse-square self-adjoint extensions, scale anomalies, limit cycles, and symmetry-preserving domains found the classical structures above, not a roots-of-unity/RH mechanism generated by simultaneous integer refinements. Absence of an exact wording match is not treated as historical novelty.

## 7. Scope, falsifiers, and surviving frontier

The assumptions carrying the negative result are explicit. It concerns the angular-constant radial sector of the universal inverse-square operator forced by PC-168, uses an ordinary self-adjoint realization on `L^2(0,infinity)`, and demands exact domain covariance under the intrinsic integer radial dilations. It does not say that every possible boundary construction on the two-dimensional punctured cylinder is prime-blind.

In particular, the theorem does **not** classify a domain that couples distinct angular modes, a boundary operator built explicitly from the primitive/old root incidence, distributional coefficients supported on the unit circle, shell-dependent or level-dependent extension data, nonlocal boundary conditions, nonlinear operators, or the global uniformization/monodromy branch. Such a construction would contain mathematical data absent from (1) and must be audited on its own. Conversely, merely choosing `g`, an extension phase, or a preferred discrete scaling ratio after inspecting arithmetic data would fail the Prime-Circle intrinsicness and matched-control requirements.

What is now closed is the canonical local continuation

\[
\text{full power refinement}
\longrightarrow
\frac{g}{t^2}\text{ local singularity}
\longrightarrow
\text{self-adjoint extension / scale anomaly}
\longrightarrow
\text{new prime-sensitive spectrum}
\longrightarrow
\text{RH}.
\]

The coefficient no-go of PC-168 and the domain classification here meet cleanly: local refinement covariance leaves only universal inverse-square coefficients, and exact refinement-compatible radial domains either collapse to universal scale fixed points or do not exist. Any surviving domain-based mechanism must therefore derive genuinely additional boundary data from the roots themselves rather than from inverse-square scale anomaly alone.
