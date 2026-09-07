# PC-201 — finite Haar Cauchy–Poisson fusion is exactly Mordell–Tornheim L-data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for using any fixed finite one-output Haar fusion of the source-native Prime-Circle Cauchy–Poisson character fields as a new multivariable RH/GRH carrier.

PC-197 identifies one primitive-shell Cauchy–Poisson character field with the ordinary Dirichlet Laplace packet. PC-199 shows that the canonical sesquilinear two-shell pairing collapses to one product character because angular orthogonality forces the same Fourier index on both legs. PC-200 then inserts the intrinsic power maps `z -> z^a`; the resulting off-diagonal relation is still only one rational ray and again collapses to a single Dirichlet packet. The live boundary after PC-200 therefore requires at least two independent Fourier directions.

The lowest-order scalar Haar invariant that actually crosses that boundary is trilinear: multiply two holomorphic character fields and one antiholomorphic field before integrating around the common circle. More generally, fuse any fixed finite number `r` of holomorphic input packets against one conjugate output packet. Angular invariance now imposes only

\[
k_1+\cdots+k_r=\ell,
\]

so `r` genuinely independent positive Fourier indices survive. This is not another rational-ray collapse.

Nevertheless the resulting multivariable Mellin transform is **exactly the classical Mordell–Tornheim multiple `L`-function** with Dirichlet characters on the independent indices and on their sum. Thus finite scalar Haar fusion really does preserve higher-dimensional Fourier information, but the entire hierarchy lands in an established multiple-Dirichlet-series class. Increasing finite valence raises Mordell–Tornheim depth; it does not by itself supply a new Prime-Circle spectral object, a new functional equation, or a critical-line mechanism.

## 1. Source-native angular packets

Let `chi` be a primitive nonprincipal Dirichlet character modulo `n`. The angularized PC-197 field is

\[
\mathcal K_{n,\chi}(x,\theta)
=
2\tau(\overline\chi)
\sum_{k\ge1}\chi(k)e^{-kx}e^{ik\theta},
\qquad x>0.
\tag{1}
\]

At prime level every nonprincipal multiplicative character is primitive, so (1) gives every nonprincipal mode of the full primitive shell. The radial depth `x` and the angular variable `theta` are the actual disk variables; no spectral order has been inserted by hand.

Choose primitive nonprincipal characters

\[
\chi_j\pmod{n_j},\qquad j=1,\ldots,r,
\]

and a primitive nonprincipal output character

\[
\psi\pmod m.
\]

For positive radial depths `x_1,...,x_r,y`, define the fixed-valence Haar fusion

\[
\boxed{
\mathcal T_r(\mathbf x;y)
:=
\frac1{2\pi}
\int_0^{2\pi}
\left(\prod_{j=1}^r
\mathcal K_{n_j,\chi_j}(x_j,\theta)\right)
\overline{\mathcal K_{m,\psi}(y,\theta)}
\,d\theta.
}
\tag{2}
\]

For `r=1`, this is exactly the PC-199 same-angle pairing. The first new case is `r=2`, where the scalar invariant is trilinear and can retain two independent Fourier indices.

The operation in (2) is the canonical scalar Haar contraction of a product of source-native circle fields. It is not asserted to be the unique possible nonlinear interaction, but it is the lowest-degree invariant in the PC-197 packet algebra that can meet PC-200's requirement of more than one surviving Fourier direction.

## 2. Haar selection leaves an `r`-dimensional additive cone

Substitute (1) into (2). Absolute convergence at positive depths allows termwise integration. If the antiholomorphic output has Fourier index `ell`, angular integration gives

\[
\frac1{2\pi}
\int_0^{2\pi}
 e^{i(k_1+\cdots+k_r-\ell)\theta}
\,d\theta
=
\mathbf 1_{\ell=k_1+\cdots+k_r}.
\tag{3}
\]

Hence

