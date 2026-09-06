# PC-183 — refinement-covariant positive two-depth kernels have only the Mangoldt boundary selector

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-MELLIN-STRUCTURE` + `DECISIVE-NEGATIVE` for obtaining a stronger prime-power/RH mechanism by replacing the positive `w(min(u,v))` kernels of PC-182 with an arbitrary continuous positive two-depth kernel that is intrinsically covariant under every Prime-Circle radial refinement.

PC-182 left two immediate scalar/nonlocal escapes after proving that monotone depth weights fill the exact Mangoldt nullspace: use a sign-changing/nonmonotone radial law forced by refinement, or use a genuinely two-depth positive kernel outside the Stieltjes family `w(min(u,v))`. The full power-refinement semigroup closes both natural refinement-covariant versions.

Let `rho_n(x)=-d/dx log Phi_n(e^{-x})` be the signed radial flux from PC-179. If a continuous Hermitian positive-semidefinite kernel `K(u,v)` on `(0,infinity)^2` transforms by a scalar under every common radial refinement `u,v -> q u,q v`, then full integer refinement and continuity force ordinary real homogeneity. In log-depth coordinates, positivity then turns the remaining ratio dependence into a positive-definite function, so Bochner/Mellin harmonic analysis gives an exact spectral mixture of the shell Mellin transforms `R_n(s)` from PC-179.

The resulting selector theorem is rigid:

\[
Q_K(n)
:=\int_0^\infty\!\!\int_0^\infty
\rho_n(u)K(u,v)\rho_n(v)\,du\,dv.
\]

If `Q_K(pq)=0` for every pair of distinct primes and `Q_K(p^a)>0` for at least one prime power, then necessarily

\[
\boxed{K(u,v)\equiv c,\qquad c>0,}
\]

and therefore

\[
\boxed{Q_K(n)=c\,\Lambda(n)^2.}
\]

So the only positive, scalar-refinement-covariant two-depth kernel that preserves the exact prime-power nullspace is the constant kernel, which is just the already-known total signed-flux boundary form. Any nonconstant positive homogeneous kernel either leaks positive mass to some mixed-prime shell or is spectrally invisible to every cyclotomic flux.

A parallel scalar corollary closes the refinement-forced nonmonotone-weight repair in the natural affine class: if a locally absolutely continuous depth weight has a finite anchor value and transforms affinely under every refinement, then it is `w(x)=w(0)+C x^alpha` with `alpha>0` unless it is constant. Hence `w'` has one sign and PC-182 applies; a nonconstant affine refinement-covariant scalar weight cannot preserve the Mangoldt nullspace.

## 1. Full integer refinement forces real homogeneity

The log-radial coordinate of PC-165 is

\[
x=-\log r>0,
\]

and the intrinsic power map `z -> z^q` acts by

\[
x\longmapsto qx.
\]

Let `K:(0,infinity)^2 -> C` be continuous, Hermitian and positive semidefinite. Assume the weakest scalar covariance compatible with using the same two-depth kernel at every level: for every integer `q>=2` there is a scalar `a_q` such that

\[
\boxed{
K(qu,qv)=a_qK(u,v)
}
\qquad(u,v>0).
\tag{1}
\]

If `K` is nonzero, positivity implies `K(x,x)>0` for some `x`. Equation (1) then gives

\[
a_q=\frac{K(qx,qx)}{K(x,x)}>0.
\]

Composition gives `a_{mn}=a_ma_n`. Applying (1) backwards and then forwards extends the relation to every positive rational `r=m/n`:

\[
K(ru,rv)=a_rK(u,v),
\qquad
a_r:=a_m/a_n.
\tag{2}
\]

For fixed `u,v` with `K(u,v) != 0`, continuity of `K` makes `a_r` continuous at `r=1` on the dense subgroup `Q_{>0}`. Thus the standard continuous multiplicative functional equation applies: there is a real `gamma` such that

\[
\boxed{
a_r=r^\gamma}
\qquad(r\in\mathbb Q_{>0}).
\tag{3}
\]

Continuity in `(u,v)` extends (3) from rational to every real scale `lambda>0`:

\[
\boxed{
K(\lambda u,\lambda v)=\lambda^\gamma K(u,v).
}
\tag{4}
\]

This is the two-depth analogue of the dense-refinement rigidity already encountered for local metrics in PC-167. A preferred discrete scale could support log-periodic freedom; the complete Prime-Circle refinement semigroup does not.

For the shell energies below to be finite on prime-power fluxes, the Mellin line must satisfy `1+gamma/2>0`, equivalently `gamma>-2`. This is also the natural integrability threshold because every `rho_n` is bounded at `0+` and decays exponentially at infinity.

