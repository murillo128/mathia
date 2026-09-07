# PC-200 — power-map angular correlations collapse to one rational-ray Dirichlet packet

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for using the source-native circle power maps, before angular pairing, as a non-diagonal two-shell repair of the PC-199 Cauchy–Poisson construction.

PC-199 classified the canonical same-angle sesquilinear pairing of two source-native Cauchy–Poisson character fields. Angular orthogonality there forced the Fourier indices to agree, so the result collapsed to the product character at radial depth `x+y`. Its explicit boundary left genuinely non-diagonal angular operators outside the theorem.

The most intrinsic such operator is already present in Prime Circle: the power map `z -> z^a`. It fixes the common anchor `1`, is the exact map underlying polygon refinement, and on boundary Fourier modes sends `e_k(theta)=e^{ik theta}` to `e_{ak}`. Pulling the two fields back by *different* power maps therefore avoids the shared-index diagonal of PC-199 and imposes the genuinely off-diagonal relation `a k = b l`.

That repair is still exactly soluble. The relation `a k=b l` is a one-dimensional rational lattice ray, and complete multiplicativity of Dirichlet characters collapses the surviving two indices to one product-character sequence. After two radial Mellin transforms the entire family is again a scalar multiple of `Gamma(s)Gamma(t)L(s+t,eta)`. Thus the first source-native non-diagonal angular correspondence left by PC-199 does not produce a new two-variable zeta object or an independent critical-line mechanism.

## 1. Source-native power-map pullbacks

Use the angularized PC-197 field from PC-199. For a primitive nonprincipal character `chi` modulo `n`,

\[
\mathcal K_{n,\chi}(x,\theta)
=
2\tau(\overline\chi)
\sum_{k\ge1}\chi(k)e^{-kx}e^{ik\theta},
\qquad x>0.
\tag{1}
\]

For an integer `a>=1`, let

\[
(U_a f)(\theta):=f(a\theta).
\tag{2}
\]

This is the boundary pullback induced by the disk map `z -> z^a`. In particular it is not an arbitrary spectral wrapper: these are the same power maps that organize the roots-of-unity refinement tower, and they preserve the marked common point because `1^a=1`.

On Fourier modes,

\[
U_a e_k=e_{ak}.
\tag{3}
\]

Hence for two positive integers `a,b`,

\[
\langle U_a e_k,U_b e_l\rangle_{L^2(S^1)}
=\mathbf 1_{ak=bl}.
\tag{4}
\]

When `a != b`, the correspondence `U_a^*U_b` is genuinely non-diagonal in the ordinary Fourier basis. Thus the calculation below is not the same-index Parseval collapse already proved in PC-199.

Define the power-correlated two-shell field

\[
\mathcal P^{a,b}_{n,\chi;m,\psi}(x,y)
:=
\frac1{2\pi}
\int_0^{2\pi}
\mathcal K_{n,\chi}(x,a\theta)
\overline{\mathcal K_{m,\psi}(y,b\theta)}
\,d\theta,
\tag{5}
\]

where `psi` is primitive nonprincipal modulo `m` and `x,y>0`.

## 2. The off-diagonal Fourier constraint is only a rational ray

Substituting (1) into (5) and using absolute convergence at positive radial depth gives

\[
\mathcal P^{a,b}(x,y)
=
4\tau(\overline\chi)
\overline{\tau(\overline\psi)}
\sum_{k,l\ge1}
\chi(k)\overline{\psi(l)}
 e^{-kx-ly}\,\mathbf 1_{ak=bl}.
\tag{6}
\]

Write

\[
g=\gcd(a,b),\qquad a=g a_0,\qquad b=g b_0,
\qquad \gcd(a_0,b_0)=1.
\tag{7}
\]

The Diophantine constraint in (6) is then equivalent to

\[
k=b_0r,\qquad l=a_0r,
\qquad r\ge1.
\tag{8}
\]

So the apparently two-index coupling retains only one primitive lattice direction. Because Dirichlet characters are completely multiplicative after extension by zero to non-units,

\[
\chi(b_0r)\overline{\psi(a_0r)}
=
\chi(b_0)\overline{\psi(a_0)}
\bigl(\chi\overline\psi\bigr)(r).
\tag{9}
\]

Put

\[
\eta:=\chi\overline\psi,
\qquad
T:=b_0x+a_0y.
\tag{10}
\]

Equations (6)--(9) give the exact collapse

\[
\boxed{
\mathcal P^{a,b}_{n,\chi;m,\psi}(x,y)
=
4\tau(\overline\chi)
\overline{\tau(\overline\psi)}
\chi(b_0)\overline{\psi(a_0)}
\sum_{r\ge1}\eta(r)e^{-rT}.
}
\tag{11}
\]

There are only two cases.