\[
\boxed{
\begin{aligned}
\mathcal T_r(\mathbf x;y)
&=
C_{\boldsymbol\chi,\psi}
\sum_{k_1,\ldots,k_r\ge1}
\left(\prod_{j=1}^r\chi_j(k_j)ight)
\overline{\psi(k_1+\cdots+k_r)}\\
&\qquad\qquad\times
\exp\!\left(
-\sum_{j=1}^r k_jx_j
-(k_1+\cdots+k_r)y
\right),
\end{aligned}}
\tag{4}
\]

with the nonzero Gauss factor

\[
\boxed{
C_{\boldsymbol\chi,\psi}
=
2^{r+1}
\left(\prod_{j=1}^r\tau(\overline\chi_j)\right)
\overline{\tau(\overline\psi)}.
}
\tag{5}
\]

This is the structural point not present in PC-199 or PC-200. For `r>=2`, the variables `k_1,...,k_r` remain independent. The only relation is that the output frequency is their sum. There is no parametrization by one rational ray and no multiplicativity identity that can replace all `k_j` by one common integer.

For `r=2`, explicitly,

\[
\boxed{
\mathcal T_2(x_1,x_2;y)
=C
\sum_{k,l\ge1}
\chi_1(k)\chi_2(l)\overline{\psi(k+l)}
 e^{-k x_1-l x_2-(k+l)y}.
}
\tag{6}
\]

Thus the first finite scalar repair of the rational-ray obstruction genuinely reaches a two-dimensional additive Fourier cone.

## 3. Independent radial Mellin variables give the classical Mordell–Tornheim multiple `L`-function

Keep every source-native radial depth independent and Mellin-transform all `r+1` variables. In the safe absolute-convergence region `Re(s_j)>1` and `Re(u)>1`, termwise integration in (4) gives

\[
\int_0^\infty x_j^{s_j-1}e^{-k_jx_j}\,dx_j
=
\Gamma(s_j)k_j^{-s_j}
\tag{7}
\]

and

\[
\int_0^\infty y^{u-1}
 e^{-(k_1+\cdots+k_r)y}\,dy
=
\Gamma(u)(k_1+\cdots+k_r)^{-u}.
\tag{8}
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal M_{r+1}\mathcal T_r
(\mathbf s;u)
&=
C_{\boldsymbol\chi,\psi}
\left(\prod_{j=1}^r\Gamma(s_j)\right)
\Gamma(u)\\
&\quad\times
L_{\mathrm{MT}}
(s_1,\ldots,s_r,u;
\chi_1,\ldots,\chi_r,\overline\psi),
\end{aligned}}
\tag{9}
\]

where

\[
\boxed{
L_{\mathrm{MT}}
(s_1,\ldots,s_r,u;
\chi_1,\ldots,\chi_r,\chi_{r+1})
:=
\sum_{k_1,\ldots,k_r\ge1}
\frac{
\chi_1(k_1)\cdots\chi_r(k_r)
\chi_{r+1}(k_1+\cdots+k_r)
}
{k_1^{s_1}\cdots k_r^{s_r}
 (k_1+\cdots+k_r)^u}.
}
\tag{10}
\]

Equation (10) is precisely the standard Mordell–Tornheim multiple `L`-function. The Prime-Circle derivation has not merely produced something analogous to that family: after the explicit nonzero Gauss normalization in (5) and the elementary gamma factors in (9), it is the same function coefficient by coefficient.

The trilinear case `r=2` gives the classical Mordell–Tornheim double `L`-function

\[
\sum_{k,l\ge1}
\frac{\chi_1(k)\chi_2(l)\overline\psi(k+l)}
{k^{s_1}l^{s_2}(k+l)^u}.
\tag{11}
\]

This is important for the research boundary: **the first source-native scalar operation that genuinely preserves two Fourier directions does not collapse back to one Dirichlet `L`, but it also does not leave established multiple-`L` theory.**

## 4. Principal modes stay inside the colored Mordell–Tornheim cone class

The restriction to nonprincipal primitive characters makes (9) especially clean because the constant Fourier term vanishes. It is not an escape to reinsert the principal shell mode.

