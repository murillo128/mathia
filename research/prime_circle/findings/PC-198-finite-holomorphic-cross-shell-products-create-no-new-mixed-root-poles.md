# PC-198 — finite holomorphic cross-shell products create no new mixed root-of-unity poles

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for using finite same-variable holomorphic products/differential polynomials of the intrinsic Prime-Circle Cauchy–Poisson fields to manufacture a new mixed-shell root-of-unity frequency or conductor carrier.

PC-197 kept the full vertexwise Cauchy–Poisson field instead of scalarizing the shell immediately. Its multiplicative-character modes are source-native in the radial depth, but their Mellin transforms are exactly the classical `Gamma(s)L(s,chi)` packet. The natural next question is whether two shells can be coupled *before the radial Mellin transform* by the most immediate nonlinear operation available on the common disk: pointwise multiplication, or more generally a finite holomorphic differential polynomial in their Cauchy fields.

That route has an exact obstruction. A finite holomorphic product can change residues and pole multiplicities, but it cannot create a new pole location. For coprime shell orders `n,m`, the nonprincipal character modes sharpen this to a partial-fraction statement: their product splits into an `n`-periodic sector plus an `m`-periodic sector. In particular there is no Fourier mode of exact order `nm`. Thus same-depth holomorphic multiplication does not synthesize a genuinely mixed root-of-unity carrier from two coprime shells.

This does **not** say that all cross-shell interactions separate. Mixed arithmetic can survive in the residues/amplitudes, and genuinely two-variable, sesquilinear, nonlocal, matrix/cocycle, inverse-limit, or uniformization interactions are outside the result.

## 1. Rational form of the PC-197 character mode

Let `chi` be a nonprincipal Dirichlet character modulo `n>1` and put

\[
F_{n,\chi}(z):=\sum_{k\ge 1}\chi(k)z^k,
\qquad |z|<1.
\]

Periodicity gives

\[
F_{n,\chi}(z)
=\frac{P_{n,\chi}(z)}{1-z^n},
\qquad
P_{n,\chi}(z):=\sum_{a=1}^{n-1}\chi(a)z^a.
\tag{1}
\]

Because `chi` is nonprincipal,

\[
P_{n,\chi}(1)=\sum_{a\bmod n}\chi(a)=0.
\]

Hence `1-z` divides `P_{n,chi}`. Writing

\[
S_n(z):=1+z+\cdots+z^{n-1}
=\frac{1-z^n}{1-z},
\]

there is a polynomial `Q_{n,chi}` with `deg Q_{n,chi}<=n-2` such that

\[
\boxed{
F_{n,\chi}(z)=\frac{Q_{n,\chi}(z)}{S_n(z)}.
}
\tag{2}
\]

Thus every pole of the nonprincipal character mode lies at a nontrivial `n`-th root of unity. Some poles may cancel for a particular character, but no other pole location can occur.

For a primitive character, PC-197 gives the intrinsic Cauchy–Poisson mode at radial depth `x>0` as

\[
\boxed{
\mathcal K_{n,\chi}(x)
=2\tau(\overline\chi)F_{n,\chi}(e^{-x}).
}
\tag{3}
\]

So the pole set of (2) is exactly the complexified radial singularity set behind the PC-197 packet.

## 2. Coprime shell products split by partial fractions

Let `chi` and `psi` be nonprincipal characters modulo coprime integers `n,m>1`. Since `gcd(n,m)=1`, the polynomials `S_n` and `S_m` are coprime: a common zero would be a nontrivial root of unity whose order divides both `n` and `m`.

Therefore

\[
F_{n,\chi}(z)F_{m,\psi}(z)
=
\frac{Q_{n,\chi}(z)Q_{m,\psi}(z)}{S_n(z)S_m(z)}
\]

has the unique proper partial-fraction form

\[
\boxed{
F_{n,\chi}(z)F_{m,\psi}(z)
=
\frac{R_n(z)}{S_n(z)}
+
\frac{R_m(z)}{S_m(z)},
}
\tag{4}
\]

with

\[
\deg R_n<n-1,
\qquad
\deg R_m<m-1.
\]

Equation (4) is the decisive structural statement. The product contains poles only on the union of the original nontrivial `n`-th and `m`-th roots. In particular it contains **no primitive `nm`-th root pole**.

The same fact can be read directly in coefficient space. Write

\[
F_{n,\chi}(z)F_{m,\psi}(z)
=\sum_{k\ge 0}c_k z^k,
\qquad
c_k=\sum_{r=1}^{k-1}\chi(r)\psi(k-r).
\tag{5}
\]

For the first term of (4),

\[
\frac{R_n(z)}{S_n(z)}
=\frac{(1-z)R_n(z)}{1-z^n}.
\]

Its coefficients form an exactly `n`-periodic sequence `u_k`; because the numerator vanishes at `z=1`, one period has zero mean. Likewise the second term gives an exactly `m`-periodic zero-mean sequence `v_k`. Hence

\[
\boxed{
c_k=u_k+v_k,
\qquad
u_{k+n}=u_k,
\qquad
v_{k+m}=v_k.
}
\tag{6}
\]

When (6) is viewed on one period of length `nm`, the discrete Fourier support of `u` lies only at indices divisible by `m`, while that of `v` lies only at indices divisible by `n`. Therefore

\[
\boxed{
\widehat c(j)=0
\quad\text{for every frequency of exact order }nm.
}
\tag{7}
\]

The two shells can alter one another's amplitudes through `R_n,R_m`, but the pointwise product does not create a new mixed additive root-of-unity frequency.