## 2. Positivity converts the ratio freedom into a Bochner measure

Write `u=e^x`, `v=e^y`, and remove the homogeneous envelope:

\[
H(x,y)
:=e^{-\gamma(x+y)/2}K(e^x,e^y).
\tag{5}
\]

Equation (4) says

\[
H(x+t,y+t)=H(x,y)
\qquad(t\in\mathbb R),
\]

so `H` depends only on the log-ratio. There is a continuous function `kappa` such that

\[
\boxed{
K(u,v)
=(uv)^{\gamma/2}
\kappa(\log u-\log v).
}
\tag{6}
\]

Multiplying a positive kernel by positive diagonal factors preserves positive semidefiniteness, hence `kappa(x-y)` is a continuous positive-definite kernel on the additive group `R`. Bochner's theorem therefore gives a finite positive measure `mu` with

\[
\boxed{
\kappa(t)=\int_{\mathbb R}e^{it\xi}\,d\mu(\xi).
}
\tag{7}
\]

Equivalently,

\[
K(u,v)
=(uv)^{\gamma/2}
\int_{\mathbb R}
\left(\frac uv\right)^{i\xi}
d\mu(\xi).
\tag{8}
\]

The factorization of homogeneous kernels into a power envelope times a ratio kernel, and their Mellin diagonalization, are classical scale-invariant operator theory. A particularly direct modern prior-art statement is L. A. Jacobs and A. Frank, *Multicriticality and Scaling: Mellin Spectral Theory, and the Decoupling of Geometric and Spectral Exponents*, arXiv:2606.07644 (2026), which writes exactly this homogeneous-kernel/ratio/Mellin structure. No novelty is claimed for (4)--(8).

## 3. Every positive two-depth energy is a positive Mellin mixture

PC-179 proved that

\[
\mathcal R_n(s)
:=\int_0^\infty \rho_n(x)x^{s-1}\,dx
\]

is holomorphic for `Re(s)>0` and satisfies the exact classical factorization

\[
\boxed{
\mathcal R_n(s)
=
-\Gamma(s)\zeta(s)\,
n^{1-s}
\prod_{p\mid n}(1-p^{s-1}).
}
\tag{9}
\]

Substituting (8) into the two-depth quadratic form and using `gamma>-2` gives

\[
\boxed{
Q_K(n)
=
\int_{\mathbb R}
\left|
\mathcal R_n\!\left(
1+\frac{\gamma}{2}+i\xi
\right)
\right|^2
 d\mu(\xi).
}
\tag{10}
\]

This is the key difference from an arbitrary spectral wrapper: the Mellin line is forced by the radial scaling degree of the kernel, the spectral measure is forced to be positive by the self-adjoint quadratic form, and the shell dependence is exactly the source-derived cyclotomic flux of PC-179.

Equation (10) also exposes the danger immediately. Because the integrand is nonnegative, exact nullity of one shell means its Mellin transform must vanish `mu`-almost everywhere; cancellations between unrelated spectral frequencies are impossible.

## 4. Mixed-prime nullity leaves only `s=1` or a common zeta zero

Assume

\[
Q_K(pq)=0
\qquad
\text{for every pair of distinct primes }p,q.
\tag{11}
\]

There are only countably many such pairs. By (10), there is therefore one full-`mu` set of frequencies on which

\[
\mathcal R_{pq}(s)=0
\qquad
\text{for every }p\ne q,
\tag{12}
\]

with

\[
s=1+\frac{\gamma}{2}+i\xi.
\]

Fix such an `s`. The removable point `s=1` must be kept separate because `zeta` has a pole there and the finite Euler factors cancel it. PC-179 already gives

\[
\mathcal R_n(1)=\Lambda(n),
\]

so `s=1` indeed annihilates every mixed-prime shell while retaining prime powers.

Now suppose `s != 1`. Since `Gamma` and the elementary power factor never vanish, equation (9) gives two possibilities. If `zeta(s)=0`, then

\[
\mathcal R_n(s)=0
\]

for **every** shell `n>1`; that spectral channel is arithmetically invisible, not a prime-power selector.

If instead `zeta(s) != 0`, then for every distinct `p,q`,

\[
(1-p^{s-1})(1-q^{s-1})=0.
\tag{13}
\]

Let

\[
S_s=\{p\text{ prime}:p^{s-1}=1\}.
\]

Condition (13) says that the complement of `S_s` contains at most one prime, so `S_s` contains at least two distinct primes `p,q`. Writing `s-1=\sigma+i\tau`, the equations `p^{s-1}=q^{s-1}=1` first force `sigma=0` from absolute values. They then give

