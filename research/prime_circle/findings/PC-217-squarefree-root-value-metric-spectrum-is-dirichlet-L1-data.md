# PC-217 — squarefree root-value metric spectrum is Dirichlet `L(1)` data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the packetwise unitary/metric escape left explicitly open by PC-216: retain the modulus profile destroyed by diagonal similarity, and ask whether singular values, condition numbers, or quadratic metric energies of the source-forced omitted-prime transport contain a new arithmetic carrier.

They do not at the fixed reduced-conductor packet level. For squarefree `d`, the complete logarithmic modulus profile of the derivative potential

\[
\eta_d(a)=\zeta_d^a\Phi_d'(\zeta_d^a),
\qquad a\in U(d),
\]

has an exact multiplicative Fourier decomposition. Its principal mode is the classical cyclotomic discriminant, every odd character vanishes, and every nonprincipal even character is an explicit Gauss factor times a primitive Dirichlet value `L(1,chi*)`, multiplied only by elementary local factors from primes dividing `d/conductor(chi)`.

Consequently every squarefree root-value modulus packet of PC-216, and every log-singular-value profile of its canonical weighted residue transports, is obtained from the same fixed `L(1)` packet by multiplying character modes by finite factors `chi(q)-1`. The packetwise metric repair therefore classicalizes to the same log-sine/cyclotomic-unit harmonic data already encountered in PC-025, now with explicit conductor-stripping factors.

This does **not** collapse the simultaneous assembly of several reduced conductors inside the full PC-215 operator `T_N`; different conductor packets still carry different Fourier spaces and incompatible gauges. What is closed is the specific PC-216 escape through metric invariants of one source-derived divisor-cube packet or one of its omitted-prime weighted shifts.

## 1. The derivative modulus is a finite sum of anchored chord fields

Let `d>1` be squarefree, put

\[
G_d=U(d)=(\mathbb Z/d\mathbb Z)^\times,
\qquad
\zeta_d=e^{2\pi i/d},
\]

and define

\[
\eta_d(a)=\zeta_d^a\Phi_d'(\zeta_d^a),
\qquad
u_d(a)=\log|\eta_d(a)|.
\tag{1}
\]

The standard Möbius product

\[
\Phi_d(x)=\prod_{e\mid d}(x^e-1)^{\mu(d/e)}
\tag{2}
\]

has exactly one vanishing factor at the primitive root `zeta_d^a`, namely `e=d`. Taking the derivative through that simple zero gives

\[
\Phi_d'(\zeta_d^a)
=d(\zeta_d^a)^{d-1}
\prod_{\substack{e\mid d\\e<d}}
((\zeta_d^a)^e-1)^{\mu(d/e)}.
\tag{3}
\]

Writing `h=d/e` and taking absolute values yields the exact identity

\[
\boxed{
\nu_d(a)
=
\log d+
\sum_{\substack{h\mid d\\h>1}}
\mu(h)\log|1-\zeta_h^a|.
}
\tag{4}
\]

Thus the metric datum left open by PC-216 is not a new local field: it is a finite Möbius combination of the same anchored log-chord profiles whose multiplicative harmonic analysis was classicalized in PC-025.

## 2. Exact multiplicative Fourier coefficients

For a character `chi` of `G_d`, use normalized Fourier coefficients

\[
\widehat\nu_d(\chi)
=
\frac1{\varphi(d)}
\sum_{a\in G_d}\nu_d(a)\overline{\chi(a)}.
\tag{5}
\]

The principal coefficient follows immediately from the classical discriminant formula

\[
|\operatorname{Disc}(\Phi_d)|
=
\frac{d^{\varphi(d)}}
{\displaystyle\prod_{p\mid d}p^{\varphi(d)/(p-1)}}.
\tag{6}
\]

Since the discriminant is, up to sign, the product of `Phi_d'` over all primitive roots,

\[
\boxed{
\widehat\nu_d(\mathbf1)
=
\log d-
\sum_{p\mid d}\frac{\log p}{p-1}.
}
\tag{7}
\]

Also `nu_d(-a)=nu_d(a)`, so

\[
\boxed{
\widehat\nu_d(\chi)=0
\qquad(\chi(-1)=-1).
}
\tag{8}
\]

Now let `chi` be nonprincipal and even, induced by a primitive character `chi*` of conductor `f|d`. For any `h|d`, the field `a -> log|1-zeta_h^a|` factors through `U(h)`. Its `chi` coefficient therefore vanishes unless `f|h`.

