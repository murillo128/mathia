# PC-199 — sesquilinear Cauchy–Poisson fusion collapses to the composite-character packet

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for using the canonical angular sesquilinear pairing of two source-native Prime-Circle Cauchy–Poisson character fields — including different radial depths — as a new mixed-conductor RH/GRH mechanism.

PC-197 showed that one primitive shell, kept as a full vertexwise Cauchy–Poisson field and then decomposed by multiplicative characters, gives exactly the classical `Gamma(s)L(s,chi)` packet. PC-198 then ruled out finite same-variable holomorphic products as a way to create a new mixed root-of-unity pole, but explicitly left sesquilinear/two-variable and different-depth interactions open.

The most intrinsic such interaction can now be classified exactly. Pairing two character fields around a common interior circle does genuinely synthesize the product conductor: for coprime primitive shell orders `n,m`, individual root channels acquire primitive `nm`-th-root poles. However, after the shell character sums are retained, the whole two-shell pairing is **exactly a scalar phase times the ordinary PC-197 character packet of the composite shell `nm`, evaluated at the summed radial depth**. A double Mellin transform therefore gives only `Gamma(s)Gamma(t)L(s+t,chi bar(psi))`.

Thus this route escapes the pole-support obstruction of PC-198 but still does not escape classical Dirichlet `L`-theory. The durable boundary is sharper: creating a mixed conductor is not enough; a surviving cross-shell mechanism must retain genuinely nonseparable two-index/two-variable information rather than collapsing to character multiplication and radial-semigroup addition.

## 1. Angularized PC-197 character fields

Let

\[
\zeta_n=e^{2\pi i/n},
\qquad
0<r=e^{-x}<1,
\qquad
x>0.
\]

For a primitive vertex `a in U(n)`, angularize the PC-197 Cayley field by

\[
K_{n,a}(x,\theta)
:=
\frac{1+e^{-x}e^{i\theta}\zeta_n^a}
{1-e^{-x}e^{i\theta}\zeta_n^a}.
\tag{1}
\]

Its absolutely convergent positive-frequency expansion is

\[
K_{n,a}(x,\theta)
=
1+2\sum_{k\ge1}e^{-kx}e^{ik\theta}\zeta_n^{ak}.
\tag{2}
\]

Let `chi` be a primitive nonprincipal Dirichlet character modulo `n` and define

\[
\mathcal K_{n,\chi}(x,\theta)
:=
\sum_{a\in U(n)}\overline{\chi(a)}K_{n,a}(x,\theta).
\tag{3}
\]

The constant term vanishes. Using the primitive Gauss identity exactly as in PC-197 gives

\[
\boxed{
\mathcal K_{n,\chi}(x,\theta)
=
2\tau(\overline\chi)
\sum_{k\ge1}\chi(k)e^{-kx}e^{ik\theta}.
}
\tag{4}
\]

For every fixed `x>0` this is an ordinary square-integrable circle field. No boundary `H^2` claim is needed: the coefficient norm diverges as `x -> 0+`, and all pairings below are taken at positive depth before any limiting operation.

## 2. The canonical two-shell pairing is coefficientwise character multiplication

Let `psi` be a primitive nonprincipal character modulo `m`, and allow the two fields to sit at **different** radial depths `x,y>0`. Their natural angular sesquilinear pairing is

\[
\mathcal P_{n,\chi;m,\psi}(x,y)
:=
\frac1{2\pi}
\int_0^{2\pi}
\mathcal K_{n,\chi}(x,\theta)
\overline{\mathcal K_{m,\psi}(y,\theta)}
\,d\theta.
\tag{5}
\]

Substituting (4), absolute convergence permits termwise integration. Angular orthogonality forces the two Fourier indices to be equal, hence

\[
\boxed{
\mathcal P_{n,\chi;m,\psi}(x,y)
=
4\tau(\overline\chi)
\overline{\tau(\overline\psi)}
\sum_{k\ge1}
\chi(k)\overline{\psi(k)}e^{-k(x+y)}.
}
\tag{6}
\]

Put

\[
\eta:=\chi\,\overline\psi.
\tag{7}
\]

Equation (6) already gives the decisive structural collapse:

- the two radial depths survive only through the single combination `x+y`;
- the two shell characters survive only through their pointwise product `eta`;
- the angular integral introduces no second Fourier index and no new convolution law.

If one removes the harmless Gauss normalization and writes

\[
F_\chi(z):=\sum_{k\ge1}\chi(k)z^k,
\tag{8}
\]

then (6) is simply the exact fusion rule