PC-197 gives the centered principal packet as

\[
\mathcal K_{n,1}(x,\theta)-\varphi(n)
=
2\sum_{k\ge1}c_n(k)e^{-kx}e^{ik\theta},
\tag{12}
\]

where

\[
c_n(k)=\sum_{a\in U(n)}\zeta_n^{ak}
\tag{13}
\]

is the Ramanujan sum. Thus every principal coefficient is already a finite sum of root-of-unity colors. Inserting one or more centered principal legs into (2), expanding (13), and repeating (3)--(9) yields a finite linear combination of colored/Lerch-type Mordell–Tornheim functions

\[
\sum_{k_1,\ldots,k_r\ge1}
\frac{
\alpha_1^{k_1}\cdots\alpha_r^{k_r}
\delta^{k_1+\cdots+k_r}
}
{k_1^{s_1}\cdots k_r^{s_r}
(k_1+\cdots+k_r)^u},
\tag{14}
\]

with all colors roots of unity forced by the shell orders.

Therefore the clean character theorem (9) and the principal extension (14) together classify the full prime-level multiplicative packet under this fixed finite one-output Haar-fusion hierarchy: nonprincipal legs give Mordell–Tornheim `L`-functions and principal legs give finite cyclotomic colored variants.

This is the angular/multivariable counterpart of PC-189. PC-189 showed that finite **same-depth local polynomial jets**, followed by one Mellin transform, land in colored Tornheim/conical functions with fixed side exponents determined by derivative order. Here the radial depths remain independent, every Mellin exponent is free, and the additive cone comes from exact angular momentum conservation. The two results meet in the same classical Mordell–Tornheim/conical architecture from different source-native constructions.

## 5. Composite-conductor and source-specificity controls

No step in (2)--(10) uses primality of the shell orders. It uses only the PC-197 character field and primitive-character Gauss expansion. Primitive characters of composite conductor therefore obey exactly the same fusion law. Prime levels are convenient only because every nonprincipal character modulo a prime is primitive.

This is a decisive matched control against interpreting the higher-dimensional additive cone as a rational-prime birth effect. Replacing one prime conductor by any composite conductor carrying a primitive character changes the finite character data but not the analytic species, Fourier-selection law, or Mellin architecture.

There is also a direct finite numerical audit of the first genuinely two-dimensional case. For the quadratic primitive characters modulo `3`, `5`, and `7`, at depths

\[
(x_1,x_2,y)=(0.41,0.53,0.37),
\]

numerical angular quadrature of the trilinear left side of (2) agrees with the two-index series (6) to about `4e-15`. This is only a sign/conjugation check; the proof is the exact Fourier calculation above.

## 6. Prior-art and novelty audit

The resulting analytic family is classical.

Hirofumi Tsumura, **On some functional relations between Mordell–Tornheim double L-functions and Dirichlet L-functions**, *Journal of Number Theory* 120:1 (2006), 161–178, DOI `10.1016/j.jnt.2005.11.006`, studies analytic functional relations between the depth-two Mordell–Tornheim `L`-functions and ordinary Dirichlet `L`-functions. This directly covers the analytic species reached by the trilinear case (11).

Kohji Matsumoto, Takashi Nakamura and Hirofumi Tsumura, **Functional relations and special values of Mordell–Tornheim triple zeta and L-functions**, *Proceedings of the American Mathematical Society* 136:6 (2008), 2135–2145, DOI `10.1090/S0002-9939-08-09192-2`, define the character-decorated Mordell–Tornheim hierarchy in exactly the form with characters on the independent summation variables and on their sum, and prove meromorphic continuation/functional relations in the triple-depth case.

Jianqiang Zhao and Xia Zhou, **Reducibility of signed cyclic sums of Mordell–Tornheim zeta and L-values**, *Journal of the Ramanujan Mathematical Society* 26:4 (2011), 383–414; arXiv `0902.1262`, explicitly records the arbitrary-depth definition (10) and studies reductions of signed cyclic combinations to lower-depth multiple `L`-values.