Write `h=ft`, `(f,t)=1`. A direct CRT decomposition of the additive character sum gives

\[
\sum_{b\in U(h)}
\overline{\chi(b)}\log|1-\zeta_h^b|
=
-\tau(\overline{\chi^*})L(1,\chi^*)
\prod_{p\mid t}(1-\overline{\chi^*(p)}),
\tag{9}
\]

where

\[
\tau(\overline{\chi^*})
=
\sum_{a\bmod f}\overline{\chi^*(a)}e^{2\pi ia/f}.
\tag{10}
\]

Equation (9) is the ordinary primitive even-character log-sine formula after inducing from modulus `f` to the squarefree modulus `ft`; the extra Euler factors come only from the Ramanujan sum on the new CRT coordinates.

Substituting (9) into (4) and summing over `t|d/f` factorizes completely:

\[
\boxed{
\widehat\nu_d(\chi)
=
-\frac{\mu(f)}{\varphi(f)}
\tau(\overline{\chi^*})L(1,\chi^*)
\prod_{p\mid d/f}
\frac{p-2+\overline{\chi^*(p)}}{p-1}.
}
\tag{11}
\]

So the entire labeled modulus field `nu_d` is reconstructed from one discriminant scalar plus a finite packet of classical even Dirichlet `L(1)` values. There is no additional metric degree of freedom hidden in `|eta_d|`.

As a check, take the quadratic character of conductor `5`. At `d=15`, the local `p=3` factor in (11) vanishes because `chi(3)=-1`, so that character mode is exactly absent. At `d=35`, the local factor is `2/3` and (11) gives

\[
\widehat\nu_{35}(\chi_5)
=\frac{\sqrt5}{6}L(1,\chi_5)
=\frac13\log\frac{1+\sqrt5}{2}.
\tag{12}
\]

## 3. Every PC-216 squarefree root-value modulus is the same `L(1)` packet with finite differences

Let

\[
N=dM,
\qquad(d,M)=1,
\]

with `N` squarefree, and define the proper-divisor root-value modulus

\[
v_{d,M}(a)
:=
\log|\Phi_{dM}(\zeta_d^a)|.
\tag{13}
\]

For a prime `q` coprime to `d`, write

\[
(T_qF)(a)=F(qa).
\tag{14}
\]

PC-216 proves at the complex multiplicative level that the one-prime complement is a first coboundary and every further omitted prime is another commuting finite difference. Taking absolute logarithms therefore gives

\[
\boxed{
v_{d,q}=\log q+(T_q-I)\nu_d}
\tag{15}
\]

when `M=q` is prime, while for `omega(M)>=2`,

\[
\boxed{
v_{d,M}
=\prod_{q\mid M}(T_q-I)\nu_d.}
\tag{16}
\]

Characters diagonalize every `T_q`. Hence for every nonprincipal character of `G_d`,

\[
\boxed{
\widehat v_{d,M}(\chi)
=
\left(\prod_{q\mid M}(\chi(q)-1)\right)
\widehat\nu_d(\chi).
}
\tag{17}
\]

Combining (11) and (17) gives the complete source coefficient modulus packet:

\[
\boxed{
\widehat v_{d,M}(\chi)
=
-\frac{\mu(f)}{\varphi(f)}
\tau(\overline{\chi^*})L(1,\chi^*)
\prod_{p\mid d/f}
\frac{p-2+\overline{\chi^*(p)}}{p-1}
\prod_{q\mid M}(\chi^*(q)-1)
}
\tag{18}
\]

for every nonprincipal even `chi`; odd modes vanish. The principal mode is `log q` when `M=q` and zero when `omega(M)>=2`, exactly matching the resultant products already recovered in PC-216.

Thus the modulus information that survived PC-216's nonunitary diagonal similarity is not merely bounded by classical data: its complete multiplicative harmonic decomposition is explicitly classical Dirichlet `L(1)` data.

## 4. Singular values of the weighted transport add no further packet

PC-216's normalized omitted-prime transport has the monomial form

\[
W_{q,F}=D_FR_qD_F^{-1},
\qquad
w(a)=\frac{F(qa)}{F(a)},
\tag{19}
\]

where `R_q` is the residue permutation. Although this similarity is not unitary, monomiality makes its metric spectrum transparent:

