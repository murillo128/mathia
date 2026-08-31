# WP-056 — Prym polarization stores `log p` in its integral discriminant, not in the positive Hodge pairing

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CANDIDATE-LOCAL-BRIDGE + DECISIVE-BOUNDARY + PRIOR-ART-REDIRECT` for the strongest intrinsic refinement of the old-prime Hodge route left open by `WP-055`.

`WP-055` showed that the granted hyperelliptic lift

\[
C_n:\qquad y^2=\Phi_n(x)
\]

has a genuine positive Hodge theory and that, whenever `p|n`, the old-prime refinement

\[
f_{n,p}:C_{pn}\to C_n,\qquad (x,y)\mapsto(x^p,y)
\]

is a cyclic cover of degree `p`. After the canonical square-root degree normalization, Hodge pullback is exactly isometric, while normalized transfer contributes the critical half-density `p^{-1/2}`. The apparent missing local scalar `log p` was therefore recorded there only as `log deg(f)` rather than as a value of the positive Hodge form.

The induced Prym polarization contains a stronger fact. The restriction of the principal Jacobian polarization to

\[
P_{n,p}:=\operatorname{Prym}(C_{pn}/C_n)
\]

has elementary-divisor type

\[
\boxed{
D_{n,p}=
\left(1^{\,d_{n,p}-g_n},\;p^{\,g_n}\right),
\qquad
d_{n,p}=(p-1)(g_n+1),
}
\]

whenever `g_n>0`, where

\[
g_n=\frac{\varphi(n)-2}{2}.
\]

Equivalently, its polarization isogeny has

\[
\boxed{
|\ker\lambda_{n,p}|=\deg\lambda_{n,p}=p^{2g_n}.
}
\]

Thus the same positive polarized Hodge object really does remember the prime degree intrinsically:

\[
\boxed{
\frac{1}{2g_n}\log\deg\lambda_{n,p}=\log p
\qquad(g_n>0).
}
\]

Combining this scalar lattice invariant with the `k`-step normalized transfer from `WP-055` gives

\[
\left(\frac{1}{2g_n}\log\deg\lambda_{n,p}\right)
\left(E^{(k)}J^{(k)}\right)
=(\log p)p^{-k/2}I,
\]

so both numerical factors of the interior finite Weil ray are present inside one old-prime cover tower without zeta zeros or analytic continuation.

This is a genuine strengthening of the local bridge, but it still does **not** give Weil positivity. The `p`-dependence lives in the **integral lattice type / finite kernel of a polarization**, while the normalized real/complex Hodge metric remains degree-flat. Extracting `log p` requires a logarithm of a determinant/cardinality, not evaluation of a positive bilinear form. Moreover the polarization type is universal for cyclic covers of the same degree, base genus, and ramification type; it survives non-arithmetic matched controls unchanged. At genus-zero base levels it forgets `p` completely, and direct degree-`p^k` covers store `k log p`, so the Weil coefficient still requires a one-step-versus-`k`-step relative construction. No archimedean `Gamma_R` or polar term is produced.

The surviving lesson is therefore narrow but useful: **integral polarization data can retain arithmetic scale that ordinary normalized Hodge norms erase, but that scale is currently available only through a nonlinear topological discriminant rather than through the positive quadratic pairing demanded by the Weil criterion.**

## 1. Old-prime refinement is a four-point ramified cyclic cover

For `n>2`,

\[
g_n=\frac{\varphi(n)-2}{2}
\]

is the genus of the smooth projective completion of `C_n`. If `p|n`, the cyclotomic identity

\[
\Phi_{pn}(x)=\Phi_n(x^p)
\]

lifts the power map to

\[
f=f_{n,p}:C_{pn}\to C_n,
\qquad
f(x,y)=(x^p,y).
\tag{1}
\]

As derived in `WP-055`, `f` is cyclic of degree `p`, with deck group `mu_p` acting by `x\mapsto\zeta x`. The map is totally ramified over the two points of `C_n` above `x=0` and the two points above `x=\infty`; hence its reduced branch divisor has degree

\[
\boxed{r=4.}
\tag{2}
\]

Riemann--Hurwitz gives

\[
g_{pn}=p g_n-p+1+\frac{4(p-1)}2
=p g_n+p-1.
\tag{3}
\]

Therefore the Prym dimension is

\[
\boxed{
 d_{n,p}=g_{pn}-g_n=(p-1)(g_n+1)
 =\frac{(p-1)\varphi(n)}2.
}
\tag{4}
\]

This agrees with half of the real `H^1` new-sector dimension `(p-1)phi(n)` computed in `WP-055`.

## 2. The induced Prym polarization contains an exact `p`-block

For a cyclic cover of degree `q`, base genus `g`, and nonempty reduced branch divisor, the classical Prym-polarization formula says that the principal polarization of the covering Jacobian restricts to the Prym with type

\[
D=(1^{\,d-g},q^{\,g}),
\tag{5}
\]

where `d` is the Prym dimension. Lange--Ortega record this explicitly for cyclic coverings: for `r>0`, the elementary divisor `q` occurs `g` times and `1` occurs `d-g` times.

Specializing (5) to (1)--(4) gives

\[
\boxed{
D_{n,p}
=\left(1^{\,d_{n,p}-g_n},p^{\,g_n}\right).
}
\tag{6}
\]

For a polarization of type `(d_1,...,d_d)`, the associated isogeny to the dual abelian variety has kernel order

\[
|\ker\lambda|=\left(\prod_i d_i\right)^2.
\tag{7}
\]

Consequently

\[
\boxed{
|\ker\lambda_{n,p}|
=\deg\lambda_{n,p}
=p^{2g_n}.
}
\tag{8}
\]

There is also a basis-free explanation of the same `p`-torsion. Let

\[
A=J(C_{pn}),\qquad B=f^*J(C_n),\qquad P=P_{n,p}.
\]

Norm is the Rosati adjoint of pullback for the canonical principal polarizations, so `P` is the connected orthogonal complement of `B`. For the ramified prime-degree cover, `f^*` is injective, and

\[
\operatorname{Nm}_f\circ f^*=[p]
\tag{9}
\]

on `J(C_n)`. Thus the finite overlap governing the restricted polarization is exactly the pulled-back `p`-torsion:

\[
P\cap B=f^*J(C_n)[p],
\tag{10}
\]

whose order is `p^{2g_n}`. Equation (10) is the intrinsic form of the `p` elementary divisors in (6): the prime is not an artifact of choosing a symplectic basis.

For `g_n=0`, the same description gives the decisive boundary case. Then `J(C_n)=0`, so

\[
P_{n,p}=J(C_{pn})
\]

with its principal polarization and

\[
|\ker\lambda_{n,p}|=1.
\tag{11}
\]

The polarization therefore contains no `p`-block at all at genus-zero base levels.

## 3. `log p` is recoverable canonically from the polarization kernel when `g_n>0`

For positive base genus, (8) immediately yields

\[
\boxed{
\log p
=\frac1{2g_n}\log|\ker\lambda_{n,p}|
=\frac1{2g_n}\log\deg\lambda_{n,p}.
}
\tag{12}
\]

The normalization is intrinsic to the cover: `2g_n` is the rank of the integral first homology of the base, equivalently the logarithmic exponent of the full base `p`-torsion. So the old-prime Hodge lift carries more arithmetic scale than the degree-normalized norm computation of `WP-055` alone revealed.

This is nevertheless a **lattice/discriminant readout**, not the value of the positive Hodge quadratic form on a distinguished vector. The polarization is a positive integral Riemann form together with its lattice; equation (12) uses the finite-index defect of that integral form. It therefore belongs to the same broad family of nonlinear determinant information already encountered in `WP-043`, where a positive cycle Laplacian remembers `Lambda(n)` through a shell log-determinant without making that logarithm the positive pairing itself.

## 4. The same tower contains the critical half-density, but only through a different operation

`WP-055` defines the square-root degree-normalized pullback

\[
J_{n,p}=p^{-1/2}f^*
\]

and normalized transfer

\[
E_{n,p}=p^{-1}f_*.
\]

They satisfy

\[
J_{n,p}^*J_{n,p}=I,
\qquad
E_{n,p}J_{n,p}=p^{-1/2}I.
\tag{13}
\]

Across `k` old-prime refinements,

\[
\boxed{
E^{(k)}J^{(k)}=p^{-k/2}I.
}
\tag{14}
\]

Combining (12) and (14) gives the exact finite Weil ray scalar

\[
\boxed{
\left(\frac1{2g_n}\log\deg\lambda_{n,p}\right)
E^{(k)}J^{(k)}
=(\log p)p^{-k/2}I.
}
\tag{15}
\]

Equation (15) is a real same-tower bridge: the logarithmic prime scale and the critical half-density are both forced by canonical cover data. But they come from **different functors** on that data:

- `log p` comes from the integral discriminant/kernel of the one-step Prym polarization;
- `p^{-k/2}` comes from Hilbert normalization of a `k`-step pull-push transfer.

Nothing in polarization positivity proves that their product is the value of one positive quadratic form.

## 5. Direct `p^k` covers expose the relative nature of the extraction

There is an especially sharp control against overinterpreting (15). Composing `k` old-prime maps gives a cyclic cover of total degree `p^k`,

\[
F^{(k)}:C_{p^k n}\to C_n,
\qquad(x,y)\mapsto(x^{p^k},y),
\tag{16}
\]

again ramified over the same four base points. Applying the same polarization-type formula to this **single direct cover** gives elementary divisor `p^k` on each of the `g_n` base directions, hence

\[
\frac1{2g_n}\log\deg\lambda_{F^{(k)}}
=\log(p^k)
=k\log p.
\tag{17}
\]

But the Riemann finite coefficient at the prime power `p^k` is

\[
\Lambda(p^k)=\log p,
\tag{18}
\]

not `k log p`. Thus the desired coefficient is **not** the logarithmic discriminant of the direct `p^k` cover. One must either retain a one-step edge invariant while separately remembering a `k`-step transfer, or take a relative increment such as

\[
\log\deg\lambda_{F^{(k)}}-\log\deg\lambda_{F^{(k-1)}}.
\tag{19}
\]

The latter is a difference of nonlinear invariants, not a positive Hodge energy. This is the cover-theoretic analogue of the recurring Weil-positivity obstruction: the arithmetic signal appears after a relative/logarithmic extraction that is not itself protected by the original positivity theorem.

## 6. Genus-zero levels are an exact internal counterexample

The base genus vanishes whenever `phi(n)=2`, for example

\[
n\in\{3,4,6\}.
\]

For such an old-prime ray, the local Riemann coefficient remains nonzero. For instance, with `n=4` and `p=2`, the refinements `4\to8\to16\to\cdots` should carry

\[
(\log2)2^{-k/2}.
\]

Yet by (11) the first Prym is simply the Jacobian of the covering curve with principal polarization, so its polarization kernel has cardinality one and (12) is unavailable. The `log p` discriminant mechanism therefore cannot be a uniform local realization of all finite Weil rays.

This is stronger than a small-level normalization nuisance: it shows that the information carrier is the **base Jacobian `p`-torsion**. When the base has no `H^1`, the carrier vanishes even though `Lambda(p^k)` does not.

## 7. Matched cyclic-cover control: the discriminant is topological degree data

The polarization type (5) depends only on the topological covering data: cover degree, base genus, and ramification type. Replace the cyclotomic curves by an unrelated cyclic degree-`p` cover of a genus-`g` curve, totally ramified over four reduced points. Its Prym polarization has exactly the same type

\[
(1^{\,d-g},p^{\,g})
\]

and the same kernel order `p^{2g}`.

Therefore the extraction

\[
\frac1{2g}\log\deg\lambda=\log p
\]

is **universal cyclic-cover geometry**. Cyclotomy tells Mathia which degree-`p` covers occur along old-prime refinement, but polarization positivity does not know that these degrees are arithmetic primes rather than arbitrary covering degrees. This matched control kills any claim that (12) is already an RH-specific or Riemann-specific positivity mechanism.

The control also clarifies the relation to `WP-055`: square-root degree transfer and Prym polarization type are both standard consequences of finite-cover geometry. The former supplies `p^{-1/2}` and the latter stores `p` integrally, but neither creates Frobenius-like fixed-point statistics or cross-prime arithmetic dynamics.

## 8. No cross-prime or archimedean completion is generated

The limitations of `WP-055` remain untouched.

If `p\nmid n`, the factorization

\[
\Phi_n(x^p)=\Phi_n(x)\Phi_{pn}(x)
\]

prevents the simple map `C_{pn}\to C_n`; the Hodge/Prym tower organizes repeated-prime rays but does not furnish a canonical cross-prime correspondence. Taking an orthogonal direct sum over primes would return to separable local positivity and the global-completion obstructions already established in `WP-001`, `WP-013`, and `WP-026`.

Likewise, the polarized Prym supplies no continuous spectral/Mellin variable, no digamma response, no Riemann `Gamma_R` factor, and no polar term. The intrinsic `q=2` archimedean selector of `WP-048` remains a different Prime-Circle construction. Equating the hyperelliptic covering geometry with that order-two Mellin channel merely because both involve a double-cover/reflection structure would be target matching; no coupling theorem currently connects them.

Thus the local bridge

\[
\text{Prym polarization kernel}
\to\log p,
\qquad
\text{normalized transfer}
\to p^{-k/2}
\]

still stops before the research mandate's decisive requirement: a **single global finite--archimedean form whose nonnegativity follows independently from geometry**.

## 9. Prior-art and novelty audit

No historical novelty is claimed for the Prym theory used here.

- Herbert Lange and Angela Ortega, *Prym varieties of cyclic coverings*, Geometriae Dedicata 150 (2011), 391--403, DOI `10.1007/s10711-010-9512-9`, arXiv `0805.1020`, record the dimension of a cyclic-cover Prym and the induced polarization type. For ramified degree-`q` covers they state that `q` occurs as an elementary divisor once for each base-genus direction. Their formula is the decisive classical input behind (6)--(8).
- The identities `Nm_f f^*=[deg f]`, orthogonality of pullback Jacobian and Prym, elementary-divisor classification of polarizations, and `deg lambda=(prod d_i)^2` are standard Jacobian/Prym and polarized-abelian-variety theory.
- `WP-055` already derived the Mathia-specific cyclotomic cover tower and its degree-normalized Hodge transfer. `WP-043` already supplies the closest internal warning that a positive geometric operator may encode exact arithmetic only through a nonlinear log-determinant rather than through the relevant positive pairing.

Directed literature searches for cyclic-cover Prym polarization types, their kernel/discriminant, and degree-`p` Prym maps show that the `p` elementary-divisor block is classical and actively used as the target polarization type of Prym moduli maps. There is no basis for claiming novelty for recovering `log p` by taking the logarithm of its kernel order. The durable Mathia-specific result is instead the **bridge-and-boundary synthesis**: the old-prime hyperelliptic lift of `WP-055` contains the missing local logarithmic prime scale inside its integral Hodge lattice, but precisely in a nonlinear topological invariant that is universal for cyclic covers, fails at genus-zero base levels, and does not supply the global Weil-positive pairing.

## 10. Boundary of the result

This finding rules out the claim that merely enriching `WP-055` from real Hodge norms to the **ordinary induced Prym polarization** solves the Weil-positivity problem. The ordinary polarization does contain more arithmetic scale than the normalized Hodge norm, but its direct positive form is still not the desired functional.

It does **not** rule out:

- a determinant-line or height construction in which the integral polarization kernel enters a genuinely bilinear global object before taking logarithms;
- a canonical relative polarization pairing with an independent order/sign theorem;
- an arithmetic or Arakelov metric on the Prym determinant line forced by Mathia rather than fitted to `Gamma_R`;
- a nonseparable correspondence coupling the Prym lattice to the intrinsic `q=2` radial/Mellin channel before positivity is formulated;
- a higher-dimensional or noncommutative cohomological object in which cover degree, ramification, and archimedean data are parts of one global class.

Any such escape must explain why the genus-zero failure is repaired, why `Lambda(p^k)=log p` rather than `k log p` is selected without an arbitrary relative subtraction, how different prime directions interact, and why the resulting completed form is nonnegative independently of RH or inserted zero data.

## 11. Falsification surface

The result has short exact checks.

1. Verify the old-prime identity `Phi_{pn}(x)=Phi_n(x^p)` for `p|n` and the degree-`p` cover (1).
2. Verify that `x=0` and `x=infinity` each have two lifts on the even-degree hyperelliptic base and give four total ramification points.
3. Insert `q=p`, `g=g_n`, `r=4` into the classical cyclic Prym formulas and recover (4) and (6).
4. From the polarization type, verify `deg lambda=p^{2g_n}`; independently check the same order from `P intersect f^*J(C_n)=f^*J(C_n)[p]`.
5. For `g_n=0`, verify directly that the Prym equals the covering Jacobian and its induced polarization is principal.
6. For the direct degree-`p^k` cover, verify that the elementary divisor becomes `p^k` and the normalized log degree is `k log p`, not `log p`.
7. Replace the cyclotomic curves by an arbitrary four-point ramified cyclic degree-`p` cover of the same base genus and verify that the polarization type is unchanged.
8. Check that no operation above produces the `Gamma_R`/digamma or polar sector, and that (15) is a product of two scalar readouts rather than the value of one positive quadratic form.

Failure of items 1--5 would invalidate the claimed local bridge. Success of all eight still does not prove Weil positivity; it instead locates the surviving information more precisely in **integral polarization data beyond the degree-flat Hodge norm**.