\[
\tau\log p\in2\pi\mathbb Z,
\qquad
\tau\log q\in2\pi\mathbb Z.
\]

If `tau != 0`, their ratio would make `log p/log q` rational, hence `p^a=q^b` for nonzero integers `a,b`, impossible for distinct primes. Therefore `tau=0` and `s=1`, contradicting the standing assumption `s != 1`. Hence there is no third case, and

\[
\boxed{
\text{every frequency allowed by all mixed-prime null constraints lies at }
s=1
\text{ or at a zero of }\zeta.
}
\tag{14}
\]

## 5. A nonzero prime-power response forces the constant kernel

Now require that the positive form actually retain the selector:

\[
Q_K(p^a)>0
\]

for at least one prime power. A frequency with `zeta(s)=0` contributes zero to **all** shells, including every prime power. Hence positive prime-power energy requires positive `mu`-mass on the alternative (14).

But `s=1` lies on the fixed Mellin line only when

\[
\boxed{\gamma=0,\qquad \xi=0.}
\tag{15}
\]

Once `gamma=0`, every remaining frequency lies on `Re(s)=1`. The classical Hadamard--de la Vallee Poussin theorem gives

\[
\zeta(1+i\xi)\ne0
\qquad(\xi\ne0).
\]

Therefore the zeta-zero alternative is absent on this line, and (12)--(15) force

\[
\boxed{
\mu=c\,\delta_0
}
\qquad(c>0).
\tag{16}
\]

Equations (7)--(8) now give

\[
\boxed{
K(u,v)\equiv c.
}
\tag{17}
\]

Finally PC-179 gives

\[
\mathcal R_n(1)=\Lambda(n),
\]

so

\[
\boxed{
Q_K(n)=c\,\Lambda(n)^2.
}
\tag{18}
\]

This is exactly the old boundary selector written as a two-depth kernel:

\[
Q_K(n)
=
c
\left(\int_0^\infty\rho_n(u)\,du\right)^2.
\]

The genuinely two-depth positive geometry has disappeared.

The use of the zero-free line is classical rather than RH-sensitive: `zeta(s) != 0` on `Re(s)=1` is the Hadamard--de la Vallee Poussin input to the prime number theorem. DLMF §25.10 records this standard result. No assumption about zeros in the open critical strip is used.

## 6. Stress tests and the critical-line trap

The constant kernel is an exact sharpness test: it satisfies every hypothesis, annihilates every mixed-prime shell, and gives `Lambda(n)^2` on prime powers.

A nonconstant homogeneous positive kernel behaves differently. For example, at `gamma=0` take

\[
\kappa(t)=e^{-a|t|},
\qquad a>0.
\]

Its Bochner measure has a positive Lorentzian density on the whole real line. Since `R_{pq}(1+i\xi)` is not identically zero, equation (10) gives

\[
Q_K(pq)>0
\]

for every fixed pair of distinct primes. Positive log-ratio nonlocality fills the selector nullspace just as the `min` kernel did in PC-182, but now for a much larger refinement-covariant class.

Conversely, one can place a spectral atom at an isolated zero of one finite Euler factor, such as a frequency with `2^{i\xi}=1`. That can annihilate selected shells divisible by `2`, but it also annihilates the corresponding `2`-power channel and fails a mixed control such as `15`. Requiring all `pq` controls is what forces the common point `s=1`.

There is also a useful RH warning. If one deliberately chooses a scaling degree whose Mellin line crosses nontrivial zeta zeros and places `mu` on those zeros, equation (9) makes those modes vanish for **every shell simultaneously**. They are null channels, not a Hilbert--Polya spectrum extracted from the prime-circle geometry. The common zeta factor identified in PC-179 cannot be turned into a positive selector merely by wrapping it in a scale-invariant two-depth kernel.

## 7. Scalar affine-refinement weights are monotone power laws

PC-182 also left open a sign-changing or nonmonotone scalar depth law if such a law were forced by refinement. The natural scalar covariance is slightly more general than pure homogeneity because adding a constant weight only changes the already-classical endpoint term. Suppose `w` is locally absolutely continuous on `[0,infinity)`, has finite `w(0)`, and for every integer `q>=2` there are constants `a_q,b_q` such that

\[
w(qx)=a_qw(x)+b_q.
\tag{19}
\]

Taking `x -> 0+` gives

\[
b_q=(1-a_q)w(0).
\]

Thus

\[
v(x):=w(x)-w(0)
\]

satisfies