The root-of-unity-colored form (14) is also adjacent to the cyclotomic conical/Tornheim literature already anchored in `SOURCES.md` for PC-082/PC-102/PC-189, notably Terasoma's rational-cone cyclotomic zeta framework and Zhao's colored Tornheim double series.

A directed prior-art search across Mordell–Tornheim double/multiple `L`-functions, Dirichlet-character Tornheim series, colored cone zeta functions, and functional-relation literature found the exact established family (10), not a distinct Prime-Circle multivariable `L`-object. **No theorem-level novelty is claimed for the multiple `L`-function or its analytic continuation.**

The durable Mathia-specific content is the exact source-to-target identification: the finite scalar Haar invariant that first escapes PC-200's one-ray obstruction lands coefficient-for-coefficient in this classical hierarchy.

## 7. RH/critical-line audit

Equation (9) is a genuine geometric-to-analytic bridge: unlike PC-199/PC-200, it preserves several independent Fourier and Mellin directions. That fact alone is not an RH mechanism.

The additive denominator `(k_1+...+k_r)^u` is exactly the classical Mordell–Tornheim coupling. The construction supplies no Euler product over rational primes, no source-derived self-adjoint operator whose spectrum is the zero set, no Weil/de Branges positivity statement, and no involution selecting `Re(s)=1/2` in any one Mellin variable. Known functional relations of Mordell–Tornheim `L`-functions are already part of the classical multiple-Dirichlet-series theory and cannot be counted as a new Prime-Circle functional equation merely because (2) realizes the same functions geometrically.

Nor does increasing `r` help by itself. Equation (9) shows that every fixed finite valence with one conjugate output simply raises the depth of the same Mordell–Tornheim hierarchy. Any zeros or singular hyperplanes of that known multivariable family belong to the classical analytic object reached after scalar Haar contraction, not to an independently derived Prime-Circle zero-confinement principle.

## 8. Boundary of the result

The exact closed route is

\[
\boxed{
\text{finite PC-197 character packets}
\xrightarrow{\text{one-output Haar fusion}}
\text{additive Fourier cone}
\xrightarrow{\text{independent radial Mellin}}
\text{Mordell--Tornheim multiple }L\text{-data}.
}
\tag{15}
\]

This is stronger than the PC-200 rational-ray negative because the intermediate object really has higher-dimensional Fourier support. The lesson is correspondingly sharper: **preserving two or more independent Fourier directions is necessary to leave the one-Dirichlet-packet closure, but it is not sufficient to leave classical analytic-number-theory packet algebra.**

The theorem does not classify scalar contractions with several holomorphic and several antiholomorphic output legs, shell-dependent non-Haar kernels forced by old/new chord geometry, matrix-valued couplings that retain the independent cone indices as operator degrees of freedom instead of summing them, infinite-valence/refinement limits, non-scalar positivity constructions, or the global uniformization/monodromy branch. Those remain structurally distinct.

A useful next candidate must therefore obtain something from the surviving multi-index data **before** the scalar Haar/Mellin contraction identifies it with a standard Mordell–Tornheim function, or add another source-forced structure whose algebra is not already the classical finite colored cone hierarchy.

## Audit / falsification tests

The finding can be falsified directly at four points.

1. Expanding (2) at positive depths must give the angular selection rule (3). Any surviving Fourier tuple not satisfying `ell=sum k_j`, or any additional relation among the independent `k_j`, would change the claimed cone.
2. Termwise Mellin transformation in an absolute-convergence region must produce exactly the factors `k_j^{-s_j}` and `(sum k_j)^{-u}` in (9). A residual radial coupling not expressible by those factors would escape the identification.
3. The coefficient series remaining after removing the Gauss and gamma factors must agree term by term with the standard definition (10) of `L_MT`.
4. Replacing a prime conductor by a composite conductor supporting a primitive character must leave the same formula intact. Failure of this matched control would indicate a prime-specific ingredient omitted above.

All four checks are independent of RH or GRH.