\[
W_{q,F}^*W_{q,F}
\]

is diagonal up to permutation, with diagonal entries `|w(a)|^2`. Therefore the singular values are exactly

\[
\boxed{
\sigma_a(W_{q,F})
=\left|\frac{F(qa)}{F(a)}\right|,
}
\tag{20}
\]

as a multiset.

If `F` is any source packet generated in the PC-216 divisor cube, then `log|F|` is a finite product of the differences `(T_r-I)` applied to `nu_d`. Hence

\[
\log\sigma_a
=(T_q-I)\log|F|(a),
\tag{21}
\]

and its character coefficients are again (11) multiplied by additional factors `chi(r)-1`.

Therefore all packetwise singular values, condition numbers, Schatten norms, and pseudospectral metric quantities of this monomial transport are functions of the same finite `L(1)` packet. They do not create a second arithmetic spectrum after PC-216 removes the eigenvalue holonomy.

A particularly natural quadratic metric is completely explicit by Parseval. For the root-value packet (13),

\[
\frac1{\varphi(d)}
\sum_{a\in G_d}
|v_{d,M}(a)-\widehat v_{d,M}(\mathbf1)|^2
=
\sum_{\substack{\chi\ne\mathbf1\\\chi(-1)=1}}
|\widehat v_{d,M}(\chi)|^2,
\tag{22}
\]

and because `|tau(chi*)|^2=f`, the right side is an explicit finite weighted second moment of `|L(1,chi*)|^2` with only elementary local factors. This lands directly in the classical regulator/class-number and Dirichlet-`L(1)` metric package, rather than producing a critical-line spectral statistic.

## 5. Prior-art and novelty audit

No novelty is claimed for the analytic-number-theory ingredients.

- PC-025 already records the classical identity expressing the multiplicative Fourier transform of `a -> log|1-zeta_f^a|` through `tau(overline chi)L(1,chi)` for primitive even characters. The source anchor is Montgomery--Vaughan, *The Bateman--Chowla functions* (2026), which states the standard primitive-character log-sine formula explicitly.
- Washington, *Introduction to Cyclotomic Fields*, and Sinnott's circular-unit work are already anchored in `SOURCES.md`; ratios of the chord factors in (4) lie in the classical cyclotomic/circular-unit regulator setting.
- The cyclotomic discriminant formula used in (6)--(7) is already a source dependency of this line.
- Kurshan--Odlyzko and Bzdega--Herrera-Poyatos--Moree, already used by PC-215--PC-216, delimit the classical root-of-unity value side of the same calculation.

The project-local content is the exact scope reduction: the metric datum that PC-216 correctly left outside diagonal similarity is itself a finite induced-character transform of classical anchored log-chord fields. The local factor in (11) is obtained by CRT induction and a finite divisor product; it does not define a new `L`-function or a new cyclotomic invariant.

A directed external audit found the standard primitive log-sine/`L(1)` identity and the established cyclotomic-root-value literature, but no evidence that this particular PC-216 packet organization constitutes an independent known operator theorem. That absence is not used as a novelty claim: equations (4), (9), and the character diagonalization make the reduction elementary from classical ingredients.

## 6. Exact boundary for the next step

This finding closes the chain

\[
\text{PC-215 high-body coefficient packet}
\longrightarrow
\text{PC-216 diagonal-similarity metric defect}
\longrightarrow
\text{singular-value / packetwise metric spectrum}
\longrightarrow
\text{new RH carrier}.
\]

At fixed reduced conductor `d`, both the phase/eigenvalue information of PC-216 and the surviving modulus/singular-value information of PC-217 are now classified: the first is pure-gauge residue permutation data, while the second is a finite even Dirichlet-`L(1)` packet with explicit local factors. Neither supplies a spectral parameter, gamma factor, `s<->1-s` symmetry, critical line, or explicit-formula zero term.

The result must not be overextended. The full mixed-mask operator

\[
T_N=P_NM_{g_N}P_N|_{E_N}
\]

simultaneously sums many proper-divisor conductors `d`, each with its own space `U(d)` and derivative potential `eta_d`. PC-217 does not exhibit a common unitary gauge for that assembly and does not collapse PC-215's exact growing locality `omega(N)-1`. A legitimate continuation must therefore keep several conductor packets coupled at once and test a genuinely collective invariant; repeating eigenvalue, singular-value, or finite-difference analysis on one packet is now exhausted.