If `chi(b_0)=0` or `psi(a_0)=0`, the entire correlation vanishes identically. The power-map degree has hit a conductor prime and kills the channel rather than creating a new one.

Otherwise (11) is exactly the ordinary PC-197 radial packet for the single product character `eta`, evaluated at the single weighted depth `T=b_0x+a_0y`, up to its finite Gauss/character scalar. If `n,m` are coprime and `chi,psi` are primitive, then `eta` is the usual primitive product character of conductor `nm`. If `eta` is imprimitive, nothing structurally changes: its `L`-series is the classical primitive `L`-function multiplied by the standard finite Euler factors.

Thus replacing the diagonal `k=l` of PC-199 by the non-diagonal relation `ak=bl` does not create a two-dimensional Fourier carrier. It merely rotates the diagonal to a rational ray and then character multiplicativity identifies that ray with the same one-index packet.

## 3. Exact recovery of PC-199 and conductor-collision controls

The formula contains useful internal controls.

For `a=b`, one has `a_0=b_0=1`, so (11) reduces exactly to the PC-199 pairing at depth `x+y`. Hence PC-199 is the diagonal member of the present family.

For a genuinely non-diagonal example, take the quadratic characters `chi_3` modulo `3` and `psi_5` modulo `5`, and choose `(a,b)=(2,7)`. Then `a_0=2`, `b_0=7`, both character prefactors are nonzero, and the whole correlation is the conductor-`15` product-character packet at depth

\[
T=7x+2y.
\tag{12}
\]

By contrast, for `(a,b)=(2,3)`, `b_0=3` and therefore `chi_3(b_0)=0`; the correlation is identically zero. This is not a new prime selector. It is exactly the ordinary support rule of a Dirichlet character at integers sharing a factor with its conductor.

These controls are decisive because they separate two effects that could otherwise be confused: the angular power maps genuinely change the Fourier matching relation, but all arithmetic produced by that change is exhausted by the gcd reduction (7)--(8) and ordinary character multiplicativity (9).

## 4. Two Mellin variables still see only `s+t`

The most favorable interpretation for a new spectral mechanism would keep the two independent radial depths and Mellin-transform both. In the half-plane

\[
\Re s>0,\qquad \Re t>0,\qquad \Re(s+t)>1,
\tag{13}
\]

termwise integration of (11) is absolutely convergent and gives

\[
\begin{aligned}
\mathcal M_2\mathcal P^{a,b}(s,t)
&:=
\int_0^\infty\int_0^\infty
x^{s-1}y^{t-1}
\mathcal P^{a,b}(x,y)\,dx\,dy\\
&=
4\tau(\overline\chi)
\overline{\tau(\overline\psi)}
\chi(b_0)\overline{\psi(a_0)}
\Gamma(s)\Gamma(t)
 b_0^{-s}a_0^{-t}
 L(s+t,\eta).
\end{aligned}
\tag{14}
\]

Therefore

\[
\boxed{
\mathcal M_2\mathcal P^{a,b}(s,t)
=
C_{a,b;\chi,\psi}\,
\Gamma(s)\Gamma(t)b_0^{-s}a_0^{-t}
L(s+t,\eta),
}
\tag{15}
\]

with a finite scalar `C_{a,b;chi,psi}` independent of `s,t`.

The power-map slopes contribute only the elementary nonvanishing factors `b_0^{-s}a_0^{-t}`. All nontrivial zeros remain those of the one-variable Dirichlet function in

\[
u=s+t.
\tag{16}
\]

Consequently a hypersurface `Re(s+t)=1/2` is only the pullback of the classical GRH line for `L(u,eta)`. No second functional equation, independent spectral parameter, or geometric zero-confining mechanism appears.

If `eta` is principal, the same statement reduces to the Riemann zeta function with its standard finite conductor factors. Hence the Riemann case is no better: the construction can recover a zeta divisor, but only by the already-classical one-variable Dirichlet packet.

## 5. Finite covering-correspondence combinations do not help

The collapse is stable under the finite linear repair naturally suggested by operator language. Consider a shell-independent finite combination of power correspondences

\[
T=\sum_{j=1}^J c_j U_{a_j}^*U_{b_j}.
\tag{17}
\]

Its matrix element between two character fields is the corresponding finite sum of (11). After double Mellinization every term contains the **same** `L(s+t,eta)`; only the elementary prefactor changes. Thus

\[
\boxed{
\mathcal M_2\langle \mathcal K_{n,\chi}(x),
T\mathcal K_{m,\psi}(y)\rangle
=
\Gamma(s)\Gamma(t)L(s+t,\eta)\,E_T(s,t),
}
\tag{18}
\]

where `E_T` is a finite sum of terms of the form

\[
c_j\chi(b_{0,j})\overline{\psi(a_{0,j})}
 b_{0,j}^{-s}a_{0,j}^{-t}
\tag{19}
\]