\[
\boxed{
\frac{
\mathcal P_{n,\chi;m,\psi}(x,y)
}{4\tau(\overline\chi)\overline{\tau(\overline\psi)}}
=
F_\eta(e^{-(x+y)}).
}
\tag{9}
\]

Thus the standard sesquilinear geometry is the Hadamard/Parseval multiplication law for the character coefficients.

## 3. Rootwise channels really do create mixed cyclotomic poles

This result is not merely another version of the PC-198 pole-support obstruction. Before summing over shell characters, take roots `alpha` and `beta` and subtract the constant term from (1):

\[
H_\alpha(z)
:=
\frac{1+\alpha z}{1-\alpha z}-1
=
2\sum_{k\ge1}\alpha^k z^k.
\tag{10}
\]

At depths `x,y`, the angular pairing of two individual channels is

\[
\begin{aligned}
\frac1{2\pi}
\int_0^{2\pi}
&H_\alpha(e^{-x}e^{i\theta})
\overline{H_\beta(e^{-y}e^{i\theta})}
\,d\theta\\
&=
4\sum_{k\ge1}
(\alpha\overline\beta)^k e^{-k(x+y)}\\
&=
\boxed{
\frac{4e^{-(x+y)}\alpha\overline\beta}
{1-e^{-(x+y)}\alpha\overline\beta}.
}
\end{aligned}
\tag{11}
\]

If `alpha` has exact order `n`, `beta` has exact order `m`, and `gcd(n,m)=1`, then `alpha bar(beta)` has exact order `nm`: if `(alpha bar(beta))^j=1`, then `alpha^j=beta^j` lies in `mu_n cap mu_m={1}`, so both `n` and `m` divide `j`.

Therefore the complexified depth variable

\[
w=e^{-(x+y)}
\]

has a genuine primitive `nm`-th-root pole in (11). **Sesquilinearity really does synthesize mixed cyclotomic support that finite same-variable holomorphic products could not create in PC-198.** The negative result below is stronger because it shows that this newly created mixed support is nevertheless exactly the classical composite-character packet.

## 4. Coprime primitive shells collapse exactly to one composite shell

Assume now

\[
\gcd(n,m)=1
\]

and that `chi mod n` and `psi mod m` are primitive. Then

\[
\eta=\chi\overline\psi
\]

is a primitive character of conductor `N=nm`. PC-197 applied directly to that composite shell gives

\[
\mathcal K_{N,\eta}(u)
=
2\tau(\overline\eta)
\sum_{k\ge1}\eta(k)e^{-ku}.
\tag{12}
\]

Comparing (6) with (12) yields immediately

\[
\boxed{
\mathcal P_{n,\chi;m,\psi}(x,y)
=
\frac{2\tau(\overline\chi)
\overline{\tau(\overline\psi)}}
{\tau(\overline\eta)}
\mathcal K_{nm,\eta}(x+y).
}
\tag{13}
\]

The prefactor is not a new arithmetic invariant. Classical CRT multiplicativity of primitive Gauss sums gives

\[
\tau(\overline\eta)
=
\overline\chi(m)\psi(n)
\tau(\overline\chi)\tau(\psi),
\tag{14}
\]

while

\[
\overline{\tau(\overline\psi)}
=
\psi(-1)\tau(\psi).
\tag{15}
\]

Hence the complete fusion law becomes

\[
\boxed{
\mathcal P_{n,\chi;m,\psi}(x,y)
=
2\,
\frac{\psi(-1)}
{\overline\chi(m)\psi(n)}
\mathcal K_{nm,\chi\overline\psi}(x+y).
}
\tag{16}
\]

The scalar in front has modulus `2` and consists only of finite character phases. Thus, even before Mellinization, the canonical two-shell/two-depth object is **literally a single composite-shell PC-197 field at the summed depth**, up to an elementary CRT phase.

This is the matched control that rules out interpreting the mixed conductor itself as new Prime-Circle spectral information.

## 5. Exact finite control at conductors 3 and 5

Take the quadratic character `chi_3` modulo `3` and the quadratic character `psi_5` modulo `5`. Both are primitive, and

\[
\eta=\chi_3\psi_5
\]

is primitive modulo `15`. Their finite character values give

\[
\psi_5(-1)=1,
\qquad
\chi_3(5)=-1,
\qquad
\psi_5(3)=-1.
\]

Therefore the phase in (16) is exactly `+1`, and

\[
\boxed{
\mathcal P_{3,\chi_3;5,\psi_5}(x,y)
=
2\mathcal K_{15,\eta}(x+y).
}
\tag{17}
\]