## 3. Direct control at conductors 3 and 5

Take the real nonprincipal characters

\[
\chi_3=(1,-1,0)\pmod 3,
\]

and the quadratic character modulo `5`, with values `+1` on residues `1,4`, `-1` on `2,3`, and `0` on `0`.

The Cauchy-product coefficients (5) over one period of length `15` are

\[
(c_1,\ldots,c_{15})
=
(0,1,-2,0,3,-3,1,1,-3,3,0,-2,1,0,0).
\tag{8}
\]

They decompose exactly as `c_k=u_k+v_k`, where by residue class

\[
(u_0,u_1,u_2)=(-2,1,1)
\quad (\bmod\ 3),
\]

and

\[
(v_0,v_1,v_2,v_3,v_4)=(2,-1,0,0,-1)
\quad (\bmod\ 5).
\]

The length-15 Fourier support is consequently

\[
\boxed{
\{3,5,6,9,10,12\},
}
\tag{9}
\]

namely the lifted order-5 and order-3 sectors. No index coprime to `15` occurs, so there is no primitive 15th-root mode. This is a finite exact check of (7), not evidence on which the proof depends.

## 4. The obstruction holds before character projection

The character calculation is useful because it gives the exact periodic decomposition, but the pole obstruction is more general and already exists at the vertexwise level.

For one primitive vertex `zeta_n^a`, PC-197 uses

\[
K_{n,a}(z)=\frac{1+z\zeta_n^a}{1-z\zeta_n^a},
\qquad z=e^{-x}.
\tag{10}
\]

Its only finite pole is at `z=zeta_n^{-a}`. Therefore any finite pointwise polynomial in vertexwise fields from shells `n_1,...,n_r` has pole set contained in

\[
\boxed{
\bigcup_{j=1}^r\{\zeta_{n_j}^{-a}:a\in U(n_j)\}.
}
\tag{11}
\]

No multiplication can add a pole at a root of unity that was absent from every input shell. Thus the failure to generate a new mixed root is not caused by taking multiplicative characters too early; character projection merely makes the same obstruction algebraically explicit.

## 5. Finite radial differentiation changes multiplicity, not support

Let

\[
D:=z\frac{d}{dz},
\]

which corresponds to `-d/dx` after `z=e^{-x}`. If a rational function has poles in a finite set `Omega`, then applying `D`, adding such functions, or multiplying them finitely many times cannot introduce a pole outside `Omega`. Differentiation can only increase existing pole orders.

Consequently every finite differential polynomial built from the same-variable PC-197 fields has poles only at the original shell roots. Its Taylor coefficients are finite sums of terms of the form

\[
P(k)\omega^k,
\qquad \omega\in\Omega,
\tag{12}
\]

with `P` a polynomial whose degree records pole multiplicity. After returning to `z=e^{-x}`, Mellin transforms of these pieces reduce to shifted polylogarithmic/root-of-unity packets such as

\[
\Gamma(s)\operatorname{Li}_{s-j}(\omega),
\]

and, after finite Fourier decomposition of periodic coefficients, to the standard finite Hurwitz/Dirichlet family. No new mixed-shell pole divisor is created by this finite holomorphic differential algebra.

## 6. Prior-art and novelty audit

The mathematical ingredients of the obstruction are classical. Periodic arithmetic functions admit finite Fourier expansions; Dirichlet characters and Gauss sums are the standard examples. Rational generating functions for periodic sequences and partial fractions over cyclotomic root sets are elementary classical algebra. Periodic Dirichlet series likewise reduce to finite Hurwitz-zeta packets. The neighboring same-index product/correlation theory for Ramanujan sums is already represented in `SOURCES.md` by Tóth, *Sums of products of Ramanujan sums* (2012).

A targeted literature check against standard finite-Fourier treatments of periodic number-theoretic functions and the periodic-Dirichlet-series literature did not reveal a distinct theorem that should be claimed as new here. The specialization (4)–(7) is best classified as an exact program-specific consequence of classical rational/periodic-function algebra. **No mathematical novelty is claimed.**

The useful Mathia-specific content is the obstruction it places immediately after PC-197: even retaining the intrinsic radial variable and coupling two already source-native shell fields nonlinearly at the same complex/radial point does not synthesize a new mixed root-of-unity frequency.

## 7. Boundary of the negative result

This finding rules out the route

\[
\boxed{
\text{finite shell Cauchy fields}
\;\xrightarrow{\text{same-variable holomorphic products/derivatives}}\;
\text{new mixed root-of-unity pole/frequency}
\;\longrightarrow\;
\text{new RH carrier}.
}
\]

It does **not** imply that the full cross-shell problem is separable. In particular, it does not cover:

- sesquilinear or genuinely two-variable angular couplings such as kernels depending simultaneously on `z` and `\overline w` before restricting to a radial ray;
- nonlocal couplings between different radial depths;
- matrices/operators whose shell labels remain active degrees of freedom rather than scalar factors of one rational function;
- transverse cocycles or inverse-limit/solenoidal constructions of the type left open by the accepted local clue on preimage-tube fiber sectors;
- nonlinear operations involving limits, inverses, spectral projections, or other constructions not contained in a finite holomorphic differential algebra;
- the global uniformization/monodromy branch.

The main consequence is therefore a sharper frontier rather than an RH mechanism: **cross-shell interaction must preserve more than a finite same-point holomorphic product of the Cauchy–Poisson carriers if it is to create genuinely new spectral support.**