up to the common Gauss normalization.

An arbitrary choice of coefficients in `T` can of course manufacture zeros in `E_T`; those zeros belong to the chosen finite operator, not to a source-forced Prime-Circle spectral law. Under the research mandate such engineered finite spectral wrappers are not progress toward RH.

This theorem does not claim to classify the full noncommutative algebra generated by arbitrary shell-dependent operators, projections, limits, and nonlinear functions of the `U_a`. It closes the canonical finite linear correspondence class obtained directly by inserting the intrinsic power maps into the PC-199 pairing.

## 6. Prior-art and novelty audit

The ingredients of the collapse are classical, and no theorem-level historical novelty is claimed for them separately.

The operator `U_a:f(theta)->f(a theta)` is the standard dilation/composition action of the inner disk map `z^a` on circle/Hardy Fourier modes. More broadly, arithmetic correlations of systems of dilated periodic functions are established harmonic-analysis territory; the Aistleitner--Berkes--Seip source already recorded in `SOURCES.md` treats such dilated systems and their Poisson/GCD structure. The multiplicative-character and Gauss-sum package is likewise classical and already anchored in `SOURCES.md` for PC-025/PC-197. The final Dirichlet `L`-series and its functional equation are the same standard objects audited in PC-197 and PC-199.

A directed check of composition-operator, dilated-function, periodic-Dirichlet-series, and character literature found no distinct Prime-Circle theorem in exactly the form (11)--(18). That absence is not a novelty claim: once the PC-197 field is written in Fourier coordinates, the proof is elementary. The durable Mathia-specific content is the **boundary classification**: the first source-native non-diagonal angular operator explicitly left open by PC-199 still collapses to one classical character packet.

This also distinguishes the present result from the GCD-kernel branch. Generic dilated functions can produce gcd-dependent correlations because arbitrary Fourier coefficients do not factor along the ray `k=b_0r`, `l=a_0r`. Here the Cauchy–Poisson character coefficients are multiplicative, and equation (9) is precisely what removes that extra gcd-kernel complexity.

## 7. What this rules out and what remains open

The finding rules out the route

\[
\text{Cauchy--Poisson character fields}
\xrightarrow{\text{different anchor-fixing power maps}}
\text{non-diagonal angular pairing}
\xrightarrow{\text{one/two radial Mellin}}
\text{new RH/GRH mechanism}.
\tag{20}
\]

It also rules out any fixed finite shell-independent linear combination of those power correspondences as a new zero source: equation (18) factors out the same classical `L(s+t,eta)`.

The remaining frontier after PC-199 is therefore narrower. A viable angular cross-shell mechanism must avoid reduction to a **single rational Fourier ray**. Examples still outside this theorem are a kernel with genuinely two-dimensional Fourier support rather than one linear Diophantine constraint; shell-dependent non-diagonal operators whose coefficients are forced by old/new geometry rather than selected externally; nonlinear or matrix-valued correspondences that keep more than one ray coupled simultaneously; infinite refinement/solenoidal limits where no fixed finite correspondence reduction exists; and the global uniformization/monodromy branch.

The result is a negative boundary, not evidence that those remaining classes work. In particular, merely choosing a more complicated finite combination of power maps and interpreting zeros of its elementary prefactor as spectral data would fail the source-forcing and arbitrary-wrapper controls in the canonical README.

## 8. Falsification checks

The exact claim has several direct checks.

For any positive integers `a,b`, solving `ak=bl` must give precisely `k=b_0r`, `l=a_0r` with `(a_0,b_0)=1`. Substitution into the absolutely convergent Fourier expansion must reproduce (11) coefficient by coefficient.

Setting `a=b` must reproduce PC-199 exactly. Choosing a reduced slope for which `b_0` is not coprime to the conductor of `chi`, or `a_0` is not coprime to the conductor of `psi`, must make the full pairing vanish because the corresponding Dirichlet-character factor is zero.

Finally, independent numerical quadrature at positive depths agrees with (11): for the quadratic characters modulo `3` and `5` and the non-diagonal slope `(a,b)=(2,7)`, direct angular integration matches the single `eta=chi_3 psi_5` series at depth `7x+2y`; for `(2,3)` it vanishes to numerical precision. These checks use no RH assumption.

## Research consequence

PC-199's phrase "non-diagonal angular operator" was too broad a surviving category. The canonical non-diagonal operators supplied by the circle's own refinement semigroup are now classified: **finite power-map correspondences rotate the Fourier diagonal into rational rays, but multiplicative character packets turn every such ray back into one ordinary Dirichlet `L`-carrier.** A future cross-shell attempt should therefore spend its complexity only on interactions that preserve at least two independent Fourier directions after all source-forced symmetries and multiplicative reductions are applied.