Direct coefficient comparison gives the same result: both sides are the same `15`-periodic product-character sequence multiplied by `e^{-k(x+y)}`, with the Gauss constants related by (14). This control fixes the conjugation/sign convention in (16).

## 6. Double Mellinization has only the single variable `s+t`

A possible repair is to insist that two independent radial depths should produce two independent spectral parameters. Equation (6) rules that out for this canonical pairing.

For

\[
\Re s>0,
\qquad
\Re t>0,
\qquad
\Re(s+t)>1,
\]

absolute convergence gives

\[
\begin{aligned}
\mathcal M_2\mathcal P(s,t)
&:=
\int_0^\infty\int_0^\infty
x^{s-1}y^{t-1}
\mathcal P_{n,\chi;m,\psi}(x,y)
\,dx\,dy\\
&=
4\tau(\overline\chi)
\overline{\tau(\overline\psi)}
\sum_{k\ge1}\eta(k)
\left(\int_0^\infty x^{s-1}e^{-kx}dx\right)
\left(\int_0^\infty y^{t-1}e^{-ky}dy\right).
\end{aligned}
\]

Thus

\[
\boxed{
\mathcal M_2\mathcal P(s,t)
=
4\tau(\overline\chi)
\overline{\tau(\overline\psi)}
\Gamma(s)\Gamma(t)L(s+t,\eta).
}
\tag{18}
\]

There is no genuinely two-variable `L`-object. The zero divisor is simply the pullback of the ordinary Dirichlet zero divisor under

\[
(s,t)\longmapsto s+t.
\]

Consequently a hypersurface such as

\[
\Re(s+t)=\frac12
\]

would merely be the pullback of GRH for `L(u,eta)` in the single variable `u=s+t`. Restricting by hand to a diagonal such as `s=t` would instead produce `L(2s,eta)` and move the classical critical line by a coordinate rescaling; neither operation supplies a zero-confining principle.

The completed functional equation also remains the ordinary primitive Dirichlet functional equation in the variable `u=s+t`. The separate factors `Gamma(s)Gamma(t)` arise only from taking two Mellin transforms of the separable exponential semigroup and do not create an independent `u <-> 1-u` geometry.

## 7. Prior-art and novelty audit

Every general ingredient is classical.

The angular step is Parseval/Fourier orthogonality for analytic power series on a circle. The multiplicative projection is the standard primitive Gauss finite Fourier transform already used and classicalized in PC-025/PC-197; `research/prime_circle/SOURCES.md` records Montgomery–Vaughan as an explicit modern anchor for this character/Gauss package. Character multiplication and the coprime-conductor Gauss-sum factorization (14) are standard CRT identities. Finally, the Dirichlet series and functional equation for `L(s,eta)` are classical; a directed check against NIST DLMF §25.15 and standard analytic-number-theory references found exactly this established structure, not a distinct two-shell spectral theory.

No theorem-level novelty is claimed for (6), (14), or (18). The Mathia-specific content is the exact placement of the Prime-Circle construction relative to PC-197/PC-198: **the first canonical sesquilinear escape really can manufacture the mixed cyclotomic conductor, but that entire mixed carrier is already isomorphic to the ordinary composite-shell Dirichlet-character packet.**

This also distinguishes the result from the older Hardy/Hankel trace branch (PC-075 onward). Those findings classify products, traces, determinants and conductor limits of a different Hankel-operator realization. Here the object is the source-native vertexwise Cauchy–Poisson field introduced in PC-197, and the obstruction is the exact character-fusion law before any Hardy/Hankel determinant is formed.

## 8. Boundary of the negative result

The finding rules out the route

\[
\boxed{
\text{two primitive Cauchy--Poisson shell fields}
\xrightarrow{\text{angular sesquilinear pairing}}
\text{mixed conductor}
\xrightarrow{\text{one/double radial Mellin}}
\text{new RH/GRH mechanism}.
}
\]

It also rules out the simplest different-depth repair: the two depths collapse exactly to `x+y` before Mellinization.

It does **not** rule out interactions that avoid the shared-Fourier-index diagonalization in (5). In particular, still outside this result are kernels with two independent angular indices, shell-dependent non-diagonal angular operators, matrix/cocycle constructions that keep both shell labels active after coupling, inverse-limit/solenoidal interactions that do not factor through one product character, and the global uniformization/monodromy branch.

The practical frontier after PC-199 is therefore sharper than the one left by PC-198: a viable cross-shell construction must preserve genuinely nonseparable information after coupling. Merely producing primitive `nm`-th-root support or a conductor-`nm` Dirichlet `L`-function is insufficient, because the canonical sesquilinear mechanism does both and still collapses exactly to one classical composite-shell packet.