\[
v(qx)=a_qv(x).
\tag{20}
\]

If `v` is nonzero, any zero at positive `x` propagates to its positive-rational orbit, which is dense; continuity would force `v` to vanish identically. Hence `v` has one sign, every `a_q` is positive, and the same dense-scale functional-equation argument as in Section 1 yields

\[
v(x)=Cx^\alpha.
\]

The finite anchor limit `v(0+)=0` excludes `alpha<=0`, so every nonconstant solution has

\[
\boxed{
w(x)=w(0)+Cx^\alpha,
\qquad
\alpha>0.
}
\tag{21}
\]

Therefore

\[
w'(x)=C\alpha x^{\alpha-1}
\]

has one fixed sign. Using the exact PC-182 symmetrization,

\[
(\operatorname{Sym}B^{(w)})_{nn}
=
\frac{w(0)}2\Lambda(n)^2
+
\frac12\int_0^\infty
w'(x)F_n(x)^2\,dx,
\]

every non-prime-power shell has

\[
\boxed{
(\operatorname{Sym}B^{(w)})_{nn}\ne0
}
\]

for nonconstant `w`. Thus no finite-anchor scalar law that is affinely covariant under the full refinement semigroup can realize the sign-changing derivative needed to repair PC-182. The only selector-preserving member is the constant weight, which returns to PC-180's boundary form.

This corollary is again classical functional-equation rigidity. It is included because it closes a specific live escape in the Prime-Circle program, not as a new theorem about scale invariance.

## 8. Prior-art and novelty audit

The analytic mechanisms are classical and were checked before interpretation.

The homogeneous-kernel factorization and Mellin diagonalization in Sections 1--3 are standard harmonic analysis on the multiplicative group; Jacobs--Frank (arXiv:2606.07644, 2026) is a direct recent formulation. Bochner representation of continuous positive-definite functions on the log group is classical. Dense scale covariance forcing real power laws is the same continuous functional-equation mechanism already audited in PC-167; J. Aczel's *A Short Course on Functional Equations* (1986) explicitly treats linear-affine equations, multiplicative/logarithmic functions, scale invariance and generalized homogeneous functions. The nonvanishing of zeta on `Re(s)=1` is the classical Hadamard--de la Vallee Poussin theorem, recorded for example in DLMF §25.10.

PC-179 already classified the one-shell Mellin factorization (9) as classical zeta/Ramanujan data. Therefore no historical novelty is claimed for any of those pieces, and the appearance of `zeta` in (10) is explicitly **not** counted as progress.

The durable Prime-Circle contribution is the conjunction: positivity plus exact full radial refinement turns every admissible two-depth kernel into a positive Mellin mixture, while the cyclotomic Euler factors make the common Mangoldt boundary point `s=1` the unique frequency capable of annihilating every mixed-prime control without annihilating the prime-power sector. That yields an exact no-go for an important surviving class rather than a new RH mechanism.

Directed searches for homogeneous Mellin kernels, positive-definite multiplicative kernels, scale-invariant operators, and von-Mangoldt/Mellin kernel constructions found the classical components above but no distinct prior result attaching this exact selector-uniqueness statement to the primitive cyclotomic radial flux. Absence of a wording match is not treated as novelty evidence.

## 9. Scope, falsifiers, and surviving frontier

The no-go requires a **fixed scalar kernel** on radial depth that is continuous, positive semidefinite and covariant by a scalar under simultaneous refinement of both depth variables. It also requires a finite quadratic form on the shell fluxes. It does not cover indefinite/sign-changing two-depth kernels, shell-dependent or matrix-valued kernels whose eigenspaces vary with depth, a second independent skew/ordered carrier coupled before self-adjointization, nonlinear or higher-order radial tensors, growing-level domains, or cross-level operators that break the single homogeneous Mellin decomposition.

The theorem is falsified by any nonconstant positive kernel satisfying (1) for all integer refinements and all `pq` null constraints while giving a positive prime-power value. Equations (10)--(18) show why such a kernel cannot exist. The scalar corollary is falsified by a nonconstant finite-anchor solution of (19) whose derivative changes sign; dense refinement forbids one.

For the accepted signed-radial-flux clue, the practical frontier therefore moves again. A successful continuation cannot obtain its extra coercivity from a positive fixed two-depth kernel compatible with all radial refinements, and it cannot obtain an oscillating scalar depth law from a finite-anchor affine refinement cocycle. It must use genuinely indefinite/noncommuting structure, a source-forced matrix-valued radial evolution, an additional independent ordered carrier, or a higher-order/cross-level construction before the positive Mellin quotient.
